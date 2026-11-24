# Establish and apply an implicit derivative, gradient and normal

NSSCAS Mathematics 8227; NIED December 2020 syllabus; Grade 12. Owner Vitalis; PLANNER Codex, 23 November 2026. Recipe `WB8227-implicit-normal`, proposed version **0.1.1**, classification version `8227-pilot-design-0.1.1`. D1 repairs D0; **Claude's short check comes next, then Vitalis approves** (OD-3). No stage-E authoring, runtime items, question generators, imports or assignments are authorised.

## Authority, selections and source repair

Accepted selection `8227:FAMILY:implicit` is retained. D1 selections are `8227:D:SEL:implicit-normal:gradient` and `8227:D:SEL:implicit-normal:normal`. The recipe list is not reopened. This purpose-built 8227 design extends the existing Workbench contract; no Flashcard Studio conversion or parallel framework. The derivative core is shared, but only the extended branch includes the newly commissioned show-that part.

Syllabus: PDF15/printed12, M2:T4 O01/O02/O03; normals PDF12/printed9, M1:T8 O03. Source file SHA256 `c53e77d60f8de1410163c4fccbfa1c41ae88479fb9a53e2bd26ef1bcc727fb30`. **The implicit component is described only at Grade a**, descriptor `8227:GRADE:A:14`, PDF20/printed17. `8227:GRADE:C:13`, PDF22/printed19, is exponential/product/quotient component support, not Grade-c implicit differentiation. Every admitted branch therefore includes a Grade-a-described implicit skill; small coefficients do not lower that description. Bounds are a limited planner-chosen subset, not grade cut-offs.

| Native official source | Locator and what it proves |
|---|---|
| 2025 P2 Q5 | Question PDF/printed5; report PDF359/printed357. Unsupplied implicit exponential gradient at a supplied point, five awards M1/A1/B1/M1/A1. Substitution before isolation is allowed; final A1 is C.A.O., not an independent answer-only concession. |
| 2023 P2 Q8(a,b) | Question PDF/printed14; report PDF339/printed337. Four-mark answer-given derivative proof: M1 product rule, A1 product result, B1 remaining derivative/zero, E1 correctly established target; then two-mark point-gradient substitution. 'Allow one slip, not omission of' stays on the product-rule M1. |
| **2021 P2 Q10(a,b), newly read** | Question PDF/printed12; report PDF241/printed239. Implicit derivative show-that then **normal** with y-recovery. Normal official M1 perpendicular gradient, DM1 line through point using their perpendicular gradient, A1 correct equivalent equation. This establishes an examination-observed normal facet; it is not textbook-only. |
| **2021 P1 Q11(b), newly read** | Question PDF/printed13; report PDF234/printed232. Explicit rational curve normal at supplied point: M1 calculus/perpendicular gradient, M1 complete line method using their perpendicular gradient, A1. Corroborates three normal marks; it does not become a literal implicit-function same-type label. |
| General rules, newly read | Reports2021 PDF236/printed234, 2025 PDF355/printed353, 2024 PDF335/printed333; apply OD-1 and complete method/answer-given working rules through MR01/09. |

Exact source paths, PDF/render hashes, printed pages, original criterion IDs and all official qualifiers are in `planning/calculus-source-reads.json`, appended D1 records. D1 read every accepted official member of `8227:FAMILY:implicit`; previous D0 all-member textbook reads remain: Goldie4D Q2/Q3/Q6 PDF121/printed107, YM Example29/Try29 Q1–3 PDF510/printed498. Discovery uses accepted assessed/component union links, not only relations. Unread wider union hits stay leads. Family distinction/precision prose, rejection templates and extracted notes are not design evidence.

### Branch-specific references

Gradient-only has the proposed part label **'Gradient part: same type as NSSCAS Mathematics 8227, 2025 Paper 2, Question 5, page 5'**, tied to its four direct demands, numeric response, unsupplied derivative and stated point. Restricting k to2/3 preserves the chain demand. The exact source tuple is excluded below.

