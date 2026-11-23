"""Rendered source census198–203: retain useful scope inside further calculus.

Mandatory general-substitution methods remain explicit extensions. These fixed
source checks are neither recipe authoring nor a runtime question generator.
"""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,fig,figures,compute,expression,equivalent
from verify_textbook_answers_r5 import primitive_agrees
AREA='8227:2020:M1:T9:O04:D01';DEF='8227:2020:M1:T9:O03:D01';POWER='8227:2020:M1:T9:O01:D01';CHAIN='8227:2020:M1:T8:O02:D02'
def ev(page):
 name=f'Goldie-scope-{196+4*((page-196)//4)}' if page<350 else 'Goldie-keys-C8-350'if page<354 else'Goldie-C8-summary-key354-source'
 p=W/f'checks/r5/textbooks/{name}.png'
 return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];new=[]
def add(kind,n,page,note,parts,direct=None,components=None,teaches=None,forced=False,continuation=None,rep='text',qualifier=None,exam_attribution=None,precision_note=None):
 direct=direct or[];components=components or[]
 for p in parts:
  kp=p.pop('key_page_override',page)
  p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
 decisions=[{'rule_id':'8227:LIMIT07','status':'outside' if forced else 'not applicable','quoted_value':note,
  'parts':['required source method'] if forced else [],'reason':'The original requires a general substitution. Audit its mathematical result as supporting/boundary evidence without claiming that this mandatory method is prescribed.' if forced else 'A geometric shift,proper area or conceptual discussion does not mandate selecting a general integration substitution.'}]
 if qualifier:decisions.append({'rule_id':'8227:QUAL05','status':'within','quoted_value':qualifier,'reason':'These rational powers are not−1. Their direct/expanded integration is prescribed mathematically;any extra source method condition is recorded separately.'})
 scope={'status':'in-scope-parts-only' if forced else 'in-scope','basis':note,'excluded_or_qualified_parts':['Mandatory general substitution is additional;only underlying mathematical content is retained as supporting evidence.'] if forced else []}
 row={'item_id':f'8227:TB:Goldie:C8:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components,'teaches_8227_demand_ids':teaches or[],
  'mapping_rationale':'The explicit learner output is direct only when within prescribed scope. Unnumbered illustrations,photographs and results with an extra mandatory method stay supporting evidence. A method used incidentally inside an excluded inverse-trig task does not create direct coverage.',
  'evidence_role':'directly related assessed practice' if direct else 'prerequisite/supporting context or boundary-method evidence;no direct8227coverage claimed',
  'representation':rep,'sketch_response_required':False,'exam_style':bool(exam_attribution),'exam_style_basis':('The textbook prints this examination attribution: '+exam_attribution+'. It was checked on the textbook render;the primary paper was not read here.')if exam_attribution else'Unattributed prompt,illustration or worked example.',
  'value_level_scope_decisions':decisions,'scope_check':scope,
  'precision_angle_check':{'source':precision_note or'The retained symbolic results are exact unless an individual response records a printed approximation. No unstated rounding or physical unit is imposed.',
   'comparison':'Retain original domains and consistent bounds/units. Additive-constant equivalence applies only to indefinite primitives on stated real components;it never changes a fixed-point curve or definite value.'},
  'expected_subpart_labels':[p['subpart'] for p in parts],'subparts':parts}
 if continuation:row['continuation_pdf_pages']=continuation
 answers.append(row)
 new.append({'item_id':row['item_id'],'item_kind':'boxed-prompt' if kind=='Prompt' else 'worked-illustration' if kind=='Worked-illustration' else 'activity' if kind=='Activity' else 'exercise' if kind.startswith('Exercise') else 'worked-example',
  'exercise':kind,'item_number':str(n),'pdf_page':page,'printed_page':page-14,'continuation_pdf_pages':continuation or[],'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components,'teaches_8227_demand_ids':teaches or[],
  'source_evidence':ev(page),'learner_display':False,'scope_check':scope,'evidence_role':row['evidence_role'],'representation':rep,'exam_style':row['exam_style'],'exam_style_basis':row['exam_style_basis'],
  'answer_key':{'available':True,'pdf_pages':sorted({p['answer_pdf_page'] for p in parts}),'printed_pages':sorted({p['answer_printed_page'] for p in parts}),'locator':'Each exact inline/answer-section source page is recorded per response.'}})
 return row
p=reasoning('estimate-method','Define a finite piece of the wave,measure a representative cross-section,choose a profile model,and integrate its cross-sectional area;multiply by along-crest width only under a stated constant-section approximation.',
 'The following source prose suggests a sine-wave profile and integration. A photograph alone gives no metric scale,boundary plane or along-crest extent,so it does not determine a numerical volume. This supports mathematical modelling discussion,not a coordinate-axis volume-of-revolution task. A crest-only volume and a signed area relative to mean water level are different quantities.',198,'matches')
