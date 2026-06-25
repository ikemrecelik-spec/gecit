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
.ctx{position:fixed;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:4px;z-index:99;box-shadow:0 12px 36px rgba(0,0,0,.55);min-width:180px;display:none}
.ctx-item{padding:7px 12px;border-radius:7px;cursor:pointer;font-size:12.5px;display:flex;align-items:center;gap:8px}
.ctx-item:hover{background:var(--panel-2)}
.ctx-item.danger{color:var(--danger)}
.ctx-sep{border-top:1px solid var(--line);margin:3px 0}
.ov{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:80;display:none}
.modal{position:fixed;inset:0;z-index:81;display:none;align-items:center;justify-content:center}
.modal.open{display:flex}
.mbox{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;width:460px;max-width:94vw;box-shadow:0 20px 60px rgba(0,0,0,.5);max-height:90vh;overflow-y:auto}
.mbox h3{font-family:'Space Grotesk';font-size:15px;margin:0 0 14px}
.minfo{background:var(--panel-2);border-radius:8px;padding:9px 12px;margin-bottom:12px;font-size:12px;color:var(--muted);line-height:1.6}
.field{margin-bottom:11px}
.field label{display:block;font-size:11px;color:var(--muted);margin-bottom:4px;font-weight:600;text-transform:uppercase}
.field input,.field select{width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;padding:8px 11px;color:var(--text);font-family:inherit;font-size:12.5px;outline:none}
.field input:focus,.field select:focus{border-color:var(--amber)}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.mbtns{display:flex;gap:8px;justify-content:flex-end;margin-top:14px}
.hlist{max-height:320px;overflow-y:auto;margin-bottom:12px}
.hitem{background:var(--panel-2);border-radius:8px;margin-bottom:6px;overflow:hidden}
.hitem-head{display:flex;align-items:center;justify-content:space-between;padding:8px 12px;font-size:12px;border-bottom:1px solid var(--line)}
.hitem-body{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:6px;padding:8px 12px;font-size:11.5px}
.hitem-body span{color:var(--muted)}
.hitem-body b{color:var(--text);font-family:'JetBrains Mono'}
.genel-row{background:var(--panel-2);border-radius:8px;margin-bottom:6px;padding:10px 12px}
.genel-row-head{display:flex;align-items:center;gap:8px;margin-bottom:8px;font-size:12px;font-weight:600}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:11px 18px;border-radius:10px;font-size:12.5px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
</style>

<div class="topbar">
  <h1>Giris / Cikis Islemleri</h1>
  <div style="display:flex;gap:6px;margin-left:auto;flex-wrap:wrap">
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
      <label>Vardiya</label>
      <select id="f-vard">
        <option value="">Tumu</option>
        <option value="C">C - Gece (00:00-08:00)</option>
        <option value="A">A - Sabah (08:00-16:00)</option>
        <option value="D">D - Oglen (09:00-17:00)</option>
        <option value="E">E - Ikindi (13:00-21:00)</option>
        <option value="Ara">Ara - Aksam (12:00-20:00)</option>
        <option value="B">B - Gece (16:00-24:00)</option>
        <option value="Gece">Gece - Sabah (24:00-08:00)</option>
        <option value="-">Plansiz</option>
      </select>
    </div>
    <div class="f">
      <label>Durum</label>
      <div class="radio-grp">
        <label><input type="radio" name="rf" value="all" checked> Tumu</label>
        <label><input type="radio" name="rf" value="miss_cikis"> Giris Var - Cikis Yok</label>
        <label><input type="radio" name="rf" value="miss_giris"> Giris Yok - Cikis Var</label>
        <label><input type="radio" name="rf" value="off_mesai"> Off da Mesai</label>
        <label><input type="radio" name="rf" value="fm"> Fazla Mesai</label>
        <label><input type="radio" name="rf" value="gelmedi"> Gelmedi</label>
      </div>
    </div>
  </div>
  <div style="overflow-x:auto">
    <table>
      <thead>
        <tr>
          <th>PDKS ID</th><th>Departman</th><th>Gorev</th><th>Ad Soyad</th>
          <th>Gun</th><th>Tarih</th><th>Planlanan</th><th>Gercek Vardiya</th>
          <th>Giris</th><th>Cikis</th><th>Toplam</th><th>Gunluk</th><th>FM</th><th>Durum</th>
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

