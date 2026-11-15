# Workbench framework audit and incremental development proposal

15 November 2026. Commissioned by Vitalis. Codex planning/investigation pass against
the current owner brief; not independent acceptance of the existing Maths bank.
Framework owner in the existing playbook: Jeremy. No ownership transfer inferred.

Owner update after this audit: Vitalis selected Namibia AS Mathematics, Grade 12,
for whole-syllabus problem-type mapping, beginning with source acquisition. The
earlier bounded NSSCO pilot proposal below is historical and no longer the immediate
scope. Continue from [the active pilot STATUS](../../../work/nam-8227-nsscas-2026/workbench/STATUS.md).

## Evidence and boundaries

Resources checkout: `/Users/professor/Documents/YYeni Study Resources`, starting
revision `d6b8f551a405673f3149910e00ebfb7f1e5312a5`. Existing harvest and Geography
changes are unrelated and preserved. Read AGENTS, TEAM-PLAYBOOK, the PLANNER role
only, Workbench README/templates/quality/technical appendix, tracker and Maths
workspace READMEs, manifests, provider provenance, tools and sampled bank/plan data.
No Mathematics 6131 row exists in the subject tracker; no Workbench STATUS,
HANDOVER, analysis folder or per-recipe work orders existed at the start of this pass.
This is a framework audit, not a claim to take over Jeremy's subject authoring.

App checkout inspected read-only:
`/Users/professor/conductor/workspaces/yyeni/chiang-mai`, revision
`0f0832ddedf40010e467f60184ccf56d63384c09`, including current
`services/api/workbench_platform/{loader,contracts,presentation}.py`, admin MCP
catalogue/source search, and the two supplied November 14/15 audit reports.
The reports' wider findings remain prior investigation evidence unless explicitly
rechecked below. No signed-in UI test, live MCP connection test or deployment.

Both `.context/resources-framework-review` and `.context/pinned-resources` exist.
Inspected the former's uncommitted five-file Bloom diff and new policy. Preserved
both checkouts without writes. The app's selected package is 1.0.1 according to its
audit; this repository's manifest/registry say 1.0.0 candidate. They are distinct
resource states and must not be silently interchanged.

## Retain and extend

Jeremy's accepted learning design already provides a strong subject-neutral core:
syllabus-first demand screening; include/exclude/hold selection; decisions that
distinguish recipe, pattern and generator; connected parts and follow-through;
answer-only rules; difficulty invariants; finite capacity; seed replay; meaningful
solutions; independent recomputation and cross-vendor review; capability escalation;
separate content acceptance, publication and environment activation.

The Maths package supplies real generators, marking evidence, assets, provenance,
saved examples and repair history. These are engineering/content candidates worth
auditing individually, not a reason to invent another framework. Preserve their
IDs and frozen history. Existing Studio cards are excluded as authoring inputs.
Legacy source-card references in the authoring plan require genealogy inspection;
they do not by themselves prove either fresh authorship or forbidden conversion.

## Findings and required corrections

