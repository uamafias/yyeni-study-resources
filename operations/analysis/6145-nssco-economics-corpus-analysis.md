# Corpus analysis — 6145 NSSCO Economics

28 October 2026. Owner: Vitalis P Haupindi. Miner: Codex. This is step 3 evidence for the 2026 learner resources; it is not an authoring plan or learner-facing text.

## 1. The corpus

The 2018 NIED syllabus was read first and its assessment tables were confirmed by Vitalis before this analysis. All held Economics question papers and Economics sections of the five annual reports were then read in plain and layout extraction. Poppler/pdftotext is unavailable on PATH, so pypdf supplied both views; selected diagrams and tables were rendered with PDFium. No other subject was mined.

| Year | QP parts, Paper 1 | QP parts, Paper 2 | Report PDF pages (one-based) |
|---|---:|---:|---|
| 2020 | 34 | 23 | 141–154 |
| 2021 | 32 | 23 | 131–144 |
| 2022 | 32 | 19 | 159–176 |
| 2023 | 32 | 23 | 173–193 |
| 2024 | 29 | 24 | 171–187 |

**271 independently tariffed parts; 1,000 marks offered; 800 candidate marks across five annual series.** Every Paper 1 reconciles to 40 + 40 = 80. Every Paper 2 reconciles to six offered questions of 20 = 120; the candidate answers compulsory Q1 plus three of Q2–Q6 = 80. The latter distinction is preserved in all exposure figures.

The reports contain answers and marking guidance; they are **not standalone mark schemes**. 259 parts have a report-supported credit-shape record; 12 parts in 2020 Paper 1 Section B have performance comments without complete per-part answer grids. 269 question-specific performance-comment records are retained (including positive observations); 610 sentence spans are indexed, not claimed as independent mistakes. 182 question parts link to a recorded weakness. One report paragraph covers both 2021 Q11 parts, and displaced 2021 comments are remapped semantically with the original reference preserved.

No 2025 papers/reports, standalone mark schemes or grade-threshold tables were found. Covers state the year, not an examination month; series are not labelled October/November without evidence. Six QP filenames from 2021–2023 say First Proof and cannot be certified final from filenames. Exact paths and hashes are in assessment-evidence/sources.json; limitations are in assessment-evidence/GAPS.md.

## 2. What each paper looks like

- **Paper 1, 2 h 30 min, 80 marks:** Section A is compulsory short response, 40 marks, using 1–3-mark parts. Definitions, precise distinctions, classifications, formula recall, simple calculations and diagram reading appear. Section B is compulsory applied/data-response work, 40 marks, normally two cases. Context interpretation, economic mechanisms, diagrams and extended judgements are required. The split between the two cases varies: 23/17 in 2020, 20/20 in the later held papers.
- **Paper 2, 2 h, 80 candidate marks:** Q1 is a compulsory 20-mark case; the remaining five 20-mark questions are optional, of which three are answered. Structured essays combine short knowledge elements with longer analysis/evaluation. Seven-mark parts recur; compulsory tasks can reach nine marks. Draw-and-explain tasks recur on demand/supply and government intervention. Students need to follow the choice instructions as well as the economics.

| Paper/section | Independently tariffed parts | Tariffs seen, with counts |
|---|---:|---|
| Paper 1, A | 116 | 1m × 41; 2m × 66; 3m × 9 |
| Paper 1, B | 43 | 1m × 2; 2m × 11; 3m × 2; 4m × 7; 5m × 2; 6m × 6; 7m × 8; 8m × 5 |
| Paper 2, A | 20 | 1m × 1; 2m × 1; 4m × 9; 5m × 3; 7m × 4; 9m × 2 |
| Paper 2, B | 92 | 2m × 10; 3m × 10; 4m × 14; 6m × 13; 7m × 44; 8m × 1 |

These are counts of tasks offered, not how many a learner attempts. Source: all ten question papers, checked against every printed tariff token.

