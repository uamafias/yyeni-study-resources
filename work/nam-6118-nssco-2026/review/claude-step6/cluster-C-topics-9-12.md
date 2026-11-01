# Cluster C review: NSSCO Physics 6118, topics 9, 10, 11, 12

Reviewer: independent physics review (REVIEW ONLY, no repository file changed).
Package: /Users/yyeniai/yyeni-study-resources/publish/nam-6118-nssco-2026/
Counting convention: a finding that applies to several topics is written once as "X" (cross-topic) and is counted in each topic it lists. Notes MC sets and flashcard MC sets are character-identical (verified in code), so each MC finding applies to both.

All numerics recomputed with python: every worked example, every MC question (all 48), every calculation card, every short-answer and practical gradient is arithmetically correct (details at the end). No keyed MC answer is wrong. No run of 7+ identical words was found between the four notes files / four flashcard files and the 24 NSSCO past papers / examiner reports (only hit: the syllabus objective "from the definitions of pressure and density", which is the syllabus heading itself, acceptable). The invented practice data are labelled "invented, idealised practice readings" in all four P03 prompts (good).

---------------------------------------------------------------------
## A. CROSS-TOPIC FINDINGS
---------------------------------------------------------------------

X1. Topics 9, 10, 11, 12. Location: every `*-P01` multiple_choice_set (notes "Practice task", Q1-Q12). Severity S3.
Quoted: keys are `A, D, C, B, A, D, C, B, A, D, C, B` in all four sets (verified by regex over the canonical answers).
Problem: a perfectly repeating 4-cycle (3 of each letter). A learner who spots Q1-Q4 can predict Q5-Q12; no randomisation. 
Fix: re-shuffle option order so keys are not cyclic (e.g. 9: C,A,D,B,B,C,A,D,D,B,A,C style, with no repeat pattern).

X2. Topics 9, 10, 11, 12. Location: `marking_guidance` of nearly all single flashcards. Severity S3.
Quoted examples: 9-002 "Property or unit: A chemical energy store. (1 mark)."; 9-019 "Method step: The cells convert incident radiation to electrical output that supplies the lamp."; 10-002 "Equation, substitution and final result: The transfer is 20 J. (1 mark)."; 11-010 "Method step: Measure the vertical liquid-level difference ...(1 mark)."; 12-001 "Combine the linked ideas and explain the reason: Combine the links: ...".
Problem: guidance is the canonical answer split into sentences with a template prefix. "Property or unit:" is attached to cards that are neither (9-003, 9-004, 9-005, 9-006, 9-007, 11-005, 11-009, 11-012, 12-023); "Method step:" is attached to Describe cards (not methods); "Equation, substitution and final result" is quoted twice for one calculation and gives no unit mark, no "accept" alternatives, no ECF, no "do not accept". Guidance therefore cannot tell a marker what equivalent wording (e.g. "molecules hit the walls and exert a force") earns credit.
Fix: write real mark points with accept/reject phrases; for calculations: 1 mark equation/substitution, 1 mark answer with unit (state that a missing unit loses the mark).

X3. Topics 9, 10, 12. Location: canonical_answer of SYNTH cards: 9-001, 9-008, 9-013, 9-018; 10-003, 10-007, 10-014; 12-001, 12-007, 12-013. Severity S3.
Quoted: 9-001 "Combine the pathways: a photovoltaic panel converts ..."; 9-008 "Link sunlight to the use: ..."; 10-003 "Combine the stores: the deformed spring ..."; 12-007 "Combine the ideas: compression ...".
Problem: the authoring instruction leaked into the model answer a learner reads; it is not part of a physics answer.
Fix: delete the instruction prefix; begin with the physics.

X4. Topics 9, 10, 11, 12. Location: every `*-P03` practical_task, part (c) [8] and marking_guidance. Severity S2.
Quoted: prompt "Include the arrangement, five operational measurement steps, controls, a table and how the data would support a conclusion. [8]"; guidance "Method: award one mark for each of the five specific operational steps (5). Results table ... (1). Graph: an appropriate relationship plotted with named axes (1). Conclusion ... (1). Controls and safety support the method; the planning allocation totals eight marks."
Problem: the prompt demands arrangement and controls but the scheme gives them 0 marks (5+1+1+1 = 8). A "graph named axes" mark sits inside the planning part although part (a) already marks graph axes. The "five operational measurement steps" in the canonical plans are not all measurement steps: 9 step 5 ("Repeat ... stopping before unsafe temperatures"), 10 step 5 ("compare work-time trends, keeping clear of suspended loads" is a safety remark), 11 step 5 ("check for a zero shift"), 12 step 5 ("Repeat on cooling"). A learner who writes a good arrangement diagram and controls but only 3 steps cannot be credited consistently.
Fix: re-allocate, e.g. arrangement 1, measurements/steps 3, controls/safety 2, table 1, conclusion 1; remove the duplicate graph mark; or drop "controls/arrangement" from the prompt.

