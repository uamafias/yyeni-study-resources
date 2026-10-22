"""Original collision-theory and catalysis manuscript plus deterministic energy curves."""
import math
from authoring_common_8224 import Topic
from render_chemistry_visuals_8224 import Figure
t=Topic('2.4')
def add(short,claims,title,text,loc,source='OpenStax-Chemistry'):t.objective(short,claims,[(title,text)],source,loc)
add('1-01',[
 'Reaction rate describes change in reactant or product concentration per unit time, or a specified measurable reaction-related change per unit time.',
 'Average rate uses a finite interval; instantaneous rate is obtained from the gradient of the relevant time curve at the chosen time.',
 'Reactant disappearance and product formation rates can have different magnitudes because their stoichiometric coefficients differ.'
], 'Measuring how quickly a reaction proceeds', '''Rate of reaction describes how quickly reactants are consumed or products are formed. A concentration-based rate uses the change in concentration divided by the corresponding time interval. For a product, average formation rate is Δ[product]/Δt. For a reactant, quote disappearance rate as −Δ[reactant]/Δt so the reported magnitude is positive when its concentration falls. A rate in mol dm⁻³ s⁻¹ is a concentration change per second, not a concentration alone.

Experiments may follow a related measurable quantity, such as gas volume or loss of mass. Label the rate accordingly: cm³ s⁻¹ describes gas-volume production, while g s⁻¹ describes mass loss. These rates cannot be compared numerically as if their units were identical. The measured quantity must actually track reaction progress; escaping gas, leaks or unrelated evaporation can distort the interpretation.

For original gas-volume data, a rise from 12.0 to 30.0 cm³ over 15.0 s gives average volume-production rate (30.0 − 12.0)/15.0 = 1.20 cm³ s⁻¹. This describes the whole interval. To find a rate at one moment, draw a tangent to a suitable smooth volume–time curve at that moment and calculate its gradient using two well-separated points on the tangent. Two points on the curve instead give a secant and an average rate.

A steeper product-time gradient indicates faster production. A flat final section indicates no further measurable net production under that setup, not proof of a particular reason without chemical evidence. In 2H2O2 → 2H2O + O2, peroxide disappears at twice the molar rate of oxygen formation. State which species or measured signal your rate describes. Topic 5.1 applies these ideas to collecting data, plotting and estimating gradients.''',
 '§12.1, printed pp.651–656 (PDF pp.661–666), rates, tangents and stoichiometric factors.')
add('1-02',[
 'In a simple collision-controlled comparison at constant temperature, increasing reactant concentration increases the frequency of encounters per unit volume.',
 'A productive collision requires suitable energy and orientation; higher concentration does not itself raise the energy distribution at fixed temperature.'
], 'Concentration changes the encounter frequency', '''Collision theory describes reactions through encounters between reacting particles. A collision must have sufficient energy and a suitable orientation to lead to the chemical rearrangement. Some encounters fail to produce product. The measured rate therefore depends on successful encounters, not merely on the existence of particles in a vessel.

At unchanged temperature, raising a reactant concentration puts more of its particles into a given volume. Other reacting particles meet them more frequently, increasing the frequency of potential reaction encounters per unit volume. For a simple reaction whose rate depends on those encounters, this increases the number of successful collisions per second and the reaction rate. Keep temperature and other relevant factors fixed when making that explanation.

Increasing concentration is not the same as heating. At a fixed temperature it does not require a higher mean kinetic energy or a different fraction of particles above an unchanged energy threshold. It changes how many particles are available to collide. In contrast, a temperature change alters particle energies as well as speeds. Separate these explanations instead of attributing the concentration effect to particles becoming more energetic.

For a comparison between a more concentrated and a more dilute acid reacting with the same form and amount of a solid, keep temperature, exposed solid surface and mixing comparable. The more concentrated reacting solution can produce gas faster initially because it supplies more reacting particles per unit volume. The final gas volume may also differ if the amount of limiting reagent differs, so initial rate and total product are separate observations. Do not claim that doubling concentration must double the rate for a reaction whose dependence has not been established. More complicated mechanisms can have different concentration responses; the syllabus explanation here is qualitative rather than a universal numerical rate law.''',
 '§12.5, printed pp.677–679 (PDF pp.687–689), collisions and concentration effects.')
