# D4 confirmation findings: 8227 Workbench pilot PLAN

**Reviewer:** Claude Opus 5.5 (cross-vendor REVIEWER). **Date:** 2026-11-24.
**Inputs:** `inputs.json` (manifest `71ee10b6…`, content digest `d3f5676a…`, Git HEAD `fa0a09d4`).
**Baseline:** D3 manifest `4667a860…` and our D3 findings in `review/opus-5-5-d3-confirm/`.

## Method

- **Changed-scope only.** D3 → D4 changed 36 design files. D4 also added 66 `planning/d4` files, 13 `checks/plan-repair-d4-*` files, the D4 confirmation prompt and the D3 archive.
- **Five agents ran in parallel:** motion, shared rule and authority, calculus, trig/log, visual. Each was briefed to re-test with its own code and cases, never re-running Codex's scripts as an oracle. Their evidence is in `check-*.json`.
- **Totals:**

  | Check | Count | Outcome |
  |---|---|---|
  | Dispositions | 38 | 37 repaired, 1 partly (stale wording) |
  | Independent recomputations | 138 | 136 agree |
  | Marking tests | 52 | 49 as expected |
  | Capacity checks | 20 | all match |
  | Native pages rendered | 12 | — |

  The 5 mismatches are all findings below: calc-D4-01 (two), calc-D4-02, trig-D4-01 and shared-D4-01. Each comes from an undefined term in the proposed misread mechanics or a route the fixture does not name. None is a wrong design answer.
- **What I verified myself:**
  - the manifest and every pin;
  - the D3 recovery: 1,708 files, 0 mismatches;
  - the write scope;
  - the two-copy rebuild (`rebuild.json`);
  - every should-fix locator in the current bytes;
  - the MR03 / MR09 conflict against the D3 archive text;
  - the stationary deduction-slot wording;
  - the motion T 3→5 reasoning in the author script;
  - the PLAN:11 sweep error.

## A. Dispositions of the D3 findings

| D3 finding | Verdict | Evidence |
|---|---|---|
| **D3-S01: authority** | **repaired, with two residues** | **What holds:** <br>• The OD-6 row holds only the principle, and the separate MR03-OPS-D4 row is labelled proposed and pending (`OWNER-CHECKPOINT.md:43,44`). <br>• MR03 calls only the principle binding (`subject-rules.md:67`). <br>• The same split appears in `recipe-contract.md:301–303`, `HANDOVER.md:15` and the trig dispositions. <br>• The 21 register rows match `d4/deviation-register.json` cell for cell. <br>• Approval stays pending. <br>**Residues:** two body sentences still credit the per-datum unit to OD-6 (D4-S01). |
| **D3-S02: shared rule** | **repaired; the rule text needs two clarifications** | **What holds:** <br>• All nine work orders carry the identical shared line. <br>• All 27 policies, their pilot-design copies and their part-register copies match `shared-misread-policy.json`, including the feedback sentence. 13 lacked it in D3. <br>• The trig-only order clause is gone. <br>• Ledgers are derived by `misread_ledger.py`. <br>• Every re-marked case recomputes: vector 4/7, 6/7, 3/7; motion V 12→21 plus wrong factor 2/5, 4/5 ×3, 5/6 ×2, 2/6; principal 2/3; implicit 9/9, 5/9, 4/5; stationary 3/6 and 5/6. <br>**What needs clarifying (D4-S02):** <br>• the rule's undefined core term; <br>• the override clause, which now collides with MR09. |
| **D3-S03 (a): motion shortcut** | **repaired** | **The domain:** <br>• The four contexts are now (4,1,3), (4,3,3), (5,2,4), (6,3,5). <br>• 168 = 144 + 24; minority 1/7; 28 shapes; directions 84/84; root margin 1; keys 150 retained / 18 removed / 18 added; raw 361; sum 438. <br>• No ambiguous instance. <br>**The shortcut:** <br>• −b/a ≥ T and \|b\| ≥ 4\|a\| no longer separate. <br>• Best visible single/pair is 156/168; best triple with T is 166/168; there is no perfect visible separator. <br>• The nine sweeps reproduce at 3 s.f. half-up, tuple for tuple (0/12/24/144/24/66/66/24/24). |
| **D3-S03 (b): vertex route** | **repaired** | **The route:** <br>• "Or a vertex bound" is deleted from the work order (`:49`) and from both JSON files. <br>• Endpoint signs plus appropriate concavity is valid for all 24 no-change cases: k < 0 gives a positive, concave curve; k > 0 a negative, convex one. <br>**Fixtures:** vertex-only R1 = 0; justified harmless split "earns" 4/4; false root 3/4. |
| **D3-S03 (c): stale count** | **repaired** | `PLAN.md:54` says 18. |
| **D3-S04: trapezium** | **repaired** | **The official row** (report PDF 337, rendered): (b) `3ln(x–2)²` B1; `6×11.5 = 69.(0)` B1 "6 × their (a)". <br>**The design:** <br>• keeps b:B1 for the factorised square everywhere; <br>• loses b:B2 www for visibly wrong log-law working; the k = 2 coincidence scores b 1/2, total 9/10; <br>• gives a bare correct product b 1/2. <br>**Labelling:** the stricter reading is labelled a proposed clarification, attributed to neither OD-1 nor OD-5. <br>**Judgement:** coherent. It matches the usual meaning of www and the comparable Cambridge rule against "fortuitously correct" answers (9709 PDF 2, rendered). |
| **Notes** (D3 §D) | **mostly repaired** | **Repaired:** <br>• the "decision 6" rename at the four named lines; <br>• the modulus `:45` wording; <br>• motion-D3-08 and -09; <br>• calc-D3-05 (proof-target sentence removed from criteria); <br>• trig-D3-04, -05 and -07; <br>• the calc-D3-06 locators; <br>• coverage-D2-03 (receipt now derived: 25 text, 2 graph, 0 unknown, matching the work orders). <br>**Partly repaired:** stale "short check" wording survives at `planning/part-evidence-register.md:3` (shared-D4-03). |

