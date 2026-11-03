"""Bounds: syllabus p.11 and existing NSSCO 2020–2024 bound/accuracy evidence."""
import re
from .number_teaching import F,n,frac,work

LABELS={1:'Writing a rounding interval',2:'Finding a single upper or lower bound',3:'Bounding rectangle area and perimeter',
        4:'Choosing bounds for sums and differences',5:'Bounding speed, area and volume'}


def interval(letter,value,unit):
    v,u=F(value),F(unit)
    return f'{n(v-u/2)}\\le {letter}<{n(v+u/2)}'


def content(problem):
    m=problem.machine;task=m['task'];lines=[]
    endpoint='The lower rounding endpoint is included and the upper endpoint excluded. An upper bound is a limiting value; the measurement need not attain it.'
    if task in ('bounds_inequality','single_bound'):
        value,unit=F(m['value']),F(m['unit']);half=unit/2;lo,hi=value-half,value+half
        lines=[r'\text{Half rounding step}='+frac(n(unit),2)+f'={n(half)}',r'\text{Lower bound}='+f'{n(value)}-{n(half)}={n(lo)}',r'\text{Upper bound}='+f'{n(value)}+{n(half)}={n(hi)}']
        if task=='bounds_inequality':
            letter=re.search(r'<=\s*([a-z])\s*<',m['answer'])[1];lines.append(interval(letter,value,unit))
            names=f'${letter}$ is the actual measurement named in the question. '
        else:names='The actual measurement is the quantity named in the question. '
        explanation=names+f'Its reported value is ${n(value)}$, rounded in steps of ${n(unit)}$. Half a step is ${n(half)}$, so subtract and add that amount to find the interval. '+endpoint
    elif task in ('max_area','min_area','max_perimeter','min_perimeter'):
        a,b,u=F(m['a']),F(m['b']),F(m['unit']);upper=task.startswith('max');A=a+(u/2 if upper else -u/2);B=b+(u/2 if upper else -u/2)
        area=task.endswith('area');label='Upper' if upper else 'Lower';quantity='area' if area else 'perimeter'
        lines=[interval('l',a,u),interval('w',b,u)]
        expression=f'{n(A)}\\times{n(B)}' if area else f'2({n(A)}+{n(B)})'
        lines.append(r'\text{'+label+' bound of '+quantity+'}='+expression)
        explanation=f'$l$ is the actual length and $w$ the actual width, reported as ${n(a)}$ and ${n(b)}$ in the units given. Each rounding step is ${n(u)}$, so its half-step is ${n(u/2)}$. '+('Area is $lw$; both positive dimensions increase the area.' if area else 'Perimeter is $2(l+w)$; both dimensions increase the perimeter.')+f' Use both {label.lower()} dimension bounds, ${n(A)}$ and ${n(B)}$, for the requested {label.lower()} bound. '+endpoint+' Keep square units for area and length units for perimeter.'
    elif task in ('min_sum','max_sum','min_diff','max_diff'):
        x,y=F(m['x']),F(m['y']);h=F('0.05');upper=task.startswith('max');diff=task.endswith('diff')
        X=x+(h if upper else -h);Y=y+(-h if upper else h) if diff else y+(h if upper else -h)
        op='-' if diff else '+';label='Upper' if upper else 'Lower'
        lines=[interval('x',x,F('0.1')),interval('y',y,F('0.1')),r'\text{'+label+' bound}='+f'{n(X)}{op}{n(Y)}']
        explanation=f'$x$ and $y$ are the actual measurements, reported as ${n(x)}$ and ${n(y)}$ to one decimal place. Their half rounding step is $0.05$. '+('A sum increases when either input increases, so use both upper bounds for an upper result and both lower bounds for a lower result.' if not diff else 'For $x-y$, increasing $x$ raises the result but increasing $y$ lowers it. A lower result needs lower $x$ and upper $y$; an upper result needs upper $x$ and lower $y$.')+f' Here use ${n(X)}$ and ${n(Y)}$ in that order. '+endpoint
    elif task=='speed_max':
        d,t=F(m['distance']),F(m['time']);D=d+F('0.5');T=t-F('0.05')
        lines=[interval('d',d,1),interval('t',t,F('0.1')),r'\text{Upper speed bound}='+frac(n(D),n(T))]
        explanation=f'$d$ is actual distance in kilometres, reported as ${n(d)}$ to the nearest kilometre; $t$ is actual time in hours, reported as ${n(t)}$ to one decimal place. Speed is $d/t$. To make this quotient as large as possible, use upper distance ${n(D)}$ and lower positive time ${n(T)}$. Do not use both upper bounds. Calculate before rounding the requested result to three significant figures. '+endpoint
    elif task=='triangle_min_area':
        a,b=F(m['a']),F(m['b']);A,B=a-F('0.05'),b-F('0.05')
        lines=[interval('a',a,F('0.1')),interval('b',b,F('0.1')),r'\text{Lower area bound}='+frac(f'{n(A)}\\times{n(B)}',2)]
        explanation=f'$a$ and $b$ are the perpendicular side lengths in centimetres, reported as ${n(a)}$ and ${n(b)}$. Each lower bound subtracts $0.05$ because measurements are to one decimal place. Use both lower positive sides in area $ab/2$, giving an area in square centimetres. The factor $1/2$ is needed for a triangle.'
    elif task=='cuboid_min_volume':
        values=[F(m[k]) for k in ('a','b','c')];lower=[v-F('0.05') for v in values]
        lines=[interval(letter,v,F('0.1')) for letter,v in zip(('a','b','c'),values)]
        lines.append(r'\text{Lower volume bound}='+r'\times'.join(n(v) for v in lower))
        explanation='$a$, $b$ and $c$ name the cuboid’s three actual side lengths in centimetres, reported as '+', '.join(f'${n(v)}$' for v in values)+'. Subtract $0.05$ from each to get its lower bound. All lengths are positive, so their product is smallest using all three lower bounds. Volume uses cubic centimetres; do not add the lengths.'
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation
