"""E1 focused generation/privacy/freshness regressions; no app state or marker calls."""
from copy import deepcopy
import json,re
from build_source import load_source,WB,dump

PRIVATE_KEYS={'source_path','source_sha256','verified_by','reviewer_notes','review_notes','learner_display_reason','comparison_reason'}
def walk(value):
 if isinstance(value,dict):
  for key,item in value.items():yield key;yield from walk(item)
 elif isinstance(value,list):
  for item in value:yield from walk(item)
def strings(value):
 if isinstance(value,str):yield value
 elif isinstance(value,dict):
  for item in value.values():yield from strings(item)
 elif isinstance(value,list):
  for item in value:yield from strings(item)
def no_bare_prime(text):
 for match in re.finditer(r'\\prime\b',text):
  prefix=text[:match.start()];opening=prefix.rfind('{');closing=prefix.rfind('}')
  assert opening>closing and prefix[:opening].rstrip().endswith('^'),'Bare prime: '+text
 return True

def check():
 m=load_source();p=m.create_provider();g='8227:D:SEL:implicit-normal:gradient';n='8227:D:SEL:implicit-normal:normal';motion='8227:D:SEL:motion-integration:interior-reversal'
 gradient=p.generate_at(g,0);bad_normal=p.generate_at(n,3)
 proof=json.dumps(['implicit-show',gradient['parameters']['a'],gradient['parameters']['k']],separators=(',',':'))
 assert proof in gradient['exposure_keys']and proof not in gradient['freshness_required_keys']
 assert proof in bad_normal['freshness_required_keys']
 assert set(bad_normal['freshness_required_keys'])&set(gradient['exposure_keys']),'Seeded pre-repair repetition did not fail'
 fresh=p.generate_fresh(n,0,gradient['exposure_keys'],mode='test');assert fresh['status']=='fresh'
 assert fresh['question']['domain_index']!=3 and proof not in fresh['question']['freshness_required_keys']
 # Reverse direction keeps the approved gradient bound: proof is exposed, not required.
 assert all(not k.startswith('["implicit-show"')for k in gradient['freshness_required_keys'])
 assert next(x for x in p.list_native_recipes()if x['selection_id']==g)['strict_complete_fresh_upper_bound']==23
 assert next(x for x in p.list_native_recipes()if x['selection_id']==n)['strict_complete_fresh_upper_bound']==8
 counters={'instances':0,'learner_payloads':0,'teacher_payloads':0,'motion_neutral_payloads':0,'held_principal_views':0,'no_real_principal_solutions':0};labels=set()
 for group,c in m.all_choices():
  for index in range(len(c['parameters'])):
   q=p.generate_at(c['selection_id'],index);counters['instances']+=1
   teach=m.teacher_projection(q);counters['teacher_payloads']+=1
   assert not PRIVATE_KEYS.intersection(walk(teach))
   for reference in teach['examination_references']:
    assert reference['relation']in('same-type','original')and reference.get('learner_label')
    assert not(reference['board']=='NSSCAS'and reference['year']==2023 and reference['paper']=='1'and reference['question']=='9')
    labels.add(reference['learner_label'])
   for mode,reveal in [('practice',False),('test',False),('practice',True)]:
    public=m.learner_projection(q,mode=mode,reveal=reveal);counters['learner_payloads']+=1
    assert 'interior-reversal'not in json.dumps(public,ensure_ascii=False)
    assert m.native_identity(q,public['selection_id'])==q['selection_id']
    for part,original in zip(public['parts'],q['parts']):assert m.native_identity(q,part['part_id'])==original['part_id']
    if c['selection_id']==motion:counters['motion_neutral_payloads']+=1
   fields=[q['stem'],q['practice_help']['title'],*q['practice_help']['prompts']]
   for part in q['parts']:
    fields.extend([part['prompt'],part['reference_answer']]);fields.extend(v for step in part['worked_steps']for v in step.values());fields.extend(cr['achievement']for cr in part['criteria'])
   for text in fields:
    no_bare_prime(text)
    assert not re.search(r'(?<![\d.])(?:-?1)\s*(?:\\ln\b|e\^|p\b|\\lvert|\()',text),'Unit coefficient: '+text
    assert r'\operatorname{sign}'not in text
   if c['selection_id']==g:
    assert not re.search(r'\bS[1-4]\b|back.substitut|establish the target',str(q['parts'][0].get('alternative_criterion_mapping'))+str(q['parts'][0].get('valid_alternatives',q['parts'][0].get('alternatives',[]))),re.I)
    assert '9/9'not in str(q['private_math'].get('open_fixture',''))
   if q['recipe_id']=='WB8227-principal-inverse':
    counters['held_principal_views']+=1
    assert not teach['examination_references']
    if q['private_math']['outcome']=='no-real-solution':
     counters['no_real_principal_solutions']+=1
     assert '(kx)'not in str(q['parts'][0]['worked_steps'])
   if q['recipe_id']=='WB8227-trapezium-sketch-estimate':
    for part in (q['parts'][1],q['parts'][3]):
     assert not re.search('follow.through|followed through|own.graph',part['reference_answer'],re.I)
    criterion=q['parts'][3]['criteria'][1];assert 'concavity shorthand'in criterion['achievement']
    reviewed=q['parts'][3]['reviewed_part']['criteria'][1];assert 'concavity shorthand'in reviewed['required']
 # These bad pre-repair values must actually be rejected by the new checks.
 for bad in [r'$f\prime(x)$',r'$y\prime=2$',r'$f\prime\prime(x)$']:
  try:no_bare_prime(bad)
  except AssertionError:pass
  else:raise AssertionError('Seeded bare-prime fixture passed')
 assert no_bare_prime(r"$f'(x),f''(x),y'$" )and no_bare_prime(r'$f^{\prime}(x)$')
 try:m.native_identity(gradient,'foreign-part')
 except ValueError:pass
 else:raise AssertionError('Unknown public part accepted')
 result={'status':'pass','scope':'E1 generated byte regressions; not app/marker acceptance','counts':counters,'displayable_exam_labels':len(labels),'SE11_old_normal_idx3_rejected':True,'SE11_fresh_normal_index':fresh['question']['domain_index'],'SE12_native_ids_unchanged':True,'SE13_held_2023_P1_Q9_excluded':True,'seeded_bare_prime_negatives':3}
 dump(WB/'checks/stage-e/e1-runtime.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':check()
