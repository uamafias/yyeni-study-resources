# Cluster A review: NSSCO Physics 6118, topics 1 to 4

Reviewer: independent physics review (review only, no repository file changed).
Package: /Users/yyeniai/yyeni-study-resources/publish/nam-6118-nssco-2026/
Severity: S1 physics/key wrong or unsafe; S2 imprecise/incomplete in a way that could cost marks or teach a misconception, or out of scope; S3 pedagogy, clarity, labelling, duplicate, weak distractor; S4 minor wording.

Headline: I found NO S1 defect in topics 1 to 4. Every number in the notes, all 48+13+19+18 flashcards, both MC sets, both short-answer tasks and all four practical tasks recompute correctly (python, listed at the end). The problems are in marking guidance (template text), MC answer-position pattern, figure titles/labels, a few imprecise explanations, duplicates and one prompt/mark-scheme mismatch in every practical task.

Plan note: topics 2 and 3 have no multiple_choice_set or short_answer item by design (curriculum/item-budget.json: 14 and 20 items; topic 2 = 13 cards + 1 practical, topic 3 = 19 cards + 1 practical). I did not count that as a defect. Topic 1 and 4 have 1 MC + 1 short answer + 1 practical each.

Cross-cutting patterns (referenced below as X1 to X4):
- X1. Marking guidance of every flashcard in topics 1 to 4 is the canonical answer cut into sentences and prefixed with a template label ("Combine the linked ideas and explain the reason:", "Method step:", "Contrast:", "Cause and effect:", "Diagram/graph feature:", "Equation, substitution and final result:", "Definition:", "Property or unit:"). Counts of guidance lines: T1 81, T2 18, T3 33, T4 25. No alternative acceptable wording, no "do not accept", no mark-splitting rationale. The label often does not match the card (e.g. "Method step:" on a card asking for a column heading).
- X2. All four practical_task items use the same prompt template for part (c): "Plan an investigation in this physical context. Include the arrangement, five operational measurement steps, controls, a table and how the data would support a conclusion. [8]". The mark scheme gives 5 marks for steps, 1 table, 1 graph, 1 conclusion = 8, and says "Controls and safety support the method; the planning allocation totals eight marks". So the prompt demands controls and arrangement but no mark is allocated to them, and the "graph" mark in (c) repeats part (a). No investigation aim is stated, yet the conclusion mark says "answer the aim".
- X3. All practice figures (practical-6118-1..4 and figure-6118-3-0x) join the plotted crosses with a straight line segment instead of showing a separate fitted line, show no gradient triangle, and do not start the axes at the origin (so the "passes through the origin" claim in T1 and T4 cannot be seen).
- X4. Both MC sets (T1 P01 and T4 P01) have the identical key sequence A D C B A D C B A D C B.

---------------------------------------------------------------------

## TOPIC 1 Mathematical skills and units

1. T1 | notes, "Multiply and divide with justified rounding" | S3.
Quote: "If a model moves 5.4 m in 2.0 s, distance divided by time gives 2.7 m/s. ... A value such as 2.666666 on a display does not mean the original measurements were that precise; a two-significant-figure final answer is 2.7."
Problem: 5.4/2.0 = 2.7 exactly (python), so no 2.666666 can appear on the display; the illustration refers to a different calculation and confuses the reader.
Fix: use data that give a repeating decimal, e.g. 5.3 m in 2.0 s no; use 8.0 m in 3.0 s = 2.666666... m/s, quote "2.7 m/s".

2. T1 | ITEM-6118-1-P01 (MC set), key pattern | S3 (X4).
Keys: 1A 2D 3C 4B 5A 6D 7C 8B 9A 10D 11C 12B. The sequence ADCB repeats three times exactly; each letter used 3 times. A learner can learn the pattern, and the same pattern is in T4. Fix: shuffle so the order is not periodic (and differs from T4).

3. T1 | P01 MC, distractor/stem quality | S3.
- Q3 option B "Between arbitrary polygon vertices" is implausible for "Which length is a radius?" and answer feedback "That describes neither a circle radius nor its fixed endpoints" is muddled. Replace by "From one point on the circle to another point on the circle" (a chord).
- Q5 "Which is the SI unit of mass?" options N, W, Pa are all obviously non-mass units; add "g" as a real distractor (A kg, B g would then be tempting, but kg is SI).
- Q1 B/D ("Their sum multiplied by four", "The last reading divided by four") and Q7 A/B/D ("2T", "T/2", "T²") are implausible; Q7 stem "nonzero period T" is fine but only C is reciprocal. Q2 A "100" feedback is circular: "This is not the kilo factor".
- Q6 (bearing east) and Q2 are pure recall for a set labelled "Apply".
- Q4 stem and key are partly cued by wording ("triangular area" / "½ × base × perpendicular height") but acceptable.
All 12 keys are correct (solved independently: mean A; kilo 1000; radius centre-to-circumference; ½bh; kg; 090°; 1/T; 9.1 s; 0.072 s; 0.25 m²; 30%; 6.28). One defensible answer each.

