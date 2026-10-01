#!/usr/bin/env python3
"""The four practical tasks for topic 12 (P01-P04)."""

T = {}

# ---------- P01: Paper 3 Question 1 style, mechanical (falling mass / energy) ----------
T['P01'] = dict(
    objective_ids=['OBJ-9702-12.2-11', 'OBJ-9702-12.3-03', 'OBJ-9702-12.3-04', 'OBJ-9702-12.3-08'],
    claims=['CLM-9702-12-040', 'CLM-9702-12-058', 'CLM-9702-12-060', 'CLM-9702-12-061', 'CLM-9702-12-068'],
    command_word='Plot',
    prompt="""A learner investigates a loaded string slider: a mass on a string over a pulley drags a trolley along a bench, and the time t for the trolley to travel a fixed distance is measured as the mass m is changed. The string is kept taut and the pulley spins freely. The time is measured with a stop-watch for a 0.500 m run of the trolley, from rest, three times at each mass; the table below shows our readings.

| m / g | t1 / s | t2 / s | t3 / s | mean t / s | t² / s² |
|---|---|---|---|---|---|
| 50 | 2.4 | 2.6 | 2.5 | 2.5 | 6.25 |
| 70 | 2.1 | 2.0 | 2.1 | 2.1 | 4.41 |
| 90 | 1.9 | 1.9 | 1.8 | 1.9 | 3.61 |
| 110 | 1.7 | 1.8 | 1.7 | 1.7 | 2.89 |
| 130 | 1.6 | 1.5 | 1.6 | 1.6 | 2.56 |
| 150 | 1.5 | 1.4 | 1.5 | 1.5 | 2.25 |

It is suggested that t² = k/m + c, where k and c are constants.
(a) Describe how each timing would be taken and repeated at the bench. [2]
(b) Justify the number of significant figures in the t² column of the table. [1]
(c) Plot a graph of t² / s² on the y-axis against (1/m) / g⁻¹ on the x-axis on your own graph paper, choosing scales so the points cover at least half of the grid in both directions, and draw the line of best fit. [4]
(d) Determine the gradient and the y-intercept of your line. [3]
(e) Hence state the values of k and c, with their units. [2]
(f) The trolley loses energy to friction as it runs. Explain what the intercept c represents in this experiment. [2]""",
    answer="""(a) Each timing is taken with the trolley released from rest at the start mark and the watch started as the trolley's front edge crosses it, stopped as it crosses the 0.500 m mark, the same two marks every time; each timing is repeated three times at the same mass, the repeats recorded separately, and the mean of the three used - the repeats are taken back to back so the bench, the string and the pulley stay in the same condition.
(b) The raw times are recorded to 0.1 s (two significant figures), so the calculated t² values are given to three significant figures, matching the raw data - 2.5 s squared is 6.25 s², and the column carries three figures because the raw times carry two.
(c) The x-axis runs 1/m from 1 ÷ 150 = 0.00667 g⁻¹ to 1 ÷ 50 = 0.020 g⁻¹, and the y-axis runs t² from 2.25 s² to 6.25 s². Scales that fill the grid: the x-axis from 0.006 to 0.021 g⁻¹ at 0.001 per 2 cm square (a false origin, since the smallest 1/m value lies away from zero and a zero start would leave the points in a third of the width), and the y-axis from 2.0 to 6.5 s² at 0.5 per 2 cm square. The six points lie close to one straight line rising with 1/m, balanced either side.
(d) Two points on the line, far apart: (0.00750 g⁻¹, 2.47 s²) and (0.0190 g⁻¹, 5.96 s²). Δy = 5.96 − 2.47 = 3.49 s², and Δx = 0.0190 − 0.00750 = 0.0115 g⁻¹, so the gradient is 3.49 ÷ 0.0115 = 303.5 = 304 s² g. The x-axis starts at 0.006 g⁻¹, not zero, so the intercept is calculated, not read: c = y − mx, and 304 × 0.0190 = 5.776, so c = 5.96 − 5.776 = 0.184 = 0.18 s². (Values read off a hand-drawn line vary by a few percent; the large triangle is the mark.)
(e) k = 304 s² g = 3.04 × 10⁵ s² kg (with 1000 g = 1 kg), and c = 0.18 s² - both to three significant figures, with their units.
(f) If the trolley ran frictionless and the hanging mass had nothing but its own motion to accelerate, the run would satisfy t² exactly proportional to 1/m and c would be zero. The measured intercept is small and positive, and that is what the model misses: the hanging mass must also accelerate the trolley's own fixed mass, and friction takes a further fixed share of the pull, so a constant part of t² does not scale with 1/m - it is the delay the fixed masses and friction impose, and the graph has measured it as the intercept.""",
    guidance=["Table and headings: the calculated t² column carries quantity / unit and its significant figures are justified in (b) against the raw times - the column is the first thing checked.",
              "Graph and uncertainty: the scales, the plotted points and the line earn the marks in (c); the gradient from a large triangle on the line and the intercept by calculation (the axis is a false origin) in (d) - the uncertainties of the read-off are what the far-apart points control.",
              "Limitation, criterion and conclusion: the intercept's meaning in (f) is the conclusion - the friction term is the constant the graph found, and k and c with their units in (e) are the constants the equation promised."],
)

