"""Explicit written methods for the existing text-only supplementary lessons."""
from .topic_teaching import *

LABELS={
'nssco_geometrical_terms':{1:'Classifying an angle',2:'Counting prism faces',3:'Using equal base angles'},
'nssco_constructions_scale_drawings':{1:'Converting a scale length',2:'Halving a bisected angle',3:'Finding a segment midpoint'},
'nssco_symmetry_two_dimensions':{1:'Counting regular-polygon symmetry lines',2:'Finding the smallest symmetry rotation',3:'Combining successive rotations'},
'nssco_symmetry_circles':{1:'Using equal tangents',2:'Bisecting a chord',3:'Comparing distances to equal chords'},
'nssco_locus_numeric':{1:'Finding an equidistant line',2:'Finding an extreme point on a circle',3:'Finding a parallel distance locus'},
'nssco_kinematics_rate_change':{1:'Speed from distance and time',2:'Acceleration from a speed change',3:'Distance during uniform acceleration',4:'Distance while braking'},
'nssco_introduction_functions':{1:'Evaluating a linear function',2:'Finding an input from its output',3:'Evaluating a quadratic function'},
'nssco_introduction_vectors':{1:'Finding displacement components',2:'Reversing a vector',3:'Finding an endpoint'},
'nssco_reading_charts_text':{1:'Reading a named frequency',2:'Applying a pictogram key',3:'Finding a pie-chart sector angle',4:'Calculating average change'},
'nssco_histograms_text':{1:'Finding class width',2:'Calculating frequency density',3:'Recovering a class frequency',4:'Combining unequal-width classes'},
}


