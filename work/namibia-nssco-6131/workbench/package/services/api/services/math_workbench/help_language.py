"""Answer-free teaching notes. Only guide text and displayed inputs are read."""
from copy import deepcopy
import json
from pathlib import Path

VERSION = 3

# These explanations describe methods, not computed results for an instance.
TOPIC_STARTERS = {
    'Factorisation': 'Factorising means rewriting an expression as a product: quantities multiplied together. Start by checking whether every term shares a factor. Keep the original expression equal to your new product; multiplying your brackets back out is how you check.',
    'Solving Quadratic Equations': 'Solving means finding every value that makes the equation true. First identify the requested method and put the equation into a form that method can use. Keep both possible roots until the original question gives a reason to reject one.',
    'Quadratic Graphs': 'A point on the graph pairs an input with its output. Read the axis scales first. A table helps you place points; intersections show where two rules give the same output. Keep readings tied to the correct curve and axis.',
    'Combined Events and Tree Diagrams': 'Each branch describes one possible next event. Start with the choices available at that stage. Multiply probabilities along one complete path; add separate qualifying paths only when they cannot happen together. If an item is not replaced, the available counts change.',
    'Income, Taxes, and Bills': 'Separate money earned or owed from money already paid or credited. Use the rates and bands supplied in the question. Work out each charge or earning component separately so you can see which amounts to add and which to subtract.',
    'Surface Area and Volume of 3D Shapes': 'Surface area measures the outside faces in square units; volume measures the space inside in cubic units. Identify which is requested, sketch the relevant parts, and match each measurement to the formula before substituting.',
    'Determinants, Inverses, and Simultaneous Equations': 'Keep each matrix entry in its row and column. For a two-by-two matrix, the determinant is the product of the top-left and bottom-right entries minus the other diagonal product. A zero determinant means the matrix has no inverse.',
    'Angle Properties (Circles)': 'Identify the centre, radii, chords and any tangent before choosing an angle rule. Connect each angle to the lines or arc that define it. State the rule you use so another person can follow why the angles are related.',
    'Advanced Graphs (Reciprocal, Cubic, and Exponential)': 'Read the axes and the stated input range first. Each plotted point must satisfy the rule. Check where the rule is undefined before drawing; a curve must not be joined through an input that is not allowed.',
    'Advanced Percentage Calculations': 'A percentage is an amount out of one hundred. Identify the amount the percentage refers to before calculating. For repeated change, use a multiplier for each period; when working backwards, undo the multiplier rather than subtracting the percentage.',
    'Algebraic Expressions and Formulae': 'Identify what each letter represents and what the question wants you to find. Keep the equality balanced when rearranging: apply the same operation to both sides. Substitute given values using brackets, especially for negative inputs.',
    'Algebraic Manipulation and Expansion': 'Expanding means multiplying a term into every term of a bracket. Keep the signs attached to their terms. Only combine terms with the same letter part and the same powers; these are called like terms.',
    'Angle Properties (Lines and Polygons)': 'Start with a labelled sketch and identify the angle relationship that applies. Angles on a straight line total 180 degrees; angles around a point total 360 degrees. Use only the rule justified by the lines and shape shown.',
    'Angle and Perpendicular Bisectors': 'A bisector divides something into two equal parts. An angle bisector gives points equally distant from the two sides; a perpendicular bisector gives points equally distant from the two endpoints. Match the construction to the distance condition requested.',
    'Angles of Elevation, Depression, and Extended Ratios': 'Draw and label the right triangle first. Elevation and depression are measured from a horizontal line. Relative to the angle you use, identify the opposite side, adjacent side and hypotenuse before selecting a trigonometric ratio.',
    'Circles, Arcs, and Sectors': 'An arc is part of a circumference and a sector is a slice of the circle. Compare the central angle with a full turn to find what fraction of the whole circle is involved. Keep radius and diameter distinct.',
    'Cumulative Frequency': 'Cumulative frequency is a running total, so each entry includes all earlier groups. To locate a median, quartile or percentile, first find the required position in the total count, then read the matching value from the graph or table.',
    'Defining Sets and Standard Notation': 'A set is a collection of distinct elements. Check the universal set, which tells you which elements are allowed. Distinguish an element belonging to a set from one whole set being contained in another.',
    'Describing and Combining Transformations': 'Track corresponding vertices, not just how the picture looks. Describe the transformation with the information it needs, such as a vector, centre, angle or mirror line. For combined transformations, apply them in the stated order.',
    'Directed Numbers in Action': 'Positive and negative signs indicate position or direction relative to zero. Decide what an increase or decrease means in this context before calculating. On a number line, movement right increases the value and movement left decreases it.',
    'Distance, Midpoint, and Gradient': 'Find the horizontal and vertical changes between the two points. Distance measures their separation, midpoint lies halfway between them, and gradient compares vertical change with horizontal change. Use the same point order in both differences.',
    'Equations of Straight Lines': 'In y = mx + c, m is the gradient and c is the vertical-axis intercept. Decide which information the question supplies, then use a known point to find what is missing. Check the final rule with that point.',
    'Estimation': 'Estimation replaces awkward values with nearby manageable values so you can judge the size of a result. Round as instructed before calculating, and keep the original operations. Your estimate should be reasonable for the original quantities.',
    'Fractions, Decimals, Percentages, and Ordering': 'These are different ways to represent numbers. For comparison, put the values into a common form or use a common denominator. Equivalent fractions change numerator and denominator by the same nonzero factor, so the value stays the same.',
    'Functions': 'A function is a rule linking an input to one output. Substitute into the whole rule using brackets. For a composition, the output of the first function becomes the input of the next; an inverse reverses the original input-output relationship.',
    'Geometrical Constructions and Scale Drawings': 'Read the given measurements and choose a scale before drawing. Construction marks show how distances or angles were fixed; keep useful arcs visible. Convert between drawing length and actual length in the correct direction.',
    'Geometrical Terms and Vocabulary': 'Use the defining properties of the object, rather than its apparent size or orientation. Check the sides, angles, faces or boundaries named in the question, then match those properties to the correct mathematical term.',
    'Grouped Data and Estimating the Mean': 'Grouped data gives intervals rather than every original value. A class midpoint stands in for the values in its interval when estimating a mean. Weight each midpoint by its frequency so larger groups contribute more.',
    'Histograms': 'In a histogram, bar area represents frequency. If class widths differ, height alone does not compare the counts: height is frequency divided by class width. Read each interval width before calculating or drawing its bar.',
    'Inequalities and Indices': 'An inequality describes a range rather than one value. Keep both sides equivalent, reversing the inequality when multiplying or dividing by a negative number. For powers, identify the base and operation before applying an index rule.',
    'Introduction to Functions': 'A function pairs each allowed input with one output. Read which set supplies the inputs and which contains the outputs. Follow the direction of the mapping and check the rule with the given pairs.',
    'Introduction to Vectors and Notation': 'A vector records a change in position, including direction. Read the horizontal change first and the vertical change second. A vector from one point to another is not the same as either point on its own.',
    'Kinematics and Rate of Change': 'A rate compares a change with the time taken. Read the graph labels before choosing a method: a gradient measures a rate of change, while an area under a speed-time graph measures distance. Keep time units consistent.',
    'Limits of Accuracy (Bounds)': 'A rounded value represents an interval of possible original values. Start by finding half the rounding unit. For a bound on a calculation, choose input endpoints that make the whole expression as small or as large as required.',
    'Linear Programming': 'Define the variables and translate each restriction into an inequality. A feasible point must satisfy all restrictions at once. Draw boundary lines, identify their common allowed region, then compare the objective at the relevant vertices.',
    'Locus': 'A locus is the set of all points satisfying a distance or angle condition. Draw the set for each condition separately. If both conditions must hold, look for points shared by the two sets.',
    'Logarithms': 'A logarithm asks which exponent produces a given number from a given base. Keep track of the base and ensure logarithm inputs are positive. Use a logarithm rule only when its conditions match the expression.',
    'Matrix Basics, Addition, and Subtraction': 'A matrix is an organised array of entries. Its order is the number of rows followed by the number of columns. Addition and subtraction match entries in the same positions, so the matrices must have the same order.',
    'Matrix Multiplication and Properties': 'Matrix multiplication combines a row from the first matrix with a column from the second. Their lengths must match. Multiply corresponding entries and add those products; reversing the matrix order may change the result or make the product undefined.',
    'Mean, Median, Mode and Range': 'Decide which summary is requested. The mean shares the total equally, the median uses the middle position after ordering, the mode is the most frequent value, and the range measures the gap between the greatest and smallest values.',
    'Metric Units and Conversions': 'Write the starting and required units before converting. A conversion factor for lengths must be squared for areas and cubed for volumes. For a compound unit, convert each component separately so you can track the direction.',
    'Number properties': 'A factor divides a number exactly; a multiple is obtained by multiplying it by a whole number. Prime factors are primes multiplied together to make the number. Decide which property is requested before selecting or combining factors.',
    'Parallel Lines, Perpendicular Lines, and Quadrilaterals': 'Use the given coordinates or marked geometric properties to choose a relationship. Parallel nonvertical lines have equal gradients; perpendicular nonvertical lines have gradients whose product is negative one. Treat horizontal and vertical lines as a separate case.',
    'Perimeters and Areas of 2D Polygons': 'Perimeter measures the outside boundary, while area measures the region inside. For a composite shape, split the region into familiar pieces. Only count actual boundary edges in a perimeter, and distinguish a sloping side from perpendicular height.',
    'Personal Finance and Currency': 'Identify what the given rate applies to and which currency or amount is required. Keep units with the calculation. Work out each cost, interest amount or conversion separately before combining it with the starting balance.',
    'Polynomials and Algebraic Fractions': 'Keep entire numerators and denominators together using brackets. Only matching factors can be cancelled, not separate terms in a sum. Note any values that make an original denominator zero before simplifying.',
    'Position Vectors and Coplanar Vectors': 'A position vector runs from the origin to a point. To travel between two points, subtract the starting position vector from the finishing one. For a ratio point, identify the whole directed segment before taking a fraction of it.',
    'Ratios, Scales, and Rates of Change': 'A ratio compares quantities in equal-sized parts. Identify what the stated total or difference represents before finding one part. For a scale, put both lengths in the same units before comparing them.',
    'Reading and Interpreting Graphs and Charts': 'Read the title, axis labels, scale and key before using a value. Check what one division or symbol represents. Distinguish a single category from a total and keep units attached to graph readings.',
    'Sequences': 'Look for a consistent relationship between consecutive terms. An arithmetic sequence has a constant difference; a geometric sequence has a constant ratio. Identify the first term and the term position before choosing a term or sum formula.',
    'Similarity and Congruence': 'Match corresponding sides and angles before comparing lengths. Similar shapes share their shape, while congruent shapes also share their size. A length scale factor acts once on lengths, twice on areas and three times on volumes.',
    'Simple Probability': 'A probability compares a favourable event with the possible outcomes. Counting favourable outcomes over total outcomes works when the outcomes are equally likely. Distinguish an experimental estimate from a guaranteed future count.',
    'Sketching Quadratics and Estimating Gradients': 'Use the equation to identify useful features such as intercepts, symmetry and the turning point. A tangent gradient describes the slope at one point; a chord gradient describes an average slope between two points. Keep the graph scale in view.',
    'Solving Linear and Simultaneous Equations': 'An equation stays balanced when the same operation is applied to both sides. For simultaneous equations, the solution must satisfy both equations. Choose substitution or elimination to reduce the problem to one unknown, then check both original equations.',
    'Straight Line Graphs and Gradients': 'Gradient compares vertical change with horizontal change. Choose two readable points on the line and keep their order the same in both differences. An intercept is where the line meets an axis, not just any marked point.',
    'Symmetry Properties of Circles': 'Look for the line through the centre that relates the points or chords. A perpendicular from the centre to a chord bisects the chord. Use the marked circle conditions to justify equal lengths or angles before calculating.',
    'Symmetry in Two Dimensions': 'Reflection symmetry matches a shape across a mirror line; rotational symmetry matches it after turning around a centre. Check all vertices or features, not just one. A full turn returns every shape to its starting position.',
    'The Sine/Cosine Rules and 3D Trigonometry': 'Label known sides and angles and identify which triangle contains the unknown. Match a side to its opposite angle before using the sine rule. Use the cosine rule or a right-triangle relationship when the given information supports it.',
    'Three-Figure Bearings and Right-Angled Triangles': 'A bearing is measured clockwise from north at the starting point and written with three digits. Draw the north line before locating the angle. For right-triangle calculations, identify the sides relative to the angle you are using.',
    'Time': 'Separate clock readings from elapsed durations. There are sixty minutes in an hour, so decimal hours are not read as hours and minutes. Counting through an hour boundary can make a journey or waiting-time calculation easier to follow.',
    'Vector Operations and Magnitude': 'Vector components describe signed movement in each direction. Add or subtract matching components. Magnitude measures the resulting length, so it is a nonnegative value and does not retain the vector’s direction.',
    'Venn Diagrams': 'Each region represents a particular combination of set memberships. Put overlaps in the correct regions and avoid counting them twice. A complement means everything in the universal set that lies outside the named set.',
}

