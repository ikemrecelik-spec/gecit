# -*- coding: utf-8 -*-
# Yeni tpl-ayarlar'i v2.html'e monte eder (eskisini degistirir)
import re, sys

V2 = '/home/ubuntu/gecit-backend/public/v2.html'
YENI = '/home/ubuntu/gecit-backend/tpl-ayarlar-yeni.html'

s = open(V2, encoding='utf-8').read()
yeni = open(YENI, encoding='utf-8').read().strip()

if 'ay-tenant-name' in s:
    print("Yeni ayarlar zaten monte edilmis - dokunulmadi")
    sys.exit()

# Eski template blogunu bul: <template id="tpl-ayarlar"> ... </template>
start = s.find('<template id="tpl-ayarlar">')
if start == -1:
    print("HATA: eski tpl-ayarlar bulunamadi")
    sys.exit(1)
end = s.find('</template>', start)
if end == -1:
    print("HATA: kapanis bulunamadi")
    sys.exit(1)
end += len('</template>')

eski_boyut = end - start
print(f"Eski tpl-ayarlar: {eski_boyut} karakter (pozisyon {start}-{end})")
print(f"Yeni tpl-ayarlar: {len(yeni)} karakter")

s2 = s[:start] + yeni + s[end:]
open(V2, 'w', encoding='utf-8').write(s2)
print("KAYDEDILDI - ayarlar modulu yenilendi")
