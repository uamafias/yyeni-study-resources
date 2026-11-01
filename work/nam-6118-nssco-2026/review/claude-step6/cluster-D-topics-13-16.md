# Cluster D review: NSSCO Physics 6118, topics 13, 14, 15, 16

Reviewer: independent physics reviewer. Review only; no repository file was edited.
Package: /Users/yyeniai/yyeni-study-resources/publish/nam-6118-nssco-2026/
Severity: S1 wrong or misleading; S2 imprecise, could cost marks, or out of scope; S3 pedagogy, clarity, duplicate, weak distractor; S4 minor.
All numeric examples, all 4x12 MC questions, all short_answer and practical_task data were recomputed in python (-I). Only the findings below are mismatches or defects. Everything else in the notes and cards that I checked was correct.

## Cross-topic facts (verified, apply to all four topics)
- The notes MC block, the short_answer and the practical_task are byte-identical to the JSON prompt/canonical_answer. The notes are the cards.
- In all four MC sets the keys are exactly A D C B A D C B A D C B (3 of each letter). I solved all 48 questions blind before reading the keys. All 48 keys agree with my answers and each question has one defensible answer.
- The marking_guidance for every flashcard is the canonical answer split into sentences under a fixed label ("Cause and effect:", "Contrast:", "Combine the linked ideas and explain the reason:", "Identify the error and give the correct distinction:", "Method step:", "Property or unit:", "Diagram/graph feature:"). It gives no acceptable alternatives, no "do not accept", no unit or sig-fig policy and no ECF.
- In every practical_task the marks sum correctly to 16 (graph 1+1+2+1=5, gradient 1+1+1=3, plan 5+1+1+1=8). Invented data are labelled "invented, idealised practice readings" in all four. Good.
- Past-paper copying: an 8-word-run check against all held NSSCO (New) papers and reports found zero hits in topics 13 and 15. Hits in topics 14 and 16 are only the syllabus-mandated definitions (specific heat capacity, specific latent heat, period, wavefront). These are acceptable, S4 at most.

---------------------------------------------------------------------
## TOPIC 13 Temperature and thermometers

**13.1 [S2] Out-of-syllabus idea taught and assessed: "resolution".** Location: notes "### Explain thermometer sensitivity"; card ITEM-6118-13-008-DIST.
Quote: "It differs from resolution, which is the smallest displayed or readable increment." Card prompt: "Explain the difference between sensitivity and resolution."
Problem: syllabus 3.2.1 asks only for sensitivity, range and linearity. Resolution is not an objective, so a 2-mark card is spent on out-of-scope content and is not flagged as extension. The same notes also bring in "response time", "self-heating" and "thermodynamic temperature".
Fix: replace with a card on sensitivity vs range, or on sensitivity vs accuracy (already in the notes). If kept, flag it as extension.

**13.2 [S2] Tariff does not match the answer.** Location: ITEM-6118-13-014-PROC (1 mark, "Describe how a thermocouple can measure a rapidly changing high temperature.").
Quote: "A small junction of two different conductors develops a calibrated electrical output relative to a reference, and its low thermal capacity allows rapid response."
Problem: the answer holds four creditable ideas (two different metals, junction, e.m.f. or output, low thermal capacity) for 1 mark. The notes' "reference junction" is dropped here as "relative to a reference". The prompt asks for two things (high temperature and rapidly varying), and only rapid response is explained. Nothing is said about why it suits high temperatures (metals with high melting points, no liquid to boil).
Fix: make it 2 marks. (1) Two different metals joined, giving an e.m.f. that depends on the junction temperature. (2) Small junction, low thermal capacity, so fast response. Add a separate note on high-temperature range.

**13.3 [S2] Prompt/answer mismatch ("one" vs two).** Location: ITEM-6118-13-013-DIST.
Quote: prompt "Explain one range difference between alcohol and mercury as thermometric liquids." Answer: "Alcohol can remain liquid at lower temperatures than mercury. Its lower boiling point limits high-temperature use compared with mercury."
Problem: the prompt says "one" difference but the 2 marks need two differences (low end and high end). A learner who gives one correct difference with an explanation gets 1 mark or is confused.
Fix: "Compare the usable temperature ranges of alcohol and mercury thermometers." (2 marks).

**13.4 [S3] Definition of absolute zero is thin and jargon-heavy.** Location: ITEM-6118-13-001-DEF.
Quote: "Absolute zero is the lower limit of thermodynamic temperature, 0 K."
Problem: "thermodynamic temperature" is not a Grade 10 term, and the answer is close to circular ("lower limit of temperature = 0 K"). It never says -273 °C or "lowest possible temperature". Typical marking expects "lowest possible temperature, 0 K (about -273 °C)". The notes' caution not to claim all motion stops is sound, but a learner answering "the lowest possible temperature" would be unsure whether to get the mark.
Fix: "The lowest possible temperature, 0 K (about -273 °C)."

