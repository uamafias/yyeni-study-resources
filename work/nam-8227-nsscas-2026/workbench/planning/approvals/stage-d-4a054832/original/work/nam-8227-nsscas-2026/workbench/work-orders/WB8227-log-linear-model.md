# Work order — WB8227-log-linear-model

NSSCAS Mathematics 8227, NIED December 2020; Grade 12. Owner Vitalis; PLANNER Codex, 24 November 2026. Proposed recipe version 0.1.4 and classification `8227-pilot-design-0.1.1`. Stage-D D4 repair only. Claude’s changed-scope confirmation comes before Vitalis approves the plan; no runtime authoring, imports, assignments, commit or push.

## Identity, retained selections and purpose

Recipe `WB8227-log-linear-model`; selections `8227:D:SEL:log-linear-model:graph-intercept` and `8227:D:SEL:log-linear-model:gradient-target`; accepted parents `8227:FAMILY:linearisation` and `8227:FAMILY:exponential-equations`. The two branches retain their supplied-model parameter-recovery purposes. Neither assesses construction of a model from an unstructured situation. They are not new recipes per number, graphic or mark.

`graph-intercept` disentangles a coupled slope/constant from a supplied transformed graph. `gradient-target` exponentiates the stated-base gradient and then uses the recovered parameter in a target equation. No Flashcard Studio input is used. Log-log/power fitting, noisy data, model choice and extrapolation remain later facets.

## Native evidence and qualifiers

Syllabus PDF 14/printed11, M2:T2:O04 and O03. Graph anchor2023 P2 Q4(a), paperPDF6: $y=Ae^{px+p}$, two labelled coordinates on $\ln y$ versus $x$; reportPDF334–335/printed332–333 gives the named log-product/intercept errors and B1 “state or imply”, M1 gradient, A1, **DM1** coordinate substitution to $A=e^{\text{constant}}$, A1, plus a simultaneous-equation alternative. Gradient anchor2025 P2 Q6(a),(b), paperPDF6; reportPDF359/printed357 gives B1 “state or imply”, M1 “state or imply” gradient, A1; then M1 F.T. their positive parameter and A1 c.a.o., with an exponential-law alternative. For eligible question-data misreads only, OD-6 A/B follow-through overrides that c.a.o. restriction; an independent named method error remains uncredited.

The exact paths/hashes/read dates are in `planning/trig-model-source-reads.json` D1 append; original diagrams were read, not text extraction. All D0 members of `logarithm-linearise-model` (9), `logarithm-line-constants` (12) and `exponential-affine-line-intersection` (3) were native-read;33 union candidate items include explicit unread leads. Textbook originals remain internal. Grade C:11/E:11 support log/index foundations; A:12 (syllabusPDF20) explicitly names linearisation and constant recovery. Proposed numeric bounds stay within supplied-form, exact-line algebra, not regression or a new change-of-base objective.

## Part identity, links and proposed Bloom

All IDs below are authoring identities, not display-order letters. The common contract resolves conditional links before an eventual instance is frozen.

### Branch `graph-intercept`

- Part `WB8227-log-linear-model:graph-intercept:g-parameters`; 5 marks; response `numeric`; primary `8227:2020:M2:T2:O04`; other direct objectives: none.
- Direct demand IDs: `8227:2020:M2:T2:O04:D01`, `8227:2020:M2:T2:O04:D02`.
- Prerequisite IDs: `8227:2020:M2:T2:O01:D02` (prerequisite or previously assessed result; no direct coverage in this part), `8227:2020:M2:T2:O02:D01` (prerequisite or previously assessed result; no direct coverage in this part).
- Proposed Bloom: Apply 3 using only G-B1 transformed equation stated/implied,G-M1/G-A1 gradient recovery,G-M2 dependent coordinate method and G-A2 recovered parameter accuracy; no sibling-branch criterion.
- Criterion IDs: `WB8227-log-linear-model:graph-intercept:g-parameters:G-B1`, `WB8227-log-linear-model:graph-intercept:g-parameters:G-M1`, `WB8227-log-linear-model:graph-intercept:g-parameters:G-A1`, `WB8227-log-linear-model:graph-intercept:g-parameters:G-M2`, `WB8227-log-linear-model:graph-intercept:g-parameters:G-A2`.

