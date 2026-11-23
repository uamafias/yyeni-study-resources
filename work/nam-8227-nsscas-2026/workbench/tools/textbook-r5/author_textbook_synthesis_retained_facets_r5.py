"""Retained Goldie algebra, rate-model and real-number facets; no whole-chapter import."""
from synthesis_authoring_support_r5 import D,members,family,emit
def G(c,k,ns,parts='*'):return members('Goldie',c,k,ns,parts)
families=[];extensions=[]
def F(slug,title,decision,givens,rep,chain,methods,answer,bounds,distinction,ds,ms):
 families.append(family(slug,title,decision,givens,
  'Retain original nonzero denominators, nonzero divisor and real root/log domains. Source chapters outside scope do not make their retained facets wholly prescribed. No general partial-fraction, complex-number or differential-equation solving requirement is imported.',
  rep,chain,methods,answer,bounds,distinction,ds,ms))
F('rational-factor-cancel-support','Factor and cancel rational products/quotients with original restrictions',
 'Factor before cancelling, invert an actual divisor correctly and keep every original forbidden value.',
 'Numeric/algebraic fractions and products/quotients.', 'Expression to simplified equivalent on its original domain.',
 'The task requests simplification rather than a general decomposition method.',
 'Exact factorisation and rational arithmetic.', 'Simplified form plus original restrictions.',
 'Goldie7illustrations1..6model the rules;7B1..10include multivariable factors and a nonzero divisor.',
 'Supporting algebra is not relabelled as prescribed partial fractions.',[],
 G(7,'Worked-illustration',[1,2,3,4,5,6])+G(7,'Exercise-7B',[1,2,3,4,5,6,7,8,9,10]))
F('rational-common-denominator-support','Combine rational expressions using a common denominator',
 'Choose the factor/coefficient LCM, distribute any whole-numerator subtraction and combine exactly.',
 'Two/three rational terms or polynomial plus a fraction.',
 'Sum/difference to one simplified fraction.',
 'Original denominator holes survive cancellation; the source variable name is preserved even when the checker uses x.',
 'Factorised denominator LCM, exact expansion and cancellation.', 'Equivalent rational form with restrictions.',
 'Goldie7B18/20/22use repeated factors;24three linear denominators.7B22key changes a source plus to minus and is wrong.',
 'Common-denominator subtraction differs from a product cancellation.',[],
 G(7,'Worked-illustration',[7,8,9,10,11,12])+G(7,'Exercise-7B',[11,12,13,14,15,16,17,18,19,20,21,22,23,24]))
F('identity-equation-distinction','Explain identity versus equality at selected values',
 'Explain why a universal algebraic identity is specialised to equations for chosen values or coefficients.',
 '4+x identically A(2-x)+B(1+x) in surrounding excluded partial-fraction exposition.',
 'Boxed notation prompt to explanation.', 'Retain the prompt as a standalone in-scope notation decision without importing its surrounding decomposition algorithm.',
 'State universal equality versus an equation/condition on selected values.',
 'Correct distinction with the actual source expression.',
 'GoldiePDF190explicitly asks the distinction; equivalence-of-fractions counterexamples elsewhere do not automatically test it.',
 'This explicit requested explanation closes the old missing-textbook-support lead for identity/equation.',[D('M1:T1:O03:D01')],G(7,'Prompt',[1]))
F('indices-rewrite-prerequisite','Rewrite a root expression using rational indices',
 'Extract the constant square-root factor and preserve the original real domain.',
 '1/sqrt(4+x); unknown equivalent index form.', 'Expression to equivalent factorised power.',
 'Only7A6(i)is retained; its subsequent infinite series and approximation stay outside the positive-integer binomial scope.',
 'Exact index laws on x>-4.', 'One-half times(1+x/4)^(-1/2).',
 'The negative exponent is a rewriting prerequisite, not permission to expand a negative binomial series.',
 'Index rewriting and infinite-series expansion are different tasks.',[],G(7,'Exercise-7A',[6]))
F('rate-model-translation','Translate a proportional rate statement into a signed equation',
 'Identify the dependent variable, actual independent variable and proportional quantity; retain physical sign and domain.',
 'Rate proportional to a variable, inverse square/root or logarithmic expression.',
 'Verbal law to derivative equation/interpretation.',
 'A spatial or angular derivative is not automatically a time rate. A model does not require solving a general ODE.',
 'Direct proportionality and dimensions/sign checks.', 'The requested signed differential relation.',
 'Goldie9A2inverse-square speed,3real log domain,6angular rate and9acceleration use different stated quantities as explicit structural branches.',
 'Translating a model differs from solving it or merely differentiating a supplied function.',[D('M1:T8:O03:D03')],
 G(9,'Exercise-9A',[1,2,3,4,5,6]))
F('rate-model-calibration','Determine a proportional-rate constant from a stated observation',
 'Substitute the actual observation into the signed law and solve for its constant with the original units.',
 'Proportional law and measured rate/state pair.',
 'Context to calibrated rate equation.', 'The initial instant is a calibration condition, not an invented zero initial value.',
 'Exact proportional substitution and independent dimensional/sign check.', 'Calibrated coefficient and model.',
 'Goldie9examples1/2calibrate velocity/distance laws;9A7/8/9/11/12use cooling, growth, acceleration and volume states.',
 'Coefficient inference is additional to simply writing a proportional law.',[D('M1:T8:O03:D03')],
 G(9,'Example',[1,2])+G(9,'Exercise-9A',[7,8,9,11,12]))
