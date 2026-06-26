# 1) Backend - hotel_users endpoint'lerini hotel rolune ac
s = open('server.js', encoding='utf-8').read()

old1 = """app.get('/api/hotel-users', auth(['operator']), (req, res) => {
  res.json(D.db.prepare('SELECT username, tenant_id, name FROM hotel_users ORDER BY tenant_id').all());
});"""

new1 = """app.get('/api/hotel-users', auth(['operator','hotel']), (req, res) => {
  if(req.session.role==='hotel'){
    return res.json(D.db.prepare('SELECT username, tenant_id, name FROM hotel_users WHERE tenant_id=? ORDER BY username').all(req.session.tenant));
  }
  res.json(D.db.prepare('SELECT username, tenant_id, name FROM hotel_users ORDER BY tenant_id').all());
});"""

old2 = """app.post('/api/hotel-users', auth(['operator']), (req, res) => {"""
new2 = """app.post('/api/hotel-users', auth(['operator','hotel']), (req, res) => {"""

old3 = """app.delete('/api/hotel-users/:username', auth(['operator']), (req, res) => {
  D.db.prepare('DELETE FROM hotel_users WHERE username=?').run(req.params.username);"""
new3 = """app.delete('/api/hotel-users/:username', auth(['operator','hotel']), (req, res) => {
  if(req.session.role==='hotel'){
    D.db.prepare('DELETE FROM hotel_users WHERE username=? AND tenant_id=?').run(req.params.username, req.session.tenant);
    return res.json({ok:true});
  }
  D.db.prepare('DELETE FROM hotel_users WHERE username=?').run(req.params.username);"""

print('get:', old1 in s)
print('post:', old2 in s)
print('del:', old3 in s)
s = s.replace(old1, new1).replace(old2, new2).replace(old3, new3)
open('server.js', 'w', encoding='utf-8').write(s)
print('server.js OK')

