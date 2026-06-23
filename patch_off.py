for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s=open(fn,encoding='utf-8').read()
    old="      var code=empPlan[ds];\n      // Eger plan yoksa OFF goster\n      if(!code)code='OFF';"
    new="      var code=empPlan[ds]||'-';"
    found=old in s
    s=s.replace(old,new)
    # Ayrica tire icin SHIFT_MAP'te karsilik ekle
    old2="var SHIFT_MAP={};SHIFTS.forEach(function(s){SHIFT_MAP[s.code]=s;});"
    new2="var SHIFT_MAP={};SHIFTS.forEach(function(s){SHIFT_MAP[s.code]=s;});SHIFT_MAP['-']={code:'-',bg:'#0d1218',color:'#23414F'};"
    found2=old2 in s
    s=s.replace(old2,new2)
    open(fn,'w',encoding='utf-8').write(s)
    print(fn,'-> code:', found, '| map:', found2)
