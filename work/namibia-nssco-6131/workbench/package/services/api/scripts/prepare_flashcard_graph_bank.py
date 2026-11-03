"""Build original gradient pilot PNGs (Pillow, build time only).

Existing manifests are immutable. Changed content requires a new bank version.
"""
import hashlib
import io
import json
from fractions import Fraction
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1] / 'data' / 'flashcard_graphs' / 'v1'


def build(font_path):
    ROOT.mkdir(parents=True, exist_ok=True)
    manifest = []
    font = ImageFont.truetype(font_path, 18)
    small = ImageFont.truetype(font_path, 15)
    for i in range(40):
        xp, xq = -(i // 8 + 1), i % 8 + 1
        m = (Fraction(1, 2), Fraction(-1, 2), Fraction(1), Fraction(-1))[i % 4]
        c = i % 5 - 2
        yp, yq = m*xp+c, m*xq+c
        row = dict(id=f'{i:02d}', xp=xp, xq=xq, numerator=m.numerator,
                   denominator=m.denominator, intercept=c, assets={})
        for role in ('question', 'answer'):
            im = Image.new('RGB', (820, 780), 'white'); d = ImageDraw.Draw(im)
            def point(x, y): return (400+float(x)*27, 350-float(y)*27)
            for tick in range(-24, 25):
                v = tick / 2
                colour = '#c3ccd5' if tick % 2 == 0 else '#e9edf1'
                d.line([point(v,-12), point(v,12)], fill=colour)
                d.line([point(-12,v), point(12,v)], fill=colour)
            d.line([point(-12,0), point(12,0)], fill='black', width=2)
            d.line([point(0,-12), point(0,12)], fill='black', width=2)
            for v in range(-11, 12):
                if v:
                    d.text((point(v,0)[0]-7,357),str(v),font=small,fill='black')
                    d.text((374,point(0,v)[1]-8),str(v),font=small,fill='black')
            d.text((737,344),'x',font=font,fill='black'); d.text((410,12),'y',font=font,fill='black')
            d.text((387,357),'0',font=small,fill='black')
            pts = [point(Fraction(k,20),m*Fraction(k,20)+c) for k in range(-240,241)
                   if -12 <= m*Fraction(k,20)+c <= 12]
            d.line(pts,fill='#174f8a',width=3)
            for name,x,y in [('P',xp,yp),('Q',xq,yq)]:
                px,py=point(x,y); d.ellipse((px-5,py-5,px+5,py+5),fill='#174f8a')
                d.text((px+9,py-26),name,font=font,fill='#174f8a',stroke_width=2,stroke_fill='white')
            d.text((76,696),'Find the gradient of the straight line PQ. Show your working.',font=font,fill='black')
            if role == 'answer':
                d.line([point(xp,yp),point(xq,yp),point(xq,yq)],fill='#9b3918',width=3)
                d.text((76,727),f'P = ({xp}, {yp}); Q = ({xq}, {yq})',font=font,fill='#9b3918')
                d.text((76,752),f'Gradient = ({yq} - ({yp})) / ({xq} - ({xp})) = {m}',font=font,fill='#9b3918')
            output=io.BytesIO(); im.save(output,format='PNG',optimize=True); data=output.getvalue()
            digest=hashlib.sha256(data).hexdigest(); filename=f'{i:02d}-{role}-{digest}.png'
            target=ROOT / filename
            if not target.exists(): target.write_bytes(data)
            row['assets'][role]={'filename':filename,'sha256':digest}
        manifest.append(row)
    target=ROOT/'manifest.json'
    serialized=json.dumps(manifest,indent=2)+'\n'
    if target.exists() and target.read_text()!=serialized:
        raise RuntimeError('Bank differs: create a new version rather than replacing its manifest.')
    target.write_text(serialized)
    print(f'Prepared {len(manifest)} immutable graph pairs in {ROOT}')

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(); p.add_argument('--font',required=True)
    build(p.parse_args().font)
