# 6 Deformation of solids

*cie-9702-as-2025-2027. Offline study notes, rendered from the approved content units on 2026-09-29. Everything here is also what the flashcards are built from.*

**What this topic asks of you**

- What a deformation is and how tensile and compressive forces cause it along one line; the terms load, extension, compression and limit of proportionality; Hooke’s law and the spring constant; stress, strain and the Young modulus; and an experiment to find the Young modulus of a metal wire.
- Elastic deformation and plastic deformation, and the elastic limit that separates them; the area under a force–extension graph as the work done by the load; the elastic potential energy stored within the limit of proportionality; and the formula EP = ½Fx = ½kx².

---

## Stress and strain

### Tensile and compressive forces

A deformation is a change in the shape or the size of an object, produced by a pair of forces. In this topic every force and every deformation is one-dimensional: the forces act along a single line, the line of the object’s length. A tensile force is a force that pulls the two ends of the object away from each other along that line; the object gets longer, which is why a tow rope on a bakkie stuck in sand is under tension. A compressive force pushes the two ends towards each other; the object gets shorter, as the legs of a table are compressed by the load on the table top. Both kinds of force change the object’s length, and both are measured in newtons. A stretched rubber band and a squeezed sponge differ only in which of the two is acting, so the first question about any deformed object is which kind of force the load applies.

### Load, extension and compression

The load on an object is the force applied to it, measured in newtons (N). The extension is the increase in the object’s length: the stretched length minus the original length, in metres (m). The compression is the matching decrease in length: the original length minus the shortened length, also in metres. A spring of original length 0.25 m that stands 0.31 m long under a load has an extension of 0.31 − 0.25 = 0.06 m; the same spring squeezed to 0.22 m has a compression of 0.03 m. Extension and compression are differences from the original length, not whole lengths, and that one habit — subtract the original first — is the step most often skipped in calculations with Hooke’s law.

### The limit of proportionality

Load a spring in steps and plot the force against the extension. Up to a point the graph is a straight line through the origin: the force is proportional to the extension, so doubling the load doubles the extension. The limit of proportionality is the point beyond which the force is no longer proportional to the extension. Beyond it the graph curves away from the straight line: extra load buys less and less extra extension. Within the limit the line’s gradient is constant and equals the spring constant; beyond it the gradient falls. The limit of proportionality is a statement about the shape of the graph, and it is not the same point as the elastic limit, which is about whether the object returns to its original shape when the load is removed — a distinction taken up with elastic and plastic deformation in topic 6.2.

### Hooke’s law

Hooke’s law states that the force on an object is proportional to its extension, provided the limit of proportionality is not exceeded. In symbols, F = kx, where F is the force in newtons (N), x is the extension in metres (m) and k is the spring constant of the object, in newtons per metre (N m⁻¹). The equation is a proportionality with a condition: it describes the straight-line part of the force–extension graph only, so any load that has bent the graph cannot be put into F = kx. Because the law links force to extension, x is the increase in length, taken from the original length, and not the stretched length of the object itself.

### Worked example: a scale spring at a garden shop

A spring scale at a garden shop in Etunda has a spring of spring constant 45 N m⁻¹. A bag of fertiliser hangs at rest on the hook, stretching the spring within its limit of proportionality. The scale shows the bag’s weight as 7.2 N, so the force on the spring is 7.2 N. The extension comes from Hooke’s law: x = F ÷ k. Substitution: 7.2 ÷ 45 = 0.16, so the extension is 0.16 m to two significant figures, the precision of the data. If the spring’s original length is 0.120 m, its stretched length is 0.120 m + 0.16 m = 0.28 m — and it is the 0.16 m, the difference, that the law needed.

### The spring constant

