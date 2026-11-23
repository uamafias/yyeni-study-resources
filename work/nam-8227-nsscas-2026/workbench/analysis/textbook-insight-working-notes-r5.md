# Working textbook insights — 8227, repair round5

These are source-analysis notes from the completed Goldie chapter1 page enumeration and answer checks. They are not the final per-demand synthesis, a recipe contract or a PLAN. The YM comparison, grade calibration and remaining chapters still need completing. All originals remain internal evidence.

Goldie teaches polynomial division through three methods on the same cubic: long division, coefficient comparison against an identity, and inspection (Example1.4, `8227:TB:Goldie:C1:Example:4`, PDF18–19). Example1.13 (PDF27) adds sparse coefficients and a quadratic divisor with a linear remainder. Exercise1A Q16–28 varies monic/nonmonic and linear/quadratic divisors; these examples mostly divide exactly, so they alone would not provide the full range of remainder demands. Exercise1B Q12, Q21 and Q22, plus the unnumbered PDF26 illustration, supply nonzero scalar/linear remainders. A later family analysis should distinguish forward division from inverse coefficient recovery using remainder/factor conditions; they require different learner decisions.

The textbook often scaffolds a cubic through function values, factorisation, roots and a sketch (Example1.6, PDF23; Exercise1B Q1–6, PDF28). NSSCAS2023P2Q1 instead connects quotient/remainder, factorisation and roots. A sketch adds an assessed representation and should remain explicit in the source family. Exercise1B Q7 (PDF28–29) reverses the direction: a crossing, a touching root and an intercept recover the cubic before a new equation is solved. The 8227 demand to reconstruct a cubic from graph data has no usable NSSCAS part in the current2021–2025corpus; this textbook task supports the syllabus gap without becoming examination-frequency evidence.

The modulus sequence begins with the definition and piecewise reflection of y=x (PDF31, Figures1.3–1.4 and Prompt2), then sketches transformations (Example1.14, PDF32), solves inside/outside intervals (Example1.15, PDF33), converts an interval back into modulus notation (Example1.16, PDF34), compares a line with a modulus (Example1.17, PDF34), and compares two V-graphs (Example1.18, PDF35). These are related but have different requested evidence. Source families should preserve forward/reverse representation, graph construction, numerical equations/inequalities and the positive-parameter case (Exercise1C Q7, PDF36). Fractional interval endpoints in Exercise1C Q3 are not modulus-graph coefficient violations; QUAL01 applies to the graph demand.

The book warns about subtracting all signs (Example1.2, PDF17), missing-power columns in division (PDF28), and two disjoint intervals that cannot be written as a single chained inequality (Example1.15, PDF33). These warnings are textbook-derived. Exact examiner-report corroboration remains to be linked before labelling them examiner-evidenced misconceptions.

Three checked key defects matter for later authoring: Exercise1B Q5(iii) labels a negative quartic crossing -2 instead of -1-sqrt(2) (keyPDF333); Exercise1B Q8(i) has the wrong sign in its first factorisation although(ii)is correct (keyPDF334); Exercise1C Q7 reverses the positive-parameter inequality half-line (keyPDF335). Each has4x evidence and an independent calculation in `textbook-defects-r5.json` and `textbook-answer-verification-r5.json`. A mismatch caused by my own missing x in the transcription of1B Q20 was corrected separately; it is not a source defect.

Example1.5 (PDF21–22) begins with a value table and plotted cubic before exact substitution/factors. This is a teaching method, not evidence that a table-built sketch earns NSSCAS method credit. Example1.7 (PDF24) displays exact quadratic radicals before final3dp approximations; later guidance should retain exact forms under NSSCAS convention003 and avoid inferring a general3dp rule from that worked example.

Implications to consider in step3, once the full source analysis is accepted:

- Preserve separate responses and criterion links for factor/roots/sketch scaffolds, including graph-to-equation reconstruction (`Example:6`, `Exercise-1B:7`).
- Include zero, scalar and linear remainders within justified degree limits, and retain alternative division methods (`Example:4`, `Example:13`, `Exercise-1B:12`, `Exercise-1B:21–22`).
- Use the modulus progression to propose scaffold sequences and response branches; do not count every numerical inequality as a new problem type (`Example:14–18`, `Exercise-1C:3–7`).
- Require the positive parameter assumption when cancelling factors in the parameter inequality; use the corrected half-line, with counterexamples that distinguish it from the wrong key (`Exercise-1C:7`).
- Generate a future graph from its actual polynomial/absolute-value expression and verify intercept labels; the two graph/factor sign defects show why copying a printed answer is insufficient (`Exercise-1B:5`, `Exercise-1B:8`).

These remain proposals. Cross-book families, grade bounds, branch marking, Bloom and the diagram-generation acceptance checks are not decided here.

## New source-backed leads from circular measure and graph investigations

YM PDF154explicitly teaches the geometric radian through equal-radius arc and full-turn diagrams; PDF155then converts units andPDF156–163progress from arc/sector formulae to reverse givens,major sectors,compound plates,segments,symbolic crescents andtangent boundaries. Every completed parent item is in answers-YM-C4-opening.jsonoranswers-YM-C4-arcs.json. Conversion is not automatic assessed evidence for explaining the geometric unit. The exact-radius/angle calculations reveal six verified wrong-key outputs across the R5checked population; do not extrapolate a defect count from the earlier review sample.

For future step3consideration only:choose graph windows from the actual period/extrema rather than one fixed default. YM PDF169–171uses−500..500degrees for b=1/3,but the full sine/cosine period is1080degrees,andcos(x/3)reaches its minimum at±540outside that window. Keep global function features distinct from features visible in the displayed interval. YM TryNow12question2(d),PDF175,asks sin(x/2)−2over0..360degrees:global range is[−3,−1],but the displayed half-cycle ranges only[−2,−1]. These are mathematically checkable representation boundaries,not a new prescribed formal proof demand.

YM Examples11–14,PDF173–176,provide a useful scaffold sequence:read extrema/period/intercept;sketch;then recover coefficients from extrema,including a negative cosine coefficient. They also expose source inconsistencies that need individual defect records during the next verification stage. No same-type examination claim or branch decision follows merely from this teaching sequence.


## 18 November 2026: proof and equation-method observations

These are source-backed working leads, not completed T5 family decisions or a PLAN.

- **Proof organisation.** YM PDF196 first says to work on one side, its hints also
  permit simplifying both sides, and PDF200 explicitly illustrates two independent
  simplifications to one expression. Example37 (PDF201) demonstrates that valid
  structure. Preserve the difference between independent transformations and assuming
  the required equality. Compare the precise examination context before turning any
  of this guidance into a marking restriction. The existing examiner rules001,005,
  092and096 respectively concern stating the conclusion,working forward,showing
  establishing steps,andnot substituting the word SHOWN for the conclusion; they
  do not by themselves settle every allowed identity-proof presentation.
- **Missing worked keys.** Try32;Try33(b,c);Try34(b,c);Try35(b,c,e,f,g);Try36(b,c,e,f);
  andTry37(a,c,d,g) have Prove-only key entries onPDF608–610. Their identities and
  author derivation chains have been checked, but no publisher worked proof is claimed.
  They cannot supply official examination award criteria.
- **Multiplier decisions.** The two worked columns onYM PDF205 distinguish an output
  factor2from an input factor2. Both illustrative acute values are correct; the right
  column mislabels a divided working line as2θinstead ofθ. The columns do not give
  complete root sets because no interval is supplied. A later practice design could
  contrast those decisions while explicitly bounding the task (proposal only).
- **All roots and original domains.** Example43(PDF206) contrasts two argument turns
  with a half-turn. Example47(PDF210) explicitly makes between endpoints strict.
  Example46/Try46(PDF209) preserve zero factors instead of cancelling them. These are
  evidence for distinct learner decisions, not merely different numbers. Quadrant
  mnemonics alone do not handle axis-angle roots; the source uses small cosine/sine
  graphs for those branches. Family relations and examination comparison remain open.
- **Precision.** YM PDF203–205 advises retaining a rounded basic angle before later
  calculations, andPDF208uses a different radian intermediate-precision wording.
  Current author checks retain exact/full-precision intermediates. More digits in a
  printed final approximation are not automatically an incorrect answer. The final
  T5synthesis must compare each convention with the applicable NSSCAS marking record.
- **Verification limits.** The bounded symbolic sec/cosec path returned false zero/empty
  sets during source checking. It was repaired by solving an equivalent numerator,
  preserving the original poles,and substituting all candidates into the original.
  Independent Python math enumerates every bounded basic equation root set/count.
  This is a checking-tool limitation, not a source-book defect or independent acceptance.


## Further rendered leads: YM PDF214–216 (not yet census-complete)

Example51 and Try51 connect arithmetic/geometric progressions to trigonometric
conditions. Their ratio/convergence work must remain distinct from the smaller
trigonometric steps. The final family analysis should preserve that connection
rather than treating a progression context as cosmetic wording.

The principal-interval and inverse-function teaching tables onPDF215–216 print
closed tangent endpoints. The correct restricted tangent domain and arctangent
range are open at−90°and90°. The graphs themselves indicate asymptotes; the printed
interval inequalities require a source-defect entry once these figure records
are added. Enlarged tangent crops have been read; the earlier suspicion of a
missing minus at the left arctangent bound was false (the minus is present).

Example52 asks acos(−√3/2) and correctly derives150°. Its final Hence line drops
the argument's minus, printing acos(+√3/2)=150°. The intermediate cosx line and the
cos30°triangle caption are correct on the4xrender; do not invent defects there.
Record the final argument-label defect with the upcoming item/figure census.

## YM chapter4 final tasks and summaries (PDF219–231, 18November2026)

These are source-backed leads for T5, not completed cross-book families or PLAN decisions.

- Example55 andTry55(PDF219–220) keep inverse construction tied to a stated injective branch. Exact reflection coordinates must be distinguished from rounded sample tables. Try55Q2 makes the learner find the largest initial branch before inverting it; Try55Q3 contrasts a squared cosine with a one-to-one cosine transform.
- Example56/Try56(PDF221–222) andRevision4Q1(PDF227) use exact30°/60° projections in connected geometry. Acute arctangent notation is a component, not separate principal-range classification. Prior right-triangle demands use the existing supplementary IDs and never enter direct138-demand coverage.
- Exercise4.2Q1(PDF223) expressly says positive integer a,b,c; this removes the coefficient sign ambiguity that earlier Example16/Try16leave open. The actual multiplier here is3. Q2 asks only an intersection count; it is not numerical root estimation. Q8(PDF224) asks squared ratio values, not a proof or a principal-sign decision.
- Exercise4.2Q3(b)(PDF223) lacks interval/unit. The two degree answers are conditional and incomplete for the literal task; later planning must decide an explicit bounded adaptation. Q5 asks cos3θ butthe key(PDF614,A28) labels its otherwise correct shape3cosθ. Detailed source crops distinguish a real label defect from a shape defect.
- Example57/Try57(PDF225) add changed-centre arc/radius decisions and overlap/region-ratio decompositions. The true show-that angle inExample57has a missing inverse step in its written working. Its reused rounded angle changes a sector intermediate, although the final3sf area remains correct. Carry full precision in later solutions and explain region assembly.
- Revision4Q4(PDF228) uses three tangent circles inside a3–4–5triangle. The radii sums equal the sides; the shaded curvilinear gap is the triangle minus three sectors. This is not blanket coverage of the distinct single-circle segment demand.
- Example58/Try58(PDF226) recover coefficients from symbolic function values. No graph is supplied; do not count these as given-graph interpretation. The twoTry58parameter tasks remain supporting symbolic practice rather than forcing a direct graph-demand link. Example58does explicitly ask range and an exact special-angle value. Its preliminary unit-cosine sketch is a teaching aid, not the actual unknown function.
- PDF229–231are summary teaching figures/tables, not additional assessed items. Their basic andinverse graphs retain domains,poles andendpoint inclusion. A4xreading clears the apparently missing sine minus sign onPDF230; it is not a source defect. The conversion flow is read in the arrow direction. These summaries add representation support,not new recipe families or examination frequency.

Cross-book/examination/grade-description comparisons remain T5work. Textbook originals remain internal; no branch, marking specification or delivery decision is made here.

## Goldie chapter3 source comparison through PDF85

These are source leads for T5, not PLAN decisions. Examples3.4/3.5 and3C(PDF83–85) make factor preservation and range rejection explicit. Goldie warns against cancelling sinθ;3C11's own key nevertheless omits the valid cosine-zero root90°. The independent original-equation solver andseparate numerical enumeration retain it. 3B4(iii)has the same axis-branch lesson with shifted tangents,where unshifted tanθisundefinedbuttheoriginalequationisdefined.

3B6(PDF79) connects a coordinate triangle to two acute component angles andan obtuse sum. Negative tangent describes the obtuse positive geometric angle,not a negative angle. 3B9(PDF80) has a two-angle paired constraint;the key transposes the roles. 3B3(i)literallymixesφandθ;its intendedsingle-angleanswercannot beusedwithout anexplicit source correction. These are distinct source defects,not new required syllabus objectives.

3C6(PDF85) asks sinx/cos2x sketches andintersections,including the sharedminimum3π/2. Counting only transverse crossings would lose a solution. 3C9changes one curve to3sinx−1andhas an inadmissible quadratic ratio−2to reject. Both are candidates for structural comparison inT5;no recipe split is decided here.

The unprompted projectile andpower-reduction expositions(PDF82) are teaching evidence. The supplied ideal projectile model gives a maximum via double-angle/range reasoning,withlevelgroundandnoairresistance assumptions. It doesnot itself assess mechanics derivation. The integration motivation states identities but asks no integral. Their teaching_exposition_counts stay separate from assessed practice andactualfigures.

The next source investigation is Currents(PDF92),newly found in the page census lead. Its arbitrary-phase sum requires cancellation andquadrant cases;do not assume thebook's onepositive-amplitudephaseformula covers all stated inputs. This is pending independent derivation/source registration,not an accepted source claim orphysics pilot.

## Goldie R-form introduction (PDF86–89)

The two headingless derivations use different coefficient orders for sine-plus and cosine-minus forms. Their exact phases are atan(3/4) and atan(4/3); printed36.9°/53.1°are approximations. These are teaching expositions. Example3.6 and Exercise3D1–3 explicitly ask for a specified form, positive amplitude and an acute phase, so those are assessed targets. Exact parameter candidates and displayed rounding are kept separately.

