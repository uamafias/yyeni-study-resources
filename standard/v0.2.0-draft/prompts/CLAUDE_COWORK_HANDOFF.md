# Draft Handoff Prompt for Claude Co-work

Use the attached `YYeni_Study_Resource_Generation_Standard_v0.1.0` package as the governing draft standard for organising and generating study resources.

## First task: inspect before changing anything

1. Read `RUNTIME_STANDARD.md` first.
2. Read the Business and Cambridge 9609 profiles in `profiles/`.
3. Inspect the current YYeni Study Resources project folder recursively.
4. Inventory all existing folders and files, detect duplicates, identify syllabus versions and subject coverage, and note files that are scans or have weak extraction.
5. Do not delete, rename, overwrite, or move existing content until you have produced a proposed migration plan and backup strategy.

## Then propose a folder architecture

The proposed structure must support:

- original source files;
- official syllabuses and assessment materials;
- source inventories;
- global objective registries and glossaries;
- qualification and subject profiles;
- topic workspaces;
- canonical claim ledgers;
- structured content units;
- flashcards and other learning items;
- deterministic and semantic QA reports;
- published learner resources;
- superseded versions and build manifests.

Separate immutable source material from generated working files and published releases.

## Required outputs before migration

Produce:

1. current-folder inventory;
2. duplicate and outdated-source report;
3. proposed target folder tree;
4. source-to-target migration map;
5. naming and versioning convention;
6. risks and unresolved questions;
7. staged migration plan;
8. validation plan using `validate_project.py` and the included schemas.

Wait for approval before performing destructive or large-scale moves.
