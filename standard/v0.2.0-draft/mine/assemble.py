# -*- coding: utf-8 -*-
"""Write the corpus findings into the two subject workspaces."""
import json, os, re, shutil, datetime, collections
ROOT = os.path.expanduser('~/mine')
OUT  = os.path.join(ROOT, 'out')
REPO = os.path.expanduser('~/mnt/YYeni Study Resources')
WS   = {'0450': os.path.join(REPO, 'work/cie-0450-igcse-2026'),
        '0455': os.path.join(REPO, 'work/cie-0455-igcse-2026')}
NOW  = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

def rd(p): return json.load(open(p))
def wr(p, o):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + '.tmp'
    json.dump(o, open(tmp, 'w'), indent=1)
    shutil.move(tmp, p)
    return p

# A role suffixed '?' is dropped, not merged, when the subject has no AO for it.
# Discriminating two terms is understanding, not analysis: in a subject with a
# distinct Application objective DIST earns it, and in one without, it does not
# silently become an analysis card.
# subtype -> (AO roles, what it tests, revised Bloom's level)
# Bloom is a property of the COGNITIVE DEMAND, which is not the same thing as the
# assessment objective. 0455 has no Application AO, but an 0455 card that asks a
# learner to draw a demand curve for a stated change is still Bloom Apply. Both
# labels ride on every item because they answer different questions: the AO says
# what the exam credits, Bloom says what the learner is being asked to do.
SUBTYPE_AO_ROLE = [
 ('DEF',      ['knowledge'],                 'Precise meaning of one term', 'Remember'),
 ('FEATURE',  ['knowledge'],                 'Essential features', 'Remember'),
 ('PROC',     ['knowledge'],                 'Ordered stages of a process', 'Remember'),
 ('WHY',      ['knowledge', 'analysis'],     'Purpose or reason', 'Understand'),
 ('DIST',     ['knowledge', 'application?'], 'Boundary between two confusable concepts', 'Understand'),
 ('MISCON',   ['knowledge'],                 'Discriminating a concept from the one it is confused with', 'Understand'),
 ('MECH',     ['analysis'],                  'The mechanism by which one thing causes another', 'Understand'),
 ('APP',      ['application'],               'A point worked through a named context', 'Apply'),
 ('CALC',     ['knowledge', 'application?'], 'A calculation with formula, working and units', 'Apply'),
 ('DIAGRAM',  ['analysis'],                  'Drawing a correctly labelled diagram, element by element', 'Apply'),
 ('BEN',      ['analysis'],                  'A benefit, developed to its consequence', 'Analyse'),
 ('LIM',      ['analysis'],                  'A limitation, developed to its consequence', 'Analyse'),
 ('CHAIN',    ['analysis'],                  'Condition, mechanism, consequence, for whom', 'Analyse'),
 ('INTERP',   ['analysis'],                  'Reading meaning out of data or a diagram', 'Analyse'),
 ('EVAL',     ['evaluation'],                'A judgement with a decisive criterion and the case against', 'Evaluate'),
 ('SYNTH',    ['analysis', 'evaluation'],    'Joining two objectives into one argument', 'Evaluate'),
]

BLOOMS = [
 ('Remember',  'Recall a fact, a term or a list, as stated.'),
 ('Understand','Explain an idea in the learner\u2019s own words, or tell it apart from a '
               'neighbouring one.'),
 ('Apply',     'Use the idea on a case, a figure or a diagram the learner has not been '
               'given the answer to.'),
 ('Analyse',   'Break a situation into its parts and trace a cause through to its '
               'consequence for a named party.'),
 ('Evaluate',  'Weigh two sides against a criterion and reach a judgement that could have '
               'gone the other way.'),
 ('Create',    'Build something new from the parts. Rare below A Level; used here only for '
               'extended performance tasks that ask a learner to design or plan.'),
]

PERF_BLOOM = {'short_answer': 'Analyse', 'data_response': 'Analyse',
              'essay_plan': 'Evaluate', 'case_analysis': 'Evaluate',
              'multiple_choice_set': 'Understand'}

