s = open('db.js', encoding='utf-8').read()
old = "listEmployees: (t) => db.prepare(\"SELECT tc,ad,sicil,dep,gorev,status,device,dob,tel,cins,dir,giris FROM accounts WHERE tenant_id=? AND approved=1 ORDER BY status, sicil\").all(t),"
new = "listEmployees: (t) => db.prepare(\"SELECT tc,ad,sicil,dep,gorev,status,device,dob,tel,cins,dir,giris,rol,rol_departmanlar,cikis_tarihi,cikis_kodu,cikis_not FROM accounts WHERE tenant_id=? AND approved=1 ORDER BY status, sicil\").all(t),"
found = old in s
s = s.replace(old, new)
open('db.js', 'w', encoding='utf-8').write(s)
print('bulundu:', found)
