"""Seeded visual measurement, geometry, construction, locus and bearing tasks."""
import math
from .visual_common import *


def clock(g,r,s,l):
    hour=r.randint(1,12);minute=r.choice((0,5,10,15,20,25,30,35,40,45,50,55))
    els=[circle(0,0,5)]+[text(4.4*math.sin(math.radians(i*30)),4.4*math.cos(math.radians(i*30))-.12,i) for i in range(1,13)]
    for angle,length in ((minute*6,4),(hour*30+minute*.5,2.6)):
        els.append(line([(0,0),(length*math.sin(math.radians(angle)),length*math.cos(math.radians(angle)))]))
    els.append(point(0,0))
    return make(g,s,l,'read_clock','Read the clock. Write the time in 12-hour notation; am or pm is not required.',f'{hour}:{minute:02d}',spec((-6,6,-6,6),'Clock face',els),None,
        f'The longer minute hand indicates {minute} minutes. The shorter hour hand is at or after {hour}. Each numbered interval represents five minutes; the hour hand moves between numbers as the minutes pass.',
        [(1,f'Correct time {hour}:{minute:02d}, allowing equivalent 12-hour wording.')],['NSSCO-6131-2018-visual-p13-26'],{'hour':hour,'minute':minute},False)


def geometry(g,r,s,l):
    if l==1:
        angle=r.choice(tuple(a for a in range(15,346,5) if a not in (90,180,270)));reflex=angle>180
        a=math.radians(angle);els=[line([(4,0),(0,0),(4*math.cos(a),4*math.sin(a))]),arc(0,0,1,0,angle),text(1.5*math.cos(a/2),1.5*math.sin(a/2),'a')]
        name='reflex' if reflex else 'obtuse' if angle>90 else 'acute'
        return make(g,s,l,'angle_name','Name the marked angle a as acute, obtuse or reflex.',name,spec((-5,5,-5,5),'Angle a is indicated by the arc',els),None,
                    'Follow the marked arc, not automatically the smaller angle between the rays. Acute is less than 90°, obtuse is between 90° and 180°, and reflex is between 180° and 360°.',[(1,f'The marked angle is {name}.')],['NSSCO-6131-2018-visual-p13-26'],{'angle':angle},False)
    shape=r.choice(('cube','cuboid','triangular prism'));els=[]
    cells=[(0,0),(1,0),(2,0),(3,0),(1,1),(1,-1)]
    if shape=='triangular prism':
        for x,y in ((0,0),(1,0),(2,0)):els.append(closed([(x,y),(x+1,y),(x+1,y+2),(x,y+2)]))
        els += [closed([(0,0),(1,0),(.5,-.866)]),closed([(0,2),(1,2),(.5,2.866)])]
        bound=(-1,4,-2,4)
    else:
        a,b,c=(1,1,1) if shape=='cube' else (r.randint(3,6),r.randint(1,2),r.randint(3,8)/2)
        x=0
        for width in (a,b,a,b):
            els.append(closed([(x,0),(x+width,0),(x+width,c),(x,c)]));x+=width
        els += [closed([(0,c),(a,c),(a,c+b),(0,c+b)]),closed([(0,0),(a,0),(a,-b),(0,-b)])]
        bound=(-1,2*(a+b)+1,-b-1,c+b+1)
    return make(g,s,l,'recognise_net','Name the solid formed by folding this net. Dashed or shared edges represent folds.',shape,spec(bound,'Net of a solid',els),None,
        'Identify the faces and how they meet when folded. Six equal squares form a cube; rectangular faces can form a cuboid; two triangular ends and three rectangular lateral faces form a triangular prism.',[(1,f'Correct solid: {shape}.')],['NSSCO-6131-2018-visual-p13-26'],{'solid':shape},False)


