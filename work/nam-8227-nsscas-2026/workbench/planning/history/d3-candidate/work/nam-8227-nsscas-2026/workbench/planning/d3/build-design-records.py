"""Derive Stage-D review records from authored designs. Never creates runtime items."""
import copy,hashlib,json,collections
from pathlib import Path
W=Path(__file__).resolve().parents[2];P=W/'planning';ROOT=W.parents[2]
NAMES=['visual-design.json','calculus-design.json','trig-model-design.json']
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
recipes=[];parts=[];choices=[]
for name in NAMES:
 for rr in read(P/name)['recipes']:
  r=copy.deepcopy(rr);rid=r['recipe_id'];slug=rid.removeprefix('WB8227-');version=r.get('version',r.get('proposed_version'));assert version=='0.1.3',(rid,version);r['version']=version;r['proposed_version']=version;r['origin_design_input']='planning/'+name;r['origin_design_input_sha256']=sha(P/name)
  r['work_order_path']='work-orders/'+rid+'.md';r['exemplar_path']='exemplars/'+rid+'.md';r['selection_ids']=[]
  for b in r['branches']:
   bs=b['branch_id'].split(':')[-1];qb=rid+':'+bs;sid='8227:D:SEL:'+slug+':'+bs
   b.update(qualified_branch_id=qb,choice_id=sid,selection_id=sid,classification_version='8227-pilot-design-0.1.1');r['selection_ids'].append(sid)
   for part in b['part_specs']:
    local=part.get('local_part_id',part['part_id'].split(':')[-1]);qp=qb+':'+local;bl=part['bloom'];level=bl['level']if isinstance(bl,dict)else bl
    criteria=part.get('bloom_criterion_ids',part.get('fully_qualified_criterion_ids',part.get('criterion_ids',bl.get('criterion_ids',[])if isinstance(bl,dict)else [])))
    rationale=part.get('bloom_rationale',bl.get('rationale')if isinstance(bl,dict)else None)
    primary=part.get('primary_objective_id',part.get('primary_assessed_objective_id'));assert primary in part['directly_assessed_objective_ids'],(qp,primary)
    assert rationale and criteria,(qp,'missing part rationale/criteria')
    part.update(qualified_part_id=qp,local_part_id=local,proposed_bloom_level=level,primary_objective_id=primary,other_directly_assessed_objective_ids=[o for o in part['directly_assessed_objective_ids']if o!=primary],bloom_rationale=rationale,bloom_criterion_ids=criteria,classification_version='8227-pilot-design-0.1.1')
    parts.append(dict(recipe_id=rid,version=version,branch_id=bs,part_id=local,qualified_part_id=qp,primary_objective_id=primary,other_directly_assessed_objective_ids=part['other_directly_assessed_objective_ids'],directly_assessed_demand_ids=part['directly_assessed_demand_ids'],conditional_directly_assessed_demand_ids=part.get('conditional_directly_assessed_demand_ids',{}),conditional_other_directly_assessed_objective_ids=part.get('conditional_other_directly_assessed_objective_ids',{}),prerequisite_demand_ids=part.get('prerequisite_demand_ids',[]),proposed_bloom_level=level,criterion_ids=criteria,rationale=rationale,marks=part['marks'],response_format=part['response_format'],misread_policy=part['misread_policy'],classification_version='8227-pilot-design-0.1.1',status='D3 proposal; Claude confirmation then Vitalis approval pending',evidence=r['work_order_path']))
   b['marks_total']=sum(q['marks']for q in b['part_specs']);b['proposed_whole_bloom']=max(q['proposed_bloom_level']for q in b['part_specs']);assert b['proposed_whole_bloom']==b.get('whole_bloom',b.get('whole_card_bloom'))
   if 'capacity_analysis'in b:
    ca=b['capacity_analysis'];raw=ca['admitted_raw_count'];sem=ca['semantic_task_count'];fresh=ca.get('strict_generated_fresh_capacity',ca['strict_all_assessed_parts_unseen_capacity'])
   elif rid.endswith('implicit-normal')or rid.endswith('stationary-inflexion'):
    raw=b['raw_capacity'];sem=b['part_semantic_capacities'];fresh=b['strict_complete_fresh_bound']
   elif rid.endswith('motion-integration'):
    raw=b['capacity'];sem=b['semantic_capacity'];fresh=sem['fresh_whole_upper_bound']
   elif rid.endswith('principal-inverse'):
    raw=b['raw_parameter_count'];sem=b['semantic_capacity'];fresh=sem
   elif rid.endswith('trig-rform-equation'):
    raw=b['capacity'];sem=b['capacity_detail'];fresh=sem['unseen_complete_cards_upper_bound_before_shared_part_exposure']
   elif bs=='graph-intercept':raw=b['presentation_count'];sem=b['capacity'];fresh=sem
   else:raw=b['capacity'];sem=b['semantic_capacity_by_part'];fresh=sem['t-parameter_model_prompts']
   b['capacity_record']=dict(admitted_parameter_presentations=raw,semantic_contexts=sem,strict_wholly_fresh_upper_bound=fresh,rule='Not a count of distinct reasoning types. All assessed part-instance keys and shared exposure must be unexposed; repeat practice may be labelled after-feedback. Raw counts are not freshness guarantees.')
   choices.append(dict(recipe_id=rid,branch_id=qb,selection_id=sid,marks=b['marks_total'],bloom=b['proposed_whole_bloom'],**b['capacity_record']))
  recipes.append(r)
