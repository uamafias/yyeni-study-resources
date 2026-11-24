# Application handoff — NSSCAS Mathematics 8227 pilot design

24 November 2026. Owner/recipient Vitalis. PLANNER Codex. These are design
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
  "metadata_contract": "proposed-workbench-design-0.1.3",
  "curriculum_id": "nam-8227-nsscas-dec2020",
  "recipe_id": "WB8227-modulus-graph-recovery",
  "recipe_version": "0.1.3",
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
current planning session on 24 November 2026, before the owner checkpoint.
Current disposition: visual inclusion remains binding; implementation verification
and design approval are pending. Next owner Vitalis/application team for the
contract/capability work after plan approval. No delivery, production activation,
learner assignment or external message is authorised here.

## D1 repair additions to APP8227-01/05/06

These are proposed contract requirements, not a new claim about the inspected app. OD-3 requires Claude's short design check before Vitalis approves implementation scope. The fixed nine recipes now have 14 branch choices, 27 assessed slots and 42 worked design cases.

**APP8227-05, answer-given proof.** The extended implicit branch has `show-derivative` (4), `gradient` (2), `normal` (3). The question may expose its derivative target because it is explicitly given. The private memo still contains the proof route and criteria. All proof marks require working; copying the target gives zero, and a correct endpoint reached through invalid algebra gives no terminal accuracy. There is no F.T. into a supplied target. Later parts may use the given derivative even if the proof failed; they do not earn the four proof marks again.

Illustrative private design binding (not a deployed API shape):

```json
{
  "recipe_id": "WB8227-implicit-normal",
  "recipe_version": "0.1.3",
  "branch_id": "normal",
  "part_id": "show-derivative",
  "response_format": "proof/show-that",
  "answer_given": true,
  "answer_only_marks": 0,
  "terminal_accuracy_requires": ["complete_correct_forward_derivation"],
  "follow_through_to_given_result": false,
  "later_part_may_use_given_result": true
}
```

Acceptance: test a full proof, copied target, invalid cancellation reaching the target, correct alternative rearrangement, incomplete proof, and failed proof followed by a valid gradient/normal. Verify 4+2+3 totals without double credit or leaking proof steps before submission. Tests also cover `www`, DM, named method caps, limited own-sketch F.T., misread, premature rounding and units requested by the stem. Under OD-1 a bare correct answer earns zero except an explicit official type exception, such as correct modulus named coefficients or a complete formula without wrong working. Practice recognises value correctness and asks for evidence rather than asserting the value is wrong.

**APP8227-01, conditional assessed metadata and response formats.** Principal inverse has one neutral fixed-3-mark branch; it accepts symbolic work or an explanation. Its range demand applies throughout; its exact-special-angle demand applies only to `real-solution` instances. Both inherit proposed Apply 3, but no obstruction instance inherits an absent exact-value assessment. Preserve `response_formats: ["symbolic", "explanation"]`, case condition, direct links and part rationale privately; safe metadata can list both supported response kinds. Acceptance: valid/invalid targets use the same neutral stem and tariff, accept substitution-contradiction reasoning, and never advertise a conditional demand as assessed in every instance.

**APP8227-06, exposure and exhaustion.** Keep raw parameter/presentation capacity separate from whole-task contexts, part-instance keys and cognitive outcome classes. Exemplar/solution exposure records all assessed keys, including shared derivative proof identities, unchanged vector-angle (r,s), unchanged R-form (a,b), trapezium sketch shape and unchanged log model. A task is wholly fresh only if every required part key is unseen. Practice with partly repeated work is labelled after-feedback; fresh tests cannot silently use it. A repeated outcome such as “underestimate” alone is not a part-instance key. Acceptance: exhaust each key space, vary only a non-key parameter and confirm it cannot reset exposure, and test cross-branch shared proof/gradient exposure. Owner-authorised exam originals are attributed separately and their exposed subfacets also block a generated clone.

**APP8227-02/03/05 notation fixture (vector-contract-14).** Enter the resultant as a three-component column vector with signed entries; also test equivalent row/component input where the interface allows it. Render negative components, scalar fractions, degree signs, exact 60°/90°, and the learner's working in question, feedback, solution and saved history. Reordering parts cannot move the vector's criterion links. Compare entered and reloaded notation visually; an offline KaTeX pass alone does not qualify the learner input control.

## D2 changed-scope acceptance additions

