# 10 D.C. circuits

*cie-9702-as-2025-2027. Offline study notes, rendered from the approved content units on 2026-09-29. Everything here is also what the flashcards are built from.*

**What this topic asks of you**

- The standard circuit symbols and how to read a circuit diagram, the electromotive force of a source and how it differs from potential difference, and what a source's internal resistance does to the p.d. at its terminals.
- Kirchhoff's two laws and the conservation principles behind them, the derivations of the series and parallel resistance formulae from the laws, the use of those formulae, and how to solve whole circuit problems step by step.
- The potential divider and the sharing rule behind it, the potentiometer as a way of comparing two potential differences, the galvanometer in null methods, and dividers that sense temperature and light with a thermistor or a light-dependent resistor.

---

## Practical circuits and sources of e.m.f.

### The standard circuit symbols

A circuit diagram shows what a circuit contains and how the components are joined, using one standard symbol for each component rather than a picture of the real thing. A cell is a pair of unequal parallel lines, the longer line marking the positive terminal. A battery is drawn as a stack of these pairs, because a battery is several cells joined in series. A fixed resistor is an open rectangle. A variable resistor is the same rectangle with a diagonal arrow drawn through it, the arrow showing that the value can be altered while the circuit works. A switch is a break in the connecting wire, closed by a hinged line. A lamp is a circle with a cross inside it. An ammeter is a circle with the letter A inside it; a voltmeter is a circle with the letter V. A junction, where three or more wires meet, is marked with a dot, so the reader can see at a glance where the current can divide or recombine. The table gathers the symbols this topic uses, described in words.

| Component | How the symbol is drawn | What it shows |
|---|---|---|
| cell | one long and one short parallel line | a single source of e.m.f.; the long line is the positive terminal |
| battery | a stack of cell symbols | several cells connected in series |
| fixed resistor | an open rectangle | a resistance of fixed value |
| variable resistor | a rectangle with a diagonal arrow | a resistance that can be altered |
| switch | a break in the wire with a hinged line | the loop can be opened and closed |
| lamp | a circle with a cross | electrical energy converted to light and heat |
| ammeter | a circle with an A | the current at the place it is put |
| voltmeter | a circle with a V | the p.d. between the two points it joins |
| junction | a dot where wires meet | current divides or combines here |

### Where the meters go

An ammeter measures the current passing the point where it sits, so it is connected in series, in the wire itself: the whole current of that branch must flow through the meter. A voltmeter measures the potential difference between two points, so it is connected across a component, from one side of it to the other, without breaking the wire. Each meter is built to change the circuit it joins as little as possible. An ammeter has a very low resistance, so placing it in series hardly affects the current it has come to measure. A voltmeter has a very high resistance, so it draws only a tiny current of its own, and the p.d. it is connected across is barely shifted by being measured. The wrong placement destroys the measurement: an ammeter connected across a lamp would give the current a near-zero-resistance route around the lamp, and a voltmeter connected in series would nearly stop the current altogether.

### Reading a circuit diagram

To interpret a diagram, start at the positive terminal of the source and trace each complete path through to the negative terminal, listing the components in order: each of these paths is one route the current can take. Components that follow one another on the same unbranched path carry the same current, because there is nowhere for it to leave: they are in series. Components that sit on separate branches between the same two junctions have the same p.d. across them: they are in parallel. A circuit can be described in a table instead of a drawing, and everything this topic asks about a circuit can be worked out from such a description. For example, described in words: a 12 V battery in series with a 4.0 Ω resistor, then a junction; one branch of the junction carries a 6.0 Ω resistor, the other a lamp of resistance 3.0 Ω; the branches rejoin and the wire returns to the battery. Reading it: the 6.0 Ω resistor and the lamp are in parallel with each other, and that pair is in series with the 4.0 Ω resistor and the battery.

### Electromotive force

The electromotive force (e.m.f.) of a source is the energy transferred from other forms to electrical energy per unit charge driven round a complete circuit. A cell of e.m.f. 1.5 V gives 1.5 J of energy to every coulomb of charge it drives round the loop. In symbols, E = W/Q, where E is the e.m.f. in volts (V), W the energy transferred from other forms in joules (J) and Q the charge driven round the complete circuit in coulombs (C). One volt is one joule per coulomb. The e.m.f. belongs to the source: it is fixed by the source itself and does not depend on what is connected to it, though the p.d. the connected circuit receives does.

