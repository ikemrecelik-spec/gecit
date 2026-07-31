# -*- coding: utf-8 -*-
p='/home/ubuntu/gecit-backend/public/v2.html'
s=open(p,encoding='utf-8').read()

if 'AYAR_RENK_v1' in s:
    print("Zaten var, dokunulmadi")
    raise SystemExit

cnt=0

# 1) Vardiya thead - Renk sutunu ekle
old="<thead><tr><th style=\"width:70px\">Kod</th><th>Ad</th><th style=\"width:105px\">Başlangıç</th><th style=\"width:105px\">Bitiş</th><th style=\"width:120px\">Geç tolerans (dk)</th><th style=\"width:46px\"></th></tr></thead>"
new="<thead><tr><th style=\"width:70px\">Kod</th><th>Ad</th><th style=\"width:95px\">Başlangıç</th><th style=\"width:95px\">Bitiş</th><th style=\"width:100px\">Tolerans (dk)</th><th style=\"width:60px\">Renk</th><th style=\"width:46px\"></th></tr></thead>"
if s.count(old)==1: s=s.replace(old,new); cnt+=1; print("vardiya thead OK")
else: print("vardiya thead ATLANDI ("+str(s.count(old))+")")

# 2) Vardiya satiri - renk hucresi ekle (tol input'undan sonra, sil'den once)
old="""      +'<td><input type="number" min="0" max="120" value="'+(v.tol!=null?v.tol:15)+'" data-i="'+i+'" data-k="tol"></td>'
      +'<td><button class="btn btn-danger btn-mini" data-del="'+i+'">✕</button></td>'"""
new="""      +'<td><input type="number" min="0" max="120" value="'+(v.tol!=null?v.tol:15)+'" data-i="'+i+'" data-k="tol"></td>'
      +'<td style="text-align:center"><input type="color" value="'+(v.color||'#6FB1FF')+'" data-i="'+i+'" data-k="color" style="width:38px;height:28px;padding:1px;border-radius:6px;cursor:pointer"></td>'
      +'<td><button class="btn btn-danger btn-mini" data-del="'+i+'">✕</button></td>'"""
if s.count(old)==1: s=s.replace(old,new); cnt+=1; print("vardiya satiri OK")
else: print("vardiya satiri ATLANDI ("+str(s.count(old))+")")

# 3) Vardiya bos mesaj colspan 6->7
old='<tr><td colspan="6" style="color:var(--muted);text-align:center;padding:18px">Vardiya tanımlanmamış</td></tr>'
new='<tr><td colspan="7" style="color:var(--muted);text-align:center;padding:18px">Vardiya tanımlanmamış</td></tr>'
if s.count(old)==1: s=s.replace(old,new); cnt+=1

# 4) Vardiya ekleme - varsayilan renk
old="S.shifts.push({code:'',name:'',start:'08:00',end:'16:00',tol:15});markDirty();renderVard();"
new="S.shifts.push({code:'',name:'',start:'08:00',end:'16:00',tol:15,color:'#6FB1FF'});markDirty();renderVard();"
if s.count(old)==1: s=s.replace(old,new); cnt+=1; print("vardiya ekleme OK")

# 5) Izin thead - Renk sutunu
old='<thead><tr><th style="width:80px">Kod</th><th>Ad</th><th style="width:90px">Ücretli</th><th style="width:46px"></th></tr></thead>'
new='<thead><tr><th style="width:80px">Kod</th><th>Ad</th><th style="width:60px">Renk</th><th style="width:110px">Ödeme</th><th style="width:46px"></th></tr></thead>'
if s.count(old)==1: s=s.replace(old,new); cnt+=1; print("izin thead OK")
else: print("izin thead ATLANDI ("+str(s.count(old))+")")

# 6) normLeave - color koru
old="""function normLeave(x){
  if(typeof x==='string')return {code:x,name:x,ucretli:true};
  return {code:x.code||'',name:x.name||'',ucretli:x.ucretli!==false};
}"""
new="""function normLeave(x){
  if(typeof x==='string')return {code:x,name:x,ucretli:true,color:'#C792EA'};
  return {code:x.code||'',name:x.name||'',ucretli:x.ucretli!==false,color:x.color||'#C792EA'};
}"""
if s.count(old)==1: s=s.replace(old,new); cnt+=1; print("normLeave OK")

