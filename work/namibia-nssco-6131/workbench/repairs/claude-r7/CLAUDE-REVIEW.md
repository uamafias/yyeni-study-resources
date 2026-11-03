**Verdict: changes are still required. I can't approve the R7 bank, and full syllabus coverage can't be certified.**

Most R6 blockers are fixed: the loci answer leak and missing working (M1, M2), historical LP regrading (M3), bisector setting 3 (M4), and most of the explanation and notation items (L1–L4). Every recipe answer I recomputed (about 75) was correct.

Two problems remain before the next review:
- **New High:** 13 graph prompts show raw floating-point fractions. Separately, every constant-graph card asks the learner to "solve" an equation with no x in it.
- **H1 is only partly fixed:** raw LaTeX no longer reaches the learner. But the new text/maths splitter files ordinary words as maths, and the learner view prints every maths fragment as its own display equation.

The coverage index also lists the same recipes for every demand of an objective, so it isn't per-clause evidence. I ran nothing, edited nothing and made no provider or database calls. Plan mode asked for a plan file, but you said not to create one, so the full report is below.

## Findings by severity

### High

**N1. Malformed questions in the new power and constant graph settings.**
- **Float fractions in prompts** (13 prompts in 6 settings). The questions themselves are unusable, though each reference answer is still correct. Examples:
  - `power-sum-exponential-graphs-power-0.json:3448` (seed 1): "solve `\frac{1}{3}=\frac{13333333333333333}{10000000000000000}`"
  - `power-1.json:4752`, `:6996`, `:18860`
  - `power-2.json:2661`, `:5058`, `:12433`
  - `power-3.json:4844`, `:14096`, `:16432`
  - `power-minus-1.json:5887`
  - `power-minus-2.json:19504`, `:25176`
  - All 13 are also in `workbench-bank.json` (for example line 1815784).
  - I checked `power-1.json:4752`: (5/3)x = 10/3 gives x = 2. The reference "x ≈ 2.00" is right; the prompt is broken.
- **Constant-graph equations with no x** (power-0, all 10 cards). Part c asks the learner to "solve" `\frac{1}{2}=\frac{1}{2}` (`:251`), `3=3`, or `\frac{3}{2}=\frac{5}{2}` (`:9934`). The answer is "every x except 0" or "no solution". That isn't an exam-valid equation; it needs to be written as (k)x⁰ = c.
- **Why the author checks missed it:** `r7-katex-check.json` only confirms that KaTeX can parse each block. It doesn't check how sensible the content is.

### Medium

**N2 (H1 residual). The text/maths splitter misfiles words, and the learner view breaks sentences apart.**
- **Cause:** `content_format.py:57` treats any single letter, and short words made only of certain letters, as maths. The article "a" isn't in `_WORDS`, and "log", "cos" and "R" end up in maths blocks.
- **Rendering:** `Content.js:18` turns every maths block into a separate display equation (`$$`) and stacks all the blocks vertically. Sentences end up as stacked fragments.
- **Learner-visible examples (final answer and step results):**
  - `angle-properties.json:319-335` (seed 0, part d): "163°" / "The interior angle sum of" / *a* as a display equation / "pentagon is (5−2) × 180°."
  - All 7 power/sum/exponential settings: references read "x≈2.00", then "(" alone as a display equation, then "allow ±0.2 per reading)." (for example `power-1.json:4822-4836`).
  - `legacy__nssco_visual_linear_programming__2.json:45-61`: "x+y≤8" / "these three inequalities describe" / *R.* as a display equation.
  - Count: 165 such learner-visible blocks across 10 recipe files.
- **Criteria text** (not rendered by the learner components in this packet):
  - `legacy__nssco_logarithms__3.json:61-125`: "k log x" as maths, which renders as italic *klogx*, plus three article "a"s.
  - `legacy__nssco_sine_cosine_rules__2.json:75`: "cos C" as maths, which renders as italic *cosC*.
  - "A valid setup…" splits off "A" as maths 506 times in 22 recipe files.
  - Broader pattern: about 5,840 grep matches in 171 recipe files.

