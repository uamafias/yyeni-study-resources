"""Original integrated practical skills and six complete assessment families."""
import math
from authoring_common_8224 import Topic,stamp
from organic_visuals_8224 import Figure
t=Topic('5.1')
def add(n,claims,title,text):
 t.objective(n,claims,[(title,text)],'NSSCAS-8224-SYLLABUS','Annexe A2 printed pp38–42 practical criteria, A5 p50 titration layout; Annexe D pp53–54 supplies qualitative reference. Worked data and deductions are original; chemistry principles from local OpenStax Chemistry §§4.5,5.2,12.1.')
add('1-01',[
 'Apparatus must be stable and arranged so the desired quantity can be measured without unintended loss or obstruction.',
 'A burette is clamped vertically and its tip filled before an initial reading is taken.'
], 'Set up for the measurement you need', '''Choose apparatus by the quantity and precision required. For a titration, clamp a burette vertically over a conical flask on a white tile. Rinse the burette with its intended solution, fill the tip and remove an air bubble before taking the initial reading. Remove the filling funnel so later drops cannot change the measured delivery. Use a pipette filler for the measured aliquot and keep the flask accessible for swirling.

For gas collection, connect the reaction vessel to a freely moving gas syringe through airtight tubing. Support the syringe and check that the apparatus has enough capacity for the expected gas. Leaks lose product before measurement; a stuck plunger can obstruct collection. A thermometric setup instead needs an insulated vessel and a thermometer positioned in the liquid without pressing against the vessel wall.

Sketch the actual measurement path before starting: what enters, what leaves and where the reading is made. Follow the supervised laboratory instructions and specified reagent handling. Apparatus that looks complete can still fail if its tip is unfilled, its joint leaks or its scale cannot be read.''')
add('1-02',[
 'Following a practical instruction requires preserving the specified quantities, order, timing and distinction between fresh portions and the same mixture.',
 'Reagent added dropwise and then in excess describes two observations on the specified sample, not interchangeable single additions.'
], 'Turn instructions into an ordered method', '''Read the complete sequence before transferring a reagent. Mark which quantities are measured, which additions are gradual, which observations precede the next addition and where a fresh portion is required. A diagram can specify a connection or thermometer position that is not repeated in the prose. Match labels between the diagram and the written method before assembling it.

“Add dropwise, then in excess” asks you to observe the initial change and then what happens when substantially more reagent is present. Record both stages. “Use a fresh portion” means take another portion of the original sample; it does not mean add a new reagent to a mixture already altered by the previous test. Otherwise a precipitate or gas may come from earlier additions rather than the unknown.

For timed reactions, identify exactly when timing begins and the defined endpoint. For a titration, identify which liquid goes in the burette and which measured portion goes in the flask. If an instruction is unclear, resolve it with the supervisor before proceeding rather than silently swapping quantities. The resulting record should make it possible to connect each observation to the action that caused it.''')
add('1-03',[
 'Useful observations specify the nature, colour and change of a material, including its behaviour with further reagent.',
 'A dataset needs enough readings to reveal the intended change rather than one isolated endpoint without context.'
], 'Collect enough detail to discriminate', '''Record what you actually see before interpreting it. “Pale blue precipitate, dissolving in excess to give a dark blue solution” describes three different features. “Blue” alone does not state whether the colour belongs to a solid or solution, or whether excess reagent changed it. Note effervescence, temperature change and whether a precipitate remains, where these are relevant to the specified test.

For a temperature experiment, one reading before mixing and one much later may miss the highest temperature. Collect a baseline and frequent readings around the reaction, then continue long enough to reveal cooling. For a rate experiment, readings across the rising region are more informative than several readings taken after gas production has finished.

Use the same descriptive level for comparable samples. If one result says “white precipitate insoluble in excess”, the other should also record initial precipitate and excess behaviour rather than merely “reacted”. Quantity comparisons such as more precipitate require comparable sample and reagent amounts. Topic 3.4 illustrates why a colour needs its material and reagent context; the qualitative task below supplies the specific reference results needed for its deductions.''')
add('1-04',[
 'Instrument reading precision should match the scale: this syllabus normally uses burette readings to0.05 cm³ and1°C-scale thermometer readings to0.5°C.',
 'Delivered burette volume is final reading minus initial reading; a pipette transfers its calibrated volume according to its design.'
], 'Use each scale correctly', '''Read a burette at eye level, using the appropriate meniscus for the liquid. Record two decimal places to the nearest 0.05 cm³ for the normal syllabus convention. A final reading 24.85 cm³ and initial reading 0.20 cm³ give a delivered titre of 24.65 cm³. The final reading alone is not the delivered volume unless the initial reading was zero.

A volumetric pipette transfers a fixed calibrated volume. Use a filler, align the meniscus with the mark and allow delivery according to its calibration; do not force out a retained tip drop unless that pipette is designed for it. A measuring cylinder is less suitable when a small volume uncertainty matters. With a 1°C thermometer scale, normally estimate to 0.5°C; immerse the sensing part appropriately and wait for its response.

Start a timing device at the defined reaction start and stop at the defined endpoint, not at an arbitrary convenient moment. Record balance readings using the displayed resolution. Raw precision comes from the measuring instrument and method, while the precision of a calculated result also depends on all inputs. Topic 1.1 supplies the unit conversions used after these readings are obtained.''')
add('1-05',[
 'Accuracy concerns closeness to an accepted value, while precision concerns agreement or resolution; consistent readings can share a systematic bias.',
 'Matching the endpoint criterion and viewing geometry improves consistency of repeated observations.'
], 'Accuracy and consistency answer different questions', '''Repeat measurements using the same endpoint definition and observation arrangement. In a titration, slow to dropwise addition near the expected endpoint, swirl thoroughly and compare the persistent indicator change against a white background. A rapid stream can overshoot even if the burette itself is read neatly. For a disappearing-cross reaction, use the same cross, viewing direction and criterion for disappearance in each run.

Precision describes agreement between repeated readings and the resolution with which they are recorded. Accuracy describes closeness to the accepted value. Titres 24.65 and 24.70 cm³ are close to each other; this supports consistency but does not prove that the concentration calculated from them is accurate. A contaminated reagent or biased calibration can affect both similarly.

Inspect the apparatus before explaining scatter. A bubble expelled from a burette tip during delivery can make the indicated volume exceed the volume actually delivered to the flask. Repeating the same faulty setup does not establish its accuracy. Use a consistent method, inspect plausible biases and report the readings rather than adjusting them to fit an expected result. Later evaluation sections distinguish removable bias from random variation.''')
add('1-06',[
 'The number of tests should be chosen to separate the stated candidates efficiently while preserving fresh material for confirmation.',
 'Repeating the same non-discriminating test does not add a new distinction between two ions with the same outcome.'
], 'Choose how many observations are needed', '''Start from the question being answered. To distinguish two candidate ions, choose a supplied test whose predicted outcomes differ, then plan a confirmation if an ambiguous observation remains. Performing many unrelated additions to one tube can destroy the evidence needed for later deductions. Keep enough original material for fresh-portion comparisons and gas tests where appropriate.

If both candidates produce a white precipitate with a particular reagent, that first observation does not distinguish them. Excess-reagent solubility or a second supplied reagent may do so. Conversely, once a discriminating observation has been obtained clearly and confirmed, repeating several chemically equivalent tests may waste time without testing a new explanation.

For a continuous variable, collect enough distinct settings to reveal a trend and repeats to assess scatter. Three tightly clustered settings can be less informative about a curve than a wider pilot range with additional points near its changing region. The choice depends on available time, reagent and the experiment's response. State why the extra reading is needed: to resolve an ambiguity, confirm an endpoint or test a suspected anomaly. A numerical count of tests without that purpose is not a complete plan.''')
add('1-07',[
 'A suitable range includes enough distinct independent-variable settings to show the relevant trend.',
 'Additional readings near a rapid change or intersection can improve interpretation without replacing wider-range coverage.'
], 'Distribute measurements across the response', '''Choose the independent-variable range using a preliminary trial and the expected measurable response. Avoid settings at which the change is too small to read or too fast to time reliably. Within a useful range, regular spacing is a reasonable starting point, while extra points can be added where the response curves sharply or two fitted regions meet.

For a concentration investigation, five distinct concentrations spanning a usable interval provide more information about proportionality than five repeated runs at one concentration. Repeats are valuable, but they answer a different question: scatter at a particular setting. Keep the total liquid volume constant by adding measured water when concentration is changed by dilution.

For a thermometric titration, gather points on both sides of the maximum or intersection rather than stopping once warming is noticed. For a time series, use shorter intervals during the fastest change and longer intervals once the response slows, if the method permits. Record the actual chosen settings, not just “a range”. This lets another reader judge whether the graph covers enough of the phenomenon. The graphing unit below explains how the chosen range affects scale selection and the reliability of interpolation.''')
add('1-08',[
 'Reading time must match the process, distinguishing stabilisation, a transient maximum and a persistent titration endpoint.',
 'Waiting longer can improve a slow instrument response but can lose a transient temperature maximum through heat transfer.'
], 'Decide when a reading represents the process', '''A useful waiting time depends on what is being measured. Before a thermal reaction, allow starting solutions to approach the same chosen temperature and check a stable baseline. After mixing, record frequently enough to capture the rise and subsequent cooling. Waiting several minutes for a single “stable final” temperature can miss the maximum because heat is already leaving the solution.

Near a titration endpoint, add a small amount, swirl and wait long enough to decide whether the colour persists under the stated method. A redox endpoint may require a pale colour to remain for a specified period; the persistence criterion belongs with the observation. Do not substitute an intense colour caused by overshooting.

For gas collection, continue until no further measurable increase occurs over an appropriate interval, while recognising that a leak can also produce an apparent plateau. For slow dissolution or precipitation, allow the instructed time before judging solubility. A preliminary run can establish a sensible sampling interval. Explain the choice through the response time or transient change, rather than treating a longer wait as an automatic improvement. In a recorded method, state both the interval between readings and the criterion used to stop collecting them.''')
add('1-09',[
 'Repeat measurements assess random scatter; anomalous readings should be investigated rather than silently deleted.',
 'This syllabus seeks concordant titres within0.10 cm³; the closest suitable pair can be used for the mean while the rough titre is excluded.'
], 'Repeat where it improves the evidence', '''Use a rough titration to locate the endpoint, then obtain careful repeat titres. For this syllabus, concordant titres agree within 0.10 cm³. Mark the closest suitable pair used in the mean and exclude the rough value. If careful titres remain inconsistent, inspect delivery, endpoint recognition and apparatus before calculating a mean that hides the disagreement.

For example, careful titres 24.65, 24.70 and 25.10 cm³ support choosing the first two. Their mean is 24.675 cm³; retain that value during subsequent calculation and report at a justified precision. Investigate the third value as a possible overshoot or other anomalous run, recording the reason rather than erasing it from the original table.

Repeats also apply to qualitative work: an unexpected precipitate may need a fresh-portion test to check contamination. Replicating a rate run at selected settings helps assess timing scatter. Repeats do not remove a constant scale offset or restore heat already lost systematically. State which uncertainty the repeat can address and preserve individual readings so the observed spread remains visible. The recording unit below shows how raw and selected data can occupy one coherent table.''')
add('1-10',[
 'A confirmatory test should supply an additional discriminating observation interpreted through the supplied reference.',
 'Gas identity requires its specified test rather than inference from effervescence alone.'
], 'Confirm the proposed identity', '''Effervescence shows gas production, not gas identity. Use a suitable fresh gas sample with the supplied reference test: carbon dioxide turns limewater milky, ammonia turns damp red litmus blue, oxygen relights a glowing splint, and hydrogen gives a pop with a lighted splint under the supervised procedure. Do not apply a flame test indiscriminately to an unknown gas mixture. The task specifies which gas test is appropriate.

For an ion, select confirmation that addresses the remaining alternative. A pale blue precipitate followed by dissolution in excess ammonia to a dark blue solution is more discriminating than the word “blue” alone. A carbonate proposal gains support when the gas produced with dilute acid is confirmed as CO2 rather than merely observed bubbling.

Keep observation and deduction in separate table columns. If the supplied notes do not distinguish two possible ions with the chosen test, report the ambiguity and choose a different permitted comparison rather than claiming certainty. Fresh portions help avoid attributing an observation to a reagent used earlier. Topic 3.4 covers relevant halogen chemistry, but the purpose here is to use the provided notes to select and interpret observations, not memorise an unsupported list of tests.''')
add('1-11',[
 'Distinguishing reagents are selected by comparing candidate outcomes, including initial precipitate and excess behaviour.',
 'Separate fresh portions prevent one reagent from changing the outcome of another comparison.'
], 'Select reagents from a candidate table', '''Read the supplied candidate results before choosing a reagent. Aluminium and zinc both give white precipitates soluble in excess aqueous sodium hydroxide, so that comparison alone cannot separate them. With aqueous ammonia, the aluminium precipitate remains in excess whereas zinc's dissolves. That difference supplies a useful second test on fresh portions.

Likewise a barium-nitrate precipitate can require acid treatment to distinguish sulfate from sulfite using the supplied notes. A persistent white precipitate after nitric acid supports sulfate; dissolution supports the sulfite alternative. Use the order and reagent specified in the question. Selecting a reagent because it produces any visible reaction is insufficient when both candidates share that reaction.

Write a small decision table: candidate, first addition, excess or follow-up, predicted difference. Then perform only the permitted comparisons and record the actual outcomes. If an observation is faint, use comparable sample amounts, a clean background and fresh apparatus to check it. Do not convert an unresolved pale precipitate into a confident identity merely to complete the table. The practical qualitative task includes its reference outcomes so the reasoning remains reconstructible offline.''')
add('2-01',[
 'A single coherent table keeps trial identifiers, raw readings and calculated values aligned.',
 'Selected data for a mean should be identified without removing other original readings.'
], 'Keep one coherent results table', '''Prepare one table in which each trial keeps its associated readings together. A titration table can use trial columns with rows for initial reading, final reading and titre, or trial rows with separate quantity columns. Either orientation must make it unambiguous which final reading belongs to which initial reading. Include units in headings and identify the rough trial.

An original example is shown below. The final-minus-initial calculation gives each titre; the two careful values are selected for the mean.

| Trial | Initial reading / cm³ | Final reading / cm³ | Titre / cm³ |
|---|---:|---:|---:|
| Rough | 0.00 | 25.30 | 25.30 |
| 1 | 0.20 | 24.85 | 24.65 |
| 2 | 0.10 | 24.80 | 24.70 |

The careful titres differ by 0.05 cm³, within the 0.10 cm³ concordance criterion. Preserve the rough reading even though it is not averaged. For qualitative tests, use the same idea of alignment: each reagent addition needs its observation and inference beside it, rather than collecting unlabelled colour descriptions elsewhere on the page.''')
add('2-02',[
 'A prepared table reduces copying and ensures the intended measurements have labelled places before a reaction starts.',
 'Table design should allow repeats and raw readings, not just a precomputed final answer.'
], 'Prepare a table before starting', '''Design the table after reading the method and before collecting data. Include trial or sample identifiers, raw quantities and any derived column needed for the question. Leave enough space for repeats and unexpected observations. A cramped table can turn a careful result into an ambiguous entry, particularly when colour, solid formation and excess behaviour must all be described.

For a gas-volume time series, prepare Time / s and Gas volume / cm³ columns. For a thermometric experiment add a note marking when mixing occurred so that baseline and post-mixing readings are distinguishable. For titration include both initial and final burette readings instead of reserving space for the titre alone.

Before using a prepared table, check a sample subtraction or unit conversion to confirm that the necessary columns exist. For instance, initial 1.10 cm³ and final 25.75 cm³ need a Titre / cm³ cell for 24.65. Do not write an expected value into a raw-reading cell before observing it. Preparation organises evidence; it does not authorise inventing data that an experiment did not produce.''')
add('2-03',[
 'Raw data, derived values and deductions have distinct roles and should be labelled separately.',
 'A calculated column should retain the raw values from which it was derived.'
], 'Separate measurements from calculations and conclusions', '''Raw readings are directly observed quantities, such as mass before and after a reaction or initial and final temperature. Derived values combine those readings, such as mass loss or temperature rise. A conclusion interprets them chemically. Give these roles separate labelled columns or clearly separated table sections so that a reader can check each step.

For a balance experiment, include Initial mass / g, Final mass / g and Mass loss / g. If the readings are 52.64 and 52.20 g, the derived loss is 0.44 g. The statement that gas escaped is an interpretation requiring the method and chemical reaction; it is not another balance reading. For qualitative analysis, “white precipitate remains in excess” is an observation, while “consistent with Al3+ among these candidates” is a deduction.

Retaining raw data allows a correction to be traced. If a subtraction is wrong, fix the derived value rather than changing the observed masses to fit it. The thermometric and rates tasks below use raw and derived columns together; Topic 2.1 supplies the energy relationship used after a measured temperature rise has been established.''')
add('2-04',[
 'A table heading identifies both the measured quantity and its unit in an accepted form such as Volume / cm³.',
 'Ambiguous symbols need clarification, especially when t could mean time or temperature.'
], 'Headings carry quantity and unit', '''Write headings such as Time / s, Temperature / °C, Volume / cm³ or Concentration / mol dm−3. “Volume (cm³)” is also clear. A bare unit does not say what was measured, and a bare quantity leaves its scale undefined. Place the unit in the heading so numerical entries can be read consistently without repeating a symbol in each cell.

Use an unambiguous quantity name. If a table contains both time and temperature, a column labelled t is unclear; spell out the quantities or define distinct symbols. For derived columns, the unit may differ from the raw one. A reciprocal time column is 1/time / s−1, while a time interval remains in seconds.

For example, times 100.0 and 50.0 s give reciprocal values 0.01000 and 0.02000 s−1. Writing those under Time / s would mislabel the calculation even though the arithmetic is correct. Unit conversion should also be explicit: a measured volume in cm³ divided by 1000 gives dm³ for use with concentration in mol dm−3. Topic 1.1 explains why matching these units matters for amounts of substance.''')
add('2-05',[
 'Raw readings in a column use consistent decimal precision compatible with the apparatus.',
 'Qualitative observations should use comparable descriptive detail across samples.'
], 'Record instrument precision', '''Use the resolution and reading convention of the apparatus rather than a number of decimal places chosen to look impressive. Normal burette readings here use two decimal places with the last digit 0 or 5. A 1°C-scale thermometer normally supports 0.5°C steps in the stated syllabus practice. Balance readings should retain the displayed decimal places consistently within a raw-data column.

If a balance resolves 0.01 g, write 2.40 g rather than 2.4 g when that is the actual display. The trailing zero records resolution; it does not change the mass. Subtracting 2.40 from 2.85 g gives 0.45 g, retaining the hundredth-gram place. A calculated quantity may later need a significant-figure decision, which is a separate issue.

Consistency also applies to words. Describe the initial precipitate, its colour and excess-reagent behaviour for each comparable sample. “White solid remained” and “dissolved to a colourless solution” are more comparable than “white” and “nothing”. Record changes as they occur instead of relying on memory after several similar tubes have been tested.''')
add('2-06',[
 'A calculation shows relationship, conversions, substitution, working and result so its reasoning can be reconstructed.',
 'A chemical deduction links observations to supplied reference outcomes rather than stating an identity without evidence.'
], 'Show the route to the answer', '''Begin a calculation with the relationship required. For a concentration calculation, use n=cV with V in dm³ when c is in mol dm−3. State the reaction's mole ratio before converting from one reactant to the other. Then calculate the requested amount, concentration or mass. Carry enough intermediate digits to avoid premature rounding and include units in the final answer.

For 24.675 cm³ of 0.100 mol dm−3 NaOH, V=0.024675 dm³ and n=0.100×0.024675=0.0024675 mol. If it neutralises a 25.00 cm³ HCl aliquot in a 1:1 reaction, c(HCl)=0.0024675/0.02500=0.0987 mol dm−3 to three significant figures. The mean titre remains unrounded until the final step.

Show reasoning similarly in qualitative work. A white precipitate soluble in excess NaOH fits both Al3+ and Zn2+ from the supplied notes; a fresh-portion ammonia test then distinguishes the remaining candidates by excess solubility. The intermediate alternatives matter. An unexplained final identity hides whether the observation actually discriminated it. Topic 2.2 supplies balanced redox ratios used in the redox titration task.''')
add('2-07',[
 'Calculated precision should reflect the least accurate measured input, with guard digits retained until the final result.',
 'Decimal places and significant figures are different conventions: zero before the first nonzero digit is not significant.'
], 'Round after the calculation', '''Read the precision of the supplied quantities before deciding how many significant figures to report. The syllabus permits calculated results at the same number of significant figures as the least accurate measured input, or one more where justified. Do not add precision by multiplying several rounded values. Keep guard digits in working and round the final result clearly.

The number 0.0500 has three significant figures, while 0.05 has one. A mass 5.00 g has three; a raw balance reading's decimal places still depend on the display. For a measured 0.100 mol dm−3 standard and titre 24.675 cm³ used internally, a resulting concentration 0.0987 mol dm−3 appropriately reflects three significant figures in the standard.

In a subtraction, absolute reading resolution matters: temperatures 23.0 and 29.5°C give a rise 6.5°C, not an artificially precise 6.500. A later enthalpy based on that rise should not claim five reliable significant figures. State the chosen precision with the final answer. Exact coefficients in a balanced equation do not restrict significant figures because they count the stoichiometric ratio rather than represent uncertain measurements.''')
add('3-01',[
 'A table is suited to discrete qualitative comparisons, whereas a graph can reveal a continuous quantitative trend.',
 'Using both preserves raw values while making a response pattern easier to assess.'
], 'Choose a useful display', '''Use a table for observations linked to samples or reagent additions. It preserves the exact words and makes initial and excess behaviour easy to compare. For a continuous measured response such as gas volume against time, a graph reveals a changing gradient more clearly than a sequence of numbers alone. Keep the raw table as well, because a graph does not replace the original measurements.

Choose the display according to the question. A straight-line calibration graph can help estimate an unknown concentration, while a precipitate's colour and solubility are better shown in a labelled observation table. A bar chart can suit categories; it is less useful than a continuous plot when the independent variable varies continuously and intermediate values have meaning.

Before plotting, decide what feature the display should reveal: trend, gradient, intercept, comparison or anomaly. This prevents a decorative graph from obscuring the calculation. The rates task uses both measured times and a reciprocal-time graph. Topic 2.4 explains the chemistry behind the changing rates, while this unit focuses on making the measured evidence readable.''')
add('3-02',[
 'Axes identify variables and units, with a regular readable scale chosen to use a substantial part of the available grid.',
 'The independent variable is normally horizontal and the dependent response vertical unless a specified transformation requires otherwise.'
], 'Choose variables and readable scales', '''Put the chosen independent variable on the horizontal axis and the measured dependent variable on the vertical axis unless a specified relationship calls for a different arrangement. Label both with quantity and unit. Gas volume / cm³ against Time / s means the vertical coordinate is volume, not a second time reading.

Choose regular increments that are easy to subdivide, such as 1, 2 or 5 units per major grid interval. Use enough of both dimensions to distinguish the points and draw a gradient triangle. A graph occupying a tiny corner makes interpolation and slope less reliable. A numerical axis need not start at zero when a different origin makes the required trend clearer, but show the chosen range honestly.

For times from 0 to 100 s and volumes from 0 to 60 cm³, a horizontal range 0–100 and vertical range 0–60 is sensible. The scale should include the data rather than stopping short of the last point. Recheck that equal physical distances represent equal numerical intervals. Topic 5.1.4 applies these displays to unknown values and control-variable evaluation.''')
add('3-03',[
 'Each plotted point must correspond to its actual x,y pair and be visible without concealing its location.',
 'An anomaly remains part of the recorded evidence even if excluded from fitting with an explanation.'
], 'Plot positions rather than approximate impressions', '''Locate each coordinate separately using the stated scales, then make a fine cross or another small clear symbol. A large blob can conceal whether a point is correctly placed. Check that each raw-table row has one matching point unless the graph intentionally uses a derived value such as a mean or reciprocal time.

If one horizontal division represents 10 s and one vertical division 5 cm³, a reading at 25 s and 32 cm³ belongs halfway between 20 and 30 s and two units above 30 cm³. Do not round it to the nearest major intersection simply to make plotting easier. If two points overlap, annotate their multiplicity or retain the table so the repeats remain known.

Check extreme points and suspected anomalies first because a misplaced point can distort the fitted trend. If an observation is genuinely anomalous, ring or label it and explain how it is treated. Do not move it towards the line, delete it silently or alter the raw table. A correctly plotted unexpected result can be useful evidence about the experiment.''')
add('3-04',[
 'A best-fit line or curve represents the overall trend and need not pass through each measured point.',
 'A straight model should not be forced through zero unless the model and evidence justify that constraint.'
], 'Fit the trend supported by the data', '''Inspect the plotted pattern before choosing a straight line or smooth curve. A roughly linear pattern supports a best-fit straight line with points distributed on both sides. A changing gradient can require a smooth curve. Joining successive measured points with sharp corners treats random scatter as if it were a physical change in the underlying process.

For a gas-volume curve, reaction often slows as a reactant is consumed. A curve can rise steeply and then level off. A straight line across the whole run would hide that changing rate. Conversely, a linear calibration should not be replaced by an arbitrary curved path just to touch each point.

Use a fine, continuous line and keep excluded anomalies visible. Do not force a line through the origin because the axes happen to cross there; an intercept can reveal a baseline contribution or systematic offset. If a theoretical model predicts zero response at zero input, consider whether the measured uncertainty supports that constraint. The next sections explain how transformations, slopes and intercepts turn the fitted trend into a quantitative interpretation.''')
add('3-05',[
 'A suitable variable transformation can turn an expected relationship into y=mx+c for testing with a straight-line graph.',
 'For a fixed small reaction endpoint,1/time can be a rate proxy when the same extent of reaction is compared.'
], 'Use a justified linear treatment', '''Choose transformed variables because a model predicts a relationship, not because a straight line looks convenient. For repeated reactions timed to the same small extent, reciprocal time can act as a rate proxy. Plotting 1/time against concentration can then test proportionality over the range studied, provided the endpoint, temperature, total volume and other relevant factors are matched.

For concentrations 0.20, 0.40, 0.60, 0.80 and 1.00 mol dm−3, illustrative endpoint times 100.0, 50.0, 33.3, 25.0 and 20.0 s give reciprocal times approximately 0.0100, 0.0200, 0.0300, 0.0400 and 0.0500 s−1. This is nearly linear with slope 0.0500 s−1 per mol dm−3 and intercept near zero.

![Original reciprocal-time data and linear fit](assets/8224-practical-linear-rate.png)

The reciprocal is not automatically a measured initial rate in mol per second. It is a comparison based on the fixed endpoint; a changing endpoint invalidates it. State the model, transformation and units before using the fitted line. Topic 2.4 provides the kinetic principles, while the practical rates task asks you to test the transformation with original data.''')
add('3-06',[
 'A straight-line gradient is Δy/Δx with units derived from both axes; its intercept is the predicted y at x=0.',
 'A large triangle on the fitted line gives a more stable slope estimate than two very close measured points.'
], 'Interpret slope and intercept physically', '''For a straight-line model y=mx+c, m is the gradient and c the vertical intercept. Choose two well-separated coordinates on the fitted line, not necessarily two raw points, and calculate Δy/Δx. Use a triangle spanning at least half the useful line where possible. The units are vertical-axis units divided by horizontal-axis units.

If a volume–time line passes through (10 s, 8 cm³) and (90 s, 40 cm³), its gradient is (40−8)/(90−10)=0.400 cm³ s−1. Extending that line to zero time gives an intercept of 4 cm³. The gradient describes the modelled volume increase per second; the intercept describes the extrapolated volume at zero time and may reflect an initial reading offset or an actual initial volume, depending on the method.

Do not interpret an intercept by naming its number alone. Explain what zero on the horizontal axis means in that experiment. If zero lies far outside the measured range, the extrapolated value can be uncertain even when the measured points fit well. Report the coordinates used so another reader can check both the arithmetic and the physical meaning.''')
add('3-07',[
 'A tangent gradient estimates instantaneous rate at a chosen point, while a secant gives an average over an interval.',
 'Area has a physical interpretation only when the axis quantities give a meaningful product, such as rate×time.'
], 'Tangent rate and meaningful area', '''On a curved volume–time graph, draw a tangent at the specified time and calculate its gradient using a large triangle on that tangent. This estimates the instantaneous volume-production rate there. A line connecting the beginning and end of a long interval instead gives an average rate and can miss the changing local slope.

An original model is V=60(1−exp(−time/40)) cm³ with time in seconds. At 40 s the volume is about 37.9 cm³ and its tangent gradient about 0.552 cm³ s−1. The tangent can be read using widely separated coordinates near (0 s,15.9 cm³) and (80 s,60.0 cm³). The curve itself is not that straight line.

![Original volume curve and tangent at40s](assets/8224-practical-tangent.png)

An area under a rate–time graph has units of amount or volume and can represent accumulated production. An area under a volume–time graph instead has units cm³ s and is not the total gas volume. Check units and the physical model before assigning meaning. Topic 2.4 supplies rate concepts; this skill connects a graph construction with the particular rate requested.''')
add('4-01',[
 'A trend description uses stated variable changes and supporting values rather than an unsupported adjective.',
 'A changing gradient should be distinguished from a change in the final amount produced.'
], 'Support patterns with measured values', '''State what changes as the independent variable increases, quoting values that show the pattern. For gas production, “volume rises from 0.0 to 37.9 cm³ in the first 40 s and then to 51.9 cm³ by 80 s” is more informative than “it increases quickly”. Equal time intervals here give smaller volume gains later, supporting a decreasing average rate.

Distinguish rate from final amount. Two runs can reach the same plateau at different speeds if the same limiting amount reacts. A steeper initial curve does not by itself establish more total gas. Likewise a larger final volume does not prove faster reaction if the experiment used more reactant.

Use the table or graph's actual numbers and units. Describe the measured range before extending to a broader claim. If a point departs from the pattern, identify it rather than hiding it in a vague statement such as “mostly proportional”. The supplied qualitative notes can support patterns across samples too, but use comparable reagent amounts before claiming that one precipitate quantity is larger. Topic 2.4 links a declining gas-production rate to the changing reacting system.''')
add('4-02',[
 'An observation summary retains features that distinguish the candidates, including excess behaviour and confirmed gas identity.',
 'A summary should not replace an observed event with an untested chemical inference.'
], 'Summarise the distinguishing evidence', '''A useful summary selects the observations relevant to the question while preserving their detail. For a cation comparison, record initial precipitate colour and whether it dissolves in excess reagent. For an anion comparison, include gas evolution and the result of its confirmation. These are different kinds of evidence and should not be collapsed into the word “reaction”.

For example, “A gave a white precipitate with NaOH, soluble in excess, but its ammonia precipitate remained in excess; B dissolved in excess with both reagents” summarises a discriminating pattern from the supplied notes. It does not yet replace the interpretation step that assigns candidate identities.

State negative observations as carefully as positive ones. “No visible precipitate after the specified addition and observation time” is clearer than leaving a blank, which could mean that the test was not done. If a solution colour obscures a small solid, acknowledge that limitation and improve the comparison. An honest summary can retain ambiguity where the collected observations do not separate the candidates. The qualitative task asks for both the observed pattern and the reason it supports a particular conclusion.''')
add('4-03',[
 'An unknown value can be obtained by interpolation on a fitted calibration within the measured range.',
 'Extrapolation beyond the data range depends more strongly on the assumed model and should be identified.'
], 'Read an unknown from coordinates', '''Use the fitted relationship rather than choosing the nearest raw point. To estimate an unknown concentration from a measured response, move from that response to the calibration line and then to the concentration axis. Show the construction or state the coordinates so the reading can be checked. Keep the unit associated with the quantity, not just the numerical coordinate.

For a calibration S=20.0c+0.10, where S is a stated dimensionless signal and c is in mol dm−3, S=0.70 gives c=(0.70−0.10)/20.0=0.0300 mol dm−3. Subtracting the intercept matters; dividing 0.70 directly by 20.0 would ignore the baseline signal. If the calibration was measured from 0.0100 to 0.0500 mol dm−3, this is interpolation.

A response corresponding to 0.0800 mol dm−3 would require extrapolation beyond that range. Report that dependence rather than presenting it as equally well supported. A new measured standard nearer the unknown can test the model there. The graphing unit's slope and intercept rules therefore contribute directly to finding unknowns, rather than being isolated numerical exercises.''')
add('4-04',[
 'A mean should use appropriately selected comparable repeats and preserve unrounded intermediate values.',
 'Stoichiometric calculations require a balanced reaction and matching volume units.'
], 'Calculate from selected comparable data', '''Identify which repeats measure the same quantity under the same settings. For titres, use a suitable concordant pair and show which are selected. For 24.65 and 24.70 cm³, the mean is (24.65+24.70)/2=24.675 cm³. A rough value is used to guide the endpoint, not included just because it is another number in the table.

Convert the mean to the volume unit required by concentration before calculating moles. Then use the balanced equation's ratio. In a redox titration, one manganate(VII) ion can react with five Fe2+ ions in acid; treating that as a 1:1 ratio would overwhelm a small improvement in burette precision. Topic 2.2 gives the balanced electron accounting.

When averaging rate runs, state whether you average endpoint times and then invert or calculate and average reciprocal times; these are not exactly identical for scattered data. Follow the task's requested method and retain individual values. A mean without the spread can conceal inconsistent measurements. Report a calculated conclusion at a precision justified by the measured quantities and distinguish a theoretical amount from an experimentally recovered one.''')
add('4-05',[
 'A fitted-line or tangent gradient is obtained from two separated coordinates on that line with correct axis units.',
 'Using successive noisy raw points can estimate a local average but is not identical to a tangent construction.'
], 'Calculate the gradient you actually drew', '''Mark two coordinates on the straight line or tangent used for the interpretation. Form a triangle large enough that small reading uncertainties are a limited fraction of its height and width. Calculate change in the vertical quantity divided by change in the horizontal quantity, preserving the sign where it has meaning. State the unit derived from both axes.

For the volume tangent near 40 s, coordinates (0 s,15.9 cm³) and (80 s,60.0 cm³) give (60.0−15.9)/80=0.55125 cm³ s−1, appropriately about 0.55 cm³ s−1 from those graph readings. This is compatible with the underlying model's approximately 0.552 rate. It is not the average rate from time zero to 80 s on the curve.

For a decreasing mass–time graph, a negative gradient indicates decreasing measured mass; its magnitude can describe mass-loss rate if that is the requested quantity. Do not silently remove a negative sign without stating the physical convention. If the graph is a transformed plot, use its transformed units rather than assigning a familiar rate unit automatically.''')
add('4-06',[
 'A control variable must be maintained or monitored well enough that it cannot plausibly explain the observed response difference.',
 'Stating a variable is controlled is weaker evidence than showing how it was held and checked.'
], 'Evaluate whether a control worked', '''Identify variables other than the chosen independent one that can affect the response. In a concentration–rate experiment these can include temperature, total volume, particle size, amount of solid and mixing method. State how each is kept comparable and what measurement checks that it remained so. A list of names without a method does not demonstrate control.

If successive reaction mixtures start at 20.0, 22.0 and 25.0°C as concentration increases, temperature is confounded with concentration. Faster reaction could partly reflect warmer mixtures. A thermostatically controlled bath and measured starting temperatures reduce that ambiguity. Merely using the same room does not guarantee the liquid temperatures match.

When diluting a reagent, replace the removed reagent volume with measured water to keep the total volume constant. Keep other reactants in the intended excess and use the same endpoint. Evaluate actual values where available: a temperature spread smaller than the stated measurement uncertainty may be less concerning than a systematic several-degree rise. Topic 2.4 explains why temperature affects rate; the practical judgement asks whether that effect has been isolated from the intended comparison.''')
add('4-07',[
 'The most significant error is judged by its likely effect on the requested result, not by naming generic human error.',
 'An error explanation identifies a mechanism, direction where justified and relative importance.'
], 'Find the error that matters most', '''Start with the measured result and trace what could bias it. In an uninsulated calorimetry experiment, heat transferred to the surroundings lowers the observed temperature rise, so a calculation attributing all reaction heat to the solution underestimates the magnitude of an exothermic enthalpy. In gas collection, a leak can reduce measured volume. These are specific mechanisms with a plausible direction.

Compare the likely size of competing effects. If temperature rise is 4.0°C and uncertainty in the rise is 1.0°C, that contribution is much larger proportionally than a 0.01 g uncertainty in a 50.00 g mass. Focus an improvement on the larger contribution while recognising that heat loss may add a separate systematic effect.

“Human error” does not explain how a result changes. A variable delay in starting a timer, a consistent parallax direction and an overrun endpoint are different errors and need different remedies. Avoid claiming a direction where the method does not establish one: variable judging of a disappearing cross can scatter readings either side. Support significance with data, apparatus resolution or a clear description of material lost or energy transferred.''')
add('4-08',[
 'Absolute uncertainty has the measured quantity unit; percentage uncertainty is absolute uncertainty divided by magnitude times100.',
 'For a difference of two readings, a simple maximum uncertainty estimate adds their absolute reading uncertainties.'
], 'Quantify uncertainty explicitly', '''State the uncertainty model used. If each burette reading has an assumed uncertainty of ±0.05 cm³, a delivered volume obtained from two readings has a simple maximum uncertainty ±0.10 cm³. For a 25.00 cm³ titre, the percentage is 0.10/25.00×100=0.400 percent. This is a conservative reading-uncertainty estimate, not a measurement of actual experimental error against a known truth.

For thermometer readings each uncertain by ±0.5°C, a temperature difference has a simple maximum uncertainty ±1.0°C. A measured rise 6.5°C therefore has about 15 percent uncertainty by this model. A rise 2.0°C would have a much larger 50 percent for the same instrument. Increasing the measured change within a valid experiment can reduce the relative contribution.

Do not invent apparatus uncertainty from the number of written decimal places when a calibration or supplied value is available. Use the stated instrument information. Separate random spread, calibration uncertainty and systematic heat transfer where relevant; one percentage does not automatically include all of them. Topic 1.1 supplies the arithmetic of ratios, while this practical skill requires deciding what uncertainty belongs in the numerator.''')
add('4-09',[
 'Random errors cause unpredictable scatter, whereas systematic errors shift results consistently through a bias.',
 'A constant additive thermometer offset can cancel in a temperature difference when both readings use that same stable offset.'
], 'Distinguish scatter from bias', '''Random errors vary unpredictably between repeats and can make values fall above or below the underlying result. Repeating and averaging comparable readings can reduce their effect on the mean. Systematic errors arise from a consistent bias, such as a calibration offset or a method that persistently loses heat before it is measured. Repeating the same biased method does not remove that bias.

Consider a thermometer that reads 1.0°C too high at both temperatures. True readings 22.0 and 28.0°C become 23.0 and 29.0°C, but the difference remains 6.0°C. The constant additive offset cancels in that difference. It still makes an individual absolute temperature wrong, and a changing or scale-factor error would not necessarily cancel.

A burette zero reading is also not itself a problem if both initial and final readings are taken correctly and subtracted. By contrast, a bubble changing during delivery can alter the relation between scale difference and liquid reaching the flask. Analyse the measured difference rather than assuming any offset must change it. An evaluation identifies both the kind of error and how the specific calculation responds.''')
add('4-10',[
 'A conclusion is limited to what the measured evidence and its uncertainty support.',
 'Chemical identity or causation requires the stated candidate context and relevant comparison, not a single ambiguous observation.'
], 'Draw a conclusion with its evidence', '''State the answer to the investigation's question, then cite the observation or calculation that supports it. An exothermic conclusion can cite a measured positive temperature rise after accounting for the baseline. A concentration conclusion gives its numerical value and unit from the selected titre and balanced reaction. A qualitative conclusion identifies the candidate pattern used.

If the supplied choices are Al3+ and Zn2+, a precipitate remaining in excess ammonia can separate them after the shared NaOH behaviour. Without those choices and reference information, the same brief observation may not identify a unique ion. Keep the conclusion tied to the evidence actually available.

Express uncertainty or ambiguity where it affects the outcome. Two concentrations differing by less than their combined plausible measurement spread may not support a claimed change. A poorly controlled temperature comparison does not establish concentration as the sole cause of faster reaction. The conclusion should not introduce observations that were never recorded or extend automatically to untested materials. The six integrated tasks below require a conclusion after the working so that the numerical and observational chain remains visible.''')
add('4-11',[
 'A hypothesis is supported when the data agree with its predicted pattern within relevant uncertainty, but finite data do not prove it universally.',
 'A prediction should identify whether it interpolates within tested settings or extrapolates beyond them.'
], 'Test a stated hypothesis rather than a vague expectation', '''Translate the hypothesis into a measurable prediction. “Reciprocal endpoint time is proportional to concentration” predicts a straight 1/time–concentration graph through the origin within uncertainty, when the same small endpoint and other relevant settings are matched. A straight line with a clearly nonzero intercept would not establish that exact proportionality, even if the response increases with concentration.

Compare the fit with scatter and control-variable evidence. Measurements near a straight trend support the model over the tested range; they do not demonstrate it for arbitrary concentrations, temperatures or reaction extents. Quote a relevant pair of values or the slope and intercept rather than simply writing “the hypothesis is correct”.

Use the supported model to make a stated prediction. With a fitted relationship 1/time=0.0500c, c=0.50 mol dm−3 gives 1/time=0.0250 s−1 and time=40.0 s. This is interpolation if the tested range spans 0.20–1.00 mol dm−3. At a much higher concentration, additional measurements would be needed before assuming the same relationship remains valid. Topic 2.4 explains why a controlled comparison matters for the kinetic inference.''')
add('4-12',[
 'An explanation connects a practical pattern to a chemical or physical mechanism and the setting in which it applies.',
 'Repeating a measured trend in words is description, not an explanation of why it occurs.'
], 'Connect evidence to a mechanism', '''After describing a result, explain it using an appropriate chemical or physical principle. A falling gas-production gradient can follow reactant consumption reducing the frequency of successful collisions. A temperature rise after neutralisation reflects energy released overall and transferred to the solution. A precipitate dissolving in excess reagent requires the relevant supplied chemistry, rather than an inference from colour alone.

For example, if two runs have the same limiting amount and final gas volume but one is initially faster at higher temperature, the result can be explained through a greater fraction of collisions exceeding the activation barrier. Do not say that a catalyst raises the temperature or changes the equilibrium yield merely because it speeds the reaction. Match the explanation to the variable actually changed.

Keep assumptions visible. A solution-temperature calculation usually assumes a density and heat capacity, and may neglect the vessel's heat capacity. Its numerical enthalpy therefore depends on that model as well as on the observations. Topic 2.1 supplies energy accounting and Topic 2.4 rate theory. In practical work these ideas explain why a particular pattern occurred and why a limitation can change the calculated result.''')
add('4-13',[
 'A useful improvement targets a specific error through an achievable change in apparatus, procedure or observation.',
 'Higher resolution does not repair unrelated loss, contamination or lack of control.'
], 'Make improvements that address the cause', '''Pair each improvement with the limitation it addresses. Insulation and a lid reduce heat transfer to the surroundings; checking gas joints reduces leakage; a thermostatic bath helps control reaction temperature. A longer, readable gradient triangle reduces the fractional effect of coordinate-reading uncertainty. These are practical changes with an identifiable connection to the result.

Repeating a timed run addresses random scatter, while checking calibration addresses a persistent scale bias. A more finely marked measuring device is useful when reading resolution is a significant contribution, but it does not recover gas that escaped through a leaking stopper. Likewise a digital thermometer alone does not remove heat absorbed by an unaccounted vessel.

Describe the change clearly enough that another student could implement it. “Be more accurate” gives no action. “Read the meniscus at eye level with a fixed white background” specifies an observational change. If an improvement introduces another effect, consider it: changing reactant volumes to increase a temperature rise can also change the limiting amount, so the amount calculation must be updated. State which quantity becomes more reliable and why the proposed change is realistic for the experiment.''')
add('4-14',[
 'An extension answers a specified new question, whereas an improvement strengthens the original measurement.',
 'A new-variable investigation still needs an appropriate range, controls, measurements and a comparison criterion.'
], 'Extend the investigation to answer a new question', '''Begin with the new question explicitly. If the original work studies concentration and rate, an extension might ask how temperature changes the same endpoint rate while concentration is held fixed. Choose several temperatures in a usable range, equilibrate mixtures in a bath, measure starting temperatures, repeat timed runs and keep the amount, total volume and endpoint unchanged.

That is different from repeating the original concentration experiment to reduce scatter. Repetition can improve evidence for the original question but does not by itself answer how temperature affects the response. Similarly, adding a lid to reduce heat loss is an improvement unless the new question is specifically about heat transfer under different insulation arrangements.

State the proposed independent variable, dependent measurement and controls. Explain what pattern would answer the question and how comparable data will be displayed. If investigating a different catalyst, keep its specified amount or exposed area comparable as appropriate and distinguish rate effects from final amount. Avoid extensions phrased merely as “try other chemicals”: different reactants can change stoichiometry and the phenomenon being compared. A useful extension is a small, testable investigation with a clear connection to the evidence already collected.''')