# 7) Izin satiri - renk hucresi + odeme dropdown (checkbox yerine)
old="""      +'<td><input value="'+(v.name||'')+'" data-i="'+i+'" data-k="name"></td>'
      +'<td style="text-align:center"><input type="checkbox" '+(v.ucretli?'checked':'')+' data-i="'+i+'" data-k="ucretli"></td>'
      +'<td><button class="btn btn-danger btn-mini" data-del="'+i+'">✕</button></td>'"""
new="""      +'<td><input value="'+(v.name||'')+'" data-i="'+i+'" data-k="name"></td>'
      +'<td style="text-align:center"><input type="color" value="'+(v.color||'#C792EA')+'" data-i="'+i+'" data-k="color" style="width:38px;height:28px;padding:1px;border-radius:6px;cursor:pointer"></td>'
      +'<td><select data-i="'+i+'" data-k="ucretli"><option value="1"'+(v.ucretli?' selected':'')+'>Ücretli</option><option value="0"'+(!v.ucretli?' selected':'')+'>Ücretsiz</option></select></td>'
      +'<td><button class="btn btn-danger btn-mini" data-del="'+i+'">✕</button></td>'"""
if s.count(old)==1: s=s.replace(old,new); cnt+=1; print("izin satiri OK")
else: print("izin satiri ATLANDI ("+str(s.count(old))+")")

# 8) Izin input handler - select ve ucretli'yi dogru isle
old="""  tb.querySelectorAll('input').forEach(function(inp){
    inp.addEventListener('input',function(){
      var i=+inp.dataset.i,k=inp.dataset.k;
      S.leaves[i][k]=(k==='ucretli')?inp.checked:inp.value;
      markDirty();
    });
  });
  tb.querySelectorAll('[data-del]').forEach(function(b){b.addEventListener('click',function(){S.leaves.splice(+b.dataset.del,1);markDirty();renderIzin();});});"""
new="""  tb.querySelectorAll('input,select').forEach(function(inp){
    inp.addEventListener(inp.tagName==='SELECT'?'change':'input',function(){
      var i=+inp.dataset.i,k=inp.dataset.k;
      S.leaves[i][k]=(k==='ucretli')?(inp.value==='1'):inp.value;
      markDirty();
    });
  });
  tb.querySelectorAll('[data-del]').forEach(function(b){b.addEventListener('click',function(){S.leaves.splice(+b.dataset.del,1);markDirty();renderIzin();});});"""
if s.count(old)==1: s=s.replace(old,new); cnt+=1; print("izin handler OK")
else: print("izin handler ATLANDI ("+str(s.count(old))+")")

# 9) Izin bos mesaj colspan 4->5
old='<tr><td colspan="4" style="color:var(--muted);text-align:center;padding:18px">İzin türü tanımlanmamış</td></tr>'
new='<tr><td colspan="5" style="color:var(--muted);text-align:center;padding:18px">İzin türü tanımlanmamış</td></tr>'
if s.count(old)==1: s=s.replace(old,new); cnt+=1

# 10) Izin ekleme - varsayilan renk
old="S.leaves.push({code:'',name:'',ucretli:true});markDirty();renderIzin();"
new="S.leaves.push({code:'',name:'',ucretli:true,color:'#C792EA'});markDirty();renderIzin();"
if s.count(old)==1: s=s.replace(old,new); cnt+=1; print("izin ekleme OK")

# marker
s=s.replace('<h1>Ayarlar <span class="tag-info" id="ay-tenant-name"></span></h1>','<h1>Ayarlar <span class="tag-info" id="ay-tenant-name"></span></h1><!-- AYAR_RENK_v1 -->',1)

open(p,'w',encoding='utf-8').write(s)
print("KAYDEDILDI - AYAR_RENK_v1 - toplam "+str(cnt)+" degisiklik")
