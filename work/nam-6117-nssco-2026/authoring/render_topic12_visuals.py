from visual_panels import save_panels
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
W=Path(__file__).resolve().parents[1];D=W/'topics/12/visuals';D.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
def save(fig,n):
 fig.savefig(D/(n+'.svg'),bbox_inches='tight');fig.savefig(D/(n+'.png'),dpi=130,bbox_inches='tight');plt.close(fig)
fig,axs=plt.subplots(2,3,figsize=(12,11))
for row,keyed in enumerate([False,True]):
 for col,(name,lo,hi,value,step) in enumerate([('Thermometer / °C',55,70,63,1),('Burette / cm³',6,7,6.4,.1),('Cylinder / cm³',30,40,36,1)]):
  ax=axs[row,col];ax.axis('off');ax.set_xlim(-1,2);ax.set_ylim(-.8,11.5);ax.set_title(name+('\nAnswer' if keyed else '\nLearner'))
  pos=lambda v:10*(1-(v-lo)/(hi-lo)) if col==1 else 10*(v-lo)/(hi-lo)
  ax.add_patch(Rectangle((0,0),.7,10,fill=False,ec='#444'))
  if col==0:
   ax.add_patch(Rectangle((.2,0),.3,pos(value),fc='#b34f48'));ax.add_patch(Circle((.35,-.25),.25,fc='#b34f48',ec='#444'))
  else:
   xx=np.linspace(.03,.67,100);yy=pos(value)+.20*((xx-.35)/.32)**2
   ax.fill_between(xx,0,yy,color='#d7edf2');ax.plot(xx,yy,c='#286579',lw=1.5)
  for i,v in enumerate(np.arange(lo,hi+step*.5,step)):
   y=pos(v);ax.plot([0,.22 if i%5==0 else .12],[y,y],c='#444',lw=.8)
   if i%5==0:ax.text(-.12,y,f'{v:.1f}' if col==1 else f'{v:.0f}',ha='right',va='center')
  if keyed:ax.text(1.15,5,f'{value:.2f} cm³' if col==1 else f'{value:g}'+(' °C' if col==0 else ' cm³'),ha='center',fontsize=12)
fig.suptitle('Read the divisions first; liquid levels are read at the lower meniscus',fontsize=14);fig.tight_layout();save_panels(fig,D,'VIS-6117-12-01',{'learner':[0,1,2],'answer':[3,4,5]});save(fig,'VIS-6117-12-01')
x=np.array([0,2,4,6,8,10],float);a=np.array([80,72,65,59,54,50],float);b=np.array([80,76,72,69,66,63],float)
def smooth(x,y):
 d=np.diff(y)/np.diff(x);m=np.r_[d[0],(d[:-1]+d[1:])/2,d[-1]];xx=[];yy=[]
 for i in range(len(x)-1):
  u=np.linspace(0,1,60);h=x[i+1]-x[i];v=(2*u**3-3*u**2+1)*y[i]+(u**3-2*u**2+u)*h*m[i]+(-2*u**3+3*u**2)*y[i+1]+(u**3-u**2)*h*m[i+1];xx.extend(x[i]+h*u);yy.extend(v)
 return np.array(xx),np.array(yy)
xx,ya=smooth(x,a);_,yb=smooth(x,b);assert np.all(np.diff(ya)<=1e-8) and np.all(np.diff(yb)<=1e-8) and np.all(yb>=ya) and min(ya)>22
fig,axs=plt.subplots(1,2,figsize=(13,6))
for ax in axs:
 ax.set_xlim(0,10);ax.set_ylim(20,90);ax.set_xticks(np.arange(0,11,2));ax.set_yticks(np.arange(20,91,10));ax.set_xticks(np.arange(0,10.1,.5),minor=True);ax.set_yticks(np.arange(20,91,2),minor=True);ax.grid(which='major',alpha=.5);ax.grid(which='minor',alpha=.15);ax.set_xlabel('time / min');ax.set_ylabel('temperature / °C')
