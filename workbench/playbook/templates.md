# Workbench paths and record templates

Read the [workflow](README.md) and [quality contract](quality.md). These are
minimal human-readable authoring records, not a claim that the draft CLI accepts
these Markdown files directly. No new schema/tool implementation is authorized.
Keep real facts out of placeholder examples; unfilled required fields are not passes.

## Exact paths

All outputs are under the named subject's existing `work/<workspace>/workbench/`.
Call this directory WB in the tables below. Reference existing verified curriculum
files and source PDFs instead of copying them. Existing legacy subject file layouts
remain intact; put new records here without silently relocating their runtime package.
WB `STATUS.md` is separate from `work/<workspace>/STATUS.md`, which tracks the
overall subject under the team playbook; link the two rather than overwrite it.
If no workspace exists, confirm its tracker claim/ownership first, then create it
using TEAM-PLAYBOOK.md section 6 naming. Do not invent another folder for an existing subject.

| Output | Exact WB-relative path | Stage |
|---|---|---|
| Current progress, notifications, checkpoints | `STATUS.md` | All |
| Resume instructions and risks | `HANDOVER.md` | All |
| Source inventory and acquisition gaps | `analysis/source-inventory.md` | A |
| Demand screen/links to verified curriculum | `analysis/demand-registry.md` | B |
| Corpus findings and pattern/marking locators | `analysis/corpus-analysis.md` | C |
| Include/exclude/hold decisions, scope log | `analysis/selection-table.md` | C |
| Zero-recipe evidence and selection review | `analysis/zero-recipe-record.md` | C0/G only if applicable |
| Capability evidence and escalation | `capability-gaps.md` | C onward only if applicable |
| Subject authoring plan | `PLAN.md` | D |
| Work order for a selected recipe | `work-orders/<recipe-id>.md` | D |
| Complete design exemplar | `exemplars/<recipe-id>.md` | D |
| Relevant rules/glossary/answer-shape evidence | `subject-rules.md` | C/D, only if needed |
| Author checks, limitations and deviations | `checks/author-report.md` | F |
| Frozen review snapshot index, source hashes and scope | `review/<round>/inputs.json` | G |
| Reviewer report and finding ledger | `review/<round>/report.md`, `review/<round>/findings.md` | G |
| Later revised immutable release | `releases/<version>/` | H, only after operational validation |

Recipe/generator/assets/fixture machine layouts belong to the separate provider
contract. Do not invent executable paths in the selection table. Every record
names subject/code/qualification/edition, owner, date and scope. Counts are computed
from the authoritative selections/definitions when tools are validated; the design
record does not need an installed generator to be owner-accepted.

## STATUS

```text
Subject/code/qualification/edition:
Owner; WB path; resources root; app checkout/revision if consulted:
Authoring tool/revision; guideline snapshot/revision:
Current stage; exact next action:
Sources complete: pending | owner/date + inventory reference
Syllabus facts checked: pending | owner/date + pages
Capability evidence checked: dated feature/code/test references, or not yet verified
Capability gaps flagged to Jeremy/Vitalis: IDs, actual recipient, date, report reference
Acknowledgement/disposition: pending | owner/date/decision + next action
Other holds: IDs/reasons + records/recipient/date
Analysis read: pending | owner/date + selection snapshot
Plan approved: pending | owner/date + scope, counts, exemplar
Author checks: not-run | fail | pass, report and limitations
Independent selection/content review: not-run | repair | accepted-scope, frozen input/report
Owner verdict read: pending | owner/date
Published resource release: not-done | version/revision
Activated environment: not-done | independently authorized deployment record
Do not overwrite:
```

If capability holds exist and the **flagged** line is blank, do not request or
record Analysis read/Plan approved. A pending disposition is allowed only after
the owner has been informed; it does not count as a resolved gap. If no gaps
were identified, write “none identified” plus the evidence checked, not a fake notification.
Human answers are never backfilled from silence. A record of a handoff to Jeremy
for Vitalis is not proof that Vitalis received it.

