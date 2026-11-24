# Recover motion from acceleration or velocity and distinguish distance from displacement

NSSCAS Mathematics 8227, December 2020 syllabus; Grade 12. Owner Vitalis; PLANNER Codex (calculus assistant), 23 November 2026. Recipe `WB8227-motion-integration`, proposed version `0.1.0`; owner approval pending. This is a stage-D paper design, not an enabled recipe.

Partwise primary/other direct objective roles and criterion-linked Bloom rationales are explicitly recorded in [the pilot part evidence register](../planning/part-evidence-register.md) and its JSON. This supplements the specific criteria below; source-item links remain unchanged.

## Purpose, connected structure and sources

Selections `8227:SEL-D:motion-polynomial-chain`, `8227:SEL-D:motion-exponential-positive` and `8227:SEL-D:motion-interior-reversal`. One motion recipe with three explicit method/decision branches, not a separate recipe per part. A polynomial motion source trains integration and distance interpretation but does not by itself train an exponential primitive. Branch choice therefore resolves the direct demands, marking, capacity and Bloom before an instance can inherit metadata.

Syllabus PDF13 / printed10 M1:T9 O01/O02/O03/O04; exponential derivative PDF15 / printed12 M2:T4 O01, integration PDF16 / printed13 M2:T5 O01. Motion interpretation M1:T8 O03:D04 PDF12. Exact per-part demands and prerequisites in `planning/calculus-design.json`.

Official anchors read: 2021 P1 Q4(a,b), PDF/printed5, report2021 PDF232 / printed230,3+3; 2023 P2 Q9(a,b), PDF/printed15, report2023 PDF339 / printed337,2+3. The former report prints 'v=3,t=0' in one condition although paper initial velocity and final expression use2; the adaptation uses the actual supplied initial velocity u. This conflict remains disclosed, not propagated. The latter report credits either definite limits or an integration constant before evaluating distance; it notes omitted lower boundaries and missed exponential chain factors. Complete paths are alternatives, not additive credit.

All eleven members of five adopted motion families were read on native YM pages363–366,368,372 / printed351–354,356,360. They include Example37/Try37; Example39/Try39Q1; Example38/Try38Q1/Try39Q2/Exercise7Q11/Revision7Q4; Exercise7Q7; Try38Q2. The best reversal part is Exercise7Q7(c): total distance needs an internal sign split, unlike the positive-velocity exam. Source polynomial and exponential skills stay distinct. The reversal branch below simplifies the velocity to a linear function so a geometric independent check exists; it is a textbook-derived structural branch, not claimed same type as the source's whole question. Related reciprocal and greatest-height source parts are omitted, not erased from the objective map. The accepted assessed/component union discovery is preserved in the source-read manifest.

Grade limits: polynomial initial conditions fit Grade e `8227:GRADE:E:09` PDF23 / printed20 and Grade c `C:09` PDF21–22 / printed18–19; exponential primitive support `E:14` PDF23; upper combined motion/initial-condition and distance decisions stay within Grade a `A:09/A:10` PDF20 / printed17. These are calibration bounds, not grade promises. The reversal branch asks an extra sign decision; it is not random numerical difficulty.

## Branch domains, capacity and canonical targets

`WB8227-motion-integration:polynomial-chain`: supply a(t)=2At+B m s^-2, initial velocity u m s^-1, s(0)=0 at O and a requested T seconds. A∈{1,2,3}, B∈{0,1,2}, u∈{1,2,3,4}, T∈{1,2,3,4};144 identities. (velocity) find v(t),3; (distance) distance from O after T,3. Canonical v=At²+Bt+u, s=(A/3)t³+(B/2)t²+ut. All v>0 on t≥0, so distance=s(T); if negatives or a reversal are introduced, that is outside this branch. The second part depends on the first; keep them connected.

`WB8227-motion-integration:exponential-positive`: supply v(t)=V exp(-kt), with V∈{6,12,18,24,30}, k∈{1/4,1/2,1}, T∈{1,2,3,4}.60 identities. (acceleration) find a(t),2; (distance) distance in first T seconds,3. Canonical a=-kV exp(-kt); d=(V/k)(1-exp(-kT)). No reversal because v>0. Acceleration and distance share a stem but neither uses the other's answer, so no false part dependency. Decimal distance3 significant figures unless an exact form is requested; a correct exact expression is accepted.

