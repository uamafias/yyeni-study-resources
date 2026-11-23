# Owner decisions and new requests: 8227 analysis repair round

Recorded 2026-11-16 by Claude (reviewer) from Vitalis's two replies to `report.md` §8. These apply to the repair of the steps 1–3 analysis. Author inputs are unchanged. The repair brief that carries these decisions into work is `REPAIR-PROMPT.md` in this folder.

## 0. Authority

Vitalis is the final decision-maker for the Workbench framework, the playbook and the app. Jeremy's approval is not required. Where `report.md`, `findings.md` or the playbook says "Jeremy/Vitalis", "owner" or "framework owner", the decision is Vitalis's, and the decisions below are final.

Vitalis has the full app codebase and is making the app changes that the Workbench direction needs.

## 1. Decisions on the escalations

| # | Escalation | Decision |
|---|---|---|
| 1 | 2023 P1 Q9 principal value (R13-04) | **Option (a).** Hold the question as defective. Build principal-value inverse trigonometry (M1 T6 O04) as syllabus-derived using the standard principal ranges, supported by Cambridge evidence (N2). |
| 2 | 2023 P2 Q7(c) degree-mode alternative (R13-06) | **Do not adopt** the degree-mode alternative in the official award table. Require radian mode where the problem is in radians. Record the anomaly. |
| 3 | 2023 P1 Q1(b) degenerate case (R13-05) | **Hold** the question as an exemplar. Proof recipes state the a ≠ 0 condition. |
| 4 | Grade descriptions as calibration evidence (R13-11) | **Yes.** The grade a/c/e descriptions (syllabus pp19–24) are official evidence for how easy or hard variations may get. Easier branches are pitched at the grade e/c statements. The hardest branch goes no further than the grade a statement. Statements naming content no paper has examined (e.g. segment area at grade c; points of inflexion and a cubic from given information at grade a) count as evidence that the content is expected. |
| 5 | Commercial textbooks and OCR in the shared repository (R13-26) | **Accepted.** The two commercial textbooks and their OCR derivatives may stay in the shared repository. (Minor, still open: refiling the root-level `Y=mc as textbook.pdf` under `sources/`.) |
| 6 | Capability notification (R13-10, R13-18) | **Superseded by an app change.** From 2026-11-17, the app accepts and reads sketched answers and diagrams. It will also generate diagrams similar to a recipe's source diagram, using image-generation models in a loop with the recipe context, with values or features changed as the recipe specifies. Consequences:<br>(a) CAP-8227-02 sketch parts and the two sketch-dependent parts (2023 P2 Q6(d), 2025 P1 Q4(c)) are **included, not held**.<br>(b) Diagram-bearing questions are included.<br>(c) Problem sets that need sketch responses and diagram inputs are wanted.<br>(d) The analysis must now record what the generator and marker need: the source diagram image; what the diagram gives; which labels and values vary; and the credited features of a sketch. |

## 2. Owner requests (approved for implementation)

### N1. Examination references on every part, family and recipe

**Approved.** Every problem part, problem family and recipe records each examination question of the same type: board, syllabus code, year, session, paper and variant, question, part and printed page. The app shows these references to learners. Vitalis is changing the app UI and the public catalogue fields, replacing the allowlist limit at `services/api/workbench_platform/loader.py:25`.

**Learner wording (approved).**

| Problem shown | Label |
|---|---|
| Generated variant | "Same type as NSSCAS Mathematics 8227, 2023 Paper 1, Question 5(b), page 7" |
| Original question shown verbatim (see N2) | "NSSCAS Mathematics 8227, 2023 Paper 1, Question 5(b), page 7" or "Cambridge International AS Level Mathematics 9709, Paper 12, May/June 2017, Question 5, page 6" |

**Order of work.** Build the references after the part→demand repair (R13-01, R13-02). Otherwise they will repeat the wrong mappings.

### N2. Cambridge evidence: gap filling and variety

**Approved and widened.**

1. **Scope.** The NSSCAS 8227 syllabus and its limits decide scope. A Cambridge question counts only when the parts used are within 8227 scope.
2. **Gap filling.** Where an in-scope objective or demand has no NSSCAS 2021–2025 question, search Cambridge 9709 Paper 1 and Paper 2 for questions that test it.
3. **Variety.** Also search Cambridge for in-scope demands that NSSCAS already examines, to add question types and variations, especially questions with diagrams or images.
4. **Labelling.** Cambridge items are labelled as Cambridge everywhere: in records, recipes and learner labels. They are never presented as Namibian.
5. **Exact questions (rights).** The exact Cambridge question text may be used verbatim, with clear attribution to the board, syllabus, paper, session, question and page. Vitalis has considered and accepted the rights position. The same applies to NSSCAS questions. This supersedes the review prompt's line that source extracts are "internal evidence, not authorised learner-facing reuse".
6. **Evidence label.** Use `comparable-examination-observed (Cambridge 9709)`, distinct from `examination-observed (NSSCAS 8227)`. Vitalis has approved this as a framework addition.

