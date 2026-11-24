> **Current gate — 24 November 2026:** Claude confirmed D4.1 and Vitalis approved the exact Stage-D manifest `4a054832…17d8ec`, including MR03-OPS-D4. Stage E is active; E/F runtime author checks and cross-vendor content review are next. Earlier pending/next-gate prose below describes the archived Stage-D proposal.

# Work order: WB8227-vector-geometry

NSSCAS Mathematics 8227; NIED December 2020 syllabus, Grade 12. Owner Vitalis; PLANNER Codex; 24 November 2026. **Proposed v0.1.4, stage-D4 repair. Claude D4 changed-scope confirmation, then Vitalis approval pending.** Accepted C selection `8227:FAMILY:vector-product`; narrowed selection `8227:D:SEL:vector-geometry:scalar-combination-and-origin-angle`; branch `scalar-combination-and-origin-angle`. No runtime authoring or assignment.

## Learner target, assessment and reuse

Apply a perpendicular scalar-product condition to a prescribed scalar combination, then calculate an origin angle from two nonzero position vectors. Parts share given vectors but(b) does not depend on(a)’s answer: do not invent an a→b cue/F.T. New 8227 design reuses the common Workbench provider/evidence structure, not Flashcard Studio cards. Supplied vector arithmetic is distinct from inferring coordinates from a spatial diagram, unit-vector construction or division of a segment; those remain later scope.

| Part | Direct demands (prefix `8227:2020:`) | Primary objective | Prerequisites | Marks / response |
|---|---|---|---|---|
| `a` | `M1:T7:O02:D01`, `M1:T7:O02:D02`, `M1:T7:O04:D02`, `M1:T7:O05:D02` | `M1:T7:O05` | `M1:T7:O01:D02` notation; NSSCO linear algebra |3; numeric$p$ with method|
| `b` | `M1:T7:O04:D01`, `M1:T7:O04:D02`, `M1:T7:O05:D01` | `M1:T7:O05` | `M1:T7:O01:D02`; square roots/inverse cosine |4; numeric angle with method|

D1 corrects(a): O02:D01 means **add/subtract vectors**, O02:D02 scalar multiplication. O02:D03 geometric interpretation is not directly assessed by any criterion and is removed. Prerequisites do not earn direct AS coverage.

## Native sources, calibration and references

- Syllabus `Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf`, SHA256 `c53e77d60f8de1410163c4fccbfa1c41ae88479fb9a53e2bd26ef1bcc727fb30`, PDF12/printed9 vector objectives, PDF18/printed15 precision. Grade `C:07` PDF21/printed18 covers supplied-vector operations/angles; `A:07` PDF20/printed17 perpendicularity/scalar-product applications. `E:07` PDF23/printed20 supports notation. Values are a modest bounded pilot subset, not the hardest whole-grade vector problems.
- NSSCAS2025 P1 Q3(a) PDF/printed4, (b) PDF/printed5: `Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/2025/8227-1.pdf`, SHA256 `9b8c39c4f0001ff266f943ff0d01d6681ac88f42f2b90dbab162844e858ae816`.
- Examiner report2025 `Question Banks/Namibian Examiner Reports/NSSCAS/2025/NSSCASExaminersReport2025.pdf`, PDF346/printed344 describes the common wrong resultant $p(OA-OB)$ and stopping at the **undistributed** restatement $pOA-OB$, before scaling its components. PDF347/printed345 contains the full3+4 award table, accepts the **distributed** uncombined scaled-minus form, reversed dot as an alternative, within(b) M1FT, and rounded degree/radian answers. PDF345/printed343 gives misread and first-uncancelled-answer rules. PDF355/printed353 and report2021 PDF236/printed234 give method/answer-only/hence/rounding conventions, read directly for D1.
- Internal textbook breadth: all19 members of `vector-between-directions-angle` and `vector-perpendicularity-parameter` read on YM C5 PDF253–254,258–261,263 and Goldie C10 PDF265,268–270,291. Exact members, accepted assessed/component union leads, source/render hashes and limitations remain in `planning/visual-source-reads.json/.md`. Goldie10F13(ii) is only supplied-direction/axis-angle practice; its skew-line proof is not adopted. Originals stay internal, `learner_display:false`. Family prose/precision/rejection templates and extracted notes are not design evidence.

