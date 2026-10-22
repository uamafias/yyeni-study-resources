# 8224 NSSCAS Chemistry — corpus analysis (step 3)

Workspace `work/nam-8224-nsscas-2026/`. Written 2026-10-21. Evidence: `assessment-evidence/assessment_evidence.json` (475 records), `curriculum/exam-exposure.json`, `answer-shapes.json`, `misconceptions.json`, `scope-scan.json`. Syllabus facts: `curriculum/syllabus-facts.json`. Every table below is computed from those files by `planning/write_corpus_analysis_8224.py`.

**Read this first: the limits of this evidence.**

- **No mark schemes exist** for 2021–2024 (none in the repo, none in Drive). So nothing here records what was credited. Credited-answer shape comes only from the 32 Paper 2/3 parts the 2025 examiner report describes.
- **The only examiner evidence is the 2025 report.** Its question papers are not held, so its comments were mapped to objectives by inference from the comment itself. 2021–2024 examiner reports do not exist.
- **Proof papers.** 2021–2023 papers are proofs (2023 Paper 3 a second revised proof); 2024 is unlabelled. Wording may differ from the printed exams.
- **Marks I inferred.** In 2024 Paper 2 Question 1(a)–(f) the page prints only a total of 6; the six parts are recorded at 1 mark each by inference.
- **Mapping.** Each part was mapped to syllabus bullets by reading its meaning. A 30-record spot-check found about 27 clearly right, 2–3 arguable, none clearly wrong. All 76 diagram-dependent records were subsequently checked against 46 page images; one locator was corrected and no meaning mapping changed. See `work/nam-8224-nsscas-2026/assessment-evidence/IMAGE-REVIEW.md`.
- **Frequency is not difficulty.** Section 5 is frequency; section 6 is difficulty (2025 only). They are kept apart.

## 1. The corpus

| Source | Used | Notes |
|---|---|---|
| Papers 1, 2, 3 for 2021, 2022, 2023, 2024 | 12 papers: 160 Paper 1 questions, 148 Paper 2 parts (240 marks), 75 Paper 3 parts (160 marks) | Proofs except 2024 |
| NSSCAS Examiners Report 2025, Chemistry 8224 (printed p. 71 onward) | 92 records (40 Paper 1, 32 Paper 2, 20 Paper 3) | Paper 1 keys with percentage correct and comments; Paper 2/3 marking points with commentary; papers not held |
| Set aside | Drive spreadsheets of grade distributions by centre (2024, 2025) | Results data, not question or content evidence |

## 2. What each paper looks like

**Paper 1 (40 four-choice questions, 1 mark each, 1 hour).** Syllabus order is not followed; every year draws from all four themes. Question types by purpose across the four years: recall 62, calculation 23, equation_writing 14, graph 11, diagram 10, data_interpretation 9, structure_drawing 6, application 5. Multiple-choice items carry no command word.

**Paper 2 (60 marks, 1 hour 15, compulsory).** Five or six questions a year. Parts by mark: 1-mark 84, 2-mark 41, 3-mark 19, 4-mark 3, 5-mark 1 (148 parts over four years). Most parts are worth 1 mark; a part above 3 marks is rare. Part types: recall 55, structure_drawing 19, calculation 18, equation_writing 14, data_interpretation 12, diagram 9, application 6, explanation 6. Questions are usually one topic area but often hold parts from other topics (a question on Group 2, for example, can end in a calculation).

**Paper 3 (40 marks, 2 hours, two or three timed experiments).** Experiment topics by year:

- 2021: redox titration: hydrogen peroxide with acidified potassium manganate(VII) (+ Mn2+ test); mass-loss determination of water of crystallisation in hydrated barium chloride; qualitative analysis of two unknown solids Q and R
- 2022: acid-base titration with dilution of hydrochloric acid against sodium hydroxide; calorimetry for CaO and CaCO3 with acid, Hess cycle, error percentage; qualitative analysis of solution F plus planning tests to distinguish ethanol from ethanoic acid
- 2023: titration to find percentage purity of sodium hydroxide; thermometric titration: enthalpy of neutralisation of sulfuric acid with sodium hydroxide, graph; qualitative analysis of four cation solutions F-I
- 2024: rates: iodine clock (hydrogen peroxide, iodide, thiosulfate), graph of rate against volume; qualitative analysis of three solutions E-G (cations and anions) plus sulfate/sulfite solution H

