# Focused check report: 8227 repair round 4

Reviewer: Claude Opus 5.5 (cross-vendor, role REVIEWER). Date: 2026-11-17. Inputs are frozen in `inputs.json` (snapshot `f3b68249…dccde1`, R3 parent `208a33a2…389d`, HEAD `11cd03fe`, with rounds 2–4 uncommitted). Findings are in `findings.md`.

## 1. Verdict: marking register accepted subject to a short row correction; provenance returned for a narrow repair; textbook work continues

**Accepted:**
- **R3-01, the award-table coverage.** All 119 questions are transcribed, and five independent blind second reads agree with the author's row structure.
- **R3-02, the named row corrections.** All 20 are confirmed on the renders.
- **R3-03, the convention register.** All rules are verbatim, the general rules are registered once across years, the specific rules have been added, and the conflicts are completed.
- **R3-05, the textbook caution corrections.**
- **R3-06, relocation.** A fresh copy rebuilds byte-identically with no edits.

**Accepted subject to correction (R4-01, R4-02):**
- **Error rate.** The new transcription has 8 marking-changing rows out of 821 (about 1%), against 6.6% in round 3. Two of these rows claim a source misprint that the print does not contain.
- **Schema fixes.** 42 E marks are stored as A with no establishment flag, 60 rows list a self-alternative, and the question records still say "no complete award schedule verified".
- **Fix size.** These are mechanical, named fixes, not another transcription round. My next check will re-read only the corrected rows and run a schema check.

**Returned to the author (R4-03, provenance):**
- All 26 recorded pairs are genuine, with correct parts, labels and tariffs. But five adaptations are still missing:
  - 2023 P2 Q8;
  - 2023 P2 Q1;
  - 2025 P2 Q3;
  - 2023 P2 Q3(a) (part-level);
  - 2023 P2 Q5(a) (part-level).
- Several "changed" fields contain a false clause or omit a change that alters the mathematics.
- 450 of the 476 ranked leads were "disposed" with a sentence saying they had not been read.
- An unregistered NSSCAS diagram defect was found in 2024 P2 Q7, where P is drawn on the wrong side of the y-axis.

**Not yet ready for review (textbook, R3-08):**
- All named corrections are in place.
- The population, qualifier decisions, answer accuracy and the fresh independent sample remain open, as the author says.
- About 450 items still carry block-level notes.

**Step 3 (recipe contract and pilot PLAN)** remains blocked on one owner decision, not on the marking work. The round-3 condition was "textbook population and answer work completed or explicitly scoped by the owner". Vitalis has not yet scoped it (see §4).

## 2. What the author got right

- **The hardest repair was done properly.** Every one of the 87 report pages was read visually, and all 119 award tables were transcribed into 821 rows with exclusive paths, SC caps and qualifiers. Every part tariff reconciles. In 2021 the blind read and the author's read agree row for row (0 marking differences in 156 rows). 2024 has no misreads at all.
- **Source gaps are handled honestly.** The two parts with no printed breakdown and the missing 2025 third-angle row are labelled as derived completions and excluded from pilot criteria. They are not dressed up as official.
- **The convention register is now a real register.** It has one record per general rule with all evidence pages, quotations verified verbatim, a complete context scan, and conflicts that preserve rather than resolve disagreements.
- **Every named textbook correction from round 3 was applied item by item**, and the author found further errors of its own, such as YM C4 Try Now 42 and C8 Example 12.
- **The relocation fix is real, and the new negative fixtures fail for the right reasons.**

## 3. Remaining work, in sequence

### Round 5 (author): finish the step-2 records

The commission is in `REPAIR-PROMPT.md`.

1. **R4-01:** correct the 8 rows and remove the 2 invented source-defect notes.
2. **R4-02:** the schema fixes (E flag, self-alternatives, stale `marking_rule_status`, empty earns field, c.a.o. on the derived row). Also register the unflagged report defects and the 2024 P2 Q4(a) third B mark.
3. **R4-03:**
   - add the five missing adaptations;
   - correct the "changed" fields;
   - register the 2024 P2 Q7 diagram defect;
   - fold 004 into 003;
   - re-record 030;
   - replace the boilerplate lead dispositions with a documented corpus-wide screen.
4. **R4-05:** reword rule 076.
5. **Textbook:** continue the completion work as the author has planned.

Then a **short focused check** by Claude: the corrected rows, a schema check, and the provenance additions.

### Step 3: recipe contract and pilot PLAN

This step is unchanged from the round-3 report §3. Rubrics are built from the official award rows. Derived completions and the 2024 P2 Q4(a) third B mark are authored and reviewed, never treated as official. The diagram spec names must-read givens (R3-07) and regenerates every diagram from instance values (this guards against the 2024 P2 Q7 defect).

## 4. Owner decision needed (Vitalis)

> **Decided 2026-11-17: no.** Step 3 waits until the textbook work is complete and accepted, so the textbook findings are available for planning. See `owner-decisions-2026-11-17.md`. The recommendation below is kept as the record of what was asked.

**Should step 3 start once the round-5 marking and provenance fixes pass my short check, with the textbook completion continuing in parallel?**

- **My recommendation: yes.** The recipe contract depends on the examination and marking evidence, which is now essentially complete. Textbook items are variety and support evidence, and none is learner-displayable. Under the parallel option they would enter recipes only after their own acceptance: the fresh independent sample, answer accuracy and qualifier decisions.
- **Risk of waiting:** step 3 waits on the largest and slowest task, about 1,900 items with full answer checks.
- **Risk of starting:** a recipe drawing on a textbook item before that item is accepted. The PLAN can prohibit this explicitly.

## 5. Limits

- **Delegated sub-checks.** The award second read (five agents) and the pair-level provenance check (one agent) were done by read-only Claude agents on renders I made. I re-read every high-confidence marking difference myself:
  - 2025 P1 Q7(c);
  - 2025 P2 Q2 SC2;
  - 2022 P1 Q2(b);
  - 2022 P2 Q1(b);
  - 2022 P2 Q6(b)(i).

  I also confirmed the five missing adaptations (three on renders, two from the paper text) and the 2024 P2 Q7 diagram defect (render and computation). The medium-confidence layout readings rest on the agents' crops, which are kept in the scratchpad.
- **Provenance.** My corpus screen covers the 355 local 9709 question papers (2015–2025). A miss outside that corpus, or one with no shared rare wording, would not be found.
- **Textbook.** I checked the named corrections and re-compared my round-3 blind sample. I did **not** classify the fresh 194-item sample. That should wait until the author declares the population complete, and it will use a reviewer-chosen seed.
- **Not run.** No app code, generator or runtime marking was run. This verdict applies to the hashed state in `inputs.json`.
