NEW_AYARLAR = '''<template id="tpl-ayarlar">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ayarlar</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--text:#EAF2F5;--muted:#8FA6B0;--radius:16px;--shadow:0 24px 60px rgba(0,0,0,.45)}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%) fixed;color:var(--text);font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:900px;margin:0 auto;padding:22px 16px 70px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);overflow:hidden;margin-bottom:18px}
.ch{display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--line)}
.ch h3{font-family:'Space Grotesk';font-weight:700;font-size:16px;margin:0}
.ch p{color:var(--muted);font-size:12.5px;margin:4px 0 0}
.body{padding:18px 20px}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px;min-height:36px}
.tag{display:inline-flex;align-items:center;gap:7px;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;padding:6px 12px;font-size:13px}
.tag .del{background:none;border:0;color:var(--muted);cursor:pointer;font-size:15px;padding:0;line-height:1}
.tag .del:hover{color:var(--danger)}
.add-row{display:flex;gap:8px}
.add-row input{flex:1;background:var(--ink);border:1px solid var(--line);color:var(--text);border-radius:9px;padding:9px 12px;font-size:13px;font-family:inherit}
.add-row input:focus{outline:none;border-color:var(--amber)}
.add-btn{background:var(--amber);color:#1a1205;border:0;border-radius:9px;padding:9px 16px;font-weight:700;font-size:13px;cursor:pointer;white-space:nowrap}
.save-btn{background:var(--amber);color:#1a1205;border:0;border-radius:10px;padding:10px 20px;font-weight:700;font-size:13.5px;cursor:pointer}
.toast{position:fixed;bottom:26px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:13px 20px;border-radius:12px;font-size:13.5px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.hint{color:var(--muted);font-size:12px;margin-top:6px;line-height:1.5}
</style>
<div class="wrap">
  <div class="card">
    <div class="ch"><div><h3>Departmanlar</h3><p>Sicil ve Roller modüllerine yansır</p></div></div>
    <div class="body">
      <div class="tags" id="dep-tags"></div>
      <div class="add-row">
        <input id="dep-input" placeholder="Yeni departman adı…" maxlength="50">
        <button class="add-btn" id="dep-add">+ Ekle</button>
      </div>
    </div>
  </div>
  <div class="card">
    <div class="ch"><div><h3>Görevler</h3><p>Sicil modülündeki görev listesine yansır</p></div></div>
    <div class="body">
      <div class="tags" id="gorev-tags"></div>
      <div class="add-row">
        <input id="gorev-input" placeholder="Yeni görev adı…" maxlength="50">
        <button class="add-btn" id="gorev-add">+ Ekle</button>
      </div>
    </div>
  </div>
  <div style="text-align:right">
    <button class="save-btn" id="save-btn">Değişiklikleri Kaydet</button>
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

var DEFAULT_DEPS=['Servis','Mutfak','Housekeeping','Güvenlik','Önbüro','Muhasebe','Teknik','Animasyon'];
var DEFAULT_GOREVS=['Müdür','Şef','Garson','Aşçı','Resepsiyonist','Güvenlik Görevlisi','Temizlik','Teknisyen','Animatör','Personel'];
var deps=[], gorevs=[];

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('show');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('show');},2500);}

function renderTags(list, containerId, onDelete){
  var box=document.getElementById(containerId);
  if(!list.length){box.innerHTML='<span style="color:var(--muted);font-size:12.5px;padding:6px 0">Henüz eklenmedi</span>';return;}
  box.innerHTML=list.map(function(d,i){
    return '<span class="tag">'+d+'<button class="del" data-i="'+i+'">×</button></span>';
  }).join('');
  box.querySelectorAll('.del').forEach(function(b){
    b.addEventListener('click',function(){onDelete(+b.dataset.i);});
  });
}

function renderDeps(){renderTags(deps,'dep-tags',function(i){deps.splice(i,1);renderDeps();});}
function renderGorevs(){renderTags(gorevs,'gorev-tags',function(i){gorevs.splice(i,1);renderGorevs();});}

async function loadSettings(){
  try{
    var s=await req('/settings');
    deps=(s.departments&&s.departments.length)?s.departments:DEFAULT_DEPS.slice();
    gorevs=(s.positions&&s.positions.length)?s.positions:DEFAULT_GOREVS.slice();
  }catch(e){
    deps=DEFAULT_DEPS.slice();
    gorevs=DEFAULT_GOREVS.slice();
  }
  renderDeps(); renderGorevs();
}

document.getElementById('dep-add').addEventListener('click',function(){
  var v=document.getElementById('dep-input').value.trim();
  if(!v)return;
  if(deps.indexOf(v)>=0){toast('Zaten var');return;}
  deps.push(v); document.getElementById('dep-input').value=''; renderDeps();
});
document.getElementById('dep-input').addEventListener('keydown',function(e){if(e.key==='Enter')document.getElementById('dep-add').click();});

document.getElementById('gorev-add').addEventListener('click',function(){
  var v=document.getElementById('gorev-input').value.trim();
  if(!v)return;
  if(gorevs.indexOf(v)>=0){toast('Zaten var');return;}
  gorevs.push(v); document.getElementById('gorev-input').value=''; renderGorevs();
});
document.getElementById('gorev-input').addEventListener('keydown',function(e){if(e.key==='Enter')document.getElementById('gorev-add').click();});

document.getElementById('save-btn').addEventListener('click',async function(){
  var btn=this; btn.textContent='Kaydediliyor…'; btn.disabled=true;
  try{
    await req('/settings',{method:'PUT',body:{departments:deps,positions:gorevs}});
    toast('Ayarlar kaydedildi — Sicil ve Roller modülleri güncellendi');
  }catch(e){toast('Hata: '+e.message);}
  btn.textContent='Değişiklikleri Kaydet'; btn.disabled=false;
});

loadSettings();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-ayarlar">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_AYARLAR + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