F('rate-geometry-model','Use geometry or net flow to derive a rate model',
 'Write the actual area/volume relation, differentiate against the stated independent variable and combine inflow/outflow correctly.',
 'Square, circular slick, tank or cone and a loss/inflow law.',
 'Geometry/context to a requested rate relation.',
 'Positive dimensions/depth, consistent units and net signs; retained cone/tank facets stop before the excluded general ODE solution.',
 'Chain rule and geometry; independently compare dimensions.',
 'Requested side/radius/height rate and any calibrated coefficient.',
 'Goldie9example3square-side rate;9A10slick;9A13tank;9C13cone exponent-3/2. Geometry changes the model and is an explicit branch.',
 'Constructing the geometric rate relation is additional to a stated proportional equation.',[D('M1:T8:O03:D03')],
 G(9,'Example',[3])+G(9,'Exercise-9A',[10,13])+G(9,'Exercise-9C',[8],['i-height-rate-coefficient'])+G(9,'Exercise-9C',[13]))
F('rate-model-assumptions-support','Explain the limits of illustrative cooling or weather rate models',
 'State the missing measurement/assumption, distinguish a gradient from pressure and explain alternative model behaviour.',
 'Coffee, weather-map transect or milk/cooling investigation without a unique fully specified numerical model.',
 'Context/illustration to graphs, assumptions and qualified explanations.',
 'No invented unique drinkable/cold time, weather estimate or exact mixing law. General ODE solving remains extra scope.',
 'Qualitative monotonicity, model assumptions and explicitly conditional comparisons.',
 'All requested investigation/profile responses with nonuniqueness stated.',
 'Goldie9investigations require every subtask, including suitability/mixture comparisons; source context is not measured data.',
 'Model critique/support is not a numeric rate-calibration problem.',[],
 G(9,'Prompt',[1,2])+G(9,'Investigation',[1,2]))
F('number-system-classification-support','Classify real numbers and roots with explicit conventions',
 'Distinguish natural/integer/rational/irrational/real sets, give examples and classify the actual finite/recurring numbers or equation roots.',
 'Set definitions, nine printed numbers or five elementary equations.',
 'Number/equation to classification and requested examples.',
 'Retain the stated natural-number convention. Finite3.1415is rational whilepi is irrational. Complex extensions are not imported.',
 'Exact fraction/root analysis and explicit set inclusions.',
 'All definitions, examples, roots and classifications.',
 'Goldie11activities compare finite decimal versus recurring third and irrational radical; this supports later algebra without creating a new assessed8227demand.',
 'Supporting set classification differs from an identity/equation explanation.',[],G(11,'Prompt',[1,2])+G(11,'Activity',[1,2]))
F('equivalent-fraction-counterexample-support','Test a proposed fraction-equivalence claim',
 'Use a valid counterexample and explain the failure of the claimed operation.',
 'Source fraction-equivalence prompt.', 'Claim to counterexample/explanation.',
 'This does not expressly ask identity-versus-equation notation and must not inherit that direct objective.',
 'Exact counterexample and original denominator check.', 'A valid counterexample and explanation.',
 'Goldie11Prompt3is a single supporting claim-test.',
 'A counterexample tests a universal claim but is not automatically the syllabus identity-notation demand.',[],G(11,'Prompt',[3]))
F('vector-analogy-retained-support','Explain vector subtraction in an Argand teaching analogy',
 'Read the two supplied vector diagrams and reverse the appropriate arrow/addition to represent a difference.',
 'Two Argand-context teaching diagrams.', 'Diagram to vector-difference explanation.',
 'Keep it as supporting analogy; do not claim prescribed complex-number arithmetic or a fully assessed vector problem.',
 'Vector subtraction as addition of the opposite vector.', 'Both requested retained real/vector explanations.',
 'Goldie11Activity7uses complex context whose further operations remain excluded.',
 'A retained analogy does not import all the surrounding chapter demands.',[],G(11,'Activity',[7]))

def E(fid,reason,ms):extensions.append(dict(family_id='8227:TEXTBOOK-FAMILY:'+fid,reason=reason,member_specs=ms))
E('binomial-direct-expansion','Only positive-integer exponent3is retained; later negative-series parts remain excluded.',G(7,'Exercise-7A',[5]))
E('polynomial-root-discovery','The retained facet expressly asks a real integer cubic root, not its later complex roots.',G(11,'Exercise-11H',[8]))
E('polynomial-inverse-remainder-constraints','A given real root4fixes the coefficient; later complex-key defects do not affect this retained coefficient equation.',G(11,'Exercise-11H',[9]))
E('polynomial-factor-solve','Expand the real root factorisation and state the quadratic root equation; complex later facets are excluded.',G(11,'Exercise-11B',[9]))
E('power-antiderivative-family','The retained ordinary primitive is direct reverse differentiation, not a general differential equation method.',G(9,'Example',[4])+G(9,'Exercise-9B',[1],['i','iv']))
E('curve-first-derivative-point','The actual supplied point determines the integration constant on the retained ordinary derivative branch.',G(9,'Worked-illustration',[2])+G(9,'Exercise-9C',[1]))
E('implicit-curve-derivative','Differentiate the fully supplied implicit relation and verify its condition/positive-root branch; do not infer a general ODE-solving requirement.',G(9,'Example',[9]))
E('rational-specified-identity','The rational identity template is explicitly supplied after the tank part; a general unsupplied decomposition method is not asked.',G(9,'Exercise-9C',[8],['ii-given-rational-identity']))

if __name__=='__main__':
 emit('retained-facets','Complete retained GoldieC7algebra,C9rate-model facets and remainingC11real facets; supporting tasks remain explicit and do not import excluded parent chapters.',families,[],extensions)
