"""Authored NSSCO exam-evidence guidance for generated maths.

All tariffs are draft adaptations; this module neither approves content nor calls AI.
Shared by the review-pack builder and the instance-bound grading contract.
"""
from __future__ import annotations

# Each profile states achievements, never a count of matching model steps.
# Award ladders are expressed as mutually exclusive total caps, not additive M2/M3.
PROFILES = {}

def profile(name, awards, note='', alternatives=''):
    PROFILES[name] = {'awards': [{'marks':m,'achievement':a} for m,a in awards],
                      'note':note,'alternative_partial_credit':alternatives}

profile('answer1', [(1,'The requested answer is correct, including the specifically requested form.')],
        'Correct-answer-only item. No invented method mark or half mark.')
profile('calculation2', [(1,'Correct mathematical setup or substantive intermediate achievement specified for this task.'),
                         (1,'Correct result from a valid method, with the required form and accuracy.')],
        'The first award requires application to the question, not an unused formula. '
        'A valid setup with an arithmetic slip can retain its method mark.')
profile('calculation3', [(1,'Correct first mathematical achievement specified for this task.'),
                         (1,'Correct subsequent operation or rearrangement towards the requested result.'),
                         (1,'Correct final result in the requested form.')],
        'Interpret the first two achievements as the one- and two-mark method stages. '
        'Do not add a cumulative M2 to M1. Equivalent valid routes can establish the same achievements.')
profile('two_values2', [(1,'First requested value is correct.'),(1,'Second requested value is correct.')],
        'Credit the two distinct values, preserving variable/coordinate pairing and order where meaningful.')
profile('factors2', [(1,'One correct mathematical linear factor.'),(1,'The other correct linear factor.')],
        'Factor order does not matter. Do not require a particular algorithm. '
        'A list of roots does not answer a request for a product of factors. '
        'For equivalent redistribution of constant factors, assess the mathematical factorisation, not substrings.')
profile('common_factor2', [(1,'A correct nontrivial partial factorisation.'),
                          (1,'The complete common factor has been extracted and the product is correct.')],
        'A complete correct answer earns both marks, including the partial achievement it implies. A correct but incomplete factorisation earns only the first mark. Never add further special-case marks above the two-mark total.')
profile('grouping3', [(1,'Correct partial grouping/factorisation.'),
                    (1,'Both groups expressed with a valid common binomial factor.'),
                    (1,'Complete correct product of factors.')],
        'Source M1/M2 stages are cumulative totals of 1 and 2, not 1 + 2 additional marks.')
profile('square3', [(1,'Correctly extract the leading coefficient from all terms, or equivalent initial square-completion achievement.'),
                   (1,'Correctly form the square with its compensating constant.'),
                   (1,'Correct completed-square expression in the requested form.')],
        'Use cumulative method stages. For a=1, extracting 1 is not an achievement: '
        'the initial achievement must be the substantive square/completing adjustment. '
        'The monic adaptation is separately labelled; never award for merely rewriting the given expression.',
        '2020 P1 Q17 alternative B1: for target a(x+p)^2+q, a completed-square-shaped '
        'answer with the correct leading coefficient OR correct inside shift OR correct outside constant '
        'can earn one mark in the first criterion even without method working. '
        'This is ONE alternative partial mark, not one mark per matching parameter. '
        'Without further correct method evidence an incorrect expression is capped at 1/3. '
        'It replaces the first-stage award and is never added to it.')
profile('square_point5', [(1,'First substantive completed-square achievement.'),
                        (1,'Correct square and compensating adjustment.'),
                        (1,'Correct completed-square expression.'),
                        (1,'Correct x-coordinate of the turning point, including supported follow-through.'),
                        (1,'Correct y-coordinate of the turning point, including supported follow-through.')],
        'Two tasks: expression [3], turning point [2]. Read the learner\'s own a(x+p)^2+q '
        'for the later coordinates (-p,q). Award both coordinate marks for correct follow-through '
        'even when the earlier outside constant is wrong. Do not give the whole five marks for either part alone.',
        'Apply the 2020 P1 Q17 structural B1 alternative within the first criterion: '
        'an expression a(x+p)^2+q with the correct leading coefficient OR inside shift OR outside constant '
        'can earn one expression mark. Without further correct method evidence an incorrect expression '
        'is capped at 1/3, regardless of how many parameters match. This is not an extra mark. '
        'Assess the two turning-point follow-through marks separately from that expression cap.')
profile('algebra_fraction3', [(1,'Correct denominator/common-factor or combination achievement for the stated operation.'),
                            (1,'Correct factorisation, numerator expansion or cancellation achievement towards one fraction.'),
                            (1,'Correct final fraction in the specifically requested form.')],
        'Respect cumulative stage caps. Equivalent expanded/factored denominators are allowed '
        'unless the question imposes a form. Do not penalise a mathematically valid alternative route.',
        'Apply source SC/B alternatives for a correct numerator or denominator without adding '
        'them to marks already earned for that same achievement. Source-dependent edge cases need review.')
profile('polynomial3', [(2,'Correct quotient, with up to one of these marks available for a correct division process with a slip.'),
                       (1,'Correct remainder.')],
        'The source process M1 is an alternative partial award within the quotient/process '
        'allocation, not an extra fourth mark. Report both quotient and remainder.')
profile('fractions3', [(1,'Correct improper-fraction representation or equivalent preparatory achievement.'),
                      (1,'Correct fractional operation, including reciprocation when dividing.'),
                      (1,'Correct final value in the requested fractional or mixed-number form.')],
        'The two-mark method stage includes the initial achievement; do not double count it.')
profile('matrix_entries2', [(1,'At least two correct matrix entries in their proper positions.'),
                           (1,'All entries correct in their proper positions.')],
        'For a 2 by 2 result: zero/one correct entry = 0; two/three = 1; four = 2. '
        'Not a quarter mark per entry. Different matrix dimensions need a flagged adaptation.')
profile('inverse2', [(1,'Correct determinant or correct adjugate as allowed by the source.'),
                    (1,'Correct complete inverse including determinant scaling.')],
        'Do not insist on both determinant and adjugate for a partial mark offered for either. '
        'A singular matrix has no inverse; do not apply this profile to a singularity question.')
profile('matrix_method5', [(1,'Correct matrix equation for the simultaneous system.'),
                          (1,'Correct determinant or adjugate achievement.'),
                          (1,'Correct inverse including its scalar factor.'),
                          (1,'Correct x-value.'),(1,'Correct y-value.')],
        'A different valid method can earn the two correct-value marks, but not the '
        'three marks for the explicitly required matrix method. The source\'s printed '
        'answer cell 640 is unrelated: use the verified system and scheme.')
profile('simultaneous3', [(1,'Correct elimination/substitution or another valid solving method.'),
                         (1,'Correct first unknown.'),(1,'Correct second unknown.')],
        'Accept a valid alternative method unless the question requires a specific one; '
        'keep variable labels and paired solutions intact.')
profile('nonlinear5', [(1,'Correct substitution/equating of the two supplied expressions for y.'),
                      (1,'Correct resulting quadratic equation.'),
                      (1,'A valid method to solve the quadratic.'),
                      (1,'Correct roots/one complete solution pair at the source partial stage.'),
                      (1,'Both complete solution pairs correctly associated.')],
        'Five-mark adaptation of 2021 P2 Q8(c): the generated equations already give y, '
        'so omit the source B1 for isolating a variable. Do not award a mark for repeating '
        'an equation already supplied. The remaining five achievements are retained; '
        'this is not a source-printed five-mark tariff for this new line/parabola task.')
profile('quadratic4', [(1,'Correct standard form and substitution in a valid quadratic method.'),
                      (1,'Correct discriminant/solution process.'),
                      (1,'One correct root.'),(1,'The other correct root.')],
        'Apply the question\'s accuracy. Do not lose negative-root solutions in a pure algebra question.')
profile('quadratic_context3', [(1,'Correct substitution or equivalent solving setup.'),
                              (1,'Correct solution process.'),
                              (1,'The valid contextual result, rejecting an inadmissible root.')],
        'Rejecting an inadmissible negative length matters; do not require every algebraic root '
        'as the final contextual answer.')
profile('roots2', [(1,'One correct root.'),(1,'The other correct root.')],
        'Use only for two distinct roots. A repeated root does not earn two independent copies '
        'of the same mark; such a branch needs the square-equation/calculation interpretation.')
profile('inequality3', [(1,'Correct bound/first inequality achievement.'),
                      (1,'Correct second bound or subsequent rearrangement.'),
                      (1,'Complete solution set with correct directions and boundary inclusion.')],
        'Do not replace an inequality by an equation. Reverse the direction after multiplying '
        'or dividing by a negative. Equivalent interval notation is acceptable when it conveys the full set.')
profile('indices4', [(1,'Correctly express relevant quantities with a common base.'),
                    (1,'Correctly apply product/power laws.'),
                    (1,'Correctly apply quotient law or combine remaining exponents.'),
                    (1,'Correct final single-power expression.')],
        'One-/two-/three-mark source stages are cumulative caps, not additive M1+M2+M3.')
profile('bounds2', [(1,'Both numerical endpoints correctly established.'),
                   (1,'Complete correct inequality, including lower/upper inclusion.')],
        'The source has B1 for both bounds seen and SC1 for reversed bounds: these are '
        'alternative partial routes. Do not award one mark for each endpoint and a third for the signs.')
profile('bounds3', [(1,'Choose all relevant upper/lower input bounds correctly.'),
                   (1,'Correct bound calculation using those inputs.'),
                   (1,'Correct unrounded limiting result.')],
        'For a maximum difference use upper minuend minus lower subtrahend. For a maximum '
        'positive ratio use upper numerator and lower denominator. Do not round exact limiting answers.')
profile('volume_bounds5', [(1,'Correct lower bound for the first dimension.'),
                         (1,'Correct lower bound for the second dimension.'),
                         (1,'Correct lower bound for the third dimension.'),
                         (1,'Correct volume operation.'),(1,'Correct unrounded result or source-authorised follow-through.')],
        'Three input dimensions plus multiplication. Do not apply the five-mark tariff to a two-input bound problem.')
profile('line3', [(1,'Correct gradient or the required parallel/perpendicular gradient relationship.'),
                 (1,'Correct point substitution/intercept determination.'),
                 (1,'Complete correct line equation.')],
        'Equivalent point-slope and rearranged line equations are acceptable. Do not require '
        'y=mx+c unless the question specifically asks for that form.')