4. T1 | all 48 flashcards, marking_guidance | S2 (X1). Example ITEM-6118-1-001-SYNTH: "Combine the linked ideas and explain the reason: Subtraction compares final and initial temperature. (1 mark)." This is not guidance, it repeats the answer with a template prefix; for the calculate cards (52 lines) "Equation, substitution and final result: Distance = speed × time = 1.8 × 4.0 (1 mark)" is acceptable in structure but lacks "accept unit missing/wrong unit penalty" etc. Needs card-specific credit points and accepted alternatives (e.g. 1-009 accept 4 Hz, 4/s; 1-046 accept 5.6E-5? no).

5. T1 | ITEM-6118-1-028-SYNTH | S2.
Prompt: "Explain why a triangular sheet has half the area of a rectangle with the same base and perpendicular height."
Answer: "A diagonal divides that rectangle into congruent triangles. Each triangular region therefore occupies half of its area."
Problem: that argument only proves the result for a right-angled triangle. For a general triangle (the prompt says "triangular sheet" with a perpendicular height) the diagonal of the rectangle is not the triangle. Also "congruent" is not otherwise taught in the notes. Fix: "Two identical triangles fit together to make a parallelogram (or rectangle) of the same base and perpendicular height, so one triangle is half of it." (notes say "half the matching parallelogram" in MC feedback Q4 B, which is the correct idea).

6. T1 | ITEM-6118-1-010-CALC | S3.
Prompt: "At fixed force, pressure is inversely proportional to contact area. Calculate the new pressure when the area doubles from a condition giving 900 Pa." Answer 450 Pa is correct. Problems: pressure and P = F/A are not yet taught (topic 11); the wording "from a condition giving 900 Pa" is awkward; the answer "Doubling area halves pressure" is stated, so the 2-mark "Calculate" is really one step. Fix: "A force of constant size is spread over a contact area that doubles. The pressure was 900 Pa. Calculate the new pressure."

7. T1 | ITEM-6118-1-012-CALC | S3. "Calculate an approximate value for 612 divided by 29.7 ..." The command word should be Estimate/Show. Accept any sensible rounding (e.g. 600/30 = 20, 610/30 about 20); guidance fixes "600/30". Exact value 20.6.

8. T1 | ITEM-6118-1-016-PROC | S3. "Describe one alignment needed when measuring an angle with a protractor." Answer contains two alignments (centre on vertex AND zero line on one arm) for a 1-mark card; ambiguity about whether one alone scores. Fix: ask "State where the centre of the protractor is placed" or award either.

9. T1 | ITEM-6118-1-009-CALC | S4. Answer adds "equivalent to 4 Hz"; hertz is not introduced in topic 1 notes (period/frequency appears later).

10. T1 | ITEM-6118-1-013-SYNTH | S3 and 1-014/1-017 context. 1-013 "constructing a ray at 35° to a surface normal" uses optics context before topic 17; acceptable but note the AO label "AB" for a 2-mark explain with two near-identical statements.

11. T1 | ITEM-6118-1-020-DEF "Define a curve" / notes "Describe a curve" | S4. "A curve is a line whose direction changes along its length" excludes straight lines (fine) but a curve in the notes is also taught as the graph line; consistent. No issue beyond wording "line".

12. T1 | ITEM-6118-1-P02 (short answer, 8 marks) | S3.
Marks: (a)1+(b)1+(c)2+(d)2+(e)2 = 8, matches guidance. Physics all correct (milli 10^-3; s^-1; mean 37.5/3 = 12.5 s; 1850/1000 = 1.85 s).
Problems: (b) prompt "State the unit notation for seconds to the power minus one" gives the answer in words (cued; also "unit notation" is odd). Better: "Write the unit of frequency using a negative index" or "Write m/s using a negative index" (the syllabus example). (c) answer "They should estimate the same physical time" is vague; better "the readings must be repeats of one measurement under the same conditions, otherwise the mean has no meaning". (a) guidance does not list accepted forms (0.001, 1/1000, 10^-3). command_word is "State" for a mixed task. No physical context (sector/situation null), trivial for an 8-mark item. Parts duplicate flashcards: (d)/1-005 and notes MC Q8, (e)/1-044 and MC Q9, (b)/1-048, (a)/MC Q2.

