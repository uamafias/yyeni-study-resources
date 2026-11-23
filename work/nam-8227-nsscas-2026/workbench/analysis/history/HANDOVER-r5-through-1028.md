# Handover — NSSCAS Mathematics 8227 repair round 5 (active)

18 November 2026. AUTHOR Codex; owner Vitalis. Commission: `review/opus-5-5-repair-r4/REPAIR-PROMPT.md`. Vitalis resumed the paused work. **Step 3 waits for both textbooks complete and independently accepted.** No parallel planning. Hand back after Part1 and T1–T6,unless an owner-only decision blocks progress. None currently does.

## Verified checkpoint: 965 outputs

The deterministic double rebuild passed:129byte-identical assembled artifacts; all18negative fixtures rejected for their expected reasons. Observed successful session54259and`checks/rebuild-verification.json`. No full runner is active. This is author structural/mathematical validation,not independent educational acceptance.

Population:2,262source records (2,004problem/worked/census-only tasks,258figures/tables). One newly retained task is explicitly outside8227(Activity3.3); it adds no assessed or teaching coverage. Census151/891pages;740pending. GoldiePDF15–37,70–96,176–197; YM153–231. YMchapter4andGoldiechapter3have full author page/response passes; finalT5cross-book/exam/grade synthesis andindependent acceptance remain open.

Answers:403responseitems/965subparts;715matches,107sketch,103show/prove,28keywrong,1nokey,11keyincomplete. Forty-four manual derivations;921executable outputs.47source-defect entries. Independent maths:96graph/viewports,20directedangles,57basic/90composite bounded equations,5inversecompositions,30R-form cases. YMsummaryadds52formula/feature checks;Goldieclosingadds34. Source counts are not family or recipe counts.

## Completed short repair

Part1A/B: eight award-row corrections,42Eflags,duplicate-self alternatives removed,derived marking statuses,seven report gaps/defects,broader rule076. Scale4source evidence inchecks/r5;history records distinguish source corrections from schema changes. `checks/repair-r5-part1-validation.json`passes.

Part1C: five requested Cambridge pairs read on both renders,changed fields corrected,004folded into003,030wording-only hidden.31confirmed pairs on29NSSCASquestions,3structural comparisons,1wording-only hypothesis.119×3208page phrase/value comparisons across202uniqueQPdocuments(214paths);all158above-threshold candidates explicitly read/disposed on136source pages. Pair036came from that screen. Below-threshold unread leads remain unread.2024P2Q7source-diagram defect independently recomputed and linked.

## Latest source analysis: Goldie chapter3

AllPDF71–96enumerated:70response/exposition records,32figures,andoneexplicitlyexcludedActivity3.3. All source/key mathematics transcribed from renders,with individual mappings,components,actual-value checks andanswer derivations. General solution formulas/Activity3.3outsideLIMIT02;principal ranges/branches andfiveformula-reference blocks retained. Page96prose-only,C4starts97.

New builders: `author_Goldie_C3_rform_exercises.py`(PDF90–91,3D4–14)and`author_Goldie_C3_closing.py`(92–96,Currents,3E,principalbranches,summary). Both wired into`run_repair_checks.py`;census/answer inputs generated.3D10given diagram continues onto91.

New defects:3D6phase67.7°should67.4°at1dp;3D10firstangle30.651026…should30.7°rather than30.6°;3D11–13give1dpwhere2dpexplicitlyrequested. Currents unrestricted-phase key wrongly guarantees larger amplitude,usesatan(Q/P)withoutquadrant/axis handling,andneedsnonzero-result/phase-representative qualifications. Source/key crops and exact counterexamples are in`textbook-defects-r5.json`. Itsphotoiscontext,notmathdata.

3E3(iii)tan4θidentityretainscosθ≠0,cos4θ≠0;do not excludeθ=π/4through an unnecessarytan2θintermediate. The symbolic simplifier initially failed a valid rational proof step; exact polynomial reduction by unit-circle identities fixes that checker limitation. This wasnotrecorded as a book defect. Precision-incomplete R-form keys are checked at both requested and printed accuracy.

The census-only excluded task has an explicit excluded evidence role,zero direct/component/teaching links,andLIMIT02basis. R4check now validates this separate role rather than forcing it to pretend to be supporting practice. All existing negative fixtures still reject.

Earlier R-form tools retain exactnorm/atan2parameters. Source rounded phases do notdrivelaterroots. Half-angle-axis regression fixture models the earlier missedπroot ofExample3.6(iv). These are source-verification helpers,notruntime problem generators.

## Continue from here

