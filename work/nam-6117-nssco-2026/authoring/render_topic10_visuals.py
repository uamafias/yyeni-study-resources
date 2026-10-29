from visual_panels import save_panels
from pathlib import Path
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
D=Path(__file__).resolve().parents[1]/'topics/10/visuals';D.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
def save(fig,name):
 fig.savefig(D/(name+'.svg'),bbox_inches='tight');fig.savefig(D/(name+'.png'),dpi=130,bbox_inches='tight');plt.close(fig)
def atoms(ax,points,bonds):
 for a,b,k in bonds:
  x,y=points[a][1:];u,v=points[b][1:];dx=u-x;dy=v-y;l=math.hypot(dx,dy);nx=-dy/l;ny=dx/l
  for off in ([0] if k==1 else [-.055,.055]):ax.plot([x+dx*.20+nx*off,u-dx*.20+nx*off],[y+dy*.20+ny*off,v-dy*.20+ny*off],c='#354653',lw=1.5)
 for label,x,y in points:ax.text(x,y,label,ha='center',va='center',fontsize=15,color='#a43c30' if label=='O' else '#203c50',bbox={'fc':'white','ec':'none','pad':.4})
fig,axs=plt.subplots(2,2,figsize=(13,9))
data=[('Ethene — C=C',[('C',1,1),('C',2.4,1),('H',1,2),('H',1,0),('H',2.4,2),('H',2.4,0)],[(0,1,2),(0,2,1),(0,3,1),(1,4,1),(1,5,1)]),('Ethanol — alcohol –OH',[('C',0,1),('C',1.4,1),('O',2.8,1),('H',4,1),('H',0,2),('H',0,0),('H',-1.1,1),('H',1.4,2),('H',1.4,0)],[(0,1,1),(1,2,1),(2,3,1),(0,4,1),(0,5,1),(0,6,1),(1,7,1),(1,8,1)]),('Ethanoic acid — –COOH',[('C',0,1),('C',1.4,1),('O',1.4,2),('O',2.8,1),('H',4,1),('H',0,2),('H',0,0),('H',-1.1,1)],[(0,1,1),(1,2,2),(1,3,1),(3,4,1),(0,5,1),(0,6,1),(0,7,1)]),('Ethyl ethanoate — ester –COO–',[('C',0,1),('C',1.3,1),('O',1.3,2),('O',2.6,1),('C',3.9,1),('C',5.2,1),('H',0,2),('H',0,0),('H',-1,1),('H',3.9,2),('H',3.9,0),('H',5.2,2),('H',5.2,0),('H',6.2,1)],[(0,1,1),(1,2,2),(1,3,1),(3,4,1),(4,5,1),(0,6,1),(0,7,1),(0,8,1),(4,9,1),(4,10,1),(5,11,1),(5,12,1),(5,13,1)])]
for ax,(title,p,b) in zip(axs.flat,data):
 atoms(ax,p,b);ax.axis('off');ax.set_aspect('equal');ax.set_xlim(min(x for _,x,y in p)-.5,max(x for _,x,y in p)+.5);ax.set_ylim(-.6,2.6);ax.set_title(title)
 # Numerical check of displayed valencies and composition.
 val=[0]*len(p)
 for a,b,k in b:val[a]+=k;val[b]+=k
 assert all(v=={'C':4,'O':2,'H':1}[q[0]] for v,q in zip(val,p)),title
fig.suptitle('Displayed structures — every atom and bond shown',fontsize=16);fig.tight_layout();save(fig,'VIS-6117-10-01')
fig,axs=plt.subplots(3,1,figsize=(12,9))
for ax in axs:ax.axis('off');ax.set_xlim(-1,8);ax.set_ylim(-.4,2.6)
atoms(axs[0],[('R',0,1),('C',1.5,1),('O',1.5,2.2),('O',3,1),('R′',4.5,1)],[(0,1,1),(1,2,2),(1,3,1),(3,4,1)]);axs[0].text(6,1,'Ester linkage',ha='center');axs[0].set_title('R and R′ stand for carbon-containing portions')
atoms(axs[1],[('R',0,1),('C',1.5,1),('O',1.5,2.2),('N',3,1),('H',3,2.2),('R′',4.5,1)],[(0,1,1),(1,2,2),(1,3,1),(3,4,1),(3,5,1)]);axs[1].text(6,1,'Amide linkage',ha='center')
for x in [0,2.8,5.6]:axs[2].add_patch(Rectangle((x, .55),1.4,.9,fc='#dfeced',ec='#395968'));axs[2].text(x+.7,1,'Sugar\nunit',ha='center',va='center')
for x in [2.1,4.9]:axs[2].text(x,1,'O',ha='center',va='center');axs[2].plot([x-.7,x-.2],[1,1],c='#444');axs[2].plot([x+.2,x+.7],[1,1],c='#444')
axs[2].text(3.5,2.2,'Joining oxygen: schematic units, not full ring structures',ha='center');axs[2].plot([-.5,0],[1,1],c='#444');axs[2].plot([7,7.5],[1,1],c='#444')
fig.tight_layout();save(fig,'VIS-6117-10-02')
fig,axs=plt.subplots(2,1,figsize=(11,8))
for ax,name,sub in zip(axs,['Poly(ethene)','Poly(chloroethene)'],['H','Cl']):
 ax.axis('off');ax.set_xlim(-1,5.5);ax.set_ylim(-.5,3);ax.set_title(name)
 p=[('C',1,1),('C',2.7,1),('H',1,2.1),('H',1,-.1),('H',2.7,2.1),(sub,2.7,-.1)]
 atoms(ax,p,[(0,1,1),(0,2,1),(0,3,1),(1,4,1),(1,5,1)])
 ax.plot([-.1,.8],[1,1],c='#354653');ax.plot([2.9,3.8],[1,1],c='#354653')
 for x,sgn in [(.3,1),(3.4,-1)]:ax.plot([x+sgn*.2,x,x,x+sgn*.2],[2.5,2.5,-.4,-.4],c='#354653',lw=1.5)
 ax.text(3.65,-.3,'n',fontsize=16);ax.text(4.3,1,'Bonds cross\nboth brackets',va='center',fontsize=10)
