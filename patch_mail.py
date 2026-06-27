s = open('server.js', encoding='utf-8').read()

# Resend import ekle - en uste
old_top = "const express = require('express');"
new_top = """const express = require('express');
const { Resend } = require('resend');
const fs = require('fs');
// .env yukle
try{ const env=fs.readFileSync('.env','utf-8'); env.split('\\n').forEach(function(l){ var p=l.split('='); if(p[0]&&p[1])process.env[p[0].trim()]=p[1].trim(); }); }catch(e){}
const resend = new Resend(process.env.RESEND_API_KEY);"""

print('top bulundu:', old_top in s)
s = s.replace(old_top, new_top)

# Sifre sifirlama token tablosu
old_db_init = "try { sessionsDb.exec('CREATE TABLE IF NOT EXISTS sessions"
new_db_init = """try { D.db.exec('CREATE TABLE IF NOT EXISTS password_resets (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, token TEXT, expires INTEGER, used INTEGER DEFAULT 0)'); } catch(e) {}
try { sessionsDb.exec('CREATE TABLE IF NOT EXISTS sessions"""
print('db_init bulundu:', old_db_init in s)
s = s.replace(old_db_init, new_db_init)

# Sifre sifirlama endpoint'leri
old_marker = "// ============ PROFİL YÖNETİMİ ============"
new_routes = """// ============ ŞİFRE SIFIRLAMA ============
app.post('/api/hotel/forgot-password', async (req, res) => {
  const { username } = req.body || {};
  if (!username) return res.status(400).json({error:'Kullanici adi gerekli'});
  const u = D.db.prepare('SELECT * FROM hotel_users WHERE username=?').get(username);
  if (!u) return res.status(404).json({error:'Kullanici bulunamadi'});
  if (!u.email) return res.status(400).json({error:'Bu hesaba kayitli e-posta yok. IK ile iletisime gecin.'});
  const token = require('crypto').randomBytes(32).toString('hex');
  const expires = Date.now() + 3600000; // 1 saat
  D.db.prepare('INSERT INTO password_resets (username, token, expires) VALUES (?,?,?)').run(username, token, expires);
  const resetLink = 'https://gecitpdks.duckdns.org/v2.html?reset=' + token;
  try {
    await resend.emails.send({
      from: 'Gecit PDKS <onboarding@resend.dev>',
      to: u.email,
      subject: 'Gecit PDKS - Sifre Sifirlama',
      html: '<div style="font-family:sans-serif;max-width:480px;margin:0 auto;padding:24px"><h2 style="color:#F2B53B">Gecit PDKS</h2><p>Merhaba <b>' + u.name + '</b>,</p><p>Sifre sifirlama talebiniz alindi. Asagidaki butona tiklayarak yeni sifrenizi belirleyebilirsiniz.</p><a href="' + resetLink + '" style="display:inline-block;background:#F2B53B;color:#1a1205;padding:12px 24px;border-radius:8px;text-decoration:none;font-weight:700;margin:16px 0">Sifremi Sifirla</a><p style="color:#666;font-size:12px">Bu link 1 saat gecerlidir. Talebiniz yoksa bu e-postay gormezden gelin.</p></div>'
    });
    res.json({ok:true,message:'Sifirlama linki e-postaniza gonderildi'});
  } catch(e) {
    console.log('Mail hata:', e.message);
    res.status(500).json({error:'Mail gonderilemedi: '+e.message});
  }
});

app.post('/api/hotel/reset-password', async (req, res) => {
  const { token, newPass } = req.body || {};
  if (!token || !newPass) return res.status(400).json({error:'Token ve yeni sifre gerekli'});
  if (newPass.length < 6) return res.status(400).json({error:'Sifre en az 6 karakter olmali'});
  const reset = D.db.prepare('SELECT * FROM password_resets WHERE token=? AND used=0 AND expires>?').get(token, Date.now());
  if (!reset) return res.status(400).json({error:'Gecersiz veya suresi dolmus link'});
  const newHash = D.bcrypt.hashSync(newPass, 10);
  D.db.prepare('UPDATE hotel_users SET pass_hash=? WHERE username=?').run(newHash, reset.username);
  D.db.prepare('UPDATE password_resets SET used=1 WHERE id=?').run(reset.id);
  res.json({ok:true,message:'Sifreniz guncellendi'});
});

// ============ PROFİL YÖNETİMİ ============"""

print('marker bulundu:', old_marker in s)
s = s.replace(old_marker, new_routes)

open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
