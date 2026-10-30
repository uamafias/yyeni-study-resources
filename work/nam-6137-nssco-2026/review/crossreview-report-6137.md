# 6137 NSSCO Geography: whole-subject cross-review (Claude), 30 October 2026

Codex authored the text and Claude reviewed it (playbook step 6), following `review/HANDOVER-claude-crossreview-6137.md`.

**Verdict: repaired, but not yet publishable.** The subject is publishable after:
1. Codex verifies the cross-review repairs and re-accepts the 10 visual resources whose bound cards changed;
2. Vitalis approves the two map repairs, and the maps are authored and accepted.

The plan is sound enough to repair within. The four plan problems listed below do not block publication.

Nothing was published, committed, pushed, uploaded or imported. No whole-subject acceptance (`review/subject-acceptance-6137.json`) was created. No Codex acceptance was written.

## 1. Codex's eight visual repairs: confirmed

I re-inspected the re-rendered images and the bound card records:
- 1.1-03: K now replaces N.
- 1.5-08: aim 2 is "not demonstrated" and overall success is "unproven".
- 1.6-03: the titles now say "Schematic" and "Simulated", with the model valid time.
- 2.3-03: the formula reads `(Yes ÷ n) × 100` on both sides.
- 3.2-01: the marker no longer covers the region name.
- 4.1-01 (P05): the working reads `12/20 × 100 = 60%` and `16/20 × 100 = 80%`.
- 4.2-07: "shallow" is removed.
- 4.2-09: the reference is image-relative ("farther back, beyond the belt of trees").

All eight are correct. Three cosmetic residues remain, all low and not learner-facing:
- The docstring of `r_1_1_03.py` still mentions N.
- The analysis panel in 1.6-03 is labelled "model valid time", although it is an analysis.
- The bound cards' `context.situation` text still says "awaiting Codex visual review". It was deliberately not edited, because editing it would invalidate the acceptances. Codex can update it at re-acceptance.

## 2. Deterministic checks (rerun after all repairs)