profile('mean_change3', [(1,'Correct original total from old mean and count.'),
                       (1,'Correct new total from new mean and count.'),
                       (1,'Correct difference giving the added value.')],
        'Do not subtract the two means as if they were the two totals.')
profile('grouped_mean4', [(1,'Correct class midpoints.'),
                        (1,'Correct frequency-weighted midpoint calculation; dependent on correct class midpoints.'),
                        (1,'Correct weighted total divided by total frequency; dependent on the preceding correct midpoint and weighted calculation stages.'),
                        (1,'Correct estimated mean at the requested accuracy.')],
        '2022 P2 Q17(c) prints M1, DM1, DM1: if incorrect midpoints prevent the first '
        'method mark, do not award either dependent method mark just for multiplying '
        'or dividing that incorrect calculation by the total frequency. A claim to '
        'have used a method without the required mathematical evidence is insufficient. '
        'The histogram FT rule in part (d) does not apply to this mean. The fourth full-answer credit is '
        'interpreted from the total where the printed row omits an explicit A label.')
profile('density_mean5', [(1,'Recover frequencies using class width times density.'),
                        (1,'Correct midpoints.'),(1,'Correct weighted total.'),
                        (1,'Divide by total recovered frequency.'),(1,'Correct rounded estimate.')],
        'Explicit combined-task adaptation: density conversion [1] plus grouped mean [4]. '
        'This five-mark combined allocation is proposed, not printed as such in a source question.')
profile('three_conditions3', [(1,'First requested condition is expressed correctly.'),
                             (1,'Second requested condition is expressed correctly.'),
                             (1,'Third requested condition is expressed correctly.')],
        'Assess the mathematical inequalities and boundaries, not a literal order of writing.')
profile('table_entries', [(1,'Each requested table value is independently correct in its required position.')],
        'Total is the number of requested entries for the specific instance; do not count '
        'values already supplied. This follows the source\'s per-entry award, with changed entry count labelled as adaptation.')
profile('cf_table2', [(1,'At least two correctly calculated entries in the required order.'),
                     (1,'All requested entries correct.')],
        'Source offers B1 for any two and full marks for the complete column. Extending the '
        'same two-mark cap to a different number of entries is an explicit tariff adaptation.')
profile('probability_paths3', [(1,'Correct product for the first relevant mutually exclusive path.'),
                            (1,'Correct product for the other relevant path.'),
                            (1,'Correct sum and final probability.')],
        'Equivalent complement methods are acceptable where they cover exactly the requested event. '
        'Do not add dependent branch probabilities along a path.')
profile('probability_total3', [(1,'Correct route/joint probability for one branch of the partition.'),
                            (1,'Correct route/joint probability for the other branch.'),
                            (1,'Correct total for the requested event.')],
        'Use total probability: multiply along each route and add across the disjoint routes. '
        'A question asking for just one joint event does not need this three-mark sum profile.')
profile('probability_complement4', [(1,'Correct event/complement identification.'),
                                  (1,'Correct first conditional/branch factor.'),
                                  (1,'Correct remaining factors/product or complete alternative event sum.'),
                                  (1,'Correct requested probability.')],
        'Use without-replacement totals at each draw. Cumulative source stages are total caps. '
        'Keep a source-authorised follow-through tied to the learner\'s own earlier branch values.')
profile('enlargement3', [(1,'Enlargement identified.'),(1,'Correct scale factor.'),(1,'Correct centre.')],
        'Description components, not a compulsory sentence. Do not reuse for other transformation types.')
profile('rotation3', [(1,'Rotation identified.'),(1,'Correct angle with its direction.'),(1,'Correct centre.')],
        'Equivalent signed-angle/direction descriptions allowed. Angle and direction form one achievement.')
profile('translation2', [(1,'Translation identified.'),(1,'Correct directed translation vector.')],
        'Vector direction is from object to image. Reversed vector is not equivalent.')
profile('reflection2', [(1,'Reflection identified.'),(1,'Correct mirror line.')],
        'Analogy from full transformation descriptions; the one-mark source for drawing '
        'a reflection is not direct evidence for this two-mark description tariff.')
profile('image_coordinates3', [(1,'Correct first labelled image coordinate pair.'),
                             (1,'Correct second labelled image coordinate pair.'),
                             (1,'Correct third labelled image coordinate pair.')],
        'Typed-coordinate adaptation. Source drawing schemes distinguish shape and position, '
        'which is not equivalent to a per-coordinate rubric. The proposed three-pair award '
        'requires review and does not claim to assess drawing accuracy.')
profile('cosine_angle4', [(1,'Correct cosine-rule equation with appropriate sides/opposite angle.'),
                        (1,'Correct rearrangement for cosine of the requested angle.'),
                        (1,'Correct inverse-cosine calculation retaining precision.'),
                        (1,'Correct angle at the requested accuracy.')],
        'This follows the four-mark cosine-rule-angle source, not a general tariff for every trig calculation.')
profile('trig_equation3', [(1,'Correct isolated trigonometric ratio or reference angle.'),
                        (1,'One valid solution in the stated interval.'),
                        (1,'The other valid solution in the stated interval.')],
        'Use the actual interval; do not invent a second solution if the question has only one.')

# Every registered level is assigned deliberately. No lesson-name/token matching.
# R = profile, evidence id(s), task-specific creditworthy mathematical demand.
RULES = {}
def levels(gid, rows):
    for level,row in enumerate(rows,1):
        RULES[(f'nssco_{gid}',level)] = {'profile':row[0], 'sources':row[1].split(), 'demand':row[2]}

levels('advanced_percentages', [
 ('calculation2','2020-P1-Q8a 2021-P1-Q7','Use the correct original base and increase/decrease/remaining multiplier; calculate the requested amount.'),
 ('calculation2','2023-P1-Q10 2024-P1-Q11','Find profit or loss and divide by cost price, then express as a percentage.'),
 ('calculation2','2020-P1-Q8b 2022-P1-Q18','Divide the changed amount by the correct percentage multiplier to recover the original.'),
 ('calculation2','2023-P2-Q1b 2022-P2-Q11b','Use change divided by original, or the requested part divided by whole, times 100.'),
 ('calculation2','2020-P1-Q29','Use the compounded growth/depreciation multiplier for every period; subtract the principal only if interest is requested.')])
levels('fractions_decimals_percentages', [
 ('answer1','2020-P1-Q1 2021-P1-Q2a 2021-P1-Q2b','Convert the number into the specifically requested decimal, fractional or percentage form.'),
 ('answer1','2023-P1-Q2 2022-P1-Q10 2020-P2-Q1e','Write an equivalent fraction, mixed number or exact recurring-decimal fraction, or find the specified fraction of a quantity.'),
 ('answer1','2024-P1-Q7a 2024-P1-Q2a','Compare the actual values without changing the requested list elements or inequality symbol.'),
 ('fractions3','2020-P1-Q12 2024-P2-Q3','Use exact fractions and the correct addition, subtraction, multiplication or division; finish in the requested form.'),
 ('calculation2','2022-P1-Q12','Invert the given fraction to recover the whole; successive-fraction tasks instead use the fraction of the remainder.')])
levels('ratios_scales_rates', [
 ('calculation2','2022-P1-Q6 2021-P1-Q12','Simplify a ratio after common-unit conversion, or divide a quantity by the sum of ratio parts before sharing.'),
 ('calculation2','2021-P1-Q12 2022-P1-Q13','Use the value of the known ratio part to find one part, then the requested other part or total.'),
 ('calculation2','2021-P1-Q15','Apply the scale in the correct direction and convert between map and real-distance units.'),
 ('calculation2','2022-P1-Q19 2022-P1-Q11','Use the direct rate or inverse work relationship appropriate to the context; do not invert both by default.'),
 ('calculation2','2023-P1-Q13b 2022-P2-Q2b','Use distance=speed*time and total distance/total elapsed time for average speed; convert time units correctly.')])
levels('number_classifications_properties', [
 ('answer1','2024-P2-Q1a 2024-P2-Q1b','Select the number satisfying the requested mathematical classification, not every plausible item.'),
 ('answer1','2021-P2-Q1a','Correct rational/irrational/real classification after interpreting the entire expression.'),
 ('calculation2','2020-P1-Q9a 2021-P1-Q6a','Obtain the prime factors with multiplicities and write their product; a list of factors is only the source partial achievement.'),
 ('answer1','2024-P2-Q2a 2024-P2-Q2b','Correct HCF or LCM as requested; do not interchange the two.'),
 ('answer1','2023-P1-Q1 2022-P1-Q2 2023-P1-Q3','Correct positional value, number in words/figures, or all primes in the stated range.')])
levels('directed_numbers_in_action', [
 ('answer1','2020-P1-Q4','Use final minus initial for the requested directed temperature change.'),
 ('answer1','2022-P1-Q7','Apply the signed increase/drop to the initial value.'),
 ('answer1','2022-P1-Q9c','Compare signed quantities with the requested relation.'),
 ('answer1','2024-P1-Q1','Evaluate the directed-number expression using operation order and signs.'),
 ('calculation2','2020-P1-Q3','Set up the signed change in balance or position and obtain the correct final value.')])
levels('standard_form_estimates_approximations', [
 ('answer1','2024-P1-Q3c 2021-P1-Q4','Convert in the requested direction; standard form requires a coefficient between 1 and 10 for positive inputs.'),
 ('answer1','2024-P1-Q3a 2024-P1-Q3b 2022-P1-Q3','Apply the particular decimal-place, significant-figure or nearest-unit instruction.'),
 ('calculation3','2020-P1-Q13a 2020-P1-Q13b','Round each operand as instructed, show those rounded values, and evaluate the estimate from them.'),
 ('calculation2','2020-P2-Q2','Perform the numerical operation correctly, then normalise the final result to the requested form.'),
 ('calculation2','2021-P1-Q1 2023-P1-Q4','Enter/evaluate the entire calculator expression correctly and follow the explicit final-accuracy instruction.')])
levels('limits_of_accuracy', [
 ('bounds2','2022-P1-Q17','Find the two half-unit endpoints at the stated measurement precision and place the correct inequalities.'),
 ('answer1','2022-P1-Q17','Choose the specifically requested single upper/lower bound; retain the half-unit precision.'),
 ('bounds3','2020-P1-Q7 2023-P1-Q17','Choose matching extremal length/width bounds for area or perimeter and combine them without rounding.'),
 ('bounds2','2024-P1-Q10','Choose input bounds in the directions needed for the extremal sum/difference; do not bound the rounded final difference.'),
 ('bounds3','2022-P2-Q4 2021-P2-Q3','Use the correct input bounds in triangle area, cuboid volume or extremal speed, as applicable.')])