**N3. The "solve graphically" parts on power graphs always ask for a value already in the table.**
- In all 50 cards for n = −2, −1, 1, 2 and 3, the answer is exactly x = ±2.00. That is one of the x-values the learner already tabulated in part a, so it can be read off the table without using the graph.
- Only the sum and exponential settings need a genuine graph reading (for example sum seed 0: x ≈ 0.32, which I checked as −3 + √11).
- So objective 7d:06 ("solve associated equations approximately by graphical methods") is only weakly assessed for the new power forms.

**N4. The demand evidence index is per objective, not per clause.**
- Every demand under an objective lists the same recipes. 7d:05 demands d01–d09 ("power −2", "power 3", "positive-integer-base exponential", and so on) each list the same 11 recipes (lines 12850–13016). The same happens for 1a:01 d01–d06 and 2main:01 d01–d05.
- The index therefore can't show which part tests which clause. The REPAIRS claim of "explicit per-clause coverage evidence" isn't met.

**N5. Content gaps I confirmed against syllabus pages 9–26** (actual prompts read):
- **1l:05 (bills and receipts):** all evidence is water bills — `water-bill-table` and `legacy__nssco_income_taxes_bills__2`, whose 10 cards all use "Tangeni's" water bill. There are no telephone or cell-phone bills, till receipts, payment receipts or clothing account statements, which are the syllabus's own examples.
- **1j:07 (variation in algebraic terms, "contextually or algebraically"):** only `legacy__nssco_expressions_formulae__4` covers it, with 10 purely algebraic cards. There is no contextual variation.
- **5e:01 ("method of intersecting loci"):** the new general-angle setting only constructs the two bisectors. Intersecting them with a second locus only happens on the coordinate axes (`intersecting-loci`).

### Low

- **"a enlargement"** in `combined-transformations` stems, lines 3330, 6490, 8058 and 12878.
- **Locus labels:** in `locus-constructions` seeds 2, 6, 8, 9 and 12–22, the A and B labels now sit just under the upper locus line (full-size seed 2). The points look as if they lie on the locus.
- **`general-intersecting-line-loci` s0 reference:** at full size the second (horizontal) bisector is thin and grey, close to the style of a construction line.
- **Parts repeat each other's answers:**
  - `ratio-all-shares` seed 0: parts a, c and d all give 116 and 261 (lines 13–273).
  - `exponential-equation-forms`: part c always has the same answer as part b.
  - The same file shows `\frac{35}{1}=35` (line 973).
- **Graph scale:** `graphical-linear-solution` s0 has a y-axis from −20 to 25 in steps of 5 for a line that only spans −11 to 3, and the reading at y = −2 isn't on a grid line.
- **Leftover notation:** `u=x-(0)` and an unexplained centre letter "E" in `legacy__nssco_transformations_coordinates__3.json:208`. `defining-sets-all-forms` always uses multiples of 4 and even numbers.

## R6 resolution ledger

| R6 | R7 status | Evidence |
|---|---|---|
| H1 bare LaTeX labelled Markdown | **Partly fixed; new splitter defect (N2)** | Text blocks can no longer contain `\cmd` (`content_format.py:112`), and KaTeX parses everything. Misfiled words and the stacked display rendering remain. |
| M1 loci question leak | **Fixed** | s0 question shows full ticks (x from −10 to 10, y from −8 to 12). |
| M2 loci working | **Fixed** | Quadratic working and ±0.2 tolerance present. I recomputed P(0,4) r=5, P(0,3) r=6, P(0,2) r=5 and P(0,3) r=8. |
| M3 historical LP | **Fixed** | Provider never called (`maths_workbench.py:635-645`, `flashcard_grading_service.py:441-443`); notice shown; retry hidden. All 10 prepared LP:1 solutions draw strict boundaries dashed and non-strict ones solid (contact sheets; full size for 1001, 1002, 1006). |
| M4 bisector setting 3 | **Fixed** | M1 is the angle-sum step; e.g. 180−38−59 = 83°, 180−32−20 = 128°. |
| M5 scope | **Partly fixed** | New generators are present and correct: the general bisector locus; all-shares ratio (5 seeds checked); monomials; exponential equations (12 checked); six transformation combinations (seeds 0, 2, 4, 5 checked); negative x and both reciprocal branches. But see N1, N3 and N5. Formula text is now readable. |
| L1 "given quantities" template | **Fixed** | 0 hits. |
| L2 double minus | **Fixed** | 0 `--` hits. |
| L3 generic reasons | **Fixed in the cards sampled** | LP:2 now says "read"; strict/broken wording correct; "negative numerators" gone. |
| L4 algebraic fractions | **Fixed** | Two meaningful steps per part (checked seed 0, parts a and b). |
| L5 label collisions | **Mostly fixed** | Transformation labels clean in 25 seeds; new locus label issue (Low). |
| L6 notation | **Partly fixed** | Bracketed numbers kept by stated policy; percentiles correct (median 18, Q1 13, Q3 25). |
| L7 contexts | **Fixed** | Girls/boys contexts now. |
| L8 variety | **Partly fixed** | Transformations now varied; power-0 still has few variants and is now degenerate (N1). |
| L9 reference diagrams | **Fixed** | Vertical reading line drawn; percentile guides drawn. |
| L10 retirement and normaliser | **Accepted from code reading only** | Semantic flags plus hashes (`legacy.py:97-114`); not executed. |
| Packet | **Fixed** | 207 listed panels match contact sheets 0–206. |

