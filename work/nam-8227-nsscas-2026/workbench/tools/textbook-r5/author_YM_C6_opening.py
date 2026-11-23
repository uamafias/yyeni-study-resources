"""YM266–273 source analysis: gradient investigation and power derivatives.

No runtime generator; question functions and printed answers are transcribed
separately from the rendered book. Optional first-principles exposition stays
outside the required proof scope.
"""
import hashlib,json
import author_YM_C1_opening as common
from author_YM_C1_opening import W,SRC,SHA,v,reasoning,fig,figures,compute,expression,equivalent
common.base.answers.clear();common.base.new.clear();figures.clear()
answers=common.base.answers;new=common.base.new;corrections=[]
GRAD='8227:2020:M1:T8:O01:D01';NOTATION='8227:2020:M1:T8:O01:D02';POWER='8227:2020:M1:T8:O02:D01'
def pp(page):return 'A'+str(page-586)if page>=587 else page-12
def ev(page):
 name=('YM-C6-keys-618-source'if page<=621 else'YM-C6-keys-622-source')if page>=618 else f'YM-C6-{266+4*((page-266)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return dict(path=str(p.relative_to(W.parents[2])),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
common.base.ev=ev
def add(kind,n,page,note,parts,direct,components=None,new_item=False,powers=None):
 missing=[p for p in parts if p.get('key_page_override')is None]
 for p in missing:p['key_page_override']=page
 r=common.add(kind,n,page,note,parts,direct,components or[]);  r['item_id']=r['item_id'].replace(':YM:C1:',':YM:C6:');meta=new.pop();meta['item_id']=r['item_id']
 r.update(representation='text',sketch_response_required=kind=='Investigation',component_demand_ids=components or[],
  mapping_rationale='Interpret gradient as the limit of chord slopes and retain derivative notation separately from calculating rational-power derivatives. Fraction/index rearrangements are components,not an assessed product/quotient-rule demand. First-principles proof is explicitly optional underLIMIT03.')
 r['scope_check']={'status':'in-scope-parts-only'if kind=='Worked-derivation'else'in-scope','basis':note,'excluded_or_qualified_parts':['First-principles proof is not required']if kind=='Worked-derivation'else[],
  'limits_considered':['8227:LIMIT03','8227:QUAL10'],'qualifier_applicability_note':'Prescribed rational powers only; retain original real domains and denominator exclusions. Source claim any real power is broader than the qualification. The investigation interprets slopes; it does not mandate a formal first-principles proof.'}
 r['value_level_scope_decisions']=[dict(rule_id='8227:QUAL10',status='within'if powers else'not applicable',quoted_value=', '.join(powers)if powers else note,reason='All actual derivative exponents are rational,including negative,fractional andzero powers; preserve real-function domains.'if powers else'No power-rule differentiation response is required by this item.'),dict(rule_id='8227:LIMIT03',status='outside'if kind=='Worked-derivation'else'not applicable',quoted_value=note,reason='Optional textbook first-principles proof; no direct assessed8227demand is claimed.'if kind=='Worked-derivation'else'Graphical slope interpretation or rule-based differentiation,not a required first-principles proof.')]
 r['precision_angle_check']={'source':'Exact symbolic derivatives. The investigation screenshot has measured ratio5.01; its suggested exact pointB(3,9)gives5. No angle units or requested decimal rounding.','comparison':'Keep exact rational exponents and algebraic equivalents. Do not mistake source style advice about negative exponents/double fractions for an official marking restriction. Even-root derivatives require positive interior x; reciprocal functions exclude0.'}
 for p in missing:p.update(answer_pdf_page=None,answer_printed_page=None,key_evidence=ev(625),key_presence='no separate key',inspected_key_pdf_pages=list(range(618,626)))
 for p in parts:p.setdefault('response_format','symbolic');p.setdefault('given_representation',r['representation'])
 if new_item:
  meta.update(scope_check=r['scope_check'],mapping_rationale=r['mapping_rationale'],component_demand_ids=components or[],value_level_scope_decisions=r['value_level_scope_decisions']);new.append(meta)
 else:corrections.append(dict(item_id=r['item_id'],pdf_page=page,printed_page=pp(page),continuation_pdf_pages=[269]if kind=='Investigation'else[]))
 if not direct:r['evidence_role']='prerequisite/supporting optional exposition; not direct syllabus demand coverage.'
 return r
def extra(p,name,expr,key):
 p.setdefault('additional_operations',{})[name]={'kind':'identity','operands':[expr]};p.setdefault('additional_operation_expected',{})[name]=key;return p