X5. Topics 9, 10, 11, 12. Location: P03 data tables and figure files practical-6118-9/10/11/12.png. Severity S3.
Quoted: data are exactly linear (9: +1.6 per 2 min; 10: +6 per 2 s; 11: +200 per 0.02 m; 12: +3 per 5 °C).
Problem: zero scatter, so "Add a suitable fitted line", "accurate points (2)" and "approximately constant gradient" practise nothing about best-fit judgement, anomalies or uncertainty; the plotted figure joins the points with straight segments (it looks like a ruled line, which hides the required student decision). The syllabus AO C expects realistic readings.
Fix: add small realistic scatter (e.g. one point 0.2 °C off) in the table and in the model graph, and draw the line of best fit separately from the points.

X6. Topics 9, 10, 11, 12. Location: MC distractor quality (detail per topic below). Severity S3.
Problem: many distractors are absurd or contradicted by the stem, so the item discriminates little and is partly answerable by elimination: 9 Q1 D "Atoms vanish without products", Q9 D "Having no water", Q4 D "Hydroelectric flow"; 10 Q5 C "Creating input energy", Q6 B "Gravity vanishes"/C "Mass becomes zero"; 11 Q5 C "It becomes density", D "fixed by container shape", Q6 C "Impossible to compare directions"; 12 Q2 C "Disappear and reappear", Q9 D "The gas becomes a solid immediately", Q12 A "Water created from nothing", D "A new gas from frozen glass", Q8 D "Volume expands freely" (contradicts "rigid" in the stem). Also several keys are the longest or most specific option (9 Q6 D "Increased water internal energy", 9 Q8 B).
Fix: replace by genuine misconceptions from curriculum/misconceptions.json (see per-topic notes).

X7. Topics 9, 10, 11, 12. Location: every `*-P02` short_answer. Severity S3.
Problem: sub-parts are duplicates of single flashcards, so P02 adds no new demand and reuses the same answer: 9 (a)=9-007, (b)=9-006/9-019, (c)=9-015, (d)=MC Q12; 10 (a)=10-012, (d)=10-008, (e)=10-021; 11 (a)=11-001 context, (c)=11-004, (d)=11-008, (e)=11-002; 12 (a)=12-023, (c)=12-019, (d)=12-020/12-001, (e)=12-022. Part (a)/(b) items are also cued by the question (12 (b) "which phase has widely separated particles" -> gas; 12 (a) "name for irregular motion of suspended particles").
Fix: make P02 a connected scenario with new numbers and one new idea per part.

X8. Topics 10, 11. Location: all CALC cards (10-002, -008, -009, -011, -019, -021; 11-002, -007, -008, -011). Severity S4.
Problem: each splits "equation + substitution" (1) and "final result" (1) with the unit hidden in the second sentence; no mark scheme line for unit or significant figures. 
Fix: see X2.

X9. Topics 9, 10, 11, 12. Location: label fields. Severity S4.
Quoted: P01 `blooms_level` "Apply", `command_word` None; P02 `command_word` "State" for an 8-mark mixed task; P03 `assessment_objectives` ["C"] only although part (b) (gradient) is AO B (B3 manipulate data) and part (a) is B2.
Fix: set P02 command word to "State, explain, calculate"; tag P03 as B/C.

---------------------------------------------------------------------
## B. TOPIC 9: Energy sources and renewable systems
---------------------------------------------------------------------

9.1 [S1] Notes, "Explain renewable heating and greenhouses". Quoted: "A greenhouse admits radiation that warms surfaces; its enclosure reduces loss by moving warm air away."
Wrong: the enclosure reduces heat loss by stopping warm air leaving (it suppresses convection and loss by draughts); "moving warm air away" is the opposite of the mechanism and would teach a misconception. The note also omits the standard NSSCO explanation: glass lets visible/short-wave solar radiation in; the warmed ground and plants re-emit longer-wavelength infrared that glass does not let out, so the interior warms. (Introductory only; no climate-change greenhouse effect needed.)
Correct version: "Glass or plastic lets sunlight in. The warmed surfaces emit infrared that the cover largely blocks, and the enclosure stops warm air escaping by convection, so the inside stays warmer than outside. Vents let hot air out to prevent overheating."

9.2 [S2] Coverage, objective OBJ-6118-2.10.2-01-M02 "heating and greenhouses". No flashcard, MC question, or P02 part concerns greenhouses (9-015 is about the solar water-heater tank only). A syllabus objective ("greenhouses") is therefore never practised, and 9.1 is not caught.
Fix: add a 2-mark card, e.g. "Explain why a greenhouse stays warmer than the air outside on a sunny day."

9.3 [S2] Notes "discuss radioactive isotopes as the source of nuclear energy..." and card 9-012. Quoted note: "Nuclear fuel can release energy through controlled fission, heating a working fluid." Quoted card: "Explain how energy released in a fission reactor reaches a generator's electrical output."
Problem: the objective is "discuss radioactive isotopes as the source ... and the problems associated" yet (i) the notes never say the fuel is a radioactive isotope (e.g. uranium-235; naming the element is not a nuclide formula and is permitted), and (ii) no card covers the problems (waste, radiation hazard, accident risk, cost/decommissioning); only MC Q7 touches waste, and the notes' own list ("Heat removal, containment...") has no card. Card 9-012 answers only the conversion chain.
Fix: add one card "State two problems of using nuclear fission to generate electricity" and a sentence naming radioactive isotopes of uranium/plutonium as the fuel.

