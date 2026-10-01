#!/usr/bin/env python3
"""Item texts for topic 12, part 3: 12.3 slots (062-117 + MISCON 123-128)."""

S = {}

# ---- OBJ-9702-12.3-01 y = mx + c ----
S['062-CALC'] = dict(
    prompt="The e.m.f. E of a cell and its internal resistance r are related by E = I(R + r), where R is the resistance in the circuit. Calculate the gradient and the intercept expected when V is plotted against I, given V = E − Ir, and state what each gives.",
    answer="""V = E − Ir is in the straight-line form y = mx + c, with V as y and I as x.
The gradient is m = −r, in V A⁻¹: the negative of the internal resistance, because V falls as I grows by r volts per ampere.
The intercept is c = E, in V: the terminal p.d. when no current flows.
So the equation in symbols is V = −rI + E, the substitution is the plot itself - V against I - and the answer is: gradient −r (V A⁻¹) and intercept E (V), each value read off the graph and given with its unit.""",
    guidance=["Equation: the symbols are rearranged into y = mx + c first, so the substitution into the straight-line form is the step that earns the mark.",
              "Answer: the gradient is −r and the intercept is E, so the final values are named with the quantities they give.",
              "Units: the gradient carries V A⁻¹ and the intercept carries V - the unit is what makes each a resistance and an e.m.f."],
    claims=['CLM-9702-12-054', 'CLM-9702-12-055'])

S['063-INTERP'] = dict(
    prompt="A suggested equation is T² = (4π²/k)m + c, where k is a stiffness and c a constant. Determine what must be plotted to give a straight line, and what the gradient and the intercept of that line give.",
    answer="Reading the equation in the y = mx + c form: T² already stands where y belongs, and m stands where x belongs, so the straight line is T² plotted against m - no rearrangement is needed. The gradient of that line is 4π²/k, in s² kg⁻¹, so k = 4π² ÷ gradient, and the intercept is c, in s². So the graph means: plot T² / s² on the y-axis against m / kg on the x-axis, read the gradient and the intercept, and recover the stiffness by dividing 4π² by the gradient - the equation is what decided the plot.",
    guidance=["Reading: the equation is read as a straight-line form, and the plot follows from it.",
              "Means: the gradient means 4π²/k and the intercept means c, so the constants are what the graph gives."],
    claims=['CLM-9702-12-054', 'CLM-9702-12-055'])

S['064-EVAL'] = dict(
    prompt="A graph of R against L for a wire is a straight line, and the suggested equation is R = (ρ/A)L + r. Explain whether the data support this equation, using the graph's behaviour as the criterion and naming the values the comparison rests on.",
    answer="""The criterion stated first: if R = (ρ/A)L + r holds, the graph of R against L must be a straight line through readings that scatter randomly about it, and the intercept must be a constant r, the same whatever the data's trust.
The judgement: the plotted points lie close to a single straight line, balanced either side along its whole length, which is the behaviour the equation predicts - so the data are consistent with the suggested equation, because a straight line is what (ρ/A)L + r requires of R against L.
The values compared: the gradient gives ρ/A (in Ω m⁻¹) and the intercept gives r (in Ω); the percentage scatter of the points about the line, a few percent, is the uncertainty the values carry. The support is conditional on that scatter, so the conclusion names it: consistent, within the few percent the points show.""",
    guidance=["Criterion: the straight-line behaviour is stated as the support test before the judgement is made.",
              "Because: the data support the equation because a straight line is what the equation predicts, since the graph is the evidence.",
              "Values: the gradient, intercept and the few-percent scatter of the points are the values the judgement rests on."],
    claims=['CLM-9702-12-054', 'CLM-9702-12-068'])

S['065-APP'] = dict(
    prompt="A learner is told the equation R = (ρ/A)L + r and plots R against L, but then quotes ρ as being about the gradient. Explain what is wrong with this reading of the graph.",
    answer="The gradient of R against L is ρ/A, not ρ: the area is still dividing, because the equation says the resistance per unit length is ρ/A, and quoting the gradient as ρ drops a whole measured quantity out of the answer. Because the constant is found from the graph by reading the gradient and then multiplying by A (the measured cross-section, in m²), ρ = gradient × A, this case needed the area measurement brought in: a gradient of 12.0 Ω m⁻¹ with A = 0.123 mm² = 1.23 × 10⁻⁷ m² gives ρ = 12.0 × 1.23 × 10⁻⁷ = 1.476 × 10⁻⁶ Ω m. The graph gives ρ/A; the micrometer gives A; the answer needs both.",
    guidance=["Situation: this case is the gradient quoted as ρ.",
              "Because: the reading is wrong because the area divides in the equation, so ρ = gradient × A is what the graph needs to finish the constant."],
    claims=['CLM-9702-12-055', 'CLM-9702-12-069'])

S['124-MISCON'] = dict(
    prompt="A graph of T² against L uses a false origin on the x-axis (starting at 0.200 m), and a learner reads the y-intercept straight off the drawn y-axis, announcing it as c. Explain what is wrong with this and state the test that catches it.",
    answer="The error: reading the y-intercept off an axis that does not start at x = 0 - the drawn y-axis is at L = 0.200 m, not at zero, so the value where the line meets it is T² at 0.200 m, not the intercept c. The correct idea: with a false origin, calculate the intercept from c = y − mx, using the gradient and one point on the line - a point (0.250 m, 1.01 s²) on a line of gradient 4.00 s² m⁻¹ gives c = 1.01 − 4.00 × 0.250 = 1.01 − 1.00 = 0.01 s². The test that tells them apart is: does the x-axis start at zero? If it does not, the intercept is calculated, never read off the axis.",
    guidance=["Error: the axis read as the intercept is the error; in fact a false origin means the intercept is calculated from c = y − mx.",
              "Test: whether the x-axis starts at zero - that is the check that decides read-or-calculate."],
    claims=['CLM-9702-12-089'], misconception='MC-9702-12-07')

# ---- OBJ-9702-12.3-02 read coordinates ----
S['066-CALC'] = dict(
    prompt="Two points on a trend line of a graph of R against L read (0.400 m, 4.8 Ω) and (0.900 m, 9.6 Ω). Calculate the differences ΔR and ΔL between the coordinates, showing the subtraction.",
    answer="""ΔR = R₂ − R₁ = 9.6 − 4.8 = 4.8 Ω
ΔL = L₂ − L₁ = 0.900 − 0.400 = 0.500 m
The subtraction is the whole step: each difference is a later reading minus an earlier one, both read from the line, and each carries its unit because the coordinates did. These differences are what a gradient divides: ΔR ÷ ΔL = 4.8 ÷ 0.500 = 9.60 Ω m⁻¹, the gradient of the line.""",
    guidance=["Equation: the differences are the named quantities, Δy and Δx, so the substitution is the two subtractions.",
              "Answer: ΔR = 4.8 Ω and ΔL = 0.500 m, so the final values are the differences the gradient needs.",
              "Units: each difference carries the unit of its axis, so the quotient will carry Ω m⁻¹ - the unit travels with the reading."],
    claims=['CLM-9702-12-056', 'CLM-9702-12-057'])

S['067-INTERP'] = dict(
    prompt="A learner needs a point on the trend line near the middle of the graph and reads it as (0.55, 1.9), writing no units. Determine what is wrong with this reading and how it should have been written.",
    answer="Reading the value: 0.55 and 1.9 are the bare numbers of the coordinates, but a point read from a line is a pair of quantities, and a bare number cannot enter an equation or a gradient. Because a point read from the line is written with both coordinates and their units - the units are what make the reading a value of length and a value of time-squared - this reading should have been written (0.55 m, 1.9 s²) on a graph of T² against L. The omission matters downstream: a gradient calculated from unitless points gives a unitless number, and a unitless gradient names no constant at all.",
    guidance=["Reading: the point is read as two values, and the omission shows at once.",
              "Means: units mean the coordinates are quantities - without them the reading cannot support a gradient, so the writing is what fails."],
    claims=['CLM-9702-12-056', 'CLM-9702-12-057'])

S['068-EVAL'] = dict(
    prompt="Two learners read the same point on a trend line. Learner A reads (0.550 m, 1.90 s²); learner B reads (0.560 m, 1.88 s²). Explain whether their difference matters, stating a criterion for what a reading off a line is worth.",
    answer="""The criterion stated first: a reading off a trend line is honest to about half a small square on the grid - the smallest division the scale resolves - so two readings of the same point are expected to differ by up to that much, and no more.
The comparison: on a scale of 0.05 m per 2 cm square and 0.1 s² per 2 cm square, half a small square is 0.0025 m in x and 0.005 s² in y. The learners differ by 0.010 m and 0.02 s² - several small squares, more than the criterion allows.
The judgement: the difference is larger than reading error alone explains, because the criterion (half a small square) is what the graph honestly resolves; so at least one learner has misjudged the crossing, and the readings should be taken again, against the labelled lines, from directly above. The difference matters: it is above the graph's own resolution, so it is a discrepancy, not a scatter.""",
    guidance=["Criterion: half a small square is the standard stated before the judgement.",
              "Because: the difference is judged against the criterion, so the reasoning shows what the data support.",
              "Values: 0.010 m and 0.02 s² against 0.0025 m and 0.005 s² - the numbers are what the conclusion rests on."],
    claims=['CLM-9702-12-056', 'CLM-9702-12-057'])

