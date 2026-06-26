s = open('server.js', encoding='utf-8').read()

# login-dob endpoint'ine device kontrolu ekle
old1 = """app.post('/api/:tenant/personnel/login-dob', (req, res) => {
  const { tenant } = req.params; const { tc, dob } = req.body || {};
  const a = D.getAccount(tenant, tc);
  if (!a) return res.status(401).json({ error: 'Bu TC ile kayıt bulunamadı. İK ile iletişime geçin.' });
  if (a.dob !== dob) return res.status(401).json({ error: 'Doğum tarihi eşleşmiyor' });
  res.json({ token: issue({ role: 'personnel', tenant, tc, name: a.ad }), approved: !!a.approved, ad: a.ad, sicil: a.sicil, dep: a.dep, gorev: a.gorev });
});"""

new1 = """app.post('/api/:tenant/personnel/login-dob', (req, res) => {
  const { tenant } = req.params; const { tc, dob, deviceId } = req.body || {};
  const a = D.getAccount(tenant, tc);
  if (!a) return res.status(401).json({ error: 'Bu TC ile kayit bulunamadi. IK ile iletisime gecin.' });
  if (a.dob !== dob) return res.status(401).json({ error: 'Dogum tarihi eslesmedi' });
  // Cihaz kontrolu
  if (deviceId) {
    if (a.device && a.device !== deviceId) {
      return res.status(403).json({ error: 'Bu hesap baska bir cihaza kayitli. IK ile iletisime gecin.' });
    }
    if (!a.device) {
      D.db.prepare('UPDATE accounts SET device=? WHERE tenant_id=? AND tc=?').run(deviceId, tenant, tc);
    }
  }
  res.json({ token: issue({ role: 'personnel', tenant, tc, name: a.ad }), approved: !!a.approved, ad: a.ad, sicil: a.sicil, dep: a.dep, gorev: a.gorev });
});"""

print('login-dob bulundu:', old1 in s)
s = s.replace(old1, new1)
open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