9.4 [S2] Out-of-syllabus content tested. Notes 2.10.2 "A small system may include a controller, storage battery and inverter where AC is required"; MC Q5 "Which device converts suitable DC output to AC for a load? A. Inverter" (key A).
Problem: syllabus 2.10.2 asks only for a "basic solar PV system ... stating the energy changes". Inverter/controller/DC-AC are not syllabus content and are not flagged as extension; one of 12 MC marks (8%) assesses it. Q5 is also answerable only by someone who has met an inverter.
Fix: either mark as "extra, not examined" in the notes and drop Q5, or replace Q5 with an energy-change question (e.g. "In a solar water heater, what is the main energy change? radiation -> internal (thermal) energy of water").

9.5 [S2] Cards 9-019, 9-020, 9-021 (and 9-018). Quoted: 9-021 "Moving air turns a rotor, which drives a generator to supply electrical output."; 9-019 "The cells convert incident radiation to electrical output that supplies the lamp."
Problem: the syllabus objective is "stating the energy changes involved". 9-021 names no energy forms (should be kinetic energy of wind -> rotational kinetic energy of rotor/generator -> electrical energy); 9-019 does not say radiant (light) energy -> electrical energy -> light/heat in lamp; 9-020 omits that radiation is absorbed as thermal/internal energy. A learner reproducing the answer would lose marks in the real exam for "energy changes".
Fix: restate each as "X energy -> Y energy" chains and award the mark for the named forms.

9.6 [S3] Notes 2.10.2 "Explain renewable refrigeration and air-conditioning". Quoted: "an appropriately designed thermal absorption system can instead use heat input." Absorption refrigeration is beyond NSSCO and unflagged. Also air-conditioning has no card or MC at all (only refrigerator 9-017). Fix: delete the absorption sentence or flag as extension; add an air-conditioner card or remove it from the claim.

9.7 [S3] Notes 2.10.1 "Outline chemical and fuel energy". Quoted: "biomass can be renewable when regrowth replaces consumption." Biomass is not among the syllabus sources (chemical/fuel list names coal, oil, gas; renewables "such as solar, hydroelectricity, geothermal and wind"). Not flagged as outside the list. Fix: flag "extra" or remove.

9.8 [S3] MC Q12 and P02(d): "Water rises from 22 to 30 °C in 4 min. What is its average heating rate?" / "Calculate the average heating rate when water warms by 9 °C in 6 min". "Heating rate in °C/min" is not an NSSCO quantity (the syllabus uses power in W, and thermal capacity in 3.2.2); these questions assess a simple division with no energy-source concept, and the notes' own text warns "temperature rise per time measures a heating rate rather than efficiency". Q12 distractors A "32" (8 x 4), C "7.5" (30/4) and D "8" (the rise, not divided) are plausible slips. Result 2 °C/min is correct (8/4). Fix: ask for a gradient/rate in a context with a unit explained, or ask power = E/t for a collector.

9.9 [S3] MC Q3. Quoted: "Which fuel is finite in the syllabus classification? A. Wind B. Tidal flow C. Nuclear fuel D. Sunlight". Three options are not fuels (wind, tidal flow, sunlight), so "fuel" in the stem is inconsistent; the question reduces to spotting the only fuel. Keyed C is correct. Fix: "Which energy source is finite? A wind B tidal C uranium/nuclear fuel D sunlight" and add coal/oil as distractors only if the key were renewable.

9.10 [S3] MC Q10. Quoted: "A PV refrigerator is operating. Where is energy rejected? ... D. To the surroundings through the hot side". "Hot side" of a refrigerator is never introduced in the notes or syllabus; learners are left to guess. D is correct (heat from the contents plus electrical input leaves to the surroundings). Fix: "Where does the thermal energy removed from the food end up? A destroyed ... D in the surroundings (warmer room)".

9.11 [S3] Card 9-010. Quoted: "Explain one environmental difference between coal generation and wind generation." Canonical mark 2: "Wind generation avoids that combustion during operation, although its construction and land use still have impacts." Mark 1 is the coal fact; mark 2 is a "contrast" that bundles a caveat. A learner who states "coal produces CO2, wind produces none while operating" has both marks but the scheme awards 1 for the caveat. Prompt says "one difference" but the guidance wants two ideas. Fix: mark 1 coal releases CO2/pollutants; mark 2 wind releases none while operating (caveat optional).

9.12 [S3] Card 9-015. Quoted canonical mark 1: "The water has gained internal energy by absorbing solar input." This does not explain why the tank is insulated; it restates that heating occurred. Only mark 2 answers. Fix: "The hot water is warmer than the surroundings so energy would flow out; insulation slows this."

