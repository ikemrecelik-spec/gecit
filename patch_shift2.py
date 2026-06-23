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
.cell:hover{filter:brightness(1.15)}
.footer{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;padding:14px 18px;border-top:1px solid var(--line)}
.cnt{color:var(--muted);font-size:12.5px;font-family:'JetBrains Mono'}
.toast{position:fixed;bottom:26px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:13px 20px;border-radius:12px;font-size:13.5px;font-weight:600;opacity:0;transition:.3s;box-shadow:var(--shadow);z-index:50}.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.ov{position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:80;display:none}
.modal{position:fixed;inset:0;z-index:81;display:none;align-items:center;justify-content:center}
.modal.open{display:flex}
.mbox{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:24px;width:400px;max-width:92vw;box-shadow:var(--shadow)}
.mbox h3{font-family:'Space Grotesk';font-size:16px;margin:0 0 14px}
.mrow{display:flex;gap:10px;margin-bottom:12px}
.mrow .f{flex:1}
.mrow select{width:100%;background:var(--panel-2);border:1px solid var(--line);color:var(--text);border-radius:9px;padding:9px 11px;font-size:13px}
.mbtns{display:flex;gap:10px;justify-content:flex-end;margin-top:4px}
</style>

<div class="wrap">
  <div class="topbar">
    <div class="logo">G</div>
    <div><b>Gecit - Haftalik Vardiya Plani</b><small>vardiya atama (Sef / IK)</small></div>
  </div>
  <div class="card">
    <div class="filters">
      <div class="f"><label>Departman</label><select id="f-dep"><option value="">Tumu</option></select></div>
      <div class="f"><label>Ay</label><select id="f-month"></select></div>
      <div class="f"><label>Yil</label><select id="f-year"></select></div>
      <div class="f"><label>Hafta</label><select id="f-week"></select></div>
      <div class="btnbar">
        <button class="pbtn am" id="b-list">Listele</button>
        <button class="pbtn" id="b-transfer">&#8644; Shift Transfer</button>
      </div>
    </div>
    <div class="legend" id="legend"></div>
    <div class="hint">Hucreye tikla: A -> B -> C -> D -> E -> OFF -> HT -> Yi -> RP -> Ui -> BT -> A. Kaydet ile puantaja yansir.</div>
    <div class="scroll"><table id="tbl"><thead></thead><tbody><tr><td colspan="8" style="text-align:center;padding:30px;color:var(--muted)">Listele butonuna basin...</td></tr></tbody></table></div>
    <div class="footer">
      <div style="display:flex;gap:8px">
        <button class="pbtn am" id="b-save">&#10003; Kaydet</button>
        <button class="pbtn" id="b-excel">&#8595; Excel</button>
      </div>
      <div class="cnt" id="cnt"></div>
    </div>
  </div>
</div>

<div class="ov" id="tr-ov"></div>
<div class="modal" id="tr-modal">
  <div class="mbox">
    <h3>Shift Transfer</h3>
    <p style="color:var(--muted);font-size:13px;margin:0 0 14px">Secili haftayi baska bir haftaya kopyala:</p>
    <div class="mrow">
      <div class="f"><label>Yil</label><select id="tr-year"></select></div>
      <div class="f"><label>Ay</label><select id="tr-month"></select></div>
    </div>
    <div class="f" style="margin-bottom:14px"><label>Hafta</label><select id="tr-week" style="width:100%;background:var(--panel-2);border:1px solid var(--line);color:var(--text);border-radius:9px;padding:9px 11px;font-size:13px"></select></div>
    <div class="mbtns">
      <button class="pbtn" id="tr-cancel">Iptal</button>
      <button class="pbtn am" id="tr-confirm">Transfer Et</button>
    </div>
  </div>
</div>
<div class="toast" id="toast"></div>