# All four units are practical AO C, rather than theory A/B defaults.
for blocks in t.blocks.values():
 for b in blocks:b['assessment_objectives']=['C'];stamp(b)
out=t.dir/'assets'
f=Figure('Read the observation sequence','Three labelled boxes linked by arrows: fresh portion of X, add reagent dropwise and record initial effect, add excess of the same reagent and record final effect.')
for x,lines in [(35,['Fresh portion','of sample X']),(300,['Add dropwise','Record initial effect']),(565,['Add excess','Record final effect'])]:
 f.line([(x,150),(x+230,150),(x+230,310),(x,310),(x,150)],width=2)
 for k,line in enumerate(lines):f.text(x+12,185+k*45,line,19)
f.arrow((270,230),(290,230));f.arrow((535,230),(555,230));f.text(40,395,'Use a new original-sample portion for a different reagent comparison.',19)
f.save('8224-practical-sequence',out=out)
f=Figure('Calibration graph for an unknown','Signal dimensionless versus concentration mol/dm3. Straight model S=20c+0.1 over0.01 to0.05; marked measured standards. Horizontal guide at signal0.70 crosses at concentration0.03. Read the unknown from the graph.')
f.text(30,70,'Signal (dimensionless)',18);f.arrow((100,355),(765,355));f.arrow((100,355),(100,105))
def calxy(c,s):return(100+12000*c,355-200*s)
f.line([calxy(.01,.3),calxy(.05,1.1)],width=3)
for c in [.01,.02,.03,.04,.05]:
 x,y=calxy(c,20*c+.1);f.circle(x,y,4);f.text(x-18,372,f'{c:.2f}',15);f.line([(x,355),(x,362)],width=1)