## Source inventory and demand screen

Source inventory columns: document ID, exact repository-relative path, hash,
code/edition/year/series, type, relevant pages, paper↔scheme/report pairing,
final/proof status, usable bytes/LFS status, used/excluded and reason.
Also list missing documents with locations searched, gap ID, scope impact,
recipient/date, decision and resolution evidence. State the actual corpus window.

Demand-registry columns: stable demand ID OR grouped excluded range, syllabus
locator/wording reference, learner action, in-scope/out-of-scope/uncertain screen,
direct/prerequisite/context role, source-vs-judgement label, related existing ID.
Grouped exclusions name exact ranges and one shared reason; check that no clause
between ranges disappears. Absence of an ID is not an exclusion decision.

## Selection table

| Selection ID / demand links | Pattern and paper locator | Marking/report locator | Required reasoning, representation, connected parts | Disposition / hold ID | Recipe grouping, distinguishing decision and evidence | Basis, rationale and limits |
|---|---|---|---|---|---|---|
| Placeholder only: replace before acceptance | Exact question/part/page, or none available | Exact criteria/report page, or none available with impact | Actual learner work, not a topic tag | include / exclude / hold + reason | Existing/new/standalone/shared; concrete discriminating response or format | observed / syllabus-derived / supporting; owner decisions and gaps |

For every separate-recipe or supporting-drill proposal, record the need and why
existing recipes are insufficient. A representation-specific response may be
different evidence even if its final number matches. For an unobserved included
candidate use “syllabus-derived, not examination-evidenced”, proposed marking and
owner acceptance. Reviewers check these claims against sources. Include capability
IDs and distinguish proposed from implemented support. Amend selections before PLAN
if authoring exposes an error; keep a dated decision log.

## Hold and capability records

```text
Gap ID / reason: capability | source | scope
Subject, selection IDs, demand/pattern/source locators:
Required learner action and educational purpose:
What is missing/uncertain; affected coverage:
Capability evidence checked: date, app revision, feature/code/test locators and result
Potential existing capability/reuse; verification limitation:
Smallest proposed capability/investigation (not implementation approval):
Flagged to Jeremy or Vitalis: actual recipient/date/session report reference
Acknowledgement/disposition: pending | build / investigate / defer / alternative
Decision owner/date/reason:
Next action/owner; conditions for reconsideration:
Delivered/validated evidence, or still held:
```

Use capability-gaps.md for capability records. Source records belong in the source
inventory, scope records in the selection decision log. A defective existing
recipe instead gets a finding/version/withdrawn-pending-repair record in review.
Link multiple causes rather than hide one behind another. Notification is a durable
fact recorded in STATUS, not merely an intended future action.

## Zero-recipe record

```text
Scope: subject/code/edition; exact syllabus and corpus references
Syllabus ranges screened: every section accounted for; grouped exclusions allowed
Relevant paper/specimen scan: documents/sections, possible exceptions, unscanned limits
No-papers case: official assessment screened; unavailable evidence explicitly stated
Selection/exclusion table reference; no unaccounted qualifying held demand
Conclusion and limits: zero qualifying demands, not zero implemented generators
Owner confirmation: pending | name/date/input reference
Independent cross-vendor selection review: pending | reviewer/input digest/report/verdict
Next: end after accepted selection; otherwise reopen C for any qualifying demand
```

No need for PLAN, work orders, subject-rule/misconception registers, providers or
releases if they add nothing to the zero conclusion. No real subject can be declared
zero by filling this template with a subject name and no evidence.

## Recipe work order and exemplar

