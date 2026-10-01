# 9 Electricity

*cie-9702-as-2025-2027. Offline study notes, rendered from the approved content units on 2026-09-29. Everything here is also what the flashcards are built from.*

**What this topic asks of you**

- Current as a flow of charge carriers, the size of the charge on one carrier, the equation Q = It, and the transport equation I = Anvq for a current-carrying conductor.
- Potential difference as the energy transferred per unit charge, the equation V = W/Q, and the three power equations P = VI, P = I²R and P = V²/R.
- Defining resistance and using V = IR; the I–V characteristics of a metallic conductor, a diode and a filament lamp; Ohm's law; resistivity through R = ρL/A; and the LDR and the thermistor.

---

## Electric current

### Electric current as a flow of charge

An electric current is a flow of charge carriers. In the copper wire that feeds a socket in a Windhoek house the carriers are free conduction electrons, drifting slowly along the wire while the signal itself travels almost instantly. In the conducting liquid inside a car battery the carriers are ions, both positive and negative, drifting in opposite directions; the current is still one number, because the two streams of charge add. Whatever the carrier, the current tells you how much charge passes a point each second: I = Q/t, with the current I in amperes (A), the charge Q in coulombs (C) and the time t in seconds (s). Current is measured with an ammeter placed in the path of the current, so the current passes through the meter. Conventional current is taken in the direction positive charge would move; in a metal the electrons drift the opposite way, and the current still reads positive in the conventional direction.

### Charge is quantised

The charge on a charge carrier comes in fixed packets. Charge is quantised: the charge on any carrier is a whole-number multiple of the elementary charge e = 1.60 × 10⁻¹⁹ C. An electron carries −e and a proton carries +e; a sodium ion in solution carries +e and a chloride ion −e. No single carrier carries half of e, or any fraction of it. A claimed charge of 2.4 × 10⁻¹⁹ C on one carrier is not possible, because 2.4 × 10⁻¹⁹ ÷ 1.60 × 10⁻¹⁹ = 1.5, not a whole number; 3.20 × 10⁻¹⁹ C is possible, being 2e. A charged object, as against a single carrier, can hold any whole number of elementary charges, so any everyday charge is still a whole-number multiple of e, just as a heap of flour comes in whole grains however fine it looks.

### Using Q = It

Q = It: the charge that passes a point equals the current I in amperes multiplied by the time t in seconds, and it comes in coulombs. One coulomb is the charge that passes when one ampere flows for one second, so a current of one ampere is a rate of one coulomb per second. Rearranged, the same equation gives the current from the charge and the time, I = Q/t, or the time from the charge and the current, t = Q/I. Because the charge on one carrier is a fixed packet of size e, the number of carriers that pass is the total charge divided by e: N = Q/e.

### Worked example: charging a phone at a camp near Etosha

A solar charger at a camp near Etosha feeds a phone with a current of 0.85 A for 40 minutes. The charge that passes is found with Q = It. First convert the time to seconds: 40 minutes is 40 × 60 = 2400 s. Then Q = It = 0.85 × 2400 = 2040 C, so 2040 C pass into the phone, which is 2.0 × 10³ C to two significant figures. Counting the carriers, each electron carries a charge of 1.60 × 10⁻¹⁹ C, so the number that pass is N = Q/e = 2040 ÷ (1.60 × 10⁻¹⁹) = 1.275 × 10²², which is 1.3 × 10²² to two significant figures. Notice how many carriers a small current needs: a coulomb is a large number of elementary charges, 1 ÷ 1.60 × 10⁻¹⁹ = 6.25 × 10¹⁸ of them.

### The transport equation I = Anvq

For a current-carrying conductor, I = Anvq. The symbols: I is the current in amperes; A is the cross-sectional area of the conductor in m²; n is the number density of the charge carriers, the number of carriers per cubic metre, in m⁻³; v is the drift speed of the carriers in m s⁻¹; q is the charge on one carrier in coulombs. The picture behind the equation: in one second the carriers within a distance v of a chosen cross-section sweep through it, so the volume that passes is Av, it holds nv carriers per unit volume's worth, and each carries charge q, giving the charge per second I = Anvq. Note carefully what n and q are: n is a number per cubic metre and q is the charge on one carrier. Using the total number of free electrons in the wire, or the total charge in it, goes wrong, because only the carriers passing the cross-section each second make the current.

