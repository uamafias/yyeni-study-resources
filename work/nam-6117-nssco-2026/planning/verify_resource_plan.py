"""Recompute structural planning gates; no claim of exhaustive semantic review."""
import json,re,subprocess
from collections import Counter,defaultdict
from pathlib import Path
import jsonschema,yaml
W=Path(__file__).resolve().parents[1];R=W.parents[1]
def read(p):return json.loads(p.read_text())
checks=[]
def check(name,condition,detail=''):
 checks.append({'check':name,'passed':bool(condition),'detail':detail})
for name,path in [('qualification_profile','qualification-profile.yaml'),('subject_profile','subject-profile.yaml'),('objective_registry','curriculum/objective_registry.json')]:
 d=yaml.safe_load((W/path).read_text()) if path.endswith('yaml') else read(W/path)
 errors=list(jsonschema.Draft202012Validator(read(R/f'standard/v0.2.0-draft/schemas/{name}.schema.json')).iter_errors(d))
 check(name+' schema',not errors,'; '.join(e.message for e in errors))
reg=read(W/'curriculum/objective_registry.json')['objectives'];ids={o['objective_id'] for o in reg};leaf={o['objective_id']:o for o in reg if o['parent_id']}
source=read(W/'curriculum/syllabus-outcomes.json');mapped=read(W/'curriculum/objective-source-map.json')['objectives']
check('309 source outcomes mapped',len(source['outcomes'])==309 and {o['outcome_id'] for o in source['outcomes']}<={m['source_outcome_id'] for m in mapped})
check('418 leaves source mapped',set(leaf)=={m['objective_id'] for m in mapped})
pages=subprocess.check_output(['pdftotext','-layout',str(R/source['source']),'-'],text=True).split('\f')
missing=[]
for o in source['outcomes']:
 for line in o['source_lines']:
  if line['verbatim_line'] not in pages[line['pdf_page']-1]:missing.append(o['outcome_id'])
check('All retained syllabus lines on exact cited pages',not missing,str(sorted(set(missing))))
orders=[read(p) for p in (W/'topics').glob('*/work_order.json')];slots=[s for o in orders for s in o['item_slots']];tasks=[t for o in orders for t in o['performance_tasks']]
fw=read(W/'curriculum/assessment-framework.json');cw={c['word']:c for c in fw['command_words']};evidence=read(W/'assessment-evidence/assessment_evidence.json')['records'];ev={e['evidence_id']:e for e in evidence}
check('Step 3 evidence totals',len(evidence)==725 and sum(e['evidence_type']=='past_paper' for e in evidence)==691 and sum(e['mark_tariff'] or 0 for e in evidence if e['evidence_type']=='past_paper')==960)
check('All leaves have card slots',set(leaf)=={s['objective_id'] for s in slots})
allowed=read(R/'standard/v0.2.0-draft/schemas/learning_items.schema.json')['properties']['items']['items']['properties']['subtype']['enum']
check('Card subtypes accepted by item schema',all(s['subtype'] in allowed for s in slots))
check('Every slot command/tariff observed',all(cw[s['command_word']]['use_in_prompts'] and s['mark_tariff'] in cw[s['command_word']]['observed_tariffs'] for s in slots))
check('Every tariff example resolves with matching command and marks',all(s['tariff_provenance']['evidence_ids'] and all(i in ev and ev[i]['command_word']==s['command_word'].lower() and ev[i]['mark_tariff']==s['mark_tariff'] for i in s['tariff_provenance']['evidence_ids']) for s in slots))
check('Every objective with an eligible opening has that command practised',all(any(s['objective_id']==oid and s['command_word'] in o['command_words'] for s in slots) for oid,o in leaf.items() if any(cw.get(c,{}).get('use_in_prompts') for c in o['command_words'])))
check('Define objectives have Define cards',all(any(s['objective_id']==oid and s['command_word']=='Define' for s in slots) for oid,o in leaf.items() if o['syllabus_text'].lower().startswith('define ')))
check('Objective-linked answer templates (not semantic credit validation)',all(s['answer_requirements']['assessed_target']==leaf[s['objective_id']]['learner_objective'] and s['marking_guidance_must_name'] for s in slots))
groups=defaultdict(list)
for s in slots:groups[(s['objective_id'],s['subtype'],s['command_word'],s['mark_tariff'])].append(s)
check('Repeated slot groups have distinct variant specifications',all(len({json.dumps(s['variant_spec'],sort_keys=True) for s in ss})==len(ss) for ss in groups.values()))
visuals={v['visual_id'] for v in read(W/'planning/visual-manifest.json')['visuals']}
check('Drawing slots retain visual requirements',all(s['required_visual_ids'] for s in slots if s.get('representation_task')))
check('Task scope and fixed parts',len(tasks)==36 and all(isinstance(t['objective_ids'],list) and set(t['objective_ids'])<=ids and t.get('context_brief') and t['mark_tariff']==sum(p['mark_tariff'] for p in t['parts']) and t['mark_tariff']==sum(t['ao_split'].values()) for t in tasks))
check('Task part commands, tariffs and credit requirements',all(((t['item_type']=='multiple_choice_set' and p['command_word'] is None and p['mark_tariff']==1) or (t['item_type']!='multiple_choice_set' and p['mark_tariff'] in cw[p['command_word']]['observed_tariffs'])) and p['credit_requirement'] and set(p['objective_ids'])<=ids for t in tasks for p in t['parts']))
check('MC demand is explicit and higher-order objectives are not labelled recall',all(p.get('planned_cognitive_demand') and p.get('blooms_level_basis') and (p['blooms_level']!='Remember' or leaf[p['objective_ids'][0]]['learner_objective'].lower().split()[0] in {'define','state','name','identify','recall','list','recognise'}) for t in tasks if t['item_type']=='multiple_choice_set' for p in t['parts']))
check('Required visuals resolve',all(set(x.get('required_visual_ids',[]))<=visuals for x in slots+tasks))
check('Every slot and task part has one Bloom label',all(x['blooms_level'] in ['Remember','Understand','Apply','Analyse','Evaluate','Create'] for x in slots+[p for t in tasks for p in t['parts']]))
m=read(W/'curriculum/misconceptions.json');check('19 misconceptions have diagnostic slots',len(m['records'])==len(m['entries'])==19 and {e['entry_id'] for e in m['entries']}=={s['misconception_entry'] for s in slots if s['subtype']=='MISCON'})
check('Volume conversion remediation explicitly planned',any('ER-6117-2022-19' in s.get('remediation_evidence_ids',[]) for s in slots))
p=read(W/'planning/practical-experiences.json')['experiences'];check('55 suggested practicals mapped',len(p)==55 and all(x['content_objective_ids'] and x['practical_skill_objective_ids'] and set(x['content_objective_ids']+x['practical_skill_objective_ids'])<=ids for x in p))
sc=read(W/'curriculum/scope-scan.json')['entries'];check('Scope guard examples enforce exclusions',all(all(re.search(x['pattern'],s) for s in x['must_catch']) and not any(re.search(x['pattern'],s) for s in x['must_allow']) for x in sc))
check('All contracts carry 12 exclusions',all(len(read(W/'topics'/o['topic_id']/'contract.json')['depth_constraints']['excluded_constructs'])==12 for o in orders))
marks=Counter()
for s in slots:
 for ao in s['assessment_objectives']:marks[ao]+=s['mark_tariff']/len(s['assessment_objectives'])