def measurement(g,r,s,l):
    length=r.randint(8,24)/2;start=r.randint(0,2);angle=r.choice(tuple(range(20,161,5)))
    if l==1:
        els=[line([(start,0),(start+length,0)]),text(start,.4,'A'),text(start+length,.4,'B')]
        for x in range(15):els += [line([(x,-1),(x,-.7 if x%5==0 else -.85)],'gray'),text(x,-1.45,x)]
        return make(g,s,l,'measure_segment','Read the length AB in centimetres using the drawn ruler; do not measure your screen.',f'$AB={length}\\text{{ cm}}$',spec((-1,15,-2,2),'Segment and centimetre ruler',els),None,
            f'A aligns with {start} cm and B aligns with {start+length:g} cm, so subtract the ruler readings. A diagram drawn on a screen does not retain a physical centimetre scale.',[(1,f'Correct length {length} cm.')],['NSSCO-6131-2018-visual-p13-26'],{'length':length,'ruler_start':start,'ruler_end':start+length},False)
    # Draw an SSS triangle; numbers generated from a right triangle scaled by k.
    k=r.randint(5,35)/10;A=(0,0);B=(round(4*k,1),0);C=(0,round(3*k,1))
    blank=spec((-1,4*k+1,-1,3*k+1),'Sketch of the labelled base; reproduce it to the stated lengths',[line([A,B]),text(0,-.4,'A'),text(4*k,-.4,'B')])
    answer=spec(blank['bounds'],'Completed triangle with compass arcs',polygon_with_labels([A,B,C])+[arc(0,0,3*k,65,115,'gray',True),arc(4*k,0,5*k,130,160,'gray',True)])
    return make(g,s,l,'construct_triangle',f'Using a ruler and compasses, construct triangle ABC with $AB={4*k:g}$ cm, $AC={3*k:g}$ cm and $BC={5*k:g}$ cm. Leave construction arcs visible.',
        f'Draw $AB={4*k:g}$ cm. Intersect arcs centred at A and B of radii {3*k:g} cm and {5*k:g} cm; label their intersection C and join AC and BC.',blank,answer,
        'Choose the compass radius from the stated side length at each endpoint. The intersection satisfies both lengths simultaneously. Either mirror-image position for C is acceptable. A ruler in the submitted photo is needed to establish centimetre scale.',
        [(1,f'Visible base AB of {4*k:g} cm and the correct-radius construction arcs, with calibration.'),(1,'Correct joined triangle and labels at the arc intersection, with the required side lengths.')],['NSSCO-6131-2018-visual-p13-26'],{'sides':[4*k,3*k,5*k]})


def bisector(g,r,s,l):
    if l==1:
        n=r.randint(20,70)/10;A=(-n,0);B=(n,0);rr=n+2;h=math.sqrt(rr*rr-n*n)
        q=spec((-n-3,n+3,-h-1,h+1),'Segment AB to be reproduced',[line([A,B]),text(-n,-.5,'A'),text(n,-.5,'B')])
        ans=spec(q['bounds'],'Perpendicular bisector with construction arcs',q['elements']+[arc(-n,0,rr,-80,80,'gray',True),arc(n,0,rr,100,260,'gray',True),line([(0,-h-.3),(0,h+.3)],'blue')])
        return make(g,s,l,'perpendicular_bisector',f'Reproduce a segment $AB={2*n:g}$ cm long. Construct its perpendicular bisector using a straight edge and compasses only. Keep your arcs.',
            'Use equal compass radii greater than half AB from A and B, crossing above and below AB. Join those intersections.',q,ans,
            'The two compass intersections are each equidistant from A and B. Joining them gives the perpendicular bisector. Correct line without arcs or correct arcs without a line can earn the source-supported partial award; do not erase the arcs.',
            [(1,'Correct perpendicular bisector OR the correct equal-radius intersecting compass arcs; one partial mark only.'),(1,'Complete correct perpendicular bisector with its valid construction arcs.')],['2020-P2-Q16a.ii'],{'A':A,'B':B,'radius':rr})
    theta=r.choice(tuple(range(30,151,5)));a=math.radians(theta);u=(4,0);v=(4*math.cos(a),4*math.sin(a));p=(4*(1+math.cos(a)),4*math.sin(a))
    q=spec((-6,10,-2,10),'Angle AOB to be reproduced',[line([u,(0,0),v]),text(4.3,0,'A'),text(-.3,-.3,'O'),text(v[0],v[1]+.4,'B')])
    # Equal-radius arcs about the two points on the first compass arc meet at p.
    ans=spec(q['bounds'],'Angle bisector with compass arcs',q['elements']+[arc(0,0,4,-5,theta+5,'gray',True),arc(*u,4,theta-18,theta+18,'gray',True),arc(*v,4,-18,18,'gray',True),line([(0,0),p],'blue')])
    return make(g,s,l,'angle_bisector',f'First draw angle AOB of {theta} degrees using a protractor. Then construct its internal angle bisector using a straight edge and compasses only. Leave the compass arcs visible.',
        'Draw one arc from O across both rays, then equal-radius arcs from the two crossings. Join O to their interior intersection.',q,ans,
        'The first arc locates two points equally far from O; the next two arcs use the same radius. Their interior crossing determines a line equally inclined to both rays. A protractor-only line does not show the required compass construction.',
        [(1,'Correct bisector without valid arcs OR valid construction arcs without the bisector; one partial award only.'),(1,'Correct internal angle bisector with valid compass arcs retained.')],['2022-P1-Q31'],{'angle':theta})


