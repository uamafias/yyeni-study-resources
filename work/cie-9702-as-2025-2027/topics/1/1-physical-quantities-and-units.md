# 1 Physical quantities and units

*cie-9702-as-2025-2027. Offline study notes, rendered from the approved content units on 2026-09-29. Everything here is also what the flashcards are built from.*

**What this topic asks of you**

- Every physical quantity as a numerical magnitude together with its unit, and how to make and check reasonable estimates of the quantities this syllabus asks you to judge.
- The SI base quantities and their units, derived units built from base units, the homogeneity test applied to physical equations, and the prefixes from pico to tera.
- Systematic and random errors in measurements, the distinction between precision and accuracy, and how uncertainties combine in a derived quantity.
- The difference between scalar and vector quantities, adding and subtracting coplanar vectors, and resolving a vector into two perpendicular components.

---

## Physical quantities

### A quantity is a magnitude with a unit

A physical quantity is a property that can be measured, and every value of it has two parts: a numerical magnitude and a unit. The unit names the standard the magnitude is counted against. A farmer who says a fence wire runs for 200 m has said how many metres were used, and the metre is the standard counted against; the number and the unit together state the length. The same magnitude with a different unit states a different value: 200 m and 200 cm are very different lengths, because the unit is part of the value. A magnitude written without its unit is incomplete — "the wire runs for 200" states a number and no quantity. This is why every value you write in physics carries its unit, and why a unit symbol is part of the value rather than a decoration: change the unit and you have changed the quantity stated. Speeds show the same point in everyday dress. A minibus taxi doing 25 m s⁻¹ on the B1 is doing 90 km h⁻¹, and the two statements describe one speed because the units convert into each other; the number changed because the unit changed, and the value did not.

### Reasonable estimates

Many judgements in physics are made without an instrument. A reasonable estimate states a magnitude with its unit, judged without measuring directly, and it is expected to lie within about a power of ten of the actual value. Estimates are anchored on reference quantities you already know. Useful references include: an adult person has a mass of about 70 kg; a car on a main road travels at about 25 m s⁻¹; a door in a house is about 2.0 m tall; a phone has a mass of about 0.15 kg; a cup holds about 0.25 kg of water. References build on one another. A loaded minibus taxi carries about twenty passengers, and twenty adults at about 70 kg each come to 20 × 70 = 1400 kg, about 1.4 × 10³ kg, so the loaded taxi has a mass of around 3 × 10³ kg once the vehicle itself is counted. A reasonable estimate is judged, not guessed: it starts from a quantity you know and moves by a factor you can defend.

### Worked example: testing an estimate

In a practical report, Sipho writes that the tower of a wind pump on a farm near Outjo is 300 m tall. Test the estimate against a reference of the same kind. A two-storey house is about 6 m tall; a wind pump tower stands about three houses high, which suggests about 20 m; a large electricity pylon is about 50 m tall, and the tower is plainly shorter than one. The stated 300 m sits more than a power of ten above these references, so the estimate is not reasonable. A value judged without measuring is checked by comparison with a known quantity of the same kind, and this one fails the comparison. A reasonable estimate for the tower would be 10 m to 20 m — a magnitude, a unit, and a defence.

### Where this leads

Quantities, units and estimates run through the whole subject. Topic 2 measures displacement, velocity and acceleration in metres and seconds; topic 3 adds force and weight in newtons; topic 9 adds charge and current. Topic 12 depends on this sub-topic directly: every practical result is written as a magnitude with a unit, and every uncertainty is judged against the size of the value measured. An answer with a missing unit is an answer with a missing part.

---

## SI units (base and derived)

### The SI base quantities and units

The SI builds every quantity from a small set of base quantities. This syllabus names five for recall — mass, length, time, electric current and temperature — and amount of substance completes the AS set.

| base quantity | unit name | unit symbol |
|---|---|---|
| mass | kilogram | kg |
| length | metre | m |
| time | second | s |
| electric current | ampere | A |
| temperature | kelvin | K |
| amount of substance | mole | mol |

A base quantity is one of the quantities the others are built from, and a base unit is its unit. The kilogram is the unit of the base quantity mass: it is a unit, not a quantity. Charge, force, energy and speed are derived quantities — each is built from base quantities through its defining equation, which is why none of them appears in the table. The table is worth memorising with its two columns named: the left column holds quantities, the right column holds the units those quantities are measured in.

