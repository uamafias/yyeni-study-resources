# Repair round5 working report — NSSCAS Mathematics8227

Author checkpoint in progress,17November2026. **Not a completion handback.**
Step3 waits for T1–T6 completion and independent acceptance, per binding owner decision.

| Finding | Change | Evidence/check |
|---|---|---|
| R4-01 | Eight marking-row fixes; all named source readings have4x crops. | analysis/award-repairs-r5.json; checks/r5/award-*; repair-r5-part1-validation.json |
| R4-02 |42E flags, self-alternative removal, derived marking status, two row completions and seven separate report defect records. | award-audit-reconciliation-r5.json; marking-conventions.json; source-defects.json; three new negative fixtures rejected |
| R4-03 | Five requested pairs plus one further screen discovery; corrected changed fields;004 folded into003;030 possible wording source hidden; original diagram warning. | provenance-reading-r5.json; nsscas-cambridge-provenance.json; full-screen136page renders with158candidate dispositions; independent diagram recomputation |
| R4-04 / textbook completion | In progress; no exhaustive or answer-complete declaration. | T1–T6 working records to follow |
| R4-05 | Rule076 covers differentiating,integrating andcubic-solving calculators; explicit row exceptions retained. | tools/convention_inputs.py; regenerated marking-conventions.json |

Part1counts:119questions,250parts,821rows(818official+3derived),42E flags. Provenance26→31confirmedpairrecords,25→29NSSCASquestions;4→3structural comparisons plus1wording-only hypothesis and1foldedduplicate record. Screen:119×3208=381752comparisons;202uniqueQPdocuments/214paths;158above-threshold candidates read on136pages. One additional correspondence036(log trapezium/Henceintegral)was found beyond the five requested pairs.

Textbook baseline:1933items,759prior targetsource-page reads,1913answer-locatorrecords,49representative recomputations. These are not exhaustive census or every-answer checks. Author review sample retired; reviewer chooses its own blind sample. Current snapshot remains the preserved R4snapshot until allR5outputs are regenerated and frozen.

Final deterministic double rebuild,fresh-copy verification and all14negative fixtures remain to run after T1–T6. No commit,push orstep3work.

## Working textbook counts (not completion)

| Measure | Baseline | Current checkpoint |
|---|---:|---:|
| Source problem/worked items |1933|1936|
| Separately enumerated mathematical figures |not separately inventoried|16|
| R5census pages enumerated |0|23(GoldieC1only)|
| Formal source questions with full subpart checks |0inR5per-subpartregister|60|
| Explicit subpart/output checks |0|129|
| Matches / sketch / show-prove / keywrong |not populationchecked|111/11/4/3|
| Confirmed new key defects with4x evidence |0|3|

T1–T6remain open for the rest of the books. There is no author-complete declaration or independent acceptance. `textbook-defects-r5.json`and`textbook-transcription-corrections-r5.json`keep source errors separate from author errors.

### R5 checkpoint: Goldie scope repair and YM circular measure (2026-11-17)

Part1 remains an author pass awaiting independent review. The latest stable double rebuild passed with127byte-identical outputs and all14negative fixtures rejected. This does not certify educational acceptance or whole-book completion.

The inventory now has2027source records:1976problem/worked items and51separate mathematical figures/tables. Goldie chapter1andthe relevant chapter7population have full author subpart derivations. YM PDF153–164has explicit task/figure census andall formal response items onPDF154–163have author subpart derivations. Across these segments:149response items,271subpart checks(240matches,15sketch,9show/prove,6keywrong,1nokey);2human reasoning outputs are explicitly distinguished from executable checks. Seven R5source-defect records are linked to their items:6wrong-key outputs plus the undefinedBstem typo inYM TryNow8question1. Internal rights/display restrictions remain false for learner display.

Census:57of891envelope content pages enumerated; the other834are explicitly pending. The prior759-page render sweep is historical reading evidence,not an exhaustive population census. The two new C7retained subparts and ordinary fraction review narrow the former broad exclusion. Goldie PDF198–230has a separate rendered boundary-read register; its relevant item/figure census and answers are still pending. No whole-book completion,step3orindependent acceptance is claimed.

The explicit identity/equation prompt is Goldie PDF190(now an assessed item). The radian lead was misattributed: the tangent/degree prompt is Goldie PDF111,notYM111. YM PDF154has two geometric radian-teaching diagrams,now separately inventoried; they teach the definition without inventing an assessed definition question. Direct practice support and teaching-figure support now have distinct per-demand counts.