**Corpus.** The 9709 P1 and P2 question papers and mark schemes held are:

| Years | Status | Source |
|---|---|---|
| 2020–2025 | Already held | n/a |
| 2018–2019 | Acquired 2026-11-16 | pastpapers.co |
| 2015–2017 and March 2018 | Acquired 2026-11-16 | dynamicpapers.com, with papacambridge as fallback |

The Harvester manifest is `_harvest/manifests/routed-9709-2015-2019.csv`. The 2015–2019 batch is 136 files: question paper and mark scheme for P1 and P2, all variants, plus March 2016–2019. All 136 fetched and passed `harvest verify` (`_harvest/reports/integrity_2026-11-16.md`). A content check confirmed the code, component/variant, year, series and document type for each file. Run report: `_harvest/reports/run_20261116-025816-076.md`. Pre-2020 Paper 1 includes vectors, which moved to Paper 3 in 2020, so it is the best Cambridge source for M1 T7. The repository holds only the 2026–2027 9709 syllabus. Older papers were set under earlier syllabus versions, but the 8227 scope check is what decides inclusion.

**Initial exploration.** This was a text search of 132 Cambridge 2020–2025 P1, P2 and P3 papers for the eight 8227 demands that R13-02 found unexamined. The table lists candidates only. None has yet been read or checked against 8227 scope. Locators give the file and PDF page; question numbers are given only where the extracted text showed them clearly. Session codes: m = Feb/March, s = May/June, w = Oct/Nov.

| 8227 demand | Cambridge position | Candidates (unverified) |
|---|---|---|
| Increasing/decreasing intervals (M1 T8 O03 D02) | 9709 P1 1.7 (syllabus p22) | 9709_m20_qp_12 p2 Q1 · 9709_s21_qp_13 p4 Q2 · 9709_w21_qp_13 p4 Q3(b) · 9709_w22_qp_11 p12 (a) · 9709_m22_qp_12 p19 · 9709_s24_qp_11 p16 (a) · 9709_s24_qp_12 p16 (a) · 9709_w24_qp_12 p17 (c) · 9709_w25_qp_12 p14 (a). Many other "increasing" hits are rates of change, not monotonicity. |
| Segment area (M1 T5 O02 D03) | P1 circular measure | 9709_w22_qp_11 p6–7 (a, b) · 9709_m24_qp_12 p13 (d) · 9709_s25_qp_11 p14–15 · 9709_s25_qp_12 p11 (c) · 9709_w25_qp_13 p6 (b) · 9709_s23_qp_11 p5 (segment perimeter) |
| Division by a quadratic (M2 T1 O03 D02) | 9709 P2 2.1 (syllabus p23) | 9709_m20_qp_22 p3 Q2(a) (÷ x² + 5x + 6). Other quotient hits use linear divisors. |
| Principal values (M1 T6 O04) | 9709 P1 1.5 (syllabus p21) | 9709_w23_qp_12 p3 Q2 · 9709_w22_qp_13 p7 Q6 |
| Failure of an iteration to converge (M2 T6 O02 D02) | 9709 P2 2.6 expects the understanding (syllabus p25), but no 2020–2025 question was found that asks for it. The closest is 9709_w21_qp_22 p9 Q9(c). | None yet; search 2015–2019 |
| Constructing a unit vector (M1 T7 O03 D01) | Vectors moved to 9709 P3 in 2020, where they come mixed with 3D lines, which are beyond 8227. | 9709_w23_qp_33 p18 Q11(a) (unit vector along a line). Search the 2015–2019 P1 papers. |
| Points of inflexion (M1 T8 O04 D02) | Excluded from 9709 P1: "Knowledge of points of inflexion is not included" (syllabus p22). Pre-2020 P1 may differ; check. | None yet |
| Cubic from a graph (M1 T1 O05 D02) | Not searched | n/a |

### N3. Direction for other subjects (not part of this repair)

For every Namibian (NIED) subject with a matching Cambridge subject (for example mathematics, physics and chemistry), Workbench analysis should also mine the corresponding Cambridge papers for questions within the NIED syllabus scope. This applies even where NIED papers already examine those objectives. The aim is more question types and variations, especially diagram-bearing ones. The same rules apply: the NIED syllabus decides scope, items are labelled as Cambridge, and exact questions are attributed.