def role_map(aos):
    m = {}
    for a in aos:
        n = a['name'].lower()
        for w in ('knowledge', 'application', 'analysis', 'evaluation'):
            if w in n:
                m[w] = a['code']
    m['_has_application'] = 'application' in m
    if 'application' not in m and 'analysis' in m:
        m['application'] = m['analysis']
    return m

def subtype_map(aos):
    rm = role_map(aos)
    out = []
    for st, roles, tests, bloom in SUBTYPE_AO_ROLE:
        codes = []
        for r in roles:
            optional = r.endswith('?')
            r = r.rstrip('?')
            if optional and not rm.get('_has_application'):
                continue
            c = rm.get(r)
            if c and c not in codes:
                codes.append(c)
        out.append({'subtype': st, 'assessment_objectives': codes or [aos[0]['code']],
                    'tests': tests, 'blooms_level': bloom})
    return out

def ao_budget(fw):
    per, comb = {}, collections.Counter()
    total = sum(p['marks'] for p in fw['papers'])
    for p in fw['papers']:
        per['P' + p['paper']] = {a: round(p['marks'] * v / 100.0)
                                 for a, v in p['ao_split'].items()}
        for a, v in per['P' + p['paper']].items():
            comb[a] += v
    return {'per_paper': per,
            'combined_marks_out_of_%d' % total: dict(comb),
            'stated_qualification_weight_percent':
                {a['code']: a['qualification_weight_percent']
                 for a in fw['assessment_objectives']},
            'arithmetic_note':
                'Each paper\'s stated AO percentages applied to its own mark total, then summed. '
                'The syllabus states AO weights as a share of MARKS, so every AO calculation '
                'downstream is marks-equivalent, never an item count.'}

# ---------------------------------------------------------------- frameworks
for code in ('0450', '0455'):
    fw = rd(os.path.join(OUT, '%s_assessment_framework.json' % code))
    fw['ao_mark_budget'] = ao_budget(fw)
    fw['flashcard_subtype_ao_map'] = subtype_map(fw['assessment_objectives'])
    fw['blooms_taxonomy'] = {
        'scheme': "Revised Bloom's taxonomy (Anderson and Krathwohl).",
        'why_both': 'The assessment objective says what the examination credits. The '
                    'Bloom level says what the learner is being asked to do. They are '
                    'different axes and an item carries both: a subject whose assessment '
                    'objectives do not name application still sets cards that ask a learner '
                    'to apply something, and those are Bloom Apply whatever AO credits them.',
        'levels': [{'level': k, 'means': v} for k, v in BLOOMS],
        'by_subtype': {st: b for st, _, _, b in SUBTYPE_AO_ROLE},
        'by_performance_task': dict(PERF_BLOOM),
        'required_on_every_item': True}
    fw['item_mix_target'] = {
        'basis': 'marks-equivalent',
        'target_share_percent': fw['ao_mark_budget']['stated_qualification_weight_percent'],
        'note': 'Balance the SUBJECT against this, never a single topic.'}
    fw['command_words_in_use'] = sorted(
        [c['word'] for c in fw['command_words'] if c['observed_count'] > 0])
    fw['command_words_listed_but_never_used'] = sorted(
        [c['word'] for c in fw['command_words']
         if c['in_syllabus_table'] and c['observed_count'] == 0])
    fw['command_words_used_but_not_listed'] = sorted(
        [c['word'] for c in fw['command_words']
         if not c['in_syllabus_table'] and c['observed_count'] >= 5])
    # the generator reads exact_mark_tariff / used_at_level; supply both, measured
    for c in fw['command_words']:
        c['exact_mark_tariff'] = c['modal_tariff']
        c['used_at_level'] = c['observed_count'] > 0
    wr(os.path.join(WS[code], 'curriculum', 'assessment-framework.json'), fw)
    print('%s framework: %d words in use, %d listed-but-unused %s'
          % (code, len(fw['command_words_in_use']),
             len(fw['command_words_listed_but_never_used']),
             fw['command_words_listed_but_never_used']))