levels('personal_finance_currency', [
 ('calculation2','2020-P1-Q3','Find total purchase cost before subtracting it from the amount paid.'),
 ('calculation2','2022-P1-Q16','Substitute principal, annual rate and time in years into simple interest.'),
 ('calculation2','2021-P1-Q13','Interpret which currency the quoted exchange rate buys and multiply/divide in the right direction.'),
 ('calculation3','2023-P1-Q12','Separate interest from final balance when needed, form the simple-interest equation and isolate the requested rate/principal/time.'),
 ('calculation2','2020-P1-Q29','Apply the compound multiplier for the number of periods and distinguish final balance from interest.')])
levels('metric_units_conversions', [
 ('answer1','2023-P2-Q3a','Use the correct metric length/mass/capacity conversion factor.'),
 ('answer1','2023-P2-Q3b 2023-P2-Q3d','Square or cube the linear conversion factor for area/volume rather than reusing it unchanged.'),
 ('calculation2','2024-P1-Q13 2024-P2-Q5','Convert both length and time dimensions before dividing or multiplying for speed.'),
 ('calculation2','2024-P2-Q5','Convert every numerator and denominator unit in a rate, or rearrange density=mass/volume correctly.')])
levels('time_clocks_timetables', [
 ('answer1','2021-P1-Q8','Correct elapsed minutes; distinguish a duration from a clock reading.'),
 ('two_values2','2022-P1-Q15','Correct hours and minutes of the duration, including borrowing across the hour/day boundary.'),
 ('answer1','2023-P2-Q12a 2023-P2-Q12b','Add/subtract the duration with correct carrying and 24-hour/12-hour notation.'),
 ('answer1','2024-P1-Q8b 2024-P1-Q8a','Convert fractional hours using 60 minutes per hour, or find the latest clock departure correctly.'),
 ('calculation2','2023-P2-Q12c','Combine journey and waiting times or derive arrival from the timetable without treating clock notation as decimal hours.')])
levels('defining_sets_notation', [
 ('answer1','2023-P2-Q6a.i','List all and only the requested elements, respecting the range and distinguishing elements from cardinality.'),
 ('answer1','2023-P2-Q6a.ii 2023-P2-Q6a.iv 2023-P2-Q6b','Apply the union/intersection/complement relative to the given universal set; output a set or count as asked.'),
 ('answer1','2024-P2-Q18b 2021-P2-Q4a','Use the correct element/subset/not-element relation, or the requested cardinality.')])
levels('venn_diagrams', [
 ('answer1','2023-P1-Q15b.i 2023-P1-Q15b.ii','Use disjoint regions and include/exclude the intersection correctly for the requested count.'),
 ('calculation2','2022-P2-Q6b','Subtract the neither group to obtain the union, then use n(A)+n(B)-n(A union B) for the intersection.'),
 ('answer1','2023-P2-Q6a.v','Apply the exact compound set expression; include every eligible element once.'),
 ('answer1','2023-P2-Q15a','Count favourable learners from the specified Venn region and divide by the entire eligible population.')])
levels('algebraic_manipulation_expansion', [
 ('calculation2','2020-P2-Q4a 2021-P1-Q19','Collect coefficients of like terms, or distribute a numeric bracket correctly before collecting.'),
 ('calculation2','2024-P2-Q9 2022-P2-Q7b.i','Apply the monomial to every bracket term, or divide by multiplying the reciprocal and cancelling valid factors.'),
 ('calculation2','2023-P1-Q24','Obtain the correct four products, then collect like terms and signs.'),
 ('calculation3','2022-P1-Q24 2020-P2-Q9','Expand the square including both cross terms, distribute outer signs and collect the expression.'),
 ('calculation3','2024-P1-Q24','Expand a pair of factors, distribute the remaining factor and collect the polynomial.')])
levels('expressions_formulae', [
 ('calculation2','2020-P2-Q4a 2021-P1-Q19','Combine only like terms or correctly expand a bracket before collecting.'),
 ('calculation2','2024-P2-Q6 2023-P2-Q4a','Substitute the assigned signed values, using brackets for negatives and evaluating powers before outer multiplication.'),
 ('calculation2','2021-P2-Q2b','Use equivalent inverse operations to isolate the requested letter while preserving equality.'),
 ('calculation3','2020-P2-Q6a 2021-P1-Q26','Express the stated direct/inverse relationship, use the data to find the constant, and supply the full equation or requested value.'),
 ('calculation3','2023-P1-Q25 2024-P2-Q10','Isolate and square the root relationship in a valid order, then isolate the requested subject.')])
profile('difference_squares2', [(1,'Correctly identifies both quantities whose squares give the two terms, or gives one correct linear factor.'),(1,'Complete correct product with one difference bracket and one sum bracket.')],
    'A complete correct final answer earns both marks without separate working. Recognising both squares alone earns the first mark. Do not require extraction of a common numerical factor when it is 1. Accept factor order and equivalent sign distribution.')
levels('factorisation_basics', [
 ('answer1','2021-P1-Q24a 2020-P2-Q5a','Extract the full common numerical factor and preserve the correct bracket.'),
 ('common_factor2','2024-P1-Q19','Extract the complete numerical and letter-power common factor; distinguish partial from complete factorisation.'),
 ('common_factor2','2023-P2-Q4b','Extract any required common factor, recognise a difference of squares, and write the complete product.'),
 ('grouping3','2020-P2-Q5b','Group terms so both groups share a binomial factor; extract that binomial with all signs correct.')])
profile('common_quadratic3', [(1,'The complete shared number factor is outside all brackets; the sign may be distributed among factors.'),
    (1,'Correct factorisation of the primitive inner quadratic.'),(1,'Complete correct product including the shared factor.')],
    'Accept any factor order and distribution of minus signs. All nonconstant integer brackets must be primitive: their coefficients share no integer factor greater than 1. Numerical factors may be split into separate factors outside brackets. Moving a numerical factor greater than 1 inside a bracket is incomplete, even when expansion is correct. Such an answer earns neither the first nor final achievement; award the middle achievement only when correct factorisation of the primitive inner quadratic is evidenced. For 10x²−25x−315, 5(x−7)(2x+9) is complete; (5x−35)(2x+9) is incomplete and can earn only the middle achievement. Missing the outside factor cannot earn full marks. These are achievements, not marks per displayed step.')
levels('factorisation_extension', [
 ('factors2','2021-P1-Q24b','Recognise a positive perfect-square trinomial and give its complete squared-binomial product.'),
 ('factors2','2021-P1-Q24b','Recognise a negative-middle-term perfect-square trinomial and preserve its sign.'),
 ('common_quadratic3','2024-P1-Q19 2022-P2-Q9a.i','Extract the complete common number factor and factorise the remaining quadratic completely.'),
 ('grouping3','2020-P2-Q5b','Factorise the four-variable syllabus form by grouping and extracting the common binomial.'),
 ('common_factor2','2024-P1-Q19','Extract the complete shared number/letter factor from terms with different remaining letters.'),
 ('common_quadratic3','2024-P1-Q19 2022-P2-Q9a.i','Preserve the negative leading coefficient while extracting a shared factor and completing the quadratic factorisation.')])
levels('factorising_quadratics', [
 ('factors2','2021-P1-Q24b','Identify the two correct linear factors of the monic trinomial.'),
 ('factors2','2021-P1-Q24b','Identify the two correct linear factors, including their signs.'),
 ('factors2','2022-P2-Q9a.i','Identify the two correct factors of the non-monic quadratic; exclude the source\'s unrelated SC1 line.'),
 ('square3','2020-P1-Q17 2024-P2-Q24a','Complete the square for a monic expression, including the compensation and final required form.'),
 ('square3','2020-P1-Q17 2024-P2-Q24a','Complete the square with the leading coefficient preserved; a compound turning-point task has a separate rule.')])
levels('polynomials_algebraic_fractions', [
 ('algebra_fraction3','2021-P2-Q5b 2023-P2-Q4c','Factor numerator and denominator correctly, cancel common factors, and give the simplified quotient.'),
 ('polynomial3','2022-P1-Q25 2020-P2-Q7c','Divide the polynomial by the linear factor and report both quotient and remainder.'),
 ('algebra_fraction3','2021-P2-Q5b','Extract/cancel only genuine factors in one- or two-variable algebraic fractions; do not cancel terms across a sum.'),
 ('algebra_fraction3','2024-P2-Q12 2023-P1-Q27','Find the common denominator, combine the adjusted numerators with the correct sign and simplify to one fraction.'),
 ('algebra_fraction3','2020-P2-Q11 2024-P2-Q12','Factor denominators as needed, form a common denominator, combine and simplify the single fraction.')])
levels('linear_simultaneous_equations', [
 ('calculation2','2024-P2-Q13a 2021-P2-Q8a','Use equivalent inverse operations and preserve the equality to isolate the unknown.'),
 ('calculation2','2024-P1-Q4 2021-P2-Q8a','Form/use the correct linear relationship, collect variable and constant terms and solve.'),
 ('calculation3','2024-P1-Q20 2021-P2-Q8b','Clear denominators without losing factors or signs, form the resulting linear equation and solve.'),
 ('simultaneous3','2023-P2-Q5c 2020-P2-Q4c','Use correct elimination/substitution and associate each solved value with its variable.'),
 ('nonlinear5','2021-P2-Q8c','Equate the supplied expressions for y, solve all roots and recover both associated coordinate/variable pairs; isolation is already supplied.')])
levels('solving_quadratic_equations', [
 ('roots2','2024-P2-Q13b 2023-P2-Q5b','Set each factor equal to zero and give both roots; do not require re-expansion.'),
 ('calculation2','2022-P1-Q26a','Isolate the square and give both real signed square roots, or the unique root when the square is zero.'),
 ('calculation3','2022-P2-Q9a.i 2022-P2-Q9a.ii','Rearrange/factorise the monic quadratic, then obtain both roots from zero factors.'),
 ('calculation3','2022-P2-Q9a.i 2022-P2-Q9a.ii','Factorise the non-monic quadratic correctly and give both roots with correct fractions/signs.'),
 ('quadratic4','2023-P2-Q5d 2021-P2-Q6b','Use a valid quadratic-solving method and the requested precision; a contextual length variant has its own admissible-root rule.')])
