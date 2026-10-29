# NSSCO Geography 6137 — corpus analysis, 2020–2024

Step 3. Owner: Vitalis P Haupindi. Miner: Codex. Target examination: 2026. Prepared 29 October 2026.

Provenance throughout: **syllabus** means a transcribed requirement; **corpus** means an observation from the available papers/reports; **judgement** means our interpretation or proposed teaching response. This is an internal evidence report, not learner-facing material or a resource plan.

## 1. The corpus

**Corpus:** 15 question papers, five annual examiner-report Geography sections, 535 terminal marked allocations and 1,375 offered marks. All three papers are represented in each year 2020–2024. Every marked allocation has a linked report block. 546 report blocks are preserved; 533 have question links, with the rest retained as paper-level guidance. 428 allocations have classified weakness evidence.

**Syllabus first:** the full 46-page 2016 syllabus was read at Step 2. Vitalis confirmed its AO/paper tables before this analysis. Official qualification AO weights remain A 30%, B 41%, C 17%, D 12%. The grid’s per-paper cells are marks, not percentages. The three-paper route totals 200 marks.

**Supplementary year guidance:** follow the later circular confirmed by Vitalis: 2026 Paper 3 physical context **Coastal/Marine Processes**, human context **Leisure and Tourism**. The historical syllabus rotation ends in 2024 and is not evidence for a guessed repeat cycle.

**Maps:** matching 2021 Mossel Bay, 2022 Parys, 2023 Tulbagh and 2024 Lüderitz sheets were recovered and checked. The 2021 original sheet was found in a legacy 4332 folder; its title/year/features, rather than its filename, establish the match. The 2020 Amersfoort sheet remains missing. Maps remain internal assessment evidence, not learner reproductions.

**Unavailable:** 2025 assessment sources and standalone mark schemes. Examiner reports include answer lists and some explicit allocations, but full scheme coverage is not claimed. Twenty curated credit-shape records cover 26 marked allocations; other `creditworthy_points` arrays remain empty. See `assessment-evidence/GAPS.md` for consequences and source caveats.

**Extraction and audit:** pypdf plain and layout extraction was used because Poppler is absent. A separate pdfplumber pass reconciles every bracketed mark and printed question total across all 15 PDFs. Selected ambiguous pages were rendered with PDFium and inspected. `extraction-manifest.json` records exact source paths, hashes and Geography-only report page ranges. `verification-6137.json` records the independent numerical/source checks.

## 2. What each paper looks like

| Paper | Syllabus structure | Observed demands and tariffs |
|---|---|---|
| 1 | 2 hours; 75 marks; 37.5%. Six 25-mark questions: choose one from each of three sections. | Physical, economic/resources and population/settlement. Short identification/definitions, comparisons, resource descriptions, causal explanations, named examples and judgement. Observed allocations 1–7 marks. |
| 2 | 1 h 45; 65 marks; 32.5%. All questions. | Compulsory 1:50 000 SADC topographic map plus graphs, tables, photographs and other resource questions. Observed allocations 1–5 marks. Map Q1 is 25 marks in 2020–2023 and 22 in 2024. |
| 3 | 2 hours; 60 marks; 30%. Two compulsory investigations, one physical and one human. | Methods/equipment, safety, sampling, recording sheets, statistics, graphical completion, hypotheses, evidence-based conclusions and evaluation. Observed allocations 1–6 marks. It is not all AO D: the official split is A12/B12/C12/D24. |

**Important choice denominator:** each Paper 1 offers 150 marks, but a learner answers 75. Across the corpus, P1 offers 750, P2 325 and P3 300 marks. The sum of offered marks is 1,375, not the 1,000 marks a learner would answer across five complete routes. Never use offered-mark totals as the qualification’s AO weights.

**2024 shift:** every P1 question has the same observed allocation sequence: 1, 3, 4, 5, 3, 4, 5. Each ends with a five-mark “How far do you agree…” task. These are six judgement opportunities across the choices, with three answered by each learner. Earlier papers repeatedly use named case-study endings and some 6/7-mark explanation/comparison tasks. Prepare both formats; five past years do not guarantee a future template.

