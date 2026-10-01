#!/usr/bin/env python3
"""Build CU-9702-12.3 (Analysis, conclusions and evaluation)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _lib
from _lib import block, save, wc, WS

blocks = []
blocks.append(block('12.3-b0', 'learner_objective', 'What this section covers',
    'Reading a graph as an equation: gradients and intercepts, including from false origins and tangents; estimating uncertainties as absolute and percentage values; drawing conclusions and constants with units; testing a suggested relationship against a criterion stated first; making predictions; and stating limitations, the most significant sources of uncertainty, and improvements tied to the measurements they affect.', []))

blocks.append(block('12.3-b1', 'plain_explanation', 'The straight line and its equation',
"""An equation of the form y = mx + c gives a straight-line graph of y against x, with m the gradient and c the y-intercept; the equation is rearranged into this form before the graph is plotted. The rearranging is the analysis: the experimenter decides what to plot so that the plot is a line, and the decision is made from the equation being tested.

The rearrangement is worth watching once, in symbols, because the same move serves every experiment. The load-extension relation of a spring, F = kx, is already y = mx + c with y as F, x as x and c = 0: plotting force against extension gives a line through the origin whose gradient is the stiffness k. The resistance of a wire of length L, R = (ρ/A)L + r, rearranges nothing: plotted as R against L it gives a straight line whose gradient is ρ/A and whose intercept is r - the resistivity is recovered by multiplying the gradient by the measured area. To find a constant from a graph, the equation is rearranged so the constant is the gradient or the intercept, and then the graph does the finding.

The payoff is that two numbers read off a line - gradient and intercept - carry the whole experiment's physics, with the scatter of the points showing how far to trust them. But the payoff exists only if the plot was arranged to be straight: an equation left un-rearranged, plotted as a curve, gives a graph whose shape can be described but whose constants stay unread.""",
    ['CLM-9702-12-054', 'CLM-9702-12-055']))

blocks.append(block('12.3-b2', 'process', 'Reading coordinates from a trend line',
"""Coordinates are read from a trend line at the intersection of labelled lines, using the smallest division on each axis to resolve values between the labels. The reading is an act of measurement in its own right: the point chosen sits on the line, not near it, and both coordinates are read to the smallest division the grid honestly resolves - typically half a small square.

A point read from the line is written with both coordinates and their units, because any gradient or intercept calculated from it inherits those units. "(0.250 m, 1.01 s²)" is a reading; "(0.25, 1.01)" is a pair of bare numbers that cannot enter an equation, and the habit of writing units with coordinates is what keeps the unit of the gradient right two steps later.

The points read for a gradient are chosen with the gradient in mind: two points on the line, far apart, covering at least half the drawn line between them. The end of the line nearest the last plotted point is the natural place to read, because the line is longest there and the smallest mis-reading of the line is divided by the longest run. A reading at each end, written down with units, is half the gradient done.

Reading coordinates is also how a graph is checked against its table. After the line is drawn, a point at the middle of the trend is read off and compared with the reading that should be there - a mid-line reading that disagrees with the table by a full square has caught either a plotting slip or a bad reading, and either way it was caught at the graph, where it costs a minute, rather than in the conclusion, where it costs the experiment.""",
    ['CLM-9702-12-056', 'CLM-9702-12-057']))

blocks.append(block('12.3-b3', 'process', 'The gradient',
"""The gradient of a straight-line graph is Δy/Δx, found from two points on the line, not data points, that are far apart and cover at least half the drawn line, and it carries the unit of y divided by the unit of x. The working is written in full: the two points, the differences, the division, the unit. A gradient quoted without its working cannot be checked, and a gradient quoted without its unit names no quantity at all.

The two points are on the line itself. A data point used for the gradient drags the calculation back to a single reading, with that reading's scatter in it; the line exists precisely to average the scatter away, and the gradient taken from the line has the whole data set behind it. Using points close together, or data points that are not on the line, is the error; the test is whether both points are on the line and far apart.

A large triangle on the line gives a gradient with a smaller percentage uncertainty than a small one, because the same plotting error is divided by a longer run. Read to the nearest half square, the coordinates carry perhaps 0.25 of a small square of doubt each way; over a run of twenty squares that doubt is a percent or two, and over a run of three squares it is a tenth of the value. The large triangle is the cheapest accuracy on the graph, and it is chosen at the moment the two points are picked.""",
    ['CLM-9702-12-058', 'CLM-9702-12-059', 'CLM-9702-12-090']))

