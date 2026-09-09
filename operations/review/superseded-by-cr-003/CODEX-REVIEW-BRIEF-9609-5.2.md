# Codex review brief — Cambridge AS Business 9609, topic 5.2 Sources of finance

**Build:** `cie-9609-as-2026-2028` · **Topic:** 5.2 · **Standard:** YYeni Study Resource Generation Standard v0.1.0-draft
**Deterministic report:** `work/cie-9609-as-2026-2028/topics/5.2/qa_report.json` (`QA-9609-AS-5.2-r1`, schema-valid)
**Packet hashes:** `operations/review/packet-9609-5.2.sha256`
**Prepared:** 2026-09-08 · **Review decision required before anything in this topic may be published.**

---

## 1. What this review is, and what it is not

You are the independent semantic reviewer required by **RS-28**. The build is at state `AUTHORED`. It cannot reach `REVIEWED` without your report, and it cannot reach `APPROVED` at all until human decisions listed in §4 are made.

**You are not being asked to check counts.** Every mechanical property of this topic — coverage, referential integrity, duplication, AO mix, budget conformance, hashes — has already been computed by code and is recorded in `qa_report.json`. **RS-30** says mechanical claims must be confirmed by code rather than accepted from a reviewer, and the corollary holds too: do not spend the review re-counting what the code counted. If you believe a mechanical result is wrong, say so as an issue with the exact input that contradicts it, and it will be re-run.

**You are being asked the one question code cannot answer:** does this material actually teach Cambridge AS Business 9609 topic 5.2 to a learner who has no other source, and will a learner who masters it write credit-worthy answers in Papers 1 and 2?

Three things follow from that framing:

- **Do not review the notes alone.** A reviewer without the objective map cannot detect omission, which is the failure mode that matters most here. Read the objective registry branch first.
- **Judge against the syllabus, not against a textbook you know.** More content than the objective requires is a defect under this build's contract, not a bonus.
- **Report defects with evidence.** "This feels thin" is not reportable. "OBJ-9609-5.2.2-02-07 is taught in one sentence that gives the definition but not the mechanism, so a learner cannot answer the 3-mark Explain that this objective's command words predict" is.

---

## 2. The standard you are reviewing against

These are the rules the build was written to satisfy. Each is a thing you can find violated.

| Rule | What it requires | How it shows up in 5.2 |
|---|---|---|
| **RS-05** | Past-paper frequency may calibrate emphasis but **must not** weaken syllabus-mandated coverage | 7 of the 24 objectives are in the `rarely-examined` review set. They must be taught to full depth. Thin treatment of an unexamined objective is a **critical** issue, not a low one. |
| **RS-06** | Objectives are atomic; syllabus wording preserved | 14 internal/external source members were split out of two syllabus bullets. Check the split did not invent scope or lose a member. |
| **RS-07** | Bidirectional traceability | Every claim must be reachable from an objective and every content block from a claim. Code confirms the links exist; you judge whether the link is *meaningful*. |
| **RS-08** | One canonical definition per recurring term unless contextual variation is documented | Five cross-topic terms are flagged homonyms. Three appear in 5.2 and none has a canonical definition yet. |
| **RS-12** | Claims are evidence-backed | 60 of 63 claims are `generated_gap` — originally authored because no supplied source covers topic 5. Their evidence array is empty **by design**, not by omission. Judge whether each is *true and adequately verified*, not whether it has a citation. |
| **RS-13** | Generated-gap claims need documented human approval | Nothing here is approved yet. Your report is the input to that approval. |
| **RS-21** | Conditional causal language | An analysis chain that asserts an outcome rather than a conditional one is a defect. "This raises profit" is wrong; "if demand holds, this raises contribution and therefore profit" is right. |
| **RS-22** | Quantitative completeness | A calculation without interpretation is incomplete. 5.2 has no `Calculate` objective, so this rule bites only if quantitative material appears anyway. |
| **RS-23** | Jurisdiction awareness | 4 claims are jurisdiction-flagged. Learners are in **Namibia** sitting a **Cambridge** paper. A claim true of the UK and false of Namibia, stated unqualified, is a **critical** issue. |
| **RS-25** | Flashcard integrity | Prompt answerable from the prompt alone; canonical answer complete; no leakage. |
| **RS-30** | Mechanical claims verified by code | See §1. |