Resume:YM PDF165–176has just been rendered and read. Finish the basic/transformed trigonometric investigations(all subtasks andgraphs),Examples10–14andTryNow10–14; exact key pages603andlater need checking. Source leads to record after item-level confirmation:YM PDF172tan(bx)+csummary incorrectly lists y-intercept0; Ex11(c)onPDF173correctly givesc. The fixed−500..500degree investigation window cannot show a full period1080degrees,orcos(x/3)minimum at±540,for the smallest multiplier. YM Example12(c)PDF174asks y=3cosx+2,but the worked graph is y=3cos2x−1; preserve the actual asked function and register the wrong model. These leads are not yet promoted to the source-defect register because the new figure census/answer pass is pending.

Tools:author_Goldie_C7.py,author_YM_C4_opening.py,author_YM_C4_arcs.pyare in tools/textbook-r5andwired into the rebuild. verify_textbook_answers_r5now checks explicit rounding and known printed-unit mismatches; it computes from source operands and only then compares keys. apply_textbook_r5copies only book-level facts into newly discovered items,keeps precise per-subpart key pages,andlinks source-defect IDs back to items. build_textbook_progressaccepts new page-specific census evidence beyond its original bounded target; it still does not equate a read page or a locator with full answer correctness.

Remaining:T1–T4for the rest of both books,T5cross-book families/full per-demand insights,T6completion declaration andfresh-copy final checks. Owner decision remains binding:step3waits for complete textbooks AND independent acceptance. No commit/push orreview-folder/source-PDF changes.

## Working checkpoint — YM throughPDF184

Current counts supersede the earlier checkpoint:2,076source records(1,986problem/worked;90figures),77census pages,290fresh mapping reviews,200response items/431outputs. Results:317matches,91sketch,9show/prove,10keywrong,1nokey,3keyincomplete. Twelve manual derivations and419executable checks are distinguished. Fourteen source-defect records are linked. Independent numeric routes pass79function/viewport combinations and20directed-angle cases. The latest double rebuild passes129byte-identical outputs/all14negative fixtures. No whole-book completion orindependent acceptance.

T1–T4continue;T5/T6remain open. The earlier possible tangent-summary-table defect was cleared bythe4x crop(the printed row hasno+c). Ex23part(c)alsohas sin inits actual stem; no missing-operator defect. Both cleared readings must not become source-defect claims. SeeHANDOVERfor the exact next pages/items.


## Owner-requested pause — 17 November 2026

Paused for internet disconnection. Author input/census/answer records are saved through
YM PDF196. Current population2,126 records(1,989 response/worked;137 figures),369 fresh
mapping reviews,89/891 census pages,232 response items and543 subpart checks(425 matches,
91 sketch,13 show/prove,10 key wrong,1 no key,3 key incomplete). Twelve manual derivations
are explicitly separated from531 executable checks. Fourteen source defects remain.
Focused working-stage checks passed. The following full double rebuild was stopped at
owner request; its old successful report is not verification of this latest checkpoint.
Re-run on resume. YM197–200 source contact sheet read; enumeration/derivations pending.
T1–T6 are not complete; step3 still waits for complete textbooks and independent acceptance.


##18November2026 — resumed author checkpoint

Restored paused double rebuild passed at543outputs(129identical artifacts,14negative fixtures).
New explicit source census reachesYM208:2,144records(1,991response/worked;153figures),
421mapping reviews,101/891pages,268response items and633subparts(478matches,91sketch,
48show/prove,12keywrong,1nokey,3keyincomplete). Twelve derivations are manual.
Independent math checks53bounded root sets in addition to79graph/viewports and20angles.
19source defects linked; exact page/crop evidence distinguishes real key errors from
author sign transcriptions andthe bounded sec/cosec symbolic-library failure.
Focused checks pass; next full double-rebuild result must be observed before claiming it.
Textbook population andT5/T6remain incomplete. No step3orindependent acceptance.


## 18 November: composite equations and progression checkpoint

Working checks pass at2,158 records(1,991 problem/worked;167 figures),461 mapping
reviews,107/891 census pages,and294 response items/670 subparts. Statuses:508 matches,
91 sketch,54 show/prove,13 key wrong,1 no key,3 key incomplete. Fourteen derivations
are manual;656 executable. Twenty source defects are registered. Independent math
agrees on53 basic and26 composite bounded root sets,besides the earlier graph/angle checks.

