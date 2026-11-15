# Textbook and visual-source analysis

Owner requirement: Vitalis, 15 November 2026. This extends stages A–D and Q01–Q15
of the existing Workbench playbook. New guidance, not covered by its earlier
independent closure review. No new source downloader or competing authoring pipeline.

## Inventory before mining

Inspect actual front matter and relevant pages. A folder name, research summary,
search snippet or PDF metadata is insufficient evidence of a book's identity.
Older and newer books are admissible ingredients after current-syllabus mapping;
neither age nor a matching subject title establishes curriculum fit.

Extend `analysis/source-inventory.md` with these fields, or reference a structured
inventory containing them:

| Field | Required evidence |
|---|---|
| Identity | Stable document ID, title as printed, author/compiler, publisher, edition/year; unknown stays unknown |
| Document | Actual path, SHA-256, page count, source URL/location and acquisition record/date when known |
| Scope | Board/level originally intended; exact current syllabus objective/clause links; mismatch/exclusion reasons |
| Locators | PDF page and printed page, chapter, exercise/item/figure IDs; record absent numbering explicitly |
| Usability | Real PDF vs LFS pointer/HTML/corruption; text/OCR quality; mathematical extraction limits; visual inspection scope |
| Origin and rights | Reused / adapted / newly authored output; permission/licence basis for direct reuse, or unresolved hold |
| Role | Explanation, method, graduated practice, representation, diagram, difficulty or misconception lead |

Record image credits separately where a compilation contains third-party artwork.
Do not infer reuse permission from access to a PDF or from its noncommercial origin.
Newly authored problems/parameterised diagrams may express underlying concepts
without reproducing source wording/artwork. Apply repository source-write boundaries.

## Mine exercise families, not isolated numbers

For each relevant exercise family record stable pattern IDs and source locators,
learner decisions, givens/unknowns, constraints, representation, scaffolding,
connected parts, alternatives, units/precision, answer requirements and graduated
difficulty. State the evidence that makes it a new recipe, structural branch or
ordinary variation. Do not count cosmetic changes as new patterns.

Map directly assessed objectives separately from prerequisites/context. Label the
basis as examination-observed, textbook-derived, syllabus-derived or supporting
practice, with separate links when more than one basis applies. Textbook exercises
do not establish examination frequency or official method/accuracy awards.
Author-proposed marking and purported misconceptions remain labelled as such
until supported and independently reviewed.

Add patterns and unresolved gaps to the existing demand/selection tables. A book
does not replace the whole-syllabus screen; an unobserved requirement stays visible.
Do not convert Flashcard Studio cards or treat a textbook question bank as a
ready-made renewable recipe bank.

## Visual problems

Record what the learner must do: read a diagram, infer relationships, plot, sketch,
construct, label or measure. Showing an image and reliably assessing the response
are separate capabilities. Refer unsupported/unverified responses to the existing
`capability-gaps.md`; preserve the syllabus demand.

Prefer rendering question and solution assets from the same declared instance
data. Record geometry, labels, scales, units, calibration and allowed variation.
A fixed image restricts the parameter space to compatible instances. Inspect
normal, changed and boundary renders, including visual feedback/solution assets.
Text extraction alone cannot verify spatial relationships or construction accuracy.

## Acquisition and review

Search existing holdings and harvest records first. Use the existing YYeni Web
Harvester for named gaps; keep research/deep-research output as leads until actual
documents/pages are checked. Do not imply Gemini or another research integration
is available without inspecting it. Record inaccessible documents and alternative
sources rather than claiming they were read.

Review the source-to-objective-to-pattern chain, copied wording, visual consistency,
independent recomputation and marking expectations under existing Q gates. Passing
an extraction, schema or hash check is not content acceptance.