# ---------- P02: Paper 3 Question 2 style, mechanical (spring stiffness) ----------
T['P02'] = dict(
    objective_ids=['OBJ-9702-12.3-06', 'OBJ-9702-12.3-09', 'OBJ-9702-12.3-11', 'OBJ-9702-12.3-13'],
    claims=['CLM-9702-12-064', 'CLM-9702-12-066', 'CLM-9702-12-070', 'CLM-9702-12-074', 'CLM-9702-12-095'],
    command_word='Estimate',
    prompt="""A learner measures the stiffness of a spring by hanging masses from it and timing the vertical oscillations - but the method is inaccurate: the mass is hung by hand, the oscillations are started by a sideways push that varies, and the ruler is read at an angle.

The period T is found by timing 20 complete oscillations, twice, and dividing by 20. The equation suggested is T = 2π√(m/k), where k is the stiffness, so k = 4π²m/T². Here are our readings.

| m / g | t(20 osc) / s | T / s | k / N m⁻¹ |
|---|---|---|---|
| 100 | 17.4, 17.6 | 0.875 | 5.16 |
| 200 | 24.1, 24.3 | 1.21 | 5.39 |

(a) Estimate the absolute uncertainty in the period at m = 100 g, and hence the percentage uncertainty in T there. [2]
(b) Verify the value of k in each row, showing the working from the readings (k = 4π²m/T², with m in kg). [2]
(c) It is suggested that k is a constant of the spring. State a criterion first, then determine whether the two values of k support the suggestion. [3]
(d) Give four limitations of this experiment, each naming the measurement it affects and how. [4]
(e) Give four improvements, each tied to the limitation it answers. [4]
(f) Explain why the sideways push is a bigger threat to the timings than the hand-hung mass. [2]""",
    answer="""(a) The two timings at 100 g are 17.4 s and 17.6 s: the range is 17.6 − 17.4 = 0.2 s, so the absolute uncertainty in the 20-oscillation total is 0.1 s, and in the period it is 0.1 ÷ 20 = 0.005 s. The percentage uncertainty in T is 0.005 ÷ 0.875 = 0.00571, which is 0.57%.
(b) Row 1: k = 4π²m ÷ T² = 4 × 9.8696 × 0.100 ÷ (0.875 × 0.875) = 3.9478 ÷ 0.765625 = 5.157 N m⁻¹, which is 5.16 N m⁻¹ to three significant figures - the table's value checks. Row 2: k = 4 × 9.8696 × 0.200 ÷ (1.21 × 1.21) = 7.8957 ÷ 1.4641 = 5.393 N m⁻¹, which is 5.39 N m⁻¹ - the table's value checks. (T enters squared, so its 0.57% share counts twice in k.)
(c) Criterion stated first: the percentage uncertainty in k is about twice T's share (0.57% doubled to 1.1%, plus the mass's small share), so a criterion of about 2% is what these measurements can resolve; the two values of k support the constant-k suggestion only if their percentage difference lies inside it. The values are 5.16 and 5.39 N m⁻¹: the difference is 5.39 − 5.16 = 0.23 N m⁻¹, on a mean of 5.275, which is 0.23 ÷ 5.275 = 0.0436, or 4.4%. The difference lies outside the criterion, so the data do not support the suggestion: the spring's effective stiffness appears larger at the greater mass, by more than the measurement uncertainties allow, so either the spring is not behaving as the equation assumes or the timings at 200 g carry an unaccounted error.
(d) Four limitations, each naming its measurement: (1) the period, because the oscillations are started by a sideways push of varying size, so the mass swings as well as bounces and the crossings of the marker are irregular, scattering each timing; (2) the period again, because the watch is started and stopped by eye on a fast-moving mass, giving the ± 0.2 s of reaction time to a 17 s total; (3) the mass, because it is hung by hand, so the stated 100 g may include a nudged hanger or a detached slug, shifting the mass actually oscillating; (4) the ruler reading of any length, because the rule is read at an angle, so the parallax error shifts the apparent mark by up to half a millimetre each way.
(e) Four improvements, one per limitation: (1) start the oscillations by pulling the mass straight down a measured distance with a card under it, then releasing - the motion is then vertical only, and the start is the same every time; (2) time more oscillations per reading - 40 instead of 20 - or use a light gate at the rest position sensing the crossings, so the eye's reaction time is removed or halved; (3) hang the masses with the hanger already on the spring, adding slugs one at a time with tweezers or clean fingers, and check the total against a balance; (4) read the rule with the eye level with the mark, using a pointer on the hanger against the rule's scale, or a mirror behind the scale to square the sight line.
(f) The sideways push feeds the timing directly and differently each time: a push that varies changes the amplitude and adds a sideways swing, so the 20 crossings the watch is started and stopped on are not the same motion from run to run, and the two k values disagree. The hand-hung mass shifts the mass by at most a few grams - under 3% of 100 g and under 2% of 200 g - while the varying push changes the timing differently at the two masses, which is exactly the pattern the failed criterion shows.""",
    guidance=["Uncertainties: the range halved for the absolute uncertainty, then divided by the value for the percentage - the estimates in (a) are what the criterion in (c) rests on.",
              "Table and verification: the check of the printed k against its own readings in (b) is the analysis mark - the arithmetic is re-run, not trusted.",
              "Criterion and conclusion: the criterion is stated before the comparison in (c), and the four limitations in (d) and four improvements in (e) pair one-to-one, each naming the measurement it affects - the pairing is the standard the whole question sets."],
)

