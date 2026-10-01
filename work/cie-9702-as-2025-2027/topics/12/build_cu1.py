#!/usr/bin/env python3
"""Build CU-9702-12.1 (Manipulation, measurement and observation) from the existing ledger."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _lib
from _lib import block, save, wc, WS

blocks = []
blocks.append(block('12.1-b0', 'learner_objective', 'What this section covers',
    'Setting up apparatus from written instructions and diagrams, choosing the right instrument for the size it measures, taking readings that span the whole available range, repeating them, timing oscillations, reading analogue scales and digital displays, and recording every reading accurately and consistently.', []))

blocks.append(block('12.1-b1', 'plain_explanation', 'Setting up',
"""Apparatus is set up in the order the instructions give, and the order has a logic: supports and clamps first, the measuring instruments next, and any electrical supply connected last, so that the finished arrangement can be looked over before anything is switched on. A stand that tips, a rule that slips in its clamp or a meter wired the wrong way round is cheap to fix before the first reading and expensive after it, because every reading taken on a faulty arrangement inherits the fault.

Before the first reading, the assembled apparatus is checked against the instructions. The stands are stable, weighted or bolted so they cannot tip when the load goes on. The instruments read zero with nothing applied: a top-pan balance that shows 0.02 g with an empty pan has a zero error, and it is either re-zeroed or recorded and subtracted from every reading, because a zero error is systematic and shifts every reading the same way. Every connection matches the diagram, and the hanging parts hang freely, because a spring that brushes the rule reads long on one side and short on the other.

The check is physical, not mental. A stand is nudged to see whether it rocks. A spring is loaded lightly and watched to see whether it hangs without touching anything. A rule is read against the bench edge to see whether it sits square. Each check takes seconds, and each names a fault that would otherwise sit inside every reading to follow.

Setting up is where the practical marks start, and the syllabus reserves at least seven of the twenty marks of a Paper 3 question for manipulation, measurement and observation. A learner who assembles in the written order, checks the zero of each instrument against nothing, and compares the finished arrangement with the diagram before switching on has already earned the first of them: the experiment that follows measures the physics, not the faults.""",
    ['CLM-9702-12-001', 'CLM-9702-12-002']))

blocks.append(block('12.1-b2', 'plain_explanation', 'Following instructions and diagrams',
"""Written instructions are followed one step at a time, in the order written, and each finished step is compared with the diagram before the next begins. The discipline matters because a mistake is easiest to see at the step where it was made: a wire joined to the wrong terminal is visible against the circuit diagram at that step, and invisible one step later, buried inside a finished arrangement.

A circuit is built the way its diagram is drawn. The components are connected in the order the diagram shows - supply to switch to rheostat to ammeter to lamp, and back - and the voltmeter is added across the lamp afterwards, because the diagram shows it in parallel, not in the loop. A meter connected the wrong way round reads in the wrong direction, so the positive terminal of every meter faces the positive terminal of the supply. When the circuit is complete it is checked wire by wire against the diagram, with the switch open, and only then is the supply connected and switched on: the last connection is the one that makes the arrangement live, and it is made after the checking is finished.

The same habit carries a written method through. "Hang the 100 g load, wait for the spring to settle, read the length against the rule" is three steps, and each one is done, checked against the instructions, and only then followed by the next. A learner who jumps straight to the readings skips the arrangement the method was written for.""",
    ['CLM-9702-12-003', 'CLM-9702-12-004', 'CLM-9702-12-005']))

blocks.append(block('12.1-b3', 'plain_explanation', 'How much data is enough',
"""An experiment earns its conclusion from its data set, so the set has to be worth concluding from. For a graph, that means at least six well-spaced readings of the dependent variable against the independent one, with repeats where the scatter matters: six points is enough to show a trend and support a line of best fit, and fewer leaves the line balancing on guesses.

The independent variable is changed in steps that span its whole available range. A wire on a metre board offers lengths from perhaps 0.100 m to 1.000 m, and the readings belong at both ends and evenly between them - not four of them crowded between 0.400 m and 0.500 m, however neatly those points might line up. The reason is the gradient: a trend line drawn over a long span divides the plotting error by a long base, so the gradient's percentage uncertainty is small; a line drawn over a short band concentrates the same error and the gradient suffers for it.

Quantity of data is also honesty at the bench. Readings are taken until the table holds enough rows to show the trend, and each row holds the repeats it needed. Six readings, spread from the shortest usable length to the longest, each repeated where it scattered - that is a data set a graph can carry and a conclusion can rest on.""",
    ['CLM-9702-12-006', 'CLM-9702-12-007']))

blocks.append(block('12.1-b4', 'plain_explanation', 'Repeats and what they cure',
"""Where readings scatter, each reading is repeated and the mean of the repeats is used. Averaging works because the scatter is random: readings land either side of the true value, and high and low partly cancel in the mean, so the mean sits closer to the truth than a typical single reading. That is the whole argument for the repeat - not ritual, but the arithmetic of random error.

