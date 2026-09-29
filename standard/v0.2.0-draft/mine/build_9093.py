# -*- coding: utf-8 -*-
"""Build the complete 9093 AS plan: curriculum files, contracts, work orders. PLAN and HANDOVER come from docs_9093.py.

    python3 build_9093.py

Refuses to run until step zero (syllabus-facts.json) and step one (the corpus analysis) exist.
Every objective's syllabus text is verified against the page it cites before anything is written.
Regenerate, never edit, what this writes.
"""
import collections
import datetime
import json
import os
import re
import statistics
import subprocess
import sys

import yaml

HOME = os.path.expanduser('~')
REPO = os.path.join(HOME, 'mnt', 'YYeni Study Resources')
MINE = os.path.join(HOME, 'mine')
STD = os.path.join(REPO, 'standard', 'v0.2.0-draft')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(STD, 'build'))
sys.path.insert(0, os.path.join(MINE, 'gen'))
from design_9093 import (CODE, SLUG, WS_NAME, UNITS, TOPICS, F, P, TEXTS, MISCONCEPTIONS, GLOSSARY,  # noqa: E402
                         VARIANT_REGISTER, CONDITIONED, NOT_IN_ROUTE)
from gates import require_prerequisites  # noqa: E402
from naming import notes_filename, flashcards_filename, topic_label  # noqa: E402
from er9093 import load as load_er  # noqa: E402
from mtest9093 import CUE  # noqa: E402

WS = os.path.join(REPO, 'work', WS_NAME)
CUR = os.path.join(WS, 'curriculum')
REL = 'work/' + WS_NAME
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
ANALYSIS = 'operations/analysis/%s-%s-corpus-analysis.md' % (CODE, SLUG)

require_prerequisites(WS)
FACTS = json.load(open(os.path.join(CUR, 'syllabus-facts.json')))
PDF = os.path.join(REPO, FACTS['source_document'])
PAGES = subprocess.run(['pdftotext', '-layout', PDF, '-'], capture_output=True, text=True, check=True).stdout.split('\f')
RAW = subprocess.run(['pdftotext', PDF, '-'], capture_output=True, text=True, check=True).stdout.split('\f')


def norm(s):
    for a, b in (('–', '-'), ('—', '-'), ('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"')):
        s = s.replace(a, b)
    s = re.sub(r'\s*/\s*', '/', s)
    return re.sub(r'\s+', ' ', s).strip().lower().rstrip('.')


def on_page(text, page):
    """Verbatim on the page, in the layout reading or the column reading (the content tables are two columns)."""
    return norm(text) in norm(PAGES[page - 1]) or norm(text) in norm(RAW[page - 1])


# ------------------------------------------------------------------------------------------ BLOOM
SUBTYPE = collections.OrderedDict([
 ('DEF', ('Precise meaning of one term', 'Remember', 1)),
 ('FEATURE', ('The features or conventions of a form, or what a strong piece of a given kind contains', 'Remember', 2)),
 ('PROC', ('The ordered steps of a technique', 'Remember', 2)),
 ('WHY', ('The reason a technique works', 'Understand', 2)),
 ('DIST', ('The boundary between two confusable ideas, and the test that separates them', 'Understand', 2)),
 ('MISCON', ('Discriminating a recorded error from the move it is confused with', 'Understand', 3)),
 ('APP', ('A technique carried out on a supplied original sentence or extract', 'Apply', 3)),
 ('MECH', ('How a choice in a supplied original sentence or extract produces its effect', 'Analyse', 3)),
 ('INTERP', ('Reading form, audience, purpose or implied meaning out of a supplied detail', 'Analyse', 3)),
 ('EVAL', ('A judgement between two versions, or on how convincing a supplied passage is, with the case against', 'Evaluate', 4)),
])
BLOOM_LEVELS = [
 ('Remember', 'Recall a term, a convention or the steps of a technique, as stated.'),
 ('Understand', 'Explain an idea in the learner’s own words, or tell it apart from a neighbouring one.'),
 ('Apply', 'Carry out a technique on a sentence, an extract or a text the learner has not seen answered.'),
 ('Analyse', 'Break a text into its choices of form, structure and language, and show how they make meaning for an audience. '
             'Forty of the hundred AS marks are for this.'),
 ('Evaluate', 'Judge which of two versions better fulfils a brief, or how convincing a passage is, against a reason.'),
 ('Create', 'Compose something new: a directed response, a shorter piece, a story, a description, an argument, a review. '
            'This is 55 of the hundred AS marks with the directed response included.'),
]
PERF_TYPES = {'short_answer': 'Analyse (short analyses of an extract in the prompt) or Apply (editing, rewriting, paragraph building), as the slot says',
              'writing_task': 'Create', 'source_analysis': 'Analyse', 'essay_plan': 'Create'}

ANSWER_STRUCTURES = {
 'DEF': ['meaning|means|definition|defined|refers'],
 'FEATURE': ['feature|features|convention|conventions|includes|contains|expected'],
 'PROC': ['step|steps|first|then|order|sequence'],
 'WHY': ['reason|because|why|purpose'],
 'DIST': ['difference|distinguish|whereas|contrast|boundary|test'],
 'MISCON': ['error|mistake|confuse|confused|confusion|wrongly|instead'],
 'APP': ['text|sentence|extract|passage|words', 'because|suggests|shows|so'],
 'MECH': ['effect|creates|suggests|reader|audience', 'word|words|phrase|quotation|sentence'],
 'INTERP': ['detail|word|phrase|evidence|feature', 'suggests|implies|shows|signals'],
 'EVAL': ['judgement|judge|convincing|stronger|better', 'evidence|reason|support', 'however|but|counter|weakness'],
 'short_answer': ['evidence|quotation|words', 'effect|purpose|audience'],
 'source_analysis': ['form|structure|language', 'audience|purpose|meaning', 'level|levels|mark|marks'],
 'essay_plan': ['structure|section|sections|paragraph|paragraphs', 'purpose|audience|effect', 'words|word'],
 'writing_task': ['level|levels|band', 'audience|purpose|form', 'organised|organisation|structure|structured|sequence',
                  'accuracy|accurate|vocabulary|language'],
}

# --------------------------------------------------------------------------------- CORPUS COUNTS
TK = json.load(open(os.path.join(MINE, 'out', '9093_tasks.json')))
THR = json.load(open(os.path.join(MINE, 'out', '9093_thresholds.json')))
SYSF = json.load(open(os.path.join(MINE, 'out', '9093_systemic.json')))
N_P1, N_P2 = TK['papers']['P1'], TK['papers']['P2']
N_SERIES = len(TK['series'])


def corpus_command_words():
    import glob
    cw = collections.defaultdict(collections.Counter)
    for f in sorted(glob.glob(os.path.join(MINE, '9093', '9093_*_qp_[12]*.txt'))):
        s = os.path.basename(f).split('_')[1]
        if s not in TK['series']:
            continue
        t = re.sub(r'\s+', ' ', open(f, errors='replace').read())
        for w, tar in (('Analyse', 25), ('Compare', 15), ('Discuss', None)):
            for m in re.finditer(r'\b%s\b(.{0,400}?)\[(\d+)\]' % w, t):
                cw[w][int(m.group(2))] += 1
    return cw


