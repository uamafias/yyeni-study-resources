"""Focused E1 calculus checks against the frozen Stage-E baseline.

Exhaustive emitted-data, derivative-notation and rubric-identity checks; new
rounding expectations are declarations, never raw-response recognition tests.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from fractions import Fraction
from decimal import Decimal,localcontext,ROUND_HALF_UP
import hashlib,json,re
import mpmath as mp
from build_source import load_source,ROOT,WB,dump

m=load_source(name='_e1_calculus_checks').groups()[0]
oldpath=WB/'authoring/history/stage-e-0/files/work/nam-8227-nsscas-2026/workbench/source/groups/calculus.py'
spec=spec_from_file_location('e1_before_calculus',oldpath);old=module_from_spec(spec);spec.loader.exec_module(old)
mp.mp.dps=90

def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,dict):
  for x in v.values():yield from strings(x)
 elif isinstance(v,list):
  for x in v:yield from strings(x)

def bare_prime(text):
 # Explicit superscript prime blocks are legal; standalone macros are not.
 stripped=re.sub(r'\^\{(?:\\prime\s*)+\}','',text)
 return bool(re.search(r'\\prime\b',stripped))

def validate_prime_notation(q):
 if any(bare_prime(s)for s in strings(q)):raise ValueError('Bare prime outside superscript')

for corrupted in ({'prompt':r'f\prime(x)'},{'worked_steps':[{'result':r'f\prime\prime(x)'}]}):
 try:validate_prime_notation(corrupted)
 except ValueError:pass
 else:raise AssertionError('Seeded bare-prime corruption was accepted')

def structure(q):
 return [{'part_id':p['local_part_id'],'marks':p['proposed_marks'],
          'criteria':[{k:c[k]for k in ('criterion_id','marks','mark_type','depends_on','depends_on_any','mr09_supplied_result_exclusion')}for c in p['criteria']]}for p in q['parts']]

assert bare_prime(r'f\prime(x)')
assert bare_prime(r'f\prime\prime(x)')
assert not bare_prime("f''(x)")
assert not bare_prime(r'f^{\prime\prime}(x)')
counts={'SE-01':0,'SE-02':0,'SE-08':0,'SE-09':2,'SE-10':0};total=0;render=[];out=[]
for choice in m.choices():
 oldchoice=next(c for c in old.choices()if c['selection_id']==choice['selection_id'])
 assert choice==oldchoice,'Domain/choice metadata changed'
 for i,params in enumerate(choice['parameters']):
  q=m.build(choice['recipe_id'],choice['branch_id'],params);before=old.build(choice['recipe_id'],choice['branch_id'],params);total+=1
  assert structure(q)==structure(before),'Tariff/criterion/dependency changed'
  assert q['exposure_keys']==before['exposure_keys'],'Required semantic exposure key changed'
  assert q['private_math'].get('gradient')==before['private_math'].get('gradient')
  if any(bare_prime(s)for s in strings(before)):counts['SE-01']+=1
  validate_prime_notation(q)
  if choice['branch_id']in ('gradient','normal'):
   counts['SE-02']+=1
   alternatives=q['parts'][0]['accepted_alternatives'];formula=alternatives[0]['formula']
   assert r'\operatorname{sign}'not in formula
   assert not re.search(r'(?<![0-9])1e\^',formula)
   assert f"\\sigma={1 if params['a']+2*params['q']>0 else -1}"in formula
   if choice['branch_id']=='gradient':
    counts['SE-08']+=1
    alt=' '.join(strings(alternatives))
    assert all(f'G{n}'in alt for n in range(1,6))
    assert not re.search(r'\bS[34]\b|back-substitut|\btarget\b',alt,re.I)
    assert '9/9'not in q['private_math']['open_fixture']
    assert '5/5'in q['private_math']['open_fixture']
  assert not any('the first 1 seconds'in s or 'boundary conditions'in s for s in strings(q))
  if i in (0,len(choice['parameters'])//2,len(choice['parameters'])-1):
   for p in q['parts']:
    texts=[p['prompt'],p['reference_answer']]+[step['result']for step in p['worked_steps']]
    for text in texts:
     for tex in re.findall(r'\$(.*?)\$',text,re.S):
      if "'"in tex:render.append({'branch':choice['branch_id'],'domain_index':i,'tex':tex})
  out.append({'branch':choice['branch_id'],'domain_index':i,'structural_preservation':'pass'})

fixtures=json.loads((WB/'authoring/calculus-fixtures.json').read_text());oldfixtures=json.loads((WB/'authoring/history/stage-e-0/files/work/nam-8227-nsscas-2026/workbench/authoring/calculus-fixtures.json').read_text())
assert len(fixtures)==len(oldfixtures)==51
assert [f['fixture_id']for f in fixtures]==[f['fixture_id']for f in oldfixtures]
for new,previous in zip(fixtures,oldfixtures):
 for key in previous:
  if key.startswith('expected')or key.startswith('max')or key.startswith('net_'):assert new.get(key)==previous[key],(new['fixture_id'],key)
normal=next(f for f in fixtures if f['fixture_id']=='calc:normal:alternative')
assert 'm=-6e^0(-4)/(3e^0+2(-4))=24/(-5)=-24/5'in normal['learner_submission']
stationary=next(f for f in fixtures if f['fixture_id']=='calc:two-extrema:alternative')
assert 'f(-1)=(-1)^3-3(-1)+2=4'in stationary['learner_submission']
assert 'f(1)=1^3-3(1)+2=0'in stationary['learner_submission']

def sig(value,places=3):
 with localcontext()as ctx:
  ctx.prec=90
  n=Decimal(str(value))
  return n.quantize(Decimal(1).scaleb(n.adjusted()-places+1),rounding=ROUND_HALF_UP)
rounding=[]
design=json.loads((WB/'planning/d4/motion-design-check.json').read_text())
exp_rows=next(b for b in design['branches']if b['branch_id'].endswith(':exponential-positive'))['rounding_flip_fixtures']
exp_choice=next(c for c in m.choices()if c['branch_id']=='exponential-positive')
for row in exp_rows:
 V=int(row['tuple'][0]);k=Fraction(row['tuple'][1]);T=int(row['tuple'][2]);params={'V':V,'k':str(k),'T':T};idx=exp_choice['parameters'].index(params)
 exponential=mp.exp(-mp.mpf(k.numerator)*T/k.denominator)
 exact=mp.mpf(V*k.denominator)/k.numerator*(1-exponential)
 rounded_e=sig(exponential,row['intermediate_sf'])
 with localcontext()as ctx:
  ctx.prec=90
  premature=Decimal(V*k.denominator)/Decimal(k.numerator)*(1-rounded_e)
 correct=sig(exact);wrong=sig(premature)
 assert correct==Decimal(row['canonical_3sf'])and wrong==Decimal(row['premature_3sf'])and correct!=wrong
 rounding.append({'fixture_id':f"calc:E1:exponential-rounding:{idx}:{row['intermediate_sf']}",'kind':'declared-rounding-expectation','selection_id':exp_choice['selection_id'],'domain_index':idx,'parameters':params,'source_basis':'planning/d4/motion-design-check.json:exponential-positive.rounding_flip_fixtures; motion WO71','true_distance_90dp':str(exact),'rounded_exponential':str(rounded_e),'intermediate_significant_figures':row['intermediate_sf'],'accepted_final_3sf':str(correct),'rejected_premature_final':str(wrong),'required_working':'Complete correct differentiation and primitive/both-bound working; only the early numerical exponential evaluation is rounded.','expected_earned_suffixes':['E1','E2','E3','E4'],'expected_lost_suffixes':['E5'],'expected_marks':4,'max_marks':5,'assessment_status':'declared rubric expectation, not response-recognition test'})
mixed=next(c for c in m.choices()if c['branch_id']=='interior-reversal')
for idx,field,exact in [(14,'distance',Fraction(233,2)),(134,'distance',Fraction(233,2)),(5,'displacement',Fraction(-265,2)),(125,'displacement',Fraction(265,2))]:
 params=mixed['parameters'][idx]
 # Integrate the independently expanded polynomial exactly, including every leg.
 k,r,c,T=(params[z]for z in ('k','r','c','T'))
 def primitive(t):return Fraction(k*t**3,3)+Fraction(k*(c-r)*t*t,2)-k*r*c*t
 cuts=[0]+([r]if r<T else[])+[T]
 value=sum(abs(primitive(b)-primitive(a))for a,b in zip(cuts,cuts[1:]))if field=='distance'else primitive(T)-primitive(0)
 assert value==exact
 dec=Decimal(exact.numerator)/Decimal(exact.denominator);correct=sig(dec)
 wrong=Decimal(116 if field=='distance'else(-132 if exact<0 else 132))
 suffix='R4'if field=='distance'else'R6'
 rounding.append({'fixture_id':f'calc:E1:mixed-half-boundary:{field}:{idx}','kind':'declared-rounding-expectation','selection_id':mixed['selection_id'],'domain_index':idx,'parameters':params,'source_basis':'motion WO71; review SE10','part':field,'accepted_exact_fraction':str(exact),'accepted_exact_decimal':str(dec),'accepted_final_3sf':str(correct),'rejected_half_even_final':str(wrong),'required_working':'Complete canonical root/interval decision and primitive/bound calculations for both parts. The only wrong evidence is the final half-boundary rounding in the identified part.','expected_lost_suffixes':[suffix],'expected_marks_if_only_this_rounding_error':5,'max_marks':6,'assessment_status':'declared rubric expectation, not response-recognition test'})
counts['SE-10']=len(rounding)
dump(WB/'authoring/e1-calculus-rounding-fixtures.json',{'status':'declared expectations independently recomputed','fixtures':rounding,'old_owner_scores_changed':False,'limitations':'No raw response marker invoked; exact and correctly half-up rounded results both accepted per approved WO71.'})
dump(WB/'authoring/e1-calculus-prime-render-inputs.json',render)
report={'status':'pass','all_domain_rows':total,'affected_instance_counts':counts,'required_freshness_keys_unchanged':True,'domains_unchanged':True,'ordered_tariffs_criterion_ids_mark_types_dependencies_unchanged':True,'old_51_fixture_expected_scores_unchanged':True,'repaired_fixture_ids':[normal['fixture_id'],stationary['fixture_id']],'new_rounding_expectations':len(rounding),'bare_prime_negative_fixtures_rejected':2,'render_expression_count':len(render),'source_sha256':hashlib.sha256((WB/'source/groups/calculus.py').read_bytes()).hexdigest(),'scope':'author verification only; derivative render inspection recorded separately; no raw learner-response recognizer/app or independent acceptance'}
dump(WB/'authoring/e1-calculus-check.json',report)
print(json.dumps(report,indent=2))
