#!/usr/bin/env python3
"""Item texts for topic 12, part 2: 12.2 slots (028-061 + MISCON 119-122)."""

S = {}

# ---- OBJ-9702-12.2-01 single table ----
S['028-APP'] = dict(
    prompt="A learner keeps raw readings in a ruled table, repeat readings on a scrap of paper, and calculated values in a separate notebook. Explain why this experiment's presentation is poor and what should change.",
    answer="The results are scattered across three places, so the trend cannot be read anywhere and nothing can be checked against anything - a calculated value away from its raw readings cannot be verified, and the repeats on the scrap are not part of the record. Because all the results of an experiment belong in one table - one row per value of the independent variable, with the repeats and calculated values in their own columns beside the raw readings - the presentation in this case needs a single table holding everything, so the whole data set is seen together.",
    guidance=["Situation: this case is the three-place record.",
              "Because: the presentation fails because the table is the one place the whole experiment must live, so scattered records cannot be checked."],
    claims=['CLM-9702-12-020', 'CLM-9702-12-021'])

S['029-INTERP'] = dict(
    prompt="A results table is drawn with columns for the raw readings and for the values calculated from them. Determine what the single table gives a reader that separate records would not, naming the parts of the table that provide it.",
    answer="Reading the table: the raw columns, the repeat columns and the calculated columns sit side by side, one row per value of the independent variable. This arrangement means each calculated value can be traced back to the readings in its own row - the table shows the arithmetic at the point it was done - and the trend can be read down a single calculated column, which is what the analysis needs. Separate records would show the same numbers but not the connections: the row-wise layout is what the single table gives, and it means the whole data set is seen and checked together.",
    guidance=["Reading: the table is read by its columns and rows, and the value of the layout is drawn from them.",
              "Means: the side-by-side layout means checkable arithmetic and a readable trend - that is what the table gives."],
    claims=['CLM-9702-12-020', 'CLM-9702-12-021'])

# ---- OBJ-9702-12.2-02 record all data ----
S['030-APP'] = dict(
    prompt="A learner takes a reading that looks too high, says nothing, and leaves it out of the table. Explain why the table is now a poorer record.",
    answer="The table no longer records all the data: the unusual reading was evidence of something - a slip, a fluctuation, a misread scale - and leaving it out removes the experiment's only trace of what actually happened. Because a table is the complete record, written as the readings are taken including the ones that look wrong, this case needed the reading recorded where it fell and repeated - the mean then argues with it honestly, and the scatter it caused stays visible in the repeats.",
    guidance=["Situation: this case is the omitted unusual reading.",
              "Because: the record is poor because it is incomplete, so the table cannot be trusted to hold what happened."],
    claims=['CLM-9702-12-022'])

S['031-INTERP'] = dict(
    prompt="A table of timings holds, in one row: 17.4 s, 17.9 s, 17.6 s, and a mean of 17.6 s. The learner's write-up says the middle reading was probably a slip and announces the mean as though the three readings agreed. Determine what the table's record shows about the readings and what the write-up hides.",
    answer="Reading the record: the three readings are all present - including the 17.9 s - and the table is complete, which is what makes it trustworthy. The table shows a scatter of 0.5 s across the repeats, with one reading (17.9 s) sitting above the other two; the mean of 17.4, 17.9 and 17.6 is 17.633 s, written as 17.6 s. What the write-up hides is that scatter: presenting 17.6 s as though the readings agreed claims a precision the 0.5 s spread does not support - the table means the reader can see the spread, and the write-up means the spread is the honest uncertainty the mean carries (about ± 0.25 s, half the range).",
    guidance=["Reading: the values in the table are read, including the spread across the repeats.",
              "Shows: the complete table shows the scatter, so the mean's honesty is checked against it - that is what the record is for."],
    claims=['CLM-9702-12-022', 'CLM-9702-12-023'])

# ---- OBJ-9702-12.2-03 table in advance ----
S['032-APP'] = dict(
    prompt="A learner arrives at the bench, takes all the readings on the back of an envelope, and copies them into a neat table in the evening. Explain what was lost by copying up.",
    answer="The readings were copied, and copying is where numbers change: a digit turns, a decimal point slides, and the neat table is a copy of a copy rather than the bench record. Because the table should be drawn up before the first reading - so the readings go straight into it and avoid transcription - this case lost the original record; the envelope was the original, and the evening table cannot be checked against the apparatus that came down hours before.",
    guidance=["Situation: this case is the envelope-then-copy-up method.",
              "Because: the record is weakened because transcription introduces errors, so the table needed to exist before the first reading."],
    claims=['CLM-9702-12-024'])