Branch maximum3 from its own classified parts; proposed only, never an average or a sibling maximum.

### Branch `gradient-target`

- Part `WB8227-log-linear-model:gradient-target:t-parameter`; 3 marks; response `symbolic`; primary `8227:2020:M2:T2:O04`; other direct objectives: none.
- Direct demand IDs: `8227:2020:M2:T2:O04:D01`, `8227:2020:M2:T2:O04:D02`.
- Prerequisite IDs: `8227:2020:M2:T2:O01:D01` (prerequisite or previously assessed result; no direct coverage in this part), `8227:2020:M2:T2:O01:D02` (prerequisite or previously assessed result; no direct coverage in this part).
- Proposed Bloom: Apply 3 using only T-B1 correctly transformed line stated/implied,T-M1 stated-base gradient relation and T-A1 parameter recovery; no graph-intercept or target criterion.
- Criterion IDs: `WB8227-log-linear-model:gradient-target:t-parameter:T-B1`, `WB8227-log-linear-model:gradient-target:t-parameter:T-M1`, `WB8227-log-linear-model:gradient-target:t-parameter:T-A1`.
- Part `WB8227-log-linear-model:gradient-target:t-target`; 2 marks; response `numeric`; primary `8227:2020:M2:T2:O03`; other direct objectives: none.
- Direct demand IDs: `8227:2020:M2:T2:O03:D01`.
- Prerequisite IDs: `8227:2020:M2:T2:O01:D02` (prerequisite or previously assessed result; no direct coverage in this part), `8227:2020:M2:T2:O04:D02` (prerequisite or previously assessed result; no direct coverage in this part).
- Proposed Bloom: Apply 3 using only U-M1 follow-through substitution of their positive a!=1 into the model/target and U-A1 canonical x; earlier part is prerequisite rather than a repeated Bloom rationale.
- Criterion IDs: `WB8227-log-linear-model:gradient-target:t-target:U-M1`, `WB8227-log-linear-model:gradient-target:t-target:U-A1`.

Branch maximum3 from its own classified parts; proposed only, never an average or a sibling maximum.

## Graph-intercept domain, assets and semantic keys

Given $y=Ae^{px+p}$, $A>0$. Let $L=\ln A\in\{-1,1/2,1,2,3\}$ and $p\in\{-3/4,-1/2,-1/4,1/4,1/2,3/4\}$. Exact graph labels are $(x_i,u_i)$ on axes $x$ and $\ln y$, where $x_1\in\{1,2,3\}$, $x_2=x_1+d$ and $d\in\{1,2,3\}$, $u_i=px_i+p+L$. Use exact decimal point labels, so a quarter is displayed as0.25, not an ambiguous measured value. Every stem retains $A>0$ and asks for parameter values, with three-significant-figure non-exact decimals; exact equivalents remain accepted.

Capacity30 model identities and270 coordinate presentations; do not count270 fresh models. There are five recovered amplitude values and six gradient values, not30 distinct reasoning methods. D1 replaces $L=0$ with $L=1/2$: at zero, the report’s wrong log-product model $u=Ap(x+1)$ can recover the correct parameter pair; all 6 such models/54 presentations are removed and six noninteger-log models/54 presentations added. This also exposes a non-integer recovered logarithm rather than only $e^{\text{integer}}$. The remaining finite five-value amplitude limitation is disclosed.

No-repeat part key is $(L,p,\text{coupled model},\text{transformed axes})$; a new point pair is a presentation, not fresh parameter work. At30 exposed models return exhausted or clearly disclose repeat practice. Future expansion of logarithm values needs a new bounded domain/review, not silent stochastic perturbation.

