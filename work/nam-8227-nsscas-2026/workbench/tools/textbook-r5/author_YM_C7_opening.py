"""Fixed-source YM322–325 census: integration introduction and rational powers.

The derivative-only illustration is not counted as assessed integration.
Source primitives and source integrands are separate transcriptions.
"""
import hashlib,json
import author_YM_C1_opening as common
from author_YM_C1_opening import W,SRC,SHA,v,reasoning,fig,figures,compute,expression,equivalent,ym_printed_page
from verify_textbook_answers_r5 import primitive_agrees
common.base.answers.clear();common.base.new.clear();figures.clear()
answers=common.base.answers;new=common.base.new;corrections=[]
REV='8227:2020:M1:T9:O01:D01';INT='8227:2020:M1:T9:O01:D02';DERIV='8227:2020:M1:T8:O02:D01'
def pp(page):return ym_printed_page(page)
def ev(page):
 name='YM-C7-key-625'if page>=625 else f'YM-C7-{322+4*((page-322)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png'
 return dict(path=str(p.relative_to(W.parents[2])),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
common.base.ev=ev
def extra(p,name,expr,key):
 p.setdefault('additional_operations',{})[name]={'kind':'identity','operands':[expr]};p.setdefault('additional_operation_expected',{})[name]=key
 return p
def integral(label,f,key,kp,reverse=False,domain=None,source_variable='x'):
 p=v(label,'0',key,kp,'Integrate the ORIGINAL integrand after a valid power/index rearrangement. Compare with the separately transcribed printed primitive by differentiating it; an arbitrary additive constant is required on each connected real component. Preserve the original domain, including denominator exclusions. For a source variable t the checker consistently renames t to x; constants are not renamed.')
 p.update(operation={'kind':'real-elementary-antiderivative','operands':[f]},answer_equivalence='up-to-additive-constant',original_integrand=f,source_variable=source_variable,normalised_variable='x',response_format='symbolic',given_representation='text',assessed_8227_demand_ids=[INT,REV]if reverse else[INT],
  original_domain=domain or 'Where the original integrand is real and finite; an indefinite primitive is asserted on each open connected component, not across excluded zeros.',author_answer_form='The primitive plus an arbitrary real constant on each original real-domain component.')
 return p
def add(kind,n,page,note,parts,direct=None,components=None,new_item=False,powers=None):
 direct=direct if direct is not None else sorted({d for p in parts for d in p.get('assessed_8227_demand_ids',[])})
 r=common.add(kind,n,page,note,parts,direct,components or[])
 r['item_id']=r['item_id'].replace(':YM:C1:',':YM:C7:');meta=new.pop();meta['item_id']=r['item_id']
 r.update(component_demand_ids=components or[],representation='text',sketch_response_required=False,
  mapping_rationale='The requested result determines direct coverage: a derivative-only task assesses differentiation; reverse recognition is explicit when recovering y/f from a given derivative. An arbitrary integration constant is not the demand to EVALUATE that constant from an initial condition.',
  scope_check={'status':'in-scope','basis':note,'excluded_or_qualified_parts':[],'limits_considered':['8227:QUAL05'],'qualifier_applicability_note':'Actual rational integration powers and original real domains recorded; the n=−1 power exception is retained. No general substitution method is required.'},
  value_level_scope_decisions=[dict(rule_id='8227:QUAL05',status='within'if powers else'not applicable',quoted_value=', '.join(powers)if powers else note,reason='Actual integration exponents are rational and none is−1. Even roots retain their nonnegative real radicands; reciprocal roots exclude zero.'if powers else'This source task differentiates rather than integrates; it does not count as assessed integration coverage.')],
  precision_angle_check={'source':'Exact symbolic answers and arbitrary constants; no angle or rounding requirement in this segment.','comparison':'Equivalent real primitives are compared up to additive constants only on their original connected domains. Source preferences about double fractions do not create an official marking restriction.'})
 for p in parts:p.setdefault('response_format','symbolic');p.setdefault('given_representation','text')
 if new_item:
  meta.update(item_kind='worked-illustration'if kind=='Worked-illustration'else'exercise',scope_check=r['scope_check'],value_level_scope_decisions=r['value_level_scope_decisions'],mapping_rationale=r['mapping_rationale']);new.append(meta)
 else:corrections.append(dict(item_id=r['item_id'],pdf_page=page,printed_page=pp(page)))
 return r

p=integral('y','4*x**3','x**4',323,True)
p.update(printed_key_normalised='4*x**3',author_expected_normalised='x**4',source_interpretation='The early reverse-arrow illustration correctly gives x⁴. The later concluding sentence instead prints family y=4x³+c;this wrong family is independently transcribed and compared,not silently corrected.')
add('Worked-illustration',1,323,'Unnumbered reverse-differentiation prompt: given dy/dx=4x³,recover y=x⁴+c. The arrow illustration is correct,but the concluding prose prints the wrong family4x³+c (native verified).',[p],new_item=True,powers=['3'])
ps=[]
for label,f in [('a','x**4+3'),('b','x**4-7'),('c','x**4+50')]:
 p=v(label,f'diff({f},x)','4*x**3',323,'Differentiate the actual polynomial, including its additive constant. The equal derivatives explain the integration constant, but this explicit requested calculation is differentiation.')
 p.update(assessed_8227_demand_ids=[DERIV],original_function=f);ps.append(p)
add('Worked-illustration',2,323,'The three explicit differentiatethese prompts have originals x⁴+3,x⁴−7,x⁴+50. Each derivative is4x³; this is assessed differentiation in an integration teaching context.',ps,[DERIV],new_item=True)
add('Example',1,324,'Recover y from dy/dx=x⁵ and dy/dx=1/x³; add an arbitrary constant and retain x≠0 for the reciprocal original.',[
 integral('a','x**5','x**6/6',324,True),integral('b','1/x**3','-1/(2*x**2)',324,True,domain='x≠0; independent constants on x<0 and x>0.')],powers=['5','−3'])
add('Try-Now',1,325,'Recover y from the three given derivatives x⁷,1/x⁶,x^−8, not from an already supplied primitive.',[
 integral('a','x**7','x**8/8',625,True),integral('b','1/x**6','-1/(5*x**5)',625,True),integral('c','x**(-8)','-1/(7*x**7)',625,True)],powers=['7','−6','−8'])
add('Example',2,325,'Integrate 1/√x,x^(2/3),x²√x by rewriting the actual rational powers; the last integrand has power5/2.',[
 integral('a','1/sqrt(x)','2*sqrt(x)',325,domain='x>0.'),integral('b','x**Rational(2,3)','Rational(3,5)*x**Rational(5,3)',325,domain='Real cube-root powers on all real x. Negative branch primitive=−(3/5)(−x)^(5/3).'),integral('c','x**2*sqrt(x)','Rational(2,7)*x**Rational(7,2)',325,domain='x≥0; primitive on x>0 with continuous extension to0.')],powers=['−1/2','2/3','5/2'])
extra(answers[-1]['subparts'][1],'real-negative-branch','simplify(diff(-Rational(3,5)*(-x)**Rational(5,3),x)-(-x)**Rational(2,3))','0')
ps=[integral('a','x**(-Rational(1,3))','Rational(3,2)*x**Rational(2,3)',625,domain='x≠0, real cube-root convention. For x<0 primitive=(3/2)(−x)^(2/3).'),integral('b','x**Rational(1,3)','Rational(3,4)*x**Rational(4,3)',625,domain='All real x using the real cube root. For x<0 primitive=(3/4)(−x)^(4/3).'),integral('c','x**(-Rational(1,5))','Rational(5,4)*x**Rational(4,5)',625,domain='x≠0, real fifth-root convention. For x<0 primitive=(5/4)(−x)^(4/5).'),integral('d','x**(-Rational(1,4))','Rational(4,3)*x**Rational(3,4)',625,domain='x>0.'),integral('e','x*sqrt(x)','Rational(2,5)*x**Rational(5,2)',625,domain='x≥0, open primitive component x>0.'),integral('f','x**Rational(1,4)/x','4*x**Rational(1,4)',625,domain='ORIGINAL fourth root divided by x requires x>0, even though the printed primitive extends to0.')]
extra(ps[0],'real-negative-branch','simplify(diff(Rational(3,2)*(-x)**Rational(2,3),x)+(-x)**(-Rational(1,3)))','0')
extra(ps[1],'real-negative-branch','simplify(diff(Rational(3,4)*(-x)**Rational(4,3),x)+(-x)**Rational(1,3))','0')
extra(ps[2],'real-negative-branch','simplify(diff(Rational(5,4)*(-x)**Rational(4,5),x)+(-x)**(-Rational(1,5)))','0')
add('Try-Now',2,325,'Six exact rational-power integrals, including real odd roots on negative components and the original fourth-root quotient that excludes0.',ps,powers=['−1/3','1/3','−1/5','−1/4','3/2','−3/4'])

refs=[(1,323,'Reverse-derivative arrow panel','y=x⁴ differentiates to4x³. Reversing recovers x⁴+c,not a uniquely determined curve. The subsequent explicit derivative prompts are separately recorded.',[REV],'diagram',[('diff(x**4,x)','4*x**3')]),(2,324,'Power integration and arbitrary-constant reference','∫xⁿdx=x^(n+1)/(n+1)+c with rationaln≠−1,on appropriate real domains. Illustration ∫x³dx=x⁴/4+c. Introductory prose says integratex⁴ while displaying4x³; keep that source typo visible.',[INT,REV],'table',[('diff(x**4/4,x)','x**3')]),(3,325,'Constant-multiple and constant-term reference','For constantk,∫kf=k∫f. Illustration∫5x³dx=5x⁴/4+c. A constant TERM k instead integrates to kx+c; it is not left unchanged.',[INT],'table',[('diff(5*x**4/4,x)','5*x**3'),('diff(k*x,x)','k')])]
for n,page,label,note,teaches,rep,checks in refs:
 fig(n,page,label,note,teaches,rep,checks,None);r=figures[-1];r.update(item_id=f'8227:TB:YM:C7:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure')
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=7,page_status='prose only'if page==322 else'items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='All explicit opening prompts,Examples1–2,Try1–2 and rule/arrow panels enumerated. Page322 is title/scope/biographical decoration,with no new mathematical task. A decorative mention of mean-value theorem does not add syllabus scope.',scope_screen='Rational-power integration excluding n−1. The three derivative-only prompts do not count as integration practice. No initial-condition task occurs yet.')for page in range(322,326)]
def save(stem,scope):
 for name,data in [(f'answers-YM-C7-{stem}.json',dict(scope=scope,items=answers)),(f'census-YM-C7-{stem}.json',dict(book='YM',book_id='8227-SRC-017',chapter=7,source_path=SRC,source_sha256=SHA,scope=scope,new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);expected=expression(p.get('author_expected_normalised',p['printed_key_normalised']))
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():
    got=compute(op)
    # Supplementary component calculations may supply evidence without a
    # separately printed component key. Compare when an independent target
    # is transcribed;the primary requested-answer assertion always runs above.
    if name in p.get('additional_operation_expected',{}):assert equivalent(got,expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save('opening','Complete rendered322–325opening census; all explicit outputs independently derived and key compared.')
