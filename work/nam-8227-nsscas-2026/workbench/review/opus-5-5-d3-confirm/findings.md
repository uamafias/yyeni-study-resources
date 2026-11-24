# D3 confirmation findings: 8227 Workbench pilot PLAN

**Reviewer:** Claude Opus 5.5 (cross-vendor REVIEWER). **Date:** 2026-11-24.
**Under check:** Codex's D3 repair, plan manifest `4667a860…` (content digest `75b2e3da…`), against the D2 baseline `2b9e53a5…`. The inputs are frozen in `inputs.json`.

## Method

**Scope.** Only the D3 delta was checked:
- 40 design files changed since D2; nothing was removed;
- the D3 folder and history archive were added (899 files).

The accepted nine-recipe selection and the analysis were not re-reviewed.

**Five independent agents** each wrote their own code and chose their own cases. Their evidence is in `check-*.json`:
- `motion`: the mixed domain, the separation and sweep tests, R1/R5, the motion OD-6 samples and the capacity/keys;
- `calc`: stationary and implicit-normal;
- `trig`: principal, R-form and log;
- `visual`: trapezium, modulus and vector;
- `shared`: subject rules, the register, the counts, the pins and the write scope.

**Totals:**
- 180 independent recomputations, 179 agree. The one disagreement is a finding: the R1 vertex argument, D3-S03(b).
- 72 marking tests, 60 as expected. The other 12 are the counterexamples behind the findings below.
- 48 dispositions: 41 repaired, 6 partly repaired, 1 not repaired (an optional note).

**What I verified myself:**
- **Native pages.** I rendered and read NSSCAS 2025 report PDF 345 item 4 and Cambridge `9709_m16_ms_12.pdf` PDF 3 "Penalties". The source bytes are unchanged since D2.
- **The two-copy rebuild** (`rebuild.json`).
- **The freeze checks.**
- **The D2 → D3 write scope.**
- **The key locators**, read in the current bytes:
  - `OWNER-CHECKPOINT.md:15,43`, `HANDOVER.md:17`, `recipe-contract.md:303` and `subject-rules.md:67`;
  - motion work order `:25–31` and `:44–50`, and `PLAN.md:54`;
  - trapezium work order `:71`, `:95`, `:110` and `:139`;
  - principal work order `:90`.
- **The motion ratio separator and the vertex claim**, worked out from the work-order domain.

## A. Dispositions of the D2 findings

