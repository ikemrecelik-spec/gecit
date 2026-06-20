for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s=open(fn,encoding='utf-8').read()
    old="""async function renderFeed(){
  var att=await fetchKapiAtt();
  var now=Date.now();
  var nowList=att.filter(function(r){return (now-(r.ts||0))<60000;}).slice(0,8);
  if(!nowList.length){ feed.innerHTML='<div style="color:var(--muted);font-size:13px;padding:6px 0;line-height:1.5">Henüz giriş yok.<br>Personel mobilden QR okutunca burada anlık belirir (10 sn görünür).</div>'; return; }"""
    new="""async function renderFeed(){
  var att=await fetchKapiAtt();
  var now=Date.now();
  var nowList=att.filter(function(r){return (now-(r.ts||0))<60000;}).slice(0,8);
  if(!nowList.length){ feed.innerHTML='<div style="color:var(--muted);font-size:11px;padding:6px 0;line-height:1.5">DEBUG: att.length='+att.length+' | son ts farki='+(att[0]?(now-att[0].ts):'yok')+'ms<br>Henüz giriş yok (60sn penceresi dışında).</div>'; return; }"""
    found = old in s
    s = s.replace(old, new)
    open(fn,encoding='utf-8',mode='w').write(s)
    print(fn, '->', found)
