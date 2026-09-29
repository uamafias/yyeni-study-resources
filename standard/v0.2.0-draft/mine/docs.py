# -*- coding: utf-8 -*-
"""Generate, for ONE syllabus code at a time, the three documents an agent needs.

One subject, one set of documents. An agent pointed at 0450 must never need to
open anything belonging to 0455, and nothing in either is written as a comparison
with the other.

  <workspace>/PLAN-<code>-<slug>.md          the authoring brief
  <workspace>/HANDOVER-<code>-<slug>.md      the prompt to paste into the harness
  operations/analysis/<code>-<slug>-corpus-analysis.md
"""
import json, os, re, glob, collections, datetime, sys
REPO = os.path.expanduser('~/mnt/YYeni Study Resources')
ROOT = os.path.expanduser('~/mine')
TODAY = datetime.date.today().strftime('%d %B %Y')

SUBJECTS = {
 '0450': {'name': 'Business Studies', 'slug': 'igcse-business-studies',
          'ws': 'work/cie-0450-igcse-2026',
          'syllabus': 'Syllabi/Cambridge Curricula/IGCSE Cambridge /Business Studies-2026-syllabus.pdf',
          'papers_note': 'Two written papers of 80 marks each, weighted 50/50.',
          'corpus': {'qp': 84, 'ms': 84, 'er': 17, 'parts': 1169, 'marks': 6660,
                     'errors': 1267}},
 '0455': {'name': 'Economics', 'slug': 'igcse-economics',
          'ws': 'work/cie-0455-igcse-2026',
          'syllabus': 'Syllabi/Cambridge Curricula/IGCSE Cambridge /Economics-2026-syllabus.pdf',
          'papers_note': 'Paper 1 multiple choice, 30 marks, 30%. Paper 2 structured, '
                         '90 marks, 70%.',
          'corpus': {'qp': 84, 'ms': 84, 'er': 17, 'parts': 1002, 'marks': 4580,
                     'errors': 807}},
}

def rd(p): return json.load(open(p, encoding='utf-8'))

def load(code):
    m = SUBJECTS[code]
    ws = os.path.join(REPO, m['ws'])
    d = {'meta': m, 'ws': ws, 'wsn': m['ws']}
    c = lambda f: rd(os.path.join(ws, 'curriculum', f))
    d['fw'] = c('assessment-framework.json')
    d['exp'] = c('exam-exposure.json')
    d['shapes'] = c('answer-shapes.json')[code]
    d['mis'] = c('misconceptions.json')
    d['units'] = c('unit_titles.json')
    d['reg'] = c('objective_registry.json')
    d['excl'] = c('syllabus-exclusions.json')
    d['facts'] = c('syllabus-facts.json')
    d['contracts'] = {}
    d['wos'] = {}
    for f in glob.glob(os.path.join(ws, 'topics', '*', 'contract.json')):
        x = rd(f); d['contracts'][x['topic_id']] = x
        w = os.path.join(os.path.dirname(f), 'work_order.json')
        if os.path.exists(w):
            d['wos'][x['topic_id']] = rd(w)
    return d

def tnum(t): return [int(x) for x in t.split('.')]

# ---------------------------------------------------------------- shared bits
def command_word_table(d):
    """The syllabus table, then what the papers did with it.

    Each row says where its claim comes from: the meaning and the page are the
    syllabus's, the AOs are our judgement, the tariffs and counts are the corpus's.
    """
    L = ['| command word | what the syllabus says it means | from | AOs (judged) '
         '| tariffs seen | times | verdict |',
         '|---|---|---|---|---|---:|---|']
    for c in d['fw']['command_words']:
        if c['verdict'] == 'extraction_noise':
            continue
        t = ', '.join('%sm \u00d7%d' % (k, v)
                      for k, v in c['observed_tariffs'].items()) or '\u2014'
        L.append('| **%s** | %s | %s | %s | %s | %d | %s |'
                 % (c['word'],
                    (c['meaning'] or '\u2014 *no published meaning*')[:96],
                    'p.%s' % c['syllabus_page'] if c['in_syllabus_table']
                    else '**not listed**',
                    '/'.join(c['primary_assessment_objectives']) or '\u2014',
                    t, c['observed_count'], c['verdict'].replace('_', ' ')))
    return L


def shape_lines(d, min_n=40):
    L = []
    for s in d['shapes']['shapes']:
        if (s.get('observed', 0) < min_n) and not s.get('banded'):
            continue
        parts = list(s.get('shape') or [])
        if s.get('per_element') and s.get('elements'):
            parts = ['%s points, each: %s' % (s['elements'], ' + '.join(s['per_element']))]
        for k in ('shape_chain', 'answer_skeleton'):
            if s.get(k):
                parts.append('the answer runs ' + ' → '.join(s[k]))
        if s.get('data_question_skeleton'):
            parts.append('on a data question: ' + ' → '.join(s['data_question_skeleton']))
        L.append('- **%s, %s mark%s** — seen %s times%s'
                 % (s['command'], s['marks'], '' if s['marks'] == 1 else 's',
                    s.get('observed', '?'),
                    ('. ' + '; '.join(parts)) if parts else ''))
        if s.get('banded'):
            top = max(s['bands'], key=lambda b: b.get('band', 0))
            L.append('  - **top band %s** needs all of: %s'
                     % (top['range'], '; '.join(top['requires'])))
            if top.get('top_of_band'):
                L.append('  - **the ceiling of that band** is reserved for: %s'
                         % top['top_of_band'])
            if s.get('options_named_in_stem'):
                L.append('  - the stem names the options to weigh: %s'
                         % ', '.join('%s (×%d)' % kv
                                     for kv in s['options_named_in_stem'].items()))
        for k, lab in (('caps', '*caps*'), ('note', ''), ('verified', '*verified*'),
                       ('guard', '*guard*')):
            if s.get(k):
                L.append('  - %s%s' % (lab + ': ' if lab else '', s[k]))
    return L