**13.5 [S3] Number coincidence cues the answer.** Location: ITEM-6118-13-006-CALC.
Quote: "reading 50 mm when its readings are 10 mm at 0 °C and 90 mm at 100 °C ... The temperature is 50 °C."
Problem: 50 mm is the midpoint (10+90)/2, so the answer 50 °C equals the reading, and a learner who ignores the offset still gets 50. (45-10 style values would discriminate; compare MC Q10, where 45 gives 25.) Computation (50-10)/(90-10)x100 = 50.0, correct.
Fix: use e.g. 58 mm giving 60 °C.

**13.6 [S3] Answer-position pattern.** Location: ITEM-6118-13-P01. Keys: A D C B A D C B A D C B. Strictly periodic, so a learner who finds the first four can predict the rest. Reorder to break the cycle.

**13.7 [S3] Weak or implausible distractors.** Location: ITEM-6118-13-P01.
- Q2 A "Liquid mass increasing with heat", B "Its fixed colour alone", C "The room's weight" are not plausible.
- Q4 A "A vertical line across many temperatures" is not a possible calibration graph, and its feedback, "Temperature belongs on an independent calibration axis", does not explain why it is wrong.
- Q9 D "0 K" is implausible.
- Q6 A "It contains a large liquid tank" is absurd for a thermocouple.
- Q7 A, B and D ("cannot expand", "no visible surface", "gas at room temperature") are physically absurd.
- Q1 and Q5 are trivial (key = 0 K; key = "known temperature references").
Also the key is the most specific and longest-worded option in Q5 and Q6.
Fix: use real misconceptions, such as "linear = starts at zero", "greater range = greater sensitivity", "0 °C = 0 K" and "add 273 to a temperature difference".

**13.8 [S3] Marking guidance is boilerplate or mislabelled.**
- ITEM-6118-13-003-SYNTH and -007-SYNTH: "Combine the linked ideas and explain the reason: Link reproducible property changes to known temperature values through calibration." The label does not match the answer, and the canonical answer contains the authoring word "Link".
- ITEM-6118-13-011-FEATURE: "Property or unit: They provide reproducible known temperatures for calibrating the scale." The answer is a purpose, not a property or unit.
- ITEM-6118-13-002-CALC: "Equation, substitution and final result: T = -15 + 273." The guidance does not say whether the unit K is required for the final mark.
Fix: write real mark points with accept and reject notes (for example "accept 258 K, not 258 °C").

**13.9 [S3] Practical task: marks and prompt do not align.** Location: ITEM-6118-13-P03 (c).
Quote: prompt "Include the arrangement, five operational measurement steps, controls, a table and how the data would support a conclusion." Guidance: "Controls and safety support the method; the planning allocation totals eight marks."
Problem: the prompt asks for an arrangement and controls, but the 8 marks are 5 steps + table + "Graph: an appropriate relationship plotted" + conclusion. Controls and arrangement earn nothing, and a graph is credited again inside the plan although the learner has already drawn it in (a).
Also: graph (a) data starts at 20 °C, so "calibration offset ... not evidence of a wrong slope" in the notes is correct, but the intercept (8 mm at 0 °C, from 22 - 0.7x20) is never asked for, which wastes the interesting feature.
Fix: allocate controls (1) and diagram/arrangement (1), drop the duplicate graph mark.

**13.10 [S3] Coverage gaps against syllabus 3.2.1.** No card states both fixed points as values (only the short answer, (b) "Ice point, 0 °C"). No card converts K to °C. No card on bulb size or wall thickness affecting sensitivity or response (only the narrow bore). No card on disadvantages of mercury (toxic, opaque, expensive) or advantages of alcohol (dye, large expansion). No card on the objective "state and apply examples ... resistance of a metal" beyond one mechanism card. No card on thermocouple structure (the answer is one sentence).

**13.11 [S3] Jargon above Grade 10.** Notes use "thermodynamic temperature", "limiting minimum thermal motion", "interpolation", "extrapolation requires further evidence", "self-heating", "compensated reference", "capillary turns a small volume change into a visible length change". These are all explainable in plainer words ("the thin tube magnifies the change").

**13.12 [S3] Vague first mark.** Location: ITEM-6118-13-015-MISCON.
Quote: "The learner has confused the origins of the Celsius and kelvin scales." Prompt: "A learner says water at 0 °C is at absolute zero."
Problem: mark 1 can be earned by a vague "they mixed up Celsius and Kelvin" without saying what each scale's zero is. "Origins" is jargon. Water at 0 °C is also ambiguous (ice or water).
Fix: mark 1 = "0 °C is the freezing point of water, not the lowest possible temperature"; mark 2 = "0 K (-273 °C) is absolute zero; 0 °C = 273 K".

**13.13 [S4] Bloom label inflated.** SYNTH cards (-003, -007) are 2-mark recall-with-reason items labelled "Analyse". The short_answer carries command_word "State" although it mixes State, Explain and Calculate.

Figures (topic 13): practical-6118-13.png viewed. Axes and units are correct (Column length / mm vs Reference temperature / °C), points match the table, the line is straight and the gradient is consistent (0.7 mm/°C). No error. (S4: no gradient triangle is shown, and the title is slightly long.)

Numerics recomputed for topic 13: 273-15=258; (55-15)/100x100=40; (70-10)/100x100=60; (50-10)/80x100=50; (45-20)/100x100=25; 27+273=300; 12/4=3; 42+273=315; gradient (57-22)/(70-20)=0.7 mm/°C. All correct.

