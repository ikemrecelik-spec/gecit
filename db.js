'use strict';
const { DatabaseSync } = require('node:sqlite');
const bcrypt = require('bcryptjs');
const path = require('path');

const DB_PATH = process.env.GECIT_DB || path.join(__dirname, 'gecit.db');
const db = new DatabaseSync(DB_PATH);
db.exec('PRAGMA journal_mode = WAL;');

db.exec(`
CREATE TABLE IF NOT EXISTS tenants (
  id TEXT PRIMARY KEY, name TEXT, loc TEXT, staff INTEGER, plan TEXT, active INTEGER DEFAULT 1
);
CREATE TABLE IF NOT EXISTS operators (
  username TEXT PRIMARY KEY, pass_hash TEXT
);
CREATE TABLE IF NOT EXISTS accounts (
  tenant_id TEXT, tc TEXT, ad TEXT, dob TEXT, pass_hash TEXT,
  approved INTEGER DEFAULT 0, sicil INTEGER, dep TEXT DEFAULT 'Servis',
  gorev TEXT DEFAULT 'Personel', status TEXT DEFAULT 'aktif',
  device TEXT, created INTEGER,
  PRIMARY KEY (tenant_id, tc)
);
CREATE TABLE IF NOT EXISTS attendance (
  id INTEGER PRIMARY KEY AUTOINCREMENT, tenant_id TEXT, sicil INTEGER, tc TEXT,
  ad TEXT, gorev TEXT, vardiya TEXT, giris TEXT, cikis TEXT,
  off INTEGER DEFAULT 0, fm INTEGER DEFAULT 0, izin TEXT DEFAULT '', dep TEXT,
  day TEXT, ts INTEGER
);
CREATE TABLE IF NOT EXISTS leaves (
  id INTEGER PRIMARY KEY AUTOINCREMENT, tenant_id TEXT, tc TEXT, ad TEXT,
  type TEXT, start TEXT, end TEXT, days INTEGER, reason TEXT,
  status TEXT DEFAULT 'beklemede', created INTEGER
);
CREATE TABLE IF NOT EXISTS puantaj_lock (
  tenant_id TEXT, month TEXT, locked INTEGER DEFAULT 0, ts INTEGER,
  PRIMARY KEY (tenant_id, month)
);
CREATE TABLE IF NOT EXISTS hotel_users (
  username TEXT PRIMARY KEY, tenant_id TEXT, pass_hash TEXT, name TEXT
);
CREATE TABLE IF NOT EXISTS tenant_settings (
  tenant_id TEXT PRIMARY KEY, settings TEXT
);
CREATE TABLE IF NOT EXISTS employee_docs (
  id INTEGER PRIMARY KEY AUTOINCREMENT, tenant_id TEXT, tc TEXT, name TEXT, note TEXT, ts INTEGER
);

`);

function seed() {
  if (db.prepare('SELECT COUNT(*) c FROM tenants').get().c === 0) {
    const ins = db.prepare('INSERT INTO tenants (id,name,loc,staff,plan,active) VALUES (?,?,?,?,?,?)');
    ins.run('arnor', 'ARNOR DELUXE HOTEL', 'Side / Antalya · Side Prenses', 241, 'Pro', 1);
    ins.run('belek-gold', 'BELEK GOLD RESORT', 'Belek / Antalya', 180, 'Pro', 1);
    ins.run('kemer-bay', 'KEMER BAY HOTEL', 'Kemer / Antalya', 95, 'Başlangıç', 0);
  }
  if (db.prepare('SELECT COUNT(*) c FROM operators').get().c === 0) {
    db.prepare('INSERT INTO operators (username,pass_hash) VALUES (?,?)').run('gecit.admin', bcrypt.hashSync('123456', 8));
  }
}
seed();

function detectShift(giris) {
  const [h, m] = giris.split(':').map(Number); const t = h * 60 + m;
  if (t >= 390 && t <= 570) return 'A · 08:00–16:00';
  if (t >= 630 && t <= 810) return 'Ara · 12:00–20:00';
  if (t >= 870 && t <= 1020) return 'B · 16:00–24:00';
  if (t >= 1380 || t <= 480) return 'Gece · 24:00–08:00';
  return 'A · 08:00–16:00';
}
const todayStr = () => new Date().toISOString().slice(0, 10);
const nextSicil = () => 2700 + Math.floor(Math.random() * 300);

