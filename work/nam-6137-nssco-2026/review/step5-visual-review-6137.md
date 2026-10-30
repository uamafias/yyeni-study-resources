# 6137 independent visual review — Codex, 30 October 2026

**Verdict: accept the 54 delivered resources after repairs. Whole subject remains incomplete and unpublished.**

Scope: 48 generated figures and six licensed photographs; 153 PNG sides/variants, 107 bindings across 102 items. Read all bound prompts, answers and marking guidance and all 55 affected notes blocks. Inspected all 153 images individually, including question-side answer concealment and practice variants; reinspected repaired outputs. This is independent review of Claude's visual work, not Codex approval of Codex's whole-subject text.

## Repairs applied

| Resource | Severity | Defect and correction |
|---|---|---|
| 1.1-03 | Low | Plate K was called N in one answer annotation; corrected to K. |
| 1.5-08 | Medium | Beach-width evidence was treated as proof that the sediment-supply aim failed. Now says aim 2 is not demonstrated and overall success remains unproven; local beach gain remains credited. |
| 1.6-03 | Medium | Generated infrared/weather panels implied real observations. Titles now disclose schematic/simulated data and model valid time; bound card updated. |
| 2.3-03 | High | Percentage formula omitted ×100. Question and answer now show `(Yes ÷ n) × 100`, with answered denominator explicit. |
| 3.2-01 | Low | Answer marker obscured Ohangwena's name; moved clear. |
| 4.1-01, P05 variant | High | Percentage working omitted ×100; both resident and visitor calculations corrected. |
| 4.2-07 | Medium | Opaque-water photograph cannot establish channel depth. Removed “shallow” from card and image. |
| 4.2-09 | High | Oblique photograph had no north reference. Replaced unsupported “north” with position farther back in the image. |

Eight renderer modules repaired and rerendered; their layout/geometry checks pass. Added linked creator/source/licence credits to the six photo answers. Seven card records restamped (one schematic card and six photo cards). Claims, labels, planned slots, contracts and approved scope unchanged. Full machine-readable findings are in `visual-repairs-6137.json`.

## Evidence and limits

- Independent script `check_visual_review_6137.py`: **307 checks pass**, covering 274 manifest hashes, decoding all 153 PNGs, six original-photo SHA-1 comparisons, counts and numerical cross-checks. PROJ independently agrees with the author's Transverse Mercator coordinates within 1 mm. Separate numerical integration confirms the road length within 0.02 m; endpoints, contour vertices, map conversions and selected chart calculations reconcile.
- Manually checked chart readings, denominators, signed displacements, rates versus totals, population dependency counts, geographic directions, gradients, relative scales, causal limits and marking guidance across every bound item. Automated geometry checks alone do not establish semantic accuracy.
- Independently sampled phone/greyscale sheets for 12 resources: 1.2-02, 1.5-01/08, 1.6-03, 2.3-03, 3.2-01 and 4.2-01/04/05/07/08/09. All resources have author phone/greyscale checks; Codex did not independently repeat every preview. Dense charts require opening/zooming the image for small labels; no live YYeni rendering tested. The Karas photo is acceptable for coarse vegetation cover and exposed ground only, not precise colour, species, rainfall or measurements. Farmland location remains unspecified.
- All six originals match the recorded Commons SHA-1 and local SHA-256. Creator/licence/source/change credits checked against archived provenance; live Commons pages additionally verified for Pebble Beach, Gochas and Gamsberg. Live retrieval failed for the other three, so their licence evidence relies on the saved acquisition/provenance record. No new photo acquisition or rights guarantee is asserted. The harvester JPEG false-positive remains a shared-tool issue outside this review.
- Learner text: zero runs of 8+ words against 35 assessment extracts. SVG text scan found 17 candidates: all ordinary numbered ticks, numbered sample sites or the January–December initial sequence with conventional axis labels; manually allowed, no copied assessment prose. See `visual-copied-wording-6137.json`.
- All **18 topics: 40 PASS, C-18 WARN, C-35/C-41/C-43 NOT_RUN, zero FAIL**. All 801 slots reconcile; section budgets pass. Deterministic PUBLISH does not clear the missing map stimuli or whole-subject semantic review.

## Acceptance and publication guard

Each manifest resource now carries Codex acceptance bound to exact asset hashes and every bound card's full JSON hash. A separate receipt records the reviewed notes-block hashes. Changing an asset or bound card invalidates its acceptance; rerun the independent review for any changed material. Do not blindly rebuild the manifest: the generator preserves acceptance only for unchanged asset hashes, and the guard separately checks card hashes.

The publication helper now accepts the plan's null photo master/spec fields while still requiring the conventional master and spec files to exist and be hashed. This repairs the adapter; it does not amend planner files or waive a missing asset. Its successful publication branch has not been run or fully exercised.

Remaining gates: five unbound map cards (2.2-013–016 and 2.6-002), explicit resolution/approval of their two map-plan concerns, creation/review of the additional resources, and Claude's whole-subject review with an exact acceptance snapshot. No whole-subject acceptance was created. No publishing, Git operations, uploads or imports performed.

## Next handover

Claude should cross-check Codex's eight visual repairs and seven card records, then review the whole 18-topic subject, including all 1,044 still-unverified claims. Read `authoring/MAP-REPAIR-PROPOSALS-6137.md`; do not generate the two extra maps until the planner records Vitalis's approval. Preserve the existing repairs and acceptance history; do not rerun bulk text-application scripts. Report changes before refreshing any acceptance. Keep 0455 untouched.
