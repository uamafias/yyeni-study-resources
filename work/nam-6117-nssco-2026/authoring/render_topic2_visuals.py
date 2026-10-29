"""Generate Matter figures from explicit particle, bond and geometry data."""
import json,math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon,Rectangle
from topic2 import MOLECULES
W=Path(__file__).resolve().parents[1];D=W/'topics/2/visuals';D.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
def save(fig,name):
 fig.savefig(D/(name+'.svg'),bbox_inches='tight');fig.savefig(D/(name+'.png'),dpi=120,bbox_inches='tight');plt.close(fig)
def setup(ax):ax.set_aspect('equal');ax.axis('off')
fig,axs=plt.subplots(2,3,figsize=(12,8))
points=[[(x,y) for x in [0,.4,.8,1.2] for y in [0,.4,.8]],[(0,0),(.4,.05),(.8,0),(1.2,.1),(.15,.4),(.6,.45),(1.05,.42),(1.45,.4),(.05,.8),(.5,.85),(.95,.8),(1.4,.85)],[(0,0),(1.4,.2),(.4,1.3),(1.7,1.7),(.9,.7)]]
for ax,label,pts in zip(axs[0],['Solid: close and ordered','Liquid: close and disordered','Gas: widely separated'],points):
 setup(ax);ax.set_xlim(-.3,2);ax.set_ylim(-.3,2);ax.set_title(label)
 for x,y in pts:ax.add_patch(Circle((x,y),.12,color='#267c9f'))
 for n,(x,y) in enumerate(pts):
  if label.startswith('Gas'):
   a=[.7,2.4,-1.1,3.5,-.2][n];ax.annotate('',xy=(x+.32*math.cos(a),y+.32*math.sin(a)),xytext=(x,y),arrowprops={'arrowstyle':'->','color':'#333'})
  elif label.startswith('Solid') and n==0:ax.annotate('',xy=(x+.16,y),xytext=(x-.16,y),arrowprops={'arrowstyle':'<->'})
  elif label.startswith('Liquid') and n in [3,8]:ax.annotate('',xy=(x+.25,y+.17),xytext=(x,y),arrowprops={'arrowstyle':'->'})
for ax,label,shells in [(axs[1,0],'Sodium-23 atom',[2,8,1]),(axs[1,1],'Sodium-23 ion Na⁺',[2,8])]:
 setup(ax);ax.set_xlim(-1.8,1.8);ax.set_ylim(-1.8,1.8);ax.set_title(label);ax.add_patch(Circle((0,0),.38,fc='#f1dab0'));ax.text(0,0,'11 p\n12 n',ha='center',va='center',fontsize=8)
 for level,count in enumerate(shells,1):
  r=.45+level*.33;ax.add_patch(Circle((0,0),r,fill=False,color='#999'))
  for k in range(count):a=2*math.pi*k/count;ax.plot(r*math.cos(a),r*math.sin(a),'o',color='#236d9a',ms=4)
 ax.text(0,-1.7,'Electrons: '+','.join(map(str,shells)),ha='center')
axs[1,2].axis('off');axs[1,2].text(0,.85,'Key and interpretation\n\np = proton; n = neutron\nBlue dot = electron\nCentral region = nucleus\n\nIon formation removes one electron.\nThe nucleus remains unchanged.\n\nParticle sizes are kept equal in\nthe three state diagrams.\nArrows indicate particle motion.',va='top')
save(fig,'VIS-6117-2-01')

