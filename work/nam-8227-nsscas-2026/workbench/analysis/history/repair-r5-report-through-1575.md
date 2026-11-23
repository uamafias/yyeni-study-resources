# Repair round 5 working report — NSSCAS Mathematics 8227

18 November 2026. AUTHOR Codex; owner Vitalis. **Active checkpoint, not a completion handback.** Step 3 waits for both textbooks to be complete and independently accepted.

| Finding | Current change | Evidence and remaining acceptance |
|---|---|---|
| R4-01 | Eight marking-row fixes, with enlarged source readings. | `analysis/award-repairs-r5.json`, `checks/r5/award-*`, Part 1 validation. Independent review pending. |
| R4-02 | All 42 E flags, self-alternative removal, regenerated marking statuses, two row completions and seven report defect records. | `award-audit-reconciliation-r5.json`, `marking-conventions.json`, `source-defects.json`; targeted negative fixtures. |
| R4-03 | Five requested pairs plus screen discovery; corrected correspondence fields, duplicate folding, hidden wording-only lead and diagram warning. | `provenance-reading-r5.json`, `nsscas-cambridge-provenance.json`, full-screen reading records. No unsupported originality claim. |
| R4-04 | Both-book completion in progress. Author passes now include Goldie C1, C3, C4, C5, C6, retained C7 content and YM C4. | Item-level records, per-part derivations, page census and working insights. Remaining pages and all final T5/T6 work are open. |
| R4-05 | Rule 076 now covers differentiating, integrating and cubic-solving calculators while retaining explicit award exceptions. | `tools/convention_inputs.py`, regenerated convention register. |
| Binding owner decision | Step 3 remains on hold. Textbook originals remain internal. | `STATUS.md`, `HANDOVER.md`; no PLAN, recipes, runtime generators or imports. |

Part 1 retains 119 questions, 250 parts, 821 rows (818 official plus 3 derived), 42 E flags and 95 convention rules. Provenance has 31 confirmed pairs on 29 NSSCAS questions, 3 structural comparisons, 1 wording-only hypothesis and 1 folded duplicate. The full screen compared 119 questions with 3,208 local pages (381,752 comparisons), covering 202 unique QP documents at 214 paths; 158 threshold candidates were read on 136 pages. Below-threshold unread leads remain unread.

| Measure | R5 baseline | Current focused checkpoint |
|---|---:|---:|
| Catalogued source records | 1,933 | 2,388 |
| Fresh assessed/component mapping reviews | 0 | 962 |
| Explicit census pages | 0 | 230 of 891 |
| Pages still pending | 891 | 661 |
| Items with full stated-response author checks | 0 | 592 |
| Individual output checks | 0 | 1,575 |
| Matches / sketch / show-prove | — | 1,215 / 136 / 163 |
| Key wrong / no key / key incomplete | — | 32 / 12 / 17 |
| Manual / executable outputs | — | 193 / 1,382 |
| Source defect or caution entries | 0 in this register | 60 |

The source-record count includes figures and tables, and is not a count of distinct recipes. The 60 source entries include domain, question, visual, working and display cautions; they are not 57 wrong final answers. The historical 759-page render sweep and 1,913 answer locators do not prove an exhaustive census or answer accuracy.

The latest completed full pass is **1,575 outputs, 131 identical artifacts and 21 expected negative rejections** (session16705). Focused checks also pass. Final fresh-copy verification remains forT6.

Additional numerical evidence at this checkpoint covers 43 proper integrals, 28 real primitives and 34 trapezium calculations. Existing independent checks cover 98 function/viewports, 20 angles, 57 basic and 94 composite trig equations, 5 inverse compositions and 31 R-form cases. These remain author verification, not cross-vendor educational acceptance.

The integration work exposed a significant-figure quantizer defect for negative decimal-place counts (rounding to tens/thousands). The fix passes large, small, positive and negative fixtures; none of the preceding 1,248 outputs changed. Original-pole and singular-parametric fixtures now exercise the actual guard functions. Trig-pole ImageSets are resolved against exact finite intervals where a generic subset test cannot decide.

New source evidence includes a genuine four-versus-five-strip key error in Goldie 5C2(i), and a separate display-precision caution in 5C4. The latter has no six-decimal requirement; the explicit author approximation policy preserves exact values and awaits independent judgement. Correct final 0.64 is not reported as wrong. Source ellipses are compared as prefixes. Enlarged reads cleared the supposed compound-interest payment-count error (the key says one million) and the suspected 5C11 integral error (the lower bound is 6).

| Stage | Current limit |
|---|---|
| T1 | 230 pages explicitly censused; all others remain pending. C5 adds a missing three-graph prompt; C6 adds a missing decimal-search prompt and iteration activity. |
| T2 | 962 fresh item/figure mappings; the rest remain open. Direct demands and components stay separate. |
| T3 | Actual-value decisions recorded for the completed segments. Remaining source items and exclusions still need review. |
| T4 | 592 items / 1,575 outputs checked. C5andC6investigations have complete source-response records; excluded/enrichment scope remains explicit. All116states in15C6iteration traces are independently replayed. Remaining items and investigations are open. |
| T5 | Item-backed working notes expanded. Final cross-book families, all-demand synthesis, examination and grade-bound comparisons remain open. |
| T6 | Neither book declared complete. Final fresh-copy checks, final snapshot, author-complete declaration and reviewer-chosen blind check have not happened. |

All 19 baseline review-file hashes and the preserved R4 snapshot were rechecked unchanged. HEAD remains `11cd03fe639f9936dd9f83fd04bd6f04d5181676`. Nothing was committed or pushed. The frozen analysis snapshot remains R4 until the entire repair is ready. Historical checkpoint narratives are preserved under `analysis/history/`.

C6 adds36independent Ridder root comparisons and32supplied-sequence checks. Its15certified traces contain116states,independently replayed through CAS evaluation. Invalid original-pole and no-sign-change root brackets reject. The quintic impossibility claim is corrected by an exact quadratic/cubic factorisation;pre-existing principal even-root branch cautions are reverified;the final qualitative steepness wording remains an independent-judgement caution. The suspected6B16key-label error is cleared by a4xread.