def deriv(label,fn,key,kp,domain='All real x where the original function is differentiable.'):
 p=v(label,f'diff({fn},x)',key,kp,'Differentiate the ORIGINAL function after rewriting its rational powers or separating each numerator term over the original denominator. Treat named parameters as constants. Compare the independently transcribed printed expression by algebraic equivalence,retaining the ORIGINAL domain. '+domain)
 p.update(assessed_8227_demand_ids=[POWER],original_function=fn,real_domain=domain)
 extra(p,'derivative-consistency',f'simplify(diff({fn},x)-({key}))','0')
 return p

ps=[]
for label,conclusion,method in[
 ('a','Graph y=x² with vertex(0,0),even symmetry,and A(2,4).','Read the original upward parabola and mark A exactly. Its shape/axes/point must agree; the named Sketchpad interface is not needed to establish the mathematical graph.'),
 ('b','For suggested B(3,9),the chordAB is y=5x−6.','B is to the RIGHT ofA and lies on the ORIGINAL curve. Joining(2,4),(3,9)gives slope5 and intercept−6. Any other chosen B requires its own slope.'),
 ('c','For B(3,9),C=(3,4),with AC horizontal andBC vertical.','Construct the right-angle component triangle atC. Its geometric lengths areAC1,BC5; their ratio is slope5 for this rightward choice.')]:
 p=reasoning(label,conclusion,method,268,'sketch');p.update(assessed_8227_demand_ids=[GRAD],response_format='sketch',credited_features=conclusion);ps.append(p)
p=v('d','(3**2-2**2)/(3-2)','5',268,'For the exact suggested B(3,9),subtract ORIGINAL coordinates to compute5. The source screenshot instead shows measured BC6.55cm/AC1.31cm≈5.01 for a nearby dragged point; those display measurements are not an exact numerical key for B=(3,9).')
p.update(assessed_8227_demand_ids=[GRAD],comparison_note='Comparison is with the exact source point suggestion,not a claim that the screenshot prints the exact value5.');ps.append(p)
p=reasoning('e-f','As B approachesA from the right,the chord gradient approaches4.','Write B=(2+h,(2+h)²)withh>0. The exact slope is4+h and tends to4 as h tends to0. Dragging is the source procedure; the mathematical output is the limiting slope,not proof that the GUI was operated.',269,'matches');p['assessed_8227_demand_ids']=[GRAD];extra(p,'right-limit','limit(((2+a)**2-4)/a,a,0,dir="+")','4');ps.append(p)
p=reasoning('g','Starting with B(1,1),the chord slope is3 and approaches4 from below.','For leftwardB,use signed coordinate differences:((1−4)/(1−2))=3. With B=(2+h,(2+h)²),h<0,the slope4+h tends to4. Positive side lengths alone hide the sign unless the common coordinate orientation is retained.',269,'matches');p['assessed_8227_demand_ids']=[GRAD];extra(p,'left-start-and-limit','Tuple((1-4)/(1-2),limit(((2+a)**2-4)/a,a,0,dir="-"))','Tuple(3,4)');ps.append(p)
p=reasoning('Question1','Gradient4 at(2,5)on y=x²+1.','A vertical translation changes every ordinate by the same1,so it cancels from every chord difference. The limiting slope atx2remains4. No separately headed investigation answer occurs in the inspected chapter6key pages; this requested extension is author-derived.',None,'no key');p.update(assessed_8227_demand_ids=[GRAD],inspected_key_pdf_pages=list(range(618,626)),key_presence='no separate key');extra(p,'translated-gradient','diff(x**2+1,x).subs(x,2)','4');ps.append(p)
r=add('Investigation',1,268,'Interpret right/left chord slopes on y=x²nearA(2,4),including all graph/triangle tasksa–g and the translated-curveQuestion1. Dragging instructions are procedural context; exact limits do not depend on a branded GUI.',ps,[GRAD])
r['sketch_response_required']=True
p=reasoning('derivation','For y=x²,the chord slope2x+h tends to2x.','Original A=(x,x²),B=(x+h,(x+h)²),h≠0. Expand the numerator,divide by the NONZERO increment,and only then take its limit0. Do not substituteh0into the original0/0quotient. The source introductory point(x,x+h)is a label typo; the displayed derivation uses the correct points.',269,'show/prove');extra(p,'chord-slope','simplify(((x+a)**2-x**2)/a)','2*x+a');extra(p,'limit','limit(2*x+a,a,0)','2*x')
add('Worked-derivation',1,269,'Optional first-principles exposition for y=x²,with correct A(x,x²),B(x+h,(x+h)²)and nonzeroh. The technique is not a prescribed proof underLIMIT03.',[p],[],[GRAD],new_item=True)
add('Example',1,271,'Differentiate five originals: integer power6,fraction3/2,square root,constant2,and reciprocalx. Preserve domains instead of requiring a single display notation.',[
 deriv('a','x**6','6*x**5',271),deriv('b','x**Rational(3,2)','Rational(3,2)*sqrt(x)',271,'Real originalx>=0;the ordinary two-sided derivative formula is used forx>0. At0a finite right derivative0exists,but that endpoint convention is separate.'),deriv('c','sqrt(x)','1/(2*sqrt(x))',271,'Real originalx>=0;finite derivative onlyx>0.'),deriv('d','2','0',271),deriv('e','1/x','-1/x**2',271,'Original and derivative requirex≠0.')],[POWER],powers=['6','3/2','1/2','0','−1'])
