"""Author-selected marking conventions after reading every 8227 report section.
Anchors are checked against the independently frozen report extraction.
Question-specific observations must never be promoted to universal penalties.
"""
# year | PDF page | question key (or general) | part or * | type | excerpt anchor | operational reading
SPEC = r'''
2021|231|general|*|method required|the conclusion must always be stated again|For show/prove tasks, finish with the stated conclusion after valid working.
2021|236|general|*|method required|Complete methods should be shown at all times|Method-bearing tasks need complete working; apply actual award rows, including independent B marks and exceptions.
2021|236|general|*|exact form|answers should be left exact where possible|Prefer exact form where possible; explicit part instructions govern.
2021|236|general|*|precision and rounding|only to round their final answer|Retain intermediate precision.
2021|236|general|*|method required|Candidates may NOT work backwards from the quoted answer|Proof/show-that evidence must lead forward to the conclusion.
2021|236|general|*|method required|the previous answer must be used|Hence requires earlier result; specific SC rules may still award limited credit.
2021|236|general|*|accepted alternative method|there are other (more complicated) methods that could be used|Hence or otherwise permits another valid method; not a requirement to use the scaffold.
2021|238|2021-2-Q3|answer|answer format|Must be a single inequality|Give the single connected solution interval as one double inequality.
2021|238|2021-2-Q4|b|precision and rounding|the number of complete weeks|Report prose requires 34 complete weeks, but award row accepts 35; retain conflict for branch review.
2021|239|2021-2-Q5|b|method required|calculator|Hence expects recognition of the earlier derivative, not unsupported calculator integration.
2021|240|2021-2-Q8|c.i|precision and rounding|5 d.p.|Use supplied starting value and show iterates to the requested precision.
2021|241|2021-2-Q9|a|recurring error that loses marks|constant|Indefinite integration requires the arbitrary constant when the task requires a general antiderivative.
2021|242|2021-2-Q12|*|angle units|radians|Use units dictated by the given domain and exact special-angle values.
2022|307|general|*|method required|Complete methods should be shown at all times|Show methods for method-credit tasks; not an automatic zero for all answer-only B criteria.
2022|307|general|*|exact form|answers should be left exact where possible|Prefer exact answers where possible.
2022|307|general|*|precision and rounding|only to round their final answer|Avoid premature rounding.
2022|307|general|*|answer format|the work at the original question was marked|Paper convention: cancel abandoned work and explicitly refer to replacement work; app response-selection policy remains a PLAN decision.
2022|307|general|*|angle units|change their calculator settings from degrees into radians|Use the required calculator mode; working in degrees then converting is discouraged.
2022|307|general|*|answer format|NOT TO CHANGE the given variable|Keep the question variable and replace formula-sheet variables appropriately.
2022|308|2022-2-Q1|b|method required|conversion from exponential form to log form|Explicit logarithmic method must be shown.
2022|309|2022-2-Q3|b|accepted alternative method|product rule|Chain rule or valid product-rule expansion may be used.
2022|310|2022-2-Q3|c|method required|both boundaries|Show substitution of both integration boundaries, including zero.
2022|311|2022-2-Q5|a|method required|steps|Quoted result requires all intermediate algebraic steps.
2022|312|2022-2-Q5|c|precision and rounding|5 decimal places|Show iteration values to the requested five decimal places before final rounding.
2022|312|2022-2-Q6|a|precision and rounding|2 decimal places|Use the requested phase-angle precision.
2022|313|2022-2-Q7|*|recurring error that loses marks|quotient|No quotient rule for integration; transform identities before integrating.
2022|315|2022-2-Q9|b.ii|follow-through behaviour|use any wrong value they found in part (a)|Wrong prior domain boundary can be followed through in this part; do not generalise.
2022|315|2022-2-Q9|c.ii|answer format|undefined|Undefined/non-real is acceptable; a calculator error message is not a mathematical answer.
2022|316|2022-2-Q10|b|method required|parallel to the y-axis|A vertical parametric tangent is located with dx/dθ=0, not dy/dx=0.
2023|321|general|*|answer format|first answer|Paper marks the first uncancelled answer; this is evidence, not an implemented app rule.
2023|325|2023-1-Q6|a|precision and rounding|3 significant figures|Keep an unrounded working value before the requested three-significant-figure result.
2023|325|2023-1-Q7|a.ii|follow-through behaviour|gained follow- through marks|Follow through the earlier vector in this specific part.
2023|330|general|*|method required|Complete methods should be shown at all times|Use award criteria; independent accuracy/statement marks retain their source meaning.
2023|330|general|*|exact form|answers should be left exact where possible|Prefer exact form where appropriate.
2023|330|general|*|precision and rounding|only to round their final answer|Retain full intermediate values.
2023|330|general|*|angle units|correct setting|Set calculator mode when reading the question.
2023|331|2023-2-Q1|b|recurring error that loses marks|without any working|Three correct brackets alone score zero; source also grants SC1 for isolated correct quadratic factorisation with working.
2023|333|2023-2-Q3|b.ii|exact form|Must be exact|Use exact special-angle values, not decimal approximations.
2023|335|2023-2-Q4|b|accepted alternative method|Condone if correctly seen and then decimals used|Exact coefficient followed by a decimal is condoned here; contrast 2024 P2 Q8(b).
2023|336|2023-2-Q5|a|accepted alternative method|Use product rule correctly|Both quotient and product methods receive the printed tariff.
2023|336|2023-2-Q5|b|method required|both boundaries|Both boundaries must be shown for this quoted integral result.
2023|337|2023-2-Q6|b|follow-through behaviour|their (a)|6 times their (a); SC1 if correct but hence not used.
2023|337|2023-2-Q6|c|recurring error that loses marks|B 0 if more than one graph seen|A second unlabelled/wrong graph can invalidate the shape mark in this table.
2023|337|2023-2-Q6|d|answer format|Reference must be made to both the curve, as well as the trapezium|Justify under/overestimate by relative trapezium/curve position, not slope alone.
2023|338|2023-2-Q7|b|angle units|radians|Radian mode is required by owner decision; reject the printed degree-mode alternative in (c).
2023|338|2023-2-Q7|c|precision and rounding|6 significant figures|Every iterate is required; final value is to three decimal places.
2023|339|2023-2-Q9|b|accepted alternative method|Substitute d = 0|Either definite integration or indefinite integration with initial condition is accepted.
2024|325|general|*|answer format|first answer|Paper convention about first uncancelled response, not an app capability claim.
2024|335|general|*|method required|Complete methods should be shown at all times|Show working for method-bearing tasks; apply criterion-level exceptions.
2024|335|general|*|precision and rounding|only to round their final answer|Retain intermediate precision.
2024|335|general|*|angle units|correct setting|Use the units of the question/domain.
2024|336|2024-2-Q1|answer|accepted alternative method|not advisable to change a quotient rule into a product rule|Report discourages a valid but error-prone method; it does not prohibit all equivalent product-rule solutions.
2024|337|2024-2-Q3|answer|answer format|Include log conditions|Restrict quadratic interval to logarithm domain, 0<x≤6.
2024|337|2024-2-Q4|b|follow-through behaviour|F.T.|Both method and accuracy awards follow their derivative.
2024|338|2024-2-Q5|c|follow-through behaviour|F.T. from their relevant factors|Specified dependent B criteria follow earlier factorisation; final A still requires both correct angles.
2024|339|2024-2-Q6|a|method required|Second boundary may be implied|This table permits implied second boundary; do not override with a universal always-write-zero rule.
2024|340|2024-2-Q7|b|precision and rounding|4 significant figures|Iterates to four significant figures; final answer to three significant figures.
2024|341|2024-2-Q8|b|exact form|A 0 if decimals seen as well|Part-specific exact-form rule is stricter than 2023 P2 Q4(b).
2024|342|2024-2-Q9|b|follow-through behaviour|Use their tan|Follow their positive tan value with exact compound-angle substitution.
2024|342|2024-2-Q10|b|follow-through behaviour|c.a.o.|Second derivative method follows through; classification accuracy is correct-answer-only.
2024|343|2024-2-Q11|a|answer format|No need to see the intercepts on the axes|Shape and relative positions suffice; straight by eye is accepted here.
2024|343|2024-2-Q11|c|follow-through behaviour|positive x-value|Follow the positive intersection from (b), including when two values were given.
2025|345|general|*|answer format|first answer|First uncancelled paper response is marked; app policy is not decided here.
2025|347|2025-1-Q4|b|answer format|ruler|For this sketch the commentary requires a ruled line; differs from 2024 P2 Q11(a).
2025|351|2025-1-Q9|c|accepted alternative method|show all the working to support their conclusion|Either second derivative or evidenced first-derivative sign change may classify the stationary point.
2025|353|2025-1-Q12|b|follow-through behaviour|A follow-through mark was allowed|Specific follow-through for point B from the incorrect line BD intercept.
2025|355|general|*|method required|Complete methods should be shown at all times|Working supports partial method credit; criterion-level tariffs govern.
2025|355|general|*|precision and rounding|confused significant figures and decimal places|Keep full values in working and apply requested final precision.
2025|355|general|*|angle units|correct setting|Calculator mode follows question units.
2025|355|general|*|answer format|Candidates must not use tables|Sketch the basic exponential/logarithmic/trigonometric/modulus shape and transformations.
2025|359|2025-2-Q5|answer|accepted alternative method|substitute|Substituting the point before isolating dy/dx is allowed; preserve correct implicit differentiation.
2025|359|2025-2-Q6|b|follow-through behaviour|correct substitution of their a-value|Earlier base a can follow through except inadmissible a≤0 or a=1.
2025|361|2025-2-Q9|a|precision and rounding|3 decimal places|Use the requested3decimalplaces for the final phase angle. The prose condones showing more decimals before rounding; it does not waive final precision generally.
2025|363|2025-2-Q11|b|precision and rounding|not penalised|Source condones 138 after 138.629 is seen in this question; not a general round-down convention.
2025|364|2025-2-Q12|d|precision and rounding|3 s.f.|Show iterates until rounded agreement and state the final value explicitly.
2021|236|general|*|method required|No marks are awarded if only answers are given|Answers produced without supporting working earn no marks; the reports cite calculators that differentiate, integrate or solve cubics. Exact part instructions and explicit B, SC and F.T. awards still govern.
2021|236|general|*|method required|no marks may be awarded for the solution|Hence requires using the previous result; general prohibition subject to source-specific SC and award rows.
2022|307|general|*|answer format|the variables used on the formula sheet must be replaced|Replace formula-sheet variable names with the question variable; do not rename the given variable.
2024|335|general|*|method required|The factorisation or substitution into the quadratic equation must be shown at all times|Show factorisation or the substitution into the quadratic formula when solving quadratics; calculator roots alone do not demonstrate method.
2022|315|2022-2-Q9|b.i|answer format|to score full marks|Final inverse must be denoted f^(-1)(x), not y; this source differs from2022P1Q6(b), which explicitly allows y.
2024|331|2024-1-Q10|b|answer format|coordinate form and not vector form|Use unit-vector or column-vector form; coordinate tuple(-12,8,0) is not accepted for this vector response.
2025|346|2025-1-Q1|b|answer format|lost the accuracy of their answer|Use and for the intersection interval; or wrongly joins the two bounds and loses accuracy.
2025|347|2025-1-Q4|a|answer format|A sketch drawn outside the domain will not be accepted|Sketch only the stipulated domain; table B0 condition applies to the shape mark.
2023|337|2023-2-Q6|a|precision and rounding|at least 4 decimal places|Use logarithms exactly or at least4decimalplaces for trapezium ordinates, preserving final-answer accuracy.
2023|337|2023-2-Q6|c|recurring error that loses marks|without labels, it resulted in the loss of all marks|Drawing both logarithmic and exponential graphs without labels loses all marks for this question; do not promote to universal sketch penalty.
2024|337|2024-2-Q5|c|recurring error that loses marks|it is not correct and no marks will be awarded|Do not replace factor2x+3 by x+3/2 without its scalar factor when factorising the polynomial.
2023|334|2023-2-Q4|b|exact form|the exact value of k must be given|Final coefficient k must be exact; printed award condones a later decimal only after a correct exact expression is seen.
2021|239|2021-2-Q6|b|recurring error that loses marks|2 solutions instead of one, lost the accuracy mark|Only the acute angle is asked; an extra solution loses the accuracy mark.
2021|240|2021-2-Q8|c.i|answer format|the first two solutions the candidates wrote down were marked|The first two written iterates are marked. Use the supplied start and at least5decimalplaces.
2025|364|2025-2-Q12|a|answer format|Correct ruled V-shape|This award requires a ruled modulus graph; source-specific and distinct from straight-by-eye2024award.
2021|232|2021-1-Q4|*|recurring error that loses marks|did not find the value of|An omitted integration constant in(a) affects both connected parts; use the stated initial condition and exact source follow-through.
2021|232|2021-1-Q5|b|method required|all steps must be shown|Proof requires all establishing steps, not just the final identity.
2021|233|2021-1-Q7|a|answer format|many answers were not simplified|The requested perimeter must be simplified; finalB1awards the simplified expression.
2021|234|2021-1-Q10|a|answer format|not as two separate inequalities|Give one double inequality for the connected interval between critical values.
2021|234|2021-1-Q10|b|method required|it must be proved firstly|Calculate the discriminant and establish positivity before concluding two real roots; perfect-square alone is not the conclusion.
2021|236|general|*|answer format|“SHOWN” is NOT an acceptable conclusion|A proof ends with the actual required conclusion; the word SHOWN alone does not establish it.
2021|237|2021-2-Q1|b|recurring error that loses marks|divide the answer|Synthetic division at a fractional root needs the correct scaling for the stated non-monic divisor; root and factor are distinct.
2021|238|2021-2-Q4|a|answer format|The descending curve must only be in the first quadrant|Respect t>=0 in the contextual decay sketch. The interceptB1has its own explicit second-quadrant allowance.
2021|238|2021-2-Q4|b|method required|It is not an acceptable method|Trial-and-error numerical guesses do not supply the expected logarithmic method.
2021|241|2021-2-Q10|a|answer format|expected markers to do the differentiation for them|Write evaluated implicit derivatives including dy/dx, not unevaluated differentiation operators.
2021|242|2021-2-Q12|b|recurring error that loses marks|lost both accuracy marks|Additional angles outside the requested domain lose both accuracy marks in this source.
2022|302|2022-1-Q4|answer|answer format|not as two separate inequalities|The connected discriminant interval must be written as a double inequality.
2022|308|2022-2-Q2|answer|answer format|Another variable like|Use a fresh substitution variable for e^x, not x itself. Replace it by e^x before the method award.
2022|309|2022-2-Q3|b|exact form|the substitution of the angle must be clearly shown|Show substitution of the angle in the derivative and leave the answer exact; no decimal final solution.
2022|313|2022-2-Q7|*|recurring error that loses marks|lose all their marks in the question|Changing the given x to A loses the question marks according to this report; preserve as a question-specific remark, not universal symbolic-equivalence policy.
2021|236|general|*|answer format|Candidates must not be encouraged to use tables|Use the basic graph shape and transformations instead of plotting a numerical table.
2023|321|general|*|recurring error that loses marks|avoid spoiling correct answers|An invalid rewriting can spoil a correct answer; do not invent a fixed penalty for an equivalent form.
2025|345|general|*|recurring error that loses marks|Learners who misread numbers do not score maximum marks|A correct method on misread data does not imply full accuracy credit; criterion-level treatment remains specific.
2025|347|2025-1-Q4|b|answer format|label the y-intercept and the x -intercept|Label straight-line intercepts for this question; no universal override of contrary sketch awards.
2025|348|2025-1-Q5|a|accepted alternative method|This was accepted as a correct answer|Recognising the geometric progression R directly and summing it is accepted instead of separate progression sums.
2025|352|2025-1-Q11|a|method required|Incomplete methods will not gain the student any marks|All establishing steps must lead to the quoted equation; retain source-specific E-mark conditions.
2025|358|2025-2-Q4|b|answer format|graphs must clearly be labelled|Label auxiliary sine and required cosecant graphs and compare chord positions to justify overestimate.
'''
