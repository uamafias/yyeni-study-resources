"""Rendered-page visual annotations, read by Codex in repair round 2."""
# key | page | crop rectangle (PDF points) | representation | read | variable labels/values | fixed features | relations/constraints
DIAGRAMS = '''
2021-1-Q2|3|160,63,405,255|graph|x-intercepts -2 and 4; vertex (1,-3); upward quadratic|roots and vertex coordinates|upward quadratic form;Cartesian x/y axes|vertex abscissa is midpoint of two distinct roots;coefficient and vertex ordinate consistent;coordinate labels regenerated
2021-1-Q7|8|180,115,400,238|diagram|exposed outer boundary; major-arc inner radius r and shaded outer-sector radius 2r; shaded and unshaded sectors|r;alpha;radius ratio only in reviewed branches|concentric circles;major inner arc plus outer minor sector;angles in radians|concentric sectors;0<alpha<pi;positive radii;perimeter excludes internal joins;labels and angle arc remain unambiguous
2021-1-Q9|10|175,80,410,350|graph|region between y=9-x^2, x-axis and y-axis in first quadrant|quadratic coefficient and intercepts|first-quadrant area;downward quadratic;y-axis rotation for part (b)|positive intercepts;shading under curve;rotation axis y for part b;recover x^2 as function of y;no scale measurement
2022-1-Q8|10|165,55,410,238|diagram|two radii and arc form the wire perimeter|wire length;r;theta|sector of a circle;wire forms two radii and the arc;radian angle|2r+r*theta=L;positive radius and admissible sector angle;arc and radial segments labelled;no unconstrained sector edits
2022-1-Q10|13|85,55,500,252|graph|midline 1, amplitude 2, three cycles over 360 degrees; tick labels|amplitude;period multiplier;vertical shift;domain endpoints|degrees;sinusoidal shape;shared axes and midline representation|ticks consistent with cycles;reflected graph changes signs consistently;read features rather than pixels
2022-1-Q11|14|165,50,410,264|diagram|OP parallel RQ; directed vector order; RQ opposite OP in the drawn traversal|given vectors and positive length multiplier|trapezium topology;OP parallel RQ;directed-vector orientation|nondegenerate trapezium;preserve parallelism and direction;use arrows not apparent scale
2022-1-Q12|16|160,50,425,237|diagram|cone radius 18, height 30; water r,h share vertex|container radius and height;water height|inverted circular cone;horizontal water surface;shared vertex;vertical height|similar cones r/h=R/H;0<h<H;dashed hidden ellipse;volume relation from same values
2022-1-Q14|19|140,65,460,235|graph|A and B intercepts of square-root curve; region AOB|linear radicand coefficients|square-root graph form;area bounded by curve and coordinate axes;x-axis rotation|radicand nonnegative;origin and intercepts consistent;shade only AOB;rotate about x-axis
2022-2-Q3|4|155,70,405,278|graph|A is the first positive crossing; shaded region from 0 to A above axis|trig coefficients and admissible root interval|radians;trigonometric curve form;first positive crossing bounds the shaded region|positive area on chosen interval;no unnoticed additional root in region;exact crossing drives bounds
2023-1-Q6|10|190,95,385,303|diagram|C and D lie on OA and OB; AB is tangent at E to inner arc; whole shaded compound region|outer radius and sector angle|concentric arcs;AB tangent at E to inner circle;compound shaded-region topology;radians|concentric circles;inner r=R*cos(theta/2);0<theta<pi;keep major outer arc plus minor inner sector shading;do not replace by a circular segment
2023-1-Q12|19|155,87,420,270|graph|R extends from x=2 to x=t under reciprocal-square curve|coefficient;linear shift;lower bound and t|reciprocal-square curve form;horizontal asymptote y=0;region bounded by lower limit and t|t exceeds lower bound;denominator nonzero throughout region;horizontal asymptote at 0;infinite-limit branch preserves convergence
2023-1-Q13|20|200,87,450,195|diagram|closed cylindrical tin with radius r and height h|fixed volume;r;h|closed cylinder;two circular ends;perspective is schematic|positive dimensions;two circular ends plus curved area;fixed volume determines h;diagram perspective is not measurement
2023-2-Q2|3|170,72,410,277|graph|downward V; vertex (3,2); intercepts (2,0),(4,0),(0,-4)|vertex;slopes and intercept labels|downward modulus V-shape;integer coefficients as bounded by syllabus|all four points belong to same scaled-and-shifted modulus graph;integer coefficients within grade-a calibrated form
2023-2-Q4|6|140,45,425,250|graph|vertical coordinate is ln y, not y; given two plotted points|points;logarithm base in separately reviewed branches|vertical coordinate is ln y;straight transformed line;two given data points|labels retain transformed vertical variable;positive original y;two points determine a nonvertical line
2024-1-Q7|8|135,55,435,239|diagram|external touching circles; common tangent ST; shaded region bounded by arcs and ST|radii and labels|externally touching circles;common tangent ST;shaded region bounded by ST and arcs|positive unequal radii;centres separated by R+r;radii perpendicular to ST;both sector angles and tangent length recomputed;no arbitrary shading
2024-1-Q8|10|90,50,500,215|diagram|AC perpendicular BD; D reflection of B; M midpoint BD|coordinates A;B;C|reflection construction;AC perpendicular BD;M midpoint of BD|A differs C;B off AC;reflect geometrically consistently;D label not a supplied numeric answer
2024-1-Q9|11|65,55,510,262|graph|amplitude sign, period and product sign from two curves|amplitudes;frequency;domain and tick labels|degrees;one sine and one cosine graph;common interval and axes|plot both functions from same parameters;turning-point label and all sign changes exact;keep visible intercept ordering
2024-1-Q10|12|120,50,500,262|diagram|OABC rectangular base; V vertically above centre M; N midpoint BV; i,j,k orientation|base side lengths;height;named midpoint|rectangular-based pyramid;V vertically above M;N midpoint of BV;i along OA, j along OC, k vertical|positive dimensions;OA aligned i and OC aligned j;k up;consistent perspective and hidden edges;midpoint and coordinate geometry derived
2024-1-Q11|14|195,55,395,264|diagram|rectangle width is diameter 2r; semicircle above it; h excludes semicircle|perimeter;r;h|semicircle above rectangle;rectangle width is semicircle diameter;h excludes semicircle|positive r,h;2h+2r+pi*r=P;area=2rh+pi*r^2/2;keep h arrow on rectangle only
2024-1-Q14|18|140,79,440,300|graph|shaded area between horizontal line and upward parabola; intersection abscissae 1,3|line ordinate and quadratic coefficients|upward quadratic;horizontal comparison line;area shaded between two intersections|two real distinct intersections;upper-minus-lower order;labels regenerated;no region outside crossings
2024-2-Q6|9|155,54,450,193.2|graph|curve cos x+sec x and shaded area from 0 to pi/3|coefficients and upper bound only in compatible branch|radians;cosine plus reciprocal-cosine form;x-axis rotation;region bounded by x=0 and upper limit|no pole in interval;ordinate squared for revolution;x-axis is rotation axis;given region ties to part a
2024-2-Q7|10|170,55,450,200|graph|point P on a parametrised curve; target ordinate 1/4|parametric constants;target ordinate and interval|given parametric-curve form;point P labelled on curve;radian parameter|P from same parameter solution as iteration;retain chosen branch 0<=t<=2;label no independently placed point
2025-1-Q9|12|165,50,440,210|diagram|equilateral triangular prism with side x and vertical height h|fixed volume and dimensions|closed equilateral triangular prism;hidden edges dashed;h is prism length|closed prism;equilateral end faces;positive x,h;volume relation eliminates h;hidden edges shown consistently
2025-1-Q10|14|125,50,450,273|diagram|inner circle touches both sector radii and outer arc; angle pi/3; NOT TO SCALE|sector angle and one radius|circle contacts both radii and outer arc;not to scale;contact-label topology|r=(R-r)*sin(theta/2);three contacts;positive radii;if angle changes R=3r no longer fixed;labels and quoted result change together
2025-1-Q11|16|130,55,455,271|graph|positive intersections A,B; shaded region between curves|parabola and reciprocal-square coefficients|downward quadratic and reciprocal-square curves;positive intersection branches;area between curves|two positive ordered intersections;denominator nonzero;area bounds a,b and curve ordering consistent
2025-1-Q12|18|115,50,460,274|diagram|ABCD rhombus; B on y-axis; A(-1,3),C(7,7)|A;C coordinates and chosen axis constraint|rhombus;B on y-axis;diagonals bisect perpendicularly;D is the opposite vertex|diagonals perpendicular and bisect each other;nondegenerate rhombus;D determined by reflection through midpoint AC
'''

