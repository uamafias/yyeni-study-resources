# Handover — NSSCAS Mathematics 8227, repair round 5

19 November 2026. AUTHOR: Codex. Owner: Vitalis. Commission: `review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.

**Work is active. Step 3 waits until both textbooks are complete and independently accepted.** This is a continuation checkpoint, not a completion handback. No owner-only blocker is known. Do not commit or push.

## Current evidence

Focused session 48878 passed all answer, inventory, census, progress, R4 and R5 working checks:

- 3,290 responses across 1,265 response items: 2,696 matches, 216 sketches, 229 show/prove, 67 key-wrong, 40 no-key and 42 key-incomplete.
- 2,974 source records and 2,084 individual mapping reviews.
- 537/891 source pages enumerated; 354 remain, all in YM. Goldie 318/318; YM 219/573. YM PDF12–231 is author-censused, excluding duplicate139.
- Source register167 includes conceptual, diagram, notation and missing-key cautions, including repeated summary occurrences; it is not a count of167 wrong numerical keys.

Goldie’s retained/boundary source author pass is complete: 954 records,606 response items,347 references/figures and one explicitly excluded task. YM Chapters1–4 are now author-censused. Chapter3 covers45 distinct pages107–152 (139 duplicates138),185 records:94 response items/284 responses and91 teaching/given references (70 teaching,21 given). Its response statuses are245 matches,21 sketches,4 show/prove,9 wrong,5 incomplete. Neither book has independent acceptance. Final T5/T6 remain open.

The last completed full proof is session91826: two139-command rebuilds,134 byte-identical assembled artifacts and28 expected negative rejections, at3205 responses/521 pages/2944 records/2022 mappings. This proves C3 through135. Subsequent geometry/closing136–152 passes focused48878 but awaits the next full proof. No build process is active after48878.

## Immediate continuation

Continue YM from PDF232, Chapter5. Nothing beyond231 has an R5 census yet. The next source contact should be rendered and read before authoring. Existing chapter4 is already complete; do not redo153–231.

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
