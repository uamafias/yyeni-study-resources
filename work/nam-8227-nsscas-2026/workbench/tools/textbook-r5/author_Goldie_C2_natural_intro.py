"""Every integral-definition activity and reference figure on59–62."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,fig,figures,compute,expression,equivalent
NAT='8227:2020:M2:T2:O02:D01';INV='8227:2020:M2:T2:O02:D02';LAW='8227:2020:M2:T2:O01:D02';DEF='8227:2020:M1:T9:O03:D01';EXPINT='8227:2020:M2:T5:O01:D01'
def ev(page):
 name='Goldie-C2-58'if page<62 else'Goldie-C2-62'if page<335 else'Goldie-key-C2-335'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(kind,n,page,note,parts,direct=None,teaches=None,rep='text',scope=None):
 for p in parts:
  kp=p.pop('key_page_override',338);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
 row={'item_id':f'8227:TB:Goldie:C2:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct or[],'component_demand_ids':[],
  'teaches_8227_demand_ids':teaches or[],'mapping_rationale':'Numerical exploration and integral-based proofs support the natural-log definition. They do not automatically assess a prescribed antiderivative or a formal substitution method. Requested definition interpretation is direct only where warranted.',
  'representation':rep,'sketch_response_required':any(p.get('author_comparison_status')=='sketch'for p in parts),'exam_style':False,'exam_style_basis':'Unattributed boxed prompt or activity.',
  'value_level_scope_decisions':[{'rule_id':'8227:LIMIT07','status':'outside'if kind=='Activity'and n in[5,6]else'not applicable','quoted_value':note,
    'reason':'Formal change-of-variable proofs are extension;retain underlying logarithm/area meaning as supporting evidence.'if kind=='Activity'and n in[5,6]else'Numerical estimates,definition interpretation or a power-rule exception;no unsupplied general substitution is required.'}],
  'precision_angle_check':{'source':'Activity4keys1.099,0.693,1.792;Activity7explicitly2decimal places. Formal identities are exact.','comparison':'Numerical area estimates are approximations;an exact log reference independently checks them. Oriented integrals are required for inputs between0and1,while positive geometric area remains positive.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
 if scope:row['scope_check']=scope
 answers.append(row);return row
p=reasoning('power-rule-exception','The integrand isx^(−1),so n+1=0and the displayed power-rule expression would divide by zero.',
 'The formula∫kx^n dx=kx^(n+1)/(n+1)+Cexplicitly excludesn=−1. A finite positive area still exists on[1,3],because1/xiscontinuous there. Failure of this formula does not mean no antiderivative or no integral exists.',338,'matches')
add('Prompt',3,59,'Explain why the power primitive kx^(n+1)/(n+1)cannot be applied to∫₁³1/x dx:the actual exponent is−1,not a pole inside the interval.',[p],teaches=[EXPINT,DEF])
parts=[]
for label,upper,key in [('i',3,'1.099'),('ii',2,'0.693'),('iii',6,'1.792')]:
 p=value(label,'0',key,338,'Use1000equal-width trapezia on the original continuous reciprocal curve. This is one valid author numerical-area estimate;the source does not require a particular quadrature method or strip count. Compare its final3decimal places to the printed approximate key.')
 p['operation']={'kind':'numeric-trapezium-rule','operands':['1/x','1',str(upper)],'strips':1000,'rounding':{'decimal_places':3}}
 p['additional_operations']={'exact_reference':{'kind':'proper-definite-integral','operands':['1/x','1',str(upper)]}}
 p['additional_operation_expected']={'exact_reference':f'log({upper})'};parts.append(p)
p=reasoning('relationship','The first two areas sum to the third: L(3)+L(2)=L(6).',
 'The numerical sums1.099+0.693=1.792suggest the relation. The independent exact valuesln3+ln2=ln6confirm this particular equality. Three numerical values alone do not prove the later general product law.',338,'matches')
p['additional_operations']={'exact_relation':{'kind':'identity','operands':['log(3)+log(2)-log(6)']}};p['additional_operation_expected']={'exact_relation':'0'};parts.append(p)
add('Activity',4,59,'Numerically estimate∫₁³1/x dx,∫₁²1/x dx,∫₁⁶1/x dxand conjecture their additive relation. No specific numerical method is prescribed.',parts,teaches=[DEF,NAT])
scope={'status':'in-scope-parts-only','basis':'Logarithm and area interpretation are supporting evidence. The formal general substitution proof is outside prescribed integration methods;it is still fully audited internally.','excluded_or_qualified_parts':['ii:formalx=azchange ofvariable','iandiii:conceptual area/log law support,not an additional examination-required proof technique']}
parts=[reasoning('i-diagram','For1<aand1<b,partition the shaded[1,ab]area atx=a;the two pieces areL(a)and∫ₐᵃᵇdx/x.',
 'Drawy=1/xforpositive inputs,mark1,a,abwith1<a<ab,and distinguish the adjacent regions. Additivity of a proper integral givesL(a)+∫ₐᵃᵇdx/x=L(ab). For other positivea,b,the identity still holds using oriented integrals,but the simple adjacent-positive-area drawing needs the stated ordering.',338,'sketch'),
 reasoning('ii-transformed-integral','Withx=azand a>0,dx=adzand the boundsa,abbecome1,b;thus∫ₐᵃᵇdx/x=∫₁ᵇdz/z=L(b).',
 'Both differential and limits change together:1/(az)·a dz=dz/z. The right-hand integrand’s dummy variable name is irrelevant. The formal proof uses general substitution,recorded as extension rather than silently prescribed8227content.',338,'show/prove'),
 reasoning('iii-product-law','L(a)+L(b)=L(ab)forpositivea,b.','Combine(i)and(ii). Positivity keeps every interval away from0. Oriented-integral additivity extends the pictureda>1,b>1case to all positivea,b.',338,'show/prove')]
row=add('Activity',5,60,'Prove the integral-defined logarithm product law using an area partition,a suppliedx=azsubstitution with transformed bounds,and combination of the results. Audit all three subtasks;formal substitution remains extension.',parts,teaches=[NAT,LAW],rep='graph',scope=scope)
row['source_interpretation']={'diagram_order':'The supplied simple shading interpretation needs1<a<ab. Formal identities can extend to other positive inputs using oriented integrals;the distinction is explicit.'}
parts=[value('i','integrate(1/x,(x,1,1))','0',338,'An integral with equal endpoints is zero,soL(1)=0.'),
 reasoning('ii','L(a)−L(b)=L(a/b)forpositivea,b.','By additivity,L(a)−L(b)=∫ᵦᵃdx/x. Letx=bzwithb>0;then this is∫₁ᵃ⁄ᵇdz/z=L(a/b). Equivalently derive from the product law andL(1)=0. The displayed general substitution is extension.',338,'show/prove'),
 reasoning('iii','L(a^n)=nL(a)fora>0and realn,withn=0handled separately.','Forn≠0,usex=z^n on positivez:dx=nz^(n−1)dzand(1/x)dx=n dz/z. Bounds1,a^nbecome1,a,including orientation whenn<0. At n=0both sides are0byL(1)=0;do not invoke an invertiblex=z^0substitution.',338,'show/prove')]
add('Activity',6,60,'EstablishL(1)=0,the quotient law,and the power law for the integral-definedL. Check positivity,oriented bounds and the separate zero-exponent case,without turning general substitution into required syllabus technique.',parts,teaches=[NAT,LAW],scope={'status':'in-scope-parts-only','basis':'Laws/definition support retained;formal integral substitutions are extension.','excluded_or_qualified_parts':['iiandiii:formal general substitution proofs']})
p=value('e-2dp','exp(1)','2.72',338,'The positive reciprocal area is strictly increasing in its upper endpoint. Solving∫₁ᵃdx/x=1therefore defines the uniquee∈(2,3). Independently evaluate the exact solution,then round to2decimal places;the source allows calculator area technology.')
p['operation']={'kind':'rounded','operands':['exp(1)'],'decimal_places':2}
p['additional_operations']={'definition':{'kind':'proper-definite-integral','operands':['1/x','1','exp(1)']},'bracket_area_order':{'kind':'identity','operands':['Tuple(sign(log(2)-1),sign(log(3)-1))']}}
p['additional_operation_expected']={'definition':'1','bracket_area_order':'Tuple(-1,1)'}
add('Activity',7,61,'Use calculator area technology and∫₁ᵉ1/x dx=1,with2<e<3,to finde to2decimal places. The defining root is unique because the integrand is positive.',[p],[NAT])
figures.clear()
for n,page,label,note,teaches,rep,checks,parent in [
 (25,59,'Figure2.11 reciprocal area definition','The shaded region lies under1/xbetween1and3,above thex-axis. It is proper and finite;the pole0is outside the interval. This is an area diagram,not a logarithm curve.',[NAT,DEF],'graph',[], 'Activity:4'),
 (26,59,'Integral-defined product-law conjecture','L(3)+L(2)=L(6)is suggested by three area estimates;the subsequentL(a)+L(b)=L(ab)claim is a conjecture until its general proof. Numerical agreement alone is not proof.',[NAT,LAW],'table',[('log(3)+log(2)-log(6)','0')],None),
 (27,60,'Activity2.5 substitution-limits callout','Originalxlimits area,abare not the transformedzlimits. Fromx=azwitha>0they become1,b;change both differential and bounds. Formal general substitution remains extension.',[NAT],'table',[], 'Activity:5'),
 (28,60,'Logarithm product identity reference','Forpositive arguments andvalidbase,log(a)+log(b)=log(ab). The integral construction motivates the same relationship;it does not establish a new examination frequency.',[LAW],'table',[('log(2)+log(3)-log(6)','0')],None),
 (29,60,'Natural logarithm base-definition reference','Definee>1bythe positive reciprocal area∫₁ᵉ1/x dx=1. General log_p p=1requiresvalidbase;the suppliedp>1discussion fits this positive-area construction.',[NAT],'table',[('integrate(1/x,(x,1,E))','1')],None),
 (30,61,'Figure2.12 unit reciprocal area','The shaded region under1/xfrom1to ehasarea1. The graph’s horizontal coordinateeisbetween2and3;the vertical area value1isnot an ordinate label atx=e.',[NAT],'graph',[], 'Activity:7'),
 (31,61,'Negative natural logs for0<x<1','ln(1/2)=−ln2and positive inputs approaching0have lnxtending−∞. InterpretL(x)=∫₁ˣdt/tas an oriented negative integral,not negative geometric area.',[NAT],'table',[('log(1/2)+log(2)','0')],None),
 (32,62,'Figure2.13 natural logarithm graph','The lncurve has positive-input domain,intercept(1,0),vertical asymptotex=0,increasing concave-down shape and no upper bound. The prose phrase slowest way to infinity is informal;iterated logarithms can grow more slowly.',[NAT,INV],'graph',[('diff(log(x),x)','1/x')],None),
 (33,62,'Figure2.14 natural log/exponential inverses','The exponential and natural logarithm reflect in y=x. Their marked intercepts(0,1),(1,0)are interchanged;the domains/ranges reverse. Preserve the diagonal’s role as reflection line.',[INV],'graph',[],None),
 (34,62,'Natural inverse identities','e^(lnx)=xforx>0;ln(e^x)=xforallrealx. Do not silently transfer the positive-input restriction from the first identity to the second,or remove it from the first.',[NAT,INV],'table',[('exp(log(2))','2'),('log(exp(-2))','-2')],None)]:
 fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C2:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C2:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page'])
 f['value_level_scope_decisions']=[{'rule_id':'8227:LIMIT07','status':'outside'if f['item_number']=='27'else'not applicable','quoted_value':f['notes'],'reason':'Formal general-substitution callout is extension;other figures show proper positive reciprocal areas or basic log/exponential meanings.'}]
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':2,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'All mathematical tasks and teaching figures enumerated;the historical biographical note is prose,not a mathematical question or figure. Formal integral proof extensions remain visible.'}for page in range(59,63)]
if __name__=='__main__':
 for name,data in [('answers-Goldie-C2-natural-intro.json',{'scope':'EveryPrompt3andActivity4–7subtask,including requested graph/relationship/proofs.','items':answers}),('census-Goldie-C2-natural-intro.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete59–62,with source extension boundaries retained.','new_items':figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
