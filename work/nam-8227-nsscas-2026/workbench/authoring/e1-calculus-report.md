# E1 calculus repair evidence

24 November 2026. Codex AUTHOR, NSSCAS Mathematics 8227, NIED December 2020 syllabus.
No new design, owner ruling, app operation or independent acceptance is claimed.

| Finding | Before | Corrected output and evidence |
|---|---|---|
| SE-01 | Frozen calculus.py154–222;850 instances contain bare prime in1,862 fields. | Live calculus.py154 onward uses apostrophe notation for every y/f derivative. Exhaustive 1,211-row scan rejects any bare prime outside an explicit superscript; two seeded corruptions fail. Browser render proof shows the superscript visually on 18 actual expressions across all 4 affected choices. |
| SE-02 | Frozen calculus.py162 explicit root displays 1e^ and symbolic sign(). | Live calculus.py162 uses common exact coefficient formatter and evaluates sigma to ±1. 16 of 54 implicit branch rows had a unit-square coefficient; all 54 sign values now print directly. |
| SE-08 | Frozen calculus.py161–166 gradient alternatives reuse S3/S4/target text; open fixture says 9/9. | Live calculus.py164 alternatives use G1–G5 and exact point substitution, with the approved explicit-root mapping. No target/back-substitution requirement or S3/S4 appears in gradient-only alternative text. The branch note identifies its 5/5 maximum. |
| SE-09 | Normal and two-extrema alternative scripts omit required substitutions/evaluations. | The two exact fixture IDs now show m=-6e^0(-4)/(3e^0+2(-4))=-24/5 and f(-1)=4/f(1)=0 via actual polynomial evaluations. Original 9/9 and 6/6 expectations retained. |
| SE-10 | Required exponential flips and half boundaries are not frozen as E/F expectations. | Separate e1-calculus-rounding-fixtures.json holds 15 approved exponential premature-rounding flips and 4 mixed half-boundaries. Independent 90-digit exponential/Decimal half-up and exact rational leg integration reproduce each accepted/rejected number. Existing 51 fixture IDs and all expected scores remain unchanged. |

Cheap notes folded in: first 1 second singular; the integration constant C is defined
when introduced; implicit constant derivative uses the actual displayed number;
steps use actual F(T) values rather than undefined T; integration bounds replace
boundary conditions; normal point-gradient construction suppresses x−0 and doubled
signs; exact/3 significant-figure instruction has one wording in calculus. Runtime
recipe version is 0.1.5, with design_rubric_version 0.1.4; criterion IDs stay@0.1.4.
No parameter domain, strict bound, mark type, dependency, tariff, Bloom or previous
owner score changed. Required exposure lists are byte-for-byte unchanged; shared
proof exposure is handled by the lead's provider split, not by tightening gradient
freshness to 8.

## Commands and evidence

- `PYTHONDONTWRITEBYTECODE=1 python3 .../authoring/calculus-check.py`: all 1,211 rows independently recomputed, seven branches,21 frozen parameter cases,51 existing declarations.
- `PYTHONDONTWRITEBYTECODE=1 python3 .../authoring/e1-calculus-check.py`: baseline structural/domain/key and old-score comparison;850 prime rows;54 implicit sign/format rows;27 gradient alternative rows;two repaired scripts;19 new rounding declarations.
- `node .../authoring/e1-calculus-render.mjs <existing-app>/apps/web`: strict KaTeX rendering for 54 selected actual expressions and three before/after superscript comparisons.
- Existing Playwright CLI loaded a local static proof, using existing KaTeX CSS/fonts, and captured `e1-calculus-primes-before-after.png` and `e1-calculus-primes-emitted.png`; both were viewed. The own browser/server were then closed. No app feature was run.

The frozen 51 records are 29 concrete scripts plus 22 declarative records under the
reviewer's classification, not 51 successful raw-response marking tests. New 19 rounding
records are explicitly declarations with independently checked numerical boundaries.
Competing datum and non-product C-misread routes remain unscored carries. Normal
product C4→5 stays 9/9. No commit/push; no review/history/design/sourcePDF/app/standard
or other subject edited.
