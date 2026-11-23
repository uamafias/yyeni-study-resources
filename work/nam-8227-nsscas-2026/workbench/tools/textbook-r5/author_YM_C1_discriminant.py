"""Fixed-source YM25–30: discriminate roots, retain parameter and proof boundaries."""
import json
import author_YM_C1_opening as opening
from author_YM_C1_opening import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent
opening.base.answers.clear();opening.base.new.clear();figures.clear()
answers=opening.base.answers;new=opening.base.new;corrections=[]
CALC='8227:2020:M1:T1:O02:D01';NATURE='8227:2020:M1:T1:O02:D02';QUAD=opening.QUAD
PARAM='8227:2020:M1:T1:O02:D03'

def add(kind,n,page,note,parts,direct=None,existing=True):
    r=opening.add(kind,n,page,note,parts,[CALC,NATURE] if direct is None else direct,
                  components=[] if direct is None else [QUAD])
    # Explicit parameter-condition tasks were previously missing their separate
    # demand. This source-item decision is independent of the family catalogue.
    if (kind,n)in [('Example',15),('Example',16),('Example',17),
                   ('Try-Now-15',1),('Try-Now-15',2),
                   ('Try-Now-16',1),('Try-Now-16',2),('Try-Now-16',3),('Try-Now',17)]:
        r['assessed_8227_demand_ids']=sorted(set(r['assessed_8227_demand_ids'])|{PARAM})
        for part in parts:
            part.update(assessed_8227_demand_ids=[CALC,NATURE,PARAM],component_demand_ids=[])
    r['mapping_rationale']='The requested discriminant, root classification, parameter condition or universal root proof is assessed directly. Given-root substitution and ordinary quadratic solving are prerequisite support. A general proof must preserve coefficient domains, zero-discriminant cases and any linear degeneration.'
    r['precision_angle_check']={'source':'Exact integer/rational parameters and discriminants; no angle units. Rounded graph labels are illustrative.',
      'comparison':'Keep parameter endpoints, repeated roots and exact irrational values. No textbook convention overrides an examination instruction.'}
    if existing:
        prior=new.pop();corrections.append({k:prior[k]for k in ['item_id','pdf_page','printed_page','continuation_pdf_pages']})
    return r

def logic(label,result,working,kp,status='matches',ops=None):
    r=reasoning(label,result,working,kp,status)
    if ops:
        r['additional_operations']={n:{'kind':'identity','operands':[expr]}for n,expr,expected in ops}
        r['additional_operation_expected']={n:expected for n,expr,expected in ops}
    return r

# The method instruction excludes solving as the demonstration, even though root
# calculation is used as an independent secondary check in the author evidence.
p=logic('nature','Discriminant25; two distinct real rational roots.',
 'Move all terms of x²+8−x=2(x+6) to the left: x²−3x−4=0. Compute Δ=(−3)²−4(1)(−4)=25. Its positive integer square gives two distinct rational real roots without solving the equation, as requested. Independently, the polynomial factors (x−4)(x+1).',27,
 ops=[('discriminant','(-3)**2-4*1*(-4)','25'),('standard_form','expand(x**2+8-x-2*(x+6))','x**2-3*x-4'),('independent_factorisation','expand((x-4)*(x+1))','x**2-3*x-4')])
add('Example',14,27,'Classify x²+8−x=2(x+6) without solving. Standardisation precedes the discriminant; a root list alone does not demonstrate the requested method.',[p])
parts=[]
for label,a,b,c,D,nature in [('a',2,-7,-3,73,'two distinct real irrational roots'),('b',3,2,1,-8,'no real roots'),('c',4,-20,25,0,'one distinct real rational root of multiplicity two'),('d',7,12,5,4,'two distinct real rational roots'),('e',4,-1,-1,17,'two distinct real irrational roots'),('f',3,4,1,4,'two distinct real rational roots')]:
    kp=588 if label=='f'else 587
    parts.append(logic(label,f'Discriminant {D}; {nature}.',
     f'The original coefficients are a={a}, b={b}, c={c}; a is nonzero and all coefficients are integers. Compute Δ=b²−4ac={D}. Interpret its sign first, then its perfect-square status when positive. The source says without solving; the discriminant explanation is required.',kp,
     ops=[('discriminant',f'({b})**2-4*({a})*({c})',str(D))]))
