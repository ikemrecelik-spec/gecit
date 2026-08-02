# -*- coding: utf-8 -*-
# doLogin'de token'i localStorage'a kaydeder (yenilemede kaybolmasin)
p='/home/ubuntu/gecit-backend/public/v2.html'
lines=open(p,encoding='utf-8').read().split('\n')

if any('TOKEN_SAVE_v1' in ln for ln in lines):
    print("Zaten yapilmis")
    raise SystemExit

# doLogin icindeki 'window.GECIT._token=d.token;' satirini bul
# (sa-login/demo degil, gercek hotel login)
target=None
for i,ln in enumerate(lines):
    if 'window.GECIT._token=d.token;' in ln:
        # doLogin icindeki ilk gecen (satir ~767)
        target=i
        break

if target is None:
    print("HATA: token satiri bulunamadi")
    raise SystemExit

# girinti hesapla
raw=lines[target]
indent=raw[:len(raw)-len(raw.lstrip())]

eklenecek=[
    indent+'/* TOKEN_SAVE_v1 */',
    indent+'if(d.tenant)window.GECIT._tenant=d.tenant;',
    indent+'try{localStorage.setItem("GECIT_TOK_"+window.GECIT._tenant,d.token);}catch(_e){}',
]
lines[target+1:target+1]=eklenecek
open(p,'w',encoding='utf-8').write('\n'.join(lines))
print("KAYDEDILDI - satir",target+1,"sonrasina token kaydi eklendi")
