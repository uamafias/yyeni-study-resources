# Handover — NSSCAS Mathematics 8227, repair round 5

**Active full rebuild:** session1161 is running the147-command double rebuild for the checkpoint through247. Do not edit wired tools,globbedJSON,analysisoutputs orworkingnotes until it finishes. Read-only inspection and unwired PY drafts are safe.

19 November 2026. AUTHOR: Codex. Owner: Vitalis. Commission: `review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.

**Work is active. Step 3 waits until both textbooks are complete and independently accepted.** This is a continuation checkpoint, not a completion handback. No owner-only blocker is known. Do not commit or push.

## Current evidence

Focused48209 passed all answer,independent vector,inventory,census,progress,R4/R5 working checks:

- 3,395 responses across1,293 response items:2,788matches,216sketches,233show/prove,69key-wrong,40no-key,49incomplete.
- 3,020 source records;2,156individual mapping reviews.
- 553/891pages enumerated;338remain,all inYM. Goldie318/318;YM235/573,covering12–247 exceptduplicate139.
- Source register170 includes teaching/diagram/wording and incomplete-key cautions,not170wrong numerical answers.

Goldie’s retained/boundary source author pass is complete: 954 records,606 response items,347 references/figures and one explicitly excluded task. YM Chapters1–4 are now author-censused. Chapter3 covers45 distinct pages107–152 (139 duplicates138),185 records:94 response items/284 responses and91 teaching/given references (70 teaching,21 given). Its response statuses are245 matches,21 sketches,4 show/prove,9 wrong,5 incomplete. Neither book has independent acceptance. Final T5/T6 remain open.

Last completed full proof78439:2×145commands,134byte-identical artifacts and28expected negative rejections,at3354responses/545pages/2998records/2120mappings. This proves C5through239 and consistently regenerates older figure-method metadata with source-neutral wording. No numeric source derivation changed in that cleanup. No process is active after78439.

Checkpoint policy (owner,19November): save durable repository checkpoints during progress,around each100pages or sooner at verified batches/pauses. Preserve counts,source issues,actual check outcomes and exact resume page. Current full proof is archived at `analysis/history/rebuild-verification-r5-YM239.json`.

## Pending locator repair after active full1161

A read-only consistency audit confirmed inline answer PRINTED pages are one too high in the C3/C5source helpers after duplicate139. Examples: C3Example19PDF140has129butshould128;C3microPDF150has139butshould138;C5Example3PDF237has226butshould225. Root cause is `author_YM_C1_opening.py` hardcoding kp−11 for every inline answer,new-item sourcepage and answer-key printed-page list. Generalise the verified YM mapping: <=138subtract11;139isduplicateprinted127;>=140subtract12;answerpages>=587useA(page−586). C3/C5existing source-question census/figure pages already use the correct mapping. Do not label this as a textbook defect.

Do NOT edit that wired helper while1161runs. After it completes,fix the shared helper,regenerate affected source builders and add a check comparing inline answer printed pages with their book/page census entry. Consider a seeded off-by-one fixture for this actual regression. The raw standalone builders currently pass numerical assertions; the locator correction must precede the next full proof. New unwired `author_YM_C5_spatial_geometry.py` covers248–251 but has NOT run or producedJSON. Its inputs will inherit the corrected helper when generated. Native roof251 caption title crop was re-rendered but not yet re-viewed; previous raw leads remain in continuation notes.

## Immediate continuation

Continue YM from248. Contact248–251 is rendered and READ;no248+builder exists yet. The232–247 C5builders opening,magnitude_units,operations,displacement_geometry are wired and passfocused48209. No full process is active after78439 at3354responses/545pages; a new full run may have launched after this checkpoint. Inspect the latest tool session before editing wired tools,globbedJSON,analysisoutputs orworkingnotes.

New source census recoveries: Example4(238)andTry8Q2(246)were absent from the older inventory and now have proper new records. The first focused244–247 attempt5922stopped at the unknown Try8Q2ID;12187then caught item-level assessed/component overlap. New-item registration and disjoint aggregate roles were corrected in the source builder. Per-part roles remain explicit; focused48209passes. Neither initial failed attempt is a pass.

C5resolutions: Try1(b)key615copies(a)’s different vertex list. Correct cubeA(2,0,0),B(4,0,0),C(4,2,0),D(2,2,0),E(2,2,2),F(4,2,2),G(4,0,2),H(2,0,2). Seven labels are missing and copiedGiswrong. Parallel-unit tasks allow either orientation,while SAME direction does not. Native239clears the false Example5coordinate8/9lead:the final2/9is correct. Native243also clears the missing2lead:the source correctly has4=2a+2b. Example6header calls scalarparametersvectors;numeric answers arecorrect. Try6Q2key616+12iswrong:parallel factor−2requiresq−12,confirmed by zero/nonzero cross products. Operations240–242are teaching references,not invented learner tasks.

Latest independent vector checks:40norm/direction,24endpoint,18unit,3perimeter,10named-point,28pair-angle and4dot checks. Formal coefficient tuples in symbolic geometry represent the source vector BASIS,not Cartesian points. Direct aggregate demands and component-only IDs are disjoint; role shifts remain in raw subpart records.

Raw248–251 leads,not yet authored:

- Ex10cuboidOF(5,4,3):OG(0,4,3),AG(−5,4,3);both OF/AGmidpoints(5/2,2,3/2),using position fromO,not half the displacement alone.
- Try10Q1triangular prism:O0,D(6,0,0),C(0,8,0),A(0,0,10),E(6,0,10),B(0,8,10).DC(−6,8,0),DE(0,0,10),DA(−6,0,10),DB(−6,8,10),EB(−6,8,0).M(3,4,0),N(3,4,10);DN=MB=(−3,4,10).
- Try10Q2:AC(12,−8,2);midAC=midOB=(1,2,2). Q3:AB(2,6,−2),BC(4,12,−4),BD(0,12,−1);BC2ABwith shared endpointBproves collinearity; recast asBC=−2BAfor common-start proof. |AB|:|AC|=1:3.
- Try10Q4roof text/keys implyO0,D(10,0,0),E(10,8,0),F(0,8,0),G(2,4,3),H(8,4,3). Slanted edgesOG(2,4,3),DH(−2,4,3),EH(−2,−4,3),FG(2,−4,3),alllengthsqrt29. Native `YM-C5-roof-height-native` CONFIRMS the given diagram draws its dotted3height fromGtoF,which is inconsistent with the centred ridge: G−F is not vertical and has lengthsqrt29,not3. Record the source diagram conflict and require a separate vertical drop to plane/projection point in future original assets. Do not change the correct text-derived values.
- Example11(250)appears MISSING from old inventory:OA(2,−5,−2),OB(4,−4,2),AB=BC givesOC=2OB−OA=(6,−3,6),norm9,unit(2/3,−1/3,2/3). Add it as a new source record,not a patch to an unknownID.
- Try11Q1:D(3,0,−4),CD=(−1,1,−7),unitOB=(1/3,−2/3,−2/3). Q2:AC=(2,4,−4),midM=(2,−1,0),unitOM=(2/sqrt5,−1/sqrt5,0).
- The two251scalar-product micro-items already have stableIDs Unnumbered-scalar-product:1/2. Both give50: sqrt200·5·cos45degrees;and(8,−6,−10)dot(4,−3,0). The source’s common-vertex arrow panels are correct for both-in/both-out orientation; its title “Vectors must point in the same direction” is ambiguous,not a requirement that vectors be parallel. Native caption crop currentlyCUTSthe title;re-crop before quoting exact wording. No251builder exists.

C3 builders now include opening,ranges,composition,inverse_opening,inverse_graphs,restricted_composites,transformations,function_exercise,geometry_opening,geometry_constraints,geometry_exercise andclosing. All are wired into `tools/run_repair_checks.py`. Geometry helper `author_YM_C3_geometry_opening.py` routes answer602–605 to the new key contact; its own use is fixed-source source analysis, not runtime generation.

All C3 sources and exact answer pages598–602 have been read on rendered contacts/native detail where needed. Four later builders136–152 add85 responses/33 response items and30 source records. The closing census found an explicit summary micro-example “Find gf(4)” on150, now a separate worked-illustration record plus its teaching diagram. Source summaries count as source occurrences, not new problem types. The revision30-mark total reconciles.

Preserve C3 corrections:

- Ex12 natural-domain sign and square-root image, Try12 reciprocal-root denominator/image, and root/inverse swapped curve labels121/149.
- Try13Q3 range depends on unset p; after selecting least p2 the simpler range becomes valid. Try13Q2 separately resets m5, so inverse input is x<=0.
- Try14Q1 composite inverse domain is x>10, not radical natural domain x>=1. Try14Q2 has only the positive inverse branch on input>=11. Q4 resets k1 and its key omits fg=2x²−7. Full-domain composition differs from a newly restricted composition.
- Exercise3.1Q4 retains only a2,b1: the other key pair violates positive b and original composite input conditions. Q1’s inverse formula is valid only for input>0, not merely input!=0.
- Ex17’s CD working calls D(12,5) by B; its coordinates and final equation are correct. Exercise3.2Q3(a) needs the vertical-perpendicular exception at a−10.
- Revision3Q2(c) correct no-solution condition is **0<=k<64/9**. At k0 the original equation16/(x−3)=0 has no solution. The key omits this degenerate branch. Source3dp distance inQ3 is explicit and overrides usual3sf.
- Summary152 point-gradient box wrongly repeats y−y1 on the right; correct is m(x−x1). Summary150 vectors use a while the rules use C; identify or correct that symbol. Summary149 repeats coordinate/duplicate-pair defects.
- Horizontal test captions149 describe their drawn test lines correctly; do not call the current affine/parabola classifications wrong. The general at-most-one/existence qualifications are reuse constraints. The finite square map has no0input and no missing zero arrow.
- Six transformations investigations128–133 are source-labelled enrichment. All mathematical subparts/graphs were checked; GUI/menu/QR steps are context, not extra assessed outputs or platform capability proof.

Next full check should run after saving any new working synthesis. During a full run, do not edit wired tools,globbedJSON,analysis outputs orworkingnotes. Read-only inspection and unwired PY drafts are safe. Final T5 families/138-demand synthesis, T6 fresh-copy/snapshot and cross-vendor acceptance remain outstanding.

## Preserve prior source resolutions

- Exercise1Q12 PDF47 uses negative exponents; key1,1/2 is correct. Example23 PDF33 annotation−(−4) correctly givesvertex(4,16). Do not revive either false-positive lead.
- Try1(b) original minus/plus/minus signs create a mixed term omitted by its key. Try4(b) usesy−12 andreciprocal exponent1/y,givingtwo admissible pairs.
- Example19’s universal rationality claim for realp is false. Try33Q3 PDF42 bounds are±2,not key±4.
- Try17Q2 PDF68: author readsS15=375witha small below-baseline scan mark,giving next15sum1050. A decimal37.5reading would instead give−7275/4. Both conditional computations/native crop are retained; the glyph is not independently settled. The key omits the requested final total under either reading.
- Try13Q7 retains both ratio signs andcorrelated term branches. Try20Q1(c) asks8terms,correct6560/729; printed8+80/81 equals the6-term total.
- Try26(f) key10ad+45d has an extraneous factor; correct10a+45d. Rounded finite81.0/0.500 displays retain exact finite totals.
- Try28(i) permitsalln≥14;Try28(j)permitsn2andalln≥4. Its key4is not even the least valid count. Example29S15last digit rounds to35,not36,while its formula is correct.
- Unit-ratio constant sequences are geometric; their nonzero infinite series diverge. Negative expansive ratios diverge by oscillation,not towardpositive infinity.
- Example32 rope is impossible as printed:62cm total with a3.5m piece. Its31pieces/d0.1m working is conditional on62m. Salary term6 means five completed raises. The savings final1993 is correct; n34 counts the initial1960 balance,not34interest years.
- Annual investment stems leave payment dates unstated; source working uses beginning-of-year payments. Keep end-of-year alternatives explicit. Recurring fraction conversion alone remains supporting practice when no8227method is required.
- Native Try37 key596 is truncated in both first expansions; its second retained126k^4m^5 also has the wrong sign. Try41(c) typeset20 is wrong; independent11·10·9=990,andthe handwriting990 is not the publisher key.
- Try46Q1 asks independence ofx although expression usesa; intended constant40095 is conditional on correcting that variable. Try46Q2’s descending-sixth term is63/(16x^6),not key−63/(8x³). Itsx^6part has no key.
- Exercise2.2Q8 key correctly saysq37andq41; the a37 suspicion was false. Preserve correlated triples(4,6,37)and(−4,4,41).
- Revision2Q4 day30loss is68,not70. Emptying occurs duringday41 after40complete days; its4-markGPpercentage part has no key and is author-derived. All printed revision tariffs reconcile to30.

Native bounce86 andstaircase88 crops were corrected/read before wiring. Their boxes are60,315,500,410 and340,500,565,630. Source originals remain internal.

## Boundaries

No PLAN,recipe contract,recipes,runtime generators,work orders,imports orlearner assignments. No edits toreview folders,PDFs/root textbook,standard,app/pinned checkouts orother subjects; preserve unrelated dirty work. Part1 author repairs remain complete:821award rows(818official+3derived),42Eflags,95markingrules,31confirmed Cambridge pairs across29NSSCASquestions,plus structural/wording leads. Independent acceptance remains pending.

All19protected review hashes andHEAD were rechecked unchanged. HEAD`11cd03fe639f9936dd9f83fd04bd6f04d5181676`. Frozen R4 history hash`f3b682495a66d71f6750e76df7972899eb8cb1a2a4b3f0f87cd15aaef5dccde1`;snapshot remains R4 untilT6. Working synthesis:`analysis/textbook-insight-working-notes-r5.md`. Prior checkpoints are archived under`analysis/history/`.