add('2-01',[
 'Activation energy is the minimum energy that colliding particles must have for a reaction to occur.',
 'A Boltzmann distribution plots a particle-energy distribution against energy; the area to the right of Ea represents the number or fraction with sufficient energy.',
 'Ea is a position on the energy axis, not an area under the distribution curve.'
], 'Activation energy on a distribution diagram', '''Activation energy is the minimum energy that colliding particles must have for a reaction to occur. Write its symbol Ea. It is an energy threshold associated with a particular pathway. Having sufficient energy is necessary but does not remove the need for a suitable collision orientation. The barrier is different from the overall reaction enthalpy discussed in Topic 2.1.

A Boltzmann distribution describes the spread of energies in a large collection at a stated temperature. Put energy on the horizontal axis and number of particles per energy interval, or a corresponding fraction density, on the vertical axis. The curve starts from zero, rises to a maximum and has a long tail towards high energy. It approaches the axis at high energy. The area represents the particle population, so comparisons for the same number of particles retain the same total area.

Mark Ea on the horizontal axis and draw a vertical threshold line. The area under the curve beyond that line represents particles with energy at least Ea. The threshold is a value of energy; the area is a number or fraction of particles. They are not interchangeable physical quantities. Do not label the shaded tail “activation energy”.

![Generated Boltzmann energy distributions at two temperatures, with a fixed Ea](assets/8224-boltzmann-temperature.png)

This is not a reaction-pathway profile. A pathway profile has enthalpy vertically and progress of reaction horizontally, whereas this distribution has particle population vertically and energy horizontally. A peak on one diagram therefore means something different from a peak on the other. When drawing from a question, identify the requested axes first. Label the threshold and explain what the area means instead of copying the shape of an unrelated energy diagram.''',
 '§9.5 printed pp.495–497, distributions and temperature; §12.5 printed pp.679–682, activation energy and temperature-dependent energetic fraction.')
add('2-02',[
 'Raising temperature broadens the energy distribution and increases the fraction above a fixed activation-energy threshold.',
 'Higher temperature also increases average speed and collision frequency, but a full qualitative rate explanation includes the increased energetic fraction.',
 'Heating does not lower activation energy for an unchanged reaction pathway.'
], 'Why heating usually increases rate strongly', '''Raising temperature increases average particle kinetic energy. On a Boltzmann diagram for the same number of particles, the higher-temperature curve is broader with a lower peak shifted towards higher energy. The total area stays the same. It is not a translation of an unchanged curve, and it does not mean that all particles acquire one identical energy.

For an unchanged pathway, Ea remains at the same position on the energy axis. The higher-temperature distribution has a larger area to the right of that threshold. A greater fraction of the particles can therefore take part in collisions with sufficient energy. This is the central energetic explanation for a strong increase in rate. Heating gives particles a wider spread including more energetic particles; it does not lower the barrier they need to cross.

Average particle speeds also increase, so collisions generally become more frequent in a controlled comparison at fixed concentration or number density. A complete qualitative explanation links both effects to successful collisions: encounters are more frequent, and a greater fraction have adequate energy. Saying only that collisions happen more often leaves out the distribution change. Saying only that particles “have more energy” does not identify the significant fraction above Ea.

When comparing curves, keep the same particle number and the same pathway threshold. If the particle number differs, area changes cannot be assigned to temperature alone. Cooling reverses the distribution effect and ordinarily slows the reaction, but does not require the reaction to stop completely. For enzyme-catalysed reactions, excessive heating can damage the catalyst, so their high-temperature behaviour needs the additional structural explanation given later. The Boltzmann comparison assumes that the reacting system and its pathway remain otherwise comparable. Such a comparison does not determine a numerical rate factor without further experimental information.''',
 '§12.5 printed pp.679–682; §9.5 printed pp.495–497. Qualitative distribution interpretation, without out-of-scope rate-equation derivations.')