S['033-INTERP'] = dict(
    prompt="A learner draws the table before starting: columns for m / g, t1 / s, t2 / s, mean t / s and T / s, and rows for the six masses planned from 100 g to 600 g. Determine what this advance table shows about the experiment before a single reading is taken.",
    answer="Reading the empty table: its columns show every quantity the experiment will read and calculate - two repeats, their mean, the period - and its six rows show the readings planned across the range. The table drawn in advance means the planning has been done as a structure: there is a place ready for every reading before it exists, the readings will be recorded at the bench rather than copied up, and the analysis (mean, then T) is already designed. An empty table with the right shape is the method written as a grid, and it shows the experiment was planned before it was run.",
    guidance=["Reading: the columns and rows are read as the plan they represent.",
              "Shows: the advance table shows the method settled - what is measured, how many times, over what range - so nothing is copied up and no reading arrives homeless."],
    claims=['CLM-9702-12-024', 'CLM-9702-12-025'])

# ---- OBJ-9702-12.2-04 raw and calculated columns ----
S['034-APP'] = dict(
    prompt="A learner's table holds L / m and T / s, but the T² values were worked out on a calculator and written on the page margin, next to a sketch of the graph. Explain what is wrong with this arrangement.",
    answer="The calculated values sit away from the readings they came from, so the arithmetic cannot be checked: a T² written in the margin cannot be traced to its T without hunting, and the graph sketch compounds the distance. Because the table carries one column for every raw reading and further columns for each quantity calculated from them - each calculated value beside the readings it came from - this case needed a T² / s² column in the table, filled row by row where the T values sit.",
    guidance=["Situation: this case is the calculated values in the margin.",
              "Because: the arrangement fails because calculated values belong beside their raw readings, so the check the table exists for cannot happen."],
    claims=['CLM-9702-12-026', 'CLM-9702-12-027'])

S['035-INTERP'] = dict(
    prompt="A table holds d / mm, then a column of A / mm² calculated as πd²/4 for each diameter, and one row shows d = 0.30 mm with A = 0.071 mm². Determine how the calculated column lets a reader check that value, and what the check gives.",
    answer="Reading the table: the A column sits beside the d column, so the value 0.071 mm² can be checked against its own row's reading of 0.30 mm. The check runs the calculation again from the raw reading: A = πd²/4, and d² = 0.30 × 0.30 = 0.09 mm², so A = 3.14159 × 0.09 = 0.282743 mm², and 0.282743 ÷ 4 = 0.0706858 mm², which is 0.0707 mm² to three significant figures - close to the table's 0.071 mm², so the row is consistent. That is what the side-by-side layout gives: every calculated value in the table can be re-run from the raw reading beside it, and a slip shows in the row where it happened.",
    guidance=["Reading: the calculated value is read against its raw reading in the same row.",
              "Gives: the check gives 0.0707 mm² against the table's 0.071 mm², so the table's arithmetic is verified - that is what the layout is for."],
    claims=['CLM-9702-12-026', 'CLM-9702-12-027', 'CLM-9702-12-032'])

# ---- OBJ-9702-12.2-05 column headings ----
S['036-APP'] = dict(
    prompt="A learner's table has a column headed length and another headed T squared. Explain what is wrong with these headings and how each should be written.",
    answer="Neither heading names a unit, so the numbers under them carry no meaning - a length in millimetres and a length in metres are different columns with the same wrong heading. Because every heading is written quantity / unit, these belong as L / mm (or L / m, whichever the rule reads) and T² / s², the unit of the calculated column worked out from its calculation - T² from T / s carries s². The written headings tell a reader what the numbers are and what unit they are in, which the bare words length and T squared cannot do.",
    guidance=["Situation: this case is the unitless headings.",
              "Because: the headings fail because they lack the quantity / unit convention, so the columns are unreadable."],
    claims=['CLM-9702-12-028', 'CLM-9702-12-029'])

S['037-INTERP'] = dict(
    prompt="A column heading is written 1/I / A⁻¹. Determine what this heading tells a reader about the numbers in the column, and how the unit follows from the calculation.",
    answer="Reading the heading in two parts: the quantity is 1/I - the reciprocal of a current - and the unit is A⁻¹, reciprocal amperes. The unit follows from the calculation: the raw currents are in A, so their reciprocals are in A⁻¹, and the heading states the result of that arithmetic. A reader opening the table knows, before reading a single value, that a number 2.5 in this column means 2.5 A⁻¹ - a current of 0.4 A inverted. That is the whole work of a heading: it makes every number in the column interpretable, including the ones calculated rather than read.",
    guidance=["Reading: the heading is read as quantity, then unit, then the value the pair gives the reader.",
              "Means: the heading means reciprocal currents in reciprocal amperes - the unit traced from the calculation is what the reading rests on."],
    claims=['CLM-9702-12-028', 'CLM-9702-12-085'])

