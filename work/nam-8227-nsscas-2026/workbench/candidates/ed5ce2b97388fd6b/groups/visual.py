"""Purpose-built 8227 visual group, native version 0.1.4.

Pure deterministic construction from the owner-approved finite domains. No attempt
recognition is implied: criteria describe evidence for the app's trusted marker.
"""
from decimal import Decimal, localcontext, ROUND_HALF_UP
from fractions import Fraction
from html import escape
from itertools import product
import json
import math

RECIPES = ['WB8227-modulus-graph-recovery', 'WB8227-trapezium-sketch-estimate', 'WB8227-vector-geometry']
_BRANCHES = ['vertex-intercepts', 'logarithmic-hence-chain', 'scalar-combination-and-origin-angle']


def _key(values):
    return json.dumps(values, separators=(',', ':'), ensure_ascii=False)


def choices():
    signs = (-3, -2, -1, 1, 2, 3)
    modulus = [dict(a=a, b=b, d=d) for a,b,d in product(signs, signs, (1,2,3))
               if d != 1 and abs(b) != 1 and b != a*(abs(b)-d) and (a,b,d) != (-2,-3,1)]
    vector = [dict(r=r,s=s,t=t) for r,s,t in product((1,2,3),signs,(1,2,3))
              if r != t and s+t-1 != 0 and 3-s+r*t-t != 0]
    trap = [dict(h=h,L=L,n=n,k=k) for h,L,n,k in product((1,3),(4,8),(2,4),(1,2,3))
            if (L,n,k) != (4,4,2)]
    rows = []
    for rid, branch, params, fresh in zip(RECIPES,_BRANCHES,(modulus,trap,vector),(44,2,17)):
        rows.append({'recipe_id':rid, 'branch_id':branch,
                     'selection_id':f'8227:D:SEL:{rid[7:]}:{branch}',
                     'parameters':params, 'raw_capacity':len(params),
                     'strict_complete_fresh_bound':fresh,
                     'exposure_key_policy':'All assessed part keys must be unseen for wholly fresh delivery; version is provenance, never a reset.',
                     'exhaustion':'Return exhausted when any required part key is already exposed; repeated practice needs an explicit after-feedback label.'})
    return rows


def _step(action,reason,result):
    return {'action':action,'reason':reason,'result':result}


def _criterion(rid, local, suffix, kind, text, **extra):
    return {'criterion_id':f'{rid}:{local}:{suffix}','mark_type':kind,'marks':1,
            'achievement':text, **extra}


def _frac(value):
    f = Fraction(value)
    if f.denominator == 1:
        return str(f.numerator)
    prefix = '-' if f < 0 else ''
    return prefix + r'\frac{' + str(abs(f.numerator)) + '}{' + str(f.denominator) + '}'


def _signed(v):
    return '+'+str(v) if v >= 0 else str(v)


def _sf(value, figures=3):
    with localcontext() as ctx:
        ctx.prec=65
        x=Decimal(value)
        if not x:
            return '0'
        unit=Decimal(1).scaleb(x.adjusted()-figures+1)
        return format(x.quantize(unit, rounding=ROUND_HALF_UP),'f')


def _svg(title,body,width=760,height=450):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title,quote=True)}">'
            f'<title>{escape(title)}</title><rect width="100%" height="100%" fill="white"/>'
            '<g font-family="Arial, sans-serif" font-size="15" fill="#17212b">'+body+'</g></svg>')


def _line(x1,y1,x2,y2,colour='#667085',extra=''):
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{colour}" stroke-width="1.5" {extra}/>'


def _text(x,y,text,extra=''):
    return f'<text x="{x:.2f}" y="{y:.2f}" {extra}>{escape(str(text))}</text>'


