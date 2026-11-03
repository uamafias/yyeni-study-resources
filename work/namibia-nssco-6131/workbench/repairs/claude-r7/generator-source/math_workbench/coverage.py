"""Bounded repairs for the specific syllabus facets challenged in review."""
from fractions import Fraction
from copy import deepcopy
import math
from .core import question,part,step,calc,fmt,coordinates,polynomial
from .diagrams import cartesian,asset,circle,line,text,polyline,spec


def build_similarity_problems(seed,rng,requested_key=None):
    a,k=rng.randint(2,12),rng.randint(2,8)
    b=a
    angle=rng.randint(30,70)
    condition=['SSS','SAS','ASA','RHS'][seed%4]
    givens={
        'SSS':'AB = DE, BC = EF and AC = DF',
        'SAS':f'AB = DE, BC = EF and angle ABC = angle DEF = {angle}°',
        'ASA':f'angle BAC = angle EDF = {angle}°, angle ABC = angle DEF = 70°, and AB = DE',
        'RHS':'ABC and DEF are right-angled at B and E, AC = DF and AB = DE',
    }
    q=question('similarity-problems',['5a.4'],'Similar and congruent triangles',
        rf'Triangles PQR and XYZ have angle P = angle X = 30° and angle Q = angle Y = 90°. '
        rf'$PQ={a}\sqrt3$ cm, QR = {a} cm and $XY={k*a}\sqrt3$ cm.',[
        part('Explain why PQR and XYZ are similar, and find YZ.',f'AA similarity; YZ = {k*b} cm.',
            [step('Match two equal angles','Two corresponding angle pairs establish similarity, so all corresponding sides have one scale factor.',f'Scale factor XY/PQ = {k}; YZ = {b} × {k} = {k*b} cm.')],
            3,[(1,'AA similarity from the two stated equal angle pairs.'),(1,f'Corresponding length scale factor {k}.'),(1,f'YZ = {k*b} cm.')]),
        part(f'For triangles ABC and DEF, {givens[condition]}. Explain why they are congruent.',condition+' with the stated corresponding sides/angles.',
            [step('Check a sufficient congruence condition','The specified correspondence satisfies '+condition+'; similarity alone would not establish equal size.',condition)],2,
            [(1,'Correct sufficient congruence condition: '+condition+'.'),(1,'Correct correspondence and explanation from the givens.')])],variant=seed)
    q['structural_case']=condition
    return [q]


def build_set_builder_forms(seed,rng,requested_key=None):
    lo,hi=rng.randint(-6,0),rng.randint(2,8);m,c=rng.randint(2,6),rng.randint(-5,5)
    return [question('set-builder-forms',['2main.1'],'Describing sets',
        'Use set-builder notation. Equivalent exact descriptions are accepted.',[
        part(f'Write the set of real numbers from {lo} to {hi}, including both endpoints.',rf'\{{x\in\mathbb R:{lo}\le x\le{hi}\}}',
            [step('State the domain and both bounds','The word real allows every real value in the closed interval, not just integers.',rf'x\in\mathbb R,\quad {lo}\le x\le {hi}')]),
        part(f'Write the set of ordered pairs on the straight line y = {polynomial([m,c])}.',rf'\{{(x,y)\in\mathbb R^2:y={polynomial([m,c])}\}}',
            [step('Describe membership by the equation','Every ordered pair on the line satisfies its equation and every real pair satisfying it lies on the line.',rf'y={polynomial([m,c])}')]),
        part(f'List all integers in the real interval from {lo} to {hi}, inclusive.',r'\{'+','.join(map(str,range(lo,hi+1)))+r'\}',
            [step('Restrict the interval to integers','List each integer meeting both bounds exactly once.',', '.join(map(str,range(lo,hi+1))))])],variant=seed)]


def build_cartesian_coordinates(seed,rng,requested_key=None):
    sx,sy=[(-1,1),(1,1),(-1,-1),(1,-1),(0,1),(1,0)][seed%6]
    x,y=sx*rng.randint(1,4),sy*rng.randint(1,4);dx,dy=rng.choice((-2,-1,1,2)),rng.choice((-2,-1,1,2))
    graph,pt=cartesian(-7,7,-7,7,width=150,height=150)
    graph['commands'] += [circle(pt(x,y),.8,fill='black'),text(pt(x+.3,y+.3),'A')]
    solution=deepcopy(graph);solution['commands'] += [circle(pt(x+dx,y+dy),.8,fill='black'),text(pt(x+dx+.3,y+dy+.3),'B')]
    return [question('cartesian-coordinates',['7a.1'],'Cartesian coordinates','Use the coordinate grid.',[
        part('Write the coordinates of A.',coordinates([(x,y)]),[step('Read horizontal then vertical displacement','An ordered pair lists x before y, including the signs.',coordinates([(x,y)]))]),
        part(f'Plot and label B at ({x+dx}, {y+dy}).',coordinates([(x+dx,y+dy)],['B']),[step('Locate both signed coordinates','Move to the horizontal coordinate, then the vertical coordinate, and label the point.',coordinates([(x+dx,y+dy)],['B']))])],variant=seed,assets=[asset('coordinates',graph,solution)])]


