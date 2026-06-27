for fn in ['v2.html','panel.html','gecit-site-v1.html']:
    s = open(fn, encoding='utf-8').read()
    
    # who-chip'i profil dropdown'a cevir
    old = """          <div class="who-chip"><div class="av" style="background:var(--amber)">EÇ</div><div><b>Emre Çelik</b><small>İK / Yönetici</small></div></div>"""
    
    new = """          <div id="profil-btn" style="display:flex;align-items:center;gap:10px;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:7px 12px;cursor:pointer;position:relative" onclick="toggleProfilMenu()">
            <div class="av" id="profil-av" style="background:var(--amber);width:32px;height:32px;border-radius:9px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:12px;color:#1a1205;flex:0 0 auto">EÇ</div>
            <div><b id="profil-ad" style="font-size:13px;font-weight:600">Emre Çelik</b><small id="profil-rol" style="color:var(--muted);font-size:11px;display:block">İK / Yönetici</small></div>
            <span style="color:var(--muted);font-size:10px;margin-left:4px">▾</span>
          </div>
          <div id="profil-menu" style="display:none;position:absolute;top:65px;right:16px;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:8px;z-index:99;box-shadow:0 16px 40px rgba(0,0,0,.55);min-width:240px">
            <div style="padding:12px 14px 10px;border-bottom:1px solid var(--line);margin-bottom:6px">
              <div style="display:flex;align-items:center;gap:10px">
                <div class="av" id="profil-menu-av" style="background:var(--amber);width:40px;height:40px;border-radius:10px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:14px;color:#1a1205;flex:0 0 auto">EÇ</div>
                <div><div id="profil-menu-ad" style="font-weight:700;font-size:14px">Emre Çelik</div><div id="profil-menu-rol" style="color:var(--muted);font-size:12px">İK / Yönetici</div></div>
              </div>
            </div>
            <div style="padding:4px 8px 6px;font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.3px">Tema</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;padding:0 4px;margin-bottom:6px">
              <div class="tema-item" data-tema="dark" onclick="setTema('dark')" style="text-align:center;font-size:11px">🌑 Koyu</div>
              <div class="tema-item" data-tema="light" onclick="setTema('light')" style="text-align:center;font-size:11px">☀️ Açık</div>
              <div class="tema-item" data-tema="navy" onclick="setTema('navy')" style="text-align:center;font-size:11px">🌊 Lacivert</div>
              <div class="tema-item" data-tema="green" onclick="setTema('green')" style="text-align:center;font-size:11px">🌿 Yeşil</div>
              <div class="tema-item" data-tema="bordo" onclick="setTema('bordo')" style="text-align:center;font-size:11px">🍷 Bordo</div>
              <div class="tema-item" data-tema="purple" onclick="setTema('purple')" style="text-align:center;font-size:11px">💜 Mor</div>
              <div class="tema-item" data-tema="ocean" onclick="setTema('ocean')" style="text-align:center;font-size:11px">🏄 Okyanus</div>
            </div>
            <div style="border-top:1px solid var(--line);margin:4px 0 6px"></div>
            <div style="padding:8px 12px;border-radius:8px;cursor:pointer;font-size:13px;display:flex;align-items:center;gap:8px;color:var(--danger)" onclick="doLogout()">
              <span>⎋</span> Çıkış Yap
            </div>
          </div>"""
    
    found = old in s
    s = s.replace(old, new)
    
    # Eski tema butonunu ve menusunu kaldir
    old2 = """          <div id="tema-btn" title="Tema değiştir" style="border:1px solid var(--line);background:var(--panel);color:var(--muted);border-radius:10px;padding:8px 12px;font-size:18px;cursor:pointer;line-height:1" onclick="toggleTemaMenu()"></div>
          <div id="tema-menu" style="display:none;position:absolute;top:60px;right:16px;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px;z-index:99;box-shadow:0 16px 40px rgba(0,0,0,.5);min-width:200px">
            <div style="font-size:11px;color:var(--muted);font-weight:600;padding:4px 8px 8px;text-transform:uppercase">Tema Seç</div>
            <div class="tema-item" data-tema="dark" onclick="setTema('dark')"> Koyu Gece</div>
            <div class="tema-item" data-tema="light" onclick="setTema('light')">☀ Açık</div>
            <div class="tema-item" data-tema="navy" onclick="setTema('navy')"> Lacivert</div>
            <div class="tema-item" data-tema="green" onclick="setTema('green')"> Yeşil</div>
            <div class="tema-item" data-tema="bordo" onclick="setTema('bordo')"> Bordo</div>
            <div class="tema-item" data-tema="purple" onclick="setTema('purple')"> Mor</div>
            <div class="tema-item" data-tema="ocean" onclick="setTema('ocean')"> Okyanus</div>
          </div>"""
    found2 = old2 in s
    s = s.replace(old2, '<!-- tema-btn profil menusune tasindi -->')
    
    # toggleTemaMenu fonksiyonunu toggleProfilMenu ile değiştir
    old3 = "  window.getMyLocation=function(){"
    new3 = """  function toggleProfilMenu(){
    var m=document.getElementById('profil-menu');
    if(m)m.style.display=m.style.display==='none'?'block':'none';
  }
  window.toggleProfilMenu=toggleProfilMenu;
  document.addEventListener('click',function(e){
    var m=document.getElementById('profil-menu');
    var b=document.getElementById('profil-btn');
    if(m&&b&&!m.contains(e.target)&&!b.contains(e.target))m.style.display='none';
  });
  function doLogout(){
    if(!confirm('Çıkış yapmak istediğinizden emin misiniz?'))return;
    window.GECIT._token=null;window.GECIT._tenant='1';
    document.getElementById('app').style.display='none';
    document.getElementById('login').style.display='grid';
    document.getElementById('lg-id').value='';
    document.getElementById('lg-pw').value='';
  }
  window.doLogout=doLogout;
  window.getMyLocation=function(){"""
    found3 = old3 in s
    s = s.replace(old3, new3)
    
    # Login sonrasi profil guncelle
    old4 = """      try{$('#app .who-chip b').textContent=d.name||uid;}catch(e){}"""
    new4 = """      try{
        var nm=d.name||uid;
        var ini=nm.trim().split(' ').map(function(p){return p[0]||'';}).join('').slice(0,2).toUpperCase();
        document.getElementById('profil-av').textContent=ini;
        document.getElementById('profil-ad').textContent=nm;
        document.getElementById('profil-menu-av').textContent=ini;
        document.getElementById('profil-menu-ad').textContent=nm;
        if(d.tenant)window.GECIT._tenant=d.tenant;
      }catch(e){}"""
    found4 = old4 in s
    s = s.replace(old4, new4)
    
    # Settings'ten hotel adi gelince profil rol guncelle
    old5 = "          var name=(d&&d.general&&d.general.name)||t.name;"
    new5 = "          var name=(d&&d.general&&d.general.name)||t.name;\n          try{document.getElementById('profil-menu-rol').textContent=name;}catch(e){}"
    found5 = old5 in s
    s = s.replace(old5, new5)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> chip:', found, '| tema:', found2, '| fn:', found3, '| login:', found4, '| rol:', found5)
