# -*- coding: utf-8 -*-
# F5 sonrasi token varsa profil+otel adi+veri yukle
p='/home/ubuntu/gecit-backend/public/v2.html'
s=open(p,encoding='utf-8').read()

if 'PROFIL_YUKLE_v1' in s:
    print("Zaten yapilmis")
    raise SystemExit

# kalkandaki if(!hasTok){...} blogunun SONUNA else ekle
# Once tam blogu bul (newline'lar cok, esnek eslesme icin normalize etmeyecegiz - tam metni kullan)
old="""    if(!hasTok){

      var appEl = document.getElementById('app');

      var loginEl = document.getElementById('login');

      var saEl = document.getElementById('superadmin');

      if(appEl) appEl.style.display = 'none';

      if(loginEl) loginEl.style.display = 'grid';

      if(saEl) saEl.style.display = 'none';

    }

  }catch(e){ console.warn('KALKAN hata:', e); }"""

new="""    if(!hasTok){

      var appEl = document.getElementById('app');

      var loginEl = document.getElementById('login');

      var saEl = document.getElementById('superadmin');

      if(appEl) appEl.style.display = 'none';

      if(loginEl) loginEl.style.display = 'grid';

      if(saEl) saEl.style.display = 'none';

    } else {
      /* PROFIL_YUKLE_v1: token varsa profil + otel adi + veri yukle */
      try{
        var G=window.GECIT;
        if(G && G._token && G._tenant){
          var _h={'Content-Type':'application/json','Authorization':'Bearer '+G._token};
          /* otel adi */
          fetch((window.__APIBASE||location.origin)+'/api/'+G._tenant+'/settings',{headers:_h})
            .then(function(r){return r.json();}).then(function(sd){
              var nm=(sd&&sd.general&&sd.general.name)||G._tenant;
              var hd=document.getElementById('hotel-name'); if(hd)hd.textContent=nm;
            }).catch(function(){});
          /* profil */
          if(typeof loadProfil==='function')loadProfil();
          /* veri */
          if(G.load)G.load().then(function(){G.refresh&&G.refresh();});
          if(G.connectWS)G.connectWS();
        }
      }catch(pe){ console.warn('profil yukleme:', pe); }
    }

  }catch(e){ console.warn('KALKAN hata:', e); }"""

n=s.count(old)
print("Eslesme:",n)
if n==1:
    open(p,'w',encoding='utf-8').write(s.replace(old,new))
    print("KAYDEDILDI - PROFIL_YUKLE_v1")
else:
    print("HATA - iptal ("+str(n)+")")
