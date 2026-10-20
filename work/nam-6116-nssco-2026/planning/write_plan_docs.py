#!/usr/bin/env python3
"""Generate PLAN-6116-nssco-biology.md and HANDOVER-6116-nssco-biology.md.

Both follow PLAN-9702-as-physics.md and HANDOVER-9702-as-physics.md section for section
(TEAM-PLAYBOOK step 4.7). Every figure is read from curriculum/ and the topic work orders;
regenerate rather than edit.
"""
import collections, datetime, json, os, re

WS = 'work/nam-6116-nssco-2026'
J = lambda p: json.load(open(os.path.join(WS, p)))
fw = J('curriculum/assessment-framework.json')
facts = J('curriculum/syllabus-facts.json')
reg = J('curriculum/objective_registry.json')['objectives']
side = J('curriculum/objective_registry.planning.json')
mis = J('curriculum/misconceptions.json')
gl = J('curriculum/glossary.json')
scope = J('curriculum/scope-scan.json')['entries']
expo = J('curriculum/exam-exposure.json')
TODAY = datetime.date.today().strftime('%d %B %Y').lstrip('0')

topics = [o for o in reg if not o['parent_id']]
leaves = [o for o in reg if o['parent_id']]
wos = {t['topic_id']: J('topics/%s/work_order.json' % t['topic_id']) for t in topics}
cons = {t['topic_id']: J('topics/%s/contract.json' % t['topic_id']) for t in topics}

# ---- subject AO total, recomputed the way build/make_work_order.py subject_rollup does
tot = collections.Counter()
for wo in wos.values():
    for a, v in wo['planned_ao_mix_by_marks'].items():
        tot[a] += wo['marks_equivalent_total'] * v['planned_share_percent'] / 100.0
g = sum(tot.values())
share = {a: round(100 * tot[a] / g) for a in ('AO1', 'AO2', 'AO3')}
stated = fw['ao_mark_budget']['stated_qualification_weight_percent']
derived = fw['ao_mark_budget']['final_grade_weight_percent']
n_items = sum(wo['planned_item_count'] for wo in wos.values())
n_perf = sum(len(wo['performance_tasks']) for wo in wos.values())
nb = J('curriculum/notes-budget.json')
w_lo, w_hi = nb['total']['min'], nb['total']['max']
c_lo, c_hi = nb['total']['contract_formula']['min'], nb['total']['contract_formula']['max']
ev_records = J('assessment-evidence/assessment_evidence.json')['records']
mapping_exceptions = J('assessment-evidence/mapping_exceptions.json')
ao_audit = J('curriculum/ao-demand-rollup.json')
groups3 = J('planning/topic3_groups.json')
errata = J('planning/syllabus_errata.json')['errata']
pc = J('curriculum/practical-coverage.json')
in_use = [c for c in fw['command_words'] if c['used_at_level']]
never = fw['command_words_listed_but_never_used']
sub_rows = fw['flashcard_subtype_ao_map']
types = collections.Counter(o['objective_type'] for o in leaves)
slot_sub = collections.Counter(s['subtype'] for wo in wos.values() for s in wo['item_slots'])
fmt = lambda n: format(n, ',')

L = []
A = L.append
A('# Plan — NSSCO Biology 6116 (Namibia, Ordinary Level, Grades 10–11)')
A('')
A('**Plan approved by Lotto, 2026-10-18.** The originally banked 254 images are operator-approved at the file hashes in `planning/operator_approvals.json`; four later item-specific graphs are unapproved. The AO discrepancy and reasoning-coverage limitations remain documented; no percentage-driven additions are required. Full authoring and the Step 6 review copy are complete. The 35 figure holds, scientific verification and actual learner delivery remain open.')
A('')
A('The brief an authoring agent works to. Generated %s from `%s/curriculum/` and the topic work '
  'orders by `planning/write_plan_docs.py`; regenerate rather than edit. The analysis it rests on is '
  '`operations/analysis/6116-nssco-biology-corpus-analysis.md` (with its 2026-10-18 corrections). '
  'Owner: Lotto. This subject is the NSSCO pilot, run under a recorded exception to the pilot rule '
  '(see `STATUS.md`).' % (TODAY, WS))
A('')
A('## 0. What the syllabus says')
A('')
A('Transcribed from `Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_BIOLOGY_SYLLABUS.pdf` (NIED 2018), '
  'every value with its page (`curriculum/syllabus-facts.json`). Printed page = PDF page − 3.')
A('')
A('| AO (build code) | NSSCO | name | stated overall weight | Paper 1 | Paper 2 | Paper 3 |')
A('|---|---|---|---:|---:|---:|---:|')
pm = fw['ao_mark_budget']['per_paper_marks']
for a in fw['assessment_objectives']:
    A('| %s | %s | %s | %d%% | %d marks | %d marks | %d marks |' % (
        a['code'], a['nssco_code'], a['name'], stated[a['code']],
        pm['P1'][a['code']], pm['P2'][a['code']], pm['P3'][a['code']]))
A('')
A('Specification grid, printed p.37 [PDF 40]. AO A carries the printed qualifier "(not more than 24% '
  'recall)"; the syllabus does not say what the 24% is a share of (open issue 1).')
A('')
for p in fw['papers']:
    dur = p.get('duration') or ('%s in the syllabus; %s on the 2025 paper; 2026 unconfirmed (open issue 2)'
                                % (p['duration_syllabus'], p['duration_2025_paper']))
    A('- **Paper %s, %s.** %d marks, %s, %d%% of the qualification.' % (
        p['paper'], p['name'], p['marks'], dur, p['weight_percent']))
A('')
A('Paper 1 is forty four-choice questions on the specific objectives, testing A and B. Paper 2 is '
  'compulsory short-answer and structured questions, mainly A and B. Paper 3 is a written paper '
  'testing familiarity with practical procedures, mainly C, specified by Annexe A criteria (a)–(k) '
  '(printed p.36 [PDF 39], p.41 [PDF 44]). The syllabus glossary (printed p.39–40) defines 18 command '
  'words. The syllabus states %d distinct content limits, one of them on two objectives (section 7).'
  % len(scope))
A('')
A('**Two AO percentages, two bases.** 47/28/25 is **stated**: the grid\'s "Overall Weighting across '
  'all components", equal to the raw marks A 75, B 45, C 40 of 160. 50/30/20 is **derived**: each '
  'paper\'s AO marks weighted by the stated paper weightings 30/50/20, i.e. the share of the final '
  'grade. The AO balance check in this plan uses the stated 47/28/25. Neither is a card quota.')
A('')
A('## 1. What the corpus says')
A('')
A('Six series, 2020–2025: 18 question papers (Paper 1, 2 and 3 each year) and six examiner reports, '
  'each with a Biology 6116 section. **No mark schemes exist** for this syllabus. Paper 2 contributes '
  '480 marks across its six papers and Paper 3 240, together 720 across twelve; Paper 1 is forty '
  'one-mark questions each year with no command word. Some papers are labelled First Proof.')