levels('inequalities_indices', [
 ('answer1','2020-P2-Q7b.i 2024-P2-Q7a','Apply the requested index multiplication, division or power law without changing the base incorrectly.'),
 ('calculation2','2021-P2-Q5a 2022-P2-Q7b.iii','Apply powers to each factor, or interpret negative/fractional indices as reciprocals/roots and evaluate.'),
 ('calculation2','2022-P1-Q21 2024-P2-Q8b','Form the stated inequality if needed and isolate the unknown with correct sign reversal.'),
 ('inequality3','2023-P1-Q8 2020-P2-Q12','Expand/rearrange both-sided or compound inequalities and give the complete solution with correct boundaries.'),
 ('indices4','2022-P1-Q27','Express quantities with a common base, combine exponents and obtain the requested single-power or equation solution.')])
levels('logarithms', [
 ('calculation3','2022-P2-Q10b','Interpret powers of ten and evaluate the requested logarithm, showing the demanded non-calculator working.'),
 ('calculation2','2023-P1-Q26 2024-P2-Q15a','Apply logarithm product/quotient/power laws; substitute the given logarithm symbol rather than taking a logarithm of that symbol.'),
 ('calculation3','2020-P1-Q19 2022-P2-Q10c','Convert constants/powers correctly, combine product and quotient logs and give the requested single logarithm.'),
 ('calculation3','2020-P2-Q7a 2023-P2-Q2b','Take logarithms on both sides and isolate the exponent without premature rounding.'),
 ('calculation3','2022-P1-Q26b 2024-P1-Q23','Rearrange the exponential equation, use logarithms to isolate the unknown and apply the requested precision.')])
levels('functions', [
 ('answer1','2023-P1-Q11a 2024-P2-Q25a.i','Evaluate the complete function at the given input, or solve the stated cube equation.'),
 ('calculation2','2022-P1-Q22a 2024-P2-Q25b','Reverse the linear function algebraically and give the inverse in the requested input notation.'),
 ('calculation2','2020-P1-Q25a 2020-P1-Q25b 2024-P2-Q25a.iii','Respect function order for a composite; otherwise substitute the requested expression or solve the stated function equation.'),
 ('calculation2','2022-P1-Q22b','Substitute the inner linear expression into the outer function and simplify.'),
 ('calculation3','2021-P1-Q23c 2022-P1-Q22b','Substitute the complete inner function, expand its square where present, and collect all terms.')])
levels('sequences', [
 ('answer1','2020-P1-Q23a','Apply the sequence rule to give the requested next term(s), not a formula when terms are requested.'),
 ('calculation2','2020-P1-Q23b 2021-P1-Q22','Find the common difference and construct the correct nth-term formula.'),
 ('calculation3','2023-P2-Q7a','Use the nth-term equation, solve for n and interpret it as the number/index of terms.'),
 ('calculation3','2024-P2-Q16 2023-P2-Q7b','For first-term/common-difference tasks solve the two term relationships; a sum-only task has a separate rule.'),
 ('indices4','2022-P2-Q16','Write the specified AP terms, impose the GP ratio condition, solve the resulting relationship and give the requested ratio.')])

profile('ap_gp4', [(1,'Correct expressions for the specified AP terms.'),
                  (1,'Correct equality of consecutive GP ratios.'),
                  (1,'Correct cross-multiplication/simplification and resulting parameter relationship.'),
                  (1,'Correct requested common ratio.')],
        'B1/B2/B3 in the source are cumulative stages, not six additive marks.')
profile('ratio_values3', [(1,'Correct relationship or equivalent preliminary equation.'),
                        (1,'Correct first requested parameter.'),(1,'Correct second requested parameter.')])

levels('straight_line_graphs_gradients', [
 ('answer1','2024-P1-Q15a','Identify the gradient or y-intercept from the given line equation.'),
 ('calculation2','2024-P2-Q26b','Use change in y divided by change in x with corresponding point order.'),
 ('calculation2','2024-P1-Q15a 2022-P1-Q23b','Rearrange a general line equation into gradient-intercept form and identify the requested coefficient.'),
 ('calculation2','2022-P1-Q23b','Substitute a known point into the line equation and isolate the missing value/intercept.'),
 ('two_values2','2023-P2-Q11a 2021-P2-Q13','Set y=0 for the x-intercept and x=0 for the y-intercept; give the two labelled intercepts.')])
levels('quadratic_graphs', [
 ('table_entries','2020-P2-Q15b','Evaluate each requested x-value in the full quadratic and retain value order.'),
 ('answer1','2023-P2-Q11a 2023-P2-Q11c','Use x=0 for the y-intercept, or root symmetry/sum to find the other root.'),
 ('two_values2','2024-P2-Q24b','Find the turning point by a valid method, or derive its axis/extreme value as requested.'),
 ('calculation3','2022-P2-Q10a 2020-P2-Q15e.ii','Equate the functions and solve all intersections; for a sign range, determine the correct inside/outside intervals.')])
levels('sketching_quadratics_gradients', [
 ('two_values2','2021-P2-Q13 2023-P2-Q11a','Calculate the requested intercept(s), retaining which axis each belongs to; this is not a sketching assessment.'),
 ('two_values2','2024-P2-Q24b','Read the turning point from the supplied completed-square form, reversing the inside sign for x.'),
 ('calculation3','2023-P2-Q11b','Complete the square or use another valid vertex method to obtain both turning-point coordinates.'),
 ('calculation2','2020-P2-Q15a 2022-P1-Q23c','Compute a secant/chord gradient, or identify the zero gradient at a quadratic turning point.')])
levels('advanced_graphs', [
 ('table_entries','2021-P2-Q12a 2024-P1-Q25a','Evaluate reciprocal/reciprocal-square values at each nonzero input, preserving signs and exact values.'),
 ('table_entries','2021-P2-Q12a','Evaluate the cubic at each input; use brackets when cubing negatives.'),
 ('table_entries','2021-P2-Q12a','Evaluate exponential values, including reciprocal powers for negative inputs; an intercept-only variant has a separate rule.'),
 ('answer1','2021-P2-Q12b','State the correct horizontal or vertical asymptote as an equation, respecting shifts.'),
 ('calculation2','2021-P2-Q12c.ii 2023-P1-Q11b','Solve the specific reciprocal, square-reciprocal, exponential or cubic equation and retain all valid real roots.')])
levels('linear_programming', [
 ('answer1','2020-P1-Q26b 2024-P2-Q8a','Translate the stated constraint into the correct inequality, including inclusive at-most/at-least limits.'),
 ('calculation2','2023-P1-Q28a','Test all given points against every constraint and count only those satisfying all conditions.'),
 ('three_conditions3','2020-P1-Q26b','Write each of the three stated constraints correctly; do not introduce extra constraints as requested answers.'),
 ('answer1','2023-P1-Q28b','Evaluate the objective at eligible vertices and select the requested greatest/least value.')])
levels('distance_midpoint_gradient', [
 ('two_values2','2024-P2-Q26c 2020-P2-Q17a','Average corresponding x- and y-coordinates to obtain the midpoint.'),
 ('calculation2','2024-P2-Q26a 2020-P2-Q17b','Use squared coordinate differences and the positive square root for distance.'),
 ('calculation2','2024-P2-Q26b','Use matching coordinate differences in the gradient quotient.'),
 ('calculation2','2020-P2-Q17b 2024-P2-Q26c','For a distance retain the required exact surd; for a midpoint average both coordinates exactly.'),
 ('calculation3','2024-P2-Q26a 2024-P2-Q26b 2024-P2-Q26c','Form the distance, gradient or midpoint equation for the missing coordinate and solve under any stated restrictions.')])
levels('equations_of_straight_lines', [
 ('calculation2','2020-P1-Q26a 2022-P1-Q23b','Use the given gradient/intercept or substitute the given point to find the intercept and write a full equation.'),
 ('line3','2020-P2-Q17c 2023-P2-Q11d','Find the gradient through the given two points, find the intercept and write the line equation.'),
 ('line3','2020-P2-Q17c 2024-P1-Q15b','Use the equal gradient of parallel lines and the given point to determine the full line.'),
 ('line3','2023-P1-Q7','Use the negative reciprocal gradient for a perpendicular line, then substitute the point.'),
 ('simultaneous3','2020-P2-Q17d','Equate/solve the line equations and give both coordinates of the intersection, not an unpaired list of values.')])
levels('parallel_perpendicular_quadrilaterals', [
 ('answer1','2024-P1-Q15a 2023-P1-Q7','Use equal gradients for parallel lines and product -1 for finite perpendicular gradients.'),
 ('calculation2','2023-P1-Q7 2020-P2-Q17c','Use the appropriate gradient relationship to form an equation in the parameter and solve it.'),
 ('two_values2','2024-P2-Q26c 2021-P2-Q11b','Use equal diagonal midpoints or equal opposite-side vectors to find the missing vertex coordinates.'),
 ('calculation3','2021-P2-Q11d','Find perpendicular rectangle dimensions or an equivalent correct coordinate-area method, then calculate the area.'),
 ('calculation3','2021-P2-Q11d','Use perpendicular height with base, or a valid determinant/shoelace method, to find parallelogram area.')])
levels('perimeters_areas_polygons', [
 ('calculation2','2021-P2-Q10a.ii 2024-P2-Q17','Select the correct area/perimeter formula and substitute the given dimensions.'),
 ('calculation2','2024-P2-Q17','Use one half of the sum of parallel sides times height, or rearrange that equation for height.'),
 ('calculation3','2022-P2-Q5b 2021-P2-Q10a.iii','Find a missing side with Pythagoras before perimeter, or add/subtract the correct component areas.'),
 ('calculation3','2023-P2-Q10a 2023-P2-Q10b','Relate circle radius/diameter and square diagonal/side correctly, then take the requested area difference.')])
levels('circles_arcs_sectors', [
 ('calculation2','2022-P1-Q33a 2021-P2-Q10a.i','Use the correct radius in circumference or circle area; do not confuse radius and diameter.'),
 ('calculation2','2022-P1-Q33b','Use angle/360 times full circumference or area for the requested sector quantity.'),
 ('calculation2','2022-P1-Q33a 2022-P1-Q33b','Rearrange the appropriate circumference/area/sector equation for the requested radius or angle.'),
 ('calculation3','2023-P2-Q10b 2022-P1-Q33b','Include both radii for sector perimeter, or subtract the appropriate triangle from the sector for segment area.'),
 ('calculation3','2023-P2-Q10b','For a segment subtract the triangle from the sector; for a ring subtract inner from outer circle area.')])
