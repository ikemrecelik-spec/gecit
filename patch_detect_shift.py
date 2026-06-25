s = open('db.js', encoding='utf-8').read()

old = """function detectShift(giris) {
  const [h, m] = giris.split(':').map(Number); const t = h * 60 + m;
  if (t >= 390 && t <= 570) return 'A \u00b7 08:00\u201316:00';
  if (t >= 630 && t <= 810) return 'Ara \u00b7 12:00\u201320:00';
  if (t >= 870 && t <= 1020) return 'B \u00b7 16:00\u201324:00';
  if (t >= 1380 || t <= 480) return 'Gece \u00b7 24:00\u201308:00';
  return 'A \u00b7 08:00\u201316:00';
}"""

new = """function detectShift(giris, tenantId) {
  const [h, m] = giris.split(':').map(Number); const t = h * 60 + m;
  try {
    const row = db.prepare('SELECT settings FROM tenant_settings WHERE tenant_id=?').get(tenantId);
    if (row) {
      const settings = JSON.parse(row.settings);
      const shifts = (settings && settings.shifts) || [];
      if (shifts.length > 0) {
        let best = null; let bestDiff = 9999;
        shifts.forEach(function(sh) {
          if (!sh.start) return;
          const sp = sh.start.split(':').map(Number);
          const st = sp[0]*60+(sp[1]||0);
          const tol = sh.tol || 60;
          let diff = Math.abs(t - st);
          if (diff > 720) diff = 1440 - diff;
          if (diff <= tol && diff < bestDiff) { bestDiff = diff; best = sh; }
        });
        if (best) return best.code + ' \u00b7 ' + best.start + '\u2013' + best.end;
      }
    }
  } catch(e) {}
  if (t >= 390 && t <= 570) return 'A \u00b7 08:00\u201316:00';
  if (t >= 630 && t <= 810) return 'Ara \u00b7 12:00\u201320:00';
  if (t >= 870 && t <= 1020) return 'B \u00b7 16:00\u201324:00';
  if (t >= 1380 || t <= 480) return 'Gece \u00b7 24:00\u201308:00';
  return 'A \u00b7 08:00\u201316:00';
}"""

print('bulundu:', old in s)
s = s.replace(old, new)

# punchIn'de detectShift cagrisina tenantId ekle
old2 = "detectShift(giris),"
new2 = "detectShift(giris, t),"
print('punchIn bulundu:', old2 in s)
s = s.replace(old2, new2)

open('db.js', 'w', encoding='utf-8').write(s)
print('OK')