add('Prompt',1,198,'Discuss how to estimate water volume in a sea wave from an illustrative photograph. The source suggests a sine profile but supplies no metric scale or finite region definition.',[p],teaches=[AREA],rep='diagram')
p=reasoning('shifted-area','The shaded area under y=√(x+1),0≤x≤3,is the same as∫₁⁴√u du;its independently derived value is14/3.',
 'Translate the known y=√xgraph left by1. The shaded endpoint pair0,3therefore corresponds to1,4on the original graph. This is the exact comparison printed in the answer section. Equivalently subtract the original area0..1from0..4;no general substitution technique is necessary.',350,'matches')
p['additional_operations']={'shifted_original_area':{'kind':'proper-definite-integral','operands':['sqrt(x+1)','0','3']},'comparison_area':{'kind':'proper-definite-integral','operands':['sqrt(x)','1','4']}}
p['additional_operation_expected']={'shifted_original_area':'14/3','comparison_area':'14/3'}
add('Prompt',2,200,'Use the graph y=√xto explain the shaded area under y=√(x+1)between0and3. Preserve the horizontal-shifted bounds1and4of the comparison graph.',[p],[AREA],[DEF],rep='graph',qualifier='√(x+1)=(x+1)^(1/2);comparison√x=x^(1/2).')
p=value('area','0','16/3',201,'The original integrand√(x−1)is continuous on[1,5],including its finite zero endpoint. Direct linear-power integration gives(2/3)(x−1)^(3/2);endpoint evaluation gives16/3. The source introduces a substitution as an alternative method,not a reason to discard this prescribed integral.')
p['operation']={'kind':'proper-definite-integral','operands':['sqrt(x-1)','1','5']}
add('Worked-illustration',1,200,'The unnumbered Figure8.3illustration evaluates the shaded area∫₁⁵√(x−1)dx. It can be integrated directly;the following worked substitution is an extra teaching method.',[p],teaches=[AREA,DEF,POWER],continuation=[201],rep='graph',qualifier='(x−1)^(1/2),bounds1and5.')
p=value('integral','0','60',202,'Independently integrate the original polynomial/linear power on[1,3]. Its primitive(x+1)^4/4gives(4^4−2^4)/4=60. The source additionally requires a suitable substitution;that enforced method is outside prescribed requirements even though the mathematical integral is ordinary.')
p['operation']={'kind':'proper-definite-integral','operands':['(x+1)**3','1','3']}
add('Example',2,201,'Evaluate∫₁³(x+1)^3dxby making a suitable substitution. Underlying linear-power integration is prescribed,but the source’s enforced general-method condition is retained as additional.',[p],teaches=[DEF,POWER],forced=True,continuation=[202],qualifier='(x+1)^3with exponent3andbounds1,3.')
p=reasoning('reverse-chain-explanation','Yes:the chain rule differentiates F(u(x))asF′(u(x))u′(x),and reversing that identity gives the corresponding substitution relationship on valid domains.',
 'Use the chain rule as a derivative identity,not informal cancellation of arbitrary fractions. Recovering F(u(x))by differentiation checks the primitive. General method selection is still outside prescribed8227scope;the conceptual relation is supporting explanation,not a new required technique.',351,'matches')
