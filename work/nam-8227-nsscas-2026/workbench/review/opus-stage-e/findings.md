# Stage-E cross-vendor content review findings: NSSCAS Mathematics 8227 Workbench pilot

**Reviewer:** Claude Opus 5.5 (cross-vendor REVIEWER; the author is Codex). **Date:** 24 November 2026.
**Inputs** (frozen in `inputs.json`):
- Stage-E manifest `22cd1799…`, content digest `b62030c6…`;
- candidate `fcd4b71e07baa07a`, manifest `7022ea50…`;
- approved Stage-D manifest `4a054832…`;
- Git HEAD `fa0a09d4`.

**Prompt:** `authoring/CLAUDE-STAGE-E-REVIEW.md`.

## Method (run in parallel)

**Lead, in the foreground:**
- Froze the inputs and ran Codex's `approval_snapshot.py` (pass, 7,539 pins) and `freeze_stage_e.py --check` (pass, 1,017 files).
- Checked that the approved Stage-D files changed only by one identical two-line "current gate" banner. The exceptions are OWNER-CHECKPOINT and app-change-handoff, which gained only their Stage-E receipts.
- Compared all 27 generated parts against the approved part register at first, middle and last domain rows: 0 criterion-ID or tariff drift, 83 marks, Bloom 13 Apply / 1 Analyse.
- Read instances end to end.
- Rendered the derivative notation.
- Re-verified every should-fix item below against the current bytes: reran the checkers' reproduction scripts, read the code and work-order lines, and looked at the rendered images myself.

**In the background:** a rebuild in two relocated copies (`rebuild.json`). All 384 source files, all 386 candidate files and every report were byte-identical. The group oracles and the wording scan also reproduce once their extra inputs are supplied.

**Five independent same-vendor agents** (their evidence is in `check-*.json`):

| Checker | Scope | Main counts |
|---|---|---|
| calc | 7 calculus choices | All 1,211 rows recomputed from learner-visible text with SymPy; 6,697 worked-step results; 51 expectations read; 19 fresh responses awarded |
| trig | 4 trig/log choices | All 395 rows recomputed with mpmath/SymPy; 26 expectations; 33 fresh responses; 11 graphs rendered and viewed |
| visual | 3 visual choices | All 96 rows recomputed, including coordinates read from the question SVGs; 20 expectations; 16 fresh responses; 20 renders viewed |
| runtime | Provider, privacy, freshness, integrity | 1,702 rows; 5,106 learner payloads; 1,858 asset-access checks; 2,973 exposure keys; 42 frozen examples replayed; 9 tamper cases |
| wording | Q10/Q15 learner text and labels | 6,936 distinct learner strings; 6,028 KaTeX strict renders; 180 rendered screenshots; 430 source PDFs scanned; all 19 displayed exam references opened at their PDF page |

## Results

**No design blocker.** Every mathematical answer and worked-step value checked agrees with independent recomputation, on all 1,702 rows. No approved tariff, criterion ID, dependency, domain, count, Bloom level or owner score has drifted.

**13 should-fix findings.** All are local corrections within the approved design, and none needs an owner decision.

### A. Learner-facing notation and text (Q10)

| ID | Locator and scope | Defect (expected vs actual) | Basis | Minimal correction |
|---|---|---|---|---|
| **SE-01** (lead; wording-E-01) | `source/groups/calculus.py:154–222`. 850/1,702 instances across 4 calculus choices: the implicit show-that prompt and answer, and the stationary-point solutions; 1,862 fields. | Bare `\prime` renders as a full-size mark on the baseline: the reader sees "y/" and "f//(x)", which can look like division (`evidence/prime-notation-render.png`). KaTeX strict mode accepts it, so `notation.json` cannot catch it. | Q10 "broken notation"; decoded-render rule | Use `y'`, `f'(x)`, `f''(x)` (KaTeX raises these as superscript primes) or `\frac{dy}{dx}`. Exposure keys do not change. |
| **SE-02** (visual-E-02, wording-E-03, calc-E-04) | Trapezium (b) prompt, b:B1 text and step: `\int_2^6 1\ln(x^2-2x+1)` (8/22). Modulus answer `y=-1\lvert x-3\rvert+2` (16/44). Vector steps `1p-1`, `2(1p-1)` (20/30). Implicit explicit-root formula `1e^{4x}` (16/54) and an unevaluated `\operatorname{sign}(-9)` (54/54). | Unit coefficients are printed, one of them in a question prompt; a sign function is left unevaluated. | Approved convention "Stems/solutions omit zero terms, unit coefficients and doubled signs" (motion `WO:71`); Q10 | Add one coefficient formatter (1→'', −1→'−'); print σ as ±1. Values and marks are unchanged. |
| **SE-03** (trig-E-01, wording-E-05) | `source/groups/trig_log.py:157`. All 24 no-real principal-inverse solutions, e.g. idx 0 "Solve sin⁻¹(2x)=−π". | The decisive step shows `\sin^{-1}(kx)` with the template symbol k, which is never defined for the learner. | Q10, no unexplained symbols | Format it with the instance coefficient, or use a defined generic u. |
| **SE-04** (wording-E-02) | Trapezium reference answers, parts (b) and (d), 22/22. | Marker rules appear in the learner's revealed answer: "Correct 3-significant-figure products of a coherently used own (a) estimate are followed through"; "For a clearly different own curve, apply the stated own-graph follow-through rules." | Q09/Q10: keep the canonical answer separate from marking rules | Move these sentences to the criteria or teacher memo; keep the learner answer canonical. |

