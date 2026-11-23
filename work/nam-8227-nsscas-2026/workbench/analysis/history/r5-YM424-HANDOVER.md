# Handover — NSSCAS Mathematics 8227, repair round 5

Role: AUTHOR (Codex). Owner: Vitalis. Workspace: `work/nam-8227-nsscas-2026/`.
Commission: `workbench/review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.
Work is active. No owner-only decision blocks progress.

## Current checkpoint

Focused24600 PASSED through YM PDF424. No active process/full rebuild.

- **730/891pages** author-censused;**161remain**. Goldie318/318;YM412/573.
- **4,618responses /1,776responseitems**:3,852matches;277sketch;308show/prove;84keywrong;44nokey;53keyincomplete.
- **3,366source records /2,973individualmappingreviews**;211source defect/caution entries.
- C8complete376–406:31pages/101responseitems/308responses/64teachingpanels/11textbookexamstyleitems/Revision8=30marks.
- Full15814through419PASSED2×190commands/134identicaloutputs/29negatives;archiveanalysis/history/rebuild-verification-r5-YM419.json. EarlierC8/C7proofs retained.
- All C9scripts through424 are WIRED and focused-checked:opening407–411,log-laws412–414,log-equations415–416,exponential-opening417–419,natural-opening420–423,natural-equations424. Nothing through424 remains an unwired draft.

## Exact continuation

Nextunfinishedcensus425. Source425–431RENDERED AND READ;nosourceafter431read. No draft beyond424yet. Next graph builder should cover425–431,including both existing investigations:8227:TB:YM:C9:Investigation-exponential:1starts425,continues426;Investigation-logarithmic:1starts428,continues429. They EXIST:correct them,do not create duplicateinvestigationIDs. SourcecontactsC9-424-source(424–427),C9-428-source(428–431). Exactkeys639(forTry26–28)readviaC9-key-637contact. Source431Try28Q1ends;possibleQ2on432notyetread.

Graph next tasks:425–426expinvestigationall a–e mathematical outputs:2^x,(6/5)^x,10^x,e^x and negative-exponent counterparts,base-comparison BOTH sides ofx0,common(0,1),asymptote0,quadrantsI/II,nox-intercept. Softwaremenu/newscreenstepsprocedurecontext. Source427summaryleftheader saysa>0increasing;correcta>1(nativeYM-C9-exp-increasing-header-nativeREAD). Register sourcecaution after drafting. WorkedExample26shared e^x and5−x asks uniqueintersection;monotonic e^x+x−5provesone. Source428Try26Q1hasEXPLICIT−2≤x≤2forgraphs(1/2)^xand1−x;equationhas2roots−1,0(strictconvexityconfirmsglobally). Try26Q2sketch e^x/e^(−x),reflectiny-axis.

Loginvestigation428–429all a–e outputs:base2,10,6/5,eandreciprocals1/2,1/10,5/6,1/e;common(1,0),domainx>0,quadrantsI/IV,verticalasymptotex0,noy-intercept,behaviour0<x≤1,baseeffectoppositeon0<x<1versusx>1. SOURCEsoftwareexplicitlyrequireslogx/logbase(changeofbase);retainasinstructionalprocedureoutsideLIMIT06,notassessedmathematicalrequirement. Graph demands remainprescribed. NativeYM-C9-log-investigation-software-nativeREAD. Sourceusesnonstandardln_subscript1/e;normalizeastheintendedlog_(1/e)x=−lnx,naturalnotationlnstaysbasee. NativeYM-C9-reciprocal-ln-notation-nativeREAD. Do not silently call it ordinarylnx.

430Example27basefrompoint(2,1/4)gives16.431Try27Q1bases2,3,1/2,1/5fromgivenpoints;Q2log3x/−log3xsketch,domain/rangeandx-axisreflection.431Example28inverseexp→ln,sharedsketchandliney=xsymmetry;Try28Q1samefor2^xandlog2x. SourceplotsareTEACHING/responseassets,notgivenquestiondiagrams. Preserveeveryaskedsketchandsymmetry/domainresponse. Do notinventgraph scope from finiteviewports.

Naturalopeningrootformatnormalizationresolved:Try23Q2asks kln3. The independentpositiveu-roots1/3,27normalizeas kset−1,3withfullsource/authoranswerformx−ln3or3ln3. GenericFiniteSetcomparisonfailsln27versus3ln3becauseitdoesnotnormaliseindividualmembers;sourcehasNOerror. Nocheckweakened/globalverifieredit;onlyexplicitrequired-formnormalizationinthatfixeditem. SourceExample25on424hasrationaly5/(x²−1)butORIGINALlnconditionsrequirex>1. Try25Q1z(y+2)/y²retainsy>0. Theseareexplicitdomains,notnewnumeric-keydefects.

C9cautionspreserved:Try6Q2csquaredproductfull-domainanswerusesabsolute-logfactors;printedbranchrequiresa>4,registeredasincompleteconvention. Try6Q2dnegative-xextensiondistinguishedfrompositive-variableconvention. NativeTry8akeydenominator10(not100)CLEARED. Example11rejectedpair−2,−6leftargument4(not−8),stillinvalidfromOTHERlogargument−2;validpair4,−12unchanged. Source412a>1proseoverrestrictive/tablea>0correct. Noe/ln-definitioncoveragefromearlyarbitrarybaselogs.InternalCASlogratiosnotlearnerchangeofbase.

BothPDFhashes,19reviewhashes,HEAD11cd03fe639f9936dd9f83fd04bd6f04d5181676andR4historyhashverifiedunchangedat406. Nocommit/push/source/reviewedits. Integrationchecks189proper/125primitive/37trapeziumunchanged. Whole-bookrole/exam-style/proseaudits,T5families/138-demandsynthesis,T6fresh-copy/finalsnapshotremainopen. BothbookscompleteANDacceptedbeforestep3. Noownerblocker.

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
