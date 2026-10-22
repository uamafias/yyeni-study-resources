# Approved plan — NSSCAS Chemistry 8224

The brief for authoring the complete learner resource. Drafted 21 October 2026 from the verified syllabus facts, the 475-record local assessment corpus, and the generated topic work orders. The analysis it rests on is `operations/analysis/8224-nsscas-chemistry-corpus-analysis.md`.

Jeremy approved this computed plan on 22 October 2026 after both structural exemplars passed their applicable deterministic checks. Jeremy subsequently authorised the shared-schema extension on the same date; the compatibility issue is resolved.

## 0. What the syllabus says

The governing assessment-objective target is the percentage table printed in the syllabus, not the percentage reconstructed from raw paper marks.

| AO | definition | target | Paper 1 | Paper 2 | Paper 3 |
|---|---|---:|---:|---:|---:|
| A | Knowledge with understanding | 40% | 50% | 50% | 0% |
| B | Handling information, application and solving problems | 40% | 50% | 50% | 0% |
| C | Practical experimental and investigative skills | 20% | 0% | 0% | 100% |

- **Paper 1:** 40 four-choice questions, 40 marks, 60 minutes, 31% of the qualification.
- **Paper 2:** compulsory structured questions, 60 marks, 75 minutes, 46%.
- **Paper 3:** advanced practical skills, 40 marks, 120 minutes, 23%.
- NSSCO Chemistry knowledge is assumed, but this resource introduces each NSSCAS term before relying on it.

## 1. What the corpus says

The local corpus contains 12 question papers from 2021–2024 and the 2025 examiner report: 475 evidence records in total. It contains no official mark schemes. The 2025 report is the only examiner report and its associated papers are not held.

- Paper 1 samples all four themes through recall, calculation, equation-writing, graph, diagram, data-interpretation, structure-drawing and application items.
- Paper 2 is dominated by 1–3 mark parts. It repeatedly requires precise terms, equations and structures as well as calculations and explanations.
- Paper 3 repeatedly requires the learner to collect and present observations or measurements, calculate and interpret results, reach conclusions, and evaluate methods and errors.
- Common losses described in the 2025 report include incomplete definitions, incorrect unit conversions or significant figures, weak working, imprecise observations, weak practical evaluation, and incorrect chemical structures.
- Frequency chooses emphasis and task type; it never removes a syllabus objective.

All 76 diagram-dependent mappings were visually checked against their page images. The remaining evidence limitations are the missing mark schemes, reliance on one examiner report, and single-source misconception evidence.

## 2. Command words and answer shapes

Prompts use words attested in the local papers or syllabus glossary: Calculate, State, Identify, Explain, Give, Suggest, Write, Draw, Describe, Name, Define, Complete, Construct, Use, Determine, Contrast and Find. Sketch is allowed where the 2025 report supplies evidence. Record, Measure, Plot and similar bench instructions belong inside practical tasks rather than standalone recall cards.

| shape | expected response |
|---|---|
| definition or statement | the exact term, required condition and chemically precise wording |
| calculation | relationship or equation, conversion, substitution, working, answer, unit and justified significant figures |
| explanation | claim, chemical reason and consequence; one distinct creditworthy point per mark |
| equation | correct reactants and products, balance, and state symbols where required |
| structure or diagram | the requested representation, complete bonds or labels, and no ambiguous shortcuts |
| data interpretation | identify the feature, use the supplied data, and draw a supported inference |
| practical response | apparatus or method, observations/readings, working, conclusion, error and specific improvement as required |

Because official mark schemes are absent, authoring must not invent board-specific marking rules beyond what the syllabus and 2025 report support.

## 3. Resource package

This is not a flashcard-only build. Each topic produces:

1. a canonical claim ledger, with every taught statement mapped to its syllabus objective;
2. full learner notes/content units, including explanations, worked examples and cross-links;
3. Bloom-labelled flashcards with assessment objective, command word and mark tariff;
4. performance tasks: multiple-choice sets, structured short-answer tasks and multi-step calculations;
5. Paper 3 practical tasks covering titration/volumetric work, thermometric/gravimetric/rates work, qualitative analysis, and planning/evaluation;
6. managed diagrams or bounded data representations where a visual is essential, each human-reviewed;
7. a publish index and manifest after review and approval.

