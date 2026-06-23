s = open('server.js', encoding='utf-8').read()

# Bozuk punch fonksiyonunu tamamen temizleyip yeniden yazalim
import re

# Punch endpoint'ini bul ve temizle - bastan sona
old_punch = re.search(r"app\.post\('/api/:tenant/attendance/punch'.*?(?=app\.post\('/api/:tenant/leaves/:id/approve')|(?=app\.get\('/health'))", s, re.DOTALL)
if old_punch:
    print('punch bulundu, uzunluk:', len(old_punch.group(0)))
    new_punch = """app.post('/api/:tenant/attendance/punch', auth(['personnel']), (req, res) => {
  const { tenant } = req.params; const tc = req.session.tc;
  const a = D.getAccount(tenant, tc);
  if (!a || !a.approved) return res.status(403).json({ error: 'Hesap henuz onaylanmadi' });
  if (!a.sicil) { const sicil = 2700+Math.floor(Math.random()*300); D.approveAccount(tenant,tc,sicil,a.dep,a.gorev); a.sicil=sicil; }
  const d = new Date(); const now = String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0');
  const open = D.openAttendance(tenant, tc);
  const action = open ? 'out' : 'in';
  if (open) D.punchOut(open.id, now); else D.punchIn(tenant, a, now);
  broadcast(tenant, 'attendance');
  // HT gununde calisma kontrolu - onaya dusurelim
  try {
    const todayStr = D.todayStr();
    const attRow = D.db.prepare('SELECT * FROM attendance WHERE tenant_id=? AND tc=? AND day=? ORDER BY id DESC LIMIT 1').get(tenant, tc, todayStr);
    if (attRow) {
      const dow = new Date(todayStr).getDay();
      const mon = new Date(todayStr);
      mon.setDate(mon.getDate() - (dow === 0 ? 6 : dow - 1));
      const weekStart = mon.toISOString().slice(0,10);
      const shiftRow = D.db.prepare('SELECT days FROM shift_plan WHERE tenant_id=? AND week_start=? AND tc=?').get(tenant, weekStart, tc);
      if (shiftRow) {
        const days = JSON.parse(shiftRow.days || '{}');
        const todayCode = days[todayStr];
        if (todayCode === 'HT' || todayCode === 'OFF') {
          const existing = D.db.prepare('SELECT id FROM att_approvals WHERE tenant_id=? AND att_id=? AND type=?').get(tenant, attRow.id, 'ht_work');
          if (!existing) {
            D.db.prepare('INSERT INTO att_approvals (tenant_id,att_id,tc,day,type,status,created) VALUES (?,?,?,?,?,?,?)').run(tenant, attRow.id, tc, todayStr, 'ht_work', 'beklemede', Date.now());
            broadcast(tenant, 'approvals');
          }
        }
      }
    }
  } catch(e) { console.log('HT approval error:', e.message); }
  res.json({ ok: true, action, time: now });
});
"""
    s = s[:old_punch.start()] + new_punch + s[old_punch.end():]
    open('server.js', 'w', encoding='utf-8').write(s)
    print('OK')
else:
    print('BULUNAMADI')
