NEW_VPLAN = r'''<template id="tpl-vplan">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Haftalik Vardiya Plani</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--purple:#C792EA;--orange:#FF9E6B;--text:#EAF2F5;--muted:#8FA6B0;--radius:16px;--shadow:0 24px 60px rgba(0,0,0,.45)}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d 0%,var(--ink) 55%) fixed;color:var(--text);font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:1320px;margin:0 auto;padding:22px 16px 70px}
.topbar{display:flex;align-items:center;gap:12px;margin-bottom:16px}
.logo{width:40px;height:40px;border-radius:12px;background:linear-gradient(150deg,var(--amber),#e08f1f);display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;color:#1a1205;font-size:19px}
.topbar b{font-family:'Space Grotesk';font-weight:700;font-size:17px;display:block;line-height:1.1}.topbar small{color:var(--muted);font-size:12px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);overflow:hidden}
.filters{display:flex;gap:12px;flex-wrap:wrap;align-items:flex-end;padding:16px 18px;border-bottom:1px solid var(--line)}
.f{display:flex;flex-direction:column;gap:5px}.f label{font-size:11px;color:var(--muted)}
.f select{background:var(--ink);border:1px solid var(--line);color:var(--text);border-radius:9px;padding:8px 11px;font-size:13px}
.btnbar{display:flex;gap:8px;align-items:flex-end}
.pbtn{border:1px solid var(--line);background:var(--panel-2);color:var(--text);border-radius:9px;padding:9px 14px;font-weight:600;font-size:12.5px;cursor:pointer}.pbtn:hover{border-color:var(--amber);color:var(--amber)}
.pbtn.am{background:var(--amber);color:#1a1205;border-color:var(--amber)}
.legend{display:flex;gap:8px;flex-wrap:wrap;padding:13px 18px;border-bottom:1px solid var(--line)}
.lg{display:inline-flex;align-items:center;gap:6px;font-size:11.5px;color:var(--muted)}.lg i{width:16px;height:16px;border-radius:4px;display:inline-block}
.hint{padding:10px 18px;color:var(--muted);font-size:12px;border-bottom:1px solid var(--line)}
.scroll{overflow-x:auto}
table{border-collapse:separate;border-spacing:0;width:100%;min-width:1080px}
thead th{position:sticky;top:0;background:var(--panel);color:var(--muted);font-weight:600;font-size:11px;padding:11px 10px;border-bottom:1px solid var(--line);text-align:center;z-index:2;white-space:nowrap}
thead th small{display:block;font-family:'JetBrains Mono';color:var(--muted);font-weight:500;font-size:10px;margin-top:2px}
.stick{position:sticky;left:0;background:var(--panel);z-index:3;text-align:left}
thead .stick{z-index:4}
tbody td{padding:6px 8px;border-bottom:1px solid rgba(35,65,79,.4);text-align:center}
td.stick{padding:8px 12px;border-right:1px solid var(--line)}
.emp{display:flex;align-items:center;gap:9px}.av{width:26px;height:26px;border-radius:7px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:11px;color:#1a1205;flex:0 0 auto}
.emp b{font-weight:600;font-size:12.5px}.emp small{color:var(--muted);font-size:10.5px;display:block}
.cell{min-width:96px;height:34px;line-height:1;border-radius:8px;font-family:'JetBrains Mono';font-weight:700;font-size:11px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:1px solid transparent;transition:.1s;padding:0 4px}
.cell:hover{filter:brightness(1.12)}
.footer{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;padding:14px 18px;border-top:1px solid var(--line)}
.cnt{color:var(--muted);font-size:12.5px;font-family:'JetBrains Mono'}
.toast{position:fixed;bottom:26px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:13px 20px;border-radius:12px;font-size:13.5px;font-weight:600;opacity:0;transition:.3s;box-shadow:var(--shadow);z-index:50}.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.ov{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:80}
.modal{position:fixed;inset:0;z-index:81;display:none;align-items:center;justify-content:center}
.modal.open{display:flex}
.mbox{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:24px;width:380px;max-width:92vw;box-shadow:var(--shadow)}
.mbox h3{font-family:'Space Grotesk';font-size:16px;margin:0 0 16px}
.mbox select{width:100%;background:var(--panel-2);border:1px solid var(--line);color:var(--text);border-radius:9px;padding:10px 12px;font-size:13px;margin-bottom:16px}
.mbtns{display:flex;gap:10px;justify-content:flex-end}
</style>

<div class="wrap">
  <div class="topbar">
    <div class="logo">G</div>
    <div><b>Gecit - Haftalik Vardiya Plani</b><small id="hotel-sub">vardiya atama</small></div>
  </div>
  <div class="card">
    <div class="filters">
      <div class="f"><label>Departman</label><select id="f-dep"><option value="">Tumu</option></select></div>
      <div class="f"><label>Ay</label><select id="f-month"></select></div>
      <div class="f"><label>Yil</label><select id="f-year"></select></div>
      <div class="f"><label>Hafta Secimi</label><select id="f-week"></select></div>
      <div class="btnbar">
        <button class="pbtn am" id="b-list">Listele</button>
        <button class="pbtn" id="b-transfer">&#8644; Shift Transfer</button>
      </div>
    </div>
    <div class="legend" id="legend"></div>
    <div class="hint">Bir hucreye tikla → vardiyanin degisir (A → B → ... → OFF → HT → Yi → RP → Ui). Kaydet ile puantaja yansir (sadece HT, Yi, RP, Ui, BT kayitlara gecer).</div>
    <div class="scroll"><table id="tbl"></table></div>
    <div class="footer">
      <div style="display:flex;gap:8px">
        <button class="pbtn am" id="b-save">&#10003; Kaydet</button>
        <button class="pbtn" id="b-excel">&#8595; Excel</button>
      </div>
      <div class="cnt" id="cnt"></div>
    </div>
  </div>
</div>

<div class="ov" id="tr-ov" style="display:none"></div>
<div class="modal" id="tr-modal">
  <div class="mbox">
    <h3>Shift Transfer</h3>
    <p style="color:var(--muted);font-size:13px;margin:0 0 14px">Secili haftayi hangi haftaya kopyalayalim?</p>
    <select id="tr-target"></select>
    <div class="mbtns">
      <button class="pbtn" id="tr-cancel">Iptal</button>
      <button class="pbtn am" id="tr-confirm">Transfer Et</button>
    </div>
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

var SHIFTS=[
  {code:'A',label:'A - 08:00-16:00',bg:'#1a3a2a',color:'#34D9A0'},
  {code:'B',label:'B - 16:00-00:00',bg:'#1a2a3a',color:'#6FB1FF'},
  {code:'C',label:'C - 23:59-08:00',bg:'#2a1a3a',color:'#C792EA'},
  {code:'D',label:'D - 09:00-17:00',bg:'#3a2a1a',color:'#FF9E6B'},
  {code:'E',label:'E - 13:00-21:00',bg:'#3a1a1a',color:'#F2B53B'},
  {code:'OFF',label:'OFF - Hafta tatili',bg:'#1e2a30',color:'#8FA6B0'},
  {code:'HT',label:'HT - Hafta tatili (resmi)',bg:'#1a2535',color:'#6FB1FF'},
  {code:'Yi',label:'Yi - Yillik izin',bg:'#1a2535',color:'#6FB1FF'},
  {code:'RP',label:'RP - Raporlu',bg:'#2d1a1a',color:'#FF6B6B'},
  {code:'Ui',label:'Ui - Ucretsiz izin',bg:'#2a2a1a',color:'#C792EA'},
  {code:'BT',label:'BT - Resmi tatil',bg:'#1a2535',color:'#6FB1FF'}
];
var CYCLE=SHIFTS.map(function(s){return s.code;});
var SHIFT_MAP={};SHIFTS.forEach(function(s){SHIFT_MAP[s.code]=s;});

var AYLAR=['Ocak','Subat','Mart','Nisan','Mayis','Haziran','Temmuz','Agustos','Eylul','Ekim','Kasim','Aralik'];
var GUNLER=['Paz','Pzt','Sal','Car','Per','Cum','Cmt'];

var now=new Date();
var selYear=now.getFullYear();
var selMonth=now.getMonth();
var selWeekIdx=0;
var employees=[];
var weekDays=[];
var plan={};
var allWeeks=[];
var curDep='';

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('show');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('show');},2500);}

function ini(s){var p=(s||'').trim().split(' ');return ((p[0]||'')[0]||'')+((p[1]||'')[0]||'');}

function getWeeksOfMonth(year,month){
  var weeks=[];
  var d=new Date(year,month,1);
  // Ayin ilk Pazartesisini bul
  while(d.getDay()!==1)d.setDate(d.getDate()+1);
  while(d.getMonth()===month||d.getDate()<=7){
    var start=new Date(d);
    var end=new Date(d); end.setDate(end.getDate()+6);
    weeks.push({start:start,end:end});
    d.setDate(d.getDate()+7);
    if(d.getMonth()>month&&d.getDate()>7)break;
  }
  // Ayın 1i pazartesi değilse ilk haftayı da ekle
  var first=new Date(year,month,1);
  if(first.getDay()!==1){
    var ws=new Date(first);
    while(ws.getDay()!==1)ws.setDate(ws.getDate()-1);
    var we=new Date(ws); we.setDate(we.getDate()+6);
    if(weeks.length===0||weeks[0].start.getTime()!==ws.getTime()){
      weeks.unshift({start:ws,end:we});
    }
  }
  return weeks;
}

function fmt(d){return String(d.getDate()).padStart(2,'0')+'.'+String(d.getMonth()+1).padStart(2,'0')+'.'+d.getFullYear();}
function isoDate(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}

function buildYearSelect(){
  var sel=document.getElementById('f-year');
  sel.innerHTML='';
  for(var y=selYear-1;y<=selYear+2;y++){
    var o=document.createElement('option');
    o.value=y; o.textContent=y;
    if(y===selYear)o.selected=true;
    sel.appendChild(o);
  }
}

function buildMonthSelect(){
  var sel=document.getElementById('f-month');
  sel.innerHTML='';
  AYLAR.forEach(function(m,i){
    var o=document.createElement('option');
    o.value=i; o.textContent=m;
    if(i===selMonth)o.selected=true;
    sel.appendChild(o);
  });
}

function buildWeekSelect(){
  allWeeks=getWeeksOfMonth(selYear,selMonth);
  var sel=document.getElementById('f-week');
  sel.innerHTML='';
  allWeeks.forEach(function(w,i){
    var o=document.createElement('option');
    o.value=i; o.textContent=fmt(w.start)+' - '+fmt(w.end);
    sel.appendChild(o);
  });
  sel.value=selWeekIdx;
}

function buildLegend(){
  var box=document.getElementById('legend');
  box.innerHTML=SHIFTS.map(function(s){
    return '<span class="lg"><i style="background:'+s.bg+';border:1px solid '+s.color+'"></i>'+s.label+'</span>';
  }).join('');
}

function getWeekDays(){
  var w=allWeeks[selWeekIdx];
  weekDays=[];
  for(var i=0;i<7;i++){
    var d=new Date(w.start); d.setDate(d.getDate()+i);
    weekDays.push(d);
  }
}

async function loadDeps(){
  try{
    var emps=await req('/employees');
    employees=emps.filter(function(e){return e.status==='aktif';});
    var deps=[''];
    employees.forEach(function(e){if(deps.indexOf(e.dep)<0)deps.push(e.dep);});
    var sel=document.getElementById('f-dep');
    sel.innerHTML=deps.map(function(d){return '<option value="'+d+'">'+(d||'Tumu')+'</option>';}).join('');
  }catch(e){console.log(e);}
}

async function loadPlan(){
  var w=allWeeks[selWeekIdx];
  var weekStart=isoDate(w.start);
  try{
    var data=await req('/shifts/plan?week='+weekStart);
    plan=data||{};
  }catch(e){plan={};}
}

function render(){
  getWeekDays();
  var filtered=curDep?employees.filter(function(e){return e.dep===curDep;}):employees;
  
  // Header
  var thead='<thead><tr><th class="stick" style="min-width:200px">Personel</th>';
  weekDays.forEach(function(d){
    var dow=d.getDay();
    var isHT=(dow===0||dow===6);
    thead+='<th style="'+(isHT?'color:var(--blue)':'')+'">'+ GUNLER[dow]+'<small>'+fmt(d)+'</small></th>';
  });
  thead+='</tr></thead>';

  // Body
  var tbody='<tbody>';
  filtered.forEach(function(e){
    var empPlan=plan[e.tc]||{};
    tbody+='<tr><td class="stick"><div class="emp"><div class="av" style="background:var(--amber)">'+ini(e.ad)+'</div><div><b>'+e.ad+'</b><small>'+e.dep+' - '+e.gorev+'</small></div></div></td>';
    weekDays.forEach(function(d){
      var ds=isoDate(d);
      var code=empPlan[ds]||'OFF';
      var sh=SHIFT_MAP[code]||SHIFT_MAP['OFF'];
      tbody+='<td><div class="cell" style="background:'+sh.bg+';color:'+sh.color+';border-color:'+sh.color+'20" data-tc="'+e.tc+'" data-date="'+ds+'">'+code+'</div></td>';
    });
    tbody+='</tr>';
  });
  tbody+='</tbody>';

  document.getElementById('tbl').innerHTML=thead+tbody;
  document.getElementById('cnt').textContent=filtered.length+' personel - '+fmt(allWeeks[selWeekIdx].start)+' - '+fmt(allWeeks[selWeekIdx].end);

  // Click olayları
  document.querySelectorAll('.cell').forEach(function(cell){
    cell.addEventListener('click',function(){
      var tc=cell.dataset.tc;
      var date=cell.dataset.date;
      if(!plan[tc])plan[tc]={};
      var cur=plan[tc][date]||'OFF';
      var idx=CYCLE.indexOf(cur);
      var next=CYCLE[(idx+1)%CYCLE.length];
      plan[tc][date]=next;
      var sh=SHIFT_MAP[next]||SHIFT_MAP['OFF'];
      cell.textContent=next;
      cell.style.background=sh.bg;
      cell.style.color=sh.color;
      cell.style.borderColor=sh.color+'20';
    });
  });
}

async function listele(){
  curDep=document.getElementById('f-dep').value;
  selYear=+document.getElementById('f-year').value;
  selMonth=+document.getElementById('f-month').value;
  selWeekIdx=+document.getElementById('f-week').value;
  await loadPlan();
  render();
}

document.getElementById('b-list').addEventListener('click',listele);

document.getElementById('f-year').addEventListener('change',function(){
  selYear=+this.value; buildWeekSelect(); selWeekIdx=0;
});
document.getElementById('f-month').addEventListener('change',function(){
  selMonth=+this.value; buildWeekSelect(); selWeekIdx=0;
});
document.getElementById('f-week').addEventListener('change',function(){
  selWeekIdx=+this.value;
});

document.getElementById('b-save').addEventListener('click',async function(){
  var w=allWeeks[selWeekIdx];
  var weekStart=isoDate(w.start);
  try{
    await req('/shifts/plan',{method:'PUT',body:{week:weekStart,plan:plan}});
    toast('Kaydedildi - puantaj guncellendi');
  }catch(e){toast('Hata: '+e.message);}
});

// Transfer modal
document.getElementById('b-transfer').addEventListener('click',function(){
  var sel=document.getElementById('tr-target');
  sel.innerHTML='';
  allWeeks.forEach(function(w,i){
    if(i===selWeekIdx)return;
    var o=document.createElement('option');
    o.value=i; o.textContent=fmt(w.start)+' - '+fmt(w.end);
    sel.appendChild(o);
  });
  // Diger aylarin haftalarini da ekle
  [-1,1].forEach(function(delta){
    var m=selMonth+delta; var y=selYear;
    if(m<0){m=11;y--;}if(m>11){m=0;y++;}
    var weeks=getWeeksOfMonth(y,m);
    weeks.forEach(function(w){
      var o=document.createElement('option');
      o.value='other_'+isoDate(w.start);
      o.textContent=AYLAR[m]+' - '+fmt(w.start)+' - '+fmt(w.end);
      sel.appendChild(o);
    });
  });
  document.getElementById('tr-ov').style.display='block';
  document.getElementById('tr-modal').classList.add('open');
});

document.getElementById('tr-cancel').addEventListener('click',function(){
  document.getElementById('tr-ov').style.display='none';
  document.getElementById('tr-modal').classList.remove('open');
});
document.getElementById('tr-ov').addEventListener('click',function(){
  document.getElementById('tr-ov').style.display='none';
  document.getElementById('tr-modal').classList.remove('open');
});

document.getElementById('tr-confirm').addEventListener('click',async function(){
  var val=document.getElementById('tr-target').value;
  var targetWeekStart;
  if(val.startsWith('other_')){
    targetWeekStart=val.replace('other_','');
  } else {
    targetWeekStart=isoDate(allWeeks[+val].start);
  }
  // Mevcut haftanin planini hedef haftaya kopyala - tarihleri shift et
  var srcStart=allWeeks[selWeekIdx].start;
  var tgtStart=new Date(targetWeekStart);
  var diffDays=Math.round((tgtStart-srcStart)/(86400000));
  var newPlan={};
  Object.keys(plan).forEach(function(tc){
    newPlan[tc]={};
    Object.keys(plan[tc]).forEach(function(date){
      var d=new Date(date); d.setDate(d.getDate()+diffDays);
      newPlan[tc][isoDate(d)]=plan[tc][date];
    });
  });
  try{
    await req('/shifts/plan',{method:'PUT',body:{week:targetWeekStart,plan:newPlan}});
    toast('Transfer tamamlandi');
  }catch(e){toast('Hata: '+e.message);}
  document.getElementById('tr-ov').style.display='none';
  document.getElementById('tr-modal').classList.remove('open');
});

document.getElementById('b-excel').addEventListener('click',function(){
  if(!weekDays.length)return;
  var filtered=curDep?employees.filter(function(e){return e.dep===curDep;}):employees;
  var csv='Sicil,Ad Soyad,Bolum';
  weekDays.forEach(function(d){csv+=','+fmt(d);});
  csv+='\n';
  filtered.forEach(function(e){
    var line=e.sicil+','+e.ad+','+e.dep;
    weekDays.forEach(function(d){line+=','+(plan[e.tc]&&plan[e.tc][isoDate(d)]||'OFF');});
    csv+=line+'\n';
  });
  var blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download='shift-'+isoDate(allWeeks[selWeekIdx].start)+'.csv';a.click();
});

// Init
buildYearSelect();
buildMonthSelect();
buildWeekSelect();
buildLegend();

(async function(){
  await loadDeps();
  await loadPlan();
  render();
})();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-vplan">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_VPLAN + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