The source's generic all-cases note needs a nonzero coefficient pair and an endpoint-aware phase convention. A negative cosine axis requires one of the±180°representatives; the printed open interval excludes both. A zero vector has no unique phase or positive-amplitude identity. This is a source-boundary qualification, not a chosen recipe convention. The later Currents investigation makes cancellation relevant; its full analysis remains pending.

Example3.6 asks a sketch only on0..2π, while Figure3.12 continues past the boundary and labels13π/6. The unrestricted curve is correct; a source display must still be checked against the requested interval. The correct requested-window endpoint values are−1 at both ends, with two zerosπ/6 and7π/6. Figures and explicit sketch responses remain separate records.

A source-checker omission was found before handback: the previous symbolic fallback returned onlyπ/3 for√3sinθ−cosθ=1 and missed validπ. An exact tangent-half-angle quadratic now preserves the separately excluded half-angle axis; the independent phase-based root enumeration agrees with both roots. This is author verification machinery, not a newly required learner method. The18th negative fixture models this actual failure. A first906-output full run then stopped on a Python-tuple versus SymPy-Tuple parsing assertion in the new independent R-form checker. Normalisation cleared that representation issue; all12persisted R-form candidates now pass separate coefficient/quadrant/function checks. Neither tool issue was registered as a book error.

These are T5 leads and validation evidence. They do not create recipe branches, grade bounds, marking rules or a PLAN.

## Goldie chapter3 closing source analysis (PDF90–96)

Exercise3D4–5tests the requested R-form and actual phase quadrant; the negative/obtuse coefficients are structural variation beyond replacing magnitudes.3D6–8connect that form to extrema,sketches and bounded roots;3D8has two cycles because its argument is2θ.3D9adds a strictly positive denominator3+cosθ+√2sinθand reciprocal order reversal. This is not a request for definitions ofsec,csc,cot.3D10requires a model from the rotated120cm×80cmtable in a130cmcorridor; both acute solutions are physical. The same scalar trig calculation without the diagram doesnot assess that modelling decision. These are candidate family discriminators forT5,not recipe decisions.

Exact phases are carried throughout.3D6prints67.7°instead ofatan(12/5)≈67.380135°.3D10's firstroot30.651026…is printed30.6°rather than30.7°at1dp;the second82.0°is correct.3D11–13explicitlyrequest phase to2dpwhile their keys show1dp;these are incomplete precision outputs,separate from wrong coefficient values. Every defect links the rendered stem/key and independent computation. No cause is asserted for a key with no working.

The previously uncatalogued Currents investigation(PDF92,key341)uses arbitrary phase difference,not only acute phase. Expansion yieldsP=a+bcosc,Q=bsinc,R²=a²+b²+2abcosc. The source's greater-amplitude claim fails for opposite phases and cancellation. Itsatan(Q/P)formula loses quadrants/axes;atan2is used here for verification,not prescribed as a learner method. Zero resultant has no phase or fundamental oscillation frequency. Phase-between needs compatible representatives/shorter-arc assumptions. These missing qualifications are recorded rather than silently narrowing the source task. The power-line photograph is context,not mathematical diagram data.

3Easks the learner to choose among addition,double-angle,Pythagorean,R-form and factoring methods.3E3(iii)'stan4θidentity is defined atθ=π/4even though a proof usingtan2θwould not be. Its author proof uses sine/cosine expansions and retains the final common domain. A symbolic simplifier initially failed to recognise one valid intermediate rational identity; exact polynomial reduction bysin²+cos²=1clears that tool limitation without numerical proof sampling. No book defect was inferred from that failed simplification.

Census93–96separates required principal-value ranges and five formula-reference blocks from excluded unbounded general-root formulas/Activity3.3(LIMIT02). Principal/bounded branches in Figures3.14–3.16remain useful teaching evidence; they donot make the whole general-solutions topic8227scope. All32chapter3figures and the excluded activity have explicit records. The closing outcome page96is prose-only. Chapter3now has a full author census/answer pass through96; final cross-book/exam/grade synthesis and independent acceptance remain open.


## Goldie differentiation through PDF117 — source leads for T5

These remain proposals/evidence leads, not PLAN decisions or an accepted whole-book synthesis.

- PDF98–101 separates the product/quotient rules required in Mathematics2 from optional first-principles proofs(LIMIT03). Example4.1 and4A1 have explicit method instructions; Example4.2 can also be expanded as a polynomial. Factorisation advice is textbook teaching guidance, not an official NSSCAS award condition.
- 4A2–8(PDF102–104) are explicit curves with geometric follow-up. Their tangent/normal demands do not become implicit/parametric objectives merely because a point or a sketch is involved.4A5 combines a minimum, horizontal tangent, vertical normal, intersections and a right-triangle area. The original formula is2x/(√x−1), not2x/√(x−1).
- A newly found polynomial proof prompt on104 is now Prompt7. Existing Prompt2 is the log-graph question on106. The author initially conflated their IDs; the census page check caught it before acceptance. The correction preserves both source occurrences and does not manufacture a source defect.
- Example4.9(PDF107) has correct final4/x but its ln(x^4)=4lnx working loses the negative real branch.4B1(PDF108) provides further log-domain variation:ln(x²),ln((x+1)/x),andln√(x²−1) have different admissible components. Chain differentiation can preserve a branch that an unqualified log-law expansion would discard. This is a candidate feedback focus, not a decision to require one method.
- 4B5(PDF108–109) supplies an odd xln(x²) graph drawn through the excluded origin; the limit exists but does not define the original function there.4B7's xlnx graph also requires its positive domain, despite approaching the limiting origin. A generated visual and its canonical function must use the same domain and point inclusion.
- 4B3(PDF108) supplies a river model valid only for the next3hours. Derivative rates are metres per hour. The supplied model is a given; do not count the item as asking the learner to formulate a model or validate a long-term forecast.
- 4B10(PDF109) asks where f″=0. Its answer has f′≠0, so it is not a stationary-point task.4B12(PDF110) names a stationary abscissa3 but does not ask for all points; the same curve also has a stationary point at0. An adaptation asking for all points would change the required evidence and must include the additional point. Unrequested key classifications and unrequested author audit results do not inflate assessed coverage.
- Activity4.2(PDF110–111) constructs gradient graphs from zeros/signs/near-origin slopes and identifies cosx/−sinx. It is a connected visual calculus task, not merely a request to recall a derivative formula. Its blank response frame is separately catalogued. Prompt5's degree coordinate introduces π/180; it does not itself define a radian by arc/radius. Prompt6 distinguishes graphical evidence from proof without imposing a first-principles proof outside required scope.
- 4C7(PDF114) finds a gradient condition on two pole-separated tangent branches.4C10(PDF115) asks every stationary point on a finite interval;4C12/13 instead supply uniqueness and a branch interval. Those source constraints affect completeness requirements.4C8 rounds both line coefficients to3sf, while4C11 rounds only the intercept; retaining exact internal coefficients prevents early-rounding drift.
- 4C4(iii)'s printed1/tanx answer for d(ln(sinx))/dx needs a domain-preserving cotangent interpretation. Literal evaluation of a tangent intermediary creates holes at positive sine maxima where the original derivative is0. The defect register labels this specifically as a source convention/domain caveat, not a wrong off-pole value. A canonical cosx/sinx orcotx form avoids the extra hole. Its acceptance remains for independent review.
- Example4.15(PDF116) is an implicit building-block drill; it does not alone establish full implicit-curve/geometric coverage. Example4.16 connects the real curve equation to a gradient and tangent at a verified regular point. Prompt3(PDF117) is a vertical-line/single-valued-function decision, not a one-to-one test. The full cubic is multibranch even though local differentiation is valid where Fy≠0.
- Figure4.5(PDF115) retains y≥0 for the upper semicircle; its first-quadrant inset has positive geometric legs and cannot be freely relabelled as another quadrant. Figure4.6(PDF117) is verified by two distinct y-values at the same x. These support different visual decisions from an ordinary single-branch graph.

The final comparison with NSSCAS patterns, grade descriptions, both books and examiner-reported pitfalls remains T5 work. No recipe branch, Bloom level, grading criterion or diagram-generation policy is settled by these notes.


## Implicit stationary and exercise evidence, PDF118–122

The existing folium-origin caution is now reverified at subpart level, not a new discovery. Example4.17's necessary condition y=x² produces the origin and a regular cube-root point. The origin has Fx=Fy=0. Exact local parametrisations confirm one horizontal and one vertical branch; they justify a qualified source interpretation without making parametric differentiation a learner-assessed demand in this implicit question. A regular-slope checker now rejects the singular point unless a separate branch analysis is supplied.

Example4.18 uses a different structure: a bounded implicit sine curve, two regular horizontal tangencies, four explicitly supplied point checks, four gradient values and a branch-based minimum/maximum conclusion. The side points are vertical tangencies, not stationary points. Its two worked slope panels are teaching illustrations, not requested learner sketches. Isolated sample slopes alone are not treated as a proof for an arbitrary curve; the actual implicit equation and box bounds justify the local signs.

Exercise4D1's twelve total derivatives are formal building blocks.4D2–4 verify a supplied point and a regular denominator before evaluating its gradient.4D5/8/10 require every horizontal-tangent point, checked jointly with the original curve.4D6 connects an implicit normal to a second curve intersection and an explicit asymptote sketch.4D7 explicitly requires natural logs for x^x: the positive domain and variable exponent matter, and the coordinates use3decimalplaces.4D9 recovers constants from a point and a gradient, not from a linearised-data graph.4D11 specifies the tangent in ax+by+c=0 form.4D12's nonzero real parameter a is essential to the uniqueness/regularity proof; a=0 creates a different curve structure.

These are candidate family discriminators and boundary cases for the eventual T5 synthesis. No recipe, branch, grading rule or parameter domain is decided here. The source-audit parametrisation at the folium node is not silently transferred into assessed-demand counts.

## Goldie differentiation and integration: author source pass, 18 November 2026

These are item-backed working insights. They do not complete T5’s cross-book, examination and grade-descriptor synthesis, and they are not planning decisions.

**Geometry and regularity.** Goldie C4 Examples22–23 (PDF126–128) distinguish a finite gradient from a valid implicit tangent or normal line. The sideways parabola includes a vertical vertex tangent even though its slope formula excludes that parameter. The ellipse normal has a valid implicit form at axis points where reciprocal-slope working fails. Example23’s solution draws an extra tangent that the question does not request. A later branch’s marking should follow the actual request rather than automatically importing all the model solution’s features.

Goldie4E4/6 (PDF130; keys345) expose nondegeneracy and unsigned-geometry boundaries. A zero scale collapses the intended curve; an axis-coincident normal has no unique intercept with that axis. The hyperbola tangent triangle has area2|ab|, so its printed2ab requires a positive product. These are structural boundaries, not ordinary number substitutions. Source cautions are linked to the items, with scale4 evidence and executable counterexamples.

Goldie4E7 (PDF131) asks for a line containing the intersection of two tangents, not a complete locus. Its answerx=4is sufficient; an unrequested ordinate-range analysis must not become a marking criterion. Goldie4E8(iii) asks for an unbounded general trig solution and stays excluded under LIMIT02, while its derivative and tangent parts remain usable. Goldie4E10’s two exponential signs are negative; the printed target is correct. Goldie Example24’s inline ordinate is wrong but its final minimum point is correct. These distinctions prevent false source-error reports as well as unsound canonical answers.

**Integration structures.** Goldie5A4–5 (PDF140–141) separate signed integrals from positive areas and use inverse-graph geometry to establish an integral oflnx. An author’s independent integration-by-parts check does not make that method a learner requirement. Goldie5A6/8 explicitly request polynomial division or an algebraic decomposition before the subsequent integral. Those requested intermediate results deserve their own demand links; a similar decomposition used only privately in working does not automatically add another assessed objective.

Goldie5B5–6 (PDF145) give two different identity-before-integration structures: phase-shift a squared linear trig combination, or invert a tangent-plus-cotangent identity. In5B6(ii)(b), the original integrand is undefined at its endpoints but has zero one-sided limits. The calculation is valid through its continuous extension; it must not be described as a proper integral of the original expression at those endpoints. This is different from a divergent pole crossing.

Goldie5B11–12 (PDF146–147) assess requested identity proofs and connected integrals. QUAL03 says small integer or simple fractional multipliers, not a maximum multiplier of2. The boundedcos4θequation is easily reduced using the requested identity and does not require a general-solution formula. The syllabus integration wording uses squared cosine as an example of identities facilitating integration; it does not by itself exclude every repeated even-power reduction. Preserve the difference between an explicit syllabus limit and a judgement about a branch’s difficulty.

**Numerical evidence and sketches.** Goldie’s numerical exposition (PDF147–151) derives the collected trapezium formula from individual areas and then asks learners to read chord/curve relationships. The increasing, decreasing and inflecting graphs show that monotonicity alone does not determine trapezium bias. Formal second derivatives are useful author checks; QUAL11 does not require them as the only learner justification.

Goldie5C6 (PDF152; key346) is especially useful: one and two strips both give2, yet the true integral is4. Both coarse grids sample only the minima and miss the two humps. Four and eight strips both give the exact area but produce different interpolation pictures. Agreement between successive estimates is evidence to inspect, not an automatic certificate of accuracy. The final investigation (PDF156–157) reinforces this with convex, concave, mixed-curvature and numerically integrated examples, and an exact counterexample where trapezia are correct but midpoint rectangles are not. Rectangle and midpoint methods remain comparative enrichment rather than new prescribed8227rules.

**Source conventions.** Goldie sometimes prints an ellipsis after a decimal prefix; those digits are not a claim of rounding to nearest. Its5C4six-decimal approximations mix truncation and nearest rounding without a six-decimal requirement. The author record explicitly accepts them within one displayed unit, retains exact unrounded values and records this convention for independent judgement. The final0.64is unaffected. In contrast,5C2(i) explicitly asks four strips but its printedπestimate matches five strips; that is a genuine strip-count error, not a rounding convention. Enlarged reading also confirms that the compound-interest key says10^6payments, and5C11’s lower integral bound is6; both suspected small-contact transcription errors are cleared.

For the later synthesis, compare these structures and conventions with YM’s corresponding integration material and the linked NSSCAS award criteria. Suggestions remain provisional until that comparison and the owner’s required independent textbook acceptance are complete.

