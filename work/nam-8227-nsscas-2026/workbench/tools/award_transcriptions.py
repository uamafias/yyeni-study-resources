"""R3 author transcription of the 24 rendered examiner-report award tables.

Each line is one printed award, not an invented atomic rubric. A multi-mark B
award retains the source's partial-credit note. Alternative paths are exclusive.
E and dependent mark notation are preserved in source_mark_type.
"""
# key | part | exclusive path | source mark | value | earning condition | dependencies / F.T. / alternatives
ROWS = r'''
2021-2-Q1|a|main|M|1|Substitute x=-2 to form 4m-2n=56|Allow one slip
2021-2-Q1|a|main|M|1|Substitute x=2 to form 4m+2n=0|Allow one slip
2021-2-Q1|a|main|A|1|Solve to obtain m=7 and n=-14|Both values
2021-2-Q1|b|main|M|1|Find first factor x-1 together with division with two terms correct|Division required
2021-2-Q1|b|main|A|1|Obtain correct quadratic quotient 6x^2+x-2|Dependent on division
2021-2-Q1|b|main|DM|1|Solve the quadratic using its factors (2x-1)(3x+2)|Dependent method; answers with no working score 0/4
2021-2-Q1|b|main|A|1|Give x=1, 1/2, -2/3|All roots; answers with no working score 0/4
2021-2-Q2|answer|main|B|1|Obtain k ln(2x+1)|Integration form
2021-2-Q2|answer|main|B|1|Obtain (8/2)ln(2x+1)|Correct coefficient
2021-2-Q2|answer|main|M|1|Apply both limits 4 and 1 correctly to k ln(2x+1)|No integration constant needed for this definite integral
2021-2-Q2|answer|main|E|1|Use logarithm laws to establish ln81|Quoted result requires algebraic working
2021-2-Q3|answer|squaring|M|1|Square both sides to obtain 9x^2+18x+9 < x^2+10x+25|Condone equals instead of inequality at this stage
2021-2-Q3|answer|squaring|A|1|Simplify to 8x^2+8x-16 < 0 or =0|Accurate quadratic
2021-2-Q3|answer|squaring|M|1|Obtain two critical values 1 and -2|Factorisation or quadratic solution
2021-2-Q3|answer|squaring|A|1|Conclude -2<x<1|Must be a single inequality
2021-2-Q3|answer|linear|M|1|Consider one linear equation or inequality to obtain one critical value|3x+3 compared with x+5
2021-2-Q3|answer|linear|M|1|Consider the other linear equation or inequality|3x+3 compared with -x-5
2021-2-Q3|answer|linear|A|1|Obtain the critical values 1 and -2|Both
2021-2-Q3|answer|linear|A|1|Conclude -2<x<1|Must be a single inequality
2021-2-Q4|a|main|B|1|Correct decreasing exponential shape in the first quadrant only|x-axis asymptote; t starts at zero
2021-2-Q4|a|main|B|1|5000 intercept seen with correct shape|Allow if drawn into second quadrant for this mark
2021-2-Q4|b|main|B|1|Form 2500=5000e^{-0.02t}|Model equation
2021-2-Q4|b|main|M|1|Complete method to find t=34.657...|Condone inequalities
2021-2-Q4|b|main|A|1|Conclude 34 complete weeks|Source also says Accept:35; preserve conflict with complete-weeks wording
2023-2-Q1|a|main|M|1|Use any method of division|Allow one slip
2023-2-Q1|a|main|A|1|Obtain quotient 6x^2-19x+15|May be in correct long-division position; must be stated for synthetic division
2023-2-Q1|a|main|E|1|Conclude remainder -5|Accept remainder theorem for this award
2023-2-Q1|b|main|B|1|State or imply (x+2) or (6x^2-19x+15) is a factor|Or p(-2)=0 used to find factor or another correct factor
2023-2-Q1|b|main|M|1|Factorise quadratic as (ax+b)(cx+d) with ac=6 and bd=15 or bc+ad=-19|SC1 for correct quadratic factorisation alone
2023-2-Q1|b|main|A|1|Show (x+2)(2x-3)(3x-5)|All three factors; condone solutions seen; B0 M0 A0 for three correct brackets with no working
2023-2-Q1|c|main|B|1|Give all three roots -2, 3/2, 5/3|Must be three values
2023-2-Q2|answer|main|B|1|a=-2|Allow value in correct place in formula
2023-2-Q2|answer|main|B|1|b=-3|Allow value in correct place in formula
2023-2-Q2|answer|main|B|1|c=2|Allow value in correct place in formula
2023-2-Q3|a|direct|M|1|Expand compound angle and use cos30 and sin30 exactly|Both special-angle values
2023-2-Q3|a|direct|M|1|Simplify to 4sinθ=(4-√3)cosθ|a sinθ=b cosθ form
2023-2-Q3|a|direct|DM|1|Rewrite tanθ=(4-√3)/4|Dependent method
2023-2-Q3|a|direct|A|1|θ=29.6 degrees|Only solution; A0 if extra solutions
2023-2-Q3|a|division|M|1|Expand compound angle and use cos30 and sin30 exactly|Alternative printed path
2023-2-Q3|a|division|M|1|Divide throughout by cosθ and simplify|Equivalent compound-angle route
2023-2-Q3|a|division|DM|1|Rewrite tanθ=(4-√3)/4|Dependent method
2023-2-Q3|a|division|A|1|θ=29.6 degrees|Only solution; A0 if extra solutions
2023-2-Q3|b.i|main|B|1|cosec2x=1/sin2x|Reciprocal identity
2023-2-Q3|b.i|main|B|1|cot2x=cos2x/sin2x or (1-tan^2x)/(2tanx)|Either printed identity
2023-2-Q3|b.i|main|M|1|Use identities to obtain a single fraction in sinx and cosx only|Correct identities
2023-2-Q3|b.i|main|E|1|Show all steps to conclude cotx|Quoted identity must be established
2023-2-Q3|b.ii|main|M|1|Substitute 60 or 120 degrees (π/3 or 2π/3)|Use the identity from preceding part
2023-2-Q3|b.ii|main|A|1|Obtain √3/3 or 1/√3|Must be exact
2023-2-Q3|b.iii|main|B|1|Use identity to simplify sin2x cot2x|To cos2x
2023-2-Q3|b.iii|main|M|1|Integrate cos2x to k sin2x|k constant
2023-2-Q3|b.iii|main|A|1|sin2x/2 (+c)|Correct coefficient
2023-2-Q4|a|gradient|B|1|State or imply ln y=px+p+ln A|Linearised equation
2023-2-Q4|a|gradient|M|1|State p is gradient and calculate gradient|Use both given coordinates
2023-2-Q4|a|gradient|A|1|p=0.5|Accurate slope
2023-2-Q4|a|gradient|DM|1|Substitute a coordinate and simplify to A=e^k|k constant
2023-2-Q4|a|gradient|A|1|A=e^{0.693} approximately 2|Not the line intercept itself
2023-2-Q4|a|simultaneous|B|1|State or imply ln y=px+p+ln A|Shared initial step
2023-2-Q4|a|simultaneous|M|1|Form two correct equations and solve simultaneously for p|Allow one slip
2023-2-Q4|a|simultaneous|A|1|p=0.5|Accurate value
2023-2-Q4|a|simultaneous|DM|1|Substitute correctly to find A|Dependent calculation
2023-2-Q4|a|simultaneous|A|1|A=e^{0.693} approximately 2|Correct model parameter
2023-2-Q4|b|change-base|M|1|Use logarithms to make y the subject|y=log_3 2^{3x}
2023-2-Q4|b|change-base|M|1|Use log laws to obtain y=3x log_3 2|Simplify
2023-2-Q4|b|change-base|A|1|k=3log_3 2 or log_3 8|Accept correct y=(3log_3 2)x without stating k
2023-2-Q4|b|logs|M|1|Take logs both sides and use log laws|y log3=3x log2
2023-2-Q4|b|logs|M|1|Make y the subject|Change-base coefficient
2023-2-Q4|b|logs|A|1|k=3log2/log3|Condone exact value followed by decimals
2023-2-Q4|c|main|M|1|Create quadratic in log y| (log y)^2=4(log5)^2
2023-2-Q4|c|main|DM|1|Make log y the subject and simplify|Both signs
2023-2-Q4|c|main|A|1|y=25 and 1/25 (or 0.04)|Both solutions
2023-2-Q5|a|quotient|M|1|Use quotient rule correctly|Allow one slip
2023-2-Q5|a|quotient|A|1|Correct derivative (5lnx-5)/(lnx)^2|Accuracy
2023-2-Q5|a|quotient|DM|1|Set derivative equal to zero and take correct first solving step|Stationary point
2023-2-Q5|a|quotient|A|1|x=e|Accept exact value seen before decimals
2023-2-Q5|a|quotient|A|1|y=5e|Exact ordinate
2023-2-Q5|a|product|M|1|Use product rule on 5x(lnx)^{-1}|Allow one slip
2023-2-Q5|a|product|A|1|Correct derivative including chain-rule factor 1/x|Alternative printed method
2023-2-Q5|a|product|DM|1|Set derivative equal to zero and take correct first solving step|Stationary point
2023-2-Q5|a|product|A|1|x=e|Accept exact value seen before decimals
2023-2-Q5|a|product|A|1|y=5e|Exact ordinate
2023-2-Q5|b|main|B|1|Rewrite 6sin^2x as 3(1-cos2x)|Seen or implied
2023-2-Q5|b|main|B|1|Rewrite tan^2(2x) as sec^2(2x)-1|Seen or implied
2023-2-Q5|b|main|B|2|Obtain antiderivative 2x-(3/2)sin2x+(1/2)tan2x|B1 for two correct elements; 3x-x can be one element
2023-2-Q5|b|main|M|1|Apply both boundaries to ax+b sin2x+c tan2x with working to final value|Both boundaries must be shown
2023-2-Q5|b|main|E|1|Establish π/3-√3/4|Quoted result
2023-2-Q6|a|main|B|1|h=(11-3)/4=2|May be unsimplified in formula
2023-2-Q6|a|main|M|1|Use trapezium formula from positive h with correct ordinates|ln3, ln5, ln7, ln9, ln11
2023-2-Q6|a|main|A|1|11.5|Unrounded 11.5051...
2023-2-Q6|b|main|B|1|Rewrite logarithm as 6ln(x-2)|3ln((x-2)^2)
2023-2-Q6|b|main|B|1|6 times their answer to (a), giving 69.0|F.T.; SC1 for correct result but hence not used
2023-2-Q6|c|main|B|1|Correct increasing logarithmic shape and position in first and fourth quadrants|B0 if more than one graph
2023-2-Q6|c|main|B|1|Correct vertical asymptote x=2|Source graph
2023-2-Q6|c|main|B|1|Correct x-intercept (3,0)|On graph
2023-2-Q6|d|main|B|1|Under-estimate|Must be correct from their graph
2023-2-Q6|d|main|DB|1|Explain trapeziums below curve (or curve concave per table)|Dependent explanation; narrative prefers relative curve/trapezium positions
2023-2-Q7|a|main|B|2|Integrate polynomial and trigonometric terms correctly|B1 for two terms correct
2023-2-Q7|a|main|M|1|Substitute both boundaries into ax^3+b cos2x+c sinx|Including lower-bound value 2
2023-2-Q7|a|main|E|1|Rearrange to quoted iteration formula|Show all steps
2023-2-Q7|b|main|M|1|Create F(a)=0 and substitute 1.3 and 1.6|Radian mode; allow values not to 3 s.f.
2023-2-Q7|b|main|E|1|Conclude change of sign from computed values|Values 0.2536... and -0.01299...
2023-2-Q7|c|main|M|1|Use iterative formula at least two times from 1.45|Radian path only; printed degree alternative rejected by Vitalis
2023-2-Q7|c|main|M|1|Perform enough iterations to justify answer (at least three)|Each iterate six significant figures
2023-2-Q7|c|main|A|1|a=1.587|Three decimal places; intermediate iterates shown
2023-2-Q8|a|main|M|1|Use product rule to differentiate y^3 sin2x|Allow one slip, not omission of dy/dx
2023-2-Q8|a|main|A|1|Obtain 2y^3 cos2x+3y^2 sin2x dy/dx|Correct product terms
2023-2-Q8|a|main|B|1|4dy/dx and derivative of 8 equal to zero seen|Implicit differentiation notation
2023-2-Q8|a|main|E|1|Make dy/dx subject and verify quoted derivative| -2y^3 cos2x/(3y^2 sin2x+4)
2023-2-Q8|b|main|M|1|Substitute (0,2) in derivative|Find intercept from original curve
2023-2-Q8|b|main|A|1|Gradient -4|Accuracy
2023-2-Q9|a|main|B|1|Derivative of exponential has form -15e^k|k constant
2023-2-Q9|a|main|B|1|Derivative has form k e^{-t/2}|k constant not ±60
2023-2-Q9|b|definite|B|1|Integrate to -60e^{-t/2}|Antiderivative
2023-2-Q9|b|definite|M|1|Substitute both boundaries 0 and 2 in k e^{-t/2}, k not -15|Must be convinced it is an integral
2023-2-Q9|b|definite|A|1|Distance 37.9|37.9272...
2023-2-Q9|b|initial-condition|B|1|Integrate to -60e^{-t/2}+c|Alternative printed method
2023-2-Q9|b|initial-condition|M|1|Use d=0 at t=0 to obtain c=60|May be implied by c=60
2023-2-Q9|b|initial-condition|A|1|d(2)=37.9|37.9272...
2024-2-Q1|answer|main|M|1|Use quotient rule correctly|Allow one slip
2024-2-Q1|answer|main|A|1|Correct derivative numerator and denominator| ((x-2)2-(2x-3))/(x-2)^2
2024-2-Q1|answer|main|A|1|Substitute x=-4 and conclude -1/36 or -0.027 recurring|Report recommends quotient; recommendation is not ban on equivalent valid product method
2024-2-Q2|answer|main|B|1|Expand compound-angle expression|Seen or implied
2024-2-Q2|answer|main|B|1|Use cos60=1/2 and sin60=√3/2|Both seen or implied
2024-2-Q2|answer|main|M|1|Use secθ=1/cosθ leading to equation in tanθ or θ|Correct conversion
2024-2-Q2|answer|main|A|1|Obtain tanθ=4-√3 and appropriate inverse-tangent solutions|Two quadrants
2024-2-Q2|answer|main|A|1|θ=66.2 and 246.2 degrees|Both; A0 for extra answers
2024-2-Q3|answer|main|M|1|Use log laws to obtain a single logarithm on each side|Correct log combination
2024-2-Q3|answer|main|DM|1|Simplify to a three-term quadratic|4x^2-16x-48≤0
2024-2-Q3|answer|main|M|1|Solve quadratic equation by any method for critical values|Factorisation or formula working
2024-2-Q3|answer|main|A|1|Solve as a single inequality -2≤x≤6|Accuracy
2024-2-Q3|answer|main|A|1|Include logarithm conditions to give 0<x≤6|Domain restriction
2024-2-Q4|a|main|B|3|Differentiate (3e^{2x}-7)^5 to 30e^{2x}(3e^{2x}-7)^4|B1 each for 5(3e^{2x}-7)^4 and 6e^{2x}; full B3 for combined derivative
2024-2-Q4|b|main|M|1|Recognise integration as anti-derivative of their (a)|F.T. from derivative
2024-2-Q4|b|main|A|1|2(3e^{2x}-7)^5 (+c)|F.T. from their (a)
2024-2-Q5|a|main|M|1|Carry out division at least as far as 2x^2+kx|Synthetic division valid with scaling
2024-2-Q5|a|main|A|1|Quotient 2x^2+9x+9|All necessary detail
2024-2-Q5|a|main|E|1|Remainder -6|May use remainder theorem
2024-2-Q5|b|main|B|1|Identify integrand from quotient in (a)|F.T.
2024-2-Q5|b|main|M|1|Integrate obtaining at least k1 x^3 and k2 ln(2x-1)|Both term types
2024-2-Q5|b|main|A|1|2x^3/3+9x^2/2+9x-3ln(2x-1) (+c)|Accept unsimplified form; source convention omits modulus
2024-2-Q5|c|main|B|1|State or imply factorisation involving (2x-1) and quotient or other equivalent factor|F.T. from quotient; also (x+3)(4x^2+4x-3), (2x+3)(2x^2+5x-3)
2024-2-Q5|c|main|DB|1|Factorise the three-term expression to (2x-1)(2x+3)(x+3)|F.T. from their trinomial
2024-2-Q5|c|main|DB|1|Obtain relevant sin2θ=-2/3 or -1/3 from factors|F.T.; accept if correct following B0 B0
2024-2-Q5|c|main|M|1|Correct process to find θ in at least one case|Third-quadrant angles for 2θ, then divide by two
2024-2-Q5|c|main|A|1|θ=99.7 or 110.9 degrees|Both solutions
2024-2-Q6|a|main|M|1|Rewrite cos^2x=k1 cos2x+k2 with both constants nonzero|Accept formula variable A before replacement
2024-2-Q6|a|main|A|1|cos^2x=(cos2x+1)/2|Accuracy
2024-2-Q6|a|main|B|1|Rewrite reciprocal cos squared as sec^2x|Second term
2024-2-Q6|a|main|M|1|Obtain at least k3 sin2x and k4 tanx in integral|Antiderivative
2024-2-Q6|a|main|DM|1|Apply boundaries|Second boundary may be implied in this table
2024-2-Q6|a|main|E|1|Establish π/6+9√3/8|All relevant steps
2024-2-Q6|b|use-a|B|1|Form volume π integral of (cosx+1/cosx)^2 from 0 to π/3|π may be implied if seen later
2024-2-Q6|b|use-a|B|1|Expand integrand to cos^2x+1/cos^2x+2|Three terms
2024-2-Q6|b|use-a|M|1|Integrate using part (a) and integral of 2|Quoted result plus 2x
2024-2-Q6|b|use-a|A|1|Volume 5π^2/6+9√3π/8|All relevant exact working
2024-2-Q6|b|direct|B|1|Form volume π integral of squared curve|Alternative printed path; π may be seen later
2024-2-Q6|b|direct|B|1|Expand squared integrand correctly|Three terms
2024-2-Q6|b|direct|M|1|Integrate three terms directly after double-angle identity|No need to invoke (a)
2024-2-Q6|b|direct|A|1|Volume 5π^2/6+9√3π/8|Exact with working
2024-2-Q7|a|main|M|1|Set 4t^2 e^{-t}=1/4 and rearrange with working|Not change-of-sign task
2024-2-Q7|a|main|E|1|Establish t=e^{t/2}/4|Quoted positive-root formula
2024-2-Q7|b|main|M|1|Use iteration from t0=0.4 with t1 and t2 seen|One complete iteration implied
2024-2-Q7|b|main|A|1|Enough iterations to justify final answer|Four significant figures per iterate
2024-2-Q7|b|main|A|1|Final t=0.289, at least through t4|Three significant figures
2024-2-Q7|c|main|M|1|Use product rule to differentiate y=4t^2e^{-t}|Allow one slip
2024-2-Q7|c|main|A|1|Correct dy/dt=e^{-t}(8t)+4t^2(-e^{-t})|Accuracy
2024-2-Q7|c|main|B|1|dx/dt=3+12e^{-2t}|Independent derivative
2024-2-Q7|c|main|DM|1|Use dy/dx=(dy/dt)/(dx/dt) from at least one M1|Dependent on correct formula
2024-2-Q7|c|main|A|1|0.15|Unrounded 0.152...
2024-2-Q8|a|main|B|1|Correct increasing exponential shape y=3e^x|No turning up or touching x-axis
2024-2-Q8|a|main|B|1|Correct intercept 3 on increasing curve|Graphic/actual question
2024-2-Q8|a|main|B|1|Correct decreasing exponential shape y=e^{-x}|Table caption says 3e^{-x}, a source inconsistency; graph and paper say e^{-x}
2024-2-Q8|a|main|B|1|Correct intercept 1 on decreasing curve|x-axis asymptote to both; caption typo not copied
2024-2-Q8|b|exponential|M|1|Equate simultaneous exponentials leading to equation in e^{2x}|3e^x=e^{-x}
2024-2-Q8|b|exponential|A|1|e^{2x}=1/3|Accuracy
2024-2-Q8|b|exponential|DM|1|Convert exponential equation to logarithmic form|Dependent method
2024-2-Q8|b|exponential|A|1|x=(1/2)ln(1/3)|Exact asked; A0 if decimals also seen
2024-2-Q8|b|logs|M|1|Take logs of both sides using multiplication rule correctly|ln3+ln(e^x)=ln(e^{-x})
2024-2-Q8|b|logs|A|1|ln3=-2x|Accuracy
2024-2-Q8|b|logs|DM|1|Make x the subject|Dependent method
2024-2-Q8|b|logs|A|1|x=-ln3/2|Exact asked; A0 if decimals also seen
2024-2-Q9|a|main|M|1|Use sec^2x=1+tan^2x to obtain quadratic in tanx|2tan^2x-3tanx-20=0
2024-2-Q9|a|main|M|1|Solve quadratic by any means|Show method
2024-2-Q9|a|main|A|1|Conclude only positive tanx=4|Reject -2.5
2024-2-Q9|b|main|B|1|Use correct tan addition formula|tan(x+3π/4)
2024-2-Q9|b|main|M|1|Use their tanx and tan(3π/4)=-1|F.T. from (a)
2024-2-Q9|b|main|A|1|3/5|Exact value
2024-2-Q10|a|main|B|2|Obtain y'=9/(3x+10)-2/x|B1 for correct structural derivative with nonzero constant coefficients
2024-2-Q10|a|main|M|1|Set derivative to zero leading to linear equation in x from at least B1|9x=2(3x+10)
2024-2-Q10|a|main|A|1|x=20/3|Stationary value
2024-2-Q10|b|main|M|1|Use their y' to calculate second derivative|F.T.
2024-2-Q10|b|main|A|1|Show y''>0 and conclude minimum|Correct answer only; y''=3/200
2024-2-Q11|a|main|B|2|V-shape with vertex on positive x-axis and straight line with negative y-intercept/positive gradient, crossing x-axis left of V vertex|B1 each shape; intercept labels unnecessary; straight by eye accepted
2024-2-Q11|b|main|M|1|Solve equation with negative leg of modulus, or square and expand to quadratic|Accept if both legs used; one slip allowed in expansion
2024-2-Q11|b|main|A|1|x=5a/4|Condone x=-3a/2 also seen
2024-2-Q11|b|main|A|1|y=11a/16|A0 if two solutions stated
2024-2-Q11|c|main|B|1|x<5a/4|F.T. from positive x-value in (b) if two solutions given
'''