add('Try-Now',14,27,'Classify all six integer-coefficient quadratics without solving: positive nonsquare, negative, zero and positive square discriminants occur. Part(f) continues on answer page588.',parts)

p=v('p','solveset(16**2-4*x,x,domain=S.Reals)','FiniteSet(64)',27,
 'The leading coefficient is1 throughout. Two equal roots require Δ=16²−4p=0, giving p64. At p64 the original is (x+8)², confirming the repeated root.')
add('Example',15,27,'Find the constant p in x²+16x+p=0 from the repeated-root condition. The quadratic coefficient is fixed nonzero.',[p])
for n,note,rows in [
 (1,'Find p in two repeated-root quadratics: the constant coefficient gives one parameter value, while the unknown linear coefficient gives both signs.',[
 ('a','solveset((-28)**2-4*2*(-x),x,domain=S.Reals)','FiniteSet(-98)','2x²−28x−p has Δ=784+8p. The leading coefficient remains2; equate Δ to zero.'),
 ('b','solveset(x**2-4*25*4,x,domain=S.Reals)','FiniteSet(-20,20)','25x²+px+4 has Δ=p²−400. Both p signs are allowed and produce repeated roots.')]),
 (2,'Find k in two repeated-root conditions, including a parameter in both the linear and constant terms. Keep the repeated parameter solution rather than counting it twice.',[
 ('a','solveset((-2)**2-4*3*(1-x),x,domain=S.Reals)','FiniteSet(Rational(2,3))','3x²−2x+1−k has Δ=12k−8; set it to zero.'),
 ('b','solveset((x+1)**2-4*x,x,domain=S.Reals)','FiniteSet(1)','x²+(k+1)x+k has Δ=(k−1)², which vanishes only at k1.')])]:
    ps=[v(l,e,k,588,m+' Independently substitute the resulting parameter into the original polynomial and check a repeated factor.')for l,e,k,m in rows]
    add('Try-Now-15',n,28,note,ps)

p=v('parameter-range','solve_univariate_inequality(25+8*(3*x+4)>0,x,relational=False)','Interval.open(-Rational(19,8),oo)',28,
 'For 2x²+5x−(3m+4), Δ=57+24m. Its leading coefficient is always2. Two distinct real roots require the strict inequality Δ>0, hence m>−19/8. At the boundary there is only a repeated root.')
add('Example',16,28,'Determine the strict m range for two distinct real roots of 2x²+5x−(3m+4)=0; the discriminant boundary is excluded.',[p])
for n,note,expr,key,method in [
 (1,'Collect both quadratic sides of 3x²−4x=2x(x+1)+2m before imposing two distinct real roots.','solve_univariate_inequality(36+8*x>0,x,relational=False)','Interval.open(-Rational(9,2),oo)',
  'Standard form is x²−6x−2m=0, with fixed a1 and Δ=36+8m. Strict positivity gives m>−9/2.'),
 (2,'Standardise x²+4x−2p=−7 and impose two distinct real roots. The constant term is 7−2p.','solve_univariate_inequality(16-4*(7-2*x)>0,x,relational=False)','Interval.open(Rational(3,2),oo)',
  'Δ=16−4(7−2p)=8p−12. The leading coefficient1 never degenerates; strict positivity gives p>3/2.'),
 (3,'Find m for two real roots of (2−m)x²=4x+4. The source hint Δ>0 selects distinct roots; exclude m2 where the equation becomes linear.',
  'Complement(solve_univariate_inequality(16+16*(2-x)>0,x,relational=False),FiniteSet(2))','Interval.open(-oo,3)',
  'For m≠2 the discriminant is48−16m, so m<3. At m2 the original reduces to −4x−4=0, which has only one root. Correct intended range is (−∞,2)∪(2,3), not the key’s entire m<3. The wording two real roots could count multiplicity at m3; the printed Δ>0 hint resolves the intended distinct-root condition and is retained explicitly.')]:
    p=v('parameter-range',expr,key,588,method)
    if n==3:
        p['author_expected_normalised']='Union(Interval.open(-oo,2),Interval.open(2,3))'
        p['additional_operations']={'linear_boundary_roots':{'kind':'real-roots','operands':['-4*x-4']},'repeated_boundary_roots':{'kind':'real-roots','operands':['-x**2-4*x-4']}}
        p['additional_operation_expected']={'linear_boundary_roots':'FiniteSet(-1)','repeated_boundary_roots':'FiniteSet(-2)'}
    add('Try-Now-16',n,28,note,[p])
