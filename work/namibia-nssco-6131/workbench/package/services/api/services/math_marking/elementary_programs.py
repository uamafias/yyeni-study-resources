"""Explicit elementary geometry and function-concept solution plans."""
from .solution_programs import Author
from .formatting_adapter import q


def elementary_program(p,content):
    f=p.generator_id.removeprefix('nssco_');m=p.machine;t=m.get('task',p.skill)
    a=Author(p,content);add=a.add;n=len(a.rows)
    if f=='bisectors_numeric':
        if t=='pythagoras':
            add('geometric_property','Find the midpoint distance','A perpendicular bisector meets AB at its midpoint.',expression=rf'AM=\frac{{AB}}{{2}}=\frac{{{2*m["half"]}}}{{2}}={m["half"]}')
            add('right_triangle','Subtract the known leg square','Triangle AMP is right-angled at M and PA is its hypotenuse.',expression=rf'PM^2={m["pa"]}^2-{m["half"]}^2={m["pm"]**2}')
            add('length','Take the positive square root','A segment length is nonnegative.',expression=rf'PM=\sqrt{{{m["pm"]**2}}}={m["pm"]}')
        elif t=='bdc':
            half=m['b']/2
            add('geometric_property','Bisect the angle at B','The bisector divides angle ABC into two equal angles.',expression=rf'\angle DBC=\frac{{{m["b"]}^\circ}}{{2}}={q(half)}^\circ')
            add('triangle','Subtract the two known triangle angles','Triangle BDC has interior angle sum 180°.',expression=rf'\angle BDC=180^\circ-{q(half)}^\circ-{m["c"]}^\circ={q(180-half-m["c"])}^\circ')
        else:
            plans={'half':('Halve the whole angle','An angle bisector produces two equal halves.'),
                   'double':('Double the given half-angle','Two equal half-angles compose the whole angle.'),
                   'midpoint':('Use the equal midpoint distances','The perpendicular bisector divides AB into two equal segments.'),
                   'equal_distance':('Use equal distances to the endpoints','Every point on the perpendicular bisector is equally distant from A and B.')}
            action,reason=plans[t];add('geometric_property',action,reason,range(n))
    elif f=='geometrical_terms':
        if t=='prism_faces':
            add('lateral','Count the lateral faces','Each base edge gives one lateral face.',[0])
            add('bases','Include both prism bases','A prism has two congruent parallel bases in addition to its lateral faces.',range(1,n))
        elif t=='isosceles_angles':
            b=m['base_angle'];add('base_angles','Add the equal base angles','The base angles of an isosceles triangle are equal.',expression=f'{b}+{b}={2*b}')
            add('vertex','Subtract from the triangle total','All three interior angles sum to 180°.',expression=f'180^\circ-{2*b}^\circ={180-2*b}^\circ')
        else:add('classification','Compare the angle with the class boundaries','Acute angles lie between 0° and 90°, obtuse between 90° and 180°, and reflex between 180° and 360°; equality gives the named boundary angle.',range(n))
    elif f=='constructions_scale_drawings':
        add('geometric_property','Apply the drawing-to-real scale','The scale denominator multiplies each drawing length in the same unit.',[0])
        add('units','Convert centimetres to metres','There are 100 centimetres in one metre.',range(1,n))
    elif f=='symmetry_two_dimensions':
        if t=='regular_polygon_symmetry':add('geometric_property','Count the reflection axes','A regular n-sided polygon has n distinct lines through its centre that fold the whole outline onto itself.',range(n))
        else:
            add('geometric_property','Find the smallest symmetry turn','The rotational order counts equal matching turns in 360°.',[0])
            if n>1:add('repeat','Apply the requested number of turns','Successive equal rotations add their angles.',range(1,n))
    elif f=='symmetry_circles':
        if t=='equal_tangents':
            add('geometric_property','Equate the tangent lengths','Tangents from the same external point to a circle have equal lengths.',[0])
            add('subtract','Subtract the constant from both sides','Equivalent subtraction isolates the term containing the unknown.',[1])
            add('divide','Divide by the coefficient','Division by the nonzero coefficient isolates the unknown.',range(2,n))
        else:
            action,reason={'chord_midpoint':('Halve the chord','The perpendicular from a circle centre to a chord bisects that chord.'),
                'equal_chord_distances':('Use equal distances from the centre','Equal chords in the same circle are equidistant from its centre.')}[t]
            add('geometric_property',action,reason,range(n))
    elif f=='introduction_vectors':
        reasons={'displacement_components':('Subtract the start from the endpoint','Directed displacement is endpoint position minus starting position, component by component.'),
                 'reverse_vector':('Reverse both component signs','Reversing a displacement preserves length and reverses direction.'),
                 'endpoint_from_displacement':('Add the displacement to the starting position','An endpoint is the start plus its signed horizontal and vertical changes.')}
        action,reason=reasons[t];add('displacement',action,reason,range(n))
    elif f=='functions_concepts':
        if t=='mapping_notation':
            add('notation','Write the same mapping in the requested notation','f(x) and x mapped to an expression describe the same input-output rule.',expression=m['written'])
            add('evaluate','Substitute the specified input','Apply the rule to the entire signed input.',expression=f'f({m["input"]})=({m["a"]})({m["input"]})+({m["b"]})={m["output"]}')
        elif t=='relation_function':
            pairs='; '.join(f'{x} → {y}' for x,y in m['pairs'])
            add('arrows','Inspect every input’s outgoing arrows','A function requires exactly one output for each member of its input set.',expression=pairs)
            add('decision','Decide whether the requirement holds','An input with no output or with two different outputs violates the function definition.',expression=m['reason'])
        elif t=='inverse_meaning':
            add('forward','Evaluate the forward mapping','The inverse starts from the output of the original function.',expression=f'f({m["input"]})={m["a"]}({m["input"]})+({m["b"]})={m["output"]}')
            add('reverse','Reverse the input-output pair','The inverse recovers the original input from that output.',expression=rf'f^{{-1}}({m["output"]})={m["input"]}')
        elif t in ('one_one_mapping','one_one_domain'):
            add('distinct','Compare outputs for different allowed inputs','A one-one function never sends distinct allowed inputs to the same output.',expression=m['reason'])
            add('inverse','Decide whether reversing the arrows gives a function','A repeated output would acquire multiple inverse outputs.',expression=m.get('inverse_reason','An inverse function on the range exists.' if m['one_one'] else 'The complete mapping has no inverse function on its range.'))
        elif t=='composite_meaning':
            inner='g' if m['order']=='fg' else 'f';outer='f' if inner=='g' else 'g'
            add('inner','Apply the inner function first','The rightmost function acts on the original input.',expression=f'{inner}({m["input"]})={m["intermediate"]}')
            add('outer','Apply the outer function to that output','Composition uses the first result as the second function’s input.',expression=f'{outer}({m["intermediate"]})={m["output"]}')
            add('rule','Write the composite rule','Substituting the inner rule in the outer rule gives one rule with the same operation order.',expression=f'{m["order"]}(x)={m["coefficient"]}x+({m["constant"]})')
        else:raise ValueError(f'Unmapped function concept {t}')
    else:return None
    return a.finish()
