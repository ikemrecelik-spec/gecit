# -*- coding: utf-8 -*-
# Mobil giris akisini coklu-otel destekli hale getirir
import sys
p='/home/ubuntu/gecit-backend/public/gecit-mobil.html'
s=open(p,encoding='utf-8').read()

if 'COKLU_OTEL_GIRIS_v1' in s:
    print("Zaten monte edilmis - dokunulmadi")
    sys.exit()

# ============ 1) TENANT'i dinamik yap ============
old_init = "var API=(Q.get('api')||'').replace(/\\/$/,''); var TENANT=Q.get('tenant')||'1';\nvar TOKKEY='GECIT_TOK_'+TENANT; var token=null; try{token=localStorage.getItem(TOKKEY);}catch(e){}"

new_init = """var API=(Q.get('api')||'').replace(/\\/$/,'');
/* COKLU_OTEL_GIRIS_v1: TENANT artik dinamik - once URL, sonra hatirlanan, sonra bos */
var TENANT=Q.get('tenant')||localStorage.getItem('GECIT_SON_TENANT')||'';
var TOKKEY='GECIT_TOK_'+TENANT; var token=null; try{if(TENANT)token=localStorage.getItem(TOKKEY);}catch(e){}
var loginCtx={tc:'',dob:'',isletmeler:[]};  /* find sonucu burada tutulur */
function setTenant(t){ TENANT=t; TOKKEY='GECIT_TOK_'+TENANT; try{localStorage.setItem('GECIT_SON_TENANT',t);}catch(e){} }
/* Global (tenant-bagimsiz) API cagrisi - find icin */
async function apiGlobal(path,opts){opts=opts||{};var h={'Content-Type':'application/json'};
  var base=API||''; var r=await fetch(base+path,{method:opts.method||'POST',headers:h,body:opts.body?JSON.stringify(opts.body):undefined});
  var d=null;try{d=await r.json();}catch(e){} if(!r.ok)throw new Error((d&&d.error)||('Sunucu hatasi '+r.status)); return d;}"""

if s.count(old_init)!=1:
    print("HATA: init blogu bulunamadi ("+str(s.count(old_init))+")"); sys.exit(1)
s=s.replace(old_init,new_init)

# ============ 2) Yeni ekranlar: otel-sec + sifre + sifre-belirle ============
# s-login ekranindan SONRA ekle. s-login'i de yeni akisa baglayacagiz.
old_login_screen = """<div class="auth" id="s-login">
  <h1 class="h">Giriş yap</h1><p class="sub">TC kimlik no ve doğum tarihinle gir.</p>
  <div class="field"><label>TC Kimlik No</label><input class="pin mono" id="lg-tc" inputmode="numeric" maxlength="11" placeholder="___________"></div>
  <div class="field"><label>Doğum tarihi</label><input class="pin mono" id="lg-p" inputmode="numeric" maxlength="10" placeholder="gg.aa.yyyy"></div>
  <div class="err" id="lg-err"></div>
  <button class="btn" onclick="doLogin()">Giriş yap</button>
  <button class="link" onclick="show('forgot')">Şifremi unuttum</button>
  <button class="link" onclick="show('splash')">← Geri</button>
</div>"""

new_login_screen = """<div class="auth" id="s-login">
  <h1 class="h">Giriş yap</h1><p class="sub">TC kimlik no ve doğum tarihinle devam et.</p>
  <div class="field"><label>TC Kimlik No</label><input class="pin mono" id="lg-tc" inputmode="numeric" maxlength="11" placeholder="___________"></div>
  <div class="field"><label>Doğum tarihi</label><input class="pin mono" id="lg-p" inputmode="numeric" maxlength="10" placeholder="gg.aa.yyyy"></div>
  <div class="err" id="lg-err"></div>
  <button class="btn" onclick="doFind()">Devam et</button>
  <button class="link" onclick="show('forgot')">Şifremi unuttum</button>
  <button class="link" onclick="show('splash')">← Geri</button>
</div>

<!-- COKLU_OTEL_GIRIS_v1: isletme secim ekrani -->
<div class="auth" id="s-isletme">
  <h1 class="h">İşletme seç</h1><p class="sub">Bu bilgilerle birden fazla işletmede kayıtlısın. Giriş yapmak istediğini seç.</p>
  <div id="isl-list" style="display:flex;flex-direction:column;gap:10px;margin:8px 0"></div>
  <button class="link" onclick="show('login')">← Geri</button>
</div>

<!-- COKLU_OTEL_GIRIS_v1: sifre gir ekrani -->
<div class="auth" id="s-pass">
  <h1 class="h">Şifre</h1><p class="sub" id="pass-sub">Şifreni gir.</p>
  <div class="field"><label>Şifre</label><input class="pin" id="pass-p" type="password" placeholder="••••••"></div>
  <div class="err" id="pass-err"></div>
  <button class="btn" onclick="doPassLogin()">Giriş yap</button>
  <button class="link" onclick="backToStart()">← Geri</button>
</div>

<!-- COKLU_OTEL_GIRIS_v1: ilk giris sifre belirle ekrani -->
<div class="auth" id="s-setpass2">
  <h1 class="h">Şifre belirle</h1><p class="sub" id="setpass-sub">İlk girişin. Kendine bir şifre oluştur.</p>
  <div class="field"><label>Yeni şifre (en az 4 hane)</label><input class="pin" id="sp2-p1" type="password" placeholder="••••••"></div>
  <div class="field"><label>Şifre tekrar</label><input class="pin" id="sp2-p2" type="password" placeholder="••••••"></div>
  <div class="err" id="sp2-err"></div>
  <button class="btn" onclick="doSetPass2()">Kaydet ve gir</button>
  <button class="link" onclick="backToStart()">← Geri</button>
</div>"""

