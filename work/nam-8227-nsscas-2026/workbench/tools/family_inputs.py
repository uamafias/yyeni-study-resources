"""R2 family decisions following the independent review's section 4.

These are analysis groupings, never a recipe count. Connected questions remain
connected even where several reusable reasoning modules occur within them.
"""
# slug | title | discriminating decision / response evidence | structural branches
DEFINITIONS='''
quadratic-form|Completed-square interpretation|Choose and interpret vertex form rather than solve for zeros; show square form or vertex evidence|complete-square;vertex;embedded-function-module
monotonicity|Increasing and decreasing intervals|Use the sign of the derivative on the admitted domain, distinguishing a global monotonicity claim from a single rate evaluation|intervals;global-sign;domain-restriction
angle-units|Radian meaning and angle conversion|Relate an arc/radius ratio and convert angle units explicitly; merely using an angle marked rad does not establish conversion coverage|radian-meaning;degrees-to-radians;radians-to-degrees
root-conditions|Parameter conditions on quadratic roots|Turn a required root count into a discriminant inequality and solve its parameter set|strict-range;nonintersection;specific-root-count
root-proofs|Universal and rational-root arguments|Prove a claim for all admitted parameters; nonzero leading coefficient and rational-square argument matter|universal-distinctness;rational-roots;degenerate-exemplar-held
coefficient-identities|Coefficients determined by an identity|An identity holds for every admitted x, so coefficients or strategically substituted values determine constants|polynomial-product;rational-identity-with-domain
quadratic-substitution|Quadratic substitution and recovery chain|Choose the transformed variable, solve in it, then recover and filter original roots; a preceding ordinary quadratic remains a module|powers;radicals;exponential;hence-reuse
polynomial-reconstruction|Polynomial from graphical constraints|Infer roots/multiplicities and scale from sufficient graph information instead of merely solving a supplied polynomial|quadratic;cubic-syllabus-required
quadratic-inequality|Quadratic critical values and intervals|Convert roots to one solution set with justified endpoint inclusion; root calculation alone is insufficient|standalone;component-of-discriminant-or-modulus
binomial-selection|Binomial terms and coefficient conditions|Select contributing terms before combining expansions; different coefficients alone are ordinary variation|linear-product;sum-difference;constant-term
ap-conditions|Arithmetic progression from conditions|Translate term/sum or context conditions into AP parameters and inclusive counts|terms-and-sums;context;module-in-AP-GP-chain
gp-finite|Finite geometric progression and thresholds|Identify ratio, finite term/sum and when a discrete threshold is first crossed|ratio-and-terms;finite-sum;integer-threshold
gp-infinite|Geometric convergence and infinite sum|Admit only ratios with absolute value below one before using an infinite sum; Sigma is a representation branch|convergence-parameter;sum-admissibility;sigma
ap-gp-connected|Connected arithmetic/geometric progression problem|Transfer an amount or sum between two progression structures rather than practise isolated substitutions|equal-context-totals;sums-as-AP-terms
function-analysis|Connected function, restriction, inverse and composition analysis|Decide admissible domains and one-to-one branches, then keep inverse/composition/sketch evidence consistent|radical;log-exp;rational;restricted-quadratic;inverse-sketch
coordinate-shapes|Coordinate lines and geometric shapes|Translate perpendicularity, midpoint, reflection or rhombus constraints into equations and unknown coordinates|reflection;perpendicular-diagonal;midpoint
line-curve|Line/curve intersections and graph deductions|Distinguish reading intersections from solving their equation and from using a tangent's repeated-root condition|algebraic-intersection;graph-root-count;line-sketch;tangency
circular-symbolic|Compound circular perimeter and area|Identify the exposed boundary and combine major/minor sectors; internal joins are not perimeter|symbolic-perimeter;compound-sector-area
circular-contact|Circle/sector contact geometry|Construct the right-triangle or tangent relationship before using arc/sector area; shaded-region topology is essential|concentric-tangent;two-touching-circles;inscribed-circle
segment-area|Circular segment area|Subtract the chord triangle from a sector, distinguishing minor and major segment; a sum of sectors does not assess this demand|minor-segment;major-segment
trig-graph-reading|Read trigonometric graph parameters and signs|Read amplitude, midline, period and sign intervals from supplied curves; response is inferred data rather than a drawn graph|parameters;reflection;product-sign
trig-graph-sketch|Sketch a transformed trigonometric graph|Produce the shape, interval, extrema and phase/period features from an equation|sine-cosine;tangent;combined-line
principal-values|Principal inverse-trigonometric values|Use restricted inverse ranges before algebraic recovery; nonprincipal inverse results are invalid|sine;cosine;tangent;defective-source-held
basic-trig-proof|Basic trigonometric identity proof|Give a chain of equalities valid on the common domain; equation solving alone does not prove an identity|Pythagorean;tan-sin-cos
bounded-trig|Basic bounded trigonometric equations|Choose an identity/substitution then recover every allowed angle and reject singular or out-of-interval candidates|direct;quadratic-in-ratio;changed-angle;hence-reduction
vector-relations|Position and displacement vector relations|Translate directed geometric relations into vector arithmetic; internal and external division must remain distinct|given-position;internal-division;external-division
vector-3d-diagram|Vectors from a three-dimensional diagram|Infer coordinates and midpoint relations from an oriented 3D solid before doing vector algebra|pyramid;prism;axis-orientation
vector-product|Magnitude, scalar product and direction|Choose vector directions for an angle or use a zero scalar product for perpendicularity; magnitude-only work is a component|angle;perpendicularity-proof;parameter;magnitude-module
unit-vector|Construct a unit vector|Normalize the correct nonzero displacement by its magnitude; coordinate basis symbols i,j,k alone do not count|given-vector;vector-chain;diagram-midpoint
power-differentiation|Power and chain-rule differentiation component|Differentiate a power/composite at the correct argument, including successive-derivative notation|rational-powers;linear-composite;successive
gradient-evaluation|Use a supplied derivative|Interpret gradient data and substitute into a given derivative; no differentiation credit is implied|parameter-from-point
tangent-normal|Derivative and tangent/normal geometry|Forward tasks find a line at a point; inverse tasks recover point or parameter from a specified gradient|forward-tangent-normal;inverse-gradient
stationary-points|Locate and classify stationary behaviour|Solve derivative zero, then supply the separately requested maximum/minimum/inflexion evidence|location;nature;inflexion-gap
constrained-optimisation|Construct a constrained model then optimise|Eliminate a geometric variable before differentiating; model-construction parts assess ability 8 and prior geometry, not calculus|perimeter-area;fixed-volume-surface;quoted-model
connected-rates|Connected rates with a geometric model|Relate changing dimensions and chain rates, keeping the geometry derivation separate from the differential rate|similar-cones;other-shape
motion-differentiation|Motion and event-conditioned derivatives|Differentiate displacement/velocity and evaluate at a rest or maximum-height event, rather than confuse rates of different quantities|maximum-height;rest-acceleration;exponential-motion
rate-evaluation|Evaluate an elementary rate|Differentiate then evaluate a rate at stated data; no connected-rate chain is present|given-time
curve-recovery|Recover a curve and integration constant|Integrate a derivative and use a compatible point/condition to fix its constant|given-point;gradient-parameter;invalid-domain-held
definite-integral|Definite and simple improper integrals|Apply limits to an antiderivative, distinguishing finite substitution from a limiting endpoint|finite;unknown-bound;quoted-exact-result;simple-improper
integral-area|Area bounded by curves and lines|Choose bounds and upper-minus-lower integrand from the actual region; integral value alone may be signed|under-curve;between-curves
integral-volume|Volume of revolution about an axis|Choose squared radius and integration variable for the named axis; changing axes changes the representation|x-axis;y-axis
motion-integration|Integrate motion with conditions|Integrate acceleration/velocity with initial or interval data; distinguish distance from signed displacement|polynomial;exponential;initial-condition
modulus-equations|Modulus equations and inequalities|Choose cases or squaring, enforce leg/domain admissibility and state one solution set|two-moduli-inequality;line-intersection;graphical-deduction;modulus-exponent
modulus-reading|Read parameters of a modulus graph|Infer vertex, signed scale and shifts from graph data; returning parameters differs from sketching|scaled-shifted-V
modulus-sketch|Construct a modulus graph|Produce a V-shape and any comparison line, with correct intercept ordering and orientations|positive-parameter;comparison-line
polynomial-division|Polynomial quotient and remainder|Carry out division and identify both quotient and remainder; non-monic linear and quadratic divisors need distinct procedures|monic-linear;nonmonic-linear;quadratic-divisor
remainder-coefficients|Unknown coefficients from factor/remainder data|Translate evaluations into coupled coefficient equations; factor and remainder conditions are different constraints|single-polynomial;coupled-polynomials
factor-solve|Factor and solve using division/factor theorem|Use a known or discovered factor, then distinguish complete factors from the requested roots|given-factor;discover-factor;hence-quotient;composite-trig
log-laws|Logarithmic equivalence and inequalities|Combine logs only on their domains and keep inequality/domain conditions through the algebra|show-equivalence;inequality;equate-log-arguments
exponential-sketch|Exponential and logarithmic graph construction|Produce transformed standard shapes with correct intercepts/asymptotes, rather than plot a table of arbitrary points|exp-decay;paired-exponentials;shifted-log
exponential-equations|Exponential/logarithmic equation solving|Choose log laws or inverse exponential operations and enforce contextual integer/positivity restrictions|single-exponential;log-equation;discrete-threshold
linearisation|Linearisation and constants from a transformed graph|Keep the plotted transformed variable distinct from the original variable before matching slope/intercept|natural-log-axis;base-three;given-slope
advanced-trig-proof|Compound/double/reciprocal identity proof|Select a non-basic identity and demonstrate equivalence with valid domains; retain proof separately from roots/evaluation|compound;double-angle;reciprocal
advanced-trig-solve|Equation solving through selected identities|Select compound/double/reciprocal transformations, reduce and recover bounded solutions|compound-angle;double-angle;reciprocal;connected-reduction
exact-trig-evaluation|Exact evaluation through an identity|Use a supplied identity or angle relationship to produce an exact value, not a proof or list of roots|changed-argument;compound-angle
r-form|R-form reduction, equations and extrema|Choose the phase/sign convention and use the resulting amplitude to solve or bound an expression|sine-form;cosine-form;reduce-first;extrema
identity-extrema|An extremum revealed by an identity|Rewrite a rational trigonometric expression into a bounded function; this source needs no R-form calculation|double-angle-bound
elementary-differentiation|Elementary exponential/log/trig derivative component|Apply the correct elementary derivative and inner factor; retained as an embedded component, not an automatic drill recipe|elementary;composite
product-quotient|Product/quotient differentiation|Choose a product/quotient method or valid algebraic rewrite before evaluating geometry or a stationary condition|product;quotient;algebraic-alternative
parametric|Parametric differentiation and geometric conditions|Use dy/dt divided by dx/dt and distinguish horizontal/vertical tangency and parameter recovery|axis-crossing;vertical-tangent;numerical-parameter
implicit|Implicit differentiation and geometric conditions|Differentiate all y-dependent terms, retain dy/dx and evaluate at a point compatible with the curve|derive-formula;find-coordinate;normal
standard-antiderivatives|Standard antiderivatives|Recognise the elementary integrand and include the constant when indefinite; no initial condition is implied|exponential;reciprocal-linear;power;trigonometric
reverse-given-derivative|Integration by reversing a preceding derivative|Compare a known derivative to the requested integrand and adjust its multiplier; do not invent a new integration rule|scaled-derivative;definite;indefinite;combined-integrand
algebra-before-integration|Algebraic pre-processing before integration|Divide or rewrite the integrand before applying standard antiderivatives; quotient differentiation is not an integration rule|polynomial-division;exponential-rewrite
trig-integration|Identity selection before a trigonometric integral|Choose an identity or a changed-argument earlier result so the integrand becomes standard|squared-trig;changed-argument;definite
trapezium-chain|Trapezium estimation, sketch and bias|Set ordinates/step width, preserve precision, and separately justify chord/curve position; log-rescaling is a structural branch|direct-estimate;log-rescaling;sketch-bias;given-graph-bias
numerical-method-chain|Connected numerical root finding|Distinguish a root bracket, fixed-point rearrangement, iterates and justified rounding; an iteration result alone is not a global root claim|given-equation;calculus-derived-equation;graph-count;failure-syllabus-required
'''