levels('surface_area_volume', [
 ('calculation2','2023-P1-Q18 2022-P2-Q12c','Choose cuboid/cylinder volume or full cuboid surface area correctly and substitute all dimensions.'),
 ('calculation2','2020-P1-Q24 2023-P2-Q13c','Use the supplied sphere/cone/pyramid formula as appropriate; halve the sphere only for a hemisphere.'),
 ('calculation2','2024-P1-Q30b 2022-P2-Q12b','Use curved rather than total surface area; derive cone slant height from vertical height when required.'),
 ('calculation3','2021-P1-Q30 2022-P2-Q12c','Find and combine the actual component volumes, including the hemisphere/half-cylinder factor.'),
 ('calculation3','2024-P1-Q30a 2023-P2-Q13c','Form the appropriate volume/curved-area equation and isolate the missing height/length; convert capacity units where asked.')])
levels('similarity_scale_factors', [
 ('calculation2','2022-P1-Q32','Use the ratio of corresponding lengths in the correct direction to find the missing length.'),
 ('calculation2','2022-P1-Q32','Square the linear ratio for areas, or square-root the area ratio for lengths.'),
 ('calculation3','2024-P2-Q20 2023-P1-Q31','Cube the linear ratio for volumes, or cube-root the volume ratio for lengths.'),
 ('calculation3','2023-P1-Q31 2024-P2-Q20','Convert an area/volume ratio to a linear ratio before converting to the other measure.')])
levels('angles_lines_polygons', [
 ('answer1','2023-P1-Q20a 2020-P2-Q14b.i','Use the stated straight-line, point, opposite-angle or adjacent-angle property.'),
 ('answer1','2023-P1-Q20b 2020-P2-Q14b.ii','Apply triangle sum, equal base angles or the exterior-angle relationship as appropriate.'),
 ('answer1','2023-P1-Q20a','Use the correct corresponding/alternate/co-interior angle relationship for the stated parallel lines.'),
 ('calculation2','2020-P2-Q14a 2024-P1-Q26','Use 360/n, (n-2)*180 or the appropriate regular-polygon relation and obtain the requested value.'),
 ('calculation3','2024-P1-Q26','Set up the polygon/angle-sum or ratio relationship, solve it and return the angle or count asked for.')])
levels('angles_circles', [
 ('calculation2','2024-P2-Q23x 2020-P1-Q21','Apply centre angle twice circumference angle, the semicircle theorem or the reflex-angle complement as applicable.'),
 ('answer1','2023-P1-Q32a 2024-P2-Q23z','Use equal same-segment angles or opposite angles of a cyclic quadrilateral summing to 180.'),
 ('calculation2','2022-P1-Q29b 2024-P2-Q23y','Use tangent-radius perpendicularity and any stated equal-radii triangle relation.'),
 ('calculation2','2023-P1-Q32b','Use the tangent-chord/alternate-segment theorem and the correct interior or centre-angle relationship.'),
 ('calculation3','2022-P2-Q8b 2022-P2-Q8c','Link the correct circle/triangle/tangent relationships to find the requested angle; do not require an unasked written reason.')])
levels('bisectors_numeric', [
 ('answer1','2023-P1-Q22b','Use the equal-angle property of the bisector to halve or double the given angle.'),
 ('calculation2','2020-P2-Q17a 2020-P2-Q17b','Use midpoint/equal-distance properties; if a right triangle is involved apply Pythagoras correctly.'),
 ('calculation2','2023-P1-Q20b 2023-P1-Q22b','Use equal halves of the bisected angle and triangle angle sum.')])
levels('bearings_right_angled_triangles', [
 ('calculation2','2020-P1-Q14a 2021-P2-Q9b','Choose the correct right-triangle ratio or Pythagorean relationship for the required side.'),
 ('calculation2','2020-P1-Q14b','Use a correct trigonometric ratio and inverse function for the requested angle.'),
 ('calculation2','2020-P1-Q14a','Distinguish hypotenuse from shorter side; add or subtract squared lengths correctly.'),
 ('calculation2','2024-P2-Q19b.i 2023-P1-Q22c','Use north-clockwise bearings, normalize through 360 and apply the correct turn/back-bearing relation.'),
 ('calculation3','2023-P2-Q13a 2023-P1-Q22c','Resolve the journey into perpendicular displacements, then use distance or the correct bearing quadrant.')])
levels('elevation_depression_extended_ratios', [
 ('calculation2','2020-P1-Q14b 2021-P2-Q9b','Choose the correct horizontal/vertical right-triangle relation for the elevation height or distance.'),
 ('calculation2','2020-P1-Q14b','Use the horizontal angle of depression/elevation relationship before solving the right triangle.'),
 ('calculation2','2023-P1-Q4 2020-P2-Q10a','Evaluate the full trigonometric calculator expression in degrees without intermediate rounding.'),
 ('trig_equation3','2020-P2-Q10b','Isolate the trigonometric ratio and find every solution in the specified interval.'),
 ('calculation3','2023-P2-Q17a 2023-P2-Q17b','Use the supplied exact ratio and quadrant signs to derive the other ratio and evaluate the expression exactly.')])
levels('sine_cosine_rules', [
 ('calculation2','2020-P2-Q10c 2023-P2-Q8a','Use half a*b*sin(included angle), preserving exact sine values when exact area is requested.'),
 ('calculation3','2023-P2-Q8b','Substitute the included-angle cosine rule, evaluate the squared side and take the positive square root.'),
 ('calculation2','2021-P2-Q9a 2021-P2-Q9b','Match each side with its opposite angle in the sine rule; use the stated acute/obtuse restriction.'),
 ('cosine_angle4','2022-P1-Q34a','Set up and rearrange the cosine rule for the angle, take inverse cosine and apply angle precision.'),
 ('calculation3','2024-P1-Q31 2023-P2-Q13a 2023-P2-Q13b','Rearrange triangle area for its angle, or use the appropriate base diagonal and half-diagonal right triangle in a pyramid.')])
levels('vector_operations_magnitude', [
 ('answer1','2024-P1-Q18a 2023-P1-Q19a','Apply scalar multiplication or add/subtract corresponding directed components.'),
 ('calculation2','2023-P1-Q19b 2020-P1-Q18b','Use the positive square root of the sum of squared components, retaining an exact surd when requested.'),
 ('calculation2','2024-P1-Q18a 2024-P1-Q18b','Form the correct vector combination; a subsequent magnitude is a separate extra achievement.'),
 ('calculation2','2024-P2-Q27b','Use directed side relationships of the parallelogram without reversing a vector or confusing position and displacement.')])
levels('position_vectors', [
 ('calculation2','2024-P2-Q27b','Use the correct fraction of the whole directed segment to locate the internal division point.'),
 ('two_values2','2024-P2-Q26c','Average the two position-vector components for the midpoint.'),
 ('calculation2','2024-P2-Q27a 2024-P2-Q27b','Form the directed path and scale the correct whole vector before collecting the coefficients of named vectors.'),
 ('calculation3','2024-P2-Q27b','Locate the ratio point and combine the correct directed paths to the requested triangle vector.')])
levels('transformations_coordinates', [
 ('image_coordinates3','2022-P2-Q15a.i','Apply the stated translation vector to each labelled vertex.'),
 ('image_coordinates3','2020-P2-Q8b 2023-P2-Q9c','Reflect each vertex across the stated line with correct invariant/doubled-distance behaviour.'),
 ('image_coordinates3','2022-P2-Q15a.ii','Rotate about the stated centre in the stated direction by the stated angle.'),
 ('image_coordinates3','2024-P2-Q28c 2021-P1-Q29b','Apply the signed scale factor to each displacement from the specified centre, then translate back.'),
 ('translation2','2024-P2-Q28a','Identify the actual transformation type and its required details; type-specific subrules select the right award.')])
levels('matrix_basics', [
 ('matrix_entries2','2024-P2-Q21c 2020-P1-Q20a','Add/subtract corresponding matrix entries without transposing their positions.'),
 ('matrix_entries2','2022-P2-Q13a.ii','Scale every entry and perform the stated matrix combination entrywise.'),
 ('two_values2','2022-P2-Q13b','Equate corresponding entries and solve the two requested unknowns.'),
 ('matrix_entries2','2024-P2-Q21a 2024-P2-Q21b','Read the stock matrix consistently; total-only and non-2-by-2 results require separate rules.')])
levels('matrix_multiplication', [
 ('two_values2','2023-P1-Q29c','Use each row dotted with the column to obtain the two resulting entries.'),
 ('matrix_entries2','2021-P2-Q7a 2022-P2-Q13a.i','Use row-by-column products in the stated multiplication order.'),
 ('matrix_entries2','2021-P2-Q7a','Multiply in the specified reverse order or square the matrix; do not assume matrix multiplication commutes.'),
 ('calculation2','2024-P1-Q29 2022-P2-Q13b','Form the relevant row-column entry equation and solve for the unknown.')])
levels('determinants_inverses', [
 ('answer1','2021-P2-Q7b','Evaluate the 2-by-2 determinant as ad-bc.'),
 ('inverse2','2021-P2-Q7b 2020-P1-Q20b','Find the determinant/adjugate and include the determinant divisor in the full inverse.'),
 ('calculation2','2024-P1-Q29','Write the determinant equation in the unknown entry and solve it with the correct signs.'),
 ('matrix_method5','2022-P2-Q13c','Represent and solve the system using matrices; keep matrix-method marks distinct from correct-value marks.'),
 ('calculation2','2024-P1-Q29','Set the determinant equal to zero for a singular matrix and solve for the unknown.')])
levels('mean_median_mode_range', [
 ('answer1','2020-P2-Q13a 2020-P2-Q13b 2020-P2-Q13c','Find the statistic actually requested; order the data for a median, and distinguish mode and range.'),
 ('calculation2','2024-P2-Q22c','Use sum divided by count for a mean; median/mode/range branches have their own one-mark rule.'),
 ('calculation2','2020-P1-Q27','Use mean times count for the required total and subtract all known values.'),
 ('mean_change3','2022-P1-Q30','Find old and new totals before taking their difference to identify the added observation.')])
