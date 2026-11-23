"""YM529–531: exponential primitives, proper integrals and convergent infinite bound.
Fixed-source author evidence only; independently transcribed originals and source keys.
"""
import hashlib,json
import author_YM_C7_opening as h
from author_YM_C7_opening import W,SRC,SHA,pp,v,reasoning,fig,figures,extra,compute,expression,equivalent,integral
from author_Goldie_C5_opening import definite
from verify_textbook_answers_r5 import primitive_agrees
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
EXP='8227:2020:M2:T5:O01:D01';DEF='8227:2020:M1:T9:O03:D01';LOG='8227:2020:M2:T2:O02:D01'
def ev(page):
 name='YM-C11-key-649'if 649<=page<=652 else'YM-C11-528-source'if 529<=page<=531 else f'YM-C12-{532+4*((page-532)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return dict(path=str(p.relative_to(W.parents[2])),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
h.common.base.ev=ev
_source_figure=fig
def fig(*args,**kwargs):
 result=_source_figure(*args,**kwargs)
 figures[-1]['mathematical_feature_review'].update(date='2026-11-20',reviewer='Codex author; independent acceptance pending')
 return result

def add(kind,n,page,note,parts):
 direct=sorted({d for p in parts for d in p.get('assessed_8227_demand_ids',[])})
 comp=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-set(direct))
 r=h.add(kind,n,page,note,parts,direct,comp)
 for part in parts:part['review_date']='2026-11-20'
 r['item_id']=r['item_id'].replace(':YM:C7:',':YM:C12:');corrections[-1]['item_id']=r['item_id']
 r.update(mapping_rationale='Exponential integration is directly assessed from the original integrand. Finite bound evaluation is additionally direct where requested. Deducing the infinite-bound value retains convergence. A requested rearranged logarithmic relation is not an unasked numerical root; integration and logarithmic inverse relation remain distinct.',value_level_scope_decisions=[dict(rule_id='8227:LIMIT07',status='within',quoted_value=note,reason='The actual elementary forms,identities,bounds and conditions are recorded in this item and its parts. No selection of a general integration substitution is prescribed;any internal CAS coordinate is author QA only.'),dict(rule_id='8227:QUAL04',status='within'if any(p.get('improper_integral')for p in parts)else'not applicable',quoted_value='; '.join(str(p.get('original_integrand'))+' on '+str(p.get('original_bounds'))for p in parts if p.get('improper_integral'))if any(p.get('improper_integral')for p in parts)else note,reason='The actual integrand and exceptional bounds are quoted here. Its parts independently establish convergence by finite-bound or separate endpoint limits;no principal-value cancellation is used.'if any(p.get('improper_integral')for p in parts)else'No valid improper-integral exemplar is prescribed here. Any diagnosed internal-pole source defect is separately excluded;finite endpoints alone do not prove continuity.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:LIMIT07','8227:QUAL04']),precision_angle_check=dict(source='Exact primitives,integrals or stated relations unless a part or this item explicitly records source precision: '+note,comparison='Keep arbitrary constants and original domains. Use exact internal values,then the source precision recorded per part. A rounded key display is distinguished from an explicit source requirement;angle units follow the actual item.'))
 return r

def primitive(label,f,key,kp):
 p=integral(label,f,key,kp,domain='All real x; exponential is positive and finite at every finite real argument. Independent additive constant required.')
 p.update(assessed_8227_demand_ids=[EXP],author_method='Independently integrate the separately transcribed original affine exponential,divide by its nonzero inner coefficient,and differentiate the separately transcribed key on the original domain. Expand the quotient in Try1(d)before integrating.')
 return p

def dv(label,f,lo,hi,key,kp):
 p=definite(label,f,lo,hi,key,kp);p.update(assessed_8227_demand_ids=[EXP,DEF],component_demand_ids=[],given_representation='text',response_format='numeric',original_integrand=f,original_bounds=[str(lo),str(hi)]);return p

