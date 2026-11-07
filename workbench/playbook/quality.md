# Workbench quality and acceptance

Learning requirements reflect Jeremy's accepted 7 November decisions. Claude's
7 November closure review closed F1–F12 with no blocking playbook gaps; the two
minor finalisation corrections are applied. See the [finalisation record](review/finalisation.json).
Operational checks below are release
requirements, not a claim that their tooling exists or has passed.

## Gates

Apply relevant gates to the exact declared scope. For each record method, inputs,
tool/source versions, result, output/evidence digest, reviewer where applicable,
and limitations. Missing applicable checks block the affected acceptance/release.
Genuine non-applicability is reasoned and reviewer-accepted, never counted as pass.

| Gate | Evidence needed | Blocking problem |
|---|---|---|
| Q01 Source authority | Exact current syllabus and corpus inventory, locators/hashes, edition/proof limits, rule provenance | Invented/mismatched authority, silent missing evidence or unsupported exam claims |
| Q02 Selection and coverage | Every screened demand/pattern disposition, grouped exclusion/zero record, hold/escalation log; selected demand → assessed part evidence | Omitted demands, false observed labels, unjustified exclusions/duplication, unreported gaps or invented coverage |
| Q03 Recipe contract | Stable IDs/versions, branches/domains/response types, intended capability checks | Undefined fields/branches, arbitrary executable selection or unsupported capabilities claimed supported |
| Q04 Subject truth | Independent recomputation, substitution/inverse/subject oracle and all branch examples | Incorrect answer, impossible data or contradiction between givens, working and result |
| Q05 Domain and termination | Admitted/rejected boundaries, feasibility/uniqueness, rejection bounds/exhaustion | Invalid/degenerate instances or unbounded generation |
| Q06 Fair marking | Award totals, dependencies, alternatives, answer-only/method rules, special-case precedence and sample response credit | Wrong credit, blanket no-working penalties, valid methods rejected or duplicate awards |
| Q07 Renewal and difficulty | Determinism, domain capacity, fingerprints/no-repeat scope, distribution and invariant-demand checks | Cosmetic freshness claims, hidden repeats/exhaustion or accidental changes to assessed decisions/difficulty |
| Q08 Economy and distinctness | Existing-recipe audit, discriminating decisions/representations, multipart/standalone and supporting-drill reasons | Inflated counts, automatic subpart/generator multiplication or retired work returning |
| Q09 Teaching and feedback | Action/reason/result solutions, answer-free support, sample response-specific repairs and fresh application | Unexplained working, generic/invented diagnosis, premature solution or helped repetition labelled mastery |
| Q10 Generation and presentation | Guideline revision, decoded template/instance/feedback samples and safe renderer evidence across question/example/feedback/history | Broken notation, hidden metadata, misleading labels, clipping or relying on cleanup as source compliance |
| Q11 Privacy and mode boundaries | Authorized learner/teacher payload/asset tests, per-instance role bindings and reveal timing | Private reference/seed/other learner data leaks or prohibited help before test submission |
| Q12 Release integrity | Sealed source/dependencies/assets, hashes, clean installation and namespace/failure checks | Changed/missing/unlisted executable/data assets, unsafe paths or unsupported dependencies |
| Q13 Independent review | Frozen scope, cross-vendor report, explicit disposition audit, repair acceptance and limitations | Self-approval, skipped exclusions/branches, open blockers or unreviewed later changes |
| Q14 Compatibility | Original snapshot/memo/assets, alias/retirement behavior, active rounds and version-policy evidence | Reinterpreted old attempts, broken history or silent fresh-question behavior changes |
| Q15 Original wording and assessment claims | Comparison of all learner-facing question/solution/support/feedback text against relevant paper/scheme/report corpus; source-backed claims | Copied examination prose, misleading predictions or claims about examiner rewards |

## Selection review, including zero output

Freeze selection/exclusion/hold records even when no content is authored. The
independent reviewer checks EVERY disposition against its evidence and the complete
syllabus screen, observed vs unobserved labels, capability evidence/notification,
supporting-drill need and separate-recipe decisions. Grouped exclusions are reviewed
as groups with coverage ranges, not silently skipped. A zero outcome gets a short
selection-only review, not generator/packaging tests for nonexistent content.
An owner confirmation does not substitute for that review. An in-scope capability
hold cannot be renamed “zero qualifying demands”. See [templates](templates.md).

Supporting-only practice does not earn direct coverage of a larger exam demand.
Syllabus-derived unobserved work needs the explicit label, proposed rules/marking,
owner acceptance and independent review; absence from papers alone is not evidence
that the syllabus demand is irrelevant. New-source evidence can reopen selections.

## Subject truth, marking and variation