### B. Diagrams (Q10)

| ID | Locator and scope | Defect | Basis | Minimal correction |
|---|---|---|---|---|
| **SE-05** (visual-E-01) | `source/groups/visual.py:115–118`. 35/44 modulus question diagrams; worst cases idx 19 and idx 4. | A graph arm runs through at least one point-name label (L, R, Y, L/Y, R/Y). Zero and Y labels are always placed below the axis, whichever way the arm continues (`evidence/modulus-idx19-label-collisions.png`). The coordinate key stays exact. | Approved modulus `WO:41`: "Place zero labels outside the V… Keep axes, points and labels legible." | Place each label on the side away from the continuing arm, or use a short leader; add a label-versus-arm overlap test. |
| **SE-06** (trig-E-03 and trig-E-02) | `source/groups/trig_log.py:208–229`. 12/270 graph-intercept presentations, e.g. idx 132; 18/270 (idx 45–62) for the origin label. | **Misplaced label:** in idx 132 "(4, −0.25)" sits directly under the dot at (3, 0), and its own dot has no label (`evidence/log-graph-idx132-misplaced-label.png`). **Origin label:** the plotted line strikes through the "0", which then reads like θ (`evidence/log-graph-origin-label-struck.png`). | Approved log `WO:56` (exact labelled coordinates are must-read givens); Q10 | Reject a label position that sits nearer the other point than its own; include the origin label in the overlap test. |

### C. Marking data and declared expectations (Q06)

| ID | Locator and scope | Defect | Basis | Minimal correction |
|---|---|---|---|---|
| **SE-07** (visual-E-03) | Runtime `d:DB1` achievement and the catalogue's reviewed `required` text for trapezium (22/22). | The text leaves out the approved allowance "Unambiguous concavity shorthand can establish the geometry". "Underestimate, because ln(x−1) is concave down" scores d 2/2 under the work order but 1/2 under the runtime text. | Approved trapezium `WO:79`; exemplar `:63` | Append the allowance to the DB1 achievement and the reviewed row. The tariff is unchanged. |
| **SE-08** (calc-E-01) | `source/groups/calculus.py:161–166`. All 27 gradient-only rows. | The gradient-only part reuses the show-that alternatives. These cite S3/S4 and "back-substitute C to establish the target", but the part has only G1–G5 and no target. Its `private_math.open_fixture` also says "9/9", which is the normal-branch total. | Approved CALC-D1-DEV05 (explicit-root route for gradient-only) and CALC-D2-DEV09 (S1–S4 mapping scoped to show-derivative) | Give gradient-only its own alternative text in G1–G5 terms with no target or back-substitution requirement. A valid differentiation route still earns credit under Q06. Give it the correct branch fixture text. |
| **SE-09** (calc-E-02) | `authoring/calculus-fixtures.json` `calc:normal:alternative` (expects 9/9) and `calc:two-extrema:alternative` (expects 6/6). | Each script leaves out working the rubric requires. The first gives "At P this is −24/5" with no substitution shown (H1, then the dependent H2): 7/9 by the rubric. The second gives "original function values 4,0" without evaluation (P4). | Implicit and stationary work orders; the F audit repaired the same gap only in the canonical scripts | Add the shown substitution and evaluation to the scripts, keeping the expectations; or re-award them by the rubric. |
| **SE-10** (calc-E-03) | No Stage-E expectation or check carries these fixtures. | The approved work order requires E/F to keep the exponential early-rounding flip fixtures and the exact 116.5 → 117 half boundary. Live rows exist: interior-reversal 14 and 134 have distance 233/2 m; rows 5 and 125 have displacement ∓265/2. | Approved motion `WO:71` | Add declared expectations for the rounding flips, for 233/2 → 117 (exact accepted) and for ∓265/2. |

