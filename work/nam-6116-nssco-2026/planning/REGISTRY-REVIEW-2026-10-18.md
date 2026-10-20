# 6116 Biology: transcription, decomposition and registry review, 2026-10-18

Why this exists: the 2026-10-17 plan was not approvable. Its defects were nonsense
decompositions, extraction fragments, empty slots and an AO mix of 15/20/65. A conservative scan
then flagged 60 of 621 registry entries as suspect. This records what was found and what was done.

## What could not be recovered

Neither the 621-entry registry nor the list of 60 suspects was saved before this session rebuilt
the registry, and the workspace is not committed. A one-to-one table "suspect → fix" therefore
cannot be produced. The review below covers **every** bullet and **every** objective, not only
the 60. It uses this session's printout of the original transcription and decomposition, read at
the start of the session.

## Defects found in the original transcription (all 364 bullets read)

| class | where | what happened | fix |
|---|---|---|---|
| topic-heading prose as objectives | topics 2, 3, 4, 5 | "of teaching time)", "teaching time)", "inuity of life (20% …", "h their environment (15% …" registered as objectives | the heading line that spans all three columns is skipped by geometry |
| columns bled and bullets merged | 4.1, 4.2.1 (PDF p.27) | GENERAL-column words ("t cell", "mportant for") prefixed bullets; 10 + 6 bullets collapsed into 5 + 3 run-on entries | read by word position (`pdftotext -bbox`), a new bullet only at a bullet glyph |
| bullets split mid-sentence | 3.6.2.3 | three bullets each split in two at a line wrap | as above |
| page numbers appended | last bullet on most content pages | "… recording results of experimental investigations 6" | footer region excluded |
| subscripts lost | 3.6.1.3, 3.10.1, 3.10.2 | C6H12O6 read as "C H O … 6 12 6" | subscripts attached to their element |
| nested lists flattened | 3.4 (food tests), 3.13.2 (drug effects) | sub-items run together | nested bullets kept as "; "-separated items |
| teacher note as objective | 4.4.2 | "NB: Teaching of human inherited conditions…" | recorded under `content_notes`, not as an objective |
| glued codes | 1.2.4, 5.4 | "1.2.4Basic" | split code from title |
| stated limits missed | 3.4, 3.14 | two limits wrap across lines; line scan found 5 of 7 | limits read from the joined objective text |

Independent check: `planning/verify_transcription.py` re-reads every cited page with
`pdftotext -raw` and requires each bullet as an in-order word sequence. Result: 364 of 364 pass,
with one explained difference (the arrow labels in the photosynthesis equation). The outline and
the content table reconcile: 70 rows, no missing codes.

## Defects found in the original decomposition

The regex splitter could not tell a list of skills from a list that qualifies one skill. It
produced entries such as "explain deci", "explain centi", "state magnesium", "state lakes",
"describe constipation", "identify on drawings", "define produced by a gland", "record and mass of
seeds", "explain distant objects in terms of the contraction" and "describe listing the substrate
and". **All of its output was discarded.** Decomposition is now a written judgement
(`planning/decomposition.json`). 80 bullets are split into complete, self-standing objectives
whose wording is built from the bullet's own words. One lead-in ("define the terms:") absorbs the
six bullets that follow it. Every other list is kept whole, with the reason recorded for the
non-obvious ones (prefixes, enzyme-action terms, the water pathway, gas-exchange features).
`decompose_objectives.py` fails if an entry stops matching exactly one bullet.

**Traceability.** Each objective carries `sub_topic`, and its sidecar entry
(`curriculum/objective_registry.planning.json`) holds the verbatim bullet it was split from
(`decomposed_from`), its kind and its PDF page. Sub-topic headings are kept there under
`sub_topic_headings`. Neither headings nor list containers are registry objectives, because
`build/make_work_order.py` plans slots for every entry with a parent. That follows the model
registry (9702 Physics): topic containers, then objectives.

## Classification (all 540 objectives read)

The content-first regex mistyped many objectives. Examples: "explain how temperature affects
transpiration" as quantitative ("rate of"); "state the functions of lymphocytes" as a practical
skill AO3 (it mentions the microscope); "construct simple food chains" and "explore how recycling
can reduce pollution" as practicals. It is replaced by a verb-first classifier. The full list
was then read, and 31 objectives are set by recorded override (`planning/objective_overrides.json`,
each with its reason). Two of those clear a misread command word: "draw" in "draw a conclusion" is
not the papers' drawing instruction.

Result: 540 objectives; by AO 363 A, 94 B, 83 C by objective (AO by marks is set by the slot plan,
plan section 6).
