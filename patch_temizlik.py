for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    # 1) Hotel name ARNOR -> Side Prenses + degistir butonunu gizle
    old1 = '''<button id="sa-back" title="\u0130\u015fletme de\u011fi\u015ftir" style="border:1px solid var(--line);background:var(--panel);color:var(--text);border-radius:10px;padding:8px 12px;font-weight:600;font-size:12.5px;cursor:pointer;display:flex;align-items:center;gap:7px;white-space:nowrap"> <span id="hotel-name">ARNOR DELUXE HOTEL</span> <span style="color:var(--muted);font-weight:400">\u00b7 de\u011fi\u015ftir</span></button>'''
    new1 = '''<span id="hotel-name" style="font-weight:600;font-size:14px;font-family:'Space Grotesk'">Side Prenses</span>'''
    found1 = old1 in s
    s = s.replace(old1, new1)
    
    # 2) TENANTS dizisini temizle
    old2 = """  var TENANTS=[
    {id:'arnor',name:'ARNOR DELUXE HOTEL',loc:'Side / Antalya \u00b7 Side Prenses',staff:241,plan:'Pro',active:true},
    {id:'belek-gold',name:'BELEK GOLD RESORT',loc:'Belek / Antalya',staff:180,plan:'Pro',active:true},
    {id:'kemer-bay',name:'KEMER BAY HOTEL',loc:'Kemer / Antalya',staff:95,plan:'Ba\u015flang\u0131\u00e7',active:false}
  ];"""
    new2 = """  var TENANTS=[
    {id:'1',name:'Side Prenses',loc:'Side / Antalya',staff:0,plan:'Pro',active:true}
  ];"""
    found2 = old2 in s
    s = s.replace(old2, new2)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> hotel:', found1, '| tenants:', found2)
