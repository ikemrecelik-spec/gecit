'use strict';
const express = require('express');
const cors = require('cors');
const http = require('http');
const crypto = require('crypto');
const path = require('path');
const { WebSocketServer } = require('ws');
const D = require('./db');

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

const sessions = new Map();
function issue(data) { const tok = crypto.randomBytes(18).toString('hex'); sessions.set(tok, data); return tok; }
function auth(roles) {
  return (req, res, next) => {
    const tok = (req.headers.authorization || '').replace('Bearer ', '');
    const s = sessions.get(tok);
    if (!s || (roles && !roles.includes(s.role))) return res.status(401).json({ error: 'yetkisiz' });
    req.session = s; next();
  };
}

const server = http.createServer(app);
const wss = new WebSocketServer({ server, path: '/ws' });
wss.on('connection', (ws, req) => {
  const url = new URL(req.url, 'http://x');
  ws.tenant = url.searchParams.get('tenant') || 'arnor';
  ws.send(JSON.stringify({ type: 'hello', tenant: ws.tenant }));
});
function broadcast(tenant, type) {
  const msg = JSON.stringify({ type, tenant, ts: Date.now() });
  wss.clients.forEach(c => { if (c.readyState === 1 && c.tenant === tenant) c.send(msg); });
}

// ============ OPERATÖR GİRİŞİ ============
app.post('/api/operator/login', (req, res) => {
  const { username, password } = req.body || {};
  const op = D.getOperator(username);
  if (!op || !D.bcrypt.compareSync(password || '', op.pass_hash))
    return res.status(401).json({ error: 'Hatalı kullanıcı adı veya şifre' });
  res.json({ token: issue({ role: 'operator', username }) });
});

// ============ TENANT (İŞLETME) CRUD ============
app.get('/api/tenants', auth(['operator']), (req, res) => res.json(D.listTenants()));

app.post('/api/tenants', auth(['operator']), (req, res) => {
  const { id, name, loc, staff, plan } = req.body || {};
  if (!id || !name) return res.status(400).json({ error: 'id ve name zorunlu' });
  if (!/^[a-z0-9-]+$/.test(id)) return res.status(400).json({ error: 'ID sadece küçük harf, rakam ve tire içerebilir' });
  try {
    D.db.prepare('INSERT INTO tenants (id,name,loc,staff,plan,active) VALUES (?,?,?,?,?,1)')
      .run(id.trim(), name.trim(), loc || '', staff || 0, plan || 'Pro');
    res.json({ ok: true });
  } catch(e) { res.status(409).json({ error: 'Bu ID zaten kullanımda' }); }
});

app.put('/api/tenants/:id', auth(['operator']), (req, res) => {
  const { name, loc, staff, plan, active } = req.body || {};
  D.db.prepare('UPDATE tenants SET name=COALESCE(?,name), loc=COALESCE(?,loc), staff=COALESCE(?,staff), plan=COALESCE(?,plan), active=COALESCE(?,active) WHERE id=?')
    .run(name || null, loc || null, staff || null, plan || null, active != null ? active : null, req.params.id);
  res.json({ ok: true });
});

app.delete('/api/tenants/:id', auth(['operator']), (req, res) => {
  D.db.prepare('UPDATE tenants SET active=0 WHERE id=?').run(req.params.id);
  res.json({ ok: true });
});

// ============ OTEL KULLANICILARI ============
app.get('/api/hotel-users', auth(['operator']), (req, res) => {
  res.json(D.db.prepare('SELECT username, tenant_id, name FROM hotel_users ORDER BY tenant_id').all());
});

app.post('/api/hotel-users', auth(['operator']), (req, res) => {
  const { tenant_id, username, password, name } = req.body || {};
  if (!tenant_id || !username || !password)
    return res.status(400).json({ error: 'tenant_id, username ve password zorunlu' });
  if (!D.getTenant(tenant_id)) return res.status(404).json({ error: 'İşletme bulunamadı' });
  try {
    D.db.prepare('INSERT INTO hotel_users (username, tenant_id, pass_hash, name) VALUES (?,?,?,?)')
      .run(username.trim(), tenant_id, D.bcrypt.hashSync(password, 8), name || username);
    res.json({ ok: true });
  } catch(e) { res.status(409).json({ error: 'Bu kullanıcı adı zaten var' }); }
});

app.delete('/api/hotel-users/:username', auth(['operator']), (req, res) => {
  D.db.prepare('DELETE FROM hotel_users WHERE username=?').run(req.params.username);
  res.json({ ok: true });
});