<!-- Satir Duzenle Modal -->
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
    <div class="field-row">
      <div class="field"><label>Yemek Suresi (dk)</label><input id="edit-yemek" type="number" min="0" max="120" value="0"></div>
      <div class="field"><label>Mola Suresi (dk)</label><input id="edit-mola" type="number" min="0" max="120" value="0"></div>
    </div>
    <div class="field">
      <label>Vardiya Durumu (Degistir)</label>
      <select id="edit-vardiya">
        <option value="">-- Degistirme --</option>
        <option value="C · 00:00–08:00">C - 00:00-08:00</option>
        <option value="A · 08:00–16:00">A - 08:00-16:00</option>
        <option value="D · 09:00–17:00">D - 09:00-17:00</option>
        <option value="E · 13:00–21:00">E - 13:00-21:00</option>
        <option value="Ara · 12:00–20:00">Ara - 12:00-20:00</option>
        <option value="B · 16:00–24:00">B - 16:00-24:00</option>
        <option value="Gece · 24:00–08:00">Gece - 24:00-08:00</option>
      </select>
    </div>
    <div class="mbtns">
      <button class="btn btn-ghost" id="edit-cancel">Iptal</button>
      <button class="btn btn-amber" id="edit-save">Guncelle</button>
    </div>
  </div>
</div>

<!-- G/C Hareketler Modal -->
<div class="modal" id="har-modal">
  <div class="mbox" style="width:560px">
    <h3 id="har-title">G/C Hareketler</h3>
    <div style="display:flex;gap:8px;margin-bottom:12px">
      <div class="f" style="flex:1"><label>Ay</label>
        <select id="har-month"></select>
      </div>
      <div class="f" style="flex:1"><label>Yil</label>
        <select id="har-year"></select>
      </div>
      <div class="f" style="justify-content:flex-end">
        <label>&nbsp;</label>
        <button class="btn btn-amber" id="har-load">Yukle</button>
      </div>
    </div>
    <div class="hlist" id="har-list"></div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding-top:8px;border-top:1px solid var(--line)">
      <span id="har-sum" style="font-size:12px;color:var(--muted)"></span>
      <button class="btn btn-ghost" id="har-close">Kapat</button>
    </div>
  </div>
</div>

<!-- Genel Duzenleme Modal -->
<div class="modal" id="genel-modal">
  <div class="mbox" style="width:600px">
    <h3 id="genel-title">Genel Duzenleme</h3>
    <div style="display:flex;gap:8px;margin-bottom:12px;align-items:flex-end">
      <div class="f"><label>Ay</label><select id="genel-month"></select></div>
      <div class="f"><label>Yil</label><select id="genel-year"></select></div>
      <button class="btn btn-amber" id="genel-load">Yukle</button>
    </div>
    <div class="hlist" id="genel-list"></div>
    <div class="mbtns"><button class="btn btn-ghost" id="genel-close">Kapat</button></div>
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
var AYLAR=['Ocak','Subat','Mart','Nisan','Mayis','Haziran','Temmuz','Agustos','Eylul','Ekim','Kasim','Aralik'];
var SHIFT_ORDER={'C':0,'A':1,'D':2,'E':3,'Ara':4,'B':5,'Gece':6,'-':7};
var rawData=[];

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

var now=new Date();
document.getElementById('f-start').value=isoDate(new Date(now.getFullYear(),now.getMonth(),now.getDate()));
document.getElementById('f-end').value=isoDate(new Date(now.getFullYear(),now.getMonth(),now.getDate()));

function getFilterVal(){return document.querySelector('input[name=rf]:checked').value;}
function shiftKey(s){return s?s.split(' ')[0]:'-';}

