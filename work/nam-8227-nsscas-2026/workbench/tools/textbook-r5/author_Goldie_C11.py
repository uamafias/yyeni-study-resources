"""C11 source census: retain prescribed facets; complex-number methods stay additional.

Fixed-source answer checks and author evidence only, not learner generators.
"""
import hashlib,json
import author_Goldie_C8_opening as base
from author_Goldie_C8_opening import W,SRC,SHA,value,reasoning,fig,figures,compute,expression,equivalent

ROOT=W.parents[2]
PRINCIPAL='8227:2020:M1:T6:O04:D01';EXACT='8227:2020:M1:T6:O03:D01'
DOUBLE='8227:2020:M2:T3:O02:D03';COMPOUND='8227:2020:M2:T3:O02:D02'
APPLY='8227:2020:M2:T3:O02:D05';RANGE='8227:2020:M1:T3:O02:D02'
RECONSTRUCT='8227:2020:M1:T1:O05:D01';FACTOR='8227:2020:M2:T1:O04:D02'
COEFFICIENT='8227:2020:M2:T1:O04:D03';POLYROOT='8227:2020:M2:T1:O04:D04'
ADD='8227:2020:M1:T7:O02:D01';DISP='8227:2020:M1:T7:O03:D02';MAG='8227:2020:M1:T7:O04:D01'

def ev(page):
    if page in[294,295]:name='Goldie-C10-end-C11-start-source'
    elif 296<=page<=331:name=f'Goldie-C11-{296+4*((page-296)//4)}-source'
    elif page in[332,333]:name='Goldie-C11-end-332-source'
    elif page in[359,360]:name='Goldie-C10-keys-357-source'
    elif 361<=page<=364:name='Goldie-C11-keys-361-source'
    elif 365<=page<=368:name='Goldie-C11-keys-365-source'
    else:raise ValueError(page)
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

base.ev=ev;base.answers.clear();base.new.clear();figures.clear()
answers=base.answers;new=base.new

def add(kind,n,page,note,parts,direct=None,components=None,teaches=None,rep='text',excluded=None,attribution=None):
    row=base.add(kind,n,page,note,parts,direct or[],components or[],teaches=teaches or[],rep=rep,exam_attribution=attribution)
    row['item_id']=row['item_id'].replace(':C8:',':C11:');new[-1]['item_id']=row['item_id']
    row['value_level_scope_decisions']=[]
    row['scope_check']={'status':'in-scope-parts-only'if excluded else'in-scope','basis':note,'excluded_or_qualified_parts':excluded or[],
      'limits_considered':[],'qualifier_applicability_note':'The actual retained output decides scope;complex-number representations and enforced complex methods do not become8227requirements. Item-specific value restrictions are recorded where relevant.'}
    row['mapping_rationale']='Map explicitly requested prescribed outputs only. Real-number prerequisites and complex/vector analogies are supporting evidence. Pure trig and separately requested real-polynomial results remain available even inside a complex-number chapter. Do not infer complex-number scope or full original-item coverage.'
    row['precision_angle_check']={'source':'Goldie answer prefacePDF333printed319:non-exact values3significant figures;degree angles1decimal place,unless otherwise specified;avoid intermediate rounding. Activity11.11explicitly requires exact surds.',
      'comparison':'This is a book-wide convention,not an explicit instruction in each stem. Principal arctangents have open endpoint bounds. Exact values and mathematical domains remain available alongside display rounding.',
      'source_evidence':ev(333)}
    for p in row['subparts']:
        p['review_date']='2026-11-19'
        if p.get('author_comparison_status')=='no key':
            p.update(answer_pdf_page=None,answer_printed_page=None,
              key_presence='no separate key',
              key_absence_note='No separate fixed answer:the response uses explicitly author-chosen valid examples.',
              inspected_key_pdf_pages=list(range(359,369)))
    key_pages=sorted({p['answer_pdf_page']for p in row['subparts']if p['answer_pdf_page']is not None})
    new[-1]['answer_key'].update(available=bool(key_pages),pdf_pages=key_pages,printed_pages=[p-14 for p in key_pages])
    new[-1].update(scope_check=row['scope_check'],value_level_scope_decisions=[],mapping_rationale=row['mapping_rationale'])
    return row

