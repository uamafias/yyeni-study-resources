"""Original ideal/real gas manuscript and practice from the frozen work order."""
from authoring_common_8224 import Topic

t=Topic('1.4')
t.objective('-01',[
 'An ideal gas is modelled as particles in continuous random motion with negligible particle volume and no intermolecular attractions.',
 'Ideal-gas collisions are elastic; pressure arises from particle collisions with container walls.',
 'The average translational kinetic energy of ideal-gas particles is proportional to absolute temperature.'
],[
 ('A particle model with stated assumptions',
 '''An ideal gas is a model that links particle behaviour to measurable pressure, volume and temperature. Treat its particles as moving continuously and randomly. Between collisions a particle travels in a straight line. Its own volume is negligible compared with the volume available to the gas, and intermolecular attractions are neglected. These are modelling assumptions: real molecules have size and attract one another. A gas may nevertheless behave sufficiently close to the model for a useful calculation.

Collisions with other particles and with the walls are elastic. This means the total kinetic energy of the colliding particles is conserved in a collision; it does not mean that each particle keeps its original speed. Energy may be transferred from one particle to another. Gas pressure results from repeated impacts on the walls, which transfer momentum and produce a force distributed over an area.

Absolute temperature is measured in kelvin, K. The particles' average translational kinetic energy increases in direct proportion to this temperature. A gas sample contains particles with a range of speeds; the temperature statement concerns an average, rather than identical motion by every particle. Increasing temperature does not make each molecule larger. In a particle explanation, distinguish the volume of the sample from the volume of the particles themselves. A gas fills its container because the particles move through the available space; the assumption of negligible particle volume does not say that the sample has zero volume.

Consider a sealed, rigid vessel heated while the amount of gas remains fixed. Faster average motion produces more frequent wall impacts and greater average momentum transfer per impact. The pressure therefore increases. There is no need to propose that heating creates more particles or expands their individual dimensions. If a question asks for one assumption, identify one distinct model feature. If it asks for an explanation of pressure, connect motion, wall collisions and force per unit area. Keep an assumption about the model separate from an observation about a real sample.''')
], 'OpenStax-Chemistry','§9.5, printed pp.493–495 (PDF pp.503–505).')
t.objective('-02',[
 'Real gases approach ideal behaviour at low pressure and high temperature, where particle volume and intermolecular attractions have relatively small effects.',
 'At very high pressure the finite volume of gas particles becomes significant relative to the available container volume.',
 'At low temperature intermolecular attractions become more important relative to particle kinetic energy and can lead to condensation.'
],[
 ('When the model works and when it fails',
 '''Low pressure keeps the particles widely separated on average. Their own volume then occupies a small fraction of the container volume, and attractions have relatively little influence on the bulk behaviour. High temperature gives the particles high average kinetic energy relative to the attractive interactions. Together, low pressure and high temperature provide the circumstances in which a real gas usually approaches ideal behaviour. “High” and “low” are relative to the substance: no single pressure or temperature boundary applies equally to all gases.

At very high pressure the particles are crowded into a smaller space. The molecules themselves have finite size, so less space is available for their movement than the ideal model assumes. The particles do not acquire larger dimensions merely because the vessel is compressed. Instead, their existing volume becomes a significant fraction of the total. This helps explain why a real gas resists compression more strongly than the ideal prediction when the size effect dominates.

At low temperature the average kinetic energy is smaller. Attractions therefore have a greater influence on particle motion. At fixed amount, volume and temperature, attractive interactions can reduce the pressure relative to the ideal prediction. Near condensation, molecules can remain close together and a liquid forms; treating the whole sample as an ideal gas then fails. Do not state that the pressure of every real gas must be below the ideal value: finite size and attractions can affect the result in different directions.

The familiar molar-volume approximations also carry stated reference settings. In this syllabus use 22.4 dm³ mol⁻¹ at s.t.p. and 24.0 dm³ mol⁻¹ at r.t.p. They are alternative approximations for different temperature and pressure settings, not interchangeable constants. Use the reference setting stated in the problem. For a gas at another stated temperature and pressure, use pV = nRT rather than choosing whichever of those volumes seems convenient. These approximations and the ideal-gas equation describe a model; they do not remove real-gas limitations.''')
], 'OpenStax-Chemistry','§9.6, printed pp.499–501 (PDF pp.509–511); syllabus §1.1.5 for the prescribed molar-volume conventions.')
t.objective('-03',[
 'The ideal-gas equation is pV = nRT; with R = 8.31 J K⁻¹ mol⁻¹, p is in Pa, V in m³, n in mol and T in K.',
 'For a molecular gas with mass m, its molar mass is M = mRT/(pV); the numerical value in g mol⁻¹ equals its dimensionless relative molecular mass.',
 'For fixed amount and temperature an ideal gas has constant pV; changing temperature requires absolute rather than Celsius temperature.'
],[
 ('Using pV = nRT and determining relative molecular mass',
 '''The general gas equation is pV = nRT. Here p is absolute pressure, V is gas volume, n is amount of gas and T is absolute temperature. Use R = 8.31 J K⁻¹ mol⁻¹, the syllabus value. This value requires pressure in pascals, Pa, and volume in cubic metres, m³. Their product has the unit joule. Convert kPa to Pa by multiplying by 1000; convert dm³ to m³ by multiplying by 10⁻³, or cm³ to m³ by multiplying by 10⁻⁶. The temperature conversion is T/K = temperature/°C + 273.15, with an explicitly supplied rounded conversion used if the problem requests it.

For example, an ideal gas occupies 1.80 dm³ at 125 kPa and 300 K. Find its amount using n = pV/(RT). Convert to p = 125000 Pa and V = 1.80 × 10⁻³ m³. Substitution gives n = (125000 × 1.80 × 10⁻³)/(8.31 × 300) = 0.0902527 mol. Report 0.0903 mol to three significant figures, taking the stated temperature as three significant figures. Carry the unrounded value into any following calculation. A sensible check is that a few dm³ around room temperature and atmospheric pressure should contain much less than one mole.

If the same sample has mass 3.96 g, its molar mass is M = m/n = 3.96/0.0902527 = 43.877 g mol⁻¹, or 43.9 g mol⁻¹ to three significant figures. Equivalently, combine the equations to obtain M = mRT/(pV). For this molecular gas its relative molecular mass, Mᵣ, is 43.9 with no unit. The molar mass and relative molecular mass share a numerical value when molar mass is expressed in g mol⁻¹, but they represent different quantities.

Before calculating a vapour's molar mass, establish that the measured volume belongs to that gas sample at the stated temperature and absolute pressure. A mixture with air or liquid remaining makes the simple interpretation unreliable. Finally check what stays fixed: pV remains constant only for fixed n and T. Doubling pressure halves volume under those assumptions; doubling kelvin temperature at fixed pressure and amount doubles volume. A Celsius ratio cannot replace a kelvin ratio.''')
], 'OpenStax-Chemistry','§9.2, printed pp.470–478 (PDF pp.480–488); syllabus §1.4 for R = 8.31.')

