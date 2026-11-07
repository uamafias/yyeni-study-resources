# Workbench creation playbook

Version: 1.0 learning/authoring standard, 7 November 2026. Owner: Jeremy.
The learning standard and three walkthrough checkpoints are owner-accepted.
Claude's [closure review](review/closure-2026-11-07/review.md) closed F1–F12 with no
blocking gaps. Its two minor finalisation corrections (status and reviewer-role
clarity) are applied; the [finalisation record](review/finalisation.json) identifies
the reviewed inputs and subsequent edits. This document does not approve
any subject's content, certify learning benefit or validate deployment tooling.

**Start with the workflow in section 5.** Read sections 1–4 once, then follow the
next incomplete stage in the subject's STATUS. Do not build generators before
analysis has selected worthwhile demands and the owner has accepted the plan.

| Companion | Purpose |
|---|---|
| [Templates](templates.md) | Exact output paths, records, start/resume and review prompts |
| [Quality and acceptance](quality.md) | Required checks, findings and review evidence |
| [Factorisation exemplar](exemplars/factorisation.md) | Source-backed question, variation, marking and feedback illustration |
| [Existing behavior to preserve](preservation.md) | Stronger existing feedback, guidance, saved-work and test protections |
| [Guideline sources](guidelines/README.md) | Versioned reference snapshots of Yeni's learner-text authorities |
| [Technical appendix](technical-appendix.md) | Unvalidated package/tool/release targets, kept separate from pedagogy |
| [Review responses](review-response.md) | F1–F12 and O1–O6 corrections, evidence and remaining limits |
| [Consistency walkthrough](validation.md) | Author checks and hypothetical workflow exercises; not independent review |

## 1. Purpose and scope

Give learners quality repetitions on specific numerical, symbolic, geometrical
and structured accounting demands, using fresh questions closely modelled on the
structure and difficulty evidenced in their examinations. Practice helps learners
improve; Workbench Test assesses fresh selected instances with question-by-question
review. Useful feedback connects a submitted attempt to a better next attempt.

Include numerical and symbolic procedures, quantitative graphs, mathematical
constructions/scale work, and structured accounting such as cashbooks, ledgers,
journals and statements. Connected explanation or interpretation stays when needed
for an authentic pattern. Drawing or labelling a recall diagram alone does not
qualify. Judge the assessed work, not the subject name. Every subject can be screened;
zero recipes is a valid evidenced result. No catalogue-size or generator-count target.

A **demand** is the specific learner work within a syllabus objective. A **pattern**
is an evidenced way of assessing it. A **recipe** defines that pattern and its
permitted variants; a **generator** produces valid instances. One objective may
need multiple recipes; several recipes may share a generator. Do not manufacture
extra recipes or engineering from the data format or a desired count.

## 2. Authority, roles and existing work

Read repository [AGENTS](../../AGENTS.md) and the [team playbook](../../TEAM-PLAYBOOK.md).
This is the owner-authorized Workbench-specific companion; it does not change the
notes/flashcard standard under `standard/`. Keep ownership, syllabus-first reading,
source provenance and checkpoint discipline. Notes-specific item quotas, AO-gap
targets and `run_checks.py` publication verdicts are not Workbench acceptance.
Use [quality.md](quality.md); validated automated Workbench tooling is not assumed.

Read exactly one role brief for the active assignment/session:

| Workbench assignment | Role brief | Responsibility |
|---|---|---|
| A–D: source inventory, syllabus, selection, plan | [PLANNER](../../standard/v0.2.0-draft/roles/PLANNER.md) | Own the evidence-to-plan chain; do not auto-delegate to a miner |
| A specifically commissioned corpus-mining assignment | [MINER](../../standard/v0.2.0-draft/roles/MINER.md) | Supply cited evidence to the planner, not a competing plan |
| E–F: author and check | [AUTHOR](../../standard/v0.2.0-draft/roles/AUTHOR.md) | Follow accepted Workbench work orders and scope |
| Selection-only review or G content review | [REVIEWER](../../standard/v0.2.0-draft/roles/REVIEWER.md) | Independently inspect frozen Workbench evidence; don't apply irrelevant static-card quotas |
| H–I: publication/installation | Operator, this playbook and technical appendix | Requires explicit operational authority; not a new content-authoring role |