13. T1 | ITEM-6118-1-P03 (practical, 16) | S2 (X2) plus S3.
Data check: gradient 8/5 = 1.6, 40/25 = 1.6, 48/30 = 1.6 s per oscillation; zero intercept; period 1.6 s corresponds to a pendulum length of about 0.64 m (T = 2π√(L/g)), realistic. Marks (a) 5 = 1+1+2+1, (b) 3, (c) 8 = 5+1+1+1: sums to 16. Invented data are labelled "invented, idealised practice readings" (good).
Issues: (i) X2 mismatch (controls demanded, not credited; graph mark duplicates (a); no aim given). (ii) The "investigation" is not an investigation of a relationship (elapsed time against oscillation count simply yields the period); tolerable as a measurement task but "controls" and a "conclusion/aim" are artificial. (iii) Gradient unit: answer "s per oscillation"; oscillation count is dimensionless, so "s" or "s per oscillation" should both score; guidance only says "axis-ratio unit". (iv) canonical_answer embeds a markdown image link "![Original fitted practice graph](assets/practical-6118-1.png)" that will not render in a text field. (v) context fields all null.

14. T1 | figure practical-6118-1.png | S3 (X3). Axes: x "Oscillation count" (no unit; fine), y "Elapsed time / s"; scale starts at 5 and ~7, so the zero intercept stated in the answer cannot be seen; title "Original practice: Timing repeated pendulum oscillations" does not follow the convention the notes teach (dependent against independent); no gradient triangle. Correct data, correct labels.

15. T1 | notes, jargon and level | S3. Terms not explained for Grade 10-11: "congruent" (card 1-028), "annular regions", "convex polygon", "supplementary obtuse angle", "chord", "calipers" (US spelling; syllabus uses "caliper"), "idealised", "operational". Also each notes section ends with the generic "Connections" paragraph "Use these ideas with the neighbouring physics topics named in the topic title ..." which names no topics in topics 1 to 4 (boilerplate, S3).

16. T1 | near duplicates across the topic | S3. 1-005 (mean 6.2 s), notes example 8.3 s, P02(d), MC Q8; 1-044 (45 ms), P02(e), MC Q9; 1-022 (radius) and MC Q3; 1-048 and P02(b); 1-014 (start at 2 cm graduation) duplicates 4-002 (1.5 to 9.2 cm) and T4 MC Q8. Acceptable for spaced practice only if declared; no intentional_duplicate_group is set.

17. T1 | notes, scope | S4. Out-of-syllabus but harmless: "annular regions", "chord", "convex". Trigonometric/inverse-sine use is in scope (refractive index). No scope-limit item (collisions, nuclides, diverging lenses) arises in topic 1. Collision/energy mentions absent.

All other numerics verified correct (see list). Notes cover every one of the 13 + 6 syllabus bullets of 1.1 and 1.2.4.

---------------------------------------------------------------------

## TOPIC 2 Planning investigations and recording results

18. T2 | all 13 flashcards, marking_guidance | S2 (X1). "Method step:" is used for cards that are not method steps: 2-009 ("Describe an aim ..."), 2-011 (ordering of a table), 2-012 (a column heading), 2-013 (axis labels). "Contrast:" and "Combine the linked ideas..." simply repeat the answer. No accepted alternatives (e.g. other valid safety precautions for 2-004, other valid parallax actions for 2-002).

19. T2 | ITEM-6118-2-P01 (practical, 16) | S2 (X2).
Data check: temperature rise 2.4 °C per 30 s every interval; gradient 12/150 = 0.08 °C/s correct; intercept 22 °C. Realistic for ~36 W into ~0.11 kg of water, ignoring heat losses (labelled "invented, idealised"). Marks (a) 5, (b) 3, (c) 8 sum to 16.
Problems: canonical plan step 5 "Compare readings over a suitable heating duration while keeping the heater setting, water mass and container unchanged" is a restatement of controls, not an operational measurement step, yet the guidance gives one mark per "specific operational step". Step 1 packs four actions. Safety in the plan is a vague "handle hot apparatus safely" and omits the real hazard of an immersion heater (do not switch on out of water, keep mains away). X2 applies (controls uncredited; aim absent; graph mark repeated). The notes say heating duration should be named with a "practicable way of maintaining" each control; the plan does not state how power is kept constant.

20. T2 | ITEM-6118-2-012-PROC and 2-013-PROC | S3. Prompt contains the answer: "Describe a suitable heading for a column of elapsed-time readings expressed in seconds" (answer "Elapsed time / s"); "Describe the axes ... using table headings Temperature / °C and Heating time / s" (answer: label them with exactly those headings). The second tests only which axis is horizontal; the prompt does not give a cue, but the "headings" are supplied. Rewrite 2-012 as "A column holds readings of elapsed time in seconds. Write its heading." and 2-013 as "Which table heading goes on the x-axis and which on the y-axis?" if the intent is independent/dependent.

21. T2 | ITEM-6118-2-009-PROC | S3. "Describe an aim ..." The command word should be "Write/State"; the answer simply restates the prompt (cued). Also the syllabus bullet is "predict the hypothesis or aim", but no card asks for a hypothesis.