### Energy, charge and time

A current I, in amperes, carries charge Q = It when it flows for a time t in seconds. The energy a source then transfers is W = EIt, with W in joules, E the e.m.f. in volts, I the current in amperes and t the time in seconds. Convert every prefix before substituting: a current of 250 mA is 0.25 A, and a time of 2.0 minutes is 120 s. Working is carried to at least three significant figures, and only the final answer is rounded.

### Worked example: a lighting loop at a lodge

A battery of e.m.f. 12 V drives a current of 0.40 A round the lighting loop of a lodge near Mariental for 2.0 minutes. How much charge passes any point of the loop, and how much energy does the battery transfer? First convert the time: 2.0 minutes is 120 s. Then the charge, from Q = It: Q = 0.40 × 120 = 48 C. Then the energy, from W = EQ: W = 12 × 48 = 576 J. The battery transfers 576 J, and every coulomb it drove round carried 12 J of it.

### E.m.f. and potential difference

E.m.f. and p.d. are both energies per unit charge and both are measured in volts, and there the likeness ends. E.m.f. is the energy given to each coulomb by a source: inside the source, other forms of energy become electrical energy. Potential difference is the energy given up by each coulomb in a component: in the component, electrical energy becomes other forms, such as heat and light. The test that tells them apart is to ask: is the energy going into the circuit or out of it? Into it, at a source, means e.m.f.; out of it, in a component, means p.d. When no current flows, the p.d. across a source's terminals equals its e.m.f., because with no current there is no energy converted inside the source. As soon as a current flows the two part company, which is the work of the internal resistance described next.

### Internal resistance and terminal p.d.

A real source does two things at once: it converts energy to electrical form, and it has some resistance of its own inside it, the internal resistance r, in ohms. When a current I flows, the charge passing through the source must pass through this resistance, so a p.d. Ir is used up inside the source itself. The p.d. that appears at the terminals, the terminal potential difference V, is therefore less than the e.m.f. whenever a current flows: V = E − Ir, with V and E in volts, I in amperes and r in ohms. The quantity Ir is the p.d. across the internal resistance, often called the lost volts, because it is energy per coulomb that leaves the source as heat inside the source instead of reaching the external circuit. The e.m.f. drives the current round the whole loop, internal and external resistance together, so the current a source drives through an external resistance R is I = E/(R + r). A source described as ideal would have r = 0, and its terminal p.d. would equal its e.m.f. at any current; real sources are not ideal, and the difference matters whenever the current is large.

### Worked example: a battery under load

A battery of e.m.f. 9.0 V and internal resistance 0.50 Ω is connected to a resistor of resistance 4.0 Ω. What current flows, and what is the terminal p.d.? The e.m.f. drives the current through the whole loop, so I = E/(R + r) = 9.0 ÷ (4.0 + 0.50). The bracket is 4.50, and 9.0 ÷ 4.50 = 2.0, so I = 2.0 A. The p.d. across the internal resistance is Ir = 2.0 × 0.50 = 1.0 V, so the terminal p.d. is V = 9.0 − 1.0 = 8.0 V. As a check, the external resistor sees V = IR = 2.0 × 4.0 = 8.0 V, the same value: the terminal p.d. is what the external circuit actually receives, and the 1.0 V of lost volts stayed inside the battery.

### Common errors: e.m.f. is not the terminal p.d.

Two errors recur here. The first is treating e.m.f. and the p.d. across a component as one quantity because both are measured in volts. They are not: the energy moves in opposite directions, into the circuit at the source and out of it in the component, and the shared unit hides that completely. The second is using the e.m.f. as the p.d. the external circuit receives. The terminal p.d. is E − Ir, and the difference Ir exists whenever a current flows through the source. The test for the second error is to ask whether a current is flowing through the source: if it is, the terminal p.d. sits below the e.m.f.; if no current flows, the terminal p.d. equals the e.m.f.

### Connections

