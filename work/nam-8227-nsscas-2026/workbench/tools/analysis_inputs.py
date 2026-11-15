"""8227-specific analyst annotations. Source quotes are assembled from the PDFs.

These are proposed demand/selection judgements, not reviewed recipes or a new
shared authoring schema. Edit these inputs and rerun build_analysis.py.
"""

# theme.topic | source PDF page | topic title | specific-objective bullet anchors
# A slash in a demand separates independently inspectable learner actions.
OBJECTIVES = '''
M1.T1|8|Equations, expressions, identities and inequalities
complete the square|Complete square/Determine vertex/Sketch quadratic
find the discriminant|Calculate discriminant/Interpret nature and number of roots/Determine parameter conditions
interpret the difference between identities|Distinguish identity from equation/Determine coefficients by identity
recognise and solve equations|Recognise quadratic substitution/Solve transformed equation/Recover and filter original-variable roots
find the equation of a graph|Reconstruct quadratic/Reconstruct cubic from sufficient graph data
solve quadratic inequalities|Find critical values/Determine intervals and endpoint inclusion
M1.T2|9|Sequences and series
use the expansion|Expand positive-integer binomial/Extract chosen coefficient or term/Combine expansions and determine parameters
recognise arithmetic|Recognise AP/Recognise GP
use the formulae|Solve AP terms and sums/Solve GP terms and finite sums/Model progression context
interpret and apply the Sigma|Interpret Sigma bounds/Evaluate Sigma sum
use the condition|Determine GP convergence/Calculate convergent sum to infinity
M1.T3|9|Graphs and functions
interpret the terms function|Interpret function and notation/Interpret domain and range/Interpret one-to-one inverse and composite
identify the domain|Determine admissible domain/Determine image range
determine whether|Decide one-to-one status/Restrict branch and find inverse
form composite|Form and evaluate composition/Recognise decomposition and admissibility
sketch graphs of functions|Sketch function on specified domain/Sketch inverse and intercepts
M1.T4|10|Coordinate geometry
interpret the relationship between a graph|Translate geometric graph information into equation
use the relationship between points|Solve graph intersections/Interpret tangency as repeated root
M1.T5|10|Circular measure
interpret the term radian|Interpret radian/Convert degrees and radians
use the formulae|Use arc length/Use sector area/Find segment or compound-region area
M1.T6|11|Trigonometry
sketch and use graphs|Sketch and use basic trig graphs in degrees or radians
find the amplitude|Find amplitude and period/Interpret transformed trig graph/Sketch transformed trig graph
use the exact values|Evaluate exact special-angle ratios and related angles
use the notations|Interpret inverse trig principal values
use the trigonometric identities|Prove identity with basic identities/Transform trig equation using basic identities
find solutions|Solve bounded trig equations/Recover all roots in specified interval
M1.T7|12|Vectors in three dimensions
use rectangular Cartesian|Locate 3D coordinates/Read and write vector notations
perform addition|Add and subtract vectors/Scale vector/Interpret geometric vector relation
use unit vectors|Use unit vector/Use displacement vector/Use position vector
calculate the magnitude|Calculate magnitude/Calculate scalar product
use the scalar product|Find angle/Establish perpendicularity or solve perpendicularity parameter
M1.T8|12|Differentiation
interpret the idea|Interpret curve gradient/Use first and second derivative notation
use the derivative|Differentiate rational powers and linear combinations/Differentiate composite using chain rule
apply differentiation|Find tangent or normal/Determine increasing and decreasing intervals/Solve rate and connected-rate problems/Relate displacement velocity and acceleration
locate stationary|Locate stationary points/Classify maximum minimum or inflexion
M1.T9|13|Integration
interpret integration|Recognise reverse differentiation/Integrate powers of linear expressions and combinations
solve problems involving the evaluation|Determine integration constant/Recover curve through given point
evaluate definite|Evaluate definite integral/Evaluate prescribed simple improper integral
use definite integration|Find area between curve and line or two curves/Find volume about either axis/Relate displacement velocity acceleration by integration
M2.T1|14|Algebra
interpret and use the notation|Use modulus notation/Solve modulus equation/Solve modulus inequality
interpret and sketch|Sketch scaled or shifted modulus/Interpret modulus graph data
divide a polynomial|Divide degree-at-most-four polynomial by linear/Divide by quadratic/Identify quotient and remainder
apply the remainder|Apply remainder theorem/Apply factor theorem/Determine unknown coefficients/Solve polynomial by factorisation
M2.T2|14|Logarithmic and exponential functions
interpret the relationship between logarithms|Link logarithms and indices/Apply log laws without change of base
interpret the definition|Use exponential and natural log definitions/Interpret inverse relation and graphs
use logarithms to solve|Solve exponential equation/Solve exponential inequality and admissibility
use logarithms to transform|Linearise relationship/Determine constants from gradient and intercept
M2.T3|15|Trigonometry
recognise the relationship|Use reciprocal trig relationships/Use properties and graphs of all six functions
use trigonometrical identities|Choose and apply Pythagorean reciprocal identity/Use compound-angle identity/Use double-angle identity/Convert to R-form/Use identities for exact evaluation simplification or equations
M2.T4|15|Differentiation
use the derivatives|Differentiate exponential log and trig functions/Differentiate composite elementary function
differentiate products|Use product rule/Use quotient rule
find and use the first derivative|Differentiate implicit curve/Differentiate parametric curve/Use derivative in geometric demand
M2.T5|16|Integration
apply further the idea|Integrate exponential or reciprocal-linear form/Integrate sin cos or sec-squared linear argument/Recognise reverse derivative
use trigonometrical relationships|Choose identity before integration/Integrate transformed squared-trig expression
use the trapezium rule|Set trapezium interval and ordinates/Calculate estimate and required precision
use sketch graphs|Sketch integrand/Justify trapezium overestimate or underestimate
M2.T6|16|Numerical solutions of equations
locate approximately|Estimate root graphically/Bracket root by sign change
interpret the idea|Interpret iterative sequence and convergence/Recognise possible failure to converge
interpret how a given|Relate iteration to original equation/Derive or verify supplied rearrangement
use a given iteration|Execute supplied iteration/Apply stopping and precision requirements
'''