---

## 3. The review packet

All paths are relative to the repository root `YYeni Study Resources/`. Hashes are in `operations/review/packet-9609-5.2.sha256` — verify them before you start; a hash mismatch means you have been given the wrong version and the review is void.

**Scope and contract**

1. `work/cie-9609-as-2026-2028/qualification-profile.yaml`
2. `work/cie-9609-as-2026-2028/subject-profile.yaml`
3. `work/cie-9609-as-2026-2028/topics/5.2/contract.json` — the depth constraints, source permissions and gates this topic was authored under

**Curriculum**

4. `curriculum/objective_registry.json` — 295 entries; the 5.2 branch is 1 container + 24 assessable objectives
5. `curriculum/dependency_graph.json`
6. `curriculum/glossary.json` — the five homonyms
7. `curriculum/decomposition-decisions.json` — why 5.2.2's two bullets were split into 19 members

**Assessment**

8. `curriculum/assessment-framework.json` — AOs, verified paper structure, the nine command words with `used_at_as` flags and exact tariffs, the subtype→AO map, the item mix target and its hard rules
9. `curriculum/exam-exposure.json` — the five exposure classes and the rarely-examined review set
10. `curriculum/item-budget.json` — the bank locked at 889 items
11. `assessment-evidence/assessment_evidence.json` — status `partial`
12. `assessment-evidence/granularity-probe.json` — the Stage 4 finding on whether questions probe members or stay at bullet level
13. `assessment-evidence/examiner-findings-firstpass.json` — 766 examiner statements, not yet mapped to objectives

**Sources**

14. `inventory/source_inventory.json` — 378 sources

**The material under review**

15. `topics/5.2/claims/canonical_claim_ledger.json` — 63 claims
16. `topics/5.2/content-units/CU-9609-5.2.1.json` (783 w)
17. `topics/5.2/content-units/CU-9609-5.2.2-INT.json` (793 w)
18. `topics/5.2/content-units/CU-9609-5.2.2-EXT.json` (1,739 w)
19. `topics/5.2/content-units/CU-9609-5.2.3-4.json` (1,042 w)
20. `topics/5.2/learning-items/topic_5.2_items.json` — 68 items
21. `topics/5.2/notes-5.2-sources-of-finance.md` — 4,606-word offline learner text
22. `topics/5.2/qa_report.json` — the deterministic report

### 3.1 Packet items that do not exist yet — **do not report these as content defects**

The protocol's required packet has twelve items. Four cannot be supplied and their absence is a build-state fact, already recorded as a blocker in `qa_report.json`:

- **Build manifest** — the `build_manifest` schema requires content units and learning items for the whole build; 1 of 19 topics is authored, so no manifest can validate. See `builds/NO-MANIFEST-YET.md`.
- **Source-to-objective adequacy map (Stage 8)** — not run. What exists instead is `source_coverage` on each objective: every one of the 24 is rated 0 / `generate_gap`.
- **Gap and repair plan (Stage 9)** — not run.
- **Exclusions and conflict-resolution log** — no exclusions were recorded during authoring.

Report the *consequences* of these gaps if you find them (for example, a claim whose truth you cannot check because no adequacy audit established what the sources actually said). Do not report the gaps themselves.

---

## 4. What the deterministic pass already found

25 checks ran. **22 pass. One fails. Two warn.** Full detail in `qa_report.json`. The three non-passes need your adjudication, because in each case the code can see the pattern but not the intent:

**D-12 — FAIL. Two item prompts instruct with `Justify`.**
`ITEM-9609-5.2-057-APP` ("…and justify the matching") and `ITEM-9609-5.2-065-DATA` ("…and justify your recommendation"). `Justify` is **retired at AS** — 22 occurrences 2020–2022, zero from 2023 — and the framework's own hard rule says do not generate AS items for it. Decide whether to rewrite both prompts to `Explain why` / `Evaluate`, and whether the answer models behind them are still right once the command word changes.

