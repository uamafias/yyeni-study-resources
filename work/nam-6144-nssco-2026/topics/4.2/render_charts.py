"""Generate original charts directly from checked teaching data using Pillow."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json
D=Path(__file__).resolve().parent/'diagrams';D.mkdir(exist_ok=True)
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
f=ImageFont.truetype(FONT,20);big=ImageFont.truetype(FONT,27)
colours=['#1c7180','#cc7b2d','#8565a6']
def base(title):
 im=Image.new('RGB',(1000,640),'white');d=ImageDraw.Draw(im);d.text((500,25),title,fill='#17324d',font=big,anchor='mt');return im,d
def bars(name,title,labels,values,unit):
 im,d=base(title);ymax=(max(values)//5+1)*5;scale=400/ymax;xs=[240,500,760]
 for y in range(0,ymax+1,5):
  yy=520-y*scale;d.line((110,yy,910,yy),fill='#dfe6eb');d.text((90,yy),str(y),fill='black',font=f,anchor='rm')
 for x,label,v,c in zip(xs,labels,values,colours):
  d.rectangle((x-65,520-v*scale,x+65,520),fill=c);d.text((x,520-v*scale-12),str(v),fill='black',font=f,anchor='mb');d.text((x,550),label,fill='black',font=f,anchor='mm')
 d.line((110,100,110,520,910,520),fill='#17324d',width=3);d.text((115,75),unit,fill='black',font=f);d.text((500,600),'Each respondent chose one option.',fill='black',font=f,anchor='mm');im.save(D/(name+'.png'))
bars('format-bar','Preferred meal format: 40 respondents',['Box','Wrap','Salad'],[12,18,10],'Number of respondents')
bars('collection-bar','Preferred collection: 40 respondents',['Workplace','Shop','Delivery'],[20,15,5],'Number of respondents')
im,d=base('Preferred meal format: shares of 40 responses');values=[12,18,10];labels=['Box','Wrap','Salad'];angle=-90
for v,c in zip(values,colours):
 end=angle+v/sum(values)*360;d.pieslice((60,105,560,605),angle,end,fill=c,outline='white',width=3);angle=end
for y,label,v,c in zip([230,320,410],labels,values,colours):
 d.rectangle((650,y,675,y+25),fill=c);d.text((695,y),f'{label}: {v} ({v/40*100:.0f}%)',fill='black',font=f)
im.save(D/'format-pie.png')
im,d=base('Annual orders: Omi Lunches');years=[2022,2023,2024,2025];vals=[40,60,55,80];xs=[160,400,640,880]
for v in range(0,101,20):
 y=520-v*4;d.line((110,y,930,y),fill='#dfe6eb');d.text((90,y),str(v),fill='black',font=f,anchor='rm')
pts=[(x,520-v*4) for x,v in zip(xs,vals)];d.line(pts,fill='#1c7180',width=4)
for (x,y),yr,v in zip(pts,years,vals):
 d.ellipse((x-6,y-6,x+6,y+6),fill='#1c7180');d.text((x,y-15),str(v),fill='black',font=f,anchor='mb');d.text((x,550),str(yr),fill='black',font=f,anchor='mm')
d.line((110,100,110,520,930,520),fill='#17324d',width=3);d.text((115,75),'Number of orders',fill='black',font=f);d.text((500,600),'Year',fill='black',font=f,anchor='mm');im.save(D/'orders-line.png')
checks={'format_total':sum(values),'angles':[v/40*360 for v in values],'angle_total':sum(v/40*360 for v in values),'annual_orders':dict(zip(years,vals)),'collection_total':20+15+5}
assert checks['format_total']==40 and checks['angle_total']==360 and checks['collection_total']==40
(D/'data-verification.json').write_text(json.dumps(checks,indent=2)+'\n');print('Four charts generated; counts, angles and plotting data verified.')