S['069-APP'] = dict(
    prompt="A learner reads a coordinate from the trend line by looking at the point from the side of the graph, at an angle to the grid. Explain what goes wrong here and how the reading should be taken.",
    answer="A reading taken at an angle to the grid misplaces the point against both scales at once - the eye is not directly above the crossing, so the coordinate picked up is the one the angled view shows, which is not the one the line holds. Because coordinates are read from the trend line at the intersection of labelled lines, with the reading taken squarely against the scale, this case needed the reader's eye over the crossing, reading each coordinate straight up its own axis. The parallax that bends pointer readings on an instrument does the same to readings on a grid, and the cure is the same: look squarely, then read.",
    guidance=["Situation: this case is the angled reading off the grid.",
              "Because: the reading goes wrong because the angled view misplaces the crossing, so square sighting is what the grid needs."],
    claims=['CLM-9702-12-056'])

# ---- OBJ-9702-12.3-03 gradient ----
S['070-CALC'] = dict(
    prompt="A graph of T² / s² against L / m has a straight trend line. Two points on the line read (0.250 m, 1.01 s²) and (0.650 m, 2.61 s²). Calculate the gradient of the line.",
    answer="""Gradient = Δy ÷ Δx
Δy = 2.61 − 1.01 = 1.60 s²
Δx = 0.650 − 0.250 = 0.400 m
Gradient = 1.60 ÷ 0.400 = 4.00 s² m⁻¹
The unit is s² divided by m, from the axes; the value is 4.00 s² m⁻¹ to three significant figures, matching the readings it came from.""",
    guidance=["Equation: gradient = Δy ÷ x, so the substitution is the two differences over each other.",
              "Answer: the working gives 1.60 ÷ 0.400 = 4.00, so the final gradient is 4.00 s² m⁻¹.",
              "Units and significant figures: s² m⁻¹ from the axes, three significant figures from the readings."],
    claims=['CLM-9702-12-058'])

S['071-INTERP'] = dict(
    prompt="A learner calculates a gradient from two readings in the table that sit on either side of the trend line, one just above it and one just below. Determine what is wrong with using those two readings and what the gradient should be taken from.",
    answer="Reading the situation: the two values are data points, and data points sit off the line - the line of best fit was drawn precisely to average out that scatter, so a gradient taken from two points that are not on the line drags their individual scatter back into the answer. The gradient should be taken from two points on the line itself, far apart, covering at least half the drawn line: the line carries the whole data set behind it, and the two readings it replaces each carried only themselves. The habit the check enforces: read the line, not the table, once the line is drawn - the table's turn is over, and the gradient belongs to the graph.",
    guidance=["Reading: the data points are read for what they are - off the line.",
              "Means: the mistake means the gradient is being taken from scatter, so the line itself is what the gradient needs."],
    claims=['CLM-9702-12-058', 'CLM-9702-12-090'])

S['072-EVAL'] = dict(
    prompt="Learner A takes a gradient from two points on the trend line 4 cm apart; learner B takes one from two points 16 cm apart, on the same line. Explain which gradient to trust more, with the criterion that decides it.",
    answer="""The criterion stated first: a reading off the line carries a doubt of about half a small square either way, so the gradient's percentage uncertainty scales with the run - the same reading doubt over a longer run is a smaller percentage.
The comparison: over 4 cm, the reading doubt of half a small square is spread over a few squares, and the gradient's percentage uncertainty is several percent; over 16 cm, the same doubt is divided by four times the run, and the percentage uncertainty is a few percent at most.
The judgement: learner B's gradient is the one to trust, because the large triangle gives the smaller percentage uncertainty - the same plotting error over a longer base - and the criterion (percentage uncertainty falling with run) is what decides it. Learner A's answer may happen to be close, but its trust is thinner, and the trust is what the comparison asked for.""",
    guidance=["Criterion: the percentage uncertainty scales with run - stated before the judgement.",
              "Because: B is trusted because the same error divides by a longer base, so the reasoning follows the stated criterion.",
              "Values: half a small square over 4 cm against over 16 cm - the numbers are what the judgement compares."],
    claims=['CLM-9702-12-059', 'CLM-9702-12-090'])

S['073-APP'] = dict(
    prompt="A learner, short of time, takes a gradient from two points on the line that are 3 small squares apart, because they were right there. Explain what this costs and what the learner should have done.",
    answer="A 3-square run gives the gradient a large percentage uncertainty: the half-square doubt of reading the line is spread over a run of three squares, so the gradient carries perhaps a sixth of itself as doubt - and a constant determined from it is barely a constant. Because the gradient uses two points on the line that are far apart, covering at least half the drawn line, the learner should have read a point at each end of the line, where the run is longest and the same reading doubt is divided by twenty squares instead of three. The two points at hand were convenient, and convenience is the one thing a gradient cannot be built from.",
    guidance=["Situation: this case is the 3-square gradient.",
              "Because: the cost is a large percentage uncertainty, so far-apart points on the line are what the gradient needs."],
    claims=['CLM-9702-12-058', 'CLM-9702-12-090'])

S['123-MISCON'] = dict(
    prompt="A learner calculates a gradient using the first and last data points in the table, which lie off the line of best fit. Explain what is wrong with this and state the test that catches it.",
    answer="The error: using data points that are not on the line for a gradient - the line of best fit was drawn to average the scatter of all the readings, and going back to two of the readings drags their individual scatter straight into the answer. The correct idea: read two points on the line itself, far apart, covering at least half the drawn line, and show them - the line carries the whole data set, while each data point carries only itself. The test that tells them apart is: are both points on the line and far apart? Points from the table fail the first half; points close together fail the second.",
    guidance=["Error: the table-points gradient is the error; in fact the gradient is read from the line itself.",
              "Test: whether both points are on the line and far apart - that is the check on any gradient triangle."],
    claims=['CLM-9702-12-090'], misconception='MC-9702-12-06')

# ---- OBJ-9702-12.3-04 intercept ----
S['074-CALC'] = dict(
    prompt="A graph of R against L uses a false origin at L = 0.400 m. The trend line's gradient is 12.0 Ω m⁻¹, and one point on the line reads (0.500 m, 4.8 Ω). Calculate the y-intercept of the line.",
    answer="""c = y − mx
c = 4.8 − 12.0 × 0.500
c = 4.8 − 6.00 = −1.20 Ω
The intercept is −1.20 Ω to three significant figures: the line crosses below zero, and because the axis is a false origin the intercept could not be read off the grid - it is calculated from a point on the line, which is the only honest route.""",
    guidance=["Equation: c = y − mx is the formula, so the substitution is the point and the gradient.",
              "Answer: 4.8 − 6.00 = −1.20, so the final intercept is −1.20 Ω.",
              "Units and significant figures: Ω from the y-axis, three significant figures matching the readings."],
    claims=['CLM-9702-12-060', 'CLM-9702-12-061'])

S['075-INTERP'] = dict(
    prompt="A trend line meets the drawn y-axis of a graph whose x-axis starts at zero. The meeting point reads 0.8 N on the y-axis scale. Determine whether this is the y-intercept, and what would change if the x-axis started at 0.300 m instead.",
    answer="Reading the axis: the x-axis starts at zero, so the drawn y-axis is the line x = 0, and the value where the trend meets it - 0.8 N - is the y-intercept, read straight off the graph. If the x-axis started at 0.300 m instead, that same drawn edge would be at x = 0.300 m, and the 0.8 N meeting would be the value of y at 0.300 m, not the intercept - the intercept would then have to be calculated, from c = y − mx with a point on the line, rather than read. So whether a meeting point is the intercept is decided entirely by where the x-axis starts: read off when it starts at zero, calculated when it does not.",
    guidance=["Reading: the axis start is read first, then the meeting point.",
              "Means: the reading means the intercept only where x = 0 is drawn - the axis start is what the meaning turns on."],
    claims=['CLM-9702-12-060', 'CLM-9702-12-089'])

S['076-EVAL'] = dict(
    prompt="A learner reads a small intercept off a graph by eye, saying it looks like about 0.3. The scale is 0.5 Ω per 2 cm square. Explain whether this reading is good enough, stating the criterion.",
    answer="""The criterion stated first: a reading taken by eye off a graph is honest to about half a small square - here, 0.25 Ω per small square's half, so 0.025 Ω... on a scale of 0.5 Ω per 2 cm square, half a small square is 0.025 Ω, and any by-eye value carries at least that much doubt, plus the judgement of where the line crosses.
The comparison: the value itself is about 0.3 Ω, and the doubt of the by-eye reading is of the same order as the value - a reading whose uncertainty is most of the reading says nothing.
The judgement: not good enough, because where the intercept is small compared with the readings it is found by calculation from c = y − mx, using a point on the line - the calculation carries no by-eye doubt, and the criterion (doubt small against value) is what rejects the reading. The eye cannot judge a small offset on a large scale; the arithmetic can, exactly.""",
    guidance=["Criterion: the by-eye doubt is stated against the value before the judgement.",
              "Because: the reading is rejected because its uncertainty is comparable with the value, so the calculation is the justified route.",
              "Values: 0.3 Ω against a by-eye doubt of order 0.1 Ω - the numbers are what the conclusion rests on."],
    claims=['CLM-9702-12-061'])

