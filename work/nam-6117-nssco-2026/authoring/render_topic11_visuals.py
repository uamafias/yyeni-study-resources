from visual_panels import save_panels
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
D=Path(__file__).resolve().parents[1]/'topics/11/visuals';D.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
def save(fig,n):
 fig.savefig(D/(n+'.svg'),bbox_inches='tight');fig.savefig(D/(n+'.png'),dpi=130,bbox_inches='tight');plt.close(fig)
def box(ax,x,y,w,h,text):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.04',fc='#e8f1f3',ec='#456575'));ax.text(x+w/2,y+h/2,text,ha='center',va='center')
def arrow(ax,a,b):ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':'#456575','lw':1.6})
fig,ax=plt.subplots(figsize=(15,5));ax.axis('off');ax.set_xlim(0,15);ax.set_ylim(0,5)
for x,text in [(0.2,'Raw\nwater'),(2.6,'Screening'),(5,'Sedimentation'),(7.4,'Filtration'),(9.8,'Chlorination'),(12.2,'Treated\nwater')]:box(ax,x,2.7,2,1,text)
for x in [2.2,4.6,7,9.4,11.8]:arrow(ax,(x,3.2),(x+.35,3.2))
for x,label in [(3.6,'Large debris'),(6,'Sediment / sludge'),(8.4,'Retained solids')]:arrow(ax,(x,2.7),(x,1.7));ax.text(x,1.4,label,ha='center',fontsize=10)
ax.text(10.8,1.4,'Disinfection:\ncontrolled dose\nand contact time',ha='center',fontsize=10)
ax.text(7.5,.3,'Outline for suitable raw water. Sewage reuse needs additional treatment and testing. Filtration does not remove dissolved salts.',ha='center',fontsize=10)
ax.set_title('Treatment stages perform different jobs',fontsize=16);save(fig,'VIS-6117-11-01')
fig,ax=plt.subplots(figsize=(13,7));ax.axis('off');ax.set_xlim(0,14);ax.set_ylim(0,8)
for x,text in [(.2,'Air'),(3,'Remove water\nvapour and CO₂'),(6,'Compress, cool\nand expand'),(9,'Liquid air')]:box(ax,x,5.5,2.3,1.2,text)
for x in [2.5,5.3,8.3]:arrow(ax,(x,6.1),(x+.45,6.1))
box(ax,8.7,2,3,1.5,'Fractional\ndistillation');arrow(ax,(10.2,5.5),(10.2,3.5))
box(ax,1,2.9,4.4,1,'Nitrogen — more volatile\nBoiling point ≈ −196 °C');box(ax,1,.8,4.4,1,'Oxygen — higher boiling\nBoiling point ≈ −183 °C')
arrow(ax,(8.7,3),(5.4,3.4));arrow(ax,(8.7,2.3),(5.4,1.3))
ax.text(7,.2,'Pretreatment avoids frozen water/CO₂ blockages. Values are boiling points at atmospheric pressure.',ha='center',fontsize=10)
ax.set_title('Separating nitrogen and oxygen already present in air',fontsize=16);save(fig,'VIS-6117-11-02')
fig,axs=plt.subplots(2,1,figsize=(15,10))
for ax in axs:ax.axis('off');ax.set_xlim(0,15);ax.set_ylim(0,5)
ax=axs[0];ax.set_title('Haber process — typical conditions',fontsize=15)
box(ax,.2,2.5,2.7,1.4,'N₂ from air\nH₂ from processing\nhydrocarbons + steam');box(ax,4,2.5,4.3,1.4,'N₂(g) + 3H₂(g) ⇌ 2NH₃(g)\nIron catalyst\n≈450 °C; ≈200 atm');box(ax,9.5,2.5,2.3,1.4,'Cool to\ncondense NH₃');box(ax,12.5,2.5,2.2,1.4,'Liquid\nammonia')
for a,b in [(2.9,4),(8.3,9.5),(11.8,12.5)]:arrow(ax,(a,3.2),(b,3.2))
ax.plot([10.6,10.6,5.8],[2.5,1,1],c='#456575');arrow(ax,(5.8,1),(5.8,2.5));ax.text(8, .5,'Unreacted N₂ and H₂ recycled',ha='center')
ax=axs[1];ax.set_title('Contact process — essential sequence',fontsize=15)
box(ax,.2,2.5,2.2,1.5,'Sulfur + air\nS + O₂ → SO₂\nPurify gas');box(ax,3.4,2.5,4.6,1.5,'2SO₂(g) + O₂(g) ⇌ 2SO₃(g)\nV₂O₅ catalyst\n≈450 °C; ≈1–2 atm');box(ax,9,2.5,2.4,1.5,'Absorb SO₃ in\nconcentrated H₂SO₄\n→ oleum');box(ax,12.2,2.5,2.6,1.5,'Carefully dilute\nwith water\n→ sulfuric acid')
for a,b in [(2.4,3.4),(8,9),(11.4,12.2)]:arrow(ax,(a,3.2),(b,3.2))
ax.text(7.5,1.2,'Do not replace the absorption stage with uncontrolled direct SO₃ + water mixing.',ha='center',fontsize=11)
fig.tight_layout();save(fig,'VIS-6117-11-03')
fig=plt.figure(figsize=(15,10));gs=fig.add_gridspec(1,3,width_ratios=[1.4,1,1]);ax=fig.add_subplot(gs[0]);ax.axis('off');ax.set_xlim(0,8);ax.set_ylim(0,10);ax.set_title('Hardness comparison apparatus')
# Burette has open top, bottom tap/tip; stand and clamp do not obstruct the tube.
ax.plot([2,2],[.5,9],c='#444',lw=3);ax.plot([1.4,2.6],[.5,.5],c='#444',lw=4);ax.plot([2,3.2],[7.6,7.6],c='#444',lw=2)
ax.plot([3,3,3.5,3.5],[9,4,4,9],c='#444',lw=1.5);ax.plot([3.25,3.25],[4,3.4],c='#444');ax.plot([2.9,3.6],[3.85,3.85],c='#444',lw=3)
for y in [4.4+i*.35 for i in range(13)]:ax.plot([3,y*0+3.15],[y,y],c='#444',lw=.6)
ax.add_patch(Rectangle((2.65,1.4),1.2,1.8,fc='#e7f3f5',ec='#444'));ax.text(4.1,2,'Comparison tube\nstopper removed for addition',fontsize=10);ax.text(4.1,6.6,'Burette with\nsoap solution\n\nStand and clamp',fontsize=10)
ax.add_patch(Rectangle((5.3,.6),1.1,.15,fc='#777'));ax.text(5.85,.2,'Stopper for shaking',ha='center',fontsize=9)
ax.add_patch(Rectangle((.1,2),1.2,2.4,fill=False));ax.plot([0,1.5],[1.9,1.9],c='#444');
for i in range(6):ax.plot([.1,.4],[2.2+i*.35,2.2+i*.35],c='#444',lw=.7)
ax.text(.7,5,'50 cm³\nmeasuring\ncylinder',ha='center',fontsize=9)
for col,keyed in [(1,False),(2,True)]:
 a=fig.add_subplot(gs[col]);a.axis('off');a.set_xlim(-1,5);a.set_ylim(-.2,8.5);a.set_title('Answer readings' if keyed else 'Learner: sample B readings')
 for x,base,value,title in [(0,0,.4,'Initial'),(3,6,6.4,'Final')]:
  a.add_patch(Rectangle((x,1),.8,5,fill=False,ec='#444'))
  # 1 cm³ segment: scale increases downwards. Meniscus minimum at y=4.
  yy=6-(value-base)*5
  import numpy as np
  xx=np.linspace(x+.04,x+.76,100);curve=yy+.25*((xx-(x+.4))/.36)**2
  a.fill_between(xx,1,curve,fc='#dceff2');a.plot(xx,curve,c='#2e687c',lw=1.5)
  for i in range(11):
   y=6-i*.5;a.plot([x,x+(.3 if i%5==0 else .18)],[y,y],c='#444',lw=.7)
   if i%5==0:a.text(x-.12,y,f'{base+i/10:.1f}',ha='right',va='center',fontsize=10)
  a.text(x+.4,6.8,title,ha='center');a.text(x+.4,.5,'cm³',ha='center')
  if keyed:a.text(x+.4,7.5,f'{value:.2f} cm³',ha='center',fontsize=12)
 a.text(1.8,-.05,'Read the lower meniscus at eye level.',ha='center',fontsize=9)
fig.suptitle('Soap-volume measurements — equal 50.0 cm³ water portions; 30 s persistent-lather endpoint',fontsize=14)
fig.tight_layout(rect=[0,.02,1,.95]);save_panels(fig,D,'VIS-6117-11-04',{'learner':[1],'answer':[0,2]});save(fig,'VIS-6117-11-04')
assert abs((6.4-.4)-6)<1e-10 and abs((2.2-.2)-2)<1e-10
assert 120/5*60*24/1000==34.56
(D/'parameters.json').write_text(json.dumps({'soap_A_cm3':2.2-.2,'soap_B_cm3':6.4-.4,'burette_divisions_cm3':.1,'leak_litres_day':120/5*60*24/1000,'emissions_A_kg_per_person':120000*1000/12000000,'emissions_B_kg_per_person':60000*1000/3000000,'gas_separation_boiling_C':{'N2':-196,'O2':-183}},indent=2)+'\n')
