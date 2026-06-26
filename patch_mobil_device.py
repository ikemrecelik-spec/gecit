s = open('gecit-mobil.html', encoding='utf-8').read()

old = "var lg=await api('/personnel/login-dob',{method:'POST',body:{tc:tc,dob:dob}});"
new = "var did=localStorage.getItem('GECIT_DID');if(!did){did=crypto.randomUUID?crypto.randomUUID():Math.random().toString(36).slice(2)+Date.now().toString(36);localStorage.setItem('GECIT_DID',did);}var lg=await api('/personnel/login-dob',{method:'POST',body:{tc:tc,dob:dob,deviceId:did}});"

print('bulundu:', old in s)
s = s.replace(old, new)
open('gecit-mobil.html', 'w', encoding='utf-8').write(s)
print('OK')
