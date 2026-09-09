# CR-002 — `objective_registry` cannot record exam exposure

**Raised:** 2026-08-31, applying the exposure decision to the 9609 AS build.
**Status:** proposed. Worked around with a sidecar file so the pilot can proceed.

## The problem

`objective_registry.schema.json` sets `additionalProperties: false` on each objective, with a fixed property list. There is no field for what the assessment evidence says about an objective, so `exam_exposure` cannot be stored where it belongs — on the objective it describes.

This is the third schema limitation the pilot has surfaced, and all three have the same shape: the schema models the *plan* well and the *evidence about the plan* not at all.

| Found at | Artifact | Limitation |
|---|---|---|
| Stage 2 | `build_manifest` | Cannot express a pre-authoring build; `content_units` and `learning_items` require `minItems: 1` |
| Stage 2 | `assessment_evidence` | Cannot record why a map is unavailable or what is missing |
| Stage 2 | `source_inventory` | No resolvable `path` distinct from `original_filename` |
| **Stage 4** | **`objective_registry`** | **No field for exposure, evidence count or observed tariff** |

## Workaround in use

`work/cie-9609-as-2026-2028/curriculum/exam-exposure.json`, keyed by `objective_id`, carrying exposure class, evidence counts, observed maximum tariff, observed command words, item allocation, required subtypes and review-set membership.

It works, but it splits one fact about an objective across two files, and nothing enforces that they stay in step.

## Proposed addition to `objective_registry.schema.json`

```json
"exam_exposure": {
  "type": ["object", "null"],
  "additionalProperties": false,
  "required": ["class", "evidence_window"],
  "properties": {
    "class": { "type": "string",
      "enum": ["probed_high", "probed_low", "unprobed", "unmeasured"] },
    "evidence_window": { "type": "string" },
    "question_parts": { "type": ["integer", "null"], "minimum": 0 },
    "distinct_series": { "type": ["integer", "null"], "minimum": 0 },
    "max_mark_tariff": { "type": ["integer", "null"], "minimum": 0 },
    "observed_command_words": { "type": "array", "items": { "type": "string" } },
    "review_sets": { "type": "array", "items": { "type": "string" } }
  }
}
```

Optional, so existing registries stay valid.

## Why it belongs in the schema

Three deterministic checks become possible, and none can be written today:

- **C8 — coverage floor.** Every objective with `class: unprobed` still has at least two learning items. This is what stops an evidence-led pipeline from quietly starving mandatory content, and it is the machine-readable form of RS-05's rule that frequency must not weaken coverage.
- **C9 — exposure freshness.** `evidence_window` must include the most recent completed series. Catches a build resting on a stale probe.
- **C10 — allocation consistency.** An objective classed `probed_high` must carry at least one AO3 and one AO4 item; one classed `probed_low` must not carry more items than the budget rule allows.

## Note on the class names

The pilot uses `unprobed_2020_2025` rather than `unprobed`, because the window matters and a bare `unprobed` invites reading absence as a property of the concept rather than of the evidence. The schema keeps `class` and `evidence_window` separate, which is the better structure — the pilot's sidecar should follow it when the field lands.