A new **unwired**source builder `tools/textbook-r5/author_Goldie_C4_opening.py`has been drafted forPDF97–101. It hasnotyetbeenrun or counted in the checkpoint above. Read/check it,generate inputs,wire it,andverify. Source contacts`Goldie-C3-boundary-94`(cover97),`Goldie-C4-98`(98–101),`Goldie-C4-102`(102–105)andanswercontact`Goldie-key-C3-341`(341–344)havebeenread. The4x`Goldie-key-4A-full`cropwasread;it doesnotcoverallanswers,so usefullcontact/nativepage for missing portions.

C4opening:Prompt1contextbrainstorm;headinglessproduct/quotientfirst-principlesderivations(optionalunderLIMIT03);Examples4.1–4.4;Activity4.1;Exercise4A1nine derivatives. Four given/reference figures. The drafted builder keeps ruleuse separate from optional proof anddoesnotattachimplicit/parametricdemands toexplicitfunctions. Examples1/3/4andExercise4A1haveexplicitmethodinstructions;Example2allows expansion as a valid alternative.

NextPDF102–104:4A2–8connectedcalculus/geometry/sketchtasks. Q5is2x/(√x−1),NOT2x/√(x−1). It continues102→103. Q6rationalstationarypoints;Q7maximum(−1,−1),minimum(0,0). Q8positivegraphx√(9−2x²),endpointa=3√2/2,maxx=3/2,originrightgradient3. Key'sunsigned“gradient=∞”is a vertical-tangent shorthand; actual leftslope tends−∞andnofiniteendpointgradientexists. Do not call it an explicit+∞claim without checking the notation/convention. PDF104alsohasPrompt2(nonzeropolynomialcannot equalitsderivative),pluslog/expteaching;105hasExamples5–6andreferenceformulas. These pages are read leads,notyetnewcensus/answerrecords.

Then continue everyremainingsection inbothbooksT1–T4,thenT5fullfamilies/per-demandinsights,andT6. The current global census remainsfalse/notexhaustive. No author-selected reviewsample. Do not freeze the snapshot until actualcompletion;currentanalysis-snapshotremainsR4,preservedhistoryhashf3b682495a66d71f6750e76df7972899eb8cb1a2a4b3f0f87cd15aaef5dccde1.

No commit/push,review-folder/sourcePDF/standard/other-subject/app/pinned edits. Preserve unrelated dirtywork. Textbook originals stayinternal. NoPLAN,recipes,runtimegenerators,workorders,imports orassignment. Seeanalysis/textbook-insight-working-notes-r5.mdfor source-backedT5leads,notdecisions.


## Active stage after the 965-output checkpoint

The C4 opening, 4A and log-introduction builders have now been run and wired. The focused answer pass reached 1,020 outputs. A full 1,028-output double rebuild is running as session **84129**, including the additional PDF106–107 examples/prompt and two reference panels. Observe its result before claiming this newer full pass. No dependent author inputs should change during it.

A locator failure caught an author staging mistake: existing **Prompt2 is on PDF106**, the ln(3x)/lnx graph prompt. It was initially overwritten by the newly found polynomial proof prompt on104. The latter now has its own new **Prompt7** record. The base Prompt2 record is restored and separately reviewed in `author_Goldie_C4_logs_examples.py`. This is an author locator error, not a source defect or evidence the old Prompt2 was a polynomial/log mis-tag.

New helper checks derive all stationary coordinates inside the original real domain and validate manual classification supporting values. During author verification, two drafted second-derivative magnitudes were corrected before passing: 4A5 at4 is1/4, and4A6 has2/(2x+3)^3. These were author draft errors, not book defects. Exact expected supporting-result assertions now guard those claims.

One new source defect is registered (48 total): Example4.9(i), PDF107, has correct final derivative4/x but rewrites ln(x^4) as4lnx without retaining the negative real branch. Its original domain isx≠0; use4ln|x|or the original composite derivative. A scale4 source crop and x=−1 counterexample support the working/domain qualification. Source-working limitations are now recorded separately from the automated final-answer comparison.

Next source reads: `Goldie-C4-106` was inspected through109; only106–107 are newly authored. Exercises4B1–11 on108–109 remain to author, with Q5 continuing108→109. `Goldie-C4-110` is rendered but NOT yet read. The scale4 crop `Goldie-4B5-origin-domain` has been read: its given graph ofx ln(x²) passes through the origin without a hole, although the original is undefined at0. Register the visual limitation only after the whole item's answer pass. Do not silently treat its continuous extension as the original. Similar care is needed for the xlnx graph starting at the limiting origin.