**R2-02 re-decision:** corrected(a)’s four direct demands now equal the accepted2025 Q3(a) set; numeric parameter response, three supplied vectors, scalar difference/perpendicular target and no earlier-part scaffold also match. It now has its own part-scoped label “Same type as NSSCAS Mathematics 8227, 2025 Paper 1, Question 3(a), page 4”, with its own comparison/display reason. Part(b) separately matches2025 Q3(b), page5. Neither label claims a whole-family union or leaks an original as a fresh variant. Full references/verifiers are in `planning/visual-design.json`; no held source is used.

## Question, domain and discrimination

Give $OA=\mathbf u=(1,r,1)$, $OB=\mathbf v=(s,1,-1)$, $OC=\mathbf w=(1,t,1)$, with $r,t\in\{1,2,3\}$ and $s\in\{-3,-2,-1,1,2,3\}$.

(a) Find$p$ such that $p\overrightarrow{OA}-\overrightarrow{OB}$ is perpendicular to$OC$. If not written exactly, give$p$ to **3 significant figures**.
(b) Use a scalar product to find angle$AOB$ **in degrees, to1 decimal place unless exact**. A pre-labelled degree answer field supplies the unit; exact$60$ or$90$ is accepted without a trailing `.0`.

Canonical $p=(s+t-1)/(2+rt)$ and $\theta=\cos^{-1}[(s+r-1)/\sqrt{(r^2+2)(s^2+2)}]$. D1 excludes:

1. $r=t$:18 raw tuples give$A=C$ and collapse part of the shared data.
2. $p=0$, equivalently$s+t-1=0$:6 raw tuples let the reported wrong resultant$p(\mathbf u-\mathbf v)$ give canonical$p$.
3. $3-s+rt-t=0$:3 raw tuples make that wrong perpendicular equation an identity$0=0$.

The union removes24 of54, leaving **30**; overlaps are not summed. No admitted$p$ is zero, and$A,B,C$ are distinct. $2+rt>0$ gives unique$p$; all angle/resultant vectors remain nonzero and no parallel$OA,OB$ occurs. Supplied components stay within magnitude3, below the source’s maximum6, while positive/negative$p$ and acute/right/obtuse angles remain. Two exact60° and four exact90° tuples survive. For90°, reversing a ray gives the same right angle and is a valid geometric equivalence, not a diagnostic wrong-answer collision. Outside right angles, uncorrected reversal gives the wrong supplementary angle and is checked. Zero-vector, nonunique-parameter or contradictory-given cases are rejected in any future extension.

Domain/discrimination script `planning/d4/visual-domain-checks.py` enumerates every raw/retained tuple and records every removal reason. No original2025 source vector triple equals this supplied template. New admitted boundary$(r,s,t)=(2,-1,1)$ gives$p=-1/4$, angle90°; the old$p=0,A=C$ boundary is excluded and retained only as a negative regression case.

## Semantic capacity and fresh evidence

| Scope | Semantic key | Count |
|---|---|---:|
| Complete supplied triple / part(a) | `('vector-perpendicular',r,s,t)` |30|
| Part(b) | `('vector-angle',r,s)` |17|

Part(b) does not depend on$t$; therefore30 raw tasks are not30 wholly fresh angle questions. Thirty presentations collapse to17(b) contexts (13 repeated part(b) presentations). A wholly fresh question requires **all assessed part keys unseen**, including worked examples; maximum packing17 before exposures. Store part keys, semantic complete key and visible fingerprint separately; answer values alone are not deduplication keys. App owns reservations/retries/seen sets and original snapshots. Part-repeated renewal is allowed only labelled after-feedback, never a wholly fresh test. Exhaustion is explicit, not silent repetition or domain expansion.

## Givens/assets and must-read information (R3-07)