S['077-APP'] = dict(
    prompt="A graph of T² against L is plotted with a false origin at L = 0.200 m. A learner announces the intercept as the value where the line hits the side of the grid. Explain what is wrong here.",
    answer="The side of the grid is the drawn y-axis, and with a false origin at 0.200 m that edge is at L = 0.200 m, not at zero - so the value where the line meets it is T² at 0.200 m, a reading, not the intercept. Because the y-intercept is the value of y where the line crosses x = 0, and an axis that does not show zero cannot be read for it, this case needed the intercept calculated: c = y − mx, from the gradient and a point on the line. The learner has read a boundary of the paper and called it a constant of the physics.",
    guidance=["Situation: this case is the grid-edge reading called an intercept.",
              "Because: the reading is wrong because the false origin moves x = 0 off the grid, so the intercept needs calculating from a point on the line."],
    claims=['CLM-9702-12-060', 'CLM-9702-12-089'])

# ---- OBJ-9702-12.3-05 absolute uncertainty ----
S['078-CALC'] = dict(
    prompt="A metre rule reads to 1 mm. A length is measured as a single reading of 245 mm. Calculate the absolute uncertainty in the reading; then calculate the absolute uncertainty in the difference of two readings, 245 mm and 238 mm.",
    answer="""Single reading: the absolute uncertainty is half the resolution, so 1 ÷ 2 = 0.5, giving ± 0.5 mm.
Difference: each reading brings its own ± 0.5 mm, and the difference inherits both: 0.5 + 0.5 = 1.0, so the difference of 245 − 238 = 7 mm carries ± 1.0 mm.
The answers: ± 0.5 mm for the single reading, ± 1.0 mm for the difference - doubling the readings doubled the doubt, which is why a length measured as a difference of two rule readings is a less certain quantity than a length read once.""",
    guidance=["Equation: half the resolution for one reading, the sum for a difference - so the substitution names which case each value is.",
              "Answer: ± 0.5 mm and ± 1.0 mm, so the final values are stated with their signs.",
              "Units: millimetres throughout, so the unit is what ties each doubt to its reading."],
    claims=['CLM-9702-12-062'])

S['079-INTERP'] = dict(
    prompt="A learner measures the extension of a spring as the difference between the loaded length and the unloaded length, both read on a millimetre rule. Determine what the absolute uncertainty in the extension is, and how it compares with the uncertainty in a single length reading.",
    answer="Reading the method: the extension is a difference of two readings - the loaded length minus the unloaded length - and each rule reading carries ± 0.5 mm (half the 1 mm resolution). The difference inherits both: 0.5 + 0.5 = 1.0, so the extension carries ± 1.0 mm, twice the doubt of a single reading. The comparison shows the cost of the method: a quantity built from two readings is always less certain than a reading alone, and where the extension is small (a few mm), ± 1.0 mm is a large share of the answer - which is why a method that measures the extension directly, or a finer instrument, is worth having.",
    guidance=["Reading: the extension is read as a difference of two readings, and the estimate follows.",
              "Means: the sum of the two doubts means ± 1.0 mm - that is what the difference costs."],
    claims=['CLM-9702-12-062'])

S['080-EVAL'] = dict(
    prompt="A learner with a micrometer that reads 0.02 mm when fully closed measures a wire's diameter as 0.34 mm and quotes ± 0.01 mm as the uncertainty. Explain whether that uncertainty is honest, stating the criterion and the correct value.",
    answer="""The criterion stated first: a systematic error such as a zero error shifts every reading by the same amount and survives any number of repeats, so the uncertainty quoted must account for it - and a single reading's random uncertainty is half the resolution.
The comparison: the micrometer shows a zero error of 0.02 mm, which belongs in the reading as a correction (0.34 − 0.02 = 0.32 mm) and in the doubt as a systematic contribution; the quoted ± 0.01 mm covers only the random half-resolution of the instrument and leaves the known 0.02 mm offset unaccounted.
The judgement: not honest, because a quoted uncertainty that ignores a measured zero error claims the reading is more certain than the instrument itself showed it to be. The correct treatment: subtract the zero error to give 0.32 mm, and quote the uncertainty with the systematic contribution included - the doubt is larger than ± 0.01 mm, and saying so is the point of quoting it.""",
    guidance=["Criterion: a systematic error must be corrected and its doubt acknowledged - stated before the judgement.",
              "Because: the quote is rejected because the zero error was measured and left out, so the claim of precision fails its own instrument.",
              "Values: 0.02 mm of zero error against a quoted ± 0.01 mm - the numbers are what the judgement rests on."],
    claims=['CLM-9702-12-062', 'CLM-9702-12-063'])

S['081-APP'] = dict(
    prompt="A learner measures the internal resistance of a cell by taking terminal p.d. readings at two different currents, then says the uncertainty in each reading (± 0.05 V) is basically nothing because the meter is digital. Explain what is wrong with this claim here.",
    answer="A digital meter still carries an uncertainty in each reading - its last displayed digit is its resolution, and half of that is the doubt on a single reading - so the claim of basically nothing is not an estimate, it is an omission. Because the internal resistance is calculated from a difference of two p.d. readings, the difference inherits both doubts: 0.05 + 0.05 = 0.1 V, and on a difference of perhaps 0.3 V that is 33% - the largest uncertainty in the whole experiment, from the instrument the learner trusted most. In this case the claim fails exactly where it was made: the readings were good, and the calculation built from them was not.",
    guidance=["Situation: this case is the digital-meter reading called certain.",
              "Because: the claim fails because differences inherit both readings' doubts, so the percentage uncertainty in the calculated quantity is what the claim overlooked."],
    claims=['CLM-9702-12-062', 'CLM-9702-12-091'])

# ---- OBJ-9702-12.3-06 percentage uncertainty ----
S['082-CALC'] = dict(
    prompt="A period is measured as 0.875 s with an absolute uncertainty of ± 0.005 s. Calculate the percentage uncertainty in the period.",
    answer="""Percentage uncertainty = (absolute uncertainty ÷ value) × 100%
= (0.005 ÷ 0.875) × 100%
= 0.00571 × 100% = 0.571%
The percentage uncertainty is 0.57% to two significant figures. Translating back the other way, the absolute uncertainty is 0.57 ÷ 100 × 0.875 = 0.005 s, as given - the two forms carry the same information in different units.""",
    guidance=["Equation: percentage = (absolute ÷ value) × 100%, so the substitution is the division first.",
              "Answer: 0.005 ÷ 0.875 = 0.00571, so the final value is 0.57%.",
              "Units: a percentage carries no unit, so the answer is stated as a percentage and the translation back is shown in s."],
    claims=['CLM-9702-12-064'])

S['083-INTERP'] = dict(
    prompt="In one experiment a length of 800 mm carries ± 0.5 mm; in another a diameter of 0.30 mm carries ± 0.01 mm. Determine which measurement has the larger percentage uncertainty, and what that means for the experiment that uses both.",
    answer="Reading the two: the length's percentage uncertainty is 0.5 ÷ 800 = 0.000625, which is 0.063%; the diameter's is 0.01 ÷ 0.30 = 0.0333, which is 3.3%. The diameter has the larger percentage uncertainty - fifty times larger - even though its absolute doubt is fifty times smaller. What that means for the experiment: the diameter is the weaker measurement, and where the diameter enters a calculation squared (as in an area), its share doubles to over 6%, so it dominates the final uncertainty. The comparison by percentage, not by absolute doubt, is what shows it: the small instrument doubt on the small quantity is the one to worry about.",
    guidance=["Reading: each measurement is read as a share of itself.",
              "Means: 0.063% against 3.3% means the diameter is the weak measurement - the percentage is what the comparison runs on."],
    claims=['CLM-9702-12-064', 'CLM-9702-12-077'])

S['084-EVAL'] = dict(
    prompt="A learner calculates a wire's cross-section area from a diameter measured to 2% and uses it in ρ = gradient × A, quoting the resistivity to 2%. Explain whether that uncertainty claim is justified, stating the criterion.",
    answer="""The criterion stated first: in a product or quotient the percentage uncertainties of the measured quantities add, so the resistivity's uncertainty is the sum of the shares of everything measured into it - here the gradient's percentage uncertainty and the area's.
The comparison: the area comes from πd²/4, so its percentage uncertainty is twice the diameter's 2%, which is 4%; the gradient carries its own few percent from the graph (say 3%); the sum is 4% + 3% = 7%, not 2%.
The judgement: not justified, because the claimed 2% is the diameter's share alone, and the calculation it feeds squares that share into the area and adds the gradient's - the criterion (percentage uncertainties add in a product) is what the claim ignored. The honest quote is about 7%, and an honest 7% is worth more than a claimed 2% that the working does not support.""",
    guidance=["Criterion: percentage uncertainties add in a product, and a squared quantity doubles - stated before the judgement.",
              "Because: the claim fails because the shares add, so the quoted figure is smaller than the working supports.",
              "Values: 4% (the doubled diameter share) + 3% (the gradient) = 7%, against the claimed 2% - the numbers decide it."],
    claims=['CLM-9702-12-065'])