## 3. Command words actually used

Counts below use one primary opening per tariffed part. Context or “Except…” prefaces are ignored, Using is normalised to Use, and “To what…” is classified with What. **Use-prefaced compound instructions retain their embedded verbs separately**, so Calculate at 2 marks, for example, is evidenced within such instructions even though the primary-opening Calculate row below has 1 and 5. All embedded verbs, tariffs and evidence IDs are in assessment-evidence/command-word-analysis.json. Interrogative frames are listed separately; their presence does not create a missing official definition.

| Syllabus-table word | Primary count | Modal tariff(s) | Primary-opening tariffs and counts |
|---|---:|---|---|
| Explain | 30 | 2 | 2m × 12; 3m × 2; 4m × 6; 6m × 3; 7m × 7 |
| Describe | 24 | 2 | 1m × 1; 2m × 9; 3m × 4; 4m × 3; 6m × 4; 7m × 3 |
| Define | 20 | 2 | 1m × 4; 2m × 13; 3m × 1; 4m × 2 |
| Identify | 19 | 1 | 1m × 9; 2m × 3; 3m × 4; 4m × 2; 6m × 1 |
| Discuss | 16 | 7 | 4m × 1; 6m × 3; 7m × 10; 8m × 2 |
| Outline | 11 | 2, 4 | 1m × 1; 2m × 4; 3m × 1; 4m × 4; 6m × 1 |
| Evaluate | 10 | 7 | 5m × 2; 7m × 5; 8m × 2; 9m × 1 |
| State | 9 | 2 | 1m × 1; 2m × 6; 4m × 1; 6m × 1 |
| Analyse | 4 | 7 | 7m × 4 |
| Give | 4 | 2 | 1m × 1; 2m × 2; 4m × 1 |
| Justify | 4 | 7 | 5m × 1; 7m × 2; 8m × 1 |
| Calculate | 3 | 1 | 1m × 2; 5m × 1 |
| Suggest | 2 | 6, 7 | 6m × 1; 7m × 1 |

**All 13 words from section 10 are observed. None is listed-but-unobserved in this corpus.**

| Other observed directive | Primary count | Modal tariff(s) | Tariffs seen |
|---|---:|---|---|
| Name | 14 | 2 | 1, 2, 3, 4, 6 |
| Use | 13 | 7 | 1, 2, 3, 4, 7 |
| List | 10 | 2 | 2, 3, 6 |
| Assess | 7 | 7 | 4, 6, 7, 9 |
| Consider | 6 | 7 | 5, 7, 8 |
| Write Down | 4 | 2 | 1, 2 |
| Comment | 3 | 2 | 2, 7 |
| Examine | 3 | 7 | 7 |
| Advise | 1 | 7 | 7 |
| Distinguish | 1 | 4 | 4 |
| Illustrate | 1 | 7 | 7 |
| Indicate | 1 | 1 | 1 |
| Mention | 1 | 1 | 1 |
| Show | 1 | 2 | 2 |

Interrogative openings: how (8); is (1); what (21); when (1); which (6); who (1); why (11).

Draw is observed as an embedded instruction, notably 2022 Paper 2 Q4(b); it must not be presented as an observed primary opening in these counts. Before slot generation, the framework must preserve the distinction between a complete compound instruction and an isolated verb/tariff. A word from another qualification is not evidence for this one.

## 4. What a creditable answer looks like

The following architectures are paraphrased from the reports’ answer/guidance columns and performance comments; exact wording is not supplied for reuse.

