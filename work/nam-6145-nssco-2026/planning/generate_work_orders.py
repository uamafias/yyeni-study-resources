"""Standard generation with topic-specific input projection; no standard edits."""
import copy
from collections import Counter
import json
import sys
from pathlib import Path
WS=Path(__file__).resolve().parents[1]; ROOT=WS.parents[1]
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/build'))
import make_work_order as standard
original_yaml=standard._yaml
profile=original_yaml(str(WS/'subject-profile.yaml'))
active_topic=None
def projected_yaml(path):
    data=profile if str(path).endswith('subject-profile.yaml') else original_yaml(path)
    if str(path).endswith('subject-profile.yaml'):
        data=copy.deepcopy(data)
        specs=data['slot_plan']['performance_tasks_by_topic'][active_topic]
        data['slot_plan']['performance_tasks']=[{'item_type':s['item_type'],'brief':s['brief'],'ao_split':s['ao_marks_equivalent']} for s in specs]
    return data
standard._yaml=projected_yaml
topics=sorted([p.name for p in (WS/'topics').iterdir()],key=lambda x:list(map(int,x.split('.'))))
for active_topic in topics:
    wo=standard.build(str(WS),active_topic)
    specs=profile['slot_plan']['performance_tasks_by_topic'][active_topic]
    for task,spec in zip(wo['performance_tasks'],specs):
        task.update({k:spec[k] for k in ('objective_ids','blooms_level','command_word','mark_tariff','part_specs','assessment_objectives','ao_marks_equivalent','objective_selection_note')})
    wo['ao_mix_note']='Balance against syllabus A/B/C weights by marks-equivalent, not item counts. Topic-specific demand and explicit composite part allocations govern practice. No automatic AO padding.'
    marks=Counter()
    for s in wo['item_slots']:
        for a in s['assessment_objectives']: marks[a]+=s['mark_tariff']/len(s['assessment_objectives'])
    for s in specs: marks.update(s['ao_marks_equivalent'])
    wo['marks_equivalent_total']=sum(marks.values())
    for a in wo['planned_ao_mix_by_marks']:
        wo['planned_ao_mix_by_marks'][a]['planned_share_percent']=round(100*marks[a]/sum(marks.values()))
    blooms=Counter(s['blooms_level'] for s in wo['item_slots']+wo['performance_tasks'])
    for level in wo['planned_blooms_mix']:
        wo['planned_blooms_mix'][level]={'items':blooms[level],'share_percent':round(100*blooms[level]/wo['planned_item_count'])}
    wo['generated_by']='standard make_work_order.build via planning/generate_work_orders.py; per-topic performance input projection and generated metadata'
    td=WS/'topics'/active_topic
    (td/'work_order.json').write_text(json.dumps(wo,indent=2,ensure_ascii=False)+'\n')
    markdown=standard.as_markdown(wo).replace('Limits the syllabus states, enforced by C-11','Planner depth boundaries, enforced by C-11')
    markdown=markdown.replace('## Owned by another topic\n\nName in passing if you must; teach there.','## Topic ownership and cross-links\n\nTeach the demand owned here; cross-link the distinct demand owned elsewhere.')
    (td/'work_order.md').write_text(markdown)
rows,share,syl,missing,grand=standard.subject_rollup(str(WS),topics)
standard.write_rollup(str(WS),rows,share,syl,missing,grand)
print('Generated',len(topics),'topic-specific work orders:',share)
