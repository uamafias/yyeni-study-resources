# Team Review Notes and Open Decisions

**Status:** Deliberately unresolved in version 0.1.0-draft.

The package is usable as a first automation standard, but the team should review the following policy choices before declaring version 1.0.

## 1. Human-review threshold

Current draft rule: unresolved, low-confidence, jurisdiction-specific, contested, medical, legal, or safety-sensitive claims require human approval.

Decision needed: should all `generated_gap` factual claims require human approval, or only those that fail automated external verification or exceed a risk threshold?

## 2. Approved source hierarchy

Decision needed: define a maintained whitelist or scoring policy for:

- official examination-board sources;
- endorsed textbooks;
- academic sources;
- professional bodies;
- teacher-created materials;
- open educational resources;
- web sources.

## 3. Assessment-material access

Decision needed: determine where past papers, mark schemes, examiner reports, and candidate responses will be stored and what copying, extraction, and quotation rules apply.

## 4. Depth ranges

Current draft uses four indicative tiers. The team should test them on several subjects and topics before fixing them.

Questions:

- Should depth be measured by words, content blocks, learner time, or all three?
- Should a master repository and learner-facing notes have separate depth limits?
- Should examination frequency influence practice quantity more than explanatory length?

## 5. Context-coverage policy for Business

Current draft requires at least one worked application for every major objective and contrasting contexts for decisions.

Decision needed: whether to require a minimum sector and business-size distribution per topic, per chapter, or per qualification.

## 6. Semantic-duplicate detection

Current test suite blocks exact normalised duplicate prompts and warns on high textual similarity.

Decision needed: select an embedding model and similarity threshold for production semantic deduplication, and define when intentional variants are allowed.

## 7. Reviewer roles and independence

Decision needed:

- minimum number of reviewer agents;
- whether one agent may perform more than one role;
- which reviews require a human subject expert;
- how disagreements are adjudicated.

## 8. Release states

Current states are draft, review, approved, published, and superseded.

Decision needed: whether YYeni also needs states such as pilot, teacher-approved, learner-tested, and production-ready.

## 9. Learner testing

The current standard includes reconstruction tests by an AI reviewer but does not yet require pilot testing with real learners.

Decision needed: define when comprehension checks, learner feedback, item difficulty data, or classroom trials become mandatory.

## 10. Folder architecture and migration

Do not finalise a project-wide folder system until Claude Co-work or another agent has inventoried the actual YYeni Study Resources folder. The migration plan should preserve source files, existing notes, and version history before reorganising them.

## 11. Namibian-context localisation for prose and worked examples

Current draft only has generic-international context vocabulary (sector, business size, ownership) for worked examples. RS-20 requires context that changes the reasoning, and a Namibian learner relates faster to Namibian-plausible scenarios (informal trade, communal farming, tourism/lodges, mining, fishing, parastatals) than to an unplaced "medium or large private business."

Decision needed: whether to add a maintained locale/context profile (same shape as `variant_register`, RS-35) supplying Namibian-relatable context facts, who maintains it, whether it's shared cross-subject or per-subject, and whether every core item needs a localised variant or only context-bearing items (case_analysis / worked_application-derived).

See `operations/standard-change-requests/CR-004-namibian-context-localisation.md` for the full writeup.
