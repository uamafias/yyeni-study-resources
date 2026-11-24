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
  "metadata_contract": "proposed-workbench-design-0.1.4",
  "curriculum_id": "nam-8227-nsscas-dec2020",
  "recipe_id": "WB8227-modulus-graph-recovery",
  "recipe_version": "0.1.4",
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
  "recipe_version": "0.1.4",
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

## Stage-D acceptance requirements — D4 update

Recipe design revision is0.1.4; classification identity is consistently `8227-pilot-design-0.1.1`. These are proposed resource/app contract requirements, not implemented APIs. OD-4 and OD-5 bind; final owner approval follows Claude’s D4 confirmation.

- **APP8227-05 marking:** named modulus coefficient fields and complete formulas receive the same B1 www awards. A bare correct triple can earn3/3; wrong working can invalidate its affected award. Practice still invites vertex/point reasoning. Test the G5 www gate against the wrong exponential-index method at x=0, mapped divided/log-form proofs, own-derived-gradient substitution, and exact equivalent final targets. OD-6 binds the misread principle and feedback. Proposed MR03-OPS-D4 operations mark gross evidence before one net deduction per eligible datum from its first earned A/B anywhere in question order; carry to a later use if the first part earns none. Dependencies, DM and www use gross evidence. Once-ineligible data stay canonical in every part. Eligible F.T. overrides ordinary c.a.o./not-F.T. qualifiers; named errors and OD-1 remain. Practice feedback names the misread. All operational details await exact-manifest approval.
- **APP8227-05 F.T. and precision:** R-form own-phase roots are judged within the learner's shifted interval; an endpoint is rejected. Trapezium b:B2 uses their own(a), not a closed whitelist of canonical-path values. Shape c:B1 is relative to their own asymptote, with canonical shift/intercept awarded separately. d:B1 follows their graph and the accepted OD-5 DB1 follows the same own curve. Log U-M1 follows a coherent earlier log equation, while a newly omitted prefactor in(b) is a new error. Vector input must preserve the 1-d.p. form80.0/63.0 when required; numerical storage must not erase that evidence. Exact 60°/90° remain allowed exceptions.
- **APP8227-01/05 outcome privacy:** the mixed-motion choice uses an outcome-neutral title, expanded velocity and one fixed4+2 tariff for 144 sign-change/24 no-change cases. The internal historical branch ID is not learner copy. Roots, case tags, conditional principal exact-angle links and reference/memo hints stay private until submission; do not leak which method is needed through metadata or labels. Test R1-only credit for root work plus calculator legs without a primitive, own-root F.T., and R4 dependence on R2/R3.
- **APP8227-04/06 original subtask guard:** for trapezium h=2, part(c) is the attributed2023 P2 Q6(c) original under `original_subtask_policy`; never label the whole question original. A generated-fresh request excludes `['log-sketch',2]`. The domain has30 mathematical presentations,11 contexts and mathematical packing3, but only 22 fully-generated presentations and strict generated-fresh packing2. Any attributed-original practice route must be explicitly selected and use the exact source wording/part label. Exposure remains part-scoped across all contexts. This requires a deliberate contract conversion, not a misleading same-type label or a hidden source path.
- **APP8227-03 later representation gap:** this pilot has no supplied geometric figure, although28 inspected examination parts do. Graph assets do not qualify geometric-figure reading/generation/marking. Keep that later-scope acceptance requirement explicit; do not infer production capability or a new capability hold.

Freeze decimal half-up fixtures at E/F: R-form half ties and the exact 116.5→117 motion boundary; preserve exact 233/2 as accepted. Rounding intermediates can flip final answers even on valid admitted tuples, so evaluate final acceptance from unrounded mathematical data and retain demonstrated method credit when precision alone fails. The named source/fixture receipts distinguish paths with rounded R, phase, ratio or both; no generic “rounding tested” claim replaces them.

Exposure migration is separate from immutable versioned marking. The motion mixed-branch key changes from `(k,r,c,tail)` to `(k,r,c,T)`; for every old reversal exposure compute `T=r+tail` and block that same task in0.1.4. A version bump or renamed public title cannot reset semantic freshness. Polynomial `(A,B,u)` and exponential `(V,k)` part keys retain their meanings with smaller domains. Trapezium keys retain their meanings, with the original h=2 sketch now explicitly blocked for generated-fresh requests. Test these aliases using D1 revealed examples before admitting a D4 test instance; keep all old question/memo bytes unchanged.

D4 APP8227-05 acceptance fixtures: persist both gross evidence and net score, the datum’s once-only eligibility decision, first-use part and actual deduction part/criterion. Verify the same datum never receives another deduction; no M/DM borrowing or negative totals. A missing first-part A/B carries the deduction to the next earned A/B on that datum. Only no A/B anywhere means no deduction.

