for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    old = "      var total=GL.regs.length+htRows.length+fmRows.length;"
    new = """      // Konum uyarilari
      var konumRows=data.filter(function(x){return x.type==='konum_uyari';});
      var konumBody=document.querySelector('#tab-konum tbody');
      if(konumBody){
        if(!konumRows.length){konumBody.innerHTML='<tr><td colspan="4" class="empty">Konum uyarisi yok</td></tr>';}
        else{konumBody.innerHTML=konumRows.map(function(x){
          return '<tr><td><div class="who"><div class="av" style="background:var(--danger)">'+ini2(x.ad||'?')+'</div><div><b>'+(x.ad||'?')+'</b></div></div></td>'
            +'<td class="mono">'+x.day+'</td>'
            +'<td style="color:var(--danger);font-size:11.5px">'+(x.note||'Tesis disinda')+'</td>'
            +'<td><span class="pill p-warn">Uyari</span></td></tr>';
        }).join('');}
      }
      document.getElementById('konum-cnt').textContent=konumRows.length||'0';
      var total=GL.regs.length+htRows.length+fmRows.length+konumRows.length;"""
    
    # tab-konum tabview ekle
    old2 = '            <div class="ntxt">Hafta tatilinde'
    new2 = """            </div>
            <div class="tabview" id="tab-konum" style="padding-top:8px">
              <table><thead><tr><th>Personel</th><th>Tarih</th><th>Detay</th><th>Durum</th></tr></thead>
                <tbody><tr><td colspan="4" class="empty">Konum uyarisi yok</td></tr></tbody>
              </table>
            </div>
            <div class="ntxt" style="display:none">Hafta tatilinde"""
    
    found1 = old in s
    found2 = old2 in s
    s = s.replace(old, new)
    # Sadece tabview ekle, ntxt'i koru
    if found2:
        s = s.replace('            <div class="ntxt">Hafta tatilinde', 
                      '            <div class="tabview" id="tab-konum" style="padding-top:8px">\n              <table><thead><tr><th>Personel</th><th>Tarih</th><th>Detay</th><th>Durum</th></tr></thead>\n                <tbody><tr><td colspan="4" class="empty">Konum uyarisi yok</td></tr></tbody>\n              </table>\n            </div>\n            <div class="ntxt">Hafta tatilinde', 1)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> total:', found1, '| tabview:', found2)
