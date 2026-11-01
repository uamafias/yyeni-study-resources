"""Physics figures constructed from the repaired task parameters."""
import copy,math

def seg(points,color='tab:blue',arrow=False,style='-'):return dict(points=points,color=color,arrow=arrow,style=style)
def combined(a,b,title,offset=12):
 return dict(kind='geometry',segments=[],panels=[copy.deepcopy(a),copy.deepcopy(b)],title=title)

def lens(u,f,title,receiver=None,eye=False):
 v=f*u/(u-f);h=-v/u;right=(v if receiver else max(3,v+.5)) if v>0 else 3;left=min(-u-1,v-1) if v<0 else -u-1
 S=[seg([[left,0],[right,0]],'grey'),seg([[0,-1.6],[0,1.6]],'black'),seg([[-u,0],[-u,1]],'tab:green',True),seg([[-u,1],[0,1]],arrow=True),seg([[0,1],[right,1-right/f]],arrow=True),seg([[-u,1],[right,-right/u]],arrow=True),seg([[v,0],[v,h]],'tab:red',True)]
 if v<0:S += [seg([[0,1],[v,h]],'tab:orange',style='--'),seg([[0,0],[v,h]],'tab:orange',style='--')]
 if receiver:S.append(seg([[v,-1.4],[v,1.4]],'tab:purple'))
 labels=[[0.1,1.8,'Eye lens (power changes)' if eye else 'Converging lens'],[-u-.3,1.2,'Object'],[-f,-.4,'F'],[f,-.4,'F'],[v+.15,h-.35,'Virtual image' if v<0 else ('Inverted image')],[v+.15,1.35,receiver or ''],[left,-2.0,f'u={u:.3g} cm; f={f:.3g} cm; v={v:.3g} cm; h′={h:.3g} cm']]
 if receiver:labels.append([-.5,-1.8,'Iris / pupil' if eye else 'Adjustable aperture'])
 return dict(kind='geometry',segments=S,circles=[],labels=labels,title=title)