Recompute and test explicit ledgers: vector OB sign alone6/7; plus wrong resultant4/7; ineligible no-p reuse3/7. Exponential V12→21 alone4/5; plus −V/k derivative error2/5. Mixed motion R2 net deduction preserves gross R4 dependency5/6. Implicit G2 deduction preserves gross G5 dependency4/5; once-ineligible proof/point data stay canonical in later parts. Designed no-real principal target sign misread2/3. A motion datum flipping the direction-change outcome is ineligible, with canonical marking in both parts. These are fixed design examples awaiting an implemented marker and local website acceptance.

D4 APP8227-01/05 motion: test the four diversified no-change contexts and report the residual lookup limits; a vertex-value-only argument earns no R1. A correctly justified harmless partition earns4/4; R5 signed legs need a primitive and both bounds. D4 APP8227-05 trapezium: a visible factorised square retains b:B1; visibly wrong log-law reasoning loses b:B2www, including the k=2 numeric coincidence. A missing derivation alone still allows B2 for a visible correct2k×own(a) product, preserving the1/2 bare-product sample. No app capability or scoring implementation is certified here.

## Stage-E implementation receipt — 24 November 2026

Vitalis approved manifest `4a054832…17d8ec`, including MR03-OPS-D4. All nine
recipes now have resource generators. This is resource authoring authority, not
app activation authority. Rechecked `workbench_platform/loader.py`, `contracts.py`,
`presentation.py` and `marking.py` read-only. No app/pinned file was changed.

| Boundary | Implemented resource behavior | Remaining app acceptance |
|---|---|---|
| Version | Package/native recipe 0.1.4; immutable provider-v1 integer revision 1→0.1.4 mapping in provenance. Both preserved on every instance. | Preserve native version through saved selections/attempts; reject wrong revision; never reinterpret old attempts. |
| Native metadata | `catalogue-native.json` retains full branch/part Bloom, rationale, direct/prerequisite/conditional links, source references and strict fresh upper bounds. Limited `recipes.json` uses the existing catalogue allowlist without hiding new fields in labels. | APP8227-01/02: version the native metadata contract; preserve qualified authored part IDs and criterion links. Existing app presentation still creates alphabetic IDs. |
| Marking | `native_marking_memo` is structured `8227-marking-evidence-v1`, including alternatives, dependencies, FT and visual references. `marking_memo` is an explicit limited v1 structural bridge; its guide contains textual criteria/steps, not encoded image-reference fields. | APP8227-03/05: consume the native rubric and visual references deliberately. v1 rejects `reference_images`; a passing v1 structural check does not show reliable sketch/photo/free-text marking. Run the 97 declared marking expectations against actual orchestration, keeping ambiguity pending. |
| Assets | 326 unique original SVG files are sealed from the same parameter records; native assets bind qualified target parts, must-read givens and fixed/variable/relation metadata. Question/solution roles and instance/reveal checks are separate. | APP8227-03 and Q11: v1 public asset whitelist drops alt text, must-read givens and target part binding. Preserve these in the new display contract. `resolve_asset` alone does not authorise access; bind caller, instance, role and reveal state. |
| Sources | Native learner projection filters held/related refs and retains part-scoped `target_part_ids` and `scope`; internal paths/hashes/reviewer notes are excluded. | APP8227-04: show each label on its assessed part, never a card-wide badge inherited from a sibling; save locators with native version. |
| Renewal | Pure seeded finite-domain selection; separate semantic/visible identities; bounded exhaustive freshness checks, cross-branch shared keys, version-independent exclusions and explicit exhaustion. Repeated practice is labelled and prohibited in test. | APP8227-06/08: learner exposure/reservation storage, atomic concurrent selection, retries, canonical-example exposure and historical aliases. Helpers hold no learner data. |
| Decks | Three unassigned resource compositions reconcile to 19/20/17 marks. | Application creates decks and assigns learners only for an explicitly chosen target. No operation was attempted. |

The 1,702 admitted branch parameter rows are not 1,702 fresh problem types or
independent complete tests. The implicit branches share curves/proofs; R-form,
principal inverse, log-model and visual chains have much smaller assessed-part
freshness bounds. The default trapezium generator supplies only its 22 fully
generated presentations (strict upper bound two before exposure); the h=2 original
sketch subtask is excluded and no original-question display mode is implemented.

The five D4.1 notes are carried in `authoring/NOTE-CARRY.md` and runtime rules.
Native marking carries remain: datum identity across repeated displays,
competing eligible misreads sharing one earned mark, implicit C4→5 non-product
routes and the further notes in that register. They are not silently given new
scores. Only design-blocking or should-fix findings trigger a design repair round.