add('3-01',[
 'A catalyst increases rate through an alternative pathway of lower activation energy and is regenerated overall.',
 'A catalyst may participate in individual steps even though it is absent from the net reaction equation.',
 'At fixed temperature a catalyst changes approach to equilibrium, not the equilibrium constant or composition.'
], 'What a catalyst changes', '''A catalyst is a substance that increases reaction rate by providing an alternative pathway of lower activation energy and is regenerated overall. It can participate in individual steps, but it is not permanently consumed in the net reaction. “Regenerated overall” is more precise than saying that it takes no part in the reaction.

The original reactants and products are the same with and without a suitable catalyst. The route between them is different. A lower barrier allows more reaction events at the same temperature without requiring an increase in average particle energy. Some catalysts enable a reaction to proceed at a useful rate where the uncatalysed change is too slow to observe conveniently.

On a reaction-pathway profile, retain the same reactant and product levels and draw a lower barrier for the catalysed route. The reaction enthalpy, the difference between endpoints, stays unchanged. A catalyst does not supply the net energy released by an exothermic reaction or turn an endothermic reaction into an exothermic one. Do not confuse a lower barrier with a lower product enthalpy.

At fixed temperature, a suitable catalyst speeds the approach to equilibrium through forward and reverse processes. It does not alter the equilibrium constant or the final composition at that temperature. A larger product amount after a short fixed time can show a faster approach, while the fully adjusted mixture remains the same. This is the connection to the industrial rate/yield compromise in Topic 2.3.

To test catalysis, compare otherwise equivalent experiments, controlling temperature, initial amounts and the physical setup. A change in temperature caused by another process can also change rate and must be separated from the catalyst's action. A small amount of catalyst may serve many reaction cycles, but practical loss, poisoning or structural damage can reduce its usefulness without making it a stoichiometric reactant in the ideal net equation.''',
 '§12.7, printed pp.689–691 (PDF pp.699–701), alternative route and regeneration; §13.3 catalyst at fixed temperature.')
add('3-02',[
 'A homogeneous catalyst is in the same phase as the reacting species; a heterogeneous catalyst is in a different phase.',
 'Heterogeneous catalytic reactions can occur at surface sites where reactants adsorb and products later leave.',
 'Catalyst classification concerns phase, not whether a catalyst is biological or how fast it acts.'
], 'Homogeneous and heterogeneous catalysis', '''Homogeneous catalysis uses catalyst and reacting species in the same phase. They may all be gases or be dissolved in one liquid phase. The comparison concerns phase, not whether the material looks uniform to the unaided eye. A dissolved catalyst and dissolved reactants occupy the same solution phase even when their solutes have different names.

Heterogeneous catalysis uses a catalyst in a different phase from the reactants. A solid catalyst with gaseous reactants is a common arrangement. Reactants reach its surface and adsorb at suitable sites, meaning that they become associated with the surface. Reaction through the surface pathway is followed by product departure, or desorption, leaving sites available for another cycle. A catalyst can therefore be regenerated at a surface without being dissolved into the reaction mixture.

For a fixed mass of solid catalyst, greater accessible surface area can provide more sites, provided the same kind of active surface is exposed and other factors are comparable. Surface coverage by an unwanted substance can block sites and reduce activity. These ideas explain why the physical form and cleanliness of a heterogeneous catalyst can matter; simply calling it a solid does not explain the rate effect.

The homogeneous/heterogeneous distinction does not state which catalyst must be faster. Rate depends on the actual pathway and experimental setting. Nor does it mean a homogeneous catalyst is consumed while a heterogeneous one is regenerated: regeneration applies to catalysts in both classes. Identify the phases explicitly in a classification answer. For instance, a gaseous catalytic species reacting with gases is homogeneous, while a solid metal surface reacting with gases is heterogeneous. Topic 4.2 includes examples involving a metal surface in hydrogenation; here the purpose is to explain the phase relationship and surface cycle rather than to memorise an industrial recipe.''',
 '§12.7, printed pp.691–696 (PDF pp.701–706), homogeneous and heterogeneous catalysis and adsorption.')
