# -*- coding: utf-8 -*-
# manager/login ve manager/enter uclarini ekle (coklu-otel yonetici girisi)
p='/home/ubuntu/gecit-backend/server.js'
s=open(p,encoding='utf-8').read()

if 'MANAGER_LOGIN_v1' in s:
    print("Zaten var")
    raise SystemExit

# hotel/login ucundan ONCE ekle (anchor: app.post('/api/hotel/login')
anchor="app.post('/api/hotel/login', (req, res) => {"

inject="""/* MANAGER_LOGIN_v1: coklu-otel yonetici girisi - kullanici+sifre ile yetkili tenantlari dondur */
app.post('/api/manager/login', (req, res) => {
  const { username, password } = req.body || {};
  if (!username || !password) return res.status(400).json({ error: 'Kullanici adi ve sifre gerekli' });
  const u = D.db.prepare('SELECT * FROM manager_users WHERE username=?').get(username);
  if (!u || !D.bcrypt.compareSync(password, u.pass_hash))
    return res.status(401).json({ error: 'Hatali kullanici adi veya sifre' });
  const access = D.db.prepare('SELECT tenant_id, role FROM manager_access WHERE username=?').all(username);
  if (!access.length) return res.status(403).json({ error: 'Hicbir isletmeye yetkiniz yok' });
  const isletmeler = access.map(function(a){
    let name = a.tenant_id;
    try {
      const t = D.db.prepare('SELECT name FROM tenants WHERE id=?').get(a.tenant_id);
      if (t && t.name) name = t.name;
      const ts = D.db.prepare('SELECT settings FROM tenant_settings WHERE tenant_id=?').get(a.tenant_id);
      if (ts && ts.settings) { const sd = JSON.parse(ts.settings); if (sd && sd.general && sd.general.name) name = sd.general.name; }
    } catch(e){}
    return { tenant: a.tenant_id, name: name, role: a.role };
  });
  res.json({ ok: true, name: u.name, isletmeler: isletmeler });
});
/* MANAGER_ENTER_v1: secilen tenant icin panel token'i uret (yetki kontrollu) */
app.post('/api/manager/enter', (req, res) => {
  const { username, password, tenant } = req.body || {};
  if (!username || !password || !tenant) return res.status(400).json({ error: 'Eksik bilgi' });
  const u = D.db.prepare('SELECT * FROM manager_users WHERE username=?').get(username);
  if (!u || !D.bcrypt.compareSync(password, u.pass_hash))
    return res.status(401).json({ error: 'Hatali kullanici adi veya sifre' });
  const acc = D.db.prepare('SELECT * FROM manager_access WHERE username=? AND tenant_id=?').get(username, tenant);
  if (!acc) return res.status(403).json({ error: 'Bu isletmeye yetkiniz yok' });
  let tenantName = tenant;
  try {
    const t = D.db.prepare('SELECT name FROM tenants WHERE id=?').get(tenant);
    if (t && t.name) tenantName = t.name;
    const ts = D.db.prepare('SELECT settings FROM tenant_settings WHERE tenant_id=?').get(tenant);
    if (ts && ts.settings) { const sd = JSON.parse(ts.settings); if (sd && sd.general && sd.general.name) tenantName = sd.general.name; }
  } catch(e){}
  res.json({ token: issue({ role: 'hotel', tenant: tenant, username: username, name: u.name }), tenant: tenant, name: u.name, tenant_name: tenantName });
});
app.post('/api/hotel/login', (req, res) => {"""

n=s.count(anchor)
print("Anchor eslesme:",n)
if n==1:
    s=s.replace(anchor,inject,1)
    open(p,'w',encoding='utf-8').write(s)
    print("KAYDEDILDI - MANAGER_LOGIN_v1 + MANAGER_ENTER_v1")
else:
    print("HATA - iptal ("+str(n)+")")
