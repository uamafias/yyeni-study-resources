# NSSCAS Chemistry 8224 — topic frequency count (v2, keyword-based, still UNVALIDATED)

> **SUPERSEDED — do not use for planning or learner-facing claims.** Use `operations/analysis/8224-nsscas-chemistry-corpus-analysis.md`, which is based on the manually meaning-mapped evidence records. This file is retained only as workflow history.

**Date:** 2026-10-18 (v1 replaced after Codex review). Papers 1 and 2, 2021–2024; Paper 3 (practical) not counted.
**Reproduce:** `python3 assessment-evidence/classify_questions.py` (reads the PDFs; writes `evidence-rows.csv` and `reconciliation.txt`).
**Rows:** `evidence-rows.csv` has one row per Paper 1 question and Paper 2 mark-bearing part: year, paper, question, part index, marks, primary topic, secondary topic, confidence, PDF page.

## What changed from v1
- v1 dropped Paper 2 part marks printed alone on a line (it mistook them for question subtotals) and kept only 188 of 240 marks. These papers print no question subtotals. v2 captures **60/60 marks in 2021, 2022 and 2023 and 54/60 in 2024** (394 of 400 marks/items in all, 98.5%).
- The 6 missing 2024 Paper 2 marks are not present as `[n]` text in the extracted PDF (no other mark format found); they may sit in graphics or be unprinted. A page-image check is needed. 2024 therefore carries 94% weight.
- The v1 "±3 points" claim is withdrawn: it was never validated.
- Each row now records a secondary topic, so integrated questions can be shown both ways.

## Limits (read first)
- **Keyword classifier, not validated.** No manually coded sample has been compared against it. Confidence by marks: high 38%, medium 31%, low 29%, unclassified 2%.
- **Sensitivity range, not an error bar:** "primary" gives all marks of a part to its top topic; "split" shares marks 50/50 with the secondary topic where one exists. The range between them shows only how much integrated parts could move a share; it says nothing about outright misclassification.
- Proof versions: 2021–2023 are proofs; 2024 is unlabelled. Wording may differ from the printed exam.
- No mark schemes or 2021–2024 examiner reports exist in the repo; this file says what was asked, not what was credited or commonly wrong. Frequency and difficulty are separate measures (2025 report: separate file, to come).
- Under RS-36, no "most examined" statement may appear in learner notes without mapped assessment evidence.

## Result (Paper 1 questions + Paper 2 marks, 2021–2024)
| Topic | Primary | Split | Range |
|---|---:|---:|---:|
| 1.1 Atoms, molecules, stoichiometry | 12.7% | 10.4% | 10.4–12.7 |
| 1.3 Chemical bonding | 9.1% | 8.4% | 8.4–9.1 |
| 1.4 Ideal and real gases | 6.6% | 5.2% | 5.2–6.6 |
| 4.2 Hydrocarbons | 6.6% | 7.4% | 6.6–7.4 |
| 1.2 Atomic structure | 6.3% | 6.1% | 6.1–6.3 |
| 2.1 Chemical energetics | 5.8% | 5.5% | 5.5–5.8 |
| 3.4 Group 17 | 5.6% | 6.6% | 5.6–6.6 |
| 3.2 Group 2 | 5.6% | 5.6% | 5.6 |
| 3.5 Nitrogen and Sulfur | 5.1% | 5.3% | 5.1–5.3 |
| 3.3 Transition elements | 4.8% | 6.0% | 4.8–6.0 |
| 2.4 Reaction kinetics | 4.6% | 4.3% | 4.3–4.6 |
| 4.5 Isomerism | 4.6% | 4.4% | 4.4–4.6 |
| 2.3 Equilibria | 4.3% | 6.7% | 4.3–6.7 |
| 2.2 Electrochemistry | 3.6% | 2.8% | 2.8–3.6 |
| 4.1 Foundations of organic | 3.3% | 3.3% | 3.3 |
| 4.4 Hydroxyl compounds | 3.0% | 3.6% | 3.0–3.6 |
| 4.7 Carboxylic acids/derivatives | 2.5% | 3.6% | 2.5–3.6 |
| 3.1 Periodicity | 2.5% | 1.9% | 1.9–2.5 |
| 4.6 Carbonyl compounds | 1.0% | 1.0% | 1.0 |
| 4.3 Halogen derivatives | 0.8% | 0.5% | 0.5–0.8 |
| unclassified | 1.5% | 1.5% | — |

**By theme (primary / split):** Theme 1 34.8% / 30.1%; Theme 3 23.6% / 25.4%; Theme 4 21.8% / 23.7%; Theme 2 18.3% / 19.3%.
**Reading:** Theme 1 is the largest block under both variants, and 1.1 then 1.3 are the two largest topics under both. Differences among the middle topics (roughly 4–7%) are within what the sensitivity range and the unvalidated classifier could change.

## Still required (from the Codex review)
1. Manually code a sample (including all low-confidence and integrated parts) and measure classifier agreement before quoting any uncertainty.
2. Page-image check of 2024 Paper 2 for the 6 missing marks.
3. Manual review of ambiguous and integrated questions.
4. Keep frequency (this file) and difficulty (2025 report) as separate measures; combine only deliberately.

> **SUPERSEDED 2026-10-18.** This keyword-based count is replaced by section 5 of `operations/analysis/8224-nsscas-chemistry-corpus-analysis.md`, which maps each part by meaning. Its theme ranking differs (Theme 4 largest, not Theme 1). Do not quote the figures above.