OPERATIONS = {
    'State the requested result': 'Reread what the question asks for. Use the requested form and units, and apply any final rounding only after the calculation.',
    'Find the shared factor': 'A shared factor divides every term exactly. Compare the number factors and any repeated letters before deciding what can go outside a bracket.',
    'Identify the complete shared factor': 'Look for the largest factor that divides every term. For a letter that appears with different powers, only the copies present in every term can be taken out.',
    'Divide each term by the shared factor': 'Divide every original term by the factor you are taking out. Those quotients belong inside the bracket, because multiplying them by the outside factor must rebuild the original terms.',
    'Divide both terms by the shared factor': 'Divide both original terms by the outside factor, keeping their signs. The two quotients make the bracket; leaving the original terms inside would multiply them again.',
    'Write the product': 'Write the shared factor outside a bracket containing the remaining terms. Multiply back into the bracket to check that each original term is recovered.',
    'Find a pair with the required product and sum': 'List factor pairs for the required product, then test their sums. The product controls the constant term and the sum controls the middle term, so both conditions must hold.',
    'Collect like terms': 'Keep each sign with its term. Combine only terms with exactly the same letter part and powers; add or subtract their coefficients.',
    'Collect equal powers': 'Line up terms with the same powers. Add or subtract their coefficients, keeping other powers separate.',
    'Distribute every factor across its bracket': 'Multiply the outside factor by every term inside the bracket. Keep each term’s sign so no product is missed.',
    'Expand the squared bracket': 'A squared bracket means multiplying the whole bracket by itself. Include both cross-products as well as the two square terms.',
    'Use a common denominator': 'Choose a denominator containing the factors needed by both fractions. Multiply each numerator and denominator by its missing factor so the fraction’s value stays unchanged.',
    'Combine over a common denominator': 'Write both fractions over a shared denominator. Change each numerator by the same factor used on its denominator, then combine the whole numerators with the original sign.',
    'Check both denominators': 'Identify values that make either denominator zero. Division by zero is undefined, so those values cannot be used in the original equation.',
    'Remove the valid denominator': 'Once its zero values are excluded, multiply every term on both sides by the common denominator. This clears the fractions while keeping the equation balanced.',
    'Solve and check the domain': 'Solve the simplified equation, retaining all possible roots. Check them in the original equation and reject any value that makes an original denominator zero.',
    'Divide by the coefficient': 'The coefficient is the number multiplying the unknown. Divide both sides by that nonzero number to leave the unknown by itself.',
    'Set each factor equal to zero': 'A product can equal zero only if at least one factor is zero. Form an equation from each factor so you do not miss a possible solution.',
    'Take both square roots': 'Squaring a positive or negative value can give the same positive result. Consider both roots, then use the question’s restrictions to decide which are allowed.',
    'Find the determinant': 'For a two-by-two matrix, multiply the top-left entry by the bottom-right entry. Subtract the product of the top-right and bottom-left entries, keeping negative signs in brackets.',
    'Form and scale the adjugate': 'For a two-by-two matrix, swap the diagonal entries and reverse the signs of the other two entries. If the determinant is nonzero, multiply every new entry by its reciprocal to obtain the inverse.',
    'Calculate each row–column dot product': 'Pair a row of the first matrix with a column of the second. Multiply matching entries and add their products to obtain the entry in that row and column of the answer.',
    'Apply the circle-angle theorem': 'Identify the arc, chord or tangent defining the angles before selecting a circle theorem. State that relationship and use it to form an equation with the marked angles.',
    'Multiply along the qualifying path': 'Follow the event in the requested order. Multiply its branch probabilities because all stages on that path must occur.',
    'Form the complete event probability': 'List every separate path that satisfies the event. Add probabilities only for paths that cannot happen at the same time, so an outcome is not counted twice.',
    'Find the corresponding length scale factor': 'Match the same length on each shape. Divide the target shape’s length by the starting shape’s length to find the multiplier in the required direction.',
    'Apply the scale factor in the requested dimension': 'A length changes by one scale factor. An area changes by its square because it has two dimensions, while a volume changes by its cube because it has three.',
    'Find the base and perpendicular height': 'Choose the base and the distance measured at a right angle to it. A sloping edge is not the perpendicular height unless the diagram shows that it is.',
    'Plot the table points': 'For each table row, use the input as the horizontal coordinate and its output as the vertical coordinate. Mark the point using the scales on both axes.',
    'Read every intersection with the target height': 'Draw or follow a horizontal line at the requested output value. Each place it meets the curve gives a possible input, which you read from the horizontal axis.',
    'Choose the required prime powers': 'For a highest common factor, use shared primes with the smaller powers. For a lowest common multiple, use every required prime with its largest power. Decide which quantity the question requests before multiplying.',
}


