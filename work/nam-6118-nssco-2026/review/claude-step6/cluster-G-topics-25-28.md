# Cluster G review: NSSCO Physics 6118, topics 25, 26, 27, 28

Reviewer: independent physics reviewer. Review only; no repository file was edited. Files read: notes/25-28 (.md), flashcards/25-28 (.json), all notes figures for these topics, syllabus PDF (text), topic work_order/contract files (skimmed).

Headline: every numerical example, every MC key and every worked answer recomputed correctly (no S1). The problems are systemic (template marking guidance, template "Link ..." answers, identical MC key pattern, duplicated figures, thin coverage of a few syllabus statements) plus specific S2 gaps listed below.

Severity tags are written [S1]..[S4] so they can be counted with grep.

Systemic facts verified by script:
- MC key string is `ADCBADCBADCB` in ALL FOUR topics (25, 26, 27, 28). Each letter appears exactly 3 times, strictly periodic.
- All numerics recomputed with python: all correct (see "Checked" at end).
- 8-word shingle search of all notes and card text against the 24 exam-paper/examiner-report PDFs under Question Banks: only hits are syllabus phrases ("against time for a simple a.c. generator", "atoms of the same element with the same"). No copying from papers or reports found.

---------------------------------------------------------------------
## TOPIC 25 Magnets, electromagnets and motors
---------------------------------------------------------------------

25.1 [S2] Location: all 29 flashcards, marking_guidance. Quoted: "Property or unit: They repel. (1 mark)." (25-001); "Combine the linked ideas and explain the reason: Link the bar to curved external lines from north toward south. (1 mark)." (25-007); "Method step: Move a plotting compass ..." (25-006); "Cause and effect: ..." (25-002, 010, 020-024, 027, 028); "Identify the error and give the correct distinction: ..." (25-029); "Diagram/graph feature: ..." (25-008, 009, 013, 014, 017). Problem: the guidance is a generic label plus a verbatim copy of the canonical answer clause. It lists no accepted alternatives, no "do not accept", no common errors, no part-marks logic. "Property or unit" is meaningless for a card that has no unit. A teacher or auto-marker cannot mark a different correct wording. Fix: write real guidance per card (e.g. 25-001: "1 mark: repel/repulsion/push apart. Do not accept 'attract'."; 25-005: "accept nickel, cobalt or both; accept any two of Ni/Co/their alloys").

25.2 [S2] Location: SYNTH cards 25-007, 25-012, 25-019, 25-026, canonical_answer. Quoted: "Link the bar to curved external lines from north toward south."; "Link a straight wire to concentric circular field lines."; "Link each turn to an additional pair of side forces."; "Link the split ring to current reversal each half-turn." These are instructions to the learner/author, not model answers (template text left in the answer). 25-007 also never explains WHY the fields differ (horseshoe poles are close and face each other). Fix: write full sentences, e.g. 25-007: "A bar magnet has curved field lines looping from N round to S outside the magnet. In a horseshoe magnet the two poles face each other across a narrow gap, so between them the lines are straight, parallel and equally spaced (uniform field)."

25.3 [S2] Location: ITEM-6118-25-010 (bell) and notes section "describe and explain the difference between the design and use of permanent magnets and electromagnets". Quoted: "Its magnetic attraction can be turned on and off by changing current. A soft-iron core can lose much of its magnetisation when switched off, permitting the armature to return." Notes: "A bell needs repeated switching, making an electromagnet useful." Problem: syllabus 5.6 names the bell as the worked example. Neither notes nor card explains the self-interrupting (make-and-break) circuit: current -> coil magnetises -> armature pulled to coil -> hammer strikes gong and contact breaks -> current stops, core demagnetises -> spring returns armature, contact remakes -> repeats. "Armature" is used without being defined. The card also does not compare with a permanent magnet (a permanent magnet cannot be switched off), which is the syllabus objective ("difference"). Fix: add bell mechanism to notes; mark scheme: electromagnet on/off with current (1), contact breaks as armature moves so current stops and armature springs back, repeating (1); permanent magnet cannot be switched off (accept as alternative).

25.4 [S2] Location: ITEM-6118-25-P01 key pattern. Keys 1-12 = A D C B A D C B A D C B, repeating period 4. A learner who has answered 4 questions can predict the rest. Fix: reorder options so keys are irregular (e.g. A C B D B A D C C A D B) and no letter more than 4 times, no run/period.

25.5 [S2] Location: ITEM-6118-25-P03 (16-mark practical), part (c). Prompt requires: "Include the arrangement, five operational measurement steps, controls, a table and how the data would support a conclusion. [8]". Marking guidance allocates: method 5 + table 1 + graph 1 + conclusion 1 = 8, and says "Controls and safety support the method; the planning allocation totals eight marks." So controls, which the question explicitly demands, carry no mark, and "arrangement" has no explicit mark. A candidate who gives perfect controls but 4 steps cannot be credited consistently. Also "Graph: an appropriate relationship plotted with named axes (1)" inside the planning part is unexplained (a graph of what, drawn when?). Fix: e.g. steps 4, controls 1-2, table 1, conclusion 1; or remove "controls" from the prompt.

25.6 [S2] Location: notes (6.1 and 5.7.1.2 sections) and cards 25-002, MC Q2 feedback. Quoted: "differently oriented regions largely cancel", "dipoles or domains", "That is not domain alignment", "remanence", "Saturation and heating", "turning couple". The syllabus term is "molecular magnets / alignment of magnetic dipoles". "Domain", "remanence", "saturation" and "couple" are not syllabus terms, are not defined for a Grade 10-11 learner, and are not flagged as extension. "Couple" is used as the key word in cards 25-020, 22, 24 canonical answers. Fix: say "tiny magnets (molecular magnets) point in different directions and cancel; in a magnetised sample they line up", "two equal opposite forces on opposite sides give a turning effect (moment)"; delete "remanence/saturation" or flag "extension, not examined".

