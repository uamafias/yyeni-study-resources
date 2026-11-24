# Application handoff — NSSCAS Mathematics 8227 pilot design

23 November 2026. Owner/recipient Vitalis. PLANNER Codex. These are design
requirements, not app changes, delivered capabilities or activation approval.
They extend the existing subject-provider route. Read with `recipe-contract.md`
and `capability-gaps.md`; subject content stays in resources.

## Evidence rechecked

Read-only inspection of the Chiang Mai app checkout at HEAD
`0f0832ddedf40010e467f60184ccf56d63384c09`; actual inspected hashes are recorded in
`planning/stage-d-baseline.json`. Its web Workbench files have local changes,
so HEAD alone does not freeze the inspected tree. No app tests, server start,
sign-in or UI acceptance were run. No pinned checkout or app file was edited.

Current `contracts.py` checks whole-question parts, marks, worked steps, frozen
memo and visible-content fingerprint. `loader.py` and the resources CLI have a
public-field allowlist without Bloom/branch/part metadata. `presentation.py`
assigns part letters by list index. These are current code observations, not
assumptions that all previous investigation findings remain unchanged.

Vitalis's owner decision includes all visual demands, accepting the announced
17 November diagram/sketch capabilities for selection. This checkout inspection
does not test that announcement. No YYeni Workbench operation is exposed by name
in this session's connected-tool inventory; the server's full MCP capability is
unverified. No importer or publication operation was attempted.

## Required conversions and acceptance checks

| ID | Requirement and purpose | Example / conversion | Acceptance check |
|---|---|---|---|
| APP8227-01 / CAP-8227-01 | Safe metadata survives catalogue, teacher picker, saved choice and history | Versioned metadata holds curriculum, recipe/version, fixed branch/choice, topic, direct links, response needs and proposed/reviewed Bloom; retain existing `id`/`recipeId` bridge | Round-trip exact IDs, grouping, marks and complete highest-part Bloom through picker→saved selection→practice→test→history. Unknown/private fields still rejected; deliberate allowlist version change, not data hidden in titles |
| APP8227-02 / CAP-8227-01 | Authored part/criterion identity survives order changes | Preserve supplied `part_id`; display label/order separate. Every criterion links to an assessed part by ID | Reorder parts without moving credit or links. Reject duplicate/missing IDs, dangling criteria and wrong-instance memo. Keep historical letter-only snapshots through explicit legacy adapter |
| APP8227-03 / CAP-8227-02 | Diagram/question/solution/marker agree on essential data | Original asset spec uses one data record; `must_read_givens`, `fixed`, `variable`, `relations`, response-feature rules and separate question/solution assets | Normal/changed/boundary asset renders preserve labels, axes, endpoints, units and visibility. Mark correct/partial/alternative/wrong/ambiguous sketches; unclear evidence stays pending/clarification. No pre-submit reference/solution asset leakage |
| APP8227-04 / CAP-8227-01 | Per-branch attributed references | Checked branch→source-part equality selects `same-type`; source paths/raw notes stay internal | Different branch cannot inherit a sibling's label. Held sources and `related` refs never display; original vs generated variant labels are distinct; code/session/variant/page survive saving |
| APP8227-05 / CAP-8227-01 | Reliable partial/alternative marking and reveal | Translate criterion IDs, alternative paths, caps, dependencies, F.T., exactness and answer-only evidence into existing frozen memo | Named sample scripts receive declared marks; exclusive paths never sum, valid alternatives accepted, ambiguity not fabricated. Practice help is answer-free; test blocks help until submission; canonical solution stays frozen |
| APP8227-06 / CAP-8227-01 | Meaningful renewal and finite exhaustion | Private seed+parameters+semantic key, visible fingerprint, exact branch capacity; reserve/retry per learner | Deterministic replay; exclude exposed example/practice/test semantic keys, including shared subparts across branches; two concurrent renewals do not collide; retry returns same reserved instance; exhausted branch reports zero rather than repeating silently |
| APP8227-07 / CAP-8227-03 | Delivery separates package installation, classroom availability and assignment | Immutable package/version/manifest; explicit school/classroom/lesson allowlist; separate deck/learner request | Inspect actual MCP operations; dry run and repeat import are idempotent; reject wrong-school/lesson and stale versions; preserve objective/recipe traceability. No Flashcard Studio importer substitution |
| APP8227-08 / CAP-8227-01 | Branch choice does not corrupt progress or historical work | Choice fixes branch/version; app owns recipe progress key and saved question/memo/assets | Selecting two branches cannot double-credit one recipe in a round. Branch-specific practice is visible; historical attempts retain versions, marks and Bloom; retired/missing resources fail without damaging active rounds |

Illustrative **proposed** safe metadata, not accepted by the current allowlist and
not an installed API payload (actual reviewed part/branch labels come from the
work order, not this example):

```json
{
  "metadata_contract": "proposed-workbench-design-0.1.0",
  "curriculum_id": "nam-8227-nsscas-dec2020",
  "recipe_id": "WB8227-modulus-graph-recovery",
  "recipe_version": "0.1.0",
  "branch_id": "explicit-fixed-branch-from-work-order",
  "directly_assessed_demand_ids": ["8227:2020:M2:T1:O02:D02"],
  "bloom": {"status": "proposed-unreviewed", "whole_level": null},
  "required_response_capabilities": ["numeric", "diagram-reading"],
  "availability": "design-only-owner-approval-pending"
}
```

Example private visual binding (not a deployed wire shape): a modulus asset uses
the exact tuple `(a,b,c)` for `y=a|x+b|+c`; must-read givens include vertex,
labelled intercept, axis direction and scale. The marker recovers the same tuple
and can compare a learner's parameter values without exposing that tuple in a
pre-submit payload. It must not receive a stale fixed textbook crop when b changes.

No proposed field is silently mapped into an unsuitable old field. Resource
definitions, package integrity and the app contract must be updated together in
later authorised engineering. An executable module count is not selected here.

## Local feature acceptance after authoring/review

Use the actual reviewed nine-recipe pilot, not synthetic renaming-only subject
data. Exercise all selected branches and response formats in the local website;
teacher selection, learner practice/support/reveal/renewal, test fresh instance,
partial/alternative/visual marking, pending clarification, saved history and
retirement/version failures all need evidence. Cross-school access tests use an
explicitly selected development target. Preserve current timer/unlock/billing
and original-attempt protections. No production inference follows from local tests.

## Notification and next owner

CAP-8227-01/02/03 and the above scope were flagged directly to Vitalis in the
current planning session on 23 November 2026, before the owner checkpoint.
Current disposition: visual inclusion remains binding; implementation verification
and design approval are pending. Next owner Vitalis/application team for the
contract/capability work after plan approval. No delivery, production activation,
learner assignment or external message is authorised here.