## Objective coverage verdict

- **Mapping:** 152 of 152 objectives have at least one mapped assessed card. That is presence, not coverage.
- **Clause probes:** I checked 24 objectives at clause level against the actual prompts:
  - **Adequate on what I saw (10):** 1a:01, 1j:01, 2main:01 (including the `(x,y)` and interval set-builder forms), 5a:05, 5c:03, 6b:01, 6c:02, 6e:03, 9b:02, 9b:05.
  - **Partial (5):** 1l:05, 1j:07, 5e:01 (all N5) and 7d:05/06 (N1, N3).
  - **Not judged at clause level (9):** the rest. I saw supporting prompts or recomputed answers, but didn't decide sufficiency.
- **The other 128 objectives are unreviewed.** Most of the 439 demands haven't had clause sufficiency accepted by anyone. N4 means the index can't stand in for that review.

## What I actually reviewed

- **Settings:** about 33 of 401 opened in depth. Packet-wide searches across all 401 for:
  - float artefacts
  - misfiled maths blocks
  - the L1, L2 and L3 phrases
  - variation and bills clauses
  - power-graph solve answers (all 8 power settings)
- **Examples:** about 65 cards (about 170 parts) read, about 75 results recomputed. No mathematical errors found in any recipe answer.
- **Images:** all 13 contact sheets (207 panels), plus 6 full-size PNGs:
  - LP 1001, 1002 and 1006 solutions
  - locus-constructions s2 reference
  - general-intersecting-line-loci s0 reference
  - graphical-linear-solution s0 reference
- **Syllabus:** PDF pages 9–26 read in full.
- **Code:** read in full: `content_format.py`, `Content.js`, `review_policy.py`, `family_prepared_visuals.py`. Read in part: the maths workbench router, `flashcard_grading_service.py`, `legacy.py`.

**Not reviewed:**
- the other ~368 settings
- the other 195 panels at full size
- PDF print scale and greyscale
- test runs
- provider and photo marking
- the content of the 41 retirement records
- tariffs

Bounded sampling is not exhaustive approval.

## Repairs needed before the next review

1. **Fix float fractions:** build graph targets from exact rationals, and add a validator that rejects digit runs of 12 or more in prompts.
2. **Fix power-0 part c:** rewrite it as a real equation in x, or drop it.
3. **Fix the splitter** (`content_format.py`):
   - Treat articles and prose words as text.
   - Use `\log`, `\cos` and similar for function names.
   - Keep punctuation and labels such as "R." out of maths blocks.
4. **Fix the learner rendering** (`Content.js:18`): render maths blocks inline within one paragraph instead of stacking display equations.
5. **Add a semantic check, not just KaTeX parsing:** no single-letter articles in maths, no maths block that is only punctuation.
6. **Vary the graph-solve targets** so the answers aren't tabulated x-values.
7. **Make the evidence index genuinely per demand:** link each demand to the specific parts that test it.
8. **Close the N5 gaps:**
   - phone bills, till receipts and account statements (1l:05)
   - contextual variation (1j:07)
   - a general-angle bisector intersected with a second locus (5e:01)
9. **Fix the Low items**, then rerun the author checks and repackage.