data=[('a','x**8','8*x**7'),('b','-x**5','-5*x**4'),('c','x**Rational(3,2)','Rational(3,2)*sqrt(x)'),('d','1','0'),('e','-8','0'),('f','x**(-Rational(4,5))','-Rational(4,5)*x**(-Rational(9,5))'),('g','x**Rational(5,2)','Rational(5,2)*x**Rational(3,2)'),('h','x**(-7)','-7*x**(-8)'),('i','5','0'),('j','x**Rational(1,3)','Rational(1,3)*x**(-Rational(2,3))'),('k','x**(-Rational(2,3))','-Rational(2,3)*x**(-Rational(5,3))'),('l','x**12','12*x**11')]
ps=[deriv(label,fn,key,618,'Even-root powers use realx>=0and interiorx>0;negative powers exclude0. Odd-root fractional powers use the REAL odd root on either side of0,not a principal complex power. Zero/endpoint differentiability must be considered separately.')for label,fn,key in data]
# On the negative half-line these two fractional powers are positive powers of -x.
extra(ps[5],'negative-real-branch','diff((-x)**(-Rational(4,5)),x).subs(x,-32)','Rational(1,640)')
extra(ps[9],'negative-real-branch','diff(-(-x)**Rational(1,3),x).subs(x,-8)','Rational(1,12)')
extra(ps[10],'negative-real-branch','diff((-x)**(-Rational(2,3)),x).subs(x,-8)','Rational(1,48)')
add('Try-Now',1,271,'Differentiate all12original monomials/constants,including−4/5,5/2,cube-root and reciprocal-cube-square exponents. Native source and key confirm the negative−4/5coefficient.',ps,[POWER],powers=['8','5','3/2','0','−4/5','5/2','−7','1/3','−2/3','12'])
add('Example',2,272,'Differentiate2x³−8x+7term by term;the constant contributes0.',[deriv('derivative','2*x**3-8*x+7','6*x**2-8',272)],[POWER],powers=['3','1','0'])
add('Try-Now',2,272,'Differentiate four given polynomials,retaining negative linear terms and zero constant derivatives.',[deriv('a','3*x**2-8','6*x',618),deriv('b','4*x**3-2*x**2+4','12*x**2-4*x',618),deriv('c','5*x**2-x+1','10*x-1',618),deriv('d','7-3*x+5*x**2','-3+10*x',618)],[POWER],powers=['3','2','1','0'])
add('Example',3,273,'Rewrite reciprocal/radical/quotient expressions before using the rational-power sum rule. a is a constant. No product/quotient method is required.',[deriv('a','-4/(9*x**3)+a*x','4/(3*x**4)+a',273,'Originalx≠0;parameter aconstant.'),deriv('b','3*x**5-4*x/sqrt(x)','15*x**4-2/sqrt(x)',273,'Original denominator sqrtx requiresx>0.'),deriv('c','(x**2-3)/x','1+3/x**2',273,'Originalx≠0is retained after simplification.')],[POWER],powers=['−3','1','5','1/2','−1'])
add('Try-Now-3',1,273,'Differentiate four original rational-power sums after termwise simplification,without inventing a quotient-rule requirement.',[
 deriv('a','5*x**4+2/x-1/x**2','20*x**3-2/x**2+2/x**3',618,'Originalx≠0.'),deriv('b','Rational(7,4)*x**4+5/(3*x**4)+x','7*x**3-Rational(20,3)*x**(-5)+1',618,'Originalx≠0.'),deriv('c','4*x**(-8)+x/sqrt(x)','-32*x**(-9)+1/(2*sqrt(x))',618,'Originalx>0.'),deriv('d','(7+6*x-5*x**2)/x**2','-14/x**3-6/x**2',618,'Originalx≠0.')],[POWER],powers=['4','−1','−2','−4','1','−8','1/2','0'])
add('Try-Now-3',2,273,'Differentiate a polynomial quotient reducible to powers,and a sum containing square,cube and fifth roots. Preserve real domains of the ORIGINAL expressions.',[
 deriv('a','(3*x+2*x**2-4*x**4)/(4*x**2)','-3/(4*x**2)-2*x',618,'Originalx≠0.'),deriv('b','sqrt(x)+7*x**Rational(7,3)-x**(-Rational(2,5))','1/(2*sqrt(x))+Rational(49,3)*x**Rational(4,3)+Rational(2,5)*x**(-Rational(7,5))',618,'The combined ORIGINAL square-root and reciprocal term domain isx>0;odd-root negative branches of isolated terms do not extend the whole expression.')],[POWER],powers=['−1','0','2','1/2','7/3','−2/5'])