The665-output double assembly agreed, but the new pole fixture initially failed in
its own seed construction (Python-set union), not the intended check. The runner
rejected that wrong-reason failure. The seed was fixed and its expected original-pole
rejection observed individually. The next full run must pass all16 fixtures before
this checkpoint receives a new full-suite pass. The last fully observed report is
still the633-output/14-fixture checkpoint. Textbook completion and independent review
remain outstanding; no step3.


## Principal-value checkpoint —18November2026

Full670-output double rebuild passed:129identical artifacts,all16fixtures rejected
for their intended reasons. New source readings coverYM215–218. Working population:
2,177records(1,994problem/worked;183figures),486fresh mappings,111/891census pages,
303response items and685subparts(518matches,91sketch,54show/prove,18keywrong,
1nokey,3keyincomplete);14manual derivations and671executable checks.28source defects
are linked,including printed inverse labels,branch endpoints,domain terminology,
wrong copied function inputs,anddegree/radian format conflicts. Independent math
agrees on54basic and26composite bounded root sets. Focused checks pass;685-output
full double rebuild is not yet observed. Whole-book,T5/T6 andindependent review
remain incomplete;step3doesnot start.

## Inverse-function checkpoint —18November2026

The685-output double rebuild passed129byte-identical artifacts/all16negative fixtures.
New focused checks pass703outputs across309response items:532matches,95sketch,
54show/prove,18keywrong,1nokey,3keyincomplete;16manual and687executable.
Population2180(1994problem/worked,186figures),495mapping reviews,113/891censuspages.
Independent math57basic/26composite bounded equations,20angles,82unique graph/viewports,
5inverse-composition cases. Previous86graph-query configurations combine to82unique
function/window configurations when sample queries merge;no source coverage was removed.
Twenty-eight source defects remain. New inverse work preserves exact domains/branches
anddoesnot mistake rounded table coordinates for exact inverse identities. Two key
reading leads were cleared by4xcrops. Textbook completion/T5/T6 remain pending.

## YM chapter4 source-pass checkpoint —18 November 2026

Current author census reaches PDF153–231, all79chapter pages:211response/worked items,
209given/teaching figures. The global population is2220(1994problem/worked,226figures),
559fresh mappings,124/891census pages.759subparts across333items:568matches,99sketch,
68show/prove,19keywrong,1nokey,4keyincomplete;24manual/735executable.31source defects.
The summary figures add52explicit fixed-source formula/feature checks. Numeric checks
cover88unique graph/viewports,20angles,57basic/34composite bounded equations,and5inverse
compositions. Current focusedR4/R5checks pass. The first759-output fullrunner stopped
at an old supporting-evidence role on two intentionally unlinked parameter drills;
explicit roles now propagate andthe focused gate passes. A new fullpass is required.

New mapping repairs separate geometry prerequisites, acute inverse notation,graphical
root counts,andidentity evaluation from overstated direct objectives. Empty directlinks
remain explicit for useful symbolic parameter inference with no matching graph demand.
Value-level decisions preserve n=3, n=2/3, original poles,positive length scales,andthe
missing interval inExercise4.2Q3(b). Added source defects are its missingcondition,
Q5wrongcos3θlabel,andExample57missing inverse workingstep. The final area inExample57
stillagrees at3sf; its rounded intermediate is not asserted exact. Cleared4xreading
leads remain separate. This is an author chapter checkpoint,not whole-book completion,
independent acceptance,finishedT5families/insights or permission to beginstep3.

## Goldie compound-angle checkpoint —18 November 2026

The759-outputfullrunnerpassed129byte-identicalartifacts/all16negativefixtures.
Current851-outputfocusedchecks pass:364responseitems,633matches,99sketch,
90show/prove,23keywrong,1nokey,5keyincomplete;37manual/814executable. Population2234
(1998problem/worked,236figures),600freshmappings,136/891censuspages.36sourcedefects.
Independentrootenumerationagreeson57basic/56compositecases;graphs/angles/inverses
remain88/20/5. A17thfixtureindividuallyrejectsthelossofvalid90°fromGoldie3B4(iii).

Goldie71–81addsproperreciprocaldomains,compoundrecognition/expansion,connected
coordinategeometry,andtwo-angleconstraints. Newre-readdefectsinclude3A6endpoints,
a copiedillustrativemodelcoefficient,3B3φ/θmismatch,missing3B4ninety,andtransposed
3B9orderedpairs. Scope/variablerolesandoriginalpolesremainexplicit. Knownangles
arenormalisedonlyafterexactratioproof;numericchecksareaseparateroute,notacceptance.
Thecurrentstageisnotwhole-bookcompletion,finishedT5orstep3readiness.

