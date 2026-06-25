for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    old = """document.getElementById('edit-save').addEventListener('click',async function(){
  var id=document.getElementById('edit-id').value;
  if(!id){toast('Bu satirda kayit yok, once QR okutulmali');return;}"""
    
    new = """document.getElementById('edit-save').addEventListener('click',async function(){
  var id=document.getElementById('edit-id').value;
  if(!id){
    // Kayit yok - yeni kayit olustur
    var tc=document.getElementById('edit-tc').value;
    var giris=document.getElementById('edit-giris').value;
    var cikis=document.getElementById('edit-cikis').value;
    var gdate=document.getElementById('edit-gdate').value;
    if(!tc||!gdate||!giris){toast('Giris saati gerekli');return;}
    try{await req('/attendance',{method:'POST',body:{tc:tc,day:gdate,giris:giris,cikis:cikis||null}});toast('Manuel kayit eklendi');closeModals();listele();}
    catch(e){toast('Hata: '+e.message);}
    return;
  }"""
    
    found = old in s
    s = s.replace(old, new)
    
    # edit-id yanina edit-tc hidden input ekle
    old2 = '    <input type="hidden" id="edit-id">'
    new2 = '    <input type="hidden" id="edit-id">\n    <input type="hidden" id="edit-tc">'
    found2 = old2 in s
    s = s.replace(old2, new2)
    
    # openEdit fonksiyonuna tc ekleme
    old3 = "  document.getElementById('edit-id').value=r.id||'';"
    new3 = "  document.getElementById('edit-id').value=r.id||'';\n  document.getElementById('edit-tc').value=r.tc||'';"
    found3 = old3 in s
    s = s.replace(old3, new3)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> save:', found, '| input:', found2, '| tc:', found3)