Topic 9 defined current, potential difference and resistance and stated V = IR; this topic assembles those quantities into complete circuits. Topic 5 established conservation of energy, the principle that stands behind Kirchhoff's second law in the next section. Topic 12 uses the meters, sources and connections met here at the bench, where the same readings and the same care over units apply to every electrical experiment.

---

## Kirchhoff's laws and combined resistance

### Kirchhoff's first law

The sum of the currents entering a junction equals the sum of the currents leaving it. A junction is a point where three or more conductors meet, marked with a dot in a circuit diagram. If 0.30 A and 0.45 A flow into a junction along two wires, then 0.75 A in total must flow out of it along the other wires: 0.30 + 0.45 = 0.75. The law is a statement about currents at a junction, and about nothing else. It says nothing about a single current somewhere else in the loop, and nothing about energy; a claim that the first law is about e.m.f.s round a loop has swapped it for the second law.

### Why the first law is conservation of charge

Charge is conserved: it can be neither created nor destroyed. At a junction, charge flows in along some wires and out along others, and there is nowhere in the junction for it to accumulate and no way for it to vanish. In any second, then, the charge entering the junction equals the charge leaving it. Current is charge flowing per second, so the total current entering equals the total current leaving, and the balance holds at every instant whatever the rest of the circuit is doing. That is the whole content of the first law: it is conservation of charge, read at a single point.

### Kirchhoff's second law

Round any closed loop in a circuit, the sum of the e.m.f.s equals the sum of the potential differences across the components of the loop. A closed loop is a path that starts at a point, runs through components and returns to the same point. The law is a statement about a closed loop, as the first law is a statement about a junction, and the test that keeps them apart is to ask: a junction or a loop? A junction means the first law and currents; a loop means the second law and energies. Writing the second law for the single loop of a series circuit, the source's e.m.f. equals the sum of the p.d.s across the components of that loop, one equation for the whole chain.

### Why the second law is conservation of energy

A charge driven round a closed loop finishes where it started, so the electrical energy it carries on arrival is the energy it carried on departure. Along the way it passed through sources, which gave it energy, and through components, which took energy from it. Conservation of energy requires the two accounts to balance: the energy gained per coulomb from the sources, which is the sum of the e.m.f.s, equals the energy given up per coulomb in the components, which is the sum of the p.d.s. If the two totals differed, a charge could return to its starting point with more or less energy than it left with, and energy would have been created or destroyed round the loop, which conservation forbids.

### Deriving the series formula

Take two resistors R1 and R2 in series, in one unbranched chain across a supply. Step one, the current: there is no junction between the two resistors, so by Kirchhoff's first law the same current I passes through each; the current leaving one is the current entering the next, because charge is conserved all along the wire. Step two, the p.d.s: by Kirchhoff's second law, round the single closed loop, the supply p.d. V equals V1 + V2, the p.d.s across the two resistors. Step three, substitute the definition of resistance for each: V1 = IR1 and V2 = IR2, so V = IR1 + IR2 = I(R1 + R2). Step four, compare with V = IR, which defines the combined resistance R of the chain: R = R1 + R2. The same steps extend to any number of resistors in series, and the resistances simply keep adding. Because they add, the combined resistance of a series chain is greater than any one resistance in it: the current has every resistor to push through, one after another, which is why chains of resistors make poor heater elements and good proof that resistances add.

### Worked example: a series chain and its p.d. shares

A control panel for a borehole pump contains three resistors in series: 4.5 Ω, 8.6 Ω and 12.9 Ω. The combined resistance is R = 4.5 + 8.6 + 12.9. Working one step at a time: 4.5 + 8.6 = 13.1, and 13.1 + 12.9 = 26.0, so R = 26.0 Ω. Now the shares: put the chain of a 20 Ω and a 30 Ω resistor across a 10 V supply of negligible internal resistance. The chain is R = 20 + 30 = 50 Ω, so the current is I = 10 ÷ 50 = 0.20 A, and the p.d. across the 30 Ω resistor is V = 0.20 × 30 = 6.0 V. The 30 Ω resistor, the larger, takes 6.0 V of the 10 V, and the 20 Ω resistor takes the other 4.0 V: the shares are in proportion to the resistances, and they add to the supply p.d. exactly as the second law says.