def draw_molecule(ax,name,spec):
 setup(ax);ax.set_xlim(-2.7,2.7);ax.set_ylim(-2.1,2.1);ax.set_title(name)
 pos=np.array(spec['positions'],float);adj={i:[] for i in range(len(pos))}
 for i,j,n in spec['bonds']:adj[i].append(j);adj[j].append(i)
 parity={0:0};queue=[0]
 while queue:
  i=queue.pop(0)
  for j in adj[i]:
   if j not in parity:parity[j]=1-parity[i];queue.append(j)
 counts=[2*n for n in spec['lone_pairs']]
 for i,j,n in spec['bonds']:
  counts[i]+=n;counts[j]+=n
  v=pos[j]-pos[i];v=v/np.linalg.norm(v);perp=np.array([-v[1],v[0]]);mid=(pos[i]+pos[j])/2
  for k in range(n):
   centre=mid+perp*(k-(n-1)/2)*.22
   for atom,sign in [(i,-1),(j,1)]:
    q=centre+v*sign*.065;ax.plot(*q,marker='o' if parity[atom]==0 else 'x',color='#155d91' if parity[atom]==0 else '#ad3d37',ms=4,mew=1.3)
 valence={'H':1,'C':4,'N':5,'O':6,'Cl':7}
 assert counts==[valence[a] for a in spec['atoms']],(name,counts)
 for i,(a,p,n) in enumerate(zip(spec['atoms'],pos,spec['lone_pairs'])):
  ax.text(*p,a,ha='center',va='center',fontsize=15)
  bondangles=[math.atan2(*(pos[j]-p)[::-1]) for j in adj[i]]
  candidates=[k*math.pi/4 for k in range(8)]
  chosen=[]
  for k in range(n):
   def clearance(t):return min(abs(math.atan2(math.sin(t-b),math.cos(t-b))) for b in bondangles+chosen)
   angle=max(candidates,key=clearance);chosen.append(angle);candidates.remove(angle)
   direction=np.array([math.cos(angle),math.sin(angle)]);perp=np.array([-direction[1],direction[0]])
   for sign in [-1,1]:q=p+.36*direction+sign*.065*perp;ax.plot(*q,marker='o' if parity[i]==0 else 'x',color='#155d91' if parity[i]==0 else '#ad3d37',ms=4,mew=1.3)
 ax.text(0,-1.9,'Dots/crosses show atom of origin; all electrons have the same charge.',ha='center',fontsize=6)
fig,axs=plt.subplots(5,2,figsize=(11,18))
for ax,(name,spec) in zip(axs.flat,MOLECULES.items()):
 draw_molecule(ax,name,spec)
 one,a=plt.subplots(figsize=(5.5,4));draw_molecule(a,name,spec);save(one,'molecule-'+name)
fig.suptitle('Outer-electron answer diagrams: shared pairs lie between atoms; lone pairs lie outside bonds',y=.93,fontsize=12)
save(fig,'VIS-6117-2-02')

def bond(ax,start,end,kind='line',double=False):
 s=np.array(start,float);e=np.array(end,float);v=e-s;perp=np.array([-v[1],v[0]])/np.linalg.norm(v)
 if kind=='wedge':ax.add_patch(Polygon([s,e+.12*perp,e-.12*perp],color='#333'))
 elif kind=='dash':
  for t in np.linspace(.15,.9,7):p=s+t*v;ax.plot(*np.array([p-.12*t*perp,p+.12*t*perp]).T,c='#333')
 else:
  for offset in ([-.04,.04] if double else [0]):ax.plot(*np.array([s+offset*perp,e+offset*perp]).T,c='#333')
def atom(ax,p,label):ax.text(*p,label,ha='center',va='center',fontsize=15,bbox={'facecolor':'white','edgecolor':'none','pad':1})
fig,axs=plt.subplots(2,2,figsize=(10,8))
for ax in axs.flat:setup(ax);ax.set_xlim(-2,2);ax.set_ylim(-1.7,1.7)
ax=axs[0,0];ax.set_title('Water: bent / V-shaped')
for p in [(-1,-.8),(1,-.8)]:bond(ax,(0,0),p);atom(ax,p,'H')
atom(ax,(0,0),'O');ax.text(-.3,.45,'••',ha='center');ax.text(.3,.45,'••',ha='center')
ax=axs[0,1];ax.set_title('Methane: tetrahedral')
for p,k in [((0,1.2),'line'),((-1,-.6),'line'),((1,-.6),'wedge'),((.6,.4),'dash')]:bond(ax,(0,0),p,k);atom(ax,p,'H')
atom(ax,(0,0),'C')
ax=axs[1,0];ax.set_title('Ammonia: pyramidal')
for p,k in [((-1,-.65),'line'),((.15,-1.2),'wedge'),((1,-.65),'dash')]:bond(ax,(0,.2),p,k);atom(ax,p,'H')
atom(ax,(0,.2),'N');ax.text(0,.7,'••',ha='center')
ax=axs[1,1];ax.set_title('Carbon dioxide: linear')
for p in [(-1.3,0),(1.3,0)]:bond(ax,(0,0),p,double=True);atom(ax,p,'O')
atom(ax,(0,0),'C');fig.text(.5,.025,'Solid wedge: towards viewer. Dashed wedge: away. Lines: in the page. Paired dots: lone pair.',ha='center')
save(fig,'VIS-6117-2-03')

fig=plt.figure(figsize=(15,5));ax=fig.add_subplot(131);setup(ax)
ax.set_title('Diamond: tetrahedral bonding at one carbon')
ax.set_xlim(-1.8,1.8);ax.set_ylim(-1.8,1.8)
# Wedge/dash projection: four bonds, with two in the page, one towards and one away.
for p,k in [((0,1.15),'line'),((-1,-.65),'line'),((1,-.65),'wedge'),((.85,.55),'dash')]:
 bond(ax,(0,0),p,k);atom(ax,p,'C')
