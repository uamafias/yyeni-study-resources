# NSSCO Mathematics 6131 resource audit — 3 November 2026

**Later instruction executed:** Jeremy explicitly requested deletion of the
3,300-card bank and removal of its dependencies. That cleanup is now complete
locally: the active bank/checksum and bulk importer/builder were removed from
both repositories. Workbench rebuilding uses direct recipe/seed plans; old Studio
preservation uses slot metadata and hashes without static card text. All 3,944
current Workbench examples remain. The audit below preserves its original findings;
its old-bank keep-for-now advice is superseded by that completed task. 628 affected
application checks and 12 export tests pass; 2,111 current package files verify.

The current resources are intact, but the workspace needs a clearer distinction
between current content, historical evidence and older experiments. Keep the
current bank and its dependencies. Repair the authoring workflow and provenance
before deleting old banks or generator code.

Scope: the local `work/namibia-nssco-6131/` workspace, its application deployment
mirror, file consumers and references to earlier review packets. This is an
organisation, integrity, reproducibility and archive-readiness audit. It is not a
new independent mathematical review or certification of syllabus coverage.
No production database or live saved-deck inventory was inspected. Findings about
safe deletion therefore distinguish known code references from unknown live usage.

## What exists

| Resource | Verified count | Meaning |
|---|---:|---|
| Current recipe settings | 401 | 316 settings wrap 83 existing families; 85 recipes come from 78 newer builder functions |
| Assignment choices | 402 | HCF and LCM are separate choices for one recipe setting |
| Available / held choices | 396 / 6 | Six power-graph settings remain held for repairs |
| Saved examples | 3,944 | One repeated question fingerprint within one recipe; 3,943 distinct fingerprints |
| Registered historical generator families | 86 | Three are outside the current Workbench catalogue |
| Prepared diagram images | 1,912 | All referenced; none missing, corrupt or unreferenced |
| Prepared graph images | 80 | All referenced; none missing, corrupt or unreferenced |
| Historical source cards | 3,300 | 3,034 retained, 41 retired, 225 excluded from the main exam bank |
| Current mapped objective records | 152 | Mapping does not certify every clause or the held content |
| Older static-card snapshot / drafts | 14 / 6 | Narrow first-batch experiment; drafts still say not imported |
| Migrated package files | 2,112 | All match the application deployment copy |

The earlier total of 164 generators combines 86 registered families with 78 newer
builder functions. This is a count of code entries in two layers, not 164 separate
skills or 401 independent generator implementations. Resource/app copies and
historical review snapshots are not additional generators.

## Findings

### MATH-RES-001 — Medium: exact replay hashes depend on formatting caches

Regenerating all 3,944 saved examples from their recorded recipe version and seed
passes the exact saved fingerprint/contract check for 3,516 and fails it for 428,
across 55 recipe settings. Every question fingerprint matches. No question text,
canonical answer, raw worked step, objective mapping, mark allocation or raw
criterion differs in these 428 cases.

All 428 discrepancies disappear when derived `*_content` display fields and the
hash itself are removed from the contracts. For example, a comma in the last
working step of `wb6131:legacy:nssco_fractions_decimals_percentages:3`, seed 3004,
was cached as a maths block and is now a text block. Because the contract includes
those caches, its hash changes when presentation improves.

Evidence: `registry.py::regenerate_card`, `registry.py::grading_contract` includes
the full worked-step and criterion dictionaries; `content_format.py` attaches
display caches to those dictionaries. Existing R7 bank tests check saved contracts
against the saved raw snapshot, not exact replay through the current generator.

Recommendation: separate the stable marking evidence/hash from the derived display
cache, or explicitly version the display/contract format. Preserve saved learner
snapshots and old hashes. Add exact-replay coverage to future package acceptance.
This is a reproducibility issue, not evidence of 428 wrong mathematical answers.

### MATH-RES-002 — Medium: the authoring migration is not yet complete

The source package can generate questions and rebuild the main bank/catalogue.
However, only two build scripts were migrated. The prepared-bank READMEs reference
`prepare_visual_flashcard_banks.py` and `prepare_flashcard_graph_bank.py`, which
remain only in the app. The visual preparation script also imports
`prepared_diagram_png.py`. The display-refresh tool and review/coverage tools also
remain app-side. The current approved rendering font is a local external input.

Recommendation: move or deliberately package the remaining authoring/preparation
tools with their dependencies, document rendering inputs and move reusable content
acceptance tests alongside them. Keep the application responsible for authorization,
sessions, learner uploads, billing and delivery. Preserve old image-bank versions.
Do not regenerate immutable assets merely to change repository ownership.

### MATH-RES-003 — Medium: evidence links will break on another computer

All 30 links under `analysis/inputs/` are absolute. Fifteen PDF links point to this
machine's resources checkout; fifteen text links point into an old `/private/tmp/`
scratch directory and are already broken. These are links to evidence, not
additional independent copies of the papers. Logical linked-file sizes in the JSON
inventory must not be interpreted as additional occupied disk space.

Recommendation: replace PDF links with repository-relative references and either
rebuild text extracts from the original papers or remove the dead scratch links
after changing their callers. Preserve the original papers and examiner reports.

### MATH-RES-004 — Medium: the subject has two different objective registries

