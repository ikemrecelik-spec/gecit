s = open('gecit-mobil.html', encoding='utf-8').read()

# 1) Login ekranına biyometrik buton ekle
old1 = """  <button class="btn" onclick="doLogin()">Giriş yap</button>"""
new1 = """  <button class="btn" onclick="doLogin()">Giriş yap</button>
  <button class="btn ghost" id="bio-login-btn" style="display:none;margin-top:8px" onclick="doBioLogin()">👆 Biyometrik ile Giriş</button>"""
found1 = old1 in s
s = s.replace(old1, new1)

# 2) Biyometrik fonksiyonlari ekle
old2 = """async function doForgot(){"""
new2 = """// Biyometrik kayit ve giris
var BIOKEY='GECIT_BIO_'+TENANT;

async function checkBioSupport(){
  if(!window.PublicKeyCredential)return false;
  try{return await PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable();}catch(e){return false;}
}

async function registerBio(tc, name){
  if(!await checkBioSupport())return;
  try{
    var challenge=new Uint8Array(32);crypto.getRandomValues(challenge);
    var cred=await navigator.credentials.create({publicKey:{
      challenge:challenge,
      rp:{name:'Gecit PDKS',id:location.hostname},
      user:{id:new TextEncoder().encode(tc),name:tc,displayName:name||tc},
      pubKeyCredParams:[{alg:-7,type:'public-key'}],
      authenticatorSelection:{authenticatorAttachment:'platform',userVerification:'required'},
      timeout:60000
    }});
    if(cred){
      localStorage.setItem(BIOKEY,JSON.stringify({credId:btoa(String.fromCharCode(...new Uint8Array(cred.rawId))),tc:tc}));
      toast('Biyometrik kayit tamamlandi');
      document.getElementById('bio-login-btn').style.display='block';
    }
  }catch(e){console.log('Bio kayit iptal:',e.message);}
}

async function doBioLogin(){
  var saved=null; try{saved=JSON.parse(localStorage.getItem(BIOKEY));}catch(e){}
  if(!saved){toast('Once normal giris yapin');return;}
  try{
    var challenge=new Uint8Array(32);crypto.getRandomValues(challenge);
    var credId=Uint8Array.from(atob(saved.credId),function(c){return c.charCodeAt(0);});
    var assertion=await navigator.credentials.get({publicKey:{
      challenge:challenge,
      allowCredentials:[{type:'public-key',id:credId,transports:['internal']}],
      userVerification:'required',
      timeout:60000
    }});
    if(assertion){
      // Biyometrik dogrulandi - TC ile token yenile
      var lg=await api('/personnel/login-bio',{method:'POST',body:{tc:saved.tc,bioToken:btoa(String.fromCharCode(...new Uint8Array(assertion.response.authenticatorData)))}}).catch(async function(){
        // Bio endpoint yoksa dob ile yenile - token gecerliyse direkt gir
        if(token){var me=await api('/personnel/me',{auth:true}); return me;}
        throw new Error('Oturum suresi doldu');
      });
      if(lg){meInfo=lg;if(lg.approved!==undefined){if(lg.approved)enterApp();else show('pending');}else{enterApp();}}
    }
  }catch(e){toast(e.message||'Biyometrik dogrulama basarisiz');console.log(e);}
}

// Biyometrik butonu goster/gizle
(async function(){
  if(await checkBioSupport()){
    var saved=null;try{saved=JSON.parse(localStorage.getItem(BIOKEY));}catch(e){}
    if(saved){var btn=document.getElementById('bio-login-btn');if(btn)btn.style.display='block';}
  }
})();

async function doForgot(){"""
found2 = old2 in s
s = s.replace(old2, new2)

# 3) Basarili giristen sonra biyometrik teklif et
old3 = """    if(lg.approved)enterApp();else show('pending');}catch(err){e.textContent=err.message;}}"""
new3 = """    if(lg.approved){
      enterApp();
      // Biyometrik kayit teklif et
      setTimeout(async function(){
        if(!await checkBioSupport())return;
        var saved=null;try{saved=JSON.parse(localStorage.getItem(BIOKEY));}catch(e){}
        if(!saved&&confirm('Bir sonraki giriste parmak izi / Face ID kullanmak ister misiniz?')){
          await registerBio(tc,lg.ad||tc);
        }
      },1500);
    }else show('pending');}catch(err){e.textContent=err.message;}}"""
found3 = old3 in s
s = s.replace(old3, new3)

open('gecit-mobil.html', 'w', encoding='utf-8').write(s)
print('btn:', found1, '| bio fn:', found2, '| register offer:', found3)