The repaired draft contains **565 flashcards and 66 performance tasks: 631 learning items in total**. The 66 tasks are 20 multiple-choice sets, 20 structured short-answer tasks, 20 calculation tasks and 6 practical tasks. A set counts as one performance-task item; its component questions or parts are counted in its `mark_tariff`, not as separate repository items. Practical coverage now separates acid-base/volumetric titration, redox titration, thermometric/enthalpy work, rates/gravimetric work, qualitative analysis, and planning/evaluation.

## 4. Item types, AOs and Bloom levels

Every item carries `subtype` or `item_type`, `assessment_objectives`, `blooms_level`, `command_word` and `mark_tariff`.

| subtype | purpose | usual Bloom level |
|---|---|---|
| DEF | precise term, law or condition | Remember |
| FEATURE | relevant property, relationship or characteristic | Understand |
| DIST | distinguish confusable ideas | Analyse |
| PROC | ordered chemical or practical procedure | Apply |
| WHY | reason for a condition or step | Understand |
| MECH | mechanism or chemically reasoned process | Analyse |
| CHAIN | trace a change through linked consequences | Analyse |
| APP | apply chemistry to a new situation | Apply |
| CALC | calculate with complete working and units | Apply |
| INTERP | interpret data, a graph, spectrum or representation | Analyse |
| DIAGRAM | draw or complete a structure, apparatus or graph | Apply |
| EVAL | judge evidence, a method or an error | Evaluate |
| SYNTH | join objectives in a multi-step problem | Analyse |

Performance tasks are labelled Apply, Analyse or Evaluate according to the actual demand. Bloom level describes what the learner does; AO describes what the examination credits. Neither substitutes for the other.

## 5. Topic plan

| topic | title | objectives | items | notes words |
|---|---|---:|---:|---:|
| 1.1 | Atoms, molecules and stoichiometry | 9 | 30 | 2,718–3,888 |
| 1.2 | Atomic structure | 14 | 35 | 3,799–5,449 |
| 1.3 | Chemical bonding | 25 | 55 | 6,668–9,556 |
| 1.4 | The ideal gas and real gases and pV = nRT | 3 | 10 | 990–1,410 |
| 2.1 | Chemical energetics | 9 | 26 | 2,679–3,840 |
| 2.2 | Electrochemistry | 10 | 25 | 2,800–4,020 |
| 2.3 | Equilibria | 11 | 29 | 3,239–4,639 |
| 2.4 | Reaction kinetics | 9 | 25 | 2,579–3,699 |
| 3.1 | The Periodic Table and chemical periodicity | 16 | 40 | 4,368–6,268 |
| 3.2 | Group 2 | 8 | 21 | 2,249–3,220 |
| 3.3 | Transition elements | 11 | 25 | 2,789–4,009 |
| 3.4 | Group 17 | 13 | 33 | 3,510–5,026 |
| 3.5 | Nitrogen and Sulfur | 10 | 23 | 2,799–4,010 |
| 4.1 | Foundations of organic chemistry | 5 | 14 | 1,430–2,050 |
| 4.2 | Hydrocarbons | 24 | 60 | 6,399–9,188 |
| 4.3 | Halogen derivatives | 9 | 22 | 2,329–3,339 |
| 4.4 | Hydroxyl compounds | 8 | 24 | 2,320–3,320 |
| 4.5 | Isomerism: structural and stereoisomerism | 6 | 15 | 1,920–2,740 |
| 4.6 | Carbonyl compounds | 4 | 11 | 1,060–1,520 |
| 4.7 | Carboxylic acids and derivatives | 10 | 24 | 2,560–3,670 |
| 5.1 | Advanced practical skills | 39 | 84 | 6,000–8,000 |

**21 topics, 253 assessable objectives, 631 learning items and approximately 65,205–92,861 words of notes.** Topic 5.1 is a resource topic derived from the syllabus Paper 3 criteria, not a new YYeni classroom section. Its 39 criteria are taught through four integrated units rather than 39 repetitive mini-lessons.

The repaired volume is inside the playbook's usual 400–900 range. Topic 1.1 still serves as the structural exemplar before whole-subject authoring.