atom(ax,(0,0),'C')
ax.text(0,-1.22,'Solid wedge: towards you; dashed: away.',ha='center',fontsize=8)
ax.text(0,-1.48,'Each outer carbon bonds onward in the network.',ha='center',fontsize=8)
ax=fig.add_subplot(132,projection='3d');ax.set_title('Graphite: separate covalent sheets')
hexpoints={}
for cx,cy in [(0,0),(1.5,math.sqrt(3)/2),(0,math.sqrt(3)),(-1.5,math.sqrt(3)/2)]:
 for k in range(6):p=(round(cx+math.cos(k*math.pi/3),5),round(cy+math.sin(k*math.pi/3),5));hexpoints[p]=1
pp=np.array(list(hexpoints))
for z in [0,1.2]:
 for i,p in enumerate(pp):
  for q in pp[i+1:]:
   if abs(np.linalg.norm(p-q)-1)<1e-4:ax.plot([p[0],q[0]],[p[1],q[1]],[z,z],c='#444')
 ax.scatter(pp[:,0],pp[:,1],z,s=13,c='#444')
ax.set_axis_off();ax.view_init(20,35)
ax=fig.add_subplot(133);setup(ax);ax.set_title('Metal lattice');ax.set_xlim(-.7,4.0);ax.set_ylim(-.7,3)
for x in range(4):
 for y in range(3):ax.add_patch(Circle((x,y),.25,fc='#e7d9b6'));ax.text(x,y,'+',ha='center',va='center')
for ex,ey in [(.4,.45),(1.4,.65),(2.55,.35),(3.4,.7),(-.35,1.35),(.65,1.6),(1.55,1.3),(2.6,1.55),(.35,2.45),(1.6,2.4),(2.55,2.5),(3.4,1.8)]:
 ax.text(ex,ey,'e⁻',fontsize=9,color='#155d91')
ax.text(1.5,-.5,'Positive ions +; electrons move throughout the lattice',ha='center',fontsize=8)
fig.text(.5,.02,'Network fragments: bonding continues beyond cut edges. No covalent bonds join the graphite layers.',ha='center')
save(fig,'VIS-6117-2-04')

fig,ax=plt.subplots(figsize=(9,6));ax.axis('off');ax.set_xlim(0,10);ax.set_ylim(0,7);ax.set_title('Low-voltage conductivity circuit — answer/reference')
ax.add_patch(Rectangle((.6,4.4),2.2,1.2,fill=False));ax.text(1.7,5,'3 V current-limited\nDC supply',ha='center',va='center')
ax.plot([2.8,4],[5,5],c='black');ax.plot([4,4.7],[5,5.35],c='black');ax.plot([4.8,6],[5,5],c='black');ax.text(4.4,5.7,'switch',ha='center')
ax.add_patch(Circle((6.5,5),.5,fill=False));ax.text(6.5,5,'A',ha='center',va='center');ax.text(6.5,5.8,'ammeter',ha='center')
ax.plot([7,8,8],[5,5,2.5],c='black');ax.plot([1.7,1.7,6,6],[4.4,4,4,3.7],c='black')
ax.plot([5.3,5.3,8.7,8.7],[3.7,1.5,1.5,3.7],c='black');ax.add_patch(Rectangle((5.35,1.55),3.3,1.6,fc='#d6edf3',zorder=-1))
ax.plot([6,6],[3.7,2.2],c='#444',lw=5);ax.plot([8,8],[3.7,2.2],c='#444',lw=5)
ax.annotate('two graphite electrodes',xy=(8,3.2),xytext=(6.8,4.15),arrowprops={'arrowstyle':'->'})
ax.annotate('sample solution',xy=(7,2),xytext=(3.1,2),arrowprops={'arrowstyle':'->'});ax.annotate('',xy=(6,2.7),xytext=(8,2.7),arrowprops={'arrowstyle':'<->'});ax.text(7,2.95,'fixed gap',ha='center',fontsize=9)
save(fig,'VIS-6117-2-circuit')
(D/'parameters.json').write_text(json.dumps({'molecules':MOLECULES,'sodium':{'protons':11,'neutrons':12,'atom_shells':[2,8,1],'ion_shells':[2,8]},'circuit_supply_V':3,'scope':'Answer/reference images; no keyed image is placed in an assessed drawing prompt.','electron_count_check':'Every atom contributes its specified valence count; all ten molecular datasets asserted.'},indent=2)+'\n')
print('Four planned visuals, ten molecular answer panels and one conductivity circuit generated; electron counts asserted.')