definitions=[('natural','Nonnegative whole numbers under this book’s stated convention;some conventions start at1.',
 'The source key explicitly notes the0convention differs between mathematicians. Positive examples1and2avoid that ambiguity.'),
 ('integer','Whole numbers,including negative values,0andpositive values.',
 'The integer set includes the natural numbers and also their additive negatives. Examples outside the natural region are−1and−2.'),
 ('rational','Real numbers expressible as p/q with integersp,qandq≠0.',
 'Fractions1/2and−2/3are rational but not integers. Reduced denominator1characterises integers;finite and repeating decimal expansions are rational.'),
 ('real','The real numbers comprise both rational and irrational numbers.',
 'The key’s phrase not complex must be understood as not non-real:every real number also embeds as a complex number with imaginary part0. The real-line classification is valid;do not copy that unqualified wording as a formal definition.')]
parts=[]
for label,conclusion,why in definitions:parts.append(reasoning('definition-'+label,conclusion,why,359,'key incomplete'if label=='real'else'matches'))
for label,conclusion,why in [('natural','1and2.','Both are natural under either convention about0.'),('integer-only','−1and−2.','Both are integers outside the natural-number region.'),('rational-only','1/2and−2/3.','Both are rational and nonintegral.'),('real-only','√2andπ.','Both are irrational,so lie in the real set outside the rational set.')]:
    parts.append(reasoning('examples-'+label,conclusion,why,294,'no key'))
add('Prompt',1,294,'Explain the four nested real-number sets inFigure11.1andgive two examples for each displayed region. This is prerequisite classification support,not an invented AS-objective coverage claim.',parts,rep='diagram')
p=reasoning('irrational-complement','The irrational numbers occupy the part of the real set outside the rational set;no extra nested set is needed.',
 'Within the real numbers,being rational and being irrational are complementary,mutually exclusive properties. The source key explains precisely this real-set complement. Numbers outside the real line are outside this prerequisite diagram.',359,'matches')
add('Prompt',2,295,'Explain whyFigure11.1has no separately nested irrational-number set. Keep its universe as the real numbers.',[p],rep='diagram')

parts=[]
for label,text,classification,why in [
 ('7','7','natural','Positive whole number;it also belongs to each enclosing set.'),
 ('sqrt5','√5','irrational real','5is not a square integer,so√5cannot be a rational number.'),
 ('minus13','−13','integer outside the natural set','Negative whole number.'),
 ('227over109','227/109','rational noninteger','Integer fraction withnonzero denominator;227is not a multiple of109.'),
 ('minus-sqrt5','−√5','irrational real','Negating a nonzero irrational preserves irrationality.'),
 ('finite-decimal','3.1415','rational noninteger','Finite decimal equals6283/2000;it is notπ.'),
 ('pi','π','irrational real','Use the known irrationality ofπ;no proof is demanded by this classification activity.'),
 ('point33','0.33','rational noninteger','Finite decimal equals33/100.'),
 ('recurring-third','0.3 recurring','rational noninteger','The dot above3on the source means recurring;it equals1/3,not3/10.')]:
    p=reasoning(label,f'{text}:place in the {classification} region.',why,359,'matches');parts.append(p)
add('Activity',1,295,'Place nine specific numbers into the smallest appropriate regions of the nested real-number diagram,distinguishing finite3.1415fromπandrecurring0.3from a terminating decimal.',parts,rep='diagram')

parts=[]
for label,equation,key,classification in [('i','x+7-9','FiniteSet(2)','Natural(andinteger,rational,real).'),('ii','7*x-9','FiniteSet(Rational(9,7))','Rational noninteger(andreal).'),('iii','x**2-9','FiniteSet(-3,3)','Both integer(andreal);only the positive root is natural.'),('iv','x+10-9','FiniteSet(-1)','Integer outside the natural set(andreal).'),('v','x**2+7*x','FiniteSet(-7,0)','Both integer;0is natural under the book’s convention,−7is not.')]:
    p=value(label+'-roots','solveset('+equation+',x,domain=S.Reals)',key,359,
      'Solve the original real equation independently. For a squared/product equation retain both real roots,including0where present;classification is a separate requested output.');parts.append(p)
    parts.append(reasoning(label+'-classification',classification,'Use the exact derived roots and the source’s real-number nesting. Do not lose the negative root or the zero root merely because a positive example appears first.',359,'matches'))