add('3-03',[
 'At the same temperature, a catalyst does not alter the Boltzmann energy distribution but supplies an alternative route with a lower Ea.',
 'Moving the threshold to lower energy increases the area representing particles energetic enough for that route.',
 'A catalysed pathway may contain intermediate stages; the energy threshold changes because the mechanism differs.'
], 'Catalysis on a Boltzmann diagram', '''A catalyst changes the reaction mechanism and supplies a pathway with a lower activation energy. Keep the temperature fixed when explaining this effect. The particles' Boltzmann energy distribution then remains the same; the catalyst does not make the collection hotter or raise its average kinetic energy.

On one distribution curve, mark an uncatalysed threshold farther right and a catalysed threshold farther left. The area beyond the lower threshold is greater. More of the existing particles therefore have sufficient energy for the alternative route, increasing the frequency of successful reaction events. The change is in which energies are sufficient, rather than in the energy population itself.

![Generated single-temperature distribution showing lower catalysed and higher uncatalysed Ea](assets/8224-boltzmann-catalyst.png)

For a construction task, label both axes, draw a distribution with a high-energy tail and place both Ea lines unambiguously. Distinguish the two thresholds in the key. Shading between the lines can identify the additional energetic population now able to use the lower-barrier route. The full energetic population for that route includes this extra region and the tail beyond the original barrier. A label pointing to an area should describe particles, not give that area the name of an energy value.

The same catalyst can be represented on a pathway profile by a lower route between unchanged endpoints. Such a profile may have more than one stage and intermediates, but it is a different kind of diagram from the Boltzmann distribution. Do not invent an electron-transfer intermediate merely to fill a diagram label; its actual identity depends on the chemical mechanism. For this qualitative comparison the required evidence is the lower route and the greater fraction above its threshold. The two diagrams explain complementary aspects of one catalytic effect.''',
 '§12.7 printed pp.689–691, different pathway; §12.5 pp.679–682 energetic fraction; distribution threshold comparison derived from these principles.')
add('3-04',[
 'Enzymes are biological catalysts; many are proteins with an active site that interacts with substrate.',
 'Enzyme specificity reflects the match between substrate and active-site features; some enzymes accept a related range of substrates.',
 'An enzyme is regenerated after product release rather than becoming a permanent part of the product.'
], 'Biological catalysts and specificity', '''Enzymes are biological catalysts. Many are proteins whose folded structure provides an active site that interacts with a reacting molecule, called the substrate. The substrate associates with the active site, reacts by the catalysed pathway and leaves as product. The enzyme becomes available for another catalytic cycle.

Specificity means an enzyme can favour a particular substrate or kind of reaction. Shape and chemical interactions at the active site help select and position suitable substrates. A random molecule with an unsuitable shape or charge arrangement may not interact productively with that site. Specificity is therefore a chemical explanation for selectivity, not a claim that a catalyst can choose consciously.

A simple sequence is enzyme + substrate → enzyme–substrate complex → enzyme + product. This describes temporary association and regeneration. It does not mean the enzyme is used up in the first stage. A useful model shows that active-site and substrate features must match; it should not imply that an enzyme is an entirely rigid object or that one enzyme necessarily accepts exactly one molecule type. Some catalyse changes in a related range of substrates.

For an application question, connect an observed selectivity to this site–substrate interaction. If an enzyme catalyses conversion of substrate S but not a similarly tested molecule T at the same pH and temperature, a reasonable explanation is that T lacks a suitable interaction with the active site. The result does not prove T could not react by any other route or with another catalyst. Enzymes share the general catalytic principle of a lower-energy pathway; their structural selectivity adds a reason for controlling the biological catalyst's surroundings. Their operating range is developed next.''',
 '§12.7, printed pp.696–697 (PDF pp.706–707), enzyme active site and specificity; Organic Chemistry Tenth Edition Study Guide, printed p.140, enzyme specificity and catalysis.')