def symmetry(g,r,s,l):
    n=r.choice((3,4,5,6,8));theta=r.randint(0,10)*5
    pts=[(4*math.cos(math.radians(theta+360*i/n)),4*math.sin(math.radians(theta+360*i/n))) for i in range(n)]
    q=spec((-5,5,-5,5),'Regular polygon',[closed(pts)])
    if l==1:
        axes=[line([(-4.5*math.cos(math.radians(theta+180*i/n)),-4.5*math.sin(math.radians(theta+180*i/n))),(4.5*math.cos(math.radians(theta+180*i/n)),4.5*math.sin(math.radians(theta+180*i/n)))],'blue',True) for i in range(n)]
        return make(g,s,l,'draw_symmetry','Copy the regular polygon and draw every line of symmetry.',f'There are {n} lines of symmetry, as shown.',q,spec(q['bounds'],'All lines of symmetry',q['elements']+axes),
            'A line of symmetry folds the entire polygon onto itself. For a regular polygon, the symmetry lines pass through the centre and the appropriate opposite vertices or side midpoints. Check the whole outline, not just one pair of edges.',
            [(1,f'At least one correct symmetry axis through the centre.'),(1,f'All {n} distinct correct axes and no extra incorrect lines.')],['NSSCO-6131-2018-visual-p13-26'],{'n':n,'vertices':pts})
    return make(g,s,l,'read_rotation_order','State the order of rotational symmetry and the smallest positive angle of rotation for this regular polygon.',f'Order {n}; angle $360^\\circ/{n}={360/n:g}^\\circ$.',q,None,
        'Count how many times the whole polygon matches itself in one full turn, including the completed turn. Divide 360° by that order for the smallest positive rotation.',[(1,f'Correct order {n}.'),(1,f'Correct smallest positive rotation {360/n:g} degrees.')],['NSSCO-6131-2018-visual-p13-26'],{'n':n},False)


def locus(g,r,s,l):
    n=r.randint(2,6);cx=r.randint(-2,2);cy=r.randint(-2,2);q=grid((-8,8,-8,8),caption='Coordinate diagram: one unit is one chosen drawing unit')
    if l==1:
        q['elements']=[point(cx,cy),text(cx+.4,cy+.4,'P')];els=q['elements']+[circle(cx,cy,n,'blue')]
        prompt=f'Copy the coordinate diagram. Draw the locus of points exactly {n} units from P.';answer=f'A circle centred at P of radius {n} units.';ref=[(1,f'Complete circle centred at P=({cx},{cy}) with radius {n} coordinate units.')];data={'radius':n,'center':[cx,cy]};sources=['2020-P2-Q16a.i']
    elif l==2:
        q['elements']=[line([(-8,cy),(8,cy)]),text(6,cy+.5,'l')];els=q['elements']+[line([(-8,cy+n),(8,cy+n)],'blue'),line([(-8,cy-n),(8,cy-n)],'blue')]
        prompt=f'Draw the complete locus of points exactly {n} units from the infinite straight line l.';answer=f'Two parallel lines, $y={cy+n}$ and $y={cy-n}$.';ref=[(1,f'One complete parallel line {n} units from l.'),(1,'Both parallel lines, one on each side, with no extra region shaded.')];data={'distance':n,'line_y':cy};sources=['NSSCO-6131-2018-visual-p13-26']
    elif l==3:
        q['elements']=[point(cx-n,cy),point(cx+n,cy),text(cx-n,cy-.5,'A'),text(cx+n,cy-.5,'B')];els=q['elements']+[line([(cx,-8),(cx,8)],'blue')]
        prompt='Draw the locus equidistant from A and B on the grid. A compass construction is not required for this coordinate task.';answer=f'The perpendicular bisector $x={cx}$.';ref=[(1,f'Complete perpendicular bisector x={cx}, not just the midpoint.')];data={'A':[cx-n,cy],'B':[cx+n,cy]};sources=['2020-P2-Q16a.ii']
    else:
        q['elements']=[point(cx,cy),text(cx+.4,cy+.4,'P'),line([(cx,-8),(cx,8)],'gray')]
        region=[(cx,cy)]+[(cx+n*math.cos(math.radians(a)),cy+n*math.sin(math.radians(a))) for a in range(-90,91,3)]+[(cx,cy)]
        els=q['elements']+[line(region,'blue',fill=True),arc(cx,cy,n,-90,90,'blue'),line([(cx,cy-n),(cx,cy+n)],'blue')]
        prompt=f'Shade points at most {n} units from P that also satisfy $x\\ge {cx}$. Draw the boundaries clearly.';answer=f'The closed right-hand half-disc of radius {n}, including the diameter and arc.';ref=[(1,f'Correct circle/arc boundary of radius {n}, centred at P.'),(1,f'Correct right-hand half-disc shaded, with x={cx} and the circular boundary included.')];data={'radius':n,'center':[cx,cy]};sources=['2020-P2-Q16b']
    ans=grid(q['bounds'],els,'Completed locus')
    return make(g,s,l,'locus_'+str(l),prompt,answer,q,ans,'A locus contains every point satisfying the condition. A fixed distance from a point gives a circle; from an infinite line it gives two parallels; equal distances from two points give their perpendicular bisector. For combined conditions take their intersection and respect whether boundaries are included.',ref,sources,data)


