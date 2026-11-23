"""Explicit one-item author source records, checked against rendered textbook pages.
No inferred ranges; source defects and answer checks are held in companion inputs.
"""
GOLDIE = r'''
1A|1||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|2||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|3||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|4||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|5||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|6||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|7||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|8||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|9||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|10||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|11||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|12||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|13||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|14||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|15||text|no|no|Supporting polynomial notation/arithmetic; no directly assessed 8227 objective claimed
1A|16|2.1.3.1,2.1.3.3|text|no|no|Degree at most four divided by linear; LIMIT05
1A|17|2.1.3.1,2.1.3.3|text|no|no|Degree at most four divided by linear; LIMIT05
1A|18|2.1.3.1,2.1.3.3|text|no|no|Degree at most four divided by linear; LIMIT05
1A|19|2.1.3.1,2.1.3.3|text|no|no|Degree at most four divided by linear; LIMIT05
1A|20|2.1.3.1,2.1.3.3|text|no|no|Degree at most four divided by linear; LIMIT05
1A|21|2.1.3.1,2.1.3.3|text|no|no|Degree at most four divided by linear; LIMIT05
1A|22|2.1.3.1,2.1.3.3|text|no|no|Degree at most four divided by linear; LIMIT05
1A|23|2.1.3.1,2.1.3.3|text|no|no|Degree at most four divided by linear; LIMIT05
1A|24|2.1.3.2,2.1.3.3|text|no|no|Degree four divided by quadratic; LIMIT05
1A|25|2.1.3.2,2.1.3.3|text|no|no|Degree four divided by quadratic; LIMIT05
1A|26|2.1.3.2,2.1.3.3|text|no|no|Degree four divided by quadratic; LIMIT05
1A|27|2.1.3.2,2.1.3.3|text|no|no|Degree four divided by quadratic; LIMIT05
1A|28|2.1.3.2,2.1.3.3|text|no|no|Degree four divided by quadratic; LIMIT05
1B|1|2.1.4.2,2.1.4.4,1.3.5.1|text|yes|no|Root evaluation, factorisation, solve and sketch; quartic in Q5 remains within polynomial/function scope
1B|2|2.1.4.2,2.1.4.4,1.3.5.1|text|yes|no|Root evaluation, factorisation, solve and sketch; quartic in Q5 remains within polynomial/function scope
1B|3|2.1.4.2,2.1.4.4,1.3.5.1|text|yes|no|Root evaluation, factorisation, solve and sketch; quartic in Q5 remains within polynomial/function scope
1B|4|2.1.4.2,2.1.4.4,1.3.5.1|text|yes|no|Root evaluation, factorisation, solve and sketch; quartic in Q5 remains within polynomial/function scope
1B|5|2.1.4.2,2.1.4.4,1.3.5.1|text|yes|no|Root evaluation, factorisation, solve and sketch; quartic in Q5 remains within polynomial/function scope
1B|6|2.1.4.2,2.1.4.4,1.3.5.1|text|yes|no|Root evaluation, factorisation, solve and sketch; quartic in Q5 remains within polynomial/function scope
1B|7|1.1.5.2,2.1.4.4|graph|no|no|Recover cubic parameters from roots and intercept then solve the equation; given graph continues onto next page
1B|8|1.1.4.1,1.1.4.2,1.1.4.3,2.1.4.4|text|no|no|Quadratic in x squared; filter real roots
1B|9|2.1.4.2,2.1.3.1,2.1.3.3|text|no|no|Show non-factor then divide
1B|10|2.1.4.2,2.1.4.4|text|no|no|Find and verify factors/roots with working
1B|11|2.1.4.2,2.1.4.4|text|no|no|Find and verify factors/roots with working
1B|12|2.1.4.2,2.1.3.1,2.1.3.2,2.1.3.3|text|no|no|Non-roots and linear/quadratic division; LIMIT05
1B|13|2.1.4.1,2.1.4.3|text|no|no|Remainders determine coefficients; Q16 also solves the cubic
1B|14|2.1.4.1,2.1.4.3|text|no|no|Remainders determine coefficients; Q16 also solves the cubic
1B|15|2.1.4.1,2.1.4.3|text|no|no|Remainders determine coefficients; Q16 also solves the cubic
1B|16|2.1.4.1,2.1.4.3|text|no|no|Remainders determine coefficients; Q16 also solves the cubic
1B|17|2.1.4.1,2.1.4.2,2.1.4.3|text|no|yes|Attributed Cambridge items embedded in book; internal textbook evidence only
1B|18|2.1.4.1,2.1.4.2,2.1.4.3|text|no|yes|Attributed Cambridge items embedded in book; internal textbook evidence only
1B|19|2.1.4.1,2.1.4.2,2.1.4.3|text|no|yes|Attributed Cambridge items embedded in book; internal textbook evidence only
1B|20|2.1.4.1,2.1.4.2,2.1.4.3|text|no|yes|Attributed Cambridge items embedded in book; internal textbook evidence only
1B|21|2.1.4.2,2.1.4.3,2.1.3.2,2.1.3.3|text|no|yes|Find coefficients then quadratic-divisor remainder
1B|22|2.1.3.2,2.1.3.3,2.1.4.4|text|no|yes|Divide quartic by quadratic then hence solve
1B|23|2.1.4.1,2.1.4.2,2.1.4.3,1.1.1.1,1.1.1.2|text|no|yes|Two polynomial conditions then greatest value of their quadratic difference
1C|1|2.1.1.1,2.1.1.2|text|no|no|Solve one- and two-modulus equations
1C|2|2.1.1.1,2.1.1.3|text|no|no|Solve inequalities; reverse task expresses an interval as modulus inequality
1C|3|2.1.1.1,2.1.1.3|text|no|no|Solve inequalities; reverse task expresses an interval as modulus inequality
1C|4|2.1.2.1|text|yes|no|Sketch translated/scaled modulus with integer coefficients
1C|5|2.1.1.3|text|no|no|Compare two modulus expressions
1C|6|2.1.1.3|text|no|yes|Numerical and positive-parameter modulus inequalities
1C|7|2.1.1.3|text|no|yes|Numerical and positive-parameter modulus inequalities
1C|8|2.1.1.2|text|no|yes|Equation includes linear and cubic-inside-modulus branches
1C|9|2.1.1.2|text|no|yes|Equation includes linear and cubic-inside-modulus branches
2A|1|2.2.2.2|text|yes|no|Exponential sketches, asymptote and intercept
2A|2|2.2.2.2|text|yes|no|Exponential sketches, asymptote and intercept
2A|3|2.2.2.1,2.2.2.2|text|yes|no|Model evaluation and long-term/asymptotic interpretation; Q4 also asks trial-and-improvement
2A|4|2.2.2.1,2.2.2.2|text|yes|no|Model evaluation and long-term/asymptotic interpretation; Q4 also asks trial-and-improvement
2A|5|2.2.2.1,2.2.2.2|text|yes|no|Model evaluation and long-term/asymptotic interpretation; Q4 also asks trial-and-improvement
2A|6|2.2.1.1,2.2.3.1|table|no|no|Frequency powers-of-two model and inverse unknown-octave decision
2B|1|2.2.1.1|text|no|no|Convert between exponential and logarithmic forms and evaluate
2B|2|2.2.1.1|text|no|no|Convert between exponential and logarithmic forms and evaluate
2B|3|2.2.1.1|text|no|no|Convert between exponential and logarithmic forms and evaluate
2B|4|2.2.1.2|text|no|no|Combine and expand log expressions without change of base
2B|5|2.2.1.2|text|no|no|Combine and expand log expressions without change of base
2B|6|2.2.2.2|text|yes|no|Log graphs, vertical asymptotes and intercepts
2B|7|2.2.3.2|text|no|no|Exponential inequalities including modulus forms; reverse sign for base below one
2B|8|2.2.1.2|text|no|no|Combine logs then solve with log domain
2B|9|2.2.3.1|text|no|no|Simple and disguised-quadratic exponential equations
2B|10|2.2.3.1|text|no|no|Simple and disguised-quadratic exponential equations
2B|11|1.2.3.2,2.2.3.1|text|no|no|Inverse geometric-progression term count, including negative ratio
2B|12|1.2.3.2,2.2.3.1|text|no|no|Inverse geometric-progression term count, including negative ratio
2B|13|2.2.1.1,2.2.1.2,2.2.3.1|text|no|no|Logarithmic physical scales; evaluate, invert and explain multiplicative comparison
2B|14|2.2.1.1,2.2.1.2,2.2.3.1|text|no|no|Logarithmic physical scales; evaluate, invert and explain multiplicative comparison
2B|15|2.1.1.3,2.2.3.2|text|no|yes|Modulus inequality followed by exponential substitution
2B|16|2.1.1.2,2.2.3.1|text|no|yes|Modulus/exponential equation with root filtering
2B|17|1.1.4.1,1.1.4.2,1.1.4.3,2.2.3.1|text|no|yes|Reciprocal exponential yields a quadratic substitution
2B|18|2.2.1.2|text|no|yes|Log equation and admissibility
2B|19|2.1.4.2,2.1.4.3,2.1.4.4,2.2.3.1|text|no|yes|Polynomial factorisation scaffolds exponential equation; discard non-positive substituted roots
2B|20|2.1.4.2,2.1.4.3,2.1.4.4,2.2.3.1|text|no|yes|Polynomial factorisation scaffolds exponential equation; discard non-positive substituted roots
2C|1|2.2.4.1,2.2.4.2|table|yes|no|Choose log axes, plot data, estimate constants and use model
2C|2|2.2.4.1,2.2.4.2|table|yes|no|Choose log axes, plot data, estimate constants and use model
2C|3|2.2.4.1,2.2.4.2|graph|no|no|Read line gradients/intercepts and recover model parameters; Q4 includes extrapolation limitation
2C|4|2.2.4.1,2.2.4.2|graph|no|no|Read line gradients/intercepts and recover model parameters; Q4 includes extrapolation limitation
2C|5|2.2.4.1,2.2.4.2|graph|no|no|Read line gradients/intercepts and recover model parameters; Q4 includes extrapolation limitation
2C|6|2.2.4.1,2.2.4.2|table|yes|no|Investigate candidate models; choose transformation and discuss fit/long-term limits
2C|7|2.2.4.1,2.2.4.2|table|yes|no|Investigate candidate models; choose transformation and discuss fit/long-term limits
2C|8|2.2.4.1,2.2.4.2|table|yes|no|Investigate candidate models; choose transformation and discuss fit/long-term limits
2C|9|2.2.4.1,2.2.4.2,2.2.3.1|text|no|yes|Linearise 3^y=4^{x+2}; log ratio arises from solving, not a standalone change-of-base formula task
2D|1|2.2.1.1,2.2.1.2|text|no|no|Make variable subject in natural-log/exponential relationships
2D|2|2.2.1.1,2.2.1.2|text|no|no|Make variable subject in natural-log/exponential relationships
2D|3|2.2.1.1,2.2.1.2|text|no|no|Make variable subject in natural-log/exponential relationships
2D|4|2.2.1.1,2.2.1.2|text|no|no|Make variable subject in natural-log/exponential relationships
2D|5|2.2.1.2,2.2.3.1|text|no|no|Logarithmic and disguised-quadratic exponential equations with admissibility
2D|6|2.2.2.2,2.2.3.1|text|yes|no|Exponential population model, initial value and inverse time
2D|7|2.2.3.1,2.2.4.1,2.2.4.2|graph|no|no|Growth/price model with log-log plot; inverse time
2D|8|2.2.1.2,2.2.3.1|text|no|yes|Rearrange logs, ratio of exponents, and quadratic substitution in e^x
2D|9|2.2.1.2,2.2.3.1|text|no|yes|Rearrange logs, ratio of exponents, and quadratic substitution in e^x
2D|10|2.2.1.2,2.2.3.1|text|no|yes|Rearrange logs, ratio of exponents, and quadratic substitution in e^x
2D|11|2.2.4.1,2.2.4.2|graph|no|yes|Read ln y versus x for A b^{-x}; sign matters
2D|12|2.2.3.1|text|no|yes|Nested log/exponential equation
2D|13|2.2.4.1,2.2.4.2|graph|no|yes|Power-law or shifted exponential model; read gradient/intercept rather than plotted ordinate
2D|14|2.2.4.1,2.2.4.2|graph|no|yes|Power-law or shifted exponential model; read gradient/intercept rather than plotted ordinate
3A|1|2.3.1.1,1.6.6.1,1.6.6.2|text|no|no|Reciprocal trigonometric equations in finite degree interval
3A|2|2.3.1.1,1.6.3.1|text|no|no|Exact reciprocal ratios at related special angles
3A|3|2.3.1.1,2.3.2.1|text|no|no|Right-triangle ratios and Pythagorean reciprocal identity
3A|4|2.3.1.1,2.3.2.1|text|no|no|Right-triangle ratios and Pythagorean reciprocal identity
3A|5|2.3.1.1|text|no|no|Shadow-height cotangent application
3A|6|2.3.1.2|text|no|no|Sign/equality decisions across all quadrants; explanations
3A|7|2.3.1.1,2.3.2.1,1.6.6.1,1.6.6.2|text|no|no|Reciprocal identities reduce bounded equations
3B|1|2.3.2.2,1.6.3.1|text|no|no|Exact special-angle values from compound-angle formulae
3B|2|2.3.2.2,2.3.2.5|text|no|no|Expand or recognise compound-angle expressions
3B|3|2.3.2.2,2.3.2.5|text|no|no|Expand or recognise compound-angle expressions
3B|4|2.3.2.2,1.6.6.1,1.6.6.2|text|no|no|Bounded compound-angle equations in degrees/radians
3B|5|2.3.2.2,1.6.6.1,1.6.6.2|text|no|no|Bounded compound-angle equations in degrees/radians
3B|6|2.3.1.1,2.3.2.2,2.3.2.5|diagram|no|no|Coordinates give signed angle ratios, then exact compound angles and interpretation
3B|7|2.3.2.1,2.3.2.2,2.3.2.5|text|no|yes|Pythagorean reciprocal identity and compound-angle exact evaluation
3B|8|2.3.2.2,2.3.2.5,1.6.6.1,1.6.6.2|text|no|yes|Quadratic reductions and coupled angle conditions; exact evaluation in Q11
3B|9|2.3.2.2,2.3.2.5,1.6.6.1,1.6.6.2|text|no|yes|Quadratic reductions and coupled angle conditions; exact evaluation in Q11
3B|10|2.3.2.2,2.3.2.5,1.6.6.1,1.6.6.2|text|no|yes|Quadratic reductions and coupled angle conditions; exact evaluation in Q11
3B|11|2.3.2.2,2.3.2.5,1.6.6.1,1.6.6.2|text|no|yes|Quadratic reductions and coupled angle conditions; exact evaluation in Q11
3C|1|2.3.2.3,1.6.6.1,1.6.6.2|text|no|no|Double-angle reductions, bounded roots; Q3 derives sin3θ from compound/double angles
3C|2|2.3.2.3,1.6.6.1,1.6.6.2|text|no|no|Double-angle reductions, bounded roots; Q3 derives sin3θ from compound/double angles
3C|3|2.3.2.3,1.6.6.1,1.6.6.2|text|no|no|Double-angle reductions, bounded roots; Q3 derives sin3θ from compound/double angles
3C|4|2.3.2.3,1.6.6.1,1.6.6.2|text|no|no|Double-angle reductions, bounded roots; Q3 derives sin3θ from compound/double angles
3C|5|2.3.2.3,1.6.6.1,1.6.6.2|text|no|no|Double-angle reductions, bounded roots; Q3 derives sin3θ from compound/double angles
3C|6|2.3.2.3,1.6.1.1,1.6.6.1,1.6.6.2|text|yes|no|Sketch two functions, obtain quadratic in sinx, recover all roots
3C|7|2.3.2.2,2.3.2.3,2.3.2.5|text|no|no|Prove identities and infer related angle without calculator
3C|8|2.3.2.2,2.3.2.3,2.3.2.5|text|no|no|Prove identities and infer related angle without calculator
3C|9|2.3.2.3,1.6.1.1,1.6.6.1,1.6.6.2|text|yes|no|Graphs then identity-based bounded intersection calculation
3C|10|2.3.2.2,2.3.2.3,2.3.2.5,1.6.6.1|text|no|yes|Proof/exact evaluation or hence equation with bounded domain
3C|11|2.3.2.2,2.3.2.3,2.3.2.5,1.6.6.1|text|no|yes|Proof/exact evaluation or hence equation with bounded domain
3C|12|2.3.2.2,2.3.2.3,2.3.2.5,1.6.6.1|text|no|yes|Proof/exact evaluation or hence equation with bounded domain
3C|13|2.3.2.2,2.3.2.3,2.3.2.5,1.6.3.1|text|no|yes|Exact compound and double-angle values; tan3α deduced from compound formula
3D|1|2.3.2.4|text|no|no|Choose correct R-form and phase quadrant
3D|2|2.3.2.4|text|no|no|Choose correct R-form and phase quadrant
3D|3|2.3.2.4|text|no|no|Choose correct R-form and phase quadrant
3D|4|2.3.2.4|text|no|no|Choose correct R-form and phase quadrant
3D|5|2.3.2.4|text|no|no|Choose correct R-form and phase quadrant
3D|6|2.3.2.4,1.6.2.3,1.6.6.1,1.6.6.2|text|yes|no|R-form, extrema and phase locations, sketches and equations; Q9 reciprocal expression extrema
3D|7|2.3.2.4,1.6.2.3,1.6.6.1,1.6.6.2|text|yes|no|R-form, extrema and phase locations, sketches and equations; Q9 reciprocal expression extrema
3D|8|2.3.2.4,1.6.2.3,1.6.6.1,1.6.6.2|text|yes|no|R-form, extrema and phase locations, sketches and equations; Q9 reciprocal expression extrema
3D|9|2.3.2.4,1.6.2.3,1.6.6.1,1.6.6.2|text|yes|no|R-form, extrema and phase locations, sketches and equations; Q9 reciprocal expression extrema
3D|10|2.3.2.4,1.6.6.1,1.6.6.2|diagram|no|no|Rectangle in corridor gives two inclination solutions; figure continues on next page
3D|11|2.3.2.4,1.6.6.1,1.6.6.2|text|no|yes|R-form then bounded equation; phase precision stated
3D|12|2.3.2.4,1.6.6.1,1.6.6.2|text|no|yes|R-form then bounded equation; phase precision stated
3D|13|2.3.2.4,1.6.6.1,1.6.6.2|text|no|yes|R-form then bounded equation; phase precision stated
3D|14|2.3.2.4,1.6.6.1,1.6.6.2|text|no|yes|R-form then bounded equation; phase precision stated
3E|1|2.3.2.2,2.3.2.3,2.3.2.5|text|no|no|Mixed identity simplification; bounded tasks, not the following general-solutions section
3E|2|2.3.2.2,2.3.2.3,2.3.2.5|text|no|no|Mixed identity simplification; bounded tasks, not the following general-solutions section
3E|3|2.3.2.3,2.3.2.5|text|no|no|Prove identities, including tan4θ from repeated double-angle formulae
3E|4|2.3.2.2,2.3.2.3,2.3.2.4,1.6.6.1,1.6.6.2|text|no|no|Choose method for seven finite-interval equations; LIMIT02 satisfied
4A|1|2.4.2.1,2.4.2.2|text|no|no|Explicit product/quotient differentiation
4A|2|2.4.2.2,2.4.3.3,1.8.3.1|graph|no|no|Differentiate rational curve; tangent equations and relationship
4A|3|2.4.2.1,2.4.2.2,1.8.4.1,1.8.4.2,1.3.5.1|text|yes|no|Stationary points, tangent/normal and sketch; polynomial expansion is a valid alternative where applicable
4A|4|2.4.2.1,2.4.2.2,1.8.4.1,1.8.4.2,1.3.5.1|text|yes|no|Stationary points, tangent/normal and sketch; polynomial expansion is a valid alternative where applicable
4A|5|2.4.2.2,1.8.4.1,1.8.4.2,1.8.3.1,1.4.1.1|graph|no|no|Rational/square-root curve, normal/tangent intersections and triangle area
4A|6|2.4.2.2,1.8.4.1,1.8.4.2|graph|no|no|Quotient curve and classify stationary points with calculus
4A|7|2.4.2.2,1.8.4.1,1.8.4.2|text|no|no|Rational stationary-point calculation/classification
4A|8|1.8.2.2,2.4.2.1,1.8.4.1,1.8.3.1|graph|no|no|Product plus chain differentiation; maximum and endpoint vertical-tangent interpretation
4B|1|2.4.1.1,2.4.1.2,2.4.2.1,2.4.2.2|text|no|no|Mixed log/exponential derivatives with chain/product/quotient as appropriate
4B|2|2.4.1.1,2.4.1.2,2.4.2.1,2.4.2.2|text|no|no|Mixed log/exponential derivatives with chain/product/quotient as appropriate
4B|3|2.4.1.2,1.8.3.3|text|no|no|Exponential river-height model and rates at stated times
4B|4|2.4.1.1,2.4.2.1,1.8.4.1,1.8.4.2|graph|no|no|Given exponential/log graphs, first/second derivatives and stationary coordinates; Q5 symmetry
4B|5|2.4.1.1,2.4.2.1,1.8.4.1,1.8.4.2|graph|no|no|Given exponential/log graphs, first/second derivatives and stationary coordinates; Q5 symmetry
4B|6|2.4.2.2,1.8.4.1,1.3.5.1|text|yes|no|Differentiate exp quotient, stationary point and sketch
4B|7|2.4.2.1,1.8.4.1|graph|no|no|Exact stationary coordinates for xlnx
4B|8|2.4.2.2,1.8.4.1,1.8.4.2|text|no|no|Stationary point and classification of x^3/e^x
4B|9|2.4.2.2,1.8.4.1,1.3.5.1|text|yes|no|Log quotient: intercept, stationary coordinates and sketch
4B|10|2.4.2.1,1.8.1.2|text|no|yes|Locate y''=0 on exponential-product curve; does not by itself assess inflexion classification
4B|11|2.4.2.1,1.8.4.1,1.8.4.2|text|no|yes|Exponential stationary point and classification
4B|12|2.4.2.1,1.8.4.1,1.8.3.1|text|no|yes|Show stationary abscissa and find tangent
4C|1|2.4.1.1|text|no|no|Elementary trig differentiation
4C|2|2.4.1.1,2.4.2.1|text|no|no|Explicit product rule with trig functions
4C|3|2.4.1.1,2.4.2.2|text|no|no|Explicit quotient rule with trig functions
4C|4|2.4.1.2,2.4.2.1,2.4.2.2|text|no|no|Choose chain/product/quotient for elementary composite derivatives
4C|5|2.4.1.2,2.4.2.1,2.4.2.2|text|no|no|Choose chain/product/quotient for elementary composite derivatives
4C|6|2.4.2.1,1.8.3.1|text|no|no|Differentiate xcosx, gradient, tangent and normal
4C|7|2.4.1.2,2.4.3.3,1.6.6.1|graph|no|yes|Locate points with prescribed gradient on tangent graph
4C|8|2.4.1.1,2.4.1.2,1.8.3.1|text|no|yes|Tangent/gradient calculations with specified precision
4C|9|2.4.1.1,2.4.1.2,1.8.3.1|text|no|yes|Tangent/gradient calculations with specified precision
4C|10|2.4.1.1,2.4.2.1,1.8.4.1,1.8.4.2|text|no|yes|Stationary point and nature on bounded trig/exponential curves
4C|12|2.4.1.1,2.4.2.1,1.8.4.1,1.8.4.2|text|no|yes|Stationary point and nature on bounded trig/exponential curves
4C|11|2.4.2.2,1.8.3.1|text|no|yes|Quotient of tan expressions; tangent equation and precision
4C|13|2.4.2.2,1.8.4.1|text|no|yes|Stationary abscissa of exponential/secant quotient in a prescribed interval
4D|1|2.4.3.1|text|no|no|Differentiate y-dependent expressions with respect to x
4D|2|2.4.3.1,2.4.3.3|text|no|no|Implicit logarithmic/exponential/trig gradient at a point
4D|3|2.4.3.1,2.4.3.3|text|no|no|Implicit logarithmic/exponential/trig gradient at a point
4D|4|2.4.3.1,1.8.3.1|text|no|no|Implicit polynomial curve and tangent
4D|5|2.4.3.1,1.8.4.1|text|no|no|Implicit stationary points; solve numerator condition with curve
4D|6|2.4.3.1,1.8.3.1,1.4.2.1,1.3.5.1|text|yes|no|Hyperbola normal, second intersection, asymptotes and sketch
4D|7|2.4.3.1,2.4.2.1,1.8.4.1,1.3.5.1|text|yes|no|x^x via supplied logarithmic differentiation scaffold; no new differentiation rule assumed
4D|8|2.4.3.1,2.4.3.3,1.8.4.1|text|no|yes|Implicit differentiation plus tangent/stationary or parameter conditions
4D|9|2.4.3.1,2.4.3.3,1.8.4.1|text|no|yes|Implicit differentiation plus tangent/stationary or parameter conditions
4D|10|2.4.3.1,2.4.3.3,1.8.4.1|text|no|yes|Implicit differentiation plus tangent/stationary or parameter conditions
4D|11|2.4.3.1,1.8.3.1,1.8.4.1|text|no|yes|Implicit tangent equation or unique stationary point with nonzero parameter
4D|12|2.4.3.1,1.8.3.1,1.8.4.1|text|no|yes|Implicit tangent equation or unique stationary point with nonzero parameter
4E|1|2.4.3.2|text|no|no|Mixed elementary parametric derivatives
4E|2|2.4.3.2,2.4.3.3,1.8.3.1,1.4.2.1|text|no|no|Gradient, tangent/normal and axis intersections, with numerical or symbolic parameter
4E|3|2.4.3.2,2.4.3.3,1.8.3.1,1.4.2.1|text|no|no|Gradient, tangent/normal and axis intersections, with numerical or symbolic parameter
4E|4|2.4.3.2,2.4.3.3,1.8.3.1,1.4.2.1|text|no|no|Gradient, tangent/normal and axis intersections, with numerical or symbolic parameter
4E|5|2.4.3.2,1.8.1.2|text|no|no|Rewrite first derivative as 4x before ordinary second differentiation; no general second-parametric-derivative rule assumed
4E|6|2.4.3.2,1.8.3.1,1.4.1.1|text|no|no|Parameter tangent and constant intercept-triangle area
4E|7|2.4.3.2,1.8.3.1,1.4.2.1|graph|no|no|Two parameter tangents, their intersection and locus under t1+t2=2
4E|8|2.4.3.2,2.4.3.3,1.8.3.1|text|no|no|Parametric path tangent direction; not credited as straight-line kinematics coverage
4E|9|2.4.3.2,2.4.3.3,1.8.4.1|text|no|yes|Show derivative and find both horizontal tangencies
4E|10|2.4.3.2,2.3.2.2,2.3.2.3|text|no|yes|Parametric trig derivatives and identity simplification
4E|12|2.4.3.2,2.3.2.2,2.3.2.3|text|no|yes|Parametric trig derivatives and identity simplification
4E|14|2.4.3.2,2.3.2.2,2.3.2.3|text|no|yes|Parametric trig derivatives and identity simplification
4E|11|2.4.3.2,2.4.3.3,2.2.3.1|text|no|yes|Find parameter/coordinates for a prescribed gradient
4E|13|2.4.3.2,2.4.3.3,2.2.3.1|text|no|yes|Find parameter/coordinates for a prescribed gradient
4E|15|2.4.3.2,1.8.3.1,1.4.1.1|text|no|yes|Parametric astroid tangent and constant distance between axis intercepts
5A|1|2.5.1.1|text|no|no|Indefinite reciprocal-linear and exponential forms; simplify exponential quotient first
5A|2|2.5.1.1|text|no|no|Indefinite reciprocal-linear and exponential forms; simplify exponential quotient first
5A|3|2.5.1.1,1.9.3.1|text|no|no|Definite elementary integrals with precision instructions
5A|4|2.5.1.1,1.8.4.1,1.9.4.1|graph|no|no|Stationary points and signed areas on reciprocal-power graph
5A|5|2.5.1.1,1.9.4.1,2.2.2.2|graph|no|no|Exponential area, inverse reflection and derived log integral; no general integration-by-parts technique required
5A|6|2.4.1.1,2.5.1.1,2.5.1.3,2.1.3.1,1.9.3.1|text|no|yes|Reverse derivative plus polynomial division before log integration
5A|7|2.5.1.1,1.9.2.1,1.9.2.2,1.8.4.1,1.8.4.2|text|no|yes|Recover curve through point, then classify stationary point
5A|8|2.4.1.2,1.8.3.1,1.1.3.2,2.5.1.1,1.9.3.1|text|no|yes|Tangent, supplied algebraic decomposition and exact definite integral
5A|9|2.5.1.1,1.9.3.1,2.2.3.1|text|no|yes|Unknown upper integration bound from logarithmic integral
5B|1|2.5.1.2,1.9.3.1|text|no|no|Elementary trig antiderivatives and exact definite integrals
5B|2|2.5.1.2,1.9.3.1|text|no|no|Elementary trig antiderivatives and exact definite integrals
5B|3|2.5.2.1,2.5.2.2,1.9.3.1|text|no|no|Choose double-angle identity before indefinite/definite integration
5B|4|2.5.2.1,2.5.2.2,1.9.3.1|text|no|no|Choose double-angle identity before indefinite/definite integration
5B|5|2.3.2.4,2.5.1.2,1.9.3.1|text|no|yes|R-form transforms inverse squared sinusoid to sec-squared linear argument
5B|6|2.3.2.3,2.3.2.5,2.5.1.2,1.6.3.1|text|no|yes|Prove tan+cot identity, exact value and reciprocal-expression integral
5B|7|2.5.2.1,2.5.2.2,1.9.3.1|text|no|yes|Identity scaffolds exact squared-trig integrals
5B|8|2.5.2.1,2.5.2.2,1.9.3.1|text|no|yes|Identity scaffolds exact squared-trig integrals
5B|9|2.5.2.1,2.5.2.2,1.9.3.1|text|no|yes|Identity scaffolds exact squared-trig integrals
5B|10|2.5.1.1,2.5.2.1,2.5.2.2,1.9.3.1|text|no|yes|Expand elementary exponential expression; transform tan-squared integral
5B|11|2.3.2.2,2.3.2.3,2.5.2.1,1.9.3.1|text|no|yes|Derive repeated-angle identities and use them to integrate higher trig powers; no substitution/integration-by-parts rule assumed
5B|12|2.3.2.2,2.3.2.3,2.5.2.1,1.9.3.1|text|no|yes|Derive repeated-angle identities and use them to integrate higher trig powers; no substitution/integration-by-parts rule assumed
5B|13|2.5.2.1,2.5.2.2,2.5.1.1,1.9.3.1|text|no|yes|Squared half-angle integration and reciprocal-linear definite integral
5C|1|2.5.3.1,2.5.3.2,1.9.4.3|table|no|no|Speed-time trapezia estimate distance and explain information limits
5C|2|2.5.3.1,2.5.3.2|text|no|no|Estimate π from supplied integral fact; no arctan antiderivative required
5C|3|2.5.3.1,2.5.3.2,2.5.4.1|text|yes|no|Sketch integrand, refine interval sizes and discuss justified digits; no formal quadrature error formula is prescribed by 8227
5C|4|2.5.3.1,2.5.3.2,2.5.4.1|text|yes|no|Sketch integrand, refine interval sizes and discuss justified digits; no formal quadrature error formula is prescribed by 8227
5C|5|2.5.3.1,2.5.3.2,2.5.4.1|text|yes|no|Sketch integrand, refine interval sizes and discuss justified digits; no formal quadrature error formula is prescribed by 8227
5C|6|2.5.3.1,2.5.3.2,2.5.4.1,2.5.1.2|text|yes|no|Different strip widths, diagrams and exact integral comparison
5C|7|2.5.3.1,2.5.3.2|text|no|yes|Trapezia for a modulus integrand; not a claim all sampled nodes capture the corner
5C|8|2.5.3.1,2.5.3.2,2.5.4.2,1.8.4.1|graph|no|yes|Stationary point then trapezia estimate and geometric over/under explanation
5C|9|2.5.3.1,2.5.3.2,2.5.4.2,1.8.4.1|graph|no|yes|Stationary point then trapezia estimate and geometric over/under explanation
5C|10|1.8.4.1,1.8.3.1,2.5.3.1,2.5.3.2|graph|no|yes|Exponential-product curve, tangent and numerical integral; does not require integration by parts
5C|11|2.5.1.1,1.9.3.1,2.5.3.1,2.5.3.2|text|no|yes|Exact logarithmic integral plus trapezia approximation of a different log integrand
6A|1|1.8.3.2,2.6.1.1,2.6.1.2|text|yes|no|Monotonic cubic, sketch/root count and numerical localisation
6A|2|2.6.1.1,2.6.1.2|text|no|no|Bracket/refine roots; decimal search and bisection are textbook extensions of sign-change localisation, not newly required exam methods
6A|4|2.6.1.1,2.6.1.2|text|no|no|Bracket/refine roots; decimal search and bisection are textbook extensions of sign-change localisation, not newly required exam methods
6A|5|2.6.1.1,2.6.1.2|text|no|no|Bracket/refine roots; decimal search and bisection are textbook extensions of sign-change localisation, not newly required exam methods
6A|3|2.6.1.1,2.6.1.2|text|yes|no|Two-graph root count then numerical localisation
6A|6|2.6.1.1,2.6.1.2|text|yes|no|Three cubic roots and interval/error notation; not a formal convergence theorem
6A|7|2.6.1.1,2.6.1.2|graph|no|no|Given exponential-minus-cubic sketch guides root bracketing
6A|8|2.6.1.1,2.6.1.2|text|yes|no|Boundary examples: discontinuity and even root defeat naive sign-change search; not full fixed-point failure coverage
6B|1|2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|no|no|Bracket, verify rearrangement, execute iteration and apply requested precision
6B|3|2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|no|no|Bracket, verify rearrangement, execute iteration and apply requested precision
6B|4|2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|no|no|Bracket, verify rearrangement, execute iteration and apply requested precision
6B|2|2.6.3.2|text|no|no|Four rearrangements; fourth-root forms need a nonnegative-branch qualification, since original equation also has a negative root
6B|5|2.6.1.1,2.6.3.2,2.6.4.1,2.6.4.2|text|yes|no|Graphical uniqueness, choose rearrangement and iterate
6B|6|2.6.3.2,2.6.4.1,2.6.4.2|text|no|no|Find second root after supplied zero root; domain x>-1
6B|7|2.6.1.1,2.6.4.1,2.6.4.2|text|yes|no|Sketch x and cosx then compute intersection by iteration
6B|8|2.5.1.1,2.6.3.2,2.6.4.1,2.6.4.2|text|no|yes|Definite integral gives unknown-bound equation then iteration
6B|9|2.6.2.1,2.6.3.1,2.6.4.1,2.6.4.2|text|no|yes|Iterate supplied rational recurrence then derive exact limiting value
6B|10|2.6.1.1,2.6.1.2,2.6.3.1,2.6.4.1,2.6.4.2|text|yes|yes|Graphical uniqueness, bracket, conditional fixed-point implication and numerical root
6B|13|2.6.1.1,2.6.1.2,2.6.3.1,2.6.4.1,2.6.4.2|text|yes|yes|Graphical uniqueness, bracket, conditional fixed-point implication and numerical root
6B|11|2.4.2.1,1.8.4.1,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|yes|Stationary point equation on trig graph, bracket and inverse-tan iteration in radians
6B|12|2.4.2.1,1.8.4.1,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|yes|Exact minimum of exponential product then line-intersection iteration
6B|14|2.6.1.2,2.6.3.1,2.6.4.1,2.6.4.2|text|no|yes|Bracket cubic and use supplied iteration; no Newton-Raphson derivation/formal convergence condition required
6B|15|2.6.1.2,2.6.3.1,2.6.4.1,2.6.4.2|text|no|yes|Bracket cubic and use supplied iteration; no Newton-Raphson derivation/formal convergence condition required
6B|16|2.4.3.2,2.4.3.3,2.6.3.2,2.6.4.1,2.6.4.2|text|no|yes|Prescribed parametric gradient yields fixed-point equation
10A|1|1.7.1.2,1.7.3.2|diagram|no|no|Read signed displacement components from coordinate-grid arrows
10A|2|1.7.1.2,1.7.4.1|text|yes|no|Draw vector diagrams and calculate magnitude/direction
10A|3|1.7.4.1|text|no|no|Magnitudes of 3D vectors
10A|4|1.7.3.2|text|no|no|Displacements between supplied coordinate points
10A|5|1.7.3.2,1.7.3.3,1.7.2.3|text|no|no|Position/displacement distinction and quadrilateral geometry
10B|1|1.7.2.1,1.7.2.2|text|no|no|Vector addition/subtraction/scaling in 2D and 3D
10B|2|1.7.2.1,1.7.2.2|text|no|no|Vector addition/subtraction/scaling in 2D and 3D
10B|3|1.7.2.1,1.7.2.2,1.7.2.3|diagram|no|no|Parallelogram/kite/triangle midpoint identities and geometric explanations
10B|4|1.7.2.1,1.7.2.2,1.7.2.3|diagram|no|no|Parallelogram/kite/triangle midpoint identities and geometric explanations
10B|5|1.7.2.1,1.7.2.2,1.7.2.3|diagram|no|no|Parallelogram/kite/triangle midpoint identities and geometric explanations
10B|6|1.7.3.1,1.7.4.1|text|no|no|Unit vectors in two and three dimensions
10B|7|1.7.3.1,1.7.4.1|text|no|no|Unit vectors in two and three dimensions
10B|8|1.7.3.2,1.7.4.1|text|no|no|Triangle perimeter or unknown coordinate from vector magnitude
10B|9|1.7.3.2,1.7.4.1|text|no|no|Triangle perimeter or unknown coordinate from vector magnitude
10B|10|1.7.2.1,1.7.2.2,1.7.2.3,1.7.3.3|diagram|no|no|Cuboid routes, ratio division and bisection proof
10B|11|1.7.2.3,1.7.3.2|text|no|no|Prove parallelogram from supplied 3D coordinates
10B|12|1.7.2.1,1.7.2.2,1.7.3.1,1.7.3.3|text|no|yes|Vector relation to find unit vector then solve component constants; no vector-line-equation method needed
10C|1|1.7.4.2,1.7.5.1,1.7.5.2|text|no|no|Angles, perpendicularity and square-coordinate geometry via displacement vectors
10C|2|1.7.4.2,1.7.5.1,1.7.5.2|text|no|no|Angles, perpendicularity and square-coordinate geometry via displacement vectors
10C|3|1.7.4.2,1.7.5.1,1.7.5.2|text|no|no|Angles, perpendicularity and square-coordinate geometry via displacement vectors
10C|4|1.7.1.1,1.7.3.2,1.7.4.1,1.7.5.1|diagram|no|no|Read room coordinates, 3D displacement/magnitude and elevation
10C|5|1.7.1.1,1.7.2.3,1.7.3.2,1.7.5.1|diagram|no|yes|Cube route/midpoint/ratio gives vectors and angle
10C|6|1.7.5.2,1.7.5.1,1.7.4.1|text|no|yes|Perpendicularity parameter, angle and length parameter alternatives
10C|7|1.7.4.2,1.7.5.1,1.7.3.1,1.7.4.1|text|no|yes|Dot-product sign/angle, unit vectors and unknown coordinate from length
10C|8|1.7.4.2,1.7.5.1,1.7.3.1,1.7.4.1|text|no|yes|Dot-product sign/angle, unit vectors and unknown coordinate from length
10C|9|1.7.4.2,1.7.5.1,1.7.3.1,1.7.4.1|text|no|yes|Dot-product sign/angle, unit vectors and unknown coordinate from length
10C|10|1.7.1.1,1.7.2.3,1.7.3.2,1.7.4.1,1.7.5.1|diagram|no|yes|Prism/roof/cube geometry supplies coordinates then scalar-product angles and lengths; before vector-line-equation section
10C|11|1.7.1.1,1.7.2.3,1.7.3.2,1.7.4.1,1.7.5.1|diagram|no|yes|Prism/roof/cube geometry supplies coordinates then scalar-product angles and lengths; before vector-line-equation section
10C|12|1.7.1.1,1.7.2.3,1.7.3.2,1.7.4.1,1.7.5.1|diagram|no|yes|Prism/roof/cube geometry supplies coordinates then scalar-product angles and lengths; before vector-line-equation section
'''