add('3-05',[
 'Enzyme activity depends on temperature and pH because these can affect molecular motion and active-site structure or interactions.',
 'Moderate heating can increase enzyme-catalysed rate, but sufficiently high temperature can denature a protein enzyme and lower activity.',
 'Low-temperature slowing does not by itself establish denaturation; the useful pH and temperature ranges depend on the enzyme.'
], 'Why pH and temperature need control', '''An enzyme-catalysed reaction works effectively within a suitable pH and temperature range. The range depends on the enzyme and the process. Do not assign a single useful pH or temperature to biological catalysts as a group. An experiment needs the values appropriate to its named or supplied enzyme rather than an assumed body-temperature setting.

Initially, increasing temperature can raise particle speeds and the energetic fraction for the catalysed pathway, increasing rate. If heating becomes sufficient to disrupt a protein enzyme's folded structure, the active site can lose the shape or interactions needed for effective binding and catalysis. This loss of the working structure is denaturation. A falling rate at high temperature can therefore reflect catalyst damage rather than a reversal of the ordinary collision-energy effect.

Cooling ordinarily slows molecular encounters and reaction without itself demonstrating permanent structural damage. Distinguish low activity because particles react more slowly from loss of activity because the catalyst's structure has changed. Returning a cooled sample to a suitable temperature may restore its earlier activity, whereas recovery after damaging heating cannot simply be assumed.

Changing pH alters protonation and the interactions that maintain the protein structure or allow substrate binding. Outside a suitable pH range, activity can fall, and sufficiently disruptive changes can denature the protein. Explain a pH effect through the active site's chemical environment rather than saying that acid or alkali automatically consumes an enzyme.

In a comparison, keep enzyme amount, substrate concentration and measurement interval consistent while varying the chosen temperature or pH. State whether rate is measured promptly or after a long heat exposure, since damage can develop over time. A peak in a rate–temperature dataset reflects both reaction kinetics and the enzyme's stability in that experiment; it is not a universal fixed temperature for the molecule independent of procedure.''',
 'Organic Chemistry Tenth Edition Study Guide, printed pp.139–140, protein structure, denaturation by pH/temperature and enzymes; syllabus §2.4.3 pH/temperature restriction.',source='OpenStax-Organic-Chemistry-Study-Guide')

# Dimensionless energy coordinates: normalized f(E) = 2 sqrt(E) exp(-E/T)/(sqrt(pi) T^(3/2)).
# Both curves integrate to one over E>=0. The display is a bounded schematic of the high-energy tail.
def dens(e,temp):return 2*math.sqrt(e)*math.exp(-e/temp)/(math.sqrt(math.pi)*temp**1.5)
assets=t.dir/'assets'
def base(title,desc):
 f=Figure(title,desc);f.arrow((80,355),(790,355));f.arrow((80,355),(80,100));f.text(25,70,'Number of particles per energy interval',17);f.text(610,383,'Energy',20);return f
def point(e,temp):return (80+43*e,355-1050*dens(e,temp))
f=base('Boltzmann distribution: effect of temperature','Normalized energy distributions at relative temperatures 2 and 3 with the same total particle number. Higher temperature has a broader lower peak and larger fraction above the unchanged threshold at relative energy 6. Schematic axes, not an experimental dataset.')
for temp,col in [(2,'#176e9a'),(3,'#a13922')]:
 pts=[point(k/25,temp) for k in range(401)];f.line(pts,col,3)
