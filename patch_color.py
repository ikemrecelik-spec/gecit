#!/usr/bin/env python3
"""
patch_color.py — Renk secici (color picker) ekleme
1. Ayarlar > Vardiya ekle/duzenle renk secici
2. Ayarlar > Izin turu ekle/duzenle renk secici
3. Puantaj > Secilen renkleri kullanma
4. Shiftler sayfasi > Ayni renkleri kullanma
"""
import shutil, sys

V2 = '/home/ubuntu/gecit-backend/public/v2.html'

shutil.copy2(V2, V2 + '.bak-color')
print('[OK] Yedek alindi:', V2 + '.bak-color')

with open(V2, 'r', encoding='utf-8') as f:
    src = f.read()

ok = 0
fail = 0

def R(old, new, label=''):
    global src, ok, fail
    n = src.count(old)
    if n == 0:
        print(f'[FAIL] {label}')
        fail += 1
        return False
    src = src.replace(old, new, 1)
    ok += 1
    print(f'[OK] {label}')
    return True


# =====================================================
# 1. AYARLAR — VARDIYA RENK SECICI
# =====================================================

# 1a. Shift tablo header: Renk kolonu
R(
    '<th>Tolerans</th><th></th></tr></thead>\n          <tbody id="shift-body"></tbody>',
    '<th>Tolerans</th><th>Renk</th><th></th></tr></thead>\n          <tbody id="shift-body"></tbody>',
    '1a. Shift tablo header: Renk kolonu'
)

# 1b. Shift bos colspan 6->7
R(
    '''colspan="6" style="color:var(--muted);text-align:center;padding:20px">Henüz eklenmedi</td></tr>';return;}''',
    '''colspan="7" style="color:var(--muted);text-align:center;padding:20px">Henüz eklenmedi</td></tr>';return;}''',
    '1b. Shift bos colspan 6->7'
)

# 1c. renderShifts satir render — renk goster + duzenle butonu
R(
    "body.innerHTML=data.shifts.map(function(s,i){return '<tr><td><b>'+s.code+'</b></td><td>'+s.name+'</td><td class=\"mono\">'+s.start+'</td><td class=\"mono\">'+s.end+'</td><td>'+(s.tol||0)+' dk</td><td><button class=\"del-btn\" data-i=\"'+i+'\">×</button></td></tr>';}).join('');",
    "body.innerHTML=data.shifts.map(function(s,i){return '<tr><td><b>'+s.code+'</b></td><td>'+s.name+'</td><td class=\"mono\">'+s.start+'</td><td class=\"mono\">'+s.end+'</td><td>'+(s.tol||0)+' dk</td><td><input type=\"color\" value=\"'+(s.color||'#34D9A0')+'\" class=\"sh-clr\" data-i=\"'+i+'\" style=\"width:30px;height:24px;padding:1px 2px;border:1px solid var(--line);border-radius:5px;background:var(--panel-2);cursor:pointer\"></td><td style=\"white-space:nowrap\"><button class=\"edit-sh\" data-i=\"'+i+'\" title=\"Düzenle\" style=\"background:none;border:1px solid var(--line);color:var(--amber);border-radius:5px;padding:2px 7px;cursor:pointer;font-size:12px;margin-right:4px\">✎</button><button class=\"del-btn\" data-i=\"'+i+'\">×</button></td></tr>';}).join('');",
    '1c. renderShifts: renk + duzenle butonu'
)

# 1d. del-btn handler sonrasi — renk change + edit handler ekle
R(
    "body.querySelectorAll('.del-btn').forEach(function(b){b.addEventListener('click',function(){data.shifts.splice(+b.dataset.i,1);renderShifts();markChanged();});});\n}\ndocument.getElementById('sh-add').addEventListener('click',function(){",
    """body.querySelectorAll('.del-btn').forEach(function(b){b.addEventListener('click',function(){data.shifts.splice(+b.dataset.i,1);renderShifts();markChanged();});});
  body.querySelectorAll('.sh-clr').forEach(function(c){c.addEventListener('input',function(){data.shifts[+c.dataset.i].color=c.value;markChanged();});});
  body.querySelectorAll('.edit-sh').forEach(function(b){b.addEventListener('click',function(){var i=+b.dataset.i,s=data.shifts[i];document.getElementById('sh-code').value=s.code;document.getElementById('sh-name').value=s.name;document.getElementById('sh-start').value=s.start;document.getElementById('sh-end').value=s.end;document.getElementById('sh-tol').value=s.tol||0;document.getElementById('sh-color').value=s.color||'#34D9A0';data.shifts.splice(i,1);renderShifts();markChanged();});});
}
document.getElementById('sh-add').addEventListener('click',function(){""",
    '1d. Shift renk change + edit handler'
)