# ---------------------------------------------------------------- exposure
for code in ('0450', '0455'):
    wr(os.path.join(WS[code], 'curriculum', 'exam-exposure.json'),
       rd(os.path.join(OUT, '%s_exam_exposure.json' % code)))

# ------------------------------------------------- 0455 registry + units
wr(os.path.join(WS['0455'], 'curriculum', 'objective_registry.json'),
   rd(os.path.join(OUT, '0455_objective_registry.json')))
wr(os.path.join(WS['0455'], 'curriculum', 'unit_titles.json'),
   rd(os.path.join(OUT, '0455_unit_titles.json')))

# ---------------------------------------------------------------- answer shapes
shapes = rd(os.path.join(OUT, 'answer_shapes.json'))
for code in ('0450', '0455'):
    wr(os.path.join(WS[code], 'curriculum', 'answer-shapes.json'),
       {'_provenance': shapes['_provenance'], code: shapes[code]})

# ---------------------------------------------------------------- misconceptions
reg = rd(os.path.join(OUT, 'misconception_register.json'))
for code in ('0450', '0455'):
    items = reg[code]
    wr(os.path.join(WS[code], 'curriculum', 'misconceptions.json'), {
        'register_id': 'MISCON-CIE-%s-IGCSE-2026' % code,
        'generated_at': NOW,
        'authority': 'Cambridge Principal Examiner Reports for Teachers, %s, 17 series '
                     '2020-2025. Each entry is a confusion the reports state candidates '
                     'actually made.' % code,
        'derivation_policy': 'Examiner-evidenced misconceptions are mined and restated. '
                             'No examiner-report wording appears in learner-facing output.',
        'how_to_use': 'Every entry earns one MISCON card on the objective it attaches to. '
                      'A MISCON card is a DISCRIMINATION card: it states the boundary between '
                      'the two ideas and gives the test that separates them. It does not simply '
                      'restate the correct definition.',
        'kinds': {
            'adjacent_concept': 'Two different concepts that sit near each other in the syllabus.',
            'near_neighbour_term': 'Two terms that share most of their wording.',
            'wrong_angle_same_concept': 'The right concept answered from the wrong angle - '
                                        'a function given where a role was asked for, a benefit '
                                        'where a definition was asked for.',
            'cause_vs_consequence': 'Causes given where consequences were asked for, or the reverse.',
            'opposite_direction': 'The right mechanism run the wrong way.'},
        'entries': sorted(items, key=lambda x: (x.get('topic_id') or 'zz', -x['n']))})
    print('%s misconceptions: %d entries' % (code, len(items)))

# ---------------------------------------------------------------- 0455 glossary
# Seeded from the examiner-evidenced confusions: the terms candidates actually
# mix up are exactly the terms whose boundaries have to be settled up front.
terms = collections.OrderedDict()
for e in reg['0455']:
    for side, other in ((e['a'], e['b']), (e['b'], e['a'])):
        t = side.strip()
        if 3 < len(t) < 40 and ' rather than ' not in t:
            terms.setdefault(t, set()).add(other.strip())
gloss = [{'term': t, 'sense': None,
          'homonym_warning': 'Candidates have confused this with: %s.'
                             % '; '.join(sorted(v)[:3])}
         for t, v in list(terms.items())[:70]]
wr(os.path.join(WS['0455'], 'curriculum', 'glossary.json'), {
    'glossary_id': 'GLOSSARY-CIE-0455-IGCSE-2026',
    'status': 'seeded_from_examiner_evidence',
    'note': 'Seeded with the terms Principal Examiner Reports record candidates confusing, '
            'so the boundary is settled before authoring rather than after review. An author '
            'writes the sense once, uses it everywhere, and does not invent alternatives. '
            'A term whose sense is still null must be settled before its topic is authored.',
    'terms': gloss})
print('0455 glossary: %d seeded terms' % len(gloss))