p=v('parameter-range','solve_univariate_inequality(4*x**2-4*(x**2+5*x-6)<0,x,relational=False)','Interval.open(Rational(6,5),oo)',28,
 'The original x²−2kx+k²+5k−6 has Δ=24−20k and fixed leading coefficient1. No real roots means Δ<0. Dividing by−20 reverses the inequality, giving k>6/5. At the boundary a repeated real root exists.')
add('Example',17,28,'Determine the no-real-root range of x²−2kx+k²+5k−6=0, keeping the strict inequality and sign reversal.',[p])
parts=[]
for label,expr,key,method in [
 ('a','64-8*x','Interval.open(8,oo)','2x²+8x+k has fixed leading coefficient2. Its discriminant64−8k must be negative.'),
 ('b','49+4*x','Interval.open(-oo,-Rational(49,4))','kx²+7x−1 has Δ49+4k. Its negative-discriminant range k<−49/4 already excludes k0. At k0 the linear equation has a real root, so no extra case belongs.'),
 ('c','64-8*x','Interval.open(8,oo)','x²+2k=−8x standardises to x²+8x+2k; Δ64−8k<0.'),
 ('d','16+12*(2*x+5)','Interval.open(-oo,-Rational(19,6))','3x²+4x−(2k+5) has Δ76+24k<0. Its leading coefficient3 is fixed.')]:
    parts.append(v(label,f'solve_univariate_inequality(({expr})<0,x,relational=False)',key,588,method+' Retain strict endpoints because Δ0 gives a real repeated root.'))
add('Try-Now',17,29,'Find all four no-real-root parameter ranges; one leading coefficient varies, so its linear case is checked rather than assumed quadratic.',parts)

p=v('a-m','solve(2**2+(x+1)*2-4*x,x)[0]','3',29,
 'Substitute the given root x2 into x²+(m+1)x−4m=0. The resulting 6−2m=0 gives m3.')
p2=v('b-other-root','-4-2','-6',29,
 'With m3 the polynomial is x²+4x−12=(x−2)(x+6). The given root is2, so the other is−6. Sum and product independently agree.')
add('Example',18,29,'Use a given root2 to determine m in x²+(m+1)x−4m=0, then obtain the other root with that same parameter.',[p,p2],direct=[],existing=False)
for n,note,rows in [
 (1,'Given root3 of x²+(p−1)x−6p=0, determine p and its other root.',[
 ('a-p','solve(9+3*(x-1)-6*x,x)[0]','2','Substitute x3, giving6−3p=0 and p2.'),('b-other-root','-1-3','-4','At p2 the polynomial is x²+x−12; the sum of roots−1 gives the other root−4.')]),
 (2,'Given root−1 of 3x²−x+n=0, determine n and the other root.',[
 ('a-n','solve(3+1+x,x)[0]','-4','Substitute x−1, giving4+n=0 and n−4.'),('b-other-root','Rational(1,3)-(-1)','Rational(4,3)','The root sum is1/3, so subtracting the given−1 gives4/3. The factorisation (x+1)(3x−4) confirms it.')]),
 (3,'Given x=m is a root of 4x²−(m+3)x−3m=0, find both m values and preserve the conditional other root for each value.',[
 ('a-m-values','solveset(4*x**2-(x+3)*x-3*x,x,domain=S.Reals)','FiniteSet(0,2)','Substitution x=m gives3m(m−2)=0, so m0 or2. Neither is removed.'),
 ('b-other-roots','FiniteSet(Rational(3,4),-Rational(3,4))','FiniteSet(-Rational(3,4),2)',
  'At m0 the polynomial x(4x−3) has given root0 and other3/4. At m2, (x−2)(4x+3) has given root2 and other−3/4. The key prints−3/4 or2, incorrectly listing a given root and omitting3/4. Preserve pairs (m,other)=(0,3/4),(2,−3/4).')])]:
    ps=[v(l,e,k,588,m)for l,e,k,m in rows]
    if n==3:
        ps[-1]['author_expected_normalised']='FiniteSet(-Rational(3,4),Rational(3,4))'
        ps[-1]['additional_operations']={'conditional_other_roots':{'kind':'identity','operands':['Tuple((0+3)/4-0,(2+3)/4-2)']},'original_checks':{'kind':'identity','operands':['Tuple(4*Rational(3,4)**2-3*Rational(3,4),4*(-Rational(3,4))**2-5*(-Rational(3,4))-6)']}}
        ps[-1]['additional_operation_expected']={'conditional_other_roots':'Tuple(Rational(3,4),-Rational(3,4))','original_checks':'Tuple(0,0)'}
    r=add('Try-Now-18',n,29,note,ps,direct=[],existing=False)
    if n==3:r['correlated_branch_check']={'required_pairs':[[0,'3/4'],[2,'-3/4']],'reason':'Part(b) explicitly asks for the other root for each m. An unordered set alone is insufficient marking evidence.'}