**D-17 — WARN. `OBJ-9609-5.2.4-01` carries no `APP` flashcard.**
It is depth tier 3, so the hard rule "every tier-3/4 objective carries at least one APP item with context facts that change the reasoning" applies. It does carry the topic's `data_response` and `case_analysis` items, which do supply such facts. Judge whether that satisfies the rule's intent or whether an APP card is genuinely missing.

**D-19 — WARN. "Cost of capital" appears in learner-facing prose.**
Once, in `CU-9609-5.2.2-EXT` and the notes, as a negation: "No cost of capital at all," describing grants and donation crowdfunding. Cost of capital is A Level. Judge whether introducing an A Level term in order to deny it helps or confuses an AS learner.

Everything else passed, including: all 24 assessable objectives covered by content, items and claims; zero dangling or orphan claim references; RS-25 integrity on all 64 flashcards; zero duplicate or near-duplicate prompts; AO mix 34/28/20/18 against a 30/30/20/20 target; all four content units inside budget; and the publication gate holding with 0 of 63 claims marked publishable.

---

## 5. Build-specific checks

These sit **on top of** the five standard reviewer roles in §6. They encode decisions specific to this build, and they are where a generic reviewer would miss the most.

### 5.1 Command words and tariffs — the six that exist at AS

Verified across all 42 papers from 2023–2025. Any material that trains a different shape is training the wrong answer.

| Command word | Exact tariff | Credit-worthy answer |
|---|---|---|
| Identify | **1** | Name or select. Nothing beyond naming earns credit. |
| Define | **2** | One canonical sentence of precise meaning. No example, no evaluation. |
| Explain | **3** | Point → reason or mechanism → relationship made clear → supported with evidence from the context. |
| Calculate | **3** | Formula, substitution, answer with units, then one sentence of interpretation. |
| Analyse | **5 or 8** | A chain: decision or condition → immediate effect → mechanism → measurable consequence → effect on an objective or stakeholder. Conditional language. No jump straight to profit. |
| Evaluate | **12** | Judgement + specific context + decisive criterion and reason + strongest counterargument + condition for success. "It depends" without saying what it depends on scores nothing. |

**`Assess`, `Advise` and `Justify` must not appear as instructions.** Assess and Advise: zero occurrences in 84 AS papers 2020–2025. Justify: retired after 2022. They appear in the syllabus command-word list only because that list also covers Papers 3 and 4.

**Watch the part-versus-question trap.** Paper 1 Section B essays are 20 marks *per question* = Analyse 8 + Evaluate 12. Paper 2 questions are 30 marks in exactly six parts: (a)(i) Identify 1, (a)(ii) Explain 3, (b)(i) Calculate 3, (b)(ii) Explain 3, (c) Analyse 8, (d) Evaluate 12. Any item whose marking guidance implies a 20-mark Evaluate or a 30-mark question part has the structure wrong.

### 5.2 Exposure is evidence, never priority

`exam-exposure.json` classes each objective by what 84 papers show. **RS-05 forbids using this to reduce coverage.** In 5.2, 22 of the 24 assessable objectives are mapped: 9 `probed_high`, 3 `probed_low`, 6 `unprobed_2020_2025`, 3 `unmeasured_bullet_level`, 1 `unmeasured_homonym_risk`. The two unmapped ones are the container bullets `OBJ-9609-5.2.2-01` and `-02`, whose members carry the mapping.

The build's position, and the one you are reviewing against: silence in six years of papers is **weak** evidence of low probability — roughly 165 question parts a year are drawn against 258 assessable objectives, so most objectives would be absent by arithmetic alone. Exposure therefore changes **item type**, never **item presence**. An unprobed objective still gets DEF and DIST items and still joins synoptic practice.

So: **an objective taught thinly because it has never been examined is a critical finding.** Check the 7 objectives in the `rarely-examined` review set specifically — the 6 unprobed members plus `OBJ-9609-5.2.2-01-05` (working capital), which is flagged for homonym risk rather than absence. Also check the converse — that the 9 `probed_high` objectives have not crowded the topic.

### 5.3 Scope discipline