function applyFilter(data){
  var f=getFilterVal();
  var dep=document.getElementById('f-dep').value;
  var vard=document.getElementById('f-vard').value;
  var d=dep?data.filter(function(r){return r.dep===dep;}):data;
  if(vard)d=d.filter(function(r){
    var sk=shiftKey(r.plannedShift||r.vardiya||'-');
    return sk===vard;
  });
  if(f==='all')return d;
  if(f==='miss_cikis')return d.filter(function(r){return r.giris&&!r.cikis;});
  if(f==='miss_giris')return d.filter(function(r){return !r.giris&&r.cikis;});
  if(f==='off_mesai')return d.filter(function(r){var sc=r.plannedShift;return r.giris&&(sc==='HT'||sc==='OFF');});
  if(f==='fm')return d.filter(function(r){var m=timeMins(r.giris,r.cikis);return m!=null&&m>540;});
  if(f==='gelmedi')return d.filter(function(r){return !r.giris&&!r.cikis&&r.plannedShift&&r.plannedShift!=='-';});
  return d;
}

function sortData(data){
  return data.slice().sort(function(a,b){
    if(a.day!==b.day)return a.day.localeCompare(b.day);
    var sa=SHIFT_ORDER[shiftKey(a.plannedShift)]??99;
    var sb=SHIFT_ORDER[shiftKey(b.plannedShift)]??99;
    return sa-sb;
  });
}

function getStatus(r){
  var m=timeMins(r.giris,r.cikis);
  var sc=r.plannedShift;
  if(r.giris&&(sc==='HT'||sc==='OFF'))return 'off_mesai';
  if(r.giris&&!r.cikis)return 'miss_cikis';
  if(!r.giris&&!r.cikis&&sc&&sc!=='-')return 'gelmedi';
  if(m!=null&&m>540)return 'fm';
  return 'ok';
}

