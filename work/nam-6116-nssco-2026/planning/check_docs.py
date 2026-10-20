#!/usr/bin/env python3
"""Consistency check across PLAN, HANDOVER, exemplar README and the files they describe. Exit 1 on any drift."""
import json, glob, re, sys
WS = 'work/nam-6116-nssco-2026'
plan, hand, readme = (open(f'{WS}/{f}').read() for f in
                      ('PLAN-6116-nssco-biology.md', 'HANDOVER-6116-nssco-biology.md', 'exemplar/README.md'))
units = [json.load(open(f)) for f in glob.glob(f'{WS}/exemplar/3/content-units/*.json')]
words = sum(u['word_count'] for u in units)
items = [i for t in '34' for i in json.load(open(f'{WS}/exemplar/{t}/learning-items/topic_{t}_items.json'))['items']]
kinds = {i['subtype'] or i['item_type'] for i in items}
bad = []
if '{:,}'.format(words) not in plan: bad.append('PLAN does not state the sample word count %d' % words)
for k in ('EVAL', 'PROC', 'SYNTH', 'CALC', 'CHAIN'):
    if (k in kinds) != (k in hand.split('Item and task types shown:')[1].split('.')[0]):
        bad.append('HANDOVER exemplar types disagree with the exemplar on %s' % k)
if 'do not reuse their scenarios in topics 3 and 4' in hand: bad.append('HANDOVER forbids reuse the README allows')
if 'group 3A starts units 3.3.2 and 3.3.3' not in hand.replace('Group', 'group') or 'Group 3A starts' not in readme:
    bad.append('reuse rule missing from HANDOVER or README')
if re.search(r'refs that drop the parent letter and collide', plan): bad.append('PLAN describes repaired defects as current')
if 'Unrounded' in plan and 'basis is the unrounded' not in plan: bad.append('PLAN AO basis unclear')
workspace = __import__('pathlib').Path(WS)
work_orders = [json.loads(p.read_text()) for p in sorted((workspace / 'topics').glob('*/work_order.json'))]
count = sum(len(w['item_slots']) + len(w['performance_tasks']) for w in work_orders)
budget = json.loads((workspace / 'curriculum/notes-budget.json').read_text())['total']
for name, doc in [('PLAN', plan), ('HANDOVER', hand)]:
    if f'{count:,} items' not in doc: bad.append(f'{name} item count disagrees with work orders')
    if f"{budget['min']:,}–{budget['max']:,}" not in doc: bad.append(f'{name} notes total disagrees with operative budget')
    if '24%%' in doc or '28%%' in doc: bad.append(f'{name} contains doubled percent signs')
if 'not the larger figure the contracts and work orders print' in hand:
    bad.append('HANDOVER describes superseded budgets as operative contract output')
if 'two stay low because they depend on figures' in plan:
    bad.append('PLAN incorrectly describes extinction mapping as figure-dependent')
evidence = json.loads((workspace / 'assessment-evidence/assessment_evidence.json').read_text())['records']
exceptions = json.loads((workspace / 'assessment-evidence/mapping_exceptions.json').read_text())
if f'{len(evidence)} Paper 2 and 3 parts have direct objective mappings' not in plan:
    bad.append('PLAN direct mapping total is stale')
if f"The {len(exceptions['exceptions'])} excluded parts" not in plan:
    bad.append('PLAN mapping exception count is stale')
rollup = json.loads((workspace / 'curriculum/ao-demand-rollup.json').read_text())
for a, value in rollup['shares_percent'].items():
    if f'| {a} (' not in plan or f'{value:.2f}%' not in plan:
        bad.append('PLAN audited AO share missing/stale: ' + a)
targets = json.loads((workspace / 'curriculum/assessment-framework.json').read_text())['ao_mark_budget']['stated_qualification_weight_percent']
if max(abs(v - targets[a]) for a, v in rollup['shares_percent'].items()) > 5 and 'OUTSIDE' not in plan:
    bad.append('PLAN must report the failed tolerance rather than imply approval')
slot_aos = {s['slot']: s['assessment_objectives'] for w in work_orders for s in w['item_slots']}
for item in items:
    if item.get('subtype') and slot_aos.get(item['item_id']) != item['assessment_objectives']:
        bad.append('Exemplar AO differs from audited slot: ' + item['item_id'])
if 'prepared*' not in plan or '*approved*' not in plan or '*delivered*' not in plan:
    bad.append('PLAN must distinguish visual preparation, approval and delivery')
if '4 YOU: plan approved' in (workspace / 'STATUS.md').read_text() and '- [ ] 4 YOU: plan approved' in (workspace / 'STATUS.md').read_text():
    if 'Do not start authoring yet' not in hand: bad.append('HANDOVER lacks the pending-approval instruction')
approval = json.loads((workspace / 'planning/operator_approvals.json').read_text())
if approval['plan']['status'] == 'approved':
    if 'Plan approved by Lotto' not in plan or 'Plan approved by Lotto' not in hand:
        bad.append('PLAN/HANDOVER omit recorded full-plan approval')
    if 'Full authoring remains unapproved' in plan or 'Do not start authoring yet' in hand:
        bad.append('PLAN/HANDOVER retain superseded plan-approval hold')
    if '- [x] 4 YOU: plan approved' not in (workspace / 'STATUS.md').read_text():
        bad.append('STATUS omits recorded full-plan approval')
print('docs: %s' % ('consistent' if not bad else '%d problems' % len(bad)))
for b in bad: print('  ', b)
sys.exit(1 if bad else 0)