22. T2 | ITEM-6118-2-003-PROC and 2-010-PROC | S3. 2-003 "Describe how apparatus choice should be stated in a plan to measure a cooling water temperature" is vague (what is asked: instrument and range?). 2-010 "Describe one way to organise information from an apparatus diagram and a table before using it in a calculation" - answer has three ideas (quantities, units, conditions, measured/calculated) for 1 mark.

23. T2 | ITEM-6118-2-004-PROC | S3. "one safety precaution" answer has two ideas (heat protection AND secure support) for 1 mark; clarify "either".

24. T2 | coverage gaps | S3. Syllabus bullet "explain the importance of units and recording results" has no card on why units matter (2-011 only asks ordering); "units in the heading, not in the cells" is only implied by 2-012. No card on hypothesis, on reading a thermometer/measuring cylinder, on ammeter/voltmeter connection (taught in notes).

25. T2 | ITEM-6118-2-006/007/008 and 2-005 | S3. Four 2-mark "explain independent/dependent/control" cards that are near-duplicates in concept; 2-007's prompt contains the answer ("measured while ... Explain why extension is dependent"). 

26. T2 | notes | S3/S4.
- "Merely saying keep everything the same", "A statement such as be careful ..." appear without quotation marks (reads as broken English).
- "a tilted ruler can describe a longer diagonal distance": correct but jargon-heavy ("describe"); "artefact" in card 2-001 is not Grade 10 vocabulary (S4).
- "Use a low-voltage supply ... follow the teacher's equipment instructions" is fine; the practice plan's "suitable low-voltage heater" is unspecific.
All numerics (0.08 °C/s etc.) correct.

27. T2 | figure practical-6118-2.png | S3 (X3). Axes labelled "Heating time / s", "Temperature / °C"; scale 22 to 34 on y (starts at 22, so the intercept is on the axis line and fine). No gradient triangle; title is a description not "Temperature against heating time" as the notes teach in "Graph headings and orientation" (topic 3) and "title describes the dependent quantity against the independent quantity" (topic 2 notes). Data all correct.

---------------------------------------------------------------------

## TOPIC 3 Graphs, uncertainty and experimental conclusions

28. T3 | figure-6118-3-06.png (card 3-007 "Draw a suitable fitted trend ...") | S2.
The figure shows two overlapping lines "Trend" (blue, joined 3,6,9,12) and "Readings" (orange, joined 3.0, 6.1, 8.9, 12.0). The readings are joined point to point (a zigzag), which is exactly what the notes forbid ("not by joining every neighbouring point"), and the "fitted line" is itself just joined marks. Best-fit line (python least squares not available, computed by hand): slope 2.98, intercept 3.03, i.e. y = 3.0x + 3.0, which is a straight line, not the blue/orange pair. Fix: plot crosses only for the readings and draw one straight ruled line y = 3.0x + 3.0 (or the best-fit).

29. T3 | figures 3-01, 3-02, 3-04, 3-05, 3-06, 3-07 | S3. Placeholder titles that break the notes' own heading rule ("A graph heading identifies the dependent quantity plotted against the independent quantity ... not merely saying graph"; syllabus 1.2.3): "Suitable regular scales", "Dependent quantity against independent quantity", "Quantity and unit on both axes", "Distinguishing two datasets", "An offset straight trend", "Unambiguous point centres". Only figure 3-03 ("Spring extension against load") is correct. Fix: "Position against time", "Temperature against heating duration", "Mass against volume", "Temperature against time for containers A and B".

30. T3 | figures 3-01 to 3-06 against cards 3-002 to 3-007 | S3. The answer figures plot invented data that are not in the prompts (3-002 prompt only gives ranges; fig shows six points 5..35 cm; 3-003 prompt has no data, fig shows 20, 23, 26, 29 °C at 0 to 90 s; 3-004 fig shows 0 to 9 mm for 0 to 0.6 N; 3-005 fig shows mass 4 to 16 g for 5 to 20 cm³ (0.8 g/cm³)). A learner cannot check their own axes against a graph with different data; cards ask only for axes, figures add data and a joined line. The units (mm, N, min) are assumed. Data are not labelled "invented".

31. T3 | figure-6118-3-05.png (cooling A and B) | S3. The two series use the same cross marker and the same solid line style, distinguished only by colour (blue/orange) and the legend, contradicting the notes ("rather than relying on colour alone"). Time axis ticks at 0.25 min with only three data times; points joined (acceptable for 3 points but not a fitted line). Data: A falls 70, 66, 62 (4 °C/min); B 70, 68, 66 (2 °C/min), correct to card.

