for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    # Tema butonu ekle - who-chip'in yanina
    old = """          <div class="who-chip"><div class="av" style="background:var(--amber)">EÇ</div><div><b>Emre Çelik</b><small>İK / Yönetici</small></div></div>"""
    new = """          <div id="tema-btn" title="Tema değiştir" style="border:1px solid var(--line);background:var(--panel);color:var(--muted);border-radius:10px;padding:8px 12px;font-size:18px;cursor:pointer;line-height:1" onclick="toggleTemaMenu()">🎨</div>
          <div id="tema-menu" style="display:none;position:absolute;top:60px;right:16px;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px;z-index:99;box-shadow:0 16px 40px rgba(0,0,0,.5);min-width:200px">
            <div style="font-size:11px;color:var(--muted);font-weight:600;padding:4px 8px 8px;text-transform:uppercase">Tema Seç</div>
            <div class="tema-item" data-tema="dark" onclick="setTema('dark')">🌑 Koyu Gece</div>
            <div class="tema-item" data-tema="light" onclick="setTema('light')">☀️ Açık</div>
            <div class="tema-item" data-tema="navy" onclick="setTema('navy')">🌊 Lacivert</div>
            <div class="tema-item" data-tema="green" onclick="setTema('green')">🌿 Yeşil</div>
            <div class="tema-item" data-tema="bordo" onclick="setTema('bordo')">🍷 Bordo</div>
            <div class="tema-item" data-tema="purple" onclick="setTema('purple')">💜 Mor</div>
            <div class="tema-item" data-tema="ocean" onclick="setTema('ocean')">🏄 Okyanus</div>
          </div>
          <div class="who-chip"><div class="av" style="background:var(--amber)">EÇ</div><div><b>Emre Çelik</b><small>İK / Yönetici</small></div></div>"""
    found1 = old in s
    s = s.replace(old, new)
    
    # CSS ekle - tema-item ve temalar
    old_css = """:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--purple:#C792EA;--text:#EAF2F5;--muted:#8FA6B0;--radius:14px;--shadow:0 24px 60px rgba(0,0,0,.45)}"""
    new_css = """:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--purple:#C792EA;--text:#EAF2F5;--muted:#8FA6B0;--radius:14px;--shadow:0 24px 60px rgba(0,0,0,.45)}
/* Temalar */
.tema-dark{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--text:#EAF2F5;--muted:#8FA6B0}
.tema-light{--ink:#F0F4F8;--panel:#FFFFFF;--panel-2:#F0F4F8;--line:#DDE3E9;--text:#1A2332;--muted:#6B7A8D}
.tema-navy{--ink:#0A0F1E;--panel:#0F1A35;--panel-2:#152040;--line:#1E2E50;--text:#E8EEFF;--muted:#7A8FB0}
.tema-green{--ink:#0A1A12;--panel:#0F2419;--panel-2:#152E20;--line:#1E4030;--text:#E8F5EE;--muted:#7AB095}
.tema-bordo{--ink:#1A0A0E;--panel:#2A0F15;--panel-2:#35141C;--line:#501E28;--text:#F5E8EA;--muted:#B08A90}
.tema-purple{--ink:#120A1A;--panel:#1A0F2A;--panel-2:#201535;--line:#301E50;--text:#EEE8F5;--muted:#9A8AB0}
.tema-ocean{--ink:#041218;--panel:#071E28;--panel-2:#0A2535;--line:#0E3545;--text:#E0F5FF;--muted:#70A5B8}
.tema-item{padding:8px 12px;border-radius:8px;cursor:pointer;font-size:13px;font-weight:500}
.tema-item:hover{background:var(--panel-2)}
.tema-item.active{background:var(--amber);color:#1a1205}"""
    found2 = old_css in s
    s = s.replace(old_css, new_css)
    
    # JavaScript ekle - tema fonksiyonlari
    old_js = """  window.renderReg=renderReg;"""
    new_js = """  // Tema sistemi
  var TEMALAR={dark:'tema-dark',light:'tema-light',navy:'tema-navy',green:'tema-green',bordo:'tema-bordo',purple:'tema-purple',ocean:'tema-ocean'};
  function setTema(t){
    var body=document.body;
    Object.values(TEMALAR).forEach(function(c){body.classList.remove(c);});
    if(t!=='dark')body.classList.add(TEMALAR[t]);
    try{localStorage.setItem('GECIT_TEMA',t);}catch(e){}
    document.querySelectorAll('.tema-item').forEach(function(el){el.classList.toggle('active',el.dataset.tema===t);});
    toggleTemaMenu();
  }
  function toggleTemaMenu(){
    var m=document.getElementById('tema-menu');
    if(m)m.style.display=m.style.display==='none'?'block':'none';
  }
  document.addEventListener('click',function(e){
    var m=document.getElementById('tema-menu');
    var b=document.getElementById('tema-btn');
    if(m&&b&&!m.contains(e.target)&&!b.contains(e.target))m.style.display='none';
  });
  // Kaydedilmis temay yukle
  try{var savedTema=localStorage.getItem('GECIT_TEMA');if(savedTema&&savedTema!=='dark'){document.body.classList.add(TEMALAR[savedTema]);document.querySelectorAll('.tema-item').forEach(function(el){el.classList.toggle('active',el.dataset.tema===savedTema);});}}catch(e){}

  window.renderReg=renderReg;"""
    found3 = old_js in s
    s = s.replace(old_js, new_js)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> btn:', found1, '| css:', found2, '| js:', found3)