`given_representation: text`, three labelled column vectors. Must read every signed component, vector names/directions$OA,OB,OC$, scalar placement/difference order in$pOA-OB$, perpendicular target$OC$, angle vertex$O$ and required accuracy/degree unit. No supplied figure is necessary; this is **not a diagram-reading task** and does not earn spatial-coordinate coverage. Optional solution schematic must derive from the vectors, keep all named points/rays distinct, show the correct origin angle and state “not to scale”; projected angle measurement is prohibited. No fixed textbook crop is used.

Marker/renderer must preserve column-vector rows, minus signs, multiplication and degree marks in input, feedback and saved history. Photo presence alone does not prove this. These are named later app acceptance checks under the 16 November owner decision 6 (visual demands), not capability holds or delivered features.

## Criteria, official qualifiers and shared rules

**D1-MR01–09 in `subject-rules.md` apply.** Criterion prefix `WB8227-vector-geometry:`; source rows `8227:EXAM:2025:P1:Q3:AWARD:01–07`.

| ID | Award | Required evidence and qualifier |
|---|---:|---|
| `a:B1` |B1| Correct scaling **and subtraction** $(p,rp,p)-(s,1,-1)$, **or** combined$(p-s,rp-1,p+1)$, or the equivalent correct scalar-product expansion. The official **distributed** uncombined setup allowance is retained. The undistributed restatement $p(1,r,1)-(s,1,-1)$ is B0 unless the scaled components are shown. |
| `a:M1` |M1| Calculate a scalar product with$OC$ and **equate to zero**. Correct scalar-product testing of an attempted resultant can retain this method mark when the component step is wrong; no inferred method from a bare$p$. |
| `a:A1` |A1| Correct exact$p$ or correct3sf decimal, with valid specified-resultant working. Wrong resultant does not earn A1 even if its numeric$p$ coincides. |
| `b:B1` |B1| Correct$OA\cdot OB=s+r-1$, **or** its sign-reversed value clearly identified as$AO\cdot OB$, as the official row allows. |
| `b:M1` |M1| One or both magnitudes correct; reversing a vector does not change its magnitude and does not remove genuine magnitude credit. |
| `b:M2` |M1 F.T.| Correct use of scalar-product angle relation with their coherent dot/magnitudes. This is within(b), no invented a→b dependency. |
| `b:A1` |A1| Correct requested angle, with required scalar-product method: exact60°/90° accepted, otherwise correctly rounded **1 d.p. form**, including a trailing zero for non-exact$80.0^\circ$ or$63.0^\circ$; naked$80$/$63$ does not satisfy the form requirement. |

Total **3+4=7**. Exclusive rearrangements/alternative methods fill the same slots, never add marks. Bilinearity $p(\mathbf u\cdot\mathbf w)=\mathbf v\cdot\mathbf w$ is valid; a reversed ray plus supplementary-angle correction is valid. Cosine rule alone does not meet the explicit scalar-product instruction, though it is a separate author oracle. Source’s2.03rad alternative is recorded: this new stem explicitly requests degrees, so radian-only final retains legitimate working but not the requested degree-form A1; **named deviation `D1-VEC-DEGREE-STEM`**. Exact60°/90° answers need no `.0` or artificial loss. Non-exact values rounding to an integer still need the requested decimal place; their raw response form must survive later input/marking/history conversion.

Answer-only: (a) bare$p$0/3; (b) bare angle0/4 under OD-1/D1-MR01. A visible equation can demonstrate method without prose; an answer alone cannot create B/M/A credit. No source exception is claimed for bare vector results. When exactness is not requested, exact rational or correctly rounded3sf$p$ earns A1 given valid working; an exact terminating decimal is also accepted. Current domain gives no hidden units beyond the stated degree response. Multiple attempts follow D1-MR07; a genuine eligible misread follows MR03: the OD-6 MR−1 principle with A/B follow-through, under the proposed MR03-OPS-D4 per-datum mechanics, preserving required working.