p=logic('universal-rationality','False as stated: roots are −2 and −1/(p+1); the second need not be rational for real p.',
 'Factor exactly as (x+2)((p+1)x+1), using the stem’s p≠−1. Taking p=√2 gives the irrational root1−√2. Thus the requested universal rationality proof is impossible. Real-root existence is true; Δ=(2p+1)²≥0, with equality at p−1/2. The printed positive-square claim also fails at that parameter. Restricting p to rational values would repair rationality, but that would change the original task and is not silently adopted.',30,'key wrong',
 [('factorisation','expand((x+2)*((p+1)*x+1))-((p+1)*x**2+(2*p+3)*x+2)','0'),('counterexample_root','simplify(-1/(sqrt(2)+1))','1-sqrt(2)'),('zero_discriminant','(2*(-Rational(1,2))+1)**2','0')])
r=add('Example',19,30,'Audit the requested universal rational-root proof for real p≠−1. Its rationality conclusion is false; retain a held source exemplar with a counterexample, not a repaired proof passed off as original.',[p]);r['source_interpretation']='Original proof demand is false and held as an exemplar; only the valid real-root/discriminant facets support planning.'
parts=[logic('a-integer-proof','For integer p,k the roots are −p and −k; all are real rational, including repeated roots when p=k.',
 'Collect x²+(p+k)x+pk=(x+p)(x+k). The discriminant is(p−k)²≥0. The original source explicitly restricts p,k to integers, so rationality follows without the false all-real-coefficients extension. Repeated roots remain valid.',588,'show/prove',
 [('factorisation','expand((x+p)*(x+k))-(x**2+(p+k)*x+p*k)','0'),('discriminant','expand((p+k)**2-4*p*k)','(p-k)**2')]),
 logic('b-integer-proof','For integer p≠0 the roots are −1 and (3p−2)/(3p); at p0 the linear equation has root−1.',
 'Factor 3px²+2x−3p+2=(x+1)(3px−3p+2). For nonzero integer p both displayed roots are real rational. For p0 the equation is2x+2=0 and must be handled separately. The printed discriminant proof omits that linear case, though the final existence/rationality conclusion remains true.',588,'key incomplete',
 [('factorisation','expand((x+1)*(3*p*x-3*p+2))-(3*p*x**2+2*x-3*p+2)','0'),('linear_case','solve(2*x+2,x)[0]','-1')])]
add('Try-Now',19,30,'Prove real rational roots under the source’s integer-parameter restriction. Factorisation exposes repetition in(a) and the p0 linear case in(b).',parts)
p=logic('universal-real-proof','All real k give real solutions: two distinct roots if k≠−1, and x−1/2 if k−1.',
 'Rearrange the original k−1−kx²=x²+4x to (k+1)x²+4x+1−k=0. If k≠−1, Δ=12+4k²>0 establishes two distinct real roots. If k−1 the original is4x+2=0, giving x−1/2. The printed proof establishes the discriminant but never separates the nonquadratic case. Its real-solution conclusion is true, with incomplete justification.',30,'key incomplete',
 [('discriminant','expand(16-4*(k+1)*(1-k))','12+4*k**2'),('linear_root','solve(4*x+2,x)[0]','-Rational(1,2)')])