s=t.wo['item_slots']
t.item(s[0],'State one ideal-gas assumption about particle size. [1]',
 'The volume of the particles themselves is negligible compared with the volume occupied by the gas. [1]')
t.item(s[1],'Suggest what happens to the total kinetic energy of two ideal-gas particles during a collision in a thermally insulated vessel. [1]',
 'It is conserved because the collision is elastic; energy may be transferred between the two particles. [1]')
t.item(s[2],'Describe three features of a real-gas sample that allow ideal behaviour to be a useful approximation. [3]',
 'Low pressure leaves particles widely separated [1], so their own volume is negligible relative to the sample volume [1]; high temperature makes average kinetic energy large relative to intermolecular attractions [1].')
t.item(s[3],'Explain why finite molecular size causes deviation from ideal behaviour at very high pressure. [2]',
 'Compression makes molecular volume a significant fraction of the total volume [1], because particles have finite size, so the space available for their motion is less than the ideal model assumes [1].',subtype='WHY')
t.deviations.append({'from':s[3]['slot']+' MECH','to':'WHY; original AO, Bloom, command word and tariff retained','why':'The explanation concerns finite particle volume and contains no reaction electron movement, intermediate or product.'})
t.item(s[4],'State the general ideal-gas equation. [1]','pV = nRT. [1] Here p is absolute pressure in Pa, V in m³, n in mol, T in K and R = 8.31 J K⁻¹ mol⁻¹.')
t.item(s[5],'Calculate the amount of an ideal gas occupying 1.80 dm³ at 125 kPa and 300 K. Use R = 8.31 J K⁻¹ mol⁻¹ and report three significant figures. [3]',
 'n = pV/(RT). Conversion: p = 125000 Pa, V = 1.80 × 10⁻³ m³ [1]. Substitution: n = 125000 × 1.80 × 10⁻³/(8.31 × 300) [1]. Answer: 0.0903 mol to three significant figures [1].')