add('Activity',2,295,'Solve five basic real equations andclassify every root by number set. Preserve both roots ofx²=9andx²+7x=0. These are prerequisite algebra support,not full AS-objective coverage.',parts)
add('Prompt',3,299,'Give a counterexample showing two equal rational fractions can have different numerators anddifferent denominators. This is fraction-equivalence support,not evidence for identity-versus-equation coverage.',[
 reasoning('counterexample','2/3=4/6,although2≠4and3≠6.','Multiplying numerator anddenominator by the same nonzero integer preserves a fraction’s value. Denominators are nonzero. A single counterexample disproves the proposed necessity of separately equal numerators/denominators.',360,'matches')])

p=value('i-factor-expansion','expand((x-a)*(x-b))','x**2-(a+b)*x+a*b',361,
 'Distribute the two factors independently andcollect powers ofx. For the prescribed real-root facet,the resulting monic quadratic has sum of rootsa+bandproductab. The identity itself is valid over the complex field too,but no complex arithmetic is needed here.');p['check_mode']='show/prove'
p2=reasoning('i-root-equation','The monic quadratic with rootsαandβis z²−(α+β)z+αβ=0.',
 'The expanded product equals(z−α)(z−β),so its zeros are exactlyαandβ,counting a repeated root whenα=β. Retain this general construction for the real-root8227facet;the following source complex-root numerical cases are additional.',361,'show/prove')
add('Exercise-11B',9,304,'Retain(i):expand the factor pair anddeduce the monic quadratic from its roots. The prescribed facet uses real roots;the subsequent complex-root cases(ii)remainadditional.',[p,p2],[RECONSTRUCT],excluded=['Part(ii)uses complex roots andis outside prescribed8227scope;no complex-number recipe coverage is claimed.'])

parts=[]
for label,conclusion,why in [('i-difference','Draw the arrow fromz₁toz₂to representz₂−z₁.',
 'The source Argand axes carry a vector analogy. As an ordinary displacement,head minus tail equals the destination position minus the starting position. The requested arrow must start atz₁andendatz₂;the negative difference reverses it.'),
 ('ii-reversed-addition','Reverse thez₂arrow,thenjoinz₁and−z₂head to tail. The resultant equalsz₁−z₂andcan be translated without changing its components.',
 'Subtraction is addition of the opposite vector. A displacement arrow fromz₂toz₁andthe translated head-to-tail resultant agree even when drawn at different places. This supports vector meaning;formal complex subtraction stays additional.')]:
    parts.append(reasoning(label,conclusion,why,361,'sketch'))
row=add('Activity',7,307,'Draw the two source subtraction diagrams,retained as supporting free-vector/displacement analogies in their original Argand context. Do not label complex arithmetic as prescribed8227practice.',parts,teaches=[ADD,DISP],rep='diagram',excluded=['Original complex-number notation/Argand interpretation remains additional;only the vector analogy is retained as supporting evidence.']);row['sketch_response_required']=True;new[-1]['sketch_response_required']=True

parts=[]
for label,given,key in [('a','1','45'),('b','2','63.4'),('c','100','89.4'),('d','-2','-63.4'),('e','-50','-88.9'),('f','-200','-89.7')]:
    p=value('i-'+label,'180*atan('+given+')/pi',key,364,
      'Apply the principal inverse tangent to the original real input andconvert radians to degrees. Compare only the final degree display at the book’s1decimal-place convention;the exact45°value stays exact.')
    p['operation']={'kind':'rounded','operands':['180*atan('+given+')/pi'],'decimal_places':1};parts.append(p)