add('Example',20,30,'Prove real solutions for every real k in k−1−kx²=x²+4x. Keep the k−1 linear branch alongside the positive-discriminant quadratic branch.',[p])
parts=[logic('a-universal-real-proof','For integer q≠−1 there are two distinct real roots; at q−1 there is one real root−2/3.',
 'For(q+1)x²+3x−(q−1)=0, Δ=4q²+5>0. This proves the quadratic cases q≠−1. At q−1 the original is3x+2=0, giving−2/3. The printed key omits this separate case. The source stem uses integer q, although the valid existence statement also extends to real q.',588,'key incomplete',
 [('discriminant','expand(9+4*(q+1)*(q-1))','4*q**2+5'),('linear_root','solve(3*x+2,x)[0]','-Rational(2,3)')]),
 logic('b-universal-real-proof','For integer q,k the discriminant4q²+36k² is nonnegative; it vanishes at q=k0 and otherwise is positive.',
 'The leading coefficient3 is fixed. Sum-of-squares nonnegativity proves real roots. When both parameters are0 the original3x²=0 has a repeated root0; the key’s strict Δ>0 conclusion is false there. Its statement that the roots are real is correct; replace strict positivity with nonnegativity and name the zero case.',588,'key incomplete',
 [('discriminant','expand((2*q)**2-4*3*(-3*k**2))','4*q**2+36*k**2'),('zero_case','4*0**2+36*0**2','0')])]
add('Try-Now',20,30,'Prove real roots for the two integer-parameter equations. Separate q−1 linear degeneration in(a) and the zero-discriminant repeated-root case in(b).',parts)