// ============ OTEL PANELİ GİRİŞİ ============
app.post('/api/hotel/login', (req, res) => {
  const { username, password } = req.body || {};
  const u = D.db.prepare('SELECT * FROM hotel_users WHERE username=?').get(username);
  if (!u || !D.bcrypt.compareSync(password || '', u.pass_hash))
    return res.status(401).json({ error: 'Hatalı kullanıcı adı veya şifre' });
  res.json({ token: issue({ role: 'hotel', tenant: u.tenant_id, username, name: u.name }), tenant: u.tenant_id, name: u.name });
});

// ============ ADMIN DASHBOARD (tüm oteller) ============
app.get('/api/admin/summary', auth(['operator']), (req, res) => {
  const tenants = D.listTenants();
  const summary = tenants.map(t => {
    const emps    = D.db.prepare("SELECT COUNT(*) c FROM accounts WHERE tenant_id=? AND approved=1").get(t.id).c;
    const inside  = D.db.prepare("SELECT COUNT(*) c FROM attendance WHERE tenant_id=? AND giris IS NOT NULL AND (cikis IS NULL OR cikis='')").get(t.id).c;
    const pending = D.db.prepare("SELECT COUNT(*) c FROM accounts WHERE tenant_id=? AND approved=0").get(t.id).c;
    const todayIn = D.db.prepare("SELECT COUNT(*) c FROM attendance WHERE tenant_id=? AND day=?").get(t.id, D.todayStr()).c;
    const leaves  = D.db.prepare("SELECT COUNT(*) c FROM leaves WHERE tenant_id=? AND status='beklemede'").get(t.id).c;
    return { ...t, emps, inside, pending, todayIn, leaves };
  });
  res.json(summary);
});

// ============ PERSONEL KAYIT / GİRİŞ ============
app.post('/api/:tenant/personnel/register', (req, res) => {
  const { tenant } = req.params; const { ad, tc, dob, pass } = req.body || {};
  if (!D.getTenant(tenant)) return res.status(404).json({ error: 'İşletme bulunamadı' });
  if (!ad || !/^\d{11}$/.test(tc || '') || !/^\d{2}\.\d{2}\.\d{4}$/.test(dob || '') || (pass || '').length < 4)
    return res.status(400).json({ error: 'Eksik veya geçersiz bilgi' });
  if (D.getAccount(tenant, tc)) return res.status(409).json({ error: 'Bu TC ile kayıt zaten var' });
  D.createAccount(tenant, { tc, ad, dob, pass_hash: D.bcrypt.hashSync(pass, 8) });
  broadcast(tenant, 'registrations');
  res.json({ ok: true, status: 'pending' });
});

// TC + DOĞUM TARİHİ ile giriş (mobil için — şifresiz)
app.post('/api/:tenant/personnel/login-dob', (req, res) => {
  const { tenant } = req.params; const { tc, dob } = req.body || {};
  const a = D.getAccount(tenant, tc);
  if (!a) return res.status(401).json({ error: 'Bu TC ile kayıt bulunamadı. İK ile iletişime geçin.' });
  if (a.dob !== dob) return res.status(401).json({ error: 'Doğum tarihi eşleşmiyor.' });
  res.json({ token: issue({ role: 'personnel', tenant, tc, name: a.ad }), approved: !!a.approved, ad: a.ad, sicil: a.sicil, dep: a.dep, gorev: a.gorev });
});


app.post('/api/:tenant/personnel/login', (req, res) => {
  const { tenant } = req.params; const { tc, pass } = req.body || {};
  const a = D.getAccount(tenant, tc);
  if (!a || !D.bcrypt.compareSync(pass || '', a.pass_hash))
    return res.status(401).json({ error: 'TC veya şifre hatalı' });
  res.json({ token: issue({ role: 'personnel', tenant, tc, name: a.ad }), approved: !!a.approved, ad: a.ad, sicil: a.sicil, dep: a.dep, gorev: a.gorev });
});

app.post('/api/:tenant/personnel/forgot', (req, res) => {
  const { tenant } = req.params; const { tc, dob, newpass } = req.body || {};
  const a = D.getAccount(tenant, tc);
  if (!a) return res.status(404).json({ error: 'Kayıt bulunamadı' });
  if (a.dob !== dob) return res.status(403).json({ error: 'Doğum tarihi eşleşmiyor' });
  if ((newpass || '').length < 4) return res.status(400).json({ error: 'Şifre çok kısa' });
  D.setPassword(tenant, tc, D.bcrypt.hashSync(newpass, 8));
  res.json({ ok: true });
});

app.get('/api/:tenant/personnel/me', auth(['personnel']), (req, res) => {
  const a = D.getAccount(req.params.tenant, req.session.tc);
  if (!a) return res.status(404).json({ error: 'Bulunamadı' });
  res.json({ approved: !!a.approved, ad: a.ad, sicil: a.sicil, dep: a.dep, gorev: a.gorev });
});

