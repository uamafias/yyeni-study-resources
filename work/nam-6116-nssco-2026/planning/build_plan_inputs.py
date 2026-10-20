#!/usr/bin/env python3
"""Assessment framework, qualification profile and the proposed activity mix.

Inputs are the transcribed syllabus and the VALIDATED evidence only. Excluded by
operator direction 2026-10-17: topic-difficulty rankings. Excluded by evidence
quality: unvalidated mappings (31% of parts validated; only those inform emphasis).

No percentage anywhere becomes a card count. Item counts are set by objective
coverage and the AO balance the syllabus states, then checked against measured
demand - not derived from it.
"""
import json, collections, io

WS = 'work/nam-6116-nssco-2026'
facts = json.load(open(f'{WS}/curriculum/syllabus-facts.json'))
reg = json.load(open(f'{WS}/curriculum/objective_registry.json'))['objectives']
side = json.load(open(f'{WS}/curriculum/objective_registry.planning.json'))['by_objective_id']
ev = json.load(open(f'{WS}/assessment-evidence/paper_evidence.json'))
shapes = json.load(open(f'{WS}/curriculum/answer-shapes.json'))['command_words']

leaf = [o for o in reg if not side[o['objective_id']]['is_container'] and o['assessment_objectives']]
gloss = {w['word'].lower().replace('/ ', '/') for w in facts['command_words']}

# command words: verdict per word, from the papers (AGENTS.md rule 5)
cw = {}
# AGENTS.md rule 5: a word may open a prompt only if the papers use it. The repo's
# own rule for "uses it" is observed_count > 0 (standard/v0.2.0-draft/mine/assemble.py:144,
# used_at_level = observed_count > 0); check C-14 forbids only words whose
# used_at_level is false. An earlier version of this script required two
# observations: that was our heuristic, not a repo requirement, and is withdrawn.
# A word seen once is usable and flagged as thin evidence.
for w, d in shapes.items():
    n = d['parts_seen']
    cw[w] = {
        'parts_observed': n,
        'modal_tariff': d['modal_tariff'],
        'tariffs_observed': d['tariffs_seen'],
        'in_syllabus_glossary': d['in_syllabus_glossary'],
        'use_in_prompts': n > 0,
        'evidence_strength': 'thin (one part)' if n == 1 else 'observed' if n else 'none',
        'reason': ('opens %d part%s in the sampled Papers 2 and 3' % (n, '' if n == 1 else 's')
                   if n else 'never observed opening a part'),
    }
for g in sorted(gloss):
    if g not in cw:
        cw[g] = {'parts_observed': 0, 'modal_tariff': None, 'tariffs_observed': [],
                 'in_syllabus_glossary': True, 'use_in_prompts': False, 'evidence_strength': 'none',
                 'reason': ('defined by the syllabus but never observed opening a part. '
                            'NOT used as a prompt opener. The underlying SKILL remains in scope '
                            'and is practised through the objectives that require it.')}

# Shape required by build/make_contract.py and build/make_work_order.py:
# command_words is a LIST with word / observed_count / modal_tariff /
# observed_tariffs, and the AO targets live under ao_mark_budget.
# Which AO a word's answer usually earns. Judgement, read from the AO descriptions
# (printed p.35-36): recall and description of taught content is A; calculation,
# data, suggestion about unfamiliar material and discussion are B; measuring and
# plotting are C on Paper 3 and B on Paper 2.
CW_AO = {'define': ['AO1'], 'state': ['AO1'], 'name': ['AO1'], 'list': ['AO1'], 'identify': ['AO1'],
         'label': ['AO1'], 'outline': ['AO1'], 'describe': ['AO1'], 'explain': ['AO1', 'AO2'],
         'describe and explain': ['AO1', 'AO2'], 'suggest': ['AO2'], 'calculate': ['AO2'],
         'determine': ['AO2'], 'complete': ['AO2', 'AO3'], 'discuss': ['AO2'], 'distinguish': ['AO2'],
         'draw': ['AO1', 'AO3'], 'plot': ['AO3'], 'measure': ['AO3'], 'estimate': ['AO2'],
         'find': ['AO2'], 'indicate': ['AO1']}
