# Focused check report: 8227 repair round 6

Reviewer: Claude Opus 5.5 (cross-vendor, role REVIEWER). Date: 2026-11-23. Inputs are frozen in `inputs.json` (snapshot `13dcf9f7…e818464`). Findings are in `findings.md`.

## 1. Verdict: most of round 6 accepted; the gap list and the rejection labels returned for a short round 7

**Accepted:**
- **The comparison is complete and positive matches are reliable.**
  - All 2,675 family–exam-part candidates are decided, and every claimed match was read on both pages.
  - In my blind sample, 28 of 30 claimed matches are real, and 23 of 25 claimed same-type matches are the same type.
- **The round-5 errors are fixed.** The named mislinks are corrected, and no insight section now wrongly says "no exam parts".
- **The per-objective problem map is structurally right.** All 138 demands are present, the counts recompute, and the sampled entries match the records.
- **Figure records, provenance and the rebuild.**
  - The stale statuses are gone and the nine printed errors are registered.
  - Pair 037 and the recall figure are recorded.
  - Two fresh rebuilds matched the author's files exactly.

**Returned:**
- **R6-01, the list of exam parts with "no textbook practice".** It contains false gaps. "Differentiate (3e²ˣ − 7)⁵" (2024 P2 Q4(a)) and "find the exact value of cosec(2π/3) + cot(2π/3)" (2023 P2 Q3(b)(ii)) both have plain textbook counterparts. That list is the planner's guide to where the Workbench matters most, so it must be right.
- **R6-02, rejections.** About 30% of sampled rejections are related pairs. The main cause is fixable:
  - 202 pairs were rejected only because they are neither simply easier nor harder. My prompt invited that reading.
  - Some rejections are over-strict. The verified case is a "differentiate, hence integrate" textbook question rejected against the same exam question because one inner function is exponential.
- **R6-04, 61 families never compared.** They were given no assessed demand, although 41 of their members practise examined skills.
- **Named record fixes (R6-05 to R6-07):**
  - members that don't fit their family;
  - one transcription error (tan²x recorded as tan²2x);
  - two answer pages;
  - two figure roles;
  - status strings.

**Step 3 stays blocked** until round 7 and my short check, under Vitalis's 2026-11-17 decision.

## 2. What the author got right

- **The scale of the work.** 2,675 decisions, 644 page readings, 500 families with prose, and a per-objective map of all 138 demands, all reproducible from a fresh copy.
- **No false positives.** When the author claims a textbook question matches an exam question, it almost always does.
- **The round-5 false "no exam parts" statements are gone.** The insight sections now list their exam parts, same-type matches and branches exactly as the records do.
- **The figure records are honest:** content is marked not checked, and the printed errors are registered with page evidence.

## 3. Round 7, then step 3

The round-7 commission is `REPAIR-PROMPT.md` in this folder:
1. **Re-check the 22 exam parts recorded as having no textbook practice** by searching the books directly, not only through demand IDs.
2. **Turn the 202 "nonordered" rejections into branches** with a "mixed" direction, where they read as branches.
3. **Re-decide the 28 pairs** where my blind agents disagreed, and the 8 rejections for 2023 P2 Q3(b)(ii).
4. **Compare or justify the 61 families with no assessed demand.**
5. **Fix the named records,** mark the notes as damaged text, and correct the report's notes claim.

Then my short check:
- all 22 gap parts;
- all 28 re-decisions;
- a sample of the converted pairs;
- the named fixes;
- a rebuild.

**Carry into step 3:**
- R5-03: union demand links.
- R6-03: same-type counts are lower bounds.
- R2-02: per-branch same-type references.
- R3-07: must-read givens in the diagram spec.
- R6-05: family `distinction_basis` and `units_and_precision` are author descriptors, not design evidence.

## 4. One scope recommendation (no decision needed unless Vitalis disagrees)

**What is not met.** Round 6 asked for family prose:
- a distinction from the nearest sibling (B.3);
- family-specific precision text (B.5).

Both are only partly met:
- 15 of 40 sampled distinctions fail;
- most precision text is assembled from shared template sentences.

**My recommendation.** Do **not** rewrite all 500 families. Step 3 decides recipe boundaries itself and reads the member pages when it does. Round 7 should fix only:
- the misfits and contradictions named in the findings;
- the doubled prefix;
- a limits note saying these two fields are not design evidence.

## 5. Limits

- **Delegated work.**
  - Ten agents did delegated work:
    - four judged pairs blind;
    - one classified figures blind;
    - five worked non-blind by design (figure media and errors, notes and answer pages, insights and map, and two on families).
  - I verified these myself on renders: PAIR-024; 2023 P2 Q3(b)(ii); the rejection texts, candidate counts and gap list behind R6-01 and R6-02; the 61 empty-demand families; the doubled prefix and template sentences; the rebuild.
  - The other agent judgements rest on their renders and notes, kept in my scratchpad.
- **Blind judgements are agreement, not truth.** Same type versus branch is a judgement call at the margin; several disputed rejections are medium or low confidence.
- **The rejection estimate is rough.** About 30% related is from 45 sampled rejections across two strata.
- **Not run.** No app code, generator or runtime marking was run. This verdict applies to the hashed state in `inputs.json`.
