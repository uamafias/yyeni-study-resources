# Plan — 6145 NSSCO Economics

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

**378 flashcards plus 80 composite practice tasks = 458 items.** The tasks contain multiple questions; a task count is not a single-question-part count. Each topic has a demand-specific short-answer set and data response. The 24 topics with a defensible discussion/decision demand also have a paired evaluation plan; 3.1, 3.4, 6.1 and 7.3 do not. The forms are:

- An eight-mark short-answer set: four two-mark retrieval/application questions with explicit commands and content per part, AO A.
- A contextual response: normally Describe 6, Explain 7, Discuss 7 (A6/B7/C7). The four narrow descriptive topics instead use a case_analysis slot: Describe 6, Explain 4, Explain 4 (A6/B8), with no forced evaluation; its rubric requires data, explanation and allocations, without opposing-argument or judgement requirements.
- Where appropriate, two contrasting seven-mark evaluation plans in one 14-mark task; change an agent, constraint or time horizon between them. Practice allocation C14.

These are **planner practice allocations**, not transcribed official per-part AO splits. `planning/performance-specs.json` supplies each composite slot's objective IDs, AO labels, Bloom level, opener, total and part tariffs. Evaluation already develops both sides; separate BEN/LIM flashcards are not automatically duplicated for the same objective. Use the observed part tariffs; do not pretend Evaluate is a 14-mark single question.

Short two-mark APP and DIST cards model Paper 1 Section A and carry A, even when Bloom demand is Apply or Understand. Four-mark mechanisms/benefits/limitations carry B. Evaluations carry C. MISCON discrimination carries A/B. Bloom and AO are separate axes; all slots declare both. No automatic AO top-up is enabled, and there is no redundant CHAIN addition on top of the same mechanism.

Bloom totals: Remember 136, Understand 68, Apply 91, Evaluate 51, Analyse 112. Every claim must be taught in the notes that support the items. Unseen member objectives retain full coverage without borrowing their parent frequency.

## 5. The topics

| Topic | Objectives | Items including tasks | Notes words |
|---|---:|---:|---:|
| 1.1 Basic economic problem: scarcity and exercise of choice | 3 | 10 | 820–1,180 |
| 1.2 Types of economic systems and economic resources | 10 | 20 | 2,480–3,560 |
| 1.3 Specialisation and division of labour | 8 | 17 | 1,950–2,800 |
| 2.1 Business organisations | 11 | 26 | 2,710–3,890 |
| 2.2 Trade unions and employer association | 10 | 22 | 2,470–3,550 |
| 2.3 Financial institutions | 11 | 21 | 2,760–3,960 |
| 3.1 What is a market? | 2 | 6 | 500–720 |
| 3.2 Market forces | 9 | 22 | 2,230–3,200 |
| 3.3 Price elasticity | 9 | 17 | 2,250–3,230 |
| 3.4 Advertising | 2 | 6 | 500–720 |
| 3.5 Policies | 3 | 8 | 730–1,050 |
| 4.1 Occupational choices | 3 | 9 | 730–1,050 |
| 4.2 Earnings | 10 | 25 | 2,410–3,460 |
| 4.3 Expenditure | 9 | 20 | 2,180–3,130 |
| 5.1 The private firm as producer and employer | 4 | 11 | 1,040–1,500 |
| 5.2 Productivity | 5 | 14 | 1,340–1,930 |
| 5.3 Production costs and revenue | 10 | 20 | 2,450–3,520 |
| 5.4 Economies and diseconomies of scale | 11 | 25 | 2,730–3,920 |
| 6.1 Government as producer and employer | 4 | 7 | 990–1,420 |
| 6.2 Government economic policies | 18 | 41 | 4,400–6,320 |
| 6.3 Government control | 5 | 10 | 1,300–1,870 |
| 7.1 Prices | 3 | 11 | 870–1,250 |
| 7.2 Employment | 4 | 10 | 1,100–1,580 |
| 7.3 Output | 9 | 18 | 2,200–3,160 |
| 7.4 International trade | 5 | 16 | 1,330–1,910 |
| 8.1 Population | 10 | 23 | 2,520–3,620 |
| 8.2 Living standards | 3 | 12 | 820–1,180 |
| 9.1 Conflicts | 6 | 11 | 1,450–2,080 |
| **Total** | **197** | **458** | **49,260–70,760** |