R3-07 diagram must-read givens: horizontal $x$, vertical $\ln y$, both exact labelled coordinates and their common straight line. Fixed: Cartesian axes, explicit logarithm, exact coordinate labels, schematic/no measurement. Variable: the exact model/point data, line direction and viewport. Relations: both points lie on $u=px+p+L$, $x_2>x_1$, negative/zero ordinates remain visible, and no hidden $A,p$ appear in labels or accessibility text. Zero-ordinate points need labels placed away from both line and axis. Labels must be offset to the side away from the line; **no opaque label box may cover the line**. Stage E/F must test bounding-box/line/axis intersection on every admitted presentation. The three current paper SVGs use offset transparent labels; they are static examples, not a runtime renderer.

## Graph-intercept solution and source-qualified memo

Take logs: $\ln y=px+p+\ln A$. Calculate $p$ from the two points; find intercept $b=u_1-px_1$; then $\ln A=b-p$ and $A=e^{b-p}$. A simultaneous solution of the two coordinate equations is equally valid. The independent oracle substitutes recovered values into the original exponential at both abscissae.

| Criterion | Award | Exact qualifier retained |
|---|---|---|
| G-B1 | B1 | Correct transformed equation **stated or implied** by visible work; correct coordinate equations may imply it, bare parameter values may not |
| G-M1 | M1 | Identify $p$ with the gradient and attempt the gradient from the labelled points; simultaneous-equation alternative: two appropriate equations and solving, allow one slip as in the source |
| G-A1 | A1 | Canonical correct $p$ with eligible working |
| G-M2 | **DM1**, dependent on G-M1 | Substitute a coordinate coherently and simplify to $A=e^k$ for constant $k$; an earlier coherent transformed-line or parameter slip does not itself destroy this method mark |
| G-A2 | A1 | Canonical correct $A$, exact equivalent or correct3 sf decimal; the coupled $+p$ is required for this accuracy, not an extra exclusion on DM1 |

The source’s DM1 is not replaced by a stricter “must include the correct+p or no method credit” test. A wrong line omitting $p$, followed by correct gradient and coherent coordinate substitution to a wrong amplitude, can earn G-M1/G-A1/G-M2=3/5, not G-B1/G-A2. Conversely a correct complete line followed by an algebraic offset slip retains independently earned line and method credit; only canonical accuracy fails. Alternatives fill the same slots, maximum5; no duplicate-method sum.

Answer-only for this single5 mark part is0 under D1-MR01; there is no official bare-parameter exception. “State or imply” means evidence in visible work, not guessing a line from the final numbers. Premature rounding loses the affected A only under D1-MR05; genuine question-data misreads use OD-6 below. $\exp/\ln$ inverse properties are explicit prerequisites in the JSON, not omitted hidden knowledge.

## Gradient-target domain, exposure and wording

Given $y=b^{ca}a^x$, $a>0$, and gradient $m$ on a graph of $\log_b y$ against $x$. Set $b\in\{2,3\}$, $m\in\{2,3\}$, $c\in\{1,3\}$, $q\in\{0,1,4,10,30\}$; target $y=b^q$, displayed as an unevaluated integer power when large. Exclude $b^m=bm$ and $b^m=m^b$. Only $(b,m)=(2,3)$ and $(3,2)$ remain. The 40 grid tuples reduce to 20 diagnostic full tuples, four model triples $(b,c,m)$ and two exponentiation subdecision contexts $(b,m)$. No target equals the prefactor, so $x=0$ is not an inspection shortcut. Both signs of $x$ occur; large powers need not be calculated.

The original tuple $(3,2,2,4)$ is explicitly excluded. Also $c=2$ is absent, so the exact2025 parameter subpart is not recycled by changing only the target. The revised boundary uses $c=3$, not the verbatim original part(a). Maximal $ca=27$ and $q=30$ remain integer-symbolic arithmetic; no giant decimal input is required. This is a diagnostic domain repair, not additional subject scope.

Every exemplar stem retains “$a$ is positive”, exact parameter request in(a), and **“Hence”** for(b). Part(b) does not request an exact answer: an exact fraction or correct3 sf decimal is accepted. Textual must-read givens: plotted log base, both plotted variables, stated gradient, full prefactor and target. Do not substitute a fake graph or change the base in alt text.

