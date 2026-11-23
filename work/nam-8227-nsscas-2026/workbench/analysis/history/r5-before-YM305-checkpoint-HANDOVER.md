# Handover — NSSCAS Mathematics 8227, repair round 5

Role: AUTHOR (Codex). Owner: Vitalis. Workspace: `work/nam-8227-nsscas-2026/`.
Commission: `workbench/review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.
Work is active. No owner-only decision blocks progress.

## Current checkpoint

Focused check 23288 passed through YM PDF page 297: answer recomputation, inventory, census, progress, R4 and R5 working checks.

- 603 of 891 pages author-censused; 288 remain. Goldie: 318/318. YM: 285/573 (PDF 12–297, excluding duplicate scan 139).
- 3,722 responses across 1,419 response items: 3,087 matches, 220 sketches, 249 show/prove, 76 key-wrong, 41 no-key, 49 key-incomplete.
- 3,086 source records; 2,344 individual mapping reviews.
- 184 source defect/caution entries. This includes wording, domain and diagram cautions; it is not a count of wrong numerical keys.

**Active full rebuild: session 58518.** It runs two 158-command rebuilds through YM297 and 29 negative fixtures. Until it ends, do not change wired tools, globbed answer/census JSON, assembled analysis outputs or working notes. Reading sources and drafting unwired Python files is safe.

Last completed full run: 99968, through YM285; two 155-command rebuilds, 134 identical outputs and 29 expected negative rejections. Proof: `analysis/history/rebuild-verification-r5-YM285.json`. Newer content has focused checks until 58518 completes.

**Pending correction after 58518:** In `author_YM_C6_second_derivatives.py`, Example26 (PDF297) has `representation='graph'` because it asks for a sketch. Its GIVEN is actually the polynomial in text. Change the item/part given representation to text; retain `sketch_response_required=True`, the sketch response and graph representation of worked-solution Teaching-figure36. Regenerate and check. This changes metadata, not answers or counts.

## Exact continuation

1. Finish the active full check and archive its proof. Apply the pending representation correction.
2. Integrate the unwired draft `tools/textbook-r5/author_YM_C6_inflexions.py` (PDF298–301): 8 items, 30 responses, 7 references. Pure-import mathematical checks passed; no output JSON has been written and it is not wired into the runner. Register Example27's copied ordinate caution first: native image `YM-C6-Ex27-coordinate-native.png` confirms its nature sentence says (0,−1), while its original function x³+1, preceding calculation and final sketch correctly give (0,1). The inflexion classification is correct.
3. Continue from PDF302. Contact302–305 is rendered AND READ, but not authored or censused. Later pages are not read. Keys618–625 are rendered and read.

All C6 builders through297 are generated and wired: opening, rules, gradients_tangents, normals_angles, monotonicity, rates, second_derivatives. The last three added 32 response items, 69 responses, 16 reference panels and 12 pages. C5 is author-complete at PDF232–265: 34 pages, 143 source records (73 response items/230 responses and 70 references).

Goldie's retained/boundary author pass and YM Chapters1–5 are author-censused. Neither book is independently accepted. C6 remains partial. T5 families/138-demand synthesis and T6 fresh-copy checks/snapshot remain open. The analysis snapshot stays at R4 until T6.

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

## PDF302–305 notes already read

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

Both textbook hashes, all19 protected review hashes and HEAD were rechecked unchanged after YM285. HEAD: `11cd03fe639f9936dd9f83fd04bd6f04d5181676`. Part1 remains821 award rows (818 official/3 derived),42 E flags,95 marking rules,31 confirmed Cambridge pairs across29 NSSCAS questions; independent acceptance pending. Earlier source resolutions and cleared false positives are preserved in `analysis/history/r5-YM297-HANDOVER.md` and prior checkpoints. Working synthesis: `analysis/textbook-insight-working-notes-r5.md`.
