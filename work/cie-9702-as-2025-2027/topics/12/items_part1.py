#!/usr/bin/env python3
"""Item texts for topic 12, part 1: 12.1 slots (001-027 + MISCON 118/131/129).

Each entry: (slot_suffix, prompt, canonical_answer, [guidance lines], claim_ids)
The build script assembles full items from these.
"""

S = {}

# ---- OBJ-9702-12.1-01 set up apparatus correctly ----
S['001-PROC'] = dict(
    prompt="A learner is given a stand, a clamp, a spring, a 100 g mass hanger, a metre rule and a pointer, with instructions to investigate how the extension of the spring depends on the mass hung from it. Describe how the apparatus is set up correctly before any readings are taken.",
    answer="""Set up in the order the instructions give, so each part can be checked as the arrangement grows:
1. Bolt or weight the stand so it cannot tip, and clamp the spring's support at the top.
2. Hang the spring from the support, attach the mass hanger, and fix the pointer to the hanger so it moves against the rule without touching it.
3. Clamp the metre rule vertically beside the spring, with its scale close to the pointer, and check the rule reads vertically with a set square.
4. Before the first reading, check the finished arrangement: the stand does not rock, the spring hangs freely without brushing the rule, and the pointer aligns with the scale.""",
    guidance=["Order: the steps are given in sequence - stand first, rule clamped next, checks made last - and the sequence is the mark.",
              "Measurements: the arrangement is built so the extension can be read as a measured difference of readings against the rule.",
              "Result: the checks complete the set-up, so the first reading is taken on an apparatus that has been compared with the instructions and gives the final arrangement its start."],
    claims=['CLM-9702-12-001', 'CLM-9702-12-002'])

S['002-WHY'] = dict(
    prompt="Explain why the electrical supply is the last thing to be connected when a circuit is being set up in a laboratory.",
    answer="The supply is connected last so that the whole arrangement can be checked, wire by wire against the diagram, before anything is live. A fault found while the circuit is dead costs a correction; the purpose of the order is that the checking happens at the moment it is safest and most useful, because a mistake spotted after switching on may already have damaged a component or given a false reading.",
    guidance=["Reason: the purpose of connecting last is stated - the check happens before the circuit is live.",
              "Purpose and need: the arrangement needs checking while it is dead, which is why the order exists."],
    claims=['CLM-9702-12-001'])

S['003-APP'] = dict(
    prompt="A learner clamps a metre rule horizontally to measure the deflection of a loaded metal strip, but clamps only 2 cm of the rule at one end. When the load is applied, the whole rule droops and the readings drift. Explain what was set up wrongly here and what should have been done.",
    answer="The rule itself was not held rigidly: 2 cm of clamp grip is too little for a metre rule, so the clamped rule bends under the load and its tip moves, and the deflection readings drift because the reference is moving. In this case the rule needed to be clamped along much more of its length, or mounted on a rigid stand, so that the measured deflection is the strip's and not the rule's.",
    guidance=["Situation: this case, the drooping rule, is named as the fault.",
              "Because: the readings drift because the clamped reference moves, so the set-up, not the strip, is being measured."],
    claims=['CLM-9702-12-002'])

# ---- OBJ-9702-12.1-02 follow instructions and diagrams ----
S['004-PROC'] = dict(
    prompt="A circuit diagram shows a cell connected to a switch, then a rheostat, then an ammeter, then a lamp, with a voltmeter drawn across the lamp. Describe, in order, how the circuit is built from the diagram so that it is ready to be switched on.",
    answer="""Build the circuit in the order of the diagram:
1. Connect the components into a single loop as drawn: cell to switch, switch to rheostat, rheostat to ammeter, ammeter to lamp, and the lamp back to the cell, keeping the switch open throughout.
2. Connect the ammeter so its positive terminal faces the positive terminal of the cell, since a meter connected the wrong way round reads in the wrong direction.
3. Add the voltmeter across the lamp, as drawn, because the diagram shows it in parallel with the lamp, not in the loop.
4. Check the completed circuit wire by wire against the diagram, then set the rheostat to its maximum and switch on.""",
    guidance=["Order: the steps are in diagram sequence - loop first, voltmeter after, check then switch on.",
              "Readings: the meters are placed where the diagram shows them so the current and the p.d. are the measured quantities.",
              "Result: the wire-by-wire check completes the build, so the final circuit is the diagram's circuit."],
    claims=['CLM-9702-12-003', 'CLM-9702-12-004'])