A('')
A('- **Short answers.** 70% of Paper 2 and 3 parts are 1–2 marks and none exceeds 6. The 5–6 mark '
  'parts are experimental design, multi-step causal explanation and genetic diagrams.')
A('- **Paper 2 is description and naming led** (describe, name, state, identify, explain). **Paper 3 '
  'is calculation and interpretation led** (calculate, explain, describe, suggest).')
A('- **Terminology precision** is the most frequent loss in the examiner reports: wrong or misspelt '
  'structure names, imprecise terms.')
A('- **%d curated, examiner-evidenced misconceptions**, from %d raw statements, each tied to one '
  'objective with a test that separates the two ideas.' % (len(mis['misconceptions']), mis['counts']['raw']))
A('- **Exposure is mapped to objectives by meaning.** %d Paper 2 and 3 parts have direct objective mappings '
  '(`assessment-evidence/assessment_evidence.json`; %d high, %d medium, %d '
  'low confidence; one Miner pass with targeted Codex review/repairs). %d of the %d objectives are named by at least one part. '
  'Exposure calibrates emphasis only; every objective is planned.' % (
    len(ev_records), *[sum(1 for r in ev_records if 'confidence: %s' % c in r['notes'][0]) for c in ('high', 'medium', 'low')],
    len({o for r in ev_records for o in r['objective_ids']}), len(leaves)))
A('All %d original parts remain inventoried. The %d excluded parts are retained in `assessment-evidence/mapping_exceptions.json`: pesticide uptake is unresolved, and the extinction definition is context-only. Neither credits direct objective exposure. The nucleus identification now maps to cell structure, not prepared-slide meiosis.' % (mapping_exceptions['total_paper_parts'], len(mapping_exceptions['exceptions'])))
A('')
A('## 2. Command words and tariffs')
A('')
A('Use only these to open a prompt. The rule is the repository\'s: a word may open a prompt if it '
  'opens at least one part in the papers (`used_at_level = observed_count > 0`, '
  '`standard/v0.2.0-draft/mine/assemble.py:144`; check C-14 forbids the rest). The tariff is the one '
  'the work-order slot names; every slot tariff is the modal tariff the papers set for that word.')
A('')
A('| command word | in the syllabus glossary | parts | modal tariff | tariffs seen | evidence |')
A('|---|---|---:|---:|---|---|')
for c in sorted(in_use, key=lambda c: -c['observed_count']):
    A('| %s | %s | %d | %s | %s | %s |' % (c['word'], 'yes' if c['in_syllabus_table'] else 'no (observed)',
                                         c['observed_count'], c['modal_tariff'],
                                         ', '.join(map(str, c['observed_tariffs'])), c['evidence_strength']))
A('')
A('**Never open a prompt with:** %s. They are glossary words that open no part in 2020–2025. '
  '**Their skills stay in scope**: prediction (B6, Annexe A (j)), comparison (A1–A2) and application '
  '(B throughout) are practised through the objectives that require them, asked with words the papers '
  'use ("suggest what will happen", "distinguish between", "explain").' % ', '.join(never))
A('')
A('## 3. Answer shapes')
A('')
A('**No mark scheme exists, so no official marking rule may be stated.** Marking guidance is written '
  'from the syllabus objectives, the observed tariffs and the examiner evidence, labelled proposed. '
  '`curriculum/answer-shapes.json` records tariff behaviour only. The parts each guidance must name are '
  'in `subject-profile.yaml -> answer_structures`.')
A('')
A('| command, marks | how a proposed answer is built |')
A('|---|---|')
for row in [('define 2', 'the term and its defining feature; where the syllabus gives the definition, its own words'),
            ('state 1, name 1', 'one precise element'),
            ('identify 2, describe 2', 'two separate creditable points, each its own line'),
            ('outline 3, list 3, label 3', 'three points, or three named parts'),
            ('explain 2, suggest 2', 'a cause and its effect, or a reasoned answer to new material: two points'),
            ('discuss 3', 'points on both sides, or a chain of three linked points'),
            ('calculate 2', 'the method or working, then the answer with its unit (or as a ratio)'),
            ('complete 2, plot 5, draw 5', 'table entries with units in the headings; a graph with labelled axes and units, '
             'or a genetic diagram with every line'),
            ('multiple-choice set', 'one mark per question; every distractor is a named error')]:
    A('| %s | %s |' % row)
A('')
A('## 4. Card types, assessment objectives and Bloom levels')
A('')
A('Each slot declares its subtype, AO and Bloom level. The explicit proposed demand audit in `planning/ao_demand_audit.json` governs the AO after the base build; `planning/apply_ao_demand_audit.py` applies it and records the mandatory demand/conditions on each slot. Taught explanation and comparison are A. B requires genuine information processing or reasoning; supplied data and unfamiliar context are not universal prerequisites. C requires an actual C1–C5 practical demand. Command words and subtype names do not decide the AO. Conditional classifications must be checked against each authored prompt.')
A('')
A('| subtype | tests | permitted AOs | Bloom level | slots |')
A('|---|---|---|---|---:|')
for s in sub_rows:
    A('| %s | %s | %s | %s | %d |' % (s['subtype'], s['tests'], ', '.join(s['assessment_objectives']),
                                   s['blooms_level'], slot_sub.get(s['subtype'], 0)))
A('')
A('Performance tasks: multiple_choice_set = Apply; short_answer = Analyse; practical_task = Evaluate.')
A('')
A('**"Discuss" is not one shape.** The syllabus defines Discuss as "a critical account of the points involved" '
  '(printed p.39). In the papers, 6 of the 7 "discuss" parts ask for developed points ("discuss two effects", '
  '"discuss how ... may affect"); one asks for advantages and disadvantages. So an objective that is itself two-sided '
  '("advantages and disadvantages", "arguments for and against") gets an EVAL card weighed to a judgement (Bloom '
  'Evaluate). Every other "discuss" objective gets a CHAIN card worded "discuss": developed points, each with its '
  'consequence, with no for/against frame (Bloom Understand; its APP card carries the application). Bloom levels '
  'follow the thinking the card demands: a CHAIN card reproduces a taught account, so it is Understand, not Analyse.')
A('')
A('Objective types (from `planning/build_registry.py`, verb-first, with %d recorded overrides): %s.' % (
    len(J('planning/objective_overrides.json')['overrides']),
    ', '.join('%s %d' % kv for kv in types.most_common())))
A('')
A('## 5. The topics')
A('')
A('| topic | title | papers | objectives | items | notes words (operative) | contract formula (superseded) |')
A('|---|---|---|---:|---:|---|---|')
for t in topics:
    tid = t['topic_id']; wo = wos[tid]; wb = nb['topics'][tid]; cf = wb['contract_formula']
    A('| %s | %s | 1/2/3 | %d | %d | %s–%s | %s–%s |' % (tid, wo['topic_title'], wo['assessable_objective_count'],
                                              wo['planned_item_count'], fmt(wb['min']), fmt(wb['max']),
                                              fmt(cf['min']), fmt(cf['max'])))