Part(a) no-repeat key $(b,c,m,\text{model form})$ has 4 contexts; its exponentiation subdecision key $(b,m)$ has 2. Part(b) key $(b,c,m,q,\text{hence})$ has 20 equation contexts, with answer collisions reported separately. A new $q$ repeats the parameter part and cannot be wholly fresh evidence after that part is revealed. These are numeric tasks within one supplied-model decision, not20 cognitive types. Exhaust or explicitly disclose repeats at the relevant part key.

## Gradient-target solution, alternatives and memo

Canonical line: $\log_b y=ca+x\log_b a$. Match $\log_b a=m$ and recover $a=b^m$. Hence $q=ca+mx$, so $x=(q-ca)/m$. Direct index laws also work, using the result from(a).

A correct $\ln$ or $\lg$ route earns the same awards: for example $\ln y=ca\ln b+x\ln a$, and the gradient of the **plotted** ordinate is $\ln a/\ln b=m$, hence $a=e^{m\ln b}$. This is a valid alternative calculator/algebra method, not a new required change-of-base learning objective or prescribed procedure. LIMIT06 is not a licence to reject correct mathematics. Treating the plotted gradient as $\ln a$ or $\lg a$ without the required base conversion is the error; merely seeing $\ln$ is not an error.

| Criterion | Award | Exact qualifier retained |
|---|---|---|
| T-B1 | B1 | Correct transformed line **stated or implied** by visible model/coordinate work; an equivalent correct $\ln/\lg$ transformation is accepted |
| T-M1 | M1 | State or imply the actual gradient relation $\log_b a=m$, including the correct ratio $\ln a/\ln b=m$ for an alternative base |
| T-A1 | A1 | Correct exact $a$ with eligible method evidence |
| U-M1 | M1 F.T. | Use their positive $a\ne1$ and the given target in their log-equation (from (a), or a correct one written in (b)), or the original/exponent equation; the earlier result must be used by the “Hence” stem |
| U-A1 | A1 c.a.o. (OD-6 eligible-misread F.T. excepted) | Canonical $x$; exact or correctly rounded3 sf decimal when needed, with eligible working |

Part totals3+2=5. State/imply is not an answer-only exception: bare $a$ earns0/3; bare $x$ earns0/2. No SC is printed for bypassing “Hence” here; do not transfer another question’s SC1. The exponential and log routes fill the same U-M1 slot. A correctly stated earlier result reused visibly may supply the dependency evidence; a marker must not invent unseen substitution.

Sample normal: $b=2,c=1,m=3,q=10$, so $a=8$ and $x=2/3\approx0.667$. A correct $\ln$-ratio route earns all 5. A student who visibly writes $\log_2a=3$ then $a=2\cdot3=6$ loses T-A1; consistent target substitution may retain U-M1 F.T., but not canonical U-A1. If the prefactor was retained in (a) and is newly omitted only in (b), U-M1 is not earned. If their own (a) line already omitted it, consistent substitution into that earlier line earns U-M1 F.T.; do not penalise the same line error twice. Canonical U-A1 still fails when the resulting value is wrong. A bare correct pair earns0, with feedback recognising correctness and asking for the method. Unreadable signs stay pending.

D1 ledger: G/T state-or-imply and G-DM1 are aligned with the actual official rows, not named deviations. The new coefficients/targets, finite discriminating domain and coordinate formatting are disclosed adaptations. All new/changed examples, three graphs and source/exclusion checks are linked in [the exemplar](../exemplars/WB8227-log-linear-model.md) and `planning/d2/trig-d2-check.py`. The optional extension to many more logarithm values remains later work; the five-amplitude limitation is explicit. Stage E/F graph label/axis overlap and runtime exact/decimal input checks remain unrun acceptance requirements.

## Shared delivery, feedback and later validation

[recipe-contract.md](../recipe-contract.md), [subject-rules.md](../subject-rules.md) D1-MR01–09 and OD-1–OD-6 govern; the local qualifier/deviation ledger below specifies the actual adapted rows. The 7 November 2026 guideline snapshots and `workbench/playbook/guidelines/provenance.json` remain the text authority. Mathematical solutions use decoded LaTeX; no mathematics inside emphasis. These paper records do not claim an implemented metadata schema or marker.

