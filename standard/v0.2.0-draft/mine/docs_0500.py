# -*- coding: utf-8 -*-
"""Write PLAN-0500 and HANDOVER-0500 from the files build_0500.py wrote. Regenerate, never edit."""
import collections, datetime, json, os, sys
HOME = os.path.expanduser('~')
REPO = os.path.join(HOME, 'mnt', 'YYeni Study Resources')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design_0500 import CODE, SLUG, WS_NAME, TOPICS, NOT_IN_ROUTE, UNITS  # noqa: E402
WS = os.path.join(REPO, 'work', WS_NAME)
REL = 'work/' + WS_NAME
J = lambda rel: json.load(open(os.path.join(WS, rel)))
FACTS, FW, SH, MC, REG = (J('curriculum/syllabus-facts.json'), J('curriculum/assessment-framework.json'),
                          J('curriculum/answer-shapes.json')[CODE]['tasks'], J('curriculum/misconceptions.json'),
                          J('curriculum/objective_registry.json'))
WO = {t['id']: J('topics/%s/work_order.json' % t['id']) for t in TOPICS}
CT = {t['id']: J('topics/%s/contract.json' % t['id']) for t in TOPICS}
TODAY = datetime.date.today().strftime('%-d %B %Y').lstrip('0')
ANALYSIS = 'operations/analysis/%s-%s-corpus-analysis.md' % (CODE, SLUG)
BRIEF = '%s/SYLLABUS-BRIEF-%s-%s.md' % (REL, CODE, SLUG)
PLAN = 'PLAN-%s-%s.md' % (CODE, SLUG)
HAND = 'HANDOVER-%s-%s.md' % (CODE, SLUG)
ORDER = [t['id'] for t in TOPICS]
N = {'flash': sum(w['planned_flashcards'] for w in WO.values()), 'perf': sum(w['planned_performance_tasks'] for w in WO.values()),
     'texts': sum(len(w['practice_texts']) for w in WO.values()),
     'tw': (sum(x['words_min'] for w in WO.values() for x in w['practice_texts']), sum(x['words_max'] for w in WO.values() for x in w['practice_texts'])),
     'nw': (sum(c['depth_constraints']['word_budget']['min'] for c in CT.values()), sum(c['depth_constraints']['word_budget']['max'] for c in CT.values())),
     'obj': sum(len(t['objectives']) for t in TOPICS)}
N['items'] = N['flash'] + N['perf']
BL = collections.Counter(s['blooms_level'] for w in WO.values() for s in w['item_slots'] + w['performance_tasks'])
BLM = collections.Counter()
for w in WO.values():
    for s in w['performance_tasks']:
        BLM[s['blooms_level']] += s['mark_tariff'] or 0
ST = collections.Counter(s['subtype'] for w in WO.values() for s in w['item_slots'])
fmt = lambda n: format(n, ',')
thr = FW['grade_thresholds']
subs = FW['sub_objectives']

