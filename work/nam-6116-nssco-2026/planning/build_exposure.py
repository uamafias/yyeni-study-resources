#!/usr/bin/env python3
"""Write curriculum/exam-exposure.json in the shape the build tools read.

Run after validate_mapping.py. build/make_contract.py and build/make_work_order.py
read `objectives`: one entry per registry objective, keyed by objective_id, with an
exposure_class from core | frequent | occasional | rare | unseen and
evidence.max_mark_tariff.

Counted from VALIDATED question parts only: parts where two independent mapping
methods agreed on the sub-topic (validate_mapping.py). Mapping is established at
sub-topic level, not objective level, so every objective inherits its sub-topic's
exposure and says so. Exposure calibrates emphasis. It never removes an objective,
and nothing here becomes an item count.

Class, by the number of the six series in which the sub-topic was examined:
  0 unseen · 1 rare · 2-3 occasional · 4 frequent · 5-6 core
"""
import json, collections

WS = 'work/nam-6116-nssco-2026'
reg = json.load(open(f'{WS}/curriculum/objective_registry.json'))['objectives']
ev = json.load(open(f'{WS}/assessment-evidence/paper_evidence.json'))
SERIES = ['2020', '2021', '2022', '2023', '2024', '2025']

# Objective-level exposure (2026-10-18): counted from the evidence map, whose records name
# objectives by meaning (planning/build_evidence_map.py). C-39 recomputes every figure below from
# those records. The sub-topic table, from the term-matched and validated parts, is kept beside it
# for reference only.
evmap = json.load(open(f'{WS}/assessment-evidence/assessment_evidence.json'))['records']
parts = [p for p in ev['question_parts'] if p.get('mapping_status') == 'validated']
by_sub = collections.defaultdict(list)
for p in parts:
    by_sub[p['proposed_sub_topic']].append(p)


def cls(n_series):
    return ('unseen' if n_series == 0 else 'rare' if n_series == 1 else
            'occasional' if n_series <= 3 else 'frequent' if n_series == 4 else 'core')


def sub_summary(ps):
    years = sorted({p['year'] for p in ps})
    return {'validated_parts': len(ps), 'marks': sum(p['mark_tariff'] for p in ps), 'series': years}


sub_table = {k: sub_summary(v) for k, v in sorted(by_sub.items())}
by_obj = collections.defaultdict(list)
for r in evmap:
    for oid in r['objective_ids']:
        by_obj[oid].append(r)
objs = []
for o in reg:
    rs = by_obj.get(o['objective_id'], [])
    series = sorted({r['exam_series'] for r in rs})
    cw = collections.Counter(r['command_word'] for r in rs if r.get('command_word'))
    tariffs = collections.Counter(str(r['mark_tariff']) for r in rs)
    objs.append({'objective_id': o['objective_id'], 'topic_id': o['topic_id'],
                 'syllabus_text': o['syllabus_text'], 'sub_topic': o.get('sub_topic'),
                 'times_examined': len(rs), 'marks_examined': sum(r['mark_tariff'] for r in rs),
                 'series': series, 'tariffs': dict(sorted(tariffs.items())),
                 'command_words': dict(cw),
                 'modal_tariff': int(max(tariffs, key=tariffs.get)) if tariffs else None,
                 'exposure_class': cls(len(series)),
                 'exposure_scope': 'Papers 2 and 3 only',
                 'evidence': {'question_parts_naming_it': len(rs), 'distinct_series': len(series),
                              'max_mark_tariff': max((r['mark_tariff'] for r in rs), default=0),
                              'command_words_observed': dict(cw),
                              'granularity': 'objective, mapped by meaning (assessment-evidence/assessment_evidence.json)'},
                 'required_subtypes': []})

out = {
    'exposure_id': 'EXPO-6116-NSSCO-2026',
    'generated_by': 'work/nam-6116-nssco-2026/planning/build_exposure.py',
    'authority': 'measured from the question papers; the syllabus remains the scope authority',
    'evidence_window': '2020-2025, six series, Papers 2 and 3 (Paper 1 carries no tariffed parts)',
    'method': ('Counted per objective from the evidence map: %d directly mapped Paper 2 and 3 parts, each read in '
               'its paper and mapped by meaning to the objective(s) it credits. Paper 1 is not mapped. '
               'The earlier sub-topic table (term matching; two methods agreed on %d of %d parts) is kept '
               'under sub_topics for reference.' % (len(evmap), len(parts), len(ev['question_parts']))),
    'exposure_scope': ('PAPERS 2 AND 3 ONLY. Paper 1 (40 multiple-choice questions a year, 30% of the qualification) '
                       'is not mapped. "unseen" means not seen in the mapped Paper 2 and 3 parts, not unexamined.'),
    'principle': ('Exposure calibrates emphasis. It never removes an objective: every objective is '
                  'mandatory and planned, including those with exposure_class unseen.'),
    'status': 'objective level, Papers 2 and 3; one Miner pass with targeted Codex repairs; unresolved/context-only parts excluded',
    'mapping_exceptions': 'assessment-evidence/mapping_exceptions.json (not counted towards direct exposure)',
    'exposure_class_rule': '0 series unseen, 1 rare, 2-3 occasional, 4 frequent, 5-6 core',
    'exposure_class_vocabulary': 'core | frequent | occasional | rare | unseen (build/make_contract.py)',
    'series_in_window': SERIES,
    'sub_topics': sub_table,
    'objectives': objs,
}
json.dump(out, open(f'{WS}/curriculum/exam-exposure.json', 'w'), indent=2, ensure_ascii=False)
print(out['method'])
print('objective exposure classes:', dict(collections.Counter(o['exposure_class'] for o in objs)))