def _modulus_svg(a,b,d):
    c=-a*d
    pts=[('V',-b,c),('L',-b-d,0),('R',-b+d,0),('Y',0,a*abs(b)+c)]
    xmin=min(x for _,x,_ in pts)-2; xmax=max(x for _,x,_ in pts)+2
    ymin=min(0,c)-max(2,abs(a)*1.5); ymax=max(0,c,a*abs(b)+c)+max(2,abs(a)*1.5)
    # Equal coordinate units; diagram labels use names plus a coordinate key to
    # avoid unsafe overlapping numeric labels in the crowded/origin fixtures.
    scale=min(450/(xmax-xmin),300/(ymax-ymin))
    ox=55+(450-(xmax-xmin)*scale)/2
    oy=55+(300-(ymax-ymin)*scale)/2
    X=lambda x:ox+(x-xmin)*scale
    Y=lambda y:oy+(ymax-y)*scale
    body=_text(30,30,'Labelled modulus graph')
    body+=_line(X(xmin),Y(0),X(xmax),Y(0),'#17212b')+_line(X(0),Y(ymin),X(0),Y(ymax),'#17212b')
    body+=_text(X(xmax)+6,Y(0)+4,'x')+_text(X(0)+8,Y(ymax)-8,'y')
    # Draw just the portion in the graph window, so steep arms never escape.
    candidates=[(xmin,a*abs(xmin+b)+c),(-b,c),(xmax,a*abs(xmax+b)+c)]
    # Clip visually through a named plot clipping path, not by changing values.
    body+='<defs><clipPath id="plot"><rect x="48" y="45" width="470" height="325"/></clipPath></defs>'
    path=' '.join(('M' if i==0 else 'L')+f'{X(x):.3f},{Y(y):.3f}' for i,(x,y) in enumerate(candidates))
    body+=f'<path d="{path}" fill="none" stroke="#1565c0" stroke-width="3" clip-path="url(#plot)"/>'
    body+=_text(545,70,'Exact coordinates')
    seen={}
    for i,(name,x,y) in enumerate(pts):
        seen.setdefault((x,y),[]).append(name)
        body+=_text(545,110+44*i,f'{name}: ({x}, {y})')
    for (x,y),names in seen.items():
        body+=f'<circle cx="{X(x):.3f}" cy="{Y(y):.3f}" r="4.5" fill="#17212b"/>'
        # Vertices label towards the outside of the V; intercepts below axis.
        dy=(-13 if a<0 else 22) if 'V' in names else 24
        dx=8 if x>=0 else -10
        anchor='start' if dx>0 else 'end'
        body+=_text(X(x)+dx,Y(y)+dy,'/'.join(names),f'text-anchor="{anchor}"')
    body+=_text(30,414,'V is the vertex. L and R are x-intercepts. Y is the y-intercept.')
    body+=_text(30,438,'Use the exact labelled coordinates; screen measurement is unnecessary.')
    return _svg('Modulus graph with exact labelled vertex and intercepts',body)


def _modulus(p):
    rid=RECIPES[0]; a,b,d=(p[k] for k in ('a','b','d')); c=-a*d; y0=a*abs(b)+c
    givens=f'Vertex $V=({-b},{c})$; zeros $L=({-b-d},0)$ and $R=({-b+d},0)$; $y$-intercept $Y=(0,{y0})$.'
    formula=rf'y={a}\lvert x{_signed(b)}\rvert{_signed(c)}'
    return {'stem':r'The labelled graph has the form $y=a\lvert x+b\rvert+c$.'+'\n\n'+givens,
      'parts':[{'local_part_id':'a','prompt':'Determine $a$, $b$ and $c$. Give named values or the complete formula.',
        'reference_answer':f'$a={a}$, $b={b}$ and $c={c}$; equivalently ${formula}$.',
        'worked_steps':[
          _step('Read the vertex.',r'The vertex of $y=a\lvert x+b\rvert+c$ is $(-b,c)$.',f'$b={b}$ and $c={c}$.'),
          _step('Substitute the right-hand zero.','At this labelled zero, the modulus argument has absolute value '+f'${d}$.',rf'$0={d}a{_signed(c)}$, so $a={a}$.'),
          _step('Check the other intercept and orientation.','Every supplied point must belong to the same graph.',rf'$a\lvert b\rvert+c={y0}$, agreeing with $Y$; '+('the graph opens upwards.' if a>0 else 'the graph opens downwards.'))],
        'criteria':[_criterion(rid,'a',f'B{i}','B',f'Correct named {name}={value}, or that value unambiguously in its formula position, without wrong working for it.',qualifiers=['www'],answer_only_allowed=True) for i,(name,value) in enumerate((('a',a),('b',b),('c',c)),1)]}],
      'assets':[{'asset_id':'given-modulus','role':'question','part_id':'a','svg':_modulus_svg(a,b,d),'alt':givens.replace('$',''),
                 'must_read_givens':['vertex and both zeros','y-intercept','axis directions','V orientation','plus sign in x+b'],
                 'diagram_parameters':{'fixed':['Cartesian axes','straight arms','one vertex'], 'variable':['vertex','intercepts','orientation','window'], 'relations':['c=-a*d','left slope=-a','right slope=a','symmetry x=-b']}}],
      'practice_help':{'title':'Read a modulus graph','prompts':['How does the vertex locate the horizontal and vertical shifts?','Which labelled point could you substitute to find the vertical scale?','Does the sign of your scale agree with the way the V opens?']},
      'exposure_keys':[_key(['modulus-model',a,b,d])],
      'part_exposure_keys':{'a':_key(['modulus-model',a,b,d])},
      'private_math':{'coefficients':{'a':a,'b':b,'c':c},'given_points':{'V':[-b,c],'L':[-b-d,0],'R':[-b+d,0],'Y':[0,y0]},'full_model':formula}}


