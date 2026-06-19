for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s=open(fn,encoding='utf-8').read()
    
    # tpl-sicil template'ini bul
    start = s.index('<template id="tpl-sicil">')
    end = s.index('</template>', start)
    chunk = s[start:end]
    
    if 'id="geri-modal"' not in chunk:
        # toast div'inden hemen once ekle (template icinde)
        old_toast = '<div class="toast" id="toast"></div>'
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
'''
        if old_toast in chunk:
            new_chunk = chunk.replace(old_toast, REACT_MODAL + old_toast, 1)
            s = s[:start] + new_chunk + s[end:]
            print(fn, 'eklendi (toast oncesi)')
        else:
            print(fn, 'TOAST BULUNAMADI - chunk icinde')
    else:
        print(fn, 'zaten var')
    
    open(fn,encoding='utf-8',mode='w').write(s)
