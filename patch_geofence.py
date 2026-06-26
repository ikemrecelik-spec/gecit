for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    # 1) Ayarlara koordinat alanlari ekle
    old1 = """        <div class="field"><label>Adres</label><textarea id="g-address" rows="2" placeholder="Açık adres"></textarea></div>
      </div>
    </section>
    <!-- BÖLÜM & GÖREV -->"""
    
    new1 = """        <div class="field"><label>Adres</label><textarea id="g-address" rows="2" placeholder="Açık adres"></textarea></div>
        <div style="background:var(--panel-2);border:1px solid var(--line);border-radius:10px;padding:14px;margin-top:8px">
          <h3 style="font-size:13px;font-weight:600;margin:0 0 10px;color:var(--text)">📍 Geofencing — Konum Doğrulama</h3>
          <p style="font-size:12px;color:var(--muted);margin:0 0 12px">Mobil QR okutma sadece bu koordinatlar içinde çalışır. Boş bırakılırsa konum kontrolü yapılmaz.</p>
          <div class="field-row">
            <div class="field"><label>Enlem (Latitude)</label><input id="g-lat" placeholder="36.7782" type="number" step="0.0001"></div>
            <div class="field"><label>Boylam (Longitude)</label><input id="g-lng" placeholder="31.3896" type="number" step="0.0001"></div>
          </div>
          <div class="field"><label>Yarıçap (Metre) — Varsayılan 200m</label><input id="g-radius" placeholder="200" type="number" min="50" max="2000"></div>
          <button class="btn btn-ghost" id="g-locate-btn" style="margin-top:4px;font-size:12px" onclick="getMyLocation()">📍 Mevcut Konumumu Kullan</button>
        </div>
      </div>
    </section>
    <!-- BÖLÜM & GÖREV -->"""
    
    found1 = old1 in s
    s = s.replace(old1, new1)
    
    # 2) Settings save'e lat/lng/radius ekle
    old2 = """    data.general={
      name: document.getElementById('g-name')?.value||'',
      city: document.getElementById('g-city')?.value||'',
      district: document.getElementById('g-district')?.value||'',
      phone: document.getElementById('g-phone')?.value||'',"""
    new2 = """    data.general={
      name: document.getElementById('g-name')?.value||'',
      city: document.getElementById('g-city')?.value||'',
      district: document.getElementById('g-district')?.value||'',
      phone: document.getElementById('g-phone')?.value||'',
      lat: parseFloat(document.getElementById('g-lat')?.value)||null,
      lng: parseFloat(document.getElementById('g-lng')?.value)||null,
      radius: parseInt(document.getElementById('g-radius')?.value)||200,"""
    found2 = old2 in s
    s = s.replace(old2, new2)
    
    # 3) Settings load'a lat/lng/radius ekle
    old3 = """    if(data.general){
      document.getElementById('g-name').value=data.general.name||'';
      document.getElementById('g-city').value=data.general.city||'';
      document.getElementById('g-district').value=data.general.district||'';
      document.getElementById('g-phone').value=data.general.phone||'';"""
    new3 = """    if(data.general){
      document.getElementById('g-name').value=data.general.name||'';
      document.getElementById('g-city').value=data.general.city||'';
      document.getElementById('g-district').value=data.general.district||'';
      document.getElementById('g-phone').value=data.general.phone||'';
      if(document.getElementById('g-lat'))document.getElementById('g-lat').value=data.general.lat||'';
      if(document.getElementById('g-lng'))document.getElementById('g-lng').value=data.general.lng||'';
      if(document.getElementById('g-radius'))document.getElementById('g-radius').value=data.general.radius||200;"""
    found3 = old3 in s
    s = s.replace(old3, new3)
    
    # 4) getMyLocation fonksiyonu ekle
    old4 = """  window.renderReg=renderReg;"""
    new4 = """  window.getMyLocation=function(){
    if(!navigator.geolocation){alert('Konum desteklenmiyor');return;}
    navigator.geolocation.getCurrentPosition(function(pos){
      document.getElementById('g-lat').value=pos.coords.latitude.toFixed(6);
      document.getElementById('g-lng').value=pos.coords.longitude.toFixed(6);
    },function(){alert('Konum alinamadi');});
  };
  window.renderReg=renderReg;"""
    found4 = old4 in s
    s = s.replace(old4, new4)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> ayar:', found1, '| save:', found2, '| load:', found3, '| fn:', found4)