For Workbench review, REVIEWER.md's published-notes question set, `run_checks.py`,
`operations/review/` YAML and ingestion procedure do not apply. Use this playbook's
[review request](templates.md#review-request) and write to the subject's
`workbench/review/<round>/`; do not let that brief narrow the required selection/content audit.

The **owner** accepts sources, scope/plan and release decisions. Cross-vendor AI
review suffices for **independent content acceptance**: Codex-authored work is
reviewed by Claude and vice versa. Record mixed authorship; someone who authored
affected work cannot independently accept it. Teacher advice is optional, not an
additional required signature. Unresolved subject or marking evidence goes to
Jeremy/Vitalis and stays unresolved for the affected scope until supported.

One subject/workspace per authoring session. Check the tracker before creating
anything; never overwrite another person's work. Reuse verified sources/analysis
by reference only for facts actually present, with matching edition/hashes. Existing
flashcard analysis may lack Workbench patterns, part dependencies and marking rules:
add those locators rather than assume they were checked. Reuse a fitting recipe
before authoring a duplicate. An extension is versioned and re-reviewed; never
mutate published bytes or saved learner snapshots. Future new-question version
selection remains subject to the application compatibility contract.

No agent commit/push by default; the person performs the team-playbook checkpoints.
An explicit active instruction can authorize a scoped commit/push, but this document
does not do so. This is the only permission exception to the team default; never
stage unrelated files. No paid review, external message, deployment, learner
assignment or parallel agent work without the relevant authorization.

## 3. Source documents: exact locations, local first

All paths are relative to **yyeni-study-resources**, not the application checkout.
Record the actual root once in STATUS. This machine uses
`/Users/jeremytiboth/Documents/yyeni-study-resources`.

Consult `operations/SUBJECT-TRACKER.md`, the named subject's STATUS/HANDOVER and
source inventory first. Search scoped paths by subject name/code and qualification:

| Order | Local location | Material |
|---|---|---|
| 1 | `sources/<board>/<level>/<code>-<subject>/syllabus/` and `assessment/<year>/` | Filed syllabuses and assessment sources; inspect actual hierarchy under `sources/cambridge/` or `sources/namibia/` |
| 2 | `Syllabi/Namibian Curricula/NSSCO (New)/`, `NSSCAS/`, `JSC (New)/`, `SP Grade 4-7 Namibia/` | Namibian syllabus; verify cover/code/edition |
| 3 | `Question Banks/Namibian Curricula/<qualification>/<actual-subject-folder>/<year>/` | Papers and matching schemes; actual Maths folder, for example, is `NSSCO (New)/Mathematics/` |
| 4 | `Question Banks/Namibian Examiner Reports/` and reports beside relevant papers | Reports, including subject sections in combined PDFs |
| 5 | `_harvest/manifests/`, `_harvest/logs/`, `_harvest/reports/` | Existing download destinations, missing/failed acquisitions and verification records |

Record exact resolved filenames, SHA-256, edition, year/series, question/page and
document relationship. Detect LFS pointers before claiming PDF contents exist.
Use the current syllabus first. The team source baseline is the last **3–6 years
on the current syllabus**, matching schemes where available, reports and specimens
when no papers exist. Inventory relevant local holdings; document the actual corpus,
missing pairs, older-edition exclusions and justified additions. Do not count duplicates.

Do not start with web search. If local material is missing, check alternate filenames,
combined reports and acquisition records; flag exact gaps and educational impact
to Jeremy/Vitalis. They supply documents or authorize targeted acquisition using
the existing YYeni Web Harvester. No new scraping scripts, speculative broad web
searches or agent writes to official source directories. Notes/generated banks
are references, not substitutes for official evidence. No quarantine/legacy source
is silently promoted into current authority.

## 4. Holds and escalation

Selection disposition is **include / exclude / hold**. A hold always has an ID and
one or more explicit reason codes; split actions if several causes apply.

| Reason | Trigger | Durable record and recipient | Condition for reconsideration |
|---|---|---|---|
| capability | Required learner input, representation or marking is unsupported or not verified | `capability-gaps.md`; explicitly flag to Jeremy or Vitalis as capability needed | Owner disposition recorded, capability delivered or suitable alternative demonstrated, then validated |
| source | Missing, conflicting or unusable official evidence prevents the proposed claim | `analysis/source-inventory.md` gaps; flag to Jeremy or Vitalis | Source supplied/verified, claim narrowed or a disclosed limitation explicitly resolved |
| scope | Unsettled relevance, syllabus interpretation or proposed marking judgement | `analysis/selection-table.md` decision log; subject owner, escalating to Jeremy/Vitalis as needed | Dated scope/rule decision and supporting evidence |

An authored version's **held (withdrawn pending repair)** state is different:
record the defect in its review findings, exclude it from new assignments, preserve
old evidence, repair/version/check/re-review before re-enabling. Link any associated
selection hold instead of treating repair as a capability request.

Capability records must say **Capability evidence checked**: dated document/code/test
locators and what they prove. Start with [preservation.md](preservation.md), the
selected Yeni revision's `docs/features/workout-bench.md`, and relevant router/UI
response/asset/marking support. Text or photo upload alone does not prove cashbook
cell-level marking or construction accuracy. If verification is unavailable, record
an investigation gap rather than invent support or assert an implementation defect.

Flag capability gaps in the current report AND STATUS with IDs, recipient/date,
acknowledgement/disposition and next owner/action. A handoff for Vitalis shown to
Jeremy is recorded as such, never as delivery to Vitalis. Group related gaps to
avoid notification spam. Open-gap notification evidence is required before asking
for **analysis read** or **plan approved**; the owner may acknowledge a pending
decision, which does not resolve it. A missing record blocks that checkpoint.

Record build/investigate/defer/alternative decisions. Build approval is not delivered
capability, and a deferred requirement remains a visible gap. Continue independent
work; do not quietly remove the demand, substitute a weaker skill or start substantial
engineering just because a capability is needed.

## 5. Workflow: inputs, actions, outputs and checkpoints

Use the exact paths and minimal record shapes in [templates.md](templates.md).
Human checkpoint answers are recorded with name/date; silence is not acceptance.
Existing authorization persists. Resume from the first incomplete evidenced step,
never recreate another session's curriculum or frozen reviews.

### A. Establish ownership and source inventory

**Input:** subject/code/qualification/years and named owner/workspace.
Check tracker and pilot rules, reuse the existing workspace, inventory section 3
sources and record limitations. No new source collection if the documents exist.
**Output:** `analysis/source-inventory.md`, STATUS.
**Owner checkpoint:** sources complete for the named scope; disclose missing items.
Current syllabus absent: stop source-dependent authoring, continue only independent work.

### B. Read the syllabus and screen demands

**Input:** accepted source inventory. Read the syllabus itself before papers.
Verify AOs/weights/paper structure/command words and exclusions; use “not stated”
where appropriate. Reuse verified `curriculum/` facts without overwriting them.
Build `analysis/demand-registry.md` with clause/method/representation locators,
direct vs prerequisite roles and the in-scope screen. Lists in one syllabus bullet
may represent several demands. Group clearly excluded ranges with exact coverage
locators and a shared reason; no need to generate hundreds of irrelevant IDs.
**Owner checkpoint:** syllabus facts/tables checked against the cited pages.

### C. Analyse examination patterns and choose Workbench scope

**Input:** syllabus screen, relevant papers, schemes and reports.
Record question structure, command, representation, methods, marks, connected
parts, alternatives, dependencies, follow-through, units/precision and evidenced
difficulties. Distinguish syllabus facts, corpus observations and proposed judgements.
Record paper AND marking locator per pattern, or “none available” with impact.

Complete `analysis/selection-table.md` before PLAN. Every in-scope demand and
observed pattern gets a disposition; grouped exclusions account for the rest of
the syllabus screen. Tags/subject titles alone never establish coverage.

- Separate recipes require a meaningful difference in reasoning, method,
  representation or part structure. State the discriminating learner decision,
  plus a concrete response/behavior showing why credit, feedback or required
  evidence differs. For representation changes, state what its response format
  uniquely demonstrates. Cosmetic name/context/number changes stay within a recipe.
- Keep connected multipart patterns. A standalone version needs a separately
  evidenced practice need and all required givens; never split all subparts by default.
- Supporting drills need a cited prerequisite dependency or evidenced learner
  difficulty, an explanation of why existing recipes are insufficient, and owner
  acceptance. No automatic drill bank. Supporting-only links do not earn direct
  coverage of the larger exam demand; credit a prerequisite objective only if
  explicitly selected and directly assessed in its own right.
- Unobserved syllabus candidates remain visible. If included, label them
  **syllabus-derived, not examination-evidenced**; marking/structure are proposed,
  need owner acceptance and independent review. Never advertise them as observed
  exam patterns or guarantee what an examination will contain.
- Declared variation preserves intended decisions and corpus-calibrated numerical,
  geometric/data-size difficulty bounds. Method/difficulty changes need a reviewed
  branch or recipe, not an unnoticed random shift.

**Outputs:** selection table, relevant subject rules/answer shapes and evidence
locators; capability/source/scope records where needed.
**Owner checkpoint:** analysis read, after all capability gaps are explicitly flagged
and recorded. Independent review of the selection is required at G, including exclusions.

### C0. Lightweight zero-recipe outcome

If the whole syllabus screen identifies no qualifying demands, record a short
`analysis/zero-recipe-record.md`: syllabus ranges screened, grouped exclusion reasons,
relevant-paper scan and limits, source inventory, proposed conclusion and owner
confirmation. Scan question structures across the inventoried relevant corpus
for possible in-scope exceptions; detailed mining/mark-rule extraction is needed
only if a candidate appears. Any sampling must declare unscanned space and cannot
justify an unqualified zero result where there is a credible uncovered calculation
demand. For no-papers subjects, screen official assessment/specimens; if absent,
label the conclusion syllabus-only and its limitation. Never invent papers.

A selected demand blocked by capability is NOT a zero-recipe exclusion. Perform
a light cross-vendor selection review at G: verify every grouped exclusion and
the absence of silently held demands. If a candidate is found, reopen C. Otherwise
record owner confirmation and independent selection acceptance, then end the
content workflow. Skip D–F, subject rules/misconception registers not needed to
justify the decision, and H–I: no empty provider, generator or release package.
This route is available to any subject, including History; subject name is no evidence.

### D. Plan and specify the smallest justified recipe set

**Input:** accepted C selections. PLAN maps included selection IDs to existing/new
recipes, priorities and explicit omissions. Reuse, extend with version/re-review,
or author new only with demand-based reasons. Count choices/recipes/generators
separately; there is no one-to-one quota. Held selections remain outside authoring
until their specific conditions are resolved.

For each recipe write a work order using the template: purpose/prerequisites,
source/part links, branch/parameter domains, difficulty invariants, capacity,
question/response assets, solution, marking and answer-only rules, supported
alternatives, sample responses/feedback, practice/test reveal rules, checks and
remaining uncertainty. Show a normal, varied and boundary instance with solutions.
The exemplar can be paper-based; design approval does not require new tooling.
Preserve canonical inputs for later reproducible derived files, never competing
manually edited outputs after a generator becomes authoritative.
**Owner checkpoint:** plan approved, including counts, gaps, flagged capabilities
and exemplar. No “approved” status inferred from an AI's confidence.

### E. Author and generate compliant instances

**Input:** approved work order and current guideline references. Write the question,
solution and memo together. Apply Yeni's [learner-text guidelines](guidelines/README.md)
at template authoring AND each instance's generation, including hints, example text,
table/diagram labels and later feedback. AI prompts reuse the shared instruction
through the approved authoring interface; deterministic generation emits compliant
Markdown/LaTeX directly. Inspect decoded output and actual rendering; cleanup is
defensive handling, not the first application of the standard.

Generate constructively with isolated seeded randomness; bounded rejection and
finite exhaustion must be explicit. Verify domain/feasibility, alternatives and
all parts against the same givens. Derive diagrams from declared data/geometry;
preserve physical calibration where needed, never require measuring an arbitrary
screen. Freeze branch/boundary examples with versions, seed and fingerprints.
No app/database/network calls in subject generator code.

**Output:** recipe/generator or justified shared generator, solutions/memo/assets,
frozen examples, independent recomputation checks, provenance and deviations.
Version output-affecting changes. Deviation affecting demand/scope returns to C/D.

### F. Check, repair and freeze

Follow [quality.md](quality.md), not the static-flashcard publication verdict.
Use verified tools where available; otherwise record the actual manual inspection
and applicable unrun automated requirements. Do not claim a tool exists or passed
because a target command appears in the [technical appendix](technical-appendix.md).

Fix authoritative source, regenerate dependents, rerun affected checks then the
agreed full scope. After three failed attempts at the same check, record the
failure, attempted repairs and needed owner; continue unrelated work without
weakening the standard. Applicable missing checks block affected release scope;
non-applicability requires rationale and independent acceptance, never a fake pass.
Freeze a candidate with file hashes, selections, exclusions, gap decisions, code,
fixtures, author reports, payload/render samples and known findings.

### G. Independent selection/content review

Use the exact [review request](templates.md#review-request) and finding ledger.
Cross-vendor reviewer audits EVERY disposition against source locators, including
observed-vs-syllabus-derived labels, exclusions, zero outcomes, capability records,
recipe distinctions and chosen multipart boundaries. For nonzero content inspect
each structural branch, marking/answer-only/alternatives, truth/domain, variation,
feedback and both mode/presentation contracts. Independent oracles must not just
call the generator's answer function. Disclose sampled and unchecked space.

Reviewer may reject the plan; do not repair coverage by retagging. Author repairs,
versions and freezes a new candidate. Preserve previous review evidence; rerun and
independently re-review changed scope/dependencies. Acceptance names exact bytes,
scope and findings, with no open blockers. Cosmetic-only deferrals need reason,
owner and reviewer acceptance. Author-verified is not independently accepted.
**Owner checkpoint:** verdict read and proposed release scope accepted. No paid
review is started without explicit authorization.

### H–I. Publish and select a resource release, separately authorized

Only accepted content goes to immutable releases with exact dependency/file pins,
computed counts and a reviewed enabled subset. Actual packaging/CI/installation
and rollback procedures are UNVALIDATED in this review candidate: use the
[technical appendix](technical-appendix.md) as an engineering target, not an
operating runbook. Verify a later implemented procedure before any activation.
Resources owns subject content; Yeni owns permissions, persistence, grading
orchestration, UI and authorized curriculum mappings. No copying new subject
generators/content into app source. Publication is not deployment or assignment.

Preserve original questions/memos/attempts/assets across version changes and
retirement. Fresh assignment/version behavior must be explicit and tested; do
not claim the current implementation already pins all future questions per deck.
Deleting material requires ownership/usage evidence and Jeremy's existing
author/committer restriction; preserve unknown authorship and frozen reviews.

## 6. Learner experiences and completion

| Stage | Practice | Workbench Test |
|---|---|---|
| Answer | Unaided attempt distinguishable from optional answer-free support and a different-instance example | Fresh assigned counts; no hints/examples/tutor while answering an unsubmitted question |
| Submit/review | Current solution, specific feedback and repair steps only after submission | Mark each question, pause answering time for marking, then existing feedback/solution/tutor review |
| Continue | Another instance of the current permitted recipe without a pass first; honest finite capacity | Existing two-minute nonfinal review, early advance, final-question/expiry/early-finish rules remain |
| Progress | Correct answer unlocks next card; every recipe correct unlocks test; practice never moves boxes | Completed reliable test results update boxes once per recipe per round; unreliable marks remain pending |

Record later same-recipe test instances following earlier feedback as after-feedback
observations, not wholly unaided evidence. The final answer is the frozen canonical
reference, never the AI repair's result. Support and correction do not overwrite
original attempts. Keep existing recovery, concurrent-request and uploaded-answer
protections in [preservation.md](preservation.md).

Feedback recognises real progress, addresses the first supported consequential
problem and gives usable action/reason/result repairs without duplicating a full
solution everywhere. Correct work gets no invented repair. A wrong final answer
alone does not establish a misconception; unclear evidence needs clarification.
Marks follow the recipe memo, not number of teaching steps or a universal
no-working policy. Preserve valid alternatives and explicit follow-through rules.

Completion has separate records: owner-accepted design; author checks;
independent selection/content acceptance; published release; named-environment
activation. None implies another. A fresh first-attempt correct response without
optional support is one independent observation, not proof of mastery or measured
learning benefit. This playbook does not authorize a classroom effectiveness study.