blocks.append(block('12.3-b4', 'process', 'The intercept',
"""The y-intercept is the value of y where the line crosses the x = 0 line; where the x-axis is a false origin, the intercept is calculated from c = y − mx using a point on the line. The distinction is the whole skill: an axis that starts at, say, 0.600 m simply does not show x = 0, and the point where the line meets the drawn edge of the grid is a point at x = 0.600 m, not an intercept. Reading the y-intercept off an axis that does not start at x = 0 is the error; the test is whether the x-axis starts at zero.

Where the intercept is small compared with the readings, it is found by calculation from c = y − mx rather than by eye, because the eye cannot judge a small offset on a large scale. A line that crosses near the bottom of the grid, read by eye, gives an intercept within a whole small square of doubt - and a small square on a scale of 0.2 is 0.2 of doubt in a value that may itself be 0.3. The calculation costs one line of working and removes the squinting entirely.

The intercept carries its unit, and the unit comes from the y-axis alone: the intercept is a value of y. A graph of R against L has an intercept in Ω; a graph of T² against L has an intercept in s². The intercept also usually means something - r, the residual resistance of the leads, or a constant the theory predicts - and a calculated intercept that lands on the value the theory named is one of the quiet pleasures of the practical room.""",
    ['CLM-9702-12-060', 'CLM-9702-12-061', 'CLM-9702-12-089']))

blocks.append(block('12.3-b5', 'worked_calculation', 'A gradient and an intercept worked through',
"""A wire's resistance R is measured against its length L, and the readings plot as a straight line of R against L on a grid where the x-axis starts at 0.400 m (a false origin - the shortest usable length). Two points on the line, far apart, read (0.500 m, 4.8 Ω) and (0.900 m, 9.6 Ω).

The gradient: ΔR = 9.6 − 4.8 = 4.8 Ω, and ΔL = 0.900 − 0.500 = 0.400 m. The gradient is ΔR/ΔL = 4.8 ÷ 0.400 = 12.0 Ω m⁻¹ - the unit is Ω divided by m, stated with the value.

The intercept: the x-axis starts at 0.400 m, not zero, so the intercept is calculated, not read. Using the point (0.500 m, 4.8 Ω): c = y − mx = 4.8 − 12.0 × 0.500 = 4.8 − 6.0 = −1.2 Ω. The line crosses the R-axis below zero, which for R = (ρ/A)L + r means r, the resistance of the leads and contacts, appears negative - a cue to look for a contact fault rather than to quote the value blind.

Had the graph been read by eye instead, the intercept would have carried the doubt of a whole small square on the R-axis scale - and the reading would have looked confidently wrong. The calculation is one line long, and it is the only honest way to read an intercept off a false-origin graph.""",
    ['CLM-9702-12-058', 'CLM-9702-12-060', 'CLM-9702-12-061']))

blocks.append(block('12.3-b6', 'plain_explanation', 'Estimating absolute uncertainty',
"""The absolute uncertainty in a single reading is half the resolution of the instrument, and in a difference of two readings it is the sum of their absolute uncertainties. A rule reading to 1 mm leaves ± 0.5 mm on a single length; a length found as the difference of two rule readings - the position of a mark minus the position of the bench edge - carries ± 1 mm, because each reading brings its own half-millimetre and the difference inherits both.

A zero error shifts every reading by the same amount, so it is measured and subtracted; it is a systematic error and survives any number of repeats. The subtraction is exact bookkeeping, not an estimate: the micrometer that reads 0.03 mm shut adds 0.03 mm to every reading it takes, and every reading has it subtracted again. What survives after the subtraction is the random scatter, which is the next case.

Where the reading was repeated, the repeats themselves measure the uncertainty: the absolute uncertainty in a repeated measurement is half the range of the repeats, where the repeats scatter randomly about a steady value, and the mean of the repeats is the best estimate. The three cases - single reading, difference, repeats - are the whole toolkit, and the first question of any estimate is which of the three the quantity belongs to.""",
    ['CLM-9702-12-062', 'CLM-9702-12-063', 'CLM-9702-12-066']))