def val(label,expr,key,kp,method,direct=None):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct if direct is not None else[EXP,DEF],component_demand_ids=[],given_representation='text',response_format='symbolic');return p
add('Example',1,530,'Three indefinite exponential integrals:e^(4x),e^(−7x/2),10e^(5−2x). Negative inner coefficients require negative primitive factors;all constants retained.',[primitive('a','exp(4*x)','exp(4*x)/4',530),primitive('b','exp(-7*x/2)','-2*exp(-7*x/2)/7',530),primitive('c','10*exp(5-2*x)','-5*exp(5-2*x)',530)])
add('Try-Now',1,530,'Four indefinite exponential integrals,including rational inner coefficient4/3,negative factor−6,and quotient(9+e^(2x))/e^(2x)=1+9e^(−2x).',[primitive('a','exp(7*x)','exp(7*x)/7',650),primitive('b','exp(4*x/3)','3*exp(4*x/3)/4',650),primitive('c','-6*exp(2-3*x)','2*exp(2-3*x)',650),primitive('d','(9+exp(2*x))/exp(2*x)','x-9*exp(-2*x)/2',650)])
add('Example',2,530,'Two proper finite integrals:e^(−3x)on[0,2]and5e^(2x)on[0,ln2]. Both endpoints use the same primitive;second exact answer15/2.',[dv('a','exp(-3*x)',0,2,'Rational(1,3)-exp(-6)/3',530),dv('b','5*exp(2*x)',0,'log(2)','Rational(15,2)',530)])
add('Try-Now-2',1,531,'Evaluate three finite exponential integrals. Part(c)requires expanding(e^x−e^(3x))²,retaining the negative middle term−2e^(4x).',[dv('a','exp(-4*x)',0,'Rational(1,2)','Rational(1,4)-exp(-2)/4',650),dv('b','2/exp(3*x-2)',0,1,'2*exp(2)/3-2/(3*exp(1))',650),dv('c','(exp(x)-exp(3*x))**2',0,2,'exp(4)/2-exp(8)/2+exp(12)/6-Rational(1,6)',650)])
p=dv('shown-integral','(exp(x)+1)**2',0,1,'exp(2)/2+2*exp(1)-Rational(3,2)',531);p.update(check_mode='show/prove',response_format='proof/show-that',required_method='Expand original square and evaluate both endpoints;the supplied target alone is not evidence.')
add('Try-Now-2',2,531,'SHOW the finite integral of(e^x+1)²on[0,1]equals e²/2+2e−3/2. Preserve derivation rather than accepting the given target as working.',[p])
add('Try-Now-2',3,531,'Find EXACT0..1 integral3e^(1−2x). Exact result3e/2−3/(2e),not a decimal replacement.',[dv('exact-value','3*exp(1-2*x)',0,1,'3*exp(1)/2-3/(2*exp(1))',650)])
p=val('a','integrate(exp(-x)+6*exp(-3*x),(x,0,a))','3-exp(-a)-2*exp(-3*a)',650,'Originala>0. Integrate the ORIGINAL two decaying exponentials and subtract the lower value−3. Parameter is a finite positive bound;no convergence claim yet.')
p.update(original_integrand='exp(-x)+6*exp(-3*x)',original_bounds=['0','a'],original_parameter_domain='a>0')
p['additional_operations']={'concrete-finite-a2':{'kind':'proper-definite-integral','operands':['exp(-x)+6*exp(-3*x)','0','2']}};p['additional_operation_expected']={'concrete-finite-a2':'3-exp(-2)-2*exp(-6)'}
q=val('b','limit(3-exp(-a)-2*exp(-3*a),a,oo)','3',650,'Use the finite-bound expression from(a),then take a→+infinity. Both decaying terms tend0;the improper integral converges to3. A bare infinity endpoint substitution without the limit is insufficient.')
q.update(improper_integral=True,original_integrand='exp(-x)+6*exp(-3*x)',original_bounds=['0','oo'],depends_on_source_parts=['a'],response_format='numeric');extra(q,'independent-improper-integral','integrate(exp(-x)+6*exp(-3*x),(x,0,oo))','3')
add('Try-Now-2',4,531,'Positive finite bounda:(a)integrate e^(−x)+6e^(−3x)from0toa;(b)DEDUCE the infinite-bound integral3 using convergence of the exponential tail.',[p,q])

def relation(kind,n,note,f,lo,hi,total,integral_result,target,kp,derivation,check):
 p=reasoning('shown-relation',target,derivation,kp,'show/prove');p.update(assessed_8227_demand_ids=[EXP,DEF,LOG],component_demand_ids=[],given_representation='text',response_format='proof/show-that',original_integrand=f,original_bounds=[lo,hi],original_integral_value=str(total),original_parameter_domain='a>0;all logarithm arguments must be positive under the original integral constraint.')
 extra(p,'original-integral','integrate('+f+', (x,'+lo+','+hi+'))',integral_result)
 extra(p,'rearrangement-equivalence',check,'0')
 return add(kind,n,531,note,[p])
