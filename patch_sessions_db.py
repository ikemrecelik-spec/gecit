s = open('server.js', encoding='utf-8').read()

old = """const sessions = new Map();
function issue(data) { const tok = crypto.randomBytes(18).toString('hex'); sessions.set(tok, data); return tok; }"""

new = """// Sessions DB'de saklanir - restart sonrasi token gecerliligi korunur
const sessionsDb = D.db;
try { sessionsDb.exec('CREATE TABLE IF NOT EXISTS sessions (tok TEXT PRIMARY KEY, data TEXT, created INTEGER)'); } catch(e) {}
// Eski sessionlari temizle (7 gunden eski)
try { sessionsDb.prepare('DELETE FROM sessions WHERE created < ?').run(Date.now() - 7*24*60*60*1000); } catch(e) {}

function issue(data) {
  const tok = crypto.randomBytes(18).toString('hex');
  sessionsDb.prepare('INSERT OR REPLACE INTO sessions (tok, data, created) VALUES (?,?,?)').run(tok, JSON.stringify(data), Date.now());
  return tok;
}"""

print('issue bulundu:', old in s)
s = s.replace(old, new)

old2 = """    const s = sessions.get(tok);"""
new2 = """    let s = null; try { const row = sessionsDb.prepare('SELECT data FROM sessions WHERE tok=?').get(tok); if(row) s = JSON.parse(row.data); } catch(e) {}"""
print('get bulundu:', old2 in s)
s = s.replace(old2, new2)

# logout endpoint varsa sessions.delete kaldiralim
old3 = """sessions.delete(tok)"""
new3 = """try{sessionsDb.prepare('DELETE FROM sessions WHERE tok=?').run(tok);}catch(e){}"""
if old3 in s:
    s = s.replace(old3, new3)
    print('delete bulundu: True')
else:
    print('delete bulundu: False (normal olabilir)')

open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
