s = open('server.js', encoding='utf-8').read()
old = "app.put('/api/:tenant/attendance/:id', authTenant, (req, res) => {"
new = """app.post('/api/:tenant/attendance', authTenant, (req, res) => {
  const t = req.params.tenant;
  const b = req.body || {};
  if (!b.tc || !b.day || !b.giris) return res.status(400).json({error:'tc, day ve giris gerekli'});
  const emp = D.getAccount(t, b.tc);
  if (!emp) return res.status(404).json({error:'Personel bulunamadi'});
  D.db.prepare('INSERT INTO attendance (tenant_id,sicil,tc,ad,gorev,vardiya,giris,cikis,off,fm,izin,dep,day,ts) VALUES (?,?,?,?,?,?,?,?,0,0,?,?,?,?)').run(t, emp.sicil, b.tc, emp.ad, emp.gorev, b.vardiya||'Manuel', b.giris, b.cikis||null, '', emp.dep, b.day, Date.now());
  broadcast(t, 'attendance');
  res.json({ok:true});
});

app.put('/api/:tenant/attendance/:id', authTenant, (req, res) => {"""
print('bulundu:', old in s)
s = s.replace(old, new)
open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