# =================================================================================== PLAN
P = []
a = P.append
a('# Plan — Cambridge IGCSE First Language English 0500')
a('')
a('Syllabus for 2024, 2025 and 2026, version 1 · route: components 12 (Paper 1 Reading) and 22 (Paper 2 Directed Writing and Composition) · first paper %s · plan generated %s' % (FACTS['first_exam'], TODAY))
a('')
a('This is the authoring brief for 0500 and nothing else. It stands on two earlier steps: step zero, the syllabus (`%s`, with every value in `curriculum/syllabus-facts.json` carrying its page and the verbatim line), and step one, the corpus analysis (`%s`). Values below are labelled **syllabus** (transcribed, page given), **corpus** (counted from 84 question papers, 84 mark schemes, 17 examiner reports and 17 threshold tables, 2020–2025) or **judgement** (our design). A value that cannot name where it came from is not in this plan.' % (BRIEF, ANALYSIS))
a('')
a('**The job:** %d topics, %d objectives, **%s items** (%s flashcards, %s performance tasks), %d original practice texts of %s–%s words, and %s–%s words of notes.' % (len(TOPICS), N['obj'], fmt(N['items']), fmt(N['flash']), fmt(N['perf']), N['texts'], fmt(N['tw'][0]), fmt(N['tw'][1]), fmt(N['nw'][0]), fmt(N['nw'][1])))
a('')
a('---')
a('')
a('## 0. What the syllabus says')
a('')
a('| | | source |')
a('|---|---|---|')
a('| AO1 Reading | 50% of the qualification | syllabus, p10 |')
a('| AO2 Writing | 50% of the qualification | syllabus, p10 |')
a('| Paper 1 Reading | 2 hours, 80 marks; AO1 80%, AO2 20% | syllabus, pp8, 10, 13 |')
a('| Paper 2 Directed Writing and Composition | 2 hours, 80 marks; AO1 20%, AO2 80% | syllabus, pp8, 10, 15 |')
a('| Speaking and Listening | separately endorsed; not in this route | syllabus, p10 |')
a('| W5 in Paper 1 | removed from Question 1(f) and Question 3 from 2024; W5 is marked in Paper 2 only | syllabus, p35 |')
a('| Dictionaries | may not be used in either paper | syllabus, pp13, 15 |')
a('')
a('**The assessed grain is the ten sub-objectives, not AO1 and AO2** (syllabus, p9). Every slot in every work order names the ones it practises.')
a('')
a('| | skill | | skill |')
a('|---|---|---|---|')
for r, w in zip(['R1', 'R2', 'R3', 'R4', 'R5'], ['W1', 'W2', 'W3', 'W4', 'W5']):
    a('| **%s** | %s | **%s** | %s |' % (r, subs[r], w, subs[w]))
a('')
a('**Where each is tested** (syllabus, pp13–15):')
a('')
a('| task | text | marks | reading | writing | length |')
a('|---|---|---:|---|---|---|')
a('| P1 Q1 comprehension | A, 700–750 words | 15 | R1 R2 R5 | — | short answers |')
a('| P1 Q1 summary | B, 700–750 words | 15 | 10: R1 R2 R5 | 5: W2 W3 | no more than 120 words |')
a('| P1 Q2 short answers | C, 500–650 words | 10 | R1 R2 R4 | — | answers of different lengths |')
a('| P1 Q2 language task | C | 15 | R1 R2 R4 | — | about 200–300 words |')
a('| P1 Q3 extended response | C | 25 | 15: R1 R2 R3 | 10: W1 W2 W3 W4 | about 250–350 words; letter, report, journal, speech, interview or article |')
a('| P2 Section A directed writing | one or two texts, 650–750 words | 40 | 15: R1 R2 R3 R5 | 25: W1–W5 | about 250–350 words; discursive, argumentative or persuasive speech, letter or article |')
a('| P2 Section B composition | one of four titles, two descriptive and two narrative | 40 | — | 40: W1–W5 | about 350–450 words |')
a('')
a('**Command words** (syllabus, p30: the complete list is four) against the papers (corpus):')
a('')
a('| word | syllabus meaning | what the papers do with it | in prompts |')
a('|---|---|---|---|')
for c in FW['command_words']:
    o = c['observed']
    if 'observed_tariffs' in o:
        use = '%d Paper 1 stems; tariffs %s' % (o['count'], ', '.join('%s mark%s × %d' % (k, '' if k == '1' else 's', v) for k, v in o['observed_tariffs'].items()))
    else:
        use = o['note']
    a('| **%s** | %s | %s | where a slot names it |' % (c['word'], c['meaning'], use))