Marks by skill (from the records): 2021: planning 0, collecting 24, analysing 12, evaluating 4; 2022: planning 3, collecting 20, analysing 14, evaluating 3; 2023: planning 0, collecting 16, analysing 20, evaluating 4; 2024: planning 0, collecting 26, analysing 10, evaluating 4. Practical types: titration 20, qualitative_analysis 16, enthalpy_experiment 14, error_evaluation 11, rates_experiment 6, mass_loss_experiment 4, graph_plotting 3, planning 1. The syllabus notes qualitative-analysis notes are supplied with Paper 3, so recall of test results is not the Paper 3 demand; observation, recording and conclusion are.

## 3. Command words actually used

Counts are Paper 2 and Paper 3 parts, 2021–2024 (Paper 1 has none). Raw wordings were normalised to their opening word.

| Opening word | Parts | Tariffs seen (marks: count) | In syllabus glossary |
|---|---:|---|---|
| Calculate | 40 | 1: 30, 2: 6, 3: 3, 4: 1 | yes |
| State | 29 | 1: 24, 2: 3, 3: 2 | yes |
| Practical: record / tests | 22 | 1: 3, 2: 4, 3: 2, 4: 3, 5: 3, 6: 2, 7: 4, 11: 1 | no |
| Explain | 17 | 1: 6, 2: 8, 3: 2, 4: 1 | yes |
| Identify | 17 | 1: 14, 2: 1, 3: 2 | no |
| Give | 16 | 1: 5, 2: 9, 3: 2 | no |
| Write | 13 | 1: 11, 2: 2 | no |
| Suggest | 13 | 1: 10, 2: 2, 4: 1 | yes |
| Draw | 9 | 1: 3, 2: 4, 3: 2 | no |
| Question word | 8 | 1: 8 | no |
| Name | 7 | 1: 5, 2: 2 | no |
| Define | 6 | 1: 4, 2: 2 | yes |
| Describe | 6 | 1: 1, 2: 3, 3: 2 | yes |
| Construct | 4 | 1: 3, 2: 1 | yes |
| Use | 4 | 2: 3, 3: 1 | no |
| Complete | 4 | 2: 1, 3: 2, 5: 1 | no |
| Determine | 3 | 1: 3 | yes |
| Plot | 2 | 3: 1, 4: 1 | no |
| Insert | 1 | 1: 1 | no |
| Find | 1 | 3: 1 | yes |
| Contrast | 1 | 2: 1 | no |

**Listed in the syllabus glossary but not seen in 2021–2024:** Classify, Comment, Compare, Deduce, Discuss, Estimate, List, Measure, Outline, Predict, Sketch, What Do You Understand By / What Is Meant By. Caution: the 2025 report shows Sketch used in 2025 (Boltzmann curve, p orbital, particle paths), so Sketch has 2025 evidence only; and Paper 3 'record / measure' wordings absorb Measure.
**Used in papers but not in the glossary:** Identify, Give, Name, Write, Draw, Complete, Plot, Use, Insert, Contrast, and question words (Which, What, How many). Under the playbook rule these are allowed to open a card because the papers use them; the syllabus words never seen should be allowed only where the plan can cite the evidence.
**Tariff pattern:** Calculate and State are mostly 1-mark; Explain and Give run 2–4; Describe and Draw reach 3; the largest Paper 2 part is 5 marks.

## 4. What a creditworthy answer looks like

**Limited evidence: no mark schemes.** From the 2025 report only (32 parts with a tariff and listed marking points):