The extended branch now supplies a show-that derivative before its two-mark gradient substitution. Its former five-mark gradient label is **withdrawn**, not inherited: its givens/awards differ from2025Q5. 2023Q8(a,b), 2021Q10(a,b) and2021Q11(b) remain **related/internal**, with full fields and learner_display:false. They establish the observed show-that/normal facets but differ in primitive, point recovery or scaffold. A source-part badge must never be rendered as a whole-card badge. E/F tests check actual label location (calc1-11); no currently eligible normal-branch same-type label is fabricated.

## Assessed parts, objectives, prerequisites and Bloom

| Branch / stable part | Primary objective / other directly assessed objectives | Direct demand IDs | Prerequisite demand IDs and role | Marks / proposed Bloom / criterion suffixes |
|---|---|---|---|---|
| `gradient / gradient` | `8227:2020:M2:T4:O03`; other `8227:2020:M2:T4:O01`, `8227:2020:M2:T4:O02` | `8227:2020:M2:T4:O03:D01`, `8227:2020:M2:T4:O02:D01`, `8227:2020:M2:T4:O01:D02`, `8227:2020:M2:T4:O03:D03` | `8227:2020:M2:T4:O01:D01` (prerequisite/support only), `8227:2020:M1:T8:O02:D01` (prerequisite/support only) | 5 / 3 / G1, G2, G3, G4, G5 |
| `normal / show-derivative` | `8227:2020:M2:T4:O03`; other `8227:2020:M2:T4:O01`, `8227:2020:M2:T4:O02` | `8227:2020:M2:T4:O03:D01`, `8227:2020:M2:T4:O02:D01`, `8227:2020:M2:T4:O01:D02` | `8227:2020:M2:T4:O01:D01` (prerequisite/support only), `8227:2020:M1:T8:O02:D01` (prerequisite/support only) | 4 / 3 / S1, S2, S3, S4 |
| `normal / gradient` | `8227:2020:M2:T4:O03`; other `8227:2020:M1:T8:O01` | `8227:2020:M2:T4:O03:D03`, `8227:2020:M1:T8:O01:D01` | `8227:2020:M2:T4:O03:D01` (prerequisite/support only), `8227:2020:M2:T4:O01:D02` (prerequisite/support only) | 2 / 3 / H1, H2 |
| `normal / normal` | `8227:2020:M1:T8:O03`; other `8227:2020:M2:T4:O03` | `8227:2020:M1:T8:O03:D01`, `8227:2020:M2:T4:O03:D03` | `8227:2020:M1:T8:O01:D01` (prerequisite/support only), `8227:2020:M2:T4:O03:D01` (prerequisite/support only) | 3 / 3 / N1, N2, N3 |

Each suffix is qualified as `recipe-id@0.1.1:branch-short:part-id:suffix`; display letters are separate. Primary/other roles, prerequisite roles and per-part Bloom rationale are canonical in `planning/calculus-design.json`; they are also stated here rather than deferred to a generic recipe rationale. No criterion from a sibling branch supports a part label.

- `gradient/gradient`: G1–G3 require the demonstrated derivative route; G4 applies the supplied point and G5 is canonical gradient accuracy after working. This is standard procedural application, not analysis from expression complexity.

- `normal/show-derivative`: S1–S3 demonstrate a complete valid differentiation route; S4 requires correct forward algebra establishing the supplied derivative. The routine answer-given derivation warrants Apply, not Evaluate merely because it says show.

- `normal/gradient`: H1 substitutes the stated point into the supplied derivative; H2 is the resulting canonical finite gradient. Earlier derivative work is not credited twice.

- `normal/normal`: N1 demonstrates the perpendicular gradient, N2 constructs the line through the given point using it, and N3 is canonical exact line accuracy. These are familiar linked applications.

Both branch maxima are proposed **Apply3** from their own complete parts. Establishing a routine supplied derivative is not automatically Analyse/Evaluate. A valid explicit-quadratic method may demonstrate a different method path; full task credit is not a claim that every optional method facet was demonstrated. Store the demonstrated path rather than fabricating product-rule evidence.

## Domains, discrimination and semantic capacity