def topic_rows(d):
    byobj = {o['objective_id']: o for o in d['exp']['objectives']}
    mis = collections.Counter(e.get('topic_id') for e in d['mis']['entries'])
    rows = []
    for tid, c in d['contracts'].items():
        ids = c['scope']['included_objective_ids']
        marks = sum(byobj.get(i, {}).get('marks_examined', 0) for i in ids)
        core = sum(1 for i in ids
                   if byobj.get(i, {}).get('exposure_class') in ('core', 'frequent'))
        rows.append({'marks': marks, 'tid': tid, 'c': c, 'core': core,
                     'mis': mis.get(tid, 0)})
    rows.sort(key=lambda r: -r['marks'])
    return rows


# ------------------------------------------------------------------ the plan
def plan(code):
    d = load(code); m = d['meta']; A = []; a = A.append
    rows = topic_rows(d)
    tot_marks = sum(r['marks'] for r in rows) or 1
    fw = d['fw']
    live = [c['word'] for c in fw['command_words'] if c.get('use_in_prompts')]
    dead = [c['word'] for c in fw['command_words'] if c['verdict'] == 'listed_not_observed']
    unlisted = [c['word'] for c in fw['command_words'] if c['verdict'] == 'observed_not_listed']

    a('# Authoring plan — Cambridge IGCSE %s %s' % (m['name'], code))
    a('')
    a('| | |')
    a('|---|---|')
    a('| syllabus | Cambridge IGCSE %s **%s**, version 2, first examined 2026 |' % (m['name'], code))
    a('| workspace | `%s` |' % m['ws'])
    a('| learners | Namibian secondary, English medium, sitting within weeks |')
    a('| assessment | %s |' % m['papers_note'])
    a('| evidence | %d question papers, %d mark schemes, %d examiner reports, 2020–2025 |'
      % (m['corpus']['qp'], m['corpus']['ms'], m['corpus']['er']))
    a('| generated | %s |' % TODAY)
    a('')
    a('This plan covers **%s alone**. Nothing in it refers to another syllabus and nothing '
      'in it requires you to open another workspace.' % code)
    a('')
    a('You are authoring **the whole subject in one run**. There is no review round: you '
      'generate, you run the deterministic checks, you fix what they name, you are done. '
      'Aim at a learner who has nothing else, not at a reviewer’s approval.')
    a('')

    a('## 1. Assessment objectives')
    a('')
    a('Transcribed from the syllabus, section 2, page %d. Not inferred, not recalled \u2014 '
      'read off the weighting tables. %s'
      % (d['facts']['ao_weights']['source']['qualification']['page'],
         'This subject has THREE assessment objectives and no Application objective \u2014 '
         'applying analysis to data sits inside AO2. Do not assume a fourth.'
         if len(fw['assessment_objectives']) == 3 else
         'This subject has four assessment objectives.'))
    a('')
    a('| AO | name | weight in the qualification | %s |'
      % ' | '.join('Paper %s' % p['paper'] for p in fw['papers']))
    a('|---|---|---:|%s' % ('---:|' * len(fw['papers'])))
    for ao in fw['assessment_objectives']:
        a('| %s | %s | %d%% | %s |'
          % (ao['code'], ao['name'], ao['qualification_weight_percent'],
             ' | '.join('%d%%' % p['ao_split'].get(ao['code'], 0) for p in fw['papers'])))
    a('')
    a('The per-paper columns come from the table "Assessment objectives as a percentage of '
      'each component" on page %d. They are not derivable from a paper\u2019s name: %s'
      % (d['facts']['ao_weights']['source']['per_component']['page'],
         'Paper 1 is the short-answer paper and still carries %d%% AO4.'
         % fw['papers'][0]['ao_split'].get('AO4', 0)
         if 'AO4' in fw['papers'][0]['ao_split'] else
         'Paper 1 is multiple choice and carries no evaluation at all, while Paper 2 '
         'carries 30%.'))
    a('')
    a('The syllabus states these as a share of **marks**, so every AO figure in this plan is '
      'marks-equivalent. An item count answers a different question and would mislead you.')
    a('')
    for p in fw['papers']:
        a('**Paper %s — %s.** %d marks, %d minutes, %d%% of the qualification. %s%s'
          % (p['paper'], p['name'], p['marks'], p.get('duration_minutes', 0),
             p['weight_percent'], p.get('structure', ''),
             ' Observed tariff mix: %s.' % p['observed_tariff_mix']
             if p.get('observed_tariff_mix') else ''))
        a('')

    a('## 2. Command words: the syllabus table reconciled with the papers')
    a('')
    a('The table below starts from **%s** the complete list the syllabus publishes, '
      'transcribed word for word, with each word\u2019s own stated meaning. Every one is then '
      'checked against %d question parts mined from the papers.'
      % (fw['command_word_table_source'], m['corpus']['parts']))
    a('')
    a('The objectives each word serves are **our judgement, not a transcription**: the '
      'syllabus publishes the words and it publishes the AO weights, but it does not join '
      'them. Everything else in the table is either transcribed or counted.')
    a('')
    A.extend(command_word_table(d))
    a('')
    a('**Use only these in a prompt: %s.**' % ', '.join('`%s`' % w for w in live))
    a('')
    if dead:
        a('*%s* %s listed in the syllabus table but never opens a question in %d mark '
          'schemes. %s'
          % (', '.join(dead), 'is' if len(dead) == 1 else 'are', m['corpus']['ms'],
             'It appears only inside longer stems, as an instruction attached to another '
             'command word.' if code == '0450' else
             'Do not write a prompt with either.'))
        a('')
    if unlisted:
        a('**%s** %s absent from the syllabus table and yet %s %s questions. The paper is the '
          'authority on what is asked, so %s live.'
          % (', '.join(unlisted), 'is' if len(unlisted) == 1 else 'are',
             'opens' if len(unlisted) == 1 else 'open',
             sum(c['observed_count'] for c in fw['command_words']
                 if c['word'] in unlisted),
             'it is' if len(unlisted) == 1 else 'they are'))
        a('')

    a('## 3. The answer shape behind each tariff')
    a('')
    a('Cambridge prints its own answer architecture in the mark scheme. Every shape below was '
      'counted per question block against raw text, and carries the share of that question '
      'population it holds for. Write to the shape.')
    a('')
    A.extend(shape_lines(d))
    a('')
    a('Full detail, including the shapes not listed here: `curriculum/answer-shapes.json`.')
    a('')

    a('## 4. Bloom’s level on every item')
    a('')
    bt = fw['blooms_taxonomy']
    a('%s %s' % (bt['scheme'], bt['why_both']))
    a('')
    a('| level | what the learner is being asked to do | subtypes that carry it |')
    a('|---|---|---|')
    for lv in bt['levels']:
        subs = [k for k, v in bt['by_subtype'].items() if v == lv['level']]
        a('| **%s** | %s | %s |' % (lv['level'], lv['means'],
                                    ', '.join('`%s`' % s for s in subs) or '—'))
    a('')
    a('Every slot in every work order already carries its `blooms_level`, and every topic’s '
      'work order reports its `planned_blooms_mix`. **Copy the level onto the item you '
      'generate.** If you change a slot’s subtype, change its Bloom level to match the '
      'table above and record the change in `authoring_notes.json`.')
    a('')
    a('Performance tasks: %s.'
      % ', '.join('`%s` → %s' % kv for kv in bt['by_performance_task'].items()))
    a('')

    a('## 5. What examiners refuse to credit')
    a('')
    a('From %d error statements across %d Principal Examiner Reports. These are not style '
      'preferences — they are where the marks go.'
      % (m['corpus']['errors'], m['corpus']['er']))
    a('')
    for line in d['shapes']['refusals']:
        a('- %s' % line)
    a('')
    kinds = collections.Counter(e['kind'] for e in d['mis']['entries'])
    a('`curriculum/misconceptions.json` holds **%d examiner-evidenced confusions**, each '
      'attached to the objective it belongs to (%s). Every one earns a `MISCON` card.'
      % (len(d['mis']['entries']),
         ', '.join('%d %s' % (v, k.replace('_', ' ')) for k, v in kinds.most_common())))
    a('')
    a('A `MISCON` card is a **discrimination**, not a definition repeated louder: it states '
      'the boundary between the two ideas and gives the test that tells them apart.')
    a('')

    a('## 6. Scope limits the syllabus itself states')
    a('')
    if d['excl']:
        a('Cambridge names these inside the subject content. Teaching past them spends a '
          'learner’s time on something the paper cannot ask.')
        a('')
        for tid in sorted(d['excl'], key=tnum):
            for x in d['excl'][tid]:
                a('- **%s %s** — %s'
                  % (tid, d['contracts'].get(tid, {}).get('topic_title', ''), x))
    else:
        a('This syllabus states no explicit content exclusions in its subject-content tables.')
    a('')
    if d['excl']:
        a('Every limit is enforced, not just recorded. `%s/curriculum/scope-scan.json` turns each '
          'sentence into the pattern check C-11 scans learner-facing text for, and every contract in '
          'the subject carries all of them: a syllabus limit stated in one topic applies to the whole '
          'subject. The sentence is Cambridge\u2019s; the pattern is our judgement of what teaching '
          'past it would look like.' % m['ws'])
        a('')
    a('Each contract also lists `adjacent_topics`: subject matter a neighbouring topic owns. These '
      'are not scanned. Naming one in passing is fine and often necessary; teaching it in this '
      'topic is scope creep.')
    a('')

    a('## 7. Where the marks are')
    a('')
    unseen = sum(1 for o in d['exp']['objectives'] if o['exposure_class'] == 'unseen')
    a('Topics ordered by marks examined in the corpus. This calibrates how much worked '
      'example and how many variants a topic gets — **never whether it is taught**. Under '
      'RS-05 every objective is taught and practised, including the %d never examined in six '
      'years.' % unseen)
    a('')
    a('| topic | title | objs | core or frequent | items | words | marks in corpus | share | miscon |')
    a('|---|---|---:|---:|---:|---:|---:|---:|---:|')
    for r in rows:
        c = r['c']
        a('| **%s** | %s | %d | %d | %d | %d–%d | %d | %.1f%% | %d |'
          % (r['tid'], c['topic_title'], c['scope']['included_count'], r['core'],
             c['required_outputs']['learning_items'],
             c['depth_constraints']['word_budget']['min'],
             c['depth_constraints']['word_budget']['max'],
             r['marks'], 100.0 * r['marks'] / tot_marks, r['mis']))
    a('')
    a('**Subject total: %d topics, %d items, %s–%s words.**'
      % (len(rows), sum(r['c']['required_outputs']['learning_items'] for r in rows),
         format(sum(r['c']['depth_constraints']['word_budget']['min'] for r in rows), ','),
         format(sum(r['c']['depth_constraints']['word_budget']['max'] for r in rows), ',')))
    a('')

    a('## 8. Files')
    a('')
    a('Read, in this order:')
    a('')
    a('1. `AGENTS.md` at the repo root — routes you to `standard/v0.2.0-draft/roles/AUTHOR.md`.')
    a('2. This plan.')
    a('3. `%s/subject-profile.yaml` — the answer structure your marking guidance must name '
      'for each subtype, the conditioned mechanisms, the prohibited patterns.' % m['ws'])
    a('4. `%s/curriculum/answer-shapes.json`' % m['ws'])
    a('5. `%s/curriculum/misconceptions.json` — filter on your topic id.' % m['ws'])
    a('6. `%s/curriculum/glossary.json` — settled senses. Use them exactly; do not invent '
      'alternatives.' % m['ws'])
    a('7. `%s/topics/<TOPIC>/contract.json` — your scope, budgets and exclusions.' % m['ws'])
    a('8. `%s/topics/<TOPIC>/work_order.json` — every item slot, pre-decided, each with its '
      'subtype, AOs, Bloom level, command word and tariff.' % m['ws'])
    a('')
    a('The work order is a computed baseline, not a cage. Where a slot does not fit its '
      'objective, change it — and record the change in `topics/<TOPIC>/authoring_notes.json` '
      'as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong.')
    a('')
    a('Produce, per topic, in `%s/topics/<TOPIC>/`:' % m['ws'])
    a('')
    a('1. `claims/canonical_claim_ledger.json` — every factual claim the topic teaches, '
      'mapped to the objectives it serves. Roughly 2–4 per assessable objective.')
    a('2. `content-units/CU-%s-<sub-topic>.json` — one per sub-topic, a list of prose blocks '
      'citing claims.' % code)
    a('3. `learning-items/topic_<TOPIC>_items.json` — the cards and performance tasks. Each '
      'item carries `subtype`, `assessment_objectives`, **`blooms_level`**, `command_word`, '
      '`mark_tariff`, `objective_ids`, `claims_seen`, `authored_hash`, `qa_status`.')
    a('4. Then render and check.')
    a('')
    a('**Structural exemplar:** `work/cie-9609-as-2026-2028/topics/5.4/`. Copy its shape, its '
      'field set and its depth. Do not copy its content, command words or tariffs \u2014 those '
      'belong to AS Business 9609 and are wrong for this subject.')
    a('')
    a('**You choose no filenames.** `render_notes.py` derives the notes filename from the '
      'contract’s `topic_title`; `publish_subject.py` names the flashcard file to match. Do '
      'not pass `--out` and do not rename anything afterwards.')
    a('')

    a('## 9. How to write')
    a('')
    a('**Notes carry full teaching depth.** They are three things at once: the source the '
      'flashcards are cut from, the offline study text when the platform is down, and a '
      'standalone learning text. A learner reading offline cannot ask a follow-up, so every '
      'mechanism, formula and worked example is written out.')
    a('')
    a('**Voice.** Plain, direct explanatory prose. Short paragraphs. Worked examples in '
      'Namibian dollars (N$) with Namibian and southern African contexts, plus at least one '
      'non-African example per unit so the examples are not parochial. No hedging filler, no '
      '"it is important to note", no bullet-point soup where prose teaches better.')
    a('')
    a('**Truth and conditions.** No unqualified universals — always, never, every, only — '
      'unless definitional, legal or arithmetic. A mechanism whose conclusion holds only '
      'under conditions carries those conditions **every time it appears**, not just in the '
      'claim. Never claim what examiners reward or what a paper contains. A flashcard is '
      'self-contained and may not rest on a fact its own prompt does not supply.')
    a('')

    a('## 10. Finishing')
    a('')
    a('```bash')
    a('python3 standard/v0.2.0-draft/build/render_notes.py %s <TOPIC>' % m['ws'])
    a('python3 standard/v0.2.0-draft/checks/run_checks.py   %s <TOPIC>' % m['ws'])
    a('python3 standard/v0.2.0-draft/checks/what_to_fix.py  %s <TOPIC>' % m['ws'])
    a('```')
    a('')
    a('Fix every **FAIL** and re-run until there are none. `C-30` warnings about stamps, and '
      '`not_run` on checks whose input does not apply, are fine. When no check fails the '
      'decision reads `PUBLISH`.')
    a('')
    a('Once every topic in the subject is clean:')
    a('')
    a('```bash')
    a('python3 standard/v0.2.0-draft/build/publish_subject.py %s' % m['ws'])
    a('```')
    a('')
    a('Under RS-42 as amended, the deterministic suite is the publication gate. Semantic '
      'review runs on published material and its findings are debt the topic carries visibly.')
    a('')
    a('Do not edit anything under `standard/`. Do not touch another subject’s workspace.')
    a('')

    a('## 11. Known debt in this plan')
    a('')
    cov = os.path.join(m['ws'], 'curriculum', 'ao_coverage.md')
    a('- **AO mix.** `%s` reports where the plan already differs from the syllabus weights '
      'and why. Read it before you start. Padding the bank to close a gap makes the resource '
      'worse, not better.' % cov)
    nl = sum(len(v) for v in d['excl'].values())
    a('- **Scope limits.** %d stated by the syllabus, each enforced by C-11 in all %d contracts. '
      'Beyond those, stay inside your contract\u2019s objective list.' % (nl, len(d['contracts'])))
    a('- **Exposure matching.** %s question parts of %d did not match any objective and were '
      'reported rather than distributed.' % (d['exp']['unmatched_parts'], m['corpus']['parts']))
    if code == '0455':
        a('- **Paper 1 is unmined.** It is multiple choice, so the question-part corpus is '
          'Paper 2 only. The `multiple_choice_set` tasks in the work orders are planned from '
          'the paper’s stated AO split, not from observed questions.')
    a('')
    return '\n'.join(A)


