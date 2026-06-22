NEW_AYARLAR = '''<template id="tpl-ayarlar">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ayarlar & Tanımlar</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--text:#EAF2F5;--muted:#8FA6B0;--radius:14px}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh}
.shell{display:grid;grid-template-columns:230px 1fr;min-height:100vh}
.side{background:var(--panel);border-right:1px solid var(--line);padding:24px 14px;display:flex;flex-direction:column;gap:4px}
.side h3{font-family:'Space Grotesk';font-size:14px;font-weight:700;margin:0 0 14px;padding:0 8px;color:var(--muted);letter-spacing:.5px;text-transform:uppercase}
.menu-item{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:9px;cursor:pointer;color:var(--muted);font-size:13.5px;font-weight:500;transition:.15s}
.menu-item:hover{background:var(--panel-2);color:var(--text)}
.menu-item.active{background:var(--amber);color:#1a1205;font-weight:700}
.menu-item .ic{font-size:15px;width:18px;text-align:center}
.main{padding:30px 36px 60px;overflow-y:auto;max-height:100vh}
.section{display:none}
.section.active{display:block;animation:fadein .3s}
@keyframes fadein{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.section h1{font-family:'Space Grotesk';font-size:22px;font-weight:700;margin:0 0 6px}
.section .sub{color:var(--muted);font-size:13.5px;margin-bottom:24px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:22px 24px;margin-bottom:18px}
.card h2{font-family:'Space Grotesk';font-size:15px;font-weight:700;margin:0 0 14px;display:flex;align-items:center;gap:8px}
.card p.hint{color:var(--muted);font-size:12.5px;margin:-8px 0 14px;line-height:1.5}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px;min-height:32px}
.tag{display:inline-flex;align-items:center;gap:7px;padding:6px 12px;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;font-size:13px}
.tag button{background:none;border:0;color:var(--danger);cursor:pointer;font-size:15px;padding:0;line-height:1}
.add-row{display:flex;gap:8px}
.add-row input{flex:1;background:var(--panel-2);border:1px solid var(--line);border-radius:9px;padding:9px 12px;color:var(--text);font-family:inherit;font-size:13.5px;outline:none}
.add-row input:focus{border-color:var(--amber)}
.btn{padding:9px 16px;border-radius:9px;border:0;font-weight:600;font-size:13px;cursor:pointer;font-family:inherit}
.btn-amber{background:var(--amber);color:#1a1205}
.btn-ghost{background:var(--panel-2);border:1px solid var(--line);color:var(--text)}
.save-bar{position:sticky;bottom:0;background:linear-gradient(0deg,var(--ink),transparent 100%);padding:16px 0 6px;margin-top:16px;display:flex;gap:10px;align-items:center;justify-content:flex-end;z-index:5}
.save-status{color:var(--muted);font-size:12px;margin-right:auto}
.save-status.changed{color:var(--amber)}
.save-btn{padding:11px 22px;border-radius:10px;border:0;background:var(--amber);color:#1a1205;font-weight:700;font-size:13.5px;cursor:pointer;font-family:inherit}
.save-btn:disabled{opacity:.5;cursor:default}
.field{margin-bottom:14px}
.field label{display:block;font-size:12px;color:var(--muted);margin-bottom:6px;font-weight:500}
.field input,.field select,.field textarea{width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:9px;padding:10px 12px;color:var(--text);font-family:inherit;font-size:13.5px;outline:none}
.field input:focus,.field select:focus,.field textarea:focus{border-color:var(--amber)}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.field small{color:var(--muted);font-size:11px;margin-top:4px;display:block}
.switch{display:flex;align-items:center;gap:12px;padding:12px 14px;background:var(--panel-2);border:1px solid var(--line);border-radius:10px;margin-bottom:10px}
.switch b{font-size:13px;font-weight:600}
.switch small{color:var(--muted);font-size:12px;display:block;margin-top:2px}
.switch .info{flex:1}
.toggle{position:relative;width:44px;height:24px;background:var(--line);border-radius:12px;cursor:pointer;transition:.2s;flex:0 0 auto}
.toggle.on{background:var(--mint)}
.toggle:after{content:'';position:absolute;top:2px;left:2px;width:20px;height:20px;background:#fff;border-radius:50%;transition:.2s}
.toggle.on:after{left:22px}
table{width:100%;border-collapse:collapse}
table th{text-align:left;font-size:11px;color:var(--muted);font-weight:600;padding:10px 12px;border-bottom:1px solid var(--line);text-transform:uppercase;letter-spacing:.3px}
table td{padding:10px 12px;border-bottom:1px solid rgba(35,65,79,.5);font-size:13px}
table .del-btn{background:none;border:0;color:var(--danger);cursor:pointer;font-size:14px}
.toast{position:fixed;left:50%;bottom:30px;transform:translateX(-50%) translateY(20px);background:var(--panel-2);border:1px solid var(--line);color:var(--text);padding:12px 20px;border-radius:11px;font-size:13.5px;font-weight:600;opacity:0;transition:.3s;z-index:90}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
.kvkk-section{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:900px){.shell{grid-template-columns:1fr}.side{position:sticky;top:0;z-index:9;flex-direction:row;flex-wrap:wrap;border-right:0;border-bottom:1px solid var(--line)}.kvkk-section,.field-row{grid-template-columns:1fr}}
</style>

<div class="shell">
  <aside class="side">
    <h3>Ayarlar</h3>
    <div class="menu-item active" data-s="general"><span class="ic">⚙</span> Genel</div>
    <div class="menu-item" data-s="dep-gorev"><span class="ic">🏢</span> Bölüm & Görev</div>
    <div class="menu-item" data-s="shifts"><span class="ic">🕐</span> Vardiyalar</div>
    <div class="menu-item" data-s="rules"><span class="ic">📋</span> Çalışma Kuralları</div>
    <div class="menu-item" data-s="leaves"><span class="ic">🌴</span> İzin Türleri</div>
    <div class="menu-item" data-s="holidays"><span class="ic">🎉</span> Tatil Günleri</div>
    <div class="menu-item" data-s="kvkk"><span class="ic">🔒</span> KVKK & Gizlilik</div>
    <div class="menu-item" data-s="system"><span class="ic">💾</span> Sistem</div>
  </aside>

  <main class="main">
    <!-- GENEL -->
    <section class="section active" id="sec-general">
      <h1>Genel</h1><p class="sub">İşletme bilgileri ve temel ayarlar</p>
      <div class="card">
        <h2>İşletme Bilgileri</h2>
        <div class="field"><label>İşletme adı</label><input id="g-name" placeholder="Side Prenses Resort"></div>
        <div class="field-row">
          <div class="field"><label>Şehir</label><input id="g-city" placeholder="Antalya"></div>
          <div class="field"><label>İlçe</label><input id="g-district" placeholder="Side"></div>
        </div>
        <div class="field"><label>Telefon</label><input id="g-phone" placeholder="+90 ..."></div>
        <div class="field"><label>Adres</label><textarea id="g-address" rows="2" placeholder="Açık adres"></textarea></div>
      </div>
    </section>

    <!-- BÖLÜM & GÖREV -->
    <section class="section" id="sec-dep-gorev">
      <h1>Bölüm & Görev</h1><p class="sub">Sicil & Roller modüllerine yansır</p>
      <div class="card">
        <h2>Bölümler</h2>
        <p class="hint">Sicil ekleme/düzenlemede kullanılır. Roller modülünde Şef'in yetkili olduğu departmanlar buradan seçilir.</p>
        <div class="tags" id="dep-tags"></div>
        <div class="add-row"><input id="dep-new" placeholder="Yeni bölüm adı (ör. Resepsiyon)"><button class="btn btn-amber" id="dep-add">+ Ekle</button></div>
      </div>
      <div class="card">
        <h2>Görevler</h2>
        <p class="hint">Sicil ekleme/düzenlemede kullanılır.</p>
        <div class="tags" id="gorev-tags"></div>
        <div class="add-row"><input id="gorev-new" placeholder="Yeni görev adı (ör. Garson)"><button class="btn btn-amber" id="gorev-add">+ Ekle</button></div>
      </div>
    </section>

    <!-- VARDİYALAR -->
    <section class="section" id="sec-shifts">
      <h1>Vardiyalar</h1><p class="sub">Vardiya tanımları ve giriş tolerans aralıkları</p>
      <div class="card">
        <h2>Vardiya Listesi</h2>
        <p class="hint">Mobil uygulama giriş yapıldığında saatine göre otomatik vardiya atanır.</p>
        <table>
          <thead><tr><th>Kod</th><th>Adı</th><th>Başlangıç</th><th>Bitiş</th><th>Tolerans</th><th></th></tr></thead>
          <tbody id="shift-body"></tbody>
        </table>
        <div style="margin-top:14px;display:grid;grid-template-columns:80px 1fr 100px 100px 130px auto;gap:8px;align-items:end">
          <div class="field" style="margin:0"><label>Kod</label><input id="sh-code" placeholder="A" maxlength="5"></div>
          <div class="field" style="margin:0"><label>Adı</label><input id="sh-name" placeholder="Sabah vardiyası"></div>
          <div class="field" style="margin:0"><label>Başlangıç</label><input id="sh-start" type="time" value="08:00"></div>
          <div class="field" style="margin:0"><label>Bitiş</label><input id="sh-end" type="time" value="16:00"></div>
          <div class="field" style="margin:0"><label>Tolerans (dk)</label><input id="sh-tol" type="number" value="15" min="0"></div>
          <button class="btn btn-amber" id="sh-add">+ Ekle</button>
        </div>
      </div>
    </section>

    <!-- ÇALIŞMA KURALLARI -->
    <section class="section" id="sec-rules">
      <h1>Çalışma Kuralları</h1><p class="sub">Mesai ve puantaj hesaplama kuralları</p>
      <div class="card">
        <h2>Günlük & Haftalık</h2>
        <div class="field-row">
          <div class="field"><label>Günlük minimum çalışma süresi (saat)</label><input id="r-min" type="number" value="7.5" step="0.5"><small>Bu sürenin altında kalan günler puantajda ⚠ işareti alır</small></div>
          <div class="field"><label>Günlük standart çalışma süresi (saat)</label><input id="r-std" type="number" value="9" step="0.5"></div>
        </div>
        <div class="field-row">
          <div class="field"><label>Haftalık maksimum çalışma (saat)</label><input id="r-weekmax" type="number" value="45"></div>
          <div class="field"><label>Hafta tatili (gün)</label><input id="r-restday" type="number" value="1" min="0" max="2"></div>
        </div>
      </div>
      <div class="card">
        <h2>Tolerans Aralıkları</h2>
        <p class="hint">Bu saatlerde yapılan girişler ilgili vardiyaya sayılır.</p>
        <div class="field-row">
          <div class="field"><label>Giriş tolerans başlangıcı</label><input id="r-tol-start" type="time" value="06:30"></div>
          <div class="field"><label>Giriş tolerans bitişi</label><input id="r-tol-end" type="time" value="08:15"></div>
        </div>
        <div class="field-row">
          <div class="field"><label>Erken giriş için max. dakika</label><input id="r-early" type="number" value="30"></div>
          <div class="field"><label>Geç giriş için max. dakika</label><input id="r-late" type="number" value="15"></div>
        </div>
      </div>
      <div class="card">
        <h2>Fazla Mesai (FM)</h2>
        <div class="field-row">
          <div class="field"><label>Yıllık FM tavanı (saat)</label><input id="r-fm-max" type="number" value="270"><small>Kanuni sınır: 270 saat/yıl</small></div>
          <div class="field"><label>FM çarpanı</label><input id="r-fm-mult" type="number" value="1.5" step="0.25"><small>Normal saat ücretinin katı</small></div>
        </div>
        <div class="switch">
          <div class="info"><b>FM için onay zorunlu</b><small>İşaretliyse, FM süresi İK/Yönetici onayı olmadan puantaja yazılmaz</small></div>
          <div class="toggle on" id="t-fm-approve"></div>
        </div>
      </div>
    </section>

    <!-- İZİN TÜRLERİ -->
    <section class="section" id="sec-leaves">
      <h1>İzin Türleri</h1><p class="sub">İzin tanımları, kısa kodları ve yıllık hakediş süreleri</p>
      <div class="card">
        <h2>İzin Tanımları</h2>
        <table>
          <thead><tr><th>Kod</th><th>Adı</th><th>Yıllık hak (gün)</th><th>Ücretli mi?</th><th></th></tr></thead>
          <tbody id="leave-body"></tbody>
        </table>
        <div style="margin-top:14px;display:grid;grid-template-columns:80px 1fr 140px 120px auto;gap:8px;align-items:end">
          <div class="field" style="margin:0"><label>Kod</label><input id="lv-code" placeholder="Yİ" maxlength="3"></div>
          <div class="field" style="margin:0"><label>Adı</label><input id="lv-name" placeholder="Yıllık izin"></div>
          <div class="field" style="margin:0"><label>Yıllık (gün)</label><input id="lv-days" type="number" value="14"></div>
          <div class="field" style="margin:0"><label>Ücretli</label><select id="lv-paid"><option value="1">Evet</option><option value="0">Hayır</option></select></div>
          <button class="btn btn-amber" id="lv-add">+ Ekle</button>
        </div>
      </div>
    </section>

    <!-- TATİL GÜNLERİ -->
    <section class="section" id="sec-holidays">
      <h1>Resmi Tatil Günleri</h1><p class="sub">Bu günler puantajda otomatik tatil sayılır</p>
      <div class="card">
        <h2>Tatil Listesi</h2>
        <table>
          <thead><tr><th>Tarih</th><th>Adı</th><th>Tür</th><th></th></tr></thead>
          <tbody id="hol-body"></tbody>
        </table>
        <div style="margin-top:14px;display:grid;grid-template-columns:160px 1fr 140px auto;gap:8px;align-items:end">
          <div class="field" style="margin:0"><label>Tarih</label><input id="hol-date" type="date"></div>
          <div class="field" style="margin:0"><label>Tatil adı</label><input id="hol-name" placeholder="Cumhuriyet Bayramı"></div>
          <div class="field" style="margin:0"><label>Tür</label><select id="hol-type"><option>Tam gün</option><option>Yarım gün</option></select></div>
          <button class="btn btn-amber" id="hol-add">+ Ekle</button>
        </div>
      </div>
    </section>

    <!-- KVKK -->
    <section class="section" id="sec-kvkk">
      <h1>KVKK & Gizlilik</h1><p class="sub">Kişisel veri görünürlüğü ve saklama kuralları</p>
      <div class="card">
        <h2>Gösterim Tercihleri</h2>
        <div class="switch">
          <div class="info"><b>Kapı ekranında isim kısaltması</b><small>Em.. Ce.. formatında gösterir</small></div>
          <div class="toggle on" id="t-kvkk-name"></div>
        </div>
        <div class="switch">
          <div class="info"><b>TC kimlik maskele</b><small>Listelerde 123****01 gösterir</small></div>
          <div class="toggle on" id="t-kvkk-tc"></div>
        </div>
        <div class="switch">
          <div class="info"><b>Doğum tarihi gizle</b><small>Personel hariç kimse göremesin</small></div>
          <div class="toggle" id="t-kvkk-dob"></div>
        </div>
      </div>
      <div class="card">
        <h2>Veri Saklama</h2>
        <div class="field"><label>Geçmiş giriş/çıkış kayıtları saklama süresi (yıl)</label><input id="kvkk-att-years" type="number" value="3"><small>Kanuni minimum 2 yıl</small></div>
        <div class="field"><label>İşten çıkan personel verisi saklama (yıl)</label><input id="kvkk-emp-years" type="number" value="10"></div>
      </div>
    </section>

    <!-- SİSTEM -->
    <section class="section" id="sec-system">
      <h1>Sistem</h1><p class="sub">Genel sistem ayarları ve veri yönetimi</p>
      <div class="card">
        <h2>Bildirimler</h2>
        <div class="switch"><div class="info"><b>Yeni giriş için bildirim</b><small>İK paneline canlı bildirim gönder</small></div><div class="toggle on" id="t-notify-in"></div></div>
        <div class="switch"><div class="info"><b>Geç giriş için uyarı</b><small>15+ dk geç gelenler için bildirim</small></div><div class="toggle on" id="t-notify-late"></div></div>
        <div class="switch"><div class="info"><b>FM onay bildirimleri</b><small>Yöneticiye FM talepleri bildirilsin</small></div><div class="toggle on" id="t-notify-fm"></div></div>
      </div>
      <div class="card">
        <h2>Tehlikeli Bölge</h2>
        <p class="hint" style="color:var(--danger)">⚠ Bu işlemler geri alınamaz</p>
        <button class="btn btn-ghost" id="reset-att" style="margin-right:8px">Tüm giriş/çıkış kayıtlarını sil</button>
        <button class="btn btn-ghost" id="reset-all" style="color:var(--danger);border-color:var(--danger)">Tüm verileri sil (demo sıfırlama)</button>
      </div>
    </section>

    <div class="save-bar">
      <span class="save-status" id="save-status">Tüm değişiklikler kaydedildi</span>
      <button class="save-btn" id="save-all-btn">Değişiklikleri Kaydet</button>
    </div>
  </main>
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

var DEFAULT_DEPS=['Önbüro','Yiyecek & İçecek','Mutfak','Kat Hizmetleri','Teknik','Güvenlik','İnsan Kaynakları','Muhasebe','Animasyon'];
var DEFAULT_GOREVS=['Müdür','Şef','Garson','Aşçı','Resepsiyonist','Güvenlik Görevlisi','Temizlik Görevlisi','Animatör','Personel'];
var DEFAULT_SHIFTS=[{code:'A',name:'Sabah',start:'08:00',end:'16:00',tol:15},{code:'Ara',name:'Ara',start:'12:00',end:'20:00',tol:15},{code:'B',name:'Akşam',start:'16:00',end:'24:00',tol:15},{code:'Gece',name:'Gece',start:'00:00',end:'08:00',tol:15}];
var DEFAULT_LEAVES=[{code:'Yİ',name:'Yıllık izin',days:14,paid:1},{code:'M',name:'Mazaret izni',days:5,paid:1},{code:'Üİ',name:'Ücretsiz izin',days:0,paid:0},{code:'RP',name:'Raporlu',days:0,paid:0}];
var DEFAULT_HOLIDAYS=[{date:'2026-01-01',name:'Yılbaşı',type:'Tam gün'},{date:'2026-04-23',name:'Ulusal Egemenlik ve Çocuk Bayramı',type:'Tam gün'},{date:'2026-05-01',name:'Emek ve Dayanışma Günü',type:'Tam gün'},{date:'2026-05-19',name:'Gençlik ve Spor Bayramı',type:'Tam gün'},{date:'2026-08-30',name:'Zafer Bayramı',type:'Tam gün'},{date:'2026-10-29',name:'Cumhuriyet Bayramı',type:'Tam gün'}];

var data={};
var changed=false;

function markChanged(){changed=true;document.getElementById('save-status').textContent='Kaydedilmemiş değişiklikler var';document.getElementById('save-status').classList.add('changed');}
function markSaved(){changed=false;document.getElementById('save-status').textContent='Tüm değişiklikler kaydedildi';document.getElementById('save-status').classList.remove('changed');}

function toast(t){var el=document.getElementById('toast');el.textContent=t;el.classList.add('on');clearTimeout(el._t);el._t=setTimeout(function(){el.classList.remove('on');},2500);}

// Menü
document.querySelectorAll('.menu-item').forEach(function(m){
  m.addEventListener('click',function(){
    document.querySelectorAll('.menu-item').forEach(function(x){x.classList.remove('active');});
    document.querySelectorAll('.section').forEach(function(x){x.classList.remove('active');});
    m.classList.add('active');
    document.getElementById('sec-'+m.dataset.s).classList.add('active');
  });
});

// Toggle butonları
document.querySelectorAll('.toggle').forEach(function(t){
  t.addEventListener('click',function(){t.classList.toggle('on');markChanged();});
});

// Genel form change tracker
['g-name','g-city','g-district','g-phone','g-address','r-min','r-std','r-weekmax','r-restday','r-tol-start','r-tol-end','r-early','r-late','r-fm-max','r-fm-mult','kvkk-att-years','kvkk-emp-years'].forEach(function(id){
  var el=document.getElementById(id);
  if(el)el.addEventListener('input',markChanged);
});

// === BÖLÜMLER ===
function renderDeps(){
  var box=document.getElementById('dep-tags');
  if(!data.departments||!data.departments.length){box.innerHTML='<span style="color:var(--muted);font-size:12px">Henüz eklenmedi</span>';return;}
  box.innerHTML=data.departments.map(function(d,i){return '<span class="tag">'+d+'<button data-i="'+i+'">×</button></span>';}).join('');
  box.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){data.departments.splice(+b.dataset.i,1);renderDeps();markChanged();});});
}
document.getElementById('dep-add').addEventListener('click',function(){var v=document.getElementById('dep-new').value.trim();if(!v)return;if(!data.departments)data.departments=[];if(data.departments.indexOf(v)<0){data.departments.push(v);markChanged();}document.getElementById('dep-new').value='';renderDeps();});
document.getElementById('dep-new').addEventListener('keydown',function(e){if(e.key==='Enter')document.getElementById('dep-add').click();});

// === GÖREVLER ===
function renderGorevs(){
  var box=document.getElementById('gorev-tags');
  if(!data.positions||!data.positions.length){box.innerHTML='<span style="color:var(--muted);font-size:12px">Henüz eklenmedi</span>';return;}
  box.innerHTML=data.positions.map(function(d,i){return '<span class="tag">'+d+'<button data-i="'+i+'">×</button></span>';}).join('');
  box.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){data.positions.splice(+b.dataset.i,1);renderGorevs();markChanged();});});
}
document.getElementById('gorev-add').addEventListener('click',function(){var v=document.getElementById('gorev-new').value.trim();if(!v)return;if(!data.positions)data.positions=[];if(data.positions.indexOf(v)<0){data.positions.push(v);markChanged();}document.getElementById('gorev-new').value='';renderGorevs();});
document.getElementById('gorev-new').addEventListener('keydown',function(e){if(e.key==='Enter')document.getElementById('gorev-add').click();});

// === VARDİYALAR ===
function renderShifts(){
  var body=document.getElementById('shift-body');
  if(!data.shifts||!data.shifts.length){body.innerHTML='<tr><td colspan="6" style="color:var(--muted);text-align:center;padding:20px">Henüz eklenmedi</td></tr>';return;}
  body.innerHTML=data.shifts.map(function(s,i){return '<tr><td><b>'+s.code+'</b></td><td>'+s.name+'</td><td class="mono">'+s.start+'</td><td class="mono">'+s.end+'</td><td>'+(s.tol||0)+' dk</td><td><button class="del-btn" data-i="'+i+'">×</button></td></tr>';}).join('');
  body.querySelectorAll('.del-btn').forEach(function(b){b.addEventListener('click',function(){data.shifts.splice(+b.dataset.i,1);renderShifts();markChanged();});});
}
document.getElementById('sh-add').addEventListener('click',function(){
  var code=document.getElementById('sh-code').value.trim();
  var name=document.getElementById('sh-name').value.trim();
  var start=document.getElementById('sh-start').value;
  var end=document.getElementById('sh-end').value;
  var tol=+document.getElementById('sh-tol').value||0;
  if(!code||!name)return toast('Kod ve ad gerekli');
  if(!data.shifts)data.shifts=[];
  data.shifts.push({code:code,name:name,start:start,end:end,tol:tol});
  ['sh-code','sh-name'].forEach(function(id){document.getElementById(id).value='';});
  renderShifts();markChanged();
});

// === İZİN TÜRLERİ ===
function renderLeaves(){
  var body=document.getElementById('leave-body');
  if(!data.leaves||!data.leaves.length){body.innerHTML='<tr><td colspan="5" style="color:var(--muted);text-align:center;padding:20px">Henüz eklenmedi</td></tr>';return;}
  body.innerHTML=data.leaves.map(function(l,i){return '<tr><td><b>'+l.code+'</b></td><td>'+l.name+'</td><td>'+(l.days||0)+'</td><td>'+(l.paid?'Evet':'Hayır')+'</td><td><button class="del-btn" data-i="'+i+'">×</button></td></tr>';}).join('');
  body.querySelectorAll('.del-btn').forEach(function(b){b.addEventListener('click',function(){data.leaves.splice(+b.dataset.i,1);renderLeaves();markChanged();});});
}
document.getElementById('lv-add').addEventListener('click',function(){
  var code=document.getElementById('lv-code').value.trim();
  var name=document.getElementById('lv-name').value.trim();
  if(!code||!name)return toast('Kod ve ad gerekli');
  if(!data.leaves)data.leaves=[];
  data.leaves.push({code:code,name:name,days:+document.getElementById('lv-days').value||0,paid:+document.getElementById('lv-paid').value});
  ['lv-code','lv-name'].forEach(function(id){document.getElementById(id).value='';});
  renderLeaves();markChanged();
});

// === TATİL GÜNLERİ ===
function renderHolidays(){
  var body=document.getElementById('hol-body');
  if(!data.holidays||!data.holidays.length){body.innerHTML='<tr><td colspan="4" style="color:var(--muted);text-align:center;padding:20px">Henüz eklenmedi</td></tr>';return;}
  body.innerHTML=data.holidays.sort(function(a,b){return (a.date||'').localeCompare(b.date||'');}).map(function(h,i){return '<tr><td class="mono">'+h.date+'</td><td>'+h.name+'</td><td>'+h.type+'</td><td><button class="del-btn" data-i="'+i+'">×</button></td></tr>';}).join('');
  body.querySelectorAll('.del-btn').forEach(function(b){b.addEventListener('click',function(){data.holidays.splice(+b.dataset.i,1);renderHolidays();markChanged();});});
}
document.getElementById('hol-add').addEventListener('click',function(){
  var date=document.getElementById('hol-date').value;
  var name=document.getElementById('hol-name').value.trim();
  if(!date||!name)return toast('Tarih ve ad gerekli');
  if(!data.holidays)data.holidays=[];
  data.holidays.push({date:date,name:name,type:document.getElementById('hol-type').value});
  document.getElementById('hol-date').value='';document.getElementById('hol-name').value='';
  renderHolidays();markChanged();
});

// === KAYDET ===
document.getElementById('save-all-btn').addEventListener('click',async function(){
  var btn=this;btn.disabled=true;btn.textContent='Kaydediliyor…';
  // Form değerlerini topla
  data.general={
    name:document.getElementById('g-name').value,
    city:document.getElementById('g-city').value,
    district:document.getElementById('g-district').value,
    phone:document.getElementById('g-phone').value,
    address:document.getElementById('g-address').value
  };
  data.rules={
    minHours:+document.getElementById('r-min').value,
    stdHours:+document.getElementById('r-std').value,
    weekMax:+document.getElementById('r-weekmax').value,
    restDay:+document.getElementById('r-restday').value,
    tolStart:document.getElementById('r-tol-start').value,
    tolEnd:document.getElementById('r-tol-end').value,
    early:+document.getElementById('r-early').value,
    late:+document.getElementById('r-late').value,
    fmMax:+document.getElementById('r-fm-max').value,
    fmMult:+document.getElementById('r-fm-mult').value,
    fmApproval:document.getElementById('t-fm-approve').classList.contains('on')
  };
  data.kvkk={
    nameMask:document.getElementById('t-kvkk-name').classList.contains('on'),
    tcMask:document.getElementById('t-kvkk-tc').classList.contains('on'),
    dobHide:document.getElementById('t-kvkk-dob').classList.contains('on'),
    attYears:+document.getElementById('kvkk-att-years').value,
    empYears:+document.getElementById('kvkk-emp-years').value
  };
  data.system={
    notifyIn:document.getElementById('t-notify-in').classList.contains('on'),
    notifyLate:document.getElementById('t-notify-late').classList.contains('on'),
    notifyFm:document.getElementById('t-notify-fm').classList.contains('on')
  };
  try{
    await req('/settings',{method:'PUT',body:data});
    toast('Tüm ayarlar kaydedildi ✓');
    markSaved();
  }catch(e){toast('Hata: '+e.message);}
  btn.disabled=false;btn.textContent='Değişiklikleri Kaydet';
});

// === RESET ===
document.getElementById('reset-att').addEventListener('click',async function(){
  if(!confirm('Tüm giriş/çıkış kayıtları silinecek. Emin misiniz?'))return;
  try{await req('/reset',{method:'POST',body:{type:'attendance'}});toast('Kayıtlar silindi');}catch(e){toast('Hata: '+e.message);}
});
document.getElementById('reset-all').addEventListener('click',async function(){
  if(!confirm('TÜM VERİLER silinecek (personel, kayıtlar, ayarlar). Geri alınamaz! Emin misiniz?'))return;
  if(!confirm('Bir kez daha onaylayın. Bu işlem geri alınamaz!'))return;
  try{await req('/reset',{method:'POST',body:{}});toast('Tüm veriler silindi');}catch(e){toast('Hata: '+e.message);}
});

// === YÜKLE ===
async function loadSettings(){
  try{
    var s=await req('/settings');
    data=s||{};
  }catch(e){data={};}
  // Defaultlar
  if(!data.departments||!data.departments.length)data.departments=DEFAULT_DEPS.slice();
  if(!data.positions||!data.positions.length)data.positions=DEFAULT_GOREVS.slice();
  if(!data.shifts||!data.shifts.length)data.shifts=DEFAULT_SHIFTS.slice();
  if(!data.leaves||!data.leaves.length)data.leaves=DEFAULT_LEAVES.slice();
  if(!data.holidays||!data.holidays.length)data.holidays=DEFAULT_HOLIDAYS.slice();
  // Genel
  if(data.general){
    document.getElementById('g-name').value=data.general.name||'';
    document.getElementById('g-city').value=data.general.city||'';
    document.getElementById('g-district').value=data.general.district||'';
    document.getElementById('g-phone').value=data.general.phone||'';
    document.getElementById('g-address').value=data.general.address||'';
  }
  // Kurallar
  if(data.rules){
    if(data.rules.minHours)document.getElementById('r-min').value=data.rules.minHours;
    if(data.rules.stdHours)document.getElementById('r-std').value=data.rules.stdHours;
    if(data.rules.weekMax)document.getElementById('r-weekmax').value=data.rules.weekMax;
    if(data.rules.restDay!=null)document.getElementById('r-restday').value=data.rules.restDay;
    if(data.rules.tolStart)document.getElementById('r-tol-start').value=data.rules.tolStart;
    if(data.rules.tolEnd)document.getElementById('r-tol-end').value=data.rules.tolEnd;
    if(data.rules.early)document.getElementById('r-early').value=data.rules.early;
    if(data.rules.late)document.getElementById('r-late').value=data.rules.late;
    if(data.rules.fmMax)document.getElementById('r-fm-max').value=data.rules.fmMax;
    if(data.rules.fmMult)document.getElementById('r-fm-mult').value=data.rules.fmMult;
    document.getElementById('t-fm-approve').classList.toggle('on',data.rules.fmApproval!==false);
  }
  // KVKK
  if(data.kvkk){
    document.getElementById('t-kvkk-name').classList.toggle('on',data.kvkk.nameMask!==false);
    document.getElementById('t-kvkk-tc').classList.toggle('on',data.kvkk.tcMask!==false);
    document.getElementById('t-kvkk-dob').classList.toggle('on',!!data.kvkk.dobHide);
    if(data.kvkk.attYears)document.getElementById('kvkk-att-years').value=data.kvkk.attYears;
    if(data.kvkk.empYears)document.getElementById('kvkk-emp-years').value=data.kvkk.empYears;
  }
  // Sistem
  if(data.system){
    document.getElementById('t-notify-in').classList.toggle('on',data.system.notifyIn!==false);
    document.getElementById('t-notify-late').classList.toggle('on',data.system.notifyLate!==false);
    document.getElementById('t-notify-fm').classList.toggle('on',data.system.notifyFm!==false);
  }
  renderDeps();renderGorevs();renderShifts();renderLeaves();renderHolidays();
  markSaved();
}

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