## Goldie numerical equations: author source pass, 18 November 2026

C6 (PDF158–175) has several different decisions that should survive the later cross-book synthesis. These notes remain provisional source analysis, not recipe or PLAN decisions.

The opening prompt’s particular quintic is algebraically factorable: x⁵−5x+3=(x²+x−1)(x³−x²+2x−3). The source’s impossibility claim on159is false;the two quadratic-factor roots are exact. The valid graph,sign brackets and iteration examples remain useful. A topic’s general limitation cannot substitute for checking the actual source values.

The census found a headingless decimal-search prompt on162and Activity6.2on171that the previous population lacked. The activity compares four starts of the same quintic map:two converge to the middle root,and two diverge on opposite tails. This is meaningful structural variation in initial conditions,not a cosmetic number change. The final family analysis must distinguish a supplied formula,its original-equation relation,its target interval,and the requested accuracy.

6A contrasts ordinary crossings,touching roots and poles (PDF163–165). A sign change requires continuity;one bracket does not establish the full root count. Conversely,a root can exist without a sign change. The two-graph and cubic-sketch questions require root-count reasoning beyond evaluating a final number. Decimal and bisection methods have separately recorded trial traces where the book explicitly asks for them. The saved midpoint/error intervals in6A6are valid examples,not unique canonical midpoint/exponent pairs;another valid stopping interval may produce different values.

The iteration introduction (PDF166–170) switches representations between polynomial zeros and intersections with y=x. Figure6.9’s generic decreasing cobweb is not the increasing quintic map from Figure6.7. The numerical method can converge to a valid root outside the intended target interval,so a mathematically valid limit can still fail the actual task. Finite stabilising digits alone are not an accuracy certificate;the source itself returns to an original-equation sign bracket on169.

6B2’s principal fourth/square-root forms (PDF171) omit a negative original root unless their positive branch is stated. This re-verifies an existing source caution rather than claiming a new discovery. 6B5/6also ask for choosing an unsupplied rearrangement,which is extension beyond interpreting a given formula. A later prescribed-demand adaptation would need to supply that choice explicitly and record the adaptation. Formal derivative convergence conditions remain excluded knowledge;qualitative recognition that a supplied iteration can fail is prescribed.

6B8–16 (PDF172–174) add different reasoning structures:an integral determines an unknown upper bound;the fixed-point limit yields an exact cubic equation;an interior stationary-point condition needs endpoint exclusion before division;a logarithmic rearrangement needs its positive domain;and a parametric slope fixes the sign before taking a sixth root. These must not collapse into one generic iteration type merely because the final action repeats a formula.

Every6Bcalculation has a complete author trace with unrounded states,required intermediate displays,and an independent original-equation root reference. The stopping record checks an original-equation sign bracket inside the selected rounding cell;it does not claim that two agreeing iterates prove convergence. The independent checker replays the supplied formula through a separate CAS evaluation path and compares reference roots with Ridder’s method. These checks establish only the listed fixed-source cases,not arbitrary future parameter domains.

The final reference wording on175has a qualitative conflict with the preceding steepness advice. It is recorded for independent judgement;it is not treated as a precise if-and-only-if theorem or copied into a generation constraint. An enlarged read cleared a suspected answer-label error:6B16’s key really says(ii),matching its exercise. The actual branch and precision issues remain visible without inventing another source defect.


## Goldie chapter 2: source pass completed, synthesis still open

Source: Goldie PDF38–69, printed24–55; keys335–339. This is author source analysis, not independent acceptance or a completed cross-book T5 synthesis.

The opening power/exponential comparisons and new boxed transformation prompt distinguish a graph's displayed positive viewport from its full mathematical domain. A vertical translation of a^x by k gives intercept1+k; a marked point translated horizontally to(h,1)need not be the new y-intercept. Activity2.1 needs its intended positive-input context stated; its correctly answered general-base counterexample is a separate issue. Ordinary exact-power arithmetic supports logarithms without automatically covering their full examination demand.

The logarithm exercises separate definition/equivalent forms, law rewriting, original-argument domains, simple exponential solves, disguised quadratics, modulus branches and strict/closed inequality endpoints. Examples4and Exercise2B10(iii)/(iv)contain substantive wrong answers. Part10(vi)has a much smaller last-digit truncation/rounding caution with no explicit requested precision. Exercise2D3adds an unexplained factor25. Enlarged reads cleared the suspected half coefficient in2B18, question20/21numbering and400/4000shopping coefficient: do not revive those false leads. All verified subparts retain their actual source keys and exact author answers.

Modelling has three distinct structures: a raw straight-line warm-up(Example6), noisy positive data that require choosing/constructing transformed axes(Examples7–8;2C1–2,6–8), and exact supplied transformed-line points(2C5;2D11,13–14). Ten fixed-data fits use standard-math covariance independently checked against45digit CAS normal-equation sums. Fitted-by-eye source coefficients remain separate. In2C1the source hand fit n≈0.690,k≈180000and the independent fit n≈0.66743,k≈192739give different follow-on period estimates; the key expressly permits graphical variation. A future marker must preserve the learner's defensible selected model and follow-through rather than demand one exact key pair. This audit has not decided an acceptance tolerance.

Axis direction, units and exponent shifts are discriminating decisions. Example7requests logd against logRbut works the reverse orientation: both test straightness, with reciprocal slope interpretations. A radius scale factor10^5changes the coefficient, not the exponent. In2D11the negative gradient is−lnb; in2D14the shifted exponent makes the ordinate interceptlnA−p. A train's first100seconds must be converted to minutes. A requested continuous threshold is not automatically a first whole-year/day count.

The natural-log introduction(PDF59–62)uses reciprocal areas and general change-of-variable proofs. Retain these as conceptual or extension evidence underLIMIT07; do not make formal general substitution a required examination method. The n=0case in the power-law proof needs separate treatment. Signed/oriented integrals for0<x<1are distinct from positive geometric area. The three numerical area estimates use an explicit author1000-strip method, while the book leaves the method open; independent exact integrals verify the values.

Real-world labels need their own source check. USGS source021, acquired through the existing Harvester and read on rendered pages8–9, conflicts with the earthquake energy/magnitude coefficient in2B13. The book's key arithmetic is still correct under its supplied formula. Activity2.2does not define its Richter quantity. Keep these conditional models separate from verified physical definitions. Likewise, the virus example is a mathematical fitted trend, not evidence of vaccine causality or clinical control; the local-user power model eventually exceeds any finite population despite slowing growth.

Proposals for step3, not decisions: separate transformation selection from reading supplied axes; preserve exact log-domain and positive-substitution checks in feedback; distinguish exact-point parameter recovery from graphical fitting; retain model-dependent follow-through and time/unit conversions; support both valid axis orientations when commissioned; specify verified or explicitly hypothetical contextual models. Final connections to YM, examination patterns and grade descriptors remain open until the full cross-book pass.


## Goldie chapter 8: retained parts and method boundaries

This remains a working source synthesis. Goldie PDF198–213 (printed184–199), with keys350–351, now has explicit retained items and scope records. Final cross-book families, examination comparisons and grade bounds are still open.

A chapter heading is not a scope decision. In `8227:TB:Goldie:C8:Exercise-8B:3` (PDF204), the first integrand is a finite polynomial after expansion; its unsigned area is45/2 while its symmetric signed integral is0. The second integrand rewrites into linear powers without partial fractions, and its pole lies outside the shaded bounds. In `8227:TB:Goldie:C8:Exercise-8C:2` (PDF207), part(ii)cancels to1/(x−3)and is prescribed, despite the neighbouring nonlinear exponential. The original pole and its relationship to the bounds remain explicit.

Required methods and mathematical outputs are separate. Several source tasks explicitly force a general substitution even though their integrands have a permitted direct or identity route. Those original method conditions remain additional; the records retain useful mathematical content as supporting/boundary evidence without silently rewriting the question. By contrast, Example11/12(PDF209)and8D1(PDF211)do not force that method. Their particular finite identity routes are derived from prescribed addition/double-angle relations. The rendered syllabusPDF16uses examples rather than an exhaustive list. Complexity relative to grade descriptions still needs independent judgement; this is not a claim every wider Cambridge integral belongs in8227.

`8227:TB:Goldie:C8:Exercise-8C:5` (PDF207)has genuine derivative-to-integral scaffolding. The learner differentiates first, then reverses the supplied derivative; that step does not require independently selecting integration by parts. Its mandatory general-substitution proof is a different demand. Given-result use and the method needed to prove that result must remain visible in connected-part records. The same item asks for an explicit stationary point and classification: it must not receive an implicit/parametric derivative tag merely because it is complex.

The maximum questions `8227:TB:Goldie:C8:Exercise-8D:6/7` (PDF212)need bounded-domain reasoning, not merely one numerical zero of a derivative. Each author solution establishes the sole admissible interior critical input and compares endpoint behaviour. Independent brackets and Ridder checks verify the displayed numerical answers. Their companion area methods remain separately qualified. Radian intervals and the requested versus merely displayed precision are recorded.

`8227:TB:Goldie:C8:Exercise-8D:11` (PDF213)adds a distinct periodic-area decision. The function changes sign afterπ/4, while its absolute value repeats. The numerical first-lobe area is not needed to solve part(ii):40equal unsigned lobes determinek=10. No unstated integer assumption onk is necessary. The absolute-value symbol changes the evidence requirement; a signed integral would cancel rather than count all lobes positively. This is a candidate structural branch for later planning, not an approved recipe.

The new source-method caution is `8227:TB:Goldie:C8:Prompt:4` (PDF213, key351). The key correctly rejectsu=x²−1,but that single failure does not justify the prompt’s blanket claim that all previously taught techniques fail. Onx>1,the previously taught general method withu=(x−1)/(x+1)givesu′/u=2/(x²−1). Preserve the useful partial-fractions discussion while narrowing its impossibility wording. This source-quality check does not add a general integration requirement to8227.

The author QA also exposed a reproducibility issue: an antiderivative for8D1(vi)could be returned in two equivalent forms with different arbitrary constants. The actual-input operation now uses a fixed symbolic algorithm; fresh-process checks agree and exact identity checks prove the old forms differ only by constants. Additive-constant equivalence is restricted to indefinite primitives. A curve fixed by a given point and a definite integral keep their exact values; unresolved piecewise branches require explicit analysis. These checks support source accuracy, not future runtime generation or independent acceptance.

Proposals for step3 remain provisional: distinguish geometric from signed area; retain original poles after simplification; preserve compulsory method instructions; separate supplied-derivative recognition from selecting an integration method; validate all critical branches and endpoints; distinguish the function’s period from the absolute-area repeat; derive each diagram from its own instance. Textbook examination attributions are secondary leads until the primary paper has been verified. Textbook originals remain internal.


## Goldie C8 closing pass: supplied structure changes scope

On PDF216,8E4supplies its coefficient template. Its later integral uses only constant,power and reciprocal-linear primitives;both original parts survive. On PDF228,8H3also supplies a coefficient template;the nonlinear term is odd on the requested−1..1bounds and cancels,leaving a reciprocal-linear integral. These are different from choosing a general partial-fractions technique. The earlier blanket boundary descriptions were too broad. By contrast8E6(ii)on217needs a nonlinear-log primitive;its independent coefficient part survives,withA3,B4,C0confirmed on the native key.

Activity8.2(PDF218,key352)suppliesxcosxandxe^(2x),then explicitly asks for their derivatives,rearrangements and target integrals. It provides the missing reverse-differentiation scaffold. A future plan could contrast supplied-product recovery with unscaffolded method selection;the latter is not automatically8227scope. That contrast is a proposal,not a recipe decision.

Graph families on224–226include full-domain exponential-polynomial sketches,finite positive trig lobes,an exponential fixed-point intersection,and volume regions that lie on different sides of the yaxis. 8G9(ii)–(iv)can use the printed target equation without deriving its extra product integral. Its iteration records every4decimal display and certifies the final2decimal answer. 8G10’sRlies−1/2..0;its maximum at1/2doesnot bound that rotation region. 8G12uses1..eand its volume key is genuinely wrong:π(e²−1)/4,notπ(e²−2)/4. Native question/key crops and independent differentiation/quadrature support defect72. These source defects must not become learner-marking expectations.

Closing practice includes finite identities for odd sine powers,all derived from addition/double-angle relations rather than assumed new memorised rules. 8H2(i)has proper limits8and24,not an improper endpoint at8/3;the earlier boundary note was an author reading error. The source’s general-method tables are useful internal taxonomy,with outside methods clearly labelled. Final cross-book family grouping,grade bounds and examiner comparison remain open.


## Goldie C9: scope follows the requested work,not the chapter name

The full rendered231–247pass found prescribed content inside the differential-equations chapter. Examples9.1–3and9A1–13form or interpret stipulated rates,calibrate proportionality,and use connected geometry rates;they do not solve a separable equation. Example9.4and9B1directly integrate independent-variable gradients;the unnumbered240illustration and9C1(i)fix an integration constant from an actual point. These refine the earlier whole-chapter exclusion. General variable-separation methods remain additional. Each context law is a mathematical premise,not verified chemical,biological,physical or causal evidence.

The same distinction applies within9C8:part(i)uses the supplied cubic volume law and net inflow;part(ii)verifies an entirely supplied rational identity;part(iii)solves the additional ODE. Emptyh0is a boundary where the height-rate formula is singular,not a legal value to substitute into5/h²−1/20. In9C13(i),the semi-angle60°givesr=√3handV=πh³;chain rates establishdh/dt=−Ah^(−3/2),while solving that state-dependent relation remains outside retained requirements. These are candidate distinctions for later families,not new recipe decisions.

Example9.9verifies an explicitly supplied implicit curve;it need not teach a memorised inverse-trig derivative. The connected branch through(0,0)must preserve−π/2<y<π/2and−1<x<1. The book’s√(cos²y)=cosyequality lacks that condition. Two other source cautions are retained:velocity sign follows coordinate orientation rather than distance from the origin,and the extra Example9.6cannot extend e^y=x+Cto a negativex+Cbranch using absolute values. Both useful true reference ideas and their surrounding defects remain visible.

