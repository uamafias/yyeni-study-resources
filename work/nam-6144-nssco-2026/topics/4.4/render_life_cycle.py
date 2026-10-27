from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json
D=Path(__file__).resolve().parent/'diagrams';D.mkdir(exist_ok=True)
im=Image.new('RGB',(1100,650),'white');d=ImageDraw.Draw(im);fp='/System/Library/Fonts/Supplemental/Arial.ttf';f=ImageFont.truetype(fp,21)
d.text((550,25),'Product life cycle: illustrative sales model',fill='#17324d',font=ImageFont.truetype(fp,28),anchor='mt')
d.line((110,90,110,520,1020,520),fill='#17324d',width=3);d.text((115,70),'Sales',fill='black',font=f);d.text((1020,550),'Time',fill='black',font=f,anchor='rm')
# Authored conceptual control points are data for a reproducible model, not claimed observations.
pts=[(150,490),(230,470),(300,410),(380,300),(460,210),(550,170),(640,170),(730,200),(810,280),(900,410)]
d.line(pts,fill='#1c7180',width=5,joint='curve')
for x in [300,460,730]:
 for y in range(105,520,14):d.line((x,y,x,y+7),fill='#b3c1ca',width=2)
for x,txt in [(205,'Introduction'),(380,'Growth'),(590,'Maturity'),(865,'Decline')]:d.text((x,575),txt,fill='#17324d',font=f,anchor='mm')
d.text((550,620),'Conceptual pattern; real products need not follow this exact path or timing.',fill='#334c5e',font=ImageFont.truetype(fp,18),anchor='mm');im.save(D/'product-life-cycle.png')
assert all(110<x<1020 and 90<y<520 for x,y in pts)
assert all(pts[i+1][1]<=pts[i][1] for i in range(5))
assert all(pts[i+1][1]>=pts[i][1] for i in range(6,9))
(D/'life-cycle-verification.json').write_text(json.dumps({'points':pts,'meaning':'Conceptual sales over time; not actual research data.','checks':['positive plotted sales','rising introduction/growth','near-level maturity','falling decline'],'shared_chart_model':'not applicable; direct assertions and visual inspection required'},indent=2)+'\n')
print('Life-cycle model generated and stage directions checked.')
