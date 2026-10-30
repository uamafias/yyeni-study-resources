# Codex handover: review the final 6137 resources and Claude's cross-check of your repairs

Workspace: `work/nam-6137-nssco-2026/`. Owner: Vitalis P Haupindi. Prepared by Claude, 30 October 2026, under `review/HANDOVER-claude-final-resources-6137.md`.

**Rules.**
- Do not publish, commit, push, upload or import.
- Do not create `review/subject-acceptance-6137.json`. Claude records it after your acceptance.
- Never self-accept your own changes. If you change an image, a bound card or a reviewed notes block, return the diff to Claude.

## Current state

- **Topics:** all 18 give 40 PASS, C-18 WARN and C-35/C-41/C-43 NOT_RUN.
- **Slots:** 801/801 reconcile, with 0 problems.
- **Claims:** 1,153.
- **Copied wording:** 0 runs of 8 or more words against the 35 assessment extracts.
- **Map amendment:** `planning/verify_map_revision_6137.py` passes.
- **Manifest:** 56 resources and 112 bindings. SHA-256 at handover: `8eaf1706e186d8bedc2f62f237a0c797766f1c537dcddf8a9fa17ea303ac1b9f`. Your 52 untouched acceptances are carried over byte for byte.
- **Read-only preflight: 6 blockers, all expected:**
  - VIS-6137-2.2-02: independent review;
  - VIS-6137-2.6-02: independent review;
  - VIS-6137-2.3-01: independent review;
  - VIS-6137-2.3-02: independent review;
  - VIS-6137-3.3-02: reviewed card text stale (alt text only; see F11);
  - whole-subject acceptance.

## 1. New map VIS-6137-2.2-02 (farming): cards 2.2-013, 014, 015, 016

- **Checklist:** `assets/checklists/ITEM-6137-2.2-013-INTERP.md`. Code: `assets/code/r_2_2_02.py` and the new shared base `assets/code/namibia_map.py`.
- **Sides:** one question map, plus a separate answer side for each card (`ITEM-6137-2.2-0NN-INTERP-VIS-6137-2.2-02-answer.png`; 013 uses the plain `-answer.png`).
- **Base layer change from the handover.** The gbOpen file you named (NAM-ADM1-33880854) was downloaded and checked. It has only 13 pre-2013 regions ("Caprivi", a single "Kavango"), so I used geoBoundaries **gbHumanitarian** NAM-ADM1-65246180 instead: 14 regions, Namibia Statistics Agency via HDX, CC BY 3.0 IGO. Please confirm that this substitution is acceptable.
- **Thematic data:** Atlas of Namibia 2022 data (CC BY 4.0), acquired with the Harvester:
  - figure 8.02: farming-system areas (from Mendelsohn 2006) and irrigation points;
  - figure 8.06: cleared land, gridded to 0.1°, with cells shaded where at least 15 % is cleared;
  - figure 8.07: farm cadastre, merged and outlined.
- **Card 015 inset:** titled "schematic, not a surveyed farm".
- **Measured evidence in the spec:**
  - share of each region in dense crop cells: Ohangwena 0.41, Oshana 0.30, Omusati 0.27, Zambezi 0.19, Oshikoto 0.15, Kavango West/East 0.07/0.06, Kunene 0;
  - inside the commercial farms: Otjozondjupa entirely cattle; Hardap and //Karas 0.66/0.60 small stock.
  - There are 15 automated data checks.
- **Card text:**
  - all four answers and rubrics were rewritten to the data;
  - the 013 and 016 prompts no longer list the answer;
  - new claim CL-6137-2.2.04-R1 is taught in BL-6137-2.2.04-01 (C-07) and cited by 013, 014 and 016.
- **Please check:**
  - that the class names are fair ("Mainly cattle" etc.: the source classes some communal northern land as cattle);
  - the dates and limits: farming systems 2006; the national cleared-land layer is undated; irrigation is shown as location only;
  - that the Atlas data downloads fall under the book's CC BY 4.0 statement.

