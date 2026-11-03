# R10 delta review: R9 residual repairs

## Verdict

**Every residual repair can be accepted except one diagram repair.** The parallel-locus tick-label fix in `visual_loci__2` introduced a new, reproducible defect. It's Low severity and doesn't block: no answer is wrong. But the brief requires tick labels to be "visibly separated", and in these diagrams they are not. Everything else in scope checks out:
- R9-M1 is fixed.
- L13, L17 and L20 are now fully fixed.
- The domain-overrun and variety repairs are correct.
- The calculator repair is correct.
- The sum label is correct.
- The diagrams are fresh captures.

No answer I recomputed was wrong. This is not a whole-bank or whole-syllabus approval.

## Resolution of each residual

| Item | Result | Evidence |
|---|---|---|
| **R9-M1** (*m* shown as metres) | **Fixed** | `content_format.py:71`: a single-letter unit is now treated as a unit only when a space comes before it, it is followed by `/s`, or it follows a `/` that comes after a unit. No `\mathrm` appears anywhere in `contextual-direct-inverse-variation`; seed 0 shows `C=32m` and `k=160/5=32; C=32m` as plain maths (`:38`, `:90`). Spaced units still render upright, e.g. `3 \,\mathrm{cm}` and `±1 \,\mathrm{mm}` in locus-constructions, and `1.8 \,\mathrm{kg} ≈ 2 \,\mathrm{kg}` in check-calculator. The tests cover `C=32m`, `t=5h`, `C=32m/2` and the spaced and compound unit cases. |
| **L13** (redundant brackets) | **Fixed** | All 10 `teaching_context` strings are clean, e.g. `-x²+9` (`:519`), `(x-2)²-4` (`:819`), `2(x+1)²-8` (`:219`), `2x²-18` (`:2019`). I recomputed all 10 turning points, roots and y-intercepts; all correct. Learners now see `(x-3)(x-5)=0` (`quadratic_graphs__2:242`) and `(3)(-5)-y=-16` (`linear_simultaneous_equations__4:1004`), which gives y=1. Powers and grouping are safe: removing brackets from `(x)` and `x-(n)` can't change the meaning, and the test keeps `x+(-3)^2` intact. |
| **L17** (≈, tolerance brackets, minus signs) | **Fixed** | `≈` is now in `_MATH`, so `x ≈ -0.5` is a maths block in all 10 graphical-linear cards (e.g. `:15008`). The tolerance splits as text "(", text "allow", maths "±0.2", text ")"; no maths block has an unmatched bracket. The exponential answers behave the same way (`:2484-2503`). "scale factor −1" now uses a true minus sign (`combined-transformations:6780`, `:6828`). |
| **L20** (origin and tick labels) | **Fixed** | `origin.png`: the "−0.5" x-label and the "−1" y-label are now clearly apart, and "0" sits above the axes. The cosmetic side-effect is listed below. |
| **Exponential domain overrun** | **Fixed** | `graphs.py:220` draws the dashed line to `domain_max`. In `negative-exponential.png` (y=3ˣ, target 0.2, x≈−1.46) the line stops at x=1. The vertical reading line and the curve also stay within −3≤x≤1. |
| **Negative-branch variety** | **Fixed** | The grid step is now 0.2 and targets come in 0.1 steps (`:180`, `:189`). I enumerated by hand the targets that pass the filters: 5 for base 2, 4 for base 3, 6 for base 4 and 4 for base 5, so 19 base–target pairs in total. The bases are integers and the targets have at most two decimals. The 5 odd seeds in the packet give 5 distinct pairs, and their roots −1.46, −0.57, −0.66, −1.32 and −2.32 are all correct. |
| **Calculator setting** | **Fixed** | Both factors vary across all 10 cards, with no duplicates and no brackets. I recomputed all 10 exact products (e.g. 45.2×38.3=1731.16), all 10 one-significant-figure estimates (e.g. 50×40=2000, 20×80=1600) and all 10 mass estimates. Each claimed answer is exactly 10× the true product, and none ends in a false ".0". |
| **Sum y label** | **Fixed** | `sum.png`: the "y" label is above the plot area. For y=x²+2x+3/x, both readings at 7.5 check out, and the negative branch correctly never reaches 7.5. |
| **Fresh diagrams** | **Accepted** | `point-labels.png` has A and B clear of every line. `prime-labels.png` matches seed 0: A′(7,−6) and A″(6,7), with the inverse recomputed. I saw no superseded captures. |
| **Parallel-locus tick labels** | **Not accepted** | See the defect below. |
| **Unknown-finding evidence filter** | **Present, not fully verifiable** | `workbench-demand-evidence.json:1004` adds `prompt_regex: "find\|calculate\|determine"`. The code that applies it isn't in the packet. I couldn't check whether the match ignores case, which matters if prompts start with "Find". |

