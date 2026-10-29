"""Generate Topic 1 figures from declared numerical geometry; no hand-edited SVGs."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Arc,Polygon
W=Path(__file__).resolve().parents[1];D=W/'topics/1/visuals';D.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
def save(fig,name):
 fig.savefig(D/(name+'.svg'),bbox_inches='tight');fig.savefig(D/(name+'.png'),dpi=140,bbox_inches='tight');plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(7,6))
for ax,kind,reading in zip(axs,['Measuring cylinder / cm³','Thermometer / °C'],[36,24]):
 ax.set_xlim(-2,3);ax.set_ylim(-3,55);ax.axis('off');ax.set_title(kind)
 ax.add_patch(Rectangle((-.5,0),1,50,fill=False,lw=1.5))
 ax.add_patch(Rectangle((-.45,0),.9,reading,color='#8cc9e9' if reading==36 else '#c64e55',alpha=.65))
 if reading==36:ax.add_patch(Arc((0,reading+1),.9,2,theta1=180,theta2=360,color='#17688c',lw=1.5))
 for v in range(51):
  ax.plot([.5,.85 if v%5==0 else .68],[v,v],color='black',lw=.8)
  if v%10==0:ax.text(.95,v,str(v),va='center')
 if reading==36:ax.plot([-.9,.9],[-.6,-.6],c='black',lw=2)
save(fig,'VIS-6117-1-01')
fig,axs=plt.subplots(1,2,figsize=(12,5))
for ax in axs:ax.set_xlim(0,10);ax.set_ylim(0,10);ax.axis('off')
a=axs[0];a.set_title('Filtration — answer/reference diagram')
a.plot([2,8,5,2],[8,8,5,8],c='black');a.plot([5,5],[5,3.5],c='black',lw=2)
a.add_patch(Polygon([(2.7,7.7),(7.3,7.7),(5,5.5)],facecolor='#e9e6da',edgecolor='grey'))
a.scatter([4.1,4.6,5,5.4,5.9],[7.3,7.1,7.2,7.1,7.3],c='#a88962',s=25)
a.plot([3,3,7,7],[4,1.5,1.5,4],c='black');a.add_patch(Rectangle((3.1,1.6),3.8,1,facecolor='#c8e3f1'))
for label,xy,tx in [('filter paper',(3.4,7.4),(.2,9)),('sand residue',(5,7.2),(6.2,9)),('salt solution filtrate',(5,2),(1,0.5))]:a.annotate(label,xy=xy,xytext=tx,arrowprops={'arrowstyle':'->'})
a=axs[1];a.set_title('Simple distillation — answer/reference diagram')
a.add_patch(Polygon([(1,2),(3,2),(2.6,4.5),(2.6,6),(1.8,6),(1.8,4.5)],fill=False,edgecolor='black'))
a.add_patch(Polygon([(1.15,2.2),(2.85,2.2),(2.6,3.5),(1.5,3.5)],facecolor='#c8e3f1'))
a.plot([2.6,4,8],[5.6,5.6,3.4],c='black',lw=2);a.plot([4,8],[6,3.8],c='#3984a7',lw=2);a.plot([4,8],[5.1,2.9],c='#3984a7',lw=2)
a.plot([4,4],[5.1,6],c='#3984a7');a.plot([8,8],[2.9,3.8],c='#3984a7');a.plot([4.3,4.3],[5.84,6.65],c='#3984a7',lw=2);a.plot([7.6,7.6],[3.12,2.35],c='#3984a7',lw=2)
a.plot([2.15,2.15],[8,5.6],c='firebrick',lw=2);a.plot(2.15,5.6,'o',color='firebrick',ms=4);a.plot([8,8.8,8.8],[3.4,3,2.7],c='black')
a.plot([8.1,8.1,9.6,9.6],[2.9,1,1,2.9],c='black')
a.annotate('heat',xy=(2,2),xytext=(1.5,.5),arrowprops={'arrowstyle':'->'})
for label,xy,tx in [('thermometer bulb at sidearm',(2.15,5.6),(.1,9)),('water out (upper port)',(4.3,6.65),(4,8.5)),('water in (lower port)',(7.6,2.35),(5.5,.4)),('open receiver',(9.1,2.7),(7.3,6.4))]:a.annotate(label,xy=xy,xytext=tx,arrowprops={'arrowstyle':'->'})
save(fig,'VIS-6117-1-02')
x=[0,10,20,30,40,50];y=[0,10.2,20.4,30.6,40.8,51]
for blank in [False,True]:
 fig,ax=plt.subplots(figsize=(7,5));ax.set_xlim(0,50);ax.set_ylim(0,55);ax.set_xticks(range(0,51,10));ax.set_yticks(range(0,56,5));ax.minorticks_on();ax.grid(which='both',alpha=.3)
 ax.set_xlabel('Reference volume / cm³');ax.set_ylabel('Cylinder reading / cm³')
 if not blank:ax.plot(x,y,'x-',color='#156082');ax.set_title('Calibration graph — answer')
 else:ax.set_title('Calibration graph — plot the supplied data')
 save(fig,'VIS-6117-1-03'+('-blank' if blank else ''))
(D/'parameters.json').write_text(json.dumps({'cylinder_reading_cm3':36,'thermometer_C':24,'scale_min':0,'scale_max':50,'scale_division':1,'graph':{'x':x,'y':y,'expected_gradient':1.02}},indent=2)+'\n')
print('Generated three required figures plus blank graph and PNG review copies.')