p=reasoning('i-degree-range','−90°<arctan x<90°for every finite realx. No largest orsmallest value is attained;the endpoint limits are−90°and90°.',
 'Tangent restricted to(−π/2,π/2)is continuous,strictly increasing andonto the real line,so its inverse has that open range. The source key correctly prints strict inequalities. Interpret the informal question about largest/smallest values as asking for bounds;never make±90°attained answers.',364,'matches')
p['additional_operations']={'degree_endpoint_limits':{'kind':'identity','operands':['Tuple(180*limit(atan(x),x,-oo)/pi,180*limit(atan(x),x,oo)/pi)']}}
p['additional_operation_expected']={'degree_endpoint_limits':'Tuple(-90,90)'};parts.append(p)
p=reasoning('ii-chosen-radian-examples','One valid chosen set:x=−√3,0,√3gives arctan x=−π/3,0,π/3radians.',
 'Part(ii)allows the learner to choose different inputs;these are author-selected examples,not extra fixed values printed in the question or key. Every output lies strictly inside the principal radian interval andits tangent returns the original input.',313,'no key')
p['additional_operations']={'chosen_principal_values':{'kind':'identity','operands':['Tuple(atan(-sqrt(3)),atan(0),atan(sqrt(3)))']},'original_tangent_checks':{'kind':'identity','operands':['Tuple(tan(-pi/3),tan(0),tan(pi/3))']}}
p['additional_operation_expected']={'chosen_principal_values':'Tuple(-pi/3,0,pi/3)','original_tangent_checks':'Tuple(-sqrt(3),0,sqrt(3))'};p['key_presence']='No fixed chosen inputs are prescribed;the key prints only the general range.';parts.append(p)
p=reasoning('ii-radian-range','−π/2<arctan x<π/2. The bounds are approached butneverattained for finite real inputs.',
 'The same principal inverse function is being measured in radians. Its endpoint limits are±π/2andits derivative1/(1+x²)is positive for every realx. The source key correctly excludes both endpoints.',364,'matches')
p['additional_operations']={'radian_endpoint_limits':{'kind':'identity','operands':['Tuple(limit(atan(x),x,-oo),limit(atan(x),x,oo))']},'monotone_derivative':{'kind':'identity','operands':['diff(atan(x),x)']}}
p['additional_operation_expected']={'radian_endpoint_limits':'Tuple(-pi/2,pi/2)','monotone_derivative':'1/(1+x**2)'};parts.append(p)
row=add('Activity',8,313,'Evaluate six principal arctangents in degrees,interpret their open bounds,choose some radian examples,andstate the radian range. No complex-number calculation is required.',parts,[PRINCIPAL,RANGE])
row['value_level_scope_decisions']=[{'rule_id':'8227:QUAL07','status':'within','quoted_value':'arctanxforrealx;−90°<arctanx<90°or−π/2<arctanx<π/2','reason':'The explicitly requested inverse-function range is a simple principal-branch case with open endpoint bounds. The source’s largest/smallest wording doesnot produce attained extrema.'}]

parts=[]
table=[('pi4','pi/4',{'tan':'1','sin':'1/sqrt(2)','cos':'1/sqrt(2)'}),('pi6','pi/6',{'tan':'1/sqrt(3)','sin':'Rational(1,2)','cos':'sqrt(3)/2'}),('pi3','pi/3',{'tan':'sqrt(3)','sin':'sqrt(3)/2','cos':'Rational(1,2)'})]
for label,theta,keys in table:
    for fn,key in keys.items():parts.append(value(label+'-'+fn,f'{fn}({theta})',key,364,
      'Derive the source’s exact special-angle ratio from the1,1,√2isosceles right triangle or the1,√3,2half-equilateral triangle. The table requests exact surds,not a calculator decimal;equivalent rationalised forms agree.'))
row=add('Activity',11,315,'Complete allnine exact cells fortan,sin,cosatπ/4,π/6,π/3,using the two standard right triangles inFigure11.17. This pure trig activity is prescribed despite its placement in the complex chapter.',parts,[EXACT],rep='table')