t.item(s[6],'Determine the volume when the absolute pressure of a fixed amount of ideal gas at constant temperature changes from 100 kPa to 200 kPa. Its initial volume is 4.00 dm³. [1]',
 '2.00 dm³ [1]: the pressure doubles, so the volume halves because pV is constant for fixed amount and temperature.')
p=t.wo['performance_tasks']
t.item(p[0],'''Identify the correct option in each question. Use R = 8.31 J K⁻¹ mol⁻¹. [4]
1. An elastic collision conserves: A total kinetic energy; B each particle's speed; C each particle's direction; D separation between particles.
2. An ideal gas is modelled with: A strong attractions; B negligible particle volume; C stationary particles; D energy lost in each collision.
3. A real gas usually approaches ideal behaviour most closely at: A high pressure, low temperature; B high pressure, high temperature; C low pressure, low temperature; D low pressure, high temperature.
4. A 0.200 mol ideal-gas sample at 300 K and 100000 Pa occupies, to three significant figures: A 4.99 m³; B 0.00499 dm³; C 4.99 dm³; D 49.9 dm³.''',
 '''Key: 1 A, 2 B, 3 D, 4 C; one mark for each correct option.
1. A is correct: total kinetic energy is conserved. Distractor B confuses conservation of total energy with unchanged individual speeds; C ignores deflection during collision; D mistakes a changing distance for a conserved quantity.
2. B is correct: particle volume is negligible relative to sample volume. A introduces attractions omitted by the model; C removes the motion needed for pressure; D describes an inelastic collision.
3. D is correct: separation is large and kinetic energy is high relative to attractions. A favours both size and attraction effects; B retains crowding; C leaves attractions influential relative to kinetic energy.
4. C is correct: V = nRT/p = 0.200 × 8.31 × 300/100000 = 0.004986 m³ = 4.99 dm³. A has a factor-of-1000 error in m³; B fails to convert m³ into dm³; D is ten times too large.''')
t.item(p[1],'''Explain the behaviour of an ideal-gas model and its limits using the following linked parts. [8]
(a) State one assumption about particle motion and one about wall collisions. [2]
(b) Explain why cooling a real gas towards condensation makes ideal behaviour less reliable. [2]
(c) Calculate the ideal pressure of 0.150 mol gas in 3.00 dm³ at 320 K. Use R = 8.31 J K⁻¹ mol⁻¹; give three significant figures. [3]
(d) State what happens to that ideal pressure if the kelvin temperature doubles with amount and volume fixed. [1]''',
 '''Part (a): continuous random motion [1]; elastic wall collisions [1].
Part (b): average kinetic energy decreases [1], so attractions have a greater effect relative to that energy and the attraction-free model becomes less accurate [1].
Part (c): equation p = nRT/V and conversion V = 3.00 × 10⁻³ m³ [1]; working p = 0.150 × 8.31 × 320/(3.00 × 10⁻³) [1]; answer 1.33 × 10⁵ Pa to three significant figures [1]. The unrounded value is 132960 Pa.
Part (d): it doubles [1], because p is directly proportional to T at fixed n and V. Each bracket identifies a separate creditworthy point.''')
t.item(p[2],'''Calculate the relative molecular mass of a molecular gas using a 2.50 g sample occupying 1.25 dm³ at 100 kPa and 300 K. Use R = 8.31 J K⁻¹ mol⁻¹. [5]
(a) State the ideal-gas assumption about attractions used in the calculation. [1]
(b) Calculate Mᵣ to three significant figures, showing conversions and working. [3]
(c) Explain why a repeat measurement at very high pressure could make the ideal-gas result less reliable, referring to particle size. [1]''',
 '''(a) Intermolecular attractions are neglected [1].
(b) Equation: n = pV/(RT), M = m/n. Convert p = 100000 Pa and V = 1.25 × 10⁻³ m³ [1]. Working: n = 125/(8.31 × 300) = 0.0501404 mol; M = 2.50/0.0501404 = 49.86 g mol⁻¹ [1]. Answer Mᵣ = 49.9, dimensionless, to three significant figures as requested [1]. Retain unrounded intermediate values.
(c) Particle volume becomes a significant fraction of the sample volume, violating the negligible-volume assumption [1].''')
t.deviations.append({'from':'Generic C-12 conditions variant scan','to':'Use reference settings and circumstances in prose; retain both s.t.p. and r.t.p. with their prescribed volumes','why':'The checker surrounds each variant with word boundaries, so an abbreviation ending in a full stop cannot match normal prose. Both consequential forms are explicitly taught; no shared checker was changed.'})
t.save()