Qualifier/deviation ledger: source row01 scaled-minus **or** resultant retained; row02 requires dot product **and=0**; row03 keeps valid-result accuracy with OD-1. Rows04–05 retain reversed-dot and one-or-both magnitudes alternatives; row06 retains formal F.T.; row07 retains degree accuracy and explicitly records the stem-specific radian departure above. `D1-VEC-A1-VALID-WORK` makes the correct-resultant dependency operational so named wrong-working coincidences cannot earn A1; it is a disclosed D1 criterion interpretation, not a falsely quoted official “www” label. Preserve independently earned M credit rather than a global wrong-resultant zero.

## Rounding and misread fixtures

Keep exact norms/guard digits until the final angle. If early approximation changes the required digit, retain genuine B/M work but lose b:A1 and give premature-rounding feedback (D1-MR05). Do not penalise early rounding that leaves every required answer correct. High-precision/decimal half-up rounding determines the memo, not double rounding a binary approximation.

`planning/d4/visual-rounding-fixtures.json` freezes **all15 D0-sensitive tuples**, not just the retained ones: five$(r,s)$ pairs$(1,-2),(1,2),(2,-3),(2,1),(3,3)$ times$t=1,2,3$. Nine survive D1; six are now rejected with their exact reason. The original fixtures stay regression evidence even when excluded. Normal/changed examples are intentionally retained with explicit accuracy feedback rather than a hidden rounded memo.

| Normal-instance submission/evidence | Credit | Feedback |
|---|---:|---|
| Correct scaled-minus setup, dot equation, $p=3/4$; dot2, norms$\sqrt3,\sqrt6$, angle$61.9^\circ$ |7/7| All required work and values present; no repair. |
| Distributed $(p,rp,p)-(s,1,-1)$ only in(a), with complete(b) |5/7| a:B1 retained. Use the perpendicular zero condition and solve$p$. |
| Undistributed $p(1,r,1)-(s,1,-1)$ only in(a), complete(b) |4/7| a:B1=0: this only restates the prompt; show the scaled components. |
| Uses$p(OA-OB)$, obtains$p=0$ via a coherent dot-zero equation, complete(b) |5/7| a:M1 only; incorrect scaling/subtraction B0 and accuracy A0. “Scale$OA$ only, then subtract$OB$.” |
| Correct(a), reversed-ray method returns$118.1^\circ$ without correction |6/7| Reversed-dot/magnitude/method credit remains; correct the supplementary final angle. |
| Correct(a), norms prematurely rounded to1.73 and2.45 yield$61.8^\circ$ |6/7| Preserve b:B1/M1/M2; b:A1=0. “Keep the exact square roots until the final angle.” |
| Misreads$OB$ as$(-2,1,-1)$; coherently gets$p=-1/4$ and angle$118.1^\circ$ |6/7 under OD-6| Correct misread-data work earns a2/3 (a:B1 carries the one MR−1, a:M1/a:A1 earned) and b4/4 with no second penalty. Name the miscopied sign. |
| Unreadable sign, angle unit or cancellation |pending| Clarify; retain original; no guessed score or best-attempt selection. |

**MR03 misread — authority and proposed mechanics.** Binding OD-6 principle: a genuine misread of question data with unchanged object and difficulty costs one mark from A/B; all A/B follow through on the misread value and M/DM are judged as usual. Own-figure errors and misreads changing object/difficulty receive ordinary canonical marking. Practice feedback names the misread. Proposed MR03 operational rules, pending Vitalis approval of the exact manifest: decide and record eligibility once at first use; ineligible data remain canonical in every later part. For each eligible misread datum, first mark all gross evidence and dependencies, then deduct one mark from the first earned A/B on that datum in question/criterion order, moving to later-use parts if necessary. Deduct nothing only if no A/B is earned on the datum anywhere. Never deduct from M/DM or make the score negative. The selected criterion remains earned for every DM, dependency and www check; one datum costs at most one net mark. Eligible OD-6 follow-through overrides not-F.T. and c.a.o. restrictions, while correct working, named method exclusions and OD-1 still apply. No-solution exclusion means a misread removes a solution the canonical question has; a designed no-real-solution outcome remains eligible when its demand and difficulty are preserved. An A/B is on a datum when it lies in the datum's first-use part or a later part whose working uses the misread data, whether or not that criterion's own value changes. Eligibility is judged at first use for the connected question. Eligible follow-through never overrides MR09 (no F.T. into a supplied result) or OD-1 answer-only rules. Sources: NSSCAS 2025 report PDF345 item4 (CONVENTION108) and comparable Cambridge 9709_m16_ms_12.pdf PDF3 Penalties; the comparable allocation is not a published Namibian rule.

