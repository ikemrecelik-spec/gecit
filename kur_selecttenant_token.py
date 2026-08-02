# -*- coding: utf-8 -*-
# selectTenant ve superadmin login'de token'i localStorage'a kaydet
p='/home/ubuntu/gecit-backend/public/v2.html'
s=open(p,encoding='utf-8').read()

if 'SELECTTENANT_TOKEN_v1' in s:
    print("Zaten yapilmis")
    raise SystemExit

cnt=0

# 1) selectTenant: _tenant set edilince token'i da localStorage'a yaz
old="  function selectTenant(t){ window.GECIT._tenant=String(t.id); window.GECIT._api=API_BASE;"
new="  function selectTenant(t){ window.GECIT._tenant=String(t.id); window.GECIT._api=API_BASE; /* SELECTTENANT_TOKEN_v1 */ try{if(window.GECIT._token)localStorage.setItem('GECIT_TOK_'+window.GECIT._tenant,window.GECIT._token);}catch(_e){}"
if s.count(old)==1:
    s=s.replace(old,new); cnt+=1; print("selectTenant OK")
else:
    print("selectTenant ATLANDI ("+str(s.count(old))+")")

open(p,'w',encoding='utf-8').write(s)
print("KAYDEDILDI - toplam",cnt,"degisiklik")