unconditional={x for p in parts for x in p['directly_assessed_demand_ids']};conditional={x for p in parts for v in p['conditional_directly_assessed_demand_ids'].values()for x in v};objs={x.rsplit(':D',1)[0]for x in unconditional|conditional}
counts=dict(objectives_with_unconditional_facets=len({x.rsplit(':D',1)[0]for x in unconditional}),objectives_with_conditional_only_facets=len(objs-{x.rsplit(':D',1)[0]for x in unconditional}),recipes=len(recipes),branch_choices=len(choices),paper_exemplar_cases=3*len(choices),assessed_part_slots=len(parts),unconditional_direct_demand_facets=len(unconditional),conditional_only_direct_demand_facets=len(conditional-unconditional),content_demands_with_direct_facets=len(unconditional|conditional),objectives_with_direct_facets=len(objs),content_demands_outside_direct_pilot=138-len(unconditional|conditional),whole_choice_bloom_counts={str(k):v for k,v in sorted(collections.Counter(c['bloom']for c in choices).items())},runtime_recipes=0,runtime_instances=0,approved_choices=0)
reg=dict(subject='NSSCAS Mathematics 8227',edition='NIED December 2020',owner='Vitalis',date='2026-11-24',status='D3 proposed; changed-scope confirmation then owner approval',authority='Derived only from the three authored design JSONs; work orders explain criteria and any named source deviations.',parts=parts,limits='Part labels remain proposed. Conditional objective/demand links apply only in the specified case. Source item mappings are unchanged.')
dump(P/'part-evidence-register.json',reg)
lines=['# Part evidence register — D3','','Each row cites only that part’s criterion IDs. Conditional links are additional and are not inherited by instances that omit the condition. All labels await Claude short check and Vitalis approval.','','| Part | Primary; other direct objectives | Direct demands; conditional | Prerequisites and role | Marks; Bloom; criteria; rationale |','|---|---|---|---|---|']
for p in parts:
 lines.append('| '+p['qualified_part_id']+' | '+p['primary_objective_id']+'; '+', '.join(p['other_directly_assessed_objective_ids'])+' | '+', '.join(p['directly_assessed_demand_ids'])+('; conditional '+json.dumps(p['conditional_directly_assessed_demand_ids'])if p['conditional_directly_assessed_demand_ids']else'')+' | '+json.dumps(p['prerequisite_demand_ids'],ensure_ascii=False)+' | '+str(p['marks'])+'; '+str(p['proposed_bloom_level'])+'; '+', '.join(p['criterion_ids'])+'; '+p['rationale'].replace('|','\\|')+' |')
lines += ['', 'Every part carries OD-6 misread_policy in the JSON; genuine unchanged-difficulty question-data misreads use one first-use A/B deduction and A/B follow-through. OD-1, correct working and named exclusions remain applicable.']
(P/'part-evidence-register.md').write_text('\n'.join(lines)+'\n')
merged=dict(subject='NSSCAS Mathematics 8227',curriculum_id='nam-8227-nsscas-dec2020',owner='Vitalis',role='PLANNER',date='2026-11-24',version='0.1.3',status='D3 design candidate; Claude changed-scope confirmation then Vitalis approval pending',normalisation='Derived merge preserves authored branch/part IDs; explicit qualified IDs are independent of display order. Design choice IDs use 8227:D:SEL:<recipe-slug>:<branch>. Not a runtime provider schema.',inputs={n:sha(P/n)for n in NAMES},counts=counts,recipes=recipes,capacity_rule='Raw presentations, task contexts, reasoning/outcome classes and strict fresh bounds are distinct; never sum them as a global bank capacity.',part_evidence_register='planning/part-evidence-register.json',part_evidence_register_sha256=sha(P/'part-evidence-register.json'))
dump(P/'pilot-design.json',merged);dump(P/'d3/choice-capacities.json',dict(counts=counts,choices=choices))
print(json.dumps(counts,indent=2))
