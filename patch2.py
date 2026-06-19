for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s=open(fn,encoding='utf-8').read()
    
    # 1) Cikis modal HTML'i ekle - toast'tan once
    old_modal_marker = '<div class="toast" id="toast"></div>'
    if old_modal_marker in s and 'cikis-modal' not in s:
        QUIT_MODAL = '''<div class="ov" id="cikis-ov" style="display:none;z-index:80"></div>
<div id="cikis-modal" style="display:none;position:fixed;inset:0;z-index:81;align-items:center;justify-content:center">
  <div style="background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:24px;width:420px;max-width:92vw;box-shadow:var(--shadow)">
    <h3 style="font-family:Space Grotesk;font-size:16px;margin:0 0 16px">İşten Çıkış Bilgileri</h3>
    <div class="blk"><label>Çıkış tarihi</label><input id="cikis-tarihi" type="date"></div>
    <div class="blk"><label>Çıkış kodu</label><select id="cikis-kodu">
      <option value="">— Seçiniz —</option>
      <option>İstifa</option>
      <option>İşveren tarafından çıkarıldı</option>
      <option>Sözleşme sona erdi</option>
      <option>Emeklilik</option>
      <option>Karşılıklı anlaşma</option>
      <option>Diğer</option>
    </select></div>
    <div class="blk"><label>Not</label><input id="cikis-not" placeholder="İsteğe bağlı açıklama"></div>
    <div style="display:flex;gap:10px;justify-content:flex-end;margin-top:16px">
      <button class="ghost" id="cikis-cancel">İptal</button>
      <button class="quit" id="cikis-confirm" style="background:var(--danger);color:#fff;border:0">İşten Çıkar</button>
    </div>
  </div>
</div>
''' + old_modal_marker
        s = s.replace(old_modal_marker, QUIT_MODAL)
    
    # 2) quitEmp fonksiyonunu modal acacak sekilde degistir
    old_quit = """async function quitEmp(){
  if(!curEdit)return;
  if(!confirm(curEdit.ad+' işten çıkarılsın mı?'))return;
  try{await req('/employees/'+curEdit.tc+'/status',{method:'POST',body:{status:'pasif'}});toast('İşten çıkarıldı');closeDrawer();loadEmployees();}catch(e){toast(e.message);}
}"""
    new_quit = """function quitEmp(){
  if(!curEdit)return;
  if(curEdit.status==='aktif'){
    document.getElementById('cikis-tarihi').value=new Date().toISOString().slice(0,10);
    document.getElementById('cikis-kodu').value='';
    document.getElementById('cikis-not').value='';
    document.getElementById('cikis-ov').style.display='block';
    document.getElementById('cikis-modal').style.display='flex';
  } else {
    reactivateEmp();
  }
}
async function confirmQuit(){
  if(!curEdit)return;
  var tarih=document.getElementById('cikis-tarihi').value;
  var kodu=document.getElementById('cikis-kodu').value;
  var not_=document.getElementById('cikis-not').value;
  try{
    await req('/employees/'+curEdit.tc+'/status',{method:'POST',body:{status:'pasif',cikis_tarihi:tarih,cikis_kodu:kodu,cikis_not:not_}});
    toast('İşten çıkarıldı');
    document.getElementById('cikis-ov').style.display='none';
    document.getElementById('cikis-modal').style.display='none';
    closeDrawer();loadEmployees();
  }catch(e){toast(e.message);}
}
async function reactivateEmp(){
  if(!curEdit)return;
  if(!confirm(curEdit.ad+' tekrar aktif edilsin mi? İşe devam edebilecek.'))return;
  try{
    await req('/employees/'+curEdit.tc+'/status',{method:'POST',body:{status:'aktif'}});
    toast('Personel tekrar aktif edildi');
    closeDrawer();loadEmployees();
  }catch(e){toast(e.message);}
}"""
    found = old_quit in s
    s = s.replace(old_quit, new_quit)
    
    # 3) d-quit butonunun metnini ve gorunurlugunu durum bazli yap (openEdit icinde)
    old_btn_show = "document.getElementById('d-quit').style.display=e.status==='aktif'?'block':'none';"
    new_btn_show = """document.getElementById('d-quit').style.display='block';
  document.getElementById('d-quit').textContent=e.status==='aktif'?'İşten çıkar':'Geri al (aktifleştir)';
  document.getElementById('d-quit').className=e.status==='aktif'?'quit':'save';
  document.getElementById('d-quit').style.marginRight=e.status==='aktif'?'':'auto';"""
    s = s.replace(old_btn_show, new_btn_show)
    
    # 4) Event listener'lari ekle (sadece yoksa)
    if "cikis-confirm" not in s.split("loadSettings().then")[0] or "addEventListener('click',confirmQuit)" not in s:
        old_evt = "document.getElementById('d-quit').addEventListener('click',quitEmp);"
        new_evt = """document.getElementById('d-quit').addEventListener('click',quitEmp);
document.getElementById('cikis-cancel').addEventListener('click',function(){document.getElementById('cikis-ov').style.display='none';document.getElementById('cikis-modal').style.display='none';});
document.getElementById('cikis-ov').addEventListener('click',function(){document.getElementById('cikis-ov').style.display='none';document.getElementById('cikis-modal').style.display='none';});
document.getElementById('cikis-confirm').addEventListener('click',confirmQuit);"""
        s = s.replace(old_evt, new_evt)
    
    open(fn,encoding='utf-8',mode='w').write(s)
    print(fn, 'quitEmp bulundu:', found)