YM = r'''
1|Example|38|49|1.1.2.1,1.1.2.2,1.1.2.3,1.4.2.2|text|no|Discriminant for curve above axis and tangent line; worked solution on page
1|Try Now|38|49|1.1.2.3,1.4.2.2,1.4.2.1|text|no|Show line always meets quadratic; exceptional tangent parameter and point
1|Revision Exercise 1|1|50|1.1.6.1,1.1.6.2,1.1.1.1,1.1.1.2|text|no|Inequality plus completing square and vertex
1|Revision Exercise 1|2|50|1.1.2.3,1.4.2.1|text|no|Reciprocal curve/line becomes quadratic; nonintersection condition then intersections
1|Revision Exercise 1|3|50|1.1.4.1,1.1.4.2,1.1.4.3|text|no|Quadratic in reciprocal x squared; filter real roots
1|Revision Exercise 1|4|50|1.1.5.1|text|no|Reconstruct parabola from origin and vertex
1|Revision Exercise 1|5|50|1.1.5.2|graph|no|Cubic from simple root -3, tangent root 2/3 and intercept 6
1|Revision Exercise 1|6|50|1.1.3.2|text|no|Determine identity coefficients by comparison
1|Revision Exercise 1|7|50|1.1.4.1,1.1.4.2,1.1.4.3|text|no|Square-root substitution with original-domain/root checks
2|Example|50|103|1.2.3.1,1.2.3.2,1.2.5.2|text|no|AP finite sum and positive-parameter GP/infinite sum
2|Try Now|50|104|1.2.2.1,1.2.2.2,1.2.3.1,1.2.3.2|text|no|Coupled AP/GP conditions with positive x,y; fourth terms
2|Example|51|104|1.2.1.2,1.2.1.3|text|no|Combine binomial coefficients to determine a
2|Try Now 51|1|104|1.2.1.1,1.2.1.2,1.2.1.3|text|no|Coefficient constraints in sum/product of positive-integer binomials
2|Try Now 51|2|104|1.2.1.1,1.2.1.2,1.2.1.3|text|no|Coefficient constraints in sum/product of positive-integer binomials
2|Try Now 51|3|104|1.2.1.1,1.2.1.2,1.2.1.3|text|no|Coefficient constraints in sum/product of positive-integer binomials
2|Revision Exercise 2|1|105|1.2.3.2,1.2.5.2,1.2.3.1|text|no|GP ratio/infinite sum then linked AP finite sum
2|Revision Exercise 2|2|105|1.2.1.2,1.2.1.3|text|no|Specified coefficient or term independent of x; LIMIT01 satisfied
2|Revision Exercise 2|3|105|1.2.1.2,1.2.1.3|text|no|Specified coefficient or term independent of x; LIMIT01 satisfied
2|Revision Exercise 2|6|105|1.2.1.2,1.2.1.3|text|no|Specified coefficient or term independent of x; LIMIT01 satisfied
2|Revision Exercise 2|4|105|1.2.3.1,1.2.3.2,1.2.3.3|text|no|Water-loss model with arithmetic or geometric daily losses and integer threshold
2|Revision Exercise 2|5|105|1.2.3.1|text|no|AP finite sum equals n; filter positive integer
3|Example|23|146|1.3.4.1,1.1.2.3|text|no|Composition equation with repeated root; printed section heading 2.3 is a numbering error, preserve locator
3|Try Now|23|146|1.1.1.1,1.3.2.2,1.1.6.2,1.3.4.1,1.1.2.3|text|no|Complete square, range, inequality and composite repeated root
3|Example|24|147|1.4.1.1,1.4.2.1|diagram|no|Perpendicular/bisected diagonals give coordinates and length ratio
3|Try Now|24|147|1.4.1.1,1.4.2.1|diagram|no|Perpendicular projection and internal/external ratio AX:XB
3|Revision Exercise 3|1|148|1.4.1.1|text|no|Unknown coordinate parameter from perpendicular-bisector equation
3|Revision Exercise 3|2|148|1.3.3.2,1.3.2.1,1.3.5.1,1.3.5.2,1.3.4.1,1.1.2.3|text|yes|Inverse functions/graphs and composite no-solutions condition; k=0 degeneracy must be checked before discriminant use
3|Revision Exercise 3|3|148|1.4.1.1,1.4.2.1|text|no|Perpendicular line, axis intercept and distance with precision
3|Revision Exercise 3|4|148|1.4.1.1,1.4.2.1|diagram|no|Kite symmetry line determines missing vertex
4|Example|57|225|1.5.2.2,1.6.3.1|diagram|no|Overlapping sectors in rectangle, radian angle and compound shaded area
4|Try Now|57|225|1.5.2.1,1.5.2.2|diagram|no|Semicircle and displaced-centre arc; derive radius/angle, arc length and ratio of regions
4|Example|58|226|1.6.2.2,1.3.2.2,1.6.3.1|text|no|Recover cosine coefficients, range and exact special-angle value
4|Try Now 58|1|226|1.6.2.2,1.6.3.1|text|no|Trig coefficients from function values; simultaneous equations
4|Try Now 58|2|226|1.6.2.2,1.6.3.1|text|no|Trig coefficients from function values; simultaneous equations
4|Revision Exercise 4|1|227|1.6.3.1|diagram|no|Trapezium/triangles use exact 30/60 ratios and show an inverse-tangent angle expression; not principal-value classification coverage
4|Revision Exercise 4|2|227|1.2.3.2,1.2.5.2,1.2.3.1,1.6.3.1|text|no|GP infinite sum; AP trig terms give exact acute angle ratios and finite sum
4|Revision Exercise 4|3|227|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Rewrite bounded trig equation as tan2x=k
4|Revision Exercise 4|4|228|1.5.2.2|diagram|no|Three touching circles in 3-4-5 triangle; area between arcs from triangle minus three sectors, not evidence for full circular-segment demand
4|Revision Exercise 4|5|228|1.6.2.2,1.6.2.3,1.6.6.1,1.6.6.2|text|yes|Recover a,b; bounded roots; sketch transformed cosine
5|Example|17|261|1.7.4.2,1.7.5.1,1.7.3.2,1.7.4.1|text|no|Dot product proof then unknown coordinate from distance; two parameter values
5|Try Now|17|261|1.7.5.2,1.7.4.1,1.7.3.2|text|no|Parameter from perpendicularity and from displacement magnitude
5|Example|18|262|1.7.3.2,1.7.5.1,1.7.4.2|text|no|Angle at A requires AB and AC; exact triangle area from sin obtained algebraically from cos
5|Try Now 18|1|262|1.7.5.1,1.7.4.2|text|no|Angle given as inverse-cos exact expression; solve both parameter signs
5|Try Now 18|2|262|1.7.3.2,1.7.5.1,1.7.4.2|text|no|Angle OAB uses AO rather than OA; triangle area
5|Revision Exercise 5|1|263|1.7.5.2,1.7.3.1,1.7.2.2|text|no|Perpendicularity parameter, then vector with prescribed magnitude/direction
5|Revision Exercise 5|2|263|1.7.2.1,1.7.2.2,1.7.3.3|text|no|Solve vector component constants in a linear combination
5|Revision Exercise 5|3|263|1.7.2.3,1.7.3.3|text|no|Missing parallelogram vertex by vector relation
5|Revision Exercise 5|4|264|1.7.1.1,1.7.2.3,1.7.3.2,1.7.5.1,1.7.4.1|diagram|no|Cube midpoint triangle, angle and perimeter; same underlying question as Goldie 10C Q12, not independent breadth
5|Revision Exercise 5|5|264|1.7.1.1,1.7.3.2,1.7.5.1|diagram|no|Truncated rectangular solid with 3D coordinates; exact inverse-cos angle form
6|Example|36|314|1.8.2.2,1.8.3.1,1.4.1.1|graph|no|Secant, parallel tangent and perpendicular separation; worked solution continues PDF315
6|Try Now 36|1|315|1.8.3.1,1.4.2.1|text|no|Parallel tangent or line/curve intersections, midpoint and distance
6|Try Now 36|2|315|1.8.3.1,1.4.2.1|text|no|Parallel tangent or line/curve intersections, midpoint and distance
6|Example|37|316|1.8.3.1|text|no|Use supplied derivative at symbolic positive-parameter point; simplify tangent equation
6|Try Now|37|316|1.8.3.1,1.9.2.2|text|no|Given normal to parameter-shifted parabola determines constant via contact point
6|Example|38|316|1.8.2.2,1.8.3.2|text|no|Largest domain endpoint for a strictly decreasing composite-power function
6|Try Now 38|1|317|1.8.3.2|text|no|Largest/smallest domain boundary giving increasing cubic function
6|Try Now 38|2|317|1.8.3.2|text|no|Largest/smallest domain boundary giving increasing cubic function
6|Example|39|317|1.8.2.1,1.8.4.1|text|no|Stationary abscissae then vertical-shift parameters placing a stationary point on axis
6|Try Now|39|317|1.8.2.2,1.8.4.1,1.8.4.2|text|no|Parameter-dependent stationary locations and classifications; k is nonzero
6|Revision Exercise 6|1|318|1.8.2.2,1.8.3.3|text|no|Gradient and reciprocal connected rate dx/dt from dy/dt
6|Revision Exercise 6|2|318|1.8.2.2,1.8.3.1|graph|no|Acute angle between tangents at two labelled points
6|Revision Exercise 6|3|318|1.8.2.1,1.8.4.1,1.8.4.2|text|no|Quartic stationary coordinates and justified nature
6|Revision Exercise 6|4|319|1.8.2.1,1.8.4.1,1.8.4.2|graph|no|Read double-root minimum, calculate maximum location, then minimise the gradient function; not inflexion classification
6|Revision Exercise 6|5|319|1.5.2.1,1.5.2.2,1.8.4.1,1.8.4.2|diagram|no|Perimeter-constrained rectangle plus quarter-circle: derive area model, optimise, classify
7|Example|40|369|1.8.2.2,1.8.3.1,1.9.4.2|graph|no|Normal then volume: curve-solid plus cone; exact solution on page
7|Try Now|40|370|1.4.1.1,1.9.4.1,1.9.4.2|graph|no|Piecewise boundary area/volume from reciprocal-square curve and two lines
7|Example|41|370|1.8.2.2,1.8.3.1,1.9.4.1,1.9.4.2|graph|no|Tangent encloses curved cap; separate region of revolution; worked solution continues PDF371
7|Try Now 41|1|371|1.8.2.2,1.8.3.1,1.9.4.1|graph|no|Tangent cap area for square-root curve
7|Try Now 41|2|371|1.8.3.1,1.4.1.1,1.9.4.2|graph|no|Reciprocal curve tangent/triangle area and volume from squared reciprocal; no Theme-1 logarithmic integration assumed
7|Revision Exercise 7|1|372|1.9.1.2,1.9.3.1|text|no|Expand square before integration; integrate linear square-root denominator and evaluate bounds
7|Revision Exercise 7|2|372|1.9.1.2,1.9.2.1,1.9.2.2|text|no|Recover curve from reciprocal-square derivative and point
7|Revision Exercise 7|3|372|1.9.4.1,1.9.4.2|graph|no|Area below axis plus volumes about both axes; sign and change of variable representation matter
7|Revision Exercise 7|4|372|1.8.4.1,1.9.4.3|text|no|Maximum velocity and straight-line displacement/distance on stated positive-velocity interval
8|Example|26|403|2.1.2.1,2.1.2.2,2.1.1.3|text|yes|Parameterised modulus sketches/inequality; literal integer-coefficient QUAL01 requires controlled specialisations; table-based sketch advice conflicts with examiner guidance
8|Try Now 26|1|403|2.1.1.2|text|no|Parameter modulus equation or compare two absolute differences at admissible roots
8|Try Now 26|2|403|2.1.1.2|text|no|Parameter modulus equation or compare two absolute differences at admissible roots
8|Example|27|404|2.1.4.1,2.1.4.2,2.1.4.3,2.1.4.4|text|no|Prove factor for all a, use remainder to recover a, then factor p(x^2) via known cubic factorisation; no degree-six division performed
8|Try Now|27|404|2.1.3.1,2.1.3.3,2.1.4.4|text|no|Quotient/remainder, adjusted polynomial factorisation, all roots
8|Revision Exercise 8|1|405|2.1.1.2|text|no|Decimal coefficients in modulus equation; graph-specific QUAL01 does not prohibit this equation
8|Revision Exercise 8|2|405|2.1.1.3|text|no|Compare two modulus expressions
8|Revision Exercise 8|3|405|2.1.2.1,2.6.1.1|text|yes|Choose graphs to justify exactly two real roots; quartic/modulus intersection
8|Revision Exercise 8|4|405|2.1.1.2,1.6.6.1,1.6.6.2,2.3.1.1|text|no|Modulus in u then hence cotx equation on finite radian interval
8|Revision Exercise 8|5|405|1.1.3.2,2.1.3.3,2.1.4.2,2.1.4.4|text|no|Polynomial identity, factor theorem and complete factorisation
8|Revision Exercise 8|6|405|2.1.4.2,2.1.4.3,2.1.4.4,1.1.2.2|text|no|Two polynomial coefficient conditions then one-real-root proof for their difference
9|Example|34|443|2.1.1.2,2.2.3.1|text|no|Modulus equation scaffolds exponential equation via positive substitution
9|Try Now 34|1|443|2.1.1.2,2.2.3.1|text|no|Hence exponential modulus equation
9|Try Now 34|2|443|2.1.1.3,2.2.3.2|text|no|Modulus inequality in logy then largest integer y
9|Try Now 34|3|443|1.1.4.1,1.1.4.2,1.1.4.3,2.2.3.1,2.1.1.1|text|no|Quadratic in 3^x then recover both signs for |x|
9|Example|35|444|2.2.4.1,2.2.4.2,1.4.2.1|text|no|Linearise 3^y=4^{x+2}, exact gradient and intersection; same item as Goldie 2C Q9, not independent breadth
9|Try Now 35|1|444|2.2.4.1,2.2.4.2,2.2.1.2|text|no|Linearise exponential relation or solve coupled exponential/log constraints
9|Try Now 35|2|444|2.2.4.1,2.2.4.2,2.2.1.2|text|no|Linearise exponential relation or solve coupled exponential/log constraints
9|Revision Exercise 9|1|445|2.2.1.2,2.2.3.1|text|no|Logarithmic solution, proportional-exponent relation or disguised quadratic
9|Revision Exercise 9|3|445|2.2.1.2,2.2.3.1|text|no|Logarithmic solution, proportional-exponent relation or disguised quadratic
9|Revision Exercise 9|4|445|2.2.1.2,2.2.3.1|text|no|Logarithmic solution, proportional-exponent relation or disguised quadratic
9|Revision Exercise 9|2|445|2.2.3.2|text|no|Base below one reverses inequality
9|Revision Exercise 9|5|445|2.1.1.2,2.2.3.1|text|no|Modulus roots reused in exponential equation with positive-variable filtering
9|Revision Exercise 9|6|445|2.2.1.2|text|no|Log laws create quadratic; check original log domains
9|Revision Exercise 9|7|445|2.2.4.1,2.2.4.2|graph|no|lny versus x, recover denominator exponential base and scale
10|Example|26|479|2.3.2.1,2.3.2.2,2.3.2.5,1.6.3.1|text|no|Reciprocal Pythagorean identity gives positive tan then exact compound angle
10|Try Now|26|479|2.3.2.1,2.3.2.2,2.3.2.5|text|no|Exact tan/cot from coupled acute-angle conditions; same source item as Goldie 3B Q7
10|Revision Exercise 10|1|480|2.3.1.2,2.6.1.1|text|yes|Sketch cotx and x to establish a unique bounded root
10|Revision Exercise 10|2|480|2.3.1.1,2.3.2.3,2.3.2.5|text|no|Prove tan+cot identity
10|Revision Exercise 10|3|480|2.3.2.2,2.3.2.5,1.6.6.1,1.6.6.2,1.6.3.1|text|no|Compound-angle proof then reciprocal equation on full degree interval
10|Revision Exercise 10|4|480|2.3.2.1,2.3.2.3,2.3.2.5,1.6.6.1,1.6.3.1|text|no|Double-angle proof, hence bounded equation and exact 15-degree reciprocal values
10|Revision Exercise 10|5|480|2.3.2.4,2.3.1.1,1.6.6.1,1.6.6.2|text|no|R-form then cot/cosec equation; radian interval and phase precision explicit
11|Example|41|525|2.4.2.1,1.8.3.1|graph|no|Product-rule tangent through origin determines contact parameter; double algebraic root
11|Try Now|41|525|2.4.3.2,2.1.3.1,1.8.3.1|text|no|Parametric derivative simplified by division, then normal contact point
11|Example|42|526|2.4.3.2,1.8.4.1,1.8.4.2|text|no|Positive parameter selects stationary point; classify via sign change or source second-parametric derivative method, which is not a required standalone 8227 technique
11|Try Now 42|1|526|2.4.3.2,1.8.4.1,1.8.4.2|text|no|Parametric stationary point; sign test is available without assuming a new second-parametric rule
11|Try Now 42|2|526|2.4.2.1,1.8.1.2|text|no|Locate zero of ordinary second derivative of exponential product; no inflexion classification asked
11|Revision Exercise 11|1|527|2.4.1.1,2.4.2.2,2.3.1.1|text|no|Derive sec derivative from reciprocal cosine rather than recall unprescribed formula
11|Revision Exercise 11|2|527|2.4.2.2,2.4.3.3|text|no|Two curve points with prescribed negative gradient
11|Revision Exercise 11|3|527|2.4.2.2,2.4.1.2,1.8.4.1|text|no|Exact stationary point of exponential quotient
11|Revision Exercise 11|4|527|2.4.3.1,2.4.3.3,1.8.4.1|text|no|Implicit derivative then all horizontal tangent points
11|Revision Exercise 11|5|527|2.4.3.2,1.8.4.1,1.8.4.2|text|no|Same parametric curve as Example42, derive derivative and classify stationary point; duplicate within book
12|Example|23|554|2.3.2.3,2.3.2.5,1.6.3.1,2.5.1.2|text|no|Tan+cot identity, exact angle value and reciprocal integral; endpoint undefined terms need removable-limit interpretation, not unqualified pointwise substitution
12|Try Now 23|1|554|2.3.2.3,2.5.2.1,2.5.1.2,1.9.3.1|text|no|Rational trig identity then exact integral with doubled argument
12|Try Now 23|2|554|2.5.2.1,2.5.2.2,1.9.3.1|text|no|Squared cosine integral then deduce squared sine; same item as Goldie 5B Q7
12|Example|24|555|2.5.2.1,2.5.1.2,2.5.3.1,2.5.3.2,2.5.4.1,2.5.4.2|text|yes|Identity before integration then cosecant trapezia/sketch explanation; source calls convex-up curve concave, retained convention conflict
12|Try Now|24|555|2.5.3.1,2.5.3.2,2.5.4.1,2.5.4.2|text|yes|Secant trapezia and sketch justify overestimate
12|Revision Exercise 12|1|556|2.5.1.1,1.9.3.1,2.2.1.2|text|no|Reciprocal-linear integral; exact result as ln(integer)
12|Revision Exercise 12|2|556|2.3.2.3,2.5.2.1,2.5.1.2,1.6.6.1,1.6.6.2|text|no|Double-angle identity, bounded tan equation and half-angle transformed integral; no general substitution technique required
12|Revision Exercise 12|3|556|2.5.2.1,2.5.1.1,2.5.1.2,1.9.3.1|text|no|Indefinite tan-squared/trig integral and exact exponential definite integral
12|Revision Exercise 12|4|556|2.5.1.1,1.9.4.1|text|no|Exact area of shifted exponential on stated bounds
12|Revision Exercise 12|5|556|2.5.3.1,2.5.3.2,2.5.4.2|graph|no|Exponential-square-root curve; two-strip estimate and diagram-based overestimate explanation
13|Example|10|581|2.1.3.1,2.1.3.3,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|Known quartic root gives cubic quotient and fixed-point equation; interval/precision selection
13|Try Now|10|581|2.1.4.2,2.1.3.1,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|Quartic factor theorem then positive-root iteration with six-significant-figure iterates
13|Example|11|582|2.4.3.2,2.4.3.3,2.6.3.2,2.6.4.1,2.6.4.2|text|no|Parametric gradient gives sixth-root iteration; same source item as Goldie 6B Q16
13|Try Now|11|582|2.5.3.1,2.5.3.2,2.6.4.1,2.6.4.2|graph|no|Trapezia and graph-intersection iteration on same square-root trig curve
13|Revision Exercise 13|1|583|2.6.2.1,2.6.3.1,2.6.4.1,2.6.4.2|text|no|Supplied recurrence and exact fifth-root limiting equation
13|Revision Exercise 13|2|583|2.6.1.1,2.6.1.2,2.6.3.1,2.6.4.1,2.6.4.2|text|yes|Sketch uniqueness, bracket, conditional convergence implication and iterate; same item as Goldie 6B Q13
13|Revision Exercise 13|3|583|2.4.2.1,1.8.4.1,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|Stationary x^2cosx equation, bracket and inverse-tan iteration; continues PDF584, same item as Goldie 6B Q11
13|Revision Exercise 13|4|584|2.5.1.1,1.9.4.1,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|Exponential area constraint gives fixed-point formula; iterate unknown upper bound
1|Exercise 1|1|47|1.1.4.1,1.1.4.2,1.1.4.3|text|no|Equations with exponential/radical/reciprocal expressions, transformed quadratics and checks
1|Exercise 1|2|47|1.1.4.1,1.1.4.2,1.1.4.3|text|no|Equations with exponential/radical/reciprocal expressions, transformed quadratics and checks
1|Exercise 1|3|47|1.1.2.1,1.1.2.2,1.1.2.3|text|no|Known root or equal-root parameter; reject zero leading coefficient before discriminant argument
1|Exercise 1|4|47|1.1.2.1,1.1.2.2,1.1.2.3|text|no|Known root or equal-root parameter; reject zero leading coefficient before discriminant argument
1|Exercise 1|5|47|1.1.1.1,1.1.1.2|text|no|Complete square, vertex and extremum
1|Exercise 1|9|47|1.1.1.1,1.1.1.2|text|no|Complete square, vertex and extremum
1|Exercise 1|13|47|1.1.1.1,1.1.1.2|text|no|Complete square, vertex and extremum
1|Exercise 1|6|47|1.1.6.1,1.1.6.2|text|no|Quadratic inequality intervals
1|Exercise 1|7|47|1.1.6.1,1.1.6.2|text|no|Quadratic inequality intervals
1|Exercise 1|8|47|1.1.1.1,1.1.1.2,1.1.1.3|text|yes|Quadratic sketch with vertex and intercepts
1|Exercise 1|10|47|1.1.3.2|text|no|Polynomial identity with unknown coefficients/remainder
1|Exercise 1|11|47|1.1.4.1,1.1.4.2,1.1.4.3|text|no|Hence shifted-variable quadratic or quadratic in y cubed
1|Exercise 1|12|47|1.1.4.1,1.1.4.2,1.1.4.3|text|no|Hence shifted-variable quadratic or quadratic in y cubed
1|Exercise 1|14|48|1.1.5.1|text|no|Quadratic reconstructed from three intercepts
1|Exercise 1|15|48|1.1.2.1,1.1.2.2,1.1.2.3|text|no|Parameter interval for real/non-real roots
1|Exercise 1|16|48|1.4.2.1,1.1.2.3|text|no|Line/curve intersection coordinates or parameter interval; Q17 circle intersects line
1|Exercise 1|17|48|1.4.2.1,1.1.2.3|text|no|Line/curve intersection coordinates or parameter interval; Q17 circle intersects line
1|Exercise 1|18|48|1.1.3.2|text|no|Coefficients in supplied rational identity; no general partial-fraction decomposition technique required
1|Exercise 1|19|48|1.1.5.2|text|no|Reconstruct cubic from roots/contact and further point data
1|Exercise 1|22|48|1.1.5.2|text|no|Reconstruct cubic from roots/contact and further point data
1|Exercise 1|20|48|1.4.2.2,1.1.2.3|text|no|Tangent to x^2+xy=12; degenerate linear elimination case must not be called a tangent merely because it has one root
1|Exercise 1|21|48|1.1.5.1,1.4.1.1|graph|no|Recover graph point then line through shown intercepts
2|Exercise 2.1|1|87|1.2.3.2,1.2.5.2|text|no|GP parameter from consecutive terms, finite/infinite-sum difference
2|Exercise 2.1|2|87|1.2.4.1,1.2.4.2|text|no|Evaluate bounded Sigma expression as geometric series
2|Exercise 2.1|3|87|1.2.3.2,1.2.5.2|text|no|Convergent GP sum and reverse parameter recovery
2|Exercise 2.1|4|87|1.2.3.2,1.2.5.2|text|no|Convergent GP sum and reverse parameter recovery
2|Exercise 2.1|5|87|1.2.3.1,1.2.3.3|text|no|AP symbolic relations, paving model and constrained octagon side lengths
2|Exercise 2.1|6|87|1.2.3.1,1.2.3.3|text|no|AP symbolic relations, paving model and constrained octagon side lengths
2|Exercise 2.1|7|87|1.2.3.1,1.2.3.3|text|no|AP symbolic relations, paving model and constrained octagon side lengths
2|Exercise 2.1|8|88|1.2.3.2,1.2.5.2|text|no|GP from separated terms then termwise-squared progression and its infinite sum
2|Exercise 2.1|9|88|1.2.3.1,1.2.3.3|text|no|Auction bids as AP with first-exceeding integer threshold
2|Exercise 2.1|10|88|1.2.3.2,1.2.3.3,1.2.5.2|text|no|Diminishing mine output: term, finite sum and long-term sum
2|Exercise 2.1|11|88|1.2.3.1,1.2.3.3|diagram|no|Staircase height and area with units conversion
2|Exercise 2.2|1|102|1.2.1.1|text|no|Pascal triangle expansion plus factorial/binomial-coefficient notation; explicitly required under LIMIT01
2|Exercise 2.2|2|102|1.2.1.1|text|no|Pascal triangle expansion plus factorial/binomial-coefficient notation; explicitly required under LIMIT01
2|Exercise 2.2|3|102|1.2.1.1,1.2.1.2|text|no|Ascending/descending powers, chosen term/coefficient and term independent of x
2|Exercise 2.2|4|102|1.2.1.1,1.2.1.2|text|no|Ascending/descending powers, chosen term/coefficient and term independent of x
2|Exercise 2.2|5|102|1.2.1.1,1.2.1.2|text|no|Ascending/descending powers, chosen term/coefficient and term independent of x
2|Exercise 2.2|6|102|1.2.1.1,1.2.1.2|text|no|Ascending/descending powers, chosen term/coefficient and term independent of x
2|Exercise 2.2|7|102|1.2.1.1,1.2.1.2|text|no|Ascending/descending powers, chosen term/coefficient and term independent of x
2|Exercise 2.2|8|102|1.2.1.3|text|no|Recover positive integer exponent and coefficients from product expansion
3|Exercise 3.1|1|134|1.3.3.2,1.3.4.1,1.3.2.1|text|no|Restricted rational inverse and compound equation, domain filtering
3|Exercise 3.1|2|134|1.3.3.2,1.3.5.1,1.3.5.2,1.4.2.1|text|yes|Linear inverse, intersection, and mirror-graph sketch
3|Exercise 3.1|3|134|1.1.1.1,1.3.2.2,1.3.3.1,1.3.3.2|text|no|Quadratic range, explain noninvertibility, choose left branch, inverse range
3|Exercise 3.1|4|134|1.3.2.2,1.3.3.1,1.3.3.2,1.3.4.1|text|no|Parameterised domain/range and one-one restriction; composition equations determine constants
3|Exercise 3.2|1|145|1.4.1.1,1.4.2.1|text|no|Perpendicular bisector/intersection or parameter from gradient and distance
3|Exercise 3.2|3|145|1.4.1.1,1.4.2.1|text|no|Perpendicular bisector/intersection or parameter from gradient and distance
3|Exercise 3.2|2|145|1.4.1.1,1.4.2.1|diagram|no|Rectangle or parallelogram geometry recovers missing coordinates
3|Exercise 3.2|4|145|1.4.1.1,1.4.2.1|diagram|no|Rectangle or parallelogram geometry recovers missing coordinates
3|Exercise 3.2|5|145|1.4.1.1,1.4.2.1|text|no|Isosceles triangle proof, exact area and perpendicular projection
4|Exercise 4.1|1|163|1.5.1.2|text|no|Exact degrees-to-radians or rounded radians-to-degrees; demand absent from sampled NSSCAS
4|Exercise 4.1|2|163|1.5.1.2|text|no|Exact degrees-to-radians or rounded radians-to-degrees; demand absent from sampled NSSCAS
4|Exercise 4.1|3|163|1.5.2.1,1.5.2.2|table|no|Reverse unknown radius/angle/arc/sector area from mixed data
4|Exercise 4.1|4|163|1.5.2.1,1.5.2.2|diagram|no|Annular sector, angle, perimeter and area; AD=12 so outer radius20 not12
4|Exercise 4.1|5|163|1.5.2.2|diagram|no|Circle with two equal central angles: shaded sector plus two triangles; supports compound area, not automatic full single-segment demand coverage
4|Exercise 4.1|6|163|1.5.2.1|diagram|no|Tangent/arc curvilinear triangle perimeter in symbolic r,α
4|Exercise 4.2|1|223|1.6.2.1,1.6.2.2,1.6.6.1|graph|no|Read amplitude/period/midline and smallest root from transformed sine
4|Exercise 4.2|2|223|1.6.1.1,1.6.2.3,1.3.3.2|text|yes|Two-graph sketches and root count or cosine inverse-domain restriction
4|Exercise 4.2|5|223|1.6.1.1,1.6.2.3,1.3.3.2|text|yes|Two-graph sketches and root count or cosine inverse-domain restriction
4|Exercise 4.2|3|223|1.6.5.2|text|no|Quadratic trig reduction in (a); part (b) lacks a specified solution interval and requires clarification before use under LIMIT02
4|Exercise 4.2|4|223|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Bounded trig equations with double/fractional argument
4|Exercise 4.2|6|223|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Bounded trig equations with double/fractional argument
4|Exercise 4.2|7|224|1.6.5.1,1.6.5.2,1.6.6.1,1.6.6.2|text|no|Prove identity then hence solve; preserve original-expression exclusions
4|Exercise 4.2|9|224|1.6.5.1,1.6.5.2,1.6.6.1,1.6.6.2|text|no|Prove identity then hence solve; preserve original-expression exclusions
4|Exercise 4.2|8|224|1.6.4.1,1.6.5.1|text|no|Principal inverse-sine angle then exact squared ratios; sign is removed by squaring, so only partial evidence for full principal-value distinctions
4|Exercise 4.2|10|224|1.6.6.1,1.6.6.2,1.6.5.2|graph|no|Find both bounded tan/cos intersections, not only the acute one
4|Exercise 4.2|11|224|1.6.5.1,1.6.5.2,1.6.6.1|text|no|Identity invariant and coupled trigonometric equation
5|Exercise 5|1|259|1.7.1.1,1.7.1.2,1.7.3.1,1.7.3.2,1.7.4.2,1.7.5.1,1.7.5.2|text|no|Coordinates, unit vector, angle/perpendicularity, parameter values
5|Exercise 5|2|259|1.7.1.1,1.7.1.2,1.7.3.1,1.7.3.2,1.7.4.2,1.7.5.1,1.7.5.2|text|no|Coordinates, unit vector, angle/perpendicularity, parameter values
5|Exercise 5|3|259|1.7.1.1,1.7.2.3,1.7.3.2,1.7.4.2,1.7.5.1|diagram|no|Triangular-prism height, midpoint displacements and angle; stamp overlaps text but essential givens remain readable
5|Exercise 5|4|260|1.7.1.1,1.7.2.3,1.7.3.2,1.7.5.1|diagram|no|Pyramid parallel square cross-section height then displacement and angle
5|Exercise 5|5|260|1.7.5.1,1.7.3.1,1.7.2.3|text|no|Angle and external ratio AC=3AB; unit position vector
5|Exercise 5|6|260|1.7.2.3,1.7.3.1,1.7.5.1,1.7.4.1|diagram|no|Parallelogram diagonals, acute angle and perimeter
6|Exercise 6|1|312|1.8.2.1,1.8.2.2|text|no|Simplify powers/quotient before differentiation or chain rule; product rule not required in Theme1
6|Exercise 6|2|312|1.8.2.1,1.8.2.2|text|no|Simplify powers/quotient before differentiation or chain rule; product rule not required in Theme1
6|Exercise 6|3|312|1.8.3.1,1.4.2.1|text|no|Tangent, normal second intersection, intersection of tangents
6|Exercise 6|4|312|1.8.3.2|text|no|Decide increasing/decreasing/neither on stated domain with justification
6|Exercise 6|5|312|1.8.3.1,1.8.3.3|text|no|Rational curve tangent and connected rate
6|Exercise 6|6|312|1.8.1.2,1.8.4.1,1.8.4.2|graph|no|First/second derivatives and stationary coordinates/nature
6|Exercise 6|7|313|1.8.3.1,1.8.4.1,1.8.4.2|text|no|Normal-axis intersection and all stationary points on reciprocal combination
6|Exercise 6|8|313|1.4.1.1,1.8.4.1,1.8.4.2|diagram|no|Open-container area constraint, derive cubic volume and optimise/classify
6|Exercise 6|9|313|1.8.3.3|diagram|no|Triangular-prism water depth: derive V(h) then connected rate
7|Exercise 7|1|367|1.9.1.2,1.9.3.1|text|no|Powers/linear composites and finite definite integrals
7|Exercise 7|2|367|1.9.1.2,1.9.3.1|text|no|Powers/linear composites and finite definite integrals
7|Exercise 7|3|367|1.8.3.1,1.9.2.1,1.9.2.2|text|no|Tangent through origin determines derivative parameter then curve constant
7|Exercise 7|4|367|1.9.4.1|graph|no|Area from positive parabola to axes
7|Exercise 7|5|367|1.9.1.2,1.9.2.2,1.9.4.1,1.9.4.2|text|no|Reciprocal-power area/volume or curve recovery before area
7|Exercise 7|6|367|1.9.1.2,1.9.2.2,1.9.4.1,1.9.4.2|text|no|Reciprocal-power area/volume or curve recovery before area
7|Exercise 7|7|368|1.9.4.3,1.8.3.4|text|no|Integrate acceleration with initial velocity; total distance requires splitting at change of direction
7|Exercise 7|8|368|1.4.2.1,1.9.4.1|graph|no|Line/square-root intersection then area between curves
7|Exercise 7|9|368|1.8.2.1,1.9.2.1,1.9.2.2|text|no|Second derivative supplied, recover first derivative and curve using two conditions
7|Exercise 7|10|368|1.8.3.1,1.9.4.2|graph|no|Normal and y-axis revolution of negative-x-side square-root region
7|Exercise 7|11|368|1.8.3.4,1.8.4.1,1.9.4.3|text|no|Symbolic velocity, acceleration, maximum speed and stop-to-stop distance
8|Exercise 8|1|401|2.1.1.1|text|no|Evaluate modulus expressions with negative input
8|Exercise 8|2|401|2.1.1.2|text|no|Modulus equations, including no-solution case
8|Exercise 8|3|401|2.1.1.3|text|no|Modulus inequalities and admissible sign of right-hand expression
8|Exercise 8|11|401|2.1.1.3|text|no|Modulus inequalities and admissible sign of right-hand expression
8|Exercise 8|4|401|2.1.3.1,2.1.3.3|text|no|Cubic by linear division
8|Exercise 8|5|401|2.1.4.2,2.1.4.4|text|no|Cubic factorisation and equation
8|Exercise 8|6|401|2.1.4.2,2.1.4.4|text|no|Cubic factorisation and equation
8|Exercise 8|7|401|2.1.4.1|text|no|Degree-five dividend exceeds LIMIT05 domain; exclude original as a required 8227 exemplar, although remainder-theorem concept is related
8|Exercise 8|8|401|2.1.3.2,2.1.3.3,2.1.4.3|text|no|Quadratic divisor or supplied quadratic factor with unknown coefficients; degrees within LIMIT05
8|Exercise 8|12|401|2.1.3.2,2.1.3.3,2.1.4.3|text|no|Quadratic divisor or supplied quadratic factor with unknown coefficients; degrees within LIMIT05
8|Exercise 8|9|401|2.1.2.1|text|yes|Integer-coefficient shifted/reflected modulus, vertex/intercepts
8|Exercise 8|10|401|2.1.1.2,1.4.2.1|text|no|Linear equation plus modulus relation, two candidate intersections
8|Exercise 8|13|402|1.1.3.2,2.1.3.3|text|no|Recover unknown divisor/quotient coefficients from supplied division identity
8|Exercise 8|14|402|2.1.4.1,2.1.4.2,2.1.4.3,2.1.4.4|text|no|Factor/remainder coefficient constraints; Q18 hence bounded secant equation
8|Exercise 8|15|402|2.1.4.1,2.1.4.2,2.1.4.3,2.1.4.4|text|no|Factor/remainder coefficient constraints; Q18 hence bounded secant equation
8|Exercise 8|16|402|2.1.4.1,2.1.4.2,2.1.4.3,2.1.4.4|text|no|Factor/remainder coefficient constraints; Q18 hence bounded secant equation
8|Exercise 8|17|402|2.1.4.1,2.1.4.2,2.1.4.3,2.1.4.4|text|no|Factor/remainder coefficient constraints; Q18 hence bounded secant equation
8|Exercise 8|18|402|2.1.4.1,2.1.4.2,2.1.4.3,2.1.4.4|text|no|Factor/remainder coefficient constraints; Q18 hence bounded secant equation
8|Exercise 8|19|402|1.1.1.1,1.1.1.2,1.1.2.3,1.3.5.1,2.1.2.1,2.1.1.3|text|yes|Sketch parabola and modulus, two negative roots condition and graph-based inequality
9|Exercise 9|1|441|2.2.1.1,2.2.1.2|text|no|Log laws and exponential/logarithmic form conversions without change of base
9|Exercise 9|2|441|2.2.1.1,2.2.1.2|text|no|Log laws and exponential/logarithmic form conversions without change of base
9|Exercise 9|3|441|2.2.1.1,2.2.1.2|text|no|Log laws and exponential/logarithmic form conversions without change of base
9|Exercise 9|4|441|2.2.1.1,2.2.1.2|text|no|Log laws and exponential/logarithmic form conversions without change of base
9|Exercise 9|5|441|2.2.1.2,2.2.3.1|text|no|Exponential/log equations, positive domains and supplied exponential substitution
9|Exercise 9|9|441|2.2.1.2,2.2.3.1|text|no|Exponential/log equations, positive domains and supplied exponential substitution
9|Exercise 9|10|441|2.2.1.2,2.2.3.1|text|no|Exponential/log equations, positive domains and supplied exponential substitution
9|Exercise 9|6|441|1.3.3.2,2.2.2.2|text|no|Inverse log/exp functions; part (a) log_3(x^4) needs a specified sign branch before an inverse function exists
9|Exercise 9|7|441|2.2.2.2|text|yes|Reflected exponential/log graphs; preserve -3^x versus (-3)^x distinction
9|Exercise 9|8|441|2.6.1.1,2.2.2.2|text|yes|Draw exponential and a chosen line to estimate root; numerical plotting task is distinct from basic shape-only sketch
9|Exercise 9|11|442|2.2.4.1,2.2.4.2|text|no|Power model with points on unspecified straight line; missing transformed-axis definition must be clarified
9|Exercise 9|12|442|2.2.1.2|text|no|Parameter log equation; retain positive log arguments
9|Exercise 9|13|442|2.2.4.1,2.2.4.2|graph|no|Recover A,p from ln y versus x for shifted exponent p(x-1); same item as Goldie 2D Q14
9|Exercise 9|14|442|2.2.2.2,1.3.3.2|text|yes|Log graph, x-axis reflection and inverse
9|Exercise 9|15|442|2.2.4.1,2.2.4.2|text|no|Read two log-linear points, recover exponential and evaluate
10|Exercise 10|1|478|2.3.2.1,2.3.1.1,1.6.6.1,1.6.6.2|text|no|Reciprocal Pythagorean identities reduce bounded equations
10|Exercise 10|2|478|2.3.2.1,2.3.1.1,1.6.6.1,1.6.6.2|text|no|Reciprocal Pythagorean identities reduce bounded equations
10|Exercise 10|3|478|2.3.2.2,2.3.2.3,2.3.2.5,1.6.6.1,1.6.6.2|text|no|Compound/double-angle proof, exact evaluation and equations; Q6 duplicates Revision10 Q4
10|Exercise 10|4|478|2.3.2.2,2.3.2.3,2.3.2.5,1.6.6.1,1.6.6.2|text|no|Compound/double-angle proof, exact evaluation and equations; Q6 duplicates Revision10 Q4
10|Exercise 10|5|478|2.3.2.2,2.3.2.3,2.3.2.5,1.6.6.1,1.6.6.2|text|no|Compound/double-angle proof, exact evaluation and equations; Q6 duplicates Revision10 Q4
10|Exercise 10|6|478|2.3.2.2,2.3.2.3,2.3.2.5,1.6.6.1,1.6.6.2|text|no|Compound/double-angle proof, exact evaluation and equations; Q6 duplicates Revision10 Q4
10|Exercise 10|7|478|2.3.2.4,1.6.6.1,1.6.6.2|text|no|R-form with doubled argument, all roots and reciprocal-square minimum
11|Exercise 11|1|523|2.4.2.2,2.4.1.1,2.3.1.1|text|no|Derive cot derivative from quotient of sin/cos; formula not assumed
11|Exercise 11|2|523|2.4.2.1,1.8.4.1,1.8.4.2|text|no|Log product stationary point and nature
11|Exercise 11|3|523|2.4.2.1,1.8.3.1,1.8.4.1|graph|no|Exponential/trig or polynomial/log curve tangent/gradient and stationary coordinates
11|Exercise 11|5|523|2.4.2.1,1.8.3.1,1.8.4.1|graph|no|Exponential/trig or polynomial/log curve tangent/gradient and stationary coordinates
11|Exercise 11|4|523|2.4.2.2,1.8.3.1|text|no|Exponential quotient tangent with integer-coefficient line form
11|Exercise 11|6|524|2.4.3.1,1.8.3.1|text|no|Implicit polynomial derivative and tangent equation
11|Exercise 11|7|524|2.4.3.1,1.8.3.1|text|no|Implicit polynomial derivative and tangent equation
11|Exercise 11|8|524|2.4.3.2,2.4.3.3,1.8.4.1|text|no|Parametric derivative, stationary point or exact gradient
11|Exercise 11|9|524|2.4.3.2,2.4.3.3,1.8.4.1|text|no|Parametric derivative, stationary point or exact gradient
11|Exercise 11|10|524|2.4.1.1,2.3.2.4,2.4.3.3,1.6.6.1|graph|no|Derivative put into R-form to locate both prescribed-gradient points, with shifted interval and precision
12|Exercise 12|1|552|2.5.1.1,1.9.3.1,2.2.1.2|text|no|Show exact log integral with both bounds
12|Exercise 12|2|552|2.5.1.2,2.5.2.1,2.5.1.1,1.9.3.1|text|no|Elementary trig, reciprocal identity and exact log/exponential form
12|Exercise 12|3|552|2.5.1.2,2.5.2.1,2.5.1.1,1.9.3.1|text|no|Elementary trig, reciprocal identity and exact log/exponential form
12|Exercise 12|4|552|2.5.1.1,1.9.3.1,2.5.3.1,2.5.3.2|graph|no|Simplify exponential quotient, exact log integral and separate trapezia area; graphic has stray duplicated integral caption from (b)
12|Exercise 12|5|552|2.5.2.1,2.5.2.2,2.5.1.1,1.9.3.1|text|no|Choose identity; unknown upper logarithmic-integral bound
12|Exercise 12|6|552|2.5.2.1,2.5.2.2,2.5.1.1,1.9.3.1|text|no|Choose identity; unknown upper logarithmic-integral bound
12|Exercise 12|7|553|2.5.1.1|text|no|Simplify e^x(1+e^x) before elementary integration
12|Exercise 12|8|553|2.4.1.2,1.8.4.1,2.5.1.1,1.9.4.1|graph|no|Exact stationary abscissa and exponential area
12|Exercise 12|9|553|2.5.1.1,1.9.3.1,2.5.3.1,2.5.3.2|text|no|Exact reciprocal-linear integral plus log trapezia; same pair as Goldie 5C Q11
12|Exercise 12|10|553|2.5.1.1,1.9.3.1,2.5.4.1,2.5.4.2|text|yes|Exact integral, exponential sketch and trapezia over/under explanation
12|Exercise 12|11|553|2.5.2.1,2.5.2.2,1.9.3.1,1.9.4.2|graph|no|Identity integral and linked volume of squared mixed trig curve
13|Exercise 13|1|579|2.6.1.1,2.6.1.2,2.6.4.1,2.6.4.2|text|yes|Graphical uniqueness, bracket and log iteration
13|Exercise 13|2|579|2.4.2.2,1.8.4.1,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|Stationary sine-quotient curve then radian inverse-tan iteration
13|Exercise 13|3|579|2.5.1.1,1.9.3.1,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|no|Unknown bound in squared exponential integral, rearrangement and iteration
13|Exercise 13|4|580|2.4.2.1,1.8.4.1,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|Maximum of 2xe^{-x}, two equal-height points and iteration selecting the left one
13|Exercise 13|5|580|2.5.1.1,1.9.3.1,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|no|Unknown upper bound in x+1/x integral gives square-root/log iteration
13|Exercise 13|6|580|2.3.1.2,2.6.1.1,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|yes|Secant/line root uniqueness and inverse-cos fixed-point iteration in radians
1|Example|21|31|1.1.1.1,1.1.1.2,1.1.1.3|text|yes|Complete square, identify nature and sketch quadratic
1|Example|24|34|1.1.1.1,1.1.1.2,1.1.1.3|text|yes|Quadratic sketch with positive minimum/no real intercept; alternate vertex methods shown
1|Try Now|24|34|1.1.1.1,1.1.1.2,1.1.1.3|text|yes|Four quadratic sketches including reversed opening
1|Example|25|35|1.1.5.1|graph|no|Reconstruct parabola from roots and vertex/intercept as alternative sufficient data
1|Try Now|25|35|1.1.5.1|text|no|Two intercepts or tangent root plus another point
1|Example|26|35|1.1.5.1|text|no|Vertex and y-intercept determine parabola; source solution diagram is not a given
1|Try Now|27|37|1.1.5.1|graph|no|Recover two quadratic equations from plotted vertices/intercepts
1|Example|28|37|1.1.6.1,1.1.6.2|text|no|Quadratic inequality with two outer intervals; source solution graph/number line are teaching assets
1|Try Now|28|38|1.1.6.1,1.1.6.2|text|yes|Solve four inequalities and explicitly illustrate each on a number line
1|Example|29|38|1.1.6.1,1.1.6.2|text|no|Connected open solution interval
1|Try Now 29|1|38|1.1.6.1,1.1.6.2|text|yes|Four inequalities with number-line illustrations
1|Try Now 29|2|38|1.1.6.1,1.1.6.2|text|no|Rearranged quadratic inequalities; Q4 boundary answers requested to two decimals
1|Try Now 29|3|38|1.1.6.1,1.1.6.2|text|no|Rearranged quadratic inequalities; Q4 boundary answers requested to two decimals
1|Try Now 29|4|38|1.1.6.1,1.1.6.2|text|no|Rearranged quadratic inequalities; Q4 boundary answers requested to two decimals
1|Example|34|43|1.1.3.2|text|no|Identity coefficient comparison or equivalent completing-square method
1|Try Now 34|1|43|1.1.3.2|text|no|Identity coefficients in quadratic/cubic/quartic forms; last item has two lettered identities
1|Try Now 34|2|43|1.1.3.2|text|no|Identity coefficients in quadratic/cubic/quartic forms; last item has two lettered identities
1|Try Now 34|3|43|1.1.3.2|text|no|Identity coefficients in quadratic/cubic/quartic forms; last item has two lettered identities
1|Try Now 34|4|43|1.1.3.2|text|no|Identity coefficients in quadratic/cubic/quartic forms; last item has two lettered identities
1|Try Now 34|5|43|1.1.3.2|text|no|Identity coefficients in quadratic/cubic/quartic forms; last item has two lettered identities
1|Try Now 34|6|43|1.1.3.2|text|no|Identity coefficients in quadratic/cubic/quartic forms; last item has two lettered identities
1|Example|35|44|1.1.3.2|text|no|Find coefficients in supplied rational identity; no general partial-fractions construction required
1|Try Now 35|1|44|1.1.3.2|text|no|Quartic identities; remaining numbered questions continue PDF45
1|Try Now 35|2|44|1.1.3.2|text|no|Quartic identities; remaining numbered questions continue PDF45
1|Try Now 35|3|45|1.1.3.2|text|no|Products of polynomial factors, compare coefficients
1|Try Now 35|4|45|1.1.3.2|text|no|Products of polynomial factors, compare coefficients
1|Example|36|45|1.1.5.2|text|no|Reconstruct cubic from three roots and another point
1|Try Now 36|1|46|1.1.5.2|graph|no|First numbered item gives roots/point in prose; second gives two graphs. Minimum record representation includes given graphs in item2 only; item1 override required
1|Try Now 36|2|46|1.1.5.2|graph|no|First numbered item gives roots/point in prose; second gives two graphs. Minimum record representation includes given graphs in item2 only; item1 override required
1|Example|37|46|1.1.5.2|graph|no|Simple and repeated roots; source note insists on integer factors, but monic factors are valid with compensating free leading coefficient
1|Try Now|37|46|1.1.5.2|text|no|Two reconstructions from a tangent root, simple root and extra point; root factors may be scaled consistently
2|Example|1|54|1.2.2.1,1.2.2.2|text|no|Explicitly classify AP versus GP and find common difference/ratio
2|Try Now|1|54|1.2.2.1,1.2.2.2|text|no|Four sequence classifications, including negative and decimal terms
2|Example|2|54|1.2.3.1|text|no|AP term condition determines parameter then actual terms
2|Try Now 2|1|54|1.2.3.1,1.2.3.2|text|no|GP parameter or overlapping AP/GP constraints; item1 is GP only and needs mapping refinement
2|Try Now 2|2|54|1.2.3.1,1.2.3.2|text|no|GP parameter or overlapping AP/GP constraints; item1 is GP only and needs mapping refinement
2|Example|29|77|1.2.3.2,1.2.5.2|text|no|Convergent GP partial sums and infinite sum81; area illustration explains limiting accumulation
2|Try Now 29|1|78|1.2.5.2|text|no|Four convergent infinite GP sums, with alternating signs
2|Try Now 29|2|78|1.2.5.2|text|no|Known first term12 and infinite sum24 determine ratio1/2 and initial4 terms
2|Example|30|78|1.2.4.1,1.2.4.2,1.2.5.2|text|no|Infinite sigma sum starts n1, so first term6 rather than24; sum8
2|Try Now 30|1|78|1.2.4.1,1.2.4.2,1.2.5.2|text|no|Six infinite sigma GPs; read shifted exponent and lower bound, including alternating signs
2|Try Now 30|2|78|1.2.4.1,1.2.4.2,1.2.5.2|text|no|Substitute x=-3/4 in sigma GP and compute convergent sum-1
2|Example|31|79|1.2.4.1,1.2.4.2,1.2.5.1,1.2.5.2|text|no|Given infinite sigma sum12, determine p5/6 and check convergence
2|Try Now 31|1|79|1.2.4.1,1.2.4.2,1.2.5.2|text|no|Unknown coefficient of convergent infinite sigma GP, ratio1/4
2|Try Now 31|2|79|1.2.4.1,1.2.4.2,1.2.5.2|text|no|Unknown coefficient with shifted starting exponent in infinite sigma GP
2|Try Now 31|3|79|1.2.3.2,1.2.5.2|text|no|Infinite sum and first3 sum determine negative ratio-1/3 and initial3 terms
2|Try Now 31|4|79|1.2.2.2,1.2.5.1,1.2.5.2|text|no|Justify GP recognition and convergence, then evaluate infinite sum
2|Try Now 31|5|79|1.2.5.1,1.2.5.2|text|no|State convergence interval then solve infinite-sum equation for ratio x
2|Example|32|80|1.2.3.1,1.2.3.3|text|no|Rope-cutting AP model; original62cm inconsistent with metre pieces, must correct to62m before use
2|Try Now 32|1|80|1.2.3.1,1.2.3.3|text|no|Polygon perimeter and shortest/longest AP sides determine number of sides
2|Try Now 32|2|80|1.2.3.1|text|no|Sum even integers50to100 inclusive; include both endpoints
2|Try Now 32|3|80|1.2.3.1,1.2.3.3|text|no|Six unequal circle sector angles in AP total360; largest three times smallest
2|Try Now 32|4|80|1.2.3.1,1.2.3.3|text|no|Hexagon perimeter36cm and largest side five times smallest; determine all six AP sides
2|Example|33|81|1.2.3.2,1.2.3.3|text|no|Donation geometric decay, first threshold year and disjoint finite totals; worked solution continues PDF82
3|Example|1|109|1.3.1.1|graph|no|Function or relation decision across graphs, tables and coordinate sets; repeated identical pair alone would not violate function definition
3|Try Now|1|109|1.3.1.1|graph|no|Graph/table/point-set classification; parts (b)(c) continue PDF110
3|Example|2|111|1.3.1.1,1.3.3.1|diagram|no|Classify one-to-one versus many-to-one from graphs and arrow mappings
3|Try Now|2|111|1.3.1.1,1.3.3.1|diagram|no|Function admissibility and one-to-one decision using graph and arrow mapping
3|Example|3|112|1.3.1.2,1.3.2.1,1.3.2.2|graph|no|Read finite domains/ranges, open endpoints and turning-point range
3|Try Now|3|113|1.3.1.2,1.3.2.1,1.3.2.2|graph|no|Read domains/ranges of three relations; (a) is a circle and is not a function despite heading
3|Example|4|113|1.3.2.2,1.1.1.1|text|no|Linear domain-to-range and unrestricted quadratic minimum via square completion
3|Try Now 4|1|114|1.3.2.2|text|no|Linear or quadratic image of stated interval
3|Try Now 4|2|114|1.3.2.2|text|no|Linear or quadratic image of stated interval
3|Try Now 4|4|114|1.3.2.2|text|no|Linear or quadratic image of stated interval
3|Try Now 4|3|114|1.3.2.2,1.1.1.1|text|no|Complete square and infer quadratic range
3|Example|5|114|1.3.2.2|text|no|Restricted quadratic range must compare vertex and both endpoint limits
3|Try Now 5|1|114|1.3.2.2|text|no|Restricted quadratic ranges, including open endpoint versus attained extremum
3|Try Now 5|2|114|1.3.2.2|text|no|Restricted quadratic ranges, including open endpoint versus attained extremum
3|Try Now 5|3|114|1.3.2.2|text|no|Restricted quadratic ranges, including open endpoint versus attained extremum
3|Example|6|115|1.3.1.1|text|no|Evaluate and distinguish arithmetic operations on functions from composition
3|Try Now 6|1|116|1.3.1.1|text|no|Arithmetic combinations of two functions, explicitly separate from composition
3|Try Now 6|2|116|1.3.1.1|text|no|Arithmetic combinations of two functions, explicitly separate from composition
3|Try Now 6|3|116|1.3.1.1|text|no|Arithmetic combinations of two functions, explicitly separate from composition
3|Example|7|116|1.3.1.3,1.3.4.1|text|no|Order of composition and evaluating two numerical compositions
3|Try Now 7|1|117|1.3.4.1|text|no|Numerical compositions, including double application
3|Try Now 7|2|117|1.3.4.1|text|no|Numerical compositions, including double application
3|Try Now 7|3|117|1.3.4.1|text|no|Numerical compositions, including double application
3|Example|8|117|1.3.4.1|text|no|Form both ordered composites and gg
3|Try Now 8|1|117|1.3.4.1|text|no|Algebraic composite expressions
3|Try Now 8|2|117|1.3.4.1|text|no|Algebraic composite expressions
3|Example|9|118|1.3.4.1|text|no|Solve composite rational equation; enlarged source render confirms correct domain x not equal -1.5
3|Try Now 9|1|118|1.3.4.1|text|no|Composite equations, commuting parameter and identity composites; Q3 explicitly restricted domain
3|Try Now 9|2|118|1.3.4.1|text|no|Composite equations, commuting parameter and identity composites; Q3 explicitly restricted domain
3|Try Now 9|3|118|1.3.4.1|text|no|Composite equations, commuting parameter and identity composites; Q3 explicitly restricted domain
3|Try Now 9|4|118|1.3.4.1|text|no|Composite equations, commuting parameter and identity composites; Q3 explicitly restricted domain
3|Try Now 9|5|118|1.3.4.1|text|no|Composite equations, commuting parameter and identity composites; Q3 explicitly restricted domain
3|Example|10|119|1.3.3.2|text|no|Square-root inverse formula needs domain x>=0; requested inverse(-2) is undefined, source answer7 is invalid
3|Try Now 10|1|119|1.3.3.2|text|no|Linear/cubic/rational inverses; Q2(c) quadratic has no branch restriction and therefore no unique inverse function
3|Try Now 10|2|119|1.3.3.2|text|no|Linear/cubic/rational inverses; Q2(c) quadratic has no branch restriction and therefore no unique inverse function
3|Example|11|120|1.3.3.2,1.3.5.2|text|yes|Find inverse and sketch both linear functions with y=x reflection
3|Try Now 11|1|121|1.3.3.2,1.3.5.2|text|yes|Two linear function/inverse paired sketches, relationship made clear
3|Try Now 11|2|121|1.3.3.2,1.3.5.2|text|yes|Two linear function/inverse paired sketches, relationship made clear
3|Example|12|122|1.3.2.1,1.3.2.2|text|no|Rational and radical domains/ranges; (b) solution incorrectly concludes range all real via unrestricted inverse polynomial, correct range y>=0
3|Try Now|12|122|1.3.2.1,1.3.2.2|text|no|Rational and reciprocal-square-root domain/range, zero denominator excluded
3|Example|13|123|1.1.1.1,1.3.2.2,1.3.3.2,1.3.5.2|text|yes|Restricted quadratic inverse domain, chosen negative root and reflected paired sketch
3|Try Now 13|1|124|1.1.1.1,1.3.2.2,1.3.3.1,1.3.3.2|text|no|Least admissible quadratic restriction then inverse including shifted restriction m=5
3|Try Now 13|2|124|1.1.1.1,1.3.2.2,1.3.3.1,1.3.3.2|text|no|Least admissible quadratic restriction then inverse including shifted restriction m=5
3|Try Now 13|3|124|1.1.1.1,1.3.2.2,1.3.3.1,1.3.3.2|text|no|Least admissible quadratic restriction then inverse including shifted restriction m=5
3|Example|14|125|1.3.4.1,1.3.4.2,1.3.2.2,1.3.3.2|text|no|Composite existence from image containment, largest restriction, inverse on selected negative branch
3|Try Now 14|1|126|1.3.4.1,1.3.3.2|text|no|Recover inner function, composite inverse/domain and composite equation
3|Try Now 14|2|126|1.3.4.1,1.3.3.2|text|no|Recover inner function, composite inverse/domain and composite equation
3|Try Now 14|3|126|1.3.2.2,1.3.4.2|text|no|Ranges and explain why gf cannot be formed on whole stated domain
3|Try Now 14|4|126|1.1.1.1,1.3.3.1,1.3.3.2,1.3.4.2|text|no|Largest one-to-one domain and largest inner-function bound allowing composition
3|Example|15|127|1.3.2.2,1.3.3.2,1.3.5.2|graph|yes|Piecewise line/reciprocal function inverse; related structural extension, check QUAL01 before selecting whole piecewise sketch
3|Try Now|15|127|1.3.2.2,1.3.5.1|text|yes|Piecewise quadratic/line graph and range; related structural extension requiring QUAL01 review
3|Example|17|137|1.4.1.1,1.4.2.1|diagram|no|Parallel/perpendicular trapezium sides and missing vertex from simultaneous lines
3|Try Now 17|1|137|1.4.1.1,1.4.2.1|diagram|no|Rectangle and right triangle with point on opposite side; reconstruct missing vertices
3|Try Now 17|2|137|1.4.1.1,1.4.2.1|diagram|no|Rectangle and right triangle with point on opposite side; reconstruct missing vertices
3|Example|18|138|1.4.1.1,1.4.2.1|text|no|Perpendicular bisector meets parallel line, then distance; PDF139 repeats this same printed page
3|Try Now 18|1|140|1.4.1.1,1.4.2.1|text|no|Perpendicular-bisector intersection in words
3|Try Now 18|2|140|1.4.1.1,1.4.2.1|text|no|Perpendicular-bisector intersection in words
3|Example|19|140|1.4.1.1|text|no|Positive intercept parameters from length and gradient
3|Try Now 19|1|140|1.4.1.1|text|no|Unknown coordinates from gradient and distance, including two possible locations
3|Try Now 19|2|140|1.4.1.1|text|no|Unknown coordinates from gradient and distance, including two possible locations
3|Example|20|141|1.4.1.1,1.4.2.1|text|no|Reflection point via perpendicular intersection and midpoint; diagram is in solution
3|Try Now|20|141|1.4.1.1,1.4.2.1|diagram|no|Perpendicular lines with intercept, intersection and reflected point
3|Example|21|142|1.4.1.1|text|no|Parametric coordinate geometry, triangle area and midpoint identity
3|Try Now 21|1|143|1.4.1.1,1.4.2.1|diagram|no|Triangle side gradients and bisector; rhombus vertices/area; reflected quadrilateral perimeter
3|Try Now 21|2|143|1.4.1.1,1.4.2.1|diagram|no|Triangle side gradients and bisector; rhombus vertices/area; reflected quadrilateral perimeter
3|Try Now 21|3|143|1.4.1.1,1.4.2.1|diagram|no|Triangle side gradients and bisector; rhombus vertices/area; reflected quadrilateral perimeter
4|Example|1|155|1.5.1.2|text|no|Degree/radian conversions; blanket textbook precision notes must defer to actual examination instruction
4|Example|2|155|1.5.1.2|text|no|Degree/radian conversions; blanket textbook precision notes must defer to actual examination instruction
4|Try Now|1|155|1.5.1.2|text|no|Three degree-to-radian conversions
4|Try Now|2|156|1.5.1.2|text|no|Three radian-to-degree conversions
4|Example|3|156|1.5.2.1|diagram|no|Minor versus major arc
4|Try Now|3|157|1.5.2.1|diagram|no|Minor and major arc lengths
4|Example|4|157|1.5.2.2|diagram|no|Major sector from complementary full-turn angle
4|Try Now|4|158|1.5.2.2|diagram|no|Major sector area
4|Example|5|158|1.5.2.1,1.5.2.2|diagram|no|Unknown angle from perimeter or area then complementary quantity
4|Example|6|158|1.5.2.1,1.5.2.2|diagram|no|Unknown angle from perimeter or area then complementary quantity
4|Try Now|5|158|1.5.2.1,1.5.2.2|diagram|no|Sector perimeter determines angle and area
4|Try Now|6|159|1.5.2.1,1.5.2.2|diagram|no|Sector area determines perimeter
4|Example|7|159|1.5.2.2|diagram|no|Overlapping sectors inside right triangle; shaded intersection by inclusion-exclusion
4|Try Now 7|1|160|1.5.2.2|diagram|no|Triangle minus sector shaded area
4|Try Now 7|2|160|1.5.2.1,1.5.2.2|diagram|no|Metal plate triangle plus sector perimeter and area
4|Example|8|161|1.5.2.1,1.5.2.2,1.5.2.3,1.6.3.1|diagram|no|Exact minor segment, chord, arc and perimeter at 2pi/3
4|Try Now 8|1|161|1.5.2.1,1.5.2.2,1.5.2.3|diagram|no|Sector, segment and chord; parts (b)(c) continue PDF162
4|Try Now 8|2|162|1.5.2.1,1.5.2.2,1.5.2.3|diagram|no|Major segment plus semicircle metal plate with chord radius constraint
4|Example|9|162|1.5.2.2,1.5.2.3|diagram|no|Equal triangle/segment areas give theta=2 sin theta
4|Try Now|9|162|1.5.2.2,1.5.2.3|diagram|no|Semicircle minus segment shaded lune in symbolic r,theta
4|Example|10|168|1.6.1.1,1.6.2.2,1.6.2.3|text|yes|Tangent and its reflection on negative-to-positive radian interval
4|Try Now 10|1|168|1.6.1.1,1.6.2.2,1.6.2.3|text|yes|Sine/cosine reflection with radian or negative-degree interval
4|Try Now 10|2|168|1.6.1.1,1.6.2.2,1.6.2.3|text|yes|Sine/cosine reflection with radian or negative-degree interval
4|Try Now 12|1|175|1.6.2.1,1.6.2.3|text|yes|Amplitude/period/range then transformed trig sketches
4|Try Now 12|2|175|1.6.2.1,1.6.2.3|text|yes|Amplitude/period/range then transformed trig sketches
4|Example|13|175|1.6.2.1,1.6.2.3|text|yes|Tangent period and one-period sketch; worked solution uses degrees although stem omits unit, preserve explicit units in new designs
4|Try Now 13|1|176|1.6.2.1,1.6.2.3|text|yes|Tangent period and transformed tangent radian sketch
4|Try Now 13|2|176|1.6.2.1,1.6.2.3|text|yes|Tangent period and transformed tangent radian sketch
4|Example|14|176|1.6.2.1,1.6.2.2|text|no|Recover amplitude/vertical shift from extrema
4|Try Now 14|1|176|1.6.2.1,1.6.2.2|text|no|Cosine extrema determine parameters and intercept
4|Try Now 14|2|176|1.6.2.1,1.6.2.2,1.6.2.3|text|yes|Negative cosine amplitude/shift then sketch
4|Example|15|177|1.6.1.1,1.4.1.1|text|yes|Sine sketch and line through maximum, symmetry gives other intersection
4|Try Now 15|1|177|1.6.2.3|text|yes|Reflected cosine or double-argument cosine with line on same axes
4|Try Now 15|2|177|1.6.2.3|text|yes|Reflected cosine or double-argument cosine with line on same axes
4|Try Now 15|3|177|1.6.2.3,2.6.1.1|text|yes|Draw suitable line to count roots of transformed sine equation
4|Example|16|178|1.6.2.1,1.6.2.2,1.6.6.2|graph|no|Recover frequencies, graph range, two intersections and inequality interval
4|Example|18|182|1.6.3.1|diagram|no|Exact lengths from two special-angle right triangles
4|Try Now 18|1|182|1.6.3.1|diagram|no|Exact right-triangle or sine-rule length with 30/45/60 angles
4|Try Now 18|2|182|1.6.3.1|diagram|no|Exact right-triangle or sine-rule length with 30/45/60 angles
4|Example|19|183||text|yes|Supporting reference-angle diagram and rotations, not itself calculation of exact trig values
4|Try Now|19|184||text|yes|Supporting positive degree/radian angle rotations and basic angle
4|Example|20|184||text|yes|Supporting negative rotations and reference angles
4|Try Now|20|184||text|yes|Supporting negative rotations, not standalone syllabus graph coverage
4|Example|24|188|1.6.3.1|text|no|Exact related special angles in all quadrants
4|Try Now|24|188|1.6.3.1|text|no|Nine exact special-angle ratios including angles over pi
4|Example|25|189||text|no|Supporting quadrant sign and Pythagorean ratio recovery, no special angle given
4|Try Now 25|1|189||text|no|Supporting arbitrary-angle ratio recovery from sign and interval
4|Try Now 25|3|189||text|no|Supporting arbitrary-angle ratio recovery from sign and interval
4|Try Now 25|2|189|1.6.3.1|text|no|Special-angle sine from cosine with reflex restriction
4|Example|26|189||text|no|Supporting symbolic ratio recovery and complementary angle using given non-special sine
4|Example|28|191|2.3.1.1|text|no|Six ratios from coordinate point, including reciprocal definitions
4|Example|52|216|1.6.4.1,1.6.3.1|text|no|Principal arccos(-sqrt3/2) in degrees; teaching tables incorrectly include tangent asymptote endpoints
4|Try Now|52|217|1.6.4.1,1.6.3.1|text|no|Three principal inverse trig values in degrees, not all periodic roots
4|Example|53|217|1.6.4.1,1.6.3.1|text|no|Principal arcsine and arctan in pi form; final line (b) changes argument from1 to1/sqrt2 in error, stem value tan inverse1=pi/4 is correct
4|Try Now|53|217|1.6.4.1,1.6.3.1|text|no|Principal inverse trig special-angle values in degrees
4|Example|54|218|1.6.4.1,1.6.3.1,1.6.6.1,1.6.6.2|text|no|Separate principal inverse equation from shifted-argument equation with all bounded roots
4|Try Now 54|1|218|1.6.4.1,1.6.3.1|text|no|Inverse-sine equation reduced to quadratic in x squared
4|Try Now 54|2|219|1.6.4.1|text|no|Principal inverse equation and equality of inverse sine/tangent
4|Try Now 54|3|219|1.6.4.1|text|no|Principal inverse equation and equality of inverse sine/tangent
4|Example|55|219|1.3.3.2,1.3.5.2,1.6.4.1|text|yes|Restricted tangent inverse, its domain and reflected graph pair
4|Example|56|221|1.6.3.1,1.6.4.1|diagram|no|Special-angle symbolic sides and principal arctan angle difference in degrees
5|Example|1|234|1.7.1.1|diagram|no|Read cuboid vertex coordinates with displayed axes
5|Try Now|1|235|1.7.1.1|diagram|no|Two prism coordinate readings
5|Example|2|235|1.7.1.1|diagram|no|Cube centred at origin, negative coordinates
5|Try Now 2|1|235|1.7.1.1|diagram|no|Centred cube and vertical prism axes
5|Try Now 2|2|235|1.7.1.1|diagram|no|Centred cube and vertical prism axes
5|Try Now 7|1|245|1.7.3.2,1.7.4.1|text|no|Coordinate displacement vectors; magnitude in item1 only
5|Try Now 7|2|245|1.7.3.2,1.7.4.1|text|no|Coordinate displacement vectors; magnitude in item1 only
5|Try Now 7|3|245|1.7.2.1,1.7.4.1|text|no|Linear vector combinations or magnitude of difference
5|Try Now 7|4|245|1.7.2.1,1.7.4.1|text|no|Linear vector combinations or magnitude of difference
5|Example|8|245|1.7.2.2,1.7.2.3|diagram|no|Triangle division point and two vector routes
5|Try Now 8|1|245|1.7.2.2,1.7.2.3|diagram|no|Triangle division ratio 1:5
5|Example|10|248|1.7.3.2,1.7.3.3,1.7.2.3|diagram|no|Cuboid midpoint coincidence using position vectors
5|Try Now 10|1|249|1.7.1.1,1.7.3.2,1.7.3.3,1.7.2.3|diagram|no|Triangular prism with midpoint equality
5|Try Now 10|2|249|1.7.3.2,1.7.3.3,1.7.2.3|text|no|Midpoint coincidence or collinearity with vector ratio
5|Try Now 10|3|249|1.7.3.2,1.7.3.3,1.7.2.3|text|no|Midpoint coincidence or collinearity with vector ratio
5|Try Now 10|4|249|1.7.3.3,1.7.3.2,1.7.4.1|diagram|no|Symmetric roof coordinates and slanted-edge lengths
5|Example|15|255|1.7.2.2,1.7.3.3,1.7.4.2,1.7.5.1|diagram|no|Pyramid edge division and scalar-product angle
5|Try Now 15|1|256|1.7.4.2,1.7.5.1|diagram|no|Pyramid scalar-product angle
5|Try Now 15|2|256|1.7.3.3,1.7.4.1,1.7.4.2,1.7.5.1|diagram|no|Symmetric roof vector magnitude and angle
5|Try Now 15|3|256|1.7.3.2,1.7.4.2,1.7.5.1|diagram|no|Cylinder with vertical midpoint and diagonal angle
6|Investigation|1|268|1.8.1.1|graph|yes|Tasks (a)-(g) approach tangent gradient from either secant side; final question transfers to y=x^2+1 at (2,5). Setup PDF267, tasks PDF268
6|Example|1|271|1.8.2.1|text|no|Differentiate five rational-power/constant functions with notation variants
6|Try Now|1|271|1.8.2.1|text|no|Twelve power-rule subparts, including negative and fractional indices
6|Example|2|272|1.8.2.1|text|no|Polynomial derivative by linearity
6|Try Now|2|272|1.8.2.1|text|no|Four polynomial linear combinations
6|Example|3|273|1.8.2.1|text|no|Re-express quotient and radical into powers before differentiation
6|Try Now 3|1|273|1.8.2.1|text|no|Quotient simplification and rational-power combinations
6|Try Now 3|2|273|1.8.2.1|text|no|Quotient simplification and rational-power combinations
6|Example|4|274|1.8.2.1,1.8.1.2|text|no|Change independent variable and expand square before derivative
6|Try Now 4|1|274|1.8.2.1,1.8.1.2|text|no|Requested derivative notation with t, s, v, a and rational-power simplification
6|Try Now 4|2|274|1.8.2.1,1.8.1.2|text|no|Requested derivative notation with t, s, v, a and rational-power simplification
6|Try Now 4|3|274|1.8.2.1,1.8.1.2|text|no|Requested derivative notation with t, s, v, a and rational-power simplification
6|Try Now 15|1|285|1.8.3.1|text|no|Tangent equation and angle to horizontal
6|Try Now 15|2|285|1.8.3.1|graph|no|Acute angle between tangents or tangent and intersecting line; Q3 also solves line/curve intersections
6|Try Now 15|3|285|1.8.3.1|graph|no|Acute angle between tangents or tangent and intersecting line; Q3 also solves line/curve intersections
6|Example|24|294|1.8.3.3|text|no|Moving point with one rate half the other, solve positive square-root substitution
6|Try Now 24|1|294|1.8.3.3|text|no|Curve coordinate rates or spherical balloon volume/radius rates
6|Try Now 24|2|294|1.8.3.3|text|no|Curve coordinate rates or spherical balloon volume/radius rates
6|Example|25|295|1.8.1.2,1.8.2.1,1.8.2.2|text|no|First and second derivative notation, polynomial and linear-composite reciprocal power
6|Try Now 25|1|295|1.8.1.2,1.8.2.1,1.8.2.2|text|no|Second derivatives with rational powers and linear composites
6|Try Now 25|2|295|1.8.1.2,1.8.2.1,1.8.2.2|text|no|Second derivatives with rational powers and linear composites
6|Example|26|297|1.8.4.1,1.8.4.2|text|yes|Cubic maximum/minimum classified by first derivative sign then sketch
6|Try Now|26|298|1.8.4.1,1.8.4.2|text|yes|Two cubic stationary-point/classification sketches
6|Example|27|298|1.8.4.1,1.8.4.2|text|yes|Stationary inflexion with unchanged derivative sign; conclusion line says (0,-1) in error, calculation and graph correctly give (0,1)
6|Try Now|27|299|1.8.4.1,1.8.4.2|text|yes|Positive and negative cubic stationary inflexion sketches
6|Example|28|300|1.8.4.1,1.8.4.2|text|yes|Two stationary points, second derivative classification and cubic sketch
6|Try Now 28|1|300|1.8.4.1,1.8.4.2|text|yes|Second derivative test then cubic sketch
6|Try Now 28|2|300|1.8.4.1,1.8.4.2|text|yes|Second derivative test then cubic sketch
6|Example|29|301|1.8.4.1,1.8.4.2|text|no|Quartic with stationary inflexion and minimum; switch to first derivative sign when second derivative zero
6|Try Now 29|1|301|1.8.4.1,1.8.4.2|text|no|Two quartic classification problems, no sketch explicitly requested
6|Try Now 31|1|304|1.8.4.1|text|no|Parameter from stationary derivative condition
6|Try Now 31|2|304|1.8.4.1,1.1.5.2|graph|no|Recover cubic coefficients from stationary coordinates/roots and classify requested maximum
6|Try Now 31|3|304|1.8.4.1,1.1.5.2|graph|no|Recover cubic coefficients from stationary coordinates/roots and classify requested maximum
6|Try Now 31|4|304|1.8.4.1,1.1.5.2|graph|no|Recover cubic coefficients from stationary coordinates/roots and classify requested maximum
6|Example|34|308|1.8.4.1|diagram|no|Wire split into square/circle, constraint and stationary area. Solution prose says maximise but convex area has a minimum; stem asks stationary only
6|Try Now 34|1|309|1.8.4.1,1.8.4.2|diagram|no|Quarter-circle plate and L-shaped garden optimisation with explicit extremum justification
6|Try Now 34|2|309|1.8.4.1,1.8.4.2|diagram|no|Quarter-circle plate and L-shaped garden optimisation with explicit extremum justification
6|Example|35|310|1.8.4.1|diagram|no|Inscribed cylinder in cone via similar triangles; reject zero radius then stationary volume
6|Try Now 35|1|311|1.8.4.1,1.8.4.2|diagram|no|Cylinder/cone maximum; rectangle under line classify stationary area; eight sheep pens maximum with no nature verification required in item3
6|Try Now 35|2|311|1.8.4.1,1.8.4.2|diagram|no|Cylinder/cone maximum; rectangle under line classify stationary area; eight sheep pens maximum with no nature verification required in item3
6|Try Now 35|3|311|1.8.4.1,1.8.4.2|diagram|no|Cylinder/cone maximum; rectangle under line classify stationary area; eight sheep pens maximum with no nature verification required in item3
7|Example|1|324|1.9.1.1,1.9.1.2|text|no|Given dy/dx, recognise reverse differentiation to recover y with arbitrary constant
7|Try Now|1|325|1.9.1.1,1.9.1.2|text|no|Find y from three given derivatives, no integration symbol supplied
7|Example|2|325|1.9.1.2|text|no|Rational-power antiderivatives
7|Try Now|2|325|1.9.1.2|text|no|Six rational-power integration subparts
7|Example|3|326|1.9.1.2|text|no|Integrate constant or constant multiple and recover y from constant derivative
7|Try Now|3|326|1.9.1.2|text|no|Constant multiples and dy/dx=p
7|Example|4|327|1.9.1.2|text|no|Reverse f-prime and re-express integrands as sum of powers
7|Example|5|327|1.9.1.2|text|no|Reverse f-prime and re-express integrands as sum of powers
7|Try Now|4|327|1.9.1.2|text|no|Recover f from given rational-power f-prime
7|Try Now 5|1|327|1.9.1.2|text|no|Expand or simplify six integrands
7|Try Now 5|2|328|1.9.1.2|text|no|Recover y after algebraic expansion and rational-power simplification
7|Example|6|328|1.9.1.2|text|no|Powers of linear functions with reverse chain coefficient
7|Try Now|6|329|1.9.1.2|text|no|Four linear-power antiderivatives
7|Example|7|329|1.9.1.2|text|no|Linear-function reciprocal/radical integrals with variable t
7|Try Now 7|1|329|1.9.1.2|text|no|Linear powers with t or x and combined numerator over common radical
7|Try Now 7|2|329|1.9.1.2|text|no|Linear powers with t or x and combined numerator over common radical
7|Try Now 7|3|329|1.9.1.2|text|no|Linear powers with t or x and combined numerator over common radical
7|Example|8|330|1.9.2.1,1.9.2.2|text|no|Curve recovery from gradient and point
7|Try Now 8|1|330|1.9.2.1,1.9.2.2|text|no|Gradient and initial point, including power of linear expression
7|Try Now 8|2|330|1.9.2.1,1.9.2.2|text|no|Gradient and initial point, including power of linear expression
7|Try Now|17|341|1.9.4.1|graph|no|Shaded region under x-axis or between roots
7|Example|18|341|1.9.4.1|text|no|Split signed integrals at intercept to obtain unsigned total area
7|Try Now 18|1|342|1.9.4.1|graph|no|Intercepts and total shaded area crossing x-axis
7|Try Now 18|2|342|1.9.4.1|text|no|Unsigned total area with optional sketch as method aid, not explicit assessed sketch
7|Try Now 18|3|342|1.9.4.1|text|no|Unsigned total area with optional sketch as method aid, not explicit assessed sketch
7|Try Now 18|4|342|1.9.4.1|text|no|Unsigned total area with optional sketch as method aid, not explicit assessed sketch
7|Try Now 18|5|342|1.9.4.1|text|yes|Reciprocal-square-root sketch then bounded area
7|Example|20|344|1.9.4.1|graph|no|Region integrated with respect to y; same region as Example16
7|Try Now 20|1|344|1.9.4.1|graph|no|Cubic area beside y-axis with y bounds
7|Try Now 20|2|344|1.9.4.1|graph|no|Defective: y=sqrt(2x-1) cannot bound a region at negative y=-1; graphic draws both inverse branches. Hold original pending corrected relation/domain
7|Try Now 23|1|348|1.8.3.1,1.9.4.1|graph|no|Tangent, intercept and area between tangent and curve
7|Try Now 23|2|348|1.8.3.1,1.9.4.1|graph|no|Tangent, intercept and area between tangent and curve
7|Example|24|348|1.9.4.1|graph|no|Three boundaries in first quadrant; integrate in y
7|Example|26|351|1.9.3.2|text|no|Convergent improper integral 1 to infinity of x^-2
7|Try Now|26|352|1.9.3.2|text|no|Three convergent infinite-interval power integrals
7|Example|27|352|1.9.3.2|text|no|Divergent radical integral over negative infinite interval
7|Try Now|27|352|1.9.3.2|text|no|Convergence/divergence decisions; (c) bounds10 to1 cross internal pole x=2.5, needs split improper-integral treatment beyond simple endpoint exemplars
7|Example|28|353|1.9.3.2|text|no|Contrast convergent inverse-square-root endpoint and divergent inverse-square endpoint
7|Example|29|353|1.9.3.2|text|no|Contrast convergent inverse-square-root endpoint and divergent inverse-square endpoint
7|Try Now|28|353|1.9.3.2|text|no|Convergent singular endpoint integrals
7|Try Now|29|354|1.9.3.2|text|no|Divergent endpoint powers and mixed integrand
7|Example|30|354|1.9.3.2|graph|no|Unbounded region has finite area2
7|Try Now 30|1|354|1.9.3.2|graph|no|Finite limiting area at endpoint singularity
7|Try Now 30|2|354|1.9.3.2|graph|no|Finite limiting area at endpoint singularity
7|Example|32|357|1.9.4.2|graph|no|Reciprocal-linear curve rotated about x-axis
7|Try Now 32|1|357|1.9.4.2|graph|no|Show exact reciprocal-linear volume
7|Try Now 32|2|357|1.9.4.2|text|no|Volumes after squaring rational expressions
7|Try Now 32|3|357|1.9.4.2|text|no|Volumes after squaring rational expressions
7|Example|34|359|1.9.4.2|graph|no|Washer volume about y-axis for region on negative x side, compare absolute radii
7|Try Now 34|1|360|1.9.4.2|graph|no|Four washer problems, including line/curve, fractional power and rotation about either axis; item2 also area
7|Try Now 34|2|360|1.9.4.2|graph|no|Four washer problems, including line/curve, fractional power and rotation about either axis; item2 also area
7|Try Now 34|3|360|1.9.4.2|graph|no|Four washer problems, including line/curve, fractional power and rotation about either axis; item2 also area
7|Try Now 34|4|360|1.9.4.2|graph|no|Four washer problems, including line/curve, fractional power and rotation about either axis; item2 also area
7|Example|35|361|1.9.4.2|graph|no|Volume below horizontal line: cylinder subtraction or direct washers
7|Try Now 35|1|361|1.9.4.2|graph|no|Rational curve versus horizontal line; circular arc bounded volume
7|Try Now 35|2|361|1.9.4.2|graph|no|Rational curve versus horizontal line; circular arc bounded volume
7|Example|36|362|1.9.4.2|diagram|no|Symbolic circular segment rotation then derive sphere volume
7|Try Now|36|362|1.9.4.2|diagram|no|Verify cone volume by integration using symbolic dimensions
8|Example|8|384|2.1.2.1|text|yes|Shifted reflected modulus graph; table method is teaching route rather than syllabus requirement
8|Try Now 8|1|384|2.1.2.1|text|yes|Scaled/shifted/reflected linear-modulus sketches
8|Try Now 8|2|384|2.1.2.1|text|yes|Scaled/shifted/reflected linear-modulus sketches
8|Example|9|385|2.1.2.1|text|yes|Vertex and both intercepts then sketch
8|Try Now 9|1|385|2.1.2.1|text|yes|Twelve linear-modulus graphs with key coordinates
8|Try Now 9|2|385|2.1.2.1|text|yes|Twelve linear-modulus graphs with key coordinates
8|Example|12|388|2.1.1.3|text|no|Modulus inequality with signed linear right side; source boundary testing is an incomplete justification, casewise/graph method must establish interval
8|Try Now|12|388|2.1.1.3|text|yes|Six inequalities; source explicitly requests sketch to help
9|Example|26|427|2.2.2.2,2.6.1.1|text|yes|Exponential/line sketch and count equation roots
9|Try Now 26|1|428|2.2.2.2,2.6.1.1|text|yes|Decay exponential and line, count roots
9|Try Now 26|2|428|2.2.2.2|text|yes|e^x and e^-x paired sketch and reflection
9|Try Now 27|1|431|2.2.1.1|text|no|Unknown log base from a graph point
9|Try Now 27|2|431|2.2.2.2,1.3.2.1,1.3.2.2|text|yes|Reciprocal-base logarithm sketches, domain/range and symmetry
9|Example|28|431|2.2.2.2,1.3.3.2,1.3.5.2|text|yes|Exponential inverse logarithm, reflected paired sketch
9|Try Now 28|1|431|2.2.2.2,1.3.3.2,1.3.5.2|text|yes|Base-two exponential and inverse sketch
9|Try Now|30|437|2.2.4.1|text|no|Select transformed variables and identify gradient/intercept for four nonlinear equations
9|Example|31|437|2.2.4.1,2.2.4.2|graph|no|ln y versus x for y=A b^-x; recover b from negative slope
9|Try Now|31|437|2.2.4.1,2.2.4.2|graph|no|Exponential constants from two transformed points
9|Example|32|438|2.2.4.1,2.2.4.2|graph|no|Power law constants from ln-ln line
9|Try Now 32|1|438|2.2.4.1,2.2.4.2|graph|no|Power law or A times B^(ln x), two transformed coordinates
9|Try Now 32|2|438|2.2.4.1,2.2.4.2|graph|no|Power law or A times B^(ln x), two transformed coordinates
9|Example|33|439|2.2.4.1,2.2.4.2|table|yes|Choose log-linear plot and estimate k,b from experimental data; source concludes 10^0.3=1.20 incorrectly, should approximately2.00
10|Example|1|449|2.3.1.2|text|yes|Secant sketch using cosine zeros and extrema
10|Try Now|1|450|2.3.1.2|text|yes|Cosecant over full degree revolution
10|Example|2|450|2.3.1.2|text|yes|Cotangent sketch with period pi and asymptotes
10|Try Now|2|450|2.3.1.2|text|yes|Double-argument cotangent sketch
10|Example|3|450|2.3.1.2,2.6.1.1|text|yes|Cosecant and line sketch to establish one root
10|Try Now|3|451|2.3.1.2,2.6.1.1|text|yes|Cotangent and increasing line show unique root
11|Example|39|519|2.4.3.2,2.4.3.3,2.3.2.2|graph|no|Parametric derivative in cot form and tangent at positive y-intercept
11|Try Now 39|1|520|2.4.3.2,2.4.3.3,2.3.2.2|graph|no|Ellipse parametric derivative and normal at positive y-axis
11|Try Now 39|2|520|2.4.3.2,2.4.3.3|text|no|Exponential/log/trig parameter tangent or normal, exact or integer line forms
11|Try Now 39|3|520|2.4.3.2,2.4.3.3|text|no|Exponential/log/trig parameter tangent or normal, exact or integer line forms
11|Try Now 39|4|520|2.4.3.2,2.4.3.3|text|no|Exponential/log/trig parameter tangent or normal, exact or integer line forms
11|Try Now 40|1|522|2.4.3.2,2.4.3.3,1.8.4.1|graph|no|Parametric minimum, gradients at roots and normal at selected abscissa
11|Try Now 40|2|522|2.4.3.2,2.4.3.3,1.8.4.1|graph|no|Parametric minimum, gradients at roots and normal at selected abscissa
12|Example|5|533|2.5.1.1,1.9.4.1|graph|no|Exponential area in p then solve unknown bound
12|Try Now 5|1|533|2.5.1.1,1.9.4.1,2.6.3.2|graph|no|Unknown-area boundary gives supplied fixed-point rearrangement
12|Try Now 5|2|533|2.5.1.1,1.9.4.1,2.6.3.2|graph|no|Unknown-area boundary gives supplied fixed-point rearrangement
12|Try Now|9|537|1.1.3.2,2.5.1.1,1.9.3.1|text|no|Given rational decomposition then exact logarithmic integral; no independent general partial fractions required
12|Example|10|537|2.5.1.1,1.9.4.1|graph|no|Reciprocal-linear area with precision
12|Try Now 10|1|537|2.5.1.1,1.9.4.1|graph|no|Log area and rectangle complement, express integral in y
12|Try Now 10|2|537|2.5.1.1,1.9.4.1|graph|no|Log area and rectangle complement, express integral in y
12|Example|18|544|1.6.6.1,2.5.2.1,2.5.2.2,1.9.4.1|graph|no|First positive sine-quadratic root then double-angle integral exact area
12|Try Now 18|1|545|2.5.2.1,2.5.2.2,1.9.4.1|graph|no|Squared-sine area by double-angle identity
12|Try Now 18|2|545|2.4.1.1,1.8.4.1,2.5.1.2,1.9.4.1|graph|no|Exact maximum location then trig area
12|Try Now 18|3|545|2.3.2.2,2.3.2.3,2.5.2.1,1.9.4.1|graph|no|Product-to-sum via supplied compound/double angle forms then exact first-region area
12|Example|19|547|2.5.3.1,2.5.3.2|graph|no|Two trapezium intervals, three ordinates and precision
12|Try Now|19|548|2.5.3.1,2.5.3.2|text|no|Two-interval estimates of rational or logarithmic integrand
12|Example|20|548|2.4.1.1,1.8.4.1,2.5.3.1,2.5.3.2,2.5.4.2|graph|no|Minimum, three-strip trapezia and overestimate via chord positions
12|Try Now|20|549|2.4.2.2,1.8.4.1,2.5.3.1,2.5.3.2,2.5.4.2|graph|no|Minimum of e^(2x)/x and chord-based overestimate
12|Example|21|549|2.5.3.1,2.5.3.2,2.5.4.2|graph|no|e^x cos x trapezia and underestimation from chords
12|Try Now 21|1|550|2.5.3.1,2.5.3.2,2.5.4.2|graph|no|Log-polynomial integrand estimate and explanation; adjacent terminology calls U-shaped concave and arch-shaped convex, opposite chosen standard convention
12|Try Now 21|2|550|2.4.2.1,1.8.4.1,2.5.3.1,2.5.3.2,2.5.4.2|graph|no|Maximum of xe^-x and underestimate; instruction(c) mis-refers to interval(a) rather than integral(b)
12|Example|22|551|2.5.3.1,2.5.3.2,2.5.4.2|graph|no|Trapezium area then rectangle complement reverses estimate direction
12|Try Now|22|551|2.5.3.1,2.5.3.2|graph|no|Two-interval estimate of radical trig integrand
13|Example|1|560|2.6.1.1,2.6.1.2|text|yes|Two-graph uniqueness and sign bracket
13|Try Now 1|1|560|2.6.1.1,2.6.1.2|text|yes|Three-root cubic or two-root radical equation; bracket specified roots
13|Try Now 1|2|560|2.6.1.1,2.6.1.2|text|yes|Three-root cubic or two-root radical equation; bracket specified roots
13|Try Now 1|3|560|2.6.1.1|text|yes|Logarithm/line graph count
13|Example|2|561|2.6.1.1,2.6.1.2|text|yes|Two exponential/line intersections and one specified sign bracket
13|Try Now 2|1|561|2.6.1.1,2.6.1.2|text|yes|Exponential, reciprocal/log, sine/reciprocal-square and base-two exponential graphical root count and bracket
13|Try Now 2|2|561|2.6.1.1,2.6.1.2|text|yes|Exponential, reciprocal/log, sine/reciprocal-square and base-two exponential graphical root count and bracket
13|Try Now 2|3|561|2.6.1.1,2.6.1.2|text|yes|Exponential, reciprocal/log, sine/reciprocal-square and base-two exponential graphical root count and bracket
13|Try Now 2|4|561|2.6.1.1,2.6.1.2|text|yes|Exponential, reciprocal/log, sine/reciprocal-square and base-two exponential graphical root count and bracket
13|Example|3|564|2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|no|Sign bracket then rational rearrangement coefficients, iterate with specified display precision; solution continues PDF565
13|Try Now|3|565|2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|no|Reciprocal-square/line root, bracket and square-root iteration
13|Example|4|565|2.6.2.1,2.6.3.1,2.6.4.1,2.6.4.2|text|no|Iteration then equation satisfied by limit and exact cube root
13|Try Now 4|1|566|2.6.2.1,2.6.3.1,2.6.4.1,2.6.4.2|text|no|Iterative sequences interpreted as algebraic limit equations
13|Try Now 4|2|566|2.6.2.1,2.6.3.1,2.6.4.1,2.6.4.2|text|no|Iterative sequences interpreted as algebraic limit equations
13|Try Now 4|3|566|2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|Positive quartic root, bracket and supplied cube-root rearrangement
13|Example|5|567|2.6.1.1,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|yes|Graphical uniqueness then log iteration; table heading says2dp but stem/final correctly3dp
13|Try Now 5|1|568|2.6.1.1,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|yes|Log/exponential root counts, brackets and iteration; item1 explicitly conditional on convergence
13|Try Now 5|2|568|2.6.1.1,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|yes|Log/exponential root counts, brackets and iteration; item1 explicitly conditional on convergence
13|Try Now 5|3|568|2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|no|Quartic bracket, supplied fourth-root rearrangement and iteration
13|Example|6|570|2.6.2.2|text|no|Convergent versus failed rearrangement; derivative convergence test is explanatory extension, not required under LIMIT08
13|Try Now 6|1|570|2.6.2.2|text|no|Compare successful/failed forms; open construction and derivative criterion are extensions. For 8227 retain recognition from supplied forms only, LIMIT08
13|Try Now 6|2|570|2.6.2.2|text|no|Compare successful/failed forms; open construction and derivative criterion are extensions. For 8227 retain recognition from supplied forms only, LIMIT08
13|Example|7|571|2.4.2.1,2.4.3.3,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|no|Specified exponential-product gradient leads to bracket/log iteration
13|Try Now 7|1|572|2.4.2.1,2.4.3.3,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|Specified gradient then fixed-point exponential iteration
13|Try Now 7|2|572|2.4.2.2,1.8.4.1,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|Quotient maximum location via iteration
13|Example|8|573|2.6.1.1,2.6.1.2,2.6.3.1,2.6.4.1,2.6.4.2|text|yes|Cosine/line uniqueness, sign bracket and limit equation of iteration
13|Try Now|8|574|2.3.1.2,2.6.1.1,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|text|yes|Cotangent/line uniqueness then principal inverse-tan iteration in radians
13|Example|9|577|1.5.2.3,2.6.1.2,2.6.3.2,2.6.4.1,2.6.4.2|diagram|no|Segment fraction of circle leads to trig fixed-point equation and checked rounding bracket
13|Try Now 9|1|578|1.5.2.3,2.6.3.2,2.6.4.1,2.6.4.2|diagram|no|Equal segment/triangle area then iteration and chord length
13|Try Now 9|2|578|2.5.1.2,1.9.4.1,2.6.3.2,2.6.4.1,2.6.4.2|graph|no|Equal rectangle/integral area then fixed-point iteration; larger source render confirms whole numerator (1-sin theta), no grouping defect
2|Try Now 33|1|82|1.2.3.2,1.2.3.3|text|no|Dam volume decays40percent annually; beginning-year volume, loss in nth year and first6 years; continues83
2|Try Now 33|2|83|1.2.3.2,1.2.3.3|text|no|Compound-interest deposit: distinguish initial1960term from33interest payments; first over500 in1993
2|Try Now 33|3|83|1.2.3.2,1.2.3.3|text|no|Increasing daily excavation areas form GP; round number of workdays upwards to16
2|Try Now 33|4|83|1.2.3.2,1.2.3.3|text|no|Daily walking distance reduces5percent; map sequence index to calendar date and total journey completion
2|Try Now 33|5|83|1.2.3.2,1.2.3.3|text|no|Email branching3recipients over five transmissions; count sum of generations, not only fifth generation
2|Try Now 33|6|83|1.2.3.1,1.2.3.3|text|no|Weekly race-training distances increase25km from200km; seventh distance and total first15 weeks
2|Try Now 33|7|83|1.2.3.1,1.2.3.3|text|no|Annual salary AP: distinguish sixth salary year from five elapsed increases; first10total696000
4|Try Now 16|1|179|1.6.2.1,1.6.2.2|graph|no|Recover trig coefficients from graph, or period/range/intersection symmetry
4|Try Now 16|2|179|1.6.2.1,1.6.2.2|graph|no|Recover trig coefficients from graph, or period/range/intersection symmetry
4|Try Now 16|3|179|1.6.2.1,1.6.2.2|graph|no|Recover trig coefficients from graph, or period/range/intersection symmetry
4|Try Now 55|1|220|1.3.2.2,1.3.3.2,1.3.5.1,1.6.4.1|text|yes|Restricted sine, inverse intercepts and inverse formula/domain/range
4|Try Now 55|2|220|1.6.2.3,1.6.6.1,1.3.3.2,1.6.4.1|text|yes|Double sine sketch/equation then greatest inverse branch bound
4|Try Now 55|3|220|1.6.6.1,1.6.2.3,1.3.3.1|text|yes|Compare squared-cosine root case and basic-cosine inverse/sketch case
9|Try Now 33|1|440|2.2.4.1,2.2.4.2|graph|no|Draw best-fit transformed line and recover exponential constants from plotted experimental points
9|Try Now 33|2|440|2.2.4.1,2.2.4.2|table|yes|Cell-growth exponential data and planetary power-law data, choose straight-line coordinates and fit
9|Try Now 33|3|440|2.2.4.1,2.2.4.2|table|yes|Cell-growth exponential data and planetary power-law data, choose straight-line coordinates and fit
3|Example|22|144|1.4.2.1,1.1.2.1,1.1.2.2,1.1.2.3|text|no|Line/parabola simultaneous intersections, known root, and tangency as repeated root; inline solution gives a=-1,P(2,5)
3|Try Now|22|144|1.4.2.1,1.1.2.1,1.1.2.2,1.1.2.3|text|no|Line/reciprocal-curve intersection parameter interval; then intersections and perpendicular bisector. Prior coordinate method is separated from AS intersection demand
1|Example|12|23|1.1.4.1,1.1.4.2,1.1.4.3|text|no|Biquadratic x^4-5x^2+4=0; substitute k=x^2 or factor directly; recover both signs, roots+-1,+-2
1|Try Now|12|24|1.1.4.1,1.1.4.2,1.1.4.3|text|no|Two biquadratics require quadratic substitution and recovery of both square-root signs
1|Example|13|24|1.1.4.1,1.1.4.2,1.1.4.3|text|no|10x+sqrt(x)-2=0 is quadratic in sqrt(x); reject negative substituted root before or after recovery; valid x=4/25
1|Try Now|13|24|1.1.4.1,1.1.4.2,1.1.4.3|text|no|Choose substitutions in sqrt(x),x^(1/3),3^x,x^3 or2x+1/x; recover original roots and filter inadmissible values; handwriting near(h) is not an authoritative answer
1|Example|14|27|1.1.2.1,1.1.2.2|text|no|Write x^2+8-x=2(x+6) in standard form; discriminant25 implies rational unequal real roots without solving
1|Try Now|14|27|1.1.2.1,1.1.2.2|text|no|Classify root nature from discriminant for six integer-coefficient quadratics; include zero,positive square,positive non-square and negative cases
1|Example|15|27|1.1.2.1,1.1.2.2,1.1.2.3|text|no|Equal roots of x^2+16x+p=0; impose discriminant0 to obtain p64
1|Try Now 15|1|28|1.1.2.1,1.1.2.2,1.1.2.3|text|no|Unknown constant or linear coefficient with two equal real roots; discriminant0, both signs of unknown linear coefficient may survive
1|Try Now 15|2|28|1.1.2.1,1.1.2.2,1.1.2.3|text|no|Repeated roots where parameter changes constant or linear/constant pair; equate discriminant0 and retain all parameter values
1|Example|16|28|1.1.2.1,1.1.2.2,1.1.2.3|text|no|Two real distinct roots of2x^2+5x-(3m+4)=0; discriminant>0 gives m>-19/8
1|Try Now 16|1|28|1.1.2.1,1.1.2.2,1.1.2.3|text|no|First collect terms in3x^2-4x=2x(x+1)+2m; discriminant>0 gives parameter interval
1|Try Now 16|2|28|1.1.2.1,1.1.2.2,1.1.2.3|text|no|Collect constant terms before discriminant in x^2+4x-2p=-7; distinguish strict real-distinct condition
1|Try Now 16|3|28|1.1.2.1,1.1.2.2,1.1.2.3|text|no|Parameter-dependent leading coefficient(2-m). Discriminant condition alone is insufficient: exclude m=2 where equation is linear
1|Example|17|28|1.1.2.1,1.1.2.2,1.1.2.3|text|no|No-real-root condition x^2-2kx+k^2+5k-6=0 reduces to k>6/5; sign reverses on division by negative number
1|Try Now|17|29|1.1.2.1,1.1.2.2,1.1.2.3|text|no|No-real-root parameter ranges with parameter appearing in constant,leading or multiple coefficients; exclude degenerate linear cases where relevant
1|Example|19|30|1.1.2.1,1.1.2.2|text|no|Universal discriminant proof for(p+1)x^2+(2p+3)x+2=0,p!=-1. Printed rational-for-all-real-p conclusion is false; hold original proof exemplar
1|Try Now|19|30|1.1.2.1,1.1.2.2|text|no|Prove rational real roots for integer parameters; distinguish perfect-square discriminant from coefficient rationality and handle p0 linear case in(b)
1|Example|20|30|1.1.2.1,1.1.2.2|text|no|Universal real-root proof with positive discriminant12+4k^2; k=-1 is linear and requires separate argument
1|Try Now|20|30|1.1.2.1,1.1.2.2|text|no|Universal real-root proofs for integer coefficients; consider q=-1 linear branch in(a), and repeated-root possibility in(b)
1|Try Now 21|1|32|1.1.1.1,1.1.1.2,1.1.1.3|text|yes|Complete square for x^2+3x-4, identify minimum vertex, then sketch with intercepts
1|Try Now 21|2|32|1.1.1.1,1.1.1.2,1.1.1.3|text|yes|Complete square for x^2-6x+8, identify minimum vertex, then sketch with intercepts
1|Example|22|32|1.1.1.1,1.1.1.2|text|no|Non-monic quadratic5x^2+8x-2; complete square to obtain minimum-26/5 at x=-4/5
1|Try Now|22|32|1.1.1.1,1.1.1.2|text|no|Four non-monic quadratics; express vertex form and obtain extremal ordinate and its input, without requiring a sketch
1|Example|23|33|1.1.1.1,1.1.1.2,1.1.1.3|text|yes|Negative-leading quadratic8x-x^2; maximum(4,16) and intercepts0,8; printed side caption has wrong vertex sign
1|Try Now 23|1|33|1.1.1.1,1.1.1.2,1.1.1.3|text|yes|Negative-leading quadratic6x-x^2; complete square, maximum vertex and graph
1|Try Now 23|2|33|1.1.1.1,1.1.1.2,1.1.1.3|text|yes|Non-monic2x^2-3x; complete square, minimum vertex and graph
1|Try Now|26|36|1.1.5.1|text|no|Reconstruct two parabolas from their turning point plus a point, choosing correct coefficient from origin or y-intercept
1|Example|27|36|1.1.5.1|graph|no|Read vertices and one further point from three given parabola graphs; choose root form or vertex form; inline solutions individually displayed
1|Example|30|39|1.4.2.1|text|no|Line x+2y=9 with xy+18=0; substitute, solve quadratic, and recover paired coordinates(-3,6),(12,-1.5)
1|Try Now 30|1|39|1.4.2.1|text|no|Line y+2x=11 and hyperbola xy=15; recover paired coordinates rather than just independent roots
1|Try Now 30|2|39|1.4.2.1|text|no|Line x+y=3 and parabola y=2x^2-8x+9; only intersection x-coordinates requested
1|Try Now 30|3|39|1.4.2.1|text|no|Two linear/nonlinear simultaneous systems; eliminate one variable and recover corresponding values
1|Example|31|40|1.4.2.2,1.1.2.1,1.1.2.3|text|no|Tangent line y=2x+k to sideways parabola y^2=4x; repeated intersection root yields k=1/2
1|Try Now 31|1|40|1.4.2.2,1.1.2.1,1.1.2.3|text|no|Slope and parabola constant both depend on k; tangent condition may have more than one parameter value
1|Try Now 31|2|40|1.4.2.2,1.1.2.1,1.1.2.3|text|no|Tangent line2y+x=p to sideways parabola y^2+2x=13; eliminate x or y consistently
1|Try Now 31|3|41|1.1.6.1,1.1.6.2,1.4.2.2,1.1.2.3|text|no|Curve2x^2-6x+5: solve y>13, then tangent y=2x+k; this numbered question continues the set on the next page
1|Example|32|41|1.4.2.1,1.1.2.1,1.1.2.2,1.1.2.3,1.1.6.1,1.1.6.2|text|no|Two distinct intersections y=px+1 and y=x^2+2x+5; discriminant inequality yields p<-2 or p>6; solution graph is method evidence, not a given
1|Try Now 32|1|41|1.4.2.1,1.1.2.1,1.1.2.2,1.1.2.3|text|no|Parameter line2y+x=p and hyperbola xy=6; strict discriminant condition for two intersections
1|Try Now 32|2|41|1.4.2.1,1.1.2.1,1.1.2.2,1.1.2.3|text|no|Parameter appears in both line y=2x-k and parabola y=x^2+kx-2; two distinct intersections
1|Try Now 32|3|42|1.4.2.1,1.1.2.1,1.1.2.2,1.1.2.3|text|no|Hyperbola y=-2/x and parameter line y=qx+3q; two distinct intersections, respecting x!=0
1|Try Now 32|4|42|1.4.2.1,1.4.2.2,1.1.2.1,1.1.2.3|text|no|Line y=x+2 meets circle y^2+(x+k)^2=2; includes tangent or two-point intersection, so discriminant>=0 rather than>0
1|Example|33|42|1.4.2.1,1.1.2.1,1.1.2.2,1.1.2.3|text|no|No intersections between y=2x-7 and y=x^2-4x+c; strict negative discriminant yields c>2
1|Try Now 33|1|42|1.4.2.1,1.1.2.1,1.1.2.2,1.1.2.3|text|no|No intersections y=4x+k and y=x^2; parameter enters constant term only
1|Try Now 33|2|42|1.4.2.1,1.1.2.1,1.1.2.2,1.1.2.3|text|no|No intersections y=kx^2+1 and y=kx, explicitly k!=0; discriminant is quadratic in k
1|Try Now 33|3|42|1.4.2.1,1.1.2.1,1.1.2.2,1.1.2.3|text|no|No intersections y=kx^2-3x and y=x-k; inspect the k0 degeneracy rather than treating every coefficient as nonzero
1|Try Now 33|4|42|1.4.2.1,1.1.2.1,1.1.2.2,1.1.2.3|text|no|No intersections hyperbola xy=3 and line y=-3x+k; paired-coordinate relation becomes quadratic
2|Try Now 2|3|55|1.2.2.1,1.2.2.2|text|no|Classify symbolic progressions; x and y denominators must be nonzero. Constant-sequence boundary in(b) can fit both AP and GP; do not force exclusive classification without parameter restriction
2|Try Now 2|4|55|1.2.3.1,1.2.3.2,2.2.1.2|text|no|log2,log(2^2),log(2^p): find p for AP and then GP using logarithmic power law; p3 and4 respectively
2|Example|3|55|1.2.3.1|text|no|AP terms6 and13 from3,8,13;28 and63
2|Example|4|56|1.2.3.1|text|no|AP fractional negative difference; tenth term-20.5 and general term4.5-2.5n
2|Example|5|56|1.2.3.1|text|no|Number of AP terms from first,last,difference; n11
2|Example|6|57|1.2.3.1|text|no|First AP term strictly above600; solve integer-index inequality, n87
2|Example|7|57|1.2.3.1|text|no|Recover a,d from eighth and sixteenth terms, then list initial terms; a13,d-3
2|Example|8|58|1.2.3.1|text|no|Multiplicative relation between AP terms plus another known term; a2,d4,T15=58
2|Example|9|60|1.2.3.2|text|no|GP with negative ratio-1/3; compute distant odd/even terms preserving signs
2|Example|10|60|1.2.3.2|text|no|Alternating GP ratio-1/2; compute ninth and general term
2|Example|11|61|1.2.3.2|text|no|Symbolic endpoint GP with ratio11/y^2; inferred n5 only unique for y!=0 and y^2!=11; retain constant-ratio1 boundary
2|Example|12|62|1.2.3.2|text|no|First decreasing positive GP term below0.04; negative logarithm reverses inequality, smallest integer index13
2|Example|13|63|1.2.3.2|text|no|Known fourth and seventh terms determine negative ratio-2 via odd root; a3 and initial terms
2|Example|14|65|1.2.3.1|text|no|First20 AP terms4+7+10; sum650
2|Example|15|66|1.2.3.1|text|no|AP endpoint20.5 is21st term, not20th; count then sum220.5
2|Example|16|66|1.2.3.1|text|no|AP sum585 gives quadratic in term count; retain positive integer13, reject negative root-18
2|Example|17|67|1.2.3.1|text|no|First6 and next6 AP sums are separate blocks; convert to S6,S12, then solve a3,d2.5
2|Try Now 3|1|56|1.2.3.1|text|no|AP25th term with negative difference
2|Try Now 3|2|56|1.2.3.1|text|no|Two distant AP terms with positive difference
2|Try Now 3|3|56|1.2.3.1|text|no|Specified fifth and twelfth terms of supplied AP
2|Try Now|4|56|1.2.3.1|text|no|Six APs: nineteenth and general terms; include fractional/decimal/negative differences
2|Try Now|5|56|1.2.3.1|text|no|Count terms from AP endpoints; symbolic-a branch needs a!=0 for unique count
2|Try Now 6|1|57|1.2.3.1|text|no|First increasing AP term greater80
2|Try Now 6|2|57|1.2.3.1|text|no|First increasing AP term greater700
2|Try Now 6|3|57|1.2.3.1|text|no|First decreasing fractional AP term below-200
2|Try Now 7|1|58|1.2.3.1|text|no|Recover a,d from19th and4th terms, then list first3
2|Try Now 7|2|58|1.2.3.1|text|no|Recover negative fractional d from4th and10th terms
2|Try Now 7|3|58|1.2.3.1|text|no|Recover a,d from8th and16th terms, then count through supplied last term
2|Try Now 8|1|58|1.2.3.1|text|no|Second AP term seven times third, plus fifth term; solve a,d then T10
2|Try Now 8|2|59|1.2.3.1|text|no|Known sixth term and excess of fifteenth over tenth; solve d,a then first3
2|Try Now 8|3|59|1.2.3.1|text|no|Sums of pairs of AP terms give two equations for a,d
2|Try Now 8|4|59|1.2.3.1|text|no|Two general-term expressions, numeric and symbolic arithmetic progressions
2|Try Now 8|5|59|1.2.3.1|text|no|Which term equals82, then decide whether124 is an integer-index AP member
2|Try Now 8|6|59|1.2.3.1|text|no|Count positive terms in decreasing AP, then test membership of-310
2|Try Now 8|7|59|1.2.3.1|text|no|Recover d from first and21st terms, then express Tn
2|Try Now 8|8|59|1.2.3.1|text|no|Two finite AP endpoint lists; determine each term count
2|Try Now 8|9|59|1.2.3.1|text|no|AP begins x,3x and has fifteenth term x^2; zero-x case makes an all-zero sequence and must be treated explicitly
2|Try Now 8|10|59|1.2.3.1|text|no|First and thirteenth AP terms expressed using same y; recover common difference
2|Try Now 8|11|59|1.2.3.1|text|no|Known48th AP term and d; recover first term
2|Try Now 8|12|59|1.2.3.1|text|no|Known8th and53rd AP terms; recover a,d
2|Try Now|9|60|1.2.3.2|text|no|Three GPs including alternating signs and fractional ratios; compute specified distant terms
2|Try Now|10|61|1.2.3.2|text|no|Seventh and general GP terms; symbolic a,b branch has nonzero denominator and ratio-identifiability conditions
2|Try Now 11|1|61|1.2.3.2|text|no|Finite GP endpoints: positive integer and alternating fractional ratio
2|Try Now 11|2|61|1.2.3.2|text|no|Find index of458752 in GP7,14,28
2|Try Now 11|3|61|1.2.3.2|text|no|Find index of3/4 in halving GP384,192,96
2|Try Now 11|4|61|1.2.3.2|text|no|Find index of mixed-fraction endpoint in decreasing GP54,36,24
2|Try Now|12|62|1.2.3.2|text|no|Four first-term threshold problems; increasing/decreasing positive ratios, strict inequalities and integer index
2|Try Now 13|1|63|1.2.3.2|text|no|Sixth and third GP terms give a positive ratio via odd root
2|Try Now 13|2|63|1.2.3.2|text|no|Symbolic fourth and seventh GP terms; zero parameter makes ratio unidentifiable
2|Try Now 13|3|63|1.2.3.2|text|no|Three consecutive GP terms involve x; quadratic gives two ratios and first terms
2|Try Now 13|4|64|1.2.3.2|text|no|Sums of first2 and4th/5th GP terms; use ratio-power relation
2|Try Now 13|5|64|1.2.3.2|text|no|Find initial3 GP terms from a/r, a later term/r, general term, or exact surd data
2|Try Now 13|6|64|1.2.3.2|text|no|Locate1024 in doubling GP
2|Try Now 13|7|64|1.2.3.2|text|no|Third and seventh GP terms give an even root; retain both possible ratio signs
2|Try Now 13|8|64|1.2.3.2|text|no|First3 GP terms p-4,p,p+12; solve parameter and recover terms
2|Try Now 13|9|64|1.2.3.2|text|no|Eleventh term with alternating ratio-1/2
2|Try Now 13|10|64|1.2.3.2|text|no|Sixth and ninth GP terms determine negative ratio via odd root
2|Try Now 13|11|64|1.2.3.2|text|no|First2 and last GP terms determine number of terms
2|Try Now 14|1|65|1.2.3.1|text|no|Sum first30 AP terms for six numeric series including negative and fractional terms
2|Try Now 14|2|65|1.2.3.1|text|no|Recognise symbolic AP across terms13x-2y,10x,7x+2y; sum first23
2|Try Now 14|3|65|1.2.3.1|text|no|Recognise reciprocal-denominator pattern as AP multiples x/60; sum first22
2|Try Now|15|66|1.2.3.1|text|no|Four endpoint arithmetic series; count terms before applying sum, including negative last terms
2|Try Now 16|1|67|1.2.3.1|text|no|Positive AP sum gives one positive integer term count
2|Try Now 16|2|67|1.2.3.1|text|no|AP starts negative then increases; sum-17 is achieved for n1 and n17, so both positive integer roots matter
2|Try Now 16|3|67|1.2.3.1|text|no|Decreasing AP sum gives two positive algebraic roots but only n7 is an integer
2|Try Now 17|1|67|1.2.3.1|text|no|First10 and next10 AP sums; convert next-block sum into S20 before solving a,d
2|Try Now 17|2|68|1.2.3.1|text|no|Known T5+T7 and S15; infer a4,d3 then sum next15=1050, not merely parameters
2|Try Now 17|3|68|1.2.3.1|text|no|AP first-24,last72,sum600; recover count25 and difference4
2|Example|18|68|1.2.3.1|text|no|Last3 sum five times first3 in23-term AP; recover d3 then S17=612; substitution typo does not change result
2|Try Now 18|1|68|1.2.3.1|text|no|First5 plus last5 in19-term AP, endpoint52; express last5 then recover a10,d7/3
2|Try Now 18|2|68|1.2.3.1|text|no|Last3 sum triple first3 in101-term AP; find last48 by subtracting S53 from S101
2|Example|19|69|1.2.3.1|text|no|Separate negative and positive AP term counts, then sum only positive terms; check no zero boundary
2|Try Now 19|1|69|1.2.3.1|text|no|Increasing AP begins negative; least term count making partial sum positive
2|Try Now 19|2|69|1.2.3.1|text|no|Increasing AP begins negative; greatest integer term count satisfying sum bound
2|Try Now 19|3|69|1.2.3.1|text|no|Sum AP from first,last,count
2|Try Now 19|4|69|1.2.3.1|text|no|One term and partial sum determine a,d
2|Try Now 19|5|69|1.2.3.1|text|no|Sum second block of10, distinguishing it from first20
2|Try Now 19|6|70|1.2.3.1|text|no|Known T15 and S9; determine T20
2|Try Now 19|7|70|1.2.3.1|text|no|Known first term,S8,whole sum; recover positive count and last term
2|Example|20|70|1.2.3.2|text|no|Alternating finite GP with ratio-1/2; first10sum341/64; printed S15 label is wrong
2|Try Now 20|1|70|1.2.3.2|text|no|Three finite GP sums including negative ratio and decreasing fractions
2|Try Now 20|2|71|1.2.3.2|text|no|Evaluate S5,S6 for alternating GP then obtain sixth term by subtraction
2|Example|21|71|1.2.3.2|text|no|Finite halving GP with last1/32; count10 then sum31 31/32
2|Try Now|21|71|1.2.3.2|text|no|Four finite endpoint GPs; find count before sum and preserve negative ratios
2|Example|22|71|1.2.3.2|text|no|GP sum605 gives positive integer count5
2|Try Now|22|72|1.2.3.2|text|no|GP sum315 gives integer count6
2|Example|23|72|1.2.3.2|text|no|Least count giving GP partial sum above2.65; reversed logarithmic inequality
2|Try Now 23|1|72|1.2.3.2|text|no|Express GP partial sum then least count to exceed20
2|Try Now 23|2|72|1.2.3.2|text|no|Greatest integer term count giving sum at most125
2|Try Now 23|3|72|1.2.3.2|text|no|Last term strictly below5000 determines count22, then sum first22 to3sf
2|Example|24|73|1.2.3.2|text|no|Recover positive ratio from relation between terms; worked division requires a!=0
2|Try Now 24|1|73|1.2.3.2|text|no|Positive ratio from T2+T3 relation; first-term-zero branch needs explicit handling
2|Try Now 24|2|73|1.2.3.2|text|no|Count GP terms from partial sum510
2|Try Now 24|3|73|1.2.3.2|text|no|Known first/fourth terms determine negative ratio; sum first10
2|Try Now 24|4|73|1.2.3.1,1.2.3.2|text|no|AP partial sum equals first6 of alternating GP; equate sums to find count
2|Try Now 24|5|73|1.2.3.2|text|no|First two GP terms give ratio, then minimum count to exceed sum bound
2|Try Now 24|6|73|1.2.3.2|text|no|Known second and fifth terms determine positive ratio, first term, S15 to3sf
2|Example|25|74|1.2.4.1,1.2.4.2|text|no|Interpret finite sigma bounds1..4 and linear summand; enumerate and evaluate38
2|Try Now 25|1|74|1.2.4.1,1.2.4.2|text|no|Expand and evaluate three finite sigma sums
2|Try Now 25|2|74|1.2.4.1,1.2.4.2|text|no|Evaluate finite sigma sums including quadratic and alternating expressions; no unsupported general sum-of-squares formula needed
2|Example|26|75|1.2.4.1,1.2.3.1,1.2.4.2|text|no|Shifted lower sigma index2:19 terms, AP sum-228
2|Try Now|26|75|1.2.4.1,1.2.3.1,1.2.3.2,1.2.4.2|text|no|Six finite sigma sums with shifted bounds, AP and GP, including symbolic parameter; demands vary by letter
2|Example|27|75|1.2.4.1|text|no|Express finite AP and alternating GP in sigma notation with correct bounds; evaluation not requested
2|Try Now 27|1|76|1.2.4.1|text|no|Express two listed finite AP/GP sums using sigma notation
2|Try Now 27|2|76|1.2.4.1|text|no|Construct summand and bounds for three finite AP/GP sums, including specified count and endpoint
2|Example|28|76|1.2.4.1,1.2.3.2,1.2.4.2|text|no|Sigma GP sum378 determines upper index6
2|Try Now|28|76|1.2.4.1,1.2.3.1,1.2.3.2,1.2.4.2|text|no|Ten sigma equations or inequalities; determine upper index or parameter, respecting strictness and count
'''


