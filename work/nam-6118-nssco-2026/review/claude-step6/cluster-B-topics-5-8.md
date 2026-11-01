# Cluster B review: NSSCO Physics 6118, topics 5, 6, 7, 8

Reviewer: independent physics reviewer. Review only; no repository file was edited.
Package: /Users/yyeniai/yyeni-study-resources/publish/nam-6118-nssco-2026/
Method: read all four notes files in full; dumped every item of the four flashcard JSON files; solved every MC question independently before reading the key; recomputed every number in python; viewed every referenced PNG; ran an 8-word shingle comparison of notes and decks against the syllabus text and all 24 PDFs under Question Banks (papers, mark schemes, examiner reports).

Severity: S1 wrong or unsafe; S2 imprecise, could cost marks or teach a misconception, or out of scope; S3 pedagogy, clarity, duplicate, weak distractor; S4 minor.

Numeric recomputation result: every numeric worked example in the four notes files, every calculation flashcard, every MC numeric key and distractor derivation, and every short_answer calculation is arithmetically correct. The only numeric error found is the topic 8 practical gradient (8.1). Numbers checked: topic 5 (4 m/s, 2.75 m/s, 3.5 m/s, 16 m, 6 m, 12 m, 20 m, 11 m/s, 0.2 m/s²), topic 6 (200 N/m, 3.0 N, 4.0 m/s², 2.0 kg m/s, 6.0 kg m/s, 2.0 m/s, +4 kg m/s, 83 N/m), topic 7 (24 N, 2.4 g/cm³, 0.80 g/cm³, 18 N, 9 cm³, 7.5 N, 0.32 kg, 2.7 g/cm³), topic 8 (3.0 N m, 8 N, 3.6 N m, 4 N, 1.2 N m, 6 N, 5 N m).

Cross-topic fact used in several findings: the correct-option letters of the MC set are A D C B A D C B A D C B in topics 5, 6, 7 and 8, and in all 26 other decks I checked (topics 1, 4 to 28; topics 2 and 3 have no MC key in the glob output). See 5.2, 6.3, 7.2, 8.6.

---

## TOPIC 5 Position, speed and acceleration

5.1 | Topic 5 | notes section "Use the constant-acceleration equations v = u + at, s = ut + ½at², v² = u² + 2as, a = (v − u)/t and s = (u + v)t/2"; deck coverage | S2
Quoted: the section contains only "Choose an equation containing the known quantities and the unknown required. To find final velocity ... use v = u + at. To find displacement without a time value, v² = u² + 2as may be appropriate."
Problem: the syllabus says "recall and use motion equations in calculations". The notes give no worked numerical example for s = ut + ½at², v² = u² + 2as or s = (u + v)t/2, and no free-fall calculation with g = 10 m/s². In the deck, v² = u² + 2as is never used. s = ut + ½at² appears only in MC Q12, and s = (u + v)t/2 only as a hidden alternative. The only equation card is ITEM-6118-5-020 (v = u + at). There is no card on free-fall calculation (objective 2.3.3-06 has only a "state 10 m/s² downward" card).
Fix: add a worked example for each equation, at least one for v² = u² + 2as (for example u = 0, a = 10 m/s², s = 20 m, v = 20 m/s) and one free-fall calculation, plus two cards using s = ut + ½at² and v² = u² + 2as.

5.2 | Topic 5 | ITEM-6118-5-P01 (MC set), all questions, and the matching list in the notes "Practice task" | S2
Quoted keys: Q1 A, Q2 D, Q3 C, Q4 B, Q5 A, Q6 D, Q7 C, Q8 B, Q9 A, Q10 D, Q11 C, Q12 B.
Problem: the key follows the exact cycle A-D-C-B repeated three times. Each letter is used exactly three times. After four questions a learner can predict the rest. This repeats in every deck I checked (cross-topic). It invalidates the set as practice.
Fix: shuffle options so each letter is used 2 to 4 times with no repeating cycle, and re-write the distractor feedback to match.

5.3 | Topic 5 | ITEM-6118-5-021-MISCON, figure used: assets/figure-6118-5-03.png | S2
Quoted prompt: "Graph A is horizontal at 3 m/s on speed-time axes. Graph B is horizontal at 12 m on distance-time axes."
Problem: the attached figure is the figure for card 5-012. It shows two speed-time lines at 0 and 4 m/s ("At rest", "Steady motion"), titled "Two horizontal lines, different speeds". It shows neither a 3 m/s line nor a 12 m distance-time line, so it contradicts the card. It also confuses a learner by showing "rest" on a speed-time graph, which is exactly the misconception being tested.
Fix: remove the figure or generate a two-panel figure: speed-time at 3 m/s and distance-time at 12 m.

5.4 | Topic 5 | ITEM-6118-5-004-DEF | S2
Quoted: prompt "Define displacement."; canonical "Displacement is the directed change from the initial position to the final position."; guidance "Definition: ... (1 mark)."
Problem: the syllabus definition is "a vector which has a magnitude equal to the shortest distance between the initial and final points and a direction from the initial to the final point". The canonical answer omits "vector", "shortest/straight-line distance" and "direction from start to finish". "Directed change" is jargon. The guidance accepts only the one sentence and lists no alternative wording, so a correct learner answer ("the distance in a straight line from start to finish in a stated direction") risks zero.
Fix: canonical "Displacement is the straight-line (shortest) distance from the starting point to the finishing point, in the direction from start to finish; it is a vector." Add acceptable alternatives to guidance.