```text
Recipe ID/proposed version; included selection IDs; author/owner:
Reuse decision: existing recipe | versioned extension | new; justification
Independent learner target; prerequisites and out-of-scope work:
Syllabus, paper, marking and report locators; evidence labels/limitations:
Pattern and connected parts; standalone justification if applicable:
Question/response structure, values supplied, assets and calibration:
Branches and domains: permitted changes, exclusions, difficulty evidence/bounds
Capacity/fingerprint/no-repeat scope; safe exhaustion:
Canonical answers and action/reason/result solutions; valid alternative methods:
Marking: part totals, individual awards, dependencies, method restrictions,
  follow-through, units, exactness/precision, intermediate rounding, special cases
Answer-only rule: exactly which awards a final answer alone can demonstrate,
  which need visible method, and source evidence or proposed justification
No double credit: precedence/caps for overlapping alternative/special awards
Practice support vs current solution; agreed test feedback/review timing:
Sample correct/partial/alternative/wrong/ambiguous submissions and feedback:
Unaided fresh-attempt observation vs correction/support; no automatic mastery claim:
Exemplar: normal + changed + admitted boundary cases with checked solutions;
  rejected cases with explicit reasons; proposed vs source-calibrated bounds
Guideline revision and raw-text/render checks from generation onward:
Truth oracle separate from generator's answer function; branch/seed test matrix:
Held capabilities, uncertainties, required reviewer decisions:
```

A numerical answer might not demonstrate a method, while a fully factorised
expression can encode the whole requested result. Decide from each memo; do not
copy a universal no-working penalty or universal full-credit policy.

## Finding and author-report records

Each finding: ID/round, scope, recipe/version/branch/seed (or explicit N/A), severity,
blocking flag, exact source/contract basis, expected/actual, reproducible evidence,
repair owner/revision, status, author validation, independent acceptance and any
accepted deferral. States: open → fixing → author-verified → awaiting-review → accepted;
deferred needs reviewer acceptance and reason. Never close your own independent finding.

Author report: applicable [Q01–Q15](quality.md), result per gate (pass/fail/not-run/
not-applicable), exact input/tool versions, commands or manual method, branch/seed
scope, output paths/hashes, limitations and remaining blockers. Selection-only
review records Q02 and relevant source/exclusion gates; it never invents content tests.

## Start or resume prompt

```text
Work on <subject, code, qualification, edition>, owner <name>, existing workspace <path>.
Read AGENTS.md, TEAM-PLAYBOOK.md and workbench/playbook/README.md. Your role is
<planner/author/reviewer>; read exactly that role brief. Follow the Workbench-specific
workflow and quality contract, not static-card quotas. Read this subject's STATUS,
HANDOVER and referenced evidence only. State what the files prove and the next
incomplete stage. Check official local source locations before any web search.
Keep analysis selections ahead of planning; flag capability holds to Jeremy/Vitalis
and record notification. Preserve existing content/history and other owners' files.
No implementation expansion, paid review, messages, commits, pushes or deployment
unless already explicitly authorized. Continue approved independent work; record
blocked scope rather than invent evidence or weaken checks.
```

## Review request

```text
Independently review <subject/code/edition, frozen input digest, scope> against
workbench/playbook/README.md and quality.md. This is <selection-only / content> review.
Read every include/exclude/hold decision, grouped exclusion, zero-recipe record,
observed-vs-syllabus-derived label and capability escalation against source locators.
Check that no demand disappears, no unsupported observed-pattern claim is made,
and no held capability is disguised as an exclusion or supported feature. Test recipe
distinctions, standalone/multipart choices and supporting-drill justifications.
For content, inspect every structural branch and its relevant subject rules,
answer-only/alternative/partial-credit criteria, truth/domain/variation, no-repeat
capacity, complete solutions and sample feedback. Verify generation-time learner
text, copied-wording checks, both mode reveal rules and preserved saved evidence.
State exact sources/pages/code read, tests actually run, numerical space sampled
and what remains unchecked. Author checks and owner ticks are not independent proof.
Return finding IDs, severity, exact scope/branch/seed/locator, expected/actual,
minimal correction and verification. Verdict: accept named scope, repair, or fix plan.
Do not edit frozen input, broaden scope, delegate, claim all seeds checked from samples,
or infer whole-subject approval from a pilot. Escalate unresolved marking questions
to Jeremy/Vitalis. Cross-vendor review suffices; no mandatory teacher sign-off.
```
