"""Reproducible original reporting diagrams; edges express direct reports."""
from pathlib import Path
import json
from PIL import Image,ImageDraw,ImageFont
D=Path(__file__).resolve().parent/'diagrams';D.mkdir(exist_ok=True)
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
def render(name,title,nodes,edges):
 im=Image.new('RGB',(1200,600),'white');d=ImageDraw.Draw(im);font=ImageFont.truetype(FONT,22);small=ImageFont.truetype(FONT,18)
 d.text((600,28),title,fill='#17324d',font=ImageFont.truetype(FONT,28),anchor='mt')
 for a,b in edges:
  x,y,_=nodes[a];xx,yy,_=nodes[b];mid=(y+yy)//2
  d.line([(x,y+29),(x,mid),(xx,mid),(xx,yy-29)],fill='#405d73',width=3)
 for key,(x,y,label) in nodes.items():
  d.rounded_rectangle((x-122,y-29,x+122,y+29),radius=8,fill='#edf4fa',outline='#17324d',width=2)
  d.text((x,y),label,fill='#17324d',font=font,anchor='mm')
 d.text((600,557),'Lines show direct reporting relationships. People at the same level do not report to one another.',fill='#334c5e',font=small,anchor='mm')
 im.save(D/(name+'.png'))
 record={'title':title,'nodes':nodes,'edges':edges,'direct_spans':{a:sum(x==a for x,y in edges) for a in nodes}}
 (D/(name+'.json')).write_text(json.dumps(record,indent=2)+'\n')
 assert all(a in nodes and b in nodes for a,b in edges)
 assert len({b for a,b in edges})==len(edges),'Each non-top role has one manager'
 return record
r=render('omano-reporting','Omano Supplies: reporting structure',{'owner':(600,110,'Owner-manager'),'production':(210,275,'Production head'),'sales':(600,275,'Sales head'),'finance':(990,275,'Finance head'),'worker_a':(145,445,'Worker A'),'worker_b':(415,445,'Worker B'),'seller':(730,445,'Sales assistant'),'clerk':(1000,445,'Accounts clerk')},[('owner','production'),('owner','sales'),('owner','finance'),('production','worker_a'),('production','worker_b'),('sales','seller'),('finance','clerk')])
assert r['direct_spans']['owner']==3 and r['direct_spans']['production']==2
render('tuli-reporting','Tuli Foods: proposed functional structure',{'general':(600,110,'General manager'),'production':(210,275,'Production head'),'sales':(600,275,'Sales head'),'finance':(990,275,'Finance head'),'team':(210,445,'Production team'),'seller':(600,445,'Sales assistant'),'clerk':(990,445,'Accounts clerk')},[('general','production'),('general','sales'),('general','finance'),('production','team'),('sales','seller'),('finance','clerk')])
print('Two original charts rendered; direct spans and single-manager reporting verified.')
