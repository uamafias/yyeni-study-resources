#!/usr/bin/env python3
"""Propose the actual items: how many, of what format, assessing what.

The earlier table counted objectives, not activities, and set AO C by comparing
an objective share against a grade percentage. That does not establish how many
practical tasks a learner needs. This plans items bottom-up:

  content skills   -> one item per assessable skill, format set by objective_type
  practical skills -> items planned against Annexe A's eleven criteria AND the
                      prac_* skills in the registry, since Paper 3 is specified
                      by Annexe A rather than by the content topics

The resulting AO balance is then CHECKED against the syllabus weighting. It is an
outcome of the plan, not an input to it, and no count is derived from a percentage.
"""
import json, collections

WS = 'work/nam-6116-nssco-2026'
reg = json.load(open(f'{WS}/curriculum/objective_registry.json'))['objectives']
side = json.load(open(f'{WS}/curriculum/objective_registry.planning.json'))['by_objective_id']
facts = json.load(open(f'{WS}/curriculum/syllabus-facts.json'))

# objective_type -> (item format, what it assesses, items per skill)
FORMAT = {
 'bio_definition':    ('DEF card',            'recall of a defined term, in the syllabus’s own sense', 1),
 'bio_concept':       ('DEF/FEATURE card',    'recall and understanding of a stated idea', 1),
 'bio_structure':     ('LABEL card + diagram','naming parts and their function on a diagram', 1),
 'bio_process':       ('PROC card',           'ordered steps of a process, in sequence', 1),
 'bio_comparison':    ('DIST card',           'the feature that separates two things', 1),
 'bio_relationship':  ('WHY/MECH card',       'the causal link, stated as a chain', 1),
 'bio_quantitative':  ('CALC item',           'a worked calculation with units shown', 1),
 'bio_application':   ('APPLY item',          'applying a principle to a stated situation', 1),
 'prac_mmo':          ('PRACTICAL technique', 'safe, correct use of apparatus and measurement', 1),
 'prac_presentation': ('GRAPH/TABLE task',    'presenting data to the Annexe B conventions', 1),
 'prac_analysis':     ('DATA/DESIGN task',    'interpreting data, or planning an investigation', 1),
}
# Annexe A's eleven criteria each need dedicated practice beyond the content skills
ANNEXE_A = [
 ('a', 'follow a sequence of instructions', 'PRACTICAL technique', 2),
 ('b', 'read scales, interpolate, average repeats', 'DATA/DESIGN task', 3),
 ('c', 'comment on experimental arrangements', 'DATA/DESIGN task', 3),
 ('d', 'interpret and evaluate observations and data', 'DATA/DESIGN task', 4),
 ('e', 'complete and process data tables', 'GRAPH/TABLE task', 3),
 ('f', 'calculations including magnification', 'CALC item', 3),
 ('g', 'plot graphs and interpret graphical information', 'GRAPH/TABLE task', 4),
 ('h', 'draw a conclusion justified by the data', 'DATA/DESIGN task', 3),
 ('i', 'identify sources of error, suggest improvements', 'DATA/DESIGN task', 3),
 ('j', 'plan an investigation with reasoned predictions', 'DATA/DESIGN task', 4),
 ('k', 'recognise, observe, record and measure specimens', 'PRACTICAL technique', 2),
]
# Skills the syllabus requires whose command word the papers never use. They are
# practised through items even though no prompt opens with that word.
RETAINED_SKILLS = [('predict', 'B6 and Annexe A (j)', 'DATA/DESIGN task', 4),
                   ('compare', 'A1-A2 and the Compare glossary entry', 'DIST card', 4),
                   ('apply/use', 'Apply/use glossary entry and AO B', 'APPLY item', 4)]

leaf = [o for o in reg if not side[o['objective_id']]['is_container'] and o['assessment_objectives']]
plan = collections.defaultdict(lambda: collections.Counter())
fmt_tot, ao_tot = collections.Counter(), collections.Counter()

for o in leaf:
    f, _, n = FORMAT[o['objective_type']]
    plan[o['topic_id']][f] += n
    fmt_tot[f] += n
    ao_tot[o['assessment_objectives'][0]] += n

