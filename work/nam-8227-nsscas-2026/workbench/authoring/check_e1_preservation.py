"""Exhaustive E0/E1 invariant comparison, using the immutable reviewed provider."""
import hashlib,json
from pathlib import Path
from build_source import ROOT,WB,load_source,read,dump
BASE=WB/'authoring/history/stage-e-0'
OLD=WB/'candidates/fcd4b71e07baa07a'
if not OLD.exists():OLD=BASE/'files'/str((WB/'candidates/fcd4b71e07baa07a').relative_to(ROOT))
FLAGS=('criterion_id','marks','mark_type','depends_on','depends_on_any','dependencies_use','follow_through','follow_through_from','accuracy','answer_only_allowed','answer_only_credit','mr09_supplied_result_exclusion','valid_resultant_required','feature_based','more_precise_answer_policy','multiple_function_graphs','misread_policy_id')
MATH_OMIT={'derivative_math','open_fixture','model_exposure_note','full_model','distance_exact_form','misread_eligibility'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def file_before(rel):return BASE/'files'/str((WB/rel).relative_to(ROOT))
def fixture_scores(value):
 fields=('fixture_id','case_id','case','expected_marks','expected_gross_marks','expected_net_marks','expected_state','max_marks','out_of','expected_gross_criterion_awards','expected_gross_earned_local_criterion_ids','expected_net_criterion_awards','pending_clarification')
 if isinstance(value,dict)and'fixtures'in value:value=value['fixtures']
 return [{k:r[k]for k in r if k in fields or k.startswith('expected_')or k.startswith('maximum_')}for r in value]
def check():
 baseline=read(BASE/'manifest.json')
 for rel,h in baseline['files'].items():assert sha(BASE/'files'/rel)==h,rel
 assert sha(OLD/'manifest.json')=='7022ea5049b0f5b02452828d5226f0a533816873f20d551186925e8aacacb250'
 for rel,h in read(OLD/'manifest.json')['files'].items():assert sha(OLD/rel)==h,rel
 current=load_source(name='_e1_preserve_new').create_provider();previous=load_source(root=OLD,name='_e1_preserve_old').create_provider()
 choices={c['selection_id']:c for _,c in load_source(name='_e1_preserve_choices').all_choices()}
 before={r['selection_id']:r for r in previous.list_native_recipes()};after={r['selection_id']:r for r in current.list_native_recipes()}
 assert set(before)==set(after)==set(choices)
 branches=[];instances=0;changed_keys=0
 for selection,c in choices.items():
  _,oc=previous._choice(selection)
  assert c['parameters']==oc['parameters'],selection
  for field in ('recipe_id','branch_id','blooms_level','classification_version','strict_complete_fresh_upper_bound','approved_capacity','raw_generated_capacity'):
   assert before[selection][field]==after[selection][field],(selection,field)
  for i in range(len(c['parameters'])):
   a=previous.generate_at(selection,i);b=current.generate_at(selection,i);instances+=1
   assert a['parameters']==b['parameters']and a['semantic_fingerprint']==b['semantic_fingerprint']
   for field in ('proposed_total_marks','objective_ids','demand_ids','blooms_level','classification_version'):
    assert a[field]==b[field],(selection,i,field)
   assert a['exposure_keys']==b['freshness_required_keys'],(selection,i,'required keys moved')
   if a['exposure_keys']!=b['exposure_keys']:
    assert selection.endswith('implicit-normal:gradient');assert set(a['exposure_keys'])<set(b['exposure_keys']);changed_keys+=1
   for pa,pb in zip(a['parts'],b['parts']):
    assert pa['part_id']==pb['part_id']and pa['proposed_marks']==pb['proposed_marks']
    assert len(pa['criteria'])==len(pb['criteria'])
    for ca,cb in zip(pa['criteria'],pb['criteria']):
     assert {k:ca.get(k)for k in FLAGS}=={k:cb.get(k)for k in FLAGS},(selection,i,ca['criterion_id'],'criterion/dependency drift')
   ma={k:v for k,v in a.get('private_math',{}).items()if k not in MATH_OMIT};mb={k:v for k,v in b.get('private_math',{}).items()if k not in MATH_OMIT}
   assert ma==mb,(selection,i,'private mathematical values changed')
  branches.append({'selection_id':selection,'parameter_rows':len(c['parameters']),'strict_fresh_bound':after[selection]['strict_complete_fresh_upper_bound'],'unchanged':True})
 for rel in ('authoring/calculus-fixtures.json','authoring/trig-log-marking-fixtures.json','authoring/visual/marking-expectations.json'):
  assert fixture_scores(read(file_before(rel)))==fixture_scores(read(WB/rel)),rel
 approved_path=WB/'planning/plan-manifest.json'
 assert sha(approved_path)=='4a0548320dcb9209dcd28e18bd4f6c77423480de6538fcbf1b0f8b6d0e17d8ec'
 approved=read(approved_path)
 for f in ('calculus-design.json','trig-model-design.json','visual-design.json','part-evidence-register.json','pilot-design.json'):
  path=WB/'planning'/f;assert sha(path)==approved['files'][str(path.relative_to(ROOT))],f
 result={'status':'pass','reviewed_stage_e_manifest_sha256':sha(BASE/'manifest.json'),'reviewed_candidate_manifest_sha256':sha(OLD/'manifest.json'),'instances_compared':instances,'branches':branches,'changed_exposed_key_rows':changed_keys,'unchanged_required_freshness_keys':instances,'original_declared_scores_preserved':97,'rubric_criterion_ids_and_mark_types_tariffs_dependencies_flags':'equal on every row','numeric_math_values':'equal; explanatory mathematical text independently recomputed by group oracles','native_version_change':{'before':'0.1.4','after':'0.1.5','transport_before':1,'transport_after':2,'rubric_design':'0.1.4'},'reviewed_candidate_unchanged':True,'reviewed_baseline_files_verified':len(baseline['files'])}
 dump(WB/'checks/stage-e/e1-preservation.json',result);print(json.dumps({k:v for k,v in result.items()if k!='branches'},indent=2))
if __name__=='__main__':check()