CW = corpus_command_words()
ER = load_er()
N_ER = len({e['series'] for e in ER})
N_ER_VAR = {p: len({(e['series'], e['variant']) for e in ER if e['paper'] == p}) for p in ('1', '2')}


def evidence(m):
    r = re.compile(m[7], re.I)
    h = [e for e in ER if e['task'] in m[3] and (e['error'] or CUE.search(e['sentence'])) and r.search(e['sentence'])]
    return {'statements': len(h), 'report_variants': len({(e['series'], e['variant']) for e in h}),
            'series': len({e['series'] for e in h})}


# ------------------------------------------------------------------------------- TASK SPECS (shapes)
def L(level, marks, text):
    return {'level': level, 'marks': marks, 'requires': text}


def forms(key, n=None):
    return ', '.join('%s %d' % (f, c) for f, c in TK[key] if f)


READ5_Q1 = [L(5, '5', 'a subtle, assured grasp of the source’s meaning, context and audience; its typical features drawn on perceptively'),
            L(4, '4', 'a thorough grasp of the source’s meaning, context and audience; its typical features drawn on well'),
            L(3, '3', 'a secure grasp of meaning, context and audience; its typical features drawn on plainly'),
            L(2, '2', 'a partial grasp of meaning, context and audience; little use of its typical features'),
            L(1, '1', 'a slight grasp of the source; almost no use of its typical features')]
TASKS = collections.OrderedDict()
TASKS['P1-Q1a'] = {
 'paper': 'P1', 'name': 'Question 1(a), directed response', 'text': 'one unseen text of about 550–750 words', 'marks': 10,
 'split': {'reading': {'marks': 5, 'assessment_objectives': ['AO1']}, 'writing': {'marks': 5, 'assessment_objectives': ['AO2']}},
 'length': '150–200 words', 'provenance': 'syllabus, page 19 (the task, the lengths, AO1 and AO2); the 5 + 5 split is corpus, from the mark schemes',
 'set_as': ('a new form for a named audience and purpose, re-using the source’s content (corpus). Forms set in the %d papers: %s. '
            'A role is given in 24 of the %d.' % (N_P1, forms('p1_q1_form'), N_P1)),
 'word_range_rule': 'no fixed deduction for the count; an answer well outside the range is marked as a poorer fit to the form and purpose (corpus, every scheme)',
 'tables': [
  {'table': 'reading (AO1)', 'out_of': 5, 'levels': READ5_Q1},
  {'table': 'writing (AO2)', 'out_of': 5, 'levels': [
   L(5, '5', 'assured, highly accurate writing; everything suits the audience and purpose, and ideas are developed with subtlety from start to finish'),
   L(4, '4', 'effective writing with only small slips that never obscure meaning; content suits the audience and purpose, ideas developed well'),
   L(3, '3', 'clear writing with occasional slips; content suits the audience and purpose, ideas developed plainly'),
   L(2, '2', 'clear but uneven writing, with frequent slips that mostly leave meaning intact; content mostly suits the task, thin development'),
   L(1, '1', 'basic writing whose errors often obscure meaning; content may drift from the audience and purpose, almost no development')]}]}
TASKS['P1-Q1b'] = {
 'paper': 'P1', 'name': 'Question 1(b), comparison', 'text': 'the Question 1(a) source and the candidate’s own response', 'marks': 15,
 'command_word': 'Compare',
 'split': {'reading': {'marks': 5, 'assessment_objectives': ['AO1']}, 'analysis': {'marks': 10, 'assessment_objectives': ['AO3']}},
 'provenance': 'syllabus, page 19 (the task, AO1 and AO3); the 5 + 10 split is corpus, from the mark schemes',
 'set_as': 'the instruction opens with Compare and names form, structure and language in all %d papers (corpus)' % N_P1,
 'organisation_rule': 'form, structure and language need not be taken in separate sections (corpus, every scheme)',
 'tables': [
  {'table': 'reading (AO1)', 'out_of': 5, 'levels': [
   L(5, '5', 'a subtle comparative grasp of both texts’ meaning, context and audience; typical features drawn on perceptively'),
   L(4, '4', 'a thorough comparative grasp of both texts; typical features drawn on well'),
   L(3, '3', 'a secure comparative grasp of both texts; typical features drawn on plainly'),
   L(2, '2', 'a partial grasp of the texts with little comparison; little use of typical features'),
   L(1, '1', 'a slight grasp of the texts with almost no comparison; almost no use of typical features')]},
  {'table': 'analysis (AO3)', 'out_of': 10, 'levels': [
   L(5, '9-10', 'a subtle, assured comparison of form, structure and language across both texts, explaining with precision how each writer’s choices suit its audience and create meaning'),
   L(4, '7-8', 'a detailed comparison of form, structure and language across both texts, and of how the choices suit each audience and create meaning'),
   L(3, '5-6', 'a clear comparison of form, structure or language across the texts, and of how the choices suit audience and meaning'),
   L(2, '3-4', 'some analysis of form, structure or language but little comparison; choices only loosely tied to audience and meaning'),
   L(1, '1-2', 'very little analysis or comparison; choices hardly tied to audience or meaning')]}]}
TASKS['P1-Q2'] = {
 'paper': 'P1', 'name': 'Question 2, text analysis', 'text': 'one unseen text of about 550–750 words', 'marks': 25,
 'command_word': 'Analyse',
 'split': {'reading': {'marks': 5, 'assessment_objectives': ['AO1']}, 'analysis': {'marks': 20, 'assessment_objectives': ['AO3']}},
 'provenance': 'syllabus, page 20 (the task, AO1 and AO3); the 5 + 20 split is corpus, from the mark schemes',
 'set_as': 'Analyse, focusing on form, structure and language, in all %d papers (corpus). Sources: %s' % (N_P1, forms('p1_q2_source')),
 'tables': [
  {'table': 'reading (AO1)', 'out_of': 5, 'levels': [
   L(5, '5', 'a subtle, assured grasp of the text’s meaning, context and audience; its typical features drawn on perceptively'),
   L(4, '4', 'a thorough grasp of meaning, context and audience; its typical features drawn on well'),
   L(3, '3', 'a secure grasp of meaning, context and audience; its typical features drawn on plainly'),
   L(2, '2', 'a partial grasp of meaning, context and audience; little use of its typical features'),
   L(1, '1', 'a slight grasp of the text; almost no use of its typical features')]},
  {'table': 'analysis (AO3)', 'out_of': 20, 'levels': [
   L(5, '17-20', 'an assured, coherent analysis that is very well organised; features chosen with insight; a subtle sense of how the writer’s choices suit the audience and make meaning; exact, apt language joining evidence to comment'),
   L(4, '13-16', 'a detailed, coherent, well-organised analysis; well-chosen features; a detailed sense of how the choices suit the audience and make meaning; effective language joining evidence to comment'),
   L(3, '9-12', 'a clear, coherent analysis with a sound structure; suitable features chosen; a clear sense of how the choices suit the audience and make meaning; clear language joining evidence to comment'),
   L(2, '5-8', 'some structure but limited coherence; some suitable features chosen; a limited sense of the writer’s choices; an attempt to join evidence to comment'),
   L(1, '1-4', 'a basic analysis with little structure; few features chosen; little sense of the writer’s choices; evidence and comment barely joined')]}]}