if s.count(old_login_screen)!=1:
    print("HATA: login ekrani bulunamadi ("+str(s.count(old_login_screen))+")"); sys.exit(1)
s=s.replace(old_login_screen,new_login_screen)

# ============ 3) doLogin'i yeni akis fonksiyonlariyla degistir ============
# Mevcut doLogin'i bul
import re
m=re.search(r'async function doLogin\(\)\{.*?\n\}', s, re.DOTALL)
if not m:
    print("HATA: doLogin fonksiyonu bulunamadi"); sys.exit(1)
old_dologin=m.group(0)

new_funcs = """/* COKLU_OTEL_GIRIS_v1: yeni giris akisi */
async function doFind(){
  var tc=val('lg-tc'),dob=val('lg-p'),e=document.getElementById('lg-err');
  e.textContent='';
  if(!/^[0-9]{11}$/.test(tc)){e.textContent='TC 11 haneli olmalı.';return;}
  if(!/^[0-9]{2}\\.[0-9]{2}\\.[0-9]{4}$/.test(dob)){e.textContent='Doğum tarihi gg.aa.yyyy biçiminde olmalı.';return;}
  try{
    var d=await apiGlobal('/api/personnel/find',{method:'POST',body:{tc:tc,dob:dob}});
    loginCtx.tc=tc; loginCtx.dob=dob; loginCtx.isletmeler=d.isletmeler||[];
    if(loginCtx.isletmeler.length===1){ secIsletme(loginCtx.isletmeler[0]); }
    else{ renderIsletmeler(); show('isletme'); }
  }catch(err){ e.textContent=err.message; }
}
function renderIsletmeler(){
  var box=document.getElementById('isl-list');
  box.innerHTML=loginCtx.isletmeler.map(function(x,i){
    return '<button class="btn ghost" style="justify-content:flex-start;text-align:left" onclick="secIsletmeIdx('+i+')">'
      +'<b>'+x.name+'</b>'+(x.sicil?'<span style="opacity:.6;font-size:12px"> · Sicil '+x.sicil+'</span>':'')+'</button>';
  }).join('');
}
function secIsletmeIdx(i){ secIsletme(loginCtx.isletmeler[i]); }
function secIsletme(isl){
  setTenant(isl.tenant);
  loginCtx.secili=isl;
  if(isl.hasPass){
    document.getElementById('pass-sub').textContent=isl.name+' için şifreni gir.';
    document.getElementById('pass-p').value='';
    document.getElementById('pass-err').textContent='';
    show('pass');
  }else{
    document.getElementById('setpass-sub').textContent=isl.name+' · İlk girişin, kendine şifre oluştur.';
    document.getElementById('sp2-p1').value=''; document.getElementById('sp2-p2').value='';
    document.getElementById('sp2-err').textContent='';
    show('setpass2');
  }
}
function backToStart(){ show('login'); }
async function doPassLogin(){
  var pass=val('pass-p'),e=document.getElementById('pass-err');
  e.textContent='';
  if(!pass){e.textContent='Şifre gir.';return;}
  try{
    var did=getDeviceId();
    var lg=await api('/personnel/login',{method:'POST',body:{tc:loginCtx.tc,pass:pass}});
    token=lg.token; try{localStorage.setItem(TOKKEY,token);}catch(e2){}
    afterLogin(lg);
  }catch(err){ e.textContent=err.message; }
}
async function doSetPass2(){
  var p1=val('sp2-p1'),p2=val('sp2-p2'),e=document.getElementById('sp2-err');
  e.textContent='';
  if(p1.length<4){e.textContent='Şifre en az 4 hane olmalı.';return;}
  if(p1!==p2){e.textContent='Şifreler eşleşmiyor.';return;}
  try{
    /* forgot ucu TC+dogum ile sifre belirlemeye izin veriyor */
    await api('/personnel/forgot',{method:'POST',body:{tc:loginCtx.tc,dob:loginCtx.dob,newpass:p1}});
    var lg=await api('/personnel/login',{method:'POST',body:{tc:loginCtx.tc,pass:p1}});
    token=lg.token; try{localStorage.setItem(TOKKEY,token);}catch(e2){}
    afterLogin(lg);
  }catch(err){ e.textContent=err.message; }
}
function afterLogin(lg){
  meInfo=lg;
  if(lg.approved===false){ show('pending'); return; }
  connectWS();
  enterApp();
}
function getDeviceId(){ try{var k='GECIT_DEVICE';var d=localStorage.getItem(k);if(!d){d='dev-'+Math.random().toString(36).slice(2)+Date.now().toString(36);localStorage.setItem(k,d);}return d;}catch(e){return null;} }"""

s=s.replace(old_dologin,new_funcs)

# ============ 4) marker ekle ============
s=s.replace('<!-- MOBIL_KAYIT_KALDIRILDI_v1 -->','<!-- MOBIL_KAYIT_KALDIRILDI_v1 --><!-- COKLU_OTEL_GIRIS_v1 -->',1)

open(p,'w',encoding='utf-8').write(s)
print("KAYDEDILDI - COKLU_OTEL_GIRIS_v1")
print("Yeni dosya boyutu:", len(s), "karakter")
