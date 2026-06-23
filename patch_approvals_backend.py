s = open('server.js', encoding='utf-8').read()

NEW_ROUTES = '''
// ============ ONAY SİSTEMİ ============
// Onay listesi
app.get('/api/:tenant/approvals', authTenant, (req, res) => {
  const rows = D.db.prepare(`
    SELECT a.*, acc.ad, acc.dep, acc.gorev, acc.sicil
    FROM att_approvals a
    LEFT JOIN accounts acc ON a.tc = acc.tc AND acc.tenant_id = a.tenant_id
    WHERE a.tenant_id = ? ${req.query.status ? "AND a.status = ?" : ""}
    ORDER BY a.created DESC LIMIT 100
  `).all(req.params.tenant, ...(req.query.status ? [req.query.status] : []));
  res.json(rows);
});

// Onay ver / reddet
app.put('/api/:tenant/approvals/:id', authTenant, (req, res) => {
  const { status, note } = req.body || {};
  if (!['onaylandi','reddedildi'].includes(status)) return res.status(400).json({error:'Gecersiz durum'});
  const appr = D.db.prepare('SELECT * FROM att_approvals WHERE id=? AND tenant_id=?').get(req.params.id, req.params.tenant);
  if (!appr) return res.status(404).json({error:'Bulunamadi'});
  D.db.prepare('UPDATE att_approvals SET status=?, note=?, approved_by=? WHERE id=?')
    .run(status, note||'', req.session?.name||'IK', req.params.id);
  // Onaylanan FM kaydi guncelle
  if (status === 'onaylandi' && appr.type === 'fm') {
    D.db.prepare('UPDATE attendance SET fm=1 WHERE id=?').run(appr.att_id);
  }
  broadcast(req.params.tenant, 'approvals');
  res.json({ok: true});
});

'''

# punch endpoint'ine HT/FM onay otomasyonu ekle
old_punch = """app.post('/api/:tenant/attendance/punch', auth(['personnel']), (req, res) => {"""

# Punch fonksiyonunun tamamını bul ve yeni versiyonla degistir
import re
punch_match = re.search(r"app\.post\('/api/:tenant/attendance/punch'.*?\}\);", s, re.DOTALL)
if punch_match:
    old_punch_full = punch_match.group(0)
    new_punch_full = old_punch_full.rstrip('};').rstrip()
    # Punch sonunda onay olustur
    new_punch_full += """
  // HT gununde calisma veya FM kontrolu - onaya dusurelim
  try {
    const attRow = D.db.prepare('SELECT * FROM attendance WHERE tenant_id=? AND tc=? AND day=? ORDER BY id DESC LIMIT 1').get(tenant, tc, D.todayStr());
    if (attRow && attRow.giris) {
      // Shift planinda bu gun HT var mi?
      const todayStr = D.todayStr();
      const dow = new Date(todayStr).getDay();
      const mon = new Date(todayStr);
      mon.setDate(mon.getDate() - (dow === 0 ? 6 : dow - 1));
      const weekStart = mon.toISOString().slice(0,10);
      const shiftRow = D.db.prepare('SELECT days FROM shift_plan WHERE tenant_id=? AND week_start=? AND tc=?').get(tenant, weekStart, tc);
      if (shiftRow) {
        const days = JSON.parse(shiftRow.days || '{}');
        const todayCode = days[todayStr];
        if (todayCode === 'HT' || todayCode === 'OFF') {
          // HT gununde calisma - onaya dusurelim
          const existing = D.db.prepare('SELECT id FROM att_approvals WHERE tenant_id=? AND att_id=? AND type=?').get(tenant, attRow.id, 'ht_work');
          if (!existing) {
            D.db.prepare('INSERT INTO att_approvals (tenant_id,att_id,tc,day,type,status,created) VALUES (?,?,?,?,?,?,?)').run(tenant, attRow.id, tc, todayStr, 'ht_work', 'beklemede', Date.now());
            broadcast(tenant, 'approvals');
          }
        }
      }
    }
  } catch(e) { console.log('Approval check error:', e.message); }
});"""
    s = s.replace(old_punch_full, new_punch_full)
    print('punch guncellendi')
else:
    print('punch bulunamadi')

marker = "app.get('/health'"
print('marker bulundu:', marker in s)
s = s.replace(marker, NEW_ROUTES + marker, 1)
open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
