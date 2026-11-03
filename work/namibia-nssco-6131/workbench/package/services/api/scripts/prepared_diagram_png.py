"""Build-time PNG preparation for the constrained authored diagram vocabulary.

No browser or runtime rendering. PNGs are bundled immutable flashcard assets.
"""
import io
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont

COLORS={'ink':'#192c3d','blue':'#235c98','purple':'#78449b','green':'#22724a',
        'red':'#a8312b','gray':'#73808b','orange':'#ac5e12'}


def render(spec, font_path):
    from services.math_generators.figures import validate_figure
    validate_figure(spec)
    width,height=1100,900
    canvas=Image.new('RGB',(width,height),'white'); draw=ImageDraw.Draw(canvas)
    font=ImageFont.truetype(font_path,22); small=ImageFont.truetype(font_path,17)
    for i,row in enumerate(textwrap.wrap(spec['caption'],85)):
        draw.text((85,12+26*i),row,font=font,fill=COLORS['ink'])
    xmin,xmax,ymin,ymax=spec['bounds']; box=(115,95,995,795)
    sx=(box[2]-box[0])/(xmax-xmin); sy=(box[3]-box[1])/(ymax-ymin)
    if spec.get('equal_scale',True): sx=sy=min(sx,sy)
    left=box[0]+((box[2]-box[0])-(xmax-xmin)*sx)/2
    top=box[1]+((box[3]-box[1])-(ymax-ymin)*sy)/2
    right=left+(xmax-xmin)*sx; bottom=top+(ymax-ymin)*sy
    def xy(x,y):return (left+(x-xmin)*sx,top+(ymax-y)*sy)
    axes=spec.get('axes')
    if axes:
        xaxis=max(ymin,min(ymax,0)); yaxis=max(xmin,min(xmax,0))
        x0,y0=xy(yaxis,xaxis)
        draw.rectangle((left,top,right,bottom),outline='#a8b6c2')
        for direction,step,low,high in [('x',axes['x_step'],xmin,xmax),('y',axes['y_step'],ymin,ymax)]:
            first=math.ceil(low/step)
            for n in range(first,math.floor(high/step)+1):
                value=n*step; label=f'{value:g}'
                if direction=='x':
                    pos=xy(value,xaxis)[0]
                    if axes.get('grid'):draw.line((pos,top,pos,bottom),fill='#dce3e9')
                    draw.line((pos,y0-4,pos,y0+4),fill=COLORS['ink'])
                    draw.text((pos-5,y0+7),label,font=small,fill=COLORS['ink'])
                else:
                    pos=xy(yaxis,value)[1]
                    if axes.get('grid'):draw.line((left,pos,right,pos),fill='#dce3e9')
                    draw.line((x0-4,pos,x0+4,pos),fill=COLORS['ink'])
                    if value!=0:draw.text((x0-12,pos-9),label,anchor='ra',font=small,fill=COLORS['ink'])
        draw.line((left,y0,right,y0),fill=COLORS['ink'],width=2)
        draw.line((x0,top,x0,bottom),fill=COLORS['ink'],width=2)
        draw.text(((left+right)/2,843),axes.get('x_label',''),anchor='mm',font=font,fill=COLORS['ink'])
        label=Image.new('RGBA',(780,38)); ImageDraw.Draw(label).text((390,19),axes.get('y_label',''),anchor='mm',font=font,fill=COLORS['ink'])
        label=label.rotate(90,expand=True);canvas.paste(label,(9,int((top+bottom-label.height)/2)),label)
    # Clip all diagram primitives to the declared plot rectangle. In particular,
    # reciprocal branches and curve extensions must not overwrite axis labels.
    layer=Image.new('RGBA',canvas.size); d=ImageDraw.Draw(layer)
    def stroke(points,colour,dashed):
        if not dashed:d.line(points,fill=colour,width=3);return
        for a,b in zip(points,points[1:]):
            length=math.hypot(b[0]-a[0],b[1]-a[1])
            if not length:continue
            for pos in range(0,int(length)+1,15):
                t=pos/length; u=min(1,(pos+8)/length)
                d.line((a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1]),a[0]+u*(b[0]-a[0]),a[1]+u*(b[1]-a[1])),fill=colour,width=2)
    for e in spec['elements']:
        kind=e['kind'];colour=COLORS[e.get('color','ink')]
        if kind in ('polyline','polygon'):
            points=[xy(*p) for p in e['points']]
            if e.get('fill'):
                d.polygon(points,fill=colour+'35')
            if kind=='polygon' and points[0]!=points[-1]:points.append(points[0])
            stroke(points,colour,e.get('dashed',False))
        elif kind=='circle':
            points=[xy(e['x']+e['r']*math.cos(a*math.pi/90),e['y']+e['r']*math.sin(a*math.pi/90)) for a in range(181)]
            if e.get('fill'):d.polygon(points,fill=colour+'90')
            stroke(points,colour,e.get('dashed',False))
        elif kind=='point':
            x,y=xy(e['x'],e['y']); d.ellipse((x-5,y-5,x+5,y+5),fill=colour)
        else:
            x,y=xy(e['x'],e['y']);d.text((x,y),e['text'],anchor='mm',font=font,fill=colour,stroke_width=2,stroke_fill='white')
    clip=(max(0,int(left)-2),max(0,int(top)-2),min(width,math.ceil(right)+3),min(height,math.ceil(bottom)+3))
    cropped=layer.crop(clip);canvas.paste(cropped,clip[:2],cropped)
    output=io.BytesIO();canvas.save(output,format='PNG',optimize=True)
    return output.getvalue()