def _axes_svg(h,L,solution=False,n=2):
    width=760; height=450
    xmin=-.75; xmax=h+L+3; ymin=-3; ymax=max(3.2,math.log(L+2)+.7)
    X=lambda x:55+(x-xmin)*640/(xmax-xmin)
    Y=lambda y:365-(y-ymin)*305/(ymax-ymin)
    body=_text(25,28,'Sketch frame' if not solution else 'Logarithmic curve and trapezium top chords')
    body+=_line(X(xmin),Y(0),X(xmax),Y(0),'#17212b')+_line(X(0),Y(ymin),X(0),Y(ymax),'#17212b')
    body+=_text(X(xmax)+10,Y(0)+4,'x')+_text(X(0)+8,Y(ymax)-12,'y')+_text(X(0)-18,Y(0)+20,'0')
    if solution:
        body+=_line(X(h),Y(ymin),X(h),Y(ymax),'#d05030','stroke-dasharray="7 5"')
        body+=_text(X(h)+8,Y(ymax)+18,f'x = {h}')
        vals=[h+math.exp(ymin+(ymax-ymin)*i/240) for i in range(241)]
        vals=[x for x in vals if x<=xmax]
        path=' '.join(('M' if i==0 else 'L')+f'{X(x):.3f},{Y(math.log(x-h)):.3f}' for i,x in enumerate(vals))
        body+=f'<path d="{path}" fill="none" stroke="#1565c0" stroke-width="3"/>'
        body+=f'<circle cx="{X(h+1):.3f}" cy="{Y(0):.3f}" r="4"/>'+_text(X(h+1)+6,Y(0)+22,f'({h+1}, 0)')
        dx=L/n
        for j in range(n):
            x0=h+1+j*dx; x1=x0+dx; y0=math.log(x0-h); y1=math.log(x1-h)
            body+=_line(X(x0),Y(y0),X(x1),Y(y1),'#16835c')
            body+=_line(X(x1),Y(0),X(x1),Y(y1),'#9bbcae')
        body+=_text(X(h+1+L),Y(0)+24,str(h+1+L),'text-anchor="middle"')
        body+=_text(25,414,'The curve is concave down; the straight top chords lie below it.')
        body+=_text(25,438,'The function continues to rise; it has no finite horizontal asymptote.')
    else:
        body+=_text(25,414,'Draw your curve, and label its axis intersections and any vertical asymptote.')
    return _svg('Blank axes for a learner sketch' if not solution else 'Logarithmic sketch solution with asymptote, intercept and trapezium chords',body,width,height)


