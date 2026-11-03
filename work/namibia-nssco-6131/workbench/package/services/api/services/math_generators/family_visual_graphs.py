"""Original graph plotting/reading, transformations and vector diagrams."""
import math
from fractions import Fraction
from .visual_common import *
from .formatting import linear_latex,polynomial_latex


def practical(g,r,s,l):
    t1=r.randint(2,5);rest=r.randint(1,3);t2=t1+rest;t3=t2+r.randint(2,5);d=r.randint(3,8)*t1
    pts=[(0,0),(t1,d),(t2,d),(t3,d+r.randint(2,5)*(t3-t2))]
    bounds=(0,t3+1,0,pts[-1][1]+5);kwargs={'x_label':'Time (minutes)','y_label':'Distance (metres)','y_step':5,'equal_scale':False}
    plotted=grid(bounds,[line(pts,'blue')],'Travel graph',**kwargs)
    if l==1:
        return make(g,s,l,'read_travel',f'Read the travel graph. State the distance from the starting point at {t1} minutes and the duration of the stationary part.',f'Distance ${d}$ m; stationary for ${rest}$ minutes.',plotted,None,
            f'The vertical coordinate at time {t1} is {d} m. The horizontal part runs from {t1} to {t2} minutes, so no distance changes for {rest} minutes. A horizontal distance-time segment means stationary, not a vertical segment.',
            [(1,f'Correct distance {d} metres at {t1} minutes.'),(1,f'Correct stationary duration {rest} minutes, not just its end time.')],['NSSCO-6131-2018-visual-p13-26'],{'points':pts,'distance':d,'rest':rest},False)
    if l==2:
        return make(g,s,l,'draw_travel','Draw a distance-time graph for the following observations, joining consecutive points with straight segments.\n\n'+points_table([p[0] for p in pts],[p[1] for p in pts]),
            'Label both axes with their units, plot each observation and join consecutive times in order.',grid(bounds,caption='Suggested blank axes',**kwargs),plotted,
            'Time belongs on the horizontal axis. Choose scales covering every observation. The two equal distances give a horizontal section; connecting points in time order represents the described stages. Each axis may use its own uniform scale.',
            [(1,'Appropriate labelled axes with uniform scales and units.'),(1,f'All observations {pts} plotted in their proper positions.'),(1,'Consecutive points joined with straight segments, including the stationary section.')],['NSSCO-6131-2018-visual-p13-26'],{'points':pts})
    v=r.randint(3,8);t=r.randint(2,5);cruise=r.randint(2,6);speedpts=[(0,0),(t,v),(t+cruise,v),(2*t+cruise,0)];distance=v*(t+cruise)
    chart=grid((0,2*t+cruise+1,0,v+2),[line(speedpts,'blue')],'Speed-time graph',x_label='Time (seconds)',y_label='Speed (m/s)',equal_scale=False)
    return make(g,s,l,'speed_graph_area','Use the speed-time graph to calculate the total distance travelled. Show the areas used.',f'$d=\\tfrac12({t})({v})+({cruise})({v})+\\tfrac12({t})({v})={distance}\\text{{ m}}$.',chart,None,
        'Distance is the area under a speed-time graph. Split this outline into two triangles and the rectangle between them. Multiply time in seconds by speed in m/s to obtain metres; do not read the final speed as the distance.',
        [(1,f'Valid triangle/rectangle area setup for the displayed graph, equivalent to {v}*({t}+{cruise}).'),(1,f'Correct distance {distance} m from that method, with required unit.')],['2021-P1-Q25'],{'points':speedpts,'distance':distance},False)