**P2 variation:** 2020 and 2024 have seven questions; 2021–2023 have six. The mapwork share falls from 25 to 22 in 2024. Direction of travel, coordinates with seconds, scale conversions, area, gradient and evidence-based interpretation are all represented, though not every skill appears every year.

**P3 contexts observed:** 2020 rivers/settlements; 2021 coasts/settlements; 2022 weather/tourism; 2023 rivers/settlements; 2024 coasts/settlements. The 2021 split is 31/29 marks, not 30/30; the other four are 30/30. For the adopted 2026 focus, 2021 and 2024 coastal investigations and 2022 tourism give especially relevant demand evidence, while other years demonstrate transferable enquiry skills.

| Series/paper | Marked allocations | Offered marks | Marks by question |
|---|---:|---:|---|
| 6137-2020-P1 | 49 | 150 | Q1: 25, Q2: 25, Q3: 25, Q4: 25, Q5: 25, Q6: 25 |
| 6137-2020-P2 | 34 | 65 | Q1: 25, Q2: 6, Q3: 8, Q4: 8, Q5: 7, Q6: 6, Q7: 5 |
| 6137-2020-P3 | 25 | 60 | Q1: 30, Q2: 30 |
| 6137-2021-P1 | 48 | 150 | Q1: 25, Q2: 25, Q3: 25, Q4: 25, Q5: 25, Q6: 25 |
| 6137-2021-P2 | 31 | 65 | Q1: 25, Q2: 8, Q3: 8, Q4: 8, Q5: 8, Q6: 8 |
| 6137-2021-P3 | 24 | 60 | Q1: 31, Q2: 29 |
| 6137-2022-P1 | 40 | 150 | Q1: 25, Q2: 25, Q3: 25, Q4: 25, Q5: 25, Q6: 25 |
| 6137-2022-P2 | 35 | 65 | Q1: 25, Q2: 8, Q3: 8, Q4: 8, Q5: 8, Q6: 8 |
| 6137-2022-P3 | 26 | 60 | Q1: 30, Q2: 30 |
| 6137-2023-P1 | 43 | 150 | Q1: 25, Q2: 25, Q3: 25, Q4: 25, Q5: 25, Q6: 25 |
| 6137-2023-P2 | 44 | 65 | Q1: 25, Q2: 8, Q3: 8, Q4: 8, Q5: 8, Q6: 8 |
| 6137-2023-P3 | 25 | 60 | Q1: 30, Q2: 30 |
| 6137-2024-P1 | 42 | 150 | Q1: 25, Q2: 25, Q3: 25, Q4: 25, Q5: 25, Q6: 25 |
| 6137-2024-P2 | 40 | 65 | Q1: 22, Q2: 7, Q3: 8, Q4: 7, Q5: 7, Q6: 7, Q7: 7 |
| 6137-2024-P3 | 29 | 60 | Q1: 30, Q2: 30 |

## 3. Command words actually used

The table counts **one primary assessed opening/operation per marked allocation**, after separating source carriers and contextual statements from actual instructions. Shared instructions are inherited by separately marked response slots. Compound operations remain compound. Counts therefore total 535; these are not counts of every verb occurrence, and secondary requirements still matter. For example, a named-case task can open with “Name” and also require description/explanation. The complete audited stem remains in its evidence record.

A raw token search initially found background words such as “complete the Project”, “high water mark” and “figures show”. These were rejected as commands by reading the demand. Recorded overrides are reproducible in `planning/build_analysis_6137.py`. Objective mapping itself never used a token-matching baseline.

