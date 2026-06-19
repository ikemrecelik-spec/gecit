for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s=open(fn,encoding='utf-8').read()

    # 1) SGK cikis kodlari - select'i guncelle
    old_select = '''<select id="cikis-kodu">
      <option value="">— Seçiniz —</option>
      <option>İstifa</option>
      <option>İşveren tarafından çıkarıldı</option>
      <option>Sözleşme sona erdi</option>
      <option>Emeklilik</option>
      <option>Karşılıklı anlaşma</option>
      <option>Diğer</option>
    </select>'''
    new_select = '''<select id="cikis-kodu">
      <option value="">— Seçiniz —</option>
      <option value="03">03 - Belirsiz süreli iş sözleşmesinin işveren tarafından feshi</option>
      <option value="04">04 - Belirli süreli iş sözleşmesinin sona ermesi</option>
      <option value="05">05 - Emeklilik (yaşlılık) veya toptan ödeme nedeniyle</option>
      <option value="08">08 - Emeklilik için yaş dışında diğer şartların tamamlanması</option>
      <option value="10">10 - Vazife malullüğü</option>
      <option value="12">12 - Askerlik</option>
      <option value="13">13 - Kadın işçinin evlenmesi</option>
      <option value="14">14 - Erken emeklilik</option>
      <option value="15">15 - Toplu işçi çıkarma</option>
      <option value="16">16 - Sözleşme sona ermeden sigortalının ölümü</option>
      <option value="17">17 - İşçi tarafından zorlayıcı sebeple fesih</option>
      <option value="18">18 - İşçi tarafından sağlık sebebiyle fesih</option>
      <option value="19">19 - İşveren tarafından zorlayıcı sebeple fesih</option>
      <option value="20">20 - İşveren tarafından sağlık sebebiyle fesih</option>
      <option value="22">22 - Diğer nedenler</option>
      <option value="23">23 - İşçi tarafından sözleşmenin haklı nedenle feshi</option>
      <option value="24">24 - İşveren tarafından haklı nedenle fesih</option>
      <option value="25">25 - İşçi tarafından zorlayıcı/ahlak-iyiniyet kuralları nedeniyle fesih</option>
      <option value="34">34 - İşyerinin kapanması</option>
    </select>'''
    found_select = old_select in s
    s = s.replace(old_select, new_select)

    # 2) tablo basliklarina cikis tarihi/kodu ekle (sadece islem cikan goruntulemede gosterecegiz - basit yontem: status sutununun yanina ekstra bilgi)
    old_row_td = '''return '<tr data-tc="'+e.tc+'">'+
        '<td class="mono">'+(e.sicil||'—')+'</td>'+
        '<td><div class="who"><div class="av">'+ini(e.ad)+'</div><div><b>'+(e.ad||'')+'</b></div></div></td>'+
        '<td>'+(e.dep||'—')+'</td><td>'+(e.gorev||'—')+'</td>'+
        '<td class="mono" style="font-size:11px">'+((e.tc||'').slice(0,3)+'••••'+(e.tc||'').slice(-2))+'</td>'+
        '<td>'+dev+'</td>'+
        '<td><span class="pill '+(e.status==='aktif'?'p-aktif':'p-cikan')+'">'+(e.status==='aktif'?'Aktif':'Çıkan')+'</span></td>'+
        '</tr>';'''
    new_row_td = '''var statusCell=(e.status==='aktif')?('<span class="pill p-aktif">Aktif</span>'):('<span class="pill p-cikan">Çıkan</span>'+(e.cikis_tarihi?('<div style="font-size:10.5px;color:var(--muted);margin-top:3px">'+e.cikis_tarihi+(e.cikis_kodu?(' · '+e.cikis_kodu):'')+'</div>'):''));
      return '<tr data-tc="'+e.tc+'">'+
        '<td class="mono">'+(e.sicil||'—')+'</td>'+
        '<td><div class="who"><div class="av">'+ini(e.ad)+'</div><div><b>'+(e.ad||'')+'</b></div></div></td>'+
        '<td>'+(e.dep||'—')+'</td><td>'+(e.gorev||'—')+'</td>'+
        '<td class="mono" style="font-size:11px">'+((e.tc||'').slice(0,3)+'••••'+(e.tc||'').slice(-2))+'</td>'+
        '<td>'+dev+'</td>'+
        '<td>'+statusCell+'</td>'+
        '</tr>';'''
    found_row = old_row_td in s
    s = s.replace(old_row_td, new_row_td)

    # 3) Cihaz & Belgeler sekmesinde cikis bilgilerini de gosterelim (openEdit icine ekleme)
    old_device_show = "document.getElementById('d-device').textContent=e.device?('Bağlı · '+e.device):'Bağlı değil';"
    new_device_show = """document.getElementById('d-device').textContent=e.device?('Bağlı · '+e.device):'Bağlı değil';
  var exitBox=document.getElementById('exit-info');
  if(exitBox){
    if(e.status!=='aktif'&&e.cikis_tarihi){exitBox.style.display='block';exitBox.innerHTML='<b style=\\"color:var(--danger);font-size:12.5px\\">İşten çıkış bilgisi</b><div style=\\"font-size:12px;color:var(--muted);margin-top:6px;line-height:1.6\\">Tarih: '+e.cikis_tarihi+'<br>Kod: '+(e.cikis_kodu||'—')+'<br>Not: '+(e.cikis_not||'—')+'</div>';}
    else{exitBox.style.display='none';}
  }"""
    found_device = old_device_show in s
    s = s.replace(old_device_show, new_device_show)

    # 4) exit-info kutusunu HTML'e ekle (devbox'tan sonra)
    old_devbox_end = '''<div style="color:var(--muted);font-size:11.5px;line-height:1.5">Hesap tek telefona kilitlidir. KVKK gereği biyometrik veri tutulmaz; doğrulama QR + cihaz eşleştirme ile yapılır.</div>
      </div>'''
    new_devbox_end = '''<div style="color:var(--muted);font-size:11.5px;line-height:1.5">Hesap tek telefona kilitlidir. KVKK gereği biyometrik veri tutulmaz; doğrulama QR + cihaz eşleştirme ile yapılır.</div>
      </div>
      <div class="devbox" id="exit-info" style="display:none;border-color:var(--danger)"></div>'''
    found_devbox = old_devbox_end in s
    s = s.replace(old_devbox_end, new_devbox_end)

    # 5) Geri al (reactivate) icin de tarih sorma modali ekleyelim
    old_reactivate = """async function reactivateEmp(){
  if(!curEdit)return;
  if(!confirm(curEdit.ad+' tekrar aktif edilsin mi? İşe devam edebilecek.'))return;
  try{
    await req('/employees/'+curEdit.tc+'/status',{method:'POST',body:{status:'aktif'}});
    toast('Personel tekrar aktif edildi');
    closeDrawer();loadEmployees();
  }catch(e){toast(e.message);}
}"""
    new_reactivate = """function reactivateEmp(){
  if(!curEdit)return;
  document.getElementById('geri-tarihi').value=new Date().toISOString().slice(0,10);
  document.getElementById('geri-ov').style.display='block';
  document.getElementById('geri-modal').style.display='flex';
}
async function confirmReactivate(){
  if(!curEdit)return;
  var tarih=document.getElementById('geri-tarihi').value;
  try{
    await req('/employees/'+curEdit.tc,{method:'PUT',body:{giris:tarih}});
    await req('/employees/'+curEdit.tc+'/status',{method:'POST',body:{status:'aktif'}});
    toast('Personel tekrar aktif edildi');
    document.getElementById('geri-ov').style.display='none';
    document.getElementById('geri-modal').style.display='none';
    closeDrawer();loadEmployees();
  }catch(e){toast(e.message);}
}"""
    found_reactivate = old_reactivate in s
    s = s.replace(old_reactivate, new_reactivate)

    # 6) Geri al modal HTML ekle
    old_toast_marker = '<div class="toast" id="toast"></div>'
    if old_toast_marker in s and 'geri-modal' not in s:
        REACT_MODAL = '''<div class="ov" id="geri-ov" style="display:none;z-index:80"></div>
<div id="geri-modal" style="display:none;position:fixed;inset:0;z-index:81;align-items:center;justify-content:center">
  <div style="background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:24px;width:380px;max-width:92vw;box-shadow:var(--shadow)">
    <h3 style="font-family:Space Grotesk;font-size:16px;margin:0 0 16px">Tekrar İşe Başlama</h3>
    <div class="blk"><label>İşe yeniden başlama tarihi</label><input id="geri-tarihi" type="date"></div>
    <div style="display:flex;gap:10px;justify-content:flex-end;margin-top:16px">
      <button class="ghost" id="geri-cancel">İptal</button>
      <button class="save" id="geri-confirm">Aktifleştir</button>
    </div>
  </div>
</div>
''' + old_toast_marker
        s = s.replace(old_toast_marker, REACT_MODAL)

    # 7) Event listenerlari ekle
    old_evt2 = "document.getElementById('cikis-confirm').addEventListener('click',confirmQuit);"
    if old_evt2 in s and "geri-confirm').addEventListener" not in s:
        new_evt2 = """document.getElementById('cikis-confirm').addEventListener('click',confirmQuit);
document.getElementById('geri-cancel').addEventListener('click',function(){document.getElementById('geri-ov').style.display='none';document.getElementById('geri-modal').style.display='none';});
document.getElementById('geri-ov').addEventListener('click',function(){document.getElementById('geri-ov').style.display='none';document.getElementById('geri-modal').style.display='none';});
document.getElementById('geri-confirm').addEventListener('click',confirmReactivate);"""
        s = s.replace(old_evt2, new_evt2)

    open(fn,encoding='utf-8',mode='w').write(s)
    print(fn,'| select:',found_select,'| row:',found_row,'| device:',found_device,'| devbox:',found_devbox,'| reactivate:',found_reactivate)