There are 28 content units, one per topic; all filenames come from the generator. Words are full teaching notes, not flashcard backs padded into paragraphs. Work through syllabus order. The topic titled Population also owns the specified developed/developing-economy content; use the registry, not the title alone, to judge coverage.

## 6. AO balance, in marks

Independent exact calculation splits each flashcard tariff across its declared AOs and uses the explicit practice allocations for tasks. This is a planning estimate, not an official exam forecast. The standard `curriculum/ao_coverage.md` is retained as generated and uses rounded per-topic shares; the exact calculation below is in `planning/plan-validation.json`.

| AO | Target | Planned | Gap in points |
|---|---:|---:|---:|
| A | 39% | 37.71% | -1.29 |
| B | 25.5% | 29.66% | +4.16 |
| C | 35.5% | 32.63% | -2.87 |

Across 2,124 marks-equivalent, the largest exact gap is **4.16 points**, within the five-point tolerance. No per-topic matching is claimed or required. Do not rebalance by padding definitions or by relabelling analysis as evaluation.

## 7. Misconceptions, glossary and scope

There are 32 named conceptual confusions, each with exactly one MISCON slot, and **132 settled glossary entries**, with no null senses. The discrimination is the target: explain the boundary and apply a test, rather than restating a definition. Generic listing, missing units and one-sided answers remain response-quality issues.

Read `curriculum/topic-ownership.json`: exchange quotation/conversion is owned by 2.3, macro trade by 7.4; banking institutions by 2.3, policy instruments by 6.2; productivity IT by 5.2, household welfare by 8.2; productivity effects of HIV and AIDS by 5.2, workplace protection by 6.3. Contracts carry the corresponding semantic cross-links, replacing lexical matches. The complete ownership table follows.

| Construct | Owner | Cross-links | Teaching rule |
|---|---|---|---|
| exchange rates | 2.3 | 7.4 | 2.3 owns quotation, conversion and direct agent effects; 7.4 owns macro causes, trade patterns and comparative advantage. |
| banking and monetary policy | 2.3 | 6.2 | 2.3 owns institutional functions and their evaluation; 6.2 owns policy aims, transmission and budget/interest instruments. |
| policy aims and outcomes | 6.2 | 7.1,7.2,7.3,7.4 | 6.2 owns instrument choices and conflicts between aims; indicator topics own definitions, measures and specific causes/consequences. |
| trade protection | 7.4 | 9.1 | 7.4 owns trade mechanisms; 9.1 owns conflicting interests and judgements over time. Cross-link the mechanism rather than reteach it. |
| IT | 5.2 | 8.2 | 5.2 owns output per input; 8.2 owns household access and living standards, including distribution. |
| HIV and AIDS | 5.2 | 6.3 | 5.2 owns productivity effects; 6.3 owns workplace protection and non-discrimination, without unverified statutory detail. |
| public corporation | 2.1 | 6.1 | 2.1 owns ownership/legal form; 6.1 owns government production, services and employment. |
| firm output and national output | 5.3 | 7.3 | 5.3 owns firm costs/revenue; 7.3 owns national accounting. Similar words do not establish an overlap. |
| pricing and government policy | 3.5 | 6.2 | 3.5 owns firm pricing/output in specified market structures; 6.2 owns macroeconomic policy. |
| allocation and markets | 1.2 | 3.1 | 1.2 owns economic systems; 3.1 owns the arrangement linking buyers and sellers. |

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
