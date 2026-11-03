"""Bounded, data-only diagrams frozen into existing question/answer snapshots."""
import json
import math
import re

FENCE='yyeni-maths-figure'
MAX_BYTES=120000
COLORS={'ink','blue','purple','green','red','gray','orange'}
KINDS={'polyline','polygon','circle','text','point'}
BLOCK=re.compile(r'```yyeni-maths-figure\n([^`]*?)\n```',re.S)


def _number(v):
    return type(v) in (int,float) and math.isfinite(v) and abs(v)<=100000


def validate_figure(s):
    if not isinstance(s,dict) or set(s)-{'v','bounds','caption','axes','elements','equal_scale'}:raise ValueError('Invalid figure fields')
    if s.get('v')!=1 or type(s.get('v')) is not int:raise ValueError('Unknown figure version')
    b=s.get('bounds')
    if not isinstance(b,list) or len(b)!=4 or not all(_number(v) for v in b):raise ValueError('Invalid bounds')
    if not (0<b[1]-b[0]<=10000 and 0<b[3]-b[2]<=10000):raise ValueError('Invalid range')
    def label(v,limit):return isinstance(v,str) and len(v)<=limit and not re.search(r'[\x00-\x1f`]',v)
    if not label(s.get('caption',''),240):raise ValueError('Invalid caption')
    if 'equal_scale' in s and type(s['equal_scale']) is not bool:raise ValueError('Invalid scale')
    axes=s.get('axes')
    if axes is not None:
        if not isinstance(axes,dict) or set(axes)-{'x_step','y_step','x_label','y_label','grid'}:raise ValueError('Invalid axes')
        for key,span in (('x_step',b[1]-b[0]),('y_step',b[3]-b[2])):
            v=axes.get(key)
            if not _number(v) or not span/80<=v<=span:raise ValueError('Too many ticks')
        if not all(label(axes.get(k,''),60) for k in ('x_label','y_label')):raise ValueError('Invalid axis labels')
        if 'grid' in axes and type(axes['grid']) is not bool:raise ValueError('Invalid grid')
    elements=s.get('elements')
    if not isinstance(elements,list) or len(elements)>250:raise ValueError('Too many elements')
    points=0
    for e in elements:
        if not isinstance(e,dict) or e.get('kind') not in KINDS:raise ValueError('Invalid primitive')
        allowed={'kind','color','dashed','fill'}|({'points'} if e['kind'] in ('polyline','polygon') else {'x','y','r'} if e['kind']=='circle' else {'x','y','text'} if e['kind']=='text' else {'x','y'})
        if set(e)-allowed:raise ValueError('Unknown primitive attribute')
        if e.get('color','ink') not in COLORS:raise ValueError('Invalid colour')
        if any(k in e and type(e[k]) is not bool for k in ('dashed','fill')):raise ValueError('Invalid style')
        if e['kind'] in ('polyline','polygon'):
            ps=e.get('points');minimum=3 if e['kind']=='polygon' else 2
            if not isinstance(ps,list) or not minimum<=len(ps)<=500:raise ValueError('Invalid points')
            if not all(isinstance(p,list) and len(p)==2 and all(_number(v) for v in p) for p in ps):raise ValueError('Invalid point')
            points+=len(ps)
        elif not all(_number(e.get(k)) for k in ('x','y')):raise ValueError('Invalid position')
        if e['kind']=='circle' and (not _number(e.get('r')) or e['r']<=0):raise ValueError('Invalid radius')
        if e['kind']=='text' and not label(e.get('text'),100):raise ValueError('Invalid text')
    if points>12000 or len(json.dumps(s).encode())>MAX_BYTES:raise ValueError('Figure too large')
    return s


def figure(spec):
    validate_figure(spec)
    return '\n\n```'+FENCE+'\n'+json.dumps(spec,sort_keys=True,separators=(',',':'),ensure_ascii=False)+'\n```\n\n'


def figures_in(text):
    for m in BLOCK.finditer(text):
        if len(m[1].encode())>MAX_BYTES:raise ValueError('Figure too large')
        yield validate_figure(json.loads(m[1]))


def spec(bounds,caption,elements=(),axes=None,equal_scale=True):
    out={'v':1,'bounds':list(bounds),'caption':caption,'elements':list(elements),'equal_scale':equal_scale}
    if axes is not None:out['axes']=axes
    return validate_figure(out)


def line(points,color='ink',dashed=False,fill=False):
    return {'kind':'polygon' if fill else 'polyline','points':[[round(float(x),6),round(float(y),6)] for x,y in points],'color':color,'dashed':dashed,'fill':fill}


def text(x,y,label,color='ink'):return {'kind':'text','x':round(float(x),6),'y':round(float(y),6),'text':str(label),'color':color}
def point(x,y,color='ink'):return {'kind':'point','x':float(x),'y':float(y),'color':color}
def circle(x,y,r,color='ink',dashed=False,fill=False):return {'kind':'circle','x':float(x),'y':float(y),'r':float(r),'color':color,'dashed':dashed,'fill':fill}


def arc(x,y,r,start,end,color='blue',dashed=False):
    return line([(x+r*math.cos(math.radians(start+(end-start)*i/48)),y+r*math.sin(math.radians(start+(end-start)*i/48))) for i in range(49)],color,dashed)


def grid(bounds,elements=(),caption='Coordinate grid',x_label='x',y_label='y',x_step=1,y_step=1,equal_scale=True):
    return spec(bounds,caption,elements,{'x_step':x_step,'y_step':y_step,'x_label':x_label,'y_label':y_label,'grid':True},equal_scale)