a('')
a('0500 is **task-led, not command-word-led**. The four words open the short items. The extended tasks are instructions: summarise on a focus, write a letter in role, analyse the language of two paragraphs, write a description. So a prompt uses a command word only where its slot names one, and otherwise the task form of the paper item it models. Two words outside the table do work in the papers (corpus): "Write" opens %s and "evaluate" opens the first bullet of all 32 readable directed-writing tasks; each is used only inside its own task.' % FW['command_words_used_but_not_listed'][0]['where'].replace('opens ', ''))
a('')
a('## 1. What the corpus says')
a('')
a('The full analysis is `%s`. What the plan takes from it:' % ANALYSIS)
a('')
a('- **What a grade takes** (corpus, median of 17 series): Paper 1 C %d/80, A %d; Paper 2 C %d/80, A %d; overall C %d/160, A %d, A* %d. November runs higher than June in every year 2021–2025; in 2023–2025 a November C needed %d–%d and an A %d–%d. **Paper 1 is the harder paper.**' % (
    thr['median_minimum_marks']['P1']['C'], thr['median_minimum_marks']['P1']['A'], thr['median_minimum_marks']['P2']['C'], thr['median_minimum_marks']['P2']['A'],
    thr['median_minimum_marks']['overall_of_160']['C'], thr['median_minimum_marks']['overall_of_160']['A'], thr['median_minimum_marks']['overall_of_160']['A*'],
    min(thr['november_series'][s]['C'] for s in ('w23', 'w24', 'w25')), max(thr['november_series'][s]['C'] for s in ('w23', 'w24', 'w25')),
    min(thr['november_series'][s]['A'] for s in ('w23', 'w24', 'w25')), max(thr['november_series'][s]['A'] for s in ('w23', 'w24', 'w25'))))
a('- **Reading success** is restating accurately in one’s own words; finding every point on a summary’s focus and grouping them; explaining what language makes a reader see or feel, not only what it means; developing ideas from a text in role without inventing.')
a('- **Writing success** is evaluating two texts rather than summarising them, organised by argument; writing a form that reads as that form; knowing that a description is built from detail and a story from a shaped plot; accuracy, which counts in Paper 2.')
a('- **The errors the reports return to, series after series,** are the misconception register: %d entries in `curriculum/misconceptions.json`, each with the number of series whose reports raise its theme.' % len(MC['entries']))
a('')
a('## 2. How the resource is organised')
a('')
a('*Judgement.* 0500 has no content syllabus: the tasks are the subject. So each topic is **one paper task**, or one skill that runs across Paper 2, and its objectives are the syllabus’s own statements of what that task assesses, transcribed with their page and verified against it.')
a('')
a('| topic | task | objectives | flashcards | tasks | practice texts | notes words |')
a('|---|---|---:|---:|---:|---:|---|')
for t in TOPICS:
    w, c = WO[t['id']], CT[t['id']]
    a('| **%s** %s | %s | %d | %d | %d | %d | %s–%s |' % (t['id'], t['title'], t['task'], len(t['objectives']), w['planned_flashcards'], w['planned_performance_tasks'], len(w['practice_texts']), fmt(c['depth_constraints']['word_budget']['min']), fmt(c['depth_constraints']['word_budget']['max'])))
a('| | | **%d** | **%d** | **%d** | **%d** | **%s–%s** |' % (N['obj'], N['flash'], N['perf'], N['texts'], fmt(N['nw'][0]), fmt(N['nw'][1])))
a('')
a('**The objectives** (syllabus text verbatim, page cited):')
a('')
a('| objective | syllabus text | page | skills | command words |')
a('|---|---|---:|---|---|')
for o in REG['objectives']:
    if o.get('parent_id'):
        a('| %s | %s | %d | %s | %s |' % (o['objective_id'], o['syllabus_text'], o['syllabus_page'], ' '.join(o['sub_objectives']), ', '.join(o['command_words']) or '—'))
a('')
a('Topics are authored in the order listed. Paper 1 comes first because it is the harder paper (section 1).')
a('')
a('## 3. How each task is set and marked')
a('')
a('The full specification of every task, including each level table paraphrased band by band, is `curriculum/answer-shapes.json`. The marks, lengths, texts and skills are **syllabus**; the item layouts, the 16/24 composition split and the ladders are **corpus**, and every ladder appears unchanged in 39–42 of the 42 schemes for its paper. The ladders are paraphrased; paraphrase them again when teaching them.')
a('')
for k, s in SH.items():
    line = '- **%s** (%s, %d marks)' % (s['name'], s['paper'], s['marks'])
    if s.get('layout'):
        lay = s['layout']
        line += ': point-marked; ' + ('items of %s marks' % ', '.join(str(x) for x in lay) if isinstance(lay, list) else '; '.join('%s %s' % kv for kv in lay.items()))
    if s.get('tables'):
        tops = []
        for tb in s['tables']:
            top = tb['levels'][0]
            tops.append('%s /%d, %d levels; top band %s: %s' % (tb['table'], tb['out_of'], len(tb['levels']), top['marks'], top['requires']))
        line += '. ' + ' • '.join(tops)
    if s.get('set_as'):
        line += '. Set as: %s' % s['set_as']
    a(line + '.')
