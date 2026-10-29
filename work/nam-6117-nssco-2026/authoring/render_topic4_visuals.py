"""Generated mole routes and correctly directed burette scales."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
W=Path(__file__).resolve().parents[1];D=W/'topics/4/visuals';D.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
def save(fig,name):fig.savefig(D/(name+'.svg'),bbox_inches='tight');fig.savefig(D/(name+'.png'),dpi=140,bbox_inches='tight');plt.close(fig)
fig,ax=plt.subplots(figsize=(11,7));ax.axis('off');ax.set_xlim(0,10);ax.set_ylim(0,7)
boxes=[((5,3.5),'Amount n / mol'),((1.8,5.7),'Mass m / g\nMolar mass M / g mol⁻¹'),((8.2,5.7),'Solution volume V / dm³\nConcentration c / mol dm⁻³'),((5,.9),'Gas volume Vgas / dm³\nat room temperature and pressure')]
for (x,y),txt in boxes:ax.text(x,y,txt,ha='center',va='center',bbox={'boxstyle':'round,pad=.7','fc':'#e2eff5','ec':'#28647b'})
for start,end,label,tx in [((2.5,5.1),(4.3,4),'n = m/M',(2.6,4.1)),((7.4,5.1),(5.8,4),'n = cV',(6.6,4.1)),((5,1.7),(5,2.9),'n = Vgas/24',(5.2,2.3))]:ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','lw':1.7});ax.text(*tx,label)
ax.text(.2,.1,'cm³ → dm³: divide by 1000.  Mass concentration in g/dm³ gives mass when multiplied by volume; convert mass to amount separately.',fontsize=9)
ax.set_title('Mole conversion routes — use compatible units',pad=15)
save(fig,'VIS-6117-4-01')
for answer in [False,True]:
 fig,axs=plt.subplots(1,2,figsize=(7,6))
 for ax,offset,title in zip(axs,[0,25],['Initial burette reading','Final burette reading']):
  ax.set_xlim(-1.1,1.5);ax.set_ylim(offset+1.2,offset-.2);ax.axis('off');ax.set_title(title)
  ax.plot([-.5,-.5],[offset-.15,offset+1.15],c='black');ax.plot([.5,.5],[offset-.15,offset+1.15],c='black')
  xx=np.linspace(-.5,.5,100);meniscus=offset+.4-.4*xx**2;ax.fill_between(xx,meniscus,offset+1.15,color='#c1e2f0');ax.plot(xx,meniscus,c='#176185',lw=2)
  for k in range(11):
   y=offset+k/10;ax.plot([.5,.85 if k%2==0 else .7],[y,y],c='black')
   if k%2==0:ax.text(.95,y,f'{y:.1f}',va='center')
  ax.text(-1,offset+1.12,'cm³',fontsize=11)
  if answer:ax.annotate(f'{offset+.4:.2f} cm³',xy=(0,offset+.4),xytext=(-1,offset+.7),arrowprops={'arrowstyle':'->'})
 fig.text(.5,.02,'Magnified scale sections; divisions 0.1 cm³. Read the bottom of the meniscus at eye level.',ha='center',fontsize=9)
 save(fig,'VIS-6117-4-readings'+('-answer' if answer else ''))
fig,ax=plt.subplots(figsize=(10,7));ax.axis('off');ax.set_xlim(0,10);ax.set_ylim(0,10);ax.set_title('Titration apparatus — labelled reference')
ax.add_patch(Rectangle((.6,.5),4.2,.25,fc='#666'));ax.plot([1,1],[.75,9.3],c='#666',lw=5);ax.plot([1,3.2],[7.4,7.4],c='#666',lw=3);ax.add_patch(Rectangle((3.05,3.4),.35,5.5,fill=False));ax.text(3.7,8.9,'50 cm³ burette')
for reading in range(0,51,10):y=8.7-reading*.10;ax.plot([3.05,3.4],[y,y],c='black',lw=.8);ax.text(2.65,y,str(reading),fontsize=8,va='center')
ax.plot([2.9,3.6],[3.3,3.3],c='black',lw=2);ax.plot([3.22,3.22],[3.4,2.9],c='black');ax.annotate('tap',xy=(3.5,3.3),xytext=(4.2,3.6),arrowprops={'arrowstyle':'->'})
ax.add_patch(Polygon([(2.3,1.1),(4.2,1.1),(3.55,2.2),(3.55,2.6),(3.0,2.6),(3.0,2.2)],fill=False,ec='black'));ax.add_patch(Polygon([(2.45,1.2),(4.05,1.2),(3.8,1.65),(2.7,1.65)],fc='#d2e9f3'))
ax.add_patch(Rectangle((2.1,.83),2.3,.15,fc='white',ec='black'));ax.annotate('white tile',xy=(4.2,.9),xytext=(5.0,1.1),arrowprops={'arrowstyle':'->'});ax.annotate('conical flask',xy=(3.9,1.7),xytext=(5,2.2),arrowprops={'arrowstyle':'->'});ax.annotate('clamp and stand',xy=(1.8,7.4),xytext=(.2,9.6),arrowprops={'arrowstyle':'->'})
ax.plot([7.7,7.7],[4,7],c='black',lw=2);ax.plot([7.5,7.9],[6.4,6.4],c='black');ax.text(8.1,6.4,'calibration mark',fontsize=8,va='center');ax.add_patch(Circle((7.7,5.5),.3,fc='white',ec='black'));ax.add_patch(Circle((7.7,7.5),.4,fc='#d2dbe3',ec='black'));ax.plot([7.7,7.7],[7,7.1],c='black');ax.text(6.2,3.5,'25.0 cm³ pipette\nand filler',ha='left');ax.text(5.5,8.8,'Scale values increase downwards.\nUse eye protection and a pipette filler.\nRemove the filling funnel before readings.',fontsize=10)
save(fig,'VIS-6117-4-02')
(D/'parameters.json').write_text(json.dumps({'initial_cm3':.4,'final_cm3':25.4,'scale_division_cm3':.1,'titre_cm3':25.4-.4,'HCl_concentration_mol_dm3':.1,'amount_mol':.1*(25.4-.4)/1000,'aliquot_cm3':25,'gas_molar_volume_dm3_mol':24,'gas_conditions':'room temperature and pressure'},indent=2)+'\n')
print('Mole route, apparatus and separate learner/answer burette readings generated.')