| Primary operation/form | Allocations | Modal tariff(s) | Tariffs observed | Paper counts (1/2/3) |
|---|---:|---|---|---|
| add | 2 | 1, 2 | 1, 2 | 0/1/1 |
| calculate | 12 | 1 | 1, 2, 3, 4, 5 | 3/5/4 |
| compare | 9 | 4 | 2, 3, 4, 6, 7 | 5/2/2 |
| complete | 29 | 2 | 1, 2, 3, 6 | 1/13/15 |
| define | 10 | 1 | 1, 2 | 6/3/1 |
| describe | 107 | 3 | 1, 2, 3, 4, 5, 6, 7 | 56/35/16 |
| describe and explain | 8 | 5 | 3, 4, 5 | 6/0/2 |
| describe and suggest | 1 | 3 | 3 | 1/0/0 |
| design | 1 | 3 | 3 | 0/0/1 |
| determine | 1 | 2 | 2 | 0/1/0 |
| discuss | 1 | 5 | 5 | 1/0/0 |
| discuss how far you agree | 6 | 1 | 1, 2 | 0/6/0 |
| distinguish | 2 | 3 | 3 | 2/0/0 |
| do the results support | 1 | 2 | 2 | 0/0/1 |
| do you accept or reject | 1 | 2 | 2 | 0/0/1 |
| do you agree | 1 | 2 | 2 | 0/0/1 |
| do you think | 1 | 4 | 4 | 0/0/1 |
| draw | 4 | 2, 4 | 2, 4 | 0/0/4 |
| estimate | 3 | 1 | 1 | 2/0/1 |
| explain | 55 | 5 | 1, 2, 3, 4, 5, 6 | 39/5/11 |
| find and calculate | 1 | 2 | 2 | 0/1/0 |
| give | 18 | 2 | 1, 2, 3, 4, 5, 6 | 7/9/2 |
| how | 8 | 2 | 1, 2, 3, 4 | 1/5/2 |
| how far do you agree | 6 | 5 | 5 | 6/0/0 |
| identify | 33 | 1 | 1, 2, 4 | 7/25/1 |
| identify and describe | 3 | 3 | 3 | 3/0/0 |
| label | 2 | 1 | 1 | 0/0/2 |
| list | 1 | 2 | 2 | 0/0/1 |
| mark | 1 | 1 | 1 | 0/1/0 |
| measure and calculate | 1 | 3 | 3 | 0/1/0 |
| name | 38 | 1 | 1, 2, 3, 4, 5, 7 | 24/13/1 |
| name and describe | 1 | 3 | 3 | 0/0/1 |
| name and explain | 2 | 4 | 4 | 2/0/0 |
| outline | 1 | 2 | 2 | 0/0/1 |
| plot | 4 | 2 | 1, 2, 3 | 0/1/3 |
| rank | 1 | 1 | 1 | 0/0/1 |
| select | 1 | 2 | 2 | 0/1/0 |
| shade | 3 | 1 | 1 | 0/1/2 |
| show | 1 | 1 | 1 | 0/1/0 |
| state | 21 | 1, 3 | 1, 2, 3, 5 | 4/11/6 |
| suggest | 66 | 2 | 1, 2, 3, 4, 5, 6, 7 | 25/17/24 |
| tick | 3 | 1 | 1, 4 | 0/2/1 |
| what | 43 | 1 | 1, 2, 3, 4, 6 | 17/15/11 |
| which | 14 | 1 | 1, 2, 3, 4 | 4/7/3 |
| write | 7 | 2 | 1, 2, 4, 6 | 0/2/5 |

**Printed rows without an observed credited operation in this coding:** Annotate; Contrast; Demonstrate; Devise or Plan; Differentiate; Factor; Feature; Illustrating your answer; Locate; Match; Pattern; Reasons; Refer to or with reference to; Study; Use or using the information provided; With the help of information in; What differences; Where; Why.

This list includes glossary nouns and source-carrier phrases; it does not mean words such as Study or Use never appear anywhere in a paper. They frequently introduce resources. `command-word-verdicts.json` records a verdict for all 38 mixed glossary rows and permits only listed observed forms. Synonyms in a combined row are not automatically licensed: observing Explain does not license Account for. Additional genuine forms outside the printed glossary, including outline, plot, rank, design and judgement questions, are explicitly recorded from the papers.

**Teaching judgement:** the dominant demands are description, suggestion and explanation, with low-tariff identification/calculation and higher-tariff contextual development. “Describe why” in 2024 still requires reasons. A command word alone cannot decide the rubric or Bloom level.

## 4. What a creditable answer looks like