def build_locus_constructions(seed,rng,requested_key=None):
    distance = rng.choice([2, 3])
    gap = rng.choice([40, 50, 60])
    cx = rng.randint(65, 90)
    ay, ly = 75, 50
    a, b = (cx-gap/2, ay), (cx+gap/2, ay)
    graph = spec(160, 130, [line((10,ly),(150,ly)),text((145,ly+3),'l'),
        circle(a,.8,fill='black'),circle(b,.8,fill='black'),
        text((a[0]-9,ay-9),'A'),text((b[0]+5,ay-9),'B')])
    sol = deepcopy(graph)
    for sign in (-1,1):
        y = ly + sign*distance*10
        sol['commands'] += [line((10,y),(150,y),color='#006633'),circle((cx,y),.8,fill='#006633')]
    sol['commands'].append(line((cx,10),(cx,120),color='#3333aa'))
    radius = .58*gap
    ih = math.sqrt(radius**2-(gap/2)**2)
    for centre in (a,b):
        for sign in (-1,1):
            angle=math.atan2(sign*ih,cx-centre[0])
            sol['commands'].append(polyline([(centre[0]+radius*math.cos(angle+d),ay+radius*math.sin(angle+d))
                for d in (-.12,-.08,-.04,0,.04,.08,.12)],color='#888888'))
    for sign in (-1,1):
        y=ly+sign*distance*10
        sol['commands'].append(line((10,y),(150,y),color='#006633',width=.45))
    return [question('locus-constructions',['5e.1'],'Constructing loci',
        'Use the actual-size printed diagram. Print the PDF at 100%. Points A and B and line l are given.',[
        part(f'Construct both loci at distance {distance} cm from line l.',
            f'Two lines parallel to l, one {distance} cm on each side.',
            [step('Mark equal perpendicular distances from l',
                'The distance from a line is measured perpendicular to it; both sides satisfy the condition.',
                f'The two parallel lines are {distance} cm from l.')],2,
            [(1,f'Parallel line {distance} cm above l (allow ±1 mm).'),
             (1,f'Parallel line {distance} cm below l (allow ±1 mm).')]),
        part('Using ruler and compasses, construct the locus equidistant from A and B. Leave construction arcs visible.',
            'The perpendicular bisector of AB, with equal-radius arcs above and below AB.',
            [step('Construct equal-radius arcs from A and B',
                'Their intersections are each equally distant from A and B; the line through them is the complete perpendicular bisector.',
                'Join the two arc intersections with a straight line.')],2,
            [(1,'Equal-radius arcs from both endpoints intersect above and below AB.'),
             (1,'Straight perpendicular bisector through the arc intersections (allow ±1 mm).')]),
        part('Mark all points satisfying both preceding conditions.',
            'The two intersections of the perpendicular bisector with the parallel loci.',
            [step('Intersect the loci',
                'A point satisfying both conditions must belong to both loci.',
                'Mark both intersections, one on each parallel line.')],2,
            [(1,'One correct intersection (allow ±1 mm from reference).'),
             (1,'The other correct intersection, with no additional points.')])],
        variant=seed,assets=[asset('loci',graph,sol,physical=True)])]


def build_angle_properties(seed,rng,requested_key=None):
    a=rng.randint(25,65);b=rng.randint(30,70);n=rng.randint(5,10)
    cases=[
      ('Angles of 90°, '+str(a)+'°, 80° and x surround a point.',190-a,'Angles at a point sum to 360°.'),
      (f'Two adjacent angles on a straight line are {a}° and x.',180-a,'Angles on a straight line sum to 180°.'),
      (f'Two straight lines intersect. One angle is {a}°; x is vertically opposite it.',a,'Vertically opposite angles are equal.'),
      (f'A transversal crosses parallel lines. An angle is {a}°; x is its alternate angle.',a,'Alternate angles between parallel lines are equal.'),
      (f'A triangle has angles {a}°, {b}° and x.',180-a-b,'The interior angles of a triangle sum to 180°.'),
      (f'A quadrilateral has angles {a}°, {b}°, 100° and x.',260-a-b,'The interior angles of a quadrilateral sum to 360°.'),
      (f'A regular polygon has {n} sides. Find its exterior angle x.',Fraction(360,n),'The exterior angles sum to 360° and are equal in a regular polygon.'),
      (f'An irregular pentagon has angles {a}°, 120°, 130°, 100° and x.',190-a,'The interior angle sum of a pentagon is (5−2) × 180°.'),
      ('AB is a diameter of a circle and C is another point on the circle. Find angle ACB = x.',90,'The angle subtended by a diameter at the circumference is 90°.'),
      ('A tangent touches a circle at T, whose centre is O. Find angle x between OT and the tangent.',90,'A tangent is perpendicular to the radius at its point of contact.'),
      (f'A chord subtends {a}° at the circumference. Find the angle x it subtends at the centre on the same arc.',2*a,'The central angle is twice the circumference angle subtended by the same arc.'),
      (f'Angles APB = {a}° and AQB = x stand on chord AB, with P and Q in the same segment.',a,'Angles subtended by the same chord in the same segment are equal.'),
      (f'ABCD is cyclic, with angle ABC = {b}° and opposite angle ADC = x.',180-b,'Opposite angles in a cyclic quadrilateral are supplementary.'),
    ]
    selected=[cases[seed%len(cases)],cases[(seed+6)%len(cases)]]
    q=question('angle-properties',['5d.1'],'Angles and geometric reasons','Find each angle x and give a geometrical reason. Give non-integer angles to 1 decimal place, or give an exact fraction.',[
        part(prompt,fmt(answer)+'°; '+reason,[step('Apply the angle relationship',reason,fmt(answer)+'°')],2,
             [(1,'Correct angle: '+fmt(answer)+'°'+(f' or {float(answer):.1f}°.' if isinstance(answer,Fraction) and answer.denominator!=1 else '.')),(1,'Correct geometrical reason: '+reason)]) for prompt,answer,reason in selected],variant=seed)
    q['structural_case']=[seed%len(cases),(seed+6)%len(cases)]
    return [q]


BUILDERS=[build_similarity_problems,build_set_builder_forms,build_cartesian_coordinates,build_locus_constructions,build_angle_properties]