S['005-WHY'] = dict(
    prompt="Explain why a circuit should be checked against its diagram wire by wire before the supply is switched on.",
    answer="The check is done before switching on because it is the moment a wrong connection can be found without cost: a wire joined to the wrong terminal is visible against the diagram while the circuit is dead. The purpose of doing it wire by wire is that the whole circuit is covered - the check is what turns a wired board into the circuit that was drawn, and it needs to happen before current can flow through any mistake.",
    guidance=["Reason: the purpose is that faults are found while the circuit is dead.",
              "Why: wire by wire, so that the need for the check - full coverage - is met."],
    claims=['CLM-9702-12-004'])

S['006-APP'] = dict(
    prompt="A learner building a circuit from a diagram connects the voltmeter in series with the lamp, in the main loop. The ammeter reads a very small current and the lamp does not light. Explain what went wrong here.",
    answer="The voltmeter was placed where the diagram shows the loop, not where it shows the voltmeter: a voltmeter is drawn in parallel with the component it measures, and in series it adds its large resistance to the loop, so the current falls to almost nothing and the lamp stays dark. In this case the voltmeter belongs across the lamp, connected on each side of it, as the diagram draws it.",
    guidance=["Situation: this case, the series voltmeter, is named as the fault.",
              "Because: the current is small because the voltmeter's resistance is in the loop, since the diagram's parallel placement was not followed."],
    claims=['CLM-9702-12-004', 'CLM-9702-12-005'])

# ---- OBJ-9702-12.1-03 collect appropriate quantity of data ----
S['007-PROC'] = dict(
    prompt="A learner plans to plot a graph of the current in a filament lamp against the p.d. across it, using a rheostat to vary the p.d. Describe how an appropriate quantity of data is collected for that graph.",
    answer="""1. Set the rheostat so the readings span the whole range available: take the p.d. from its smallest usable value up to its largest, since the plotted points need to be spread out, not gathered in one place.
2. Take at least six well-spaced readings of p.d. and current across that range - enough to show the curve of the trend and support a line through them.
3. At each setting, wait for the readings to settle, then record the p.d. and the current together in the table.
4. Repeat where the scatter matters, and use the mean of the repeats, so the data set is large enough to show the trend.""",
    guidance=["Order: the steps are sequenced - range first, then number of readings, then repeats.",
              "Measurements: each reading of p.d. and current is a measurement made at the bench and recorded.",
              "Result: the final data set of at least six spread readings is what the graph needs."],
    claims=['CLM-9702-12-006', 'CLM-9702-12-007'])

S['008-WHY'] = dict(
    prompt="Explain why a graph used to test a relationship needs at least six well-spaced readings rather than three.",
    answer="Three points show where a line could go; six show where the trend actually runs. The reason for the larger set is that a trend needs to be distinguished from scatter - with repeats and spread readings the line of best fit is supported at several places along it, and the purpose of the graph, which is to show the relationship over the whole range, is met. Three readings crowded together cannot show a trend apart from their own scatter.",
    guidance=["Reason: the purpose of six readings is to show the trend apart from the scatter.",
              "Need: the graph needs support along its whole length, which is why the count matters."],
    claims=['CLM-9702-12-006'])

S['009-APP'] = dict(
    prompt="A learner measures the resistance of a wire at five lengths: 0.500 m, 0.520 m, 0.540 m, 0.560 m and 0.580 m, all taken within the first minute, and then finds the gradient of the plotted line is unreliable. Explain what was wrong with the quantity of data collected here.",
    answer="The readings cover a tenth of the wire's usable span, all gathered between 0.500 m and 0.580 m, so the plotted line is short and the triangle used for the gradient is small. Because the data are spread over so narrow a range, the same plotting error is divided by a short run and the gradient carries a large percentage uncertainty. In this case the readings needed to run from near 0.100 m to near 1.000 m, well spaced, for the gradient to be worth quoting.",
    guidance=["Situation: this case is the narrow 0.500-0.580 m cluster.",
              "Because: the gradient is unreliable because the range is short, so the data collected were not the quantity the graph needed."],
    claims=['CLM-9702-12-007'])