def _trapezium(p):
    rid=RECIPES[1]; h,L,n,k=(p[x] for x in ('h','L','n','k')); lo=h+1; hi=lo+L
    with localcontext() as ctx:
        ctx.prec=65
        delta=Decimal(L)/n
        ordinates=[(Decimal(1)+j*delta).ln() for j in range(n+1)]
        estimate=delta/2*(ordinates[0]+2*sum(ordinates[1:-1])+ordinates[-1])
        scaled=2*k*estimate
        actual=(Decimal(L+1)*(Decimal(L+1).ln())-Decimal(L))
        estimate_s=_sf(estimate); scaled_s=_sf(scaled)
    square=rf'x^2-{2*h}x+{h*h}'
    parts=[
      {'local_part_id':'a','prompt':rf'Use {n} equal trapeziums to estimate $I=\int_{{{lo}}}^{{{hi}}}\ln(x-{h})\,dx$. Give your answer to 3 significant figures.',
       'reference_answer':f'$I \\approx {estimate_s}$.',
       'worked_steps':[
        _step('Find the width and ordinates.','Equal strips have width equal to the interval length divided by the strip count.',rf'$\Delta x={L}/{n}={delta}$; '+', '.join(rf'$y_{{{j}}}=\ln({1+j*delta})$' for j in range(n+1))+'.'),
        _step('Apply the trapezium weights.','Each interior ordinate belongs to two neighbouring trapeziums.',rf'$T=\frac{{{delta}}}{{2}}\left(y_0+2\sum_{{j=1}}^{{{n-1}}}y_j+y_{{{n}}}\right)={str(estimate)[:18]}\ldots$.'),
        _step('Round only the reported result.','Guard digits avoid premature-rounding error.',f'$I \\approx {estimate_s}$ to 3 significant figures.')],
       'criteria':[_criterion(rid,'a','B1','B',f'Positive width {delta}, unsimplified or in the formula.'),_criterion(rid,'a','M1','M','Correct trapezium weighting or actual sum of trapezium areas using a positive width.'),_criterion(rid,'a','A1','A',f'Correct 3 significant figure result {estimate_s}, with the required valid method.',depends_on=[rid+':a:M1'])]},
      {'local_part_id':'b','prompt':rf'Hence, showing the transformation, estimate $J=\int_{{{lo}}}^{{{hi}}}{k}\ln({square})\,dx$. Give your answer to 3 significant figures.',
       'reference_answer':f'$J \\approx {scaled_s}$ using guard digits from (a). Correct 3-significant-figure products of a coherently used own (a) estimate are followed through.',
       'worked_steps':[
        _step('Recognise the square.','The expanded quadratic is a perfect square.',rf'${square}=(x-{h})^2$.'),
        _step('Use the logarithm power rule.','Throughout the integration interval, '+rf'$x-{h}>0$.',rf'${k}\ln((x-{h})^2)={2*k}\ln(x-{h})$.'),
        _step('Scale the previous estimate.','The same bounds are used, so the factor multiplies the whole estimate.',rf'$J\approx {2*k}T={str(scaled)[:18]}\ldots\approx {scaled_s}$ (3 significant figures).')],
       'criteria':[_criterion(rid,'b','B1','B',rf'Factorised form ${k}\ln((x-{h})^2)$ alone, the correct ${2*k}\ln(x-{h})$, or a correctly derived {2*k} scale; the direct expression implies the square.'),
                   _criterion(rid,'b','B2','B',f'Correct visible {2*k} times the learner own (a) estimate, with no visibly wrong log-law reasoning; exact product or any rendering correct to at least 3 significant figures.',qualifiers=['FT','www'],follow_through_from=['a'],alternatives=[{'exclusive_cap':1,'description':'Correct visible non-hence method; maximum with main route, never additive.'}])]},
      {'local_part_id':'c','prompt':rf'Sketch $y=\ln(x-{h})$, labelling axis intersections and any vertical asymptote.',
       'reference_answer':rf'One log branch for $x>{h}$, tending downwards as $x\to {h}^+$, increasing with decreasing gradient; vertical asymptote $x={h}$ and labelled intercept $({h+1},0)$; no $y$-intercept or finite horizontal asymptote.',
       'worked_steps':[
        _step('Set the logarithm argument positive.','A real logarithm needs a positive argument.',rf'$x>{h}$; the approached vertical boundary is $x={h}$.'),
        _step('Locate the axis intersection.','The logarithm equals zero when its argument is one.',rf'$x-{h}=1$, so the intercept is $({h+1},0)$; $x=0$ is outside the domain.'),
        _step('Draw the translated logarithm branch.','Translation preserves its increasing, concave-down shape.',rf'The curve lies to the right of $x={h}$, falls without bound near that line, and rises without a finite horizontal asymptote.')],
       'criteria':[_criterion(rid,'c','B1','B','Single log-shaped function graph relative to its approached boundary: right-hand branch, downwards approach without crossing/touching, rising through below/above-axis regions with decreasing gradient and no finite horizontal asymptote.',feature_based=True,multiple_function_graphs='B0'),
                   _criterion(rid,'c','B2','B',f'Correct asymptote x={h} identified on the sketch by a labelled guide or clearly labelled approached boundary; detached text is insufficient.',feature_based=True),
                   _criterion(rid,'c','B3','B',f'Correct intercept ({h+1},0), labelled on the sketch.',feature_based=True)]},
      {'local_part_id':'d','prompt':'Use your sketch to state, with a reason about the trapeziums and the curve, whether your answer to part (a) is an overestimate or an underestimate.',
       'reference_answer':'Underestimate: the curve is concave down on the interval, so the top chords of the trapeziums lie below the curve. For a clearly different own curve, apply the stated own-graph follow-through rules.',
       'worked_steps':[
        _step('Compare each top chord with the curve.','The logarithm has decreasing gradient on the integration interval.','Each straight top chord lies below the concave-down curve.'),
        _step('Relate the areas.','The trapezium tops lie below the graph on the same positive interval.','The estimated area is smaller than the area under the curve, so it is an underestimate.')],
       'criteria':[_criterion(rid,'d','B1','B','Bias conclusion supported by the learner own sketch on (a) interval; concave-up own curve supports over, concave-down supports under. Absent sketch earns no credit; unreadable evidence is pending.',qualifiers=['FT'],follow_through_from=['c']),
                   _criterion(rid,'d','DB1','DB','Correct top-chord/trapezium position relative to the same own curve; verbal geometric reason or correct overlay with a brief referring statement. Increasing alone is insufficient.',depends_on=[rid+':d:B1'],follow_through_from=['c'],authority='OD-5 own-curve dependent-reason extension')]}]
    keys={'a':['trapezium-quadrature',L,n],'b':['trapezium-hence',L,n,k],'c':['log-sketch',h],'d':['own-log-chord-context',h,L,n]}
    return {'stem':rf'Consider $f(x)=\ln(x-{h})$ on its real domain. Show your working for the numerical estimates.',
      'parts':parts,'assets':[
       {'asset_id':'sketch-frame','role':'question','part_id':'c','svg':_axes_svg(h,L),'alt':'Blank Cartesian axes for your sketch; no function curve is supplied.','must_read_givens':['x-axis','y-axis']},
       {'asset_id':'log-solution','role':'solution','part_id':'c','svg':_axes_svg(h,L,True,n),'alt':f'Logarithmic branch right of x={h}, intercept ({h+1},0), with top chords below the curve.','must_read_givens':['asymptote','intercept','domain side','integration interval','strip count','curve/chord relation'],
        'diagram_parameters':{'fixed':['one increasing concave-down logarithmic branch'], 'variable':['shift h','interval L','strip count n'], 'relations':['x>h','asymptote x=h','intercept (h+1,0)','chords below curve']}}],
      'practice_help':{'title':'Connect an estimate and its graph','prompts':['How do the first, interior and last ordinates enter the trapezium rule?','Can you recognise a square in the second integrand?','What do a curve and its top chords tell you about an area estimate?']},
      'exposure_keys':[_key(v) for v in keys.values()],'part_exposure_keys':{q:_key(v) for q,v in keys.items()},
      'private_math':{'width':str(delta),'ordinates':[str(v) for v in ordinates],'trapezium':str(estimate),'a_3sf':estimate_s,'b_guard_3sf':scaled_s,'b_scale':2*k,'exact_integral':str(actual),'bias':'underestimate','strict_generated_fresh_bound':2,
       'original_subtask_guard':'h=2 is excluded from this generated pool. Explicit original/mixed route requires exact source wording and attribution, not implemented here.'}}