9.13 [S3] Near duplicates. 9-001 (PV vs wind electricity pathways) vs 9-018 (outputs of PV, solar heating, wind) vs 9-006 (PV output vs solar water heater) vs 9-019/9-021 vs P02(b). Same answer reused 4-5 times. Fix: keep 9-018 only and vary the others.

9.14 [S3] Card 9-004. Quoted: "State where geothermal energy originates." Answer "Earth's internal thermal energy." Circular (geothermal = Earth heat). Fix: "Hot rocks deep inside the Earth (heat from the Earth's interior)".

9.15 [S3] Objective "appreciate Namibia's solar energy potential" has no card; the notes only say "Solar resources offer strong opportunities in Namibia, but actual output depends on location..." and deliberately omit the syllabus ranking (acceptable and sourced to syllabus). Fix: add a short card on why Namibia suits solar (many sunshine hours, high irradiance, sparsely populated areas needing off-grid power).

9.16 [S4] Figure notes/assets/practical-6118-9.png. Axes "Time / min", "Water temperature / °C" correct; points match table (21...29); gradient 0.8 consistent. Defect: the title "Original practice: Model solar water heater over a short interval with steady illumination" is clipped at the right edge ("illumination" touches the border). Also points are joined as a line (see X5).

Also: X1, X2, X3, X4, X5, X6, X7, X9 apply to topic 9.
Specific MC distractor weakness: Q1 D, Q2 (cued by "hot rocks beneath Earth's surface" = geothermal), Q4 (A/D weak; stem asks about the Sun, key "Fusion" obvious), Q9 B/C/D absurd, Q11 A "Its output cannot vary" trivially false.

Checks passed (topic 9): arithmetic 8/4=2, 9/6=1.5, 10-minute gradient 8/10=0.8 (data 1.6 per 2 min), distractor numbers (32, 7.5, 8) as described; P02 marks 1+1+2+2+2=8; P03 marks 5+3+8=16, guidance sums 5, 3, 8; statements on fission/fusion, renewable vs finite classification (nuclear = non-renewable as syllabus), hydro, wind, geothermal, PV vs solar thermal are correct and in scope; no nuclide formulae; fusion in Sun stated.

---------------------------------------------------------------------
## C. TOPIC 10: Energy, work, efficiency and power
---------------------------------------------------------------------

10.1 [S2] Objective 2.10.3 "give examples of energy in different forms, its conversion and conservation". The notes never list the forms (chemical, thermal/internal, light, sound, electrical, nuclear, kinetic, gravitational/elastic potential) or give everyday conversion chains (e.g. torch, car engine, hydro dam); only the pendulum is treated. The only card for this objective (10-001) is the pendulum; no MC covers it except Q6. Fix: add a note paragraph with a forms list and 3 conversion chains, and a card "State the energy changes when a battery lights a torch bulb".

10.2 [S2] Objective 2.10.4 "identify examples of levers, gears and pulleys". Notes give no real examples (wheelbarrow, scissors, spanner, crowbar; bicycle gears; flagpole/crane pulley), and cards 10-015/016/017 are all idealised statements. "Identify examples" cannot be practised. Fix: add examples to the notes and a card "Name two everyday levers".

10.3 [S3] Notes "Use kinetic energy Ek = ½mv²". Quoted: "A negative speed squared does not imply negative energy; kinetic energy uses speed rather than signed velocity." Speed is never negative, and "negative speed" appears in no NSSCO context. Confusing for Grade 10. Fix: "Speed squared is never negative, so kinetic energy is never negative; the direction of motion does not matter."

10.4 [S3] Card 10-015. Prompt: "Describe how an ideal lever reduces effort while conserving work." Canonical: "A longer effort arm reduces the force but makes its point move farther for the same load movement." The prompt asks for the conservation of work but the answer never states that work in = work out (effort x effort distance = load x load distance). Fix: add "so effort x distance moved by effort equals load x distance moved by load".

10.5 [S3] Card 10-014 canonical: "In an ideal machine their product gives the same input work as the useful output work." "Their product" has no clear referent (effort and distance? ambiguous). Fix: "effort x effort distance = load x load distance, so input work = output work".

10.6 [S3] Card 10-013 prompt "State the relation between the joule and newton metre for work." answer "1 J = 1 N m". The prompt contains both units, so the answer is just restating; near-duplicate of 10-012 (unit of work/energy). Fix: "State the unit of work in terms of newton and metre" or "A force of 1 N moves 1 m in its direction. State the work done" -> 1 J.

10.7 [S3] Near duplicates: 10-003 (stretched spring launches trolley) vs 10-006 (compressed spring produces motion); 10-008 vs P02(d) vs MC Q9 (mgh); 10-021 vs P02(e) vs MC Q12 (P = E/t); 10-010 vs notes definition. Fix: vary.

