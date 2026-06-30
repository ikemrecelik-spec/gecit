import re

# Orijinal dosyadan eksik template'leri cikart
orig = open('/tmp/original.html', encoding='utf-8').read()

missing = ['tpl-dashboard', 'tpl-sicil', 'tpl-roller', 'tpl-raporlar', 'tpl-tolerans', 'tpl-vardiya', 'tpl-kapi']

extracted = {}
for tpl_id in missing:
    pattern = re.compile(r'(<template id="' + tpl_id + r'">[\s\S]*?</template>)', re.DOTALL)
    m = pattern.search(orig)
    if m:
        extracted[tpl_id] = m.group(1)
        print(tpl_id, '-> bulundu,', len(m.group(1)), 'karakter')
    else:
        print(tpl_id, '-> BULUNAMADI!')

if len(extracted) != 7:
    print('HATA: Tum template bulunamadi, iptal!')
    exit(1)

# Mevcut v2.html'e ekle
for fn in ['v2.html', 'panel.html', 'gecit-site-v1.html']:
    s = open(fn, encoding='utf-8').read()
    
    # Zaten var mi kontrol et
    already = [t for t in missing if '<template id="'+t+'">' in s]
    if already:
        print(fn, '-> zaten var:', already, '- atlaniyor')
        continue
    
    # tpl-kullanici'den once ekle
    insert_point = '<template id="tpl-kullanici">'
    if insert_point not in s:
        print(fn, '-> tpl-kullanici bulunamadi, atlaniyor')
        continue
    
    # Template'leri birlestir
    all_templates = '\n'.join(extracted[t] for t in missing)
    
    s = s.replace(insert_point, all_templates + '\n' + insert_point)
    open(fn, 'w', encoding='utf-8').write(s)
    
    # Dogrulama
    count = sum(1 for t in missing if '<template id="'+t+'">' in s)
    print(fn, '-> eklendi:', count, 'template')