app.get('/api/:tenant/personnel/attendance', auth(['personnel']), (req, res) =>
  res.json(D.db.prepare('SELECT * FROM attendance WHERE tenant_id=? AND tc=? ORDER BY id DESC LIMIT 30').all(req.params.tenant, req.session.tc)));

app.post('/api/:tenant/personnel/leaves', auth(['personnel']), (req, res) => {
  const { tenant } = req.params; const a = D.getAccount(tenant, req.session.tc);
  const l = req.body || {};
  if (!l.type || !l.start || !l.end) return res.status(400).json({ error: 'İzin türü ve tarih zorunlu' });
  const days = l.days || (Math.round((new Date(l.end) - new Date(l.start)) / 86400000) + 1) || 1;
  D.createLeave(tenant, { tc: req.session.tc, ad: a.ad, type: l.type, start: l.start, end: l.end, days, reason: l.reason });
  broadcast(tenant, 'leaves'); res.json({ ok: true });
});

app.get('/api/:tenant/personnel/leaves', auth(['personnel']), (req, res) =>
  res.json(D.listLeavesByTc(req.params.tenant, req.session.tc)));

// ============ YÖNETİM (operator veya hotel rolü) ============
function authTenant(req, res, next) {
  const tok = (req.headers.authorization || '').replace('Bearer ', '');
  const s = sessions.get(tok);
  if (!s) return res.status(401).json({ error: 'Yetkisiz' });
  if (s.role === 'operator' || (s.role === 'hotel' && s.tenant === req.params.tenant)) {
    req.session = s; return next();
  }
  res.status(403).json({ error: 'Bu otele yetkiniz yok' });
}

app.get('/api/:tenant/registrations', authTenant, (req, res) => res.json(D.listRegistrations(req.params.tenant)));
app.get('/api/:tenant/employees', authTenant, (req, res) => res.json(D.listEmployees(req.params.tenant)));
app.get('/api/:tenant/attendance', authTenant, (req, res) => res.json(D.listAttendance(req.params.tenant)));
app.get('/api/:tenant/leaves', authTenant, (req, res) => res.json(D.listLeaves(req.params.tenant, req.query.status)));
app.get('/api/:tenant/summary', authTenant, (req, res) => {
  const t = req.params.tenant; const emps = D.listEmployees(t); const att = D.listAttendance(t);
  res.json({ employees: emps.length, inside: att.filter(r=>r.giris&&!r.cikis).length, todayIn: att.filter(r=>r.day===D.todayStr()).length, pending: D.listRegistrations(t).length });
});

app.post('/api/:tenant/registrations/:tc/approve', authTenant, (req, res) => {
  const { tenant, tc } = req.params; const a = D.getAccount(tenant, tc);
  if (!a) return res.status(404).json({ error: 'Kayıt bulunamadı' });
  const sicil = 2700 + Math.floor(Math.random() * 300);
  D.approveAccount(tenant, tc, sicil, req.body.dep || 'Servis', req.body.gorev || 'Personel');
  broadcast(tenant, 'employees'); broadcast(tenant, 'registrations');
  res.json({ ok: true, sicil });
});

app.post('/api/:tenant/registrations/:tc/reject', authTenant, (req, res) => {
  D.rejectAccount(req.params.tenant, req.params.tc);
  broadcast(req.params.tenant, 'registrations');
  res.json({ ok: true });
});

app.post('/api/:tenant/employees', authTenant, (req, res) => {
  const { tenant } = req.params; const e = req.body || {};
  if (!e.ad || !/^\d{11}$/.test(e.tc || '')) return res.status(400).json({ error: 'Ad ve 11 haneli TC zorunlu' });
  if (D.getAccount(tenant, e.tc)) return res.status(409).json({ error: 'Bu TC zaten kayıtlı' });
  const sicil = D.createEmployeeDirect(tenant, e);
  broadcast(tenant, 'employees');
  res.json({ ok: true, sicil, tempPass: String(e.tc).slice(-4) });
});

app.put('/api/:tenant/employees/:tc', authTenant, (req, res) => {
  D.updateEmployee(req.params.tenant, req.params.tc, req.body || {});
  broadcast(req.params.tenant, 'employees'); res.json({ ok: true });
});

app.post('/api/:tenant/employees/:tc/status', authTenant, (req, res) => {
  D.setEmpStatus(req.params.tenant, req.params.tc, req.body.status === 'pasif' ? 'pasif' : 'aktif');
  broadcast(req.params.tenant, 'employees'); res.json({ ok: true });
});

