# Plan — Cambridge International AS Level Physics 9702

The brief an authoring agent works to. Generated 29 September 2026 from `work/cie-9702-as-2025-2027/curriculum/` and the topic work orders; regenerate rather than edit. The analysis it rests on is `operations/analysis/9702-as-physics-corpus-analysis.md`.

## 0. What the syllabus says

Transcribed from the syllabus, every value with its page (`curriculum/syllabus-facts.json`).

| AO | definition | weight | Paper 1 | Paper 2 | Paper 3 |
|---|---|---:|---:|---:|---:|
| AO1 | scientific phenomena, facts, laws, definitions, concepts and theories; scientific vocabulary, terminology and  | 40% | 50% | 50% | 0% |
| AO2 | locate, select, organise and present information from a variety of sources; translate information from one for | 40% | 50% | 50% | 0% |
| AO3 | plan experiments and investigations; collect, record and present observations, measurements and estimates; ana | 20% | 0% | 0% | 100% |

- **Paper 1, Multiple Choice.** 40 marks, 75 minutes, 31% of the qualification. Forty multiple-choice items of the four-choice type testing assessment objectives AO1 and AO2. Questions are based on the AS Level syllabus content.
- **Paper 2, AS Level Structured Questions.** 60 marks, 75 minutes, 46% of the qualification. Structured questions testing assessment objectives AO1 and AO2. Questions are based on the AS Level syllabus content.
- **Paper 3, Advanced Practical Skills.** 40 marks, 120 minutes, 23% of the qualification. This paper tests assessment objective AO3 in a practical context. Two questions assess the AS Level practical skills in the Practical assessment section of the syllabus. The content of the questions may be outside the syllabus content.

The command-word table on page 41 lists 15 words for AS and A Level together. Paper 3 is marked by the allocation on page 43: Question 1 (a graph) at least 7 marks for manipulation, measurement and observation, 6 for presentation and 4 for analysis; Question 2 (an inaccurate method to evaluate) at least 5, 2 and 10; 3 marks in each that vary. The syllabus assumes IGCSE-level physics and mathematics.

## 1. What the corpus says

The 12 series examined on the current content, March 2022 to November 2025: 1,099 Paper 1 multiple-choice questions, 978 Paper 2 parts (1,800 marks) and 867 Paper 3 parts (1,938 marks), with their mark schemes and 108 examiner-report sections. The 2020-2021 series were set on the previous syllabus (six of their Paper 2s examine electric fields, now A Level) and are set aside.

- **Papers 1 and 2 examine the same content in syllabus order.** Paper 1 is forty one-mark items; Paper 2 is structured parts of 1-3 marks (99%). Calculate, Determine and Show carry 58% of Paper 2 marks; definitions and statements of laws most of the rest.
- **Calculations are marked in steps.** The equation or the substitution earns a mark before the final answer in 95-100% of 2- and 3-mark Calculate parts; the answer carries its unit. Definitions are marked on their key words (per unit charge, sum of, about the same point, original length, taken to act).
- **Paper 3 credits the same criteria every series,** whatever the experiment: the number and range of readings, quantity / unit headings, consistent raw data, justified significant figures, the graph, the gradient and intercept, a percentage uncertainty, a conclusion against a criterion, and four limitations with four improvements.
- **The failures that recur in every series:** vague explanations; a vector’s sign ignored; rounding too early; the wrong equation, or none; a definition missing its key word; powers of ten lost in a conversion; on Paper 3, vague limitations, inconsistent precision, poor gradients and intercepts, missing units.
- **100 examiner-evidenced misconceptions**, curated by hand from 2,731 error statements, each with a test that separates the two ideas.

## 2. Command words and tariffs

Use only these to open a prompt. The tariff is the one the work-order slot names; every slot tariff is one the papers set for that word.

| command word | in the syllabus table | parts | modal tariff | tariffs seen |
|---|---|---:|---:|---|
| Calculate | yes | 358 | 2 | 1, 2, 3, 4 |
| Determine | yes | 288 | 2 | 1, 2, 3, 4, 5 |
| State | yes | 225 | 1 | 1, 2, 3, 4 |
| Describe | yes | 113 | 4 | 1, 2, 3, 4 |
| Explain | yes | 91 | 1 | 1, 2, 3, 4 |
| Show | yes | 78 | 2 | 1, 2, 3, 5 |
| Estimate | no (observed) | 47 | 1 | 1 |
| Define | yes | 43 | 1 | 1, 2 |
| Justify | yes | 42 | 1 | 1 |
| Sketch | yes | 41 | 2 | 1, 2, 3 |
| Complete | no (observed) | 20 | 2 | 1, 2, 3, 4 |
| Compare | yes | 15 | 2 | 1, 2, 3 |
| Suggest | yes | 7 | 1 | 1, 2, 3 |
| Give | yes | 5 | 1 | 1, 2, 3 |

