s = open('gecit-mobil.html', encoding='utf-8').read()

old = """async function recordPunch(qr){try{var res=await api('/attendance/punch',{method:'POST',auth:true,body:{qr:qr}});"""

new = """async function recordPunch(qr){
  // Geofence kontrolu
  try{
    var settings=await api('/settings').catch(function(){return {};});
    var geo=settings&&settings.general;
    if(geo&&geo.lat&&geo.lng){
      var radius=geo.radius||200;
      await new Promise(function(resolve,reject){
        if(!navigator.geolocation){resolve();return;}
        navigator.geolocation.getCurrentPosition(function(pos){
          var R=6371000;
          var dLat=(pos.coords.latitude-geo.lat)*Math.PI/180;
          var dLng=(pos.coords.longitude-geo.lng)*Math.PI/180;
          var a=Math.sin(dLat/2)*Math.sin(dLat/2)+Math.cos(geo.lat*Math.PI/180)*Math.cos(pos.coords.latitude*Math.PI/180)*Math.sin(dLng/2)*Math.sin(dLng/2);
          var dist=R*2*Math.atan2(Math.sqrt(a),Math.sqrt(1-a));
          if(dist>radius){
            reject(new Error('Konum dogrulama basarisiz. Tesis siniri disinda gorununuyorsunuz ('+Math.round(dist)+'m).'));
          } else {
            resolve();
          }
        },function(err){
          // Konum alinamazsa uyar ama engelleme
          resolve();
        },{timeout:5000,maximumAge:10000});
      });
    }
  }catch(geoErr){
    if(geoErr.message&&geoErr.message.indexOf('Konum')>=0){
      document.getElementById('scan-err').textContent=geoErr.message;
      toast(geoErr.message);
      document.getElementById('ov-scan').classList.remove('on');
      return;
    }
  }
  try{var res=await api('/attendance/punch',{method:'POST',auth:true,body:{qr:qr}});"""

print('bulundu:', old in s)
s = s.replace(old, new)
open('gecit-mobil.html', 'w', encoding='utf-8').write(s)
print('OK')
