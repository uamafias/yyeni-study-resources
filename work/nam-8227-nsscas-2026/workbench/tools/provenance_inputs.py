"""Candidate matches selected for paired rendered-page confirmation in R3."""
# NSSCAS key | Cambridge file stem | question | Cambridge pages | confidence | shared | changed | defect explanation
SPEC = r'''
2023-1-Q6|9709_w16_qp_13|5|2|adapted|Concentric major-arc/tangent diagram; radius 6 and angle 1.8; show inner radius 3.73 then shaded area|Roman parts renumbered as (a),(b); stem shortened; shaded-area tariff 4 becomes 3; layout; statement that C,D lie on OA,OB respectively is omitted|None
2024-2-Q5|9709_m22_qp_22|6|8,9|adapted|Polynomial 4x^3+16x^2+9x-15; quotient/remainder; integrate quotient; factor p(x)+6 and cosec2θ equation|NSSCAS names polynomial f(x) but retains p(x) in the division instruction; divisor 2x+3 becomes 2x-1 in (a),(b), with a changed quotient and integration; part (b) tariff 2 becomes 3|SRC-8227-POLYNOMIAL-NAME-2024-P2-Q5
2022-2-Q5|9709_s16_qp_22|5|2|adapted|y=6xe^{x/3}; derivative-to-log rearrangement, bracket and fixed-point iteration structure|Gradient 40 becomes 20; corresponding numerator 20 becomes 10 and bracket/starting value change; Cambridge(iii) supplies neither formula nor start: NSSCAS supplies both; bracket tariff2→3 and iteration3→2|None
2022-2-Q5|9709_s16_qp_23|5|2|adapted|Same Cambridge common component question as variant 22, with y=6xe^{x/3} and gradient 40|NSSCAS changes gradient to 20 and iteration data accordingly; Cambridge(iii) supplies neither formula nor start: NSSCAS supplies both; bracket tariff2→3 and iteration3→2|None
2022-1-Q3|9709_w16_qp_13|2|2|adapted|Coefficient of x^3 in a sum (1-3x)^6+(1+ax)^n determines a|Second exponent 5 becomes 4; coefficient 100 becomes -1040|None
2022-2-Q3|9709_m20_qp_22|7|10,11|adapted|Quadratic in sinx, x-intercept A, exact gradient there and shaded-region integral using double angles|4sin^2x+8sinx+3 becomes 2sin^2x+7sinx+3; NSSCAS(c) adds the double-angle hint for2sin^2x and drops exact; (b)3→5 marks|None
2022-2-Q8|9709_m20_qp_22|3|4|adapted|Definite integral of reciprocal linear expression with bounds proportional to positive a equated to a logarithm|2/(2x-5), bounds a to 3a and ln(7/2) become 3/(3x-5), bounds a to 2a and ln(13/4)|None
2022-2-Q10|9709_s18_qp_21|5|8,9|adapted|Parametric cosine-double-angle/sine curve, gradient at θ=1 and vertical tangent|x coefficient 2 becomes 4; y coefficient 3 becomes 5; (a)4→5 marks; NSSCAS(b) prints were for where|None
2023-1-Q4|9709_w21_qp_13|2|3|structurally similar, no specific source|First three binomial terms, then x^2 coefficient after multiplication by a linear factor to find possible a|Expansion (1+ax)^6 becomes (3+ax)^4; linear factor 1-3x becomes 1+4x; target -3 becomes 1080; (a)1→2 marks and(b)4→3; no distinctive value is shared, so this is not evidence of a specific source|None
2023-2-Q5|9709_w18_qp_22|6|8,9|adapted|Part (b) only: definite integral of sin^2x plus tan^2(2x) on 0 to π/6|sin^2 coefficient 8 becomes 6; integral target is supplied as a show-that in NSSCAS; part (a) is unrelated and has no provenance link here|None
2024-2-Q6|9709_w15_qp_22|7|3|identical|Integral cos^2x+1/cos^2x on 0 to π/3 with exact value π/6+9√3/8; squared-curve volume and diagram|Roman parts become letters; layout and whitespace; curve label added in NSSCAS|None
2024-2-Q7|9709_s19_qp_22|6|8,9|adapted|Same x=3t-6e^{-2t}, y=4t^2e^{-t} and curve; rearrange, iterate, then find parametric gradient|Point y=1 becomes 1/4; fixed-point factor 1/2 becomes 1/4; start .7 becomes .4; iterate precision 5 becomes 4 s.f.; t1 renamed t0; using your answer in(b) added to(c)|None
2024-2-Q11|9709_w20_qp_22|3|5|adapted|Positive parameter a, sketch modulus and straight line, intersection, then deduce inequality|Modulus x coefficient 1/2 becomes 1/4; straight-line coefficients 3/2 and -1/2 become 3/4 and -1/4; predrawn axes and in terms of a added|None
2025-1-Q9|9709_s17_qp_11|6|10,11|adapted|Equilateral triangular prism of fixed volume, derive total surface area, stationary dimension and classification|Volume 2000 becomes 432; wooden-block context; coefficients change accordingly; prism diagram added; (a)3→4 marks; (c) replaces nature of stationary value with whether minimum or maximum and explicitly asks all necessary working|None
2025-2-Q1|9709_w23_qp_21|5|6|structurally similar, no specific source|Unknown cubic coefficients, factor x+2 plus specified remainder give simultaneous equations|Leading coefficient 6 becomes 2; constant -20 becomes 6; divisor x+1 becomes x-1 and remainder -11 becomes -6; only coefficient part retained|None
2025-2-Q5|9709_w22_qp_23|5|7|adapted|Implicit curve combines y times exponential of x with y^2; find gradient at x=0, negative y|4e^{2x}y+y^2=21, point (0,-7), becomes 2e^{3x}y+y^2=15, point (0,-5)|None
2025-2-Q9|9709_s18_qp_21|7|12|adapted|Exactly 5cosθ-2sinθ into Rcos(θ+α), then 5cotθ-4cosecθ=2|Radians/domain 2π and phase 4 d.p. become degrees/domain 360 and phase 3 d.p.|None
2025-2-Q10|9709_m22_qp_22|5|6,7|adapted|tan^2x derivative 2tanx+2tan^3x then exact integral tanx+tan^2x+tan^3x from π/4 to π/3|NSSCAS explicitly adds Hence in part (b); same mathematical expressions and bounds|None
2021-2-Q2|9709_w18_qp_22|6|8|structurally similar, no specific source|Part (a) only: show exact logarithmic definite integral of a reciprocal linear expression using log laws|12/(3x+2), bounds 1 to 6, ln256 become 8/(2x+1), bounds 1 to 4, ln81; tariff 5 becomes 4|None
2025-2-Q6|9709_m22_qp_22|3|4|adapted|y=3^(2a)*a^x and straight-line logarithmic graph to identify a then intercept|ln y becomes log_3 y; gradient0.239 becomes2; a requested3sf→exact; (b) y=36 becomes81 and drops3sf; same3+2 marks|None
2025-2-Q12|9709_s22_qp_21|5|6,7|adapted|Same modulus5-2x and3lnx graphs, rearrangement, bracket and iteration sequence|Larger root becomes smaller; plus sign becomes minus in rearrangement; bracket4.5..5.0 becomes1.68..1.71; supplied start1.698; tariff(b)1→2,  iteration5sf→4sf|None
2022-2-Q4|9709_s15_qp_21|4|2|adapted|Two cubic polynomials f=x^3+ax^2+b and g=x^3+bx^2-a; factor/remainder simultaneous equations then extremum of g-f|Factor x+2→x+3; remainder-18→6; greatest→smallest; part(i)/(ii) relabelled(a)/(b)|None
2022-2-Q7|9709_m18_qp_22|6|10,11|adapted|Identity cosec2x+cot2x=cotx followed by integral sin2x(cosec4x+cot4x)|Cambridge exact cot(pi/12) part(ii) omitted; (i)→(a), (iii)→(b); same4+3 marks|None
2023-2-Q3|9709_m18_qp_22|6|10,11|adapted|Identity cosec2x+cot2x=cotx then exact evaluation and transformed integral|Source(i)→(b.i) 4marks; cot(pi/12)→cosec(2pi/3)+cot(2pi/3) for(b.ii)2marks; source(iii)→(b.iii)3marks; Cambridge Hence in source(ii) is lost in NSSCAS(b.ii); NSSCAS(a) not linked to this source|None
2024-2-Q9|9709_s15_qp_22|3|2|adapted|Acute angle; quadratic equation in tan followed by compound-angle exact value|Degrees→radians;2sec^2theta+3tan theta=22→2sec^2theta-3tan theta=22; theta+135degrees→theta+3pi/4; same3+3 marks; source theta renamed x; use an appropriate formula removed and using your value of tan x in part(a) added|None
2024-2-Q2|9709_s21_qp_21|2|4|adapted|Expand shifted sine then solve trig equation over a full turn|theta+30degrees→theta+60degrees; cosectheta→sectheta; RHS2 retained; tariff6→5; strict source interval endpoints become inclusive in NSSCAS|None
2023-2-Q4|9709_m19_qp_22|3|4|adapted|y=Ae^(px+p), linear ln y against x diagram to determine A,p|Points(1,2.835),(6,6.585)→(1,1.693),(3,2.693);5marks retained; source only corresponds to(a)|None
2021-2-Q12|9709_s19_qp_22|7|10,11|adapted|R-form followed by transformed equation and restricted trigonometric domain|4sin theta+4cos theta→3cos theta+3sin theta; Rsin(theta+alpha)→Rcos(theta-alpha); (a.i) angle units degrees→radians; (a.ii) RHS5→sqrt2; (b)4cot2x=5+tanx→4/tan2x+5=tanx with quadratic3t^2+5t-2 changing to3t^2-5t-2, and radians→degrees,drops2dp; tariffs3+2+6→3+3+5|None
2022-1-Q11|9709_w17_qp_12|9|16,17|adapted|Trapezium with parallel opposite sides, position vectors of adjacent points and side-length ratio determine fourth point|OABC renamed OPQR; A(2,-2,-1),B(6,1,1)→P(3,-2,-1),Q(5,1,2); long side3times→2times; source(ii) findC→(a) showR=(-1,5,4), same3marks; diagram redrawn; source(i) right-angle proof and(iii) area omitted; NSSCAS(b) scalar-product angle is new|None
2021-1-Q6|9709_s17_qp_13|4|5|possible source (wording only)|Position vectors, AP as a multiple of AB, then dot-product perpendicularity|OA(5,1,3),OB(5,4,-3)→(3,3,6),(1,5,2); AP=AB/3→3AB/2 but on AB wording retained; coordinates rather than position vector,3→4marks; distanceOP part omitted; perpendicular OP to AB test becomes show AP perpendicular OB,2marks retained. Unique local wording The point P lies on AB such that AP=kAB is a possible source lead: Cambridge1/3 places P on the segment,whereas replacing it by3/2 creates the NSSCAS external-division wording defect; hidden wording-only inference,not confirmed adaptation|SRC-8227-EXTERNAL-DIVISION-2021-P1-Q6
2023-2-Q8|9709_s18_qp_22|5|8|adapted|Identical curve y^3 sin2x+4y=8 and yaxis crossing; implicit differentiation|Cambridge asks tangent equation as an unscaffolded6mark task; NSSCAS(a) supplies derivative to establish[4],then(b)hence asks gradient only[2]; tangent-equation output omitted|None
2023-2-Q1|9709_s16_qp_21|4|2|adapted|Quotient on division by x+2 plus supplied remainder; hence factorisation and roots;3+3+1marks|Polynomial8x^3+30x^2+13x-25 becomes6x^3-7x^2-23x+25; remainder5 becomes-5; p(x)-5 becomes p(x)+5; source final p(abs(x))-5=0 becomes ordinary p(x)+5=0 and adds Hence; Roman parts become letters|None
2025-2-Q3|9709_w22_qp_21|3|5|adapted|Acute angle with exact secant value; exact tangent of compound quarter-turn;4marks|sec theta=sqrt17 becomes sqrt10; tangent(theta+pi/4) becomes tangent(theta-pi/4),changing the exact answer from-5/3 to1/2; same strict acute interval|None
2023-2-Q3|9709_m20_qp_22|1|2|adapted|Part(a)only:compound-angle equation over0..90degrees,4marks|Source2sin(theta+30)+5cos theta=2sin theta becomes2cos(theta+30)+5sin theta=4cos theta; same strict interval; source standaloneQ1 becomes multipartQ3(a); Q3(b)has separate source024|None
2023-2-Q5|9709_s19_qp_22|3|4|adapted|Part(a)only:find exact coordinates of stationary point of y=kx/lnx,5marks|Numerator3x becomes5x; stationary inpute unchanged and ordinate3e becomes5e; standaloneQ3 becomes multipartQ5(a); Q5(b)has separate source010|None
2023-2-Q6|9709_m18_qp_22|3|5|adapted|Four-interval trapezium approximation of shifted ln followed by Hence approximation of3ln of the corresponding perfect-square quadratic;3+2marks|ln(x+2)on0..8 becomes ln(x-2)on3..11;3ln(x^2+4x+4) becomes3ln(x^2-4x+4),same bounds as preceding integral; NSSCASadds sketch[3]and use-sketch estimate-direction[2],not present in the Cambridge source question|None
2023-2-Q4|9709_s20_qp_22|1|3|adapted|Part (b) only: relate powers of two bases and obtain the slope of the straight line y = kx by logarithms|Bases 2^y = 9^(3x) become 3^y = 2^(3x); slope to 3 s.f. becomes exact; source standalone Q1 becomes Q4(b), while Q4(a) retains source 027|None
'''

