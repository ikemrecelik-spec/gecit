NEW_DASHBOARD = r'''<template id="tpl-dashboard">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Genel Bakis</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E1A24;--panel:#14242F;--panel-2:#1B313E;--line:#23414F;--amber:#F2B53B;--mint:#34D9A0;--danger:#FF6B6B;--blue:#6FB1FF;--purple:#C792EA;--text:#EAF2F5;--muted:#8FA6B0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:radial-gradient(1200px 700px at 80% -10%,#16303d,var(--ink) 55%);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;padding:18px 16px 60px}
.topbar{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;flex-wrap:wrap;gap:10px}
.topbar h1{font-family:'Space Grotesk';font-size:18px;font-weight:700;margin:0}
.topbar small{color:var(--muted);font-size:12px}
.refresh-btn{background:var(--panel);border:1px solid var(--line);color:var(--muted);border-radius:8px;padding:6px 12px;font-size:12px;cursor:pointer}
.refresh-btn:hover{color:var(--text);border-color:var(--amber)}
.stat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px;margin-bottom:18px}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px;position:relative;overflow:hidden}
.stat .val{font-family:'Space Grotesk';font-size:32px;font-weight:700;line-height:1;margin-bottom:6px}
.stat .lbl{color:var(--muted);font-size:12px;font-weight:500}
.stat .ic{position:absolute;right:14px;top:14px;font-size:22px;opacity:.3}
.stat.green .val{color:var(--mint)}
.stat.amber .val{color:var(--amber)}
.stat.danger .val{color:var(--danger)}
.stat.blue .val{color:var(--blue)}
.stat.purple .val{color:var(--purple)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:18px}
@media(max-width:700px){.grid2{grid-template-columns:1fr}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.card-head{display:flex;align-items:center;justify-content:space-between;padding:12px 16px;border-bottom:1px solid var(--line)}
.card-head h3{font-family:'Space Grotesk';font-size:14px;font-weight:600;margin:0}
.card-body{padding:14px 16px}
table{width:100%;border-collapse:collapse;font-size:12px}
tbody td{padding:7px 0;border-bottom:1px solid rgba(35,65,79,.3);vertical-align:middle}
tbody tr:last-child td{border:0}
.bar-wrap{height:8px;background:var(--panel-2);border-radius:4px;overflow:hidden;margin-top:4px}
.bar{height:100%;border-radius:4px;background:var(--amber);transition:.4s}
.dep-item{display:flex;align-items:center;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(35,65,79,.3)}
.dep-item:last-child{border:0}
.dep-name{font-size:12.5px;font-weight:500}
.dep-cnt{font-family:'JetBrains Mono';font-size:12px;color:var(--muted)}
.chart-wrap{height:120px;display:flex;align-items:flex-end;gap:6px;padding:0 4px}
.chart-bar-wrap{flex:1;display:flex;flex-direction:column;align-items:center;gap:4px}
.chart-bar{width:100%;border-radius:4px 4px 0 0;background:var(--amber);min-height:4px;transition:.3s}
.chart-bar.danger{background:var(--danger)}
.chart-lbl{font-size:9px;color:var(--muted);text-align:center}
.chart-val{font-size:9px;color:var(--text);text-align:center;font-family:'JetBrains Mono'}
.who{display:flex;align-items:center;gap:8px}
.av{width:26px;height:26px;border-radius:7px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:10px;color:#1a1205;background:var(--amber);flex:0 0 auto}
.pill{display:inline-flex;align-items:center;font-size:10.5px;font-weight:600;padding:2px 7px;border-radius:5px}
.p-ok{background:rgba(52,217,160,.15);color:var(--mint)}
.p-warn{background:rgba(255,107,107,.15);color:var(--danger)}
.p-amber{background:rgba(242,181,59,.15);color:var(--amber)}
.loading{color:var(--muted);font-size:12px;text-align:center;padding:20px}
</style>

<div class="topbar">
  <div>
    <h1>Genel Bakis</h1>
    <small id="dash-date">-</small>
  </div>
  <button class="refresh-btn" id="refresh-btn">&#8635; Yenile</button>
</div>

<!-- STAT KARTLARI -->
<div class="stat-grid">
  <div class="stat green"><div class="val" id="s-aktif">-</div><div class="lbl">Aktif Personel</div><div class="ic">👥</div></div>
  <div class="stat blue"><div class="val" id="s-bugun">-</div><div class="lbl">Bugün Giriş Yapan</div><div class="ic">✅</div></div>
  <div class="stat amber"><div class="val" id="s-iceride">-</div><div class="lbl">Şu An İçeride</div><div class="ic">🏢</div></div>
  <div class="stat danger"><div class="val" id="s-devamsiz">-</div><div class="lbl">Bugün Devamsız</div><div class="ic">❌</div></div>
  <div class="stat purple"><div class="val" id="s-onay">-</div><div class="lbl">Bekleyen Onay</div><div class="ic">⏳</div></div>
  <div class="stat amber"><div class="val" id="s-cikis">-</div><div class="lbl">Çıkış Yapmayan</div><div class="ic">⚠️</div></div>
</div>

<div class="grid2">
  <!-- Son 7 Gun Devamsizlik Grafigi -->
  <div class="card">
    <div class="card-head"><h3>Son 7 Gün Devamsızlık</h3></div>
    <div class="card-body">
      <div class="chart-wrap" id="chart-devamsizlik">
        <div class="loading">Yukleniyor...</div>
      </div>
    </div>
  </div>

  <!-- Departman Bazli Personel -->
  <div class="card">
    <div class="card-head"><h3>Departman Dağılımı</h3></div>
    <div class="card-body">
      <div id="dep-list"><div class="loading">Yukleniyor...</div></div>
    </div>
  </div>
</div>

<div class="grid2">
  <!-- Bugun Gec Girenler -->
  <div class="card">
    <div class="card-head"><h3>Bugün Geç Giriş</h3><span id="gec-cnt" style="color:var(--muted);font-size:11px"></span></div>
    <div class="card-body">
      <table><tbody id="gec-list"><tr><td class="loading">Yukleniyor...</td></tr></tbody></table>
    </div>
  </div>

  <!-- Bekleyen Onaylar -->
  <div class="card">
    <div class="card-head"><h3>Bekleyen Onaylar</h3><span id="onay-cnt" style="color:var(--muted);font-size:11px"></span></div>
    <div class="card-body">
      <table><tbody id="onay-list"><tr><td class="loading">Yukleniyor...</td></tr></tbody></table>
    </div>
  </div>
</div>

<script>
function getG(){try{return window.parent&&window.parent.GECIT||null;}catch(e){return null;}}
async function req(path,opts){
  var g=getG(); var tenant=(g&&g._tenant)||'1'; var tok=(g&&g._token)||null;
  opts=opts||{}; var h={'Content-Type':'application/json'};
  if(tok)h['Authorization']='Bearer '+tok;
  var r=await fetch('https://gecitpdks.duckdns.org/api/'+tenant+path,{method:opts.method||'GET',headers:h,body:opts.body?JSON.stringify(opts.body):undefined});
  var d=null;try{d=await r.json();}catch(e){}
  if(!r.ok)throw new Error((d&&d.error)||('Hata '+r.status));
  return d;
}

var GUNLER=['Paz','Pzt','Sal','Car','Per','Cum','Cmt'];
var AYLAR=['Oca','Sub','Mar','Nis','May','Haz','Tem','Agu','Eyl','Eki','Kas','Ara'];

function isoDate(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function ini(s){var p=(s||'').trim().split(' ');return((p[0]||'')[0]||'')+((p[1]||'')[0]||'');}
function timeMins(g,c){if(!g||!c)return null;var gp=g.split(':').map(Number);var cp=c.split(':').map(Number);var m=(cp[0]*60+cp[1])-(gp[0]*60+gp[1]);if(m<0)m+=1440;return m;}

async function loadDashboard(){
  var now=new Date();
  var today=isoDate(now);
  var dow=now.getDay();
  document.getElementById('dash-date').textContent=now.toLocaleDateString('tr-TR',{weekday:'long',year:'numeric',month:'long',day:'numeric'});

  try{
    // Paralel yükle
    var [emps, attAll, approvals, settings] = await Promise.all([
      req('/employees'),
      req('/attendance'),
      req('/approvals?status=beklemede').catch(function(){return [];}),
      req('/settings').catch(function(){return {};})
    ]);

    var aktif=emps.filter(function(e){return e.status==='aktif';});
    var todayAtt=attAll.filter(function(r){return r.day===today;});
    var girisYapan=todayAtt.filter(function(r){return r.giris;});
    var iceride=todayAtt.filter(function(r){return r.giris&&!r.cikis;});
    var cikisYapan=todayAtt.filter(function(r){return r.giris&&!r.cikis;});

    // Devamsiz - shift planından gelenleri hesapla
    var attReport=await req('/attendance/report?start='+today+'&end='+today).catch(function(){return [];});
    var devamsiz=attReport.filter(function(r){return r.status==='gelmedi';});

    // Stats
    document.getElementById('s-aktif').textContent=aktif.length;
    document.getElementById('s-bugun').textContent=girisYapan.length;
    document.getElementById('s-iceride').textContent=iceride.length;
    document.getElementById('s-devamsiz').textContent=devamsiz.length;
    document.getElementById('s-onay').textContent=approvals.length;
    document.getElementById('s-cikis').textContent=cikisYapan.length;

    // Departman dagilimi
    var depMap={};
    aktif.forEach(function(e){depMap[e.dep]=(depMap[e.dep]||0)+1;});
    var deps=Object.keys(depMap).sort(function(a,b){return depMap[b]-depMap[a];});
    var maxDep=deps.length?depMap[deps[0]]:1;
    document.getElementById('dep-list').innerHTML=deps.slice(0,8).map(function(d){
      var pct=Math.round(depMap[d]/maxDep*100);
      return '<div class="dep-item"><div><div class="dep-name">'+d+'</div><div class="bar-wrap"><div class="bar" style="width:'+pct+'%"></div></div></div><div class="dep-cnt">'+depMap[d]+'</div></div>';
    }).join('')||'<div class="loading">Veri yok</div>';

    // Son 7 gun devamsizlik grafigi
    var days7=[]; var maxVal=1;
    for(var i=6;i>=0;i--){
      var d=new Date(now); d.setDate(d.getDate()-i);
      var ds=isoDate(d);
      var report=await req('/attendance/report?start='+ds+'&end='+ds).catch(function(){return [];});
      var cnt=report.filter(function(r){return r.status==='gelmedi';}).length;
      if(cnt>maxVal)maxVal=cnt;
      days7.push({date:ds,cnt:cnt,dow:d.getDay()});
    }
    document.getElementById('chart-devamsizlik').innerHTML=days7.map(function(x){
      var h=maxVal>0?Math.round(x.cnt/maxVal*100):0;
      return '<div class="chart-bar-wrap">'
        +'<div class="chart-val">'+(x.cnt||'')+'</div>'
        +'<div class="chart-bar'+(x.cnt>5?' danger':'')+'" style="height:'+Math.max(h,4)+'%"></div>'
        +'<div class="chart-lbl">'+GUNLER[x.dow]+'</div>'
        +'</div>';
    }).join('');

    // Gec girisler (bugun, 15 dk tolerans)
    var shiftDefs=(settings&&settings.shifts)||[];
    var gecList=todayAtt.filter(function(r){
      if(!r.giris)return false;
      var shKey=r.vardiya&&r.vardiya.split(' ')[0];
      var shDef=shiftDefs.find(function(s){return s.code===shKey;});
      if(!shDef||!shDef.start)return false;
      var sp=shDef.start.split(':').map(Number);
      var gp=r.giris.split(':').map(Number);
      var diff=(gp[0]*60+gp[1])-(sp[0]*60+sp[1]);
      return diff>15&&diff<720;
    }).slice(0,5);
    document.getElementById('gec-cnt').textContent=gecList.length+' kisi';
    document.getElementById('gec-list').innerHTML=gecList.length?gecList.map(function(r){
      return '<tr><td><div class="who"><div class="av">'+ini(r.ad)+'</div><b style="font-size:12px">'+r.ad+'</b></div></td>'
        +'<td style="text-align:right;color:var(--muted);font-family:JetBrains Mono,monospace;font-size:11.5px">'+r.giris+'</td></tr>';
    }).join(''):'<tr><td style="color:var(--muted);font-size:12px;text-align:center;padding:16px">Gec giris yok</td></tr>';

    // Bekleyen onaylar
    document.getElementById('onay-cnt').textContent=approvals.length+' bekliyor';
    document.getElementById('onay-list').innerHTML=approvals.length?approvals.slice(0,5).map(function(r){
      var typeLabel=r.type==='ht_work'?'HT Calisma':'Fazla Mesai';
      return '<tr><td><div class="who"><div class="av" style="background:var(--blue)">'+ini(r.ad||'?')+'</div><b style="font-size:12px">'+(r.ad||'?')+'</b></div></td>'
        +'<td style="text-align:right"><span class="pill p-amber">'+typeLabel+'</span></td></tr>';
    }).join(''):'<tr><td style="color:var(--muted);font-size:12px;text-align:center;padding:16px">Bekleyen onay yok</td></tr>';

  }catch(e){
    console.log('Dashboard hata:',e);
  }
}

document.getElementById('refresh-btn').addEventListener('click',loadDashboard);
loadDashboard();
</script>
</template>'''

for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    start = s.index('<template id="tpl-dashboard">')
    end = s.index('</template>', start) + len('</template>')
    s = s[:start] + NEW_DASHBOARD + s[end:]
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, 'OK - boyut:', len(s))