UnderPressureuses a map transect,latitude-dependent distance scale,pressure estimates,a finite half-wave profile,and a qualitative fit judgement. The illustrative source profile996+39cos(πx/900)has high1035,low957anddistance900nautical miles;its derivative fixes approximatea.136,b.0035. Those are one map fit,not unique exact measurements or a verified wind law. Coolingrecords model assumptions,an independently checked explicit exponential profile,weighted mixing and a same-time comparison. The source’s10percent coefficient71is valid when milk is10percent of the final mixture;relative-to-original-volume10percent gives790/11instead. Under the stated unchanged cooling model,the late mixture is cooler by1−e^(−t/160). This is conditional model analysis,not universal physical advice. Both investigations stay supporting evidence;all final cross-book and examiner/grade comparisons remain open.


## Goldie C10 opening: representation and angle-method boundaries

PDF248–254contains free-arrow grids,position versus displacement,2Dpolar orientation,3Dcoordinates,exact/numeric norms,and an equal-vector parallelogram argument. All requested10A2diagrams are separate response records;computing the magnitude alone doesnot complete that source item. Arrowheads on displaced grids matter:10A1(iii)is(3,0)despiteheight2;10A1(iv)is(−3,−1),not its reverse. 10A4includes explicit endpoint reversals;10A5requires geometric interpretation beyond tuple subtraction.

The primaryM1:T7:O05wording requires scalar products for angles between directions. The source’s signed polar directions use an axis-angle convention and arctangent-style method. They are retained as supporting orientation practice,not as proof of full scalar-product demand coverage. The chapter explicitly distinguishes these angles from compass bearings. Later scalar-product work must provide that required method evidence. Source precision also varies:Example10.1uses3significant figures,Example10.3uses2decimal places,10A2keeps exact radical lengths and1decimal-degree directions,and10A3uses3significant figures. No single copied display rule should overwrite those source distinctions.

A separate author check recomputes19magnitude/direction outputs withPythonmath.hypot/atan2and14directed endpoint differences withFraction arithmetic,independently of the symbolic operation code. Seeded wrong-quadrant,zero-direction and sum-of-components norm examples reject. These checks validate fixed-source mathematics;they do not certify diagram transcription,a sketch marker or future generated vector instances. All vector tasks retain existing source IDs;only17new given/teaching figures extend the population.


## Goldie C10 operations and spatial scalar products

PDF255–261contrasts component addition/subtraction with diagrams,all-matching displacement sets,unit normalisation and internal ratios. Activity10.1has13named points:all5position-name and5complete ordered-pair searches are retained and independently recomputed with exact coordinates. The hexagonal-prism example combines regular-face symmetry with one back-face translation;Cartesian recomputation checks all8formal p/q/ranswers without making matrices a learner requirement. Example10.8andPrompt3use positive internal ratios. By contrast10B12on264explicitly givesAC=2AB,placingCbeyondB;its negative/greater-than-one coefficients must not be silently converted into internal ratios.

10B262–264adds geometric explanations:diagonal bisection in a parallelogram,the kite’s unequal upper/lower heights,midpoint-triangle directions,a differently labelled cuboid,andall roots of a magnitude parameter constraint. B3/B5joining-vector goals are displacement/geometry demands;an author’s temporary origin doesnot make position-vector knowledge another assessed goal. Some source numerical displays differ from exam defaults:10B8prints11.74for exact8+√14without asking2decimal places. Keep that as a key-display comparison,not an invented learner instruction.

The scalar-product source264–268makes the officialM1:T7:O05method explicit. Supporting proof prompts list cosine-rule/Pythagorean assumptions,commutativity and3Dextension. Numeric between-vector angle tasks require nonzero vectors and the appropriate0..180°angle. The two diagrammed warnings on268show that reversing just one ray gives the supplementary angle;reversing both preserves the angle. A zero-dot-product right-angle proof also tolerates reversing one vector,because its supplement is still90°. Future alternative-method criteria should preserve those distinctions.

10C268–272broadens the givens before the shared scalar-product step. The room journey uses a horizontal projection for elevation;the6-unit cube combines a trisection and midpoint;the semicircular prism uses radius,length and a midpoint to build coordinates without any circle-area demand;the roof first requires a centred-ridge inference from equal slopes. The4-unit cube uses a different midpoint/face-centre construction and explicitly asks1decimal place for its perimeter. These are discriminating learner decisions,not cosmetic contexts. The final family split/branch decisions await comparison withYM/exam evidence.

Case scope matters in multipart parameter questions:10C6uses p−2for perpendicularity,an explicitp6case for one angle,andgeneralpagain for both distance roots.10C9likewise resets fromq3for an exact cosine togeneralqfor a length equation. Native4xsource resolves two misleading thumbnail readings:10C7(ii)uses2/5,not2/3;10C8(iii)hasOC=6j+pkwith noicomponent. The source keys are correct. No defects are invented from those cleared readings.

Independent vector QA now supplements CASwithPythonhypot/atan2,Fraction endpoint searches,unit/perimeter checks,and a normalised chord/sum formula for between-vector angles;the latter doesnot reuse the source dot/acosformula. Seeded zero-direction,zero-unit,wrong-quadrant,wrong-norm,zero-pair-angle andsupplementary-angle cases reject. These fixed-source author checks do not establish future parameter safety,a visual marker,independent educational acceptance or production readiness.


## Goldie C10 closing: original goals, extra methods and branch preservation

Author source read: PDF272–293, printed258–279; exact answer pages358–359. All retained tasks and teaching/given figures are recorded by author_Goldie_C10_line_opening.py and author_Goldie_C10_closing.py. These are source-analysis records; independent scope/classification acceptance is pending. They do not decide recipe branches.

- Figure10.22andPrompt7(272–273)give joining vectors,midpoint/fractional subdivision and a supplied vector-sum identity. Activity10.2(274–275)has allseven requested multipliers−2,−1,0,1/2,3/4,1,3;the native answer358contains allseven. Negative parameters and values beyond1are meaningful spatial branches,not cosmetic numeric changes. Formal vector-line-equation mastery is not inferred from evaluating the supplied sum.
- Example10.12(iii)(277–278)omits the external unsigned-ratio solution. The printed condition is3|AN|=|NB|on the line,without a segment restriction. SourceA=(−2,4,1),B=(2,1,3)gives internalN=(−1,13/4,3/2)andexternalN=(−4,11/2,0). DefectTB-Goldie-C10-EX12-EXTERNAL-RATIOrecords exact native evidence and full root/point/residualchecks. Planning should distinguish a directed ratio,a nonnegative length ratio and an explicitly internal segment condition;neither missing branch nor unintended ambiguity should transfer.
-10D1(278)has15ordinary displacement,magnitude andmidpoint outputs despite its line-equation section.10D5(ii)(279)independently asks a midpoint. Whole-section exclusion would lose prescribed practice. Its other original formal vector-line goals remain additional.
-Example10.14(280–281)asks an unforced2Dintersection. Prescribed Cartesian equationsy=8−2xandy=(x+1)/2give(3,2);the source’s vector-parameter method is an extra valid alternative.10E4(285)similarly permits ordinary Cartesian intersections after side midpoints. Preserve the original goal and method instruction separately;one numerical median-concurrence observation is not a proof for alltriangles.
-10E3(284)uses supplied positions in a shared time variable,not two independent path parameters. Initial distance,speeds and collision after40minutes are distinct outputs. The shared time is essential to the collision claim. Constant-rate context doesnot create an integration demand.
-10F9(290)requires genuine3Dfigure reading,two obtuse roof angles,and a combined claim:the streamers touch,butare not perpendicular. A shared midpoint proves touching without formal line equations. Feedback proposals:select the common vertex before dot products;split a compound claim into separately evidenced conclusions;do not infer3Dintersection from crossing2Dink.
-10F10(ii)(291)givesP(t)explicitly. The60°condition leads to3t²+7t+2=0,butonlyt=−2is valid;the other root gives120°. This is branch-filter evidence from the original angle,not numerical difficulty.10F11uses the suppliedAP=λABto find the internal angle bisectorλ=3/8andverify3:5ratios. Its addition/cosine/ratio goals are distinct from the extra formal-line/skew tasks around it.
-Examples16–17and10F1–5are kept as supporting scalar-product calculations from supplied directions,with the original vector-line representation qualified as additional. They are not counted as full prescribed original-practice coverage.10F13(ii)explicitly asks only the supplied direction’s acute angle to thexaxis;its earlier skew proof is separated.
-Representations retained:coordinate grid with subdivisions,translated direction comparison,perpendicular-foot reference,tree-guy spatial illustration,roof-coordinate diagram,andthe vector summary. Each has a stable teaching/given-figure ID. None of these pictures is another problem family.

Outstanding T5work:compare these structures with YM,each actual NSSCAS exam pattern,grade descriptions and examiner difficulties. The bullets above are item-backed planning leads,not that final cross-book/exam synthesis.


## Goldie C11: final scope screen and author source pass

19November2026 author checkpoint. AllPDF294–332pages now have an explicit population/scope census;the Goldie envelope is318/318pages. All954retained/boundary inventory records have individual assessed/component mapping:606question/worked items have complete explicit-response checks,347figures have mathematical feature reviews,andone separately excluded whole task has no answer-accuracy claim. These are author records;the book is not independently accepted orT5/T6complete.

New C11 retained sources show why section titles are insufficient for scope:

-Activity11.8(313,key364)directly practises principal inverse-tangent values/ranges in degrees andradians. The printed key uses strict bounds correctly;the informal largest/smallest wording must be interpreted as limiting bounds,no attained extrema. Author-chosen radian examples are explicitly not publisher key entries.
-Activity11.11(315,key364)has nine exact special-angle ratio cells andthe two standard triangles. This is ordinary prescribed trigonometry inside a complex-number chapter.
-11E8(iii)(317)expressly permits an alternative to complex arguments. The ordinary double-angle proof must establish that the doubled principal angle remains in(0,π/2). The numerical tangent identity alone is insufficient to remove allperiodic alternatives.
-11G5(326,key367)and11G9(ii)(327)have useful exact/compound-angle results,butthe original hence/argument methods remainadditional. These are supporting boundary evidence,not full original8227practice coverage.
-11H8(i)and11H9coefficient determination(330,key368)are independently requested real-polynomial outputs. Their later complex roots remainadditional. The nativeH9key has a wrong real component in those non-real roots:−5/2instead of−3/2. Its prescribedk36answer is correct. This boundary defect is registered without adding a complex curriculum demand orcounting its answer as directly assessed8227practice.
-Real-number nesting/classification(294–295,key359)andvector addition/subtraction analogies(306–307,key361)are supporting/prerequisite evidence. The definition key’s unqualified not complex needs non-real complex;the source nesting itself remains useful. These sources do not fill the identity-versus-equation gap merely because they mention equality.

Book-wideprecision evidence is now preserved on the inventory’s Goldie book record fromPDF333printed319:non-exact results3significantfigures,degree angles1decimalplace unless otherwise specified,round only at the end. This is a textbook convention,not an official examination marking rule or a per-stem quotation.

T5still requires the YMcomparison,all-demand/examination/grade-bound synthesis anddefensible cross-book family splits. Do not promote these item-backed observations into approved recipe branches.


## YM C1 opening12–21: prerequisite structure andsource signs

19November2026 focused author pass. AllExamples1–9andTryNow1–9responses are recorded,withTryNow4’s two original questions separate:19items/48responses and21teaching/reference figures. Census12–21is complete,not wholechapter1. The index/surd recap contains useful preparatory practice previously outside the bounded inventory’s opening population.

-Directbinomial-square facets use outer exponent2even when inner terms contain fractional powers. Real root-basis substitutions are explicit;even roots require nonnegative inputs andquotient denominators staynonzero. The sum/difference-of-cubes-style products are not automatically binomial-series questions.
-Common-base exponential equations are preparatory for the official use-logarithms demand;matching exponents alone is not evidence that a learner has demonstrated that official method. Preserve this distinction in coverage counts andfuture source-family proposals. Structures include common-factor extraction,quadratic exponents,simultaneous index equations,division byreciprocals,reciprocal exponents withtwo admissible pairs,andone model constrained bythree points.
-Native source14confirmsTryNow1(b)’s signs:(p^(2/3)−q^(1/3))(p^(4/3)+p^(2/3)q^(1/3)−q^(2/3)). Exact expansion isp²−2p^(2/3)q^(2/3)+q,not the key’sp²+q. Atp=q=1,the original0versuskey2is an independent counterexample. Do not silently repair the source into a presumed intended difference-of-cubes exercise.
-Cleared source leads:the zero-index note correctly hasnegative exponents after0^0;TryNow3(b)has125^n,so its keyn4/−1is correct. TryNow4’s native source hasy−12and1/y;both original equation pairs were checked,not fitted to a desired key.
-The enrichment note on16needs a nonzero rational multiplier for its irrational-product claim;n0is a counterexample. Its example5√2is correct. This is a condition-preservation caution,not a wrong numeric key.
-The four-method quadratic reference on21usesone equation andone root set,not four distinct problem types. Factorisation,formula,completing square andthe table/graph allagree. The source explicitly states a≠0. Its table-plotting guidance must later be compared withNSSCASexaminer preferences;the textbook method is not an official marking rule.

Proposals remain proposals:use sign-preserving expansion checks,original-equation substitution after transformation,andshared-parameter consistency as acceptance requirements when planning relevant branches. No recipe contract orPLANhas been authored.


### YM25–30 — discriminant and proof evidence (author notes, proposals only)

The discriminant builder records every response and thirteen reference/teaching figures. YM progresses from sign/root-count tables to parameter intervals and universal proofs. Keep rational-coefficient assumptions separate from real-root existence: the generic table overstates rationality, while Example19 is false for real p even with its stated p≠−1. Factorisation supplies a direct counterexample and reveals repeated roots. Try19’s integer parameters are a valid, distinct domain.

For future branches, enforce a≠0 before quadratic root-count arguments. Try16Q3 changes to a linear equation at m2; Example20 and Try19(b)/20(a) have true existence conclusions but missing linear-case justifications. Try20(b) requires nonnegative rather than positive discriminant. Try18Q3 tests conditional branch correspondence, so a flat set of roots is insufficient evidence. These are textbook-derived design suggestions, not new recipe decisions or examination marking rules. Item IDs/pages and exact recomputations are in answers-YM-C1-discriminant.json and the defect register.


### YM31–46 — representations and decision structure (author evidence, proposals only)