S['119-MISCON'] = dict(
    prompt="A learner writes a calculated column's heading as T² because, in the learner's words, the unit was already in the T column. Explain what is wrong with this heading and state the test that catches it.",
    answer="The error: leaving the unit out of a calculated column's heading (or leaving out the separator, or giving the calculated column the raw column's unit) - the T column's unit does not travel to T², because squaring squares the unit too. The correct idea: every heading is quantity / unit, including calculated columns - T² / s², 1/I / A⁻¹ - with the unit worked out from the calculation. The test that tells them apart is: could a reader tell the unit of every number in the column? Under a bare T2 heading, a reader cannot tell whether the numbers are in s², s, or nothing at all.",
    guidance=["Error: the missing unit in the calculated heading is the error; in fact the unit is part of the heading for calculated columns too.",
              "Test: whether a reader can tell the unit of every number in the column - that is what separates a heading from a label."],
    claims=['CLM-9702-12-085'], misconception='MC-9702-12-02')

# ---- OBJ-9702-12.2-06 consistent precision ----
S['038-APP'] = dict(
    prompt="A learner's column of micrometer readings runs: 0.31 mm, 0.28 mm, 0.3 mm, 0.32 mm. Explain what is wrong with the precision of this column.",
    answer="One reading is recorded to one decimal place while the rest carry two - 0.3 mm among 0.31 mm and 0.32 mm - so the column mixes precisions and misstates the instrument: a micrometer resolves 0.01 mm, and every reading it takes deserves two decimal places. Because raw readings of one quantity are recorded to the same number of decimal places, matching the instrument's resolution, this case needed 0.30 mm in the third place - the trailing zero records the decimal place the instrument resolved.",
    guidance=["Situation: this case is the 0.3 among two-decimal readings.",
              "Because: the column fails because mixed precision misstates the instrument, so the readings needed consistent decimal places."],
    claims=['CLM-9702-12-030', 'CLM-9702-12-086'])

S['039-INTERP'] = dict(
    prompt="Two columns from the same experiment are shown. Column P / mm: 245, 613, 702. Column Q / mm: 12.5, 38.0, 45.2. Determine what the precision of each column says about the instruments that took the readings, and which column has an inconsistency.",
    answer="Reading the columns: P holds whole millimetres, the precision of a millimetre rule, so P's readings were taken with a rule - consistent. Q holds readings to 0.5 mm, which suggests a finer instrument - a set of calipers, perhaps - but that is also consistent across its three values. The inconsistency is not inside either column; it is that the same symbol, mm, appears at two precisions in one table, which is fine only if P and Q are genuinely different quantities measured with different instruments. If Q is a difference of two P readings (a change in length, say), then Q's claimed 0.5 mm precision is not supported by P's 1 mm rule: differences of rule readings carry ± 1 mm, and Q's column would be claiming a precision its source cannot give. So the check is: the number of decimal places states the instrument, and a calculated column cannot be finer than the readings it came from.",
    guidance=["Reading: the decimal places of each column are read as a statement of the instrument.",
              "Shows: the columns show their instruments - and a finer calculated column than its raw source is the inconsistency to look for."],
    claims=['CLM-9702-12-031', 'CLM-9702-12-086'])

S['120-MISCON'] = dict(
    prompt="A learner's table records the mass of water added to a beaker as: 46 g, 45.5 g, 47 g, 45 g. Explain what is wrong with the precision of these readings and state the test that catches it.",
    answer="The error: recording raw readings of one quantity to different precisions - three whole grams and one reading of 45.5 g, in a single column. If the balance displays whole grams, the 45.5 is a guess wearing a decimal place; if it displays 0.1 g, then 46 g and 47 g have dropped a digit the instrument resolved. The correct idea: record every raw reading of a quantity to the same number of decimal places, matching the instrument's resolution - all four to the gram, or all four to 0.1 g, whichever the balance shows. The test that tells them apart is: do all the readings in the column have the same number of decimal places?",
    guidance=["Error: the mixed one-decimal-then-whole-gram column is the error; in fact the resolution of one instrument sets one precision for all.",
              "Test: whether all the readings in the column share the same number of decimal places - that is the check."],
    claims=['CLM-9702-12-086'], misconception='MC-9702-12-03')

# ---- OBJ-9702-12.2-07 calculate from raw data ----
S['040-APP'] = dict(
    prompt="A learner calculates the resistance for each row of a table but does the arithmetic at home, away from the bench and the table. Explain why the calculated values should have been worked out in the table itself.",
    answer="Calculated quantities are computed from the raw readings in the table, in the table - a value worked out away from its raw readings cannot be checked against them, and the check is the point of the layout. Because a resistance belongs beside the V and I readings that produced it, working at home broke the trace: an arithmetic slip in the sitting room shows as a wrong value with no way to see which reading it came from, whereas in the table it shows in the row where it happened, while the apparatus could still be re-measured.",
    guidance=["Situation: this case is the calculate-at-home method.",
              "Because: the practice fails because calculated values need their raw readings beside them, so the table is where the arithmetic belongs."],
    claims=['CLM-9702-12-032', 'CLM-9702-12-033'])

