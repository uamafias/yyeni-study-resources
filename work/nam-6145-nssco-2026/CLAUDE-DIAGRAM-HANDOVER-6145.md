# Claude handover — diagrams and chart cards, 6145 NSSCO Economics

Paste below the line into Claude Code in this same checkout. Revision-01 scope was approved by Vitalis on 28 October 2026 and activated; visual authoring is authorised now.

---

You are the AUTHOR for the diagram/chart portion of 6145 NSSCO Economics, workspace `work/nam-6145-nssco-2026/`, owner Vitalis P Haupindi. Vitalis explicitly assigned visual authoring to Claude and visual review to Codex. Read AGENTS.md, TEAM-PLAYBOOK.md, only the AUTHOR role brief, STATUS.md and the revised PLAN-6145-nssco-economics.md. This handover narrows the generic whole-subject author instruction to the visual assignment below.

## Approval and preservation

Read planning/revision-01/approval-and-activation.json and STATUS: Vitalis approved the revised scope and explicitly requested this Claude authoring handover. The approved candidate inputs are already promoted to live contracts/orders. Start the visual phase now; do not request the same scope approval again. Codex’s 37 nonvisual additions are pending and no Codex authoring is running, so visual work may safely run first. A local Git checkpoint remains pending; no commit or push is claimed or authorised by this handover. The saved baseline and activation hashes preserve the reviewable starting state. The reviewed baseline and any completed nonvisual additions must survive. Do not run author_support.py, write_packet.py, final_author_audit.py, or the original planning bootstrap/write_plan.py. Those scripts describe earlier content or scope and can overwrite reviews.

## Exact visual assignment

Read `planning/revision-01/claude-visual-work-order.json`. It fixes 12 item IDs, parents, labels, targets, side-specific file paths and economic requirements: eight new cards and four existing market-forces PROC cards. Produce 12 question PNGs and 12 answer PNGs, plus matching SVG masters. Save all parameters, plotted points, equations, scales, labels and render code. Names in the work order are derived from item IDs; do not rename files manually.

| Item | New/existing | Visual target |
|---|---|---|
| `ITEM-6145-1.1-011-PROC` | new | Production possibility curve |
| `ITEM-6145-3.3-019-PROC` | new | Demand elasticity diagrams |
| `ITEM-6145-3.3-020-PROC` | new | Supply elasticity diagrams |
| `ITEM-6145-4.2-025-PROC` | new | Labour market equilibrium and demand shift |
| `ITEM-6145-5.4-031-PROC` | new | Long-run average cost and scale |
| `ITEM-6145-6.3-017-PROC` | new | Binding maximum price |
| `ITEM-6145-6.3-018-PROC` | new | Binding minimum price |
| `ITEM-6145-6.3-019-PROC` | new | Binding minimum wage in the competitive model |
| `ITEM-6145-3.2-002-PROC` | existing | Define and illustrate demand and supply |
| `ITEM-6145-3.2-006-PROC` | existing | Discuss and illustrate the principle of equilibrium price |
| `ITEM-6145-3.2-010-PROC` | existing | Analyse simple market situations with changes in supply and demand |
| `ITEM-6145-3.2-017-PROC` | existing | Analyse such changes to show effects on price |

Use exact existing task data wherever enhancing an existing card. For a genuinely necessary change, record it and update the relevant worked calculation/claim and derivatives, rather than quietly drawing a different case. New examples must be original invented Namibian cases, N$, British English. Do not copy official diagrams, question text or marking wording.

## Mandatory pace: one diagram pair at a time

Vitalis explicitly requires sequential, meticulous visual authoring. This overrides any generic instruction allowing Claude to author topics in parallel. Do not spawn parallel diagram authors. Finish one card’s question/answer pair, its note integration and review log before starting the next card. Follow the item order in the visual work order.

For each of the 12 cards:

1. Read the relevant syllabus outcome, current reviewed notes and work-order requirement. State the intended economic relationship and the question’s given facts, expected response and mark allocation before plotting.
2. Declare the original data/model, axes, units, curve equations or coordinates, domains and assumptions. Identify whether numbers are illustrative; do not imply schematic curves are empirical observations. Do not force numerical precision onto a purely conceptual relationship.
3. Calculate expected intersections, points, quantities, shifts, slope/elasticity distinctions or extrema independently of the drawing code. Use explicit analytic/numeric assertions appropriate to that figure; merely checking that a PNG exists is insufficient. Cross-check calculated values against the question and textual answer.
4. Generate the question and answer images from the saved data and reproducible plotting code. A question image must contain only the supplied stimulus/starter; the solution must not leak onto it.
5. Inspect both rendered PNGs visually at full size and phone-sized width. Check axis direction and units, labels, line styles/arrows, curve positions, clipping, overlap and legibility. Check greyscale distinction where colour differentiates curves.
6. Perform a fresh second pass against the economics and independently calculated expected values. Check that the curve movement actually follows the stated cause, the solution matches the prompt, and the four-point visual rubric credits what is asked. A program can accurately draw a wrong model; visual appearance alone is not evidence of economic correctness.
7. Fix any discrepancy and repeat the relevant calculations, render and visual inspection. Save a per-card checklist with model/data paths, checks actually run and their results, inspected image paths, hashes and any remaining limitations. Do not record a second independent model review when only self-review occurred. If a substantive issue remains unresolved, report the specific issue rather than moving on as though the pair passed.
8. Only after the pair is clean, integrate its canonical note references and asset-manifest entries, update progress in STATUS, and proceed to the next card.

