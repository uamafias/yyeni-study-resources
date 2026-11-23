"""YM116–118: pointwise operations versus ordered composition and admissibility."""
import json
import author_YM_C3_opening as prior
from author_YM_C3_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent,FUNCTION
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
COMPOSE='8227:2020:M1:T3:O04:D01';ADMISS='8227:2020:M1:T3:O04:D02'

def add(kind,n,page,note,parts,direct):
 r=prior.add(kind,n,page,note,parts,direct)
 r['mapping_rationale']='Pointwise function arithmetic is distinct from composition. Composition outputs use the given inner function as the outer function’s INPUT; solving an input equation retains the actual composite domain. Admissibility is a component guard unless its separate determination is asked.'
 for p in r['subparts']:p['given_representation']='text'
 return r

def val(label,expr,key,kp=599,method=None):return v(label,expr,key,kp,method or'Independently substitute the ORIGINAL function rule(s)and numeric argument,keeping the rightmost function as the first operation. Compare with the separately transcribed key; a product of function values is not composition.')
def extra(p,name,expr,key):
 p.setdefault('additional_operations',{})[name]={'kind':'identity','operands':[expr]};p.setdefault('additional_operation_expected',{})[name]=key;return p

def guard(row,basis):
 row['component_demand_ids']=[ADMISS];row['component_demand_roles']=[{'demand_id':ADMISS,'role':basis}];row['scope_check']['basis']+=' '+basis
 return row
add('Try-Now-6',1,116,'Compute four pointwise operations onf=−2x²−32andg=−3x−4. Native key confirms both negative signs in the sum.',[
 val('a','expand((-2*x**2-32)+(-3*x-4))','-2*x**2-3*x-36'),val('b','expand((-2*x**2-32)*(-3*x-4))','6*x**3+8*x**2+96*x+128'),val('c','(-3*3-4)/(-2*3**2-32)','Rational(13,50)'),val('d','(-3*(-2)-4)-(-2*(-2)**2-32)','42')],[FUNCTION])
r=add('Try-Now-6',2,116,'Evaluate pointwise sums,differences,product andquotient involving a reciprocal functiong=2/x and affineh=x/2−3.',[
 val('a','2/10+10/2-3','Rational(11,5)'),val('b','2/(-8)-((-8)/2-3)','Rational(27,4)'),val('c','expand((2/x)*(x/2-3))','1-6/x'),val('d','(4/2-3)/(2/4)','-2')],[FUNCTION]);r['scope_check']['basis']+=' Originalg requiresx≠0; retain that exclusion even when a product formula simplifies.'
add('Try-Now-6',3,116,'Interpret pointwise scalar combinations and evaluated products/quotients forP=4−x²andQ=2−x. Native key’s linear coefficient in2P+3Qisnegative3.',[
 val('a','expand(-3*(4-x**2))','-12+3*x**2'),val('b','expand(2*(4-x**2)+3*(2-x))','-2*x**2-3*x+14'),val('c','(4-3**2)*(2-(-4))','-30'),val('d','-2*(2-(-1))/(3*(4-3**2))','Rational(2,5)')],[FUNCTION])
r=add('Example',7,116,'Evaluatefg(3)andgf(3)forf=x²andg=3x−2; the numeric answers are correct but one printed nested-function step is wrong.',[
 val('a','(3*3-2)**2','49',116),val('b','3*(3**2)-2','25',116)],[COMPOSE]);r['source_label_warning']='The source writesgf(3)=g(3)^2on one line; it should beg(3²). The right-hand inner/outer calculation and final25are correct. Squaringg(3)would give49instead.'
add('Try-Now-7',1,117,'Evaluate four ordered compositions for quadraticgandaffineh at signed numeric arguments.',[
 val('a','4*(3*2+2)**2-1','255'),val('b','3*(4*(-3)**2-1)+2','107'),val('c','4*(3*(-3)+2)**2-1','195'),val('d','3*(4*5**2-1)+2','299')],[COMPOSE])
add('Try-Now-7',2,117,'Evaluatefg(−3)under four different rule pairs; preserve outer/inner order rather than multiplying outputs.',[
 val('a','((-3)+2)-3','-4'),val('b','3*(-(-3)+6)','27'),val('c','(2*(-3))/2','-3'),val('d','(3*(-3))**2-8','73')],[COMPOSE])
add('Try-Now-7',3,117,'Evaluategf(−4)for two rational-coefficient affine rule pairs,retaining exact fractional values.',[
 val('a','(3*(3*(-4)/5)-2)/2','-Rational(23,5)'),val('b','(3*(-Rational(1,3)*(-(-4)+5))+3)/4','-Rational(3,2)')],[COMPOSE])