### D. Runtime exposure and privacy (Q07/Q11)

| ID | Locator and scope | Defect | Basis | Minimal correction |
|---|---|---|---|---|
| **SE-11** (runtime-E-01) | `source/groups/calculus.py:174–175`; `provider.generate_fresh`. | A gradient-branch instance never records the shared proof identity `["implicit-show",a,k]`. After exposure to gradient idx 0 (a=1, k=2), a fresh test request for the normal branch returns idx 3 (a=1, k=2, different C). Its show-that proof is step-for-step the solution already revealed. | Approved implicit `WO:134` ("exposure keys include revealed examples and shared components across branches"); handoff APP8227-06 ("shared derivative proof identities… test cross-branch shared proof/gradient exposure") | Separate the keys an instance exposes from the keys that must be unseen. Gradient instances also expose `implicit-show(a,k)`, but do not require it to be fresh. This keeps the approved bounds: gradient 23, normal 8. |
| **SE-12** (runtime-E-02; calc-E-05; wording-E-13) | `source/provider.py:138–150` `learner_projection`. All 168 interior-reversal rows. | The learner payload carries `interior-reversal` in `selection_id` and in every part ID. For the 24 no-change rows (idx 144–167) the tag is false, e.g. v=−3t²+9t+12 on [0,3]. | Approved motion `WO:27` ("internal branch ID… historical; public title and stem outcome-neutral"); handoff ("not learner copy… do not leak… through metadata or labels") | Emit outcome-neutral public selection and part IDs in the learner projection. Qualified IDs stay unchanged in native, teacher and marking data. |
| **SE-13** (runtime-E-03) | `source/provider.py:152–154` `teacher_projection`. | It copies every examination reference unfiltered. That includes the held 2023 P1 Q9 reference with its "Held defective…" note, the Cambridge related reference, and the repo `source_path`, `source_sha256` and `verified_by` reviewer notes on all 31 references. | Review prompt: "Related/held refs stay internal"; handoff APP8227-04 (internal paths, hashes and reviewer notes excluded) | Give teachers the displayable same-type labels and safe locators only. Leave out held refs, paths, hashes and reviewer notes. |

## Notes (no repair round; fold into the E1 edit where cheap)

- **Wording:**
  - "the first 1 seconds" (48 motion prompts);
  - Python float noise "3.8066624897703197…" and `\frac{2}{2}`, `\sum_{j=1}^{1}`, `A=e^{1}`, `-(0)`;
  - undefined C and T in single steps;
  - "boundary conditions" where the step means the bounds;
  - the 3 s.f. instruction is phrased four ways;
  - one label reads "Gradient part: same type as…" while the other 18 read "Same type as…".
  - (wording-E-04/08/09/10/12/14, trig-N-07)
- **Teaching:**
  - The R-form root step jumps straight to the two transformed roots, with no principal value, quadrant reasoning or rejected candidate (trig-N-01, wording-E-11).
  - The trapezium hint "recognise a square" supplies the fact that b:B1 credits (visual-E-N2).
  - On width-1 strips the chords are hard to tell apart from the curve (visual-E-N7).
- **Metadata:**
  - The trapezium solution diagram also shows the part-(d) answer but is bound only to part (c) (visual-E-N1).
  - Stale "pending Vitalis approval" status strings remain in runtime qualifiers and policies (visual-E-N4).
  - A teacher-side `learner_display_reason` reads "original" on a same-type reference (visual-E-N3).
  - `approved_capacity` means the fresh bound for some choices and the raw count for others (calc-E-08, runtime-E-09).
  - The principal-inverse top-level objective and demand IDs differ by outcome in the teacher view (trig-N-05; this is an app carry).
- **Q15:** the one maths-aware run of 12 or more words is the standard constraint "R sin(θ+α), where R>0 and 0°<α<90°". It appears in at least eight Cambridge papers, and I accept it as a standard-formula exception (wording-E-06). The 8–11-word runs, such as "Use a scalar product to find angle AOB", are necessary command terminology (wording-E-07). The prose scan found no run of 8 or more words and no examiner-reward or prediction claims.
- **Integrity tooling (app carries):**
  - `verify_candidate.py` accepts a tampered candidate whose manifest has been re-sealed; only the pinned manifest hash catches it (runtime-E-04).
  - `validate_instance` accepts a changed answer once the self-digest is recomputed (runtime-E-05). The app must store the frozen hash on the server.