The spring constant of an object is the force per unit extension, k = F ÷ x, with the force F in newtons and the extension x in metres, so k is measured in N m⁻¹. A stiff spring needs a large force for each metre of stretch, so it has a large spring constant; a soft spring has a small one. On the force–extension graph, within the limit of proportionality, the spring constant is the gradient of the straight line. Joining springs changes the combined constant. Springs joined end to end, in series, each carry the whole load, so each stretches fully and their extensions add: two identical springs in series stretch twice as far as one, and the pair behaves like one spring of half the spring constant. Springs joined side by side, in parallel, share the load between them, so each stretches less and the constants add: two identical springs in parallel behave like one spring of twice the constant. The test for which case you have: does each spring carry the full load?

### Stress, strain and the Young modulus

Two wires of the same steel, one thick and one thin, carry very different forces for the same stretch, so force and extension describe the object, not the material. Stress and strain strip the dimensions out. The tensile stress is the force divided by the cross-sectional area: σ = F ÷ A, with F in newtons and A in m², measured in pascals (Pa), where 1 Pa = 1 N m⁻². The tensile strain is the extension divided by the original length: ε = x ÷ L, a ratio of metres to metres, so it has no unit. The Young modulus is the ratio of the stress to the strain for a material deformed within its limit of proportionality: E = (F ÷ A) ÷ (x ÷ L) = FL ÷ Ax, also in pascals. Steel has E of about 2.0 × 10¹¹ Pa; rubber is around 2 × 10⁷ Pa; a larger Young modulus means a stiffer material. Unlike a spring constant, which depends on the length and area of the particular object, the Young modulus is a property of the material alone.

### Worked example: a guy wire on the Kalahari

A steel wire 2.5 m long ties a solar-pump frame to a post in the Kalahari. Its diameter is 0.80 mm, and the wind loads it with 89 N, well within its limit of proportionality. How much does it stretch? First the area: A = πd² ÷ 4. The diameter is 0.80 mm = 0.80 × 10⁻³ m, so d² = 0.64 × 10⁻⁶ m², and A = 3.142 × 0.64 × 10⁻⁶ ÷ 4 = 0.503 × 10⁻⁶ m², that is 5.03 × 10⁻⁷ m². Then the strain, using E = 2.0 × 10¹¹ Pa for steel: the stress is F ÷ A = 89 ÷ 5.03 × 10⁻⁷ = 1.77 × 10⁸ Pa, and the strain is stress ÷ E = 1.77 × 10⁸ ÷ 2.0 × 10¹¹ = 8.85 × 10⁻⁴. Finally the extension: x = strain × L = 8.85 × 10⁻⁴ × 2.5 = 2.21 × 10⁻³ m, so the wire stretches about 2.2 mm.

### An experiment to determine the Young modulus of a wire

The Young modulus of a metal in the form of a wire is found by loading the wire and measuring how it stretches. Clamp a long wire — 2 m or more — at one end, pass it over a pulley at the edge of the bench, and hang a mass hanger from the other end, with a sticky marker on the wire beside a metre rule fixed alongside. First measure the original length L from the clamp to the marker with the metre rule, in metres. Then measure the diameter d of the wire with a micrometer screw gauge, at several places and at different orientations across the wire, and average the readings, since the area A = πd² ÷ 4 depends on the square of d. Now add masses one at a time, recording the load F = mg each time and reading the marker to find the extension x, the new length minus the original; unload in steps and check that the marker returns, so the wire has stayed within its elastic limit. Plot force against extension and take the gradient of the straight line: since F = (EA ÷ L)x, the gradient is EA ÷ L, and the final result is E = gradient × L ÷ A, in pascals.

### Sources of uncertainty in the experiment

The weak point of the method is that the extension is small: a 2 m steel wire stretches a few millimetres, and a metre rule graduated in millimetres therefore gives a large percentage uncertainty in x, which feeds straight into E. A long wire helps because it makes the extension proportionally larger; a marker read with a set square held against the rule reduces the parallax in the reading. The diameter matters twice over: it is small, and it is squared in the area, so the percentage uncertainty in d is doubled in A — the reason for taking several micrometer readings and averaging them, which reduces the random scatter of the readings. A systematic error also lurks: new wire has kinks, and the first loads straighten them, so early extensions read too large; pre-stretching the wire with the hanger alone, and measuring the original length after that, keeps E from coming out too small.

