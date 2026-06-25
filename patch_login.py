for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    # 1) Superadmin ekranini gizle, login ekranini goster
    old1 = '<div id="superadmin" style="display:grid'
    new1 = '<div id="superadmin" style="display:none'
    found1 = old1 in s
    s = s.replace(old1, new1)
    
    old2 = '<div id="login" style="display:none">'
    new2 = '<div id="login" style="display:grid;min-height:100vh;place-items:center">'
    found2 = old2 in s
    s = s.replace(old2, new2)
    
    # 2) app gizle
    old3 = '<div id="app">'
    new3 = '<div id="app" style="display:none">'
    found3 = old3 in s
    s = s.replace(old3, new3, 1)
    
    # 3) Login inputlardan default deger kaldir
    old4 = '<input id="lg-id" value="emre.celik">'
    new4 = '<input id="lg-id" placeholder="Kullanici adi">'
    found4 = old4 in s
    s = s.replace(old4, new4)
    
    old5 = '<input id="lg-pw" type="password" value="123456">'
    new5 = '<input id="lg-pw" type="password" placeholder="Sifre">'
    found5 = old5 in s
    s = s.replace(old5, new5)
    
    # 4) Demo hint kaldir
    old6 = '    <div class="loginhint">Demo: herhangi bir id/şifre ile giriş</div>\n  </div>\n</div>\n<div id="app"'
    new6 = '    <div class="loginhint" id="lg-hint"></div>\n  </div>\n</div>\n<div id="app"'
    found6 = old6 in s
    s = s.replace(old6, new6)
    
    # 5) Login buton - gercek API cagrisi
    old7 = "  function doLogin(){ $('#login').style.display='none'; $('#app').style.display='block'; activate(document.querySelector('.navitem.active')); window.GECIT.load().then(function(){ window.GECIT.refresh&&window.GECIT.refresh(); }); }\n  $('#lg-btn').addEventListener('click',doLogin);"
    new7 = """  async function doLogin(){
    var uid=$('#lg-id').value.trim(); var pw=$('#lg-pw').value;
    if(!uid||!pw){showToast('Kullanici adi ve sifre gerekli');return;}
    var hint=document.getElementById('lg-hint'); if(hint)hint.textContent='Giris yapiliyor...';
    try{
      var d=await window.GECIT.api('/'+window.GECIT._tenant+'/hotel/login',{method:'POST',auth:false,body:{username:uid,password:pw}});
      window.GECIT._token=d.token;
      // Profil guncelle
      try{$('#app .who-chip b').textContent=d.name||uid;}catch(e){}
      if(hint)hint.textContent='';
      $('#login').style.display='none';
      $('#app').style.display='block';
      activate(document.querySelector('.navitem.active'));
      window.GECIT.load().then(function(){window.GECIT.refresh&&window.GECIT.refresh();});
    }catch(e){
      if(hint)hint.textContent='Hatali kullanici adi veya sifre';
      if(hint)hint.style.color='var(--danger)';
    }
  }
  $('#lg-btn').addEventListener('click',doLogin);
  $('#lg-pw').addEventListener('keydown',function(e){if(e.key==='Enter')doLogin();});
  $('#lg-id').addEventListener('keydown',function(e){if(e.key==='Enter')doLogin();});"""
    found7 = old7 in s
    s = s.replace(old7, new7)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> sup:', found1, '| login:', found2, '| app:', found3, '| inputs:', found4, found5, '| btn:', found7)