| D2 finding | Verdict | Evidence / residual |
|---|---|---|
| D2-OD6 | **partly repaired** | **What holds:** <br>• All 27 parts carry a misread policy, and the pilot-design copies match. <br>• All nine work orders have a misread line. <br>• No residue of the withdrawn allocation remains in the live files. No deduction comes from M marks and there is no two-mark penalty. Cambridge is labelled comparable everywhere. <br>• The samples recompute: motion V = 12→21, 18→81 and 30→36 each 4/5; vector 6/7 (p = −1/4, 118.1255…° → 118.1°). <br>**Residuals:** <br>• Operational details are credited to the owner (D3-S01). <br>• The operational rules leave gaps and can let a misread cost nothing (D3-S02). |
| D2-S01 | **partly repaired** | **What holds:** <br>• 168 = 144 + 24, minority 1/7, 28 shapes (24 + 4), directions 84/84. <br>• T and \|k\| are shared by both outcomes. <br>• No admitted instance is ambiguous. <br>• None of the 28 single/pair tests separates the outcomes. <br>• The title is neutral and the internal ID private. <br>**Residual:** every no-change tuple uses c = 1, so a coefficient-ratio rule still separates all 168 (D3-S03a). |
| D2-S02 | **partly repaired** | **What holds:** <br>• The R1 alternative was added, and the routes are exclusive. <br>• A false interior root with a canonical sum scores 3/4; a harmless justified split scores 4/4. <br>• The coincidences are disclosed, and all nine sweeps reproduce at 3 s.f. half-up (0/12/24/144/24/66/66/24/24). <br>**Residual:** the example "or a vertex bound" is never a valid argument in this domain (D3-S03b). |
| D2-S03 | repaired | R5 now requires an attempted primitive with both bounds, and calculator legs alone score 0/2. The work order, both JSON files and the exemplars agree. |
| D2-S04 | repaired | **Motion:** OD-4 is cited only for the live decision, and the 4+2 tariff is called a proposal. **Log:** the domain is described as reviewer-prescribed. No live file says "owner-fixed". The same pattern recurs for OD-6 (D3-S01). |
| D2-S05 | repaired | The capacity sum is derived: 438 = 402 + 36. Motion has 361 raw tasks; fresh bounds 35/14/168; part keys 108 retained, 24 removed, 60 added. The old tail keys map one-to-one (108/108). |
| D2-S06 | repaired | The four motion Bloom rationales cite their own `@0.1.3` criteria. |
| D2-S07 | repaired | Both stationary branches are Apply 3, and the receipts cite the D3 checks. |
| D2-S08 | repaired | Back-substitution is in S4. **Proofs whose back-substitution fails:** divided route 3/4; log route 3/4. A complete product proof plus a divided proof scores 4/4 (the cap holds). The explicit route scores 2/4 when its identity fails. |
| D2-S09 | repaired | The no-real P-B1 mark requires a target comparison, and the rote answer scores 0/3 (fixture present). |
| D2-S10 | repaired | The class table describes canonical instances only, and the learner's own root set is judged. All 58 canonical tuples reproduce. |
| D2-S11 | repaired | **Trapezium bounds:** mathematical packing 3 and generated-fresh packing 2 are named separately everywhere. After one exemplar 1 card remains; after two, none. |
| D2-S12 | repaired | The 2k scale must be derived from the log law. A bare J = 6 × 11.5 scores 1/2 (official row, report PDF 337, rendered). OD-5 is intact. The new k = 2 fixture contradicts row 04 (D3-S04). |
| D2-S13 | repaired | The register has 20 readable rows, each with a status class, and it matches `deviation-register.json` in both directions. `checkpoint-stage-d.json` is marked historical. |
| closeout-D2-02 | repaired | All 47 live `checks/plan-*` files are pinned with correct hashes, and the content digest recomputes. |
| closeout-D2-01 and -03 | deferred, as asked | HANDOVER records them as maintenance that needs the full analysis proof if the tools change. |

**Notes.**
- calc-D2-04..08, trig-D2-04..08, visual-D2-03/05/06/07, motion-D2-11, vecrec-D2-02/03/06 and coverage-D2-04 are repaired.
- visual-D2-04 and vecrec-D2-08 are partly repaired; see D3-S04 and D3-S02(c).
- coverage-D2-03 is not repaired: the receipt still hard-codes its literals, but the values are correct.

## B. Corrections to our own work

Three D3 residuals trace to our own wording.
1. **D3 prompt §1:**
   - "Make the deduction once per misread datum, in the part where it is first used"
   - "If there are no A or B marks to deduct from, nothing is deducted"

   Codex read these as "no deduction anywhere if the first-use part earns no A/B". That lets a misread cost nothing (D3-S02a). We meant the whole question.
2. **D3 prompt §2 (D2-S02):** our wording "such as endpoint signs plus concavity, or the vertex value" suggested an R1 route that never proves constant sign here (D3-S03b).
3. **D3 prompt §2 (D2-S01):** it asked Codex to show that "no single visible parameter, or simple pair" separates the outcomes. That test was too narrow: a derived coefficient ratio still separates them (D3-S03a).

The D3 prompt also listed the operational settlements as "Settle and state these". Codex then recorded them as the owner's choice, which is D3-S01.

## C. What passed

- **Rebuild.** `planning/d3/rebuild-design.py` was run in two fresh temporary copies:
  - 2 rounds × 16 commands, 43 outputs byte-identical within each copy;
  - 19 seeded faults and 5 inline motion-domain faults all rejected.

  All 45 design outputs, and every one of the 9,463 workbench files, match each other and the author checkout. The freeze check passes in the author checkout and in both copies (1,708 files, 436 sources, 75 review files, 47 live plan checks, 809 D2 files recoverable). The R7 analysis freeze passes: 7,771 files, 436 sources, 37 review files.