blocks.append(block('12.3-b7', 'plain_explanation', 'Absolute and percentage uncertainty',
"""The percentage uncertainty is the absolute uncertainty divided by the value, × 100%; translating back, the absolute uncertainty is the percentage divided by 100, times the value. The two forms say the same thing in different units: the absolute form states the doubt in the unit of the quantity (± 0.005 s), the percentage form states it as a share of the value (0.57%), and the translation between them is one multiplication either way.

The percentage form is the one that compares. A ± 0.5 mm doubt on a length of 30 mm is 1.7% of it; the same doubt on a length of 300 mm is 0.17% - the same absolute care, worth ten times more on the longer reading. When the question is which measurement weakens the experiment most, the percentage uncertainties answer it, and only they do.

The percentage uncertainty of a difference of two readings is found by adding the two absolute uncertainties and dividing by the difference; using one reading's uncertainty alone is the error, and the test is whether the quantity is a difference of two readings. The rule matters most where the difference is small: two thermometers each read to ± 0.5 °C give a temperature difference with ± 1.0 °C of doubt, and on a difference of 4 °C that is 25% - a "small" difference of two good readings can be the least trustworthy number in the experiment.

Two combining rules carry the forms through a calculation. In a product or quotient of measured quantities the percentage uncertainties add, and a value raised to a power n carries n times the percentage uncertainty of the quantity: an area πd²/4 from a diameter measured to 2% holds 4% (twice the diameter's), and a T² calculated from a T measured to 1% holds 2%. The rules are why a small uncertainty in a squared or multiplied quantity can quietly dominate an experiment, and why the estimate is made before trusting the result.""",
    ['CLM-9702-12-064', 'CLM-9702-12-065', 'CLM-9702-12-091']))

blocks.append(block('12.3-b8', 'plain_explanation', 'Half the range, and its limits',
"""Half the range is the standard estimate of the uncertainty from repeats: the absolute uncertainty in a repeated measurement is half the range of the repeats - the largest minus the smallest, halved - and the mean is the value quoted with it. Five timings spread over 0.7 s carry ± 0.35 s; the mean of them is the best estimate the set supports.

The estimate is honest about where it applies. Half the range is appropriate where repeats scatter randomly; where readings drift steadily in one direction the scatter is not random, and half the range then understates the real uncertainty. Readings that climb 2.1, 2.3, 2.6, 2.8 are not four measurements of one value - something in the apparatus is changing, a warming wire, a slipping clamp - and the honest response is to find and name the drift, not to average over it. Forgetting to halve the range is the other error, and the test is whether the range is divided by two.

The repeats must also be genuine: at least two, taken the same way, in the same conditions. A "repeat" taken after adjusting the apparatus measures the adjustment, and half the range of a pair like that is a number with no experiment behind it. The estimate is only as good as the repeats it is drawn from, and the repeats are only as good as the bench discipline that took them.""",
    ['CLM-9702-12-066', 'CLM-9702-12-067', 'CLM-9702-12-092']))

blocks.append(block('12.3-b9', 'plain_explanation', 'Conclusions and constants',
"""A conclusion is drawn from the graph: the constants of the equation come from the gradient and the intercept, with their units, and the scatter of the points about the line shows how far the data can be trusted. The conclusion is the experiment's answer, and it is written as values with units, not as a mood: k = 12.0 Ω m⁻¹ × 0.123 mm² = 1.48 × 10⁻⁷ Ω m, or as close as the graph supports.

A constant found from a graph is stated with its unit worked out from the units of the axes. The gradient of R against L arrives in Ω m⁻¹; multiplied by the area in m² it becomes the resistivity in Ω m. The working of the unit is part of the working of the value, and the check is run the other way too: a resistivity quoted in Ω m⁻¹ has kept the gradient's unit and lost the area's, and the error is visible in the unit before it is visible anywhere else.

The conclusion also states what the graph showed about the relationship - the points lay close to a straight line, the scatter was about 2% of the readings - because a constant without a stated trust is a number pretending to be exact. The scatter is not a confession; it is a measurement of the measurement, and quoting it is what separates a conclusion from a claim.""",
    ['CLM-9702-12-068', 'CLM-9702-12-069']))

