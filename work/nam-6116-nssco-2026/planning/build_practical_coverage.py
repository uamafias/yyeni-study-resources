#!/usr/bin/env python3
"""Write curriculum/practical-coverage.json: what the written resource covers of each practical objective.

A written resource, like Paper 3 (Alternative to Practical), can teach and test how to plan a
practical, the procedure, the readings, their interpretation and the method's limitations. It cannot
show that a learner has carried a practical out. An objective worded "design and carry out", "make
temporary slides" or "use and manipulate a light microscope" therefore has a hands-on component that
no card covers. This file keeps the two apart, objective by objective, so that coverage of an
objective by cards is never read as evidence that the hands-on part was done.

Run after the work orders exist (it reads each practical objective's slots).
"""
import json, re, collections

WS = 'work/nam-6116-nssco-2026'
reg = [o for o in json.load(open(f'{WS}/curriculum/objective_registry.json'))['objectives']
       if o.get('parent_id') and (o['objective_type'].startswith('prac_') or o['objective_type'].startswith('task_drawing'))]
slots = collections.defaultdict(list)
for t in '12345':
    for s in json.load(open(f'{WS}/topics/{t}/work_order.json'))['item_slots']:
        slots[s['objective_id']].append(s['subtype'])

HANDS_ON = re.compile(r'carry out|\bmake (?:temporary|observations|a clear)|prepare and stain|use and manipulate|'
                      r'\bhandle\b|\bmeasure\b|\brecord\b|\binvestigate\b|\bobserve\b|use dialysis|'
                      r'\bdraw (?:prepared|organisms|and interpret)|explore', re.I)
WRITTEN = {'PROC': 'plan or procedure (what to change, measure, keep the same; the steps)',
           'LIM': 'limitations, errors and improvements', 'APP': 'interpreting an unfamiliar version',
           'INTERP': 'reading, completing or presenting data', 'WHY': 'the reason for a step',
           'CALC': 'calculation from readings', 'MISCON': 'an evidenced confusion'}
out, n_hands = [], 0
for o in reg:
    m = HANDS_ON.search(o['syllabus_text'])
    n_hands += bool(m)
    out.append({'objective_id': o['objective_id'], 'objective': o['syllabus_text'],
                'written_coverage': [WRITTEN.get(s, s) for s in slots[o['objective_id']]],
                'hands_on_component': m.group(0) if m else None,
                'hands_on_covered_by_resource': False if m else None,
                'note': ('The cards test planning, procedure and interpretation in writing, as Paper 3 does. '
                         'Doing it needs the school laboratory; no card is evidence that it was done.'
                         if m else 'Written skill; fully covered by the cards.')})
json.dump({'generated_by': f'{WS}/planning/build_practical_coverage.py',
           'rule': __doc__.split('\n\n')[1].replace('\n', ' '),
           'practical_objectives': len(out), 'with_hands_on_component': n_hands, 'objectives': out},
          open(f'{WS}/curriculum/practical-coverage.json', 'w'), indent=2, ensure_ascii=False)
print('%d practical objectives, %d with a hands-on component the written resource cannot cover' % (len(out), n_hands))
