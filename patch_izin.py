NEW_IZIN = r'''<template id="tpl-izin">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Izin Yonetimi</title>
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
.section{display:none}.section.active{display:block}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;margin-bottom:14px}
.filter-bar{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end;padding:12px 16px;border-bottom:1px solid var(--line)}
.f{display:flex;flex-direction:column;gap:4px}
.f label{font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase}
.f input,.f select,.f textarea{background:var(--panel-2);border:1px solid var(--line);color:var(--text);border-radius:8px;padding:7px 10px;font-size:12.5px;font-family:inherit;outline:none}
.f input:focus,.f select:focus,.f textarea:focus{border-color:var(--amber)}
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
.empty{text-align:center;color:var(--muted);padding:40px;font-size:13px}
.footer-bar{display:flex;align-items:center;justify-content:space-between;padding:8px 16px;border-top:1px solid var(--line)}
.footer-bar span{color:var(--muted);font-size:11.5px}
.ov{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:80;display:none}
.modal{position:fixed;inset:0;z-index:81;display:none;align-items:center;justify-content:center}
.modal.open{display:flex}
.mbox{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;width:440px;max-width:94vw}
.mbox h3{font-family:'Space Grotesk';font-size:15px;margin:0 0 14px}
.field{margin-bottom:11px}
.field label{display:block;font-size:11px;color:var(--muted);margin-bottom:4px;font-weight:600;text-transform:uppercase}
.field input,.field select,.field textarea{width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;padding:8px 11px;color:var(--text);font-family:inherit;font-size:12.5px;outline:none}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.mbtns{display:flex;gap:8px;justify-content:flex-end;margin-top:14px}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:11px 18px;border-radius:10px;font-size:12.5px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
</style>

<div class="topbar">
  <h1>İzin Yönetimi</h1>
  <div class="tabs">
    <button class="tab active" data-t="beklemede">Bekleyen <span id="cnt-bekl" style="background:var(--danger);color:#fff;border-radius:10px;padding:1px 6px;font-size:10px;margin-left:4px">0</span></button>
    <button class="tab" data-t="onaylandi">Onaylanan</button>
    <button class="tab" data-t="reddedildi">Reddedilen</button>
    <button class="tab" data-t="tumu">Tümü</button>
  </div>
  <button class="btn btn-amber" id="add-btn" style="margin-left:auto">+ İzin Ekle</button>
</div>

<div class="card">
  <div class="filter-bar">
    <div class="f"><label>Departman</label><select id="f-dep"><option value="">Tümü</option></select></div>
    <div class="f"><label>İzin Türü</label><select id="f-tur"><option value="">Tümü</option></select></div>
    <div class="f"><label>Baş. Tarihi</label><input type="date" id="f-start"></div>
    <div class="f"><label>Bit. Tarihi</label><input type="date" id="f-end"></div>
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
      <th>İzin Türü</th><th>Başlangıç</th><th>Bitiş</th><th>Gün</th>
      <th>Açıklama</th><th>Durum</th><th></th>
    </tr></thead>
    <tbody id="izin-body"><tr><td colspan="10" class="empty">Listele butonuna basin...</td></tr></tbody>
  </table>
  <div class="footer-bar"><span id="izin-cnt">-</span><span id="izin-sum"></span></div>
</div>

<div class="ov" id="ov"></div>

<!-- Yeni İzin Modal -->
<div class="modal" id="add-modal">
  <div class="mbox">
    <h3>Yeni İzin Ekle</h3>
    <div class="field"><label>Personel</label><select id="add-emp"></select></div>
    <div class="field"><label>İzin Türü</label>
      <select id="add-tur">
        <option value="yillik">Yıllık İzin</option>
        <option value="ucretsiz">Ücretsiz İzin</option>
        <option value="hastalik">Hastalık Raporu</option>
        <option value="mazeret">Mazeret İzni</option>
        <option value="dogum">Doğum İzni</option>
        <option value="evlilik">Evlilik İzni</option>
        <option value="olum">Ölüm İzni</option>
        <option value="diger">Diğer</option>
      </select>
    </div>
    <div class="field-row">
      <div class="field"><label>Başlangıç</label><input id="add-start" type="date"></div>
      <div class="field"><label>Bitiş</label><input id="add-end" type="date"></div>
    </div>
    <div class="field"><label>Açıklama</label><textarea id="add-note" rows="2" placeholder="Opsiyonel..."></textarea></div>
    <div class="mbtns">
      <button class="btn btn-ghost" id="add-cancel">İptal</button>
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

var TUR_LABEL={yillik:'Yıllık İzin',ucretsiz:'Ücretsiz İzin',hastalik:'Hastalık Rpr.',mazeret:'Mazeret',dogum:'Doğum',evlilik:'Evlilik',olum:'Ölüm',diger:'Diğer'};
var curStatus='beklemede'; var allData=[]; var employees=[];

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('on');},2500);}
function ini(s){var p=(s||'').trim().split(' ');return((p[0]||'')[0]||'')+((p[1]||'')[0]||'');}
function daysBetween(s,e){return Math.round((new Date(e)-new Date(s))/86400000)+1;}

function applyFilter(data){
  var dep=document.getElementById('f-dep').value;
  var tur=document.getElementById('f-tur').value;
  var start=document.getElementById('f-start').value;
  var end=document.getElementById('f-end').value;
  return data.filter(function(r){
    if(dep&&r.dep!==dep)return false;
    if(tur&&r.type!==tur)return false;
    if(start&&r.end<start)return false;
    if(end&&r.start>end)return false;
    return true;
  });
}

function render(){
  var filtered=applyFilter(allData);
  var deps=[''],turs=[''];
  allData.forEach(function(r){
    if(deps.indexOf(r.dep)<0)deps.push(r.dep);
    if(turs.indexOf(r.type)<0)turs.push(r.type);
  });
  var dsel=document.getElementById('f-dep');var cv=dsel.value;
  dsel.innerHTML=deps.map(function(d){return '<option value="'+d+'"'+(d===cv?' selected':'')+' >'+(d||'Tümü')+'</option>';}).join('');
  var tsel=document.getElementById('f-tur');var ctv=tsel.value;
  tsel.innerHTML=turs.map(function(t){return '<option value="'+t+'"'+(t===ctv?' selected':'')+' >'+(t?TUR_LABEL[t]||t:'Tümü')+'</option>';}).join('');

  if(!filtered.length){
    document.getElementById('izin-body').innerHTML='<tr><td colspan="10" class="empty">Kayıt bulunamadı</td></tr>';
    document.getElementById('izin-cnt').textContent='0 kayıt';
    document.getElementById('izin-sum').textContent='';
    return;
  }

  var totalDays=0;
  document.getElementById('izin-body').innerHTML=filtered.map(function(r){
    var days=daysBetween(r.start,r.end);
    totalDays+=days;
    var st=r.status;
    var stHtml=st==='onaylandı'?'<span class="pill p-ok">Onaylandı</span>':st==='reddedildi'?'<span class="pill p-warn">Reddedildi</span>':'<span class="pill p-pend">Bekliyor</span>';
    var btns=st==='beklemede'?'<button class="btn-ok" data-id="'+r.id+'" data-a="onay">✓ Onayla</button> <button class="btn-no" data-id="'+r.id+'" data-a="red">✕ Reddet</button>':'';
    return '<tr>'
      +'<td class="mono" style="color:var(--muted)">#'+r.sicil+'</td>'
      +'<td><div class="who"><div class="av">'+ini(r.ad)+'</div><b>'+r.ad+'</b></div></td>'
      +'<td style="color:var(--muted);font-size:11.5px">'+r.dep+'</td>'
      +'<td><span class="pill p-blue">'+(TUR_LABEL[r.type]||r.type)+'</span></td>'
      +'<td class="mono">'+r.start+'</td>'
      +'<td class="mono">'+r.end+'</td>'
      +'<td class="mono" style="text-align:center"><b>'+days+'</b></td>'
      +'<td style="color:var(--muted);font-size:11.5px;max-width:150px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">'+(r.reason||'-')+'</td>'
      +'<td>'+stHtml+'</td>'
      +'<td style="white-space:nowrap">'+btns+'</td>'
      +'</tr>';
  }).join('');

  document.getElementById('izin-cnt').textContent=filtered.length+' kayıt';
  document.getElementById('izin-sum').textContent='Toplam: '+totalDays+' gün';

  // Onay/red butonları
  document.querySelectorAll('[data-a="onay"],[data-a="red"]').forEach(function(btn){
    btn.addEventListener('click',async function(){
      var id=btn.dataset.id; var a=btn.dataset.a;
      try{
        await req('/leaves/'+id+'/'+(a==='onay'?'approve':'reject'),{method:'POST'});
        toast(a==='onay'?'Onaylandı':'Reddedildi');
        load();
      }catch(e){toast('Hata: '+e.message);}
    });
  });
}

async function load(){
  try{
    var status=curStatus==='tumu'?undefined:curStatus;
    var url='/leaves'+(status?'?status='+status:'');
    allData=await req(url);
    // Bekleyen sayisi badge
    var bekl=await req('/leaves?status=beklemede').catch(function(){return [];});
    document.getElementById('cnt-bekl').textContent=bekl.length||'0';
    render();
  }catch(e){
    document.getElementById('izin-body').innerHTML='<tr><td colspan="10" class="empty">Hata: '+e.message+'</td></tr>';
  }
}

// Tab
document.querySelectorAll('.tab').forEach(function(t){
  t.addEventListener('click',function(){
    document.querySelectorAll('.tab').forEach(function(x){x.classList.remove('active');});
    t.classList.add('active');
    curStatus=t.dataset.t;
    load();
  });
});

document.getElementById('listele-btn').addEventListener('click',render);
document.getElementById('f-dep').addEventListener('change',render);
document.getElementById('f-tur').addEventListener('change',render);

// Yeni izin modal
document.getElementById('add-btn').addEventListener('click',function(){
  document.getElementById('add-emp').innerHTML=employees.map(function(e){return '<option value="'+e.tc+'">'+e.ad+' (#'+e.sicil+')</option>';}).join('');
  var now=new Date(); var today=now.getFullYear()+'-'+String(now.getMonth()+1).padStart(2,'0')+'-'+String(now.getDate()).padStart(2,'0');
  document.getElementById('add-start').value=today;
  document.getElementById('add-end').value=today;
  document.getElementById('add-note').value='';
  document.getElementById('ov').style.display='block';
  document.getElementById('add-modal').classList.add('open');
});

function closeModal(){
  document.getElementById('ov').style.display='none';
  document.getElementById('add-modal').classList.remove('open');
}
document.getElementById('ov').addEventListener('click',closeModal);
document.getElementById('add-cancel').addEventListener('click',closeModal);

document.getElementById('add-save').addEventListener('click',async function(){
  var tc=document.getElementById('add-emp').value;
  var type=document.getElementById('add-tur').value;
  var start=document.getElementById('add-start').value;
  var end=document.getElementById('add-end').value;
  var note=document.getElementById('add-note').value;
  if(!tc||!type||!start||!end){toast('Tüm alanları doldurun');return;}
  if(end<start){toast('Bitiş tarihi başlangıçtan önce olamaz');return;}
  var emp=employees.find(function(e){return e.tc===tc;});
  var days=daysBetween(start,end);
  try{
    // IK adina izin ekle
    await req('/leaves',{method:'POST',body:{tc:tc,ad:emp?emp.ad:'',type:type,start:start,end:end,days:days,reason:note,status:'onaylandı'}});
    toast('İzin eklendi');closeModal();load();
  }catch(e){
    // Alternatif endpoint
    try{
      await req('/leaves/add',{method:'POST',body:{tc:tc,type:type,start:start,end:end,days:days,reason:note}});
      toast('İzin eklendi');closeModal();load();
    }catch(e2){toast('Hata: '+e.message);}
  }
});

document.getElementById('excel-btn').addEventListener('click',function(){
  var filtered=applyFilter(allData);
  var csv='Sicil,Ad Soyad,Departman,Tur,Baslangic,Bitis,Gun,Aciklama,Durum\n';
  filtered.forEach(function(r){
    var days=daysBetween(r.start,r.end);
    csv+=r.sicil+','+r.ad+','+r.dep+','+(TUR_LABEL[r.type]||r.type)+','+r.start+','+r.end+','+days+','+(r.reason||'')+','+r.status+'\n';
  });
  var blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='izin-raporu.csv';a.click();
});

(async function(){
  try{employees=(await req('/employees')||[]).filter(function(e){return e.status==='aktif';});}catch(e){}
  load();
})();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-izin">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_IZIN + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