A('')
A('**5 topics, %d objectives, %s items (%s flashcards, %d performance tasks), %s–%s words of notes.**'
  % (len(leaves), fmt(n_items), fmt(n_items - n_perf), n_perf, fmt(w_lo), fmt(w_hi)))
A('')
import glob as _g
ex_units = [json.load(open(f_)) for f_ in sorted(_g.glob(os.path.join(WS, 'exemplar', '3', 'content-units', '*.json')))]
ex_words = sum(u_['word_count'] for u_ in ex_units)
ex_items = len(json.load(open(os.path.join(WS, 'exemplar', '3', 'learning-items', 'topic_3_items.json')))['items'])
vis = J('curriculum/visual-requirements.json')
refs = J('planning/references.json')
deps = J('planning/dependencies.json')['dependencies']
types_all = collections.Counter(o['objective_type'] for o in leaves)
n_pre = sum(1 for o in leaves if o['prerequisite_ids'])
A('**The notes budget is set per syllabus bullet, not per objective** (`curriculum/notes-budget.json`, '
  'model in `planning/notes_budget.py`). The contract formula (`build/make_contract.py:34`, 230–470 words for '
  'every registry objective by exposure class) pays once per member of every split bullet; the revised model gives '
  'each bullet a band for what it asks (recall 60–100 words, description 120–180, explanation or practical '
  '180–280), 30–50 for each extra member of a split bullet, and 50–90 per unit. Total %s–%s words, against %s–%s '
  'from the formula; 9702 Physics has 54,270–77,720. **The budget is a ceiling, not a target**: a unit that '
  'teaches its objectives in fewer words is finished, with a one-line note in `authoring_notes.json` if it falls '
  'below the minimum (C-26 warns, it does not fail); a unit that needs more says why there. The operative figures '
  'are written into every work order and contract by `planning/apply_notes_budget.py` (the formula\'s figure is '
  'kept as `word_budget_superseded`); `planning/check_unit_budgets.py` confirms each content unit declares it. '
  'The representative section, `exemplar/REPRESENTATIVE-SECTION.md`, is 3.3.2 and 3.3.3 in full: %s words of '
  'notes for 10 objectives and %d cards and tasks.' % (fmt(w_lo), fmt(w_hi), fmt(c_lo), fmt(c_hi), fmt(ex_words), ex_items))
A('')
A('Each topic carries content objectives (Papers 1 and 2) and practical objectives (Paper 3), so every '
  'topic gets a multiple-choice set, a structured question and an Alternative-to-Practical task. Topic 3 has %d '
  'objectives and %d items, so it is authored in four groups of whole content units (`planning/topic3_groups.json`): '
  '%s. Each group writes its own unit and item files and stages its claims; the lead merges the claims and checks '
  'the topic as one.' % (wos['3']['assessable_objective_count'], wos['3']['planned_item_count'],
    '; '.join('%s %s (%s)' % (k, g['title'], ', '.join(g['units'])) for k, g in groups3['groups'].items())))
A('')
A('**How the 364 syllabus bullets became %d objectives.** 80 bullets that list separately assessable '
  'members were split into one objective per member (`planning/decomposition.json`), each tied to its verbatim '
  'bullet in `curriculum/objective_registry.planning.json` and linked to its siblings through `related_ids`; lists '
  'that only qualify one skill were left whole, with reasons recorded. **Teaching dependencies**: %d recorded '
  '(`planning/dependencies.json`), written into `prerequisite_ids` on %d objectives; the author of a dependent '
  'unit links to its prerequisite and uses its terms rather than re-teaching it. One crosses topic order: '
  '"chromosome" is defined in 4.4.1 but used from 4.1, so 4.1 defines it on first use and links forward.'
  % (len(leaves), len(deps), n_pre))
A('')
A('### Complete tasks for the demanding skills')
A('')
A('The 4–6 mark parts in 2020–2025 are investigation plans, genetic diagrams, keys, drawings, graphs and multi-step '
  'mechanisms. Each has a complete task, with its marks taken from the papers (evidence per objective in '
  '`planning/objective_overrides.json`):')
A('')
A('| skill | objectives | the task | marks |')
A('|---|---:|---|---:|')
for row in [('Plan an investigation (investigate, design, plan)', types_all['prac_investigation'], 'one coherent plan: changed, measured, kept the same, method, repeats (SYNTH, describe), plus a limitation card', '5'),
            ('Construct and use a dichotomous key', types_all['task_key'], 'construct a key (APP, construct) and use one to identify several organisms (INTERP, identify)', '4 + 4'),
            ('Produce a labelled drawing from a specimen, slide or image', types_all['task_drawing'] + types_all['task_drawing_interp'], 'a complete labelled drawing (APP, draw), plus an explanation where the objective says interpret', '4'),
            ('Monohybrid crosses', types_all['task_genetics'], 'a full genetic diagram with the calculation (CALC, draw), plus why the ratio arises', '5'),
            ('Multi-step mechanisms', types_all['task_mechanism'], 'a short recall card plus a full account in order (MECH)', '4')]:
    A('| %s | %d | %s | %s |' % row)
A('')
A('**Practical objectives: what a written resource can and cannot cover** (`curriculum/practical-coverage.json`). '
  'Of %d practical objectives, %d have a hands-on component ("design and carry out", "make temporary slides", "use '
  'and manipulate a light microscope"). The cards cover what Paper 3 (Alternative to Practical) tests: planning, the '
  'procedure, readings, interpretation and limitations. None of them is evidence that the learner carried the '
  'practical out; the map records the hands-on part as not covered. It needs the school laboratory.' % (
    pc['practical_objectives'], pc['with_hands_on_component']))
