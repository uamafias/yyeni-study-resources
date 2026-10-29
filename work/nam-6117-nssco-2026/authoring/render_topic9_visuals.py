from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
D=Path(__file__).resolve().parents[1]/'topics/9/visuals';D.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
def save(fig,name):
 fig.savefig(D/(name+'.svg'),bbox_inches='tight');fig.savefig(D/(name+'.png'),dpi=140,bbox_inches='tight');plt.close(fig)
fig,ax=plt.subplots(figsize=(12,9));ax.axis('off');ax.set_xlim(0,13);ax.set_ylim(0,11)
ax.add_patch(Polygon([(2,1),(5,1),(5.5,3),(4.8,8.5),(4.8,9.5),(2.2,9.5),(2.2,8.5),(1.5,3)],fc='#f0e8de',ec='#555',lw=2))
ax.add_patch(Rectangle((2.1,1.05),2.8,.7,fc='#ac4e36'));ax.add_patch(Rectangle((2.1,1.75),2.8,.5,fc='#c7b678'))
ax.annotate('Iron ore + coke + limestone',xy=(3.5,9.2),xytext=(3.5,10.5),ha='center',arrowprops={'arrowstyle':'->'})
ax.annotate('Waste gases',xy=(4.85,8.6),xytext=(6,9.4),arrowprops={'arrowstyle':'<-'});ax.plot([4.8,5.5],[8.6,8.6],c='#555')
ax.annotate('Hot air',xy=(1.8,3),xytext=(.1,3),arrowprops={'arrowstyle':'->'});ax.annotate('Hot air',xy=(5.2,3),xytext=(6,3),arrowprops={'arrowstyle':'->'})
ax.plot([4.9,5.8],[1.95,1.95],c='#a08c48',lw=5);ax.text(6,1.95,'Slag outlet',va='center');ax.plot([4.9,5.8],[1.35,1.35],c='#a84b35',lw=5);ax.text(6,1.35,'Molten iron outlet',va='center')
ax.text(3.5,5.8,'Charge descends\n\nHot reducing gas rises',ha='center',linespacing=1.8)
ax.text(7.1,8.5,'C + O₂ → CO₂\n\nCO₂ + C → 2CO\n\nFe₂O₃ + 3CO → 2Fe + 3CO₂\n\nCaCO₃ → CaO + CO₂\n\nCaO + SiO₂ → CaSiO₃',va='top',fontsize=12)
ax.text(6.5,.3,'Schematic: less dense slag above molten iron. CO reduces the iron oxide.',ha='center');ax.set_title('Blast furnace — inputs, products and essential reactions',fontsize=15)
save(fig,'VIS-6117-9-01')
fig,axs=plt.subplots(1,2,figsize=(11,5))
for k,ax in enumerate(axs):
 ax.axis('off');ax.set_xlim(-.6,5.5);ax.set_ylim(-.7,4.5);ax.set_aspect('equal')
 for row in range(4):
  for col in range(5):
   special=k==1 and (row,col) in [(0,2),(1,1),(2,3),(3,2)];r=.42 if special else .29;offset=.15 if k==1 and row in [1,2] else 0
   ax.add_patch(Circle((col+offset,row),r,fc='#c28a46' if special else '#72a2be',ec='#35566b'))
 ax.set_title('Pure metal: equal-sized atoms' if k==0 else 'Model alloy: different-sized atoms')
 ax.text(2,-.6,'Regular layers can slide' if k==0 else 'Disturbed layers hinder sliding',ha='center',fontsize=10)
fig.suptitle('Introductory structure model — real alloy properties depend on composition',fontsize=12);save(fig,'VIS-6117-9-02')
fig,axs=plt.subplots(1,2,figsize=(13,7))
for ax,metal,vals in zip(axs,['Magnesium','Zinc'],[[0,12,22,30],[0,5,9,12]]):
 ax.axis('off');ax.set_xlim(0,10);ax.set_ylim(0,9);ax.set_title(metal)
 ax.add_patch(Polygon([(1,3),(4,3),(3.1,5),(3.1,5.7),(2,5.7),(2,5)],fill=False,ec='#444',lw=2));ax.add_patch(Polygon([(1.2,3.1),(3.8,3.1),(3.4,4),(1.6,4)],fc='#dcebf3'))
 ax.add_patch(Rectangle((2,5.55),1.1,.25,fc='#777'));ax.plot([2.55,2.55,5],[5.7,6.3,6.3],c='#444',lw=2)
 ax.add_patch(Rectangle((5,5.95),3,.7,fill=False));ax.plot([7.3,7.3],[5.98,6.62],c='#444',lw=3);ax.plot([7.3,9],[6.3,6.3],c='#444',lw=2);ax.plot([9,9],[6,6.6],c='#444')
 for i in range(7):ax.plot([5.2+i*.35,5.2+i*.35],[6.65,6.45],c='#444',lw=.7)
 ax.add_patch(Rectangle((2,3.4),.8,.12,angle=15,fc='#999',ec='#555'))
 ax.text(.4,2.1,'Reaction flask: measured dilute HCl\nMatched-area, consistently cleaned metal strip',fontsize=9)
 ax.text(4.9,7.2,'Gas syringe: freely moving plunger',fontsize=9);ax.text(.7,7.4,'Bung and delivery tube',fontsize=9);ax.annotate('',xy=(2.55,5.7),xytext=(2.55,7.1),arrowprops={'arrowstyle':'->'})
 ax.add_patch(Circle((8,4),.45,fill=False));ax.plot([8,8,8.2],[4.3,4,3.8],c='#444');ax.text(8,3.2,'Stopwatch',ha='center',fontsize=9)
 ax.text(5,.7,'Time / s: 0, 10, 20, 30\nGas / cm³: '+', '.join(map(str,vals)),ha='center',fontsize=11)
fig.suptitle('Comparison — equal acid concentration, volume and temperature',fontsize=13)
fig.text(.5,.04,'Hydrogen is flammable: no flames. Gas outlets remain unobstructed. Do not test sodium or potassium with acid.',ha='center',fontsize=10)
fig.tight_layout(rect=[0,.07,1,.95]);save(fig,'VIS-6117-9-03')
(D/'parameters.json').write_text(json.dumps({'time_s':[0,10,20,30],'Mg_cm3':[0,12,22,30],'Zn_cm3':[0,5,9,12],'Mg_rate_cm3_s':30/30,'Zn_rate_cm3_s':12/30,'furnace':'slag above iron; hot air lower, charge top, waste gas upper','particle_model':'Illustrative equal-radius pure lattice and minority larger-radius alloy atoms, not an exact crystal structure.'},indent=2)+'\n')
