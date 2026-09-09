# Why there is no build manifest yet

`build_manifest.schema.json` cannot represent this build's state, so creating a manifest now would mean inventing content that does not exist. `stage-state.json` in this folder records the state instead.

The schema requires all of the following:

- `content_units` — array, `minItems: 1`
- `learning_items` — array, `minItems: 1`
- `objective_registry`, `claim_ledger`, `qa_report` — required path strings

None of these exist after pipeline Stage 2 (source ingestion and triage). The earliest point at which a schema-valid manifest can exist is after Stage 13 (learning-item generation).

`PIPELINE.md` defines the build states `INVENTORIED`, `MAPPED` and `PLANNED`, all of which precede Stage 11. **None of those three states can be recorded in a build manifest under the current schema**, even though `RS-32` requires every release to have one and the pipeline treats the manifest as the place where the topic contract lives (Stage 5).

## Recommendation for standard v1.0

One of:

1. relax `content_units` and `learning_items` to allow empty arrays when `status` is `draft`, and allow `null` for artifact paths that do not yet exist; or
2. add a `pipeline_state` field so a manifest can legitimately describe a pre-authoring build; or
3. define a separate, lighter `build_state` artifact for stages 1–10 and require the full manifest only from Stage 14 onward.

Option 1 is the smallest change and keeps one artifact for the whole lifecycle.

## Current state

- pipeline state: `INVENTORIED`
- publication: **BLOCKED** under RS-31 (assessment mining incomplete, no semantic review, objective registry not built)