### Extension, not total length

The commonest slip in Hooke’s-law work is putting the length of the stretched object into F = kx where the extension belongs. A wire 1.50 m long that stands 1.68 m under a load has an extension of 1.68 − 1.50 = 0.18 m, not 1.68 m; using the whole length makes the extension — and so the calculated force — many times too large. The test: has the original length been subtracted before the value is used?

### Stress, strain and strain energy are three things

Stress, strain and strain energy sound alike and are not the same quantity. Stress is force per unit cross-sectional area and is measured in Pa; strain is extension ÷ original length and has no unit at all; elastic potential energy (also called strain energy) is the energy stored in a deformed object and is measured in joules. A learner who writes of a “large strain in pascals” has mixed the first two. The test that tells them apart: does the quantity have a unit, and which one? Pa means stress, no unit means strain, J means energy.

### Strain divides by the original length

Strain is the extension divided by the original, unstretched length of the object — the length before the load went on. Dividing by the stretched length instead, or by “the length of the wire” without saying which, makes the strain too small, and the difference grows the further the object is stretched: a wire stretched from 2.00 m to 2.02 m has strain 0.02 ÷ 2.00 = 0.010, not 0.02 ÷ 2.02. The test: which length sits on the bottom of the fraction?

### Connections

Forces and their vector addition come from topic 3; the work done when a force moves its point of application — the same idea as the area under a force–extension graph — is developed in topic 5, where the stored energy of this topic reappears as elastic potential energy in the conservation of energy. The practical skills used here — the micrometer, repeated readings and the gradient of a straight-line graph — are the tools of topic 12, and the cross-sectional area of a wire is the same A that appears with resistivity in topic 9.

### Checking the topic

You can state what a deformation is and name the tensile or compressive force that caused it; use load, extension, compression and limit of proportionality exactly; apply F = kx and k = F ÷ x with the right quantities and units; define stress, strain and the Young modulus and use them together; and describe, with its instruments and its uncertainties, an experiment that finds the Young modulus of a wire.

---

## Elastic and plastic behaviour

### Elastic deformation, plastic deformation and the elastic limit

An elastic deformation is a change of shape that disappears when the load is removed: the object returns to its original length. A plastic deformation is a permanent change of shape: it stays after the load is removed. A wire loaded within its elastic limit shows elastic deformation — unload it and it returns exactly; loaded beyond the elastic limit, the deformation becomes plastic and the wire keeps a permanent extension. The elastic limit is therefore the point beyond which an object will not return to its original shape when the load is removed. It sits at or a little beyond the limit of proportionality, which is a different point: the limit of proportionality marks where the force stops being proportional to the extension, where the graph’s straight line ends, whereas the elastic limit marks where the returning stops. Between the two, the graph curves but the wire still comes back.

### The force–extension graph of a wire loaded to breaking

Draw the axes: force on the vertical, extension on the horizontal, both with their units. For a ductile metal wire the loading curve is a straight line through the origin up to the limit of proportionality, then a gentle curve with a lessening gradient that passes the elastic limit. Beyond the elastic limit the deformation is plastic: the extension grows quickly, and large extensions follow from small extra loads; a neck forms and the wire breaks at its breaking stress. Unloading anywhere tells the two regions apart. Unload inside the elastic region and the line retraces itself back to the origin. Unload from beyond the elastic limit and the wire follows a straight line parallel to the original loading line, falling to zero force at a non-zero extension — the permanent extension left by the plastic deformation. The elastic limit is found on the graph, if at all, by this unloading test, not by looking for a bend in the loading curve. For example, a wire loaded to 70 N that unloads along a parallel line to zero force at 0.8 mm has a permanent extension of 0.8 mm; the same wire loaded to 40 N would have returned to the origin. Where on the curve the elastic limit sits, that example cannot say — only the unloading test locates it.

