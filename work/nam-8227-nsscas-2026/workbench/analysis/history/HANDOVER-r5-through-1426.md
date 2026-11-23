# Handover — NSSCAS Mathematics 8227, repair round 5

18 November 2026. AUTHOR: Codex. Owner: Vitalis. Commission: `review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.

**Step 3 waits for both textbooks complete AND independently accepted.** Continue Part1 and all T1–T6. No owner-only blocker exists. This is an active working checkpoint, not a completion handback.

## Current checkpoint: 1,426 outputs; full pass observed

Focused answer, independent numerical, inventory, census, R4 and R5 working checks passed. **Full double rebuild 27937 passed: 130 artifacts byte-identical and all 21 negative fixtures rejected for their expected reasons.** This is author QA, not independent acceptance.

- 2,356 source records;898 fresh assessed/component mapping reviews.
- Census212/891pages;679pending. Goldie PDF15–37,70–157,176–197;YM153–231.
- 551response items/1,426outputs:1,104matches,126sketch,143show/prove,31key wrong,7no key,15incomplete.125manual/1,301executable.
- 57formal source defect/caution entries. Domain,question,working,visual and precision cautions are not all numerical key errors.
- Additional numerical checks:43proper integrals,28real primitives,34trapezium computations;98graph/viewports,20angles,57basic/94composite equations,5inverse compositions,31R-form cases. These are author QA, not independent reviewer acceptance.
- All19baseline review-file hashes and preserved R4snapshot rechecked unchanged;HEAD remains11cd03fe639f9936dd9f83fd04bd6f04d5181676. No commit/push.

No runner is currently active. The latest complete rebuild proof is `checks/rebuild-verification.json`.

## Newly completed integration source segment

Goldie C5 PDF135–157 now has a complete author page and response pass. Its31given/teaching/reference figures are separate from problem counts. The headingless Figure5.7three-graph prompt was missing from the prior inventory and now has stable ID `8227:TB:Goldie:C5:Prompt:4`. Both series/compound-interest investigations and every guiding subtask of the final rectangle/midpoint investigation are answered. The final investigation has20experiment rows and an exact counterexample;no printed key is falsely claimed.

Scope remains explicit:Maclaurin series is excluded source evidence;finite compound growth is prescribed but continuous-frequency limits are enrichment. Rectangle/midpoint rules and formal convergence/error theorems are comparative enrichment. The book’s general advice to prefer analytic methods does not override a source question that explicitly requires trapezia. QUAL03 permits small integers/simple fractions,not only multipliers1or2;5B11’s boundedcos4θequation is not excluded by an invented maximum2.

Source issues and cleared leads:

- 5C2(i),151/key346:four strips giveπestimate3.131176470588…,but key3.1349…matches five strips. Genuine source error with4x evidence;do not change the stem to fit the key.
- 5C4,152/key346:two six-decimal approximations truncate rather than round to nearest. The question does not demand6dp. An explicit author policy compares those approximations within one displayed unit,preserves exact values and records the convention for independent judgement. The final0.64is correct. Do not report it as a wrong final answer.
- Ellipses denote decimal prefixes,not nearest rounding. Worked8/16-strip circle estimates and5C2prefixes use an explicit truncation comparison.
- 5B6(ii)(b),145:original6/(tanθ+cotθ)is undefined at endpoints0andπ/2,but equals3sin2θinside and has zero one-sided limits. Record the continuous extension/improper endpoint argument,not a proper integral of the original endpoint values.
- Compound-interest key345says10^6payments,not10^5,and its5dpclaim is correct. 5C11’s lower bound is6,not4;ln125is correct. Both small-contact transcription leads are cleared by4x reads.
- 5C6coarse estimates2and2are both wrong;the true integral is4. Preserve the missed-hump/aliasing lesson and all four shading panels.

Verifier corrections:significant-figure quantization now handles tens/thousands as well as decimal places. Positive/negative/large/small fixtures pass;none of the prior1,248outputs changed. Real logarithm primitives use separate nonzero components;proper integrals reject original discontinuities. Trig pole ImageSets are checked against the exact finite interval instead of treating an unresolved subset expression as a mathematical failure. Two new fixtures reject an original pole crossing and a singular parametric derivative. `verify_textbook_integration_r5.py` adds independent quadrature,real-branch derivative spot checks and sums of individual trapezium segments. All remain fixed-source QA,not runtime generators.

The source-backed working synthesis is `analysis/textbook-insight-working-notes-r5.md`. It does not complete T5’s final cross-book/examination/grade-bound synthesis.

## Next: Goldie C6 PDF158–175

Contacts Goldie-C6-158/162/166/170/174 have now been read. They are discovery leads, not yet a C6 census or completed answer pass. Key contact Goldie-key-C4-C5-345 includes347–348and has been read;later6Banswers may need a349+render. C6covers sign-change bracketing and supplied iteration,which are prescribed M2T6demands;inspect their exact syllabus records before scope decisions. Bisection algorithm step counts and formal convergence conditions have separate extension/exclusion limits in the existing records. Reconfirm them from the pages.

Then finish remaining Goldie/YM pages,all investigations/answers and value-level qualifiers(T1–T4),full cross-book families/per-demand insights(T5),and T6fresh-copy/deterministic checks and author-complete declaration awaiting independent review. Do not freeze early:the current snapshot remains R4.

## Newly completed source segment

Goldie C4 PDF97–134 has a complete author page and requested-response pass. Its 57 individual figure/reference records include formula tables and solution panels, not 57 independent problem types. The final cross-book/examination/grade-bound synthesis and independent acceptance remain open.

Parametric Examples19–24 and 4E1–15 are now wired into the builder. Coordinate tables, full versus restricted plotting domains, singular parameters, tangent/normal lines and original poles are explicit. Derivative-at-parameter checking now applies the requested substitution and rejects a zero original x-derivative. The focused mathematical checks caught and corrected an author-drafted astroid line scaling before passing; it is not a source defect.

Important source readings:

- Example20 asks whether **any** x-values are excluded. The key's x<0 is valid. The restricted plot has x∈[0,4], while the original full curve has x∈[0,∞). Do not revive the cleared missing-x>4 allegation.
- Example23 asks for ellipse and normal; its solution's extra blue tangent is not a learner requirement.
- Example24 has an inline y=2 typo at t=−1, but correctly concludes minimum(−1,−2). The final answer is not wrong.
- 4E4 needs a≠0 for the intended curve and t≠0 for two unique normal axis-intercepts; the source states only a constant. At t=0 the normal is the entire x-axis.
- 4E6 area is 2|ab|, with a,b,t≠0 for the intended hyperbola/intercepts. The source prints 2ab without a positive-product condition; a=1,b=−1,t=1 is an executable counterexample.
- 4E8(iii) asks an unbounded general trig solution. It is solved as internal source evidence but excluded from 8227 coverage by LIMIT02. Parts(i)–(ii) remain in scope. The apply layer now preserves explicit per-item scope overrides.
- 4E10 has **negative** exponents e^(−t) in both coordinates. Its tan(t−π/4) target is correct. Do not register the cleared positive-exponent transcription lead as an error.
- 4E7 asks for a line containing the tangent intersection, not a complete locus. x=4 answers it; no missing ordinate-range defect is claimed.

## Retained earlier work and boundaries

Part1 author pass:8marking-row fixes,42Eflags,821award rows,95rules,schema/record repairs and report defects. Provenance31confirmed pairs on29NSSCAS questions,3structural comparisons and1hidden wording-only hypothesis. The119×3208page screen disposed158threshold candidates on136rendered pages;below-threshold unread leads remain unread. No unsupported originality claim.

Goldie C1 PDF15–37,C3PDF71–96,C4PDF97–134,C5PDF135–157and YM C4PDF153–231have author page/response passes. C7PDF176–197is scope-screened. C2remains largely open despite its closing70page being recorded. T5/T6and independent acceptance remain open across the books.

Old checkpoint narratives are preserved in `analysis/history/HANDOVER-r5-through-1248.md` and earlier histories. Use the current checkpoint above to resume.

No commit/push. Do not edit review folders,source PDFs/root textbook,standard,other subjects,app code or pinned checkouts. Preserve unrelated dirty work. No PLAN,recipe contract,recipes,runtime generators,work orders,imports,assignment oractivation. Source QA helpers are not runtime generators. The preserved R4snapshot hash is f3b682495a66d71f6750e76df7972899eb8cb1a2a4b3f0f87cd15aaef5dccde1. FinalT6requires fresh-copy verification and a reviewer-chosen blind sample;never generate an author-selected acceptance sample.