## B. Corrections to our own work

1. **Our D4 prompt §2(e) caused part of D4-S02.** It said that eligible follow-through "overrides 'not F.T.' and c.a.o. qualifiers", with no exception for answer-given proofs. When Codex rewrote MR03, it dropped D3's sentence "no MR deduction rescues answer-only work or a supplied-result proof". MR03 now literally overrides MR09's "no F.T. into a given result".
2. **Our D4 prompt §2(a) left "on that datum" undefined.**
   - We wrote "the first A/B earned on that datum … the first-use part, otherwise the next part that uses the datum".
   - Codex's fixtures read this part by part.
   - A criterion-by-criterion reading is also possible, and it changes scores. One example is the stationary deferred-accuracy fixture: 3/6 becomes 4/6, which re-creates the free misread D3-S02(a) removed.
3. **Our D3 check missed two authority residues:** `exemplars/WB8227-implicit-normal.md:125` and `work-orders/WB8227-vector-geometry.md:73`. Both were byte-identical in D3 and already credited the once-per-datum unit to OD-6 (D4-S01).
4. **Our D3 note calc-D3-01 was wrong about q.** It said the point-on-curve guard makes every q misread ineligible. Reading q as the curve's other y-intercept keeps P on the curve in 27/27 tuples, and on 4 curves that point is an admitted negative one (calc-D4-05). This is carried into E/F.

## C. What passed

- **Write scope.**
  - All 36 changed design files are within D4's allowed scope. Analysis, tools and curriculum are unchanged (2,346 files), and the R7 analysis freeze passes (7,771 files).
  - The 85 earlier review files are pinned and unchanged; the D0–D3 recoveries verify.
  - No mark, criterion type or non-motion domain changed. The one undisclosed value change, trapezium strict-unseen 3 → 2, is a correct fix of a stale summary (shared-D4-07).
- **Manifest.** sha `71ee10b6…`; the digest recomputes; 3,497 files, 436 sources, 85 reviews; all 60 live `checks/plan-*` files pinned; `freeze-plan.py --check` passes.
- **Rebuild.** `planning/d4/rebuild-design.py` ran in two fresh copies. Both rounds pass, 25 seeded negatives and 2 motion negatives reject, and the 28 derived outputs reproduce.
  - One output embeds the absolute checkout path, so two files differ byte-wise between checkouts (note D4-N01).
  - After normalising that path, author, copy 1 and copy 2 are identical across all 11,252 files.