**Never open a prompt with:** Adjust, Change, Comment, Draw, Identify, Label, Measure, Place, Plot, Predict, Record, Remove, Repeat, Set, Take, Underline, Vary. Comment and Predict are listed for A Level too and open no AS part in 2022-2025; Identify opens three. The bench instructions (Measure, Set, Repeat, Adjust, Change, Record, Place, Take, Vary, Remove, Write) and Plot, Draw, Label and Underline are used by the papers, but only as steps inside a practical task or a short answer: no flashcard opens with one.

- **Definitions** open with "Define" (43 parts) or "State what is meant by" (18); a law or principle with "State the …" (29). All 1-2 marks.
- **Describe has two forms.** On Paper 2 it is 1-3 marks and a card models it at 2 (3 for an experiment or a derivation). On Paper 3 it is 4 marks: four limitations, or four improvements. The Question 2 practical task models that.
- **Justify and Estimate are Paper 3 words,** always 1 mark: justify the significant figures of a calculated value; estimate a percentage uncertainty.
- **Show that** ends with the result to one more significant figure than the value the question gives.

## 3. Answer shapes

From the mark schemes’ award rules (`curriculum/answer-shapes.json`). Write each answer to the shape its tariff carries.

| command, marks | how it is marked |
|---|---|
| Define 1, State 1 | one precise element; a definition earns its mark only with its key words |
| State 2, Explain 2 | two separate creditable points, each its own line |
| Calculate 2-3, Determine 2-3 | in steps: the equation in symbols and the substitution earn marks before the final answer, which carries its unit |
| Show 2 | in steps, and the working must arrive at the given value, stated to more significant figures than given |
| Sketch 2-3 | marked on features: the shape, where the line starts and ends, the key values |
| Justify 1, Estimate 1 (Paper 3) | one reasoned element: the significant figures and why, or the uncertainty and how |
| Describe 4 (Paper 3) | one mark per specific limitation or improvement, each tied to the measurement it affects |
| multiple-choice set | one mark per question; every distractor is a named error |

## 4. Card types, assessment objectives and Bloom levels

Each slot declares its subtype, its AOs (narrowed from the permitted set below by objective type and paper) and its Bloom level.

| subtype | tests | permitted AOs | Bloom level |
|---|---|---|---|
| DEF | A definition, a law or an equation stated precisely, with its symbols and units | AO1, AO3 | Remember |
| FEATURE | The features or properties of something (a particle, a region of the spectrum, a wave) | AO1, AO3 | Remember |
| DIST | The difference between two confusable quantities or terms | AO1, AO2, AO3 | Understand |
| PROC | An ordered sequence: a derivation from definitions, or the steps of an experimental method | AO1, AO2, AO3 | Apply |
| WHY | The reason for a step or a condition (why many oscillations are timed; why coherence is needed) | AO1, AO2, AO3 | Understand |
| MECH | How something happens, explained physically | AO1, AO2 | Understand |
| BEN | An advantage taken to its consequence | AO2 | Understand |
| LIM | A limitation of a procedure, or a source of uncertainty, and what it does to the result | AO2, AO3 | Evaluate |
| APP | The physics applied to a situation the learner has not met: a qualitative prediction or a design | AO2, AO3 | Apply |
| CHAIN | A change traced to its effect through a relationship (double the extension, four times the energy) | AO2, AO3 | Analyse |
| EVAL | A judgement on data or a method: does the evidence support the relationship, and by what criterion | AO2, AO3 | Evaluate |
| CALC | A calculation with the equation, the substitution, the answer, its unit and a sensible number of significant figures | AO2, AO3 | Apply |
| INTERP | Reading a graph, a table, a trace or a circuit: a gradient, an area, an intercept, a value | AO2, AO3 | Analyse |
| MISCON | Telling a correct idea from the error it is confused with | AO1, AO2, AO3 | Understand |
| SYNTH | Two objectives joined in one problem | AO2, AO3 | Create |

Performance tasks: calculation = Apply; multiple_choice_set = Apply; practical_task = Analyse; short_answer = Apply.

## 5. The topics

| topic | title | paper | objectives | items | notes words |
|---|---|---|---:|---:|---|
| 1 | Physical quantities and units | 1/2 | 12 | 59 | 3,500–5,020 |
| 2 | Kinematics | 1/2 | 9 | 64 | 2,760–3,950 |
| 3 | Dynamics | 1/2 | 13 | 52 | 3,910–5,590 |
| 4 | Forces, density and pressure | 1/2 | 13 | 65 | 3,800–5,450 |
| 5 | Work, energy and power | 1/2 | 11 | 71 | 3,210–4,600 |
| 6 | Deformation of solids | 1/2 | 10 | 61 | 3,010–4,310 |
| 7 | Waves | 1/2 | 16 | 69 | 4,840–6,930 |
| 8 | Superposition | 1/2 | 12 | 57 | 3,530–5,060 |
| 9 | Electricity | 1/2 | 15 | 83 | 4,470–6,400 |
| 10 | D.C. circuits | 1/2 | 16 | 89 | 4,510–6,480 |
| 11 | Particle physics | 1/2 | 18 | 55 | 5,390–7,720 |
| 12 | Practical skills | 3 | 40 | 135 | 11,340–16,210 |