def apply(A):
 t=int(A.t);D=A.data
 if t==3:
  for key in ['1.2.3-02','1.2.3-03','1.2.3-04','1.2.3-05']:
   p=A.figures['OBJ-6118-'+key];p.update(ys={},xlim=[0,10] if key.endswith('02') else [0,max(p['x'])],ylim=[0,40] if key.endswith('02') else [0,30] if key.endswith('03') else [0,10] if key.endswith('04') else [0,20]);p['title']='Axes only: '+p['title']
  p=A.figures['OBJ-6118-1.2.3-07'];p.update(ys={'Measured positions':[3,6.1,8.9,12]},fit=True,title='Scattered readings with a separate straight best fit')
  A.figures['OBJ-6118-1.2.3-08'].update(xlim=[0,4],ylim=[0,10])
 if t==4:
  for k in D:
   D[k]['teach']=D[k]['teach'].replace('8 N east and 6 N north','4 N east and 3 N north').replace('10 N at 36.9','5 N at 36.9')
 if t==5:
  x=[n/40 for n in range(121)];A.plot('2.3.3-04',x,{'Velocity':[v*v for v in x]},'Time / s','Velocity / (m/s)','Velocity = t²: a continuously increasing gradient',origin=True)
  for p in A.figures.values():p['origin']=True
  # Both graphs in the misconception are shown with their own different axes.
  A.figures['MISCON-24-graphs']=dict(kind='comparison',panels=[dict(x=[0,4],ys={'A: steady motion':[3,3]},xlabel='Time / s',ylabel='Speed / (m/s)',title='A: speed stays 3 m/s'),dict(x=[0,4],ys={'B: at rest':[12,12]},xlabel='Time / s',ylabel='Distance / m',title='B: distance stays 12 m')],title='Horizontal lines on different axes')
  # Added keyed figure belongs to the existing objective; a dedicated answer asset is handled below.
  A.miscon_figure_specs={'ITEM-6118-5-021-MISCON':A.figures.pop('MISCON-24-graphs')}
 if t==18:
  D['OBJ-6118-4.3.3-12-M02']['prompt']='Draw the image of a 1 cm tall object 1.5 cm before a converging lens with focal length 2 cm.'
  D['OBJ-6118-4.3.3-12-M02']['teach']='For object distance 1.5 cm and focal length 2 cm, the outgoing rays diverge. Their backward extensions meet 6 cm before the lens at an upright virtual image 4 cm tall. This construction keeps the image distinct from the near focus.'
  A.figures['OBJ-6118-4.3.3-12-M01']=lens(6,2,'Real image: object beyond 2F')
  A.figures['OBJ-6118-4.3.3-12-M02']=lens(1.5,2,'Virtual magnified image: object inside F')
  A.figures['OBJ-6118-4.3.3-12']=lens(4,1,'Real-image construction using two standard rays')
  camera=lens(8,2,'Camera: lens-to-sensor separation adjusted',receiver='Sensor')
  eye=lens(4,12/7,'Eye: near object with accommodated lens',receiver='Retina fixed',eye=True)
  A.figures['OBJ-6118-4.3.3-15']=combined(camera,eye,'Camera and eye: real images on different receiving surfaces',offset=15)
  A.figures['OBJ-6118-4.3.3-15-M01']=camera
  A.figures['OBJ-6118-4.3.3-15-M02']=eye
  far=lens(12,2.4,'Distant-object eye',receiver='Retina at 3 cm',eye=True)
  near=lens(4,12/7,'Near-object eye',receiver='Same retina at 3 cm',eye=True)
  A.figures['OBJ-6118-4.3.3-15-M03']=combined(far,near,'Eye accommodation: shorter focal length; unchanged retina position',offset=22)
 if t==21:
  p=A.figures['OBJ-6118-5.1-09-M03'];p['labels'].append([2.5,-.25,'e⁻'])
 if t==23:
  x=[-1+i*.005 for i in range(361)];ohm=[v/10 for v in x];lamp=[math.copysign(.1*math.log1p(3*abs(v)),v) for v in x];diode=[-.00002 if v<0 else .00002*v if v<.55 else .000011+.13*(math.exp(8*(v-.55))-1) for v in x]
  curves={'Ohmic, fixed T':ohm,'Filament lamp':lamp,'Diode (illustrative knee)':diode}
  A.plot('5.2.4-06',x,curves,'Voltage / V','Current / A','Three characteristics: fixed T, heating and directional conduction')
  A.plot('5.2.4-06-M01',x,{'Ohmic, fixed T':ohm},'Voltage / V','Current / A','Ohmic comparison: straight origin line')
  A.plot('5.2.4-06-M02',x,{'Lamp with heating':lamp,'Fixed-T resistor':ohm},'Voltage / V','Current / A','Filament heating reduces I–V slope')
  A.plot('5.2.4-06-M03',x,{'Diode':diode,'Fixed-T resistor':ohm},'Voltage / V','Current / A','Diode knee and reverse blocking (illustrative)',annotations=[[.55,.01,'Forward knee']])
  A.geometry('5.3-01-M02',[seg([[-4,0],[-3.5,0]],'black'),seg([[-2.5,0],[-2,0]],'black'),seg([[-.8,0],[0,0]],'black'),seg([[0,0],[.8,.5]],'black'),seg([[1,0],[1.5,0]],'black'),seg([[2.3,0],[3,0]],'black'),seg([[3,0],[4,0]],'black'),seg([[4,0],[4.5,0]],'black')],circles=[dict(centre=[0,0],radius=.055,color='black'),dict(centre=[1,0],radius=.055,color='black'),dict(centre=[3,0],radius=.055,color='black'),dict(centre=[4,0],radius=.055,color='black')],labels=[[-3.2,-.12,'~'],[-3.6,-.8,'AC supply'],[0,-.8,'Open'],[3,-.8,'Closed']],title='Syllabus AC mark and open/closed switches')
  A.geometry('5.3-01-M06',[seg([[-4,0],[-2,0]],'black'),seg([[-3.7,-.3],[-2.3,-.3],[-2.3,.3],[-3.7,.3],[-3.7,-.3]],'black'),seg([[0,-.3],[1.5,-.3],[1.5,.3],[0,.3],[0,-.3]],'black'),seg([[.75,-.3],[.75,.3]],'black'),seg([[-.7,0],[0,0]],'black'),seg([[1.5,0],[2.2,0]],'black'),seg([[.75,.3],[.75,1.2]],'grey',style='--'),seg([[0,1.2],[1.5,1.2]],'black'),seg([[-.5,1.2],[0,1.2]],'black'),seg([[1.5,1.2],[2,1.2]],'black')],circles=[dict(centre=[0,1.2],radius=.05,color='black'),dict(centre=[1.5,1.2],radius=.05,color='black')],labels=[[-3.5,-.8,'Fuse'],[.2,-.9,'Relay coil'],[.1,1.7,'Separate contacts']],title='Fuse and relay: dashed mechanical link')
 if t==25:
  F=A.figures;F['OBJ-6118-5.6-07']=combined(F['OBJ-6118-5.6-07-M01'],F['OBJ-6118-5.6-07-M02'],'Bar magnet and horseshoe central-gap comparison',offset=5)
  F['OBJ-6118-5.7.1.1-02']=combined(F['OBJ-6118-5.7.1.1-02-M01'],F['OBJ-6118-5.7.1.1-02-M02'],'Wire and solenoid: different field patterns',offset=6)
  # Dot/cross winding orientation makes the assigned pole direction checkable.
  p=F['OBJ-6118-5.7.1.1-02-M02'];p['labels'] += [[-.8,.65,'⊙ ⊙ ⊙: current out'],[-.8,-.85,'⊗ ⊗ ⊗: current in']]
 if t==26:
  x=[n/200 for n in range(401)];a=[2*math.sin(2*math.pi*v) for v in x];b=[4*math.sin(4*math.pi*v) for v in x]
  A.plot('5.7.2.2-02',x,{'Original: 2 V, T=1 s':a,'Twice rate: 4 V, T=0.5 s':b},'Time / s','Induced e.m.f. / V','Generator comparison: same coil and field',xlim=[0,2],ylim=[-4.5,4.5])
  A.plot('5.7.2.2-02-M01',x,{'Original rotation':a},'Time / s','Induced e.m.f. / V','Original generator: peak 2 V; period 1 s',xlim=[0,2],ylim=[-4.5,4.5],annotations=[[.25,2,'Peak 2 V']])
  A.plot('5.7.2.2-02-M02',x,{'Twice rotation rate':b},'Time / s','Induced e.m.f. / V','Faster generator: peak 4 V; period 0.5 s',xlim=[0,2],ylim=[-4.5,4.5],annotations=[[.125,4,'Peak 4 V']])