module.exports = {
  db, bcrypt, detectShift, todayStr, nextSicil,

  getOperator: (u) => db.prepare('SELECT * FROM operators WHERE username=?').get(u),
  listTenants: () => db.prepare('SELECT * FROM tenants ORDER BY active DESC, name').all(),
  getTenant: (id) => db.prepare('SELECT * FROM tenants WHERE id=?').get(id),

  getAccount: (t, tc) => db.prepare('SELECT * FROM accounts WHERE tenant_id=? AND tc=?').get(t, tc),
  createAccount: (t, a) => db.prepare('INSERT INTO accounts (tenant_id,tc,ad,dob,pass_hash,approved,created) VALUES (?,?,?,?,?,0,?)').run(t, a.tc, a.ad, a.dob, a.pass_hash, Date.now()),
  setPassword: (t, tc, hash) => db.prepare('UPDATE accounts SET pass_hash=? WHERE tenant_id=? AND tc=?').run(hash, t, tc),
  listRegistrations: (t) => db.prepare('SELECT tc,ad,dob,created FROM accounts WHERE tenant_id=? AND approved=0 ORDER BY created').all(t),
  approveAccount: (t, tc, sicil, dep, gorev) => db.prepare('UPDATE accounts SET approved=1, sicil=?, dep=?, gorev=? WHERE tenant_id=? AND tc=?').run(sicil, dep, gorev, t, tc),
  rejectAccount: (t, tc) => db.prepare('DELETE FROM accounts WHERE tenant_id=? AND tc=?').run(t, tc),
  listEmployees: (t) => db.prepare("SELECT tc,ad,sicil,dep,gorev,status,device FROM accounts WHERE tenant_id=? AND approved=1 ORDER BY status, sicil").all(t),

  createEmployeeDirect: (t, e) => {
    const sicil = e.sicil || nextSicil();
    db.prepare('INSERT INTO accounts (tenant_id,tc,ad,dob,pass_hash,approved,sicil,dep,gorev,status,created) VALUES (?,?,?,?,?,1,?,?,?,?,?)')
      .run(t, e.tc, e.ad, e.dob || '', bcrypt.hashSync(e.pass || String(e.tc || '0000').slice(-4), 8), sicil, e.dep || 'Servis', e.gorev || 'Personel', 'aktif', Date.now());
    return sicil;
  },
  updateEmployee: (t, tc, e) => db.prepare('UPDATE accounts SET ad=COALESCE(?,ad), dep=COALESCE(?,dep), gorev=COALESCE(?,gorev) WHERE tenant_id=? AND tc=?').run(e.ad ?? null, e.dep ?? null, e.gorev ?? null, t, tc),
  setEmpStatus: (t, tc, status) => db.prepare('UPDATE accounts SET status=? WHERE tenant_id=? AND tc=?').run(status, t, tc),
  resetDevice: (t, tc) => db.prepare('UPDATE accounts SET device=NULL WHERE tenant_id=? AND tc=?').run(t, tc),

  listAttendance: (t) => db.prepare('SELECT * FROM attendance WHERE tenant_id=? ORDER BY id DESC LIMIT 1000').all(t),
  openAttendance: (t, tc) => db.prepare("SELECT * FROM attendance WHERE tenant_id=? AND tc=? AND giris IS NOT NULL AND (cikis IS NULL OR cikis='') ORDER BY id DESC").get(t, tc),
  punchIn: (t, acc, giris) => db.prepare('INSERT INTO attendance (tenant_id,sicil,tc,ad,gorev,vardiya,giris,cikis,off,fm,izin,dep,day,ts) VALUES (?,?,?,?,?,?,?,?,0,0,?,?,?,?)').run(t, acc.sicil, acc.tc, acc.ad, acc.gorev, detectShift(giris), giris, null, '', acc.dep, todayStr(), Date.now()),
  punchOut: (id, cikis) => db.prepare('UPDATE attendance SET cikis=? WHERE id=?').run(cikis, id),
  updateAttendance: (id, f) => db.prepare('UPDATE attendance SET giris=COALESCE(?,giris), cikis=COALESCE(?,cikis), izin=COALESCE(?,izin) WHERE id=?').run(f.giris ?? null, f.cikis ?? null, f.izin ?? null, id),

  createLeave: (t, l) => db.prepare('INSERT INTO leaves (tenant_id,tc,ad,type,start,end,days,reason,status,created) VALUES (?,?,?,?,?,?,?,?,?,?)').run(t, l.tc, l.ad, l.type, l.start, l.end, l.days, l.reason || '', 'beklemede', Date.now()),
  listLeaves: (t, status) => status ? db.prepare('SELECT * FROM leaves WHERE tenant_id=? AND status=? ORDER BY id DESC').all(t, status) : db.prepare('SELECT * FROM leaves WHERE tenant_id=? ORDER BY id DESC').all(t),
  listLeavesByTc: (t, tc) => db.prepare('SELECT * FROM leaves WHERE tenant_id=? AND tc=? ORDER BY id DESC').all(t, tc),
  setLeaveStatus: (id, status) => db.prepare('UPDATE leaves SET status=? WHERE id=?').run(status, id),

  getLock: (t, m) => db.prepare('SELECT * FROM puantaj_lock WHERE tenant_id=? AND month=?').get(t, m),
  setLock: (t, m, locked) => db.prepare('INSERT INTO puantaj_lock (tenant_id,month,locked,ts) VALUES (?,?,?,?) ON CONFLICT(tenant_id,month) DO UPDATE SET locked=excluded.locked, ts=excluded.ts').run(t, m, locked, Date.now()),
};
