# 1) Backend: BÇ yerine HTÇ (onaylı HT) kodu don
s = open('server.js', encoding='utf-8').read()
old = """          // HT gununde calisma - BÇ onayliysa BÇ, yoksa X
          if(shiftCode==='HT') {
            const htApproval=approvalsMap[e.tc] && approvalsMap[e.tc][ds];
            code = (htApproval==='onaylandi') ? 'BÇ' : 'X';
          } else {"""
new = """          // HT gununde calisma - onayliysa HTÇ (farkli renk), yoksa X
          if(shiftCode==='HT') {
            const htApproval=approvalsMap[e.tc] && approvalsMap[e.tc][ds];
            code = (htApproval==='onaylandi') ? 'HTÇ' : 'X';
          } else {"""
found = old in s
s = s.replace(old, new)
open('server.js', 'w', encoding='utf-8').write(s)
print('backend:', found)

# 2) Frontend: puantaj modulunde HTÇ rengi ekle
for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    # CSS: HTÇ rengi - HT ama turuncu (geldi + onaylandi)
    old2 = """.cHT{color:var(--blue);font-weight:700}"""
    new2 = """.cHT{color:var(--blue);font-weight:700}
.cHTC{background:rgba(242,181,59,.2);color:var(--amber);font-weight:700}"""
    found2 = old2 in s
    s = s.replace(old2, new2)
    
    # CELL_CLS: HTÇ ekle
    old3 = """var CELL_CLS={X:'cX',HT:'cHT',BT:'cBT',BC:'cBC',M:'cM',Ui:'cUi',Yi:'cYi',RP:'cRP',UR:'cUR',G:'cG',D:'cD','·':'cDot'};"""
    new3 = """var CELL_CLS={X:'cX',HT:'cHT','HTÇ':'cHTC',BT:'cBT',BC:'cBC',M:'cM',Ui:'cUi',Yi:'cYi',RP:'cRP',UR:'cUR',G:'cG',D:'cD','·':'cDot'};"""
    found3 = old3 in s
    s = s.replace(old3, new3)
    
    # Legend: HTÇ ekle
    old4 = """  <div class="leg"><span class="c cHT">HT</span> Haftalik izin</div>"""
    new4 = """  <div class="leg"><span class="c cHT">HT</span> Haftalik izin</div>
  <div class="leg"><span class="c cHTC">HTÇ</span> HT gunu calisma (onaylandi)</div>"""
    found4 = old4 in s
    s = s.replace(old4, new4)
    
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '-> css:', found2, '| cls:', found3, '| legend:', found4)
