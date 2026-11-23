"""T5 standard elementary derivatives and rule-selection evidence (partial C4/C11)."""
import json
from pathlib import Path
W=Path(__file__).resolve().parents[2]
families=[];insights=[]
def D(s):return '8227:2020:'+s
def E(o,n):return D(f'M2:T4:O0{o}:D0{n}')
def M(b,k,ns,parts='*'):
 ch=4 if b=='Goldie' else 11
 return [dict(item_id=f'8227:TB:{b}:C{ch}:{k}:{n}',parts=parts,membership_reason='Named original response demonstrates this derivative decision. Other source responses,required methods,original real domains and defects remain attached to the complete source item.')for n in ns]
def G(k,ns,parts='*'):return M('Goldie',k,ns,parts)
def Y(k,ns,parts='*'):return M('YM',k,ns,parts)
def F(slug,title,decision,givens,constraints,rep,scaffold,methods,form,difficulty,distinction,ds,ms,pattern=None,exams=(),why=None):
 families.append(dict(family_id='8227:TEXTBOOK-FAMILY:'+slug,title=title,learner_decisions=decision,givens_and_unknowns=givens,
  constraints=constraints,representation_and_response=rep,scaffolding_and_connected_parts=scaffold,alternative_methods=methods,
  units_and_precision='Exact equivalent derivative expressions on the ORIGINAL real domain. Radian coordinate for standard trig derivatives;degree-coordinate factor is not silently omitted. Preserve requested variable and alloriginal poles/root/log restrictions even after cancellation.',
  answer_form=form,difficulty_progression=difficulty,distinction_basis=distinction,assessed_demand_ids=ds,member_specs=ms,
  examination_relation=dict(kind='structural branch'if pattern else'textbook-only',pattern_ids=['8227:FAMILY:'+pattern]if pattern else[],part_ids=list(exams),
   evidence_label='examination-observed (NSSCAS 8227), comparative link only'if pattern else'textbook-derived',
   reason=why or 'Textbook-derived/supporting evidence. No complete matching sampled examination structure or official marking award is claimed.')))

F('product-polynomial-radical-derivative','Differentiate a product of algebraic factors',
 'Identify both factors,retain BOTHproduct terms and apply inner derivatives without cancelling legitimate zero factors.',
 'Polynomial/radical product;unknown derivative in requested form.',
 'Original root domains and nondifferentiable endpoints remain;factoring must not lose repeated-factor roots if a later task asks zero gradient.',
 'Symbolic product to exact derivative.',
 'An explicit product-rule instruction requires demonstrated method;where none is prescribed,expansion or chain-square alternatives may be valid.',
 'Product rule plus chain rule;valid expansion where allowed;independent symbolic derivative checks equivalence.',
 'Equivalent derivative expression with required method evidence when source-enforced.',
 'Goldie1explicitlyprescribes product rule;YM1shows expansion as another route;YM3’sradical endpoint is outside the finite derivative formula.',
 'A required product-rule demonstration differs from a reducible product with no method instruction.',[E(2,1)],
 G('Example',[1,2])+G('Exercise-4A',[1],['i','ii','iii','vi','ix'])+Y('Example',[1,2,3])+Y('Try-Now',[1,2,3]),
 'product-quotient',['8227:EXAM:2021:P2:Q5:a'],
 'The observed product/quotient-rule calculus anchors comparison;textbook explicit method and expandable-polynomial alternatives remain source-specific branches.')
F('quotient-algebraic-derivative','Differentiate a quotient of algebraic factors',
 'Keep numerator/denominator order,subtract the second quotient term correctly and retain the squared denominator and original domain.',
 'Rational/radical quotient;unknown derivative with stated differentiation variable.',
 'Original denominator nonzero;whole-root versus split-root domain must be preserved. Simplified final formula doesnotreinstate holes.',
 'Symbolic quotient to derivative.',
 'Explicit quotient-rule sources require the method;where no method is prescribed,rewrite as powers/product when valid.',
 'Quotient rule,valid product/negative-power route or polynomial division/simplification as allowed.',
 'Equivalent exact derivative on the original domain.',
 'Goldie3/4prescribe quotient rule;YM7usesvariabletandleading cancellation;Try8(c)has a whole radical quotient whose split-key form loses a valid negative component.',
 'Quotient order/domain is substantive;not every printed fraction mandates a quotient method.',[E(2,2)],
 G('Example',[3,4])+G('Exercise-4A',[1],['iv','v','vii','viii'])+G('Exercise-4A',[2],['i'])+Y('Example',[6,7,8])+Y('Try-Now',[6,7,8]),
 'product-quotient',['8227:EXAM:2022:P2:Q5:a'],
 'The examination supplies a quotient-calculus comparison. Different original radicals and prescribed-method instructions preserve additional source constraints.')