### Verdict topic 13: ready after fixes
Physics is correct throughout and the MC keys agree. The fixes needed are scope (resolution), two tariff and prompt mismatches (13.2 and 13.3), thin and mislabelled mark guidance and weak distractors.

---------------------------------------------------------------------
## TOPIC 14 Heat capacity and changes of state

**14.1 [S1] Practical task: gradient value, unit and meaning wrong; graph description contradicts the prompt.** Location: ITEM-6118-14-P03 canonical answer and notes "Practice task ... Graph:" and "Gradient:".
Quote: "Graph: Plot temperature rise vertically against absorbed energy horizontally for the fixed 0.20 kg sample." and "Gradient: 8000 ÷ 10 = 800 K/J. The gradient is 1/(mc), reciprocal heat capacity, rather than specific heat capacity itself. For known mass, c = 1/(mass × gradient)."
Working: the prompt says Energy supplied / J on the vertical axis and Temperature rise / K on the horizontal axis. Gradient = ΔE/ΔT = 8000 J / 10 K = 800 J/K, which is the heat capacity C = mc of the sample (not 1/(mc)). Then c = gradient/m = 800/0.20 = 4000 J/(kg K). The printed 800 K/J has the wrong unit and the wrong physical meaning (it would be 800 K per joule, an absurd value). The formula "c = 1/(mass x gradient)" gives 1/(0.2x800) = 0.00625, wrong. The figure practical-6118-14.png correctly plots E vertically against ΔT, so the figure also contradicts the canonical text. The marking guidance ("axis-ratio unit") would accept J/K, which contradicts the canonical K/J.
Correct version: "Plot energy supplied (vertical) against temperature rise (horizontal). Gradient = 8000 / 10 = 800 J/K. The gradient is the heat capacity C of the sample. c = C/m = 800 / 0.20 = 4000 J/(kg K)."

**14.2 [S2] Circular definition and out-of-scope term.** Location: notes "### Define boiling point" and ITEM-6118-14-016-DEF.
Quote: "Boiling point is the temperature at which a liquid boils at a specified pressure. Boiling occurs when its vapour pressure permits bubbles to form throughout the liquid."
Problem: "boils" is used to define boiling point. "vapour pressure permits bubbles" is vague (the correct idea is saturated vapour pressure equals external pressure) and is beyond Grade 10 and the syllabus. Syllabus: "temperature at which a change of state occurs".
Fix: "The temperature at which a liquid changes to vapour throughout the liquid (bubbles form) at a given pressure; it stays constant while boiling." Drop vapour pressure.

**14.3 [S2] Tariff does not match the answer.** Location: ITEM-6118-14-007-PROC (1 mark).
Quote: "Measure its mass, the heater energy and its temperature rise, minimise losses and calculate c = Q/(mΔT)."
Problem: at least four creditable points (mass, energy via joulemeter or P x t, temperature rise, insulation, formula) for 1 mark. The notes' close-contact holes, initial and final temperature, and stirring for liquids are not credited. 14-008-PROC is similar (equal energy, different masses, ΔT versus 1/m, control) for 1 mark. These are Paper 2-type "describe" questions that normally carry 3-4 marks.
Fix: make these 3-mark cards with separate points.

**14.4 [S2] Unit form and the syllabus's c of water.** Location: short_answer ITEM-6118-14-P02 (a), notes "Use specific heat capacity".
Quote: "(a) One mark for energy per kg per kelvin." Answer "J/(kg K)".
Problem: the syllabus practical list uses "4200 J/(kg ˚C)". The guidance does not accept J/(kg °C), J/kg°C or J kg⁻¹ K⁻¹. The guidance text "energy per kg per kelvin" is a description, not a unit. The notes and cards never give c(water) = 4200 J/(kg °C), though the syllabus requires it (kettle practical).
Fix: state accepted forms and add a card or worked example using 4200 J/(kg °C).

**14.5 [S3] Unrealistic heating and cooling curve data teaches a misleading time scale.** Location: notes "plot and interpret heating and cooling curves" and card ITEM-6118-14-018-INTERP; figure-6118-14-01.png.
Quote: "times 0, 2, 4, 6, 8, 10 min with temperatures -10, 0, 0, 50, 100, 100 °C".
Working at constant power with ice 2100, water 4200, L_f 334 000, L_v 2.26x10^6 (J/kg or J/(kg K)): warming ice 10 K = 21 kJ per kg; melting = 334 kJ (about 16x longer); warming water 0 to 50 °C = 210 kJ (10x the ice-warming time); boiling = 2260 kJ (about 5.4x the time of heating 0 to 100 °C). So equal 2-minute plateaux and equal 2-minute heating segments are physically wrong by an order of magnitude. The notes' remark "Plateau durations depend on energy rate and amount" is correct but the data given contradicts the physics, and the boiling plateau should be the longest feature. It also makes the cooling example look as if freezing takes as long as condensation.
Fix: label "not to scale" or re-time, e.g. heating -10 °C at 0, 0 °C at 1, melting end at 17, 100 °C at 28, boiling end at 150 min-equivalent scaled; at least make melting about 8x and boiling about 5x longer than the warming segments.