25.7 [S2] Location: figure-6118-25-05.png used by ITEM-6118-25-012 canonical answer ("Explain using a field diagram how straight-wire and solenoid field patterns differ."). The image is a copy of figure 04 (single wire cross-section, three circles) with the title "Wire cross-section; solenoid diagram follows". It shows no solenoid. The card's answer figure therefore only illustrates half of the comparison. Fix: use figure 05 = solenoid diagram (figure 06 content) or a side-by-side figure.

25.8 [S3] Location: figure-6118-25-02.png (ITEM-25-007). Identical to figure 01 (bar magnet) except the title "Bar pattern; compare with horseshoe gap below". There is no horseshoe below. Card asks to compare bar vs horseshoe; the figure shows only the bar. Fix: combine figures 01 and 03 in one panel or retitle.

25.9 [S3] Location: figure-6118-25-01/02.png. All field lines converge to a single point at each end of the rectangle (the poles drawn as points). Direction is correct (N left -> S right outside, red arrow S->N inside) and spacing is denser near the ends, but lines are 3 above/3 below only, all spaced evenly in apex height; adequate but schematic. Title says "schematic closed field pattern" (acceptable). No error; note the red internal arrow is unlabelled (no legend saying "inside the magnet").

25.10 [S3] Location: figure-6118-25-03.png (horseshoe). The "N" and "S" labels float above and outside the arms; only three field lines drawn, all in the top third of the gap; lower two thirds of the U are empty; no pole faces drawn. Directions correct (N face left -> S face right). Fix: lines evenly across the gap, labels next to the faces.

25.11 [S3] Location: figure-6118-25-04.png (and 05). Arrowheads are malformed: each circle has one tiny arrowhead drawn as a skewed chord off the circle on the right-hand side, not tangent. The current-out-of-page dot is displaced from the circle centre (dot at ~(502,394), centre ~(512,383)). Direction (anticlockwise, arrow upward on the right) is correct. Fix: tangent arrowheads on each circle, dot centred.

25.12 [S3] Location: figure-6118-25-06.png (solenoid). Coil is drawn as seven vertical grey lines (no wire loops, no current direction/dots and crosses); "S" and "N" are placed far below and outside the ends. Interior lines point right, exterior return lines point left (N->S), consistent with the card, but the N end cannot be derived from the figure because the current direction is not shown, which is what the syllabus asks (right-hand grip rule). Fix: draw current direction in the turns and place N/S at the ends.

25.13 [S3] Location: figure-6118-25-07.png (ITEM-25-017). Directions are correct (B right, current out of page, force up) but "B right" and "Current out of page" labels are placed in the bottom corners far from the items; the blue horizontal line (the B arrow) is drawn as a wire-like line; the current dot sits left-below the force arrow base. A learner could read the horizontal line as the wire. Fix: label each symbol in place.

25.14 [S3] Location: practical-6118-25.png. Title is clipped ("...at fixed geom"). The "fitted line" is just the data points joined; axes start at ~0.08 A and ~0.25 N so the non-zero intercept (0.1 N at 0 A) that the canonical answer talks about ("without forcing the line through zero") cannot be seen. Fix: extend line to the y-axis, show origin.

25.15 [S3] Location: P03 data table vs MC question 12. Table: 0.2 A -> 0.5 N; 0.4 A -> 0.9 N (intercept 0.1 N at 0 A, slope exactly 2 N/A: recomputed, all five successive gradients = 2.0). MC12 invents different readings "0.4 N at 0.2 A and 0.8 N at 0.4 A" (direct proportionality). Same topic, same quantity, two incompatible practice data sets, one proportional and one not. Also an electromagnet with a soft-iron core giving 0.1 N pull at zero current is physically implausible, and real pull is not linear in current (roughly rises faster than linearly until saturation). The data are correctly labelled "invented, idealised" (good) but the 0.1 N at zero current is unexplained. Fix: use one data set; either pass through the origin or add "residual magnetism" explanation.

25.16 [S3] Location: MC12 stem. Quoted: "What is the secant gradient?" "Secant" is not NSSCO language; "gradient of the line" suffices. Also "A short empirical test" is jargon.

25.17 [S3] Location: MC11. Quoted: "More turns are added but current falls. What is needed for the simple turns comparison?" Stem is unclear ("simple turns comparison"), option D "Assume torque must increase by any amount" and A "Ignore winding resistance" are implausible/unclear. Correct option C is also the longest (51 vs 28/19/44). It tests control of variables, not a syllabus statement in 5.7.1.2. Fix: "A learner wants to test whether more turns give a bigger turning effect. Which must stay the same?"

25.18 [S3] Location: MC distractors. Weak/implausible: Q1 D "Lose all field by approaching"; Q2 B "The sample loses every atom", C "Electrons become magnetic north only"; Q3 A "Glass and plastic", B "Water and air"; Q4 C "It is a permanent electrical source", D "It has no magnetic response"; Q5 B, C; Q6 B "Stores fuel"; Q7 A "Only a disconnected wire", D "No input"; Q10 B "It becomes an electric field by definition"; Q11 D. Correct answer is longest in Q4, Q8, Q11. Several stems cue the key (Q7 "Mechanical work" is the only physical-input option).

