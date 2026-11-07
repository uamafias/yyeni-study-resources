# Yeni learner-facing guideline references

The governing instructions come from Yeni, not a new Workbench prompt standard.
These byte-identical snapshots were generated from the local app checkout on
7 November 2026 so resource authors can read the same authority offline. They
are not proof that those local bytes are published or deployed. Exact source paths
and SHA-256 values are in [provenance.json](provenance.json).

| Read | Source in Yeni | Use |
|---|---|---|
| [UI language](ui-language.md) | `docs/conventions/ui-language.md` | Plain language, meaningful labels and no model/provider names |
| [AI output](ai-generated-output-formatting.md) | `docs/conventions/ai-generated-output-formatting.md` | Generation, defensive parsing, private metadata and safe rendering |
| [Maths/science notation and rendering](latex-generation-and-rendering.md) | `docs/conventions/latex-generation-and-rendering.md` | Markdown/LaTeX syntax, escaping, meaningful steps, tables/units and existing gaps |
| [Shared instruction source snapshot](shared-formatting-instruction-source.txt) | `services/api/services/math_formatting_instructions.py::LATEX_FORMATTING_INSTRUCTION` | Exact shared AI generation authority; this archived source is not an executable dependency |
| [Existing feedback contract snapshot](existing-feedback-contract-source.txt) | `services/api/services/math_workbench/feedback_contract.py` | Preserve action/reason/result, first evidenced error, alternative-method and unresolved-evidence behavior |

Apply these at authored-template, generated-instance and feedback-generation time.
AI prompt builders reuse the selected shared instruction through the authorized
authoring interface; do not hand-copy and edit a local variant. Runtime subject
providers must not import Yeni's services/database to obtain the instruction.
If that interface is not available, record the tooling gap; design authoring can
still follow these references without claiming implemented prompt integration.

The shared constant has a known ambiguous “double backslash” sentence. Read the
notation reference sections 4 and 8.2: JSON source escaping and decoded Markdown
are different layers. Use a serializer, inspect decoded output, and preserve two
backslashes only for mathematical row breaks where needed. Do not silently edit
the snapshot or introduce another prompt constant to work around the ambiguity.
Future improvements belong in the shared Yeni authority with its parity checks.

Use clear English/British spelling, explanatory sentences and distinct equations.
Never wrap mathematics in Markdown emphasis. Keep currency literal, units correct,
parts/tables legible and internal fields/model names out of learner copy. Preserve
Workbench-specific names and mark display: Recall/Digital Practice Test conventions
in the broader references do not rename Workbench Test or impose a different mode.

These are preserved source documents, not locally rewritten guides. Links inside
the snapshots retain their original Yeni context; use this index for navigation.
On a guideline update, choose and record the new authoritative source revision,
regenerate byte-identical snapshots/provenance and review affected text/fixtures.
Do not independently edit snapshots. Renderer recovery does not certify source
compliance or permit alteration of saved mathematical evidence.