def content(p):
    if p.generator_id not in LABELS:return None
    m=p.machine;s=p.skill;lines=[]
    if s=='angle_vocabulary':
        a=m['angle'];lo,hi=(0,90) if a<90 else (90,180) if a<180 else (180,360)
        lines=[f'{lo}^\\circ<{a}^\\circ<{hi}^\\circ']
        e=f'The given angle is ${a}^\\circ$. Acute means between $0^\\circ$ and $90^\\circ$; obtuse means between $90^\\circ$ and $180^\\circ$; reflex means between $180^\\circ$ and $360^\\circ$. Compare with the boundaries rather than judging a drawing’s appearance.'
    elif s=='prism_faces':
        a=m['sides'];lines=[label('Lateral faces')+f'={a}',label('Total faces')+f'={a}+2={a+2}']
        e=f'The prism has two congruent ${a}$-sided bases. Each base edge gives one lateral face, so there are ${a}$ lateral faces and two bases. Count surfaces, not vertices or edges.'
    elif s=='isosceles_angles':
        a=m['base_angle'];lines=[label('Vertex angle')+f'=180^\\circ-2({a}^\\circ)={180-2*a}^\\circ']
        e=f'The two base angles are equal, each ${a}^\\circ$. All three interior angles of a triangle total $180^\\circ$. Subtract both equal base angles to leave the vertex angle; subtracting one would leave two angles together.'
    elif s=='scale_length':
        a,b=m['cm'],m['scale'];lines=[label('Actual length in cm')+f'={a}\\times{b}={a*b}',label('Actual length in m')+'='+frac(a*b,100)]
        e=f'The drawing length is ${a}$ cm and scale $1:{b}$ means one drawing centimetre represents ${b}$ actual centimetres. Multiply by ${b}$, then divide by $100$ to express the actual length in metres. Both sides of the scale ratio must use the same unit.'
    elif s in ('angle_bisection','perpendicular_bisection','chord_midpoint'):
        a=m.get('angle',m.get('length'));lines=[label('One equal part')+'='+frac(a,2)+'='+q(F(a)/2)]
        e=(f'The original '+('angle' if s=='angle_bisection' else 'length')+f' is ${a}$. Bisect means divide into two equal parts, so each is ${q(F(a)/2)}$. '+{'angle_bisection':'Use degrees. This calculation finds the angle size; it does not demonstrate a compass construction.','perpendicular_bisection':'The perpendicular bisector meets AB at its midpoint M, so AM is half AB. Use centimetres.','chord_midpoint':'A perpendicular from the circle centre to a chord bisects the chord. Thus AM is half AB; use centimetres.'}[s])
    elif s in ('regular_polygon_symmetry','rotation_angle','repeated_rotation'):
        a=m['n'];k=m.get('k',1)
        lines=[label('Symmetry lines')+f'={a}'] if s=='regular_polygon_symmetry' else [label('Smallest rotation')+'='+frac(360,a),label('Requested rotation')+'='+frac(f'{360}\\times{k}',a)]
        e=f'The polygon is regular with ${a}$ sides. It has ${a}$ lines of symmetry and rotational order ${a}$. One complete turn is $360^\\circ$, so its smallest positive symmetry rotation is ${frac(360,a)}^\\circ$. '+(f'The question requests ${k}$ successive turns, so multiply this angle by ${k}$.' if s=='repeated_rotation' else 'Use the property asked for: a line count is not an angle.')
    elif s=='equal_tangents':
        a,b,L=m['a'],m['b'],m['length'];lines=[f'{a}x+{b}={L}',f'{a}x={L}-{b}={L-b}','x='+frac(L-b,a)]
        e=f'PA and PB are tangents drawn from the same external point P, so their lengths are equal. Here PA is ${a}x+{b}$ cm and PB is ${L}$ cm. Equate them, subtract ${b}$, then divide by ${a}$. $x$ is the unknown in the length expression, not itself the entire tangent length.'
    elif s=='equal_chord_distances':
        lines=[f'd={m["distance"]}\\text{{ cm}}'];e=f'Equal chords of one circle are the same perpendicular distance from its centre. Here the known distance is ${m["distance"]}$ cm, so $d$ is also ${m["distance"]}$ cm. Compare perpendicular centre-to-chord distances, not chord lengths.'
    elif s=='equidistant_points':
        a,b=m['a'],m['b'];lines=['x='+frac(f'({a})+({b})',2)+'='+q(F(a+b)/2)]
        e=f'A and B lie on the horizontal axis at $({a},0)$ and $({b},0)$. The locus of points equally far from them is the perpendicular bisector of AB, a vertical line through their midpoint. Its constant $x$-coordinate is the average of ${a}$ and ${b}$, not their separation.'
    elif s=='point_distance_locus':
        h,k,r=m['h'],m['k'],m['r'];lines=[f'x_{{\\max}}=({h})+{r}={h+r}',f'y={k}']
        e=f'The centre is C$({h},{k})$ and the fixed distance is radius ${r}$. The locus is a circle. Its greatest $x$ occurs one radius to the right of C, at $({h+r},{k})$. The question asks for that $x$-coordinate, not the radius or the full equation of the circle.'
    elif s=='line_distance_locus':
        c,d=m['c'],m['d'];lines=[f'y=({c})+{d}={c+d}']
        e=f'The original horizontal line is $y={c}$ and the perpendicular distance is ${d}$. There are two parallel distance loci, $y={c}+{d}$ and $y={c}-{d}$. The condition “above” selects the larger $y$ value, even when the original line has a negative coordinate.'
    elif s in ('distance_time_gradient','acceleration','trapezium_distance','braking_distance'):
        if s=='distance_time_gradient':
            d,t=m['distance'],m['time'];lines=['v='+frac(d,t)];e=f'$v$ is speed in metres per second. The distance change is ${d}$ metres over ${t}$ seconds. A distance-time gradient is change in distance divided by elapsed time; it is not the area under this graph.'
        elif s=='acceleration':
            u,v,t=m['u'],m['v'],m['t'];lines=['a='+frac('v-u','t')+'='+frac(f'{v}-{u}',t)];e=f'$a$ is acceleration, $u={u}$ m/s the initial speed, $v={v}$ m/s the final speed and $t={t}$ seconds the duration. Divide the change in speed by time. The result is in metres per second squared; final speed divided by time would ignore the initial speed.'
        else:
            u=m.get('u',m.get('v'));v=0 if s=='braking_distance' else m['v'];t=m['t'];lines=['d='+frac('(u+v)t',2)+'='+frac(f'({u}+{v})\\times{t}',2)];e=f'$d$ is distance, initial speed $u={u}$ m/s, final speed $v={v}$ m/s and duration $t={t}$ seconds. Uniform acceleration makes the speed-time segment straight. Distance is its trapezium area, equivalently average speed $(u+v)/2$ times time. '+('Braking ends at rest, so the region is a triangle.' if s=='braking_distance' else 'Using the final speed for the whole interval would overestimate distance.')
    elif s in ('function_value','function_input','nonlinear_function_value'):
        a,b=m['a'],m['b']
        if s=='function_input':
            out=m['output'];lines=[f'{a}x+({b})={out}',f'{a}x={out}-({b})','x='+frac(f'{out}-({b})',a)];e=f'$f$ names the function, $x$ its unknown input and ${out}$ the given output. The rule multiplies by ${a}$ then adds ${b}$. Undo those operations in reverse order: subtract ${b}$ from the output and divide the entire remainder by ${a}$. This is solving for an input, not evaluating $f({out})$.'
        else:
            x=m['x'];power='^2' if s=='nonlinear_function_value' else '';lines=[f'f({x})={a}({x}){power}+({b})'];e=f'$f$ names the function and its input here is ${x}$. Substitute that complete input in brackets. '+(f'Square the input first, giving ${x*x}$, then multiply by coefficient ${a}$ and add constant ${b}$. The coefficient itself is not squared.' if power else f'Multiply the input by coefficient ${a}$, then add constant ${b}$. Function notation does not mean multiplication by a letter $f$.')
    elif s in ('displacement_components','reverse_vector','endpoint_from_displacement'):
        if s=='reverse_vector':
            a,b=m['AB'];lines=[r'\overrightarrow{BA}=-\overrightarrow{AB}='+point([-a,-b])];e=f'The displacement from A to B is ${point([a,b])}$. Reversing the journey negates both the horizontal and vertical components, giving ${point([-a,-b])}$. Reversing only one component would be a different displacement.'
        elif s=='displacement_components':
            a,b=m['A'],m['B'];lines=['A='+point(a)+r',\quad B='+point(b),r'\overrightarrow{AB}=('+f'({b[0]})-({a[0]}),({b[1]})-({a[1]}))'];e=f'A is ${point(a)}$ and B ${point(b)}$. For A to B use endpoint minus starting point in each coordinate, keeping horizontal first and vertical second. Negative components represent leftward or downward movement, not a negative length.'
        else:
            a,b=m['A'],m['AB'];lines=['B=('+f'({a[0]})+({b[0]}),({a[1]})+({b[1]}))'];e=f'The start is A${point(a)}$ and displacement AB is ${point(b)}$. Add the horizontal displacement to A’s $x$-coordinate and the vertical displacement to its $y$-coordinate. The result is endpoint B, not a new displacement.'
    elif s=='frequency_table':
        i=m['i'];values=m['counts'];lines=[label('Frequency for '+chr(65+i))+f'={values[i]}'];e=f'The stated categories A, B, C and D have frequencies ${", ".join(map(str,values))}$ in that order. Category {chr(65+i)} is position ${i+1}$, so read its corresponding frequency ${values[i]}$. The question asks for one category, not the sum of all categories.'
    elif s=='pictogram_key':
        a,k,h=m['symbols'],m['key'],m['half'];lines=[label('Equivalent full symbols')+f'={a}+'+frac(h,2),label('Learners')+f'=({a}+'+frac(h,2)+f')\\times{k}'];e=f'One full symbol represents ${k}$ learners. There are ${a}$ full symbols'+(' and one half symbol' if h else '')+f'. A half symbol represents ${q(F(k)/2)}$ learners. Count equivalent full symbols, then multiply by the key; adding the symbol count to the key has no counting meaning.'
    elif s=='pie_sector_angle':
        a,t=m['football'],m['total'];lines=[r'\theta='+frac(a,t)+r'\times360^\circ'];e=f'The full circle represents all ${t}$ learners and has angle $360^\\circ$. Football represents ${a}$ of them. Multiply its fraction ${frac(a,t)}$ by $360^\\circ$ to find sector angle $\\theta$. The frequency and the angle use different units.'
    elif s=='line_chart_change':
        a,b,t=m['start'],m['end'],m['dt'];lines=[label('Average change per hour')+'='+frac(f'({b})-({a})',t)];e=f'The reading changes from ${a}$ to ${b}$ over ${t}$ hours. Average rate of change is final reading minus initial reading, divided by elapsed time. A negative answer correctly describes a decrease; it should not be made positive just because it is a rate.'
    elif s in ('class_width','frequency_density','frequency_from_density','unequal_width_total'):
        if s=='unequal_width_total':
            w1,w2=m['widths'];d1,d2=m['densities'];lines=[f'f_1={w1}\\times{d1}={w1*d1}',f'f_2={w2}\\times{d2}={w2*d2}',f'f_{{total}}={w1*d1}+{w2*d2}'];e=f'The two class widths are ${w1}$ and ${w2}$, with densities ${d1}$ and ${d2}$. In a histogram, frequency is bar area: width × density. Compute each area separately, then add the two frequencies. Adding heights alone is invalid when widths differ.'
        else:
            a,b=m['left'],m['right'];w=b-a;lines=[f'w={b}-{a}={w}'];e=f'$w$ is the class width: upper boundary ${b}$ minus lower boundary ${a}$, giving ${w}$. Histogram frequency $f$ equals width $w$ times frequency density $D$.'
            if s=='frequency_density':lines.append('D='+frac('f','w')+'='+frac(m['frequency'],w));e+=f' Here frequency is ${m["frequency"]}$, so divide by width, not by the upper boundary.'
            elif s=='frequency_from_density':lines.append(f'f=wD={w}\\times{m["density"]}');e+=f' Here density is ${m["density"]}$, so multiply it by width to recover the class frequency.'
    else:raise ValueError(s)
    return finish(p,lines,e)