25.19 [S3] Location: MC worked feedback (canonical_answer of P01), several lines do not explain the wrong option. Quoted: Q4 D "Its response is the useful feature."; Q6 B "It is an electrical contact arrangement."; Q3 D "They do not show the same strong ferromagnetism." (copper/aluminium are non-magnetic, not "weaker"); Q8 A "Unmagnetised iron can be attracted to either." (OK) but Q8 B restates the question. Fix: one clear reason per wrong option. Q3D wrong: copper and aluminium show no ferromagnetism at all.

25.20 [S3] Location: near-duplicate cards. 25-019 vs 25-021 (both "more turns, fixed current/geometry, more torque"; same two ideas); 25-024 vs 25-027 vs P02(d) (split ring/commutator reverses current each half-turn); 25-026 (second half) vs 25-028 (soft-iron core purpose); 25-001 vs MC1 vs P02(a) (like poles repel); 25-005 vs P02(b) (nickel). Intentional_duplicate_group is None for all. Fix: merge or differentiate.

25.21 [S3] Location: Bloom/difficulty labels. Cards 25-007, 012, 019, 026: item "Analyse", difficulty 5, 2 marks, answer is two statements; 25-008, 009, 013, 014, 017 ("Draw", standard textbook sketch) labelled "Analyse", AO B; 25-006/015/016/018/025 recall-of-method labelled "Apply". Plausible to teachers but over-rated; difficulty 5 for a 2-mark recall-level answer is misleading.

25.22 [S3] Location: ITEM-25-006, 016, 018, 025 canonical answers. 006: no mention of placing the magnet on paper, marking the compass needle ends with dots and joining the dots (what examiners expect); 016: no way to measure attraction (e.g. paper clips picked up) and no expected result (iron loses its magnetism, steel keeps it) although objective asks to "show the difference"; 018: no named apparatus; 025: no indicated meter type. Single mark for a multi-part sentence in each.

25.23 [S3] Location: ITEM-25-005. "State two ferromagnetic elements other than iron." Answer "Nickel and cobalt" for 1 mark; marking guidance elsewhere (P02(b)) says "nickel or cobalt". Gadolinium is also ferromagnetic below ~20 C, so "elements" is not unique; the prompt should say "from the syllabus list" and the tariff should be "1 mark for both".

25.24 [S3] Location: ITEM-25-011. "A nearby compass changes direction when current is switched on and reverses its current-related deflection when current reverses." Phrase "current-related deflection" is awkward; two observations in a 1-mark State card.

25.25 [S3] Location: ITEM-25-029 and cards 25-012 etc. 25-029 prompt "does not prove it is permanent" is partly cued by the stem; second mark bundles two ideas (repulsion test + retention). Minor.

25.26 [S3] Location: notes, section "state that the Earth has bar-magnet like properties...". Missing: Earth's geographic north is a magnetic SOUTH pole (hence the north-seeking pole points north). Without it the convention in the syllabus reads as a paradox. Notes say "magnetic and geographic directions are not identical everywhere" and "No current local compass correction is assumed here" (vague).

25.27 [S3] Location: notes headings and wording. "Original graphical solution" appears 7 times with no caption saying what each figure shows; "Practice task with worked feedback" appears 4 times; sentences like "in the school account", "Original structured practice", "under the stated practice values", "Distinguish a magnetic pole from an electric charge sign" read as generation artefacts, not learner English. "Draw a bar-magnet field", "Explain how turns affect coil torque" headings are card titles, not teaching headings. Figures are not numbered or referred to in the text.

25.28 [S3] Location: ITEM-6118-25-P02 prompt. "Answer the parts with working and units where needed." appears though nothing needs working or units. Command word "State" on an 8-mark mixed task; (a) and (b) are trivial recall. Marking guidance (c)-(e) are fine, and sums to 8 (1+1+2+2+2).

25.29 [S3] Location: notes MC placement. The first "Practice task" MC (under 5.6) contains 5.7 questions (generator, commutator, force direction, turns/current); items 9-12 are not "5.6" content.

25.30 [S4] Location: MC9 "Current is out of the page and field rightward." Should say "conventional current". Key (A, upward) verified: F ∝ I (out of page, +z) x B (right, +x) = +y, up. Correct.

25.31 [S4] Location: ITEM-25-003 "State why a freely suspended magnet can serve as a compass." Answer fine; does not say the north pole points to geographic north.

25.32 [S4] Location: P03 "Calculate its gradient" canonical "1 ÷ 0.5 = 2 N/A" does not name the two points used (e.g. (0.1, 0.3) and (0.6, 1.3)); marking asks for a "visible wide construction" so the model answer should show it.

---------------------------------------------------------------------
## TOPIC 26 Induction, generators and transformers
---------------------------------------------------------------------

26.1 [S2] Location: all 17 flashcards, marking_guidance. Same defect as 25.1. Mislabels: 26-007 (role of slip rings) "Method step: ..."; 26-012 (how a transformer transfers energy) "Method step: ..."; 26-017 "Method step: ..."; 26-002 "Property or unit: Move the magnet faster relative to the coil. (1 mark)."; 26-011 "Method step". Guidance is a copy of the answer; no alternatives (see 26.8).

26.2 [S2] Location: ITEM-6118-26-004 and 26-008 canonical_answer. Quoted: "Link both to periodic change in magnetic linkage through a coil."; "Link faster rotation to a shorter output period and higher frequency." Template residue; 26-004 also uses "magnetic linkage" (not NSSCO wording: "changing magnetic field/ magnetic field cutting").

26.3 [S2] Location: ITEM-6118-26-P01 keys A D C B A D C B A D C B. Predictable pattern (see 25.4).