YM += r'''
2|Example|34|84|1.2.5.2|text|no|Recurring decimals as infinite GP plus nonrecurring offset; preserve repeating-block length
2|Try Now 34|1|84|1.2.5.2|text|no|Three purely recurring decimals represented as GP sums and simplified fractions
2|Try Now 34|2|84|1.2.5.2|text|no|Four recurring decimals with nonrecurring prefix; separate prefix from infinite repeating GP
2|Example|35|85|1.2.3.2,1.2.3.3|text|no|Annual compound-interest deposits form finite GP; source assumes each payment receives a full first year of interest
2|Try Now 35|1|85|1.2.3.2,1.2.3.3|text|no|Ten annual deposits with8percent interest; first3accumulated terms and total, payment timing must be explicit
2|Try Now 35|2|85|1.2.3.2,1.2.3.3|text|no|Annual deposits1994to2012 inclusive; source uses19full-year accumulation terms
2|Try Now 35|3|85|1.2.3.1,1.2.3.2,1.2.3.3|text|no|Compare compound percentage growth with fixed annual addition; thresholds and eventual exceedance; continues86
2|Example|36|86|1.2.3.2,1.2.5.2,1.2.3.3|text|no|Bouncing ball: initial drop plus paired upward/downward GP distances, finite third-impact and limiting total
2|Try Now|36|86|1.2.5.2,1.2.3.3|text|no|Prove bouncing-ball total cannot exceed19m; initial1m plus paired infinite rebound distances
2|Example|37|90|1.2.1.1|text|no|Positive-integer binomial expansions from Pascal coefficients, powers8and10
2|Try Now 37|1|90|1.2.1.1|text|no|Two symbolic binomial expansions; final observation on exponent sums is instructional enrichment, coefficient properties not required by syllabus
2|Try Now 37|2|90|1.2.1.1|text|no|Expand(1+b)^6 then deduce negative-sign variant by substitution
2|Try Now 37|3|90|1.2.1.1|text|no|Expand(a-1)^8 with alternating signs
2|Example|38|91|1.2.1.1|text|no|Three positive-integer expansions with scaled and fractional binomial terms
2|Try Now|38|91|1.2.1.1|text|no|Six scaled binomial expansions, including reciprocal symbolic terms
2|Example|39|91|1.2.1.1,1.2.1.2,1.2.1.3|text|no|Truncate expansion through square term then combine with another factor to extract square coefficient
2|Try Now 39|1|92|1.2.1.1,1.2.1.2,1.2.1.3|text|no|Expand through y^2 and combine with linear factor to extract coefficient
2|Try Now 39|2|92|1.2.1.1,1.2.1.2,1.2.1.3|text|no|Expand through a^2 and combine with squared factor to extract coefficient
2|Try Now 39|3|92|1.2.1.1,1.2.1.3|text|no|Two expansions truncated through b^2 then their product
2|Try Now 39|4|92|1.2.1.1,1.2.1.2,1.2.1.3|text|no|Truncated expansion and y coefficient of product with squared factor
2|Example|40|92|1.2.1.1,1.2.1.3|text|no|Treat quadratic inner expression as binomial component; collect terms only through x^3
2|Try Now 40|1|92|1.2.1.1,1.2.1.3|text|no|Expand(1+y-2y^2)^6 through cubic term
2|Try Now 40|2|92|1.2.1.1,1.2.1.3|text|no|Two quadratic-inner positive-integer expansions truncated through cubic
2|Example|41|93||text|no|Factorial notation and cancellation support; does not itself ask binomial expansion or coefficient extraction
2|Try Now|41|93||text|no|Evaluate three factorial expressions; prerequisite notation support, not a full expansion demand
2|Example|42|94||text|no|Evaluate numerical and symbolic n-choose-r notation; prerequisite for expansion, no direct expansion demand claimed
2|Try Now|42|94||text|no|Evaluate four n-choose-r expressions; keep support distinct from full binomial demand
2|Example|43|96|1.2.1.1|text|no|First4terms of(a+2b)^8 in descending a powers
2|Try Now|43|97|1.2.1.1|text|no|Two expansions to first4terms in descending a powers
2|Example|44|97|1.2.1.1,1.2.1.3|text|no|First4terms for linear and quadratic inner expressions; reuse first expansion by substitution
2|Try Now|44|97|1.2.1.1,1.2.1.3|text|no|First4terms for(1-2x)^10 then quadratic-inner variant
2|Example|45|97|1.2.1.1|text|no|Complete fourth-power two-variable binomial expansion with exact fractional coefficients
2|Try Now|45|98|1.2.1.1|text|no|Four scaled two-variable positive-integer expansions
2|Example|46|98|1.2.1.2|text|no|Choose indexed term, constant term and x^6 term by matching exponent; negative reciprocal term controls sign
2|Try Now 46|1|99|1.2.1.2|text|no|Choose fourth and constant terms in a-based reciprocal binomial; source says independent of x incorrectly
2|Try Now 46|2|99|1.2.1.2|text|no|Choose sixth term, constant term and x^6 term with non-monotonic exponent order; source descending-powers phrase needs clarification
2|Example|47|99|1.2.1.1,1.2.1.2,1.2.1.3|text|no|First3terms of scaled binomial then quadratic product coefficient-4912
2|Try Now 47|1|99|1.2.1.1,1.2.1.2,1.2.1.3|text|no|First4terms involve only even y powers; reciprocal prefactor changes target exponent selection
2|Try Now 47|2|99|1.2.1.1,1.2.1.2,1.2.1.3|text|no|Expand two fourth powers then extract cubic coefficient from their product
2|Example|48|100|1.2.1.2,1.2.1.3|text|no|Find neighbouring coefficients then combine with linear factor for cubic coefficient560
2|Try Now 48|1|100|1.2.1.2|text|no|Find x coefficient in reciprocal binomial using exponent equation
2|Try Now 48|2|100|1.2.1.2|text|no|Find x^9 coefficient in reciprocal binomial
2|Try Now 48|3|100|1.2.1.2,1.2.1.3|text|no|Find x^2,x^3 coefficients then unknown factor parameter from absence of cubic term
2|Try Now 48|4|100|1.2.1.2,1.2.1.3|text|no|Extract x^2 coefficient after multiplying reciprocal-binomial expansion by1+x^2
2|Try Now 48|5|100|1.2.1.2,1.2.1.3|text|no|Equal adjacent coefficients determine nonzero scale parameter
2|Example|49|101|1.2.1.2,1.2.1.3|text|no|Known linear coefficient of product determines exponent n6 then square coefficient21/4
2|Try Now 49|1|101|1.2.1.2,1.2.1.3|text|no|Constant and linear coefficients determine scale a and positive integer n, then square coefficient q
2|Try Now 49|2|101|1.2.1.2,1.2.1.3|text|no|Signed product coefficient conditions determine a,n,p
2|Try Now 49|3|101|1.2.1.2,1.2.1.3|text|no|Known linear coefficient and symbolic square coefficient determine k,n
'''