# ---------- P03: Paper 3 Question 1 style, electrical (wire resistance) ----------
T['P03'] = dict(
    objective_ids=['OBJ-9702-12.2-05', 'OBJ-9702-12.3-03', 'OBJ-9702-12.3-01', 'OBJ-9702-12.3-08'],
    claims=['CLM-9702-12-028', 'CLM-9702-12-058', 'CLM-9702-12-055', 'CLM-9702-12-069'],
    command_word='Plot',
    prompt="""A learner measures the resistance of a coil of fine wire at different lengths. The wire is taped along a metre board, connections are made at six points, and the resistance between each point and one fixed end is measured with an ohmmeter. The wire's diameter is measured with a micrometer at three places: 0.280 mm, 0.284 mm, 0.282 mm. Here are our readings.

| L / m | R / Ω | L / m | R / Ω |
|---|---|---|---|
| 0.200 | 4.1 | 0.700 | 9.4 |
| 0.300 | 5.3 | 0.800 | 10.5 |
| 0.400 | 6.5 | 0.900 | 11.7 |
| 0.500 | 7.6 | | |
| 0.600 | 8.5 | | |

It is suggested that R = (ρ/A)L + r, where ρ is the resistivity of the wire, A its cross-section area and r the resistance of the leads.
(a) Describe how the micrometer readings of the diameter would be taken, and calculate the mean diameter and the area A in m². [3]
(b) Draw up the table with a column for the calculated quantity needed for the graph, with quantity / unit headings. [2]
(c) Plot a graph of R / Ω on the y-axis against L / m on the x-axis, choosing scales so the points cover at least half of the grid in both directions, and draw the line of best fit. [4]
(d) Determine the gradient and the y-intercept of your line. [4]
(e) Hence calculate ρ, the resistivity, in Ω m, and state r with its unit. [4]
(f) The x-axis you chose starts at zero in this experiment. Explain why the intercept can be read straight off the graph here, and why that would not be so if the shortest length available had been 0.500 m. [3]""",
    answer="""(a) The diameter is measured with the micrometer's ratchet closing the jaws, at three places along the wire and in two perpendicular directions at each place, the zero error checked first with the jaws shut and subtracted from every reading. Mean d = (0.280 + 0.284 + 0.282) ÷ 3 = 0.846 ÷ 3 = 0.282 mm - the mean of the repeats, which works because the readings scatter randomly about the wire's true diameter. The area: A = πd²/4, and d² = 0.282 × 0.282 = 0.079524 mm², so A = 3.14159 × 0.079524 = 0.249860 mm², and 0.249860 ÷ 4 = 0.0624650 mm², and 1 mm² = 10⁻⁶ m², so A = 6.25 × 10⁻⁸ m² (to three significant figures).
(b) The table carries columns L / m, R / Ω and the calculated column the analysis needs - none is needed beyond R itself, since the plot is R against L directly; the headings are all quantity / unit, and the mean diameter and area are recorded beside the table with their units.
(c) The x-axis runs L from 0 to 1.000 m and the y-axis runs R from 0 to 12 Ω - both from zero, since the readings start near zero and a zero start fills more than half the grid in both directions. Scales: 0.1 m per 2 cm square on x, 1 Ω per 2 cm square on y. The seven points lie close to one straight line.
(d) Two points on the line, far apart: (0.150 m, 3.5 Ω) and (0.950 m, 12.2 Ω). ΔR = 12.2 − 3.5 = 8.7 Ω and ΔL = 0.950 − 0.150 = 0.800 m, so the gradient is 8.7 ÷ 0.800 = 10.875 = 10.9 Ω m⁻¹. The x-axis starts at zero, so the intercept is read where the line crosses the y-axis: about 1.9 Ω. (Values from a hand-drawn line vary by a few percent; the triangle's size is the mark.)
(e) Gradient = ρ/A, so ρ = gradient × A = 10.875 × 6.25 × 10⁻⁸ = 6.797 × 10⁻⁷ = 6.80 × 10⁻⁷ Ω m to three significant figures. The intercept is r = 1.9 Ω, the resistance of the leads and contacts.
(f) The x-axis starts at zero here, so the drawn y-axis is the line x = 0, and the point where the trend line crosses it is the y-intercept, read directly. If the shortest length had been 0.500 m, an axis starting at zero would leave the readings crowded into the top half, so a false origin at about 0.400 m would fill the grid - and the drawn y-axis would then be at L = 0.400 m, not zero, so the crossing would be R at 0.400 m and the intercept would have to be calculated from c = y − mx with a point on the line.""",
    guidance=["Table and headings: the quantity / unit columns and the mean-diameter working in (a) and (b) are the presentation marks - the micrometer's repeats and the area's unit conversion are what the table rests on.",
              "Graph and gradient: the scales filling the grid, the line and the large-triangle gradient in (c) and (d) - the far-apart points on the line are what the gradient's uncertainty rests on.",
              "Conclusion and criterion: ρ from gradient × A and r from the intercept in (e), with units, and the read-or-calculate judgement in (f) is the false-origin criterion applied - the conclusion is what the graph was for."],
)

