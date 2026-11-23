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
