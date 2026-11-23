# Handover — NSSCAS Mathematics 8227, repair round 5

Role: AUTHOR (Codex). Owner: Vitalis. Workspace: `work/nam-8227-nsscas-2026/`.
Commission: `workbench/review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.
Work is active. No owner-only decision blocks it.

## Verified checkpoint — Chapter 12 through YM557, 2026-11-20

- **863/891 textbook pages enumerated;28 pending.** Goldie318/318;YM545/573.
- **5,453 responses /2,134 response items** checked:4,511matches,321sketch,408show/prove,107keywrong,45nokey,61keyincomplete.
- **3,858 source records /3,814 individual mapping reviews.** **258 source defect/caution entries**,not258wrongnumeric keys.
- C12 author population: **29pages,86 response items,192 responses,128 teaching/given panels**;214 total source records. Both chapter author flags true;`whole_chapter_complete:false` remains correct pending synthesis/independent acceptance. Revision12 totals **30marks**.
- Focused36747 passed:answer verifier,inventory,census,progress,R4,R5working. Independent integration/trig checks had passed before stable-ID/date/metadata repairs;full rebuild below refreshes their locators and all outputs.
- Latest full proof through551: **2×235commands,134byte-identical outputs,31seeded errors rejected**. Archived `analysis/history/rebuild-verification-r5-YM551.json`. Full541/C11 proofs also archived.
- **Next action:**launch full239-command double rebuild throughC12,31fixtures. While active,do not mutate wiredscripts,globbed `tools/textbook-r5/*.json`,analysisroot JSON/MD,assets or curriculum. New renders and unwired Python drafts are safe. Archive successful proof as `analysis/history/rebuild-verification-r5-YM-C12-complete.json`.

## Exact continuation: C13

All C12 scripts529–557 are wired. No C13 JSON exists or is wired yet.

Two C13 drafts have passed read-only mathematics and stable-ID preflight:

1. `tools/textbook-r5/author_YM_C13_opening.py` — canonical filename but **UNWIRED**. Covers558–560:four response items/ten responses/five panels. Its `save()` has not run. IDs exist in inventory. Source558 is title/prose;559 generic sign-change graph;560 Example1 and Try1Q1–3.
2. `tools/textbook-r5/author_YM_C13_graph_choices_UNWIRED.py` — covers561:five response items/ten responses/four panels. Read-only test77302 passed all five stable IDs and supporting assertions. `save()` not run. Imports canonical C13opening above. Rename to `author_YM_C13_graph_choices.py` when integrating.

**After the full C12 run finishes:**register the three confirmed C13 source defects below;save both drafts,wire before answer verifier,and run sequential focused checks. This first C13 batch addsfour pages558–561. Next C13 figure ID10. Then continue562–585;no stop rule.

Read boundary:

- Source through **563 READ**. `YM-C12-556-source.png` includes558–559;`YM-C13-560-source.png` includes560–563.
- Keys649–652 READ in`YM-C11-key-649.png`;keys653–656 READ in`YM-C13-key-653.png`.
- No source after563 or keys after656 read. Render/read before using.
- C13 `ev()`already maps these actual files;future source blocks560+everyfourpages use`YM-C13-{block}-source`. Do not invent key-page aliases.

C13 source defects **confirmed at native scale4 and NOT registered yet**:

- **560 Example1(a):**`YM-C13-Example1-label-native.png`. Workedplotstraightlinecaptionwronglyprints`y=11−2x³`;explicitstem,tableanddrawnlineare`11−2x`. Draft labels response `a-sketch-one-root` **key wrong**,while retainingcorrectone-rootconclusion and correctgeometry. Register against`8227:TB:YM:C13:Example:1`,subpart`a-sketch-one-root`.
- **561 Try2Q1(a),key653:**`YM-C13-Try2-keys-native.png`. Sourceasks`e^(2x)+x−2=0`;keylabels exponential`e^x`. Correctchosenpair`e^(2x)`and`2−x`;rootcount1right. Draft response`a-chosen-pair` **key wrong**. Item`8227:TB:YM:C13:Try-Now-2:1`.
- **561 Try2Q4(b),key653:**same native key. Printed`f(2.8)=0.0625`wrong for`2^x−x−4`;correct`2^(14/5)−34/5≈0.164404506`. Stillpositive;lower`f(2.7)≈−.2019808`androotbracketremainright. Draft response`b-larger-root` **key wrong**. Item`8227:TB:YM:C13:Try-Now-2:4`.

C13 draft methods:graph/count and sign-bracket outputs are distinct. Originaldomain matters for√(1+x),ln(x+1),and1/x. One sign bracket proves existence under continuity,notglobaluniqueness. Source-prescribedgraphpair inTry1 versus learner-chosen pair inTry2 is a real decision difference. Try2Q3 sine/reciprocal rootcount is only on **0<x<π/2,radians**,notallpositiveperiods. Root-count completeness uses independent author monotonicity/convexity/polynomial arguments;those are not automatically mandatory learner methods. Reversedsourceendpoints−4,−5 are preserved in`source_endpoint_order`while`original_bracket`isnormalised−5,−4.

## Next un-authored source562–563

Both pages READ. This is unnumbered iterative-process teaching,returning to Example1`x³+2x−11=0`:

- Given rearrangement`x=cuberoot(11−2x)`and start`x1=1.5`.
- Table states`x2=2,x3≈1.91293,x4≈1.92866,x5≈1.92584,x6≈1.92634`;lasttwo both1.926to4sf. Finalroot1.926.
- 562 hasrearrangement/procedurepanel,firsttwo-state table and first-stepgraph;563continuedtable,cobwebgraph,enlargedspiral,andnotationpanel.
- Treat unprompted worked teaching as such;do not invent separately assessed outputs for every intermediate. Verify all source table states as supporting calculations and the final root independently. Real cube root,not principal complex power.
- Two consecutive rounded states matching do not universally certify root accuracy;check original equation/bracket. Formal derivative convergence condition excluded by`8227:LIMIT08`,while understanding failure remains required. Reuse GoldieC6 fixed-source iteration/root tools and `verify_textbook_numerical_roots_r5.py`.

Demand IDs read from syllabus/registry:ROOTG=`M2:T6:O01:D01`;BRACKET=`O01:D02`;sequence convergence=`O02:D01`,failure=`O02:D02`;relate original=`O03:D01`,derive supplied rearrangement=`O03:D02`;execute=`O04:D01`,stopping/precision=`O04:D02`. Prefix each`8227:2020:`. Syllabus full objective text read from current registry;formal convergence condition is not included.

## C12 findings and implementation resolutions

- Example8(b),535 crossespole3/2in4/(3−2x)over[1,3];left+infinity,right−infinity. Printed−ln9invalidordinaryintegral. Registered,heldasvalidexemplar.
- Ordinary-logpositivebranches534–535 are correct restricted forms;fullrealprimitivesuse ln|u|on separate components. Registered convention caution.
- Native550 curvaturetable callsupwardbendconcave/downwardbendconvex. Actual chord-over/under reasoning correct. Use explicit bend/chord descriptions. Source549 general refinement claim limited;notuniversalmonotonic error theorem.
- Native550 Try21Q2(c)wronglyreferences(a),butintegralintervalisin(b). Native549 Example21/551Example22workinglabels(c)belongtostem(b). All registered; numeric answers correct.
- Native552 Exercise12Q4(c)graphlabel repeats part(b)integral instead of explicitstem`log10(x+2)`. Correctstem,bounds0..6,andestimate3.9remain;registered`TB-YM-C12-EXERCISE4C-GRAPH-LABEL`,stableitem`Exercise-12:4`.
- **Cleared false leads:**Try21Q1graphdoesnotinterceptaxisatx1;nativeverticalshadebound1haspositiveordinate,rootlater. Revision12Q5stemANDdiagramnativebothhave x/3,notx/2. No false defects registered.
- Example23 original6/(tan+cot)undefinedatbothendpoints butremovable;separatehalfintegrals converge3/2each,total3. This is not principal-value cancellation. Exact rational-trig rewrites used by CAS are independently asserted and preserve original integrands.
- Asked sketch versus GIVEN graph,exact area versus required numerical estimate,stationaryabscissa versus FULLcoordinates,complementaryareaerror reversal,and actual source precision are retained.
- Initial new Exercise12 IDs incorrectly used`Exercise`;fixed to EXISTING **Exercise-12** on all11items,parents and defectreference. Preflightconfirmed everycorrectiontargets anexistingID;no competing recordscreated.
- Common C12 helpernowsets actualNov20part/figurereviewdates,derives improper-integralqualifier evidence fromactualparts,and avoids inheriting opening-only exponential/precision statementsinto later trig/area records. ActualQUAL05decisionsaddedfor mixedrational-power terms;askedsketch/biascaseshaveQUAL11;rotationx-axisQUAL06.
- `apply_textbook_r5.py`nowpreserves`source_part_repeats`so repeatedsubparts survive in detailed inventory. Not a runtime/app-contract change.

## Remaining work and hard boundaries

T1–T4 still need C13;T5 cross-book families and138-demand insights,T6 fresh-copy/final freeze,andwhole-book metadata/roles/exam-style/prose/qualifier audits remain open. Neither textbook independently accepted. Frozenanalysis-snapshot remainsR4untilT6. Both books must be completeANDaccepted before step3. No author review sample;Claude draws its own.

After saving sourceinputs:answer verifier first;relevantindependentnumericchecks;sourceaddenda;inventory;census;progress;R4;R5working—sequentially. Do notruninventorybeforeanswerverifierfinishes. Fullrebuild runs twiceand31seeded errors;do not mutate its hashedinputs while active. User requested checkpoints atmostroughly100pagesapart;save more often atverifiedbatches. Archive proof and updateSTATUS/HANDOVER/report.

**No commit/push;Vitalis commits.** No PLAN,recipecontract,recipes,runtimegenerators,workorders,importsorlearnerassignment. No review/sourcePDF/standard/other-subject/app/pinned edits. Preserve unrelatedwork. No acquisitions/scrapers or delegatedagents.

At557,both textbooks,all19protectedreview files,R4history andHEAD reverifiedunchanged. HEAD`11cd03fe639f9936dd9f83fd04bd6f04d5181676`. Scopedgitdiff--checkpassed. Part1remains821awardrows(818official/3derived),42Eflags,95rules,31confirmedCambridgepairsacross29NSSCASquestions;independentacceptancepending. Working synthesis:`analysis/textbook-insight-working-notes-r5.md`.


### Live after C12 checkpoint

Full239-command double rebuildthroughC12ACTIVE session4663. No modifications to wired/globbedJSON/analysisroot while active. Archive proof after pass as analysis/history/rebuild-verification-r5-YM-C12-complete.json.

C13opening.py remainsUNWIRED/NOJSON. It now accepts new_item=True through existingC7sourceauthorhelper to support genuinelyrecoveredworkedteaching;alloldstableIDs unchanged. NewC13graph_choices_UNWIRED.py standalone tests77302passed5items/10responses/4panels,allstableIDs. Itoverridesopening-onlyprecisionmetadatabecauseTry2Q3usesradians. C13firsttwo drafts together558–561=9items/20responses/9panels.

NewC13iteration_intro_UNWIRED.py covers562–563,recoveredunpromptedWorked-illustration1,newmetadata,7checkedsourceoutputs(6states+finalroot)and8panels;read-onlymathcheckjustlaunched,inspecttoolsessionresult. Itusesreal_root(11−2x,3),start1.5,fullinternalstatesandliteral5-decimalprefixesforx3..x6;sourcex4prefix1.92866andx6prefix1.92634areNOTnearest5dprounding. Independentoriginalroot/bisectionandrounding-cellsignchecksvalidate1.926to4sf. DirectassessedlinksEMPTY,teachessequence/rearrangement/iteration/accuracy;noinflatedassignedquestioncoverage. Not saved/wired. NextC13figureID18afterthesesources.

T3audit finding to repairAFTERactivefullrun(orafterT1):existingGoldieC6builders wrongly use LIMIT07 for formaliterationconvergencecondition. Current actual syllabus-exclusions register usesLIMIT08;LIMIT07 is generalintegrationbysubstitution. author_Goldie_C6_opening.py andauthor_Goldie_C6_iteration_intro.pybothobservedwiththismis-ID;searchallGoldieC6scriptsandcorrectactualqualifierreferences/reasons. Preserve source answers;notanewsourcePDFdefect. Do not edit whilefullactive.

Lastsource/keysreadboundariesunchanged:source563/keys656. Noafterread. NoC13JSONornewdefectentriesyet;register3confirmedC13sourceerrorsbeforefirstC13save/check. Workactive,noownerblocker,no step3/commit/push.


### Latest read boundary and next iteration cases

C13iteration-introread-onlymathcheck28468PASSED:onefreshworkedteachingitem,7sourceoutputs,8panels,2pages. Source564–567NOWREADinYM-C13-564-source.png;keys653–656alreadyREAD. Noafter567sourceorafter656keysread. NoC13JSONsaved/wiredyet. FullC12session4663stillactive;protecthashedinputs.

Next564–565,notdraftedyet:
- Example3:originalx³−2x²+5x−3,bracket.7..8values−.137,+.232;givenformx=(a x²+3)/(x²+b),a2,b5. cfinal2dp.74,eachiterate4dp. No stipulatedstart;sourceworkingselects.75andexplicitlysaysanypoint.7..8acceptable. States.75→.7416→.7387(display),then.74final. Do not requirethatparticularstartintracemarking.
- Try3:curve6/x²versuslinex+1,bracket1.4..1.6values+.661224.../−.25625. Providedpositive-rootform√[6/(x+1)]requirespositivePfrombracket;initial1.5ISgiven. Key653states1.5→1.5492→1.5342→1.5387→1.5373,final1.54(2dp),each4dp. Independentlycheckoriginalrationaldifference,nopoleinbracket.
- Example4:F=2x/3+4/x²,start2given;a2dp2.29,each4dp. States2→2.3333→2.2902→2.2894. bfixedpointx³12,exactrealcuberoot12,x≠0. Nooriginalpolynomialgiveninitially;derivefrommapaspart(b),donotlabelitasverbatimgiven.

566–567notdrafted:
- Try4Q1:F=(1/2)realcuberoot(x²+6),start1;final3dp.952,each5dp. Key6531→.95647→.95257→.95222→.95220. Askedreverse-equationax³+bx²+c=0:8x³−x²−6. Nonzeroscalarmultiplesvalid.
- Try4Q2:F=2+4/(x²+2x+4),start2;final3dp2.289,each5dp. States2→2.33333→2.28346→2.29025→2.28932→2.28944. bderivefixedpointx³12andexactcuberoot12. Denominator(x+1)²+3never0. SamefixedpointasExample4,differentmap/convergencepattern.
- Try4Q3:GIVENquarticx⁴+2x−9withpositiveP;abracket1.5..1.6values−.9375,+.7536;bprovidedF=realcuberoot(9/x−2),nonzeroxandspecificpositivebranch;cfinal2dp1.56,each4dp,startNOTstipulated,keyselects1.55. Key6541.55→1.5614→1.5556. Trackonerepresentativetrace,notmandatoryuniquestart.
- Example5:aASKEDsuitablepair3e^xand8−2x(globaloneintersection);bbracket.7..8values−.559,+.277(3sfdisplays);cderiveF=ln[(8−2x)/3],realx<4;dfinal3dp.768,each5dp,startNOTstipulated,working.75→.77319→.76603→.76825→.76756. SourceTABLEHEADERappears2dpwhilequestion/final3dp;nativeYM-C13-Example5-precision-nativejustrendering,NOTREADyet. Verifybeforeclaimingdefect. Lasttwostatesmatch3dp,notasstated2dpheader.

Helperreuse:author_Goldie_C6_iteration_intro.iterate;sourceiterationkind`suppled-source-iteration`(actualspellinginexistingcodeis`supplied-source-iteration`),real_rootworkswithmpmathandwasread-onlytestedforintroall6states. Keepfullinternalstates,roundonlydisplays,independentlysolveoriginalequationwithbracketed-source-root. Sourceellipsisprefixesdifferfromrounded5dpinintro;explicititeration-exercisedisplaysmustROUNDwhenasked4/5dp. Graphicalcobwebsourcepanelsareteachingunlessexplicitlyaskedsketches.


### Latest draft and native-check checkpoint

FullC12session4663stillACTIVE. Canonical-butUNWIRED author_YM_C13_iteration_examples.py covers564–565;read-onlytest33482PASSEDall3stableIDsandmathassertions. Itprovidesreusableauthoring-onlysequence_partshelper(basedonexistingGoldieiterate),recordsinitialvaluepolicy,givenversusderivedverificationequation,andverification-bracketorigin. Example3final.74notseparatelyprinted:authorrootresponseusesNO KEYstatuswithsource-tablecorroboration,notafakeprintedanswer. Workedstatesareexplicitlyaskedandcheckedseparately;givenstartismetadata,notanotherassessedoutput. Sourceparts3items18responses7panels,2pages. NextfigureID25.

Newauthor_YM_C13_iteration_branches_UNWIRED.pycovers566–567:Try4Q1–3andExample5. Read-onlystable-ID/mathcheckjustlaunched,inspectsessionresult. Source4items;actualcountprintedonsave. FigureIDs25–31(sevenpanels),next32. NoJSONsaved/wired. Allsourceafter567stillunread,keysafter656unread.

NativeYM-C13-Example5-precision-native.pnghasNOWBEENREAD(scale4):workingTABLEHEADERsays2dpbutquestion/finalandparenthesisedstatesuse3dp. CONFIRMEDsourceheaderdefect;registerwithExample5(d)whenintegratingthisbatch. Numeric5dpstatesandfinal.768remaincorrect. Draftstoresanomalyonall(d)outputs;do notchangerequested3dptoheader2dp.

Afteractivefullrun:considerpreservingsource_related_item_idsinapply_textbook_r5.pyallowlist(formerpartlinksource_part_repeatsalreadyretained). NewTry4Q2linksExample4becausesamefixedpointcuberoot12throughdifferentmap;notawholequestionduplicate. Relevantrownotesalreadyretaintherelation.

C13draftfilescurrentlyNOJSON/UNWIRED:opening.py,graph_choices_UNWIRED.py,iteration_intro_UNWIRED.py,iteration_examples.py,iteration_branches_UNWIRED.py. First3confirmedsourcekeyissuesand4thExample5headerdefectunregisteredyet. Nevermutateactivefullruninputs. Noownerblocker/step3/commit/push.


### Live checkpoint refresh — 20 November 2026
C12 double rebuild is COMPLETE and archived in analysis/history/rebuild-verification-r5-YM-C12-complete.json: two runs of 239 commands, 134 identical outputs, 31 rejected negative fixtures. Earlier appended notes saying session4663 is active are superseded.

All five C13 builders through source567 are canonical, saved and wired in run_repair_checks.py. Their JSON inputs exist. Five confirmed source defects are registered (263 textbook defect/caution entries total); four GoldieC6 LIMIT07 misreferences have been corrected to LIMIT08 and regenerated. apply_textbook_r5.py preserves source_related_item_ids. No source after567 or key after656 has been read.

Sequential focused validation is ACTIVE as exec session63861. Log: checks/r5/C13-first10-checkpoint-validation.log. Order: answer verifier, independent numerical roots, source addenda, inventory, census, progress, R4, R5 textbook-working. Poll this session and inspect the log before starting another validation. Current verified figures remain863/891pages,5453responses,2134responseitems until this sequence passes; expected next census873pages must not be claimed prematurely. Once passed, update opening STATUS and save a history checkpoint with actual counts. Then continue source568–585.

STATUS.md now opens with the actual C12 verified checkpoint and clearly separates the saved-but-validating C13 batch. Historic appended entries remain. T5/T6, whole-book audits and independent acceptance remain open. No commit/push or step3.


### Verified checkpoint: YM567, 20 November 2026

Focused sequential validation session63861 PASSED all eight stages, including independent numerical roots and R4/R5 checks. Census873/891pages,18pending;Goldie318/318,YM555/573. 5525responses/2151responseitems;3890source records/3862mappingreviews;263source defect/caution entries. C13first10pages contain17responseitems/72responses/31panels. All builders through567saved/wired;fiveC13source issuesregistered. CorrectedGoldieC6LIMIT07→LIMIT08metadata andpreservedsource_related_item_ids.

Last full double rebuild remains C12:2×239commands/134identicaloutputs/31negatives. New C13 focused pass is separate. Source568–571 andkey657–660are rendering,notyetread. Continue568;sourceafter567andkeyafter656unread. T5/T6,whole-bookauditsandindependentacceptanceopen;no step3/commit/push.


### Final-page author inputs saved — 20 November 2026

All source pages through585 and answer pages through657 have been visually read;658–660read as index only. Seven new fixed-source author-analysis builders (log_power,convergence,calculus,geometry,exercise,examstyle,closing) are saved and wired. Their individual mathematical checks PASS:30responseitems/227responses/48panels/18pages. This includes two recovered supporting worked illustrations, not extra assigned questions. Revision13tariffs total30. Total267source defect/caution entries after registering Example7 missing fifth digits, golden-ratio reciprocal/header, Example11 table index/cross-reference. Native sign-test note and golden long decimal were verified CORRECT, not registered as defects.

Combined validation ACTIVE session93183, log checks/r5/C13-complete-checkpoint-validation.log. All7builderspassed;answer verification running, then independent numericalroots,sourceaddenda,inventory,census,progress,R4,R5working. Census builder now derives author census.exhaustive only when no pending page AND every inventory item is linked; this is not whole-textbook acceptance. Inspect actual counters after pass; expected891/891pages but do not claim until checks pass. Last verified checkpoint remains873/891. No active full double rebuild yet.

After combined pass, save actual current counters/history, then run full double rebuild with31seededfixtures. Do not mutate hashed inputs while full runs. T5/T6,whole-book metadata/roles/qualifier audits and independent acceptance remain open. No step3/commit/push.


### Verified final-source-page checkpoint — YM585,20 November2026

Final combined validation75306and follow-up10095PASS. 891/891source pages author-enumerated, no pending page or unlinked inventory item; Goldie318/318,YM573/573, duplicate139excluded. All3940source records individually mapped,1758figure records. 5752responses/2181responseitems:4735matches,336sketch,460show/prove,111keywrong,46nokey,64keyincomplete. One separately retained GoldieC3Activity3 is out-of-scope and has no prescribed8227response. Register268includes metadata/precision cautions, not268wrong numerical answers. C13whole author population:126records=47responseitems plus79panels;299responses;28sourcepages. Revision13totals30marks.

Proof:analysis/history/r5-YM585-page-census-complete.json;checks/r5/C13-complete-final-validation.log;checks/r5/C13-final-register-validation.log. Continuation page fields now survive assembly, and supporting illustrations retain correct prerequisite/supporting evidence-role prefix. Census.exhaustive now means only explicit author census completeness:all891pages AND every inventory ID linked. This doesnotclaimT5/T6completionorindependentacceptance.

Allsource through585andneededkeys through657READ;658–660are index only. Native checks also CLEARED false leads:Try3key correctly haspositive.661at1.4; golden long decimalcorrect; rounding-cellsigncorrect. New precision-labelcautionTry4Q3 source1.56(3dp)wronglabel:stem2dp iscorrect;actualroot1.557527...wouldbe1.558to3dp.

Next:full251-command double rebuild with31negativefixtures. No editing hashed inputs or analysisroot duringfullrun. Afterwards archiveproof andupdatehere. T5 textbook families/138-demandinsights,whole-book metadata/roles/qualifiers/exam-styleaudits,T6fresh-copy/freeze and independentacceptance remainOPEN. Step3stilldeferred. No commit/push.


Full final-page double rebuild ACTIVE session9445. Log checks/r5/C13-full-double-rebuild.log. Do not modify wired inputs or analysisroot while active. Poll to completion, archive successful checks/rebuild-verification.json as analysis/history/rebuild-verification-r5-YM-C13-complete.json, then update currentSTATUS/HANDOVER. Source-page checkpoint is saved; fullproof not yet claimed.