S['041-INTERP'] = dict(
    prompt="A row of a table holds V / V = 4.8 and I / mA = 240, with a calculated R / Ω = 20. Determine how this row lets a reader verify the calculated value, and state the working that gives it.",
    answer="Reading the row: the calculated R sits beside the two readings it came from, so the verification runs on the row itself. The working: R = V ÷ I. The current is 240 mA = 0.240 A (converted to the unit the calculated column uses), so R = 4.8 ÷ 0.240 = 20.0 Ω - the table's 20 Ω, checked from its own row. The row means the value is not a claim but a calculation on display: any reader with the row can run the same one-line check, and the row-wise layout is what makes that possible.",
    guidance=["Reading: the row is read as equation, substitution and result in one place.",
              "Gives: the working gives R = 4.8 ÷ 0.240 = 20.0 Ω, so the table's value is verified - the row is the whole calculation."],
    claims=['CLM-9702-12-032', 'CLM-9702-12-033', 'CLM-9702-12-034'])

# ---- OBJ-9702-12.2-08 show working ----
S['042-APP'] = dict(
    prompt="A learner writes, for one row, the single line R = 20. Explain what is missing from this calculated value and what the full working should show.",
    answer="The value shows no working: no equation in symbols, no substitution, no unit on the way. Because working is shown for each calculated value - the equation in symbols, the substitution of the readings, and the result with its unit - the full form is: R = V ÷ I, then R = 4.8 ÷ 0.240 = 20.0, so R = 20 Ω. The steps are what make the value checkable and what carry the marks: a bare 20 is a claim, and a reader cannot tell whether the unit, the conversion or the division was where it went wrong.",
    guidance=["Situation: this case is the bare calculated value.",
              "Because: the value is poor because its working is missing, so equation, substitution and unit are what the record needs."],
    claims=['CLM-9702-12-034', 'CLM-9702-12-035'])

S['043-INTERP'] = dict(
    prompt="A worked step reads: A = πd²/4 = 3.14 × 0.30² / 4 = 0.0707 mm². Determine what this working shows a reader at each of its stages, and why the units at each stage matter.",
    answer="Reading the working left to right: the equation in symbols (A = πd²/4) shows what was calculated and from what; the substitution (3.14 × 0.30² / 4) shows the actual reading used, with the diameter in mm; the result (0.0707 mm²) carries the unit worked out from the calculation - mm squared, because d was in mm and the equation squares it. The unit at each stage is the check: the substitution's mm becomes the result's mm², and a result labelled mm after that squaring would announce its own error. The working means the reader can follow the argument from reading to result, which is the whole standard - each stage shows what the last one did.",
    guidance=["Reading: the working is read stage by stage, from equation to substitution to result.",
              "Shows: the stages show the trace from reading to unit-bearing result - the units mean the physics of the step is visible."],
    claims=['CLM-9702-12-034', 'CLM-9702-12-035'])

# ---- OBJ-9702-12.2-09 significant figures ----
S['044-APP'] = dict(
    prompt="A learner's raw times are recorded to 0.1 s, and the calculated T² column is written to six figures because the calculator showed six. Explain what is wrong and how many figures the T² values deserve.",
    answer="The calculator's display is not a reason: it shows every digit it can hold, and the calculated value follows the raw data, not the display. Because a calculated value is given to the significant figures of the raw data with the fewest, or one more - and the raw times here carry three significant figures - the T² values deserve three or four: 0.585 s², not 0.585225 s². The figures beyond the raw data's support are a claim about the calculator, and the justification that earns the mark names the raw value with the fewest figures.",
    guidance=["Situation: this case is the six-figure calculator column.",
              "Because: the quoting is wrong because calculated figures follow the raw data, so three or four significant figures is what the T² column supports."],
    claims=['CLM-9702-12-036', 'CLM-9702-12-037', 'CLM-9702-12-087'])

S['045-INTERP'] = dict(
    prompt="A diameter is measured as 2.4 mm (two significant figures) and a length as 0.318 m (three significant figures). The resistivity calculated from them is quoted as 1.4762 × 10⁻⁷ Ω m. Determine how many significant figures this value deserves, and justify the answer.",
    answer="Reading the raw data: the diameter carries two significant figures and enters the calculation squared (so its share doubles), while the length carries three. Because a calculated value is given to the significant figures of the raw data with the fewest, or one more, the resistivity deserves two or three significant figures: 1.5 × 10⁻⁷ Ω m or 1.48 × 10⁻⁷ Ω m. The five figures quoted (1.4762 × 10⁻⁷) are not supported - the 2.4 mm diameter limits the whole calculation to two figures' worth of trust - and the justification names it: the raw value with the fewest significant figures is the diameter, so the result is given to two, or three at most.",
    guidance=["Reading: the raw values are read for their significant figures, and the quoted result against them.",
              "Means: the quoted precision means a claim the diameter cannot support, so two or three figures is what the value deserves - that is the judgement."],
    claims=['CLM-9702-12-036', 'CLM-9702-12-087'])

