NEW_GECISLER = r'''<template id="tpl-gecisler">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Giris / Cikis</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--text:#EAF2F5;--muted:#8FA6B0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;padding:18px 16px 60px}
.topbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:14px}
.topbar h1{font-family:'Space Grotesk';font-size:18px;font-weight:700;margin:0}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;margin-bottom:14px}
.filter-bar{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end;padding:14px 16px;border-bottom:1px solid var(--line)}
.f{display:flex;flex-direction:column;gap:4px}
.f label{font-size:11px;color:var(--muted);font-weight:600}
.f input,.f select{background:var(--panel-2);border:1px solid var(--line);color:var(--text);border-radius:8px;padding:7px 10px;font-size:13px;font-family:inherit;outline:none}
.f input:focus,.f select:focus{border-color:var(--amber)}
.radio-group{display:flex;flex-direction:column;gap:5px}
.radio-group label{display:flex;align-items:center;gap:6px;font-size:12.5px;cursor:pointer;color:var(--muted)}
.radio-group input[type=radio]{accent-color:var(--amber);width:14px;height:14px}
.radio-group label:hover{color:var(--text)}
.btn{padding:8px 14px;border-radius:8px;border:0;font-weight:600;font-size:12.5px;cursor:pointer;font-family:inherit}
.btn-amber{background:var(--amber);color:#1a1205}
.btn-ghost{background:var(--panel-2);border:1px solid var(--line);color:var(--text)}
.btn-ghost:hover{border-color:var(--amber);color:var(--amber)}
table{width:100%;border-collapse:collapse}
thead th{text-align:left;font-size:11px;color:var(--muted);font-weight:600;padding:10px 12px;border-bottom:1px solid var(--line);white-space:nowrap;cursor:pointer;user-select:none}
thead th:hover{color:var(--text)}
tbody td{padding:9px 12px;border-bottom:1px solid rgba(35,65,79,.4);font-size:12.5px;vertical-align:middle}
tbody tr:hover td{background:rgba(27,49,62,.5)}
.who{display:flex;align-items:center;gap:9px}
.av{width:28px;height:28px;border-radius:7px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:10px;color:#1a1205;background:var(--amber);flex:0 0 auto}
.who b{font-size:12.5px;font-weight:600}.who small{color:var(--muted);font-size:10.5px;display:block}
.mono{font-family:'JetBrains Mono';font-size:12px}
.pill{display:inline-flex;align-items:center;font-size:11px;font-weight:600;padding:3px 8px;border-radius:6px}
.p-ok{background:rgba(52,217,160,.15);color:var(--mint)}
.p-miss{background:rgba(255,107,107,.15);color:var(--danger)}
.p-fm{background:rgba(242,181,59,.15);color:var(--amber)}
.p-ht{background:rgba(111,177,255,.15);color:var(--blue)}
.p-off{background:rgba(199,146,234,.15);color:#C792EA}
.empty{text-align:center;color:var(--muted);padding:40px;font-size:13px}
.footer-bar{display:flex;align-items:center;justify-content:space-between;padding:10px 16px;border-top:1px solid var(--line)}
.footer-bar span{color:var(--muted);font-size:12px}
/* Sag tik menu */
.ctx-menu{position:fixed;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:5px;z-index:99;box-shadow:0 16px 40px rgba(0,0,0,.6);min-width:180px}
.ctx-item{padding:8px 14px;border-radius:7px;cursor:pointer;font-size:13px;display:flex;align-items:center;gap:8px}
.ctx-item:hover{background:var(--panel-2)}
.ctx-item.danger{color:var(--danger)}
.ctx-sep{border-top:1px solid var(--line);margin:4px 0}
/* Modal */
.ov{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:80;display:none}
.modal{position:fixed;inset:0;z-index:81;display:none;align-items:center;justify-content:center}
.modal.open{display:flex}
.mbox{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:24px;width:420px;max-width:92vw}
.mbox h3{font-family:'Space Grotesk';font-size:16px;margin:0 0 16px}
.field{margin-bottom:12px}
.field label{display:block;font-size:12px;color:var(--muted);margin-bottom:5px;font-weight:500}
.field input,.field select{width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:9px;padding:9px 12px;color:var(--text);font-family:inherit;font-size:13px;outline:none}
.field input:focus,.field select:focus{border-color:var(--amber)}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.mbtns{display:flex;gap:10px;justify-content:flex-end;margin-top:16px}
/* Hareket modal */
.hlist{max-height:280px;overflow-y:auto;margin-bottom:12px}
.hitem{display:flex;align-items:center;justify-content:space-between;padding:8px 12px;background:var(--panel-2);border-radius:8px;margin-bottom:6px;font-size:12.5px}
.hitem .mono{font-size:11.5px}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:12px 20px;border-radius:11px;font-size:13px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
</style>

<div class="topbar">
  <h1>Giris / Cikis Islemleri</h1>
  <div style="margin-left:auto;display:flex;gap:8px">
    <button class="btn btn-ghost" id="add-btn">+ Manuel Ekle</button>
    <button class="btn btn-ghost" id="export-btn">&#8595; Excel</button>
    <button class="btn btn-amber" id="list-btn">Listele</button>
  </div>
</div>

<div class="card">
  <div class="filter-bar">
    <div class="f">
      <label>Baslangic Tarihi</label>
      <input type="date" id="f-start">
    </div>
    <div class="f">
      <label>Bitis Tarihi</label>
      <input type="date" id="f-end">
    </div>
    <div class="f">
      <label>Departman</label>
      <select id="f-dep"><option value="">Tumu</option></select>
    </div>
    <div class="f">
      <label>Filtre</label>
      <div class="radio-group">
        <label><input type="radio" name="filt" value="all" checked> Tumu</label>
        <label><input type="radio" name="filt" value="miss_cikis"> Giris Var - Cikis Yok</label>
        <label><input type="radio" name="filt" value="miss_giris"> Giris Yok - Cikis Var</label>
        <label><input type="radio" name="filt" value="off_mesai"> Off da Mesai</label>
        <label><input type="radio" name="filt" value="fm"> Fazla Mesai</label>
      </div>
    </div>
  </div>

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
        <th>Giris Saati</th>
        <th>Cikis Saati</th>
        <th>Toplam Cal.</th>
        <th>Gunluk Cal.</th>
        <th>FM Sure</th>
        <th>Durum</th>
      </tr>
    </thead>
    <tbody id="att-body">
      <tr><td colspan="13" class="empty">Listele butonuna basin...</td></tr>
    </tbody>
  </table>
  <div class="footer-bar">
    <span id="footer-cnt">-</span>
    <span id="footer-sum"></span>
  </div>
</div>

<!-- Context Menu -->
<div class="ctx-menu" id="ctx-menu" style="display:none"></div>
<div class="ov" id="edit-ov"></div>

<!-- Duzenle Modal -->
<div class="modal" id="edit-modal">
  <div class="mbox">
    <h3>Satir Duzenle</h3>
    <input type="hidden" id="edit-id">
    <div style="background:var(--panel-2);border-radius:8px;padding:10px 12px;margin-bottom:14px;font-size:12.5px" id="edit-info"></div>
    <div class="field-row">
      <div class="field"><label>Giris Tarihi</label><input id="edit-gdate" type="date"></div>
      <div class="field"><label>Giris Saati</label><input id="edit-giris" type="time"></div>
    </div>
    <div class="field-row">
      <div class="field"><label>Cikis Tarihi</label><input id="edit-cdate" type="date"></div>
      <div class="field"><label>Cikis Saati</label><input id="edit-cikis" type="time"></div>
    </div>
    <div class="mbtns">
      <button class="btn btn-ghost" id="edit-cancel">Iptal</button>
      <button class="btn btn-amber" id="edit-save">Guncelle</button>
    </div>
  </div>
</div>

<!-- Hareket Modal -->
<div class="modal" id="har-modal">
  <div class="mbox">
    <h3 id="har-title">G/C Hareketler</h3>
    <div class="hlist" id="har-list"></div>
    <div class="mbtns">
      <button class="btn btn-ghost" id="har-close">Kapat</button>
    </div>
  </div>
</div>

<!-- Manuel Ekle Modal -->
<div class="modal" id="add-modal">
  <div class="mbox">
    <h3>Manuel Kayit Ekle</h3>
    <div class="field"><label>Personel</label><select id="add-emp"></select></div>
    <div class="field-row">
      <div class="field"><label>Giris Tarihi</label><input id="add-gdate" type="date"></div>
      <div class="field"><label>Giris Saati</label><input id="add-giris" type="time"></div>
    </div>
    <div class="field-row">
      <div class="field"><label>Cikis Tarihi</label><input id="add-cdate" type="date"></div>
      <div class="field"><label>Cikis Saati</label><input id="add-cikis" type="time"></div>
    </div>
    <div class="mbtns">
      <button class="btn btn-ghost" id="add-cancel">Iptal</button>
      <button class="btn btn-amber" id="add-save">Kaydet</button>
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
var attData=[]; var shiftMap={}; var employees=[];

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('on');},2500);}
function isoDate(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function ini(s){var p=(s||'').trim().split(' ');return((p[0]||'')[0]||'')+((p[1]||'')[0]||'');}
function timeDiffMins(g,c){
  if(!g||!c)return null;
  var gp=g.split(':').map(Number); var cp=c.split(':').map(Number);
  var m=(cp[0]*60+cp[1])-(gp[0]*60+gp[1]);
  if(m<0)m+=1440; return m;
}
function fmtMins(m){if(m==null||m<0)return '-';return String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0');}

// Init tarihleri
var now=new Date();
document.getElementById('f-start').value=isoDate(new Date(now.getFullYear(),now.getMonth(),now.getDate()));
document.getElementById('f-end').value=isoDate(new Date(now.getFullYear(),now.getMonth(),now.getDate()));

function getFilter(){return document.querySelector('input[name=filt]:checked').value;}
function getDep(){return document.getElementById('f-dep').value;}

function getShiftCode(tc,day){return shiftMap[tc]&&shiftMap[tc][day]?shiftMap[tc][day]:null;}

function getStatus(r){
  var sc=getShiftCode(r.tc,r.day);
  var isOff=(sc==='HT'||sc==='OFF');
  if(r.giris&&isOff)return 'off_mesai';
  if(r.giris&&!r.cikis)return 'miss_cikis';
  var m=timeDiffMins(r.giris,r.cikis);
  if(m!=null&&m>540)return 'fm';
  return 'ok';
}

function applyFilter(data){
  var f=getFilter(); var dep=getDep();
  var d=dep?data.filter(function(r){return r.dep===dep;}):data;
  if(f==='all')return d;
  if(f==='miss_cikis')return d.filter(function(r){return r.giris&&!r.cikis;});
  if(f==='miss_giris')return d.filter(function(r){return !r.giris&&r.cikis;});
  if(f==='off_mesai')return d.filter(function(r){return getStatus(r)==='off_mesai';});
  if(f==='fm')return d.filter(function(r){var m=timeDiffMins(r.giris,r.cikis);return m!=null&&m>540;});
  return d;
}

function render(){
  var filtered=applyFilter(attData);
  if(!filtered.length){
    document.getElementById('att-body').innerHTML='<tr><td colspan="13" class="empty">Kayit bulunamadi</td></tr>';
    document.getElementById('footer-cnt').textContent='0 kayit';
    document.getElementById('footer-sum').textContent='';
    return;
  }
  var totalWork=0, totalFm=0;
  var html=filtered.map(function(r){
    var dow=new Date(r.day).getDay();
    var mins=timeDiffMins(r.giris,r.cikis);
    var fmMins=(mins!=null&&mins>540)?mins-540:0;
    var gunluk=mins!=null?Math.min(mins,540):null;
    var status=getStatus(r);
    if(mins!=null)totalWork+=gunluk;
    totalFm+=fmMins;
    var statusHtml='';
    if(status==='miss_cikis')statusHtml='<span class="pill p-miss">Cikis yok</span>';
    else if(status==='off_mesai')statusHtml='<span class="pill p-off">Off da Mesai</span>';
    else if(status==='fm')statusHtml='<span class="pill p-fm">FM: '+fmtMins(fmMins)+'</span>';
    else statusHtml='<span class="pill p-ok">Tamamlandi</span>';
    return '<tr data-id="'+r.id+'" data-r="'+encodeURIComponent(JSON.stringify(r))+'">'
      +'<td class="mono">#'+r.sicil+'</td>'
      +'<td style="color:var(--muted);font-size:11.5px">'+r.dep+'</td>'
      +'<td style="color:var(--muted);font-size:11.5px">'+r.gorev+'</td>'
      +'<td><div class="who"><div class="av">'+ini(r.ad)+'</div><div><b>'+r.ad+'</b></div></div></td>'
      +'<td style="font-size:11.5px">'+GUNLER[dow]+'</td>'
      +'<td class="mono">'+r.day+'</td>'
      +'<td style="font-size:11.5px">'+r.vardiya+'</td>'
      +'<td class="mono">'+(r.giris||'-')+'</td>'
      +'<td class="mono">'+(r.cikis||'-')+'</td>'
      +'<td class="mono">'+fmtMins(mins)+'</td>'
      +'<td class="mono">'+fmtMins(gunluk)+'</td>'
      +'<td class="mono">'+(fmMins>0?('<span style="color:var(--amber)">'+fmtMins(fmMins)+'</span>'):'-')+'</td>'
      +'<td>'+statusHtml+'</td>'
      +'</tr>';
  }).join('');
  document.getElementById('att-body').innerHTML=html;
  document.getElementById('footer-cnt').textContent=filtered.length+' kayit';
  document.getElementById('footer-sum').textContent='Toplam: '+fmtMins(totalWork)+' | FM: '+fmtMins(totalFm);

  // Sag tik
  document.querySelectorAll('#att-body tr').forEach(function(tr){
    tr.addEventListener('contextmenu',function(e){
      e.preventDefault();
      var r=JSON.parse(decodeURIComponent(tr.dataset.r));
      showCtxMenu(e.clientX,e.clientY,r);
    });
  });
}

function showCtxMenu(x,y,r){
  closeCtx();
  var menu=document.getElementById('ctx-menu');
  menu.innerHTML='<div class="ctx-item" id="ctx-edit">&#9998; Satir Duzenle</div>'
    +'<div class="ctx-item" id="ctx-har">&#8646; G/C Hareketler</div>'
    +'<div class="ctx-sep"></div>'
    +'<div class="ctx-item danger" id="ctx-del">&#10005; Satir Sil</div>';
  menu.style.display='block';
  menu.style.left=Math.min(x,window.innerWidth-200)+'px';
  menu.style.top=Math.min(y,window.innerHeight-160)+'px';

  document.getElementById('ctx-edit').addEventListener('click',function(){openEdit(r);closeCtx();});
  document.getElementById('ctx-har').addEventListener('click',function(){openHar(r);closeCtx();});
  document.getElementById('ctx-del').addEventListener('click',async function(){
    closeCtx();
    if(!confirm(r.ad+' kaydini silmek istediginizden emin misiniz?'))return;
    try{await req('/attendance/'+r.id,{method:'DELETE'});toast('Silindi');load();}
    catch(e){toast('Hata: '+e.message);}
  });
}

function closeCtx(){document.getElementById('ctx-menu').style.display='none';}
document.addEventListener('click',closeCtx);

function openEdit(r){
  document.getElementById('edit-id').value=r.id;
  document.getElementById('edit-info').textContent=r.ad+' - '+r.day+' - '+r.vardiya;
  document.getElementById('edit-gdate').value=r.day;
  document.getElementById('edit-giris').value=r.giris||'';
  document.getElementById('edit-cdate').value=r.day;
  document.getElementById('edit-cikis').value=r.cikis||'';
  document.getElementById('edit-ov').style.display='block';
  document.getElementById('edit-modal').classList.add('open');
}

function openHar(r){
  document.getElementById('har-title').textContent='G/C Hareketler - '+r.ad;
  document.getElementById('har-list').innerHTML='<div style="color:var(--muted);font-size:12px;padding:20px;text-align:center">Yukleniyor...</div>';
  document.getElementById('edit-ov').style.display='block';
  document.getElementById('har-modal').classList.add('open');
  // Ayni personelin kayitlarini goster
  var same=attData.filter(function(x){return x.tc===r.tc;}).sort(function(a,b){return b.day.localeCompare(a.day);});
  document.getElementById('har-list').innerHTML=same.map(function(x){
    var m=timeDiffMins(x.giris,x.cikis);
    return '<div class="hitem"><div><b>'+x.day+'</b><div class="mono">'+x.vardiya+'</div></div>'
      +'<div style="text-align:right"><div class="mono">'+(x.giris||'-')+' - '+(x.cikis||'-')+'</div>'
      +'<div style="font-size:11px;color:var(--muted)">'+fmtMins(m)+'</div></div></div>';
  }).join('')||'<div style="color:var(--muted);font-size:12px;text-align:center;padding:16px">Kayit yok</div>';
}

function closeModals(){
  document.getElementById('edit-ov').style.display='none';
  document.getElementById('edit-modal').classList.remove('open');
  document.getElementById('har-modal').classList.remove('open');
  document.getElementById('add-modal').classList.remove('open');
}

document.getElementById('edit-ov').addEventListener('click',closeModals);
document.getElementById('edit-cancel').addEventListener('click',closeModals);
document.getElementById('har-close').addEventListener('click',closeModals);
document.getElementById('add-cancel').addEventListener('click',closeModals);

document.getElementById('edit-save').addEventListener('click',async function(){
  var id=document.getElementById('edit-id').value;
  var giris=document.getElementById('edit-giris').value;
  var cikis=document.getElementById('edit-cikis').value;
  try{
    await req('/attendance/'+id,{method:'PUT',body:{giris:giris,cikis:cikis}});
    toast('Guncellendi');closeModals();load();
  }catch(e){toast('Hata: '+e.message);}
});

// Manuel ekle
document.getElementById('add-btn').addEventListener('click',function(){
  var sel=document.getElementById('add-emp');
  sel.innerHTML=employees.map(function(e){return '<option value="'+e.tc+'">'+e.ad+' (#'+e.sicil+')</option>';}).join('');
  document.getElementById('add-gdate').value=document.getElementById('f-start').value;
  document.getElementById('add-cdate').value=document.getElementById('f-start').value;
  document.getElementById('edit-ov').style.display='block';
  document.getElementById('add-modal').classList.add('open');
});

document.getElementById('add-save').addEventListener('click',async function(){
  var tc=document.getElementById('add-emp').value;
  var gdate=document.getElementById('add-gdate').value;
  var giris=document.getElementById('add-giris').value;
  var cdate=document.getElementById('add-cdate').value;
  var cikis=document.getElementById('add-cikis').value;
  if(!tc||!gdate||!giris){toast('Personel ve giris saati gerekli');return;}
  try{
    await req('/attendance',{method:'POST',body:{tc:tc,day:gdate,giris:giris,cikis:cikis||null}});
    toast('Kayit eklendi');closeModals();load();
  }catch(e){toast('Hata: '+e.message);}
});

async function loadShifts(start,end){
  // Tarih araligindaki haftaları bul
  shiftMap={};
  var d=new Date(start);
  var endD=new Date(end);
  var seen={};
  while(d<=endD){
    var dow=d.getDay(); var diff=dow===0?-6:1-dow;
    var mon=new Date(d); mon.setDate(d.getDate()+diff);
    var key=isoDate(mon);
    if(!seen[key]){
      seen[key]=true;
      try{
        var data=await req('/shifts/plan?week='+key);
        Object.keys(data).forEach(function(tc){
          if(!shiftMap[tc])shiftMap[tc]={};
          Object.assign(shiftMap[tc],data[tc]);
        });
      }catch(e){}
    }
    d.setDate(d.getDate()+1);
  }
}

async function load(){
  var start=document.getElementById('f-start').value;
  var end=document.getElementById('f-end').value;
  if(!start||!end)return;
  document.getElementById('att-body').innerHTML='<tr><td colspan="13" class="empty">Yukleniyor...</td></tr>';
  try{
    var all=await req('/attendance');
    attData=all.filter(function(r){return r.day>=start&&r.day<=end;});
    // Departman filtresi doldur
    var deps=[''];
    attData.forEach(function(r){if(deps.indexOf(r.dep)<0)deps.push(r.dep);});
    var dsel=document.getElementById('f-dep');
    var curDep=dsel.value;
    dsel.innerHTML=deps.map(function(d){return '<option value="'+d+'"'+(d===curDep?' selected':'')+' >'+(d||'Tumu')+'</option>';}).join('');
    await loadShifts(start,end);
    render();
  }catch(e){
    document.getElementById('att-body').innerHTML='<tr><td colspan="13" class="empty">Hata: '+e.message+'</td></tr>';
  }
}

document.getElementById('list-btn').addEventListener('click',load);
document.querySelectorAll('input[name=filt]').forEach(function(r){r.addEventListener('change',render);});
document.getElementById('f-dep').addEventListener('change',render);

document.getElementById('export-btn').addEventListener('click',function(){
  var filtered=applyFilter(attData);
  var csv='PDKS ID,Departman,Gorev,Ad Soyad,Gun,Tarih,Vardiya,Giris,Cikis,Toplam,Gunluk,FM,Durum\n';
  filtered.forEach(function(r){
    var dow=new Date(r.day).getDay();
    var m=timeDiffMins(r.giris,r.cikis);
    var fm=(m!=null&&m>540)?m-540:0;
    csv+=r.sicil+','+r.dep+','+r.gorev+','+r.ad+','+GUNLER[dow]+','+r.day+','+r.vardiya+','+(r.giris||'')+','+(r.cikis||'')+','+fmtMins(m)+','+fmtMins(m?Math.min(m,540):null)+','+fmtMins(fm)+','+getStatus(r)+'\n';
  });
  var blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download='gecis-'+document.getElementById('f-start').value+'_'+document.getElementById('f-end').value+'.csv';a.click();
});

// Personel listesini yukle
(async function(){
  try{
    employees=(await req('/employees')||[]).filter(function(e){return e.status==='aktif';});
  }catch(e){}
  // Backend'de POST /attendance endpoint yoksa sessiz fail
})();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-gecisler">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_GECISLER + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
