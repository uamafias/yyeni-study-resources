"""Render the plan/handover and item budget from generated curriculum and work orders."""
from pathlib import Path
from collections import Counter
import json,shutil
W=Path(__file__).resolve().parents[1]
def j(p):return json.loads((W/p).read_text())
fw=j('curriculum/assessment-framework.json');reg=j('curriculum/objective_registry.json')['objectives'];rows=[];counts=Counter();totals=Counter()
for p in sorted((W/'topics').glob('*/work_order.json'),key=lambda p:int(p.parent.name)):
 wo=json.loads(p.read_text());c=json.loads(p.with_name('contract.json').read_text());r=dict(topic_id=wo['topic_id'],title=wo['topic_title'],objectives=wo['assessable_objective_count'],leaf_objectives=sum(o['parent_id'] is not None and o['topic_id']==wo['topic_id'] and o['objective_type']!='phys_container' for o in reg),items=wo['planned_item_count'],notes_words=c['depth_constraints']['word_budget'],marks_equivalent=wo['marks_equivalent_total']);rows.append(r)
 totals.update(objectives=r['objectives'],leaf_objectives=r['leaf_objectives'],items=r['items'],min_words=r['notes_words']['min'],max_words=r['notes_words']['max']);counts['flashcards']+=len(wo['item_slots']);counts.update(t['item_type'] for t in wo['performance_tasks'])
budget=dict(budget_id='ITEM-BUDGET-NAM-6118',generated_by='planning/write_plan.py',topics=rows,totals=dict(totals),item_types=dict(counts));(W/'curriculum/item-budget.json').write_text(json.dumps(budget,indent=2,ensure_ascii=False)+'\n')
L=[]
def a(s=''):L.append(s)
a('# Plan — Namibia NSSCO Physics 6118');a('\nDraft for operator approval · generated 31 October 2026. No full-subject authoring, commit or release is authorised by this draft.\n')
a('## 0. What the syllabus says');a('\nThe approved working source is the NIED-listed 2018 edition. The operator accepted it for this 2026 workflow; no separate NIED statement establishing 2026 applicability is claimed. All source figures are transcribed in `curriculum/syllabus-facts.json`.\n')
a('| AO | Name | Raw specification-grid target | P1 raw marks | P2 raw marks | P3 raw marks |\n|---|---|---:|---:|---:|---:|')
for ao in fw['assessment_objectives']:
 a('| '+ao['code']+' | '+ao['name']+' | '+str(ao['qualification_weight_percent'])+'% | '+' | '.join(str(p['ao_raw_marks'][ao['code']]) for p in fw['papers'])+' |')