A('')
A('### Visual bank: exact figures and delivery still under review')
A('')
bank = J('visuals/manifest.json')['assets']
binds = J('visuals/bindings.json')['bindings']
need_states = collections.Counter(n['status'] for b in binds for n in b['needs'].values())
bind_states = collections.Counter(b['status'] for b in binds)
A('**Preparation, approval and delivery remain separate.** *prepared* means located, stored and mapped; *approved* means scientific accuracy and reuse terms have been checked; *delivered* means shown on a real learner card and tested. The originally banked 254 assets have operator approval at their recorded hashes; newer item-specific graphs do not. No asset has completed scientific verification. Current YYeni connector contracts expose card-side image IDs and an image-attachment action, but image display, learner drawing or image submission and multi-mark guidance have not been tested in the actual interfaces. A located or mapped candidate never fulfils a visual requirement.')
A('')
A('- **Graphs** come from `planning/make_graphs_6116.py`, which reuses the matplotlib approach of `publish/cie-0455-igcse-2026/diagrams/make_diagrams_0455.py`. Each graph has a question variant (no answer marked) and an answer variant. Data are declared in the script as learner readings, a model curve or published figures; published figures are flagged for verification.')
A('- **Micrographs and anatomical images** are authentic, never generated. They are searched for in the local notes and the assessment corpus first, then on Wikimedia Commons (CC0, public domain, CC BY or CC BY-SA only). Local-note and exam images stay reference only: their rights are unknown, and exam figures show which views are examined but are never reproduced. Web originals and their Commons metadata are fetched with the shared harvester (`harvest run`); the log is in `_harvest/logs/`.')
A('- **Variants.** Originals are never edited. `planning/make_visual_variants.py` writes a teaching variant (syllabus terms), a question variant (neutral letters) and an answer variant (letters plus key) from label positions in `planning/visual_labels.json`. Each label records whether its placement is confident or uncertain. Scale bars are kept. A wrong or doubtful scale is flagged, and covered in variants only where it would mislead.')
A('- **Gaps are tracked per need.** A stimulus objective needs a teaching image, a question image, an answer image and an unfamiliar example: a second, different specimen. A model-drawing objective needs a model drawing and its criteria; a photograph does not substitute. Images whose identity or content is in doubt are held and do not count. A text description never completes a visual objective.')
A('')
A('Bank now: %d asset records (%s), %d stored files. Of %d requirement × kind bindings: %s. Of %d individual needs: %s. **Operator-approved image assets: %d. Completed scientific verifications: 0. Requirements met: 0.** Details: `visuals/INDEX.md`; integrity check: `planning/check_visual_bank.py` (integrity only, not approval).' % (
    len(bank), ', '.join('%s %d' % kv for kv in collections.Counter(a['source_kind'] for a in bank).items()),
    sum(len(a['files']) for a in bank), len(binds), ', '.join('%s %d' % kv for kv in bind_states.items()),
    sum(need_states.values()), ', '.join('%s %d' % kv for kv in need_states.items()),
    sum(bool(a.get('operator_approval')) for a in bank)))
A('')
A('Register: %d objectives; visual kinds overlap: %d stimulus images, %d teaching diagrams, %d model drawings and %d graphs. Requirement IDs are stable (`VIS-6116-<objective>`). The authored draft has 35 image-dependent items under `visuals_pending`; six have exact draft graph pairs in `planning/figure_item_candidates.json`, but none is delivered or released.' % (vis['objectives_needing_visuals'], vis['by_kind']['stimulus_image'], vis['by_kind']['teaching_diagram'], vis['by_kind']['model_drawing'], vis['by_kind']['graph']))
A('')
A('### Scientific sources and verification')
A('')
A('The syllabus and the corpus set scope and demand; they do not supply the science. `planning/references.json` lists '
  'the approved references: %s. %s. Every substantive claim carries at least one evidence entry (source, a locator '
  'such as chapter.section, support type); a claim with no suitable reference says so and goes to the verifier as '
  'teacher knowledge. **Verification**: %s, %s; recorded per topic in `topics/<T>/verification.json`. It is kept '
  'outside the claim ledger because check C-24 fails any claim marked verified before review and the standard '
  'defines no post-review state (a framework finding). **Release rule**: %s In the exemplar, %d of %d claims cite an '
  'approved reference; the rest are practical procedures flagged for the verifier. Proposed marking guidance is '
  'never evidence and is never presented as the board\'s.' % (
    '; '.join('%s (%s)' % (x['title'], x['licence']) for x in refs['sources'] if x.get('status') is None),
    'The school\'s NIED-approved textbook is to be named by the operator; the third-party notes in `Revision Notes/` '
    'are not approved factual references, but may be inspected for reference-only visual candidates with rights recorded',
    refs['verification']['who'], refs['verification']['when'], refs['verification']['release_rule'],
    sum(1 for t_ in '34' for c_ in json.load(open(os.path.join(WS, 'exemplar', t_, 'claims', 'canonical_claim_ledger.json')))['claims'] if c_['evidence']),
    sum(len(json.load(open(os.path.join(WS, 'exemplar', t_, 'claims', 'canonical_claim_ledger.json')))['claims']) for t_ in '34')))
A('')
A('## 6. AO balance, in marks')
A('')
exact = collections.Counter()
for wo in wos.values():
    for s_ in wo['item_slots']:
        for a_ in s_['assessment_objectives']:
            exact[a_] += s_['mark_tariff'] / len(s_['assessment_objectives'])
    for p_ in wo['performance_tasks']:
        if p_['item_type'] == 'multiple_choice_set':
            exact['AO1'] += 12 * 0.625; exact['AO2'] += 12 * 0.375
        elif p_['item_type'] == 'short_answer':
            exact['AO1'] += 5; exact['AO2'] += 3
        elif p_['item_type'] == 'practical_task':
            exact['AO3'] += 10
ex_t = sum(exact.values())
gaps = {a_: 100 * exact[a_] / ex_t - stated[a_] for a_ in ('AO1', 'AO2', 'AO3')}
worst = max(gaps, key=lambda a_: abs(gaps[a_]))
A('**The basis is the unrounded aggregate of planned marks**: every slot at its tariff, split across its AOs, plus '
  'each performance task at the marks of the paper part it models, summed over the subject before any rounding.')
A('')
A('| AO | planned (exact) | stated weight | gap | derived final-grade share (reference) |')
A('|---|---:|---:|---:|---:|')
for a_ in ('AO1', 'AO2', 'AO3'):
    A('| %s (%s) | %.2f%% | %d%% | %+.2f | %d%% |' % (a_, ' ABC'[int(a_[-1])], 100 * exact[a_] / ex_t, stated[a_], gaps[a_], derived[a_]))
A('')
A('Largest gap: **%.2f points** (%s), %s the 5-point tolerance, over %s marks-equivalent. `curriculum/ao_coverage.md`, '
  'which the build writes from per-topic rounded figures, reads %d; the exact figure above is the one this plan '
  'answers to. Labels were corrected by the demand audit, without targeting the balance: `top_up` is empty, counts/tariffs are unchanged and the gap is reported without tuning.' % (abs(gaps[worst]), worst, 'inside' if abs(gaps[worst]) <= 5 else 'OUTSIDE', fmt(round(ex_t)),
               max(abs(share[a_] - stated[a_]) for a_ in share)))
