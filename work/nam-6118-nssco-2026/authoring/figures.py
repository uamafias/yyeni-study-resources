"""Parameter-generated original scientific plots; no source images or hand-edited figures."""
from pathlib import Path
import json,os
os.environ.setdefault('MPLCONFIGDIR','/tmp/6118-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def graph(folder,name,x,ys,xlabel,ylabel,title='',line=True,fit=False,triangle=False,origin=False,xlim=None,ylim=None,annotations=None):
 import numpy as np,textwrap
 folder.mkdir(parents=True,exist_ok=True)
 fig,ax=plt.subplots(figsize=(7,4.8),layout='constrained')
 styles=['-','--',':','-.'];marks=['x','o','s','^']
 for n,(label,y) in enumerate(ys.items()):
  assert len(x)==len(y)
  if fit:
   slope,intercept=np.polyfit(x,y,1);xx=np.array([min(0,min(x)) if origin else min(x),max(x)]);ax.plot(x,y,marker=marks[n%4],linestyle='None',markersize=6,label=label if 'readings' in label.lower() else label+' readings');ax.plot(xx,slope*xx+intercept,styles[n%4],lw=1.3,label='Fitted '+label.lower())
   if triangle and n==0:
    x0,x1=x[0],x[-1];y0,y1=slope*x0+intercept,slope*x1+intercept;ax.plot([x0,x1,x1],[y0,y0,y1],':',color='tab:red');ax.annotate('Δx = '+f'{x1-x0:g}',((x0+x1)/2,y0),xytext=(0,-15 if y1<y0 else 6),textcoords='offset points',fontsize=8,bbox=dict(facecolor='white',alpha=.85,edgecolor='none'));ax.annotate('Δy = '+f'{y1-y0:g}',(x1,(y0+y1)/2),xytext=(-5,0),ha='right',textcoords='offset points',fontsize=8)
  else:ax.plot(x,y,marker=marks[n%4] if len(x)<=25 else None,linestyle=styles[n%4] if line else 'None',linewidth=1.4,markersize=5,label=label)
 ax.set_xlabel(xlabel);ax.set_ylabel(ylabel);ax.set_title('\n'.join(textwrap.wrap(title,70)),fontsize=10);ax.grid(True,alpha=.25);ax.set_axisbelow(True)
 if origin:
  ax.set_xlim(left=min(0,min(x)));low=min([v for yy in ys.values() for v in yy] or [0]);ax.set_ylim(bottom=min(0,low))
 if xlim:ax.set_xlim(*xlim)
 if ylim:ax.set_ylim(*ylim)
 for ann in annotations or []:
  if isinstance(ann,dict):ax.annotate(**ann,fontsize=8,bbox=dict(facecolor='white',alpha=.9,edgecolor='none'))
  else:
   xx,yy,t=ann;ax.annotate(t,(xx,yy),xytext=(0,10),textcoords='offset points',ha='center',fontsize=8,bbox=dict(facecolor='white',alpha=.9,edgecolor='none'))
 ax.margins(y=.12)
 if ys:ax.legend(fontsize=8)
 path=folder/(name+'.png');fig.savefig(path,dpi=160);plt.close(fig)
 return path

def vectors(folder,name,components,unit='N',title='Vector addition'):
 import math
 folder.mkdir(parents=True,exist_ok=True);fig,ax=plt.subplots(figsize=(6,4.3),layout='constrained');x=y=0;points=[(0,0)]
 for n,(mag,angle) in enumerate(components,1):
  dx=mag*math.cos(math.radians(angle));dy=mag*math.sin(math.radians(angle));ax.annotate('',xy=(x+dx,y+dy),xytext=(x,y),arrowprops=dict(arrowstyle='->',lw=1.8,color='tab:blue'));ax.annotate(f'Vector {n}: {mag:g} {unit}',(x+dx/2,y+dy/2),xytext=(12,-10) if n==2 else (0,10),textcoords='offset points',fontsize=8,bbox=dict(facecolor='white',alpha=.9,edgecolor='none'));x+=dx;y+=dy;points.append((x,y))
 ax.annotate('',xy=(x,y),xytext=(0,0),arrowprops=dict(arrowstyle='->',lw=1.8,color='tab:red',linestyle='--'));ax.text(x*.35,y*.35-.5,f'Resultant = {math.hypot(x,y):.2f} {unit}\n{math.degrees(math.atan2(y,x)):.1f}° north of east',color='tab:red',fontsize=8)
 pad=max(1,max(abs(a)+abs(b) for a,b in points)*.12);ax.set_xlim(min(a for a,b in points)-pad,max(a for a,b in points)+pad);ax.set_ylim(min(b for a,b in points)-pad,max(b for a,b in points)+pad);ax.set_aspect('equal');ax.set_xlabel('Eastward component / '+unit);ax.set_ylabel('Northward component / '+unit);ax.grid(alpha=.25);ax.set_title(title+'\nScale: one labelled axis unit = 1 '+unit,fontsize=10);path=folder/(name+'.png');fig.savefig(path,dpi=160);plt.close(fig);return path

def geometry(folder,name,segments=None,circles=None,labels=None,title='Original construction',panels=None):
 from matplotlib.patches import Circle
 import textwrap
 folder.mkdir(parents=True,exist_ok=True)
 pp=panels or [dict(segments=segments or [],circles=circles or [],labels=labels or [])]
 fig,aa=plt.subplots(1,len(pp),figsize=(7*len(pp),5),layout='constrained',squeeze=False)
 for ax,p in zip(aa[0],pp):
  for s in p['segments']:
   pts=s['points'];ax.plot([v[0] for v in pts],[v[1] for v in pts],s.get('style','-'),color=s.get('color','tab:blue'),lw=1.4)
   if s.get('arrow'):
    pairs=list(zip(pts,pts[1:])) if len(pts)<=6 else [(pts[int((len(pts)-1)*.42)],pts[int((len(pts)-1)*.58)])]
    for a,b in pairs:
     v=(a[0]+.35*(b[0]-a[0]),a[1]+.35*(b[1]-a[1]));w=(a[0]+.65*(b[0]-a[0]),a[1]+.65*(b[1]-a[1]));ax.annotate('',xy=w,xytext=v,arrowprops=dict(arrowstyle='-|>',color=s.get('color','tab:blue'),lw=1.4,mutation_scale=12))
  for c in p.get('circles',[]):ax.add_patch(Circle(c['centre'],c['radius'],fill=False,color=c.get('color','tab:blue'),lw=1.3))
  for x,y,txt in p.get('labels',[]):
   ax.text(x,y,txt,fontsize=9,bbox=dict(facecolor='white',alpha=.9,edgecolor='none',pad=.7));ax.update_datalim([[x,y]])
  ax.autoscale_view();ax.margins(.2);ax.set_aspect('equal');ax.set_axis_off()
  if panels:ax.set_title('\n'.join(textwrap.wrap(p.get('title',''),55)),fontsize=10,pad=18)
 fig.suptitle('\n'.join(textwrap.wrap(title,90)),fontsize=11)
 path=folder/(name+'.png');fig.savefig(path,dpi=160);plt.close(fig);return path

def comparison(folder,name,panels,title=''):
 folder.mkdir(parents=True,exist_ok=True);fig,axes=plt.subplots(1,len(panels),figsize=(10,4),layout='constrained')
 for ax,p in zip(axes,panels):
  for label,y in p['ys'].items():ax.plot(p['x'],y,label=label)
  ax.set_xlabel(p['xlabel']);ax.set_ylabel(p['ylabel']);ax.set_title(p['title']);ax.set_ylim(bottom=0);ax.grid(alpha=.25)
 fig.suptitle(title);path=folder/(name+'.png');fig.savefig(path,dpi=160);plt.close(fig);return path