# ---------- P04: Paper 3 Question 2 style, thermal/liquid (cooling, deliberately inaccurate) ----------
T['P04'] = dict(
    objective_ids=['OBJ-9702-12.3-07', 'OBJ-9702-12.3-09', 'OBJ-9702-12.3-11', 'OBJ-9702-12.3-13'],
    claims=['CLM-9702-12-066', 'CLM-9702-12-093', 'CLM-9702-12-094', 'CLM-9702-12-078'],
    command_word='Estimate',
    prompt="""A learner investigates how quickly hot water in a beaker cools, to test the suggestion that the mass lost by evaporation in the first two minutes is proportional to the water's starting temperature excess above room temperature. The method is inaccurate: the beaker is moved between readings, the thermometer is read while the bulb touches the glass, and the balance is draughty.

The mass of water lost in two minutes is found by weighing the beaker before and after. Here are our readings (two runs at each condition).

| Condition | m lost / g (run 1) | m lost / g (run 2) |
|---|---|---|
| hot (about 80 °C) | 1.8 | 2.2 |
| warm (about 50 °C) | 1.1 | 1.3 |

The suggested relationship is: the mass lost is proportional to the temperature excess, so m lost ÷ (T − Troom) should be the same constant at both conditions. Take the room as 25.0 °C and the water's mean starting temperatures as 78.6 °C and 51.2 °C.
(a) Estimate the absolute uncertainty in the mass lost at each condition, from the repeats, and hence the percentage uncertainty in each. [3]
(b) Calculate the constant m ÷ (T − Troom) at each condition, in g °C⁻¹. [2]
(c) State a criterion first, then determine whether the data support the suggested proportionality. [3]
(d) Give four limitations of this experiment, each naming the measurement it affects and how. [4]
(e) Give four improvements, each tied to the limitation it answers. [4]
(f) The thermometer's readings at the bulb touching the glass carry a systematic error, not a random one. Explain why repeating the readings does not reduce this error, and what does. [2]""",
    answer="""(a) Hot condition: the range of the repeats is 2.2 − 1.8 = 0.4 g, so the absolute uncertainty is 0.4 ÷ 2 = 0.2 g, on a mean of 2.0 g - a percentage uncertainty of 0.2 ÷ 2.0 = 0.10, which is 10%. Warm condition: the range is 1.3 − 1.1 = 0.2 g, so the absolute uncertainty is 0.1 g on a mean of 1.2 g, and 0.10 ÷ 1.2 = 0.0833, which is 8.3%.
(b) Hot: mean m = 2.0 g, T − Troom = 78.6 − 25.0 = 53.6 °C, so the constant is 2.0 ÷ 53.6 = 0.0373 g °C⁻¹. Warm: mean m = 1.2 g, T − Troom = 51.2 − 25.0 = 26.2 °C, so the constant is 1.2 ÷ 26.2 = 0.0458 g °C⁻¹.
(c) Criterion stated first: the mass measurements carry about 10% uncertainty, and the temperature difference carries the sum of two thermometer readings' doubts (say ± 0.5 °C each) on 53.6 °C and 26.2 °C - under 2% and 4% respectively - so a criterion of about 10% covers the weaker measurements; the two constants support the proportionality only if their percentage difference lies inside that. The values are 0.0373 and 0.0458 g °C⁻¹: the difference is 0.0458 − 0.0373 = 0.0085 g °C⁻¹ on a mean of 0.04155, which is 0.0085 ÷ 0.04155 = 0.2046, or 20%. The difference lies outside the 10% criterion, so the data do not support the suggested proportionality: the warm water lost proportionally more than the hot, and the imbalance is twice what the measurement uncertainties allow.
(d) Four limitations, each naming its measurement: (1) the mass lost, because the beaker is moved onto and off the balance between readings, so water splashed on the outside or a fingerprint changes the recorded mass by tenths of a gram - the same order as the quantity being measured; (2) the temperature, because the thermometer's bulb touches the glass, so it reads the glass rather than the water, and it reads low by a similar amount in every run - a systematic error; (3) the mass lost again, because the balance sits in a draught, so the reading wanders while it settles and the recorded mass depends on when the reader stops watching; (4) the temperature excess, because the room temperature is read once at the start and assumed constant, so if the room warms or cools during the runs, both conditions' excesses are computed against the wrong baseline.
(e) Four improvements, one per limitation: (1) keep the beaker on the balance for the whole run and read the mass in place - the difference of two readings taken without lifting it - so nothing is splashed or added between readings; (2) stir the water with the thermometer held clear of the glass, or use a clip holding the bulb in the middle of the water, so it reads the water's temperature; (3) shield the balance with a draught screen and wait for the reading to settle before taking it, so the recorded mass is the settled value, the same for every run; (4) read and record the room temperature at the start and end of each run, and use the mean, so the excess is computed against the baseline that actually held.
(f) The bulb-on-glass error is systematic: every reading is shifted the same way - low, by roughly the same amount - so repeats scatter randomly around the shifted value and their mean carries the shift undiminished; averaging cancels random scatter, and this error is not random. What reduces it is removing the cause: holding the bulb in the middle of the water, away from the glass, so the thermometer reads the water; the correction, once made, is made for every reading at once.""",
    guidance=["Table and headings: the two-condition readings table in the prompt is the record the analysis works from, its columns carrying the repeats side by side.",
              "Uncertainties: half the range of the repeats for each absolute uncertainty, then the percentage in (a) - the estimates are what the criterion in (c) is built from.",
              "Constants and criterion: the two constants in (b), and the test in (c) with the criterion stated before the comparison - the percentage difference against the percentage uncertainty is the analysis.",
              "Limitations and improvements: the four in (d) each name the measurement, the cause and the effect, and the four in (e) pair with them one-to-one - the pairing is what the marks are for, and the systematic-error question in (f) closes the method's diagnosis."],
)

if __name__ == '__main__':
    print(len(T), 'tasks')