Source31–35 separates prescribed square completion from optional vertex formula use, then separates equation-to-sketch tasks from graph-to-equation reconstruction. Try21Q1’s correct coordinate conflicts with a wrong vertical tick; native reading clears the apparent Example23 sign lead as−(−4). Keep equalities, bracket signs, orientation and all labels generated from one polynomial.

Source36–42 adds explicit number-line responses, strict/inclusive endpoints, rounded display of exact interval bounds, coordinate-pair recovery and tangency/intersection counts. Try29Q1(b)’s textual key wrongly excludes endpoints while its filled-dot graphic includes them; Try29Q3 has a malformed supplementary lower label. Source-derived feedback proposals should distinguish these response failures, not collapse them into a generic wrong root. Try33Q3’s wrong±4 bounds are countered by exact elimination and a validk3 example. None of these author findings is an official marking rule.

Source43/45 is concrete supporting teaching evidence for the identity-versus-equation distinction: definition, coefficient method and a three-column comparison table. Coefficient exercises directly assess unknown constants, not necessarily the distinction itself. The table should refer to conditional equations and common domains. Source46 shows simple versus touching cubic roots, fractional scales and rational-root factors. Its categorical ban on(x+1/2) is misleading; accept the equivalent scaled factor with a compensated global multiplier. These distinctions suggest future branch and marking requirements, pending step3.


### YM47–59 — source interpretation and progression boundaries

Exercise1Q12 is reciprocal-power work: native47showsy^(−6)−9y^(−3)+8=0. Its key1,1/2 is correct. Exercise1Q20 separates a single intersection from genuine tangency when the eliminated quadratic becomes linear. Chapter1 source49–51 links universal meeting, the tangent equality case, positive-root substitution and a30-mark revision exercise; repeated source occurrences are not new problem-type breadth.

YM52–59 builds from AP/GPrecognition through term formulas, inverse index problems, first strict thresholds and shared-parameter systems. Keep classification nonexclusive for constant/zero cases; ratio division needs nonzero previous terms. Try2Q2’s two a,b solutions must remain paired. A sequence index is a positive integer: an algebraic31.5 means124is not a term, while strict threshold selection needsfloor(t)+1with adjacent-term checks. Do not round a membership index or use ceiling blindly at an integral strict threshold.

Source56Try5(d) lacks the nonzero parameter needed for unique length. Source59Try8Q9 loses a valid zero APby dividing byx; Q10’s keyd12contradicts its13th-term increment24(actuald2). Native source58confirms SEVEN timesT3, clearing a possible six-times misreading. These distinctions are source-backed proposals for domains/feedback in step3, not recipe decisions or official marking criteria.


### YM60–63 — GP signs, index uniqueness and source annotations

Negative ratios require parity-preserving term evaluation; an index inferred from magnitudes must be checked against the signed endpoint. A unit ratio can make an endpoint/term-count problem nonunique: Example11’sn5requiresy²≠11inaddition toy≠0. Try13Q2’s symbolic ratio also needs its intended nonzeroxbranch; atx0zero given terms do not identify a common ratio, while the first-three-term formula remains0,0,0. Odd index gaps fix the real ratio sign; algebraic consecutive terms can instead yield two correlated(r,a)branches.

For first strict thresholds, divide by a negative logarithm with a sign reversal, use a positive integer index and compare exact adjacent terms. Try12(d) printed14is correct; handwritten13is not a publisher correction. Example9’s stem and final values are correct, despite its copied term row dropping the1in12. Future feedback should distinguish source working typos from wrong final results. These are cited source-audit implications,not approved recipe domains or official marking rules.


### YM64–71 — finite sums and what must be selected

The even term-index gap inTry13Q7admits both±2/3ratios andnegative-middle first-three-term branch. A finite sum can lead to more than one valid positive integer term count: Try16Q2hasn1or17. Future marking must not retain only one root automatically. Other roots can be positive but nonintegral and therefore invalid counts.

Block selection is an assessed decision: first/last edge blocks, NEXTblocks, last48of101terms, positive-only terms, andconsecutive partialsum differences require different index sets. Source keys sometimes give only intermediate a,d ormislabel a correct block total asS48. Keep requested outputs, working andnotation checks separate. An APwitha zero term needs a third counting category when comparing positive/negative counts. First positive term andfirst positive partialsum are distinct tasks.

FiniteGPsums do not require convergence. Both quotient forms agree forr≠1,including negative ratios; ther1case usesna. Try20Q1(c)keyequals a6term total despite an8term request; that equality supports an index-slip hypothesis,not a claim about unseen author working. SourceExample18/20has incorrect working operands/subscripts with correct final values. Preserve valid answers while correcting their explanation/labels.

Try17Q2’s requestedNEXT15sum is absent fromthe key. The source digit string is read375witha below-baseline mark; both375→1050andalternate37.5→−7275/4derivations are retained. This remains a source-legibility limitation for independent review,not a silently settled original suitable for learner display.

### YM72–87: bounds, finite limits, modelling and cash-flow timing

- Sigma source74–76 separates writing ordered terms, evaluating their sum and choosing bounds/formula. Zero/negative lower indices are valid. Alternative index shifts need the same ordered terms, not merely equal totals.
- GPthresholds72–73 require strict/non-strict integer handling andadjacentchecks; termthresholdandpartialsumthresholdaredifferent. Try28(i/j)76illustrateswhyakeystatingoneintegerdoesnotcertifythefullsolutionofaninequality.
- Convergence77–79 distinguishesclassification,explicitconvergencejustificationandcomputingthelimit. Finitevaluesclose81or0.5retainexacttotals. Unit-ratiosequencesaregeometricbutnonzeroinfiniteseriesdiverge;negativeratio<−1divergesbyoscillation.
- Physicalunitsandfeasibility80matterbeforeAPalgebra:the62cmropewith3.5mpieceisimpossibleasprinted. Calendarblocks81–83,interestroundcounts,partialfinaldaysandcompletedserviceyearsneedexplicitindex-to-contextmapping. Chain-emailrecipientcount363assumesnewdistinctrecipientseachround;itisnotguaranteedbythreeotherfriendsalone.
- Annualinvestmentexamples85leavepaymentdatesunstated;publisherworkingusesbeginning-of-yearpayments. Preserveend-of-yearalternativesandrequiredeposit/credit/valuationdatesforunambiguousfutureauthoring. Thisisatimingtreatment,notanewrecipecontractinthisround.
- Fraction-onlyrecurringdecimaloutputs84supporttheinfinite-GPmethodbutcanbesolvedbyplace-valuealgebra;donotautomaticallycountthemasdirect8227infinite-sumassessment. Nativeblockdotsarechecked.
- Bouncingball86offersavisualpattern:initialdropisunpaired,everylaterheightisup/down,impactnumberfixeshowmanycompletepairsareincluded. Thediagramisworked-solutionevidence,notalearnersketchresponse.

### YM88–91: transformed series and Pascal investigation

Exercise2.1 Q8 distinguishes the series of squared terms from the square of a series sum. Q9 fixes bids at the end of each hour, so its term index equals elapsed hours; summing bid values does not imply revenue. Q10 uses an ideal infinite extraction model. Q11 combines an exceptional first riser with a constant later rise and tread width: side area is a strip sum, with cm² converted to m².

The previously absent investigation on PDF89 is now individually enumerated: four repeated-product expansions, four coefficient rows and seven conceptual responses. The source’s printed triangle supports coefficient comparisons; faint handwritten worksheet fills are not treated as publisher keys. Author-derived responses without a separate key remain labelled that way.

PDF90–91 separates full expansion, a truncated expansion through a stated power, and a coefficient in a product. Equivalent reordered polynomials are valid; omitting leading terms is not. Try37’s first two keys are truncated, and its second retained coefficient also has the wrong sign. The convolution example only needs degree pairs summing to2; this is a candidate teaching sequence for later planning, not a recipe or branch decision.

### YM92–99: notation facets, Laurent ordering and shifted coefficient depth

Factorial/nCr notation is explicitly required by the syllabus parent objective, but a notation calculation alone does not demonstrate full binomial expansion or term extraction. Those drills retain the notation facet as supporting evidence. Properties of Pascal coefficients beyond the required notation are not automatically examination demands.

Truncation depends on the requested output. A quadratic base can be grouped into a binomial; intermediate higher-degree fragments need not be complete coefficients. Example40’s requested cubic expansion is correct, while its displayed fourth-degree fragment lacks a contribution from an omitted outer term.

A prescribed descending variable order can differ from the order obtained by choosing the second binomial factor r times. Try46Q2 on99 illustrates that reversal for a Laurent binomial. Its constant term is unaffected by ordering, but its sixth term changes. Original nonzero-denominator domains remain explicit. The adjacent independent-variable typo and missing third key are recorded rather than silently repaired.

A negative-power multiplying factor can require higher expansion terms than the target coefficient’s degree. Try47Q1(b) needs the degree6 term to compute degree4 after multiplication by−3/y². This is a structural teaching distinction for later planning, rather than a numeric variation of an ordinary polynomial product.

### YM100–106: coefficient recovery, explicit textbook tariffs and final census

The final binomial tasks distinguish sums of expansions from products, zero coefficients from missing powers, and a nonzero parameter restriction from unrestricted two-root cases. Exercise2.2Q8 gives two correlated(a,n,q)triples. Its native key labels q37 and q41 correctly; a small-render suspicion ofa37 was false and was cleared before registering any defect.

The section beginning103 explicitly calls itself Exam-Style Questions; that label establishes textbook intent,not primary examination provenance. RevisionExercise2 on105 supplies30 printed tariff marks across all parts. Its water-loss question distinguishes a daily term,a cumulative threshold and a percentage of the original volume. The first daily loss is10,so day30loss is68,not key70. Emptying occurs during day41 after40complete loss days; the final day cannot lose its full planned amount because only8litres remain. The GPpercentage alternative has4 printed marks but no answer key; its answer is author-derived,not official marking evidence.

The Chapter2 author census covers all55pages52–106. It has302records:218responseitems with483responses and84printed mathematical references/assets(83teaching references andone given staircase diagram). These references include formula boxes,tables,worked annotations anddiagram panels;84isnotacountof84visualproblems. Two purely author-derived interpretative notes were removed from separate source-reference population and remain attached to their parent questions. Parent context links do not by themselves make a worked-solution figure a diagram given to the learner.

### YM107–119: function evidence across representations and inverse admissibility

The function tasks use graphs,tables,ordered pairs andarrow diagrams. Function validity and injectivity are separate decisions. Duplicate outputs can be valid; identical repeated pairs do not create conflicting outputs. A missing declared-domain output andmultiple distinct outputs for one input are different failure cases. The many-to-one square maps on110/111have no0input; a small-render missing-arrow lead was cleared on native images.

Graphical range questions require attained versus excluded bounds and interior extrema,not only endpoint evaluation. Source112confuses range with codomain and swaps diagram axis letters; its later worked final intervals are mostly correct despite some intermediate sign/endpoint prose errors. A circle can supply relation projections while failing the function test; that supporting exercise does not become a valid function example.

Pointwise function arithmetic on115/116does not demonstrate composition. Ordered composition on116–118does. The source’s explicitg²(x)=gg(x)means iteration in that context,whereas[g(x)]²is pointwise squaring. Example7’s final25is correct,but one printed intermediateg(3)^2shouldbeg(3²). NativeTry6keys confirm negative3xcoefficients; the earlier sign leads were false.

Composition domains require the INNERoutput to lie in the OUTERdomain. Example9’s original outer exclusiont≠−3/2becomescomposite inputx≠−3aftert=x/2. Try9Q3’s explicitx>3restriction filters a valid algebraic root; denominator checks alone are insufficient. Special affine pairs can commute or compose to the identity,so generally noncommutative must not become an absolute rule.

Inverse source119demonstrates whyQUAL08must be checked using actual values. For g(t)=√(t−3),the inverse input domain is[0,∞);the printed evaluationg^−1(−2)=7is invalid. The unrestricted quadratich=t²+2has no inverse function onR;the key’spositive-root formula needs a stated original branch. Conditional source analysis is not a new recipe or a planning decision.


## YM120–135: inverse restrictions, full-domain composition and enrichment graphs

- Ex12(122), Try12(122/key600) and Try14Q1(126/key600): formula existence is insufficient for an inverse domain. Preserve the original image, including sign and strict endpoints. The reciprocal root domain excludes its zero denominator; the composite inverse input is strictly greater than10, not merely radical input>=1.
- Try13Q3(124/key600) asks range before fixing p. The range is conditional on whether the domain includes vertex2. Exercise3.1Q4(134/key601), by contrast, explicitly gives injectivity and therefore forces c>=−2. These superficially similar tasks require different evidence.
- Try14Q2(126/key600) loses an essential branch sign; Q4 resets the original domain before composing, then its key omits the requested formula. Preserve parameter resets and every asked output. Full-domain composition and an author-imposed restricted composition are distinct.
- Ex15/Try15(127) add piecewise sketches, image unions, inverse branch domains and overlapping endpoint reconciliation. The adjacent root/inverse table121 swaps curve labels despite correct adjacent tables. Diagrams and algebra must be checked together.
- Investigations1–6(128–133) distinguish output and input translations/reflections/scales using quadratics, roots, exponentials and cubics. Root domains move with input changes; output scaling preserves cubic roots, input scaling changes their horizontal positions reciprocally. These are source-labelled enrichment. The software menu/QR steps do not assess mathematical demands and are not capability evidence.
- Exercise3.1Q4(134/key601) retains an algebraic pair violating positive b and composite-domain conditions. Suggestions for later planning: retain positivity/domain filtering as meaningful branches; do not count extra algebraic roots as valid alternatives. These remain proposals, not recipe decisions.


## YM136–152: geometric constraints, parameter boundaries and summary quality

