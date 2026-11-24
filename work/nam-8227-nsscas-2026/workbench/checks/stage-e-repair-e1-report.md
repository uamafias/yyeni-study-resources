# E1 repair report — NSSCAS Mathematics 8227

24 November 2026. Owner Vitalis; AUTHOR Codex with three parallel same-vendor
repair agents. NIED December 2020 syllabus, Grade 12. **E1 author repairs complete;
Claude's diff-only confirmation is next. No independent acceptance is claimed.**

## Reviewed baseline and version decision

The reviewed Stage-E manifest is
`22cd1799146ce1d07c25c837f7078b6bb0f717d0e5b9985d57f4371f2ec87025`.
All 1,017 pinned baseline files and that exact manifest are preserved under
`authoring/history/stage-e-0/`. Below, **E0/** means
`authoring/history/stage-e-0/files/work/nam-8227-nsscas-2026/workbench/`.
The old immutable candidate `candidates/fcd4b71e07baa07a/`, manifest
`7022ea5049b0f5b02452828d5226f0a533816873f20d551186925e8aacacb250`,
is unchanged and independently re-hashed by the preservation script.

Output-affecting repairs use native recipe/package **0.1.5**, provider-v1
integer revision **2**. The old 0.1.4/revision 1 bytes remain in the old candidate;
the new provider rejects revision 1 rather than reinterpreting it. Approved design
and rubric identity remains 0.1.4: criterion IDs (including their @0.1.4 segment),
classification version, native selection/part IDs, tariffs, dependencies, domains,
owner scores and bounds do not move. No learner attempts exist. Semantic exposure
keys remain version-free; previously exposed content is not freshened by the bump.

## Finding-by-finding repairs

| ID | Before locator | After locator and correction | Generated scope / check |
|---|---|---|---|
| SE-01 | E0/source/groups/calculus.py:154–222, bare prime | source/groups/calculus.py:146–233 uses raised apostrophe derivatives throughout actual prompts, answers, steps and criteria. | 850 previously affected rows; all 1,211 calculus rows checked. e1-calculus-check.json; actual browser-rendered prime proof; check_e1_runtime.py rejects three seeded bare-prime cases. |
| SE-02 | E0/visual.py trapezium b/modulus/vector templates; E0/calculus.py explicit root | source/formatting.py supplies one exact coefficient formatter, used by both groups; sigma prints its actual ±1 value. | 16 modulus,20 vector,8 trapezium unit-coefficient rows;16 implicit unit coefficients and all 54 implicit sign fields. e1-visual-check.json, e1-calculus-check.json; global byte scan rejects unit patterns and unevaluated sign. |
| SE-03 | E0/source/groups/trig_log.py:157 undefined k | source/groups/trig_log.py:139 (_principal) substitutes this instance's coefficient. | All 24 no-real rows; all 47 principal rows checked. e1-trig-check.json and e1-runtime.json. |
| SE-04 | E0/source/groups/visual.py trapezium b/d reference answers | source/groups/visual.py:214 (_trapezium) keeps canonical learner answers separate from FT/own-curve marking instructions retained in criteria/native memo. | Both answers on all 22 trapezium rows. e1-visual-check.json and full generated-byte regression. |
| SE-05 | E0/source/groups/visual.py:115–118, point labels crossing arms | source/groups/visual.py:103 (_modulus_svg) uses tested label rectangles and short leaders away from arms/axes/points/other labels. | All 44layouts regenerated and independently geometry-checked; actual old idx 4/19 fail negative fixtures. All 44rendered; contacts and worst cases inspected. |
| SE-06 | E0/source/groups/trig_log.py:208–229, wrong-dot association/origin collision | source/groups/trig_log.py:197–265 checks box/centre distance to own point versus the other dot, and chooses/tests origin0 before coordinate labels. | All 270 graphs regenerated/tested;12 wrong associations and18 origin conflicts were 28 distinct defective rows. All 19 requested indices 45–62 and 132 rendered/inspected; old 132/45 fail seeded geometry checks. |
| SE-07 | E0/visual.py d:DB1 and catalogue reviewed required text | source/groups/visual.py:261 and authoring/build_source.py:15 restore unambiguous same-own-curve concavity shorthand; increasing alone is insufficient. | All 22 runtime and reviewed rows. Existing approved d 2/2 expectation restored, not a new score/rule. e1-visual-check.json and e1-runtime.json. |
| SE-08 | E0/calculus.py:161–166 reused proof-route wording and 9/9 | source/groups/calculus.py:146–196 gives gradient-only alternatives their G1–G5 mapping, no supplied target/S3/S4/back-substitution requirement, and its own five-mark maximum. | All 27 gradient-only rows; exact criterion IDs/marks unchanged. e1-calculus-check.json; branch-specific byte regression. |
| SE-09 | E0/authoring/calculus-fixtures.json: calc:normal:alternative and calc:two-extrema:alternative | The same live fixture IDs now show actual gradient substitution and original-function evaluations. | Two scripts repaired, keeping 9/9 and 6/6. All 51 original calculus expectation IDs/scores compared unchanged. |
| SE-10 | E0/authoring/calculus-fixtures.json has no approved rounding cases | authoring/e1-calculus-rounding-fixtures.json adds 15 exponential premature-rounding flips plus four mixed half-boundaries. | 19 additional declared cases, independently recomputed at 90 digits/exact rational arithmetic: distance 233/2→117 on rows 14/134 (exact accepted), displacement ∓265/2 on rows 5/125. No existing expectation changes. |
| SE-11 | E0/calculus.py:174–175 and provider.generate_fresh share a single key list | source/provider.py:52–130 separates freshness_required_keys from emitted exposure_keys; gradients additionally expose implicit-show(a,k). | All 27 gradients emit the proof; required keys unchanged across all 1,702 rows. After gradient idx 0, old normal idx 3 fails freshness; seed 0 now returns normal idx 14. Bounds 23/8 preserved; APP8227-06 updated. |
| SE-12 | E0/source/provider.py:138–150 emits historical outcome tag | source/provider.py:145–177 aliases learner selection/part/ref/asset IDs to quadratic-motion; native_identity resolves only IDs belonging to the frozen question. | All 168 motion rows × three learner modes/reveal states = 504 payloads contain no interior-reversal. Native/teacher/marking IDs unchanged. |
| SE-13 | E0/source/provider.py:152–154 copies raw teacher refs | source/provider.py:156–191 filters displayable original/same-type refs and strips internal source paths/hashes/reviewer fields recursively from teacher metadata. | All 1,702 teacher payloads checked. All 47 principal views exclude held 2023 P1 Q9 and related Cambridge refs; safe source labels/locators remain. |

## Preservation and verification actually run

`authoring/check_e1_preservation.py` compares all 1,702 E0/E1 generated rows, ordered
parameter domains, native branch/part identity, exact criterion order/IDs/types,
marks, dependency/FT/accuracy/answer-only flags, objectives, demand links, whole
Bloom, numerical mathematical data, strict bounds and original 97 declared scores.
Required freshness keys equal the old key list on every row. Only 27 gradient rows
add an emitted proof identity. Five approved design inputs remain byte-identical.
All 1,017 baseline copies and every old candidate file still hash correctly.
`check_e1_delta.py` additionally rejects existing-file changes outside the named
E1 namespaces; replacement live SVGs remain recoverable in history/old candidate.
See `checks/stage-e/e1-preservation.json`; this is an executable guard, not a
hash-only educational correctness claim.

The three group mathematical oracles were rerun: calculus 1,211, trig/log 395,
visual 96. Their focused E1 regressions pass, including actual old defective SVG
fixtures. Shared check_source passes all 1,702 rows and 67 existing negatives;
check_ids reconciles 27 part slots/83 branch marks. Global E1 regressions check
5,106 learner payloads and 1,702 teacher views, bare-prime negatives, the shared-proof
counterexample, canonical-vs-marker answer separation and concavity allowance.

Actual notation: 6,216 distinct generated expressions parse under strict KaTeX.
Prime DOM structure and actual screenshots were checked in addition to parsing.
The scoped wording scan passes on 6,132 distinct generated learner strings with
no 8-word prose run or unsupported assessment claim. Its extraction/formula/feedback
limits remain as documented; Claude's accepted standard-formula and necessary
terminology exceptions are retained below.

The existing app provider-v1 loader/contracts validate 56 instances across 14 choices,
resolve all 326 sealed assets, and reject changed/missing/unlisted files and a sealed
unsupported catalogue field. No app code, server, actual website, recogniser,
marking orchestration, history, MCP or production operation was run.

Canonical build plus **two relocated minimal-input rebuilds pass**: all 385 source
files, eight report files and the candidate manifest match exactly with no path
normalisation. `checks/stage-e/rebuild-proof.json` pins each comparison. The source
and compared reports were unchanged between final canonical and relocated runs.

Current candidate: `candidates/af6f77e940430033/`, manifest
`126850d05311bbb53b013aba4170d88ca612f7d510a8bc7d4fb71737964c61de`.
It remains **candidate**, not installed/accepted for release. The fresh Stage-E
manifest is `authoring/stage-e-manifest.json`. Its exact digest and actual successful
freeze-check receipt are in `checks/stage-e-repair-e1-freeze.json`. That receipt
is intentionally outside its own manifest input set to avoid a self-hash cycle;
the reviewer must compare its digest to the actual manifest and rerun --check.

## Notes, corrections and explicit carries

Folded in: singular second; defined constants/actual bounds; integration terminology;
simplified coefficient/fraction/guard digits/e^1/zero notation; principal R-form
candidate/quadrant/rejection teaching; uniform gradient source label; answer-free
trapezium help; clearer narrow-strip chords; solution asset bound to both c/d;
stale owner-pending language removed from operational qualifiers. Rendering/teaching
changes preserve mathematical values and every approved award condition.

Process correction from review: the original 51 calculus records comprise 29 concrete
scripts and 22 declarative records, rather than 35/16. The total, IDs and scores stay
unchanged. Trig 26/visual 20 include abbreviated trusted evidence descriptions. The
new 19 rounding records are additional declarations, never recogniser tests.

Q15 exceptions accepted by Claude are recorded: standard R sin(theta+alpha) with
R>0 and acute alpha; scalar-product angle command terminology; log-ordinate graph
terminology; and position-vector terminology. Formula/numeric coincidences are not
copying claims. Textbook originals stay internal; exam originals require attribution.

The review's unresolved cases remain unscored notes: trig FT/precision/sign-reading,
vector overprecision, conflicting own-sketch words/overlay, E2 k-read-as-1, stationary
correct-x/wrong-y and exact-then-overrounded answers, alternative implicit C4→5
routes, competing/repeated datum settlement. The product-route 9/9 stays approved.
Reverse normal→gradient proof repetition remains permitted under the approved bound of 23;
we did not silently tighten it to 8.

Runtime/app carries remain explicit: server-pinned digests rather than self-hash
claims; native visual/metadata conversion; atomic learner exposure/reservations;
subdecision repetition reporting; replay identity; excluded-original handling and
named website/permissions/history/marker/MCP acceptance. No optional note is promoted
to a new score. Only actual should-fix/design-blocking findings open a repair round.

No review folder, source PDF, analysis, curriculum, approved design, standard, other
subject, app/pinned checkout or global registry was modified. Existing ignored cache
files are outside the freezes; the review's cache housekeeping is not a content
change. No commit, push, installation, assignment, import or publication.

Next: Claude's diff-only E1 check using `authoring/CLAUDE-STAGE-E1-CHECK.md`, then
named content acceptance and local website/app testing under Vitalis's scope.
