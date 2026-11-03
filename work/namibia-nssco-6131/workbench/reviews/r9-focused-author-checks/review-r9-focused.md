**Focused R9 verdict: changes are still required, but only one Medium item blocks.**

That item is a regression from the M3 unit fix: in the variation setting, the algebraic variable *m* is now formatted as the unit metres. Of L01–L22, 17 are fixed, 3 are only partly fixed (all Low), and the 2 retained items have reasons I accept. M1, M2 and M4 show no regressions. Apart from the *m* problem, M3 has only Low leftovers. No answer I recomputed was wrong. This is not a whole-bank or whole-syllabus approval.

I ran nothing and edited nothing. I used only Read, Glob and Grep, with no database, Bash, provider tools or sub-agents, and created no plan file.

## Medium regression

**R9-M1. The variable *m* is shown as metres** (`contextual-direct-inverse-variation`, all 10 cards, 20 blocks)
- **Where:** part a's reference answer and its step 2 result. Seed 0 shows `C=32\,\mathrm{m}` at `wb6131__contextual-direct-inverse-variation.json:38` and `:90`; seeds 1–9 do the same at `:363/:415` … `:2963/:3015`. Learners would read "C = 32 m" as 32 metres.
- **Cause:** `content_format.py:71`. The new `_UNITS` set (`:12`) includes `m`, `s`, `h`, `g` and `l`. Any of those letters straight after a digit inside maths becomes `\mathrm{}`, even with no space. So "32m", "3h" and "2s" in algebra all turn into units.
- **Why tests miss it:** the tests (`test_math_workbench_r8_medium.py:50-61`) only check spaced units and `y=mx+c`.
- **Suggested fix:** treat a single-letter unit as a unit only when a space separates it from the number, or when `/` follows it. Add tests for `C=32m` and `t=5h`.
- **Extent:** in this packet it appears only in this setting. I couldn't measure it bank-wide, because Grep returns no matches inside `workbench-bank.json`.

## L01–L22 resolution ledger

| ID | Status | Evidence |
|---|---|---|
| L01 | **Fixed** | `10main:03/d04` now links only to part c of `three-by-three-matrix-arithmetic` (`workbench-demand-evidence.json:5181`). RC = (−4)(6)+(3)(2) = −18, order 1×1 ✓. This matches the p.24 example (1 2)(4 5)ᵀ = (14). |
| L02 | **Fixed (presence only)** | d04 links to `legacy:nssco_expressions_formulae:4` part a (`:997`). Only 3 of its 10 slots (4004, 4006, 4007) actually find an unknown, e.g. F ∝ 1/d³ gives F = ½ ✓. The other 7 only form the equation, which repeats d01/d02 (Low). |
| L03 | **Fixed** | Stems now say "A bag with mass … kg". No "A 8" left. |
| L04 | **Fixed** | New worker counts are 2, 3, 4, 6, 10 and 14; the packet has 8 distinct old→new pairs. All 10 times recomputed ✓. |
| L05 | **Fixed** | Tariffs are 0.40 (3 cards), 0.60 (3), 0.80 (2) and 1.20 (2). All 20 charges and balances recomputed ✓. |
| L06 | **Fixed** | Five shops cycle. All 20 line totals, totals and change amounts recomputed ✓. |
| L07 | **Fixed (counts and rounding)** | Count endings vary, and all 10 one-significant-figure estimates are correct (half-up, e.g. 45→50, 65→70). The packet shows only 4 masses (1.2 kg ×5), not the claimed 6; I can't check the fresh samples. |
| L08 | **Retained; reason accepted** | The wording is identical, but the givens vary: 6 angles, 3 rotations and 4 radii (36, 40, 45, 48). Uniform construction wording is normal exam style. The syllabus asks learners to construct and use loci, not for varied wording. |
| L09 | **Fixed** | `graphs.py:143-144` and `:188`: odd seeds use −3≤x≤1 and require all roots to be negative. The base stays a positive integer (2–5). Seeds 1 and 5 give 5^x=0.5 → −0.43 and 2^x=0.75 → −0.42 ✓. All 8 even seeds use −3≤x≤3 and give positive roots ✓. The stem, the table x-values and the answer's domain wording agree. See Low items 4–5. |
| L10 | **Retained; reason accepted** | Printed p.12 says "interpret and perform calculations involving simple bills and payment receipts (e.g. …)" and nowhere mentions VAT. Tax appears only in the separate income-tax-table objective. Tariff × usage, balances and change are suitable for simple bills. |
| L11 | **Fixed** | All 40 parts recomputed ✓. Each card's four unit shares differ (e.g. seed 0: 19, 22, 26, 30). |
| L12 | **Fixed** | No `\frac{n}{1}` anywhere in the packet. |
| L13 | **Partly fixed** | See Low item 1. |
| L14 | **Fixed** | No "+ (-n)" left in prompts. The bracketed substitution forms that remain, such as (−1)(−1), are acceptable. |
| L15 | **Fixed** | Every prompt now gives the centre as coordinates. All 30 images in `transformations_coordinates__4` recomputed ✓, including the k=−2 cases. `combined-transformations` defines E=(0,−5) in the stem (`:3293`). |
| L16 | **Fixed** | Prompts, answers and diagrams use A′/A″. Checked on the full-size combined-transformations PNG. |
| L17 | **Partly fixed** | See Low item 3. |
| L18 | **Fixed** | Uppercase L and M appear in `general-intersecting-line-loci`, `visual_loci__2` and `locus-current.png`. |
| L19 | **Fixed** | The speed–time graph now has only "Speed (m/s)" and "Time (seconds)". |
| L20 | **Partly fixed** | See Low item 2. |
| L21 | **Fixed** | `locus-current.png` has no leader lines, and A and B sit clear of both parallel lines. |
| L22 | **Fixed** | "Kudu General Store" is used in all 10 cards. |

