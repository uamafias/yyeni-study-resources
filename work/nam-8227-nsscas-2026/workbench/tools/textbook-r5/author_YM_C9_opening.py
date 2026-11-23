"""YM407–411: definitions, notation conversion and exact/rounded logarithm values."""
import hashlib,json
import author_YM_C8_opening as h
from author_YM_C8_opening import W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
LOG='8227:2020:M2:T2:O01:D01';EXP='8227:2020:M2:T2:O03:D01'
def ev(page):
 name='YM-C9-key-637'if page>=637 else'YM-C8-404-source'if page==407 else f'YM-C9-{408+4*((page-408)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png'
 return dict(path=str(p.relative_to(W.parents[2])),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
h.common.base.ev=ev
def conversion(label,original,result,kp,check=None):
 p=reasoning(label,result,'Preserve the ORIGINAL base and exchange only the exponent/output roles by the real definition: a^u=v iff log_a(v)=u for a>0,a≠1,v>0. Check the complete written relation,not just its already-given numerical exponent. Generic source parameters retain these domain conditions; no common-base10 assumption is imposed on a different base.',kp,'matches')
 p.update(original_relation=original,assessed_8227_demand_ids=[LOG],response_format='symbolic',base_argument_conditions='Base positive and not1; logarithm argument positive. Exponent real.')
 if check:extra(p,'original-numerical-relation',check,'True')
 return p
def value(label,expr,key,kp,exp=False,sf=None):
 p=v(label,expr,key,kp,'Derive from the ORIGINAL power/logarithm definition, preserving positive arguments and a positive nonunit base. For exact powers, solve the matching exponent without a calculator. For the explicitly requested numerical solve, retain the exact internal value and round only the final answer. The internal CAS log ratio is a truth oracle,not a mandated learner change-of-base method.')
 p.update(assessed_8227_demand_ids=[EXP]if exp else[LOG],response_format='numeric')
 if sf:p['operation']={'kind':'rounded','operands':[expr],'significant_figures':sf};p['requested_precision']=str(sf)+' significant figures'
 return p
def add(kind,n,page,note,parts,new_item=False):
 r=h.add(kind,n,page,note,parts,new_item)
 r['item_id']=r['item_id'].replace(':YM:C8:',':YM:C9:')
 target=new[-1]if new_item else corrections[-1];target['item_id']=r['item_id']
 direct=set(r['assessed_8227_demand_ids']);r.update(component_demand_ids=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-direct),mapping_rationale='Base-a logarithm/index conversion directly assesses M2T2O01,not the separate e/ln-definition objectiveO02. Numerical exponential equations are direct only when actually solved,not when the source merely converts notation. Exact powers and generic-domain explanations remain distinct from calculator approximation.',value_level_scope_decisions=[dict(rule_id='8227:LIMIT06',status='within',quoted_value=note,reason='Use the defining inverse-power relation or exact exponent matching. No learner change-of-base method is requested; an internal CAS oracle is not the assessed method.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:LIMIT06']),precision_angle_check=dict(source='Examples3/4,Try3/4 and the introductory50-equation explicitly display3significant figures. Other opening values are exact; no angles occur.',comparison='Use exact internal logarithms/powers,round final numerical outputs once,and retain trailing zeros where the written3sf answer requires them. Generic logs require base>0,base≠1,argument>0.'))
 if new_item:target.update(mapping_rationale=r['mapping_rationale'],value_level_scope_decisions=r['value_level_scope_decisions'],scope_check=r['scope_check'])
 return r