- **Write scope.** Since D2 only the following changed:
  - the 40 manifest design files;
  - `planning/d3`;
  - `planning/history`;
  - `checks/plan-repair-d3-*`;
  - `CLAUDE-D3-CONFIRM.md`.

  Every changed non-recipe hunk is explained by OD-6, D2-S01..S13 or a §D note. All 2,346 analysis, tool and curriculum files match the D3 baseline. The analysis snapshot `1c8cb96f…` matches both manifests. The earlier review folders are untouched. STATUS and HANDOVER claim neither approval nor a Stage E start.
- **Counts,** recomputed from the design files:
  - 9 recipes / 14 choices / 42 exemplar cases / 27 parts / 83 marks;
  - Bloom 13 Apply / 1 Analyse; decks 19/20/17;
  - facets 38 + 1 conditional-only; objectives 25 + 1; 99 demands outside the pilot;
  - rounding totals 720.1 / 720.5 / 2162/3.
- **Capacities** all reproduce:
  - implicit 27/23/8; two-extrema 540/30; flat 256/16 (128/64/64);
  - R-form 58; principal 48/47; log 40→20;
  - trapezium 30→11; modulus 108→44; vector 54→30/17;
  - motion 361 / 168.
- **Exemplars.** Every changed exemplar recomputes, including the new no-change case v = −t² + 3t + 4 on [0, 3]: roots −1 and 4, distance = displacement = 33/2.

## D. Findings

There is no design-blocking defect. Four should-fix groups must be corrected before approval.

### Should-fix (correct in D4, before approval)