- **Short definitions:** include the features that distinguish the term. The 2024 report distinguishes total income from income per head (P1 Q19, PDF p.175), and requires active willingness/ability to find work in unemployment (P2 Q5(a), p.184). Do not assume an example earns full definition credit.
- **Lists versus developed descriptions:** six marks can ask for six items or three developed features. 2021 P2 Q2(a), report p.138, caps bare feature names at three of six marks. Conversely 2022 P2 Q3(a), p.170, asks for six growth motives. Tariff alone does not decide the structure.
- **Calculations:** give the requested method, substitution, magnitude and unit. Elasticity is not a percentage; a percentage change is. The 2021 P1 Q25(a) report (p.135) explicitly records loss of marks for a percent sign on the final elasticity. The 2023 population calculation needs a consistent persons/millions unit (P2 Q1(c), p.181). Source arithmetic anomalies are quarantined.
- **Diagram with analysis:** multiple tasks use a 4-mark diagram plus a 3-mark explanation, e.g. 2020 P2 Q1(b), report p.146, and 2024 P2 Q1(c), pp.179–180. Label axes, curves, original and changed positions; use the correct curve/control and connect the written mechanism to the diagram. A binding minimum wage/maximum price does not itself shift the curves.
- **Diagram-only and mixed tasks:** 2022 P1 Q26(b), report p.164, awards four marks for the diagram and no unrequested explanation. 2022 P2 Q4(b), p.172, combines a quota definition and a diagram within seven marks. Do not impose a 4+3 model on these.
- **Analysis:** show the relevant change and causal links to the specified actor/outcome. 2023 P2 Q3(b), report p.186, concerns saving, not a generic discussion of cheaper borrowing. 2024 P2 Q6(b), p.186, requires two developed causes and penalises a static statement where a change is asked for.
- **Evaluation and decisions:** two-sided “whether/always” tasks need developed opposing considerations; recent report guidance often reserves a distinct conclusion/decision. 2023 P2 Q2(c), p.185, and Q5(c), p.190, state this. In 2024 P2 Q2(d), p.181, a one-sided answer is capped at four of seven. However 2021 P2 Q1(c), p.138, is a focused five-mark evaluation of employment consequences; 2024 P2 Q1(d), p.180, is a five-mark subsidy justification. Do not add a compulsory counterargument/conclusion mark where the source does not require one.
- **Multiple components/enquiry:** 2021 P1 Q24(c), report p.134, requires stock-exchange functions and economic effects, rather than a generic pros/cons debate. 2023 P1 Q25(d), p.178, requires questions to investigate economic costs, not statements about accidents. 2023 P2 Q2(a), p.184, requires the link between productivity and profit as well as the definitions.

The generated curriculum/answer-shapes.json records 13 families and task-specific allocations. They are planning guidance, not a universal mark scheme. Assessment AO labels on individual evidence records are explicitly judgement unless the source states them; component percentages remain the syllabus values.

## 5. Where the marks fall

Every part was mapped by reading its actual assessed meaning and the case context. No token-matching first pass was used, so there is no fabricated count of mappings corrected from such a pass. A cross-topic part has one primary owner for mark-share arithmetic; secondary links count for exposure without double-counting marks. This is an analytic allocation convention, not an official topic weighting.

| Syllabus topic | Primary marks offered | Share of 1,000 offered marks | Annual series represented |
|---|---:|---:|---|
| 3.2 Market forces | 93 | 9.3% | 5 |
| 6.2 Government economic policies | 82 | 8.2% | 5 |
| 8.1 Population | 64 | 6.4% | 5 |
| 2.3 Financial institutions | 61 | 6.1% | 5 |
| 9.1 Conflicts | 54 | 5.4% | 5 |
| 7.2 Employment | 50 | 5.0% | 5 |
| 1.2 Types of economic systems and economic resources | 44 | 4.4% | 5 |
| 7.1 Prices | 44 | 4.4% | 3 |
| 2.1 Business organisations | 40 | 4.0% | 5 |
| 5.2 Productivity | 39 | 3.9% | 4 |
| 8.2 Living standards | 39 | 3.9% | 4 |
| 6.3 Government control | 38 | 3.8% | 5 |
| 6.1 Government as producer and employer | 36 | 3.6% | 4 |
| 5.4 Economies and diseconomies of scale | 34 | 3.4% | 4 |
| 2.2 Trade unions and employer association | 33 | 3.3% | 4 |
| 4.2 Earnings | 30 | 3.0% | 4 |
| 5.3 Production costs and revenue | 30 | 3.0% | 5 |
| 3.3 Price elasticity | 25 | 2.5% | 5 |
| 7.4 International trade | 25 | 2.5% | 4 |
| 4.3 Expenditure | 24 | 2.4% | 3 |
| 1.1 Basic economic problem: scarcity and exercise of choice | 21 | 2.1% | 5 |
| 5.1 The private firm as producer and employer | 20 | 2.0% | 4 |
| 1.3 Specialisation and division of labour | 18 | 1.8% | 5 |
| 7.3 Output | 16 | 1.6% | 3 |
| 3.5 Policies | 15 | 1.5% | 2 |
| 4.1 Occupational choices | 12 | 1.2% | 2 |
| 3.4 Advertising | 11 | 1.1% | 3 |
| 3.1 What is a market? | 2 | 0.2% | 1 |

