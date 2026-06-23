s = open('server.js', encoding='utf-8').read()

# Punch baslangicini ve bitisini bul
START = "app.post('/api/:tenant/attendance/punch'"
END_MARKER = "app.post('/api/:tenant/leaves/:id/approve'"

start_idx = s.find(START)
end_idx = s.find(END_MARKER)

if start_idx < 0 or end_idx < 0:
    print('BULUNAMADI start:', start_idx, 'end:', end_idx)
else:
    print('bulundu, uzunluk:', end_idx - start_idx)
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
    s = s[:start_idx] + new_punch + s[end_idx:]
    open('server.js', 'w', encoding='utf-8').write(s)
    print('OK')