## Double-angle checkpoint —18 November 2026

Current focusedchecks pass890outputs across381items:658matches,103sketch,
99show/prove,23keywrong,1nokey,6keyincomplete;38manual/852executable. Sourcepopulation
2241(2000problem/worked,241figures),622freshmappings,140/891censuspages;37source defects.
Independentrootenumerationagreeson57basic/74compositecases;graph/angle/inversechecks
are91/20/5. The last fullpassremains759outputs/16fixtures;new890/17fullrunisnext.

The approximate-key comparator now identifies proper subsets one-to-one ratherthan
misaligning values after a missing middle root. Exact angular-unit rescaling precedes
multiple-angle reduction,anddifferent tangent arguments are not treated as one tangent
polynomial. An unevaluated constant tan(2atan(4/3)) caused afalsecomparison on3C13;
constantcompoundnormalisationcleared it. No source defect wasregisteredforthat toolissue.

Pure explanatoryderivations now use teaching/component links, with exposition support
separate from figure support. This prevents a displayed proof/model becoming an invented
assessed task. Bookfrequency,officialawards,whole-bookcompletionandindependentreview
remain unclaimed. Goldie86–93source/keyleads are inHANDOVER;notyet analysedoutputs.

### Observed 890-output full pass

The deterministic double rebuild passed with129byte-identical artifacts andall17negative fixtures rejected for their intended reasons. Result observed fromsession96064. This validates current author assembly/regressions; it doesnot complete the remaining textbook population or replace independent review.

### R-form introduction: author inputs and checker repair

New inputs cover Goldie86–89:6items,16outputs,7figures. The main answer register reaches906outputs, with672matches,103sketch,99show/prove,24keywrong,1nokey,7keyincomplete.39source defects are registered. A full906attempt stopped on the new numeric checker's persisted tuple type guard; parsing normalisation repaired it. The independent route now passes92graph/viewports,20angles,57basic/75composite equations,5inverse compositions and12R-form cases. No906fullpass is claimed yet.

The exact original-equation solver also gained a separately preserved half-angle axis after it missedπ inExample3.6. The18th fixture tests that actual omission. Exact internal R-form phases are retained even when the key displays rounded angles. Two new source records cover the generic phase/zero-vector qualifications and the requested-sketch interval overrun; neither tool failure was misreported as a book defect.


Checkpoint 18 November 2026: the906-output deterministic double rebuild passed (129identical artifacts,18expected negative rejections).144/891census pages;747pending.2,250source records,635fresh mappings,387responseitems/906subparts,39registeredsource defects. This working checkpoint does not complete T1–T6 or freeze the R4snapshot.


Checkpoint18November2026(965outputs):double rebuildpassed,129identicalartifacts,18expectednegativerejections.2,262source records,258figures,151/891censuspages,403responseitems/965subparts,47defects. GoldieC3nowenumeratedthrough96;Currentsand3D/3Ecompleted. Onecensus-onlyActivity3.3excludedunderLIMIT02. R4checkvalidatesitsseparateexcludedrole/zero-coverageinvariants. Finalwhole-bookT1–T6andindependentacceptancearestillopen. NextC4builderisdraftedbutnotyetcounted.


Checkpoint18November2026(1,123 outputs):double rebuild passed,129 identical artifacts,18 expected negative rejections.2,292 records,749 fresh mappings,172/891 census pages,464 response items;50 formal source defect/caution entries. New helper operations verify original real domains,stationary coordinates,total/implicit derivatives andmanual supporting claims;source-working caveats cannot mask a wrong final value. Exact trig identities are used when simplification alone fails. All19 review hashes andthe preservedR4snapshot areunchanged. Nextstage118–120isfocused/staged,notanewfullpass. T1–T6remainincomplete.


Checkpoint18November2026(1,167 outputs):double rebuild passed,129 identical artifacts,19 expected negative rejections.2,296 source records,767 fresh mappings,176/891 census pages,478 response items;51 formal source defect/caution entries. The new singular-implicit fixture models the actual folium boundary;only a separately qualified branch audit permits discussion of its origin. Source4D1–12 is fully checked. No parametric-opening census yet. A scale4 read clears Example20's suspected omittedx>4answer:the literal question asks foranyexcludedvalues,sox<0isvalid. Retain both full/restricted projections rather than manufacture a key defect. Both books andT5/T6 remain open.