## 6. AO balance

| AO | planned | syllabus target | gap |
|---|---:|---:|---:|
| A | 44% | 40% | +4 |
| B | 39% | 40% | -1 |
| C | 18% | 20% | -2 |

The largest gap is 4 percentage points across 1,481 marks-equivalent, so the generated plan meets the playbook gate without AO-padding. The bank now follows objective-shaped practice; performance tasks carry integrated exam practice instead of synthetic cards added only to move a percentage. Multiple-choice sets scale from 4 to 12 questions with topic size rather than defaulting to 12 everywhere.

## 7. Evidence, misconceptions and scope

- All 253 assessable objectives receive coverage, including the heading-level electric-field objective in 1.2.1. Objectives not observed in the small paper corpus are still taught and tested.
- Practical exposure figures copied across criteria are broad skill-category planning proxies, not measurements of individual criteria. Direct evidence metadata now reports only records naming the exact objective; the 39 practical criteria have not yet been mapped at that granularity. This limits frequency claims, not syllabus coverage.
- The 19 misconception entries come from the 2025 examiner report only. Each now produces a MISCON slot. They may be described only with their actual provenance (one report, one series), not generalised into claims about recurring board-wide performance.
- Publication follows RS-12: each factual claim is source-backed, externally verified against an approved authority, or transparently derived from verified premises. The playbook does not impose a universal two-source rule.
- The author works from the local source package and derived curriculum files. Do not search the web while writing individual cards.
- Scope exclusions in `curriculum/scope-scan.json` include mass-spectrometer operation, hybridisation, Kp/Kc relationships, quadratic equilibrium solutions, E/Z priority rules, diastereoisomers, traditional systematic qualitative-analysis separation, ions outside the supplied list, and weak-acid pH/Ka calculations.
- The general atomic-structure objective includes particle behaviour in an electric field; the 2025 report confirms that it is examinable even though no narrower specific bullet repeats it.

## 8. Chemistry-specific authoring rules

- Use British English and the syllabus terminology.
- Give formulae, charges, displayed structures, balanced equations and state symbols unambiguously. Use managed visuals when text cannot faithfully represent the assessed structure or apparatus.
- In calculations, show the relationship, conversions, substitution, working, units and significant figures. Distinguish s.t.p. (22.4 dm³ mol⁻¹) from r.t.p. (24.0 dm³ mol⁻¹).
- In definitions, preserve every condition that carries chemical meaning: particles counted, gaseous states, standard states, closed system and equal rates where applicable.
- Practical resources teach performance: measurements and observations, precision, repeats, table headings and units, consistent raw data, graphs, gradients/intercepts, uncertainty, conclusions, errors and specific improvements. Do not reduce supplied qualitative-analysis notes to recall trivia.
- Do not reproduce source-paper wording. Build original questions from objective and evidence patterns.
- Do not make frequency or examiner-behaviour claims in learner-facing content.
- Every generated visual must be viewed by a person before publication.

## 9. Exemplar and approval gate

Build Topic 1.1 first as the structural exemplar. It must include its claim ledger, notes, full item set and performance tasks, then pass the automated checks and Codex inspection. Claude performs the fresh-context cross-vendor review after the complete subject is authored. A knowledgeable Chemistry teacher may also sample it when available, but teacher availability is not a publication prerequisite in the playbook.

No live YYeni curriculum repair, card import, learner assignment or fee is authorised by this draft. Those actions require a separate exact preview and approval.

### Structural validation completed — 22 October 2026

Topic 1.1: 27 claims, five units, 30 items, zero failed checks. Thin practical exemplar: six claims, one 426-word unit, three cards and one 20-mark task, zero failed checks against its five-objective scratch contract. Both reports contain 40 passes, one AO-mix warning and three inapplicable checks. Claims remain unverified and non-publishable pending the required semantic review.

Resolved on 22 October 2026: Jeremy explicitly authorised adding EQUATION and DIAGRAM to both subtype enums in the shared schema. All 51 affected slots retain the approved shapes. Topic 1.1’s temporary EQUATION-to-PROC deviation has been removed; its planned EQUATION subtype is restored. Full authoring can proceed.
