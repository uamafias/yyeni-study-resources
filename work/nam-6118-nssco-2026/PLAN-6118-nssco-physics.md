# Plan — Namibia NSSCO Physics 6118

Operator-approved plan · approval recorded in curriculum/operator-decisions.json. Approved for Step 5 authoring; learner release remains separate.

## 0. What the syllabus says

The approved working source is the NIED-listed 2018 edition. The operator accepted it for this 2026 workflow; no separate NIED statement establishing 2026 applicability is claimed. All source figures are transcribed in `curriculum/syllabus-facts.json`.

| AO | Name | Raw specification-grid target | P1 raw marks | P2 raw marks | P3 raw marks |
|---|---|---:|---:|---:|---:|
| A | Knowledge with understanding | 47% | 25 | 50 | 0 |
| B | Handling information, application and solving problems | 28% | 15 | 30 | 0 |
| C | Practical (experimental and investigative) skills and abilities | 25% | 0 | 0 | 40 |

P1: 40 four-option MC items, 30% of the grade. P2: 80 structured marks, 90 minutes, 50%. P3: 40 written practical marks, 75 minutes, 20%. The P1 timing conflict remains explicitly waived as non-major: syllabus and 2020/2022–2024 covers say 45 minutes; 2021/2025 covers say one hour. Neither is asserted as the 2026 timing.

The practice target uses the approximate raw grid **47/28/25**, consistent with 75/45/40 raw marks. The different **50/30/20** is derived from final component weighting. The syllabus also states **53% skills / 47% knowledge**. These are distinct measures; none is a card quota. The denominator of the 24% recall limit remains unresolved.

## 1. What the corpus says

The approved Step 3 analysis covers 18 question papers and six Physics report sections from 2020–2025: 622 demand segments and 960 printed marks, with a compensated 2024 MC item excluded from usable exposure. Calculate is the largest single P2 family at 36% of marks. The practical corpus repeatedly tests graph/data work and an eight-mark investigation plan.

Checked credit architecture covers **355 demands**, including every primary calculate (99), define (16) and explain (22) demand and all 25 three-mark calculations. The exact **267 outstanding demands** remain listed in `assessment-evidence/GAPS.md`. 2020 P1 contributes demands only, with no difficulty or answer evidence. Keys for 2021–2025 provide 199 usable answers plus one compensation marker. The 2022/2023 First Proof versions remain unconfirmed.

## 2. Command words and tariffs

`curriculum/assessment-framework.json` carries the measured primary-command counts and exact observed tariffs, with listed-but-unobserved glossary rows disabled. Every planned flashcard uses an observed command/tariff combination. A modal tariff is not a universal marking rule. `planning/task-shape-anchors.json` supplies the additional narrow State/Describe/Draw/Derive examples used by the slot policy.

| Planned use | Command | Tariff |
|---|---|---:|
| Core meaning or one fact | Define / State | 1 |
| A causal explanation, distinction or linked case | Explain | 2 |
| A numerical application | Calculate | 2 |
| One explicitly requested practical action | Describe | 1 |
| Two specified graph/diagram features | Draw | 2 |
| Hydrostatic derivation | Derive | 4 |
| Complete investigation plan, inside a practical task | Plan | 8 |

A long conditioned definition is taught fully in notes and in the structured task; a one-mark core-meaning card must not claim to reproduce a two-mark official definition. For calculations, use the located row relevant to the task: units, conversions, intermediate results and rounding receive different credit. No unentered memo row is silently treated as an official rubric.

## 3. Answer shapes

`curriculum/answer-shapes.json` records 156 distinct structured/practical demand architectures. A topic has a 12-question original MC set, an eight-mark structured task, and, where a suitable physical investigation exists, a 16-mark integrated practical task: graph 5, gradient 3, plan 8. This is a practice composite, not a claimed fixed Paper 3 layout. Specific graph and plan architectures come from the located report examples.

Every task is bound to objective IDs, a physical context and, for practicals, an original six-point dataset in `curriculum/topic-task-specifications.json`. Every dataset declares itself invented/idealised. All quantities and axis meanings must be checked before authoring. Topic-specific limits explain inverse relationships, echo return time, empirical magnetic data and calculated rather than independently measured energy.

The two thin exemplars contain pressure definitions/calculations and practical graph/conclusion/investigation tasks. Both have **40 passed, zero failed, one warning and three not-run checks**. Not-run checks concern graphical stimulus automation, generated chart rendering and reading texts; they are not semantic approval. Claims remain unverified and non-publishable. The standard CLI returns 1 because it compares its decision to `pass` while the suite emits `publish`; this existing mismatch is recorded, not edited.

## 4. Card types, assessment objectives and Bloom levels

Definitions/features recall knowledge; explanations teach causal understanding; calculations and diagram processing require application. Source-list containers receive one linked comparison/application card, while their members receive focused practice. Only the 23 retained examiner-evidenced conceptual distinctions produce MISCON slots. The six moved candidate-error entries stay as skill practice.

A/B/C and Bloom are separate labels. Content cards narrow to A or B as specified; foundational practical topics and integrated practical tasks carry C. Mixed A/B marks on a container or MC set are a planning estimate, not an official per-item allocation. No balancing top-up cards were added. The source-to-registry crosswalk retains existing demand links on source containers when a finer member link is not established; children do not inherit exam frequency by guesswork.

## 5. The topics