def topic_for(question):
    rows = json.loads((Path(__file__).resolve().parents[4] / 'provider-catalogue.json').read_text())
    key = question.get('pilot_key')
    row = next((row for row in rows if row['id'] == key), None)
    if row is None:
        row = next((row for row in rows if row['recipeId'] == question['recipe_id']), None)
    return row['topic'] if row else None


def coach_saved_help(question, guide):
    """Upgrade authored guide wording without reading any solution fields."""
    if guide.get('version', 0) >= VERSION:
        return deepcopy(guide)
    result = deepcopy(guide)
    starter = TOPIC_STARTERS.get(topic_for(question))
    parts = result.get('parts', [])
    for part in parts:
        part['prompts'] = [OPERATIONS.get(prompt.rstrip('.'), prompt) for prompt in part['prompts']]
    if starter and parts:
        # One method introduction for the whole guide, rather than repeating it
        # for every part of a multipart question.
        parts[0]['prompts'][0] = starter + '\n\n' + parts[0]['prompts'][0]
    prompts = []
    for part in parts:
        for index, prompt in enumerate(part['prompts']):
            label = f"**Part ({part['part_id']}): {part['method']}**\n\n" if len(parts) > 1 and index == 0 else ''
            prompts.append(label + prompt)
    if not parts:
        prompts = list(result['prompts'])
        if starter and prompts:
            prompts[0] = starter + '\n\n' + prompts[0]
    result.update(version=VERSION, prompts=prompts, source='authored_teaching_principles_and_displayed_inputs; no solution results')
    return result