The 5.2 contract excludes, as A Level content: **gearing ratios, capital structure, cost of capital, investment appraisal (NPV, DCF, payback)**. Working capital appears **only** as a source of finance; its management belongs to 5.1.2 and must not be taught here.

Both directions are defects. Content beyond the objective is out-of-scope (report as `curriculum`). Content short of the objective is omission (report as `curriculum`, higher severity).

### 5.4 Jurisdiction — RS-23

Learners are in Namibia; the paper is Cambridge International. Four claims are flagged. Look for finance claims that are silently UK-specific or silently Namibia-specific: overdraft norms, the availability of venture capital and business angels, government grant schemes, microfinance structures, stock-exchange listing routes, and what "the bank" will lend against.

The right form is a claim that holds generally, with the local variation named where it matters. A claim that is true in one jurisdiction and stated flatly is **critical**, because the learner will write it in an exam marked against an international standard.

### 5.5 RS-21 — conditional causal language

Every CHAIN and EVAL item, and every analysis passage in the notes, must reason conditionally. Flag any place where an effect is asserted as automatic. This is the single most common way a Business resource teaches a chain that examiners do not credit.

### 5.6 The five-part evaluation structure

Every EVAL item and every evaluation passage must reach: **judgement · specific context · decisive criterion with reason · strongest counterargument · condition under which it succeeds.** An evaluation that lists advantages and disadvantages and stops has not evaluated. Check all 12 EVAL items against all five parts and report which parts are missing where.

### 5.7 Homonyms — RS-08

Three flagged terms appear in 5.2 material. None has a canonical definition yet (`definition_status: pending_stage_10`). Where 5.2 uses one, judge whether the sense used is right for this topic and whether it will collide with the sense a learner meets elsewhere:

- **contribution** — costing term in 5.4 (selling price − variable cost) vs the ordinary sense
- **enterprise** — factor of production (1.1.1) vs the activity (1.1.2) vs "social enterprise"
- **growth** — business growth (1.3.3) vs market growth (3.1.3)
- **objectives** — business objectives (1.4) vs marketing objectives (3.1.1) vs the qualification's assessment objectives
- **promotion** — marketing promotion (3.3.5) vs employee promotion (2.2.4)

### 5.8 Original authoring — what "verify" means here

60 of 63 claims are `generated_gap`. No supplied source covers topic 5: the chapter notes track a superseded syllabus edition and have no chapter 5, and the only source with finance content is a condensed revision PDF with a partial text layer. Authoring against the syllabus was therefore the correct action, not a shortcut.

The consequence for you: **an empty `evidence` array is expected and is not itself a defect.** What you must judge instead, claim by claim, is (a) is it factually true, (b) is it within the objective's scope, (c) does it say enough that a learner is not left with a gap, and (d) does it say more than the objective requires. The user's authoring constraint was exactly this: *factual, aligned to the learning objective, sticking to it, not giving more information than the objective requires and not giving so little that something is left out.* Report each direction of that constraint separately — over-scope and under-scope are different repairs.

### 5.9 Notes ↔ flashcards ↔ content units must agree

The notes serve triple duty: source for the flashcards, offline study text when the YYeni platform is unavailable, and standalone learning text for a learner with nothing else. So check three-way consistency: a definition given one way in the notes and another on a card is a defect even when both are defensible; and any card whose answer cannot be reconstructed from the notes alone breaks the offline promise.

---

## 6. The five reviewer roles

Run these as separate passes. They find different things.

**1. Curriculum and omission** — correct board, version, level, route and topic scope; every mandatory objective adequately taught *and* practised; nothing covered only nominally; no out-of-level content presented as core; prerequisites and cross-topic terms handled consistently; nothing supplied was dropped without a recorded reason.

**2. Accuracy and evidence** — definitions, classifications, formulas, dates and factual relationships; whether generated claims are adequately verified; whether analytical inferences follow from their premises; whether legal and jurisdictional claims are properly qualified; whether contradictions between claims are resolved.

**3. Pedagogy and accessibility** — clarity for the intended learner; conceptual progression and prerequisite order; whether mechanisms are *explained* rather than listed; whether distinctions and misconceptions are taught explicitly; proportionality and cognitive load; examples, non-examples and worked steps; whether the learner could reconstruct the knowledge without the source notes.