# AO B5 is "present reasoned explanations of phenomena, patterns and relationships",
# and the syllabus says AO B is tested on material unfamiliar to the learner. A
# process or relationship skill is therefore assessed twice: once as the chain
# itself (AO A), once applied to a situation the learner has not seen (AO B).
# This is a slot-plan adjustment justified by B5, not padding to chase a number.
b5_items = 0
for o in leaf:
    if o['objective_type'] in ('bio_process', 'bio_relationship'):
        plan[o['topic_id']]['APPLY item (unfamiliar context)'] += 1
        fmt_tot['APPLY item (unfamiliar context)'] += 1
        ao_tot['B'] += 1
        b5_items += 1

annexe_items = sum(n for *_, n in ANNEXE_A)
for _, _, f, n in ANNEXE_A:
    plan['1'][f] += n; fmt_tot[f] += n; ao_tot['C'] += n
retained_items = sum(n for *_, n in RETAINED_SKILLS)
for _, _, f, n in RETAINED_SKILLS:
    plan['3'][f] += n; fmt_tot[f] += n
    ao_tot['B' if f != 'DIST card' else 'A'] += n

# misconception items: one per curated confusion that has a discriminating test
mis = json.load(open(f'{WS}/curriculum/misconceptions.json'))
ready = [m for m in mis['misconceptions'] if m.get('discriminating_test')]
held = [m for m in mis['misconceptions'] if not m.get('discriminating_test')]
for m in ready:
    plan[(m.get('proposed_sub_topic') or '3').split('.')[0]]['MISCON card'] += 1
    fmt_tot['MISCON card'] += 1; ao_tot['A'] += 1

total = sum(fmt_tot.values())
titles = {r['code']: r['title'] for r in facts['content'] if r['code'].isdigit()}
out = {
 'plan_id': 'ITEMPLAN-6116-NSSCO-2026',
 'method': ('One item per assessable skill, format from objective_type; practical items planned '
            'additionally against Annexe A’s eleven criteria; items added for syllabus skills '
            'whose command word the papers never use; one MISCON item per curated confusion that '
            'has a discriminating test. AO balance is an OUTCOME, checked below, not an input.'),
 'total_items': total,
 'by_format': dict(fmt_tot),
 'by_topic': {t: dict(c) for t, c in plan.items()},
 'annexe_a_items': annexe_items,
 'b5_application_items': b5_items,
 'b5_justification': ('AO B5 requires reasoned explanations of phenomena, patterns and '
                      'relationships, on material unfamiliar to the learner (syllabus printed '
                      'p.35). Process and relationship skills are therefore assessed both as the '
                      'chain and as its application. Slot-plan adjustment, not padding.'),
 'retained_skill_items': retained_items,
 'misconception_items_ready': len(ready),
 'misconception_items_held': len(held),
 'ao_balance_outcome': {k: round(v / total * 100, 1) for k, v in ao_tot.items()},
 'ao_targets': {'raw_marks': {'A': 47, 'B': 28, 'C': 25},
                'final_grade': {'A': 50, 'B': 30, 'C': 20}},
}
json.dump(out, open(f'{WS}/curriculum/item-plan.json', 'w'), indent=2, ensure_ascii=False)

print(f"TOTAL PROPOSED ITEMS: {total}\n")
print(f"{'topic':<5}{'title':<42}{'items':>6}")
for t in sorted(plan):
    print(f"{t:<5}{titles.get(t,'')[:40]:<42}{sum(plan[t].values()):>6}")
print(f"\n{'format':<24}{'items':>6}")
for f, n in fmt_tot.most_common():
    print(f"  {f:<22}{n:>6}")
print(f"\nAO BALANCE (outcome of the plan, checked against the syllabus)")
for ao in 'ABC':
    got = out['ao_balance_outcome'].get(ao, 0)
    print(f"  AO {ao}: {got:>5.1f}%   raw-mark target {out['ao_targets']['raw_marks'][ao]}%"
          f"   final-grade target {out['ao_targets']['final_grade'][ao]}%"
          f"   gap vs final {got - out['ao_targets']['final_grade'][ao]:+.1f}")
print(f"\nmisconception items ready {len(ready)}, held pending teacher input {len(held)}")