BASE={
 '01':'quadratic-form','02':'root-conditions','03':'coefficient-identities','04':'quadratic-substitution',
 '05':'polynomial-reconstruction','06':'quadratic-inequality','07':'binomial-selection','08':'gp-finite',
 '09':'ap-conditions','10':'gp-finite','11':'gp-infinite','12':'gp-infinite','13':'ap-gp-connected',
 '14':'function-analysis','15':'function-analysis','16':'function-analysis','17':'function-analysis',
 '18':'line-curve','19':'circular-contact','20':'trig-graph-reading','21':'principal-values',
 '22':'basic-trig-proof','23':'bounded-trig','24':'vector-relations','25':'vector-product','26':'vector-product',
 '27':'power-differentiation','28':'tangent-normal','29':'stationary-points','30':'constrained-optimisation',
 '31':'connected-rates','32':'curve-recovery','33':'definite-integral','34':'integral-area','35':'integral-volume',
 '36':'motion-integration','37':'modulus-equations','38':'modulus-reading','39':'polynomial-division',
 '40':'remainder-coefficients','41':'factor-solve','42':'log-laws','43':'exponential-sketch',
 '44':'exponential-equations','45':'linearisation','46':None,'47':'advanced-trig-proof','48':'r-form',
 '49':'r-form','50':'elementary-differentiation','51':'product-quotient','52':'parametric','53':'implicit',
 '54':'standard-antiderivatives','55':'trig-integration','56':'trapezium-chain','57':'trapezium-chain',
 '58':'numerical-method-chain','59':'numerical-method-chain','60':'numerical-method-chain',
 '61':'numerical-method-chain','62':'numerical-method-chain'}

