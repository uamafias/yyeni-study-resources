# NSSCAS Mathematics 8227 — Stage-E candidate

Owner Vitalis, NIED December 2020 syllabus, Grade 12. Native recipe version 0.1.4.
Nine purpose-built recipes, 14 branch selections. Stage-D design is approved;
Stage-E generated content awaits cross-vendor acceptance. This is not installed.

The provider is a resource implementation under the existing YYeni package tools.
It has no application, database, network, learner-attempt or billing dependency.
The app owns authorisation, attempts, scoring orchestration and progress.

`catalogue-native.json` preserves the complete educational contract, part Bloom
rationales, objective/demand roles, branch-specific source references and honest
capacity bounds. `recipes.json` is the deliberately limited provider-v1 transport
catalogue. Its integer revision **1 maps exactly to native 0.1.4**. It is never a
floating point encoding of a semantic version. Future changes must preserve old
mapping/snapshots or use a new immutable package.

`generate(selection, 1, seed)` chooses one admitted parameter row using an isolated
seeded random instance. `generate_at` replays a known finite-domain row. Neither
method alone promises freshness. `generate_fresh` checks every assessed exposure
key and terminates with `exhausted` when none is fresh. Explicitly repeated
practice is labelled; tests cannot repeat. Shared-model and subpart exclusions
cross branch/version boundaries; the app must reserve keys atomically per learner.
No learner state is stored here. Raw row counts are not distinct fresh capacity.

Every generated private question contains frozen question/solution/criteria,
canonical answers, meaningful action/reason/result steps, practice guidance,
reproducible parameters, native marking evidence and a v1 structural memo. The
native memo keeps visual marking references and all part/alternative/FT details
as structured data. The v1 bridge cannot certify that a learner marker consumes
those fields. It must not be activated as a complete marking integration without
the application acceptance checks in `../app-change-handoff.md`.

`learner_projection` preserves authored part identities and part-scoped references,
removes private answers/parameters/criteria, and separates practice, test and reveal.
`teacher_projection` provides educational evidence. These are projection helpers;
caller permissions and test-submission/reveal state remain application-owned.
`resolve_asset` implements the sealed v1 file lookup. Callers must additionally
bind it through `asset_for_instance` and actual application authorisation.
Question and solution SVGs come from the same parameter record and are sealed by
hash. No source artwork or Flashcard Studio content is copied.

Textbook originals remain internal. Attributed examination references retain
branch/part scope; related or held references cannot appear in the learner helper.
Default trapezium generation excludes h=2 original sketch subtasks. This candidate
does not implement an original-question browsing mode or learner assignment.

Authoring and independent recomputation commands, fixtures and scope limitations
are documented in `../authoring/README.md`. A structural pass is not educational,
visual-response, website, MCP or production acceptance.