fig.suptitle('Addition polymers — single bonds in the backbone',fontsize=15);fig.tight_layout();save(fig,'VIS-6117-10-03')
fig,axs=plt.subplots(1,3,figsize=(16,10),gridspec_kw={'width_ratios':[1,1.2,1.2]})
ax=axs[0];ax.axis('off');ax.set_xlim(-.3,5);ax.set_ylim(-1,11);ax.set_title('Starting setup')
ax.add_patch(Rectangle((.1,0),4.2,10,fill=False,lw=2));ax.add_patch(Rectangle((-.05,10),4.5,.25,fc='#888'));ax.add_patch(Rectangle((.15,.05),4.1,.45,fc='#c9e6f0'));ax.add_patch(Rectangle((.6,.1),3.2,9.2,fc='white',ec='#777'));ax.plot([.6,3.8],[1,1],c='#555',ls='--')
for x in [1.1,2.2,3.3]:ax.add_patch(Circle((x,1),.07,fc='#4f5760'))
ax.annotate('Pencil baseline',xy=(.8,1),xytext=(.4,2.2),arrowprops={'arrowstyle':'->'},fontsize=9);ax.text(.85,7.5,'Covered chamber\n\nSmall dried spots:\nsample + references\n\nSolvent below baseline',fontsize=10)
ax.annotate('Solvent',xy=(.4,.35),xytext=(1.5,-.6),arrowprops={'arrowstyle':'->'},fontsize=9)
for ax,answer in zip(axs[1:],[False,True]):
 ax.set_xlim(-1.3,5.5);ax.set_ylim(-.6,10.5);ax.set_aspect('equal');ax.axis('off');ax.set_title('Answer overlay' if answer else 'Learner panel — developed paper')
 ax.add_patch(Rectangle((0,0),4,10,fc='#fafaf5',ec='#777'));ax.plot([0,4],[1,1],c='#555',ls='--');ax.plot([0,4],[9,9],c='#45859d',ls='--')
 for x,ys in [(0.7,[3.4,5.8]),(2,[3.4]),(3.3,[5.8])]:
  for y in ys:ax.add_patch(Circle((x,y),.10,fc='#58616b'))
 for i in range(101):
  y=i/10;ax.plot([-.45,-.45-(.2 if i%10==0 else .1)],[y,y],c='#444',lw=.6)
  if i%10==0:ax.text(-.75,y,str(i//10),ha='right',va='center',fontsize=9)
 ax.text(-.8,10.3,'cm',ha='center',fontsize=10)
 for x,t in [(0.7,'Sample'),(2,'Glucose'),(3.3,'Sugar B')]:ax.text(x,-.3,t,ha='center',fontsize=9)
 ax.text(4.1,9,'Front',va='center',fontsize=9);ax.text(4.1,1,'Baseline',va='center',fontsize=9)
 if answer:
  for y,t in [(3.4,'2.4 cm\nRf 0.30'),(5.8,'4.8 cm\nRf 0.60')]:ax.annotate(t,xy=(.7,y),xytext=(1.5,y+.6),arrowprops={'arrowstyle':'->'},fontsize=9)
  ax.text(.3,7.6,'Front travels 8.0 cm\nfrom baseline',fontsize=10)
fig.suptitle('Chromatography model — ruler heights start at paper bottom',fontsize=15)
fig.text(.5,.03,'Distances for Rf start at the pencil baseline. Developed-paper panels are removed from the chamber; shaded/grey spots represent visualised components.',ha='center',fontsize=10)
fig.tight_layout(rect=[0,.06,1,.95]);save_panels(fig,D,'VIS-6117-10-04',{'learner':[0,1],'answer':[2]});save(fig,'VIS-6117-10-04')
(D/'parameters.json').write_text(json.dumps({'displayed_valency_check':'All C=4, O=2, H=1 in VIS-10-01','baseline_cm':1,'front_height_cm':9,'spot_heights_cm':[3.4,5.8],'travel_cm':[2.4,4.8],'Rf':[2.4/8,4.8/8],'absorption_g':[5.6-2,3.2-2],'cooling_C':[50-43,50-39]},indent=2)+'\n')