### Worked example: drift speed in a copper wire

A copper wire of cross-sectional area 1.2 mm² carries a current of 3.6 A. Copper has a number density of conduction electrons of 8.0 × 10²⁸ m⁻³, and each electron carries a charge of 1.60 × 10⁻¹⁹ C. First convert the area: 1.2 mm² is 1.2 × 10⁻⁶ m². Rearrange I = Anvq for the drift speed: v = I ÷ (Anq). Substitute: v = 3.6 ÷ (1.2 × 10⁻⁶ × 8.0 × 10²⁸ × 1.60 × 10⁻¹⁹). The bottom line is 1.2 × 8.0 = 9.60, times 1.60 gives 15.36, and the powers of ten give 10⁻⁶⁺²⁸⁻¹⁹ = 10³, so Anq = 1.536 × 10⁴. Then v = 3.6 ÷ 1.536 × 10⁴ = 2.34 × 10⁻⁴ m s⁻¹, which is 2.3 × 10⁻⁴ m s⁻¹ to two significant figures. The drift speed is far smaller than the speed at which anything else in the room moves: the wire holds so many carriers per cubic metre that a slow drift carries an everyday current. The same equation rearranged also gives the current from a drift speed, or the number density from the other quantities.

### What I = Anvq explains about materials

The transport equation shows why metals conduct and why the current in a wire depends on more than the wire's size. A copper wire and a germanium crystal of the same area carry currents in the ratio of their number densities and drift speeds; a metal has a huge n, of the order of 10²⁸ to 10²⁹ m⁻³, so a drift speed too small to see carries amps. When a wire narrows, the same current needs a larger drift speed in the thinner part, because A has shrunk; when a wire is doubled in area at the same current, the drift speed halves. These are the kinds of reasoning the equation supports, all of them one substitution away.

### Where this connects

Current as a flow of charge meets charge again in topic 11, where the same quantised charge e is carried by fundamental particles and the same counting of multiples of e is used on nuclei. The power delivered by a current appears in section 9.2, the resistance that limits a current in section 9.3, and both return in topic 10, where I = Anvq reasoning is applied to whole circuits and sources. The unit work of topic 1 built the ampere and the coulomb; the reading-and-uncertainty habits of topic 12 apply to every ammeter reading here.

### Worked example: time to pass a given charge

The starter motor of a bakkie at a Otjiwarongo garage draws 180 A from the battery. The charge that passes in a 2.0 s start attempt is Q = It = 180 × 2.0 = 360 C. How long would a current of 0.50 A take to move the same charge, a current more like the interior lamp? Rearranged, t = Q/I = 360 ÷ 0.50 = 720 s, which is 12 minutes. The same charge moved by a small current takes much longer: the equation trades current against time at fixed charge. Each coulomb shifted carries the same packet size, 1 ÷ 1.60 × 10⁻¹⁹ = 6.25 × 10¹⁸ elementary charges, whatever the current.

---

## Potential difference and power

### Potential difference

The potential difference (p.d.) across a component is the energy transferred from electrical to other forms, per unit charge that passes through the component. P.d. is a ratio: the energy converted divided by the charge that carried it, not the energy alone. Its unit is the volt (V). A p.d. of 12 V across a car lamp means each coulomb passing through the lamp converts 12 J from electrical energy into heat and light; twice the charge converts twice the energy at the same p.d. P.d. is measured with a voltmeter connected across the component, in parallel with it, and it is a property of the two points it is measured between. Potential difference is not the same as electromotive force, which belongs to a source driving charge round a circuit and is treated in topic 10.

### Using V = W/Q

V = W/Q, with the p.d. V in volts, the energy W transferred from electrical form in joules and the charge Q in coulombs. One volt is one joule per coulomb, which is what the ratio says. Rearranged, W = VQ gives the energy converted by a component from the p.d. across it and the charge that passes; and because Q = It, a component working at a steady p.d. converts W = VIt in a time t. The same equation read the other way, Q = W/V, tells you how much charge a given energy conversion shifts at a given p.d.

