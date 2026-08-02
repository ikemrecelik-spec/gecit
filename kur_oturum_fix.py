# -*- coding: utf-8 -*-
# Oturum dusme bugu - 4 adimda kesin cozum
p='/home/ubuntu/gecit-backend/public/v2.html'
s=open(p,encoding='utf-8').read()

if 'OTURUM_FIX_v1' in s:
    print("Zaten yapilmis")
    raise SystemExit

cnt=0

# --- ADIM 1: Sabit EÇ harflerini temizle ---
old1='place-items:center;font-family:&#39;Space Grotesk&#39;;font-weight:700;font-size:12px;color:#1a1205;flex:0 0 auto">EÇ</div>'
new1='place-items:center;font-family:&#39;Space Grotesk&#39;;font-weight:700;font-size:12px;color:#1a1205;flex:0 0 auto"></div>'
if s.count(old1)==1: s=s.replace(old1,new1); cnt+=1; print("Adim1a (profil-av) OK")
else: print("Adim1a ATLANDI ("+str(s.count(old1))+")")

old1b='box-shadow:0 4px 12px rgba(242,181,59,.3)">EÇ</div>'
new1b='box-shadow:0 4px 12px rgba(242,181,59,.3)"></div>'
if s.count(old1b)==1: s=s.replace(old1b,new1b); cnt+=1; print("Adim1b (profil-menu-av) OK")
else: print("Adim1b ATLANDI ("+str(s.count(old1b))+")")

# --- ADIM 2: Rastgele tenant secen dongucu duzelt ---
old2='''    /* TENANT_FROM_TOKEN_v1: acilista tokeni olan tenanti sec */
    GE._tenant=(function(){
      try{
        for(var i=0;i<localStorage.length;i++){
          var k=localStorage.key(i);
          if(k && k.indexOf('GECIT_TOK_')===0){
            var v=localStorage.getItem(k);
            if(v && v.length>10)return k.substring(10);
          }
        }
      }catch(e){}
      return GE._tenant||'1';
    })();'''
new2='''    /* OTURUM_FIX_v1: rastgele degil, aktif tenant'i sakli anahtardan al */
    GE._tenant=(function(){
      var urlT=Q.get('tenant');
      if(urlT){try{localStorage.setItem('GECIT_CURRENT_TENANT',urlT);}catch(e){}return urlT;}
      try{var sv=localStorage.getItem('GECIT_CURRENT_TENANT');if(sv&&localStorage.getItem('GECIT_TOK_'+sv))return sv;}catch(e){}
      return '1';
    })();'''
if s.count(old2)==1: s=s.replace(old2,new2); cnt+=1; print("Adim2 (tenant secim) OK")
else: print("Adim2 ATLANDI ("+str(s.count(old2))+")")

# --- ADIM 3a: doLogin'de GECIT_CURRENT_TENANT kaydet ---
old3='''      /* TOKEN_SAVE_v1 */
      if(d.tenant)window.GECIT._tenant=d.tenant;
      try{localStorage.setItem("GECIT_TOK_"+window.GECIT._tenant,d.token);}catch(_e){}'''
new3='''      /* TOKEN_SAVE_v1 + OTURUM_FIX_v1 */
      if(d.tenant)window.GECIT._tenant=d.tenant;
      try{localStorage.setItem("GECIT_TOK_"+window.GECIT._tenant,d.token);localStorage.setItem("GECIT_CURRENT_TENANT",window.GECIT._tenant);}catch(_e){}'''
if s.count(old3)==1: s=s.replace(old3,new3); cnt+=1; print("Adim3a (doLogin) OK")
else: print("Adim3a ATLANDI ("+str(s.count(old3))+")")

# --- ADIM 3b: selectTenant'ta da GECIT_CURRENT_TENANT kaydet ---
old3b="function selectTenant(t){ window.GECIT._tenant=String(t.id); window.GECIT._api=API_BASE;"
new3b="function selectTenant(t){ window.GECIT._tenant=String(t.id); window.GECIT._api=API_BASE; /* OTURUM_FIX_v1 */ try{if(window.GECIT._token){localStorage.setItem('GECIT_TOK_'+window.GECIT._tenant,window.GECIT._token);localStorage.setItem('GECIT_CURRENT_TENANT',window.GECIT._tenant);}}catch(_e){}"
if s.count(old3b)==1: s=s.replace(old3b,new3b); cnt+=1; print("Adim3b (selectTenant) OK")
else: print("Adim3b ATLANDI ("+str(s.count(old3b))+")")

open(p,'w',encoding='utf-8').write(s)
print("KAYDEDILDI - OTURUM_FIX_v1 - toplam",cnt,"degisiklik")
