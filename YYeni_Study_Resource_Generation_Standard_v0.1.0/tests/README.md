# Test Suite

The test suite deliberately separates **deterministic validation** from **semantic judgement**.

## Deterministic checks included

- every JSON Schema is itself valid;
- the supplied Business and Cambridge 9609 profiles validate;
- the demonstration project validates end to end;
- IDs are unique;
- references between objectives, claims, content units, and learning items resolve;
- mandatory objectives have content and at least one learning item;
- publishable claims have required verification;
- generated claims have evidence or a verified derivation;
- duplicate source hashes are explicitly handled;
- core content remains within the selected level;
- enrichment is not embedded in core units;
- major objectives include worked application;
- exact duplicate prompts are blocked;
- near-duplicate prompts are flagged;
- recorded metrics match counts calculated from the final structured artifacts;
- approved and published builds satisfy stricter release conditions.

## What code should not pretend to judge

The script cannot reliably decide whether:

- a definition is conceptually excellent;
- an application genuinely uses the most important case facts;
- an analysis chain is economically or behaviourally persuasive;
- an evaluation weighs the right criteria;
- the resource is accessible to the intended learner;
- a source has been interpreted fairly.

Those checks belong to independent semantic reviewers using `prompts/SEMANTIC_REVIEW_PROTOCOL.md` and reporting issues through `qa_report.schema.json`.

## Run

```bash
python3 validate_project.py tests/fixtures/valid_project/build_manifest.json
pytest -q
```

Use `--strict-warnings` when a release policy treats warnings as blockers:

```bash
python3 validate_project.py path/to/build_manifest.json --strict-warnings
```

## Demonstration fixture

`fixtures/valid_project` is intentionally a **draft** build. It passes structural validation but its QA report correctly holds publication because assessment mining and independent review have not been completed. A valid data structure is not automatically a publishable educational resource.
