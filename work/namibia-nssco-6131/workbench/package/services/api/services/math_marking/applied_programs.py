"""Coordinate, vector, trigonometry and statistics solution operations."""
from fractions import Fraction
from .operation_reasons import operation_reason
import ast
import re
from .solution_programs import Author
from .formatting_adapter import q


def applied_program(p,content):
    f=p.generator_id.removeprefix('nssco_');m=p.machine;t=m.get('task',p.skill)
    a=Author(p,content);add=a.add;n=len(a.rows);awards=()
    if f=='kinematics_rate_change':
        reasons={'distance_time_gradient':'Speed is change of distance divided by elapsed time.',
                 'acceleration':'Acceleration is the signed change of velocity divided by its time interval.',
                 'trapezium_distance':'For uniform acceleration, distance is average of the initial and final speeds multiplied by duration.',
                 'braking_distance':'The area under the speed–time graph gives distance; uniform braking forms a triangle with final speed zero.'}
        add('rate_or_area','Apply the requested motion relationship',reasons[p.skill],range(n))
    elif f=='linear_programming':
        if t=='test_points':
            add('conditions','Test every supplied point against every constraint','A feasible point must satisfy all the inequalities simultaneously, including their boundary conventions.',range(n-1))
            add('count','Count the points meeting every condition','A point passing only some constraints is not feasible.',[n-1])
        elif t=='three_inequalities':
            # The fourth source line repeats the same three inequalities.
            a.rows=a.rows[:3];n=len(a.rows)
            for i in range(n):add('constraint_'+str(i),'Translate the next independent restriction','Use the specified minimum, maximum or rate comparison with the correct inclusive boundary.',[i])
        elif t=='best_value':add('vertices','Compare the objective at feasible vertices','A linear objective over this bounded polygon reaches the requested greatest or least value at a vertex or along a tying edge.',range(n))
        else:add('constraint','Express the stated resource restriction','Multiply each count by its matching resource use and compare the total with the supplied limit.',range(n))
    elif f=='introduction_functions':
        if p.skill=='function_input':
            add('equation','Equate the function to the required output','The unknown input must make the stated rule equal the supplied output.',[0])
            add('isolate','Undo the linear operations','Apply inverse operations to both sides of the equation.',range(1,n))
        else:add('substitution','Substitute the stated input in the complete rule','Replace every input occurrence, retaining brackets around negative values and evaluating powers before products.',range(n))
    elif f=='straight_line_graphs_gradients':
        if t=='gradient_two_points':
            add('changes','Find both directed coordinate changes','Use the same point order for horizontal and vertical differences.',range(n-1))
            add('gradient','Divide vertical by horizontal change','Gradient is rise divided by run, provided the horizontal difference is nonzero.',[n-1])
        elif t in ('gradient_general_form','intercept_general_form','axis_intercepts'):
            add('rearrange','Express the equation as y=mx+c','Subtract the x-term and divide the entire equation by the y coefficient.',range(3))
            if n>3:add('intercepts','Set the opposite coordinate to zero','An x-intercept has y=0 and a y-intercept has x=0.',range(3,n))
        elif t=='find_intercept_constant':
            add('point','Substitute the known point','A point on the line satisfies its equation.',[0])
            add('intercept','Isolate c and write the equation','Subtract mx from y to find the intercept.',range(1,n))
        else:add('line','Use the stated straight-line relationship',operation_reason(f,t),range(n))
    elif f in ('quadratic_graphs','sketching_quadratics_gradients'):
        if t in ('turning_point','extreme_value'):
            add('vertex_x','Find the axis of symmetry','A quadratic vertex lies at x=−b/(2a), equivalently at the minimum/maximum of its completed square.',[0])
            add('vertex_y','Evaluate the original quadratic at that x','The turning-point ordinate is the function value at the axis of symmetry.',range(1,n));awards=('vertex_x','vertex_y')
        elif t=='solve_f_equals_g':
            add('equate','Equate the function values','At an intersection both rules have the same output.',[0])
            add('quadratic','Rearrange and factorise','Move all terms to one side and form factors reconstructing the quadratic.',range(1,n));awards=('equate','quadratic')
        elif t=='range_of_x':
            add('boundaries','Find the quadratic zeros','The zeros divide the number line into intervals where the quadratic can change sign.',range(n-1))
            add('intervals','Choose the intervals satisfying the inequality','Test the sign between/outside zeros and preserve the requested endpoint inclusion.',[n-1]);awards=('boundaries','intervals')
        elif t in ('x_intercepts','other_root'):
            add('factor','Set y=0 and factorise','The x-axis consists of points with y=0.',range(n-1))
            add('roots','Use the zero-product rule','Set each factor equal to zero and retain the requested root(s).',[n-1])
        elif t=='chord_gradient':
            add('values','Find both points on the curve','Substitute each endpoint x in the original quadratic.',range(n-1))
            add('gradient','Calculate the chord slope','A chord is a straight segment, so its gradient is Δy/Δx.',[n-1])
        elif t=='square_form_turning_point':
            add('zero_square','Make the squared bracket zero','The square term reaches zero at the vertex.',range(n-1))
            add('ordinate','Read the remaining constant','Once the square is zero, the outside constant is the vertex ordinate.',[n-1])
        else:add('values','Evaluate the requested quadratic values','Substitute the stated x-values in the complete rule, or x=0 for the y-intercept.',range(n))
    elif f=='advanced_graphs':
        if t in ('reciprocal_values','cubic_values','exp_values'):
            add('values','Evaluate each stated input','Use the complete function rule, preserving denominator restrictions and negative/fractional exponents.',range(n))
        else:
            add('relationship','Undo the function operation','Use equivalent operations to isolate the cube, reciprocal, square or common-base exponential relationship.',range(n-1))
            add('solutions','Retain the permitted solutions','A square equation has both real branches unless the domain restricts it; a reciprocal excludes zero.',[n-1])
    elif f=='distance_midpoint_gradient':
        if t=='find_missing_coordinate_distance':
            add('distance_equation','Form the squared-distance relationship','Pythagoras relates the horizontal and vertical coordinate differences to the supplied distance.',[0])
            add('isolate','Isolate the missing displacement square','Subtract the known squared displacement from the distance squared.',[1])
            add('branches','Recover both possible coordinates','Take both signs of the square root and restore the known coordinate offset.',range(2,n));awards=('distance_equation','isolate')
        elif t=='find_missing_coordinate_gradient':
            add('displacement','Use the given gradient to find vertical change','Gradient × horizontal change gives the required vertical displacement.',range(n-1))
            add('coordinate','Add the displacement to the known ordinate','A coordinate is a position; restore the starting ordinate after finding its displacement.',[n-1]);awards=('displacement','coordinate')
        elif t=='distance_surd':
            from math import isqrt
            radicand=re.search(r'\\sqrt\{(\d+)\}',a.rows[-1])
            if not radicand:raise ValueError('Missing exact distance radicand')
            N=int(radicand[1]);factor=max(k for k in range(1,isqrt(N)+1) if N%(k*k)==0);inside=N//(factor*factor)
            add('differences','Find the coordinate differences','Subtract the starting coordinate from the ending coordinate on each axis.',range(n-1))
            add('measure','Apply Pythagoras','Square both displacements and add before taking the square root.',[n-1])
            add('simplify','Take the square factor outside the root','The square root of a positive product is the product of its square roots.',expression=rf'\sqrt{{{N}}}=\sqrt{{{factor*factor}\times{inside}}}={factor}\sqrt{{{inside}}}')
        elif t.startswith('distance_') or t=='gradient_between_points':
            add('differences','Find the coordinate differences','Use endpoint minus starting point in the same order for both axes.',range(n-1))
            add('measure','Apply the requested distance or gradient relationship',('Distance is the positive square root of the sum of squared coordinate differences.' if t.startswith('distance_') else 'Gradient is vertical difference divided by horizontal difference.'),[n-1])
        else:add('midpoint','Use the midpoint relationship',operation_reason(f,t),range(n))
    elif f=='equations_of_straight_lines':
        if t in ('lines_meet','line_intersection'):
            if t=='line_intersection':
                add('line','Determine the unknown line first','Find its gradient from the supplied points, then use a point to obtain c.',range(n-4))
            start=0 if t=='lines_meet' else n-4
            add('equate','Equate the two line rules','Their common point has the same x and y in both equations.',[start])
            add('abscissa','Solve the resulting linear equation','Collect x-terms and divide by their nonzero coefficient.',range(start+1,n-1))
            add('ordinate','Substitute x into an original line','This recovers the y-value paired with the intersection x.',[n-1])
        elif t=='line_through_two_points':
            add('gradient','Calculate rise divided by run','Use the same point order in both coordinate differences.',range(n-3))
            add('intercept','Use a known point in y=mx+c','The point fixes c once m is known.',range(n-3,n-1))
            add('equation','Combine the determined gradient and intercept','Both parameters are needed for the complete line equation.',[n-1])
        elif n>1:
            add('point','Apply the required gradient to a known point','Parallel lines have equal gradients; nonvertical perpendicular gradients multiply to −1.',range(n-1))
            add('equation','Write the complete line equation','Combine the gradient with the intercept determined by substitution.',[n-1])
        else:add('equation','Combine the supplied gradient and intercept','In y=mx+c the gradient is m and y-intercept c.',range(n))
    elif f=='parallel_perpendicular_quadrilaterals':
        if t in ('rectangle_area','parallelogram_area'):
            add('dimensions','Find the base and perpendicular height','Coordinate distance gives the actual side lengths; use the perpendicular height rather than a slanted side.',range(n-1))
            add('area','Multiply base by perpendicular height','A rectangle/parallelogram area is base times perpendicular height.',[n-1]);awards=('dimensions','area')
        elif t in ('find_k_parallel','find_k_perpendicular'):
            add('gradient','Express the unknown line gradient','Rearrange to y=mx+c to identify the coefficient of x.',range(2))
            add('relationship','Impose the required gradient relationship',('Parallel gradients are equal.' if t=='find_k_parallel' else 'Nonvertical perpendicular gradients have product −1.'),range(2,n))
        else:add('geometry','Apply the directed-side or gradient relationship',operation_reason(f,t),range(n))
    elif f=='introduction_vectors':add('displacement','Use directed displacement',operation_reason(f,t),range(n))
    elif f=='vector_operations_magnitude':
        if t in ('combination','combination_magnitude'):
            add('scalars','Scale both vector components','A scalar multiplies the complete vector, including every signed component.',range(2))
            add('combine','Combine corresponding components','Vector addition/subtraction acts component by component in the stated order.',[2])
            if n>3:add('magnitude','Calculate the length of the resultant','Pythagoras gives the nonnegative square root of the sum of squared components.',range(3,n))
        else:add('vector','Apply the requested vector operation',operation_reason(f,t),range(n))
    elif f=='position_vectors':
        if t in ('ratio_point','position_letters','vector_AM','vector_MN'):
            add('displacement','Find the complete directed side','A displacement equals endpoint position vector minus starting position vector.',[0])
            add('ratio','Take the specified fraction of the directed side','The first ratio term divided by the sum of ratio terms gives the fraction measured from the stated starting point.',[1])
            if t=='vector_MN':
                add('positions','Express both intermediate position vectors','Add the starting position to a displacement; a midpoint position is half the endpoint-position sum.',range(2,n-1))
                add('requested','Subtract endpoint position vectors','The vector from M to N is ON−OM, in that direction.',[n-1]);awards=('ratio','requested')
            elif n>2:add('position','Restore the starting position','A ratio displacement becomes a position only after adding the starting position vector.',range(2,n))
            if t=='vector_AM':awards=('displacement','ratio')
        else:add('midpoint','Average corresponding position components','A midpoint position is half the sum of the endpoint position vectors.',range(n))
    elif f=='transformations_coordinates':
        if t=='enlarge':
            points=[ast.literal_eval(x) for x in m['points']];centre=tuple(Fraction(x) for x in m['centre']);k=Fraction(m['k'])
            from ..math_workbench.core import coordinates
            vectors=[(Fraction(x)-centre[0],Fraction(y)-centre[1]) for x,y in points];scaled=[(k*x,k*y) for x,y in vectors]
            add('displacements','Find the displacements from the given centre','Subtract centre coordinates from each original vertex; the centre need not be the origin.',expression=coordinates(vectors))
            add('scale','Scale each displacement','Multiply both components by the signed enlargement factor.',expression=coordinates(scaled))
            add('images','Add the centre coordinates back','Restore position coordinates after scaling each displacement.',expression=p.answer)
        elif t=='rotate':
            add('relative','Express points relative to the rotation centre','Subtract the centre coordinates before applying an origin-centred rotation rule.',range(2))
            add('turn','Rotate the relative vectors','Apply the stated angle and direction to the displacements, rather than the original positions.',[2])
            add('images','Restore and label the image positions','Add the centre coordinates back to each rotated displacement.',range(3,n))
        elif t in ('reflect','translate','describe_transformation'):
            add('rule','Establish the specified coordinate mapping','A translation adds the same vector to every vertex; a reflection preserves perpendicular distance to its mirror line.',[0])
            add('images','Apply and check the mapping for all vertices','Use one consistent transformation and preserve corresponding vertex labels.',range(1,n))
        else:return None
    elif f=='matrix_basics':
        if t=='equal_matrices':
            add('first','Equate the first corresponding entries','Equal matrices have equal entries in each matching row/column position.',range(2))
            add('second','Equate and solve the other entry relationship','Apply the same corresponding-entry equality to the second unknown.',range(2,n))
        else:add('entries','Operate on corresponding matrix entries',operation_reason(f,t),range(n))
    elif f=='matrix_multiplication':
        if t=='unknown_in_product':
            add('entry','Form the required row–column dot product','Multiply matching row/column components and sum them in the stated multiplication order.',[0])
            add('unknown','Solve the resulting entry equation','The required matrix entry supplies a linear equation for the unknown.',range(1,n))
        else:add('product','Calculate each row–column dot product','An entry of AB uses a row of A and column of B; preserve row/column placement and multiplication order.',range(n))
    elif f=='determinants_inverses':
        if t in ('inverse','matrix_method'):
            add('determinant','Find the determinant','For a 2×2 matrix, determinant is ad−bc; a nonzero value is needed for an inverse.',[0])
            add('inverse','Form and scale the adjugate','Swap diagonal entries, negate off-diagonal entries and divide the whole matrix by the determinant.',[1])
            if n>2:
                add('matrix_equation','Express the simultaneous equations as a matrix equation','Place coefficients in the same variable order as the unknown column vector.',[2])
                add('solve','Multiply the constants column by the inverse','Left multiplication by the inverse removes the coefficient matrix.',range(3,n))
        elif t in ('missing_element','singular_matrix'):
            add('det_equation','Impose the supplied determinant condition','Use ad−bc, equating it to zero for a singular matrix.',range(n-1))
            add('unknown','Isolate the unknown entry','Use equivalent algebraic operations to solve the determinant equation.',[n-1])
        else:add('determinant','Calculate ad−bc','Subtract the off-diagonal product from the diagonal product.',range(n))
    elif f=='bearings_right_angled_triangles':
        if t=='journey_bearing':
            add('reference_angle','Find the right-triangle reference angle','The ratio of perpendicular journey legs gives a tangent ratio.',[0])
            add('forward','Relate the angle to clockwise north','Use the supplied initial bearing and the stated direction of the perpendicular turn.',[1])
            add('back_bearing','Reverse direction and reduce within one turn','A reverse bearing differs by 180°; add or subtract full turns to give a value from 0° to below 360°.',range(2,n));awards=('reference_angle','forward')
        elif t=='journey_distance':
            add('pythagoras','Form the right-triangle distance equation','Perpendicular journey legs are the two shorter sides.',[0])
            add('root','Recover the positive distance','Distance is the positive square root of the summed squares.',range(1,n));awards=('pythagoras','root')
        elif n>1:
            add('relationship','Form the relevant angle or side relationship','Use the named opposite/adjacent/hypotenuse sides for trigonometry, or the supplied direction for a bearing.',[0])
            add('requested','Recover the requested value','Rearrange the ratio or use the inverse trig function; express bearings clockwise from north within a full turn.',range(1,n))
        else:add('triangle','Apply the right-triangle relationship',operation_reason(f,t),range(n))
    elif f=='elevation_depression_extended_ratios':
        if t in ('exact_ratio','exact_expression'):
            if t=='exact_ratio':s,c=Fraction(m['sin']),Fraction(m['cos'])
            else:
                tangent=Fraction(p.steps[0].value);s=Fraction(p.steps[1].value);c=s/tangent
            given=re.search(r'\\(sin|cos)\s*\\theta\s*=',p.question)[1]
            missing='cos' if given=='sin' else 'sin';known=s if given=='sin' else c;derived=c if missing=='cos' else s
            add('identity','Recover the missing ratio magnitude','Use sin²θ+cos²θ=1 before choosing the sign.',expression=rf'\{missing}^2\theta=1-({q(known)})^2')
            add('quadrant','Choose the sign from the stated quadrant','The given quadrant determines the signs of sine and cosine independently.',expression=rf'\{missing}\theta={q(derived)}')
            expression=(rf'\tan\theta=\frac{{{q(s)}}}{{{q(c)}}}' if t=='exact_ratio' else rf'{m["p"]}\tan\theta+{m["q"]}\sin\theta={m["p"]}({q(s/c)})+{m["q"]}({q(s)})')
            add('expression','Evaluate the requested exact expression','Tangent is sine divided by cosine; retain exact fractions throughout the requested operations.',expression=expression);awards=('identity','expression')
        elif t=='solve_trig_equation':
            add('reference','Find the reference angle and allowed quadrants','The sign of the given ratio determines which quadrants can contain solutions.',[0])
            add('solutions','List all solutions within the stated interval','Include each permitted angle once and respect the supplied inclusive boundaries.',range(1,n))
        elif n>1:
            add('ratio','Form the appropriate right-triangle ratio','Use opposite and adjacent sides relative to the horizontal elevation/depression angle.',[0])
            add('requested','Rearrange or invert the tangent relationship','Solve for the stated side, or use inverse tangent for the angle, in degree mode.',range(1,n))
        else:add('evaluate','Evaluate the requested trigonometric expression','Use degree mode, the stated signs and the original order of operations.',range(n))
    elif f=='sine_cosine_rules':
        if t=='cosine_rule_side':
            add('cosine_rule','Apply the included-angle cosine rule','The unknown side opposite the included angle satisfies c²=a²+b²−2ab cos C.',[0])
            add('root','Take the positive square root','A side length is positive; preserve the complete expression under the root.',range(1,n));awards=('cosine_rule','root')
        elif t=='area_to_angle':
            add('sine','Isolate the sine of the included angle','From area=ab sin C/2, divide twice the area by the product of the two sides.',range(2))
            add('inverse','Recover the angle under the stated restriction','Use inverse sine and the question’s acute/obtuse restriction; do not invent a unique angle without it.',range(2,n));awards=('sine','inverse')
        elif t=='pyramid_height':
            add('base_distance','Find the distance from base centre to a corner','The rectangular base diagonal follows from Pythagoras, and the centre bisects that diagonal.',range(n-1))
            add('height','Use the edge–height right triangle','The slant edge is the hypotenuse; subtract the centre-to-corner distance squared before taking the positive root.',[n-1]);awards=('base_distance','height')
        elif n>1:
            add('rule','Form the matching sine/cosine relationship','Match each side to its opposite angle; choose the rule supported by the supplied data.',[0])
            add('requested','Rearrange for the requested side or angle','Keep the complete numerator/denominator and apply the corresponding inverse function for an angle.',range(1,n))
        else:add('area_or_diagonal','Apply the triangle-area or right-triangle relationship',operation_reason(f,t),range(n))
    elif f=='mean_median_mode_range':
        if t=='mean':
            add('total','Find the observation total','Every observation contributes once to the total.',range(n-1))
            add('mean','Divide the total by the observation count','The arithmetic mean gives equal weight to every observation.',[n-1])
        elif t in ('change_in_mean','missing_value'):
            add('totals','Recover the total(s) from the given means','Mean × count gives a total; compare totals rather than subtracting the means.',range(n-1))
            add('difference','Find the unaccounted observation','Subtract the known/old total from the complete/new total.',[n-1])
        else:
            add('order','Put the observations in order','Ordered data reveal the middle position and range endpoints; repeated values retain their multiplicities.',[0])
            add('statistic','Read the requested summary',{'range':'Range is greatest minus least.','median':'The median occupies the middle ordered position(s).','mode':'The mode is the value with greatest frequency.'}[t],range(1,n))
    elif f=='grouped_data_mean':
        if t=='grouped_mean':
            add('contributions','Estimate each class contribution','Represent each class by its midpoint and multiply that midpoint by class frequency.',range(n-2))
            add('total','Add all frequency-weighted midpoint contributions','The sum estimates the data total while counting each observation through its frequency.',[n-2])
            add('mean','Divide by total frequency','The grouped mean estimate is the weighted total divided by the observation count.',[n-1])
        elif t=='median_class':
            add('position','Determine the median position','Use the total frequency to locate the middle observation.',range(2))
            add('class','Locate that position in the cumulative counts','The first cumulative total reaching the median position identifies its class.',range(2,n))
        elif t=='modal_class':
            add('frequency','Identify the largest class frequency','The modal class has the largest frequency, not necessarily the largest boundary.',[0])
            add('class','Give the complete class interval','State both boundaries with their correct inclusion.',range(1,n))
        else:
            add('count','Add the qualifying class frequencies','Include all and only classes meeting the stated boundary.',range(n-1))
            add('percentage','Compare the qualifying count with the total','Divide by the observation total and multiply by 100.',[n-1])
    elif f=='cumulative_frequency_reading':
        if t=='median_class':
            add('position','Find the median position','Use half the total frequency to locate the central observation.',[0])
            add('class','Locate the position in the cumulative totals','Identify the interval where the cumulative count first reaches the median position.',range(1,n))
        else:add('cumulative','Use the cumulative-count relationship',operation_reason(f,t),range(n))
    elif f=='simple_probability':
        if n>1:
            add('counts','Identify total and favourable equally likely outcomes','Count distinct elementary outcomes, respecting the event condition and any complement.',range(n-1))
            add('probability','Divide favourable by total outcomes','For equally likely outcomes, probability is favourable count divided by total count.',[n-1])
        else:add('probability','Apply the event or expectation relationship',operation_reason(f,t),range(n))
    elif f=='tree_diagrams':
        if t in ('total_late','not_late'):
            add('routes','Find the qualifying joint probability on each route','Multiply conditional branch probabilities along each route.',range(2))
            add('total','Combine the mutually exclusive routes','Disjoint qualifying routes are added, not multiplied.',[2])
            if n>3:add('complement','Take the complement of lateness','The probabilities of late and not late sum to one.',range(3,n))
        elif n>1:
            add('branches','Establish the required conditional branches','Apply the event condition and update counts after a draw without replacement.',range(n-1))
            add('path','Multiply along the qualifying path','A joint path probability is the product of its sequential conditional factors.',[n-1])
        else:add('event','Form the complete event probability',operation_reason(f,t),range(n))
    elif f=='histograms_text':
        if p.skill=='unequal_width_total':
            add('frequencies','Recover the frequency of each class','Histogram frequency is class width multiplied by density; unequal widths require separate products.',range(n-1))
            add('total','Add recovered frequencies','The total counts the class frequencies, not their densities.',[n-1]);awards=('frequencies','total')
        elif p.skill in ('frequency_density','frequency_from_density'):
            add('width','Find the class width','Subtract the lower class boundary from the upper boundary.',[0])
            add('histogram_measure','Apply the frequency–area relationship',('Divide frequency by width for frequency density.' if p.skill=='frequency_density' else 'Multiply density by width for frequency.'),range(1,n))
        else:add('histogram','Use histogram frequency as bar area',operation_reason(f,t),range(n))
    elif f=='reading_charts_text':
        if p.skill=='pictogram_key':
            add('symbols','Count equivalent complete symbols','A half symbol contributes half the value of a complete symbol.',[0])
            add('key','Apply the supplied key','Multiply the equivalent symbol count by the count represented by one complete symbol.',range(1,n))
        else:add('read_or_calculate','Use the stated chart values and scale',operation_reason(f,t),range(n))
    elif f=='prepared_line_graphs':add('read','Use the graph coordinates and labelled scale',operation_reason(f,t),range(n))
    elif f.startswith('visual_'):add('representation','Construct or read the specified mathematical representation',operation_reason(f,t),range(n))
    else:return None
    return a.finish(awards)
