#!/usr/bin/env python3
"""Apply/check explicit per-slot demand decisions; preserve every slot and tariff.

Run after the standard work-order build, before budget application/exemplar/docs.
No standard files are changed. --check only verifies, including the exact rollup.
"""
import collections
from fractions import Fraction
import json
from pathlib import Path
import sys

WS = Path('work/nam-6116-nssco-2026')
sys.path.insert(0, 'standard/v0.2.0-draft/build')
import make_work_order as shared
audit = json.loads((WS/'planning/ao_demand_audit.json').read_text())
decisions = {s['slot']: s for s in audit['records']}
label_review = json.loads((WS/'planning/post_authoring_label_decisions.json').read_text())
label_decisions = {s['slot']: s for s in label_review['decisions']}
assert len(label_decisions) == len(label_review['decisions'])
check = '--check' in sys.argv
seen, all_tot, rows = set(), collections.Counter(), []
for t in range(1, 6):
    p = WS/f'topics/{t}/work_order.json'
    wo = json.loads(p.read_text())
    totals = collections.Counter()
    for s in wo['item_slots']:
        d = decisions[s['slot']]
        label = label_decisions.get(s['slot'])
        for k in ('objective_id', 'objective_title', 'subtype', 'mark_tariff'):
            assert s[k] == d[k], (s['slot'], k, 'audit stale; re-review changed demand')
        for k in ('command_word', 'blooms_level'):
            before = label['previous'][k] if label else d[k]
            after = label['decided'][k] if label else d[k]
            assert before == d[k], (s['slot'], k, 'label decision does not match plan baseline')
            assert s[k] == (after if check else before), (s['slot'], k, 'label decision stale')
        if label:
            assert label['previous']['assessment_objectives'] == d['assessment_objectives'], s['slot']
        seen.add(s['slot'])
        annotation = {k: d[k] for k in ('rule', 'status', 'planned_demand', 'condition')}
        if label:
            annotation['post_authoring_label_review'] = {'source': label['source'], 'reason': label['reason']}
        final_ao = label['decided']['assessment_objectives'] if label else d['assessment_objectives']
        if check:
            assert s['assessment_objectives'] == final_ao, s['slot']
            assert s.get('ao_demand') == annotation, s['slot']
        else:
            s['assessment_objectives'] = final_ao
            s['command_word'] = label['decided']['command_word'] if label else d['command_word']
            s['blooms_level'] = label['decided']['blooms_level'] if label else d['blooms_level']
            s['ao_demand'] = annotation
        for a in s['assessment_objectives']:
            totals[a] += Fraction(s['mark_tariff'], len(s['assessment_objectives']))
    for task in wo['performance_tasks']:
        label = label_decisions.get(task['slot'])
        if label:
            assert label['previous']['blooms_level'] == 'Analyse' and label['decided']['blooms_level'] == 'Apply', task['slot']
            assert task['blooms_level'] == ('Apply' if check else 'Analyse'), task['slot']
            if not check:
                task['blooms_level'] = 'Apply'
            seen.add(task['slot'])
        split = {'multiple_choice_set': {'AO1': Fraction(15, 2), 'AO2': Fraction(9, 2)},
                 'short_answer': {'AO1': 5, 'AO2': 3}, 'practical_task': {'AO3': 10}}[task['item_type']]
        totals.update(split)
    total = sum(totals.values())
    expected = {a: round(100 * totals[a] / total) for a in ('AO1', 'AO2', 'AO3')}
    counts = collections.Counter(a for s in wo['item_slots'] for a in s['assessment_objectives'])
    count_mix = {a: round(100 * counts[a] / sum(counts.values())) for a in expected}
    if check:
        assert wo['marks_equivalent_total'] == total
        assert all(wo['planned_ao_mix_by_marks'][a]['planned_share_percent'] == expected[a] for a in expected)
        assert all(wo['planned_ao_mix_by_item_count'][a]['planned_share_percent'] == count_mix[a] for a in expected)
    else:
        for a, value in expected.items():
            wo['planned_ao_mix_by_marks'][a]['planned_share_percent'] = value
            wo['planned_ao_mix_by_item_count'][a]['planned_share_percent'] = count_mix[a]
        wo['marks_equivalent_total'] = int(total)
        wo['ao_demand_audit_source'] = 'planning/ao_demand_audit.json and planning/post_authoring_label_decisions.json (demand-based decisions)'
        p.write_text(json.dumps(wo, indent=1, ensure_ascii=False)+'\n')
        md = shared.as_markdown(wo)
        md += '\n\n## Mandatory AO demand decisions\n\nLabels follow `planning/ao_demand_audit.json` and the later demand-based decisions in `planning/post_authoring_label_decisions.json`; read the per-slot `ao_demand` in work_order.json. B requires genuine information handling or reasoning; supplied data or unfamiliar context are not universal prerequisites. Practical C requires a practical demand. The post-authoring decisions were made against the actual prompts and are not a quota adjustment.\n'
        (p.parent/'work_order.md').write_text(md)
    all_tot.update(totals)
    rows.append({'topic': str(t), 'marks': {a: str(totals[a]) for a in expected},
                 'items': wo['planned_item_count']})
assert set(decisions) <= seen, 'audit contains missing slots'
assert set(label_decisions) <= seen, 'label decision names a missing slot'
grand = sum(all_tot.values())
result = {'basis': 'unrounded sum of slot tariffs plus explicit performance-task planning assumptions',
          'rule_status': 'Full plan approved by Lotto, 2026-10-18; post-authoring demand-based label decisions applied; breastfeeding/standard-ratio boundaries retained', 'total_marks': str(grand),
          'marks': {a: str(all_tot[a]) for a in ('AO1', 'AO2', 'AO3')},
          'shares_percent': {a: float(100 * all_tot[a] / grand) for a in ('AO1', 'AO2', 'AO3')},
          'topics': rows,
          'slots_changed': sum(d['previous_assessment_objectives'] != (label_decisions[d['slot']]['decided']['assessment_objectives'] if d['slot'] in label_decisions else d['assessment_objectives']) for d in decisions.values()),
          'ambiguous_slots': [d['slot'] for d in decisions.values() if d['status'].startswith('ambiguous')],
          'counts_by_status': dict(collections.Counter(d['status'] for d in decisions.values()))}
rp = WS/'curriculum/ao-demand-rollup.json'
if check:
    assert json.loads(rp.read_text()) == result, 'exact AO rollup stale'
else:
    rp.write_text(json.dumps(result, indent=2)+'\n')
    rs, sh, sy, mi, gr = shared.subject_rollup(str(WS), [str(t) for t in range(1, 6)])
    shared.write_rollup(str(WS), rs, sh, sy, mi, gr)
print(('AO demand check PASS: ' if check else 'AO demand applied: ') + json.dumps(result))