for t in tasks:marks.update(t['ao_split'])
total=sum(marks.values());shares={a:100*marks[a]/total for a in 'ABC'};gap=max(abs(shares[a]-v) for a,v in zip('ABC',[50,30,20]))
recall=sum(s['mark_tariff'] for s in slots if s['subtype'] in ['DEF','FEATURE'])+sum(p['mark_tariff'] for t in tasks for p in t['parts'] if p['blooms_level']=='Remember')
check('AO largest gap <= 5 points',gap<=5,str(shares));check('Recall mark estimate <=25%',100*recall/total<=25,f'{recall}/{total}')
check('No standard files changed',not subprocess.check_output(['git','diff','--name-only','--','standard/'],cwd=R,text=True).strip())
gate=read(W/'planning/semantic-review-gate.json')
check('Human semantic review gate lists all required specifications',set(gate['required_calculation_slot_ids'])=={s['slot'] for s in slots if s['subtype']=='CALC'} and set(gate['required_activity_ids'])=={t['slot'] for t in tasks} and set(gate['required_visual_ids'])==visuals, 'Inventory check only; does not grant approval.')
policy=read(W/'planning/recall-monitoring-policy.json')
check('Recall monitoring thresholds defined','topic_card_recall_review_trigger_percent' not in policy and policy['subject_recall_warning_percent']==24 and policy['subject_recall_ceiling_percent']==25)
practical=[t for t in tasks if t['item_type']=='practical_task']
check('All 12 practical activities have actual stimuli and expected answers',len(practical)==12 and all(t.get('stimulus_specification',{}).get('expected') and t['stimulus_specification'].get('accepted_ranges') and t['stimulus_specification'].get('apparatus_labels') for t in practical))
check('Graph points fit declared axes and have tolerances',all(len(g['x'])==len(g['y']) and all(g['x_range'][0]<=v<=g['x_range'][1] for v in g['x']) and all(g['y_range'][0]<=v<=g['y_range'][1] for v in g['y']) and g['point_tolerance_y']>0 for t in practical if (g:=t['stimulus_specification'].get('graph'))))
from practical_data import DATA
from math import isclose
m={k:v.get('measurements',{}) for k,v in DATA.items()};e={k:v['expected'] for k,v in DATA.items()}
g6=DATA['6']['graph'];g12=DATA['12']['graph']
titre=m['4']['final_burette_cm3']-m['4']['initial_burette_cm3'];amount=m['4']['acid_concentration_mol_dm3']*titre/1000
results=[(sum(m['1']['repeated_volumes_cm3'])/len(m['1']['repeated_volumes_cm3']),e['1']['mean_volume_cm3']),
 (m['3']['wet_mass_g']-m['3']['dry_mass_g'],e['3']['water_uptake_g']), (titre,e['4']['titre_cm3']), (amount,e['4']['HCl_mol']), (amount/(m['4']['aliquot_cm3']/1000),e['4']['NaOH_concentration_mol_dm3']),
 ((g6['y'][3]-g6['y'][1])/(g6['x'][3]-g6['x'][1]),e['6']['average_rate_cm3_s']),
 (m['9']['Mg_gas_cm3'][-1]/m['9']['time_s'][-1],e['9']['Mg_average_rate_cm3_s']), (m['9']['Zn_gas_cm3'][-1]/m['9']['time_s'][-1],e['9']['Zn_average_rate_cm3_s']),
 (m['10']['sample_spots_from_baseline_cm'][0]/m['10']['solvent_front_from_baseline_cm'],e['10']['sample_Rf'][0]), (m['10']['sample_spots_from_baseline_cm'][1]/m['10']['solvent_front_from_baseline_cm'],e['10']['sample_Rf'][1]),
 (m['11']['sample_A_final_burette_cm3']-m['11']['sample_A_initial_burette_cm3'],e['11']['A_soap_cm3']), (m['11']['sample_B_final_burette_cm3']-m['11']['sample_B_initial_burette_cm3'],e['11']['B_soap_cm3']),
 ((g12['y'][3]-g12['y'][1])/(g12['x'][3]-g12['x'][1]),e['12']['signed_rate_C_min'])]