5.5 | Topic 5 | ITEM-6118-5-P02 parts (c) and (e) | S2
Quoted (c): "The first has no increase in path distance. The second directly states a constant nonzero speed, so the object continues moving."
Quoted guidance (e): "One mark for the graph-area relation; one for 12 m."
Problems: (c) never links the distance-time line to its gradient being the speed (gradient zero means speed zero), which is the physics the 2-mark answer should show. "No increase in path distance" is vague. (e) The prompt does not mention a graph ("Calculate the travelled distance for that uniform speed increase"). The guidance forces the "graph-area relation" mark, so a learner using s = (u + v)t/2 = 12 m or average speed 4 m/s × 3 s would lose a mark. The answer line "The trapezium area is ½ × (1 + 7) × 3" does not state the area-equals-distance relation as the guidance expects.
Fix: (c) "Gradient of a distance-time graph is speed; a horizontal line has gradient zero so speed is zero (at rest). A horizontal speed-time line at 2 m/s means speed is 2 m/s, not zero." (e) accept area under graph, s = (u + v)t/2, or average speed × time.

5.6 | Topic 5 | ITEM-6118-5-P03 part (c) canonical Plan | S2
Quoted: "2. Use suitable position/timing equipment or recorded motion to estimate speed at a sequence of times." and "5. Use the speed-time trend to test whether similar speed changes occur during equal time intervals."
Problem: the prompt asks for "five operational measurement steps". Step 2 names no apparatus (ticker-timer, light gates, stopwatch plus marked distances, phone video) and does not say how speed is obtained, so a learner cannot copy a repeatable method. Step 5 is analysis, not a measurement step. The syllabus practical (ball or trolley from rest through marked distances s = 10, 20, 30 cm, v = 2s/t from average speed = s/t = (u + v)/2) is not used. A model vehicle starting at 0.1 m/s is not "from rest", so v = 2s/t cannot be used with this data either.
Fix: rewrite the plan with named equipment and the calculation of speed from distance and time, and make every step an action. Mark scheme for "five specific operational steps" must list them.

5.7 | Topic 5 | ITEM-6118-5-P03 marking_guidance | S2 (same pattern in 6.5, 7.4, 8.7)
Quoted: "Method: award one mark for each of the five specific operational steps (5)." ... "Controls and safety support the method; the planning allocation totals eight marks."
Problem: the prompt asks for "arrangement, five operational measurement steps, controls, a table and how the data would support a conclusion", but the scheme gives 5 (method) + 1 (table) + 1 (graph) + 1 (conclusion) = 8 and awards nothing to controls or arrangement, contradicting the prompt. "Correctly signed calculation (1)" and "axis-ratio unit (1)" are template phrases (the gradient 0.2 m/s² is positive; "axis-ratio" is unexplained). The canonical answer does not show the "visible wide construction" (e.g. (5, 1.1) and (0, 0.1), Δv = 1.0, Δt = 5) that earns a mark, and gives no scale. The 16-mark total does add up (5 + 3 + 8).
Fix: allocate the 8 planning marks to the items listed in the prompt and show the construction triangle in the model answer.

5.8 | Topic 5 | ITEM-6118-5-008-MECH | S3
Quoted: prompt "Explain why a trolley moving at a constant −2 m/s is not necessarily decelerating."; canonical "...so its velocity is constant and its acceleration is zero."
Problem: "not necessarily" implies it might be decelerating, but the answer says it definitely is not. It also gives away the scenario in the prompt ("constant").
Fix: "A trolley moves at a constant velocity of −2 m/s (east positive). A learner says it is decelerating because the sign is negative. Explain why this is wrong."

5.9 | Topic 5 | ITEM-6118-5-013-DIST | S3
Quoted canonical: "Equal speeds require equal magnitudes. Equal velocities require that magnitude and direction match."
Problem: it restates the definitions and does not use the stated context ("two vehicles on the same straight road"). The point worth marking is that equal speeds in opposite directions give different velocities.
Fix: canonical "Equal speed only needs the same magnitude, so vehicles travelling in opposite directions at 20 m/s have equal speeds but different velocities (+20 and −20 m/s). Equal velocity needs the same speed and the same direction."

5.10 | Topic 5 | figures figure-6118-5-01 to -04, practical-6118-5 and notes layout | S3
- figure-6118-5-04.png (cards 5-017): data are joined by straight segments, but the card requires "a smooth upward-curving trend"; the picture shows a kinked line, and its legend says "Velocity" while the notes and syllabus talk about speed-time graphs.
- figure-6118-5-02.png: the vertical axis starts at 2, so the area under the line (which the card discusses) cannot be seen from zero.
- figures 5-01 to 5-03 appear in the notes under three identical headings "Original graphical solution" with no stated data in the notes (the data are only in cards 5-010, 5-011, 5-012), so a notes reader cannot tell what they show.
- practical-6118-5.png: no gradient triangle or labelled construction is drawn although part (b) asks for one.
Checked as correct: axis labels and units ("Distance / m", "Time / s", "Speed / m s⁻¹"), plotted values, and legibility.

5.11 | Topic 5 | all flashcards, marking_guidance field | S3
Quoted examples: 5-001 "Property or unit: A reference origin and a specified positive direction are needed. (1 mark)."; 5-013 "Contrast: Equal speeds require equal magnitudes. (1 mark)."; 5-009 "Equation, substitution and final result: Average speed = total distance / total time = 48/12. (1 mark)."
Problem: the guidance is the canonical answer cut into sentences under a generic label. Labels do not fit the content: "Property or unit:" for cards that are not about a property or unit (5-001, 5-002, 5-019). It lists no acceptable alternatives, no "do not credit" and no unit/ECF rule. The calculation cards credit the final value with its unit in one line and never say that a missing unit costs the mark.
Fix: write per-card guidance with acceptable variants and the specific condition for each mark.