A('')
A('**AO approach approved by Lotto; boundary cases retained.** A includes a taught causal account, familiar comparison or rehearsed implications (syllabus PDF p.38, A1–A4). B covers information handling (B1–B4), reasoned explanation, inference, prediction and problem solving (B5–B7). The syllabus does not require supplied data or an unfamiliar context in every B task; distinguish actual reasoning from reproduction of taught accounts. A new name/place alone is insufficient. C requires practical operation/planning, observations/data or method evaluation (PDF p.39, C1–C5). AO and Bloom remain separate axes.')
A('Examples: explain why a plant cell in pure water does not burst = A; infer an isotonic concentration interval from new gain/loss readings = C4 when assessing practical-data interpretation (B3/B4 in a non-practical data task); reason from supplied parental genotypes and sampling uncertainty = provisional B; reproduce a taught 3:1 explanation = A. The genetics WHY slots do not move with the taught WHY/CHAIN accounts. A mitochondria/adaptation APP exemplar is corrected to A because it rehearses a taught relationship.')
A('The audit records %d slots, %d changed AO labels since the original generated work orders, and %d explicitly ambiguous slots. Generic taught EVAL comparisons are A following the operator corpus review. Breastfeeding study explanations and recognition of standard genetic ratios remain explicitly A/B debatable. A later review of the authored prompts decided 41 AO/Bloom/command-word cases, recorded in `planning/post_authoring_label_decisions.json` and `review/POST-AUTHORING-LABEL-DECISIONS-2026-10-19.md`. This corrects labels to demand; it does not establish sufficient reasoning breadth or difficulty. `curriculum/ao-demand-rollup.json` stores rational mark totals. Lotto approved the full plan on 2026-10-18 with the coverage-first approach recorded.' % (len(J('planning/ao_demand_audit.json')['records']), ao_audit['slots_changed'], len(ao_audit['ambiguous_slots'])))
A('')
A('## 7. Misconceptions, glossary and scope')
A('')
A('- **%d examiner-evidenced misconceptions** in `curriculum/misconceptions.json`, each on its '
  'objective with a `discriminating_test`. Every entry has its own MISCON slot (`misconception_entry`). '
  'All %d are authorable: none awaits a teacher. Three flagged on 2026-10-18 were resolved the same day '
  '(MISCON-6116-013 settled by reading the source question; 019 and 038 discriminate without the detail the '
  'evidence lacks); two carry an `authoring_constraint` that the MISCON card must respect.' % (
    len(mis['misconceptions']), len(mis['misconceptions'])))
A('- **%d glossary terms** in `curriculum/glossary.json`, each with its settled sense; %d use the '
  'syllabus\'s own definition word for word.' % (len(gl['terms']), sum(t['provenance'] == 'syllabus' for t in gl['terms'])))
A('- **%d scope patterns** in `curriculum/scope-scan.json`, one per limit the syllabus states, carried '
  'by every contract as `excluded_constructs`; C-11 fails any learner-facing match. Each was tested '
  'against text it must catch and required text it must leave alone:' % len(scope))
for e in scope:
    A('  - %s (syllabus, printed p.%s, %s)' % (e['construct'], e['source']['printed_page'], e['source']['sub_topic']))
A('')
A('## 8. Rules particular to this subject')
A('')
for r in [
 '**Teach in the notes, retrieve on the cards.** Each content unit opens with a Key points block (block type `summary`) that states the essential knowledge visibly, usually as a table. Full explanations live in the notes. A card\'s canonical answer is the shortest complete answer that earns its marks: roughly one short sentence per mark, plus any data. Use a table wherever it removes repetition (one table for the 13 classification groups, not 13 paragraphs). Say a mechanism once, in its own unit, and link to it elsewhere.',
 '**Definitions are the syllabus\'s.** Where the syllabus says "define X as ...", the notes and the DEF card use that definition; the glossary marks which.',
 '**Names exact and spelt correctly.** Structure names (oesophagus, alveoli, xylem, phloem, chloroplast) are given exactly and drilled; imprecise or misspelt terms are the most frequent loss.',
 '**Cell words and solution words.** Turgid, flaccid and plasmolysed describe cells; hypertonic, isotonic and hypotonic describe solutions.',
 '**Data conventions (Annexe B).** Table headings and axes as quantity / unit (time / s), the independent variable on the x-axis, points as crosses or encircled dots, a graph headed dependent against independent.',
 '**Calculations.** Show the working, then the answer with its unit (a ratio has none). Write each step as "a × b = c" or "a ÷ b = c" with c unrounded, because C-32 recomputes it. Magnification: convert to the same unit before dividing; the answer has no unit and is written ×.',
 '**The syllabus misprints one equation** (`planning/syllabus_errata.json`). 3.6.1.3 prints "6HO2"; the correct equation is 6CO2 + 6H2O → C6H12O6 + 6O2 (light, chlorophyll), verified against the Cambridge 0610 syllabus. Use the correct one and do not draw attention to the misprint.',
 '**Accurate at syllabus level.** Simplify, but never into something false: simple diffusion needs no transport protein, but water also crosses through water channel proteins; carrier proteins use energy from respiration directly or indirectly; water potential depends mainly on concentration and also on pressure; water crosses a root through cells and along cell walls.',
 '**Say how sure a cause is.** Where a prompt does not establish a cause, the answer says "one likely reason" or "if ..." and the guidance accepts the other plausible reasons. A control is accepted only if the method in the prompt states it.',
 '**Plasmolysis means the membrane leaves the wall.** Credit requires the cell membrane (with the cytoplasm) pulled away from the cell wall; "flaccid" or "shrunk" alone does not earn it.',
 '**Genetic diagrams in text.** Lines in order: parental phenotypes, parental genotypes, gametes, offspring genotypes, offspring phenotypes and ratio. A grid may be a markdown table.',
 '**Visuals.** No hand-drawn ASCII pictures and no code fences (C-41). Data go in markdown tables. Acquire existing or original assets into `visuals/`, preserving provenance and proposed bindings. Candidate, approved and learner-delivered are separate states. Register requirements in `curriculum/visual-requirements.json`; until the correct variant is reviewed and deliverable, the item names its figure and is held back.',
 '**Practical data are ours.** Readings in a practical task are invented, realistic and consistent with the biology, and introduced as a learner\'s results.',
 '**Namibian context where it does work.** Use local organisms and settings when the situation needs one (pearl millet, quiver trees, a flooded field); do not add place names that carry nothing. Money in N$ where it appears. Teaching of human inherited conditions is done with sensitivity (syllabus note, 4.4.2).',
 '**No board marking claimed.** Guidance is our proposed marking. Never write "examiner" or "mark scheme" in learner-facing text, and never claim what a paper contains (C-10).']:
    A('- ' + r)
A('')
A('## 9. Open issues carried into authoring')
A('')
A('1. **Recall ceiling denominator undefined.** "not more than 24% recall" has no stated denominator. No interpretation is adopted and no item count is derived from it.')
A('2. **Paper 1 duration unconfirmed for 2026.** The syllabus says 45 minutes; the 2025 paper says 1 hour. Needs NIED/DNEA. No learner-facing text states a Paper 1 duration.')
A('3. **Visual preparation and delivery** (section 5): %d objectives have pending visual coverage/review. Assets can be acquired now; shared-build integration and YYeni image display/submission remain separate delivery requirements. Affected items remain held until reviewed and deliverable.' % vis['objectives_with_unresolved_visuals'])
A('4. **Verification needs people.** The operator names the verifying Biology teacher and the school textbook (SRC-SCHOOL). Nothing is released to learners before verification (section 5).')
A('5. **Exposure covers Papers 2 and 3 only.** Paper 1 (30%% of the qualification) is not mapped. There are %d direct mapped records and %d exceptions among %d original parts. Pesticide uptake remains unresolved; extinction is a definition/context-only record, not habitat-destruction evidence. Neither exception counts as direct exposure. The five originally flagged mappings have targeted Codex review, not a claim that the whole map has independent approval.' % (len(ev_records), len(mapping_exceptions['exceptions']), mapping_exceptions['total_paper_parts']))
A('6. **No mark schemes.** All marking guidance is proposed; the step-6 reviewer and the verifier read it as such. The mined question records were repaired on 2026-10-18 (full references, opening command words; `assessment-evidence/GAPS.md`).')
A('7. **Sources.** Available sources are inventoried (`curriculum/source-inventory.json`): the syllabus, 18 question papers and six examiner reports, 2020–2025; no mark scheme exists for any series. The step-1 checkbox records that state rather than "complete".')
A('')
open(os.path.join(WS, 'PLAN-6116-nssco-biology.md'), 'w').write('\n'.join(L))

