"""Original electrolysis schematics; dimensions are illustrative, not construction specifications."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
D=Path(__file__).resolve().parents[1]/'topics/5/visuals';D.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
def save(fig,name):
 fig.savefig(D/(name+'.svg'),bbox_inches='tight');fig.savefig(D/(name+'.png'),dpi=140,bbox_inches='tight');plt.close(fig)
fig,ax=plt.subplots(figsize=(12,8));ax.set_xlim(0,12);ax.set_ylim(0,9);ax.axis('off')
ax.set_title('Aqueous CuSO₄ with carbon electrodes — collection at the positive anode')
# Open beaker and liquid; collection tube has a closed top and OPEN submerged mouth.
ax.plot([2,2,9,9],[6,1.3,1.3,6],c='#333',lw=2)
ax.add_patch(Rectangle((2.03,1.33),6.94,3.6,fc='#d4e9fa',ec='none'))
ax.plot([2.03,8.97],[4.93,4.93],c='#5090b0')
ax.plot([3,3,4.4,4.4],[2.5,6.4,6.4,2.5],c='#446079',lw=2)
ax.add_patch(Rectangle((3.03,2.5),1.34,3.86,fc='#bdddea',ec='none',alpha=.8))
# Carbon anode stands within tube; insulated lead travels through open mouth, then over rim.
ax.add_patch(Rectangle((3.5,2.6),.35,1.15,fc='#343434'))
ax.plot([3.67,3.67,2.55,2.55,2.55,4.7],[2.6,2.1,2.1,5.4,7.6,7.6],c='#b53a35',lw=2.4)
# Cathode enters from above liquid, immersed but not touching anode.
ax.add_patch(Rectangle((7.3,2.6),.35,3.0,fc='#343434'))
ax.plot([7.47,7.47,7.1],[5.6,7.6,7.6],c='#234a88',lw=2.4)
ax.add_patch(Rectangle((4.7,7.1),2.4,1,fc='#f4f4f4',ec='#333'))
ax.text(5.9,7.65,'Low-voltage DC',ha='center');ax.text(4.9,7.27,'+',color='#b53a35',fontsize=15);ax.text(6.75,7.27,'−',color='#234a88',fontsize=15)
for y in [3.95,4.25,4.65]:ax.add_patch(Circle((3.65,y),.065,fc='white',ec='#447080'))
for label,xy,txt in [('Positive carbon anode',(3.65,3.3),(.1,1.0)),('Negative carbon cathode',(7.5,3.6),(8.1,.6)),('Inverted water-filled tube\n(open mouth submerged)',(4.4,5.8),(5.0,6.0)),('Insulated lead enters\nthrough the open mouth',(3.05,2.1),(.05,.1)),('Aqueous CuSO₄',(8.2,4),(9.2,4.4)),('Beaker open to air',(8.9,5.8),(9.2,6.1))]:
 ax.annotate(label,xy=xy,xytext=txt,arrowprops={'arrowstyle':'->','color':'#555'},fontsize=9)
ax.text(5.8,-.45,'Schematic only. Teacher-supervised small gas collection; disconnect before testing. No sealed cell.',ha='center',fontsize=9)
save(fig,'VIS-6117-5-01')
fig,axs=plt.subplots(1,2,figsize=(12,7))
for ax,material,anode,colour in zip(axs,['Carbon anode','Copper anode'],['2H₂O → O₂ + 4H⁺ + 4e⁻','Cu → Cu²⁺ + 2e⁻'],['#333333','#b66c46']):
 ax.axis('off');ax.set_xlim(0,10);ax.set_ylim(0,10);ax.set_title(material)
 ax.add_patch(Rectangle((.4,5.7),9.2,2.1,fc='#e6f1f9',ec='#555'))
 ax.add_patch(Rectangle((1,6.0),.5,2.8,fc=colour));ax.add_patch(Rectangle((8.4,6.0),.5,2.8,fc='#b66c46'))
 ax.text(1.25,9,'+ anode',ha='center');ax.text(8.65,9,'− cathode',ha='center')
 ax.text(5,6.8,'Aqueous CuSO₄',ha='center');ax.text(5,5.0,'Anode: '+anode,ha='center')
 ax.text(5,4.1,'Cathode: Cu²⁺ + 2e⁻ → Cu',ha='center')
 note='Oxygen forms; the solution becomes more acidic.\nCu²⁺ removed at the cathode is not\nreplenished; the blue colour fades.' if material.startswith('Carbon') else 'Copper anode loses mass.\nCu²⁺ is replenished; its concentration\nremains approximately constant.'
 ax.text(5,2.5,note,ha='center',va='center',linespacing=1.6)
fig.suptitle('Electrode material changes the anode reaction',fontsize=15)
fig.text(.5,.045,'Compare equal current and time, matched initial solution concentration and volume, and equal immersed electrode area.',ha='center',fontsize=9)
save(fig,'VIS-6117-5-02')
(D/'parameters.json').write_text(json.dumps({'state':'aqueous','electrolyte':'copper(II) sulfate','supply':'low-voltage DC','anode_polarity':'+','cathode_polarity':'-','anodes_compared':['carbon','copper'],'collection':'inverted initially water-filled tube with submerged open mouth above carbon anode; insulated lead enters through mouth','scale':'schematic, not to scale','scientific_review':'author self-check pending; independent review required'},indent=2)+'\n')