# ---- OBJ-9702-12.1-04 repeat readings ----
S['010-PROC'] = dict(
    prompt="A learner is timing the period of a load oscillating on a spring and finds the timings scatter. Describe how the repeat readings should be taken and used.",
    answer="""1. Time the same whole number of oscillations again - the same count, from the same marker, in the same conditions - so the repeats measure the same quantity.
2. Record each repeat in its own place in the table as it is taken, never over the reading it repeats.
3. Take enough repeats to show the scatter (three or four), since the spread of the repeats is what measures the uncertainty.
4. Use the mean of the repeats as the value, and record the repeats beside it, so the scatter that the mean averaged away stays visible in the table.""",
    guidance=["Order: the steps are sequenced - repeat, record, take enough, then average.",
              "Measurements: each repeat is a measurement recorded in its own place.",
              "Result: the mean of the repeats is the final value, so the answer carries the benefit of the repeats - no equation is needed, only the arithmetic of the mean."],
    claims=['CLM-9702-12-008'])

S['011-WHY'] = dict(
    prompt="Explain why repeating a reading and using the mean gives a value closer to the true value than a single reading.",
    answer="The readings scatter randomly about the true value - some high, some low - and the mean of the repeats lets the high and low partly cancel, so the mean sits closer to the truth than a typical single reading. The reason repeating works at all is the kind of error it acts on: it reduces the effect of random error, because only random scatter cancels in the average.",
    guidance=["Reason: the purpose of the mean is that random error partly cancels.",
              "Why: the answer names the kind of error repeating reduces, so the reason is complete."],
    claims=['CLM-9702-12-008'])

S['012-APP'] = dict(
    prompt="A learner takes four readings of a wire's diameter with a micrometer that was never zero-checked, and averages them, expecting the average to cure the zero error. Explain why the mean will not do what the learner expects here.",
    answer="A zero error is systematic: the micrometer that reads 0.02 mm shut adds 0.02 mm to every reading it takes, so all four readings carry the same offset and the mean carries exactly the same offset too. Because the error is not random, averaging has nothing to cancel in this case - the cure was to check the zero first, record the zero error and subtract it from each reading.",
    guidance=["Situation: this case is the un-zeroed micrometer.",
              "Because: the mean fails because a systematic error survives averaging, since every repeat inherits the same offset."],
    claims=['CLM-9702-12-009'])

# ---- OBJ-9702-12.1-05 common laboratory apparatus ----
S['013-PROC'] = dict(
    prompt="A learner has to measure the diameter of a wire, the length of the wire along a metre board, and the volume of water in a beaker. Describe how each measurement is made with the appropriate instrument.",
    answer="""1. The diameter, about 0.3 mm across: use a micrometer screw gauge (resolution 0.01 mm). Check the zero with the jaws closed, close the jaws on the wire using the ratchet so the wire is not squashed, and record the reading to 0.01 mm, subtracting any zero error.
2. The length, several tens of centimetres: use a millimetre rule (resolution 1 mm) along the board, with the eye directly above each mark, recording to the nearest millimetre.
3. The volume: use a measuring cylinder stood on the bench, reading the bottom of the meniscus with the eye level with it, and record to the cylinder's graduations.
Each reading is taken at the resolution of its instrument and recorded in the unit the table heading uses.""",
    guidance=["Order: the steps are sequenced by instrument, smallest resolution first.",
              "Measurements: each reading is a measurement named with its instrument and its resolution.",
              "Result: so the final set of readings matches each size to the instrument built for it."],
    claims=['CLM-9702-12-010', 'CLM-9702-12-011'])

S['014-WHY'] = dict(
    prompt="Explain why a micrometer rather than a millimetre rule is used to measure the diameter of a wire.",
    answer="A wire's diameter is a few tenths of a millimetre, and a rule's resolution is 1 mm, so the rule cannot resolve the quantity at all - its reading would be a guess at half the value. The micrometer is used because its resolution is 0.01 mm, and the purpose of matching the instrument to the size is that the measurement then carries a percentage uncertainty small enough to be worth using.",
    guidance=["Reason: the purpose is resolution matched to size, so the reading is worth taking.",
              "Need: the wire needs the finer instrument, which is why the micrometer is chosen."],
    claims=['CLM-9702-12-010'])

S['015-APP'] = dict(
    prompt="A learner measures the internal width of a pipe with a millimetre rule pushed through the opening, and the reading varies by several millimetres each try. Explain what went wrong here and what instrument belonged in the opening.",
    answer="A rule pushed through an opening cannot sit squarely across its internal width - the rule's edge wanders and the reading varies because the rule sits differently each time. Because the measurement is an internal width, this case needed calipers: the jaws sit against the internal faces, are locked where they touch, and the width is read from the caliper scale, giving the same value each try.",
    guidance=["Situation: this case is the rule pushed through the pipe opening.",
              "Because: the readings vary because the rule cannot be placed squarely, so the instrument was wrong for the internal width."],
    claims=['CLM-9702-12-010'])

