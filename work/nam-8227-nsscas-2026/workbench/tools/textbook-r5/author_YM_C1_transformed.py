"""YM22–24:solve original radical/transformed equations andretain domain filters."""
import json
import author_YM_C1_opening as opening
from author_YM_C1_opening import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent

opening.base.answers.clear();opening.base.new.clear();figures.clear()
answers=opening.base.answers;new=opening.base.new;corrections=[]
RECOGNISE='8227:2020:M1:T1:O04:D01';SOLVE='8227:2020:M1:T1:O04:D02';FILTER='8227:2020:M1:T1:O04:D03'
QUAD='8227:PRIOR:NSSCO:quadratic'

def add(kind,n,page,note,parts,direct,existing=False):
    row=opening.add(kind,n,page,note,parts,direct,components=[QUAD])
    row['mapping_rationale']='The original nonlinear equation is the assessed goal. Selecting a quadratic substitution andrecovering alladmissible original-variable roots are distinct demands;ordinary quadratic factorisation is a component. A squared candidate is never accepted without the original radical/domain conditions.'
    if existing:
        prior=new.pop();corrections.append({key:value for key,value in prior.items()if key in['item_id','pdf_page','printed_page','continuation_pdf_pages']})
    return row

def roots(label,original,key,kp,method):
    p=v(label,original,key,kp,method);p['operation']={'kind':'real-roots','operands':[original]}
    return p

p=roots('original-roots','x+sqrt(x-4)-4','FiniteSet(4)',22,
 'The real domain isx≥4. Isolate√(x−4)=4−x,whose nonnegative left side also requiresx≤4;these bounds already give onlyx4. Alternatively squaring gives candidates4and5,but5fails the original equation. The source explicitly rejects5after substitution.')
p['additional_operations']={'squared_candidates':{'kind':'real-roots','operands':['x**2-9*x+20']},'original_residuals':{'kind':'identity','operands':['Tuple(4+sqrt(4-4)-4,5+sqrt(5-4)-4)']}}
p['additional_operation_expected']={'squared_candidates':'FiniteSet(4,5)','original_residuals':'Tuple(0,2)'}
add('Example',10,22,'Solve x+√(x−4)=4. The original domain andnonnegative isolated root leave onlyx4;the squared candidate5is extraneous.',[p],[SOLVE,FILTER])

parts=[]
for label,original,key,domain,polynomial in [
 ('a','x-sqrt(x+6)','FiniteSet(3)','x≥0andx≥−6','x**2-x-6'),
 ('b','sqrt(x**2+3)-2*x','FiniteSet(1)','x≥0because the original RHSis2x','3*x**2-3'),
 ('c','sqrt(40-x**2)-3*x','FiniteSet(2)','0≤x≤√40','10*x**2-40'),
 ('d','sqrt(3-4*x)-2*x','FiniteSet(Rational(1,2))','0≤x≤3/4','4*x**2+4*x-3')]:
    p=roots(label,original,key,587,'Start withthe original real/principal-square-root conditions:'+domain+'. Isolate/square to obtain the candidate polynomial '+polynomial+',thencheck candidates in the original equation. A negative RHS cannot equal a principal square root.')
    p['additional_operations']={'squared_candidates':{'kind':'real-roots','operands':[polynomial]}}
    parts.append(p)
add('Try-Now-10',1,22,'Solve four original square-root equations. Each has two algebraic candidates after squaring butonlyone valid principal-root solution;the sign/domain restriction is explicit per response.',parts,[SOLVE,FILTER])
p=reasoning('a-no-real-solution','No real solution.',
 'The original1=t+√(2t−3)requires t≥3/2. Its RHS isthen at least3/2,greater than1. This is a complete direct infeasibility proof;there is no need to force a quadratic method. Squaring without the original sign/domain constraint wouldmislead. The source key correctly says No solution.',587,'matches')
p['additional_operations']={'independent_real_solution_set':{'kind':'real-roots','operands':['1-x-sqrt(2*x-3)']}};p['additional_operation_expected']={'independent_real_solution_set':'EmptySet'}
p2=roots('b','x-sqrt(5*x+6)+2','FiniteSet(-1,2)',587,
 'The original equation t=√(5t+6)−2gives t+2=√(5t+6),with t≥−6/5. Squaring gives t²−t−2=0. Both t−1andt2satisfy the original domain andequation;do not reject a negative variable merely because the isolated square root is nonnegative.')