**Evidence boundary:** this section is supported by examiner-report allocation guidance, not by standalone mark schemes. It provides representative, task-specific structures; it is not a complete marking specification for all 535 allocations. The 20 structured shapes carry exact linked question/report IDs.

- **Compare:** make linked comparisons of the same variable and support them with suitable data where asked. Two independent lists or a table of copied figures do not necessarily perform comparison. Examples: 2022 P1 Q3(a)(ii), six marks; Q6(b), four marks; 2021 P3 Q2(c)(i), four marks.
- **Explain:** name the relevant factor/process, then show how it produces the stated effect in this context. The 2021 P1 Q4(b)(i) report caps bare lists at two out of seven; the 2022 vegetation task caps description at three out of five. These are observed caps, not universal rules.
- **Named examples:** 2021 floodplain guidance reserves a mark for the name in isolation; 2022 rainforest guidance gives no separate name mark, but limits a non-specific answer to three. Teach a small stock of accurate, developed examples and match the actual task. Do not promise a mark simply for naming a place.
- **Judgement:** 2024 P1 reports reserve four marks for judging relevant facts and one for a decision, which may be implied. Reciting a process and appending “I agree” is insufficient. This is not a mandatory equal-sided essay format.
- **Calculations:** show a suitable method and units. The 2024 map-distance report separates measurement, conversion and final distance; area requires dimensions, calculation and square units. However, the 2024 HIV calculation explicitly allows full marks for a correct answer without working, despite the prompt requesting working. Do not invent a global working-mark rule.
- **Map evidence:** pair service with its mapped evidence when requested. Use the actual key and area. Bearings depend on the stated origin and destination. The disputed 2024 bearing is quarantined as a source conflict, not used as a verified worked value.
- **Fieldwork methods:** name the actual equipment and describe how it obtains the required measurement. A description of longshore drift is not a method to investigate its direction. Give repeatable positions, readings, recording and controls appropriate to the task.
- **Hypotheses:** give a conclusion consistent with the observed variable, back it with the requested data and acknowledge exceptions where relevant. The 2023 river pollution task distinguishes judgement/decision from evidence. The two-mark land-use task gives no separate mark just for agree/disagree. A stock “one conclusion mark plus data” rule is unsafe.
- **Evaluation:** connect a specific limitation to a workable improvement. The 2021 six-mark traffic conclusion requires both hypotheses, supporting evidence and critical method evaluation; the 2022 four-mark weather improvement task explicitly allocates one mark to each of four specified demands.

## 5. Where the marks fall

The table is computed using **one primary content/skill context per allocation**, so its columns reconcile to 750/325/300. It is an allocation convention, not an official board topic weighting. Mixed questions may test more than one content outcome; secondary tags remain in the evidence. P3 marks are assigned to their investigation context, while integrated enquiry outcomes are counted in exposure separately. P2 topographic Q1 is assigned to map skills, even when interpreting agriculture or settlements.

| Topic/context | P1 offered /750 | P2 /325 | P3 /300 |
|---|---:|---:|---:|
| 1.1 The Earth’s structure | 49 (6.5%) | 16 (4.9%) | 0 (0.0%) |
| 1.2 Weathering and Erosion | 40 (5.3%) | 6 (1.8%) | 0 (0.0%) |
| 1.3 River processes | 24 (3.2%) | 21 (6.5%) | 60 (20.0%) |
| 1.4 Wind/Aeolian processes | 30 (4.0%) | 0 (0.0%) | 0 (0.0%) |
| 1.5 Coastal/Marine processes | 20 (2.7%) | 8 (2.5%) | 61 (20.3%) |
| 1.6 Weather and Climate | 50 (6.7%) | 21 (6.5%) | 30 (10.0%) |
| 1.7 Climatic regions and natural vegetation | 37 (4.9%) | 19 (5.8%) | 0 (0.0%) |
| 2.1 Industrial system | 50 (6.7%) | 0 (0.0%) | 0 (0.0%) |
| 2.2 Agriculture | 50 (6.7%) | 16 (4.9%) | 0 (0.0%) |
| 2.3 Leisure and tourism | 25 (3.3%) | 13 (4.0%) | 30 (10.0%) |
| 2.4 Energy sources | 53 (7.1%) | 21 (6.5%) | 0 (0.0%) |
| 2.5 Utilisation and management of water resources in Namibia | 22 (2.9%) | 17 (5.2%) | 0 (0.0%) |
| 2.6 Utilisation and management of wildlife animals in Namibia | 50 (6.7%) | 0 (0.0%) | 0 (0.0%) |
| 3.1 Population Studies | 109 (14.5%) | 34 (10.5%) | 0 (0.0%) |
| 3.2 HIV and AIDS | 25 (3.3%) | 0 (0.0%) | 0 (0.0%) |
| 3.3 Settlement Studies | 116 (15.5%) | 9 (2.8%) | 119 (39.7%) |
| 4.1 Research skills | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| 4.2 Map reading skills | 0 (0.0%) | 124 (38.2%) | 0 (0.0%) |