S['121-MISCON'] = dict(
    prompt="A learner justifies a five-figure calculated value by saying that the calculator gave 1.4762, so that is the answer. Explain what is wrong with this justification and state the test that gives the right number of figures.",
    answer="The error: giving calculated values to an unjustified number of significant figures - the calculator displays every digit it holds, and none of the extra digits came from the measurement. The correct idea: match the significant figures of a calculated value to the raw data with the fewest, or give one more, and justify by naming that raw value. The test that tells them apart is: which raw value has the fewest significant figures? That value sets the ceiling - a diameter read to two figures supports a resistivity to two or three, however many digits the calculator offers.",
    guidance=["Error: quoting the calculator's display is the error; in fact the raw data with the fewest figures set the count.",
              "Test: which raw value has the fewest significant figures - that is the check that gives the justified number."],
    claims=['CLM-9702-12-087'], misconception='MC-9702-12-04')

# ---- OBJ-9702-12.2-10 label graph axes ----
S['046-APP'] = dict(
    prompt="A learner plots a graph with the x-axis labelled length and the y-axis labelled T2. Explain what is wrong with these axis labels and how each should be written.",
    answer="Neither axis carries a unit, so the graph's axes do not say what the numbers on them are - and every gradient read from the graph will inherit the omission. Because each graph axis is labelled with the quantity and its unit, written quantity / unit - the same convention as the table heading - these belong as L / m and T² / s², matching the table columns they came from. The labelled axes are what make a later gradient meaningful: T² / s² against L / m gives a gradient in s² m⁻¹ before the arithmetic even starts.",
    guidance=["Situation: this case is the unitless axes.",
              "Because: the labels fail because they lack the quantity / unit form, so the graph cannot carry units into its readings."],
    claims=['CLM-9702-12-038', 'CLM-9702-12-039'])

S['047-INTERP'] = dict(
    prompt="A graph's y-axis is labelled T² / s² and its x-axis L / m. Determine what these labels tell a reader before a single point is plotted, and what they fix about any gradient later read from the graph.",
    answer="Reading the labels: the y-axis holds time-squared values in s², the x-axis holds lengths in m - both in the same quantity / unit form as the table columns, so a reader moves between table and graph without converting anything. The labels also fix the gradient's unit before the line is even drawn: a gradient of this graph is Δy ÷ Δx, s² divided by m, so any gradient read from it is in s² m⁻¹ and can be attached to a constant with a name. Unlabelled or unitless axes give gradients that belong to no quantity at all; the labels mean the graph is a measuring instrument, not a sketch.",
    guidance=["Reading: the labels are read as quantity, unit and the column they came from.",
              "Means: the labels mean the gradient's unit is settled in advance - s² m⁻¹ - so every reading off the graph is interpretable."],
    claims=['CLM-9702-12-038', 'CLM-9702-12-039'])

# ---- OBJ-9702-12.2-11 scales fill the grid ----
S['048-APP'] = dict(
    prompt="A learner plots lengths 0.700 m to 1.200 m on an x-axis running from 0 to 2.000 m, because, in the learner's words, zero is where axes start. The plotted points fill only a quarter of the grid. Explain what went wrong and what scale the x-axis needed.",
    answer="The axis was started at zero out of habit, not from the data: with the readings beginning at 0.700 m, a zero start spends most of the grid on the range 0 to 0.700, where no readings sit, so the points occupy only a quarter of the width. Because scales are chosen so the plotted points cover at least half of the grid in both directions - usually by starting each axis just below the smallest reading - this case needed the x-axis started near 0.600 m (a false origin), letting the 0.700-1.200 m readings stretch across the whole grid.",
    guidance=["Situation: this case is the zero-start axis against readings from 0.700 m.",
              "Because: the scale fails because the points cover less than half the grid, so the axis needed to start near the smallest reading."],
    claims=['CLM-9702-12-040', 'CLM-9702-12-041', 'CLM-9702-12-088'])