# 1e. Shift ekleme grid — renk kolonu ekle
R(
    'grid-template-columns:80px 1fr 100px 100px 130px auto;gap:8px;align-items:end">\n          <div class="field" style="margin:0"><label>Kod</label><input id="sh-code"',
    'grid-template-columns:80px 1fr 100px 100px 130px 50px auto;gap:8px;align-items:end">\n          <div class="field" style="margin:0"><label>Kod</label><input id="sh-code"',
    '1e. Shift form grid: renk kolonu genislik'
)

# 1f. Shift form — renk input ekle (butondan hemen once)
R(
    '<button class="btn btn-amber" id="sh-add">+ Ekle</button>\n        </div>\n      </div>\n    </section>\n\n    <!-- \xc7ALI\u015eMA KURALLARI -->',
    '<div class="field" style="margin:0"><label>Renk</label><input id="sh-color" type="color" value="#34D9A0" style="width:40px;height:34px;padding:2px;border:1px solid var(--line);border-radius:6px;background:var(--panel-2);cursor:pointer"></div>\n          <button class="btn btn-amber" id="sh-add">+ Ekle</button>\n        </div>\n      </div>\n    </section>\n\n    <!-- \xc7ALI\u015eMA KURALLARI -->',
    '1f. Shift form: renk input'
)

# 1g. Shift push — renk dahil et
R(
    "data.shifts.push({code:code,name:name,start:start,end:end,tol:tol});",
    "var shColor=document.getElementById('sh-color').value||'#34D9A0';\n  data.shifts.push({code:code,name:name,start:start,end:end,tol:tol,color:shColor});",
    '1g. Shift push: renk ekle'
)

# 1h. DEFAULT_SHIFTS'e renk ekle
R(
    "var DEFAULT_SHIFTS=[{code:'A',name:'Sabah',start:'08:00',end:'16:00',tol:15},{code:'Ara',name:'Ara',start:'12:00',end:'20:00',tol:15},{code:'B',name:'Ak\u015fam',start:'16:00',end:'24:00',tol:15},{code:'Gece',name:'Gece',start:'00:00',end:'08:00',tol:15}];",
    "var DEFAULT_SHIFTS=[{code:'A',name:'Sabah',start:'08:00',end:'16:00',tol:15,color:'#34D9A0'},{code:'Ara',name:'Ara',start:'12:00',end:'20:00',tol:15,color:'#6FB1FF'},{code:'B',name:'Ak\u015fam',start:'16:00',end:'24:00',tol:15,color:'#F2B53B'},{code:'Gece',name:'Gece',start:'00:00',end:'08:00',tol:15,color:'#C792EA'}];",
    '1h. DEFAULT_SHIFTS: renkler'
)


# =====================================================
# 2. AYARLAR — IZIN TURU RENK SECICI
# =====================================================

# 2a. Izin tablo header: Renk kolonu
R(
    "<th>\xdccretli mi?</th><th></th></tr></thead>\n          <tbody id=\"leave-body\"></tbody>",
    "<th>\xdccretli mi?</th><th>Renk</th><th></th></tr></thead>\n          <tbody id=\"leave-body\"></tbody>",
    '2a. Izin tablo header: Renk kolonu'
)

# 2b. Izin bos colspan 5->6
R(
    '''colspan="5" style="color:var(--muted);text-align:center;padding:20px">Hen''',
    '''colspan="6" style="color:var(--muted);text-align:center;padding:20px">Hen''',
    '2b. Izin bos colspan 5->6'
)