`exam-exposure.json` computes exposure for 140 source specific-objective bullets plus two cross-cutting aims: 73 high-exposure entries and 33 unprobed entries. High means an observed tariff of at least five, or appearances in at least three annual series. Mid means maximum three/four marks in fewer than three series; low means maximum one/two marks in fewer than three series. These thresholds are **judgement**; the underlying counts are **corpus**.

**Observed in four or five annual series (source-bullet resolution):** 1.1.09, 1.3.02, 1.5.06, 1.6.04, 2.4.02, 2.5.05, 3.1.09, 3.3.03, 3.3.04, 3.3.05, 3.3.06, 4.1.03, 4.1.06, 4.1.07, 4.1.08, 4.2.03, 4.2.04, 4.2.05, 4.2.07. The catalogue supplies their verbatim source descriptions.

**Unprobed source outcomes/aims in this mapping:** 1.1.01, 1.1.02, 1.1.05, 1.1.06, 1.3.09, 1.5.01, 1.5.02, 1.5.03, 1.5.08, 1.5.10, 1.6.01, 1.6.07, 1.7.06, 2.1.04, 2.1.07, 2.1.10, 2.2.03, 2.2.05, 2.2.06, 2.2.11, 2.3.01, 2.3.04, 2.3.07, 2.4.04, 2.4.05, 2.4.07, 2.5.02, 2.5.03, 3.1.08, 3.1.11, 4.1.01, 4.1.05, 4.2.06. No such outcome may be deleted from the plan. A compound bullet hit is not proof that all nested examples were tested. The two aim-level mappings prevent falsely treating coastal opportunities as beach formation or coastal climate impacts as wildlife questions.

**2026 priority is not historical frequency:** allocate extra enquiry practice to the confirmed coastal/tourism contexts, sustain mapwork and retain the full P1/P2 syllabus. Four older settlement investigations do not make settlements a prescribed 2026 P3 topic.

## 6. How candidates lose marks

The following are recurring patterns, not candidate-level rates. Reports provide qualitative comments; no reliable denominator of candidate responses is available.