S['085-APP'] = dict(
    prompt="A learner says the area of a wire's cross-section, calculated from a diameter measured to 1%, carries about 1% of uncertainty because, in the learner's words, it is all one measurement. Explain what is wrong with this estimate.",
    answer="The area is πd²/4: the diameter enters squared, and a value raised to a power n carries n times the percentage uncertainty of the quantity - so 1% in the diameter becomes 2% in the area, not 1%. Because the estimate treated a squared quantity as though it were the quantity itself, it understated the area's uncertainty by half; and where the area then feeds a resistivity or a density, the understated share propagates into the final answer. In this case the honest chain is: 1% in d, 2% in A, and the sum of A's share with the gradient's share in whatever A multiplies into.",
    guidance=["Situation: this case is the squared-share estimate.",
              "Because: the estimate fails because squaring doubles the percentage uncertainty, so the power rule is what the area's doubt follows."],
    claims=['CLM-9702-12-065'])

S['130-MISCON'] = dict(
    prompt="A learner finds the temperature drop across a block as 25.4 °C − 21.2 °C = 4.2 °C and assigns it the uncertainty of one thermometer reading, ± 0.5 °C, calling it the thermometer's uncertainty. Explain what is wrong and state the test that catches it.",
    answer="The error: finding the percentage uncertainty of a difference from one reading alone - the 4.2 °C is a difference of two readings, and each brings its own ± 0.5 °C, so the difference carries 0.5 + 0.5 = 1.0 °C, giving 1.0 ÷ 4.2 = 0.238, which is 24% - half again the claimed share. The correct idea: for a difference, add the two absolute uncertainties, then divide by the difference itself. The test that tells them apart is: is the quantity a difference of two readings? If it is, both doubts travel with it, and the percentage uncertainty is far larger than one reading suggests.",
    guidance=["Error: the one-reading uncertainty on a difference is the error; in fact both readings' doubts are added first.",
              "Test: whether the quantity is a difference of two readings - that is the check that decides the estimate."],
    claims=['CLM-9702-12-091'], misconception='MC-9702-12-13')

# ---- OBJ-9702-12.3-07 half the range ----
S['086-CALC'] = dict(
    prompt="Five repeats of a timing are: 17.4 s, 17.6 s, 17.5 s, 17.2 s, 17.7 s. Calculate the absolute uncertainty and the mean of the repeats.",
    answer="""Range = largest − smallest = 17.7 − 17.2 = 0.5 s
Absolute uncertainty = half the range = 0.5 ÷ 2 = 0.25 s
Mean = (17.4 + 17.6 + 17.5 + 17.2 + 17.7) ÷ 5 = 87.4 ÷ 5 = 17.48 s
The timing is 17.5 s ± 0.25 s to three significant figures - the mean as the value, half the range as its doubt, since the repeats scatter randomly about a steady value.""",
    guidance=["Equation: half the range for the uncertainty, the sum divided by the count for the mean - so the substitution names both.",
              "Answer: 0.5 ÷ 2 = 0.25 and 87.4 ÷ 5 = 17.48, so the final value is 17.5 s ± 0.25 s.",
              "Units: seconds throughout, so the mean and the doubt carry the same unit - the timing is quoted complete."],
    claims=['CLM-9702-12-066', 'CLM-9702-12-092'])

S['087-INTERP'] = dict(
    prompt="A learner's four repeats of a diameter are 0.46 mm, 0.48 mm, 0.46 mm and 0.48 mm, and the learner quotes the uncertainty as 0.48 − 0.46 = 0.02 mm. Determine what the quoted value actually is and what the uncertainty should have been.",
    answer="Reading the working: 0.48 − 0.46 = 0.02 mm is the range of the repeats, not the uncertainty - the range is the full spread, and the estimate the repeats support is half of it. The absolute uncertainty is 0.02 ÷ 2 = 0.01 mm, so the diameter is the mean with half the range as its doubt: mean = (0.46 + 0.48 + 0.46 + 0.48) ÷ 4 = 1.88 ÷ 4 = 0.47 mm, quoted 0.47 mm ± 0.01 mm. The quoted 0.02 mm is not wrong as a number - it is the range - but as an uncertainty it doubles the honest doubt, and the test that separates them is whether the range is divided by two.",
    guidance=["Reading: the quoted value is read for what it is - the undivided range.",
              "Means: the range means the spread, so half of it means the uncertainty - that is what the quote needed."],
    claims=['CLM-9702-12-066', 'CLM-9702-12-092'])

S['088-EVAL'] = dict(
    prompt="A learner's repeats of a mass reading climb steadily: 46.0 g, 46.2 g, 46.5 g, 46.9 g. The learner halves the range and quotes the mass as 46.4 g ± 0.45 g. Explain whether the half-range estimate is honest here, stating the criterion.",
    answer="""The criterion stated first: half the range is appropriate where repeats scatter randomly about a steady value - readings wandering up and down with no direction.
The comparison: these repeats do not scatter - they climb steadily, 0.2 g then 0.3 g then 0.4 g at a time, which is drift, not random scatter: something in the apparatus is changing (a balance still settling, water evaporating, a draught), so the four readings are not four measurements of one value.
The judgement: the half-range quote is not honest here, because the scatter is not random and half the range then understates the real uncertainty - the drift between first and last reading is a change in the quantity itself. The honest response is to name the drift as the dominant effect: quote the mean with a larger doubt (or the trend), and record that the readings climbed - the criterion (random scatter) is what the data fail.""",
    guidance=["Criterion: half the range needs random scatter - stated before the judgement.",
              "Because: the quote is rejected because the readings drift in one direction, so the spread is not scatter but change.",
              "Values: the climbs of 0.2 g, 0.3 g and 0.4 g are the values that show the drift - the numbers are the evidence."],
    claims=['CLM-9702-12-066', 'CLM-9702-12-067'])

S['089-APP'] = dict(
    prompt="A learner quotes a mean of three repeats as 2.45 g, and when asked for the uncertainty, says the repeats were all pretty much the same. Explain what is wrong with this answer at the bench.",
    answer="The repeats are the evidence the uncertainty is built from, and the answer throws the evidence away: the phrase pretty much the same names no spread, and the uncertainty from repeats is half the range of them - a number, or it is nothing. Because the repeats scatter randomly about a steady value (even 2.44 g, 2.45 g, 2.46 g scatter by 0.02 g), the honest quote is the mean with half the range: 2.45 g ± 0.01 g. The uncertainty is not decoration on the value; it is the measurement of how much the readings deserved to be trusted, and it is sitting in the learner's own table, unhalved.",
    guidance=["Situation: this case is the all-the-same answer.",
              "Because: the answer fails because the repeats' range is the estimate the uncertainty needs, so the spread - not an adjective - is what the quote requires."],
    claims=['CLM-9702-12-066', 'CLM-9702-12-092'])

S['125-MISCON'] = dict(
    prompt="A learner times 20 oscillations three times, getting 15.2 s, 15.4 s and 15.6 s, and announces the uncertainty as 0.4 s - the full spread. Explain what is wrong and state the test that catches it.",
    answer="The error: forgetting to halve the range when estimating uncertainty from repeated readings - 15.6 − 15.2 = 0.4 s is the range, the full spread of the repeats, and quoting it as the uncertainty doubles the honest doubt. The correct idea: the absolute uncertainty is half the range, ½ × (largest − smallest) = 0.4 ÷ 2 = 0.2 s, and the timing is the mean with it: mean = (15.2 + 15.4 + 15.6) ÷ 3 = 46.2 ÷ 3 = 15.4 s, quoted 15.4 s ± 0.2 s. The test that tells them apart is: is the range divided by two? The range measures the spread both sides of the mean; the uncertainty is one side of it.",
    guidance=["Error: the unhalved range as the uncertainty is the error; in fact half the range is the estimate.",
              "Test: whether the range is divided by two - that is the check on any repeat-based uncertainty."],
    claims=['CLM-9702-12-092'], misconception='MC-9702-12-08')