- **Counts unchanged:**
  - 9 recipes, 14 choices, 42 cases, 27 parts, 83 branch marks;
  - Bloom 13 Apply / 1 Analyse;
  - decks 19/20/17;
  - facets 38 + 1; objectives 25 + 1; 99 demands outside scope;
  - versions 0.1.4; classification `8227-pilot-design-0.1.1`.
- **Exemplars.** Every canonical exemplar in all nine recipes recomputes, including the changed motion no-change case (−1,4,3,3): v = −t²+t+12, distance = displacement = 63/2, endpoint velocities 12 and 6.
- **Source rights.** Textbook items stay internal and exam originals are attributed. Cambridge is labelled a comparable board throughout. No held original is an anchor.

## D. Findings

### Should-fix (a text-only errata, D4.1, before approval)

| ID | Locator | Defect | Repair |
|---|---|---|---|
| **D4-S01** | `work-orders/WB8227-vector-geometry.md:73` ("a genuine eligible misread uses OD-6 once-per-datum MR−1"); `exemplars/WB8227-implicit-normal.md:125` ("eligible OD-6 genuine question-data misreads under the once-per-datum rule") | Both credit the per-datum unit to OD-6, which is the D3-S01 defect class. The same vector work order contradicts it at `:94` and `:110`. These are the only live residues the shared agent's wide grep found (shared-D4-02, visual-D4-01). | Reword both, e.g. "follows MR03: the OD-6 MR−1 principle, under the proposed MR03-OPS-D4 per-datum mechanics". |
| **D4-S02** | `subject-rules.md:67` (MR03 operational sentence), `planning/d4/shared-misread-policy.json` `operational_rules`, and their copies in nine work orders and 27 policies; against `subject-rules.md:73` (MR09) | **(a) Override collision.** MR03 says eligible follow-through "overrides not-F.T. and c.a.o. restrictions". MR09 says "no F.T. into a given result". D3 MR03 kept answer-only work and supplied-result proofs out of the concession; D4 dropped that. The implicit eligibility guard (`WO:142`) prevents harm in this pilot, but the shared rules contradict each other (shared-D4-05, visual-D4-05). <br>**(b) Undefined core term.** "The first earned A/B on that datum" is undefined, and every fixture tags all A/B in a using part as being on the datum. The readings diverge: <br>• **Per criterion:** the stationary deferred-accuracy fixture (`WB8227-stationary-inflexion.md:122`) becomes 4/6 instead of 3/6, a free misread again (calc-D4-03). <br>• The principal k 4→5 slot moves from P-B1 to P-A1 (trig-D4-01). <br>• The polynomial T 2→3 slot moves from S2, which does not use T, to S3 (motion-D4-04). | Add to the operational sentence, then propagate: <br>• (i) "An A/B is on a datum when it lies in the datum's first-use part or a later part whose working uses the misread data, whether or not that criterion's own value changes." <br>• (ii) "Eligibility is judged at first use for the connected question." This is already in implicit `WO:142` (shared-D4-09). <br>• (iii) "Eligible follow-through never overrides MR09 (no F.T. into a supplied result) or OD-1 answer-only rules." <br>**Effect:** no fixture score changes, because (i) is the convention every fixture already uses. |

### Later-test (carry into stage E/F)