Curve and point: $ae^{kx}y+y^2=C$, $C=q(q+a)$, $P=(0,q)$. Integer $a\in\{1,2,3,4\}$, $k\in\{2,3\}$, $q\in\{-5,-4,-3,-2,-1\}$. Exclude $a+2q=0$ (nonfinite gradient), $q=-a$ (zero constant/factorisation changes intended demand), and $(a,k,q)=(2,3,-5)$, the attributed2025Q5 original. Original exam questions are not served as fresh same-type variants.

Before repair D0 had **42 point-tasks on 36 curves**, not 42 curves. D1 starts with40 Cartesian tuples and admits **27 point-tasks on23 curves**. Four curves retain both possible negative y-axis points; their gradients differ. Neither a renamed point nor another seed makes another curve. Do not conflate point-task count, curve count and decision-level capacity.

| Branch / part | Raw tasks | Part semantic key and capacity | Strict complete-fresh upper bound |
|---|---:|---|---:|
| gradient / gradient |27| curve+supplied point `(a,k,C,q)`:27 |23 after the additional shared curve key `(a,k,C)` |
| normal / show-derivative |27| target differentiation identity `(a,k)`:8; C differentiates to zero and is not extra proof capacity |8 |
| normal / gradient |27| curve+point plus supplied-derivative application:27 |normal branch also limited by the8 unseen proof keys |
| normal / normal |27| curve+point and exact normal request:27 |normal branch also limited by the8 unseen proof keys |

All assessed part keys and the shared curve exposure key must be unseen for wholly fresh practice/test. Thus27 raw tuples do not promise27 wholly fresh complete extended questions. Branch bounds23 and 8 are not additive; shared curves/gradient exposure can reduce remaining capacity. The app must reserve keys atomically and report a shortage/exhaustion instead of silently switching branches. A reused component may be served only as disclosed after-feedback practice.

The discrimination script exhausts all27 tuples. Named error formulas omit the k chain factor; omit y' from y²; differentiate C as C; omit either product-rule contribution; reverse the gradient sign; negate instead of taking the negative reciprocal; or take the positive reciprocal. **None gives the canonical gradient/normal in any admitted tuple.** k=1 is rejected so the chain factor is live; the changed exemplar is now(3,3,-1), so its show-that identity is also distinct from the normal example. Copying the supplied derivative yields zero proof credit even though its final formula is canonical. Error detection uses visible method signatures as well as final values; do not infer a diagnosis from a correct number.

Given representation is text. Must read the whole exponent, the product by y, y², constant, supplied point, branch's displayed target and requested accuracy. No diagram is required. For the nearby vertical-turn curves C<0, a local branch boundary is $x_0=\ln(-4C/a^2)/(2k)$; **omit optional diagrams in this pilot** rather than render an unverified neighbourhood. A future diagram must resolve the correct local branch/turn and be separately checked (calc1-14).

## Stems and canonical working

Gradient-only: 'For the curve [equation], find its gradient at P, showing all working. Give an exact value or a correctly rounded3sf decimal.' One part,5 marks. Differentiate to

$$
ake^{kx}y+ae^{kx}y'+2yy'=0,\qquad m=-\frac{akq}{a+2q}.
$$

Extended normal branch: (show-derivative) 'Show that $y'=-ake^{kx}y/(ae^{kx}+2y)$, showing all necessary working' [4]; (gradient) '**Hence**, using the displayed derivative, find the gradient at P; exact or3sf' [2]; (normal) 'Find the **exact** equation of the normal at P, showing the perpendicular-gradient and line-construction steps' [3]. Total **4+2+3=9**, not4+5+3: the derivative awards are not repeated in the gradient part.

The normal is $y-q=\frac{a+2q}{akq}x$. Equivalent exact affine equations are accepted. No physical units apply. A correct3sf gradient can earn its A mark when working is present; keep the exact gradient for the exact normal. Premature rounding retains valid methods but loses the affected final exact-line A mark under MR05.

## Criterion and qualifier/deviation ledger

All criteria below are **adapted proposed** except their cited source conditions; owner design approval is pending. `AWARD` IDs are from `analysis/marking-conventions.json`, native source page identities from the reading manifest. No official general www or F.T. is invented where absent.

