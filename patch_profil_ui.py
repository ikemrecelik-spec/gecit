for fn in ['v2.html','panel.html','gecit-site-v1.html']:
    s = open(fn, encoding='utf-8').read()
    
    # Profil menusunu guncelle
    old = """          <div id="profil-menu" style="display:none;position:absolute;top:65px;right:16px;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:8px;z-index:99;box-shadow:0 16px 40px rgba(0,0,0,.55);min-width:240px">
            <div style="padding:12px 14px 10px;border-bottom:1px solid var(--line);margin-bottom:6px">
              <div style="display:flex;align-items:center;gap:10px">
                <div class="av" id="profil-menu-av" style="background:var(--amber);width:40px;height:40px;border-radius:10px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:14px;color:#1a1205;flex:0 0 auto">EÇ</div>
                <div><div id="profil-menu-ad" style="font-weight:700;font-size:14px">Emre Çelik</div><div id="profil-menu-rol" style="color:var(--muted);font-size:12px">İK / Yönetici</div></div>
              </div>
            </div>
            <div style="padding:4px 8px 6px;font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.3px">Tema</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;padding:0 4px;margin-bottom:6px">
              <div class="tema-item" data-tema="dark" onclick="setTema('dark')" style="text-align:center;font-size:11px">🌑 Koyu</div>
              <div class="tema-item" data-tema="light" onclick="setTema('light')" style="text-align:center;font-size:11px">☀️ Açık</div>
              <div class="tema-item" data-tema="navy" onclick="setTema('navy')" style="text-align:center;font-size:11px">🌊 Lacivert</div>
              <div class="tema-item" data-tema="green" onclick="setTema('green')" style="text-align:center;font-size:11px">🌿 Yeşil</div>
              <div class="tema-item" data-tema="bordo" onclick="setTema('bordo')" style="text-align:center;font-size:11px">🍷 Bordo</div>
              <div class="tema-item" data-tema="purple" onclick="setTema('purple')" style="text-align:center;font-size:11px">💜 Mor</div>
              <div class="tema-item" data-tema="ocean" onclick="setTema('ocean')" style="text-align:center;font-size:11px">🏄 Okyanus</div>
            </div>
            <div style="border-top:1px solid var(--line);margin:4px 0 6px"></div>
            <div style="padding:8px 12px;border-radius:8px;cursor:pointer;font-size:13px;display:flex;align-items:center;gap:8px;color:var(--danger)" onclick="doLogout()">
              <span>⎋</span> Çıkış Yap
            </div>
          </div>"""
    
    new = """          <div id="profil-menu" style="display:none;position:absolute;top:65px;right:16px;background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:0;z-index:99;box-shadow:0 20px 60px rgba(0,0,0,.6);min-width:280px;overflow:hidden">
            <!-- Profil basligi -->
            <div style="padding:16px;background:linear-gradient(135deg,rgba(242,181,59,.15),rgba(27,49,62,.5));border-bottom:1px solid var(--line)">
              <div style="display:flex;align-items:center;gap:12px">
                <div class="av" id="profil-menu-av" style="background:linear-gradient(135deg,var(--amber),#d99a1f);width:46px;height:46px;border-radius:12px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:16px;color:#1a1205;flex:0 0 auto;box-shadow:0 4px 12px rgba(242,181,59,.3)">EÇ</div>
                <div style="flex:1;min-width:0">
                  <div id="profil-menu-ad" style="font-weight:700;font-size:14px;font-family:'Space Grotesk'">Emre Çelik</div>
                  <div id="profil-menu-email" style="color:var(--muted);font-size:11.5px;margin-top:2px">-</div>
                  <div id="profil-menu-rol" style="color:var(--amber);font-size:11px;font-weight:600;margin-top:2px">İK / Yönetici</div>
                </div>
              </div>
            </div>
            <!-- Menu itemlari -->
            <div style="padding:8px">
              <div onclick="openProfilDuzenle()" style="padding:10px 12px;border-radius:9px;cursor:pointer;font-size:13px;display:flex;align-items:center;gap:10px;color:var(--text)">
                <span style="width:20px;text-align:center">✏️</span> Profili Düzenle
              </div>
              <div onclick="openSifreDegistir()" style="padding:10px 12px;border-radius:9px;cursor:pointer;font-size:13px;display:flex;align-items:center;gap:10px;color:var(--text)">
                <span style="width:20px;text-align:center">🔑</span> Şifre Değiştir
              </div>
              <div style="margin:6px 0;border-top:1px solid var(--line)"></div>
              <div style="padding:6px 8px 4px;font-size:10.5px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.4px">Tema</div>
              <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:3px;padding:0 4px;margin-bottom:6px">
                <div class="tema-item" data-tema="dark" onclick="setTema('dark')" style="text-align:center;font-size:11px;padding:6px 4px">🌑 Koyu</div>
                <div class="tema-item" data-tema="light" onclick="setTema('light')" style="text-align:center;font-size:11px;padding:6px 4px">☀️ Açık</div>
                <div class="tema-item" data-tema="navy" onclick="setTema('navy')" style="text-align:center;font-size:11px;padding:6px 4px">🌊 Lacivert</div>
                <div class="tema-item" data-tema="green" onclick="setTema('green')" style="text-align:center;font-size:11px;padding:6px 4px">🌿 Yeşil</div>
                <div class="tema-item" data-tema="bordo" onclick="setTema('bordo')" style="text-align:center;font-size:11px;padding:6px 4px">🍷 Bordo</div>
                <div class="tema-item" data-tema="purple" onclick="setTema('purple')" style="text-align:center;font-size:11px;padding:6px 4px">💜 Mor</div>
                <div class="tema-item" data-tema="ocean" onclick="setTema('ocean')" style="text-align:center;font-size:11px;padding:6px 4px">🏄 Okyanus</div>
              </div>
              <div style="margin:6px 0;border-top:1px solid var(--line)"></div>
              <div onclick="doLogout()" style="padding:10px 12px;border-radius:9px;cursor:pointer;font-size:13px;display:flex;align-items:center;gap:10px;color:var(--danger)">
                <span style="width:20px;text-align:center">⎋</span> Çıkış Yap
              </div>
            </div>
          </div>
          <!-- Profil Duzenle Modal -->
          <div id="profil-ov" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:200"></div>
          <div id="profil-modal" style="display:none;position:fixed;inset:0;z-index:201;align-items:center;justify-content:center">
            <div style="background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:24px;width:380px;max-width:92vw;box-shadow:0 20px 60px rgba(0,0,0,.5)">
              <h3 style="font-family:'Space Grotesk';font-size:16px;margin:0 0 16px">Profili Düzenle</h3>
              <div style="margin-bottom:12px"><label style="font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase;display:block;margin-bottom:4px">Ad Soyad</label><input id="pd-name" style="width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;padding:9px 12px;color:var(--text);font-family:inherit;font-size:13px;outline:none" placeholder="Ad Soyad"></div>
              <div style="margin-bottom:12px"><label style="font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase;display:block;margin-bottom:4px">E-posta</label><input id="pd-email" type="email" style="width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;padding:9px 12px;color:var(--text);font-family:inherit;font-size:13px;outline:none" placeholder="ornek@email.com"></div>
              <div id="pd-err" style="color:var(--danger);font-size:12px;margin-bottom:8px"></div>
              <div style="display:flex;gap:8px;justify-content:flex-end">
                <button onclick="closeProfilModal()" style="padding:8px 14px;border-radius:8px;border:1px solid var(--line);background:var(--panel-2);color:var(--text);font-weight:600;font-size:12px;cursor:pointer">İptal</button>
                <button onclick="saveProfilDuzenle()" style="padding:8px 14px;border-radius:8px;border:0;background:var(--amber);color:#1a1205;font-weight:600;font-size:12px;cursor:pointer">Kaydet</button>
              </div>
            </div>
          </div>
          <!-- Sifre Degistir Modal -->
          <div id="sifre-modal" style="display:none;position:fixed;inset:0;z-index:201;align-items:center;justify-content:center">
            <div style="background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:24px;width:380px;max-width:92vw;box-shadow:0 20px 60px rgba(0,0,0,.5)">
              <h3 style="font-family:'Space Grotesk';font-size:16px;margin:0 0 16px">Şifre Değiştir</h3>
              <div style="margin-bottom:12px"><label style="font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase;display:block;margin-bottom:4px">Mevcut Şifre</label><input id="sp-old" type="password" style="width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;padding:9px 12px;color:var(--text);font-family:inherit;font-size:13px;outline:none" placeholder="••••••"></div>
              <div style="margin-bottom:12px"><label style="font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase;display:block;margin-bottom:4px">Yeni Şifre</label><input id="sp-new" type="password" style="width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;padding:9px 12px;color:var(--text);font-family:inherit;font-size:13px;outline:none" placeholder="••••••"></div>
              <div style="margin-bottom:12px"><label style="font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase;display:block;margin-bottom:4px">Yeni Şifre Tekrar</label><input id="sp-new2" type="password" style="width:100%;background:var(--panel-2);border:1px solid var(--line);border-radius:8px;padding:9px 12px;color:var(--text);font-family:inherit;font-size:13px;outline:none" placeholder="••••••"></div>
              <div id="sp-err" style="color:var(--danger);font-size:12px;margin-bottom:8px"></div>
              <div style="display:flex;gap:8px;justify-content:flex-end">
                <button onclick="closeSifreModal()" style="padding:8px 14px;border-radius:8px;border:1px solid var(--line);background:var(--panel-2);color:var(--text);font-weight:600;font-size:12px;cursor:pointer">İptal</button>
                <button onclick="saveSifreDegistir()" style="padding:8px 14px;border-radius:8px;border:0;background:var(--amber);color:#1a1205;font-weight:600;font-size:12px;cursor:pointer">Değiştir</button>
              </div>
            </div>
          </div>"""
    
    found = old in s
    s = s.replace(old, new)
    
    # Profil fonksiyonlari ekle
    old2 = "  window.toggleProfilMenu=toggleProfilMenu;"
    new2 = """  window.toggleProfilMenu=toggleProfilMenu;
  
  // Profil yukle
  async function loadProfil(){
    try{
      var g=window.GECIT; var tok=g._token;
      var h={'Content-Type':'application/json','Authorization':'Bearer '+tok};
      var r=await fetch('https://gecitpdks.duckdns.org/api/hotel/profile',{headers:h});
      var d=await r.json();
      if(d.name){
        var ini=d.name.trim().split(' ').map(function(p){return p[0]||'';}).join('').slice(0,2).toUpperCase();
        document.getElementById('profil-av').textContent=ini;
        document.getElementById('profil-ad').textContent=d.name;
        document.getElementById('profil-menu-av').textContent=ini;
        document.getElementById('profil-menu-ad').textContent=d.name;
        document.getElementById('profil-menu-email').textContent=d.email||'E-posta girilmemiş';
      }
    }catch(e){}
  }
  
  function openProfilDuzenle(){
    document.getElementById('pd-name').value=document.getElementById('profil-menu-ad').textContent||'';
    document.getElementById('pd-email').value=document.getElementById('profil-menu-email').textContent||'';
    document.getElementById('pd-err').textContent='';
    document.getElementById('profil-ov').style.display='block';
    document.getElementById('profil-modal').style.display='flex';
    document.getElementById('profil-menu').style.display='none';
  }
  function closeProfilModal(){
    document.getElementById('profil-ov').style.display='none';
    document.getElementById('profil-modal').style.display='none';
  }
  async function saveProfilDuzenle(){
    var name=document.getElementById('pd-name').value.trim();
    var email=document.getElementById('pd-email').value.trim();
    if(!name){document.getElementById('pd-err').textContent='Ad Soyad gerekli';return;}
    try{
      var g=window.GECIT; var tok=g._token;
      var h={'Content-Type':'application/json','Authorization':'Bearer '+tok};
      await fetch('https://gecitpdks.duckdns.org/api/hotel/profile',{method:'PUT',headers:h,body:JSON.stringify({name:name,email:email})});
      document.getElementById('profil-menu-ad').textContent=name;
      document.getElementById('profil-ad').textContent=name;
      document.getElementById('profil-menu-email').textContent=email||'E-posta girilmemiş';
      var ini=name.trim().split(' ').map(function(p){return p[0]||'';}).join('').slice(0,2).toUpperCase();
      document.getElementById('profil-av').textContent=ini;
      document.getElementById('profil-menu-av').textContent=ini;
      closeProfilModal();
      showToast('Profil guncellendi');
    }catch(e){document.getElementById('pd-err').textContent='Hata: '+e.message;}
  }
  
  function openSifreDegistir(){
    document.getElementById('sp-old').value='';
    document.getElementById('sp-new').value='';
    document.getElementById('sp-new2').value='';
    document.getElementById('sp-err').textContent='';
    document.getElementById('profil-ov').style.display='block';
    document.getElementById('sifre-modal').style.display='flex';
    document.getElementById('profil-menu').style.display='none';
  }
  function closeSifreModal(){
    document.getElementById('profil-ov').style.display='none';
    document.getElementById('sifre-modal').style.display='none';
  }
  async function saveSifreDegistir(){
    var oldP=document.getElementById('sp-old').value;
    var newP=document.getElementById('sp-new').value;
    var newP2=document.getElementById('sp-new2').value;
    if(!oldP||!newP){document.getElementById('sp-err').textContent='Tum alanlar gerekli';return;}
    if(newP!==newP2){document.getElementById('sp-err').textContent='Yeni sifreler eslesmedi';return;}
    if(newP.length<6){document.getElementById('sp-err').textContent='Sifre en az 6 karakter olmali';return;}
    try{
      var g=window.GECIT; var tok=g._token;
      var h={'Content-Type':'application/json','Authorization':'Bearer '+tok};
      var r=await fetch('https://gecitpdks.duckdns.org/api/hotel/password',{method:'PUT',headers:h,body:JSON.stringify({oldPass:oldP,newPass:newP})});
      var d=await r.json();
      if(!r.ok)throw new Error(d.error||'Hata');
      closeSifreModal();
      showToast('Sifre degistirildi');
    }catch(e){document.getElementById('sp-err').textContent=e.message;}
  }
  
  document.getElementById('profil-ov').addEventListener('click',function(){closeProfilModal();closeSifreModal();});
  window.openProfilDuzenle=openProfilDuzenle;
  window.closeProfilModal=closeProfilModal;
  window.saveProfilDuzenle=saveProfilDuzenle;
  window.openSifreDegistir=openSifreDegistir;
  window.closeSifreModal=closeSifreModal;
  window.saveSifreDegistir=saveSifreDegistir;"""
    
    found2 = old2 in s
    s = s.replace(old2, new2)
    
    # Login sonrasi profil yukle
    old3 = "      loadApprovals&&loadApprovals();"
    new3 = "      loadApprovals&&loadApprovals();\n      setTimeout(loadProfil,500);"
    found3 = old3 in s
    s = s.replace(old3, new3)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> menu:', found, '| fn:', found2, '| load:', found3)