26.4 [S2] Location: ITEM-6118-26-009 and 26-010 marking_guidance. 009: "Put time / s horizontally and voltage / V vertically. (1 mark)" and "Draw two sinusoidal cycles spanning +2 V to -2 V about zero. (1 mark)". There is no mark for the period of 1 s (two complete cycles in 0-2 s), which is the learning point; a trace with the wrong period still scores. 010: mark 1 bundles axes, 4 V peak and 0.5 s period; mark 2 "It has twice as many cycles in the same time interval." is a statement, not a drawing feature. Fix: 009: axes labelled with units (1), amplitude 2 V and negative half (1), period 1 s/two cycles (1)... and keep total 2 by merging; 010: peak 4 V (1), period 0.5 s / four cycles (1).

26.5 [S2] Location: ITEM-6118-26-017 and notes section "Namibia-context generation and transmission". Syllabus: "describe how electricity is generated and transmitted in Namibia and how this process requires the use of transformers". The card has no Namibian content at all ("A step-up stage supports high-voltage transfer from generation, while step-down substations provide appropriate distribution and consumer voltages."), prompt uses the awkward "Namibia-context". Notes name only Ruacana (hydro) and cite an ECB September 2025 licence list ("identifies Ruacana as hydro"). I could not fetch the PDF (TLS certificate error), so this claim is UNVERIFIED. Notes give no transmission voltages/stages (and the notes deliberately avoid numbers; acceptable) but also do not mention that Namibia imports power or other generation types as an assessed fact. Fix: add a Namibia-specific mark (e.g. "name one Namibian generating station/type and where power goes") and verify the ECB reference.

26.6 [S2] Location: ITEM-6118-26-P03 (c) marking_guidance. Same defect as 25.5: prompt demands "controls" but guidance gives them no marks ("Controls and safety support the method; the planning allocation totals eight marks.") and an unexplained "Graph: an appropriate relationship plotted with named axes (1)" inside the planning mark list.

26.7 [S2] Location: notes sections "describe the structure and principle of operation of a simple iron-cored transformer" and "state the advantages of high voltage transmission". Quoted: "laminations reduce unwanted circulating-current heating in a real design"; "The familiar line-loss relation varies with the square of current". Eddy currents/laminations and the I^2R relation are outside the 2018 syllabus (not in 5.7.2.3) and are not flagged as extension. Also "magnetic linkage", "transient", "open-circuit", "terminal convention", "unloaded idealised traces" are unexplained jargon for Grade 10-11. Fix: remove or flag "extension: not examined"; use "changing magnetic field in the core".

26.8 [S3] Location: ITEM-26-002, 26-015, 26-001. 26-002 "State one change that can increase a magnet-coil induced e.m.f." accepts only "Move the magnet faster"; stronger magnet and more turns (the other syllabus factors, in the notes) are equally correct but not credited in guidance. 26-015 accepts one benefit/one drawback only (alternatives: no visual pollution, safer from storms/vandals, lower line losses; drawbacks: expensive, hard to repair, excavation disturbing habitat). 26-001: "meter-connected coil" - should be sensitive/centre-zero galvanometer; "compare ... with the stationary case" is OK.

26.9 [S3] Location: figures figure-6118-26-01.png, -02.png, -03.png. The three files are byte-identical in content: one plot with both traces (2 V/1 s and 4 V/0.5 s). Card 26-009 (draw 2 V, 1 s only) therefore shows the answer to 26-010 as well, and 26-010's answer figure is the same as 26-008's. Directions/axes are correct (time / s, voltage / V, peaks 2 V and 4 V, periods 1 s and 0.5 s: verified from the plot); legend "Original rate / Double rate" is clear. Fix: three distinct figures (single trace, comparison).

26.10 [S3] Location: practical-6118-26.png. Plot joins the data points; no fitted line extending to the origin; y-axis starts near 0.8 V and x near 15 turns so the origin is off the plot while the notes say "A straight near-origin ... line supports the ideal turns relation". Title nearly touches the plot edge (not clipped).

26.11 [S3] Location: P03 data. Six points exactly on a perfect line (0.05 V per turn); no scatter, all values are integers. For a graph-drawing/fitting exercise, real scatter is needed to make "line of best fit" and "accurate points" meaningful. Data are labelled "invented, idealised" (good). Gradient 5/100 = 0.05 V/turn recomputed correct; note "the slope is Vp/Np" is right but Vp and Np are not given in the task, so the learner cannot check it.

26.12 [S3] Location: MC distractors, topic 26. Weak: Q1 B/C/D ("The coil becomes a cell"); Q2 B "Only the coil's weight", C "Energy conservation"; Q3 B, D; Q4 A, C, D; Q5 B, C, D; Q6 A "No excavation needed", B "Guaranteed zero repair cost", C "No need for insulation"; Q7 A/B/D; Q10 C "It becomes amplitude" (nonsense); Q11 A "Charge is created", B "The coil loses its turns". Key is the longest option in Q1 (55 chars vs 49/38/26), Q5 ("To lower current and line heating", the only option with a mechanism) and Q11. Q6 correct option is the only non-absurd one.

26.13 [S3] Location: MC wording. Q1 "What is expected after transients?" (transients undefined). Q10 canonical feedback for key D reads "D: Frequency doubles." (does not say period halves); feedback for A "This reverses the frequency relation." obscure. Q12 stem "At fixed primary conditions" jargon. Q9/Q8/Q12 correct (verified: 4 V, 4 A, twice).

26.14 [S3] Location: repetition between notes and cards. Notes worked example "A 12 V, 0.50 A primary input is 6 W. At an ideal 3 V secondary output, current is 2 A." is identical in numbers to card 26-016 "Vp = 12 V, Ip = 0.50 A and Vs = 3 V" (answer 2 A); notes "primary 100 turns at 6 V and secondary 50 turns ... 3 V". Card 26-013 (12 V, 240 -> 60 turns -> 3 V), P02(d), P02(e), MC8, MC9, MC12 all repeat the same 3-step recipe. The card becomes recall, not calculation. Fix: change card numbers.

