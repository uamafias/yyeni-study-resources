# Application handoff — 6131 Mathematics pilot

15 November 2026. Commissioned by Vitalis; selections/edition remain provisional.
Reported to Vitalis through this session and linked audit, acknowledgement pending.
These are investigation/build needs, not delivered capabilities or deployment approval.

Evidence checked read-only: Chiang Mai revision
`0f0832ddedf40010e467f60184ccf56d63384c09`, platform loader/contracts/presentation,
admin MCP catalogue/source searches and supplied November 14/15 audit reports.
Wider UI/persistence findings from those reports have not been replayed here.

| ID | Need and evidence | Acceptance / next owner |
|---|---|---|
| CAP-01 | Bloom, exact curriculum identity, stable part and criterion links; current catalogue allowlist omits Bloom and public parts use ordinal IDs | App team: validate reviewed metadata; preserve IDs/labels through catalogue, selection, saved instance and history; whole-card maximum from complete selected branch; unknown remains explicit |
| CAP-02 | Graph/sketch/construction response and visual marking reference/feedback; showing assets or accepting photos is insufficient | App team with resource author: exercise real source-backed task, correct/partial/alternative/wrong/ambiguous visual submissions and required accuracy/calibration; keep affected demand held until verified |
| CAP-03 | YYeni MCP delivery of reviewed Workbench packages, scoped availability and learner assignment; local action catalogue has no Workbench action found | App/MCP team: discover actual deployed capabilities; then implement or verify separate install/mapping/deck operations, permissions, dry-run, idempotency and rollback |

## Proposed metadata example, not an accepted runtime schema

This deliberately uses placeholders; it is not a classified real recipe. Agree field
names/conversion with the provider contract before implementing or publishing.

```json
{
  "recipe_id": "<existing-or-new-stable-recipe-id>",
  "recipe_version": 1,
  "selection_id": "<stable-choice-id>",
  "branch_id": "<reviewed-branch-id>",
  "curriculum_id": "<board-code-edition-id>",
  "parts": [{
    "part_id": "<stable-part-id>",
    "primary_objective_id": "<verified-objective-id>",
    "other_assessed_objective_ids": [],
    "criterion_ids": ["<stable-award-id>"],
    "blooms_level": null,
    "classification_status": "unclassified"
  }],
  "whole_card_blooms_level": null,
  "classification_version": 1,
  "required_response_capabilities": ["<capability-id>"],
  "required_asset_capabilities": ["<capability-id>"]
}
```

Keep source quotations, detailed rationale/review inputs and parameter design in
authoring evidence. Runtime gets exact version/branch/seed/fingerprint, frozen
question/solution/memo and references. Teacher display receives safe objective
descriptions, reviewed classifications and capability/review status. Learner views
must not expose private answers, criteria, hidden review notes or test solutions
before the permitted reveal. Attempts/progress remain app-owned.

CAP-01 checks must include mixed Apply/Analyse/Evaluate => Level 5 once, a lower
branch that cannot inherit another branch's higher level, an unclassified part,
changed part order and preserved historical snapshots. Response capabilities are
subject-specific requirements, not a demand that all subjects use geometry fields.

For CAP-03 the proposed delivery envelope names resource revision, manifest digest,
accepted recipe versions/choices, explicit school/classroom/lesson mapping and an
idempotency key. Learner assignment uses a separate request. Acceptance rejects
wrong-school mappings, unavailable/held versions, stale digests, duplicate retries
and partial failed imports without corrupting previous assignments. No real target
or operation has been selected or invoked in this pass.
