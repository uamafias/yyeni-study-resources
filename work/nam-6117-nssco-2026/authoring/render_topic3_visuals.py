"""Generate Materials diagrams and the original water-uptake dataset."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
W=Path(__file__).resolve().parents[1];D=W/'topics/3/visuals';D.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
def save(fig,name):
 fig.savefig(D/(name+'.svg'),bbox_inches='tight');fig.savefig(D/(name+'.png'),dpi=130,bbox_inches='tight');plt.close(fig)
fig,ax=plt.subplots(figsize=(8,6));ax.set_aspect('equal');ax.set_xlim(-3,3);ax.set_ylim(-2.5,2.5);ax.axis('off');ax.set_title('Cleaning molecules around grease — teaching reference')
ax.add_patch(Rectangle((-3,-2.5),6,5,fc='#e9f4fa'));ax.add_patch(Circle((0,0),1.25,fc='#e4c581'));ax.text(0,0,'grease droplet',ha='center')
for a in np.linspace(0,2*np.pi,16,endpoint=False):
 u=np.array([np.cos(a),np.sin(a)]);ax.plot(*np.array([.75*u,1.42*u]).T,c='#444',lw=2);ax.add_patch(Circle(1.48*u,.11,fc='#266f9b'))
ax.text(-2.7,2,'water',color='#266f9b');ax.annotate('hydrophilic head',xy=(1.48,0),xytext=(1.65,1.75),arrowprops={'arrowstyle':'->'});ax.annotate('hydrophobic tail',xy=(.9,-.4),xytext=(.8,-2.1),arrowprops={'arrowstyle':'->'})
save(fig,'VIS-6117-3-01')
fig,ax=plt.subplots(figsize=(10,3));ax.set_xscale('log');ax.set_xlim(.7e-9,1.4e-3);ax.set_ylim(0,1);ax.set_yticks([]);ax.set_xlabel('Size / m — logarithmic spacing (equal steps represent multiplication)');ax.set_xticks([1e-9,1e-7,1e-6,1e-3],['1 nm\n10⁻⁹ m','100 nm\n10⁻⁷ m','1 μm\n10⁻⁶ m','1 mm\n10⁻³ m']);ax.axvspan(1e-9,1e-7,color='#d2e9f4');ax.text(1e-8,.6,'Approximate nanoscale range\n1–100 nm',ha='center');ax.set_title('Size comparison — not a linear scale')
save(fig,'VIS-6117-3-02')
fig,axs=plt.subplots(1,3,figsize=(12,4))
for ax in axs:ax.axis('off');ax.set_xlim(0,5);ax.set_ylim(0,5)
a=axs[0];a.set_title('1. Immerse');a.plot([1,1,4,4],[4,1,1,4],c='black');a.add_patch(Rectangle((1.05,1.05),2.9,2.2,fc='#c8e7f1'));a.add_patch(Rectangle((1.8,1.5),1.1,1.3,fc='#b9a08b',ec='#555',hatch='///'));a.annotate('fabric fully immersed',xy=(2.3,2.1),xytext=(.1,.3),arrowprops={'arrowstyle':'->'});a.text(1.5,3.5,'water beaker')
a=axs[1];a.set_title('2. Drain for a fixed time');a.plot([.5,4.5],[1.8,1.8],c='black',lw=2);a.plot([1,1],[.5,1.8],c='black');a.plot([4,4],[.5,1.8],c='black');a.add_patch(Rectangle((1.7,1.85),1.3,.5,fc='#b9a08b',ec='#555',hatch='///'));a.text(1.3,1,'draining rack');a.plot([2,2.6,3.2],[3.5,2.6,3.5],c='#555');a.text(3.3,3.5,'tongs');a.add_patch(Circle((.6,4),.35,fill=False));a.plot([.6,.6,.8],[4.2,4,3.9],c='black');a.text(1.1,4,'stopwatch')
a=axs[2];a.set_title('3. Weigh in a dry area');a.add_patch(Rectangle((.6,.7),3.8,1.4,fill=False));a.add_patch(Rectangle((1.4,1.1),2.2,.6,fc='#dbe7de',ec='black'));a.text(2.5,1.4,'mass / g',ha='center',va='center');a.plot([1,4],[2.2,2.2],c='black',lw=3);a.add_patch(Rectangle((1.5,2.25),2,.25,fill=False));a.add_patch(Rectangle((1.8,2.5),1.3,.5,fc='#b9a08b',hatch='///'));a.text(.4,3.5,'Tared tray supports the fabric.\nKeep spills from electronics.');a.text(1.5,.2,'balance')
save(fig,'VIS-6117-3-03')
fig,axs=plt.subplots(1,2,figsize=(8,3))
for ax,label,value in zip(axs,['Dry sample','Drained-wet sample'],['10.0 g','14.0 g']):
 ax.axis('off');ax.set_title(label);ax.add_patch(Rectangle((.1,.2),.8,.6,transform=ax.transAxes,fill=False));ax.add_patch(Rectangle((.2,.35),.6,.3,transform=ax.transAxes,fc='#dbe7de'));ax.text(.5,.5,value,ha='center',va='center',fontsize=24,transform=ax.transAxes)
save(fig,'VIS-6117-3-readings')
x=np.array([0,1,2,3,4,5],float);y=np.array([0,1.8,2.8,3.4,3.8,4.0]);slopes=np.diff(y);m=np.zeros(6);m[0]=slopes[0];m[-1]=slopes[-1]
for i in range(1,5):m[i]=2*slopes[i-1]*slopes[i]/(slopes[i-1]+slopes[i])
xx=[];yy=[]
for i in range(5):
 t=np.linspace(0,1,31);xx.extend(i+t);yy.extend((2*t**3-3*t**2+1)*y[i]+(t**3-2*t**2+t)*m[i]+(-2*t**3+3*t**2)*y[i+1]+(t**3-t**2)*m[i+1])
assert np.all(np.diff(yy)>=-1e-10)
for answer in [False,True]:
 fig,ax=plt.subplots(figsize=(7,5));ax.set_xlim(0,5);ax.set_ylim(0,4.5);ax.set_xticks(range(6));ax.set_yticks(np.arange(0,4.6,.5));ax.minorticks_on();ax.grid(which='both',alpha=.3);ax.set_xlabel('Immersion time / min');ax.set_ylabel('Water uptake / g');ax.set_title('Water uptake — '+('answer curve' if answer else 'plot the supplied data'))
 if answer:ax.plot(xx,yy,c='#267393');ax.plot(x,y,'x',color='#267393')
 save(fig,'VIS-6117-3-graph-'+('answer' if answer else 'blank'))
(D/'parameters.json').write_text(json.dumps({'dry_mass_g':10.0,'wet_mass_g':14.0,'uptake_g':14.0-10.0,'graph':{'x':x.tolist(),'y':y.tolist(),'interpolation':'monotone cubic Hermite; exact supplied points'},'nanometre_m':1e-9,'source':'Original synthetic teaching data.'},indent=2)+'\n')
print('Three required figures, two balance readings and learner/answer graphs generated.')