levels('grouped_data_mean', [
 ('answer1','2022-P2-Q17b 2021-P2-Q15a','Identify the modal class using frequency for equal widths and frequency density for unequal widths.'),
 ('answer1','2023-P1-Q33','Locate the median observation in cumulative frequencies; percentage-at-least tasks have their own calculation rule.'),
 ('grouped_mean4','2022-P2-Q17c 2024-P1-Q34','Use midpoints, weighted total and total frequency to estimate the mean.'),
 ('grouped_mean4','2022-P2-Q17c','Use true midpoints of unequal-width classes, not endpoints or equal-width shortcuts.'),
 ('density_mean5','2023-P2-Q14a 2022-P2-Q17c','Recover each frequency from density times class width, then calculate the midpoint-weighted mean.')])
levels('cumulative_frequency_reading', [
 ('cf_table2','2020-P2-Q19a','Accumulate frequencies in increasing class order.'),
 ('table_entries','2024-P2-Q30a','Recover each ordinary class frequency by subtracting adjacent cumulative totals.'),
 ('answer1','2020-P2-Q19c.iv','Use the correct cumulative total or difference for less-than/between/at-least counts.'),
 ('answer1','2023-P1-Q33 2021-P1-Q33b','Find the median class; an interquartile-range calculation has its own two-mark rule.')])
levels('simple_probability', [
 ('answer1','2020-P2-Q18a 2020-P1-Q28b','Count favourable objects over the eligible total, including numeric zero for an impossible event.'),
 ('answer1','2022-P2-Q1a 2022-P2-Q3a.i','Count the requested number/letter outcomes and divide by the correct eligible total.'),
 ('answer1','2023-P2-Q15a','Use the correct row/column/whole-table denominator for the event as worded.'),
 ('answer1','2024-P2-Q29c 2021-P1-Q32b','Use the probability total/complement or multiply probability by number of trials for expected frequency.'),
 ('answer1','2021-P2-Q14a.ii','Count the equally likely ordered die outcomes satisfying the condition and divide by 36.')])
levels('tree_diagrams', [
 ('calculation2','2023-P1-Q34 2022-P1-Q28','Select pass/fail complements correctly and multiply the independent event probabilities.'),
 ('calculation2','2022-P2-Q3b','Without replacement, update both the favourable count and total for the next draw; conditional-one-draw tasks differ.'),
 ('probability_paths3','2020-P2-Q18c.ii 2023-P2-Q16b','For one-each use both orders; for at-least-one use the full event sum or a valid complement.'),
 ('calculation3','2023-P2-Q16c','Update without-replacement counts over three draws; at-least-one also requires complementing or summing all paths.'),
 ('probability_total3','2024-P2-Q29b.ii','Multiply along each relevant route and sum over the disjoint routes; a single joint route has a separate rule.')])

# Text-only completion families: where the corpus assesses drawings or recognition,
# the numeric adaptation is explicitly disclosed by the output's evidence relation.
levels('geometrical_terms', [
 ('answer1','2022-P2-Q5a 2023-P1-Q21a','Classify the angle using its stated magnitude; this transfers the one-item geometry-name demand.'),
 ('answer1','2024-P1-Q16b','Count lateral faces plus both polygonal bases; face-count transfer from solid-property recognition is explicit.'),
 ('answer1','2020-P2-Q14b.ii','Use two equal base angles and triangle sum to obtain the vertex angle.')])
levels('constructions_scale_drawings', [
 ('calculation2','2021-P1-Q15','Use the scale multiplier and centimetres-to-metres conversion for the actual length.'),
 ('answer1','2023-P1-Q22b','Apply the angle-bisector property numerically; this does not assess compass construction.'),
 ('answer1','2020-P2-Q16a.ii','Apply the midpoint property numerically; this does not assess construction arcs or drawing accuracy.')])
levels('symmetry_two_dimensions', [
 ('answer1','2023-P1-Q30 2024-P1-Q17','Give the number of symmetry axes of the regular polygon; line and rotational symmetry are distinct properties.'),
 ('answer1','2024-P1-Q17','Use 360 divided by rotational order for the smallest positive symmetry rotation.'),
 ('calculation2','2024-P1-Q17','Find the smallest symmetry rotation and multiply by the stated number of successive rotations.')])
levels('symmetry_circles', [
 ('calculation2','2024-P2-Q23y','Use equal tangent lengths to form and solve the equation; this is a circle-property analogy, not the same source task.'),
 ('answer1','2024-P2-Q26c','Use the fact that a perpendicular from the centre bisects the chord.'),
 ('answer1','2024-P2-Q23w','Use equal chords having equal perpendicular distances from the centre; source tests another circle property.')])
levels('locus_numeric', [
 ('answer1','2020-P2-Q16a.ii 2024-P2-Q26c','The equal-distance vertical locus passes through the segment midpoint.'),
 ('answer1','2020-P2-Q16a.i','The fixed-distance locus is a circle; the rightmost x-coordinate is centre x plus radius.'),
 ('answer1','2020-P2-Q16b','The point is on the specified side of a parallel fixed-distance locus, so use the correct signed offset.')])
levels('kinematics_rate_change', [
 ('calculation2','2023-P1-Q13b 2020-P2-Q15a','Use distance-time gradient as change in distance divided by change in time.'),
 ('calculation2','2020-P2-Q15a','Use acceleration as change in speed divided by elapsed time; gradient transfer is explicit.'),
 ('calculation2','2021-P1-Q25','Use trapezium area or mean speed times duration for uniform acceleration.'),
 ('calculation2','2021-P1-Q25','Use triangular area or half initial speed times braking duration for uniform deceleration to rest.')])
levels('introduction_functions', [
 ('answer1','2024-P2-Q25a.i','Evaluate the linear output at the specified input.'),
 ('calculation2','2024-P2-Q13a','Form the input-output equation and isolate the unknown input.'),
 ('answer1','2023-P1-Q11a','Evaluate the nonlinear function, squaring the signed input before multiplication.')])
levels('introduction_vectors', [
 ('answer1','2021-P1-Q31b.i','Subtract endpoint minus starting-point coordinates for the directed displacement.'),
 ('answer1','2024-P1-Q18a','Reverse the vector by negating both components.'),
 ('two_values2','2024-P2-Q26c 2021-P1-Q31b.i','Add the displacement to the starting point to obtain the two endpoint coordinates.')])
levels('income_taxes_bills', [
 ('calculation3','2020-P1-Q3 2023-P1-Q10','Calculate basic wages and commission on sales separately, then combine them.'),
 ('calculation2','2022-P1-Q8','Subtract the old meter reading from the new, then multiply usage by the stated unit price.'),
 ('calculation3','2020-P1-Q3','Apply the supplied fictional tax table to each applicable band, combine the tax and obtain the requested net amount.')])
levels('reading_charts_text', [
 ('calculation2','2022-P2-Q11c','Read the requested table frequencies and combine/subtract them for the asked total.'),
 ('calculation2','2023-P1-Q35','Convert the represented count using the pictogram key, accounting for any fractional symbol.'),
 ('calculation2','2023-P1-Q35','Use part/whole times 360 for the requested pie-sector angle.'),
 ('calculation2','2022-P2-Q11b','Read the initial/final values and calculate the stated change, using the right base if a percentage is requested.')])
levels('histograms_text', [
 ('answer1','2022-P2-Q17a','Subtract the class endpoints for class width; do not confuse width and frequency.'),
 ('calculation2','2022-P2-Q17a 2023-P2-Q14a','Use frequency divided by the true class width to find frequency density.'),
 ('calculation2','2024-P2-Q31','Use density times class width to recover the frequency represented by bar area.'),
 ('calculation3','2024-P2-Q31','Recover frequencies using each unequal class width, then add the recovered counts.')])

# Branch-specific allocations. These are review proposals, never official schemes
# for a generated instance. All uses retain their exact source records below.
profile('order2', [(1,'Correct comparison/conversion of at least two entries, or the source special-case reverse order.'),
                   (1,'The complete list in the requested order.')],
        'Reverse-order SC1 is an alternative partial route, not another mark. Preserve the original list elements.')
profile('successive4', [(1,'Correct fraction used at the first stage.'),
                       (1,'Correct remainder after that stage.'),
                       (1,'Correct application of the next fraction to the remainder.'),
                       (1,'Correct requested final quantity.')],
        'The subsequent fraction applies to the remainder, not the original whole. This is a changed-demand allocation requiring review.')
profile('estimate3', [(1,'First operand rounded as instructed.'),(1,'Second operand rounded as instructed.'),
                      (1,'Correct estimate using those rounded operands.')],
        'Combined source parts: rounded operands [2] and evaluation [1]. Exact calculation alone does not show the requested estimation.')
profile('indices_terms2', [(1,'At least two correct coefficient/exponent components, following the source partial rule.'),
                          (1,'The complete correct simplified term.')],
        'The source product has three assessable components. A two-component quotient is a changed-demand adaptation; no mark for merely copying an unchanged component.')
profile('form_solve4', [(1,'Correct mathematical relationship from the wording.'),
                        (1,'Correct complete inequality with the requested strict/non-strict boundary.'),
                        (1,'Valid solution method on that inequality.'),
                        (1,'Correct final solution set, allowing only source-supported follow-through.')],
        'Combines forming [2] and solving [2] from the source. The generated wording is a simpler adaptation; the four-mark tariff is provisional.')
profile('vector_magnitude3', [(1,'Correct directed vector combination.'),
                            (1,'Correct squared-component magnitude calculation.'),
                            (1,'Correct positive magnitude in the requested form.')],
        'Explicit combination of vector [1] and magnitude [2]; not a source-printed three-mark combined item.')
profile('iqr2', [(1,'Correct upper minus lower quartile setup.'),(1,'Correct interquartile range.')],
        'The source requires reading two quartiles for its partial award. Here they are provided: subtraction-method credit is a proposed adaptation, not graph-reading credit.')
profile('log_multiple2', [(1,'Correct logarithm as its exponent, showing the required working.'),
                         (1,'Correct multiplication by the coefficient and final result.')],
        'Reduced demand from the three-mark two-logarithm source. Proposed two-mark adaptation.')


# Concept descriptions are required by the syllabus; no matched exam definition
# tariff was established in the earlier paper analysis. Keep that provenance
# explicit rather than citing an unrelated calculation scheme as direct evidence.
for concept_level, demand in (
    (1,'Describe a function and use function/mapping notation.'),
    (2,'Describe one-one functions and inverse functions on the specified domain/range.'),
    (4,'Describe composite functions, form their linear rule and use the stipulated order and mapping notation.'),
):
    RULES[('nssco_functions_concepts',concept_level)] = {
        'profile':'answer1', 'sources':['NSSCO-6131-2018-7c-p21'], 'demand':demand}