5.12 | Topic 5 | ITEM-6118-5-P01 weak distractors and stem wording | S3
Independent solutions agree with every key (Q1 A, Q2 D, Q3 C, Q4 B, Q5 A, Q6 D, Q7 C, Q8 B, Q9 A, Q10 D, Q11 C, Q12 B); no question has two defensible answers.
Weak distractors: Q4 A "A decreasing distance" (distance cannot decrease, nothing plausible); Q5 C "m²/s" and D "s/m"; Q6 B "That the object is at a negative position" and C "That no force acts"; Q11 B "0 m".
Q7 stem: "For the stated straight-line motion with constant acceleration" refers to nothing stated, and the keyed option is the longest and the only one containing the condition. Q1 stem "full length of a travelled path" nearly restates the definition of distance. Q2 feedback for B ("A negative path distance") is fine. Q10 correct 2 m/s² is also the smallest option, which a test-wise learner may pick.
Fix: reword Q7 ("When can v = u + at and s = ut + ½at² be used?"), replace the implausible distractors with common slips (for example Q5 "m/s", "N", Q11 "1.25 m" is good).

5.13 | Topic 5 | coverage of objectives in flashcards | S3
The objective "plot readings for and interpret a distance-time graph" and "identify ... at rest, constant speed, changing speed" are covered only by "Draw" cards. No card asks the learner to read a speed from a distance-time gradient, to read distance from a speed-time area on a given graph, or to describe a segment of a given graph. No card on average speed from a graph, and none on positive/negative velocity from a position-time gradient.
Fix: add 2 to 3 graph-reading cards.

5.14 | Topic 5 | ITEM-6118-5-017-INTERP | S3
Quoted: "Draw a velocity-time trend through readings 0, 1, 4 and 9 m/s at times 0, 1, 2 and 3 s to show increasing acceleration."
Problem: the prompt states the conclusion ("increasing acceleration"), so the learner only has to plot. Bloom "Analyse" is too high for plotting given values.
Fix: "Plot these readings and state what the shape shows about the acceleration."

5.15 | Topic 5 | notes "Practice task with worked feedback" (three of them) versus the deck | S3
The notes print the full MC set with keys and feedback, the full short answer with answers, and the full practical with worked feedback, identical to ITEM-6118-5-P01, P02 and P03. A learner who reads the notes first sees the answers to the deck's assessment items, so the deck is not independent practice.
Fix: keep the practice tasks only in the deck, or give the notes different tasks.

5.16 | Topic 5 | notes wording and scope | S3
Jargon for Grade 10 to 11 learners, not explained: "does not encode the direction" (2.3.1 distance), "A secant gradient between distant points gives an average" (not syllabus), "signed component" (several places), "nonuniform", "trapezium" (British, fine, but not defined), "idealised". Also unflagged beyond-syllabus statement: "A direction change can also be acceleration even when the speed stays the same." True, and consistent with acceleration = rate of change of velocity, but the syllabus works only in straight-line motion; it needs one sentence of context or a scope flag.
Also "Position ... In two or three dimensions, more than one coordinate is needed" is fine. Scope limits (collisions, nuclides, diverging lenses) are not breached in topic 5.

5.17 | Topic 5 | ITEM-6118-5-019-FEATURE versus ITEM-6118-7-004-FEATURE | S3
Quoted: 5-019 "State the approximate magnitude and direction of free-fall acceleration near Earth's surface when air resistance is negligible." / "Approximately 10 m/s² downward." and 7-004 "...It is 10 m/s² downward."
Problem: near duplicate across topics (7-004 also gives "10 N/kg" in the stem, which cues the 10).
Fix: keep one; make the 7-004 card ask for the link (g in N/kg equals free-fall acceleration in m/s²).

5.18 | Topic 5 | ITEM-6118-5-P03 prompt wording | S4
Quoted: "The following are invented, idealised practice readings for uniformly accelerating model vehicle." Missing article ("a"). The data are correctly labelled as invented practice data.

5.19 | Topic 5 | metadata labels | S4
5-023-MISCON is labelled AO A but requires a calculation (2.75 m/s), so AO B applies. The "Draw" cards 5-010, 5-011, 5-012 and 5-017 are plotting given values, so Bloom "Apply" fits better than "Analyse". P01 is labelled "Apply" but 8 of 12 questions are recall or one-step.

### Topic 5 verdict
Ready after fixes. Physics in notes, MC keys and calculation cards is correct. The weaknesses are a figure that contradicts card 5-021, a non-operational practical plan with a mark scheme that does not credit the elements the prompt asks for, the predictable MC key, thin equation coverage and template marking guidance.
Counts: S1 0, S2 7 (5.1 to 5.7), S3 10 (5.8 to 5.17), S4 2 (5.18, 5.19). Total 19.

---

## TOPIC 6 Forces, springs and momentum

6.1 | Topic 6 | flashcard coverage | S2
Syllabus verbs "state Hooke's law", "state that a force ... may produce a change in size, shape or velocity ... relate to Newton's first and second laws", "identify ... friction". Cards: OBJ-2.4-06 has only a calculation card (6-013). There is no card asking the learner to state Hooke's law in words (the notes do not state it as "force is proportional to extension while the limit is not exceeded" in one place either). There is no card stating Newton's first law, and no card for friction (only air resistance, 6-009). No card for the unit newton or for force changing size/shape.
Fix: add cards "State Hooke's law", "State Newton's first law", "State what friction is and its direction".

6.2 | Topic 6 | ITEM-6118-6-002-FEATURE | S2
Quoted: "State one way a resultant force can change motion besides increasing the speed." Canonical: "It can change the direction of motion." Guidance: "Property or unit: It can change the direction of motion. (1 mark)."
Problem: decreasing the speed (slowing down) is an equally correct answer to the prompt, and the notes themselves list it ("A ball slowing down ..."). The key accepts only direction change, so a correct learner is marked wrong.
Fix: canonical "It can decrease the speed, or change the direction of motion"; guidance accepts either.

