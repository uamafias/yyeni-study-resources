"""Explicit renewable demands closing the independent R6 scope findings."""
from copy import deepcopy
from fractions import Fraction as F
import math
from .core import question,part,step,fmt,polynomial
from .diagrams import spec,line,text,polyline,asset


def build_general_intersecting_lines(seed,rng,requested_key=None):
    theta=math.radians(rng.choice((40,50,60,70,80,100,110,120,130,140)))
    rotation=math.radians(rng.choice((10,20,30,40)))
    O=(90,85);radius=rng.randint(20,28)
    direction=lambda angle:(math.cos(angle),math.sin(angle))
    point=lambda angle,length:(O[0]+length*math.cos(angle),O[1]+length*math.sin(angle))
    u,v=point(rotation,radius),point(rotation+theta,radius)
    graph=spec(180,170,[line(point(rotation,-65),point(rotation,65)),line(point(rotation+theta,-65),point(rotation+theta,65)),text((O[0]+3,O[1]-5),'O'),text(point(rotation,68),'l'),text(point(rotation+theta,68),'m')])
    sol=deepcopy(graph)
    for angle in (rotation+theta/2,rotation+theta/2+math.pi/2):sol['commands'].append(line(point(angle,-65),point(angle,65),color='#006633'))
    # Compass marks: equal initial radii locate crossings on each ray. Equal
    # radii from those crossings intersect on each of the two angle bisectors.
    sol['commands'].append(polyline([point(rotation-.15+(theta+math.pi+.3)*i/160,radius) for i in range(161)],color='#888888'))
    for second in (v,point(rotation+theta+math.pi,radius)):
        crossing=(u[0]+second[0]-O[0],u[1]+second[1]-O[1])
        for centre in (u,second):
            angle=math.atan2(crossing[1]-centre[1],crossing[0]-centre[0])
            sol['commands'].append(polyline([(centre[0]+radius*math.cos(angle+d),centre[1]+radius*math.sin(angle+d)) for d in (-.18,-.12,-.06,0,.06,.12,.18)],color='#888888'))
    answer='Both complete angle bisectors of lines l and m, including the bisector of the adjacent angle, with compass arcs retained.'
    q=question('general-intersecting-line-loci',['5e.1'],'Angle-bisector loci','Two intersecting straight lines l and m are given. Use a straight edge and compasses only.',[
      part('Construct the complete locus of points equidistant from l and m. Keep all construction arcs.',answer,[
        step('Mark equal distances along the rays','One compass radius from O locates points equally far from the angle vertex.','Keep the compass radius fixed when crossing both rays.'),
        step('Construct the first angle bisector','Equal-radius arcs from the two ray crossings meet at a point equally inclined to both rays.','Join their intersection to O and extend the line in both directions.'),
        step('Construct the adjacent angle bisector','The full locus includes points in both pairs of opposite angles, not only the first angle.','Repeat using an opposite ray to construct the second, perpendicular bisector.')],3,[(1,'Correct equal-radius ray and intersection arcs for a valid bisector.'),(1,'One correct complete angle-bisector line.'),(1,'Both complete perpendicular angle-bisector lines and no extra locus.')]),
      part('Explain why both bisectors belong to the locus.','Distance is measured perpendicularly to each line; points on either angle bisector have equal perpendicular distances to l and m.',[step('Compare perpendicular distances','Distance to a straight line is the shortest, perpendicular distance.','Both the internal and external angle bisectors satisfy the same equality.')])],variant=seed,assets=[asset('general-bisectors',graph,sol)])
    q['structural_case']='general_intersecting_lines';q['parameter_evidence']={'angle_degrees':round(math.degrees(theta)),'rotation_degrees':round(math.degrees(rotation))}
    return [q]