# 2) Frontend - Kullanici Yonetimi modulu ekle
NEW_KULLANICI = r'''<template id="tpl-kullanici">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kullanici Yonetimi</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--text:#EAF2F5;--muted:#8FA6B0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;padding:18px 16px 60px}
.topbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:16px}
.topbar h1{font-family:'Space Grotesk';font-size:18px;font-weight:700;margin:0;flex:1}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;margin-bottom:14px}
.btn{padding:7px 13px;border-radius:8px;border:0;font-weight:600;font-size:12px;cursor:pointer;font-family:inherit}
.btn-amber{background:var(--amber);color:#1a1205}
.btn-ghost{background:var(--panel-2);border:1px solid var(--line);color:var(--text)}
.btn-ghost:hover{border-color:var(--amber);color:var(--amber)}
.btn-danger{background:rgba(255,107,107,.15);color:var(--danger);border:1px solid rgba(255,107,107,.3);border-radius:7px;padding:5px 10px;cursor:pointer;font-size:11.5px;font-weight:600}
table{width:100%;border-collapse:collapse;font-size:12.5px}
thead th{text-align:left;font-size:11px;color:var(--muted);font-weight:600;padding:10px 14px;border-bottom:1px solid var(--line);text-transform:uppercase}
tbody td{padding:10px 14px;border-bottom:1px solid rgba(35,65,79,.35);vertical-align:middle}
tbody tr:hover td{background:rgba(27,49,62,.4)}
.who{display:flex;align-items:center;gap:9px}
.av{width:30px;height:30px;border-radius:8px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:11px;color:#1a1205;background:var(--amber)}
.pill{display:inline-flex;align-items:center;font-size:11px;font-weight:600;padding:3px 8px;border-radius:6px}
.p-ok{background:rgba(52,217,160,.15);color:var(--mint)}
.empty{text-align:center;color:var(--muted);padding:40px;font-size:13px}
.ov{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:80;display:none}
.modal{position:fixed;inset:0;z-index:81;display:none;align-items:center;justify-content:center}
.modal.open{display:flex}
.mbox{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:24px;width:400px;max-width:94vw}
.mbox h3{font-family:'Space Grotesk';font-size:15px;margin:0 0 16px}
.field{margin-bottom:12px}
.field label{display:block;font-size:11px;color:var(--muted);margin-bottom:4px;font-weight:600;text-transform:uppercase}
.field input,.field select{width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;padding:9px 12px;color:var(--text);font-family:inherit;font-size:13px;outline:none}
.field input:focus,.field select:focus{border-color:var(--amber)}
.mbtns{display:flex;gap:8px;justify-content:flex-end;margin-top:16px}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:11px 18px;border-radius:10px;font-size:12.5px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
</style>

<div class="topbar">
  <h1>Kullanıcı Yönetimi</h1>
  <button class="btn btn-amber" id="add-btn">+ Yeni Kullanıcı</button>
</div>

<div class="card">
  <table>
    <thead><tr><th>Kullanıcı Adı</th><th>Ad Soyad</th><th>Yetki</th><th></th></tr></thead>
    <tbody id="user-body"><tr><td colspan="4" class="empty">Yukleniyor...</td></tr></tbody>
  </table>
</div>

<div class="ov" id="ov"></div>
<div class="modal" id="add-modal">
  <div class="mbox">
    <h3>Yeni Kullanıcı Ekle</h3>
    <div class="field"><label>Ad Soyad</label><input id="add-name" placeholder="Ad Soyad"></div>
    <div class="field"><label>Kullanıcı Adı</label><input id="add-user" placeholder="kullanici.adi"></div>
    <div class="field"><label>Şifre</label><input id="add-pass" type="password" placeholder="Şifre"></div>
    <div class="field"><label>Yetki</label>
      <select id="add-rol">
        <option value="ik">İK / Yönetici (Tam Yetki)</option>
        <option value="muhasebe">Muhasebe (Sadece Görüntüle)</option>
        <option value="departman">Departman Müdürü</option>
      </select>
    </div>
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
  var r=await fetch('https://gecitpdks.duckdns.org/api'+path,{method:opts.method||'GET',headers:h,body:opts.body?JSON.stringify(opts.body):undefined});
  var d=null;try{d=await r.json();}catch(e){}
  if(!r.ok)throw new Error((d&&d.error)||('Hata '+r.status));
  return d;
}

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('on');},2500);}
function ini(s){var p=(s||'').trim().split(' ');return((p[0]||'')[0]||'')+((p[1]||'')[0]||'');}
var ROL_LABEL={ik:'IK / Yonetici',muhasebe:'Muhasebe',departman:'Departman Mudurlugu'};

async function load(){
  try{
    var data=await req('/hotel-users');
    if(!data.length){
      document.getElementById('user-body').innerHTML='<tr><td colspan="4" class="empty">Henuz kullanici yok</td></tr>';
      return;
    }
    document.getElementById('user-body').innerHTML=data.map(function(u){
      return '<tr>'
        +'<td><div class="who"><div class="av">'+ini(u.name||u.username)+'</div><b>'+u.username+'</b></div></td>'
        +'<td>'+(u.name||'-')+'</td>'
        +'<td><span class="pill p-ok">'+(ROL_LABEL[u.rol]||'IK / Yonetici')+'</span></td>'
        +'<td style="text-align:right"><button class="btn-danger" data-u="'+u.username+'">Sil</button></td>'
        +'</tr>';
    }).join('');
    document.querySelectorAll('.btn-danger').forEach(function(btn){
      btn.addEventListener('click',async function(){
        if(!confirm(btn.dataset.u+' kullanicisini silmek istediginizden emin misiniz?'))return;
        try{
          await req('/hotel-users/'+btn.dataset.u,{method:'DELETE'});
          toast('Silindi');load();
        }catch(e){toast('Hata: '+e.message);}
      });
    });
  }catch(e){
    document.getElementById('user-body').innerHTML='<tr><td colspan="4" class="empty">Hata: '+e.message+'</td></tr>';
  }
}

document.getElementById('add-btn').addEventListener('click',function(){
  document.getElementById('add-name').value='';
  document.getElementById('add-user').value='';
  document.getElementById('add-pass').value='';
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
  var g=getG(); var tenant=(g&&g._tenant)||'1';
  var name=document.getElementById('add-name').value.trim();
  var user=document.getElementById('add-user').value.trim();
  var pass=document.getElementById('add-pass').value;
  var rol=document.getElementById('add-rol').value;
  if(!name||!user||!pass){toast('Tum alanlari doldurun');return;}
  try{
    await req('/hotel-users',{method:'POST',body:{username:user,password:pass,tenant_id:tenant,name:name,rol:rol}});
    toast('Kullanici eklendi');closeModal();load();
  }catch(e){toast('Hata: '+e.message);}
});

load();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    # Menuye ekle - Ayarlar'in ustune
    old_nav = """      <div class="navitem" data-v="ayarlar" data-frame="tpl-ayarlar"><span class="i">⚙</span> Ayarlar</div>"""
    new_nav = """      <div class="navitem" data-v="kullanici" data-frame="tpl-kullanici"><span class="i">👤</span> Kullanıcılar</div>
      <div class="navitem" data-v="ayarlar" data-frame="tpl-ayarlar"><span class="i">⚙</span> Ayarlar</div>"""
    found_nav = old_nav in s
    s = s.replace(old_nav, new_nav)
    
    # Template ekle
    old_tpl = '<template id="tpl-ayarlar">'
    found_tpl = old_tpl in s
    s = s.replace(old_tpl, NEW_KULLANICI + '\n<template id="tpl-ayarlar">', 1)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> nav:', found_nav, '| tpl:', found_tpl)