check('Practical numerical answers independently recompute',all(isclose(a,b,rel_tol=1e-10,abs_tol=1e-10) for a,b in results))
vs=read(W/'planning/visual-manifest.json')['visuals']
check('All 35 visuals have concrete labels values and scientific criteria',len(vs)==35 and all(v.get('required_labels') and v.get('geometry_and_values') and v.get('scientific_acceptance_criteria') for v in vs))
check('Three unscaffolded free-response activities specified',len([t for t in tasks if t.get('response_format')=='free_response' and t.get('free_response_prompt') and t.get('learner_presentation')])==3)
check('Activity AO splits recompute from part demands',all(all(abs(sum(p['mark_tariff']/len(p['assessment_objectives']) for p in t['parts'] if ao in p['assessment_objectives'])-marks)<1e-9 for ao,marks in t['ao_split'].items()) for t in tasks))
check('MC fresh-quantity tasks are B and isotope discussion is not automatically Evaluate',all(('fresh supplied quantities' not in p['planned_cognitive_demand'] or p['assessment_objectives']==['B']) and (not p['content_target'].lower().startswith('discuss isotopes') or p['blooms_level']=='Understand') for t in tasks if t['item_type']=='multiple_choice_set' for p in t['parts']))
check('All full investigation design parts use Plan',all(p['command_word']=='Plan' for t in practical for p in t['parts'] if p.get('practical_criterion')=='C2' and p['blooms_level']=='Create'))
from scope_text import scope_view
example='use gas volumes (questions on the ideal gas law will not be set)'
clean=scope_view(example,[{'syllabus_text':example}])
check('Scope exclusions ignored only inside known objective titles','ideal gas law' not in clean and 'ideal gas law' in scope_view('Use the ideal gas law to calculate volume.',[{'syllabus_text':example}]))
check('Pre-production gate includes authored card samples',len(gate['authored_card_sample_gate']['required_planned_slot_ids'])==7 and len(gate['authored_card_sample_gate']['required_existing_exemplar_item_ids'])==2)
ex=read(W/'exemplar/topics/4/qa_report.json');check('Structural exemplar has no failed checks',not any(c['status']=='fail' for c in ex['deterministic_checks']))
report={'status':'pass' if all(c['passed'] for c in checks) else 'fail','scope':'Structural recomputation and source-line verification; semantic review of all planned items remains the human plan checkpoint.','counts':{'registry':len(reg),'assessable':len(leaf),'cards':len(slots),'activities':len(tasks),'items':len(slots)+len(tasks),'marks':total},'semantic_review_gate_status':gate['status'],'ao_marks':dict(marks),'ao_percent':shares,'recall_marks':recall,'recall_percent':100*recall/total,'checks':checks}
(W/'planning/plan-validation.json').write_text(json.dumps(report,indent=2)+'\n')
for c in checks:print(('PASS' if c['passed'] else 'FAIL'),c['check'],c['detail'] if not c['passed'] else '')
raise SystemExit(report['status']!='pass')