`WB8227-motion-integration:interior-reversal`: supply v(t)=k(t-r) m s^-1 for0≤t≤T, positive coordinate direction stated. k∈{1,2,3}, r∈{1,2,3}, s∈{1,2,3}, T=r+s.27 identities. (rest) time of rest,1; (displacement) signed change,2; (distance) total distance,3. Canonical rest r; displacement k(s²-r²)/2; distance k(r²+s²)/2. Zero net displacement is admitted (s=r). Exclude k=0, r=0, T≤r, extra zeros and unsigned displacement: those change the decision/feasibility. The interior sign split, not a different story or coefficient, warrants this branch.

Total branch-qualified capacity144+60+27=231, without counting wording/context rewrites. Each branch's givens identify its parameter tuple uniquely. Use curriculum/recipe/version/branch/parameters and output-affecting engine/asset revision in the canonical fingerprint. The no-repeat registry is app-owned; exhaustion at144/60/27 fresh identities must be returned explicitly without silently relaxing constraints. Seeds are not evidence of distinctness.

Question representation: text, all values and units explicit. Must read whether the given function is a or v, initial v/u and s(0), integration interval, positive direction, and whether displacement or total distance is asked. No given diagram is required. A visual solution may show v against t with the zero at r and signed areas; axes must read t/s and v/(m s^-1), labels derive from the same k,r,T, and total distance uses absolute areas. It cannot contain a fixed source diagram inconsistent with a new tuple. A learner may show a labelled velocity graph/triangles as valid method evidence for the linear reversal; generic sketch upload alone is not runtime marking acceptance.

## Marking and answer-only evidence

All suffix criteria are scoped by recipe version and branch. Main and alternative routes fill the same awards; never add their totals.

| Branch/part | Awards and requirements |
|---|---|
| polynomial/velocity3 | V1 M1 integration attempt with a correct term (a correct final v implies it); V2 A1 correct general antiderivative; V3 A1 correct constant from initial u. A correct symbolic v alone encodes all3, because no method is prescribed. |
| polynomial/distance3 | S1 M1 integrate their credible v, at least one correct term; S2 A1 correct primitive (follow through a visible arithmetic error in v); S3 A1 canonical distance and appropriate metre unit. Numeric-only correct distance gives S3=1/3, not unshown integration evidence. |
| exponential/acceleration2 | E1 B1 correct coefficient -kV; E2 B1 unchanged exponential factor exp(-kt). Equivalent final expression earns2/2 without prose. |
| exponential/distance3 | E3 B1 correct primitive -V exp(-kt)/k; E4 M1 apply BOTH limits or fix s(0)=0; E5 A1 canonical final distance3sf or valid exact form with m. Numeric-only result earns E5=1/3. This preserves the official report's two exclusive full-credit routes. |
| reversal/rest1 | R1 B1 t=r with s (seconds), from v=0 or correct answer alone. |
| reversal/displacement2 | R2 M1 signed integral over 0..T (or signed triangle difference); R3 A1 canonical signed value with m. Numeric-only correct value earns R3=1/2. |
| reversal/distance3 | R4 M1 split at an interior zero and add nonnegative leg lengths (integrals or triangles); R5 A1 correct two leg magnitudes, may follow through a plausible arithmetic-error rest time from a visible zero calculation; R6 A1 canonical positive total with m. Numeric-only total earns R6=1/3. |

R4+R5 can follow through the learner's plausible single interior zero if a visible v=0 arithmetic attempt leads to it; R6 is canonical accuracy. A wrong split is not automatically full method credit from arbitrary numbers. No extra mark for separately repeating the zero solve. Rest→distance is a cue edge; R5 follow-through is separately typed. Displacement→distance is not a cue requiring reuse of signed displacement: it is a comparison of distinct outputs. Polynomial velocity→distance is cue plus explicitly limited S1/S2 follow-through. Source2021's worded 'their answer' does not make all final accuracy follow-through.

