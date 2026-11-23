"""Every Example2–5 and Activity2.2response;all reference blocks on43–45."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,compute,expression,equivalent
LOGIND='8227:2020:M2:T2:O01:D01';LOGLAW='8227:2020:M2:T2:O01:D02';EXPEQ='8227:2020:M2:T2:O03:D01';EXPI='8227:2020:M2:T2:O03:D02';GP='8227:2020:M1:T2:O03:D02';MODEL='8227:2020:M1:T2:O03:D03';QUADRATIC='8227:PRIOR:NSSCO:quadratic'
def ev(page):
 name='Goldie-C2-42'if page<335 else'Goldie-key-C2-335'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(kind,n,page,note,parts,direct,components=None,teaches=None):
 for p in parts:
  kp=p.pop('key_page_override',page);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
 row={'item_id':f'8227:TB:Goldie:C2:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],'teaches_8227_demand_ids':teaches or[],
  'mapping_rationale':'Definition evaluation,log laws,solving an exponential equation,positive substitution admissibility and a discrete GPthreshold require different decisions. External scale conventions are not silently treated as syllabus facts.',
  'representation':'text','sketch_response_required':False,'exam_style':False,'exam_style_basis':'Unattributed worked example or activity.',
  'value_level_scope_decisions':[{'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,
   'reason':'Evaluating known powers uses the log definition. Taking a fixed common logarithm on both sides of an exponential equation uses the power law;it does not require memorising a general change-of-base formula. CASnumeric normalisation is not an extra learner method.'}],
  'precision_angle_check':{'source':'Examples3/4print3significant figures;Example5requires an integer index and strict threshold. Activity2.2gives approximate scale relationships without a complete supplied model for every context.',
   'comparison':'Retain exact roots and admissibility before rounding. A near-integer threshold must follow the strict inequality,not automatic nearest-integer rounding.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row);return row
parts=[]
for label,arg,key in [('i-a','64','6'),('i-b','1/2','-1'),('i-c','1','0'),('i-d','sqrt(2)','1/2')]:
 p=value(label,f'log({arg},2)',key,43,'Recognise the original argument as an exact power of2. The normalised CASlog ratio is internal arithmetic,not a requested change-of-base derivation.');parts.append(p)
p=value('ii','2**log(64,2)','64',43,'The inverse definition gives2^(log₂64)=64for the positive argument. This is a stated-result check rather than a new numerical instance.');p['check_mode']='show/prove';parts.append(p)
add('Example',2,43,'Find base2logarithms of64,½,1,√2;then show2^(log₂64)=64. Exact index recognition precedes any numerical calculator method.',parts,[LOGIND])
p=value('solution','log(1000)/log(2)','9.97',44,'Take common logs of both sides of2^n=1000to getnlog10(2)=log10(1000). Solve the resulting linear equation in realn,and round only the final value to3significant figures.')
p['operation']={'kind':'rounded','operands':['solve(2**x-1000,x)[0]'],'significant_figures':3}
p['additional_operations']={'exact_substitution':{'kind':'identity','operands':['exp((log(1000)/log(2))*log(2))']}}
p['additional_operation_expected']={'exact_substitution':'1000'}
add('Example',3,44,'Solve2^n=1000for realn,displayed to3significant figures. Unlike a first-whole-day threshold,nneed not be an integer.',[p],[EXPEQ],[LOGLAW])
p=value('root','0','1.46',45,'Sety=3^x>0. Independently solve the correct quadraticy²+2y−15=(y−3)(y+5)=0,discardy=−5,and obtainx=1. The printed solution factorises the wrong sign pattern and reports1.46.')
p['operation']={'kind':'rounded','operands':['solve(3**(2*x)+2*3**x-15,x)[0]'],'significant_figures':3}
p['expected_source_key_status']='key wrong';p['author_answer_form']='x=1exactly.'
p['additional_operations']={'correct_y_roots':{'kind':'identity','operands':['FiniteSet(*solve(y**2+2*y-15,y))']},'original_at_correct_root':{'kind':'identity','operands':['(3**(2*x)+2*3**x-15).subs(x,1)']},'printed_factorisation_discrepancy':{'kind':'identity','operands':['expand((y-5)*(y+3))-(y**2+2*y-15)']},'printed_positive_y_residual':{'kind':'identity','operands':['(y**2+2*y-15).subs(y,5)']}}
p['additional_operation_expected']={'correct_y_roots':'FiniteSet(-5,3)','original_at_correct_root':'0','printed_factorisation_discrepancy':'-4*y','printed_positive_y_residual':'20'}
add('Example',4,45,'Solve3^(2x)+2·3^x−15=0using a positive exponential substitution. The worked solution’s factorisation and final root are wrong;the correct unique real root is1.',[p],[EXPEQ],[QUADRATIC])
p=value('k','floor(log(500000/(1/5))/log(5))+2','11',45,'The kthterm is(1/5)5^(k−1). For strict greater-than,ktakes the first integer beyond1+log₅(2500000). Use floor plus the correct offset;do not merely round the logarithmic bound.')
p['additional_operations']={'adjacent_terms':{'kind':'identity','operands':['Tuple((1/5)*5**9,(1/5)*5**10)']}}
p['additional_operation_expected']={'adjacent_terms':'Tuple(390625,1953125)'}
add('Example',5,45,'The GP0.2,1,5,…has its first term greater than500000at indexk. Solve the strict threshold and check the previous/current terms;indexing starts atk=1.',[p],[GP,MODEL,EXPI],[LOGLAW])
p=reasoning('i','Under the book’s intended base-ten scale convention,the higher reading represents10times the measured quantity.',
 'A difference of1in a base-ten logarithmic scale multiplies the specified underlying quantity by10. The activity calls it Richterintensitywithout defining the physical quantity here. Treat the book’s factor10as conditional on that intended convention;do not silently equate amplitude,intensity and released energy. A purpose-authored question must supply or cite its model.',336,'matches')
p['additional_operations']={'conditional_base_ten_ratio':{'kind':'identity','operands':['10**(8-7)']}}
p['additional_operation_expected']={'conditional_base_ten_ratio':'10'}
p2=reasoning('ii','MiddleC’s frequency is half that of theCabove;equivalently,the upperCis twice the lower.',
 'The exact octave-doubling rule is supplied in the preceding2A6material. State which ratio is meant:the source key’s½is lower/upper,not upper/lower. No external tuning table is needed for this relationship.',336,'matches')
p2['additional_operations']={'lower_to_upper':{'kind':'identity','operands':['262/(2*262)']}}
p2['additional_operation_expected']={'lower_to_upper':'1/2'}
p3=reasoning('iii','If the intended level model isL=10log10(I/I₀),thenI₈₆/I₈₅=10^0.1≈1.26.',
 'Subtract the two stated model equations to get1=10log10(I₈₆/I₈₅),then invert the logarithm. The formula is the assumption required for the key’s1.26;this activity does not print it. A different measured quantity or coefficient would change the ratio,so retain this as conditional context evidence rather than an independently verified physical definition.',336,'matches')
p3['additional_operations']={'conditional_ratio_3sf':{'kind':'rounded','operands':['10**(1/10)'],'significant_figures':3}}
p3['additional_operation_expected']={'conditional_ratio_3sf':'1.26'}
row=add('Activity',2,43,'Discuss one-step changes on Richter,octave and decibel scales. Explain ratio orientation and the assumed underlying model;only octave doubling is explicitly supplied in nearby source material.',[p,p2,p3],[],teaches=[LOGIND])
row['evidence_role']='prerequisite/supporting external-scale context discussion;no direct8227demand coverage'
row['scope_check']={'status':'in-scope-parts-only','basis':'Conditional logarithmic arithmetic is relevant,but the activity assumes external scale definitions. It is not evidence that learners must recall those physical conventions.','excluded_or_qualified_parts':['iandiii:underlying physical model/quantity needs supplied or verified definition','ii:nearby octave rule supplies the relation']}
row['source_interpretation']={'external_context_assumptions':'Mathematical relationships are checked conditionally on explicitly recorded models. This is not certification of a global Richter/decibel physical definition.','future_use':'Supply the mathematical relation in a purpose-authored problem or verify an exact primary definition before using context recall as an assessed demand.'}
from author_Goldie_C5_opening import fig,figures
figures.clear()
for n,page,label,note,checks,parent in [
 (7,43,'Inverse logarithm identity and common-log reference','Forvalidbasea>0,a≠1andx>0,a^(log_a x)=x. The base10reference lists1000↦3,100↦2,10↦1,1↦0,0.1↦−1,0.01↦−2. The pHsentence is illustrative context,not a posed chemistry assessment.',[(f'log({arg},10)',key)for arg,key in [('1000','3'),('100','2'),('10','1'),('1','0'),('1/10','-1'),('1/100','-2')]],None),
 (8,44,'Logarithm product-law reference','Forpositive arguments and valid common base,log_a(xy)=log_a x+log_a y. The source derives it from multiplying the corresponding powers;it is not a change-of-base formula.',[('log(8,2)','log(2,2)+log(4,2)')],None),
 (9,44,'Logarithm quotient-law reference','Forx,y>0andvalidbasea,log_a(x/y)=log_a x−log_a y. Original positivity restrictions remain even if algebraically simplifying a later expression.',[('log(8/4,2)','log(8,2)-log(4,2)')],None),
 (10,44,'Logarithm of one reference','Foranyvalidbasea,log_a1=0becausea^0=1. Base1isnot an admissible logarithm base.',[('log(1,3)','0')],None),
 (11,44,'Logarithm power-law reference','Forx>0andvalidbasea,log_a(x^n)=nlog_a xon its stated real domain. The multiplication explanation begins with integern;extension to other real exponents retains positive realx.',[('log(16,2)','4*log(2,2)')],None),
 (12,45,'Example4 exponential substitution callout','The correct callout states3^(2x)=(3^x)²and shows the substitution into the quadratic. The later factorisation is wrong;do not reject this valid representation identity along with it.', [('3**(2*x)-(3**x)**2','0')],'Example:4'),
 (13,45,'Example4 positivity callout','3^xisalwayspositive,so a negative substituted variable cannot correspond to a realx. The printed negative candidate−3isfrom the wrong factorisation;the correct discarded root is−5.', [('3**0','1')],'Example:4')]:
 fig(n,page,label,note,[LOGIND,LOGLAW],'table',checks,parent)
for f in figures:f['item_id']=f['item_id'].replace(':C5:',':C2:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C2:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page'])
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':2,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every worked example,context activity,logarithm reference block and visual callout recorded. Calculator-key and historical explanatory prose are not extra tasks. The external-scale assumptions stay explicit.'}for page in range(43,46)]
if __name__=='__main__':
 for name,data in [('answers-Goldie-C2-log-intro.json',{'scope':'All Examples2–5and three Activity2.2responses;conditional context evidence distinguished.','items':answers}),('census-Goldie-C2-log-intro.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete43–45including every reference block and worked callout.','new_items':figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);same=equivalent(got,expression(p['printed_key_normalised']))
    assert (not same)if p.get('expected_source_key_status')=='key wrong'else same,(row['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'reference/callout figures')