# -------------------------------------------------------------- the analysis
def analysis(code):
    d = load(code); m = d['meta']; A = []; a = A.append
    fw = d['fw']; rows = topic_rows(d)
    cl = collections.Counter(o['exposure_class'] for o in d['exp']['objectives'])
    live = [c for c in fw['command_words'] if c.get('use_in_prompts')]
    dead = [c['word'] for c in fw['command_words'] if c['verdict'] == 'listed_not_observed']
    unlisted = [c for c in fw['command_words'] if c['verdict'] == 'observed_not_listed']
    kinds = collections.Counter(e['kind'] for e in d['mis']['entries'])
    top = sorted(d['exp']['objectives'], key=lambda o: -o['marks_examined'])[0]

    a('# Corpus analysis — Cambridge IGCSE %s %s' % (m['name'], code))
    a('')
    a('What %d published Cambridge documents say about this syllabus, and what changed in '
      'the plan because of it. %s.'
      % (m['corpus']['qp'] + m['corpus']['ms'] + m['corpus']['er'], TODAY))
    a('')
    a('## What was read')
    a('')
    a('| | |')
    a('|---|---:|')
    a('| question papers | %d |' % m['corpus']['qp'])
    a('| mark schemes | %d |' % m['corpus']['ms'])
    a('| Principal Examiner Reports | %d |' % m['corpus']['er'])
    a('| years | 2020–2025 |')
    a('| question parts mined | %s |' % format(m['corpus']['parts'], ','))
    a('| marks accounted for | %s |' % format(m['corpus']['marks'], ','))
    a('| examiner error statements | %s |' % format(m['corpus']['errors'], ','))
    a('')
    a('Plus the syllabus itself: section 2 for the assessment objectives and their weighting '
      'per component, section 3 for the subject content and its stated limits, section 4 for '
      'the paper structure and the command-word table.')
    a('')
    a('Extraction was validated against published paper totals before anything was built on '
      'it. %s'
      % ('73 of 84 Paper 1 and Paper 2 mark schemes reconcile to exactly 80 marks.'
         if code == '0450' else
         'Every Paper 2 mark scheme reconciles to 110 — 30 for Section A plus four Section '
         'B questions of 20, of which a candidate answers three, for 90. That is the paper '
         'structure the syllabus describes, recovered from the arithmetic.'))
    a('')

    a('## 1. The syllabus command-word table, reconciled with the papers')
    a('')
    a('%s' % fw['command_word_table_source'])
    a('')
    A.extend(command_word_table(d))
    a('')
    if dead:
        a('**%s** %s listed and never observed.' % (', '.join(dead),
                                                    'is' if len(dead) == 1 else 'are'))
        if code == '0450':
            a('')
            a('Justify is not absent from the paper — it is absent as a *command word*. It '
              'appears inside 12-mark stems as "Justify your answer", attached to Consider. '
              'A card whose prompt opens with Justify is modelling a question the paper does '
              'not set.')
        a('')
    if unlisted:
        a('**%s** %s the reverse case: absent from the table, present in the papers.'
          % (', '.join(c['word'] for c in unlisted),
             'is' if len(unlisted) == 1 else 'are'))
        for c in unlisted:
            a('')
            a('- **%s** opens %d questions, modal tariff %s marks%s.'
              % (c['word'], c['observed_count'], c['modal_tariff'],
                 ', all on Paper %s' % list(c['papers'])[0][0]
                 if len(set(k[0] for k in c['papers'])) == 1 else ''))
        a('')
        a('The paper is the authority on what is asked, so these are live.')
        a('')
    a('This is the finding that most changes the output. A generator that draws command '
      'words from the syllabus table alone produces prompts for questions that are never '
      'set, and misses ones that are. The framework now carries the verdict, and the '
      'contracts carry the live list.')
    a('')

    a('## 2. Every tariff has a shape, and the mark scheme prints it')
    a('')
    a('%s' % ('Cambridge tags each creditable point in an 0450 mark scheme `[k]`, `[app]`, '
             '`[an]` or `[ev]` — the assessment objective the mark belongs to. The award '
             'instructions above the points say how many of each are available. Between them '
             'they state the answer’s architecture.'
             if code == '0450' else
             'An 0455 mark scheme marks each creditable element `(1)` and states the '
             'composition in its Guidance column. Extended answers carry a printed skeleton '
             '— "Why it might", "Why it might not", "Expected relationship", "Exception" — '
             'which is the shape the answer is expected to take.'))
    a('')
    A.extend(shape_lines(d, min_n=60))
    a('')

    a('## 3. Examiners name the same failures every year')
    a('')
    a('%s error statements were extracted from %d reports and clustered. A fault named in '
      'one report is noise; one named in every report is systemic.'
      % (format(m['corpus']['errors'], ','), m['corpus']['er']))
    a('')
    for line in d['shapes']['refusals']:
        a('- %s' % line)
    a('')

    a('## 4. %d nameable misconceptions' % len(d['mis']['entries']))
    a('')
    a('Clustering produced **%d examiner-evidenced confusions**, each a specific pair of '
      'ideas, each attached to the syllabus objective it belongs to.'
      % len(d['mis']['entries']))
    a('')
    sample = [e for e in d['mis']['entries'] if e.get('topic_id')][:14]
    a('> ' + ' · '.join('%s ↔ %s' % (e['a'], e['b']) for e in sample))
    a('')
    a('| kind of error | count | what fixes it |')
    a('|---|---:|---|')
    FIX = {'adjacent_concept': 'a card that states the boundary and the test',
           'near_neighbour_term': 'a card that names the one word that differs and why it matters',
           'wrong_angle_same_concept': 'a card that asks the same concept from both angles',
           'cause_vs_consequence': 'a card that runs the chain in one direction and names it',
           'opposite_direction': 'a card that runs the mechanism both ways'}
    for k, v in kinds.most_common():
        a('| %s | %d | %s |' % (k.replace('_', ' '), v, FIX.get(k, '')))
    a('')
    wrong = kinds.get('wrong_angle_same_concept', 0) + kinds.get('cause_vs_consequence', 0)
    a('%d of the %d are not term confusions at all but **answering the adjacent question** — '
      'a cause given where a consequence was asked for, a function where a role was asked '
      'for, how where why was asked. That reframes what a misconception card is: not a '
      'definition repeated louder, but a discrimination with a test.'
      % (wrong, len(d['mis']['entries'])))
    a('')

    a('## 5. Exposure, measured')
    a('')
    a('Every question part was matched to the objective whose syllabus wording it shares the '
      'most distinctive vocabulary with. %s of %s failed to match and are reported rather '
      'than distributed.' % (d['exp']['unmatched_parts'], format(m['corpus']['parts'], ',')))
    a('')
    a('| exposure class | objectives |')
    a('|---|---:|')
    for k in ('core', 'frequent', 'occasional', 'rare', 'unseen'):
        a('| %s | %d |' % ({'core': 'core (10+ series)', 'frequent': 'frequent (6–9)',
                            'occasional': 'occasional (2–5)', 'rare': 'rare (1)',
                            'unseen': '**never examined**'}[k], cl.get(k, 0)))
    a('')
    a('The most heavily examined objective is *%s* — %d questions, %d marks, %d of the '
      'series in the corpus.'
      % (top['syllabus_text'], top['times_examined'], top['marks_examined'],
         top['series_spread']))
    a('')
    a('%d objectives have never been examined in six years. Under RS-05 they are still '
      'taught and still practised; exposure decides how much worked example a topic gets, '
      'never whether it is covered.' % cl.get('unseen', 0))
    a('')

    a('## 6. What now exists')
    a('')
    a('| | |')
    a('|---|---:|')
    a('| assessable objectives | %d |'
      % sum(1 for o in d['reg']['objectives'] if o.get('parent_id')))
    a('| topics with a contract | %d |' % len(d['contracts']))
    a('| work orders | %d |' % len(d['wos']))
    a('| item slots | %d |' % sum(len(w['item_slots']) for w in d['wos'].values()))
    a('| performance tasks | %d |' % sum(len(w['performance_tasks']) for w in d['wos'].values()))
    a('| planned items in total | %d |'
      % sum(c['required_outputs']['learning_items'] for c in d['contracts'].values()))
    a('| planned note words | %s–%s |'
      % (format(sum(c['depth_constraints']['word_budget']['min']
                    for c in d['contracts'].values()), ','),
         format(sum(c['depth_constraints']['word_budget']['max']
                    for c in d['contracts'].values()), ',')))
    a('| examiner-evidenced misconceptions | %d |' % len(d['mis']['entries']))
    a('| glossary terms seeded | %d |'
      % len(rd(os.path.join(d['ws'], 'curriculum', 'glossary.json'))['terms']))
    a('')
    bl = collections.Counter()
    for w in d['wos'].values():
        for s in w['item_slots'] + w['performance_tasks']:
            bl[s.get('blooms_level')] += 1
    tb = sum(bl.values()) or 1
    a('Bloom’s spread across the whole plan:')
    a('')
    a('| level | items | share |')
    a('|---|---:|---:|')
    for lv in fw['blooms_taxonomy']['levels']:
        a('| %s | %d | %d%% |' % (lv['level'], bl.get(lv['level'], 0),
                                  round(100.0 * bl.get(lv['level'], 0) / tb)))
    a('')

    a('## 7. Debt, stated plainly')
    a('')
    cov = rd(os.path.join(d['ws'], 'curriculum', 'assessment-framework.json'))
    nl = sum(len(v) for v in d['excl'].values())
    a('- **AO mix.** See `%s/curriculum/ao_coverage.md`.' % m['ws'])
    fixed = (' Two work-order slots (3.3 PED, 6.3 exchange rates) had planned a calculation the syllabus '
             'rules out; both are corrected.' if code == '0450' else '')
    a('- **Scope limits.** The %d the syllabus states are enforced by C-11 in every contract. Until 29 '
      'September 2026 they were recorded as sentences, which C-11 could not match.%s No limit comes from '
      'an A Level boundary: a planner adds constructs belonging to the next qualification up.' % (nl, fixed))
    if code == '0455':
        a('- **Paper 1 is unmined.** Multiple choice, so the question-part corpus is Paper 2 '
          'only. MCQ practice is planned from the paper’s stated AO split.')
    a('- **Semantic review is debt, not a gate.** Under RS-42 as amended the deterministic '
      'suite gates publication; semantic findings are carried visibly on published material.')
    a('')
    a('## Derivation policy')
    a('')
    a('Official assessment material is `mine_do_not_reproduce`. What was extracted is '
      'structure, frequency and examiner-stated failure. No question wording and no '
      'mark-scheme wording reaches learner-facing output; the verification suite checks this '
      'directly against sampled stems. Mine the demand, write the answer yourself.')
    a('')
    return '\n'.join(A)