WRITE5 = lambda bands: [
 L(5, bands[0], 'assured expression drawing on a broad repertoire of structures and vocabulary, some complex or unusual; very few errors; organised with clear logic and strong effect, ideas developed with subtlety throughout; the task achieved in full, everything relevant; the audience held throughout'),
 L(4, bands[1], 'effective expression using a range of structures and vocabulary, some complex or unusual; a few small slips that never obscure meaning; logically organised, ideas developed effectively; the task well achieved, content relevant; the audience engaged'),
 L(3, bands[2], 'clear expression with some complex structures and some unusual vocabulary, perhaps with repetition; occasional slips that do not obscure meaning; clearly organised, ideas developed clearly; the task achieved, content relevant; the audience addressed'),
 L(2, bands[3], 'clear expression that may not flow, in mostly common structures and vocabulary; frequent slips that mostly leave meaning intact; some organisation, thin development; the task broadly achieved, content mostly relevant; little sense of the audience'),
 L(1, bands[4], 'basic expression in mostly simple structures and common words; errors that obscure meaning; little organisation or development; the task misread or only partly done, some content irrelevant; almost no sense of the audience')]
TASKS['P2-Q1a'] = {
 'paper': 'P2', 'name': 'Question 1(a), shorter writing', 'marks': 15, 'assessment_objectives': ['AO2'],
 'length': 'no more than 400 words', 'provenance': 'syllabus, page 20',
 'set_as': ('a form for a named audience and purpose; in %d of the %d papers the prompt adds a focus sentence (corpus). Forms: %s'
            % (TK['p2_q1_focus'], N_P2, forms('p2_q1_form'))),
 'marking_rules': ('expression and accuracy count equally with development and organisation; each strand counts equally inside a '
                   'level; the word limit is judged as part of task achievement, not by deduction (corpus, every scheme)'),
 'tables': [{'table': 'writing (AO2)', 'out_of': 15, 'strands': ['expression and range', 'accuracy', 'organisation and development',
                                                                  'task achievement and relevance', 'engagement of the audience'],
             'levels': WRITE5(['13-15', '10-12', '7-9', '4-6', '1-3'])}]}
TASKS['P2-Q1b'] = {
 'paper': 'P2', 'name': 'Question 1(b), reflective commentary', 'marks': 10, 'assessment_objectives': ['AO3'],
 'text': 'the candidate’s own Question 1(a) text', 'provenance': 'syllabus, page 20',
 'tables': [{'table': 'analysis (AO3)', 'out_of': 10, 'levels': [
   L(5, '9-10', 'assured analysis of the text’s form, structure and language, and of how the choices suit its audience and shape its meaning'),
   L(4, '7-8', 'detailed analysis of form, structure and language, and of how the choices suit the audience and shape meaning'),
   L(3, '5-6', 'clear analysis of form, structure and language, and of how the choices suit the audience and shape meaning'),
   L(2, '3-4', 'limited analysis of form, structure or language, and of how the choices suit the audience'),
   L(1, '1-2', 'minimal analysis of form, structure or language, and of how the choices suit the audience')]}]}
TASKS['P2-B'] = {
 'paper': 'P2', 'name': 'Section B, extended writing', 'marks': 25, 'assessment_objectives': ['AO2'],
 'length': '600–900 words', 'choice': 'one question from three, one per category: imaginative/descriptive, discursive/argumentative, review/critical',
 'provenance': 'syllabus, page 21',
 'set_as': ('one question per category in all %d papers, in six different orders, so a question number never identifies a category; '
            'imaginative/descriptive: narrative 19, descriptive 15, a focus added in 33, a given sentence in 9; discursive/argumentative: '
            'article 14, essay 12, speech 8, letter 4; review/critical: a review in all 34 (corpus)' % N_P2),
 'tables': [{'table': 'writing (AO2)', 'out_of': 25, 'strands': ['expression and range', 'accuracy', 'organisation and development',
                                                                  'task achievement and relevance', 'engagement of the audience'],
             'levels': WRITE5(['21-25', '16-20', '11-15', '6-10', '1-5'])}]}
TOPIC_TASKS = {'1.1': ['P1-Q1a', 'P1-Q1b', 'P1-Q2', 'P2-Q1a', 'P2-B'], '1.2': ['P1-Q1b', 'P1-Q2', 'P2-Q1b'],
               '1.3': ['P1-Q1b', 'P1-Q2', 'P2-Q1b'], '1.4': ['P1-Q1a', 'P1-Q1b'], '1.5': ['P1-Q2'],
               '2.1': ['P2-Q1a', 'P2-Q1b'], '2.2': ['P2-B'], '2.3': ['P2-B'], '2.4': ['P2-B'], '2.5': ['P2-B'],
               '2.6': ['P1-Q1a', 'P2-Q1a', 'P2-B']}

# ------------------------------------------------------------------------------------ VALIDATE
problems = []
OBJ = {}          # (topic, key) -> objective record
for t in TOPICS:
    cont_text, cont_page = t['container']
    if not on_page(cont_text, cont_page):
        problems.append('%s container not on page %d: %s' % (t['id'], cont_page, cont_text))
    per = collections.Counter()
    for (k, st, txt, pg, aos, cws, learner, tier) in t['objectives']:
        if not on_page(txt, pg):
            problems.append('%s-%s not on page %d: %s' % (t['id'], k, pg, txt))
        per[st] += 1
        OBJ[(t['id'], k)] = {'id': 'OBJ-%s-%s-%02d' % (CODE, st, per[st]), 'sub_topic': st, 'syllabus_text': txt, 'page': pg,
                             'aos': aos, 'cws': cws, 'learner': learner, 'tier': tier, 'papers': t['papers']}
        if 'AO1' in aos and t['papers'] == ['2']:
            problems.append('%s-%s claims AO1 but Paper 2 assesses no AO1' % (t['id'], k))
MC = {m[0]: m for m in MISCONCEPTIONS}
for tid, slots in F.items():
    for s in slots:
        if (tid, s[0]) not in OBJ:
            problems.append('%s slot on unknown objective %s' % (tid, s[0]))
        if s[1] not in SUBTYPE:
            problems.append('%s unknown subtype %s' % (tid, s[1]))
        if s[1] == 'MISCON':
            m = MC.get(s[5])
            if not m or m[1] != tid or m[2] != s[0]:
                problems.append('%s MISCON slot %s does not match its misconception' % (tid, s[5]))
EVID = {}
for m in MISCONCEPTIONS:
    if not any(s[5] == m[0] for s in F.get(m[1], [])):
        problems.append('misconception %s has no MISCON slot' % m[0])
    EVID[m[0]] = evidence(m)
    if not EVID[m[0]]['statements']:
        problems.append('misconception %s has no evidence in the examiner reports' % m[0])
for t in TOPICS:
    tid = t['id']
    for (k, *_r) in t['objectives']:
        o = OBJ[(tid, k)]
        if not any(s[0] == k for s in F[tid]):
            problems.append('%s-%s has no flashcard' % (tid, k))
        if not any(k in p['keys'] for p in P[tid]):
            problems.append('%s-%s is exercised by no performance task' % (tid, k))
        for cw in o['cws']:
            if not (any(s[0] == k and s[3] == cw for s in F[tid]) or any(k in p['keys'] and p['command_word'] == cw for p in P[tid])):
                problems.append('%s-%s carries %s but no slot instructs with it (C-15)' % (tid, k, cw))
    for p in P[tid]:
        if not set(p['aos']) <= {a for k in p['keys'] for a in OBJ[(tid, k)]['aos']} | set(p['ao_marks']):
            problems.append('%s task AOs %s outside its objectives' % (tid, p['aos']))
        if p['ao_marks'] and sum(p['ao_marks'].values()) != p['mark_tariff']:
            problems.append('%s task AO marks do not sum to its tariff' % tid)