- **calc-D4-01.** The implicit C 4→5 fixture (`WO:148`) gives 9/9 without naming a route. That holds on the product route only. On the divided route the misread constant enters S3/S4, and strict canonical marking gives 7/9; on the explicit-root route it can drop to 6/9. Qualify the fixture by route.
- **calc-D4-02.** Datum identity. A displayed-formula number that restates an already-ruled curve parameter should inherit that ruling. The current text allows either 6/9 or 5/9.
- **shared-D4-01.** With two eligible data whose only earned A/B is shared, `misread_ledger.py:29–35` gives 1/2 or 0/2 depending on list order. Settle data in first-use order, each taking the first earned A/B not already charged. No current fixture is affected.
- **visual-D4-06.** At k = 2, a legible but ambiguous "2 2 ln" (superscript or product) needs a pending or benefit-of-doubt fixture.
- **motion-D4-02.** Derived-ratio rules can be fitted to separate this finite bank, e.g. (d/a, T) at 162/168, or \|d\| ≥ 2.5\|a\|T, which catches 18/24 no-change cases and no sign-change case. None is a plausible learner shortcut. Qualify the headline as "visible single/pair".
- **Carried from D3:** calc-D3-04, trig-D3-02, visual-D3-05, the more precise vector angle, and the items in the D2/D3 reports.

### Owner attention (not a defect)

- **shared-D4-08 / calc-D4-01: an ineligible misread can cost nothing.**
  - In the implicit recipe, misreading C as 5 for 4 moves P off the curve. That makes the misread ineligible, so it is marked normally. On the product route the misread constant never enters a marked step, so the learner scores 9/9.
  - A milder, eligible misread would lose one mark.
  - This follows OD-6's "marked as normal against the canonical question". NSSCAS item 4 ("do not score maximum marks") leans the other way.
  - Vitalis may wish to rule on it; otherwise it stays an E/F fixture.

### Notes (apply while editing D4.1; no approval impact)

- **D4-N01: rebuild portability.** `planning/d4/visual-d4-independent-checks.py:95` writes `render_path=str(render)` as an absolute path, which appears at `visual-d4-independent-checks.json:1045`. `freeze-plan.py --check` therefore fails in any relocated copy after a rebuild. Write a repo-relative path.
- **motion-D4-06: a sweep error.** `PLAN.md:11` reads "The D1 D4 changed-scope confirmation confirmed …". Restore "The D1 short check confirmed …".
- **shared-D4-04, visual-D4-04: undated "decision 6".** `capability-gaps.md:34` and `recipe-contract.md:162` still say it without the date. Add "16 November … (visual demands)".
- **shared-D4-03: stale labels.** `planning/part-evidence-register.md:3` still says "await Claude short check". Further stale round stamps are at `calculus-design.json:286` and `calculus-source-reads.md:65,69`, and in the calc bloom and visual classification status fields. Also trig-D4-03: `checks/plan-repair-d4-trig-validation.json:2` says "D3 author-side".
- **motion-D4-01.** `WB8227-motion-integration.md:75` gives the T 3→5 result (2/6) without its reason. The reason is only in `misread-policy-check.py:38`: R1 judges the decision against the printed interval; R2 does not depend on T; R5 needs an attempted primitive with both bounds. Add one sentence.
- **motion-D4-03.** `WB8227-motion-integration.md:35` says exposure keys "include recipe version", which conflicts with `:31` and `capacity-key-delta.json` ("exposure preserved across versions"). Say the version is provenance only. At `:25`, name 0.1.1–0.1.3 as the old versions.
- **motion-D4-05.** The mixed-branch eligibility note (sign-change outcome, R2/S2) is copied into the polynomial and exponential policies.
- **calc-D4-04.** The gradient-only `eligibility_notes` carry proof-target and later-part text that does not apply to that branch.
- **visual-D4-02.** The B2 www clarification sits in the D1-TRAP-FT-BRIDGE row without citing 2023 AWARD05. Trapezium `WO:95` does not mention it.
- **visual-D4-03.** The part-specific policy tails were replaced by generic text; vector a and b are now identical. Report `:28` ("with part-specific scope notes") overstates this.
- **shared-D4-06.** The `coverage-plan.md` prose is still template text, although its values are correct.
- **shared-D4-07.** The D4 report does not mention the trapezium strict-unseen 3 → 2 correction.
- **trig-D4-02.** Three of the "whole-question" trig ledgers cover one part. No trig fixture moves a deduction to a later part; our own case gives 4/7, as the rule says.

## E. Not checked

- **No runtime.** No app, generator, marker, renderer, local website or MCP operation was run.
- **Single read per recipe group.** Each group was read by one agent; marking judgements at the margin carry that limit.
- **Unchanged material.** Accepted material that D4 did not change was not re-reviewed.
