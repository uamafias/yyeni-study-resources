# Handover — NSSCAS Mathematics 8227, repair round 5

Role: AUTHOR (Codex). Owner: Vitalis. Workspace: `work/nam-8227-nsscas-2026/`.
Commission: `workbench/review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.
Work is active. No owner-only decision blocks progress.

## Current checkpoint

Focused5302 PASSED through YM PDF435. No incomplete wired draft through435.

- **741/891pages** author-censused;**150remain**. Goldie318/318;YM423/573.
- **4,701responses /1,792responseitems**:3,907matches;303sketch;309show/prove;85keywrong;44nokey;53keyincomplete.
- **3,399source records /3,022individualmappingreviews**;215source defect/caution entries.
- C8complete376–406:31pages/101responseitems/308responses/64teachingpanels/11textbookexamstyleitems/Revision8=30marks.
- Full15814through419PASSED2×190commands/134identicaloutputs/29negatives;archiveanalysis/history/rebuild-verification-r5-YM419.json. EarlierC8/C7proofs retained.
- AllC9sourcebuildersthrough435WIREDandfocused-checked. Lasttranslationbatch432–435:6items/27responses/13panels(2given/11teaching). Correctoriginalrestrictedrangef=e^(x+1),x≥0hasrange[e,∞);sourcekeyy>0wrong. Sourcegraph(d)hascorrectDISTINCTapproximate2.7and3intercepts;falsegraphleadCLEARED. SourceQ2inversecurvef^−1labelshouldh^−1,formulaandgeometrycorrect.
- Next195-commandfull double rebuild through435is launching;do NOTeditwired/globbedinputsoranalysisrootJSON/MDduringit. NewrendersandUNWIRED.pydraftssafe.

## Exact continuation

Nextunfinishedcensus436. Source436–439RENDEREDANDREAD;no later source read. Source440–443andkeys641–644rendercommand63270isrunning/needsresultpoll;they are NOT YET READ. No draftafter435yet. Nextsourcebuildercanhandle436–438(examples30–32,Try30/31/Try32Q1–2),then439–440graphfit/example33/Try33. SourceC9-436-sourcecontact. Originalkeys640forTry30–32read,includingexactaxislabels.

PENDINGnativechecks,notyetregistered:YM-C9-Ex33-base-key-native(page439)andYM-C9-Try32Q2-point-native(page438)werebeingrenderedby63270. Example33sourceappears10^0.3=1.20;actual1.995→2.00to3sf. Confirmnativebeforeclaimingpublishererror. Datax0..5,y1.5,2.9,6.2,12,25,46isapproximately1.5×2^x. Sourceusesroundedlogtable0.2,0.5,0.8,1.1,1.4,1.7andchosenlinem0.3,c0.2;keepgraph-estimate/toleranceandindependentfitdistinctfromexactarithmetic. Itsksource1.58isconsistentwithchosenline,notnecessarilybadbecausefitisestimated. Try32Q2textpoints(2.2,4.908),(5.9,11.008);diagramfirstpointmightread2.4—needsnative. TextgivesA≈3.6,B≈5.2to2sf;do notsilentlymixdiagramcoordinates.

436Example30linearforms:e^y=a b^x givesYy,Xx,m lnb,c lna(a,bpositive). x^a y^b8 givesYlogy,Xlogx,m−a/b,c log8/b,requiringpositiveargumentsandb≠0. Genericdegeneratecoefficientsmustremainvisible.437Try30forms:a y=a x^b(power),b x a^y=b(m−1/loga,c logb/loga,a≠1),c y=a e^(−bx),d y=e^(ax+b).437Example31givenlny-vs-xpoints(0,1.3),(1.6,0.9),modely=A b^(−x):m−0.25=−lnb,b1.28,A3.67to2dp. Try31y=A e^(px),points(5,3.17),(10,4.77):p0.32,A4.81to2dp.438Example32lny-vs-lnxpoints(1.28,3.69),(2.11,4.81),modelKx^p:p1.35,K7.12to2dp. Try32Q1points(0,2.3),(4,1.7):powerexponentn−0.15,A9.97. Try32Q2modelA B^(lnx):gradientislnB,NOTB;givenln-coordinatesusetextuntildiagramreadingresolved.

Source432–435rangeerrorandlabeltypo215registeredwithnatives. Exactmathreflectioncalculationsderivefromoriginalgfunctions/coordinates;actualinverseCASsolvesoriginalequationratherthancomparingliteralanswertothekey. SourceTry29Q3inverseinputx≥e,evenwhenthekeyonlyprintslnx−1. Itscompositiong(−4)=7admissible;0.946matchesln7−1. C9earlierconventions/falseleadsretainedinhistoryr5-YM431and424. Bothgraphinvestigationsa–ecompletewithsoftwareprocedureboundaryLIMIT06andreciprocallnnotationnormalization;actualgraphsareprescribed.

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