### Deriving the parallel formula

Take two resistors R1 and R2 in parallel: two separate branches running between the same two junctions. Step one, the p.d.: go round the loop that runs out along one branch and back along the other. There is no source in that loop, so by Kirchhoff's second law the p.d.s round it must balance, and the p.d. across R1 equals the p.d. across R2; call the shared value V. Step two, the currents: by Kirchhoff's first law at either junction, the supply current I splits as I = I1 + I2. Step three, substitute the definition of resistance for each branch: I1 = V/R1 and I2 = V/R2, so I = V/R1 + V/R2. Step four, divide both sides by V: I/V = 1/R1 + 1/R2. The combined resistance R of the pair is defined by I = V/R, so 1/R = 1/R1 + 1/R2. For any number of branches the reciprocals keep adding. The last step of a parallel calculation takes the reciprocal again: adding reciprocals gives 1/R, and the resistance itself is 1 ÷ that total, a step often forgotten.

### Worked example: resistors in parallel

Two interior lamps of a minibus taxi have resistances of 40 Ω and 60 Ω and are connected in parallel when both are switched on. The combined resistance: 1/R = 1/40 + 1/60 = 0.0417 to three significant figures, so R = 1 ÷ 0.0417 = 24.0 Ω. The pair behaves as a single 24.0 Ω resistance, smaller than either lamp on its own, exactly as a parallel combination must be, because the supply current has two routes instead of one. A second example, with a twist: three resistors of 2.0 Ω, 3.0 Ω and 6.0 Ω in parallel give 1/R = 1/2.0 + 1/3.0 + 1/6.0 = 1.00, so R = 1 ÷ 1.00 = 1.0 Ω, one sixth of the largest resistor in the group. The reciprocals add; the resistances themselves do not.

### Solving circuit problems with the laws

A circuit problem is solved in a fixed order. First mark the current in each branch, with a chosen direction for each. Second, apply Kirchhoff's first law at the junctions: currents in equal currents out, which relates the branch currents to one another. Third, apply Kirchhoff's second law round the closed loops: e.m.f.s in the loop equal p.d.s across its components. Where a circuit has a single source and resistors combined in series and parallel steps, the same job can be done by combining: reduce the network stepwise to one total resistance, find the supply current from I = E/Rtotal, then split the p.d. and the currents back down through the combinations in reverse order. Worked through: a 12 V battery of negligible internal resistance feeds a 4.0 Ω resistor in series with a parallel pair of 6.0 Ω and 3.0 Ω. The parallel pair: 1/R = 1/6.0 + 1/3.0 = 0.500, so the pair is 2.0 Ω. The total is 4.0 + 2.0 = 6.0 Ω, so the supply current is I = 12 ÷ 6.0 = 2.0 A. The p.d. across the pair is then 2.0 × 2.0 = 4.0 V, and the branch currents follow: the 3.0 Ω branch carries 4.0 ÷ 3.0 = 1.3 A and the 6.0 Ω branch carries 4.0 ÷ 6.0 = 0.67 A, which recombine to 2.0 A at the far junction, as the first law requires. Notice how the smaller branch resistance took the larger current: between the same two junctions, the branch currents divide in inverse proportion to the branch resistances.

### Worked example: currents at a junction

At a junction in a lighting circuit, currents of 0.30 A and 0.45 A enter along two wires, and a current of 0.12 A leaves along one of the outgoing branches. The first law fixes the other outgoing branch: total in equals total out. Total in: 0.30 + 0.45 = 0.75 A. Total out must equal 0.75 A, and one outgoing branch already carries 0.12 A, so the other carries 0.75 − 0.12 = 0.63 A. The two outgoing currents, 0.12 A and 0.63 A, add back to the incoming 0.75 A, and the balance is a direct use of the law, with no need to know anything else about the circuit.

### Worked example: two loops through one junction