for s in [0,.2,.4,.6,.8,1.0,1.2]:
 x,y=calxy(0,s);f.text(48,y-10,f'{s:.1f}',15);f.line([(93,y),(100,y)],width=1)
f.line([calxy(0,.7),calxy(.03,.7)],'#a13922',2);f.text(110,188,'unknown signal 0.70',17,'#a13922')
f.text(460,410,'Concentration / mol dm^-3',18);f.save('8224-practical-calibration',out=out)
f=Figure('Reciprocal-time rate proxy','Original fixed-endpoint times for concentrations0.2,0.4,0.6,0.8,1.0 mol/dm3:100.0,50.0,33.3,25.0,20.0 seconds. Reciprocal-time points and straight model y=0.05x; both axes start at zero.')
f.text(28,70,'1/time / s^-1',19);f.arrow((100,355),(765,355));f.arrow((100,355),(100,105))
def xy(c,r):return(100+600*c,355-4400*r)
f.line([xy(0,0),xy(1,.05)],'#a13922',2)
for c,tm in [(.2,100),(.4,50),(.6,33.3),(.8,25),(1,20)]:
 x,y=xy(c,1/tm);f.circle(x,y,4);f.line([(x,355),(x,362)],width=1);f.text(x-10,370,str(c),16)
for r in [0,.01,.02,.03,.04,.05]:
 x,y=xy(0,r);f.line([(93,y),(100,y)],width=1);f.text(42,y-10,f'{r:.2f}',15)