p=value('x','log(1000)/log(10)','3',408)
p['assessed_8227_demand_ids']=[];p['supporting_practice_reason']='The source common-base recap gives10^x=1000=10³. It does not demonstrate the later use-logarithms method.'
add('Worked-illustration',1,408,'Recovered opening common-base illustration10^x=1000 givesx3. It is preparatory exponent matching,not direct coverage of a logarithm-solve method.',[p],True)
p=value('x','log(50)/log(10)','Rational(17,10)',408,True,3);p['component_demand_ids']=[LOG]
add('Worked-illustration',2,408,'Recovered opening10^x=50 is solved by logarithmic form and displayed1.70to3sf. The display is approximate; it is not an exact10^1.70=50 identity.',[p],True)
ps=[conversion('a','10²=100','log_10(100)=2',408,'Eq(10**2,100)'),conversion('b','4⁰=1','log_4(1)=0',408,'Eq(4**0,1)'),conversion('c','80=10^x','x=log_10(80)',408),conversion('d','a^b=c','b=log_a(c)',408)]
add('Example',1,408,'Convert four original index relations to logarithmic notation. Retain the original base,including the generica,while swapping the exponent/output roles.',ps)
ps=[conversion('a','2⁵=32','log_2(32)=5',637,'Eq(2**5,32)'),conversion('b','4¹=4','log_4(4)=1',637,'Eq(4**1,4)'),conversion('c','10=5^x','log_5(10)=x',637),conversion('d','p=q^r','log_q(p)=r',637)]
add('Try-Now',1,408,'Four index-to-log conversions,including UNKNOWN exponentx and generic positive argumentp/baseq. These are symbolic relations,not extra numerical-root requests.',ps)
add('Example',2,409,'Convert x=log_8(5) and log_3(x)=1/5 to exponential form,keeping the base8 or3.',[conversion('a','x=log_8(5)','8^x=5',409),conversion('b','log_3(x)=1/5','3^(1/5)=x',409)])
ps=[conversion('a','log_2(128)=7','2^7=128',637,'Eq(2**7,128)'),conversion('b','log_2(1)=0','2^0=1',637,'Eq(2**0,1)'),conversion('c','−2=log_4(1/16)','4^(−2)=1/16',637,'Eq(4**(-2),Rational(1,16))'),conversion('d','log_n(m)=p','n^p=m',637),conversion('e','x=log_3(0.1)','3^x=0.1',637),conversion('f','log_0.25(k)=n','0.25^n=k',637)]
add('Try-Now',2,409,'Six log-to-index conversions. The reciprocal base0.25 is valid; a negative exponent is also valid. Generic basen remains positive and not1,argumentmpositive.',ps)
add('Example',3,410,'Convert10^x200 to logarithmic notation,THEN solve it to3sf. Exact internalxlog_10(200),display2.30.',[conversion('a','10^x=200','x=log_10(200)=log(200)',410),value('b','log(200)/log(10)','Rational(23,10)',410,True,3)])
add('Try-Now-3',1,410,'For10^x250 convert notation and solve to3sf,display2.40. The written trailing zero records precision.',[conversion('a','10^x=250','log(250)=x',637),value('b','log(250)/log(10)','Rational(12,5)',637,True,3)])
add('Try-Now-3',2,410,'For10^x0.05 convert notation and solve to3sf,display−1.30. A positive argument below1 gives a negative exponent without violating the logarithm domain.',[conversion('a','10^x=0.05','log(0.05)=x',637),value('b','log(Rational(1,20))/log(10)','-Rational(13,10)',637,True,3)])
add('Example',4,410,'Convert log_10(x)=1.2 to x=10^1.2,then find the positive argument to3sf,15.8.',[conversion('a','log_10(x)=1.2','x=10^1.2',410),value('b','10**Rational(6,5)','Rational(79,5)',410,sf=3)])
add('Try-Now-4',1,410,'Convert log_10(x)=3.5 then solve for the positive original argument to3sf:3,160 (three significant digits).',[conversion('a','log_10(x)=3.5','10^3.5=x',637),value('b','10**Rational(7,2)','3160',637,sf=3)])
add('Try-Now-4',2,410,'Convert log_10(x)=−0.6 then solve for its positive argument to3sf:0.251. Negative log value does not mean a negative argument.',[conversion('a','log_10(x)=−0.6','10^(−0.6)=x',637),value('b','10**(-Rational(3,5))','Rational(251,1000)',637,sf=3)])
data=[('a','log(27)/log(3)','3'),('b','log(Rational(1,8))/log(8)','-1'),('c','log(1)/log(5)','0'),('d','log(32)/log(Rational(1,2))','-5')]
add('Example',5,411,'Without a calculator evaluate four logarithms by exact power matching. Reciprocal base1/2 in(d)gives a negative exponent−5; argument1 in(c)giveszero.',[value(l,e,k,411)for l,e,k in data])
data=[('a','log(16)/log(2)','4',637),('b','log(Rational(1,4))/log(2)','-2',637),('c','log(sqrt(27))/log(3)','Rational(3,2)',637),('d','log(Rational(1,8))/log(2)','-3',637),('e','log(5**(-1))/log(5)','-1',637),('f','log(Rational(1,16))/log(4)','-2',637),('g','log(2)/log(Rational(1,2))','-1',637),('h','log(2*sqrt(2))/log(2)','Rational(3,2)',637)]
add('Try-Now-5',1,411,'Eight exact logarithms without a calculator:integer,negative and fractional powers;reciprocal base1/2 remains valid.',[value(l,e,k,kp)for l,e,k,kp in data])
add('Try-Now-5',2,411,'Without a calculator evaluate log_2√8 + log_5(1/∛25) − (1/2)log_3(1/81). Exact result17/6; the leading half multiplies the ENTIRE final logarithm.',[value('answer','log(sqrt(8))/log(2)+log(25**(-Rational(1,3)))/log(5)-log(Rational(1,81))/(2*log(3))','Rational(17,6)',637)])
add('Try-Now-5',3,411,'Evaluate K=log_2(8)+log_3√27−log_(1/3)(9). The last log is−2 and its OUTSIDE minus changes the contribution to+2; K13/2.',[value('K','log(8)/log(2)+log(sqrt(27))/log(3)-log(9)/log(Rational(1,3))','Rational(13,2)',637)])
refs=[(1,408,'Index/log inverse-notation arrows','a^x=y iff log_a(y)=x. Preserve the base while exchanging exponent/output roles; real-domain conditions are required.',[LOG],'table',None),(2,408,'Approximate50-equation check display','The source1.70 is an explicitly rounded3sf exponent for10^x50. Do not promote the displayed approximation to an exact identity.',[EXP],'table','Worked-illustration:2'),(3,408,'Example1 base-preservation reminder','The basea stays fixed; x andy exchange their index/log roles. The symbolic relation is not a request to approximate every numeric argument.',[LOG],'table','Example:1'),(4,409,'Logarithm base/argument domain panel','Base must bepositive and not1; argumentpositive. The0^0=0 line is crossed out as undefined,not endorsed. Negative exponents are admissible for valid positive bases.',[LOG],'table',None),(5,410,'Common-log calculator notation and3sf display','An unlabelledlog here meansbase10. Exact internal values precede the requested final3sf displays; this is not the e/ln definition.',[LOG,EXP],'table','Example:3'),(6,410,'Inverse common-log calculator layout','log_10(x)=1.2 meansx10^1.2; button layout is procedure context,not an additional assessed mathematical output.',[LOG],'table','Example:4'),(7,411,'Base-a inverse rules','log_a(a)=1,log_a(1)=0,log_a(a^x)=x and a^(log_a x)=x require basea>0,a≠1 andpositive argument where applicable.',[LOG],'table',None),(8,411,'Exact-power method reminder','Recognise integer/reciprocal/fractional powers to evaluate the source logs without a calculator. A helpful powers-up-to1000 suggestion does not extend syllabus scope.',[LOG],'table','Example:5')]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,teaches,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C9:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C9:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Read source base/subscript/exponent roles, crossed-out invalid-base examples and calculator layouts. Recompute exact powers and stated final3sf values. Domain restrictions and crossed-out reasoning are distinguished from endorsed equations.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=9,page_status='prose only'if page==407 else'items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='Chapter title/scope/photo407has no mathematical task. Every opening illustration,Example1–5,Try1–5question and eight teaching/reference panels enumerated over408–411.',scope_screen='Logarithm/index relationship versus explicit exponential numerical solve are separate; no e/ln-definition or learner change-of-base demand inferred.')for page in range(407,412)]
def save():
 for name,data in [('answers-YM-C9-opening.json',dict(scope='Complete407–411source responses and exact corresponding keys.',items=answers)),('census-YM-C9-opening.json',dict(book='YM',book_id='8227-SRC-017',chapter=9,source_path=SRC,source_sha256=SHA,scope='Complete407–411page/item/reference census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