<script>
function getG(){try{return window.parent&&window.parent.GECIT||null;}catch(e){return null;}}
async function apiReq(path,opts){
  var g=getG(); var tenant=(g&&g._tenant)||'1'; var tok=(g&&g._token)||null;
  opts=opts||{}; var h={'Content-Type':'application/json'};
  if(tok)h['Authorization']='Bearer '+tok;
  var r=await fetch('https://gecitpdks.duckdns.org/api/'+tenant+path,{method:opts.method||'GET',headers:h,body:opts.body?JSON.stringify(opts.body):undefined});
  var d=null;try{d=await r.json();}catch(e){}
  if(!r.ok)throw new Error((d&&d.error)||('Hata '+r.status));
  return d;
}

var SHIFTS=[
  {code:'A',label:'A - 08:00-16:00',bg:'#0d2e1e',color:'#34D9A0'},
  {code:'B',label:'B - 16:00-00:00',bg:'#0d1e2e',color:'#6FB1FF'},
  {code:'C',label:'C - 00:00-08:00',bg:'#1e0d2e',color:'#C792EA'},
  {code:'D',label:'D - 09:00-17:00',bg:'#2e1e0d',color:'#FF9E6B'},
  {code:'E',label:'E - 13:00-21:00',bg:'#2e200d',color:'#F2B53B'},
  {code:'OFF',label:'OFF - Tatil',bg:'#141e24',color:'#8FA6B0'},
  {code:'HT',label:'HT - Hafta tatili',bg:'#0d1a2e',color:'#6FB1FF'},
  {code:'Yi',label:'Yi - Yillik izin',bg:'#0d1a2e',color:'#6FB1FF'},
  {code:'RP',label:'RP - Raporlu',bg:'#2e0d0d',color:'#FF6B6B'},
  {code:'Ui',label:'Ui - Ucretsiz izin',bg:'#1e1a0d',color:'#C792EA'},
  {code:'BT',label:'BT - Resmi tatil',bg:'#0d1a2e',color:'#6FB1FF'}
];
var CYCLE=SHIFTS.map(function(s){return s.code;});
var SHIFT_MAP={};SHIFTS.forEach(function(s){SHIFT_MAP[s.code]=s;});
var AYLAR=['Ocak','Subat','Mart','Nisan','Mayis','Haziran','Temmuz','Agustos','Eylul','Ekim','Kasim','Aralik'];
var GUNLER=['Paz','Pzt','Sal','Car','Per','Cum','Cmt'];

