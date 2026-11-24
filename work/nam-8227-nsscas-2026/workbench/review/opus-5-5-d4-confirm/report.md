# D4 confirmation report: 8227 Workbench pilot PLAN

**Reviewer:** Claude Opus 5.5 (cross-vendor REVIEWER). **Date:** 2026-11-24.

This is the changed-scope confirmation of Codex's D4 repair.
- **Inputs:** frozen in `inputs.json` (plan manifest `71ee10b6…`, content digest `d3f5676a…`, Git HEAD `fa0a09d4`).
- **Findings:** `findings.md`.
- **Agent evidence:** `check-*.json`.
- **Rebuild:** `rebuild.json`.

## 1. Verdict: the D4 repairs are confirmed. Approval should wait for a short text-only errata (D4.1)

**All four D3 groups are repaired, and no design blocker remains.**
- **The register no longer over-credits Vitalis.** Only the OD-6 principle is attributed to him. The detailed misread mechanics sit in a separate row, MR03-OPS-D4, labelled proposed and pending his approval.
- **The shared misread rule is consistent.** All 9 work orders and all 27 parts carry the same text, including "practice feedback names the misread".
- **Every re-marked case recomputes:**
  - vector 4/7, 6/7 and 3/7;
  - motion 2/5, 4/5 ×3, 5/6 ×2 and 2/6;
  - principal-inverse 2/3;
  - implicit 9/9, 5/9 and 4/5;
  - stationary 3/6 and 5/6.

  A misread no longer costs 0 marks or 2.
- **Motion.**
  - The coefficient-ratio shortcut is gone. The best lookup on visible coefficients is 156/168, and no visible feature or combination separates the outcomes perfectly.
  - The invalid "vertex bound" route is deleted.
  - All counts and the nine sweeps reproduce.
  - The changed example (v = −t²+t+12 on [0,3], distance 63/2) is correct.
- **Trapezium.** The factorised form keeps B1, as the official row gives it. Wrong log-law working loses B2.
- **Totals:**
  - 138 independent recomputations, 136 agree;
  - 52 marking tests, 49 as expected;
  - 20 capacity checks, all match.

  The five mismatches come from undefined wording, not wrong answers.
- **Rebuild.** The rebuild reproduces in two fresh copies, apart from one stored absolute file path. Analysis, tools and curriculum are unchanged.

**Why approval should wait for D4.1.** Vitalis approves exact text, and two small items in that text are still wrong.
- **D4-S01.** Two leftover sentences still say the per-number misread unit comes from OD-6: vector work order `:73` and implicit exemplar `:125`.
- **D4-S02.** The proposed misread rule has two wording faults:
  - its override clause now contradicts the answer-given-proof rule (MR09);
  - its core phrase "the first earned A/B on that datum" can be read part by part or criterion by criterion, and the readings give different scores. Under one, a misread can again cost nothing.

  One clarifying sentence fixes both, and it matches what every fixture already does, so no score changes.

**Two of these trace to our own D4 prompt wording** (findings §B). Our D3 check also missed the two authority residues.

**If Vitalis prefers to approve D4 as it stands,** the errata can instead be the first edit of stage E. None of them changes a mark, domain or answer.

## 2. Next steps

1. Vitalis gives Codex `ERRATA-D4-1-PROMPT.md` (this folder).
2. Claude runs a diff-only check of D4 → D4.1:
   - only the listed lines changed;
   - the MR03 text is identical everywhere;
   - no score moved;
   - the rebuild passes in two relocated copies.
3. Vitalis approves the exact manifest, counts, gaps, capabilities, exemplars and the proposed operations, including MR03-OPS-D4.

## 3. For Vitalis's attention (not a defect)

**In one rare implicit case, an ineligible misread scores full marks.** Misreading the constant C (5 for 4) moves the given point off the curve. Under OD-6 that misread is marked normally, and on one proof route the constant never enters a marked step, so the learner scores 9/9. A milder misread would lose a mark. This follows OD-6's wording; the NSSCAS report's "do not score maximum marks" leans the other way. It is carried as an E/F fixture unless Vitalis rules otherwise.

## 4. Carry into stage E/F

- **Fixtures:**
  - calc-D4-01: which route the C misread fixture uses;
  - calc-D4-02: datum identity;
  - shared-D4-01: two misreads competing for one mark;
  - visual-D4-06: the ambiguous "2 2 ln" notation;
  - motion-D4-02: fitted derived-ratio rules;
  - the D3 carries: calc-D3-04, trig-D3-02, visual-D3-05, the vector angle.
- **Binding rules:** OD-1 to OD-6. The operational misread rules bind only once Vitalis approves the exact manifest.

## 5. Limits

- **Who did the checking.** Five same-vendor agents did the re-testing; their evidence is in `check-*.json`.
- **What I verified myself:**
  - the manifest and pins;
  - the D3 recovery;
  - the write scope;
  - the two-copy rebuild;
  - every should-fix locator, in the current bytes, including the MR03/MR09 collision against the D3 archive text.
- **Single read.** Each recipe group was read by one agent; marking judgements at the margin carry that limit.
- **Not run.** No app, generator, marker, renderer or MCP operation was run.

This verdict applies to the hashed state in `inputs.json`.