def straight(g,r,s,l):
    m=r.choice((-3,-2,-1,1,2,3));c=r.randint(-4,4);pts=[(-3,-3*m+c),(3,3*m+c)]
    q=grid((-5,5,-20,20),caption='Straight-line grid',y_step=5,equal_scale=False)
    ans=grid(q['bounds'],[line([(-5,-5*m+c),(5,5*m+c)],'blue')],'Line through the plotted points',y_step=5,equal_scale=False)
    if l==1:
        return make(g,s,l,'draw_straight',f'Draw the graph of $y={linear_latex(m,c)}$. Use at least two calculated points and a ruler.',f'Plot, for example, {pts}; join with one straight line.',q,ans,
            f'The intercept is {c} and the gradient is {m}. Calculate y for two or more x values, plot the ordered pairs, then extend one ruled line across the required domain. The line must not stop as isolated points.',
            [(1,f'At least two correct distinct points satisfying y={linear_latex(m,c)}.'),(1,'Correct ruled straight line through those points with appropriate labelled axes.')],['2024-P1-Q27a'],{'gradient':m,'intercept':c,'points':pts})
    q=grid(q['bounds'],ans['elements']+[point(*p) for p in pts]+[text(pts[0][0]-.3,pts[0][1]+1,'P'),text(pts[1][0]+.3,pts[1][1]+1,'Q')],'Read P and Q from the line',y_step=5,equal_scale=False)
    return make(g,s,l,'read_gradient','Read two points from the line and calculate its gradient. Show rise divided by run.',f'$m=\\frac{{{pts[1][1]}-({pts[0][1]})}}{{3-(-3)}}={m}$.',q,None,
        'Use the same point order in both differences. Count numerical coordinate changes, allowing for the different horizontal and vertical scales; do not divide screen pixel distances.',[(1,'Correct rise/run setup using two distinct points on the displayed line.'),(1,f'Correct gradient {m} from that setup.')],['2020-P2-Q15a'],{'gradient':m,'intercept':c,'points':pts},False)


def quadratic(g,r,s,l):
    a=r.choice((-2,-1,1,2));h=r.randint(-3,3);d=r.randint(2,3);k=-a*d*d
    f=lambda x:a*(x-h)**2+k;xs=list(range(h-3,h+4));ys=[f(x) for x in xs]
    bounds=(h-4,h+4,min(ys+[0])-3,max(ys+[0])+3)
    curve=line([(h-4+i/25,f(h-4+i/25)) for i in range(201)],'blue')
    q=grid(bounds,caption='Axes for the function',y_step=2,equal_scale=False)
    ans=grid(bounds,[curve]+[point(x,y,'blue') for x,y in zip(xs,ys)],'Completed function graph',y_step=2,equal_scale=False)
    rule=polynomial_latex([a,-2*a*h,a*h*h+k])
    if l==1:
        return make(g,s,l,'plot_quadratic',f'Plot and draw $y={rule}$ using the values below. Join with a smooth curve.\n\n'+points_table(xs,ys),
            'Plot all seven points in the table and draw one smooth parabola through them.',q,ans,
            'Use the coordinate pairs, keeping their x/y order. A quadratic graph is a smooth curve with one turning point; do not join the points with separate ruled segments. Reproduce the labelled axes and scales clearly.',
            [(1,'Appropriate labelled axes and consistent scales.'),(1,'At least four of the seven given points correctly plotted.'),(1,'All seven given points correctly plotted.'),(1,'One correct smooth quadratic curve through the points, not ruled segments.')],['2020-P2-Q15c'],{'coefficients':[a,-2*a*h,a*h*h+k],'x':xs,'y':ys})
    if l==2:
        roots=[h-d,h+d];turn=[h,k];intercept=f(0)
        features=[(roots[0],0),(roots[1],0),(0,intercept),(h,k)]
        ans=grid(bounds,ans['elements']+[text(x+.35,y+.7,f'({x},{y})','blue') for x,y in features],
                 'Parabola with intercepts and turning point labelled',y_step=2,equal_scale=False)
        return make(g,s,l,'sketch_quadratic',f'Sketch $y={rule}$, showing and labelling both x-intercepts, the y-intercept and the turning point.',
            f'x-intercepts $({roots[0]},0)$ and $({roots[1]},0)$; y-intercept $(0,{intercept})$; turning point $({h},{k})$.',q,ans,
            f'The rule is {a}(x-({h}))²+({k}). The turning point is ({h},{k}); solving y=0 gives x={roots[0]} and {roots[1]}, and substituting x=0 gives y={intercept}. A sketch need not have a precise plotting scale, but its locations, orientation and labels must agree.',
            [(1,f'First x-intercept ({roots[0]},0) labelled.'),(1,f'Second x-intercept ({roots[1]},0) labelled.'),(1,f'Correct y-intercept (0,{intercept}) labelled.'),(1,f'Correct turning point ({h},{k}) labelled.'),(1,'Correct smooth parabola with its proper opening and intercept/turning-point relationships.')],['2021-P2-Q13'],{'roots':roots,'turning_point':turn,'y_intercept':intercept})
    return make(g,s,l,'read_quadratic_roots','Use the supplied graph to estimate both solutions of $y=0$. State each x-value.',f'$x={h-d}$ or $x={h+d}$.',ans,None,
        'Solutions of y=0 are where the curve crosses the horizontal axis. Read both x-values, not the y-coordinate of the turning point. These intersections occur on labelled grid positions.',[(1,f'First root x={h-d}.'),(1,f'Second root x={h+d}.')],['2020-P2-Q15e.i'],{'roots':[h-d,h+d]},False)