# ---- OBJ-9702-12.3-08 conclusions and constants ----
S['090-CALC'] = dict(
    prompt="A graph of R against L for a wire of cross-section area A = 1.23 × 10⁻⁷ m² has gradient 12.0 Ω m⁻¹ and y-intercept −1.20 Ω. The suggested equation is R = (ρ/A)L + r. Calculate ρ and r from the graph.",
    answer="""Gradient = ρ/A, so ρ = gradient × A
ρ = 12.0 × 1.23 × 10⁻⁷ = 1.476 × 10⁻⁶ Ω m
Intercept = r, read straight from the graph:
r = −1.20 Ω
The constants are ρ = 1.48 × 10⁻⁶ Ω m to three significant figures (the gradient and the area each carry three) and r = −1.20 Ω - each with its unit, which is what makes them values rather than numbers.""",
    guidance=["Equation: ρ = gradient × A and r = intercept, so the substitution is the graph's two readings times the measured area.",
              "Answer: 12.0 × 1.23 × 10⁻⁷ = 1.476 × 10⁻⁶, so the final values are ρ = 1.48 × 10⁻⁶ Ω m and r = −1.20 Ω.",
              "Units: Ω m for the resistivity (Ω m⁻¹ times m²) and Ω for the internal resistance - the units are what the constants are."],
    claims=['CLM-9702-12-068', 'CLM-9702-12-069'])

S['091-INTERP'] = dict(
    prompt="An experiment ends with a straight-line graph whose gradient is 4.00 s² m⁻¹ and whose intercept is 0.01 s², with the points scattered about 2% along the line. Determine what the conclusion of the experiment should state, and what the 2% adds to it.",
    answer="Reading the graph's three outputs: a gradient of 4.00 s² m⁻¹, an intercept of 0.01 s², and a scatter of about 2% of the readings. The conclusion states the constants the equation asked for - from T² = (4π²/k)L + c, the gradient gives k = 4π² ÷ 4.00 = 3.14159 × 4 ÷ 4.00... worked: 4π² = 39.478, and k = 39.478 ÷ 4.00 = 9.87 N m⁻¹ (a stiffness, in newtons per metre, once the mass side of the equation is included), and the intercept gives c = 0.01 s². What the 2% adds: the constants are quoted with the scatter as their uncertainty - k = 9.87 N m⁻¹ to within about 2% - because a constant without a stated trust is a number pretending to be exact, and the scatter is the measurement of the trust.",
    guidance=["Reading: the gradient, intercept and scatter are read as the graph's three outputs.",
              "Means: the conclusion means the constants with their units and their 2% trust - that is what the graph was for."],
    claims=['CLM-9702-12-068', 'CLM-9702-12-069'])

S['092-EVAL'] = dict(
    prompt="A learner concludes an experiment with the sentence that the experiment went well and the results are good. Explain whether this is a conclusion, stating what a conclusion must contain.",
    answer="""The criterion stated first: a conclusion is drawn from the graph - the constants of the equation from the gradient and the intercept, with their units, and the scatter of the points as the stated trust.
The comparison: the sentence contains no value, no unit, no constant, and no statement of trust - it is a verdict on the experimenter, not a result of the experiment, and nothing in it could be checked by a reader.
The judgement: it is not a conclusion, because the criterion asks for what the graph gives and the sentence gives none of it - the data's support for the equation, the constants with their units, and the few-percent scatter are what "good" would have to mean, stated as numbers. A conclusion a reader can check is the whole point of the practical method; a verdict is not checkable by anyone.""",
    guidance=["Criterion: constants from gradient and intercept, with units and stated trust - stated before the judgement.",
              "Because: the sentence fails because it contains no value the criterion asks for, so the judgement follows the stated standard.",
              "Values: the missing gradient, intercept and scatter are the values the sentence should have carried - naming them is the check."],
    claims=['CLM-9702-12-068'])

S['093-APP'] = dict(
    prompt="A learner finds a constant from a graph and writes it as k = 9.87, because, in the learner's words, the graph's axes had units already. Explain what is wrong with this conclusion.",
    answer="A constant stated without its unit is a number with no quantity attached: the axes' units were s² and m, and the gradient divided them into s² m⁻¹ - the constant inherits a unit from the axes, and it does not travel to the answer by itself. Because a constant found from a graph is stated with its unit worked out from the units of the axes, k here is 9.87 N m⁻¹ (once the equation's mass side is converted) - a stiffness, in newtons per metre, not a bare 9.87. In this case the omission is not shorthand; it is the difference between a value and a number, and the conclusion is the one place the difference is worth marks.",
    guidance=["Situation: this case is the unitless constant.",
              "Because: the conclusion fails because the unit is worked out from the axes' units, so the constant needs it stated - that is what makes it a quantity."],
    claims=['CLM-9702-12-069'])

# ---- OBJ-9702-12.3-09 test a relationship ----
S['094-CALC'] = dict(
    prompt="A constant is calculated twice from one experiment: k₁ = 2.51 N m⁻¹ and k₂ = 2.43 N m⁻¹. The estimated percentage uncertainty of the measurements is 3%. Calculate the percentage difference between the two values.",
    answer="""Percentage difference = (difference ÷ mean) × 100%
Difference = 2.51 − 2.43 = 0.08 N m⁻¹
Mean = (2.51 + 2.43) ÷ 2 = 4.94 ÷ 2 = 2.47 N m⁻¹
Percentage difference = (0.08 ÷ 2.47) × 100% = 0.0324 × 100% = 3.24%
The percentage difference is 3.2% to two significant figures - against the stated criterion of 3%, the difference lies just outside it, so the data do not support the suggested relationship at that criterion: the values are close, but "close" was defined first, and 3.2% is more than 3%.""",
    guidance=["Equation: percentage difference = (difference ÷ mean) × 100%, so the substitution runs the three steps.",
              "Answer: 0.08 ÷ 2.47 = 0.0324, so the final value is 3.2% against the 3% criterion.",
              "Units: a percentage carries none, so the judgement compares it with the stated criterion - the unit of the constant cancels in the division."],
    claims=['CLM-9702-12-070', 'CLM-9702-12-071'])

S['095-INTERP'] = dict(
    prompt="A learner tests whether a stone's mass density is the same throughout by calculating it from two halves of the data and gets 2.61 g cm⁻³ and 2.66 g cm⁻³, then writes that these are basically equal, so the relationship is supported. Determine what is missing from this judgement.",
    answer="Reading the claim: the two values differ by 2.66 − 2.61 = 0.05 g cm⁻³, which on a mean of 2.635 g cm⁻³ is 0.05 ÷ 2.635 = 0.0190, or 1.9% - a number, not an opinion. What is missing is the criterion, stated before the comparison: the estimated percentage uncertainty of the measurements (say 2%), against which the 1.9% difference is judged. Without the criterion stated first, the judgement cannot be made - the values might be close because the relationship holds, or because the measurements were too coarse to tell, and the criterion is the only thing that distinguishes them. The complete judgement names the values, the 1.9%, the criterion, and the verdict: supported, since 1.9% lies inside 2%.",
    guidance=["Reading: the two values are read, and the difference turned into a percentage.",
              "Means: the missing criterion means the judgement has no standard, so the test - stated first - is what the answer needed."],
    claims=['CLM-9702-12-070', 'CLM-9702-12-093'])

S['096-EVAL'] = dict(
    prompt="A learner writes that the two values of the constant are close, so the data support the relationship. Explain whether this judgement is complete, stating the criterion it needs.",
    answer="""The criterion stated first: a suggested relationship is tested by comparing the percentage difference between the values against a criterion declared before the comparison - usually the estimated percentage uncertainty of the measurements.
The comparison: the sentence never states the percentage difference (a number), never states the criterion (another number), and never says whether the difference lies inside it - the word close is an opinion where the test needs an inequality.
The judgement: incomplete, because the data may support the relationship or the measurements may simply be too uncertain to tell - the criterion is the only thing that separates those, and it is absent. The complete judgement names the values compared, the percentage difference, the criterion, and the verdict: for example, "2.51 and 2.43 N m⁻¹ differ by 3.2%; the estimated uncertainty is 3%; the difference lies outside the criterion, so the data do not support the relationship." Both verdicts earn the marks - and a stated criterion is what either verdict needs.""",
    guidance=["Criterion: percentage difference against the estimated percentage uncertainty, stated before comparing.",
              "Because: the judgement fails because no criterion was declared, so the word close cannot decide anything.",
              "Values: the percentage difference and the criterion are the two values the judgement must name - they are the test."],
    claims=['CLM-9702-12-070', 'CLM-9702-12-071', 'CLM-9702-12-093'])

S['097-APP'] = dict(
    prompt="A learner decides, after seeing that two calculated constants differ by 9%, that a criterion of 10% seems reasonable. Explain what is wrong with choosing the criterion at that moment.",
    answer="The criterion was chosen after the comparison was already visible: with the 9% difference in hand, picking 10% decides the answer before the test is run - the criterion is no longer testing the data, it is agreeing with them. Because the criterion is stated before the comparison, usually as the estimated percentage uncertainty of the measurements, the honest sequence is: estimate the uncertainty first (from the repeats, the resolutions and the powers in the calculation), state it, and only then compare the difference with it. A criterion chosen to fit the result is a number wearing the costume of a test, and the reader can see the seam every time.",
    guidance=["Situation: this case is the after-the-fact criterion.",
              "Because: the choice fails because the criterion must be stated before comparing, so the estimated uncertainty is what sets it - not the answer it is meant to judge."],
    claims=['CLM-9702-12-070', 'CLM-9702-12-093'])