## Remaining substantive defect (Low, reproducible)

**The parallel-locus label nudge also moves x-axis labels onto the x-axis.**

- **Recipe:** `wb6131:legacy:nssco_visual_loci:2`, part a, in both the question and solution diagrams.
- **Cause:** `legacy.py:165-167` raises every text label whose value equals `cy±distance` by 3.3 mm. That catches the y-axis label it was aimed at, but also the x-axis tick label with the same value. Those x-labels move from 66.0 to 69.3, while the x-axis is at 70.0.
- **Effect:** the axis stroke runs through the labels and hides the minus sign. In the fresh `parallel-locus.png` / `.svg` (lines 25–26, y=70.7 against the axis at y=70.0), the x-axis reads "2 … 0 … 2" instead of "−2 … 0 … 2".
- **Affected seeds:** seeds 0, 3, 4, 6, 7 and 8. For example, seed 0 moves the x-labels −4 and 8 (`:424`, `:469`); seed 3 moves −6 and 4 (`:3910`, `:3946`). Seeds 1, 2 and 5 are unaffected because their locus lines sit at odd values, which have no tick label.
- **Seeds 4 and 8:** one locus line is at y=0, so the origin "0" is also raised from 71.0 to 74.3 (`:5244`, `:9904`).
- **Suggested fix:** move only the y-axis labels (the ones at x = 75.0), never the origin.

## Separate cosmetic notes (outside the review loop)

- `mathFormatting.js:11` joins blocks with spaces, so graphical-linear-solution shows "(allow ±0.2 )" with a space before the bracket.
- Lines run through tick labels: the dashed lines through "0.2" in `negative-exponential.png` and "7.5" in `sum.png`; the y=4x−4 line through "−5" in `origin.png`.
- In `origin.png`, the negative x-labels now sit about 0.2 units left of their gridlines, and "−3" sits outside the grid.
- In `prime-labels.png`, the leader lines cross the A, B, A′ and B′ labels.
- "50 × 40; result:" is split off as plain text (`check-calculator:24`).
- Some worked steps leave fractions unsimplified, e.g. `y=-\frac{2}{2}` in simultaneous-equations seed 0.
- Rules that could misfire but don't in this packet:
  - `prose_formatting.py:42` turns `x-(0)` into `x` regardless of what follows, so `x-(0)^2` would become `x^2`.
  - `:45` would drop a `1(` that follows `_` or a letter, e.g. `x_1(`.
  - `content_format.py:109` would make a spaced single letter in explicit `$…$` maths upright as a unit.

## Scope and limits

I used only Read, Glob and Grep, ran no code and edited nothing. The brief rules out plans, and no plan-writing tool was available, so no plan file was created.

- **Read:** the brief, REPAIRS, the Medium and remaining-Low sections of the previous review, `content_format.py`, `prose_formatting.py`, `test_math_workbench_r9_residual.py`, `graphs.py:114-247`, `legacy.py:140-182`, `mathFormatting.js:1-30`, and the relevant demand-evidence entries.
- **Example files:** 8 of the 11 settings, targeted reads only. Not opened: `quadratic_graphs__2` beyond grep, `power-sum…-sum` JSON, and most of `locus-constructions`.
- **Diagrams:** all 6 full-size PNGs, plus the `parallel-locus.svg`.
- **Not done:**
  - test execution or KaTeX rendering;
  - checking the evidence-selector code;
  - how far any of these issues reach across the whole bank;
  - re-checking the 17 accepted Low fixes or the 2 retained reasons;
  - the wider syllabus.
- The question pool being finite was disclosed and is accepted.