Use an oracle separate from answer construction: substitute roots, independently
recalculate figures, check dimensions/physical feasibility, balance reactions or
accounting entries as appropriate. Calling the same answer builder twice proves
consistency/determinism only. A fluent explanation is not mathematical evidence.

Test admitted zero/negative/fractional/large/small boundaries where relevant,
denominator/log/root domains, geometry degeneracy, tied ranks, rounding transitions
and conflicting data. Declare rejected cases. Domain reasons plus sampling are
needed for unbounded spaces; samples are never a proof of every seed.

Each work order declares:

- What a correct final answer alone demonstrates and whether method marks follow,
  with source evidence or explicit proposed rationale. No universal working penalty.
- Exact/rounded/unit requirements, intermediate rounding, alternatives, method
  restrictions only when asked, follow-through and caps/precedence for special cases.
- Allowed variant domains and fixed learner decisions; corpus-calibrated numerical,
  data-size and geometric complexity bounds. Author-chosen illustration bounds are
  labelled and need subject-corpus calibration before release.
- Connected-part dependencies and the evidence each part directly assesses; tagging
  an objective because its topic appears is not coverage.

Baseline engineering test targets when implemented: deterministic replay at seeds
0, 1, 42 and `2**63 - 1`, targeted boundary seeds and at least 64 valid draws per
structural branch. Exhaust finite banks/small spaces when feasible and declare the
enumeration cutoff. Replay saved release fixtures. Report actual branch/seed counts,
untested space and added risk-specific reasoning; these targets are not learning
effectiveness claims. Exact fingerprints and structural-demand comparison serve
different purposes; neither title similarity nor a repeated answer alone proves duplication.

## Learner-facing text at generation

Use the pinned [Yeni guideline references](guidelines/README.md) during authoring,
instance generation and later feedback generation. AI prompts reuse the shared
instruction, not local forks. Inspect actual decoded Markdown/LaTeX and safely
render all surfaces. No emphasis around maths, transport/schema leaks, arbitrary
HTML/images, model/provider names or unexplained jumps. Distinguish valid JSON
escaping from decoded mathematical backslashes; use serializers, not blind repeated
unescaping. Formatting must not change values, units or saved evidence.

Meaningful steps explain action, reason and result; step count is not mark count.
Keep short feedback, learner submission, authored repair and full canonical answer
distinct. Valid alternatives receive memo credit. Full-credit work gets no invented
repair; unresolved evidence requests clarification, with no fabricated mark/error.

Practice can support the attempt but must not reveal the current solution before
submission. Test retains question-by-question post-submission review and timing;
no practice support while answering an unsubmitted question. A later same-recipe
question after feedback is an after-feedback observation. Preserve the stronger
existing protections in [preservation.md](preservation.md).

## Q15 copied wording and claims

Mine examination demand, not sentences. Compare learner text (including solutions,
hints and generated feedback) with the relevant papers, schemes and reports;
do not pass the syllabus as copied-assessment prose. Under the team policy, runs
of 12+ identical words require repair, with only documented standard-definition,
formula or necessary-terminology exceptions accepted by the reviewer. Review 8–11
word runs manually and rewrite copied examination phrasing; record allowed cases.
Do not reword mathematical command terminology into inaccurate synonyms to evade a check.

Do not put “examiners reward” or promises about what an exam will contain into
learner copy. Internal claims about observed structure/frequency need cited evidence;
source analysis may quote privately with locators, not leak those passages into cards.
The existing copied-wording checker has not been validated as complete for
Workbench templates/runtime feedback: document tool limits and use scoped manual
comparison when necessary. A tool that scans only stored notes does not prove
runtime feedback compliant. This gate must appear in the F-stage author report.

## Review, repairs and release records

Cross-vendor AI review suffices; teacher acceptance is optional. Record authorship
and independence for the affected scope. Review the frozen sources, selection,
code, dependencies, branch fixtures, renders, check reports and historical findings.
Disclose exactly what was read/recomputed/tested. If evidence remains uncertain,
escalate to Jeremy/Vitalis; confidence or an owner tick cannot replace missing facts.

Critical/high defects in truth, marking, privacy, saved evidence or main workflow
block release. Medium defects affecting scope, branches, variation or teaching also
block affected content. Cosmetic-only deferrals need reviewer acceptance, reason,
owner and action; a tiny sign/unit change that changes meaning is not cosmetic.
Use the [finding ledger](templates.md#finding-and-author-report-records).

Repairs update authoritative content, bump output-affecting versions, retain old
review evidence, rerun affected checks and undergo independent closure. Never mark
an author's fix independently accepted. New changes reopen affected acceptance.

Record separately: owner design approval, author gate results, independent
selection/content scope/digest, publication and named-environment activation.
Enabled recipe versions must match accepted bytes, with no open blockers and
disclosed held gaps. Technical self-attestation is not independent review.
Whole-subject acceptance cannot be inferred from a pilot or migration checks.