# Fxx | decision/evidence distinction | primary objective (theme.topic.ordinal)
FAMILIES = '''
01|Complete square and connect form to vertex or sketch|M1.T1.1
02|Use discriminant to establish root nature or parameter range|M1.T1.2
03|Determine coefficients from polynomial identity|M1.T1.3
04|Recognise quadratic in another expression and recover admissible roots|M1.T1.4
05|Reconstruct polynomial from graph information|M1.T1.5
06|Solve quadratic inequality with correct intervals|M1.T1.6
07|Select binomial terms or coefficients including combined products|M1.T2.1
08|Recognise and justify AP or GP structure|M1.T2.2
09|Determine AP parameters or finite sum|M1.T2.3
10|Determine GP parameters terms thresholds or finite sum|M1.T2.3
11|Interpret and evaluate a Sigma expression|M1.T2.4
12|Convergence conditions and sum to infinity of GP|M1.T2.5
13|Connect multiple AP and GP quantities in one demand|M1.T2.3
14|Find domain or range with branch and endpoint decisions|M1.T3.2
15|Choose one-to-one restriction and recover inverse|M1.T3.3
16|Form or evaluate composition including inadmissible input|M1.T3.4
17|Sketch function and inverse on specified domains|M1.T3.5
18|Translate coordinate geometry into equations intersections or tangency|M1.T4.2
19|Resolve circular geometry into arc sector segment or compound region|M1.T5.2
20|Read or construct trig graph and interpret parameters or signs|M1.T6.2
21|Use exact trig or principal inverse values|M1.T6.3
22|Demonstrate basic trigonometric identity|M1.T6.5
23|Transform and solve trig equation over specified interval|M1.T6.6
24|Infer vector or point from geometric relationships|M1.T7.2
25|Compute vector magnitude or unit representation|M1.T7.4
26|Use scalar product for angle perpendicularity or parameter|M1.T7.5
27|Differentiate powers composites or successive derivatives|M1.T8.2
28|Use derivative and geometry for tangent or normal|M1.T8.3
29|Locate and classify stationary behaviour|M1.T8.4
30|Build constrained geometric model and optimise|M1.T8.4
31|Model and evaluate connected rates or acceleration at an event|M1.T8.3
32|Recover curve or constant by integration and initial conditions|M1.T9.2
33|Evaluate definite or improper integral and limiting behaviour|M1.T9.3
34|Determine integration region bounds and area|M1.T9.4
35|Choose axis and integrand for volume of revolution|M1.T9.4
36|Integrate motion with initial conditions or interval|M1.T9.4
37|Solve modulus equations or inequalities using cases and admissibility|M2.T1.1
38|Sketch or infer parameters of modulus graph|M2.T1.2
39|Polynomial division and interpretation of remainder|M2.T1.3
40|Use factor or remainder data to determine coefficients|M2.T1.4
41|Use factor theorem and division to factorise or solve polynomial|M2.T1.4
42|Apply log laws with domain and equivalence checks|M2.T2.1
43|Sketch exponential or logarithmic function and interpret parameters|M2.T2.2
44|Solve exponential or logarithmic equations or inequalities|M2.T2.3
45|Linearise exponential relationship and infer constants from graph|M2.T2.4
46|Use reciprocal trigonometric relationships or graph|M2.T3.1
47|Select compound double-angle or reciprocal identity and use it|M2.T3.2
48|Construct R-form and solve bounded trig equation|M2.T3.2
49|Use R-form or identity to establish an extremum|M2.T3.2
50|Differentiate elementary exponential logarithmic or trig composite|M2.T4.1
51|Differentiate product or quotient for geometric demand|M2.T4.2
52|Parametric differentiation including tangent or vertical tangent|M2.T4.3
53|Implicit differentiation and evaluation or normal|M2.T4.3
54|Choose elementary reverse derivative or antiderivative|M2.T5.1
55|Use identity or earlier derivative to evaluate trig integral|M2.T5.2
56|Calculate trapezium estimate with stated intervals and precision|M2.T5.3
57|Use graph shape to justify trapezium bias|M2.T5.4
58|Use graph intersections to establish root count|M2.T6.1
59|Establish root bracket by function signs|M2.T6.1
60|Derive or verify fixed-point rearrangement|M2.T6.3
61|Execute fixed-point iteration to prescribed accuracy|M2.T6.4
62|Interpret convergence or nonconvergence of iterative sequence|M2.T6.2
'''

