for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s=open(fn,encoding='utf-8').read()
    old="var r=await fetch(location.origin+'/api/'+tenant+'/attendance',{headers:h});"
    new="var r=await fetch('https://gecitpdks.duckdns.org/api/'+tenant+'/attendance',{headers:h});"
    found = old in s
    s = s.replace(old, new)
    open(fn,encoding='utf-8',mode='w').write(s)
    print(fn, '->', found)