def _vector(p):
    rid=RECIPES[2]; r,s,t=(p[q] for q in ('r','s','t'))
    u=(1,r,1); v=(s,1,-1); w=(1,t,1)
    numerator=s+t-1; denominator=2+r*t; scalar=Fraction(numerator,denominator)
    dot=s+r-1; nu=r*r+2; nv=s*s+2
    theta=math.degrees(math.acos(dot/math.sqrt(nu*nv)))
    angle=str(90 if dot==0 else 60) if dot==0 or (dot>0 and 4*dot*dot==nu*nv) else format(Decimal(str(theta)).quantize(Decimal('.1'),rounding=ROUND_HALF_UP),'f')
    col=lambda vv:r'\begin{pmatrix}'+r' \\ '.join(str(q) for q in vv)+r'\end{pmatrix}'
    return {'stem':rf'The position vectors of $A$, $B$ and $C$ from $O$ are $\overrightarrow{{OA}}={col(u)}$, $\overrightarrow{{OB}}={col(v)}$ and $\overrightarrow{{OC}}={col(w)}$.',
      'parts':[
       {'local_part_id':'a','prompt':r'Find $p$ such that $p\overrightarrow{OA}-\overrightarrow{OB}$ is perpendicular to $\overrightarrow{OC}$. If not written exactly, give $p$ to 3 significant figures.',
        'reference_answer':rf'$p={_frac(scalar)}$.',
        'worked_steps':[
         _step('Scale the first vector, then subtract the second.','The scalar multiplies only $\\overrightarrow{OA}$.',rf'$p\overrightarrow{{OA}}-\overrightarrow{{OB}}=\begin{{pmatrix}}p{_signed(-s)}\\{r}p-1\\p+1\end{{pmatrix}}$.'),
         _step('Set the scalar product with the third vector to zero.','Perpendicular vectors have zero scalar product.',rf'$(p{_signed(-s)})+{t}({r}p-1)+(p+1)=0$.'),
         _step('Solve the linear equation.','Collect the terms in $p$ and divide by its nonzero coefficient.',rf'${denominator}p={numerator}$, so $p={_frac(scalar)}$.')],
        'criteria':[_criterion(rid,'a','B1','B','Correct distributed scaling and subtraction, combined resultant, or equivalent correct scalar-product expansion; undistributed prompt restatement alone is insufficient.'),_criterion(rid,'a','M1','M','Calculate a scalar product with OC and equate to zero; a coherent attempted resultant may retain this method mark.'),_criterion(rid,'a','A1','A',rf'Correct $p={_frac(scalar)}$ or 3-significant-figure decimal, with valid specified-resultant working.',depends_on=[rid+':a:M1'],valid_resultant_required=True)]},
       {'local_part_id':'b','prompt':r'Use a scalar product to find angle $AOB$ in degrees, to 1 decimal place unless exact.',
        'reference_answer':rf'$\angle AOB={angle}^\circ$.',
        'worked_steps':[
         _step('Find the scalar product of the two rays from the origin.','Both position vectors start at the angle vertex $O$.',rf'$\overrightarrow{{OA}}\cdot\overrightarrow{{OB}}={s}+{r}-1={dot}$.'),
         _step('Find the two magnitudes.','The magnitude is the square root of the sum of squared components.',rf'$|\overrightarrow{{OA}}|=\sqrt{{{nu}}}$ and $|\overrightarrow{{OB}}|=\sqrt{{{nv}}}$.'),
         _step('Use the scalar-product angle formula.','Divide the dot product by the product of the magnitudes, retaining guard digits.',r'$\cos\theta=\frac{'+str(dot)+r'}{\sqrt{'+str(nu)+r'}\sqrt{'+str(nv)+r'}}$.'),
         _step('Evaluate and report the origin angle.','Use degree mode and the requested final accuracy.',rf'$\theta={angle}^\circ$.')],
        'criteria':[_criterion(rid,'b','B1','B',f'Correct dot product {dot}, or its negation explicitly identified as AO dot OB.',alternatives=['Reversed ray with supplementary-angle correction.']),_criterion(rid,'b','M1','M',f'One or both magnitudes correct: sqrt({nu}) and sqrt({nv}).'),_criterion(rid,'b','M2','M','Correct scalar-product angle relation using coherent own dot and magnitudes.',qualifiers=['FT'],follow_through_from=['b']),_criterion(rid,'b','A1','A',f'Correct requested angle {angle} degrees, with scalar-product method and exact 60/90 or correctly rounded 1-decimal-place form. Preserve a trailing zero for nonexact integer-rounded angles.',depends_on=[rid+':b:M2'],more_precise_answer_policy='Carry: acceptance of more precise final form awaits F/app decision; do not silently reject or award.')]}],
      'assets':[],'practice_help':{'title':'Use the vector directions','prompts':['Which vector does the scalar multiply?','What scalar-product equation expresses perpendicularity?','Do both rays in your angle calculation begin at O?']},
      'exposure_keys':[_key(['vector-perpendicular',r,s,t]),_key(['vector-angle',r,s])],
      'part_exposure_keys':{'a':_key(['vector-perpendicular',r,s,t]),'b':_key(['vector-angle',r,s])},
      'private_math':{'vectors':{'OA':list(u),'OB':list(v),'OC':list(w)},'p_fraction':str(scalar),'dot':dot,'norm_squares':[nu,nv],'angle_degrees':str(theta),'angle_display':angle}}


def build(recipe_id,branch_id,parameters):
    rows=[r for r in choices() if r['recipe_id']==recipe_id and r['branch_id']==branch_id]
    if (len(rows)!=1 or not isinstance(parameters,dict)
            or any(type(value) is not int for value in parameters.values())
            or parameters not in rows[0]['parameters']):
        raise ValueError('Unreviewed recipe, branch or parameters; no domain expansion is allowed.')
    return (_modulus if recipe_id==RECIPES[0] else _trapezium if recipe_id==RECIPES[1] else _vector)(dict(parameters))
