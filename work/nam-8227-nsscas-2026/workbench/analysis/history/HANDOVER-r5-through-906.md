# Handover — NSSCAS Mathematics8227 repair round5 (in progress)

17November2026. AUTHOR Codex; owner Vitalis. Active commission:
`review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.

**Binding owner decision: step3 waits for complete textbook analysis AND independent acceptance. No parallel planning.** Read the unchanged owner decision in that review folder. This is a working checkpoint, not a completion handback.

## Latest verified checkpoint — 18 November 2026

The 906-output deterministic double rebuild completed successfully: 129 assembled artifacts byte-identical; all 18 seeded negative fixtures rejected for their intended reasons. Verified from checks/rebuild-verification.json. No runner is active. This supersedes the older active-session notes below.

Saved population: 2,250 source records (2,002 problem/worked items; 248 figures/tables), 635 fresh mappings; 144/891 census pages, 747 pending. Goldie PDF15–37,70–89,176–197; YM PDF153–231. Answers:387 items/906subparts:672matches,103sketch,99show/prove,24keywrong,1nokey,7keyincomplete;40manual/866executable.39source defects. Independent checks:92graph/viewports,20angles,57basic/75composite bounded equations,5inverse compositions,12R-form coefficient/function checks. Full textbook completion remains open.

Goldie PDF86–89 inputs ARE saved and wired: author_Goldie_C3_rform_intro.py, textbook_rform_checks_r5.py, answers/census-Goldie-C3-rform-intro.json. They cover headingless sine/cosine forms, Example3.6, Exercise3D1–3 and seven figures. Exact phase retained; source rounded phase never drives another answer. Example3.6(iv) includes both π/3 and π; exact half-angle fallback preserves the missing-at-infinity branch and has a seeded regression check. Generic zero-vector/phase-endpoint qualifications and Example3.6 wide plot are registered source defects.

**Next:** author Goldie Exercise3D4–14 (PDF90–91), Currents investigation and3E(PDF92), then principal-value/summary material93–96. Existing inventory misses Currents. General solution formulas and Activity3.3 remain outside LIMIT02, but principal-value ranges and the five formula blocks on95 are retained. Goldie C3 ends96; C4 begins97. The notes below include stale historical checkpoint statements; this section is authoritative until superseded.

## Current checkpoint

Part1 A/B corrections implemented: eight named marking-row fixes plus schema repairs;42E flags, self-alternative removal, derived marking status, seven report gaps/defects and broadened rule076. Corrected source rows have4x rendered evidence in`checks/r5/`. Preserved pre-repair audits live under`analysis/history/`; reconciliation distinguishes schema-only changes from a new source read.

Part1 C author pass complete: five new Cambridge pairs read on both renders; changed descriptions corrected;004 folds into003;030 wording-only possible source hidden. `provenance-reading-r5.json` records the actual reads. Thirty-one confirmed pairs on29questions,3structural comparisons,1wording-only hypothesis. The original2024P2Q7diagram defect is linked and independently recomputed. Full local-page phrase/value screen compared119questions×3208pages=381752comparisons across202unique QPdocuments (214paths). All158above-threshold candidates have explicit rendered dispositions on136source pages; newpair036 came from this screen. Below-threshold leads remain unread unless separately paired.

`checks/repair-r5-part1-validation.json` passes; three new marking negative fixtures reject the seeded errors for their expected reasons. The R4 structural checks also pass on the repaired records. This is author validation, not cross-vendor acceptance.

**Resumed at Vitalis's request on 18 November 2026.** No commit or push. This is an active working checkpoint, not a completion handback.

Current saved population: **2,241 source records** (2,000 problem/worked items and 241 figures/tables); 622 fresh mapping reviews. Explicit census: **140/891 pages**, 751 pending. Goldie PDF15–37,70–85,176–197; YM chapter4 PDF153–231. Goldie198–230 has boundary readings only.

Answer verification: **381 response items /890 subparts** —658 matches,103 sketch,99 show/prove,23 key wrong,1 no key,6 key incomplete. Thirty-eight logical derivations are manual;852 have executable checks. Thirty-seven source-defect entries are registered and linked. Focused answer/inventory/census/progress/R5/R4 checks pass. Independent maths checks91unique function/viewports,20directed angles,57basic and74composite bounded equations,and5inverse-composition cases. YM summary figures add52explicit formula/feature comparisons.

**Latest full pass: the 890-output deterministic double rebuild passed, with129byte-identical artifacts andall17negative fixtures rejected for their intended reasons.** The result was observed from session96064. A new906-output/18-fixture full run is active as exec session16534. This is author structural/math verification,not independent educational acceptance or whole-book completion.

New author_Goldie_C3_double.py coversPDF82–85: headingless ideal-projectile andpower-reduction expositions,Examples3.4/3.5,all13Exercise3Cquestions,andfivefigures. 3C11key misses valid90°;its source/key are read at4x. Approximate printed roots now match one-to-one,so a missing middle root is correctly incomplete,without misaligning later printed values. Common angular units are exactly rescaled before multiple-angle expansion;pure tangent preservation applies only to one argument. Constant compound expressions are fully reduced (the earlier false tan3a mismatch was a checker simplification limit,not a book defect). All74composite numeric checks pass.

Mapping refinement: unprompted explanatory derivations use separate teaching/component links,not invented assessed questions. Their teaching_exposition_count/IDs are now separate from actual teaching_figure_count/IDs; direct source-practice counts retain their meaning. This affects the new Goldie Pythagorean,sine-addition,double-angle,projectile andpower-reduction expositions. Actual instructed activities/Examples keep their assessed targets. Counts are source records,not problem-type or recipe counts.

**Next source work:** GoldiePDF86–97andthekey contactPDF341–344have now been read. C3ends at96;C4begins97. PDF94 has two general-solution plots with identifiable principal-value branches andout-of-scope Activity3.3. PDF95is an in-scope five-block key-point formula panel,despite the general-solution margin label;96is prose-only outcomes. These pages are not yet censused. C3doesNOTendat92: PDF93starts general solutions(outsideLIMIT02)butalsohas in-scope principal-value interval evidence. Scope-screening has read94–96; retain principal-branch/required formula support while excluding general solution expressions andActivity3.3underLIMIT02. No new census/input records for86onwards exist yet. The existing inventory misses the unnumbered Currents investigation onPDF92. Do not lose it.

Pending R-form analysis details:
- PDF86–87headingless4sinθ+3cosθ and3cosθ+4sinθ derivations,generic formulas,andtriangles3.9/3.10. Keep exact internal phases atan(3/4),atan(4/3);36.9°/53.1°are rounded displays. Source general positive-r/strict−180°<phase<180°convention has degenerate/axis caveats; actual explicit exercises must use their own allowed phase ranges.
- Example3.6 starts87,solution88–89:√3sinθ−cosθ=2sin(θ−π/6),max/min±2;sketch requested0..2πbutFigure3.12extends beyond2πwithlabelled13π/6zero. Both source interval andwide graph have now been verified at4x(checks/r5/textbooks/Goldie-Ex3-6-sketch-interval.png andGoldie-Ex3-6-wide-graph.png);registration waits for its answer pass. Equation=1givesθπ/3,π. Figures3.11–3.13 need census.
- Exercise3D Q1–3start89,Q4–10start90,Q11–14start91. Corridor/table Q10diagram is on91andmust be linked as continuation; its geometry boundsθtoacute tilt. Q6–9request sketches/extrema. Q8uses2θandfourboundedroots. Q9has reciprocal1/(3+cosθ+√2sinθ),so extrema swap and denominator positivity matters. Q11–13request phase to2dp,whilekey341appears to print1dp; Q6(i)appears67.7°where atan(12/5)≈67.38°. Four-times source/key checks now confirm these readings. Independent Python-math atan2givesQ6phase67.380135°(key67.7°),Q11phase53.130102°(requested2dp53.13,key53.1),Q12phase11.309932°(11.31,key11.3),Q13phase73.739795°(73.74,key73.7). They are not yet registered until the item answer pass.
- Currents investigation(PDF92)asks sum of A1sin(2πft) andA2sin(2πft+α),samef,unrestrictedphase. Key341bottomright gives P=A1+A2cosα,Q=A2sinα,R=√(P²+Q²),thenε=atan(Q/P),claims greater amplitude andphase between0andα. Need independently audit actual arbitrary-phase scope: cancellation(A1=A2,απ),axis/quadrant cases,atan2 andR=0undefinedphase. The frequency statement also needs the nonzero-result condition. Full4xkeyandoriginaltaskareavailable(Goldie-key-Currents-full.png andGoldie-Currents-original.png);both needmetadatainspectionupdatesonceviewed. Thefullkeywasviewed;theoriginalcropisrenderedbutnotyetviewed. TheolderCurrentscropcutsrightandmustnotbeusedforcompleteclaimquotes. No newR-form helper orsourceinputhasyetbeenwritten.
- All4Exercise3Equestions on92 need full individual responses. PDF93principal inverse ranges are correct; general formula/unbounded roots stay excluded. Chapterend96hasnowbeenread;94generalformula/Activity3.3outsideLIMIT02,95requiredformula summariesretained,96proseoutcomes. C4cover97hasonegivencontextgraph4.1andPrompt1(notyetcensused).

No source PDF,review folder,standard,app orpinned edits. No commit/push. No owner-only blocker. Continue bothbooksT1–T4,thenT5/T6;do not hand back partial completion. Goldie R-form data/builders are still pending;current frozen snapshot remainsR4.

## Active R-form input stage (after the890-output full pass)

New inputs/builders are saved forGoldiePDF86–89: author_Goldie_C3_rform_intro.py (6items,16outputs,7figures). It is wired inrun_repair_checks.py. New textbook_rform_checks_r5.py derives exact positive amplitude/quadrant-aware phase for the source target; the main verifier rounds only display phases. Exact candidates are retained asunrounded_canonical_parameters. The numeric verifier reads those persisted candidates and independently checks the original coefficients/function withPythonmath; it doesnot call the R-form answer routine.

The first source-answer pass produced906outputs/387items:672matches,103sketch,99show/prove,24keywrong,1nokey,7keyincomplete. Since then the extrema operation was strengthened to derive its norm from originalcoefficients rather than repeating the finalconstant.39source-defectentries are now saved,adding the genericR-form zero/phase-endpoint qualifications andExample3.6plot extent. These new records still need the active full-run result before a newpass claim.

**Full906 attempt64801 stopped in the new numeric checker:** SymPy printed tuples parse as Python tuples, so its too-strict type assertion failed. Both tuple representations are now normalised. The main906-output answer pass andindependent92graph/20angle/57basic/75composite/5inverse/12R-form checks pass. **ACTIVE FULL RUN: exec session16534**, fresh906-output/18-fixture double rebuild. Observe its result before claiming it. The18th half-angle-axis-branch-lost fixture removesπfromExample3.6(iv),which the old CASfallback missed. The original√3sinθ−cosθ=1really hasπ/3andπ. The source checker now solves a linear sine/cosine equation with an exact tangent-half-angle quadratic AND separately preserves the omitted argumentπaxis; this is authorverification machinery,not a learner-required method. Original poles remain checked. While the new fullrun is active, do not modify dependent tools or assembled analysis; read its result explicitly.

The new R-form graph/scalar inputs have not yet received a new fullpass claim. Old stable fullpass remains890outputs/129identical artifacts/17fixtures. Last full runner failure,if any,must be investigated rather than silently bypassed. Current source-input count is ahead of the previous stable assembled checkpoint. After success,updatecounts from theactualJSON files andreport/HANDOVER/STATUS.

Pending source after89:3D4–14on90–91,Currentsinvestigationand3Eon92,principal-value/limitedscope evidence on93–94,formula summary95andprose96. Allthese pages are nowread,including94–97boundary contact. Currentsoriginal/fullkey4xcrops have nowbothbeenviewed,andmetadata updated. ConfirmedR-form keyleadsQ6phase67.7andQ11–13one-DPversustwo-DPrequests remain UNREGISTERED untiltheir answer pass. Currentshas no statedαrestriction;key claims unconditionalgreateramplitude andusesatan(Q/P). Need cancellation,axis/quadrant andphase-convention analysis. Source3D10diagram is on91andcontinues thequestionstarting90. Do not lose that continuation.

Source3D9reciprocal extrema need positive denominator3−√3andmax/minposition reversal. Source3D8uses2θandfourroots. Q11strict0<x<360;Q12/13inclusiveendpoints. The next R-form helper stage can reuse theexactparam operation andfixed-source graph/roots; numerical roots must use originalcoefficients/fullprecision,not rounded printedphases. No remaining source90+R-form data has been authored yet.

T1–T4 across the remaining population,T5 cross-book families/full per-demand insights,andT6 remain open. No author-selected independent sample. Frozen snapshot remainsR4. Step3 waits for complete author work AND independent acceptance. No commit/push or source/review/app/standard changes.

## Resume safely

- R4 snapshot preserved as`analysis/history/analysis-snapshot-r4.json` (sha256f3b682495a66d71f6750e76df7972899eb8cb1a2a4b3f0f87cd15aaef5dccde1). Current snapshot is stale whileR5 is active.
- Part1 registers regenerated. The full runner now includes the original14 fixtures and2 mathematical root-regression fixtures. Repeat the final double rebuild in a fresh copy onlywhen allT1–T6author work is complete; current passing checks are working-stage validations.
- Continue textbook T1–T6 without returning a partial completion. Update this handover after each stage.
- Final: focused cross-vendor check, then step3 only after acceptance. No author-seeded review sample.

Do not commit/push or edit review folders, source PDFs,standard,other subjects,app,pinned checkouts. Preserve unrelated dirty work. No acquisition inR5; any acquisition only through existing Harvester. No PLAN,recipe contract,recipes,runtime generators,work orders,imports or assignments.

Earlier R4 checkpoint retained as`analysis/history/HANDOVER-r4.md`; its sample/next-step wording is historical, superseded by the binding owner decision above.

Textbook stage started: author-seeded R4sample retired to history; build_textbook_progress.py now refuses to regenerate it. T1census must revisit Goldie chapter8/other scope boundaries and record allteachingfigures, not merely reuse the759page readcount.

## Textbook checkpoint — Goldie chapter1

T1page enumeration is recorded for all23chapter1pages(PDF15–37),including a prose-only finalpage. Census found3missing tasks: unnumbered remainder illustration onPDF26, remainder-degree prompt onPDF27,and graph/inequality explanation prompt onPDF33. Added16mathematical figure records; their teaching links are separate from assessed links. Exercise1B Q7 now continues toPDF29.

Current inventory:1952records=1936problem/worked items+16figure records. This is a working population,not finalcount. Census envelope has891contentpages plus1duplicateYMscan; only23pages enumerated sofar. Goldie scope exclusions,especiallychapter8,remain to be reconfirmed.

All60formal questions inGoldieExercises1A/1B/1C have129explicit output/subpart checks:111matches,11sketches,4show/prove,3keywrong. Verified source defects:1B5(iii)negative intercept mislabeled-2;1B8(i)wrong sign in quadratic factor;1C7inequality half-line reversed. Four-times crops were read. One author transcription error in1B20(bxmistypedb)was corrected and disclosed separately; it is not a book defect. Allitem examples/prompts/figures and the rest ofbothbooks still need T4checks.

Inputs are under`tools/textbook-r5/`;1B/1C author input builders are explicit source annotations,not runtime generators. `verify_textbook_answers_r5.py` computes from question operands independently of the printed key. `apply_textbook_r5.py` merges only explicit re-read fields; unprocessed component mappings remain null/pending. Allstep3decisions remain deferred.

R5new negative fixtures have individually rejected allseven seeded errors. The fullrunner has been extended to14fixtures and is being checked at this working checkpoint; this does not make T1–T6complete. Snapshot remains staleR4until finalfreeze. No completion handback before allT1–T6author work is done; step3stillrequires independent acceptance.

### Later C1checkpoint (supersedes the earlier129-output count)

All83C1problem/worked/prompt items now have166output/subpart records:142matches,15sketches,5show/prove,3keywrong,1no-key explanation. Two reasoning outputs are explicitly manual logical derivations,not machine proofs. The remaining164have executable arithmetic/algebra/feature checks. All18examples and allfourboxedprompts are included,plus the previously missed unnumbered illustration. Every source figure has parent-check/feature reasoning; design status still awaits wholeT1–T6completion and independent review.

The three verified key defects remain1B5(iii),1B8(i),1C7. `textbook-insight-working-notes-r5.md`records source-backed planning observations without making a PLAN or deciding cross-book families. Next textbook priority: reconfirm Goldie scope exclusions,especiallychapter8andthe identity/equation prompt nearPDF190,then continue census/reclassification/answers across bothbooks. No author review sample exists.

The fullrunner initially exposed a legacy R2exact-key-set assertion after two new source recomputations were added. It now preserves every original reviewer comparison and explicitly names the two new computations2024P2Q7and2021P2Q12_report. A subsequent indentation error was fixed before rerun. Do not claim the double-rebuild/fresh-copy check has passed until reading its new command result.

### R5 checkpoint: Goldie scope repair and YM circular measure (2026-11-17)

Part1 remains an author pass awaiting independent review. The latest stable double rebuild passed with127byte-identical outputs and all14negative fixtures rejected. This does not certify educational acceptance or whole-book completion.

The inventory now has2027source records:1976problem/worked items and51separate mathematical figures/tables. Goldie chapter1andthe relevant chapter7population have full author subpart derivations. YM PDF153–164has explicit task/figure census andall formal response items onPDF154–163have author subpart derivations. Across these segments:149response items,271subpart checks(240matches,15sketch,9show/prove,6keywrong,1nokey);2human reasoning outputs are explicitly distinguished from executable checks. Seven R5source-defect records are linked to their items:6wrong-key outputs plus the undefinedBstem typo inYM TryNow8question1. Internal rights/display restrictions remain false for learner display.

Census:57of891envelope content pages enumerated; the other834are explicitly pending. The prior759-page render sweep is historical reading evidence,not an exhaustive population census. The two new C7retained subparts and ordinary fraction review narrow the former broad exclusion. Goldie PDF198–230has a separate rendered boundary-read register; its relevant item/figure census and answers are still pending. No whole-book completion,step3orindependent acceptance is claimed.

The explicit identity/equation prompt is Goldie PDF190(now an assessed item). The radian lead was misattributed: the tangent/degree prompt is Goldie PDF111,notYM111. YM PDF154has two geometric radian-teaching diagrams,now separately inventoried; they teach the definition without inventing an assessed definition question. Direct practice support and teaching-figure support now have distinct per-demand counts.

Resume:YM PDF165–176has just been rendered and read. Finish the basic/transformed trigonometric investigations(all subtasks andgraphs),Examples10–14andTryNow10–14; exact key pages603andlater need checking. Source leads to record after item-level confirmation:YM PDF172tan(bx)+csummary incorrectly lists y-intercept0; Ex11(c)onPDF173correctly givesc. The fixed−500..500degree investigation window cannot show a full period1080degrees,orcos(x/3)minimum at±540,for the smallest multiplier. YM Example12(c)PDF174asks y=3cosx+2,but the worked graph is y=3cos2x−1; preserve the actual asked function and register the wrong model. These leads are not yet promoted to the source-defect register because the new figure census/answer pass is pending.

Tools:author_Goldie_C7.py,author_YM_C4_opening.py,author_YM_C4_arcs.pyare in tools/textbook-r5andwired into the rebuild. verify_textbook_answers_r5now checks explicit rounding and known printed-unit mismatches; it computes from source operands and only then compares keys. apply_textbook_r5copies only book-level facts into newly discovered items,keeps precise per-subpart key pages,andlinks source-defect IDs back to items. build_textbook_progressaccepts new page-specific census evidence beyond its original bounded target; it still does not equate a read page or a locator with full answer correctness.

Remaining:T1–T4for the rest of both books,T5cross-book families/full per-demand insights,T6completion declaration andfresh-copy final checks. Owner decision remains binding:step3waits for complete textbooks AND independent acceptance. No commit/push orreview-folder/source-PDF changes.

### Latest R5checkpoint: YM throughPDF184(2026-11-17)

The current-count paragraph at the top supersedes all earlier numerical checkpoints belowit. New builders:author_YM_C4_trig_graphs.py,author_YM_C4_graph_deductions.py,author_YM_C4_exact_angles.py. Allare wired into run_repair_checks.py. Everybasic/transformed investigation row andgraph inPDF165–172has an explicit mathematical result; source blank rows are labelled author-derived withnullanswer pages. Source software menu steps were read,but the proprietary application was not executed; the task here is mathematical source analysis.

The apparent tangent-table defect atYM PDF172was CLEARED bythe4x crop:the rowactuallysaysatanbxwithout+c,sointercept0is correct. Do not propagate the older lead below. Ex23PDF187alsohasits sinoperator inpart(c); a4x stem crop cleared that small-contact-sheet concern. These are not defects.

Confirmed new graph/key issues:Example12(c)asks3cosx+2butmodels3cos2x−1;Try13Q2keyextends beyond its expresslyrestricted domain;Try15Q1keydrops the negative sign inits equation label. Unwritten coefficient-sign conventions inExample16andTry16Q1leave additional valid choices; the printed canonical choices remain valid,but the key doesnot justify rejecting equivalent alternatives. Exact-set subset checks andfunctional identity assertions record this distinction. Try18Q1(c)asksBCbutkeyanswersCD;Try20(c)labels bothθandreferenceβincorrectly. Allare intextbook-defects-r5.jsonwithsource crops/hashes.

Resume atYM PDF185–188:inverse reference-angle tasks(Example21/Try21);related-angle property reductions(Example22/Try22);given-ratio transformations(Example23/Try23Q1–3);exact special-angle evaluations(Example24/Try24a–i). The source pages andall chapter4answer pages602–615have been visuallyread; named future answers stillrequire independent derivation. Key pages:Try21/22/23andTry24a–care606;Try24d–iare607. The source187Ex23stem is valid asprintedafter the high-resolution check.

Keep learner-demand classification separate from the independent proof method:Example16is a graph-deduction task,so the double-angle identity used inauthor recomputation is not a learner-required assessed/component link. Try15Q3counts intersections; it doesnot ask for numerical root estimates. Defensible source limitations/planning suggestions are intextbook-insight-working-notes-r5.md,not a PLAN.
