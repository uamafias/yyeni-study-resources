#!/usr/bin/env python3
"""Put the operative notes budget into every work order and contract, and mark the old figure.

Run after build/make_work_order.py (planning/RUN_ORDER.md). make_contract.py:34 budgets 230-470
words for every registry objective and has no input through which a subject can set its own
budget; make_work_order.py then shares the contract budget across units by objective count. For
this subject that pays the same explanation once per member of every split bullet (see
planning/notes_budget.py). Rather than leave authors two numbers, this step writes the operative
figure from curriculum/notes-budget.json into:

  topics/<T>/work_order.json   each content unit's word_budget, with word_budget_superseded
                               (the formula's figure) and word_budget_source beside it
  topics/<T>/work_order.md     re-rendered by make_work_order.as_markdown, the standard's own
                               renderer, plus a line saying where the figures come from
  topics/<T>/contract.json     depth_constraints.word_budget (topic total), with the superseded
                               figure and the source recorded

Nothing else in either file changes. --check verifies, without writing, that every work order and
contract carries the operative figure; it exits 1 if any does not.
"""
import json, os, sys

WS = 'work/nam-6116-nssco-2026'
sys.path.insert(0, 'standard/v0.2.0-draft/build')
from make_work_order import as_markdown            # read-only import of the standard's renderer

nb = json.load(open(f'{WS}/curriculum/notes-budget.json'))
SRC = 'curriculum/notes-budget.json (per syllabus bullet; planning/notes_budget.py)'
NOTE = ('> **Word budgets.** Every unit budget below is the operative figure from '
        '`curriculum/notes-budget.json`. The figure `build/make_contract.py` computes per objective is '
        'superseded; it is kept in `work_order.json` as `word_budget_superseded` for the record. Set each '
        'content unit\'s `word_budget` to the figure shown here: C-26 measures the unit against it.')
check = '--check' in sys.argv
bad = []
for t in sorted(nb['topics']):
    wp, cp = f'{WS}/topics/{t}/work_order.json', f'{WS}/topics/{t}/contract.json'
    wo, c = json.load(open(wp)), json.load(open(cp))
    for u in wo['content_units']:
        want = [nb['units'][u['unit_id']]['min'], nb['units'][u['unit_id']]['max']]
        if check:
            if u['word_budget'] != want:
                bad.append('%s %s: %s, operative %s' % (t, u['unit_id'], u['word_budget'], want))
            continue
        if u.get('word_budget_source') != SRC:
            u['word_budget_superseded'] = u['word_budget']
        u['word_budget'], u['word_budget_source'] = want, SRC
    dc = c['depth_constraints']
    want_t = {'min': nb['topics'][t]['min'], 'max': nb['topics'][t]['max']}
    if check:
        if dc['word_budget'] != want_t:
            bad.append('%s contract: %s, operative %s' % (t, dc['word_budget'], want_t))
        if NOTE not in open(f'{WS}/topics/{t}/work_order.md').read():
            bad.append('%s work_order.md lacks the budget note' % t)
        continue
    if dc.get('word_budget_source') != SRC:
        dc['word_budget_superseded'] = dc['word_budget']
    dc['word_budget'], dc['word_budget_source'] = want_t, SRC
    json.dump(wo, open(wp, 'w'), indent=1, ensure_ascii=False)
    json.dump(c, open(cp, 'w'), indent=1, ensure_ascii=False)
    md = as_markdown(wo).replace('## Content units', NOTE + '\n\n## Content units', 1)
    if wo.get('ao_demand_audit_source'):
        md += '\n\n## Mandatory AO demand decisions\n\nRead each slot\'s `ao_demand` in work_order.json and `planning/ao_demand_audit.json`. B requires genuine information handling or reasoning; supplied data and unfamiliarity are not universal prerequisites. A renamed taught example alone is insufficient. Practical C requires a practical demand. Recheck every actual prompt against these conditions. Plan approved by Lotto, 2026-10-18; actual prompts still require review.\n'
    open(f'{WS}/topics/{t}/work_order.md', 'w').write(md)
    print('topic %s: %d units, notes %d-%d words (formula %s-%s, superseded)'
          % (t, len(wo['content_units']), want_t['min'], want_t['max'],
             dc['word_budget_superseded']['min'], dc['word_budget_superseded']['max']))
if check:
    print('budget check: %s' % ('every work order and contract carries the operative budget' if not bad
                                else '%d mismatches' % len(bad)))
    for b in bad:
        print('  ', b)
    sys.exit(1 if bad else 0)