# Authored static visual recipes share the frozen contract, not a second grader.
from ..math_generators import registered_generator_ids, get_generator
for visual_id in registered_generator_ids():
    if visual_id.startswith('nssco_visual_'):
        for visual_level in get_generator(visual_id).levels:
            RULES[(visual_id,visual_level)] = {'profile':'answer1',
                'sources':['NSSCO-6131-2018-visual-p13-26'],
                'demand':'Read, construct or plot the specified diagram using its actual instance data and the explicitly requested response mode.'}


RULES[('nssco_prepared_line_graphs',2)] = {
    'profile':'calculation2', 'sources':['2024-P2-Q26b'],
    'demand':'Read the two labelled points from the graph and calculate gradient using matching vertical and horizontal differences. Proposed two-mark adaptation to a visual question.'}


def signature(problem):
    """Finite structural signature; no random coefficient values or question text."""
    m = problem.machine
    result = {
        'skill':problem.skill, 'task':m.get('task',''),
        'transform_type':m.get('transform',{}).get('type',''),
        'compound_turning_point':bool(m.get('turning_point')),
        # A completed-square form is a numeric parameter dictionary, not a
        # structural branch. Counting its random coefficients inflated coverage.
        'form':m.get('form','') if isinstance(m.get('form',''),str) else 'completed_square_parameters',
        'shape':m.get('shape',''),
        'exam_marks':m.get('exam_marks'),
        'requested_x_count':len(m.get('x',[])) if isinstance(m.get('x'),(list,tuple)) else None,
        'class_count':len(m.get('classes',[])) if isinstance(m.get('classes'),(list,tuple)) else None,
    }

    if problem.generator_id == 'nssco_functions_concepts':
        result['concept_variant'] = '|'.join(str(m.get(k,'')) for k in ('shape','direction','domain','one_one','order'))
    return result