var now=new Date();
var state={year:now.getFullYear(),month:now.getMonth(),weekIdx:0,dep:''};
var employees=[];
var plan={};
var allWeeks=[];
var weekDays=[];

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('show');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('show');},2500);}
function ini(s){var p=(s||'').trim().split(' ');return((p[0]||'')[0]||'')+((p[1]||'')[0]||'');}
function isoDate(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function fmt(d){return String(d.getDate()).padStart(2,'0')+'.'+String(d.getMonth()+1).padStart(2,'0')+'.'+d.getFullYear();}

function getWeeks(year,month){
  var weeks=[];
  var d=new Date(year,month,1);
  // Ayin tum gunleri uzerinden haftaları bul
  var seen={};
  for(var i=0;i<31;i++){
    if(d.getMonth()!==month)break;
    // Bu gunun haftasinin Pazartesisini bul
    var dow=d.getDay();
    var diff=dow===0?-6:1-dow;
    var mon=new Date(d); mon.setDate(d.getDate()+diff);
    var key=isoDate(mon);
    if(!seen[key]){
      seen[key]=true;
      var sun=new Date(mon); sun.setDate(mon.getDate()+6);
      weeks.push({start:mon,end:sun,key:key});
    }
    d.setDate(d.getDate()+1);
  }
  return weeks;
}

function buildSelects(){
  // Yil
  var ySel=document.getElementById('f-year');
  ySel.innerHTML='';
  for(var y=state.year-2;y<=state.year+2;y++){
    var o=document.createElement('option');o.value=y;o.textContent=y;
    if(y===state.year)o.selected=true;
    ySel.appendChild(o);
  }
  // Ay
  var mSel=document.getElementById('f-month');
  mSel.innerHTML=AYLAR.map(function(a,i){return '<option value="'+i+'"'+(i===state.month?' selected':'')+'>'+a+'</option>';}).join('');
  // Haftalar
  buildWeekSelect();
}

function buildWeekSelect(){
  allWeeks=getWeeks(state.year,state.month);
  var wSel=document.getElementById('f-week');
  wSel.innerHTML=allWeeks.map(function(w,i){return '<option value="'+i+'"'+(i===state.weekIdx?' selected':'')+'>'+fmt(w.start)+' - '+fmt(w.end)+'</option>';}).join('');
}

function buildLegend(){
  document.getElementById('legend').innerHTML=SHIFTS.map(function(s){
    return '<span class="lg"><i style="background:'+s.bg+';border:1px solid '+s.color+'"></i>'+s.label+'</span>';
  }).join('');
}

function getWeekDays(){
  weekDays=[];
  var w=allWeeks[state.weekIdx];
  for(var i=0;i<7;i++){
    var d=new Date(w.start);d.setDate(d.getDate()+i);
    weekDays.push(d);
  }
}

function render(){
  getWeekDays();
  var filtered=state.dep?employees.filter(function(e){return e.dep===state.dep;}):employees;
  
  var thead='<thead><tr><th class="stick" style="min-width:200px">Personel</th>';
  weekDays.forEach(function(d){
    var dow=d.getDay();
    var ht=(dow===0||dow===6);
    thead+='<th'+(ht?' style="color:var(--blue)"':'')+'>'+GUNLER[dow]+'<small>'+fmt(d)+'</small></th>';
  });
  thead+='</tr></thead>';

  var tbody='<tbody>';
  if(!filtered.length){
    tbody+='<tr><td colspan="8" style="text-align:center;padding:30px;color:var(--muted)">Personel bulunamadi</td></tr>';
  }
  filtered.forEach(function(e){
    var empPlan=plan[e.tc]||{};
    tbody+='<tr><td class="stick"><div class="emp"><div class="av" style="background:var(--amber)">'+ini(e.ad)+'</div><div><b>'+e.ad+'</b><small>'+e.dep+'</small></div></div></td>';
    weekDays.forEach(function(d){
      var ds=isoDate(d);
      var code=empPlan[ds];
      // Eger plan yoksa OFF goster
      if(!code)code='OFF';
      var sh=SHIFT_MAP[code]||SHIFT_MAP['OFF'];
      tbody+='<td><div class="cell" style="background:'+sh.bg+';color:'+sh.color+';border-color:'+sh.color+'33" data-tc="'+e.tc+'" data-date="'+ds+'">'+code+'</div></td>';
    });
    tbody+='</tr>';
  });
  tbody+='</tbody>';

  document.getElementById('tbl').innerHTML=thead+tbody;
  var w=allWeeks[state.weekIdx];
  document.getElementById('cnt').textContent=filtered.length+' personel - '+fmt(w.start)+' - '+fmt(w.end);

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
      cell.style.borderColor=sh.color+'33';
    });
  });
}

async function listele(){
  state.dep=document.getElementById('f-dep').value;
  state.year=+document.getElementById('f-year').value;
  state.month=+document.getElementById('f-month').value;
  state.weekIdx=+document.getElementById('f-week').value;
  buildWeekSelect();
  getWeekDays();
  var w=allWeeks[state.weekIdx];
  if(!w)return;
  var weekStart=isoDate(w.start);
  try{
    var data=await apiReq('/shifts/plan?week='+weekStart);
    plan=data||{};
  }catch(e){plan={};}
  render();
}

document.getElementById('b-list').addEventListener('click',listele);

document.getElementById('f-year').addEventListener('change',function(){
  state.year=+this.value; state.weekIdx=0; buildWeekSelect();
});
document.getElementById('f-month').addEventListener('change',function(){
  state.month=+this.value; state.weekIdx=0; buildWeekSelect();
});
document.getElementById('f-week').addEventListener('change',function(){
  state.weekIdx=+this.value;
});

