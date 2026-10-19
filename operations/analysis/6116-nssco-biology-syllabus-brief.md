# 6116 NSSCO Biology — syllabus brief

**Authority:** NSSCO Biology Syllabus, NIED 2018. Syllabus code 6116, Ordinary Level, Grades 10–11.
Published Dec 2018, ISBN 99916-69-12-4. Implementation 2019, **first examination 2020**. The syllabus
states no final examination year, so it remains the current edition for the 2026 cohort.

**Source:** `Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_BIOLOGY_SYLLABUS.pdf`, 49 physical pages.
Transcribed by `work/nam-6116-nssco-2026/planning/transcribe_syllabus.py` into
`work/nam-6116-nssco-2026/curriculum/syllabus-facts.json`. Every value there carries the page that
states it and the verbatim line.

**Page numbering.** The PDF carries three front-matter pages, so `pdf_page = printed_page + 3`.
Both are recorded on every citation. Printed pages are cited below with the PDF page in brackets.

## Assessment objectives

**The wording and the weightings are on different pages, and are cited separately.**

| What | Where |
|---|---|
| AO A and AO B names, lead-ins and sub-objectives A1–A4, B1–B7 | printed p.35 [**PDF 38**] |
| AO C name, lead-in and sub-objectives C1–C5 | printed p.36 [**PDF 39**] |
| AO percentages and the per-paper mark allocations (specification grid) | printed p.37 [**PDF 40**] |
| Paper descriptions, durations and marks (scheme of assessment) | printed p.36 [**PDF 39**] |
| Paper weightings (30/50/20) | printed p.37 [**PDF 40**] |

Weightings exactly as the grid labels them, under its column header
*"Overall Weighting across all components"* — printed p.37 [PDF 40]. The grid's own preamble calls
these weightings *"approximate"*.

| AO | Name (p.35–36 / PDF 38–39) | Grid label (p.37 / PDF 40) |
|---|---|---|
| A | Knowledge with understanding | **47% (not more than 24% recall)** |
| B | Handling information, application and solving problems | **28%** |
| C | Practical (experimental and investigative) skills and abilities | **25%** |