blocks.append(block('12.3-b10', 'plain_explanation', 'Testing a suggested relationship',
"""A suggested relationship is tested by comparing the values it gives against a criterion stated before the comparison, usually the estimated percentage uncertainty: the data support the relationship where the percentage difference between the values is smaller than the criterion. The order is the whole discipline - criterion first, comparison second - because a criterion chosen after seeing the numbers is not a test at all, it is a number chosen to agree with itself.

The judgement that data support a relationship names the values compared, the percentage difference between them, the criterion, and whether the difference lies inside it. "The two values of the constant differ by 4%, and the estimated percentage uncertainty in the measurements is 5%, so the data support the suggested relationship" - that is a judgement a reader can check. Saying the data support a relationship because two values are close, with no criterion, is the error; the test is what counts as close enough, and whether it was stated before comparing.

The comparison is usually made where the relationship leaves a number checkable: a constant calculated twice from two different parts of the data, or a calculated value against a value measured directly. Each route carries its own percentage uncertainty, the criterion is the larger of them (or their sum, where both routes are measured), and the comparison is one division: the percentage difference against the percentage uncertainty. Inside the criterion, supported; outside it, not supported - and both answers are worth full marks when the criterion was honest.""",
    ['CLM-9702-12-070', 'CLM-9702-12-071', 'CLM-9702-12-093']))

blocks.append(block('12.3-b11', 'plain_explanation', 'Making predictions',
"""A prediction from a graph is a value read from the trend line, between the readings or a short way beyond them, with the unit of the axis it is read from. The prediction is the graph paying back the work of plotting: a line drawn through ten readings answers any reading in its span, including values nobody measured.

Between the readings, the prediction carries the scatter of the points as its uncertainty - a line through points scattered 2% predicts values good to about 2%. A short way beyond the readings, the prediction adds the small assumption that the trend continues past the last point measured, which is usually safe for a gentle extension of a well-populated line.

A prediction made far beyond the measured range assumes the trend continues, which a straight line within the measured range does not guarantee. A wire's resistance rising linearly to 1.000 m does not promise the same rise to 1.500 m - the wire may warm, the contacts may change - and a graph of cooling does not extend to "when it reaches room temperature" as a straight line would have it. The prediction is quoted with its span: read from the line, for a value within or just past the measured range, in the unit of the axis, and saying so.

A prediction can also be checked, and the check is worth making. The predicted value is stated with the reading it came from - "at L = 0.550 m, the line reads R = 6.6 Ω" - so that a reader with the same graph can find the same value. A prediction stated as a bare number is a claim about the graph nobody can verify, and the whole value of a prediction is that the graph verifies it for anyone.""",
    ['CLM-9702-12-072', 'CLM-9702-12-073']))

blocks.append(block('12.3-b12', 'plain_explanation', 'Limitations, stated properly',
"""A limitation is stated by naming the measurement it affects, what makes that measurement unreliable, and its effect on the result, not by a general phrase such as human error. The three parts are what make a limitation worth marks: the measurement (the period, the diameter, the temperature), the cause (the load swings slightly sideways, the wire is not uniform, the room warms during the run), and the effect (the timings scatter by more than the repeat spread suggests, the area carries the wire's non-uniformity into the resistivity).

The most useful limitations are those that affect the measurements with the largest percentage uncertainty, because changing them changes the result most. The order of work is therefore: estimate the percentage uncertainty of each measurement, rank them, and name the limitations behind the largest - the diameter measured to 3% dominates a resistivity experiment (it enters squared, at 6%), and the limitation that explains its scatter is the one worth stating first.

The vague phrase is the enemy because it names nothing. "Human error" cannot be improved, because nobody knows what to change; "parallax" without saying which scale and which reading is a word, not a diagnosis. The test of a real limitation is: which measurement, and what exactly makes it unreliable? A limitation that passes that test is half an improvement already, and the four limitations a Paper 3 question asks for are four answers to it.

The four are chosen, not scraped. A Paper 3 evaluation asks for four limitations because the experiment has four worth naming - the ranking of percentage uncertainties points at them, and the bench experience explains them. Writing down whatever four phrases arrive first produces the vague list the marking guidance warns against; writing the four behind the largest uncertainties produces a list a reader could act on, which is the whole standard.""",
    ['CLM-9702-12-074', 'CLM-9702-12-075', 'CLM-9702-12-094']))