Repeating is also honest about what it cannot do. A zero error - a balance reading 0.02 g with nothing on it, a micrometer showing 0.03 mm shut - is systematic: it adds the same offset to every reading taken, so every repeat inherits it and the mean carries exactly the same offset as any single reading. The cure for a systematic error is to measure it and subtract it, not to out-number it with repeats.

At the bench the repeats are recorded as they are taken, each in its own place in the table, and the mean is written beside them: an average written in place of the repeats hides the scatter it came from. A reading that looks unusual is recorded anyway and repeated again - the table shows what happened, and the mean of agreeing readings is the value used.""",
    ['CLM-9702-12-008', 'CLM-9702-12-009']))

blocks.append(block('12.1-b5', 'plain_explanation', 'Instruments and their resolutions',
"""Each instrument is matched to the size it measures. A micrometer screw gauge, reading to 0.01 mm, belongs on a wire's diameter; a millimetre rule, reading to 1 mm, belongs on lengths above a few centimetres; calipers belong on internal widths, where a rule cannot reach. A protractor measures angles, a top-pan balance mass, a newton meter force, a measuring cylinder volume, a thermometer temperature, and the electrical meters, analogue or digital, current and voltage. The resolution of an instrument, the smallest change it can show, sets the number of decimal places a raw reading is recorded to.

The micrometer deserves its care named, because it is the instrument that punishes haste. The jaws are closed on the object using the ratchet, which slips at a set grip, so the jaws hold the wire without squashing it - twisting the sleeve by hand squeezes a soft wire and reads small. The zero error is checked first, with the jaws closed on nothing, and recorded and subtracted from every reading. A wire's diameter is taken at several places and in two perpendicular directions, because wires are not uniform, and the mean of those readings is the value used.

Choosing an instrument is also choosing an uncertainty. A 1 mm rule on a 30 mm length leaves about 2% in the reading; the same rule on a metre leaves a twentieth of that. The instrument is picked so that its resolution is small against the quantity it measures, which is what makes a reading worth taking.

A measuring cylinder is read at the bottom of the meniscus with the eye level with it, and the volume is recorded to the cylinder's graduations - 1 cm³ on a 250 cm³ cylinder, for instance. A thermometer is read while its bulb sits in what it measures, not after withdrawal, and a newton meter is read at the moment the load is steady, with the pointer not swinging. Each instrument names its own care, and the common thread is the same: the reading is taken the way the instrument was built to be read, at the moment it was built to be read.""",
    ['CLM-9702-12-010', 'CLM-9702-12-011']))

blocks.append(block('12.1-b6', 'process', 'Timing an oscillating system',
"""The period of an oscillating system - a load bouncing on a spring, a metal strip vibrating - is measured by timing a whole number of complete oscillations and dividing by that number. One complete oscillation is one full journey there and back: the load passes its lowest point, rises, falls and passes the lowest point going the same way again. At least ten are timed, usually twenty, and the timing is repeated and averaged.

The reason for counting many is the stop-watch's own weakness. Starting and stopping carry a reaction uncertainty of a few tenths of a second however many oscillations are timed, so over twenty oscillations that fixed uncertainty is shared across the whole run: the percentage uncertainty in the total is about a twentieth of what it would be timing one, and the period, the total divided by the count, inherits the same small share. Timing a single oscillation hands the full reaction uncertainty to a reading of well under a second, which is why a single-swing period cannot be trusted.

The count has to be honest. The watch is started as the moving part passes a chosen marker, and stopped as the part passes the same marker at the end of the last complete oscillation - a whole number of complete oscillations, never a half, and never the whole run until the motion dies away, which is a different quantity entirely. The marker is chosen where the part moves fastest, not at an end of the swing, because the instant of crossing is sharpest there and the start and stop are timed most surely. The test of a usable timing is: has a whole number of complete oscillations been timed? A timing that passes it gives a period; one that does not gives a number with no meaning at all.""",
    ['CLM-9702-12-012', 'CLM-9702-12-013', 'CLM-9702-12-082']))

blocks.append(block('12.1-b7', 'plain_explanation', 'Analogue scales and digital displays',
"""An analogue scale, a pointer moving over divisions, is read with the eye directly above the pointer, estimating to the nearest half of the smallest division. The eye position matters because the pointer stands above the scale: viewed from the side it appears against a different mark, and the same instrument gives different readings to different eyes. Reading from directly above removes the parallax error the geometry creates.

A digital display is read once the value has settled: the digits hunt while the reading stabilises, and any number caught mid-hunt is a snapshot of the settling, not a measurement. The display names its unit - the panel is marked mA or mV, or the range switch names it - and the reading is recorded in the unit the display shows, converted to whatever unit the table heading uses. A display flashing an over-range warning is reporting that the reading lies outside the range selected, and the response is a larger range, not a squint.

Both kinds of instrument share one habit: the reading is taken in the instrument's own unit and written down at the moment it is read. A milliammeter showing 250 is a current of 250 mA, which is 0.250 A - writing 250 A stores a thousand times the current the meter reported. The number and the unit belong together, or the reading never happened.""",
    ['CLM-9702-12-014', 'CLM-9702-12-015']))