F('elementary-standard-sum-derivative','Differentiate standard elementary functions and linear combinations',
 'Choose the correcte/ln/sin/cos/tan derivative,retain outside coefficients and signs and combine terms.',
 'Standard elementary functions or linear combinations;unknown derivative.',
 'Log arguments positive;trig inputs radians;tanpolesexcluded. A negativecos derivative sign is not optional.',
 'Function formula to exact derivative.',
 'No unasked tangent,stationary point or implicit/parametric demand is added.',
 'Prescribed standard derivatives and linearity;valid simple log-law simplification on the original domain.',
 'Equivalent derivative with correct signs and conditions.',
 'Goldie4C1contrasts tangent poles and sine/cosine signs;YM18Q1(a–c)contains constant offsets and mixed trig sums.',
 'Standard-rule application is smaller than a nested composite or product/quotient decision.',[E(1,1)],
 G('Example',[8],['i'])+G('Exercise-4B',[1],['i'])+G('Exercise-4B',[2],['i'])+G('Exercise-4C',[1])+Y('Try-Now',[10],['a'])+Y('Example',[12],['a'])+Y('Try-Now-12',[1],['a'])+Y('Example',[18],['a'])+Y('Try-Now-18',[1],['a','b','c']),
 'elementary-differentiation',['8227:EXAM:2024:P2:Q4:a'],
 'The observed standard-function derivative supports this core;not every textbook sum has the same form or further demand.')
F('elementary-composite-derivative','Differentiate nested elementary functions with original-domain control',
 'Identify each inner function and multiply every chain factor while distinguishing a power of a trig value from a multiplied argument.',
 'Composite exponential/log/trig/radical function;unknown derivative.',
 'ln(x²)has bothnonzero realbranches even if2lnxworking doesnot. ln(sinx)requiressinx>0;√cosxrequiresrealroot and finite derivative conditions.',
 'Nested function to exact derivative in an equivalent form.',
 'A source may request a particular simplified form;alloriginal exclusions remain after log/trig identities.',
 'Chain rule,valid same-domain log identities and algebraic/trig simplification.',
 'Complete derivative including every inner multiplier/sign.',
 'Goldie9usesln(x⁴)with a flawed positive-only working route;YM11contrasts√xwith√(e^x);YM20includes shiftedradianarguments and powers oftrigvalues.',
 'A changed inner range or nesting changes domain/chain decisions;numeric coefficient changes alone are ordinary variation.',[E(1,1),E(1,2)],
 G('Example',[5,6,7,9,11,13])+G('Example',[8],['ii'])+G('Exercise-4B',[1],['ii','iii','iv','v','viii','ix'])+G('Exercise-4B',[2],['ii','iii','iv','viii'])+G('Exercise-4C',[4])+G('Exercise-4C',[5],['i','iii','iv','vi'])+
 Y('Example',[10,11,14,15])+Y('Try-Now',[10],['b','c','d'])+Y('Try-Now',[11,14,15])+Y('Try-Now',[16],['d'])+Y('Example',[18],['d'])+Y('Try-Now-18',[1],['f'])+Y('Try-Now-18',[2])+Y('Example',[19],['a'])+Y('Try-Now',[19],['a'])+Y('Example',[20],['b','c'])+Y('Try-Now-20',[1],['a','b','c','d'])+Y('Try-Now-20',[2],['a','c']),
 'elementary-differentiation',['8227:EXAM:2025:P2:Q10:a'],
 'The observed elementary composite supplies a comparison. Particular nested-domain and source-form constraints remain explicit branches.')