S['128-MISCON'] = dict(
    prompt="A learner compares two calculated values of a constant - 2.51 and 2.43 - and writes that the data support the relationship because the values are close. Explain what is wrong with this judgement and state the test that makes it a real test.",
    answer="The error: saying the data support a relationship because two values are close, with no criterion - the word close is not a standard, and the same gap could look close with coarse measurements and far with fine ones. The correct idea: compare the percentage difference between the values (here 2.51 − 2.43 = 0.08, on a mean of 2.47, so 0.08 ÷ 2.47 = 0.0324, which is 3.2%) with a criterion stated in advance, such as the estimated percentage uncertainty of the measurements. The test that tells them apart is: what counts as close enough, and was it stated first? Only the stated criterion turns agreement into evidence.",
    guidance=["Error: the no-criterion agreement is the error; in fact the percentage difference is judged against a criterion declared first.",
              "Test: what counts as close enough, and was it stated before comparing - that is the check on any such judgement."],
    claims=['CLM-9702-12-093'], misconception='MC-9702-12-11')

# ---- OBJ-9702-12.3-10 predictions ----
S['098-CALC'] = dict(
    prompt="A graph of R against L is a straight line through readings from L = 0.100 m (R = 2.4 Ω) to L = 1.000 m (R = 12.0 Ω). Calculate the resistance predicted by the line at L = 0.550 m, inside the measured range.",
    answer="""The line is straight, so the prediction is a proportional read: R = R₀ + gradient × L.
Gradient = (12.0 − 2.4) ÷ (1.000 − 0.100) = 9.6 ÷ 0.900 = 10.667 Ω m⁻¹
The line's share at 0.550 m: 10.667 × 0.550 = 5.867 Ω, and R = 2.4 + 5.867 = 8.267 Ω
The predicted resistance at 0.550 m is 8.27 Ω to three significant figures - a value read from the trend line between the readings, so it carries the unit of the y-axis and the scatter of the points as its uncertainty.""",
    guidance=["Equation: the straight-line form R = R₀ + mL, so the substitution uses the line's own readings.",
              "Answer: 2.4 + 10.667 × 0.550 = 8.267, so the final prediction is 8.27 Ω.",
              "Units: ohms from the y-axis, three significant figures matching the readings the line was drawn from."],
    claims=['CLM-9702-12-072'])

S['099-INTERP'] = dict(
    prompt="A learner uses a straight trend line from an experiment that ran from 20 °C to 60 °C to predict the value at 200 °C. Determine what this prediction rests on, and what the trend line does and does not promise there.",
    answer="Reading the request: 200 °C lies far beyond the measured range of 20 °C to 60 °C - more than three times the span of the whole experiment - so the prediction rests on the assumption that the trend continues, which a straight line within the measured range does not guarantee. What the line promises: between the readings, and a short way past them, the trend is supported by the data on both sides. What it does not promise: that the physics is unchanged beyond the last reading - a wire warms and its resistivity behaviour may change, a material may melt, a spring may exceed its elastic range - and nothing in the 20-60 °C data speaks to any of it. So the prediction at 200 °C is an extrapolation wearing the name of a reading, and the honest statement is: read from the line, beyond the measured range, assuming the trend holds - and the assumption is the whole of the answer.",
    guidance=["Reading: the requested value is read against the measured span.",
              "Means: the far extrapolation means an assumption the data cannot check - the trend's guarantee is what the reading rests on."],
    claims=['CLM-9702-12-072', 'CLM-9702-12-073'])

S['100-EVAL'] = dict(
    prompt="A learner predicts a value a short way beyond the last reading, at 1.100 m on a line whose readings ran from 0.100 m to 1.000 m. Explain whether this prediction is justified, stating the criterion.",
    answer="""The criterion stated first: a prediction from a graph is a value read from the trend line, between the readings or a short way beyond them - the trust of the prediction is the scatter of the points, and the span rule is what bounds it.
The comparison: 1.100 m is 10% beyond the last reading, on a line drawn from a 0.900 m span of well-populated readings - a short extension of a well-supported trend.
The judgement: justified, because the prediction is a small extension of a line with readings on both sides of nearly all of it, and the criterion (a short way beyond) is satisfied - the assumption that the trend continues is a mild one over a small gap. The prediction still carries its stated basis - read from the line, a little beyond the last reading, so the trend's continuation is assumed - and that statement is what separates a justified prediction from a borrowed certainty.""",
    guidance=["Criterion: between the readings or a short way beyond, with the scatter as the trust.",
              "Because: the prediction is justified because it extends a well-populated line a short way, so the reasoning follows the stated span rule.",
              "Values: 10% beyond on a 0.900 m span - the numbers are what short means here, and they are stated."],
    claims=['CLM-9702-12-072', 'CLM-9702-12-073'])

S['101-APP'] = dict(
    prompt="A learner reads a predicted value off the trend line between two readings and reports it as 4.6, read off the graph, so it is exact. Explain what is wrong with the report.",
    answer="A value read from a trend line is not exact: the line was drawn through points that scatter, and any reading taken from it inherits that scatter - the prediction is worth about what the readings were worth, not more. Because a prediction from a graph is a value read from the trend line with the unit of its axis and the scatter of the points as its uncertainty, this case needed the report to say what the reading rests on: 4.6 with its unit, and the scatter (a percent or two) as its doubt. The word exact claims a precision no graph has ever had, and the honest prediction is the more useful one - a reader who knows its trust knows what to do with it.",
    guidance=["Situation: this case is the exact-by-graph report.",
              "Because: the report fails because the line's scatter is the prediction's uncertainty, so the read-off value needs its doubt stated - that is what the graph can honestly give."],
    claims=['CLM-9702-12-072'])

# ---- OBJ-9702-12.3-11 limitations ----
S['102-CALC'] = dict(
    prompt="In a resistivity experiment, the length carries 0.1% uncertainty and the diameter carries 2% uncertainty. Calculate which measurement dominates the uncertainty in the resistivity, remembering that the diameter enters the calculation squared.",
    answer="""The diameter enters through the area A = πd²/4, so its percentage uncertainty counts twice:
Area's share = 2 × 2% = 4%
Length's share = 0.1%
Total into the resistivity = 4% + 0.1% = 4.1%
The diameter dominates: 4% of the 4.1% total is its doubled share, so the measurement that looked twice as uncertain as the length is in fact forty times more damaging once the squaring is counted. The limitation worth stating first is whatever makes the diameter unreliable - the wire's non-uniformity, the micrometer's zero error - because that is the uncertainty the improvement budget should go to.""",
    guidance=["Equation: the doubled share for a squared quantity, so the substitution is 2 × 2% before the addition.",
              "Answer: 4% against 0.1%, so the final total is 4.1% and the diameter is the dominant measurement.",
              "Units: percentages throughout, so the significant figures are the shares themselves - the ranking is the answer."],
    claims=['CLM-9702-12-075', 'CLM-9702-12-076'])

S['103-INTERP'] = dict(
    prompt="An experiment reports these limitations: human error; the instruments were old; the room was hot; parallax. Determine what each of these statements fails to do, and what a real limitation statement would add.",
    answer="Reading each against the standard - a limitation names the measurement it affects, what makes that measurement unreliable, and its effect - every one of them fails at the naming. The human error phrase names no measurement and no cause: nothing can be improved. The old-instruments phrase names no measurement either - age is not a mechanism, a zero error or a worn scale is. The hot-room phrase names a condition but not what it did to which reading. The parallax word names a cause but not which scale, which reading, and which way it shifted. A real statement repairs each in one move: the timing, because the pointer is judged by eye against a hunting scale, scattering the start and stop by ± 0.2 s; the diameter, because the micrometer's zero error was 0.02 mm and shifts every reading. That is what the four answers to the test - which measurement, and what exactly makes it unreliable - actually sound like.",
    guidance=["Reading: each stated limitation is read against the naming standard.",
              "Means: each fails to mean anything improvable - the measurement, the cause and the effect are what a real statement carries."],
    claims=['CLM-9702-12-074', 'CLM-9702-12-094'])

S['104-EVAL'] = dict(
    prompt="A learner lists as limitations: the ruler was hard to read; the masses might be wrong; wind; eyesight. Explain whether these are usable limitations, stating the criterion each must meet.",
    answer="""The criterion stated first: a limitation names the measurement it affects, what makes that measurement unreliable, and its effect on the result - the three parts are what make it improvable.
The comparison: The hard-to-read ruler gestures at a reading but names no cause (parallax? a worn scale? the eye's angle?) and no effect; the wrong masses name no measurement that suffered, and might is not a mechanism; wind names no measurement at all; eyesight is the human error phrase wearing a different coat.
The judgement: not usable, because each fails the criterion's first part - no named measurement, no named cause, no stated effect - and a limitation that cannot say what it affects cannot be improved by anything. The repair is the same for each: name the reading (the extension, judged by eye against a millimetre rule at arm's length), the cause (the eye's angle shifts the apparent mark, a parallax error of up to half a millimetre), and the effect (each length carries it, so the gradient carries it too). Four of those are the four marks; four gestures are not.""",
    guidance=["Criterion: measurement, cause, effect - the three parts stated before the judgement.",
              "Because: each statement fails because it names nothing the criterion asks for, so the verdict follows the stated standard.",
              "Values: the missing readings and causes are what the values should have been - naming them is the check."],
    claims=['CLM-9702-12-074', 'CLM-9702-12-094'])