S['049-INTERP'] = dict(
    prompt="A learner's readings of T² run from 1.55 s² to 2.55 s² and are plotted on a y-axis scaled 0 to 3.0 s². Determine whether this scale fills at least half of the grid in the y-direction, and what the comparison shows about the scale choice.",
    answer="Reading the numbers: the readings span 2.55 − 1.55 = 1.00 s² of a 3.0 s² axis, so the plotted points cover 1.00 ÷ 3.0 = 0.333, which is 33% of the grid in the y-direction - less than half. The comparison shows the scale is wrong for these readings: an axis started at 1.5 s² (a false origin) and running to 2.6 s² would give the same readings 1.00 s² of a 1.1 s² span, over 90% of the grid. So the scale fails the half-the-grid test, and the fix is the standard one - start the axis just below the smallest reading.",
    guidance=["Reading: the span of the readings is read against the span of the axis.",
              "Shows: the numbers show 33% coverage against the at-least-half rule, so the scale fails the stated condition."],
    claims=['CLM-9702-12-040', 'CLM-9702-12-088'])

S['122-MISCON'] = dict(
    prompt="A learner scales a graph with 3 units to a 2 cm square on one axis because it fitted the numbers, and finds every reading off the line needs counting squares. Explain what is wrong with this scale and state the test that catches it.",
    answer="The error: choosing compressed or awkward scales - 3 units to a 2 cm square turns every reading into a mental division, which is where reading errors begin, and the fit was an accident, not a plan. The correct idea: the plotted points fill at least half of the grid in both directions, and each 2 cm square stands for 1, 2 or 5 units times a power of ten, so each small square is a simple fraction and values read off easily. The test that tells them apart is: do the points spread over at least half the grid each way? A scale that passes the fill test but uses 3 or 7 per square still fails the easy-reading half of the rule - both halves are the standard.",
    guidance=["Error: the 3-per-square scale is the error; in fact 1, 2 or 5 units per 2 cm square is what the scale uses.",
              "Test: whether the points spread over at least half the grid each way - that is the check on the scale."],
    claims=['CLM-9702-12-088'], misconception='MC-9702-12-05')

# ---- OBJ-9702-12.2-12 false origin ----
S['050-APP'] = dict(
    prompt="Readings of resistance run from 3.2 Ω to 7.8 Ω, and the learner plots them on a y-axis starting at zero, leaving the points crowded into the top third of the grid. Explain what the axis needed and why.",
    answer="The readings begin a long way from zero, so a zero start wastes the grid below 3.2 Ω where no readings sit, crowding the points into the top third. Because a false origin is used where the readings begin a long way from zero - the axis starts at a convenient value just below the smallest reading - this case needed the y-axis started near 3.0 Ω, so the 3.2-7.8 Ω readings fill the grid instead of a third of it. The false origin is marked with its value, and the labels count up from it, so a reader can see the axis does not start at zero.",
    guidance=["Situation: this case is the zero-start y-axis against readings from 3.2 Ω.",
              "Because: the axis needs a false origin because the readings begin far from zero, so the grid is spent on the data."],
    claims=['CLM-9702-12-042', 'CLM-9702-12-043'])

S['051-INTERP'] = dict(
    prompt="A graph of R against L uses a false origin on the x-axis, labelled starting at 0.400 m. Determine what this axis marking tells a reader, and what it costs the analysis that follows.",
    answer="Reading the axis: the marking at 0.400 m says the x-axis does not start at zero - the readings begin at 0.400 m or just above, and the labels count up from there - so a reader knows the grid is being spent on the data's span rather than on the empty range below it. The cost is in the analysis: the y-intercept can no longer be read off the graph, because the drawn y-axis is at x = 0.400 m, not x = 0, so any intercept the experiment needs must be calculated from c = y − mx with a point on the line. The marking means the choice was visible and honest - the reader can see exactly what was traded.",
    guidance=["Reading: the axis is read from its marked starting value.",
              "Means: the false origin means the intercept must be calculated, not read - that is the cost the marking announces."],
    claims=['CLM-9702-12-042', 'CLM-9702-12-043', 'CLM-9702-12-089'])

# ---- OBJ-9702-12.2-13 easy scales ----
S['052-APP'] = dict(
    prompt="A learner needs to plot readings from 0.020 m to 0.080 m along an axis and considers a scaling of 4 small squares per 0.01 m. Explain why this scale is a poor choice and what scale belongs on the axis.",
    answer="Four squares per 0.01 m means each small square is 0.0025 m - a value no reader can divide by in their head, so every plotted point and every read-off becomes a mental division, which is where reading errors begin. Because scales are chosen as 1, 2 or 5 units to a 2 cm square, times a power of ten, this axis belongs on one of those: 0.01 m per 2 cm square (each small square 0.002 m) or 0.02 m per square, both of which turn the readings into whole numbers of squares. The 1-2-5 rule is not a preference; it is what makes the graph readable to anyone but its author.",
    guidance=["Situation: this case is the 4-squares-per-0.01 m scale.",
              "Because: the scale is poor because it is not 1, 2 or 5 per 2 cm square, so reading the graph turns into arithmetic."],
    claims=['CLM-9702-12-044', 'CLM-9702-12-045'])