F('elementary-product-derivative','Differentiate a product containing an elementary function',
 'Retain the derivative of EACHfactor and combine it with allnested chain factors;do not merely multiply individual derivatives.',
 'Algebraic×e/ln/trig or mixed elementary product;unknown derivative.',
 'Original log/root/trig domains remain;rewriting a denominator exponential changes its exponent sign consistently.',
 'Product formula to exact derivative.',
 'Method explicitly prescribed in some Goldiesources;other membersequivalentproduct/quotient routes remain valid.',
 'Product rule with standard/chain rules;valid equivalent rewrite where not method-restricted.',
 'Equivalent derivative with both required product contributions.',
 'Goldie12usesx²sinx;4C2requires product rule. YM19(b–f)mixes trigsimple/composite products,not just a standardtrigrecall exercise.',
 'Product terms are extra mathematical evidence beyond a chain multiplier.',[E(2,1)],
 G('Example',[12])+G('Exercise-4B',[1],['vi','vii'])+G('Exercise-4B',[2],['v','vi'])+G('Exercise-4C',[2])+G('Exercise-4C',[5],['ii'])+G('Exercise-4C',[6],['i'])+
 Y('Example',[12],['b'])+Y('Try-Now-12',[1],['b'])+Y('Try-Now-12',[2],['c'])+Y('Example',[16],['a'])+Y('Try-Now',[16],['a'])+Y('Example',[18],['b'])+Y('Try-Now-18',[1],['d'])+Y('Example',[19],['b'])+Y('Try-Now',[19],['b','c','d','e','f'])+Y('Try-Now-20',[1],['f'])+Y('Try-Now-20',[2],['b']),
 'product-quotient',['8227:EXAM:2023:P2:Q5:a'],
 'The observed product-rule chain is shared;functions/domains and explicitly required method evidence vary by source.')
F('elementary-quotient-derivative','Differentiate a quotient containing elementary functions',
 'Choose quotient/product rewrite as permitted,retain denominator-order subtraction and preserve ALLoriginal holes after simplification.',
 'Quotient containinge,lnortrig functions;unknown derivative.',
 'Positive log arguments and original denominators remain. Deriving a formula equivalent away from a hole doesnotdefine the original there.',
 'Quotient formula to exact derivative.',
 'A source-required quotient demonstration is distinct from a free-method derivative question.',
 'Quotient rule or valid inverse-power/product route if allowed;trig/log identities with domain retained.',
 'Equivalent derivative and method demonstration where asked.',
 'Goldie10notes the productlnx*x^-1alternative;4C3explicitlyprescribesquotient. YM12(c)has a negative exponent in the denominator;Try18Q3asks a cot/cosec targetform.',
 'Denominator restriction and quotient subtraction differ from a simple standard derivative.',[E(2,2)],
 G('Example',[10,14])+G('Exercise-4B',[1],['x'])+G('Exercise-4B',[2],['vii'])+G('Exercise-4C',[3])+G('Exercise-4C',[5],['v'])+
 Y('Example',[12],['c'])+Y('Try-Now-12',[1],['c'])+Y('Try-Now-12',[2],['a','b'])+Y('Example',[16],['b'])+Y('Try-Now',[16],['b'])+Y('Example',[18],['c'])+Y('Try-Now-18',[1],['e'])+Y('Try-Now-18',[3])+Y('Example',[20],['a'])+Y('Try-Now-20',[2],['d']),
 'product-quotient',['8227:EXAM:2024:P2:Q1:answer'],
 'Observed product/quotient elementary calculus anchors comparison. Source target forms and original-domain holes remain specific.')
F('reciprocal-trig-derivation','Derive a reciprocal-trigonometric derivative from prescribed sine/cosine quotients',
 'Rewrite the supplied function in prescribedsin/cosforms and demonstrate the required quotient/chain argument rather than claim an extra mandatoryrecallrule.',
 'tan/cot/sec/cosecexpression or a show-that derivative prompt;unknown established derivative.',
 'Radian input and original sin/cos poles;factor cancellations retain the original functiondomain.',
 'Specified function to proof/derivative with required working.',
 'GoldieActivity3uses sine/cosinederivatives as premises;YMsources explicitly requestdifferentiating the supplied quotient.',
 'Quotient or reciprocal-chain rule from prescribed standardfunctions;identitysimplification.',
 'Established derivative with original-domain qualification.',
 'YMTry19(g–i)uses scaledreciprocal functions;Exercise11Q1andRevision11Q1require the derivation route.',
 'A prescribed derivation requires method evidence absent from a recalled finalformula.',[E(1,1),E(2,2)],G('Activity',[3])+Y('Try-Now',[19],['g','h','i'])+Y('Try-Now-20',[1],['e'])+Y('Exercise-11',[1])+Y('Revision-Exercise-11',[1]))
