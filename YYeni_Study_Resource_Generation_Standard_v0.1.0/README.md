# YYeni Study Resource Generation Standard

**Version:** 0.1.0-draft  
**Status:** Draft for team review  
**Purpose:** A reusable, auditable system for turning an official syllabus and supporting source materials into high-quality learner notes, retrieval items, examination practice, and publishing artifacts.

## What this package contains

- `RUNTIME_STANDARD.md` — the concise operative rules every generation agent must follow.
- `PIPELINE.md` — the end-to-end build process and release states.
- `profiles/business_subject_profile.yaml` — machine-readable subject rules for Business.
- `profiles/BUSINESS_SUBJECT_PROFILE.md` — the human-readable Business subject profile.
- `profiles/cambridge_9609_as_2026_2028.yaml` — qualification-specific settings for Cambridge International AS Level Business 9609, 2026–2028.
- `schemas/` — JSON Schemas for the principal project artifacts.
- `tests/` — deterministic validation tests, negative controls, and semantic-review guidance.
- `prompts/` — concise reviewer and handoff prompts.
- `examples/` — a minimal project skeleton and explanatory examples.

## Core architecture

The system separates three concerns:

1. **Universal engine** — scope control, source triage, objective decomposition, evidence mapping, authoring, review, and release.
2. **Qualification profile** — board, syllabus, examination route, papers, assessment objectives, command words, and level boundaries.
3. **Subject profile** — subject-specific reasoning patterns, application rules, quantitative requirements, learning-item shapes, and quality checks.

The learner-facing Word document is a publication artifact, not the master source of truth. The master source should be the structured objective, claim, content-unit, and learning-item files validated by this package.

## Recommended reading order for an AI agent

1. `RUNTIME_STANDARD.md`
2. `profiles/cambridge_9609_as_2026_2028.yaml`
3. `profiles/business_subject_profile.yaml`
4. `PIPELINE.md`
5. The relevant schemas for the stage being executed
6. `prompts/SEMANTIC_REVIEW_PROTOCOL.md` when reviewing a draft

## Quick validation

From this folder, run:

```bash
python3 validate_project.py tests/fixtures/valid_project/build_manifest.json
pytest -q
```

Dependencies are listed in `tests/requirements.txt`.

## Release philosophy

A resource is publishable only when:

- every mandatory syllabus objective is covered;
- factual claims are evidence-backed or approved after verification;
- application, analysis, and evaluation meet the subject profile;
- deterministic checks pass;
- independent semantic reviewers receive the original objective and evidence maps;
- no unresolved blocker remains; and
- the final artifact matches the approved structured build.

## Status of this version

This is the first implementation draft. It is intentionally structured so that Vitalis, the YYeni team, Codex, Claude Co-work, and subject experts can review individual rules without rewriting the whole system.