S['053-INTERP'] = dict(
    prompt="Two learners plot the same readings. Learner A scales the axis 0.05 m per 2 cm square; learner B scales it 0.03 m per 2 cm square. Determine which learner's graph is easier to read a value from, and what the difference is.",
    answer="Reading the two scales: A's small squares are 0.05 m ÷ 10 = 0.005 m each, so a point at 0.235 m sits 47 small squares up the axis - or, on the labelled lines, between the 0.20 and 0.25 marks, easily placed. B's small squares are 0.003 m each, so the same point sits at 0.235 ÷ 0.003 = 78.333 squares - a value that must be divided out, and the mark lands a third of a square past a count nobody wanted to make. The difference: A's scale is one of the 1-2-5 family, so every reading is a simple fraction of a square and values read off easily; B's turns each plot and each read-off into mental division, which is where reading errors begin. A's graph is the readable one, and it is readable for anyone, not just its author.",
    guidance=["Reading: each scale is read as the size of its small square.",
              "Gives: the comparison gives 0.005 m squares against 0.003 m squares, so the 1-2-5 scale is what the difference is."],
    claims=['CLM-9702-12-044', 'CLM-9702-12-045'])

# ---- OBJ-9702-12.2-14 label along whole axis ----
S['054-APP'] = dict(
    prompt="A learner labels an axis only at its ends: 0 at the start and 1.0 at the finish, with no labels between. Explain what is wrong and what the labelling should be.",
    answer="A two-label axis leaves its whole middle anonymous: a reader wanting to place or check a point at 0.450 must first work out where the middle of the axis is, and counting squares is where mistakes enter. Because numerical labels are written at regular intervals along the whole of each axis, at least every 2 cm, this axis needed labels every 0.1 or 0.2 (whichever the scale makes natural), from 0 to 1.0, so any plotted point can be read against a labelled line. The labels are the graph's addressing scheme, and an address system with two addresses is not one.",
    guidance=["Situation: this case is the two-label axis.",
              "Because: the labelling fails because unlabelled stretches force counting, so regular labels along the whole axis are what the graph needs."],
    claims=['CLM-9702-12-046', 'CLM-9702-12-047'])

S['055-INTERP'] = dict(
    prompt="An axis runs 0, 0.2, 0.4, 0.6, 0.8, 1.0, and each 2 cm square on the grid carries one of these labels. Determine whether this axis meets the labelling standard, and what the regular spacing gives a reader.",
    answer="Reading the axis: labels appear at a constant interval of 0.2, each on its own 2 cm square, running the whole length from 0 to 1.0 - so the axis meets the standard: regular, at least every 2 cm, along the whole of the axis. What the spacing gives: any plotted point can be read against a labelled line rather than counted to - a point between 0.4 and 0.6 sits against small squares that are 0.02 each (0.2 per 2 cm square ÷ 10), so its coordinate is read, not computed. The regular labels are what make the graph a measuring instrument: every position on the axis has an address a reader can use.",
    guidance=["Reading: the interval and extent of the labels are read against the standard.",
              "Gives: the spacing gives every point a labelled line to be read against, so read-offs are readings, not calculations."],
    claims=['CLM-9702-12-046', 'CLM-9702-12-047'])

# ---- OBJ-9702-12.2-15 plot accurately ----
S['056-APP'] = dict(
    prompt="A learner plots points as small filled dots made with a felt-tip marker, each about 2 mm across. Explain what is wrong with this plotting and how the points should be marked.",
    answer="A dot 2 mm across covers the small squares around it, so its position is uncertain by the width of the dot - on a scale of 0.05 m per 2 cm square, that is 0.05 m of doubt planted in every reading. Because points are plotted as small, accurate crosses placed to better than 1 mm, this case needed fine pencil crosses, one stroke on each coordinate, checked against the table before the line is drawn. A cross is honest where a dot is not: two thin strokes hold the reading at their intersection, and the table can be checked against them at any time.",
    guidance=["Situation: this case is the felt-tip dots.",
              "Because: the plotting fails because a dot's width swallows the position, so fine crosses are what the points need."],
    claims=['CLM-9702-12-048', 'CLM-9702-12-049'])

