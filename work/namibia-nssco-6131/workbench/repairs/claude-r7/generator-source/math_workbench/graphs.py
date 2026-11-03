"""Seeded complete graphical questions with instance-bound diagrams."""
from copy import deepcopy
from fractions import Fraction as F
import math
import random
from .core import calc, fmt, part, question, step, polynomial, coordinates
from .diagrams import asset, cartesian, circle, line, polygon, polyline, rect, spec, text

def build_conversion_graph(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    graph, pt = cartesian(0, 16, 0, 10, width=155, height=110, xstep=2, ystep=1)
    graph['commands'] += [line(pt(0, 0), pt(16, 10)), text((60, 3), 'Distance in kilometres'), text((14, 103), 'Distance in miles')]
    km = rng.choice([4.8, 6.4, 8.8, 10.4, 12.8])
    mi = rng.choice([2.5, 3.5, 4.5, 5.5, 6.5])
    q('conversion-graph', ['7a.2'], 'A conversion graph', 'The graph uses the approximate conversion 1 mile = 1.6 kilometres. Use the graph for both answers.', [part(f'Estimate the number of miles equivalent to {km:g} km.', f'{km / 1.6:g} miles (allow ±0.1 mile)', [step('Read across from the kilometre value', 'The graph links corresponding kilometre and mile distances.', f'{km:g} km corresponds to about {km / 1.6:g} miles.')]), part(f'Estimate the number of kilometres equivalent to {mi:g} miles.', f'{mi * 1.6:g} km (allow ±0.2 km)', [step('Read from the mile value to the line and then to the kilometre axis', 'The same conversion line can be read in either direction.', f'{mi:g} miles corresponds to about {mi * 1.6:g} km.')])], assets=[asset('conversion', graph)])
    return out

def build_household_spending_chart(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    amounts = [50 * rng.randint(3, 10) for _ in range(4)]
    labels = ['Food', 'Water', 'Electricity', 'Transport']
    chart = spec(150, 110, [text((45, 103), 'Monthly household spending (N$)')])
    for y in range(0, 601, 100):
        chart['commands'] += [line((20, 15 + y * 0.12), (140, 15 + y * 0.12), color='#dddddd'), text((7, 14 + y * 0.12), y)]
    for i, (label, n) in enumerate(zip(labels, amounts)):
        x = 27 + 27 * i
        chart['commands'] += [rect(x, 15, 14, n * 0.12, fill='#cccccc'), text((x - 3, 7), label, size=2.5)]
    q('household-spending-chart', ['1l.3', '12a.2'], 'Reading a budget chart', 'The bar chart shows one household’s spending in one month.', [part('Read the amount spent on food.', f'N${amounts[0]}', [step('Read the height of the food bar', 'The vertical scale is measured in Namibian dollars.', f'N${amounts[0]}')]), calc('Calculate the total shown.', f'N${sum(amounts)}', ' + '.join(map(str, amounts)), f'N${sum(amounts)}', reason='Add the four non-overlapping spending categories read from the chart.'), calc('Express the water spending as a percentage of this total, to 1 decimal place.', f'{100 * amounts[1] / sum(amounts):.1f}%', f'{amounts[1]} ÷ {sum(amounts)} × 100%', f'{100 * amounts[1] / sum(amounts):.1f}%', reason='Compare the water amount with the whole budget shown, then express that fraction per hundred.')], assets=[asset('budget', chart)])
    return out

def build_reading_calibrated_dial(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    reading = 2 * rng.randint(5, 45)
    center = (65, 25)
    radius = 38
    dial = spec(130, 85, [text((38, 75), 'Pressure in kPa')])
    arc = []
    for value in range(101):
        ang = math.radians(180 - 1.8 * value)
        arc.append((center[0] + radius * math.cos(ang), center[1] + radius * math.sin(ang)))
    dial['commands'].append(polyline(arc))
    for value in range(0, 101, 2):
        ang = math.radians(180 - 1.8 * value)
        rr = radius - (5 if value % 10 == 0 else 2)
        dial['commands'].append(line((center[0] + rr * math.cos(ang), center[1] + rr * math.sin(ang)), (center[0] + radius * math.cos(ang), center[1] + radius * math.sin(ang))))
        if value % 10 == 0:
            dial['commands'].append(text((center[0] + (radius + 7) * math.cos(ang) - 2, center[1] + (radius + 7) * math.sin(ang) - 1), value, size=2.5))
    ang = math.radians(180 - 1.8 * reading)
    dial['commands'] += [line(center, (center[0] + 32 * math.cos(ang), center[1] + 32 * math.sin(ang))), circle(center, 1, fill='black')]
    q('reading-calibrated-dial', ['3main.4'], 'Reading a dial', 'The dial measures pressure. Adjacent small divisions represent 2 kPa.', [part('Write down the pressure shown.', f'{reading} kPa', [step('Count divisions from a numbered mark', 'Each minor division adds 2 kPa.', f'{reading} kPa')])], assets=[asset('dial', dial)], paper='short_answer')
    return out

def build_complete_linear_programme(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    r = rng.randint(4, 8)
    s = rng.randint(1, r - 1)
    n = r + s
    m = 2 * r
    a, b = (rng.randint(2, 8), rng.randint(3, 12))
    vertices = [(0, 0), (n, 0), (2 * s, r - s), (0, r)]
    values = [a * x + b * y for x, y in vertices]
    best = max(values)
    bestpt = vertices[values.index(best)]
    blank, pt = cartesian(0, 2 * r + 1, 0, 2 * r + 1, width=140, height=140)
    sol = deepcopy(blank)
    edge = 2 * r + 1
    sol['commands'] += [polygon([pt(*xy) for xy in [(n, 0), (edge, 0), (edge, edge), (0, edge), (0, n)]], fill='#eeeeee'), polygon([pt(*xy) for xy in [(m, 0), (edge, 0), (edge, edge), (0, edge), (0, m / 2)]], fill='#dddddd'), text(pt(1, 1), 'R')]
    sol['commands'] += [line(pt(n, 0), pt(0, n)), line(pt(m, 0), pt(0, m / 2)), polyline([pt(*p) for p in vertices + [vertices[0]]], color='#006633')]
    sol['commands'] += [deepcopy(c) for c in blank['commands'] if c['kind']=='text' and c['value'] in ('x','y')]
    q('complete-linear-programme', ['7b.1'], 'Production planning', f'A factory produces $x$ tonnes of one blend and $y$ tonnes of another. Its constraints are $x\\ge0$, $y\\ge0$, $x+y\\le {n}$ and $x+2y\\le {m}$. The profit, in thousands of Namibian dollars, is $P={a}x+{b}y$.', [part('Draw the boundary lines on a coordinate grid. Shade the unwanted regions and label the feasible region R.', f'Feasible vertices: {coordinates(vertices)}. All boundaries are solid.', [step('Plot the boundary equations', 'Each equality gives an edge of a permitted half-plane.', f'x=0, y=0, x+y={n}, x+2y={m}'), step('Identify the common region', 'A feasible point satisfies every inequality.', 'Keep the polygon whose vertices are ' + coordinates(vertices) + '.')], 3, [(1, 'Correct boundary lines.'), (1, 'Correct sides of the constraints.'), (1, 'Correct feasible region and inclusive boundaries.')]), part('Find the greatest profit and give one production plan that achieves it.', f'N${1000 * best}; x={bestpt[0]}, y={bestpt[1]}.', [step('Evaluate the objective at feasible vertices', 'A linear objective attains a maximum at a vertex or along a whole edge.', '; '.join((f'At ({x}, {y}), P = {value}' for (x, y), value in zip(vertices, values)))), step('Choose the greatest value and interpret units', 'P is measured in thousands of Namibian dollars.', f'P={best}; actual profit N${1000 * best}, at {bestpt}.')], 3, [(1, 'Relevant feasible vertices used.'), (1, 'Correct objective comparison.'), (1, 'Maximum, units and a valid achieving plan.')], checks=[(all((x >= 0 and y >= 0 and (x + y <= n) and (x + 2 * y <= m) for x, y in vertices)), 'Every candidate vertex satisfies all inequalities')])], assets=[asset('programme', blank, sol)])
    return out

def build_linear_quadratic_reciprocal_tables(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    a, b, c = (rng.randint(1, 5), rng.randint(-4, 4), rng.randint(-3, 3))
    qa = rng.choice([-3, -2, -1, 1, 2, 3])
    k = 2 * rng.randint(1, 6)
    xs = [-2, -1, 1, 2]
    table = lambda vals: ' | '.join((f'${fmt(x)}$' for x in vals))
    stem = 'Complete each table.\n\n| x | ' + table(xs) + ' |\n|---|---|---|---|---|\n| y | ? | ? | ? | ? |'
    ps = []
    for rule, vals in [(f'y={polynomial([a,b])}', [a * x + b for x in xs]), (f'y={polynomial([qa,b,c])}', [qa * x * x + b * x + c for x in xs]), (f'y=\\frac{{{k}}}x', [F(k, x) for x in xs])]:
        ps.append(part(f'For ${rule}$, give the four y-values in increasing x order.', ', '.join((fmt(x) for x in vals)), [step('Substitute each listed x', 'Evaluate the complete function rule, preserving signs and fractions.', ', '.join((fmt(x) for x in vals)))], 4, [(1, f'Correct value {i + 1}: {fmt(value)}.') for i, value in enumerate(vals)]))
    q('linear-quadratic-reciprocal-tables', ['7d.1'], 'Tables of values', stem, ps)
    return out

def build_linear_quadratic_graph_intersections(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    r1, r2 = (rng.choice([-2, -1]), rng.choice([2, 3, 4]))
    b, c = (rng.randint(-2, 2), rng.randint(-3, 3))
    slope = b + r1 + r2
    if slope == 0:
        b += 1
        slope = 1
    intercept = c - r1 * r2
    f = lambda x: x * x + b * x + c
    g = lambda x: slope * x + intercept
    xmin, xmax = (r1 - 1, r2 + 1)
    ymin = min(f(-b / 2), g(xmin), g(xmax)) - 2
    ymin = math.floor(ymin / 2) * 2
    ymax = math.ceil(max(f(xmin), f(xmax), g(xmin), g(xmax)) / 2) * 2 + 2
    blank, pt = cartesian(xmin, xmax, ymin, ymax, width=150, height=130, ystep=max(1, math.ceil((ymax - ymin) / 16)))
    sol = deepcopy(blank)
    sol['commands'] += [polyline([pt(xmin + (xmax - xmin) * i / 120, f(xmin + (xmax - xmin) * i / 120)) for i in range(121)], color='#006633'), line(pt(xmin, g(xmin)), pt(xmax, g(xmax)), color='#3333aa')]
    q('linear-quadratic-graph-intersections', ['7d.2', '7d.4'], 'Graphs and intersections', f'$f(x)={polynomial([1,b,c])}$ and $g(x)={polynomial([slope,intercept])}$. Use ${xmin}\\le x\\le {xmax}$.', [part('Draw both graphs on the same coordinate grid.', f'Quadratic f and straight line g; intersections ({r1},{f(r1)}) and ({r2},{f(r2)}).', [step('Calculate enough points for both rules', 'A smooth quadratic needs points on both sides of its turning point; the linear rule gives a straight line.', f'Quadratic turning point x={-b / 2:g}; line gradient {slope}.'), step('Plot the points and draw the graphs', 'Both functions must share one coordinate scale.', 'A smooth quadratic and a ruled straight line.')], 4, [(1, 'Sufficient correctly calculated quadratic points.'), (1, 'Accurate smooth quadratic.'), (1, 'Correct straight-line points.'), (1, 'Accurate common scales and straight line.')]), part('Use your graphs to solve f(x) = g(x).', f'x ≈ {r1} and x ≈ {r2}', [step('Locate the intersections', 'At an intersection the two functions have the same y-value.', f'x ≈ {r1} and x ≈ {r2}')], 2, [(1, 'First graphical solution.'), (1, 'Second graphical solution.')], checks=[(f(r1) == g(r1) and f(r2) == g(r2), 'Both graph intersections independently satisfy both equations')])], assets=[asset('two-graphs', blank, sol)])
    return out

def build_graphical_linear_solution(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    slope = rng.randint(2, 5)
    intercept = rng.randint(-5, 5)
    root = rng.choice([-0.5, 0.5, 1.5, 2.5])
    target = slope * root + intercept
    graph, pt = cartesian(-3, 4, -20, 25, width=140, height=130, ystep=5)
    graph['commands'].append(line(pt(-3, slope * -3 + intercept), pt(4, slope * 4 + intercept)))
    sol = deepcopy(graph)
    sol['commands'].append(line(pt(-3, target), pt(4, target), dash=True, color='#006633'))
    sol['commands'].append(line(pt(root,target),pt(root,0),dash=True,color='#006633'))
    q('graphical-linear-solution', ['7d.4'], 'Solving using a graph', f'The graph shows $y={polynomial([slope,intercept])}$.', [part(f'Use the graph to solve ${polynomial([slope,intercept])}={target:g}$. Show the reading lines used.', f'x ≈ {root:g} (allow ±0.2)', [step('Locate the required y-value', 'The equation asks where the line has height ' + f'{target:g}.', f'Draw the horizontal reading line y={target:g}.'), step('Read the corresponding x-coordinate', 'The intersection gives the solution.', f'x ≈ {root:g}')], 2, [(1, 'Correct horizontal reading line/intersection.'), (1, 'Correct graphical x-reading.')])], assets=[asset('linear-solve', graph, sol)])
    return out

def build_power_sum_exponential_graphs(seed,rng,requested_key=None):
    import numpy as np
    out=[];suffixes=['power-minus-2','power-minus-1','power-0','power-1','power-2','power-3','sum','exponential']
    cases=[suffixes.index(requested_key.removeprefix('power-sum-exponential-graphs-'))] if requested_key else range(8)
    for case in cases:
        a=F(rng.randint(1,9),rng.randint(1,3));base=rng.randint(2,5);power=[-2,-1,0,1,2,3][case] if case<6 else None
        excluded=case in (0,1,2,6)
        xs=[-3,-2,-1,1,2,3] if excluded else [-3,-2,-1,0,1,2,3]
        if case<6:
            fn=lambda x:float(a)*x**power
            exact=lambda x:a*F(x)**power
            rule='y='+ (fmt(a) if power==0 else fmt(a)+f'x^{{{power}}}')
            facet=f'power:{power}'
            if power==0:
                target=float(a if seed%2==0 else a+1);roots=[]
            else:
                chosen=-2 if seed%2 else 2;target=float(exact(chosen))
                roots=[-2.,2.] if power in (-2,2) else [float(chosen)]
        elif case==6:
            b,c=rng.randint(2,5),rng.randint(1,4)
            fn=lambda x:x*x+b*x+c/x
            exact=lambda x:F(x*x+b*x)+F(c,x)
            rule=rf'y=x^2+{b}x+\frac{{{c}}}x';facet='sum_of_three_powers';target=float(exact(2))
            roots=sorted(float(z.real) for z in np.roots([1,b,-target,c]) if abs(z.imag)<1e-8 and -3-1e-8<=z.real<=3+1e-8 and abs(z.real)>1e-8)
        else:
            fn=lambda x:base**x;exact=lambda x:F(base)**x;rule=f'y={base}^x';facet='exponential'
            target=float(f'{fn(rng.choice((1.5,2,2.5))):.3g}');roots=[math.log(target,base)]
        vals=[exact(x) for x in xs]
        low=min(0.,float(min(vals)),target);high=max(1.,float(max(vals)),target)
        raw=(high-low)/9;power10=10**math.floor(math.log10(raw));ystep=next(s*power10 for s in (1,2,2.5,5,10) if s*power10>=raw)
        ymin=math.floor((low-ystep*.2)/ystep)*ystep;ymax=math.ceil((high+ystep*.2)/ystep)*ystep
        blank,pt=cartesian(-4,4,ymin,ymax,width=170,height=140,xstep=1,ystep=ystep)
        sol=deepcopy(blank)
        intervals=[(-3,-.04),(.04,3)] if excluded else [(-3,3)]
        for lo,hi in intervals:
            points=[]
            for i in range(241):
                x=lo+(hi-lo)*i/240;y=fn(x)
                if ymin<=y<=ymax:points.append(pt(x,y))
                elif points:
                    if len(points)>1:sol['commands'].append(polyline(points,color='#006633'))
                    points=[]
            if len(points)>1:sol['commands'].append(polyline(points,color='#006633'))
        sol['commands'].append(line(pt(-3,target),pt(3,target),dash=True,color='#777777'))
        for root in roots:
            assert -3-1e-7<=root<=3+1e-7 and abs(fn(root)-target)<1e-6*max(1,abs(target))
            sol['commands'].append(line(pt(root,target),pt(root,0),dash=True,color='#777777'))
        target_text=fmt(F(str(target)))
        query=f'Use your graph to solve ${rule[2:]}={target_text}$. State all solutions in the displayed domain.'
        answer=('Every x in [-3,3] except 0.' if target==float(a) else 'No solution.') if case==2 else r'$x \approx '+', '.join(f'{x:.2f}' for x in roots)+'$ (allow ±0.2 per reading).'
        domain=r'$-3\le x\le3$'+(r', with $x\ne0$' if excluded else '')
        stem=f'The function is ${rule}$, for {domain}.'
        if case==2:stem+=f' It is equivalently $y={fmt(a)}x^0$ on this nonzero domain.'
        ps=[part('Calculate the y-values for x = '+', '.join(map(str,xs))+'.',', '.join(fmt(y) for y in vals),
            [step('Evaluate the complete rule at each input','Keep brackets around negative inputs. A negative power takes the reciprocal; zero is excluded when stated.', '; '.join(f'y({x})={fmt(y)}' for x,y in zip(xs,vals)))],len(xs),[(1,f'Correct value at x={x}: {fmt(y)}.') for x,y in zip(xs,vals)]),
            part('Draw the graph on the supplied grid.',f'Graph of {rule} on the stated domain; '+('separate branches on either side of x=0.' if excluded else 'include the negative and nonnegative inputs.'),
            [step('Plot the table points','The horizontal coordinate is the input and the vertical coordinate its output.', '; '.join(f'({x},{fmt(y)})' for x,y in zip(xs,vals))),
             step('Draw the correct curve or line','Never join across an excluded input. Keep each continuous branch separate.' if excluded else 'A linear or constant rule gives a straight line; other rules here give smooth curves.',rule)],2,[(1,'Accurate plotted points including negative inputs.'),(1,'Correct curve/line and domain, with no joining across an excluded zero.')]),
            part(query,answer,[step('Read every intersection with the target height','Every intersection of the curve and the horizontal reading line gives a solution in the stated domain.',answer)],1 if case==2 else 2,[(1,'Correct conclusion from the constant graph.')] if case==2 else [(1,'Appropriate horizontal reading line on all relevant branches.'),(1,'All and only solutions, within ±0.2 in x.')])]
        q=question('power-sum-exponential-graphs-'+suffixes[case],['7d.5','7d.6'],'A function and its graph: '+facet,stem,ps,variant=seed,assets=[asset('function',blank,sol)])
        q['structural_case']=facet;q['parameter_evidence']={'inputs':xs,'outputs':[float(v) for v in vals],'target':target,'roots':roots,'excluded_zero':excluded}
        if case==1 and a.denominator==1:
            q['objective_ids'].append('6131:7d:02');q['parts'][1]['objective_ids'].append('6131:7d:02')
        out.append(q)
    return out

BUILDERS = [build_conversion_graph, build_household_spending_chart, build_reading_calibrated_dial, build_complete_linear_programme, build_linear_quadratic_reciprocal_tables, build_linear_quadratic_graph_intersections, build_graphical_linear_solution, build_power_sum_exponential_graphs]

def build(v, rng=None):
    rng = rng or random.Random(v)
    return [q for builder in BUILDERS for q in builder(v, rng)]
