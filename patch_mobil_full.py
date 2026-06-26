s = open('gecit-mobil.html', encoding='utf-8').read()

# 1) Device ID ekle + biometric teklif
old1 = "  try{var lg=await api('/personnel/login-dob',{method:'POST',body:{tc:tc,dob:dob}});token=lg.token;try{localStorage.setItem(TOKKEY,token);}catch(x){}meInfo=lg;e.textContent='';\n    if(lg.approved)enterApp();else show('pending');}catch(err){e.textContent=err.message;}}"

new1 = """  try{
    var did=localStorage.getItem('GECIT_DID');
    if(!did){did=(typeof crypto!=='undefined'&&crypto.randomUUID)?crypto.randomUUID():Math.random().toString(36).slice(2)+Date.now().toString(36);localStorage.setItem('GECIT_DID',did);}
    var lg=await api('/personnel/login-dob',{method:'POST',body:{tc:tc,dob:dob,deviceId:did}});
    token=lg.token;try{localStorage.setItem(TOKKEY,token);}catch(x){}meInfo=lg;e.textContent='';
    if(lg.approved){
      enterApp();
      setTimeout(async function(){
        if(!window.PublicKeyCredential)return;
        try{var ok=await PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable();if(!ok)return;}catch(e){return;}
        var saved=null;try{saved=JSON.parse(localStorage.getItem('GECIT_BIO_'+TENANT));}catch(e){}
        if(!saved&&confirm('Bir sonraki giriste parmak izi / Face ID kullanmak ister misiniz?')){
          try{
            var challenge=new Uint8Array(32);crypto.getRandomValues(challenge);
            var cred=await navigator.credentials.create({publicKey:{challenge:challenge,rp:{name:'Gecit PDKS',id:location.hostname},user:{id:new TextEncoder().encode(tc),name:tc,displayName:lg.ad||tc},pubKeyCredParams:[{alg:-7,type:'public-key'}],authenticatorSelection:{authenticatorAttachment:'platform',userVerification:'required'},timeout:60000}});
            if(cred){localStorage.setItem('GECIT_BIO_'+TENANT,JSON.stringify({credId:btoa(String.fromCharCode(...new Uint8Array(cred.rawId))),tc:tc}));toast('Biyometrik kayit tamamlandi');}
          }catch(e){console.log('Bio iptal');}
        }
      },1500);
    }else show('pending');
  }catch(err){e.textContent=err.message;}}"""

found1 = old1 in s
s = s.replace(old1, new1)

# 2) Biyometrik buton ekle
old2 = '  <button class="btn" onclick="doLogin()">Giriş yap</button>'
new2 = '  <button class="btn" onclick="doLogin()">Giriş yap</button>\n  <button class="btn ghost" id="bio-login-btn" style="display:none;margin-top:8px" onclick="doBioLogin()">👆 Biyometrik ile Giriş</button>'
found2 = old2 in s
s = s.replace(old2, new2)

# 3) Bio fonksiyonları ve başlangıç kontrolü ekle
old3 = "function logout(){"
new3 = """async function doBioLogin(){
  var saved=null;try{saved=JSON.parse(localStorage.getItem('GECIT_BIO_'+TENANT));}catch(e){}
  if(!saved){toast('Once normal giris yapin');return;}
  try{
    var challenge=new Uint8Array(32);crypto.getRandomValues(challenge);
    var credId=Uint8Array.from(atob(saved.credId),function(c){return c.charCodeAt(0);});
    var assertion=await navigator.credentials.get({publicKey:{challenge:challenge,allowCredentials:[{type:'public-key',id:credId,transports:['internal']}],userVerification:'required',timeout:60000}});
    if(assertion&&token){
      var me=await api('/personnel/me',{auth:true});
      meInfo=me;enterApp();
    }
  }catch(e){toast('Biyometrik dogrulama basarisiz');}
}
function logout(){"""
found3 = old3 in s
s = s.replace(old3, new3)

# 4) Sayfa yuklenince bio buton goster
old4 = "connectWS();"
new4 = """connectWS();
// Biyometrik buton kontrolu
(async function(){
  if(!window.PublicKeyCredential)return;
  try{var ok=await PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable();if(!ok)return;}catch(e){return;}
  var saved=null;try{saved=JSON.parse(localStorage.getItem('GECIT_BIO_'+TENANT));}catch(e){}
  if(saved){var btn=document.getElementById('bio-login-btn');if(btn)btn.style.display='block';}
})();"""
found4 = old4 in s
s = s.replace(old4, new4)

open('gecit-mobil.html', 'w', encoding='utf-8').write(s)
print('device+bio:', found1, '| bio-btn:', found2, '| bio-fn:', found3, '| init:', found4)