add('Example',8,117,'Form both orders of a quadratic/affine composition and a repeated compositiongg; repeated-function notation is iteration,not squaring a value.',[
 val('a','expand(3*(8+2*x-x**2)-1)','-3*x**2+6*x+23',117),val('b','expand(8+2*(3*x-1)-(3*x-1)**2)','-9*x**2+12*x+5',117),val('c','expand(3*(3*x-1)-1)','9*x-4',117)],[COMPOSE])
add('Try-Now-8',1,117,'Form four compositions ofg=2x+5andh=3x²,including both self-compositions.',[
 val('a','expand(3*(2*x+5)**2)','12*x**2+60*x+75'),val('b','expand(2*(3*x**2)+5)','6*x**2+5'),val('c','expand(2*(2*x+5)+5)','4*x+15'),val('d','expand(3*(3*x**2)**2)','27*x**4')],[COMPOSE])
add('Try-Now-8',2,117,'Form both ordersARandRAfor a quadraticAandaffineR; changing order changes the coefficients.',[
 val('a','expand(2+3*(2*x-1)-(2*x-1)**2)','-4*x**2+10*x-2'),val('b','expand(2*(2+3*x-x**2)-1)','-2*x**2+6*x+3')],[COMPOSE])
p=val('x','solveset(6/(x+3)-Rational(3,2),x,domain=S.Reals)','FiniteSet(1)',118,'Originalf(t)=6/(2t+3)requires t≠−3/2,andg(x)=x/2. Thusfg(x)=6/(x+3)requiresx≠−3. Solve the ORIGINAL composite equation and retainx1; do not applyf’s excluded input directly to the raw composite inputx.')
extra(p,'original-solution-check','6/(2*(1/2)+3)-Rational(3,2)','0')
guard(add('Example',9,118,'Solve a reciprocal/affine composite equation,propagating the outer function’s exclusion through the inner input.',[p],[COMPOSE]),'The composite domain excludesx−3,not automaticallyx−3/2.')
p=val('x-values','solveset((3/(x-2))**2+1-5,x,domain=S.Reals)','FiniteSet(Rational(1,2),Rational(7,2))',method='Originalf requiresx≠2. Substitute it into outerg=t²+1,then solve9/(x−2)²+1=5. Both roots1/2and7/2satisfy the original denominator condition.')
guard(add('Try-Now-9',1,118,'Solve a squared reciprocal composite equation andretain both admissible input roots.',[p],[COMPOSE]),'Original/composite input excludesx2.')
p=val('x-values','solveset((2/(x+1)+2)**2-5-11,x,domain=S.Reals)','FiniteSet(0,-Rational(4,3))',method='Originalp requiresx≠−1. Substitute intoq=t²+4t−1=(t+2)²−5,andretain both branches after taking the square root. Inputs0and−4/3satisfy the original composite;−1is excluded.')
guard(add('Try-Now-9',2,118,'Solve a quadratic-of-reciprocal equation with two signed branches,retaining the original pole exclusion.',[p],[COMPOSE]),'Original/composite input excludesx−1.')
p=val('a','expand(2*(2*x-3)-3)','4*x-9',method='Both original functions are declared for input>3. Forx>3,the innerg(x)=2x−3also exceeds3,so gg(x)=4x−9is admissible onthat same domain.')
p2=val('b','Intersection(solveset(1/((2*x-3)**2-9)-Rational(1,7),x,domain=S.Reals),Interval.open(3,oo))','FiniteSet(Rational(7,2))',method='Solve the ORIGINAL composite equation first: roots−1/2and7/2. Both original functions have declared input>3,so only7/2is admissible; natural denominator exclusions alone are not enough.')
extra(p2,'unrestricted-equation-roots','solveset(1/((2*x-3)**2-9)-Rational(1,7),x,domain=S.Reals)','FiniteSet(-Rational(1,2),Rational(7,2))')
guard(add('Try-Now-9',3,118,'Form a self-composition andsolve a separate reciprocal composite under the SAMEexplicitx>3function domains.',[p,p2],[COMPOSE]),'Both original declared domains are(3,∞); inner outputs must also belong to the outer domain.')
p=val('k','solve((x-4+k)-(x+(k-4)/3),k)[0]','4',method='Compose the originalaffine rulesg=3x+kandh=(x−4)/3inbothorders. Equalityasfunctionsrequiresk−4=(k−4)/3,sok4. This is an identity inx,not an equation to solve for one specialx.')
extra(p,'commuting-identity-at-k','expand(3*((x-4)/3)+4-(3*x+4-4)/3)','0')
add('Try-Now-9',4,118,'Determine a constant so two affine compositions agree as functions; special commuting cases do exist.',[p],[COMPOSE])
p3=reasoning('c','Bothfg(x)andgf(x)equalx; each composition acts as the identity.','The original f=3x−2andg=(x+2)/3undo one another in either order. Equality alone is weaker than identity; the displayed algebra establishes both. The next source section names this inverse relationship.',599,'matches')
add('Try-Now-9',5,118,'Form both orders of an inverse affine pair andstate the identity pattern they share.',[
 val('a','expand(3*((x+2)/3)-2)','x'),val('b','expand(((3*x-2)+2)/3)','x'),p3],[COMPOSE])