p=reasoning('iii-double-angle-proof','arctan(4/3)=2arctan(1/2).',
 'Letθ=arctan(1/2). Since0<1/2<1andprincipal tangent is increasing,0<θ<π/4,so0<2θ<π/2. The double-angle formula gives tan2θ=2(1/2)/(1−(1/2)²)=4/3. Uniqueness on the principal interval therefore establishes the exact equality. The original explicitly allows or otherwise,so this ordinary trig proof meets its method condition.',317,'show/prove')
p['additional_operations']={'double_angle_value':{'kind':'identity','operands':['2*Rational(1,2)/(1-Rational(1,2)**2)']},'direct_identity':{'kind':'identity','operands':['tan(2*atan(Rational(1,2)))-Rational(4,3)']}}
p['additional_operation_expected']={'double_angle_value':'Rational(4,3)','direct_identity':'0'}
add('Exercise-11E',8,317,'Retain(iii):prove an exact inverse-tangent double-angle identity,using the source-permitted ordinary-trig alternative andexplicit principal-range justification. Earlier complex parts remainadditional.',[p],[APPLY],[DOUBLE,PRINCIPAL],excluded=['Parts(i)/(ii)require complex-number representations/arithmetic. Part(iii)expressly permits an alternative proof anddoesnot need their results.'],attribution='Cambridge9709Paper3Q7June2006')

parts=[]
for fn,key in [('cos','(sqrt(3)-1)/(2*sqrt(2))'),('sin','(sqrt(3)+1)/(2*sqrt(2))')]:
    p=value('trig-conclusion-'+fn,f'{fn}(pi/4+pi/6)',key,367,
      'Independently use the45°+30°compound-angle identity andexact triangle ratios to check the stated75°surds. This verifies the underlying trig result as supporting evidence;it doesnot pretend to satisfy the original hence instruction from its preceding complex-number steps.');parts.append(p)
add('Exercise-11G',5,326,'Retain the exact75°cosine/sine conclusions as supporting compound-angle evidence. The original begins with complex division/polar form andthen says hence;its full method is additional.',parts,teaches=[COMPOUND,APPLY,EXACT],excluded=['The original hence chain requires preceding complex-number work. Ordinary compound-angle recomputation checks the result only,not full compliance with that source method.'],rep='text')
p=reasoning('ii-trig-result','arctan(3/5)+arctan(1/4)=π/4.',
 'Forα=arctan(3/5),β=arctan(1/4),both lie in(0,π/4),so0<α+β<π/2. Tangent addition gives(3/5+1/4)/(1−3/20)=1. Uniqueness in that interval givesα+β=π/4. This is an independent mathematical check of the result;the original expressly requires considering complex arguments andthat method stays additional.',327,'show/prove')
p['additional_operations']={'compound_tangent':{'kind':'identity','operands':['(Rational(3,5)+Rational(1,4))/(1-Rational(3,5)*Rational(1,4))']}};p['additional_operation_expected']={'compound_tangent':'1'}
add('Exercise-11G',9,327,'Check(ii)’s inverse-tangent sum as supporting compound-angle/principal-range evidence,while preserving its original forced complex-argument method boundary.',[p],teaches=[COMPOUND,APPLY,PRINCIPAL],excluded=['Part(i)andthe explicitly required argument method in(ii)arecomplex-number work. No directly assessed original8227coverage is claimed.'],attribution='Cambridge9709Paper33Q5November2014')

p=value('i-real-integer-root','solveset(x**3-2*x**2-6*x+27,x,domain=Interval(-6,0))','FiniteSet(-3)',368,
 'Solve the original real cubic inside the stated closed interval−6≤x≤0. Independently factor it as(x+3)(x²−5x+9);the quadratic discriminant is−11,so−3is the only real root. The original requests only this real root in(i).')