document.getElementById('b-save').addEventListener('click',async function(){
  if(!allWeeks[state.weekIdx])return;
  var weekStart=isoDate(allWeeks[state.weekIdx].start);
  try{
    await apiReq('/shifts/plan',{method:'PUT',body:{week:weekStart,plan:plan}});
    toast('Kaydedildi');
  }catch(e){toast('Hata: '+e.message);}
});

// Transfer modal
function buildTransferSelects(){
  var ty=document.getElementById('tr-year');
  ty.innerHTML='';
  for(var y=state.year-1;y<=state.year+2;y++){
    var o=document.createElement('option');o.value=y;o.textContent=y;
    if(y===state.year)o.selected=true;
    ty.appendChild(o);
  }
  var tm=document.getElementById('tr-month');
  tm.innerHTML=AYLAR.map(function(a,i){return '<option value="'+i+'"'+(i===state.month?' selected':'')+'>'+a+'</option>';}).join('');
  buildTransferWeeks();
}

function buildTransferWeeks(){
  var ty=+document.getElementById('tr-year').value;
  var tm=+document.getElementById('tr-month').value;
  var weeks=getWeeks(ty,tm);
  var tw=document.getElementById('tr-week');
  tw.innerHTML=weeks.map(function(w,i){return '<option value="'+w.key+'">'+fmt(w.start)+' - '+fmt(w.end)+'</option>';}).join('');
}

document.getElementById('b-transfer').addEventListener('click',function(){
  buildTransferSelects();
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
document.getElementById('tr-year').addEventListener('change',buildTransferWeeks);
document.getElementById('tr-month').addEventListener('change',buildTransferWeeks);

document.getElementById('tr-confirm').addEventListener('click',async function(){
  var srcStart=isoDate(allWeeks[state.weekIdx].start);
  var tgtStart=document.getElementById('tr-week').value;
  if(srcStart===tgtStart){toast('Ayni hafta secildi');return;}
  var srcDate=new Date(srcStart);
  var tgtDate=new Date(tgtStart);
  var diffDays=Math.round((tgtDate-srcDate)/86400000);
  var newPlan={};
  Object.keys(plan).forEach(function(tc){
    newPlan[tc]={};
    Object.keys(plan[tc]).forEach(function(date){
      var d=new Date(date);d.setDate(d.getDate()+diffDays);
      newPlan[tc][isoDate(d)]=plan[tc][date];
    });
  });
  try{
    await apiReq('/shifts/plan',{method:'PUT',body:{week:tgtStart,plan:newPlan}});
    toast('Transfer tamamlandi');
  }catch(e){toast('Hata: '+e.message);}
  document.getElementById('tr-ov').style.display='none';
  document.getElementById('tr-modal').classList.remove('open');
});

document.getElementById('b-excel').addEventListener('click',function(){
  if(!weekDays.length)return;
  var filtered=state.dep?employees.filter(function(e){return e.dep===state.dep;}):employees;
  var csv='Sicil,Ad Soyad,Bolum';
  weekDays.forEach(function(d){csv+=','+fmt(d);});csv+='\n';
  filtered.forEach(function(e){
    var line=e.sicil+','+e.ad+','+e.dep;
    weekDays.forEach(function(d){line+=','+(plan[e.tc]&&plan[e.tc][isoDate(d)]||'OFF');});
    csv+=line+'\n';
  });
  var blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download='shift-'+isoDate(allWeeks[state.weekIdx].start)+'.csv';a.click();
});

async function init(){
  buildSelects();
  buildLegend();
  try{
    var emps=await apiReq('/employees');
    employees=(emps||[]).filter(function(e){return e.status==='aktif';});
    var deps=[''];
    employees.forEach(function(e){if(deps.indexOf(e.dep)<0)deps.push(e.dep);});
    var sel=document.getElementById('f-dep');
    sel.innerHTML=deps.map(function(d){return '<option value="'+d+'">'+(d||'Tumu')+'</option>';}).join('');
    await listele();
  }catch(e){console.log('init hata:',e);}
}

init();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-vplan">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_VPLAN + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