# ---- OBJ-9702-12.1-06 stop-watch and oscillations ----
S['016-PROC'] = dict(
    prompt="A strip of metal clamped at one end vibrates after being pulled aside and released. Describe how the period of the vibration is measured with a stop-watch.",
    answer="""1. Choose a fixed marker - the strip's rest position - and count one complete oscillation as the tip passing the marker going the same way as at the start, after a full journey out and back.
2. Time a whole number of complete oscillations, at least ten and usually twenty, starting and stopping the watch as the tip passes the marker.
3. Record the total time and the number of oscillations counted, then repeat the timing and record the repeat.
4. Divide the mean total time by the number of oscillations: T = t ÷ n, giving the period in seconds, and use the mean of the repeat periods.""",
    guidance=["Order: the steps are sequenced - marker, count, time, repeat, divide.",
              "Measurements: the total time and the count are the readings, and the period is calculated from them.",
              "Result: the final period comes from dividing the mean total by the count, so the answer is the period in seconds."],
    claims=['CLM-9702-12-012', 'CLM-9702-12-013'])

S['017-WHY'] = dict(
    prompt="Explain why twenty oscillations are timed rather than one when measuring a period with a stop-watch.",
    answer="Starting and stopping the watch carry the same reaction uncertainty of a few tenths of a second however many oscillations are timed, so the purpose of timing twenty is that the fixed uncertainty is shared across the whole run: as a percentage of the total it is a twentieth of what it would be on a single swing, and the period, the total divided by twenty, inherits that smaller share. Because one oscillation takes well under a second, timing one hands the full reaction uncertainty to a tiny reading and the period is not worth quoting.",
    guidance=["Reason: the purpose of the count is to share the fixed timing uncertainty across many oscillations.",
              "Why: the percentage uncertainty is what shrinks, so the need for the count is stated in the useful form."],
    claims=['CLM-9702-12-013'])

S['018-APP'] = dict(
    prompt="A learner times a bouncing mass, starting the watch as the mass is released and stopping it when the bouncing appears to have stopped, then divides by 12 - in the learner's words, about 12 bounces happened. Explain what is wrong with this timing.",
    answer="The watch was stopped when the motion died away, not when a whole number of complete oscillations had finished - so the total includes a part-oscillation and the count of 12 was a guess, not a count. Because the timing does not answer the test - has a whole number of complete oscillations been timed? - the value has no meaning as a period in this case: the watch should have been started as the mass passed a marker going one way and stopped at the same marker after a counted whole number of bounces.",
    guidance=["Situation: this case is the stop-when-it-dies timing with the guessed count.",
              "Because: the timing is invalid because no whole number of complete oscillations was measured, so the division gives no period."],
    claims=['CLM-9702-12-012', 'CLM-9702-12-082'])

S['118-MISCON'] = dict(
    prompt="A learner announces that timing half an oscillation is fine - it is the time from the top to the bottom of the swing, and doubling it gives the period. Explain what is wrong with this idea and how the timing should be done.",
    answer="The error: timing a half oscillation, or one oscillation, or the time for the motion to die away, hands the full reaction uncertainty of starting and stopping the watch to a reading of well under a second, so the period is not worth quoting. The correct idea: time a whole number of complete oscillations, at least ten, and divide the total by the count - the test that tells them apart is whether a whole number of complete oscillations has been timed. Half an oscillation also fails that test twice over: the count is not a whole number, and the halves of a swing need not even be equal.",
    guidance=["Error: the half-oscillation timing is named as the error, in fact a whole-number count is needed instead.",
              "Test: has a whole number of complete oscillations been timed - that is what separates the two ideas."],
    claims=['CLM-9702-12-082'], misconception='MC-9702-12-01')

# ---- OBJ-9702-12.1-07 analogue and digital ----
S['019-PROC'] = dict(
    prompt="A circuit contains an analogue voltmeter with a pointer and a digital milliammeter. Describe how a reading is taken from each so that it is accurate.",
    answer="""1. The analogue voltmeter: place the eye directly above the pointer, and estimate the reading to the nearest half of the smallest division on its scale - the eye must be above the pointer because viewing at an angle shifts the apparent position of the pointer against the scale.
2. Read the scale in the printed direction, with the unit the scale carries.
3. The digital milliammeter: wait until the displayed value settles, then read what the display shows, in the unit marked on its panel - a display showing 250 on a meter marked mA is a current of 250 mA.
4. Record both readings at the moment they are taken, converted to the units the table headings use.""",
    guidance=["Order: the steps are sequenced - analogue first, digital second, recording last.",
              "Measurements: each reading is a measurement taken in the instrument's own unit.",
              "Result: the final record holds both readings, so each value is what its instrument actually said."],
    claims=['CLM-9702-12-014', 'CLM-9702-12-015'])

