s = open('server.js', encoding='utf-8').read()

if "employees/:tc/rol" not in s:
    NEW_ROUTES = '''
// ============ ROL ATAMA ============
app.put('/api/:tenant/employees/:tc/rol', authTenant, (req, res) => {
  const { rol, rolDepartmanlar } = req.body || {};
  if (!['Personel','Şef','İK / Yönetici'].includes(rol)) return res.status(400).json({error:'Geçersiz rol'});
  D.db.prepare('UPDATE accounts SET rol=?, rol_departmanlar=? WHERE tenant_id=? AND tc=?')
    .run(rol, JSON.stringify(rolDepartmanlar||[]), req.params.tenant, req.params.tc);
  broadcast(req.params.tenant, 'employees');
  res.json({ ok: true });
});

'''
    marker = "app.get('/health'"
    s = s.replace(marker, NEW_ROUTES + marker, 1)
    print("rol endpoint eklendi")
else:
    print("zaten var")

# listEmployees zaten dep/gorev donduruyor, rol alanini da eklemek icin db.js'i guncellememiz lazim
open('server.js', 'w', encoding='utf-8').write(s)