# the AO balance, in marks, against the syllabus weights
AOM = collections.Counter()
for tid in P:
    for p in P[tid]:
        for a, v in p['ao_marks'].items():
            AOM[a] += v
AO_TOT = sum(AOM.values())
AO_SHARE = {a: round(100 * AOM.get(a, 0) / AO_TOT) for a in ('AO1', 'AO2', 'AO3')}
AO_SYL = FACTS['ao_weights']['qualification_percent']
AO_GAP = max(abs(AO_SHARE[a] - AO_SYL[a]) for a in AO_SHARE)
if AO_GAP > 5:
    problems.append('AO mix %s is more than 5 points from the syllabus %s' % (AO_SHARE, AO_SYL))
for w, tar in (('Analyse', 25), ('Compare', 15)):
    if not CW[w] or max(CW[w], key=CW[w].get) != tar:
        problems.append('corpus does not show %s at %d marks: %s' % (w, tar, dict(CW[w])))
if problems:
    for p in problems:
        print('  PROBLEM', p)
    raise SystemExit('%d problems; nothing written.' % len(problems))


# ------------------------------------------------------------------------------------ WRITERS
def wj(rel, obj):
    p = os.path.join(WS, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as fh:
        json.dump(obj, fh, indent=1, ensure_ascii=False)
        fh.write('\n')


def wt(rel, text):
    p = os.path.join(WS, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as fh:
        fh.write(text)


PC = FACTS['ao_weights']['per_component_percent']
AS_AOS = ['AO1', 'AO2', 'AO3']
ao_pick = lambda d: {a: d[a] for a in AS_AOS}

# -- profiles
QP = {
 'profile_id': 'cambridge-9093-as-2024-2026', 'version': '0.1.0-draft', 'status': 'draft',
 'board': 'Cambridge International Education', 'qualification': 'Cambridge International AS Level',
 'subject': 'English Language', 'syllabus_code': CODE, 'syllabus_version': '2',
 'examination_years': [2024, 2025, 2026], 'route': 'AS Level only: components 12 (Paper 1 Reading) and 22 (Paper 2 Writing)',
 'source': FACTS['source_document'],
 'assessment_objectives': [
  {'code': a['code'], 'name': a['verbatim'], 'qualification_weight_percent': a['qualification_weight_percent']}
  for a in FACTS['assessment_objectives']],
 'papers': [
  {'paper_id': 'P%s' % p['paper'], 'name': p['name'], 'duration_minutes': p['duration_minutes'], 'marks': p['marks'],
   'qualification_weight_percent': 50, 'question_basis': p['description'],
   'assessment_objective_weights': ao_pick(PC['P%s' % p['paper']])}
  for p in FACTS['papers']],
 'grades': 'a-e (AS Level route; syllabus page 10)',
 'learner_context': {'region': 'Namibia', 'medium': 'English', 'currency': 'N$',
                     'note': 'AS Level English Language, first examination for this learner in the October/November 2026 series. '
                             'Papers 3 and 4 (A Level) are not in this route.'},
}
SP = {
 'profile_id': 'yyeni-subject-english-language-as-v0.1.0', 'version': '0.1.0-draft', 'status': 'draft',
 'subject_name': 'English Language (Cambridge International AS Level 9093)', 'language_variant': 'British English',
 'purpose': ('The teaching model for AS Level English Language. 9093 at AS is examined by task: six tasks on two papers, each on an '
             'unseen text or a brief and each marked against a level table. Forty of the hundred marks are for analysing how form, '
             'structure and language make meaning for an audience; forty-five are for writing to a brief; fifteen are for reading '
             'the unseen text accurately. The resource therefore teaches the analytical vocabulary and the moves each task rewards, '
             'practises them on short original extracts in flashcards, and rehearses every task on original practice texts and briefs.'),
 'depth_model': {'note_mode': 'full teaching depth',
                 'rationale': ('Notes teach each term and move a task rewards, demonstrate it on a short original extract, and name the '
                               'errors that cost marks as discriminations. They are the source for the flashcards and a standalone study text.'),
                 'words_per_objective': '300-450'},
 'terminology_rules': ['Use the syllabus wording for the tasks, the three categories of Section B and the linguistic elements listed on page 12.',
                       'Use the glossary senses exactly: curriculum/glossary.json.',
                       'British spelling throughout.'],
 'answer_structures': ANSWER_STRUCTURES,
 'variant_register': VARIANT_REGISTER,
 'conditioned_mechanisms': CONDITIONED,
 'prohibited_patterns': [
  'Do not reproduce any Cambridge text, question, task, title, mark-scheme or examiner-report wording.',
  'Do not claim what examiners reward, report or want; teach the technique and why it works.',
  'Do not use the command word Discuss in any prompt: the AS papers never use it.',
  'Do not teach Papers 3 and 4 or their content; this route sits Papers 1 and 2 only.',
  'Do not state a fixed deduction for word counts; the schemes judge length as part of the task.'],
 'glossary_homonyms': [
  {'term': 'voice', 'senses': ['grammatical voice: active or passive', 'a writer’s voice: the sense of a particular person speaking'],
   'rule': 'Say which sense the first time it appears in a block; the glossary files them as two entries.'},
  {'term': 'structure', 'senses': ['the organisation of a whole text', 'sentence structure, a feature of language'],
   'rule': '“Structure” alone means the whole text; say “sentence structure” for the other.'},
  {'term': 'form', 'senses': ['the kind of text (article, speech, review)', 'the grammatical shape of a word'],
   'rule': 'In this subject it means the kind of text unless a block says otherwise.'},
  {'term': 'context', 'senses': ['the situation a text is produced and read in', 'the words around a quotation'],
   'rule': 'Say which sense the first time it appears in a block.'}],
}
for fn, obj in (('qualification-profile.yaml', QP), ('subject-profile.yaml', SP)):
    with open(os.path.join(WS, fn), 'w', encoding='utf-8') as fh:
        yaml.safe_dump(obj, fh, sort_keys=False, allow_unicode=True, width=110)

# -- registry
reg = {'registry_id': 'REGISTRY-CIE-9093-AS-2026', 'qualification_profile_id': QP['profile_id'],
       'subject_profile_id': SP['profile_id'], 'generated_at': NOW, 'authority': FACTS['authority'],
       'granularity_note': ('9093 at AS assesses by task. Two foundation topics and one on evidence carry the knowledge every task '
                            'uses; the rest follow the paper sections. One objective per syllabus statement (pages 12-14 and 19-21), '
                            'transcribed with its page. Topic containers carry the syllabus heading they sit under.'),
       'objectives': []}
SRC = ('No third-party 9093 notes are approved for derivation. Content is authored from the syllabus wording and the '
       'assessment corpus (mined, not reproduced).')
for t in TOPICS:
    reg['objectives'].append({
     'objective_id': 'OBJ-%s-%s' % (CODE, t['id']), 'parent_id': None, 'topic_id': t['id'],
     'syllabus_text': t['container'][0], 'syllabus_page': t['container'][1], 'task': t['task'],
     'learner_objective': '%s (%s)' % (t['title'], t['task']), 'level': 'AS', 'route_status': 'core', 'mandatory': True,
     'objective_type': 'task', 'assessment_objectives': sorted({a for o in t['objectives'] for a in o[4]}),
     'papers': t['papers'], 'command_words': sorted({c for o in t['objectives'] for c in o[5]}),
     'prerequisite_ids': [], 'related_ids': [], 'depth_tier': 4,
     'source_coverage': {'rating': 0, 'action': 'generate_gap', 'rationale': SRC}, 'status': 'planned'})
    for (k, st, txt, pg, aos, cws, learner, tier) in t['objectives']:
        o = OBJ[(t['id'], k)]
        kind = ('analysis_skill' if aos == ['AO3'] else 'writing_skill' if aos == ['AO2'] else 'reading_skill' if aos == ['AO1']
                else 'reading_and_analysis' if set(aos) == {'AO1', 'AO3'} else 'reading_and_writing')
        reg['objectives'].append({
         'objective_id': o['id'], 'parent_id': 'OBJ-%s-%s' % (CODE, t['id']), 'topic_id': t['id'],
         'syllabus_text': txt, 'syllabus_page': pg, 'task': t['task'], 'learner_objective': learner,
         'sub_topic': st, 'sub_topic_heading': t['sub_topics'][st], 'level': 'AS', 'route_status': 'core',
         'mandatory': True, 'objective_type': kind, 'assessment_objectives': aos, 'papers': t['papers'], 'command_words': cws,
         'prerequisite_ids': [], 'related_ids': [], 'depth_tier': tier,
         'source_coverage': {'rating': 0, 'action': 'generate_gap', 'rationale': SRC}, 'status': 'planned'})
wj('curriculum/objective_registry.json', reg)
wj('curriculum/unit_titles.json', UNITS)

# -- framework
cw_rows = []
for c in FACTS['command_words']:
    w = c['word']
    tar = dict(sorted(CW[w].items()))
    used = bool(tar)
    cw_rows.append({'word': w, 'meaning': c['meaning'], 'meaning_provenance': 'syllabus, page %d' % c['source']['page'],
                    'in_syllabus_table': True, 'syllabus_page': c['source']['page'], 'syllabus_verbatim': c['verbatim'],
                    'used_at_level': used, 'use_in_prompts': used,
                    'observed': {'where': {'Analyse': 'Paper 1 Question 2', 'Compare': 'Paper 1 Question 1(b)'}.get(w, 'no AS paper'),
                                 'count': sum(tar.values()), 'of_papers': N_P1 + N_P2},
                    'observed_tariffs': {str(k): v for k, v in tar.items()}, 'observed_provenance': 'corpus',
                    'modal_tariff': max(tar, key=tar.get) if tar else None,
                    'verdict': 'primary' if used else 'listed_not_observed',
                    **({} if used else {'note': 'Listed for the qualification but never used in the %d AS papers, 2021-2025. '
                                                'Never used in a prompt (C-14).' % (N_P1 + N_P2)})})
IN_USE = [c['word'] for c in cw_rows if c['used_at_level']]
framework = {
 'framework_id': 'ASSESS-CIE-9093-AS-2026', 'generated_at': NOW, 'generated_by': 'build_9093.py, from curriculum/syllabus-facts.json',
 'authority': FACTS['authority'],
 'provenance_rule': ('Every value carries one of three provenances. "syllabus" is transcribed from the named page and is the '
                     'authority. "corpus" is counted from the published papers. "judgement" is our reading and is neither. '
                     'A value that cannot name where it came from is a value we do not have.'),
 'syllabus_facts_ref': 'curriculum/syllabus-facts.json',
 'route': 'AS Level: Papers 1 and 2 (syllabus page 10)',
 'assessment_objectives': [{'code': a['code'], 'definition': a['verbatim'], 'qualification_weight_percent': a['qualification_weight_percent'],
                            'provenance': 'syllabus, page 11', **({'note': '0% at AS Level; assessed only in Papers 3 and 4'}
                                                                  if a['qualification_weight_percent'] == 0 else {})}
                           for a in FACTS['assessment_objectives']],
 'per_component_ao_percent': {k: PC[k] for k in ('P1', 'P2')}, 'per_component_provenance': 'syllabus, page 11',
 'papers': [{'paper': p['paper'], 'name': p['name'], 'marks': p['marks'], 'duration_minutes': p['duration_minutes'],
             'weight_percent': 50, 'ao_split': PC['P%s' % p['paper']],
             'structure': p['description'], 'provenance': 'syllabus, pages 10, 19-21'} for p in FACTS['papers']],
 'task_ao_marks': {'note': 'Each question’s marks by AO, from its level table (corpus). They sum to the syllabus weights exactly.',
                   'P1-Q1a': {'AO1': 5, 'AO2': 5}, 'P1-Q1b': {'AO1': 5, 'AO3': 10}, 'P1-Q2': {'AO1': 5, 'AO3': 20},
                   'P2-Q1a': {'AO2': 15}, 'P2-Q1b': {'AO3': 10}, 'P2-B': {'AO2': 25}},
 'tasks': 'curriculum/answer-shapes.json',
 'command_word_table_source': 'syllabus, page %d, %d words' % (FACTS['command_word_table']['page'], FACTS['command_word_table']['count']),
 'command_word_reconciliation': ('9093 at AS is task-led. Two of the three listed words open the two analysis questions of Paper 1 '
                                 '(Compare for 1(b), Analyse for Question 2). Every other task is an instruction to write, with its form, '
                                 'audience, purpose and length stated. Discuss is never used at AS.'),
 'command_words': cw_rows,
 'command_words_in_use': IN_USE,
 'command_words_listed_but_never_used': [c['word'] for c in cw_rows if not c['used_at_level']],
 'command_words_used_but_not_listed': [
  {'word': 'Write', 'where': 'opens Paper 1 Question 1(a) and every Paper 2 task', 'provenance': 'corpus',
   'use_in_prompts': 'as a task instruction only'}],
 'flashcard_subtype_ao_map': [{'subtype': st, 'assessment_objectives': ['AO1', 'AO2', 'AO3'], 'tests': v[0], 'blooms_level': v[1]}
                              for st, v in SUBTYPE.items()],
 'subtype_ao_note': ('9093’s three AS objectives are domains (reading, writing, analysis), not cognitive levels, so any card subtype '
                     'can serve any of them. The slot decides: a card carries the AOs of the objective it is on.'),
 'blooms_taxonomy': {'scheme': 'Revised Bloom’s taxonomy (Anderson and Krathwohl).',
                     'why_both': ('The assessment objective says what the examination credits. The Bloom level says what the '
                                  'learner is being asked to do. They are different axes and every item carries both.'),
                     'levels': [{'level': a, 'means': b} for a, b in BLOOM_LEVELS],
                     'by_subtype': {st: v[1] for st, v in SUBTYPE.items()},
                     'by_performance_task': PERF_TYPES, 'required_on_every_item': True},
 'item_mix_target_note': ('No per-topic AO target is set, so C-18 reports not_run. Each 9093 topic is a task or the knowledge '
                          'behind tasks, so its AO mix is fixed by the task. The subject is balanced by marks: the practice tasks '
                          'reproduce the six tasks twelve times each, which is the AS weighting exactly (curriculum/ao_coverage.md).'),
 'ao_mark_budget': {'stated_qualification_weight_percent': ao_pick(AO_SYL), 'planned_percent': AO_SHARE,
                    'planned_marks': dict(AOM), 'largest_gap_points': AO_GAP},
}
M = THR['median']
framework['grade_thresholds'] = {
 'provenance': 'corpus: %d grade threshold tables, March 2021 to November 2025, components 12 and 22 and the AS option' % len(THR['rows']),
 'grades': 'a-e (AS Level)',
 'median_minimum_marks': {'P1_of_50': M['P1_of_50'], 'P2_of_50': M['P2_of_50'], 'AS_of_100': M['AS_of_100']},
 'november_series': THR['november'],
 'band_reading': 'judgement: a grade c is Level 3 on every table; a grade a is the bottom of Level 4 on every table'}
wj('curriculum/assessment-framework.json', framework)

# -- task specifications (answer shapes)
wj('curriculum/answer-shapes.json', {
 '_provenance': {'syllabus': 'marks, AOs, lengths, texts and the three categories: syllabus pages 19-21',
                 'corpus': ('the AO split inside each question and the level ladders: the %d published AS mark schemes, 2021-2025; '
                            'every ladder appears with the same bands in all %d schemes for its paper' % (N_P1 + N_P2, N_P1)),
                 'derivation_policy': ('The level descriptors are paraphrased in our words. No mark-scheme wording is to reach '
                                       'learner-facing output; paraphrase again when teaching them.'),
                 'generated': NOW},
 CODE: {'subject': 'Cambridge International AS Level English Language', 'tasks': TASKS}})

# -- misconceptions
wj('curriculum/misconceptions.json', {
 'register_id': 'MISCON-CIE-9093-AS-2026', 'generated_at': NOW,
 'authority': 'Cambridge Principal Examiner Reports for Teachers, 9093 Papers 1 and 2, %d series 2021-2025 (%d report variants per paper).'
              % (N_ER, N_ER_VAR['1']),
 'derivation_policy': 'Examiner-evidenced errors, restated in our words. No examiner-report wording appears in learner-facing output.',
 'how_to_use': ('Every entry earns one MISCON card on the objective it attaches to (the work order names the slot). A MISCON '
                'card is a DISCRIMINATION: it states the error, the correct move, and the test that tells them apart. It does '
                'not simply restate the correct technique.'),
 'evidence_method': ('Counted over report sentences that record a weakness, filed by task (gen/er9093.py), matched by the pattern '
                     'shown. report_variants is the spread; it does not measure prominence.'),
 'entries': [{'misconception_id': m[0], 'topic_id': m[1], 'objective_id': OBJ[(m[1], m[2])]['id'], 'report_tasks': m[3],
              'report_theme': m[4], 'evidence': EVID[m[0]], 'evidence_pattern': m[7],
              'learners': m[5], 'test': m[6]} for m in MISCONCEPTIONS]})

# -- glossary
wj('curriculum/glossary.json', {'glossary_id': 'GLOSSARY-CIE-9093-AS-2026', 'status': 'settled',
                                'note': 'Use these senses exactly. Do not invent alternatives.',
                                'terms': [dict({'term': a, 'sense': b}, **({'boundary': c} if c else {})) for a, b, c in GLOSSARY]})

# -- exposure
exp = {'exposure_id': 'EXPOSURE-CIE-9093-AS-2026', 'generated_at': NOW,
       'authority': 'Cambridge International AS Level English Language 9093, %d published AS question papers and mark schemes, 2021-2025.' % (N_P1 + N_P2),
       'evidence_window': '%d Paper 1 and %d Paper 2 question papers, %d series.' % (N_P1, N_P2, N_SERIES),
       'method': ('9093 at AS has no optional content: every Paper 1 task and Paper 2 Section A are compulsory on every paper, '
                  'and Section B offers one question in each category on every paper. So every objective is tested, or '
                  'available to be answered, on every paper of its component. The class is structural, not a frequency.'),
       'principle': 'RS-05: exposure calibrates emphasis. Every objective in scope is taught and practised.',
       'status': 'structural', 'classes': {'every_paper': 'tested by a task on every paper of its component'},
       'objectives': []}
for t in TOPICS:
    for (k, *_r) in t['objectives']:
        o = OBJ[(t['id'], k)]
        req = sorted({'MISCON'} if any(m[1] == t['id'] and m[2] == k for m in MISCONCEPTIONS) else set())
        exp['objectives'].append({'objective_id': o['id'], 'topic_id': t['id'], 'syllabus_text': o['syllabus_text'],
                                  'task': t['task'], 'papers': t['papers'],
                                  'papers_in_corpus': (N_P1 if '1' in t['papers'] else 0) + (N_P2 if '2' in t['papers'] else 0),
                                  'exam_exposure': 'every_paper', 'required_subtypes': req})
wj('curriculum/exam-exposure.json', exp)

# -- exclusions
wj('curriculum/syllabus-exclusions.json', {
 'stated_in_the_syllabus': [
  {'fact': 'Dictionaries may not be used in Paper 1 or Paper 2.', 'pages': [19, 20]},
  {'fact': 'The examples in the subject content are suggested, not prescribed, and not exhaustive.', 'page': 12},
  {'fact': 'Candidates on an AS Level route are graded a-e.', 'page': 10},
  {'fact': 'AO4 and AO5 carry 0% at AS Level.', 'page': 11}],
 'not_in_this_route': {'terms': NOT_IN_ROUTE, 'why': 'This learner sits components 12 and 22 (syllabus-facts.json papers_sat); '
                                                     'Papers 3 and 4 are A Level only.'}})

# ----------------------------------------------------------------------------------- CONTRACTS
DIFF_PERF = lambda m: 2 if not m else 3 if m <= 10 else 4 if m <= 15 else 5
TOPICS_BY = {t['id']: t for t in TOPICS}


def slots_for(tid):
    out, n = [], 0
    for (k, st, teaches, cw, tar, mc) in F[tid]:
        n += 1
        o = OBJ[(tid, k)]
        s = {'slot': 'ITEM-%s-%s-%03d-%s' % (CODE, tid, n, st), 'objective_id': o['id'], 'objective_title': o['learner'],
             'syllabus_text': o['syllabus_text'], 'subtype': st, 'assessment_objectives': o['aos'],
             'command_word': cw, 'mark_tariff': tar, 'difficulty': SUBTYPE[st][2],
             'blooms_level': SUBTYPE[st][1], 'teaches': teaches,
             'marking_guidance_must_name': ANSWER_STRUCTURES[st]}
        if mc:
            s['misconception_id'] = mc
        s['reason'] = 'the misconception register records this error' if mc else 'a term or move the tasks depend on'
        out.append(s)
    return out


def perf_for(tid):
    out = []
    for n, p in enumerate(P[tid], 1):
        s = {'slot': 'ITEM-%s-%s-P%02d' % (CODE, tid, n), 'item_type': p['item_type'],
             'objective_ids': [OBJ[(tid, k)]['id'] for k in p['keys']],
             'assessment_objectives': p['aos'], 'command_word': p['command_word'], 'mark_tariff': p['mark_tariff'],
             'ao_marks': p['ao_marks'], 'difficulty': DIFF_PERF(p['mark_tariff']), 'blooms_level': p['blooms_level'],
             'brief': p['brief'], 'models': TOPIC_TASKS[tid], 'marking_guidance_must_name': ANSWER_STRUCTURES[p['item_type']]}
        if p['text'] is not None:
            s['text_id'] = TEXTS[tid][p['text']][0]
        if p['pair'] is not None:
            s['written_about'] = 'ITEM-%s-%s-P%02d' % (CODE, tid, p['pair'] + 1)
            s['pair_note'] = ('This task is written about the model answer of %s: author that first, and quote it here.'
                              % s['written_about'])
        out.append(s)
    return out


def units_for(t):
    out = []
    for st, head in t['sub_topics'].items():
        objs = [OBJ[(t['id'], k)] for (k, s_, *_r) in t['objectives'] if s_ == st]
        n = len(objs)
        out.append({'unit_id': 'CU-%s-%s' % (CODE, st), 'file': 'content-units/CU-%s-%s.json' % (CODE, st), 'sub_topic': st,
                    'heading': head, 'objective_ids': [o['id'] for o in objs],
                    'objectives': [{'objective_id': o['id'], 'title': o['learner'], 'syllabus_text': o['syllabus_text'],
                                    'syllabus_page': o['page'], 'assessment_objectives': o['aos']} for o in objs],
                    'word_budget': [max(500, 300 * n), max(800, 450 * n)],
                    'blocks_required': [
                     'a plain explanation block for every objective above, in the glossary’s senses',
                     'at least one worked demonstration: a short original extract (no more than 120 words) and the move carried out on it step by step',
                     'a block that restates each misconception attached to these objectives as a discrimination: the error, the correct move, the test',
                     'where this unit introduces its task, what the syllabus states about it (marks, length, texts) and nothing the syllabus does not state']})
    return out


ADJ = {'1.1': [('the linguistic toolkit', '1.2'), ('the paper tasks', '1.4, 1.5, 2.1 to 2.5')],
       '1.2': [('writing evidence into an analysis', '1.3'), ('rhetorical devices in your own arguments', '2.4')],
       '1.3': [('the vocabulary of analysis', '1.2')], '1.4': [('text analysis', '1.5'), ('accuracy', '2.6')],
       '1.5': [('comparison', '1.4')], '2.1': [('the analytical vocabulary', '1.2'), ('accuracy', '2.6')],
       '2.2': [('the three categories', '2.3, 2.4 and 2.5')], '2.3': [('structure', '2.2'), ('accuracy', '2.6')],
       '2.4': [('structure', '2.2'), ('rhetorical devices as analysed', '1.2')], '2.5': [('structure', '2.2')],
       '2.6': [('the writing tasks', '1.4, 2.1 and 2.3 to 2.5')]}


def ao_targets(t):
    if len(t['papers']) == 1:
        return ao_pick(PC['P' + t['papers'][0]])
    return ao_pick(AO_SYL)


WORK = {}
for t in TOPICS:
    tid, title = t['id'], t['title']
    fl, pf, cu = slots_for(tid), perf_for(tid), units_for(t)
    texts = [{'text_id': x[0], 'file': 'texts/%s.md' % x[0], 'words_min': x[1], 'words_max': x[2], 'genre': x[3],
              'used_by': [p['slot'] for p in pf if p.get('text_id') == x[0]]} for x in TEXTS.get(tid, [])]
    items = fl + pf
    bl = collections.Counter(s['blooms_level'] for s in items)
    wb = [sum(u['word_budget'][0] for u in cu), sum(u['word_budget'][1] for u in cu)]
    am = collections.Counter()
    for p in pf:
        for a, v in p['ao_marks'].items():
            am[a] += v
    am_tot = sum(am.values())
    contract = {
     'contract_id': 'CONTRACT-%s-%s' % (CODE, tid), 'topic_id': tid, 'topic_title': title,
     'unit': 'Unit %s — %s' % (tid[0], UNITS[tid[0]]), 'qualification': WS_NAME, 'standard_version': '0.2.0-draft',
     'generated_at': NOW, 'generated_by': 'build_9093.py', 'status': 'active',
     'scope': {'task': t['task'], 'included_objective_ids': [OBJ[(tid, o[0])]['id'] for o in t['objectives']],
               'included_count': len(t['objectives']),
               'depth_tiers': dict(collections.Counter(str(o[7]) for o in t['objectives']))},
     'target_learner_profile': {'prior_teaching': 'Learners who completed a first-language English course at IGCSE or equivalent; no prior knowledge of the AS papers assumed.',
                                'context': 'Namibian secondary learners, Cambridge International AS Level, English medium, sitting the October/November 2026 series.',
                                'note_purpose': ['source of record for flashcard generation', 'offline reading', 'standalone study text']},
     'assessment_expectations': {
      'papers': ['P%s' % p for p in t['papers']], 'task_specifications': ['curriculum/answer-shapes.json -> %s' % x for x in TOPIC_TASKS[tid]],
      'command_words_in_scope': sorted({c for o in t['objectives'] for c in o[5]}),
      'command_words_note': ('Only Compare and Analyse are used at AS (syllabus page 23; corpus). Use one only where a slot names it; '
                             'otherwise use the task form of the paper item the slot models. Never use Discuss.'),
      'ao_targets': ao_targets(t),
      'ao_note': ('The syllabus’s split for this paper by marks (page 11)' if len(t['papers']) == 1 else
                  'The AS weights (page 11): this topic serves both papers') + '. Not a per-topic item-count target.'},
     'exposure': {'class': 'every_paper', 'principle': exp['principle']},
     'depth_constraints': {
      'note_mode': 'full teaching depth', 'word_budget': {'min': wb[0], 'max': wb[1]}, 'item_budget': len(items),
      'excluded_constructs': list(NOT_IN_ROUTE),
      'excluded_constructs_source': ('Components this learner does not sit (route 12 and 22). C-11 scans learner-facing text for '
                                     'these exact terms, so they are short terms, not sentences.'),
      'stated_in_the_syllabus': ['Dictionaries may not be used (pages 19-20).',
                                 'The content examples are suggested, not prescribed (page 12): teach the listed features, and never '
                                 'present them as a closed list.'],
      'adjacent_topics': ['%s — taught in topic %s; name it in passing if you must, teach it there' % a for a in ADJ.get(tid, [])]},
     'required_outputs': {'claim_ledger': True, 'content_units': len(cu), 'learning_items': len(items), 'notes': True,
                          'practice_texts': len(texts)},
     'misconceptions': 'curriculum/misconceptions.json (filter on topic_id "%s")' % tid,
     'subtype_waivers': [],
     'item_budget_note': 'Set from the work order, which is the operative plan.'}
    wo = {
     'work_order_id': 'WO-%s-%s' % (CODE, tid), 'topic_id': tid, 'topic_title': title, 'topic': topic_label(tid, title),
     'task': t['task'], 'generated_by': 'build_9093.py — regenerate, never edit', 'standard': 'v0.2.0-draft',
     'authoring_note': ('Every slot is decided. Write the prose, the texts and the items; do not redesign the plan. If a slot '
                        'is wrong for its objective, change it and record {from, to, why} in authoring_notes.json.'),
     'output_files': {'claims': 'claims/canonical_claim_ledger.json', 'content_units': [u['file'] for u in cu],
                      'learning_items': 'learning-items/topic_%s_items.json' % tid, 'texts': [x['file'] for x in texts],
                      'notes': notes_filename(tid, title), 'flashcards_when_published': flashcards_filename(tid, title)},
     'assessable_objective_count': len(t['objectives']),
     'claims_plan': {'per_objective': '3 to 6', 'approximate_total': [3 * len(t['objectives']), 6 * len(t['objectives'])],
                     'what_a_claim_is': ('one statement the notes teach and a card rests on: a definition, a convention of a '
                                         'form, a step of a technique, or why a choice has its effect. Technique claims are claims.')},
     'content_units': cu, 'practice_texts': texts, 'item_slots': fl, 'performance_tasks': pf,
     'planned_item_count': len(items), 'planned_flashcards': len(fl), 'planned_performance_tasks': len(pf),
     'planned_blooms_mix': {b: {'items': bl[b], 'share_percent': round(100 * bl[b] / len(items))} for b, _ in BLOOM_LEVELS},
     'planned_ao_mix_by_marks': {a: {'planned_share_percent': round(100 * am[a] / am_tot) if am_tot else 0,
                                     'syllabus_weight_percent': AO_SYL[a]} for a in AS_AOS},
     'marks_equivalent_total': am_tot,
     'ao_mix_note': ('Marks-equivalent counts the performance tasks at the AO split of the level table each models. Flashcards '
                     'model no paper item and carry no tariff, so they count nothing here; they carry their objective’s AOs.'),
     'excluded_constructs': list(NOT_IN_ROUTE), 'subtype_waivers': []}
    WORK[tid] = wo
    wj('topics/%s/contract.json' % tid, contract)
    wj('topics/%s/work_order.json' % tid, wo)
    md = ['# Work order — %s' % topic_label(tid, title), '', '**Task:** %s  ' % t['task'],
          '**Items:** %d (%d flashcards, %d performance tasks) · **practice texts:** %d · **notes:** %d–%d words'
          % (len(items), len(fl), len(pf), len(texts), wb[0], wb[1]), '', '## Objectives', '',
          '| id | syllabus text (page) | AOs | command words |', '|---|---|---|---|']
    for o in t['objectives']:
        r = OBJ[(tid, o[0])]
        md.append('| %s | %s (p%d) | %s | %s |' % (r['id'], r['syllabus_text'], r['page'], ', '.join(r['aos']), ', '.join(r['cws']) or '—'))
    md += ['', '## Flashcard slots', '', '| slot | subtype | Bloom | AOs | teaches |', '|---|---|---|---|---|']
    for s in fl:
        md.append('| %s | %s | %s | %s | %s%s |' % (s['slot'], s['subtype'], s['blooms_level'], ', '.join(s['assessment_objectives']),
                  s['teaches'], ' (%s)' % s['misconception_id'] if s.get('misconception_id') else ''))
    md += ['', '## Performance tasks', '', '| slot | type | text | Bloom | AO marks | command word · tariff | brief |',
           '|---|---|---|---|---|---|---|']
    for s in pf:
        md.append('| %s | %s | %s | %s | %s | %s | %s%s |' % (
            s['slot'], s['item_type'], s.get('text_id', '—'), s['blooms_level'],
            ', '.join('%s %d' % kv for kv in s['ao_marks'].items()) or '—',
            ('%s · %d' % (s['command_word'], s['mark_tariff'])) if s['command_word'] else (str(s['mark_tariff']) if s['mark_tariff'] else '—'),
            s['brief'], (' — written about %s' % s['written_about']) if s.get('written_about') else ''))
    if texts:
        md += ['', '## Practice texts', '', '| text | words | genre | used by |', '|---|---|---|---|']
        for x in texts:
            md.append('| %s | %d–%d | %s | %d tasks |' % (x['text_id'], x['words_min'], x['words_max'], x['genre'], len(x['used_by'])))
    md += ['', '## Out of scope', '', ', '.join('`%s`' % c for c in NOT_IN_ROUTE)] + \
          ['- %s' % a for a in contract['depth_constraints']['adjacent_topics']] + ['']
    wt('topics/%s/work_order.md' % tid, '\n'.join(md))

# -- AO coverage, in marks-equivalent, the measure the syllabus uses
L_ = ['# AO coverage — whole subject', '', '*Generated by standard/v0.2.0-draft/mine/build_9093.py. Regenerate, never edit.*', '',
      'The syllabus states its assessment-objective weights as a share of marks (page 11). The practice tasks model the six AS '
      'tasks, twelve of each, and each is valued at the AO split of the level table it models. Flashcards model no paper item '
      'and carry no tariff.', '', '## Subject total', '', '| AO | planned | syllabus weight | gap |', '|---|---:|---:|---:|']
for a in AS_AOS:
    L_.append('| %s | %d%% | %d%% | %+d |' % (a, AO_SHARE[a], AO_SYL[a], AO_SHARE[a] - AO_SYL[a]))
L_ += ['', '%s **largest gap %d points** across %s marks-equivalent of practice.' % ('✅' if AO_GAP <= 5 else '⚠️', AO_GAP, format(AO_TOT, ',')),
       '', '## By topic', '', '| Topic | Objectives | Items | Marks-eq | AO1 | AO2 | AO3 |', '|---|---:|---:|---:|---:|---:|---:|']
for t in TOPICS:
    w = WORK[t['id']]
    m = w['planned_ao_mix_by_marks']
    L_.append('| **%s** %s | %d | %d | %d | %s |' % (t['id'], t['title'], w['assessable_objective_count'], w['planned_item_count'],
              w['marks_equivalent_total'], ' | '.join('%d%%' % m[a]['planned_share_percent'] for a in AS_AOS)))
wt('curriculum/ao_coverage.md', '\n'.join(L_) + '\n')

# summary numbers for the documents
TOT = {'topics': len(TOPICS), 'objectives': sum(len(t['objectives']) for t in TOPICS),
       'flash': sum(w['planned_flashcards'] for w in WORK.values()), 'perf': sum(w['planned_performance_tasks'] for w in WORK.values()),
       'texts': sum(len(w['practice_texts']) for w in WORK.values()),
       'text_words': (sum(x['words_min'] for w in WORK.values() for x in w['practice_texts']),
                      sum(x['words_max'] for w in WORK.values() for x in w['practice_texts'])),
       'notes_words': (sum(u['word_budget'][0] for w in WORK.values() for u in w['content_units']),
                       sum(u['word_budget'][1] for w in WORK.values() for u in w['content_units']))}
TOT['items'] = TOT['flash'] + TOT['perf']
BLOOM_ALL = collections.Counter(s['blooms_level'] for w in WORK.values() for s in w['item_slots'] + w['performance_tasks'])
json.dump({'TOT': TOT, 'BLOOM': BLOOM_ALL, 'AO': AO_SHARE, 'AO_GAP': AO_GAP, 'AO_MARKS': dict(AOM)},
          open(os.path.join(WS, 'curriculum', '.build_totals.json'), 'w'))
print('9093 plan data written: %(topics)d topics, %(objectives)d objectives, %(flash)d flashcards + %(perf)d performance '
      'tasks = %(items)d items, %(texts)d practice texts' % TOT)
print('AO by marks %s (syllabus %s), largest gap %d; misconceptions %d, all evidenced' % (AO_SHARE, ao_pick(AO_SYL), AO_GAP, len(MISCONCEPTIONS)))