blocks.append(block('12.1-b8', 'plain_explanation', 'Accurate readings',
"""A measurement is made accurate by care at the three moments it can go wrong: sighting, recording, converting.

The sighting: a reading on a scale is taken with the eye in line with the pointer or the edge being read, because viewing at an angle shifts the apparent position of the mark against the scale - the parallax error again - and the instrument, however fine, cannot correct a sight line that is wrong. For a liquid in a measuring cylinder the eye reads the bottom of the meniscus, level with the graduation.

The converting: every recorded reading carries the unit of the instrument's display, converted to the unit the table heading uses. A reading on a milliampere display is a current in milliamperes until it is converted; writing the display's number under a heading in amperes stores a current a thousand times too large, and every value calculated from the row inherits the error. The same honesty covers reading a scale in its printed direction - a scale read backwards reports a value that was never shown.

The recording: a reading is written as it is taken, not remembered for later. The record at the bench is the experiment's memory, and a reading held in the head is a reading half lost. Taken together - eye in line, unit converted, written at once - the readings in a table are what the instruments actually said.""",
    ['CLM-9702-12-016', 'CLM-9702-12-017', 'CLM-9702-12-083']))

blocks.append(block('12.1-b9', 'plain_explanation', 'The widest range of readings',
"""The independent variable spans the largest range of values within the limits of the equipment provided or the instructions given. If the wire offers 0.100 m to 1.000 m, the readings run from near one end to near the other; if the loads run to 600 g, the readings do not stop at 150 g. Within the span the readings are spread evenly, so the plotted points fill the graph rather than gathering wherever the apparatus found convenient.

The argument is the gradient, and it deserves its full statement. A trend line drawn from a narrow band of readings is short, so the triangle used for the gradient is small, and the same plotting error is divided by a short run: the gradient carries a large percentage uncertainty, and a constant determined from it is barely a constant at all. The same error spread over a long line is divided by a long base, and the gradient becomes worth quoting. The widest range the apparatus allows is the cheapest accuracy available in the whole experiment, because it costs only the decision to use it.

The test of a range is whether the data cover the whole span the apparatus permits. A learner whose readings run from 0.100 m to 1.000 m of the board has passed it; one whose points cluster between 0.400 m and 0.500 m has run a neat experiment on a tenth of the question, and neatness does not repair a short line.""",
    ['CLM-9702-12-018', 'CLM-9702-12-019', 'CLM-9702-12-084']))

blocks.append(block('12.1-b10', 'worked_calculation', 'A timing worked through',
"""A load bouncing on a spring is timed through twenty complete oscillations, three times, on a stop-watch reading to 0.1 s. The three totals are 17.4 s, 17.6 s and 17.5 s.

The mean total is (17.4 + 17.6 + 17.5) ÷ 3 = 52.5 ÷ 3 = 17.5 s, and the period is T = 17.5 ÷ 20 = 0.875 s. The totals scatter by 0.2 s from highest to lowest, so the absolute uncertainty in the total is half of that, 0.1 s, and the period inherits a twentieth of it: 0.1 ÷ 20 = 0.005 s. The percentage uncertainty in the period is 0.005 ÷ 0.875 = 0.00571, which is 0.57%, so the period is 0.875 ± 0.005 s - a timing to be pleased with, and the direct product of counting twenty oscillations instead of one. Timing a single oscillation would have left the same 0.1 s sitting on a reading of about 0.875 s, over 10% of it, and no amount of care at the watch would have repaired the choice.""",
    ['CLM-9702-12-012', 'CLM-9702-12-013']))

blocks.append(block('12.1-b11', 'cross_link', 'Where this connects',
"""This topic is the practical half of everything else in the subject. Topic 1's uncertainties and significant figures are the language used here to state what a reading is worth; topics 2 and 3 supply the motion that oscillating loads and falling objects run on; topic 6's Hooke's law gives the spring experiments their physics; topics 9 and 10 supply the meters, the circuits and the resistance that the electrical experiments measure. The reverse holds too: every experiment met in topics 1 to 11 is an occasion to practise these skills, and the bench is where the marks for them are earned.""",
    []))

text_words = sum(wc(b['text']) for b in blocks)
unit = {
    'unit_id': 'CU-9702-12.1',
    'title': 'Manipulation, measurement and observation',
    'objective_ids': ['OBJ-9702-12.1-01', 'OBJ-9702-12.1-02', 'OBJ-9702-12.1-03', 'OBJ-9702-12.1-04',
                      'OBJ-9702-12.1-05', 'OBJ-9702-12.1-06', 'OBJ-9702-12.1-07', 'OBJ-9702-12.1-08',
                      'OBJ-9702-12.1-09'],
    'level': 'AS Level',
    'core_status': 'core',
    'objective_type': 'prac_mmo',
    'depth_tier': 3,
    'word_budget': {'min': 2551, 'target': 3100, 'max': 3647},
    'blocks': blocks,
    'word_count': text_words,
    'qa_status': 'review_required',
    'notes': ['Authored for Cambridge 9702 AS 2025-2027; word budget from the topic 12 work order.'],
}
save(os.path.join(_lib.TDIR, 'content-units/CU-9702-12.1.json'), unit)
print('word_count:', text_words)