S['057-INTERP'] = dict(
    prompt="A point is plotted as a fine cross at the position of the reading L = 0.650 m on an axis scaled 0.05 m per 2 cm square (small squares of 0.005 m). Determine how accurately a reader can recover the reading from the plotted cross, and what the cross's size has to do with it.",
    answer="Reading the plot: the cross is at 0.650 m, which on this axis sits 13 small squares above 0.585 m's neighbour marks - more simply, between the 0.65 label and its neighbours, on the line. A cross of 1 mm strokes sits within about half a small square of its true position, so a reader can recover the reading to within about 0.0025 m - half of the 0.005 m small square. What the cross's size does: the fine strokes mean the plotted position is the reading, to better than 1 mm on the grid; a 2 mm dot on the same axis would leave the reading uncertain by 0.005 m, a full small square. So the cross is what makes the plotted point a measurement rather than a region.",
    guidance=["Reading: the position is read against the scale, and the cross's width against the small square.",
              "Means: the fine cross means the reading is recoverable to about half a small square, so the plot is a measurement - that is what the size means."],
    claims=['CLM-9702-12-048', 'CLM-9702-12-049'])

# ---- OBJ-9702-12.2-16 line of best fit ----
S['058-APP'] = dict(
    prompt="A learner draws the trend line through the first and last plotted points only, leaving four points visibly off the line - two above, two below, both pairs far from it. Explain what is wrong with this line.",
    answer="A line through just the first and last readings ignores the six readings between them: it is a line drawn by two points, not a trend supported by the data. Because the line of best fit is a single straight line with the points balanced on either side along its whole length - not drawn through the first and last points alone - this case needed the line shifted to balance the four stray points, leaving roughly as many above as below. The two endpoint readings have no special authority: each is one reading with its own scatter, and the line that honours them alone has quietly discarded the rest of the experiment.",
    guidance=["Situation: this case is the endpoint-to-endpoint line.",
              "Because: the line fails because it ignores the middle readings, so a balanced line of best fit is what the data need."],
    claims=['CLM-9702-12-050', 'CLM-9702-12-051'])

S['059-INTERP'] = dict(
    prompt="Six plotted points scatter about a straight trend line as follows, reading left to right: above, above, below, below, above, below. Determine whether this line is behaving as a line of best fit, and what the pattern shows.",
    answer="Reading the pattern: the points alternate around the line - two above, two below, one above, one below - with roughly as many on each side (three above, three below) and the balance holding along the whole length, not just at one end. That is what a line of best fit does: a single straight line with the points balanced on either side, checked over its whole length. The pattern also shows the scatter is random rather than systematic - points alternating above and below is the signature of random reading scatter, whereas points all above at one end and all below at the other would show a curve being forced straight. So the line is behaving, and the scatter it balances is the honest uncertainty of the readings.",
    guidance=["Reading: the positions of the points relative to the line are read along its length.",
              "Shows: the alternating scatter shows a balanced line over random spread - that is what the pattern means."],
    claims=['CLM-9702-12-050', 'CLM-9702-12-051'])

# ---- OBJ-9702-12.2-17 tangents ----
S['060-APP'] = dict(
    prompt="A learner draws a tangent to a curve by laying a ruler through the point of contact and extending the line only 2 cm either side, then reads the gradient from that short stretch. Explain what is wrong with this tangent work.",
    answer="The tangent is drawn too short to be measured: over a 2 cm stretch the same drawing error is divided by a tiny run, and the gradient read from it carries a large percentage uncertainty. Because a tangent is drawn to touch the curve at the point and measured from two widely separated points on the tangent line, this case needed the ruler extended well across the grid - long enough that two points far apart on the tangent can be read - and the gradient taken from those. A short tangent is a guess about the curve's slope at the point; a long one is a measurement of it.",
    guidance=["Situation: this case is the 2 cm tangent.",
              "Because: the tangent fails because it is too short to read, so widely separated points on a long tangent are what the gradient needs."],
    claims=['CLM-9702-12-052'])

S['061-INTERP'] = dict(
    prompt="A curve of distance against time steepens as it runs. A tangent is drawn at t = 2.0 s, and two points on the tangent line read (1.0 s, 2.2 m) and (3.0 s, 8.6 m). Determine what the gradient of this tangent gives and its value.",
    answer="Reading the tangent: the two points lie on the tangent line, far apart, spanning the point of contact at t = 2.0 s. The gradient is Δy ÷ Δx: Δd = 8.6 − 2.2 = 6.4 m, and Δt = 3.0 − 1.0 = 2.0 s, so the gradient is 6.4 ÷ 2.0 = 3.2 m s⁻¹. What it gives: the gradient of a tangent is the gradient of the curve at the point of contact - here, the speed at t = 2.0 s, a rate at an instant, in the unit of the y-axis divided by the unit of the x-axis (m ÷ s = m s⁻¹). Because the curve's gradient changes along it, the value belongs to that point only, which is the whole reason the tangent was drawn there and named.",
    guidance=["Reading: the tangent's two points are read, and the differences taken.",
              "Gives: the working gives 3.2 m s⁻¹, the speed at the instant t = 2.0 s - that is what a tangent's gradient means."],
    claims=['CLM-9702-12-052', 'CLM-9702-12-053'])

if __name__ == '__main__':
    print(len(S), 'slots part 2')