**14.6 [S3] Near-duplicate cards.** ITEM-6118-14-011-MECH ("Explain what supplied energy changes during a constant-temperature phase change"), -020-MISCON (boiling, error in "continuously increasing average kinetic energy") and -013-MECH (heater on while boiling) give the same two points (interaction potential energy up, mean kinetic energy unchanged). Also -009-DEF and -010-DEF overlap with the short answer (a), (b), (c). Keep one and replace the others with melting vs boiling or cooling-curve interpretation.

**14.7 [S3] MC key pattern.** ITEM-6118-14-P01 keys A D C B A D C B A D C B (periodic).

**14.8 [S3] MC distractors and stems.** ITEM-6118-14-P01.
- Q5 "A pure substance melts at fixed pressure. What can remain constant?" has the stem "can", with options partly "must" statements. Weak: B "Energy input must be zero" is absurd.
- Q6 B "To prevent a temperature rise" and A are absurd.
- Q7 A "Temperature as a mass" and B "A unit of force" are not plausible. Also the key "Microscopic particle kinetic energy" omits potential energy, the very idea that topic 14 is built on.
- Q12 A "Zero elapsed time" is implausible.
- Q1 trivial (unit of heat capacity J/K is the only one with K and no kg, while the others are named in the options).
Numerics verified: Q8 900/3=300; Q9 0.5x400x5=1000; Q10 0.10x300000=30000; Q11 half. All correct.

**14.9 [S3] Boilerplate guidance and authoring text in answers.** ITEM-6118-14-014-SYNTH: "Combine the linked ideas and explain the reason: Link the lower plateau near 0 °C to solid changing to liquid." The canonical answer contains the instruction word "Link". ITEM-6118-14-019-MISCON mark 1 "The error is using a temperature-rise equation for a phase change" is fine, but the same label is used for answers that do not name an error.

**14.10 [S3] INTERP card: answer figure does not show the required labels, and the card is over-labelled.** Location: ITEM-6118-14-018-INTERP; figure-6118-14-01.png (also used under notes "### Original graphical solution", titled "Original labelled graph").
Quote: "labelling the two phase-change regions" / "Label the horizontal 0 °C region melting and the 100 °C region boiling."
Problem: the figure contains no "melting" or "boiling" text; it also adds an unrequested orange cooling curve (110, 100, 100, 50, 0, 0), so the "answer" differs from the task. Axes and units are correct (Time / min, Temperature / °C) and the points match the stated data. The guidance gives no marks for axis labels, units or scale. Bloom "Analyse" is high for plotting given data (Apply).
Fix: add labels to the figure, or remove the second curve; guidance should credit axes, plotting and labels.

**14.11 [S3] Confusing sentence in notes.** Location: notes "### Define melting point".
Quote: "A temperature below that point does not mean a hot liquid is present simply because heating has started; the initial state and supplied energy must be considered."
Problem: reads as a non sequitur and is not part of the definition. Remove or reword: "Heating a solid below its melting point first raises its temperature; it only melts once the melting point is reached."

**14.12 [S3] Practical task plan quality.** ITEM-6118-14-P03 (c).
Quote: "4. Wait for a representative temperature and record the rise after each increment. 5. Repeat with the same mass and compare the temperature-rise versus energy lines."
Problem: "representative temperature" is unclear; step 5 does not vary anything and has no independent aim. The plan also uses a "joulemeter"; the syllabus practical list uses power and time (kettle or heater of known power). No mention of stirring for a liquid, and "Curvature may indicate heat loss or changing response" is fine. The plan uses the energy-increment method but the task data table (energy vs rise) are treated as given.
Fix: add a measured P and t option (Q = Pt), stir for liquids, and make step 5 vary the mass (links to inverse proportionality objective).

**14.13 [S3] Coverage gaps.** No card for: thermal capacity term (objective 02 only through a comparison card), evaporation cooling, cooling curve interpretation, a two-stage calculation (warm to melting point, then melt), 4200 J/(kg °C) kettle calculation, measuring l of water by kettle.

**14.14 [S3] Vague prompt.** Short_answer (c) "Explain energy input during constant-temperature melting." The question does not say what is to be explained (where the energy goes), so the two mark points (interaction/arrangement change; unchanged mean kinetic energy) are not cued by the prompt.

**14.15 [S4] Odd phrasing.** ITEM-6118-14-009-DEF "Define latent heat for a whole sample." The syllabus says only "L". Use "Define latent heat L."

**14.16 [S4] Bloom/command labels.** SYNTH -014 and the short answer's command word "State" for a mixed task.

Numerics recomputed for topic 14: C=800/4=200; c=2100/(0.5x10)=420; l=12000/0.040=300000; 1600/(0.2x20)=400; 600/3=200; 15000/0.05=300000; Q=0.2x400x10=800; Q=0.03x300000=9000; practical gradient 8000/10=800 J/K (notes say 800 K/J, wrong); c=4000 J/(kg K). All correct except 14.1.

