# Examples

The executable demonstration project lives in `../tests/fixtures/valid_project` because it doubles as a test fixture.

It demonstrates the minimum relationships among:

```text
build_manifest
  -> qualification_profile
  -> subject_profile
  -> source_inventory
  -> objective_registry
  -> assessment_evidence
  -> canonical_claim_ledger
  -> content_units
  -> learning_items
  -> qa_report
```

The fixture is intentionally small and remains in `draft` status. It passes deterministic validation while publication remains on hold because assessment mining and independent semantic review are incomplete. This models an important distinction: structurally valid content is not automatically educationally approved.

## Suggested production topic workspace

```text
topic_workspace/
  build_manifest.json
  source_inventory.json
  objective_registry.json
  assessment_evidence.json
  source_adequacy_and_repair_plan.json
  canonical_claim_ledger.json
  content_units/
  learning_items/
  reviews/
  qa_report.json
  outputs/
```

The final project-wide folder system should be designed after inspecting the existing YYeni Study Resources folder. Do not impose this topic workspace blindly on legacy content.