### The area under the graph is the work done

The work done by the load is the area under the force–extension graph, because work is force multiplied by the distance moved in the direction of the force, and on the graph the force is the height and the extension the width. Within the limit of proportionality the graph is a triangle, so the area is easy: a spring stretched 0.040 m by a force of 12 N has work done on it of half of 12 × 0.040 = 0.24, which is 0.24 J. Where the graph curves, the area is found by counting squares on the grid, each square worth its width in N multiplied by its height in m; the count is the work done whatever the shape of the line. Up to the elastic limit that work is stored as elastic potential energy and comes back out on unloading. Beyond the elastic limit, the loading curve and the parallel unloading line enclose an area as well: that energy is not stored — it is dissipated in making the change of shape permanent — which is why bending a wire back and forth warms it.

### EP = ½Fx = ½kx²

For a material deformed within its limit of proportionality, the elastic potential energy stored is EP = ½Fx = ½kx², where F is the force in newtons at the extension x, in metres, and k is the spring constant in N m⁻¹; the energy is in joules (J). The half is not decoration: the force rises from zero in step with the extension, so the average force during the stretch is half the final force, and the work done — the area of the triangle under the graph — is half the product of the final force and the extension. Since F = kx on the straight part of the graph, the two forms are the same equation: EP = ½Fx = ½ × kx × x = ½kx². Beyond the limit of proportionality the formula is not valid, because the graph is no longer a triangle.

### Worked example: a gate spring in the Otavi hills

A gate spring on a farm gate in the Otavi hills has a spring constant of 250 N m⁻¹. The gate swings the spring to an extension of 0.16 m, within its limit of proportionality, and the stored energy holds the gate shut. Stored energy: EP = ½kx². First square the extension: 0.16 × 0.16 = 0.0256 m². Then 250 × 0.0256 = 6.4, and half of that is 3.2, so EP = 3.2 J. Stretching the gate further, to 0.32 m, would not store 6.4 J but four times more, 12.8 J, because doubling the extension doubles the force as well.

### Double the extension, four times the energy

A learner who expects twice the extension to store twice the energy is assuming the force stays as it was. It does not: within the limit of proportionality the force grows with the extension, F = kx, so twice the stretch means twice the force at the end. The energy, EP = ½kx², carries one factor of the force and one of the extension, so doubling the extension doubles both factors: the stored energy is multiplied by four, not two. The test that keeps this straight: does the force stay the same as the extension grows? If it does, the work is Fx; if it grows with the stretch, the work is the triangle, ½Fx.

### The limit of proportionality is not the elastic limit

Labelling the point where the force–extension graph stops being straight as “the elastic limit” is a confusion of two different markers. The end of the straight line is the limit of proportionality — a statement about the graph’s shape. The elastic limit is a statement about the object’s behaviour: beyond it the object does not return to its original shape when the load is removed. The test: is the question about the line going curved, or about the object not returning?

### Connections

The work–energy ideas here belong to topic 5: work done is force × distance, and the energy stored in a deformed object is elastic potential energy in the conservation of energy. Topic 3 supplies the force as a vector along one line. The graph skills — gradient as spring constant, area by triangle or by counting squares, the unloading test — are the same ones topic 12 practises on practical graphs.

### Checking the topic

You can state what elastic deformation and plastic deformation are and where the elastic limit sits; describe the force–extension graph of a wire loaded to breaking, with its straight region, its curve and its parallel unloading line; read from that graph both the work done by the load and the elastic potential energy stored within the limit of proportionality; and use EP = ½Fx = ½kx² with its condition and its units, saying why the energy quadruples when the extension doubles.
