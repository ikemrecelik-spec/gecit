s = open('server.js', encoding='utf-8').read()
old = '  } catch(e) { console.log(\'Approval check error:\', e.message); }\n});\n  if (!a.sicil) {'
new = '  } catch(e) { console.log(\'Approval check error:\', e.message); }\n  if (!a.sicil) {'
print('bulundu:', old in s)
s = s.replace(old, new)
open('server.js', 'w', encoding='utf-8').write(s)
print('OK')