### Verdict topic 14: not ready
Contains a genuine answer-key error (14.1: gradient unit, meaning and graph orientation wrong in notes and JSON). After fixing 14.1 and the 14.2-14.5 items it is "ready after fixes".

---------------------------------------------------------------------
## TOPIC 15 Thermal energy transfer

**15.1 [S1] Practical task: gradient unit wrong by a factor of 60; table unit inconsistent.** Location: ITEM-6118-15-P03; notes "Gradient:" and "Table:".
Quote: "Gradient: -8 ÷ 100 = -0.08 °C/min. The negative gradient is temperature decrease per minute." Table: "Record time / min and water temperature / °C".
Working: the data table uses Time / s (0, 20, ..., 100) and the graph axis is Time / s (practical-6118-15.png confirms). -8 °C / 100 s = -0.08 °C/s = -4.8 °C/min. The printed unit °C/min is wrong; the value -0.08 °C/min would be 100 times too small compared with the data. A learner who correctly writes -0.08 °C/s would be marked wrong by the canonical answer, and the "axis-ratio unit" guidance would give °C/s, contradicting the key.
Correct version: "Gradient = (70 - 78)/(100 - 0) = -0.08 °C/s (= -4.8 °C/min). Table: Time / s."

**15.2 [S2] Molecular account of conduction is too vague to earn exam marks.** Location: notes "### give a simple molecular account of the heat transfer in insulators and the migration of electrons in metals"; ITEM-6118-15-003-MECH.
Quote: "Both transfer energy through particle interactions. The metal additionally has mobile electrons that carry energy through it."
Problem: the syllabus asks for the simple molecular account. The accepted account is "particles vibrate, pass the vibrations to neighbouring particles (by collisions)" and "free electrons gain kinetic energy, move through the metal and collide with atoms, passing energy on". "Particle interactions" and "mobile electrons that carry energy" are not that. The first mark ("Both transfer energy through particle interactions") would be awarded for almost any sentence. The notes also never say that the hotter end's particles vibrate more strongly.
Fix: "Hot end: particles vibrate more and pass this energy to neighbours by collisions. In metals free electrons also move through the metal and pass on energy."

**15.3 [S3] Unrealistic cooling data.** Location: ITEM-6118-15-P03 table (78 to 70 °C in 100 s).
Working: 4.8 °C/min. A covered hot-water container loses about 0.2-1 °C/min near 70 °C. The data are labelled "invented, idealised", but a 100 s window makes the "covered container" claim misleading and the graph is unlike what a learner would measure. The plan then has time recorded "at regular short intervals", which is fine.
Fix: use minutes, 0 to 10 min, 78 to 70 °C (0.8 °C/min).

**15.4 [S3] Misuse of "temperature gradient".** Location: ITEM-6118-15-P01 Q12 and short_answer (e).
Quote: "What is its average temperature gradient?" / "Calculate the average temperature-time gradient".
Problem: in thermal physics, temperature gradient means temperature change per unit distance, the quantity that drives conduction in this very topic. The rate of change of temperature with time is the "rate of cooling" or "gradient of the temperature-time graph". "Temperature-time gradient" is clearer, but Q12 uses "temperature gradient" alone. Maths is correct: (64-70)/3 = -2 °C/min.

**15.5 [S3] MC key pattern.** ITEM-6118-15-P01 keys A D C B A D C B A D C B (periodic).

**15.6 [S3] MC distractor and cueing problems.** ITEM-6118-15-P01.
- Q3 "Which material can sustain ordinary internal convection?" key "A liquid"; a gas is also correct physically, but is not offered. "ordinary" is vague. Options A "A vacuum" and B "An isolated empty region" are the same idea, so they are redundant.
- Q4: A "Water circulation" and D "Convection" are near-synonyms.
- Q5 D "Electron streams by definition" and Q2 B/C are not plausible.
- Q6 stem "What must match in an emission comparison?" with options A, B, C phrased as things that differ ("Different detector distances", "Different exposed areas", "One surface being heated much more"); only D is a quantity that can match, so the grammar cues the key. Answer D "Surface temperature".
- Q7 A "No surface at all" and B "A finish selected without specifying properties" are absurd; the stem phrase "named school comparison" is odd.
- Q10 A "It becomes an exact material-only test" and Q11 D "To improve heat flow into the hand" are absurd.
Also Q9 key "They reduce radiation" is correct, and incomplete as a full flask explanation, but acceptable for MC.

**15.7 [S3] Unclear first mark point.** ITEM-6118-15-017-MISCON.
Quote: prompt "A metal heater warms water that then circulates upward. Explain why calling the entire transfer conduction is incomplete." Mark 1: "The correct boundary process can involve conduction without bulk material flow."
Problem: this mark point does not state the error (calling the circulation conduction). Fix: "The upward circulation is convection (bulk movement of the water); conduction is only the transfer from the heater into the nearby water."

**15.8 [S3] Coverage gaps (syllabus 3.3).** No card for: surface properties (matt black = good absorber and emitter, shiny/white = poor absorber and poor emitter, good reflector); good conductors/insulators examples; the experiment for conduction in more than one sentence; why the vacuum flask has a stopper and silvered walls separately; convection in gases (sea breeze, ventilation) beyond the room-heater card; infra-red as a heat radiation from hot objects.

