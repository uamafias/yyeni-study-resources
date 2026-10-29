from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
D=Path(__file__).resolve().parents[1]/'topics/8/visuals';D.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
def save(fig,name):
 fig.savefig(D/(name+'.svg'),bbox_inches='tight');fig.savefig(D/(name+'.png'),dpi=140,bbox_inches='tight');plt.close(fig)
rows=[['NaOH dropwise','Light-blue precipitate forms.'],['NaOH excess','Precipitate remains insoluble.'],['Fresh portion: dilute HNO₃, then AgNO₃','White precipitate forms.']]
for answer in [False,True]:
 fig,ax=plt.subplots(figsize=(11,4));ax.axis('off');tab=ax.table(cellText=rows,colLabels=['Procedure','Observation for unknown X'],cellLoc='left',loc='center',colWidths=[.52,.48]);tab.auto_set_font_size(False);tab.set_fontsize(11);tab.scale(1,2.3)
 for (i,j),c in tab.get_celld().items():
  if i==0:c.set_facecolor('#dcebf3');c.set_text_props(weight='bold')
 ax.set_title('Test record — unknown X',pad=20)
 fig.text(.5,.08,'Cu²⁺ and Cl⁻ supported; purity is not established.' if answer else 'Precipitate means a solid formed in solution. It is not the colour of the whole solution.',ha='center')
 save(fig,'VIS-6117-8-01'+('-answer' if answer else ''))
fig,axs=plt.subplots(1,3,figsize=(12,5))
for ax,col,precip,title,caption in zip(axs,['#9bd5ef','#d9edf7','#194f9e'],[False,True,False],['Cu²⁺ solution','NH₃ dropwise','NH₃ excess'],['Initial blue solution','Light-blue precipitate','Deep-blue solution; no solid remains']):
 ax.axis('off');ax.set_xlim(0,4);ax.set_ylim(0,6);ax.plot([1,1,3,3],[5,1,1,5],c='#444',lw=2);ax.add_patch(Rectangle((1.02,1.02),1.96,2.8,fc=col,ec='none'))
 if precip:
  for x,y in [(1.3,1.4),(1.8,1.5),(2.3,1.3),(2.6,1.7),(1.5,2.2),(2.4,2.5),(2,1.9)]:ax.add_patch(Circle((x,y),.16,fc='#55a9d7',ec='#3280ac'))
 ax.set_title(title);ax.text(2,.3,caption,ha='center',fontsize=9)
fig.suptitle('Distinguish solid precipitate from coloured solution',fontsize=15);save(fig,'VIS-6117-8-02')
for answer in [False,True]:
 fig,axs=plt.subplots(2,2,figsize=(12,9))
 for ax in axs.flat:ax.axis('off');ax.set_xlim(0,10);ax.set_ylim(0,7)
 ax=axs[0,0];ax.plot([3,3,6,6],[5,1.5,1.5,5],c='#444',lw=2);ax.plot([4.5,4.5],[3.8,6.5],c='#8c6537',lw=5);ax.add_patch(Circle((4.5,3.8),.11,fc='#e66a32'));ax.text(6.2,5.5,'Glowing splint\n(no initial flame)');ax.set_title('Small gas sample — splint test');ax.text(4.5,.7,'Oxygen: glowing splint relights' if answer else 'Observe the change at the glowing tip.',ha='center',fontsize=9)
 ax=axs[0,1];ax.plot([3,3,6,6],[5,1.5,1.5,5],c='#444',lw=2);ax.add_patch(Rectangle((3.8,5.2),1.5,.3,fc='#c64747'));ax.text(6.1,5.3,'Damp red litmus\nclear of liquid');ax.set_title('Small gas sample — indicator test');ax.text(4.5,.7,'Ammonia: red paper turns blue' if answer else 'Observe the paper; do not smell the gas.',ha='center',fontsize=9)
 ax=axs[1,0];ax.plot([3,3,6,6],[5,1.5,1.5,5],c='#444',lw=2);ax.add_patch(Rectangle((3.02,1.52),2.96,1.7,fc='#e6f2f7'));ax.plot([.7,4,4],[6,6,2],c='#444',lw=2);ax.text(.2,6.3,'Gas delivery tube');ax.text(6.2,2.5,'Limewater')
 for x,y in [(4,2.2),(4.1,2.6),(4,3)]:ax.add_patch(Circle((x,y),.07,fc='white',ec='#55778a'))
 ax.set_title('Gas bubbled through test liquid');ax.text(4.5,.7,'Carbon dioxide: limewater turns milky' if answer else 'Observe the initially clear test liquid.',ha='center',fontsize=9)
 ax=axs[1,1];ax.add_patch(Rectangle((3.2,1.4),1.2,.35,fc='#666'));ax.add_patch(Rectangle((3.65,1.75),.3,1.7,fc='#777'));ax.add_patch(Polygon([(3.6,3.4),(3.4,4.0),(3.8,5.2),(4.2,4),(4,3.4)],fc='#9873c0' if answer else '#8cc3e4',ec='#527da3'));ax.plot([4,8],[4.2,5.3],c='#555',lw=2);ax.text(6.1,5.6,'Clean wire with\nsmall salt sample');ax.set_title('Supervised non-luminous flame test');ax.text(4.5,.7,'Potassium: lilac flame' if answer else 'Observe the flame colour after a blank check.',ha='center',fontsize=9)
 fig.suptitle('Test setups — captions state expected results; teacher supervision required',fontsize=14);fig.tight_layout(rect=[0,.03,1,.95]);save(fig,'VIS-6117-8-03'+('-learner' if not answer else ''))
(D/'parameters.json').write_text(json.dumps({'source_check':'Syllabus Annexe B, PDF viewer p.49, printed p.46','unknown':'X; identities omitted from learner matrix','observations':rows,'answer':{'cation':'Cu²⁺','anion':'Cl⁻'},'copper_ammonia':['blue solution','light-blue precipitate','deep-blue solution without solid'],'panels':'Separate learner and answer panels; not instructions for unsupervised gas generation.'},indent=2)+'\n')
