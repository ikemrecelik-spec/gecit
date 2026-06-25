s = open('server.js', encoding='utf-8').read()

old = "app.post('/api/:tenant/leaves/:id/approve', authTenant, (req, res) => {"

new = """app.post('/api/:tenant/leaves', authTenant, (req, res) => {
  const t = req.params.tenant;
  const b = req.body || {};
  if (!b.tc || !b.type || !b.start || !b.end) return res.status(400).json({error:'tc, type, start, end gerekli'});
  const emp = D.getAccount(t, b.tc);
  if (!emp) return res.status(404).json({error:'Personel bulunamadi'});
  const days = b.days || Math.round((new Date(b.end)-new Date(b.start))/86400000)+1;
  D.createLeave(t, {tc:b.tc, ad:emp.ad, type:b.type, start:b.start, end:b.end, days, reason:b.reason||''});
  if (b.status === 'onaylandi') {
    const leaves = D.listLeaves(t);
    const last = leaves[leaves.length-1];
    if (last) D.setLeaveStatus(last.id, 'onaylandi');
  }
  broadcast(t, 'leaves');
  res.json({ok:true});
});

app.post('/api/:tenant/leaves/:id/approve', authTenant, (req, res) => {"""

print('bulundu:', old in s)
s = s.replace(old, new)
open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
