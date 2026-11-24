"""Build native metadata and prepared SVGs from approved design + Stage-E groups.

Uses the existing yyeni_workbench_tools builder for immutable candidates.
No registry installation, source acquisition or application mutation.
"""
import hashlib,importlib,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];WB=ROOT/'work/nam-8227-nsscas-2026/workbench';S=WB/'source';P=WB/'planning'
def read(p):return json.loads(p.read_text())
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load_source(root=S,name='_wb8227_author'):
 spec=importlib.util.spec_from_file_location(name,root/'__init__.py',submodule_search_locations=[str(root)]);module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
 return importlib.import_module(name+'.provider')
def runtime_spec(value):
 """Clarify approved authority without changing a criterion condition or its ID."""
 if isinstance(value,dict):
  result={key:runtime_spec(item)for key,item in value.items()}
  if isinstance(result.get('qualifiers'),list):
   result['qualifiers']=[x for x in result['qualifiers']if x!='D4 proposed clarification; final-manifest approval pending']
  if result.get('criterion_id_rule'):
   result['criterion_id_rule']='Literal approved criterion IDs use design/rubric version 0.1.4; runtime implementation version is separate. Do not reconstruct IDs from the runtime version.'
  if result.get('criterion_id')=='WB8227-trapezium-sketch-estimate:d:DB1':
   result['required'] += " Unambiguous concavity shorthand for the same own curve can establish the geometry; 'increasing' alone cannot."
  return result
 if isinstance(value,list):return [runtime_spec(x)for x in value]
 if isinstance(value,str):
  return value.replace('apply the proposed MR03 operational ledger, pending exact-manifest approval','apply the owner-approved MR03-OPS-D4 operational ledger')
 return value

def runtime_references(references):
 result=json.loads(json.dumps(references))
 for r in result:
  if r.get('learner_label','')and r['learner_label'].startswith('Gradient part: same type as '):
   r['learner_label']='Same type as '+r['learner_label'].split('Gradient part: same type as ',1)[1]
 return result