blocks.append(block('12.3-b13', 'plain_explanation', 'The most significant sources of uncertainty',
"""The most significant source of uncertainty is the measurement with the largest percentage uncertainty; the percentage uncertainties are compared to find it. The comparison is the analysis: each measurement's estimate - half the resolution, half the range of repeats, the sum for a difference - is divided by its value, and the largest share names the source that most weakens the experiment's answer.

A source of uncertainty is significant where its percentage uncertainty is comparable with the others: a large absolute uncertainty in a large value can matter less than a small one in a small value. A ± 0.5 mm doubt on a length of 800 mm is 0.06% of it; a ± 0.01 mm doubt on a wire's diameter of 0.30 mm is 3.3%, and squared in the area it becomes over 6%. The small instrument doubt on the small quantity dominates, and the comparison by percentage is what sees it - the absolute comparison does not.

The significant source is also where the improvement money goes. An experimenter with one afternoon and one budget improves the measurement whose percentage uncertainty is largest, because halving the largest share halves the total it dominates; halving a share already at 0.06% changes nothing the conclusion can see. The ranking is the experiment's own diagnosis of itself, and it is the first thing an evaluation asks for.

The ranking deserves to be shown, not just stated. The percentage uncertainty of each measurement is written down beside its value - the length 0.06%, the diameter 3.3% entering squared at 6.6%, the temperature difference 25% - and the list is what the answer cites. An evaluation that shows its ranking can be checked line by line; one that announces a source without the list is asking to be believed rather than followed, and the credibility of the whole evaluation rests on the numbers being visible.""",
    ['CLM-9702-12-076', 'CLM-9702-12-077']))

blocks.append(block('12.3-b14', 'plain_explanation', 'Improvements, and describing them',
"""A modification improves the accuracy of an experiment where it reduces the uncertainty of the measurement it is aimed at, and it is justified by naming the limitation it answers. The pairing is the discipline: each improvement exists because a specific limitation was stated, and the improvement names it - "the diameter is the largest uncertainty, so measure it with a micrometer at several places and in two directions, averaging" - and an improvement with no limitation behind it is a solution looking for a problem.

An investigation is extended to answer a new question by changing the independent variable or the range, keeping the measurements that worked and stating the new question first. The same wire experiment extends to temperature (does the resistivity rise when the wire warms?) by adding a heater and a thermometer, keeping the micrometer and the same table structure - extension is a redesign of one variable, not a new experiment from scratch.

A modification is described clearly enough to be carried out: the equipment, where it is placed, what it replaces, and what is done with it, in words or a diagram. A description of a modification names the apparatus, its position in the arrangement, and the measurement it improves, so a reader could set it up without asking a question. "Use a data-logger" names nothing; "replace the stop-watch with a data-logger with the light gate at the marker, timing twenty oscillations automatically" could be built from the sentence. The test is the test of the limitation again, run in reverse: which limitation does the improvement fix, and how, exactly?""",
    ['CLM-9702-12-078', 'CLM-9702-12-079', 'CLM-9702-12-080', 'CLM-9702-12-081', 'CLM-9702-12-095']))

blocks.append(block('12.3-b15', 'cross_link', 'Where this connects',
"""Everything in this section runs on the machinery of topics 1 and 12.1-12.2: the percentage uncertainty is topic 1's arithmetic, the table and graph are 12.2's craft, and the estimate of what a reading is worth begins at the instrument chosen in 12.1. The conclusions drawn here feed back into the content: topic 6's stiffness, topic 9's resistivity, topic 2's acceleration of free fall are all constants that a graph like this recovers. Paper 3's second question is this section end to end - an inaccurate method, an uncertainty, a test against a criterion, four limitations and four improvements - and the marks for all of it are earned at the bench.""",
    []))

text_words = sum(wc(b['text']) for b in blocks)
unit = {
    'unit_id': 'CU-9702-12.3',
    'title': 'Analysis, conclusions and evaluation',
    'objective_ids': ['OBJ-9702-12.3-%02d' % n for n in range(1, 15)],
    'level': 'AS Level',
    'core_status': 'core',
    'objective_type': 'prac_analysis',
    'depth_tier': 3,
    'word_budget': {'min': 3968, 'target': 4600, 'max': 5673},
    'blocks': blocks,
    'word_count': text_words,
    'qa_status': 'review_required',
    'notes': ['Authored for Cambridge 9702 AS 2025-2027; word budget from the topic 12 work order.'],
}
save(os.path.join(_lib.TDIR, 'content-units/CU-9702-12.3.json'), unit)
print('word_count:', text_words)
