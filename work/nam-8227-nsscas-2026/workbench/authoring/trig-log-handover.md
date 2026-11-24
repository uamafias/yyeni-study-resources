# Stage E trig/log authoring handover

24 November 2026. AUTHOR Codex parallel trig/log agent, same vendor as the main author. Authority: Vitalis's exact Stage-D manifest approval, `4a0548320dcb9209dcd28e18bd4f6c77423480de6538fcbf1b0f8b6d0e17d8ec`, recipe version `0.1.4`. This is author evidence, not cross-vendor acceptance or application validation.

`source/groups/trig_log.py` constructs question, canonical answer, worked action/reason/result solution, criterion memo and answer-free practice help together. `source/domains/trig_log.json` carries the accepted finite inputs. Runtime dependencies are Python's standard library only; there are no app, database, network or model calls. `choices()` and `build(recipe_id, branch_id, parameters)` implement the shared Stage-E group interface. Full approved curriculum/review/source metadata is enriched by the shared provider.

| Choice | Generated parameter rows | Maximum wholly fresh cards before exposure | Marks |
|---|---:|---:|---:|
| R-form, degree-cycle | 58 | 12 conversion contexts; 10 phase values disclosed separately | 3+4 |
| Principal inverse, solve-or-explain | 47 | 12 target decisions | 3 |
| Log model, graph-intercept | 270 | 30 parameter models | 5 |
| Log model, gradient-target | 20 | 4 parameter models; 2 exponentiation decisions disclosed separately | 3+2 |

Primary `exposure_keys` describe assessed-part identities. `subdecision_exposure_keys` disclose smaller repeated decisions without silently narrowing the approved freshness rule. Changing presentation, target, seed, or output-affecting version does not reset an exposed assessed-part key. The shared provider owns seeded selection, history filtering and explicit exhaustion.

The principal task retains neutral wording and equal tariffs across real/no-real outcomes. Its resolved exact-angle links, outcome label and exact answer are private until submission. The original Cambridge equation remains excluded. The broader three-mark decision has no unqualified same-type learner badge to the narrower Cambridge recovery part.

Every logarithm graph is original SVG derived from its instance's exact points. The vertical axis remains `ln y`; labels use exact terminating decimals. Must-read givens are recorded. Label boxes are transparent, conservatively bound a 28px font, and are tested against the complete line, both axes and the other label. All 270 graphs admit a safe placement, including zero and negative ordinates. Nine original graphs were rasterised with the existing app's `sharp` dependency and their contact sheet inspected by eye, including the explicit zero-ordinate example `graph-04.png`. These are asset checks, not a website/browser interaction test. The application must preserve readable labels and allow suitable enlargement on narrow displays.

## Checks and reproduction

```bash
python3 work/nam-8227-nsscas-2026/workbench/authoring/trig-log-check.py
python3 work/nam-8227-nsscas-2026/workbench/authoring/trig-log-check.py --check
node work/nam-8227-nsscas-2026/workbench/authoring/trig-log-render-check.mjs /path/to/yyeni/apps/web
```

The Python author check uses SymPy and mpmath only outside the runtime package. It independently recomputes all 395 admitted instances:

- R-form roots from the tangent-half-angle polynomial, then direct original-equation substitution at 75-digit precision; generated phase/root round-half-up labels agree.
- Symbolic principal-inverse consistency or the forced-candidate obstruction for every target/divisor.
- Log graph parameters from simultaneous equations and substitution into the original exponential model.
- Log target values from the original-base index laws.
- A separately implemented segment/orientation checker verifies all graph-label geometry.

Two consecutive Python runs agree byte for byte with saved outputs. Eleven invalid-domain fixtures reject: the equal-coefficient R-form, excluded exact Cambridge inverse original, zero-log-amplitude model and nondiagnostic base/gradient pair; plus four equal-valued float substitutions and three equal-valued Boolean substitutions. Runtime domain validation requires the exact dictionary shape, field names and scalar types of an admitted row; Python's `True == 1 == 1.0` does not authorise a noncanonical parameter identity. All 1,111 unique mathematical strings across all 395 instances parse with KaTeX `throwOnError:true`, `strict:error`, `trust:false`. See `trig-log-check.json`, `trig-log-rounding-oracle.json`, `trig-log-frozen-examples.json` and `trig-log-render-check.json`.

`trig-log-marking-fixtures.json` contains 26 explicit correct, partial, wrong, alternative, answer-only, ambiguous and misread expectations. Criterion IDs and award arithmetic reconcile to the approved tariffs. These are authored evidence expectations; a learner handwriting/photo/free-text marker has not been exercised. Ambiguous cases remain pending, rather than receiving an invented zero. Correct bare answers receive supportive working-request feedback, while official method/answer requirements remain in force.

## Notes carried without changing the accepted design

MR03-OPS-D4 is now owner-approved; gross dependencies precede any once-only net A/B deduction. OD-1 and MR09 remain limits. The source-qualified dependent-method and own-equation follow-through clauses are preserved, including the R-form shifted interval, the graph's coherent offset slip and the target's distinction between an earlier omission and a new substitution error. No arbitrary universal method requirement has replaced these local rules.

The common-marker E/F work still needs explicit endpoint/tangent R-form misread eligibility, target-equals-prefactor difficulty changes, principal supplementary-target coincidences, datum identity and competing misreads sharing an earned A/B. No new score ruling is claimed for those carries. This group did not modify the approved planning records, reviews, PDFs, app, standard, registry or pinned checkouts. No commit, push, import, publication or learner assignment occurred.

## E1 repair — 24 November 2026

SE-03 substitutes the actual instance coefficient in all 24 no-real principal
inverse steps. SE-06 checks point-label association by rectangle and centre
distance, and places the origin0 label through the same line/axis safety test.
All 270 graph layouts pass; the old idx132 wrong-point label and idx45 struck
origin are rejected as negative fixtures. All 19 requested idx45–62 and 132 graphs
are rasterised and visually inspected, with four full-size checks.

The R-form worked root step now gives the principal inverse value, the two
integer-shift families, nearby candidates and the rejected values. A=e^1 is
written A=e and a zero ordinate is not subtracted as -(0). The original26
marking expectations, criterion IDs, tariffs, dependencies, numeric answers and
exposure keys are unchanged. Design/rubric version 0.1.4 is explicit; the lead
owns the new runtime/package version and transport mapping. No score ruling for
the carried marking questions is invented.

Run `authoring/e1-trig-check.py` after the ordinary group oracle.
`authoring/e1-trig-render.mjs /path/to/app/apps/web` renders the requested
regression images; `e1-trig-inspection.json` records the images actually viewed.
These are same-vendor author checks, not actual app or cross-vendor acceptance.