relation('Example',3,'Original∫−a..a(4e^(2x)+5)=100witha>0;SHOWa=(1/2)ln(50+e^(−2a)−5a),not a numeric root.','4*exp(2*x)+5','-a','a',100,'2*exp(2*a)-2*exp(-2*a)+10*a','a=log(50+exp(-2*a)-5*a)/2',531,'Independent integral2e^(2a)−2e^(−2a)+10a=100. Rearrange e^(2a)=50+e^(−2a)−5a;right side is positive because it equals the positive exponential. Taking ln gives the requested relation.','(2*exp(2*a)-2*exp(-2*a)+10*a-100)-2*(exp(2*a)-(50+exp(-2*a)-5*a))')
relation('Try-Now-3',1,'Original∫−a..2a4e^(−2x)=25witha>0;SHOWa=(1/2)ln(12.5+e^(−4a)).','4*exp(-2*x)','-a','2*a',25,'2*exp(2*a)-2*exp(-4*a)','a=log(Rational(25,2)+exp(-4*a))/2',531,'Evaluate the ORIGINAL endpoints:2e^(2a)−2e^(−4a)=25. Thus e^(2a)=25/2+e^(−4a)>0 and ln gives2a. No numerical answer is requested.','(2*exp(2*a)-2*exp(-4*a)-25)-2*(exp(2*a)-(Rational(25,2)+exp(-4*a)))')
relation('Try-Now-3',2,'Original∫0..a(1+e^(x/2))²=10,a>0;SHOWa=2ln[(15−a)/(4+e^(a/2))].','(1+exp(x/2))**2','0','a',10,'a+4*exp(a/2)+exp(a)-5','a=2*log((15-a)/(4+exp(a/2)))',531,'Expand original square and integrate: a+4e^(a/2)+e^a−5=10. Set z=e^(a/2)>0,so z(z+4)=15−a>0. Divide by positivez+4 and take ln. This uses the original constraint to justify the logarithm domain.','(a+4*exp(a/2)+exp(a)-15)-(exp(a/2)*(exp(a/2)+4)-(15-a))')
p=val('a','2*log(1+835/(8*exp(3)))','Rational(73,20)',650,'ORIGINALintegral8e³(e^(a/2)−1)=835. Solve the positive exponential for a exactly,then round ONCE to3significant figures3.65. Monotonicity of this integral for a>0 proves the positive solution unique.')
p.update(operation=dict(kind='rounded',operands=['2*log(1+835/(8*exp(3)))'],significant_figures=3),requested_precision='3 significant figures',original_integrand='4*exp(x/2+3)',original_bounds=['0','a'])
extra(p,'original-integral','integrate(4*exp(x/2+3),(x,0,a))','8*exp(3)*(exp(a/2)-1)');extra(p,'unrounded-original-equation','simplify((8*exp(3)*(exp(a/2)-1)-835).subs(a,2*log(1+835/(8*exp(3)))))','0')
add('Try-Now-3',3,531,'Given0..a integral4e^(x/2+3)=835,a>0,finda3sf3.65. Keep the independently solved exactinternalvalue and test the original integral equation.',[p])
refs=[(1,530,'Exponential integration rule','∫e^x=e^x+C;∫e^(ax+b)=e^(ax+b)/a+C fornonzeroa. Ifa0,the integrandconstant e^b instead integratesxe^b+C. No divisionby0.',EXP,None),(2,530,'Example1(a) working','Innercoefficient4requires1/4.',EXP,'Example:1'),(3,530,'Example1(b) working','Innercoefficient−7/2requires−2/7;nativeexponentchecked.',EXP,'Example:1'),(4,530,'Example1(c) working','Originalfactor10andinner−2givemultiplier−5.',EXP,'Example:1'),(5,530,'Example2(a) endpoint evaluation','Primitive−e^(−3x)/3at2and0gives1/3−1/(3e^6).',DEF,'Example:2'),(6,530,'Example2(b) endpoint evaluation','Primitive5e^(2x)/2and e^(2ln2)=4give15/2.',DEF,'Example:2'),(7,530,'Same integration constant cancellation reminder','The SAME primitiveconstantcancelswhenendpointsareevaluatedinonecontinuousdomain.',DEF,'Example:2'),(8,531,'Example3 parameter relation derivation','Symmetricboundsproduce2(e^(2a)−e^(−2a))+10a=100. Rearrangeandjustifypositiveexponentialbeforetakingln.',LOG,'Example:3')]
for n,page,label,note,d,parent in refs:
 fig(n,page,label,note,[d],'table',[],parent);figures[-1].update(item_id=f'8227:TB:YM:C12:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C12:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Read the actual exponential exponents/signs,finite bounds,solution panels and constant-cancellation reminder. Independently differentiate all primitive keys,integrate finite originals,and check the actual infinite-bound convergence in Try2Q4(b). These are teaching/working panels,not given diagrams.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=12,page_status='prose only'if page==529 else'items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='Title/scope/biography529hasno mathematicaltask. AllExamples1–3,Try1,Try2Q1–4,Try3Q1–3andactualrule/working/reminderpanelsenumerated. No unasked numericalrootaddedtoSHOWrelations.',scope_screen='Affineexponentialintegrationandproperendpointwork;Try2Q4(b)actualsimpleconvergentimproperintegral. No general substitution selection.')for page in range(529,532)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:
    got=compute(p['operation']);expected=expression(p.get('author_expected_normalised',p['printed_key_normalised']))
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(row['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C12-opening.json',dict(scope='Complete529–531exponentialopening;20requestedresponses.',items=answers)),('census-YM-C12-opening.json',dict(book='YM',book_id='8227-SRC-017',chapter=12,source_path=SRC,source_sha256=SHA,scope='Complete529–531page/item/panelcensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
