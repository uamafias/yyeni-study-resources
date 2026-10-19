#!/usr/bin/env python3
"""Revised notes word budget: per syllabus bullet, not per decomposed objective.

Why. build/make_contract.py:34 budgets 230-470 words for EVERY registry objective by exposure
class. That suits a registry of whole syllabus outcomes (9702: 197 objectives). Here 80 bullets
were split into their members so each member gets its own card, and the same formula then pays for
the shared explanation once per member: the 13 "list the visible external features used to
classify <group>" objectives would get 3,000-4,300 words for what is one comparative table and its
lead-in. Cards need decomposition; prose does not.

Model, per syllabus bullet (curriculum/syllabus-facts.json), by what the bullet asks:
  recall (define, state, name, list, identify)      60-100 words
  description (describe, outline, other)            120-180
  explanation or practical (explain, discuss,
    investigate, plan, describe how, design ...)    180-280
  each member beyond the first of a split bullet    +30-50 (its own sentence or table row)
  per content unit: introduction and cross-links    +50-90
Bullets the lead-in absorbed count as members of it. Worked calculations and genetic diagrams sit
inside the explanation band.

Output: curriculum/notes-budget.json, per work-order content unit and per topic. The content
unit's own `word_budget` is set from it by the author, and C-26 measures every unit against it.
"""
import json, re, collections, os, sys

WS = 'work/nam-6116-nssco-2026'

REC = re.compile(r'^(define|state|name|list|identify)\b', re.I)
EXP = re.compile(r'^(explain|discuss|investigate|plan|design|evaluate|analyse|interpret|observe|'
                 r'record and present|measure and record|make temporary|prepare|identify and explain|'
                 r'describe how|describe and explain|draw and interpret)\b|^(describe|outline) how', re.I)
BANDS = {'recall': (60, 100), 'description': (120, 180), 'explanation': (180, 280)}
MEMBER, UNIT = (30, 50), (50, 90)


def band(t):
    return 'explanation' if EXP.match(t) else 'recall' if REC.match(t) else 'description'


def budget_for(texts):
    """(min, max) words for a unit, or a slice of one, holding objectives with these texts."""
    return (UNIT[0] + sum(BANDS[band(t)][0] for t in texts),
            UNIT[1] + sum(BANDS[band(t)][1] for t in texts))


def main():
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    os.chdir(root)
    sys.path.insert(0, 'standard/v0.2.0-draft/build')
    from make_work_order import sub_topic      # the unit key the work orders use (read-only import)
    facts = json.load(open(f'{WS}/curriculum/syllabus-facts.json'))

    units = collections.defaultdict(lambda: {'bullets': 0, 'members_extra': 0, 'lo': 0, 'hi': 0,
                                             'by_band': collections.Counter()})
    for r in facts['content']:
        if r['code'].isdigit():
            continue
        key = sub_topic('OBJ-6116-%s-01' % r['code'])
        for o in r['specific_objectives']:
            if o.get('absorbed_by'):
                continue
            b = band(o['text'])
            u = units[key]
            lo, hi = BANDS[b]
            extra = len((o.get('decomposition') or {}).get('members') or [None]) - 1
            u['bullets'] += 1; u['members_extra'] += extra; u['by_band'][b] += 1
            u['lo'] += lo + extra * MEMBER[0]; u['hi'] += hi + extra * MEMBER[1]
    for u in units.values():
        u['lo'] += UNIT[0]; u['hi'] += UNIT[1]; u['by_band'] = dict(u['by_band'])

    topics = collections.defaultdict(lambda: [0, 0])
    for k, u in units.items():
        topics[k.split('.')[0]][0] += u['lo']; topics[k.split('.')[0]][1] += u['hi']
    contract = {t: (lambda dc: dc.get('word_budget_superseded') or dc['word_budget'])(
                    json.load(open(f'{WS}/topics/{t}/contract.json'))['depth_constraints'])
                for t in topics}
    out = {'generated_by': f'{WS}/planning/notes_budget.py', 'model': __doc__.split('Model,')[1].split('Output:')[0].strip(),
           'operative': True,
           'note': ('Supersedes the word_budget in the topic contracts and work orders, which make_contract.py '
                    'computes per decomposed objective (framework finding in PLAN section 9).'),
           'units': {f'CU-6116-{k}': {'min': v['lo'], 'max': v['hi'], 'bullets': v['bullets'],
                                      'split_members_beyond_first': v['members_extra'], 'by_band': v['by_band']}
                     for k, v in sorted(units.items(), key=lambda kv: [int(x) for x in kv[0].split('.')])},
           'topics': {t: {'min': lo, 'max': hi, 'contract_formula': contract[t]} for t, (lo, hi) in sorted(topics.items())},
           'total': {'min': sum(v[0] for v in topics.values()), 'max': sum(v[1] for v in topics.values()),
                     'contract_formula': {'min': sum(c['min'] for c in contract.values()),
                                          'max': sum(c['max'] for c in contract.values())}}}
    json.dump(out, open(f'{WS}/curriculum/notes-budget.json', 'w'), indent=2)
    for t, v in out['topics'].items():
        print(t, v['min'], v['max'], 'was', v['contract_formula']['min'], v['contract_formula']['max'])
    print('total', out['total'])
    print('CU-6116-2.2', out['units']['CU-6116-2.2'], '\nCU-6116-3.3.2', out['units']['CU-6116-3.3.2'])


if __name__ == '__main__':
    main()