**15.9 [S3] Practical task is mapped to objectives it does not test.** ITEM-6118-15-P03 objective_ids include OBJ-6118-3.3.3-03 (emitters and absorbers) but the plan compares insulation layers on a covered container. Also step 3 "record the stirred water temperature" is awkward through a lid. The notes' conclusion statement ("a smaller magnitude indicates slower cooling") is correct. Fix: either map to 3.3.4, or plan a black/shiny can cooling test.

**15.10 [S3] Trivial card cued by neighbour.** ITEM-6118-15-009-FEATURE "State the type of wave that infrared radiation is." Answer "It is an electromagnetic wave." Card 15-008 already states "electromagnetic waves", so it cues the answer. Fix: "Name two other types of wave in the same family" or similar; the notes also lack the infrared-specific content the syllabus asks (emission from hot objects).

**15.11 [S3] Shiny surfaces: missing reason.** Notes "### Explain an application of thermal radiation" and card 15-016: "Shiny metallic surfaces can reduce infrared exchange" and "The flask benefits from reducing radiative transfer with suitable shiny surfaces." The key reason (shiny surfaces reflect radiation and emit poorly) is missing; "reducing radiative transfer" would not earn the mark in an exam that asks "why is the flask silvered?".

**15.12 [S3] Boilerplate guidance.** ITEM-6118-15-013-SYNTH answer begins "Combine mechanisms:" and mark 1 reads "Combine the linked ideas and explain the reason: Combine mechanisms: the vacuum reduces conduction and convection across the gap." ITEM-6118-15-010-SYNTH, -013-SYNTH, -002-PROC (1 mark for "Heat matched rods equally and compare temperature rises at equal distances after the same time", which has 3 ideas) are similar. 15-002 is also arguably AO C (planning an investigation) not A.

**15.13 [S4] Jargon and wording.** "matched thermal capacities" (10-SYNTH), "Do not infer infrared behaviour from visible colour alone for every advanced material", "confounds" (Q10 feedback), "Conduction across a heater-fluid boundary".

**15.14 [S4] Figure title cropped.** practical-6118-15.png: the title "Original practice: Initial cooling of a covered water container over a short approximately linear..." is cut off at the right edge. Axes (Temperature / °C, Time / s), data and straight falling line are correct.

Numerics recomputed for topic 15: (64-70)/3 = -2 °C/min; (60-68)/4 = -2 °C/min; table gradient (70-78)/100 = -0.08 °C/s (notes say °C/min, wrong).

Figures: topic 15 has no explanatory figure other than practical-6118-15.png (checked above).

### Verdict topic 15: not ready
One answer-key error (15.1, unit off by a factor of 60 and a unit contradiction between table and answer) and a vague account of molecular conduction (15.2). After fixing these it is "ready after fixes".

---------------------------------------------------------------------
## TOPIC 16 Wave motion and wavefronts

**16.1 [S1] Practical task: wave speed in the wrong unit, off by a factor of 100.** Location: ITEM-6118-16-P03; notes "Gradient:".
Quote: "Gradient: 5 ÷ 0.25 = 20 m/s. The gradient is wave speed because λ = c(1/f)."
Working: the table gives wavelength in cm and period in s. Gradient = 5 cm / 0.25 s = 20 cm/s = 0.20 m/s. A ripple-tank speed of 0.20 m/s is realistic and matches the topic's own example (5 Hz x 0.040 m = 0.20 m/s); 20 m/s is not. The task's "axis-ratio unit" credit would give cm/s, contradicting "m/s" in the key. Check: 0.1 s with 2 cm gives 20 cm/s as well.
Correct version: "Gradient = (7 - 2) cm / (0.35 - 0.10) s = 20 cm/s = 0.20 m/s. The gradient is the wave speed (λ = cT)."

**16.2 [S3] Graph description does not match the task.** Same item. Prompt: "Wavelength / cm on the vertical axis and Period / s on the horizontal axis." Answer: "Plot wavelength vertically against reciprocal frequency horizontally at fixed depth." Reciprocal frequency equals period, but the learner is never told this, and the phrase "reciprocal frequency" and the table in the plan ("frequency / Hz, reciprocal frequency / s") add a conversion that the data table does not need. Fix: "Plot wavelength against period (T = 1/f); gradient = λ/T = c."

**16.3 [S3] MC key pattern.** ITEM-6118-16-P01 keys A D C B A D C B A D C B (periodic).

**16.4 [S3] MC distractor and stem issues.** ITEM-6118-16-P01.
- Q1 B "A repeated train by definition" and Q6 B, C ("New rope mass", "Only a colour change") are absurd.
- Q4 C "The same source distance in every wave type" is a weak distractor, and the feedback "Plane fronts need no single finite source centre" is hard for learners.
- Q5 D "5 m/s" is absurd.
- Q7 "Which remains unchanged at a stationary depth boundary?" ("stationary" is odd; a depth boundary does not move).
- Q12 the stem gives "slows at unchanged frequency", which nearly states the answer ("decreases").
Numerics verified: Q8 4x0.08=0.32; Q9 1/0.5=2; Q10 2x340=680; Q11 20/4=5. All correct.

