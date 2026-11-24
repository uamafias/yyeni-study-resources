# Stage-E repair E1: NSSCAS Mathematics 8227

You are Codex, AUTHOR for the 8227 Workbench pilot. The workspace is `work/nam-8227-nsscas-2026/`. Vitalis's decisions are final.

## Where Stage E stands

Claude reviewed Stage E (candidate `fcd4b71e07baa07a`, manifest `7022ea50…`; Stage-E manifest `22cd1799…`).

**What holds:**
- All 1,702 rows are mathematically correct.
- The approved design is preserved exactly.
- Runtime freshness, exhaustion and reveal behave as specified.
- Labels are accurate.
- The rebuild is byte-identical in two relocated copies.

**What needs repair:** 13 should-fix items, and no design blocker. E1 is a targeted repair. It changes:
- no tariff, criterion ID, dependency, domain, count, Bloom level, owner score or approved bound;
- no analysis input.

**Read first,** in `workbench/review/opus-stage-e/`:
- `report.md`;
- `findings.md`;
- the `check-*.json` record behind each ID;
- the images in `evidence/`.

**Before changing anything:**
- Keep candidate `fcd4b71e07baa07a` and the current Stage-E manifest recoverable, for example under `authoring/history/stage-e-0/`.
- Never rewrite old candidates.
- No learner attempts exist, because nothing was installed. Apply your version policy, keep exposure keys version-free, and record your version decision in the report.

## Repairs

1. **SE-01, notation.** Replace bare `\prime` with `y'`, `f'(x)`, `f''(x)` (or `\frac{dy}{dx}`) in every calculus prompt, answer, step and criterion. Add a check that fails on bare `\prime` outside a superscript.
2. **SE-02, unit coefficients and signs.** Add one coefficient formatter (1→'', −1→'−') for:
   - the trapezium (b) prompt, b:B1 and its step;
   - the modulus formula answer;
   - the vector steps;
   - the implicit explicit-root formula.

   Print σ as its value. Add a check for `1\ln`, `1e^`, `1p`, `-1\lvert`, `1(` and an unevaluated `\operatorname{sign}`.
3. **SE-03, undefined k.** Fix the principal-inverse no-real step at `trig_log.py:157` to use the instance coefficient.
4. **SE-04, marking rules in learner answers.** Move the follow-through sentences out of the trapezium (b) and (d) reference answers into the criteria or the teacher memo.
5. **SE-05, modulus labels.** Place zero and Y labels away from the continuing arm, or use a short leader (`WO:41`). Add a label-versus-arm overlap test across all 44 rows.
6. **SE-06, log-graph labels.**
   - Reject any label position nearer the other point than its own.
   - Include the origin "0" in the overlap test.
   - Re-render and visually inspect at least idx 45–62 and 132.
7. **SE-07, trapezium d:DB1.** Add "Unambiguous concavity shorthand for the same own curve can establish the geometry; 'increasing' alone cannot." to the DB1 achievement and to the catalogue's reviewed row (`WO:79`).
8. **SE-08, gradient-only alternatives.**
   - Give the gradient-only part its own alternative-route text in G1–G5 terms, with no target, no S3/S4 and no back-substitution requirement. The explicit-root route is CALC-D1-DEV05.
   - Correct its `open_fixture` text, which currently gives the normal branch's 9/9.
9. **SE-09, two declared expectations.** Make each script match its expectation: add the shown substitution to `calc:normal:alternative` and the shown evaluation to `calc:two-extrema:alternative`, or re-award each by the rubric.
10. **SE-10, motion rounding fixtures.** Add declared expectations for:
    - the exponential early-rounding flips;
    - distance 233/2 → 117 (exact 233/2 accepted), interior-reversal rows 14 and 134;
    - displacement ∓265/2, rows 5 and 125 (motion `WO:71`).
11. **SE-11, shared proof exposure.**
    - In the provider, separate the keys an instance **exposes** from the keys that must be **unseen** for a fresh question.
    - Gradient instances also expose `["implicit-show",a,k]`, without requiring it to be fresh. The approved gradient bound 23 and normal bound 8 stay unchanged.
    - Add a negative fixture: after gradient idx 0, a fresh normal test must not return idx 3.
    - Update `app-change-handoff.md` APP8227-06.
12. **SE-12, outcome tag in learner payload.**
    - The learner projection must emit outcome-neutral public selection and part IDs for the mixed-motion choice. Qualified IDs stay unchanged in native, teacher and marking data.
    - Add a negative fixture: no learner payload contains `interior-reversal`.
13. **SE-13, teacher view.**
    - `teacher_projection` must leave out held and related refs, `source_path`, `source_sha256` and reviewer notes, keeping the displayable same-type labels and safe locators.
    - Add a negative fixture for the held 2023 P1 Q9 reference.

**Cheap notes to fold in** (optional; listed in `findings.md`):
- "the first 1 seconds";
- float noise and `\frac{2}{2}`, `\sum_{j=1}^{1}`, `e^{1}`, `-(0)`;
- undefined C and T in single steps;
- "boundary conditions";
- a single 3 s.f. phrasing;
- the "Gradient part:" label;
- the trapezium solution asset also bound to part (d);
- stale "pending" status strings moved out of qualifiers;
- the R-form principal value and rejected candidate shown in the root step.

## Deliverables

1. **Regenerated outputs.** Rerun the group oracles, check_source, notation (Python and KaTeX), verify_candidate, check_ids and check_wording, and the relocated rebuilds. Freeze a new immutable candidate and Stage-E manifest.
2. **`checks/stage-e-repair-e1-report.md`:**
   - each repair with its before and after locator;
   - generated-instance counts affected;
   - a statement, backed by a script, that no tariff, criterion ID, dependency, domain, bound or owner score changed;
   - the rebuild and freeze results;
   - the version decision.
3. **Updated records:** STATUS, HANDOVER and author report.
4. **`authoring/CLAUDE-STAGE-E1-CHECK.md`,** asking Claude for a **diff-only check** of Stage-E → E1. Claude will check:
   - that only the named outputs changed;
   - that the 13 items are fixed in the generated bytes and renders;
   - that no score moved;
   - that the rebuild passes in two relocated copies.

## Constraints

- **No commit or push.** Vitalis commits.
- **Do not modify:** any review folder, the source PDFs, `standard/`, other subjects, app code or pinned checkouts.
- **Scope:** no imports, installation, assignment or publication.
- **Sources:**
  - Textbook originals stay internal.
  - NSSCAS and Cambridge originals appear only with attribution.
  - Cambridge is never labelled Namibian.
  - Held originals are never anchors.
- Only design-blocking or should-fix findings open a repair round; notes carry forward.