| Part / suffix | Award and evidence | Official source row / retained qualifier or named deviation |
|---|---|---|
| gradient-only/G1 |M1 product-rule attempt differentiating both factors |2025P2Q5 AWARD01: allow one numerical slip;2023Q8 AWARD01: not omission of a factor. |
| gradient-only/G2 |A1 correct exponential product derivative; depends on G1 |2025Q5 AWARD02, canonical derivative accuracy. |
| gradient-only/G3 |B1 $2yy'$ and derivative of constant0 visibly present |2025Q5 AWARD03, both required; no credit for unsupported slope alone. |
| gradient-only/G4 |M1 substitute P into a credible differentiated relation and solve |2025Q5 AWARD04: from at least G1 orG3; substitution before isolation accepted. |
| gradient-only/G5 |A1 canonical gradient after visible work; no F.T. |2025Q5 AWARD05 C.A.O.; MR01 makes bare answer=0. |
| show/S1 |M1 differentiate product, allow one numerical slip, not omitted contribution |2023P2Q8 AWARD01 condition retained. |
| show/S2 |A1 correct full product result |2023Q8 AWARD02; depends on valid S1. |
| show/S3 |B1 correct remaining y² derivative and zero constant derivative |Adapt2023Q8 AWARD03 (source4y rather than y²); **CALC-D1-DEV01**, preserves implicit chain evidence at same one-mark tariff. |
| show/S4 |A1 correctly establish supplied expression by complete forward algebra |2023Q8 AWARD04 is E1; **CALC-D1-DEV02** normalises terminal E to A without changing its proof requirement. Depends on S1–S3 all correct and complete; **no F.T. into given answer**. Copying/backwards manipulation earns0. |
| extended-gradient/H1 |M1 substitute P into the correct given derivative |2023Q8(b) AWARD05; source requires y-axis recovery whereas our point is supplied, **CALC-D1-DEV03**. Must use the displayed/prior formula because stem says hence; no official non-hence SC is identified, so bypass earns0 for this part. |
| extended-gradient/H2 |A1 canonical gradient after H1; no F.T. final accuracy |2023Q8(b) AWARD06. A failed proof does not prevent using the correctly displayed formula in this later part, but it does not restore S4 credit. |
| normal/N1 |M1 show perpendicular gradient $m_\perp=-1/m$ |2021P2Q10(b) AWARD04; their credible finite nonzero gradient allowed. A bare line or bare negative-reciprocal value without the step shown earns no M mark. |
| normal/N2 |DM1 complete line construction through supplied P using their perpendicular gradient |2021Q10 AWARD05 DM dependency retained: requires N1 and a valid point-line substitution. The source recovered y; P is supplied here, **CALC-D1-DEV04**. |
| normal/N3 |A1 canonical exact normal, equivalent line forms allowed |2021Q10 AWARD06; canonical accuracy, not F.T.; requires the visible normal path under MR01. |

Proof S4 is not a mark for merely writing the displayed answer. A derivative slip can retain S1/S3 but S4 stays0 even if the learner copies the given expression afterwards. Later H1/H2 may use the supplied correct derivative independently of the failed proof. Cue edges show→gradient→normal are distinct from N1/N2's limited formal follow-through. All paths fill each slot at most once; no sum of implicit and explicit methods.

Valid alternative in gradient-only: solve the original quadratic locally,

$$
y=\frac{-ae^{kx}+\sigma\sqrt{a^2e^{2kx}+4C}}2,\qquad \sigma=\operatorname{sign}(a+2q),
$$

then differentiate and substitute. Exclusive mapping G1 valid quadratic-solving attempt; G2 correct local root; G3 correct root/exponential chain derivative; G4 point substitution; G5 canonical gradient. This is **CALC-D1-DEV05**, a proposed alternative allocation rather than an official transcription. It earns the same5mark cap with complete working, not bare answers. In show-that, the explicit-root route instead must prove its derivative equals the displayed target, using $2y+ae^{kx}=\sigma\sqrt{a^2e^{2kx}+4C}$: S1 root derivation, S2 correct derivative, S3 that justified identity/substitution, S4 fully established target. Same4mark cap and complete-correct-working dependency. No such non-hence alternative bypasses the extended gradient's explicit hence instruction.

