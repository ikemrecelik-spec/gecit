for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s=open(fn,encoding='utf-8').read()
    
    # Mevcut renderFeed'i bul (debug mesajli versiyon) ve eski basit mantığa döndür
    # ama isim KVKK kısaltmalı olsun, 60sn pencere ile (60sn = gercekci, kapida 1 dk gorunur)
    import re
    start_marker = "async function renderFeed(){"
    idx = s.find(start_marker)
    if idx == -1:
        print(fn, "renderFeed bulunamadi")
        continue
    end_idx = s.find("\n}\n", idx) + 3
    old_func = s[idx:end_idx]
    
    new_func = """async function renderFeed(){
  var att=await fetchKapiAtt();
  var now=Date.now();
  var nowList=att.filter(function(r){return (now-(r.ts||0))<60000;}).slice(0,8);
  if(!nowList.length){ feed.innerHTML='<div style="color:var(--muted);font-size:13px;padding:6px 0;line-height:1.5">Henüz giriş yok.<br>Personel mobilden QR okutunca burada anlık belirir.</div>'; return; }
  feed.innerHTML=nowList.map(function(r,i){ var io=r.cikis?('Çıkış '+r.cikis):('Giriş '+r.giris);
    return '<div class="entry"><div class="av" style="background:'+PAL[i%5]+'">'+initials(r.ad||'')+'</div><div><div class="nm">'+kvkkName(r.ad)+'</div><div class="meta">'+(r.dep||'')+' · '+(r.vardiya||'')+'</div></div><div class="ok"><span class="tm">'+io+'</span> ✓</div></div>';
  }).join('');
}
"""
    s = s[:idx] + new_func + s[end_idx:]
    open(fn,encoding='utf-8',mode='w').write(s)
    print(fn, 'guncellendi, eski:', len(old_func), 'yeni:', len(new_func))