- 1-mark parts: 1 listed point(s) in 10 part(s); 2 listed point(s) in 2 part(s); 3 listed point(s) in 2 part(s)
- 2-mark parts: 2 listed point(s) in 11 part(s)
- 3-mark parts: 3 listed point(s) in 2 part(s)
- 4-mark parts: 4 listed point(s) in 1 part(s)
- 5-mark parts: 3 listed point(s) in 1 part(s); 6 listed point(s) in 1 part(s)
- 6-mark parts: 6 listed point(s) in 1 part(s)
- 7-mark parts: 5 listed point(s) in 1 part(s)

(Counts are of listed marking items, not marks: the report sometimes lists alternatives, so a part can show more items than its tariff.)

What the report itself states about answers (paraphrased): (1) Give calculated answers to the number of significant figures the data justify, and say so in the working. (2) Convert cm3 to dm3 before using a concentration or molar volume; use Ar values as printed (24.3 for Mg, not 24). (3) Quote the printed tariff as the guide to how many separate points to make. (4) Use the full term; give both the bond and the wavenumber range for infra-red peaks; draw displayed formulae with every bond, including O-H. (5) Name versus formula: answer in the form asked. (6) Practical: record readings to the burette's precision, put units in column headings, use concordant titres and exclude the rough titre; name an acceptable source of error (apparatus or method, not 'human error' or parallax); say 'soluble' or 'not soluble in excess' when adding excess NaOH or ammonia; draw a conclusion about the ions present.

Marks in calculation parts are shown as separate steps in the report (conversion, substitution, final answer to the right number of significant figures). Whether a 1-mark part wants one point or a point with a reason cannot be settled without mark schemes.

## 5. Where the marks fall (frequency; not difficulty)

Paper 1 questions plus Paper 2 marks, 2021–2024: **400 marks**, each part counted once to its primary topic (a part that tests two ideas is not split). By theme: Theme 1 Particulate nature of matter and stoichiometry 25.8%; Theme 2 Physical chemistry 24.2%; Theme 3 Inorganic chemistry 21.2%; Theme 4 Organic chemistry and analysis 28.8%.

| Topic | Marks | Share | Objectives never named 2021–2025 |
|---|---:|---:|---:|
| 4.2 Hydrocarbons | 47 | 11.8% | 7 of 24 |
| 1.1 Atoms, molecules and stoichiometry | 36 | 9.0% | 0 of 9 |
| 2.3 Equilibria | 36 | 9.0% | 1 of 11 |
| 1.3 Chemical bonding | 28 | 7.0% | 10 of 25 |
| 2.1 Chemical energetics | 26 | 6.5% | 0 of 9 |
| 1.2 Atomic structure | 23 | 5.8% | 3 of 13 |
| 4.5 Isomerism: structural and stereoisomerism | 22 | 5.5% | 0 of 6 |
| 3.2 Group 2 | 19 | 4.8% | 2 of 8 |
| 3.4 Group 17 | 19 | 4.8% | 4 of 13 |
| 2.2 Electrochemistry | 18 | 4.5% | 1 of 10 |
| 3.1 The Periodic Table and chemical periodicity | 18 | 4.5% | 2 of 16 |
| 2.4 Reaction kinetics | 17 | 4.2% | 0 of 9 |
| 3.3 Transition elements | 17 | 4.2% | 4 of 11 |
| 1.4 The ideal gas and real gases and pV = nRT | 16 | 4.0% | 0 of 3 |
| 4.3 Halogen derivatives | 13 | 3.2% | 4 of 9 |
| 4.4 Hydroxyl compounds | 13 | 3.2% | 2 of 8 |
| 3.5 Nitrogen and Sulfur | 12 | 3.0% | 2 of 10 |
| 4.1 Foundations of organic chemistry | 12 | 3.0% | 0 of 5 |
| 4.7 Carboxylic acids and derivatives | 5 | 1.2% | 6 of 10 |
| 4.6 Carbonyl compounds | 3 | 0.8% | 1 of 4 |

