# D4.1 diff-only check findings: 8227 Workbench pilot PLAN

**Reviewer:** Claude Opus 5.5 (cross-vendor REVIEWER). **Date:** 2026-11-24.
**Inputs:** `inputs.json` (manifest `4a054832…`, content digest `e9cd8f58…`, Git HEAD `fa0a09d4`).
**Baseline:** D4 manifest `71ee10b6…`. Our D4 findings and the errata brief are in `review/opus-5-5-d4-confirm/`.

## Method (run in parallel)

- **Lead, in the foreground:**
  - froze the inputs and re-verified every manifest pin: 7,008 files, 436 sources, 95 reviews, 0 mismatches;
  - verified the D4 archive (3,497 files, 0 mismatches) and the D0–D4 recoveries;
  - computed the D4 → D4.1 delta myself: 42 changed files, 0 removed; additions are only the D4 archive and the D4.1 bookkeeping files;
  - read the two should-fix lines and counted the three clauses in MR03 and the nine work orders;
  - ran Codex's no-score guard inside a copy.
- **Background:** `planning/d4/rebuild-design.py`, then `freeze-plan.py --check`, in two relocated copies (`rebuild.json`).
- **One independent agent** classified every changed hunk and every changed JSON leaf against `ERRATA-D4-1-PROMPT.md`, using its own diffs and comparator (`check-diffscope.json`).

## Results

| Item | Verdict | Evidence |
|---|---|---|
| **D4-S01: authority residues** | **repaired** | Vector `WO:73` and implicit exemplar `:125` now read "follows MR03: the OD-6 MR−1 principle with A/B follow-through, under the proposed MR03-OPS-D4 per-datum mechanics". A grep of all live lines where OD-6 appears with per-datum, first-use, ledger or unit finds the principle and the proposal clearly separated in every one. |
| **D4-S02: MR03 clauses** | **repaired** | Each of the three exact clauses appears: <br>• once in MR03 (`subject-rules.md:67`); <br>• in the shared `operational_rules` and `work_order_line`; <br>• in all 9 work orders; <br>• in all 27 policies (14 calculus, 6 trig, 7 visual) and the 27 pilot-design and 27 part-register copies. <br>All 81 JSON copies are identical to the shared text, and the apostrophe is U+0027 throughout. The authority split ("proposed … pending Vitalis approval") is intact, and MR09 and MR01 are no longer contradicted. |
| **D4-N01: portability** | **repaired** | `render_path` is now repo-relative. Both relocated copies rebuild and pass the freeze check. All 14,763 files are byte-identical across the author checkout and both copies, with no normalisation; there are 28 derived outputs and 25 + 2 seeded negatives reject. |
| **Listed notes** | **applied** | Each is in place: <br>• the PLAN:11 historical sentence is restored; <br>• "16 November owner decision 6 (visual demands)" is at `capability-gaps.md:34` and `recipe-contract.md:162`; <br>• the stale labels are updated; <br>• the T 3→5 reasoning for its unchanged 2/6 is at motion `WO:75`; <br>• the exposure version is provenance only, and `:25` names 0.1.1–0.1.3; <br>• the "visible" 156/168 qualifier is added, with (d/a, T) 162/168 disclosed; <br>• the polynomial, exponential and gradient-only policies have branch-specific eligibility notes; <br>• the C 4→5 9/9 fixture is limited to the product route, with the other routes left as E/F fixtures; <br>• 2023 P2 Q6 AWARD05 is cited, with a proposed B2 www clause at trapezium `WO:95`; <br>• the generic visual tails and the strict-unseen 3 → 2 correction are disclosed. |
| **No score or mathematical change** | **confirmed** | **Agent:** across the 16 generated JSON files, only string leaves changed (87 leaf groups). There are 0 number, boolean, list-length or key-set changes, and each group traces to an errata item or to a provenance hash or status label. <br>**Lead:** every scoring fixture and oracle file is byte-identical to D4 (25 of 33 `planning/d4` JSON files unchanged, among them every misread, marking, exemplar, capacity, separation and key-delta file). Codex's guard passes in a copy: 42 examples, 70 ledgers, 5 seeds rejected. The only new number in text is the 162/168 disclosure statistic. |
| **Scope** | **clean** | All 46 authored hunks are in scope; 0 are out of scope or questionable. No line claims that Claude confirmed D4.1. Analysis, tools and curriculum are unchanged, and the R7 freeze passes. Earlier review folders are unchanged. |

## Notes (carry into stage E; no repair round)

- **d41-01.** The gradient-only eligibility note says "finite gradient", while implicit `WO:142` says "finite and nonzero". No case changes.
- **d41-02.** The exponential eligibility note adds an explicit nonunit-chain-factor guard (k read as 1 is ineligible). This is a correct application of OD-6's "changes difficulty" test. Like all eligibility details it falls under the proposed MR03-OPS-D4, but the note does not say so itself. No fixture is affected.
- **d41-03.** Motion `WO:35` also dropped "output-affecting revisions" from the exposure-key sentence. The remaining wording covers it.
- **d41-04.** These still name "Claude's D4 changed-scope confirmation" as the next gate: `PLAN.md:3,11,122`, `subject-rules.md:145`, `recipe-contract.md:173` and the work-order headers. Update the gate wording when stage E starts.
- **d41-05.** In MR03, the MR09 limit comes four sentences after the "overrides not-F.T." sentence it limits. The meaning is clear; adjacency would read better.

## Still open for Vitalis (unchanged from D4)

- **The C 4→5 product-route fixture still scores 9/9.** On that route, an ineligible misread (the point moves off the curve) never enters a marked step. It follows OD-6's "marked as normal" wording, while the NSSCAS report's "do not score maximum marks" leans the other way. It stays an E/F fixture unless Vitalis rules otherwise.
- **The E/F carries** from `review/opus-5-5-d4-confirm/report.md` §4.

## Not checked

- No app, generator, marker, renderer, local website or MCP operation was run.
- This was a diff-only check. Unchanged D4 material was confirmed in the D4 review and was not re-reviewed.