6.3 | Topic 6 | ITEM-6118-6-P01 (MC set) | S2
Independent solutions agree with all keys (Q1 A, Q2 D, Q3 C, Q4 B, Q5 A, Q6 D, Q7 C, Q8 B, Q9 A, Q10 D, Q11 C, Q12 B). The key is the same A D C B cycle as topic 5 (see 5.2). Fix: shuffle.

6.4 | Topic 6 | ITEM-6118-6-P03 canonical Plan | S2
Quoted: "3. Apply a known calibrated force gently and read the loaded length after oscillations settle. 4. ... repeat the reading where appropriate."
Problem: not operational. It never says how a "known force" is produced (slotted masses on a hanger; weight = m × g from topic 7, 0.1 kg is about 1 N). It does not state the measuring range or increments, and "repeat where appropriate" is not a step. The prompt asks for five operational steps; steps 1, 2, 5 are fine but 3 and 4 are vague. The notes' measurement of x as "loaded length minus unloaded length" is correct.
Also: the model answer gives only gradient 12 mm/N and notes it is reciprocal stiffness; it never completes k = 1/12 N/mm = 83 N/m, so the learner is told k is "required" but not shown it (data are physically realistic: k about 83 N/m).
Fix: name masses and hanger, state the load increments (for example 0.1 kg steps = 1 N), and give k = 83 N/m as an extension.

6.5 | Topic 6 | ITEM-6118-6-P03 marking_guidance | S2 (same pattern as 5.7)
Controls and safety carry no marks ("Controls and safety support the method; the planning allocation totals eight marks"), yet the prompt asks for controls. "correctly signed calculation (1)" is meaningless for a positive gradient; "axis-ratio unit" is unexplained jargon. The total adds to 16 (5 + 3 + 8) only because method 5 + table 1 + graph 1 + conclusion 1 = 8.

6.6 | Topic 6 | ITEM-6118-6-003-SYNTH | S3
Quoted prompt: "Explain the link between a force agent and a force diagram for a book resting on a table." Guidance: "Combine the linked ideas and explain the reason: Earth exerts the book's weight and the table exerts its contact force. (1 mark)." and "Combine the linked ideas and explain the reason: Both arrows belong on a diagram of forces on the book because the book is the receiving body. (1 mark)."
Problem: the prompt is vague (a learner cannot tell what is being asked); the guidance is the boilerplate template with a label that does not match the answer; the two marks are two halves of one answer. "Earth exerts the book's weight" is loose (Earth exerts a gravitational force, which is the weight).
Fix: "A book rests on a table. Name the force acting on the book from each of Earth and the table, and state which direction each arrow points on a diagram of forces on the book." Marks 1 + 1 for the force and direction pairs.

6.7 | Topic 6 | ITEM-6118-6-005 to 6-010 (identify-force cards) | S3
The prompt contains the answer or nearly so: 6-005 "repulsion between two similarly charged objects" (electrical), 6-006 "a magnet attracts an iron nail" (magnetic), 6-007 "force exerted by Earth on a falling stone" (weight), 6-009 "force that resists a parachutist's downward motion relative to the air" (air resistance), 6-010 "State the force agent when a table supports a book through contact" (answer: the table). 6-010 duplicates 6-003. Only 6-008 (direction of tension) tests anything beyond naming.
Fix: ask the learner to identify the force from a situation without the answer words, or merge into one "name the force and its agent" card with three situations.

