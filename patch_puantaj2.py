NEW_PUANTAJ = r'''<template id="tpl-puantaj">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Aylık Puantaj</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--purple:#C792EA;--text:#EAF2F5;--muted:#8FA6B0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;padding:22px 16px 60px}
.topbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:16px}
.topbar h1{font-family:'Space Grotesk';font-size:18px;font-weight:700;margin:0;flex:1}
.nav{display:flex;align-items:center;gap:6px;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:5px 10px}
.nav button{background:none;border:0;color:var(--muted);cursor:pointer;font-size:18px;padding:0 4px}
.nav button:hover{color:var(--text)}
.nav span{font-family:'Space Grotesk';font-weight:600;font-size:14px;min-width:120px;text-align:center}
.btn{padding:8px 14px;border-radius:8px;border:0;font-weight:600;font-size:12.5px;cursor:pointer;font-family:inherit}
.btn-amber{background:var(--amber);color:#1a1205}
.btn-ghost{background:var(--panel);border:1px solid var(--line);color:var(--text)}
.filters{display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap;align-items:center}
.filter-btn{padding:6px 12px;border-radius:7px;border:1px solid var(--line);background:var(--panel);color:var(--muted);font-size:12px;font-weight:600;cursor:pointer}
.filter-btn.active{background:var(--amber);color:#1a1205;border-color:var(--amber)}
.wrap{overflow-x:auto}
table{border-collapse:collapse;font-size:11.5px;white-space:nowrap;min-width:100%}
thead th{position:sticky;top:0;background:var(--panel);border-bottom:2px solid var(--line);padding:8px 5px;text-align:center;font-weight:600;color:var(--muted);z-index:2;min-width:28px}
thead th.sticky-col{text-align:left;padding-left:10px;position:sticky;z-index:3;background:var(--panel)}
thead th.sticky-col:nth-child(1){left:0;min-width:65px}
thead th.sticky-col:nth-child(2){left:65px;min-width:130px}
thead th.sticky-col:nth-child(3){left:195px;min-width:90px}
thead th.ht{color:var(--blue)}
thead th.sum-head{background:var(--panel-2);color:var(--amber);font-size:11px;min-width:30px}
tbody td{padding:6px 4px;border-bottom:1px solid rgba(35,65,79,.4);text-align:center;vertical-align:middle}
tbody td.sticky-col{text-align:left;padding-left:10px;position:sticky;background:var(--panel);z-index:1}
tbody td.sticky-col:nth-child(1){left:0;min-width:65px;font-family:'JetBrains Mono';font-size:10.5px;color:var(--muted)}
tbody td.sticky-col:nth-child(2){left:65px;min-width:130px;font-weight:600;font-size:12px}
tbody td.sticky-col:nth-child(3){left:195px;min-width:90px;font-size:11px;color:var(--muted)}
tbody tr:hover td{background:rgba(27,49,62,.6)}
tbody tr:hover td.sticky-col{background:var(--panel-2)}
.c{display:inline-flex;align-items:center;justify-content:center;width:22px;height:20px;border-radius:4px;font-weight:700;font-size:11px}
.cX{background:rgba(52,217,160,.15);color:var(--mint)}
.cHT{color:var(--blue);font-weight:700}
.cBT{background:rgba(111,177,255,.12);color:var(--blue)}
.cBC{background:rgba(111,177,255,.2);color:#fff}
.cM{background:rgba(242,181,59,.12);color:var(--amber)}
.cUi{background:rgba(199,146,234,.12);color:var(--purple)}
.cYi{background:rgba(111,177,255,.12);color:var(--blue)}
.cRP{background:rgba(255,107,107,.1);color:var(--danger)}
.cUR{background:rgba(52,217,160,.1);color:var(--mint)}
.cG{background:rgba(143,166,176,.1);color:var(--muted)}
.cD{background:rgba(255,107,107,.15);color:var(--danger)}
.cDot{color:var(--line)}
.sum-col{background:var(--panel-2)!important;font-weight:700;font-size:11px;border-left:1px solid var(--line)}
.sum-row td{background:rgba(27,49,62,.8)!important;font-weight:700;border-top:2px solid var(--line)}
.sum-row td.sticky-col{background:var(--panel-2)!important}
.legend{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap}
.leg{display:flex;align-items:center;gap:5px;font-size:11.5px;color:var(--muted)}
.locked-badge{background:rgba(255,107,107,.15);color:var(--danger);border:1px solid var(--danger);border-radius:7px;padding:4px 10px;font-size:12px;font-weight:600}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:12px 20px;border-radius:11px;font-size:13px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
</style>

<div class="topbar">
  <h1>Aylık Puantaj</h1>
  <div class="nav">
    <button id="prev-btn">&#8249;</button>
    <span id="month-label">-</span>
    <button id="next-btn">&#8250;</button>
  </div>
  <span id="locked-badge" style="display:none" class="locked-badge">&#128274; Kilitli</span>
  <button class="btn btn-ghost" id="lock-btn">Kilitle</button>
  <button class="btn btn-amber" id="export-btn">Excel</button>
</div>

<div class="filters" id="dep-filters">
  <button class="filter-btn active" data-dep="">Tum bolumler</button>
</div>

<div class="wrap">
  <table id="puantaj-table">
    <thead id="pt-head"></thead>
    <tbody id="pt-body"></tbody>
  </table>
</div>

<div class="legend">
  <div class="leg"><span class="c cX">X</span> Calisma</div>
  <div class="leg"><span class="c cHT">HT</span> Haftalik izin</div>
  <div class="leg"><span class="c cBT">BT</span> Resmi tatil</div>
  <div class="leg"><span class="c cBC">BC</span> Resmi tatil calismasi</div>
  <div class="leg"><span class="c cM">M</span> Ucretli izin</div>
  <div class="leg"><span class="c cUi">Ui</span> Ucretsiz izin</div>
  <div class="leg"><span class="c cYi">Yi</span> Yillik izin</div>
  <div class="leg"><span class="c cRP">RP</span> Raporlu</div>
  <div class="leg"><span class="c cUR">UR</span> Odenen rapor</div>
  <div class="leg"><span class="c cG">G</span> Gorevli</div>
  <div class="leg"><span class="c cD">D</span> Devamsiz</div>
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

var now=new Date(); var curYear=now.getFullYear(); var curMonth=now.getMonth()+1; var curDep=''; var pData=null;
var AYLAR=['Ocak','Subat','Mart','Nisan','Mayis','Haziran','Temmuz','Agustos','Eylul','Ekim','Kasim','Aralik'];
var GUNLER=['Paz','Pzt','Sal','Car','Per','Cum','Cmt'];
var SUMCOLS=['X','HT','BT','BC','M','Ui','Yi','RP','UR','G','D'];
var CELL_CLS={X:'cX',HT:'cHT',BT:'cBT',BC:'cBC',M:'cM',Ui:'cUi',Yi:'cYi',RP:'cRP',UR:'cUR',G:'cG',D:'cD','·':'cDot'};

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('on');},2500);}
function updateLabel(){document.getElementById('month-label').textContent=AYLAR[curMonth-1]+' '+curYear;}
function monthStr(){return curYear+'-'+String(curMonth).padStart(2,'0');}

function renderFilters(rows){
  var deps=[''];
  rows.forEach(function(r){if(deps.indexOf(r.dep)<0)deps.push(r.dep);});
  var bar=document.getElementById('dep-filters');
  bar.innerHTML=deps.map(function(d){
    return '<button class="filter-btn'+(d===curDep?' active':'')+'" data-dep="'+d+'">'+(d||'Tum bolumler')+'</button>';
  }).join('');
  bar.querySelectorAll('.filter-btn').forEach(function(b){
    b.addEventListener('click',function(){curDep=b.dataset.dep;renderTable(pData);});
  });
}

function renderTable(data){
  pData=data; var dim=data.dim||30; var rows=data.rows||[]; var locked=data.locked;
  renderFilters(rows);
  var filtered=curDep?rows.filter(function(r){return r.dep===curDep;}):rows;

  // Baslik
  var hc='<th class="sticky-col">Sicil</th><th class="sticky-col">Ad Soyad</th><th class="sticky-col">Bolum</th>';
  for(var d=1;d<=dim;d++){
    var dow=new Date(curYear,curMonth-1,d).getDay();
    var isHT=(dow===0||dow===6);
    hc+='<th class="'+(isHT?'ht':'')+'" title="'+GUNLER[dow]+'">'+d+'</th>';
  }
  SUMCOLS.forEach(function(c){hc+='<th class="sum-head">'+c+'</th>';});
  hc+='<th class="sum-head">TOP</th>';
  document.getElementById('pt-head').innerHTML='<tr>'+hc+'</tr>';

  // Satırlar
  var html='';
  var totals={};SUMCOLS.forEach(function(c){totals[c]=0;});var totWork=0;

  filtered.forEach(function(row){
    var counts={};SUMCOLS.forEach(function(c){counts[c]=0;});
    var cells='<td class="sticky-col">#'+row.sicil+'</td><td class="sticky-col">'+row.ad+'</td><td class="sticky-col">'+row.dep+'</td>';
    for(var d=1;d<=dim;d++){
      var code=row.days[d]||'·';
      var cls=CELL_CLS[code]||'cDot';
      cells+='<td><span class="c '+cls+'">'+code+'</span></td>';
      if(counts[code]!==undefined)counts[code]++;
      if(SUMCOLS.indexOf(code)>=0)SUMCOLS.forEach(function(c){if(c===code)totals[c]++;});
    }
    var rowTotal=0;
    SUMCOLS.forEach(function(c){cells+='<td class="sum-col">'+counts[c]+'</td>';rowTotal+=counts[c];});
    cells+='<td class="sum-col"><b>'+rowTotal+'</b></td>';
    html+='<tr>'+cells+'</tr>';
  });

  // Toplam satiri
  var sc='<td class="sticky-col"></td><td class="sticky-col"><b>TOPLAM</b></td><td class="sticky-col"></td>';
  for(var d=1;d<=dim;d++)sc+='<td></td>';
  var grandTotal=0;
  SUMCOLS.forEach(function(c){sc+='<td class="sum-col"><b>'+totals[c]+'</b></td>';grandTotal+=totals[c];});
  sc+='<td class="sum-col"><b>'+grandTotal+'</b></td>';
  html+='<tr class="sum-row">'+sc+'</tr>';

  document.getElementById('pt-body').innerHTML=html;
  document.getElementById('locked-badge').style.display=locked?'inline-block':'none';
  document.getElementById('lock-btn').textContent=locked?'Kilidi Ac':'Kilitle';
}

async function load(){
  document.getElementById('pt-body').innerHTML='<tr><td colspan="50" style="text-align:center;padding:30px;color:var(--muted)">Yukleniyor...</td></tr>';
  try{
    var data=await req('/puantaj?month='+curYear+'-'+curMonth);
    renderTable(data);
  }catch(e){
    document.getElementById('pt-body').innerHTML='<tr><td colspan="50" style="text-align:center;padding:30px;color:var(--danger)">Hata: '+e.message+'</td></tr>';
  }
}

document.getElementById('prev-btn').addEventListener('click',function(){curMonth--;if(curMonth<1){curMonth=12;curYear--;}updateLabel();load();});
document.getElementById('next-btn').addEventListener('click',function(){curMonth++;if(curMonth>12){curMonth=1;curYear++;}updateLabel();load();});

document.getElementById('lock-btn').addEventListener('click',async function(){
  if(!pData)return;
  var locked=!pData.locked;
  if(locked&&!confirm('Bu ay puantaji kilitlenecek?'))return;
  try{await req('/puantaj/lock',{method:'POST',body:{month:monthStr(),locked:locked}});toast(locked?'Kilitlendi':'Kilit acildi');load();}
  catch(e){toast('Hata: '+e.message);}
});

document.getElementById('export-btn').addEventListener('click',function(){
  if(!pData)return;
  var rows=pData.rows||[]; var dim=pData.dim||30;
  var csv='Sicil,Ad Soyad,Bolum';
  for(var d=1;d<=dim;d++)csv+=','+d;
  SUMCOLS.forEach(function(c){csv+=','+c;}); csv+=',TOPLAM\n';
  rows.forEach(function(r){
    var line=r.sicil+','+r.ad+','+r.dep;
    var counts={};SUMCOLS.forEach(function(c){counts[c]=0;});
    for(var d=1;d<=dim;d++){var code=r.days[d]||'.';line+=','+code;if(counts[code]!==undefined)counts[code]++;}
    var tot=0;
    SUMCOLS.forEach(function(c){line+=','+counts[c];tot+=counts[c];});
    line+=','+tot;
    csv+=line+'\n';
  });
  var blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download='puantaj-'+curYear+'-'+curMonth+'.csv';a.click();
});

updateLabel();load();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-puantaj">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_PUANTAJ + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
