"""Render reviewer-facing plan and author handover from validated counts."""
import json
from pathlib import Path
WS=Path(__file__).resolve().parents[1]
def read(p):return json.loads((WS/p).read_text())
v=read('planning/plan-validation.json');tot=v['totals']
table='\n'.join(f"| {r['topic_id']} {r['title']} | {r['objectives']} | {r['items']} | {r['notes_min']:,}–{r['notes_max']:,} |" for r in v['topic_table'])
ao='\n'.join(f"| {a} | {v['ao_targets_percent'][a]:g}% | {v['ao_share_percent'][a]:.2f}% | {v['ao_share_percent'][a]-v['ao_targets_percent'][a]:+.2f} |" for a in ('A','B','C'))
ownership=json.loads((WS/'curriculum/topic-ownership.json').read_text())
ownership_table='| Construct | Owner | Cross-links | Teaching rule |\n|---|---|---|---|\n'+'\n'.join(f"| {r['construct']} | {r['owner']} | {r['cross_links']} | {r['rule']} |" for r in ownership['entries'])
topics='\n'.join(f"{r['topic_id']:5} {r['title']}" for r in v['topic_table'])
plan=f'''# Plan — 6145 NSSCO Economics

7 November 2026 · Owner Jeremy · Codex · **Approved by Jeremy, 7 November 2026 · Awaiting human commit**.

## 0. What the syllabus says

NIED Economics Ordinary Level 6145, Grades 10–11, published 2018, implementation 2019, first examination 2020. Jeremy checked the assessment tables against the PDF. Every source quotation is in `curriculum/syllabus-facts.json`; printed pages 13–15 correspond to PDF 17–19.

Both papers are compulsory and have 80 attempted marks, each weighted 50%. Paper 1 lasts 2 hours 30 minutes: 40 marks of short answers under A and 40 marks of contextual interpretation/evaluation under B/C. Paper 2 lasts 2 hours: a compulsory 20-mark question and three chosen 20-mark questions from five. A Paper 2 offers 120 marks, not 120 attempted marks.

The paper AO splits are A/B/C = 50/16/34 and 28/35/37. Overall targets are **calculated** 39/25.5/35.5; the syllabus does not print an independent overall row. Keep A/B/C, not generic AO1/AO2/AO3. The generator's legacy key says stated_qualification_weight_percent; its provenance explicitly records the calculation.

The complete scope is nine themes and 28 topics. This registry retains all 96 specific-objective bullets, adds explicit members for 32 lists and has **197 assessable objectives plus 28 topic containers**. Lists and their relationships are both taught. `planning/decomposition-map.json` records every expansion. Tax, integration and national-income method members are additionally supported by corpus usage. Do not infer that a source bullet's frequency belongs to every member.

## 1. What the corpus says

The approved analysis is `operations/analysis/6145-nssco-economics-corpus-analysis.md`. Ten QPs across 2020–2024 produce 271 question-part records and 1,000 offered marks. Six Economics report sections cover 2020–2025. The evidence includes 213 retained error comments and 32 curated conceptual confusions. All QP totals reconcile; the standard C-39 recomputes exposure across the expanded 197-reference branch.

No standalone schemes or 2025 QPs are held. Suggested answers/guidance in reports support selected shapes, not a fictitious full mark-scheme transcription. First Proof filenames remain provisional. `assessment-evidence/GAPS.md` and `source-discrepancies.json` remain part of the authoring packet. The 2025 report supplements errors and guidance without contributing invented QP frequencies.

## 2. Command words and tariffs

The framework records all 13 syllabus-table words and observed additional forms. Slot openers are **Define, Identify, Explain, Analyse, Calculate, Evaluate**. Composite performance tasks also use Describe and Discuss. Other framework-permitted words may be used only through a recorded, justified slot deviation. No item opens with Draw: it appears embedded in a held paper rather than as a primary opening. A diagram instruction may be phrased Explain using a diagram.

| Subtype | Opener | Marks | Function |
|---|---|---:|---|
| DEF | Define | 1 | Precise recall |
| FEATURE | Identify | 2 | Distinct requested elements |
| DIST / APP / MISCON | Explain | 2 | Short distinction, scenario or conceptual discrimination |
| MECH / BEN / LIM | Explain | 4 | Developed economic reasoning |
| INTERP | Analyse | 4 | Relationship, evidence and explanation |
| CALC | Calculate | 2 | Formula, working, quantity and interpretation |
| DIAGRAM | Explain | 7 | Construction and economic explanation |
| EVAL | Evaluate | 7 | Opposing arguments, condition and judgement |

Every pair occurs in the held QPs. One mark can require the complete essential definition; do not assign independent marks to more elements than its total. Some slot words are common to several papers and AOs; the whole demand determines the response, not the verb alone.

## 3. Answer shapes

Read `curriculum/answer-shapes.json` and `subject-profile.yaml -> answer_structures`. Guidance must identify the actual credit-bearing elements, not repeat labels as filler. A mechanical C-16 pass is not semantic certification.

Definitions require the economic sense. A short application supplies its facts in the prompt and applies that sense. Mechanisms run initial change → reason → consequence for a named agent. A numerical answer supplies the relationship, working, final units and an economic interpretation. An INTERP response explains a data relationship using evidence, rather than recalculating it.

Evaluation develops the case for and the case against, then identifies the decisive condition and answers the actual question. The 2023 report sometimes reserves a conclusion mark; the 2024 report sometimes splits marks across sides. Neither is a universal rule. The author must give a coherent seven-mark rubric totalling seven and never add a mark above the stated tariff. Discrepant report figures do not become new rules.

Diagram practice uses a numerical schedule and precise construction instructions for the learner: axes, labelled curves, initial equilibrium, specified shift/control, new equilibrium or shortage/surplus, and interpretation. The standard renderer supports break-even, not NSSCO demand/supply or PPF diagrams. No hand-drawn character art, ad hoc SVG or unrelated break-even chart may masquerade as a checked economic diagram. This plan does not claim graphical production has been certified.

## 4. Card types, assessment objectives and Bloom levels

**{tot['flashcards']} flashcards plus {tot['performance_tasks']} composite practice tasks = {tot['items']} items.** The tasks contain multiple questions; a task count is not a single-question-part count. Each topic has a demand-specific short-answer set and data response. The 24 topics with a defensible discussion/decision demand also have a paired evaluation plan; 3.1, 3.4, 6.1 and 7.3 do not. The forms are:

- An eight-mark short-answer set: four two-mark retrieval/application questions with explicit commands and content per part, AO A.
- A contextual response: normally Describe 6, Explain 7, Discuss 7 (A6/B7/C7). The four narrow descriptive topics instead use a case_analysis slot: Describe 6, Explain 4, Explain 4 (A6/B8), with no forced evaluation; its rubric requires data, explanation and allocations, without opposing-argument or judgement requirements.
- Where appropriate, two contrasting seven-mark evaluation plans in one 14-mark task; change an agent, constraint or time horizon between them. Practice allocation C14.

These are **planner practice allocations**, not transcribed official per-part AO splits. `planning/performance-specs.json` supplies each composite slot's objective IDs, AO labels, Bloom level, opener, total and part tariffs. Evaluation already develops both sides; separate BEN/LIM flashcards are not automatically duplicated for the same objective. Use the observed part tariffs; do not pretend Evaluate is a 14-mark single question.

Short two-mark APP and DIST cards model Paper 1 Section A and carry A, even when Bloom demand is Apply or Understand. Four-mark mechanisms/benefits/limitations carry B. Evaluations carry C. MISCON discrimination carries A/B. Bloom and AO are separate axes; all slots declare both. No automatic AO top-up is enabled, and there is no redundant CHAIN addition on top of the same mechanism.

Bloom totals: {', '.join(f'{k} {n}' for k,n in v['blooms'].items())}. Every claim must be taught in the notes that support the items. Unseen member objectives retain full coverage without borrowing their parent frequency.

## 5. The topics

| Topic | Objectives | Items including tasks | Notes words |
|---|---:|---:|---:|
{table}
| **Total** | **{tot['objectives']}** | **{tot['items']}** | **{tot['notes_min']:,}–{tot['notes_max']:,}** |

There are 28 content units, one per topic; all filenames come from the generator. Words are full teaching notes, not flashcard backs padded into paragraphs. Work through syllabus order. The topic titled Population also owns the specified developed/developing-economy content; use the registry, not the title alone, to judge coverage.

## 6. AO balance, in marks

Independent exact calculation splits each flashcard tariff across its declared AOs and uses the explicit practice allocations for tasks. This is a planning estimate, not an official exam forecast. The standard `curriculum/ao_coverage.md` is retained as generated and uses rounded per-topic shares; the exact calculation below is in `planning/plan-validation.json`.

| AO | Target | Planned | Gap in points |
|---|---:|---:|---:|
{ao}

Across {sum(v['ao_marks_equivalent'].values()):,.0f} marks-equivalent, the largest exact gap is **{v['largest_gap_points']:.2f} points**, within the five-point tolerance. No per-topic matching is claimed or required. Do not rebalance by padding definitions or by relabelling analysis as evaluation.

## 7. Misconceptions, glossary and scope

There are 32 named conceptual confusions, each with exactly one MISCON slot, and **132 settled glossary entries**, with no null senses. The discrimination is the target: explain the boundary and apply a test, rather than restating a definition. Generic listing, missing units and one-sided answers remain response-quality issues.

Read `curriculum/topic-ownership.json`: exchange quotation/conversion is owned by 2.3, macro trade by 7.4; banking institutions by 2.3, policy instruments by 6.2; productivity IT by 5.2, household welfare by 8.2; productivity effects of HIV and AIDS by 5.2, workplace protection by 6.3. Contracts carry the corresponding semantic cross-links, replacing lexical matches. The complete ownership table follows.

{ownership_table}

All contracts contain the seven judgement-based scope patterns plus positive/manual depth constraints. No false explicit syllabus exclusion has been invented. Keep elementary theory and simple data; include comparative advantage, economic rent, transfer earnings and appropriately conditioned profit maximisation because they are in scope. A glossary entry alone does not commission a new independent unit.

Adjacent topics can be named for a cross-link but are taught in their own topic. Do not import statutory shareholder limits, present tax rates, current economic statistics or named legal rights from memory. Conceptual ownership and protection mechanisms can be taught without those details; verify a jurisdiction-specific claim before using it. The verified Bank of Namibia constraint is in `curriculum/jurisdiction-sources.json`: actual N$ examples maintain the one-to-one rand peg. Use a clearly quoted third currency for appreciation/depreciation. Monetary-policy choices support the peg; do not assert unrestricted independence or identical repo rates. `definition-rulings.json` resolves syllabus shorthand for demand, long-run diseconomies and increasing opportunity cost; the settled glossary governs learner wording.

## 8. Rules particular to this subject

1. Invented Namibian/southern African entities, N$, British English, and teaching data identified as invented. No real company scenarios copied from the corpus.
2. All item IDs and labels come from the work order; composite metadata comes from performance-specs.json. A justified change is recorded in authoring_notes.json.
3. Every numerical example is internally consistent. Do not identify causal elasticity from simultaneous supply shocks and quality changes. Distinguish percentage changes from percentage-point changes.
4. State conditions: price/revenue depends on elasticity; a binding wage floor is above equilibrium; growth does not guarantee distributed gains; scale and short-run output changes differ; currency effects depend on response.
5. No exam-priority claims, official question wording or mark-scheme language in learner-facing material.
6. Exemplar: `exemplar/topics/1.1/` shows seven claims, a full original content unit and ten original items. It has **no failures**, one C-18 item-count warning, C-35/C-41/C-43 not_run because the renderer has no supported economic graphical model and no separate practice text is present, and a separate semantic-review pending entry. Original schedule-based DIAGRAM practice is present; it is not a rendered image. Those are not reported as passes. The checker returns PUBLISH; no material has been published. `exemplar/shape-slices/3.2/` and `5.3/` demonstrate a market DIAGRAM/INTERP and cost CALC/INTERP with original Namibian data and concrete mark allocations. Thin slices pass schemas, claim links and independent numerical controls; they are not whole-topic publication verdicts.
7. Tooling caveats: the contract generator reads a transient legacy exposure projection through generate_contracts.py and the work-order generator uses generate_work_orders.py for topic-specific performance inputs; canonical metrics stay nested and C-39 passes. Profile schemas predate the slot_plan/conditioned_mechanisms extensions; registry/claims/units/items validate under the operative schemas. The run_checks CLI may return a nonzero status despite a serialized publish verdict because it compares against the older decision string; inspect qa_report.json and what_to_fix.py. No standard file was edited.
8. Codex authors sequentially under the playbook. Once the plan is approved and committed, author all topics, run render_notes/run_checks/what_to_fix for each and fix real failures. Cross-review with Claude follows authoring; older model handovers saying no review do not apply.
'''
(WS/'PLAN-6145-nssco-economics.md').write_text(plan)
handover=f'''# Handover prompt — 6145 NSSCO Economics

Jeremy approved the plan on 7 November 2026. Use after the human plan commit. Owner Jeremy; authoring tool Codex. Current stage is planning, not authoring permission.

## Start here

Read AGENTS.md and TEAM-PLAYBOOK.md, then this subject's PLAN-6145-nssco-economics.md, subject-profile.yaml, curriculum/answer-shapes.json, curriculum/glossary.json and the AUTHOR role when step 5 starts. This handover wins over generic authoring instructions, but the team playbook controls order and human checkpoints. Do not reopen another subject or regenerate the plan.

## The job

Author {tot['items']} items: {tot['flashcards']} flashcards and {tot['performance_tasks']} composite tasks, across {tot['topics']} topics and {tot['objectives']} assessable objectives. Full notes total {tot['notes_min']:,}–{tot['notes_max']:,} words. Topic order:

```text
{topics}
```

For each topic read its generated contract and work_order, plus the matching records in planning/performance-specs.json. Write claims/canonical_claim_ledger.json, the named content-units file and learning-items/topic_<T>_items.json. The renderer chooses the markdown filename. Main topics currently contain plans only; the isolated exemplar is not completed topic output and must not be copied into main topics wholesale.

## Every item carries its labels

Use the slot ID as item_id. Copy subtype or item_type, assessment_objectives, blooms_level, command_word and mark_tariff. Composite totals are sums of their observed part tariffs. MISCON items copy misconception_entry. Claim IDs resolve to original claim statements; every item-objective mapping is supported by a cited claim, and the notes teach that claim. Set revision 1 initially; claims_seen records cited revisions and authored_hash is SHA-256 of _artefact_text. All new derivatives have qa_status review_required; claims stay unverified and publishable false.

## Rules that come from the syllabus and the corpus

Follow the plan's command/tariff table and economic answer shapes. Full context and data live in the item prompt. A two-mark Paper 1-style application can carry A while Bloom is Apply. Do not convert every B into C by adding the word judgement. Four-mark explanations develop mechanisms; evaluations genuinely weigh opposing arguments and a decisive condition. State the exact marking elements and an allocation that totals the item's parts.

Teach every source objective and every listed member, including objectives with zero direct frequency. Preserve original wording only as internal syllabus metadata. Write every learner scenario, question, answer and rubric originally. No reproduced exam scenarios, real named companies, copied mark-scheme answers or assessment-frequency claims. Use the glossary and conceptual boundaries. No unverified current legal/numerical assertions. Keep marginal revenue limited to distinguishing it from average revenue and the source-evidenced profit-maximisation treatment; do not expand it into a separate advanced unit.

For diagrams, supply clean schedules and construction/interpretation instructions for the learner to plot. The standard has no demand/supply renderer; do not use break-even art for it, hand-author fences or claim that a nonexistent diagram is verified. Keep short-run diminishing returns distinct from long-run scale effects and state the conditions on causal claims.

## Voice

Plain British English, connected explanatory prose, invented Namibian or southern African scenarios and N$. Notes are a standalone teaching resource. Worked examples explain the steps and economic meaning, not just the result. No filler added to meet counts and no instructional implementation details in learner prose.

## The work order is a baseline, not a cage

A genuinely unsuitable slot is reported with objective, proposed change and reason in topics/<T>/authoring_notes.json as {{from, to, why}}. Preserve totals and labels unless a deviation is justified. Do not add high-level content to make a seven-mark question easier to write. The paired evaluation plans use the explicit first/second conditions in performance-specs.json, not duplicated wording. Narrow descriptive topics have no essay-plan slot. Follow topic ownership and definition rulings; actual N$ exchange examples must respect the rand peg documented in jurisdiction-sources.json. Separate supplied data from worked results. Learner prompts/context contain the inputs and task only; canonical answers and separately labelled teaching explanations contain the solution. Read the exemplar and the 3.2/5.3 shape slices; copy their rubric discipline and data consistency, never their scenarios.

## Finishing each topic

Run the standard render_notes.py, run_checks.py and what_to_fix.py with this workspace and topic. Read the JSON verdict as well as exit status: the current run_checks wrapper expects an older pass string while the suite returns publish. Fix every fail; never call not_run a pass. Report inapplicable checks separately with their reason, and investigate missing applicable inputs. Stop after three unsuccessful attempts on the same real check and record the blocker, then continue other topics as the playbook directs.

## Boundaries

Do not edit standard/, sources/, another subject, curriculum files, the exemplar or generated work orders while authoring. Do not commit or push. The person commits at playbook checkpoints. Do not treat deterministic success as human or cross-vendor review. The required reviewer after Codex authors is Claude.

## Report back when the subject is finished

Under 250 words: topics completed/blocked, claims/units/items/notes totals, final check verdicts, remaining not_run checks and warnings, deviations, plan problems and whether publication was performed. Update STATUS.md throughout. No material is published during step 4.
'''
(WS/'HANDOVER-6145-nssco-economics.md').write_text(handover)
print('Plan and handover rendered with validated counts.')