def advanced(g,r,s,l):
    if l==2:
        a=r.choice((-1,1));x0=r.choice((-2,-1,1,2));k=r.randint(-2,2);f=lambda x:a*x*x+k;slope=2*a*x0;y0=f(x0)
        bounds=(-4,4,-12,12);els=[line([(x/25,f(x/25)) for x in range(-100,101)],'blue'),point(x0,y0),text(x0+.4,y0+.7,'P')]
        q=grid(bounds,els,'Curve with marked point P',y_step=2,equal_scale=False)
        ans=grid(bounds,els+[line([(-4,y0+slope*(-4-x0)),(4,y0+slope*(4-x0))],'green')],'Tangent at P',y_step=2,equal_scale=False)
        return make(g,s,l,'draw_tangent',f'Draw a tangent to the curve at P, where $x={x0}$. Use two points on your tangent to estimate its gradient. Show rise/run.',f'The tangent at $P=({x0},{y0})$ has gradient approximately ${slope}$.',q,ans,
            'A tangent matches the local direction of the curve at P. Choose two well-separated points on that tangent, not two points on the curve, and calculate vertical change divided by horizontal change. A graphical estimate consistent with a correctly drawn tangent is accepted; this is not a request for calculus.',
            [(1,'A reasonable tangent drawn at P, matching the local direction of the curve.'),(1,'Valid rise/run calculation from two points on the learner’s tangent.'),(1,f'Gradient estimate consistent with the correct tangent, reference {slope}; assess graph-scale precision without inventing a pixel tolerance.')],['2022-P1-Q23c'],{'a':a,'k':k,'x0':x0,'gradient':slope})
    shape=('reciprocal','reciprocal_square','cubic','exponential','reciprocal_linear')[(s-1)%5];a=r.randint(1,9)
    if shape=='exponential':
        a=r.choice((2,3));f=lambda x:a**x;xs=[-2,-1,0,1,2,3];rule=f'{a}^x';segments=[(-2,3)]
    elif shape=='cubic':f=lambda x:a*x**3/2;xs=[-2,-1,0,1,2];rule=f'\\frac{{{a}}}{{2}}x^3';segments=[(-2,2)]
    else:
        f=(lambda x:a/x) if shape=='reciprocal' else (lambda x:a/(x*x)) if shape=='reciprocal_square' else (lambda x:x+a/x)
        xs=[-4,-2,-1,1,2,4];rule=f'\\frac{{{a}}}{{x}}' if shape=='reciprocal' else f'\\frac{{{a}}}{{x^2}}' if shape=='reciprocal_square' else f'x+\\frac{{{a}}}{{x}}';segments=[(-4,-.05),(.05,4)]
    ys=[f(x) for x in xs];lo=min(0,*ys)-2;hi=max(0,*ys)+2;bounds=(min(xs)-1,max(xs)+1,lo,hi)
    q=grid(bounds,caption='Suggested plotting axes',y_step=tick_step(hi-lo),equal_scale=False)
    curves=[line([(left+(right-left)*i/150,f(left+(right-left)*i/150)) for i in range(151)],'blue') for left,right in segments]
    ans=grid(bounds,curves+[point(x,y,'blue') for x,y in zip(xs,ys)],'Completed curve',y_step=tick_step(hi-lo),equal_scale=False)
    return make(g,s,l,'plot_advanced',f'Plot and draw $y={rule}$ from the table. '+('Do not draw across $x=0$, where the rule is undefined.\n\n' if len(segments)==2 else '\n\n')+points_table(xs,[f'{y:g}' for y in ys]),
        'Plot the given points, then draw the correct smooth branch or branches.',q,ans,
        'Use the actual x and y scales. Reciprocal rules are undefined at zero: their branches approach an asymptote and must not be joined through it. Cubic and exponential rules have their own continuous shapes; avoid ruled point-to-point segments.',
        [(1,'Appropriate axes/scales and at least half the table points correctly plotted.'),(1,'All requested table points correctly plotted.'),(1,'Correct smooth graph shape, with separate branches at x=0 for reciprocal rules.')],['2021-P2-Q12b','2024-P1-Q25b'],{'shape':shape,'a':a,'x':xs,'y':ys})