axs[0].set_title('Learner grid — plot the supplied data')
axs[1].plot(xx,ya,label='Uninsulated',c='#426b8c');axs[1].plot(x,a,'o',c='#426b8c');axs[1].plot(xx,yb,label='Insulated',c='#b46b38');axs[1].plot(x,b,'s',c='#b46b38');axs[1].axhline(22,c='#777',ls=':',label='Room 22 °C');axs[1].legend();axs[1].set_title('Cooling curves — answer')
fig.tight_layout();save_panels(fig,D,'VIS-6117-12-02',{'learner':[0],'answer':[1]});save(fig,'VIS-6117-12-02')
fig,axs=plt.subplots(1,2,figsize=(12,7))
for ax,insulated in zip(axs,[False,True]):
 ax.axis('off');ax.set_xlim(0,8);ax.set_ylim(0,9);ax.set_title('Identical vessel: '+('jacket material B' if insulated else 'jacket material A'))
 ax.add_patch(Rectangle((1.5,1.5),3.3,4,fc='#eadbc9' if insulated else '#dfebdb',ec='#777'));ax.add_patch(Rectangle((1.8,1.7),2.7,3.8,fc='white',ec='#444',lw=1.4));ax.add_patch(Rectangle((1.85,1.75),2.6,2.4,fc='#dbeff4'))
 # Lid split by a real thermometer opening.
 ax.plot([1.7,2.9],[5.55,5.55],c='#555',lw=4);ax.plot([3.15,4.6],[5.55,5.55],c='#555',lw=4)
 ax.add_patch(Rectangle((2.95,2.9),.15,4.5,fc='white',ec='#444'));ax.add_patch(Circle((3.025,2.9),.14,fc='#b34f48',ec='#444'));ax.plot([3.025,3.025],[3,6.5],c='#b34f48',lw=2)
 ax.add_patch(Rectangle((1.2,1.3),3.9,.15,fc='#777'));ax.text(3.1,.8,'Heatproof mat',ha='center',fontsize=9)
 ax.annotate('100 cm³ water',xy=(3.9,3.7),xytext=(4.9,4.3),arrowprops={'arrowstyle':'->'},fontsize=9)
 ax.annotate('Bulb immersed;\nno glass contact',xy=(3.025,2.9),xytext=(5,2.5),arrowprops={'arrowstyle':'->'},fontsize=9)
 ax.text(.2,7.8,'Lid with thermometer opening\nEqual jacket thickness and covered area',fontsize=10)
 ax.add_patch(Circle((6.5,6.4),.4,fill=False));ax.plot([6.5,6.5,6.7],[6.7,6.4,6.3],c='#444');ax.text(6.5,5.5,'Stopwatch',ha='center',fontsize=9)
fig.suptitle('Cooling investigation — same 80 °C start, water amount and 22 °C surroundings',fontsize=13);fig.tight_layout();save(fig,'VIS-6117-12-03-cooling')
# Topic 12 uses only cooling apparatus. No Topic 11 soap-test panels belong here.
import shutil
for ext in ['svg','png']:
 shutil.copyfile(D/('VIS-6117-12-03-cooling.'+ext),D/('VIS-6117-12-03-answer.'+ext))
 shutil.copyfile(D/('VIS-6117-12-03-cooling.'+ext),D/('VIS-6117-12-03.'+ext))
(D/'parameters.json').write_text(json.dumps({'x_min':x.tolist(),'uninsulated_C':a.tolist(),'insulated_C':b.tolist(),'signed_rate_C_min':(59-72)/(6-2),'curve_checks':'Both monotone, insulated >= uninsulated, all above room temperature on plotted domain','scales':{'thermometer_C':63,'burette_cm3':6.4,'cylinder_cm3':36},'mass_loss_g':round(104.36-103.92,2),'titre_cm3':round(24.8-1.2,2)},indent=2)+'\n')

# Bare vessel outlines; controls and thermometer placement remain for learners to plan.
fig,axs=plt.subplots(1,2,figsize=(8,4))
for ax,label in zip(axs,['Vessel A','Vessel B']):
 ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal');ax.set_title(label)
 ax.plot([.22,.22,.78,.78],[.82,.2,.2,.82],color='#444',lw=2)
 ax.plot([.19,.22],[.84,.82],color='#444',lw=2);ax.plot([.78,.81],[.82,.84],color='#444',lw=2)
fig.tight_layout();save(fig,'VIS-6117-12-03-learner')
