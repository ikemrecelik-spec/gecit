s = open('server.js', encoding='utf-8').read()

old = "app.get('/api/tenants', auth(['operator']), (req, res) => res.json(D.listTenants()));"

new = """app.get('/api/tenants', auth(['operator','hotel']), (req, res) => {
  if(req.session.role==='hotel'){
    const t=D.listTenants().filter(x=>x.id===req.session.tenant);
    return res.json(t);
  }
  res.json(D.listTenants());
});"""

print('bulundu:', old in s)
s = s.replace(old, new)
open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