F('graphical-derivative-inference','Infer a sine/cosine gradient graph from supplied graphical evidence',
 'Read tangent gradients/zeros/signs and construct the full requested derivativegraph,then distinguish visual resemblance from a formalproof.',
 'Givenradiansinegraph,localtangentandgradientframe;unknowngradientplots.',
 'Radian scale is essential;degreecoordinates change the derivativefactor. Source framedrawing must remain consistent with axis/period.',
 'Given graph/emptyframe to derivativegraph.',
 'Construct sinegradient,then cosine/itsgradient;allsourcegraphicalresponses retained.',
 'Tangent-gradient sampling and symmetry/period checks;standardderivatives independently validate features but do not erase the askeddrawing.',
 'Gradientcurves with requiredzeros,signs,period andamplitude.',
 'GoldieActivity2uses-2π..2πandemptyframe;its prompts later explain evidential limits.',
 'Drawing/inference is different evidence from a symbolic standard derivative.',[D('M1:T8:O01:D01')],G('Activity',[2]))
F('differentiation-conceptual-proof-support','Read derivative-rule proofs and explain their limits',
 'Identify required assumptions,distinguish a rule proof from a numericcheck,and explain angular-unit or polynomial-degree reasoning.',
 'Worked first-principles derivations or openconceptualprompts;unknown internal supportingreasoning.',
 'LIMIT03doesnotrequire first-principlesproof;degreecoordinate sine needs a unitfactor;nonzero polynomialdegreeargument includes constantcase.',
 'Workedformula/graph/explanation to proof audit or source-concept response.',
 'Optional teaching support and contextual brainstorm do not become directly assessedcalculusformula outputs.',
 'Valid limit/componentarguments,degreecomparison and unitconversion;source formula relationships checked independently.',
 'Requested conceptual explanation with sourceassumptions.',
 'GoldiePrompts1/5/6/7distinguish contexts,degreefactor,graphicalprooflimit andnonzeropolynomialdegree;YMWorkedderivation1explains e^xusing limits.',
 'Supporting proof/context is explicitly separated from direct derivative-demand coverage.',[],G('Prompt',[1,5,6,7])+G('Worked-derivation',[1,2,3])+G('Activity',[1])+Y('Worked-derivation',[1]))

def I(slug,title,ds,teaching,exam,difficulty,pitfalls,gaps,proposals,items,parts,grades):
 insights.append(dict(insight_id='8227:TEXTBOOK-INSIGHT:'+slug,title=title,demand_ids=ds,
  teaching_comparison=teaching,examination_comparison=exam,difficulty_and_grade_bounds=difficulty,pitfalls=pitfalls,
  gaps_and_representations=gaps,implications_for_step3=proposals,evidence_item_ids=items,examination_part_ids=parts,grade_descriptor_ids=grades,marking_rule_ids=[],examiner_error_ids=[]))
def S(b,k,n):return f'8227:TB:{b}:C{4 if b=="Goldie" else 11}:{k}:{n}'
I('elementary-calculus-standard-chain','Elementary standard derivatives,nesting and real domains',[E(1,1),E(1,2)],
 'Goldie motivates naturalderivatives throughln/expinverse relationships and trigderivatives throughgradientgraphs,then gives standard/composite drills. YM first introduces algebraic product/quotientrules,then e,lnandtrigfunctions,explicitly separating sums,products and quotients. Both show alternative loglaw routes,but a positive-only expansion cannotreplace a chain route on a larger originaldomain. Standard radiansine/cos/tan are prescribed;reciprocaltrig derivative proofs use those premises rather than invent mandatoryrecall.',
 'NSSCAS2024P2Q4(a)and2025P2Q10(a)anchor standard/composite elementarycalculus. A graphical gradient-investigation asks visualevidence beyond an algebraic derivative;an optionalfirst-principles derivation is teaching support rather than required examinationproof. A derivative formula request doesnotdirectlyassess a stationarypoint that an author could subsequently find.',
 'E13names elementary standard/composite derivatives;C13/A14retain them with product/quotient and implicit/parametric extensions. Harder nesting changes chain/domain reasoning:√xversus√(e^x),ln(x²)versus(lnx)²,and powers ofsinxversussin(kx). Numericalcoefficient size alone is not a levelboundary.',
 'Goldie9andYM14have a valid derivative but a loglawworking route losing negativex. YM16(d)prints a wrongnumerator coefficient. Degreecoordinates require theangularunitfactor. These are source/author cautions,not examiner-frequency evidence or justification to classify a standard derivative by the sophistication of its modelsolution.',
 'Both books provide rich symboliccalculus;Goldie’s derivativegraph frame adds a representation not equivalent to formula-only practice. Optionalproofs and reciprocal-function derivations remain labelledsupport. Originalholes and finite-derivative endpoints remain even when a simplifiedanswer looks defined elsewhere.',
 'Propose storing original expression/domain and requested derivativeform,testing equivalentanswers only on that domain,and retaining requiredvisual/proof evidence where asked. Keep nested-domain branches and explicitlyderived reciprocalfunctions separate from mandatoryrecall. Sourceproofexposition should not expand8227scope.',
 [S('Goldie','Activity',2),S('Goldie','Example',9),S('Goldie','Exercise-4C',4),S('YM','Example',11),S('YM','Example',14),S('YM','Try-Now',16),S('YM','Try-Now',19)],
 ['8227:EXAM:2024:P2:Q4:a','8227:EXAM:2025:P2:Q10:a'],['8227:GRADE:E:13','8227:GRADE:C:13','8227:GRADE:A:14'])