p['additional_operations']={'original_root_residual':{'kind':'identity','operands':['(-3)**3-2*(-3)**2-6*(-3)+27']},'factor_identity':{'kind':'identity','operands':['expand((x+3)*(x**2-5*x+9))-(x**3-2*x**2-6*x+27)']}};p['additional_operation_expected']={'original_root_residual':'0','factor_identity':'0'}
add('Exercise-11H',8,330,'Retain(i):find the real integer root ofz³−2z²−6z+27=0in−6≤z≤0. Part(ii)asks allcomplex roots andremainsadditional.',[p],[POLYROOT],[FACTOR],excluded=['Part(ii)requires two non-real roots;no complex-root curriculum demand is added.'])
p=value('coefficient-k','4**3-4**2-3*4','36',368,
 'Substitute the given root4into the original cubic,so64−16−12−k=0andk=36. This independently requested coefficient is prescribed factor-theorem evidence;the later non-real roots remain outside scope.')
p['additional_operations']={'original_factorisation':{'kind':'identity','operands':['expand((x-4)*(x**2+3*x+9))-(x**3-x**2-3*x-36)']},'required_root_sum':{'kind':'identity','operands':['4+(-3)']},'printed_root_sum':{'kind':'identity','operands':['4+2*(-Rational(5,2))']}}
p['additional_operation_expected']={'original_factorisation':'0','required_root_sum':'1','printed_root_sum':'-1'}
add('Exercise-11H',9,330,'Given root4ofz³−z²−3z−k=0,retain determination ofk=36. The original later asks non-real roots;its key has a separate confirmed wrong real component in those additional roots.',[p],[COEFFICIENT],[FACTOR],excluded=['The other-root goal requires complex numbers. Native key368prints−5/2±3√3i/2,butreal factorisation requires−3/2±3√3i/2. This boundary defect is recorded without counting a complex answer as an assessed8227response.'])

for n,page,label,note,teaches,rep,checks,parent in [
 (1,294,'Figure11.1 real-number nesting','Natural numbers lie inside integers,inside rationals,inside reals. Irrationals occupy the real complement of the rationals. Number classification is prerequisite support;no new ASdemand is invented.',[],'diagram',[],'Prompt:1'),
 (2,295,'Real quadratic has no real roots','The unasked x²+9=0illustration has discriminant−36andno real roots becausex²≥0. Extending to complex roots is additional;the real discriminant interpretation is useful teaching support.',['8227:2020:M1:T1:O02:D01','8227:2020:M1:T1:O02:D02'],'table',[('0**2-4*1*9','-36')],None),
 (3,306,'Figure11.3 origin-based vector analogy','The Argand pointx+iycorresponds to the position vector(x,y). The complex plane is additional representation;the origin-to-point arrow supports the prescribed position-vector concept.',['8227:2020:M1:T7:O03:D03'],'diagram',[],None),
 (4,306,'Figure11.4 parallelogram sum analogy','The two position vectors have resultant diagonalz₁+z₂. The ordinary vector sum/parallelogram relationship is retained as supporting illustration in its original complex notation.',[ADD],'diagram',[],None),
 (5,306,'Figure11.5 translated head-to-tail sum','A free vector can be translated to form a head-to-tail triangle without changing its components. The source uses the same complex addition result;the retained facet is vector interpretation.',[ADD],'diagram',[],None),
 (6,306,'Figure11.6 other diagonal subtraction','The other parallelogram diagonal,w,hasz₂+w=z₁andthereforew=z₁−z₂. Arrow orientation is part of the relation;the scalar diagonal length alone is insufficient.',[ADD,DISP],'diagram',[],'Activity:7'),
 (7,307,'Figure11.7 directed subtraction','The arrow fromz₂toz₁representsz₁−z₂. Reversing the endpoints gives the negative vector. Formal complex interpretation stays additional.',[DISP,ADD],'diagram',[],'Activity:7'),
 (8,307,'Figure11.8 modulus-length analogy','The right triangle with signed coordinate offsetsx,yhas positive Euclidean length√(x²+y²). The complex modulus notation remains additional;the ordinary vector norm relation is retained as support.',[MAG],'diagram',[('sqrt(x**2+y**2)','sqrt(y**2+x**2)')],None),
 (9,313,'Principal inverse-tangent quadrant warning','A calculator’s principal arctangent lies strictly between−π/2andπ/2. It alone cannot encode all quadrant orientations of a nonzero vector or a complex argument. The inverse-trig range is prescribed;Argand reconstruction is additional.',[PRINCIPAL],'table',[],'Activity:8'),
 (10,315,'Figure11.17 exact-angle triangles','The1,1,√2right triangle gives45°ratios. Halving an equilateral side2triangle gives legs1,√3andhypotenuse2for30°/60°. The activity asks exact surds,not decimal approximations.',[EXACT],'diagram',[('sqrt(1**2+1**2)','sqrt(2)'),('sqrt(2**2-1**2)','sqrt(3)')],'Activity:11')]:
    fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:
    f['item_id']=f['item_id'].replace(':C5:',':C11:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C11:')if f['parent_item_id']else None
    f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]