# Explicit part correspondence; unmatched subparts never inherit a provenance claim.
PART_MAP = {
 '2023-1-Q6': {'a':'i','b':'ii'},
 '2022-2-Q5': {'a':'i','b':'ii','c':'iii'},
 '2022-2-Q10': {'a':'i','b':'ii'},
 '2023-2-Q5': {'b':'b'},
 '2024-2-Q6': {'a':'i','b':'ii'},
 '2024-2-Q7': {'a':'i','b':'ii','c':'iii'},
 '2025-1-Q9': {'a':'i','b':'ii','c':'iii'},
 '2025-2-Q1': {'answer':'a'},
 '2025-2-Q9': {'a':'i','b':'ii'},
 '2021-2-Q2': {'answer':'a'},
}

PART_MAP.update({
 '2025-2-Q6':{'a':'a','b':'b'}, '2025-2-Q12':{'a':'a','b':'b','c':'c','d':'d'},
 '2022-2-Q4':{'a':'i','b':'ii'}, '2022-2-Q7':{'a':'i','b':'iii'},
 '2023-2-Q3':{'b.i':'i','b.ii':'ii','b.iii':'iii'}, '2024-2-Q9':{'a':'i','b':'ii'},
 '2024-2-Q2':{'answer':None}, '2023-2-Q4':{'a':None}, '2021-2-Q12':{'a.i':'a.i','a.ii':'a.ii','b':'b'},
 '2022-1-Q11':{'a':'ii'}, '2021-1-Q6':{'a':'i','b':'ii'}
})

# Pair-specific mappings keep two sources of one multipart question separate.
PAIR_PART_MAP = {31:{'a':None,'b':None},32:{'a':'i','b':'ii','c':'iii'},33:{'answer':None},34:{'a':None},35:{'a':None},36:{'a':'i','b':'ii'}}

PAIR_PART_MAP[37]={'b':None}