I('elementary-calculus-product-quotient','Product/quotient selection,prescribed methods and valid alternatives',[E(2,1),E(2,2)],
 'Goldie opens with product/quotient derivations and examples explicitly demanding those methods,then permits alternate productrewrite in laterexamples. YM shows expansion as a valid alternative for its opening polynomialproduct before adding affinepowers,radicals and elementaryfunctions. The same printed expression can have different assessed method evidence when one source enforces a rule and another permits any valid method.',
 'NSSCAS2021P2Q5(a),2022P2Q5(a),2023P2Q5(a)and2024P2Q1anchor product/quotientcalculus. Those examination awards must be read individually;a methodprescription in a textbook doesnotestablish an identical official awardtable. Explicitcurve product/quotient derivatives doNOTbecome implicit/parametricgeometric demandM2T4O03D03.',
 'C13/A14explicitly include products and quotients. Difficulty grows through innerchainfactors,radicaldomains,secondorder or geometrylater;presence of a fraction alone is insufficient. Rationalpowers/simplifiedsums inMaths1remain validlower scaffolds without requiringMaths2rules.',
 'YMTry8(c)’sWHOLEsqrtquotient has a validnegative-domaincomponent lost by splittingits key radicals. An equivalent quotient/productrewrite must retainoriginalpoles;correctincidence or one sampleinput doesnotcertify the derivative. Quotientorder and missingproductterm are mathematical feedback hypotheses here,not an asserted examinererrorrate.',
 'Both books offer direct drill breadth and applications. Goldie supplies explicitlyprescribed methodbranches;YM provides free-method expansion/rewrite contrasts. A derivative used to find a pointgradient or stationarycoordinate is a component unless the formula/method is independently asked. Sourcepartlinking must preserve that distinction.',
 'Propose per-partmethodrequirements,accepting equivalentvalid routes when unconstrained,and original-domain equivalence checks. Retain a required method comparison as extraevidence;do not count productrule versus expansion as separate recipes automatically. Guard explicit-versus-implicit/parametric classification independently of algebraform.',
 [S('Goldie','Example',1),S('Goldie','Example',3),S('Goldie','Example',10),S('Goldie','Exercise-4C',2),S('Goldie','Exercise-4C',3),S('YM','Example',1),S('YM','Try-Now',8),S('YM','Example',12)],
 ['8227:EXAM:2021:P2:Q5:a','8227:EXAM:2022:P2:Q5:a','8227:EXAM:2023:P2:Q5:a','8227:EXAM:2024:P2:Q1:answer'],['8227:GRADE:C:13','8227:GRADE:A:14'])

if __name__=='__main__':
 target=W/'tools/textbook-r5/synthesis-elementary-diff.json'
 target.write_text(json.dumps(dict(authorship='Codex author; independent review pending',scope='Partial GoldieC4/YMC11source families:standard/composite elementary derivatives and product/quotient rule decisions;twoinsightsectionscover4M2T4demands. Geometric,implicit and parametric source responses remain pending.',families=families,insights=insights),ensure_ascii=False,indent=2)+'\n')
 print(len(families),'authored families;',sum(len(f['member_specs'])for f in families),'explicit assignments')
