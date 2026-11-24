# Subject binding — NSSCAS Mathematics 8227

Proposed stage-D binding, 23 November 2026. Owner Vitalis; PLANNER Codex.
Qualification: NSSCAS Mathematics 8227, Grade 12, NIED December 2020, first
examination 2021. This binds `recipe-contract.md` to the existing curriculum;
it does not edit or replace that accepted analysis.

## Assessment authority

Source: `Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf`,
SHA256 `c53e77d60f8de1410163c4fccbfa1c41ae88479fb9a53e2bd26ef1bcc727fb30`.
The planner reread content PDF pp7–16, assessment pp17–18 and grade descriptors
pp19–24; pp17–18 were also inspected as rendered pages. Exact assessed content
and source identity remain in `curriculum/objective_registry.json`,
`syllabus-facts.json`, `syllabus-exclusions.json` and `grade-descriptions.json`.
Root-native render hashes are recorded in `planning/planner-source-reads.json`.

There is one assessment area, **technique with application**, with eleven
abilities (`8227:2020:ABILITY:01`–`11`), not eleven separately weighted AOs.
Any may be assessed on either paper (PDF17/printed14). Both papers are compulsory,
75 marks, 120 minutes and 50% each, without choice (PDF18/printed15). No separate
per-ability weights or standalone command-word table are stated. Do not invent
AO percentage quotas or import the static-card subtype mix. A pilot deck is not
a 75-mark examination paper and does not certify qualification AO balance.

Mathematics 1 and 2 are content themes, not exclusive paper boundaries. The
assessment-conditions register documents cross-theme demands on Paper 2 and
year-specific formula provision. Use the selected year's exact support policy;
MF9 is notation/formula support, not extra assessed scope. For later pilot tests
the proposed default is the reduced 2023–2025 formula support, with the chosen
formula contents frozen and shown before the attempt. Do not offer additional
formula help during a test or turn practice hints into test support.

## Accuracy, units and methods

The syllabus permits a non-programmable scientific calculator. Unless an exact
answer or other precision is specified, non-exact answers use three significant
figures; answers in degrees use one decimal place. Use calculator pi or 3.142
(PDF18/printed15). Keep guard digits during calculations. Exact surds, fractions
and multiples of pi remain exact where requested. Radian calculus and radian
integrals must not accept the rejected 2023 P2 Q7(c) degree-mode anomaly.

Question/criterion restrictions outrank generic advice. `show`, `hence`, `using
logarithms`, diagram consistency and explicit exactness requirements are assessed
only as stated by the task and memo. A single-question examiner comment is not a
universal prohibition. Trace source conventions through `analysis/marking-conventions.json`:
119 question tables, 821 criterion rows including exclusive alternatives; 818
official rows and three explicit derived completions. Two missing part breakdowns
and a missing alternative-path end remain disclosed. New/adapted pilot criteria
are proposed, even when aligned to official method/accuracy evidence.

NSSCO algebra/geometry may be required prerequisites. Record their role, but do
not count prerequisite manipulation as direct coverage of an AS objective unless
the task and criteria explicitly assess that AS demand. Content objectives,
assessment abilities, Bloom, difficulty, marks and memory-box state remain distinct.

## Scope boundaries

The complete accepted limits/qualifiers stay in `curriculum/syllabus-exclusions.json`.
Work orders apply them using actual admitted values, not a boilerplate checklist.

| Binding | Consequence for this pilot and later expansion |
|---|---|
| LIMIT02 / QUAL03 | Trig equations use specified finite intervals and small integer/simple fractional arguments; no unbounded general-solution bank |
| LIMIT03 / LIMIT04 | No required first-principles differentiation; product/quotient rules are Mathematics 2 content, not assumed Mathematics 1 methods |
| LIMIT05 | Polynomial division dividends at most degree4, divisors linear/quadratic; omitted from this pilot rather than silently covered by calculus |
| LIMIT06 | Change of logarithm base excluded; linearisation uses log laws in a fixed base. The reciprocal-log equation is not a pilot exemplar |
| LIMIT07 | Reverse differentiation of admitted forms, not compulsory general substitution; no integration-by-parts expansion |
| LIMIT08 | Numerical root finding may expose failure to converge but not require formal convergence criteria; numerical iteration remains later scope |
| QUAL01 | Modulus graph coefficients are integers. A fractional-coefficient textbook exercise cannot define the pilot domain |
| QUAL04 / QUAL05 | Only simple prescribed improper integrals; rational power n≠−1 in Mathematics 1, reciprocal-linear log primitive belongs to Mathematics 2 |
| QUAL06 | Volumes revolve about a coordinate axis; volumes remain later scope, not covered by distance integration |
| QUAL07 / QUAL08 / QUAL09 | Simple domain/range and one-to-one inverse restrictions matter; line tangency/repeated-root correspondence is specific, not every normal/tangent task |
| QUAL10 / QUAL11 | Rational power derivatives permitted; sketch-based trapezium bias accepts geometric chord reasoning and does not require a formal second-derivative test |
| LIMIT01 / QUAL02 | Positive-integer binomial expansion excludes greatest-term/coefficient-property demands and rational infinite expansions; sequences/series remain explicit later scope |

Grade a/c/e descriptions calibrate variation and do not create new objectives
(PDF19). Link each branch's easy and hard cases to the recorded descriptor IDs;
label finite numerical choices as planner-chosen bounded design choices. No claim
that a number size, mark total or Bloom label automatically equals a school grade.
The pilot's easiest branches stay within applicable e/c descriptions and its
hardest no further than grade a. Corpus examples and native source reading support
the chosen learner decisions; release must verify actual varied/boundary instances.

## Source and rights decisions

Preserve source defects and owner decisions in `analysis/source-defects.json`
and the immutable review folders. The held 2022 P1 Q13, 2023 P1 Q1(b) and 2023
P1 Q9 originals cannot become learner-facing originals or same-type anchors.
Valid demands remain in scope. A universal quadratic proof must state a≠0;
the principal-value inverse demand is taught correctly from valid sources.

Textbook items/figures are internal ingredients with `learner_display:false`.
Their reported answers are checked evidence, not unquestioned truth. Create
original diagrams and learner wording from the mathematics. Attributed NSSCAS
and Cambridge exam originals are authorised by Vitalis; no Cambridge source is
presented as a Namibian original. Per-branch source equality and learner labels
follow `recipe-contract.md`; `related` and draft `derived-from` references stay internal.

## Learning text and feedback

Use the existing guideline snapshots indexed by
`workbench/playbook/guidelines/provenance.json` (7 November 2026, file digests pinned
in the planning manifest). Those were local app snapshots, not proof of deployed
bytes. No forked shared AI instruction is added. Use British spelling, clear
English, decoded Markdown/LaTeX, separate equations and correct mathematical units.
Never put mathematical notation inside emphasis or expose provider/internal keys
as learner copy. Render all later question, help, solution, feedback and history
surfaces; a tolerant formatter does not establish authoring compliance.

Feedback recognises demonstrated work, names the first evidenced error and offers
an action/reason/result repair. It distinguishes an ambiguous upload from a wrong
answer, and the app retains the original attempt. No invented misconception is
labelled examiner-evidenced. Solutions/support and ordinary practice do not move
memory boxes; the application owns reliable completed-test progress.

## Current status

These are proposed subject rules for the stage-D owner checkpoint. The accepted
analysis proves source-level mapping and review, not implemented recipes, Bloom
approval, generator correctness, visual marking or local website acceptance.
The next stage is owner approval of the plan, counts, gaps, capabilities and
exemplars. Stage E does not begin from silence or from passing document checks.
