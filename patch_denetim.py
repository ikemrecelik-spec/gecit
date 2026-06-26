for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    # Dashboard'da cikis yapmayan kartini genislet
    old = """    var cikisYapan=todayAtt.filter(function(r){return r.giris&&!r.cikis;});

    // Stats
    document.getElementById('s-aktif').textContent=aktif.length;
    document.getElementById('s-bugun').textContent=girisYapan.length;
    document.getElementById('s-iceride').textContent=iceride.length;
    document.getElementById('s-devamsiz').textContent=devamsiz.length;
    document.getElementById('s-onay').textContent=approvals.length;
    document.getElementById('s-cikis').textContent=cikisYapan.length;"""
    
    new = """    var cikisYapan=todayAtt.filter(function(r){return r.giris&&!r.cikis;});
    
    // Vardiyasi bitti ama cikis yapmadi kontrolu
    var nowMins=now.getHours()*60+now.getMinutes();
    var vardiyaBitiUyari=[];
    var shiftDefs=(settings&&settings.shifts)||[];
    cikisYapan.forEach(function(r){
      if(!r.vardiya)return;
      var shKey=r.vardiya.split(' ')[0];
      var shDef=shiftDefs.find(function(s){return s.code===shKey;});
      if(!shDef||!shDef.end)return;
      var ep=shDef.end.split(':').map(Number);
      var endMins=ep[0]*60+ep[1];
      var diff=nowMins-endMins;
      if(diff<0)diff+=1440;
      if(diff>30&&diff<720){ // 30 dk gecikme
        vardiyaBitiUyari.push({ad:r.ad,vardiya:r.vardiya,giris:r.giris,gecikme:diff});
      }
    });

    // Stats
    document.getElementById('s-aktif').textContent=aktif.length;
    document.getElementById('s-bugun').textContent=girisYapan.length;
    document.getElementById('s-iceride').textContent=iceride.length;
    document.getElementById('s-devamsiz').textContent=devamsiz.length;
    document.getElementById('s-onay').textContent=approvals.length;
    document.getElementById('s-cikis').textContent=cikisYapan.length;
    
    // Uyari banner
    var banner=document.getElementById('limit-banner');
    if(banner&&vardiyaBitiUyari.length>0){
      banner.style.display='block';
      banner.innerHTML='&#9888; '+vardiyaBitiUyari.length+' personelin vardiyasi bitti ama cikis yapmadi: '+vardiyaBitiUyari.map(function(x){return '<b>'+x.ad+'</b> ('+x.vardiya+', +'+Math.round(x.gecikme)+' dk)';}).join(', ');
    }"""
    
    found = old in s
    s = s.replace(old, new)
    
    # Banner div ekle - dashboard'a
    old2 = """<div class="topbar">
  <div>
    <h1>Genel Bakis</h1>
    <small id="dash-date">-</small>
  </div>
  <button class="refresh-btn" id="refresh-btn">&#8635; Yenile</button>
</div>"""
    new2 = """<div id="limit-banner" style="background:rgba(255,107,107,.1);border:1px solid rgba(255,107,107,.3);border-radius:10px;padding:10px 16px;margin-bottom:14px;font-size:13px;color:var(--danger);display:none"></div>
<div class="topbar">
  <div>
    <h1>Genel Bakis</h1>
    <small id="dash-date">-</small>
  </div>
  <button class="refresh-btn" id="refresh-btn">&#8635; Yenile</button>
</div>"""
    found2 = old2 in s
    s = s.replace(old2, new2)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> stats:', found, '| banner:', found2)