# 2c. renderLeaves — renk goster + duzenle butonu
R(
    "body.innerHTML=data.leaves.map(function(l,i){return '<tr><td><b>'+l.code+'</b></td><td>'+l.name+'</td><td>'+(l.days||0)+'</td><td>'+(l.paid?'Evet':'Hay\u0131r')+'</td><td><button class=\"del-btn\" data-i=\"'+i+'\">×</button></td></tr>';}).join('');",
    "body.innerHTML=data.leaves.map(function(l,i){return '<tr><td><b>'+l.code+'</b></td><td>'+l.name+'</td><td>'+(l.days||0)+'</td><td>'+(l.paid?'Evet':'Hay\u0131r')+'</td><td><input type=\"color\" value=\"'+(l.color||'#8FA6B0')+'\" class=\"lv-clr\" data-i=\"'+i+'\" style=\"width:30px;height:24px;padding:1px 2px;border:1px solid var(--line);border-radius:5px;background:var(--panel-2);cursor:pointer\"></td><td style=\"white-space:nowrap\"><button class=\"edit-lv\" data-i=\"'+i+'\" title=\"Düzenle\" style=\"background:none;border:1px solid var(--line);color:var(--amber);border-radius:5px;padding:2px 7px;cursor:pointer;font-size:12px;margin-right:4px\">✎</button><button class=\"del-btn\" data-i=\"'+i+'\">×</button></td></tr>';}).join('');",
    '2c. renderLeaves: renk + duzenle butonu'
)

# 2d. renderLeaves del-btn sonrasi — renk + edit handler
R(
    "body.querySelectorAll('.del-btn').forEach(function(b){b.addEventListener('click',function(){data.leaves.splice(+b.dataset.i,1);renderLeaves();markChanged();});});\n}\ndocument.getElementById('lv-add').addEventListener('click',function(){",
    """body.querySelectorAll('.del-btn').forEach(function(b){b.addEventListener('click',function(){data.leaves.splice(+b.dataset.i,1);renderLeaves();markChanged();});});
  body.querySelectorAll('.lv-clr').forEach(function(c){c.addEventListener('input',function(){data.leaves[+c.dataset.i].color=c.value;markChanged();});});
  body.querySelectorAll('.edit-lv').forEach(function(b){b.addEventListener('click',function(){var i=+b.dataset.i,l=data.leaves[i];document.getElementById('lv-code').value=l.code;document.getElementById('lv-name').value=l.name;document.getElementById('lv-days').value=l.days||0;document.getElementById('lv-paid').value=l.paid?'1':'0';document.getElementById('lv-color').value=l.color||'#8FA6B0';data.leaves.splice(i,1);renderLeaves();markChanged();});});
}
document.getElementById('lv-add').addEventListener('click',function(){""",
    '2d. Izin renk change + edit handler'
)

# 2e. Izin form grid — renk kolonu ekle
R(
    'grid-template-columns:80px 1fr 140px 120px auto;gap:8px;align-items:end">\n          <div class="field" style="margin:0"><label>Kod</label><input id="lv-code"',
    'grid-template-columns:80px 1fr 140px 120px 50px auto;gap:8px;align-items:end">\n          <div class="field" style="margin:0"><label>Kod</label><input id="lv-code"',
    '2e. Izin form grid: renk kolonu genislik'
)

# 2f. Izin form — renk input ekle
R(
    "<button class=\"btn btn-amber\" id=\"lv-add\">+ Ekle</button>\n        </div>\n      </div>\n    </section>\n\n    <!-- TAT\u0130L G\xdcNLER\u0130 -->",
    "<div class=\"field\" style=\"margin:0\"><label>Renk</label><input id=\"lv-color\" type=\"color\" value=\"#8FA6B0\" style=\"width:40px;height:34px;padding:2px;border:1px solid var(--line);border-radius:6px;background:var(--panel-2);cursor:pointer\"></div>\n          <button class=\"btn btn-amber\" id=\"lv-add\">+ Ekle</button>\n        </div>\n      </div>\n    </section>\n\n    <!-- TAT\u0130L G\xdcNLER\u0130 -->",
    '2f. Izin form: renk input'
)