### Worked example: a borehole pump at a farm near Gobasis

A borehole pump at a farm near Gobasis draws a current of 9.0 A from a supply that keeps a p.d. of 230 V across the pump. The charge that passes in one minute is Q = It = 9.0 × 60 = 540 C. The energy converted from electrical form in that minute is W = VQ = 230 × 540 = 124200 J, which is 1.2 × 10⁵ J to two significant figures. In kilowatt-hours, the unit the farm pays for, that is 124200 ÷ 3.6 × 10⁶ = 0.0345 kWh per minute, so a full hour of pumping converts 60 × 0.0345 = 2.07 kWh, about 2.1 kWh. Every step is one of the two equations, Q = It then W = VQ, with the time converted to seconds first.

### Worked example: energy per charge in a stove element

A stove element at a Katima Mulilo kitchen converts 9.0 × 10⁴ J of electrical energy to heat while a charge of 3.6 × 10² C passes through it. The p.d. across the element is V = W/Q = (9.0 × 10⁴) ÷ (3.6 × 10²) = 250 V. Each coulomb carried 250 J of energy into the element. If the element runs for 4.0 minutes, the current that passed that charge is I = Q/t = 360 ÷ 240 = 1.5 A, and the power converted is P = VI = 250 × 1.5 = 375 W, which is 0.38 kW to two significant figures. The three readings, energy, charge and time, chain through V = W/Q and Q = It into the power.

### Power in an electrical component

P = VI: the electrical power converted in a component equals the p.d. V across it in volts multiplied by the current I in it in amperes, giving watts. This is the energy-per-charge of the p.d. combined with the charge-per-second of the current, so the product is energy per second. Substituting V = IR into P = VI gives the two equivalent forms P = I²R and P = V²/R; all three describe the same component of resistance R, and each converts into the others through V = IR.

### Worked example: choosing the right power equation

Two heater elements at an Oshakati workshop are connected one at a time across the same 230 V supply: the first has a resistance of 19 Ω, the second of 38 Ω. Because both elements have the same p.d. across them, compare them with P = V²/R. For the first: P = V²/R = 230² ÷ 19. Here 230² = 52900, and 52900 ÷ 19 = 2784 W. For the second: 52900 ÷ 38 = 1392 W. The 19 Ω element converts 2780 W and the 38 Ω element 1390 W, each to three significant figures. The element with the smaller resistance converts more power in this situation because both share the same p.d. and so carry different currents; the larger resistance passes the smaller current, and the current appears squared in P = I²R. To compare two components, pick the form of the power equation whose other quantity is the same for both: P = V²/R when they share a p.d., P = I²R when they carry the same current, as two components in series do.

### Where this connects

Power as energy transferred per unit time came from topic 5, and the efficiency of a motor, a lamp or a solar panel divides an output power by an input power, both in the watts this section calculates. The resistance that appears in P = I²R and P = V²/R is defined in section 9.3. In topic 10 the same equations price the losses inside a source with internal resistance and the energy delivered to a load, and the energy totals of this section become the electricity account of a household.

### Worked example: power at a laptop charger

A laptop charger at a student flat in Windhoek keeps a p.d. of 19 V across the charging circuit and drives a current of 3.2 A through it. The power converted is P = VI = 19 × 3.2 = 60.8 W, which is 61 W to two significant figures. The energy converted in 30 minutes of charging is W = VIt = 19 × 3.2 × 1800 = 109440 J, since 30 minutes is 1800 s, which is 1.1 × 10⁵ J to two significant figures. The same power from P = I²R needs the resistance of the circuit: R = V/I = 19 ÷ 3.2 = 5.9375 Ω, which is 5.9 Ω, and P = I²R = 3.2² × 5.9375 = 60.8 W, the same answer by the second route. Note that the second route is a check on the first, not an added meaning: the meaning of 61 W is the rate of converting electrical energy.

---

## Resistance and resistivity

### Resistance

