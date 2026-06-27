s = open('server.js', encoding='utf-8').read()

new_routes = """
// ============ PROFİL YÖNETİMİ ============
// Profil bilgisi
app.get('/api/hotel/profile', auth(['hotel']), (req, res) => {
  const u = D.db.prepare('SELECT username, name, email, tenant_id FROM hotel_users WHERE username=?').get(req.session.username);
  if (!u) return res.status(404).json({error:'Kullanici bulunamadi'});
  res.json(u);
});

// Profil guncelle (email)
app.put('/api/hotel/profile', auth(['hotel']), (req, res) => {
  const { email, name } = req.body || {};
  D.db.prepare('UPDATE hotel_users SET email=?, name=? WHERE username=?').run(email||null, name||req.session.name, req.session.username);
  res.json({ok:true});
});

// Sifre degistir
app.put('/api/hotel/password', auth(['hotel']), (req, res) => {
  const { oldPass, newPass } = req.body || {};
  if (!newPass || newPass.length < 6) return res.status(400).json({error:'Yeni sifre en az 6 karakter olmali'});
  const u = D.db.prepare('SELECT * FROM hotel_users WHERE username=?').get(req.session.username);
  if (!u) return res.status(404).json({error:'Kullanici bulunamadi'});
  if (!D.bcrypt.compareSync(oldPass || '', u.pass_hash)) return res.status(401).json({error:'Mevcut sifre yanlis'});
  const newHash = D.bcrypt.hashSync(newPass, 10);
  D.db.prepare('UPDATE hotel_users SET pass_hash=? WHERE username=?').run(newHash, req.session.username);
  res.json({ok:true});
});

"""

marker = "app.get('/health'"
print('bulundu:', marker in s)
s = s.replace(marker, new_routes + marker, 1)
open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
