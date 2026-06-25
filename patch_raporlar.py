NEW_RAPORLAR = r'''<template id="tpl-raporlar">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Raporlar</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--text:#EAF2F5;--muted:#8FA6B0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;padding:18px 16px 60px}
.topbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:16px}
.topbar h1{font-family:'Space Grotesk';font-size:18px;font-weight:700;margin:0;flex:1}
.tabs{display:flex;gap:6px;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:5px}
.tab{padding:7px 14px;border-radius:7px;border:0;background:transparent;color:var(--muted);font-size:13px;font-weight:600;cursor:pointer;font-family:inherit}
.tab.active{background:var(--amber);color:#1a1205}
.section{display:none}.section.active{display:block}
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
table{width:100%;border-collapse:collapse;font-size:12px}
thead th{text-align:left;font-size:10.5px;color:var(--muted);font-weight:600;padding:9px 12px;border-bottom:1px solid var(--line);white-space:nowrap;text-transform:uppercase}
tbody td{padding:8px 12px;border-bottom:1px solid rgba(35,65,79,.35);vertical-align:middle}
tbody tr:hover td{background:rgba(27,49,62,.4)}
.mono{font-family:'JetBrains Mono';font-size:11.5px}
.pill{display:inline-flex;align-items:center;font-size:10.5px;font-weight:600;padding:2px 7px;border-radius:5px}
.p-ok{background:rgba(52,217,160,.15);color:var(--mint)}
.p-warn{background:rgba(255,107,107,.15);color:var(--danger)}
.p-amber{background:rgba(242,181,59,.15);color:var(--amber)}
.p-blue{background:rgba(111,177,255,.15);color:var(--blue)}
.who{display:flex;align-items:center;gap:8px}
.av{width:26px;height:26px;border-radius:7px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:10px;color:#1a1205;background:var(--amber);flex:0 0 auto}
.empty{text-align:center;color:var(--muted);padding:40px;font-size:13px}
.footer-bar{display:flex;align-items:center;justify-content:space-between;padding:8px 16px;border-top:1px solid var(--line)}
.footer-bar span{color:var(--muted);font-size:11.5px}
.stat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px;padding:14px 16px}
.stat-card{background:var(--panel-2);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.stat-card .val{font-family:'Space Grotesk';font-size:28px;font-weight:700;margin-bottom:4px}
.stat-card .lbl{color:var(--muted);font-size:12px}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:11px 18px;border-radius:10px;font-size:12.5px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
</style>

<div class="topbar">
  <h1>Raporlar</h1>
  <div class="tabs" id="rap-tabs">
    <button class="tab active" data-t="devamsizlik">Devamsizlik</button>
    <button class="tab" data-t="gec-giris">Gec Giris</button>
    <button class="tab" data-t="fm">Fazla Mesai</button>
    <button class="tab" data-t="ozet">Personel Ozeti</button>
  </div>
</div>

<!-- DEVAMSIZLIK RAPORU -->
<div class="section active" id="sec-devamsizlik">
  <div class="card">
    <div class="filter-bar">
      <div class="f"><label>Baslangic</label><input type="date" id="dev-start"></div>
      <div class="f"><label>Bitis</label><input type="date" id="dev-end"></div>
      <div class="f"><label>Departman</label><select id="dev-dep"><option value="">Tumu</option></select></div>
      <div class="f" style="justify-content:flex-end">
        <label>&nbsp;</label>
        <div style="display:flex;gap:6px">
          <button class="btn btn-ghost" id="dev-excel">&#8595; Excel</button>
          <button class="btn btn-amber" id="dev-listele">Listele</button>
        </div>
      </div>
    </div>
    <div class="stat-grid" id="dev-stats" style="display:none">
      <div class="stat-card"><div class="val" id="dev-s1">0</div><div class="lbl">Toplam Devamsizlik</div></div>
      <div class="stat-card"><div class="val" id="dev-s2">0</div><div class="lbl">Etkilenen Personel</div></div>
      <div class="stat-card"><div class="val" id="dev-s3">0</div><div class="lbl">En Cok Devamsiz Dep.</div></div>
    </div>
    <table><thead><tr><th>Sicil</th><th>Ad Soyad</th><th>Departman</th><th>Tarih</th><th>Gun</th><th>Planlanan Vardiya</th></tr></thead>
      <tbody id="dev-body"><tr><td colspan="6" class="empty">Listele butonuna basin...</td></tr></tbody>
    </table>
    <div class="footer-bar"><span id="dev-cnt">-</span></div>
  </div>
</div>

<!-- GEC GIRIS RAPORU -->
<div class="section" id="sec-gec-giris">
  <div class="card">
    <div class="filter-bar">
      <div class="f"><label>Baslangic</label><input type="date" id="gec-start"></div>
      <div class="f"><label>Bitis</label><input type="date" id="gec-end"></div>
      <div class="f"><label>Departman</label><select id="gec-dep"><option value="">Tumu</option></select></div>
      <div class="f"><label>Tolerans (dk)</label><input type="number" id="gec-tol" value="15" style="width:80px"></div>
      <div class="f" style="justify-content:flex-end">
        <label>&nbsp;</label>
        <div style="display:flex;gap:6px">
          <button class="btn btn-ghost" id="gec-excel">&#8595; Excel</button>
          <button class="btn btn-amber" id="gec-listele">Listele</button>
        </div>
      </div>
    </div>
    <div class="stat-grid" id="gec-stats" style="display:none">
      <div class="stat-card"><div class="val" id="gec-s1">0</div><div class="lbl">Toplam Gec Giris</div></div>
      <div class="stat-card"><div class="val" id="gec-s2">0</div><div class="lbl">Etkilenen Personel</div></div>
      <div class="stat-card"><div class="val" id="gec-s3">0</div><div class="lbl">Ort. Gecikme (dk)</div></div>
    </div>
    <table><thead><tr><th>Sicil</th><th>Ad Soyad</th><th>Departman</th><th>Tarih</th><th>Vardiya Baslangici</th><th>Giris Saati</th><th>Gecikme</th></tr></thead>
      <tbody id="gec-body"><tr><td colspan="7" class="empty">Listele butonuna basin...</td></tr></tbody>
    </table>
    <div class="footer-bar"><span id="gec-cnt">-</span></div>
  </div>
</div>

<!-- FAZLA MESAİ RAPORU -->
<div class="section" id="sec-fm">
  <div class="card">
    <div class="filter-bar">
      <div class="f"><label>Ay</label><select id="fm-month"></select></div>
      <div class="f"><label>Yil</label><select id="fm-year"></select></div>
      <div class="f"><label>Departman</label><select id="fm-dep"><option value="">Tumu</option></select></div>
      <div class="f" style="justify-content:flex-end">
        <label>&nbsp;</label>
        <div style="display:flex;gap:6px">
          <button class="btn btn-ghost" id="fm-excel">&#8595; Excel</button>
          <button class="btn btn-amber" id="fm-listele">Listele</button>
        </div>
      </div>
    </div>
    <div class="stat-grid" id="fm-stats" style="display:none">
      <div class="stat-card"><div class="val" id="fm-s1">0</div><div class="lbl">Toplam FM (saat)</div></div>
      <div class="stat-card"><div class="val" id="fm-s2">0</div><div class="lbl">FM'li Personel</div></div>
      <div class="stat-card"><div class="val" id="fm-s3">0</div><div class="lbl">En Fazla FM</div></div>
    </div>
    <table><thead><tr><th>Sicil</th><th>Ad Soyad</th><th>Departman</th><th>Toplam FM (saat)</th><th>FM Gun Sayisi</th><th>Yillik Kalan</th><th>Durum</th></tr></thead>
      <tbody id="fm-body"><tr><td colspan="7" class="empty">Listele butonuna basin...</td></tr></tbody>
    </table>
    <div class="footer-bar"><span id="fm-cnt">-</span></div>
  </div>
</div>

<!-- PERSONEL OZETİ -->
<div class="section" id="sec-ozet">
  <div class="card">
    <div class="filter-bar">
      <div class="f"><label>Ay</label><select id="oz-month"></select></div>
      <div class="f"><label>Yil</label><select id="oz-year"></select></div>
      <div class="f"><label>Departman</label><select id="oz-dep"><option value="">Tumu</option></select></div>
      <div class="f" style="justify-content:flex-end">
        <label>&nbsp;</label>
        <div style="display:flex;gap:6px">
          <button class="btn btn-ghost" id="oz-excel">&#8595; Excel</button>
          <button class="btn btn-amber" id="oz-listele">Listele</button>
        </div>
      </div>
    </div>
    <table><thead><tr><th>Sicil</th><th>Ad Soyad</th><th>Departman</th><th>Calisma Gun</th><th>Devamsizlik</th><th>HT Calisma</th><th>FM (saat)</th><th>Gece Cal.</th><th>Izin Gun</th></tr></thead>
      <tbody id="oz-body"><tr><td colspan="9" class="empty">Listele butonuna basin...</td></tr></tbody>
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
var GUNLER=['Pazar','Pazartesi','Sali','Carsamba','Persembe','Cuma','Cumartesi'];
var now=new Date();

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('on');},2500);}
function isoDate(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function ini(s){var p=(s||'').trim().split(' ');return((p[0]||'')[0]||'')+((p[1]||'')[0]||'');}
function fmtM(m){if(m==null||m<0)return '-';return String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0');}
function timeMins(g,c){if(!g||!c)return null;var gp=g.split(':').map(Number);var cp=c.split(':').map(Number);var m=(cp[0]*60+cp[1])-(gp[0]*60+gp[1]);if(m<0)m+=1440;return m;}

// Bugun + aybaslangic
var todayStr=isoDate(now);
var monthStart=isoDate(new Date(now.getFullYear(),now.getMonth(),1));
document.getElementById('dev-start').value=monthStart;
document.getElementById('dev-end').value=todayStr;
document.getElementById('gec-start').value=monthStart;
document.getElementById('gec-end').value=todayStr;

// Ay/yil select'leri
function buildMonthYear(mId,yId){
  var ms=document.getElementById(mId); var ys=document.getElementById(yId);
  ms.innerHTML=AYLAR.map(function(a,i){return '<option value="'+(i+1)+'"'+(i===now.getMonth()?' selected':'')+'>'+a+'</option>';}).join('');
  ys.innerHTML=''; for(var y=now.getFullYear()-1;y<=now.getFullYear()+1;y++){var o=document.createElement('option');o.value=y;o.textContent=y;if(y===now.getFullYear())o.selected=true;ys.appendChild(o);}
}
buildMonthYear('fm-month','fm-year');
buildMonthYear('oz-month','oz-year');

// Tab sistemi
document.querySelectorAll('#rap-tabs .tab').forEach(function(t){
  t.addEventListener('click',function(){
    document.querySelectorAll('#rap-tabs .tab').forEach(function(x){x.classList.remove('active');});
    document.querySelectorAll('.section').forEach(function(x){x.classList.remove('active');});
    t.classList.add('active');
    document.getElementById('sec-'+t.dataset.t).classList.add('active');
  });
});

function csvExport(headers,rows,filename){
  var csv=headers.join(',')+'\n';
  rows.forEach(function(r){csv+=r.map(function(v){return '"'+(v||'')+'"';}).join(',')+'\n';});
  var blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=filename;a.click();
}

function depFilter(data,depSel){
  var dep=document.getElementById(depSel).value;
  return dep?data.filter(function(r){return r.dep===dep;}):data;
}

// ========== DEVAMSIZLIK ==========
document.getElementById('dev-listele').addEventListener('click',async function(){
  var start=document.getElementById('dev-start').value;
  var end=document.getElementById('dev-end').value;
  document.getElementById('dev-body').innerHTML='<tr><td colspan="6" class="empty">Yukleniyor...</td></tr>';
  try{
    var data=await req('/attendance/report?start='+start+'&end='+end);
    // Gelmedi satırları
    var rows=data.filter(function(r){return r.status==='gelmedi';});
    rows=depFilter(rows,'dev-dep');
    // Dep filtresi doldur
    var deps=[''];data.forEach(function(r){if(deps.indexOf(r.dep)<0)deps.push(r.dep);});
    document.getElementById('dev-dep').innerHTML=deps.map(function(d){return '<option value="'+d+'">'+(d||'Tumu')+'</option>';}).join('');
    // Stats
    var uniq={}; rows.forEach(function(r){uniq[r.tc]=1;});
    var depCount={}; rows.forEach(function(r){depCount[r.dep]=(depCount[r.dep]||0)+1;});
    var topDep=Object.keys(depCount).sort(function(a,b){return depCount[b]-depCount[a];})[0]||'-';
    document.getElementById('dev-s1').textContent=rows.length;
    document.getElementById('dev-s2').textContent=Object.keys(uniq).length;
    document.getElementById('dev-s3').textContent=topDep;
    document.getElementById('dev-stats').style.display='grid';
    if(!rows.length){document.getElementById('dev-body').innerHTML='<tr><td colspan="6" class="empty">Devamsizlik kaydi yok</td></tr>';document.getElementById('dev-cnt').textContent='0 kayit';return;}
    document.getElementById('dev-body').innerHTML=rows.map(function(r){
      var dow=new Date(r.day+'T12:00:00').getDay();
      return '<tr><td class="mono" style="color:var(--muted)">#'+r.sicil+'</td>'
        +'<td><div class="who"><div class="av">'+ini(r.ad)+'</div><b>'+r.ad+'</b></div></td>'
        +'<td style="color:var(--muted);font-size:11.5px">'+r.dep+'</td>'
        +'<td class="mono">'+r.day+'</td>'
        +'<td style="font-size:11.5px">'+GUNLER[dow]+'</td>'
        +'<td style="color:var(--blue);font-size:11.5px">'+(r.plannedShift||'-')+'</td></tr>';
    }).join('');
    document.getElementById('dev-cnt').textContent=rows.length+' devamsizlik';
  }catch(e){document.getElementById('dev-body').innerHTML='<tr><td colspan="6" class="empty">Hata: '+e.message+'</td></tr>';}
});

document.getElementById('dev-excel').addEventListener('click',function(){
  var rows=Array.from(document.querySelectorAll('#dev-body tr')).filter(function(r){return !r.querySelector('td.empty');});
  csvExport(['Sicil','Ad Soyad','Departman','Tarih','Gun','Planlanan Vardiya'],rows.map(function(r){
    var cells=r.querySelectorAll('td'); return [cells[0].textContent,cells[1].textContent,cells[2].textContent,cells[3].textContent,cells[4].textContent,cells[5].textContent];
  }),'devamsizlik-raporu.csv');
});

// ========== GEC GIRIS ==========
document.getElementById('gec-listele').addEventListener('click',async function(){
  var start=document.getElementById('gec-start').value;
  var end=document.getElementById('gec-end').value;
  var tol=+document.getElementById('gec-tol').value||15;
  document.getElementById('gec-body').innerHTML='<tr><td colspan="7" class="empty">Yukleniyor...</td></tr>';
  try{
    var data=await req('/attendance/report?start='+start+'&end='+end);
    var gecRows=[];
    // Ayarlardan vardiya bilgilerini al
    var settings=await req('/settings').catch(function(){return {};});
    var shiftDefs=(settings.shifts||[]);
    data.filter(function(r){return r.giris;}).forEach(function(r){
      if(!r.plannedShift||r.plannedShift==='-')return;
      var shKey=r.plannedShift.split(' ')[0];
      var shDef=shiftDefs.find(function(s){return s.code===shKey;});
      if(!shDef||!shDef.start)return;
      var sp=shDef.start.split(':').map(Number);
      var gp=r.giris.split(':').map(Number);
      var planMins=sp[0]*60+sp[1];
      var girisMins=gp[0]*60+gp[1];
      var diff=girisMins-planMins;
      if(diff<0)diff+=1440;
      if(diff>tol&&diff<720){
        gecRows.push({r:r,shiftStart:shDef.start,gecikme:diff});
      }
    });
    gecRows=gecRows.filter(function(x){return !document.getElementById('gec-dep').value||x.r.dep===document.getElementById('gec-dep').value;});
    var deps=[''];data.forEach(function(r){if(deps.indexOf(r.dep)<0)deps.push(r.dep);});
    document.getElementById('gec-dep').innerHTML=deps.map(function(d){return '<option value="'+d+'">'+(d||'Tumu')+'</option>';}).join('');
    var uniq2={}; gecRows.forEach(function(x){uniq2[x.r.tc]=1;});
    var avgGec=gecRows.length?Math.round(gecRows.reduce(function(s,x){return s+x.gecikme;},0)/gecRows.length):0;
    document.getElementById('gec-s1').textContent=gecRows.length;
    document.getElementById('gec-s2').textContent=Object.keys(uniq2).length;
    document.getElementById('gec-s3').textContent=avgGec+' dk';
    document.getElementById('gec-stats').style.display='grid';
    if(!gecRows.length){document.getElementById('gec-body').innerHTML='<tr><td colspan="7" class="empty">Gec giris kaydi yok</td></tr>';document.getElementById('gec-cnt').textContent='0 kayit';return;}
    document.getElementById('gec-body').innerHTML=gecRows.map(function(x){
      return '<tr><td class="mono" style="color:var(--muted)">#'+x.r.sicil+'</td>'
        +'<td><div class="who"><div class="av">'+ini(x.r.ad)+'</div><b>'+x.r.ad+'</b></div></td>'
        +'<td style="color:var(--muted);font-size:11.5px">'+x.r.dep+'</td>'
        +'<td class="mono">'+x.r.day+'</td>'
        +'<td class="mono">'+x.shiftStart+'</td>'
        +'<td class="mono">'+x.r.giris+'</td>'
        +'<td><span class="pill p-warn">+'+x.gecikme+' dk</span></td></tr>';
    }).join('');
    document.getElementById('gec-cnt').textContent=gecRows.length+' gec giris';
  }catch(e){document.getElementById('gec-body').innerHTML='<tr><td colspan="7" class="empty">Hata: '+e.message+'</td></tr>';}
});

document.getElementById('gec-excel').addEventListener('click',function(){
  var rows=Array.from(document.querySelectorAll('#gec-body tr')).filter(function(r){return !r.querySelector('td.empty');});
  csvExport(['Sicil','Ad Soyad','Departman','Tarih','Planlanan','Giris','Gecikme'],rows.map(function(r){
    var c=r.querySelectorAll('td');return[c[0].textContent,c[1].textContent,c[2].textContent,c[3].textContent,c[4].textContent,c[5].textContent,c[6].textContent];
  }),'gec-giris-raporu.csv');
});

// ========== FAZLA MESAİ ==========
document.getElementById('fm-listele').addEventListener('click',async function(){
  var month=+document.getElementById('fm-month').value;
  var year=+document.getElementById('fm-year').value;
  var pad=function(n){return String(n).padStart(2,'0');};
  var start=year+'-'+pad(month)+'-01';
  var lastDay=new Date(year,month,0).getDate();
  var end=year+'-'+pad(month)+'-'+lastDay;
  document.getElementById('fm-body').innerHTML='<tr><td colspan="7" class="empty">Yukleniyor...</td></tr>';
  try{
    var data=await req('/attendance/report?start='+start+'&end='+end);
    var empFM={};
    data.filter(function(r){return r.giris&&r.cikis;}).forEach(function(r){
      var m=timeMins(r.giris,r.cikis);
      if(m!=null&&m>540){
        if(!empFM[r.tc])empFM[r.tc]={tc:r.tc,ad:r.ad,dep:r.dep,sicil:r.sicil,totalFm:0,days:0};
        empFM[r.tc].totalFm+=m-540;
        empFM[r.tc].days++;
      }
    });
    var fmRows=Object.values(empFM);
    var dep=document.getElementById('fm-dep').value;
    if(dep)fmRows=fmRows.filter(function(r){return r.dep===dep;});
    var deps=[''];data.forEach(function(r){if(deps.indexOf(r.dep)<0)deps.push(r.dep);});
    document.getElementById('fm-dep').innerHTML=deps.map(function(d){return '<option value="'+d+'">'+(d||'Tumu')+'</option>';}).join('');
    var totalFmH=fmRows.reduce(function(s,r){return s+r.totalFm;},0)/60;
    var maxEmp=fmRows.sort(function(a,b){return b.totalFm-a.totalFm;})[0];
    document.getElementById('fm-s1').textContent=totalFmH.toFixed(1);
    document.getElementById('fm-s2').textContent=fmRows.length;
    document.getElementById('fm-s3').textContent=maxEmp?(maxEmp.ad.split(' ')[0]+': '+Math.round(maxEmp.totalFm/60)+'s'):'-';
    document.getElementById('fm-stats').style.display='grid';
    if(!fmRows.length){document.getElementById('fm-body').innerHTML='<tr><td colspan="7" class="empty">FM kaydi yok</td></tr>';document.getElementById('fm-cnt').textContent='0 kayit';return;}
    document.getElementById('fm-body').innerHTML=fmRows.map(function(r){
      var fmH=r.totalFm/60;
      var kalanH=Math.max(0,270-fmH);
      var status=fmH>200?'<span class="pill p-warn">Limite Yaklasıyor</span>':'<span class="pill p-ok">Normal</span>';
      return '<tr><td class="mono" style="color:var(--muted)">#'+r.sicil+'</td>'
        +'<td><div class="who"><div class="av">'+ini(r.ad)+'</div><b>'+r.ad+'</b></div></td>'
        +'<td style="color:var(--muted);font-size:11.5px">'+r.dep+'</td>'
        +'<td class="mono"><b>'+fmH.toFixed(1)+'</b></td>'
        +'<td class="mono">'+r.days+'</td>'
        +'<td class="mono">'+kalanH.toFixed(1)+'</td>'
        +'<td>'+status+'</td></tr>';
    }).join('');
    document.getElementById('fm-cnt').textContent=fmRows.length+' personel';
  }catch(e){document.getElementById('fm-body').innerHTML='<tr><td colspan="7" class="empty">Hata: '+e.message+'</td></tr>';}
});

document.getElementById('fm-excel').addEventListener('click',function(){
  var rows=Array.from(document.querySelectorAll('#fm-body tr')).filter(function(r){return !r.querySelector('td.empty');});
  csvExport(['Sicil','Ad Soyad','Departman','FM (saat)','Gun','Yillik Kalan','Durum'],rows.map(function(r){
    var c=r.querySelectorAll('td');return[c[0].textContent,c[1].textContent,c[2].textContent,c[3].textContent,c[4].textContent,c[5].textContent,c[6].textContent];
  }),'fm-raporu.csv');
});

// ========== PERSONEL OZETİ ==========
document.getElementById('oz-listele').addEventListener('click',async function(){
  var month=+document.getElementById('oz-month').value;
  var year=+document.getElementById('oz-year').value;
  var pad=function(n){return String(n).padStart(2,'0');};
  var start=year+'-'+pad(month)+'-01';
  var lastDay=new Date(year,month,0).getDate();
  var end=year+'-'+pad(month)+'-'+lastDay;
  document.getElementById('oz-body').innerHTML='<tr><td colspan="9" class="empty">Yukleniyor...</td></tr>';
  try{
    var [attData, puantajData] = await Promise.all([
      req('/attendance/report?start='+start+'&end='+end),
      req('/puantaj?month='+year+'-'+month)
    ]);
    var empMap={};
    attData.forEach(function(r){
      if(!empMap[r.tc])empMap[r.tc]={tc:r.tc,ad:r.ad,dep:r.dep,sicil:r.sicil,work:0,miss:0,fm:0,gece:0,izin:0};
      if(r.giris){
        empMap[r.tc].work++;
        var m=timeMins(r.giris,r.cikis);
        if(m!=null&&m>540)empMap[r.tc].fm+=m-540;
      } else if(r.status==='gelmedi'){
        empMap[r.tc].miss++;
      }
    });
    // Puantajdan izin + gece bilgisi
    if(puantajData && puantajData.rows){
      puantajData.rows.forEach(function(row){
        if(!empMap[row.tc])return;
        empMap[row.tc].izin=row.leaveD||0;
        empMap[row.tc].gece=row.geceCalisma||0;
      });
    }
    var dep=document.getElementById('oz-dep').value;
    var rows=Object.values(empMap);
    if(dep)rows=rows.filter(function(r){return r.dep===dep;});
    var deps=[''];attData.forEach(function(r){if(deps.indexOf(r.dep)<0)deps.push(r.dep);});
    document.getElementById('oz-dep').innerHTML=deps.map(function(d){return '<option value="'+d+'">'+(d||'Tumu')+'</option>';}).join('');
    if(!rows.length){document.getElementById('oz-body').innerHTML='<tr><td colspan="9" class="empty">Kayit yok</td></tr>';document.getElementById('oz-cnt').textContent='0 personel';return;}
    document.getElementById('oz-body').innerHTML=rows.sort(function(a,b){return a.dep.localeCompare(b.dep)||a.ad.localeCompare(b.ad);}).map(function(r){
      var fmH=(r.fm/60).toFixed(1);
      return '<tr><td class="mono" style="color:var(--muted)">#'+r.sicil+'</td>'
        +'<td><div class="who"><div class="av">'+ini(r.ad)+'</div><b>'+r.ad+'</b></div></td>'
        +'<td style="color:var(--muted);font-size:11.5px">'+r.dep+'</td>'
        +'<td class="mono"><b>'+r.work+'</b></td>'
        +'<td class="mono">'+(r.miss>0?('<span style="color:var(--danger)">'+r.miss+'</span>'):r.miss)+'</td>'
        +'<td class="mono">'+(r.gece>0?('<span style="color:var(--blue)">'+r.gece+'</span>'):r.gece)+'</td>'
        +'<td class="mono">'+(r.fm>0?('<span style="color:var(--amber)">'+fmH+'</span>'):fmH)+'</td>'
        +'<td class="mono">'+r.gece+'</td>'
        +'<td class="mono">'+r.izin+'</td></tr>';
    }).join('');
    document.getElementById('oz-cnt').textContent=rows.length+' personel';
  }catch(e){document.getElementById('oz-body').innerHTML='<tr><td colspan="9" class="empty">Hata: '+e.message+'</td></tr>';}
});

document.getElementById('oz-excel').addEventListener('click',function(){
  var rows=Array.from(document.querySelectorAll('#oz-body tr')).filter(function(r){return !r.querySelector('td.empty');});
  csvExport(['Sicil','Ad Soyad','Departman','Calisma Gun','Devamsizlik','HT Calisma','FM (saat)','Gece Cal.','Izin Gun'],rows.map(function(r){
    var c=r.querySelectorAll('td');return[c[0].textContent,c[1].textContent,c[2].textContent,c[3].textContent,c[4].textContent,c[5].textContent,c[6].textContent,c[7].textContent,c[8].textContent];
  }),'personel-ozet.csv');
});
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-raporlar">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_RAPORLAR + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
