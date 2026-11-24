# D4.1 diff-only check report: 8227 Workbench pilot PLAN

**Reviewer:** Claude Opus 5.5 (cross-vendor REVIEWER). **Date:** 2026-11-24.

This is the diff-only check of Codex's D4.1 text errata.
- **Inputs:** `inputs.json` (manifest `4a0548320dcb9209dcd28e18bd4f6c77423480de6538fcbf1b0f8b6d0e17d8ec`, content digest `e9cd8f58345364e7b3bb45fadf2bab162571cc4c101df5beff2189a514fd8780`, Git HEAD `fa0a09d4`).
- **Findings:** `findings.md`.
- **Agent evidence:** `check-diffscope.json`.
- **Rebuild:** `rebuild.json`.

## Verdict: D4.1 confirmed. The stage-D plan is ready for Vitalis's approval

- **Both should-fix items are repaired.**
  - **Authority.** No live line now credits Vitalis with the per-datum misread mechanics.
  - **The misread rule.** It defines "on that datum", judges eligibility for the connected question, and no longer overrides MR09 or OD-1. The text is identical in all 9 work orders and all 81 policy copies.
- **No score, mark, domain, answer, count or version changed.**
  - Every scoring fixture is byte-identical to D4.
  - Only text leaves changed in the generated JSON.
  - All 46 authored hunks trace to the errata brief.
- **The rebuild is now portable.** Two relocated copies rebuild and pass the freeze check, and all 14,763 files are byte-identical to the author checkout without normalisation.
- **Five minor notes** carry into stage E with no repair round (`findings.md`).

## What Vitalis approves

The exact manifest `4a054832…`, with:
- its counts: 9 recipes / 14 choices / 42 cases / 27 parts / 83 branch marks; Bloom 13 Apply / 1 Analyse; decks 19/20/17;
- its gaps and flagged capabilities (APP8227-01–08);
- its exemplars;
- the active proposed adaptations and operations, including MR03-OPS-D4.

The OD-1 to OD-6 principles already bind.

**One optional ruling.** The implicit C 4→5 misread scores 9/9 on the product route (`findings.md`, "Still open"). Without a ruling, it stays an E/F fixture.

## Then

Stage E (author and generate) begins after that approval. The three recipe groups (calculus, trig/log, visual) are independent and can be built in parallel.
- Only design-blocking or should-fix findings should start a repair round.
- Notes carry into the next stage's work.
- No commit, push, import, assignment or publication has been made.