| Failure evidenced in reports | Examples / PDF pages | Resource response (judgement) |
|---|---|---|
| Give unpaired descriptions or copy data instead of comparing. | 2020 P1 Q1(a)(iii), p323; 2021 P3 Q2(c)(i), p343; 2022 P1 Q3(a)(ii), p393; 2024 P1 Q4(b)(i), p480. | Short paired-comparison tasks using the same variable and correct units/data; separate a pattern statement from evidence. |
| List a factor without its causal effect. | 2021 P1 fishing-location Q4(b)(i), p330; 2022 P1 vegetation Q1(b)(ii), p389; tourism-infrastructure Q3(b)(i), p394. | Factor → mechanism → effect, applied to the actual location or issue. |
| Describe a process when the question asks for visible features, evidence or reasons. | 2022 P1 Q2(b)(i), p391; 2024 P1 freeze-thaw source task Q1(b)(i), p469. | Mix matched prompts on the same original stimulus: describe features, explain formation, identify supporting evidence. |
| Ignore a named example or give generic knowledge without place detail. | 2020 P1 coastal case Q2(c), p326 and pollution Q3(c), p328; 2022 P1 rainforest Q1(c), pp389–390. | Case-study teaching units with location, process, effect and relevant supporting detail; avoid an isolated place-name card as the whole preparation. |
| Use the wrong statistic, graph axis, scale or unit. | 2022 P3 Q1(b)(i), p412; 2024 P2 distance/area, pp489–490; climate statistics, pp494–495. | Work through range/mean/total separately, practise interpolation and scale conversion, retain units and reasonable tolerances. |
| Substitute general knowledge for the particular map/photo/table. | 2021 P2 map irrigation, p335; 2023 P2 map farming/relief, pp483–484; 2024 P1 traffic photo, pp483–484. | Require a visible evidence cue with each inference; use original maps with keys, not memorised answers about a town. |
| Name equipment or a method without explaining its use. | 2021 P3 beach profile, p341; 2022 P3 sampling, p415; 2024 P3 beach measurements, p507 and urban methods, p521. | Sequential method cards plus practice designing a workable procedure; explain positions, measurements and recording. |
| Repeat a hypothesis without a defensible conclusion or relevant paired data. | 2021 P3 conclusion, p344; 2022 P3 tourism hypotheses, pp416–417; 2023 P3 water quality, pp497–498; 2024 P3 coastal conclusions, pp509–511. | Decide using the observed data, show a relevant pair, test an exception, then conclude at the strength the evidence supports. |
| Give a generic problem or repeat it instead of evaluating the method. | 2021 P3 Q1(f), p342; 2023 P3 Q1(f)(i), pp496–497 and Q2(f), pp503–504; 2024 sampling task, pp507–508. | Match limitation → effect on results → practical improvement. Distinguish precision, bias, representativeness and reliability in context. |
| Confuse the requested category: economic/social/environmental, causes/effects, physical/human, age structure/total growth. | 2020 ageing Q5(b)(i), p330; 2022 eruption economic effects, pp408–409; 2024 fishing/wildlife/HIV tasks, pp475–486. | Contrasting original scenarios that differ only in the requested category; require an explicit consequence rather than a vague label. |

## 7. Curated misconceptions

`curriculum/misconceptions.json` contains **27 conceptual confusions**, each with source finding IDs, mapped objectives, PDF locators, an explicit distinction and a proposed discriminating card demand. Examples include weathering versus erosion; freeze-thaw versus exfoliation; abrasion versus attrition; basin versus divide; erosion versus transport; relief versus drainage; cultivation versus irrigation; ageing versus overpopulation; urbanisation versus migration; mean versus range; and pollution score versus water quality.

Missing units, weak comparisons and unsupported hypotheses remain exam-skill findings rather than being padded into this register. A report’s “wrong answer” can be geographically true but irrelevant to the task: a definition of carbonation does not answer an evaluation of where it occurs. Such cases must not become cards claiming that the definition is false.

AIDS/HIV and antiretroviral-treatment confusions are evidenced, but final learner medical wording must be checked against appropriate primary health sources at authoring. This register specifies what needs distinguishing; it is not permission to copy an official answer list.

## 8. Scope and source safeguards

`curriculum/scope-scan.json` contains **13 context-sensitive review rules**, one for every Step 2 source limit, with must-catch and must-leave examples. Patterns flag potentially wrong claims for review; they do not invent blanket exclusions.

- Keep Theme 4 integrated into physical, economic and population/settlement teaching.
- The P2 map is a 1:50 000 SADC topographic extract with a full key. Prior knowledge of the mapped town is not required, but relevant topic knowledge is applied.
- P2 cross-sections are interpreted rather than constructed. This does **not** ban P3 river-channel cross-section completion (2023) or beach-profile plotting (2024).
- Use equal units in gradient calculations. Mapwork answers depend on map evidence.
- The syllabus statement about plotting with provided axes does not establish a global ban on explaining how to choose axes/scales. Similarly, simple photograph-description scope does not erase other analytical resource questions.
- Named case studies are not restricted to the illustrative list in the syllabus; a question asking for an example still needs one.
- The historical rotation cannot establish 2026 topics. Use the separately recorded operator-confirmed circular.