Practice permits a new admitted instance without passing first. Current-instance hints are answer-free; a worked example uses a different semantic identity. Show solution and criterion feedback after submission, preserve the original response, acknowledge a correct bare answer and request its working under OD-1. A later repetition after feedback is not wholly unaided evidence. Ambiguous handwriting or an unclear sign stays pending clarification, not zero by assumption. Full-credit work gets no invented repair.

Workbench Test keeps no hints/example/tutor before submission; preserve question-by-question post-submission review, marking-time pause and existing nonfinal two-minute review/advance/expiry behavior. The app owns attempts, progress, no-repeat history, reservations and once-per-recipe-round credit. No resource field silently changes these policies.

Later E/F: independently enumerate admitted domains; verify mathematics, method/accuracy/dependency paths, answer-only zero, exactness, misread/rounding/extra-answer examples and semantic no-repeat. Replay seeds0,1,42 and2**63-1 once implemented, with at least64 draws per branch or exhaust smaller spaces. A separate oracle must not call the future answer constructor. Validate actual notation input/rendering, role-safe assets, solution reveal and grading. The D4 script is a design checker, not a question generator or runtime marker. Applicable runtime checks are not run now.

Textbook originals and images remain internal (`learner_display:false`). Exact exam originals require their own attribution and are outside the fresh pools; a same-type label never authorises unattributed verbatim reuse. Source findings and accepted item-level links are not retagged. Family templates, rejection notes and extracted prose are not design evidence. D0 whole-family page reads/union leads are preserved in `planning/trig-model-source-reads.json`; the D1 append records the current native marking reads. No whole-syllabus coverage or learning-effectiveness claim follows.

## D2 follow-through and misread fixtures

For the normal case, a learner may write the wrong earlier line $\log_2y=x\log_2a$, then correctly use $\log_2a=3$ and obtain $a=8$. T-B1 fails for the missing prefactor, but T-M1/T-A1 survive. Substituting the target into that same earlier line, $10=3x$, earns U-M1 F.T.; the wrong $x=10/3$ loses canonical U-A1. Total 3/5. If the learner instead wrote the correct earlier line $\log_2y=a+x\log_2a$ and newly dropped $a$ only when substituting in (b), U-M1 fails: this is a new substitution error, not F.T.

**MR03 misread — authority and proposed mechanics.** Binding OD-6 principle: a genuine misread of question data with unchanged object and difficulty costs one mark from A/B; all A/B follow through on the misread value and M/DM are judged as usual. Own-figure errors and misreads changing object/difficulty receive ordinary canonical marking. Practice feedback names the misread. Proposed MR03 operational rules, pending Vitalis approval of the exact manifest: decide and record eligibility once at first use; ineligible data remain canonical in every later part. For each eligible misread datum, first mark all gross evidence and dependencies, then deduct one mark from the first earned A/B on that datum in question/criterion order, moving to later-use parts if necessary. Deduct nothing only if no A/B is earned on the datum anywhere. Never deduct from M/DM or make the score negative. The selected criterion remains earned for every DM, dependency and www check; one datum costs at most one net mark. Eligible OD-6 follow-through overrides not-F.T. and c.a.o. restrictions, while correct working, named method exclusions and OD-1 still apply. No-solution exclusion means a misread removes a solution the canonical question has; a designed no-real-solution outcome remains eligible when its demand and difficulty are preserved. An A/B is on a datum when it lies in the datum's first-use part or a later part whose working uses the misread data, whether or not that criterion's own value changes. Eligibility is judged at first use for the connected question. Eligible follow-through never overrides MR09 (no F.T. into a supplied result) or OD-1 answer-only rules. Sources: NSSCAS 2025 report PDF345 item4 (CONVENTION108) and comparable Cambridge 9709_m16_ms_12.pdf PDF3 Penalties; the comparable allocation is not a published Namibian rule.

Domain authority: the narrow gradient-target domain is reviewer-prescribed (step-3 calc2-08), disclosed above; owner approval is pending. It is not owner-fixed.
