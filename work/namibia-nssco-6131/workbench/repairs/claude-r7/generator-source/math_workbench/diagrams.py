"""Code-native diagram specifications, rendered offline as SVG and true-size PDF."""
from html import escape
from copy import deepcopy
import math
from pathlib import Path


def line(a,b,*,dash=False,color='black',width=.35):
    return dict(kind='line',a=list(a),b=list(b),dash=dash,color=color,width=width)


def arrow(a,b,*,color='black'):
    dx,dy=b[0]-a[0],b[1]-a[1];length=math.hypot(dx,dy)
    assert length>0
    ux,uy=dx/length,dy/length
    head=[b,(b[0]-3*ux+1.2*uy,b[1]-3*uy-1.2*ux),(b[0]-3*ux-1.2*uy,b[1]-3*uy+1.2*ux)]
    return [line(a,b,color=color),polygon(head,fill=color,color=color)]


def text(p,value,*,size=3):
    return dict(kind='text',p=list(p),value=str(value),size=size)


def circle(p,r,*,fill='none',color='black'):
    return dict(kind='circle',p=list(p),r=r,fill=fill,color=color)


def polygon(points,*,fill='none',color='black'):
    return dict(kind='polygon',points=[list(p) for p in points],fill=fill,color=color)


def polyline(points,*,color='black'):
    return dict(kind='polyline',points=[list(p) for p in points],fill='none',color=color)


def rect(x,y,w,h,*,fill='none'):
    return polygon([(x,y),(x+w,y),(x+w,y+h),(x,y+h)],fill=fill)


def spec(width,height,commands,**metadata):
    return dict(width_mm=width,height_mm=height,commands=commands,**metadata)


def calibrated(diagram):
    """A physical 20 mm check detects accidental fit-to-page printing."""
    diagram=deepcopy(diagram)
    height=diagram['height_mm']
    diagram['commands'] += [line((8,height+6),(28,height+6)),
        line((8,height+4.5),(8,height+7.5)),line((28,height+4.5),(28,height+7.5)),
        text((32,height+5),'Print check: this line must measure 2 cm',size=2.5)]
    diagram['height_mm']=height+13
    diagram['width_mm']=max(diagram['width_mm'],145)
    diagram['calibration_mm']=20
    return diagram


def asset(key,question,solution=None,*,physical=False):
    return dict(asset_id=key,role='question_and_solution',
                question_diagram=calibrated(question) if physical else question,
                solution_diagram=calibrated(solution or question) if physical else solution or question,
                print_at_actual_size=physical,
                display_instruction=('Print the supplied PDF at 100% / actual size. Check the 2 cm calibration line before measuring.' if physical else 'Use the labelled diagram and its coordinate scale; do not measure the screen.'))


def learner_assets(assets):
    """Allowlist projection. No answer/reference content crosses this boundary."""
    result=[]
    for item in assets:
        if item.get('role')!='question_and_solution':continue
        public={k:item[k] for k in ('asset_id','question_diagram','prepared_question_reference',
                'print_at_actual_size','display_instruction') if k in item}
        if 'question_diagram' in public or 'prepared_question_reference' in public:
            result.append(public)
    return result