### Quantities are not units

A common slip when base quantities are asked for is to answer with units — kg, m, s, A, K — or with a derived quantity such as charge. Both miss the question. The test is whether each item in the answer is a quantity or a unit: mass is a quantity, the kilogram is its unit, and charge is a derived quantity built from current and time, not a base one. Keeping the two columns of the table apart — what is measured, and what it is measured in — removes the whole error.

### Derived units

A derived unit is written as a product or a quotient of SI base units, and the unit follows from the defining equation. Force comes from F = ma, so the newton is N = kg m s⁻². Pressure comes from p = F/A, so the pascal is Pa = N/m², and in base units kg m⁻¹ s⁻². Energy and work come from W = Fd, so the joule is J = N m = kg m² s⁻². Power comes from P = W/t, so the watt is J s⁻¹ = kg m² s⁻³. Read each derived unit straight off its equation: write the equation in symbols, replace each quantity by its unit, and simplify the powers. The same procedure produces any derived unit in this syllabus, however unfamiliar the quantity first looks.

### Base units only

When a unit is asked for in base units, the answer must contain base units and nothing else. Leaving a unit such as N, Pa or J in the answer leaves the conversion unfinished, because those symbols are themselves derived. The test is whether the final unit contains base units only: kg, m, s, A, K and mol. J = kg m² s⁻² passes; "J" alone does not, and neither does "N m", which is a derived unit wearing another name.

### Homogeneity

An equation is homogeneous when every term in it carries the same SI base units. A physical equation compares like with like, so the two sides must be equatable and the terms must be addable. To test an equation, write each symbol in base units and compare both sides. In v² = u² + 2as, the terms v² and u² carry (m s⁻¹)², which is m² s⁻², and the term 2as carries m s⁻² × m, which is also m² s⁻²; the three terms agree, so the equation is homogeneous. The 2 carries no units, because a pure number has none.

### Worked example: testing an equation

Test the equation P = Fv, where P is power, F is force and v is speed. The left side, power, has the watt: W = J s⁻¹, and J = kg m² s⁻², so the left side is kg m² s⁻³. The right side multiplies force by speed: kg m s⁻² × m s⁻¹ = kg m² s⁻³. Both sides carry kg m² s⁻³, so the equation is homogeneous.

Homogeneity is necessary, not sufficient. The equation F = 2ma is also homogeneous — the 2 is a pure number and carries no units — yet it is wrong. A units check can reject an equation whose sides disagree; it cannot confirm one whose sides agree, because a wrong constant hides inside matching units.

### Prefixes

Prefixes attach to unit symbols to state decimal multiples and submultiples, of base units and derived units alike.

| prefix | symbol | factor |
|---|---|---|
| pico | p | 10⁻¹² |
| nano | n | 10⁻⁹ |
| micro | µ | 10⁻⁶ |
| milli | m | 10⁻³ |
| centi | c | 10⁻² |
| deci | d | 10⁻¹ |
| kilo | k | 10³ |
| mega | M | 10⁶ |
| giga | G | 10⁹ |
| tera | T | 10¹² |

The symbol attaches directly to the unit symbol: mA, µs, GHz, mm. Note the case: mega is a capital M while milli is a lower-case m, and a slip between the two moves a value by nine powers of ten. A prefix is part of the unit, so it converts with the unit: a millimetre is 10⁻³ m, and a square millimetre is (10⁻³ m)², which is 10⁻⁶ m².

### Worked example: converting prefixes

Values are converted to base units before anything is substituted. A charger delivering 250 mA: milli is 10⁻³, so 250 mA = 250 × 10⁻³ A = 0.250 A. A radio frequency of 2.0 GHz: giga is 10⁹, so 2.0 GHz = 2.0 × 10⁹ Hz. An area of 4.0 mm²: the millimetre converts as 10⁻³ m and the square converts with it, so 4.0 mm² = 4.0 × 10⁻⁶ m². Writing each conversion as its own line, with the factor beside it, makes a slip visible at the point where it happens rather than in the final answer.

### Slipped powers of ten

The commonest prefix slip is a factor left unsquared. Converting 4.0 mm² with 10⁻³ gives 4.0 × 10⁻³ m², a thousand times too large, because the millimetre converted and the square did not. Areas carry the square and volumes the cube: mm² converts with 10⁻⁶ and mm³ with 10⁻⁹. The test is whether every value has been converted to base units before substituting — a check that catches this slip, and the mA, µs and GHz slips with it.

