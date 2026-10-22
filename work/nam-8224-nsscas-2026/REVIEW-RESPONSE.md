# Response to REVIEW.md (Codex, 2026-10-18)

Each finding was checked against the source before acting. "Verified" = re-checked by me, not just accepted.

| # | Finding | Status |
|---|---|---|
| 1 | Only 188 of 240 Paper 2 marks captured | **Fixed.** Cause: part marks printed alone on a line were discarded as "subtotals". Now 60/60 (2021, 2022, 2023) and 54/60 (2024). The 6 missing 2024 marks are not in the extracted PDF text; page-image check still needed. |
| 1 | ±3 points never validated | **Withdrawn.** Replaced by a primary-versus-split sensitivity range; the classifier itself is still unvalidated (38% of marks high-confidence). |
| 1 | Script and assignments not retained | **Fixed.** `assessment-evidence/classify_questions.py` and `evidence-rows.csv` (year, paper, question, part, marks, primary and secondary topic, confidence, PDF page) are in the repo. |
| 1 | Single-topic assignment distorts integrated questions | **Partly addressed.** Secondary topic recorded and a split-credit variant reported. Manual review of integrated parts not done. |
| 2 | Five defective YYeni objective records | **Verified 3 of 5** (6626 blank record and missing oxyanion objective; 6658 duplicate and missing reactions objective; 6508 truncated record). Lessons 6674 and 6832 not yet checked by me. **Not repaired** (shared template classroom; needs your approval and a YYeni preview). All of topic 1.3 reads clean. |
| 3 | "Five" lessons for 1.3 | **Verified wrong; corrected to six.** |
| 3 | Electronegativity "overlap" | **Verified wrong; withdrawn.** 6557 = 1.3.3, 6589 = 1.3.4. |
| 3 | 1.1 lessons "already merge" 1.1.1–1.1.5 | **Verified and corrected:** 6507 = 1.1.1–1.1.4, 6508 = 1.1.5. |
| 4 | Data Booklet sentence is policy, not syllabus | **Fixed and relabelled** as our flashcard design policy. |
| 5 | Preserve weighting contradictions | Already stated unresolved in the summary; unchanged. |
| 6 | 2025 report stored under Biology workspace | **Noted** in CLAIM.md; not moved (another package's path). |
| 7 | Authority order should include assessment evidence | **Fixed** in CLAIM.md. |
| 8.1 | Repair YYeni objectives | Open: needs approval. |
| 8.4 | Recover all Paper 2 marks | Done except 6 marks in 2024. |
| 8.5–8.6 | Manual review; validate classifier on a coded sample | **Open.** |
| 8.7 | Keep frequency and difficulty separate | Followed; 2025 difficulty analysis still to do. |
| 8.8 | 2025 examiner-report analysis | Open. |
| Rec. | Provisional pilot: 1.1 stoichiometry, in an objective cluster | **Agreed as provisional.** After correction 1.1 is still the largest topic under both variants (10–13%), and I checked that the 2025 report names mass-spectra gaps, repeated significant-figure errors and 22.4 versus 24 dm³ molar-volume confusion. My earlier 1.3 recommendation rested on lesson fit and flashcard suitability, not frequency. |

## Pilot decision still open (yours)
- **1.1 cluster:** highest frequency and clear 2025 difficulty evidence; calculation-heavy, so it needs worked-example and calculation items, not only recall cards; lesson 6508's record 30757 is truncated (cards can follow the syllabus wording instead).
- **1.3 Chemical bonding:** second largest, six clean lessons, strong flashcard fit, but weaker difficulty evidence so far.
