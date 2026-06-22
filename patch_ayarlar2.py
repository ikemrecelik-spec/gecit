NEW_AYARLAR = '''<template id="tpl-ayarlar">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ayarlar & Tanımlar</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--text:#EAF2F5;--muted:#8FA6B0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;padding:22px 24px 60px}
h1{font-family:'Space Grotesk';font-size:20px;font-weight:700;margin:0 0 4px}
.sub{color:var(--muted);font-size:13px;margin-bottom:24px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px}
.section{background:var(--panel);border:1px solid var(--line);border-radius:15px;padding:20px 22px}
.section h2{font-family:'Space Grotesk';font-size:15px;font-weight:700;margin:0 0 14px;display:flex;align-items:center;gap:8px}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px;min-height:32px}
.tag{display:inline-flex;align-items:center;gap:6px;padding:5px 11px;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;font-size:13px}
.tag button{background:none;border:0;color:var(--danger);cursor:pointer;font-size:15px;padding:0;line-height:1}
.add-row{display:flex;gap:8px}
.add-row input{flex:1;background:var(--panel-2);border:1px solid var(--line);border-radius:9px;padding:9px 12px;color:var(--text);font-family:inherit;font-size:13.5px;outline:none}
.add-row input:focus{border-color:var(--amber)}
.btn{padding:9px 14px;border-radius:9px;border:0;font-weight:600;font-size:13px;cursor:pointer;font-family:inherit}
.btn-amber{background:var(--amber);color:#1a1205}
.save-btn{width:100%;margin-top:14px;padding:12px;border-radius:11px;border:0;background:var(--amber);color:#1a1205;font-weight:700;font-size:14px;cursor:pointer;font-family:inherit}
.save-btn:disabled{opacity:.5;cursor:default}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(16px);background:#0b1820;border:1px solid var(--line);color:var(--text);padding:11px 16px;border-radius:11px;font-size:12.5px;opacity:0;transition:.25s;z-index:50;text-align:center}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
.field{margin-bottom:12px}
label{display:block;font-size:12px;color:var(--muted);margin-bottom:5px;font-weight:500}
input.fin,select.fin{width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:9px;padding:10px 12px;color:var(--text);font-family:inherit;font-size:13.5px;outline:none}
input.fin:focus,select.fin:focus{border-color:var(--amber)}
</style>

<h1>Ayarlar & Tanımlar</h1>
<p class="sub">Bölümler, görevler ve çalışma kuralları — değişiklikler kaydedilince Sicil modülüne yansır</p>

<div class="grid">
  <div class="section">
    <h2>Bölümler</h2>
    <div class="tags" id="dep-tags"></div>
    <div class="add-row"><input id="dep-new" placeholder="Yeni bölüm adı…"><button class="btn btn-amber" id="dep-add">Ekle</button></div>
    <button class="save-btn" id="save-deps">Bölümleri Kaydet</button>
  </div>
  <div class="section">
    <h2>Görevler</h2>
    <div class="tags" id="gorev-tags"></div>
    <div class="add-row"><input id="gorev-new" placeholder="Yeni görev adı…"><button class="btn btn-amber" id="gorev-add">Ekle</button></div>
    <button class="save-btn" id="save-gorevler">Görevleri Kaydet</button>
  </div>
  <div class="section">
    <h2>Çalışma Kuralları</h2>
    <div class="field"><label>Günlük minimum çalışma süresi (saat)</label><input class="fin" id="rule-min" type="number" value="7.5" step="0.5"></div>
    <div class="field"><label>Giriş tolerans başlangıcı</label><input class="fin" id="rule-tol-start" type="time" value="06:30"></div>
    <div class="field"><label>Giriş tolerans bitişi</label><input class="fin" id="rule-tol-end" type="time" value="08:15"></div>
    <div class="field"><label>Yıllık FM tavanı (saat)</label><input class="fin" id="rule-fm-max" type="number" value="270"></div>
    <button class="save-btn" id="save-rules">Kuralları Kaydet</button>
  </div>
  <div class="section">
    <h2>Vardiya Tanımları</h2>
    <div class="tags" id="shift-tags"></div>
    <div class="add-row"><input id="shift-new" placeholder="ör: A · 08:00–16:00"><button class="btn btn-amber" id="shift-add">Ekle</button></div>
    <button class="save-btn" id="save-shifts">Vardiyaları Kaydet</button>
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

var DEFAULT_DEPS=['Önbüro','Yiyecek & İçecek','Mutfak','Kat Hizmetleri','Teknik','Güvenlik','İnsan Kaynakları','Muhasebe','Satış & Pazarlama','Havuz & Plaj','Spa & Wellness','Animasyon','Bahçe','Servis','Depo & Lojistik'];
var DEFAULT_GOREVS=['Müdür','Müdür Yardımcısı','Şef','Usta','Personel','Stajyer','Teknisyen','Güvenlik Görevlisi','Resepsiyon','Kasiyer','Garson','Aşçı','Temizlik Görevlisi','Animatör','Bahçıvan','Şoför'];
var DEFAULT_SHIFTS=['A · 08:00–16:00','Ara · 12:00–20:00','B · 16:00–24:00','Gece · 24:00–08:00'];

var deps=[], gorevs=[], shifts=[], rules={};

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('on');},2400);}

function renderTags(arr,containerId,removeArr){
  var box=document.getElementById(containerId);
  if(!arr.length){box.innerHTML='<span style="color:var(--muted);font-size:12px">Henüz eklenmedi</span>';return;}
  box.innerHTML=arr.map(function(item,i){
    return '<span class="tag">'+item+'<button data-i="'+i+'" data-arr="'+removeArr+'">×</button></span>';
  }).join('');
  box.querySelectorAll('button').forEach(function(b){
    b.addEventListener('click',function(){
      var arr=(b.dataset.arr==='deps')?deps:(b.dataset.arr==='gorevs'?gorevs:shifts);
      arr.splice(+b.dataset.i,1);
      renderTags(deps,'dep-tags','deps');
      renderTags(gorevs,'gorev-tags','gorevs');
      renderTags(shifts,'shift-tags','shifts');
    });
  });
}

async function loadSettings(){
  try{
    var s=await req('/settings');
    deps=(s.departments&&s.departments.length)?s.departments:DEFAULT_DEPS.slice();
    gorevs=(s.positions&&s.positions.length)?s.positions:DEFAULT_GOREVS.slice();
    shifts=(s.shifts&&s.shifts.length)?s.shifts:DEFAULT_SHIFTS.slice();
    if(s.rules){
      document.getElementById('rule-min').value=s.rules.minHours||7.5;
      document.getElementById('rule-tol-start').value=s.rules.tolStart||'06:30';
      document.getElementById('rule-tol-end').value=s.rules.tolEnd||'08:15';
      document.getElementById('rule-fm-max').value=s.rules.fmMax||270;
    }
  }catch(e){
    deps=DEFAULT_DEPS.slice(); gorevs=DEFAULT_GOREVS.slice(); shifts=DEFAULT_SHIFTS.slice();
  }
  renderTags(deps,'dep-tags','deps');
  renderTags(gorevs,'gorev-tags','gorevs');
  renderTags(shifts,'shift-tags','shifts');
}

async function saveAll(what){
  var btn=document.getElementById('save-'+what); btn.disabled=true; btn.textContent='Kaydediliyor…';
  var rules_={
    minHours:+document.getElementById('rule-min').value,
    tolStart:document.getElementById('rule-tol-start').value,
    tolEnd:document.getElementById('rule-tol-end').value,
    fmMax:+document.getElementById('rule-fm-max').value
  };
  try{
    await req('/settings',{method:'PUT',body:{departments:deps,positions:gorevs,shifts:shifts,rules:rules_}});
    toast('Kaydedildi ✓ — Sicil ve Roller modülleri güncellendi');
  }catch(e){toast('Hata: '+e.message);}
  btn.disabled=false;
  var labels={deps:'Bölümleri Kaydet',gorevler:'Görevleri Kaydet',rules:'Kuralları Kaydet',shifts:'Vardiyaları Kaydet'};
  btn.textContent=labels[what]||'Kaydet';
}

// Ekle butonları
document.getElementById('dep-add').addEventListener('click',function(){var v=document.getElementById('dep-new').value.trim();if(!v)return;if(deps.indexOf(v)<0)deps.push(v);document.getElementById('dep-new').value='';renderTags(deps,'dep-tags','deps');});
document.getElementById('gorev-add').addEventListener('click',function(){var v=document.getElementById('gorev-new').value.trim();if(!v)return;if(gorevs.indexOf(v)<0)gorevs.push(v);document.getElementById('gorev-new').value='';renderTags(gorevs,'gorev-tags','gorevs');});
document.getElementById('shift-add').addEventListener('click',function(){var v=document.getElementById('shift-new').value.trim();if(!v)return;if(shifts.indexOf(v)<0)shifts.push(v);document.getElementById('shift-new').value='';renderTags(shifts,'shift-tags','shifts');});

// Enter ile ekle
document.getElementById('dep-new').addEventListener('keydown',function(e){if(e.key==='Enter')document.getElementById('dep-add').click();});
document.getElementById('gorev-new').addEventListener('keydown',function(e){if(e.key==='Enter')document.getElementById('gorev-add').click();});
document.getElementById('shift-new').addEventListener('keydown',function(e){if(e.key==='Enter')document.getElementById('shift-add').click();});

// Kaydet butonları
document.getElementById('save-deps').addEventListener('click',function(){saveAll('deps');});
document.getElementById('save-gorevler').addEventListener('click',function(){saveAll('gorevler');});
document.getElementById('save-rules').addEventListener('click',function(){saveAll('rules');});
document.getElementById('save-shifts').addEventListener('click',function(){saveAll('shifts');});

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