S['105-APP'] = dict(
    prompt="A learner writes that a limitation was that the measurements had errors in them. Explain what is wrong with this statement as an evaluation of the experiment.",
    answer="The statement names nothing: no measurement (the length? the period? the diameter?), no cause of the unreliability (parallax? scatter? a zero error?), and no effect on the result (which constant inherits the doubt, and how much). Because a limitation is stated by naming the measurement it affects, what makes that measurement unreliable and its effect - not by a general phrase such as human error - the sentence is the empty form of a limitation: it would fit any experiment ever performed, which is the proof that it says nothing about this one. The repair starts with the ranking - the measurement with the largest percentage uncertainty - and names the cause of that measurement's scatter, which turns the phrase into a mark.",
    guidance=["Situation: this case is the errors-were-present statement.",
              "Because: the statement fails because it names no measurement, cause or effect, so the three-part standard is what it needed."],
    claims=['CLM-9702-12-074', 'CLM-9702-12-094'])

S['126-MISCON'] = dict(
    prompt="Asked for limitations of a falling-paper experiment, a learner writes human error, and parallax. Explain what is wrong with these two limitations and state the test that catches them.",
    answer="The error: naming vague limitations - the human error phrase, the parallax word - without saying which measurement is affected and why; both phrases fit every experiment ever run, which is the proof that they diagnose nothing. The correct idea: name the measurement, what makes it hard, and its effect - the time of fall, because the paper flutters and the watch is started and stopped by eye, scattering each timing by a few tenths of a second and so the calculated acceleration with it. The test that tells them apart is: which measurement, and what exactly makes it unreliable? An answer that passes names a reading and a mechanism; the human error phrase passes nothing.",
    guidance=["Error: the vague phrases are the error; in fact a limitation names the measurement, the cause and the effect.",
              "Test: which measurement, and what exactly makes it unreliable - that is the check on every limitation."],
    claims=['CLM-9702-12-094'], misconception='MC-9702-12-09')

# ---- OBJ-9702-12.3-12 most significant uncertainty ----
S['106-CALC'] = dict(
    prompt="Three measurements feed a result: a length of 0.450 m read to the nearest 1 mm; a mass of 0.200 kg on a balance reading to 0.001 kg, with repeats spread over 0.004 kg; and a time of 12.4 s from a stop-watch with repeats spread over 0.4 s. Calculate the percentage uncertainty of each and state which is the most significant source.",
    answer="""Length: ± 0.5 mm on 0.450 m = 0.0005 ÷ 0.450 = 0.00111, which is 0.11%
Mass: half the range = 0.004 ÷ 2 = 0.002 kg, on 0.200 kg: 0.002 ÷ 0.200 = 0.01, which is 1.0%
Time: half the range = 0.4 ÷ 2 = 0.2 s, on 12.4 s: 0.2 ÷ 12.4 = 0.0161, which is 1.6%
The most significant source is the time, at 1.6% - the ranking is time (1.6%), mass (1.0%), length (0.11%) - and the improvement budget goes to the timing: more oscillations per reading, or a light gate, because, provided the timing is where the largest share lies, halving that share is the change the final result feels most.""",
    guidance=["Equation: half the resolution or half the range, then divided by the value, so each measurement's share is the substitution.",
              "Answer: 0.11%, 1.0% and 1.6%, so the final ranking names the time as the most significant.",
              "Units: percentages are the comparable form, so the ranking - not the absolute doubts - is what the answer states."],
    claims=['CLM-9702-12-076', 'CLM-9702-12-077'])

S['107-INTERP'] = dict(
    prompt="A learner says the most significant source of uncertainty in a resistivity experiment is the length, because the rule is a metre long and easy to get wrong. Determine what the comparison of percentage uncertainties actually shows, using the readings: length 0.800 m ± 0.5 mm; diameter 0.30 mm ± 0.01 mm.",
    answer="Reading the percentages: the length's share is 0.0005 ÷ 0.800 = 0.000625, which is 0.063%; the diameter's is 0.01 ÷ 0.30 = 0.0333, which is 3.3% - and the diameter enters the resistivity squared, so its share counts twice: 6.6%. The comparison shows the learner has it backwards: the diameter, with its tiny absolute doubt of 0.01 mm, is over a hundred times more damaging than the length's half-millimetre, because the share, not the absolute doubt, is what the result feels. The length being easy to get wrong is a feeling; the ranking is arithmetic, and the most significant source is the measurement with the largest percentage uncertainty - here, the diameter.",
    guidance=["Reading: the two shares are read from the readings, and the squaring is counted.",
              "Means: the comparison means 0.063% against 6.6% - the percentage is what significance runs on, and the learner's ranking is reversed by it."],
    claims=['CLM-9702-12-076', 'CLM-9702-12-077'])

S['108-EVAL'] = dict(
    prompt="A learner states that the biggest source of uncertainty was the timing, obviously, because stop-watches are bad. Explain whether the reasoning holds, stating the criterion the claim must meet.",
    answer="""The criterion stated first: the most significant source of uncertainty is the measurement with the largest percentage uncertainty - established by estimating each measurement's share (half the resolution, half the range of repeats, doubled for squared quantities) and ranking them.
The comparison: the claim rests on an opinion about a class of instrument, not on any share of anything - no estimate for the timing, none for the other measurements, and so no ranking at all. A stop-watch that is bad on a 20-oscillation total may still carry a smaller share than a single squinted diameter.
The judgement: the reasoning does not hold, because the criterion asks for numbers and the claim offers a stereotype - the timing may well be the largest share, but only the estimates can say so, and they are absent. The repair is one line per measurement: the shares, the ranking, and then the verdict - which is the whole difference between an evaluation and an opinion.""",
    guidance=["Criterion: the largest percentage uncertainty, from estimated shares - stated before the judgement.",
              "Because: the claim fails because it offers no shares to rank, so the verdict cannot follow the stated criterion.",
              "Values: the missing estimates for each measurement are the values the claim needed - the ranking is built from them."],
    claims=['CLM-9702-12-076'])

S['109-APP'] = dict(
    prompt="A learner compares uncertainties by their absolute values and concludes the metre rule (± 0.5 mm) matters more than the thermometer (± 0.5 °C), because millimetres are smaller than degrees. Explain what is wrong with this comparison.",
    answer="Absolute uncertainties of different quantities cannot be compared at all: a millimetre and a degree are different units, and the word smaller is not a relation between them. Because the most significant source is found by comparing percentage uncertainties - each doubt divided by its own value - the comparison needed the shares: ± 0.5 mm on 800 mm is 0.063%, while ± 0.5 °C on a difference of 6 °C is 8.3%, and the thermometer dominates by more than a hundredfold. In this case the learner's conclusion is exactly reversed, and the reason is structural: comparing absolute doubts across units is not a rough version of the real comparison, it is a different operation with no meaning.",
    guidance=["Situation: this case is the cross-unit absolute comparison.",
              "Because: the comparison fails because shares, not absolute doubts, are what significance runs on, so the percentage uncertainty is the only comparable form."],
    claims=['CLM-9702-12-076', 'CLM-9702-12-077'])

# ---- OBJ-9702-12.3-13 suggest modifications ----
S['110-CALC'] = dict(
    prompt="A limitation is stated: the time of fall of a paper cone is judged by eye, and the start and stop of the watch scatter by about ± 0.2 s each, on a fall of 1.4 s. Calculate the percentage uncertainty this gives, and the percentage uncertainty if the fall were filmed against a timer in frame.",
    answer="""By eye: the start and stop each bring ± 0.2 s, so the time carries 0.2 + 0.2 = 0.4 s of doubt on 1.4 s: 0.4 ÷ 1.4 = 0.286, which is 29%.
Filmed against a timer: the frame rate resolves the start and stop to about ± 0.01 s each, so 0.01 + 0.01 = 0.02 s on 1.4 s: 0.02 ÷ 1.4 = 0.0143, which is 1.4%.
The improvement drops the timing's share from 29% to 1.4% - a twentyfold reduction on the measurement that dominated the experiment, which is what "an improvement answers a named limitation" is worth when the answer is worked out.""",
    guidance=["Equation: the two reading doubts added, then divided by the value, so each route's share is the substitution.",
              "Answer: 0.4 ÷ 1.4 = 0.286 and 0.02 ÷ 1.4 = 0.0143, so the final shares are 29% and 1.4%.",
              "Units: percentages make the two routes comparable, so the significant figures are the shares - the improvement is the answer."],
    claims=['CLM-9702-12-078'])

