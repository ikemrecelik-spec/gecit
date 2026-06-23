s = open('server.js', encoding='utf-8').read()

NEW_ROUTES = '''
// ============ SHIFT PLANI ============
app.get('/api/:tenant/shifts/plan', authTenant, (req, res) => {
  const t = req.params.tenant;
  const week = req.query.week; // "2026-06-08"
  if (!week) return res.status(400).json({error:'week gerekli'});
  const rows = D.db.prepare('SELECT * FROM shift_plan WHERE tenant_id=? AND week_start=?').all(t, week);
  const result = {};
  rows.forEach(r => { result[r.tc] = JSON.parse(r.days || '{}'); });
  res.json(result);
});

app.put('/api/:tenant/shifts/plan', authTenant, (req, res) => {
  const t = req.params.tenant;
  const { week, plan } = req.body || {};
  if (!week || !plan) return res.status(400).json({error:'week ve plan gerekli'});
  Object.keys(plan).forEach(tc => {
    const existing = D.db.prepare('SELECT id FROM shift_plan WHERE tenant_id=? AND week_start=? AND tc=?').get(t, week, tc);
    if (existing) {
      D.db.prepare('UPDATE shift_plan SET days=? WHERE id=?').run(JSON.stringify(plan[tc]), existing.id);
    } else {
      D.db.prepare('INSERT INTO shift_plan (tenant_id,week_start,tc,days) VALUES (?,?,?,?)').run(t, week, tc, JSON.stringify(plan[tc]));
    }
  });
  broadcast(t, 'shifts');
  res.json({ok:true});
});

'''

marker = "app.get('/health'"
print('bulundu:', marker in s)
s = s.replace(marker, NEW_ROUTES + marker, 1)
open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
