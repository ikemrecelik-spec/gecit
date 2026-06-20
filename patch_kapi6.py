for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s=open(fn,encoding='utf-8').read()
    old="var nowList=att.filter(function(r){return (now-(r.ts||0))<60000;}).slice(0,8);"
    new="var nowList=att.filter(function(r){return (now-(r.ts||0))<300000;}).slice(0,8);"
    found = old in s
    s = s.replace(old, new)
    open(fn,encoding='utf-8',mode='w').write(s)
    print(fn, '->', found)