| ID | Locator | Defect | Repair |
|---|---|---|---|
| **D3-S01** | `planning/OWNER-CHECKPOINT.md:15,43`; `planning/d3/deviation-register.json:190,192`; `subject-rules.md:67` (row labelled "Binding OD-6"); `HANDOVER.md:17`; `recipe-contract.md:303`; `checks/plan-repair-d3-trig-dispositions.json:22` ("owner approved") | **Operational details are credited to the owner.** The register says "Owner chose one earned A/B deduction per eligible datum in its first-use part … earliest eligible earned A/B … none earned means no deduction". OD-6 decided the principle only. The unit, the order and the no-carry rule came from our D3 prompt and from Codex. This is the D2-S04 pattern again (shared-D3-01, motion-D3-03, trig-D3-03, visual-D3-03). | Split the record. **The OD-6 owner decision:** <br>• one mark from the A/B marks, with all A/B following through and M/DM as usual; <br>• the learner's own figures are an accuracy error; <br>• a changed object or difficulty gets no MR treatment; <br>• practice feedback names the misread. <br>**A separate row, proposed and pending approval:** the operational rules of D3-S02. Label only the principle binding in MR03. |
| **D3-S02** | `subject-rules.md:67` (MR03); the misread line in all nine work orders; `misread_policy` in all 27 parts (calculus, trig, visual and pilot-design JSON); `planning/d3/misread-policy-check.json` | **The operational misread rules contradict OD-6 or leave the outcome open.** <br>**(a) A misread can cost nothing.** "If that first-use part earns no A/B, deduct nothing and do not defer" means that when an unrelated error removes the first-use A/B, later parts still earn A/B by follow-through and no mark is lost. Vector OB sign misread plus a wrong resultant: 5/7, against 4/7 under OD-6. Motion V 12→21 plus the wrong −V/k factor: 3/5, against 2/5. Both equal the score with no misread (shared-D3-02). <br>**(b) One misread can cost two marks.** The deduction falls on R2 or S2 (motion) and G2 or S2 (calculus), and later marks depend on those. Nothing says the dependencies use the mark before the deduction, so a literal marker gives 4/6 where 5/6 is intended (motion-D3-06, calc-D3-03). <br>**(c) Ineligible misreads reused later are undecided.** For the vector no-p misread, (b) scores 3/7 if marked canonically and 5/7 under a follow-through reading (visual-D3-04). Two implicit-normal edges also have two possible scores (calc-D3-02). <br>**(d) "Leaves no solution" breaks a designed outcome.** In the principal recipe, "no real solution" is a correct designed answer. Reading (3, −3π/4) as 3π/4 and answering "no real solution" gets 2/3 under OD-6 but 0/3 under the literal clause (trig-D3-01). <br>**(e) "Not F.T." and c.a.o. qualifiers carry no OD-6 exception.** Motion S3 reads "S3 is not F.T." (work order :46, `calculus-design.json:3560`). The trig c.a.o. qualifiers are the same (motion-D3-05, trig-D3-06). <br>**(f) "Practice feedback names the misread" is missing** from MR03, from 13 of the 27 policies (motion 6, visual 7) and from the motion, modulus and trapezium work orders (shared-D3-03, motion-D3-04, visual-D3-02). | **Restate MR03 once and copy it consistently everywhere:** <br>(a) **One deduction per misread datum,** taken from the first A/B earned on that datum in question order: the first-use part, otherwise the next part that uses it. Nothing is deducted only if no A/B is earned on that datum anywhere. Re-mark the two samples: vector + wrong resultant 4/7; motion 21 + wrong factor 2/5. <br>(b) **The deduction is a net penalty applied after marking.** The criterion it comes from still counts as earned for every dependency (DM, "dependent on", www), so one misread never costs more than one mark. <br>(c) **Eligibility is decided once,** at first use, and recorded in the ledger. An ineligible misread is marked canonically in every later part. State the single outcome of the vector no-p fixture in (b) and of the two implicit edges. A misread that flips the motion sign-change outcome changes the object, so it is marked canonically. <br>(d) **"Leaves no solution"** means no solution where the canonical question has one. A designed "no real solution" outcome keeps the OD-6 treatment. <br>(e) **For eligible misreads only,** OD-6 follow-through overrides "not F.T." and c.a.o. qualifiers. Say so in MR03, and add a pointer in motion S3 and the trig c.a.o. qualifiers. <br>(f) **Add the feedback sentence** to MR03 and to every policy and work-order line that lacks it. Drop or justify the trig-only "unless the actual scheme specifies an order" (shared-D3-04). |
| **D3-S03** | (a) `work-orders/WB8227-motion-integration.md:27,29`; `calculus-design.json:5358–5375`; `pilot-design.json:6451–6468`; `d3/motion-separation.json`. (b) work order `:49`; `calculus-design.json:5439`; `pilot-design.json:6532`. (c) `PLAN.md:54` | **(a) A coefficient ratio still gives the motion outcome away.** All 24 no-change tuples use c = 1 and r ≥ 4, so there are only 3 normalised no-change polynomials. <br>• "Sum of roots −b/a ≥ T" (the vertex at or beyond T/2) separates 168/168. <br>• \|b\| ≥ 4\|a\| occurs only in no-change cases (18/24 no-change, 0/144 sign-change). <br>• v(0) = v(T) occurs only in no-change cases (18/24) (motion-D3-01). <br>**(b) "Or a vertex bound" is never a valid R1 route.** In all 24 no-change cases the vertex lies inside (0, T), and its value lies on the side away from zero. It therefore never proves constant sign, and a marker following the example would give R1 for an invalid argument (motion-D3-02). <br>**(c) A stale count.** `PLAN.md:54` still says the reversal subset excludes 54 triangle-method coincidences; the D3 domain excludes 18, the 2r = T cases (motion-D3-07). | **(a)** Spread c (and r) across the no-change contexts. The reviewer's candidate is (4,1,3), (4,3,3), (5,2,4), (6,3,5): margins 1, best single/pair lookup 156/168, no perfectly separating visible triple. Codex may choose others. Keep a bounded minority. Extend the separation test to derived features: −b/a against T, \|b/a\| thresholds, d/a, v(0) = v(T), and triples containing T. Then re-enumerate, re-run the nine sweeps at 3 s.f. half-up, recompute the affected exemplars, and update the counts, shapes, part keys and aliases. <br>**(b)** Delete "or a vertex bound" and keep endpoint signs plus concavity, or name another argument that is valid in this domain. Add a fixture: a vertex-value-only argument scores R1 = 0. <br>**(c)** Correct the count. |
| **D3-S04** | `planning/visual-design.json:580` (scale-slip feedback fixture); `pilot-design.json:680`; trapezium work order `:139`; exemplar `:91`, against work order `:71`, `:95`, `:110` | **The new k = 2 fixture contradicts the official row 04.** It says "visible wrong log-law working → b:B1 = 0 (www/OD-1)". Row 04 (report PDF 337, rendered) gives B1 for the factorised form alone, and work order :110 keeps b:B1 when the log law is then misused. "2ln((x−1)²) = 2²ln(x−1); J = 4T" scores 9/10 or 10/10 depending on which text the marker follows (visual-D3-01). | Keep b:B1 for the factorised form. Wrong log-law reasoning loses b:B2 (www), in line with :85 and :110. The fixture stays a feedback fixture (visual-D2-04). |