YM += r'''
4|Example|11|173|1.6.2.1|text|no|Amplitude, period in degrees/radians, range extrema and intercept for sine/cosine/tangent transformations; tangent has no amplitude/extrema
4|Try Now|11|173|1.6.2.1|text|no|Three transformed trig formulae: determine extrema, amplitude, periods and intercept; no given graph to read
4|Example|12|174|1.6.2.1,1.6.2.3|text|yes|Determine features of3cos2x-1 then sketch; part(c) prints a different formula from the worked graph
4|Try Now|17|181|1.6.3.1|text|no|Exact expressions from30,45,60degree ratios; rationalise final denominator without calculator
4|Example|21|185||text|no|Recover angle from supplied reference angle, quadrant and interval, degrees or radians; supporting quadrant reasoning, not a whole bounded-equation demand
4|Try Now|21|185||text|no|Three reference-angle/quadrant-to-angle conversions, including negative rotation; prerequisite support
4|Example|22|187||text|no|Rewrite arbitrary obtuse/reflex trig arguments as ratios of acute reference angles; prerequisite quadrant identities
4|Try Now|22|187||text|no|Rewrite150,250,330degree ratios using same function of acute reference angle; supportive quadrant reasoning
4|Example|23|187||text|no|Use known sine and symmetry to evaluate related-angle ratios; adjacent radians table contains sign defects; supporting symmetry evaluation, not an equation-transformation coverage claim
4|Try Now 23|1|187||text|no|Known tangent determines three related-angle values using symmetry; supporting symmetry evaluation, not an equation-transformation coverage claim
4|Try Now 23|2|187||text|no|Known cosine determines values at pi-theta,pi+theta,2pi-theta; supporting symmetry evaluation, not an equation-transformation coverage claim
4|Try Now 23|3|187||text|no|Known sine determines three related-angle values; do not copy incorrect adjacent table; supporting symmetry evaluation, not an equation-transformation coverage claim
4|Try Now 26|1|190|2.3.2.1|text|no|Given cos50=a, derive six related ratios including complementary angles, signs and square-root branch
4|Try Now 26|2|190|2.3.2.1,2.3.1.1|text|no|Given cosine of acute x, derive sine,tangent and complementary tangent in terms of p
4|Example|27|190||text|no|Reduce negative degree/radian arguments to basic reference angles; prerequisite quadrant reasoning, with instructional solution diagrams
4|Try Now|27|190||text|no|Four negative or positive angles: express sine,cosine,tangent via reference-angle ratios; no exact evaluation requested
4|Try Now|28|192|2.3.1.1|text|no|Determine six trig ratios from point coordinates in all four quadrants, signed surds included
4|Example|29|192|2.3.1.1,2.3.2.1|text|no|Given reciprocal sine equation, retain both possible quadrants for tangent; use quotient and Pythagorean identities without calculator
4|Try Now 29|1|193|2.3.1.1,2.3.2.1|text|no|Known sine and obtuse angle; exact cosine, reciprocal and quotient comparisons
4|Try Now 29|2|193|2.3.1.1,2.3.2.1|text|no|Known tangent with broad interval; squared reciprocal ratios remove quadrant-sign ambiguity
4|Try Now 29|3|193|2.3.2.1|text|no|Given sine and full-radian interval, determine both possible3tan beta values without calculator
4|Try Now 29|4|193|2.3.1.1,2.3.2.1|text|no|Two signed ratios and quadrant intervals; evaluate mixed cosecant-square/secant expression
4|Example|30|194|2.3.2.1,2.3.1.1|text|no|Given tangent of acute radian angle, derive complementary/related tangent and sine in parameter k
4|Try Now|30|194|2.3.2.1|text|no|Obtuse radian angle with sine q; choose negative cosine and tangent, then related-angle sine values
4|Example|31|196|1.6.5.1|text|no|Prove squared sine-plus-cosine identity by expansion and basic Pythagorean identity
4|Try Now|31|197|1.6.5.1|text|no|Prove squared sine-minus-cosine identity; action is proof, not numerical equation solving
4|Example|32|197|1.6.5.1|text|no|Prove cubic identity by expanding, grouping and substituting1-sin^2 or1-cos^2
4|Try Now|32|197|1.6.5.1|text|no|Simplify quotient using1-sin^2=cos^2, preserving common domain
4|Example|33|197|1.6.5.1,2.3.1.1|text|no|Prove sum-of-quotients equals2cosecant using common denominator and factor cancellation
4|Try Now|33|198|1.6.5.1,2.3.1.1|text|no|Three quotient identities; common denominators and Pythagorean substitution, respect zeros excluded by original expressions
4|Example|34|198|1.6.5.1,2.3.1.1|text|no|Show reciprocal-sum quotient equals cosecant; factor after converting to sine/cosine
4|Try Now|34|198|1.6.5.1,2.3.1.1|text|no|Three reciprocal quotient identities; transform one side or both to common expression without assuming target
4|Example|35|199|1.6.5.1,2.3.1.1|text|no|Square of reciprocal difference; Pythagorean factor cancellation to half-angle-style quotient without requiring half-angle formula
4|Try Now|35|199|1.6.5.1,2.3.1.1,2.3.2.1|text|no|Seven proof identities using reciprocal,quotient and squared identities; choose strategy by form, no new seven recipe count assumed
4|Example|36|200|1.6.5.1|text|no|Rationalise trigonometric numerator with conjugate1+sin beta to prove quotient identity
4|Try Now|36|200|1.6.5.1,2.3.1.1,2.3.2.1|text|no|Six proof identities with conjugate,quotient,reciprocal and squared identities; common-domain exclusions retained
4|Example|37|201|1.6.5.1,2.3.2.1|text|no|Simplify both sides separately to cos^2-sin^2; legitimate common-expression proof rather than assume equality
4|Try Now|37|201|1.6.5.1,2.3.1.1,2.3.2.1|text|no|Eight proof identities with quartic powers and reciprocal relationships; handwritten answer in(b) is not authoritative
4|Example|38|202|1.6.6.1,1.6.6.2|text|no|Solve sine=-1/2 over full turn; graph method and reference-angle method are both illustrated
'''