- **Freshness (app carries):**
  - `generate_fresh` does not report repeated R-form and log sub-decisions (runtime-E-07).
  - The `normalized_exposure` alias pattern is narrow (runtime-E-08).
  - Keys for excluded exam originals cannot be requested (runtime-E-10).
  - The generation identity needed for replay differs between `generate` and `generate_fresh` (runtime-E-06).
- **Process:** the "35 concrete scripts" are really 29 scripts plus 22 declarative records (calc-E-06).

## Rubric cases that stay pending (E/F/app carries; no score invented)

- **Trig:**
  - Does T-B1 depend on the gradient mapping (FT-02)?
  - Does A=10^k earn G-M2 (FG-03)?
  - Do over-precise roots (299.55) earn b-A (FR-08b)?
  - Is a legible sign change with no restated equation a misread or an own slip (FP-08, trig-N-06)?
- **Visual:**
  - The more precise vector angle 104.25° (true value 104.2518…; half-up versus banker's re-rounding).
  - Part (d) where the words say "under" but the drawn overlay shows chords above the curve.
- **Calculus:**
  - E2 when k is read as 1;
  - C2 with the correct x and a wrong y;
  - a correct exact answer followed by an over-rounded "≈37".
- **Unchanged from D4:**
  - C 4→5 routes other than the product route;
  - competing-datum settlement;
  - repeated-datum identity.

## For Vitalis's attention (no action needed)

**Reverse cross-branch exposure.** A learner who sees a normal-branch solution can later get a gradient test on the same (a, k) with a different C, and that test counts as fresh. The approved gradient bound of 23 permits this, so I have not raised it as a defect. Tightening it would drop that bound to 8, which is Vitalis's decision.

## Confirmed (accepted within the named scope, subject to SE-01–SE-13)

- **Mathematics:** every answer and every worked-step value on all 1,702 rows, recomputed independently from learner-visible data, including the 1,336 function evaluations and the SVG coordinates. Givens are sufficient and answers unique. Rounding is correct, including the near-boundary values (299.5519°, 63.434949°, 104.2518°).
- **Domains** reproduce from the work-order rules: 27/27, 540, 256, 137/35, 56/14, 168 = 144 + 24 with 28 shapes, 58, 47 = 23 + 24, 270, 20, 44, 22, 30. The trapezium h=2 original subtask is excluded.
- **Marking data:** all 27 parts keep their approved criterion IDs, order, mark types, tariffs, dependencies, F.T./c.a.o./www flags and answer-only rules; total 83 marks.
  - All 97 declared expectations agree with the rubric, except the two in SE-09.
  - 68 fresh responses were awarded; the undecidable ones are listed above.
  - The C 4→5 product-route 9/9 fixture is kept and scoped to the product route only.
  - The nonunit-k guard is in all 56 exponential rows.
- **Runtime:**
  - deterministic at seeds 0, 1, 42 and 2⁶³−1; all 42 frozen examples replay byte for byte;
  - every invalid seed, revision, index and type coercion is rejected;
  - all 14 strict fresh bounds are exact;
  - exhaustion is bounded, and practice repeats are labelled "repeated-practice";
  - a test with repetition raises an error;
  - test mode carries no help, and solution assets are refused before reveal or to another instance or role;
  - every unsealed tamper is rejected.
- **Labels:**
  - all 19 learner-displayed references point to a real paper, question, part and printed page;
  - each is the same type as its bound part, is scoped to that part, and is never card-wide;
  - no held original appears;
  - Cambridge is never shown as Namibian;
  - no textbook content appears in any payload.
- **Q15:** no copied examination prose (see the notes).
- **Release integrity:** the candidate and reports rebuild byte for byte in two relocated copies. The provider-v1 contract hashes still match the app as read.

## Not checked

- No app server, website, UI, history, marker orchestration, MCP, installation or production operation was run.
- There is no recogniser; every award above is a reviewer reading of a typed script against the rubric.
- The renders used sharp/librsvg and Quick Look, not the app's display. Only samples were viewed (the counts are above); the remaining SVGs were checked by parsing.
- Examiner-report award pages were not re-read for every row; the approved work orders were taken as their transcription.
- Formula novelty against the textbook relies on unverified OCR.
- **Process disclosure:** the wording checker's first provider import used `python3 -I`, which ignores `PYTHONDONTWRITEBYTECODE`. It rewrote two pre-existing, git-ignored caches: `source/__pycache__/__init__.cpython-313.pyc` and `source/groups/__pycache__/__init__.cpython-313.pyc`. They sit outside every freeze manifest, and the freeze check still passes. No other workspace file changed apart from this review folder.