26.15 [S3] Location: ITEM-26-008 canonical and notes. 008 says "larger voltage amplitude" while 26-010 and figure state it doubles; notes say "increases". Syllabus requires effect on the graph: higher peak AND shorter period. OK but inconsistent precision (S3/S4).

26.16 [S3] Location: ITEM-26-014 "State the main energy advantage of high-voltage transmission at fixed transmitted power." "energy advantage" is ambiguous (energy saved? power loss?). Answer correct. Wording: "State why high-voltage transmission reduces power loss in the cables."

26.17 [S3] Location: Bloom/difficulty. 26-004, 26-008 "Analyse", diff 5, 2 marks; 26-009/010 "Draw" labelled Analyse; 26-001, 005-007, 011, 012, 017 describe/recall labelled "Apply". Command word "State" on the 8-mark P02 though parts include Calculate and Explain.

26.18 [S3] Location: notes headings and wording. Same as 25.27 ("Original graphical solution" x3; "Practice task with worked feedback" x3; headings like "Sketch the alternating output voltage" appear as separate teaching headings; "Use an invented model with peak 2 V and period 1 s over 0-2 s" appears in a statement section; sentences "does not mean ... ", "in the school model").

26.19 [S3] Location: notes section "state that the direction of induced current is such as to oppose the change". The explanation covers approach only; withdrawing a N pole ("the induced face changes so it opposes withdrawal") is left unexplained (near face becomes S). Also "The opposing effect is consistent with the need for energy input" without saying why. 26-003 card only tests approach.

26.20 [S4] Location: ITEM-26-P02 prompt "Answer the parts with working and units where needed." boilerplate. P02 marks 1+1+2+2+2 = 8 correct; (a) marking "continuous slip rings" vs canonical "Slip rings" (accept either).

26.21 [S4] Location: MC order in notes. The MC "Practice task" under 5.7.2 mixes 5.7.2.1-5.7.2.3. Fine.

---------------------------------------------------------------------
## TOPIC 27 Atomic structure and isotopes
---------------------------------------------------------------------

27.1 [S2] Location: all 18 flashcards, marking_guidance. Same boilerplate defect (25.1). Specific mislabels: 27-004 "Diagram/graph feature: Place A = 31 at upper left and Z = 15 at lower left of P. (1 mark)." (nothing is drawn); 27-006 and 27-007 "Equation, substitution and final result: A remains 32 because the total nucleon count is unchanged. (1 mark)" (no equation or substitution); 27-017 and 27-018 "Identify the error and give the correct distinction". No credit rules for alternatives (e.g. 27-002 "number of protons" without "in the nucleus"; 27-008 "same number of protons, different number of neutrons" should be accepted).

27.2 [S2] Location: ITEM-6118-27-005 and 27-009 canonical_answer. Quoted: "Link alpha emission to removal of A = 4 and Z = 2."; "Link tracing to detecting the location of a moving labelled substance." Template residue (see 25.2).

27.3 [S2] Location: ITEM-6118-27-P01 keys A D C B A D C B A D C B. Predictable pattern.

27.4 [S2] Location: notes section "use the nuclide notation in equations to show alpha and beta decay" and "Represent beta-minus decay using nuclear numbers". Quoted: "A beta-minus process also emits an antineutrino, omitted from that simplified display"; "Including the antineutrino completes the particle account". The antineutrino is not in the 2018 syllabus and is not flagged as out of scope; it is also not needed (equations in 6.1.1 only show A and Z). Also unnecessary: "Beta-minus decay converts a neutron into a proton with an emitted electron" is acceptable but should stay unelaborated. Fix: delete the antineutrino sentences or flag "not examined".

27.5 [S2] Location: syllabus 6.1.1 "use the term nuclide and nuclide notation" and notes/cards. Neither notes nor cards define "nuclide" (a particular type of nucleus with given A and Z); the word appears only in passing ("for most nuclides"). Also no card/notes statement of the relative charge and mass of proton, neutron and electron beyond "Protons have positive charge and neutrons have no net electric charge". The syllabus composition objective is covered by only card 27-001 ("Define a nucleon"), which tests a term outside the objective wording. Fix: add a nuclide definition and a charge/mass table or card.

27.6 [S3] Location: ITEM-6118-27-004. "Draw the nuclide notation for phosphorus with 15 protons and 16 neutrons." Notation cannot be "drawn"; command word/label Draw/Analyse with AO B for a 2-mark recall-plus-subtraction task. Mark 2 ("The notation is 31/15 P") is the same as mark 1 restated. Fix: "Write the nuclide notation ..." Apply; marks: A = 31 (1), Z = 15 (1).

27.7 [S3] Location: ITEM-27-010 canonical. "The remaining fraction compared with a calibrated starting model indicates elapsed time." "Calibrated starting model" is jargon. The standard idea is missing: living things take in carbon-14 so the proportion in them is constant; after death no new C-14 is taken in and the C-14 decays with a known half-life (5730 years, never given in notes or cards), so the measured activity/ratio shows how many half-lives have passed. The notes have no worked dating calculation.

27.8 [S3] Location: near-duplicates. 27-011 (how a tracer reveals movement) vs 27-013 (tracer locates a leak): second mark of 013 is a specific case of 011's second mark; 27-009 repeats both leak tracing and sterilisation content; 27-017 vs MC8 vs notes ("A = 39, Z = 19"); 27-006 vs MC9 vs notes (226/88 -> 222/86 used in notes "original practice choice" and in the card with identical numbers); 27-007 vs notes (P-32 -> S-32, identical numbers); 27-002/003 vs P02(a)(b); 27-008 vs P02(c) vs MC11.