**12 topics, 860 items, 54,270–77,720 words of notes.**

## 6. AO balance, in marks

| AO | planned | syllabus weight | gap |
|---|---:|---:|---:|
| AO1 | 37% | 40% | -3 |
| AO2 | 44% | 40% | +4 |
| AO3 | 19% | 20% | -1 |

Topics 1-11 are examined on Papers 1 and 2, which assess AO1 and AO2 equally and no AO3; topic 12 on Paper 3, which assesses AO3 only (syllabus page 14). So a content topic is balanced against 50/50/0 and the practical topic against 0/0/100; the subject total answers to 40/40/20. Every content topic carries a multiple-choice set for Paper 1, a structured question and a multi-step calculation for Paper 2; topic 12 carries four practical tasks, two in the style of each Paper 3 question.

## 7. Misconceptions, glossary and scope

- **100 examiner-evidenced misconceptions** in `curriculum/misconceptions.json`, each on its objective with a `test`. Every entry has its own MISCON slot in the work order (`misconception_entry`).
- **77 glossary terms** in `curriculum/glossary.json`, each with its settled sense.
- **21 scope patterns** in `curriculum/scope-scan.json`, carried by every contract as `excluded_constructs`; C-11 fails any learner-facing match:
  - coefficients of friction or viscosity (syllabus, page 18, 3.2.1)
  - the coefficient of restitution (syllabus, page 18, 3.3.2)
  - deformation in more than one dimension (syllabus, page 20, 6.1.1)
  - the Doppler effect for a moving observer (syllabus, page 21, 7.3.1)
  - an unpolarised wave through a polarising filter, calculated (syllabus, page 21, 7.5.2)
  - end corrections (syllabus, page 22, 8.1.2)
  - the spectrometer (syllabus, page 22, 8.4.2)
  - positive temperature coefficient thermistors (syllabus, page 23, 9.3.8)
  - motion in a circle (A Level topic 12) (syllabus, pages 26-39, A Level content)
  - gravitational fields (A Level topic 13) (syllabus, pages 26-39, A Level content)
  - temperature and thermal physics (A Level topics 14 and 16) (syllabus, pages 26-39, A Level content)
  - ideal gases and kinetic theory (A Level topic 15) (syllabus, pages 26-39, A Level content)
  - oscillations and simple harmonic motion (A Level topic 17) (syllabus, pages 26-39, A Level content)
  - electric fields (A Level topic 18) (syllabus, pages 26-39, A Level content)
  - capacitance (A Level topic 19) (syllabus, pages 26-39, A Level content)
  - magnetic fields and electromagnetic induction (A Level topic 20) (syllabus, pages 26-39, A Level content)
  - alternating currents (A Level topic 21) (syllabus, pages 26-39, A Level content)
  - quantum physics (A Level topic 22) (syllabus, pages 26-39, A Level content)
  - nuclear physics beyond AS (A Level topic 23) (syllabus, pages 26-39, A Level content)
  - medical physics (A Level topic 24) (syllabus, pages 26-39, A Level content)
  - astronomy and cosmology (A Level topic 25) (syllabus, pages 26-39, A Level content)

## 8. Rules particular to this subject

- **Equations in symbols, then numbers.** Every calculation writes the equation, the substitution, and the answer with its unit, on separate lines or clauses. Equations are plain text with Unicode symbols: Ek = ½mv², I = I0 cos²θ, R = ρL/A, 3.0 × 10⁸ m s⁻¹. No LaTeX.
- **Three significant figures in working, rounding once.** Carry intermediate values to at least three significant figures and round only the final answer, saying to how many. Write each step as "a × b = c" or "a ÷ b = c" with c unrounded: C-32 recomputes it and fails a rounded equality ("9.81 × 1.2 = 12").
- **Base units first.** Convert every prefix before substituting (mA to A, mm² to m² as × 10⁻⁶, GHz to Hz).
- **No fences, no drawings.** This subject has no chart renderer and no code. Data and readings go in markdown tables; a graph is described by its axes, shape and key values, or given as a table for the learner to plot on their own graph paper; circuits and force diagrams are described in words or tables (C-41).
- **Practical data is ours, and says so.** Readings in a practical task are introduced as our readings, realistic and consistent with the physics. The notes for topic 12 say plainly that the manipulation marks are earned at the bench.
- **Definitions exact.** A DEF card’s guidance names the words that carry the mark.
- **Symbols and units follow the syllabus.** Its summary of key quantities, symbols and units (pages 55-57), its data and formulae (pages 58-60) and its circuit symbols (pages 61-62) are the reference for every symbol, unit and diagram description.
- **Paper 1 practice is a multiple-choice set per content topic**, four options, one key, every distractor built from a named error (the misconception register first), the reason each distractor is wrong on the back.