Units are m, s, m s^-1 and m s^-2; dimensional truth is checked. Keep intermediate exact precision; round only final nonexact distances. No hidden blanket unit penalty: final accuracy award includes the unit when requested; other valid method marks survive a single final unit omission. Handwritten m/s and ms^-1 are equivalent. If the task's response box supplies metres, the unit is already explicit and need not be rewritten.

Bloom proposed: all polynomial and exponential parts Level3 Apply, complete maximum 3. Reversal rest3, displacement3, distance4 Analyse because R4–R6 require separating signed displacement from two travelled legs and selecting a sign-aware decomposition. Maximum4 applies only to reversal. A support graph does not alone raise Bloom; retaining R4's assessed decision is required.

## Sample work and response-specific feedback

Polynomial normal a=4t+1,u=3,T=2: v=2t²+t+3 and d=40/3m gives 6/6 with credible integration evidence. A correct symbolic v with no prose earns 3/3; numeric distance alone40/3 earns 1/3. If v omits3, S1/S2 may still follow through visible integration, S3 fails. Feedback: enforce the given velocity when t=0, then keep that constant in the next integral.

Exponential normal V=12,k=1/2,T=2: a=-6e^(-t/2),d=24(1-e^-1)≈15.2m gives 5/5. An indefinite primitive with c determined by s(0)=0 is a full-credit alternative. Substituting onlyT gives -24/e: E3 only; feedback names the omitted lower boundary, not a guessed learning defect. Ambiguous notation '-1/2t' must be read against the printed exp(-t/2) and clarified if handwriting could mean -1/(2t).

Reversal normal v=2(t-1),T=3: rest1s, displacement3m, total5m gives 6/6. Correct signed integral3 presented as total distance loses R4–R6 but can earn the separate displacement marks; feedback: your net change is3m, while the travelled length includes the1m negative-direction leg and4m positive leg. Alternative velocity triangles earn full credit. If a submission has only '3,5' without labels, clarify which is displacement and distance rather than assigning them by guess. Full-credit work gets no repair.

All three branches have normal/changed/admitted-boundary examples in `exemplars/WB8227-motion-integration.md`. Supporting hints must use different numerical instances and retain branch-specific primitives; polynomial examples are not advertised as exponential-method practice.

## Practice, feedback and mode boundary

Before submission, offer answer-free method reminders or a worked example with a different branch-qualified fingerprint. Do not reveal current answers through hints, asset URLs, alt text or diagram labels. A learner may request another instance without first passing. Preserve original work; correction is an after-feedback observation, not evidence of unaided mastery. Full-credit work gets confirmation and no invented repair. For unclear handwriting or ambiguous units, request clarification rather than fabricate a mark. Test gives no hints/example/tutor on an unsubmitted question, retains question-by-question post-submission feedback and the existing review/timing rules; no test policy change is proposed.

## Guideline, validation and release requirements

Use the pinned learner-text authorities in `workbench/playbook/guidelines/provenance.json` and shared Bloom policy. Question, example, feedback, solution and history surfaces need decoded LaTeX and actual app-render inspection at E/F; a Markdown design is not that proof. Interpret source text from rendered pages, not the damaged notes or family distinction/precision templates. Newly authored wording is used here; owner-authorised exam originals may be shown only with their original attribution, never as generated variants. Textbook problem text/artwork remains internal (`learner_display: false`).

At E/F, independently check the full declared finite domains (all are below 1,000 tuples per branch), then replay seeds 0, 1, 42 and 2**63-1 and at least 64 valid draws per branch; small domains permit repeats in draw tests but not false claims of 64 distinct questions. Exhaust each small domain and verify safe exhaustion, no-repeat registry scope and exact answer equivalence. Freeze version, branch, parameters, deterministic engine/asset versions, seed and canonical fingerprint. Render sample/boundary/ambiguous responses. An oracle must use substitution/differentiation, explicit roots or geometric areas, not call the answer constructor twice.

Marking, Bloom and finite domain proposals need cross-vendor branch review and Vitalis's design approval. Automated resource checks, diagram input/feedback and application capability acceptance are unrun. Owner decision 6 includes visual work; nothing is silently held for capability. Flag actual runtime requirements to Vitalis through the common plan handoff. No runtime item, generator or deck is created by this work order.
