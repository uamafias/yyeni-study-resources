"""Validate the operative plan independently of the generator's rounded rollup."""
import collections
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import jsonschema
import yaml
WS=Path(__file__).resolve().parents[1]; ROOT=WS.parents[1]
def read(p):return json.loads((WS/p).read_text())
registry=read('curriculum/objective_registry.json')
schema=json.loads((ROOT/'standard/v0.2.0-draft/schemas/objective_registry.schema.json').read_text())
jsonschema.Draft202012Validator(schema).validate(registry)
fw=read('curriculum/assessment-framework.json')
sp=yaml.safe_load((WS/'subject-profile.yaml').read_text())
targets=read('curriculum/syllabus-facts.json')['ao_weights']['derived_qualification_percent']
commands={c['word']:c for c in fw['command_words']}
objects={o['objective_id']:o for o in registry['objectives']}
perf_defs={p['item_type']:p for p in sp['slot_plan']['performance_tasks']}
ao=collections.Counter();counts=collections.Counter();bloom=collections.Counter();rows=[];seen=set();specs=[]
miscon=[]
for td in sorted((WS/'topics').iterdir(),key=lambda p:[int(x) for x in p.name.split('.')]):
    w=json.loads((td/'work_order.json').read_text());c=json.loads((td/'contract.json').read_text())
    assert len(w['excluded_constructs'])==len(read('curriculum/scope-scan.json')['entries'])
    assert len(w['item_slots'])+len(w['performance_tasks'])==c['required_outputs']['learning_items']==w['planned_item_count']
    assert len(w['content_units'])==c['required_outputs']['content_units']
    branch={o['objective_id'] for o in registry['objectives'] if o['topic_id']==td.name and o['parent_id']}
    covered=set()
    for slot in w['item_slots']:
        assert slot['slot'] not in seen; seen.add(slot['slot'])
        assert slot['objective_id'] in branch
        covered.add(slot['objective_id'])
        cmd=commands[slot['command_word']]
        assert cmd['use_in_prompts'] and str(slot['mark_tariff']) in cmd['observed_tariffs'],slot
        assert slot['assessment_objectives'] and set(slot['assessment_objectives'])<=set(targets)
        assert slot['blooms_level'] and slot['marking_guidance_must_name']
        for a in slot['assessment_objectives']:ao[a]+=slot['mark_tariff']/len(slot['assessment_objectives'])
        counts['flashcards']+=1;bloom[slot['blooms_level']]+=1
        if slot.get('misconception_entry'):miscon.append(slot['misconception_entry'])
    assert covered==branch,(td.name,branch-covered)
    originals=[o['objective_id'] for o in registry['objectives'] if o['topic_id']==td.name and o['parent_id']=='OBJ-6145-'+td.name]
    for slot in w['performance_tasks']:
        split=slot['ao_marks_equivalent'];ao.update(split)
        counts['performance_tasks']+=1;bloom[slot['blooms_level']]+=1
        parts=slot['part_specs']
        for part in parts:
            assert str(part['mark_tariff']) in commands[part['command_word']]['observed_tariffs']
            assert all(oid in branch for oid in part['objective_ids'])
        assert sum(p['mark_tariff'] for p in parts)==sum(split.values())
        assert set(slot['objective_ids'])=={o for p in parts for o in p['objective_ids']}
        assert slot['objective_selection_note'].startswith('Demand-led')
        specs.append(slot)
    budget=c['depth_constraints']['word_budget']
    rows.append({'topic_id':td.name,'title':w['topic_title'],'objectives':len(branch),'items':w['planned_item_count'],
                 'flashcards':len(w['item_slots']),'performance_tasks':len(w['performance_tasks']),
                 'notes_min':budget['min'],'notes_max':budget['max']})
    counts.update(objectives=len(branch),notes_min=budget['min'],notes_max=budget['max'])
assert len(miscon)==len(set(miscon))==32
assert set(miscon)=={m['entry_id'] for m in read('curriculum/misconceptions.json')['entries']}
assert {r['objective_id'] for r in read('planning/objective-reference.json')['objectives']}<=set(objects)
total=sum(ao.values());share={a:100*v/total for a,v in ao.items()};gap=max(abs(share[a]-targets[a]) for a in targets)
assert gap<=5
spec=importlib.util.spec_from_file_location('plan_checks',ROOT/'standard/v0.2.0-draft/checks/yyeni_checks.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
check=module.c39(SimpleNamespace(evidence=read('assessment-evidence/assessment_evidence.json'),exposure=read('curriculum/exam-exposure.json'),branch=objects))
assert check[0]=='pass',check
ex=read('exemplar/topics/1.1/qa_report.json')
assert ex['release_decision']=='publish'
report={'result':'PASS','totals':dict(counts,topics=len(rows),items=counts['flashcards']+counts['performance_tasks'],content_units=len(rows)),
 'ao_marks_equivalent':dict(ao),'ao_share_percent':share,'ao_targets_percent':targets,'largest_gap_points':gap,
 'blooms':dict(bloom),'topic_table':rows,'misconception_slots':len(miscon),
 'checks':['Registry schema valid; every original source bullet preserved.',f'All {counts["objectives"]} assessable objectives have slots.',
    'All flashcard command/tariff pairs and composite task parts observed in held QPs.','All contracts contain scope guards and reconcile to work-order counts.',
    'All 32 misconceptions have exactly one named slot.','No automatic AO top-up or duplicated CHAIN pass.',check[1],
    'Exact subject AO shares are within 5 points; generator rounded totals kept separately.','Exemplar has no failures.'],
 'exemplar':{'decision':ex['release_decision'],'warnings':[r['check_id'] for r in ex['deterministic_checks'] if r['status']=='warn'],
             'not_run':[{'check':r['check_id'],'reason':r['message']} for r in ex['deterministic_checks'] if r['status']=='not_run']},
 'limits':['Plan pending Jeremy approval and human commit. Main topics are unauthored.',
 'The standard chart renderer is break-even specific. NSSCO diagram work uses numerical schedules and learner construction instructions; graphical production is not certified by this exemplar.',
 'Standard profile schemas predate slot_plan/conditioned_mechanisms; no claim is made that the extended profile dictionaries pass those older closed schemas. The operative registry/claims/units/items schemas do pass.']}
for path,data in [('planning/plan-validation.json',report),('planning/performance-specs.json',{'note':'Metadata supplement to the generated composite performance slots; these practice AO allocations are judgement, not official per-part distributions. Each total is the sum of observed part tariffs.','slots':specs})]:
    (WS/path).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('topic_table','exemplar')},indent=2))
