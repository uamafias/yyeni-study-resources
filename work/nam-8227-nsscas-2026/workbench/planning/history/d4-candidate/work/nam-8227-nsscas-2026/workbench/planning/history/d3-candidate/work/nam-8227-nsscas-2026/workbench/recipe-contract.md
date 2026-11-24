# Recipe design contract — NSSCAS Mathematics 8227 pilot

Proposed contract `8227-workbench-design-0.1.3`, 24 November 2026. Owner Vitalis;
PLANNER Codex. **Design for owner approval, not a runtime schema or an approved
resource package.** This extends the existing Workbench playbook/template and
whole-question provider; it does not replace either or create a second framework.

Applicability: the common obligations below are reusable. The bindings in
`subject-rules.md` are specific to NSSCAS Mathematics 8227, NIED December 2020,
Grade 12. Other subjects supply their own curriculum, truth/marking rules and
supporting data; they do not inherit radians, calculator policy or grade bounds.
An eventual Physics pilot must test this separation before shared promotion.

## Authority and record layers

`workbench/playbook/README.md` stage D and `templates.md` govern this plan.
`quality.md` Q01–Q15 and `BLOOM-CLASSIFICATION.md` govern later checking.
Vitalis authorises attributed NSSCAS/Cambridge exam originals in [owner decision N2 item 5](review/opus-5-5-step-1-3/owner-decisions-2026-11-16.md#n2-cambridge-evidence-gap-filling-and-variety), overriding the
generic prohibition on quoting those questions. It does not authorise textbook
originals, source artwork or examiner-report prose for learner display. The pilot
uses newly authored design examples; source evidence stays attributable/internal.

| Layer | Content and owner | Visibility |
|---|---|---|
| Authoring/review | Work orders, sources/hashes, all-member search, rejected leads, scope reasons, grade calibration, review findings; resources | Internal; never a learner payload |
| Runtime definition, later | Versioned recipe/branch, admissible domains, constructive generation, solution/memo, assets, checks; resources | Trusted package, private reference separated from public question |
| Generated question, later | Frozen data, authored stable parts, question text/assets, private canonical answers/criteria, reproducibility/fingerprints; resources, persisted by app | Role- and submission-state projections |
| Safe catalogue | Choice title/grouping, curriculum links, marks, reviewed branch Bloom, response/asset needs, renewal/availability, safe exam references | Teacher picker and approved learner summaries; no answer/criterion content |
| Learner activity | School/classroom/lesson access, deck/assignment, attempts/uploads, timers, grading orchestration, payment and progress; app | App-owned; never generated or assigned by resources |

Source inventories, analysed families and positive textbook relations are inputs,
not runtime recipes. A recipe is a stable assessed pattern. A branch is a change
in reasoning, evidence or connected structure that remains deliberately grouped.
An instance varies the admitted data without changing that branch. A parameter
tuple is not itself an additional recipe or proof of meaningful variation.

## Identity, parts and versioning

Required design identities are `curriculum_id=nam-8227-nsscas-dec2020`, recipe ID,
proposed recipe version `0.1.3`, selection IDs from the accepted analysis, branch ID,
authored part ID and criterion ID. IDs are immutable strings; human display labels
such as `(a)` are separate. A family ID is a selection/evidence link, never an
implicit recipe implementation or an executable path. Display order does not
rename a part or criterion.

Each proposed teacher choice binds one recipe version and one explicit branch.
The plan counts recipes, branch choices and implementation modules separately.
This is a design request: the current application does not establish that this
choice contract is installed. No arbitrary branch is chosen after advertising a
different demand/Bloom/mark range. Saved selections must retain the chosen IDs,
grouping and classification. App-owned progression must continue to credit a
recipe at most once per completed test round; branch evidence does not silently
create additional memory-box credits. `app-change-handoff.md` requires explicit
choice/progress-key tests before implementation acceptance.

Change the version when output, allowed domain, assessed structure, marking,
classification or meaning changes. A renderer-only change also needs its own
version/bound asset identity if it changes saved output. Preserve old question,
memo, asset and label bytes. Alias/retirement rules cannot reinterpret old work.

## Minimum authoring contract

Every work order and its exemplar must resolve the applicable fields below.
Absence means unresolved, not permission to guess. Use `not applicable` with a
reason for irrelevant subject features; do not require a diagram on text-only work.

| Field group | Minimum evidence and rule |
|---|---|
| Identity and selection | Stable recipe/version/branch/choice/part/criterion IDs; owner, planner and status; accepted selection IDs; reuse/extension/new decision |
| Curriculum | Exact syllabus/edition/hash and page; primary and other directly assessed objective/demand IDs **per part**; prerequisites labelled by role; assessment abilities separate from content objectives |
| Learning purpose | Discriminating learner decisions, connected-part boundaries, givens/unknowns, standalone justification, deliberate omissions; no topic-tag coverage |
| Evidence | Exact paper and official award/report locator, matched textbook item/figure locators and scope check, source origin/rights, original/derived award status and defects; page-reading manifest |
| Domain | Explicit finite sets/ranges, dependencies, all exclusions/degeneracies, fixed/variable features, difficulty invariants and grade-descriptor bounds; ordinary variation vs structural branch |
| Response and assets | Numeric/symbolic/proof/sketch/explanation requirements per part, reading requirements, all essential units/labels/relationships, diagram specification where relevant |
| Canonical solution | Answer in required form; action, reason and result for meaningful steps; valid alternative methods; shared givens used by question, solution and marker |
| Memo | Part and total marks; named criteria, dependencies and alternative paths, F.T. conditions, method restrictions, exactness/rounding/units, answer-only evidence, special-case precedence/caps; no double counting |
| Practice and feedback | Answer-free help, a different-instance example policy, reveal after submission, correct/partial/wrong/alternative/ambiguous cases and credit; no invented diagnosis or mastery claim |
| Bloom | Part level, assessed decision and supporting criterion IDs; classification status/version; whole-branch maximum only with all assessed parts classified; never marks-weighted |
| Renewal | Reproducible identity, semantic/visible fingerprints, meaningful capacity with counted equivalences, exclusions, no-repeat scope, reservation/retry and exhaustion policy |
| Checks and review | Independent mathematical oracle, normal/varied/admitted/rejected boundaries, branch test targets, marking examples, render/role tests, outstanding uncertainty, versioned cross-vendor review |

Detailed work orders may reference this common contract for shared mode/identity
rules; their domain, criteria, alternatives, answers and source judgements must
remain specific. Work orders and exemplars are canonical paper design records at
stage D. Later tooling may render derived files from preserved inputs; no competing
manually edited runtime records should be maintained once a builder is authoritative.

## Source search and honest coverage

Use the accepted item-level directly assessed **and component/prerequisite union**
as a discovery aid (R5-03). A union link means inspect the source, not automatically
count it as direct coverage. Search every member of an adopted/compared family for
the best matching response, recording rejected subparts and the reason. Do not
start or stop with the current positive relation list.

Same-type and branch counts are lower bounds (R6-03/R7-05). Roughly one sampled
rejection in five or six was related in the review; the samples do not estimate a
population error rate. Family distinction/precision templates, 403 templated
rejection reasons and damaged extracted notes are not design evidence. Read the
rendered page, including the figure, mathematical conditions and continuation.
Page reading and independent recomputation are distinct checks.

For every one of the 138 demands the plan records selected pilot part/branch links
or a reason for later work. It also lists partial facets and held originals.
`planned direct assessment` is not `implemented coverage`, and neither textbook
support nor an incidental prerequisite earns full examination-demand coverage.
Source-defect holds attach to originals; a valid syllabus demand remains in scope.

## Branch-specific examination references (R2-02)

Each reference retains board, code, year, session (null for NSSCAS), component/
variant, question, part, printed and PDF page, path/hash, relation and verifier.
Generate the display label from these values; do not hand-copy inconsistent labels.
An original reference identifies an attributed original; a newly authored question
is never an original simply because it has the same answer.

For each branch explicitly compare the directly assessed demand set, requested
response, givens and scaffold/dependency structure of the source and the proposed
branch. A demand-set or response mismatch rules out an unqualified whole-branch
`same-type` label. Shared component work may instead have a precisely scoped
part-level relation with its matched part IDs; it must not advertise that the
whole card duplicates the source task. Related references stay internal. Do not
inherit the union of a family's references as branch-level same-type evidence.

Record scope, equality/non-equality and a reason even when no same-type reference
is retained. A syllabus-derived branch may correctly have no learner exam label.
Held originals have `learner_display:false` regardless of their relation. Draft
Cambridge `derived-from` provenance stays internal pending a display decision.

Approved labels include:

- `Same type as NSSCAS Mathematics 8227, 2023 Paper 1, Question 5(b), page 7`
  (format illustration; actual fields/pages come from the checked source record).
- `Cambridge International AS Level Mathematics 9709, Paper 12, May/June 2017, Question 5, page 6`
  for that exact original only.

Source paths, raw excerpts and author/reviewer notes are not needed in learner
labels. A safe teacher review may show objective wording, source locator and why
the branch was selected without leaking the memo into an unsubmitted learner view.

## Diagrams and visual responses (R3-07)

A diagram specification lists **must-read givens** independently of decorative
appearance: labelled point values, endpoints, axis direction/unit, scales,
domain, angle convention, equal/perpendicular marks and shaded-region definition
where relevant. Do not hide an essential given only in alternative text that a
learner would not see. Provide accessible equivalent givens without answering the
assessed reading task.

Separate `fixed`, `variable` and `relations` fields. Build question, solution and
marking geometry from one instance-data record; changing a value must change all
three. A fixed source crop restricts possible instances and cannot be advertised
as renewable. Textbook artwork is not an output asset. Parameterised original
diagrams are a later implementation, not delivered by these paper specifications.

For sketches, mark credited features rather than pixel identity: relevant points,
asymptotes, branches/domain, curvature, scale where required and relationship to
other parts. Tolerance must be in mathematical coordinates or a declared visual
criterion, never arbitrary screenshot pixels. Unreadable/ambiguous uploads need
clarification/pending grading; accepting a photo alone is not assessment proof.

Vitalis's decision 6 includes these demands without capability holds. The app's
announced 17 November support is an owner selection decision, separate from runtime
verification on the selected checkout. These resources must test correct, partial,
alternative, wrong and ambiguous visual responses before release.

## D1 repair authority and marking precedence

The binding 23 November owner decisions OD-1/2/3 in `review/opus-5-5-step-3/owner-decisions-2026-11-23.md` supersede D0 implied-method proposals. For this NSSCAS pilot, apply `subject-rules.md` D1-MR01–09, then the named official per-part exceptions/qualifiers. Bare answers normally earn zero; a correct value still receives supportive practice feedback requesting working. Hence, misread, exactness/rounding, units, multiple attempts, state-or-imply and answer-given proof rules are explicit. These are qualification-specific, not universal rules for other subjects.

D1 keeps the nine-recipe selection. Named branch changes, discrimination checks, exam-original exclusions and per-part semantic/exposure keys repair the proposed design. Raw tuples, unique task contexts, outcome/shape classes and no-repeat capacity are separate counts. A whole task is wholly fresh only when none of its assessed part-instance keys has been exposed; a repeated outcome alone is not an instance key. Partly repeated practice can continue, but is labelled after-feedback and cannot masquerade as wholly fresh testing. Count shape/outcome classes honestly without inventing extra cognitive decisions from numeric rescaling.

Next gate: Claude's D3 changed-scope confirmation **before** Vitalis's plan/count/gap/capability/exemplar approval. This is the owner's OD-3 sequence, not a new approval requirement inferred by the planner. No stage-E resources or activation follow until approval.

## Marks, alternatives and mathematical truth

Official award evidence is an anchor, not an automatic licence to apply the same
tariff after changing the task. Each adapted/new criterion is explicitly proposed and must carry its official qualifiers or a named deviation.
An author may use M/A/B notation but cannot call a derived award official. A
dependency cue such as `hence` is not formal F.T.; formal F.T. needs an award-table
source or a disclosed proposed rule.

Part totals reconcile under each valid alternative path; mutually exclusive
awards are not summed. In reusable cross-subject contracts, declare answer-only
credit from that qualification’s rules; do not infer a universal missing-working
penalty or universal method credit. **For this NSSCAS pilot, OD-1/D1-MR01 controls:
bare answers earn zero except explicit official question-type exceptions.**
An expression containing the credited working can still be evidence; a terminal
formula is not automatically working. A correct alternative method earns
the declared credit unless the question explicitly restricts the method.

Canonical references are private and frozen before an attempt. Feedback can
explain a submitted error but cannot change the canonical result or overwrite the
original work. Retain partial credit already demonstrated, identify only an
evidenced error, and request clarification when evidence is ambiguous. Full-credit
work gets no fabricated repair. Independent checks substitute roots, differentiate
primitives or recalculate geometric/numeric results separately from answer creation.

## Reproducibility, capacity and exhaustion

Later generation identity binds package/recipe/branch/version, deterministic
algorithm version, canonical parameters, seed, curriculum and asset/memo hashes.
Seed is private; save the parameters and full frozen evidence, not only the seed.
Use isolated seeded randomness, constructive domains and bounded failure handling.
Never make generation depend on app state, database, network or current time.

Maintain both a visible-question fingerprint (decoded prompt, parts and bound
assets) and a semantic instance key (canonical mathematical data plus requested
response). Deduplicate equivalent parametrisations; swapped names, whitespace,
alternative algebraic spellings or another seed are not extra practice capacity.
Different answers are neither necessary nor sufficient for distinct questions.
Report finite capacity per branch and repeated-answer collisions separately.

Before a fresh practice/test choice, the app checks the branch/version exclusion
set against saved semantic keys. Reserve a fresh key atomically, make retries
idempotent and retain failed/abandoned reservations according to explicit app
policy. Worked examples and solution reveals count as exposure too. Cross-branch
exposure keys also identify shared underlying givens/assessed subparts (for
example the same implicit curve in gradient and normal branches); adding a part
does not make already revealed working unaided evidence. No-repeat across a
learner's examples, practice and subsequent test is the proposed pilot rule. At exhaustion return `exhausted`, remaining capacity zero, and an honest
message. Repetition or a different branch requires a deliberate new selection;
never silently relabel an old instance as fresh or loop indefinitely.

Design capacity is a mathematical count, not implemented no-repeat behaviour.
The plan's distinct branch capacities must not be summed as unique cross-branch
questions until semantic overlap is checked. Future generation/module counts are
not deduced from recipe or choice counts.

## Practice, test and saved evidence

Preserve the playbook's current learning rules. Practice permits another instance
without a pass first. Help is optional, answer-free for the current unsubmitted
instance; a worked example uses a different instance. Reveal the current canonical
solution, mark and submitted-work feedback after submission. Classify subsequent
helped attempts as after-feedback observations, not wholly unaided evidence.

In Workbench Test, no hint/example/tutor help while an unsubmitted question is being
answered. Preserve question-by-question marking/review, paused marking time,
two-minute nonfinal review and existing advance/expiry/early-finish protections.
The app owns timers, unlocks and once-per-recipe round progress; resources do not
replace those policies. Unreliable marks remain pending and cannot move boxes.

The pre-submit learner projection contains question givens/assets, authored part
IDs, marks and the allowed response shape. It excludes answers, worked steps,
criteria, repair hints, private source text, seeds, future instances and another
learner's data. Post-submit projection is bound to the submitted instance and
frozen original. Teacher access is role-checked separately from learner reveal.

## Existing v1 bridge and required extension

Read-only inspection on 24 November 2026 of app HEAD
`0f0832ddedf40010e467f60184ccf56d63384c09` found the current provider methods
`describe`, `list_recipes`, `generate`, `validate_instance`, `resolve_asset`.
The inspected file hashes and uncommitted-state qualification are in
`planning/stage-d-baseline.json`. These names prove interface presence, not local
website behaviour. `yyeni_workbench_tools/__main__.py` already builds candidates
from `package-definition.json` and `source/`, and expects public descriptors;
it does not consume these Markdown work orders.

| Design meaning | Current v1 bridge | Required verification/change |
|---|---|---|
| Recipe/choice | `recipeId`, `recipeVersion`, public `id` | Bind branch/choice explicitly and preserve grouping/saved labels |
| Part identity | `parts` prompt/marks; projection currently generates letters by index | Preserve authored part IDs and link criteria by ID |
| Truth/marks | `reference_answer`, `worked_steps`, `criteria`, `grading_contract`, `marking_memo` | Lossless memo translation, alternative paths and response/asset evidence |
| Curriculum | `objectiveIds`, `demandIds`, instance `objective_ids` | Preserve part-level direct/prerequisite roles and source traceability |
| Classification | No Bloom fields in catalogue allowlist | Versioned safe metadata extension; do not hide educational fields in title/search text |
| Assets | Prepared assets and question/solution roles | Per-part bindings, must-read givens, sketch/reference/feedback rendering and authorisation |
| Renewal | Visible-content fingerprint | Add semantic-equivalence/no-repeat capacity checks and explicit exhaustion |

The draft framework worktree's shared Bloom-policy changes were inspected. This
repository already carries the fuller approved policy; no draft files were copied
over or edited. The current app and resource CLI allowlists both need coordinated
support for new fields. Do not loosen an allowlist blindly or insert private
evidence into public descriptors. Proposed field examples and acceptance checks
are in `app-change-handoff.md`. Neither CLI structural checks nor a self-written
`approved` flag certify educational correctness or independent acceptance.

## Acceptance and handoff

Stage D ends with Vitalis's explicit approval of this contract, pilot counts,
scope/gaps, flagged capabilities and every exemplar. Approval is currently pending.
After it, stage E may author the agreed definitions and implementations; stage F
must check Q01–Q15 against exact bytes, branches and retained examples. Minimum
later targets are seeds 0, 1, 42 and `2**63-1`, at least 64 valid draws per branch
or exhaustive enumeration if smaller, all admitted/rejected boundaries and
independent correct/partial/wrong/alternative/ambiguous marking cases. Record
untested space. Paper checks now do not claim seeded generation, runtime marking or app-render
tests passed. Static paper-diagram renders and offline syntax checks are recorded
separately.

Cross-vendor review remains mandatory for implemented resources, including every
selection disposition and structural branch. Claude confirms R7 close-out at the
start of the step-3 review; this does not add a separate repair-round gate.
Local website acceptance with real reviewed pilot resources follows, before any
merge/deploy decision. Publishing/installing a package, making choices available
to a school/classroom/lesson, and assigning a deck are separate operations. No
target is selected or import/activation authorised by this plan.


D2 retains OD-1–03 and implements [OD-4/05](review/opus-5-5-d1-short-check/owner-decisions-2026-11-23-d1.md): stationary classification Apply, mixed motion with a live sign-change decision, and the accepted own-curve DB1 extension. Classification version is consistently `8227-pilot-design-0.1.1`; recipe design revisions are0.1.3. The consolidated named adaptation/interpretation/deviation register is in `planning/OWNER-CHECKPOINT.md`. Modulus correct named values and formula entries both earn the official B1 www awards. OD-6 now makes all A/B follow through an eligible unchanged-difficulty question-data misread, with one first-use A/B deduction per datum. M/DM, www, named exclusions and OD-1 still apply. Own-figure/easier/no-solution errors use normal canonical marking.

D3 owner authority: [OD-6](review/opus-5-5-d2-confirm/owner-decisions-2026-11-24-d2.md) binds the genuine question-datum misread rule. Every part carries a misread policy; all A/B follow through when object/difficulty are unchanged, with one eligible earned A/B deduction in the datum's first-use part. Record a per-datum ledger; no double deduction, no borrowing where no A/B is earned. Correct working, supplied-target proofs, named errors and OD-1 remain. Native source and example verification is in `planning/d3/misread-policy-check.json`; the comparable Cambridge convention must never be described as a published Namibian allocation. No other domain changes are authorised.
