# 6145 visual authoring report (revision-01): for Codex review

Author: Claude (Opus 5.5), 28 October 2026, working to `CLAUDE-DIAGRAM-HANDOVER-6145.md` and `planning/revision-01/claude-visual-work-order.json`.
**Every check below is self-review. No second model has reviewed this work.**

> **Update, 28 October 2026:** Codex has since reviewed and accepted all 12 cards after repairs; see `review/codex-visual-review-6145.md` and `diagrams/CODEX-REVIEW-6145.json`. The cardtext files are now superseded by the repaired canonical items. **Do not rerun `apply_card_text.py`**: it stamps items fresh and would remove the review repair history. Re-rendering and verifying remain safe.

## Status

All 12 diagram cards are complete, done one pair at a time in the work-order order:

- **New cards:** 1.1-011, 3.3-019, 3.3-020, 4.2-025, 5.4-031, 6.3-017, 6.3-018, 6.3-019.
- **Existing cards, enhanced:** 3.2-002, 3.2-006, 3.2-010, 3.2-017.

**Files:** 12 question PNGs and 12 answer PNGs, plus 24 SVG masters. They sit at the paths the work order specifies (`topics/<T>/diagrams/`). Every pair has:

- a declarative spec;
- an independent verifier report;
- a checklist;
- 390-px and greyscale previews.

**Not done, by design:**

- No cloud upload and no classroom or YYeni write.
- No Git commit or push.
- No write to `publish/`. Publication waits for all 625 slots.

## Counts and reconciliation

| | |
|---|---|
| Planned slots (live work orders) | 625 |
| Filled | 588 |
| Unfilled | 37, all Codex's nonvisual slots. None of mine. |
| Verifier checks across the 12 cards | 542 passed, 0 failed |
| Copied wording (10 papers + 5 report volumes) | 0 runs of 8+ words |
| Topics at PUBLISH | 1.1 and 6.3 (every slot filled; C-18 warns; C-35, C-41, C-43 not_run) |

Every other topic fails C-42 (see below). Some also fail C-05, C-06, C-15 or C-27, and in each case only because a Codex slot is still empty.

## Where to look

| What | Path (relative to the workspace) |
|---|---|
| Index of every image, spec, checklist and report | `diagrams/contact-sheet.md` |
| All 24 images on one sheet | `diagrams/contact-sheet.png` |
| Declarative inputs (model, equations, points, scales, labels, layers per side) | `diagrams/specs/<ITEM>.json` |
| Renderer (spec → SVG → Chromium PNG at 1.5×; records measured text boxes) | `diagrams/render_6145_diagrams.py` |
| Independent verifier (restates each model by hand; exact fractions; reads geometry back from the SVG) | `diagrams/verify_6145_diagrams.py` |
| Verifier results with SHA-256 of all four files per card | `diagrams/checks/<ITEM>.json` |
| Per-card record: target, model, calculations, visual fixes, second pass, canonical changes | `diagrams/checklists/<ITEM>.md` |
| Canonical text applied per card (item, claims, notes blocks) | `diagrams/cardtext/<ITEM>.json` via `diagrams/apply_card_text.py` |
| Asset manifest keyed by item ID and side (paths, hashes, alt text, `question_asset_id`/`answer_asset_id` = null) | `diagrams/asset-manifest.json` via `diagrams/build_manifest.py` |
| Publication helper (standard publisher, then copies referenced PNGs and writes the `diagram-assets.json` sidecar) | `diagrams/publish_6145_with_diagrams.py` |
| Phone (390 px) and greyscale previews | `diagrams/inspection/` |

### Reproduce

Run from the repository root:

```bash
python3 work/nam-6145-nssco-2026/diagrams/render_6145_diagrams.py        # all 24 SVG + PNG
python3 work/nam-6145-nssco-2026/diagrams/verify_6145_diagrams.py        # exits 1 on any failure
python3 work/nam-6145-nssco-2026/diagrams/build_manifest.py
python3 work/nam-6145-nssco-2026/diagrams/make_contact_sheet.py
```

**Environment:** Python 3.13, Playwright 1.58 with its Chromium build, Pillow 11.3, system Arial. Re-rendering on this machine gives byte-identical SVG and PNG files; this was checked after each renderer change. Another machine's fonts may move text by a pixel or two, but they cannot move the geometry.

**Publication helper:**

- It refuses to run while slots are unfilled.
- It refuses `--allow-incomplete` for the real `publish/` folder.
- A test run into a scratch folder resolved every notes image reference.

## What the verifier checks

### Every side

- PNG present, at 1.5× the SVG canvas.
- Every curve vertex inside its axes.
- Browser-measured text inside the canvas.
- No overlapping text boxes.
- No point marker under a label.

### Every card

- The model restated by hand, with intersections and changes solved in exact fractions.
- Each drawn curve inverted from pixels to data and tested against its equation (≤ 1.5 px), and against every given point (distance to the drawn segments).
- Points, arrows (direction checked by cosine) and spans at the expected coordinates.
- No solution labels or values on the question side.
- The card text states the same numbers.
- The guidance names diagram, labels, original and change, and sums to the 4-mark tariff.

### Card-specific invariants

| Card | Invariants |
|---|---|
| PPC | Increasing opportunity cost (5, 15, 25, 35) |
| Elasticity | Same panel and same starting point; the more elastic curve is drawn flatter on screen |
| Labour market | Supply not shifted (curve set D1, D2, S; S byte-identical on both sides) |
| LRAC | Vertical axis is average cost; no total-cost labelling |
| Price and wage controls | Control on the binding side; curve set unchanged; quantities read off the original curves |
| Minimum wage | The word "unemployment" absent |
| Existing cards | Item text hash equals the reviewed stamp, so the text is unchanged |

