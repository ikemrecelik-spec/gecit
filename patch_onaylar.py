for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    old = """  window.renderReg=renderReg;
  window.GECIT.refresh=function(){ try{ if(window.renderReg)window.renderReg(); var act=document.querySelector('.navitem.active'); if(act&&act.dataset.frame){ curFrame=null; showFrame(act.dataset.frame); } }catch(e){} };"""
    
    new = """  window.renderReg=renderReg;

  // Gercek API'den HT/FM onaylarini yukle
  async function loadApprovals(){
    try{
      var g=window.GECIT; var tenant=g._tenant||'1'; var tok=g._token||null;
      var h={'Content-Type':'application/json'}; if(tok)h['Authorization']='Bearer '+tok;
      var r=await fetch('https://gecitpdks.duckdns.org/api/'+tenant+'/approvals?status=beklemede',{headers:h});
      var data=await r.json();
      if(!Array.isArray(data))return;
      var htRows=data.filter(function(x){return x.type==='ht_work';});
      var fmRows=data.filter(function(x){return x.type==='fm';});
      // HT tablosu
      var htb=document.querySelector('#tab-ht tbody');
      if(htb){
        if(!htRows.length){htb.innerHTML='<tr><td colspan="4" class="empty">Bekleyen hafta tatili mesaisi yok</td></tr>';}
        else{
          htb.innerHTML=htRows.map(function(x){
            return '<tr>'
              +'<td><div class="who"><div class="av" style="background:var(--blue)">'+ini2(x.ad||'')+'</div><div><b>'+(x.ad||'?')+'</b><small>'+(x.dep||'')+'</small></div></div></td>'
              +'<td class="mono">'+x.day+'</td>'
              +'<td><span class="pill p-ht">HT gununde calisma</span></td>'
              +'<td style="text-align:right">'
              +'<button class="btn ok" onclick="approveItem('+x.id+',\'onaylandi\',\'ht\')">Onayla</button> '
              +'<button class="btn no" onclick="approveItem('+x.id+',\'reddedildi\',\'ht\')">Reddet</button>'
              +'</td></tr>';
          }).join('');
        }
      }
      // FM tablosu
      var fmb=document.querySelector('#tab-fm tbody');
      if(fmb){
        if(!fmRows.length){fmb.innerHTML='<tr><td colspan="4" class="empty">Bekleyen fazla mesai yok</td></tr>';}
        else{
          fmb.innerHTML=fmRows.map(function(x){
            return '<tr>'
              +'<td><div class="who"><div class="av" style="background:var(--amber)">'+ini2(x.ad||'')+'</div><div><b>'+(x.ad||'?')+'</b><small>'+(x.dep||'')+'</small></div></div></td>'
              +'<td class="mono">'+x.day+'</td>'
              +'<td><span class="pill p-fm">Fazla mesai</span></td>'
              +'<td style="text-align:right">'
              +'<button class="btn ok" onclick="approveItem('+x.id+',\'onaylandi\',\'fm\')">Onayla</button> '
              +'<button class="btn no" onclick="approveItem('+x.id+',\'reddedildi\',\'fm\')">Reddet</button>'
              +'</td></tr>';
          }).join('');
        }
      }
      // Badge guncelle
      var total=GL.regs.length+htRows.length+fmRows.length;
      $('#nav-onay').textContent=total>0?total:'';
      // Tab sayilari guncelle
      document.querySelectorAll('#view-onaylar .tab').forEach(function(t){
        if(t.dataset.t==='ht')t.innerHTML='Hafta tatili mesaisi ('+htRows.length+')';
        if(t.dataset.t==='fm')t.innerHTML='Fazla mesai ('+fmRows.length+')';
      });
    }catch(e){console.log('loadApprovals error:',e.message);}
  }

  window.approveItem=async function(id,status,type){
    try{
      var g=window.GECIT; var tenant=g._tenant||'1'; var tok=g._token||null;
      var h={'Content-Type':'application/json'}; if(tok)h['Authorization']='Bearer '+tok;
      await fetch('https://gecitpdks.duckdns.org/api/'+tenant+'/approvals/'+id,{method:'PUT',headers:h,body:JSON.stringify({status:status})});
      loadApprovals();
      showToast(status==='onaylandi'?'Onaylandi':'Reddedildi');
    }catch(e){showToast('Hata: '+e.message);}
  };

  // Onaylar sekmesine gecince yukle
  document.querySelectorAll('.navitem').forEach(function(n){
    n.addEventListener('click',function(){
      if(n.dataset.v==='onaylar')setTimeout(loadApprovals,200);
    });
  });

  window.renderReg=renderReg;
  window.GECIT.refresh=function(){ try{ if(window.renderReg)window.renderReg(); loadApprovals(); var act=document.querySelector('.navitem.active'); if(act&&act.dataset.frame){ curFrame=null; showFrame(act.dataset.frame); } }catch(e){} };"""
    
    found = old in s
    s = s.replace(old, new)
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '->', found)