**4. Assessment alignment** — alignment to AOs and command words; use of paper, mark-scheme and examiner-report evidence; genuine contextual application rather than an industry name dropped into a generic answer; causal validity of chains; decisiveness of evaluation; whether practice matches the paper formats and tariffs in §5.1.

**5. Learning-item integrity** — objective and claim mapping; atomicity and self-containment; answer completeness; prompt ambiguity or answer leakage; *semantic* duplication (the code caught only lexical); progression from recall to transfer; the balance of 64 flashcards against 4 performance items; one consistent item architecture across the topic.

### 6.1 Bidirectional audit — both directions, both required

1. **Objective → content.** For each of the 24 assessable objectives, name exactly where it is adequately taught and where it is practised. Code proved a link exists; you judge adequacy.
2. **Content → objective.** For each substantial block of the notes and content units, name the objective, prerequisite or approved enrichment that justifies its inclusion. A block that justifies nothing is scope creep.

### 6.2 Reconstruction test

Using **only** the generated resource — no outside knowledge, no textbook — construct answers to a representative sample:

- a 2-mark Define and a 1-mark Identify
- three 3-mark Explains across different objectives
- an 8-mark Analyse on an unfamiliar business
- a 12-mark Evaluate on source appropriateness
- one application to a context the material never mentions

Report every objective for which the resource does not contain enough knowledge or reasoning support to build a strong answer. **This is the highest-value part of the review**, because it is the only test that measures the resource the way a learner will use it.

---

## 7. How to report

### Issue format — required, one YAML block per issue

```yaml
issue_id: unique-id
severity: critical | high | medium | low
category: curriculum | accuracy | evidence | pedagogy | application | analysis | evaluation | quantitative | learning-item | coherence | publishing
affected_ids:
  - objective-or-claim-or-item-id
finding: precise description of the defect
evidence:
  - exact block, claim, card or line reference
educational_consequence: how this could affect learner understanding or exam performance
recommended_repair: specific corrective action
confidence: 0.0-1.0
status: open
```

Do not report unsupported impressions. Identify the exact defect and the exact evidence.

### Severity

- **Critical** — wrong syllabus scope; dangerous misinformation; materially wrong definition or formula; missing compulsory objective; unsupported factual claim that changes learner understanding; an unqualified jurisdiction-specific claim; a rarely-examined objective taught thinly.
- **High** — major omission; invalid causal reasoning; misleading evaluation; systematic application failure; a command word that does not exist at AS.
- **Medium** — limited example range; structural inconsistency; incomplete comparison; semantically repeated items.
- **Low** — wording, formatting, minor sequencing, non-blocking clarity.

### Decision

- **Pass** — no open critical, high or medium issues; low issues resolved or explicitly accepted.
- **Conditional pass** — only clearly bounded issues remain; publication stays blocked until they are resolved.
- **Reject** — any critical issue, any unresolved high issue, systematic failure, or inability to verify coverage.

Note that even a **Pass** does not release this topic. The RS-13 human approval of 60 generated-gap claims and the RS-23 jurisdiction decision on 4 claims are human decisions that sit outside this review.

### Output

Return **one file**: `operations/review/codex-review-9609-5.2.yaml`, containing

```yaml
review_id: SR-9609-5.2-CODEX
reviewer_role: <one of the five, or "combined">
packet_hash_verified: true | false
status: pass | conditional_pass | reject
coverage_confirmed: <how you verified the 24 objectives, in one paragraph>
reconstruction_test: <what you attempted and what failed, in one paragraph>
issues:
  - <issue blocks as above>
```

Its issue blocks drop straight into the `semantic_reviews` array of `qa_report.json`, which is why the field names must match exactly.

---

## 8. One honest caution

This topic was authored by the same system that assembled this brief. That is precisely why an independent reviewer is required, and it is also why the brief's own framing should not constrain you. **If you think a decision recorded here is wrong — the split into 19 members, the exposure position, the depth chosen, the 68-item allocation — say so as an issue against the decision rather than working around it.** A review that only finds defects the brief told it to look for has not been independent.