a('')
a('## 4. What each topic gets')
a('')
a('Every slot is decided in `topics/<T>/work_order.json` (and readable as `work_order.md`): its objective, subtype, sub-objectives, AO, **Bloom level**, command word and tariff where it models a paper item, and a one-line statement of what it teaches.')
a('')
a('| subtype | cards | what it is for in 0500 |')
a('|---|---:|---|')
for m in FW['flashcard_subtype_ao_map']:
    if ST[m['subtype']]:
        a('| %s | %d | %s |' % (m['subtype'], ST[m['subtype']], m['tests']))
a('')
a('- **MISCON cards** are discriminations, one per misconception-register entry, placed on the objective the error belongs to: the error, the correct move, and the test that tells them apart.')
a('- **APP, INTERP, MECH and EVAL cards supply their own sentence or short extract**, original and written for the card. A card never depends on a practice text or on another card.')
PT = {t: WO[t]['planned_performance_tasks'] for t in ORDER}
a('- **Performance tasks rehearse the paper**: %d comprehension items on %d Text A-style passages; %d summaries; %d word-and-phrase items on %d Text C-style passages; %d pairs of "one example" and language-task items; %d extended responses in %d different text types; %d evaluation plans; %d directed-writing tasks (letter, speech, article); %d descriptive and %d narrative compositions; %d editing and rewriting tasks.' % (PT['1.1'], len(WO['1.1']['practice_texts']), PT['1.2'], PT['1.3'], len(WO['1.3']['practice_texts']), PT['1.4'] // 2, PT['1.5'], PT['1.5'], PT['2.1'], PT['2.2'], PT['2.3'], PT['2.4'], PT['2.5']))
RM = collections.Counter()
for w in WO.values():
    for p_ in w['performance_tasks']:
        m = p_['mark_tariff'] or 0
        if p_['assessment_objectives'] == ['AO1']:
            RM['AO1'] += m
        elif p_['assessment_objectives'] == ['AO2']:
            RM['AO2'] += m
        else:
            tk = SH[p_['models'][-1]]
            for part in (tk.get('split') or {}).values():
                RM['AO1' if part['sub_objectives'][0].startswith('R') else 'AO2'] += part['marks']
FC = collections.Counter(tuple(s_['assessment_objectives']) for w in WO.values() for s_ in w['item_slots'])
a('- **AO balance by marks.** The exam is 80 reading and 80 writing marks. The rehearsed tasks here carry %d reading and %d writing marks, close to the exam\u2019s even split, with a composition counted as the single 40-mark task it is; %d flashcards practise reading skills and %d writing skills. No per-topic item-count target is set, because each topic is one task (C-18 reports not_run by design).' % (RM['AO1'], RM['AO2'], FC[('AO1',)], FC[('AO2',)]))
a('')
a('## 5. Bloom’s levels')
a('')
a('Every item carries its Bloom level and its AO; they are different axes. The level comes from the subtype for flashcards and from the task for performance items (`assessment-framework.json -> blooms_taxonomy`).')
a('')
a('| level | items | marks of practice carried by performance tasks |')
a('|---|---:|---:|')
for lv in ['Remember', 'Understand', 'Apply', 'Analyse', 'Evaluate', 'Create']:
    a('| %s | %d | %d |' % (lv, BL[lv], BLM[lv]))
a('')
a('By count the bank leans to Remember and Understand, because every technique needs its terms and its discriminations. By marks it leans the other way: **Create carries %d of the %d marks of rehearsed practice**, because Question 3, directed writing and composition are compositions. That is the shape of 0500, and it is why the notes must teach craft, not only terms.' % (BLM['Create'], sum(BLM.values())))
a('')
a('## 6. Practice texts (RS-48)')
a('')
a('%d texts, each **original**, written for its tasks, held at `topics/<T>/texts/<text_id>.md` with front matter `text_id`, `title`, `genre`, `setting`, `written_for`, `words_min`, `words_max`, `original: true`. Check C-43 enforces the file, the declaration and the length. The lengths are the syllabus’s own (p13, p15).' % N['texts'])
a('')
a('| topic | texts | words each | what the texts must make possible |')
a('|---|---:|---|---|')
NEED = {'1.1': 'seven items each: explicit details, two-part phrases worth explaining, implied attitudes, a paragraph holding three reasons',
        '1.2': 'at least ten distinct ideas on one focus, mixed with examples and off-focus material a learner must leave out',
        '1.3': 'seven target words and phrases each: four with a clear synonym in the text, three whose meaning depends on the sentence',
        '1.4': 'two named paragraphs dense with imagery and precise word choice, and a short extract for the "one example" item',
        '1.5': 'a person the learner can speak as, and material for three bullets that invites development',
        '2.1': 'views that can be judged: claims with thin support, a perspective that shapes the evidence, points where the texts conflict',
        '2.2': 'views on a question the learner can argue, for a named audience and form'}
for t in TOPICS:
    tx = WO[t['id']]['practice_texts']
    if tx:
        a('| %s | %d | %d–%d | %s |' % (t['id'], len(tx), tx[0]['words_min'], tx[0]['words_max'], NEED[t['id']]))
a('')
a('*Judgement:* settings are Namibian or southern African, with at least one text per topic set elsewhere. Genres vary as the syllabus asks (p11: fiction and non-fiction from the twentieth and twenty-first centuries, including articles, reviews and discursive essays). A text is never modelled on the subject of a Cambridge paper the author may know of.')
a('')
a('## 7. Answers and marking guidance')
a('')
a('- **Point-marked items** (comprehension, word-and-phrase, "one example"): the canonical answer, one mark per point, the acceptable alternatives, and what is not credited and why.')
a('- **Level-marked tasks** (summary, language task, extended response, directed writing, composition): a model answer written to the top band and inside the length, then guidance that names, table by table, the band descriptors (paraphrased) the answer meets and how. Add one or two sentences on what a middle-band answer to the same task would do instead, so a learner can place their own.')
a('- **Summaries** also list the content points on the focus, in our words.')
a('- Every item’s guidance names the parts its subtype or task type declares (`subject-profile.yaml -> answer_structures`, checked by C-16).')
a('')
a('## 8. Scope')
a('')
a('- Not in this route, and scanned for by C-11: %s.' % ', '.join('`%s`' % x for x in NOT_IN_ROUTE))
a('- Never say accuracy is marked in Paper 1 (syllabus, p35).')
a('- Each contract lists its adjacent topics: name them in passing if needed, teach them in their own topic.')
a('- Two conditioned mechanisms are registered (C-37): a short sentence creates emphasis *by contrast with longer ones*; a formal register is right *for an audience and a purpose*, not in general.')
a('')
a('## 9. What the checks catch, and what they do not')
a('')
a('The suite checks structure, traceability, coverage of every objective, command-word discipline, declared answer parts, misconception cards, universals, scope terms, conditioned mechanisms and practice-text length. A worked slice of topic 1.3 in `%s/exemplar/` passes all of it (`python3 standard/v0.2.0-draft/mine/exemplar_0500.py --prove`).' % REL)
a('')
a('It cannot judge whether a model composition is really top band, whether a practice text reads well, or whether a text echoes a published one. Those need review, which under RS-42 runs on published material. After the run, a planner audit compares every item’s Bloom level, sub-objectives, command word and tariff with its slot.')
a('')
a('## 10. Limits')
a('')
a('- No question-level assessment-evidence map is built for 0500, so C-39 reports not_run. Exposure is structural: every task is compulsory on every paper.')
a('- Third-party 0500 revision notes are held but predate this syllabus and are not approved for derivation; every claim is `generated_gap`.')
a('- The theme counts behind the misconceptions are keyword matches over examiner-report sentences. They show a theme is discussed each series, not how often it costs marks.')
a('')
a('## Derivation policy')
a('')
a('Official assessment material is `mine_do_not_reproduce`. No question, insert, task, title, mark-scheme or examiner-report wording appears in any learner-facing output. Mine the demand; write the text, the task and the answer yourself.')
a('')
open(os.path.join(WS, PLAN), 'w').write('\n'.join(P))

# =================================================================================== HANDOVER
H = []
h = H.append
h('# Handover prompt — Cambridge IGCSE First Language English 0500')
h('')
h('Paste everything below the line into Hermes Agent or OpenCode with this repository open. It is self-contained: the agent needs no other instruction from you.')
h('')
h('---')
h('')
h('You are authoring the complete learner resource for **Cambridge IGCSE First Language English, syllabus code 0500** (syllabus for 2024–2026). The learners are Namibian secondary students, English medium, sitting Paper 1 Reading and Paper 2 Directed Writing and Composition in the October/November 2026 series, the first 0500 paper on %s. They may have nothing else to study from.' % FACTS['first_exam'])
h('')
h('## Start here')
h('')
h('Read these before writing anything:')
h('')
h('1. `AGENTS.md` (repo root) — which role brief applies. You are the AUTHOR.')
h('2. `%s/%s` — **the plan. This is your brief.** Read all of it.' % (REL, PLAN))
h('3. `%s/subject-profile.yaml` — the answer parts your marking guidance must name for each card subtype and task type, the conditioned mechanisms, the prohibited patterns.' % REL)
h('4. `%s/curriculum/answer-shapes.json` — how every task is set and marked, with each level table paraphrased band by band.' % REL)
h('5. `standard/v0.2.0-draft/roles/AUTHOR.md` \u2014 written for business subjects. Where it conflicts with this handover, this handover wins for 0500: there are no Namibian-dollar figures or invented businesses here, and its "never say what a paper contains" means never claim frequencies or what examiners do. The syllabus\u2019s own statements about a task (its marks, length, texts and text types) are allowed.')
h('')
h('Everything is derived already. `%s/curriculum/syllabus-facts.json` records where each assessment value came from, with the syllabus page and the verbatim line, and every objective’s syllabus text was verified against its page. Do not re-derive them, do not re-read the syllabus PDF, and do not open any other subject’s workspace.' % REL)
h('')
h('## The job')
h('')
h('**%d topics, %s items (%s flashcards, %s performance tasks), %d original practice texts of %s–%s words, and %s–%s words of notes.** Work through the topics in this order and take the whole subject in one run. Do not stop after a topic to ask what is next. Paper 1 comes first because it is the harder paper: a C needs 44%% of its marks, against 53%% on Paper 2.' % (len(TOPICS), fmt(N['items']), fmt(N['flash']), fmt(N['perf']), N['texts'], fmt(N['tw'][0]), fmt(N['tw'][1]), fmt(N['nw'][0]), fmt(N['nw'][1])))
h('')
h('```')
for t in TOPICS:
    h('  %-4s %s' % (t['id'], t['title']))
h('```')
h('')
h('0500 is examined by **task and skill**, not by topic. Each topic above is one paper task, or one Paper 2 skill. The skills are R1–R5 (reading) and W1–W5 (writing); every slot names the ones it practises.')
h('')
h('For each topic `<T>`, read `%s/topics/<T>/contract.json` (scope, budgets, exclusions) and `%s/topics/<T>/work_order.json` (every slot, every practice text, pre-decided; `work_order.md` is the same thing as a table). Then produce, in `%s/topics/<T>/`:' % (REL, REL, REL))
h('')
h('1. `texts/<text_id>.md` — each practice text the work order lists, **written first**, because its tasks are answered from it. Front matter: `text_id`, `title`, `genre`, `setting`, `written_for`, `words_min`, `words_max`, `original: true`; then the text.')
h('2. `claims/canonical_claim_ledger.json` — every statement the topic teaches: definitions, the conventions of a form, the steps of a technique, why a move works. 3–6 per objective, each mapped to the objectives it serves.')
h('3. `content-units/CU-0500-<sub-topic>.json` — one unit per sub-topic in the work order, prose blocks that cite the claims they rest on.')
h('4. `learning-items/topic_<T>_items.json` — one item per slot, flashcards and performance tasks.')
h('5. Then render the notes and run the checks (commands at the end).')
h('')
h('**Structural exemplar.** `%s/exemplar/` is a small, complete slice of topic 1.3 that passes every check: a ledger, two content units, five flashcards, two tasks answered from a practice text, and the text. Copy its **shape** — the field set of every claim, block and item, `context.text_id`, the text’s front matter, `claims_seen` and `authored_hash`. Do not copy its volume or its content. Do not reuse its text or its items in topic 1.3.' % REL)
h('')
h('Every block and every item needs `claims_seen` (`{claim_id: revision}`), `authored_hash`, and `qa_status: "review_required"`. Compute the hash with:')
h('')
h('```python')
h('import sys, hashlib')
h("sys.path.insert(0, 'standard/v0.2.0-draft/checks')")
h('from yyeni_checks import _artefact_text')
h("x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()")
h('```')
h('')
h('## Every item carries its labels')
h('')
h('Each slot has already decided `subtype` (or `item_type`), `assessment_objectives`, `sub_objectives`, `blooms_level`, `command_word` and `mark_tariff`. **Carry all six onto the item**, plus `context.text_id` where the slot names a text.')
h('')
h('The item\u2019s `item_id` is its slot id. After the run, `standard/v0.2.0-draft/mine/verify_0500.py` compares every item with its slot; a difference not recorded in `authoring_notes.json` is reported as drift.')
h('')
h('- `assessment_objectives` (AO1 reading, AO2 writing) and `sub_objectives` (R1–R5, W1–W5) are what the examination credits.')
h('- `blooms_level` is what the learner is asked to do: Remember, Understand, Apply, Analyse, Evaluate, Create. A different axis, required on every item.')
h('- `command_word` and `mark_tariff` are null on a technique card that models no paper item. Do not invent either.')
h('')
h('If you change a slot’s subtype, change its Bloom level to match the plan’s section 5 and record the change.')
h('')
h('## Rules that come from the syllabus and the corpus')
h('')
h('Breaking one produces material that teaches something the papers do not ask, or asks it the wrong way.')
h('')
h('1. **The syllabus facts, and only those.** You may state what the syllabus states about a task: its marks, its length, its texts, its text types, the skills it tests (plan section 0). Never state that accuracy is marked in Paper 1 — it is not, from 2024. Never claim what examiners reward, report or want: the words "examiner" and "mark scheme" must not appear in learner-facing text (C-10). Teach the technique and why it works.')
h('2. **Command words.** Only four exist: `Identify`, `Explain`, `Give`, `Describe`. Use one where the slot names it. Elsewhere use the task form of the paper item the slot models (summarise on a focus, write in role, analyse the language of two paragraphs). Vary your wording: never copy a stem formula from a paper you may know.')
h('3. **Tariffs.** Use the slot’s. A comprehension item’s marks decide how many points its answer needs.')
h('4. **Misconceptions.** Each MISCON slot names its entry in `curriculum/misconceptions.json`. A MISCON card is a **discrimination**: the error, the correct move, and the test that tells them apart — the `test` field gives it.')
h('5. **Glossary.** `curriculum/glossary.json` settles every term’s sense. Use them exactly.')
h('6. **Scope.** Never mention %s (C-11 scans for them). Adjacent topics in each contract: name in passing, teach there.' % ', '.join('`%s`' % x for x in NOT_IN_ROUTE))
h('7. **Truth.** No unqualified universals (always, never, only, every) unless definitional. Two registered mechanisms must carry their conditions wherever they appear (C-37): a short sentence creates emphasis by contrast with the sentences around it; a formal register is right for an audience and a purpose, not in general.')
h('8. **Self-containment.** A flashcard supplies its own sentence or extract — original, written for the card — and never depends on a practice text or another card. A performance task names its text by `context.text_id`, and its prompt refers to the text by title and paragraph.')
h('9. **Nothing is reproduced.** No Cambridge text, question, task, title, mark-scheme or examiner-report wording, anywhere. Every text, prompt, model answer and piece of guidance is yours.')
h('10. **Filenames are derived, never chosen.** Do not pass `--out` to the renderer and do not rename anything afterwards.')
h('')
h('## Practice texts')
h('')
h('- **Original and the right length.** The work order gives each text’s range, which is the syllabus’s (Text A and B 700–750, Text C 500–650, directed writing 650–750 in total). C-43 checks the file, the declaration and the length.')
h('- **Written for their tasks.** Plan section 6 says what each topic’s texts must make possible. Write the text, then the items; revise the text if an item needs something it lacks.')
h('- **Namibian and southern African settings, with at least one text per topic set elsewhere.** Vary the genre: fiction, memoir, articles, reports, speeches, letters, reviews, as the syllabus asks.')
h('- **Directed-writing texts come as a pair or a single text** inside one file, headed Text A and Text B, and together inside the stated range.')
h('- Age-appropriate, and never modelled on the subject of a Cambridge paper you may know.')
h('')
h('## Answers and marking guidance')
h('')
h('- **Point-marked items:** the answer, one mark per point, the acceptable alternatives, and what is not credited and why.')
h('- **Level-marked tasks:** a model answer written to the top band and inside the stated length. Then guidance that names, table by table, the band descriptors in `answer-shapes.json` the answer meets, in your own words, and one or two sentences on what a middle-band answer to the same task would do instead.')
h('- **Summaries** also list the content points on the focus.')
h('- The guidance must name every part `subject-profile.yaml -> answer_structures` declares for the subtype or task type (C-16).')
h('')
h('## Voice')
h('')
h('Plain, direct explanatory prose in British English. Short paragraphs. Full teaching depth: the notes are the source the flashcards are cut from, the offline study text, and a standalone learning text at once. Every technique is shown working on a short original extract, step by step. No hedging filler and no bullet-point soup where prose teaches better.')
h('')
h('## The work order is a baseline, not a cage')
h('')
h('Where a slot does not fit its objective, change it and record the change in `%s/topics/<T>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong. Where an exposure-required subtype genuinely does not fit, add an entry to the contract’s `subtype_waivers` with a reason of at least twelve words rather than padding the bank.' % REL)
h('')
h('## Finishing each topic')
h('')
h('```bash')
h('python3 standard/v0.2.0-draft/build/render_notes.py %s <T>' % REL)
h('python3 standard/v0.2.0-draft/checks/run_checks.py   %s <T>' % REL)
h('python3 standard/v0.2.0-draft/checks/what_to_fix.py  %s <T>' % REL)
h('```')
h('')
h('`what_to_fix.py` prints only failures, structure first, each with the action that clears it, and exits 0 when clean. Loop on it. Fix every **FAIL**. `not_run` on C-18 (no per-topic AO target, by design), C-35, C-39 and C-41 is expected. Set the contract’s `required_outputs.learning_items` and `required_outputs.content_units` to what you actually produced; a check compares them.')
h('')
h('When all %d topics are clean:' % len(TOPICS))
h('')
h('```bash')
h('python3 standard/v0.2.0-draft/build/publish_subject.py %s' % REL)
h('```')
h('')
h('It publishes only topics whose checks pass, carries each practice text with the tasks that use it, and reports any topic it skipped.')
h('')
h('## Boundaries')
h('')
h('- Do not edit anything under `standard/`, or anything in `%s/curriculum/`.' % REL)
h('- Do not touch any workspace other than `%s`, and do not edit `%s/exemplar/`.' % (REL, REL))
h('- Do not regenerate contracts or work orders; they are the plan you are working to.')
h('- There is no review round. The deterministic suite is the gate.')
h('')
h('## Report back when the subject is finished')
h('')
h('Under 250 words:')
h('')
h('- topics completed, and any not completed with the reason')
h('- totals: claims, content units, items, practice texts, notes words')
h('- the final check line per topic, or a single line if all read `PUBLISH`')
h('- every call you made rather than derived, and every deviation from a work order and why')
h('- anything in the plan that turned out to be wrong')
h('')
open(os.path.join(WS, HAND), 'w').write('\n'.join(H))
print('wrote %s (%d words) and %s (%d words)' % (PLAN, len('\n'.join(P).split()), HAND, len('\n'.join(H).split())))
