# Author analysis checks for Mathematics 8227

15 November 2026. Scope: commissioned source preparation, syllabus map and first
problem-family analysis. Author: Codex. No independent acceptance or recipe release.

## Results and scope

| Check | Result | Evidence and limit |
|---|---|---|
| Syllabus transcription | Pass for assembly | 60 objective quotations are literal substrings on cited PDF pages; 11 assessment abilities retained; mathematical demand labels are analyst judgements |
| Question/part references | Pass for assembly | 119 question records, 250 unique assessed-part IDs; all family/objective references resolve |
| Tariffs | Pass | Reopens actual paper PDFs; each annotated part-mark sequence matches printed brackets within its question pages; all ten papers reconcile to 75 marks |
| Source identity | Pass | Registered file hashes and current source PDFs agree; original source bytes not changed |
| Textbook OCR completeness | Pass for processing | 663 page records, each bound to original source hash/page; cache settings checked; does not certify recognition accuracy |
| Textbook recognition quality | Limited | 20 listed visual QC pages; serious formula errors in OCR remain. Use images for mathematics, exact exercise IDs and diagrams |
| Textbook analysis breadth | First sample | 17 source samples, including all 13 Namibia-book chapters and two Goldie sections. Remaining exercise/answer space is unreviewed |
| Marking evidence | Partial | 22 questions have linked official report award excerpts. Detailed award/alternative/follow-through reconciliation and remaining full schemes pending |
| Selection/coverage | First author pass | 138 proposed demands retained, 62 provisional broad families, stable source-part links. Exact atomic-demand mapping/branch boundaries and independent disposition review pending |
| Mathematical correctness | Not run as acceptance | No generated recipes or all-question independent solution audit. Two source defects flagged, not silently corrected |
| Application/visual grading | Not run | 11 visual-response parts and other capability needs handed off; no app modification/validation in this pass |
| Independent review | Pending | Author source checks are not independent educational acceptance |

## Rebuild and review

From repository root, using installed Python with pypdf and macOS Swift/Vision:

```text
swift operations/tools/pdf_ocr_macos.swift "Y=mc as textbook.pdf" work/nam-8227-nsscas-2026/workbench/analysis/ocr/ymxc 1 663
python3 work/nam-8227-nsscas-2026/workbench/tools/build_source_addenda.py
python3 work/nam-8227-nsscas-2026/workbench/tools/build_analysis.py
```

OCR is local, cached and resumable; metadata rejects changed source/settings.
Originals stay intact. The two Python assemblers are subject analysis tools, not a
new content-generation framework. Their inputs and exact outputs are frozen in
`analysis/analysis-snapshot.json`; OCR page hashes are separately indexed.
Native paper/report text derivatives record their original PDF path/hash.

Applicable Workbench Q01/Q02/Q03/Q06/Q07/Q10/Q13 source/selection concerns remain
subject to the stated limits. Q04–Q14 recipe/runtime/release checks cannot be claimed
passed without recipes and a named app/release scope. Static flashcard PUBLISH
checks do not certify this Workbench analysis. No standard files were changed.

The owner authorised proceeding with steps 1–3; that is recorded as work scope,
not backfilled source-completeness, syllabus-table verification or analysis acceptance.
No source wording/assets were approved for direct learner reuse. No commits,
pushes, publication, imports, assignment or production activation performed.