a('\nP1: 40 four-option MC items, 30% of the grade. P2: 80 structured marks, 90 minutes, 50%. P3: 40 written practical marks, 75 minutes, 20%. The P1 timing conflict remains explicitly waived as non-major: syllabus and 2020/2022–2024 covers say 45 minutes; 2021/2025 covers say one hour. Neither is asserted as the 2026 timing.\n')
a('The practice target uses the approximate raw grid **47/28/25**, consistent with 75/45/40 raw marks. The different **50/30/20** is derived from final component weighting. The syllabus also states **53% skills / 47% knowledge**. These are distinct measures; none is a card quota. The denominator of the 24% recall limit remains unresolved.\n')
a('## 1. What the corpus says');a('\nThe approved Step 3 analysis covers 18 question papers and six Physics report sections from 2020–2025: 622 demand segments and 960 printed marks, with a compensated 2024 MC item excluded from usable exposure. Calculate is the largest single P2 family at 36% of marks. The practical corpus repeatedly tests graph/data work and an eight-mark investigation plan.\n')
a('Checked credit architecture covers **355 demands**, including every primary calculate (99), define (16) and explain (22) demand and all 25 three-mark calculations. The exact **267 outstanding demands** remain listed in `assessment-evidence/GAPS.md`. 2020 P1 contributes demands only, with no difficulty or answer evidence. Keys for 2021–2025 provide 199 usable answers plus one compensation marker. The 2022/2023 First Proof versions remain unconfirmed.\n')
a('## 2. Command words and tariffs');a('\n`curriculum/assessment-framework.json` carries the measured primary-command counts and exact observed tariffs, with listed-but-unobserved glossary rows disabled. Every planned flashcard uses an observed command/tariff combination. A modal tariff is not a universal marking rule. `planning/task-shape-anchors.json` supplies the additional narrow State/Describe/Draw/Derive examples used by the slot policy.\n')
a('| Planned use | Command | Tariff |\n|---|---|---:|\n| Core meaning or one fact | Define / State | 1 |\n| A causal explanation, distinction or linked case | Explain | 2 |\n| A numerical application | Calculate | 2 |\n| One explicitly requested practical action | Describe | 1 |\n| Two specified graph/diagram features | Draw | 2 |\n| Hydrostatic derivation | Derive | 4 |\n| Complete investigation plan, inside a practical task | Plan | 8 |\n')
a('A long conditioned definition is taught fully in notes and in the structured task; a one-mark core-meaning card must not claim to reproduce a two-mark official definition. For calculations, use the located row relevant to the task: units, conversions, intermediate results and rounding receive different credit. No unentered memo row is silently treated as an official rubric.\n')
a('## 3. Answer shapes');a('\n`curriculum/answer-shapes.json` records 156 distinct structured/practical demand architectures. A topic has a 12-question original MC set, an eight-mark structured task, and, where a suitable physical investigation exists, a 16-mark integrated practical task: graph 5, gradient 3, plan 8. This is a practice composite, not a claimed fixed Paper 3 layout. Specific graph and plan architectures come from the located report examples.\n')
a('Every task is bound to objective IDs, a physical context and, for practicals, an original six-point dataset in `curriculum/topic-task-specifications.json`. Every dataset declares itself invented/idealised. All quantities and axis meanings must be checked before authoring. Topic-specific limits explain inverse relationships, echo return time, empirical magnetic data and calculated rather than independently measured energy.\n')
a('The two thin exemplars contain pressure definitions/calculations and practical graph/conclusion/investigation tasks. Both have **40 passed, zero failed, one warning and three not-run checks**. Not-run checks concern graphical stimulus automation, generated chart rendering and reading texts; they are not semantic approval. Claims remain unverified and non-publishable. The standard CLI returns 1 because it compares its decision to `pass` while the suite emits `publish`; this existing mismatch is recorded, not edited.\n')
a('## 4. Card types, assessment objectives and Bloom levels');a('\nDefinitions/features recall knowledge; explanations teach causal understanding; calculations and diagram processing require application. Source-list containers receive one linked comparison/application card, while their members receive focused practice. Only the 23 retained examiner-evidenced conceptual distinctions produce MISCON slots. The six moved candidate-error entries stay as skill practice.\n')
a('A/B/C and Bloom are separate labels. Content cards narrow to A or B as specified; foundational practical topics and integrated practical tasks carry C. Mixed A/B marks on a container or MC set are a planning estimate, not an official per-item allocation. No balancing top-up cards were added. The source-to-registry crosswalk retains existing demand links on source containers when a finer member link is not established; children do not inherit exam frequency by guesswork.\n')
a('## 5. The topics');a('\nThe 335 source bullets become 71 source-family containers and 495 leaf practice outcomes (including one bounded Annex D symbol anchor): **566 non-root registry records**, within 28 teaching topics. Counts below include containers; leaf counts are stated separately. The generated item budget counts an MC set as one learning item.\n')
a('| Topic | Objectives (leaf) | Items | Notes words |\n|---|---:|---:|---:|')
for r in rows:a(f"| {r['topic_id']}. {r['title']} | {r['objectives']} ({r['leaf_objectives']}) | {r['items']} | {r['notes_words']['min']:,}–{r['notes_words']['max']:,} |")
a(f"| **Total** | **{totals['objectives']} ({totals['leaf_objectives']})** | **{totals['items']}** | **{totals['min_words']:,}–{totals['max_words']:,}** |")
a(f"\nThe item mix is {counts['flashcards']} individual cards, {counts['multiple_choice_set']} MC sets (312 one-mark questions), {counts['short_answer']} structured tasks and {counts['practical_task']} integrated practical tasks. The note ranges come from explicit source/member/type depth budgets, not a full chapter per list member. Work orders are the operative counts; containers and source-bullet totals are not volume quotas.\n")
a('## 6. AO balance, in marks');a('\nThe following is the standard generator’s whole-subject estimate. Its independent rounding can make the displayed percentages sum to 99 or 101.\n');coverage=(W/'curriculum/ao_coverage.md').read_text();start=coverage.index('| AO | planned |');end=coverage.index('## By topic');a(coverage[start:end].strip());a('\nThe largest gap is two percentage points, within the required five. The three stated syllabus measures remain distinct. Per-topic differences are intentional; whole-subject balance is the comparison that matters.\n')
a('## 7. Misconceptions, glossary and scope');a('\nThe 23 retained misconception entries, 53 glossary senses and three bounded scope screens travel with the contracts. All 35 depth/condition statements remain binding. Collision definitions are not required; nuclear formulas are limited only in energy-source teaching; diverging lenses are restricted to eye correction. Decay equations remain required. Every contract carries all three screens. Neighbour topics are boundaries for extended teaching, not banned vocabulary.\n')
a('## 8. Rules particular to this subject');a('\n1. Author original stems, data, explanations, diagrams and answers. Never reproduce official assessment wording in learner materials.\n2. Teach each formula with symbol meanings, units, its physical conditions and a worked application. Keep unrounded working; round the final result as requested.\n3. Graph tasks must specify axes, quantities, units, scale and data. Infer the slope’s physical meaning from those axes. Never transplant the known density/stiffness source mistakes.\n4. Drawing outcomes require actual drawing/construction practice. Provide an original accessible diagram or a sufficiently specified construction task, with a labelled solution; text alone must not erase diagram reasoning. No code fences or LaTeX.\n5. Full practical plans must say what changes, what is measured, what is controlled, how data is recorded, and how a conclusion follows. Written preparation accompanies real practical experience.\n6. All demand mappings and registry decomposition remain lead-planner judgements. Independent mapping/content review is scheduled for Step 6; no such review is claimed here.\n7. The operator-approved working syllabus and waived non-major P1 timing issue are not reopened. The First Proof and outstanding-marking caveats remain visible.\n8. Await operator approval of this topic/AO table and the exemplars before Step 5. Approval of this plan is separate from approval to publish or any new push.\n')
(W/'PLAN-6118-nssco-physics.md').write_text('\n'.join(L)+'\n')
H='''# Handover — Namibia NSSCO Physics 6118

## Start here

This is a draft authoring handover, effective only after the operator approves the Step 4 plan. Read AGENTS.md, the active Author role, PLAN-6118-nssco-physics.md, the relevant generated work_order.json and the original structural exemplars. Work only in the assigned topic inside work/nam-6118-nssco-2026/. The plan follows the operator-approved 2018 working syllabus; do not reopen that decision or the waived non-major Paper 1 duration conflict.

## The job

Fill every generated slot, one topic after another in Codex. The complete subject has 28 topics and 666 planned learning items. Each topic needs a canonical claim ledger, the specified content units, one item per flashcard/performance slot and rendered offline notes. Treat topic-task-specifications.json as the concrete context/objective/data binding for performance tasks. Source containers need an overview and their members need targeted teaching; do not repeat a complete chapter for each member.

## Every item carries its labels

Carry item/slot IDs, objective IDs, claim IDs, subtype or performance item_type, A/B/C, Bloom level, primary command and tariff. Keep the axes distinct. Generated cards can be single-AO or A/B as the slot states; integrated practical tasks carry C. Performance tasks contain 12 MC questions, eight structured marks or 16 practical marks. The MC A/B 7.5/4.5 is an estimate across sets: alternate seven/eight A-focused questions rather than inventing a fractional-mark question. Give every question/part an explicit correct answer and complete marking guidance.

## Rules that come from the syllabus and the corpus

Use syllabus-facts.json, the registry and the explicit crosswalk. All 335 source bullets are represented; the larger registry counts include semantic decomposition and containers, not card quotas. Existing demand links were retained at a source container when a finer member link was not justified. Exam exposure does not remove coverage and must not be copied to every member automatically.

Use the 156 located answer-shape entries and the narrowly located supplementary task anchors. All calculate/define/explain primary demands have table checks. Other gaps remain: the 267 entries in assessment-evidence/GAPS.md are not reconstructed official rubrics. A proposed original teaching rubric is a judgement; never describe it as an official row. Source errors in inverse gradients, refraction arithmetic, wire diameter and tariff columns must not enter the authored material.

Use only the observed command/tariff pairs in the framework. A one-mark definition card asks a precise core meaning; teach longer conditions completely in notes and structured practice. A Describe-one-action card is not a complete method. Full planning is practised at eight marks. Distinguish graph construction from drawing a conclusion, and define each physical quantity before using it. All textbook exposition and examples are original. Do not reuse the exemplar scenarios or numerical values in the final bank.

Write each equation in plain text with clear symbols and units. Convert prefixes and squared/cubed units correctly. State assumptions such as fixed temperature, an ideal transformer or no external resultant force where the result needs them. A gradient’s unit and physical meaning come from the actual axes. Do not force a graph through the origin unless data support it. Preserve a negative slope. For an echo, one-way distance uses half the travel time.

Three explicit scope limits and 35 further depth/condition statements apply. Energy-source wording about no nuclide formulas does not remove nuclear decay equations. Diverging lenses are limited to eye correction. Illustrative examples in a source are not automatically mandatory independent card quotas.

## Voice

Plain British English for Namibian secondary learners. Explain with connected paragraphs and concrete examples; introduce terminology before using it. Use N$ only where money is relevant. Give units and working, not just formula lists. Invented data must say that they are practice data. No claims about what examiners always want, no copied official stems, no invented assurance that a source version is final.

## The work order is a baseline, not a cage

Do not silently alter a slot. If its objective, command or task is inappropriate, record the change and reason in authoring_notes.json and raise it with the operator. Do not add cards merely to chase an AO percentage. The planned whole-subject AO comparison uses the raw specification-grid target A47/B28/C25; final grade weighting implies a different 50/30/20. Keep both visible. Do not invent a denominator for the 24% recall statement.

## Finishing each topic

Run the standard render_notes.py, run_checks.py and what_to_fix.py for the topic. Fix real failed checks. The standard run_checks.py CLI currently returns 1 even for a publish decision because it checks for the literal string pass; inspect qa_report.json and failed checks rather than treating that existing wrapper mismatch as a content failure. Do not edit standard/ to hide it. The exemplar reports have zero failed checks; warnings and not-run checks remain explicit. Claims stay unverified and non-publishable until the appropriate operator/review decisions.

## Boundaries

Do not edit standard/, another workspace or the approved curriculum. Do not commit, push or publish during authoring without the required authorisation. The main topics presently contain plans only; the exemplars are thin drafts, not the completed topics. The 2022/2023 First Proof equivalence and the absence of 2020 MC difficulty/answer evidence remain caveats. Independent demand-to-syllabus and content review is scheduled for Step 6, with Lotto and Claude; no independent review is claimed by the current planner.

## Report back when the subject is finished

Report topics completed, counts of claims/units/items/notes words, the mechanical check result, deviations and unresolved limitations. Keep actual publication separate from a check suite’s publish verdict. Preserve operator decisions and unrelated files.
'''
(W/'HANDOVER-6118-nssco-physics.md').write_text(H)
(W/'exemplar/README.md').write_text('''# NSSCO Physics 6118 structural exemplars

Two original thin slices: `11/` demonstrates pressure meaning, units, two- and three-mark calculations and a small MC set; `3/` demonstrates gradient reasoning, evidence-based conclusions, a graph/data task and a complete eight-mark investigation plan. Copy the schema/claim/answer structure, not their content, quantities or item count. Full topic work orders set volume.

Each slice has 40 passed checks, zero failed, one AO-count warning and three not-run checks (C-35/C-41/C-43). The reports are copied beside the exemplars; the isolated `validation-workspace/` retains the complete reproducible fixture. Its item budget is a slice budget, not the subject plan. The standard CLI returns 1 despite a publish decision because of an existing wrapper string comparison; no standard files were changed. Check the JSON decision and failures.

Claims are unverified and non-publishable. Mechanical success is not a scientific/teaching review or operator approval. The renderer’s generic “approved content units” wording does not change the draft QA state.
''')
print('Plan/handover and item budget generated:',dict(totals),dict(counts))