p2['additional_operations']={'both_original_checks':{'kind':'identity','operands':['Tuple(-1-sqrt(5*(-1)+6)+2,2-sqrt(5*2+6)+2)']}};p2['additional_operation_expected']={'both_original_checks':'Tuple(0,0)'}
add('Try-Now-10',2,22,'Solve two further radical equations:one is impossible fromits real-domain lower bound,the other admits both a negative andpositive original variable value.',[p,p2],[FILTER])

p=roots('original-roots','sqrt(2*x-1)-sqrt(x-4)-2','FiniteSet(5,13)',23,
 'Original domainy≥4. Isolate the first root,square,thenisolate the remaining root andsquare again to obtainy²−18y+65=0. Both5and13satisfy the original equation;the two-squaring process must not be assumed reversible without these checks.')
p['additional_operations']={'candidate_polynomial':{'kind':'real-roots','operands':['x**2-18*x+65']},'original_checks':{'kind':'identity','operands':['Tuple(sqrt(2*5-1)-sqrt(5-4)-2,sqrt(2*13-1)-sqrt(13-4)-2)']}}
p['additional_operation_expected']={'candidate_polynomial':'FiniteSet(5,13)','original_checks':'Tuple(0,0)'}
add('Example',11,23,'Solve√(2y−1)−√(y−4)=2using two squarings ifneeded. Both candidate roots5and13are valid in the original real domain.',[p],[SOLVE,FILTER])
p=roots('a','sqrt(3-x)-sqrt(x+7)-2','FiniteSet(-6)',587,
 'Original domain−7≤x≤3. After the first squaring,the remaining equality is−x−4=2√(x+7),which further requiresx≤−4. The second squaring gives candidates−6and2;only−6satisfies the original equation.')
p['additional_operations']={'squared_candidates':{'kind':'real-roots','operands':['x**2+4*x-12']},'original_residuals':{'kind':'identity','operands':['Tuple(sqrt(3-(-6))-sqrt(-6+7)-2,sqrt(3-2)-sqrt(2+7)-2)']}}
p['additional_operation_expected']={'squared_candidates':'FiniteSet(-6,2)','original_residuals':'Tuple(0,-4)'}
p2=roots('b','6/sqrt(3*x-1)-sqrt(3*x-1)-1','FiniteSet(Rational(5,3))',587,
 'Original domainy>1/3because the root is also a denominator. Setu=√(3y−1)>0. Multiplication byu isvalid andgivesu²+u−6=0,whose roots2and−3leave onlyu2. Hencey5/3;the discarded negativeu doesnot create an extra originalyroot.')
add('Try-Now',11,23,'Solve one two-root radical equation andone reciprocal-root equation. Retain the intermediate sign condition in(a)andthe strictly positive substitution/denominator condition in(b).',[p,p2],[RECOGNISE,SOLVE,FILTER])

p=roots('original-roots','x**4-5*x**2+4','FiniteSet(-2,-1,1,2)',23,
 'Setu=x²≥0. The quadraticu²−5u+4=(u−1)(u−4)hasu1and4. Recover both real square-root signs fromeach positiveu. The source also supplies a direct factorisation alternative;allfour original roots are required.')
p['additional_operations']={'quadratic_substitution_roots':{'kind':'real-roots','operands':['x**2-5*x+4']},'direct_factor_identity':{'kind':'identity','operands':['expand((x-2)*(x+2)*(x-1)*(x+1))-(x**4-5*x**2+4)']}}
p['additional_operation_expected']={'quadratic_substitution_roots':'FiniteSet(1,4)','direct_factor_identity':'0'}
add('Example',12,23,'Solve x⁴−5x²+4=0by a quadratic substitution ordirect factorisation. Both signs of each original-variable square root are retained.',[p],[RECOGNISE,SOLVE,FILTER],existing=True)
parts=[]
for label,original,key in [('a','x**4-13*x**2+36','FiniteSet(-3,-2,2,3)'),('b','x**4-7*x**2+12','FiniteSet(-2,-sqrt(3),sqrt(3),2)')]:
    parts.append(roots(label,original,key,587,'Useu=x²≥0to reduce the original quartic to a quadratic. Solve foru,thenrecover both real signs for every positiveu. Check the resulting set in the original polynomial;do not return only the positive roots.'))
add('Try-Now',12,24,'Solve two quartics quadratic inx². One has four integer roots;the other has both integer andirrational roots. Retain complete original-variable root sets.',parts,[RECOGNISE,SOLVE,FILTER],existing=True)

p=roots('original-roots','10*x+sqrt(x)-2','FiniteSet(Rational(4,25))',24,
 'The original domain isx≥0. Setu=√x≥0,so10u²+u−2=(5u−2)(2u+1)=0. Rejectu−1/2before mapping back to x. The validu2/5givesx4/25. The source explicitly tests and rejects the squared imagex1/4ofthat invalid substitution root.')