notes={
 294:'Figure11.1andthe two-part real-number prompt retained as prerequisite support. The opening jigsaw photograph/quotation motivates imaginary numbers;no prescribed mathematical given/response depends on it.',
 295:'Irrational-complement prompt,allnineActivity11.1classifications,allfiveActivity11.2root/classification pairs,andthe unasked negative-discriminant callout retained. Complex extension remains additional.',
 296:'Imaginary-number definitions,Example11.1complex quadratic andgeneral extension exposition are additional. The original task demands non-real roots;no directly assessed8227coverage is created from incidental quadratic arithmetic.',
 297:'Example1verification,Activity11.3complex-root substitution,powers-of-iprompts andcomplex arithmetic/conjugation references are additional.',
 298:'Example11.2complex coefficients,Activity11.4conjugate sums/products,andcomplex equality exposition are additional.',
 299:'Rational-equality counterexample retained asPrompt3. Example11.3real/imaginary coefficient comparison and11A1(i–xii)complex arithmetic remainadditional.',
 300:'11A2–7all require complex roots,conjugation orcomplex-coefficient expressions;additional original goals. No independently requested prescribed task starts.',
 301:'Example11.4complex division,Activity11.5reciprocal/conjugate proof,andcomplex-denominator method are additional.',
 302:'Examples11.5/6complex division remainadditional. The rational-surddenominator analogy is unasked explanatory support,not another original practice task.',
 303:'Example11.7complex square roots,reciprocal-ipower prompts,and11B1complex quotients are additional.',
 304:'11B9(i)factor expansion/general quadratic construction retained with its real-root facet explicit.11B2–8,9(ii)and10require complex operations/roots andremainadditional.',
 305:'Figure11.2Argand plotting,Activity11.6complex negation/conjugation andimaginary-axis reflection prompt are additional. They are not mistaken for a prescribed complex-plane objective.',
 306:'Allfour ordinary-vector analogy diagrams11.3–11.6retained as supporting evidence. Their Argand axes stay explicitly additional representation.',
 307:'Figure11.7,Activity11.7two subtraction sketches,andFigure11.8norm analogy retained as supporting vector evidence;no directcomplex assessment is claimed.',
 308:'11C1–6andthe distance-of-complex-difference prompt require Argand/complex notation orpowers andremainadditional.',
 309:'Figure11.9complex distance andExample11.8/Figure11.10circle locus remainadditional original representation;no ordinary Cartesian question is silently substituted.',
 310:'Both three-case complex-locus prompts,Example11.9andFigure11.11half-plane locus are additional.',
 311:'11D1–5complex loci andFigure11.12complex-argument introduction remainadditional.',
 312:'Figures11.13/14,three exact complex-argument prompts andpolar-form exposition remainadditional. Principal complex argument is not automatically the8227inverse-trig principal-value demand.',
 313:'EveryActivity11.8output retained:6degree values,degree/radian open bounds andexplicitly author-chosen radian examples. Figure11.15complex-quadrant illustration remainsadditional;its calculator principal-range warning is separately retained.',
 314:'Figure11.16,Activities11.9/10complex arguments/calculator polar conversion,andpolar rewriting exposition are additional. Calculator menus are not new assessed mathematical demands.',
 315:'Activity11.11allnine exact ratios andFigure11.17triangles retained. The polar-rewriting prompt andExample11.10complex polar conversion remainadditional.',
 316:'Example10continuation and11E1–4complex modulus/argument/polar forms remainadditional.',
 317:'11E8(iii)expressly permits an ordinary-trig alternative andis retained.11E5–7,8(i)/(ii)and9require complex methods/representations andremainadditional.',
 318:'11E9continuation,argument-of-difference prompt andFigure11.18Argand direction relationships are additional. The complex chapter is not globally certified mathematically correct.',
 319:'Example11.11andFigures11.19–11.21Argand rays/wedges remainadditional.',
 320:'11F1–5all ask complex-plane regions/roots/arguments;additional original goals.',
 321:'11F6–8complex exam-style tasks andpolar multiplication exposition remainadditional.',
 322:'Activity11.12complex multiplication/rotations andpolar division/spiral-dilation exposition are additional;incidental negative-vector scaling is not a new original8227task.',
 323:'Figure11.22,Activity11.13measured complex multiply/divide plots,andExample11.12polar products remainadditional.',
 324:'Figure11.23polar roots,integer-turn square-root prompt andcomplex-exponent introduction are additional.',
 325:'ComplexODE/Euleridentity exposition andExample11.13complex exponential arithmetic remainadditional.',
 326:'11G5exact-trig conclusions are retained as supporting boundary-method evidence;its enforced hence chain stays additional. Example13continuation and11G1–4/6require complex operations andremainadditional.',
 327:'11G9(ii)trig identity is checked as support while its forced argument method stays additional.11G7/8and9(i),andfundamental-theorem complex-root exposition,remainadditional.',
 328:'Activity11.14calculator polynomial procedure andExamples11.14/15complex-conjugate roots are additional. No calculator operation is executed orclaimed assessed.',
 329:'Example15continuation and11H1–7complex-root/Argand goals remainadditional. An integer intermediate root inside a whole complex-solving task doesnot automatically become an independently asked prescribed output.',
 330:'11H8(i)real root and11H9coefficient determination retained.8(ii),9other roots,and10–13complex roots/Argand work remainadditional. Native source/key confirmH9’s separate wrong real component in the excluded non-real answers;coefficient36is correct.',
 331:'All15complex-number keypoints are additional reference;no new original task orprescribed given figure starts.',
 332:'Complex-number learning outcomes are additional;no new original task orprescribed figure starts.'}
