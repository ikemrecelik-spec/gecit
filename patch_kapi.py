for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s=open(fn,encoding='utf-8').read()
    
    old = """function initials(n){return n.split(' ').slice(0,2).map(w=>w[0]).join('');}
function gstore(){ try{ if(window.parent&&window.parent.GECIT&&window.parent.GECIT.live) return window.parent.GECIT.live; }catch(e){} return null; }
const PAL=['#34D9A0','#6FB1FF','#C792EA','#FF9E6B','#F2B53B'];
function renderFeed(){
  const L=gstore();
  if(!L){ feed.innerHTML='<div style="color:var(--muted);font-size:13px;padding:6px 0">Bağlı sistem yok.</div>'; return; }
  const att=(L.att||[]).slice(0,6);
  if(!att.length){ feed.innerHTML='<div style="color:var(--muted);font-size:13px;padding:6px 0;line-height:1.5">Henüz giriş yok.<br>Personel mobilden QR okutunca burada anlık belirir.</div>'; return; }
  feed.innerHTML=att.map(function(r,i){ const io=r[5]?('Çıkış '+r[5]):('Giriş '+r[4]);
    return '<div class="entry"><div class="av" style="background:'+PAL[i%5]+'">'+initials(r[2])+'</div><div><div class="nm">'+r[2]+'</div><div class="meta">'+(r[9]||'')+' · '+(r[3]||'')+'</div></div><div class="ok"><span class="tm">'+io+'</span> ✓</div></div>';
  }).join('');
}
renderFeed(); setInterval(renderFeed,2000);"""

    new = """function initials(n){return n.split(' ').slice(0,2).map(w=>w[0]).join('');}
function kvkkName(n){var p=(n||'').trim().split(' ');if(p.length<2)return (p[0]||'').slice(0,2)+'.. ';return p[0].slice(0,2)+'.. '+p[p.length-1].slice(0,2)+'..';}
function getKapiG(){try{return window.parent&&window.parent.GECIT||null;}catch(e){return null;}}
const PAL=['#34D9A0','#6FB1FF','#C792EA','#FF9E6B','#F2B53B'];
var kapiFeedItems=[]; // {tc, ad, dep, time, action, ts}
async function fetchKapiAtt(){
  var g=getKapiG(); var tenant=(g&&g._tenant)||'1'; var tok=(g&&g._token)||null;
  var h={'Content-Type':'application/json'}; if(tok)h['Authorization']='Bearer '+tok;
  try{
    var r=await fetch(location.origin+'/api/'+tenant+'/attendance',{headers:h});
    var d=await r.json();
    return Array.isArray(d)?d:[];
  }catch(e){return [];}
}
async function renderFeed(){
  var att=await fetchKapiAtt();
  var now=Date.now();
  var nowList=att.filter(function(r){return (now-(r.ts||0))<10000;}).slice(0,8);
  if(!nowList.length){ feed.innerHTML='<div style="color:var(--muted);font-size:13px;padding:6px 0;line-height:1.5">Henüz giriş yok.<br>Personel mobilden QR okutunca burada anlık belirir (10 sn görünür).</div>'; return; }
  feed.innerHTML=nowList.map(function(r,i){ var io=r.cikis?('Çıkış '+r.cikis):('Giriş '+r.giris);
    return '<div class="entry"><div class="av" style="background:'+PAL[i%5]+'">'+initials(r.ad||'')+'</div><div><div class="nm">'+kvkkName(r.ad)+'</div><div class="meta">'+(r.dep||'')+' · '+(r.vardiya||'')+'</div></div><div class="ok"><span class="tm">'+io+'</span> ✓</div></div>';
  }).join('');
}
renderFeed(); setInterval(renderFeed,2000);"""

    found = old in s
    s = s.replace(old, new)
    open(fn,encoding='utf-8',mode='w').write(s)
    print(fn, '->', found)