27.9 [S3] Location: cueing. 27-012 prompt "Explain why radiation used to damage cancerous cells also needs careful targeting" gives away "healthy cells also affected"; 27-016 "benefit of penetrating radiation for sterilising suitable packaged equipment" gives away "reach through packaging"; 27-017/018 stems state the error. 27-014 answer says "suitable incident radiation" without naming beta (notes name beta for thin sheets), vague.

27.10 [S3] Location: ITEM-27-015. "Controlled fission releases energy that heats a working fluid. The fluid drives a turbine coupled to a generator." "Working fluid" is jargon; no steam/water, no reference to nuclear fuel (uranium) or the chain reaction; overlaps topic 9 (energy sources) where nuclide equations are out of scope. Fine physically.

27.11 [S3] Location: MC distractors, topic 27. Weak/implausible: Q1 B/C/D; Q2 B "The sample's temperature", C "number of atoms in the sample"; Q4 A/C/D; Q5 B/C/D ("Its charge must become zero instantly", "The detector must create the leak"); Q6 B/C; Q7 A "A shadow on a wall", B "An arbitrary vacuum gap", D; Q12 A "Zero". Key is longest option in Q4, Q5 (43 vs 36/40/36). Feedback weak: Q7 "D: The required clock is not established."; Q6 "C: Detector and source are different."; Q5 "C: That is not the detection principle."

27.12 [S3] Location: MC10 stem "Beta-minus decay starts with A = 14 and Z = 6. What daughter results?" Key D (A = 14, Z = 7) correct; distractor B (A = 14, Z = 5) feedback "wrong beta-minus charge direction" fine. Q9 key A (206, 82), Q8 key B (12), Q12 key B (two half-lives): all verified correct.

27.13 [S3] Location: topic coverage. No ITEM of type practical_task in topic 27 (and none in 28): types are 18 flashcards, 1 MC set, 1 short_answer. 25 and 26 each have the 16-mark practical. I could not confirm from contract.json that a practical is required for 27/28; reported as a coverage difference. Also no card on radiology, on same chemical behaviour of isotopes, on neutral atom electron count (although notes say it), or on Z in a neutral atom.

27.14 [S3] Location: notes headings and wording. Same artefacts as 25.27: "Practice task with worked feedback" x2, "Distinguishing the ideas", sentences such as "gives the school beta-number balance", "using the original practice choice 226/88 Ra", "Treating A as neutron count adds the protons twice when reconstructing the nucleus" (confusing), "Electrons occupy the surrounding atomic region rather than being ordinary constituent nucleons" (awkward), "not a rule that radiation recognises disease automatically". Section "The atomic nucleus" has no syllabus statement as title while other sections use verbatim syllabus text.

27.15 [S3] Location: ITEM-27-001 "Define a nucleon." The syllabus term is nucleon number; fine, but combined with 27.5 the nucleus-composition statement lacks a card. Also 27-001/002/003 define by single clause, acceptable.

27.16 [S3] Location: P02 prompt "Answer the parts with working and units where needed." (no units relevant); (d)/(e) marking "One mark for each correctly reduced number" fine. Sum 1+1+2+2+2 = 8 correct. Command word "State".

27.17 [S4] Location: difficulty/Bloom. 27-005, 27-009 "Analyse", diff 5 for 2 marks.

27.18 [S4] Location: notes. Section "use the nuclide notation..." text: "A beta-minus electron is represented 0/-1 e" fine; "²¹⁰₈₄Po -> ²⁰⁶₈₂Pb + ⁴₂He" verified (84-2 = 82; 210-4 = 206), "¹⁴₆C -> ¹⁴₇N + ⁰₋₁e" correct, "³²₁₅P -> ³²₁₆S" correct, "²²⁶₈₈Ra -> ²²²₈₆Rn" correct, "A = 39, Z = 19 -> 20 neutrons" correct, "15 protons + 16 neutrons -> A = 31" correct.

---------------------------------------------------------------------
## TOPIC 28 Radioactivity and half-life
---------------------------------------------------------------------

28.1 [S2] Location: all 20 flashcards, marking_guidance. Same defect (25.1). Mislabels: 28-004/005/006 (how a cloud chamber/G-M/film works) "Method step: ..."; 28-002 "Property or unit: Cosmic radiation and radioactive materials in rocks or soil. (1 mark)."; 28-020 "Equation, substitution and final result: The source rate falls by a factor of two over each 6 min interval. (1 mark)" (no equation); 28-001 "Method step". No alternatives accepted (e.g. 28-002: radon, cosmic rays, rocks, buildings, food, medical, fallout).

28.2 [S2] Location: ITEM-6118-28-003, 28-012, 28-016 canonical_answer. Quoted: "Link both to ionisation caused by radiation interactions."; "Link alpha and beta-minus charges to field-dependent deflection."; "Link element identity to Z in the balanced equation." Template residue. 28-008 prompt "Explain the link between alpha and gamma's typical ionising and penetrating effects." is ungrammatical and omits beta.

28.3 [S2] Location: ITEM-6118-28-P01 keys A D C B A D C B A D C B. Predictable pattern.

28.4 [S2] Location: ITEM-6118-28-P01 Q5. Stem: "What is predictable for one unstable nucleus?" Key A: "Its decay is random rather than exactly scheduled". The key says what is NOT predictable; a learner who reads "predictable" is led to reject it. Options C "It must decay at one half-life" and D "It cannot decay before one half-life" are also unclear. Also the longest option (52 chars). Fix stem: "Which statement about ONE unstable nucleus is correct?" with key "Its decay time cannot be predicted exactly".