At the 96 syllabus-bullet anchors, exposure classes are: core: 22; frequent: 20; unseen: 11; occasional: 25; rare: 18. Here core means 4–5 annual series; frequent 3; occasional 2; rare 1; unseen 0. These thresholds are explicitly calibrated to five years.

Eleven bullet anchors have no observation in this held corpus; they remain mandatory coverage. There is one low-confidence mapping (2021 P1 Q8, e-commerce, not explicitly named in the content outline) and eleven supporting/cross-cutting mappings. Value added, formal/informal firms, WTO and occupational mobility are retained as visibly supporting mappings, not silently promoted into explicit syllabus wording. The planner must decompose listed members and preserve an ID crosswalk from assessment-evidence/syllabus-objective-index.json.

## 6. How candidates lose marks

| Recurring failure | Evidence examples (report PDF pages) | Resource response |
|---|---|---|
| Giving definitions where reasons, applications or methods were asked for | 2020 P1 Q18 p.143; 2023 P1 Q26(b) p.178; 2024 P1 Q10 p.173 | Use contrast tasks: identify the requested operation, then perform it in the new case. |
| Listing without developing the mechanism | 2021 P2 Q4(c) p.141; 2022 P2 Q2(c) p.169; 2024 P2 Q2(c) p.181 | Worked point → reason → economic effect chains, followed by independent short practice. |
| One-sided evaluation, no distinct decision, or mirrored repetitions | 2020 P2 Q1(c) pp.146–147; 2023 P1 Q26(c) p.179; 2024 P1 Q24(d) p.178 and P2 Q4(d) p.184 | Balanced case reasoning where demanded; decisions must add a condition or priority, not repeat a credited point. |
| Missing labels, wrong curve or price-control diagram | 2020 P1 Q23(a)(ii) p.144; 2021 P2 Q1(b) p.137; 2022 P2 Q1(b) p.167; 2024 P2 Q1(c) pp.179–180 | Label-and-complete tasks; discriminate a curve shift from a price ceiling/floor on unchanged curves. |
| Wrong direction or a static factor instead of a change | 2022 P2 Q5(a)/(c) pp.173–175; 2023 P2 Q6(b) p.190; 2024 P2 Q1(a) p.179 and Q6(b) p.186 | State increase/decrease explicitly and trace it to the requested price, quantity or income effect. |
| Wrong actor, level or case; copying an excluded factor | 2020 P2 Q3(b)/(c) p.149; 2021 P1 Q25(c) p.136; 2023 P2 Q6(d) p.192; 2024 P2 Q1(a) p.179 | Case-linked explanations, actor checks, national versus individual specialisation, and “other than” drills. |
| Incomplete definitions or confused neighbouring concepts | 2021 P1 Q17–20 p.133; 2022 P1 Q19–24 pp.160–161; 2024 P1 Q12 p.173 and Q22 p.175 | Discrimination cards and short examples that expose the boundary rather than repeating the definition. |
| Missing formula elements, percent signs or magnitude/units | 2021 P1 Q25(a)(i) p.135; 2023 P2 Q6(a) p.190; 2024 P1 Q17 p.174 | Calculation cards with independent checking of ratio, percentage, currency and persons/millions. |