32. T3 | figure-6118-3-07.png | S4. Points (1,4) and (3,9) lie on the extreme edge of the axes (x range 0.9 to 3.1; y 4 to 9) so the crosses touch the frame; x axis ticks at 0.25 s unnecessarily fine. Use axes 0 to 4 s and 0 to 10 cm.

33. T3 | figure practical-6118-3.png | S3 (X3). Data correct (3 cm/s, intercept 5 cm); intercept at x = 0 is visible; no gradient construction triangle; generic title.

34. T3 | notes, seven repeated headings | S3. Seven consecutive sections are titled "Original graphical solution" with the identical sentence "The following plot is generated from the stated practice values." and identical alt text "Original labelled graph". The "stated practice values" are not stated anywhere in the notes (they are only in the flashcard prompts or invisible), so the figures have no explanation or caption, and alt text is useless to screen-reader users. Fix: caption each with what it demonstrates and the values plotted.

35. T3 | notes, section "present points on the curve as crosses (x) or encircled dots (...)" | S4. The heading contains a private-use glyph (copied from the syllabus symbol font) and renders as a missing character. Replace by "(⊙)" or "encircled dots".

36. T3 | all 19 flashcards, marking_guidance | S2 (X1). Examples: "Diagram/graph feature: Use a horizontal time axis spanning 0 to 10 s with a regular scale. (1 mark)". "Cause and effect:" prefix on 3-010, 3-012, 3-016, 3-017, 3-018 simply repeats the answer. The graph-drawing cards allocate marks 1+1 to descriptions and give no credit for correct plotting, label of unit, or heading (e.g. 3-004 asks for a heading and units but the guidance gives units only half of a mark).

37. T3 | ITEM-6118-3-002 to 3-008 | S3. Bloom label "Analyse" for "Draw" cards (labelling axes, plotting two points) is too high; Apply is plausible. Prompt cues: 3-003 states "Label the independent and dependent quantities" then the answer is that heating duration is independent; 3-008 prompt says "using a fine cross" and the answer is "small visible crosses" (answer in prompt); 3-004 "suitable heading" is answered "Spring extension against load" (fine). 3-002 and 3-005 are near duplicates (axes labels); 3-003 and 3-004 as well.

38. T3 | ITEM-6118-3-006-INTERP | S3. Prompt gives A: 70, 66, 62 °C and B: 70, 68, 66 °C at 0, 1, 2 min. Linear fall over 2 min is acceptable but cooling is exponential; two containers have no stated difference; data are not labelled as invented practice data. Guidance gives no mark for correct plotted points or key; "Label the two trends A and B so their different cooling rates can be identified" is a labelling mark only.

39. T3 | ITEM-6118-3-015-SYNTH | S3. Prompt: "Explain the link between random scatter and systematic offset when assessing a fitted graph." There is no causal link; the card contrasts them. The word "link" invites a wrong answer (e.g. that one causes the other). Rewrite: "Explain the difference between the effect of random scatter and of a systematic offset on a fitted graph."

40. T3 | ITEM-6118-3-014-PROC | S3. "Describe one numerical test that could support direct proportionality..." Answer y/x constant. A second valid test (straight line through the origin) is in the notes but guidance does not allow it, and the test is graph-based, not numerical (so not required). Fine but should say "accept ratio y/x approximately constant within the measurement uncertainty".