def bearings(g,r,s,l):
    bearing=r.choice(tuple(range(15,360,15)));a=math.radians(bearing);B=(5*math.sin(a),5*math.cos(a))
    els=[line([(0,-1),(0,6)]),text(0,6.5,'N'),point(0,0),text(-.4,-.4,'A')]
    if l==1:
        # Compass rose is explicitly graduated, so reading does not require screen calibration.
        for b in range(0,360,15):
            rad=math.radians(b);els.append(line([(5.6*math.sin(rad),5.6*math.cos(rad)),(6*math.sin(rad),6*math.cos(rad))],'gray'))
            if b%30==0:els.append(text(6.7*math.sin(rad),6.7*math.cos(rad),f'{b:03d}'))
        els += [line([(0,0),B],'blue'),text(B[0]+.4,B[1]+.3,'B')]
        return make(g,s,l,'read_bearing','Use the graduated compass diagram to write the three-figure bearing of B from A.',f'${bearing:03d}^\\circ$',spec((-8,8,-8,8),'Bearings measured clockwise from north',els),None,
            'Start at north at A and turn clockwise to AB. Bearings below 100° need a leading zero, such as 030°. Do not use an anticlockwise angle or the return bearing.',[(1,f'Correct clockwise three-figure bearing {bearing:03d} degrees.')],['NSSCO-6131-2018-visual-p13-26'],{'bearing':bearing},False)
    q=spec((-8,8,-8,8),'North line at A',els);ans=spec(q['bounds'],'Required bearing ray',els+[line([(0,0),B],'blue'),text(*B,'B')])
    return make(g,s,l,'draw_bearing',f'Copy the north line. Using a protractor, draw a ray from A on a bearing of ${bearing:03d}^\\circ$ and mark B anywhere on that ray.',
        f'Measure {bearing}° clockwise from north at A, then draw and label ray AB.',q,ans,
        'The starting point and direction of measurement matter: north is 000°, east 090°, south 180° and west 270°. The distance to B is unspecified, so any point on the correct ray is valid. A photo should include your protractor or a clearly graduated angle reference if the angle cannot otherwise be established.',
        [(1,f'Correct ray clockwise from north at A at {bearing} degrees.'),(1,'B placed on that ray and the start/north direction clear; do not require a particular distance.')],['NSSCO-6131-2018-visual-p13-26'],{'bearing':bearing})

GENERATORS=[
 VisualGenerator('clocks',15804,'Time, Clocks and Timetables',{1:clock},{1:'Reading clock faces'}),
 VisualGenerator('geometry',15808,'Geometrical Terms',{1:geometry,2:geometry},{1:'Recognising marked angles',2:'Recognising solid nets'}),
 VisualGenerator('constructions',15810,'Geometrical Constructions',{1:measurement,2:measurement},{1:'Reading a ruler',2:'Constructing triangles with instruments'}),
 VisualGenerator('bisectors',15811,'Angle and Perpendicular Bisectors',{1:bisector,2:bisector},{1:'Constructing a perpendicular bisector',2:'Constructing an angle bisector'}),
 VisualGenerator('symmetry',15812,'Symmetry in Two Dimensions',{1:symmetry,2:symmetry},{1:'Drawing symmetry axes',2:'Recognising rotational symmetry'}),
 VisualGenerator('loci',15816,'Loci',{1:locus,2:locus,3:locus,4:locus},{1:'Drawing a fixed-distance locus',2:'Drawing loci parallel to a line',3:'Drawing an equidistant locus',4:'Shading intersecting locus conditions'}),
 VisualGenerator('bearings',15847,'Bearings and Right-Angled Triangles',{1:bearings,2:bearings},{1:'Reading graduated bearings',2:'Drawing a bearing ray'}),
]