Exposure classes over the 213 content objectives (definitions in `exam-exposure.json`): core 70, frequent 8, occasional 36, rare 50, unseen 49. Core plus frequent corresponds to the earlier `probed_high` grouping; occasional plus rare corresponds to `probed_low`. Silence is weak evidence: 213 objectives against about 160 questions and 60 Paper 2 marks a year means most objectives cannot appear in any one year. **Frequency calibrates emphasis; it never removes coverage (RS-05).** The earlier keyword-based count in this workspace is superseded by this one and is not to be quoted.

## 6. How candidates lose marks (2025 report only)

Findings by class (87 statements): omission 37, misconception 25, calculation slip 10, shallow development 9, command-word miss 6.

Hardest 2025 Paper 1 questions (percentage correct; the report gives a percentage for 38 of 40): Q17 17% (2.2.2-05); Q15 24% (2.2.1-05); Q24 28% (3.2.1-04); Q36 32% (4.7.1-05); Q28 34% (3.4.2-01); Q29 35% (3.5.1-01); Q37 36% (4.4.1-06); Q12 37% (2.1.1-05); Q10 38% (1.4-02). Easiest: Q2 82%; Q7 85%; Q31 89%; Q26 89%; Q6 97%.

Recurring failures and what the resource will do about each:

1. **Significant figures, unit conversion and mole calculations** (Paper 2 Q1(b)(ii), Q3(b); most of Paper 3 Q1 and Q2): answers not given to the stated number of figures, cm³ not converted to dm³, wrong Ar (24 for Mg), s.t.p. versus r.t.p. molar volume. *Plan:* calculation cards that require the working, the conversion and the figure count; MISCON cards on 22.4 versus 24.0 and on weighted-mean division.
2. **Practical evaluation and observation** (Paper 3): parallax or 'human error' offered as an experimental error; excess NaOH/ammonia not added or 'soluble in excess' not stated; no conclusion about the ions. *Plan:* practical-skills items, not recall cards; a card family on acceptable error sources and on recording observations.
3. **Boltzmann distribution and rate explanations** (2.4.2): curve confused with an energy profile, area mistaken for Ea, only 'more collisions' given, compromise temperature argued from one side. *Plan:* MISCON cards and explanation items with both-sides answer structure.
4. **Definitions and trend explanations** (3.1.1, 3.1.3): first ionisation energy defined without the ion formed or gaseous states; period trends not linked to nuclear charge and shell. *Plan:* definition cards that name every required element; explain items with claim + reason.
5. **Redox, electrolysis and oxidation numbers** (Paper 1 Q15, Q17, Q28): the lowest-scoring items; the report gives no explanation for the wrong options on Q17 and Q28, so no misconception is claimed for them. *Plan:* items on these objectives; MISCON cards only where an error is stated (nitrate(V) for nitrite).
6. **Drawing and naming organic structures** (4.4.1, 4.5, 4.2.2): O–H bond left out, missing hyphens, primary or tertiary drawn for secondary, double bond kept in a repeat unit, 2-D drawings of enantiomers. *Plan:* structure-drawing items with a displayed-formula discipline.

## 7. Misconceptions

19 entries in `curriculum/misconceptions.json`, each stated by the 2025 report, restated in our words with a discriminating test. All are **single-report evidence** and must retain that provenance; they may guide discriminating practice but must not be generalised as recurring or board-wide patterns. Slips and answering habits were dropped (parallax, 'human error', wrong rounding, item-specific mistakes).

