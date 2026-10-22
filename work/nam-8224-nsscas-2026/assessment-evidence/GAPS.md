# NSSCAS Chemistry 8224 — evidence and knowledge gaps

**Updated:** 2026-10-22
**Stage:** Step 3 corpus analysis  
**Purpose:** keep uncertainty explicit so planning and flashcard authors do not invent evidence or repeatedly search for the same answer.

## Research rule for this run

Research is corpus-first and is done before flashcard authoring. The searchable corpus is the local set of syllabus documents, question papers, examiner reports, mark schemes (when present), revision notes, textbooks and YYeni learning resources recorded in `sources/SOURCES.md`.

- Do not search the web card by card.
- Search the local corpus once, record evidence with a source locator, and reuse the derived evidence files during planning and authoring.
- If the local corpus cannot support a claim, leave it in this gap register. Do not fill it from memory.
- Any later web or Drive acquisition is a separate source-gathering pass, followed by re-running the affected analysis. It is not an authoring-time lookup.

## Source gaps

| Gap | Consequence | Treatment |
|---|---|---|
| No official mark schemes for the 2021–2024 papers | Exact creditworthy points and acceptable alternatives cannot be reconstructed reliably | Use papers only for assessed content, demand and question form; do not present inferred answers as official marking guidance |
| No examiner reports for 2021–2024 | Recurring misconceptions cannot be triangulated across those years | Keep all misconception claims from 2025 marked `single_source` |
| 2025 question papers are not held | The 2025 examiner-report records cannot always be tied back to full question wording or diagrams | Preserve report locators and summaries; do not infer missing stems |
| 2021–2023 papers are proof copies; 2024 papers are unlabelled | Wording or layout may differ from final printed papers | Treat frequencies as corpus observations, not a complete historical record |
| Original Chemistry revision-notes directory is empty, but the reference pack now supplies teaching references | OpenStax textbook, organic guide and 41 chapter/section HTML pages are archived and searchable locally | Use `sources/reference-pack/references.json`; cite exact pages/sections per claim. Source availability does not replace semantic verification |

## Evidence gaps and qualifications

| Gap | Evidence | Consequence / treatment |
|---|---|---|
| Fourteen 2025 Paper 1 report records are not objective-mapped | The report provides an answer key/performance note but not enough question content | Retain as unmapped rather than guessing the syllabus objective |
| Nineteen misconception records come from one source | All are from the 2025 examiner report | Use them for discriminating practice with explicit one-report provenance; do not generalise them into recurring or board-wide claims |
| Answer-shape evidence is partial | No 2021–2024 mark schemes; only the 2025 report provides credited-response detail | Do not generalise answer shapes across years without another source |
| Difficulty evidence is 2025-only | The available report covers one examination year | Keep difficulty separate from frequency and label it by year |
| 2024 P2 Q1(a)–(f) prints one total of 6 rather than part tariffs | Page 2 contains six one-response parts and `[Total: 6]` | The evidence map assigns 1 mark to each part and records this as an inference |
| A 30-record manual mapping spot check had 27 clear and 3 arguable/qualified mappings | Recorded in the corpus analysis | Use objective-level counts directionally; inspect the cited question before making a fine-grained claim |

## Diagram and extraction audit

All 76 records marked `needs_graphic: yes` were checked against 46 relevant page images on 2026-10-21. The audit confirmed the meaning mappings and the 2024 P2 Q1 allocation. One source locator was corrected: `EV-8224-2021-P1-Q37` is on PDF page 11, not page 10. See `assessment-evidence/IMAGE-REVIEW.md`.

## Curriculum and platform gaps

The live YYeni Chemistry classroom still needs a separate, previewed repair transaction before resources are mapped/imported or assigned in YYeni (repository authoring can proceed):

- Topic 1.2 Atomic Structure has no lesson in the current classroom structure.
- The Group 2 lesson is filed under the wrong section.
- Lesson 6626 has a blank redox objective.
- Lesson 6658 duplicates the melting-point objective and omits reactions with oxygen, water and dilute acids.
- Lesson 6674 has a blank Group 17 objective and omits the bond-energy interpretation of hydrogen-halide stability.
- Lesson 6832 has three blank objectives and omits systematic nomenclature of alcohols.
- Lesson 6508 contains a truncated standard-condition note.

These are operational mapping gaps, not reasons to alter the official syllabus facts. Repair them from the syllabus wording through YYeni preview/confirm, with explicit approval of the preview.

## What this means for flashcards

- Full syllabus coverage remains the governing requirement; observed frequency sets emphasis, not scope.
- Formula and calculation cards may be prioritised where the corpus supports them, but the deck plan must still include conceptual, explanatory, practical and representation demands.
- No learner-facing card should claim a topic is “most examined” unless the claim cites the mapped corpus analysis and states its limits.
- Do not author or publish cards until the Step 3 analysis checkpoint and the subsequent Step 4 plan checkpoint are accepted.

## Preparation gaps closed — 22 October 2026

- The original 2025 examiner report has been restored into this subject’s own reference pack, with an exact hash match. The earlier dependency on a missing file in another subject is removed.
- The teaching reference pack has topic/objective routes for all 21 topics and 253 assessable objectives. It supports source-based authoring; individual fact verification remains part of each claim ledger. See the edition and scope qualifications in the pack README.
- Four original diagram families now have deterministic SVG and PNG generation. A one-objective visual exemplar passes the standard checks and a separate reproducibility/asset-packaging check. No standard generator or checker was modified. Use `planning/publish_chemistry_8224.py` so image files travel with notes and card JSON.
- Model inspection of previews is complete. Human inspection of final generated visuals is still pending before publication and cannot be inferred from model inspection.

The missing official mark schemes, older examiner reports and 2025 question papers remain evidence limitations. No frequency/marking assumptions were revised during this teaching-source preparation pass.