f.text(475,410,'Concentration / mol dm^-3',18);f.save('8224-practical-linear-rate',out=out)
f=Figure('Gas-volume curve and tangent at40s','Original model V=60(1-exp(-t/40)). Tangent at40s has gradient0.5518 cm3/s; time range0 to100s, volume0 to65cm3. Curve not experimental data.')
f.text(28,70,'Gas volume / cm³',18);f.arrow((100,355),(765,355));f.arrow((100,355),(100,105))
def xy2(tm,v):return(100+6*tm,355-3.5*v)
f.line([xy2(tm,60*(1-math.exp(-tm/40))) for tm in range(101)],width=3)
f.line([xy2(0,60*(1-2/math.e)),xy2(80,60)],'#a13922',2);f.circle(*xy2(40,60*(1-1/math.e)),r=5)
for tm in [0,20,40,60,80,100]:
 x,y=xy2(tm,0);f.line([(x,355),(x,362)],width=1);f.text(x-8,370,str(tm),15)
for v in [0,10,20,30,40,50,60]:
 x,y=xy2(0,v);f.line([(93,y),(100,y)],width=1);f.text(60,y-9,str(v),15)
f.text(535,410,'Time / s',18);f.text(400,95,'Tangent at40s (red)',18,'#a13922');f.save('8224-practical-tangent',out=out)