The resistance of a component is the ratio of the potential difference across it to the current in it: R = V/I. Its unit is the ohm (Ω), and one ohm is one volt per ampere. The ohm is the resistance of a component in which a p.d. of one volt drives a current of one ampere. Resistance describes a ratio between two readings; it is not a measure of how much a component pushes back on the current, a description that cannot be tested with numbers.

### Using V = IR

V = IR links the p.d. V across a component in volts, the current I in it in amperes and its resistance R in ohms. The equation holds at any instant, for any component: the ratio of the two readings at that instant is the resistance at that instant, whether or not the resistance stays constant as the current changes. The equation is the working definition of resistance at every level: the resistance of a component is found by dividing the p.d. reading by the current reading, in ohms.

### Ohm's law

Ohm's law: the current through a conductor is proportional to the p.d. across it, provided the temperature and other physical conditions stay constant. The condition is part of the law, not a footnote: heat a wire while you measure it and the proportionality fails, not because the law is wrong but because its condition is broken. A conductor that obeys Ohm's law at fixed temperature has a constant resistance, and its I–V graph is a straight line through the origin. A metal at constant temperature, kept cool by a water bath or by small currents, obeys the law; a filament lamp does not over a wide range, because its own current raises its temperature.

### The three I–V characteristics

An I–V characteristic is a graph of the current I in a component against the p.d. V across it, with current on the vertical axis and p.d. on the horizontal axis. Three shapes cover the components this syllabus names. A metallic conductor at constant temperature gives a straight line through the origin: the current is proportional to the p.d., and the line has the same gradient in both directions. A filament lamp gives a line that starts straight through the origin but curves over as the p.d. grows, its gradient decreasing at larger currents; the same curve appears in both directions, because the lamp heats the same way whichever way the current flows. A semiconductor diode gives a graph that hugs the current axis: a very small current passes for p.d. below about 0.7 V in the forward direction, and a very small current passes at any reverse p.d.; above the forward threshold the current rises steeply, so the diode conducts in one direction only. On any of these graphs the resistance at a point is the ratio V/I of the coordinates there, which is not the gradient of the line, because the axes are I against V and resistance is V over I. Only a straight line through the origin shows a constant resistance, because only there is the ratio V/I the same at every point.

### A straight line is not constant resistance

A learner sees a straight I–V line and says the resistance is constant because the line is straight. The error is confusing the gradient with the ratio. Resistance at a point is V/I at that point, not the gradient of the line. A straight line that does not pass through the origin has a constant gradient, but V/I changes along it, so the resistance is not constant. The test: does the straight line pass through the origin? If it does, the resistance is constant; if it does not, it is not.

### Why a filament lamp's resistance rises with current

The resistance of a filament lamp increases as the current in it increases, because the larger current raises the filament's temperature. At the higher temperature the lattice ions in the metal vibrate with greater amplitude, and the conduction electrons collide with them more often, so a larger p.d. is needed per ampere: the ratio V/I is larger. This is why the lamp's I–V graph curves over at larger p.d., and it is why the lamp does not obey Ohm's law over a wide range, since its own current changes its temperature.

### Worked example: resistance from a pair of readings on a lamp

Readings taken on a small lamp in a Tsumeb school laboratory: at a p.d. of 2.0 V the current is 0.40 A, and at a p.d. of 6.0 V the current is 0.75 A. At the first point the resistance is R = V/I = 2.0 ÷ 0.40 = 5.0 Ω. At the second point it is 6.0 ÷ 0.75 = 8.0 Ω. The resistance at the larger current is greater, consistent with the lamp running hotter at 6.0 V; the lamp's resistance is not constant, and each ratio is the resistance at that one operating point.

### Resistivity

The resistance of a uniform wire is R = ρL/A, where ρ (rho) is the resistivity of the material in Ω m, L is the length of the wire in m and A is its cross-sectional area in m². For a circular wire A = πd²/4 with d the diameter. A longer wire has a greater resistance in proportion to its length; a fatter wire has a smaller resistance, and because the area depends on the square of the diameter, doubling the diameter makes the area four times larger and cuts the resistance to a quarter. Resistivity is a property of the material alone: two wires of the same metal, whatever their shape, share one resistivity.