The individual source comments remain attached to question evidence. Performance-only comments are not counted as misconceptions. Source defects are not treated as learner beliefs.

## 7. Misconceptions

**37 curated concept confusions** are saved in curriculum/misconceptions.json, each with syllabus anchors, source evidence and an original discrimination test. They cover, for example, real/disposable income; average/marginal revenue; social/external cost; absolute/comparative advantage; budget/trade balance; production/productivity; natural/total population change; fiscal/monetary policy; transfer earnings/economic rent; public/free goods; and economic/population growth.

Unemployment classification is conditional on the stated mechanism. The 2022 tourism case asks for structural rather than seasonal unemployment, while the 2023 economy-wide downturn case is marked cyclical. A resource must not teach “pandemic = one universal type”. Neither listing nor omitting units is promoted into a concept-confusion entry.

## 8. Scope and source reliability

The syllabus has no explicit subject-content prohibition of the kind found in some other qualifications. Its positive depth limits require simple market situations/calculations/applications. All seven constraints transcribed at step 2 have corresponding reviewed scan entries and 30 must-catch/must-allow controls in curriculum/scope-scan.json. Patterns catch explicit incompatible instructions only; depth still needs semantic review. No bare marginal-cost, comparative-advantage or economic-rent term is banned: this syllabus/report corpus explicitly supports them.

Fourteen source-anomaly records are saved in assessment-evidence/source-anomalies.json. Material issues include the displaced 2021 P1 performance comments; 2022 public-good and multinational assertions; the reversed 2022 depreciation/imported-inflation mechanism; inconsistent debt/expected-price statements; tariff/band typos; the malformed 2023 population calculation; and 2023 scale/diminishing-returns conflation. The held QP supplies the printed tariff; inconsistent report suballocations are not invented into a clean grid. The syllabus overrides wrong report content. The 2023 supply diagram and the 2022 currency row were visually checked.

## 9. What this means for the plan

1. Cover all 28 topics and every decomposed outcome; reserve additional applied practice for market forces, government policy, financial institutions, population/development, employment and costs/conflicts, without using exposure as a content filter.
2. Preserve the syllabus’s A/B/C labels and its per-paper target percentages. Calculated overall targets are A 39%, B 25.5%, C 35.5%; these are derived from the 50/50 paper weights, not a separate printed qualification table.
3. Include short exact retrieval, discrimination, calculations, diagram construction/reading, data analysis, applied causal chains and task-specific extended judgement. Map Bloom separately from the credited AO.
4. Use observed complete command/tariff forms, including prefaced/compound instructions, and original invented Namibian cases. All thirteen syllabus-table verbs occur; additional examined verbs are retained with evidence rather than guessed.
5. Build genuine misconception slots from the curated register. Put command interpretation, exclusions, units and development practice into the appropriate skill tasks instead of labelling every answering fault a misconception.
6. Keep legal/current institutional statements modest and source-specific; do not turn dated report statements into universal law or live facts. Exact numerical examples and diagrams must be newly worked, checked and internally consistent.
7. Carry the missing standalone schemes, 2020 credit-grid gaps, First Proof status, supporting mappings and source anomalies into the plan/handover. No grade prediction or certainty about the next paper is warranted by this corpus.

Verification: all 15 source hashes reopened; all ten printed tariff sequences independently reconciled; all 269 extracted performance quotes rechecked on their cited report pages; all 96 exposure rows recomputed; all 30 scope controls passed. See assessment-evidence/source-verification.json. This verifies the mining, not later learner content.

**Next YOU checkpoint:** Vitalis reads the paper/command/error summary and confirms that it fits the examination the learners are preparing for. Planning has not started.
