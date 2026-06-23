for fn in ['v2.html','gecit-site-v1.html','panel.html']:
    s = open(fn, encoding='utf-8').read()
    
    old = """  document.querySelectorAll('.cell').forEach(function(cell){
    cell.addEventListener('click',function(){
      var tc=cell.dataset.tc;
      var date=cell.dataset.date;
      if(!plan[tc])plan[tc]={};
      var cur=plan[tc][date]||'OFF';
      var idx=CYCLE.indexOf(cur);
      var next=CYCLE[(idx+1)%CYCLE.length];
      plan[tc][date]=next;
      var sh=SHIFT_MAP[next]||SHIFT_MAP['OFF'];
      cell.textContent=next;
      cell.style.background=sh.bg;
      cell.style.color=sh.color;
      cell.style.borderColor=sh.color+'33';
    });
  });
}"""
    
    new = """  var activeMenu=null;
  function closeMenu(){if(activeMenu){activeMenu.remove();activeMenu=null;}}
  document.addEventListener('click',function(e){if(activeMenu&&!activeMenu.contains(e.target))closeMenu();});

  document.querySelectorAll('.cell').forEach(function(cell){
    cell.addEventListener('click',function(e){
      e.stopPropagation();
      closeMenu();
      var tc=cell.dataset.tc;
      var date=cell.dataset.date;
      var menu=document.createElement('div');
      menu.style.cssText='position:fixed;background:#0E1A24;border:1px solid #23414F;border-radius:10px;padding:6px;z-index:99;box-shadow:0 16px 40px rgba(0,0,0,.6);min-width:190px;max-height:300px;overflow-y:auto;';
      var rect=cell.getBoundingClientRect();
      menu.style.left=Math.min(rect.left,window.innerWidth-210)+'px';
      menu.style.top=(rect.bottom+4)+'px';
      SHIFTS.forEach(function(sh){
        var item=document.createElement('div');
        item.style.cssText='padding:7px 12px;border-radius:7px;cursor:pointer;font-family:JetBrains Mono,monospace;font-weight:700;font-size:11.5px;color:'+sh.color+';background:'+sh.bg+';margin-bottom:2px;';
        item.textContent=sh.code+(sh.label.indexOf(' - ')>=0?' — '+sh.label.split(' - ').slice(1).join(' - '):'');
        item.addEventListener('mouseenter',function(){item.style.filter='brightness(1.2)';});
        item.addEventListener('mouseleave',function(){item.style.filter='';});
        item.addEventListener('click',function(ev){
          ev.stopPropagation();
          if(!plan[tc])plan[tc]={};
          plan[tc][date]=sh.code;
          cell.textContent=sh.code;
          cell.style.background=sh.bg;
          cell.style.color=sh.color;
          cell.style.borderColor=sh.color+'33';
          closeMenu();
        });
        menu.appendChild(item);
      });
      var delItem=document.createElement('div');
      delItem.style.cssText='padding:7px 12px;border-radius:7px;cursor:pointer;font-size:11.5px;color:#FF6B6B;margin-top:3px;border-top:1px solid #23414F;';
      delItem.textContent='— Temizle';
      delItem.addEventListener('click',function(ev){
        ev.stopPropagation();
        if(plan[tc])delete plan[tc][date];
        cell.textContent='-';
        var sh=SHIFT_MAP['-']||{bg:'#141e24',color:'#23414F'};
        cell.style.background=sh.bg;
        cell.style.color=sh.color;
        cell.style.borderColor=sh.color+'33';
        closeMenu();
      });
      menu.appendChild(delItem);
      document.body.appendChild(menu);
      activeMenu=menu;
    });
  });
}"""
    
    found = old in s
    s = s.replace(old, new)
    open(fn, 'w', encoding='utf-8').write(s)
    print(fn, '->', found)