def build():
 S.mkdir(exist_ok=True);(S/'__init__.py').write_text('"""NSSCAS Mathematics 8227 reviewed-design candidate resources."""\n')
 (S/'groups/__init__.py').write_text('"""Subject recipe groups; common provider owns transport and seed selection."""\n')
 provider=load_source();choices=provider.all_choices()
 assert len(choices)==14 and len({c['recipe_id']for _,c in choices})==9
 recipe_sources={r['recipe_id']:f for f in ('calculus-design.json','trig-model-design.json','visual-design.json')for r in read(P/f)['recipes']}
 recipes={r['recipe_id']:r for f in ('calculus-design.json','trig-model-design.json','visual-design.json')for r in read(P/f)['recipes']}
 rows=[];native=[];assets={};rawcounts={}
 for module,c in choices:
  recipe=recipes[c['recipe_id']];branch=next(b for b in recipe['branches']if provider.norm_branch(b['branch_id'])==provider.norm_branch(c['branch_id']))
  parts=runtime_spec(branch['part_specs'])
  for part in parts:
   local=part.get('local_part_id',part['part_id'].rsplit(':',1)[-1]);part['qualified_part_id']=c['recipe_id']+':'+provider.norm_branch(c['branch_id'])+':'+local
  marks=sum(s['marks']for s in parts)
  levels=[s['bloom']['level']if isinstance(s['bloom'],dict)else s['bloom']for s in parts]
  objectives=sorted({o for p in parts for o in p['directly_assessed_objective_ids']});demands=sorted({d for p in parts for d in p['directly_assessed_demand_ids']})
  descriptor={'id':c['selection_id'],'recipeId':c['recipe_id'],'recipeVersion':provider.TRANSPORT_REVISION,'title':branch.get('display_title',recipe['title']),'topic':'NSSCAS Mathematics 8227','topicKey':c['recipe_id'],'objectiveIds':objectives,'demandIds':demands,'marks':marks,'minMarks':marks,'maxMarks':marks,'availability':'available','renewal':'finite','state':'candidate','reviewStatus':'Stage-D design approved; Stage-E authoring awaits independent content review'}
  rows.append({'public':descriptor})
  native.append(dict(selection_id=c['selection_id'],recipe_id=c['recipe_id'],recipe_version=provider.VERSION,design_rubric_version=provider.RUBRIC_VERSION,branch_id=c['branch_id'],title=branch.get('display_title',recipe['title']),objective_ids=objectives,demand_ids=demands,part_specs=parts,blooms_level=max(levels),classification_version='8227-pilot-design-0.1.1',examination_references=runtime_references(branch.get('examination_references',[])),raw_generated_capacity=len(c['parameters']),strict_complete_fresh_upper_bound=c.get('strict_complete_fresh_bound',c.get('strict_fresh_upper_bound')),approved_capacity=branch.get('capacity'),approved_domain=branch.get('domain',{'parameter_record':str((P/recipe_sources[c['recipe_id']]).relative_to(ROOT)),'branch_id':branch['branch_id']}),capacity_metadata={k:v for k,v in branch.items()if any(word in k for word in ('capacity','fresh','semantic','root_classes'))},required_response_formats=sorted({part['response_format']for part in parts}),native_marking_schema='8227-marking-evidence-v1',requires_app_acceptance=True,state='candidate',design_approval='approved exact Stage-D manifest; stored proposal-status text is historical evidence'))
  rawcounts[c['selection_id']]=len(c['parameters'])
  assert c['parameters'] and len({provider.digest(x)for x in c['parameters']})==len(c['parameters'])
  for params in c['parameters']:
   q=module.build(c['recipe_id'],c['branch_id'],params)
   for asset in q.get('assets',[]):
    svg=asset['svg'].encode();h=hashlib.sha256(svg).hexdigest();path='assets/'+h+'.svg';target=S/path;target.parent.mkdir(exist_ok=True);target.write_bytes(svg)
    if h not in assets:assets[h]=dict(path=path,sha256=h,roles=[],mime_type='image/svg+xml',authorship='newly authored from generated parameters')
    if asset['role']not in assets[h]['roles']:assets[h]['roles'].append(asset['role']);assets[h]['roles'].sort()
  # Domain validation must finish before publishing any descriptor for that choice.
 dump(S/'recipes.json',rows);dump(S/'catalogue-native.json',native);dump(S/'asset-index.json',dict(sorted(assets.items())))
 live=set('assets/'+h+'.svg'for h in assets)
 for path in (S/'assets').glob('*.svg'):
  if path.relative_to(S).as_posix()not in live:path.unlink()
 approval=read(P/'approvals/stage-d-4a054832/approval.json')
 dump(S/'provenance.json',dict(schema='8227-stage-e-provenance-v1',package_id='namibia-nsscas-8227',curriculum={'board':'NIED','qualification':'NSSCAS','subject':'Mathematics','syllabus_code':'8227','edition':'December 2020','grade':'12'},approved_design_manifest_sha256=approval['manifest_sha256'],approved_content_digest=approval['content_digest'],owner='Vitalis',approval_date=approval['date'],runtime_content_review='pending; same-vendor author checks do not accept content',textbook_originals_learner_display=False,source_design_files={str((P/f).relative_to(ROOT)):sha(P/f)for f in ('calculus-design.json','trig-model-design.json','visual-design.json','part-evidence-register.json')},authorship='Codex AUTHOR with three parallel same-vendor author assistants',reuse='Purpose-built original instances; no Flashcard Studio input bank',transport_version_map={str(provider.TRANSPORT_REVISION):provider.VERSION},prior_immutable_transport={'1':{'native_version':'0.1.4','candidate':'fcd4b71e07baa07a','manifest_sha256':'7022ea5049b0f5b02452828d5226f0a533816873f20d551186925e8aacacb250'}},design_rubric_version=provider.RUBRIC_VERSION,raw_generated_counts=rawcounts))
 rules_text=(WB/'subject-rules.md').read_text()
 dump(S/'subject-rules.json',dict(schema='8227-subject-rules-v1',curriculum='NIED NSSCAS Mathematics 8227 December 2020',design_manifest_sha256=approval['manifest_sha256'],authority='Vitalis approved exact Stage-D rubric, including MR03-OPS-D4',historical_rules_text=rules_text,mr03='Approved MR03-OPS-D4: determine eligibility for the connected question at first use of each datum. Genuine unchanged-object/unchanged-difficulty misreads permit A/B follow-through and one A/B deduction per datum; M/DM remain normal. This overrides not-F.T./cao for eligible misreads, but never MR09 supplied-result proof or OD-1 method requirements. Record gross evidence before net deduction; dependencies use gross evidence.',runtime_marking_limit='Frozen rubric/evidence only. Raw handwritten, photographed, sketch or free-text responses require trusted application marking orchestration. Competing-datum settlement and alternative implicit routes remain E/F carries.',d41_notes={'d41-01':'Implicit gradient finite AND nonzero','d41-02':'Nonunit exponential chain-factor eligibility guard is approved MR03-OPS-D4','d41-03':'Exposure keys persist across output-affecting revisions; version is provenance','d41-04':'Stage E active after exact owner approval','d41-05':'MR09 limit is adjacent to the eligible-misread override in this runtime summary'}))
 compositions=read(P/'d4/deck-compositions.json')['current'];decks=[]
 for name,entries in compositions.items():
  selections=[next(n['selection_id']for n in native if n['recipe_id']==rid and provider.norm_branch(n['branch_id'])==slug)for rid,slug in entries]
  total=sum(next(r['public']['marks']for r in rows if r['public']['id']==key)for key in selections)
  decks.append({'composition_id':'8227:pilot:'+name,'selection_ids':selections,'marks':total,'scope':'unassigned representative composition; application owns deck creation and assignment'})
 assert [d['marks']for d in decks]==[19,20,17]
 dump(S/'deck-compositions.json',decks)
 definition=dict(package_id='namibia-nsscas-8227',version=provider.VERSION,curriculum=read(S/'provenance.json')['curriculum'],provider_entrypoint='provider:create_provider',requires=['whole-question-v1','prepared-assets-v1','portable-objectives-v1'],dependency_versions={},coverage={'approved_stage_d_counts':read(P/'pilot-design.json')['counts'],'stage_e_authored_recipes':9,'stage_e_choices':14,'release_approved':False})
 dump(WB/'package-definition.json',definition)
 result=dict(status='pass',recipes=9,choices=len(rows),assessed_part_slots=sum(len(n['part_specs'])for n in native),branch_marks=sum(r['public']['marks']for r in rows),generated_parameter_rows=sum(rawcounts.values()),prepared_assets=len(assets),native_versions=[provider.VERSION],bridge_integer_revision=provider.TRANSPORT_REVISION,state='candidate',raw_counts=rawcounts)
 dump(WB/'checks/stage-e/source-build.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':build()
