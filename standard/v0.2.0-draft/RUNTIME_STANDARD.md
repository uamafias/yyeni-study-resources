# YYeni Study Resource Generation Runtime Standard

**Version:** 0.2.0-draft  
**Applies to:** All AI agents that plan, author, review, validate, or publish YYeni study resources.

## 1. Purpose

Generate syllabus-complete, assessment-aligned, pedagogically coherent study resources from an official syllabus and supporting materials. The syllabus defines the curriculum contract. Supporting notes are evidence to assess, not a quality ceiling. Missing content must be generated and verified. Weak or inaccurate content must be rewritten or replaced.

## 2. Normative terms

- **MUST** — non-negotiable. Failure blocks publication.
- **SHOULD** — expected unless a documented educational reason justifies another approach.
- **MAY** — optional enhancement.

## 3. Mandatory runtime rules

### Scope, planning, and inputs

**RS-01 — Whole-syllabus first.** The system MUST parse the entire official syllabus before drafting an individual topic. It must create a global objective registry, level boundaries, optional routes, recurring-concept registry, and dependency graph.

**RS-02 — Scope lock.** The system MUST record the board, qualification, subject, syllabus code, examination years, syllabus version, learner route, selected level, included topics, excluded topics, papers, and language before authoring begins.

**RS-03 — Qualification and subject profiles.** The system MUST load an approved qualification profile and subject profile. Board-specific assessment rules and subject-specific reasoning templates MUST NOT be hard-coded into the universal engine.

**RS-04 — Source triage before use.** Every supplied file MUST be inventoried, hashed, checked for duplicates, classified by authority and likely syllabus version, mapped to topics, and assessed for text, table, formula, diagram, and scan readability before content is extracted.

**RS-05 — Assessment-material mining.** Relevant specimen papers, past papers, mark schemes, candidate responses, and examiner reports MUST be mined when available. Results must be mapped to objective IDs, command words, mark tariffs, contexts, credit-worthy reasoning, and evidenced misconceptions. Past-paper frequency may calibrate emphasis but MUST NOT remove or weaken syllabus-mandated coverage.

### Curriculum decomposition and depth

**RS-06 — Atomic objectives.** Every syllabus bullet MUST be decomposed into atomic, assessable knowledge and skill objectives. Exact syllabus wording must be preserved internally.

**RS-07 — Bidirectional traceability.** Every mandatory objective MUST map to approved content and at least one suitable learning item. Every substantial content block and learning item MUST map back to a syllabus objective, necessary prerequisite, or separately labelled enrichment objective. A mapping counts only where the content or item actually teaches or practises the objective; see RS-40.

**RS-08 — Dependency-aware sequencing.** Objectives MUST be sequenced using the dependency graph. Recurring terms MUST inherit one canonical definition from the global glossary unless a documented subject reason requires a contextual variation.

**RS-09 — Proportionate depth.** Each objective MUST receive a depth tier based on conceptual complexity, likely mark tariff, assessment evidence, misconception risk, prerequisite importance, cross-topic reuse, and procedural or quantitative demands. “Comprehensive” MUST NOT mean unlimited length.

### Source adequacy and evidence

**RS-10 — Adequacy, not presence.** The system MUST score the supplied treatment of each objective for accuracy, completeness, clarity, assessment usefulness, and conceptual coherence. Mentioning a topic is not sufficient coverage.

**RS-11 — Explicit authoring action.** For each objective the system MUST select and record one action: retain, refine, synthesise, correct, regenerate, generate-gap, or exclude.

**RS-12 — Evidence-backed claims.** No factual claim may be published solely from model memory. Each canonical factual claim MUST be source-backed, verified externally against an approved authority, or derived transparently from verified premises.

**RS-13 — Generated-content control.** Generated-gap and generated-quality claims MUST carry provenance and verification status. Unresolved, low-confidence, jurisdiction-specific, contested, medical, legal, or safety-sensitive claims require human approval before publication.

**RS-14 — Source conflict resolution.** Conflicts MUST be classified as curricular, assessment-related, factual, terminological, or jurisdictional and resolved using the appropriate authority hierarchy. The conflict and resolution must remain in the audit trail.

**RS-15 — Core versus enrichment.** Core learner notes may contain only syllabus-required knowledge, necessary prerequisites, assessment support, and directly relevant explanation. Optional enrichment MUST be placed in a clearly separate appendix and MUST NOT automatically generate core flashcards or exam questions.

### Authoring and assessment alignment

**RS-16 — Canonical source of truth.** The system MUST author approved canonical claims and content units before generating the final Word document, flashcards, quizzes, or lessons. Published outputs must be derived from the same approved structured source.