### Later-test (carry into stage E/F)

- **calc-D3-04.** Define "difficulty unchanged" for stationary coefficient misreads. In 252 of 3,240 two-extrema cases the misread still gives integer roots. In the flat branch only constant-term misreads can be eligible.
- **trig-D3-02.** Misreads that land on degenerate or excluded cases:
  - R-form c read as b (an endpoint root) or as ±R (a tangent);
  - log q read as ca, giving x = 0;
  - principal θ read as π − θ.
- **visual-D3-05.** Eligibility for two cases:
  - a modulus label misread that contradicts a redundant label or the drawn orientation;
  - a trapezium strip-count misread.
- **Carried forward:**
  - vecrec-D2-08: a more precise angle (79.98);
  - coverage-D2-05, trig-D2-04, visual-D2-06 and motion-D2-12, as in the D2 report.

### Notes (apply when touching the text; no approval impact)

**Naming clash**
- **shared-D3-06, visual-D3-06.** The phrase "owner decision 6" refers to the 16 November visual-demand decision. It now collides with OD-6 at `PLAN.md:74`, trapezium work order `:58`, modulus `:39` and vector `:55`. Rename it, for example "16 Nov decision 6".

**Stale wording**
- **Modulus work order `:45`** says MR01–09 "bind every row".
- **shared-D3-05.** Further stale lines:
  - `PLAN.md:120`;
  - `app-change-handoff.md:131`;
  - `recipe-contract.md:301`;
  - modulus work order `:82`;
  - leftover "short check" gate wording (also coverage-D2-01/02).

**Motion**
- **motion-D3-08.** "May earn 4/4" should read "earns 4/4".
- **motion-D3-09.** The new no-change case is labelled as a D1 exemplar.

**Calculus**
- **calc-D3-01.** The point-off-curve rule makes a, C and q misreads in the implicit recipe ineligible. This is a disclosed judgement.
- **calc-D3-05.** A proof-target sentence was pasted into 15 criteria that have no proof target.
- **calc-D3-07.** Superseded by D3-S02(a).
- **calc-D3-08.** The ln y maximum of 1/4 is coherent and disclosed.

**Trig and log**
- **trig-D3-04.** The principal exemplar `:19` tags a bare interval sentence [P-B1].
- **trig-D3-05.** R-form work order `:46` still says "b-M2 requires" the canonical interval.

**Report locators and receipts**
- **calc-D3-06, trig-D3-07.** The D3 report cites the wrong lines for S07–S10, and the 0.1.3 trig JSON still carries "D2" status labels.
- **shared-D3-07, coverage-D2-03.** The coverage receipt still hard-codes its literals.

## E. Not checked

- **Runtime.** No app, generator, marker, renderer, local website or MCP operation was run. The offline KaTeX/Markdown check runs inside the author rebuild only.
- **Single read.** Each recipe was re-tested by one agent, so marking judgements at the margin carry that limit. The exceptions are the OD-6 authority point, raised independently by four agents, and the misread feedback gap, raised by three. I verified both myself.
- **Analysis.** The accepted R7 analysis proof was not rerun; it is preserved by unchanged hashes.
