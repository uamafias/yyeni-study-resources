# -*- coding: utf-8 -*-
"""Build the complete 0500 plan: curriculum files, contracts, work orders, PLAN and HANDOVER.

    python3 build_0500.py

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
from design_0500 import (CODE, SLUG, WS_NAME, UNITS, TOPICS, F, P, TEXTS, MISCONCEPTIONS, GLOSSARY,  # noqa: E402
                         VARIANT_REGISTER, CONDITIONED, NOT_IN_ROUTE)
from gates import require_prerequisites  # noqa: E402
from naming import notes_filename, flashcards_filename, topic_label  # noqa: E402

WS = os.path.join(REPO, 'work', WS_NAME)
CUR = os.path.join(WS, 'curriculum')
REL = 'work/' + WS_NAME
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
TODAY = datetime.date.today().strftime('%-d %B %Y')
ANALYSIS = 'operations/analysis/%s-%s-corpus-analysis.md' % (CODE, SLUG)
PLAN_NAME = 'PLAN-%s-%s.md' % (CODE, SLUG)
HANDOVER_NAME = 'HANDOVER-%s-%s.md' % (CODE, SLUG)

require_prerequisites(WS)
FACTS = json.load(open(os.path.join(CUR, 'syllabus-facts.json')))
PDF = os.path.join(REPO, FACTS['source_document'])
PAGES = subprocess.run(['pdftotext', '-layout', PDF, '-'], capture_output=True, text=True, check=True).stdout.split('\f')


def norm(s):
    for a, b in (('–', '-'), ('—', '-'), ('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"')):
        s = s.replace(a, b)
    s = re.sub(r'\s*/\s*', '/', s)
    return re.sub(r'\s+', ' ', s).strip().lower().rstrip('.')


def on_page(text, page):
    return norm(text) in norm(PAGES[page - 1])


# ------------------------------------------------------------------------------------------ BLOOM
SUBTYPE = collections.OrderedDict([
 ('DEF', ('Precise meaning of one term', 'Remember', 1)),
 ('FEATURE', ('The features or conventions of a form or a kind of writing', 'Remember', 2)),
 ('PROC', ('The ordered steps of a technique', 'Remember', 2)),
 ('WHY', ('The reason a technique works', 'Understand', 2)),
 ('DIST', ('The boundary between two confusable ideas, and the test that separates them', 'Understand', 2)),
 ('MISCON', ('Discriminating a recorded confusion from the idea it is confused with', 'Understand', 3)),
 ('MECH', ('How a language choice produces its effect', 'Understand', 3)),
 ('APP', ('A technique carried out on a supplied original sentence or extract', 'Apply', 3)),
 ('INTERP', ('Reading an implied meaning out of a supplied detail', 'Analyse', 3)),
 ('EVAL', ('A judgement on how convincing a supplied view is, with the case against', 'Evaluate', 4)),
])
BLOOM_LEVELS = [
 ('Remember', 'Recall a term, a convention or the steps of a technique, as stated.'),
 ('Understand', 'Explain an idea in the learner’s own words, or tell it apart from a neighbouring one.'),
 ('Apply', 'Carry out a technique on a sentence, an extract or a text the learner has not seen answered.'),
 ('Analyse', 'Break a text into its parts: what it states, what it implies, how its language works.'),
 ('Evaluate', 'Judge how convincing an idea or a view is, against a reason, and reach a position that could have gone the other way.'),
 ('Create', 'Compose something new: a summary, a response in role, an argument, a description, a story. In 0500 this is '
            'most of Paper 2 and all of Paper 1 Question 3, so it carries far more of the practice than in a content subject.'),
]
PERF_TYPES = {'short_answer': 'Understand (comprehension) or Apply (editing and rewriting), as the slot says',
              'writing_task': 'Create, except the summary, which is Analyse (the marks are for selecting)',
              'source_analysis': 'Analyse', 'essay_plan': 'Evaluate'}

ANSWER_STRUCTURES = {
 'DEF': ['meaning|means|definition|defined'],
 'FEATURE': ['feature|features|convention|conventions|includes|expected'],
 'PROC': ['step|steps|first|then|order|sequence'],
 'WHY': ['reason|because|why|purpose'],
 'DIST': ['difference|distinguish|whereas|contrast|boundary|test'],
 'MISCON': ['error|mistake|confuse|confused|confusion|wrongly|instead'],
 'MECH': ['effect|creates|suggests|reader'],
 'APP': ['text|sentence|extract|passage|words', 'because|suggests|shows|so'],
 'INTERP': ['detail|word|phrase|evidence', 'suggests|implies|shows'],
 'EVAL': ['judgement|judge|convincing|persuasive', 'evidence|reason|support', 'however|but|counter|other view|weakness'],
 'short_answer': ['mark|marks', 'text|paragraph|line|lines|passage|sentence'],
 'source_analysis': ['meaning', 'effect', 'level|mark|marks'],
 'essay_plan': ['evaluate|evaluation|judgement|judge', 'both texts|each text|text a|text b', 'own words'],
 'writing_task': ['level|levels|band', 'organised|organisation|organise|structure|structured|sequence|sequenced',
                  'vocabulary|language|style|register'],
}


def ao_of(subs):
    out = []
    if any(s.startswith('R') for s in subs):
        out.append('AO1')
    if any(s.startswith('W') for s in subs):
        out.append('AO2')
    return out


# --------------------------------------------------------------------------------- CORPUS COUNTS
def corpus_command_words():
    ms = json.load(open(os.path.join(MINE, '0500_markscheme.json')))
    seen, cw = set(), collections.defaultdict(collections.Counter)
    for m in ms:
        if m['paper'] != '1':
            continue
        for s in m['stems']:
            k = (m['file'], s['item'])
            if k in seen:
                continue
            seen.add(k)
            mm = re.search(r'\b(identify|give|explain|describe)\b', s['stem'], re.I)
            if mm:
                cw[mm.group(1).capitalize()][s['marks']] += 1
    titles = collections.Counter()
    import glob
    qps = sorted(glob.glob(os.path.join(MINE, '0500', '0500_*_qp_2*.txt')))
    for f in qps:
        for mm in re.finditer(r'(?m)^\s*[2-5]\s+(.{0,160})$', open(f).read()):
            w = re.match(r'(Describe|Write)', mm.group(1).strip())
            if w:
                titles[w.group(1)] += 1
    return cw, titles, len(qps), len({k[0] for k in seen})


CW, TITLES, N_P2, N_P1 = corpus_command_words()
THEMES = json.load(open(os.path.join(MINE, 'out', '0500_themes.json')))
THR = json.load(open(os.path.join(MINE, 'out', '0500_thresholds.json')))


def theme_series(task, theme):
    for t in THEMES.get(task) or THEMES.get('P2 Section B composition' if task.startswith('P2 Section B') else task, []):
        if t['theme'] == theme:
            return t['series'], t['of']
    raise SystemExit('theme not found: %s / %s' % (task, theme))


# ------------------------------------------------------------------------------- TASK SPECS (shapes)
def L(level, marks, text):
    return {'level': level, 'marks': marks, 'requires': text}


TASKS = collections.OrderedDict()
TASKS['P1-Q1-comprehension'] = {
 'paper': 'P1', 'name': 'Question 1, comprehension', 'text': 'A, 700–750 words', 'marks': 15,
 'sub_objectives': ['R1', 'R2', 'R5'], 'provenance': 'syllabus, page 13',
 'how_marked': 'point-marked items', 'layout': [1, 2, 2, 2, 2, 3, 3],
 'layout_provenance': 'corpus: the same seven-item layout in 22 of the 31 mark schemes whose item table could be read; the rest were partial reads',
 'set_as': 'short questions, each naming the paragraph to use; two-mark items ask the candidate to explain in their own words (corpus)'}
TASKS['P1-Q1-summary'] = {
 'paper': 'P1', 'name': 'Question 1, summary', 'text': 'B, 700–750 words', 'marks': 15,
 'split': {'reading': {'marks': 10, 'sub_objectives': ['R1', 'R2', 'R5']}, 'writing': {'marks': 5, 'sub_objectives': ['W2', 'W3']}},
 'length': 'no more than 120 words, continuous writing, own words', 'provenance': 'syllabus, page 13',
 'set_as': 'a selective summary on a stated focus (corpus)',
 'tables': [
  {'table': 'reading', 'out_of': 10, 'levels': [
   L(5, '9-10', 'understands the task thoroughly; covers a wide range of relevant ideas with consistent focus; points selected skilfully enough to give an overview'),
   L(4, '7-8', 'understands the task competently; a good range of relevant ideas, mostly focused; careful selection with some sense of overview'),
   L(3, '5-6', 'reasonable understanding; focus slips at times; some selection, but excess material may be included'),
   L(2, '3-4', 'some understanding; some relevant ideas, focused only at times; selection partly indiscriminate'),
   L(1, '1-2', 'limited understanding of the task; may read as a bare list of disconnected ideas; little selection')]},
  {'table': 'writing', 'out_of': 5, 'levels': [
   L(3, '4-5', 'clear, fluent and mostly concise; well organised; in the candidate’s own words, with well-chosen vocabulary'),
   L(2, '2-3', 'generally clear with some concision; some lapses in organisation; mainly own words but leaning on the text’s wording'),
   L(1, '1', 'unclear or not concise: overlong explanations or very brief; may include lifted sections')]}]}
TASKS['P1-Q2-short-answers'] = {
 'paper': 'P1', 'name': 'Question 2, short-answer questions', 'text': 'C, 500–650 words', 'marks': 10,
 'sub_objectives': ['R1', 'R2', 'R4'], 'provenance': 'syllabus, page 14', 'how_marked': 'point-marked items',
 'layout': {'2(a)': '4 x 1 mark: the text’s word or phrase for a given idea',
            '2(b)': '3 x 1 mark: the meaning of a single word as used, in the candidate’s own words',
            '2(c)': '1 x 3 marks: one example from a short extract, and how it suggests something'},
 'layout_provenance': 'corpus: stable across the 42 Paper 1 mark schemes'}
TASKS['P1-Q2-language-task'] = {
 'paper': 'P1', 'name': 'Question 2, language task', 'text': 'C, two named paragraphs', 'marks': 15,
 'sub_objectives': ['R1', 'R2', 'R4'], 'length': 'about 200–300 words', 'provenance': 'syllabus, page 14',
 'tables': [{'table': 'reading', 'out_of': 15, 'levels': [
   L(5, '13-15', 'wide-ranging discussion of well-chosen language across both paragraphs; comments that add meaning and associations and show why the writer chose the words; imagery handled with precision and imagination; a clear grasp of how language works'),
   L(4, '10-12', 'carefully chosen words and phrases explained; secure meanings in context and effects identified in both paragraphs; images recognised and partly explained'),
   L(3, '7-9', 'satisfactory choices; mostly meanings, with basic or general comment on effect; one paragraph may be handled better than the other'),
   L(2, '4-6', 'a mix of apt and weaker choices; devices may be named without the reason for using them; few, general or partial explanations; may repeat the text’s own words'),
   L(1, '1-3', 'sparse or rarely relevant choices; very thin comment')]}]}
TASKS['P1-Q3'] = {
 'paper': 'P1', 'name': 'Question 3, extended response to reading', 'text': 'C', 'marks': 25,
 'split': {'reading': {'marks': 15, 'sub_objectives': ['R1', 'R2', 'R3']}, 'writing': {'marks': 10, 'sub_objectives': ['W1', 'W2', 'W3', 'W4']}},
 'length': 'about 250–350 words', 'text_types': ['letter', 'report', 'journal', 'speech', 'interview', 'article'],
 'provenance': 'syllabus, page 14',
 'set_as': 'written in role, in a given form, with exactly three bullets to address in every one of the 42 tasks (corpus); forms where readable (33 of 42): letter 9, speech 7, interview 7, journal or diary 5, article 3, report 2',
 'tables': [
  {'table': 'reading', 'out_of': 15, 'levels': [
   L(5, '13-15', 'the text analysed and judged in depth; ideas developed, sustained and anchored in it; a wide range of ideas; supporting detail woven in throughout; all three bullets fully covered; a voice that stays consistent and convincing'),
   L(4, '10-12', 'a competent reading that analyses or judges at times; plenty of ideas, some developed though not always sustained; frequent, useful detail; all three bullets covered; a suitable voice'),
   L(3, '7-9', 'a reasonable reading; straightforward ideas, rarely developed; detail present but sometimes used mechanically; uneven focus on the bullets; a plain voice'),
   L(2, '4-6', 'general understanding of the main ideas but thin or unfocused in places; brief reference to the text; some lifting; a bullet may be missing; the voice may not fit'),
   L(1, '1-3', 'very general, or largely reproduced from the text; insubstantial or unselective; little sign of reworking the text’s material')]},
  {'table': 'writing', 'out_of': 10, 'levels': [
   L(5, '9-10', 'a register that suits audience and purpose; language that convinces and stays apt; ideas put with force in varied, well-chosen language; structure and sequence sound throughout'),
   L(4, '7-8', 'some awareness of an apt register; mostly fluent and clear; enough vocabulary for some subtlety and precision; mainly well structured and sequenced'),
   L(3, '5-6', 'clear but plain or factual, with little opinion; ideas rarely extended though explanations are adequate; some sections well sequenced, with flaws in structure'),
   L(2, '3-4', 'some awkward expression and inconsistent style; language too limited for shades of meaning; structural weakness; some copying'),
   L(1, '1-2', 'unclear expression and structure; weak, undeveloped language; little attempt to explain; frequent copying')]}]}
TASKS['P2-A'] = {
 'paper': 'P2', 'name': 'Section A, directed writing', 'text': 'one or two texts totalling 650–750 words', 'marks': 40,
 'split': {'writing': {'marks': 25, 'sub_objectives': ['W1', 'W2', 'W3', 'W4', 'W5']}, 'reading': {'marks': 15, 'sub_objectives': ['R1', 'R2', 'R3', 'R5']}},
 'length': 'about 250–350 words', 'forms': 'a discursive, argumentative or persuasive speech, letter or article',
 'provenance': 'syllabus, page 15',
 'set_as': 'two bullets; the first opens with "evaluate" in all 32 readable tasks, and all 32 ask for both texts and the candidate’s own words (corpus); forms where readable (24 of 42): letter 13, speech 6, article 5',
 'tables': [
  {'table': 'writing', 'out_of': 25, 'levels': [
   L(6, '22-25', 'a highly effective style conveying subtle meaning (W1); structured carefully for the reader (W2); a wide, sophisticated vocabulary used precisely (W3); a highly effective register (W4); accuracy almost always secure (W5)'),
   L(5, '18-21', 'an effective style; a secure structure that helps the reader; a wide vocabulary used with some precision; an effective register; mostly accurate, with occasional minor errors'),
   L(4, '14-17', 'a sometimes effective style; ideas generally well sequenced; adequate, sometimes effective vocabulary; a sometimes effective register; generally accurate, with some errors'),
   L(3, '10-13', 'an inconsistent style, sometimes awkward but clear; follows the sequence of the source texts; simple or limited vocabulary, or leaning on the texts; some awareness of register; frequent, sometimes serious errors'),
   L(2, '6-9', 'a limited style; not well sequenced; limited vocabulary, or phrases copied from the texts; limited sense of register; persistent errors'),
   L(1, '1-5', 'unclear expression; poor sequencing; very limited vocabulary or copying; very limited sense of register; errors that get in the way of meaning')]},
  {'table': 'reading', 'out_of': 15, 'levels': [
   L(6, '13-15', 'successfully evaluates explicit and implicit ideas and opinions; absorbs ideas from the texts into a developed, sophisticated response'),
   L(5, '10-12', 'some successful evaluation of explicit and implicit ideas; a thorough response built on a detailed selection of relevant ideas'),
   L(4, '7-9', 'begins to evaluate, mainly explicit ideas; an appropriate response with relevant ideas from the texts'),
   L(3, '5-6', 'selects and comments on explicit ideas; a general response with a few relevant ideas'),
   L(2, '3-4', 'identifies explicit ideas; a limited response with little evidence from the texts'),
   L(1, '1-2', 'very limited, with little connection to the texts')]}]}
TASKS['P2-B'] = {
 'paper': 'P2', 'name': 'Section B, composition', 'marks': 40,
 'split': {'content and structure': {'marks': 16, 'sub_objectives': ['W1', 'W2']}, 'style and accuracy': {'marks': 24, 'sub_objectives': ['W3', 'W4', 'W5']}},
 'split_provenance': 'the 40 marks and W1-W5 are syllabus, page 15; the 16/24 division and the objectives tagged to each table are corpus, from the mark schemes',
 'length': 'about 350–450 words', 'choice': 'one of four titles: two descriptive and two narrative', 'provenance': 'syllabus, page 15',
 'tables': [
  {'table': 'content and structure', 'out_of': 16, 'levels': [
   L(6, '14-16', 'content complex, engaging and effective; structure secure, balanced and managed for deliberate effect. Descriptive: many well-defined, developed ideas and images build a convincing overall picture with varied focus. Narrative: a well-defined, strongly developed plot using features of fiction — description, characterisation, an effective climax, convincing detail'),
   L(5, '11-13', 'developed, engaging, effective content; a well-managed structure with some deliberate choices. Descriptive: frequent, well-chosen images and details give a mostly convincing picture. Narrative: a defined, developed plot with features of fiction including a climax'),
   L(4, '8-10', 'relevant content with some development; a competently managed structure. Descriptive: a relevant selection of ideas, images and details, even where it drifts toward narrative. Narrative: a relevant, cohesive plot with some characterisation and setting'),
   L(3, '5-7', 'straightforward, briefly developed content; mostly organised, not always effectively. Descriptive: relevant but straightforward details, possibly more like a narrative. Narrative: a straightforward plot with limited use of narrative features'),
   L(2, '3-4', 'simple content with limited ideas or events; partly organised. Descriptive: some relevant events recorded with little detail. Narrative: simple events only partly linked or partly clear'),
   L(1, '1-2', 'only occasionally relevant or clear; a limited, ineffective structure. Descriptive: unclear and lacking detail. Narrative: incoherent')]},
  {'table': 'style and accuracy', 'out_of': 24, 'levels': [
   L(6, '21-24', 'precise, well-chosen vocabulary and sentence structures varied for effect; a consistent, well-judged register; accuracy almost always secure'),
   L(5, '17-20', 'mostly precise vocabulary; a range of structures mostly used for effect; a mostly consistent register; mostly accurate, with occasional minor errors'),
   L(4, '13-16', 'some precise vocabulary; a range of structures sometimes used for effect; some appropriate register; generally accurate, with some errors'),
   L(3, '9-12', 'simple vocabulary and straightforward structures; a simple register with general awareness of the context; frequent errors, occasionally serious'),
   L(2, '5-8', 'limited or imprecise vocabulary and structures; a limited register; persistent errors'),
   L(1, '1-4', 'frequently imprecise vocabulary and structures; little sense of the context; errors that get in the way of meaning')]}]}
TOPIC_TASKS = {'1.1': ['P1-Q1-comprehension'], '1.2': ['P1-Q1-summary'], '1.3': ['P1-Q2-short-answers'],
               '1.4': ['P1-Q2-short-answers', 'P1-Q2-language-task'], '1.5': ['P1-Q3'], '2.1': ['P2-A'],
               '2.2': ['P2-A'], '2.3': ['P2-B'], '2.4': ['P2-B'], '2.5': ['P2-A', 'P2-B']}

# ------------------------------------------------------------------------------------ VALIDATE
problems = []
OBJ = {}          # (topic, key) -> objective record
for t in TOPICS:
    cont_text, cont_page = t['container']
    if not on_page(cont_text, cont_page):
        problems.append('%s container not on page %d: %s' % (t['id'], cont_page, cont_text))
    for (k, st, txt, pg, subs, cws, learner, tier) in t['objectives']:
        if not on_page(txt, pg):
            problems.append('%s-%s not on page %d: %s' % (t['id'], k, pg, txt))
        OBJ[(t['id'], k)] = {'id': None, 'sub_topic': st, 'syllabus_text': txt, 'page': pg, 'subs': subs, 'cws': cws,
                             'learner': learner, 'tier': tier}
    # ids: OBJ-0500-<sub_topic>-<nn>
    per = collections.Counter()
    for (k, st, *_rest) in t['objectives']:
        per[st] += 1
        OBJ[(t['id'], k)]['id'] = 'OBJ-%s-%s-%02d' % (CODE, st, per[st])
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
for m in MISCONCEPTIONS:
    if not any(s[5] == m[0] for s in F.get(m[1], [])):
        problems.append('misconception %s has no MISCON slot' % m[0])
    theme_series(m[3], m[4])
for t in TOPICS:
    tid = t['id']
    for (k, *_r) in t['objectives']:
        o = OBJ[(tid, k)]
        if not any(s[0] == k for s in F[tid]):
            problems.append('%s-%s has no flashcard' % (tid, k))
        for cw in o['cws']:
            if not (any(s[0] == k and s[3] == cw for s in F[tid]) or any(k in p[2] and p[4] == cw for p in P[tid])):
                problems.append('%s-%s carries %s but no slot instructs with it (C-15)' % (tid, k, cw))
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


# -- profiles
QP = {
 'profile_id': 'cambridge-0500-igcse-2024-2026', 'version': '0.1.0-draft', 'status': 'draft',
 'board': 'Cambridge International Education', 'qualification': 'Cambridge IGCSE',
 'subject': 'First Language English', 'syllabus_code': CODE, 'syllabus_version': '1',
 'examination_years': [2024, 2025, 2026], 'route': 'components 12 and 22 (Paper 1 Reading, Paper 2 Directed Writing and Composition)',
 'source': FACTS['source_document'],
 'assessment_objectives': [
  {'code': a['code'], 'name': a['name'], 'qualification_weight_percent': a['qualification_weight_percent'],
   **({'weight_note': a['weight_note']} if a.get('weight_note') else {})} for a in FACTS['assessment_objectives']],
 'papers': [
  {'paper_id': 'P%s' % p['paper'], 'name': p['name'], 'duration_minutes': p['duration_minutes'], 'marks': p['marks'],
   'qualification_weight_percent': 50, 'question_basis': p['description'],
   'assessment_objective_weights': FACTS['ao_weights']['per_component_percent']['P%s' % p['paper']]}
  for p in FACTS['papers']],
 'learner_context': {'region': 'Namibia', 'medium': 'English', 'currency': 'N$',
                     'note': 'First-language English candidates. Speaking and Listening is separately endorsed and is not in this route.'},
}
SP = {
 'profile_id': 'yyeni-subject-first-language-english-igcse-v0.1.0', 'version': '0.1.0-draft', 'status': 'draft',
 'subject_name': 'First Language English (Cambridge IGCSE 0500)', 'language_variant': 'British English',
 'purpose': ('The teaching model for IGCSE First Language English. Unlike a content subject, 0500 is examined by task '
             'and skill: five reading skills (R1-R5) and five writing skills (W1-W5), each tested in named tasks on unseen '
             'texts. The resource therefore teaches techniques, practises them on short original extracts in flashcards, '
             'and rehearses the full tasks on original practice texts written to the lengths the syllabus sets.'),
 'depth_model': {'note_mode': 'full teaching depth',
                 'rationale': ('Notes teach each move a task rewards, demonstrate it step by step on a short original extract, '
                               'and name the errors that cost marks as discriminations. They are the source for the flashcards and a '
                               'standalone study text.'),
                 'words_per_objective': '300-450'},
 'terminology_rules': ['Use the syllabus wording for the tasks, the skills (R1-R5, W1-W5) and the six text types.',
                       'Use the glossary senses exactly: curriculum/glossary.json.',
                       'British spelling throughout.'],
 'answer_structures': ANSWER_STRUCTURES,
 'variant_register': VARIANT_REGISTER,
 'conditioned_mechanisms': CONDITIONED,
 'prohibited_patterns': [
  'Do not reproduce any Cambridge text, question, task, title, mark-scheme or examiner-report wording.',
  'Do not claim what examiners reward, report or want; teach the technique and why it works.',
  'Do not say that spelling, punctuation and grammar are marked in Paper 1; the syllabus removed W5 from Paper 1 from 2024.',
  'Do not teach the coursework or the speaking and listening components; this route sits Papers 1 and 2 only.'],
 'glossary_homonyms': [
  {'term': 'summary', 'senses': ['the Paper 1 selective summary on a stated focus', 'a general retelling of a text'],
   'rule': 'In this subject it always means the selective sense unless a block says otherwise.'},
  {'term': 'evaluate', 'senses': ['judge how convincing an idea is (directed writing)', 'the everyday sense of assessing'],
   'rule': 'Use the directed-writing sense and say what the judgement rests on.'},
  {'term': 'context', 'senses': ['the words around a word (Question 2)', 'the situation a piece of writing is for (register)'],
   'rule': 'Say which sense the first time it appears in a block.'}],
}
for fn, obj in (('qualification-profile.yaml', QP), ('subject-profile.yaml', SP)):
    with open(os.path.join(WS, fn), 'w', encoding='utf-8') as fh:
        yaml.safe_dump(obj, fh, sort_keys=False, allow_unicode=True, width=110)

# -- registry
reg = {'registry_id': 'REGISTRY-CIE-0500-IGCSE-2026', 'qualification_profile_id': QP['profile_id'],
       'subject_profile_id': SP['profile_id'], 'generated_at': NOW, 'authority': FACTS['authority'],
       'granularity_note': ('0500 assesses by task. One topic per paper task (or per Paper 2 skill); one objective per '
                            'syllabus statement of what that task assesses, transcribed with its page. Topic containers '
                            'carry the task heading.'),
       'objectives': []}
SRC = ('Third-party 0500 revision notes are held but predate the 2024-2026 syllabus and are not approved for derivation '
       '(R-04). Content is authored from the syllabus wording and the assessment corpus.')
for t in TOPICS:
    reg['objectives'].append({
     'objective_id': 'OBJ-%s-%s' % (CODE, t['id']), 'parent_id': None, 'topic_id': t['id'],
     'syllabus_text': t['container'][0], 'syllabus_page': t['container'][1], 'task': t['task'],
     'learner_objective': '%s (%s)' % (t['title'], t['task']), 'level': 'IGCSE', 'route_status': 'core', 'mandatory': True,
     'objective_type': 'task', 'assessment_objectives': ao_of(sorted({s for o in t['objectives'] for s in o[4]})),
     'sub_objectives': sorted({s for o in t['objectives'] for s in o[4]}), 'command_words': [],
     'prerequisite_ids': [], 'related_ids': [], 'depth_tier': 4,
     'source_coverage': {'rating': 0, 'action': 'generate_gap', 'rationale': SRC}, 'status': 'planned'})
    for (k, st, txt, pg, subs, cws, learner, tier) in t['objectives']:
        o = OBJ[(t['id'], k)]
        reg['objectives'].append({
         'objective_id': o['id'], 'parent_id': 'OBJ-%s-%s' % (CODE, t['id']), 'topic_id': t['id'],
         'syllabus_text': txt, 'syllabus_page': pg, 'task': t['task'], 'learner_objective': learner,
         'sub_topic': st, 'sub_topic_heading': t['sub_topics'][st], 'level': 'IGCSE', 'route_status': 'core',
         'mandatory': True, 'objective_type': 'reading_skill' if ao_of(subs) == ['AO1'] else 'writing_skill' if ao_of(subs) == ['AO2'] else 'reading_and_writing',
         'assessment_objectives': ao_of(subs), 'sub_objectives': subs, 'command_words': cws,
         'prerequisite_ids': [], 'related_ids': [], 'depth_tier': tier,
         'source_coverage': {'rating': 0, 'action': 'generate_gap', 'rationale': SRC}, 'status': 'planned'})
wj('curriculum/objective_registry.json', reg)
wj('curriculum/unit_titles.json', UNITS)

# -- framework
cw_rows = []
for c in FACTS['command_words']:
    w = c['word']
    if w == 'Describe':
        obs = {'where': 'Paper 2 Section B titles', 'count': TITLES['Describe'], 'of_titles': 4 * N_P2,
               'tariff': 40, 'note': 'opens %d of the %d composition titles; the rest open with "Write" (%d)'
                                     % (TITLES['Describe'], 4 * N_P2, TITLES['Write'])}
        modal = 40
    else:
        tar = dict(sorted(CW[w].items()))
        obs = {'where': 'Paper 1 mark-scheme stems (first command word, one count per question part)',
               'count': sum(tar.values()), 'observed_tariffs': {str(k): v for k, v in tar.items()}}
        modal = max(tar, key=tar.get) if tar else None
    cw_rows.append({'word': w, 'meaning': c['meaning'], 'meaning_provenance': 'syllabus, page %d' % c['source']['page'],
                    'in_syllabus_table': True, 'syllabus_page': c['source']['page'], 'syllabus_verbatim': c['verbatim'],
                    'used_at_level': True, 'use_in_prompts': True,
                    'observed': obs, 'observed_provenance': 'corpus', 'modal_tariff': modal,
                    'verdict': 'primary' if w in ('Identify', 'Explain') else 'secondary'})
framework = {
 'framework_id': 'ASSESS-CIE-0500-IGCSE-2026', 'generated_at': NOW, 'generated_by': 'build_0500.py, from curriculum/syllabus-facts.json',
 'authority': FACTS['authority'],
 'provenance_rule': ('Every value carries one of three provenances. "syllabus" is transcribed from the named page and is the '
                     'authority. "corpus" is counted from the published papers. "judgement" is our reading and is neither. '
                     'A value that cannot name where it came from is a value we do not have.'),
 'syllabus_facts_ref': 'curriculum/syllabus-facts.json',
 'assessment_objectives': [{'code': a['code'], 'name': a['name'], 'qualification_weight_percent': a['qualification_weight_percent'],
                            'provenance': 'syllabus, page 10', **({'note': a['weight_note']} if a.get('weight_note') else {})}
                           for a in FACTS['assessment_objectives']],
 'sub_objectives': {'note': 'The assessed grain. Syllabus, page 9, verbatim.',
                    'R1': 'demonstrate understanding of explicit meanings',
                    'R2': 'demonstrate understanding of implicit meanings and attitudes',
                    'R3': 'analyse, evaluate and develop facts, ideas and opinions, using appropriate support from the text',
                    'R4': 'demonstrate understanding of how writers achieve effects and influence readers',
                    'R5': 'select and use information for specific purposes',
                    'W1': 'articulate experience and express what is thought, felt and imagined',
                    'W2': 'organise and structure ideas and opinions for deliberate effect',
                    'W3': 'use a range of vocabulary and sentence structures appropriate to context',
                    'W4': 'use register appropriate to context',
                    'W5': 'make accurate use of spelling, punctuation and grammar'},
 'per_component_ao_percent': FACTS['ao_weights']['per_component_percent'], 'per_component_provenance': 'syllabus, page 10',
 'w5_change': {'fact': 'W5 has been removed from Paper 1 (Question 1(f) and Question 3). It is assessed in Paper 2 only.',
               'provenance': 'syllabus, page 35'},
 'papers': [{'paper': p['paper'], 'name': p['name'], 'marks': p['marks'], 'duration_minutes': p['duration_minutes'],
             'weight_percent': 50, 'ao_split': FACTS['ao_weights']['per_component_percent']['P%s' % p['paper']],
             'structure': p['description'], 'provenance': 'syllabus, pages 8, 13-15'} for p in FACTS['papers']],
 'tasks': 'curriculum/answer-shapes.json',
 'command_word_table_source': 'syllabus, page %d, %d words' % (FACTS['command_word_table']['page'], FACTS['command_word_table']['count']),
 'command_word_reconciliation': ('0500 is task-led, not command-word-led. The four listed words open the short items; the '
                                 'extended tasks are instructions (summarise, write a letter, analyse the language of two '
                                 'paragraphs). A prompt uses the four words where the papers use them, and otherwise the '
                                 'task form of the paper it models.'),
 'command_words': cw_rows,
 'command_words_in_use': [c['word'] for c in cw_rows],
 'command_words_listed_but_never_used': [],
 'command_words_used_but_not_listed': [
  {'word': 'Write', 'where': 'opens %d Paper 2 composition titles and the directed-writing task' % TITLES['Write'], 'provenance': 'corpus',
   'use_in_prompts': 'as a task instruction only'},
  {'word': 'evaluate', 'where': 'opens the first bullet of all 32 readable directed-writing tasks', 'provenance': 'corpus',
   'use_in_prompts': 'inside a directed-writing task only'}],
 'flashcard_subtype_ao_map': [{'subtype': st, 'assessment_objectives': ['AO1', 'AO2'], 'tests': v[0], 'blooms_level': v[1]}
                              for st, v in SUBTYPE.items()],
 'subtype_ao_note': ('0500’s two AOs are domains (reading, writing), not cognitive levels, so any card subtype can serve '
                     'either. The slot decides: a card on a reading skill carries AO1, on a writing skill AO2, and both where '
                     'it practises both. The finer grain is sub_objectives (R1-R5, W1-W5) on every slot.'),
 'blooms_taxonomy': {'scheme': 'Revised Bloom’s taxonomy (Anderson and Krathwohl).',
                     'why_both': ('The assessment objective says what the examination credits. The Bloom level says what the '
                                  'learner is being asked to do. They are different axes and every item carries both.'),
                     'levels': [{'level': a, 'means': b} for a, b in BLOOM_LEVELS],
                     'by_subtype': {st: v[1] for st, v in SUBTYPE.items()},
                     'by_performance_task': PERF_TYPES, 'required_on_every_item': True},
 'item_mix_target_note': ('No per-topic AO target is set, so C-18 reports not_run. Each 0500 topic is one task, so a topic’s '
                          'AO mix is fixed by the task, and balancing it by item count would be meaningless. The subject is '
                          'balanced by marks: the practice tasks reproduce both papers, 80 reading and 80 writing marks.'),
 'grade_thresholds': None,
}
med = lambda comp, g: statistics.median([r[comp][g] for r in THR if r.get(comp) and g in r[comp]])
framework['grade_thresholds'] = {
 'provenance': 'corpus: %d grade threshold tables, 2020-2025, components 12 and 22' % len(THR),
 'median_minimum_marks': {'P1': {g: med('c12', g) for g in ('A', 'C', 'E')}, 'P2': {g: med('c22', g) for g in ('A', 'C', 'E')},
                          'overall_of_160': {g: med('opt', g) for g in ('A*', 'A', 'C')}},
 'november_series': {r['series']: {g: r['opt'][g] for g in ('A*', 'A', 'C')} for r in THR if r['series'].startswith('w')}}
wj('curriculum/assessment-framework.json', framework)

# -- task specifications (answer shapes)
wj('curriculum/answer-shapes.json', {
 '_provenance': {'syllabus': 'marks, sub-objectives, lengths, texts and text types: syllabus pages 13-15',
                 'corpus': ('item layouts, the 16/24 composition split and the level ladders: the 84 published mark schemes, '
                            '2020-2025; each ladder appears unchanged in 39-42 of the 42 schemes for its paper'),
                 'derivation_policy': ('The level descriptors are paraphrased in our words. No mark-scheme wording is to reach '
                                       'learner-facing output; paraphrase again when teaching them.'),
                 'generated': NOW},
 CODE: {'subject': 'Cambridge IGCSE First Language English', 'tasks': TASKS}})

# -- misconceptions
wj('curriculum/misconceptions.json', {
 'register_id': 'MISCON-CIE-0500-IGCSE-2026', 'generated_at': NOW,
 'authority': 'Cambridge Principal Examiner Reports for Teachers, 0500, 17 series 2020-2025.',
 'derivation_policy': 'Examiner-evidenced errors, restated in our words. No examiner-report wording appears in learner-facing output.',
 'how_to_use': ('Every entry earns one MISCON card on the objective it attaches to (the work order names the slot). A MISCON '
                'card is a DISCRIMINATION: it states the error, the correct move, and the test that tells them apart. It does '
                'not simply restate the correct technique.'),
 'entries': [{'misconception_id': m[0], 'topic_id': m[1], 'objective_id': OBJ[(m[1], m[2])]['id'], 'report_task': m[3],
              'report_theme': m[4], 'series_raising_theme': '%d of %d' % theme_series(m[3], m[4]),
              'learners': m[5], 'test': m[6]} for m in MISCONCEPTIONS]})

# -- glossary
wj('curriculum/glossary.json', {'glossary_id': 'GLOSSARY-CIE-0500-IGCSE-2026', 'status': 'settled',
                                'note': 'Use these senses exactly. Do not invent alternatives.',
                                'terms': [dict({'term': a, 'sense': b}, **({'boundary': c} if c else {})) for a, b, c in GLOSSARY]})

# -- exposure
exp = {'exposure_id': 'EXPOSURE-CIE-0500-IGCSE-2026', 'generated_at': NOW,
       'authority': 'Cambridge IGCSE First Language English 0500, 84 published question papers and mark schemes, 2020-2025.',
       'evidence_window': '%d Paper 1 and %d Paper 2 question papers, 17 series.' % (N_P1, N_P2),
       'method': ('0500 has no optional content: every task is compulsory on every paper, so every objective is tested in '
                  'every paper of its component. The class is structural, not a frequency.'),
       'principle': 'RS-05: exposure calibrates emphasis. Every objective in scope is taught and practised.',
       'status': 'structural', 'classes': {'every_paper': 'tested by a compulsory task on every paper of its component'},
       'objectives': []}
for t in TOPICS:
    for (k, *_r) in t['objectives']:
        o = OBJ[(t['id'], k)]
        req = sorted({'MISCON'} if any(m[1] == t['id'] and m[2] == k for m in MISCONCEPTIONS) else set())
        exp['objectives'].append({'objective_id': o['id'], 'topic_id': t['id'], 'syllabus_text': o['syllabus_text'],
                                  'task': t['task'], 'papers_in_corpus': N_P1 if t['paper'] == 'P1' else N_P2,
                                  'exam_exposure': 'every_paper', 'required_subtypes': req})
wj('curriculum/exam-exposure.json', exp)

# -- exclusions
wj('curriculum/syllabus-exclusions.json', {
 'stated_in_the_syllabus': [
  {'fact': 'W5 (spelling, punctuation and grammar) is not assessed in Paper 1 from 2024; it is removed from Question 1(f) and Question 3.', 'page': 35},
  {'fact': 'Dictionaries may not be used in Paper 1 or Paper 2.', 'pages': [13, 15]}],
 'not_in_this_route': {'terms': NOT_IN_ROUTE, 'why': 'This learner sits components 12 and 22 (syllabus-facts.json papers_sat).'}})

# ----------------------------------------------------------------------------------- CONTRACTS
DIFF_PERF = lambda m: 2 if (m or 0) <= 1 else 3 if m <= 3 else 4 if m <= 15 else 5


def slots_for(tid):
    out, n = [], 0
    for (k, st, teaches, cw, tar, mc) in F[tid]:
        n += 1
        o = OBJ[(tid, k)]
        s = {'slot': 'ITEM-%s-%s-%03d-%s' % (CODE, tid, n, st), 'objective_id': o['id'], 'objective_title': o['learner'],
             'syllabus_text': o['syllabus_text'], 'subtype': st, 'assessment_objectives': ao_of(o['subs']),
             'sub_objectives': o['subs'], 'command_word': cw, 'mark_tariff': tar, 'difficulty': SUBTYPE[st][2],
             'blooms_level': SUBTYPE[st][1], 'teaches': teaches,
             'marking_guidance_must_name': ANSWER_STRUCTURES[st]}
        if mc:
            s['misconception_id'] = mc
        s['reason'] = ('models a Paper %s item: %s, %d mark%s' % (TOPICS_BY[tid]['paper'][1], cw, tar, '' if tar == 1 else 's')
                       if cw else 'the misconception register records this error' if mc else 'a technique the task depends on')
        out.append(s)
    return out


TOPICS_BY = {t['id']: t for t in TOPICS}


def perf_for(tid):
    out = []
    for n, (itype, tix, keys, subs, cw, tar, bloom, brief) in enumerate(P[tid], 1):
        s = {'slot': 'ITEM-%s-%s-P%02d' % (CODE, tid, n), 'item_type': itype,
             'objective_ids': [OBJ[(tid, k)]['id'] for k in keys], 'sub_objectives': subs,
             'assessment_objectives': ao_of(subs), 'command_word': cw, 'mark_tariff': tar,
             'difficulty': DIFF_PERF(tar), 'blooms_level': bloom, 'brief': brief,
             'models': TOPIC_TASKS[tid], 'marking_guidance_must_name': ANSWER_STRUCTURES[itype]}
        if tix is not None:
            s['text_id'] = TEXTS[tid][tix][0]
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
                                    'syllabus_page': o['page'], 'sub_objectives': o['subs']} for o in objs],
                    'word_budget': [max(500, 300 * n), max(800, 450 * n)],
                    'blocks_required': [
                     'a plain explanation block for every objective above, in the glossary’s senses',
                     'at least one worked demonstration: a short original extract (no more than 120 words) and the move carried out on it step by step',
                     'a block that restates each misconception attached to these objectives as a discrimination: the error, the correct move, the test',
                     'where this unit introduces its task, what the syllabus states about it (marks, length, texts) and nothing the syllabus does not state']})
    return out


ADJ = {'1.1': [('selective summary', '1.2'), ('language analysis', '1.4')], '1.2': [('comprehension', '1.1')],
       '1.3': [('language analysis', '1.4')], '1.4': [('word-or-phrase items', '1.3')],
       '1.5': [('directed writing', '2.1 and 2.2')], '2.1': [('form and register', '2.2')],
       '2.2': [('evaluating the texts', '2.1'), ('accuracy', '2.5')], '2.3': [('narrative', '2.4'), ('accuracy', '2.5')],
       '2.4': [('descriptive', '2.3'), ('accuracy', '2.5')], '2.5': [('composition content', '2.3 and 2.4')]}

WORK = {}
for t in TOPICS:
    tid, title = t['id'], t['title']
    fl, pf, cu = slots_for(tid), perf_for(tid), units_for(t)
    texts = [{'text_id': x[0], 'file': 'texts/%s.md' % x[0], 'words_min': x[1], 'words_max': x[2], 'genre': x[3],
              'used_by': [p['slot'] for p in pf if p.get('text_id') == x[0]]} for x in TEXTS.get(tid, [])]
    items = fl + pf
    bl = collections.Counter(s['blooms_level'] for s in items)
    subs = collections.Counter(x for s in items for x in s['sub_objectives'])
    wb = [sum(u['word_budget'][0] for u in cu), sum(u['word_budget'][1] for u in cu)]
    contract = {
     'contract_id': 'CONTRACT-%s-%s' % (CODE, tid), 'topic_id': tid, 'topic_title': title,
     'unit': 'Unit %s — %s' % (tid[0], UNITS[tid[0]]), 'qualification': WS_NAME, 'standard_version': '0.2.0-draft',
     'generated_at': NOW, 'generated_by': 'build_0500.py', 'status': 'active',
     'scope': {'task': t['task'], 'included_objective_ids': [OBJ[(tid, o[0])]['id'] for o in t['objectives']],
               'included_count': len(t['objectives']),
               'sub_objectives': sorted({s for o in t['objectives'] for s in o[4]}),
               'depth_tiers': dict(collections.Counter(str(o[7]) for o in t['objectives']))},
     'target_learner_profile': {'prior_teaching': 'First-language English learners; no prior knowledge of the paper assumed.',
                                'context': 'Namibian secondary learners, Cambridge IGCSE, English medium, sitting the October/November 2026 series.',
                                'note_purpose': ['source of record for flashcard generation', 'offline reading', 'standalone study text']},
     'assessment_expectations': {
      'papers': [t['paper']], 'task_specifications': ['curriculum/answer-shapes.json -> %s' % x for x in TOPIC_TASKS[tid]],
      'command_words_in_scope': sorted({c for o in t['objectives'] for c in o[5]}),
      'command_words_note': ('Only four command words exist (syllabus page 30). Use one only where a slot names it; '
                             'otherwise use the task form of the paper item the slot models.'),
      'ao_targets': framework['per_component_ao_percent'][t['paper']],
      'ao_note': 'The syllabus’s split for this paper, by marks (page 10). Not a per-topic item-count target.'},
     'exposure': {'class': 'every_paper', 'principle': exp['principle']},
     'depth_constraints': {
      'note_mode': 'full teaching depth', 'word_budget': {'min': wb[0], 'max': wb[1]}, 'item_budget': len(items),
      'excluded_constructs': list(NOT_IN_ROUTE),
      'excluded_constructs_source': ('Components this learner does not sit (route 12 and 22). C-11 scans learner-facing text for '
                                     'these exact terms, so they are short terms, not sentences.'),
      'stated_in_the_syllabus': ['W5 is not assessed in Paper 1 (page 35): never say accuracy is marked in Paper 1.'] if t['paper'] == 'P1' else [],
      'adjacent_topics': ['%s — taught in topic %s; name it in passing if you must, teach it there' % a for a in ADJ.get(tid, [])]},
     'required_outputs': {'claim_ledger': True, 'content_units': len(cu), 'learning_items': len(items), 'notes': True,
                          'practice_texts': len(texts)},
     'misconceptions': 'curriculum/misconceptions.json (filter on topic_id "%s")' % tid,
     'subtype_waivers': [],
     'item_budget_note': 'Set from the work order, which is the operative plan.'}
    wo = {
     'work_order_id': 'WO-%s-%s' % (CODE, tid), 'topic_id': tid, 'topic_title': title, 'topic': topic_label(tid, title),
     'task': t['task'], 'generated_by': 'build_0500.py — regenerate, never edit', 'standard': 'v0.2.0-draft',
     'authoring_note': ('Every slot is decided. Write the prose, the texts and the items; do not redesign the plan. If a slot '
                        'is wrong for its objective, change it and record {from, to, why} in authoring_notes.json.'),
     'output_files': {'claims': 'claims/canonical_claim_ledger.json', 'content_units': [u['file'] for u in cu],
                      'learning_items': 'learning-items/topic_%s_items.json' % tid, 'texts': [x['file'] for x in texts],
                      'notes': notes_filename(tid, title), 'flashcards_when_published': flashcards_filename(tid, title)},
     'assessable_objective_count': len(t['objectives']),
     'claims_plan': {'per_objective': '3 to 6', 'approximate_total': [3 * len(t['objectives']), 6 * len(t['objectives'])],
                     'what_a_claim_is': ('one statement the notes teach and a card rests on: a definition, a convention of a '
                                         'form, a step of a technique, or why a move works. Technique claims are claims.')},
     'content_units': cu, 'practice_texts': texts, 'item_slots': fl, 'performance_tasks': pf,
     'planned_item_count': len(items), 'planned_flashcards': len(fl), 'planned_performance_tasks': len(pf),
     'planned_blooms_mix': {b: {'items': bl[b], 'share_percent': round(100 * bl[b] / len(items))}
                            for b, _ in BLOOM_LEVELS},
     'planned_sub_objective_coverage': dict(sorted(subs.items())),
     'excluded_constructs': list(NOT_IN_ROUTE), 'subtype_waivers': []}
    WORK[tid] = wo
    wj('topics/%s/contract.json' % tid, contract)
    wj('topics/%s/work_order.json' % tid, wo)
    md = ['# Work order — %s' % topic_label(tid, title), '', '**Task:** %s  ' % t['task'],
          '**Items:** %d (%d flashcards, %d performance tasks) · **practice texts:** %d · **notes:** %d–%d words'
          % (len(items), len(fl), len(pf), len(texts), wb[0], wb[1]), '', '## Objectives', '',
          '| id | syllabus text (page) | skills | command words |', '|---|---|---|---|']
    for o in t['objectives']:
        r = OBJ[(tid, o[0])]
        md.append('| %s | %s (p%d) | %s | %s |' % (r['id'], r['syllabus_text'], r['page'], ', '.join(r['subs']), ', '.join(r['cws']) or '—'))
    md += ['', '## Flashcard slots', '', '| slot | subtype | Bloom | skills | command word · tariff | teaches |', '|---|---|---|---|---|---|']
    for s in fl:
        md.append('| %s | %s | %s | %s | %s | %s%s |' % (s['slot'], s['subtype'], s['blooms_level'], ', '.join(s['sub_objectives']),
                  ('%s · %d' % (s['command_word'], s['mark_tariff'])) if s['command_word'] else '—', s['teaches'],
                  ' (%s)' % s['misconception_id'] if s.get('misconception_id') else ''))
    md += ['', '## Performance tasks', '', '| slot | type | text | Bloom | skills | tariff | brief |', '|---|---|---|---|---|---|---|']
    for s in pf:
        md.append('| %s | %s | %s | %s | %s | %s | %s |' % (s['slot'], s['item_type'], s.get('text_id', '—'), s['blooms_level'],
                  ', '.join(s['sub_objectives']), s['mark_tariff'] if s['mark_tariff'] is not None else '—', s['brief']))
    if texts:
        md += ['', '## Practice texts', '', '| text | words | genre | used by |', '|---|---|---|---|']
        for x in texts:
            md.append('| %s | %d–%d | %s | %d tasks |' % (x['text_id'], x['words_min'], x['words_max'], x['genre'], len(x['used_by'])))
    md += ['', '## Out of scope', '', ', '.join('`%s`' % c for c in NOT_IN_ROUTE)] + \
          ['- %s' % a for a in contract['depth_constraints']['adjacent_topics']] + ['']
    wt('topics/%s/work_order.md' % tid, '\n'.join(md))

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
json.dump({'TOT': TOT, 'BLOOM': BLOOM_ALL}, open(os.path.join(WS, 'curriculum', '.build_totals.json'), 'w'))
print('0500 plan data written: %(topics)d topics, %(objectives)d objectives, %(flash)d flashcards + %(perf)d performance '
      'tasks = %(items)d items, %(texts)d practice texts' % TOT)