### Worked example: an earthing stake at a Rehoboth smallholding

A copper earthing stake at a smallholding near Rehoboth is connected to a consumer unit by a copper wire 8.0 m long and 0.80 mm in diameter. The resistivity of copper is 1.7 × 10⁻⁸ Ω m. First convert the diameter: 0.80 mm is 0.80 × 10⁻³ m. The cross-sectional area is A = πd²/4 = 3.142 × (0.80 × 10⁻³)² ÷ 4. Here (0.80 × 10⁻³)² = 6.4 × 10⁻⁷, so A = 3.142 × 6.4 × 10⁻⁷ ÷ 4 = 5.03 × 10⁻⁷ m². Then R = ρL/A = (1.7 × 10⁻⁸ × 8.0) ÷ (5.03 × 10⁻⁷). The top line is 1.36 × 10⁻⁷. Dividing, 1.36 ÷ 5.03 = 0.270, and 10⁻⁷ ÷ 10⁻⁷ cancels, so R = 0.270 Ω, which is 0.27 Ω to two significant figures. If the same run were made with wire of twice the diameter, 1.6 mm, the area would be four times larger and the resistance would fall to about 0.068 Ω.

### The LDR and the thermistor

A light-dependent resistor (LDR) is a semiconductor component whose resistance decreases as the light intensity falling on it increases: brighter light gives the semiconductor more charge carriers, so a larger current flows for the same p.d. A thermistor is a semiconductor component whose resistance decreases as its temperature increases, again because more charge carriers are released at the higher temperature; this is the behaviour the syllabus assumes for thermistors. The two differ in what they respond to: the LDR to light intensity, the thermistor to temperature. Both are the opposite of a metal in their own way. A metal's resistance rises as its temperature rises, because its carrier number is fixed and its hotter lattice obstructs the carriers more; a thermistor's resistance falls as its temperature rises, because the growing number of carriers wins. An LDR in a street light in Keetmanshoop sits in a sensing divider that detects dusk; a thermistor in a car engine senses how warm the coolant has become, and each reading converts to a change of resistance that the rest of the circuit reads.

### Worked example: a diode's resistance below and above the threshold

Readings for a semiconductor diode in the forward direction, taken in a school laboratory: at a p.d. of 0.5 V the current is 1.2 mA, and at a p.d. of 0.9 V the current is 62 mA. At the first point the resistance is the ratio of the coordinates: R = V/I = 0.5 ÷ 0.0012 = 416.7 Ω, which is 420 Ω to two significant figures. At the second point: R = 0.9 ÷ 0.062 = 14.5 Ω, which is 15 Ω to two significant figures. The resistance at the larger current is much smaller: above about 0.7 V the diode's current rises steeply for a small extra p.d., which is the same thing as saying its resistance falls fast. Below the threshold the resistance is large, so the diode blocks; above it the resistance is small, so the diode passes current in the forward direction. The two ratios are each the resistance at one operating point, read from the table; no single resistance describes the diode.

### Worked example: reading an LDR and a thermistor in a sensing circuit

A light-dependent resistor in a sensing circuit is read at two light levels. In bright daylight its resistance is measured as 220 Ω; in darkness it rises to 1.8 × 10⁵ Ω. A p.d. of 6.0 V is connected across it in turn at each level, and the current follows from V = IR rearranged. In daylight: I = V/R = 6.0 ÷ 220 = 0.0273 A, which is 27 mA to two significant figures. In darkness: I = 6.0 ÷ (1.8 × 10⁵) = 3.33 × 10⁻⁵ A, which is 0.033 mA to two significant figures. The same LDR passes a current nearly a thousand times larger in daylight than in darkness, which is what makes it useful as a dusk sensor: the current change is large and easy to detect. A thermistor read in the same circuit behaves the same way towards temperature: as its temperature rises, its resistance falls, and the current at a fixed p.d. rises. In each case the direction is fixed by the release of extra charge carriers in the semiconductor - more light or more heat, more carriers, smaller resistance, larger current.

### Reading resistance off an I–V graph: the method that never fails

