reset_code = """
var resetToken=Q.get('reset');
if(resetToken){
  window.addEventListener('DOMContentLoaded',function(){
    var lb=document.querySelector('#login .loginbox');
    if(!lb)return;
    lb.innerHTML='<div class="logo">G</div><h1>Sifre Sifirla</h1><p style="color:var(--muted);font-size:13px">Yeni sifrenizi belirleyin.</p><div class="field"><label>Yeni Sifre</label><input id="rst-pw" type="password" placeholder="En az 6 karakter"></div><div class="field"><label>Yeni Sifre Tekrar</label><input id="rst-pw2" type="password" placeholder="Tekrar girin"></div><div id="rst-err" style="font-size:12px;margin:8px 0"></div><button class="loginbtn" id="rst-btn">Sifremi Guncelle</button>';
    document.getElementById('login').style.display='grid';
    try{document.getElementById('superadmin').style.display='none';}catch(e){}
    try{document.getElementById('app').style.display='none';}catch(e){}
    document.getElementById('rst-btn').addEventListener('click',async function(){
      var pw=document.getElementById('rst-pw').value;
      var pw2=document.getElementById('rst-pw2').value;
      var err=document.getElementById('rst-err');
      if(pw.length<6){err.textContent='Sifre en az 6 karakter olmali';err.style.color='var(--danger)';return;}
      if(pw!==pw2){err.textContent='Sifreler eslesmedi';err.style.color='var(--danger)';return;}
      err.textContent='Guncelleniyor...';err.style.color='var(--muted)';
      try{
        var r=await fetch(location.origin+'/api/hotel/reset-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({token:resetToken,newPass:pw})});
        var d=await r.json();
        if(r.status>=400)throw new Error(d.error||'Hata');
        err.style.color='var(--mint)';err.textContent='Sifreniz guncellendi! Yonlendiriliyorsunuz...';
        setTimeout(function(){window.location.href=window.location.pathname;},2500);
      }catch(e){err.textContent=e.message;err.style.color='var(--danger)';}
    });
  });
}
"""

for fn in ['v2.html','panel.html','gecit-site-v1.html']:
    s = open(fn, encoding='utf-8').read()
    old = "var Q=new URLSearchParams(location.search);\n"
    found = old in s
    # Zaten eklenmis mi kontrol et
    if 'resetToken=Q.get' in s:
        print(fn, '-> ZATEN VAR, atlandi')
        continue
    s = s.replace(old, old + reset_code, 1)
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> bulundu:', found)