cw_list = []
for w, d in sorted(cw.items()):
    cw_list.append({'word': w, 'observed_count': d['parts_observed'],
                    'modal_tariff': d['modal_tariff'],
                    'observed_tariffs': d['tariffs_observed'],
                    'in_syllabus_table': d['in_syllabus_glossary'],
                    'use_in_prompts': d['use_in_prompts'],
                    'used_at_level': d['use_in_prompts'],
                    'exact_mark_tariff': d['modal_tariff'] if d['use_in_prompts'] else None,
                    'exact_mark_tariff_basis': 'modal tariff observed in Papers 2 and 3 (corpus)',
                    'evidence_strength': d['evidence_strength'],
                    'verdict_reason': d['reason'],
                    'primary_assessment_objectives': CW_AO.get(w, []),
                    'assessment_objectives_provenance': 'judgement'})

AO_DEF = {s_['ao']: s_ for s_ in facts.get('assessment_objective_detail', [])}
subs = collections.defaultdict(list)
for s_ in facts.get('assessment_objective_detail', []):
    subs['AO' + str(' ABC'.index(s_['ao']))].append('%s %s' % (s_['code'], s_['text']))

framework = {
 'framework_id': 'FRAMEWORK-6116-NSSCO-2026',
 'generated_by': 'work/nam-6116-nssco-2026/planning/build_plan_inputs.py',
 'authority': ('syllabus scheme of assessment printed p.36 [PDF 39] and specification grid printed '
               'p.37 [PDF 40]; command-word behaviour measured from the papers'),
 'evidence_window': '2020-2025, six series',
 'ao_code_crosswalk': {'AO1': 'NSSCO A', 'AO2': 'NSSCO B', 'AO3': 'NSSCO C',
                       'why': ('build/make_work_order.py and the checks address AOs by code; these are '
                               'the syllabus\'s own A, B and C under build-tool names, not Cambridge AOs')},
 'assessment_objectives': [
   {'code': 'AO1', 'nssco_code': 'A', 'name': 'Knowledge with understanding',
    'definition': ' '.join(subs['AO1']), 'provenance': 'syllabus printed p.35 [PDF 38]'},
   {'code': 'AO2', 'nssco_code': 'B', 'name': 'Handling information, application and solving problems',
    'definition': ' '.join(subs['AO2']), 'provenance': 'syllabus printed p.35 [PDF 38]'},
   {'code': 'AO3', 'nssco_code': 'C',
    'name': 'Practical (experimental and investigative) skills and abilities',
    'definition': ' '.join(subs['AO3']), 'provenance': 'syllabus printed p.36 [PDF 39]'}],
 'papers': [
   {'paper': '1', 'name': 'Theory: Multiple choice questions', 'marks': 40, 'weight_percent': 30,
    'weighting_percent': 30, 'ao_marks': {'AO1': 25, 'AO2': 15, 'AO3': 0},
    'ao_split': {'AO1': 62.5, 'AO2': 37.5, 'AO3': 0},
    'duration_syllabus': '45 minutes', 'duration_2025_paper': '1 hour',
    'duration_2026': 'UNCONFIRMED - open issue'},
   {'paper': '2', 'name': 'Theory: Structured questions', 'marks': 80, 'weight_percent': 50,
    'weighting_percent': 50, 'ao_marks': {'AO1': 50, 'AO2': 30, 'AO3': 0},
    'ao_split': {'AO1': 62.5, 'AO2': 37.5, 'AO3': 0}, 'duration': '1 hour 30 minutes'},
   {'paper': '3', 'name': 'Alternative to Practical Paper', 'marks': 40, 'weight_percent': 20,
    'weighting_percent': 20, 'ao_marks': {'AO1': 0, 'AO2': 0, 'AO3': 40},
    'ao_split': {'AO1': 0, 'AO2': 0, 'AO3': 100}, 'duration': '1 hour 15 minutes'}],
 'papers_provenance': ('names, marks and durations printed p.36 [PDF 39]; weightings and AO marks '
                       'printed p.37 [PDF 40]; ao_split is the AO marks as a share of the paper'),
 'ao_mark_budget': {
   'per_paper_marks': {'P1': {'AO1': 25, 'AO2': 15, 'AO3': 0}, 'P2': {'AO1': 50, 'AO2': 30, 'AO3': 0},
                       'P3': {'AO1': 0, 'AO2': 0, 'AO3': 40}},
   'stated_qualification_weight_percent': {'AO1': 47, 'AO2': 28, 'AO3': 25},
   'stated_basis': ('STATED by the syllabus: the "Overall Weighting across all components" column of '
                    'the specification grid, printed p.37 [PDF 40]. It equals the raw marks: A 75, '
                    'B 45, C 40 of 160. This is the target the AO balance check uses.'),
   'final_grade_weight_percent': {'AO1': 50, 'AO2': 30, 'AO3': 20},
   'final_grade_basis': ('DERIVED, not stated: each paper\'s AO marks as a share of that paper, '
                         'weighted by the stated paper weightings 30/50/20. Recorded for reference; '
                         'no check balances against it.'),
   'recall_ceiling': '"not more than 24% recall" inside AO A; denominator undefined (open issue 1)'},
 'item_mix_target': {'basis': 'marks-equivalent',
                     'target_share_percent': {'AO1': 47, 'AO2': 28, 'AO3': 25},
                     'note': ('The stated overall weighting. Balance the SUBJECT against it, never a '
                              'single topic. Not a card quota.')},
 'command_words_in_use': sorted(w for w, d in cw.items() if d['use_in_prompts']),
 'command_words_listed_but_never_used': sorted(
     w for w, d in cw.items() if d['in_syllabus_glossary'] and d['parts_observed'] == 0),
 'command_words_used_but_not_listed': sorted(
     w for w, d in cw.items() if not d['in_syllabus_glossary'] and d['parts_observed'] > 0),
 'command_word_rule': ('used_at_level = observed_count > 0, the repo rule '
                       '(standard/v0.2.0-draft/mine/assemble.py:144). Words never observed are not '
                       'used to open prompts; their skills stay in scope.'),
 'recall_ceiling': {'stated': 'not more than 24% recall', 'denominator': 'UNDEFINED IN THE SYLLABUS',
                    'status': 'open', 'use': 'not converted into any item count'},
 'corpus_totals': ('Paper 2 contributes 480 marks across its six papers; Paper 3 contributes 240 '
                   'across its six; together 720 across twelve.'),
 'tariff_distribution_observed': dict(sorted(collections.Counter(
     p['mark_tariff'] for p in ev['question_parts']).items())),
 'command_words': cw_list,
 'flashcard_subtype_ao_map': [
   {'subtype': 'DEF', 'assessment_objectives': ['AO1'], 'blooms_level': 'Remember',
    'tests': 'A term defined in the syllabus sense'},
   {'subtype': 'FEATURE', 'assessment_objectives': ['AO1', 'AO3'], 'blooms_level': 'Remember',
    'tests': 'Named parts, features, functions or facts; on a practical objective, the apparatus or reagent'},
   {'subtype': 'PROC', 'assessment_objectives': ['AO1', 'AO3'], 'blooms_level': 'Understand',
    'tests': 'An ordered sequence: a biological process, or the steps of a practical procedure'},
   {'subtype': 'MECH', 'assessment_objectives': ['AO1', 'AO2'], 'blooms_level': 'Understand',
    'tests': 'A full account of a taught multi-step mechanism, every step in order with its cause and effect'},
   {'subtype': 'DIST', 'assessment_objectives': ['AO1', 'AO2'], 'blooms_level': 'Understand',
    'tests': 'The feature that separates two confusable things'},
   {'subtype': 'WHY', 'assessment_objectives': ['AO1', 'AO2', 'AO3'], 'blooms_level': 'Understand',
    'tests': 'The reason for an outcome, a step or a condition'},
   {'subtype': 'CHAIN', 'assessment_objectives': ['AO1', 'AO2'], 'blooms_level': 'Understand',
    'tests': ('A reasoned explanation of a taught relationship, each link stated (Understand: it '
              'reproduces a taught account; applying it to a new case is the APP card)')},
   {'subtype': 'APP', 'assessment_objectives': ['AO1', 'AO2', 'AO3'], 'blooms_level': 'Apply',
    'tests': ('Taught biology applied to a situation the learner has not met (B7); on a practical '
              'objective, knowledge applied to interpret an unfamiliar experiment (C4); also producing a '
              'labelled drawing from a specimen or image, and constructing a key')},
   {'subtype': 'CALC', 'assessment_objectives': ['AO2', 'AO3'], 'blooms_level': 'Apply',
    'tests': 'A calculation with working and units'},
   {'subtype': 'INTERP', 'assessment_objectives': ['AO2', 'AO3'], 'blooms_level': 'Analyse',
    'tests': 'Reading, completing, plotting or concluding from a table, graph or diagram'},
   {'subtype': 'LIM', 'assessment_objectives': ['AO3'], 'blooms_level': 'Evaluate',
    'tests': 'A source of error or limitation in a method, and an improvement tied to it'},
   {'subtype': 'EVAL', 'assessment_objectives': ['AO1', 'AO2', 'AO3'], 'blooms_level': 'Evaluate',
    'tests': 'A judgement weighed from both sides, for an objective that is itself two-sided'},
   {'subtype': 'SYNTH', 'assessment_objectives': ['AO3'], 'blooms_level': 'Create',
    'tests': 'A complete investigation plan: what is changed, measured and kept the same, how, and repeats (devising a procedure)'},
   {'subtype': 'MISCON', 'assessment_objectives': ['AO1', 'AO2', 'AO3'], 'blooms_level': 'Understand',
    'tests': 'An examiner-evidenced confusion, discriminated'}],
 'flashcard_subtype_ao_map_note': ('The AOs a subtype may carry. Which one a slot carries is set by '
                                   'the explicit proposed demand audit planning/ao_demand_audit.json, applied '
                                   'after the subject-profile base build. Subtype/objective type alone does not determine it.'),
 'blooms_taxonomy': {
   'levels': [{'level': l} for l in ['Remember', 'Understand', 'Apply', 'Analyse', 'Evaluate', 'Create']],
   'by_performance_task': {'multiple_choice_set': 'Apply', 'short_answer': 'Analyse',
                           'practical_task': 'Evaluate'}},
 'excluded_from_planning_inputs': ['topic-difficulty rankings from examiner scoring percentages '
                                   '(Paper 1 only, n=1 for three sub-topics, operator-excluded '
                                   '2026-10-17)'],
}
json.dump(framework, open(f'{WS}/curriculum/assessment-framework.json', 'w'), indent=2, ensure_ascii=False)