pages=[]
for page in range(294,333):
    ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':11,'page_status':'items enumerated'if ids else'scope-screened; no in-scope item starts',
      'item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19',
      'non_item_content':notes[page],'scope_screen':'All39renderedpages screened. Retained real/trig/vector facets have individual records;original complex-number goals andforced methods stay explicitly additional. Independent scope acceptance pending.'})

conventions={'book_id':'8227-SRC-015','source_path':SRC,'source_sha256':SHA,'pdf_page':333,'printed_page':319,
 'evidence':ev(333),'source_kind':'transcribed book-wide answer preface','short_excerpt':'Non-exact numerical answers should be given correct to three significant figures',
 'non_exact_significant_figures':3,'degree_angle_decimal_places':1,'question_specific_instruction_overrides':True,'round_only_final_answer':True,
 'interpretation':'Applies across this book unless the original question specifies another precision. Exact surds/formulas remain exact. Do not mistake a key’s inconsistent display for a per-question requirement orimport this convention as an official NSSCAS marking rule.',
 'checked_by':'Codex author;independent acceptance pending','date':'2026-11-19'}

if __name__=='__main__':
    for name,data in [('answers-Goldie-C11.json',{'scope':'Every retainedC11source output;complex-number original scope remains explicit.','items':answers}),
      ('census-Goldie-C11.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':11,'source_path':SRC,'source_sha256':SHA,
        'scope':'All39pages294–332screened;retainedpuretrig,realpolynomialandprerequisite/vectorfacetsindividuallyrecorded. Excluded complex mathematics is not claimed fully recomputed.',
        'new_items':new+figures,'corrections':[],'pages':pages,'book_answer_conventions':conventions})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    for r in answers:
        for p in r['subparts']:
            if 'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'])
            for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures;',len(pages),'pages')