A 6.0 V source of negligible internal resistance feeds a parallel pair: a 2.4 Ω resistor on one branch and a 4.8 Ω resistor on the other, the branches meeting at two junctions. Step one, the shared p.d.: round the loop that runs out along one branch and back along the other there is no source, so by the second law the p.d. across the 2.4 Ω resistor equals the p.d. across the 4.8 Ω resistor, and both equal the 6.0 V between the junctions. Step two, the branch currents, each from V = IR: 6.0 ÷ 2.4 = 2.5 A on the smaller resistance, and 6.0 ÷ 4.8 = 1.25 A on the larger. Step three, the junction, by the first law: the source must supply the sum, 2.5 + 1.25 = 3.75 A. Step four, the check by combining: the pair has 1/R = 1/2.4 + 1/4.8 = 0.625, so R = 1 ÷ 0.625 = 1.6 Ω, and 6.0 ÷ 1.6 = 3.75 A, the same supply current. Notice the branch currents: equal p.d.s across unequal resistances force the currents into inverse proportion, 2 : 1 here, and the smaller resistance carries the larger current.

### Common errors: laws swapped, and parallel totals that rise

Two errors recur in this sub-topic. The first is swapping the laws: writing the first law about e.m.f.s round a loop, or the second about currents at a junction. The first law is currents at a junction, a consequence of conservation of charge; the second is e.m.f.s against p.d.s round a closed loop, a consequence of conservation of energy. The test is to ask, a junction or a loop, and to let the answer name the law. The second error is expecting an extra parallel branch to raise the total resistance, on the grounds that the circuit now contains more resisting material. The new branch gives the current another route: more current flows for the same p.d., so the combined resistance falls, to a value smaller than the smallest branch resistance. In the parallel formula the reciprocals add, and adding reciprocals of positive resistances can only make the total resistance smaller.

### Connections

Topic 9 gave V = IR, the ohm and the behaviour of ohmic and non-ohmic conductors; every derivation here divides or multiplies by V or I at some step. Topic 5 stated conservation of energy, which stands behind the second law, and conservation of charge behind the first is the same principle met there and in electrostatics. Topic 12 sets these circuit problems at the bench, where a real ammeter, a real voltmeter and a real cell all carry the resistances this section has accounted for.

---

## Potential dividers, potentiometers and sensing circuits

### The potential divider

A potential divider is two or more resistors in series across a supply, used to provide a p.d. that is a chosen fraction of the supply p.d. The supply p.d. is shared between the series resistors in the ratio of their resistances, because the same current flows through each and every p.d. is V = IR. For two resistors R1 and R2 across a supply of p.d. V, the p.d. across R1 is V1 = R1/(R1 + R2) × V. No single resistor of the chain takes the whole supply p.d.: the p.d.s across the chain add up to the supply p.d., which is Kirchhoff's second law written for the chain, and each share is in proportion to its resistance. To make the output larger, lower the fixed resistance it is taken across, or raise the other; to make it smaller, the reverse.

### Worked example: setting a divider's output

A 6.0 V supply feeds a divider made of a 2.0 kΩ resistor and a 4.0 kΩ resistor in series, and the output is taken across the 4.0 kΩ resistor. Convert first: 2.0 kΩ is 2000 Ω and 4.0 kΩ is 4000 Ω. The chain's total is 2000 + 4000 = 6000 Ω, so the current is I = 6.0 ÷ 6000 = 0.0010 A. The output is then V = IR = 0.0010 × 4000 = 4.0 V. The 4.0 kΩ resistor has 4.0 V across it and the 2.0 kΩ resistor has the other 2.0 V: the shares, 4.0 V and 2.0 V, are in the ratio 2 : 1 of the resistances turned about, and they add to the 6.0 V supply. The same sum run for the output across the 2.0 kΩ resistor gives 0.0010 × 2000 = 2.0 V, the smaller share of the smaller resistance.

### The potentiometer