qa=[
('Describe a titration setup before an initial burette reading.','Clamp burette vertically above flask/tile; rinse with intended solution and fill tip without bubbles; remove funnel and read meniscus at eye level.'),
('Suggest one check if a gas syringe records less gas than expected.','Check the joints and tubing for leaks before repeating the measurement.'),
('Describe the actions and observation points shown in this diagram.\n\n![Original instruction sequence](assets/8224-practical-sequence.png)','Take a fresh portion of X; follow the diagram arrow to add reagent dropwise and record the initial effect; then add excess of the same reagent and record whether the precipitate remains or dissolves.'),
('Suggest why a fresh portion is required for a second candidate-ion test.','It avoids attributing changes caused by earlier reagents to the new test.'),
('Describe three features to record when ammonia is added to a coloured precipitate test.','State precipitate formation and colour; record its change with excess ammonia; state the colour and clarity of any resulting solution.'),
('Suggest a useful observation beyond “bubbling occurred” when acid is added to a possible carbonate.','Record a suitable confirmation of CO2, such as the gas turning limewater milky under the specified method.'),
('Describe taking and recording a delivered burette volume.','Read the appropriate meniscus at eye level; record initial and final readings to0.05 cm³; subtract initial from final to obtain the titre.'),
('Suggest a suitable instrument for transferring a25.00 cm³ titration aliquot.','A calibrated25.00 cm³ volumetric pipette with a filler.'),
('Describe how to make repeated indicator endpoints consistent.','Use the same indicator amount and visual criterion; slow to dropwise addition near endpoint while swirling; use a white background and check persistence after mixing.'),
('Suggest why two close titres do not establish accuracy.','They can share a systematic reagent or calibration bias even when their scatter is small.'),
('Describe deciding how many ion tests to perform from supplied candidate notes.','Find a first test separating outcomes; preserve fresh material for a discriminating follow-up if needed; repeat an ambiguous observation rather than adding unrelated reagents to one tube.'),
('Suggest why repeating a shared white-precipitate test cannot alone distinguish Al3+ from Zn2+.','Both candidates can give that outcome; a different excess-solubility comparison is needed.'),
('Describe a suitable concentration range design for a rate investigation.','Use a pilot to choose measurable endpoints; use several distinct concentrations across the usable range; keep total volume and other reactants controlled and add repeats to assess scatter.'),
('Suggest where to add measurements if a thermometric graph has too few points near its maximum.','Add points around the expected maximum or intersection while retaining coverage on both sides.'),
('Describe choosing observation times in a thermal reaction.','Measure a stable pre-mixing baseline; sample frequently during the rise; continue into cooling so a transient maximum is not missed.'),
('Suggest why waiting several minutes for a stable final temperature can underestimate an exothermic rise.','Heat can leave the mixture before that reading, so the transient maximum has passed.'),
('Describe selecting repeats for a titre mean.','Exclude the rough run; find careful titres within0.10 cm³; mark the closest suitable pair and average them while retaining the other recorded trials.'),
('Suggest what to do with an unexpectedly high careful titre.','Retain and investigate it, then repeat the run to check for overshoot or another cause rather than silently deleting it.'),
('Describe confirming CO2 after effervescence in a specified carbonate test.','Collect or direct a suitable gas sample under the supervised method; pass it into limewater; record a milky appearance as confirmation supporting CO2.'),
('Suggest the supplied confirmatory test for ammonia evolved on warming with alkali.','Damp red litmus turns blue in the gas; record the observation under the instructed procedure.'),
('Describe selecting a reagent to distinguish Al3+ and Zn2+ using supplied notes.','Recognise both NaOH precipitates dissolve in excess; test fresh portions with aqueous ammonia; Al precipitate remains in excess whereas Zn precipitate dissolves.'),
('Suggest a follow-up for a white barium-nitrate precipitate when sulfate and sulfite are the candidates.','Apply the supplied nitric-acid follow-up: sulfate precipitate remains while sulfite precipitate dissolves.'),
('Describe a coherent raw-and-derived titration table.','Include trial identifiers/rough label; align initial and final readings with titres; put units in headings and mark the careful values selected for the mean.'),
('Calculate the two titres and their mean for trials with initial/final readings0.20/24.85 and0.10/24.80 cm³; retain the rows in a results table.','|Trial|Initial / cm³|Final / cm³|Titre / cm³|\n|---|---:|---:|---:|\n|1|0.20|24.85|24.65|\n|2|0.10|24.80|24.70|\nEquation/working: titre=final−initial; mean=(24.65+24.70)/2=24.675 cm³, about24.68 cm³ to two decimal places. The values differ by0.05 cm³ and are concordant; retain unrounded mean in later calculations.'),
('Describe preparing a gas-volume experiment table before the run.','Read the planned intervals; draw Time / s and Gas volume / cm³ headings; leave enough rows for the full range, repeats and any endpoint note.'),
('Calculate the missing titre in a prepared table row with initial reading1.10 cm³ and final25.75 cm³. Show the completed row headings.','|Initial reading / cm³|Final reading / cm³|Titre / cm³|\n|---:|---:|---:|\n|1.10|25.75|24.65|\nEquation/working:25.75−1.10=24.65 cm³. Answer retains0.01 cm³ decimal places; the raw readings follow0.05 cm³ increments.'),
('Describe separating raw, calculated and conclusion columns in a mass-loss experiment.','Keep initial/final masses as raw readings; calculate their difference in a labelled mass-loss column; record the chemical inference separately with its supporting method.'),
('Calculate and enter mass loss from raw masses52.64 and52.20 g in a table with separate raw and derived columns.','|Initial mass / g|Final mass / g|Mass loss / g|\n|---:|---:|---:|\n|52.64|52.20|0.44|\nEquation/working:52.64−52.20=0.44 g, answer to the raw hundredth-gram place. Gas escape is a separate inference, not a raw balance reading.'),
('Describe correct headings when time and reciprocal time are both tabulated.','Name Time / s and1/time / s−1 separately; define symbols if ambiguous; put reciprocal values under their reciprocal unit rather than under seconds.'),
('Calculate reciprocal times for100.0 and50.0 s and provide the derived column heading.','Equation:r=1/time. Working:1/100.0=0.01000 and1/50.0=0.0200; answer heading1/time / s−1. Values are0.01000 and0.0200 s−1 with significant figures reflecting each supplied time.'),
('Describe consistent raw reading and qualitative recording.','Use decimal places supported by the instrument throughout each raw column; preserve trailing zeros; give comparable colour, solid and excess-behaviour detail across samples.'),
('Calculate the mass difference from2.85 g and2.40 g on a0.01 g-resolution balance and state recording precision.','Equation: difference=final−initial. Working:2.85−2.40=0.45 g. Answer keeps the hundredth-gram place; raw2.40 must retain its trailing zero. Significant figures do not override raw scale resolution.'),
('Describe the calculation chain for unknown HCl concentration from a NaOH titre.','Convert titre cm³ to dm³; use n=cV and the balanced1:1 mole ratio; divide HCl amount by aliquot volume in dm³ and report justified precision.'),
('Calculate HCl concentration if25.00 cm³ acid is neutralised by24.675 cm³ of0.100 mol dm−3 NaOH.','Equation:HCl+NaOH→NaCl+H2O; n=cV. Working:Vbase=0.024675 dm³; n=0.100×0.024675=0.0024675 mol. Answer:cacid=0.0024675/0.02500=0.0987 mol dm−3 to three significant figures. Retain unrounded intermediate amount.'),
('Describe choosing significant figures for a calculated result.','Identify the least accurate measured input; retain guard digits through working; round the final result to matching precision or one extra significant figure where justified by the syllabus convention.'),
('Calculate a product mass from0.0500 mol and molar mass58.0 g mol−1, stating justified precision.','Equation:m=nM. Working:0.0500×58.0=2.90 g. Answer has three significant figures matching the inputs; quantities already use mol and g mol−1 so no conversion is required.'),
('Determine a suitable display for sample-by-sample precipitate colour and excess-solubility results.','A labelled qualitative results table, with separate initial and excess observations.'),
('Suggest a display that reveals how gas-production rate changes during one run.','Plot gas volume against time and retain the raw table; the curve gradient shows changing rate.'),
('Determine which quantity belongs on the vertical axis for gas volume plotted against time.','Gas volume / cm³; time / s is horizontal.'),
('Suggest a readable horizontal scale for times0–100 s across five equal major intervals.','20 s per major interval, giving a0–100 s range.'),
('Determine the correct horizontal position of25 s on a scale with marked20 and30 s.','Halfway between20 and30 s.'),
('Suggest how to retain a genuinely anomalous plotted value while excluding it from a fit.','Ring or label the point and explain its exclusion; keep the original table reading.'),
('Determine whether a straight line or a smooth curve fits a gas-volume response whose gradient steadily declines.','A smooth curve showing the declining gradient.'),
('Suggest why joining noisy successive points with sharp corners can misrepresent a smooth reaction trend.','The corners can turn random scatter into artificial changes in the underlying rate.'),
('Determine a suitable vertical variable to test proportional endpoint-rate behaviour when each run reaches the same small endpoint.','1/time / s−1, a fixed-endpoint rate proxy, plotted against concentration.'),
('Suggest the key endpoint requirement for comparing rates using1/time.','Each run must reach the same defined extent or endpoint under matched other settings.'),
('Determine the meaning of the intercept4 cm³ in V=0.400t+4 with t in s.','The model predicts a volume4 cm³ at zero time; its physical cause depends on the experimental baseline.'),
('Suggest how to reduce coordinate-reading influence when calculating a straight-line gradient.','Use two well-separated coordinates on the fitted line and a large gradient triangle.'),
('Determine whether the tangent or a whole-run secant gives the local rate at40 s on a curved volume–time graph.','The tangent gradient at40 s.'),
('Suggest the physical meaning of area under a volume-production-rate versus time graph.','Accumulated produced volume over the interval, because(cm³ s−1)×s gives cm³.'),
('Determine the rate trend shown by the gas-volume graph over0–40 s and40–80 s, using supporting volumes.\n\n![Original volume-time graph](assets/8224-practical-tangent.png)','The graph rises from0 to about37.9 cm³ by40 s and then to about51.9 cm³ by80 s. Smaller gain in the second equal interval supports a declining average rate.'),
('Suggest two numerical features that distinguish faster reaction from greater final gas amount.','Compare an early gradient for rate and the plateau volume for final amount; they describe different features.'),
('Determine the useful distinguishing observation if both candidates form white NaOH precipitates soluble in excess but only one dissolves in excess ammonia.','The excess-ammonia solubility difference, recorded on fresh portions.'),
('Suggest how to improve a summary recorded merely as “tubeA white, tubeB clear”.','State whetherA contained a precipitate and whetherB was a colourless solution, then add each change with excess reagent.'),
('Determine the unknown concentration by reading the calibration graph at its indicated signal0.70.\n\n![Original calibration graph](assets/8224-practical-calibration.png)','The horizontal signal0.70 guide meets the fitted line at concentration about0.030 mol dm−3. Read the corresponding x-coordinate; this is interpolation within the measured range.'),
('Suggest how to check an unknown estimate lying beyond the measured calibration range.','Measure additional suitable standards nearer the unknown; compare their fit before relying on extrapolation.'),
('Determine which titres to average from a rough25.30 cm³ and careful24.65,24.70,25.10 cm³ runs.','The careful24.65 and24.70 cm³ pair; exclude rough and investigate25.10.'),
('Suggest why a mean without individual repeats can hide a problem.','Averages can conceal large scatter or an anomalous run, so preserve the component values and selection reason.'),
('Determine the sign of the gradient on a measured mass–time graph that decreases with time.','Negative; its magnitude can represent mass-loss rate if that convention is stated.'),
('Suggest why very close tangent coordinates give a less reliable gradient.','Their small differences make coordinate-reading uncertainty a larger fraction of the slope calculation; choose a larger triangle.'),
('Determine whether temperature is controlled if starting values rise20.0,22.0,25.0°C as concentration increases.','No; temperature changes systematically with concentration and can affect the measured rate.'),
('Suggest a temperature control and a check for a concentration-rate experiment.','Equilibrate mixtures in a thermostatic bath and record starting liquid temperatures to verify comparability.'),
('Determine the likely direction of heat-loss error on an exothermic enthalpy magnitude calculated from solution warming alone.','It lowers the observed rise and underestimates the exothermic magnitude.'),
('Suggest an improvement targeting an observed gas leak rather than scale resolution.','Reseal/check the joints and tubing before repeating; a finer scale would not recover escaped gas.'),
('Determine the simple maximum uncertainty in a titre obtained from two burette readings each ±0.05 cm³.','±0.10 cm³, adding the two absolute reading uncertainties.'),
('Suggest why measuring a larger temperature rise can reduce percentage reading uncertainty when each temperature has unchanged uncertainty.','The absolute uncertainty in the difference stays similar while the measured rise increases, reducing the uncertainty-to-rise ratio; keep the changed reaction amount accounted for.'),
('Determine the error type if repeated readings scatter unpredictably above and below a central value.','Random error.'),
('Suggest why repeating a calorimetry run without changing a persistent heat-loss mechanism cannot remove its bias.','The same systematic loss remains in each repeat; insulation or a suitable correction addresses the cause.'),
('Determine the supported ion among Al3+ and Zn2+ if a white precipitate dissolves in excess NaOH but remains in excess ammonia.','Al3+, from the supplied candidate outcomes.'),
('Suggest how to qualify a conclusion from two results whose difference is smaller than their plausible uncertainty.','State that the data do not clearly resolve a difference and obtain more precise evidence before claiming a change.'),
('Determine whether a rising1/time–concentration line with a clearly nonzero intercept establishes direct proportionality.','No; exact proportionality requires an intercept consistent with zero within the relevant uncertainty.'),
('Suggest how to test a prediction at a concentration outside the original measured range.','Run controlled repeats at new suitable concentrations and compare the resulting endpoint rates with the extrapolated model.'),
('Determine an explanation for a declining gas-volume gradient as a reacting solution is consumed.','Reactant depletion can reduce successful collision frequency and hence rate, under the stated reaction setting.'),
('Suggest why an observed temperature rise does not by itself give an exact reaction enthalpy.','The calculation also needs amount, heat capacity/mass assumptions and consideration of heat transferred to the vessel/surroundings.'),
('Determine the targeted improvement for variable manual delay at a timed endpoint: a bath or automated timing trigger.','An appropriate automated timing/endpoint trigger targets that delay; a bath addresses temperature instead.'),
('Suggest a specific calorimetry improvement and explain the error it reduces.','Use an insulated vessel with a lid to reduce heat exchange with surroundings, improving the measured temperature rise.'),
('Determine which is an extension to a concentration-rate study: repeating the same run or investigating temperature at fixed concentration.','Investigating temperature at fixed concentration answers a new question and is an extension.'),
('Suggest a controlled extension asking whether solid particle size changes rate.','Use equal masses of the same solid in defined size fractions with fixed solution concentration/volume/temperature; measure the same endpoint and repeat each fraction to compare rate.')
]
assert len(qa)==78,len(qa)
for s,(q,a) in zip(t.wo['item_slots'],qa):t.item(s,q,a)

