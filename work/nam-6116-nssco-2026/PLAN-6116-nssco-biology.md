# Plan — NSSCO Biology 6116 (Namibia, Ordinary Level, Grades 10–11)

**Plan approved by Lotto, 2026-10-18.** The originally banked 254 images are operator-approved at the file hashes in `planning/operator_approvals.json`; four later item-specific graphs are unapproved. The AO discrepancy and reasoning-coverage limitations remain documented; no percentage-driven additions are required. Full authoring and the Step 6 review copy are complete. The 35 figure holds, scientific verification and actual learner delivery remain open.

The brief an authoring agent works to. Generated 19 October 2026 from `work/nam-6116-nssco-2026/curriculum/` and the topic work orders by `planning/write_plan_docs.py`; regenerate rather than edit. The analysis it rests on is `operations/analysis/6116-nssco-biology-corpus-analysis.md` (with its 2026-10-18 corrections). Owner: Lotto. This subject is the NSSCO pilot, run under a recorded exception to the pilot rule (see `STATUS.md`).

## 0. What the syllabus says

Transcribed from `Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_BIOLOGY_SYLLABUS.pdf` (NIED 2018), every value with its page (`curriculum/syllabus-facts.json`). Printed page = PDF page − 3.

| AO (build code) | NSSCO | name | stated overall weight | Paper 1 | Paper 2 | Paper 3 |
|---|---|---|---:|---:|---:|---:|
| AO1 | A | Knowledge with understanding | 47% | 25 marks | 50 marks | 0 marks |
| AO2 | B | Handling information, application and solving problems | 28% | 15 marks | 30 marks | 0 marks |
| AO3 | C | Practical (experimental and investigative) skills and abilities | 25% | 0 marks | 0 marks | 40 marks |

Specification grid, printed p.37 [PDF 40]. AO A carries the printed qualifier "(not more than 24% recall)"; the syllabus does not say what the 24% is a share of (open issue 1).

- **Paper 1, Theory: Multiple choice questions.** 40 marks, 45 minutes in the syllabus; 1 hour on the 2025 paper; 2026 unconfirmed (open issue 2), 30% of the qualification.
- **Paper 2, Theory: Structured questions.** 80 marks, 1 hour 30 minutes, 50% of the qualification.
- **Paper 3, Alternative to Practical Paper.** 40 marks, 1 hour 15 minutes, 20% of the qualification.

Paper 1 is forty four-choice questions on the specific objectives, testing A and B. Paper 2 is compulsory short-answer and structured questions, mainly A and B. Paper 3 is a written paper testing familiarity with practical procedures, mainly C, specified by Annexe A criteria (a)–(k) (printed p.36 [PDF 39], p.41 [PDF 44]). The syllabus glossary (printed p.39–40) defines 18 command words. The syllabus states 7 distinct content limits, one of them on two objectives (section 7).

**Two AO percentages, two bases.** 47/28/25 is **stated**: the grid's "Overall Weighting across all components", equal to the raw marks A 75, B 45, C 40 of 160. 50/30/20 is **derived**: each paper's AO marks weighted by the stated paper weightings 30/50/20, i.e. the share of the final grade. The AO balance check in this plan uses the stated 47/28/25. Neither is a card quota.

## 1. What the corpus says

Six series, 2020–2025: 18 question papers (Paper 1, 2 and 3 each year) and six examiner reports, each with a Biology 6116 section. **No mark schemes exist** for this syllabus. Paper 2 contributes 480 marks across its six papers and Paper 3 240, together 720 across twelve; Paper 1 is forty one-mark questions each year with no command word. Some papers are labelled First Proof.

