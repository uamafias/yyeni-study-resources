# NSSCAS Mathematics 8227 — Stage-E candidate

Owner Vitalis, NIED December 2020 syllabus, Grade 12. Native recipe version 0.1.5; approved design/rubric identity 0.1.4.
Nine purpose-built recipes, 14 branch selections. Stage-D design is approved;
Stage-E generated content awaits cross-vendor acceptance. This is not installed.

The provider is a resource implementation under the existing YYeni package tools.
It has no application, database, network, learner-attempt or billing dependency.
The app owns authorisation, attempts, scoring orchestration and progress.

`catalogue-native.json` preserves the complete educational contract, part Bloom
rationales, objective/demand roles, branch-specific source references and honest
capacity bounds. `recipes.json` is the deliberately limited provider-v1 transport
catalogue. Its integer revision **2 maps exactly to native 0.1.5**. It is never a
floating point encoding of a semantic version. Future changes must preserve old
mapping/snapshots or use a new immutable package.

`generate(selection, 2, seed)` chooses one admitted parameter row using an isolated
seeded random instance. `generate_at` replays a known finite-domain row. Neither
method alone promises freshness. `generate_fresh` checks every required freshness
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

## E1 version, exposure and display boundary

Output-affecting E1 repairs use native/package 0.1.5 and transport revision 2.
The reviewed 0.1.4/revision 1 candidate remains immutable at
`../candidates/fcd4b71e07baa07a/`; it is never reinterpreted by the new provider.
Approved criterion IDs (including their 0.1.4 rubric segment), Bloom version,
parameters, dependencies and owner scores stay unchanged. No attempts exist.

`freshness_required_keys` decides whether an instance is fresh; `exposure_keys`
records what its question/solution exposes. Gradient-only instances also expose
the shared implicit proof without requiring that proof to be fresh. A later normal
proof with that identity is blocked. Reverse-direction gradient freshness retains
the approved bound of 23; normal retains 8. The app records exposure at the appropriate
question/example/solution event and reserves required keys atomically.

Learner mixed-motion selection/part IDs use the outcome-neutral `quadratic-motion`
alias; native/teacher/marking identities keep the historical branch ID.
`native_identity(question,public_id)` resolves only IDs belonging to that frozen
question; the app must preserve this mapping when saving submissions. Teacher
references are displayable original/same-type references only, with safe locators;
held/related refs and internal paths, hashes and reviewer annotations stay private.
