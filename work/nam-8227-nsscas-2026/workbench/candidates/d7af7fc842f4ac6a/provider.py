"""NSSCAS 8227 candidate provider. No application state or grading-model calls.

The v1 bridge is a structural transport. Native metadata remains authoritative;
visual response assessment and safe app presentation require the documented handoff.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import json
import random
import re

ROOT=Path(__file__).resolve().parent
PACKAGE_ID='namibia-nsscas-8227'
VERSION='0.1.5'
RUBRIC_VERSION='0.1.4'
TRANSPORT_REVISION=2

def read(name):return json.loads((ROOT/name).read_text())
def canonical(value):return json.dumps(value,sort_keys=True,ensure_ascii=False,allow_nan=False,separators=(',',':')).encode()
def digest(value):return hashlib.sha256(canonical(value)).hexdigest()
def groups():
 from .groups import calculus,trig_log,visual
 return (calculus,trig_log,visual)
def all_choices():
 return [(module,choice) for module in groups() for choice in module.choices()]
def norm_branch(value):return value.rsplit(':',1)[-1]
def legacy_visible(q):
 assets=[]
 for asset in q['assets']:
  if asset['role']=='question_and_solution':
   assets.append({k:deepcopy(asset[k]) for k in ('asset_id','question_diagram','prepared_question_reference','print_at_actual_size','display_instruction') if k in asset})
 return {'stem':q['stem'],'parts':[p['prompt']for p in q['parts']],'assets':assets}
def normalized_exposure(key):
 # Versions are provenance, never a means of resetting no-repeat history.
 return re.sub(r'@0\.1\.[1-5](?=:|$)','',key)

class NSSCASProvider:
 def describe(self):return {'package_id':PACKAGE_ID,'version':VERSION,'native_recipe_version':VERSION,'transport_revision':TRANSPORT_REVISION,'state':'candidate'}
 def list_recipes(self):return [deepcopy(r['public'])for r in read('recipes.json')]
 def list_native_recipes(self):return read('catalogue-native.json')
 def _choice(self,key):
  for module,c in all_choices():
   if c['selection_id']==key:return module,c
  raise ValueError('Unknown reviewed selection')
 def generate(self,key,recipe_version,seed):
  if type(recipe_version)is not int or recipe_version!=TRANSPORT_REVISION:raise ValueError('Unsupported transport revision')
  if type(seed)is not int or not 0<=seed<2**63:raise ValueError('Seed must be an integer in [0, 2**63)')
  _,c=self._choice(key)
  index=random.Random(seed).randrange(len(c['parameters']))
  return self.generate_at(key,index,seed=seed)
 def generate_at(self,key,index,*,seed=0):
  module,c=self._choice(key)
  if type(seed)is not int or not 0<=seed<2**63:raise ValueError('Invalid seed')
  if type(index)is not int or not 0<=index<len(c['parameters']):raise ValueError('Outside admitted finite domain')
  params=deepcopy(c['parameters'][index]);q=deepcopy(module.build(c['recipe_id'],c['branch_id'],params))
  native=next(row for row in self.list_native_recipes() if row['selection_id']==key)
  specs=native['part_specs'];parts=q['parts']
  if len(parts)!=len(specs):raise ValueError('Part count differs from reviewed branch')
  for p,spec in zip(parts,specs):
   local=spec.get('local_part_id',spec['part_id'].rsplit(':',1)[-1])
   if p['local_part_id']!=local:raise ValueError('Part identity differs from reviewed branch')
   p.update(part_id=spec['qualified_part_id'],proposed_marks=spec['marks'],reviewed_part=deepcopy(spec))
   if sum(c['marks']for c in p['criteria'])!=spec['marks']:raise ValueError('Criterion tariff differs from approved part')
  assets=[];index_assets=read('asset-index.json')
  for asset in q.get('assets',[]):
   body=asset['svg'].encode();sha=hashlib.sha256(body).hexdigest();asset_id='8227:asset:'+sha
   row=index_assets.get(sha)
   if not row or row['sha256']!=sha or asset['role'] not in row['roles']:raise ValueError('Asset is not sealed for requested role')
   ref={'asset_id':asset_id,'sha256':sha,'role':asset['role'],'mime_type':'image/svg+xml'}
   targets=asset.get('part_ids',[asset['part_id']]if asset.get('part_id')else[])
   target_ids=[part['part_id']for part in parts if not targets or part['local_part_id']in targets or part['part_id']in targets]
   if not target_ids:raise ValueError('Diagram refers to an unknown assessed part')
   assets.append(dict(asset_id=asset_id,role='question_and_solution'if asset['role']=='question'else'solution',question_diagram=ref if asset['role']=='question'else None,reference=ref,alt=asset.get('alt',''),must_read_givens=asset.get('must_read_givens',[]),target_part_ids=target_ids,diagram_parameters=deepcopy(asset.get('diagram_parameters',{}))))
  required_keys=sorted({normalized_exposure(k)for k in q['exposure_keys']})
  exposed_keys=set(required_keys)
  if c['recipe_id']=='WB8227-implicit-normal'and norm_branch(c['branch_id'])=='gradient':
   exposed_keys.add(json.dumps(['implicit-show',params['a'],params['k']],separators=(',',':'),ensure_ascii=False))
  q['freshness_required_keys']=required_keys
  q['exposure_keys']=sorted(exposed_keys)
  q['assets']=assets
  q['practice_help']={'version':1,**q['practice_help']}
  q.update(recipe_id=c['recipe_id'],selection_id=key,branch_id=c['branch_id'],recipe_version=VERSION,generator_version=TRANSPORT_REVISION,generator_seed=seed,parameters=params,domain_index=index,source_branch={'kind':norm_branch(c['branch_id'])},proposed_total_marks=sum(p['proposed_marks']for p in parts),objective_ids=native['objective_ids'],demand_ids=native['demand_ids'],blooms_level=native['blooms_level'],classification_version=native['classification_version'],examination_references=deepcopy(native['examination_references']),generation_identity={'package_id':PACKAGE_ID,'package_version':VERSION,'recipe_version':VERSION,'selection_id':key,'branch_id':c['branch_id'],'seed':seed,'parameters_sha256':digest(params),'algorithm':'finite-domain-python-random-v1','approved_design_manifest_sha256':read('provenance.json')['approved_design_manifest_sha256']},exposure_keys=sorted({normalized_exposure(k)for k in q['exposure_keys']}))
  for reference in q['examination_references']:
   applies=reference.get('applies_to_part_ids',[])
   if reference.get('target_part_id'):applies=applies+[reference['target_part_id']]
   targets=[part['part_id']for part in parts if part['local_part_id']in applies or part['part_id']in applies]
   reference['target_part_ids']=targets
   reference['scope']='part'if targets else'branch-internal'
   if reference.get('relation')in('same-type','original')and reference.get('learner_display',True)and not targets:
    raise ValueError('Displayable reference lacks an assessed part binding')
  q['owner_design_approval']={'owner':'Vitalis','manifest_sha256':read('provenance.json')['approved_design_manifest_sha256'],'runtime_content_review':'pending'}
  q['objective_ids']=sorted(set(q['objective_ids'])|set(q.get('conditional_direct_objective_ids',[])))
  q['demand_ids']=sorted(set(q['demand_ids'])|set(q.get('conditional_direct_demand_ids',[])))
  q['semantic_fingerprint']=digest({'recipe_id':q['recipe_id'],'branch_id':q['branch_id'],'parameters':params})
  q['fingerprint']=digest(legacy_visible(q))
  rules=read('subject-rules.json')
  q['native_marking_memo']={'schema':'8227-marking-evidence-v1','recipe_version':VERSION,'parts':deepcopy(parts),'assets':deepcopy(assets),'subject_rules':rules,'marks':q['proposed_total_marks'],'app_adapter_required':True}
  rubric_text='\n\n'.join('Part '+p['local_part_id']+'\n'+p['reference_answer']+'\n'+'\n'.join(c['criterion_id']+' ['+str(c['marks'])+']: '+c['achievement']for c in p['criteria'])+'\n'+'\n'.join(step['action']+' — '+step['reason']+' — '+step['result']for step in p['worked_steps'])for p in parts)
  memo={'contract_version':'workbench-exam-guidance-v1','package_id':PACKAGE_ID,'recipe_id':q['recipe_id'],'recipe_version':TRANSPORT_REVISION,'native_recipe_version':VERSION,'question':q['stem']+'\n\n'+'\n\n'.join(p['prompt']for p in parts),'canonical_answer':'\n\n'.join(p['reference_answer']for p in parts),'grading_guide_answer':rubric_text,'subject_rules':rules,'marks':q['proposed_total_marks'],'criteria':[dict(criterion_id=c['criterion_id'],criterion=c['achievement'],marks_available=c['marks'])for p in parts for c in p['criteria']]}
  ids=[r['criterion_id']for r in memo['criteria']]
  if len(ids)!=len(set(ids)):raise ValueError('Duplicate criterion identity')
  memo['contract_hash']=digest(memo);q['marking_memo']=memo
  contract={'schema_version':'workbench-whole-question-v1','question_fingerprint':q['fingerprint'],'max_marks':q['proposed_total_marks'],'source_marking_contract':memo}
  contract['contract_hash']=digest(contract);q['grading_contract']=contract
  q['instance_hash']=digest(q)
  return q
 def validate_instance(self,q):
  try:
   assert q['instance_hash']==digest({k:v for k,v in q.items()if k not in ('instance_hash','resource_origin')})
   assert q['recipe_version']==VERSION and q['generator_version']==TRANSPORT_REVISION
   assert q['fingerprint']==digest(legacy_visible(q))
   assert sum(p['proposed_marks']for p in q['parts'])==q['proposed_total_marks']
   for p in q['parts']:
    assert p['prompt'].strip()and p['reference_answer'].strip()
    assert sum(c['marks']for c in p['criteria'])==p['proposed_marks']
    assert all(s.get(k,'').strip()for s in p['worked_steps']for k in ('action','reason','result'))
   return {'valid':True,'scope':'structural and frozen-evidence integrity; not independent content acceptance'}
  except (AssertionError,KeyError,TypeError,ValueError):return {'valid':False,'reason':'Frozen instance integrity or structure differs'}
 def generate_fresh(self,key,seed,excluded_exposure_keys=(),*,mode='practice',allow_repeat=False):
  if mode not in ('practice','test'):raise ValueError('Unknown learning mode')
  if mode=='test'and allow_repeat:raise ValueError('Tests require fresh instances')
  if type(seed)is not int or not 0<=seed<2**63:raise ValueError('Invalid seed')
  _,c=self._choice(key);indices=list(range(len(c['parameters'])));random.Random(seed).shuffle(indices)
  excluded={normalized_exposure(k)for k in excluded_exposure_keys}
  for i in indices:
   q=self.generate_at(key,i,seed=seed)
   if not excluded.intersection(q['freshness_required_keys']):return {'status':'fresh','question':q,'searched':indices.index(i)+1}
  if allow_repeat:
   return {'status':'repeated-practice','question':self.generate_at(key,indices[0],seed=seed),'fresh':False,'searched':len(indices)}
  return {'status':'exhausted','question':None,'fresh':False,'searched':len(indices),'reason':'No admitted instance has all required assessed exposure keys fresh. Choose another reviewed type or explicitly repeat in practice.'}
 def resolve_asset(self,asset_id,sha,role):
  if role not in ('question','solution')or asset_id!='8227:asset:'+sha:raise ValueError('Asset identity/role mismatch')
  row=read('asset-index.json').get(sha)
  if not row or role not in row['roles']:raise ValueError('Asset not allowed for role')
  p=ROOT/row['path']
  if hashlib.sha256(p.read_bytes()).hexdigest()!=sha:raise ValueError('Asset bytes differ')
  return row['path']
 def asset_for_instance(self,q,asset_id,sha,role,*,solution_revealed=False):
  if not self.validate_instance(q)['valid']:raise ValueError('Invalid frozen instance')
  if role=='solution'and not solution_revealed:raise ValueError('Solution not revealed')
  if not any(a['asset_id']==asset_id and a['reference']['sha256']==sha and a['reference']['role']==role for a in q['assets']):raise ValueError('Asset belongs to another instance or role')
  return self.resolve_asset(asset_id,sha,role)

def public_identity(identifier):
 """Display aliases are separate from immutable native/marking identities."""
 return identifier.replace(':interior-reversal',':quadratic-motion')

def native_identity(question, public_id):
 """Resolve only an identity belonging to this frozen question, server-side."""
 identities=[question['selection_id']]+[p['part_id']for p in question['parts']]
 for identifier in identities:
  if public_identity(identifier)==public_id:return identifier
 raise ValueError('Public identity does not belong to this question')

def display_references(question, *,learner=False):
 result=[]
 allowed=('board','syllabus_code','year','session','paper','question','part','printed_page','relation','learner_label','target_part_id','target_part_ids','scope')
 for reference in question['examination_references']:
  if reference.get('relation')not in('original','same-type')or not reference.get('learner_display',True):continue
  value={key:deepcopy(reference[key])for key in allowed if key in reference}
  if learner:
   if value.get('target_part_id'):value['target_part_id']=public_identity(value['target_part_id'])
   value['target_part_ids']=[public_identity(x)for x in value.get('target_part_ids',[])]
  result.append(value)
 return result

def learner_projection(q,*,mode='practice',reveal=False):
 """Safe native display; app ownership still enforces attempt/reveal permissions."""
 if mode not in ('practice','test'):raise ValueError('Unknown learning mode')
 if mode=='test'and reveal:raise ValueError('Test solution reveal must wait until the test is submitted')
 public={'stem':q['stem'],'max_marks':q['proposed_total_marks'],'selection_id':public_identity(q['selection_id']),'recipe_version':q['recipe_version'],'parts':[{'part_id':public_identity(p['part_id']),'prompt':p['prompt'],'max_marks':p['proposed_marks'],'response_format':p['reviewed_part']['response_format']}for p in q['parts']],'assets':[{'reference':deepcopy(a['reference']),'alt':a['alt'],'must_read_givens':deepcopy(a['must_read_givens']),'target_part_ids':[public_identity(x)for x in a['target_part_ids']]}for a in q['assets']if a['role']=='question_and_solution'],'examination_references':display_references(q,learner=True)}
 if mode=='practice':public['practice_help']=deepcopy(q['practice_help'])
 if reveal:
  public['solution']=[{'part_id':public_identity(p['part_id']),'answer':p['reference_answer'],'steps':deepcopy(p['worked_steps'])}for p in q['parts']]
  public['solution_assets']=[deepcopy(a['reference'])for a in q['assets']if a['role']=='solution']
 return public

def create_provider():return NSSCASProvider()


def _teacher_metadata(value):
 """Keep educational rationale/locators while omitting internal file/review data."""
 private={'source_path','source_sha256','verified_by','reviewer_notes','review_notes','learner_display_reason','comparison_reason'}
 if isinstance(value,dict):return {key:_teacher_metadata(item)for key,item in value.items()if key not in private}
 if isinstance(value,list):return [_teacher_metadata(item)for item in value]
 return deepcopy(value)

def teacher_projection(q):
 """Safe educational metadata; authentication and teacher access are app-owned."""
 return {'owner_design_approval':{'owner':q['owner_design_approval']['owner'],'runtime_content_review':q['owner_design_approval']['runtime_content_review']},'recipe_id':q['recipe_id'],'recipe_version':q['recipe_version'],'selection_id':q['selection_id'],'branch_id':q['branch_id'],'blooms_level':q['blooms_level'],'classification_version':q['classification_version'],'objective_ids':deepcopy(q['objective_ids']),'demand_ids':deepcopy(q['demand_ids']),'parts':[{'part_id':p['part_id'],'reviewed_part':_teacher_metadata(p['reviewed_part'])}for p in q['parts']],'examination_references':display_references(q)}