The 335 source bullets become 71 source-family containers and 495 leaf practice outcomes (including one bounded Annex D symbol anchor): **566 non-root registry records**, within 28 teaching topics. Counts below include containers; leaf counts are stated separately. The generated item budget counts an MC set as one learning item.

| Topic | Objectives (leaf) | Items | Notes words |
|---|---:|---:|---:|
| 1. Mathematical skills and units | 48 (41) | 51 | 4,615–7,825 |
| 2. Planning investigations and recording results | 13 (11) | 14 | 1,410–2,230 |
| 3. Graphs, uncertainty and experimental conclusions | 19 (18) | 20 | 2,695–4,285 |
| 4. Measurement, scalars and vectors | 18 (15) | 21 | 1,855–3,005 |
| 5. Position, speed and acceleration | 20 (20) | 26 | 2,640–4,260 |
| 6. Forces, springs and momentum | 19 (18) | 25 | 2,125–3,415 |
| 7. Mass, weight and density | 12 (12) | 16 | 1,630–2,570 |
| 8. Moments, equilibrium, stability and friction | 11 (11) | 15 | 1,660–2,600 |
| 9. Energy sources and renewable systems | 21 (17) | 24 | 1,580–2,640 |
| 10. Energy, work, efficiency and power | 21 (18) | 24 | 2,175–3,585 |
| 11. Pressure and hydraulics | 11 (11) | 15 | 1,590–2,530 |
| 12. Particles, phases and gases | 24 (21) | 27 | 2,755–4,445 |
| 13. Temperature and thermometers | 14 (12) | 18 | 1,450–2,370 |
| 14. Heat capacity and changes of state | 18 (17) | 23 | 2,375–3,765 |
| 15. Thermal energy transfer | 16 (14) | 20 | 1,690–2,730 |
| 16. Wave motion and wavefronts | 23 (19) | 27 | 2,020–3,440 |
| 17. Light propagation and reflection | 17 (14) | 20 | 1,625–2,675 |
| 18. Refraction, lenses and vision | 33 (27) | 39 | 3,120–5,180 |
| 19. The electromagnetic spectrum | 19 (17) | 21 | 1,460–2,440 |
| 20. Sound and echoes | 13 (12) | 17 | 1,565–2,515 |
| 21. Electrostatics | 18 (15) | 21 | 1,595–2,685 |
| 22. Current, electromotive force and potential difference | 14 (13) | 18 | 1,685–2,695 |
| 23. Resistance and electric circuits | 36 (31) | 40 | 3,695–6,145 |
| 24. Electrical energy and safety | 27 (22) | 30 | 2,315–3,885 |
| 25. Magnets, electromagnets and motors | 28 (24) | 32 | 2,980–4,880 |
| 26. Induction, generators and transformers | 17 (15) | 20 | 2,020–3,240 |
| 27. Atomic structure and isotopes | 16 (14) | 20 | 1,420–2,400 |
| 28. Radioactivity and half-life | 20 (16) | 22 | 1,780–2,960 |
| **Total** | **566 (495)** | **666** | **59,525–97,395** |

The item mix is 590 individual cards, 26 MC sets (312 one-mark questions), 26 structured tasks and 24 integrated practical tasks. The note ranges come from explicit source/member/type depth budgets, not a full chapter per list member. Work orders are the operative counts; containers and source-bullet totals are not volume quotas.

## 6. AO balance, in marks

The following is the standard generator’s whole-subject estimate. Its independent rounding can make the displayed percentages sum to 99 or 101.

| AO | planned | syllabus weight | gap |
|---|---:|---:|---:|
| A | 48% | 47% | +1 |
| B | 28% | 28% | +0 |
| C | 23% | 25% | -2 |

✅ **largest gap 2 points** across 1,867 marks-equivalent of practice.

A gap inside 5 points is the plan matching the exam. A larger one means the item plan needs more of that kind of practice - not that a topic should be padded.

The largest gap is two percentage points, within the required five. The three stated syllabus measures remain distinct. Per-topic differences are intentional; whole-subject balance is the comparison that matters.

## 7. Misconceptions, glossary and scope

The 23 retained misconception entries, 53 glossary senses and three bounded scope screens travel with the contracts. All 35 depth/condition statements remain binding. Collision definitions are not required; nuclear formulas are limited only in energy-source teaching; diverging lenses are restricted to eye correction. Decay equations remain required. Every contract carries all three screens. Neighbour topics are boundaries for extended teaching, not banned vocabulary.

## 8. Rules particular to this subject

1. Author original stems, data, explanations, diagrams and answers. Never reproduce official assessment wording in learner materials.
2. Teach each formula with symbol meanings, units, its physical conditions and a worked application. Keep unrounded working; round the final result as requested.
3. Graph tasks must specify axes, quantities, units, scale and data. Infer the slope’s physical meaning from those axes. Never transplant the known density/stiffness source mistakes.
4. Drawing outcomes require actual drawing/construction practice. Provide an original accessible diagram or a sufficiently specified construction task, with a labelled solution; text alone must not erase diagram reasoning. No code fences or LaTeX.
5. Full practical plans must say what changes, what is measured, what is controlled, how data is recorded, and how a conclusion follows. Written preparation accompanies real practical experience.
6. All demand mappings and registry decomposition remain lead-planner judgements. Independent mapping/content review is scheduled for Step 6; no such review is claimed here.
7. The operator-approved working syllabus and waived non-major P1 timing issue are not reopened. The First Proof and outstanding-marking caveats remain visible.
8. Use the recorded Step 4 approval to proceed with Step 5. Learner publication remains a separate decision.