# ============================================================ HANDOVER
H = []
B = H.append
words_open = ', '.join('`%s`' % c['word'] for c in sorted(in_use, key=lambda c: -c['observed_count']))
B('# Handover prompt — NSSCO Biology 6116')
B('')
B('Paste everything below the line into the authoring harness with this repository open. It is '
  'self-contained: the agent needs no other instruction. (Claude Code: per TEAM-PLAYBOOK step 5, the lead '
  'agent gives each topic sub-agent the brief there and points it at this file.)')
B('')
B('---')
B('')
B('**Plan approved by Lotto, 2026-10-18.** The originally banked 254 images are operator-approved at their recorded hashes; four later item-specific graphs remain unapproved. The authored draft and Step 6 review copy are complete, but 35 figure items remain held. The operator waived the named-teacher checkpoint without verifying claims. This handover does not authorise a commit, push, YYeni write or learner release; retain all scientific, rights, data and delivery holds.')
B('')
B('You are authoring the complete learner resource for **NSSCO Biology, syllabus code 6116** (NIED 2018 '
  'syllabus, Ordinary Level, Grades 10–11). The learners are Namibian secondary students, English medium, '
  'sitting Papers 1, 2 and 3 in the 2026 examination. They may have nothing else to study from.')
B('')
B('## Start here')
B('')
B('Read these before writing anything:')
B('')
B('1. `AGENTS.md` (repo root) — which role brief applies. You are the AUTHOR.')
B('2. `%s/PLAN-6116-nssco-biology.md` — **the plan. This is your brief.** Read all of it.' % WS)
B('3. `%s/subject-profile.yaml` — the answer parts your marking guidance must name for each subtype and task '
  'type, the conditioned mechanisms, the variant register, the prohibited patterns and the depiction rule.' % WS)
B('4. `%s/curriculum/answer-shapes.json` — how each command word behaves in the papers (tariffs only: no '
  'mark scheme exists).' % WS)
B('5. `standard/v0.2.0-draft/roles/AUTHOR.md` — written for business subjects. Where it conflicts with this '
  'handover, this handover wins for 6116: money appears only where a situation involves it, the context '
  'object\'s business fields are null, and "never say what a paper contains" means never claim frequencies or '
  'what examiners do. The syllabus\'s own statements about a paper (marks, question types) are allowed.')
B('')
B('Everything is derived already. `%s/curriculum/syllabus-facts.json` records where each assessment value '
  'came from. Do not re-derive them, do not re-read the syllabus PDF, and do not open any other subject\'s '
  'workspace.' % WS)
B('')
B('## The job')
B('')
B('**5 topics, %d objectives, %s items (%s flashcards, %d performance tasks), %s–%s words of notes** (the budget '
  'in `curriculum/notes-budget.json`, carried in the contracts and work orders as the operative budget; the older formula is retained as `word_budget_superseded`). Work through '
  'the topics in this order and take the whole subject in one run.' % (
    len(leaves), fmt(n_items), fmt(n_items - n_perf), n_perf, fmt(w_lo), fmt(w_hi)))
B('')
B('```')
for t in topics:
    B('  %-4s  %s' % (t['topic_id'], wos[t['topic_id']]['topic_title']))
B('```')
B('')
B('**Topic 3 is authored in four groups** (`%s/planning/topic3_groups.json`), one agent per group, each owning '
  'whole content units: %s. Follow the protocol in that file: own unit files, `learning-items/topic_3_items_<group>.json`, '
  'claims staged in `claims/staging/claims_<group>.json` with ids `CLM-6116-<group>-NNN`; the lead merges the claims '
  'into the one ledger, renders once and checks the whole topic.' % (WS, '; '.join('%s %s' % (k, ', '.join(g['units'])) for k, g in groups3['groups'].items())))
B('')
B('Topic 1 (scientific processes: mathematical requirements, graphs, units, error, experimental technique) '
  'underpins the practical objectives in every later topic. Topic 3 is by far the largest; give it the time '
  'its size needs.')
B('')
B('For each topic `<T>`, read `%s/topics/<T>/contract.json` (scope, budgets, exclusions) and '
  '`%s/topics/<T>/work_order.json` (every slot, pre-decided; `work_order.md` is the same plan as a table). '
  'Then produce, in `%s/topics/<T>/`:' % (WS, WS, WS))
B('')
B('1. `claims/canonical_claim_ledger.json` — every statement the topic teaches, each mapped to the objectives it serves. 2–4 claims per objective.')
B('2. `content-units/CU-6116-<sub-topic>.json` — one unit per content unit in the work order, prose blocks that cite the claims they rest on.')
B('3. `learning-items/topic_<T>_items.json` — one item per slot, flashcards and performance tasks.')
B('4. Then render the notes and run the checks (commands at the end).')
B('')
B('**Notes budget.** Each content unit\'s `word_budget` is the figure its work order gives (`work_order.json`, '
  '`content_units[].word_budget`, taken from `%s/curriculum/notes-budget.json`); C-26 measures the unit against it and '
  '`planning/check_unit_budgets.py` confirms you declared the right one. Ignore `word_budget_superseded`: it is the old '
  'per-objective formula, kept only for the record. **The budget is a ceiling, not a target**: never pad to reach the '
  'minimum; if a unit is complete below it, say so in one line in `authoring_notes.json`, and if it needs more, say '
  'why there. One explanation serves all the members of a split bullet; give each member its own sentence or table '
  'row, not its own essay. Read `%s/exemplar/REPRESENTATIVE-SECTION.md` for the depth and length expected.' % (WS, WS))
B('')
ex_types = sorted({i_['subtype'] or i_['item_type'] for t_ in '34' for i_ in
                   json.load(open(os.path.join(WS, 'exemplar', t_, 'learning-items', 'topic_%s_items.json' % t_)))['items']})