function render(){
  var filtered=sortData(applyFilter(rawData));
  var deps=[''];
  rawData.forEach(function(r){if(deps.indexOf(r.dep)<0)deps.push(r.dep);});
  var dsel=document.getElementById('f-dep'); var cv=dsel.value;
  dsel.innerHTML=deps.map(function(d){return '<option value="'+d+'"'+(d===cv?' selected':'')+' >'+(d||'Tumu')+'</option>';}).join('');

  if(!filtered.length){
    document.getElementById('att-body').innerHTML='<tr><td colspan="14" style="text-align:center;padding:40px;color:var(--muted)">Kayit bulunamadi</td></tr>';
    document.getElementById('f-cnt').textContent='0 kayit';
    document.getElementById('f-sum').textContent='';
    return;
  }

  var tw=0,tf=0;
  var html=filtered.map(function(r){
    var dow=new Date(r.day+'T12:00:00').getDay();
    var m=timeMins(r.giris,r.cikis);
    var fm=(m!=null&&m>540)?m-540:0;
    var gl=m!=null?Math.min(m,540):null;
    if(gl!=null)tw+=gl; tf+=fm;
    var st=getStatus(r);
    var stHtml='';
    if(st==='miss_cikis')stHtml='<span class="pill p-miss">Cikis yok</span>';
    else if(st==='off_mesai')stHtml='<span class="pill p-off">Off Mesai</span>';
    else if(st==='gelmedi')stHtml='<span class="pill p-gelmedi">Gelmedi</span>';
    else if(st==='fm')stHtml='<span class="pill p-fm">FM: '+fmtM(fm)+'</span>';
    else stHtml='<span class="pill p-ok">Tamamlandi</span>';
    var vHtml=(r.vardiya||'-');
    if(r.shiftMismatch)vHtml+='<span class="mismatch">&#9888; Farkli</span>';
    return '<tr data-r="'+encodeURIComponent(JSON.stringify(r))+'">'
      +'<td class="mono" style="color:var(--muted)">#'+r.sicil+'</td>'
      +'<td style="font-size:11px;color:var(--muted)">'+r.dep+'</td>'
      +'<td style="font-size:11px;color:var(--muted)">'+r.gorev+'</td>'
      +'<td><div class="who"><div class="av">'+ini(r.ad)+'</div><b>'+r.ad+'</b></div></td>'
      +'<td style="font-size:11px">'+GUNLER[dow]+'</td>'
      +'<td class="mono">'+r.day+'</td>'
      +'<td style="font-size:11px;color:var(--blue)">'+(r.plannedShift||'-')+'</td>'
      +'<td style="font-size:11px">'+vHtml+'</td>'
      +'<td class="mono">'+(r.giris||'-')+'</td>'
      +'<td class="mono">'+(r.cikis||'-')+'</td>'
      +'<td class="mono">'+fmtM(m)+'</td>'
      +'<td class="mono">'+fmtM(gl)+'</td>'
      +'<td class="mono">'+(fm>0?('<span style="color:var(--amber)">'+fmtM(fm)+'</span>'):'-')+'</td>'
      +'<td>'+stHtml+'</td>'
      +'</tr>';
  }).join('');
  document.getElementById('att-body').innerHTML=html;
  document.getElementById('f-cnt').textContent=filtered.length+' kayit';
  document.getElementById('f-sum').textContent='Toplam: '+fmtM(tw)+' | FM: '+fmtM(tf);

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
    +'<div class="ctx-item" id="cx-genel">&#9783; Genel Duzenleme</div>'
    +'<div class="ctx-item" id="cx-har">&#8646; G/C Hareketler</div>'
    +(r.id?'<div class="ctx-sep"></div><div class="ctx-item danger" id="cx-del">&#10005; Satiri Sil</div>':'');
  c.style.cssText='display:block;left:'+Math.min(x,window.innerWidth-200)+'px;top:'+Math.min(y,window.innerHeight-160)+'px';
  document.getElementById('cx-edit').onclick=function(){openEdit(r);closeCtx();};
  document.getElementById('cx-genel').onclick=function(){openGenel(r);closeCtx();};
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
  document.getElementById('edit-info').innerHTML='<b>'+r.ad+'</b> | '+r.day+' | Planlanan: <b style="color:var(--blue)">'+(r.plannedShift||'-')+'</b>'+(r.vardiya&&r.shiftMismatch?' | Gercek: <span style="color:#FF9E6B">'+r.vardiya+'</span>':'');
  document.getElementById('edit-gdate').value=r.day;
  document.getElementById('edit-giris').value=r.giris||'';
  document.getElementById('edit-cdate').value=r.day;
  document.getElementById('edit-cikis').value=r.cikis||'';
  document.getElementById('edit-yemek').value=r.yemek||0;
  document.getElementById('edit-mola').value=r.mola||0;
  document.getElementById('edit-vardiya').value='';
  document.getElementById('ov').style.display='block';
  document.getElementById('edit-modal').classList.add('open');
}

function buildMonthYearSelects(mSel,ySel){
  mSel.innerHTML=AYLAR.map(function(a,i){return '<option value="'+(i+1)+'"'+(i===now.getMonth()?' selected':'')+'>'+a+'</option>';}).join('');
  ySel.innerHTML='';
  for(var y=now.getFullYear()-1;y<=now.getFullYear()+1;y++){
    var o=document.createElement('option');o.value=y;o.textContent=y;
    if(y===now.getFullYear())o.selected=true;
    ySel.appendChild(o);
  }
}

async function loadHarData(tc,month,year){
  var pad=function(n){return String(n).padStart(2,'0');};
  var start=year+'-'+pad(month)+'-01';
  var lastDay=new Date(year,month,0).getDate();
  var end=year+'-'+pad(month)+'-'+lastDay;
  try{
    var all=await req('/attendance');
    return all.filter(function(r){return r.tc===tc&&r.day>=start&&r.day<=end;})
      .sort(function(a,b){return a.day.localeCompare(b.day);});
  }catch(e){return [];}
}