def resolve(problem):
    """Select an authored level rule, with explicit demand-specific overrides."""
    from copy import deepcopy
    gid, level, m = problem.generator_id[6:], problem.level, problem.machine
    task = m.get('task','')
    r = deepcopy(RULES[(problem.generator_id,level)])
    r['selection'] = 'authored_level_rule'
    # Conservative default: linking an analogous scheme never establishes an
    # official tariff for new wording or a different response mode.
    r['evidence_relation'] = 'adapted_exam_demand'
    r['review_reason'] = 'New generated question: compare its mathematical demand and response mode with the cited source before approving the proposed allocation.'
    def use(p, sources=None, demand=None, reason=None):
        r['profile'] = p
        r['selection'] = 'authored_branch_rule'
        if sources: r['sources'] = sources.split()
        if demand: r['demand'] = demand
        if reason: r['review_reason'] = reason

    if gid == 'factorisation_basics' and level == 3 and m['g']==1:
        use('difference_squares2',demand='Recognise the two squares and write their complete difference-of-squares product.')
    if gid == 'factorising_quadratics' and level == 5 and m.get('turning_point'):
        use('square_point5','2020-P1-Q17 2024-P2-Q24a 2024-P2-Q24b',
            'Complete the square [3], then use that form to state both turning-point coordinates [2].')
    if gid == 'fractions_decimals_percentages':
        if level == 2 and task == 'fraction_of_quantity':
            use('calculation2','2023-P2-Q1a.i','Multiply the whole quantity by the stated fraction; retain exact arithmetic.')
        if task == 'order_fractions': use('order2','2021-P1-Q5','Order the whole supplied list by actual fractional value.')
        if level == 4 and task != 'fraction_div':
            use('calculation2','2024-P2-Q3 2021-P1-Q9',
                'Use a correct common denominator for addition/subtraction, or multiply numerators and denominators for multiplication; simplify the final fraction.',
                'The division source has a different preparatory stage; multiplication is analogous to, not printed in, these cited addition/subtraction schemes.')
        if task == 'successive_fractions': use('successive4','2023-P2-Q1a.ii',
            'Apply each stated fraction to the correct remaining quantity in sequence, keeping track of what the question finally requests.')
    if gid == 'standard_form_estimates_approximations' and level == 3:
        use('estimate3','2020-P1-Q13a 2020-P1-Q13b')
    if gid == 'ratios_scales_rates':
        if task == 'simplify_ratio': use('answer1','2022-P1-Q6','Convert unlike units if needed, then give the complete simplest integer ratio.')
        if task == 'cost_per_100kg': use('answer1','2022-P1-Q11','Scale the cost to exactly 100 kg, rather than merely giving cost per kg.')
        if task == 'average_speed_two_legs': use('calculation3', demand='Find the distance of each leg, combine distances and times, then divide total distance by total time.', reason='Two-leg task adds a stage to the cited single-journey speed task; proposed three-mark combined allocation.')
    if gid == 'limits_of_accuracy':
        if level == 4: use('calculation2', demand='Choose upper/lower endpoints in the directions required for the extremal sum or difference, and calculate the requested limit. No inequality is requested.')
        if task == 'cuboid_min_volume': use('volume_bounds5','2021-P2-Q3')
        if task == 'speed_max':
            r['demand'] += ' This question explicitly requests 3 significant figures: retain exact inputs during calculation and round the final speed as instructed.'
    if gid == 'expressions_formulae' and level == 5 and m.get('exam_marks') == 2:
        use('calculation2','2022-P2-Q7a','Divide to isolate the square root, square both sides and express the requested subject correctly.')
    if gid == 'sequences':
        if level == 5: use('ap_gp4','2022-P2-Q16')
        if task == 'ap_a_and_d': use('ratio_values3','2024-P2-Q16','Form the two specified term relationships, solve them for the first term and common difference, and label both.')
        if task == 'ap_sum': use('calculation2','2023-P2-Q7b','Use the correct AP sum formula with first term, difference and number of terms; calculate the requested sum.')
    if gid == 'inequalities_indices':
        if level == 2:
            if task.startswith('evaluate_'): use('answer1','2024-P1-Q6','Interpret the fractional/negative exponent correctly and give the exact numeric value.')
            else: use('indices_terms2','2021-P2-Q5a 2024-P2-Q7a')
        if task == 'inequality_form_solve': use('form_solve4','2024-P2-Q8a 2024-P2-Q8b')
        if task == 'inequality_both_sides': use('calculation2','2024-P2-Q8b')
        if task in ('exponential_simple','exponential_linear'):
            use('calculation2','2023-P2-Q2a','Express both sides with the same base, equate exponents and solve the resulting linear equation.')
        if task == 'numeric_index': use('calculation3','2022-P1-Q27',
            'Combine numerator exponents, subtract the denominator exponent, then evaluate the constant power to give a number.',
            'Reduced and changed final demand from the four-mark single-power source; proposed three-mark adaptation.')
    if gid == 'logarithms':
        if level == 1 and m.get('shape') == 'multiple': use('log_multiple2','2022-P2-Q10b')
        if task == 'log_in_terms_of_m':
            use('calculation2','2023-P1-Q26',reason='Log-law analogy. The 2024 P2 Q15b report has no usable scheme row; do not claim an official tariff for it.')
    if gid == 'functions':
        if task == 'cube_equation': use('answer1','2023-P1-Q11b')
        if task == 'function_of_expression': use('answer1','2024-P2-Q25a.ii','Replace every occurrence of the function input by the specified expression and simplify if requested.')
    if gid == 'distance_midpoint_gradient':
        if task == 'midpoint_fraction': use('two_values2','2024-P2-Q26c')
        if task == 'find_other_end': use('two_values2','2024-P2-Q26c', 'Reverse the coordinate-wise midpoint relationships to recover both endpoint coordinates.')
        if task == 'find_missing_coordinate_gradient': use('calculation2','2024-P2-Q26b')
    if gid == 'equations_of_straight_lines' and task == 'line_from_gradient_intercept':
        use('answer1','2020-P1-Q26a','Insert the supplied gradient and y-intercept into a correct equation of the line.',
            'Source includes reading information not required here; reduced one-mark demand.')
    if gid == 'quadratic_graphs' and level == 3 and task != 'turning_point':
        use('answer1','2024-P2-Q24b','Give only the requested axis equation or extreme y-value, not both coordinates.',
            'Reduced single-component demand from a two-coordinate source.')
    if gid == 'sketching_quadratics_gradients':
        if task in ('y_intercept','turning_point_gradient'):
            use('answer1','2023-P2-Q11a' if task == 'y_intercept' else '2022-P1-Q23c')
    if gid == 'advanced_graphs':
        if task == 'exp_intercept': use('answer1','2023-P2-Q11a','Set x=0 and state the correct y-intercept.')
        if task == 'solve_cubic': use('answer1','2023-P1-Q11b','Isolate the cube if needed and give the unique real cube root.')
        if task == 'solve_recip_sq': use('roots2','2021-P2-Q12c.ii','Solve the reciprocal-square equation and retain both real roots.')
    if gid == 'angles_circles':
        if task == 'semicircle': use('answer1','2020-P1-Q21','The angle subtended by the diameter at the circumference is 90 degrees; no unasked written reason is required.')
        if task == 'radii_isosceles': use('answer1','2022-P1-Q29a')
    if gid == 'bisectors_numeric' and task in ('midpoint','equal_distance'):
        use('answer1','2024-P2-Q26c' if task == 'midpoint' else '2020-P2-Q16a.ii',
            'Use the stated midpoint/equidistance property directly; do not award an unperformed Pythagorean stage.')
    if gid == 'solving_quadratic_equations' and task == 'quadratic_context_length':
        use('quadratic_context3','2021-P2-Q6b')
    if gid == 'sine_cosine_rules' and task == 'pyramid_diagonal':
        use('calculation2','2024-P2-Q26a','Apply Pythagoras to the two rectangular-base lengths and calculate the positive diagonal.')
    if gid == 'surface_area_volume' and task == 'cone_height':
        use('calculation3','2022-P2-Q12b',
            'Use Pythagoras on radius and vertical height to obtain the slant height, then calculate curved surface area.',
            'An additional slant-height stage is needed; proposed three-mark allocation rather than two marks for directly supplied slant height.')
    if gid == 'vector_operations_magnitude' and level == 3:
        if task == 'combination': use('answer1','2024-P1-Q18a')
        else: use('vector_magnitude3','2024-P1-Q18a 2024-P1-Q18b')
    if gid == 'transformations_coordinates':
        if level < 5:
            r['evidence_relation'] = 'changed_response_mode_and_tariff'
            r['review_reason'] = 'Exam drawing/shape-and-position criteria do not directly transfer to typed coordinates. Three labelled-pair marks are a proposed adaptation.'
        else:
            kind = m['transform']['type']
            use({'translation':'translation2','rotation':'rotation3','enlargement':'enlargement3','reflection':'reflection2'}[kind],
                {'translation':'2024-P2-Q28a','rotation':'2023-P2-Q9a.i','enlargement':'2022-P2-Q15b','reflection':'2023-P2-Q9c'}[kind],
                'Describe the '+kind+' with the mathematically necessary type-specific details; equivalent descriptions are allowed.')
            if kind == 'reflection': r['evidence_relation'] = 'changed_response_mode_and_tariff'
    if gid == 'matrix_basics':
        if task == 'scalar': use('answer1','2023-P1-Q29a','Scale all four entries and preserve matrix shape and positions.')
        if task == 'stock_total': use('answer1','2024-P2-Q21a 2024-P2-Q21b','Sum exactly the stock entries requested by the question; distinguish original from remaining stock.')
    if gid == 'mean_median_mode_range' and level == 2 and task != 'mean':
        use('answer1','2020-P2-Q13a 2020-P2-Q13b 2020-P2-Q13c')
    if gid == 'grouped_data_mean' and task == 'percentage_at_least':
        use('calculation2','2021-P2-Q15b','Sum the frequencies in the requested classes and divide by the full frequency total, then multiply by 100.')
    if gid == 'cumulative_frequency_reading':
        if level == 2:
            n = len(m['classes'])
            # Keep the observed six-entry source rule explicit. Different column
            # lengths are proposed adaptations, never silently per-entry marks.
            r['profile'] = 'frequency_pairs'
            r['selection'] = 'authored_branch_rule'
            r['dynamic_awards'] = [{'marks':(n+1)//2,'achievement':
                f'For {n} requested frequencies: full {(n+1)//2} marks for all correct; otherwise floor(number of correct entries / 2), capped below full marks. Compare entries in their required positions.'}]
            r['review_reason'] = ('Six-entry source awards three marks, B1 per any two correct. Other entry counts use a proposed ceil(n/2) full-credit tariff; odd counts especially require teacher review.')
        if task in ('between','at_least'): use('calculation2','2020-P2-Q19c.iv','Subtract the appropriate two cumulative totals, or subtract the below-threshold total from the full count.')
        if task == 'iqr': use('iqr2','2024-P2-Q30c.ii')
    if gid == 'simple_probability' and level == 1 and task in ('not','two'):
        use('calculation2','2020-P1-Q28a','Find/combine the relevant counts or complement, then form the probability over the eligible total.',
            'The source event tariff is two marks; generated one-step versions are adaptations requiring review, not a universal two-mark rule for complements.')
    if gid == 'tree_diagrams':
        if task == 'second_given_first': use('answer1','2022-P2-Q3a.ii','Use the given first draw as a condition, update the remaining counts, and give the single requested conditional probability.')
        if level == 3 and task == 'at_least_one': use('calculation2','2020-P2-Q18c.iii','Calculate the complementary no-success probability over the two draws, then subtract from one; accept an equivalent complete path sum.',
            'This source gives two marks; another at-least-one task has four. The proposal follows this shorter two-draw complement demand, not one universal probability tariff.')
        if level == 4: use('calculation2','2021-P2-Q14b.iii' if task == 'at_least_one' else '2023-P2-Q16c',
            'Update counts over all three draws and form the correct product; complement it if at least one is requested. Accept an equivalent complete event sum.')
        if level == 5 and task == 'joint_late': use('calculation2','2024-P2-Q29b.i','Multiply the probability of the specified route by the lateness probability conditional on that route.')

    if gid == 'functions_concepts':
        from ..math_generators.functions_concepts_content import marking_achievements
        r['dynamic_awards'] = [{'marks':1,'achievement':a} for a in marking_achievements(problem)]
        r['selection'] = 'authored_concept_task_rule'
        r['evidence_relation'] = 'syllabus_objective_no_direct_exam_tariff'
        r['review_reason'] = ('NSSCO 6131 syllabus printed page 21, Topic 7(c), establishes scope. '
            'The new conceptual wording has no directly matched exam tariff in the reviewed paper set; '
            'these independent whole-mark achievements are proposed Recall allocations, not an official exam scheme.')

    if problem.generator_id.startswith('nssco_visual_'):
        from ..math_generators.visual_common import guidance as visual_guidance
        r['dynamic_awards'],r['sources'],visual_note=visual_guidance(problem)
        r['selection']='authored_visual_task_rule'
        r['evidence_relation']='adapted_visual_exam_demand' if all(s[:4].isdigit() for s in r['sources']) else 'syllabus_visual_objective_proposed_tariff'
        r['review_reason']=('Original generated visual question. Compare the exact diagram, requested drawing/reading, '
            'number of entries and supplied/reproduced axes with the cited source. The authored achievements are '
            'proposed adaptations, not official tariffs for this instance; scope-only syllabus citations supply no exam allocation.')

    awards = deepcopy(r.pop('dynamic_awards',None))
    if awards is None:
        if r['profile'] not in PROFILES: raise ValueError(f'Undefined profile {r}')
        awards = deepcopy(PROFILES[r['profile']]['awards'])
    if r['profile'] == 'table_entries':
        count = len(m.get('x',[]))
        if not count: raise ValueError(f'Unknown requested entry count: {problem.generator_id}/{level}')
        awards = [{'marks':1,'achievement':f'Correct table value at requested input {i+1} ({x}), in the required position.'} for i,x in enumerate(m['x'])]
    from .instance_awards import instantiate
    awards = instantiate(problem,r['profile'],awards,r['demand'])
    from ..math_generators.prose_formatting import normalise_notation
    for award in awards:award['achievement']=normalise_notation(award['achievement'])
    r['awards'] = awards
    r['proposed_total_marks'] = sum(a['marks'] for a in awards)
    r['profile_note'] = PROFILES.get(r['profile'],{}).get('note','')
    r['alternative_partial_credit'] = PROFILES.get(r['profile'],{}).get('alternative_partial_credit','')
    if gid == 'functions_concepts':
        r['profile_note'] = ('Judge mathematical meaning, accepting equivalent prose and notation. '
            'Do not require verbatim reference wording or match isolated keywords. '
            'Award only requested achievements; a correct classification alone cannot earn an explanation mark. '
            'These are independent conceptual/notation/value awards, not the two-mark method/result calculation profile.')
        r['alternative_partial_credit'] = ''
    if problem.generator_id.startswith('nssco_visual_'):
        r['profile_note']=visual_note
        r['alternative_partial_credit']='Only the explicitly stated partial routes apply; do not add duplicate drawing/shape/position awards.'
    if r['profile'] == 'bounds3' and task == 'speed_max':
        r['profile_note'] = 'Use exact extremal input bounds and retain intermediate precision; round only the final speed to the explicitly requested 3 significant figures.'
    r['status'] = 'draft_requires_maths_teacher_review'
    r['tariff_status'] = 'proposed_not_official_for_generated_question'
    r['follow_through'] = 'Use only the specific source-authorised FT route where applicable; do not invent a universal FT entitlement.'
    r['accuracy_and_form'] = {
        'question_instruction':'The generated question is authoritative about requested exactness, decimal places, significant figures, interval and answer form.',
        'generator_marking':deepcopy(problem.marking),
        'caution':'Generator metadata supplies an expected answer, not independent evidence of an exam tariff or a universal tolerance. Any conflict needs review.'}
    r['units'] = 'Use the quantity and units requested. If an answer field already supplies the unit, omission of a repeated unit is not an error. A unit mentioned in question prose is not proof of a preprinted answer-field unit. Do not invent an extra unit mark or blanket deduction; use the linked scheme where applicable.'
    if gid == 'bearings_right_angled_triangles' and level >= 4:
        r['sources'] = list(dict.fromkeys(r['sources']+['2024-P2-Q19b.ii']))
        r['accuracy_and_form']['bearing_format'] = 'A requested three-figure whole-degree bearing requires e.g. 095 degrees. The 2024 source retains M1 for 95 seen but withholds full marks for missing leading zero. Retain explicit decimal-place instructions where present; normalise bearings to [0,360). Numeric equivalence alone does not establish the required bearing format.'
    r['working'] = 'Assess mathematical achievements, not the number, order or wording of model steps. A valid alternative method is acceptable unless a method is explicitly required. Correct answers alone do not prove working on a show/prove/required-method task. Use only the working requirement explicitly stated in the question; do not invent an extra requirement.'
    if gid in ('factorisation_basics','factorising_quadratics','factorisation_extension') and task not in ('complete_square','complete_square_turning_point') and 'Factorise' in problem.question:
        r['working'] = ('For Factorise or Factorise completely without an explicitly required method, a correct complete final product earns every mathematical achievement it demonstrates, even without separate working. Do not flag or deduct merely for answer-only work or advise that unrequested working is compulsory. An equivalent unfinished factorisation receives only evidenced partial achievements. A sum of grouped products is partial, not a complete product. Missing working alone is not a reason for teacher review.')
    # Reuse the existing assessment-authoring content vocabulary. The richer
    # selector/source fields are research provenance, not a new runtime schema.
    r['marks'] = r['proposed_total_marks']
    r['creditworthy_points'] = [f"{a['marks']}: {a['achievement']}" for a in awards]
    from .solution_programs import program_for
    reference_program=program_for(problem,strict=False)
    if reference_program:
        reference_work=[f"{s['action']}. Reason: {s['reason']} Working: {s['result']}" for s in reference_program.steps]
    else:
        from ..math_generators.presentation import worked_example
        reference_work=[worked_example(problem)]
    r['grading_guide_answer'] = '\n'.join([
        f"DRAFT — teacher review required. Proposed total: {r['marks']}.",
        'Question: '+problem.question,
        'Reference final answer: '+problem.answer,
        'Creditworthy mathematical demand: '+r['demand'],
        *r['creditworthy_points'], r['profile_note'],r['alternative_partial_credit'],
        r['working'],r['units'],r['follow_through'],
        r['accuracy_and_form']['question_instruction'],
        r['accuracy_and_form'].get('bearing_format',''),
        'Evidence: '+', '.join(r['sources'])+'. '+r['review_reason'],
        'Worked reference (one valid route; these steps are not separate automatic marks):',
        *reference_work,
    ])
    r['grading_guide_answer']=normalise_notation(r['grading_guide_answer'])
    return r