p['additional_operations']={'substitution_candidates':{'kind':'real-roots','operands':['10*x**2+x-2']},'source_original_checks':{'kind':'identity','operands':['Tuple(10*Rational(4,25)+sqrt(Rational(4,25))-2,10*Rational(1,4)+sqrt(Rational(1,4))-2)']}}
p['additional_operation_expected']={'substitution_candidates':'FiniteSet(-Rational(1,2),Rational(2,5))','source_original_checks':'Tuple(0,1)'}
add('Example',13,24,'Solve10x+√x−2=0. The nonnegative substitution root givesx4/25;the squared image1/4ofits rejected negative substitution root is not a solution.',[p],[RECOGNISE,SOLVE,FILTER],existing=True)

parts=[]
for label,original,key,method in [
 ('a','x-9*sqrt(x)+14','FiniteSet(4,49)','Useu=√x≥0;the quadratic hasu2and7,so both square back to valid roots.'),
 ('b','sqrt(x)*(sqrt(x)+1)-6','FiniteSet(4)','Useu=√x≥0;u²+u−6hasroots2and−3,soonlyu2survives.'),
 ('c','8*x-14*sqrt(x)+5','FiniteSet(Rational(1,4),Rational(25,16))','Useu=√x≥0;factor(4u−5)(2u−1). Both positiveuvalues survive.'),
 ('d','3*sqrt(x)+5/sqrt(x)-16','FiniteSet(Rational(1,9),25)','Originalx>0. Useu=√x>0andmultiply bynonzeroutoget3u²−16u+5=0. Bothu1/3and5are valid.')]:
    parts.append(roots(label,original,key,587,method+' Check every recovered value in the original expression,including denominator conditions.'))
p=v('e','imageset(Lambda(x,x**3),solveset(x**2-2*x-15,x,domain=S.Reals))','FiniteSet(-27,125)',587,
 'The source fractional powers use real cube roots. Setu=realcuberoot(x),which is a bijection on the real line. Then u²−2u−15=0hasu−3and5,and x=u³gives−27and125. Using a principal complex fractional power wouldincorrectly discard the negative original root.')
p['additional_operations']={'original_real_cube_root_checks':{'kind':'identity','operands':['Tuple(real_root(-27,3)**2-2*real_root(-27,3)-15,real_root(125,3)**2-2*real_root(125,3)-15)']}}
p['additional_operation_expected']={'original_real_cube_root_checks':'Tuple(0,0)'};parts.append(p)
p=v('f','imageset(Lambda(x,log(x)/log(3)),solveset(3*x**2-28*x+9,x,domain=Interval.open(0,oo)))','FiniteSet(-1,2)',587,
 'Useu=3^x>0. The quadratic3u²−28u+9hasroots1/3and9;both are admissible. Recoverx−1and2from the positive exponential map. No nonpositiveu may enter a real logarithm.')
p['additional_operations']={'original_exponential_checks':{'kind':'identity','operands':['Tuple(3*(3**(-1))**2-28*(3**(-1))+9,3*(3**2)**2-28*(3**2)+9)']}}
p['additional_operation_expected']={'original_exponential_checks':'Tuple(0,0)'};parts.append(p)
p=v('g','imageset(Lambda(x,real_root(x,3)),solveset(2*x**2-20*x+32,x,domain=S.Reals))','FiniteSet(real_root(2,3),2)',587,
 'Setu=x³,a real bijection. The quadratic2u²−20u+32hasu2and8;their unique real cube roots give x=cuberoot2and2. Do not introduce independent±signs as for square roots.')
p['additional_operations']={'original_polynomial_checks':{'kind':'identity','operands':['Tuple(2*(real_root(2,3))**6-20*(real_root(2,3))**3+32,2*2**6-20*2**3+32)']}}
p['additional_operation_expected']={'original_polynomial_checks':'Tuple(0,0)'};parts.append(p)
p=roots('h','2*(2*x+1/x)**2+5*(2*x+1/x)-3','FiniteSet(-1,-Rational(1,2))',587,
 'Originalx≠0. Setu=2x+1/x;2u²+5u−3=0givesu1/2or−3. Theu1/2branch has no realxbecause2x²−x/2+1has negative discriminant. Theu−3branch gives2x²+3x+1=0andx−1,−1/2,both nonzero andvalid.')