function renderHarList(data,tc){
  if(!data.length)return '<div style="color:var(--muted);text-align:center;padding:20px;font-size:12px">Bu ay kayit yok</div>';
  var tw=0,tf=0,ht=0;
  var html=data.map(function(r){
    var dow=new Date(r.day+'T12:00:00').getDay();
    var m=timeMins(r.giris,r.cikis);
    var fm=(m!=null&&m>540)?m-540:0;
    var gl=m!=null?Math.min(m,540):null;
    if(gl!=null)tw+=gl; tf+=fm;
    var scRaw=rawData.find(function(x){return x.tc===tc&&x.day===r.day;});
    var sc=scRaw?scRaw.plannedShift:null;
    if(sc==='HT'&&r.giris)ht++;
    var statusColor=r.cikis?'var(--mint)':(r.giris?'var(--amber)':'var(--muted)');
    return '<div class="hitem">'
      +'<div class="hitem-head"><b class="mono">'+r.day+'</b><span style="font-size:11px">'+GUNLER[dow]+'</span><span style="color:var(--blue);font-size:11px">'+(r.vardiya||'-')+'</span><span style="color:'+statusColor+';font-size:11px">&#9679;</span></div>'
      +'<div class="hitem-body"><span>Giris</span><b>'+(r.giris||'-')+'</b><span>Cikis</span><b>'+(r.cikis||'-')+'</b><span>Toplam</span><b>'+fmtM(m)+'</b><span>FM</span><b style="color:var(--amber)">'+fmtM(fm)+'</b></div>'
      +'</div>';
  }).join('');
  document.getElementById('har-sum').textContent='Toplam: '+fmtM(tw)+' | FM: '+fmtM(tf)+' | HT calisme: '+ht;
  return html;
}

var harTC='';
function openHar(r){
  harTC=r.tc;
  document.getElementById('har-title').textContent='G/C Hareketler - '+r.ad;
  buildMonthYearSelects(document.getElementById('har-month'),document.getElementById('har-year'));
  document.getElementById('har-list').innerHTML='<div style="color:var(--muted);text-align:center;padding:16px;font-size:12px">Yukle butonuna basin...</div>';
  document.getElementById('har-sum').textContent='';
  document.getElementById('ov').style.display='block';
  document.getElementById('har-modal').classList.add('open');
}

document.getElementById('har-load').addEventListener('click',async function(){
  var month=+document.getElementById('har-month').value;
  var year=+document.getElementById('har-year').value;
  document.getElementById('har-list').innerHTML='<div style="color:var(--muted);text-align:center;padding:16px;font-size:12px">Yukleniyor...</div>';
  var data=await loadHarData(harTC,month,year);
  document.getElementById('har-list').innerHTML=renderHarList(data,harTC);
});

var genelTC=''; var genelAd='';
function openGenel(r){
  genelTC=r.tc; genelAd=r.ad;
  document.getElementById('genel-title').textContent='Genel Duzenleme - '+r.ad;
  buildMonthYearSelects(document.getElementById('genel-month'),document.getElementById('genel-year'));
  document.getElementById('genel-list').innerHTML='<div style="color:var(--muted);text-align:center;padding:16px;font-size:12px">Yukle butonuna basin...</div>';
  document.getElementById('ov').style.display='block';
  document.getElementById('genel-modal').classList.add('open');
}