| ID / priority | Evidence and implication | Smallest useful correction |
|---|---|---|
| FW-01 / high | Playbook source inventory and selection template did not explicitly cover textbooks, exercise families, editions, visual figures or reuse basis. This is a real gap against the new brief. | Extend existing A–D/Q gates with textbook analysis; no new pipeline. Added companion and template fields in this pass. Apply them to actual pilot sources next. |
| FW-02 / high | Bloom absent from sampled contract code and all 5,982 saved parts when checked for `blooms_level`; generic CLI and app catalogue allowlists omit Bloom. | Incorporate inspected owner policy; then implement reviewed recipe/branch/part labels, validators and app propagation. Unknown historical parts remain unknown. Policy additions now saved; runtime remains unchanged. |
| FW-03 / high | New playbook's source-to-selection/work-order records are missing from existing Maths package. Package edition is `existing-2026-candidate-bank`, not an exact syllabus identity. | Reconstruct a bounded, source-backed pilot packet without overwriting existing plan/bindings. Bind selected versions to exact edition/hash and assessed parts. Preserve wider gaps. |
| FW-04 / high | Current manifests/provenance explicitly say candidate, independent whole-bank approval pending and coverage uncertified. Prior focused repairs do not approve the whole bank. | Select and review exact pilot scope/bytes; do not promote all 409 settings or claim syllabus sufficiency from tags/counts. |
| FW-05 / high | Generic CLI `check()` counts `manifest.state == approved` as independent review and treats presence/success of an author hook as an independent oracle. It cannot establish reviewer independence or whether the oracle reuses the answer builder. | Bind review evidence to exact candidate digest, scope and reviewer; audit oracle implementation and known-error detection. Keep technical success separate from content acceptance. |
| FW-06 / medium | Older `tools/package.py verify` fails against current tree; generic provider validation stops for missing SymPy in this interpreter. README still describes older copy/export route and future provider as not enabled, while provider code exists. | Reconcile tooling/docs around selected provider contract, pinned interpreter/dependencies and honest checks. Do not reseal merely to silence a failure. |
| FW-07 / high | App catalogue allowlist rejects new classification fields. `validate_instance()` checks mark totals/text, but does not require stable part/criterion IDs; public presentation derives part IDs from ordinal positions. | Extend app contract with explicit stable IDs, criterion links and safe display metadata; verify persistence and grouping through teacher selection, saved labels and learner snapshots. |
| FW-08 / high | Diagram display/photograph submission does not establish reliable construction/graph assessment. Generic visual response capability remains unverified. | Include one visual-response pilot case as a visible capability hold until the app can demonstrate its required evidence/marking. Do not substitute an easier numeric question. |
| FW-09 / high for delivery | No Workbench action found in local admin MCP action catalogue; Python search found Studio exclusion tests, not recipe installation/mapping operations. No YYeni connector or Gemini tool was available in this session's discovered tools. | Design and verify explicit Workbench package/catalogue/deck operations. This is local-source evidence, not proof about every deployed MCP endpoint. Never use Studio importer as a substitute. |
| FW-10 / medium | Existing authoring plan contains school/classroom/lesson routing identifiers. These are deployment context rather than portable curriculum authority. | Keep app-owned routing in an explicit mapping/install envelope; retain immutable objective and version identities in the resource package. Do not silently migrate existing saved mappings. |

## Verification actually performed

Commands from repository root, Python 3.13 available in this shell:

```text
python3 work/namibia-nssco-6131/workbench/tools/package.py verify
  FAIL: Package differs from manifest (provider additions and generator files included).
python3 -m unittest discover -s work/namibia-nssco-6131/workbench/tools -p test_package.py
  PASS: 17 integrity/export tests, using temporary fixtures, no actual app export.
python3 -m yyeni_workbench_tools --app-root /Users/professor/conductor/workspaces/yyeni/chiang-mai validate work/namibia-nssco-6131/workbench
  BLOCKED/exit 1: Missing installed dependency: sympy.
```

Independent stdlib file-hash pass over the *provider* manifest found 2,121 declared
files with no mismatches and a matching registry-to-manifest hash. This does not
resolve the older wrapper verifier's failure or certify dependency closure/content.
See subject `analysis/provider-integrity-2026-11-15.json` for exact scope.
Recomputed bank census: 4,022 examples, 409 distinct recipe IDs, 5,982 parts;
provider catalogue holds 410 choices. Counts are different objects, not coverage.
No new generator truth tests, all-seed validation or content acceptance performed.

## Source position

See the subject's [source inventory](../../../work/namibia-nssco-6131/workbench/analysis/source-inventory.md)
and machine-generated path/hash inventory. Local syllabus cover confirms 6131,
Grades 10–11, implementation 2019, first examination 2020; publication December
2018. Assessment pages 27–28 were read directly. Do not use the package's
`existing-2026-candidate-bank` string as an edition.

Targeted official search located NIED's matching 2018 syllabus at
https://www.nied.edu.na/assets/documents/02Syllabuses/05SeniorSecondary/Mathematics/NSSCO_Mathematics_syllabus_final_2018.pdf .
The search is a current availability lead, not proof that no later amendment exists
or that downloaded bytes match; local PDF hash is recorded separately.

