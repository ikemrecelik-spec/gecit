NEW_ROLLER = '''<template id="tpl-roller">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Roller & Yetkiler</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--text:#EAF2F5;--muted:#8FA6B0;--radius:16px;--shadow:0 24px 60px rgba(0,0,0,.45)}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%) fixed;color:var(--text);font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:1100px;margin:0 auto;padding:22px 16px 70px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);overflow:hidden;margin-bottom:18px}
.ch{display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--line)}
.ch h3{font-family:'Space Grotesk';font-weight:700;font-size:16px;margin:0}
.ch p{color:var(--muted);font-size:12.5px;margin:4px 0 0}
table{width:100%;border-collapse:collapse}
thead th{text-align:left;font-size:11px;color:var(--muted);font-weight:600;padding:11px 16px;border-bottom:1px solid var(--line);white-space:nowrap}
tbody td{padding:10px 16px;border-bottom:1px solid rgba(35,65,79,.5);font-size:13px;vertical-align:middle}
tbody tr:hover{background:rgba(27,49,62,.4)}
.who{display:flex;align-items:center;gap:10px}
.av{width:32px;height:32px;border-radius:9px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:12px;color:#1a1205;background:linear-gradient(135deg,var(--amber),#d99a1f);flex:0 0 auto}
.who b{font-size:13px;font-weight:600}.who small{color:var(--muted);font-size:11px;display:block}
select{background:var(--panel-2);border:1px solid var(--line);color:var(--text);border-radius:8px;padding:7px 10px;font-size:12.5px;font-family:inherit;cursor:pointer}
select:focus{outline:none;border-color:var(--amber)}
.pill{display:inline-flex;align-items:center;font-size:11px;font-weight:600;padding:4px 9px;border-radius:7px}
.p-ik{background:rgba(242,181,59,.15);color:var(--amber)}
.p-sef{background:rgba(111,177,255,.15);color:var(--blue)}
.p-per{background:rgba(143,166,176,.15);color:var(--muted)}
.dep-tags{display:flex;flex-wrap:wrap;gap:5px}
.dep-tag{display:inline-flex;align-items:center;gap:5px;background:var(--panel-2);border:1px solid var(--line);border-radius:6px;padding:3px 8px;font-size:11.5px;cursor:pointer}
.dep-tag.on{background:rgba(111,177,255,.15);border-color:var(--blue);color:var(--blue)}
.save-btn{background:var(--amber);color:#1a1205;border:0;border-radius:9px;padding:8px 14px;font-weight:700;font-size:12.5px;cursor:pointer;white-space:nowrap}
.save-btn:disabled{opacity:.5;cursor:default}
.toast{position:fixed;bottom:26px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:13px 20px;border-radius:12px;font-size:13.5px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.empty{text-align:center;color:var(--muted);padding:30px;font-size:13px}
/* yetki matrisi */
.matrix{width:100%;border-collapse:collapse}
.matrix th{padding:12px 16px;font-size:12px;color:var(--muted);font-weight:600;border-bottom:1px solid var(--line);text-align:center}
.matrix th:first-child{text-align:left}
.matrix td{padding:11px 16px;border-bottom:1px solid rgba(35,65,79,.4);font-size:13px}
.matrix td:not(:first-child){text-align:center}
.ok{color:var(--mint);font-size:16px}.no{color:var(--danger);font-size:16px}.par{color:var(--muted);font-size:12px}
</style>
<div class="wrap">
  <div class="card">
    <div class="ch">
      <div><h3>Rol & Yetki Ataması</h3><p>Personele rol ata; Şef rolünde yetkili olduğu departman(lar)ı seç.</p></div>
      <button class="save-btn" id="save-all">Tümünü Kaydet</button>
    </div>
    <table>
      <thead><tr><th>Personel</th><th>Departman</th><th>Rol</th><th>Şef Departmanları</th></tr></thead>
      <tbody id="rol-body"><tr><td colspan="4" class="empty">Yükleniyor…</td></tr></tbody>
    </table>
  </div>

  <div class="card">
    <div class="ch"><div><h3>Yetki Matrisi</h3><p>Hangi rol neyi yapabilir?</p></div></div>
    <table class="matrix">
      <thead><tr><th>Yetki</th><th>İK / Yönetici<br><small style="color:var(--muted);font-weight:400">tam yetki</small></th><th>Şef / Yetkili<br><small style="color:var(--muted);font-weight:400">sınırlı</small></th><th>Personel<br><small style="color:var(--muted);font-weight:400">kendi kaydı</small></th></tr></thead>
      <tbody>
        <tr><td>Vardiya girişi</td><td><span class="ok">✓</span></td><td><span class="ok">✓</span></td><td><span class="no">✗</span></td></tr>
        <tr><td>Hafta tatili girişi</td><td><span class="ok">✓</span></td><td><span class="ok">✓</span></td><td><span class="no">✗</span></td></tr>
        <tr><td>Devam takip görüntüleme</td><td><span class="ok">✓</span></td><td><span class="ok">✓</span></td><td><span class="par">sadece kendi</span></td></tr>
        <tr><td>Sicil düzenleme</td><td><span class="ok">✓</span></td><td><span class="no">✗</span></td><td><span class="no">✗</span></td></tr>
        <tr><td>İzin onaylama</td><td><span class="ok">✓</span></td><td><span class="par">kendi dep.</span></td><td><span class="no">✗</span></td></tr>
        <tr><td>Raporlar</td><td><span class="ok">✓</span></td><td><span class="par">kendi dep.</span></td><td><span class="no">✗</span></td></tr>
      </tbody>
    </table>
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

var ROLLER=['Personel','Şef','İK / Yönetici'];
var DEFAULT_DEPS=['Servis','Mutfak','Housekeeping','Güvenlik','Önbüro','Muhasebe','Teknik','Animasyon'];
var employees=[], allDeps=DEFAULT_DEPS, changes={};

function ini(s){var p=(s||'').trim().split(' ');return ((p[0]||'')[0]||'')+((p[1]||'')[0]||'');}
function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('show');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('show');},2500);}

async function loadData(){
  try{
    employees=await req('/employees');
    var settings=await req('/settings').catch(function(){return {};});
    if(settings.departments&&settings.departments.length) allDeps=settings.departments;
    render();
  }catch(e){
    document.getElementById('rol-body').innerHTML='<tr><td colspan="4" class="empty">Veri alınamadı: '+e.message+'</td></tr>';
  }
}

function getRolClass(rol){
  if(rol==='İK / Yönetici')return 'p-ik';
  if(rol==='Şef')return 'p-sef';
  return 'p-per';
}

function render(){
  var active=employees.filter(function(e){return e.status==='aktif';});
  if(!active.length){
    document.getElementById('rol-body').innerHTML='<tr><td colspan="4" class="empty">Aktif personel yok.</td></tr>';
    return;
  }
  var rows=active.map(function(e){
    var rol=changes[e.tc]?changes[e.tc].rol:(e.rol||'Personel');
    var rolDeps=changes[e.tc]?changes[e.tc].deps:(e.rol_departmanlar?JSON.parse(e.rol_departmanlar):[]);
    var depsHtml=allDeps.map(function(d){
      var on=rolDeps.indexOf(d)>=0;
      return '<span class="dep-tag'+(on?' on':'')+'" data-dep="'+d+'" data-tc="'+e.tc+'">'+d+'</span>';
    }).join('');
    var showDeps=(rol==='Şef');
    return '<tr data-tc="'+e.tc+'">'
      +'<td><div class="who"><div class="av">'+ini(e.ad)+'</div><div><b>'+e.ad+'</b><small>'+e.dep+' · #'+e.sicil+'</small></div></div></td>'
      +'<td>'+e.dep+'</td>'
      +'<td><select class="rol-select" data-tc="'+e.tc+'">'
      +ROLLER.map(function(r){return '<option value="'+r+'"'+(r===rol?' selected':'')+'>'+r+'</option>';}).join('')
      +'</select></td>'
      +'<td><div class="dep-tags" id="deps-'+e.tc+'" style="'+(showDeps?'':'display:none')+'">'+depsHtml+'</div>'
      +(showDeps?'':'<span style="color:var(--muted);font-size:12px">—</span>')
      +'</td>'
      +'</tr>';
  }).join('');
  document.getElementById('rol-body').innerHTML=rows;

  // Events
  document.querySelectorAll('.rol-select').forEach(function(sel){
    sel.addEventListener('change',function(){
      var tc=sel.dataset.tc;
      if(!changes[tc])changes[tc]={deps:[]};
      changes[tc].rol=sel.value;
      // deps goster/gizle
      var depsDiv=document.getElementById('deps-'+tc);
      var nextTd=depsDiv?depsDiv.parentElement:null;
      if(depsDiv){
        depsDiv.style.display=sel.value==='Şef'?'flex':'none';
        if(nextTd){
          var noText=nextTd.querySelector('span');
          if(noText)noText.style.display=sel.value==='Şef'?'none':'inline';
        }
      }
    });
  });

  document.querySelectorAll('.dep-tag').forEach(function(tag){
    tag.addEventListener('click',function(){
      var tc=tag.dataset.tc, dep=tag.dataset.dep;
      if(!changes[tc])changes[tc]={rol:null,deps:[]};
      var idx=changes[tc].deps.indexOf(dep);
      if(idx>=0)changes[tc].deps.splice(idx,1);
      else changes[tc].deps.push(dep);
      tag.classList.toggle('on');
    });
  });
}

document.getElementById('save-all').addEventListener('click',async function(){
  var btn=this; btn.disabled=true; btn.textContent='Kaydediliyor…';
  var tcs=Object.keys(changes);
  if(!tcs.length){toast('Değişiklik yok');btn.disabled=false;btn.textContent='Tümünü Kaydet';return;}
  var ok=0,err=0;
  for(var i=0;i<tcs.length;i++){
    var tc=tcs[i]; var ch=changes[tc];
    var emp=employees.find(function(e){return e.tc===tc;});
    var rol=ch.rol||(emp?emp.rol:'Personel')||'Personel';
    var deps=ch.deps||(emp&&emp.rol_departmanlar?JSON.parse(emp.rol_departmanlar):[]);
    try{
      await req('/employees/'+tc+'/rol',{method:'PUT',body:{rol:rol,rolDepartmanlar:deps}});
      ok++;
    }catch(e){err++;console.log('hata:',tc,e.message);}
  }
  changes={};
  toast(ok+' rol güncellendi'+(err?' · '+err+' hata':''));
  btn.disabled=false; btn.textContent='Tümünü Kaydet';
  loadData();
});

loadData();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-roller">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_ROLLER + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