6.8 | Topic 6 | ITEM-6118-6-012-INTERP and figure-6118-6-01.png | S3
Quoted prompt: "Draw an extension-versus-load graph for forces 0, 1, 2, 3 N producing extensions 0, 4, 8, 12 mm." Guidance awards "its gradient is 4 mm/N" though the prompt asks only for the graph. The figure is correct (0, 4, 8, 12 mm at 0 to 3 N; labelled axes) but its title "Proportional extension, inverse-stiffness slope" is jargon and tells the learner the answer to the gradient interpretation. In the notes the figure is introduced as "generated from the stated practice values", but the notes state no such values (the notes' practice table is 0 to 1 N / 0 to 12 mm), so it is unexplained.
Fix: ask for the gradient in the prompt or drop it from the guidance; retitle the figure "Extension against force"; state the data in the notes.

6.9 | Topic 6 | ITEM-6118-6-018-DEF | S3
Quoted: "The total momentum of a system remains unchanged when its external resultant force is zero."
Problem: the syllabus principle is about interacting objects ("When two or more objects interact, their total momentum remains constant, provided no external resultant force acts"). The card omits "objects interact" and "constant"; a learner answer "total momentum before = total momentum after if no external force" would need explicit acceptance. The condition is correct and the card is physically right.
Fix: add "when two or more objects interact" and accept "before = after".

6.10 | Topic 6 | ITEM-6118-6-021-MISCON | S3
Quoted: "A person gives an external push to a single trolley system. Explain why one cannot simply assume its momentum stays constant during that push."
Problem: "single trolley system" is a confusing phrase for a one-body system; the principle concerns interacting bodies, so it is unclear what is being tested. The answer (external push is an external impulse) is correct.
Fix: "A person pushes a trolley. A learner says the trolley's momentum is conserved. Explain why this is wrong."

6.11 | Topic 6 | all flashcards, marking_guidance | S3
Same template guidance as 5.11: for example 6-001 "Cause and effect: The forces do not balance, so their vector sum is nonzero. (1 mark)."; 6-004 "Property or unit: Perpendicular to the contact surface. (1 mark)." (it is neither a property nor a unit); 6-022 "Identify the direction-sign error (1 mark)." (no wording given).

6.12 | Topic 6 | ITEM-6118-6-P01 distractors | S3
Weak or implausible: Q1 C "Geographically north"; Q4 A "The load multiplied by total length" and D "The original length divided by the load"; Q5 C "At the first nonzero load for every spring" and D "At zero extension only"; Q6 A "Every body has zero velocity", C "No internal interactions occur"; Q3 A "Its mass multiplied by its speed" (not a force). Q5 key A "Where the initial proportional graph trend ends" is almost a restatement of the term. Q3 stem uses "constant-mass model", which is jargon. Q2 and Q7 are good.

6.13 | Topic 6 | coverage of momentum and forces | S3
Every collision card (6-019) and every notes example has the bodies sticking together or one body at rest, and there is no card or note with a rebound or separation (the syllabus says "including elastic and inelastic collisions"; the definitions are rightly not required). The notes say "For a rebound, retain the final velocity sign" but give no worked example. 6-011 uses only two forces (syllabus: "two or more"). No MC question tests momentum conservation numerically.
Fix: add a rebound example (for example 1 kg at +3 m/s hits a 2 kg at rest, 1 kg rebounds at −1 m/s, 2 kg moves at +2 m/s) and a three-force resultant.

6.14 | Topic 6 | notes style | S3
Jargon: "vector sum", "collinear" ("simple collinear model"), "constant-mass model", "external impulse", "signed components". No figure shows a force diagram, spring experiment arrangement or momentum before/after, although every force and spring topic depends on one. Practice: only one figure (6-01) exists for the topic.

6.15 | Topic 6 | duplicates and notes-versus-deck independence | S3
The limit of proportionality is tested by 6-014, MC Q5 and P02(b) with essentially the same answer; F = ma is tested by 6-015, MC Q10, P02(e). As in 5.15, the notes reprint the deck's MC set, short answer and practical with answers.

6.16 | Topic 6 | notes wording | S4
"A simple rope can pull a load but does not push it along its length in the same way." The phrase "in the same way" is vague. Tension direction text "At the attachment it acts along the rope away from the object being pulled" is correct (force on the object points along the rope, towards the rope).

6.17 | Topic 6 | metadata labels | S4
P01 labelled Bloom "Apply" but mostly recall. 6-012 "Draw" labelled "Analyse". 6-020 "MISCON" explain labelled AO A is fine.

### Topic 6 verdict
Ready after fixes. Physics is correct throughout (all calculations check; limit-of-proportionality, equilibrium and conservation statements are right; no scope-limit breach, no collision definitions). Needs: add missing "state" cards (Hooke, Newton 1), fix 6-002 key, make the practical plan operational, fix mark scheme, shuffle MC key, tidy template guidance.
Counts: S1 0, S2 5 (6.1 to 6.5), S3 10 (6.6 to 6.15), S4 2 (6.16, 6.17). Total 17.

---

## TOPIC 7 Mass, weight and density

7.1 | Topic 7 | ITEM-6118-7-012-MECH and notes section "state that the density of water around 4 °C is a maximum ..." | S2
Quoted card: "Water cooled below about 4 °C and the resulting ice are less dense, so the ice stays at the surface. The surface layer can insulate liquid water below, leaving a habitat rather than the lake freezing from its bottom upward."
Problem: the syllabus objective is to state that water is densest at about 4 °C and to explain the advantage. The card answer never says that 4 °C water is densest, that it sinks and therefore stays at the bottom of the lake, which is why the bottom stays liquid at about 4 °C. This is the point examiners credit. The notes mention it only indirectly ("As surface water cools toward 4 °C, its increased density can make it sink and promote mixing") and never say the bottom layer stays at about 4 °C. Marking guidance repeats the answer sentences only.
Fix: canonical "Water is densest at about 4 °C, so water cooling to 4 °C sinks and the bottom of the lake stays at about 4 °C. Water below 4 °C and ice are less dense and stay at the surface, so ice forms on top and insulates the water below, allowing fish to survive."

7.2 | Topic 7 | ITEM-6118-7-P01 (MC set) | S2
Independent solutions agree with all keys (Q1 A, Q2 D, Q3 C, Q4 B, Q5 A, Q6 D, Q7 C, Q8 B, Q9 A, Q10 D, Q11 C, Q12 B). Same A D C B A D C B A D C B cycle as topics 5, 6 and 8 (see 5.2). Fix: shuffle.

7.3 | Topic 7 | ITEM-6118-7-P03 data and canonical Plan | S2
Quoted: "5. Take repeats where needed and compare the mass-volume results across the range." and "Use the same liquid at a similar temperature and the same dry container".
Problem: step 5 is not an operational measurement step, so only four real steps are given for a prompt requiring five. The liquid is never named; the data give 0.80 g/cm³ (not water; for example ethanol or paraffin), but a learner planning with water will get 1.0 g/cm³ and the answer does not say which liquid is intended. The data are stated to be "after subtracting the container mass", which removes the experiment's main difficulty (the real graph of total mass against volume has a non-zero intercept equal to the container mass); the notes do not say this. The check "the idealised trend passes through zero" cannot be seen on practical-6118-7.png (see 7.13).
Fix: name a liquid, make step 5 a real measurement step (for example "repeat each volume reading and average"), and note the intercept equals the container mass if total mass is plotted.

7.4 | Topic 7 | ITEM-6118-7-P03 marking_guidance | S2
Same as 5.7: controls carry no marks although requested; "correctly signed calculation (1)" and "axis-ratio unit (1)" are template phrases (gradient 0.8 g/cm³ is positive). Gradient construction numbers (20 g over 25 cm³) are correct and the 16-mark total adds up.

7.5 | Topic 7 | ITEM-6118-7-004-FEATURE | S3
Quoted: "State the free-fall acceleration corresponding to a downward gravitational field strength of 10 N/kg when air resistance is negligible." / "It is 10 m/s² downward."
Problem: the number 10 is in the prompt, so the card tests only a unit change. Near duplicate of 5-019 (see 5.17).
Fix: "State the value of g near Earth's surface in N/kg and the free-fall acceleration it gives in m/s²."

7.6 | Topic 7 | ITEM-6118-7-002-DEF | S3
Quoted: "Inertia is the mass-associated resistance to a change in motion."
Problem: "mass-associated" is awkward and not syllabus wording ("the property of mass which resists change in motion"). Learners may paraphrase correctly ("the reluctance of an object to change its state of motion") and the single-sentence guidance gives no alternatives.
Fix: "Inertia is the property of a body (its mass) that resists a change in its motion."

7.7 | Topic 7 | ITEM-6118-7-P01 Q6 | S3
Quoted: "6. What should be avoided in a displacement measurement? A. Reading an initial volume ... D. Trapped bubbles on the submerged object"
Problem: "displacement" is also the vector from topic 5; the stem should say "measuring the volume of an irregular solid by displacement of water". Key D is correct and no other option is defensible.

7.8 | Topic 7 | ITEM-6118-7-P01 weak distractors and cues | S3
Q2: "Density alone", "Weight alone", "Speed alone" use "alone", a cue that these are wrong; the stem restates the definition of inertia. Q3 B "The mass of Earth per object" is implausible. Q4 A "An increasing downward force" and Q5 D "Weight / time" are weak. Q7 A "100 °C" is implausible (B "At every temperature equally" also). Q1 is trivially easy. No question tests floating or sinking, or g = a.

7.9 | Topic 7 | coverage gaps | S3
No flashcard or MC item on: density of a regular solid (measure dimensions, calculate volume), sinking (denser than liquid) as well as floating, the 4 °C maximum as a "state" card, converting g/cm³ to kg/m³ (notes say 1 g/cm³ = 1000 kg/m³ but no card), weight versus mass measuring instruments (7-007 is the only card). The practical covers liquid density only.

7.10 | Topic 7 | notes wording and scope | S3
"Distinguish an object's mass from its apparent support or scale force in a changing-motion situation." (section on mass): refers to lift or accelerating-frame problems outside the syllabus and is unexplained jargon. "The two forms of unit describe different definitions of the same local gravitational effect." is confusing (N/kg versus m/s²). "A balance compares masses or infers mass from a calibrated force measurement, so its operating principle matters" is vague. "Inertia ... This is not because an additional force called inertia pushes backward" is a good correction.

7.11 | Topic 7 | ITEM-6118-7-P02 parts (a), (b), (e) | S3
(b) "State a suitable unit for density when mass is in grams and volume in cubic centimetres." is answered by the prompt wording (g/cm³). (a) is a one-mark recall duplicating MC Q1. (e) answer "W = mg = 18 N" shows no substitution although guidance says "multiplying by g". The marks add to 8 (1 + 1 + 2 + 2 + 2).

7.12 | Topic 7 | all flashcards, marking_guidance | S3
Same template guidance as 5.11, for example 7-009 "Method step: Subtract the empty-container mass from the combined container-plus-liquid mass. (1 mark)." For 7-010 the prompt includes the conditions ("sinks and does not absorb the liquid"), so the card cues the method and cannot show that the learner knows when displacement works.

7.13 | Topic 7 | figures and notes diagrams | S3
practical-6118-7.png: both axes start above zero (x from 4, y from 4), so "the idealised trend passes through zero" cannot be seen and the learner cannot check a through-origin line. Title is long, but legible. Plotted points are correct (5/4 ... 30/24). The notes have no diagram of the displacement method, density bottle/measuring cylinder, or floating.

7.14 | Topic 7 | notes versus deck independence | S3
As 5.15: the notes reprint P01, P02 and P03 in full with answers.

7.15 | Topic 7 | ITEM-6118-7-001-DEF | S4
Quoted canonical "Mass is a measure of the matter in an object." Identical to the syllabus wording and to the 2020 Paper 3 mark scheme Q5(a) ("Is a measure of the matter in an object"), a 7-word run. It is a standard textbook definition, so risk is low.

7.16 | Topic 7 | minor items | S4
7-011 "float partly immersed in water": an object of equal density floats fully immersed, so the "partly" qualifier is not needed for the density comparison. The 7-005 explanation is correct. Cooling and ice statements in the notes are correct.

### Topic 7 verdict
Ready after fixes. Physics is correct: W = mg, g = W/m, terminal velocity, density, displacement method, 1 g/cm³ = 1000 kg/m³ all check. The main defects are the incomplete aquatic-life answer (the syllabus's only "explain" objective in the topic), the predictable key, an under-specified practical and gaps in coverage of floating, sinking and regular solids.
Counts: S1 0, S2 4 (7.1 to 7.4), S3 10 (7.5 to 7.14), S4 2 (7.15, 7.16). Total 16.

---

## TOPIC 8 Moments, equilibrium, stability and friction

8.1 | Topic 8 | ITEM-6118-8-P03 canonical answer, "Gradient"; also notes "Practice task" worked feedback | S1
Quoted: "Gradient: 0.125 ÷ 0.25 = 0.5 N m. The gradient of effort against reciprocal arm is the fixed opposing moment, because F = M/d."
Data (prompt): effort distance d (m) horizontal, reciprocal effort 1/F (N⁻¹) vertical: (0.05, 0.025) ... (0.30, 0.15).
Working: 1/F = d/M, so the gradient of 1/F against d is 1/M. Every point gives 1/F ÷ d = 0.5, so the gradient is 0.5 N⁻¹ m⁻¹ and the fixed moment is M = 1/0.5 = 2.0 N m (check: F = 40 N at 0.05 m, 6.67 N at 0.30 m, F × d = 2.0 N m each). The answer's value 0.5 is right but its unit "N m" is wrong (it is N⁻¹ m⁻¹), and the claim that the gradient equals the opposing moment is wrong by a reciprocal: the opposing moment is 2.0 N m, not 0.5 N m. The sentence "gradient of effort against reciprocal arm" describes a different graph from the one asked. The work file practical-parameters.json gives "expected_gradient": 0.5 with the unit rule "vertical unit divided by horizontal unit", which is N⁻¹ m⁻¹, so the canonical answer contradicts its own source file. A learner who follows this answer learns a wrong physical meaning and a wrong unit.
Fix: "Gradient = Δ(1/F)/Δd = (0.15 − 0.025)/(0.30 − 0.05) = 0.50 N⁻¹ m⁻¹ (per newton metre). Gradient = 1/M, so M = 1/0.50 = 2.0 N m."

8.2 | Topic 8 | ITEM-6118-8-P03 canonical answer, "Graph" | S1
Quoted: "Graph: Plot balancing effort vertically against reciprocal effort arm horizontally; the straight trend is expected for a fixed opposing moment."
Problem: the prompt asks for "Reciprocal effort / N⁻¹ on the vertical axis and Effort distance / m on the horizontal axis". The model answer describes a different graph (effort F vertical against 1/d horizontal) and a different quantity ("reciprocal effort arm"). If a learner plots that, the points and gradient (which would be M = 2.0 N m) differ from the question. The model answer and the question contradict each other. The figure practical-6118-8.png follows the prompt, so the figure and the written model answer also disagree. The notes' practice feedback repeats the same sentence.
Fix: rewrite to match the prompt, or change the prompt to the simpler and more usual F against 1/d, whose gradient is M = 2.0 N m.

8.3 | Topic 8 | notes "Practice task" worked feedback, Table; ITEM-6118-8-P03 Table | S2
Quoted: "Table: Record effort arm / m, reciprocal arm / m⁻¹ and balancing effort / N."
Problem: the data table in the prompt uses effort distance and reciprocal effort (N⁻¹), but the model table records reciprocal arm (m⁻¹), a different column set that does not lead to the graph asked for, with no 1/F column. Together with 8.2 the whole model answer for this task is internally inconsistent.
Fix: table columns "effort arm d / m, effort F / N, 1/F / N⁻¹" (and optionally F × d / N m as a check).

8.4 | Topic 8 | ITEM-6118-8-P03 data realism and experimental design | S2
Data imply F = 40 N at d = 0.05 m falling to 6.7 N at d = 0.30 m (fixed moment 2.0 N m). A school metre rule or beam balance cannot carry a 40 N (4 kg) effort at 5 cm without damage or tipping, and the notes' own experiment uses "known weights". Plotting 1/F against d is unusual at this level (the syllabus verification is moments equal, with F against 1/d or F × d constant). The plan also asks the learner to "Choose an effort position ... Adjust the effort force until the beam is horizontal and stationary": forces from slotted masses are discrete, so the usual method is to choose the force and move the mass until the beam balances (the arm is then the continuous variable). The plan says "Repeat for a range of effort arms, keeping the opposing moment fixed" but does not name the load and arm that give 2.0 N m (for example 10 N at 0.20 m).
Fix: use realistic values (for example fixed load 2.0 N at 0.20 m, so M = 0.40 N m, efforts 0.5 N to 4 N) and plot F against 1/d.

8.5 | Topic 8 | notes section "state that, when there is no resultant force and no resultant turning effect, a system is in equilibrium", and MC Q4 feedback | S2
Quoted notes: "Two equal opposite forces whose lines do not coincide have zero resultant force but can produce a turning effect." Quoted MC feedback Q4 C: "A couple can still turn the body."
Problem: this is a couple, a concept not in the 2018 syllabus. It is true and brief, but it is not flagged as extra and the word "couple" is introduced without explanation.
Fix: remove the term "couple" or flag the sentence as optional extension.

8.6 | Topic 8 | ITEM-6118-8-P01 (MC set) | S2
Independent solutions agree with all keys (Q1 A, Q2 D, Q3 C, Q4 B, Q5 A, Q6 D, Q7 C, Q8 B, Q9 A, Q10 D, Q11 C, Q12 B); numerics Q8 1.2 N m, Q9 6 N, Q11 8 N correct. Same A D C B cycle as topics 5, 6 and 7 (see 5.2). Fix: shuffle.

8.7 | Topic 8 | ITEM-6118-8-P03 marking_guidance | S2
Same as 5.7: controls and safety carry no marks although the prompt requires "controls"; "correctly signed calculation (1)" and "axis-ratio unit (1)" are template phrases. Here "axis-ratio unit" is where the model answer goes wrong (8.1): the mark scheme would credit the unit "N m" because the canonical answer says so. The 16 marks add up (5 + 3 + 8).

8.8 | Topic 8 | ITEM-6118-8-006-PROC, 8-008-PROC | S3
8-006 "Describe a beam experiment that tests the balance of moments." is worth 1 mark but the canonical answer omits the beam being horizontal, measuring distances from the pivot, and repeating. 8-008 "Describe how to locate a thin irregular card's centre of mass using suspension." omits hanging the plumb line from the same pin. Both are multi-step descriptions marked as one point.
Fix: raise to 2 marks or state the single idea being tested.

8.9 | Topic 8 | coverage gaps | S3
No card for: moment is a vector and work is a scalar (only MC Q2); everyday lever examples (pliers, tweezers, tongs, crowbar); how to reduce friction (8-011 mentions lubrication only inside an answer); friction depends on the surfaces; base width and stability (only lowering the load, 8-009); the load, effort and fulcrum of a spanner or scissors (only the wheelbarrow, 8-003).

8.10 | Topic 8 | ITEM-6118-8-P01 weak distractors | S3
Q1 D "A change of force unit alone" and C "A force line through the pivot" (obviously zero); Q6 A, B, C are all opposites of D; Q7 A, B, D are three low-friction cases, so "which needs friction" is answered by finding the odd one out; Q10 A "The force value in N m" and C "Its weight" are weak; Q11 A "15 N" (product) is not a plausible slip; Q12 A, C, D are all formula-mangling options.

8.11 | Topic 8 | ITEM-6118-8-P01 Q2 | S3
"Which quantity is a scalar? ... B. Moment ... D. Work". The key (Work) is correct under the syllabus statement "moment is a vector, work is a scalar", but many learners meet moment as a scalar with a clockwise/anticlockwise sense. The set offers a second plausible answer to anyone who learned otherwise. A safer stem: "Which quantity has no direction?" with distractors force, velocity, momentum.

8.12 | Topic 8 | ITEM-6118-8-012-MISCON and notes "Distinguishing the ideas" | S3
Quoted: "A 10 N force holds a bar stationary 0.50 m from its pivot." A single 10 N force about a pivot gives a 5 N m moment, so the bar can be stationary only if another force (a load or its weight) supplies an equal opposite moment. The conclusion (the work done by the held force is zero) is correct, but the prompt should say "against a load".

8.13 | Topic 8 | all flashcards, marking_guidance | S3
Same template as 5.11. Mislabels: 8-011 "Contrast: Tyre-road friction provides grip ... (1 mark)." (the card asks for one useful and one unwanted effect, not a contrast); 8-012 "Identify the error and give the correct distinction: ..." duplicates the answer; 8-003 and 8-005 "Property or unit: ...".

8.14 | Topic 8 | ITEM-6118-8-P02 part (b) | S3
Canonical "The resultant moment is zero." Guidance "One mark for zero net turning effect." Neither accepts the usual NSSCO statement "clockwise moments equal anticlockwise moments" (the principle of moments); the notes also use that form. Add it as acceptable. Parts (a) to (e) calculations are correct and marks sum to 8.

8.15 | Topic 8 | notes diagrams | S3
The notes have no figure other than the (incorrectly explained) practical graph. A topic on moments, beam experiments, plumb-line lamina and stability needs at least a lever diagram with load, effort, fulcrum and perpendicular distances, the beam experiment set-up and the lamina method.

8.16 | Topic 8 | figure practical-6118-8.png | S3
Plotted points and labels are correct for the prompt (d horizontal, 1/F vertical, "Reciprocal effort / N⁻¹"). Both axes start above zero (x from 0.04, y from 0.02), so the through-origin behaviour implied by "idealised" cannot be seen. No gradient triangle is drawn.

8.17 | Topic 8 | notes versus deck independence | S3
As 5.15: the notes reprint P01, P02 and P03 with answers (including the wrong practical feedback in 8.1 and 8.2).

8.18 | Topic 8 | ITEM-6118-8-010-MECH | S4
"Static friction opposes that tendency": the term "static friction" is not used in the syllabus or the notes (notes say "force needed to start motion"). Explain it or reword.

### Topic 8 verdict
Not ready. The practical task P03 (and the matching notes feedback) has a wrong gradient unit, a wrong physical interpretation of the gradient (0.5 N m instead of 1/M = 2.0 N m) and a model answer that describes a different graph from the one asked, so the highest-mark item in the topic teaches an error. The rest of the topic (moment calculations, equilibrium, lamina method, stability, friction) is physically correct and can be released after the template-guidance and MC-key fixes.
Counts: S1 2 (8.1, 8.2), S2 5 (8.3 to 8.7), S3 10 (8.8 to 8.17), S4 1 (8.18). Total 18.

---

## Counts by severity

| Topic | S1 | S2 | S3 | S4 | Total |
|---|---:|---:|---:|---:|---:|
| 5 | 0 | 7 | 10 | 2 | 19 |
| 6 | 0 | 5 | 10 | 2 | 17 |
| 7 | 0 | 4 | 10 | 2 | 16 |
| 8 | 2 | 5 | 10 | 1 | 18 |
| Total | 2 | 21 | 40 | 7 | 70 |

## What was checked

- Every line of the four notes files (all worked numbers, definitions, units, scope limits) and every referenced figure (figure-6118-5-01 to -04, figure-6118-6-01, practical-6118-5 to -8), viewed as images.
- All 23 + 22 + 13 + 12 flashcards, the four MC sets (48 questions solved independently, then compared with keys), the four short_answer items and the four practical_task items. Mark totals: each short_answer sums to 8 (1 + 1 + 2 + 2 + 2); each practical sums to 16 (5 + 3 + 8) with the caveat in 5.7.
- Verbatim copying: 8-word shingles from notes and all deck text compared with the 2018 syllabus text and 24 PDFs in Question Banks. The only run matching papers or reports is the 7-word definition of mass (7.15) and the syllabus principle of conservation of momentum used as a notes heading; the many matches to the syllabus are the objective headings, which are expected.
- Practical data in work/nam-6118-nssco-2026/topics/8/assets/practical-parameters.json, which confirms the 8.1 unit rule.
- Answer-position pattern across all decks (A D C B repeated in every MC set with a key).

## What was not checked or could not be checked

- Whether claim_ids and objective_ids mapping in the JSON is complete in every case (spot-read only; not audited item by item against claims files).
- Scanned past papers or reports without a text layer (pdftotext only), so the copying check cannot cover image-only pages; the examiner-report misconception wording was not re-audited beyond the misconceptions.json entries MIS-01 to MIS-08 that touch these topics.
- The reproduction of the notes in the published website or app (only the markdown and PNG files were reviewed).
- Namibian past-paper marking practice for planning questions: assessment-evidence/GAPS.md states that marking evidence is partial, so my judgement of how marks would be awarded is from the syllabus and general NSSCO practice, not from a confirmed mark scheme.
- Figures for topics 5 to 8 other than those listed: no other figure files exist for these topics (flashcards/assets duplicates notes/assets; figure 5-03 confirmed identical by cmp, others not byte-compared).