S['111-INTERP'] = dict(
    prompt="A limitation is stated: the wire's diameter varies along its length, so the single area used in the calculation carries the wire's non-uniformity. Determine what an improvement must do to answer this limitation, and give one that does.",
    answer="Reading the limitation: the measurement that suffers is the diameter (and so the area), the cause is the wire's non-uniformity, and the effect is an area that misstates every length of that wire. An improvement must answer that named limitation by reducing the uncertainty of that measurement: taking the diameter at several places along the wire and in two perpendicular directions at each place, and averaging - so the area used is the wire's mean cross-section, not one reading's luck. The improvement is tied to the limitation it fixes, which is the test: which limitation does it fix? This one fixes the non-uniformity; a data-logger would fix nothing here, because the timing was never the measurement that suffered.",
    guidance=["Reading: the limitation is read for its measurement, cause and effect.",
              "Means: the improvement means the diameter's uncertainty shrinks - the tie to the named limitation is what makes it an improvement."],
    claims=['CLM-9702-12-078', 'CLM-9702-12-095'])

S['112-EVAL'] = dict(
    prompt="A learner, asked for an improvement on a timing limitation, writes the two words: use better equipment. Explain whether this is an improvement answer, stating the criterion it must meet.",
    answer="""The criterion stated first: a modification improves the experiment where it reduces the uncertainty of the named measurement it is aimed at, and it is described specifically enough to be carried out - the equipment, where it is placed, what it replaces.
The comparison: the phrase names no equipment, no placement, no replacement - the phrase could mean a new stop-watch, a light gate, a data-logger, or nothing, and no reader could set any of them up from it.
The judgement: not an improvement answer, because the criterion asks for a specific method aimed at a stated limitation and the phrase offers neither. The repair: the timing of the oscillations, because the start and stop are judged by eye, scattering ± 0.2 s each - replace the watch with a light gate at the rest position, connected to a timer, so the crossings are sensed rather than judged and the timing's share falls from about 25% to under 1%. That sentence could be built from its words, and that is the standard.""",
    guidance=["Criterion: specific, aimed at the named measurement, described enough to be built.",
              "Because: the phrase fails because it names nothing the criterion asks for, so the verdict follows the standard.",
              "Values: the timing's scatter and the shares are the values that make the improvement measurable - they are the evidence."],
    claims=['CLM-9702-12-078', 'CLM-9702-12-080', 'CLM-9702-12-095'])

S['113-APP'] = dict(
    prompt="A limitation is stated: the temperature of a wire rises during the experiment, so the later resistance readings carry a temperature the earlier ones do not. A learner suggests, as the improvement, measuring the temperature. Explain what is wrong with this suggestion.",
    answer="Measuring the temperature names what happens but improves nothing: the readings would still carry the drift, now with a number beside it. Because a modification improves the accuracy of the experiment where it reduces the uncertainty of the measurement it is aimed at, the improvement for this limitation must attack the drift itself - switch the circuit off between readings so the wire cools, take the readings quickly in one run, or use a lower current so the heating is smaller. The learner's suggestion observes the illness and calls the observation the cure; the criterion is which limitation the change fixes, and this one fixes none.",
    guidance=["Situation: this case is the observe-don't-improve suggestion.",
              "Because: the suggestion fails because it reduces no uncertainty, so the drift itself - not its measurement - is what the change must attack."],
    claims=['CLM-9702-12-078', 'CLM-9702-12-095'])

S['127-MISCON'] = dict(
    prompt="Asked for improvements on a stopwatch-timing experiment, a learner writes use a computer, and do more repeats. Explain what is wrong with these suggestions and state the test that catches them.",
    answer="The error: suggesting improvements that are not tied to a stated limitation - the computer suggestion names no measurement, no placement, no replacement, and no fault it fixes; the repeats suggestion answers scatter, but if the stated limitation was the reaction time of the eye at start and stop, repeats average the same fault and reduce nothing. The correct idea: each improvement answers one named limitation with a specific method - the start and stop judged by eye (± 0.2 s each) are answered by a light gate at the rest position sensing the crossings, and the description names the apparatus, its position and what it replaces. The test that tells them apart is: which limitation does the improvement fix? An improvement that cannot say is a purchase, not a repair.",
    guidance=["Error: the untethered suggestions are the error; in fact each improvement names the limitation it answers with a specific method.",
              "Test: which limitation does the improvement fix - that is the check on every suggested improvement."],
    claims=['CLM-9702-12-095'], misconception='MC-9702-12-10')

# ---- OBJ-9702-12.3-14 describe modifications clearly ----
S['114-CALC'] = dict(
    prompt="A limitation is stated: the extension of a spring is measured as the difference of two rule readings, so it carries ± 1.0 mm. Calculate the percentage uncertainty this gives on an extension of 20 mm, and on the improvement of clamping a vernier scale to the hanger (resolution 0.1 mm, one reading of the extension).",
    answer="""Two rule readings: 0.5 + 0.5 = 1.0 mm on 20 mm: 1.0 ÷ 20 = 0.05, which is 5.0%
Vernier, one reading: 0.1 ÷ 2 = 0.05 mm on 20 mm: 0.05 ÷ 20 = 0.0025, which is 0.25%
The vernier cuts the extension's share from 5.0% to 0.25% - a twentyfold reduction, achieved by measuring the extension directly instead of as a difference of two readings. The numbers are what make the improvement worth describing: the gain is stated, not implied by the word "vernier".""",
    guidance=["Equation: the difference's two doubts added, the single reading's half-resolution taken, then each divided by the value.",
              "Answer: 1.0 ÷ 20 = 0.05 and 0.05 ÷ 20 = 0.0025, so the final shares are 5.0% and 0.25%.",
              "Units: percentages compare the two methods, so the significant figures are the shares - the gain is the answer."],
    claims=['CLM-9702-12-078', 'CLM-9702-12-080'])

S['115-INTERP'] = dict(
    prompt="An improvement is described as follows: replace the stop-watch with a light gate, positioned where the strip crosses its rest position, connected to a timer that starts when the strip first breaks the beam and stops when it breaks it again after one complete oscillation; the timer's display replaces the watch's. Determine whether this description meets the standard, naming the parts that make it so.",
    answer="Reading the description against the standard - the equipment, where it is placed, what it replaces, and what is done with it: the equipment is a light gate and a timer; the position is at the strip's rest position, where the crossings are fastest and sharpest; the replacement is the stop-watch, named; and what is done is stated - the timer starts and stops on the beam's breaking, one complete oscillation apart. The description also names the measurement it improves, the timing, by removing the eye's ± 0.2 s judgement at start and stop. A reader could set this up without asking a question, which is the whole test of a carried-out-able description - every part the criterion names is present in the sentence.",
    guidance=["Reading: the description is read part by part against the standard.",
              "Means: the naming of equipment, position, replacement and use means the improvement is buildable - that is what the standard asks."],
    claims=['CLM-9702-12-080', 'CLM-9702-12-081'])

S['116-EVAL'] = dict(
    prompt="A learner describes an improvement by saying a motion sensor would be better for the timing. Explain whether this description is clear enough to be carried out, stating the criterion.",
    answer="""The criterion stated first: a modification is described clearly enough to be carried out - the equipment, where it is placed, what it replaces, and what is done with it.
The comparison: the sentence names a device (a motion sensor) and a benefit (better for the timing), but no position (where does the sensor sit? what does it watch?), no replacement (does it replace the watch, or the whole method?), and no operation (what does it trigger, and on what signal?).
The judgement: not clear enough, because a reader could not set it up from the sentence - the criterion asks for the four parts and the sentence carries one and a half. The repair completes them: a motion sensor below the strip, facing upward, connected to a timer that starts when the strip first passes the rest position and stops after a counted twenty crossings, replacing the stop-watch and the eye. Same sensor, now a buildable instruction - and the description is the whole difference.""",
    guidance=["Criterion: equipment, position, replacement, operation - stated before the judgement.",
              "Because: the description fails because it names no position or operation, so the verdict follows the stated standard.",
              "Values: the missing parts are what the values should have been - naming them completes the instruction."],
    claims=['CLM-9702-12-080', 'CLM-9702-12-081'])

S['117-APP'] = dict(
    prompt="A learner describes an improvement as putting a mirror somewhere to help with the parallax. Explain what is missing from this description, and write the version that could be carried out.",
    answer="The description names equipment (a mirror) and a purpose (parallax) but no position - somewhere is not a place on an apparatus - and no operation, so a reader cannot build it. Because a modification names the apparatus, its position in the arrangement and the measurement it improves, the carried-out version is: stand a small mirror flat on the bench behind the scale, beside the pointer's rest position, and move the eye until the pointer hides its own reflection before each reading - the eye is then directly above the pointer, and the parallax error in the length reading is removed. Same mirror, same purpose, but the sentence now tells the reader where it goes and what is done with it - or a labelled diagram of the bench, rule, pointer and mirror would do the same - which is the difference between a suggestion and an instruction.",
    guidance=["Situation: this case is the somewhere-mirror description.",
              "Because: the description fails because position and operation are missing, so the named apparatus, its place and its use are what the sentence needed."],
    claims=['CLM-9702-12-080', 'CLM-9702-12-081'])

if __name__ == '__main__':
    print(len(S), 'slots part 3')
