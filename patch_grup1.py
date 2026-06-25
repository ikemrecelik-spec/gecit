import re

s = open('server.js', encoding='utf-8').read()
db = open('db.js', encoding='utf-8').read()

# ============================================================
# 1) db.js - calculateMola fonksiyonu ekle
# ============================================================
old_db = """const todayStr = () => new Date().toISOString().slice(0, 10);"""
new_db = """const todayStr = () => new Date().toISOString().slice(0, 10);

// 4857 sayili Is Kanunu Madde 68 - Kademeli mola kesintisi
function calculateMola(giris, cikis) {
  if (!giris || !cikis) return 0;
  const gp = giris.split(':').map(Number);
  const cp = cikis.split(':').map(Number);
  let mins = (cp[0]*60+cp[1]) - (gp[0]*60+gp[1]);
  if (mins < 0) mins += 1440;
  if (mins <= 240) return 15;       // 4 saat ve alti: 15 dk
  if (mins <= 450) return 30;       // 4-7.5 saat: 30 dk
  return 60;                         // 7.5 saatten fazla: 1 saat
}

// Gece calismasi tespiti - surenin yarisi 20:00-06:00 araligindaysa
function detectGeceCalismasi(giris, cikis) {
  if (!giris || !cikis) return false;
  const gp = giris.split(':').map(Number);
  const cp = cikis.split(':').map(Number);
  let totalMins = (cp[0]*60+cp[1]) - (gp[0]*60+gp[1]);
  if (totalMins < 0) totalMins += 1440;
  // Gece araligi: 20:00 (1200 dk) - 06:00 (360 dk)
  let geceMins = 0;
  for (let i = 0; i < totalMins; i++) {
    const t = (gp[0]*60 + gp[1] + i) % 1440;
    if (t >= 1200 || t < 360) geceMins++;
  }
  return geceMins > totalMins / 2;
}
"""
print('1) calculateMola bulundu:', old_db in db)
db = db.replace(old_db, new_db)

# module.exports'a ekle
old_exports = "  db, bcrypt, detectShift, todayStr, nextSicil,"
new_exports = "  db, bcrypt, detectShift, todayStr, nextSicil, calculateMola, detectGeceCalismasi,"
print('1b) exports bulundu:', old_exports in db)
db = db.replace(old_exports, new_exports)

open('db.js', 'w', encoding='utf-8').write(db)
print('db.js OK')

# ============================================================
# 2) server.js - puantaj endpoint: dinamik ? ve mola
# ============================================================
old_puantaj = """      if(hasAtt){code='X';work++;}
      else if(lv){code=LEAVE_CODE[lv.type]||'Yi';leaveD++;}
      else if(shiftCode&&SHIFT_LEAVE_CODES.includes(shiftCode)){code=shiftCode;if(shiftCode!=='HT'&&shiftCode!=='OFF')leaveD++;}
      days[d]=code;
    }
    return {sicil:e.sicil,ad:e.ad,dep:e.dep,days,work,leaveD};"""

new_puantaj = """      if(hasAtt){
        // Calisma suresi kontrolu
        const attRow = att.find(r=>r.tc===e.tc&&r.day===ds&&r.giris);
        if(attRow && attRow.giris && attRow.cikis) {
          const gp=attRow.giris.split(':').map(Number);
          const cp=attRow.cikis.split(':').map(Number);
          let mins=(cp[0]*60+cp[1])-(gp[0]*60+gp[1]);
          if(mins<0)mins+=1440;
          const mola=D.calculateMola(attRow.giris,attRow.cikis);
          const netMins=mins-mola;
          // Shift planindaki vardiyanin beklenen suresi
          const plannedCode=shiftCode;
          let minRequired=450; // varsayilan 7.5 saat
          if(settingsShifts && plannedCode) {
            const shKey=plannedCode.split(' ')[0];
            const shDef=settingsShifts.find(s=>s.code===shKey);
            if(shDef && shDef.start && shDef.end) {
              const sp=shDef.start.split(':').map(Number);
              const ep=shDef.end.split(':').map(Number);
              let shMins=(ep[0]*60+ep[1])-(sp[0]*60+sp[1]);
              if(shMins<0)shMins+=1440;
              minRequired=shMins-mola;
            }
          }
          // HT gununde calisma - BÇ onayliysa BÇ, yoksa X
          if(shiftCode==='HT') {
            const htApproval=approvalsMap[e.tc] && approvalsMap[e.tc][ds];
            code = (htApproval==='onaylandi') ? 'BÇ' : 'X';
          } else {
            code = netMins >= minRequired ? 'X' : '?';
          }
          // Gece calismasi flag
          if(D.detectGeceCalismasi(attRow.giris,attRow.cikis)) {
            e._geceCalisma = (e._geceCalisma||0)+1;
          }
        } else {
          // Cikis yok - sadece giris var
          if(shiftCode==='HT') code='X'; else code='X';
        }
        work++;
      }
      else if(lv){code=LEAVE_CODE[lv.type]||'Yi';leaveD++;}
      else if(shiftCode&&SHIFT_LEAVE_CODES.includes(shiftCode)){code=shiftCode;if(shiftCode!=='HT'&&shiftCode!=='OFF')leaveD++;}
      days[d]=code;
    }
    return {sicil:e.sicil,ad:e.ad,dep:e.dep,days,work,leaveD,geceCalisma:e._geceCalisma||0};"""

print('2) puantaj bulundu:', old_puantaj in s)
s = s.replace(old_puantaj, new_puantaj)

# ============================================================
# 3) server.js - puantaj endpoint basina settings ve approvals ekle
# ============================================================
old_puantaj_start = """  const [y,mo] = month.split('-').map(Number); const dim = new Date(y,mo,0).getDate(); const monthPad=String(y)+'-'+String(mo).padStart(2,'0');
  // Shift planini oku - o ay icindeki tum haftalari getir"""

