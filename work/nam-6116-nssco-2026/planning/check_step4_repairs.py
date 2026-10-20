#!/usr/bin/env python3
"""Targeted evidence and demand checks for the authorised Step 4 repairs."""
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import sys
import jsonschema

WS = Path('work/nam-6116-nssco-2026')
J = lambda name: json.loads((WS/name).read_text())
evidence = J('assessment-evidence/assessment_evidence.json')
schema = json.loads(Path('standard/v0.2.0-draft/schemas/assessment_evidence.schema.json').read_text())
jsonschema.validate(evidence, schema)
direct = {(str(r['year']), r['paper_id'], r['question_ref']): r for r in evidence['records']}
assert len(direct) == len(evidence['records']) == 339
assert direct[('2024', '2', '6(a)')]['objective_ids'] == ['OBJ-6116-3.2-01']
assert ('2023', '2', '2(c)') not in direct
assert ('2022', '2', '1(d)(i)') not in direct
exceptions = J('assessment-evidence/mapping_exceptions.json')['exceptions']
assert {e['part_key'] for e in exceptions} == {'2023/P2/2(c)', '2022/P2/1(d)(i)'}
assert all(not e['counts_towards_direct_exposure'] and not e['objective_ids'] for e in exceptions)
assert {e['mapping_status'] for e in exceptions} == {'unresolved', 'context_only'}
raw = J('assessment-evidence/paper_evidence.json')['question_parts']
assert len(raw) == len(direct) + len(exceptions) == 341
raw_keys = {(str(r['year']), r['paper'], r['question_ref']) for r in raw}
exception_keys = {(e['year'], e['paper'], e['question_ref']) for e in exceptions}
assert set(direct).isdisjoint(exception_keys) and set(direct) | exception_keys == raw_keys
sys.path.insert(0, 'standard/v0.2.0-draft/checks')
from yyeni_checks import Build, c39
for t in range(1, 6):
    status, message, affected = c39(Build(str(WS), str(t)))
    assert status == 'pass', (t, message, affected)
print('Evidence schema, all 341 parts accounted for, repaired/excluded mappings and C-39 on all five topics: PASS')

before = {s['slot']: s for s in J('planning/ao_slots_before_repair.json')['slots']}
post = {r['slot']: r for r in J('planning/post_authoring_label_decisions.json')['decisions']}
allowed = {s['subtype']: s['assessment_objectives'] for s in J('curriculum/assessment-framework.json')['flashcard_subtype_ao_map']}
totals, seen, changed = Counter(), set(), Counter()
for t in range(1, 6):
    wo = J(f'topics/{t}/work_order.json')
    for s in wo['item_slots']:
        assert s['slot'] not in seen
        seen.add(s['slot'])
        old = before[s['slot']]
        for k in ('objective_id', 'subtype', 'mark_tariff'):
            assert s[k] == old[k], (s['slot'], k)
        for k in ('command_word', 'blooms_level'):
            assert s[k] == (post[s['slot']]['decided'][k] if s['slot'] in post else old[k]), (s['slot'], k)
        if not set(s['assessment_objectives']) <= set(allowed[s['subtype']]):
            assert s['slot'] in post and s['assessment_objectives'] == post[s['slot']]['decided']['assessment_objectives'], s['slot']
        if s['assessment_objectives'] != old['assessment_objectives']:
            changed[s['subtype']] += 1
        for a in s['assessment_objectives']:
            totals[a] += Fraction(s['mark_tariff'], len(s['assessment_objectives']))
    totals.update({'AO1': Fraction(25, 2), 'AO2': Fraction(15, 2), 'AO3': 10})
assert seen == set(before) and len(seen) == 871
rollup = J('curriculum/ao-demand-rollup.json')
assert {a: str(totals[a]) for a in ('AO1', 'AO2', 'AO3')} == rollup['marks']
assert sum(totals.values()) == Fraction(rollup['total_marks']) == 2029
assert len(post) == 41 and set(post) - seen == {'ITEM-6116-3-P02'}
print('Slots/counts/tariffs preserved; post-authoring label decisions and independent rational AO sum: PASS')
print('Changed slot labels by subtype:', dict(changed))
