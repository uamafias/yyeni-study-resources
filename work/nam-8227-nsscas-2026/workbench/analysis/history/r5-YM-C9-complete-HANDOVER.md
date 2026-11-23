# Handover — NSSCAS Mathematics 8227, repair round 5

Role: AUTHOR (Codex). Owner: Vitalis. Workspace: `work/nam-8227-nsscas-2026/`.
Commission: `workbench/review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.
Work is active. No owner-only decision blocks progress.

## Current checkpoint

2026-11-20 — C9 author-population checkpoint447: 753/891 pages author-censused, 138 pending; 4,795 responses / 1,832 response items; 3,446 source records / 3,109 individual mapping reviews; 225 source defect/caution entries. Statuses: 3,983 matches, 311 sketch, 312 show/prove, 91 key wrong, 44 no key, 54 key incomplete. C9 covers41pages,122responseitems/328responses and127panels (114teaching,13given);14 textbook exam-style items;Revision9=30marks. All source builders through447 are wired. Focused27168 caught two missing subpart metadata fields on new source cautions; repaired, R5check37313 passed; targeted dependent regeneration18891 follows. No mathematics or checker relaxation was needed. Full28923through435 passed2×195/134identical/29negatives and is archived. Source448–451read,nextC10openingdraft;no source after451read. Independent acceptance, whole-book metadata audits, T5families/138-demand synthesis and T6fresh-copy/final snapshot remain open. No step3, commits or pushes.

## Exact continuation

C9 author population is complete through447: mapping/answer metadata true, whole_chapter_complete false because independent acceptance and T5/T6 remain open. Five new source builders since435:linearisation436–438,fittedmodels439–440,exercisebasic441,exercisemodels442,closing443–447. All wired and mathchecked. Full double rebuild through447 is the next validation (200commands per run,134outputs,29negativefixtures); do not edit wired/globbed inputs or analysisroot JSON/MD while it runs. New renders and UNWIRED.py drafts are safe. Last full proof through435 is archived atanalysis/history/rebuild-verification-r5-YM435.json.

Next unfinished census448. C10source448–451rendered/read inYM-C10-448-source.png. No source after451 read. Corresponding keys642–644 are read inYM-C9-key-641.png;use accurate evidence mapping,notkey637. No C10draft written yet. Chapter title448 has no task. 449definitionscosec/sec/cotandExample1secgraph0..360degrees. 450Try1cosec0..360degrees,Example2cot0..2pi,Try2cot2x0..2pi,Example3showone rootcosecx=3−x on0<x<pi/2bysharedsketch. 451Try3showone rootcotx=4x−2 onthatopenradianinterval,thenaddition-formula triangle/area derivation reference panels and worked boxed instructions.

C10 graph reasoning:cot=cos/sin extends through tan’s poles,so naive1/tan formula is only common-domain equality. Cosec/sec undefined where sin/coszero. Cosec rootcount must not be justified merely by comparing two decreasing curves. Forf=cscx+x−3, derivative1−cosx/sin²xhasonezero withcosx=(sqrt5−1)/2;fendpointpi/2=pi/2−2<0andinitiallimit+infinity,so exactlyonecrossing beforetheminimum. Forcotx−4x+2,derivative−csc²x−4<0andendlimits+infinity,2−2pi<0proveonecrossing. Preserve missing endpoints/polesandactualrequesteddegrees/radians. Source triangle451:PQ=r,PR=q,PX=h,anglesA/Bacute,cosA=h/r,cosB=h/q. Areas .5rqsin(A+B),.5rhsinA,.5qhsinB derive additionformula. Treat sourceimperativeboxedworkedsteps andteachingfigures explicitly;do not invent an examproof requirement.

C9 source resolutions (225registeredcautions,not225numericwrongkeys):
- Example33chosenline m.3,c.2 givesb10^.3→2.00to3sf,notprinted1.20;itsk1.58isconsistentwithchosenline. Rawdatafitgivesk1.5016,b1.9988separately;do not mandateoneexactgraphfit.
- Try33Q2 originalN=pq^t givespabout3.1,qabout2.0;printedp.0123contradictsownpositivegraphintercept. Printedq1.94aloneisplausiblegraphestimate. Growthmodelendsatchemicalterminationt10minutes.
- Try33Q1 nativeORIGINAL exponent−x CLEARS sign/baselead; decreasinglnyscatterwitha2.12isconsistent. Try32Q2 text anddiagramBOTH2.2;thumbnail2.4leadCLEARED.
- Exercise9Q1(a)keylogbshouldloga. Q4(c) native sourceANDkeyboth−14,NOT−1/4;fractional-exponentleadCLEAREDbeforedefectregistration.
- Exercise9Q6(a)log_3(x^4)isnotinjectiveonfullnonzerorealdomain;positiveinversekeyconditionalonoriginalx>0. Q6(c)native5^(x/3),not5^((x−1)/3). Q5(b)native−5x.
- Exercise9Q8 caption1.8wrong;actualuniquegraphroot.6259832407. Itsdrawnintersectionnear.63iscorrect;keyextendsbeyondrequested0..1. Do notinventofficialgraphreadingtolerance.
- Exercise9Q11transformedaxesabsent;keyp2.82,q3,x.452conditionalonbase10log-loginterpretation. Q12rejectextraneous−2kbecausek>0andoriginallogdomain0<x<2k;only3k/2. Q14(b)(i)keydraws inverse2^(−x)instead ofrequiredx-axisreflectionlog_2x;its(b)(ii)/(c)formulasarecorrect.
- Summary446log-increasingheadera>0wrong;requirea>1. Summary447repeatsalreadyregisteredexpheadererror;extendexistingrecord,notnewconceptualcount. Reciprocallnsubscriptnotationrepeats446. Allshownvalidcurvesremaincorrect.
- Revision9sourceQ6/Q7aremisnumbered6(a)/6(b)inanswer642;values15anda1.3/K8.4correct. StableactualsourceIDs/tariffsretained. Revision2exactstrictcutoffln(.5)/ln(.8)storedseparatelyfromrounded3.11display.

BothsourcePDFs,all19protectedreviewhashes,HEAD11cd03fe639f9936dd9f83fd04bd6f04d5181676andR4historyhashwereverifiedunchangedat447;scopedgitdiff--checkpassed. No ownerblocker,commit/push,review/sourceedits. Usercheckpointfrequencyroughly100pagesisbeingexceededwithmuchsmallerverifiedbatches. T5/T6andwhole-bookrole/exam-style/proseauditsstillopen. Frozenanalysis-snapshotstaysR4untilT6. BothbookscompleteANDindependentlyacceptedbeforestep3.

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