- Examples16–21/Try16–21(136–143) distinguish forming a perpendicular/parallel equation, solving an incidence intersection, midpoint recovery,normal reflection and terminal distance/area calculations. Keep supporting coordinate arithmetic separate from directly requested line/intersection outputs. Sign-correlated parameter pairs and original positivity constraints matter.
- Exercise3.2(145/key602) spans equation normalisation, rectangle/parallelogram constraints, exceptional vertical perpendiculars and exact area/foot calculations. Drawn diagrams supply relationships,not measured lengths. Ex17(137) has a point-letter slip while its final equation remains correct.
- Example23(146) uses composition and equal-root parameter conditions; this is not automatically a request for a tangent argument. Both pole exclusion and correlated parameter/root pairs are checked. The exam-style section is source-labelled,but has no primary board attribution.
- Revision3(148/key602) has a genuine missing degenerate parameter: the correct no-solution condition is0<=k<64/9. A discriminant-only approach would miss k0 after turning the equation into an apparent quadratic. Suggested later branch checks should include zero leading coefficients and original rational poles. This remains a PLAN proposal.
- Revision3Q3 explicitly requests3dp for a distance; preserve that instruction rather than imposing default3sf. All revision tariffs reconcile to30. Solution-table references are not official awards.
- Summary149 repeats diagram/coordinate errors and swapped root/inverse labels;150 has unbound vector symbola versus ruleC;152 prints the wrong variable in point-gradient form. Correct task answers,illustrative captions and source teaching defects stay separate. The explicit summary gf(4) micro-example is newly catalogued,not lost among prose.


## YM232–239: coordinate-frame reading and unit-vector wording

- Ex1/2,Try1/2(234–235) distinguish an origin-anchored cuboid,an offset cube and centre-origin cubes. Read actual axis labels,vertex names and half-side signs; page perspective is not a calibrated length source. Try1(b)key615 repeats the different(a)list. Seven named outputs are absent and coincidentGiswrong.
- Ex3/Try3(237) ask norms,including already-unit vectors. Ex4/Try4(238) ask for A unit vector parallel,so either orientation works and one correct printed choice is sufficient. Ex5/Try5(239) require the SAME direction and positive target length,which forbids the negative branch. Keep this wording distinction for later alternatives/feedback proposals.
- The census recovered previously uncatalogued Ex4(238). Native239confirms Ex5finalR=(16/9,2/9,−8/9),clearing a false8/9reading. Source corrections require exact rendered evidence rather than low-resolution impressions.
- Generic inherited figure-method wording was cleaned up to remove a bird-photo-specific clause. Individual notes/features remain source-specific; a full rebuild must regenerate older figure inputs before that cleanup is considered reflected in assembled outputs.


## YM240–247: common vector factors and geometric proof evidence

- Try6Q2(243/key616)needs a common NEGATIVE scale−2; correctq−12,not key+12. Both remaining ratios and a cross-product check independently reject the printed answer. Example6scalar/vector header terminology is defective,but native algebra4=2a+2b and finala,b are correct.
- Source240–242teaches head-to-tail routes,reverse bearings,subtraction and scalar multiplication; these are reference panels rather than extra asked tasks. Bearings are supporting orientation,not scalar-product angle coverage.
- Try8Q2(246)was genuinely absent from the previous inventory. Its midpoint/internal-division outputs are now newly recorded. T1page census continues to find population that a zero heading backlog did not prove complete.
- Ex8/9,Try8/9(245–247)require ratio orientation,consistent origins and actual incidence for collinearity. Formal coefficient tuples represent the source vector basis; they must not be mistaken for Cartesian point coordinates. Component algebra/scaling stays separate from primary geometric outcomes. Aggregate assessed/component IDs are disjoint,while raw subpart roles retain shifts across connected parts.
- Planning proposals: distinguish a free-vector parallel relation from collinearity with a common point; include internal-division direction and origin-offset mistakes in later feedback. These are proposals awaiting T5synthesis and PLAN decisions.


## YM248–251: spatial reference frames and scalar-product orientation

- Ex10/Try10(248–249)compare midpoint POSITIONS from one origin. Half a displacement from a different starting point is a common structural trap. Try10Q3shares an endpoint,not initially a tail; either join/incidence proof or BC=−2BA establishes collinearity.
- Symmetric-roofTry10Q4(249/key616–617)requires central offsets(10−6)/2and8/2,height3,and a ridgeparallelOD. The native diagram places a dotted3dimension againstFG; separate true vertical height from the slantededge lengthsqrt29 in later original assets. Valid text/key numeric solutions stay separate from this diagram clarity defect.
- Ex11(250)was missing from the previous inventory and is now recovered. Unit direction after an AB=BC reconstruction differs from simply normalisingAB. Try11changes the named target vector betweenparts; preserve actual names/origins.
-251pairs the magnitude-angle andcomponent scalar-product methods,bothgiving50. Its heading aboutsame direction means consistent arrow orientation relative to a common vertex; the vectors need not be parallel. Laterfeedback should distinguish an angle from its supplement and one-vector reversal from simultaneous reversal. These are textbook-derived proposals,not official marking criteria.
- Author metadata repair:45inlineanswerprintedlocatorsafterduplicate139wereonehigh;the shared helper now uses the verified piecewise page mapping. An explicit census-to-inline-locator check and seededoff-by-one fixture prevent this structural regression. No numeric derivation changed.

### YM252–255: signed dot products and actual angle vertices

All11items/26responses and5reference panels checked. The same AB/CD known components appear in parallel(q−12)and perpendicular(q13/3)tasks; their learner decisions differ despite cosmetic similarity. Example15pyramid BPC can use both incoming BP/CP or both outgoing PB/PC; reversing one arrow gives the supplement. Example13(b)copies a/b norm labels into c/d work,with correct norms and45degree result. Retain original explicit1decimal-place instructions separately from key display conventions. Calculator strips are source-specific unoperated instructions,not app capability evidence. Author checks only.

### YM256–265: vector chapter complete at author stage

All Chapter5pages232–265are author-censused:143source records,73response items/230responses,70reference panels. New source errors:Exercise5Q1(c)unitvector retains a wrong ksign;Exercise5Q6(a)keydoesnotnormalise its diagonal. Same-direction/parallel wording changes admissible sign choices. Native key618confirmsExercise5Q5(b)negative middle component is correct.

Roof/cylinder/prism/pyramid diagrams require labelled-point reconstruction before selecting rays at the named vertex. Ordinary angle,acute angle between diagonal lines,nearest-degree output,1dpdisplay,and exactacosrational output are distinct response requirements. Reset parameters in independent parts; don't carry perpendicular roots into later preset-value angles. Exact triangle area uses the positive sine and prior mensuration; neither rounded intermediate angles nor this follow-on part creates additional vector-angle demand coverage. Revision30marks reconcile. Independent acceptance remains pending.

### YM266–277: gradient meaning before derivative rules

The book starts with graphical chords approaching a tangent from both sides,then optional first-principles exposition,derivative notation,power/sum rules,changed differentiation variable,explicit chain rule,and substitution for a point gradient. These are different learner decisions/scaffolds. The formal first-principles proof is not required by8227. The source all-real-exponent formula must not expand the qualification's rational-power scope.

Try5Q1explicitly contrasts chain rule with expansion/sum rule and requires an agreement check;both method demands and the expansion have stable separate response labels. Earlier product/quotient expressions can be expanded/split and do not automatically assess Mathematics2product/quotient rules. Same mathematical expression can therefore have a different required-method branch. Preserve original roots/denominators and real odd-root branches;fourthroot(−4x)requiresx<=0,finite derivativex<0.

Source269has a point-label typo in prose but correct displayed derivation. Try7Q1point(3,7)isoffcurve;correct ordinate25whilegradient15atx3remainsvalid. Treatthisasconditional source reuse,not a wrong derivative key. Source advice about double fractions/negative powers is presentation guidance,not an official marking prohibition. Cross-book/examiner synthesis remainsT5work.

### YM278–285: parameters,tangent/normal and angle conventions

RecoveredTry10Q1/2were missing from the old heading inventory;both are now individuallymapped/checked. Two gradient constraints differ from a point-plus-gradient pair. Denominatorclearing canintroduce an inadmissible parameterpair:Example10rejectsa0,b1/2because the given pointwould beundefined.

Given-dy/dxquestions do not require differentiating again or finding the wholecurve. Normalintercept/midpointgeometry is a branch beyond merely returning the normal line. Positive-axisinclination(negative-slopeobtuse)differsfromacuteanglebetweentwolines;keep the source requesteddegreeprecision and actual vertex/point constraints.

Example13on282dropsanegativesignand swaps tangent/normal lines;both wrong lines stillpass through thecorrectpoint,so incidence alone is insufficientvalidation. Try12Q4stem saysTANGENTbutitsnormal-sectioncontextandkeygiveNORMALanswers. Both literal and intended branchesare recorded;the source conflictmustberesolvedbefore reuse. Theseare observedsourceissues,notlearnermisconceptionevidenceunlessconfirmedbyexaminerreports.

### YM286–297: monotonicity,units,inverse rates and stationary sketches

The derivative-sign interval tasks progress from linear inequalities to quadratic sign sets,then whole-domain explanations. Distinguish positive derivative on open sign sets from maximal monotonic intervals;an isolatedzero gradient doesnotdestroystrictincrease. Rational monotonicity requires connected domain components. SourceExample18(b)needs that qualification;its numeric derivative is correct.

ForwardconnectedratesmultiplyaSIGNEDinputrate;inverseratesdividebythenonzerolocalderivativeoruseanonzerorateratio. Example24needs this cancellation condition. Geometric circle/sphere formulas createdifferentunitpowers;Try22Q1numeric6.4piiscorrectbutunitcm/smustbecm²/s. Motionrequires signedvelocityversusspeedandaccelerationversusdeceleration;the sourceprose needsclarificationalthoughitscurrentcomputedexampleiscorrect.

Second-derivative-onlyrequestsdo notadd unasked firstderivative responses. Reducibleproducts/quotientsdo notmandateMaths2methods. The initial stationaryExample26askscoordinates,natureandSKETCH;sourcefirst-sign-changeevidencecanbe independentlycheckedbysecondderivatives. Stationarydoesnotnecessarilymeanturning;thefollowinginflexioncontentmustpreservethis. All are author-analysis proposals/observations,not a recipe PLAN or independent acceptance.

### YM298–305: inflexions,requested evidence and constraints

Stationarycoordinates,naturejustificationandsketchareseparateoutputs. Example29andTry29Q1donotasksketches;the precedingcubic/inflexionexercisesdo. A zero secondderivative is inconclusive;check derivative sign and curvature. Example27's one copied(0,−1)sentence contradicts its correct(0,1)coordinate calculationandgraph;recorded as a source label caution.

Given-derivative tasks may ask only stationary xvalues;do not invent missingordinates ordifferentiateagainbeforefindingroots. Graph-basedparameterrecoverycan require information not contained in the printed point list:Try31Q4's touchingstationaryrootDsuppliesthefourthcubicconstraint. Example32begins geometricoptimisation:identify thefixedvolume,all sixclosedfaces,andpositivedimensions before differentiating the objective. Its diagram is a worked-solution aid,notadditionalgivens.

Representation audit:an analytic polynomial with asketchresponse remains aTEXTinput. C6 solution graphs/formula panels have been corrected to teaching figures ratherthan automatically given figures justbecause theylinktoaparentquestion. TruecurrentC6givenfigures19,20,44,45,46remainexplicit. Whole-book given/solution-roleauditremainsopenbeforecompletion;this is metadata/source-role QA,notadrawingspecorPLAN.

### YM306–313: models,shared boundaries and source-key locators

Fixedvolume/closedarea,fixedsurface/volume,open-tankfacecounts,curvedperimeter,andsharedinternalfencesrequire different model decisions. A quarter-discplate andLshape bothleadtoquadraticarea,buttheir givens/constraintderivationsdiffer;do notcollapseallreasoningintoonefinalderivativepattern. The eight-penlayoutcounts sharedfences onceandasks individualpen dimensions,notwholelandsize. Sourceexplicitlydoesnotrequiremaximumverificationinthattask.

Example34wirearea has a stationaryMINIMUM;workingprose incorrectlysays maximise althoughits numeric stationaryxiscorrect. SourceTry35Q1(b)andExercise6Q3(b)answerblocksare swappedbetweenkey623/624. Bothmatchinganswerswererecoveredand independentlyderived;their actual answerpages/incorrectprintedheadingsremainexplicit. Thisisnotmissing-keyevidence. Nativecone6cm/10cmdimensionarrowscorrectlyshowradii;do notrevivethediameterfalselead.

Givenversusworked-solutiondiagramrolesand source-exam-styleflagsneed a final whole-bookmetadataaudit:shared authoringhelpershad overbroaddefaults. The knownC6figure-rolecorrectionpassed;source314+is explicitlyExam-StyleQuestions. Suchtextbookflagsdo notmeanexamination-observed evidence.

### YM314–321: exam-style section and differentiation checkpoint

Source section6.3 explicitly labels exam-style practice; this is textbook-derived evidence, not an examination attribution. Its tasks distinguish a chord from a parallel tangent, perpendicular distance between lines from distance to the curve, parameter positivity, nonzero signed parameters, and whole-domain endpoint selection. Connected midpoint/distance calculations remain prerequisite extensions where they do not independently assess another AS demand.

Revision6Q4 asks for the minimum of the GRADIENT function, a different target from the cubic's own minimum. Completing the square in the derived gradient is a valid alternative to differentiating that quadratic again. Try39's maximum2/k and minimum4/k remain valid for negative k even though their numerical left-right order reverses.

The revision's printed tariffs total30. Multiple response outputs within one source part share that tariff, rather than doubling it. RevisionQ2 was absent from the heading inventory and is now recovered. It repeats Try15Q2;RevisionQ5 repeats Try34Q1. These are source occurrences,not new type breadth.

C6 author population:56pages,136responseitems/354responses and73figurepanels,including20truegivenassets. Distinguish text-input/sketch-response items from questions that supply a graph. The assembler now retains authored optional domains, connected-part dependencies, duplicate links and tariff groups in the inventory. Whole-book metadata audits and final cross-book synthesis remain open.


### YM322–337: reverse processes,initial conditions and integrability

The introductory derivative-only tasks support the integration explanation but directly assess differentiation. An arbitrary constant is different from the demand to determine its value from data;fixed-curve comparisons must not allow an arbitrary additive shift. Two integrations require two independent conditions. The normal-line tasks add a point-recovery stage before imposing the integration condition;retain the positive-abscissa/positive-parameter constraints.

Several real odd-root primitives require separate negative-component representations. A single point fixes a constant only on its connected derivative-domain component. Example9moves from A(3,1)to the y-axis across a singular derivative at1/3;its printed answer assumes a shared constant or continuous extension. Keep that implicit convention visible when proposing future variations.