app.post('/api/:tenant/employees/:tc/reset-device', authTenant, (req, res) => {
  D.resetDevice(req.params.tenant, req.params.tc);
  broadcast(req.params.tenant, 'employees'); res.json({ ok: true });
});

app.put('/api/:tenant/attendance/:id', authTenant, (req, res) => {
  D.updateAttendance(+req.params.id, req.body || {});
  broadcast(req.params.tenant, 'attendance'); res.json({ ok: true });
});

app.post('/api/:tenant/attendance/punch', auth(['personnel']), (req, res) => {
  const { tenant } = req.params; const tc = req.session.tc;
  const a = D.getAccount(tenant, tc);
  if (!a || !a.approved) return res.status(403).json({ error: 'Hesap henüz onaylanmadı' });
  if (!a.sicil) { const sicil = 2700+Math.floor(Math.random()*300); D.approveAccount(tenant,tc,sicil,a.dep,a.gorev); a.sicil=sicil; }
  const d = new Date(); const now = String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0');
  const open = D.openAttendance(tenant, tc);
  const action = open ? 'out' : 'in';
  if (open) D.punchOut(open.id, now); else D.punchIn(tenant, a, now);
  broadcast(tenant, 'attendance');
  res.json({ ok: true, action, time: now });
});

app.post('/api/:tenant/leaves/:id/approve', authTenant, (req, res) => {
  D.setLeaveStatus(+req.params.id, 'onaylandı'); broadcast(req.params.tenant, 'leaves'); res.json({ ok: true });
});
app.post('/api/:tenant/leaves/:id/reject', authTenant, (req, res) => {
  D.setLeaveStatus(+req.params.id, 'reddedildi'); broadcast(req.params.tenant, 'leaves'); res.json({ ok: true });
});

const LEAVE_CODE = { 'Yıllık':'Yİ','Ücretli':'M','Ücretsiz':'Üİ','Raporlu':'RP','Görevli':'G','Hafta tatili':'HT' };
app.get('/api/:tenant/puantaj', authTenant, (req, res) => {
  const t = req.params.tenant; const month = req.query.month || new Date().toISOString().slice(0,7);
  const emps = D.listEmployees(t).filter(e=>e.status!=='pasif');
  const att = D.listAttendance(t); const leaves = D.listLeaves(t).filter(l=>l.status==='onaylandı');
  const [y,mo] = month.split('-').map(Number); const dim = new Date(y,mo,0).getDate();
  const rows = emps.map(e => {
    const days={}; let work=0,leaveD=0,totalMins=0;
    for(let d=1;d<=dim;d++){
      const ds=month+'-'+String(d).padStart(2,'0');
      const dayAtts=att.filter(r=>r.tc===e.tc&&r.day===ds&&r.giris);
      const lv=leaves.find(l=>l.tc===e.tc&&l.start<=ds&&l.end>=ds);
      const dow=new Date(y,mo-1,d).getDay(); let code='·';
      if(dayAtts.length){
        let mins=0;
        dayAtts.forEach(r=>{
          if(r.giris&&r.cikis){
            const [gh,gm]=r.giris.split(':').map(Number);
            const [ch,cm]=r.cikis.split(':').map(Number);
            mins+=(ch*60+cm)-(gh*60+gm);
          }
        });
        totalMins+=Math.max(0,mins);
        code=(mins>=450)?'X':'?';
        work++;
      } else if(lv){code=LEAVE_CODE[lv.type]||'Yİ';leaveD++;}
      else if(dow===0)code='HT';
      days[d]=code;
    }
    return {sicil:e.sicil,ad:e.ad,dep:e.dep,days,work,leaveD,hours:Math.round(totalMins/60)};
  });
  const lock=D.getLock(t,month);
  res.json({month,locked:!!(lock&&lock.locked),dim,rows});
});

app.post('/api/:tenant/puantaj/lock', authTenant, (req, res) => {
  const month=req.body.month||new Date().toISOString().slice(0,7);
  D.setLock(req.params.tenant,month,req.body.locked?1:0);
  broadcast(req.params.tenant,'puantaj'); res.json({ok:true});
});

app.post('/api/:tenant/reset', authTenant, (req, res) => {
  const t=req.params.tenant;
  D.db.prepare('DELETE FROM accounts WHERE tenant_id=?').run(t);
  D.db.prepare('DELETE FROM attendance WHERE tenant_id=?').run(t);
  D.db.prepare('DELETE FROM leaves WHERE tenant_id=?').run(t);
  ['registrations','employees','attendance','leaves'].forEach(x=>broadcast(t,x));
  res.json({ok:true});
});

app.get('/health', (req, res) => res.json({ ok: true, ts: Date.now() }));

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => console.log('Geçit backend → http://localhost:' + PORT));