28.5 [S2] Location: ITEM-6118-28-009. Canonical: "Its charge and interactions transfer energy densely to nearby material. It loses its energy over a short path and is stopped relatively readily." "Its charge and interactions transfer energy" is circular (explains strong ionisation by "interactions"). Expected: alpha particles are relatively large/heavy and have +2 charge, so they ionise many atoms along a short track, losing energy quickly. Also for 28-008 "Gamma interacts less frequently along a path" lacks reason (no charge, no mass).

28.6 [S2] Location: notes sections "describe radioactive emission" and "describe their deflection..."; cards 28-010, 28-013, 28-014. The syllabus requires relative charge and mass: notes give alpha +2e, mass about 4 but for beta give only "mass much smaller than a nucleon" (no value, e.g. about 1/1840 of a nucleon, relative charge -1) and for gamma "no rest mass". Nowhere do notes or cards state that beta is deflected MORE than alpha in the same field (lighter), nor that alpha deflection is small; notes only say "Relative curvature also depends on speed and momentum, so charge alone does not set an exact radius", which hides the standard expected comparison. Fix: add relative charge/mass table (alpha +2/4, beta -1/1/1840, gamma 0/0) and "beta deflects more than alpha".

28.7 [S2] Location: syllabus practical for topic 6 ("establish half-life of radioactive material (using dice or coins...)") and notes/cards. No notes section, card or task mentions the dice/coin half-life model, the mandatory practical. Half-life items are only 28-019 (definition) and 28-020 (read off a data set that halves exactly every 6 min and states "80, 40, 20 and 10" in the prompt: trivial), plus MC12/P02(d). There is no card for time from fraction remaining, fraction remaining from time, reading a half-life from a decay curve with non-trivial points, or subtracting background first (only in P02(e)/MC9). Fix: add a dice-model card and a graph-reading card.

28.8 [S3] Location: ITEM-28-002. "State two causes of background radiation." tariff 1 mark for two items (marking is "1 mark" for the whole sentence); alternatives not accepted. Fix: tariff 2 or "any two".

28.9 [S3] Location: ITEM-28-014. Canonical: "Positive alpha is forced upward by the field-motion relation." "Field-motion relation" is jargon; the rule (Fleming's left-hand rule with the first finger = field, second finger = direction of positive charge's motion) is not named. Verified result: v right, B into the page, force on + is up; correct. The syllabus ties 5.7.1 (left-hand rule) to this; cross-reference missing.

