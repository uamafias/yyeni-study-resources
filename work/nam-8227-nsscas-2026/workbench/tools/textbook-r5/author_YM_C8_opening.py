"""YM376–379: scalar modulus,operation order and two-branch linear equations."""
import hashlib,json
import author_YM_C1_opening as common
from author_YM_C1_opening import W,SRC,SHA,v,fig,figures,compute,expression,equivalent,ym_printed_page
common.base.answers.clear();common.base.new.clear();figures.clear()
answers=common.base.answers;new=common.base.new;corrections=[]
MOD='8227:2020:M2:T1:O01:D01';EQ='8227:2020:M2:T1:O01:D02'
def pp(page):return ym_printed_page(page)
def ev(page):
 name='YM-C8-key-630' if page>=630 else f'YM-C8-{376+4*((page-376)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png'
 return dict(path=str(p.relative_to(W.parents[2])),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
common.base.ev=ev
def extra(p,name,expr,key):
 p.setdefault('additional_operations',{})[name]={'kind':'identity','operands':[expr]};p.setdefault('additional_operation_expected',{})[name]=key;return p
def scalar(label,original,key,kp,units=None):
 p=v(label,original,key,kp,'Evaluate the ORIGINAL expression inside each absolute-value bar first. Take its nonnegative magnitude,then retain any OUTSIDE minus sign,power or other operation. Compare the separately transcribed printed result;do not simply remove every minus sign in the expression.')
 p.update(assessed_8227_demand_ids=[MOD],response_format='numeric',given_representation='text',original_expression=original)
 if units:p.update(units=units,printed_key_units=units)
 return p
def equation(label,original,key,kp):
 p=v(label,f'solveset({original},x,domain=S.Reals)',key,kp,'Start from the ORIGINAL real modulus equation. Isolate the modulus and inspect its right-hand side before branching:negative gives no solution,zero one linear zero,positive both signs. Check every resulting root in the original equation. The source key is a separate transcription,not input to the solver.')
 p.update(assessed_8227_demand_ids=[EQ],response_format='symbolic',given_representation='text',original_equation_zero_form=original)
 return p
def add(kind,n,page,note,parts,new_item=False):
 direct=sorted({d for p in parts for d in p.get('assessed_8227_demand_ids',[])})
 r=common.add(kind,n,page,note,parts,direct,[]);r['item_id']=r['item_id'].replace(':YM:C1:',':YM:C8:');meta=new.pop();meta['item_id']=r['item_id']
 for p in r['subparts']:p['review_date']='2026-11-20'
 r.update(representation='text',sketch_response_required=False,component_demand_ids=[],mapping_rationale='Scalar absolute-value interpretation is direct modulus-notation practice. Solving an actual modulus equation is a separate direct demand. Arithmetic order inside/outside bars is a component,not a new AS problem type. Forecast/tolerance contexts do not create additional scientific uncertainty demands.',
  scope_check={'status':'in-scope','basis':note,'excluded_or_qualified_parts':[],'limits_considered':['8227:QUAL01','8227:LIMIT05'],'qualifier_applicability_note':'These are scalar modulus values or linear modulus EQUATIONS,not a parameterised modulus GRAPH or polynomial-division task.'},
  value_level_scope_decisions=[dict(rule_id='8227:QUAL01',status='not applicable',quoted_value=note,reason='The integer-coefficient restriction concerns the specified modulus graph forms. This item evaluates scalar expressions or solves an equation;it is not a fractional-coefficient graph task.'),dict(rule_id='8227:LIMIT05',status='not applicable',quoted_value=note,reason='No polynomial long division is requested.')],
  precision_angle_check={'source':'Exact integer/fraction arithmetic. Diameter inputs46.0,46.8,45.3mm give exact displayed deviations0.8,0.7mm. Temperature differences retain degreesC. No angle is present.','comparison':'Keep signs outside bars,powers and nested grouping. Absolute value is NONNEGATIVE,including0. Contextual magnitudes carry the original difference units;no additional rounding is invented.'})
 if new_item:
  meta.update(item_kind='worked-illustration',scope_check=r['scope_check'],mapping_rationale=r['mapping_rationale'],value_level_scope_decisions=r['value_level_scope_decisions']);new.append(meta)
 else:corrections.append(dict(item_id=r['item_id'],pdf_page=page,printed_page=pp(page)))
 return r
add('Example',1,377,'Forecast34°C,actual32°C or37°C:find absolute error magnitudes2°C and3°C;the signed forecast differences are not the requested output.',[scalar('a','Abs(34-32)','2',377,'°C'),scalar('b','Abs(34-37)','3',377,'°C')])
ps=[scalar('a','Abs(Rational(468,10)-46)','Rational(4,5)',630,'mm'),scalar('b','Abs(Rational(453,10)-46)','Rational(7,10)',630,'mm')]
ps[0]['printed_key_display']='0.8mm';ps[1]['printed_key_display']='0.7mm'
add('Try-Now',1,377,'Specified diameter46.0mm versus actual46.8mm/45.3mm:report nonnegative deviations0.8mm/0.7mm. Exact decimal operands are represented as rationals.',ps)
add('Example',2,378,'Four expressions distinguish an inside subtraction,an OUTSIDE minus,a product inside bars,and an OUTSIDE square followed by minus.',[scalar('a','Abs(2-5)','3',378),scalar('b','-Abs(-3)','-3',378),scalar('c','Abs(2+3*(-4))','10',378),scalar('d','-Abs(-2)**2','-4',378)])
data=[('a','Abs(-9)','9',630),('b','-9-Abs(9)','-18',631),('c','Abs(11)-Abs(13)','-2',631),('d','Abs(7-5)','2',631),('e','Abs(-4-9)','13',631),('f','Abs(0)-1','-1',631),('g','-Abs(-2)+Abs(7)','5',631),('h','Abs(-2)+0','2',631),('i','-Abs(-3)-4','-7',631),('j','Abs(-2)+Abs(2)','4',631),('k','Abs(-2-3)','5',631),('l','-Abs(-8+2)','-6',631)]
add('Try-Now-2',1,378,'Twelve original signed expressions test the exact scope of each modulus bar. Negative whole-expression answers remain possible when minus/subtraction is outside the bars.',[scalar(label,original,key,kp)for label,original,key,kp in data])
data=[('a','Abs(18)-Abs(-2)','16'),('b','-Abs((-2)**2)','-4'),('c','(-Abs(-2))**2','4'),('d','-(Abs(-3)-Abs(4))','1'),('e','(-2)**3*Abs(-2)**5','-256'),('f','Abs(-2)**3/Abs(-4)**2','Rational(1,2)')]
add('Try-Now-2',2,378,'Six nested/powered expressions. Preserve outer grouping in(c),(d),the negative base outside bars in(e),and the nonzero squared denominator in(f).',[scalar(label,original,key,631)for label,original,key in data])
p=equation('solutions','Abs(x)-7','FiniteSet(-7,7)',378)
add('Worked-illustration',1,378,'The explicit boxed question asks which TWO numbers have modulus7. Its answer number line and text give−7,+7;this recovered worked prompt is not a new source-numbered example.',[p],True)
p=equation('solutions','Abs(5-2*x)-7','FiniteSet(-1,6)',379)
extra(p,'original-root-checks','Tuple(Abs(5-2*(-1))-7,Abs(5-2*6)-7)','Tuple(0,0)')
add('Example',3,379,'Solve the ORIGINAL|5−2x|=7 with two branches and check roots−1,6 in the original.',[p])
add('Try-Now',3,379,'Four linear modulus equations:|x|3,|3−x|2,|−3x|9,|x−4|4. Keep both distinct roots,including zero in the final equation.',[equation('a','Abs(x)-3','FiniteSet(-3,3)',631),equation('b','Abs(3-x)-2','FiniteSet(1,5)',631),equation('c','Abs(-3*x)-9','FiniteSet(-3,3)',631),equation('d','Abs(x-4)-4','FiniteSet(0,8)',631)])
ps=[equation('a','Abs(4*x+6)+3-8','FiniteSet(-Rational(1,4),-Rational(11,4))',379),equation('b','-2*Abs(x-3)+8-(-24)','FiniteSet(-13,19)',379)]
extra(ps[0],'original-root-checks','Tuple(Abs(4*(-Rational(1,4))+6)+3-8,Abs(4*(-Rational(11,4))+6)+3-8)','Tuple(0,0)')
extra(ps[1],'original-root-checks','Tuple(-2*Abs(-13-3)+8+24,-2*Abs(19-3)+8+24)','Tuple(0,0)')
add('Example',4,379,'Isolate modulus before branching:|4x+6|+3=8 gives modulus5;−2|x−3|+8=−24 gives modulus16. Outside negative scaling is retained.',ps)

refs=[(1,377,'Absolute-distance number line','Points−3,+3 lie the same distance3 from0;the oriented coordinate sign differs but distance is nonnegative.',[MOD],'diagram',None),(2,377,'Piecewise absolute-value definition','|x|=x forx>0,0 atx0,−x forx<0. Source examples±7 and0 verify all three cases. Earlier loose positive wording must not exclude0.',[MOD],'table',None),(3,378,'Absolute-expression evaluation order','Evaluate inside each bar first,take its NONNEGATIVE magnitude,then apply outside signs/powers. Do not remove an outside negative sign or change a nested product before evaluating it.',[MOD],'table','Example:2'),(4,378,'Worked ±7 answer number line','The inline worked prompt|x|7 has solution points−7,+7. This is a SOLUTION/teaching illustration,not extra givens for an independent problem.',[EQ],'diagram','Worked-illustration:1'),(5,378,'Negative/zero/positive modulus target table','For|x|d,negative d gives no real solution,zero gives only0,positive d gives two roots±d. The count depends on the isolated target,not a blanket two-root rule.',[EQ],'table',None),(6,379,'Isolate modulus before solving','Move outside terms and divide by the nonzero outer coefficient before deciding target sign and branching. SourceExample4 includes negative outer coefficient−2.',[EQ],'table','Example:4')]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,teaches,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C8:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C8:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Read actual bar boundaries,outer signs,powers and number-line orientation. Recompute all parent scalar values/root sets from separately transcribed originals. The piecewise zero case is retained;solution illustrations are not counted as given diagrams or asked sketches.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=8,page_status='prose only'if page==376 else'items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='Title/scope/decorative biography376has no mathematical task. AllExamples1–4,Try1/Try2Q1–2/Try3,the recovered boxed|x|7prompt,and six actual number-line/reference panels enumerated over377–379.',scope_screen='Scalar modulus notation and linear modulus equations;no graph coefficient or polynomial-division demand is claimed from these tasks.')for page in range(376,380)]
def save(stem,scope):
 for name,data in [(f'answers-YM-C8-{stem}.json',dict(scope=scope,items=answers)),(f'census-YM-C8-{stem}.json',dict(book='YM',book_id='8227-SRC-017',chapter=8,source_path=SRC,source_sha256=SHA,scope=scope,new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation' in p:
    target=p.get('author_expected_normalised',p.get('printed_key_normalised',p.get('author_check_target_normalised')))
    assert equivalent(compute(p['operation']),expression(target)),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    got=compute(op)
    if name in p.get('additional_operation_expected',{}):assert equivalent(got,expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save('opening','Complete376–379opening:34responses and every reference panel.')