B('**Structural exemplar.** `%s/exemplar/` holds two slices that pass every check (verified in a scratch copy of '
  'this workspace; see its README): 3, the whole of 3.3.2 Osmosis and 3.3.3 Active transport (every slot of ten '
  'objectives, Key points blocks, two complete investigation plans, two "discuss" cards written as developed points), '
  'and 4, part of 4.4.2 monohybrid inheritance (a full genetic diagram). Item and task types shown: %s. Copy their '
  '**shape**: the field set of every claim, block and item, the evidence entries on claims, the null business fields '
  'of `context`, `claims_seen`, `authored_hash`, working written as "a ÷ b = c", concise canonical answers. '
  '**Reuse:** group 3A starts units 3.3.2 and 3.3.3 from the exemplar, which already is those units, and completes '
  'them against the work order (re-stamping anything it changes); topic 4 extends the 4.4.2 slice to the whole unit. '
  'Nowhere else reuse the exemplar\'s scenarios.' % (WS, ', '.join(ex_types)))
B('')
B('Every block and every item needs `claims_seen` (`{claim_id: revision}`), `authored_hash`, and '
  '`qa_status: "review_required"`. Compute the hash with:')
B('')
B('```python')
B('import sys, hashlib')
B("sys.path.insert(0, 'standard/v0.2.0-draft/checks')")
B('from yyeni_checks import _artefact_text')
B("x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()")
B('```')
B('')
B('## Every item carries its labels')
B('')
B('Each slot has already decided `subtype` (or `item_type`), `assessment_objectives`, `blooms_level`, '
  '`command_word` and `mark_tariff`. **Carry all five onto the item.** The item\'s `item_id` is its slot id; a '
  'MISCON slot also names its `misconception_entry`.')
B('')
B('- `assessment_objectives` is what the examination credits (AO1 = NSSCO A, AO2 = B, AO3 = C). '
  '`blooms_level` is what the learner is asked to do. Different axes, both required on every item.')
B('- Read each slot\'s `ao_demand`: the planned demand and conditions are mandatory. B requires actual information handling or reasoning; supplied data or unfamiliarity are not universal prerequisites. A renamed taught case alone is insufficient. C requires a practical demand. Record the new input and inference for conditional B slots in `authoring_notes.json`. If the actual prompt cannot support the planned AO, report it rather than silently changing the demand or label.')
B('- If you change a slot\'s subtype, change its Bloom level to match plan section 4 and record the change.')
B('')
B('## Rules that come from the syllabus and the corpus')
B('')
B('1. **Command words.** Only these open a prompt: %s. Never %s. Command words are lower case in the slot; '
  'capitalise the first word of the prompt as normal English. The skills behind the never-used words (predict, '
  'compare, apply) stay in scope; ask for them with a word the papers use.' % (
    words_open, ', '.join('`%s`' % w for w in never)))
B('2. **Tariffs.** Use the slot\'s. A point-marked answer carries exactly as many creditable points as its '
  'tariff, and its guidance says which.')
B('3. **Answer shape.** Marking guidance names every part `subject-profile.yaml -> answer_structures` declares '
  'for the subtype or task type, using one of its listed words (C-16 matches whole words). All guidance is '
  'proposed: no mark scheme exists for 6116, so never present a marking rule as the board\'s.')
B('4. **Misconceptions.** Each MISCON slot names its entry in `curriculum/misconceptions.json`. A MISCON card '
  'is a **discrimination**: the error, the correct idea, and the test that tells them apart; the entry\'s '
  '`discriminating_test` gives it. Where the entry carries an `authoring_constraint` (MISCON-6116-013: no ciliated '
  'cells as a mechanical barrier; MISCON-6116-019: no week number for embryo and fetus), the card respects it.')
B('5. **Glossary.** `curriculum/glossary.json` settles each confusable term\'s sense; where it quotes the '
  'syllabus\'s definition, use that definition word for word.')
B('6. **Scope.** The contract\'s `excluded_constructs` are the limits the syllabus states, each with the '
  'pattern C-11 scans every learner-facing text for. Any match fails the topic: do not teach, practise or '
  'mention them, not even to say they are not required. Note what is NOT excluded: "water potential" is '
  'required in 3.3.2 (osmosis); "maternal and paternal chromosomes" is the wording of 4.1.')
B('7. **Truth.** No unqualified universals (always, never, only, every) unless definitional, in which case '
  'set `generality` on the claim. The conditioned mechanisms in the subject profile carry their conditions '
  'wherever they appear (C-37). The words "examiner" and "mark scheme" do not appear in learner-facing text (C-10).')
B('8. **Self-containment.** A flashcard supplies its own scenario, data or readings and never depends on '
  'another card. Arithmetic is correct (C-32 recomputes it) and every quantity carries its unit.')
B('9. **Nothing is reproduced.** No question, scenario, indicative answer or examiner-report wording from any '
  'NSSCO paper or report, anywhere. Every scenario, prompt, model answer and piece of guidance is yours. 12 or '
  'more identical words is a defect; 8–11 is allowed only for a standard definition or term.')
B('10. **Filenames are derived, never chosen.** Do not pass `--out` to the renderer and do not rename anything.')
B('11. **Staged visuals, no ASCII pictures.** Code fences fail C-41. Preserve images and generated graphs in '
  'the visual bank with proposed bindings. Keep tables with quantity / unit headings alongside graphs; a table '
  'does not replace an image-reading task. Genetic crosses may also use labelled lines or a markdown grid. '
  'C-41 does not certify bank assets: planning/check_visual_bank.py checks integrity and Biology review checks meaning.')
B('12. **Multiple-choice sets.** `item_type: "multiple_choice_set"`, `mark_tariff` equal to the number of '
  'questions, `command_word` null. Four options A–D on their own lines; the canonical answer gives the key and, '
  'for each question, why the key is right and what error each distractor comes from. Build distractors from '
  'the misconception register first. About five in eight on knowledge, three in eight on handling information.')
B('13. **Practical tasks.** `item_type: "practical_task"`, `assessment_objectives: ["AO3"]`. Describe the '
  'experiment in words, give a learner\'s readings in a markdown table with quantity / unit headings, and number '
  'the parts with their marks: variables, completing or processing the table, a trend or conclusion from the '
  'data, a controlled variable, a source of error with an improvement tied to it. Readings must be realistic and '
  'consistent with the biology (check them).')
B('14. **Structured questions.** `item_type: "short_answer"`, `assessment_objectives: ["AO1", "AO2"]`, about 8 '
  'marks in four or five parts, each part\'s marks shown; `command_word` is the word that opens the first part.')
B('15. **"Discuss" cards.** An EVAL slot (two-sided objectives only) weighs points on both sides to a judgement. A '
  'CHAIN slot worded "discuss" gives developed points, each with its consequence; never force a for/against frame on '
  'it, and an energy cost is not an argument against a process the organism needs.')