f.line([(338,355),(338,145)],'#66747b',2);f.text(331,363,'Ea',19)
f.text(160,130,'Lower T',18,'#176e9a');f.text(235,188,'Higher T',18,'#a13922')
f.text(390,224,'Area beyond Ea:',18);f.text(390,252,'larger at higher temperature',18)
for e in [6+k*.1 for k in range(101)]:f.line([point(e,3),(80+43*e,355)],'#e1b7a9',1)
f.line([point(k/25,3) for k in range(401)],'#a13922',3)
f.text(25,423,'Same particle number; same pathway. Ea stays fixed.',18)
f.save('8224-boltzmann-temperature',out=assets)
f=base('Boltzmann distribution: effect of a catalyst','One normalized energy distribution at fixed relative temperature 2.5. The catalysed threshold is at energy 4 and uncatalysed at 7. The extra region between thresholds represents additional particles energetic enough for the lower-barrier route.')
for e in [4+k*.1 for k in range(30)]:f.line([point(e,2.5),(80+43*e,355)],'#bad8c0',1)
f.line([point(k/25,2.5) for k in range(401)],'#176e9a',3)
for e,label,yy in [(4,'Ea catalysed',367),(7,'Ea uncatalysed',395)]:
 x=80+43*e;f.line([(x,355),(x,145)],'#66747b',2);f.text(x-65,yy,label,18)
f.text(440,150,'Same curve at fixed T',20);f.text(440,185,'Lower threshold:',18);f.text(440,212,'greater energetic fraction',18)
f.text(25,423,'Shaded interval adds particles; energy is the horizontal coordinate.',17)
f.save('8224-boltzmann-catalyst',out=assets)