**The denominator of "not more than 24% recall" is not stated anywhere in the syllabus.** The
figure sits inside AO A's cell in the "Overall Weighting across all components" column, which
suggests it is a share of the whole qualification (at most 24 of AO A's 47 points). But it could
equally qualify AO A alone, meaning 24% *of* 47% = 11.3% of the qualification. The other six
mentions of "recall" in the document are grade descriptors and content wording, none carrying a
percentage. **No interpretation is adopted.** The uncertainty is recorded in `syllabus-facts.json`
as `recall_ceiling_denominator`, provenance `uncertain`, with the evidence for both readings.

Either way it is a ceiling on the share of assessment that may be pure recall — a property of the
examination, not of a card bank, and it converts to no item count.

### Exact wording — transcribed, not summarised

Section lead-in (printed p.35 [PDF 38]): *"The assessment will include, wherever appropriate, personal, social, environmental, economic and technological applications of Biology in modern society. Learners are required to demonstrate the assessment objectives in the context of the content and skills prescribed, within each of the assessment objectives. Assessment must take account of the learners' ability to communicate clearly and logically and apply conventions where appropriate."*

**A — Knowledge with understanding.** Lead-in: *"The learning content defines what learners need to recall and understand:"*

- **A1** scientific phenomena, facts, laws, definitions, concepts, theories;
- **A2** scientific vocabulary, terminology, conventions (including symbols, quantities and units);
- **A3** scientific instruments and apparatus, including techniques of operation and aspects of safety;
- **A4** scientific and technological applications with their social, economic and environmental implications.

A also carries a question-word note (printed p.35 [PDF 38]): questions testing it *"will often begin with one of the following words: define, name, list, indicate, give examples, state, describe, compare, explain (using your knowledge and understanding), distinguish, outline and give reasons."*

**B — Handling information, application and solving problems.** Lead-in: *"Learners should be able to, in words or using written forms of presentation, (i.e. symbolic, graphical and numerical):"*

- **B1** locate, select, organise and present information from a variety of sources;
- **B2** translate information from one form to another;
- **B3** manipulate numerical and other data
- **B4** use information to identify patterns, report trends and draw inferences;
- **B5** present reasoned explanations of phenomena, patterns and relationships;
- **B6** make predictions and propose hypotheses;
- **B7** solve problems including some of a qualitative nature as they relate to everyday life.

B carries a condition that matters for item design (printed p.35 [PDF 38]): *"These skills cannot be precisely specified in the learning content as questions testing such skills are often based on information, which is unfamiliar to the learner. In answering such questions, learners are required to use principles and concepts that are within the syllabus and apply them in a logical, deductive manner to a novel situation."* Its question words: *"discuss, deduce, compare and discuss, find, estimate, interpret, evaluate, sketch, predict, identify, relate, suggest, calculate or determine."*

**C — Practical (experimental and investigative) skills and abilities.** Lead-in: *"Learners should be able to:"*

- **C1** demonstrate knowledge of how to use apparatus and materials safely (including following a sequence of instructions where appropriate)
- **C2** plan experiments and investigations (including how to record accurate estimates, observations and measurements accurately and make deductions from simple tests)
- **C3** handle and process experimental observations and data (including dealing with anomalous or inconsistent results)
- **C4** apply scientific knowledge and understanding to make interpretations and to draw appropriate conclusions from practical observations and data;
- **C5** evaluate methods and suggest possible improvements

The parentheticals on C1–C3 are qualifications, not examples, and are preserved verbatim in `syllabus-facts.json` under `assessment_objective_detail`.

## Papers — printed p.36–37 [PDF 39–40]

| Paper | Description | Duration | Marks | Weighting | AO A | AO B | AO C |
|---|---|---|---|---|---|---|---|
| 1 | Theory — 40 multiple-choice, four-choice type | 45 min | 40 | 30% | 25 | 15 | 0 |
| 2 | Theory — compulsory short-answer and structured | 1 h 30 min | 80 | 50% | 50 | 30 | 0 |
| 3 | Alternative to Practical | 1 h 15 min | 40 | 20% | 0 | 0 | 40 |
| | | | **160** | **100%** | **75** | **45** | **40** |

All three papers are compulsory for every learner.

**Raw marks and final-grade weighting are different quantities and must not be mixed.** The AO
percentages the syllabus states reconcile to RAW MARKS: 75/160 = 46.9% ≈ 47%, 45/160 = 28.1% ≈ 28%,
40/160 = 25%. But the paper weightings (30/50/20) do NOT match the papers' raw mark proportions
(25/50/25) — Paper 1 is scaled up and Paper 3 scaled down. Applying the paper weightings to each
paper's AO split gives effective FINAL-GRADE weightings of **A 50%, B 30%, C 20%**.

| | AO A | AO B | AO C |
|---|---|---|---|
| Raw-mark proportion (what the syllabus states) | 46.9% ≈ 47% | 28.1% ≈ 28% | 25.0% |
| Share of the final grade (after paper weighting) | 50.0% | 30.0% | 20.0% |

Both are real. Neither is a card quota. Recorded in `syllabus-facts.json` as
`derived_weighting_reconciliation`, tagged `judgement` to keep it separate from transcription.

**Paper 1 duration: an unresolved conflict between the syllabus and the live paper.**

| Source | Paper 1 duration | Issuing footer |
|---|---|---|
| Syllabus, printed p.36 [PDF 39] | **45 minutes** | NIED 2018 |
| 2020, 2021, 2022, 2023, 2024 papers | 45 minutes | MoEAC/DNEA |
| **2025 paper** (`6116/1/25`) | **1 hour** | MEIYSAC/DNEA |

The 2025 paper's identity was verified: cover reads BIOLOGY ORDINARY LEVEL 6116/1, Marks 40, 2025;
footer `6116/1/25`; cover states "There are forty questions on this paper" and 40 were counted.
Structure matches the syllabus exactly — forty four-choice questions, equal marks, 40 total. Only
the duration differs. The issuing ministry was renamed in the same year (MoEAC to MEIYSAC).

`Syllabi/`, `sources/` and `_harvest/` were searched for a revised syllabus, erratum or amendment:
**none exists in the repository**, only NSSCO_BIOLOGY_SYLLABUS.pdf (NIED 2018). The 2025 examiner
report's Biology section says nothing about duration.

**Unresolved.** Both statements are retained in `syllabus-facts.json` as `paper_1_duration_conflict`,
provenance `conflict`. The syllabus remains the authority under AGENTS.md rule 0, but the most
recent live paper contradicts it on this value. What governs the 2026 cohort must be confirmed with
NIED/DNEA before the plan fixes any paper timing.

## Command words — printed p.39–40 [PDF 42–43]

Eighteen, exactly as the glossary states them: Apply/use · Calculate · Compare · Define ·
Describe · Describe and explain · Determine · Discuss · Estimate · Explain ·
Give a reason/Give reasons · List · Measure · Outline · Predict · Sketch · State · Suggest.

`Describe`, `Explain` and `Give a reason` are listed with lettered senses, (a) and (b), which the
transcription keeps as a `sense` field.

The AO descriptions name further question-opening words that the glossary does not define —
*name, indicate, give examples, distinguish, deduce, find, interpret, evaluate, identify, relate*.
Per AGENTS.md rule 5, which words may actually open a generated prompt is settled from the papers
at step 3, not from either list.

## Content — printed p.4–34 [PDF 7–37]

Five topics, 70 sub-topic rows, **393 specific objectives**. The outline and the content table
reconcile exactly: no outline code lacks a content row and no content row is absent from the
outline.

| Topic | Title | Specific objectives |
|---|---|---:|
| 1 | Scientific processes | 43 |
| 2 | Classification and diversity of living organisms | 9 |
| 3 | Organisation and maintenance of the organism | 197 |
| 4 | Development of the organism and the continuity of life | 91 |
| 5 | Relationship of organisms with one another and with their environment | 53 |

Topic 3 carries half the subject's objectives. Topic 2 carries nine.

## Stated exclusions — five, each cited

- water potential and hydrostatic pressure are not required — printed p.18 [PDF 21]
- nephron detail is not required — printed p.21 [PDF 24]
- details of the stages of cell division are not required — printed p.24 [PDF 27]
- details of maternal and paternal chromosomes are not required — printed p.24 [PDF 27]
- details of endosperm production and development are not required — printed p.25 [PDF 28]

These are captured as the lines that state them; each is a parenthetical inside a specific
objective, so the surrounding objective supplies the scope it limits.

## Paper 3, Alternative to Practical — printed p.41 [PDF 44]

Annexe A sets eleven criteria, (a) to (k): follow a sequence of instructions; read scales from
diagrams of apparatus, interpolating between divisions and averaging repeats; describe, explain or
comment on experimental arrangements; interpret and evaluate observations and data; complete and
process data tables; perform calculations including magnification of a drawing; plot graphs and
interpret graphical information; draw a conclusion justified by reference to the data; identify
sources of error and suggest improvements; plan an investigation with reasoned predictions; and
recognise, observe, record and measure images of familiar and unfamiliar specimens.

Annexe B (printed p.42 [PDF 45]) fixes the data conventions: the solidus separates quantity from
unit (`time / s`), column headings transfer directly to graph axes, and the independent variable
is plotted on the x-axis unless instructed otherwise.

## What this means for the plan

1. **AO C is assessed only on Paper 3**, worth 25% of raw marks and 20% of the final grade.
   Annexe A's eleven criteria are its specification. What the existing platform deck does or does
   not cover for AO C is a question for the card-level comparison at the upload stage, not
   something to infer from image counts or absent Bloom labels — a card can exercise a practical
   skill in words, and an absent label is a metadata gap, not evidence of absent coverage.
2. **Recall is capped at "not more than 24% recall"** inside AO A's 47% raw-mark share. This is a
   ceiling stated by the syllabus, and it constrains the Remember/Understand balance. It is not a
   card count and does not convert to one.
3. **Topic 3 carries 197 of 393 objectives.** Emphasis follows the objectives and the measured
   exam demand, never a percentage converted into a quota.
4. **Transcription anomalies are recorded, not smoothed.** The syllabus renders two sub-topic
   codes irregularly — `4.3.5.` with a trailing dot (printed p.27 [PDF 30]) and `4.4 .3` with an
   internal space (printed p.29 [PDF 32]). Both are handled; without that, 4.3.5 Growth and
   development and 4.4.3 Variation would each have lost every objective they own.
5. **Two source-vs-syllabus divergences are open for the operator**: Paper 1's duration (45 minutes
   stated, 1 hour on the 2025 paper) and the absence of any mark scheme, which no examiner report
   substitutes for.

## Separation of transcription from reading

`curriculum/syllabus-facts.json` holds transcription only, every value tagged `syllabus` and
carrying its page and verbatim line. Anything this brief derives — the final-grade weighting
reconciliation, the emphasis reading above — is tagged `judgement` and kept out of the
transcription blocks, so the two are never mistaken for each other.