# The six performance tasks exercise data production/design and interpretation together.
t.item(t.wo['performance_tasks'][0],'''Determine unknown HCl concentration by the following original titration exercise. Work in a supervised laboratory or analyse the supplied simulated readings. Pipette25.00 cm³ acid; use0.100 mol dm−3 NaOH and a suitable supplied indicator. Near endpoint add dropwise, swirl and judge the instructed persistent change.
Rough initial/final0.00/25.30 cm³; careful runs0.20/24.85,0.10/24.80,0.00/25.10 cm³.
(a) Describe apparatus preparation and endpoint timing. [4]
(b) Construct the results table before entering all raw readings and titres, with headings/precision. [5]
(c) Select concordant values and calculate the mean. [3]
(d) Write the reaction and calculate acid concentration. [4]
(e) Give the conclusion, a specific error and an improvement; explain the role of repeats. [4]''',
'''(a) Apparatus and method: vertical rinsed burette [1], filled bubble-free tip/funnel removed [1], measured pipette aliquot [1], dropwise/swirl/persistence near endpoint [1].
(b) Observations/data table: draw before taking readings with labelled trial/initial/final/titre spaces [1]; quantity/unit headings [1]; two-decimal raw readings [1]; correct retained raw rows [1]; titres25.30,24.65,24.70,25.10 cm³ [1].
|Trial|Initial / cm³|Final / cm³|Titre / cm³|
|---|---:|---:|---:|
|Rough|0.00|25.30|25.30|
|1|0.20|24.85|24.65|
|2|0.10|24.80|24.70|
|3|0.00|25.10|25.10|
(c) Select runs1/2 [1], difference0.05 cm³ within0.10 [1], mean24.675 cm³ retained internally [1].
(d) HCl+NaOH→NaCl+H2O [1]; Vbase=0.024675 dm³ [1]; nbase=nacid=0.0024675 mol [1]; cacid=0.0024675/0.02500=0.0987 mol dm−3 to3 significant figures [1].
(e) Conclusion0.0987 mol dm−3 for the stated acid [1]; overshooting endpoint inflates base titre [1]; slower dropwise delivery near endpoint reduces it [1]; repeats reveal scatter and allow the concordant selection but do not erase systematic bias [1]. Total20 marks.''')
t.item(t.wo['performance_tasks'][1],'''Determine Fe2+ concentration in25.00 cm³ aliquots using0.0200 mol dm−3 manganate(VII) under the supplied dilute sulfuric-acid conditions. Supplied reaction: MnO4−+5Fe2++8H+→Mn2++5Fe3++4H2O. Endpoint is the first faint pink remaining for30 s after swirling; no added indicator is required.
Simulated initial/final readings in cm³: rough0.00/20.20; careful0.10/20.00,0.20/20.15,0.00/20.40.
(a) Describe preparation and endpoint judgement. [4]
(b) Prepare a table and record all readings/titres. [4]
(c) Select concordant values and calculate their mean. [3]
(d) Calculate manganate and Fe2+ amounts, then concentration, showing conversions and precision. [5]
(e) Give a conclusion, one specific error, its remedy and the value of repeats. [4]''',
'''(a) Apparatus/method: rinsed vertical burette with filled tip [1], pipette25.00 cm³ Fe2+ [1], use specified dilute sulfuric-acid conditions [1], dropwise near endpoint with faint pink persistent30 s after swirling [1].
(b) Table prepared with trial/initial/final/titre fields [1]; quantity/unit headings [1]; retain two-decimal raw readings [1]; titres20.20,19.90,19.95,20.40 cm³ [1].
|Trial|Initial / cm³|Final / cm³|Titre / cm³|
|---|---:|---:|---:|
|Rough|0.00|20.20|20.20|
|1|0.10|20.00|19.90|
|2|0.20|20.15|19.95|
|3|0.00|20.40|20.40|
(c) Runs1/2 [1],0.05 cm³ difference concordant [1], mean19.925 cm³ [1].
(d) V=0.019925 dm³ [1]; n(MnO4−)=0.0200×0.019925=0.0003985 mol [1]; Fe2+:MnO4−=5:1 [1]; n(Fe2+)=0.0019925 mol [1]; c=0.0019925/0.02500=0.0797 mol dm−3,3 significant figures [1].
(e) Conclusion Fe2+ concentration0.0797 mol dm−3 [1]; intense pink overshoot overstates titre [1]; slow dropwise addition and persistence check reduce it [1]; repeats identify scatter/anomalous overshoot without proving accuracy [1]. Total20 marks.''')
t.item(t.wo['performance_tasks'][2],'''Determine the approximate molar enthalpy of neutralisation from simulated data. Mix50.0 cm³ of1.00 mol dm−3 HCl with50.0 cm³ of1.00 mol dm−3 NaOH in an insulated cup. Both start23.0°C; record every30 s. Temperature at time relative to mixing−60,−30,0,30,60,90,120 s is23.0,23.0,23.0,29.5,29.0,28.5,28.0°C. Use the observed maximum for this exercise. Assume density1.00 g cm−3, specific heat capacity4.18 J g−1°C−1 and neglect the cup heat capacity. Each temperature reading uncertainty is±0.5°C.
(a) Describe apparatus and timed observations. [3]
(b) Construct a raw table, with derived rise and interpretation separate. [4]
(c) Calculate heat gained and molar enthalpy. [6]
(d) Give the conclusion and molecular/energy explanation. [3]
(e) Calculate simple maximum rise uncertainty and percentage; name a limitation and targeted improvement. [4]''',
'''(a) Apparatus/method: insulated cup with immersed thermometer [1], measure equal volumes and starting temperatures [1], mix/stir consistently and record frequent timed values through peak/cooling [1].
(b) Time / s and Temperature / °C headings [1]; all seven raw pairs with0.5°C-compatible precision [1]; derived ΔT=29.5−23.0=6.5°C [1]; keep exothermic inference separate from raw values [1].
|Time / s|Temperature / °C|
|---:|---:|
|−60|23.0|
|−30|23.0|
|0|23.0|
|30|29.5|
|60|29.0|
|90|28.5|
|120|28.0|
(c) Working: mass=100.0 cm³×1.00=100 g [1]; q=mcΔT [1]; q=100×4.18×6.5=2717 J [1]; nwater=1.00×0.0500=0.0500 mol,1:1 limiting amounts [1]; ΔH=−q/n with J→kJ [1]; −2.717/0.0500=−54.34 kJ mol−1, appropriately about−54 kJ mol−1 from the2-significant-figure rise [1].
(d) Conclusion exothermic neutralisation [1], supported by6.5°C rise [1]; chemical energy release heats solution, with reaction heat opposite in sign to solution heat gain [1].
(e) Maximum absolute rise uncertainty±1.0°C [1]; percentage1.0/6.5×100≈15 percent [1]; heat lost before/after peak can lower observed rise [1]; lid/improved insulation and faster logging reduce loss or missed peak respectively [1]. Total20 marks.''')
t.item(t.wo['performance_tasks'][3],'''Determine whether a fixed-endpoint rate proxy is proportional to concentration. Keep temperature, total volume and other reagent amounts fixed. A supplied endpoint corresponds to the same small reaction extent. Original data: concentrations0.20,0.40,0.60,0.80,1.00 mol dm−3; endpoint times100.0,50.0,33.3,25.0,20.0 s.
(a) Describe apparatus/method controls and endpoint timing. [3]
(b) Prepare raw and derived table headings and calculate1/time. [4]
(c) Plot1/time against concentration with labelled axes and a suitable fit. [4]
(d) Calculate and interpret gradient/intercept, then predict time at0.50 mol dm−3. [4]
(e) Give the conclusion and its limits. [2]
(f) For±0.5 s timing uncertainty at20.0 s, calculate percentage uncertainty and suggest an error-specific improvement and repeat strategy. [3]''',
'''(a) Apparatus/method: measure solution volumes [1], match total volume/other reagent amounts and temperature [1], use the same start and endpoint criterion [1].
(b) Concentration / mol dm−3 and Time / s raw headings [1]; derived1/time / s−1 heading [1]; working reciprocals0.01000,0.02000,0.03003,0.04000,0.05000 s−1 [2].
|Concentration / mol dm−3|Time / s|1/time / s−1|
|---:|---:|---:|
|0.20|100.0|0.01000|
|0.40|50.0|0.02000|
|0.60|33.3|0.03003|
|0.80|25.0|0.04000|
|1.00|20.0|0.05000|
(c) Appropriate variables/units [1], useful regular scales [1], accurate points [1], straight fit approximately through zero [1]. Example generated figure: assets/8224-practical-linear-rate.png.
(d) Wide triangle gives gradient≈(0.0500−0.0100)/(1.00−0.20)=0.0500 s−1 per mol dm−3 [1]; gradient is rate-proxy increase per concentration increment [1]; intercept≈0 is compatible with proportionality [1]; at0.50,1/time≈0.0250 s−1 so time≈40 s, precision reflecting graph/data [1].
(e) Conclusion supports proportionality over the measured range [1];1/time is a fixed-endpoint proxy, not an independently measured initial molar rate or proof outside the range [1].
(f)0.5/20.0×100=2.5 percent [1]; automated start/endpoint sensing can reduce manual timing delay [1]; repeat each setting to assess random scatter [1]. Total20 marks.''')
t.item(t.wo['performance_tasks'][4],'''Determine candidates from an original qualitative exercise using these supplied reference notes. Al3+ and Zn2+ both give white precipitates soluble in excess NaOH; with ammonia Al precipitate remains in excess and Zn precipitate dissolves. Carbonate plus dilute acid gives CO2, confirmed by limewater turning milky. Sulfate gives a white precipitate with barium nitrate that remains after nitric acid; sulfite precipitate dissolves after that acid. Use clean fresh portions and only the specified tests.
Simulated observations: X and Y each give a white precipitate soluble in excess NaOH. X gives a white ammonia precipitate that remains in excess; Y gives one that dissolves to a colourless solution. Anion sampleP effervesces with dilute acid; its gas makes limewater milky. Q gives a white barium-nitrate precipitate remaining after nitric acid. Q has twice the sample volume of P.
(a) Choose tests/fresh portions and explain any repeated observation needed. [4]
(b) Construct a precise observation-and-deduction table forX,Y,P,Q. [6]
(c) Identify candidates, explaining discrimination and gas confirmation. [5]
(d) Summarise the pattern and explain why precipitate quantity cannot be compared across unequal sample volumes. [2]
(e) Give one possible observational error, targeted improvement and justified confirmatory repeat. [3]''',
'''(a) Apparatus/method: separate clean labelled portions [1]; NaOH dropwise then excess [1]; fresh-portion ammonia initial/excess [1]; repeat any faint or inconsistent result with clean fresh sample rather than mixing tests [1].
(b) Table with sample/test/observation/deduction [1]; X white then soluble NaOH, insoluble excess-ammonia solid [1]; Y white then soluble with both excess reagents and colourless final solution [1]; P effervescence [1], limewater milky [1]; Q white solid remains after acid [1].
(c) Working/reasoning: X=Al3+ [1], Y=Zn2+ [1]; excess-ammonia difference separates candidates after shared NaOH outcome [1]; P carbonate with confirmed CO2 [1]; Q sulfate from acid-insoluble barium precipitate [1].
(d) Conclusion pattern: X/Y differ in excess ammonia and P/Q have different anion tests [1]; Q/P volumes differ and different reactions occur, so visible quantity is not a controlled concentration comparison [1].
(e) Residual reagent contamination can create/mask a solid [1]; use clean separate tubes and controlled sample quantities [1]; repeat the discriminating ammonia result on fresh material if uncertain, retaining observations [1]. Total20 marks. These results are supplied simulation data, not a claim that a physical test was performed.''')
t.item(t.wo['performance_tasks'][5],'''Determine a plan to investigate how acid concentration affects gas-production rate from equal masses of one carbonate solid at25.0°C. Available: gas syringe, flask/tubing, balance resolving0.01 g, volumetric apparatus, water bath, thermometer and timer. Choose a range with measurable reactions. A pilot with0.50 g solid gives20.0 cm³ gas in40.0 s; assume timer uncertainty±0.5 s per elapsed-time reading. The new extension question is whether particle size affects rate at fixed acid concentration.
(a) Describe stable apparatus, initial checks and measurements. [4]
(b) Plan the independent variable, measurement range and four effective controls with verification. [6]
(c) Prepare results-table headings and a repeat/graph strategy. [3]
(d) Calculate pilot average gas-production rate and percentage timing uncertainty. [3]
(e) Give a likely systematic limitation and targeted improvement, distinguishing it from random timing scatter. [2]
(f) Give the specified particle-size extension with a controlled comparison. [2]''',
'''(a) Apparatus/method: supported gas syringe and airtight flask/tubing [1]; check leaks and free plunger/capacity [1]; weigh solid on balance [1]; measure acid/dilution volumes and coordinate mixing with timer [1].
(b) Acid concentration independent [1]; several distinct pilot-informed settings with usable endpoint times [1]; bath/measure liquid starts at25.0°C [1]; same solid mass and composition [1]; same size fraction for original investigation [1]; same total liquid volume and mixing/start/endpoint, with acid in appropriate excess for the intended rate comparison [1].
(c) Table concentration/time/gas volume with units [1]; repeat each setting and retain scatter [1]; plot volume–time curves for initial gradients or use a justified fixed-extent timing proxy, matching method across runs [1].
(d) Working: average rate=20.0/40.0=0.500 cm³ s−1,3 significant figures [1]; timing ratio0.5/40.0 [1], times100=1.25 percent, about1.3 percent [1].
(e) A gas leak systematically lowers measured collection [1]; reseal/check apparatus, while repeats assess random timing scatter and cannot restore escaped gas [1].
(f) New question: use defined particle-size fractions of the same carbonate at fixed concentration [1]; keep mass, acid volume, temperature and measurement criterion matched, repeat and compare rates [1]. Conclusion is a testable plan, not an invented experimental outcome. Total20 marks.''')
t.deviations.append({'from':'Seven generic CALC slots mapped to table-recording objectives','to':'Calculations explicitly produce correctly headed completed table entries or a justified precision decision','why':'Arithmetic alone would not practise recording; each answer preserves its mapped table/working requirement rather than changing the frozen count or AO.'})
t.deviations.append({'from':'Generic theory block AO defaults','to':'All practical blocks carry AO C','why':'The qualification assesses this integrated resource through experimental skills; all frozen practical item labels remain AO C.'})
t.deviations.append({'from':'Experimental tasks potentially read as completed laboratory performance','to':'Explicit supplied simulated data plus supervised performance/design instructions','why':'The resource can be used offline but does not claim the agent physically performed the experiments. Method, recording and evaluation are practised together.'})
t.save()