## Bloom, modes, checks and stop

Classification `8227-pilot-design-0.1.1`: a Apply3, supported only by a:B1/a:M1/a:A1; b Apply3, supported only by b:B1/b:M1/b:M2/b:A1. Whole branch3.3D notation, numeric sign or a larger model solution does not raise it. No O02:D03 geometric interpretation or unasked model-construction credit is inferred.

Practice permits answer-free generic support and a separately bound different-instance example before submission; current solution/feedback only after submission. Repeated parts are after-feedback. Test has no pre-submit help and retains existing per-question review/timing/progress; app owns all state. Original attempts remain frozen and unreliable evidence pending.

Current D4 domain and exemplar-oracle scripts enumerate30 admitted tasks,17 angle keys, every targeted error, source/domain exclusions and all15 rounding fixtures. Stage E/F must replay seeds0/1/42/$2^{63}-1$, exhaust the revised domain, test scaled-minus partial work, wrong-resultant, misread, premature-rounding, reversed-ray, exact60/90, multiple attempts and notation/history rendering; independently check angles by Euclidean cosine law. Additional form fixtures: $(r,s,t)=(3,-1,1)$ gives$80.0^\circ$, and$(3,3,1),(3,3,2)$ give$63.0^\circ$. Each is non-exact: reject$80^\circ$/$63^\circ$ for b:A1, retain genuine working. These three form fixtures are frozen beside the15 numeric-rounding fixtures. Every admitted$p$ terminates within3sf; the non-examiner-named wrong dot-with-$OA$ method coincides at$(2,2,1),(2,2,3)$ and is retained as a disclosed later feedback fixture, not an invented exclusion.

No runtime generator, marking, app, import or production acceptance is claimed. Existing learner-text guidelines remain pinned; private memo/seed/reference data must not leak.

Next under OD-3: Claude D4 changed-scope confirmation of the repaired design, then Vitalis approves exact scope/counts/gaps/capabilities/exemplars. No commit or push.

D4 ineligible-reuse fixture: in the changed case, misreading $OA=(1,2,1)$ as $(1,-2,1)$ gives $OA\cdot OC=0$ and $OB\cdot OC=-3$, so no $p$ solves the altered question. Eligibility is recorded as false once and remains false in (b). A visible zero-dot attempt earns a:M1 only, 1/3. In (b), the learner's dot is −6, the correct magnitudes are $\sqrt6$ and $\sqrt{11}$, and the resulting angle is $137.6^\circ$. Canonical marking awards only b:M1 and b:M2, 2/4; **total3/7**, with no MR penalty and no MR accuracy follow-through. Own-figure miscopies are ordinary accuracy errors. The later acceptance decision for a more precise angle such as $79.98^\circ$ remains open.

OD-6 sources: NSSCAS 2025 examiner report PDF345 item4 (`CONVENTION:108`) and Cambridge International 9709/12 March2016 mark scheme PDF3, Penalties. The Cambridge convention is comparable-board evidence adopted by Vitalis, not a Namibian published allocation. The per-datum unit, deduction order, eligibility ledger and gross-before-net dependency mechanics are proposed operational rules in MR03, pending approval of the exact manifest; they are not further owner decisions. Practice feedback names the misread.


D4 deferred-deduction fixture: in the normal case, genuinely misread $OB=(-2,1,-1)$ and then use the named wrong resultant $p(OA-OB)$. The visible zero-dot equation gives a:M1 only, 1/3; correct misread-data work in (b) earns all four gross awards. The first A/B earned on this datum is b:B1, so apply the one net MR deduction there: b3/4, **total4/7**, not5/7. The named error is not rescued and the deduction never removes the gross award used by a dependency. Practice feedback names both the miscopied sign and the separate resultant error.