# 2g. Izin push — renk dahil et
R(
    "data.leaves.push({code:code,name:name,days:+document.getElementById('lv-days').value||0,paid:+document.getElementById('lv-paid').value});",
    "var lvColor=document.getElementById('lv-color').value||'#8FA6B0';\n  data.leaves.push({code:code,name:name,days:+document.getElementById('lv-days').value||0,paid:+document.getElementById('lv-paid').value,color:lvColor});",
    '2g. Izin push: renk ekle'
)

# 2h. DEFAULT_LEAVES'e renk ekle + ASCII kodlar
R(
    "var DEFAULT_LEAVES=[{code:'Y\u0130',name:'Y\u0131ll\u0131k izin',days:14,paid:1},{code:'M',name:'Mazaret izni',days:5,paid:1},{code:'\xdc\u0130',name:'\xdccretsiz izin',days:0,paid:0},{code:'RP',name:'Raporlu',days:0,paid:0}];",
    "var DEFAULT_LEAVES=[{code:'Yi',name:'Y\u0131ll\u0131k izin',days:14,paid:1,color:'#6FB1FF'},{code:'M',name:'Mazaret izni',days:5,paid:1,color:'#F2B53B'},{code:'Ui',name:'\xdccretsiz izin',days:0,paid:0,color:'#C792EA'},{code:'RP',name:'Raporlu',days:0,paid:0,color:'#FF6B6B'}];",
    '2h. DEFAULT_LEAVES: renkler + ASCII kodlar'
)


# =====================================================
# 3. PUANTAJ — DINAMIK RENKLER
# =====================================================

# 3a. CELL_CLS sonrasina CODE_COLORS map + ayarlar yukle
R(
    "var CELL_CLS={X:'cX',EK:'cEK',HT:'cHT',BT:'cBT',BC:'cBC',M:'cM',Ui:'cUi',Yi:'cYi',RP:'cRP',UR:'cUR',G:'cG',D:'cD','\xb7':'cDot'};",
    r"""var CELL_CLS={X:'cX',EK:'cEK',HT:'cHT',BT:'cBT',BC:'cBC',M:'cM',Ui:'cUi',Yi:'cYi',RP:'cRP',UR:'cUR',G:'cG',D:'cD','\u00b7':'cDot'};
var CODE_COLORS={};
async function loadSettingsColors(){
  try{
    var s=await req('/settings');
    if(s&&s.shifts){s.shifts.forEach(function(sh){if(sh.color)CODE_COLORS[sh.code]=sh.color;});}
    if(s&&s.leaves){s.leaves.forEach(function(lv){if(lv.color)CODE_COLORS[lv.code]=lv.color;});}
    if(!CODE_COLORS['X']&&s&&s.shifts&&s.shifts[0])CODE_COLORS['X']=s.shifts[0].color||'#34D9A0';
  }catch(e){}
}""",
    '3a. Puantaj: CODE_COLORS + loadSettingsColors'
)

# 3b. Puantaj hucre render — dinamik renk
R(
    "var cls=CELL_CLS[code]||'cDot';\n      cells+='<td><span class=\"c '+cls+'\">'+code+'</span></td>';",
    """var _cc=CODE_COLORS[code];
      if(_cc){
        cells+='<td><span class="c" style="background:'+_cc+'22;color:'+_cc+';font-weight:700">'+code+'</span></td>';
      }else{
        var cls=CELL_CLS[code]||'cDot';
        cells+='<td><span class="c '+cls+'">'+code+'</span></td>';
      }""",
    '3b. Puantaj hucre: dinamik renk'
)

# 3c. Puantaj load — settings renkleri yukle
R(
    "async function load(){\n  document.getElementById('pt-body').innerHTML='<tr><td colspan=\"50\" style=\"text-align:center;padding:30px;color:var(--muted)\">Yukleniyor...</td></tr>';\n  try{\n    var data=await req('/puantaj?month='+curYear+'-'+curMonth);\n    renderTable(data);",
    "async function load(){\n  document.getElementById('pt-body').innerHTML='<tr><td colspan=\"50\" style=\"text-align:center;padding:30px;color:var(--muted)\">Yukleniyor...</td></tr>';\n  try{\n    await loadSettingsColors();\n    var data=await req('/puantaj?month='+curYear+'-'+curMonth);\n    renderTable(data);",
    '3c. Puantaj load: settings renkleri yukle'
)


