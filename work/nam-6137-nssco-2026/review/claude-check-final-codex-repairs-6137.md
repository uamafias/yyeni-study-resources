# Claude's check of Codex's final-resource repairs: Geography 6137

Reviewer: Claude, 30 October 2026, under `review/HANDOVER-claude-check-final-codex-repairs-6137.md`. This is an independent cross-vendor check of Codex's four repairs. Claude made no repairs to content in this round.

**Verdict: all four repairs confirmed.** Codex may renew its acceptance of VIS-6137-2.3-01 and VIS-6137-2.3-02 on the hashes in `review/claude-check-final-codex-repairs-6137.json`. That file also records the manifest SHA-256 at the time of checking: `923c3575738b1394432d1a4a43e7619157b4c6f2df72298b4120964e91446aa3`.

| # | Repair | Check | Result |
|---|---|---|---|
| 1 | P04 grid: "Facilities clean / Facilities broken" became "Facilities clean / Facilities dirty" | **Pair:** now a true opposite pair; both ends rate cleanliness. **Images:** viewed the question and answer at full size, 390 px and greyscale; the scores, totals (−6, −3, +1, +5, +8), mean (+1) and plotted points are unchanged. **Renderer:** re-running `r_2_3_01.py` reproduces every VIS-6137-2.3-01 file byte for byte. **Other images:** the 036, 038 and P07 PNGs are identical to Claude's handover hashes. **Text:** neither the card nor the notes use "broken". | confirmed |
| 2 | P05: distance is no longer called a proxy for years of use | **(g):** the answer and rubric now say the survey compares present path form with distance and does not measure visitor use or change over time; this is accurate, and the claim that trampling is usually concentrated near the hot spot is retained. **Remaining wording:** none in topic 2.3 calls distance a proxy for use. **Unchanged:** tariffs, AOs and images. | confirmed |
| 3 | Ruacana: 26 % of all electricity used in 2018/19 | **Source:** the Atlas energy chapter (https://atlasofnamibia.online/chapter-10/energy) says "contributed 26 per cent of all the electricity used in Namibia", for 2018/19. **Text:** CL-6137-2.4.04-R1 (revision 4), BL-6137-2.4.04-03, 2.4-025 and 2.4-P03 agree with it, and no learner text keeps the ambiguous 45 %. **Consistency:** `claims_seen` has 0 mismatches subject-wide. | confirmed |
| 4 | 51.6 % is a December 2025 figure, not an annual one | **Source:** the NSA *Electricity December 2025* report was acquired with the Harvester (`assets/sources/energy/NSA-Electricity-December-2025.pdf`, SHA-256 `4651e8c5…5c5`). PDF page 2 says: "In December 2025, local generation accounted for 51.6 percent (213 957 MWh) of the total electricity supplied to the domestic economy, while imports contributed 48.4 percent (201 024 MWh)". **Text:** CL-6137-2.4.10-R1 (revision 3) and BL-6137-2.4.10-01 match. | confirmed |

## Notes, not blocking

- **Local share swings by season.** NSA's chart on page 2 suggests local generation varied through 2025, from roughly 37 % to 71 % in each month, highest in the early-year months when Ruacana's flow is high. If a later edit wants to teach this run-of-river seasonality, it should first read the chart values from the rendered page rather than the extracted text.
- **East–west scale on the maps.** I computed the maximum east–west error inside Namibia at about 5.3 %; Codex gives about 5.7 % at the southern edge. Either way, the printed "within 5%" is slightly understated. Codex accepted this as a documented limit. Fixing it means re-rendering both accepted maps, so it is left as it is. Do not set distance-measurement tasks on these maps.
- **Checklists.** Two lines in Claude's own checklists still described the pre-repair state. They now say "dirty" and use the corrected wording on what distance measures, and their hash tables were refreshed. Checklists are not part of any acceptance hash.

## Remaining

1. Codex renews the acceptance of VIS-6137-2.3-01 and VIS-6137-2.3-02.
2. Claude runs `authoring/publish_guarded_6137.py` read-only and writes the whole-subject acceptance against the final `snapshot()` and manifest hash.

The read-only preflight currently reports 3 blockers: those two resources and the subject acceptance.

Nothing was published, committed, pushed, uploaded or imported.
