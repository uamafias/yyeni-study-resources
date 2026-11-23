# Independent check report: 8227 repair round 5

Reviewer: Claude Opus 5.5 (cross-vendor, role REVIEWER). Date: 2026-11-21. Inputs are frozen in `inputs.json` (snapshot `03cde4e4…022d`, HEAD `11cd03fe`). Findings are in `findings.md`.

## 1. Verdict: textbook population, records and answers accepted; the textbook-to-exam comparison returned for a focused repair

**Accepted:**
- **Part 1, marking and provenance:**
  - all 8 award rows are corrected;
  - the record-keeping fixes are complete;
  - the five requested Cambridge pairs are added, and one more was found by the author;
  - the 2024 P2 Q7 diagram defect is registered.

  One further part-level pair remains (R5-06, a small addition).
- **T1, the census.** A blind re-read of 45 random pages found nothing missing.
- **T2, item records.** These are accepted with a recorded limitation on the direct/component split (R5-03).
- **T3, value-level qualifiers.** There is no conflicting decision in 126 sampled items.
- **T4, answers.** The author had recorded 19 of the 21 key defects my blind recomputation found, and the two it missed are minor. It also caught 9 more that my check passed.
- **T6, the declaration.**
- **The rebuild.** A fresh copy built twice, byte-identically, matching the author checkout.

**Returned to the author: the comparison with the exams (R5-01, R5-02, R5-04).**
- The families never record a "same type" match. All 219 exam links are labelled "structural branch", even where a member matches an exam part in everything but its values.
- 94 of the 161 "textbook-only" families cover demands that an exam part assesses directly.
- Six insight sections, among them bounded trig equations and identity proofs, wrongly state that no exam part exists.
- Figure records still say "comparison pending".

This is the part Vitalis held step 3 back for. As recorded, it would misinform the planner, so it should be repaired before step 3 starts.

**Step 3 remains blocked** under the owner decision of 2026-11-17: the textbooks must be complete and accepted. Acceptance now depends on one focused round.

## 2. What the author got right

- **The population is complete and honest.**
  - 891 pages are enumerated, with exclusions stated on the page rather than assumed.
  - My blind census sample found no missing questions, examples, activities or continuations.
- **The answer work is excellent.**
  - Every one of 5,752 responses has its own status.
  - The author's recorded defects were more thorough than my own blind recomputation: it caught second-derivative slips, lost branches and precision labels that my check passed.
- **The author was careful about what the evidence shows.** Textbook originals stay internal, source defects are preserved, and no exam frequency is claimed from textbook evidence.
- **The full Cambridge screen found a pair I had missed** (036), and the rebuild is genuinely reproducible.

## 3. Remaining work, in sequence

### Round 6 (author): repair the exam comparison

The commission is in `REPAIR-PROMPT.md`:
1. **Member-level exam relations** (R5-01). Compute candidates from demand overlap, read each one, and record "same type", "structural branch" with the differing decision, or "no counterpart" with the demands searched. Then rebuild the family relations and the "Examination comparison" sections of the insights from those records.
2. **Family membership and demand claims** (R5-02).
3. **Figure records** (R5-04): graphic versus text callout, retire the stale statuses, register the listed errors, and mark unchecked content as not design evidence.
4. **Small fixes** (R5-05, R5-06): spaced notes, page-break answer pages, two slips, and the 2023 P2 Q4(b) Cambridge pair.

Then a **short focused check** by Claude:
- the 20 sampled families plus 20 freshly drawn ones;
- all eight "no exam parts" sections;
- an automated cross-check of family demands against exam parts;
- the new pair and the figure status counts.

### Step 3: recipe contract and pilot PLAN

Step 3 starts after that check passes. Carry forward:
- R5-03: use union links, count support as a lower bound, and resolve the overlapping registry demands in the recipe contract;
- R2-02: same-type references per branch, which the member-level relations from round 6 now supply;
- R3-07: must-read givens in the diagram spec.

## 4. No owner decision is needed now

Vitalis's 2026-11-17 decision covers this round: step 3 waits. The only open choice is scope. I recommend **not** auditing the content of all 1,758 figures. Figures are cited as evidence only five times, so marking unchecked figures as "not design evidence until checked" is enough.

## 5. Limits

- **Delegated work.** Eight agents did delegated work. Five classification agents, two answer agents and one census agent worked blind on renders I chose. One families agent worked non-blind, by design. I verified myself:
  - the families agent's strongest claims (the 2021 P2 Q2/Q9 texts, the 2025 P2 Q12(a) text, the six "none claimed" sections against `question-analysis.json`, and the 94-family count);
  - both answer-page misses (on renders);
  - one disputed answer value (by hand);
  - the new provenance pair (renders of both papers).

  The other agent judgements, such as individual family member fit, rest on their crops and notes, kept in my scratchpad.
- **Classification comparison.** The comparison measures agreement, not truth. Where the reviewer adds a demand, the reviewer may be the one over-mapping.
- **Provenance.** The screen covers the 214 local P1–P3 9709 question papers. A source outside that set, or one with no shared rare wording, would not be found.
- **Not run.** No app code, generator or runtime marking was run. This verdict applies to the hashed state in `inputs.json`.