refs=[
 (27,116,'Composition two-stage function machine','The diagram’s output fromfbecomes the input tog,so gf(x)meansg(f(x)). Flow order is rightmost function first; it is not a product of f(x)andg(x).',[COMPOSE],'diagram',[],None,'teaching-figure'),
 (28,116,'Numeric composition arrow chain','The original illustration usesf=2x+1,g=x²andinput4,so4→9→81. Original input,intermediate output and final output are different values that must stay linked in a variation.',[COMPOSE],'diagram',[('(2*4+1)**2','81')],None,'teaching-figure'),
 (29,116,'Worked numeric nested-function steps','Example7 showsfg(3)=49andgf(3)=25. One source linewritesg(3)^2instead ofg(3²); that incorrect intermediate would produce49andmustnotbeadopted. The correct right-side flow and final25remain valid.',[COMPOSE],'table',[('Tuple((3*3-2)**2,3*(3**2)-2,(3*3-2)**2)','Tuple(49,25,49)')],'Example:7','teaching-figure'),
 (30,117,'Order-of-composition warning','The printed note says composition order usually matters:fgandgfare generally different. Special inverse/commuting pairs can agree; the word generally must not become an absolute prohibition.',[COMPOSE],'table',[],None,'teaching-figure'),
 (31,117,'Substitution arrows and repeated-function convention','Example8’s arrows insert the complete inner expression into every outer-input occurrence. Its explicitg²(x)=gg(x)means repeated composition here; it is distinct from[g(x)]²and must not be silently converted to a pointwise square.',[COMPOSE],'diagram',[('expand(3*(3*x-1)-1)','9*x-4')],'Example:8','teaching-figure'),
 (32,117,'Symbolic argument versus numeric result reminder','The source note distinguishes expressions inxfrom numeric evaluated values. Exact function-operation notation and response expectations must be explicit in later authoring; a scalar and a function formula are different outputs.',[FUNCTION,COMPOSE],'table',[],'Example:8','teaching-figure'),
 (33,118,'Composite reciprocal substitution and admissibility','Example9 substitutesx/2into6/(2t+3),giving6/(x+3),then solvesfg(x)=3/2. The correct composite pole isx−3; the outer function’s own forbidden argument−3/2is not simply a forbidden rawxvalue.',[COMPOSE,ADMISS],'diagram',[('simplify(6/(2*(x/2)+3)-6/(x+3))','0')],'Example:9','teaching-figure')]
for n,page,label,note,teaches,rep,checks,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,checks,parent)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C3:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C3:')if f['parent_item_id']else None
 f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind)
notes={116:'AllTry6Q1–3pointwise outputs,the two composition-flow illustrations andExample7(a/b)are enumerated. Native keys confirm the negative3xcoefficients; those sign suspicions are cleared. Theg(3)^2working step is a verified notation defect despite correct final25.',117:'EveryTry7Q1–3,Example8andTry8Q1/2response,and the printed order/substitution/reminder references are enumerated. g²(x)uses the source’s explicit iteration convention.',118:'EveryExample9andTry9Q1–5output and substitution asset is enumerated. Composition poles,explicitx>3domains,commuting parameter identity and mutual inverse identity are kept distinct.'}
pages=[]
for page in range(116,119):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':pp(page),'chapter':3,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],'scope_screen':'All arithmetic/composition tasks are in scope. Pointwise operations do not create composition coverage. Composite domains depend on inner-input admissibility; no unrelated inverse branch rule is imposed before inverse tasks.'})
if __name__=='__main__':
 for name,data in [('answers-YM-C3-composition.json',{'scope':'Every116–118 explicit response and printed reference.','items':answers}),('census-YM-C3-composition.json',{'book':'YM','book_id':'8227-SRC-017','chapter':3,'source_path':SRC,'source_sha256':SHA,'scope':'Complete116–118 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
