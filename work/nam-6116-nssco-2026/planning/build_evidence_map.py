#!/usr/bin/env python3
"""Write assessment-evidence/assessment_evidence.json: question parts mapped to OBJECTIVES by meaning.

The sub-topic mapping (map_and_expose.py, validate_mapping.py) proposes a sub-topic per part by term
matching. That is not enough for check C-39, which recomputes each objective's exposure from an
evidence map whose records name objectives. On 2026-10-18 every Paper 2 and Paper 3 part (341) was
read in its paper, with its parent question for context, and mapped to the objective(s) whose skill
a creditable answer must show (planning/objective_mapping/map_A|B|C.json, one Miner pass per two
series, provenance judgement, each mapping with a confidence and a one-line basis).

Paper 1 multiple-choice questions are not mapped: they carry no command word or tariff and were not
mined as parts. The map is therefore `partial` and says so.
"""
import json, glob

WS = 'work/nam-6116-nssco-2026'
parts = json.load(open(f'{WS}/assessment-evidence/paper_evidence.json'))['question_parts']
reg = {o['objective_id'] for o in json.load(open(f'{WS}/curriculum/objective_registry.json'))['objectives']
       if o['parent_id']}
maps = {}
for f in sorted(glob.glob(f'{WS}/planning/objective_mapping/map_*.json')):
    for m in json.load(open(f)):
        if m['part_key'] in maps:
            raise SystemExit('part %s mapped twice' % m['part_key'])
        maps[m['part_key']] = m
key = lambda p: '%s/P%s/%s' % (p['year'], p['paper'], p['question_ref'])
if len({key(p) for p in parts}) != len(parts):
    raise SystemExit('question references are not unique; re-mine with full references')
missing = sorted({key(p) for p in parts} - set(maps))
unknown = sorted({o for m in maps.values() for o in m['objective_ids']} - reg)
if missing or unknown:
    raise SystemExit('unmapped parts %s; unknown objectives %s' % (missing[:10], unknown[:10]))

# second look at the low-confidence mappings (objective_mapping/review_low_confidence.json)
review = json.load(open(f'{WS}/planning/objective_mapping/review_low_confidence.json'))['decisions']
regtext = {o['objective_id']: o['syllabus_text'] for o in
           json.load(open(f'{WS}/curriculum/objective_registry.json'))['objectives'] if o['parent_id']}
for k, d in review.items():
    m = maps[k]
    if not d.get('keep'):
        ids = []
        for pre in d['objective_starts']:
            hit = [o for o, t in regtext.items() if t.startswith(pre)]
            if len(hit) != 1:
                raise SystemExit('review %s: "%s" matched %d objectives' % (k, pre, len(hit)))
            ids += hit
        m['objective_ids'] = ids
    m['confidence'] = d['confidence']
    m['basis'] = d['note'] if d.get('replace_basis') else m['basis'] + ' | reviewed 2026-10-18: ' + d['note']
    m['mapping_status'] = d.get('mapping_status', 'direct')
    m['contextual_objective_ids'] = d.get('contextual_objective_ids', [])

records = []
exceptions = []
for i, p in enumerate(parts):
    m = maps[key(p)]
    if not m['objective_ids']:
        exceptions.append({'part_key': key(p), 'year': p['year'], 'paper': p['paper'],
                           'question_ref': p['question_ref'], 'mark_tariff': p['mark_tariff'],
                           'mapping_status': m.get('mapping_status', 'unresolved'),
                           'decision_confidence': m['confidence'], 'objective_ids': [],
                           'contextual_objective_ids': m.get('contextual_objective_ids', []),
                           'counts_towards_direct_exposure': False, 'basis': m['basis']})
        continue
    cw = p['command_word'] if p['command_word'] not in (None, 'None', 'direct question') else None
    records.append({'evidence_id': 'EV-6116-%s-P%s-%s' % (p['year'], p['paper'], p['question_ref']),
                    'source_id': '6116/%s/%s' % (p['paper'], p['year'][2:]),
                    'evidence_type': 'past_paper', 'exam_series': p['year'], 'year': int(p['year']),
                    'paper_id': p['paper'], 'variant': None, 'question_ref': p['question_ref'],
                    'mark_tariff': p['mark_tariff'], 'objective_ids': m['objective_ids'], 'command_word': cw,
                    'ao_focus': ['AO3'] if p['paper'] == '3' else [],
                    'source_locator': '%s Paper %s, question %s' % (p['year'], p['paper'], p['question_ref']),
                    'notes': ['mapping confidence: %s' % m['confidence'], 'basis: %s' % m['basis']]})
out = {'map_id': 'EVMAP-6116-NSSCO-2026', 'status': 'partial', 'records': records}
json.dump(out, open(f'{WS}/assessment-evidence/assessment_evidence.json', 'w'), indent=1, ensure_ascii=False)
json.dump({'rule': 'All original paper parts remain in paper_evidence.json. These parts have no defensible direct objective mapping; contextual links never count towards objective exposure.',
           'total_paper_parts': len(parts), 'direct_records': len(records), 'exceptions': exceptions},
          open(f'{WS}/assessment-evidence/mapping_exceptions.json', 'w'), indent=2, ensure_ascii=False)
assert len(records) + len(exceptions) == len(parts)
import collections
print('%d direct records from %d parts; %d exceptions; direct confidence %s; objectives named %d of %d'
      % (len(records), len(parts), len(exceptions), dict(collections.Counter(r['notes'][0] for r in records)),
         len({o for r in records for o in r['objective_ids']}), len(reg)))
