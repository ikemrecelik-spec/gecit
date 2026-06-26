for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    old = '        <div class="field"><label>Adres</label><textarea id="g-address" rows="2" placeholder="A\u00e7\u0131k adres"></textarea></div>\n      </div>\n    </section>\n    <!-- B\u00d6L\u00dcM & G\u00d6REV -->'
    
    new = '''        <div class="field"><label>Adres</label><textarea id="g-address" rows="2" placeholder="A\u00e7\u0131k adres"></textarea></div>
        <div style="background:var(--panel-2);border:1px solid var(--line);border-radius:10px;padding:14px;margin-top:8px">
          <h3 style="font-size:13px;font-weight:600;margin:0 0 10px;color:var(--text)">Geofencing \u2014 Konum Do\u011frulama</h3>
          <p style="font-size:12px;color:var(--muted);margin:0 0 12px">Mobil QR okutma sadece bu koordinatlar i\u00e7inde \u00e7al\u0131\u015f\u0131r. Bo\u015f b\u0131rak\u0131l\u0131rsa konum kontrol\u00fc yap\u0131lmaz.</p>
          <div class="field-row">
            <div class="field"><label>Enlem (Latitude)</label><input id="g-lat" placeholder="36.7782" type="number" step="0.0001"></div>
            <div class="field"><label>Boylam (Longitude)</label><input id="g-lng" placeholder="31.3896" type="number" step="0.0001"></div>
          </div>
          <div class="field"><label>Yar\u0131\u00e7ap (Metre) \u2014 Varsay\u0131lan 200m</label><input id="g-radius" placeholder="200" type="number" min="50" max="2000"></div>
          <button class="btn btn-ghost" style="margin-top:4px;font-size:12px" onclick="window.getMyLocation()">Mevcut Konumumu Kullan</button>
        </div>
      </div>
    </section>
    <!-- B\u00d6L\u00dcM & G\u00d6REV -->'''
    
    found = old in s
    s = s.replace(old, new)
    
    # Settings save'e lat/lng/radius ekle
    old2 = "    data.general={\n      name: document.getElementById('g-name')?.value||'',\n      city: document.getElementById('g-city')?.value||'',\n      district: document.getElementById('g-district')?.value||'',\n      phone: document.getElementById('g-phone')?.value||'',\n      address: document.getElementById('g-address')?.value||''"
    new2 = "    data.general={\n      name: document.getElementById('g-name')?.value||'',\n      city: document.getElementById('g-city')?.value||'',\n      district: document.getElementById('g-district')?.value||'',\n      phone: document.getElementById('g-phone')?.value||'',\n      address: document.getElementById('g-address')?.value||'',\n      lat: parseFloat(document.getElementById('g-lat')?.value)||null,\n      lng: parseFloat(document.getElementById('g-lng')?.value)||null,\n      radius: parseInt(document.getElementById('g-radius')?.value)||200"
    found2 = old2 in s
    s = s.replace(old2, new2)
    
    # Settings load'a lat/lng/radius ekle
    old3 = "      document.getElementById('g-address').value=data.general.address||'';"
    new3 = "      document.getElementById('g-address').value=data.general.address||'';\n      if(document.getElementById('g-lat'))document.getElementById('g-lat').value=data.general.lat||'';\n      if(document.getElementById('g-lng'))document.getElementById('g-lng').value=data.general.lng||'';\n      if(document.getElementById('g-radius'))document.getElementById('g-radius').value=data.general.radius||200;"
    found3 = old3 in s
    s = s.replace(old3, new3)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> alan:', found, '| save:', found2, '| load:', found3)
