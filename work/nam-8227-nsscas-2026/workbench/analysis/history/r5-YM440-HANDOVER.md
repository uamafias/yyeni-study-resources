# Handover — NSSCAS Mathematics 8227, repair round 5

Role: AUTHOR (Codex). Owner: Vitalis. Workspace: `work/nam-8227-nsscas-2026/`.
Commission: `workbench/review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.
Work is active. No owner-only decision blocks progress.

## Current checkpoint

2026-11-20 — YM440 verified checkpoint: 746/891 pages author-censused, 145 pending; 4,728 responses / 1,803 response items; 3,425 source records / 3,059 individual mapping reviews; 217 source defect/caution entries. Focused93669 passes. Full28923 through435 passed 2×195 commands, 134 byte-identical outputs and 29 rejected negative fixtures; archived as analysis/history/rebuild-verification-r5-YM435.json. Linearisation/fitted-model builders through440 are wired and focused-checked. Confirmed Example33 b=10^0.3→2.00, not1.20; Try33Q2 p≈3.1, not0.0123. Graph estimates remain approximate. Try33Q1 negative exponent and Try32Q2 coordinate2.2 cleared earlier false leads. Next441 basic-exercise draft passes math-only80959, UNWIRED. Sources through443 and keys637–644 read;444–447 rendered but unread. T5/T6, whole-book metadata audit and independent acceptance remain open; no step3, commits or pushes.

## Exact continuation

No active full rebuild. Latest full proof through435 is archived; latest focused through440 passes. No incomplete wired source builder through440.

Next unfinished census441. `tools/textbook-r5/author_YM_C9_exercise_basic.py` covers all Exercise9Q1–10 and one teaching note; 10items/27responses. Draft math-only80959 PASSED, but no JSON generated and it is UNWIRED. Before wiring, register the confirmed source defects against native crops:
- Q1(a), source441/key640: source log(5a), key log5+logb; correct log5+loga. `YM-C9-Ex9Q1-Q2-key-native` confirms.
- Q4(c), source441/key641: source a^(−1/4)=b; nativekey log_a(b)=−14. Correct−1/4. `YM-C9-Ex9Q3-Q8-key-native` and `YM-C9-Ex9Q5-Q10-native` read; need native sourceQ4 crop before exact publisher claim if not yet available.
- Q6(a) log_3(x^4) has no inverse on its literal full real domainx≠0. Positive key root is conditional on x>0; preserve missing-branch caution, not an unexplained numeric wrong-key classification.
- Q8 captionx≈1.8 is wrong; original e^x=5−5x has unique root0.6259832407 within0..1. Its drawn intersection is near.63 and mathematically correct. Source requests0..1,0.5step;keygraph extends further. Native source/key crops read. Runnable bisection included in draft.
Draft warnings: replace prose R\{0} invalid escape with 'nonzero reals'. Q5(b) native exponent−5x; Q6(c) native exponentx/3, not(x−1)/3. Both cleared/recorded.

Then442 Exercise9Q11–15 (source and key641 read, no draft): Q11 axes unspecified; key assumes log10y versuslog10x and givesp2.82,q3, x.452for y.26. Q12 k>0 original logdomains eliminate key’s−2k, leaving3k/2. Q13model A e^(p(x−1)) means interceptlnA−p; points(2,1.60),(5,2.92)givep.44,A=e^1.16≈3.2 to2sf. Q14 output-reflected log/inverse/sketch. Q15logy versusx through(−1,0),(0,1): logy=x+1,y10^(x+1), y1000atx2.
Source443 examstyle Example34/Try34Q1–3 read. 444–447 rendered `YM-C9-444-source.png`, NOT READ; no source after443 read. Key641–644 contact read, but C10 content only incidental preview, not source census. Extend local evidence mapping when using641+; do not reuse key637 contact for641. The draft basic exercise already has correct local ev override.

Latest436–440 batch: 11 response items/27 responses,26 panels. 436–438 linearisation 7items/16responses/17panels;439–440 fits4items/11responses/9panels. Actual supplied transformed axes are not rawx,y. Parameter degeneraciesb0/a1 recorded. Estimate uncertainty is preserved; sourcek1.58 from chosenline is not wrong merely because rawdataregression yields1.50. Native Try33Q1 ORIGINAL y=k a^(−x) explains decreasing scatter witha2.12; no sign error. Native Try32Q2 diagram and text BOTH2.2,not2.4. Source issues registered217 total, not217 numeric key errors.

C8 complete author population376–406:31pages/101responseitems/308responses/64teachingpanels/11examstyleitems/Revision8=30marks. C7 population322–375 complete; full proofs archived. Both books still await independent acceptance and T5/T6/full metadata audit. Frozen analysis-snapshot staysR4 untilT6. No owner blocker. No commit/push.

## Source issues to preserve

- Example13, PDF282: 3/cuberoot(x+1) at x=−2 has ordinate −3 and derivative −1. Correct tangent: −x−5; normal: x−1. The book drops a minus sign and swaps them. Both wrong lines still pass through the point, so incidence alone misses the error. Use the real negative-root branch, not a principal complex power.
- Try12 Q4, PDF282: literal stem asks for tangents, but the surrounding normal section and keys give normals. Literal tangents: −4x+9 and 3x+9. Context-intended normals: x/4+19/4 and −x/3+17/3. Both interpretations are recorded; do not silently rewrite the source.
- Try22 Q1, PDF292/key621: numeric 6.4pi is correct; printed cm/s must be cm²/s. Unit comparison correctly makes this key-wrong.
- Example18(b), PDF288: 3/(2x+5) decreases on each pole-separated component, not across the disconnected union. Try18 Q2's cubic is strictly increasing despite one zero derivative; that is not a defect.
- Example24, PDF294: cancellation of the rate ratio requires a nonzero rate. The resulting x=1 and 9/4 are correct under that condition.
- PDF291: signed displacement derivative is velocity; speed is its absolute value. Negative acceleration alone does not prove deceleration. PDF296: stationary does not necessarily mean turning.
- Example26, PDF297: maximum (−1,10), minimum (3,−22), y-intercept5; coordinates, nature and SKETCH are all asked. Source uses first-derivative sign changes; second derivatives independently confirm the classification.
- PDF269's prose point (x,x+h) is wrong for y=x²; its displayed derivation uses correct points. Try7 Q1 on277 gives off-curve point (3,7); correct point is (3,25), with gradient15 still valid at x3.
- Try1(f)'s exponent −4/5 and its key are correct (native crops read). Investigation chord slopes5 and3 approach4. Its screenshot5.01 is approximate, not an exact key for B(3,9). The translated-curve extension has an author-derived no-key answer.
- First-principles proof is optional under LIMIT03. Source claims about all real powers do not extend the syllabus's rational-power scope. Source presentation advice about negative exponents/double fractions is not an official marking rule.

## Completed PDF302–305 notes to preserve

- Try29 Q2 supplies dy/dx=−x²+5x−4. Only stationary x-values1,4 are asked; second derivative −2x+5 classifies minimum at1, maximum at4. No ordinates can be inferred without a curve constant, and none are requested.
- Example30: y=8x+(2x−1)^−1; stationary x=1/4 (maximum), 3/4 (minimum), excluding pole1/2. No ordinates requested. Try30 Q1 similarly asks x and nature for (2x−3)³−6x: x1 maximum, x2 minimum.
- Try30 Q2: y=8sqrt(x)−2x, stationary point (4,8), maximum; asks second derivative and classification. Q3: y=1/(x−3)+x; first/second derivative, maximum A(2,1), minimum B(4,5).
- Example31 gives fprime(x)=2x²+kx−12 and stationary P(3,−10): k=−2, other stationary x=−2; fsecond=4x−2, P minimum and Q maximum. Q's ordinate is not asked.
- Try31 Q1: a nonzero, fprime=ax²+a²x and stationary x3 imply a=−3 (reject0). Q2's minimum (2,−4) gives a1,b−3. Q3's stationary abscissas−1,3 give b−3,c−9. Q4's graph has a double root at D(2,0); f=(x+3)(x−2)², coefficients1,−1,−8,12, maximum B(−4/3,500/27).
- Example32: closed block base2x by x, volume72cm³, positive x. h=36/x²; total area4x²+216/x; stationary x3, minimum area108cm². The block diagram appears in the SOLUTION; the given is text. Keep all six faces and positive dimensions.

## Working procedure and boundaries

Use the existing PDF render tools and read the images; rendering alone is not a census. Source files stay unchanged. Fixed-source author scripts go under `tools/textbook-r5/`; wire completed scripts into `run_repair_checks.py`. Existing IDs need correction records; recovered missing items need new metadata. Aggregate assessed/component IDs must be disjoint. Use registered prerequisite IDs and actual source values for qualifier decisions. Preserve real odd-root branches and original domains.

Focused checks: answer verifier (plus relevant independent checks), inventory, census, progress, R4, then R5 `--stage textbook-working`. The full runner rebuilds twice and tests 29 seeded errors. The common YM printed-page helper accounts for duplicate scan139; do not restore the old late-page minus11 offset.

**Checkpoints:** Vitalis requested at most roughly100 pages between saves. Save more often at verified batches and pauses; update HANDOVER/STATUS and archive useful proof/history. Distinguish rendered, read, author-verified, deterministic rebuild and independent acceptance.

No commit or push; Vitalis commits. No PLAN, recipe contract, recipes, runtime generators, work orders, imports or learner assignments. Both textbooks must be complete AND independently accepted before step3. Do not modify review folders, source PDFs/root textbook, standard, other subjects, app or pinned checkouts. Preserve unrelated work.

Both textbook hashes, all19 protected review hashes and HEAD were rechecked unchanged after YM341. HEAD: `11cd03fe639f9936dd9f83fd04bd6f04d5181676`. Part1 remains821 award rows (818 official/3 derived),42 E flags,95 marking rules,31 confirmed Cambridge pairs across29 NSSCAS questions; independent acceptance pending. Earlier source resolutions and cleared false positives are preserved in `analysis/history/r5-YM297-HANDOVER.md` and prior checkpoints. Working synthesis: `analysis/textbook-insight-working-notes-r5.md`.