## Remaining Low defects

1. **L13 leftovers.**
   - `teaching_context` in `legacy__nssco_visual_quadratics__2` still has the old notation in 8 of 10 cards: `-(x)²+(9)` (`:519`), `(x-(2))²+(-4)` (`:819`), `2(x)²+(-18)` (`:2019`), `2(x+1)²+(-8)` (`:219`), plus `:1419`, `:1719`, `:2319` and `:2919`.
   - Cause: in `prose_formatting.py:44-51` the lookaheads leave out ".", so a sentence-final `+(9).` is skipped. Non-zero shifts like `x-(2)` and the bare `(x)` aren't handled at all.
   - No learner-facing code in this packet reads `teaching_context`.
   - Learners do see these worked-step forms: `(x-(3))(x-(5))=0` (`legacy__nssco_quadratic_graphs__2.json:242`) and `(3)(-5)-1y=-16` (`linear_simultaneous_equations__4.json:1004`). The coefficient-one rules at `:54` and `:69` don't include "=" in their lookahead.
2. **L20 partly fixed.** In `graphical-linear-solution-solution.png`, the origin "0" has moved, but the x-tick "−0.5" now runs into the y-tick "−1" and reads as "−0.5−1".
3. **L17 partly fixed.**
   - The step result "x ≈ −0.5" or "x ≈ 2.5" is stored as plain text in all 10 `graphical-linear-solution` cards (e.g. `:2452`). The cause is that `≈` is missing from `_MATH` (`content_format.py:8`).
   - The reference answer is split into a maths block "x ≈ -0.5", text "(", text "allow" and a maths block "±0.2)", so the closing bracket is unbalanced (`:2498-2512`).
   - "scale factor -1" uses a hyphen-minus inside text blocks (`combined-transformations.json:6780`, `:6828`).
4. **Exponential target line overruns the domain.** On the −3≤x≤1 branch the dashed target line is still drawn to x=3, because `pt(3,target)` is hard-coded (`graphs.py:210`). It's visible in `negative-exponential.png`.
5. **Negative-reading branch has little variety.** From the candidate rules (`:182-190`), the odd branch can produce only 5 distinct cards: base 2 → 0.75; base 3 → 0.25 or 0.5; base 4 → 0.5; base 5 → 0.5. That explains why seeds 3, 7, 9, 11 and 13 are missing from the sample.
6. **`check-calculator-answer` problems** (same setting as L07):
   - Every stem brackets a positive number, as in "$(59.8)\times51.3$".
   - Estimates show false precision, e.g. "3000.0".
   - The second factor 51.3, the ".8" ending and the reasonableness answer are the same in all 10 cards.
   - Two cards are duplicates: 40.8×51.3 appears at `:2305` and `:2633`.
   - All 9 distinct products are correct.
7. **Diagram nits.**
   - In `sum-solution.png` the curve crosses the "y" axis label.
   - In `visual_loci__2` the locus lines strike through the tick labels "2" and "−2".
   - `wb6131__locus-constructions-solution.png` still shows A and B sitting on the locus line. It's an older capture superseded by `locus-current.png`; regenerate it to avoid confusion.
8. **Nit:** ratios 6:4 and 4:6 are left unsimplified (seeds 4 and 7).

**One observation outside L01, not a defect here:** the p.24 example also includes a row × 2×2 product, (1 2)(2 3; −4 0). The d01–d05 split doesn't list that as a demand.

## M1–M4 regression check
- **M1, no regression:** all graph targets are integers or 1–2 decimal places. I recomputed 40 answers (10 each for power-3, power-−1, power-0 and exponential), all correct. Power-1 never uses coefficient 1.
- **M2, no regression:** tables carry 2 marks (1 for power-0), graphs 3 and the solve part 2.
- **M3:** the regression is R9-M1 above. The unit, colon and prose-word handling is otherwise working.
- **M4, no regression:** the power-0 graph has an open circle and a separate target line. In the coincident case the target line is suppressed and a note is shown.

## Scope and limits
- **Example files:** I opened 21 of the 40 `INDEX.json` files, 13 of them in depth.
- **Recomputation:** about 230 values by hand, none wrong.
- **Images:** 12 full-size PNGs. No contact sheets.
- **Syllabus PDF:** pages 11, 12 and 24.
- **Code read in full:** `content_format.py` and `prose_formatting.py`. Read in part: `graphs.py:110-237`, `registry.py:95-154`, the `legacy.py` teaching lines and `test_math_workbench_r8_medium.py:40-69`.
- **Coverage JSON:** only the `1j:07` and `10main:03` blocks.
- **Not reviewed:**
  - the logs, `SNAPSHOT.json`, `STATUS.json` and hashes;
  - test execution and KaTeX rendering;
  - how far R9-M1 reaches across the whole bank;
  - the other 19 INDEX settings and most of their worked steps;
  - the author's fresh-sample claims (11 workforce ratios, 6 sack masses);
  - the other 439 demands and the wider syllabus.