### What the verifier cannot do

It cannot judge legibility, economic framing or whether a rubric is fair. I did those passes by eye; they are recorded in each checklist. They need Codex's independent look.

## Canonical changes

| Topic | Items | Claims (revision 1) | Notes blocks |
|---|---|---|---|
| 1.1 | +011-PROC | +CL-1.1-09, -10 | +B08 (PPC); B03's PPC paragraph moved into B08 (B03 restamped) |
| 3.3 | +019-PROC, +020-PROC | +CL-3.3-16 to -19 | +B05 (PED diagram), +B06 (PES diagram and limiting cases) |
| 4.2 | +025-PROC | +CL-4.2-22, -23 | +B05 (labour market); B01's diagram paragraph moved into B05 (B01 restamped) |
| 5.4 | +031-PROC | +CL-5.4-37, -38 | +B06 (LRAC); B04's LRAC paragraph moved into B06 (B04 restamped) |
| 6.3 | +017, +018, +019-PROC | +CL-6.3-13 to -18 | +B06 (maximum price), +B07 (minimum price), +B08 (minimum wage) |
| 3.2 | none changed | none | +B06 (movements along both curves); image references added in B02, B04, B05 (restamped) |

Further details:

- **Unit objectives:** each new diagram objective (OBJ-…-1.1-04, 3.3-04/05, 4.2-09, 5.4-06, 6.3-06/07/08) was added to its unit. No mapping was removed.
- **The three moved paragraphs** were my own step-6 additions. Every teaching point in them survives in the new block.
- **Metadata:** no `question_asset_id` or `answer_asset_id` was added to canonical items.
- **Reviewed-content markers:** conditions, homogeneity wording and the other reviewed markers are untouched.

## Deviations and judgements

1. **Card 2 (PED) values.** The first drafts used price rises of 10% and 20%. On a phone, the inelastic curve's movement arrow was then too short to read. I widened the rise to 50% (N$20 → N$30), giving PED of −0.5 and −1.5. The answer says the elasticity applies to this change only, and that elasticity varies along a straight line.
2. **Existing 3.2 question images show only the data table.** Their rubrics award a mark for axes and labels, so starter axes would give that mark away.
3. **Card 8 cites only CL-6.3-17 and -18.** Also citing the revision-2 claim CL-6.3-09 made C-30 warn: a fresh item cannot carry a prior_hash. CL-6.3-17 is derived from CL-6.3-09.
4. **The notes word budget forced very short 6.3 blocks** (35–43 words each). The mechanism is already taught in B02 and B04.
5. **Renderer additions during the work:**
   - one-axis guides;
   - per-side canvas;
   - minor gridlines;
   - suppression of a tick label that clashes with a marked value;
   - arrow offset.

   After each change, all earlier cards were re-rendered and confirmed byte-identical.

## Issues for Vitalis and Codex

1. **Planning defect: contract counts (C-42).** The activated revision-01 contracts set `required_outputs.learning_items` above the work-order slot count in 11 topics. The `item_budget` field is correct in each.

   | Topic | Contract says | Slots |
   |---|---|---|
   | 1.2 | 45 | 22 |
   | 1.3 | 25 | 16 |
   | 2.1 | 48 | 22 |
   | 3.1 | 16 | 12 |
   | 3.2 | 34 | 29 |
   | 3.4 | 17 | 12 |
   | 3.5 | 13 | 9 |
   | 4.3 | 25 | 16 |
   | 5.2 | 23 | 20 |
   | 7.2 | 49 | 24 |
   | 7.3 | 38 | 20 |

   The reviewed baseline was correct (3.2's baseline contract said 29). These topics now fail C-42 however the cards are written; 3.2 would otherwise PUBLISH. The contracts are planner files whose activation hashes are recorded, so I have not edited them. **Fix:** regenerate `required_outputs.learning_items` from the work orders. That is a planning correction for Vitalis and Codex to make.
2. **Word-budget headroom is nearly gone in three units:**
   - CU-6145-4.2: 1,408 of a 1,412 maximum. Codex's DEF cards 4.2-021 to 024 will need to draw on existing text; gross and net pay and the payment methods are already in B01.
   - CU-6145-6.3: 2,009 of 2,010.
   - CU-6145-3.3: 1,134 of 1,135.
3. **Pre-existing C-26 warnings** in CU-6145-3.3.3, 4.2.2, 5.4.1 and 5.4.2 belong to Codex's budget work order and are untouched.
4. **C-35 and C-41 stay `not_run`** (`depictions.chart_model: none`). That is not visual validation. This report and Codex's review are the visual checks.
5. **Metadata on the existing 3.2 cards** still says `context.situation: "Original case or focused retrieval"`, from the original authoring. I left it alone because the reviewed items are preserved exactly.
6. **Check reports regenerated.** Running all 28 topic checks rewrote each topic's `qa_report.json`, a generated file. The copied-wording run rewrote `review/copied-wording.md` (still 0 runs). No other file outside my six topics and `diagrams/` was changed.

## What Codex needs to review

- All 24 images, at full size and phone width.
- The coordinates against each spec and the independent calculations.
- Mechanisms:
  - movements against shifts;
  - binding controls;
  - derived demand;
  - LRAC against total cost;
  - elasticity comparisons.
- The textual answers and the 4-mark rubrics.
- Answer leakage on the question images.
- The 12 note references and the new notes blocks.
- The 16 new claims.