- **Short answers.** 70% of Paper 2 and 3 parts are 1–2 marks and none exceeds 6. The 5–6 mark parts are experimental design, multi-step causal explanation and genetic diagrams.
- **Paper 2 is description and naming led** (describe, name, state, identify, explain). **Paper 3 is calculation and interpretation led** (calculate, explain, describe, suggest).
- **Terminology precision** is the most frequent loss in the examiner reports: wrong or misspelt structure names, imprecise terms.
- **27 curated, examiner-evidenced misconceptions**, from 89 raw statements, each tied to one objective with a test that separates the two ideas.
- **Exposure is mapped to objectives by meaning.** 339 Paper 2 and 3 parts have direct objective mappings (`assessment-evidence/assessment_evidence.json`; 262 high, 77 medium, 0 low confidence; one Miner pass with targeted Codex review/repairs). 264 of the 540 objectives are named by at least one part. Exposure calibrates emphasis only; every objective is planned.
All 341 original parts remain inventoried. The 2 excluded parts are retained in `assessment-evidence/mapping_exceptions.json`: pesticide uptake is unresolved, and the extinction definition is context-only. Neither credits direct objective exposure. The nucleus identification now maps to cell structure, not prepared-slide meiosis.

## 2. Command words and tariffs

Use only these to open a prompt. The rule is the repository's: a word may open a prompt if it opens at least one part in the papers (`used_at_level = observed_count > 0`, `standard/v0.2.0-draft/mine/assemble.py:144`; check C-14 forbids the rest). The tariff is the one the work-order slot names; every slot tariff is the modal tariff the papers set for that word.

| command word | in the syllabus glossary | parts | modal tariff | tariffs seen | evidence |
|---|---|---:|---:|---|---|
| describe | yes | 52 | 2 | 1, 2, 3, 4, 5 | observed |
| explain | yes | 39 | 2 | 1, 2, 3, 4 | observed |
| name | no (observed) | 39 | 1 | 1, 2, 3 | observed |
| state | yes | 34 | 1 | 1, 2, 3, 4 | observed |
| suggest | yes | 28 | 2 | 1, 2, 3, 4 | observed |
| identify | no (observed) | 22 | 2 | 1, 2, 3, 4 | observed |
| define | yes | 12 | 2 | 1, 2, 3 | observed |
| complete | no (observed) | 10 | 2 | 1, 2, 3, 4, 6 | observed |
| draw | no (observed) | 10 | 4 | 1, 2, 3, 4, 5 | observed |
| calculate | yes | 9 | 2 | 1, 2, 3 | observed |
| give a reason/give reasons | yes | 9 | 1 | 1, 2 | observed |
| give | no (observed) | 8 | 2 | 1, 2, 3 | observed |
| show | no (observed) | 8 | 2 | 2, 3 | observed |
| discuss | yes | 7 | 3 | 2, 3, 4 | observed |
| outline | yes | 7 | 3 | 2, 3, 4 | observed |
| write | no (observed) | 6 | 4 | 1, 4, 5 | observed |
| construct | no (observed) | 4 | 4 | 2, 3, 4 | observed |
| list | yes | 4 | 2 | 1, 2, 3 | observed |
| describe and explain | yes | 3 | 2 | 2, 3, 4 | observed |
| label | no (observed) | 3 | 3 | 2, 3 | observed |
| count | no (observed) | 2 | 2 | 1, 2 | observed |
| determine | yes | 2 | 1 | 1 | observed |
| distinguish | no (observed) | 2 | 2 | 2 | observed |
| match | no (observed) | 2 | 4 | 3, 4 | observed |
| plot | no (observed) | 2 | 5 | 3, 5 | observed |
| shade | no (observed) | 2 | 1 | 1, 3 | observed |
| what is meant by | no (observed) | 2 | 1 | 1 | observed |
| work out | no (observed) | 2 | 1 | 1 | observed |
| estimate | yes | 1 | 1 | 1 | thin (one part) |
| indicate | no (observed) | 1 | 4 | 4 | thin (one part) |
| measure | yes | 1 | 1 | 1 | thin (one part) |
| read | no (observed) | 1 | 1 | 1 | thin (one part) |
| record | no (observed) | 1 | 1 | 1 | thin (one part) |
| support | no (observed) | 1 | 1 | 1 | thin (one part) |

