# Handover — NSSCAS Mathematics 8227, repair round 5

Role: AUTHOR (Codex). Owner: Vitalis. Workspace: `work/nam-8227-nsscas-2026/`.
Commission: `workbench/review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.
Work is active. No owner-only decision blocks progress.

## Current checkpoint

2026-11-20 — YM522 verified checkpoint:828/891pages,63pending;Goldie318/318,YM510/573. 5,228responses/2,028responseitems;4,338matches,318sketch,364show/prove,103keywrong,45nokey,60keyincomplete. 3,710source records/3,562mappingreviews;247source defect/caution entries. Focused14937passes. Full8069through511PASSED2×219commands/134identicaloutputs/30negativefixtures;archivedanalysis/history/rebuild-verification-r5-YM511.json. Allthrough522wired/focusedchecked. Noactivefullrun. Exercise523–524UNWIREDdraftmath61671passes10items/17responses/3figures;noJSONyet. Source525–531READ;C11closes528,C12opens529. Keys649–652READ. No sourceafter531read. No step3/commit/push;T5/T6/whole-bookmetadataaudits/independentacceptanceopen.

## Exact continuation

Allthrough522wired/focusedchecked;full511proof219×2/134identical/30negativesarchived. Noactivefullrun. Parametricopening512–515,geometry516–519,diagrams520–522JSONgeneratedandwired;247registeredsourcecautions. Try38Q1keyonlyt2butcorrectrequestedpoint(6,5);Try39Q2wrongtangentslope1/8versuscorrect3/4,correctline3x−4y+45=0. Nativeevidencehashed.

NEXTauthor_YM_C11_exercise.py523–524UNWIRED/math61671passed10items/17responses/3GIVENfigures. Nextmain-generate,registerconfirmedExercise11Q10defect248th,wireandfocusedcheck. NativeQ10source524interval0..π,key649P−.08623OUTSIDE,retainedQ1.979mislabelledandmissingcycle-shiftedroot. CorrectorderedP1.979,Q3.055each4sf. Exactrootsrecordedinmodule;independentnumerictrigscanrequiredfornewboundedroot. Source/keynativecropsREAD. FigureIDs121–123usedbydraft;closingstarts124.

Closing525–528NOTYETDRAFTED,allREAD. 525explicit11.7ExamStyleheader,Example41+tangentthroughoriginforf(4−x)e^xgivesp2;Try41parametricX t³+6t+1,Yt⁴−2t³+4t²−12t+5,derivative(4/3)t−2,a4/3,b−2,normalx−2y+9=0hasgradient1/2thereforetangent−2,t0,P(1,5).
526Example42X2t+lnt,Yt+4/t,t>0asksYatstationarypointandnature:Y4,min. CORRECTsecondderivative4/25=80/500(sourceexemplarcorrect). Try42Q1X3−t³,Yt²−2t:stationaryt1,point(2,−1),second2/9>0MINIMUM. Nativekey649onlyt1(no pointcoordinates)andwrongMAXwithwrongsecondderivative;recordincompletecoordinatesANDwrongnatureagainstonesourceentrywithalso_affects_subparts. Try42Q2f xexp(−x/2),fsecondzeroat4,point(4,4e^−2),keycorrect.
527Revision11=30marks,Q1=3,Q2=5,Q3=5,Q4a4b5,Q5a4b4. Q2repeatsTry9Q2butNEWkey649includesbothcoords(3,−5),(7,11),CORRECT;doNOTinheritpreviousmissingordinatesdefect. Q3sameasTry13Q3(1/3,3/2),correctkey650. Q4F x²+y²−4xy+3,showdy/dx(2y−x)/(y−2x),horizontalpoints(2,1),(−2,−1). Q5duplicatesExample42,y4minimumcorrect,butNEWkey650second2/5isWRONGversus4/25;recordsourceworkingdefectwithcorrectfinalnatureexplicit. Allfour4×nativesREAD:YM-C11-Try42Q1-source-native,Try42-key-native,Revision11Q5-key-native,Ex42-second-native. No canonicalentriesyetforfutureclosing.
528summarypanels product/quotient,exp/log,basictrig,affinetrig,implicit,parametric. Needfigurecensus. Source529titleC12and530–531openingexpintegralsREADinYM-C11-528-source.png,butnoC12draft. No sourceafter531read.

Frozenanalysis-snapshotremainsR4untilT6. T5families/138-demandsynthesis,T6freshcopy/freeze,whole-bookmetadataauditsandindependentacceptanceopen. BothbookscompleteANDacceptedbeforestep3.

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






