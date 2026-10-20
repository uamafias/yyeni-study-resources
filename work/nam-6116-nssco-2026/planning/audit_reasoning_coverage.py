#!/usr/bin/env python3
"""Inspect planned reasoning routes before proposing any quantity-driven redesign.

This is a bounded planning audit, not certification of unauthored learner material.
The route selections are explicit judgement, not counts inferred from AO percentages.
"""
import json
from pathlib import Path

WS = Path('work/nam-6116-nssco-2026')
slots = {s['slot']: s for t in range(1, 6)
         for s in json.loads((WS/f'topics/{t}/work_order.json').read_text())['item_slots']}
routes = [
 ('B1', 'Select and organise information', ['ITEM-6116-1-033-APP'],
  'Use multiple sources to select relevant information; do not turn this into a definition of a source.'),
 ('B2', 'Translate representations', ['ITEM-6116-1-051-CALC', 'ITEM-6116-2-006-INTERP'],
  'Carry out unit conversions or use the supplied key branches/features; the key still needs a usable visual stimulus.'),
 ('B3', 'Manipulate numerical information', ['ITEM-6116-1-009-CALC', 'ITEM-6116-3-001-CALC', 'ITEM-6116-4-084-CALC'],
  'Calculate from given quantities with working/units; recalling the formula alone does not meet this demand.'),
 ('B4', 'Infer patterns and trends', ['ITEM-6116-4-085-INTERP', 'ITEM-6116-5-045-APP'],
  'Interpret germination/population observations rather than recite a known curve. Population graphics remain held/unapproved.'),
 ('B5', 'Reasoned explanations', ['ITEM-6116-3-258-APP', 'ITEM-6116-3-166-APP'],
  'Reason about limiting factors or reconcile wet-soil/wilting observations. The fertiliser exemplar demonstrates a conditional explanation; full topic breadth is unauthored.'),
 ('B6', 'Predictions and hypotheses', ['ITEM-6116-4-110-CALC', 'ITEM-6116-4-115-CALC', 'ITEM-6116-4-117-CALC'],
  'Derive predictions from crosses. Standard-ratio recognition remains an A/B boundary; require actual derivation where that is the planned task.'),
 ('B7', 'Solve biological problems', ['ITEM-6116-3-170-APP', 'ITEM-6116-3-172-APP'],
  'The existing flooded-root and inhibited-respiration exemplars require biological consequences/inference rather than a generic process description.'),
 ('C2', 'Investigation planning and reasoned prediction', ['ITEM-6116-1-076-SYNTH'],
  'Plan an investigation and justify a prediction. This practises reasoning under C; it must not be relabelled B to improve the bank mix.'),
 ('C3', 'Process experimental observations and anomalous results', ['ITEM-6116-1-059-PROC', 'ITEM-6116-1-068-APP'],
  'Process the observations and deal with anomalous/inconsistent results; naming an anomaly without processing its consequences is insufficient.'),
 ('C4', 'Interpret practical evidence and justify conclusions', ['ITEM-6116-1-064-APP'],
  'Use practical observations/data to justify the conclusion in relation to the hypothesis.'),
 ('C5', 'Evaluate methods and suggest improvements', ['ITEM-6116-1-057-PROC', 'ITEM-6116-1-058-LIM'],
  'Both slots serve the explicit objective: Identify sources of error and suggest possible improvements in procedures. In the actual task, evaluate a stated method: identify the error, explain its effect and tie a feasible improvement to it. A generic list of errors alone is insufficient.'),
]
records = []
for code, title, ids, caveat in routes:
    assert all(s in slots for s in ids), (code, ids)
    expected = 'AO3' if code.startswith('C') else 'AO2'
    assert all(slots[s]['assessment_objectives'] == [expected] for s in ids)
    records.append({'skill': code, 'demand': title, 'slots': ids,
                    'objectives': sorted({slots[s]['objective_id'] for s in ids}),
                    'slot_objective_text': {s: slots[s]['objective_title'] for s in ids},
                    'state': 'planned route; actual authored demand must be checked',
                    'authoring_review': caveat})
out = {'scope': 'planned demand-type routes and existing exemplars; not whole-bank adequacy or stimulus approval',
       'decision_basis': 'operator approved corrected classification and coverage-first approach; no automatic 28% quota',
       'records': records,
       'finding': 'Every B1–B7 demand type has an identifiable planned route. This does not establish sufficient breadth, frequency or challenge in the future authored bank.',
       'action': 'No additional items or demand redesign justified solely by the percentage mismatch. Keep existing reasoning demands explicit, address known stimulus holds, and inspect actual prompts/results before deciding whether specific gaps need repair.',
       'shared_rule': 'The repository five-point tolerance remains a reported framework rule. Lotto approved the full plan, including the coverage-first approach, on 2026-10-18. This is not a change to standard/ or a claim of adequate authored coverage.'}
(WS/'review/reasoning-coverage-audit.json').write_text(json.dumps(out, indent=2, ensure_ascii=False)+'\n')
L = ['# Biology 6116 — reasoning coverage before redesign', '',
     '**Outcome:** no wholly missing B demand type was identified in this bounded plan-level review. No new items or redesign are justified by the percentage mismatch alone.', '',
     'This audits explicit planned routes against the syllabus B1–B7 and related C demands. It does not certify an unauthored bank as sufficient. Existing exemplars demonstrate some reasoning tasks; a generic slot name does not demonstrate an effective learner activity.', '',
     '| Skill | Planned route | Existing slots | What the actual task must do |', '|---|---|---|---|']
for r in records:
    L.append(f"| {r['skill']} | {r['demand']} | {', '.join(r['slots'])} | {r['authoring_review']} |")
L += ['', '## Consequence for the plan', '', out['action'], '',
      'At item review, check whether the learner actually selects/derives/infers rather than repeats a taught answer, whether the prompt supports the conclusion, and whether required tables/keys/images are present and reviewed. Use failures of those checks to identify repairs. Do not infer adequacy from a tally of APP cards or infer a deficit from the AO percentage alone.', '',
      'Uncertainty remains about authored breadth, frequency and challenge because full authoring has not started. Population/key/other required visuals retain their existing holds. The known breastfeeding-pattern and standard-ratio boundaries remain recorded rather than forced into one category.', '',
      out['shared_rule'], '']
(WS/'review/REASONING-COVERAGE-AUDIT.md').write_text('\n'.join(L))
print('Reasoning coverage: B1–B7 planned routes identified; no quota-driven redesign; authored adequacy remains unverified')