# year-paper Q | PDF pages | connected-pattern annotation | part:families:marks
# Families are analyst proposals. First family is the proposed primary assessed
# objective; additional families are directly assessed secondary links.
QUESTIONS = '''
2021-1 1|2|Expansion followed by coefficient condition|a:07:2;b:07:3
2021-1 2|3|Reconstruct parabola from diagram and vertex|answer:05:3
2021-1 3|4|Quartic roots reused after radical substitution|a:04:2;b:04:3
2021-1 4|5|Acceleration to velocity to displacement with initial data|a:36:3;b:36:3
2021-1 5|6|Bounded trig equation and separate identity proof|a:23:3;b:22:3
2021-1 6|7|Point on vector segment and perpendicularity proof|a:24:4;b:26:2
2021-1 7|8|Compound circular plate perimeter and area|a:19:3;b:19:3
2021-1 8|9|Compare GP donation sum with AP donation sum|a:10:3;b:13+09:3
2021-1 9|10,11|Region area then revolution around y-axis|a:34:3;b:35:4
2021-1 10|12|Nonintersection parameter condition and root-nature explanation|a:02+18:4;b:02:2
2021-1 11|13|Stationary point and normal of algebraic curve|a:29:4;b:28:3
2021-1 12|14,15|Radical domain inverse paired sketch and derivative|a:14:2;b:15+14:3;c:17:4;d:27:3
2021-2 1|2,3|Remainder coefficients then distinct cubic-root task|a:40:3;b:41:4
2021-2 2|4|Exact reciprocal-linear definite-integral demonstration|answer:54+33:4
2021-2 3|5|Compare two absolute-value expressions in inequality|answer:37:4
2021-2 4|6|Exponential decline sketch and whole-week threshold|a:43:2;b:44:3
2021-2 5|7|Product derivative reused as antiderivative|a:51:3;b:54+33:2
2021-2 6|8|Expand shifted trig expressions then solve acute angle|a:47:4;b:23+47:2
2021-2 7|9|Parametric intersections with axis and two tangents|answer:52+28:6
2021-2 8|10|Bracket derive iteration execute and report root|a:59:2;b:60:2;c.i:61:2;c.ii:61:1
2021-2 9|11|Elementary integral and double-angle definite integral|a:54:3;b:55+33:4
2021-2 10|12|Implicit derivative then normal at specified input|a:53:3;b:53+28:3
2021-2 11|13|Log equation reduced to quadratic then exponential substitution|a:42+04:3;b:44+04:4
2021-2 12|14,15|R-form bounded root and separate double-angle equation|a.i:48:3;a.ii:48+23:3;b:47+23:5
2022-1 1|2|Completed square then vertex|a:01:3;b:01:1
2022-1 2|3|Quadratic roots reused under transformed variable|a:04:2;b:04:2
2022-1 3|4|Combined binomial coefficient determines parameter|answer:07:4
2022-1 4|5|Strict real-root discriminant parameter range|answer:02:4
2022-1 5|6,7|AP parameter recovery and Sigma infinite GP|a:09:4;b:11+12:3
2022-1 6|8|Log domain inverse and paired graph|a:14:1;b:15:2;c:17+43:4
2022-1 7|9|Tangent condition recovers point and intercept|answer:28+18:4
2022-1 8|10,11|Wire sector model then stationary-area classification|a:19+30:4;b:30+29:4
2022-1 9|12|Trig reduction to quadratic then interval roots|a:22+23:2;b:23:3
2022-1 10|13|Read transformed trig graph period and reflected equation|a:20:3;b:20:1;c:20:1
2022-1 11|14,15|Trapezium vector relation then scalar-product angle|a:24:3;b:26:4
2022-1 12|16,17|Similar cone dimensions then connected inflow rate|a:31:2;b:31:4
2022-1 13|18|Recover curve with contradictory stated domain and point|answer:32:4
2022-1 14|19|Read intercepts then revolve region about x-axis|a:18:2;b:35:4
2022-2 1|2|Modulus roots reused in exponential equation|a:37:3;b:44+37:2
2022-2 2|3|Quadratic in exponential with logarithmic recovery|answer:44+04:4
2022-2 3|4,5|Trig intercept gradient and shaded integral area|a:23:2;b:50:5;c:55+34:5
2022-2 4|6|Coupled polynomial remainder data then quadratic extremum|a:40:5;b:01:2
2022-2 5|7|Gradient condition gives iteration and numerical root|a:51+60:4;b:59:3;c:61:2
2022-2 6|8|R-form bounded equation and extrema|a:48:3;b.i:48+23:4;b.ii:49:2
2022-2 7|9|Reciprocal identity reused at changed argument in integral|a:47:4;b:55:3
2022-2 8|10|Unknown integral limit determined by exact logarithm|answer:54+33+44:6
2022-2 9|11|Log domain inverse range and valid or invalid compositions|a:14:1;b.i:15:2;b.ii:14:1;c.i:16:2;c.ii:16+14:2
2022-2 10|12|Parametric gradient and vertical-tangent condition|a:52:5;b:52:3
2023-1 1|2,3|Quadratic inequality and general discriminant proof|a:06:3;b:02:4
2023-1 2|4,5|Rational inverse domain and composed-function parameter|a:15:3;b:14:1;c.i:16:1;c.ii:16:2
2023-1 3|6|Unknown coefficients in rational identity|answer:03:4
2023-1 4|7|Binomial expansion followed by product coefficient equation|a:07:2;b:07:3
2023-1 5|8,9|Recognise GP determine convergence range and sum parameter|a:08:2;b:12:2;c:12:5
2023-1 6|10,11|Concentric arc tangent geometry and shaded area|a:19:2;b:19:3
2023-1 7|12,13|Vector chain magnitudes and scalar-product angle|a.i:24:2;a.ii:24:2;b.i:25:2;b.ii:26:3
2023-1 8|14,15|Identity proof reused in bounded trig equation|a:22:4;b:23:3
2023-1 9|16|Principal inverse trig value and algebraic recovery|answer:21+04:3
2023-1 10|17|Height model differentiation and maximum event|a:29+31:3;b:29:2
2023-1 11|18|Successive derivatives of reciprocal-linear expression|answer:27:4
2023-1 12|19|Improper area limit demonstrated and evaluated|answer:33+34:4
2023-1 13|20,21|Fixed-volume cylinder surface-area model and optimum|a:30:2;b:30:4
2023-2 1|2|Polynomial division then adjusted polynomial factors and roots|a:39:3;b:41:3;c:41:1
2023-2 2|3|Infer modulus graph parameters from vertex and intercepts|answer:38:3
2023-2 3|4,5|Shifted trig equation and identity exact evaluation integral chain|a:47+23:4;b.i:47:4;b.ii:47:2;b.iii:55:3
2023-2 4|6,7|Linearised exponential graph and separate log equations|a:45:5;b:44:3;c:42+44:3
2023-2 5|8,9|Quotient stationary point and definite trig integral|a:51+29:5;b:55+33:6
2023-2 6|10,11|Trapezium estimate transformed integral graph and bias|a:56:3;b:56+42:2;c:43:3;d:57:2
2023-2 7|12,13|Integral boundary becomes bracketed fixed-point problem|a:54+60:4;b:59:2;c:61:3
2023-2 8|14|Implicit derivative then axis-intercept gradient|a:53:4;b:53:2
2023-2 9|15|Exponential motion acceleration and distance|a:50+31:2;b:54+36:3
2024-1 1|2|Quadratic in exponential under supplied substitution|answer:04+44:4
2024-1 2|3|Compare coefficients in polynomial product identity|answer:03:4
2024-1 3|4|Select constant term in binomial with reciprocal power|answer:07:3
2024-1 4|4,5|GP pump ratio threshold and infinite total|a:10:2;b:10:3;c:12:2
2024-1 5|6|No-real-root parameter range then specific root count|a:02:3;b:02:2
2024-1 6|7|Complete square bounded range and restricted inverse|a:01:3;b:14:2;c:15:2
2024-1 7|8,9|Touching-circle common tangent angle and shaded region|a:19:2;b:19:4
2024-1 8|10|Coordinate reflection via perpendicular line and midpoint|answer:18:5
2024-1 9|11|Two trig graphs parameters period and sign of product|a:20:2;b:20:1;c:20:2
2024-1 10|12,13|3D pyramid midpoint vectors and angle|a:24:2;b:24:1;c:26:4
2024-1 11|14,15|Door perimeter constraint area model and maximum|a:30:2;b:30:3;c:30:2
2024-1 12|16|Trig quadratic reduction then bounded roots|a:22+23:2;b:23:3
2024-1 13|17|Normal gradient determines derivative parameter then curve|a:28:3;b:32:3
2024-1 14|18|Area between line and parabola|answer:34:4
2024-2 1|2|Quotient derivative evaluated at point|answer:51:3
2024-2 2|3|Required compound-angle expansion before bounded solving|answer:47+23:5
2024-2 3|4|Logarithmic inequality with domain intersection|answer:42+44:5
2024-2 4|5|Composite exponential derivative reused in integral|a:50:3;b:54:2
2024-2 5|6,7|Polynomial quotient rational integral and trig substitution roots|a:39:3;b:39+54:3;c:41+46+23:5
2024-2 6|8,9|Trig-identity definite integral then revolution|a:55+33:6;b:35+55:4
2024-2 7|10,11|Parametric point iteration then gradient at numerical point|a:60:2;b:61:3;c:52+51:5
2024-2 8|12,13|Two exponential sketches and exact intersection|a:43:4;b:44:4
2024-2 9|14|Reciprocal identity to tangent then exact compound angle|a:46+47:3;b:47:3
2024-2 10|15|Log stationary point and nature|a:50+29:4;b:29:2
2024-2 11|16,17|Parameterized modulus-line sketch intersection and inequality|a:38:2;b:37:3;c:37:1
2025-1 1|2|General rational-root proof then quadratic inequality instance|a:02:3;b:06:3
2025-1 2|3|Combined expansion coefficient determines parameter|answer:07:4
2025-1 3|4,5|Perpendicularity parameter then vector angle|a:26:3;b:26:4
2025-1 4|6|Trig and line sketches followed by intersection root count|a:20:3;b:18:1;c:58:1
2025-1 5|7|Sums of three GPs form AP|a:13+12:3;b:13+09:2
2025-1 6|8,9|Identity proof then cubic-trig equation reduction|a:22:3;b:23:4
2025-1 7|10|Completed square one-to-one restriction range and inverse domain|a:01:2;b:15:1;c:14:1;d:15+14:4
2025-1 8|11|Gradient data determines parameter then initial-value curve|a:27:1;b:32:4
2025-1 9|12,13|Fixed-volume triangular-prism area model and classification|a:30:4;b:30:3;c:29:2
2025-1 10|14,15|Circle inscribed in sector then area ratio|a:19:2;b:19:3
2025-1 11|16,17|Curve intersections quartic substitution then enclosed area|a:18:1;b:04:3;c:34:4
2025-1 12|18,19|Rhombus diagonal line then remaining vertices|a:18:4;b:18:2
2025-2 1|2|Factor and remainder constraints recover coefficients|answer:40:5
2025-2 2|3|Exponential equation with modulus in exponent|answer:37+44:4
2025-2 3|3|Reciprocal ratio then exact angle difference|answer:46+47:4
2025-2 4|4|Trapezium reciprocal-trig estimate and graph-based bias|a:56:3;b:57+46:2
2025-2 5|5|Implicit exponential-product derivative at point|answer:53+51:5
2025-2 6|6|Log-base linearisation identifies parameter then unknown input|a:45:3;b:44:2
2025-2 7|7|Double-angle identity reused to establish maximum|a:47:3;b:49:3
2025-2 8|8|Rest event from rational velocity then acceleration|answer:31+51:7
2025-2 9|9|R-form then transformed cotangent-cosecant equation|a:48:3;b:48+46+23:5
2025-2 10|10,11|Derivative relation reused for exact multi-term trig integral|a:50:2;b:55+54:6
2025-2 11|12,13|Radioactive decay sketch fractional threshold and rate|a:43:2;b:44:3;c:50+31:3
2025-2 12|14,15|Modulus-log root count rearrangement bracket and iteration|a:58+38+43:3;b:60:2;c:59:2;d:61:3
'''