| Check | Result |
|---|---|
| `run_checks.py`, all 18 topics | 40 PASS, C-18 WARN (AO mix by item count), C-35/C-41/C-43 NOT_RUN, zero FAIL. Decision PUBLISH everywhere. |
| Slot reconciliation (own script) | 801/801 slots, each with exactly one item. Subtype, AOs, Bloom, command word and tariff match. No extras or duplicates. |
| Claims | 1,044 original plus 107 added in this review, giving 1,151. No original claim text was rewritten. |
| Copied wording vs 15 papers and 7 report extracts | 0 runs of 8 or more words. |
| Copied wording vs `assessment-evidence/extracted` (35 files, the guard's own source set) | 0 runs of 8 or more words. |
| Word budgets | Every content unit lies within its contract min–max (the C-checks pass). |
| Read-only preflight (`publish_guarded_6137.py`) | 23 blockers, listed in §6. |

## 3. Method

- **Readers:** six read-only reviewers (Claude) covered 3–4 topics each. Each read:
  - the syllabus objectives and syllabus PDF first;
  - then the contracts, work orders, misconceptions and examiner evidence;
  - then every notes file in full and every one of the 801 items (prompt, answer, rubric and every package part).
- **Claim ledgers:**
  - read in full for 1.1–1.7, 3.2, 3.3, 4.1 and 4.2;
  - read selectively for 2.1–2.6 and 3.1 (Namibia-specific claims), with the notes text checked directly.
- **Lead checks:** I checked every finding against the syllabus wording and the cited block before accepting it. Repairs were then made by the same reviewers under a fixed repair brief:
  - no label or slot changes;
  - word budgets respected;
  - every new real-world fact verified against a cited source;
  - protected (image-accepted) artefacts edited only as a last resort.
- **Lead re-reads and corrections:** I re-read the repaired text and corrected five overstatements:
  - air links to Frankfurt;
  - "northern cattle cannot be sold overseas";
  - "parks cover the whole coastline";
  - the Zambezi Region's borders (it borders Zambia and Botswana, not Angola);
  - a double-credited mean in 1.5-P07.

  I also fixed one miscited article title, and removed mark tags from five rewritten prompts for consistency.
- **Logging:** every change is logged, with the issue id and the before and after text, in `review/crossreview-text-changes-6137.jsonl` (534 entries). All topics were restamped and re-rendered with `assets/code/topic_done.sh`.

## 4. Findings

There are **106 findings: 22 high, 46 medium, 38 low, none critical.** Full YAML records are in `review/crossreview-findings-6137-g1.yaml` … `-g6.yaml`, in the REVIEWER brief format.

The reviewers found **no inverted causal mechanism, no wrong calculation and no false learner-facing fact** in the original text; every worked figure was recomputed. The defects follow one pattern (see the memory note on Codex authoring): the text is accurate but hedged and abstract, so syllabus-named and examinable content is missing. Judgement cards were built so that the answer is always "Disagree", and some prompts state their own answer.

| Topic | H | M | L | Main repairs |
|---|---|---|---|---|
| 1.1 | 1 | 1 | 2 | Convection currents drag the plates; why people live in hazard zones; the LEDC/MEDC death-toll contrast |
| 1.2 | 1 | 1 | 0 | Weathering landforms (scree, exfoliation dome, tor, caves); rock resistance, colour and grain size |
| 1.3 | 1 | 2 | 1 | Falling volume causes deposition (Kuiseb); bedrock seepage; Okavango Delta; Ruacana, Popa Falls, Fish River Canyon |
| 1.4 | 1 | 0 | 2 | Seif dunes near Swakopmund (two-direction winds, Orange River sand); star-dune growth and slip faces |
| 1.5 (P3 2026) | 1 | 2 | 5 | Wave energy and form; longshore drift linked to the prevailing wind; pebble sorting across the beach; discordant coast; Pelican Point; field equipment |
| 1.6 | 1 | 3 | 2 | Six's thermometer (reading, magnet reset); screen height and wood; why altitude is cooler; Benguela, the subtropical high and the ITCZ |
| 1.7 | 1 | 4 | 0 | Climate explanation for each region; welwitschia, baobab, camel thorn; deforestation and the water cycle; matching misconception card |
| 2.1 | 0 | 5 | 3 | EEZ, licences, closed seasons, patrols; trade winds and upwelling; length of coast; causes of overfishing; Namibianisation and onshore processing |
| 2.2 | 2 | 2 | 1 | Red Line, colonial land division, the 1995 Land Reform Act, Green Scheme (Etunda), Aussenkehr and Naute; desertification practices; conservation agriculture |
| 2.3 (P3 2026) | 3 | 2 | 3 | Bi-polar grid design and use; footpath erosion against distance from a hot spot (systematic sampling); business surveys and question design; named sites and the Etosha case |
| 2.4 | 1 | 4 | 3 | 1998 White Paper goals, the off-grid master plan, electricity imports, the Caprivi Link, fuel imports; coal pollutants; HEP penstock and siting; trimmed above-level storage physics |
| 2.5 | 1 | 3 | 2 | Namibia's water sources (border rivers, aquifers, dams, desalination); benefits and problems of dams; Cuvelai floods and the 2024 drought; Goreangab pollution |
| 2.6 | 1 | 2 | 4 | Stakeholder roles (1996 Act, quotas, joint ventures, game guards); hunting and game-meat income; positive wildlife effects; conflict types; protected-area belt |
| 3.1 | 2 | 3 | 4 | Namibia's population distribution (2023 census); Windhoek migration; China's one-child to three-child policies; HIV/AIDS mortality; equal-size misconception data |
| 3.2 | 3 | 3 | 0 | Explaining the HIV distribution; effects of condoms and ART on the pyramid and the economy; Namibian stakeholder efforts; AIDS definition; national impacts |
| 3.3 | 2 | 2 | 2 | Burgess and LEDC models, illustrated with Windhoek (Katutura, Havana); site, situation, functions, push and pull, Kolmanskop; CBD congestion and solutions; giveaway prompts |
| 4.1 | 0 | 2 | 3 | Field equipment and methods; model answers; cross-references; plainer register; pie chart and best-fit line |
| 4.2 | 0 | 5 | 1 | Landforms from contours and the V rule; three scale types; a non-cardinal back bearing; describing relief, drainage and land use; leaked author instructions removed |

**Repairs:** 168 notes blocks and 147 items changed, and 107 claims were added (one per new fact set, each citing its source URL). Of the 46 "How far do you agree" flashcards, 10 still open with "Disagree", each resting on an evidence-limit argument; the other 36 now weigh evidence on both sides.

**Not fixed, or only partly fixed:**

| Issue | Status and reason |
|---|---|
| 1.1-003 (stale `context.situation`) | Not fixed: it is on bound cards. Codex can update it at re-acceptance. |
| 1.3-003 | Partly fixed: named landforms are in the notes only. A card would displace another landform. |
| 1.4-001 | Fixed, except berg winds, which could not be verified. |
| 1.7-002 | Partly fixed: branchless rainforest trunks were not sourced, and no card was added. |
| 2.2-004 | Not fixed: cards 013–016 wait for the map. When it is added, remove the distribution wording from their prompts. |
| 2.3-002/003 | Fixed in the notes and in cards 037/039/041. The image-bound packages P04 and P05 still use the 0–2 score and pedestrian counts; see plan problems. |
| 2.3-006/007 | Not fixed: low severity, on protected packages. |
| 2.3-008 | Partly fixed: the P07 objective mapping is a plan label. |
| 2.4-001 | Partly fixed: no fuelwood-depletion area could be verified. |
| 3.1-001/005 | Partly fixed: no Windhoek age-structure data and no verified under-population or forced-migration example. |
| 3.3-004 | Partly fixed: the protected image alt text still describes the layout. |
| 4.1-003 | Partly fixed: no cross-reference added to protected packages P04–P07. |
| 4.2-003 | Partly fixed: the other bearing cards are image-bound with fixed tariffs. |

## 5. For Codex to verify (exact acceptance is now stale for these)

**Visual resources whose bound card text changed (10).** Their acceptance must be re-run:
- VIS-6137-1.5-05, -06, -07, -08: cards 1.5-P03, P04, P05, P06, P07;
- VIS-6137-3.3-01, -02: cards 3.3-002 to 005 and 015 to 021;
- VIS-6137-4.1-01, -02, -03: cards 4.1-P04, P05, P07, part (b) answers only;
- VIS-6137-4.2-03: card 4.2-019-CALC.

No image, master or spec changed.

**Reviewed notes blocks edited (3).** In each, one leaked author-instruction sentence was deleted:
- BL-6137-3.3.01-05
- BL-6137-3.3.04-14
- BL-6137-4.1.04-09

**New claims (107).** These are status `unverified`, with method "Added by Claude during whole-subject cross-review". Each `CROSSREVIEW-6137` evidence entry carries its URL and access date. These are weakly sourced and need checking first:
- CL-6137-2.4.10-R2 (no refinery; fuel through Walvis Bay): rests on a search excerpt and news reports.
- CL-6137-2.5.05-03-R1 (desalination plant): rests on Wikipedia.
- The NSA 2023 census figures: from an NSA presentation on a third-party site.
- CL-6137-2.3.07-R1 (air links): rests on Wikipedia.
- CL-6137-2.6.\* (2022 conservancy figures): from NACSO.

Several Wikipedia-based claims (Sossusvlei, Red Line, Katutura, Kolmanskop) should be checked against a primary source.

**Original claims (1,044).** Their verification status is unchanged (`unverified`). The review checked their content through the notes and cards, but not every ledger was read line by line (§3), so I did not mark them verified.

## 6. Remaining publication blockers (read-only preflight: 23)

- **5:** unresolved stimulus, and **5:** map-stimulus binding absent. These are cards 2.2-013 to 016 and 2.6-002.
- **2:** unapproved map-plan concerns (2.2, 2.6). See `authoring/MAP-REPAIR-PROPOSALS-6137.md`; Vitalis's approval is pending.
- **10:** "Reviewed card text absent or stale" (§5). This is expected after the repairs.
- **1:** independent whole-subject acceptance not recorded. Deliberately not created: it must follow Codex's verification and the maps, with the `snapshot()` and manifest hash then current.

## 7. Plan problems (for the planner; nothing in `curriculum/`, contracts or work orders was changed)

1. **The practical-activity objectives were abbreviated in the registry.**
   - Affected objectives: OBJ-6137-2.3.91/92/93 and 3.1.91. Their `syllabus_text` reads, for example, "Tourism environmental-quality assessment", while the full syllabus paragraph is kept only in `planning/registry-provenance-6137.json`.
   - What was dropped: the bi-polar grid design, footpath erosion against distance from a hot spot, business surveys and question design. This content never reached the author.
   - This is the known work-order-builder defect. It was repaired within the existing slots.
2. **Two image-bound 2.3 Paper 3 packages still model the older method.** P04 (environmental quality, 0–2 score) and P05 (footpath counts) need new stimulus images to model the bi-polar grid and the distance design.
3. **The 4.2 bearing cards are image-bound with fixed tariffs.** A measured non-cardinal bearing would need a new image, and the trivial 3-mark tariffs on 015 and 017 cannot change.
4. **Labels the reviewers wanted changed.** Card objectives 1.7-011, 2.2-021, 2.3-006, 2.3-P07 and 3.1-034 were rewritten within their slots instead. The P07 mapping to OBJ-2.3.93 remains odd.

Case-study selection was **not** treated as a defect. The syllabus states its case studies are not prescriptive, and Vitalis approved the planner's register. Unselected cases (Kenya, Mauritius, Fukushima, Iceland, China HEP, Horn of Africa, Swaziland) were not built, except one verified sentence each for Fukushima and Iceland where an objective had no example at all.

## 8. Changed paths

- `topics/*/content-units/*.json`, `topics/*/learning-items/*.json`, `topics/*/claims/canonical_claim_ledger.json`, the rendered `topics/*/*.md` and `topics/*/qa_report.json` (all 18 topics).
- `review/crossreview_edit_6137.py` (repair helper), `review/crossreview-text-changes-6137.jsonl`, `review/crossreview-findings-6137-g1…g6.yaml`, this report and `review/HANDOVER-codex-verify-crossreview-6137.md`.
- `review/copied-wording.md` (regenerated by the tool).
- `STATUS.md`.
