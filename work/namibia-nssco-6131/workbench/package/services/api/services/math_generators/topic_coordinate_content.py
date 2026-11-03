"""Coordinate calculations: named points, signed differences and line equations."""
from .topic_teaching import *

LABELS={
'nssco_straight_line_graphs_gradients':{1:'Reading a gradient or intercept',2:'Gradient between points',3:'Rearranging a line equation',4:'Substituting a point into a line',5:'Finding both axis intercepts'},
'nssco_distance_midpoint_gradient':{1:'Finding a midpoint',2:'Distance using Pythagoras',3:'Gradient between points',4:'Exact surd distances and fractional midpoints',5:'Finding a missing endpoint or coordinate'},
'nssco_equations_of_straight_lines':{1:'Using a gradient and intercept or point',2:'Line through two points',3:'Finding a parallel line',4:'Finding a perpendicular line',5:'Finding line intersections'},
'nssco_parallel_perpendicular_quadrilaterals':{1:'Related gradients',2:'Finding a coefficient from related gradients',3:'Completing a parallelogram',4:'Rectangle area from coordinates',5:'Parallelogram area from coordinates'},
}


def slope_lines(a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]
    return [r'\Delta x='+f'({q(b[0])})-({q(a[0])})={q(dx)}',r'\Delta y='+f'({q(b[1])})-({q(a[1])})={q(dy)}','m='+frac(q(dy),q(dx))],F(dy)/dx


def line_work(m,pt):
    x,y=map(F,pt);c=y-m*x
    return [f'{q(y)}=({q(m)})({q(x)})+c',f'c=({q(y)})-({q(m)})({q(x)})={q(c)}',f'y={linear_latex(m,c)}']