### Where this leads

Prefixes return in every topic: currents in milliamps in topic 9, wavelengths in nanometres in topic 7, masses in unified atomic mass units in topic 11. Homogeneity is the habit that checks each new equation in topics 2 to 11. Topic 12 leans on the prefixes when a calculated column is set up: converting every reading to base units first is what keeps the calculated values consistent.

---

## Errors and uncertainties

### Systematic errors and zero errors

A systematic error shifts every reading of the same measurement by the same amount, or in the same direction. The commonest kind is a zero error: the instrument reads a non-zero value before anything is measured. A micrometer that reads 0.02 mm with its jaws closed adds 0.02 mm to every diameter taken with it; a tape stretched at its end adds its own offset to every length. Because the shift is the same on every reading, a systematic error does not average away. It is corrected at its source: zero the instrument, or subtract the offset from every reading before the value is used.

### Random errors

A random error is an unpredictable scatter of readings about the mean value. Judging when a stopwatch is started, small vibrations, and reading a wobbling needle all scatter readings a little above and a little below the true value. Repeating and averaging reduces the effect of random error, because the scatter partly cancels — readings above the mean balance readings below it — and the mean of repeated readings is a better estimate of the true value than any single reading. The repeats should be genuine ones, taken afresh each time, and an odd reading far from the others is a sign to look for a cause rather than to average it away silently.

### Repeats do not cure a zero error

Some learners believe that repeating readings and averaging removes a zero error, or any other systematic error. It does not. Averaging reduces the effect of random error only. A systematic error pushes every reading in the same direction, so it survives any number of repeats: the mean of ten readings, each 0.02 mm too large, is still 0.02 mm too large. The test is whether the error pushes every reading in the same direction — if it does, the correction belongs at the instrument, not in the arithmetic of the repeats.

### Precision and accuracy

Accuracy is how close a measured value is to the true value. Precision is how close repeated readings are to each other; it is also the smallest division a reading is recorded to. The two are different properties of a set of readings. A set can be precise and inaccurate at once: the readings agree closely with each other while a systematic error shifts the whole set away from the true value. The test is whether the readings could agree closely and all be wrong — if they could, they are precise without being accurate. A single reading can be accurate without being precise: close to the true value, with no other readings to compare against it.

### Absolute and percentage uncertainty

Every measured value carries an uncertainty. The absolute uncertainty of a value is the range either side of it within which the true value is expected to lie, in the unit of the quantity. For one reading it is half the smallest division the instrument reads to; for repeated readings it is half the range of the repeats. The percentage uncertainty is the absolute uncertainty divided by the value itself, multiplied by 100. The same absolute uncertainty matters more on a small value: 0.5 s on a timing of 2 s is 25%, while 0.5 s on a timing of 200 s is 0.25% — which is why experiments time many swings rather than one. Uncertainty is not a failure of the measurement; it is an honest statement of how well the value is known.

### Combining uncertainties

Uncertainties combine by simple addition. When a derived quantity is found by adding or subtracting measured values, the absolute uncertainties add. When it is found by multiplying or dividing, the percentage uncertainties add. A quantity raised to the power n contributes n times its own percentage uncertainty: a squared diameter contributes twice its percentage uncertainty, a cubed one three times. The rule set is short — add absolutes for sums and differences, add percentages for products and quotients, multiply by the power — and it covers every derived quantity this syllabus asks you to assess.

### Worked example: uncertainty in an area

A learner measures a rectangular solar panel: length l = 1.00 m with absolute uncertainty 0.02 m, and width w = 0.500 m with absolute uncertainty 0.01 m. The percentage uncertainties: 0.02 ÷ 1.00 = 0.020, so 2.0%, and 0.01 ÷ 0.500 = 0.020, so 2.0%. The area is a product, A = l × w = 1.00 × 0.500 = 0.500 m², so the percentage uncertainties add: 2.0% + 2.0% = 4.0%. The absolute uncertainty in the area follows from the percentage: 0.040 × 0.500 = 0.020 m², so A = 0.500 ± 0.020 m². Had the area come from a squared length, the percentage uncertainty in that length would have counted twice.

### Where this leads

Topic 12 takes these ideas into the practical work: half the range of repeats as the absolute uncertainty, percentage uncertainties compared between two calculations of the same constant, and a stated criterion for whether data supports a relationship. The distinction between the two error kinds decides which readings repeats can rescue and which they cannot.