def lp(g,r,s,l):
    a=r.randint(1,3);b=r.randint(1,3);c=a+b+r.randint(4,7);strict=r.choice((False,True));L=c+2
    boundaries=[line([(a,0),(a,L)]),line([(0,b),(L,b)],dashed=strict),line([(0,c),(c,0)])]
    unwanted=[line([(0,0),(a,0),(a,L),(0,L)],'gray',fill=True),line([(0,0),(L,0),(L,b),(0,b)],'gray',fill=True),line([(0,c),(0,L),(L,L),(L,0),(c,0)],'gray',fill=True)]
    vertices=[(a,b),(c-b,b),(a,c-a)];center=(sum(p[0] for p in vertices)/3,sum(p[1] for p in vertices)/3)
    shown=grid((0,L,0,L),unwanted+boundaries+[text(*center,'R','blue')],'Unwanted regions shaded; R remains unshaded')
    inequalities=f'$x\\ge {a}$, $y'+('>' if strict else r'\ge')+f'{b}$ and $x+y\\le {c}$'
    if l==1:
        return make(g,s,l,'shade_lp',f'Draw the boundaries for {inequalities}. Shade the unwanted regions and label the remaining region R.',
            'The intersection R is the triangular region left unshaded. '+('The horizontal boundary is broken because its inequality is strict; both other boundaries are solid.' if strict else 'All three boundaries are solid because equality is allowed in every inequality.'),grid((0,L,0,L),caption='Blank grid for inequalities'),shown,
            'Test a point to determine which side of each boundary fails its inequality, then shade that unwanted half-plane. The solution must satisfy all conditions at once. Broken lines exclude equality; solid lines include it.',
            [(1,'All three boundary lines correctly positioned, including broken/solid convention.'),(1,'Unwanted half-planes shaded, leaving the correct intersection unshaded.'),(1,'Remaining feasible region correctly labelled R.')],['2024-P1-Q27a','2024-P1-Q27b'],{'a':a,'b':b,'c':c,'strict':strict,'vertices':vertices})
    if l==2:
        return make(g,s,l,'read_lp','Write the three inequalities defining the unshaded region R. Use the solid or broken boundaries to decide equality.',inequalities,shown,None,
            'Read each boundary equation and decide which side contains R. '+('The broken horizontal boundary excludes equality.' if strict else 'All three solid boundaries include equality.')+' Describe R, rather than the shaded unwanted regions.',[(1,f'x >= {a}.'),(1,f'y {">" if strict else ">="} {b}.'),(1,f'x+y <= {c}, or an equivalent inequality.')],['2020-P1-Q26b'],{'a':a,'b':b,'c':c,'strict':strict},False)
    # A closed region is needed to ask for an attained maximum.
    p=r.randint(1,4);q=r.randint(1,4);values=[p*x+q*y for x,y in vertices];maximum=max(values)
    shown=grid((0,L,0,L),unwanted+[line([(a,0),(a,L)]),line([(0,b),(L,b)]),line([(0,c),(c,0)])]+[text(*center,'R','blue')],'Closed region R')
    return make(g,s,l,'optimise_lp',f'Using the graph, find the maximum of ${p}x+{q}y$ in the closed unshaded region R. Show the vertex values.',f'At vertices {vertices}, the objective values are {values}; maximum ${maximum}$.',shown,None,
        'For this bounded triangular linear-programming region, an optimum occurs at a vertex; if two adjacent vertices tie, the edge between them is also optimal. Read all vertices, evaluate the same objective at each, then compare.',[(1,f'Correct vertex evaluations {values} from {vertices}.'),(1,f'Correct maximum {maximum}.')],['2023-P1-Q28b'],{'vertices':vertices,'objective':[p,q],'values':values,'maximum':maximum},False)


