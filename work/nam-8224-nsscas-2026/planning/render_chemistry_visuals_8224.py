#!/usr/bin/env python3
"""Generate original, deterministic Chemistry SVG/PNG assets from one geometry.

Keep this subject-specific renderer outside the shared standard. PNG is the
offline preview/fallback; SVG is the scalable publication asset. No third-party
figures are copied. Both formats use the identical primitive list.
"""
import hashlib
import html
import json
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WS = Path(__file__).resolve().parents[1]
OUT = WS / 'exemplar' / 'visual' / 'assets'
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
W, H = 840, 460


class Figure:
    def __init__(self, title, description):
        self.title, self.description = title, description
        self.shapes = []
        self.text(26, 26, title, 25)

    def text(self, x, y, text, size=18, colour='#172b3a'):
        self.shapes.append(('text', [x, y, text, size, colour]))

    def line(self, points, colour='#24475c', width=3):
        self.shapes.append(('line', [points, colour, width]))

    def arrow(self, a, b, colour='#24475c', width=3):
        self.line([a, b], colour, width)
        angle = math.atan2(b[1]-a[1], b[0]-a[0])
        ends = [(b[0]-11*math.cos(angle+d), b[1]-11*math.sin(angle+d)) for d in [-.45, .45]]
        self.line([ends[0], b, ends[1]], colour, width)

    def circle(self, x, y, r=9, colour='#176e9a'):
        self.shapes.append(('circle', [x, y, r, colour]))

    def polygon(self, points, colour='#24475c'):
        self.shapes.append(('polygon', [points, colour]))

    def save(self, slug, out=None):
        destination = Path(out) if out is not None else OUT
        destination.mkdir(parents=True, exist_ok=True)
        canvas = Image.new('RGB', (W*2, H*2), 'white')
        draw = ImageDraw.Draw(canvas)
        svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
               f'<title id="title">{html.escape(self.title)}</title><desc id="desc">{html.escape(self.description)}</desc>',
               '<rect width="100%" height="100%" fill="white"/>']
        for kind, args in self.shapes:
            if kind == 'text':
                x,y,text,size,colour = args
                svg.append(f'<text x="{x}" y="{y}" dominant-baseline="text-before-edge" font-family="Arial, sans-serif" font-size="{size}" fill="{colour}">{html.escape(text)}</text>')
                draw.text((x*2,y*2), text, font=ImageFont.truetype(FONT,size*2), fill=colour)
            elif kind == 'line':
                points,colour,width = args
                svg.append(f'<polyline points="{" ".join(f"{x},{y}" for x,y in points)}" fill="none" stroke="{colour}" stroke-width="{width}" stroke-linejoin="round"/>')
                draw.line([(x*2,y*2) for x,y in points],fill=colour,width=width*2)
            elif kind == 'polygon':
                points,colour=args
                svg.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in points)}" fill="{colour}"/>')
                draw.polygon([(x*2,y*2) for x,y in points],fill=colour)
            else:
                x,y,r,colour=args
                svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{colour}"/>')
                draw.ellipse(((x-r)*2,(y-r)*2,(x+r)*2,(y+r)*2),fill=colour)
        svg.append('</svg>')
        (destination / f'{slug}.svg').write_text('\n'.join(svg)+'\n')
        canvas.save(destination / f'{slug}.png')
        (destination / f'{slug}.geometry.json').write_text(json.dumps({'title':self.title,'description':self.description,'width':W,'height':H,'primitives':self.shapes},indent=2)+'\n')


