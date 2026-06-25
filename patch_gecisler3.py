NEW_GECISLER = r'''<template id="tpl-gecisler">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Giris / Cikis Islemleri</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--purple:#C792EA;--text:#EAF2F5;--muted:#8FA6B0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;padding:16px 14px 60px}
.topbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:12px}
.topbar h1{font-family:'Space Grotesk';font-size:17px;font-weight:700;margin:0;flex:1}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;margin-bottom:12px}
.filter-bar{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end;padding:12px 14px;border-bottom:1px solid var(--line)}
.f{display:flex;flex-direction:column;gap:4px}
.f label{font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.3px}
.f input,.f select{background:var(--panel-2);border:1px solid var(--line);color:var(--text);border-radius:8px;padding:7px 10px;font-size:12.5px;font-family:inherit;outline:none}
.f input:focus,.f select:focus{border-color:var(--amber)}
.radio-grp{display:flex;flex-direction:column;gap:4px;min-width:160px}
.radio-grp label{display:flex;align-items:center;gap:6px;font-size:12px;cursor:pointer;color:var(--muted);padding:2px 0}
.radio-grp input[type=radio]{accent-color:var(--amber)}
.radio-grp label:has(input:checked){color:var(--text);font-weight:600}
.btn{padding:7px 13px;border-radius:8px;border:0;font-weight:600;font-size:12px;cursor:pointer;font-family:inherit}
.btn-amber{background:var(--amber);color:#1a1205}
.btn-ghost{background:var(--panel-2);border:1px solid var(--line);color:var(--text)}
.btn-ghost:hover{border-color:var(--amber);color:var(--amber)}
table{width:100%;border-collapse:collapse;font-size:12px}
thead th{text-align:left;font-size:10.5px;color:var(--muted);font-weight:600;padding:9px 10px;border-bottom:1px solid var(--line);white-space:nowrap;text-transform:uppercase;letter-spacing:.3px}
tbody td{padding:8px 10px;border-bottom:1px solid rgba(35,65,79,.35);vertical-align:middle}
tbody tr:hover td{background:rgba(27,49,62,.5);cursor:pointer}
tbody tr.selected td{background:rgba(242,181,59,.08)}
.who{display:flex;align-items:center;gap:8px}
.av{width:26px;height:26px;border-radius:7px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:10px;color:#1a1205;background:var(--amber);flex:0 0 auto}
.mono{font-family:'JetBrains Mono';font-size:11.5px}
.pill{display:inline-flex;align-items:center;font-size:10.5px;font-weight:600;padding:2px 7px;border-radius:5px}
.p-ok{background:rgba(52,217,160,.15);color:var(--mint)}
.p-miss{background:rgba(255,107,107,.15);color:var(--danger)}
.p-off{background:rgba(199,146,234,.15);color:var(--purple)}
.p-fm{background:rgba(242,181,59,.15);color:var(--amber)}
.p-ht{background:rgba(111,177,255,.15);color:var(--blue)}
.p-warn{background:rgba(255,158,107,.15);color:#FF9E6B}
.p-gelmedi{background:rgba(143,166,176,.1);color:var(--muted)}
.mismatch{color:#FF9E6B;font-size:10px;display:block}
.footer-bar{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:8px 14px;border-top:1px solid var(--line);flex-wrap:wrap}
.footer-bar span{color:var(--muted);font-size:11.5px}
/* Context menu */
.ctx{position:fixed;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:4px;z-index:99;box-shadow:0 12px 36px rgba(0,0,0,.55);min-width:170px;display:none}
.ctx-item{padding:7px 12px;border-radius:7px;cursor:pointer;font-size:12.5px;display:flex;align-items:center;gap:8px}
.ctx-item:hover{background:var(--panel-2)}
.ctx-item.danger{color:var(--danger)}
.ctx-sep{border-top:1px solid var(--line);margin:3px 0}
/* Modal */
.ov{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:80;display:none}
.modal{position:fixed;inset:0;z-index:81;display:none;align-items:center;justify-content:center}
.modal.open{display:flex}
.mbox{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;width:420px;max-width:92vw;box-shadow:0 20px 60px rgba(0,0,0,.5)}
.mbox h3{font-family:'Space Grotesk';font-size:15px;margin:0 0 14px}
.minfo{background:var(--panel-2);border-radius:8px;padding:9px 12px;margin-bottom:12px;font-size:12px;color:var(--muted);line-height:1.6}
.field{margin-bottom:11px}
.field label{display:block;font-size:11px;color:var(--muted);margin-bottom:4px;font-weight:600;text-transform:uppercase}
.field input,.field select{width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;padding:8px 11px;color:var(--text);font-family:inherit;font-size:12.5px;outline:none}
.field input:focus,.field select:focus{border-color:var(--amber)}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.mbtns{display:flex;gap:8px;justify-content:flex-end;margin-top:14px}
.hlist{max-height:260px;overflow-y:auto;margin-bottom:12px}
.hitem{display:flex;align-items:center;justify-content:space-between;padding:7px 11px;background:var(--panel-2);border-radius:7px;margin-bottom:5px;font-size:12px}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:11px 18px;border-radius:10px;font-size:12.5px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
</style>

<div class="topbar">
  <h1>Giris / Cikis Islemleri</h1>
  <div style="display:flex;gap:6px;margin-left:auto;flex-wrap:wrap">
    <button class="btn btn-ghost" id="add-btn">+ Manuel Ekle</button>
    <button class="btn btn-ghost" id="print-btn">&#9113; Yazdir</button>
    <button class="btn btn-ghost" id="excel-btn">&#8595; Excel</button>
    <button class="btn btn-amber" id="list-btn">Listele</button>
  </div>
</div>

<div class="card">
  <div class="filter-bar">
    <div class="f">
      <label>Baslangic</label>
      <input type="date" id="f-start">
    </div>
    <div class="f">
      <label>Bitis</label>
      <input type="date" id="f-end">
    </div>
    <div class="f">
      <label>Departman</label>
      <select id="f-dep"><option value="">Tumu</option></select>
    </div>
    <div class="f">
      <label>Filtre</label>
      <div class="radio-grp">
        <label><input type="radio" name="rf" value="all" checked> Tumu</label>
        <label><input type="radio" name="rf" value="miss_cikis"> Giris Var - Cikis Yok</label>
        <label><input type="radio" name="rf" value="miss_giris"> Giris Yok - Cikis Var</label>
        <label><input type="radio" name="rf" value="off_mesai"> Off da Mesai</label>
        <label><input type="radio" name="rf" value="fm"> Fazla Mesai</label>
      </div>
    </div>
  </div>

  <div style="overflow-x:auto">
    <table>
      <thead>
        <tr>
          <th>PDKS ID</th>
          <th>Departman</th>
          <th>Gorev</th>
          <th>Ad Soyad</th>
          <th>Gun</th>
          <th>Tarih</th>
          <th>Planlanan Vardiya</th>
          <th>Gercek Vardiya</th>
          <th>Giris Saati</th>
          <th>Cikis Saati</th>
          <th>Toplam Cal.</th>
          <th>Gunluk Cal.</th>
          <th>FM Sure</th>
          <th>Durum</th>
        </tr>
      </thead>
      <tbody id="att-body">
        <tr><td colspan="14" style="text-align:center;padding:40px;color:var(--muted)">Listele butonuna basin...</td></tr>
      </tbody>
    </table>
  </div>
  <div class="footer-bar">
    <span id="f-cnt">-</span>
    <span id="f-sum"></span>
  </div>
</div>

<div class="ctx" id="ctx"></div>
<div class="ov" id="ov"></div>

<!-- Duzenle Modal -->
<div class="modal" id="edit-modal">
  <div class="mbox">
    <h3>Satir Duzenle</h3>
    <div class="minfo" id="edit-info"></div>
    <input type="hidden" id="edit-id">
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

<!-- G/C Hareketler Modal -->
<div class="modal" id="har-modal">
  <div class="mbox">
    <h3 id="har-title">G/C Hareketler</h3>
    <div class="hlist" id="har-list"></div>
    <div class="mbtns"><button class="btn btn-ghost" id="har-close">Kapat</button></div>
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
var rawData=[]; var employees=[];

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('on');},2500);}
function isoDate(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function ini(s){var p=(s||'').trim().split(' ');return((p[0]||'')[0]||'')+((p[1]||'')[0]||'');}
function timeMins(g,c){
  if(!g||!c)return null;
  var gp=g.split(':').map(Number); var cp=c.split(':').map(Number);
  var m=(cp[0]*60+cp[1])-(gp[0]*60+gp[1]);
  if(m<0)m+=1440; return m;
}
function fmtM(m){if(m==null||m<0)return '-';return String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0');}

// Tarihleri bugune ayarla
var now=new Date();
document.getElementById('f-start').value=isoDate(new Date(now.getFullYear(),now.getMonth(),now.getDate()));
document.getElementById('f-end').value=isoDate(new Date(now.getFullYear(),now.getMonth(),now.getDate()));

function getFilterVal(){return document.querySelector('input[name=rf]:checked').value;}

function applyFilter(data){
  var f=getFilterVal(); var dep=document.getElementById('f-dep').value;
  var d=dep?data.filter(function(r){return r.dep===dep;}):data;
  if(f==='all')return d;
  if(f==='miss_cikis')return d.filter(function(r){return r.giris&&!r.cikis;});
  if(f==='miss_giris')return d.filter(function(r){return !r.giris&&r.cikis;});
  if(f==='off_mesai')return d.filter(function(r){return r.status==='off_mesai'||r.shiftMismatch;});
  if(f==='fm')return d.filter(function(r){var m=timeMins(r.giris,r.cikis);return m!=null&&m>540;});
  return d;
}

function getStatus(r){
  var m=timeMins(r.giris,r.cikis);
  var sc=r.plannedShift;
  var isOff=(sc==='HT'||sc==='OFF');
  if(r.giris&&isOff)return 'off_mesai';
  if(r.giris&&!r.cikis)return 'miss_cikis';
  if(!r.giris&&!r.cikis&&r.plannedShift&&r.plannedShift!=='-')return 'gelmedi';
  if(m!=null&&m>540)return 'fm';
  if(m!=null&&m>0)return 'ok';
  return 'ok';
}

function render(){
  var filtered=applyFilter(rawData);
  if(!filtered.length){
    document.getElementById('att-body').innerHTML='<tr><td colspan="14" style="text-align:center;padding:40px;color:var(--muted)">Kayit bulunamadi</td></tr>';
    document.getElementById('f-cnt').textContent='0 kayit';
    document.getElementById('f-sum').textContent='';
    return;
  }

  // Dep filter guncelle
  var deps=[''];
  rawData.forEach(function(r){if(deps.indexOf(r.dep)<0)deps.push(r.dep);});
  var dsel=document.getElementById('f-dep'); var curDep=dsel.value;
  dsel.innerHTML=deps.map(function(d){return '<option value="'+d+'"'+(d===curDep?' selected':'')+' >'+(d||'Tumu')+'</option>';}).join('');

  var totalWork=0,totalFm=0;
  var html=filtered.map(function(r){
    var dow=new Date(r.day+'T12:00:00').getDay();
    var m=timeMins(r.giris,r.cikis);
    var fm=(m!=null&&m>540)?m-540:0;
    var gunluk=m!=null?Math.min(m,540):null;
    if(gunluk!=null)totalWork+=gunluk;
    totalFm+=fm;
    var status=getStatus(r);
    var statusHtml='';
    if(status==='miss_cikis')statusHtml='<span class="pill p-miss">Cikis yok</span>';
    else if(status==='off_mesai')statusHtml='<span class="pill p-off">Off da Mesai</span>';
    else if(status==='gelmedi')statusHtml='<span class="pill p-gelmedi">Gelmedi</span>';
    else if(status==='fm')statusHtml='<span class="pill p-fm">FM: '+fmtM(fm)+'</span>';
    else if(status==='ht')statusHtml='<span class="pill p-ht">HT</span>';
    else statusHtml='<span class="pill p-ok">Tamamlandi</span>';

    var vardiyaHtml=(r.vardiya||'-');
    if(r.shiftMismatch)vardiyaHtml+='<span class="mismatch">&#9888; Farkli vardiya</span>';

    return '<tr data-id="'+(r.id||'')+'" data-r="'+encodeURIComponent(JSON.stringify(r))+'">'
      +'<td class="mono" style="color:var(--muted)">#'+r.sicil+'</td>'
      +'<td style="font-size:11.5px;color:var(--muted)">'+r.dep+'</td>'
      +'<td style="font-size:11.5px;color:var(--muted)">'+r.gorev+'</td>'
      +'<td><div class="who"><div class="av">'+ini(r.ad)+'</div><b>'+r.ad+'</b></div></td>'
      +'<td style="font-size:11.5px">'+GUNLER[dow]+'</td>'
      +'<td class="mono">'+r.day+'</td>'
      +'<td style="font-size:11.5px;color:var(--blue)">'+(r.plannedShift||'-')+'</td>'
      +'<td style="font-size:11.5px">'+vardiyaHtml+'</td>'
      +'<td class="mono">'+(r.giris||'-')+'</td>'
      +'<td class="mono">'+(r.cikis||'-')+'</td>'
      +'<td class="mono">'+fmtM(m)+'</td>'
      +'<td class="mono">'+fmtM(gunluk)+'</td>'
      +'<td class="mono">'+(fm>0?('<span style="color:var(--amber)">'+fmtM(fm)+'</span>'):'-')+'</td>'
      +'<td>'+statusHtml+'</td>'
      +'</tr>';
  }).join('');
  document.getElementById('att-body').innerHTML=html;
  document.getElementById('f-cnt').textContent=filtered.length+' kayit';
  document.getElementById('f-sum').textContent='Toplam: '+fmtM(totalWork)+' | FM: '+fmtM(totalFm);

  // Sag tik
  document.querySelectorAll('#att-body tr').forEach(function(tr){
    tr.addEventListener('contextmenu',function(e){
      e.preventDefault(); e.stopPropagation();
      var r=JSON.parse(decodeURIComponent(tr.dataset.r));
      showCtx(e.clientX,e.clientY,r);
    });
  });
}

function showCtx(x,y,r){
  closeCtx();
  var c=document.getElementById('ctx');
  c.innerHTML='<div class="ctx-item" id="cx-edit">&#9998; Satir Duzenle</div>'
    +'<div class="ctx-item" id="cx-har">&#8646; G/C Hareketler</div>'
    +(r.id?'<div class="ctx-sep"></div><div class="ctx-item danger" id="cx-del">&#10005; Satiri Sil</div>':'');
  c.style.cssText='display:block;left:'+Math.min(x,window.innerWidth-190)+'px;top:'+Math.min(y,window.innerHeight-150)+'px';
  document.getElementById('cx-edit').onclick=function(){openEdit(r);closeCtx();};
  document.getElementById('cx-har').onclick=function(){openHar(r);closeCtx();};
  var cd=document.getElementById('cx-del');
  if(cd)cd.onclick=async function(){
    closeCtx();
    if(!confirm(r.ad+' kaydini silmek istediginizden emin misiniz?'))return;
    try{await req('/attendance/'+r.id,{method:'DELETE'});toast('Silindi');listele();}
    catch(e){toast('Hata: '+e.message);}
  };
}
function closeCtx(){document.getElementById('ctx').style.display='none';}
document.addEventListener('click',closeCtx);

function openEdit(r){
  document.getElementById('edit-id').value=r.id||'';
  document.getElementById('edit-info').innerHTML='<b>'+r.ad+'</b> &nbsp;|&nbsp; '+r.day+' &nbsp;|&nbsp; '+(r.plannedShift||'-');
  document.getElementById('edit-gdate').value=r.day;
  document.getElementById('edit-giris').value=r.giris||'';
  document.getElementById('edit-cdate').value=r.day;
  document.getElementById('edit-cikis').value=r.cikis||'';
  document.getElementById('ov').style.display='block';
  document.getElementById('edit-modal').classList.add('open');
}

function openHar(r){
  document.getElementById('har-title').textContent='G/C Hareketler - '+r.ad;
  var same=rawData.filter(function(x){return x.tc===r.tc;}).sort(function(a,b){return b.day.localeCompare(a.day);});
  document.getElementById('har-list').innerHTML=same.map(function(x){
    var m=timeMins(x.giris,x.cikis);
    return '<div class="hitem">'
      +'<div><b class="mono">'+x.day+'</b><div style="font-size:11px;color:var(--muted)">'+( x.vardiya||x.plannedShift||'-')+'</div></div>'
      +'<div style="text-align:right"><div class="mono">'+(x.giris||'-')+' - '+(x.cikis||'-')+'</div>'
      +'<div style="font-size:11px;color:var(--muted)">'+fmtM(m)+'</div></div>'
      +'</div>';
  }).join('')||'<div style="color:var(--muted);text-align:center;padding:16px;font-size:12px">Kayit yok</div>';
  document.getElementById('ov').style.display='block';
  document.getElementById('har-modal').classList.add('open');
}

function closeModals(){
  document.getElementById('ov').style.display='none';
  ['edit-modal','har-modal','add-modal'].forEach(function(id){document.getElementById(id).classList.remove('open');});
}

document.getElementById('ov').addEventListener('click',closeModals);
document.getElementById('edit-cancel').addEventListener('click',closeModals);
document.getElementById('har-close').addEventListener('click',closeModals);
document.getElementById('add-cancel').addEventListener('click',closeModals);

document.getElementById('edit-save').addEventListener('click',async function(){
  var id=document.getElementById('edit-id').value;
  if(!id){toast('Kayit ID yok (shift plani satiri duzenlenemez)');return;}
  var giris=document.getElementById('edit-giris').value;
  var cikis=document.getElementById('edit-cikis').value;
  try{await req('/attendance/'+id,{method:'PUT',body:{giris:giris,cikis:cikis}});toast('Guncellendi');closeModals();listele();}
  catch(e){toast('Hata: '+e.message);}
});

document.getElementById('add-btn').addEventListener('click',function(){
  document.getElementById('add-emp').innerHTML=employees.map(function(e){return '<option value="'+e.tc+'">'+e.ad+' (#'+e.sicil+')</option>';}).join('');
  document.getElementById('add-gdate').value=document.getElementById('f-start').value;
  document.getElementById('add-cdate').value=document.getElementById('f-start').value;
  document.getElementById('ov').style.display='block';
  document.getElementById('add-modal').classList.add('open');
});

document.getElementById('add-save').addEventListener('click',async function(){
  var tc=document.getElementById('add-emp').value;
  var gdate=document.getElementById('add-gdate').value;
  var giris=document.getElementById('add-giris').value;
  var cdate=document.getElementById('add-cdate').value;
  var cikis=document.getElementById('add-cikis').value;
  if(!tc||!gdate||!giris){toast('Personel ve giris saati gerekli');return;}
  try{await req('/attendance',{method:'POST',body:{tc:tc,day:gdate,giris:giris,cikis:cikis||null}});toast('Eklendi');closeModals();listele();}
  catch(e){toast('Hata: '+e.message);}
});

async function listele(){
  var start=document.getElementById('f-start').value;
  var end=document.getElementById('f-end').value;
  if(!start||!end)return;
  document.getElementById('att-body').innerHTML='<tr><td colspan="14" style="text-align:center;padding:40px;color:var(--muted)">Yukleniyor...</td></tr>';
  try{
    rawData=await req('/attendance/report?start='+start+'&end='+end);
    render();
  }catch(e){
    document.getElementById('att-body').innerHTML='<tr><td colspan="14" style="text-align:center;padding:40px;color:var(--danger)">Hata: '+e.message+'</td></tr>';
  }
}

document.getElementById('list-btn').addEventListener('click',listele);
document.querySelectorAll('input[name=rf]').forEach(function(r){r.addEventListener('change',render);});
document.getElementById('f-dep').addEventListener('change',render);

document.getElementById('excel-btn').addEventListener('click',function(){
  var filtered=applyFilter(rawData);
  var csv='PDKS ID,Departman,Gorev,Ad Soyad,Gun,Tarih,Planlanan Vardiya,Gercek Vardiya,Giris,Cikis,Toplam,Gunluk,FM,Durum\n';
  filtered.forEach(function(r){
    var dow=new Date(r.day+'T12:00:00').getDay();
    var m=timeMins(r.giris,r.cikis);
    var fm=(m!=null&&m>540)?m-540:0;
    csv+=r.sicil+','+r.dep+','+r.gorev+','+r.ad+','+GUNLER[dow]+','+r.day+','+(r.plannedShift||'-')+','+(r.vardiya||'-')+','+(r.giris||'')+','+(r.cikis||'')+','+fmtM(m)+','+fmtM(m?Math.min(m,540):null)+','+fmtM(fm)+','+getStatus(r)+'\n';
  });
  var blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download='gecis-'+document.getElementById('f-start').value+'_'+document.getElementById('f-end').value+'.csv';a.click();
});

document.getElementById('print-btn').addEventListener('click',function(){window.print();});

// Init
(async function(){
  try{employees=(await req('/employees')||[]).filter(function(e){return e.status==='aktif';});}catch(e){}
  listele();
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