`assessment-evidence/source-conflicts-6137.json` preserves eight source caveats: numbering, a conflicting 2024 bearing, conditional solar statements, ozone/greenhouse wording needing verification, an inconsistent report allocation for humidity, a mixed vegetation-adaptation context, a questionable map-specific tourism answer, and gradient answer units. The five Step 2 glossary/content flags also remain open. Original source files are untouched. Resolve affected facts before final learner wording; no disputed numeric/map answer is presented as verified.

## 9. What this means for the plan

1. **Retain all syllabus outcomes.** Use exposure to calibrate practice, never to remove unprobed material. Preserve the source-bullet IDs or record an explicit crosswalk if the planner decomposes them.
2. **Prepare the actual three-paper route.** Preserve Paper 1 choice across all three sections, all-question Paper 2 skills and the Paper 3 balance of knowledge, analysis, judgement and investigation.
3. **Prioritise the adopted 2026 P3 contexts.** Coastal work needs safe profiling, equipment use, pebble selection/measurement, longshore-drift investigations, graph interpretation, conclusions and method evaluation. Tourism needs question design, suitable sampling, local/visitor perspectives, seasonal/economic/environmental impacts, data presentation and evidence-based conclusions.
4. **Reserve genuine visual tasks.** Maps with a usable key/scale, contour/coordinate/bearing exercises, process diagrams, profiles, climographs, population pyramids, pie/bar/line/scatter/dispersion plots and isolines need original, readable stimuli. Some tasks require learners to draw or label; do not reveal the answer in a question image. The demand list is not yet an approved image/card count.
5. **Teach developed, named content.** Explicitly include the causal links, specific terminology, relevant examples and category distinctions the examiners credit. Avoid abstract templates that omit named teaching points.
6. **Plan notes as a real teaching text.** Every flashcard answer and worked result must be recoverable from the notes; methods need usable sequences and limitations, not short equipment lists.
7. **Choose item types by demand.** Combine concise retrieval cards with supported explanations, resource analysis, calculations, drawing/plotting practice, case-study application and judgement. AO and Bloom labels remain different axes.
8. **Make source uncertainty visible.** Resolve disputed definitions and scientific/map facts with primary evidence before authoring. Keep missing schemes and map limitations attached to affected rubrics. Never rerender a report list as unquestioned learner truth.
9. **Specify independent review.** Deterministic source/mark reconciliation does not prove that semantic mappings, diagram interpretations or learner explanations are correct. Later cross-review must inspect them.

**Checkpoint:** Step 3 evidence and report are written. Vitalis’s “analysis read” checkpoint remains open. No plan, contracts, work orders, notes, cards, publication, upload, Git commit or push has been performed in this step.

## Evidence and regeneration

- Sources: `source-inventory.json`; `assessment-evidence/extraction-manifest.json`.
- Full stems/records: `assessment-evidence/assessment_evidence.json`.
- Full report blocks, mappings and categories: `assessment-evidence/examiner-findings.json`.
- Source outcome catalogue and computed exposure: `curriculum/mining-objectives.json`; `curriculum/exam-exposure.json`.
- Operations/verdicts: `curriculum/command-word-observations.json`; `curriculum/command-word-verdicts.json`.
- Curated credit structures/confusions: `curriculum/answer-shapes.json`; `curriculum/misconceptions.json`.
- Scope/caveats: `curriculum/scope-scan.json`; `assessment-evidence/GAPS.md`; `assessment-evidence/source-conflicts-6137.json`.
- Rebuild parsed allocations: `python3 work/nam-6137-nssco-2026/planning/mine_corpus_6137.py` (add `--extract` only to refresh both pypdf extraction modes).
- Rebuild analysis artefacts: `python3 work/nam-6137-nssco-2026/planning/build_analysis_6137.py`.
- Reconcile independently: `python3 work/nam-6137-nssco-2026/planning/verify_corpus_6137.py`.
- Render this report: `python3 work/nam-6137-nssco-2026/planning/render_corpus_analysis_6137.py`.