def build():
    f=Figure('Charged particles between electric plates',
             'Particles enter to the right. Positive upper plate and negative lower plate: electron bends upwards more strongly, proton downwards less strongly at equal entry speeds, neutron continues straight. Schematic; deflections are not to scale.')
    f.line([(150,100),(650,100)],'#bd492d',7)
    f.text(230,63,'Positive plate:  +   +   +   +   +',19,'#a13922')
    f.line([(150,350),(650,350)],'#176e9a',7)
    f.text(230,365,'Negative plate:  −   −   −   −   −',19,'#176e9a')
    f.arrow((90,225),(165,225))
    f.text(28,245,'Entry',16)
    for sign,colour,label in [(-1,'#176e9a','Electron'),(0,'#66747b','Neutron'),(1,'#b94d2c','Proton')]:
        points=[(165+x,225+sign*85*(0.25 if sign==1 else 1)*(x/470)**2) for x in range(0,471,10)]
        f.line(points,colour,4);f.arrow(points[-2],points[-1],colour,4)
        f.text(662,points[-1][1]-12,label,18,colour)
    f.arrow((760,108),(760,174),'#66747b',2);f.text(685,184,'Field direction',15)
    f.text(26,418,'Equal entry speeds: electron bends more; deflections are not to scale.',17)
    f.save('8224-electric-field')

    f=Figure('Ethanol: displayed formula', 'Ethanol with two carbons, six hydrogens and one oxygen; every covalent bond is drawn, including O–H.')
    positions={'C1':(265,235),'C2':(425,235),'O':(585,235),'H1':(105,235),'H2':(265,105),'H3':(265,365),'H4':(425,105),'H5':(425,365),'H6':(745,235)}
    bonds=[('C1','C2'),('C2','O'),('O','H6'),('C1','H1'),('C1','H2'),('C1','H3'),('C2','H4'),('C2','H5')]
    for a,b in bonds:
        x,y=positions[a];xx,yy=positions[b];distance=math.hypot(xx-x,yy-y);dx=(xx-x)/distance*25;dy=(yy-y)/distance*25
        f.line([(x+dx,y+dy),(xx-dx,yy-dy)])
    for name,(x,y) in positions.items():f.text(x-13,y-21,name[0],34,'#a13922' if name=='O' else '#172b3a')
    f.text(26,416,'Every bond is shown; atom count: C2H6O.',18)
    f.save('8224-ethanol-displayed')

    f=Figure('Gas volume during a reaction', 'Original illustrative data: time in seconds 0,20,40,60,80,100; gas volume in cubic centimetres 0,20,32,39,43,45. A declining gradient shows slowing gas production.')
    f.text(26,65,'Gas volume / cm³',18)
    f.arrow((100,360),(750,360));f.arrow((100,360),(100,110))
    data=[(0,0),(20,20),(40,32),(60,39),(80,43),(100,45)]
    for t,v in data:
        x=100+6*t;y=360-5*v
        f.circle(x,y,5)
        f.line([(x,360),(x,367)],width=1);f.text(x-10,374,str(t),15)
    f.line([(100+6*t,360-5*v) for t,v in data],width=3)
    for v in range(0,51,10):
        y=360-5*v;f.line([(93,y),(100,y)],width=1);f.text(60,y-10,str(v),15)
    f.text(660,405,'Time / s',18);f.text(200,80,'Original illustrative data; points joined by straight segments.',16)
    f.save('8224-rates-graph')

    f=Figure('Titration apparatus: arrangement', 'Schematic of a clamped vertical burette over a conical flask on a white tile. The burette jet points into the flask opening. The support stand is shown.')
    f.line([(130,380),(270,380)],width=8);f.line([(190,380),(190,88)],width=6)
    f.line([(190,145),(400,145)],width=5);f.line([(386,132),(418,132),(418,159),(386,159)],width=3)
    f.line([(393,74),(393,250),(399,261),(399,291)],width=3);f.line([(411,74),(411,250),(405,261),(405,291)],width=3)
    for y in range(92,242,15):f.line([(394,y),(404,y)],width=1)
    f.line([(382,256),(425,256)],width=4)
    f.line([(381,305),(381,320),(338,365),(338,374),(466,374),(466,365),(423,320),(423,305)],width=3)
    f.line([(344,361),(461,361)],'#176e9a',4);f.line([(318,380),(488,380)],'#66747b',4)
    for x,y,label,tx,ty in [(411,104,'Burette',510,90),(425,256,'Tap',510,230),(405,287,'Jet',510,278),(455,349,'Conical flask',510,330),(488,380,'White tile',510,382)]:
        f.line([(x,y),(tx-14,ty+10)],'#66747b',1);f.text(tx,ty,label,18)
    f.text(26,419,'Schematic arrangement; apparatus dimensions are not to scale.',17)
    f.save('8224-titration-apparatus')
    paths=sorted(OUT.glob('*'))
    (OUT.parent/'assets-manifest.json').write_text(json.dumps({'generator':str(Path(__file__).relative_to(WS)), 'assets':[{'path':'assets/'+p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]},indent=2)+'\n')
    thumbs=[]
    for p in sorted(OUT.glob('*.png')):
        im=Image.open(p);im.thumbnail((840,460));thumbs.append(im)
    contact=Image.new('RGB',(1680,920),'#dddddd')
    for n,im in enumerate(thumbs):contact.paste(im,((n%2)*840,(n//2)*460))
    contact.save(OUT.parent/'contact-sheet.png')
    print('Generated four SVG/PNG figure pairs, geometry, manifest and contact sheet.')


if __name__=='__main__':build()
