NEW_GECISLER = r'''<template id="tpl-gecisler">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Giris / Cikis</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--text:#EAF2F5;--muted:#8FA6B0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;padding:22px 16px 60px}
.topbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:16px}
.topbar h1{font-family:'Space Grotesk';font-size:18px;font-weight:700;margin:0;flex:1}
.nav{display:flex;align-items:center;gap:6px;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:5px 10px}
.nav button{background:none;border:0;color:var(--muted);cursor:pointer;font-size:18px;padding:0 4px}
.nav button:hover{color:var(--text)}
.nav span{font-family:'Space Grotesk';font-weight:600;font-size:14px;min-width:80px;text-align:center}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px;align-items:center}
.filter-btn{padding:6px 12px;border-radius:7px;border:1px solid var(--line);background:var(--panel);color:var(--muted);font-size:12px;font-weight:600;cursor:pointer}
.filter-btn.active{background:var(--amber);color:#1a1205;border-color:var(--amber)}
.btn{padding:8px 14px;border-radius:8px;border:0;font-weight:600;font-size:12.5px;cursor:pointer;font-family:inherit}
.btn-amber{background:var(--amber);color:#1a1205}
.btn-ghost{background:var(--panel);border:1px solid var(--line);color:var(--text)}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;margin-bottom:14px}
table{width:100%;border-collapse:collapse}
thead th{text-align:left;font-size:11px;color:var(--muted);font-weight:600;padding:10px 14px;border-bottom:1px solid var(--line);white-space:nowrap}
tbody td{padding:10px 14px;border-bottom:1px solid rgba(35,65,79,.4);font-size:13px;vertical-align:middle}
tbody tr:hover td{background:rgba(27,49,62,.4)}
.who{display:flex;align-items:center;gap:10px}
.av{width:30px;height:30px;border-radius:8px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:11px;color:#1a1205;background:var(--amber);flex:0 0 auto}
.who b{font-size:13px;font-weight:600}.who small{color:var(--muted);font-size:11px;display:block}
.mono{font-family:'JetBrains Mono';font-size:12px}
.pill{display:inline-flex;align-items:center;font-size:11px;font-weight:600;padding:3px 8px;border-radius:6px}
.p-ok{background:rgba(52,217,160,.15);color:var(--mint)}
.p-miss{background:rgba(255,107,107,.15);color:var(--danger)}
.p-fm{background:rgba(242,181,59,.15);color:var(--amber)}
.p-ht{background:rgba(111,177,255,.15);color:var(--blue)}
.edit-btn{background:none;border:1px solid var(--line);color:var(--muted);border-radius:6px;padding:4px 8px;cursor:pointer;font-size:11px}
.edit-btn:hover{border-color:var(--amber);color:var(--amber)}
.empty{text-align:center;color:var(--muted);padding:40px;font-size:13px}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:12px 20px;border-radius:11px;font-size:13px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
.ov{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:80;display:none}
.modal{position:fixed;inset:0;z-index:81;display:none;align-items:center;justify-content:center}
.modal.open{display:flex}
.mbox{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:24px;width:380px;max-width:92vw}
.mbox h3{font-family:'Space Grotesk';font-size:16px;margin:0 0 16px}
.field{margin-bottom:12px}
.field label{display:block;font-size:12px;color:var(--muted);margin-bottom:5px}
.field input{width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:9px;padding:9px 12px;color:var(--text);font-family:'JetBrains Mono';font-size:13px;outline:none}
.field input:focus{border-color:var(--amber)}
.mbtns{display:flex;gap:10px;justify-content:flex-end;margin-top:16px}
</style>

<div class="topbar">
  <h1>Giris / Cikis</h1>
  <div class="nav">
    <button id="prev-btn">&#8249;</button>
    <span id="date-label">-</span>
    <button id="next-btn">&#8250;</button>
  </div>
  <button class="btn btn-ghost" id="today-btn">Bugun</button>
  <button class="btn btn-amber" id="export-btn">Excel</button>
</div>

<div class="filters" id="filters">
  <button class="filter-btn active" data-f="all">Tumu (0)</button>
  <button class="filter-btn" data-f="missing">Cikis yok (0)</button>
  <button class="filter-btn" data-f="fm">Fazla mesai (0)</button>
  <button class="filter-btn" data-f="ht">HT calisma (0)</button>
</div>

<div class="card">
  <table>
    <thead>
      <tr>
        <th>PDKS ID</th>
        <th>Departman</th>
        <th>Gorev</th>
        <th>Ad Soyad</th>
        <th>Gun</th>
        <th>Tarih</th>
        <th>Vardiya</th>
        <th>Giris</th>
        <th>Cikis</th>
        <th>Toplam</th>
        <th>Gunluk</th>
        <th>FM Sure</th>
        <th>Durum</th>
        <th></th>
      </tr>
    </thead>
    <tbody id="att-body">
      <tr><td colspan="14" class="empty">Yukleniyor...</td></tr>
    </tbody>
  </table>
</div>

<div class="ov" id="edit-ov"></div>
<div class="modal" id="edit-modal">
  <div class="mbox">
    <h3>Kayit Duzenle</h3>
    <input type="hidden" id="edit-id">
    <div class="field"><label>Giris saati</label><input id="edit-giris" type="time"></div>
    <div class="field"><label>Cikis saati</label><input id="edit-cikis" type="time"></div>
    <div class="mbtns">
      <button class="btn btn-ghost" id="edit-cancel">Iptal</button>
      <button class="btn btn-amber" id="edit-save">Kaydet</button>
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

var GUNLER=['Pazar','Pazartesi','Sali','Carsamba','Persembe','Cuma','Cumartesi'];
var now=new Date();
var curDate=new Date(now.getFullYear(),now.getMonth(),now.getDate());
var curFilter='all';
var attData=[];
var shiftData={};

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('on');},2500);}
function isoDate(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function ini(s){var p=(s||'').trim().split(' ');return((p[0]||'')[0]||'')+((p[1]||'')[0]||'');}
function timeDiff(g,c){
  if(!g||!c)return null;
  var gp=g.split(':').map(Number); var cp=c.split(':').map(Number);
  var mins=(cp[0]*60+cp[1])-(gp[0]*60+gp[1]);
  if(mins<0)mins+=1440;
  return mins;
}
function fmtMins(m){if(m==null)return '-';var h=Math.floor(m/60); var mn=m%60; return String(h).padStart(2,'0')+':'+String(mn).padStart(2,'0');}

function updateLabel(){
  var d=curDate;
  document.getElementById('date-label').textContent=String(d.getDate()).padStart(2,'0')+'.'+String(d.getMonth()+1).padStart(2,'0')+'.'+d.getFullYear();
}

async function loadShiftForDate(){
  // O haftanin Pazartesisini bul
  var d=new Date(curDate);
  var dow=d.getDay(); var diff=dow===0?-6:1-dow;
  d.setDate(d.getDate()+diff);
  var weekStart=isoDate(d);
  try{
    shiftData=await req('/shifts/plan?week='+weekStart);
  }catch(e){shiftData={};}
}

async function load(){
  var ds=isoDate(curDate);
  try{
    var all=await req('/attendance');
    attData=all.filter(function(r){return r.day===ds;});
    await loadShiftForDate();
    render();
  }catch(e){
    document.getElementById('att-body').innerHTML='<tr><td colspan="14" class="empty">Hata: '+e.message+'</td></tr>';
  }
}

function getShiftCode(tc){
  var ds=isoDate(curDate);
  if(shiftData[tc]&&shiftData[tc][ds])return shiftData[tc][ds];
  return null;
}

function getStatus(r){
  var shCode=getShiftCode(r.tc);
  var mins=timeDiff(r.giris,r.cikis);
  var isHT=(shCode==='HT'||shCode==='OFF');
  if(r.giris&&isHT)return 'ht'; // HT gununde calisma
  if(r.giris&&!r.cikis)return 'missing'; // Cikis yok
  if(mins!=null&&mins>540)return 'fm'; // 9 saat ustunde FM
  if(r.giris&&r.cikis)return 'ok';
  return 'ok';
}

function render(){
  var ds=isoDate(curDate);
  var dow=curDate.getDay();
  
  var filtered=attData;
  if(curFilter==='missing')filtered=attData.filter(function(r){return r.giris&&!r.cikis;});
  else if(curFilter==='fm')filtered=attData.filter(function(r){var m=timeDiff(r.giris,r.cikis);return m!=null&&m>540;});
  else if(curFilter==='ht')filtered=attData.filter(function(r){var sc=getShiftCode(r.tc);return r.giris&&(sc==='HT'||sc==='OFF');});

  // Filter badge sayilari
  var missing=attData.filter(function(r){return r.giris&&!r.cikis;}).length;
  var fm=attData.filter(function(r){var m=timeDiff(r.giris,r.cikis);return m!=null&&m>540;}).length;
  var ht=attData.filter(function(r){var sc=getShiftCode(r.tc);return r.giris&&(sc==='HT'||sc==='OFF');}).length;
  document.querySelectorAll('.filter-btn').forEach(function(b){
    if(b.dataset.f==='all')b.textContent='Tumu ('+attData.length+')';
    else if(b.dataset.f==='missing')b.textContent='Cikis yok ('+missing+')';
    else if(b.dataset.f==='fm')b.textContent='Fazla mesai ('+fm+')';
    else if(b.dataset.f==='ht')b.textContent='HT calisma ('+ht+')';
    b.classList.toggle('active',b.dataset.f===curFilter);
  });

  if(!filtered.length){
    document.getElementById('att-body').innerHTML='<tr><td colspan="14" class="empty">Bu tarihte kayit yok</td></tr>';
    return;
  }

  var html='';
  filtered.forEach(function(r){
    var mins=timeDiff(r.giris,r.cikis);
    var fmMins=mins!=null&&mins>540?mins-540:0;
    var status=getStatus(r);
    var gunluk=mins!=null?fmtMins(Math.min(mins,540)):'-';
    var statusHtml='';
    if(status==='missing')statusHtml='<span class="pill p-miss">Cikis yok</span>';
    else if(status==='fm')statusHtml='<span class="pill p-fm">FM: '+fmtMins(fmMins)+'</span>';
    else if(status==='ht')statusHtml='<span class="pill p-ht">HT calisma</span>';
    else statusHtml='<span class="pill p-ok">Tamamlandi</span>';

    html+='<tr>'
      +'<td class="mono">#'+r.sicil+'</td>'
      +'<td style="color:var(--muted);font-size:12px">'+r.dep+'</td>'
      +'<td style="color:var(--muted);font-size:12px">'+r.gorev+'</td>'
      +'<td><div class="who"><div class="av">'+ini(r.ad)+'</div><div><b>'+r.ad+'</b></div></div></td>'
      +'<td style="color:var(--muted);font-size:12px">'+GUNLER[dow]+'</td>'
      +'<td class="mono">'+ds+'</td>'
      +'<td style="font-size:12px">'+r.vardiya+'</td>'
      +'<td class="mono">'+(r.giris||'-')+'</td>'
      +'<td class="mono">'+(r.cikis||'-')+'</td>'
      +'<td class="mono">'+fmtMins(mins)+'</td>'
      +'<td class="mono">'+gunluk+'</td>'
      +'<td class="mono">'+(fmMins>0?('<span style="color:var(--amber)">'+fmtMins(fmMins)+'</span>'):'-')+'</td>'
      +'<td>'+statusHtml+'</td>'
      +'<td><button class="edit-btn" data-id="'+r.id+'" data-giris="'+(r.giris||'')+'" data-cikis="'+(r.cikis||'')+'">Duzenle</button></td>'
      +'</tr>';
  });
  document.getElementById('att-body').innerHTML=html;

  document.querySelectorAll('.edit-btn').forEach(function(b){
    b.addEventListener('click',function(){
      document.getElementById('edit-id').value=b.dataset.id;
      document.getElementById('edit-giris').value=b.dataset.giris||'';
      document.getElementById('edit-cikis').value=b.dataset.cikis||'';
      document.getElementById('edit-ov').style.display='block';
      document.getElementById('edit-modal').classList.add('open');
    });
  });
}

// Navigasyon
document.getElementById('prev-btn').addEventListener('click',function(){
  curDate.setDate(curDate.getDate()-1);updateLabel();load();
});
document.getElementById('next-btn').addEventListener('click',function(){
  curDate.setDate(curDate.getDate()+1);updateLabel();load();
});
document.getElementById('today-btn').addEventListener('click',function(){
  curDate=new Date();curDate.setHours(0,0,0,0);updateLabel();load();
});

// Filtreler
document.getElementById('filters').addEventListener('click',function(e){
  var b=e.target.closest('.filter-btn');
  if(!b)return;
  curFilter=b.dataset.f;
  render();
});

// Duzenle modal
document.getElementById('edit-cancel').addEventListener('click',function(){
  document.getElementById('edit-ov').style.display='none';
  document.getElementById('edit-modal').classList.remove('open');
});
document.getElementById('edit-ov').addEventListener('click',function(){
  document.getElementById('edit-ov').style.display='none';
  document.getElementById('edit-modal').classList.remove('open');
});
document.getElementById('edit-save').addEventListener('click',async function(){
  var id=document.getElementById('edit-id').value;
  var giris=document.getElementById('edit-giris').value;
  var cikis=document.getElementById('edit-cikis').value;
  try{
    await req('/attendance/'+id,{method:'PUT',body:{giris:giris,cikis:cikis}});
    toast('Kaydedildi');
    document.getElementById('edit-ov').style.display='none';
    document.getElementById('edit-modal').classList.remove('open');
    load();
  }catch(e){toast('Hata: '+e.message);}
});

// Excel
document.getElementById('export-btn').addEventListener('click',function(){
  var ds=isoDate(curDate);
  var csv='Sicil,Departman,Gorev,Ad Soyad,Tarih,Vardiya,Giris,Cikis,Toplam,FM Sure,Durum\n';
  attData.forEach(function(r){
    var mins=timeDiff(r.giris,r.cikis);
    var fm=mins!=null&&mins>540?fmtMins(mins-540):'-';
    var status=getStatus(r);
    csv+=r.sicil+','+r.dep+','+r.gorev+','+r.ad+','+ds+','+r.vardiya+','+(r.giris||'-')+','+(r.cikis||'-')+','+fmtMins(mins)+','+fm+','+status+'\n';
  });
  var blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download='gecis-'+ds+'.csv';a.click();
});

updateLabel();
load();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-gecisler">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_GECISLER + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