def transform(g,r,s,l):
    x=2*r.randint(1,3);y=2*r.randint(1,3);pts=[(x,y),(x+4,y),(x,y+2)]
    task={1:'reflection',2:'translation',3:'rotation',4:'enlargement',5:('reflection','translation','rotation','enlargement')[(s-1)%4]}[l]
    center=[r.randint(-2,2),r.randint(-2,2)];axis=r.choice(('x','y'));c=r.randint(-2,2);dx=r.choice((-5,-3,2,4));dy=r.choice((-4,-2,3,5));angle=r.choice((90,180,270));k=r.choice((-.5,-2,.5,1.5,2))
    if task=='reflection':
        image=[(2*c-u,v) if axis=='x' else (u,2*c-v) for u,v in pts];detail=f'reflection in ${axis}={c}$';extra=[line([(c,-24),(c,24)] if axis=='x' else [(-24,c),(24,c)],'gray',True)]
    elif task=='translation':image=shifted(pts,dx,dy);detail=f'translation by vector $({dx},{dy})$';extra=[]
    elif task=='rotation':
        def rotate(p):
            u,v=p[0]-center[0],p[1]-center[1]
            U,V=(-v,u) if angle==90 else (-u,-v) if angle==180 else (v,-u)
            return U+center[0],V+center[1]
        image=[rotate(p) for p in pts];detail=f'rotation {angle}° anticlockwise about $({center[0]},{center[1]})$';extra=[]
    else:image=[(center[0]+k*(u-center[0]),center[1]+k*(v-center[1])) for u,v in pts];detail=f'enlargement, scale factor ${k:g}$, centre $({center[0]},{center[1]})$';extra=[]
    allpts=pts+image;bound=max(12,math.ceil(max(abs(v) for p in allpts for v in p))+2);step=max(1,math.ceil(bound/8))
    original=polygon_with_labels(pts,'ABC');target=polygon_with_labels(image,('A′','B′','C′'),'blue')
    chart=grid((-bound,bound,-bound,bound),original+extra,'Original triangle ABC',x_step=step,y_step=step)
    ans=grid(chart['bounds'],original+target+extra,'Original and transformed triangle',x_step=step,y_step=step)
    data={'shape':task,'original':pts,'image':image,'center':center,'axis':axis,'line':c,'dx':dx,'dy':dy,'angle':angle,'scale_factor':k,'detail':detail}
    source={'reflection':['2020-P2-Q8b'],'translation':['2022-P2-Q15a.i'],'rotation':['2022-P2-Q15a.ii'],'enlargement':['2024-P2-Q28c']}[task]
    if l==5:
        marks=3 if task in ('rotation','enlargement') else 2
        achievements=([(1,'Correct transformation type: '+task+'.'),(1,'Correct scale factor '+str(k)+'.'),(1,'Correct centre '+str(center)+'.')] if task=='enlargement' else [(1,'Correct transformation type: rotation.'),(1,f'Correct {angle}° anticlockwise, or equivalent signed angle/direction.'),(1,'Correct centre '+str(center)+'.')] if task=='rotation' else [(1,'Correct transformation type: '+task+'.'),(1,'Correct '+('directed vector '+str([dx,dy]) if task=='translation' else 'mirror line '+axis+'='+str(c))+'.')])
        return make(g,s,l,'describe_visual_transform','Describe fully the single transformation taking triangle ABC to A′B′C′.',detail+'.',ans,None,
            'Match corresponding labelled vertices, then determine the transformation and all of its defining information. A rotation needs angle, direction and centre; enlargement needs scale factor and centre; reflection needs its mirror line; translation needs its directed vector. Negative or fractional scale factors must be retained.',achievements,['2023-P2-Q9a.i'] if task=='rotation' else ['NSSCO-6131-2018-visual-p13-26'],data,False)
    return make(g,s,l,'draw_visual_transform',f'Draw and label the image A′B′C′ of triangle ABC under a {detail}.',f'Image vertices, in corresponding order: {image}.',chart,ans,
        'Apply the transformation to every labelled vertex and join the image in the original order. Preserve the whole shape. For enlargement measure vectors from the stated centre and multiply by the signed scale factor; a negative factor places the image on the opposite side. Coordinates alone do not establish the required drawing.',
        [(1,'Correct transformed shape/size with a positional error, or the applicable one-component translation / wrong-centre enlargement partial route; do not award for an unrelated triangle.'),(1,f'Complete correct positioned and labelled image with corresponding vertices {image}.')],source,data)


