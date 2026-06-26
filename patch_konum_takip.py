# 1) Backend - konum uyari endpoint'i ekle
s = open('server.js', encoding='utf-8').read()

old = "app.get('/health'"
new = """// Konum uyari kaydı
app.post('/api/:tenant/location-alert', (req, res) => {
  const t = req.params.tenant;
  const tok = (req.headers.authorization || '').replace('Bearer ', '');
  let session = null;
  try { const row = sessionsDb.prepare('SELECT data FROM sessions WHERE tok=?').get(tok); if(row) session = JSON.parse(row.data); } catch(e) {}
  if (!session || session.role !== 'personnel') return res.status(401).json({error:'Yetkisiz'});
  const { lat, lng, dist } = req.body || {};
  const tc = session.tc;
  const emp = D.getAccount(t, tc);
  if (!emp) return res.status(404).json({error:'Personel bulunamadi'});
  // att_approvals tablosuna konum uyarisi ekle
  try {
    D.db.prepare('INSERT INTO att_approvals (tenant_id,att_id,tc,day,type,status,note,created) VALUES (?,?,?,?,?,?,?,?)').run(
      t, 0, tc, D.todayStr(), 'konum_uyari', 'beklemede',
      'Personel tesis disinda tespit edildi. Mesafe: '+Math.round(dist||0)+'m', Date.now()
    );
    broadcast(t, 'approvals');
  } catch(e) {}
  res.json({ok:true});
});

app.get('/health'"""

print('location-alert bulundu:', old in s)
s = s.replace(old, new)
open('server.js', 'w', encoding='utf-8').write(s)
print('server.js OK')

# 2) Mobil - periyodik konum kontrolü ekle
m = open('gecit-mobil.html', encoding='utf-8').read()

old2 = "function logout(){"
new2 = """// Periyodik konum takibi - 5 dk'da bir
var locationTimer=null;
function startLocationTracking(){
  if(locationTimer)return;
  locationTimer=setInterval(async function(){
    if(!token||!meInfo)return;
    // Icerideysek (giris var, cikis yok) konum kontrol et
    if(!curOpen)return;
    try{
      var settings=await api('/settings').catch(function(){return {};});
      var geo=settings&&settings.general;
      if(!geo||!geo.lat||!geo.lng)return;
      var radius=geo.radius||200;
      navigator.geolocation.getCurrentPosition(function(pos){
        var R=6371000;
        var dLat=(pos.coords.latitude-geo.lat)*Math.PI/180;
        var dLng=(pos.coords.longitude-geo.lng)*Math.PI/180;
        var a=Math.sin(dLat/2)*Math.sin(dLat/2)+Math.cos(geo.lat*Math.PI/180)*Math.cos(pos.coords.latitude*Math.PI/180)*Math.sin(dLng/2)*Math.sin(dLng/2);
        var dist=R*2*Math.atan2(Math.sqrt(a),Math.sqrt(1-a));
        if(dist>radius){
          // Uyari gonder
          api('/location-alert',{method:'POST',auth:true,body:{lat:pos.coords.latitude,lng:pos.coords.longitude,dist:dist}}).catch(function(){});
          toast('Uyari: Tesis siniri disinda tespit edildiniz!');
        }
      },function(){},{timeout:10000,maximumAge:60000});
    }catch(e){}
  },5*60*1000); // 5 dakika
}

function stopLocationTracking(){
  if(locationTimer){clearInterval(locationTimer);locationTimer=null;}
}

function logout(){"""
found2 = old2 in m
m = m.replace(old2, new2)

# enterApp icinde tracking baslat
old3 = "function enterApp(){"
new3 = """function enterApp(){
  startLocationTracking();"""
# sadece ekle degistirme
old3_safe = "function enterApp(){"
found3 = old3_safe in m
if found3:
    m = m.replace(old3_safe, new3, 1)

# logout icinde tracking durdur
old4 = "function logout(){token=null;"
new4 = "function logout(){stopLocationTracking();token=null;"
found4 = old4 in m
m = m.replace(old4, new4)

open('gecit-mobil.html', 'w', encoding='utf-8').write(m)
print('mobil -> tracking:', found2, '| enterApp:', found3, '| logout:', found4)