Recipe design revision is0.1.3; classification identity is consistently `8227-pilot-design-0.1.1`. These are proposed resource/app contract requirements, not implemented APIs. OD-4 and OD-5 bind; final owner approval follows Claude’s D3 confirmation.

- **APP8227-05 marking:** named modulus coefficient fields and complete formulas receive the same B1 www awards. A bare correct triple can earn3/3; wrong working can invalidate its affected award. Practice still invites vertex/point reasoning. Test the G5 www gate against the wrong exponential-index method at x=0, mapped divided/log-form proofs, own-derived-gradient substitution, and exact equivalent final targets. OD-6 genuine unchanged-difficulty question misreads use one first-use earned A/B deduction, all A/B F.T. and normal M/DM; the per-datum ledger prevents a second deduction. Own-figure/easier/no-solution errors receive normal canonical treatment. OD-1, www and named method exclusions remain.
- **APP8227-05 F.T. and precision:** R-form own-phase roots are judged within the learner's shifted interval; an endpoint is rejected. Trapezium b:B2 uses their own(a), not a closed whitelist of canonical-path values. Shape c:B1 is relative to their own asymptote, with canonical shift/intercept awarded separately. d:B1 follows their graph and the accepted OD-5 DB1 follows the same own curve. Log U-M1 follows a coherent earlier log equation, while a newly omitted prefactor in(b) is a new error. Vector input must preserve the 1-d.p. form80.0/63.0 when required; numerical storage must not erase that evidence. Exact 60°/90° remain allowed exceptions.
- **APP8227-01/05 outcome privacy:** the mixed-motion choice uses an outcome-neutral title, expanded velocity and one fixed4+2 tariff for 144 sign-change/24 no-change cases. The internal historical branch ID is not learner copy. Roots, case tags, conditional principal exact-angle links and reference/memo hints stay private until submission; do not leak which method is needed through metadata or labels. Test R1-only credit for root work plus calculator legs without a primitive, own-root F.T., and R4 dependence on R2/R3.
- **APP8227-04/06 original subtask guard:** for trapezium h=2, part(c) is the attributed2023 P2 Q6(c) original under `original_subtask_policy`; never label the whole question original. A generated-fresh request excludes `['log-sketch',2]`. The domain has30 mathematical presentations,11 contexts and mathematical packing3, but only 22 fully-generated presentations and strict generated-fresh packing2. Any attributed-original practice route must be explicitly selected and use the exact source wording/part label. Exposure remains part-scoped across all contexts. This requires a deliberate contract conversion, not a misleading same-type label or a hidden source path.
- **APP8227-03 later representation gap:** this pilot has no supplied geometric figure, although28 inspected examination parts do. Graph assets do not qualify geometric-figure reading/generation/marking. Keep that later-scope acceptance requirement explicit; do not infer production capability or a new capability hold.

Freeze decimal half-up fixtures at E/F: R-form half ties and the exact 116.5→117 motion boundary; preserve exact 233/2 as accepted. Rounding intermediates can flip final answers even on valid admitted tuples, so evaluate final acceptance from unrounded mathematical data and retain demonstrated method credit when precision alone fails. The named source/fixture receipts distinguish paths with rounded R, phase, ratio or both; no generic “rounding tested” claim replaces them.

Exposure migration is separate from immutable versioned marking. The motion mixed-branch key changes from `(k,r,c,tail)` to `(k,r,c,T)`; for every old reversal exposure compute `T=r+tail` and block that same task in0.1.3. A version bump or renamed public title cannot reset semantic freshness. Polynomial `(A,B,u)` and exponential `(V,k)` part keys retain their meanings with smaller domains. Trapezium keys retain their meanings, with the original h=2 sketch now explicitly blocked for generated-fresh requests. Test these aliases using D1 revealed examples before admitting a D2 test instance; keep all old question/memo bytes unchanged.

D3 APP8227-05 acceptance additions: persist the OD-6 datum ledger with first-use part and the actual deducted A/B slot; no second penalty in later parts, no negative/borrowed deduction if no A/B earned. The normal exponential misread12→21 is4/5, vector OB sign misread6/7. Verify wrong-root no-change distance3/4 despite a coincident total; R1 accepts a complete constant-sign proof without a root solve. R5 accepts signed part-(a) legs only when evaluated from an attempted primitive with both bounds; quadrature-only legs yield0/2 on displacement. This is a proposed app handoff, no app behaviour is certified.