def vector(g,r,s,l):
    a=[r.choice((-5,-4,-3,-2,2,3,4,5)),r.choice((-5,-4,-3,-2,2,3,4,5))];b=[r.choice((-3,-2,2,4)),r.choice((-3,-1,2,3))]
    if [a[0]+b[0],a[1]+b[1]]==[0,0]:b[1]+=1
    def arrow(u,v,color):
        dx,dy=v[0]-u[0],v[1]-u[1];n=math.hypot(dx,dy);ux,uy=dx/n,dy/n
        return [line([u,v],color),line([(v[0]-.6*ux+.25*uy,v[1]-.6*uy-.25*ux),v,(v[0]-.6*ux-.25*uy,v[1]-.6*uy+.25*ux)],color)]
    q=grid((-10,10,-10,10),[point(0,0),text(-.4,-.4,'O')],'Vector grid')
    if l==1:
        els=q['elements']+arrow((0,0),a,'blue')+[text(a[0]+.4,a[1]+.4,'A','blue')];target=a;prompt=f'Draw the directed vector $\\binom{{{a[0]}}}{{{a[1]}}}$ starting at O. Label its endpoint A.';answer=f'$A=({a[0]},{a[1]})$, with the arrow pointing from O to A.'
    else:
        target=[a[0]+b[0],a[1]+b[1]];q['elements']+=arrow((0,0),a,'ink')+arrow((0,0),b,'green')+[text(a[0],a[1]+.6,'a'),text(b[0],b[1]+.6,'b')]
        els=q['elements']+[line([a,target,b],'gray',True)]+arrow((0,0),target,'blue') if target!=[0,0] else q['elements']+[point(0,0,'blue')]
        prompt='Copy vectors a and b. Construct their sum a+b using a parallelogram or head-to-tail diagram, showing the resultant direction.';answer=f'$a+b=({target[0]},{target[1]})$, directed from O to the opposite parallelogram vertex.'
    return make(g,s,l,'draw_vector_'+str(l),prompt,answer,q,grid(q['bounds'],els,'Completed vector diagram'),
        'The first component is horizontal displacement and the second vertical displacement. The arrow gives direction, not an undirected segment. For a sum, place the second vector at the end of the first or complete a parallelogram; the resultant starts at the common origin.',
        [(1,'Correct component displacements or correct head-to-tail/parallelogram construction.'),(1,f'Correct resultant endpoint {target}, with direction and requested label visible.')],['NSSCO-6131-2018-visual-p13-26'],{'a':a,'b':b,'result':target})

GENERATORS=[
 VisualGenerator('practical_graphs',15828,'Kinematics and Rate of Change',{1:practical,2:practical,3:practical},{1:'Reading travel graphs',2:'Drawing graphs from observations',3:'Reading areas under speed-time graphs'}),
 VisualGenerator('straight_lines',15831,'Straight-Line Graphs and Gradients',{1:straight,2:straight},{1:'Drawing a straight-line graph',2:'Reading a gradient from a graph'}),
 VisualGenerator('quadratics',15832,'Quadratic Graph Calculations',{1:quadratic,2:quadratic,3:quadratic},{1:'Plotting a quadratic',2:'Sketching with intercepts and turning point',3:'Reading graphical roots'}),
 VisualGenerator('advanced_graphs',15834,'Reciprocal, Cubic and Exponential Graph Properties',{1:advanced,2:advanced},{1:'Plotting reciprocal, cubic and exponential curves',2:'Drawing a tangent and estimating gradient'}),
 VisualGenerator('linear_programming',15829,'Linear Programming Calculations',{1:lp,2:lp,3:lp},{1:'Drawing boundaries and shading unwanted regions',2:'Reading inequalities from a region',3:'Optimising from graphical vertices'}),
 VisualGenerator('transformations',15841,'Transformations in Coordinates (shared lessons 15841–15843)',{1:transform,2:transform,3:transform,4:transform,5:transform},{1:'Drawing a reflection',2:'Drawing a translation',3:'Drawing a rotation',4:'Drawing an enlargement',5:'Describing a transformation from figures'}),
 VisualGenerator('vectors',15838,'Introduction to Vectors',{1:vector,2:vector},{1:'Drawing a directed vector',2:'Constructing a vector sum'}),
]
