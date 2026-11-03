"""Operation-specific working for immutable prepared visual questions.

Only explanations are new. Prepared question/reference files remain unchanged.
"""
from fractions import Fraction
from .solution_programs import Author
from .formatting_adapter import q

def measurement(value):
    """Keep familiar decimal readings for instruments and physical lengths."""
    return format(float(value), ".10g")



def visual_program(p,content):
    f=p.generator_id.removeprefix('nssco_');m=p.machine;t=m.get('task',p.skill)
    if not f.startswith('visual_'):return None
    if t=='shade_lp':
        from dataclasses import replace
        boundary=('The horizontal boundary is broken; the other two are solid.' if m['strict'] else 'All three boundaries are solid because equality is allowed.')
        p=replace(p,answer='The triangular intersection R is left unshaded. '+boundary)
    a=Author(p,content)
    def add(key,action,reason,result):a.add(key,action,reason,expression=result)
    def seq(values):return ', '.join(q(x) for x in values)
    def coords(values):return '; '.join('('+seq(v)+')' for v in values)
    if t=='shade_venn':
        rules={'intersection':('Select the overlap','An intersection contains elements in both sets.'),
               'union':('Select both circles','A union includes either set and their overlap once.'),
               'complement':('Select the region outside both circles','The complement of the union contains only points outside A and B.'),
               'a_complement':('Select every region outside A','The complement of A includes the B-only region and the region outside both circles.'),
               'a_not_b':('Select A outside the overlap','A intersect B-prime requires membership of A and exclusion from B.')}
        # Prepared operation names are explicit; reject an unknown operation.
        aliases={'A_only':'a_not_b','a_only':'a_not_b','A_intersection_B_complement':'a_not_b','A_complement':'a_complement','not_A':'a_complement','outside_union':'complement','A_prime':'a_complement','difference':'a_not_b'}
        op=aliases.get(m['operation'],m['operation'])
        if op not in rules:
            raise ValueError('Unmapped Venn operation '+op)
        action,reason=rules[op];add('regions',action,reason,p.answer)
    elif t=='read_venn':
        x,y,z,o=(m[k] for k in ('A_only','intersection','B_only','outside'));total=x+y+z+o
        add('union','Add the disjoint regions inside either circle','The intersection is counted once in a union.',f'n(A∪B)={x}+{y}+{z}={x+y+z}')
        add('total','Count every universal-set region','A probability denominator includes outcomes outside both circles.',f'n(U)={x}+{y}+{z}+{o}={total}')
        add('probability','Divide the overlap count by the total','The intersection is the favourable event.',rf'P(A\cap B)=\frac{{{y}}}{{{total}}}={q(Fraction(y,total))}')
    elif t=='read_clock':
        add('minutes','Read the longer minute hand','Each numbered clock interval represents five minutes.',f'{m["minute"]} minutes past the hour')
        add('hour','Read the shorter hour hand','The hour hand advances towards the next hour as minutes pass.',f'{m["hour"]}:{m["minute"]:02d}')
    elif t=='angle_name':add('classify','Follow the marked arc','Classify that arc using 90°, 180° and 360°, rather than automatically taking the smaller angle.',f'{m["angle"]}°: {p.answer}')
    elif t=='recognise_net':add('fold','Match the face shapes and adjacencies','A net must fold into the solid with matching edges and no overlapping faces.',m['solid'])
    elif t=='measure_segment':
        # Frozen prepared v1 records lack endpoint fields; their authored
        # explanation retains the actual readings, so recover only that pair.
        import re
        readings=re.search(r'A aligns with ([0-9.]+) cm and B aligns with ([0-9.]+) cm',m.get('explanation',''))
        start=m.get('ruler_start',float(readings[1]) if readings else None)
        end=m.get('ruler_end',float(readings[2]) if readings else None)
        if start is None or end is None:raise ValueError('Missing ruler endpoint evidence')
        add('difference','Subtract the reading at A from the reading at B','Length is the difference between the two readings.',rf'AB={measurement(end)}-{measurement(start)}={measurement(m["length"])}\,\mathrm{{cm}}')
    elif t=='construct_triangle':
        b,l,r=m['sides'];add('base','Draw the base to scale','The base fixes the separation of the two compass centres.',f'AB={measurement(b)} cm')
        add('arcs','Intersect the two distance arcs','A point on both arcs has the required distance from each endpoint.',f'Radius from A: {measurement(l)} cm; radius from B: {measurement(r)} cm.')
        add('join','Join the intersection to both endpoints','The intersection supplies the third vertex; either mirror-image intersection is valid.', 'Label C and join AC and BC, retaining the arcs.')
    elif t in ('perpendicular_bisector','angle_bisector'):
        if t=='perpendicular_bisector':
            add('arcs','Draw equal-radius arcs from A and B','A radius greater than half AB gives intersections above and below the segment.',f'Equal compass radii {measurement(m["radius"])} cm; retain both crossings.')
            add('line','Join the two arc intersections','Both crossings are equidistant from A and B, so their joining line is the perpendicular bisector.','Rule the line through both crossings; retain all arcs.')
        else:
            add('first_arc','Draw one arc from the angle vertex','The two ray crossings are equally far from the vertex.','Mark the two ray crossings.')
            add('equal_arcs','Intersect equal-radius arcs from those crossings','Their interior intersection is symmetric between the two rays.','Keep the compass radius unchanged for the two arcs.')
            add('bisector','Join the vertex to the interior crossing','That ray makes equal angles with the original rays.',f'Each half-angle is {measurement(Fraction(m["angle"],2))}°; retain the arcs.')
    elif t in ('draw_symmetry','read_rotation_order'):
        n=m['n']
        if t=='draw_symmetry':
            add('axis','Locate axes through the polygon centre','Each valid fold maps the whole regular polygon onto itself.',f'{n} distinct reflection axes.')
            add('complete','Include every distinct fold exactly once','Axes pass through opposite vertices or side midpoints as appropriate.','Draw the full set shown in the reference, without extra lines.')
        else:
            add('order','Count matching positions in one full turn','The completed full turn counts as a matching position.',f'Rotational order {n}.')
            add('angle','Divide a full turn by the order','Equally spaced matching positions have equal intervening angles.',f'360°/{n}={q(Fraction(360,n))}°')
    elif t.startswith('locus_'):
        if t=='locus_1':add('circle','Draw a circle about the fixed point','A circle is the set of points at one fixed distance from its centre.',f'Centre {coords([m["center"]])}; radius {m["radius"]} units.')
        elif t=='locus_2':
            d,y=m['distance'],m['line_y'];add('parallel','Draw parallels on both sides','Distance from a line is measured perpendicularly; both sides satisfy the same fixed distance.',f'y={y+d} and y={y-d}.')
        elif t=='locus_3':
            x=Fraction(m['A'][0]+m['B'][0],2);add('midpoint','Find the segment midpoint','Equal distances to two fixed endpoints require their perpendicular bisector.',f'Midpoint x={q(x)}.')
            add('bisector','Draw the perpendicular through that midpoint','The segment is horizontal, so its perpendicular bisector is vertical.',f'x={q(x)}')
        else:
            add('disc','Draw the radius boundary and diameter','The fixed-radius condition defines the circle boundary; the half-plane condition selects one side.',f'Centre {coords([m["center"]])}; radius {m["radius"]}.')
            add('region','Include the permitted interior and boundary','A closed half-disc includes both its arc and diameter.',p.answer)
    elif t=='read_travel':
        add('distance','Read the distance ordinate at the requested time','The vertical scale records distance from the starting point.',f'{m["distance"]} m')
        add('rest','Subtract times at the ends of the horizontal segment','Constant distance means stationary motion.',f'{m["rest"]} minutes stationary.')
    elif t=='draw_travel':
        add('plot','Plot the recorded time-distance pairs','Time is horizontal and distance vertical, with units on both axes.',coords(m['points']))
        add('join','Join successive observations in time order','The stated stages are represented by the consecutive straight segments.','Retain horizontal segments for periods at rest.')
    elif t=='speed_graph_area':
        pts=m['points'];x0,y0=pts[0];x1,y1=pts[1];x2,y2=pts[2];x3,y3=pts[3]
        add('areas','Calculate the two triangles and the rectangle','Distance travelled is the area under a nonnegative speed-time graph.',f'½({x1-x0})({y1}) + ({x2-x1})({y1}) + ½({x3-x2})({y2})')
        add('distance','Add the three non-overlapping areas','Every time interval contributes once to total distance.',f'{m["distance"]} m')
    elif t in ('shade_lp','read_lp'):
        strict='>' if m['strict'] else '≥'
        add('vertical','Read the vertical boundary and allowed side' if t=='read_lp' else 'Identify the vertical boundary and allowed side','A lower bound on x keeps points to the right.',f'x≥{m["a"]}')
        add('horizontal','Identify the horizontal boundary and inclusion',(('A broken line excludes equality, so use a strict inequality.' if m['strict'] else 'A solid line includes equality, so use a non-strict inequality.') if t=='read_lp' else ('A strict inequality excludes its boundary, so draw a broken line.' if m['strict'] else 'Equality is allowed on this boundary, so draw a solid line.')),f'y{strict}{m["b"]}')
        add('diagonal','Keep the side satisfying the sum limit','The required region is the intersection of all three half-planes.',f'x+y≤{m["c"]}'+('; these three inequalities describe R.' if t=='read_lp' else '; label their common permitted region R.'))
    elif t=='optimise_lp':
        add('vertices','Evaluate the objective at every feasible vertex','A linear objective attains a bounded maximum at a vertex or a tying edge.',a.rows[0])
        add('compare','Select the largest objective value','Compare all candidates and include any tied optimum.',str(m['maximum']))
    elif t=='draw_straight':
        add('points','Plot two distinct points on the rule','Two correct points determine a straight line.',coords(m['points']))
        add('line','Join using a ruler','A linear rule has constant gradient.',f'y={m["gradient"]}x+({m["intercept"]})')
    elif t=='read_gradient':
        (x1,y1),(x2,y2)=m['points'];add('changes','Find rise and run using one point order','Both differences must use the same direction.',f'Δy={y2}-({y1}); Δx={x2}-({x1})')
        add('gradient','Divide rise by run','Gradient measures vertical change per horizontal unit.',f'm={m["gradient"]}')
    elif t in ('plot_quadratic','plot_advanced'):
        add('points','Plot each input-output pair','Use one consistent coordinate scale for the full table.',coords(list(zip(m['x'],m['y']))))
        add('curve','Join the points with the appropriate smooth curve','A polynomial is continuous; a reciprocal has separate branches and must not be joined across its undefined input.', 'A smooth parabola.' if t=='plot_quadratic' else f'Smooth {m["shape"]} graph through the plotted points.')
    elif t=='sketch_quadratic':
        add('intercepts','Mark the x- and y-intercepts','At an x-intercept y=0; at the y-intercept x=0.',coords([(r,0) for r in m['roots']]+[(0,m['y_intercept'])]))
        add('vertex','Mark the turning point and sketch the parabola','The turning point sets the axis of symmetry and whether the graph opens up or down.',coords([m['turning_point']]))
    elif t=='read_quadratic_roots':add('zeros','Read the x-axis intersections','The roots are inputs where the graph has output zero.',seq(m['roots']))
    elif t=='draw_tangent':
        x=m['x0'];y=m['a']*x*x+m['k'];add('contact','Locate the specified point on the curve','The tangent must touch the curve at that point.',f'P=({x},{y})')
        add('tangent','Draw a straight line matching the local direction','A tangent follows the curve’s direction at the contact point, rather than a chord through two distant curve points.',f'Extend the line on both sides of P.')
        add('gradient','Calculate rise divided by run on the tangent','Read two well-separated points from your drawn tangent, not two points on the curve. Your gradient is an estimate.',rf'm\approx\frac{{y_2-y_1}}{{x_2-x_1}};\quad \text{{reference gradient}}={m["gradient"]}')
    elif t.startswith('draw_vector_'):
        add('components','Find the signed horizontal and vertical displacement','Vector sums add corresponding components; a single vector already supplies both displacements.',coords([m['result']]))
        add('arrow','Draw the directed segment from O','The arrowhead records direction and the endpoint records the displacement.',f'O → {coords([m["result"]])}')
    elif t in ('draw_visual_transform','describe_visual_transform'):
        reasons={'reflection':'Corresponding points lie at equal perpendicular distances on opposite sides of the mirror line.',
                 'translation':'Every corresponding vertex moves by the same signed displacement.',
                 'rotation':'Every vertex turns through the same angle about the same fixed centre.',
                 'enlargement':'Every centre-to-vertex displacement is multiplied by the same signed scale factor.'}
        add('rule','Establish the transformation and its defining information',reasons[m['shape']],m['detail'])
        add('vertices','Apply or verify the rule at all three vertices','A single matching vertex is insufficient to determine the whole transformation.',coords(m['image']))
    elif t in ('read_bearing','draw_bearing'):
        add('north','Locate north at the starting point','A bearing starts at the north ray of its starting point.','Use the north line through A.')
        add('clockwise','Measure clockwise from north','Bearings use clockwise angles and three-digit notation.',f'{m["bearing"]:03d}°')
    elif t in ('draw_bar','read_bar'):
        if t=='draw_bar':
            add('heights','Assign each frequency to its category','Bar height represents frequency on a common zero-based scale.',seq(m['counts']))
            add('bars','Draw separated bars of equal width','Categories are distinct rather than continuous measurement intervals.','Label A, B and C and the frequency scale.')
        else:
            j=m['selected'];add('read','Read the requested bar against the scale','Use the bar’s height, including intermediate scale ticks.',f'{chr(65+j)}: {m["counts"][j]}')
            add('compare','Compare all bar heights','The tallest bar represents the largest frequency.',f'Largest: {chr(65+m["counts"].index(max(m["counts"])))}')
    elif t=='draw_pie':
        total=sum(m['counts']);add('total','Find the complete frequency','All categories partition the complete circle.',f'Total={total}')
        for j,(count,angle) in enumerate(zip(m['counts'],m['angles'])):
            add('sector_'+str(j),'Calculate the next sector angle','Each category occupies its frequency fraction of 360°.',rf'\text{{{chr(65+j)}}}: \frac{{{count}}}{{{total}}}\times360^\circ={angle}^\circ')
        add('draw','Draw and label consecutive sectors','Their angles total one full turn without overlap or gaps.','Use the calculated angles and a clear category key.')
    elif t in ('draw_pictogram','read_pictogram'):
        if t=='draw_pictogram':
            add('key','Convert frequencies to symbol counts','Divide each frequency by the value of one whole symbol.',f'One symbol={m["unit"]}; counts '+seq([Fraction(x,2) for x in m['half_symbols']]))
            add('symbols','Draw the corresponding whole and half symbols','Consistent symbol size and an explicit key preserve proportional counts.','Label all categories; use a clearly divided symbol for each half.')
        else:
            j=m['selected'];h=m['half_symbols'][j];add('symbols','Count whole-symbol equivalents','Two half-symbols equal one complete symbol.',q(Fraction(h,2)))
            add('key','Multiply by the key','Each complete symbol represents the stated number of learners.',f'{q(Fraction(h,2))}×{m["unit"]}={m["counts"][j]} learners')
    elif t in ('draw_histogram','read_histogram'):
        for j,(w,d,freq) in enumerate(zip(m['widths'],m['densities'],m['frequencies'])):
            expression=rf'\frac{{{freq}}}{{{w}}}={d}' if t=='draw_histogram' else f'{w}×{d}={freq}'
            add('class_'+str(j),'Calculate the next class density' if t=='draw_histogram' else 'Recover the next class frequency',
                'Histogram area, not height alone, represents frequency.',f'Class {m["edges"][j]} to {m["edges"][j+1]}: {expression}')
        if t=='draw_histogram':add('bars','Draw bars across their actual class intervals','Continuous adjacent intervals touch; widths must remain proportional to the class widths.','Use the calculated density heights and label both axes.')
    elif t=='draw_cumulative':
        add('totals','Accumulate class frequencies in order','Each cumulative total counts all observations below the next upper boundary.',seq(m['cumulative']))
        add('plot','Plot totals at upper class boundaries','A cumulative graph starts at zero at the initial lower boundary.',coords(list(zip(m['edges'],m['cumulative']))))
        add('join','Join in increasing boundary order','Cumulative totals cannot decrease; ruled joins are accepted in this task.','Label both scales and retain every plotted point.')
    elif t=='read_cumulative':
        total=m['cumulative'][-1];add('positions','Locate the three quartile frequency levels','Quartiles divide the observation count into four equal parts.',f'N/4={total/4:g}; N/2={total/2:g}; 3N/4={3*total/4:g}')
        add('read','Read across to the graph and then down','The time-axis readings, not the frequency positions, are the quartile values.',f'Q1≈{m["q1"]:.2f}, median≈{m["median"]:.2f}, Q3≈{m["q3"]:.2f} minutes')
        add('iqr','Subtract the lower quartile from the upper','The interquartile range measures the spread of the middle half of the data.',f'IQR≈{m["q3"]:.2f}−{m["q1"]:.2f}≈{m["q3"]-m["q1"]:.2f} minutes; allow consistent rounded graph readings.')
    elif t=='possibility_diagram':
        add('pairs','Select ordered pairs satisfying the event','Reversed unequal outcomes are distinct elementary outcomes.',coords(m['selected']))
        add('probability','Divide favourable outcomes by all equally likely pairs','Each of the two independent devices has the stated number of outcomes.',rf'\frac{{{len(m["selected"])}}}{{{m["sides"]**2}}}={q(Fraction(m["probability"]))}')
    elif t=='complete_tree':
        r,b=m['red'],m['blue'];N=r+b
        add('first','Form first-draw probabilities','The first denominator is the original total.',rf'R: \frac{{{r}}}{{{N}}}; B: \frac{{{b}}}{{{N}}}')
        add('after_red','Update counts after removing red','Without replacement there is one fewer counter and one fewer red.',rf'R: \frac{{{r-1}}}{{{N-1}}}; B: \frac{{{b}}}{{{N-1}}}')
        add('after_blue','Update counts after removing blue','This branch removes blue instead, so only the blue count decreases.',rf'R: \frac{{{r}}}{{{N-1}}}; B: \frac{{{b-1}}}{{{N-1}}}')
    elif t=='read_tree':
        r,b=m['red'],m['blue'];N=r+b
        add('RB','Multiply along the red-then-blue path','Sequential conditional probabilities multiply along a path.',rf'P(RB)=\frac{{{r}}}{{{N}}}\times\frac{{{b}}}{{{N-1}}}')
        add('BR','Multiply along the blue-then-red path','The reversed colour order is another qualifying path.',rf'P(BR)=\frac{{{b}}}{{{N}}}\times\frac{{{r}}}{{{N-1}}}')
        add('sum','Add the two disjoint path probabilities','Either order satisfies the event and both cannot occur in the same two-draw outcome.',rf'P(RB)+P(BR)={q(Fraction(m["probability"]))}')
    else:raise ValueError(f'Missing visual solution plan: {f}/{t}')
    return a.finish()
