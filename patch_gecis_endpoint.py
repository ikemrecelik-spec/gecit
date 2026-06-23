s = open('server.js', encoding='utf-8').read()

NEW_ENDPOINT = """
// ============ GELİŞMİŞ GİRİŞ/ÇIKIŞ LİSTESİ ============
app.get('/api/:tenant/attendance/report', authTenant, (req, res) => {
  const t = req.params.tenant;
  const start = req.query.start;
  const end = req.query.end;
  if (!start || !end) return res.status(400).json({error:'start ve end gerekli'});

  // Tüm aktif personel
  const emps = D.listEmployees(t).filter(e => e.status === 'aktif');
  
  // Tarih aralığındaki attendance kayıtları
  const attRows = D.db.prepare('SELECT * FROM attendance WHERE tenant_id=? AND day>=? AND day<=? ORDER BY day, ts').all(t, start, end);
  
  // Tarih aralığındaki shift planları
  const shiftRows = D.db.prepare('SELECT * FROM shift_plan WHERE tenant_id=?').all(t);
  const shiftMap = {};
  shiftRows.forEach(r => {
    const days = JSON.parse(r.days || '{}');
    Object.keys(days).forEach(date => {
      if (date >= start && date <= end) {
        if (!shiftMap[r.tc]) shiftMap[r.tc] = {};
        shiftMap[r.tc][date] = days[date];
      }
    });
  });

  // Ayarlardan vardiya tanımlarını al
  const settings = D.getSettings(t);
  const shiftDefs = (settings && settings.shifts) || [];

  // Tarih listesi oluştur
  const dates = [];
  const d = new Date(start);
  const endD = new Date(end);
  while (d <= endD) {
    dates.push(d.toISOString().slice(0,10));
    d.setDate(d.getDate()+1);
  }

  // Her personel + her gün için satır oluştur
  const rows = [];
  emps.forEach(emp => {
    dates.forEach(day => {
      const shiftCode = shiftMap[emp.tc] && shiftMap[emp.tc][day];
      const att = attRows.filter(r => r.tc === emp.tc && r.day === day);
      
      if (att.length > 0) {
        // Giriş kaydı var
        att.forEach(a => {
          const plannedShift = shiftCode || '-';
          const actualShift = a.vardiya || '-';
          const shiftMismatch = shiftCode && shiftCode !== '-' && actualShift !== '-' && 
            !actualShift.startsWith(shiftCode.split(' ')[0]);
          rows.push({
            id: a.id,
            tc: emp.tc,
            sicil: emp.sicil,
            ad: emp.ad,
            dep: emp.dep,
            gorev: emp.gorev,
            day: day,
            plannedShift: plannedShift,
            vardiya: actualShift,
            shiftMismatch: shiftMismatch,
            giris: a.giris,
            cikis: a.cikis,
            off: a.off,
            fm: a.fm,
            status: a.cikis ? 'tamamlandi' : 'cikis_yok'
          });
        });
      } else if (shiftCode && shiftCode !== '-' && shiftCode !== 'OFF') {
        // Shift var ama gelmemiş
        const dow = new Date(day).getDay();
        const isHT = (shiftCode === 'HT');
        rows.push({
          id: null,
          tc: emp.tc,
          sicil: emp.sicil,
          ad: emp.ad,
          dep: emp.dep,
          gorev: emp.gorev,
          day: day,
          plannedShift: shiftCode,
          vardiya: null,
          shiftMismatch: false,
          giris: null,
          cikis: null,
          off: 0,
          fm: 0,
          status: isHT ? 'ht' : 'gelmedi'
        });
      }
    });
  });

  // Vardiyaya göre sırala
  const SHIFT_ORDER = {'Gece': 0, 'A': 1, 'Ara': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 6};
  rows.sort((a, b) => {
    if (a.day !== b.day) return a.day.localeCompare(b.day);
    const sa = SHIFT_ORDER[a.plannedShift && a.plannedShift.split(' ')[0]] ?? 99;
    const sb = SHIFT_ORDER[b.plannedShift && b.plannedShift.split(' ')[0]] ?? 99;
    return sa - sb;
  });

  res.json(rows);
});

"""

marker = "app.get('/health'"
print('marker bulundu:', marker in s)
s = s.replace(marker, NEW_ENDPOINT + marker, 1)
open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