refs=[
 (1,267,'Straight-line gradient triangle','A(x1,y1),B(x2,y2),C(x2,y1);gradient(y2−y1)/(x2−x1),withx2≠x1. Vertical lines do not have a finite gradient.',[GRAD],'diagram',[],None),
 (2,267,'Tangent to y=−x²+x+2','The source tangent atA(1,2)is y=−x+3,slope−1;intercepts0,3and3,0agree with the rendered line.',[GRAD],'graph',[('diff(-x**2+x+2,x).subs(x,1)','-1')],None),
 (3,268,'Investigation graph and measured chord','Original parabola y=x²,A(2,4),rightwardBnear(3,9),component triangleABC. Screenshot ratio5.01is a measured display,not an exact coordinate key for suggestedB3.',[GRAD],'graph',[],'Investigation:1'),
 (4,269,'Chord-to-tangent derivation diagram','A(x,f(x)),B(x+h,f(x+h));horizontal incrementh,vertical differencef(x+h)−f(x). Both curve labels and nonzerohare required before a limit.',[GRAD],'graph',[],'Worked-derivation:1'),
 (5,269,'Gradient at A(2,4)from2x','The derived gradient2xgives4atx2. This source inline illustration supports interpretation;it is not another numbered exercise.',[GRAD],'table',[('2*2','4')],None),
 (6,270,'Derivative notation reference','Leibniz dy/dx,d/dx(x²),and Lagrange fprime(x)represent the derivative2x. Derivative notation is not ordinary cancellation of standalone numbers.',[NOTATION],'table',[('diff(x**2,x)','2*x')],None),
 (7,270,'Power rule with worked illustration','Source states realn;8227requires rationaln. On appropriate real domains,d(x^n)/dx=n*x^(n−1). Examplex⁴gives4x³. Source mnemonic uses exponent reduction,not differentiation of the coefficient.',[POWER],'table',[('diff(x**4,x)','4*x**3')],None),
 (8,271,'Derivative answer-form guidance','The book allows surd or fractional-index forms and discourages double-fraction layouts. This is source presentation advice,not a verified NSSCAS marking prohibition. Constant derivative0andreciprocal derivative−1/x²are checked inExample1.',[POWER],'table',[],'Example:1'),
 (9,272,'Constant multiple reference','k is constant in differentiation ofkf(x);example4x³gives12x². It would not apply with a variablek(x)without an extra product term.',[POWER],'table',[('diff(4*x**3,x)','12*x**2')],None),
 (10,272,'Sum and difference reference','Differentiate each term;examplex⁴+x³−x²gives4x³+3x²−2x. Preserve all original minus signs.',[POWER],'table',[('diff(x**4+x**3-x**2,x)','4*x**3+3*x**2-2*x')],None)]
for n,page,label,note,teaches,rep,checks,parent in refs:
 fig(n,page,label,note,teaches,rep,checks,parent);r=figures[-1]
 r['item_id']=r['item_id'].replace('Goldie:C5:','YM:C6:');r['parent_item_id']=r['parent_item_id'].replace('Goldie:C5:','YM:C6:')if r['parent_item_id']else None
 r.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[])
 r['item_kind']='teaching-figure'
 r['mathematical_feature_review']['method']='Inspect original graph labels,tangent/chord incidence and exact functions. Recompute displayed slopes/derivatives from originals. A screenshot measurement or source GUI instruction is not a formal limit proof or evidence that the app was operated.'
pages=[]
for page in range(266,274):
 pages.append(dict(pdf_page=page,printed_page=pp(page),chapter=6,page_status='prose only'if page==266 else'items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=['8227:TB:YM:C6:Investigation:1']if page==269 else[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='Title/scope/photo266has no mathematical task. All opening gradient graphs,Investigationa–g/Question1,optional derivation,notation/rule illustrations,Examples1–3,Try1/2andTry3Q1/2are enumerated across266–273. GUI/video instructions are context,not extra mathematical responses.',scope_screen='Rational-power rule and curve-gradient interpretation are prescribed. Optional first-principles proof is outside requiredLIMIT03scope. Source any-real-power statement doesnotextend the prescribed rational-exponent scope.'))
if __name__=='__main__':
 for name,data in [('answers-YM-C6-opening.json',dict(scope='All266–273explicit tasks and optional derivation.',items=answers)),('census-YM-C6-opening.json',dict(book='YM',book_id='8227-SRC-017',chapter=6,source_path=SRC,source_sha256=SHA,scope='Complete266–273page census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
