# Short check report: 8227 repair round 7

Reviewer: Claude Opus 5.5 (cross-vendor, role REVIEWER). Date: 2026-11-23. Inputs are frozen in `inputs.json` (snapshot `abfc3399…f567e8`). Findings are in `findings.md`.

## 1. Verdict: round 7 accepted; five small corrections close it out, then step 3 may start

**Accepted:**
- **The gap search.** 21 of the 22 exam parts formerly listed as having "no textbook practice" are now correctly resolved.
  - "Differentiate (3e²ˣ − 7)⁵" and "exact value of cosec(2π/3) + cot(2π/3)" have same-type textbook counterparts.
  - The two held exam originals really are defective.
  - The one remaining gap (2023 P2 Q2, recovering a, b, c from a modulus graph) is a real gap.
- **The 28 disputed pairs.** 26 now follow my reviewers' verdicts, and the 2 dissents are reasoned margin calls.
- **The mixed-branch conversion.** 15 of the 16 sampled converted pairs are real relations.
- **The named record fixes** (D.1–D.8): all are in place.
- **The per-objective map.** 73 syllabus skills now have same-type textbook practice (69 before), 64 have only variant or other practice, and 1 has none.

**Five small corrections (R7-01 to R7-05):**
- **R7-01.** The 12 "nonordered" pairs Codex kept rejected are all related: 4 same type and 8 branches.
  - Codex judged each one through a single worked example, not the family's best matching question.
  - Verified on the pages: YM Try Now 39 Q1(c), "how deep was the shaft after 4 s", is the same task as 2021 P1 Q4(b), "how far from O after 3 s".
- **R7-02.**
  - One gap relation does not hold: 2023 P2 Q4(c), a log equation, against Goldie 2B Q10(ii).
  - One gap record contradicts itself (2024 P1 Q9(c)).
- **R7-03.** Two of the 10 families left without an assessed skill contain exam-style practice that should be compared.
- **R7-04.** The 403 "part-specific" rejection reasons are templates. They paste the extracted exam text, sometimes garbled, in front of a reused sentence, and most lost the specific reason they had in round 6. The decisions themselves mostly hold, so the fix is honest labelling, not another rewrite.
- **R7-05.** A limits note: rejections under-call relations, so step 3 searches family members, not only the recorded relations.

## 2. Why accept rather than return

- **The defects are small.** They are named, and none changes what the planner would conclude about where the Workbench matters most:
  - every exam part involved in R7-01 already has other textbook relations;
  - the gap list changes by one part;
  - the two families add a handful of comparisons.
- **The defects are cheap to fix.** Each correction is bounded: 12 pairs, 3 records and 3 families.
- **A further full round would cost about a day.** It would buy little the step-3 review cannot check.

**What I recommend.** Codex makes the corrections as a close-out (`REPAIR-PROMPT.md` in this folder). Step 3 then starts, and I confirm the close-out at the start of my step-3 review.

**If you want the stricter route** under your 2026-11-17 decision, have me check the close-out separately before step 3 starts. That adds a short check, about an hour, not a full round.

## 3. Carry into step 3

- R5-03: union demand links.
- R6-03 and R7-05: same-type and branch counts are lower bounds; search family members.
- R2-02: per-branch same-type references.
- R3-07: must-read givens in the diagram spec.
- R6-05: family `distinction_basis` and `units_and_precision` are author descriptors, not design evidence.
- Rejection reasons are not evidence (R7-04).
- Notes are damaged text: read the page.

## 4. Limits

- **Delegated work.** Seven reviewer agents did the page reading:
  - two checked the gap parts;
  - four made blind pair judgements;
  - one checked the empty-demand families.

  I verified the following myself:
  - R7-01's mechanism, on the pages: the motion pair, and the reasons citing only Example 39;
  - the R7-04 statistics;
  - the self-contradiction in the 2024 P1 Q9(c) record;
  - the 28-pair comparison;
  - the named fixes and the map counts, in the records;
  - the rebuild.

  The other judgements rest on the agents' renders and notes, kept in `blind-sample-r7.json`, `gap-search-check-r7.json` and `empty-family-check-r7.json`.
- **Blind agreement is not truth.** Same type versus branch is a judgement call at the margin.
- **Small samples.** The batch-rejection sample is only 6 records, and the converted-branch sample is 16 of 186.
- **Not run.** No app code, generator or runtime marking was run. This verdict applies to the hashed state in `inputs.json`.