add('Prompt',3,202,'Explain whether integration by substitution can be viewed as the reverse of the chain rule. The general-method discussion remains supporting conceptual evidence.',[p],teaches=[CHAIN])
p=value('primitive','0','(x**2+2)**4/8',203,'Independently expandx(x²+2)³=x^7+6x^5+12x³+8xand integrate termwise. The CASprimitive isx^8/8+x^6+3x^4+4x²,which differs from the printed compact primitive by the constant2. Both derivatives equal the original integrand. The source’s mandatory substitution remains an extra method.')
p['operation']={'kind':'real-elementary-antiderivative','operands':['x*(x**2+2)**3']};p['answer_equivalence']='up-to-additive-constant';p['author_answer_form']='(x²+2)^4/8+C,all realx;equivalently the expanded primitive plus an arbitrary constant.'
add('Example',4,203,'Find∫x(x²+2)^3dxby a suitable substitution. Polynomial expansion gives an in-scope mathematical route,but does not meet that additional original method instruction.',[p],teaches=[POWER],forced=True,qualifier='Expanded powersx^7,6x^5,12x³,8x;all exponents positive integers.')
p=value('primitive','0','2*(3*x+4)*(x-2)**(3/2)/15',203,'Independently rewrite x=(x−2)+2,sox√(x−2)=(x−2)^(3/2)+2(x−2)^(1/2). Directly integrate both linear powers and factor the result. The real primitive is checked onx>2and extends continuously tox=2. The source requires substitution;record that extra condition instead of silently changing the task.')
p['operation']={'kind':'real-elementary-antiderivative','operands':['x*sqrt(x-2)'],'integration_algorithm':'manual'};p['answer_equivalence']='up-to-additive-constant';p['author_answer_form']='(2/15)(3x+4)(x−2)^(3/2)+C,on the open real componentx>2.'
add('Example',5,203,'Find∫x√(x−2)dxby a suitable substitution. Its algebraic rewrite into two linear powers is prescribed mathematics;the forced substitution remains additional.',[p],teaches=[POWER],forced=True,qualifier='(x−2)^(3/2)+2(x−2)^(1/2),realinteriorx>2.')
figures.clear()
for n,page,label,note,teaches,rep,checks,parent in [
 (1,198,'Sea-wave context photograph','An illustrative sea wave has no metric scale or finite along-crest extent. It motivates cross-sectional modelling;it does not fix a numerical volume or demonstrate a volume of revolution.',[AREA],'diagram',[], 'Prompt:1'),
 (2,200,'Figure8.1 square-root graph','The basic y=√xcurve has domainx≥0and points(0,0),(1,1),(4,2). Its drawn viewport ending near4is not the function’s full domain.',[POWER,AREA],'graph',[('Tuple(sqrt(0),sqrt(1),sqrt(4))','Tuple(0,1,2)')],None),
 (3,200,'Figure8.2 shifted square-root area','y=√(x+1)has full real domainx≥−1,but the shaded area uses0≤x≤3and endpoint heights1and2. The reference area on√xisbetween1and4.',[AREA],'graph',[('Tuple(sqrt(0+1),sqrt(3+1))','Tuple(1,2)')], 'Prompt:2'),
 (4,200,'Figure8.3 right-shifted square-root area','y=√(x−1)has real domainx≥1and the shaded region1≤x≤5has endpoint heights0and2. The lower endpoint is a finite zero,not an integrand pole.',[AREA,DEF],'graph',[('Tuple(sqrt(1-1),sqrt(5-1))','Tuple(0,2)')], 'Worked-illustration:1'),
 (5,201,'Differential-notation warning','The source explainsdu=dxas notation within its change-of-variable argument,not arbitrary cancellation of fractions. This is method-boundary exposition,not an additional required8227technique.',[],'table',[],None),
 (6,202,'Figure8.4 cubic area','The curve y=(x+1)^3has root−1and intercept1;the shaded region is1≤x≤3with area60. The qualitative sketch has no numerical vertical scale to infer extra givens.',[AREA,DEF],'graph',[('Tuple(((-1)+1)**3,(0+1)**3)','Tuple(0,1)')], 'Example:2'),
 (7,202,'Example3 derivative-matching note','The extra-method example uses2xas the derivative ofx²−4inside its nonlinear root. The derivative relation is correct;it does not make the whole mandatory-substitution task prescribed.',[CHAIN],'table',[('diff(x**2-4,x)','2*x')],None),
 (8,203,'Example4 half-factor callout','Foru=x²+2,the original measurexdxisone half ofdu. The displayed factor1/2is required;omitting it would double the primitive derivative.',[CHAIN],'table',[('diff(x**2+2,x)/2','x')], 'Example:4'),
 (9,203,'Return-to-original-variable reminder','An indefinite primitive requested as a function ofxmust ultimately be expressed inx,even when a temporary variable was used. The chosen general substitution method remains extension.',[],'table',[],None)]:fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C8:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C8:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page'])
 f['value_level_scope_decisions']=[{'rule_id':'8227:LIMIT07','status':'outside'if f['item_number']in['5','7','8','9']else'not applicable','quoted_value':f['notes'],'reason':'The referenced general-method exposition is extension;the retained figure relation is supporting evidence,not an automatic directly assessed demand.'}]
pages=[]
notes={198:'The opening wave prompt/photo is retained. Example8.1inverse-tan differentiation is excluded;its incidental implicit-differentiation method does not create direct coverage.',
 199:'Example8.1continuation,its inverse-trig derivative reference and8A1–5are outside prescribed derivatives. No retained item starts here.',
 200:'8A6–7are inverse-trig derivative/tangent tasks,outside scope. All three relevant square-root figures,the area-shift prompt and unnumbered illustration are recorded.',
 201:'Square-root illustration continues;differential notation warning and Example2are recorded with their method boundary.',
 202:'Example2continues;Figure8.4and reverse-chain prompt retained. Example3requires a nonlinear-root general substitution;its derivative-matching note is retained separately,not its whole task as prescribed.',
 203:'Examples4and5have prescribed mathematical alternatives but explicitly enforce extra substitution methods. Both results and their warnings/callouts are retained as boundary evidence.'}
for page in range(198,204):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 continuation=['8227:TB:Goldie:C8:Worked-illustration:1']if page==201 else['8227:TB:Goldie:C8:Example:2']if page==202 else[]
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':8,'page_status':'items enumerated'if ids else'scope-screened; no in-scope item starts','item_ids':ids,'continuation_item_ids':continuation,'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],'scope_screen':'Full rendered-page boundary read;the reason for every excluded group remains explicit.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C8-opening.json',{'scope':'Every retained198–203task or supporting mathematical result,with mandatory-method distinctions.','items':answers}),('census-Goldie-C8-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':8,'source_path':SRC,'source_sha256':SHA,'scope':'Complete198–203scope/item census;inverse-trig derivative tasks excluded with reasons.','new_items':new+figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);expected=expression(p['printed_key_normalised'])
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