OPTIMISATION={'2022-1-Q8','2023-1-Q13','2024-1-Q11','2025-1-Q9'}
REVERSE={'2021-2-Q5:b','2024-2-Q4:b','2025-2-Q10:b'}
ALGEBRA={'2021-2-Q9:a','2024-2-Q5:b'}


def memberships(q, part):
    key=part['source_key'];qkey=q['source_key']
    if qkey in OPTIMISATION:return ['constrained-optimisation']
    if qkey=='2022-1-Q12':return ['connected-rates']
    if key=='2025-1-Q8:a':return ['gradient-evaluation']
    if key=='2022-1-Q2:a':return ['quadratic-substitution']
    if key=='2023-1-Q9:answer':return ['principal-values']
    if key in REVERSE:return ['reverse-given-derivative']
    if key in ALGEBRA:return ['algebra-before-integration']
    out=[]
    for legacy in part['legacy_pattern_ids']:
        n=legacy.rsplit('-',1)[-1];slug=BASE[n]
        if not slug:continue
        if n=='02' and key in {'2021-1-Q10:b','2023-1-Q1:b','2025-1-Q1:a'}:slug='root-proofs'
        if n=='18' and qkey in {'2024-1-Q8','2025-1-Q12'}:slug='coordinate-shapes'
        if n=='19' and qkey=='2021-1-Q7':slug='circular-symbolic'
        if n=='20' and part['requires_sketch_response']:slug='trig-graph-sketch'
        if n=='24' and qkey=='2024-1-Q10':slug='vector-3d-diagram'
        if n in {'29','31'} and qkey=='2023-1-Q10':slug='motion-differentiation'
        if n=='31' and key in {'2023-2-Q9:a','2025-2-Q8:answer'}:slug='motion-differentiation'
        if n=='31' and key=='2025-2-Q11:c':slug='rate-evaluation'
        if n=='38' and part['requires_sketch_response']:slug='modulus-sketch'
        if n=='44' and any(x.endswith('PAT-04') for x in part['legacy_pattern_ids']):continue
        if n=='47':
            if key in {'2023-2-Q3:b.ii','2024-2-Q9:b','2025-2-Q3:answer'}:slug='exact-trig-evaluation'
            elif part['response_format']!='proof/show-that' or key in {'2021-2-Q6:a'}:slug='advanced-trig-solve'
        if n=='49' and key=='2025-2-Q7:b':slug='identity-extrema'
        if slug not in out:out.append(slug)
    assert out,key
    return out