p['additional_operations']={'intermediate_values':{'kind':'real-roots','operands':['2*x**2+5*x-3']},'unattainable_branch_discriminant':{'kind':'identity','operands':['(-Rational(1,2))**2-4*2*1']}}
p['additional_operation_expected']={'intermediate_values':'FiniteSet(-3,Rational(1,2))','unattainable_branch_discriminant':'-Rational(31,4)'};parts.append(p)
add('Try-Now',13,24,'Solve alleight source equations using square-root,real-cube-root,exponential,cubic andnested rational substitutions. Preserve the distinct admissible ranges andall valid original roots;handwritten scan annotations are not treated as publisher instructions.',parts,[RECOGNISE,SOLVE,FILTER],existing=True)

for n,page,label,note,teaches,checks,parent in [
 (22,22,'Original-equation check and squaring warning','The source checks squared candidates5and4in x+√(x−4)=4. Candidate5has residual2andis rejected;4has residual0. Squaring is not an equivalence without sign/domain conditions.',[FILTER],[('Tuple(5+sqrt(5-4)-4,4+sqrt(4-4)-4)','Tuple(2,0)')],'Example:10'),
 (23,23,'Two-stage radical isolation/checks','For√(2y−1)−√(y−4)=2,originaly≥4;the twice-squared candidates5and13both return exactly2on the original LHS. The repeated squaring still requires original checks.',[SOLVE,FILTER],[('Tuple(sqrt(2*5-1)-sqrt(5-4),sqrt(2*13-1)-sqrt(13-4))','Tuple(2,2)')],'Example:11'),
 (24,23,'Quartic-to-quadratic substitution cells','The source setsK=x²andthenreturns to x=±√K. Kcannot be negative for realx;each positive admissibleKhas two preimages.',[RECOGNISE,SOLVE,FILTER],[('expand((x**2-1)*(x**2-4))','x**4-5*x**2+4')],'Example:12'),
 (25,23,'Direct quartic factorisation alternative','(x²−4)(x²−1)=(x−2)(x+2)(x−1)(x+1). This is a valid alternative to substitution forthe same task,not another source problem type.',[SOLVE],[('expand((x-2)*(x+2)*(x-1)*(x+1))','x**4-5*x**2+4')],'Example:12'),
 (26,24,'Nonnegative square-root substitution','K=√xmust satisfyK≥0. SquaringK−1/2to get x1/4doesnot restore a valid K. The source’s final original-equation check correctly rejects that candidate.',[FILTER],[('10*Rational(1,4)+sqrt(Rational(1,4))-2','1')],'Example:13'),
 (27,24,'Quadratic index relationship reminder','The exponent1is twice1/2inthe source10x+x^(1/2)−2. This identifiesK=√xandthe quadratic10K²+K−2,butthe substitution range must remain visible.',[RECOGNISE],[('expand((5*x-2)*(2*x+1))','10*x**2+x-2')],'Example:13')]:
    fig(n,page,label,note,teaches,'table',checks,parent)
for f in figures:
    f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C1:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C1:')if f['parent_item_id']else None
    f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={22:'EveryExample10andbothTryNow10question blocks are recorded. The source’s original-equation substitution checks andwarning about squaring have a teaching record. The direct no-solution bound andnegative validtcase remain distinct.',
 23:'EveryExample11,TryNow11andExample12response recorded. Both stages ofradical squaring andthe quartic substitution/direct-factorisation alternatives have reference records. Original IDsforExample12are retained.',
 24:'EveryTryNow12,Example13andalleightTryNow13responses recorded. Square/cube/exponential/rational substitution domains are explicit. The nonnegative-root andtwice-index reminders have reference records;handwritten annotations are excluded from publisher evidence.'}
pages=[]
for page in range(22,25):
    ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    pages.append({'pdf_page':page,'printed_page':page-11,'chapter':1,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
      'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
      'scope_screen':'Alloriginal responses andteaching blocks enumerated. Domains andsubstitution ranges govern admissible roots;no extra complex roots are requested.'})

if __name__=='__main__':
    for name,data in [('answers-YM-C1-transformed.json',{'scope':'Alloriginal22–24radical/transformed-equation responses,not only the old bounded inventory.','items':answers}),
      ('census-YM-C1-transformed.json',{'book':'YM','book_id':'8227-SRC-017','chapter':1,'source_path':SRC,'source_sha256':SHA,'scope':'Complete22–24page/response census;existingExample12/13andTry12/13IDsretained.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    for row in answers:
        for p in row['subparts']:
            if 'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
            for name,op in p.get('additional_operations',{}).items():
                if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures;',len(pages),'pages')