10.8 [S3] P03 realism. Data: gravitational energy gained 0, 6, 12, 18, 24, 30 J at 0..10 s (3 J/s). With bench-scale apparatus (ruler scale, low-voltage motor, manageable mass) 30 J needs mgh = 30, e.g. 3 kg lifted 1 m, or 1 kg lifted 3 m, in 10 s: not realistic for the stated plan ("manageable fixed mass", "low-voltage motor"). Gradient is correctly 30/10 = 3 J/s = 3 W; but a learner who tries the plan will get ~0.1-1 J. Fix: use a lifting arrangement with larger scale (e.g. stairs/step-up exercise as in the syllabus practical "power of leg muscles") or scale the data to 0..3 J.

10.9 [S4] Card 10-007 "Explain when mgh may be equated to ½mv² for a falling object." Canonical states "release from rest" and negligible resistance: correct; but the expression equates a change in gravitational energy with the kinetic energy gained, and the prompt does not say "change in"; minor.

10.10 [S4] Notes "Explain the action of gears". Quoted: "Each tooth engages corresponding motion at the contact." Meaningless phrase. Fix: "Teeth of the two gears mesh, so equal lengths of rim move past the contact point."

10.11 [S4] Plan step 3 in P03 uses elapsed times but no timing device is named in the apparatus (step 3 "Lift with a low-voltage motor..." then step 4 "Record height gained at several elapsed times" with no stopwatch). Also see X4 (step 5 is safety).

Checks passed (topic 10): 7x3=21 J; 3x1.2x10=36 J; 0.5x4x9=18 J; 48/12=4 m; 1 N x 0.01 m = 0.01 J; 250 J x 70% = 175 J, 75 J left; 360/12=30 W; 3x10x2=60 J, 60/5=12 W; P03 gradient 30/10=3 J/s. MC: Q1 A; Q2 D; Q3 C; Q4 B; Q5 A; Q6 D; Q7 C (small external drives larger: slower, opposite: correct); Q8 B (9 J; distractors 6, 3, 18 as described); Q9 A (20 J; 2, 80, 200 as described); Q10 D (20 J; 1.25, 0.8, 9); Q11 C (60%; 40, 90, 167%: 150/90 = 166.7); Q12 B (30 W; 240, 1920, 0.033). All keys defensible and unique; I disagree with none. Cards 10-002 (20 J), 10-008 (30 J), 10-009 (4 J), 10-011 (3 m), 10-019 (60%), 10-021 (30 W) all correct. P02 marks sum to 8 (1+1+2+2+2); P03 16 (5+3+8). Figure practical-6118-10.png: axes "Time / s" and "Gravitational energy gained / J", points match table, passes through origin, scale legible; no defect other than X5.
Also X1, X2, X3, X4, X5, X6 (Q5 C, Q6 B/C weak; Q4/Q1 trivially cued), X7, X8, X9 apply.

---------------------------------------------------------------------
## D. TOPIC 11: Pressure and hydraulics
---------------------------------------------------------------------