Try14(e)crosses an INTERNAL second-order pole at−2/3. Both one-sided integrals diverge+∞;the negative finite endpoint difference−16/11is invalid. This is a source defect,not a valid finite-integral pattern. The existing seeded pole-crossing rejection remains essential. The opening also has a wrong prose family4x³+c,an integrand-name typo,and Example11an intermediate sign error despite a correct final curve. Source evidence and mathematical correctness remain separate.

Standalone symbolic checks are supplemented by numeric derivative checks with actual samples for constant parameters;numeric checks neither prove all parameter cases nor replace real-domain analysis. These16pages are an author checkpoint,not independent acceptance or a completed integration chapter.


### YM338–341: geometry determines the integral

A graph can specify one shaded lobe while leaving another bounded lobe unshaded. Try17(b)requires only the negative lobe1..2ofx(x−1)(x−2);the positive lobe0..1must not be added. In Example18the text instead requests the whole region0..4across a crossing:the correct area19/3is neither its signed integral−8/3nor the magnitude8/3of that whole integral. Preserve the distinction as a future structural branch.

Area338's strip diagrams teach convergence of finite approximations,not a new requested computation. Example18's worked sketch is a solution asset to a text-given problem;the prompt does not request an assessed sketch. Try16was missed by the heading inventory and is recovered as an exercise. Twentyintegration pages now pass author checks;wholechapter and independent acceptance remain open.


### YM342–357: inverse branches,connected regions,limits and rotation

Try20Q2shows why squaring an equation must retain original branch conditions:the principal square root has no negative-y branch,but the figure/key use the full parabola. Both interpretations are kept visible;the defective literal task does not add valid coverage. Conversely,native pages cleared two apparent minus-sign errors;we do not register thumbnail suspicions as defects.

Try22and24include regions bounded by TWOcurves ANDanaxis:they require the lower envelope,not the lens between the curves. Example23supplies enough endpoint coordinates for a trapezium subtraction without independently requiring another derivative calculation. Hints to sketch are distinct from an explicit assessed sketch,as inTry18Q5. Two repeated regions are linked and do not inflate breadth.

Improper integrals use finite cutoffs and explicit one-sided limits. Some convergent integrals have negative signed values;positivity applies to geometric area,not every integral. Infinite limits diagnose divergence rather than finite answers. Source shorthand with∞or1/0is replaced by valid limiting reasoning.

The x-axis volume questions require the square of the WHOLEradius,its cross term,correct bounds,πandcubicunits. Show-by-integration demands are retained. The cone illustration offers an independent mensuration comparison. These are author-checked fixed sources;parameterised recipes and criterion-level marking remain for the later accepted planning stage.


### YM358–361: axis distances and changing washer models

Example34lies LEFT ofy-axis. Outer radius is the larger NONNEGATIVE distance to the axis,not the greater signed x-coordinate. Squaring the signed inverses happens to work here,but a variation must preserve the geometric ordering.

Try34Q2rotates a single quadratic-bounded region that needs discs on y1..5andwashers on y5..13. A single inverse expression over the full height changes the region. An independent shell recomputation checks the same volume;it is author QA and does not impose a new learner method. Try34Q4explicitly asks both rotation axes for the SAME plane region,which changes limits and radial expressions.

Try34Q3uses a CHORD,not a tangent. Try35Q2shades only the circular cap abovey3,so its rotation retains an inner cylinder. A generic under-curve disc answer would be wrong. These decisions should inform later structural branches and diagram consistency checks;they are not yet recipes or parameter domains.


### YM362–375: motion,proofs and integration-chapter checkpoint

Sphere/hemisphere proofs need the doubling step:rotating a quarter-disc produces a hemisphere. Cone proof retains positive height/radius and the required integration method. Motion tasks distinguish supplied displacement from recovering it through integration;the former does not automatically supply integration coverage. Nonzero-time velocity data can fix an initial velocity,and nonzero initial position must not be reset to0.

Exercise7Q7is a verified key failure:velocity changes sign at2inside0..3. Totaldistance21/2 differs from signed displacement3/2. Source distance/displacement wording and a descending height graph labelledDistance are linked to the existing conceptual caution. Maximumspeed requests are bounded by the actual rest-to-rest journey;an unbounded quadratic model could have no finite maximum absolute speed.

Example41(c)omits the left boundary used by its solution. Source40πrequiresx0;the literal three-boundary region gives128π/3fromthecurve-root−4/3. Keep this convention visible rather than inventing a silent domain restriction. Revision7also shows a below-axis quartic rotated about each axis,with a domain-selected fourth-root inverse. Its printed tariffs sum30,and two outputs within1(b)share4marks.

C7author population is complete at54pages/135responseitems/285responses/124figurepanels. Four missed source response items were recovered;source duplicates and part duplicates remain distinct from breadth. The nine exam-style flags come from the explicit textbook section,not examination attribution. Independent acceptance and final cross-book families/138-demand synthesis are still open.


### YM376–383: modulus structure,scope and source reliability

Scalar modulus notation,one modulus equal to a constant,one modulus equal to a variable affine expression,and two equal moduli require different decisions. Negative/zero targets give empty/singleton sets;an affine RHS can reject algebraic branch candidates. Squaring BOTHmoduli is equivalent because both sides are already nonnegative,whereas squaring a plain possibly negative RHS needs original-equation checking. Some source questions explicitly require both methods;others ask learners to alternate methods. Preserve those instructions without inventing official award criteria.

Integer coefficients constrain the prescribed modulus GRAPH practice,not all scalar/equation arithmetic. The reference(1/3)|x|is mathematically valid boundary evidence outside that condition. The first asked sketch2|x−1|+3has integer coefficients and a warranted set of graph features. A graph supplied in a worked solution is not a given diagram.

Try4(a)has a handwritten obstruction over its second key root. We independently derive−15,3but do not pretend to have read−15or certify a publisher error from the obscured glyph. The horizontal-shift graph|x−2|is correct,but accompanying prose reverses the sign rule forh inx−h. Retain the distinction between that h and C inx+C. Neither an obscured key nor a prose typo is automatically a wrong mathematical graph.


2026-11-20 — YM389 checkpoint:695/891pages author-censused (196pending),4,311responses/1,643responseitems;3,286source records and2,762mapping reviews. Focused46657passes. Full49277through383passes2×180/134identical/29negatives,archived. Graph/inequality extension384–389focused-checked;full extension rebuild pending. Next390–393polynomial draft math-only checked,unwired. No independent acceptance;T5/T6and remaining pages open. No commits/pushes.


2026-11-20 — YM399 checkpoint:705/891pages author-censused,186pending;4,395responses/1,676responseitems;3,305source records/2,814mappingreviews;207source defect/caution entries. Focused95173/69279passes after fixing Example14continuation locator. Full184-step double rebuild launching through399. Source400–407read,closingC8draftsnext. Independent acceptance,T5/T6andremainingpagesopen. No commits/pushes.


2026-11-20 — C8 complete author checkpoint406:712/891pages,179pending;4,467responses/1,710responseitems;3,317source records/2,860mappingreviews;209source defect/caution entries. C8=31pages/101responseitems/308responses/64teachingpanels;11textbookexamstyleitems;Revision8=30marks. Focused65556passes. Full73979through399passes2×184/134identical/29negatives,archived. Full186-step through406launching. BothsourcePDFs,19reviewhashes,HEAD,R4history unchanged. C9source407–411read,nextdraft;T5/T6andindependentacceptanceopen. No commits/pushes.


2026-11-20 — YM416checkpoint:722/891pages,169pending;4,549responses/1,741responseitems;3,344source records/2,916mappingreviews;211source defect/caution entries. Focused2008passes. Full60942C8proof2×186/134identical/29negativesarchived. C9through416wired/focusedchecked;417–419draftmathcheck11643,nextwireonlyafterpass. No sourceafter419read. Independentacceptance,T5/T6andremainingpagesopen. No commits/pushes.


2026-11-20 — YM419checkpoint:725/891pages,166pending;4,571responses/1,753responseitems;3,354source records/2,938mappingreviews;211sourcecautions. Focused69136passes. Next420–423sourcealreadyread,natural-logopeningdraftnext;no sourceafter423read. Noactivefullrun;C8fullproofretained. No commits/pushes.


2026-11-20 — YM424checkpoint:730/891pages,161pending;4,618responses/1,776responseitems;3,366source records/2,973mappingreviews;211sourcecautions. Focused24600passes. Full15814through419passes2×190/134identical/29negatives,archived. Allthrough424wiredandfocusedchecked. Source425–431read,nextgraphinvestigationsbuilder;nosourceafter431read. Noactivefullrun. No commits/pushes.


2026-11-20 — YM431checkpoint:737/891pages,154pending;4,674responses/1,786responseitems;3,386source records/3,003mappingreviews;213sourcecautions. Focused9490passes. Bothgraphinvestigationsfullyenumeratedandwiredwithsourceprocedures/notationlimits. Source432–435read,nextdraft. Noactivefullrun;no commits/pushes.


2026-11-20 — YM435checkpoint:741/891pages,150pending;4,701responses/1,792responseitems;3,399source records/3,022mappingreviews;215sourcecautions. Focused5302passes. Nextfull195-step double rebuildthrough435launching. Source436–439read,nextlinearisationdraft;440–443/641–644renderpendingnotread. Restrictedrangeerrorconfirmed;nativegraph2.7/3falseleadcleared. No commits/pushes.


2026-11-20 — YM440 verified checkpoint: 746/891 pages author-censused, 145 pending; 4,728 responses / 1,803 response items; 3,425 source records / 3,059 individual mapping reviews; 217 source defect/caution entries. Focused93669 passes. Full28923 through435 passed 2×195 commands, 134 byte-identical outputs and 29 rejected negative fixtures; archived as analysis/history/rebuild-verification-r5-YM435.json. Linearisation/fitted-model builders through440 are wired and focused-checked. Confirmed Example33 b=10^0.3→2.00, not1.20; Try33Q2 p≈3.1, not0.0123. Graph estimates remain approximate. Try33Q1 negative exponent and Try32Q2 coordinate2.2 cleared earlier false leads. Next441 basic-exercise draft passes math-only80959, UNWIRED. Sources through443 and keys637–644 read;444–447 rendered but unread. T5/T6, whole-book metadata audit and independent acceptance remain open; no step3, commits or pushes.


2026-11-20 — C9 author-population checkpoint447: 753/891 pages author-censused, 138 pending; 4,795 responses / 1,832 response items; 3,446 source records / 3,109 individual mapping reviews; 225 source defect/caution entries. Statuses: 3,983 matches, 311 sketch, 312 show/prove, 91 key wrong, 44 no key, 54 key incomplete. C9 covers41pages,122responseitems/328responses and127panels (114teaching,13given);14 textbook exam-style items;Revision9=30marks. All source builders through447 are wired. Focused27168 caught two missing subpart metadata fields on new source cautions; repaired, R5check37313 passed; targeted dependent regeneration18891 follows. No mathematics or checker relaxation was needed. Full28923through435 passed2×195/134identical/29negatives and is archived. Source448–451read,nextC10openingdraft;no source after451read. Independent acceptance, whole-book metadata audits, T5families/138-demand synthesis and T6fresh-copy/final snapshot remain open. No step3, commits or pushes.


2026-11-20 — YM467 verified checkpoint: 773/891 pages author-censused, 118 pending; Goldie318/318, YM455/573. 4,899 responses /1,879 response items:4,049 matches,317 sketch,338 show/prove,95 key wrong,45 no key,55 key incomplete. 3,529 source records /3,235 individual mapping reviews;233 source defect/caution entries. Focused54225 passes, including independent numeric checks of98function/viewports,20directedangles,57basic/107compositeequations,5inversecompositions,31R-formcases. C10through467 is WIRED and checked:20pages,47responseitems/104responses,80panels. Fixed supporting-exposition role metadata and preserved aggregate component links; basic sin²+cos² support is separated from the reciprocal Pythagorean objective. Full41348throughC9passed2×200commands/134identicaloutputs/29negativefixtures;archived. Next full207-step rebuild through467 launching. Sources468–471read,nextR-formbuilder;no source after471read. Independent acceptance,T5/T6andwhole-bookmetadataauditsremainopen. No step3,commit orpush.


## Provisional source insights through YM467 (author observations, not step-3 decisions)

YM's chapter9 distinguishes several learner decisions that should remain visible in the later cross-book family synthesis. Examples30–32 and Try30–32 (PDF436–438) distinguish choosing semi-log versus log-log axes from recovering constants on already transformed axes. The learner must identify what a slope means in the ORIGINAL model: in A*b^(−x) it is −ln(b), in A*x^n it is n, and in A*B^(ln x) it is ln(B). These are structural decisions; changing the numerical coordinates within one such model is ordinary variation. Exact transformed coordinates must not be logged again. Worked solutions explicitly connect action (take the specified logarithm), reason (linearise the original relation), and result (the coefficient/intercept and recovered parameter).

Experimental tables add a different response requirement. Example33/Try33 (PDF439–440) ask for a transformed plot and an estimated line before estimating constants. The raw-data checks retain full precision and a least-squares consistency calculation, but that calculation is not a mandated learner method or a unique official answer. The source's own selected line in Example33 gives b≈2.00, not its erroneous1.20. Try33Q2's p=.0123 contradicts its plotted positive intercept. Future marking proposals should distinguish ordinary fit variation from arithmetic inconsistent with the learner's own selected line. No official graph tolerance has been invented.

Graph transformations and domains stay connected. Exercise9Q6(a) (PDF441) supplies log_3(x^4) without the restriction needed for an inverse. Exercise9Q14 (PDF442) asks for an x-axis reflection, but its key draws the inverse. These are different requested objects even when familiar formula names appear nearby. A future branch should preserve original domain/range and the requested reflection axis; accepting a familiar-looking curve would miss the demand. These are textbook-derived design cautions, not examiner-reported misconceptions or new official marking rules.

YM chapter10 (PDF448–467) places reciprocal sketches before compound values/proofs, then equations, half/double angles and R-form. Reciprocal sketches require pole positions, zero positions, endpoint treatment, units and separate connected branches. Example3/Try3 (PDF450–451) ask for suitable paired graphs to support a root count. Two decreasing curves alone do not prove one intersection; the independent derivative/interval reasoning is retained alongside the source sketches. A picture shown in the worked solution is labelled as a solution asset, not as givens.