document.getElementById('genel-load').addEventListener('click',async function(){
  var month=+document.getElementById('genel-month').value;
  var year=+document.getElementById('genel-year').value;
  document.getElementById('genel-list').innerHTML='<div style="color:var(--muted);text-align:center;padding:16px;font-size:12px">Yukleniyor...</div>';
  var data=await loadHarData(genelTC,month,year);
  if(!data.length){document.getElementById('genel-list').innerHTML='<div style="color:var(--muted);text-align:center;padding:16px;font-size:12px">Bu ay kayit yok</div>';return;}
  var html=data.map(function(r){
    var dow=new Date(r.day+'T12:00:00').getDay();
    return '<div class="genel-row" data-id="'+r.id+'">'
      +'<div class="genel-row-head"><span class="mono">'+r.day+'</span><span style="color:var(--muted);font-size:11px">'+GUNLER[dow]+'</span><span style="color:var(--blue);font-size:11px">'+(r.vardiya||'-')+'</span></div>'
      +'<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:6px">'
      +'<div><div style="font-size:10px;color:var(--muted);margin-bottom:3px">GİRİŞ SAATİ</div><input class="genel-giris" type="time" value="'+(r.giris||'')+'" style="width:100%;background:var(--panel);border:1px solid var(--line);color:var(--text);border-radius:7px;padding:6px 8px;font-family:JetBrains Mono,monospace;font-size:12px"></div>'
      +'<div><div style="font-size:10px;color:var(--muted);margin-bottom:3px">ÇIKIŞ SAATİ</div><input class="genel-cikis" type="time" value="'+(r.cikis||'')+'" style="width:100%;background:var(--panel);border:1px solid var(--line);color:var(--text);border-radius:7px;padding:6px 8px;font-family:JetBrains Mono,monospace;font-size:12px"></div>'
      +'<div><div style="font-size:10px;color:var(--muted);margin-bottom:3px">YEMEK (DK)</div><input class="genel-yemek" type="number" min="0" value="'+(r.yemek||0)+'" style="width:100%;background:var(--panel);border:1px solid var(--line);color:var(--text);border-radius:7px;padding:6px 8px;font-size:12px"></div>'
      +'<div><div style="font-size:10px;color:var(--muted);margin-bottom:3px">MOLA (DK)</div><input class="genel-mola" type="number" min="0" value="'+(r.mola||0)+'" style="width:100%;background:var(--panel);border:1px solid var(--line);color:var(--text);border-radius:7px;padding:6px 8px;font-size:12px"></div>'
      +'</div>'
      +'<div style="display:flex;justify-content:flex-end;margin-top:6px">'
      +'<button class="btn btn-amber genel-save-btn" style="padding:5px 12px;font-size:11.5px">Kaydet</button>'
      +'</div>'
      +'</div>';
  }).join('');
  document.getElementById('genel-list').innerHTML=html;

  document.querySelectorAll('.genel-save-btn').forEach(function(btn){
    btn.addEventListener('click',async function(){
      var row=btn.closest('[data-id]');
      var id=row.dataset.id;
      var giris=row.querySelector('.genel-giris').value;
      var cikis=row.querySelector('.genel-cikis').value;
      var yemek=+row.querySelector('.genel-yemek').value||0;
      var mola=+row.querySelector('.genel-mola').value||0;
      try{
        await req('/attendance/'+id,{method:'PUT',body:{giris:giris,cikis:cikis,yemek:yemek,mola:mola}});
        btn.textContent='Kaydedildi'; btn.style.background='var(--mint)'; btn.style.color='#0E1A24';
        setTimeout(function(){btn.textContent='Kaydet';btn.style.background='';btn.style.color='';},2000);
      }catch(e){toast('Hata: '+e.message);}
    });
  });
});

function closeModals(){
  document.getElementById('ov').style.display='none';
  ['edit-modal','har-modal','genel-modal'].forEach(function(id){document.getElementById(id).classList.remove('open');});
}
document.getElementById('ov').addEventListener('click',closeModals);
document.getElementById('edit-cancel').addEventListener('click',closeModals);
document.getElementById('har-close').addEventListener('click',closeModals);
document.getElementById('genel-close').addEventListener('click',closeModals);

document.getElementById('edit-save').addEventListener('click',async function(){
  var id=document.getElementById('edit-id').value;
  if(!id){toast('Bu satirda kayit yok, once QR okutulmali');return;}
  var body={
    giris:document.getElementById('edit-giris').value,
    cikis:document.getElementById('edit-cikis').value,
    yemek:+document.getElementById('edit-yemek').value||0,
    mola:+document.getElementById('edit-mola').value||0
  };
  var v=document.getElementById('edit-vardiya').value;
  if(v)body.vardiya=v;
  try{await req('/attendance/'+id,{method:'PUT',body:body});toast('Guncellendi');closeModals();listele();}
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
document.getElementById('f-vard').addEventListener('change',render);

document.getElementById('excel-btn').addEventListener('click',function(){
  var filtered=sortData(applyFilter(rawData));
  var csv='PDKS ID,Departman,Gorev,Ad Soyad,Gun,Tarih,Planlanan,Gercek Vardiya,Giris,Cikis,Toplam,Gunluk,FM,Durum\n';
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
listele();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-gecisler">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_GECISLER + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