B('16. **Complete tasks.** A SYNTH slot is a whole investigation plan (5 marks: changed, measured, kept the same, '
  'method, repeats). A drawing slot (APP, draw, 4 marks) asks for a complete labelled drawing and its guidance names '
  'the drawing criteria. A key slot asks the learner to construct a key, or to use one on several organisms. A '
  'genetics CALC slot (draw, 5 marks) asks for the full genetic diagram. A MECH slot asks for the whole mechanism in '
  'order. Never cut these down to a fragment. Never write as if the learner has carried a practical out; '
  '`curriculum/practical-coverage.json` records the hands-on part as not covered.')
B('17. **Accuracy and certainty.** Plan section 8 lists the corrections the sample review required (membrane '
  'proteins, carrier energy, water potential and pressure, root water routes, plasmolysis). Where a prompt does not '
  'establish a cause, say "one likely reason" or "if ..."; accept a control only if the method states it.')
B('18. **Teach in the notes, retrieve on the cards.** Open every content unit with a Key points block (block type '
  '`summary`) that states the essential knowledge, usually as a table. Keep each canonical answer to the shortest '
  'complete answer that earns its marks (about one short sentence per mark, plus data). Put the fuller explanation '
  'in the notes, say a mechanism once in its own unit and link to it elsewhere, and use a table wherever it removes '
  'repetition.')
B('19. **Visuals.** Read `visuals/INDEX.md`, `visuals/manifest.json`, `visuals/bindings.json`, `planning/figure_item_candidates.json` and `curriculum/visual-requirements.json` for your topic. Existing candidates can be acquired, reviewed and stored before YYeni image delivery is demonstrated. Preserve originals, licences and scale bars; keep teaching, question and answer variants separate. Do not treat a proposed binding as covered or claim image display or drawing submission without interface evidence. Where an objective needs an image, '
  'teaching diagram or model drawing, write the notes and items as planned; an item that cannot be answered without '
  'the image names it ("Fig. VIS-6116-<objective>") and is listed under `visuals_pending` in `authoring_notes.json`. Never '
  'replace a required image with a verbal description and count the objective as covered. No ASCII drawings, no '
  'code fences.')
B('20. **Evidence.** Every substantive claim carries at least one `evidence` entry from `planning/references.json` '
  '(source_id, a locator such as "5.2 Passive Transport", support_type). Where no approved reference covers a claim '
  '(often a practical procedure), leave evidence empty and say so in the claim\'s `notes`, for the verifier. Leave '
  '`verification.status` as "unverified" and `publishable` false: verification is a later human step (C-24).')
B('21. **Dependencies.** Read `prerequisite_ids` on your objectives (from `planning/dependencies.json`). Link to a '
  'prerequisite taught in another unit with a cross_link block and use its glossary terms; do not re-teach it. If '
  'your topic uses a term defined later (e.g. "chromosome" in 4.1), define it briefly on first use and link forward.')
B('22. **Sensitivity.** Human inherited conditions, HIV and AIDS, birth control and drug use are taught '
  'factually and respectfully, without judgement of people (syllabus note, 4.4.2).')
B('')
B('## Voice')
B('')
B('Plain, direct explanatory prose in British English. Short paragraphs. Full teaching depth: the notes are the '
  'source the flashcards are cut from, the offline study text and a standalone learning text at once. Every '
  'process is explained step by step; every calculation is shown working on a small original example. '
  'Use a Namibian setting where the situation needs one (pearl millet in a school garden, a flooded maize field, '
  'quiver trees) with invented names; do not add place names that carry nothing. Money in N$ where it appears.')
B('')
B('## The work order is a baseline, not a cage')
B('')
B('Where a slot does not fit its objective, change it and record the change in '
  '`%s/topics/<T>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that '
  'is wrong. Never add cards to change the AO balance.' % WS)
B('')
B('## Finishing each topic')
B('')
B('```bash')
B('python3 standard/v0.2.0-draft/build/render_notes.py %s <T>' % WS)
B('python3 standard/v0.2.0-draft/checks/run_checks.py   %s <T>' % WS)
B('python3 standard/v0.2.0-draft/checks/what_to_fix.py  %s <T>' % WS)
B('python3 %s/planning/check_unit_budgets.py %s <T>' % (WS, WS))
B('```')
B('')
B('`what_to_fix.py` prints only failures, each with the action that clears it, and exits 0 when clean. Loop on '
  'it. Fix every **FAIL**. Expected and not yours to fix: `not_run` on C-35, C-41 and C-43 (no graphical '
  'stimulus, generated depiction or practice text), and a C-18 warning (the per-topic AO mix by item count is reported, '
  'not targeted). Set the contract\'s `required_outputs.learning_items` and `required_outputs.content_units` to '
  'what you actually produced; C-42 compares them.')
B('')
B('If the same check still fails after three attempts, stop on that topic and report the check, its output and '
  'what you tried. Do not work around it.')
B('')
B('When all 5 topics are clean, run the isolated checker and the learner-text gate, then build the review copy:')
B('')
B('```bash')
B('.venv/bin/python %s/topics/check_release_hygiene.py          # wording gate (lexical only)' % WS)
B('.venv/bin/python %s/topics/build_review_package.py           # review-only copy, held-figure items omitted' % WS)
B('```')
B('')
B('**Do not run `standard/v0.2.0-draft/build/publish_subject.py` on this workspace while any figure item is held.** The standard builder exports every item, '
  'ignores `visuals_pending` and calls its output the copy to upload. `topics/build_review_package.py` wraps it on a filtered copy, writes only to '
  '`%s/review-package/`, lists the omitted item IDs and refuses to run if `publish/nam-6116-nssco-2026` exists. Omitting a held item does not meet its visual '
  'need. The Step 6 review is complete for the review copy; the operator waived the named-teacher checkpoint without verifying the claims. '
  'Release to learners still requires resolving the figure holds, testing actual YYeni image delivery, a release decision and the remaining handover checks. Say in your report that the '
  'package is a review copy and unreleased.' % WS)
B('')
B('## Boundaries')
B('')
B('- Do not edit anything under `standard/` or another subject workspace. Treat `%s/curriculum/`, `%s/planning/` and `%s/exemplar/` as traced inputs: record any new decision at its source, regenerate dependants and run the checks.' % (WS, WS, WS))
B('- Do not regenerate contracts or work orders; they are the plan you are working to.')
B('- Do not commit or push.')
B('')
B('## Report back when the subject is finished')
B('')
B('Under 250 words:')
B('')
B('- topics completed, and any not completed with the reason')
B('- totals: claims, content units, items, notes words')
B('- the final check line per topic, or a single line if all read `PUBLISH`')
B('- every call you made rather than derived, and every deviation from a work order and why')
B('- per topic: items held under `visuals_pending`, claims with no evidence entry, units below their budget minimum')
B('- anything in the plan that turned out to be wrong')
B('')
open(os.path.join(WS, 'HANDOVER-6116-nssco-biology.md'), 'w').write('\n'.join(H))
print('PLAN and HANDOVER written: %d topics, %s items, AO %s vs stated %s'
      % (len(topics), fmt(n_items), '/'.join(str(share[a]) for a in share), '/'.join(str(stated[a]) for a in share)))
