NEW_PUANTAJ = '''<template id="tpl-puantaj">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Aylık Puantaj</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--text:#EAF2F5;--muted:#8FA6B0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;padding:22px 16px 60px}
.topbar{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:20px}
.topbar h1{font-family:'Space Grotesk';font-size:20px;font-weight:700;margin:0;flex:1}
.nav{display:flex;align-items:center;gap:8px;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:6px 10px}
.nav button{background:none;border:0;color:var(--muted);cursor:pointer;font-size:18px;padding:0 4px;line-height:1}
.nav button:hover{color:var(--text)}
.nav span{font-family:'Space Grotesk';font-weight:600;font-size:14px;min-width:120px;text-align:center}
.btn{padding:9px 16px;border-radius:9px;border:0;font-weight:600;font-size:13px;cursor:pointer;font-family:inherit}
.btn-amber{background:var(--amber);color:#1a1205}
.btn-ghost{background:var(--panel);border:1px solid var(--line);color:var(--text)}
.filters{display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap}
.filter-btn{padding:7px 14px;border-radius:8px;border:1px solid var(--line);background:var(--panel);color:var(--muted);font-size:12.5px;font-weight:600;cursor:pointer}
.filter-btn.active{background:var(--amber);color:#1a1205;border-color:var(--amber)}
.wrap{overflow-x:auto}
table{border-collapse:collapse;font-size:12px;white-space:nowrap;min-width:100%}
thead th{position:sticky;top:0;background:var(--panel);border-bottom:2px solid var(--line);padding:10px 6px;text-align:center;font-weight:600;color:var(--muted);z-index:2}
thead th:first-child,thead th:nth-child(2),thead th:nth-child(3){text-align:left;min-width:80px;padding-left:12px;position:sticky;left:0;z-index:3;background:var(--panel)}
thead th:nth-child(2){left:80px}
thead th:nth-child(3){left:160px}
thead th.ht{color:var(--blue)}
tbody td{padding:8px 6px;border-bottom:1px solid rgba(35,65,79,.4);text-align:center;vertical-align:middle}
tbody td:first-child,tbody td:nth-child(2),tbody td:nth-child(3){text-align:left;padding-left:12px;position:sticky;background:var(--panel);z-index:1}
tbody td:first-child{left:0;min-width:80px;font-family:'JetBrains Mono';font-size:11px}
tbody td:nth-child(2){left:80px;min-width:80px;font-weight:600}
tbody td:nth-child(3){left:160px;min-width:80px;color:var(--muted);font-size:11px}
tbody tr:hover td{background:var(--panel-2)}
tbody tr:hover td:first-child,tbody tr:hover td:nth-child(2),tbody tr:hover td:nth-child(3){background:var(--panel-2)}
.cell-x{background:rgba(52,217,160,.12);color:var(--mint);font-weight:700;border-radius:5px;padding:2px 5px}
.cell-ht{color:var(--blue);font-weight:600}
.cell-yi{background:rgba(111,177,255,.12);color:var(--blue);border-radius:5px;padding:2px 5px}
.cell-dot{color:var(--line)}
.cell-q{background:rgba(255,107,107,.12);color:var(--danger);font-weight:700;border-radius:5px;padding:2px 5px}
.sum-row td{background:var(--panel-2)!important;font-weight:700;border-top:2px solid var(--line)}
.legend{display:flex;gap:16px;margin-top:14px;flex-wrap:wrap}
.leg{display:flex;align-items:center;gap:6px;font-size:12px;color:var(--muted)}
.leg span{padding:2px 8px;border-radius:5px;font-weight:700;font-size:11px}
.locked-badge{background:rgba(255,107,107,.15);color:var(--danger);border:1px solid var(--danger);border-radius:7px;padding:5px 12px;font-size:12.5px;font-weight:600}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:12px 20px;border-radius:11px;font-size:13px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
</style>

<div class="topbar">
  <h1>Aylık Puantaj</h1>
  <div class="nav">
    <button id="prev-btn">‹</button>
    <span id="month-label">—</span>
    <button id="next-btn">›</button>
  </div>
  <span id="locked-badge" style="display:none" class="locked-badge">🔒 Kilitli</span>
  <button class="btn btn-ghost" id="lock-btn">Kilitle</button>
  <button class="btn btn-amber" id="export-btn">Excel</button>
</div>

<div class="filters">
  <button class="filter-btn active" data-dep="">Tüm bölümler</button>
</div>

<div class="wrap">
  <table id="puantaj-table">
    <thead id="pt-head"></thead>
    <tbody id="pt-body"></tbody>
  </table>
</div>

<div class="legend">
  <div class="leg"><span class="cell-x">X</span> Çalışıldı</div>
  <div class="leg"><span class="cell-q">?</span> Eksik çalışma (&lt;7.5 saat)</div>
  <div class="leg"><span class="cell-ht">HT</span> Hafta tatili</div>
  <div class="leg"><span class="cell-yi">Yİ</span> Yıllık izin</div>
  <div class="leg"><span class="cell-dot">·</span> Gelmedi</div>
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

var now=new Date();
var curYear=now.getFullYear();
var curMonth=now.getMonth()+1;
var curDep='';
var puantajData=null;

var AYLAR=['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık'];
var GUNLER=['Paz','Pzt','Sal','Çar','Per','Cum','Cmt'];

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('on');},2500);}

function monthStr(){return curYear+'-'+String(curMonth).padStart(2,'0');}
function updateLabel(){document.getElementById('month-label').textContent=AYLAR[curMonth-1]+' '+curYear;}

function cellClass(code){
  if(code==='X')return 'cell-x';
  if(code==='?')return 'cell-q';
  if(code==='HT')return 'cell-ht';
  if(code==='·')return 'cell-dot';
  return 'cell-yi';
}

function renderTable(data){
  puantajData=data;
  var dim=data.dim||30;
  var rows=data.rows||[];
  var locked=data.locked;

  // Deps filtresi
  var deps=[''];
  rows.forEach(function(r){if(deps.indexOf(r.dep)<0)deps.push(r.dep);});
  var fbar=document.querySelector('.filters');
  fbar.innerHTML=deps.map(function(d){
    return '<button class="filter-btn'+(d===curDep?' active':'')+'" data-dep="'+d+'">'+(d||'Tüm bölümler')+'</button>';
  }).join('');
  fbar.querySelectorAll('.filter-btn').forEach(function(b){
    b.addEventListener('click',function(){curDep=b.dataset.dep;renderTable(puantajData);});
  });

  var filtered=curDep?rows.filter(function(r){return r.dep===curDep;}):rows;

  // Başlık
  var headCols='<th>Sicil</th><th>Ad Soyad</th><th>Bölüm</th>';
  for(var d=1;d<=dim;d++){
    var dow=new Date(curYear,curMonth-1,d).getDay();
    var isHT=(dow===0);
    headCols+='<th class="'+(isHT?'ht':'')+'">'+d+'<br><small>'+GUNLER[dow]+'</small></th>';
  }
  headCols+='<th>Çalışma</th><th>İzin</th><th>FM</th>';
  document.getElementById('pt-head').innerHTML='<tr>'+headCols+'</tr>';

  // Satırlar
  var html='';
  filtered.forEach(function(row){
    var cells='<td>#'+row.sicil+'</td><td>'+row.ad+'</td><td>'+row.dep+'</td>';
    for(var d=1;d<=dim;d++){
      var code=row.days[d]||'·';
      cells+='<td><span class="'+cellClass(code)+'">'+code+'</span></td>';
    }
    cells+='<td><b>'+(row.work||0)+'</b></td>';
    cells+='<td>'+(row.leaveD||0)+'</td>';
    cells+='<td>'+(row.fm||0)+'</td>';
    html+='<tr>'+cells+'</tr>';
  });

  // Toplam satırı
  var totWork=0,totLeave=0,totFm=0;
  filtered.forEach(function(r){totWork+=(r.work||0);totLeave+=(r.leaveD||0);totFm+=(r.fm||0);});
  var sumCells='<td></td><td><b>TOPLAM</b></td><td></td>';
  for(var d=1;d<=dim;d++)sumCells+='<td></td>';
  sumCells+='<td><b>'+totWork+'</b></td><td><b>'+totLeave+'</b></td><td><b>'+totFm+'</b></td>';
  html+='<tr class="sum-row">'+sumCells+'</tr>';

  document.getElementById('pt-body').innerHTML=html;

  // Kilit durumu
  document.getElementById('locked-badge').style.display=locked?'inline-block':'none';
  document.getElementById('lock-btn').textContent=locked?'Kilidi Aç':'Kilitle';
}

async function loadPuantaj(){
  document.getElementById('pt-body').innerHTML='<tr><td colspan="40" style="text-align:center;padding:30px;color:var(--muted)">Yükleniyor…</td></tr>';
  try{
    var data=await req('/puantaj?month='+curYear+'-'+curMonth);
    renderTable(data);
  }catch(e){
    document.getElementById('pt-body').innerHTML='<tr><td colspan="40" style="text-align:center;padding:30px;color:var(--danger)">Hata: '+e.message+'</td></tr>';
  }
}

document.getElementById('prev-btn').addEventListener('click',function(){
  curMonth--;if(curMonth<1){curMonth=12;curYear--;}
  updateLabel();loadPuantaj();
});
document.getElementById('next-btn').addEventListener('click',function(){
  curMonth++;if(curMonth>12){curMonth=1;curYear++;}
  updateLabel();loadPuantaj();
});

document.getElementById('lock-btn').addEventListener('click',async function(){
  if(!puantajData)return;
  var locked=!puantajData.locked;
  if(locked&&!confirm('Bu ay puantajı kilitlenecek. Emin misiniz?'))return;
  try{
    await req('/puantaj/lock',{method:'POST',body:{month:monthStr(),locked:locked}});
    toast(locked?'Puantaj kilitlendi':'Kilit açıldı');
    loadPuantaj();
  }catch(e){toast('Hata: '+e.message);}
});

document.getElementById('export-btn').addEventListener('click',function(){
  if(!puantajData){return;}
  var rows=puantajData.rows||[];
  var dim=puantajData.dim||30;
  var csv='Sicil,Ad Soyad,Bölüm';
  for(var d=1;d<=dim;d++)csv+=','+d;
  csv+=',Çalışma,İzin,FM\n';
  rows.forEach(function(r){
    var line=r.sicil+','+r.ad+','+r.dep;
    for(var d=1;d<=dim;d++)line+','+(r.days[d]||'·');
    line+=','+(r.work||0)+','+(r.leaveD||0)+','+(r.fm||0);
    csv+=line+'\n';
  });
  var blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download='puantaj-'+curYear+'-'+curMonth+'.csv';a.click();
});

updateLabel();
loadPuantaj();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-puantaj">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_PUANTAJ + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