Quadrant information controls missing ratios and half-angle signs. Try13Q4 (PDF464) has B in quadrantIII, so B/2 is quadrantII and its cosine is negative; the key's ± answer is wrong. Try16Q2 (PDF466) exposes a complementary issue: θ=90° is a valid original cotangent-zero solution, although it disappears if a cosine factor is divided away or cotangent is treated only as1/tan. The complete original-equation root set is28.1°,90°,151.9°. These concrete counterexamples can later test branch filtering and response feedback; they do not yet specify recipes.

The source's selected proof route can have a narrower domain than its final identity. Example10 (PDF459) introduces tangent intermediates into a cotangent identity; Example15 (PDF465) introduces tan2x into a triple-angle proof. Direct sine/cosine routes preserve valid final-domain cases. Future alternative-method guidance should state the actual common domain and distinguish a valid conditional route from an erroneous identity. The two cleared thumbnail leads (Try13Q1(d)−527/625 and Try14(b)√((1−a)/2)) are preserved as reading resolutions, not publisher defects.

R-form's introductory prose permits real coefficients, but its chosen R*sin(θ+α) derivation assumes positive R and acute α (PDF467). That combination requires positive coefficients. Phase quadrants, zero coefficients and the zero pair therefore need explicit decisions before generalising the teaching table. The later R-form exercises are the next source population to check. These observations are inputs for T5; comparison with Goldie, specific NSSCAS award patterns, grade descriptors and examiner evidence remains to be completed before any planning decision.


2026-11-20 — YM475 verified checkpoint: 781/891 pages author-censused, 110 pending; Goldie318/318, YM463/573. 4,938 responses /1,893 response items:4,084 matches,317 sketch,339 show/prove,97 key wrong,45 no key,56 key incomplete. 3,559 source records /3,278 individual mapping reviews;237 source defect/caution entries (not a count of wrong numeric keys). Focused84680 passes, including independent numeric checks of98function/viewports,20directedangles,57basic/118compositeequations,5inversecompositions,45R-formcases. C10through475 WIRED and checked:28pages,61responseitems/143responses,109panels. Full56937through467 PASSED2×207commands/134identicaloutputs/29negativefixtures; proof archived. No active full rebuild. Sources through479 READ;480–483 rendered but unread. Next476–477 composite-extrema author module, then478exercise/479exam-style. Neither book independently accepted; T5/T6 and whole-book metadata audits remain open. No step3,commit orpush.


2026-11-20 — C10 author-population checkpoint481: 787/891 pages author-censused,104pending; Goldie318/318,YM469/573. 4,998responses/1,912responseitems:4,136matches,318sketch,346show/prove,97keywrong,45nokey,56keyincomplete. 3,588source records/3,326individual mappingreviews;237source defect/caution entries. Focused73545passes, including98function/viewports,20directedangles,57basic/128compositeequations,5inversecompositions,53R-formcases. C10=34pages/80responseitems/203responses/137panels;7textbookexamstyleitems;Revision10=30marks. Allthrough481wiredandfocusedchecked. Source482–487READ; nextC11opening/product-rulebatch;no sourceafter487read. Full double rebuild through481 launching; prior full467proof archived. T5/T6,whole-book metadata audits and independentacceptance open;no step3,commit orpush.


2026-11-20 — YM490 verified checkpoint:796/891pages,95pending; Goldie318/318,YM478/573. 5,038responses/1,940responseitems;4,172matches,318sketch,346show/prove,99keywrong,45nokey,58keyincomplete. 3,607source records/3,373individual mappingreviews;241source defect/caution entries. Focused41695passed. Full95378throughC10 PASSED2×212commands/134identicaloutputs/29negativefixtures;archivedanalysis/history/rebuild-verification-r5-YM-C10-complete.json. C11through490 wired/focusedchecked. Noactivefullrun. New491–494exponentialdraftUNWIRED,mathcheckhas an equivalent-exponential/hyperbolic normalization issue toresolve before saving JSON. Source491–495READ,496–499renderedbutunread. No step3,commit orpush;T5/T6,whole-bookmetadataaudits and independentacceptance open.


2026-11-20 — YM498 verified checkpoint:804/891pages,87pending; Goldie318/318,YM486/573. 5,100responses/1,963responseitems;4,230matches,318sketch,347show/prove,102keywrong,45nokey,58keyincomplete. 3,638source records/3,426individual mappingreviews;244source defect/caution entries. Focused43961passes. FullC10proof212commandsperpass/134identical/29negativefixturesarchived. Noactivefullrun. Exponentialidentitychecker now handles exactCAShyperbolicnormalisation; new wrong-signfixture rejected,bringing nextfullrun to30fixtures. Allthrough498wired/focusedchecked. Trig499–503draftmathpassed9items/38responses/20panels;nextgenerate/wire/check. Sources through503READ;504–507andkeys649–652renderednotread. No step3,commit orpush.


C11 provisional planning evidence (not T5 completion/PLAN): quotient and logarithm simplification must preserve the original real domain. Try8(c),source489/key646,has a valid both-negative quotient-root component; split-root key removes it. Try8(b) real cube roots retain the negative branch and its printed key is correct. Example14(a),495,has correct2/x and a valid chain alternative,but its2lnxworking loses negative inputs; use2ln|x|or directchain. Try16(c),498,is an actual e^yrelation and allows logarithmic conversion before differentiation; this differs from explicit geometriccurves wrongly tagged implicit in earlier analysis. Try9Q2,490,key646 supplies abscissas where full coordinates were asked. Keep requested-output completeness separate from calculation correctness. Try13Q4(a),494,only asks establishing the givenx3stationarypoint; x0also being stationary does not make that key incomplete. Derivation/teaching panels and original graph software illustrations do not become separately assessed examproof/sketch tasks. All are internal textbook evidence; cross-book/exam/grade synthesis still open.


2026-11-20 — YM506 verified checkpoint:812/891pages,79pending;Goldie318/318,YM494/573. 5,151responses/1,982responseitems;4,277matches,318sketch,350show/prove,102keywrong,45nokey,59keyincomplete. 3,667source records/3,474mappingreviews;245source defect/caution entries. Focused60267passes. Allthrough506wired/focusedchecked. Noactivefullrun;C10fullproofretained. NativeTry23falseuniquenessrecorded;originalrootsetπ/12and5π/12,notjustprintedfirstroot. Nextimplicitdraft507–511math64000pending,UNWIRED/noJSON;initialcomprehensionparseissuefixedusingdirectsolve-listtupleswithoutchangingmathematics. Source507–511READ;512–515renderedbutunread;keys649–652renderedbutunread. No step3/commit/push;T5/T6andindependentacceptanceopen.


2026-11-20 — YM511 verified checkpoint:817/891pages,74pending;Goldie318/318,YM499/573. 5,179responses/2,000responseitems;4,302matches,318sketch,353show/prove,102keywrong,45nokey,59keyincomplete. 3,679source records/3,503mappingreviews;245source defect/caution entries. Focused1513passes. Allthrough511wired/focusedchecked. Source512–515READ;516–519renderednotread;keys649–652READ. Bothsourcehashes,protectedreviewhashes,HEADandR4historyverifiedunchanged. Full219command double rebuild through511launching,with30seedednegativefixtures. LastC10full212×2/134identical/29negativesarchived. No step3/commit/push;T5/T6,whole-bookmetadataauditsandindependentacceptanceopen.


2026-11-20 — YM522 verified checkpoint:828/891pages,63pending;Goldie318/318,YM510/573. 5,228responses/2,028responseitems;4,338matches,318sketch,364show/prove,103keywrong,45nokey,60keyincomplete. 3,710source records/3,562mappingreviews;247source defect/caution entries. Focused14937passes. Full8069through511PASSED2×219commands/134identicaloutputs/30negativefixtures;archivedanalysis/history/rebuild-verification-r5-YM511.json. Allthrough522wired/focusedchecked. Noactivefullrun. Exercise523–524UNWIREDdraftmath61671passes10items/17responses/3figures;noJSONyet. Source525–531READ;C11closes528,C12opens529. Keys649–652READ. No sourceafter531read. No step3/commit/push;T5/T6/whole-bookmetadataaudits/independentacceptanceopen.


2026-11-20 — C11 author-population checkpoint528:834/891pages,57pending;Goldie318/318,YM516/573. 5,261responses/2,048responseitems;3,728source records/3,600mappingreviews;250source defect/caution entries. Focused88114passed;correctedNEWRevision11Q5manualstatusfrommatches tokeywrong(source2/5wrong,finalminimumcorrect),awaitingfullregeneration. Expectedstatusafterlabelrepair:4,360matches,318sketch,371show/prove,106keywrong,45nokey,61keyincomplete. C11=47pages/136responseitems/263responses/138panels;10textbookexamstyleitems;Revision11=30marks. Allthrough528wired. Full224commanddouble rebuildthroughC11launchingwith30negativefixtures. Full511proof219×2/134identical/30negativesarchived. Source529–531READ;532–535renderednotread. NoC12draftyet;no sourceafter531read. No step3/commit/push;T5/T6,whole-bookmetadataauditsandindependentacceptanceopen.


C11 closing provisional insight: independently check BOTH point incidence and tangent slope. Try39Q2source520/key649wronglinepasses the correctpoint(1,12)but has1/8instead3/4slope. Forparametricnature,theX-chainfactorisessential:Try42Q1source526/key649omitsit,andwronglycallsaminimumamaximum;independentY+1=(t−1)²confirmsminimum. Repeatedquestionscanhavedifferentkeyquality:Revision11Q2key649fixesearlierTry9Q2missingordinates;Revision11Q5key650introduceswrongsecond2/5althoughExample42source526correct80/500. Keepdefectsperoccurrence,notblindlyinheritedthroughduplicatealiases. Exercise11Q10source524/key649againshowsprincipal-value/cycleloss:actual0..πneedsP1.979,Q3.055,notoutside−.08623. Thesearetextbook-derivedplanningevidence,notofficialmarking/examfrequencyoracceptedT5synthesis.


### C12 provisional insights through535

The exponential sequence progresses from constant inner-factor correction to expanded squares,parameter bounds,an actual convergent infinite-bound integral,and fixing one or two constants from different initial conditions. The requested show-relations in Example3/Try3 must remain relations;turning each into a numerical root would change the task. The shaded-area sequence distinguishes under-curve and top-minus-bottom regions,and positive parameters justify square-root/logarithm branches.

The logarithm sequence deliberately begins with ordinaryln positive-argument branches,then introduces absolute values during definite integration. This is a source convention,not a universal restriction or an examiner rule. A planner should retain original-domain components and distinguish primitive validity from definite-integral continuity. Example8(b)is a serious counterexample:its interval crosses3/2,but the working subtracts endpoints anyway. ln|u|does not repair that error. Keep this defective exemplar internal and use properly continuous intervals in any later authored work. These are T5 evidence notes,not a PLAN or recipe specification.


### C12 provisional insights through541

Rational integration proceeds from safe positive and negative denominator intervals to division/HENCE chains and two orientations of the same shaded region. Try10Q2's horizontal-strip setup is a requested unevaluated integral,not another numeric answer. Its complementary area should use the unrounded first area;its key's3sf display is not an explicit precision instruction in that question.

The trig sequence distinguishes direct affine primitives,identity choice for unscaffolded squared powers,repeated reduction of cos⁴,and a supplied identity that scaffolds a later integral. Choosing an identity should not be automatically claimed where the preceding part already supplies it. Try16Q3 specifically requires expanding sin(2x+x)before double-angle reduction;its cubic integral then uses that established relation. These method and dependency distinctions should inform T5 family splits rather than cosmetic changes in values. Source diagrams used solely to evaluate special angles are solution aids,not GIVENgeometry;the0°reference is a limiting degenerate diagram,not a normal triangle construction.

Author QA now retains real logarithmic component derivatives and supports an explicitly declared affine CAS coordinate for a shifted secant-square sum. The normalized integration input is proved equal to the original integrand,all derivatives are checked,and independent finite-difference evidence remains required. This internal CAS aid does not turn a syllabus-exempt general substitution method into a learner requirement. The old shifted tangent derivative was rechecked after the equivalence change to prevent a false source-key defect.


### C12 provisional insights through551

Explicit quotient differentiation supplies cot/sec derivatives for later reverse recognition;this is distinct from demanding memorisedreciprocalderivatives. Finitecot²integrationcanincludexπ/2becauseoriginalcot=cos/sinisdefinedthere;1/tanhasaremovablegapandmustnotshrinktheoriginaldomain. Shadedtrigareasrequirethefirstindicatedlobe,aninteriormaximumbound,oraspecifiedproduct-curvezeroratherthanallperiods.

Thepairedheadinglessx²workedprompts546compareexact124/3againsttrapezium42andareseparatelyrecovered. Numericalmethodfamiliesincludeoriginalnodeconstruction,finalprecision,stationarycoordinatepreparation,justifiedbias,andcomplementaryarea. Example22reversestheerrorsignwhenAissubtractedfromafixedrectangle. YMcurvaturewordsconflictwithusualdirectionlabels;itsactualchordreasoningremainscorrectandshouldbetheportableteachingbasis. NativecheckingclearedtheapparentTry21Q1graphintercepterror:itsverticalbound1isbelowapositivecurveordinate. TheseareT5evidenceinputs,notPLANdecisions.


### C12 completed author-population inputs,through557

Thefinalexercise/revisionsequenceadds exactsingle-loganswerformswithwithout-calculatorrequirements,positiveunknownintegrationbounds,anexplicitintegrandsketchandbiasjudgement,andavolumeusingthepreviouspart'sintegral. Sharedsubpartsarepreservedaslinks ratherthanwhole-questionduplicates. Revision2'sboundedtan-equationhasone repeatedauxiliaryroot;bothoriginalviewportandpoleexclusionareessential. Numericalestimateprecisionmustretain0.90for2significantfigures. Theendpoint-undefinedtan/cotintegrandhasremovablelimits;separatehalfintegralsestablishconvergencewithoutprincipal-valuecancellation.

Sourcegraphicsneedfunction-labelchecksaswellasshapechecks:Exercise4(c)diagramlabelincorrectlyrepeatsanearlierintegralalthoughitsstem/region/keyarevalid. Twootherapparentplot/exponentdefectswereclearedbynativeinspection. TheauthorpopulationiscompleteforC12,butT5familyclassificationandexamination/gradedemandcomparisonremainpending. Theseareevidenceinputs,notPLANdecisions.
