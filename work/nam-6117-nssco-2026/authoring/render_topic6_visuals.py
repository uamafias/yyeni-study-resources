from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
D=Path(__file__).resolve().parents[1]/'topics/6/visuals';D.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
def save(fig,name):
 fig.savefig(D/(name+'.svg'),bbox_inches='tight');fig.savefig(D/(name+'.png'),dpi=140,bbox_inches='tight');plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(12,5))
for ax,start,end,title in zip(axs,[80,30],[30,80],['Exothermic','Endothermic']):
 x=np.linspace(0,1,100);ramp=(1-np.cos(np.pi*x))/2
 ax.plot(np.r_[x,x+1],np.r_[start+(140-start)*ramp,140+(end-140)*ramp],c='#245d80',lw=2)
 ax.hlines(start,-.2,.15,color='#245d80');ax.hlines(end,1.85,2.2,color='#245d80');ax.text(-.15,start+6,'Reactants');ax.text(1.55,end+6,'Products')
 ax.annotate('',xy=(.65,140),xytext=(.65,start),arrowprops={'arrowstyle':'<->'});ax.text(.1,115 if start==80 else 90,f'Activation\nenergy = {140-start}')
 ax.annotate('',xy=(2.25,end),xytext=(2.25,start),arrowprops={'arrowstyle':'->','color':'#a63e35'});ax.text(1.65,(start+end)/2,f'ΔH = {end-start:+d}',color='#a63e35')
 ax.set_xlim(-.25,2.55);ax.set_ylim(0,165);ax.set_xlabel('Reaction progress');ax.set_ylabel('Energy / arbitrary units');ax.set_xticks([]);ax.set_title(title)
fig.tight_layout();save(fig,'VIS-6117-6-01')
x=np.array([0,20,40,60,80,100,120.]);slow=np.array([0,18,30,38,43,46,48.]);fast=np.array([0,28,41,47,48,48,48.])
def curve(y):
 d=np.diff(y)/20;m=np.zeros(len(y));m[0]=d[0];m[-1]=d[-1]
 for i in range(1,len(y)-1):
  m[i]=2*d[i-1]*d[i]/(d[i-1]+d[i]) if d[i-1]*d[i]>0 else 0
 xx=[];yy=[]
 for i in range(len(y)-1):
  t=np.linspace(0,1,40);v=(2*t**3-3*t**2+1)*y[i]+(t**3-2*t**2+t)*20*m[i]+(-2*t**3+3*t**2)*y[i+1]+(t**3-t**2)*20*m[i+1]
  xx.extend(x[i]+20*t);yy.extend(v)
 assert min(yy)>=-1e-8 and max(yy)<=48+1e-8
 return np.array(xx),np.array(yy)
for mode in ['both','blank','chip-answer']:
 fig,ax=plt.subplots(figsize=(8,5));ax.set_xlim(0,120);ax.set_ylim(0,50);ax.set_xticks(x);ax.set_yticks(np.arange(0,51,10));ax.set_xlabel('Time / s');ax.set_ylabel('CO₂ volume / cm³');ax.grid(alpha=.3)
 if mode!='blank':
  ax.plot(*curve(slow),label='Curve A',c='#246987');ax.scatter(x,slow,c='#246987',s=18)
 if mode=='both':
  ax.plot(*curve(fast),label='Curve B',c='#b04d36');ax.scatter(x,fast,c='#b04d36',s=18);ax.legend()
 ax.set_title('Gas collection over time' if mode!='blank' else 'Learner plotting grid')
 save(fig,'VIS-6117-6-02' if mode=='both' else 'VIS-6117-6-'+mode)
assert np.all(curve(fast)[1]>=curve(slow)[1]-1e-8)
fig,ax=plt.subplots(figsize=(11,6));ax.axis('off');ax.set_xlim(0,12);ax.set_ylim(0,7)
ax.add_patch(Rectangle((.5,1.1),11,5,fc='#edf5fa',ec='#333',lw=2));ax.text(6,6.5,'Closed vessel — N₂(g) + 3H₂(g) ⇌ 2NH₃(g)',ha='center',fontsize=14)
# Stoichiometric groups, NOT a claim of equal amounts at equilibrium.
for cx,cy,col in [(2,4.5,'#477baf'),(2,3,'#f0c45e'),(3,3,'#f0c45e'),(4,3,'#f0c45e')]:
 for dx in [-.14,.14]:ax.add_patch(Circle((cx+dx,cy),.18,fc=col,ec='#333'))
ax.text(3,2.2,'1 N₂ + 3 H₂ per forward event',ha='center')
for cx in [8,9.5]:
 ax.add_patch(Circle((cx,4),.2,fc='#477baf',ec='#333'))
 for dx,dy in [(-.3,0),(.3,0),(0,.35)]:ax.add_patch(Circle((cx+dx,4+dy),.13,fc='#f0c45e',ec='#333'))
ax.text(8.75,2.2,'2 NH₃ per forward event',ha='center')
ax.annotate('',xy=(7,4.5),xytext=(4.7,4.5),arrowprops={'arrowstyle':'->','lw':2});ax.text(5.85,4.9,'Forward reaction',ha='center')
ax.annotate('',xy=(4.7,3.3),xytext=(7,3.3),arrowprops={'arrowstyle':'->','lw':2});ax.text(5.85,2.9,'Reverse reaction',ha='center')
ax.text(6,.45,'At equilibrium: equal continuing reaction rates; amounts need not be equal.\nParticle groups show equation ratios, not a snapshot of equilibrium composition.',ha='center')
save(fig,'VIS-6117-6-03')
(D/'parameters.json').write_text(json.dumps({'energy_profiles':[{'reactants':80,'peak':140,'products':30,'Ea':60,'deltaH':-50},{'reactants':30,'peak':140,'products':80,'Ea':110,'deltaH':50}],'time_s':x.tolist(),'slow_cm3':slow.tolist(),'fast_cm3':fast.tolist(),'average_rate_20_to_60':(38-18)/(60-20),'curve_checks':'monotone Hermite; bounded 0–48; fast never below slow','equilibrium':'stoichiometric event diagram, not composition snapshot'},indent=2)+'\n')
