for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s=open(fn,encoding='utf-8').read()
    old = """async function fetchKapiAtt(){
  var g=getKapiG(); var tenant=(g&&g._tenant)||'1'; var tok=(g&&g._token)||null;
  var h={'Content-Type':'application/json'}; if(tok)h['Authorization']='Bearer '+tok;
  try{
    var r=await fetch('https://gecitpdks.duckdns.org/api/'+tenant+'/attendance',{headers:h});
    var d=await r.json();
    return Array.isArray(d)?d:[];
  }catch(e){return [];}
}"""
    new = """async function fetchKapiAtt(){
  var g=getKapiG(); var tenant=(g&&g._tenant)||'1'; var tok=(g&&g._token)||null;
  var h={'Content-Type':'application/json'}; if(tok)h['Authorization']='Bearer '+tok;
  try{
    var r=await fetch('https://gecitpdks.duckdns.org/api/'+tenant+'/attendance',{headers:h});
    if(!r.ok){ window.__kapiErr='HTTP '+r.status; return []; }
    var d=await r.json();
    window.__kapiErr=null;
    window.__kapiLastLen=Array.isArray(d)?d.length:-1;
    return Array.isArray(d)?d:[];
  }catch(e){ window.__kapiErr='EXC: '+e.message; return []; }
}"""
    found = old in s
    s = s.replace(old, new)
    
    # Hata varsa feed'de goster
    old2 = "if(!nowList.length){ feed.innerHTML='<div style=\"color:var(--muted);font-size:13px;padding:6px 0;line-height:1.5\">Henüz giriş yok.<br>Personel mobilden QR okutunca burada anlık belirir.</div>'; return; }"
    new2 = "if(window.__kapiErr){ feed.innerHTML='<div style=\"color:var(--danger);font-size:12px;padding:6px 0\">HATA: '+window.__kapiErr+'</div>'; return; } if(!nowList.length){ feed.innerHTML='<div style=\"color:var(--muted);font-size:13px;padding:6px 0;line-height:1.5\">Henüz giriş yok (son veri: '+(window.__kapiLastLen||0)+' kayit).<br>Personel mobilden QR okutunca burada anlık belirir.</div>'; return; }"
    found2 = old2 in s
    s = s.replace(old2, new2)
    
    open(fn,encoding='utf-8',mode='w').write(s)
    print(fn, '->', found, found2)