# =====================================================
# 4. SHIFTLER (tpl-vplan) — AYARLAR RENKLERI
# =====================================================

# tpl-vplan'da SHIFTS dizisi hardcoded. Mevcut yapıyı bozmadan,
# settings'ten renkleri yükleyip SHIFTS'i güncelleyen kod ekleyelim.
# Bunun için legend oluşturma kodundan sonra enjeksiyon yapalım.
# Hint satirini anchor olarak kullanalim:

R(
    "<div class=\"hint\">Bir hucreye tikla",
    """<div class="hint" id="vplan-hint">Bir hucreye tikla""",
    '4a. tpl-vplan: hint id ekle'
)

# tpl-vplan script'inin sonuna (updateLabel();load(); oncesine) renk guncelleme kodu ekle
# Anchor: tpl-vplan'daki toast fonksiyonunun hemen oncesine degil,
# SHIFTS dizisinden sonra (legend oluşturulduktan sonra)

# Daha guvenli anchor: tpl-vplan'daki req fonksiyonu icindeki gecitpdks URL'si
# (bu zaten duzeltilmis olabilir ama bilinmiyor)
# En guvenli: SHIFTS dizisi tanimlandiktan sonra ekleme

# SHIFTS dizisinin son elemani '-' (bos). Ondan sonra gelen kodu bulalim.
# Legend olusturma kodu: document.getElementById('legend') ile baslayan

# Alternatif yaklasim: Mevcut load fonksiyonuna settings renk yüklemesi ekle
# tpl-vplan'da data load edildikten sonra SHIFTS renklerini guncelle

# En temiz yol: SHIFTS tanımından sonra, settings'ten renkleri güncelleyen
# bir IIFE (immediately invoked) eklemek
# Anchor olarak "Bir hucreye tikla" hint'inden sonraki scroll div'i kullanabiliriz

# Fakat tpl-vplan'ın tam script yapısını görmediğimiz için,
# en güvenli yol: legend div'inin olusturulma kodunu bulmak
# Grep'ten: <div class="legend" id="legend"></div>

# tpl-vplan script'inde legend'ı dolduran kod olmalı
# SHIFTS.forEach → legend innerHTML seklinde

# Guvenli enjeksiyon noktasi: <div class="legend" id="legend"></div> satirindan sonra
# Ama bu HTML'de, script'te degil.

# En basit: tpl-vplan'ın <script> tagı sonuna, </script></template> den once ekle
# Ama tam kapatma noktasını bilmiyorum.

# Alternatif: tpl-vplan'daki mevcut SHIFTS tanımını değiştirmek yerine,
# sadece hücre render'ında renk override'ı yapalım

# tpl-vplan'daki hücre render kodu: cell tıklandığında SHIFTS dizisinden
# bir sonraki shift'e geçiyor ve renk SHIFTS[i].color'dan geliyor
# Yani SHIFTS.color'ı güncellemek yeterli

# tpl-vplan'ın script bloğu genellikle en sonda bir load() veya init() çağrısı yapar
# Bu çağrıdan hemen önce, settings'ten renk güncelleme kodu ekleyebiliriz

# En güvenli yaklaşım: Mevcut SHIFTS tanımına dokunmadan,
# settings'ten okuma yapan ayrı bir script bloğu enjekte edelim
# <div class="toast" id="toast"></div> satırından sonra yeni <script> ekleyelim

# tpl-vplan'daki toast div'i (benzersiz olmalı)
# Aslında tpl-puantaj'da da toast div var. Ama tpl-vplan'daki context ile bulalim.

# Cozum: tpl-vplan'in icindeki hint metnini anchor olarak kullanalim
# "degisir (A → B → ... → OFF → HT → Yi → RP → Ui). Kaydet ile puantaja yansir"
# Bu benzersiz olmali