- MC-8224-01 (1.1.5-02): Using the r.t.p. molar gas volume (24 dm3 mol-1) in a calculation set at s.t.p.
- MC-8224-02 (1.1.3-01): Counting the peaks in the mass spectrum of Cl2 as the number of chlorine isotopes.
- MC-8224-03 (1.1.3-02): Dividing the sum of (mass x peak height) by 100 when the peak heights are not percentages.
- MC-8224-04 (1.2.1-01): Giving the electron a relative mass of 0, or 'nil' for a neutron, as if mass and charge were the same thing.
- MC-8224-05 (1.2.1-01): Drawing electrons and protons deflected by the same amount in an electric field.
- MC-8224-06 (1.2.3-07): Writing chromium as 3d4 4s2, following the simple filling order.
- MC-8224-07 (1.2.3-04): Giving how many electrons the s, p and d sub-shells hold when asked how many orbitals of each type are occupied.
- MC-8224-08 (2.2.1-05): Naming NO2- as nitrate(V) because nitrate is the familiar oxyanion of nitrogen.
- MC-8224-09 (1.3.3-02): Treating hydrogen chloride as an ionic compound.
- MC-8224-10 (1.3.4-01): Calling van der Waals forces (or other intermolecular forces) 'bonds' when asked for the bonding in a covalent substance.
- MC-8224-11 (2.4.2-01): Drawing a reaction-pathway (energy profile) diagram when asked for a Boltzmann distribution curve.
- MC-8224-12 (2.4.2-01): Saying the area under the right-hand part of the curve is the activation energy.
- MC-8224-13 (2.4.2-02): Explaining the faster rate at a higher temperature only as 'collisions are more frequent'.
- MC-8224-14 (2.3.1-07): Justifying an industrial temperature by yield alone or by rate alone.
- MC-8224-15 (3.1.3-02): Saying the maximum oxidation number of the Period 3 oxides rises and then falls across the period.
- MC-8224-16 (4.4.1-04): Naming dilute acid as the reagent to dehydrate an alcohol to an alkene.
- MC-8224-17 (4.4.1-07): Describing a positive alkaline iodine test as a colour change in solution.
- MC-8224-18 (4.4.1-07): Naming an iodoalkane such as iodobutane as the compound that forms in the alkaline iodine test.
- MC-8224-19 (4.2.2-09): Drawing the repeat unit of an addition polymer with the C=C double bond still in it.

## 8. Scope

Twelve limits the syllabus states are transcribed with page and verbatim line in `syllabus-facts.json` (`limits`). Ten become draft patterns in `curriculum/scope-scan.json` (nine from stated limits, one inferred exclusion of weak-acid pH calculations, labelled as inferred): how a mass spectrometer works; hybridisation; the relationship between Kp and Kc; quadratic equations in equilibrium calculations; effect of paired electrons on ionisation energy; E/Z priority rules; diastereoisomers; systematic qualitative analysis and traditional separation; ions outside the listed cations and anions; weak-acid pH and acid dissociation constants. Patterns are drafts; C-11 must be run on authored text and narrowed where it flags ordinary text.

One finding for the plan: the 1.2.1 general objective names behaviour in electric fields, but no specific objective does, and a 2025 question tested it. Treat it as examinable, with the evidence.

## 9. What this means for the plan

1. **Coverage is every syllabus objective.** Frequency (section 5) only chooses item types and emphasis.
2. **AO basis must be chosen.** The syllabus prints 40/40/20 percent, while the marks give 35.7/35.7/28.6. The grid splits Papers 1 and 2 equally between A and B; my judgement of the part types gave B-type parts 60% of the Paper 1 and Paper 2 marks (judgement, not syllabus). Decide which basis the AO targets use and say so.
3. **Command words for prompts:** the words with evidence in section 3 (Calculate, State, Explain, Identify, Give, Suggest, Write, Draw, Name, Define, Describe, Construct, Determine, plus Sketch on 2025 evidence). Words never seen should not open a card without a stated reason.
4. **Calculation and practical items are required, not optional.** Sections 4 and 6 show that the lost marks are in working, units, significant figures and practical method; recall cards alone will not move them.
5. **Exemplar slice: topic 1.1 (Atoms, molecules and stoichiometry)** as agreed. It carries the heaviest evidence of lost marks (significant figures, mole and gas-volume calculations, mass-spectrum reading) and 9.0% of Paper 1 and 2 marks. YYeni lesson 6508's objective record is truncated and 1.1 is held in two lessons; cards follow the syllabus bullets, not the broken record.
6. **Evidence gaps to carry into the plan:** no mark schemes; one examiner report; all misconceptions single-source. The diagram gap is closed: all 76 diagram-dependent records were visually checked. Earlier examiner reports or official marking schemes would still strengthen the evidence base if they become available.