def content(p):
    if p.generator_id not in LABELS:return None
    m=p.machine;t=m['task'];lines=[]
    if t in ('midpoint','midpoint_fraction'):
        a,b=m['p1'],m['p2'];lines=['x_M='+frac(f'({a[0]})+({b[0]})',2),'y_M='+frac(f'({a[1]})+({b[1]})',2)]
        e=f'The endpoints are ${point(a)}$ and ${point(b)}$. $M$ names their midpoint: average the two $x$-coordinates for $x_M$ and separately the two $y$-coordinates for $y_M$. Keep the horizontal/vertical order and retain exact halves when the midpoint is not integral.'
    elif t in ('distance_whole','distance_surd'):
        a,b=m['p1'],m['p2'];dx,dy=b[0]-a[0],b[1]-a[1]
        lines=[f'\\Delta x=({b[0]})-({a[0]})={dx}',f'\\Delta y=({b[1]})-({a[1]})={dy}','d=\\sqrt{(\\Delta x)^2+(\\Delta y)^2}'+f'=\\sqrt{{({dx})^2+({dy})^2}}=\\sqrt{{{dx*dx+dy*dy}}}']
        e=f'The endpoints are ${point(a)}$ and ${point(b)}$. Their horizontal and vertical changes are ${dx}$ and ${dy}$. These form perpendicular sides of a right triangle, so distance $d$ is the positive square root of the sum of their squares. '+('Extract the largest square factor and keep the requested exact surd form.' if t=='distance_surd' else 'A length is nonnegative even when a coordinate difference is negative.')
    elif t in ('gradient_two_points','gradient_between_points'):
        a,b=m['p1'],m['p2'];lines,_=slope_lines(a,b);e=f'The points are ${point(a)}$ and ${point(b)}$. Gradient $m$ is vertical change divided by horizontal change. Use second minus first for both differences; reversing just one changes the sign incorrectly. Simplify the quotient exactly.'
    elif t=='find_other_end':
        a,mid=m['p1'],m['mid'];lines=[f'x_B=2({mid[0]})-({a[0]})',f'y_B=2({mid[1]})-({a[1]})'];e=f'The known endpoint is A${point(a)}$ and midpoint M${point(mid)}$. Since $M=(A+B)/2$ coordinate by coordinate, solve for the missing endpoint using $B=2M-A$. Doubling the known endpoint instead would place the midpoint incorrectly.'
    elif t=='find_missing_coordinate_gradient':
        a=m['p1'];x=m['x2'];gradient=F(m['m'][0])/m['m'][1]
        lines=[f'\\Delta x={x}-({a[0]})={x-a[0]}',f'\\Delta y=({q(gradient)})({x-a[0]})',f'k={a[1]}+({q(gradient)})({x-a[0]})']
        e=f'The known point is ${point(a)}$, the other $x$-coordinate is ${x}$, and gradient $m={q(gradient)}$. Let $k$ name the unknown $y$-coordinate. Rearrange $m=\\Delta y/\\Delta x$ to get $\\Delta y=m\\Delta x$, then add that change to the first $y$-coordinate. Preserve signed differences.'
    elif t=='find_missing_coordinate_distance':
        a,x,L=m['p1'],m['x2'],m['length'];dx=x-a[0];square=L*L-dx*dx
        lines=[f'({dx})^2+(k-({a[1]}))^2={L}^2',f'(k-({a[1]}))^2={L}^2-({dx})^2={square}',f'k={a[1]}\\pm\\sqrt{{{square}}}']
        e=f'The known point is ${point(a)}$, the other point has $x={x}$ and unknown $y=k$, and their distance is ${L}$. Pythagoras determines the square of the vertical change after accounting for the horizontal change ${dx}$. Both signs of that vertical change can give the same length, so retain both values of $k$.'
    elif t in ('gradient_from_equation','intercept_from_equation','line_from_gradient_intercept'):
        gradient=F(m['m'][0])/m['m'][1] if isinstance(m['m'],(list,tuple)) else F(m['m']);c=m['c'];lines=[f'y={linear_latex(gradient,c)}']
        if t=='gradient_from_equation':lines.append('m='+q(gradient))
        elif t=='intercept_from_equation':lines.append(f'x=0,\\quad y={c}')
        e=f'Compare the given rule with $y=mx+c$. Here gradient $m={q(gradient)}$ is the signed coefficient of $x$ and $c={c}$ is the constant term. The $y$-intercept is $(0,{c})$. Reading terms in a different written order does not change their roles; retain the sign attached to the $x$ term.'
    elif t in ('gradient_general_form','intercept_general_form','axis_intercepts'):
        a,b,c=m['abc'];gradient=F(-a)/b;intercept=F(c)/b
        lines=[f'{a}x+({b})y={c}',f'y='+frac(f'{c}-({a})x',b),f'y={linear_latex(gradient,intercept)}']
        if t=='axis_intercepts':lines.extend(['y=0:\\quad x='+frac(c,a),'x=0:\\quad y='+frac(c,b)])
        e=f'The line is $ax+by=c$, with $a={a}$, $b={b}$ and $c={c}$. Divide every term by ${b}$ after moving the $x$ term: the gradient is ${q(gradient)}$ and $y$-intercept ${q(intercept)}$. '+('For the $x$-axis put $y=0$; for the $y$-axis put $x=0$. Give both coordinate pairs in the requested order.' if t=='axis_intercepts' else 'Use the requested coefficient or intercept point; the original coefficient of $x$ is not the gradient until $y$ is isolated.')
    elif t=='point_on_line_value':
        gradient=F(m['m'][0])/m['m'][1];x=m['h'];c=m['c'];lines=[f'y=({q(gradient)})({x})+({c})'];e=f'The line has gradient ${q(gradient)}$ and $y$-intercept ${c}$. The given point’s $x$-coordinate is ${x}$, so substitute it into $y=mx+c$ to find the missing $y$. Bracket the signed input before multiplying.'
    elif t in ('find_intercept_constant','line_from_gradient_point','line_through_two_points','parallel_line','perpendicular_line'):
        if t=='line_through_two_points':pt=m['p1'];lines,gradient=slope_lines(m['p1'],m['p2'])
        else:
            pt=m['point'];raw=m.get('perp',m['m']);gradient=F(raw[0])/raw[1] if isinstance(raw,(list,tuple)) else F(raw)
        lines+=line_work(gradient,pt)
        e=f'$m$ is the required line’s gradient and $c$ its unknown $y$-intercept. '+('Calculate $m$ from the two given points. ' if t=='line_through_two_points' else 'Parallel lines have the same gradient. ' if t=='parallel_line' else 'Perpendicular nonvertical lines have gradients whose product is $-1$, so use the negative reciprocal of the given gradient. ' if t=='perpendicular_line' else 'Use the supplied gradient. ')+f'Here $m={q(gradient)}$ and point ${point(pt)}$ lies on the required line. Substitute both coordinates into $y=mx+c$, solve for $c$, then write the full equation unless only $c$ was requested.'
    elif t in ('lines_meet','line_intersection'):
        if t=='line_intersection':
            a,b=m['A'],m['B'];lines,gradient=slope_lines(a,b);C=m['C'];constant=F(C[1])-gradient*C[0];lines+=line_work(gradient,C);second=m['line'];first=(gradient,constant)
        else:first,second=m['lines']
        a,b=map(F,first);c,d=map(F,second);x=(d-b)/(a-c);y=a*x+b
        lines.extend([f'{linear_latex(a,b)}={linear_latex(c,d)}',f'({q(a-c)})x={q(d-b)}','x='+frac(q(d-b),q(a-c))+f'={q(x)}',f'y=({q(a)})({q(x)})+({q(b)})={q(y)}'])
        e=f'At an intersection, both line equations have the same $x$ and the same $y$. Equate their expressions for $y$, solve for $x={q(x)}$, then substitute into either original line for $y={q(y)}$. '+('The required parallel line first uses AB’s gradient through point C. ' if t=='line_intersection' else '')+'Give the answer as the ordered pair $(x,y)$ and check it in both equations.'
    elif t=='parallel_perpendicular_gradient':
        given=F(m['m'][0])/m['m'][1];parallel=m['kind']=='parallel';answer=given if parallel else -1/given;lines=['m_1='+q(given),'m_2='+('m_1' if parallel else frac('-1','m_1'))+'='+q(answer)]
        e=f'The given gradient is $m_1={q(given)}$. '+('Parallel lines have $m_2=m_1$.' if parallel else 'Perpendicular nonvertical lines satisfy $m_1m_2=-1$, so $m_2=-1/m_1$.')+f' Here the requested gradient is ${q(answer)}$. The intercept does not affect the angle between the lines.'
    elif t in ('find_k_parallel','find_k_perpendicular'):
        given=F(m['m'][0])/m['m'][1];a=m['a'];e0=m['e'];parallel=t=='find_k_parallel'
        lines=[f'{a}x+ky={e0}', 'm_2='+frac(-a,'k')]
        if parallel:lines.extend([frac(-a,'k')+'='+q(given),'k='+frac(-a,q(given))])
        else:lines.extend([f'({q(given)})'+frac(-a,'k')+'=-1',f'k={q(a*given)}'])
        e=f'The first gradient is ${q(given)}$. In the second equation, $k$ is the coefficient of $y$, so making $y$ the subject gives gradient $\\frac{{{-a}}}{{k}}$. '+('Equate this to the first gradient because the lines are parallel.' if parallel else 'Set the product of the two gradients to $-1$ because the lines are perpendicular.')+' Solve the resulting equation for $k$; do not compare the original $x$ coefficients directly.'
    elif t=='parallelogram_fourth_vertex':
        a,b,c=m['vertices'];dx,dy=c[0]-b[0],c[1]-b[1];lines=[r'\overrightarrow{BC}=('+f'{c[0]}-({b[0]}),{c[1]}-({b[1]}))',f'D=({a[0]}+({dx}),{a[1]}+({dy}))']
        e=f'A, B and C are consecutive vertices ${point(a)}$, ${point(b)}$ and ${point(c)}$. Opposite sides have equal displacement: AD = BC. Find BC by C minus B, then add it to A to obtain D. The stated order of vertices matters.'
    elif t in ('rectangle_area','parallelogram_area'):
        a,b,c=m['vertices'];dx,dy=b[0]-a[0],b[1]-a[1];base2=dx*dx+dy*dy
        lines=[f'b=\\sqrt{{({dx})^2+({dy})^2}}=\\sqrt{{{base2}}}']
        if t=='rectangle_area':dx2,dy2=c[0]-b[0],c[1]-b[1];height2=dx2*dx2+dy2*dy2;lines.extend([f'h=\\sqrt{{({dx2})^2+({dy2})^2}}=\\sqrt{{{height2}}}','A=bh=\\sqrt{'+str(base2)+'}\\sqrt{'+str(height2)+'}']);e=f'The rectangle’s adjacent sides join P${point(a)}$ to Q${point(b)}$, then Q to R${point(c)}$. Find each side length with Pythagoras. These sides are perpendicular, so area $A$ is their product; retain exact surds until multiplying.'
        else:
            mid=[F(a[i]+b[i])/2 for i in (0,1)];dx2,dy2=F(c[0])-mid[0],F(c[1])-mid[1];height2=dx2*dx2+dy2*dy2
            lines.extend([f'M={point(mid)}',f'h=MD=\\sqrt{{({q(dx2)})^2+({q(dy2)})^2}}',f'A=bh=\\sqrt{{{base2}}}\\sqrt{{{q(height2)}}}'])
            e=f'AB is the base from ${point(a)}$ to ${point(b)}$ and D is ${point(c)}$. M is the midpoint of AB, here ${point(mid)}$. The question states MD is perpendicular to AB, so MD is the required height, unlike the sloping side AD. Find AB and MD by Pythagoras and multiply them for area $A$.'
    else:raise ValueError(t)
    return finish(p,lines,e)