DIAGRAM_PARTS = {'2024-2-Q6':{'b'}}

SKETCH_FEATURES = {
 '2021-1-Q12:c':(['Square-root branch on x>=-1, starting (-1,0)', 'Inverse branch on x>=0 reflected in y=x',
                   'Correct intercepts (0,sqrt(2)) and (sqrt(2),0), inverse (0,-1)', 'Label both curves and retain domains'],None),
 '2021-2-Q4:a':(['B1: correct descending exponential shape in first quadrant',
                 'B1: 5000 shown with correct shape; table condition on second quadrant retained in source excerpt'],238),
 '2022-1-Q6:c':(['Log graph x>2, vertical asymptote x=2 and intercept (3,0)',
                 'Inverse exponential with y=2 horizontal asymptote and intercept (0,3)',
                 'Both graphs labelled as reflections in y=x; no x-intercept for inverse'],None),
 '2023-2-Q6:c':(['B1: correct log shape/position in first and fourth quadrants; only one graph',
                 'B1: correct vertical asymptote x=2','B1: correct x-intercept (3,0)'],337),
 '2024-2-Q8:a':(['Increasing y=3e^x and decreasing y=e^(-x)',
                 'Both positive with horizontal asymptote y=0', 'Intercepts (0,3) and (0,1)'],341),
 '2024-2-Q11:a':(['B1: V-shape with vertex on positive x-axis',
                  'B1: straight line, positive gradient and negative y-intercept',
                  'Line x-intercept left of V vertex; no numerical intercepts required; straight by eye allowed'],343),
 '2025-1-Q4:a':(['One sine cycle over [0,pi], midline y=3, amplitude 2',
                 'Starts/ends y=3; minimum (pi/4,1), maximum (3pi/4,5); appropriate smooth shape'],None),
 '2025-1-Q4:b':(['Straight line on same domain/axes, from (0,2pi) to (pi,0)'],None),
 '2025-2-Q4:b':(['Sketch positive decreasing cosec x on (0,pi/2], vertical asymptote at 0, endpoint (pi/2,1)',
                 'Trapezium chords above curve on [pi/4,pi/2]; justify over-estimate'],None),
 '2025-2-Q11:a':(['Positive decaying exponential for t>=0; y-intercept 10; horizontal asymptote y=0'],None),
 '2025-2-Q12:a':(['V-shape |5-2x| with vertex (2.5,0) and y-intercept 5',
                  'Increasing 3ln x, x>0, vertical asymptote x=0 and x-intercept 1',
                  'Same axes with exactly two intersections shown'],None),
}

# Blank axes provided for a learner response, not mathematical input data.
RESPONSE_FRAMES = {
 '2021-1-Q12:c':(15,[140,115,450,422]),
 '2021-2-Q4:a':(6,[155,165,425,425]),
 '2023-2-Q6:c':(11,[100,86,490,450]),
 '2024-2-Q8:a':(12,[100,95,490,510]),
 '2024-2-Q11:a':(16,[95,116,490,510]),
 '2025-2-Q11:a':(12,[155,155,425,403]),
}