vpHint = "Kaydet ile puantaja yansir"
if vpHint in src:
    # Bu metnin oldugu satirdan sonra gelen </div> dan sonra script ekle
    # Ama satir bulmak zor. Alternatif: tpl-vplan icerisinde
    # <div class="toast" id="toast"></div> satirini bul
    # ve ondan ONCE settings script'i ekle
    
    # tpl-vplan'daki footer-toast bolumu:
    # </div> (card kapatma)
    # </div> (wrap kapatma)
    # ...toast ve modal divleri...
    # <script>
    
    # En iyisi: vplan'ın ana <script> tagından hemen sonra (iceride) ekle
    # Ama script tag'ini tam bulmam lazim
    
    # Simdilik: SHIFTS dizisi hardcoded oldugu icin
    # settings'ten okuyan bir güncelleme fonksiyonu ekleyelim
    # Bunu tpl-vplan script'inin req() fonksiyonundan sonra ekleyelim
    pass

# VPLAN icin daha guvenli yaklasim:
# SHIFTS'in ilk elemanini anchor olarak kullan (benzersiz)
vplan_anchor = "{code:'A',label:'A - 08:00-16:00',bg:'#1a3a2a',color:'#34D9A0'}"
if vplan_anchor in src:
    # SHIFTS dizisi tamamen tanimlandiktan sonra ekleme yapmak icin
    # Dizinin son elemanini ({code:'-',...}) bulmamiz lazim
    # Ama onu gormedigimiz icin, farkli bir strateji kullanalim
    
    # SHIFTS dizisinden SONRA gelen ilk 'function' veya 'var' satirini bulalim
    # Bu cok riskli. Bunun yerine:
    # SHIFTS tanimindan SONRA, legend olusturma kodundan ONCE
    # bir enjeksiyon yapalim
    pass

# ===== VPLAN RENK GUNCELLEME — EN GUVENLI YONTEM =====
# tpl-vplan icinde var SHIFTS=[ ... ]; tanimindan sonra
# legend'i dolduran ve diger isler yapan kod var.
# SHIFTS'e dokunmadan, vplan'daki <script> sonuna renk guncelleme ekleyelim.

# Strateji: tpl-vplan'daki "Shift Transfer" modal confirm butonundan sonraki
# script koduna ekleme yapalim. tr-confirm butonunun event listener'i
# genellikle script'in sonlarinda olur.

# Alternatif (en basit): SHIFTS dizisini dinamik yapmak yerine,
# sadece hucre renderinda settings renklerini override edelim.
# Bunun icin hucre CSS'inde inline style kullanilsin.

# VPLAN hucre render: .cell class'i ile style="background:... color:..."
# Bu SHIFTS[].bg ve SHIFTS[].color'dan geliyor.
# Eger SHIFTS'i guncelleyemiyorsak, baska bir yol:
# Sayfa yuklendiginde SHIFTS dizisini settings'ten guncelle

# FINAL COZUM: vplan req fonksiyonundan hemen sonra, 
# settingsColorUpdate fonksiyonu tanimlayalim
# vplan'daki req fonksiyonunun benzersiz imzasi:
# "fetch('https://gecitpdks.duckdns.org/api/'+tenant+path" VEYA
# fetch(''+ window.__APIBASE + ... (duzeltilmis versyon)

# Iki farkli req fonksiyonu var:
# 1. tpl-puantaj: window.__APIBASE kullaniyor
# 2. tpl-vplan: gecitpdks.duckdns.org kullaniyor olabilir

# vplan'in kendi script'i icindeki toast fonksiyonunu anchor kullanalim
# tpl-vplan'daki toast: function toast(t){...} — ama puantaj'da da ayni var

# EN GUVENLI: SHIFTS dizisinin ILCE elemanini (benzersiz) anchor olarak kullan
# ve hemen SONRA settings load ekle

