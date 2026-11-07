# Existing Workbench behavior to preserve

This checklist was derived from local Yeni code inspected on 7 November 2026.
It is evidence of implemented rules, not a fresh end-to-end test or a production
deployment claim. A subsequent operator must check the selected app revision.
The feature record and runtime paths below belong to the Yeni repository.

| Behavior | Existing evidence | Authoring/implementation obligation |
|---|---|---|
| Specific feedback and repair structure | `services/api/services/math_workbench/feedback_contract.py`, `system_prompt`, `validate_steps` | Preserve recognition of real progress, first evidenced error, action/reason/result repairs, alternatives and no fabricated misconception |
| No repair for correct work; unresolved evidence treated separately | Same validation and review payload paths | Do not invent corrective steps from a score; request clarification rather than pretend ambiguity is reliable marking |
| Canonical final answer separate from generated repairs | `apps/web/components/MathsWorkbench/Content.js`, `ExamAnswer` | The final answer is the frozen recipe reference, never an AI repair's result |
| Contextual tutoring | `services/api/routers/maths_workbench.py`, `message`; `guidance.py` displayed-example resolution | Preserve actual-working, relevant earlier-attempt and server-resolved example/step context; direct/Socratic modes; no claimed mark changes |
| Same-instance binding and renewal | Router `renew`, `ensure_practice_example`; platform runtime `fresh_question` | Keep solution/example identity separate; fresh practice instances remain the same intended demand with repeat controls |
| Original saved answer and retry protection | Router `answer`, learner locking and submission claim handling | Retry marking the same saved submission after failure, reject changed-answer replacement and stale positions, avoid duplicate/conflicting writes |
| Test timing/review | Router answer/advance/start and `services/math_workbench/timing.py` | Server budget, marking pause, two-minute nonfinal review, early advance, final-question behavior, early finish/expiry and active-test restrictions |
| Progress/reporting | `services/api/services/math_workbench/reporting.py` | Practice never moves boxes; completed test once per recipe/round; reliable marks only; distinguish unmarked, unanswered and partially correct |
| Saved evidence and history | Router public projections and reporting/history services | Keep original question/answer/memo/assets and feedback distinct; staff reports must not expose unsubmitted questions |
| Safe mathematical rendering | `components/MathsWorkbench/Content.js`, WorkbenchMarkdown and shared renderer | Preserve safe HTML/image choices, part layout, equation structure and frozen final answer; source compliance still starts at generation |

Some existing paths still need verification against the accepted standard. In
particular, direct tutoring before practice submission must not reveal the current
solution; generation-time compliance is not proved by a tolerant formatter; not
all new-provider absence/retirement paths preserve history; Maths-specific prompts
must not become another subject's rules. These are known engineering checks, not
permission to resume or claim them fixed here.

## Capability evidence rule

This list is a starting evidence map, not an exhaustive capability catalogue.
Capabilities declared by the local draft loader are `whole-question-v1`,
`prepared-assets-v1` and `portable-objectives-v1`. These names do not establish
interactive graph/construction tools or accounting cell-level marking. Record
the selected app revision, exact input/render/mark paths and relevant verified
test evidence in each capability record. Mark insufficient evidence as unverified
and escalate an investigation; do not invent either availability or a missing feature.

## Preservation decision for a proposed change

Classify each requirement as **preserve**, **document** or **verify/change later**.
Use existing compliant behavior before building another helper. Reuse/extension
is versioned and re-reviewed; saved attempts retain their exact evidence.
Future-question version selection for existing decks must be explicitly proven
under the later application compatibility work; it is not already guaranteed here.
Do not silently change unlock, timer, feedback, billing or progression rules while
moving subject content ownership. Any material expansion goes to Jeremy/Vitalis.