Use ordinary code-based plotting/vector tools suitable for precise economic curves. Preserve the renderer and declarative inputs so Codex can reproduce and review every image. Do not use generative illustration tools for these plots. Claude’s per-pair self-check is followed by independent Codex review of all 24 images and associated answers; the two are different checks.

## Author the economics, not a decorative picture

- Each card’s target and visual requirements are explicit in the work order. Keep its subtype, AOs, Bloom level, command and tariff. A Use-4 construction has a concrete four-point visual rubric. Include economic reasoning in the model answer, but do not award unrequested extra marks.
- Put the starter/data/original state on the question image. Put the completed solution on the answer image. The question must not give away a labelled answer it asks the learner to construct or identify.
- Derive original curves from declared values. Independently solve intersections, check which curve moves and why, quantify shortages/surpluses where used, and verify all points against equations or supplied schedules. Use competitive-model and binding-control conditions. A control alone does not shift curves; distinguish supply from sales.
- For elasticity, control units/scales and reference points. Do not infer elasticity from visual steepness alone or call every steep supply curve inelastic. Do not confuse LRAC with total cost or short-run diminishing returns. Do not imply a straight PPC has increasing opportunity cost.
- Render programmatically from a declarative specification with a repeatable subject-owned renderer under this workspace. Do not hand-correct SVG coordinates after generation or use text-to-image output for precise economic curves. The standard renderer only understands business break-even charts and cannot validate these figures.
- Use high-contrast lines distinguishable in greyscale, clear curve/axis labels and arrows, and sufficient font size for phone-sized display. Multi-panel comparisons must remain readable as a single image on one card side. Review every PNG at a narrow display width and in offline notes.

## Canonical schema, offline notes and the asset manifest

Write canonical items only in each assigned topic’s existing learning-items JSON; add new claims only where the visual concept needs them, with explicit source provenance. Notes live in content-units, not directly edited Markdown. Teach the visual before a card requires it. Add/correct objective mappings to cover the new planned diagram objectives without deleting old mappings.

Do not invent `question_asset_id` or `answer_asset_id` fields in canonical learning items: the repository schema does not have them. Keep a separate manifest keyed by item ID with question/answer image paths, master/data paths, hashes, descriptions and exact semantic values/relationships. Put all necessary solution facts in canonical_answer and marking_guidance as text as well.

For offline notes, canonical block text may reference the local image as `diagrams/<derived-image-name>.png`, resolving under the topic directory. Render notes with the standard renderer. A reproducible subject-owned publication helper must run the standard publisher, copy the referenced PNGs into the generated publication’s notes/diagrams directory and verify every image reference resolves. Copy the asset manifest with generated publication-relative paths as an upload sidecar. Do not edit exported notes or JSON by hand, and do not assume the standard publisher copies arbitrary new assets.

The repository-relative manifest is the bridge to later import, not a live URL list. Local files are reviewed first. No cloud upload, classroom write, Git commit or push is included in this authoring handover.

## Current YYeni integration design

Verified via the live MCP flashcard contract: each imported card can carry one managed `question_asset_id` and one managed `answer_asset_id`. The app stores the resulting question/answer image URLs; its teacher upload flow uses GCS, and the learner pages render these images separately. Use one composite image per side for multi-panel figures.

Later, with the classroom import authorised, import approved PNGs through the YYeni managed-image workflow and record returned IDs by repository item ID and side. Preview card import with those IDs, show the exact classroom/cards, obtain teacher approval, confirm and reconcile saved cards/assets. Do not store an expiring signed upload URL or raw markup link in place of a managed asset attachment. Current image IDs, storage ACLs, learner drawing input and live Recall grading still need verification at import time.

## Checks and independent review

Preserve reviewed conditions, legal qualifications, homogeneity wording, National Income valuation basis and correct age-dependency interpretation. If a claim changes, increment its revision, update all claims_seen and record reviewed_unchanged on unchanged citing artifacts. Re-stamp edited blocks/items with operations/tools/restamp.py, regenerate notes, run the topic checks and what_to_fix.

Do not publish incomplete topics while the other author’s slots are missing. After all planned cards exist, run all 28 checks and reconcile 625 items exactly. Keep warning/not_run results visible. `depictions.chart_model: none` means the shared checker cannot judge these curves; it does not constitute visual validation. Supply a separate reproducibility/geometry report and a thumbnail/contact-sheet index for Codex to inspect every question and answer image.

Record every affected block/item, asset path and hash and every deviation. Stop for **Codex review of the visual changes**. Codex checks all 24 images, coordinates, mechanisms, textual answers, rubrics, image references, learner answer leakage and narrow-display legibility. A PUBLISH result alone cannot substitute for that review. Report completed/blocked items and exact counts; do not claim a cloud upload or classroom import.