YM += r'''
4|Try Now|38|203|1.6.3.1,1.6.6.1,1.6.6.2|text|no|Twelve bounded degree equations; exact special ratios in(a)-(c), numerical roots to1dp otherwise, strict lower endpoint
4|Example|39|203|2.3.1.1,1.6.6.1,1.6.6.2|text|no|Reciprocal secant equation over half turn: only first-quadrant root survives interval
4|Try Now|39|203|2.3.1.1,1.6.6.1,1.6.6.2|text|no|Six reciprocal trig equations on90<=x<=360degrees, retain every valid branch and endpoint
4|Example|40|204|1.6.6.1,1.6.6.2|text|no|Rearrange tangent equation with surd coefficient; radians, two roots,3sf
4|Try Now|40|204|2.3.1.1,1.6.6.1,1.6.6.2|text|no|Six full-turn radian equations, basic and reciprocal functions; calculator mode and all roots matter
4|Example|41|204|1.6.3.1,1.6.6.1,1.6.6.2|text|no|cos^2y=1/4: retain both square-root signs and all four degree solutions
4|Try Now 41|1|205|1.6.6.1,1.6.6.2|text|no|Squared cosine equation gives four bounded-degree roots; do not drop negative square root
4|Try Now 41|2|205|2.3.1.1,1.6.6.1,1.6.6.2|text|no|Squared cosecant equation over0..pi; reciprocal transformation and interval restriction
4|Example|42|205|1.6.6.1,1.6.6.2|text|no|Sine-positive equation with negative-radian domain; choose coterminal negative angles
4|Try Now 42|1|205|1.6.6.1,1.6.6.2|text|no|Cosine equation on negative full-radian interval
4|Try Now 42|2|205|1.6.6.1,1.6.6.2|text|no|Tangent equation on negative half-turn degrees
4|Try Now 42|3|205|1.6.6.1,1.6.6.2|text|no|Cosine equation on asymmetric negative-degree interval
4|Try Now 42|4|205|1.6.6.1,1.6.6.2|text|no|Cosine and tangent equations on centred radian interval-pi..pi
4|Example|43|206|1.6.3.1,1.6.6.1,1.6.6.2|text|no|Scale angle domain before solving sin2theta and sintheta/2; four roots versus two roots
4|Try Now|43|207|1.6.6.1,1.6.6.2|text|no|Four degree equations with doubled or halved arguments; interval transforms with argument
4|Example|44|207|1.6.3.1,1.6.6.1,1.6.6.2|text|no|Exact cosine double-argument equation over full radians; two argument revolutions and four roots
4|Try Now|44|207|2.3.1.1,1.6.6.1,1.6.6.2|text|no|Four radian equations with double,triple or half argument, including cotangent and sign-sensitive half-angle branches
4|Example|45|208|1.6.6.1,1.6.6.2|text|no|Scaled and shifted tangent argument; transform bounds to-78..642degrees before finding four original-variable roots
4|Try Now 45|1|208|2.3.1.1,1.6.6.1,1.6.6.2|text|no|Four degree equations with scaled/shifted arguments, reciprocal functions and squared secant
4|Try Now 45|2|208|1.6.3.1,1.6.6.1,1.6.6.2|text|no|Exact shifted double-angle sine equation over two degree turns
4|Example|46|209|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Factor sinx cosx=cos^2x, keeping cosx0 branch rather than dividing away roots
4|Try Now 46|1|209|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Factor common cosine without discarding its zero roots
4|Try Now 46|2|209|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Tangent/sine equation: preserve sin0 roots and exclude cosine0 poles
4|Try Now 46|3|209|1.6.6.1,1.6.6.2|text|no|Factor tan^2theta-tantheta; include both full-radian interval endpoints where defined
4|Try Now 46|4|209|1.6.6.1,1.6.6.2|text|no|Factor cosine; sine3 is infeasible so only cosine-zero branch survives
4|Try Now 46|5|209|1.6.6.1,1.6.6.2|graph|no|Given sine-double-angle hint graph supplies zeros; factor product equation and keep tan2x poles excluded
4|Example|47|210|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Quadratic cosine equation and identity-reduced sine/cosine equation; open-interval endpoints excluded
4|Try Now 47|1|210|1.6.6.1,1.6.6.2|text|no|Quadratic tangent equation; solve both ratio roots on closed full degree turn
4|Try Now 47|2|210|2.3.1.1,1.6.6.1,1.6.6.2|text|no|Quadratic secant equation; ratio-range feasibility and bounded roots
4|Try Now 47|3|210|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Convert sine-square/cosine equation to one trig variable before solving
4|Try Now 47|4|210|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Identity-reduced quadratic restricted to half degree turn
4|Try Now 47|5|210|2.3.2.1,1.6.6.1,1.6.6.2|text|no|Use sec^2=1+tan^2 to solve quadratic relation between squared reciprocal functions
4|Try Now 47|6|210|2.3.1.1,1.6.6.1,1.6.6.2|text|no|Quadratic secant with full radian interval and feasibility rejection
4|Example|48|211|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Show equation reduces to quadratic in sin^2, then solve; reject negative square and retain both sine signs
4|Try Now 48|1|211|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Show quartic sine relation reduces to supplied quadratic, hence recover full degree roots
4|Try Now 48|2|211|1.6.5.1,1.6.5.2,1.6.6.1,1.6.6.2|text|no|Prove fourth-power identity then use it to solve a quartic trig equation
4|Example|49|212|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Reduce to cosine quadratic and reject cos3/2; reuse result for half-angle argument with transformed interval
4|Try Now|49|212|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Show real solutions require cosx=-2/3, then solve shifted-argument equation on half turn
4|Example|50|213|1.6.6.1,1.6.6.2|text|no|Rational tangent equation reduces to quadratic; original tangent and denominator exclusions survive cross multiplication
4|Try Now 50|1|213|1.6.5.1,1.6.5.2,1.6.6.1,1.6.6.2|text|no|Prove quotient identity then hence solve; exclude cosine-zero points undefined in original quotient
4|Try Now 50|2|213|1.6.5.2,1.6.6.1,1.6.6.2|text|no|Transform cosine/tangent relation to quadratic in cosine-square then solve exact radians
4|Try Now 50|3|213|2.3.1.1,1.6.5.2,1.6.6.1,1.6.6.2|text|no|Use supplied proved reciprocal identity to solve equation; original denominator exclusions retained
4|Try Now 50|4|213|2.3.1.1,1.6.6.1,1.6.6.2|text|no|Double-angle cotangent equation on-pi..pi; enumerate all roots and exclude poles
4|Example|51|214|1.2.3.1,1.2.5.1,1.6.5.2|text|no|AP trig term sum expressed in sine-square; then GP convergence inequality gives open radian interval
4|Try Now 51|1|214|1.2.3.1,1.6.5.2,1.6.6.1,1.6.6.2|text|no|Thirteen-term AP with trigonometric terms determines cosine quadratic; keep feasible roots within open domain
4|Try Now 51|2|214|1.2.5.1,1.2.5.2,1.6.3.1|text|no|GP ratio is tan^2x/3; convergence range and exact sum at pi/6
4|Try Now 56|1|222|1.6.3.1|diagram|no|Read collinear baseline, perpendicular height, lengths4/6 and150degree angle; exact projected length and surd hypotenuse proof
4|Try Now 56|2|222|1.6.3.1|diagram|no|Read right triangle and midpoint; express AM in x and prove difference of acute angles, with inverse-tangent expression
'''