**16.5 [S3] Weak mark point.** ITEM-6118-16-005-MECH ("Explain why sound typically travels faster in glass than in air."). Mark 2: "The gas's widely separated particles and different mechanical response transmit the disturbance more slowly." "Different mechanical response" is not Grade 10 content. The syllabus wants: particles are closer, so vibrations pass on more quickly. The notes' "stiffness and inertia" and "mechanical response" are also above the level.

**16.6 [S3] Two mark points are the same idea.** ITEM-6118-16-006-MECH. Mark 1 "The light and sound travel toward the observer at very different speeds." Mark 2 "Light arrives much earlier because its air speed is far greater." Both say "light is faster". Better: mark 1 "light travels at about 3x10^8 m/s, sound about 340 m/s", mark 2 "so the flash arrives first, and the delay can be used to find distance".

**16.7 [S3] Repeated numbers across cards.** ITEM-6118-16-016-CALC (T=0.20 s gives 5 Hz) and ITEM-6118-16-024-MISCON (λ=0.060 m, T=0.20 s) and the notes' worked example are the same numbers. Card 024's answer 0.30 m/s equals card 015's answer (6 x 0.050), and the notes "Distinguishing the ideas" example. This lets learners memorise answers. Vary the numbers.

**16.8 [S3] Notes contradict the syllabus's own definition.** Notes "### define oscillations or simple harmonic motion ...": "the stricter term simple harmonic motion additionally requires a particular restoring-effect relation, so not every possible repeated motion has that special form." This is true physics, but the syllabus (and the exam) defines SHM as "any repeated to-and-fro motion". A learner using the notes' definition would write a more complex answer than the mark scheme; the notes should say "for NSSCO use the syllabus wording" and flag the extension. Card 16-002 ("Define an oscillation") does not mention SHM or give the syllabus examples (tuning fork, pendulum, stretched string).

**16.9 [S3] Examples not tested.** Syllabus: "distinguish between transverse and longitudinal waves ... and give examples of each". Card ITEM-6118-16-007-DIST asks only for the difference and the answer has no examples ("Transverse oscillations are perpendicular to propagation"), and the notes name only rope and sound. Missing: water, light and other EM waves (transverse); sound, compressions in a spring (longitudinal). The phrase "vibration of the particles" from the syllabus should be used.

**16.10 [S3] Coverage gap: typical speeds.** Syllabus: "state typical values of the speed of sound and light in air, water and glass and the speed of light in a vacuum". Only ITEM-6118-16-004-FEATURE (air, 340 m/s) is a card; the MC Q5 uses 3.0x10^8 once. Water and glass values (1500, 5000 m/s; 2.25x10^8, 2.0x10^8 m/s) have no card. The 340 m/s card's guidance gives only "Approximately 340 m/s": it should accept about 330-345 m/s, and say "ordinary room conditions" (about 343 m/s at 20 °C).

**16.11 [S3] Confusing safety sentence.** Notes "### Different arrival times of light and sound": "This is a propagation-time model, not an instruction to remain outside during a storm." The sentence is double-negative and could be misread. Fix: "In a thunderstorm take shelter indoors; do not wait to hear the thunder."

**16.12 [S3] Figure figure-6118-16-01.png (circular wavefronts).** Viewed. Three circles with radii in ratio 1:2:3 (about 85, 170, 255 px) and an outward arrow, correct in concept. Defects: no dot at the centre to mark the source; the word "Source" floats above the arrow start; the arrow head is at the 2nd circle but the shaft runs on beyond the 3rd circle; "Outward" label overlaps the ray line. A learner could read the arrow as pointing at the middle ring only.

**16.13 [S3] Figure figure-6118-16-03.png (reflection).** Viewed. Measured geometry: incident ray 30° (dx=187, dy=322) and reflected ray 30° (dx=186, dy=323) from the normal; fronts perpendicular to the rays (dot product about 0); arrows toward and away from the barrier. Physics correct. Defects: card ITEM-6118-16-022 says "incidence angle of 30°" but neither angle nor "i" and "r" is labelled; no label on the wavefront lines; the central V-shaped front mixes incident and reflected parts without explanation. The syllabus phrase "wave fronts reflect at the same angle to the surface" is never shown (angle between front and barrier is 30° too, not marked).

**16.14 [S3] Notes: angle to surface vs normal.** Notes "Describe reflected wavefronts" measure angles to the normal and use rays; the syllabus statement is about wave fronts at the same angle to the surface. The notes never state that the angle between the wavefront and the barrier equals the angle of incidence, so a learner reading an exam question in the syllabus wording is unprepared.

**16.15 [S3] Prompt without data.** ITEM-6118-16-008-SYNTH "Explain how a displacement-distance graph and a displacement-time graph give different wave quantities." No graph is supplied, so it is a recall card labelled Analyse. The mark scheme needs both graphs to read wavelength vs period; amplitude is common to both and not mentioned.

