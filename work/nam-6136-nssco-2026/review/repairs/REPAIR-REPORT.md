# Codex repairs after Claude’s whole-subject review

Jeremy authorised repairs after Claude’s **FIX CONTENT BEFORE PUBLICATION** verdict. Codex applied them across the completed subject. No further Claude call, web research, publication, commit, push or platform import was made.

The original [Claude report](../CLAUDE-RESOURCE-REVIEW.md) remains unchanged. These dispositions are **Codex repair judgements**, not new independent approval. Claims remain unverified/non-publishable; resources remain review_required.

## Content findings

| Finding | Repair applied | Where |
|---|---|---|
| R6136-001 | Vision 2030 definition and 2004–2030 horizon; assessed description | 2.1 unit 01 and 001 |
| R6136-002 | HPP year, president, pillars and purpose; NDP5 goal-based evaluation | 2.2 unit 02 and 003/004/P01 |
| R6136-003 | Syllabus term restored; definition, GBV types, factors, effects and responses | 6.2 units 05–06, revision history and rewritten cards |
| R6136-004 | Distinct teaching sets for breadth gaps, including trade, aid and decentralisation | 1.1/1.2, 3.1, 4.1, 5.1, 6.2, 7.1–7.3, 8.1, 9.1–9.3, 10.1 |
| R6136-005 | Worked percentage change, percentage points, natural increase and per-thousand conversion | 7.2 unit 01; 7.1 unit 03 |
| R6136-006 | All 72 flagged templates individually rewritten with responsive answers | REWRITES in repair_resources.py; IDs in content-actions.json |
| R6136-007 | Three work categories reconciled; employed and unmet-need totals distinguished | 4.2-022 and notes example |
| R6136-008 | 32 evaluations rewritten with real merits/costs and developed conditional answers | EVALUATIONS in repair_resources.py; 7.3-006 describes both routes before judging |
| R6136-009 | Named Namibian/regional examples and historical mechanisms added; original industry names retained | 4.1, 5.1, 6.1, 6.2 and 9.3 |
| R6136-010 | Disease-route distinctions, immunisation purpose and delivery conditions taught | 7.2 unit 01; no clinical schedule |
| R6136-011 | All four Section B answer sets become own-enquiry scaffolds; personal-record template added | 10.1 P01–P04 and unit 12; old fictional answers retained only as audit history |
| R6136-012 | Sampling quantities supplied inline and exact package IDs given | 10.1 units 10–11 |
| R6136-013 | P02 whole defined as production cost and inference limit clarified; P03 journeys linked to schools | 10.1-P02 A2(3–4) and P03 stimulus |
| R6136-014 | Area examples use average income; unsafe-water wording corrected | 1.1 unit 04 and 017/P02 |
| R6136-015 | Repeated unit-end filler removed; woodland, irrigation and regional cases varied | 5.1-034/038, revised 4.1/9.3 cases and cross-link removal log |
| R6136-016 | Three misconception cards require applied separating tests | 9.1-031; 9.2-017/018 |
| R6136-017 | Existing dated official-source locators attached to relevant claim ledgers | Source blocks and ledger evidence; still unverified |

## Plan repairs

PL-1–PL-5 are addressed in `curriculum/post-resource-review-amendments.json` and the plan/handover. Eighty-two generic member titles were made specific, with two additional same-word targets kept distinct for their different contexts. Work-order displays were regenerated with the standard Markdown function. EVAL requirements now demand genuine trade-offs while retaining multi-point knowledge teaching. CALC requirements include prerequisite methods. Named examined examples remain required.

The compound command on 7.3-006 retains its metadata, describes both alternatives, then requires reasoned judgement. Its C14 incompatibility remains an owner issue. No silent metadata change was made.

All 356 targets, 543 slots, IDs, subtypes, AOs, Bloom labels, command metadata, tariffs and unit ceilings remain. Research P02 is correctly A1=20/A2=15; the others are A1=25/A2=10. Every package has A=35 and B=15. The review brief’s universal 25/10 assumption was wrong; P02’s authored total was correct.

## Learner tests repeated by Codex

**GBV/baby dumping (6.2.05–06):** the notes now supply the definition with lack of appropriate care and risk of harm, two or more GBV types, distinct contributing factors, personal/development effects and matched responses. The prior term-recognition and knowledge gaps are addressed. Cards 020/021/024/025 ask specific questions. This is a teaching-coverage judgement, not a promised examination score.

**Rural schemes (5.1.04):** the notes give at least six distinct cooperative benefits, named regional schemes and separate implementation barriers. Namibian land reform/resettlement and conservancies provide local context. Revised 024–030 evaluations give both options merits and costs. The production-versus-marketing distinction remains explicit.

**Calculation prerequisites:** 7.1 teaches birth-minus-death rates and 20 per thousand = 2%; 7.2 teaches change divided by the original value, works 80→100 and 100→80 separately, and distinguishes percentage points. Learners now have the methods required by 7.1-011 and 7.2-003/014.

## Verification

- All **18/18** check reports say `publish`, with **zero deterministic failures** and `what_to_fix` exit 0. This is a tool result, not learner-release approval.
- **749 claims, 101 units, 505 flashcards and 38 activities; 33,570 rendered-note words.** No upper ceiling exceeded.
- Exact slot/metadata audit: no missing, extra or mismatched items. Registry schema validates. The pre-existing subject-profile schema incompatibility remains open.
- **16 checks parse actual authored research inputs, answers and question tariffs**, including age-sex totals. Fixed-literal checks were removed. Three corrupted in-memory cases (output, pie angle, tariff) were correctly rejected; files were not mutated.
- Copied wording against 40 saved paper/report extracts: **zero 8+ and zero 12+ matches**; syllabus excluded. Exact matching does not prove semantic originality.
- Changed claim text has revision/history records, updated claims_seen and unchanged-text reviews where applicable. Previous artefact hashes are retained. Standard restamping and rendering completed.

## Standard/tool findings

| Finding | Disposition |
|---|---|
| T-1 | Open with standard owner. C35/C41/C43 are not_run. The stock no-graph explanation is incorrect for 7.1 and 10.1. Specifications are checked; no rendered-figure PASS claimed. |
| T-2 | Fixed locally: audit_research.py parses actual stimuli, answers and tariffs; audit_build.py consumes it. See authored-numerical-audit.json and numerical-audit-negative-checks.json. |
| T-3 | Open with standard owner: runner exit/JSON mismatch and stale subject-profile schema. standard/ is unchanged. |
| T-4 | AO allocations remain explicit planning judgements. The documented D relative shortfall remains; metadata cannot establish real demand. |
| T-5 | Claude found no causal error. The pronatalist comparison was nevertheless strengthened with two real support alternatives and fuller reasoning. |
| T-6 | Advisory minima remain advisory. Missing substance was added; word counts were not padded. |
| T-7 | Exact copied-wording tool limits remain visible; the rerun is not semantic-originality certification. |

## Reproduction and next state

The original author_topic.py files are pre-review manuscripts. Do not run them alone as current build sources. Run `review/repairs/repair_resources.py` to replay explicit repairs from the preserved pre-repair JSON baseline, then `planning/repair_review_demands.py`, standard restamping/rendering, `topics/audit_build.py` and the copied-wording scan. Repair scripts make no model or network calls.

The first repair set received a second whole-subject Claude review; its findings and Codex's subsequent repairs are recorded in `../CLAUDE-RESOURCE-REVIEW-2.md` and `SECOND-REPAIR-REPORT.md`. The second-review repairs have not been independently re-reviewed. Standard-owner fixes, publication, commit/push, pilot completion and YYeni replacement/import remain pending.