s=t.wo['item_slots']
qa=[
 ('Describe a concentration-based reaction rate, its time basis and a suitable unit. [3]','Change in a stated reactant or product concentration [1] per unit time [1], for example mol dm⁻³ s⁻¹ [1].'),
 ('Explain why a falling reactant concentration gives a positive disappearance rate when written as −Δ[reactant]/Δt. [2]','Consumption makes Δ[reactant] negative [1]; the leading minus sign converts that decrease into the positive disappearance-rate magnitude [1].'),
 ('Describe how increasing reactant concentration can increase rate in a simple collision-controlled reaction at constant temperature. [3]','There are more reacting particles per unit volume [1], causing more frequent encounters [1] and more successful collisions per second [1].'),
 ('Explain why higher concentration can increase rate without raising particle energy when temperature is fixed. [2]','More particles per unit volume increase collision frequency [1]; the energy distribution is unchanged at fixed temperature, so the increase comes from more encounters [1].'),
 ('Describe activation energy and its representation on a Boltzmann distribution, including the meaning of the area beyond it. [3]','Ea is the minimum collision energy required for reaction [1]; it is marked on the energy axis as a threshold [1]; the area beyond it represents particles with sufficient energy [1].'),
 ('Explain why a collision can fail to react even when particles meet. [2]','Its energy may be below the activation threshold [1], or its orientation may be unsuitable for the required rearrangement [1].'),
 ('Explain why a reaction-pathway profile is not an answer to a request for a Boltzmann distribution, using the axes as a discriminating test. [2]','A pathway profile has enthalpy versus progress of reaction [1]; a Boltzmann distribution needs particle population per energy interval versus energy [1].'),
 ('Explain the error in labelling the right-hand area under a Boltzmann curve “activation energy”. [2]','Ea is an energy value on the horizontal axis [1]; the area beyond its threshold represents the number or fraction of particles energetic enough, not an energy [1].'),
 ('Describe three effects relevant to a higher-temperature Boltzmann comparison with the same number of particles and the same pathway. [3]','The curve broadens with a lower peak at higher energy [1]; a greater fraction lies above the fixed Ea [1]; increased average speeds also increase collision frequency in a fixed-density comparison [1].'),
 ('Explain why heating usually increases rate, using energy distribution and collisions. Keep concentration and the reaction pathway unchanged. [2]','The fraction above the unchanged Ea increases [1]; faster particles also collide more frequently, increasing successful collisions per second [1].'),
 ('Explain why “heating increases rate because collisions are more frequent” is incomplete for an unchanged pathway. [2]','It omits the energy-distribution change [1]: a greater fraction has energy at least Ea, so a greater fraction of encounters can react [1].'),
 ('Describe a catalyst through its pathway, activation energy and fate overall. [3]','It provides an alternative reaction pathway [1] with lower activation energy [1] and is regenerated overall [1].'),
 ('Explain why a catalyst can appear in an intermediate step but not in the net reaction equation. [2]','It participates temporarily in the steps [1]; because it is regenerated later, it cancels when the steps are added [1].'),
 ('Describe homogeneous and heterogeneous catalysts and the basis of their distinction. [3]','A homogeneous catalyst shares the reactants’ phase [1]; a heterogeneous catalyst is in another phase [1]; classification concerns phase rather than rate or biological origin [1].'),
 ('Explain how a solid catalyst can act repeatedly with gaseous reactants at its surface. [2]','Reactants associate with surface sites and react through that route [1]; products leave, making the sites available again [1].'),
 ('Describe a catalyst’s effect on the Boltzmann distribution and energy threshold at fixed temperature. [3]','The distribution curve stays the same [1]; the alternative pathway has a lower Ea [1]; a larger fraction of the existing particles has sufficient energy [1].'),
 ('Explain why a catalyst raises rate without increasing the average kinetic energy at fixed temperature. [2]','It provides a lower-Ea pathway [1]; because more of the unchanged energy distribution lies above that threshold, more encounters can react [1].'),
 ('Draw one labelled Boltzmann distribution at fixed temperature, with separate catalysed and uncatalysed Ea thresholds. Show which threshold gives more particles with sufficient energy. [2]','A correct sketch has energy horizontally, particle population per energy interval vertically, and one rising then falling long-tailed curve [1]; the catalysed Ea lies left of the uncatalysed Ea, with a greater area beyond the lower threshold [1].\n\n![Generated model showing one distribution and two thresholds](assets/8224-boltzmann-catalyst.png)'),
 ('State what an enzyme is. [1]','A biological catalyst [1].'),
 ('Suggest why an enzyme converts substrate S but not molecule T in comparable tests at the same suitable pH and temperature. [1]','Its active-site features interact suitably with S but not T [1], giving substrate specificity.'),
 ('Describe how temperature, damaging heat and pH can affect a protein enzyme’s activity. [3]','Moderate warming can raise rate through particle-energy effects [1]; sufficiently high heat can disrupt active-site structure and lower activity [1]; unsuitable pH can alter active-site interactions or structure [1].'),
 ('Explain why a protein enzyme can show low activity after damaging heat even when reactant collisions would otherwise be faster. [2]','The heat can denature the protein and alter its active site [1]; because substrate interaction/catalysis is impaired, the catalyst loses activity despite faster particle motion [1].')
]
assert len(qa)==len(s)
for slot,(prompt,answer) in zip(s,qa):
 st='WHY' if slot['subtype']=='MECH' else None
 t.item(slot,prompt,answer,subtype=st)
 if st:t.deviations.append({'from':slot['slot']+' MECH','to':'WHY; preserve AO/Bloom/command/tariff','why':'The objective requires kinetic, population or structural reasoning, rather than a specific electron-movement reaction mechanism with a named intermediate and product.'})
