# Technical appendix — unvalidated targets

This appendix is separate from the accepted learning design. It records unfinished
local implementation and future operational evidence. Do not execute the examples
as an approved runbook, publish a package or restart engineering from reading it.
The document-only closure review was subsequently authorized and completed on
7 November; it did not validate this appendix. Platform engineering remains on hold.

## Ownership and release target

Resources owns recipes, generators, banks, subject guidance/marking, evidence,
assets and content review. Yeni owns authorization, assignments, database/media
integration, grading orchestration, UI, reporting and environment-specific mappings.
Do not copy subject content into app source. Source-only providers are trusted
software dependencies with isolated namespaces, not an operating-system sandbox.

A reviewed release should be immutable and explicitly selected by exact repository
revision/registry/manifest/dependency digests. Candidate, held and retired content
must not become assignable from a folder or author-written approval flag. Approval
is a recorded independent act bound to exact inputs and release scope. Runtime
must not fetch dependencies or content automatically.

The partial implementation still has review findings in startup isolation,
verification-path consistency, self-attested approval, descriptor validation,
mapping/history behavior, subject-neutral prompts, assets and CI. This playbook
does not claim those fixed. Preserve existing source/application copies and old
review evidence pending an authorized usage/ownership cleanup.

## Authoring records vs machine package

The Markdown [templates](templates.md) are the authoritative design record shapes.
The partial CLI instead expects a `package-definition.json` and `source/` for
build-candidate, with a provider, recipe definitions, rules and provenance. A validated
translation/contract between design records and machine inputs remains to be proven;
do not pretend passing a Markdown work order into the CLI validates it.

Provider target operations are describe/list_recipes/generate/validate_instance/
resolve_asset, with deterministic identity/version/seed output and bound private
marking evidence. Data paths, imports, hashes, dependency closure, public/private
fields and instance/role asset authorization need integrity checks before activation.
New arbitrary recipe/asset/module paths must never come from a learner request.

## Local draft command shapes

The module exists locally; these are inspected argument shapes only, NOT verified
tool behavior. Use a selected development checkout and an explicitly reviewed
tool revision if later authorized to validate it. Never point at production.

```text
python -m yyeni_workbench_tools --app-root <development-checkout> build-candidate <WB> --output <new-candidate-directory>
python -m yyeni_workbench_tools --app-root <development-checkout> validate <sealed-candidate-directory>
python -m yyeni_workbench_tools --app-root <development-checkout> check <sealed-candidate-directory> --report <check-report.json>
python -m yyeni_workbench_tools --app-root <development-checkout> what-to-fix <check-report.json>
```

The older Maths `work/namibia-nssco-6131/workbench/tools/package.py` also exists.
Its verification behavior has not been rerun for this documentation pass; it cannot
certify content truth or generic Workbench acceptance. Its export belongs to the
old copied-deployment workflow, not the desired new activation process.

## Evidence required before operational use

1. Make the author/build/check/report interface agree with the design records;
   provide --help, honest gate names, nonzero blocking exits and reproducible reports.
2. Fix and independently review the previously identified platform/tool defects;
   establish consistent verification and explicit independent approval records.
3. Verify exact external resource installation and all recipe/asset/module origins
   in a clean environment with no fallback to copied app banks.
4. Prove authorized classroom/lesson catalogues and assignment, stale/forged request
   rejection, practice/test grading and history with real bounded subject content.
5. Replay Maths compatibility evidence; test missing/damaged/retired resources,
   active saved work, version policy and rollback. Invalid updates must not damage
   the previous release or prevent unrelated API work.
6. Make CI actually enforce the selected resource chain and critical tests. Private
   cross-repo access/configuration must be explicit and must not expose credentials.
7. Write and rehearse exact publish/install/restart/rollback commands for the chosen
   environment, including any actual migration requirements and ordering. No model
   change or database migration is authorized by this document alone.

Keep committed/published, installed/activated and independently approved as separate
states. A second-subject provider with renaming-only data is not a real proof; a
bounded source-backed pilot must exercise differing subject rules through the
same supported platform. Missing shared capabilities must follow owner escalation.