**RS-17 — Objective-type templates.** Each objective MUST be classified by type, such as concept, process, method, comparison, theory, quantitative measure, practical skill, source analysis, speaking, writing, or performance. The content and learning-item format MUST match the objective type.

**RS-18 — Full understanding before retrieval.** Notes MUST establish meaning, mechanism, purpose, boundaries, relationships, and relevant misconceptions before retrieval items are generated.

**RS-19 — Subject-specific assessment skills.** Application, analysis, evaluation, calculation, practical performance, interpretation, or other assessed skills MUST follow the loaded subject and qualification profiles. Small factual objectives must not receive artificial evaluation merely to fill a template.

**RS-20 — Genuine context.** Examples and worked applications MUST use contextual facts that change or sharpen the reasoning. Merely naming a business or industry does not count as application.

**RS-21 — Accurate causal language.** Consequences MUST be expressed conditionally unless logically guaranteed. Analysis chains MUST include a defensible mechanism and must not jump automatically from an action to profit. Statements about what an independent third party will do — a lender, investor, buyer, supplier, employer, regulator or customer — MUST be expressed as likelihood with the reason behind it, never as certainty, and MUST NOT prescribe a provider's internal method unless that method is evidenced for the named context.

**RS-22 — Quantitative completeness.** Every required quantitative measure MUST include the formula, variable definitions, units, worked calculation, interpretation, comparison basis, limitations, and common errors.

**RS-23 — Jurisdiction awareness.** For international qualifications, exact legal rules MUST NOT be presented as universal. Notes must teach the general business or subject principle and identify when local law controls the detail.

### Learning items

**RS-24 — Appropriate item type.** The system MUST NOT force every objective into a flashcard. It must generate the activity type appropriate to the skill, including flashcards, calculations, worked examples, data-response tasks, essays, practical tasks, source analysis, listening, speaking, or writing activities.

**RS-25 — Flashcard integrity.** Flashcards MUST be atomic, self-contained, unambiguous, answerable from approved claims, and non-duplicative. Answers must be complete canonical statements rather than fragments.

**RS-26 — Unified architecture.** Each topic MUST use one consistent learning-item architecture. “Base” and “extension” banks may exist only as metadata or filtered views, not as inconsistent duplicate structures across objectives.

### Generalisation, variants and assessment claims (added in 0.2.0-draft)

**RS-33 — Bounded generality.** A claim MUST NOT assert exclusivity or universality — that a thing is available *only* from a list, that no party will ever act, that one option exceeds *any other*, that something *always* or *never* holds — unless the proposition is definitional, legally necessary, or arithmetically true. Where a bounded universal is genuinely correct, the claim MUST carry `generality: definitional | legal | arithmetic` recording why. Everything else is a tendency and MUST be written as one.

**RS-34 — Generalisations must survive their own members.** Any summary, family, taxonomy or mnemonic that groups several objectives or instruments MUST hold for every member it covers. The grouping MUST declare `generalisation_scope` listing the member objective IDs it claims to be true of. If any member contradicts the grouping, the grouping MUST be narrowed, qualified or removed — the exception MUST NOT simply be taught later in the same material.

**RS-35 — Variant completeness.** Where a syllabus term names an instrument, practice or process that exists in materially different forms, and the difference changes a learner-relevant consequence — repayment, ownership, obligation, risk, cost, entitlement, method — the material MUST name the forms and MUST condition every stated benefit and limitation on the form. Consequential variants are recorded per subject in the subject profile's `variant_register`, which is maintained by a human and is a required input to authoring.

**RS-36 — Assessment claims require assessment evidence.** Any statement about what examiners reward, what carries the most marks, what is most frequently asked, what a paper will contain, or what an answer must do to score MUST cite a mapped record in the assessment evidence artifact. Where the assessment evidence status is `partial` for the relevant objective, such statements MUST NOT appear in learner-facing material at all. An impression about assessment is not assessment evidence, and the system's own confidence is not a substitute for a mark scheme.

### Practice shape and answer structure (added in 0.2.0-draft)

**RS-37 — Command-word-shaped practice.** Every objective MUST carry at least one learning item whose prompt instructs with one of that objective's own command words, at that command word's tariff and in that command word's answer shape. An objective whose command words include an analysis or evaluation verb is not adequately practised by recall items, however many of them exist.

**RS-38 — Declared answer structures are enforced.** Where a subject or qualification profile declares the required parts of an answer for an item subtype, every item of that subtype MUST model all declared parts in its canonical answer and MUST name each part in its marking guidance. A subtype whose declared structure is not modelled MUST be reclassified rather than left mislabelled.

### Coherence of the derived set (added in 0.2.0-draft)

**RS-39 — Offline reconstructibility.** Every canonical answer MUST be derivable from the topic's own content units. Any mechanism, distinction, figure or piece of evidence an answer relies on MUST appear in a claim that a content-unit block also cites. A learning item MUST NOT be the sole place a learner meets an idea.

