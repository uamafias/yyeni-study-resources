"""Original geometry, construction and measurement recipes."""
from copy import deepcopy
from fractions import Fraction
import math
import random
from .core import calc, part, question, step, significant, fmt
from .diagrams import calibrated, asset, cartesian, circle, line, polygon, rect, spec, text

def build_cube_and_prism_measures(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    a, b, c = (rng.randint(2, 5), rng.randint(6, 9), rng.randint(10, 14))
    q('cube-and-prism-measures', ['4main.1'], 'Prisms', f'A right triangular prism has a right-angled triangular cross-section with perpendicular sides {3 * a} cm and {4 * a} cm. Its length is {b} cm.', [calc('Calculate its volume.', f'{6 * a * a * b} cm³', f'½ × {3 * a} × {4 * a} × {b}', f'{6 * a * a * b} cm³'), calc('Calculate its total surface area.', f'{12 * a * a + 12 * a * b} cm²', f'2(½ × {3 * a} × {4 * a}) + ({3 * a}+{4 * a}+{5 * a}) × {b}', f'{12 * a * a + 12 * a * b} cm²', checks=[((3 * a) ** 2 + (4 * a) ** 2 == (5 * a) ** 2, 'Triangular prism cross-section checked using Pythagoras')]), calc(f'A cube has side {a} cm. Calculate its surface area and volume.', f'{6 * a * a} cm²; {a ** 3} cm³', f'6 × {a}²; {a}³', f'{6 * a * a} cm²; {a ** 3} cm³')])
    return out

def build_sphere_cone_pyramid_measures(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    r = rng.randint(2, 20)
    side = 2 * r
    height = 3 * r
    slant = math.sqrt(height ** 2 + r ** 2)
    q('sphere-cone-pyramid-measures', ['4main.3'], 'Surface area and volume', 'Use the following formulae: sphere surface area $4\\pi r^2$, sphere volume $\\frac43\\pi r^3$; cone total surface area $\\pi r^2+\\pi rl$, cone volume $\\frac13\\pi r^2h$; pyramid volume $\\frac13Ah$, and regular pyramid surface area $A+\\frac12pl$. Here $l$ is slant height, $A$ is base area and $p$ is base perimeter.', [calc(f'A sphere has radius {r} cm. Find its surface area and volume in terms of π.', f'{4 * r * r}\\pi\\text{{ cm}}^2;\\ {fmt(Fraction(4 * r ** 3, 3))}\\pi\\text{{ cm}}^3', f'4π × {r}²; 4π × {r}³ ÷ 3', f'{4 * r * r}\\pi;\\ {4 * r ** 3}\\pi/3'), calc(f'A cone has radius {r} cm and vertical height {height} cm. Calculate its total surface area to 3 significant figures.', significant(math.pi * r * (r + slant)) + ' cm²', f'l = √({r}²+{height}²); area = π × {r} × ({r}+l)', significant(math.pi * r * (r + slant)) + ' cm²'), calc(f'A square-based pyramid has base side {side} cm and vertical height {height} cm. Calculate its volume.', f'{side * side * height / 3:g} cm³', f'⅓ × {side}² × {height}', f'{side * side * height / 3:g} cm³'), calc(f'The same pyramid is regular. Calculate its total surface area to 3 significant figures.', significant(side * side + 2 * side * math.sqrt(height * height + (side / 2) ** 2)) + ' cm²', f'l = √({height}² + ({side}/2)²); area = {side}² + ½ × {4 * side} × l', significant(side * side + 2 * side * math.sqrt(height * height + (side / 2) ** 2)) + ' cm²', reason='Use the face slant height, whose right triangle reaches the midpoint of a base side, then add all four triangular faces and the square base.')])
    return out

def build_geometrical_language(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    angle = rng.choice([30, 45, 60, 120, 135, 150])
    turns = rng.choice([90, 180, 270])
    q('geometrical-language', ['5a.1'], 'Geometrical terms', 'Answer each question using the appropriate geometrical term or relationship.', [part(f'Classify an angle of {angle}° and state the size of a right angle.', f"{('acute' if angle < 90 else 'obtuse')}; 90°", [step('Compare the angle with 90° and 180°', 'An acute angle is below 90°; an obtuse angle is between 90° and 180°.', f"{('acute' if angle < 90 else 'obtuse')}; right angle = 90°")], 2, [(1, 'Correct classification.'), (1, 'Right angle is 90°.')]), part(f'A turn measures {360 - angle}°. Classify this angle.', 'reflex', [step('Compare with a straight angle and a full turn', 'A reflex angle is between 180° and 360°.', 'Reflex')]), part('Two distinct straight lines meet at a point. Name this point. What term describes lines meeting at 90°?', 'Point of intersection; perpendicular lines', [step('Identify the two relationships', 'Intersecting lines share a point; perpendicular lines meet at a right angle.', 'Intersection; perpendicular')], 2, [(1, 'Intersection.'), (1, 'Perpendicular.')]), part('What term describes two straight lines in the same plane that never meet?', 'Parallel', [step('Use the defining property', 'Distinct coplanar straight lines with no intersection are parallel.', 'Parallel')]), part(f'A direction is {turns}° clockwise from north. Write its three-figure bearing.', f'{turns:03d}°', [step('Use the north reference and clockwise direction', 'A bearing has three digits before any decimal part.', f'{turns:03d}°')])])
    return out

def build_similarity_and_congruence(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    k = rng.randint(2, 30)
    q('similarity-and-congruence', ['5a.4', '5a.1'], 'Comparing triangles', f'Triangle $ABC$ has sides $AB=3$ cm, $BC=4$ cm and $AC=5$ cm. Triangle $PQR$ has $PQ={3 * k}$ cm, $QR={4 * k}$ cm and $PR={5 * k}$ cm.', [part('State whether the triangles are similar. Give a reason.', f'Yes. Corresponding side ratios are all {k}.', [step('Compare corresponding sides', 'Equal ratios of all three corresponding sides establish similarity.', f'{3 * k}/3 = {4 * k}/4 = {5 * k}/5 = {k}')], 2, [(1, 'Correct similarity conclusion.'), (1, 'Equal corresponding side ratios as reason.')]), part('State whether the triangles are congruent. Give a reason.', 'No. Corresponding side lengths are different.', [step('Compare sizes', 'Congruent figures have the same shape and size; a scale factor other than 1 changes size.', f'The scale factor is {k}, not 1.')], 2, [(1, 'Not congruent.'), (1, 'Valid size reason.')]), part('Triangle XYZ has XY = 3 cm, YZ = 4 cm and XZ = 5 cm. Explain why it is congruent to ABC.', 'The three corresponding sides are equal (SSS).', [step('Match three side pairs', 'Three equal corresponding side lengths determine congruent triangles.', 'XY = AB, YZ = BC, XZ = AC')])])
    return out

def build_plane_figure_vocabulary(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    a, b, c = (rng.randint(2, 5), rng.randint(6, 9), rng.randint(10, 14))
    sides = rng.choice([5, 6, 8])
    name = {5: 'pentagon', 6: 'hexagon', 8: 'octagon'}[sides]
    q('plane-figure-vocabulary', ['5a.2'], 'Plane figures', f'A designer draws figures on paper. One rectangle has length {b} cm and width {a} cm.', [part('Name a triangle with three equal sides and a triangle with two equal sides.', 'Equilateral; isosceles', [step('Use side-equality definitions', 'The names distinguish three equal sides from at least two.', 'Equilateral; isosceles')], 2, [(1, 'Equilateral.'), (1, 'Isosceles.')]), part('Name a quadrilateral with both pairs of opposite sides parallel. Give two special examples.', 'Parallelogram; for example rectangle and rhombus (or square).', [step('Identify the parallel-side condition', 'Rectangles, rhombi and squares are special parallelograms.', 'Parallelogram; rectangle; rhombus')], 2, [(1, 'Parallelogram.'), (1, 'Two valid special examples.')]), part('Name a quadrilateral with exactly one pair of parallel sides.', 'Trapezium', [step('Count parallel side pairs', 'Exactly one parallel pair gives a trapezium.', 'Trapezium')]), part('In a circle, name a line segment from the centre to the circumference, a chord through the centre, and a straight line touching the circle once.', 'Radius; diameter; tangent', [step('Use each relationship with the circle', 'A radius joins centre to circumference; a diameter passes through the centre; a tangent touches at one point.', 'Radius; diameter; tangent')], 3, [(1, 'Radius.'), (1, 'Diameter.'), (1, 'Tangent.')]), part(f'Name a polygon with {sides} sides.', name, [step('Count the sides', 'Polygon names depend on the side count.', name)])])
    return out

def build_solid_figure_vocabulary(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    a, b, c = (rng.randint(2, 5), rng.randint(6, 9), rng.randint(10, 14))
    q('solid-figure-vocabulary', ['5a.3'], 'Solid figures', f'One of the solids described below has edge length {a} cm. Name each solid.', [part('It has six equal square faces.', 'Cube', [step('Identify the face pattern', 'Six congruent square faces form a cube.', 'Cube')]), part(f'It has six rectangular faces and dimensions {a} cm, {b} cm and {c} cm.', 'Cuboid', [step('Use the rectangular faces', 'A rectangular prism is a cuboid.', 'Cuboid')]), part('It has two congruent, parallel triangular faces and three rectangular faces.', 'Triangular prism', [step('Identify the repeated cross-section', 'A prism has congruent parallel ends and a constant cross-section.', 'Triangular prism')]), part('It has two equal circular ends and a curved surface.', 'Cylinder', [step('Identify circular parallel ends', 'A cylinder has two congruent circular ends joined by a curved surface.', 'Cylinder')]), part('It has one circular base and one vertex.', 'Cone', [step('Identify the base and vertex', 'The curved surface joins the circular base to a single vertex.', 'Cone')]), part('It has a square base and four triangular faces meeting at one vertex.', 'Square-based pyramid', [step('Identify the common apex', 'A pyramid has triangular side faces meeting above its polygonal base.', 'Square-based pyramid')])])
    return out

def build_instrument_measurements(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    length = rng.randint(35, 85)
    theta = rng.choice(range(25, 156, 5))
    O = (60, 30)
    rays = [line(O, (100, 30)), line(O, (60 + 40 * math.cos(math.radians(theta)), 30 + 40 * math.sin(math.radians(theta))))]
    drawing = spec(140, 90, [line((20, 12), (20 + length, 12)), text((18, 8), 'A'), text((21 + length, 8), 'B'), *rays, text((56, 25), 'O'), text((102, 29), 'X'), text((60 + 43 * math.cos(math.radians(theta)), 30 + 43 * math.sin(math.radians(theta))), 'Y')])
    solution = deepcopy(drawing)
    solution['commands'] += [text((20, 17), f'AB = {length / 10:g} cm'), text((62+17*math.cos(math.radians(theta/2)),30+17*math.sin(math.radians(theta/2))), f'{theta}°')]
    q('instrument-measurements', ['5b.1'], 'Measuring with instruments', 'Print the measurement diagram at 100% / actual size. Do not measure the screen.', [part('Measure AB in centimetres, to the nearest millimetre.', f'{length / 10:g} cm (allow ±0.1 cm)', [step('Align the ruler zero with A', 'Use the printed physical scale rather than the on-screen size.', f'AB = {length / 10:g} cm')], 1, [(1, 'Measurement within 1 mm of the printed length.')]), part('Measure angle XOY using a protractor.', f'{theta}° (allow ±1°)', [step('Align the protractor baseline with OX', 'Read the interior angle from OX to OY.', f'{theta}°')], 1, [(1, 'Angle within 1° of the printed angle.')])], assets=[asset('measurement', drawing, solution, physical=True)])
    return out

def build_constructing_nets(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    L, W, H = (rng.randint(2, 4), rng.randint(2, 3), rng.randint(2, 5))
    x, y = (10, 10 + 10 * W)
    net = []
    for w in [L, W, L, W]:
        net.append(rect(x, y, 10 * w, 10 * H))
        x += 10 * w
    net += [rect(10, y + 10 * H, 10 * L, 10 * W), rect(10, y - 10 * W, 10 * L, 10 * W)]
    net += [text((12, y+10*H+10*W/2), f'{L} cm × {W} cm',size=2.5), text((12,y+10*H/2),f'{L} cm × {H} cm',size=2.5),text((12+10*L,y+10*H/2),f'{W} cm × {H} cm',size=2.5)]
    netdiagram = spec(20 + 20 * (L + W), 20 + 10 * (H + 2 * W), net)
    q('constructing-nets', ['5b.2', '5a.3'], 'Nets of solids', f'A {"cube" if L==W==H else "cuboid"} has dimensions {L} cm by {W} cm by {H} cm.', [part('Draw an accurate net of the cuboid. Label its dimensions.', 'Any valid connected net with the correct six rectangular faces and dimensions.', [step('Identify the faces', 'A cuboid has two faces of each pair of dimensions.', f'Two {L}×{W}, two {L}×{H}, two {W}×{H} rectangles.'), step('Arrange a connected net', 'The faces must fold into the solid without overlapping.', 'A band of four side faces with the remaining faces attached in compatible positions.')], 3, [(1, 'Six correct faces.'), (1, 'Valid foldable arrangement.'), (1, 'Correct lengths and labels.')]), part(f'A right triangular prism has cross-section sides 3 cm, 4 cm and 5 cm and length {H} cm. Draw a net of this prism.', f'Two congruent 3–4–5 triangles and rectangles 3×{H}, 4×{H}, 5×{H}, in a valid foldable arrangement.', [step('Identify the end and lateral faces', 'The prism has two identical triangular ends and a rectangle for each cross-section side.', f'Two 3–4–5 triangles; rectangles 3×{H}, 4×{H}, 5×{H}.'), step('Arrange the faces', 'Each triangular end must meet the appropriate edges of the rectangular band.', 'Any valid net with the correct dimensions.')], 3, [(1, 'Two correct triangular ends.'), (1, 'Three correct lateral rectangles.'), (1, 'Valid accurately dimensioned net.')])], assets=[{'asset_id':'cuboid-net-reference','role':'solution_only','solution_diagram':calibrated(netdiagram),'print_at_actual_size':True,'display_instruction':'Reference solution only. Print at actual size for centimetre measurements.'}])
    return out

def build_irregular_symmetry(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    u, w = (rng.randint(2, 5), rng.randint(1, 3))
    graph, point = cartesian(-6, 6, -4, 5)
    vertices = [(-u, 0), (0, 4), (u, 0), (0, -w)]
    graph['commands'].append(polygon([point(*p) for p in vertices]))
    sol = deepcopy(graph)
    sol['commands'].append(line(point(0, -3), point(0, 5), dash=True, color='#006633'))
    q('irregular-symmetry', ['5c.1'], 'Symmetry of a kite', 'The diagram shows a kite on a coordinate grid.', [part('Copy the kite and draw every line of symmetry.', 'One line of symmetry, x = 0.', [step('Reflect matching vertices', 'The left and right vertices match across the vertical diagonal; the top and bottom are different distances from the horizontal diagonal.', 'The only axis is x = 0.')]), part('State its order of rotational symmetry.', '1', [step('Test rotations less than a full turn', 'The unequal top and bottom portions prevent a half-turn symmetry.', 'Order 1')])], assets=[asset('kite', graph, sol)])
    return out

def build_symmetry_properties(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    bhalf = rng.randint(2, 20)
    equal = bhalf + 2
    q('symmetry-properties', ['5c.2'], 'Using symmetry', f'Triangle $ABC$ has $AB=AC={equal}$ cm and $BC={2 * bhalf}$ cm. $M$ is the midpoint of $BC$.', [calc('Find BM.', f'{bhalf} cm', f'{2 * bhalf} ÷ 2', f'{bhalf} cm', marks=1), part('State angle AMB and explain your answer using symmetry.', '90°. AM is the axis of symmetry and is perpendicular to BC.', [step('Use the isosceles triangle symmetry', 'The line from the apex to the midpoint of the base is a reflection axis and perpendicular bisector.', 'Angle AMB = 90°')], 2, [(1, '90°.'), (1, 'Valid symmetry reason.')]), part('A rhombus has diagonals AC and BD meeting at O. State two facts about the diagonals arising from its symmetry.', 'They bisect each other and meet at right angles (also accept that they bisect the vertex angles).', [step('Use the rhombus reflection axes', 'The diagonals are symmetry axes; corresponding halves are equal and the axes are perpendicular.', 'AO = OC, BO = OD and angle AOB = 90°')], 2, [(1, 'One valid symmetry fact.'), (1, 'A second distinct valid symmetry fact.')])])
    return out

def build_angle_reasons(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    alpha = rng.randint(35, 75)
    beta = rng.randint(65, 115)
    q('angle-reasons', ['5d.1'], 'Angles and reasons', 'Lines AB and CD are parallel. A transversal crosses them at P and Q. A pair of corresponding angles is labelled x and y.', [part(f'If x = {alpha}°, find y and give a reason.', f'{alpha}°, corresponding angles on parallel lines are equal.', [step('Identify corresponding positions', 'A transversal makes equal corresponding angles with parallel lines.', f'y = {alpha}°')], 2, [(1, 'Correct angle.'), (1, 'Corresponding-angle reason.')]), part(f'PQRS is a cyclic quadrilateral. Angle PQR is {beta}°. Calculate angle PSR and give a reason.', f'{180 - beta}°, opposite angles in a cyclic quadrilateral sum to 180°.', [step('Use the cyclic quadrilateral relationship', 'Opposite angles are supplementary.', f'angle PSR = 180° − {beta}° = {180 - beta}°')], 2, [(1, 'Correct angle.'), (1, 'Valid cyclic-angle reason.')])])
    return out

def build_intersecting_loci(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    p = rng.randint(2, 4)
    radius = rng.randint(5, 8)
    disc = math.sqrt(2 * radius ** 2 - p * p)
    intersections = [((p + sgn * disc) / 2, (p + sgn * disc) / 2) for sgn in (-1, 1)] + [((-p + sgn * disc) / 2, -(-p + sgn * disc) / 2) for sgn in (-1, 1)]
    graph, point = cartesian(-10, 10, -8, 12, width=150, height=150)
    graph['commands'] += [circle(point(0, p), 0.8, fill='black'), text((point(0, p)[0] + 2, point(0, p)[1] + 2), 'P')]
    sol = deepcopy(graph)
    sol['commands'] += [line(point(-8, -8), point(10, 10), color='#006633'), line(point(-10, 10), point(8, -8), color='#006633')]
    unit = (150 - 24) / 20
    sol['commands'].append(circle(point(0, p), radius * unit, color='#006633'))
    for xy in intersections:
        sol['commands'].append(circle(point(*xy),1,fill='#006633'))
    # Only solution labels may react to solution geometry. Never alter the
    # question's axis markings using undisclosed answer positions.
    for command in sol['commands']:
        if command['kind']!='text' or not command['value'].lstrip('-').isdigit():continue
        original=command['p']
        if abs(math.dist(original,point(0,p))-radius*unit)<3:
            command['p']=max([(original[0]+dx,original[1]+dy) for dx,dy in ((0,3),(0,-3),(-3,0),(3,0))],key=lambda v:abs(math.dist(v,point(0,p))-radius*unit))
    q('intersecting-loci', ['5e.1'], 'Intersecting loci', f'The coordinate axes are two perpendicular lines. $P=(0,{p})$. A point $X$ is equidistant from the two axes and is {radius} coordinate units from P.', [part('Copy the diagram and construct the locus of points equidistant from the two axes.', 'Both angle-bisector lines y = x and y = −x.', [step('Use the angle-bisector locus', 'Points equidistant from intersecting lines lie on both angle bisectors.', 'Draw y = x and y = −x.')], 2, [(1, 'One complete correct angle bisector.'), (1, 'Both angle bisectors with no extra locus.')]), part(f'Construct the locus of points {radius} units from P.', f'A circle with centre (0,{p}) and radius {radius}.', [step('Use the fixed-distance locus', 'A fixed distance from one point gives a circle.', f'Centre (0,{p}); radius {radius}.')]), part('Mark every possible position of X.', '; '.join((f'({x:.2f},{y:.2f})' for x, y in intersections)), [step('Mark the intersections on both bisectors','A point must lie on one of the two bisectors and on the circle. The drawing is the assessed method; the calculations below verify the readings.',r'x^2+(y-'+str(p)+r')^2='+str(radius**2)),
        step('Check the two points on y = x','Substitute y = x in the circle equation and solve the resulting quadratic.',rf'2x^2-{2*p}x+({p*p-radius*radius})=0;\quad '+ '; '.join(f'(x,y)=({x:.2f},{y:.2f})' for x,y in intersections[:2])),
        step('Check the two points on y = -x','Substitute y = -x in the circle equation. This gives the intersections on the other angle bisector.',rf'2x^2+{2*p}x+({p*p-radius*radius})=0;\quad '+ '; '.join(f'(x,y)=({x:.2f},{y:.2f})' for x,y in intersections[2:]))],2,[(1,'Both correct intersections on one bisector, allowing ±0.2 coordinate units per reading; algebra is not required.'),(1,'All four correct intersections and no extra points, allowing ±0.2 coordinate units per reading; accept accurate marked drawings.')], checks=[(all((abs(abs(x) - abs(y)) < 1e-08 and abs(x * x + (y - p) ** 2 - radius ** 2) < 1e-08 for x, y in intersections)), 'Every reference point satisfies both distance conditions')])], assets=[asset('loci', graph, sol)])
    return out

def build_make_scale_drawing(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    AB = rng.choice([60, 70, 80, 90])
    AC = rng.choice([50, 60, 70])
    theta = rng.choice([40, 50, 60, 70])
    BC = math.sqrt(AB ** 2 + AC ** 2 - 2 * AB * AC * math.cos(math.radians(theta)))
    q('make-scale-drawing', ['5b.4', '1j.4'], 'A scale drawing', f'Two paths AB and AC leave A at an angle of {theta}°. AB is {AB} m long and AC is {AC} m long. Use a scale of 1 cm to 20 m.', [part('Make an accurate scale drawing of triangle ABC.', f'AB = {AB / 20:g} cm; AC = {AC / 20:g} cm; included angle {theta}°.', [step('Convert actual lengths to drawing lengths', 'At this scale, divide metres by 20 to obtain centimetres.', f'AB = {AB / 20:g} cm and AC = {AC / 20:g} cm.'), step('Construct the triangle', 'The included angle locates C relative to AB.', f'Draw the {theta}° angle at A and join B to C.')], 3, [(1, 'Correct scale lengths.'), (1, 'Correct included angle.'), (1, 'Accurate completed triangle.')]), part('Measure BC on your drawing and estimate its actual length, to the nearest metre.', f'About {BC:.0f} m; allow ±2 m for an accurate drawing.', [step('Measure the third side', 'The required length is read from the constructed triangle.', f'BC is about {BC / 20:.2f} cm.'), step('Apply the scale', 'Each centimetre represents 20 m.', f'BC is about {BC:.0f} m.')], 2, [(1, 'A consistent drawing measurement.'), (1, 'Correct scale conversion, allowing reasonable drawing tolerance.')])])
    return out

def build_line_plane_angle(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    a = 3 * rng.randint(1, 10)
    h = 4 * rng.randint(1, 10)
    depth = 4 * a / 3
    diag = 5 * a / 3
    space = math.sqrt(diag ** 2 + h ** 2)
    angle = math.degrees(math.atan(h / diag))
    q('line-plane-angle', ['11main.6'], 'A cuboid in three dimensions', f'In cuboid ABCDEFGH, ABCD is the horizontal base. E, F, G and H are vertically above A, B, C and D respectively. AB = {a:g} cm, BC = {depth:g} cm and CG = {h:g} cm.', [calc('Calculate AC.', f'{diag:g} cm', f'AC = √({a:g}² + {depth:g}²)', f'{diag:g} cm'), calc('Calculate AG to 3 significant figures.', significant(space) + ' cm', f'AG = √({diag:g}² + {h:g}²)', significant(space) + ' cm'), calc('Calculate the angle between AG and the base plane ABCD.', f'{angle:.1f}°', f'tan(angle GAC) = {h:g}/{diag:g}', f'{angle:.1f}°', reason='AC is the projection of AG onto the horizontal base, so angle GAC is the line-plane angle.')])
    return out
BUILDERS = [build_cube_and_prism_measures, build_sphere_cone_pyramid_measures, build_geometrical_language, build_similarity_and_congruence, build_plane_figure_vocabulary, build_solid_figure_vocabulary, build_instrument_measurements, build_constructing_nets, build_irregular_symmetry, build_symmetry_properties, build_angle_reasons, build_intersecting_loci, build_make_scale_drawing, build_line_plane_angle]

def build(v, rng=None):
    rng = rng or random.Random(v)
    return [q for builder in BUILDERS for q in builder(v, rng)]
