for fn in ['v2.html','panel.html','gecit-site-v1.html']:
    s = open(fn, encoding='utf-8').read()
    
    old = """// Sifre sifirlama token kontrolu
(function(){
  var resetToken=Q.get('reset');
  if(!resetToken)return;
  // Login ekranini gizle, reset formu goster
  document.addEventListener('DOMContentLoaded',function(){
    var loginBox=document.querySelector('#login .loginbox');
    if(!loginBox)return;
    loginBox.innerHTML='<div class=\"logo\">G</div><h1>Sifre Sifirla</h1><p>Yeni sifrenizi belirleyin.</p><div class=\"field\"><label>Yeni Sifre</label><input id=\"rst-pw\" type=\"password\" placeholder=\"••••••\"></div><div class=\"field\"><label>Yeni Sifre Tekrar</label><input id=\"rst-pw2\" type=\"password\" placeholder=\"••••••\"></div><div id=\"rst-err\" style=\"color:var(--danger);font-size:12px;margin-bottom:8px\"></div><button class=\"loginbtn\" onclick=\"doReset()\">Sifremi Guncelle</button>';
    document.getElementById('login').style.display='grid';
    document.getElementById('superadmin').style.display='none';"""
    
    new = """// Sifre sifirlama token kontrolu
(function(){
  var resetToken=Q.get('reset');
  if(!resetToken)return;
  function showResetForm(){
    var loginBox=document.querySelector('#login .loginbox');
    if(!loginBox){setTimeout(showResetForm,100);return;}
    loginBox.innerHTML='<div class="logo">G</div><h1 style="font-family:Space Grotesk">Sifre Sifirla</h1><p style="color:var(--muted);font-size:13px">Yeni sifrenizi belirleyin.</p><div class="field"><label>Yeni Sifre</label><input id="rst-pw" type="password" placeholder="En az 6 karakter" style="width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:9px;padding:11px 13px;color:var(--text);font-size:14px;outline:none"></div><div class="field" style="margin-top:10px"><label>Yeni Sifre Tekrar</label><input id="rst-pw2" type="password" placeholder="Tekrar girin" style="width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:9px;padding:11px 13px;color:var(--text);font-size:14px;outline:none"></div><div id="rst-err" style="color:var(--danger);font-size:12px;margin:8px 0"></div><button onclick="window.doReset()" class="loginbtn" style="margin-top:8px">Sifremi Guncelle</button>';
    document.getElementById('login').style.display='grid';
    try{document.getElementById('superadmin').style.display='none';}catch(e){}
    try{document.getElementById('app').style.display='none';}catch(e){}"""
    
    found = old in s
    s = s.replace(old, new)
    
    # doReset fonksiyonundaki !resetToken ve !r.ok satirlarini duzelt
    old2 = "    window.doReset=async function(){\n      var pw=document.getElementById('rst-pw').value;\n      var pw2=document.getElementById('rst-pw2').value;\n      var err=document.getElementById('rst-err');\n      if(pw.length<6){err.textContent='Sifre en az 6 karakter olmali';return;}\n      if(pw!==pw2){err.textContent='Sifreler eslesmedi';return;}\n      try{\n        var r=await fetch('https://gecitpdks.duckdns.org/api/hotel/reset-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({token:''+resetToken,newPass:pw})});\n        var d=await r.json();\n        if(!r.ok)throw new Error(d.error||'Hata');\n        err.style.color='var(--mint)';err.textContent='Sifreniz guncellendi! Giris yapabilirsiniz.';\n        setTimeout(function(){window.location.href=window.location.pathname;},2000);\n      }catch(e){err.textContent=e.message;}\n    };\n  });\n})();"
    new2 = """    window.doReset=async function(){
      var pw=document.getElementById('rst-pw').value;
      var pw2=document.getElementById('rst-pw2').value;
      var err=document.getElementById('rst-err');
      if(pw.length<6){err.textContent='Sifre en az 6 karakter olmali';return;}
      if(pw!==pw2){err.textContent='Sifreler eslesmedi';return;}
      err.textContent='Guncelleniyor...';err.style.color='var(--muted)';
      try{
        var r=await fetch('https://gecitpdks.duckdns.org/api/hotel/reset-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({token:resetToken,newPass:pw})});
        var d=await r.json();
        if(r.status>=400)throw new Error(d.error||'Hata');
        err.style.color='var(--mint)';err.textContent='Sifreniz guncellendi! Giris sayfasina yonlendiriliyorsunuz...';
        setTimeout(function(){window.location.href=window.location.pathname;},2500);
      }catch(e){err.textContent=e.message;err.style.color='var(--danger)';}
    };
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',showResetForm);}
  else{showResetForm();}
})();"""
    found2 = old2 in s
    s = s.replace(old2, new2)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> form:', found, '| doReset:', found2)
