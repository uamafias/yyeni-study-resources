#!/usr/bin/env python3
"""Authoring check: every content unit declares the operative word budget.

C-26 (standard) measures each content unit's word_count against the word_budget the unit itself
declares. This confirms the declared figure is the operative one, so C-26 is measuring against
curriculum/notes-budget.json and not a number an author chose or copied from the superseded formula.

    python3 work/nam-6116-nssco-2026/planning/check_unit_budgets.py <workspace> <topic>

A unit that holds only some of its work-order unit's objectives (an exemplar slice) is compared with
the same model applied to its own objectives (planning/notes_budget.py budget_for). Exit 1 on any
mismatch.
"""
import glob, json, os, sys

ws, t = sys.argv[1].rstrip('/'), sys.argv[2]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from notes_budget import budget_for

nb = json.load(open(os.path.join(ws, 'curriculum', 'notes-budget.json')))['units']
wo = {u['unit_id']: u for u in json.load(open(os.path.join(ws, 'topics', t, 'work_order.json')))['content_units']}
reg = {o['objective_id']: o['syllabus_text'] for o in
       json.load(open(os.path.join(ws, 'curriculum', 'objective_registry.json')))['objectives']}
bad, n = [], 0
for p in sorted(glob.glob(os.path.join(ws, 'topics', t, 'content-units', '*.json'))):
    u = json.load(open(p)); n += 1
    have = [u['word_budget']['min'], u['word_budget']['max']]
    whole = wo.get(u['unit_id'])
    if whole is None:
        bad.append('%s is not a unit in the work order' % u['unit_id']); continue
    if set(u['objective_ids']) == set(whole['objective_ids']):
        want, how = [nb[u['unit_id']]['min'], nb[u['unit_id']]['max']], 'notes-budget.json'
    else:
        want, how = list(budget_for([reg[o] for o in u['objective_ids']])), 'model on the slice'
    if have != want:
        bad.append('%s declares %s; operative %s (%s)' % (u['unit_id'], have, want, how))
print('unit budgets: %d units, %s' % (n, 'all declare the operative budget' if not bad else '%d wrong' % len(bad)))
for b in bad:
    print('  ', b)
sys.exit(1 if bad else 0)