YM += r'''
5|Example|3|237|1.7.4.1|text|no|Magnitudes in2D/3D, including existing unit vectors and exact square roots
5|Try Now|3|237|1.7.4.1|text|no|Four vector magnitudes in column notation
5|Try Now|4|238|1.7.3.1,1.7.4.1|text|no|Unit vectors parallel to four nonzero vectors; parallel alone permits either orientation
5|Example|5|239|1.7.3.1,1.7.3.3|text|no|Given direction8i+j-4k and required magnitude2, recover position coordinates by normalising and scaling
5|Try Now 5|1|239|1.7.3.1,1.7.3.3|text|no|Point at distance6 from origin in specified direction; normalise3D vector then scale
5|Try Now 5|2|239|1.7.3.1,1.7.3.3|text|no|Point at distance5 in direction of supplied position vector; exact surd components
5|Try Now 5|3|239|1.7.3.1,1.7.2.2|text|no|Reconstruct vector from supplied unit direction and magnitude24
5|Example|6|243|1.7.2.2,1.7.2.3|text|no|Parallel column vectors with unknown scalar parameters; recover multiplier before solving two linear equations
5|Try Now 6|1|243|1.7.2.2|text|no|Equal scaled column vectors; known middle component fixes scale and two unknown components
5|Try Now 6|2|243|1.7.2.2,1.7.2.3|text|no|Parallel3D vectors imply a common scalar multiplier, then determine q
5|Example|7|244|1.7.3.2,1.7.4.1|text|no|Coordinate endpoints to directed displacement in i,j,k, then segment length
5|Example|9|246|1.7.3.2,1.7.2.3|diagram|no|Given three position vectors and illustrative geometry, prove collinearity from common-start multiples and identify midpoint ratio
5|Try Now 9|1|247|1.7.2.1,1.7.2.2,1.7.2.3,1.7.3.3|diagram|no|Connected position-vector geometry with extended rays; express vectors then prove collinearity using common point L
5|Try Now 9|2|247|1.7.2.1,1.7.2.2,1.7.2.3|diagram|no|Midpoint and2/3division in triangle; endpoint extension then show MTY collinear; handwritten vector not authoritative
5|Try Now 9|3|247|1.7.2.1,1.7.2.2,1.7.2.3|text|no|Parallelogram internal ratios OR:RC1:2 and AS:SC2:1; prove OB=3RS
5|Try Now 11|1|250|1.7.1.1,1.7.3.1,1.7.3.2|text|no|Position-vector components to point coordinates; displacement and directed unit vector
5|Try Now 11|2|250|1.7.3.2,1.7.3.3,1.7.3.1|text|no|Displacement from given endpoints, midpoint position and unit vector from origin towards midpoint
5|Example|12|252|1.7.4.2|text|no|Component scalar products in2D and3D; zero third component must be included consistently
5|Try Now 12|1|252|1.7.4.2|text|no|Two component scalar products, with missing basis components treated as zero
5|Try Now 12|2|252|1.7.4.2,1.6.3.1|text|no|Scalar product from magnitudes4,5 and60degree angle, not component coordinates
5|Example|13|253|1.7.4.2,1.7.4.1,1.7.5.1|text|no|Find angle between2D/3D vectors via signed dot product and positive magnitudes
5|Try Now 13|1|254|1.7.4.2,1.7.4.1,1.7.5.1|text|no|Two vector-angle computations in2D/3D
5|Try Now 13|2|254|1.7.4.1,1.7.4.2,1.7.5.1|text|no|Compute three magnitudes,two scalar products,then corresponding angles to1dp
5|Try Now 13|3|254|1.7.4.1,1.7.4.2,1.7.5.1|text|no|Angle between two3D column vectors, approximately75.7degrees
5|Example|14|254|1.7.3.2,1.7.3.3,1.7.5.2|text|no|Recover endpoint from displacement, then scalar-product-zero condition determines perpendicularity parameter13/3
5|Try Now 14|1|254|1.7.5.2|text|no|Show one vector perpendicular to each of two others by two distinct zero dot products
5|Example|16|257|1.7.4.1,1.7.3.3,1.7.2.2,1.7.5.2,1.7.5.1|text|no|Magnitude and extension point, then perpendicularity parameter and two60degree-angle parameters; check signs after squaring
5|Try Now 16|1|258|1.7.4.1,1.7.4.2,1.7.5.1,1.7.5.2|text|no|Angle between two vectors then parameter making another pair perpendicular
5|Try Now 16|2|258|1.7.3.2,1.7.3.3,1.7.2.2,1.7.2.3,1.7.5.2|text|no|Recover endpoint; contrast parallel-multiplier parameter with perpendicular-dot-product parameter
5|Try Now 16|3|258|1.7.4.1,1.7.5.1,1.7.5.2,1.7.3.1|text|no|Triangular pyramid from position vectors; angle at origin, right angle, then scaled parallel direction with magnitude10
5|Try Now 16|4|258|1.7.4.2,1.7.5.2,1.7.5.1|text|no|Parameter dot product25+p^2 proves perpendicularity impossible over reals; solve two60degree-angle parameter values
'''

YM += r'''
5|Try Now 14|2|255|1.7.5.2|text|no|Select all listed vectors perpendicular to a via zero dot product; continuation after Q1 on254
'''

YM += r'''
6|Example|5|275|1.8.2.2|text|no|Differentiate50th power of quadratic composite without expanding; inner derivative2x+3 must remain
6|Try Now 5|1|276|1.8.2.1,1.8.2.2|text|no|Differentiate same cubic composite by chain rule then expansion, compare equivalent forms
6|Try Now 5|2|276|1.8.2.2|text|no|Six polynomial-inner chain derivatives, large positive and negative outer powers
6|Example|6|276|1.8.2.2|text|no|Reciprocal cube-root composite; rewrite rational exponent then chain rule with nonzero inner value
6|Try Now|6|276|1.8.2.2|text|no|Eight chain derivatives with radicals,reciprocals and nested powers; real domains and poles must be respected
6|Example|7|277|1.8.2.1,1.8.1.1|text|no|Expand product then differentiate to obtain tangent gradient28 at supplied point
6|Try Now 7|1|277|1.8.2.1,1.8.1.1|text|no|Evaluate derivative at a supplied point on quadratic
6|Try Now 7|2|277|1.8.2.1,1.8.1.1|text|no|Gradient at y-axis intercept: infer x0 before evaluating derivative
6|Example|8|277|1.8.2.1,1.8.1.1|text|no|Distinguish derivative value60 from curve ordinate-77 at x-3; continues278
6|Try Now|8|278|1.8.2.1,1.8.1.1|text|no|Six pairs of gradient and ordinate at supplied input, including radicals and reciprocal powers
6|Example|9|278|1.8.2.1,1.8.1.1|text|no|Two gradient conditions determine quadratic coefficients a5,b-6
6|Try Now 9|1|278|1.8.2.1,1.8.1.1|text|no|Two gradient conditions determine coefficients of quartic-plus-quadratic curve
6|Try Now 9|2|278|1.8.2.1,1.8.1.1|text|no|Gradient conditions at opposite inputs determine linear-plus-reciprocal-square coefficients
6|Example|10|279|1.8.2.2,1.8.1.1|text|no|Point and gradient on a/(bx-1); solve coefficients and reject denominator-zero spurious branch
6|Example|11|280|1.8.2.1,1.8.3.1|text|no|Find contact ordinate,derivative and tangent line at x-1
6|Try Now 11|1|280|1.8.2.1,1.8.3.1|text|no|Cubic tangent at x-1
6|Try Now 11|2|280|1.8.2.1,1.8.3.1|text|no|Quadratic tangent at y-axis intercept
6|Try Now 11|3|280|1.8.2.1,1.8.3.1|text|no|Cubic tangent at fractional input3/2
6|Try Now 11|4|281|1.8.2.1,1.8.3.1|text|no|Two reciprocal/polynomial tangents; numbered question continues prior page set
6|Example|12|281|1.8.2.1,1.8.3.1|text|no|Negative reciprocal normal, slope negative reciprocal of derivative3/2
6|Try Now 12|1|281|1.8.2.1,1.8.3.1|text|no|Normal to cubic at x-1
6|Try Now 12|2|281|1.8.2.1,1.8.3.1|text|no|Normal to quadratic at x0
6|Try Now 12|3|282|1.8.2.1,1.8.3.1|text|no|Normal to cubic at fractional input3/2
6|Try Now 12|4|282|1.8.2.1,1.8.3.1|text|no|Source explicitly asks tangents despite surrounding normal exercise; preserve wording conflict rather than silently change assessed response
6|Example|13|282|1.8.2.2,1.8.3.1|text|no|Tangent and normal to reciprocal cube-root at negative input; source loses derivative minus sign and interchanges answers
6|Try Now 13|1|283|1.8.2.1,1.8.2.2,1.8.3.1|text|no|Three tangent-and-normal pairs at supplied input, with polynomial-power,root and reciprocal-quadratic forms
6|Try Now 13|2|283|1.8.2.2,1.8.3.1|text|no|Two root-composite tangent/normal pairs at supplied contact points
6|Example|14|283|1.8.3.1|text|no|Derivative formula already given; normal intercepts and their midpoint, no re-differentiation required
6|Try Now 14|1|284|1.8.3.1|text|no|Given derivative function and point; find normal using evaluated derivative and reciprocal slope
6|Try Now 14|2|284|1.8.3.1|text|no|Given reciprocal-quadratic derivative, not original curve; normal through given point
6|Example|15|284|1.8.2.1,1.8.3.1|text|no|Explicit reciprocal curve tangent versus given intersecting line; acute angle from slope inclinations, no implicit differentiation required
6|Example|16|286|1.8.2.1,1.8.3.2|text|no|Derivative sign inequalities give increasing/decreasing ranges for two quadratics
6|Try Now 16|1|286|1.8.2.1,1.8.3.2|text|no|Two increasing-function ranges from linear derivative inequalities
6|Try Now 16|2|287|1.8.2.1,1.8.3.2|text|no|Two decreasing-function ranges; continuation after preceding page heading
6|Example|17|287|1.8.2.1,1.8.3.2|text|no|Cubic monotonic intervals from derivative quadratic sign; source illustrations confuse function zeros with derivative zeros
6|Try Now 17|1|288|1.8.2.1,1.8.3.2|text|no|Cubic increasing/decreasing ranges; solve derivative quadratic inequality
6|Try Now 17|2|288|1.8.2.1,1.8.3.2|text|no|Second cubic with two turning inputs; distinguish outside and inside intervals
6|Try Now 17|3|288|1.8.2.2,1.8.3.2|text|no|Shifted cubic-minus-linear derivative inequality; recover original x boundaries
6|Example|18|288|1.8.2.2,1.8.3.2|text|no|Explain derivative sign for cubic composite and reciprocal-linear function; disconnected reciprocal domain requires component intervals
6|Try Now 18|1|289|1.8.2.2,1.8.3.2|text|no|Prove reciprocal function decreasing on stated x>=0 from negative derivative
6|Try Now 18|2|289|1.8.2.1,1.8.3.2|text|no|Prove cubic gradient never negative by perfect square, allowing zero at isolated input
6|Example|19|289|1.8.2.1,1.8.3.3|text|no|Differentiate V(t) then evaluate instantaneous rate15 at t2
6|Try Now 19|1|290|1.8.2.1,1.8.3.3|text|no|Instantaneous rate from quadratic A(t), not average difference quotient
6|Try Now 19|2|290|1.8.2.2,1.8.3.3|text|no|Instantaneous rate from reciprocal-root time function
6|Example|20|290|1.8.2.2,1.8.3.3|text|no|Water-depth time model: values at0and4 then instantaneous depth rate1/3cm/s
6|Try Now|20|290|1.8.2.2,1.8.3.3|text|no|Supplied medicine-mass time model; initial/later amounts then signed instantaneous rate-8mg/h; mathematical context only
6|Example|21|291|1.8.2.1,1.8.3.4|text|no|Displacement polynomial to velocity and acceleration; evaluate and interpret negative acceleration
6|Try Now|21|291|1.8.2.2,1.8.3.4|text|no|Composite fifth-power displacement, first and second time derivatives at t2 with correct units
6|Example|22|292|1.8.3.3|text|no|Connected circle-area and radius rates; chain factor dr/dt yields4pi square cm/s
6|Try Now 22|1|292|1.8.3.3|text|no|Connected rate of circle area from given increasing radius
6|Try Now 22|2|292|1.8.3.3|text|no|Sphere surface-area and volume rates from same radial rate; formulae explicitly supplied
6|Example|23|293|1.8.2.2,1.8.3.3|text|no|Negative dx/dt times negative derivative gives positive y-rate.04units/s
6|Try Now 23|1|293|1.8.2.1,1.8.3.3|text|no|Coordinate connected rate on quadratic curve; interpret decreasing x as negative rate
6|Try Now 23|2|293|1.8.2.2,1.8.3.3|text|no|Coordinate connected rate on reciprocal-quadratic curve
6|Try Now 23|3|293|1.8.2.2,1.8.3.3|text|no|Coordinate connected rate on square-root curve
6|Try Now 29|2|302|1.8.4.1,1.8.4.2|text|no|Derivative already given; find stationary x-values and classify by second derivative, no ordinates available or requested
6|Example|30|302|1.8.2.2,1.8.4.1,1.8.4.2|text|no|Reciprocal composite stationary inputs1/4and3/4; second-derivative signs justify max/min
6|Try Now 30|1|302|1.8.2.2,1.8.4.1,1.8.4.2|text|no|Shifted cubic-minus-linear stationary inputs and justified classification
6|Try Now 30|2|303|1.8.2.1,1.8.4.1,1.8.4.2|text|no|Root-minus-linear stationary coordinates and second-derivative classification
6|Try Now 30|3|303|1.8.2.1,1.8.4.1,1.8.4.2|text|no|Reciprocal-shift-plus-linear max/min coordinates; respect pole x3
6|Example|31|303|1.8.4.1,1.8.4.2|text|no|Known stationary point and derivative with unknown k; determine k,other stationary input and nature of both
6|Example|32|305|1.8.4.1,1.8.4.2|text|no|Fixed-volume rectangular block; eliminate height and minimise surface area with positive-dimension domain
6|Try Now 32|1|306|1.8.4.1,1.8.4.2|text|no|Fixed-volume cuboid with base ratio1:3; derive area expression and classify stationary minimum
6|Try Now 32|2|306|1.8.4.1,1.8.4.2|text|no|Fixed-surface square-base block: eliminate height then maximise volume within positive feasible dimensions
6|Try Now 32|3|306|1.8.4.1,1.8.4.2|text|no|Open tank500litres; convert units,derive sheet area,prove minimum and recover dimensions
6|Try Now|33|307|1.8.4.1,1.8.4.2|text|no|Fixed-volume closed cylinder; derive area in r and find/classify stationary value
'''

YM += r'''
6|Try Now 23|4|294|1.8.3.3|text|no|Oil-patch area rate from radius50m and increasing3m/h; fourth numbered item continues the set beyond page293
'''

YM += r'''
7|Example|9|331|1.9.1.2,1.9.2.1,1.9.2.2|text|no|Integrate supplied cube-root reciprocal derivative, use point3,1 then y-intercept; branch-continuity assumption across x1/3 needs clarity
7|Try Now 9|1|331|1.9.1.2,1.9.2.1,1.9.2.2|text|no|Recover curve from reciprocal-root derivative and supplied point
7|Try Now 9|2|331|1.9.1.2,1.9.2.1,1.9.2.2|text|no|Recover curve from reciprocal-square linear derivative and point
7|Try Now 9|3|331|1.9.1.2,1.9.2.1,1.9.2.2|text|no|Recover square-root-gradient curve then y-axis crossing
7|Try Now 9|4|331|1.9.1.2,1.9.2.1,1.9.2.2|text|no|Integrate two-term derivative and use function value to settle constant
7|Example|10|332|1.8.3.1,1.9.1.2,1.9.2.1,1.9.2.2|text|no|Normal slope determines positive contact coordinate, then integrate derivative and use contact point
7|Try Now 10|1|332|1.8.3.1,1.9.2.1,1.9.2.2|text|no|Normal slope fixes gradient parameter p, then curve recovered from supplied point
7|Try Now 10|2|333|1.8.3.1,1.9.1.2,1.9.2.1,1.9.2.2|text|no|Positive a and point(a^2,3): tangent and curve in a, then second point determines a and distance between points
7|Example|11|333|1.9.1.2,1.9.2.1,1.9.2.2|text|no|Integrate given second derivative twice; stationary condition and point settle two distinct constants
7|Try Now 11|1|334|1.9.1.2,1.9.2.1,1.9.2.2|text|no|Second derivative12/x^3 and stationary point2,10 determine complete curve
7|Try Now 11|2|334|1.9.1.2,1.9.2.1,1.9.2.2|text|no|Second derivative and stationary input determine first constant; another curve point determines second and stationary ordinate
7|Example|12|334|1.8.2.2,1.9.1.1|text|no|Differentiate given reciprocal-quadratic function then recognise a scalar multiple to integrate; derivative hint avoids general substitution claim
7|Try Now 12|1|334|1.8.2.2,1.9.1.1|text|no|Supplied derivative task supports reverse-recognition integral with cubic inner expression
7|Try Now 12|2|334|1.8.2.2,1.9.1.1|text|no|Differentiate sixth power of quadratic then recognise integral as scalar multiple of derivative
7|Try Now 12|3|334|1.8.2.2,1.9.1.1|text|no|Differentiate shifted-quadratic sixth power then reverse supplied result, not unrestricted substitution
7|Example|13|336|1.9.1.2,1.9.3.1|text|no|Three definite integrals; simplify reciprocal quotient before applying upper-minus-lower
7|Try Now|13|336|1.9.1.2,1.9.3.1|text|no|Six definite power integrals including fractional and reciprocal powers; bounds read exactly
7|Example|14|337|1.9.1.2,1.9.3.1|text|no|Expand rational integrand into powers and integrate reciprocal-root linear composite; two finite exact answers
7|Try Now|14|337|1.9.1.2,1.9.3.1|text|no|Six definite integrals; part(e) crosses a pole and is defective as a finite-integral exercise
7|Example|15|339|1.9.4.1|graph|no|Read shaded positive region below parabola with x1,3 bounds; integrate in x
7|Try Now|15|339|1.9.4.1|graph|no|Two positive shaded regions under polynomial curves, with explicit vertical bounds
7|Example|16|339|1.9.4.1|graph|no|Read square-root curve and x-axis region0..4; integrate in x, alternative y-method appears asExample20
7|Example|17|340|1.9.4.1|graph|no|Find parabola intercepts then unsigned below-axis area; signed integral is-36 but geometric area36
7|Example|19|343|1.9.4.1|graph|no|Read y1..3 horizontal boundaries and positive branchx=sqrt y; integrate with respect to y
7|Try Now 19|1|343|1.9.4.1|graph|no|Sideways parabola x=y(3-y) and y-axis; infer horizontal bounds from zeros
7|Try Now 19|3|343|1.9.4.1|graph|no|Shifted cubic with horizontal bounds1,8; y-axis boundary supplied by shaded graph, not complete prose alone
7|Example|21|345|1.4.2.1,1.9.4.1|graph|no|Find two curve-line intersection bounds then integrate upper minus lower between them
7|Try Now 21|1|346|1.4.2.1,1.9.4.1|graph|no|Parabola and line enclose region; solve endpoints and subtract in correct order
7|Try Now 21|2|346|1.4.2.1,1.9.4.1|text|no|Area between quadratic and line; hint recommends a sketch but sketch is not a required submitted response
7|Example|22|346|1.4.2.1,1.9.4.1|graph|no|Square-root curve meets line; reject extraneous squared root then combine curve area and triangle across switching boundary
7|Try Now 22|1|347|1.4.2.1,1.9.4.1|graph|no|Find non-origin crossing P3,6; shaded region uses line from0to3 and curve3to5, not merely lens between them
7|Try Now 22|2|347|1.8.3.1,1.9.4.1|graph|no|Normal at square-root curve contact meets x-axis; area boundary switches from curve to normal
7|Example|23|347|1.9.4.1|graph|no|Cubic and two normals bound region; subtract curve area from trapezium; given normal intersections avoid unasked differentiation
7|Try Now 24|1|349|1.4.2.1,1.9.4.1|graph|no|Parabolas intersect at positive A; shaded area below piecewise upper boundary and above x-axis
7|Try Now 24|2|349|1.1.1.1,1.9.4.1|graph|no|Horizontal strips between two quadratic curves y4..6; complete square before choosing positive inverse branch
7|Example|25|349|1.9.4.1|graph|no|Given positive shaded cubic area4, recover boundary b2; graph excludes negative fourth-root branch
7|Try Now 25|1|349|1.9.4.1|graph|no|Prescribed parabola shaded area9 determines positive right boundary p3
7|Try Now 25|2|349|1.9.4.1|graph|no|Equal shaded areas below and above axis determine k3; split at root2, preserve unsigned comparison
7|Example|31|356|1.9.4.2|graph|no|Rotate shaded parabola stripx1..3 about x-axis; square radius before integration
7|Try Now 31|1|356|1.9.4.2|graph|no|Rotate cubic-plus-one regionx0..3 about x-axis; graph supplies x-axis boundary omitted from prose
7|Try Now 31|2|356|1.9.4.2|text|no|Rotate4sqrt x-x region0..16 about x-axis; expand square with correct cross term
7|Example|33|358|1.9.4.2|graph|no|Rotate y=x^2+1 regiony1..2 around y-axis; use x^2=y-1 directly
7|Try Now 33|1|358|1.9.4.2|graph|no|Rotate parabola strip from y1to5 about y-axis; graph specifies right branch and axis boundary
7|Try Now 33|2|358|1.9.4.2|graph|no|x=8/y^2-2 and positive y-axis crossing; infer upper2 then integrate squared horizontal radius
7|Example|37|363|1.9.4.3,1.9.2.1|text|no|Integrate time acceleration twice with initial velocity4 and displacement0; distinct constants and units
7|Try Now|37|364|1.9.4.3,1.9.2.1|text|no|Acceleration6t+1, initial velocity2 and displacement1; recover v(t),s(t)
7|Example|38|364|1.9.4.3,1.8.3.4,1.8.4.1,1.8.4.2|text|no|Given velocity12t-t^2; initial value,acceleration,max velocity,travel before2seconds and next rest time
7|Try Now 38|1|365|1.9.4.3,1.8.4.1,1.8.4.2|text|no|Bus acceleration5-t from rest; next stop,positive-velocity distance and peak speed before stop
7|Try Now 38|2|365|1.8.3.4,1.9.4.3|text|no|Positive reciprocal-square velocity: initial acceleration and distance on3..6seconds
7|Example|39|365|1.9.4.3,1.9.2.1|text|no|Upwards projectile with acceleration-10 and initial velocity12; differential equation,height and maximum reached at rest
7|Try Now 39|1|366|1.9.4.3,1.9.2.1|text|no|Downwards projectile: velocity after1second fixes initial value, then mine-shaft depth after4seconds
7|Try Now 39|2|366|1.9.4.3,1.8.4.1,1.8.4.2|text|no|Acceleration6-t from rest; next stop,distance and maximum speed on positive-velocity journey
7|Try Now 39|3|366|1.8.3.4,1.8.4.1,1.8.4.2|text|yes|Given cubic displacement: derive v,a,next rest,distance and maximum velocity,then sketch linear acceleration with axis intercepts
'''

YM += r'''
4|Example|17|181|1.6.3.1|text|no|Exact30,45,60degree expressions without calculator; equivalent rationalised methods shown inline
6|Example|33|307|1.8.4.1,1.8.4.2|text|no|Closed fixed-volume cylinder: eliminate height then minimise total surface area; positive radius5.4cm to1dp
'''

YM += r'''
8|Example|1|377|2.1.1.1|text|no|Absolute temperature forecast errors; interpret magnitude independent of direction
8|Try Now|1|377|2.1.1.1|text|no|Absolute diameter deviations from46.0mm; units and nonnegative result
8|Example|2|378|2.1.1.1|text|no|Four nested-sign numeric modulus expressions, distinguish outer minus and power from modulus
8|Try Now 2|1|378|2.1.1.1|text|no|Twelve numeric modulus expressions with signs outside bars
8|Try Now 2|2|378|2.1.1.1|text|no|Six nested/power/fraction modulus expressions, including0.5 quotient
8|Example|3|379|2.1.1.2|text|no|Absolute linear expression equals positive7; two sign branches, substitute both into original
8|Try Now|3|379|2.1.1.2|text|no|Four basic positive-modulus equations with two roots
8|Example|4|379|2.1.1.2|text|no|Isolate modulus after outer scalar/translation, then solve both branches; positive and negative outer multipliers
8|Try Now|4|380|2.1.1.2|text|no|Six scaled/translated modulus equations; retain sign when dividing negative outer coefficient
8|Example|5|380|2.1.1.2|text|no|Contrast impossible negative modulus value with zero modulus giving one root
8|Try Now|5|380|2.1.1.2|text|no|Six zero or negative modulus targets: singleton versus empty solution sets
8|Example|6|380|2.1.1.2|text|no|Linear expression on right can be negative; solve candidates then reject extraneous x-1 by substitution
8|Try Now|6|381|2.1.1.2|text|no|Six modulus-versus-linear equations, including no valid root or one/two valid roots after sign constraints
8|Example|7|381|2.1.1.2|text|no|Modulus both sides; compare signed-linear branches or square both sides, equivalent here because both sides nonnegative
8|Try Now 7|1|381|2.1.1.2|text|no|Two equations explicitly require both branch and squaring methods; method evidence is part of requested work
8|Try Now 7|2|381|2.1.1.2|text|no|Six modulus-on-both-sides equations; alternate the two introduced valid methods
8|Example|10|386|2.1.1.3|text|no|Bounded modulus inequality and impossible negative bound; adjacent summary table has sign/domain errors
8|Try Now|10|387|2.1.1.3|text|no|Nine less-than/at-most modulus inequalities including empty and singleton solutions
8|Example|11|387|2.1.1.3|text|no|Outside-interval modulus inequality versus strictly positive modulus excluding exactly one zero
8|Try Now 11|1|387|2.1.1.3|text|yes|Nine inequalities and explicitly illustrate solutions on number lines; include open/closed endpoints and all-real/empty cases
8|Try Now 11|2|387|2.1.1.3|text|yes|Three mixed inequalities with required number-line illustrations
8|Try Now 11|3|388|2.1.1.3|text|no|Six additional inequalities continue set; rational outer scaling and negative-multiplier reversal
8|Example|13|389|2.1.1.3|text|no|Modulus inequality both sides; square and solve quadratic or compare graphs, outside two crossings
8|Try Now|13|389|2.1.1.3|text|no|Six modulus-on-both-sides inequalities, strict and non-strict comparisons
8|Example|14|390|2.1.3.1,2.1.3.3|text|no|in-scope|Cubic divided by linear expression; missing-zero/order handling and quotient/remainder identity; continuation391
8|Try Now|14|391|2.1.3.1,2.1.3.3|text|no|Six degree2..4 dividends divided by linear factors, including non-monic divisor
8|Example|15|391|2.1.3.3,2.1.4.1|text|no|Find remainder of2x^3-x on division byx+4; long/synthetic methods shown but alternative remainder evaluation valid
8|Try Now|15|392|2.1.3.1,2.1.3.3|text|no|Simplify two polynomial quotients and find remainders, degree3/4 by linear divisors
8|Example|16|392|2.1.3.2,2.1.3.3|text|no|Reorder degree4dividend then divide by quadratic, linear remainder-9x+5
8|Try Now 16|1|392|2.1.3.2,2.1.3.3|text|no|Six quadratic-divisor quotient/remainder tasks with degree2..4 dividends, including factored divisor
8|Try Now 16|2|392|2.1.3.2,2.1.3.3|text|no|Three quadratic-divisor divisions, repeated/factored/irreducible expressions
8|Example|17|393|2.1.4.1|text|no|Explicit remainder-theorem request, evaluate cubic at divisor root1
8|Try Now|17|393|2.1.4.1|text|no|Three remainders explicitly without doing division; evaluate correct signed root
8|Example|18|394|2.1.4.1,2.1.4.3|text|no|Given remainder and degree5polynomial determine p; degree5 is calibration caution, not LIMIT05 division exclusion
8|Try Now 18|1|394|2.1.4.1,2.1.4.3|text|no|Two given remainders yield unknown linear coefficient
8|Try Now 18|2|394|2.1.4.1,2.1.4.3|text|no|Remainder condition quadratic in parameter p; retain both real parameter roots
8|Example|19|394|2.1.4.1,2.1.4.3|text|no|Two remainders determine two polynomial coefficients by simultaneous equations
8|Try Now 19|1|395|2.1.4.1,2.1.4.3|text|no|Remainders determine unknown positive integer exponent and coefficient; parity of(-3)^n matters
8|Try Now 19|2|395|2.1.4.1,2.1.4.3|text|no|Two remainder conditions, one non-monic divisor, determine a,b
8|Try Now 19|3|395|2.1.4.1,2.1.4.3|text|no|Equal remainders at two divisors plus known third remainder determine two coefficients
8|Try Now 19|4|395|2.1.4.1,2.1.4.3,2.1.3.2,2.1.3.3|text|no|Determine coefficients from two linear-divisor remainders then divide by quadratic
8|Example|20|395|2.1.4.1,2.1.4.3|text|no|One divisor remainder is twice another; translate relation into f(-3)=2f(2)
8|Try Now 20|1|395|2.1.4.1,2.1.4.3|text|no|Two different polynomials have equal remainder under same divisor; determine common parameter
8|Try Now 20|2|395|2.1.4.1,2.1.4.3|text|no|Unknown constant from R and2R remainders at opposite divisor roots
8|Example|21|396|2.1.4.2|text|no|Show supplied linear factor using zero evaluation; adjacent general formula has b/c symbol typo
8|Try Now 21|1|396|2.1.4.2,2.1.3.2|text|no|Show two linear factors and a quadratic factor; quadratic case needs division or equivalent polynomial identity
8|Try Now 21|2|396|2.1.4.2,2.1.4.3|text|no|Given linear factor determines unknown quadratic coefficient of cubic
8|Try Now 21|3|396|2.1.4.2,2.1.4.3|text|no|Two given linear factors determine two coefficients
8|Example|22|397|2.1.4.2|text|no|Factor cubic completely via candidate root,division and quadratic factorisation; method alternatives shown
8|Try Now|22|397|2.1.4.2|text|no|Seven cubic factorisations including symbolic a-scaled coefficients; constant/leading-coefficient root candidates
8|Example|23|398|2.1.4.1,2.1.4.2,2.1.4.3|text|no|One known factor and another nonzero remainder determine a,b
8|Try Now 23|1|398|2.1.4.1,2.1.4.2,2.1.4.3|text|no|Determine coefficients from factor and remainder then completely factorise cubic
8|Try Now 23|2|398|2.1.4.1,2.1.4.2,2.1.4.3,2.1.3.2,2.1.3.3|text|no|Known factor and opposite remainder determine cubic then find quadratic-divisor remainder
8|Try Now 23|3|398|2.1.4.1,2.1.4.2,2.1.4.3|text|no|Exactly divisible byx+2 and parameter-dependent remainder atx-a; compare expressions without confusing polynomial variable with parameter
8|Try Now 23|4|398|2.1.4.2,2.1.4.3|text|no|Known quadratic factor; factor it to obtain two root conditions for unknown coefficients
8|Example|24|399|2.1.4.2,2.1.4.4|text|no|Cubic equation has three rational roots, including noninteger values; final copied equation has wrong middle sign
8|Try Now|24|399|2.1.4.2,2.1.4.4|text|no|Four cubic equations explicitly using factor theorem, integer and fractional roots
8|Example|25|400|2.1.4.2,1.1.2.1,1.1.2.2|text|no|Given real linear factor; remaining quadratic negative discriminant proves no additional real roots
8|Try Now 25|1|400|2.1.4.2,1.1.2.1,1.1.2.2|text|no|Show supplied factor then prove cubic has exactly one real root using remaining quadratic discriminant
8|Try Now 25|2|400|2.1.4.1,2.1.4.2,2.1.4.4|text|no|Remainder,show supplied factor and solve complete cubic equation
8|Try Now 25|3|400|2.1.4.1,2.1.4.2,2.1.4.4|text|no|Remainder plus given factor lead to remaining linear factors and three roots
'''