### Per-part answer-only and sample feedback

Under **D1-MR01/OD-1**, every part here has answer-only credit **0**: gradient-only0/5, copied show formula=0/4, extended gradient0/2, bare normal0/3. No official exception for this question type is identified. Visible linked working can earn only the criteria it actually establishes; do not infer M1 from a bare correct equation.

Normal tuple(3,2,-4): $m=-24/5$, normal $y+4=(5/24)x$. Full gradient-only working5/5; full extended proof4 + substitution2 + visible perpendicular slope and point-line3 =9/9. A wrong sign $m=24/5$ after valid work loses canonical gradient accuracy; a clearly shown $m_\perp=-5/24$ and line through P earns N1/N2=2/3, N3=0. A copied correct normal alone0/3 receives 'Your line is correct; show the perpendicular-gradient and line steps.' If the handwritten denominator could be3 or5, ask for clarification and preserve the original. Correct work gets confirmation, no invented repair. Complete normal/changed/boundary solutions and rejected cases are in `exemplars/WB8227-implicit-normal.md`.

## Shared policy, mode, checks and current stop

`subject-rules.md` **D1-MR01–09** controls answers-only, hence, misread, accuracy, premature rounding, requested units, multiple attempts, official qualifiers and answer-given proof. This work order specifies its per-part application; it does not replace that policy with an invented local exception. A misread may retain valid visible method awards, but the affected canonical accuracy fails; do not silently correct the input. When exactness is not requested, correct 3sf decimals with the required working can earn A. Exactness is explicit in each stem below where needed. No physical unit is requested for these dimensionless curves, so there is no hidden unit penalty. Mark the first uncancelled coherent attempt under MR07; ask for clarification on illegible signs or ambiguous alternatives.

Practice: offer answer-free reminders and a different-instance example before submission; do not leak the current derivative, normal, point or classification in hints/alt text. For a proof, the displayed target is deliberately part of the question, but its proof is not. After submission reveal the frozen solution and the first evidenced repair. A correct bare value with zero credit receives 'Your value is correct; show the working needed for credit', not a claim that it is wrong. A corrected/partly repeated task is after-feedback practice, not wholly unaided evidence. Another practice instance is permitted without a pass.

Test: preserve no help before submission and the existing question-by-question marking/review, paused marking time, early-advance/expiry rules and saved original attempts. App-owned semantic exposure keys include revealed examples and shared components across branches; all assessed part keys must be unseen for a wholly fresh test question. If any is seen, either disclose repeated-component practice or report exhaustion; never silently reset keys or relabel it fresh. Recipe progress remains once per completed round, not once per branch.

Use the pinned 7 November learner-text snapshots at `workbench/playbook/guidelines/provenance.json`, decoded LaTeX, meaningful action/reason/result and safe teacher/learner projections. Source artwork/textbook originals remain internal (`learner_display:false`). Attributed official exam originals remain separate from renewable fresh pools. No source PDF, accepted item-level mapping or review folder is changed here.

D1 checks are `planning/d1/calculus-design-check.py`, `calculus-domain-audit.json` and `calculus-exemplar-oracle.json`: exhaustive finite domain/semantic counts, named error collisions, all twelve changed paper cases by separate explicit-root/Taylor oracles, and explicit marking-evidence expectations. This is planner-side verification, not independent acceptance or a runtime grader. E/F still needs independent implementation oracles, seeds 0/1/42/2**63-1, at least64 valid draws or exhaustive smaller domains, real marking submissions, no-repeat reservations/exhaustion, actual notation/input/history rendering and role/reveal tests. Preserve negative fixtures and disclosed non-diagnostic cases. No applicable unrun runtime gate is called passed. Visual inclusion remains owner-approved but unverified capabilities stay in the app handoff. Stop for Claude's focused short check, then Vitalis's approval; do not commit or push.
