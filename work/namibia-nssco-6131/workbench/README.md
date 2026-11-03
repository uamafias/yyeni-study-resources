# NSSCO Mathematics recipe cards and generators

This is the authoring home for NSSCO Maths Workout Bench. App paths are versioned
deployment mirrors. Existing decks use their immutable question snapshots.

## Current package

R8 smaller findings: 22 recorded outcomes, 32 settings / 318 examples refreshed.
440 authored demand entries have actual-part evidence after adding the algebraic
variation branch. R9/R10 focused reviews accepted the original repairs; the final small diagram
correction is locally verified. Full syllabus acceptance is not claimed. See `reviews/r9-focused-author-checks/`.

R8 M1–M4 follow-up: eight graph settings are now version 10 with readable
grid-aligned targets, balanced marks and clear excluded-zero markers. Shared
display formatting and served-solution validation are repaired. Independent
re-review, Low findings and wider syllabus acceptance remain pending.

- **409 recipe settings / 410 assignment choices / 4,022 distinct examples.**
- 2,116 managed source/build/dependency/provenance files; the manifest pins every
  checksum. The deployment lock verifies the app without needing this checkout.
- Generator code, canonical references, meaningful worked steps, marking contracts,
  diagrams, lesson routing and seed plans stay together.
- R7 author repairs: six power types restored at version 9, inline text/maths,
  missing contexts and general intersecting loci, smaller presentation fixes,
  and actual part evidence for all 439 authored demand entries.
- Whole-bank independent acceptance and syllabus sufficiency certification remain
  pending. Generation pools are finite and disclosed; a new seed need not be a
  new distinct question.

`package/` preserves application-relative paths for existing imports and builders.
`repairs/claude-r7/` preserves the original problematic examples/source separately
from their active corrected versions. `reviews/r8-author-checks/` records current
evidence. Neither learner snapshots nor immutable review packets are rewritten.

Only material authored or committed by Jeremy may be deleted. The obsolete 3,300
and 420-card banks/importers were verified under his Git records and removed.
Unverified-authorship drafts, prototype files and scratch links remain preserved.
The current builder uses `workbench-authoring-plan.json` and `catalogue-homes.json`;
Studio preservation uses slot decisions/hashes, not the deleted bank text.

Seven core authoring/check scripts are deployed with the package: bank/catalogue
builders, image-bank preparation, PNG rendering, display refresh and R8 author
checks. The app's coverage reporter consumes the source-owned demand selectors.

## Existing Yeni learner-facing standards

Before writing or changing any learner-facing content, read the existing Yeni
guidelines listed below. Use them while drafting the question, reference answer,
worked steps and diagram labels. Write text, mathematics and physical units
explicitly in their intended forms, and use the established presentation
components. Checks verify this authored output; they do not establish its style
after writing.

Author and review Workbench content against the existing guidelines in the
`yyeni` application repository. These are the authority; do not create a parallel
wording, mathematics or worked-example standard:

- `docs/conventions/ui-language.md`
- `docs/conventions/ai-generated-output-formatting.md`
- `docs/conventions/latex-generation-and-rendering.md`
- `docs/conventions/maths-workbench-question-acceptance.md`
- `services/api/services/math_formatting_instructions.py::LATEX_FORMATTING_INSTRUCTION`

Use the shared instruction in any AI prompt that authors mathematical learner
content. Deterministic recipes must follow the same output conventions. Check
plain language, explicit mathematical notation, upright physical units, meaningful
action/reason/result steps and the actual learner rendering. Use the existing
Workbench renderer and saved-instance answer authority. Successful parsing alone
is insufficient. Legacy display repair is compatibility work; future authored
content should make its text, mathematics and units explicit.

## Edit, check, update the app

Use Python 3.12. For generation, install `sympy==1.13.3` and `numpy==2.2.6`;
image preparation uses Pillow and a supplied font; optional PDF diagram
rendering uses `reportlab==4.4.3`, matching the current API requirements. The
package tools themselves use only Python's standard library.

From the resources repo:

```bash
# Check the saved source package.
python work/namibia-nssco-6131/workbench/tools/package.py verify

# After deliberately editing/rebuilding source files, update the file list/hashes.
python work/namibia-nssco-6131/workbench/tools/package.py seal

# Update an inactive application checkout, then check that it matches.
python work/namibia-nssco-6131/workbench/tools/package.py export --target /path/to/yyeni
python work/namibia-nssco-6131/workbench/tools/package.py check --target /path/to/yyeni
```

For bank/catalogue rebuilds, run the existing scripts in `package/services/api/scripts/`.
That folder now also includes the graph/visual preparation scripts, their PNG
renderer and the compact display-refresh tool. Review-packet assembly and
application-wide coverage reporting remain application-side integration tools.
Set `PYTHONPATH` to `package/services/api` when generating directly from this source.
The bank builder's coverage/review claims remain candidate claims. Do not replace a
reviewed bank merely to change its location. Keep IDs, versions and historical
snapshots stable; changing question content requires the usual content review.

The export checks every file first. It refuses conflicting application edits and
requires an explicit exact `--remove PATH` list to delete previously deployed
files. Without that list, deletions are refused. It updates the app lock at
`services/api/data/resource_packages/namibia-nssco-6131.lock.json`. It never contacts
GitHub, imports cards into a database, assigns learners or restarts a server.
Export is a checkout operation, not a live update; individual file writes are atomic,
but the multi-file export must finish before the checkout is deployed.

In the application, run:

```bash
python services/api/scripts/verify_workbench_resources.py
```

This check also runs as a required-to-pass step in the backend CI job. Review the
source changes, manifest and app lock together. Before a shared release, commit
both repositories and record the resources commit in the release notes; the
manifest checksum already pins the exact local package contents.

## Next: audit before cleanup

The initial audit is recorded in
`operations/review/namibia-nssco-6131-resource-audit-2026-11-03.md` at the repo root.
The later explicit deletion instruction supersedes its advice to retain the
3,300-card source bank: that bank and its dependencies have now been removed.
The subsequent Workbench-only cleanup removed the six rejected graph types and
duplicates, archived the static-card experiment and superseded documents, removed
15 broken extract links and repaired 15 evidence links. No learner database rows
were deleted. Known exact-replay failures from display caches are resolved by
verifying raw evidence separately while preserving old saved hashes.

Future subjects get their own qualification/syllabus package in their existing
workspace. NSSCAS Maths must not reuse NSSCO Maths as its subject bank. Chemistry,
Physics and Accounting require their own reviewed recipes and marking rules.
The app's future subject-provider interface is planned, not enabled by this move.