28.10 [S3] Location: near-duplicates. 28-008 vs 28-009 vs 28-015 (alpha/gamma ionisation vs penetration, three cards, same content); 28-011 vs 28-012 vs 28-013 vs 28-014 (gamma undeflected/deflection directions; 011 and 012 duplicate each other's second mark); 28-018 uses 222/86 -> 218/84, identical to the notes example "Starting with A = 222 and Z = 86"; 28-017 vs notes; P02(a),(b) vs 28-010/011; MC3/MC4 vs 28-010.

28.11 [S3] Location: ITEM-28-020 and figure-6118-28-01.png. The notes' figure is not used by any card; 28-020 says "using a decay curve" but only gives a list of four values. The figure itself is correct (checked: 80 at 0, about 40 at 6 min, 20 at 12, 10 at 18; axis "Background-corrected count rate / s^-1" and "Time / min") but draws ~60 measurement-like markers although the data are "idealised" values at four times. Fix: use the figure in the card or give a table.

28.12 [S3] Location: MC distractors, topic 28. Weak: Q1 C "A shadow alone", D "A static ruler mark"; Q2 B "Only visible colour", C; Q3 B "Neutral hydrogen atoms"; Q5 C, D; Q6 A "None", C "All nuclei"; Q7 A "Open a sealed source", B "Remove controlled storage", D "Hold the source close to the body" (three obviously unsafe actions, correct option the only plausible); Q10 B, C; Q12 A "Zero". Correct longest in Q2, Q5.

28.13 [S3] Location: MC10 stem "With positive plate above and negative below, which way does beta-minus deflect?" Key D (upward) correct (electron force opposite to field, toward + plate). Option A "Downward like alpha" is the useful distractor. Stem should say the beam travels horizontally between the plates. Minor.

28.14 [S3] Location: notes wording, topic 28. "no rest mass", "attenuate", "ionisation density", "deposits energy ... spatial densities", "secondary particles", "nuclear excitation energy", "transmitted intensity", "relative curvature ... momentum" are above Grade 10 for an unexplained first use. "The curved trajectory does not mean the magnetic field is doing work through a force along the velocity in this ideal account" is confusing and out of scope. Also repeated meta-artefacts: "in the school comparison" (x5), "Original curve data", "Original graphical solution".

28.15 [S3] Location: notes "describe the existence and major causes of background radioactivity" and 6.2.1. Only natural sources are listed (cosmic, rocks, radon, living matter); human sources (medical X-rays, fallout, nuclear industry) are absent from notes and 28-002. Safety notes lack specific stored/handled practices students are asked in exams (lead-lined container, tongs, never point at people, wash hands, limited time/sources stored in locked cupboard, wear film badge): notes give general principles only; card 28-001 matches notes.

28.16 [S3] Location: topic structure. No practical_task item (no 16-mark task) for topic 28 even though a graph (figure 28-01) exists and half-life data are ideal; see 27.13. Also no card on gamma emission not changing A and Z (only in 28-016 and notes).

28.17 [S3] Location: notes MC placement. The MC under 6.2.2 contains 6.2.3-6.2.5 questions (alpha identity, deflection, half-life, nuclide equation); 6.2.4 and 6.2.5 sections have no practice at all.

28.18 [S3] Location: notes headings and wording as 25.27. "Define radioactive decay", "Represent nuclear changes during decay", "Original graphical solution" as headings; "Do not subtract four from Z or add two to A by confusing their notation positions" is hard to follow.

28.19 [S4] Location: Bloom/difficulty. 28-003, 28-008, 28-012, 28-016 "Analyse", diff 5, 2 marks.

28.20 [S4] Location: P02 prompt boilerplate "working and units where needed"; marks 1+1+2+2+2 = 8 correct. (d) 96 -> 24 = two halvings, 10/2 = 5 min correct; (e) 42-6 = 36 correct. Note (c) "equal short counting intervals" ok.

28.21 [S4] Location: ITEM-28-007 "State what random decay means for an individual nucleus." Covers time only; the syllabus says "randomly over space and time" (direction of emission).

---------------------------------------------------------------------
## Per-topic verdicts

Topic 25: READY AFTER FIXES. No physics errors; key, direction (F up, anticlockwise field, N on right for the solenoid), gradient (2 N/A) all correct. Must fix: template marking guidance and "Link ..." answers, key pattern, bell mechanism (syllabus example) and permanent-vs-electromagnet comparison, controls unmarked in the 16-mark task, undefined "domain/couple/remanence/saturation", inconsistent practice data (MC12 vs P03), and three faulty or duplicate figures (02, 05, 04/07 labelling).

Topic 26: READY AFTER FIXES. All formulae and numbers correct (3 V, 2 A, 4 V, 0.05 V/turn, 4 A, period halves). Must fix: boilerplate/mislabelled marking guidance, missing period mark in 26-009/010, identical figures 01/02/03, Namibia coverage (card has none; ECB claim unverified), out-of-syllabus laminations/I^2R unflagged, same key pattern, controls unmarked in 16-mark task.

Topic 27: READY AFTER FIXES. All A/Z arithmetic correct. Must fix: nuclide and composition (charge/mass) gap, out-of-syllabus antineutrino, template marking guidance and "Link" answers, mislabelled draw/equation guidance, MC key pattern and weak distractors, near duplicates, no practical task (confirm contract).

Topic 28: READY AFTER FIXES (heavier). Physics correct, deflection directions verified (electric: alpha down, beta up; magnetic: alpha up, beta down for rightward beam, B into page). Must fix: MC Q5 stem/key mismatch, circular alpha answer (28-009), missing relative deflection beta>alpha and relative charge/mass values, missing dice/coin half-life practical and weak half-life coverage, template marking guidance, key pattern, near-duplicate cluster 008/009/015 and 011-014.

## Counts by severity (finding IDs above; one finding counted once)

Computed by grep of the "[Sx]" tags at the head of each numbered finding (see end of file for the generated table).

## Checked
- Read in full: notes 25, 26, 27, 28; all items in the four flashcard JSONs (every flashcard, 4 MC sets x 12 questions with keys and feedback, 4 short_answer, 2 practical_task).
- Recomputed with python: 25 gradient 2 N/A (all successive gradients 2.0, intercept 0.1 N), MC12 (0.4/0.2 = 2; 0.4x0.2 = 0.08); 26: 6x50/100 = 3 V, 12x0.5 = 6 W -> 2 A, 10x80/200 = 4 V, 8/4 = 2 A, 8x100/200 = 4 V, 12/3 = 4 A, 12x60/240 = 3 V, 12x0.5/3 = 2 A, 5/100 = 0.05; 27: all A/Z subtractions (226/88->222/86, 210/84->206/82, 218/84->214/82, 24/11->24/12, 32/15->32/16, 14/6->14/7, 23-11 = 12, 39-19 = 20, 15+16 = 31); 28: 120->30 = two halvings, 120/4/8/16 values, 96->24 over 10 min = 5 min, 42-6 = 36, 55-5 = 50, 230/90->226/88, 12 h/4 h -> 1/8, 80/40/20/10 at 6 min steps, +5 background sequence 85/45/25/15. No numeric mismatches found.
- Independently solved every MC question before reading the key; no key disagreements and no question with zero or two defensible answers (28 Q5 key is defensible but the stem is misleading, 28.4).
- Direction checks (Fleming left-hand rule, right-hand grip, solenoid polarity, charge deflection in E and B fields): all stated directions are correct.
- Every figure viewed: 25-01 to 25-07, practical-25, 26-01 to 26-03, practical-26, 28-01. (Topic 27 notes have no figures.)
- Syllabus text for 5.6, 5.7.1, 5.7.2, 6.1, 6.2 and the topic 6 practical list compared with notes and cards.
- 8-word shingle copy check against the 24 exam-paper and examiner-report PDFs.

## Could not check
- ECB generation licences PDF (Ruacana as hydro, September 2025): WebFetch failed with a TLS certificate error; claim unverified.
- Did not read assessment-evidence/GAPS.md, misconceptions.json, answer-shapes.json, claims files or contract.json in depth; did not verify claim_ids/objective_ids mappings, authored_hash or provenance fields.
- Whether practical_task items are required for topics 27 and 28 (not confirmed from the contracts).
- Whether figures render the same in the final app (reviewed PNG files only).
- Real examiner mark-scheme wording for bell, dating and half-life items (marking evidence is partial); statements about "what examiners expect" are from general NSSCO/IGCSE practice, not from a located mark scheme.


## Counts by severity (generated)

| Topic | S1 | S2 | S3 | S4 | Total |
|---|---|---|---|---|---|
| 25 | 0 | 7 | 22 | 3 | 32 |
| 26 | 0 | 7 | 12 | 2 | 21 |
| 27 | 0 | 5 | 11 | 2 | 18 |
| 28 | 0 | 7 | 11 | 3 | 21 |