# ---- coverage and proposed activity mix ------------------------------------
by_topic = collections.defaultdict(lambda: collections.Counter())
for o in leaf:
    by_topic[o['topic_id']][o['assessment_objectives'][0]] += 1
titles = {r['code']: r['title'] for r in facts['content'] if r['code'].isdigit()}

ao_tot = collections.Counter(o['assessment_objectives'][0] for o in leaf)
n = sum(ao_tot.values())
mix = collections.Counter(o['objective_type'] for o in leaf)

print('COVERAGE BY TOPIC (every objective mandatory)')
print(f"{'topic':<6}{'title':<46}{'obj':>5}{'A':>6}{'B':>5}{'C':>5}")
for t in sorted(by_topic):
    c = by_topic[t]; tot = sum(c.values())
    print(f"{t:<6}{titles.get(t,'')[:44]:<46}{tot:>5}{c['AO1']:>6}{c['AO2']:>5}{c['AO3']:>5}")
print(f"{'':<52}{n:>5}{ao_tot['AO1']:>6}{ao_tot['AO2']:>5}{ao_tot['AO3']:>5}")
print(f"{'% of objectives':<52}{'':>5}{ao_tot['AO1']/n*100:>5.0f}%{ao_tot['AO2']/n*100:>4.0f}%{ao_tot['AO3']/n*100:>4.0f}%")
print(f"{'syllabus raw-mark target':<52}{'':>5}{'47%':>6}{'28%':>5}{'25%':>5}")
print(f"{'final-grade target':<52}{'':>5}{'50%':>6}{'30%':>5}{'20%':>5}")
print('\nOBJECTIVE TYPE MIX (drives flashcard subtypes)')
for k, v in mix.most_common():
    print(f"   {k:<22}{v:>4}  {v/n*100:>4.0f}%")
usable = [w for w, d in cw.items() if d['use_in_prompts']]
print(f"\ncommand words usable in prompts: {len(usable)} of {len(cw)}")
print('   ' + ', '.join(sorted(usable)))
print('   NOT used as openers (skills still in scope): ' +
      ', '.join(sorted(w for w, d in cw.items() if not d['use_in_prompts'])))
