for fn in ['v2.html','panel.html','gecit-site-v1.html']:
    s = open(fn, encoding='utf-8').read()
    old = '  window.doLogout=doLogout;'
    new = """  window.doLogout=doLogout;
  window.showForgot=function(){var b=document.getElementById('forgot-box');if(b)b.style.display=b.style.display==='none'?'block':'none';};
  window.sendForgot=async function(){
    var user=document.getElementById('forgot-user').value.trim();
    var err=document.getElementById('forgot-err');
    if(!user){err.textContent='Kullanici adi gerekli';return;}
    err.textContent='Gonderiliyor...';err.style.color='var(--muted)';
    try{
      var r=await fetch('https://gecitpdks.duckdns.org/api/hotel/forgot-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:user})});
      var d=await r.json();
      if(r.status>=400)throw new Error(d.error||'Hata');
      err.textContent='Link e-postaniza gonderildi!';err.style.color='var(--mint)';
    }catch(e){err.textContent=e.message;err.style.color='var(--danger)';}
  };"""
    print(fn,'->', old in s)
    open(fn,'w',encoding='utf-8').write(s.replace(old,new))