**Never open a prompt with:** apply/use, compare, predict, sketch. They are glossary words that open no part in 2020–2025. **Their skills stay in scope**: prediction (B6, Annexe A (j)), comparison (A1–A2) and application (B throughout) are practised through the objectives that require them, asked with words the papers use ("suggest what will happen", "distinguish between", "explain").

## 3. Answer shapes

**No mark scheme exists, so no official marking rule may be stated.** Marking guidance is written from the syllabus objectives, the observed tariffs and the examiner evidence, labelled proposed. `curriculum/answer-shapes.json` records tariff behaviour only. The parts each guidance must name are in `subject-profile.yaml -> answer_structures`.

| command, marks | how a proposed answer is built |
|---|---|
| define 2 | the term and its defining feature; where the syllabus gives the definition, its own words |
| state 1, name 1 | one precise element |
| identify 2, describe 2 | two separate creditable points, each its own line |
| outline 3, list 3, label 3 | three points, or three named parts |
| explain 2, suggest 2 | a cause and its effect, or a reasoned answer to new material: two points |
| discuss 3 | points on both sides, or a chain of three linked points |
| calculate 2 | the method or working, then the answer with its unit (or as a ratio) |
| complete 2, plot 5, draw 5 | table entries with units in the headings; a graph with labelled axes and units, or a genetic diagram with every line |
| multiple-choice set | one mark per question; every distractor is a named error |

## 4. Card types, assessment objectives and Bloom levels

Each slot declares its subtype, AO and Bloom level. The explicit proposed demand audit in `planning/ao_demand_audit.json` governs the AO after the base build; `planning/apply_ao_demand_audit.py` applies it and records the mandatory demand/conditions on each slot. Taught explanation and comparison are A. B requires genuine information processing or reasoning; supplied data and unfamiliar context are not universal prerequisites. C requires an actual C1–C5 practical demand. Command words and subtype names do not decide the AO. Conditional classifications must be checked against each authored prompt.

| subtype | tests | permitted AOs | Bloom level | slots |
|---|---|---|---|---:|
| DEF | A term defined in the syllabus sense | AO1 | Remember | 69 |
| FEATURE | Named parts, features, functions or facts; on a practical objective, the apparatus or reagent | AO1, AO3 | Remember | 210 |
| PROC | An ordered sequence: a biological process, or the steps of a practical procedure | AO1, AO3 | Understand | 114 |
| MECH | A full account of a taught multi-step mechanism, every step in order with its cause and effect | AO1, AO2 | Understand | 19 |
| DIST | The feature that separates two confusable things | AO1, AO2 | Understand | 9 |
| WHY | The reason for an outcome, a step or a condition | AO1, AO2, AO3 | Understand | 91 |
| CHAIN | A reasoned explanation of a taught relationship, each link stated (Understand: it reproduces a taught account; applying it to a new case is the APP card) | AO1, AO2 | Understand | 51 |
| APP | Taught biology applied to a situation the learner has not met (B7); on a practical objective, knowledge applied to interpret an unfamiliar experiment (C4); also producing a labelled drawing from a specimen or image, and constructing a key | AO1, AO2, AO3 | Apply | 154 |
| CALC | A calculation with working and units | AO2, AO3 | Apply | 19 |
| INTERP | Reading, completing, plotting or concluding from a table, graph or diagram | AO2, AO3 | Analyse | 27 |
| LIM | A source of error or limitation in a method, and an improvement tied to it | AO3 | Evaluate | 44 |
| EVAL | A judgement weighed from both sides, for an objective that is itself two-sided | AO1, AO2, AO3 | Evaluate | 7 |
| SYNTH | A complete investigation plan: what is changed, measured and kept the same, how, and repeats (devising a procedure) | AO3 | Create | 30 |
| MISCON | An examiner-evidenced confusion, discriminated | AO1, AO2, AO3 | Understand | 27 |

Performance tasks: multiple_choice_set = Apply; short_answer = Analyse; practical_task = Evaluate.