**16.16 [S3] Boilerplate guidance.** For example ITEM-6118-16-018-SYNTH: "Combine the linked ideas and explain the reason: Link the front geometry to direction: circular fronts spread radially from a point. (1 mark)." The answer contains "Link"; "Plane fronts travel perpendicular to parallel straight lines" is wrong wording (fronts are the lines; the wave travels perpendicular to them). ITEM-6118-16-014-SYNTH "Therefore c = λ/T" would also be marked by a rubric that does not demand the unit.

**16.17 [S4] Figure figure-6118-16-04.png (refraction).** Viewed. Incident ray 30° to the normal (dx=124, dy=216), refracted ray about 14.5° (dx=64, dy=247), bends toward the normal into shallower water, fronts perpendicular to the rays, spacing smaller below the boundary. Physics correct. The ratio sin30/sin14.5 = 2 implies λ halves, but front spacing in the picture changes only by about 1.7 (pixel estimate, approximate), so it is only qualitatively consistent. The labels "Deeper: longer spacing" and "Shallower: shorter spacing" are placed on top of the ray start and the normal, so they are hard to read; the boundary is unlabelled; angles are not marked.

**16.18 [S4] Bloom.** The four Draw cards (16-019 to 16-023) are labelled "Analyse" (a drawing recall task is Apply), AO "B". Marking guidance for these does not credit marking the source or labelling the wavelength.

**16.19 [S4] Syllabus-verbatim definitions.** Cards 16-011 ("Period is the time taken for one complete oscillation") and 16-017 ("a line joining adjacent points in the same phase") match the syllabus wording (8-word hits). This is acceptable for definitions required by the syllabus. "adjacent points in the same phase" is itself ambiguous (nearest points that are in phase).

**16.20 [S4] Wording.** short_answer (e) "Calculate period at 8 Hz." should read "for a frequency of 8 Hz". Notes "Use hertz and metres for m/s." is clumsy.

Figures: figure-6118-16-02.png (plane wavefronts) viewed: three equally spaced parallel lines, arrow perpendicular, correct (S4: the arrow shaft overruns both outer lines and the label "Propagation" sits on the shaft). practical-6118-16.png viewed: axes Period / s and Wavelength / cm, data correct, straight line.

Numerics recomputed for topic 16: 5x0.040=0.20 m/s; 10 cycles/2 s = 5 Hz; 1/0.25=4 Hz; 1/0.20=5 Hz; λ/T = 0.060/0.20 = 0.30 m/s (and 0.20x0.060 = 0.012, wrong); 8x0.025=0.20; 1/8=0.125; 6x0.050=0.30; 2x340=680; practical gradient 20 cm/s = 0.20 m/s (notes say 20 m/s, wrong).

### Verdict topic 16: ready after fixes
One answer-key error (16.1, unit wrong by a factor of 100). All other physics correct, diagrams correct in geometry. Needs fixing of 16.1, and the figure and wording items.

---------------------------------------------------------------------
## Counts by severity
| Topic | S1 | S2 | S3 | S4 | Total |
|---|---|---|---|---|---|
| 13 | 0 | 3 | 9 | 1 | 13 |
| 14 | 1 | 3 | 10 | 2 | 16 |
| 15 | 1 | 1 | 10 | 2 | 14 |
| 16 | 1 | 0 | 15 | 4 | 20 |

Exact tallies from the lists above:
- Topic 13: S1=0, S2=3 (13.1-13.3), S3=9 (13.4-13.12), S4=1 (13.13). Total 13.
- Topic 14: S1=1 (14.1), S2=3 (14.2-14.4), S3=10 (14.5-14.14), S4=2 (14.15-14.16). Total 16.
- Topic 15: S1=1 (15.1), S2=1 (15.2), S3=10 (15.3-15.12), S4=2 (15.13-15.14). Total 14.
- Topic 16: S1=1 (16.1), S2=0, S3=15 (16.2-16.16), S4=4 (16.17-16.20). Total 20.

## What I checked
- All four notes files in full, every definition, equation, unit and worked example, recomputed with python.
- Every item in the four flashcard JSON files: 18, 23, 20 and 27 items respectively, including all 12 questions in each MC set (48), solved blind before reading the key, all four short_answer items, all four practical_task items.
- JSON text vs notes text (identical for MC/short_answer/practical).
- All figures referenced by the four topics: figure-6118-14-01.png, figure-6118-16-01 to -04.png, practical-6118-13 to -16.png (viewed; ray angles measured by pixel geometry for 16-03 and 16-04).
- Syllabus text for 3.2.1 to 3.3.4 and 4.1 and the practical list (pdftotext).
- 8-word-run overlap against all 203 held NSSCO (New) paper and report PDFs.

## What I could NOT check
- Examiner-report phrasing for these specific topics beyond the 8-word overlap check; GAPS.md says marking evidence is partial, so I could not confirm whether the real mark schemes accept "J/(kg °C)", "330 m/s" or the specific molecular wording.
- The work/ topic claim files, contract.json and authored.py were not read, so claim sourcing (claim_ids) is unchecked.
- Pixel-based estimates of front spacing in figure 16-04 are approximate.
- Readability level (Grade 10-11 Namibian learners) was judged by me, not tested with learners.