# "{code:'A',label:'A - 08:00-16:00',bg:'#1a3a2a',color:'#34D9A0'}," benzersiz mi?
if src.count(vplan_anchor) == 1:
    # SHIFTS array taniminin icindeyiz. Array'in tamamlanmasindan sonra
    # enjeksiyon yapmamiz lazim. Array ];'den sonraki ilk satirda.
    # Ama array'in sonunu bilmiyoruz.
    
    # YAKLASIM: Array'in icindeki son bilinen eleman:
    # {code:'-',label:'- (Bos)',bg:'transparent',color:'#3a4a55'}
    vplan_last = "{code:'-',label:'- (Bos)',bg:'transparent',color:'#3a4a55'}"
    if vplan_last in src:
        # Bu elemanin ardindan "];" gelir, sonra fonksiyonlar baslar
        # "];" dan sonra settings renk guncelleme ekleyelim
        R(
            vplan_last + "\n];",
            vplan_last + """
];
// Settings'ten renkleri guncelle
(async function updateShiftColors(){
  try{
    var g=null;try{g=window.parent&&window.parent.GECIT;}catch(e){}
    var tenant=(g&&g._tenant)||'1';var tok=(g&&g._token)||null;
    var hd={'Content-Type':'application/json'};if(tok)hd['Authorization']='Bearer '+tok;
    var base=(window.__APIBASE||'');
    var r=await fetch(base+'/api/'+tenant+'/settings',{headers:hd});
    var s=await r.json();
    if(s&&s.shifts){
      s.shifts.forEach(function(sh){
        if(!sh.color)return;
        for(var i=0;i<SHIFTS.length;i++){
          if(SHIFTS[i].code===sh.code){SHIFTS[i].color=sh.color;SHIFTS[i].bg=sh.color+'18';break;}
        }
      });
    }
    if(s&&s.leaves){
      s.leaves.forEach(function(lv){
        if(!lv.color)return;
        for(var i=0;i<SHIFTS.length;i++){
          if(SHIFTS[i].code===lv.code){SHIFTS[i].color=lv.color;SHIFTS[i].bg=lv.color+'18';break;}
        }
      });
    }
    // Legend guncelle
    var lg=document.getElementById('legend');
    if(lg)lg.innerHTML=SHIFTS.filter(function(s){return s.code!=='-';}).map(function(s){
      return '<div class="lg"><i style="background:'+s.color+'30"></i><span style="color:'+s.color+';font-weight:600">'+s.code+'</span></div>';
    }).join('');
  }catch(e){console.log('vplan renk yuklenemedi',e);}
})();""",
            '4b. tpl-vplan: SHIFTS renk guncelleme (IIFE)'
        )
    else:
        print("[INFO] vplan SHIFTS son eleman bulunamadi, elle kontrol edin")
else:
    print("[INFO] vplan SHIFTS anchor bulunamadi, elle kontrol edin")


# =====================================================
# 5. GECIT.shifts RENK PROPAGASYONU (ana v2.html)
# =====================================================

# Ayarlar loadSettings bittiginde GECIT.shifts'e renk aktar
R(
    "renderDeps();renderGorevs();renderShifts();renderLeaves();renderHolidays();\n  markSaved();\n}\n\nloadSettings();",
    """renderDeps();renderGorevs();renderShifts();renderLeaves();renderHolidays();
  markSaved();
  // GECIT.shifts + leaves renklerini aktar
  try{
    var g=window.parent&&window.parent.GECIT;
    if(g&&data.shifts){
      if(g.shifts){data.shifts.forEach(function(ds){if(!ds.color)return;for(var i=0;i<g.shifts.length;i++){if(g.shifts[i].code===ds.code){g.shifts[i].c=ds.color;break;}}});}
      g._settingsColors={shifts:{},leaves:{}};
      data.shifts.forEach(function(s){if(s.color)g._settingsColors.shifts[s.code]=s.color;});
      if(data.leaves)data.leaves.forEach(function(l){if(l.color)g._settingsColors.leaves[l.code]=l.color;});
    }
  }catch(e){}
}

loadSettings();""",
    '5. GECIT.shifts renk propagasyonu'
)


# =====================================================
# KAYIT
# =====================================================
with open(V2, 'w', encoding='utf-8') as f:
    f.write(src)

print(f'\n{"="*50}')
print(f'BASARILI: {ok} degisiklik uygulandi')
if fail:
    print(f'BASARISIZ: {fail} degisiklik uygulanamadi')
print(f'Dosya: {V2}')
print(f'Yedek: {V2}.bak-color')
print(f'\nSonraki adim: pm2 restart gecit-backend')