## 2. New map VIS-6137-2.6-02 (conservation): card 2.6-002

- **Checklist:** `assets/checklists/ITEM-6137-2.6-002-INTERP.md`. Code: `assets/code/r_2_6_02.py`.
- **Boundaries.** The Atlas figure 8.09 protected areas and conservancies. The Atlas source note says these were generated from Government Gazette coordinate tables. The NACSO gazette and conservancy pages returned 404, so no gazette schedule was traced directly.
- **Data checks.** The areas match the Atlas attributes within 5 %:

| Feature | Area from geometry | Atlas attribute |
|---|---|---|
| Etosha | 23,064 km² | 22,941 km² |
| Torra | 3,512 km² | 3,494 km² |
| Salambala | 941 km² | 936 km² |

  - Torra is in Kunene and Salambala in Zambezi; both were registered in June 1998.
- **CCF centre.** A point at the GeoNames farm Elandsvreugde (12761849). CCF's own page places its centre on that farm. The point is 40.2 km from Otjiwarongo at 93°.
- **Distance wording.** The answer says about 40 km "in a straight line". BL-6137-2.6.01-09 now explains that the road distance is a little farther (the existing claim's "about 44 km").
- **Key.** It says "Conservation centre" without "point", because spotting that the centre is a point earns a mark.
- **New claim** CL-6137-2.6.01-R1.
- **Please check:** that 89 registered records (2020) against the notes' 86 conservancies (2022) is acceptable with the dated key.

## 3. Rebuilt practical packages VIS-6137-2.3-01 (P04) and VIS-6137-2.3-02 (P05)

See the "Revision" sections in `assets/checklists/ITEM-6137-2.3-036-PROC.md` and `-038-PROC.md`.

**What did not change.** The 036, 038 and P07 PNGs are byte-identical to your accepted versions; the SHA-256 was checked. Only the P04 and P05 sides and the shared master and spec changed.

**P04: a true bi-polar grid.**
- Five paired rows, scored +2 to −2, with the positive description on the left.
- Five sites every 100 m from a car-park hot spot, surveyed at the same time (10:00–10:30).
- Totals −6, −3, +1 (blank), +5, +8. H1 supported; H2 (facilities) not supported.

**P05: erosion against distance from a hot spot.**
- Stations every 30 m from 0 to 120 m.
- Reproducible method: widths by tape at right angles, edge to edge; depth by pole and five ruler readings.
- Widths 220, 170 (blank), 140, 155 (blank), 95. The rise at S4 is explained by the recorded wet hollow.
- Depths 8.0, 6.4, 4.2 (calculate), 3.0, 1.6.
- No visitor counts are used; the card states that distance only stands in for years of use.

**Both cards.** All 12 parts keep their tariffs and AOs. The rubrics still name hypothesis, sampling, data, conclusion and evaluation. The cards now cite CL-6137-2.3.91-R1/R2 and 2.3.92-R1/R2. The business and people survey method stays taught in BL-6137-2.3.93-04 and the 2.3 survey cards; no change.

## 4. Claude's cross-check of your text repairs

The full record is in `review/claude-crosscheck-codex-repairs-6137.yaml`.

**Confirmed correct:**
- census versus microdata cooking fuel (50.1 % / 84.6 %);
- the conditional U=U wording, and no fixed net growth effect;
- altitude cooling;
- veterinary restrictions varying by product and destination;
- groundwater and perennial rivers;
- desalination opened in 2010 against the 2013 supply contract;
- the date-bounded Windhoek reserves (August 2025);
- the settlement alt text no longer leaking answers;
- all 23 claim revisions at revision 2, with `claims_seen` consistent across 60 citing references.

**Corrected.** Logged in `review/crossreview-text-changes-6137.jsonl` with issue IDs XC-F01 to F11. Five claim revisions were raised and every citer's `claims_seen` moved.

| Finding | Severity | What was wrong | What was done |
|---|---|---|---|
| **F01** | high | Your "45 per cent of electricity produced in Namibia" is wrong. Ruacana produces most local generation: 95 % until 2016 (Atlas node/126). The Atlas sentence (node/144) says "up to 45 per cent of Namibia's electricity", with no year or qualifier. | Restored; CL-6137-2.4.04-R1 raised to revision 3. |
| **F02/F03** | high | The HIV distribution lost all its locational content, but the syllabus says "account for its spatial distribution". | Restored the borders of Zambezi and Ohangwena, the Trans-Caprivi Highway through Katima Mulilo (KfW evaluation; B8), and dense Ohangwena against sparse Kunene, keeping your non-causal caveat. CL-6137-3.2.02-R1 raised to revision 3; the 3.2-P03 answer and rubric now name Zambezi's borders and route. |
| **F04/F05** | medium | "Payments overseas" is wrong: imports come from neighbouring countries. The undated "less than half" is out of date: Namibia produced 51.6 % of its own electricity in 2025 (The Namibian, 19 July 2026; a single source). | Wording corrected; CL-6137-2.4.10-R1 raised to revision 2. |
| **F06** | medium | The Stevenson screen claim lost the school height and the wood point that its citers still teach. | CL-6137-1.6.02-01-R1 raised to revision 3 ("about 1.2–1.25 m"; wooden walls conduct heat poorly). |
| **F07** | medium | 3.2-016 still said "about 90 % Christian", which no claim supports. | Reworded without the figure. |
| **F08** | medium | The Red Line dates (1896–1907, early 1960s) have no source: the Atlas gives none. | Dates removed from BL-6137-2.2.05-02, and the overstatement softened. The diseases, which the Atlas supports, were added back to CL-6137-2.2.05-R2 (revision 3). |
| **F09** | medium | The 2.5-008 rubric needs a named aquifer, but the answer named none. | The answer now names the Karstveld and Stampriet (CL-6137-2.5.02-R1 supports this). |
| **F10** | low | A rubric typo in 3.2-018. | Fixed. |
| **F11** | low | The 3.3-015 to 021 alt text said "use its … scale", but the town plan has no scale bar. | Now reads "Schematic town plan, not to scale, with a land-use key". This is the only change to a bound card, so VIS-6137-3.3-02 needs re-acceptance. The 3.3-002 to 005 plans do have a scale and are unchanged. |

## What to return

1. Accept or reject VIS-6137-2.2-02, 2.6-02, 2.3-01 and 2.3-02, and re-accept 3.3-02, with item and notes-block hashes as before.
2. Your verdict on the cross-check corrections and the two new claims.
3. Any diff you make, for Claude to re-review.

After that, Claude records the whole-subject acceptance against the final `snapshot()` and manifest hash. Publication remains a separate later step.

## Changed paths in this round

**Code**
- New: `assets/code/namibia_map.py`, `r_2_2_02.py`, `r_2_6_02.py`.
- Changed: `r_2_3_01.py` and `r_2_3_02.py` (P04/P05 layers only); `build_manifest.py` (keeps the existing manifest author line); `review/crossreview_edit_6137.py` (adds `revise_claim`).

**Assets**
- New: `assets/sources/maps/` (geoBoundaries, GeoNames and Atlas data, with the harvest logs in `_harvest/`).
- New: the masters, specs, images, checks, inspection previews and records for VIS-6137-2.2-02 and 2.6-02.
- Updated: the P04 and P05 images, the 2.3-01/02 masters and specs, three checklists, and `assets/asset-manifest-6137.json`.

**Topics**
- 2.2: cards 013–016; BL-6137-2.2.04-01; BL-6137-2.2.05-02; claims.
- 2.6: card 002; BL-6137-2.6.01-09; claims.
- 2.3: P04, P05.
- 1.6, 2.4, 2.5, 3.2, 3.3: as listed in the table.
- Rendered notes and QA reports for every touched topic.

**Review**
- This handover, `review/claude-crosscheck-codex-repairs-6137.yaml`, and the change logs (`assets/records/text-changes-6137.jsonl`, `review/crossreview-text-changes-6137.jsonl`).
