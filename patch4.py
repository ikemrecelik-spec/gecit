for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s=open(fn,encoding='utf-8').read()
    
    if 'id="geri-modal"' not in s:
        # cikis-modal'dan hemen sonra ekle
        marker = '''<button class="quit" id="cikis-confirm" style="background:var(--danger);color:#fff;border:0">İşten Çıkar</button>
    </div>
  </div>
</div>'''
        REACT_MODAL = '''
<div class="ov" id="geri-ov" style="display:none;z-index:80"></div>
<div id="geri-modal" style="display:none;position:fixed;inset:0;z-index:81;align-items:center;justify-content:center">
  <div style="background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:24px;width:380px;max-width:92vw;box-shadow:var(--shadow)">
    <h3 style="font-family:Space Grotesk;font-size:16px;margin:0 0 16px">Tekrar İşe Başlama</h3>
    <div class="blk"><label>İşe yeniden başlama tarihi</label><input id="geri-tarihi" type="date"></div>
    <div style="display:flex;gap:10px;justify-content:flex-end;margin-top:16px">
      <button class="ghost" id="geri-cancel">İptal</button>
      <button class="save" id="geri-confirm">Aktifleştir</button>
    </div>
  </div>
</div>'''
        found = marker in s
        if found:
            s = s.replace(marker, marker + REACT_MODAL, 1)
        print(fn, 'marker bulundu:', found)
    else:
        print(fn, 'zaten var')
    
    open(fn,encoding='utf-8',mode='w').write(s)