`curriculum/objective_registry.json` honestly identifies itself as a six-objective
partial registry from the initial lesson experiment. The current 152-objective
mapping is buried under `workbench/package/docs/audits/nssco-6131-objective-map-2026-10-30/`.
The older IDs use `OBJ-6131-...`; Workbench uses `6131:...`. There is no single
subject-level entry point explaining which registry to use for new work.

Recommendation: name one current subject registry and supply a crosswalk for old
IDs. Keep the six-objective record as historical evidence rather than overwriting
it. Add a subject index showing current bank, source evidence and review status.

### MATH-RES-005 — Medium: older files are still required by current code

`selection.py::source_policy` reads `all-topics.json` and validates the disposition
against its exact checksum. `legacy.py` reads the retired-card list and legacy
settings. Studio's generated-card path still resolves registered generator IDs;
ordinary bank cards and frozen Studio deck cards retain `generator_id` and params.

The three families outside Workbench are `nssco_histograms_text`,
`nssco_locus_numeric` and `nssco_reading_charts_text`. Absence from Workbench does not
prove absence from saved Studio decks. Offline `family_visual_*` modules are used
by the prepared-bank build tools even though they are not registered at runtime.

Recommendation: keep these dependencies until their callers are replaced and a
read-only saved-card/deck usage inventory establishes whether old generator IDs
are still needed. Deleting them now could break replay, imports or future rounds.

### MATH-RES-006 — Low: old guidance and examples need historical labels

The initial `analysis/ENGINE-REQUIREMENTS.md` describes photos as a proposed new
feature and some now-supported figures as unavailable. The first static-card
review packet describes six fixed worked-problem cards (41920–41925), whose job is
now covered by renewable recipes. These are useful historical records, but poor
instructions for someone creating the next recipe today.

Recommendation: archive superseded operator briefs/review requests after adding a
current index. Keep useful formula/concept cards separate from worked-problem
examples. The 14-card file is only a dated snapshot, not proof of current live
card status; do not delete live cards based on this file.

### MATH-RES-007 — Low: one repeated saved example

Fingerprint `f7adc8ff732b647e4b6ab9c03c77726cb69cc3a5c420b7ddb37da65fd5117efe`
appears twice inside `wb6131:legacy:nssco_factorising_quadratics:1`. No exact
question fingerprint repeats across different settings. This does not rule out
overlapping skills with different wording or values.

Recommendation: deduplicate or replace the repeated candidate example in a future
reviewed bank version. Preserve any saved historical instances. Review semantic
overlap separately before merging apparently similar recipes.

## Keep, archive or delete

| Material | Recommendation | Reason / prerequisite |
|---|---|---|
| Current recipe bank, catalogue, definitions, marking references | Keep active | Required by Workbench; six holds remain enforced |
| Prepared graph/diagram manifests and all 1,992 PNGs | Keep | Every image has a manifest reference; historical identities are immutable |
| Original papers, examiner reports, syllabus facts, raw analysis, benchmarks | Keep as evidence | Underpin resource provenance; some verification remains partial |
| Old 3,300-card source bank, dispositions, retired list, legacy settings | Keep for now | Current runtime/build/import code still reads them |
| Three generator families outside Workbench | Retirement candidates, not deletion-ready | Check saved Studio usage before removing registration/code |
| Offline visual builders | Keep as authoring tools | Needed to prepare future versioned visual banks |
| Earlier first-batch instructions and outdated capability briefs | Archive candidates | Add a current index and preserve provenance first |
| Six fixed worked-problem examples in the dated static snapshot | Mark superseded for new authoring | Preserve conceptual/formula cards and establish live usage separately |
| Earlier application review rounds | Preserve as historical review evidence | Archive/package separately if desired; do not treat copies as new resources |
| Fifteen broken scratch-text links | Replace or remove after caller review | They cannot currently provide evidence; originals remain in the repo |
| Python caches and temporary generated files | Disposable local artifacts | Not curriculum source; not a meaningful content cleanup |

No bank, registered generator or prepared asset is proven safe for immediate
permanent deletion by this audit.

## Validation and limits

- Package manifest verification and source/application equality: 2,112 files pass.
- All 1,992 prepared PNGs exist and match their manifest identities; no orphans.
- All 3,944 recorded recipe versions load; exact replay results detailed above.
- Ten raw-paper record checks pass: 519 records representing 1,000 marks.
  Only 271 records claim image verification; six lack an official answer field.
  Passing schema checks is not independent verification of all source claims.
- Existing static-card checks pass with warnings: six fixed worked problems,
  and exam-wording overlap on two of the six draft cards.
- The latest existing R7 review still requests changes and declines full syllabus
  certification. The current catalogue keeps the six known graph settings held.
- No fresh human/vendor content approval, live DB inspection, paid provider call,
  database import, learner assignment or deployment was performed.
- The migration remains local/uncommitted. Its resources files must be committed
  with their manifest before anyone else can retrieve this package from GitHub.

Recommended order: fix evidence portability and exact-hash replay; complete the
authoring tool package and subject index; inventory saved generator usage; then
archive obsolete instructions and retire unused content through a reviewed change.

Detailed machine evidence: [inventory and replay results](namibia-nssco-6131-resource-audit-2026-11-03.json)
and [existing validator outputs](namibia-nssco-6131-existing-checks-2026-11-03.json).
