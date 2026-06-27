import re

new_block = """(function(){
  var resetToken=Q.get('reset');
  if(!resetToken)return;
  function showResetForm(){
    var loginBox=document.querySelector('#login .loginbox');
    if(!loginBox){setTimeout(showResetForm,100);return;}
    loginBox.innerHTML='<div class="logo">G</div><h1 style="font-family:Space Grotesk">Sifre Sifirla</h1><p style="color:var(--muted);font-size:13px">Yeni sifrenizi belirleyin.</p><div class="field" style="margin-bottom:10px"><label>Yeni Sifre</label><input id="rst-pw" type="password" placeholder="En az 6 karakter" style="width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:9px;padding:11px 13px;color:var(--text);font-size:14px;outline:none;box-sizing:border-box"></div><div class="field" style="margin-bottom:10px"><label>Yeni Sifre Tekrar</label><input id="rst-pw2" type="password" placeholder="Tekrar girin" style="width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:9px;padding:11px 13px;color:var(--text);font-size:14px;outline:none;box-sizing:border-box"></div><div id="rst-err" style="font-size:12px;margin:8px 0"></div><button onclick="window.doReset()" class="loginbtn" style="margin-top:4px">Sifremi Guncelle</button>';
    document.getElementById('login').style.display='grid';
    try{document.getElementById('superadmin').style.display='none';}catch(e){}
    try{document.getElementById('app').style.display='none';}catch(e){}
    window.doReset=async function(){
      var pw=document.getElementById('rst-pw').value;
      var pw2=document.getElementById('rst-pw2').value;
      var err=document.getElementById('rst-err');
      if(pw.length<6){err.textContent='Sifre en az 6 karakter olmali';err.style.color='var(--danger)';return;}
      if(pw!==pw2){err.textContent='Sifreler eslesmedi';err.style.color='var(--danger)';return;}
      err.textContent='Guncelleniyor...';err.style.color='var(--muted)';
      try{
        var r=await fetch('https://gecitpdks.duckdns.org/api/hotel/reset-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({token:resetToken,newPass:pw})});
        var d=await r.json();
        if(r.status>=400)throw new Error(d.error||'Hata');
        err.style.color='var(--mint)';err.textContent='Sifreniz guncellendi! Yonlendiriliyorsunuz...';
        setTimeout(function(){window.location.href=window.location.pathname;},2500);
      }catch(e){err.textContent=e.message;err.style.color='var(--danger)';}
    };
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',showResetForm);}
  else{setTimeout(showResetForm,0);}
})();"""

pattern = re.compile(r'\(function\(\)\{[\s\S]*?var resetToken=Q\.get\(\'reset\'\);[\s\S]*?\}\)\(\);', re.DOTALL)

for fn in ['v2.html','panel.html','gecit-site-v1.html']:
    s = open(fn, encoding='utf-8').read()
    matches = pattern.findall(s)
    print(fn, '- eslesen:', len(matches))
    # Hepsini yeni blok ile degistir, sadece bir tane kalsin
    s2 = pattern.sub('', s)
    # Dogru yere ekle - Q tanimlamasinin hemen ardindan
    s2 = s2.replace('var Q=new URLSearchParams(location.search);', 
                    'var Q=new URLSearchParams(location.search);\n' + new_block, 1)
    open(fn, 'w', encoding='utf-8').write(s2)
    print(fn, 'OK')
