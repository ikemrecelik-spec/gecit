s = open('server.js', encoding='utf-8').read()

old = """app.get('/api/:tenant/puantaj', authTenant, (req, res) => {
  const t = req.params.tenant; const month = req.query.month || new Date().toISOString().slice(0,7);
  const emps = D.listEmployees(t).filter(e=>e.status!=='pasif');
  const att = D.listAttendance(t); const leaves = D.listLeaves(t).filter(l=>l.status==='onaylandı');
  const [y,mo] = month.split('-').map(Number); const dim = new Date(y,mo,0).getDate(); const monthPad=String(y)+'-'+String(mo).padStart(2,'0');
  const rows = emps.map(e => {
    const days={}; let work=0,leaveD=0;
    for(let d=1;d<=dim;d++){
      const ds=monthPad+'-'+String(d).padStart(2,'0');
      const hasAtt=att.some(r=>r.tc===e.tc&&r.day===ds&&r.giris);
      const lv=leaves.find(l=>l.tc===e.tc&&l.start<=ds&&l.end>=ds);
      const dow=new Date(y,mo-1,d).getDay(); let code='·';
      if(hasAtt){code='X';work++;}else if(lv){code=LEAVE_CODE[lv.type]||'Yİ';leaveD++;}else if(dow===0)code='HT';
      days[d]=code;
    }
    return {sicil:e.sicil,ad:e.ad,dep:e.dep,days,work,leaveD};
  });
  const lock=D.getLock(t,month);
  res.json({month,locked:!!(lock&&lock.locked),dim,rows});
});"""

new = """app.get('/api/:tenant/puantaj', authTenant, (req, res) => {
  const t = req.params.tenant; const month = req.query.month || new Date().toISOString().slice(0,7);
  const emps = D.listEmployees(t).filter(e=>e.status!=='pasif');
  const att = D.listAttendance(t); const leaves = D.listLeaves(t).filter(l=>l.status==='onaylandı');
  const [y,mo] = month.split('-').map(Number); const dim = new Date(y,mo,0).getDate(); const monthPad=String(y)+'-'+String(mo).padStart(2,'0');
  // Shift planini oku - o ay icindeki tum haftalari getir
  const shiftRows = D.db.prepare('SELECT * FROM shift_plan WHERE tenant_id=?').all(t);
  const shiftMap = {}; // tc -> date -> code
  shiftRows.forEach(r => {
    const days = JSON.parse(r.days || '{}');
    Object.keys(days).forEach(date => {
      if (!shiftMap[r.tc]) shiftMap[r.tc] = {};
      shiftMap[r.tc][date] = days[date];
    });
  });
  // Puantaja yansiyacak shift kodlari (vardiya kodlari yansimaz)
  const SHIFT_LEAVE_CODES = ['HT','Yi','RP','Ui','BT','OFF'];
  const rows = emps.map(e => {
    const days={}; let work=0,leaveD=0;
    for(let d=1;d<=dim;d++){
      const ds=monthPad+'-'+String(d).padStart(2,'0');
      const hasAtt=att.some(r=>r.tc===e.tc&&r.day===ds&&r.giris);
      const lv=leaves.find(l=>l.tc===e.tc&&l.start<=ds&&l.end>=ds);
      const shiftCode=shiftMap[e.tc]&&shiftMap[e.tc][ds];
      let code='·';
      if(hasAtt){code='X';work++;}
      else if(lv){code=LEAVE_CODE[lv.type]||'Yi';leaveD++;}
      else if(shiftCode&&SHIFT_LEAVE_CODES.includes(shiftCode)){code=shiftCode;if(shiftCode!=='HT'&&shiftCode!=='OFF')leaveD++;}
      days[d]=code;
    }
    return {sicil:e.sicil,ad:e.ad,dep:e.dep,days,work,leaveD};
  });
  const lock=D.getLock(t,month);
  res.json({month,locked:!!(lock&&lock.locked),dim,rows});
});"""

print('bulundu:', old in s)
s = s.replace(old, new)
open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