41. T3 | ITEM-6118-3-011-DEF and objective AO labels | S3. "Define measurement error" is pure recall but labelled AO C (the 1.2 slots are all assigned AO C by the plan's slot design; the syllabus AO for recall of definitions would be A). Flag for the plan owner, not a card error.

42. T3 | ITEM-6118-3-010-MECH | S3. Prompt "Explain how repeated readings of 15.8, 15.8 and 15.9 cm can be precise but inaccurate if the accepted length is 15.0 cm": mean 15.83 cm, offset 0.83 cm, spread 0.1 cm, correct. The prompt gives the conclusion ("precise but inaccurate"), so the answer is cued; ask "Comment on the precision and accuracy of these readings". Syllabus defines accuracy via the average, which the answer does not mention (it says "common displacement").

43. T3 | ITEM-6118-3-P01 (practical, 16) | S2 (X2).
Data: gradient 30/10 = 3 cm/s, intercept 5 cm, correct. Context realistic (slow model vehicle 3 cm/s), labelled invented. Marks 5+3+8 = 16 correct. Issue: plan step 5 "Use the repeated positions at each time to obtain a representative trend while preserving any anomalous readings" is analysis, not a measurement step; X2 applies. The same graphed relationship (position-time, gradient = speed) is re-used in topic 5, so the notes' phrase "The gradient is the model vehicle's rate of position change" should say "speed (3 cm/s)" to connect, or deliberately avoid it. "Draw a suitable fitted line" is credited only 1 mark although the data are exactly linear.

44. T3 | notes 1.2.5 coverage | S3. The syllabus bullet "explain uncertainty as the interval on either side ..." is taught, but no way is given to decide the size of an uncertainty (for example, half the smallest division, or half the range of repeats). Notes only say the smallest division "is not a universal complete account". Card 3-012 provides ±0.5 °C without saying where it comes from.

45. T3 | notes and wording | S4. "Replace the instrument may be reasonable only if ..." (unquoted phrase, in "suggest possible improvements"); "A statement such as be careful ..." style. "Original graphical solution" boilerplate (see 34). Numerics verified: gradient (63−75)/(80−20) = −0.20 °C/s; 24.0 ± 0.2 cm gives 23.8 to 24.2 cm; y = 2, 5, 10 increments 3 and 5.

---------------------------------------------------------------------

## TOPIC 4 Measurement, scalars and vectors

46. T4 | ITEM-6118-4-P01 (MC set) key pattern | S3 (X4). Keys A D C B A D C B A D C B (identical to T1 P01).

47. T4 | P01 MC solved independently (all keys agree) | S3 distractors/cues. Answers: 1 cylinder; 2 internal jaws; 3 ratchet limits force; 4 same position and direction; 5 energy; 6 direction; 7 first tail; 8 8.7 cm (10.7−2.0); 9 12.4 mm (12 + 4×0.1); 10 4.68 mm (4.5+0.18); 11 1.60 s (32.0/20); 12 13 N (√(25+144)). No question has zero or two defensible answers. Weak items:
- Q1 "Which instrument is calibrated for a liquid volume?" options Stopwatch, Ammeter, Metre rule are trivially wrong; "calibrated" is jargon.
- Q2 stem "Which caliper feature measures the inside width" cued by "inside/Internal"; option C "An external micrometer anvil" is not a caliper feature; B "The zero-checking label" is nonsense.
- Q3 A "changes a diameter into a radius" and B "measures internal volume" implausible.
- Q5/Q6 pure recall; Q6 A/B/C ("Whether a unit exists", "Whether it changes", "measured experimentally") are implausible; feedback "Direction is part of the vector specification".
- Q7 A "At the midpoint of either component" implausible; D "At the final tip, pointing back" is the reversed resultant (good distractor).
- Q8 A "5.35 cm" (halving) is not a real error; Q9 D "11.6 mm" feedback "There is no stated correction requiring subtraction" is a poor reason (a real mistake is reading the vernier from the wrong end). Q10 C "18.45 mm" feedback "misreads the scales as decimal strings" is unclear. Q12 A feedback "wrong dimensional interpretation" is jargon (should say it is 13² not 13).
- Q4 option D "Travel from one extreme to the other" is half a cycle (good), C partly defensible only if "any crossing" is read loosely; keyed answer is still unique.

48. T4 | ITEM-6118-4-P02 (short answer, 8) | S3.
Marks 1+1+2+2+2 = 8; guidance matches. Maths correct: 37.5/25 = 1.50 s; √(9²+12²) = 15 m. Problems: (e) asks only for the magnitude although the syllabus objective is "magnitude AND direction" (the direction is never practised at 2-mark level except 4-017); (a) is trivial and duplicates 4-014 and MC Q5; (b) duplicates 4-010 and MC Q4; (c)/(d) duplicate 4-012 and 3-019; (e) duplicates MC Q12 (same 5-12-13 triple) and 4-017; command_word "State" for a mixed task; no context fields. (c) guidance "one for division by the correct cycle count" does not match the question (explain why 25 oscillations are better).

49. T4 | ITEM-6118-4-P03 (practical, 16) | S2 (X2) plus S3.
Data: 7, 14, ..., 42 s for 5 to 30 oscillations; gradient 35/25 = 1.4 s/oscillation; correct; pendulum length about 0.49 m, realistic; labelled invented. Marks 5+3+8 = 16.
(i) X2. (ii) It is nearly the same task as T1 P03 (same counts 5..30, same template; only the period 1.4 s vs 1.6 s differs): near duplicate. (iii) The canonical conclusion states "this is a period measurement, not a test of length dependence", yet the syllabus bullet for this topic (2.1) is "describe a simple experiment to establish that the only variable that affects the period is the length", which is the better practical. (iv) Notes "Table: Record cycle count" vs prompt "Oscillation count" (wording mismatch, S4). (v) Plan step 5 "Repeat for several counts with the same length" is not a new operational step.

50. T4 | ITEM-6118-4-018-INTERP and figure-6118-4-02.png | S3.
Card: "Draw a tip-to-tail scale diagram adding 3 N east to 3 N at 60° north of east." Physics: resultant = √(3²+3²+2·3·3·cos60°) = √27 = 5.196 N, direction 30° north of east (bisector of two equal vectors), so "about 5.20 N at 30° north of east" is correct. Figure shows vectors correct (tip at (4.5, 2.60)). Problems: the figure is a coordinate plot with axes "Eastward component / N" and "Northward component / N", which is not a scale drawing (no scale such as 1 cm = 1 N, no ruler/protractor construction), and mislabels the 60° vector as "components"; the 60° angle, the 5.2 N magnitude and the 30° are not annotated; the label "Vector 2: 3 N" overlaps the arrow. The numbers 3 N and 60° do not appear in the notes text (only in the card), so the figure belongs to no taught example. Marking guidance 1+1 gives credit for "about 5.20 N at 30°" with no tolerance range for a hand-drawn answer (accept 5.1 to 5.3 N and 28° to 32°).

51. T4 | figure-6118-4-01.png | S3. Correct geometry: 4 N east, 3 N north, resultant from the origin to (4,3), dashed red. Missing: resultant length (5 N) and angle (36.9°) not labelled, so it does not show the worked result in the notes text (the notes' own example is 8 N and 6 N, giving 10 N and 36.9°). Label "Vector 2: 3 N" touches the right-hand frame. The two figures use identical colours/styles for components and resultant, fine. Fix: add "R = 5 N", the angle arc, and align with the notes example (8 N and 6 N) or the card.

52. T4 | ITEM-6118-4-017-CALC | S4. √(4²+3²) = 5 N; tan⁻¹(3/4) = 36.9°, correct. Guidance does not accept the bearing form 053.1° or the angle from north 53.1° with its reference stated; add. Prompt "Give the angle north of east" fixes the reference, so fine.

53. T4 | ITEM-6118-4-016-DIST | S3. "Equal speeds require equal magnitudes of motion" is circular and vague. Better: "Speed is only the size of the velocity; velocity also needs a direction, so two objects with equal speed but different directions have different velocities."

54. T4 | flashcards 4-002, 4-003, 4-006, 4-007, 4-011 | S3.
- 4-002 duplicates T1 1-014 and T4 MC Q8.
- 4-003 "Describe one action..." answer is two ideas (eye level and meniscus bottom) and the notes also demand a vertical cylinder on a level surface; fine, but "bottom of the meniscus" only holds for water (prompt says water, OK).
- 4-006 compound 1-mark answer: add main-scale, add aligned division × resolution, apply zero correction.
- 4-007 "avoids excessive force" cues "ratchet".
- 4-011 "Explain why a measuring tape can be preferable to a micrometer for the length of a classroom bench" is trivially obvious (cued by "classroom bench").
- 4-001 and 4-004 "calibrated", "three-dimensional volume" jargon.

55. T4 | all 18 flashcards, marking_guidance | S2 (X1). "Method step: Time a known number of complete oscillations and divide the elapsed time by that number. (1 mark)" etc. 4-017 is the only card with card-specific guidance. No alternatives (e.g. 4-005 accept "measure 10 sheets", 4-010 accept "start at the lowest point").

56. T4 | notes 2.2 | S3. The graphical-addition section has no worked numerical example (scale chosen, measured length, angle), although card 4-018 and the figure use one (3 N, 3 N at 60°). The perpendicular-vectors example (8 N, 6 N) differs from figure and card (4 N, 3 N). Bearing/compass notation is not linked to the vector direction given as "north of east". Fix: add a worked example matching the figure.

57. T4 | notes 2.1, 2.2 numerics | verified, no defect. Examples: 11.6−3.0 = 8.6 cm; 8.0 mm/80 = 0.10 mm; 18 + 6×0.1 = 18.6 mm; 5.5+0.23 = 5.73 mm; 10:14:45 to 10:15:20 = 35 s; 24.0/15 = 1.60 s; resultant of 8 N and 6 N = 10 N at 36.9° (53.1° from north); practice gradient 1.4 s. Physics statements (small-angle pendulum, mass not affecting period, g constant) correct and caveated. The scalar/vector definitions and examples are correct (mass, distance, speed, energy, time scalar; force, displacement, velocity, acceleration vector).

58. T4 | notes level | S4. "a sag" in tape, "a depth probe", "pivot-to-bob-centre" fine; "ratchet", "anvil", "spindle", "thimble", "sleeve" are not explained or illustrated and there is no diagram of a micrometer or caliper in the notes (unlabelled parts). Add a labelled drawing or define each part.

59. T4 | figure practical-6118-4.png | S3 (X3). Data correct (7 to 42 s); no origin; no triangle.

---------------------------------------------------------------------

## Source copying and unsourced claims
Compared 8-word runs of every notes file, card prompt, answer and guidance against the text of all 24 exam papers and examiner reports in Question Banks (pdftotext) and against the syllabus text. Corpus hits: one (the syllabus bullet "use averages, decimals, fractions, percentages, ratios and reciprocals", used as a section heading). Verbatim syllabus text appears only in headings (the objective bullets), which is intended. No copied exam/report wording found in notes or flashcards. No unsourced factual claims found; "invented, idealised" is used on the practical data, but the card data in 3-006 to 3-009 and the short numerical cards are not labelled invented (S4).

## Per-topic verdicts

Topic 1: ready after fixes. Physics is correct throughout; all numerical examples, 48 cards, the MC key, short answer and practical recompute correctly. Needed: replace template marking guidance with card-specific credit points, repair the triangle explanation (card 1-028), fix the 2.666666 example, reshuffle MC keys and strengthen distractors, cure the practical prompt/mark-scheme mismatch, and add context and aims to the practical.

Topic 2: ready after fixes. Short, accurate notes and cards; main faults are template guidance, the practical mark scheme (non-operational step, uncredited controls), cued/duplicate cards and thin coverage of units and hypothesis. Figure fine apart from title/triangle.

Topic 3: ready after fixes (largest fix list among the four). Physics and numbers are correct, but the seven answer figures have placeholder titles that contradict the notes, one figure (3-06) shows a zigzag joined line as the "fitted trend", the figures plot data not in the prompts, notes captions are empty, one heading has a broken glyph, and card 3-015 is misleading.

Topic 4: ready after fixes. All measurements, vector sums and keys are correct. Needed: MC key reshuffle and distractor repair, scale-diagram figure (4-02) that is a true scale drawing with annotations, a worked graphical-addition example in the notes, duplicate short-answer parts, a length-dependence practical (the syllabus experiment), and card-specific marking guidance.

## Counts of findings by severity (finding numbers above; no. 57 is a verification note and not counted)
- Topic 1: S1 0; S2 3 (4, 5, 13); S3 11 (1, 2, 3, 6, 7, 8, 10, 12, 14, 15, 16); S4 3 (9, 11, 17).
- Topic 2: S1 0; S2 2 (18, 19); S3 7 (20, 21, 22, 23, 24, 25, 27); S4 1 (26).
- Topic 3: S1 0; S2 3 (28, 36, 43); S3 12 (29, 30, 31, 33, 34, 37, 38, 39, 40, 41, 42, 44); S4 3 (32, 35, 45).
- Topic 4: S1 0; S2 2 (49, 55); S3 9 (46, 47, 48, 50, 51, 53, 54, 56, 59); S4 2 (52, 58).
The cross-cutting patterns X1 (template guidance), X2 (practical prompt/mark-scheme mismatch), X3 (figure joined lines/no origin/no triangle) and X4 (MC key pattern) are counted once per topic in the findings that cite them.

## What I checked
- Read all four notes files in full; every statement/example/unit; python recomputation of every numeric example in the notes, every calculation card, both MC sets (independently solved before reading keys, then compared), both short answers, all four practical datasets (gradients, intercepts, mark sums), and the vector sums and angles (4 N/3 N, 8 N/6 N, 9 m/12 m, 5 N/12 N, 3 N at 60°). Rounding behaviour confirmed (3.746 to 3 s.f. = 3.75; 0.007864 = 0.00786).
- Read every item of the four JSON files (items 48+1+1+1, 13+1, 19+1, 18+1+1+1) for prompt, answer, guidance, command word, Bloom, AO, tariff, duplicates, cueing; confirmed MC/short/practical prompts are identical to the notes' practice tasks; all items have qa_status review_required.
- Viewed every referenced image: practical-6118-1, -2, -3, -4; figure-6118-3-01 to -07; figure-6118-4-01, -02 (all 13 PNGs).
- Syllabus bullets for 1.1, 1.2.1 to 1.2.5, 2.1, 2.2 from pdftotext of NSSCO_Physics_syllabus.pdf; all bullets are present in the notes as headings. Scope limits (collisions, nuclide formulae, diverging lenses) do not arise in these four topics.
- 8-word overlap scan against 24 PDFs of exam papers/examiner reports (2020 to 2025) and the syllabus.

## What I could NOT check
- Whether the examiner reports rubric style for the 8- and 16-mark tasks matches (assessment-evidence/GAPS.md says marking evidence is partial; I did not reconstruct official rubrics).
- I did not read misconceptions.json, answer-shapes.json or each topic's authoring files (claims, contract.json) in detail, so I did not verify claim_id mapping or objective_id accuracy beyond spot checks of titles; AO label correctness was judged from the plan's slot design (work_order.md for topic 2 shows the 1.2.x slots are assigned AO C by design).
- No image-pixel measurement tools (PIL/numpy not installed); least-squares fit for card 3-007 done by hand (slope 2.98, intercept 3.03).
- Rendering of the markdown image links inside canonical_answer fields in the actual learner app.
- Past-paper PDFs that are scanned images (no text layer) would not be found by the text overlap scan.