YM += r'''
9|Example|1|408|2.2.1.1|text|no|Convert four exponential equalities to logarithmic notation, including symbolic base subject to positive nonunit base
9|Try Now|1|408|2.2.1.1|text|no|Four exponential-to-log conversions; preserve base,argument and exponent roles
9|Example|2|409|2.2.1.1|text|no|Two logarithmic-to-exponential conversions, including fractional exponent
9|Try Now|2|409|2.2.1.1|text|no|Six log-to-index conversions with zero,negative and symbolic exponent and base1/4
9|Example|3|410|2.2.1.1,2.2.3.1|text|no|Convert10^x=200 then evaluate x to3sf
9|Try Now 3|1|410|2.2.1.1,2.2.3.1|text|no|Exponential-to-common-log conversion and3sf solution250
9|Try Now 3|2|410|2.2.1.1,2.2.3.1|text|no|Common-log solution with subunit argument.05, negative exponent
9|Example|4|410|2.2.1.1|text|no|Convert log10x1.2 to index form then evaluate positive x
9|Try Now 4|1|410|2.2.1.1|text|no|Common-log value3.5 determines x, rounded3sf
9|Try Now 4|2|410|2.2.1.1|text|no|Negative common-log value-.6 determines positive x below1
9|Example|5|411|2.2.1.1|text|no|Four exact logarithm values using powers, reciprocal fractions,zero exponent and base1/2
9|Try Now 5|1|411|2.2.1.1|text|no|Eight exact log values with roots and reciprocal bases, without calculator
9|Try Now 5|2|411|2.2.1.1|text|no|Exact composite expression in logarithms of roots and reciprocal powers
9|Try Now 5|3|411|2.2.1.1|text|no|Exact sum of three logs with distinct bases; evaluate separately before combining
9|Example|6|413|2.2.1.2|text|no|Expand logarithms of quotient,power and cube root; preserve positive-argument convention from412
9|Try Now 6|1|413|2.2.1.2|text|no|Nine log expansions; products,quotients,powers and variable exponents, with original argument-domain restrictions
9|Try Now 6|2|413|2.2.1.2|text|no|Four expansions at different bases; factored differences and squared factors require care over positive domains
9|Example|7|414|2.2.1.2|text|no|Combine same-base weighted sum/difference into single log of quotient
9|Try Now|7|414|2.2.1.2|text|no|Four compressed log expressions; combine only same base and keep original domain
9|Example|8|414|2.2.1.2|text|no|Absorb standalone constant into base2log before compressing quotient b^2/(8c^5)
9|Try Now 8|1|414|2.2.1.2|text|no|Two single-log compressions with numerical offsets and products
9|Try Now 8|2|414|2.2.1.2|text|no|Mixed-base expression; group only matching bases, final0
9|Example|9|415|2.2.1.1,2.2.1.2|text|no|Log-product equation yields quadratic candidates; reject negative original arguments
9|Try Now 9|1|415|2.2.1.1,2.2.1.2|text|no|Two log equations: inverse conversion versus power-law reduction
9|Try Now 9|2|415|2.2.1.1,2.2.1.2|text|no|Four log product/quotient equations; original positivity conditions reject algebraic candidates
9|Example|10|416|2.2.1.2|text|no|Log-product equation has algebraic candidate6/5 but no valid real solution because original arguments negative
9|Try Now|10|416|2.2.1.2|text|no|Three log equations, including quadratic admissibility rejection and cancellation of leading polynomial terms
9|Example|11|416|2.2.1.1,2.2.1.2|text|no|Simultaneous log equations; negative y can be valid since logarithms apply to sums, while x must be positive
9|Try Now|11|416|2.2.1.1,2.2.1.2|text|no|Two simultaneous systems using log laws and inverse conversion; apply positivity to actual arguments rather than every variable blindly
9|Example|12|417|2.2.3.1,2.2.1.2|text|no|Solve positive-base exponential equation by taking common logs and isolating exponent
9|Try Now|12|417|2.2.3.1,2.2.1.2|text|no|Three exponential equations, including affine exponent2x-5
9|Example|13|417|2.2.3.1,2.2.1.2|text|no|Different positive bases and affine exponents on both sides; collect parameter times log constants
9|Try Now|13|418|2.2.3.1,2.2.1.2|text|no|Three two-base exponential equations with affine exponents
9|Example|14|418|2.2.3.1,2.2.1.2|text|no|Product of exponentials with bases5and7; linear equation in x after logs
9|Try Now|14|418|2.2.3.1,2.2.1.2|text|no|Three products/equalities of different exponential bases and constant multipliers
9|Example|15|418|2.2.3.1|text|no|Convert4^x-2^(x+2)=5 to quadratic in2^x; reject negative exponential candidate
9|Try Now 15|1|418|2.2.3.1|text|no|Quadratic in3^x with one impossible negative exponential root
9|Try Now 15|2|418|2.2.3.1|text|no|Show shifted powers reduce to quadratic in2^x, then solve with admissibility
9|Try Now 15|3|418|2.2.3.1|text|no|9^x and3^(x+1) reduce to quadratic in3^x
9|Try Now 15|4|419|2.2.3.1|text|no|Supplied y=2^x transforms positive/negative exponents to quadratic; both positive y roots yield x values
9|Example|16|419|2.2.3.2|text|no|Increasing and decreasing exponential inequalities; division by negative log reverses bound
9|Try Now|16|420|2.2.3.2|text|no|Three exponential inequalities with bases above/below1, strict and non-strict bounds
9|Example|17|420|2.2.3.2,2.2.1.2|text|no|Exponent3-x and subunit base5/6; two sign reversals, exact common-log bound
9|Try Now 17|1|420|2.2.3.2,2.2.1.2|text|no|Two affine-exponent inequalities with exact base10log answers
9|Try Now 17|2|420|2.2.3.2,2.2.1.2|text|no|Prove supplied exact logarithmic bound for product of base3and2 exponentials
9|Example|18|421|2.2.2.1|text|no|Evaluate supplied natural-exponential population model at present and6years; units millions
9|Try Now|18|422|2.2.2.1|text|no|Evaluate supplied natural-exponential decay model at0and5years; no physical half-life accuracy claim
9|Example|19|422|2.2.2.1|text|no|Calculator evaluation of e^.6,ln.8,lne to stated3sf
9|Try Now|19|422|2.2.2.1|text|no|Four numerical natural-exponential/log evaluations to3sf
9|Example|20|422|2.2.2.1,2.2.1.2|text|no|Exact e-ln inverse expressions, including negative coefficient and negative logarithm
9|Try Now|20|422|2.2.2.1,2.2.1.2|text|no|Three exact e-ln inverse evaluations without calculator
9|Example|21|422|2.2.2.1,2.2.3.1|text|no|Solve two natural-exponential equations, retaining exact natural-log answers
9|Try Now|21|423|2.2.2.1,2.2.3.1|text|no|Two affine-exponent equations with exact ln answers
9|Example|22|423|2.2.2.1,2.2.3.1|text|no|Solve7e^(3x)=320 by logarithm, numerical3sf
9|Try Now|22|423|2.2.2.1,2.2.3.1|text|no|Two natural-exponential equations with additive or multiplicative external constants
9|Example|23|423|2.2.3.1|text|no|Quadratic in positive e^x from positive/negative exponents; two admissible positive roots yield x of different signs
9|Try Now 23|1|423|2.2.3.1|text|no|Two quadratic-type equations in e^x, including inadmissible negative roots
9|Try Now 23|2|423|2.2.3.1,2.2.1.2|text|no|Exponential quadratic with exact roots leading to3ln3or-ln3
9|Example|24|424|2.2.3.2|text|no|Natural-exponential inequality with multiplier5andaffine exponent; numerical3sf bound
9|Try Now|24|424|2.2.3.2|text|no|Two natural-exponential inequalities, strict or non-strict, rounded3sf
9|Example|25|424|2.2.1.2,2.2.2.1|text|no|Eliminate natural logs to make y subject; preserve x>1,y>0 inherited from original arguments
9|Try Now 25|1|424|2.2.1.2,2.2.2.1|text|no|Rearrange ln z in terms of positive y to algebraic z=(y+2)/y^2
9|Try Now 25|2|424|2.2.1.2,2.2.2.1|text|no|Four natural-log equations; retain argument positivity after algebraic quadratic solving
9|Try Now 25|3|424|2.2.1.2,2.2.2.1|text|no|Natural-log quotient equals1; express exact x in e and check positive original arguments
9|Investigation exponential|1|425|2.2.2.2|text|yes|Plot four increasing and four decreasing exponentials; compare common intercept,asymptote,quadrants and base size. Continues426; graph-properties facet, not full inverse-demand coverage
9|Example|27|430|2.2.1.1|text|no|Point(2,1/4) on logarithmic graph determines allowed base16
9|Example|29|434|2.2.2.2,1.3.2.2,1.3.4.1,1.3.4.2|text|yes|Shifted log domain boundary,inverse and paired labelled sketches; asymptotes and axis intercepts
9|Try Now 29|1|435|2.2.2.2,1.3.2.2,1.3.3.1,1.3.4.1,1.3.4.2,1.3.3.2|text|yes|Natural-log domain/range,inverse,paired sketches and composite evaluation/admissibility
9|Try Now 29|2|435|2.2.2.2,1.3.2.2,1.3.4.1,1.3.4.2|text|yes|Shifted exponential range,inverse and common-axis sketches with all axis intersections
9|Try Now 29|3|435|2.2.2.2,1.3.2.2,1.3.3.1,1.3.4.1,1.3.4.2|text|yes|Restricted exponential range,inverse and evaluation,then sketch exponential and straight line on stated domain
9|Example|30|436|2.2.4.1|text|no|Linearise e^y=ab^x and x^a y^b=8; name transformed coordinates,gradient and intercept, preserve positive log domains and b!=0
'''

YM += '''
10|Example|4|452|2.3.2.2,1.6.3.1|text|no|Exact sine of compound special angles in degrees and radians; worked special triangles are solution aids
10|Try Now|4|452|2.3.2.2,1.6.3.1|text|no|Exact sine evaluation including compound angles and ordinary pi/2
10|Example|5|453|2.3.2.2,1.6.3.1|text|no|Exact sine difference and recognise compound-angle expression before evaluation
10|Try Now 5|1|453|2.3.2.2,1.6.3.1|text|no|Show exact sine pi/12 using alternate angle decomposition
10|Try Now 5|2|453|2.3.2.2,1.6.3.1|text|no|Recognise three sine-difference expressions and evaluate exactly by special angles
10|Example|6|454|2.3.2.2|text|no|Prove compound sine quotient equals tangent difference on common defined domain
10|Try Now|6|454|2.3.2.2|text|no|Three compound-angle identity proofs with denominator restrictions
10|Example|7|456|2.3.2.2,1.6.3.1|text|no|Recognise cosine difference and evaluate exact cosine compound angles
10|Try Now|7|456|2.3.2.2,1.6.3.1|text|no|Three exact cosine sums or compound special-angle values
10|Example|8|457|2.3.2.2|text|no|Recover missing ratios using quadrant signs, then compute compound sine and cosine exactly; triangles in solution only
10|Try Now 8|1|457|2.3.2.2|text|no|Given sine/cosine in fourth and first quadrant, find exact compound cosine and sine
10|Try Now 8|2|457|2.3.2.2|text|no|Resolve two angles within90..270 to second/third quadrants, then exact compound sine cosine and tangent
10|Example|9|458|2.3.2.2,1.6.3.1|text|no|Recognise tangent sum quotient and evaluate exact surd
10|Try Now|9|459|2.3.2.2,1.6.3.1,2.3.1.1|text|no|Exact tangent difference, negative angle and reciprocal cotangent in radians
10|Example|10|459|2.3.2.2,2.3.1.1|text|no|Prove shifted cotangent identity through tangent difference; preserve denominator restrictions
10|Try Now|10|459|2.3.2.2,2.3.1.1|text|no|Two compound tangent/cotangent proofs on common defined domain
'''

YM += '''
10|Example|11|460|2.3.2.2,1.6.6.1,1.6.6.2|text|no|Expand compound sine equation to tangent constant, then solve all angles on stated degree interval
10|Try Now 11|1|460|2.3.2.2,1.6.6.1,1.6.6.2|text|no|Two compound angle equations on negative-to-positive degree domain
10|Try Now 11|2|460|2.3.2.2,1.6.3.1,2.3.1.1,1.6.6.1,1.6.6.2|text|no|Show sine-sum identity, hence exact evaluation and equation involving secant on bounded domain
10|Example|12|461|2.3.2.2,1.6.6.1,1.6.6.2|text|no|Rearrange tangent-sum formula for tan B; then solve compound tangent equation via quadratic in tan x and admissibility
10|Try Now|12|461|2.3.2.2,1.6.6.1,1.6.6.2|text|no|Show tangent-sum/difference equation becomes quadratic in tan x and hence solve in first quadrant; exclude original poles
10|Example|13|463|2.3.2.3|text|no|Given sine and obtuse quadrant, exact sin2A,tan2A,sin4A and tan(A/2); reject incompatible half-angle candidate
'''

YM += '''
10|Try Now 13|1|464|2.3.2.3|text|no|Given obtuse angle cosine, determine exact double/fourth/half-angle ratios with signs
10|Try Now 13|2|464|2.3.2.3|text|no|Given obtuse angle sine, exact sin2B,sin4B and tan(B/2)
10|Try Now 13|3|464|2.3.2.3|text|no|Given negative tangent on90..270 choose quadrant2 then double/fourth angle ratios
10|Try Now 13|4|464|2.3.2.2,2.3.2.3|text|no|Two quadrant signs followed by exact sine sum and negative half-angle cosine
10|Example|14|464|2.3.2.3|text|no|Express sin2theta and cos-squared(theta/2) in symbolic p with acute-angle sign restriction
10|Try Now|14|465|2.3.2.3|text|no|Given acute-angle cosine a, derive symbolic sin4theta and sin(theta/2)
10|Example|15|465|2.3.2.2,2.3.2.3|text|no|Derive triple-tangent identity from sum and double-angle formulae; not memorisation of extra syllabus formula
10|Try Now|15|465|2.3.2.2,2.3.2.3,2.3.1.1|text|no|Six identities derived from double and compound angles including triple sine and reciprocal ratios; respect original domains
10|Example|16|466|2.3.2.3,1.6.6.1,1.6.6.2|text|no|Double-angle equation with tan; transform to sine squared and check original pole exclusions
10|Try Now 16|1|466|2.3.2.3,1.6.6.1,1.6.6.2|text|no|Double-angle cosine equation reduced to quadratic in cosine
10|Try Now 16|2|466|2.3.2.3,2.3.1.1,1.6.6.1,1.6.6.2|text|no|Tangent double-angle and cotangent equation; preserve poles while solving bounded degree roots
10|Try Now 16|3|466|2.3.2.3,1.6.5.1|text|no|Double-angle cosine times cosine reduces to cubic in cosine on full degree turn
10|Example|17|466|2.3.2.3,2.3.1.1,1.6.6.1,1.6.6.2|text|no|Prove reciprocal double-angle identity then hence solve radian equation with original denominator restrictions
10|Try Now 17|1|467|2.3.2.3,2.3.1.1,1.6.6.1,1.6.6.2|text|no|Show double-angle quotient identity then quadratic tangent equation on0..pi with original poles excluded
10|Try Now 17|2|467|2.3.2.3,2.3.1.1,1.6.5.1|text|no|Show squared-cosecant identity then tangent quadratic with numerical radian roots
'''

YM += '''
10|Example|18|468|2.3.2.4,1.6.6.1,1.6.6.2|text|no|R sine difference representation with exact amplitude and2dp phase; hence two bounded degree roots
10|Try Now|18|469|2.3.2.4,1.6.6.1,1.6.6.2|text|no|R sine difference and hence bounded degree equation; retain guard digits in phase
10|Example|19|469|2.3.2.3,2.3.1.1,2.3.2.4,1.6.6.1,1.6.6.2|text|no|Simplify reciprocal/double-angle expression to sine-cosine sum, then R form and bounded equation; original poles remain excluded
10|Try Now 19|1|470|2.3.2.4,1.6.6.1,1.6.6.2|text|no|R sine sum and hence positive right-hand side bounded equation
10|Try Now 19|2|470|2.3.2.4,1.6.5.1|text|no|R sine difference with irrational amplitude; negative right-hand side and shifted angle interval
10|Example|20|471|2.3.2.4,1.6.6.1,1.6.6.2|text|no|R cosine difference and hence bounded degree equation; source stamp overlaps some mathematics
10|Try Now 20|1|471|2.3.2.4,1.6.6.1,1.6.6.2|text|no|R cosine difference with surd coefficient, then equation reverses sine sign: use substitution or adapted phase deliberately
'''

YM += '''
10|Try Now 20|2|472|2.3.2.4,1.6.6.1,1.6.6.2|text|no|R cosine sum with irrational amplitude and bounded equation
10|Example|21|472|2.3.2.4,1.6.3.1,1.6.6.1,1.6.6.2|text|no|Exact special-angle phase in radians; show one exact root and find other bounded root
10|Try Now|21|473|2.3.2.4,1.6.3.1,1.6.6.1,1.6.6.2|text|no|Exact radian phase and bounded equation with special-angle right-hand side
10|Example|22|473|2.3.2.4,1.6.6.1,1.6.6.2|text|no|R sine difference then equation with3x; enumerate six roots across three full periods
10|Try Now|22|474|2.3.2.4,1.6.6.1,1.6.6.2|text|no|R cosine sum and equation with2x; enumerate every bounded-domain root
10|Example|23|475|2.3.2.4|text|no|Two R sine/cosine forms and global extrema with corresponding phase angles; solutions repeat periodically
'''

YM += '''
10|Try Now|23|476|2.3.2.4|text|no|R sine and cosine forms, exact extrema and corresponding angles modulo one period
10|Example|24|476|2.3.2.4|text|no|R sine amplitude followed by shifted,squared,cubed expression bounds; squared minimum occurs at zero rather than negative amplitude
10|Try Now|24|477|2.3.2.4|text|no|R sine difference then extrema of expression, shifted expression and square/cube transformations
10|Example|25|477|2.3.2.4|text|no|R cosine sum then shifted half-angle maximum and smallest positive input achieving it
10|Try Now|25|477|2.3.2.4|text|no|R cosine sum then recognise threefold scalar for smallest value
'''

YM += '''
11|Example|1|483|2.4.2.1|text|no|Differentiate polynomial product by product rule, with expansion as valid alternative
11|Try Now|1|484|2.4.2.1|text|no|Four polynomial products; explicit product-rule and expanded alternatives
11|Example|2|484|2.4.2.1,1.8.2.2|text|no|Product of shifted powers, chain factors and common-factor simplification
11|Try Now|2|484|2.4.2.1,1.8.2.2|text|no|Two products of affine powers with nonunit inner derivatives
11|Example|3|484|2.4.2.1,1.8.2.2|text|no|Polynomial times square-root product; write derivative as single fraction on interior domain
11|Try Now|3|485|2.4.2.1,1.8.2.2|text|no|Square-root products; part(b) repeats preceding Example3 exactly and supplies no additional breadth
11|Example|4|485|2.4.2.1,1.8.2.2,1.8.4.1|text|no|Differentiate factored powers and solve every zero-gradient factor including repeated roots
11|Try Now 4|1|485|2.4.2.1,1.8.2.2,1.8.4.1|text|no|Product-rule derivative then all stationary x values
11|Try Now 4|2|485|2.4.2.1,1.8.2.2|text|no|Product-rule gradient at given x
11|Try Now 4|3|485|2.4.2.1,1.8.2.2|text|no|Gradient of polynomial times root at stated point
11|Try Now 4|4|485|2.4.2.1,1.8.2.2,1.8.4.1|text|no|Stationary x for linear times square-root product; enforce differentiability domain
11|Try Now 4|5|486|2.4.2.1,1.8.2.2|text|no|Given nonzero gradient solve derivative equation for x
11|Example|5|486|2.4.2.1,1.8.2.2,1.8.3.1|text|no|Product-rule tangent at given input with negative inner derivative
11|Try Now 5|1|486|2.4.2.1,1.8.3.1|text|no|Polynomial-product tangent at given x, horizontal special case
11|Try Now 5|2|486|2.4.2.1,1.8.2.2,1.8.3.1|text|no|Product-rule tangent at y-axis crossing
11|Try Now 5|3|486|2.4.2.1,1.8.2.2,1.8.3.1|text|no|Gradient of product involving square root at positive x
'''

YM += '''
11|Example|6|487|2.4.2.2|text|no|Rational derivative by quotient rule and alternative reciprocal-power product rule; solution continues488
11|Try Now|6|488|2.4.2.2|text|no|Three rational derivatives, including cancellation to constant numerator
11|Example|7|488|2.4.2.2|text|no|Quotient rule in variable t, leading fifth-power terms cancel
11|Try Now|7|489|2.4.2.2|text|no|Two rational derivatives in t including cubic denominator
11|Example|8|489|2.4.2.2,1.8.2.2|text|no|Quotient with square-root denominator, chain factor and fractional simplification; real domain outside sqrt3 endpoints
11|Try Now|8|489|2.4.2.2,1.8.2.2|text|no|Four root/rational quotients including root of quotient and cube-root denominator; keep differentiability exclusions
11|Example|9|490|2.4.2.2,1.8.4.1|text|no|Quotient derivative and all stationary x, excluding denominator zero
11|Try Now 9|1|490|2.4.2.2,1.8.4.1|text|no|Rational stationary inputs with explicit x!=3
11|Try Now 9|2|490|2.4.2.2|text|no|Find full coordinates for given nonzero gradient on rational curve
11|Try Now 9|3|490|2.4.2.2|text|no|Evaluate quotient derivative at supplied input
11|Try Now 9|4|490|2.4.2.2,1.8.3.1|text|no|Rational tangent equation at supplied input
11|Try Now 9|5|490|2.4.2.2,1.8.3.1|text|no|Rational normal at x-axis crossing, use reciprocal negative gradient
'''

YM += '''
11|Example|10|492|2.4.1.1,2.4.1.2|text|no|Differentiate three affine-argument exponentials, including negative multiplier/exponent
11|Try Now|10|492|2.4.1.1,2.4.1.2|text|no|Four exponential derivatives with positive/negative/fractional inner slopes
11|Example|11|492|2.4.1.2|text|no|Exponential of quadratic or square root, nonlinear chain factors and positive-root domain
11|Try Now|11|493|2.4.1.1,2.4.1.2|text|no|Nonlinear exponential chains and sum of exponentials with square-root exponent
11|Example|12|493|2.4.1.1,2.4.1.2,2.4.2.1,2.4.2.2|text|no|Compare additive,product and quotient forms of x with exponential; reciprocal exponential can be rewritten
11|Try Now 12|1|493|2.4.1.1,2.4.1.2,2.4.2.1,2.4.2.2|text|no|Three related polynomial-exponential sum/product/quotient derivatives
11|Try Now 12|2|493|2.4.1.1,2.4.1.2,2.4.2.1,2.4.2.2|text|no|Exponential quotient/root quotient and product derivatives with distinct product-rule alternatives
11|Try Now 12|3|493|2.4.1.2,2.4.2.2|text|no|Gradient of reciprocal affine exponential at specified x
11|Example|13|494|2.4.1.1,2.4.1.2,2.2.3.1,1.8.4.1,1.8.4.2|text|no|Stationary equation quadratic in e^x; exact log inputs and second-derivative nature without premature rounding
11|Try Now 13|1|494|2.4.1.1,2.4.2.1,1.8.4.1,1.8.4.2|text|no|Exact stationary coordinates and maximum/minimum for linear times exponential
11|Try Now 13|2|494|2.4.1.2,2.4.2.1,1.8.4.1|text|no|Stationary input for x times negative-slope exponential
11|Try Now 13|3|494|2.4.1.2,2.4.2.2,1.8.4.1|text|no|Stationary coordinates for exponential over x, excluding x0
11|Try Now 13|4|494|2.4.1.1,2.4.2.1,1.8.4.1,1.8.3.1|text|no|Show specified stationary input then tangent at a different input; other stationary inputs are not requested
'''

YM += '''
11|Example|14|495|2.4.1.1,2.4.1.2,2.2.1.2|text|no|Log derivative via expansion versus chain; ln(3x^2) has both nonzero sign components, preserve domain
11|Try Now|14|496|2.4.1.1,2.4.1.2,2.2.1.2|text|no|Six natural logs of powers or quotients; log-law simplification with actual positive-argument domain
11|Example|15|496|2.4.1.2,2.2.1.2|text|no|Natural log of affine expression or its square root; alternate log-law derivative
11|Try Now|15|497|2.4.1.2,2.2.1.2|text|no|Six logs with shifts,square,root,nested log and5x-ln x; domain-aware chain differentiation
11|Example|16|497|2.4.1.1,2.4.1.2,2.4.2.1,2.4.2.2|text|no|Nested-log product, shifted-log quotient and exponential equation rearranged before differentiation
11|Try Now|16|498|2.4.1.1,2.4.1.2,2.4.2.1,2.4.2.2,2.2.1.2|text|no|Log products/quotients, rearranged e^y and log of rational factors; keep original positive quotient domain
11|Example|17|498|2.4.1.1,2.4.2.1,1.8.4.1,1.8.4.2|text|no|Exact stationary coordinates in e and second-derivative minimum for x ln x
11|Try Now 17|1|498|2.4.1.1,2.4.1.2,1.8.4.1,1.8.4.2|text|no|Logarithmic derivative sum yields stationary input then second derivative determines nature
11|Try Now 17|2|498|2.4.1.2|text|no|Gradient of exponential minus shifted log at supplied x
'''

YM += '''
11|Example|18|501|2.4.1.1,2.4.1.2,2.4.2.1,2.4.2.2|text|no|Basic trig, polynomial product,trig quotient and power composite derivatives in radians
11|Try Now 18|1|501|2.4.1.1,2.4.1.2,2.4.2.1,2.4.2.2|text|no|Six trig derivatives of sums,products,quotients and composites
11|Try Now 18|2|501|2.4.1.2|text|no|Powers of sine,cosine and shifted cosine through chain rule
11|Try Now 18|3|501|2.4.1.1,2.4.2.2,2.3.1.1|text|no|Show quotient derivative expressed as a cot x+b x cosec squared x; reciprocal rewriting is allowed
11|Example|19|502|2.4.1.2,2.4.2.1|text|no|Contrast constant times cos2x with x times cos2x; inner2 and product rule
11|Try Now|19|502|2.4.1.2,2.4.2.1,2.4.2.2,2.3.1.1|text|no|Nine trig derivatives including polynomial products,squared tangent and reciprocal functions. Derive reciprocal derivatives from sin/cos rather than require extra memorised formulae
'''

YM += '''
11|Example|20|503|2.4.1.2,2.4.2.2,2.3.1.1|text|no|Shifted/multiple-angle derivatives, quotient and sine-power chain; reciprocal simplification optional
11|Try Now 20|1|503|2.4.1.2,2.4.2.1,2.3.1.1|text|no|Six affine-angle trig composite/power/product derivatives in radians
11|Try Now 20|2|503|2.4.1.1,2.4.1.2,2.4.2.1,2.4.2.2|text|no|Exponential of cosine,exponential-sine product,log of sine and cosine/exponential quotient
11|Example|21|504|2.4.1.1,2.4.2.1,1.8.3.1|graph|no|Given x sin x curve and Q(pi/2,pi/2), show normal passes through(pi,0). Graph indicates interval,curve and Q; analytic proof still required
11|Try Now 21|1|504|2.4.1.1,2.4.1.2|text|no|Gradient of sine plus tan2x at0
11|Try Now 21|2|504|2.4.1.1,2.4.1.2|text|no|Gradient of mixed-frequency cosine/sine at given radian point
11|Try Now 21|3|504|2.4.1.1,2.4.1.2,1.8.3.1|text|no|Tangent for mixed-frequency trig curve with m,c rounded3sf
11|Example|22|505|2.4.1.2,2.4.2.2,2.3.2.3,1.8.4.1,1.6.6.1,1.6.6.2|text|no|Show simplified trig quotient derivative using double angle then solve stationary cosine quadratic on negative-to-positive radian interval
11|Try Now 22|1|506|2.4.1.1,1.8.4.1,1.8.4.2,1.6.6.1,1.6.6.2|text|no|Stationary inputs and nature for x+2cos x over full radian turn
11|Try Now 22|2|506|2.4.1.1,1.8.4.1,1.6.6.1,1.6.6.2|text|no|Stationary full coordinates for2x-tan x across interval centred on0, excluding poles
11|Try Now 22|3|506|2.4.1.2,1.8.4.1,1.6.6.1,1.6.6.2|text|no|Half-angle tangent plus sine derivative,stationary coordinates in restricted second half-turn
11|Example|23|506|2.4.1.2,2.4.2.2,1.8.4.1,1.6.6.1,1.6.6.2|text|no|Trig/exponential quotient stationary input with exact special angle
11|Try Now|23|506|2.4.1.2,2.4.2.2,1.8.4.1,1.6.6.1,1.6.6.2|text|no|Exponential/trig reciprocal quotient stationary exact input; exclude sine zeros in stated interval
'''

YM += '''
11|Example|24|507|2.4.3.1|text|no|Implicit circle derivative, collecting chain-factor dy/dx; exclude vertical-tangent denominator
11|Try Now|24|507|2.4.3.1|text|no|Two implicit quadratic curves differentiated and rearranged
11|Example|25|508|2.4.3.1,2.4.2.1|text|no|Implicit quadratic with xy mixed product, collect both derivative terms
11|Try Now|25|508|2.4.3.1,2.4.2.1|text|no|Three implicit polynomial curves with mixed products and powers
11|Example|26|508|2.4.3.1,2.4.2.1,2.4.1.1|text|no|Implicit x ln y derivative with y>0; equation excludes x0
11|Try Now|26|508|2.4.3.1,2.4.2.1,2.4.1.2|text|no|Three implicit logarithmic curves including ln(xy); preserve each original positive argument
11|Example|27|509|2.4.3.1,2.4.2.1,2.4.1.2|text|no|Implicit sine of xy requires outer chain and inner product rule
11|Try Now|27|509|2.4.3.1,2.4.2.1,2.4.1.2|text|no|Two mixed trig/log implicit derivatives, with variable y inside sine or cosine
11|Example|28|509|2.4.3.1,2.4.2.1,2.4.1.2|text|no|Two exponential-y products, collect and simplify implicit derivative
11|Try Now|28|509|2.4.3.1,2.4.2.1,2.4.1.2|text|no|Implicit exponential products combined with polynomial y terms
11|Example|29|510|2.4.3.1,2.4.3.3,2.4.2.1|text|no|Implicit cubic derivative then gradient at valid given point
11|Try Now 29|1|510|2.4.3.1,2.4.3.3,2.4.1.1|text|no|Gradient of implicit log curve at given point
11|Try Now 29|2|510|2.4.3.1,2.4.3.3,2.4.1.2,2.4.2.1|text|no|Gradient of implicit trig curve at radian point
11|Try Now 29|3|510|2.4.3.1,2.4.3.3,2.4.1.2,2.4.2.1|text|no|Implicit exponential curve gradient at valid given point
11|Try Now 29|4|510|2.4.3.1,2.4.3.3|text|no|Show implicit derivative then combine gradient relation with curve to find both full points
'''

YM += '''
11|Example|30|511|2.4.3.1,2.4.3.3,1.8.4.1|text|no|Implicit quadratic,horizontal tangent relation then substitution for both points
11|Try Now|30|511|2.4.3.1,2.4.3.3,1.8.4.1|text|no|Show implicit derivative then find both horizontal-tangent coordinates
11|Example|31|512|2.4.3.1,2.4.3.3,1.8.3.1,1.8.4.1|text|no|Implicit tangent in integer general form,then prove no stationary point by impossible real square
11|Try Now 31|1|512|2.4.3.1,2.4.3.3,1.8.4.1|text|no|Prove implicit cubic/product curve has no horizontal stationary point,checking original relation
11|Try Now 31|2|512|2.4.3.1,2.4.3.3,2.4.1.1,1.8.3.1|text|no|Implicit log curve normal at given point in integer general form
11|Example|32|514|2.4.3.2|text|no|Parametric polynomial derivative via ratio,undefined at t0 due vertical tangent
11|Try Now|32|514|2.4.3.2|text|no|Two polynomial parametric derivatives; part(a) degenerates at t0 and needs limit or parameter restriction
11|Example|33|514|2.4.3.2,2.4.1.2|text|no|Parametric shifted-log and reciprocal derivative, t<1/2 and t!=0
11|Try Now|33|514|2.4.3.2,2.4.1.2|text|no|Two log/root/reciprocal parameter pairs; infer simultaneous real domains and parameter exclusions
'''

YM += '''
11|Example|34|515|2.4.3.2,2.4.1.2,2.4.2.1|text|no|Show parametric derivative for two exponentials, one with quadratic multiplier
11|Try Now|34|515|2.4.3.2,2.4.1.2,2.4.2.1|text|no|Four exponential/log parametric ratios, including product differentiation and t>3 log domain
11|Example|35|515|2.4.3.2,2.4.1.1,2.3.1.1|text|no|Parametric tan/sec ratio simplifies to sin theta on original non-pole domain; reciprocal derivative can be derived
11|Try Now|35|516|2.4.3.2,2.4.1.1,2.4.1.2|text|no|Two trig parametric ratios with explicit denominator/pole checks
11|Example|36|516|2.4.3.2,2.4.1.2,2.3.2.3|text|no|Multiple-angle and squared-sine parametric derivative, use double-angle identity to simplify
11|Try Now 36|1|516|2.4.3.2,2.4.1.2|text|no|Two mixed linear/multiple-angle trig parametric derivatives
11|Try Now 36|2|516|2.4.3.2,2.4.1.2,2.3.2.3|text|no|Double-angle ratio simplifies on open interval with cos theta!=0
11|Example|37|517|2.4.3.2,2.4.3.3,2.4.1.2,2.3.2.3|text|no|Parametric gradient at1radian,then vertical-tangent condition on quadrant1 parameter domain
11|Try Now 37|1|517|2.4.3.2,2.4.3.3|text|no|Prove dx/dt always positive,so no vertical tangent; distinguish numerator and denominator tests
11|Try Now 37|2|518|2.4.3.2,2.4.3.3,2.4.1.2,2.3.2.3,1.8.3.1|text|no|Show derivative cot theta,then tangent at pi/4 and both horizontal-tangent coordinates over0..2pi
11|Example|38|518|2.4.3.2,2.4.3.3,2.4.1.2,2.2.3.1|text|no|Parametric exponential ratio, solve supplied gradient exactly in natural logs
11|Try Now 38|1|518|2.4.3.2,2.4.3.3,2.4.1.2|text|no|Log/polynomial parametric gradient condition with t>1 rejects extraneous t0; find full point
11|Try Now 38|2|518|2.4.3.2,2.4.3.3,2.4.1.2,2.3.2.3|text|no|Trig parametric gradient condition, interval chooses cosine root,then full point
'''

YM += '''
11|Example|40|521|2.4.3.2,2.4.3.3,2.4.1.2,2.3.2.3,1.8.4.1|graph|no|Labelled loop graph identifies which stationary point and axis crossing; show derivative,find both stationary parameters3dp and exact gradient at specified crossing
'''

YM += '''
12|Example|1|530|2.5.1.1|text|no|Three affine-exponential indefinite integrals,including negative inner slopes and constants
12|Try Now|1|530|2.5.1.1|text|no|Four indefinite exponential forms including simplify numerator over exponential first
12|Example|2|530|2.5.1.1,1.9.3.1|text|no|Two definite exponential integrals,one with exact logarithmic endpoint
12|Try Now 2|1|531|2.5.1.1,1.9.3.1|text|no|Three definite exponentials including expand square of two exponential terms before integration
12|Try Now 2|2|531|2.5.1.1,1.9.3.1|text|no|Show exact definite integral after expanding(e^x+1)^2
12|Try Now 2|3|531|2.5.1.1,1.9.3.1|text|no|Exact definite integral with exponential affine argument
12|Try Now 2|4|531|2.5.1.1,1.9.3.1,1.9.3.2|text|no|Finite upper parameter then deduce simple convergent improper exponential integral
12|Example|3|531|2.5.1.1,1.9.3.1,2.2.1.2|text|no|Symmetric parameter limits and given definite value,show logarithmic rearrangement rather than run iteration
12|Try Now 3|1|531|2.5.1.1,1.9.3.1,2.2.1.2|text|no|Asymmetric parameter limits,show supplied logarithmic rearrangement
12|Try Now 3|2|531|2.5.1.1,1.9.3.1,2.2.1.2|text|no|Expand squared shifted exponential,integrate then show specified logarithmic rearrangement
12|Try Now 3|3|531|2.5.1.1,1.9.3.1,2.2.3.1|text|no|Use given definite integral to solve upper bound numerically3sf
12|Example|4|532|2.5.1.1,1.9.2.1,1.9.2.2|text|no|Recover curve by twice integrating exponential second derivative with independent gradient and point conditions
12|Try Now 4|1|532|2.5.1.1,1.9.2.1,1.9.2.2|text|no|Recover curve from derivative sum of exponentials and point
12|Try Now 4|2|532|2.5.1.1,1.9.2.1,1.9.2.2|text|no|Recover curve from exponential first derivative with signs and point condition
12|Try Now 4|3|532|2.5.1.1,1.9.2.1,1.9.2.2|text|no|Twice integrate exponential with gradient-at0 and exact point; keep separate constants
'''

