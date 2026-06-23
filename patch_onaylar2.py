for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    # onclick icindeki tirnak sorununu duzelt
    old1 = """+'<button class="btn ok" onclick="approveItem('+x.id+',\\'onaylandi\\',\\'ht\\')">Onayla</button> '
              +'<button class="btn no" onclick="approveItem('+x.id+',\\'reddedildi\\',\\'ht\\')">Reddet</button>'"""
    new1 = """+'<button class="btn ok" data-id="'+x.id+'" data-s="onaylandi" data-t="ht">Onayla</button> '
              +'<button class="btn no" data-id="'+x.id+'" data-s="reddedildi" data-t="ht">Reddet</button>'"""
    
    old2 = """+'<button class="btn ok" onclick="approveItem('+x.id+',\\'onaylandi\\',\\'fm\\')">Onayla</button> '
              +'<button class="btn no" onclick="approveItem('+x.id+',\\'reddedildi\\',\\'fm\\')">Reddet</button>'"""
    new2 = """+'<button class="btn ok" data-id="'+x.id+'" data-s="onaylandi" data-t="fm">Onayla</button> '
              +'<button class="btn no" data-id="'+x.id+'" data-s="reddedildi" data-t="fm">Reddet</button>'"""
    
    f1 = old1 in s
    f2 = old2 in s
    s = s.replace(old1, new1)
    s = s.replace(old2, new2)
    
    # Event delegation ekle - tbody click
    old3 = "      document.querySelectorAll('#view-onaylar .tab').forEach(function(t){"
    new3 = """      document.querySelector('#tab-ht tbody').addEventListener('click',function(e){
        var b=e.target.closest('button[data-id]'); if(!b)return;
        window.approveItem(+b.dataset.id,b.dataset.s,b.dataset.t);
      });
      document.querySelector('#tab-fm tbody').addEventListener('click',function(e){
        var b=e.target.closest('button[data-id]'); if(!b)return;
        window.approveItem(+b.dataset.id,b.dataset.s,b.dataset.t);
      });
      document.querySelectorAll('#view-onaylar .tab').forEach(function(t){"""
    f3 = old3 in s
    s = s.replace(old3, new3)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> ht:', f1, '| fm:', f2, '| evt:', f3)