S['020-WHY'] = dict(
    prompt="Explain why an analogue scale is read with the eye directly above the pointer.",
    answer="The pointer stands a little above the scale, so viewing from an angle shifts its apparent position against the marks - the parallax error. The purpose of reading from directly above is that the sight line passes squarely through pointer and scale, and the reading taken is the one the instrument built; at an angle the same scale would give a different value to each eye position.",
    guidance=["Reason: the purpose of the eye position is to remove the parallax shift.",
              "Why: the pointer stands above the scale, so the need for the square sight line follows from the geometry."],
    claims=['CLM-9702-12-014'])

S['021-APP'] = dict(
    prompt="A learner reads a digital meter just as the circuit is switched on, records 168 mA, and later notices the display settles at 172 mA. Explain what was wrong with taking the reading at that moment.",
    answer="The reading was taken while the value was still settling, so the 168 recorded was a snapshot of the settling, not a measurement of the current - in this case the display needed to be watched until it steadied at 172 mA before the reading was taken. Because a reading taken mid-settle depends on when the watch fell rather than on the circuit, it is not reproducible, and the digital display is only accurate once the value it shows has settled.",
    guidance=["Situation: this case is the mid-settle reading of 168 mA.",
              "Because: the reading is wrong because the display had not settled, so the timing of the reading, not the circuit, set the value."],
    claims=['CLM-9702-12-015'])

# ---- OBJ-9702-12.1-08 accurate measurements ----
S['022-PROC'] = dict(
    prompt="Describe how accurate readings are taken and recorded in an experiment, from sighting the instrument to writing the value in the table.",
    answer="""1. Sight the reading properly: the eye in line with the pointer or the edge being read, because viewing at an angle shifts the apparent position of the mark against the scale (a parallax error).
2. Read the unit and the scale the instrument displays - a milliampere display is read in milliamperes - and convert to the unit the table heading uses before recording.
3. Record the reading at the moment it is taken, with its unit, in its column in the table.
4. Include every reading taken, repeats and unusual values alike, since the record at the bench is the experiment's memory.""",
    guidance=["Order: the steps are sequenced - sight, convert, record, keep everything.",
              "Measurements: each reading is a measurement carried from instrument to table with its unit.",
              "Result: the final table holds what the instruments said, so the record is accurate."],
    claims=['CLM-9702-12-016', 'CLM-9702-12-017', 'CLM-9702-12-083'])

S['023-WHY'] = dict(
    prompt="Explain why a reading should be written down at the moment it is taken rather than remembered and written up later.",
    answer="A reading held in the head is a reading half lost: the purpose of writing at the bench is that the value is recorded exactly once, by the person who saw it. Because writing up later involves copying, and copying is where numbers change - a digit turns, a decimal point slides - the bench record is the one that can be trusted, so the reading needs its place in the table at the moment it exists.",
    guidance=["Reason: the purpose of writing at once is that the record is made by the reader who saw the value.",
              "Need: the reading needs recording before memory and copying can change it, which is why the habit exists."],
    claims=['CLM-9702-12-017'])

S['024-APP'] = dict(
    prompt="A learner's table has a column headed I / A. The learner's milliammeter displays 250, and the learner writes 250 in the column. Explain what is wrong with this recorded reading.",
    answer="The display read 250 on a meter marked mA, so the current is 250 mA - which is 0.250 A - but the value written under the A heading was 250, a thousand times too large. Because the table heading sets the unit and the recorded number must match it, this reading needed converting before it was recorded: 250 mA written as 0.250 under I / A. Every value calculated from the row inherits the error if it is left as it is.",
    guidance=["Situation: this case is the 250 under a column headed I / A.",
              "Because: the reading is wrong because the display unit was not converted, so the recorded value does not match the heading."],
    claims=['CLM-9702-12-017', 'CLM-9702-12-083'])

