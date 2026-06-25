for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    old = """  function selectTenant(t){ window.GECIT._tenant=String(t.id); window.GECIT._api=location.origin; $('#hotel-name').textContent=t.name; window.GECIT.connectWS&&window.GECIT.connectWS();
    window.GECIT.load().then(function(){ if(window.renderReg)window.renderReg(); });
    $('#superadmin').style.display='none'; $('#login').style.display='grid'; }"""
    
    new = """  function selectTenant(t){ window.GECIT._tenant=String(t.id); window.GECIT._api=location.origin; $('#hotel-name').textContent=t.name; window.GECIT.connectWS&&window.GECIT.connectWS();
    window.GECIT.load().then(function(){
      if(window.renderReg)window.renderReg();
      // Settings'ten hotel adini cek
      try{
        var h={'Content-Type':'application/json','Authorization':'Bearer '+window.GECIT._token};
        fetch('https://gecitpdks.duckdns.org/api/'+window.GECIT._tenant+'/settings',{headers:h})
          .then(function(r){return r.json();})
          .then(function(d){
            var name=(d&&d.general&&d.general.name)||t.name;
            $('#hotel-name').textContent=name;
          }).catch(function(){});
      }catch(e){}
      loadApprovals&&loadApprovals();
    });
    $('#superadmin').style.display='none'; $('#login').style.display='grid'; }"""
    
    found = old in s
    s = s.replace(old, new)
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '->', found)