**"Discuss" is not one shape.** The syllabus defines Discuss as "a critical account of the points involved" (printed p.39). In the papers, 6 of the 7 "discuss" parts ask for developed points ("discuss two effects", "discuss how ... may affect"); one asks for advantages and disadvantages. So an objective that is itself two-sided ("advantages and disadvantages", "arguments for and against") gets an EVAL card weighed to a judgement (Bloom Evaluate). Every other "discuss" objective gets a CHAIN card worded "discuss": developed points, each with its consequence, with no for/against frame (Bloom Understand; its APP card carries the application). Bloom levels follow the thinking the card demands: a CHAIN card reproduces a taught account, so it is Understand, not Analyse.

Objective types (from `planning/build_registry.py`, verb-first, with 59 recorded overrides): bio_definition 69, bio_relationship 66, bio_process 65, bio_concept 56, bio_structure 52, bio_causal 51, bio_function 36, prac_investigation 30, task_mechanism 19, prac_mmo 18, bio_quantitative 15, prac_analysis 12, prac_presentation 10, bio_comparison 9, bio_application 8, bio_evaluation 7, task_drawing 5, task_drawing_interp 4, task_genetics 3, prac_conclusion 2, prac_trend 1, prac_quantitative 1, task_key 1.

## 5. The topics

| topic | title | papers | objectives | items | notes words (operative) | contract formula (superseded) |
|---|---|---|---:|---:|---|---|
| 1 | Scientific processes | 1/2/3 | 55 | 109 | 5,630–8,730 | 14,170–20,350 |
| 2 | Classification and diversity of living organisms | 1/2/3 | 20 | 26 | 1,270–2,030 | 5,020–7,230 |
| 3 | Organisation and maintenance of the organism | 1/2/3 | 284 | 484 | 26,140–41,200 | 68,960–99,160 |
| 4 | Development of the organism and the continuity of life | 1/2/3 | 105 | 156 | 11,060–17,440 | 25,520–36,700 |
| 5 | Relationship of organisms with one another and with their environment | 1/2/3 | 76 | 111 | 6,700–10,640 | 18,260–26,250 |

**5 topics, 540 objectives, 886 items (871 flashcards, 15 performance tasks), 50,800–80,040 words of notes.**