**RS-41 — Derived work goes stale when its source changes.** Every claim carries a `revision`. Every content block
and learning item records, in `claims_seen`, the revision of each claim it was authored against. When a claim's text
changes its revision MUST be bumped, and every block and item citing it is **stale** until it has been re-authored
against the new text and its `claims_seen` updated. A stale derivative blocks release. Correcting a claim is not a
repair; propagating the correction is.

A `claims_seen` stamp asserts that a human or agent re-read this artefact against the new claim text. It MUST be
accompanied by an `authored_hash` of the artefact's own text at the moment of stamping. Advancing `claims_seen`
without the artefact's text changing is a **bulk stamp**: it records a review that did not happen, and it defeats
the rule entirely. Bulk stamps MUST be detected and MUST block release. Where re-reading genuinely found nothing
to change, record that decision on the artefact rather than silently advancing the stamp.

**RS-40 — Meaningful traceability.** An item's or block's `objective_ids` MUST be limited to the objectives it actually teaches or practises. Coverage credit for an objective is granted only where the item or block cites at least one claim that also serves that objective. Breadth of mapping MUST NOT be used to manufacture coverage, and a shared item MUST NOT claim objectives it merely mentions.

### Review, validation, and release

**RS-27 — Deterministic QA.** Code MUST check schema validity, unique IDs, objective coverage, reference integrity, claim evidence, scope boundaries, duplicate items, metric accuracy, core/enrichment separation, and publication-state consistency.

**RS-28 — Independent semantic review.** A reviewer operating in a fresh context MUST assess curricular completeness, factual accuracy, conceptual clarity, application quality, causal validity, evaluation quality, accessibility, proportionality, and subject-specific pedagogy.

**RS-29 — Complete critic packet.** Reviewers MUST receive the original syllabus scope, objective registry, dependency graph, source inventory, source-to-objective map, adequacy audit, claim ledger, exclusions log, draft content, learning items, and deterministic QA results. Reviewing the final notes alone is insufficient.

**RS-30 — Evidence-bearing criticism.** Every critic issue MUST identify affected IDs, evidence location, severity, educational consequence, and recommended repair. Mechanical critic claims such as counts or duplicates MUST be verified by code.

**RS-42 — The release bar.** A topic is releasable when no critical and no high issue is open. Medium and low
issues are logged against the topic and cleared in a later maintenance pass; they do not block release. This is a
deliberate choice, recorded by Vitalis on 2026-09-08: a bar of "zero open issues" against an adversarial reviewer
does not converge, and a pipeline that cannot converge cannot run at scale. Every issue that ships open MUST remain
open in the qa report — released is not the same as resolved, and a released topic carries its debt visibly.

**RS-31 — Hard release gates.** A draft MUST NOT be published while any mandatory objective is missing, any critical factual or scope defect is unresolved, any publishable claim lacks required verification, any required reviewer has rejected the build, or any deterministic blocker remains.

**RS-32 — Reproducible release.** Every release MUST have a build manifest recording standard version, profile versions, syllabus version, source hashes, objective-map version, model or agent identifiers where available, counts calculated from the final artifact, QA results, output hashes, and release status.

## 4. Required project artifacts

A production build SHOULD contain at least:

1. qualification profile;
2. subject profile;
3. source inventory;
4. global objective registry and dependency graph;
5. assessment evidence map;
6. source adequacy and repair plan;
7. canonical claim ledger;
8. content units;
9. learning-item dataset;
10. deterministic QA report;
11. semantic critic reports;
12. build manifest; and
13. learner-facing publication artifacts.

## 5. Hard release blockers

Publication is blocked by any of the following:

- wrong syllabus version, route, or level;
- missing mandatory objective;
- out-of-level content presented as core;
- unresolved contradiction with a higher-authority source;
- unsupported factual claim marked publishable;
- formula, unit, or worked-answer error;
- learning item with an invalid claim or objective reference;
- exact duplicate learning items not intentionally tagged;
- critic rejection on curriculum, accuracy, or assessment alignment;
- final document not generated from the approved structured content;
- final metrics or output hashes not recorded;
- an unqualified universal or third-party-certainty claim in publishable material (RS-33, RS-21);
- an assessment-priority claim without mapped assessment evidence (RS-36);
- an objective with no command-word-shaped practice (RS-37);
- a canonical answer that cannot be reconstructed from the topic's content units (RS-39);
- coverage satisfied only by mappings that fail RS-40;
- any block or item left stale by a claim revision (RS-41).

## 6. Runtime completion statement

An agent may report a topic as complete only when all required artifacts exist, all deterministic checks pass, all mandatory semantic reviews pass, all blockers are resolved, and the final release is registered in the build manifest.