A potentiometer is a length of uniform resistance wire or track with a driver p.d. applied across its full length L, and a sliding contact that can tap the wire at any distance x from one end. Because the wire is uniform, its resistance is spread evenly along it, so the p.d. between one end and the contact is x/L of the driver p.d.: a contact halfway along taps half the driver p.d. The potentiometer compares two p.d.s without drawing current from them at the moment of comparison. The unknown p.d. is connected between the sliding contact and the near end of the wire, and the contact is moved until the galvanometer in that connecting lead reads zero. At that balance position the p.d. tapped from the wire equals the unknown p.d., and the balance length is read off. Comparing two unknowns on the same wire, the balance lengths are in the ratio of the p.d.s: V1/V2 = x1/x2. A potentiometer is preferred to a voltmeter for comparing p.d.s because at balance no current is drawn from the source being measured, so the source's internal resistance does not reduce the reading the way it can through a voltmeter taking its small current.

### The galvanometer and null methods

A galvanometer is a sensitive centre-zero meter: it reads zero when no current flows through it, and it deflects to either side according to the direction of the current, which makes it a detector of small currents rather than a meter of large ones. In a null method, the galvanometer is connected between two points whose p.d.s are to be compared, and one of the two is adjusted until the reading is exactly zero. At that balance point no current flows through the meter, so no current is drawn from the source being measured either: the comparison does not disturb the thing it measures. The balance point is an exact position of the sliding contact, found by moving the contact until the deflection changes from one side to the other and then narrowing the interval down: it is the position where the reading is zero, not a vague region where the needle happens to look small.

### Sensing dividers: the thermistor and the light-dependent resistor

A thermistor is a resistor whose resistance falls as its temperature rises. A light-dependent resistor (LDR) is a resistor whose resistance falls as the light intensity falling on it rises: in bright light its resistance is low, and in darkness it is very large. In a sensing divider, one of the two series resistors is the sensor and the other is fixed, and the output is taken across one of the two. Take a thermistor in series with a fixed resistor R across a supply. As the temperature rises, the thermistor's resistance falls, so its share of the supply p.d. falls and the fixed resistor's share rises: the shares still add to the supply p.d., and the split has simply moved towards the fixed resistor. The output taken across the fixed resistor rises with temperature; the output taken across the thermistor falls with temperature. Which way the output moves is decided by where the output leads are attached, and by nothing else. The same reasoning with an LDR: more light, lower LDR resistance, larger p.d. across the fixed resistor. This is how a divider comes to switch things: a cooling fan, a street lamp or an alarm waits for the output p.d. to cross a threshold, and the sensor moves it there as light or temperature changes.

### Worked example: a temperature switch

A divider for a greenhouse fan is made from a thermistor and a 5.0 kΩ fixed resistor across a 6.0 V supply, and the output is taken across the fixed resistor. The fan is to run when the output exceeds 3.0 V. On a warm evening the thermistor's resistance is 5.0 kΩ: the two resistances are equal, so the supply halves across each, and the output is 3.0 V, which does not exceed the threshold, so the fan stays off. Later the temperature rises and the thermistor's resistance falls to 3.0 kΩ. The chain is then 3.0 + 5.0 = 8.0 kΩ, which is 8000 Ω, so the current is I = 6.0 ÷ 8000 = 0.00075 A, and the output across the fixed resistor is V = 0.00075 × 5000 = 3.75 V, which is 3.8 V to two significant figures. The output has crossed the threshold, so the fan runs: the divider has turned a change of temperature into a change of p.d., and the switch has answered it.

### Common errors: the whole supply across one resistor, and a vague balance point

Two errors recur in this sub-topic. The first is taking the whole supply p.d. as the p.d. across one resistor of a divider, as though a single component of the chain received everything the supply offers. The supply p.d. is shared by every resistor in the series chain, in proportion to resistance, and the shares add to the supply. The test is to ask how many resistors share the supply p.d., and to share it before quoting any single p.d. The second is describing the balance point vaguely, as a region where the needle settles down. At balance the galvanometer reads zero: no current flows through it, the two p.d.s being compared are equal, and the exact position of the sliding contact is the measurement. The test is to ask what the meter reads at balance, and to answer: zero, at one point, and nowhere else.

### Connections

Topic 9 introduced how the resistance of materials depends on conditions, including the thermistor; this topic puts that behaviour to work in a circuit that senses. Kirchhoff's second law from the previous section is the sharing rule the divider runs on. Topic 12 uses potential dividers and potentiometers at the bench, and its advice on readings, repeats and uncertainties applies to the balance lengths measured here.