11.1 [S2] Hydraulic brakes. Syllabus: "transmission of pressure in hydraulic systems with particular reference to hydraulic brakes on vehicles and hydraulic jacks". Notes give one sentence ("Brake fluid transmits a pedal-induced pressure to wheel mechanisms. Trapped air compresses and can make the response less effective") and no card, MC or P02 part mentions brakes. Missing: pedal -> master cylinder -> same pressure transmitted equally in all directions through the incompressible liquid -> slave pistons press brake pads on all wheels equally; larger slave pistons give larger force. Also "equally in all directions" (Pascal's principle) is never stated in the notes (they say only "An applied pressure change is transmitted"). Fix: add paragraph and a 2-mark card "Explain how pressing the brake pedal makes the brakes act on the wheels".

11.2 [S2] Manometer calculations. Syllabus "use and describe the use of a manometer and perform calculations". The notes have no worked manometer numerical (e.g. level difference 0.20 cm of water ... gas pressure = atmospheric + rho g h), the only card is 11-010 (descriptive, 1 mark), and neither MC nor P02 contains a manometer calculation (Q6 is directional only). Fix: add a worked example and a CALC card.

11.3 [S3] Missing value. Atmospheric pressure (about 100 kPa; 760 mm Hg = 101 kPa) is not stated anywhere although mm Hg <-> Pa and "gauge versus absolute" are taught. Check: 760 x 133 = 101 080 Pa. Fix: add it.

11.4 [S3] Card 11-007 vs 11-008 and objective mapping. 11-007 "Calculate the pressure difference for a 0.40 m height of water ..." is mapped to OBJ-6118-2.11-06 (derive the equation) while the recall-and-use objective 2.11-07 is served by 11-008. 11-007 and 11-008 are the same calculation with different numbers; the notes' worked example (0.40 m, 4000 Pa) is the card answer verbatim (4000 Pa). Fix: remap 11-007 to -07 or replace with a different task (e.g. find depth from a given pressure).

11.5 [S3] Card 11-005. Prompt "State how pressure changes as depth increases in a stationary liquid." / "It increases with depth." The objective is "related to depth and to density"; the card ignores density; cued (the stem says depth increases). Fix: "State two factors that affect the pressure in a liquid" -> depth and density.

11.6 [S3] Card 11-003 context "broad snowshoes ... on snow" is unfamiliar to Namibian learners. Fix: use a camel's foot, tractor tyres on sand, or a sharp versus blunt knife.

11.7 [S3] P02 (b). Quoted: prompt "State how increasing liquid density changes pressure at a fixed depth and g. [1]"; canonical "It increases the pressure above the surface value."; guidance "One mark for increased pressure difference." The canonical wording is mismatched to the guidance and imprecise; it should say "pressure increases (in proportion to density)". Fix: "Pressure (difference) increases; it is proportional to density."

11.8 [S3] Card 11-010 (1 mark). "Measure the vertical liquid-level difference and calculate rho g delta h; the gas pressure is higher when its connected surface is lower." Three ideas for one mark, and it omits stating the result "gas pressure = atmospheric + rho g delta h" which is the point of finding pressure relative to atmosphere (the prompt says "relative to atmosphere", so p - p_atm = rho g h is acceptable, but the mark scheme should say which). Fix: split into 2 marks.

11.9 [S3] Notes "recall and use the equation". Quoted: "A negative upward depth change gives a decrease in pressure; reporting its magnitude without direction can hide this meaning. Use one consistent height convention." Over-technical and confusing for NSSCO (vector sign conventions for depth). Fix: "Pressure decreases as you go up (to a smaller depth)".

11.10 [S3] Notes "state that a wind is caused by high and low pressure systems". Quoted: "Real wind direction also depends on Earth's rotation, friction and local terrain ... pressure-gradient effect". Earth-rotation (Coriolis) effects are beyond the syllabus and unflagged, and the note hedges the syllabus statement ("contributes to wind") instead of stating it: "Wind is air moving from a region of high pressure to a region of low pressure." Fix: state the syllabus sentence plainly; move deviations to an "extra" note.

11.11 [S3] P03 apparatus. Plan uses "a suitable low-range pressure sensor" zeroed at the surface; a 200-1000 Pa range with 2 cm depth steps needs a digital sensor not typical in Namibian school labs, while the syllabus practical is "investigate the relationship between pressure in liquids and depth" (rubber diaphragm/thistle funnel with U-tube manometer, or a tall can with holes). Gradient 10 000 Pa/m = rho g with rho 1000, g 10 is correct. Fix: give the manometer version (depth h of funnel; read manometer level difference; pressure = rho_liquid g x level difference).

11.12 [S4] Card 11-011 "using 1 mm Hg = 133 Pa" and notes "1 mm Hg ≈ 133 Pa": the accepted value is 133.3 Pa; the card uses "=" while the notes use "≈". Fix: "≈" and state "use this value".

Checks passed (topic 11): 60/0.020=3000 Pa; 40/0.020=2000 Pa; 30/0.010=3000 Pa; 1000x10x0.20=2000 Pa; 1000x10x0.40=4000; x0.35=3500; x0.60=6000; 20x133=2660; 30x133=3990; 50x133=6650; 3500x0.020=70 N; gradient 1000/0.1 = 10 000 Pa/m. MC keys: Q1 A, Q2 D, Q3 C, Q4 B, Q5 A, Q6 D (gas side lower => gas pressure higher: correct), Q7 C, Q8 B (distractors 300, 0.30, 3 as described), Q9 A (2000; 200 omits g; 50 000 = 10 000/0.2), Q10 D (2660; 6.65 = 133/20; 153 = 133+20; 0.150 = 20/133), Q11 C, Q12 B. All unique and defensible. The derivation (volume A dh, mass rho A dh, weight rho A dh g, /A) is correct and in scope (card 11-006: 4 marks; steps sum to 4). P02 marks 1+1+2+2+2=8; P03 16. Hydraulic equation F2 = F1 A2/A1 and "jack: smaller piston moves farther, no work created" are correct. Figure practical-6118-11.png: axes "Depth / m", "Pressure difference / Pa", points match table, passes through origin, no defect other than X5.
Specific MC weakness (X6): Q5 C "It becomes density", D "fixed by container shape"; Q6 C "Impossible to compare directions"; Q4 feedback for D "Input energy is required" does not address "newly created work"; Q1 and Q2 trivially cued by the stem ("force per area", "unit equals a pascal"). Q11 feedback B "Force is proportional to area, not its square" fine.
Also X1, X2, X4, X5, X6, X7, X8, X9 apply (X3 does not: no template prefixes in canonical answers).

---------------------------------------------------------------------
## E. TOPIC 12: Particles, phases and gases
---------------------------------------------------------------------

12.1 [S2] Card 12-018. Prompt: "Explain why stationary hot air can have a higher temperature than a cooler moving breeze." Canonical: "Temperature concerns mean random molecular kinetic energy. Bulk flow speed alone does not determine that thermal energy measure." Problems: (i) it never states the comparison the question asks (the hot air's molecules have greater mean random kinetic energy than the breeze's molecules; the breeze's organised motion adds no temperature); (ii) "that thermal energy measure" wrongly implies temperature measures thermal (internal) energy; temperature is related to mean kinetic energy, not to total thermal energy; (iii) the second mark is a negative statement. Fix: "Temperature depends on the average random kinetic energy of the molecules. The hot air's molecules have a larger average random kinetic energy; the breeze's movement is bulk motion in one direction and does not raise its temperature."

12.2 [S3] Card 12-021. Canonical: "Warmer particles tend to increase wall momentum transfer. The piston moves outward and the larger volume allows the gas pressure to balance the unchanged external pressure." The mechanism the objective wants (volume rises until impacts per area return to the original rate) is only implied; "tend to" is vague. Fix: "Particles move faster and hit the piston harder and more often, so the gas pushes the piston out; as volume increases the impacts per area fall until pressure equals the outside pressure."

12.3 [S3] Near duplicates among cards: 12-003 vs 12-015 (solid keeps shape/fixed relative positions, vibration); 12-013 vs 12-014 (liquid vs gas spacing and volume); 12-002 vs 12-010 (gas compressibility, spaces); 12-001 vs 12-020 (temperature, pressure, fixed volume) vs P02(d); 12-019 vs P02(c); 12-022 vs P02(e). Fix: merge or differentiate (e.g. 12-015 could ask about fluid flow only).

12.4 [S3] Card 12-005 and notes "Describe elastic particle collisions qualitatively". Prompt: "Explain why two interacting gas particles can leave with different speeds while the simple encounter model conserves kinetic energy." The syllabus lists "elastic collisions between particles" only as a feature of the model; the project scope screen says collision definitions are not required. The card asks for a formal conservation statement and wording ("simple encounter model", "combined kinetic energy") that is above Grade 10; notes also leave out the more important point for pressure explanations: collisions with the walls are elastic, so molecules do not lose energy and pressure does not die away. Fix: simplify to "State what 'elastic' means for collisions between gas molecules (no kinetic energy lost to the surroundings)" or make it a 1-mark recall; add the wall-collision sentence.

12.5 [S3] Card 12-016. Canonical: "Mean kinetic energy does not rise during the ideal phase change". "Ideal phase change" is unexplained jargon, and the answer does not say what the energy does (breaks/weakens the attractions between particles, increasing their potential energy). Fix: "The energy is used to overcome the forces holding the particles together instead of speeding them up."

12.6 [S3] Notes "describe the phases of matter and explain their inter-conversion". Evaporation (versus boiling) is absent, though "inter-conversion in everyday life" (drying clothes, sweat) is the objective; "deposition" is introduced but is not on the syllabus. Fix: add evaporation (fast molecules escape from the surface; cooling effect) and drop deposition or flag it.

12.7 [S3] Cards 12-019 and 12-020 / P02(c),(d). Guidance requires the word "momentum" ("impacts change molecular momentum", "transfer momentum to the walls at a greater rate"). Many learners will answer "molecules collide with the walls and exert a force; faster molecules collide harder and more often", which is a full syllabus-level answer ("describe qualitatively ... in terms of the motion of molecules"). The marking guidance has no accept list. Fix: accept "collide with walls / exert force" and treat "momentum" as optional.

12.8 [S4] Card 12-009. Canonical: "Heating increases the liquid's volume over the stated ordinary range." The prompt states no range. Fix: delete the phrase.

12.9 [S4] P03 table: "Liquid-column length / mm" 22 at 20 °C: the reference point (length measured from what mark?) is not stated; gradient 0.6 mm/°C is correct (15/25) and the "not the intrinsic expansion coefficient" remark is correct. Plausibility check: bulb of about 6 cm³ of water into a 1 mm radius tube gives about 0.5 mm per °C, so 0.6 mm/°C is realistic.

12.10 [S4] Notes "Explain thermal expansion ..." / "Pressure Law": "do not use a Celsius-temperature ratio as a proportional gas law" assumes the Kelvin scale (taught in topic 13); a one-clause pointer would help. Also "A gas has no comparable fixed sample volume at ordinary pressure" (notes, phase comparison) is awkward; say "A gas has no fixed volume; it spreads to fill its container."

12.11 [S4] MC wording. Q6 "What is directly seen in a Brownian-motion demonstration?" key D "Small suspended particles" is correct (smoke particles via microscope); fine but A feedback "They are not resolved by that observation" would be clearer as "molecules are too small to see". Q12 stem "sufficiently cold intact glass in humid air" cues the key.

Checks passed (topic 12): P03 gradient 15/25 = 0.6 mm/°C (every 5 °C -> 3 mm, exactly linear); P02 marks 1+1+2+2+2 = 8; P03 16. MC: all 12 keys are defensible and unique (Q1 A, Q2 D, Q3 C, Q4 B, Q5 A, Q6 D, Q7 C, Q8 B, Q9 A, Q10 D, Q11 C, Q12 B); I disagree with none. Physics statements in the notes (kinetic model, expansion, compressibility, diffusion, plateau at phase change = energy changes arrangement not mean KE, Brownian motion = random bombardment, gas laws qualitative with fixed amount/constant condition stated, water anomaly at 4 °C, condensation on cold glass) are correct; explanations at card level are correct apart from 12.1. Figure practical-6118-12.png: axes "Temperature / °C" and "Liquid-column length / mm", points match the table; y-axis starts at 22 (acceptable, a false-origin note for learners is absent); title is as wide as the plot (tight but readable).
Also X1, X2, X3, X4, X5, X6, X7, X9 apply.

---------------------------------------------------------------------
## F. COUNTS BY SEVERITY (cross-topic findings counted in each topic they list)
---------------------------------------------------------------------

| Topic | S1 | S2 | S3 | S4 | Total |
|---|---|---|---|---|---|
| 9  | 1 | 5 (X4, 9.2, 9.3, 9.4, 9.5) | 16 (X1, X2, X3, X5, X6, X7, 9.6, 9.7, 9.8, 9.9, 9.10, 9.11, 9.12, 9.13, 9.14, 9.15) | 2 (X9, 9.16) | 24 |
| 10 | 0 | 3 (X4, 10.1, 10.2) | 12 (X1, X2, X3, X5, X6, X7, 10.3-10.8) | 5 (X8, X9, 10.9, 10.10, 10.11) | 20 |
| 11 | 0 | 3 (X4, 11.1, 11.2) | 14 (X1, X2, X5, X6, X7, 11.3-11.11) | 3 (X8, X9, 11.12) | 20 |
| 12 | 0 | 2 (X4, 12.1) | 12 (X1, X2, X3, X5, X6, X7, 12.2-12.7) | 5 (X9, 12.8, 12.9, 12.10, 12.11) | 19 |


---------------------------------------------------------------------
## G. PER-TOPIC VERDICTS
---------------------------------------------------------------------

Topic 9 verdict: READY AFTER FIXES. One S1 physics error (greenhouse "moving warm air away", 9.1) must be corrected and the greenhouse objective needs a card; nuclear problems and "energy changes" answers must be made complete; the inverter content should be removed or flagged. All arithmetic and keys are correct; the structured tasks are labelled as practice data. Marking guidance is boilerplate and the MC key pattern is cyclic.

Topic 10 verdict: READY AFTER FIXES. Physics, numerics and keys are all correct; no S1. Needs: a forms-of-energy / lever-gear-pulley examples section and cards (objectives not practised), clearer lever/machine answers (10.4, 10.5), a fix to the "negative speed" sentence, realistic P03 scale, and the shared marking/MC fixes.

Topic 11 verdict: READY AFTER FIXES. Physics and numerics are correct and the derivation is sound. Hydraulic brakes and manometer calculations (both named in the syllabus) are practically uncovered and need notes plus cards; atmospheric pressure value, wind sentence and the pressure-sensor practical need adjusting; shared marking/MC fixes apply.

Topic 12 verdict: READY AFTER FIXES. Content is physically accurate and in scope. Card 12-018 is imprecise (S2) and several cards are near duplicates with weak mechanisms (12-021, 12-016); marking guidance should accept "collide with walls" wording; evaporation is missing; shared MC/practical fixes apply.

---------------------------------------------------------------------
## H. WHAT WAS CHECKED / NOT CHECKED
---------------------------------------------------------------------

Checked: all four notes files in full (every section, definition, equation, unit and worked example); every item in all four flashcard JSON files (9: 24 items; 10: 24; 11: 15; 12: 27, each 3 of which are P01/P02/P03); all 48 MC questions solved independently and compared with keys (no disagreements), with every numeric distractor reconstructed; every calculation card, P02 and P03 gradient recomputed in python (python3 -I, no numpy available: simple arithmetic); mark allocations summed (P01 12, P02 8, P03 16, flashcards 1/2/4); all 4 figures viewed (practical-6118-9/10/11/12.png; these are the only figures referenced by these notes); a 7-word shingle comparison of notes+flashcards against pdftotext of all 24 NSSCO (New) papers/examiner reports (no copied runs; the numbers are limited by extractable text layers, so scanned pages or heavily column-split tables could hide a match); syllabus objectives 2.10.1-2.11 and 3.1 read from the syllabus PDF text; scope screens read from PLAN-6118-nssco-physics.md (collision definitions not required; nuclide formulae limited in energy sources; diverging lenses only for eye correction). No nuclide formulae were found in topic 9; no diverging-lens content in these topics.

Not checked / limits: examiner-report marking evidence for these topics is partial (assessment-evidence/GAPS.md not individually reconciled against each guidance line); I did not open topics/<N>/claims, contract.json or qa_report.json to trace claim_ids to sources (the `claim_ids` fields were not audited); I did not verify the rendered/HTML versions of notes, only the markdown and JSON; I did not read misconceptions.json entry by entry, so distractor suggestions are my own physics judgement, not tied to catalogue IDs; Namibian classroom availability of apparatus (11.11, 10.8) is judgement not evidence; no learner trial of reading level. No file in the repository was edited; scratch work lives in the scratchpad (review/Cwork/).