new_puantaj_start = """  const [y,mo] = month.split('-').map(Number); const dim = new Date(y,mo,0).getDate(); const monthPad=String(y)+'-'+String(mo).padStart(2,'0');
  // Ayarlardan vardiya tanımlarını al
  const settingsRow2 = D.db.prepare('SELECT settings FROM tenant_settings WHERE tenant_id=?').get(t);
  const settingsObj = settingsRow2 ? JSON.parse(settingsRow2.settings) : {};
  const settingsShifts = settingsObj.shifts || [];
  // Onaylanan HT calismalarini al
  const approvalRows = D.db.prepare("SELECT tc, day, status FROM att_approvals WHERE tenant_id=? AND type='ht_work'").all(t);
  const approvalsMap = {};
  approvalRows.forEach(r => { if(!approvalsMap[r.tc])approvalsMap[r.tc]={}; approvalsMap[r.tc][r.day]=r.status; });
  // Shift planini oku - o ay icindeki tum haftalari getir"""

print('3) puantaj_start bulundu:', old_puantaj_start in s)
s = s.replace(old_puantaj_start, new_puantaj_start)

# ============================================================
# 4) server.js - istten cikista shift planini temizle
# ============================================================
old_status = """app.post('/api/:tenant/employees/:tc/status', authTenant, (req, res) => {
  const b = req.body || {};
  const status = b.status === 'pasif' ? 'pasif' : 'aktif';
  D.setEmpStatus(req.params.tenant, req.params.tc, status);
  if (status === 'pasif') {
    D.db.prepare('UPDATE accounts SET cikis_tarihi=?, cikis_kodu=?, cikis_not=? WHERE tenant_id=? AND tc=?')
      .run(b.cikis_tarihi || new Date().toISOString().slice(0,10), b.cikis_kodu || '', b.cikis_not || '', req.params.tenant, req.params.tc);
  } else {
    D.db.prepare('UPDATE accounts SET cikis_tarihi=NULL, cikis_kodu=NULL, cikis_not=NULL WHERE tenant_id=? AND tc=?')
      .run(req.params.tenant, req.params.tc);
  }
  broadcast(req.params.tenant, 'employees'); res.json({ ok: true });
});"""

new_status = """app.post('/api/:tenant/employees/:tc/status', authTenant, (req, res) => {
  const b = req.body || {};
  const status = b.status === 'pasif' ? 'pasif' : 'aktif';
  D.setEmpStatus(req.params.tenant, req.params.tc, status);
  if (status === 'pasif') {
    D.db.prepare('UPDATE accounts SET cikis_tarihi=?, cikis_kodu=?, cikis_not=? WHERE tenant_id=? AND tc=?')
      .run(b.cikis_tarihi || new Date().toISOString().slice(0,10), b.cikis_kodu || '', b.cikis_not || '', req.params.tenant, req.params.tc);
    // Cikis tarihinden sonraki shift planlarini temizle
    const cikisDate = b.cikis_tarihi || new Date().toISOString().slice(0,10);
    const shiftRows = D.db.prepare('SELECT * FROM shift_plan WHERE tenant_id=? AND tc=?').all(req.params.tenant, req.params.tc);
    shiftRows.forEach(row => {
      const days = JSON.parse(row.days || '{}');
      let changed = false;
      Object.keys(days).forEach(date => {
        if (date > cikisDate) { days[date] = '-'; changed = true; }
      });
      if (changed) D.db.prepare('UPDATE shift_plan SET days=? WHERE id=?').run(JSON.stringify(days), row.id);
    });
  } else {
    D.db.prepare('UPDATE accounts SET cikis_tarihi=NULL, cikis_kodu=NULL, cikis_not=NULL WHERE tenant_id=? AND tc=?')
      .run(req.params.tenant, req.params.tc);
  }
  broadcast(req.params.tenant, 'employees'); res.json({ ok: true });
});"""

print('4) status bulundu:', old_status in s)
s = s.replace(old_status, new_status)

# ============================================================
# 5) server.js - att_approvals'a approved_by/at ekle
# ============================================================
old_approve = """app.put('/api/:tenant/approvals/:id', authTenant, (req, res) => {
  const { status, note } = req.body || {};
  if (!['onaylandi','reddedildi'].includes(status)) return res.status(400).json({error:'Gecersiz durum'});
  const appr = D.db.prepare('SELECT * FROM att_approvals WHERE id=? AND tenant_id=?').get(req.params.id, req.params.tenant);
  if (!appr) return res.status(404).json({error:'Bulunamadi'});
  D.db.prepare('UPDATE att_approvals SET status=?, note=?, approved_by=? WHERE id=?')
    .run(status, note||'', req.session?.name||'IK', req.params.id);"""

new_approve = """app.put('/api/:tenant/approvals/:id', authTenant, (req, res) => {
  const { status, note } = req.body || {};
  if (!['onaylandi','reddedildi'].includes(status)) return res.status(400).json({error:'Gecersiz durum'});
  const appr = D.db.prepare('SELECT * FROM att_approvals WHERE id=? AND tenant_id=?').get(req.params.id, req.params.tenant);
  if (!appr) return res.status(404).json({error:'Bulunamadi'});
  const approvedBy = req.session?.name || 'IK';
  const approvedAt = new Date().toISOString();
  D.db.prepare('UPDATE att_approvals SET status=?, note=?, approved_by=?, approved_at=? WHERE id=?')
    .run(status, note||'', approvedBy, approvedAt, req.params.id);"""

print('5) approve bulundu:', old_approve in s)
s = s.replace(old_approve, new_approve)

open('server.js', 'w', encoding='utf-8').write(s)
print('server.js OK')
