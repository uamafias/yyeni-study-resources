# Whole-subject acceptance: NSSCO Geography 6137 (Claude)

Reviewer: Claude, 30 October 2026. Owner: Vitalis P Haupindi. Playbook step 6: the cross-vendor semantic sign-off. The acceptance record is `review/subject-acceptance-6137.json`.

**Verdict: publish.** This acceptance authorises nothing by itself. Publication, commit, push, upload and classroom import remain separate steps for Vitalis to approve.

## What this acceptance rests on

1. **Whole-subject cross-review** (`review/crossreview-report-6137.md`). All 18 topics and 801 items were reviewed against the syllabus, the 2026 Paper 3 circular and the examiner evidence. That produced 106 findings, which were repaired within the approved slots.
2. **Codex's verification of that review** (`review/codex-crossreview-verification-6137.md`).
3. **Claude's cross-check of Codex's repairs** (`review/claude-crosscheck-codex-repairs-6137.yaml`): 11 corrections, XC-F01 to F11.
4. **Map revision 01, approved by Vitalis:**
   - two original maps from open data: VIS-6137-2.2-02 (NSA regions plus Atlas of Namibia farming data) and VIS-6137-2.6-02 (Atlas Gazette-derived parks and conservancies, plus the CCF farm point);
   - the 2.3-P04 bi-polar grid and 2.3-P05 hot-spot footpath packages rebuilt (`review/HANDOVER-codex-review-final-resources-6137.md`).
5. **Codex's final-resource review** (`review/codex-final-resource-review-6137.md`): both maps accepted, VIS-6137-3.3-02 re-accepted, and four repairs made.
6. **Claude's check of those four repairs** (`review/claude-check-final-codex-repairs-6137.md`): all four confirmed against the Atlas energy chapter and NSA's *Electricity December 2025* report, page 2.
7. **Codex's renewal of the two tourism acceptances** (`review/codex-final-tourism-renewal-6137.md`). All 56 visual resources now carry current independent acceptances.

## Final checks (run by Claude on the final state, 30 October 2026)

- **Topic checks:** all 18 topics give 40 PASS, C-18 WARN and C-35/C-41/C-43 NOT_RUN; decision publish; no failures.
- **Slots:** 801/801 planned slots each have exactly one item, with labels unchanged; 1,153 claims.
- **Copied wording:** 0 runs of 8 or more words against the 35 assessment extracts.
- **Map revision:** `planning/verify_map_revision_6137.py` passes.
- **Read-only preflight** (`authoring/publish_guarded_6137.py`): before this acceptance, the only blocker was the missing whole-subject acceptance.
- **Manifest SHA-256:** `2ded69cc96873c369ba2cee00c959beef46a576b420d48bc92b99b3d2d6e93c4`, matching Codex's renewal receipt.

## Known limits, accepted and documented

- **All 1,153 claims stay `unverified` and `publishable=false`, as check C-24 requires.** The independent verification is recorded in the review receipts, not in those flags.
- **Map dates and scale:** the farming map uses 2006 farming systems, an undated cleared-land layer, and irrigation locations shown as locations only. Both maps' east–west scale note ("within 5%") is slightly understated: the true maximum is about 5.3–5.7 %. Do not set distance-measurement questions on these maps.
- **Conservancy count:** the conservancy layer has 89 records and 87 names (2020). It is not a national count.
- **Electricity figures:** these are dated: Ruacana 26 % of electricity used (2018/19), and local generation 51.6 % in December 2025.
- **Plan problem recorded for the planner:** the abbreviated practical objectives (OBJ-6137-2.3.91 to 93 and 3.1.91) were repaired within existing slots, not in the work orders.

Any change to topic content, planning files or the manifest after this record makes the acceptance stale. The guard will then refuse to publish.