---

## Scalars and vectors

### Scalars and vectors

A scalar quantity has magnitude only. Mass, speed, distance, energy, work, power, pressure, charge, time and temperature are scalars. A vector quantity has magnitude and direction. Displacement, velocity, acceleration, force, weight and momentum are vectors. The test between the two is whether reversing the direction changes the quantity: reversing the direction of a force reverses the force, while a mass has no direction to reverse. Displacement is the distance moved in a stated direction from the starting point; the distance travelled says nothing about direction. Speed is the magnitude of velocity — a car's speedometer reads the same whichever way the car points.

### Scalars that look like vectors

Work, energy, power, pressure and charge are often called vectors, because vectors appear in their defining equations — work from a force moving through a distance, charge from a current flowing for a time. The appearance does not make the quantity a vector. The test is whether reversing the direction changes the quantity: a push reversed does negative work instead of positive work, and work is still fully described by its magnitude and its sign, not by a direction in space. Pressure and charge are the same: scalars, whatever their equations contain.

### Adding and subtracting coplanar vectors

Coplanar vectors lie in one plane, and two of them are added with a scale drawing or by trigonometry. By the triangle method, draw the first vector, then draw the second starting where the first ends; the resultant runs from the start of the first to the end of the second. The parallelogram method draws both vectors from one point and completes the parallelogram: the resultant is the diagonal from the shared point. To subtract a vector, add its reverse, because A − B = A + (−B), and the reverse of B has the same magnitude and the opposite direction.

### Resultant magnitudes

Two perpendicular vectors of magnitudes x and y give a resultant of magnitude √(x² + y²), at an angle θ to the first, where tan θ = y ÷ x. Two vectors of magnitudes P and Q at any other angle θ between them give a resultant from R² = P² + Q² + 2PQ cos θ, where θ is the angle between the two vectors. When the two vectors point the same way, θ = 0° and cos θ = 1, so the magnitudes simply add; when they point opposite ways, θ = 180° and cos θ = −1, so they subtract.

### Worked example: two ropes on a bakkie

A bakkie stuck in sand is pulled by two ropes in the same horizontal plane: one with 200 N due north, the other with 300 N at 60° to it. The angle between the pulls is 60°, so R² = P² + Q² + 2PQ cos θ = 200² + 300² + 2 × 200 × 300 × cos 60°. With cos 60° = 0.500, R² = 40000 + 90000 + 60000 = 190000, and R = 436 N to three significant figures. The direction of the resultant is found from its components, which the next section develops.

### Resolving into perpendicular components

A vector V at an angle θ to a reference direction is replaced, wherever that helps, by two perpendicular components: V cos θ along the reference direction and V sin θ perpendicular to it, where θ is the angle between the vector and the reference direction. Resolving is the reverse of adding perpendicular vectors: the two components recombine to give the original vector, because (V cos θ)² + (V sin θ)² = V². Which direction serves as the reference is your choice — along the ground, along a slope, along a string — and the components follow from the angle the vector makes with that chosen direction.

### Worked example: pulling a sledge

A sledge on a dry river bed is pulled by a rope at 40° to the ground, with a tension of 200 N. Along the ground, the component alongside the angle: 200 × cos 40° = 200 × 0.766 = 153.2 N, so 153 N to three significant figures. Perpendicular to the ground: 200 × sin 40° = 200 × 0.643 = 128.6 N, so 129 N. The component along the ground is the one that moves the sledge forward; the perpendicular component lifts a little, and reduces how hard the sledge presses on the ground.

### Sine and cosine swapped

When resolving, the common error is swapping sine and cosine. The component alongside the angle is V cos θ; the component opposite the angle is V sin θ. The test is whether the wanted component is next to the angle or opposite it. A check that keeps the two straight: set θ to 0°, where the vector lies along the reference direction. Its component there is the whole of V, and V cos 0° = V while V sin 0° = 0 — so the alongside component must be the cosine.

### Where this leads

Components carry the rest of the subject. Topic 2 resolves velocities into horizontal and vertical parts; topic 3 resolves forces, and weight on a slope into components along and across the slope; topic 4 does the same for objects on inclined planes. In topic 12, the same geometry appears when a gradient is read from a graph drawn on paper. An angle and a magnitude, resolved into two perpendicular parts, is the shape of half the mechanics in this syllabus.