YM += '''
12|Example|6|534|2.5.1.1|text|no|Three reciprocal-linear primitives with explicit intervals supporting non-absolute log form
12|Try Now|6|535|2.5.1.1|text|no|Integrate reciprocal-linear forms and state validity intervals; log absolute form permits each connected non-pole branch
12|Example|7|535|2.5.1.1,1.9.1.2|text|no|Expand squared numerator and divide by x squared to combine power and logarithmic primitives
12|Try Now|7|535|2.5.1.1,1.9.1.2|text|no|Three rational expressions simplified into powers and1/x before integration
12|Example|8|535|2.5.1.1,1.9.3.1|text|no|Two reciprocal-linear definite integrals; part(b) crosses an interior pole and is not a valid finite integral
12|Try Now|8|536|2.5.1.1,1.9.3.1|text|no|Three definite reciprocal-linear combinations,including negative denominator with no pole in interval
12|Example|9|536|2.4.1.2,2.5.1.1,1.9.3.1,2.1.1.1|text|no|Differentiate shifted log,hence reciprocal integral,divide quadratic by linear and hence show exact mixed integral
'''

YM += '''
12|Example|11|538|2.5.1.2|text|no|Basic affine-angle sine/cosine/sec-squared primitives in radians
12|Try Now|11|538|2.5.1.2|text|no|Three basic multiple/fractional-angle trig primitives
12|Example|12|539|2.5.1.2,2.5.2.1|text|no|Rewrite tangent squared using sec squared,and reciprocal cosine squared before integrating
12|Try Now|12|539|2.5.1.2,2.5.2.1|text|no|Tangent-squared double angle and mixed polynomial/reciprocal cosine squared
12|Example|13|539|2.5.1.2,1.9.1.2|text|no|Mixed power and shifted-angle sine/sec-squared primitives, including negative inner slope
12|Try Now|13|539|2.5.1.2,1.9.1.2|text|no|Two mixed root/constant plus affine-cosine primitives
12|Example|14|540|2.5.1.2,2.5.2.1,2.5.2.2|text|no|Use double-angle identities before integrating cosine squared or sine-squared triple argument
12|Try Now|14|540|2.5.1.2,2.5.2.1,2.5.2.2|text|no|Four squared/fourth-power trig integrals; repeated double angle handles fourth power without introducing a new memorised formula
12|Example|15|540|2.5.1.2,2.5.2.1,2.5.2.2,1.9.3.1,1.6.3.1|text|no|Exact bounded mixed squared-cosine and double-sine integral, special-angle endpoint values
12|Try Now 15|1|540|2.5.1.2,1.9.3.1,1.6.3.1|text|no|Exact sine/cosine definite integral across quarter-turn
12|Try Now 15|2|540|2.5.1.2,1.9.3.1,1.6.3.1|text|no|Exact double cosine plus sine integral to pi/6
12|Try Now 15|3|540|2.5.1.2,1.9.3.1,1.6.3.1|text|no|Exact sine double angle plus sec squared integral to pi/3,no poles crossed
12|Try Now 15|4|540|2.5.1.2,2.5.2.1,1.9.3.1|text|no|Show exact symmetric integral of constant plus tangent squared after identity
12|Example|16|541|2.5.1.2,2.5.2.1,2.5.2.2,1.9.3.1|text|no|Expand squared sine-cosine sum and apply double angles,then exact definite value
12|Try Now 16|1|541|2.5.1.2,2.5.2.1,2.5.2.2,1.9.3.1|text|no|Show identity for tan squared plus cos squared,then exact integral
12|Try Now 16|2|541|2.5.1.2,2.5.2.1,2.5.2.2,1.9.3.1|text|no|Show sine-squared cosine-squared identity at4x,then exact short-interval integral
12|Try Now 16|3|541|2.3.2.2,2.3.2.3,2.5.1.2,2.5.2.1,1.9.3.1|text|no|Derive triple-sine identity from compound/double angle,then integrate sine cubed using that identity
'''

YM += '''
12|Example|17|542|2.4.2.2,2.4.1.1,2.5.1.3,2.5.2.1,2.3.1.1,2.3.2.3,1.9.3.1|text|no|Derive cotangent derivative from quotient,hence integrate transformed cot-squared or reciprocal double-angle form; no extra memorised primitive assumed
12|Try Now 17|1|543|2.4.1.2,2.5.1.2,2.5.2.1,2.3.2.3,1.9.3.1|text|no|Differentiate tan2x,hence integrate sec-squared2x,then separately tan-squared x and reciprocal1+cos4x on valid interval
12|Try Now 17|2|543|2.4.1.1,2.4.2.2,2.5.1.3,2.5.2.1,2.3.1.1,1.9.3.1|text|no|Prove reciprocal identities,derive secant derivative,then reverse derivative to integrate1/(1-sin x) on0..pi/4
12|Try Now 17|3|543|2.4.1.1,2.4.2.2,2.4.2.1,2.5.1.3,2.5.2.1,1.9.3.1|text|no|Derive first and second secant derivatives,then exact transformed integral using derived primitive
'''

# Rendered Goldie worked examples: chapter|number|PDFpage|continuations|demand aliases|given|sketch|scope|individual note.
GOLDIE_WORKED = ''

GOLDIE_WORKED += '''
1|1|16|||text|no|in-scope|Polynomial addition is prerequisite arithmetic/supporting practice; no direct 138-demand coverage is claimed
1|2|17|||text|no|in-scope|Polynomial subtraction/sign handling is prerequisite arithmetic; no direct 8227 assessed-demand coverage
1|3|17|18||text|no|in-scope|Multiply cubic by quadratic using columns or expansion. Supporting algebra,not a polynomial-division demand; degree5 product does not invoke dividend LIMIT05
1|4|18|19|2.1.3.1,2.1.3.3|text|no|in-scope|Cubic divided by linear with zero remainder; long division,coefficient comparison and inspection alternatives. Later p20reference is not a second question
'''

GOLDIE_WORKED += '''
1|5|21|22|2.1.4.2,2.1.4.4|text|no|in-scope|Solve cubic using trial exact roots and factorisation; graph/table are worked-method aids rather than givens
1|6|23||1.3.1.1,2.1.4.2,2.1.4.4,1.3.5.1|text|yes|in-scope|Evaluate cubic at supplied inputs,identify factors,solve all roots,then sketch cubic with intercepts
'''

GOLDIE_WORKED += '''
1|7|24||2.1.4.2,2.1.3.1,2.1.4.4|text|no|in-scope|Show given linear factor,divide cubic,solve remaining quadratic with irrational roots
1|8|25||2.1.4.2|text|no|in-scope|Find one integer cubic root by testing divisors of constant; constrained root-search supporting factor-theorem use
1|9|25|||text|no|in-scope|Show no integer root by finite divisor tests; supporting root-search reasoning,not full examination-demand coverage or general rational-root theorem requirement
1|10|25|26|2.1.4.2,2.1.4.3|text|no|in-scope|Two given linear factors including nonmonic divisor determine two coefficients by simultaneous substitutions
1|11|27||2.1.4.1|text|no|in-scope|Remainder on division by x+1 from f(-1)
1|12|27||2.1.4.1,2.1.4.3|text|no|in-scope|Given remainder under nonmonic linear divisor determines constant coefficient
1|13|27||2.1.3.2,2.1.3.3|text|no|in-scope|Quartic divided by quadratic,remainder is a linear polynomial,not a scalar evaluation
'''

GOLDIE_WORKED += '''
1|14|32||2.1.1.1,2.1.2.1|text|yes|in-scope|Sketch straight line,its modulus and translated modulus on separate axes; integer modulus coefficients meet QUAL01
1|15|33||2.1.1.3|text|no|in-scope|Three inside/outside modulus inequalities including rearrangement of constant minus absolute value;and/or intervals
'''

GOLDIE_WORKED += '''
1|16|34||2.1.1.1,2.1.1.3|text|no|in-scope|Reverse interval-to-modulus representation; recover midpoint a and radius b from two endpoints
1|17|34||2.1.1.3|text|no|in-scope|Linear expression versus absolute expression inequality; graph is worked-method aid,not a given or requested sketch
1|18|35||2.1.1.2,2.1.1.3|text|no|in-scope|Equal moduli then modulus inequality by squaring or shared graph; two intersections bound inside interval
'''

GOLDIE_WORKED += '''
2|2|43||2.2.1.1|text|no|in-scope|Exact base2 logs of powers,fraction,one and square root; verify exponential-log inverse
2|3|44||2.2.3.1,2.2.1.2|text|no|in-scope|Solve2^n=1000 by taking common logarithms and isolating exponent; not a request for change-of-base formula
2|4|45||2.2.3.1,2.2.1.2|text|no|in-scope|Quadratic in3^x,reject negative exponential root then common-log numerical exponent
2|5|45||1.2.3.2,2.2.3.2,2.2.1.2|text|no|in-scope|Geometric-sequence least integer index exceeds threshold; exponential inequality and adjacent-index confirmation
'''

GOLDIE_WORKED += '''
2|1|40|41|2.2.2.2,1.3.5.1|text|yes|in-scope|Given exponential cost model,evaluate initial value,state limiting cost and sketch shifted decay;graph facet only,not full inverse-demand coverage
2|6|51|||table|yes|in-scope|Plot nearly linear temperature data and fit straight line; supporting coordinate/graph practice with no logarithmic linearisation demand
2|7|52|53|2.2.4.1|table|yes|in-scope|Explain logarithmic linearisation,plot transformed pipe-flow data,fit power-law parameters; source axes wording conflicts with worked graph
2|8|53|54,55|2.2.4.1|table|yes|in-scope|Plot cooling data,choose log-temperature versus time,fit exponential decay parameters from transformed straight line
'''

GOLDIE_WORKED += '''
2|9|63|64|2.2.2.1,2.2.2.2,2.2.3.1|text|yes|in-scope|Sketch supplied natural-exponential population model,evaluate future population and solve threshold time; graph-properties facet only
2|10|64|65|2.2.2.1,2.2.2.2,2.2.3.1|text|yes|in-scope|Sketch natural-exponential decay,initial mass,unit conversion for one hour and solve half-life with definition supplied
2|11|65||2.2.1.2,2.2.2.1|text|no|in-scope|Make p subject of ln p-ln(1-p)=t; preserve0<p<1 and logistic-form equivalence
2|12|66||2.2.1.2,2.2.3.1|text|no|in-scope|Log shifted-argument equation and quadratic in e^x; enforce x>4 in first and positive e^x in second
'''

GOLDIE_WORKED += '''
3|1|73||2.3.1.1,1.6.3.1|text|no|in-scope|Exact cosecant120degrees in surd form from reciprocal sine and related special angle
3|2|73|74|2.3.2.1,1.6.5.2,1.6.6.1,1.6.6.2|text|no|in-scope|Sec-squared/tangent equation reduced by identity to tangent quadratic; all four degree roots
3|3|78||2.3.2.2|text|no|in-scope|Recognise cosine-sum pattern in reverse for theta and3theta; no numerical solving
'''

GOLDIE_WORKED += '''
3|4|83||2.3.2.3,1.6.5.2,1.6.6.1,1.6.6.2|text|no|in-scope|Double-sine equation,factor rather than cancel sine,retain zero family and both inclusive degree endpoints
3|5|84||2.3.2.3,1.6.5.2,1.6.6.1,1.6.6.2|text|no|in-scope|Choose cosine double-angle variant giving sine quadratic,reject impossible ratio,and exact radian boundary-root set
'''

GOLDIE_WORKED += '''
3|6|87|88,89|2.3.2.4,1.6.2.1,1.6.2.3,1.6.6.1,1.6.6.2|text|yes|in-scope|R sine difference with exact special-angle phase,extrema,restricted sketch and bounded exact roots; worked sketch extends beyond requested0..2pi,so clip adaptation to its stated domain
'''

GOLDIE_WORKED += '''
4|1|99||2.4.2.1|text|no|in-scope|Explicitly use product rule on linear times quadratic; expanded power derivative is checked as an alternative method,not replacement for method instruction
4|2|99||2.4.2.1,1.8.2.2|text|no|in-scope|Product and chain rule for20x(x-1)^6; factor derivative for later stationary work without claiming stationary points were assessed
4|3|101||2.4.2.2|text|no|in-scope|Explicit quotient-rule derivative of linear over linear simplifies to constant numerator
4|4|101||2.4.2.2|text|no|in-scope|Explicit quotient-rule derivative of quadratic over linear; retain denominator exclusion
'''

GOLDIE_WORKED += '''
4|5|105||2.4.1.2|text|no|in-scope|Affine exponential derivative by chain rule with explicit inner variable
4|6|105||2.4.1.2|text|no|in-scope|Reciprocal exponential rewritten as negative exponent before differentiation
4|7|106||2.4.1.2|text|no|in-scope|Exponential of quadratic with external multiplier,nonlinear chain
4|8|106||2.4.1.1,2.4.1.2|text|no|in-scope|Log multiple versus log of multiple; inner factor cancels in latter derivative
4|9|107||2.4.1.2,2.2.1.2|text|no|in-scope|Log of fourth power versus shifted square; preserve both nonzero real components for ln(x^4)
4|10|107||2.4.1.1,2.4.2.2|text|no|in-scope|Natural log over x derivative by quotient rule
'''

GOLDIE_WORKED += '''
4|11|112||2.4.1.2|text|no|in-scope|Cosine of doubled argument,chain-rule inner factor
4|12|112||2.4.1.1,2.4.2.1|text|no|in-scope|Polynomial times sine product-rule derivative
4|13|113||2.4.1.2|text|no|in-scope|Exponential of tangent,chain rule with sec-squared inner derivative
4|14|113||2.4.1.1,2.4.2.2,1.6.5.1|text|no|in-scope|Quotient of shifted sine and cosine; simplify via Pythagorean identity after differentiating
'''

GOLDIE_WORKED += '''
4|15|116||2.4.3.1,2.4.2.1,2.4.1.1|text|no|in-scope|Differentiate isolated implicit-y terms with respect to x,including mixed power product and sine y; precursor to whole implicit equation
4|16|116|117|2.4.3.1,2.4.3.3,2.4.2.1,1.8.3.1|text|no|in-scope|Implicit cubic/product derivative,then gradient and tangent at given valid point
4|17|118||2.4.3.1,2.4.3.3,2.4.2.1,1.8.4.1|text|no|in-scope-parts-only|Implicit folium stationary coordinates; origin is singular and needs branch analysis rather than denominator-free stationary test; nonsingular point remains valid
'''

GOLDIE_WORKED += '''
4|18|119|120|2.4.3.1,2.4.3.3,2.4.1.1,1.8.4.1,1.8.4.2|graph|no|in-scope|Given implicit trig closed curve on0..pi,find stationary coordinates,verify four given test points/gradients and infer maximum/minimum from local signs
'''

GOLDIE_WORKED += '''
4|19|124|||text|yes|in-scope|Parametric coordinate table,plot and asymptotic limit; prerequisite parametric representation,not direct derivative coverage
4|20|125|||text|yes|in-scope|Parametric coordinate table,loop sketch and admissible x for bounded t; prerequisite representation,not direct derivative. Stated parameter interval gives0<=x<=4,not merely x>=0
4|21|126|||text|no|in-scope|Eliminate t from polynomial pair; prerequisite parametric/Cartesian conversion,not an assessed derivative
4|22|126|127|2.4.3.2,2.4.3.3,1.8.3.1|text|yes|in-scope|Parametric derivative,general and specified tangent,eliminate parameter and sketch parabola with tangent; t0 vertical tangent needs separate treatment
'''

GOLDIE_WORKED += '''
4|23|127|128|2.4.3.2,2.4.3.3,2.4.1.1,1.8.3.1|text|yes|in-scope|Parametric ellipse derivative,general and specified normal,point coordinates and sketch with normal; use general line form to handle exceptional horizontal/vertical normals
4|24|129||2.4.3.2,2.4.3.3,1.8.4.1,1.8.4.2|text|no|in-scope|Stationary coordinates of monotone-linear-x parametrisation,classify from derivative signs in x order rather than parameter order blindly
'''

GOLDIE_WORKED += '''
5|1|136||2.5.1.1,1.9.3.1|text|no|in-scope|Affine exponential indefinite primitive and definite numerical value
5|2|136||2.5.1.1,1.9.3.1|text|no|in-scope|Definite reciprocal x integral with constant multiplier and positive interval
5|3|137||2.5.1.1,1.9.3.1|text|no|in-scope|Reciprocal affine definite integral,inner-slope factor and3sf value
5|4|138||2.5.1.1,1.9.3.1|text|no|in-scope|Reciprocal negative denominator on connected non-pole interval; absolute-log or sign-extraction alternatives. Adjacent139explicitly forbids integrating across pole
'''

GOLDIE_WORKED += '''
5|5|143||2.5.1.2|text|no|in-scope|Three basic trig primitives,including shifted cosine and scaled angle
5|6|143||2.5.1.2,1.9.3.1,1.6.3.1|text|no|in-scope|Exact mixed-frequency sine/cosine definite integral with special-angle endpoints
5|7|144||2.5.2.1,2.5.2.2,2.5.1.2|text|no|in-scope|Choose double-angle identity before integrating sine squared
5|8|144|145|2.5.2.1,2.5.2.2,2.5.1.2|text|no|in-scope|Repeat double-angle reduction to integrate cosine fourth power; no memorised general reduction formula
'''

GOLDIE_WORKED += '''
6|1|160|161|2.6.1.2|text|no|in-scope|Show root in specified interval by either opposite LHS/RHS ordering or sign change of continuous difference; both methods are explicit
'''

GOLDIE_WORKED += '''
10|1|250||1.7.4.1,1.7.5.1|text|no|in-scope|Find magnitude and direction relative to horizontal for2Dvector; solution triangle only. Polar answer pair must not be confused with Cartesian components
10|2|252||1.7.3.3,1.7.3.2,1.7.2.1,1.7.2.3|text|no|in-scope|Position and displacement column vectors from given points,then interpret equal vectors as parallel equal-length directed segments
10|3|253||1.7.4.1|text|no|in-scope|Magnitude of3Dcolumn vector from three squared components
'''

GOLDIE_WORKED += '''
10|4|256||1.7.2.1|text|no|in-scope|Add two2Dcomponent vectors; geometrical triangle/parallelogram drawing appears in worked solution only
10|5|257||1.7.2.1,1.7.2.3|text|yes|in-scope|Subtract2Dvectors and explicitly draw a,b and a-b; direction and shared endpoints are credited visual features to retain
'''

GOLDIE_WORKED += '''
10|6|258|259|1.7.2.1,1.7.2.2,1.7.2.3|diagram|no|in-scope|Read regular hexagonal prism labels and given edge vectors,express eight directed segments via geometry and vector paths
10|7|260|261|1.7.3.1,1.7.3.2,1.7.4.1,1.7.2.1|text|no|in-scope|3Dposition vectors,derive directed displacement,normalise in stated direction and sum triangle side magnitudes for perimeter
10|8|261||1.7.2.3,1.7.3.3,1.7.2.1,1.7.2.2|diagram|no|in-scope|Triangle diagram and internal division2:3; express position vector by weighted endpoints,not scalar lengths alone
'''

GOLDIE_WORKED += '''
10|9|265||1.7.4.1,1.7.4.2,1.7.5.1|text|no|in-scope|Find obtuse angle between two nonzero2Dcolumn vectors via scalar product and magnitudes; direction signs matter
'''

GOLDIE_WORKED += '''
10|10|266||1.7.4.2,1.7.5.2|text|no|in-scope|Show two nonzero vectors perpendicular through zero scalar product
10|11|267|268|1.7.3.2,1.7.4.1,1.7.4.2,1.7.5.1|text|no|in-scope|3Dpoint angle at named vertex; choose both displacement vectors from vertex then scalar product rather than supplement
'''

# Headingless prompts/activities are retained in the same inventory,not a parallel bank.
GOLDIE_OTHER = '''
1|Prompt|1|15|||text|no|in-scope|Taxicab1729two sums of positive cubes; enrichment/prerequisite exploration,not direct8227demand coverage
1|Prompt|2|31||2.1.1.1|text|no|in-scope|Evaluate modulus at positive/negative input and contrast modulus of sums with sum of moduli; displayed basic modulus graph is teaching support
2|Prompt|1|38||1.2.3.2,1.2.3.3,2.2.3.1|text|no|in-scope|Idealised daily cell doubling,calculate two population terms and solve approximate million-cell threshold;model assumptions are explicitly given
2|Activity|1|39||2.2.2.2,2.6.1.1|graph|yes|in-scope-parts-only|Given2^x and x^2 graph,find intersections/inequality intervals;plot3^x/x^3and4^x/x^4. General-all-a claims need base-domain conditions; supporting exploration beyond simple supplied-model evaluation
'''

GOLDIE_OTHER += '''
2|Activity|3|46||2.2.2.2,1.3.5.1|text|yes|in-scope|Plot log2 x from specified powers then read sqrt2 by inverse graphical lookup; graph facet of log/exponential demand
2|Prompt|2|47||2.2.2.2,2.2.1.1|graph|no|in-scope|Justify five labelled logarithm-graph properties using prior log/indices knowledge; diagram shows intercept,domain,asymptote and point(a,1),a>1
2|Prompt|3|59|||diagram|no|in-scope|Explain power-rule exclusion n=-1 for area under1/x; prerequisite/supporting concept,not claiming evaluated-integral coverage
2|Activity|4|59|||text|no|in-scope|Numerically estimate three reciprocal areas and conjecture log-product relation; no specific quadrature method is required,so do not count as assessed trapezium-rule evidence
2|Activity|5|60|||text|yes|out-of-scope|Derive logarithm product rule from integral definition using general change of variable x=az. Formal substitution proof exceeds prescribed8227 methods; retain as explanatory enrichment only
2|Activity|6|60|||text|no|in-scope-parts-only|Explore properties of integral-defined L resembling logarithms. Retain conceptual laws as supporting evidence; formal integral-law derivations are not prescribed direct assessment
'''

GOLDIE_OTHER += '''
2|Activity|7|61|||diagram|no|in-scope|Technology-assisted search for e from area of1/x equal1. Supporting natural-log meaning; no prescribed numeric algorithm supplied and no direct iteration/trapezium credit inferred
3|Prompt|1|71||1.6.2.1|diagram|no|in-scope-parts-only|Wave-photo amplitude estimate and suitable sine-model parameters,then critique fit. Photo has no metric scale,so metre estimates and wavelength assumptions require explicit calibration; schematic defines amplitude/period only
'''

GOLDIE_OTHER += '''
3|Prompt|2|76||2.3.2.2|diagram|no|in-scope-parts-only|Identify assumptions in area-of-triangle proof of compound-sine formula; drawn acute triangle and altitude position do not themselves prove all angle cases. Supporting proof-method analysis,not a new universal formula demand
3|Activity|2|76|77|2.3.2.2|text|no|in-scope|Derive cosine sum/difference and tangent sum/difference from sine formula via complementary/negative-angle substitutions and quotient; all tangent components need defined domains
3|Prompt|3|77||2.3.2.2,1.6.3.1|text|no|in-scope|Ask whether compound formulae valid for all angles,then test60/30; distinguish a numerical test from proof and recognise denominator restrictions
3|Prompt|4|81|||text|no|in-scope|Compare checking a result with proving it while reading double-angle derivations. Supporting proof literacy; does not by itself assess identity-versus-equation syllabus demand
'''

GOLDIE_OTHER += '''
4|Prompt|1|97|||text|no|in-scope|Suggest contexts needing non-polynomial derivatives. Supporting modelling brainstorm,no calculative directly assessed demand
4|Activity|1|101||2.4.2.2|text|no|in-scope|Verify quotient rule on x^10/x^7 against simplified x^3; compare method results and preserve x!=0
4|Prompt|2|106||2.2.2.2,2.2.1.2|text|no|in-scope|Explain why ln3x and ln x have same derivative and relate graph shapes over x>0; log-law translation explanation,not new inverse coverage
4|Prompt|3|117||1.3.1.1|graph|no|in-scope|Use given implicit-curve plot to explain failure of single-valued y as function of x; vertical-line evidence,not one-one/inverse classification
4|Prompt|4|123|||graph|no|out-of-scope|Where a two-rod ride produces greatest sensations requires a physical acceleration/force model beyond prescribed8227 derivative demand. Keep labelled parametric path as teaching illustration,no direct coverage credit
'''

GOLDIE_OTHER += '''
5|Prompt|1|135|||diagram|no|in-scope|Suggest method to estimate bird count in photograph. Supporting estimation/context only,no assumed integration or statistical-density assessment
5|Investigation|1|142|||text|no|out-of-scope|Derive infinite power series for e^x from derivatives and use it to approximate e; Taylor/Maclaurin series are not prescribed8227content
5|Investigation|2|142||1.2.3.2,1.2.3.3|text|no|in-scope-parts-only|Compare lump interest,annual and half-year compound returns,then explore continuous-payment limit. Finite GP modelling in scope; formal derivation of continuous-compounding limit is enrichment
'''

GOLDIE_OTHER += '''
5|Activity|1|137|138||graph|no|in-scope-parts-only|Compare areas under reciprocal curve on reflected non-pole intervals and prove relation. Sign/area symmetry useful as supporting evidence; printed proof uses general substitution beyond required8227method
5|Prompt|2|139||1.3.2.1|text|no|in-scope|Identify rational-function discontinuities and prove quadratic has no real-domain exclusions; distinguish holes/poles from a denominator-zero test alone
5|Problem-solving investigation|1|156|157|2.5.4.2|graph|yes|in-scope-parts-only|Critique three universal claims about left/right rectangles,averages and midpoint estimates by choosing graphs/counterexamples. Retain sketch-based trapezium bias reasoning; general quadrature proofs and midpoint algorithm are enrichment,not new prescribed method
'''

GOLDIE_OTHER += '''
6|Prompt|1|158|159|2.6.1.1|text|yes|in-scope-parts-only|Choose algebraic or approximate solutions for five quadratic,cubic,quintic/exponential equations; supplied explanation159uses graphs for nonalgebraic roots. Retain graphical/numerical scope,do not infer an unprescribed general quintic formula
6|Activity|1|162|||text|no|out-of-scope|Investigate number of bisection steps for prescribed decimal accuracy; interval-bisection algorithm is supporting numerical-method enrichment,not an8227supplied fixed-point iteration demand
6|Investigation|1|166||2.6.2.1,2.6.4.1|text|no|in-scope|Execute supplied repeated cosine/square-root/sqrt(1+x)processes,observe fixed points and explain convergence qualitatively; no formal derivative convergence test required
'''

GOLDIE_OTHER += '''
6|Prompt|2|167|||text|no|out-of-scope|Invent other rearrangements of a quintic and ask how many exist. Open learner-built rearrangement search exceeds supplied-rearrangement LIMIT08; two source-supplied forms remain usable in bounded adaptations
6|Prompt|3|169||2.6.1.2,2.6.4.2|text|no|in-scope|Explain certainty of root bounds from given endpoint sign change and continuity,contrasted with merely stabilising iterates
6|Prompt|4|170||2.6.2.1|text|no|in-scope|Discuss convergence to a different root than intended. Interpret target interval separately from sequence convergence; not numerical failure-to-converge proof
6|Prompt|5|170||2.6.2.2|graph|no|in-scope-parts-only|Read given cobweb and identify qualitative divergence under supplied recurrence. Formal derivative convergence conditions in surrounding section are excluded by LIMIT08
'''

GOLDIE_OTHER += '''
10|Prompt|1|248|||diagram|no|in-scope|Identify information needed about aircraft passing from a vapour-trail photograph. Supporting3D/context reasoning only; do not infer unprescribed closest-skew-line or relative-motion calculations
10|Activity|1|258||1.7.1.1,1.7.1.2,1.7.3.2,1.7.2.3|diagram|no|in-scope|Read labelled cuboid,axes and six edge midpoints; identify3Dpoints and every directed displacement matching supplied column vectors
10|Prompt|2|253||1.7.4.1|text|no|in-scope|Show3Dvector magnitude formula from orthogonal components; Pythagorean derivation,not mere formula recall
10|Prompt|3|261||1.7.2.3,1.7.3.3,1.7.2.1,1.7.2.2|diagram|no|in-scope|Prove internal ratio formula for point C dividing AB in s:t using given triangle construction; require nonzero s+t
10|Prompt|4|264||1.7.4.2,1.7.5.1|diagram|no|in-scope|List assumptions in cosine-rule derivation of scalar-product angle formula,including nonzero vectors and chosen angle
10|Prompt|5|266||1.7.4.2|text|no|in-scope|Prove commutativity of scalar product from component formula,not commutativity of vector or cross product
10|Prompt|6|267||1.7.4.2,1.7.5.1|text|no|in-scope|Extend scalar-product angle formula from2Dto3Dby component/length argument; nonzero magnitudes required
'''

GOLDIE_OTHER += '''
2|Activity|2|43|||text|no|in-scope-parts-only|Compare earthquake intensity,musical octave frequency and decibel noise levels; source relies on external scale conventions not supplied. Retain log-context leads only with explicit definitions in any adaptation
3|Activity|1|75|77|2.3.2.2,1.6.6.1|text|yes|in-scope|Find acute root of sin(theta+60)=cos(theta-60),with graph/search suggestion and later compound-formula solution; alternative methods and unique acute root
5|Worked illustration|1|147|148,149,150||graph|no|in-scope|Unnumbered trapezium demonstration for sqrt(5x-x^2) on0..4. Compares2,4,8,16strips and explains underestimation visually; explanatory evidence,not a separate assessed question
5|Prompt|3|150|||graph|no|in-scope-parts-only|Find the same curved area geometrically and compare16-strip estimate. Circle-segment geometry can support an alternative exact check; source supplies no standalone answer and demands calibrated within circular measure
'''

YM += '''
3|Investigation transformations|2|129|1.3.5.1|text|yes|Compare horizontal shifts of quadratic and square-root graphs; additive input constant moves opposite horizontal direction,with shifted domains
3|Investigation transformations|3|129|1.3.5.1|text|yes|Compare original and negative-output quadratic,root and exponential graphs; reflection in horizontal axis. Continued result130
3|Investigation transformations|4|130|1.3.5.1|text|yes|Compare root and negative-input root or exponential graphs; reflection in vertical axis,domain reversal is essential
3|Investigation transformations|5|131|1.3.5.1|text|yes|Cubic and scaled-output cubic with factors2and1/2; compare vertical stretch/compression and shared zeros
3|Investigation transformations|6|131|1.3.5.1|text|yes|Cubic with scaled input2x or x/2; inverse horizontal scale and changed zeros; illustrated result continues132
'''

YM += '''
4|Investigation basic trig graphs|1|165|1.6.1.1,1.6.2.1,1.3.2.2|table|yes|Plot sine in degrees then complete extrema,amplitude,period and range table; graph/scale interpretation plus table response
4|Investigation basic trig graphs|2|166|1.6.1.1,1.6.2.1,1.3.2.2|table|yes|Repeat cosine and tangent graph/table; tangent has no finite maximum/minimum or amplitude,not amplitude0. Poles and unrestricted real range remain explicit
4|Investigation basic trig graphs|3|166|1.6.1.1,1.6.2.1|text|yes|Plot wide-angle degree graphs and justify periodicity of sine,cosine,tangent from repeated shapes; interval width changes view,not period
'''

YM += '''
4|Investigation transformed trig graphs|1|169|1.6.2.1,1.6.2.3|table|yes|Complete sine amplitude,extrema,period and graph table for output factors1,2,3; table continues170
4|Investigation transformed trig graphs|2|170|1.6.2.1,1.6.2.3|table|yes|Complete cosine and tangent output-scale tables; tangent amplitude and finite extrema do not exist
4|Investigation transformed trig graphs|3|170|1.6.2.2|text|no|Explain output multiplier effect,including reflection for negative factors if extended; distinguish tangent steepness from amplitude
4|Investigation transformed trig graphs|4|171|1.6.2.1,1.6.2.3|table|yes|Compare sine,cosine,tangent input factors1,2,3,1/2,1/3; complete period and sketch table
4|Investigation transformed trig graphs|5|171|1.6.2.2|text|no|Explain inverse dependence of period on nonzero input multiplier; positive source factors only
4|Investigation transformed trig graphs|6|172|1.6.2.1,1.6.2.3|table|yes|Complete sine/cosine vertical shifts by1,2,-1,-2; preserve period and amplitude
4|Investigation transformed trig graphs|7|172|1.6.2.2|text|no|Explain vertical translation effect on extrema,range and unchanged period
'''

YM += '''
5|Unnumbered scalar product|1|251|1.7.4.2|diagram|no|Magnitude-angle worked illustration with sqrt(200),5,45degrees; inline result50,not an extra numbered exercise
5|Unnumbered scalar product|2|251|1.7.4.2|text|no|Component worked illustration(8,-6,-10)dot(4,-3,0)=50; inline solution compares magnitude-angle method
'''

YM += '''
8|Unnumbered modulus sketch|1|383|2.1.2.1|graph|yes|Sketch2abs(x-1)+3 from vertex,slopes and shifts; combined output/inside/vertical transformations exceed prescribed simple forms. Internal partial-scope lead,not full8227modulus-graph coverage
9|Investigation logarithmic|1|428|2.2.2.2|graph|yes|Compare graphs with bases2,10,1.2,e and1/2,1/10,1/1.2,1/e; common point(1,0),quadrants,asymptote and monotonicity. Continuation429; software change-base expression is not assessed8227method
'''

YM += '''
3|Investigation transformations|1|128|1.3.5.1|graph|yes|Plot x^2,x^2+2,x^2-3 and sqrt(x),sqrt(x)+4,sqrt(x)-5; explain vertical shifts without changed input domain
'''

GOLDIE_OTHER += '''
4|Activity|2|110|111|2.4.1.1|graph|yes|in-scope|Read supplied sine graph in radians and sketch derivative from gradient zeros,signs and magnitudes; compare cosine then repeat for cosine. Graphical reasoning,not a proof by sampling
4|Activity|3|111||2.4.2.2,2.4.1.1|text|no|in-scope|Prove derivative of tan(x) from sin/cos quotient rule in radians,on intervals with cos(x)nonzero
4|Prompt|5|111|||graph|no|in-scope-parts-only|Decide whether y=x remains tangent to sine when horizontal coordinate is degrees. Supporting angle-unit/derivative explanation; not direct evidence for the definition of radian
4|Prompt|6|111|||text|no|in-scope-parts-only|Explain why graphical slope evidence does not constitute a general proof of derivative formulas. Supporting evidence reasoning; no invented8227proof-demand coverage
'''

YM += '''
3|Example|16|136||text|no|Use midpoint and perpendicular line through a given point,then distance13; prerequisite coordinate geometry,not automaticASintersection coverage
3|Try Now|16|136||text|no|Perpendicular bisector of A(14,-7),B(-6,3) meets yaxis; CD:y=2x-10,AD=sqrt205. Prior coordinate practice with no automaticASdemand credit
'''

YM += '''
9|Try Now 28|2|432|2.2.2.2,1.3.5.2,1.3.3.2|graph|yes|Read logarithm curve through B(8,3/2),recover base4,identify A(1,0),reflect in xaxis and y=x,and find Cinput for ordinate-2
9|Try Now 28|3|432|2.2.2.2,1.3.3.2,1.3.5.2|graph|no|Match three reflected log-base3 curves,distinguish input/output reflection,then find inverses of g and f with domains
'''
