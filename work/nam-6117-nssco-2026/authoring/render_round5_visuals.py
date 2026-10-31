from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
W=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'none','font.size':12})
def save(fig,t,n):
 for ext in ['svg','png']:fig.savefig(W/f'topics/{t}/visuals/{n}.{ext}',bbox_inches='tight',dpi=140)
 plt.close(fig)
fig,ax=plt.subplots(figsize=(6,6));ax.set_aspect('equal');ax.axis('off');ax.set_xlim(-2,2);ax.set_ylim(-2,2)
ax.add_patch(Circle((0,0),.3,fc='#efe1c4'));ax.text(0,0,'13 p\n14 n',ha='center',va='center')
for radius,n in [(.65,2),(1.15,8),(1.65,3)]:
 ax.add_patch(Circle((0,0),radius,fill=False,color='#888'))
 for i in range(n):a=2*math.pi*i/n;ax.plot(radius*math.cos(a),radius*math.sin(a),'o',color='#205b8a')
ax.set_title('Answer: aluminium-27 atom');save(fig,2,'R5-bohr-answer')
fig,ax=plt.subplots(figsize=(10,4));ax.set_aspect('equal');ax.axis('off');ax.set_xlim(-1,7);ax.set_ylim(-1.4,1.5)
ax.text(0,0,'[Mg]²⁺',ha='center',fontsize=19)
for x in [2.5,5.5]:
 ax.text(x,0,'F',ha='center',va='center',fontsize=20)
 for i in range(8):
  a=2*math.pi*i/8;ax.plot(x+.55*math.cos(a),.55*math.sin(a),marker='x' if i==0 else 'o',color='#a43d31' if i==0 else '#205b8a',markersize=7)
 ax.plot([x-.85,x-.95,x-.95,x-.85],[-.8,-.8,.8,.8],c='#333');ax.plot([x+.85,x+.95,x+.95,x+.85],[-.8,-.8,.8,.8],c='#333');ax.text(x+1,.85,'−',fontsize=18)
ax.text(2.9,-1.2,'Dots: fluorine electrons. Crosses: electrons transferred from magnesium.',ha='center',fontsize=10)
ax.set_title('Answer: MgF₂ — outer electrons only; separate ions');save(fig,2,'R5-ionic-answer')
fig,ax=plt.subplots(figsize=(7,4));ax.plot([0,1,2,3,4],[40,40,95,15,15],c='#315b7b');ax.set_ylim(0,110);ax.set_yticks([0,15,40,95]);ax.set_xticks([]);ax.set_ylabel('Energy / kJ mol⁻¹');ax.set_xlabel('Reaction progress');ax.text(.3,44,'Reactants');ax.text(3.05,19,'Products');ax.set_title('Reaction energy profile');fig.tight_layout();save(fig,6,'R5-profile-learner')