def cartesian(xmin,xmax,ymin,ymax,*,width=150,height=110,grid=True,xstep=1,ystep=1):
    margin=12
    sx,sy=(width-2*margin)/(xmax-xmin),(height-2*margin)/(ymax-ymin)
    point=lambda x,y:(margin+(x-xmin)*sx,margin+(y-ymin)*sy)
    commands=[]
    ticks=lambda lo,hi,delta:[i*delta for i in range(math.ceil(lo/delta),math.floor(hi/delta)+1)]
    xticks,yticks=ticks(xmin,xmax,xstep),ticks(ymin,ymax,ystep)
    assert len(xticks)<=50 and len(yticks)<=50, 'Choose a readable graph scale'
    if grid:
        for x in xticks:
            commands.append(line(point(x,ymin),point(x,ymax),color='#dddddd',width=.15))
        for y in yticks:
            commands.append(line(point(xmin,y),point(xmax,y),color='#dddddd',width=.15))
    if ymin<=0<=ymax:
        commands.append(line(point(xmin,0),point(xmax,0)))
        for x in xticks:
            if abs(x)>1e-10: commands.append(text((point(x,0)[0]-.9,point(x,0)[1]-4),f'{x:g}',size=2.2))
        commands.append(text((width-8,point(xmax,0)[1]+2),'x'))
    if xmin<=0<=xmax:
        commands.append(line(point(0,ymin),point(0,ymax)))
        for y in yticks:
            if abs(y)>1e-10:commands.append(text((point(0,y)[0]-5,point(0,y)[1]-.7),f'{y:g}',size=2.2))
        commands.append(text((point(0,ymax)[0]+2,height-17),'y'))
    commands.append(text((point(max(xmin,0),max(ymin,0))[0]+1,point(max(xmin,0),max(ymin,0))[1]+1),'0',size=2.2))
    return spec(width,height,commands,coordinate_bounds=[xmin,xmax,ymin,ymax]),point


def render(diagram,stem):
    """SVG and PDF share millimetre geometry; the PDF preserves physical scale."""
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.colors import HexColor
    from reportlab.lib.units import mm
    stem=Path(stem);stem.parent.mkdir(parents=True,exist_ok=True)
    w,h=diagram['width_mm'],diagram['height_mm']
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}">',
         f'<rect width="{w}" height="{h}" fill="white"/>']
    pdf=Canvas(str(stem.with_suffix('.pdf')),pagesize=(w*mm,h*mm),invariant=1)
    for c in diagram['commands']:
        color=c.get('color','black'); fill=c.get('fill','none')
        pdf.setStrokeColor(HexColor(color) if color.startswith('#') else color)
        pdf.setLineWidth(c.get('width',.35)*mm)
        pdf.setDash(1.5*mm,1.5*mm) if c.get('dash') else pdf.setDash()
        style=f'stroke="{color}" stroke-width="{c.get("width",.35)}" fill="{fill}"'
        if c.get('dash'):style+=' stroke-dasharray="1.5 1.5"'
        if c['kind']=='line':
            (x1,y1),(x2,y2)=c['a'],c['b']
            svg.append(f'<line x1="{x1}" y1="{h-y1}" x2="{x2}" y2="{h-y2}" {style}/>')
            pdf.line(x1*mm,y1*mm,x2*mm,y2*mm)
        elif c['kind']=='text':
            x,y=c['p']; size=c['size'];value=c['value']
            svg.append(f'<text x="{x}" y="{h-y}" font-family="Arial,sans-serif" font-size="{size}">{escape(value)}</text>')
            pdf.setFillColor('black');pdf.setFont('Helvetica',size*mm);pdf.drawString(x*mm,y*mm,value)
        elif c['kind']=='circle':
            x,y=c['p'];r=c['r']
            svg.append(f'<circle cx="{x}" cy="{h-y}" r="{r}" {style}/>')
            if fill!='none':pdf.setFillColor(HexColor(fill) if fill.startswith('#') else fill)
            pdf.circle(x*mm,y*mm,r*mm,stroke=1,fill=int(fill!='none'))
        elif c['kind'] in ('polygon','polyline'):
            points=c['points']; svg.append(f'<{c["kind"]} points="'+' '.join(f'{x},{h-y}' for x,y in points)+f'" {style}/>')
            path=pdf.beginPath();path.moveTo(points[0][0]*mm,points[0][1]*mm)
            for x,y in points[1:]:path.lineTo(x*mm,y*mm)
            if c['kind']=='polygon':path.close()
            if fill!='none':pdf.setFillColor(HexColor(fill) if fill.startswith('#') else fill)
            pdf.drawPath(path,stroke=1,fill=int(fill!='none'))
        else:
            raise ValueError(c['kind'])
    svg.append('</svg>');stem.with_suffix('.svg').write_text('\n'.join(svg))
    # Even a blank construction canvas must be a valid one-page PDF.
    pdf.showPage()
    pdf.save()