# Each teaching diagram/reference is internal evidence, not another assessed task.
refs=[
 (28,25,'Quadratic formula and discriminant definition','For ax²+bx+c with a≠0, Δ=b²−4ac controls real root count. Rationality requires coefficient-domain information in addition to the sign of Δ.',[CALC,NATURE],'table',[],None),
 (29,25,'Negative-discriminant two-orientation sketches','Δ<0: an upward parabola is wholly above the x-axis; a downward parabola is wholly below it. Both sketches presume real coefficients and a≠0.',[NATURE],'graph',[],None),
 (30,25,'Negative-discriminant example graph','For2x²+x+3, Δ−23, positive leading coefficient, intercept3 and vertex(−1/4,23/8); no real crossing. The negative square root is not a real answer.',[CALC,NATURE],'graph',[('Tuple(1-4*2*3,2*(-Rational(1,4))**2-Rational(1,4)+3)','Tuple(-23,Rational(23,8))')],None),
 (31,26,'Zero-discriminant orientation pair','The two generic sketches touch the x-axis once when Δ0. The table’s unconditional rational label needs rational coefficients; (x−√2)² has a repeated irrational root despite Δ0.',[NATURE],'graph',[('expand((x-sqrt(2))**2)','x**2-2*sqrt(2)*x+2')],None),
 (32,26,'Repeated-root numerical illustration','−3x²+6x−3=−3(x−1)² touches at(1,0), opens downward and has y-intercept−3. The single distinct root has multiplicity two.',[CALC,NATURE],'graph',[('expand(-3*(x-1)**2)','-3*x**2+6*x-3')],None),
 (33,26,'Positive nonsquare-discriminant orientation pair','Both generic parabolas cross twice when Δ>0. Calling both roots irrational from a nonsquare integer Δ requires rational coefficients; √2x²−√2 has Δ8 yet rational roots±1.',[NATURE],'graph',[('expand(0**2-4*sqrt(2)*(-sqrt(2)))','8')],None),
 (34,26,'Irrational-root illustration with copied caption','The actual plotted example x²−7x−1 has Δ53, roots(7±√53)/2, intercept−1 and vertex(7/2,−53/4). The caption wrongly repeats the preceding tangent parabola; exact irrational surds remain exact values.',[CALC,NATURE],'graph',[('Tuple((-7)**2-4*(-1),(Rational(7,2))**2-7*Rational(7,2)-1)','Tuple(53,-Rational(53,4))')],None),
 (35,26,'Positive-square discriminant orientation pair','Two distinct crossings follow from Δ>0. Rational roots from a square discriminant also require rational coefficients; a square real discriminant alone does not make every coefficient rational.',[NATURE],'graph',[],None),
 (36,26,'Rational-root numerical illustration','−2x²−3x+5 has Δ49 and roots−5/2,1. It opens downward and has y-intercept5. These rational values are exact, including the displayed decimal−2.5.',[CALC,NATURE],'graph',[('Tuple((-3)**2-4*(-2)*5,-2*(-Rational(5,2))**2-3*(-Rational(5,2))+5)','Tuple(49,0)')],None),
 (37,27,'Root-condition summary table','For an actual quadratic: repeated means Δ0; no real roots means Δ<0; at least one real root means Δ≥0; distinct real means Δ>0. The nonzero leading coefficient must be checked before applying these cases.',[NATURE],'table',[],None),
 (38,28,'Inequality sign-reversal note','In Example17, −20k<−24 becomes k>6/5 after division by−20. Reversing the sign is essential; the boundary has a real repeated root.',[NATURE],'table',[('24-20*Rational(6,5)','0')],'Example:17'),
 (39,30,'Square nonnegativity warning','The introductory statement says a square always gives a positive result; zero is possible. Example19 has Δ0 at p−1/2, and Try20(b) has Δ0 at q=k0. Correct bound is nonnegative.',[NATURE],'table',[('Tuple((2*(-Rational(1,2))+1)**2,4*0**2+36*0**2)','Tuple(0,0)')],None),
 (40,30,'All-sign discriminant table for Example20','The source tests k positive, negative and zero for Δ12+4k², with k±3 giving48 and k0 giving12. Those values are correct, but this sign table does not replace the separate k−1 linear case.',[CALC,NATURE],'table',[('Tuple(12+4*3**2,12+4*(-3)**2,12+4*0**2)','Tuple(48,48,12)')],'Example:20')]
for args in refs:fig(*args)
for f in figures:
    f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C1:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C1:')if f['parent_item_id']else None
    f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={25:'Complete discriminant definition/formula, negative-case orientation pair and numerical example/graph. No learner exercise starts here.',
26:'All three remaining generic discriminant cases, their two-orientation sketches and each numerical example are separately recorded. Rationality-domain and copied-caption/exact-value defects are explicit.',
27:'Every Example14/15 and six Try14 responses recorded, plus the root-condition table. Without-solving instructions are preserved.',
28:'Every numbered question under Try15/16, Examples16/17 and the sign-reversal callout is recorded individually. Try16Q3 missing linear exclusion is explicit.',
29:'Every Try17 subpart, Example18 and all three independently numbered Try18 tasks recorded. The last task retains parameter/other-root correspondence.',
30:'Examples19/20, all Try19/20 subtasks and both teaching references recorded. False real-parameter rationality, zero-square and linear-case proof limitations are not silently repaired.'}
pages=[]
for page in range(25,31):
    ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    pages.append({'pdf_page':page,'printed_page':page-11,'chapter':1,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
      'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
      'scope_screen':'All root-classification, parameter, proof and source-reference content screened. Basic given-root tasks remain prerequisite support; generic rationality statements are not adopted without their coefficient domains.'})
if __name__=='__main__':
    for name,data in [('answers-YM-C1-discriminant.json',{'scope':'Every25–30 response, with exact boundaries and separate proof dispositions.','items':answers}),
      ('census-YM-C1-discriminant.json',{'book':'YM','book_id':'8227-SRC-017','chapter':1,'source_path':SRC,'source_sha256':SHA,'scope':'Complete25–30 census, including all table figures.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    for r in answers:
        for p in r['subparts']:
            if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
            for name,op in p.get('additional_operations',{}).items():
                if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