A learner given any I–V graph needs one method that works on all of them. Choose the point of interest, read the p.d. V and the current I there, and divide: R = V/I. The method works on a straight line through the origin, where it gives the same answer at every point, because there the resistance is constant. It works on a filament lamp's curve, where it gives a growing resistance as the current grows. It works on a diode's characteristic, where it gives a large resistance below the forward threshold and a small one above it. And it works on a straight line that misses the origin, where it gives a different value at every point even though the line looks tidy. What the method never does is read the gradient: on an I–V graph the gradient is the change in current divided by the change in p.d., which is 1/R only for a line through the origin. Where a question hands over a table of I and V values instead of a graph, the same method applies row by row: each row is one operating point, and each ratio V/I is the resistance there.

### Worked example: two wires compared through R = ρL/A

A student at a Rundu school compares two sample wires of the same metal. Wire P is 0.75 m long with a cross-sectional area of 2.7 × 10⁻⁷ m². Wire Q is 1.5 m long with a cross-sectional area of 5.4 × 10⁻⁷ m². Because the two wires share one resistivity, their resistances can be compared from the ratio of L/A without knowing ρ at all. For wire P: L/A = 0.75 ÷ (2.7 × 10⁻⁷) = 2.78 × 10⁵ m⁻¹, which is 2.78 × 10⁵ to three significant figures. For wire Q: L/A = 1.5 ÷ (5.4 × 10⁻⁷) = 2.78 × 10⁵ m⁻¹ as well: doubling the length and doubling the area leave L/A unchanged. So the two wires have the same resistance, whatever the metal, because R = ρL/A with the same ρ and the same L/A. The comparison is the whole point of the equation: resistance belongs to the sample through two lengths and an area, and only the resistivity belongs to the material. A wire of twice the length and twice the area of another of the same metal has the same resistance; a wire of twice the length and the same area has twice the resistance.

### Where this connects

The straight-line I–V graph is read with the gradient skills of topic 12, and the resistivity method, a wire, a micrometer and a graph of R against L/A, is a standard practical. Ohm's law and the lamp characteristic lead directly into topic 10, where resistors, sources with internal resistance and the potential divider, built from exactly these components, are combined into circuits.

### Worked example: is this wire ohmic?

A student at a Swakopmund school records the current through a sample wire held at constant temperature in a water bath: at 1.0 V the current is 0.20 A, at 2.0 V it is 0.40 A, at 3.0 V it is 0.61 A and at 4.0 V it is 0.79 A. The ratios V/I at the four points: 1.0 ÷ 0.20 = 5.0 Ω; 2.0 ÷ 0.40 = 5.0 Ω; 3.0 ÷ 0.61 = 4.918 Ω, which is 4.9 Ω; 4.0 ÷ 0.79 = 5.063 Ω, which is 5.1 Ω. The ratio is constant to within the reading scatter, about 5 Ω, and the points plotted as I against V lie on a straight line through the origin, so at this temperature the wire obeys Ohm's law and its resistance is 5.0 Ω to two significant figures. Had the ratios drifted upward as the current grew, that would be the signature of the sample warming, as a filament lamp does.

### Worked example: resistivity of a constantan sample

A student measures a constantan wire at a Keetmanshoop school: length 1.50 m, diameter 0.44 mm, resistance 5.6 Ω. First the area: d = 0.44 mm = 0.44 × 10⁻³ m, so d² = 1.936 × 10⁻⁷ m² and A = πd²/4 = 3.142 × 1.936 × 10⁻⁷ ÷ 4 = 1.521 × 10⁻⁷ m². Then rearrange R = ρL/A for the resistivity: ρ = RA/L = (5.6 × 1.521 × 10⁻⁷) ÷ 1.50. The top line is 8.518 × 10⁻⁷, and 8.518 ÷ 1.50 = 5.679, so ρ = 5.679 × 10⁻⁷ Ω m, which is 5.7 × 10⁻⁷ Ω m to two significant figures. This is the standard practical route to a resistivity: measure R, L and the diameter, and compute ρ; the diameter, entering squared, has the largest effect on the uncertainty.