Local holdings: 11 paper files across 2020–2024 (including an extra 2021 P2 version),
six combined NSSCO reports for 2020–2025, two instructional candidates. No separate
matching schemes were found in the scoped Maths folder or dedicated Maths sources
folder. Report sections/appendices must be checked before declaring schemes absent
repository-wide. Proof-labelled papers need final-version verification.

One instructional PDF is a 2009 Zambian booklet despite its NSSCO folder. The
Grade 9 2025 workbook supplies relevant visual-source leads, not automatic NSSCO
coverage. No current commercial NSSCO textbook identity was established.

YYeni Web Harvester exists at `/Users/professor/Documents/YYeni Web Harvester`.
Read its README: manifest discovery/acquisition/verification and existing project
logs are the intended route. CLI/browser health was not run. No separate Web Hub
or Gemini integration was established. No sources were downloaded in this pass.

## Phases, deliverables and acceptance

This is a development sequence, not the subject authoring PLAN approval.

| Phase | Concrete outputs | Acceptance before progressing |
|---|---|---|
| 0 Audit and owner scope | This audit, source inventory, STATUS/HANDOVER, policy additions | Owner selects edition/grades, bounded pilot and continuing authorship responsibility; preserve Jeremy's work |
| 1 Verified evidence | Current edition/assessment facts, actual paper↔scheme/report pairs, textbook exercise/figure records; demand/selection matrix with stable IDs and holds | Source/assessment checkpoints; every selected part maps to exact objective, primary/direct/prerequisite roles explicit; examination vs textbook vs judgement separated |
| 2 Contract and exemplars | Extend current provider/design bridge with optional subject rules; work orders for smallest justified set; normal/changed/boundary question+solution+memo; app handoff | Owner accepts scope/work orders after source analysis; all applicable fields justified; no unclassified-part maximum or invented official awards |
| 3 Author pilot | Purpose-built or individually justified existing Workbench recipe versions, generators, diagrams, canonical answers, criteria, fixtures and illustrative practice/test deck compositions | Independent recomputation; normal/varied/boundary cases; correct/partial/wrong/alternative/ambiguous submissions; honest capacity/exhaustion; at least 64 draws per structural branch plus boundaries under existing quality target |
| 4 Independent acceptance and local feature test | Frozen candidate/review findings and exact accepted subset; actual app contract updates; teacher/learner render and saved-history evidence | Cross-vendor content review; local website practice/renewal/test/feedback/solution checks with real resources; no open affected blockers; historical snapshots preserved |
| 5 Delivery rehearsal | Versioned install and mapping/deck envelopes; dry-run/idempotency/rollback tests for selected dev school/classroom | Distinguish installation, availability and learner assignment; reject wrong-school requests/duplicate imports; target explicitly chosen before activation |
| 6 Physics transfer | Separately commissioned small source-backed Physics pilot exercising units, constraints and different marking/representations | Same core works without renamed Maths assumptions; subject rules explicit; no Studio conversion; new capabilities remain held until verified |

Recommended initial scope: approximately 6–10 justified recipe/branch choices
across algebra, contextual calculation, graph/diagram interpretation and one
genuine visual response. The latter can remain held while other choices progress.
Final count follows the selection analysis; it is not a production quota. Propose
one focused practice composition and one mixed fresh-instance test composition;
counts/timing are design proposals, not learner assignments.

## Owner decisions still needed

1. Use 6131 Mathematics, NIED December 2018, Grades 10–11 as the proposed baseline,
   subject to supersession/amendment checks, or supply another required edition?
2. Mixed bounded pilot (recommended), algebra-only, or whole-syllabus project?
3. Who continues Maths authoring and coordinates with Jeremy? His historical
   framework ownership remains intact; no tracker claim or acceptance was invented.

No school/classroom decision is needed for source/framework work now. It is needed
before actual delivery. No commit/push, source import, assignment or activation.