def build_ratio_all_shares(seed,rng,requested_key=None):
    a,b,c=[rng.randint(2,9) for _ in range(3)];unit=rng.randint(12,40)
    if a==b:b+=1
    total=(a+b)*unit;total3=(a+b+c)*unit;difference=abs(a-b)*unit
    specs=[(f'Divide N${total} in the ratio {a}:{b}. Give both shares.',f'N${a*unit} and N${b*unit}.',total,a+b,[a,b]),
      (f'Divide {total3} litres among three tanks in the ratio {a}:{b}:{c}. Give all three amounts.',f'{a*unit}, {b*unit} and {c*unit} litres.',total3,a+b+c,[a,b,c])]
    ps=[]
    for prompt,answer,whole,parts,weights in specs:
        ps.append(part(prompt,answer,[step('Find one ratio part','The total is shared among the sum of the ratio parts.',rf'\frac{{{whole}}}{{{parts}}}={unit}'),step('Find every requested share','Multiply one part by each ratio number, and check that the shares sum to the total.','; '.join(f'{w}\\times{unit}={w*unit}' for w in weights))],2,[(1,'Correct unit share from the sum of ratio parts.'),(1,'All correct shares, with their units.')]))
    ps.append(part(f'Two lengths are in the ratio {a}:{b}. The first is {a*unit} cm. Find the second and their total length.',f'{b*unit} cm; total {total} cm.',[step('Recover the unit share','The first length contains the first ratio number of equal parts.',rf'\frac{{{a*unit}}}{{{a}}}={unit}'),step('Scale to the unknown amounts','The second length uses the second ratio number; the total uses the sum.',f'{b}\\times{unit}={b*unit}; ({a}+{b})\\times{unit}={total}')],2,[(1,'Correct unit share.'),(1,'Correct second length and total.')]))
    ps.append(part(f'Two masses are in the ratio {a}:{b} and differ by {difference} kg. Find both masses.',f'{a*unit} kg and {b*unit} kg.',[step('Relate the difference to ratio parts','The difference between the masses is the difference between their numbers of parts.',rf'\text{{One part}}=\frac{{{difference}}}{{{abs(a-b)}}}={unit}'),step('Calculate both masses','Use the same unit share for each side of the ratio.',f'{a}\\times{unit}={a*unit}; {b}\\times{unit}={b*unit}')],2,[(1,'Correct use of the difference of ratio parts.'),(1,'Both masses correct.')]))
    return [question('ratio-all-shares',['1j.2'],'Sharing in a ratio','Show your working.',ps,variant=seed)]


def build_monomial_products(seed,rng,requested_key=None):
    a,b,c,d=[rng.randint(2,8) for _ in range(4)]
    from services.math_generators.algebra_content import _sum
    specs=[(rf'{a}x({b}x^2-{c}x+{d})',polynomial([a*b,-a*c,a*d,0]),rf'{a*b}x^3-{a*c}x^2+{a*d}x'),
      (rf'-{a}y^2({b}y^3-{c}y+{d})',_sum((-a*b,'y^5'),(a*c,'y^3'),(-a*d,'y^2')),rf'-{a*b}y^5+{a*c}y^3-{a*d}y^2'),
      (rf'{a}xy({b}x^2-{c}y^2)',_sum((a*b,'x^3y'),(-a*c,'xy^3')),rf'{a*b}x^3y-{a*c}xy^3')]
    return [question('monomial-polynomial-products',['6b.1'],'Distributing a monomial','Expand each product and simplify.',[
      part('$'+expression+'$',answer,[step('Multiply the monomial by every term','The distributive law applies to every term, including its sign. Multiply coefficients and add powers of matching letters.',working),step('Check powers and signs','Only like terms can be collected; different monomials remain separate.',answer)],2,[(1,'Correct distribution to all polynomial terms.'),(1,'All signs, coefficients and powers correct.')]) for expression,answer,working in specs],variant=seed)]


def build_exponential_equation_forms(seed,rng,requested_key=None):
    b=rng.choice((2,3,5));u=rng.randint(2,5);v=rng.randint(-5,5);k=rng.randint(1,6);p=rng.randint(3,6);q=rng.randint(1,p-1);r=rng.randint(1,8)
    from .core import polynomial
    linear=polynomial([u,v])
    specs=[(rf'{b}^{{{linear}}}={b**k}',rf'{linear}={k}',F(k-v,u)),
      (rf'{b}^{{{linear}}}=\frac{{1}}{{{b**k}}}',rf'{linear}=-{k}',F(-k-v,u)),
      (rf'(\frac{{1}}{{{b}}})^{{{linear}}}={b**k}',rf'-({linear})={k}',F(-k-v,u)),
      (rf'{b**p}^x={b}^{{{polynomial([q,r])}}}',rf'{p}x={polynomial([q,r])}',F(r,p-q))]
    return [question('exponential-equation-forms',['6e.3'],'Solving with a common base','Solve each equation using the laws of indices.',[
      part('$'+expression+'$',f'x={fmt(answer)}',[step('Write both sides with the same base','Express the number or reciprocal as a power of the same positive base. Then equate exponents.',equation),step('Solve the linear exponent equation','Collect the x terms, then divide by the nonzero coefficient.',f'x={fmt(answer)}')],2,[(1,'Correct common-base equation in the exponents.'),(1,'Correct value of x.')]) for expression,equation,answer in specs],variant=seed)]

BUILDERS=[build_general_intersecting_lines,build_ratio_all_shares,build_monomial_products,build_exponential_equation_forms]
