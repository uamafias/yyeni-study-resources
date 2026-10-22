"""Original deterministic organic-diagram primitives shared within this subject."""
import math
from render_chemistry_visuals_8224 import Figure

def curved_arrow(f,start,end,control,colour='#a13922',single=False):
    pts=[]
    for k in range(51):
        u=k/50
        pts.append(((1-u)**2*start[0]+2*(1-u)*u*control[0]+u*u*end[0],(1-u)**2*start[1]+2*(1-u)*u*control[1]+u*u*end[1]))
    f.line(pts,colour,2)
    dx=end[0]-pts[-2][0];dy=end[1]-pts[-2][1];a=math.atan2(dy,dx)
    p1=(end[0]-12*math.cos(a-.45),end[1]-12*math.sin(a-.45));p2=(end[0]-12*math.cos(a+.45),end[1]-12*math.sin(a+.45))
    if single:f.line([p1,end],colour,2)
    else:f.polygon([p1,end,p2],colour)

def planar_ethene(out,slug='8224-ethene-planar'):
    f=Figure('Ethene: planar around each carbon','Two carbon atoms joined by a double bond. Each carbon joins two hydrogens in one plane; angles approximately 120 degrees. Schematic lengths.')
    f.text(300,205,'C',32);f.text(500,205,'C',32);f.line([(336,220),(483,220)]);f.line([(336,232),(483,232)])
    for c,h in [((315,225),(245,104)),((315,225),(245,346)),((515,225),(585,104)),((515,225),(585,346))]:
        dx=h[0]-c[0];dy=h[1]-c[1];length=math.hypot(dx,dy)
        f.line([(c[0]+25*dx/length,c[1]+25*dy/length),(h[0]-24*dx/length,h[1]-24*dy/length)])
        f.text(h[0]-10,h[1]-18,'H',28)
    f.text(32,65,'Angles at each carbon ≈120°',18);f.text(26,380,'All six atoms lie in one plane.',18);f.text(26,420,'C=C is shorter than the C–C single bond in ethane.',18)
    f.save(slug,out=out)

def tetrahedral_carbon(out,slug='8224-carbon-tetrahedral'):
    f=Figure('Carbon with four single-bond regions','A carbon centre with four single bonds in a tetrahedral arrangement. Two in-plane bonds, one solid wedge towards and one hashed away. Approximate angles 109.5 degrees. R is a single-bonded group.')
    f.text(407,214,'C',32)
    for x,y,label in [(280,132,'H'),(560,132,'H')]:f.line([(400 if x<420 else 440,212),(x+15 if x<420 else x-15,y+16)]);f.text(x-10,y-18,label,29)
    f.polygon([(405,252),(300,343),(320,360)]);f.text(288,367,'H',29)
    for k in range(2,11):
        u=k/11;x=420+110*u;y=230+130*u;d=9*u;f.line([(x-d,y+d*.7),(x+d,y-d*.7)],width=2)
    f.text(535,367,'R',29);f.text(32,95,'H–C–H / H–C–R',18);f.text(32,127,'≈109.5°',20);f.text(26,422,'R = a single-bonded group; R = CH3 gives a carbon centre in ethane.',17)
    f.save(slug,out=out)