**The notes budget is set per syllabus bullet, not per objective** (`curriculum/notes-budget.json`, model in `planning/notes_budget.py`). The contract formula (`build/make_contract.py:34`, 230–470 words for every registry objective by exposure class) pays once per member of every split bullet; the revised model gives each bullet a band for what it asks (recall 60–100 words, description 120–180, explanation or practical 180–280), 30–50 for each extra member of a split bullet, and 50–90 per unit. Total 50,800–80,040 words, against 131,930–189,690 from the formula; 9702 Physics has 54,270–77,720. **The budget is a ceiling, not a target**: a unit that teaches its objectives in fewer words is finished, with a one-line note in `authoring_notes.json` if it falls below the minimum (C-26 warns, it does not fail); a unit that needs more says why there. The operative figures are written into every work order and contract by `planning/apply_notes_budget.py` (the formula's figure is kept as `word_budget_superseded`); `planning/check_unit_budgets.py` confirms each content unit declares it. The representative section, `exemplar/REPRESENTATIVE-SECTION.md`, is 3.3.2 and 3.3.3 in full: 1,985 words of notes for 10 objectives and 25 cards and tasks.

Each topic carries content objectives (Papers 1 and 2) and practical objectives (Paper 3), so every topic gets a multiple-choice set, a structured question and an Alternative-to-Practical task. Topic 3 has 284 objectives and 484 items, so it is authored in four groups of whole content units (`planning/topic3_groups.json`): 3A Cells, movement across membranes, biological molecules and enzymes (3.1, 3.2, 3.3.1, 3.3.2, 3.3.3, 3.4, 3.5); 3B Nutrition in plants and humans (3.6, 3.6.1, 3.6.2); 3C Transport in plants and animals, defence, gas exchange (3.7, 3.8.1, 3.8.2, 3.8.3, 3.9); 3D Respiration, excretion, co-ordination and homeostasis (3.10.1, 3.10.2, 3.11, 3.12, 3.13.1, 3.13.2, 3.13.3, 3.14). Each group writes its own unit and item files and stages its claims; the lead merges the claims and checks the topic as one.

**How the 364 syllabus bullets became 540 objectives.** 80 bullets that list separately assessable members were split into one objective per member (`planning/decomposition.json`), each tied to its verbatim bullet in `curriculum/objective_registry.planning.json` and linked to its siblings through `related_ids`; lists that only qualify one skill were left whole, with reasons recorded. **Teaching dependencies**: 21 recorded (`planning/dependencies.json`), written into `prerequisite_ids` on 237 objectives; the author of a dependent unit links to its prerequisite and uses its terms rather than re-teaching it. One crosses topic order: "chromosome" is defined in 4.4.1 but used from 4.1, so 4.1 defines it on first use and links forward.

### Complete tasks for the demanding skills

The 4–6 mark parts in 2020–2025 are investigation plans, genetic diagrams, keys, drawings, graphs and multi-step mechanisms. Each has a complete task, with its marks taken from the papers (evidence per objective in `planning/objective_overrides.json`):

| skill | objectives | the task | marks |
|---|---:|---|---:|
| Plan an investigation (investigate, design, plan) | 30 | one coherent plan: changed, measured, kept the same, method, repeats (SYNTH, describe), plus a limitation card | 5 |
| Construct and use a dichotomous key | 1 | construct a key (APP, construct) and use one to identify several organisms (INTERP, identify) | 4 + 4 |
| Produce a labelled drawing from a specimen, slide or image | 9 | a complete labelled drawing (APP, draw), plus an explanation where the objective says interpret | 4 |
| Monohybrid crosses | 3 | a full genetic diagram with the calculation (CALC, draw), plus why the ratio arises | 5 |
| Multi-step mechanisms | 19 | a short recall card plus a full account in order (MECH) | 4 |

**Practical objectives: what a written resource can and cannot cover** (`curriculum/practical-coverage.json`). Of 83 practical objectives, 52 have a hands-on component ("design and carry out", "make temporary slides", "use and manipulate a light microscope"). The cards cover what Paper 3 (Alternative to Practical) tests: planning, the procedure, readings, interpretation and limitations. None of them is evidence that the learner carried the practical out; the map records the hands-on part as not covered. It needs the school laboratory.

### Visual bank: exact figures and delivery still under review

**Preparation, approval and delivery remain separate.** *prepared* means located, stored and mapped; *approved* means scientific accuracy and reuse terms have been checked; *delivered* means shown on a real learner card and tested. The originally banked 254 assets have operator approval at their recorded hashes; newer item-specific graphs do not. No asset has completed scientific verification. Current YYeni connector contracts expose card-side image IDs and an image-attachment action, but image display, learner drawing or image submission and multi-mark guidance have not been tested in the actual interfaces. A located or mapped candidate never fulfils a visual requirement.

- **Graphs** come from `planning/make_graphs_6116.py`, which reuses the matplotlib approach of `publish/cie-0455-igcse-2026/diagrams/make_diagrams_0455.py`. Each graph has a question variant (no answer marked) and an answer variant. Data are declared in the script as learner readings, a model curve or published figures; published figures are flagged for verification.
- **Micrographs and anatomical images** are authentic, never generated. They are searched for in the local notes and the assessment corpus first, then on Wikimedia Commons (CC0, public domain, CC BY or CC BY-SA only). Local-note and exam images stay reference only: their rights are unknown, and exam figures show which views are examined but are never reproduced. Web originals and their Commons metadata are fetched with the shared harvester (`harvest run`); the log is in `_harvest/logs/`.
- **Variants.** Originals are never edited. `planning/make_visual_variants.py` writes a teaching variant (syllabus terms), a question variant (neutral letters) and an answer variant (letters plus key) from label positions in `planning/visual_labels.json`. Each label records whether its placement is confident or uncertain. Scale bars are kept. A wrong or doubtful scale is flagged, and covered in variants only where it would mislead.
- **Gaps are tracked per need.** A stimulus objective needs a teaching image, a question image, an answer image and an unfamiliar example: a second, different specimen. A model-drawing objective needs a model drawing and its criteria; a photograph does not substitute. Images whose identity or content is in doubt are held and do not count. A text description never completes a visual objective.

Bank now: 258 asset records (web 233, local_notes 10, original_graph 15), 317 stored files. Of 158 requirement × kind bindings: every need has a candidate (unreviewed) 76, partial 54, GAP 28. Of 350 individual needs: candidate (unreviewed) 228, variant to prepare 76, GAP 46. **Operator-approved image assets: 254. Completed scientific verifications: 0. Requirements met: 0.** Details: `visuals/INDEX.md`; integrity check: `planning/check_visual_bank.py` (integrity only, not approval).

Register: 109 objectives; visual kinds overlap: 54 stimulus images, 74 teaching diagrams, 11 model drawings and 19 graphs. Requirement IDs are stable (`VIS-6116-<objective>`). The authored draft has 35 image-dependent items under `visuals_pending`; six have exact draft graph pairs in `planning/figure_item_candidates.json`, but none is delivered or released.

### Scientific sources and verification

The syllabus and the corpus set scope and demand; they do not supply the science. `planning/references.json` lists the approved references: NSSCO Biology Syllabus, NIED 2018 (6116) (official curriculum document); OpenStax, Biology 2e (Clark, Douglas, Choi), 2018, updated (Verify exact edition and component terms before reproduction; no blanket clearance for visual reuse); OpenStax, Concepts of Biology, 2013, updated (Verify exact edition and component terms before reproduction; no blanket clearance for visual reuse); Cambridge IGCSE Biology 0610 syllabus, 2026-2028 (public syllabus document). The school's NIED-approved textbook is to be named by the operator; the third-party notes in `Revision Notes/` are not approved factual references, but may be inspected for reference-only visual candidates with rights recorded. Every substantive claim carries at least one evidence entry (source, a locator such as chapter.section, support type); a claim with no suitable reference says so and goes to the verifier as teacher knowledge. **Verification**: a qualified Biology teacher named by the operator (not the authoring agent, not the step-6 reviewing agent), after the step-6 cross-vendor review and before release to learners; recorded per topic in `topics/<T>/verification.json`. It is kept outside the claim ledger because check C-24 fails any claim marked verified before review and the standard defines no post-review state (a framework finding). **Release rule**: publish_subject.py may build the package once checks pass; the package is not released to learners until every topic's verification.json covers all its substantive claims with no rejected claim outstanding, and every visual it depends on has passed its acceptance check. In the exemplar, 29 of 36 claims cite an approved reference; the rest are practical procedures flagged for the verifier. Proposed marking guidance is never evidence and is never presented as the board's.

## 6. AO balance, in marks

**The basis is the unrounded aggregate of planned marks**: every slot at its tariff, split across its AOs, plus each performance task at the marks of the paper part it models, summed over the subject before any rounding.

| AO | planned (exact) | stated weight | gap | derived final-grade share (reference) |
|---|---:|---:|---:|---:|
| AO1 (A) | 57.59% | 47% | +10.59 | 50% |
| AO2 (B) | 15.70% | 28% | -12.30 | 30% |
| AO3 (C) | 26.71% | 25% | +1.71 | 20% |

Largest gap: **12.30 points** (AO2), OUTSIDE the 5-point tolerance, over 2,029 marks-equivalent. `curriculum/ao_coverage.md`, which the build writes from per-topic rounded figures, reads 12; the exact figure above is the one this plan answers to. Labels were corrected by the demand audit, without targeting the balance: `top_up` is empty, counts/tariffs are unchanged and the gap is reported without tuning.

**AO approach approved by Lotto; boundary cases retained.** A includes a taught causal account, familiar comparison or rehearsed implications (syllabus PDF p.38, A1–A4). B covers information handling (B1–B4), reasoned explanation, inference, prediction and problem solving (B5–B7). The syllabus does not require supplied data or an unfamiliar context in every B task; distinguish actual reasoning from reproduction of taught accounts. A new name/place alone is insufficient. C requires practical operation/planning, observations/data or method evaluation (PDF p.39, C1–C5). AO and Bloom remain separate axes.
Examples: explain why a plant cell in pure water does not burst = A; infer an isotonic concentration interval from new gain/loss readings = C4 when assessing practical-data interpretation (B3/B4 in a non-practical data task); reason from supplied parental genotypes and sampling uncertainty = provisional B; reproduce a taught 3:1 explanation = A. The genetics WHY slots do not move with the taught WHY/CHAIN accounts. A mitochondria/adaptation APP exemplar is corrected to A because it rehearses a taught relationship.
The audit records 871 slots, 146 changed AO labels since the original generated work orders, and 4 explicitly ambiguous slots. Generic taught EVAL comparisons are A following the operator corpus review. Breastfeeding study explanations and recognition of standard genetic ratios remain explicitly A/B debatable. A later review of the authored prompts decided 41 AO/Bloom/command-word cases, recorded in `planning/post_authoring_label_decisions.json` and `review/POST-AUTHORING-LABEL-DECISIONS-2026-10-19.md`. This corrects labels to demand; it does not establish sufficient reasoning breadth or difficulty. `curriculum/ao-demand-rollup.json` stores rational mark totals. Lotto approved the full plan on 2026-10-18 with the coverage-first approach recorded.

## 7. Misconceptions, glossary and scope

- **27 examiner-evidenced misconceptions** in `curriculum/misconceptions.json`, each on its objective with a `discriminating_test`. Every entry has its own MISCON slot (`misconception_entry`). All 27 are authorable: none awaits a teacher. Three flagged on 2026-10-18 were resolved the same day (MISCON-6116-013 settled by reading the source question; 019 and 038 discriminate without the detail the evidence lacks); two carry an `authoring_constraint` that the MISCON card must respect.
- **30 glossary terms** in `curriculum/glossary.json`, each with its settled sense; 17 use the syllabus's own definition word for word.
- **7 scope patterns** in `curriculum/scope-scan.json`, one per limit the syllabus states, carried by every contract as `excluded_constructs`; C-11 fails any learner-facing match. Each was tested against text it must catch and required text it must leave alone:
  - full names of DNA bases (syllabus, printed p.12, 3.4)
  - roles of water potential and hydrostatic pressure in tissue-fluid exchange (syllabus, printed p.18, 3.8.2)
  - kidney structure and nephron detail (syllabus, printed p.21, 3.11)
  - detail of the pancreatic cells that secrete insulin (syllabus, printed p.23, 3.14)
  - stages of mitosis and meiosis (syllabus, printed p.24, 4.1)
  - mechanism detail of how meiosis produces variation (syllabus, printed p.24, 4.1)
  - endosperm production and seed development detail (syllabus, printed p.25, 4.2.2)

## 8. Rules particular to this subject

- **Teach in the notes, retrieve on the cards.** Each content unit opens with a Key points block (block type `summary`) that states the essential knowledge visibly, usually as a table. Full explanations live in the notes. A card's canonical answer is the shortest complete answer that earns its marks: roughly one short sentence per mark, plus any data. Use a table wherever it removes repetition (one table for the 13 classification groups, not 13 paragraphs). Say a mechanism once, in its own unit, and link to it elsewhere.
- **Definitions are the syllabus's.** Where the syllabus says "define X as ...", the notes and the DEF card use that definition; the glossary marks which.
- **Names exact and spelt correctly.** Structure names (oesophagus, alveoli, xylem, phloem, chloroplast) are given exactly and drilled; imprecise or misspelt terms are the most frequent loss.
- **Cell words and solution words.** Turgid, flaccid and plasmolysed describe cells; hypertonic, isotonic and hypotonic describe solutions.
- **Data conventions (Annexe B).** Table headings and axes as quantity / unit (time / s), the independent variable on the x-axis, points as crosses or encircled dots, a graph headed dependent against independent.
- **Calculations.** Show the working, then the answer with its unit (a ratio has none). Write each step as "a × b = c" or "a ÷ b = c" with c unrounded, because C-32 recomputes it. Magnification: convert to the same unit before dividing; the answer has no unit and is written ×.
- **The syllabus misprints one equation** (`planning/syllabus_errata.json`). 3.6.1.3 prints "6HO2"; the correct equation is 6CO2 + 6H2O → C6H12O6 + 6O2 (light, chlorophyll), verified against the Cambridge 0610 syllabus. Use the correct one and do not draw attention to the misprint.
- **Accurate at syllabus level.** Simplify, but never into something false: simple diffusion needs no transport protein, but water also crosses through water channel proteins; carrier proteins use energy from respiration directly or indirectly; water potential depends mainly on concentration and also on pressure; water crosses a root through cells and along cell walls.
- **Say how sure a cause is.** Where a prompt does not establish a cause, the answer says "one likely reason" or "if ..." and the guidance accepts the other plausible reasons. A control is accepted only if the method in the prompt states it.
- **Plasmolysis means the membrane leaves the wall.** Credit requires the cell membrane (with the cytoplasm) pulled away from the cell wall; "flaccid" or "shrunk" alone does not earn it.
- **Genetic diagrams in text.** Lines in order: parental phenotypes, parental genotypes, gametes, offspring genotypes, offspring phenotypes and ratio. A grid may be a markdown table.
- **Visuals.** No hand-drawn ASCII pictures and no code fences (C-41). Data go in markdown tables. Acquire existing or original assets into `visuals/`, preserving provenance and proposed bindings. Candidate, approved and learner-delivered are separate states. Register requirements in `curriculum/visual-requirements.json`; until the correct variant is reviewed and deliverable, the item names its figure and is held back.
- **Practical data are ours.** Readings in a practical task are invented, realistic and consistent with the biology, and introduced as a learner's results.
- **Namibian context where it does work.** Use local organisms and settings when the situation needs one (pearl millet, quiver trees, a flooded field); do not add place names that carry nothing. Money in N$ where it appears. Teaching of human inherited conditions is done with sensitivity (syllabus note, 4.4.2).
- **No board marking claimed.** Guidance is our proposed marking. Never write "examiner" or "mark scheme" in learner-facing text, and never claim what a paper contains (C-10).

## 9. Open issues carried into authoring

1. **Recall ceiling denominator undefined.** "not more than 24% recall" has no stated denominator. No interpretation is adopted and no item count is derived from it.
2. **Paper 1 duration unconfirmed for 2026.** The syllabus says 45 minutes; the 2025 paper says 1 hour. Needs NIED/DNEA. No learner-facing text states a Paper 1 duration.
3. **Visual preparation and delivery** (section 5): 109 objectives have pending visual coverage/review. Assets can be acquired now; shared-build integration and YYeni image display/submission remain separate delivery requirements. Affected items remain held until reviewed and deliverable.
4. **Verification needs people.** The operator names the verifying Biology teacher and the school textbook (SRC-SCHOOL). Nothing is released to learners before verification (section 5).
5. **Exposure covers Papers 2 and 3 only.** Paper 1 (30% of the qualification) is not mapped. There are 339 direct mapped records and 2 exceptions among 341 original parts. Pesticide uptake remains unresolved; extinction is a definition/context-only record, not habitat-destruction evidence. Neither exception counts as direct exposure. The five originally flagged mappings have targeted Codex review, not a claim that the whole map has independent approval.
6. **No mark schemes.** All marking guidance is proposed; the step-6 reviewer and the verifier read it as such. The mined question records were repaired on 2026-10-18 (full references, opening command words; `assessment-evidence/GAPS.md`).
7. **Sources.** Available sources are inventoried (`curriculum/source-inventory.json`): the syllabus, 18 question papers and six examiner reports, 2020–2025; no mark scheme exists for any series. The step-1 checkbox records that state rather than "complete".