S['131-MISCON'] = dict(
    prompt="A learner records a current in a table as 0.30 under a column headed I / A, using a meter whose display is marked mA and shows 300. Explain what is wrong with the learner's reading, and state the test that catches it.",
    answer="The error: the meter displays milliamperes, so 300 on its display is 300 mA, and writing 0.30 under a column in A has divided by a thousand twice - the value recorded is a thousandth of the true current. The correct idea: read the unit and scale printed on the instrument, and convert to the unit the table heading uses - 300 mA is 0.300 A, so 0.300 is the value that belongs in the column. The test that tells them apart is: what unit does the instrument display? Reading a scale the wrong way round fails the same test - the printed direction is part of the reading.",
    guidance=["Error: the mA-as-A recording is the error; in fact the display unit must be converted to the heading's unit.",
              "Test: what unit does the instrument display - that is the check that catches the mistake."],
    claims=['CLM-9702-12-083'], misconception='MC-9702-12-14')

# ---- OBJ-9702-12.1-09 largest range ----
S['025-PROC'] = dict(
    prompt="A metre board carries a wire that can be connected at any point from 0.100 m to 1.000 m along it. Describe how the readings are chosen so that they span the largest possible range of values.",
    answer="""1. Identify the limits the apparatus sets: the wire is usable from 0.100 m to 1.000 m, so that span is the largest range available.
2. Take readings from near each end of the span, since the trend is shown over the whole range available - a first reading at 0.100 m and a last at 1.000 m.
3. Spread the readings evenly between the ends, at least six in all, so the plotted points fill the graph rather than gathering wherever the clips happened to sit.
4. Keep the same spacing if a reading is added, so the set stays spread across the span.""",
    guidance=["Order: the steps are sequenced - limits first, ends next, even spread between.",
              "Measurements: each reading is a measurement placed by plan across the span.",
              "Result: the final set spans 0.100 m to 1.000 m, so the data cover the whole range the apparatus permits."],
    claims=['CLM-9702-12-018', 'CLM-9702-12-084'])

S['026-WHY'] = dict(
    prompt="Explain why readings should span the widest range the apparatus allows rather than a convenient band in the middle.",
    answer="A wide range gives a long trend line, and a long line is why the range matters: the triangle used for the gradient is then large, and the same plotting error is divided by a long run, so the gradient carries a small percentage uncertainty. Because a narrow band produces a short line and a large percentage uncertainty in the gradient, the widest range is the cheapest accuracy in the experiment - it costs only the decision to use it.",
    guidance=["Reason: the purpose of the wide range is a long line and an accurate gradient.",
              "Why: the gradient's percentage uncertainty is what improves, so the need for range is stated in the form that earns the mark."],
    claims=['CLM-9702-12-019', 'CLM-9702-12-084'])

S['027-APP'] = dict(
    prompt="A learner measuring how the period of a spring-mass system depends on mass uses masses 100 g, 105 g, 110 g and 115 g, although the mass hanger takes slugs up to 600 g. Explain what is wrong with the range used here.",
    answer="The apparatus allows masses from 100 g to 600 g, so the widest usable range is 500 g wide - and the learner's readings sit inside a 15 g band at one end of it. Because the plotted points will crowd into a short line, the gradient measured from it carries a large percentage uncertainty, and in this case the readings needed to run from 100 g up towards 600 g, spread across the span the hanger permits.",
    guidance=["Situation: this case is the 100-115 g cluster against a 600 g limit.",
              "Because: the range fails because it is narrow, so the data do not cover the range the apparatus permits."],
    claims=['CLM-9702-12-018', 'CLM-9702-12-084'])

S['129-MISCON'] = dict(
    prompt="A learner defends a set of readings taken at 0.400 m, 0.450 m, 0.500 m and 0.550 m on a metre board usable from 0.100 m to 1.000 m, saying the points line up beautifully. Explain what is wrong with this data set and state the test that catches it.",
    answer="The error: using a narrow range of the independent variable - four readings inside half a metre of a board that offers 0.100 m to 1.000 m, so the trend line is short and the gradient carries a large percentage uncertainty, however neatly the crowded points appear to lie. The correct idea: span the widest range the apparatus allows, with readings spread across it from near 0.100 m to near 1.000 m. The test that tells them apart is: does the data cover the whole range the apparatus permits? A beautiful line over a tenth of the span is a beautiful line over a tenth of the question.",
    guidance=["Error: the narrow 0.400-0.550 m range is the error; in fact the span should run the length of the board.",
              "Test: whether the data cover the whole range the apparatus permits - that is the check."],
    claims=['CLM-9702-12-084'], misconception='MC-9702-12-12')

if __name__ == '__main__':
    print(len(S), 'slots part 1')
