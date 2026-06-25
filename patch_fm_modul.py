NEW_FM = r'''<template id="tpl-fm">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fazla Mesai Yonetimi</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--purple:#C792EA;--text:#EAF2F5;--muted:#8FA6B0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;padding:18px 16px 60px}
.topbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:16px}
.topbar h1{font-family:'Space Grotesk';font-size:18px;font-weight:700;margin:0;flex:1}
.tabs{display:flex;gap:4px;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:4px}
.tab{padding:7px 14px;border-radius:7px;border:0;background:transparent;color:var(--muted);font-size:13px;font-weight:600;cursor:pointer;font-family:inherit}
.tab.active{background:var(--amber);color:#1a1205}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;margin-bottom:14px}
.filter-bar{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end;padding:12px 16px;border-bottom:1px solid var(--line)}
.f{display:flex;flex-direction:column;gap:4px}
.f label{font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase}
.f input,.f select{background:var(--panel-2);border:1px solid var(--line);color:var(--text);border-radius:8px;padding:7px 10px;font-size:12.5px;font-family:inherit;outline:none}
.f input:focus,.f select:focus{border-color:var(--amber)}
.btn{padding:7px 13px;border-radius:8px;border:0;font-weight:600;font-size:12px;cursor:pointer;font-family:inherit}
.btn-amber{background:var(--amber);color:#1a1205}
.btn-ghost{background:var(--panel-2);border:1px solid var(--line);color:var(--text)}
.btn-ghost:hover{border-color:var(--amber);color:var(--amber)}
.btn-ok{background:rgba(52,217,160,.15);color:var(--mint);border:1px solid rgba(52,217,160,.3);border-radius:7px;padding:5px 10px;cursor:pointer;font-size:11.5px;font-weight:600}
.btn-no{background:rgba(255,107,107,.15);color:var(--danger);border:1px solid rgba(255,107,107,.3);border-radius:7px;padding:5px 10px;cursor:pointer;font-size:11.5px;font-weight:600}
table{width:100%;border-collapse:collapse;font-size:12px}
thead th{text-align:left;font-size:10.5px;color:var(--muted);font-weight:600;padding:9px 12px;border-bottom:1px solid var(--line);white-space:nowrap;text-transform:uppercase}
tbody td{padding:8px 12px;border-bottom:1px solid rgba(35,65,79,.35);vertical-align:middle}
tbody tr:hover td{background:rgba(27,49,62,.4)}
.who{display:flex;align-items:center;gap:8px}
.av{width:26px;height:26px;border-radius:7px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:10px;color:#1a1205;background:var(--amber);flex:0 0 auto}
.mono{font-family:'JetBrains Mono';font-size:11.5px}
.pill{display:inline-flex;align-items:center;font-size:10.5px;font-weight:600;padding:2px 7px;border-radius:5px}
.p-ok{background:rgba(52,217,160,.15);color:var(--mint)}
.p-warn{background:rgba(255,107,107,.15);color:var(--danger)}
.p-pend{background:rgba(242,181,59,.15);color:var(--amber)}
.p-blue{background:rgba(111,177,255,.15);color:var(--blue)}
.p-limit{background:rgba(255,107,107,.3);color:var(--danger);font-weight:700}
.empty{text-align:center;color:var(--muted);padding:40px;font-size:13px}
.footer-bar{display:flex;align-items:center;justify-content:space-between;padding:8px 16px;border-top:1px solid var(--line);flex-wrap:wrap;gap:8px}
.footer-bar span{color:var(--muted);font-size:11.5px}
.stat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;padding:14px 16px;border-bottom:1px solid var(--line)}
.stat{background:var(--panel-2);border:1px solid var(--line);border-radius:10px;padding:12px 14px}
.stat .val{font-family:'Space Grotesk';font-size:24px;font-weight:700;margin-bottom:4px}
.stat .lbl{color:var(--muted);font-size:11.5px}
.warn-banner{background:rgba(255,107,107,.1);border:1px solid rgba(255,107,107,.3);border-radius:10px;padding:10px 16px;margin-bottom:14px;font-size:13px;color:var(--danger);display:none}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:11px 18px;border-radius:10px;font-size:12.5px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
</style>

<div class="topbar">
  <h1>Fazla Mesai Yönetimi</h1>
  <div class="tabs">
    <button class="tab active" data-t="beklemede">Bekleyen <span id="fm-bekl-cnt" style="background:var(--danger);color:#fff;border-radius:10px;padding:1px 6px;font-size:10px;margin-left:4px">0</span></button>
    <button class="tab" data-t="onaylandi">Onaylanan</button>
    <button class="tab" data-t="reddedildi">Reddedilen</button>
    <button class="tab" data-t="ozet">Aylık Özet</button>
  </div>
</div>

<div id="limit-banner" class="warn-banner">⚠️ 270 saat yıllık FM limitine yaklaşan personel var!</div>

<!-- ONAY LİSTESİ -->
<div id="sec-onay">
  <div class="card">
    <div class="filter-bar">
      <div class="f"><label>Departman</label><select id="f-dep"><option value="">Tümü</option></select></div>
      <div class="f" style="justify-content:flex-end"><label>&nbsp;</label>
        <div style="display:flex;gap:6px">
          <button class="btn btn-ghost" id="excel-btn">↓ Excel</button>
          <button class="btn btn-amber" id="listele-btn">Listele</button>
        </div>
      </div>
    </div>
    <table>
      <thead><tr>
        <th>Sicil</th><th>Ad Soyad</th><th>Departman</th>
        <th>Tarih</th><th>Giriş</th><th>Çıkış</th>
        <th>FM Süresi</th><th>Yıllık Toplam</th><th>Durum</th><th></th>
      </tr></thead>
      <tbody id="fm-body"><tr><td colspan="10" class="empty">Listele butonuna basin...</td></tr></tbody>
    </table>
    <div class="footer-bar">
      <span id="fm-cnt">-</span>
      <span id="fm-total"></span>
    </div>
  </div>
</div>

<!-- AYLIK ÖZET -->
<div id="sec-ozet" style="display:none">
  <div class="card">
    <div class="filter-bar">
      <div class="f"><label>Ay</label><select id="oz-month"></select></div>
      <div class="f"><label>Yıl</label><select id="oz-year"></select></div>
      <div class="f"><label>Departman</label><select id="oz-dep"><option value="">Tümü</option></select></div>
      <div class="f" style="justify-content:flex-end"><label>&nbsp;</label>
        <div style="display:flex;gap:6px">
          <button class="btn btn-ghost" id="oz-excel">↓ Excel</button>
          <button class="btn btn-amber" id="oz-listele">Listele</button>
        </div>
      </div>
    </div>
    <div class="stat-grid" id="oz-stats" style="display:none">
      <div class="stat"><div class="val" id="oz-s1">0</div><div class="lbl">Toplam FM (saat)</div></div>
      <div class="stat"><div class="val" id="oz-s2">0</div><div class="lbl">FM'li Personel</div></div>
      <div class="stat"><div class="val" id="oz-s3">0</div><div class="lbl">Ort. FM/Kişi (saat)</div></div>
      <div class="stat"><div class="val" id="oz-s4" style="color:var(--danger)">0</div><div class="lbl">270s Limitine Yakın</div></div>
    </div>
    <table>
      <thead><tr>
        <th>Sicil</th><th>Ad Soyad</th><th>Departman</th>
        <th>Bu Ay FM (saat)</th><th>FM Gün</th><th>Yıllık FM (saat)</th><th>Kalan Limit</th><th>Durum</th>
      </tr></thead>
      <tbody id="oz-body"><tr><td colspan="8" class="empty">Listele butonuna basin...</td></tr></tbody>
    </table>
    <div class="footer-bar"><span id="oz-cnt">-</span></div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
function getG(){try{return window.parent&&window.parent.GECIT||null;}catch(e){return null;}}
async function req(path,opts){
  var g=getG(); var tenant=(g&&g._tenant)||'1'; var tok=(g&&g._token)||null;
  opts=opts||{}; var h={'Content-Type':'application/json'};
  if(tok)h['Authorization']='Bearer '+tok;
  var r=await fetch('https://gecitpdks.duckdns.org/api/'+tenant+path,{method:opts.method||'GET',headers:h,body:opts.body?JSON.stringify(opts.body):undefined});
  var d=null;try{d=await r.json();}catch(e){}
  if(!r.ok)throw new Error((d&&d.error)||('Hata '+r.status));
  return d;
}

var AYLAR=['Ocak','Subat','Mart','Nisan','Mayis','Haziran','Temmuz','Agustos','Eylul','Ekim','Kasim','Aralik'];
var now=new Date();
var curTab='beklemede'; var allData=[]; var yillikFM={};

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('on');},2500);}
function ini(s){var p=(s||'').trim().split(' ');return((p[0]||'')[0]||'')+((p[1]||'')[0]||'');}
function fmtM(m){if(m==null||m<0)return '-';return String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0');}
function timeMins(g,c){if(!g||!c)return null;var gp=g.split(':').map(Number);var cp=c.split(':').map(Number);var m=(cp[0]*60+cp[1])-(gp[0]*60+gp[1]);if(m<0)m+=1440;return m;}

// Ay/yıl select
var ozMs=document.getElementById('oz-month'); var ozYs=document.getElementById('oz-year');
ozMs.innerHTML=AYLAR.map(function(a,i){return '<option value="'+(i+1)+'"'+(i===now.getMonth()?' selected':'')+'>'+a+'</option>';}).join('');
for(var y=now.getFullYear()-1;y<=now.getFullYear()+1;y++){var o=document.createElement('option');o.value=y;o.textContent=y;if(y===now.getFullYear())o.selected=true;ozYs.appendChild(o);}

// Tab
document.querySelectorAll('.tab').forEach(function(t){
  t.addEventListener('click',function(){
    document.querySelectorAll('.tab').forEach(function(x){x.classList.remove('active');});
    t.classList.add('active'); curTab=t.dataset.t;
    document.getElementById('sec-onay').style.display=curTab==='ozet'?'none':'block';
    document.getElementById('sec-ozet').style.display=curTab==='ozet'?'block':'none';
    if(curTab!=='ozet')load();
  });
});

async function loadYillikFM(){
  try{
    var year=now.getFullYear();
    var start=year+'-01-01'; var end=year+'-12-31';
    var att=await req('/attendance');
    var empFM={};
    att.filter(function(r){return r.day>=start&&r.day<=end&&r.giris&&r.cikis;}).forEach(function(r){
      var m=timeMins(r.giris,r.cikis);
      if(m!=null&&m>540){
        empFM[r.tc]=(empFM[r.tc]||0)+(m-540);
      }
    });
    yillikFM=empFM;
    // Limit uyarisi
    var limit=Object.values(empFM).filter(function(v){return v>=(270-20)*60;});
    if(limit.length>0){
      document.getElementById('limit-banner').style.display='block';
    }
  }catch(e){}
}

async function load(){
  try{
    var url='/approvals'+(curTab==='tumu'?'':'?status='+curTab);
    var data=await req(url);
    var fmData=data.filter(function(r){return r.type==='fm'||r.type==='ht_work';});
    allData=fmData;
    // Badge
    var bekl=data.filter(function(r){return r.status==='beklemede'&&(r.type==='fm'||r.type==='ht_work');});
    document.getElementById('fm-bekl-cnt').textContent=bekl.length||'0';
    // Dep filtre
    var deps=[''];fmData.forEach(function(r){if(r.dep&&deps.indexOf(r.dep)<0)deps.push(r.dep);});
    var dsel=document.getElementById('f-dep');var cv=dsel.value;
    dsel.innerHTML=deps.map(function(d){return '<option value="'+d+'"'+(d===cv?' selected':'')+' >'+(d||'Tümü')+'</option>';}).join('');
    render();
  }catch(e){
    document.getElementById('fm-body').innerHTML='<tr><td colspan="10" class="empty">Hata: '+e.message+'</td></tr>';
  }
}

function render(){
  var dep=document.getElementById('f-dep').value;
  var filtered=dep?allData.filter(function(r){return r.dep===dep;}):allData;
  if(!filtered.length){
    document.getElementById('fm-body').innerHTML='<tr><td colspan="10" class="empty">Kayıt bulunamadı</td></tr>';
    document.getElementById('fm-cnt').textContent='0 kayıt';
    document.getElementById('fm-total').textContent='';
    return;
  }
  var totalFM=0;
  document.getElementById('fm-body').innerHTML=filtered.map(function(r){
    var att=r.att_id;
    var typeLabel=r.type==='ht_work'?'HT Çalışma':'Fazla Mesai';
    var st=r.status;
    var stHtml=st==='onaylandi'?'<span class="pill p-ok">Onaylandı</span>':st==='reddedildi'?'<span class="pill p-warn">Reddedildi</span>':'<span class="pill p-pend">Bekliyor</span>';
    var yFM=yillikFM[r.tc]||0; var yFMh=(yFM/60).toFixed(1);
    var limitWarn=yFM>=(270-20)*60?'<span class="pill p-limit">⚠ '+yFMh+'s</span>':'<span class="pill p-blue">'+yFMh+'s</span>';
    var btns=st==='beklemede'?'<button class="btn-ok" data-id="'+r.id+'">✓ Onayla</button> <button class="btn-no" data-id="'+r.id+'" data-red="1">✕ Reddet</button>':'';
    return '<tr>'
      +'<td class="mono" style="color:var(--muted)">#'+(r.sicil||'-')+'</td>'
      +'<td><div class="who"><div class="av">'+ini(r.ad||'?')+'</div><b>'+(r.ad||'?')+'</b></div></td>'
      +'<td style="color:var(--muted);font-size:11.5px">'+(r.dep||'-')+'</td>'
      +'<td class="mono">'+r.day+'</td>'
      +'<td class="mono">'+'-'+'</td>'
      +'<td class="mono">'+'-'+'</td>'
      +'<td><span class="pill p-amber">'+typeLabel+'</span></td>'
      +'<td>'+limitWarn+'</td>'
      +'<td>'+stHtml+'</td>'
      +'<td style="white-space:nowrap">'+btns+'</td>'
      +'</tr>';
  }).join('');
  document.getElementById('fm-cnt').textContent=filtered.length+' kayıt';

  document.querySelectorAll('#fm-body .btn-ok').forEach(function(btn){
    btn.addEventListener('click',async function(){
      try{await req('/approvals/'+btn.dataset.id,{method:'PUT',body:{status:'onaylandi'}});toast('Onaylandı');load();}
      catch(e){toast('Hata: '+e.message);}
    });
  });
  document.querySelectorAll('#fm-body .btn-no').forEach(function(btn){
    btn.addEventListener('click',async function(){
      var note=prompt('Red sebebi (opsiyonel):');
      try{await req('/approvals/'+btn.dataset.id,{method:'PUT',body:{status:'reddedildi',note:note||''}});toast('Reddedildi');load();}
      catch(e){toast('Hata: '+e.message);}
    });
  });
}

// Aylık özet
document.getElementById('oz-listele').addEventListener('click',async function(){
  var month=+document.getElementById('oz-month').value;
  var year=+document.getElementById('oz-year').value;
  var pad=function(n){return String(n).padStart(2,'0');};
  var start=year+'-'+pad(month)+'-01';
  var lastDay=new Date(year,month,0).getDate();
  var end=year+'-'+pad(month)+'-'+lastDay;
  var dep=document.getElementById('oz-dep').value;
  document.getElementById('oz-body').innerHTML='<tr><td colspan="8" class="empty">Yukleniyor...</td></tr>';
  try{
    var att=await req('/attendance');
    var empFM={};
    att.filter(function(r){return r.day>=start&&r.day<=end&&r.giris&&r.cikis;}).forEach(function(r){
      var m=timeMins(r.giris,r.cikis);
      if(m!=null&&m>540){
        if(!empFM[r.tc])empFM[r.tc]={tc:r.tc,ad:r.ad,dep:r.dep,sicil:r.sicil,fm:0,days:0};
        empFM[r.tc].fm+=m-540;
        empFM[r.tc].days++;
      }
    });
    var rows=Object.values(empFM);
    if(dep)rows=rows.filter(function(r){return r.dep===dep;});
    // Dep filtre
    var deps=[''];Object.values(empFM).forEach(function(r){if(deps.indexOf(r.dep)<0)deps.push(r.dep);});
    document.getElementById('oz-dep').innerHTML=deps.map(function(d){return '<option value="'+d+'"'+(d===dep?' selected':'')+' >'+(d||'Tümü')+'</option>';}).join('');
    // Stats
    var totalFM=rows.reduce(function(s,r){return s+r.fm;},0);
    var nearLimit=rows.filter(function(r){return (yillikFM[r.tc]||0)>=(270-20)*60;}).length;
    document.getElementById('oz-s1').textContent=(totalFM/60).toFixed(1);
    document.getElementById('oz-s2').textContent=rows.length;
    document.getElementById('oz-s3').textContent=rows.length?(totalFM/rows.length/60).toFixed(1):'0';
    document.getElementById('oz-s4').textContent=nearLimit;
    document.getElementById('oz-stats').style.display='grid';
    if(!rows.length){document.getElementById('oz-body').innerHTML='<tr><td colspan="8" class="empty">FM kaydi yok</td></tr>';document.getElementById('oz-cnt').textContent='0 personel';return;}
    rows.sort(function(a,b){return b.fm-a.fm;});
    document.getElementById('oz-body').innerHTML=rows.map(function(r){
      var fmH=(r.fm/60).toFixed(1);
      var yFM=yillikFM[r.tc]||0; var yFMh=(yFM/60).toFixed(1);
      var kalan=Math.max(0,270-yFM/60).toFixed(1);
      var limitCls=yFM>=(270-20)*60?'p-limit':yFM>=200*60?'p-pend':'p-ok';
      return '<tr>'
        +'<td class="mono" style="color:var(--muted)">#'+r.sicil+'</td>'
        +'<td><div class="who"><div class="av">'+ini(r.ad)+'</div><b>'+r.ad+'</b></div></td>'
        +'<td style="color:var(--muted);font-size:11.5px">'+r.dep+'</td>'
        +'<td class="mono"><b>'+fmH+'</b></td>'
        +'<td class="mono">'+r.days+'</td>'
        +'<td class="mono">'+yFMh+'</td>'
        +'<td class="mono">'+kalan+'</td>'
        +'<td><span class="pill '+limitCls+'">'+(yFM>=(270-20)*60?'⚠ Limit!':yFM>=200*60?'Dikkat':'Normal')+'</span></td>'
        +'</tr>';
    }).join('');
    document.getElementById('oz-cnt').textContent=rows.length+' personel';
  }catch(e){document.getElementById('oz-body').innerHTML='<tr><td colspan="8" class="empty">Hata: '+e.message+'</td></tr>';}
});

document.getElementById('listele-btn').addEventListener('click',load);
document.getElementById('f-dep').addEventListener('change',render);

document.getElementById('excel-btn').addEventListener('click',function(){
  var rows=Array.from(document.querySelectorAll('#fm-body tr')).filter(function(r){return !r.querySelector('td.empty');});
  var csv='Sicil,Ad Soyad,Departman,Tarih,Tur,Yillik FM,Durum\n';
  rows.forEach(function(r){var c=r.querySelectorAll('td');csv+=c[0].textContent+','+c[1].textContent+','+c[2].textContent+','+c[3].textContent+','+c[6].textContent+','+c[7].textContent+','+c[8].textContent+'\n';});
  var blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='fm-onaylar.csv';a.click();
});

loadYillikFM();
load();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    # Menüye FM ekle - İzin Yönetimi'nden sonra
    old_nav = """      <div class="navitem" data-v="izin" data-frame="tpl-izin"><span class="i">✈</span> İzin Yönetimi</div>"""
    new_nav = """      <div class="navitem" data-v="izin" data-frame="tpl-izin"><span class="i">✈</span> İzin Yönetimi</div>
      <div class="navitem" data-v="fm" data-frame="tpl-fm"><span class="i">⏱</span> Fazla Mesai <span class="badge" id="nav-fm">0</span></div>"""
    found_nav = old_nav in s
    s = s.replace(old_nav, new_nav)
    
    # Template ekle - tpl-izin'den önce
    old_tpl = '<template id="tpl-izin">'
    found_tpl = old_tpl in s
    s = s.replace(old_tpl, NEW_FM + '\n<template id="tpl-izin">', 1)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> nav:', found_nav, '| tpl:', found_tpl, '| boyut:', len(s))