p=t.wo['performance_tasks']
t.item(p[0],'''Identify one correct option per question. [6]
1. A gas volume rises by 18.0 cm³ over 15.0 s. Average rate is: A 270 cm³ s⁻¹; B 1.20 cm³ s⁻¹; C 0.833 cm³ s⁻¹; D 18.0 cm³ s⁻¹.
2. At unchanged temperature, higher reacting concentration mainly raises: A Ea; B mean kinetic energy; C encounters per unit volume per second; D the energetic fraction for an unchanged barrier.
3. Ea on a Boltzmann diagram is: A an energy-axis threshold; B the entire area; C the vertical population maximum; D the time at the curve peak.
4. At higher temperature for the same pathway and particle number: A Ea moves left; B all particles have identical energy; C total particle area increases; D the fraction above Ea increases.
5. A productive collision needs: A suitable orientation alone; B suitable orientation and sufficient energy; C equal particle masses; D a catalyst in every reaction.
6. The instantaneous rate on a product-volume/time curve comes from: A the final volume alone; B total time alone; C the tangent gradient at the chosen time; D the curve height divided by temperature.''',
 '''Key: 1 B, 2 C, 3 A, 4 D, 5 B, 6 C; one mark per correct option.
1. B follows 18.0/15.0 = 1.20. Distractor A multiplies; C reverses the ratio; D omits time.
2. C follows more reacting particles per unit volume. A changes the pathway barrier without reason; B assigns an energy change at fixed temperature; D mistakes a concentration effect for a temperature effect.
3. A is an energy value. B confuses particle number with energy; C confuses peak population with a threshold; D uses an absent time axis.
4. D follows the broader higher-energy distribution. A describes a lowered pathway barrier; B removes the distribution; C changes the number of particles.
5. B includes both requirements. A omits energy; C invents an equal-mass requirement; D incorrectly makes catalysis necessary to reaction itself.
6. C gives the local change per time. A is an amount measure; B omits the change; D divides by the wrong variable.''')
t.item(p[1],'''Explain the kinetics using the linked parts. [8]
(a) A concentration falls from 0.120 to 0.0800 mol dm⁻³ in 20.0 s. Calculate average disappearance rate, giving three significant figures. [2]
(b) Explain how increasing reacting concentration can increase rate at fixed temperature in a simple collision-controlled comparison. [2]
(c) Describe Ea and identify what the area beyond it means on a Boltzmann diagram. [2]
(d) Explain how heating at unchanged concentration and pathway increases rate, including both energetic fraction and collision frequency. [2]''',
 '''Part (a): rate = (0.120 − 0.0800)/20.0 [1]; answer 0.00200 mol dm⁻³ s⁻¹ to three significant figures [1], treating the stated concentrations at the supplied precision.
Part (b): more reactant particles occur per unit volume [1], increasing encounter frequency and successful collisions per second [1].
Part (c): Ea is the minimum collision-energy threshold [1]; the area beyond it represents particles with sufficient energy [1].
Part (d): a greater fraction has energy at least the unchanged Ea [1], while higher speeds increase collision frequency in the fixed-concentration comparison [1]. Each bracket is a separate creditworthy point.''')
t.item(p[2],'''Calculate and interpret the rates from original data collected with the same apparatus. At temperature T1, a reaction produces 36.0 cm³ gas in 30.0 s; a second mixture at T1 with greater reacting concentration produces 54.0 cm³ in 30.0 s. Use these intervals as average-rate measurements. [5]
(a) Calculate both rates and their ratio, to three significant figures. [3]
(b) State which particle-level frequency change can explain the concentration result at unchanged T1. [1]
(c) A separate run is heated at unchanged concentration and pathway. State how the fraction above Ea changes. [1]''',
 '''(a) Equation: average volume rate = ΔV/Δt. First rate = 36.0/30.0 = 1.20 cm³ s⁻¹ [1]; second = 54.0/30.0 = 1.80 cm³ s⁻¹ [1]; ratio second/first = 1.80/1.20 = 1.50, dimensionless [1]. Three significant figures follow the supplied data; no conversion is needed because both times are seconds and volumes cm³.
(b) Encounter frequency per unit volume increases with the reacting concentration in this model [1].
(c) The fraction with energy at least the unchanged Ea increases [1], aiding successful collisions. The concentration run did not itself require such an energetic-fraction change.''')
t.deviations.append({'from':'Absolute wording that enzyme reactions only work at specific conditions','to':'Teach enzyme-dependent useful pH/temperature ranges and distinguish slowing from denaturation','why':'A single universal pH or temperature is not implied; the syllabus wording describes controlled operating requirements rather than a mathematical on/off point.'})
t.save()