# --------------------------------------------------------- the handover prompt
def handover(code):
    d = load(code); m = d['meta']; fw = d['fw']
    rows = topic_rows(d)
    live = [c['word'] for c in fw['command_words'] if c.get('use_in_prompts')]
    dead = [c['word'] for c in fw['command_words'] if c['verdict'] == 'listed_not_observed']
    items = sum(c['required_outputs']['learning_items'] for c in d['contracts'].values())
    wmin = sum(c['depth_constraints']['word_budget']['min'] for c in d['contracts'].values())
    wmax = sum(c['depth_constraints']['word_budget']['max'] for c in d['contracts'].values())
    plan_name = 'PLAN-%s-%s.md' % (code, m['slug'])
    topics = sorted(d['contracts'], key=tnum)
    A = []; a = A.append

    a('# Handover prompt — Cambridge IGCSE %s %s' % (m['name'], code))
    a('')
    a('Paste everything below the line into Hermes Agent or OpenCode with this repository '
      'open. It is self-contained: the agent needs no other instruction from you.')
    a('')
    a('---')
    a('')
    a('You are authoring the complete learner resource for **Cambridge IGCSE %s, syllabus '
      'code %s**, first examined 2026. The learners are Namibian secondary students, English '
      'medium, sitting this exam within weeks. They may have nothing else to study from.'
      % (m['name'], code))
    a('')
    a('## Start here')
    a('')
    a('Read these four files before writing anything:')
    a('')
    a('1. `AGENTS.md` (repo root) — tells you which role brief applies. You are the AUTHOR.')
    a('2. `%s/%s` — **the plan. This is your brief.** Read all of it.' % (m['ws'], plan_name))
    a('3. `%s/subject-profile.yaml` — the answer structure your marking guidance must name '
      'for each card subtype, the conditioned mechanisms, the prohibited patterns.' % m['ws'])
    a('4. `standard/v0.2.0-draft/roles/AUTHOR.md`')
    a('')
    a('Everything you need is derived already. `%s/curriculum/syllabus-facts.json` records '
      'where each assessment value came from \u2014 the syllabus page and the verbatim line '
      'that states it \u2014 and a check re-opens the PDF to prove every quote is real. So the '
      'assessment objectives, the AO weights, the paper structures and the command words in '
      'the plan are the document\u2019s, not a summary of it. Do not re-derive them, do not '
      're-read the syllabus PDF, and do not open any other subject\u2019s workspace.' % m['ws'])
    a('')

    a('## The job')
    a('')
    a('**%d topics, %d items, %s–%s words of notes.** Work through the topics in the order '
      'listed below and take the whole subject in one run. Do not stop after each topic to '
      'ask what is next.' % (len(topics), items, format(wmin, ','), format(wmax, ',')))
    a('')
    a('```')
    for i in range(0, len(topics), 10):
        a('  ' + '  '.join(topics[i:i + 10]))
    a('```')
    a('')
    a('For each topic `<T>`, read `%s/topics/<T>/contract.json` (scope, budgets, exclusions) '
      'and `%s/topics/<T>/work_order.json` (every item slot, pre-decided), then produce four '
      'things in `%s/topics/<T>/`:' % (m['ws'], m['ws'], m['ws']))
    a('')
    a('1. `claims/canonical_claim_ledger.json` — every factual claim the topic teaches, each '
      'mapped to the objectives it serves. Roughly 2–4 claims per assessable objective.')
    a('2. `content-units/CU-%s-<sub-topic>.json` — one unit per sub-topic, a list of prose '
      'blocks, each citing the claims it rests on.' % code)
    a('3. `learning-items/topic_<T>_items.json` — the flashcards and performance tasks, one '
      'per slot in the work order.')
    a('4. Then render the notes and run the checks (commands at the end).')
    a('')
    a('**Structural exemplar.** Neither of this subject\u2019s topics is written yet, so copy '
      'the exact metadata field set from `work/cie-9609-as-2026-2028/topics/5.4/` \u2014 its '
      'claim ledger, its four content units and its item file. That is a different '
      'qualification: take its SHAPE and its depth, never its content, its command words or '
      'its tariffs, which belong to AS Business 9609 and are wrong here.')
    a('')
    a('Every block and every item needs `claims_seen` (`{claim_id: revision}`), '
      '`authored_hash`, and `qa_status: "review_required"`. Compute the hash with:')
    a('')
    a('```python')
    a('import sys, hashlib')
    a("sys.path.insert(0, 'standard/v0.2.0-draft/checks')")
    a('from yyeni_checks import _artefact_text')
    a("x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()")
    a('```')
    a('')

    a('## Every item carries both labels')
    a('')
    a('The work order has already decided each slot’s `subtype`, `assessment_objectives`, '
      '`blooms_level`, `command_word` and `mark_tariff`. **Carry all five onto the item you '
      'generate.**')
    a('')
    a('- `assessment_objectives` is what the examination credits.')
    a('- `blooms_level` is what the learner is being asked to do: %s.'
      % ', '.join(l['level'] for l in fw['blooms_taxonomy']['levels']))
    a('')
    a('They are different axes and both are required on every item. If you change a '
      'slot’s subtype, change its Bloom level to match the table in section 4 of the plan, '
      'and record the change.')
    a('')

    a('## Rules that come from the corpus, not from a style guide')
    a('')
    a('These were measured across %d mark schemes and %d examiner reports for this syllabus. '
      'Breaking one produces a card that models a question the paper does not set.'
      % (m['corpus']['ms'], m['corpus']['er']))
    a('')
    a('1. **Command words.** Use only: %s. Never use %s \u2014 %s listed in the syllabus '
      'command-word table but never open%s a question in %d mark schemes.%s'
      % (', '.join('`%s`' % w for w in live),
         ', '.join('`%s`' % w for w in dead) or 'any word outside that list',
         'it is' if len(dead) == 1 else 'they are',
         's' if len(dead) == 1 else '',
         m['corpus']['ms'],
         ' Justify appears only inside longer stems, attached to another command word; a '
         'prompt that opens with it models a question the paper does not set.'
         if 'Justify' in dead else ''))
    a('2. **Tariffs.** A command word’s tariff is not free. Use the modal tariff in the '
      'plan’s section 2 table, or one of that word’s observed tariffs. Never invent one.')
    a('3. **Answer shape.** Section 3 of the plan gives the shape behind each tariff, with '
      'the share of real questions it holds for. Write to the shape. The marking guidance on '
      'each card must name every part of its subtype’s declared structure in '
      '`subject-profile.yaml`.')
    a('4. **Misconceptions.** `%s/curriculum/misconceptions.json`, filtered on your topic id, '
      'lists confusions examiners record learners actually making. Each earns a `MISCON` '
      'card, and a MISCON card is a **discrimination** — the boundary between the two ideas '
      'and the test that tells them apart — not the correct definition repeated.' % m['ws'])
    a('5. **Glossary.** `%s/curriculum/glossary.json` settles senses. Use them exactly and do '
      'not invent alternatives. Where a sense is still `null`, settle it once and use that '
      'everywhere in the subject.' % m['ws'])
    a('6. **Scope.** The contract\u2019s `excluded_constructs` are the limits the syllabus states '
      'anywhere in this subject, each with the pattern C-11 scans every learner-facing text for. '
      'Any match fails the topic, so do not teach, practise or mention them, not even to say they '
      'are not required. `adjacent_topics` are not scanned: name one in passing if you must, '
      'teach it in its own topic.')
    a('7. **Truth.** No unqualified universals — always, never, every, only — unless '
      'definitional, legal or arithmetic. A mechanism whose conclusion holds only under '
      'conditions carries those conditions every time it appears, not just once in the '
      'claim. What an independent third party will do is a likelihood with a reason, never a '
      'certainty. Never claim what examiners reward or what a paper contains.')
    a('8. **Self-containment.** A flashcard may not depend on another card, and its answer '
      'may not rest on a fact its own prompt does not supply. Arithmetic is correct, every '
      'figure carries its unit or currency, and a quantity is named in the units it is '
      'measured in.')
    a('9. **Nothing is reproduced.** You may not have Cambridge question or mark-scheme '
      'wording in front of you, and you must not reproduce any. Write every prompt and every '
      'answer yourself.')
    a('10. **Filenames are derived, never chosen.** Do not pass `--out` to the renderer and '
      'do not rename anything afterwards.')
    a('')

    a('## Voice')
    a('')
    a('Plain, direct explanatory prose. Short paragraphs. Full teaching depth: the notes are '
      'the source the flashcards are cut from, the offline study text, and a standalone '
      'learning text at once, so every mechanism, formula and worked example is written out. '
      'Worked examples in Namibian dollars (N$) with Namibian and southern African contexts, '
      'and at least one non-African example per unit. No hedging filler, no "it is important '
      'to note", no bullet-point soup where prose teaches better.')
    a('')

    a('## The work order is a baseline, not a cage')
    a('')
    a('Where a slot does not fit its objective, change it — and record the change in '
      '`%s/topics/<T>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is '
      'the only kind that is wrong. Where an exposure class demands a subtype that genuinely '
      'does not fit, add an entry to the contract’s `subtype_waivers` with a written reason '
      'of at least twelve words rather than padding the bank with a card that teaches '
      'nothing.' % m['ws'])
    a('')

    a('## Finishing each topic')
    a('')
    a('```bash')
    a('python3 standard/v0.2.0-draft/build/render_notes.py %s <T>' % m['ws'])
    a('python3 standard/v0.2.0-draft/checks/run_checks.py   %s <T>' % m['ws'])
    a('python3 standard/v0.2.0-draft/checks/what_to_fix.py  %s <T>' % m['ws'])
    a('```')
    a('')
    a('`what_to_fix.py` prints only failures, structure first, each with the action that '
      'clears it, and exits 0 when clean. Loop on it. Fix every **FAIL**; `C-30` stamp '
      'warnings and `not_run` on checks whose input does not apply are fine.')
    a('')
    a('Set the contract’s `required_outputs.learning_items` and `required_outputs.'
      'content_units` to what you actually produced — a check compares them.')
    a('')
    a('When all %d topics are clean:' % len(topics))
    a('')
    a('```bash')
    a('python3 standard/v0.2.0-draft/build/publish_subject.py %s' % m['ws'])
    a('```')
    a('')
    a('It publishes only topics whose checks pass and reports any it skipped.')
    a('')

    a('## Boundaries')
    a('')
    a('- Do not edit anything under `standard/`.')
    a('- Do not touch any workspace other than `%s`.' % m['ws'])
    a('- Do not regenerate contracts or work orders; they are the plan you are working to.')
    a('- There is no review round. The deterministic suite is the gate.')
    a('')

    a('## Report back when the subject is finished')
    a('')
    a('Under 250 words:')
    a('')
    a('- topics completed, and any not completed with the reason')
    a('- totals: claims, content units, items, notes words')
    a('- the final check line per topic, or a single line if all read `PUBLISH`')
    a('- every scope call you had to make rather than derive — where the syllabus wording '
      'was ambiguous, or where you deviated from a work order and why')
    a('- anything in the plan that turned out to be wrong')
    a('')
    return '\n'.join(A)


# ------------------------------------------------------------------------ main
def main(codes):
    for code in codes:
        m = SUBJECTS[code]
        ws = os.path.join(REPO, m['ws'])
        out = []
        p = os.path.join(ws, 'PLAN-%s-%s.md' % (code, m['slug']))
        open(p, 'w', encoding='utf-8').write(plan(code)); out.append(p)
        p = os.path.join(ws, 'HANDOVER-%s-%s.md' % (code, m['slug']))
        open(p, 'w', encoding='utf-8').write(handover(code)); out.append(p)
        ad = os.path.join(REPO, 'operations', 'analysis')
        os.makedirs(ad, exist_ok=True)
        p = os.path.join(ad, '%s-%s-corpus-analysis.md' % (code, m['slug']))
        open(p, 'w', encoding='utf-8').write(analysis(code)); out.append(p)
        for x in out:
            print('%7d  %s' % (os.path.getsize(x), x.replace(REPO + '/', '')))


if __name__ == '__main__':
    main(sys.argv[1:] or ['0450', '0455'])
