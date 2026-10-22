"""Original energetic principles, numerical examples and work-order practice."""
from authoring_common_8224 import Topic
from render_chemistry_visuals_8224 import Figure

t=Topic('2.1')
def add(short,claims,title,text,locator):
    t.objective(short,claims,[(title,text)],'OpenStax-Chemistry',locator)

add('1-01',[
 'At constant pressure, an exothermic reaction transfers heat to its surroundings and has negative reaction enthalpy change.',
 'An endothermic reaction absorbs heat from its surroundings and has positive reaction enthalpy change.',
 'Reaction enthalpy change is the enthalpy of the products minus that of the reactants for the stated reaction.'
], 'Following energy across the system boundary', '''A chemical reaction rearranges atoms and changes the interactions between them. Energy is transferred as the reacting system changes into products. For this topic, focus on heat transfer at constant pressure. The reacting substances are the system; the solution, apparatus and wider environment may act as surroundings. Choose the boundary before interpreting a temperature change. Energy transferred out of the reacting system is gained elsewhere rather than destroyed.

Enthalpy change is written ΔH, read as “change in enthalpy”. For a stated reaction, ΔH = H(products) − H(reactants). In an exothermic reaction the products have lower enthalpy than the reactants. Heat passes from the reacting system to its surroundings and ΔH is negative. A temperature rise in a surrounding solution can therefore indicate an exothermic reaction. The positive temperature change of that solution and the negative enthalpy change of the reaction describe opposite sides of the same energy transfer.

In an endothermic reaction the products have higher enthalpy. The reacting system absorbs heat and ΔH is positive. Its surroundings may cool as they supply that heat. An observed temperature decrease does not mean energy has vanished. It indicates transfer into the reacting system, provided other thermal effects are accounted for.

The sign of ΔH does not by itself give a reaction rate. A reaction may release heat overall yet need heating to get started. The energy barrier and the overall enthalpy change are different quantities, connected later by reaction-pathway diagrams. A large negative ΔH also does not imply a large measured temperature rise without knowing how much reacts, the mass being warmed and the apparatus heat capacity. State the amount basis whenever quoting a heat change, and distinguish the reaction's energy transfer from a temperature reading.''',
 '§§5.1–5.3, printed pp.228–234 and 244–255; constant-pressure heat and sign convention.')

add('1-02',[
 'A standard reaction enthalpy change refers to the stated equation with substances in their standard states at standard pressure and a specified temperature.',
 'Standard enthalpy of formation forms one mole of compound from its elements in their standard states; standard enthalpy of combustion completely burns one mole of substance in oxygen.',
 'Hydration transfers one mole of gaseous ions into aqueous solution; solution dissolves one mole of solute to the specified final solution; neutralisation forms one mole of water by acid–base reaction.',
 'Atomisation forms one mole of gaseous atoms from an element in its standard state; bond dissociation enthalpy breaks one mole of a specified gaseous covalent bond and is positive.'
], 'Naming the process and its amount basis', '''Standard enthalpy change is the enthalpy change when reactants and products are in their standard states at standard pressure and a specified temperature. A standard state specifies a reference physical form at standard pressure, 100 kPa, and a stated temperature, commonly 298 K. For solutions, the usual school reference concentration is 1 mol dm⁻³ where applicable. The superscript ° identifies the standard reference. Temperature must still be specified; the symbol does not mean that every measurement was made at 298 K.

Standard enthalpy change of formation, ΔH°f, forms one mole of a compound from its constituent elements in their standard states. For water at 298 K, H2(g) + ½O2(g) → H2O(l) has the correct one-mole basis. Using gaseous water describes a different product state. Forming two moles requires twice the enthalpy change. An element in its standard state has standard enthalpy of formation zero by convention; that does not mean it contains no energy.

Standard enthalpy change of combustion, ΔH°c, is the change when one mole of a substance burns completely in oxygen with substances in their standard states. For methane, CH4(g) + 2O2(g) → CO2(g) + 2H2O(l). Distinguish complete combustion from partial oxidation and retain the state of water. Standard enthalpy change of neutralisation refers to acid and base reacting to form one mole of water: H+(aq) + OH−(aq) → H2O(l) is the net ionic equation for dilute strong acid and strong alkali.

Enthalpy change of hydration transfers one mole of gaseous ions into aqueous solution, for example Na+(g) → Na+(aq), at the stated reference setting. Enthalpy change of solution dissolves one mole of solute to form the specified solution, often treated as sufficiently dilute that further dilution has negligible heat effect. For example NaCl(s) → Na+(aq) + Cl−(aq) describes solution rather than hydration. The starting lattice distinguishes those processes. Hydration of ions releases energy; the net solution process can have either sign because separating solute particles also requires energy.

Standard enthalpy change of atomisation forms one mole of gaseous atoms from an element in its standard state, as in ½Cl2(g) → Cl(g). Bond dissociation enthalpy instead refers to breaking one mole of specified covalent bonds in gaseous species: Cl2(g) → 2Cl(g) breaks one mole of Cl–Cl bonds but forms two moles of gaseous atoms. Bond breaking requires energy and has positive ΔH. The “one mole” object, starting state and final state are part of each definition; a process name alone cannot replace them. Thermochemical standard states differ from gas-volume reference settings: Topic 1.1 uses s.t.p. and r.t.p. for its separate molar-volume approximations.''',
 '§5.3, printed pp.255–260, standard states/formation/combustion; §7.5 pp.364–365, gaseous bond dissociation; §11.1, dissolution and solvation. Hydration/solution/neutralisation/atomisation terminology is syllabus §2.1.1; amount bases derived from the written processes.')

add('1-03',[
 'A solution heat change is qsolution = mcΔT; under negligible heat exchange elsewhere, qreaction = −mcΔT.',
 'A molar reaction enthalpy change requires dividing the reaction heat by the amount corresponding to the stated reaction basis.',
 'Heat loss and calorimeter heat capacity can make a simple solution-only calorimetric result less exothermic than the true value.'
], 'From a measured temperature change to a molar enthalpy', '''Calorimetry relates a temperature change to heat transfer. For the solution use qsolution = mcΔT, where m is the mass warmed, c is its specific heat capacity and ΔT = Tfinal − Tinitial. With m in grams and c in J g⁻¹ K⁻¹, the result is joules. A change of one degree Celsius has the same size as a change of one kelvin, so either scale gives the same temperature difference. This does not permit Celsius temperatures in gas-law ratios.

If heat transfer to the vessel and the wider surroundings is negligible, qreaction = −qsolution = −mcΔT. The syllabus shorthand ΔH = −mcΔT describes the heat change for the reacting sample under this constant-pressure approximation. To report a molar value, divide by the amount on the equation's chosen basis and convert J to kJ. Identify the limiting reactant or the amount of water formed rather than dividing automatically by the total moles mixed.

Consider 60.0 g of solution warming by 5.00 K when 0.0250 mol of water forms in a neutralisation. With c = 4.18 J g⁻¹ K⁻¹, qsolution = 60.0 × 4.18 × 5.00 = 1254 J. Hence qreaction = −1.254 kJ and ΔHneut = −1.254/0.0250 = −50.16 kJ mol⁻¹. Report −50.2 kJ mol⁻¹ to three significant figures. The negative sign agrees with warming of the surroundings. The amount basis is one mole of water formed.

Use the total solution mass when both mixed solutions warm. If mass is inferred from volume, state the assumed density. Approximating a dilute aqueous solution's heat capacity by that of water must also be stated. Heat absorbed by the cup or lost during an exothermic reaction reduces the measured temperature rise; ignoring it gives a magnitude that is too small. These limitations explain a discrepancy without changing the arithmetic sign convention.''',
 '§5.2, printed pp.239–245, especially pp.244–245; example data and arithmetic original.')

add('1-04',[
 'Breaking chemical bonds requires an energy input; making the same bonds releases energy.',
 'A reaction is exothermic when bond formation releases more energy than is required for bond breaking.',
 'The complete-separation bond-energy route is a bookkeeping path and need not be the actual molecular reaction mechanism.'
], 'Breaking and making bonds', '''A stable chemical bond holds atoms together at a lower energy than the corresponding separated atoms. Energy must be supplied to separate them. Bond breaking is therefore endothermic. Forming that same bond from the separated gaseous atoms releases energy and is exothermic. The forward and reverse changes have opposite signs when their endpoints are identical.

For a reaction, consider the energy needed to break the relevant bonds in reactants and the energy released when bonds form in products. If bond formation releases more than bond breaking requires, the net change is negative. If breaking requires more than formation releases, the net change is positive. The reactants can need an initial energy input even when the overall process is exothermic. Do not describe fuels as releasing energy because their bonds are broken: the net release depends on the stronger total bonding established in the products relative to the energy input.

For example, forming two H–Cl bonds from separated atoms releases energy, while separating H2 and Cl2 into atoms first requires energy. Adding the two stages gives the overall enthalpy change for H2(g) + Cl2(g) → 2HCl(g). The calculation uses an imagined path through separated gaseous atoms. It does not establish that the real reaction first converts an entire sample into isolated atoms. A reaction mechanism describes actual steps; an energy bookkeeping path need only have the correct endpoints.

Keep chemical bonds separate from attractions between molecules. Vaporising liquid water involves overcoming intermolecular attractions while the O–H covalent bonds remain intact. Separating gaseous water into H and O atoms requires bond breaking and is a different change. When an energy question includes changes of physical state, include those transfers separately or use thermochemical data that already describe the stated phases.''',
 '§7.5, printed pp.364–368; §5.3 Hess-law state-function reasoning.')

add('1-05',[
 'For a gaseous bond-energy route, estimated ΔH equals the sum of bond energies for bonds broken minus the sum for bonds formed.',
 'Bond counts must include stoichiometric coefficients and distinguish single, double and triple bonds.'
], 'Counting bonds before substituting numbers', '''Bond-energy estimates use ΔH ≈ ΣE(bonds broken) − ΣE(bonds formed). The tabulated bond energies are positive dissociation values. Subtract the total for product bond formation because forming those bonds releases energy. Begin with a balanced equation and identify the bonds in each molecule. Multiply each bond count by both the number of such bonds in one molecule and the stoichiometric coefficient. A molecular subscript counts atoms, while a coefficient multiplies the whole molecule.

For H2(g) + Cl2(g) → 2HCl(g), take the supplied bond energies H–H = 436, Cl–Cl = 243 and H–Cl = 432 kJ mol⁻¹. Break one mole of H–H bonds and one mole of Cl–Cl bonds: the input is 436 + 243 = 679 kJ for the equation as written. Form two moles of H–Cl bonds: the release has magnitude 2 × 432 = 864 kJ. Thus ΔH ≈ 679 − 864 = −185 kJ mol⁻¹ of reaction, or −185 kJ when one mole of H2 reacts as written. It is an estimate to the nearest kJ from the supplied whole-number bond data.

If the question asks for the enthalpy per mole of HCl formed, divide that result by two. This is a change of amount basis, not a different reaction pathway. Do not double the reactant bond energies just because two product molecules appear. Balance atoms first, then count the actual bonds.

For larger molecules, a displayed structure helps identify bond types and numbers. A double bond is represented by its own bond-energy value, not twice a single-bond value. Bonds appearing unchanged on both sides can cancel in the energy sum, provided the approximation treats them as equivalent. Give the sign, the unit and the equation basis with the answer. A bare positive number described as “energy released” should be distinguished from the negative ΔH assigned to the reaction.''',
 '§7.5, printed pp.364–368, Table 7.2 and bond-energy calculation method; example uses cited table values in original worked sequence.')

add('1-06',[
 'Mean bond enthalpies average gaseous bond-breaking values across molecular environments and therefore usually give approximate reaction enthalpies.',
 'A measured or tabulated reaction enthalpy refers to specified substances and physical states; phase changes can account for differences from a gaseous bond estimate.',
 'Experimental heat transfer errors and approximation errors are distinct possible causes of disagreement.'
], 'Explaining differences between enthalpy values', '''A mean bond enthalpy is an average for a bond type in gaseous species. The exact energy of a bond depends on its molecular environment, including the other atoms bonded nearby. Replacing a specific bond value by a mean therefore introduces an approximation. Even perfectly counted bonds and accurate arithmetic may give an estimate different from a tabulated reaction enthalpy for particular compounds.

Physical state matters as well. A bond-energy route commonly describes gaseous molecules. A measured combustion enthalpy may instead form liquid water. Condensation releases additional energy, so the liquid-water result is more exothermic than the corresponding gaseous-water result with other endpoints unchanged. Before comparing numbers, check that both describe the same balanced equation, amount basis, temperature and states. Different endpoints cannot be treated as competing measurements of exactly the same change.

For an illustrative comparison, suppose an estimate for a specified gaseous reaction is −190 kJ mol⁻¹ and a more specific value for the same endpoints is −204 kJ mol⁻¹. The magnitude of their difference is |−190 − (−204)| = 14 kJ mol⁻¹. Relative to the specific value, the percentage discrepancy is 14/204 × 100 = 6.86%, or 6.9% to two significant figures. This arithmetic quantifies disagreement; it does not prove which molecular approximation caused it. Evidence about bond values or endpoint states is still needed for the explanation.

A school calorimetry result adds a further issue: heat lost to the environment, heat absorbed by apparatus, incomplete combustion or an uncertain mass can affect its accuracy. Choose an error that fits the experiment and state its direction where supported. Repeating a heat-loss experiment may improve consistency without removing the systematic underestimate. Keep a bond-average limitation separate from a measurement limitation, and avoid asserting that every difference must be experimental error.''',
 '§7.5, printed pp.364–368 (mean gaseous bond values); §5.2 pp.244–245 (calorimetric assumptions); §5.3 state-dependent enthalpies.')

add('2-01',[
 'Hess’s law states that the enthalpy change between the same initial and final states is independent of route.',
 'Reversing a thermochemical equation reverses the sign of its enthalpy change; multiplying an equation multiplies its enthalpy change by the same factor.',
 'An energy cycle calculation requires matching species, physical states and amounts at shared endpoints.'
], 'Constructing a Hess cycle', '''Hess's law allows a reaction enthalpy to be found through another route with the same starting and finishing states. Enthalpy is a state function: only the endpoints determine its change. Draw the target reaction first, then identify a common endpoint or a set of intermediate equations that cancels to give the target. Every arrow has a direction, a balanced transformation and its corresponding ΔH.

As an original numerical cycle, let A, B and C represent specified chemical states on the same amount basis. The direct A → C change is −120 kJ mol⁻¹, while A → B is −45 kJ mol⁻¹. The route A → B → C gives −120 = −45 + ΔH(B → C), so ΔH(B → C) = −75 kJ mol⁻¹. Going backwards from C to A would instead require +120 kJ mol⁻¹. The letters represent complete states, including any necessary reagents, rather than unbalanced elemental symbols.

![Original Hess cycle with A to C −120 and A to B −45 kJ mol⁻¹](assets/8224-hess-cycle.png)

For real chemical equations, reverse any equation used backwards and reverse its enthalpy sign. Multiply a step by two if two moles are required, including its ΔH. Add the equations and cancel identical species that occur on opposite sides. Check both atoms and physical states after cancellation. Two appearances of H2O with different state symbols cannot cancel without including the phase-change energy.

The cycle need not follow the actual molecular sequence. Its purpose is to connect thermochemical measurements without changing endpoints. An energy difference calculated by subtracting two routes is meaningful only when those routes share the proper states. Labelled arrows make the sign choice visible and prevent a memorised subtraction order from replacing chemical reasoning.''',
 '§5.3, printed pp.260–266; original numerical three-state cycle derived by energy conservation.')

add('2-02',[
 'Combustion enthalpies can determine a formation enthalpy by connecting the elements and the compound to identical complete-combustion products.',
 'For such a cycle, formation enthalpy equals the total combustion enthalpy of the required elements minus combustion enthalpy of the compound.'
], 'Finding an inaccessible formation enthalpy', '''A compound may not be obtainable cleanly from its elements in a direct experiment. Competing products, slow reaction or difficult heat collection can prevent a reliable direct formation measurement. Hess's law can connect separately measurable combustion enthalpies instead. Both routes must finish at the same products with matching states and amounts.

For methane the target is C(s, graphite) + 2H2(g) → CH4(g). Introduce enough oxygen so that both the elements and methane reach CO2(g) + 2H2O(l). Burning the elements separately gives the sum ΔH°c(C) + 2ΔH°c(H2). The alternative route first forms methane, then burns it. Therefore ΔH°f(CH4) + ΔH°c(CH4) = ΔH°c(C) + 2ΔH°c(H2). The oxygen is shared bookkeeping material and cancels from the final target equation.

Using rounded illustrative data −394 kJ mol⁻¹ for carbon combustion, −286 kJ mol⁻¹ for hydrogen combustion and −890 kJ mol⁻¹ for methane combustion, the calculation is ΔH°f(CH4) = −394 + 2(−286) − (−890) = −76 kJ mol⁻¹. Quote the answer to the nearest kJ, consistent with the supplied data. The target forms one mole of methane, so no further division by its hydrogen atom count is needed.

If a combustion datum forms steam while another forms liquid water, this simple cancellation fails. Include the appropriate vaporisation or condensation term before combining routes. Likewise, use graphite for carbon's standard state, rather than an unspecified carbon form. A correct numerical subtraction cannot repair mismatched states. After completing the cycle, rewrite its summed equation and check that it is precisely the desired formation equation.''',
 '§5.3, printed pp.255–266, standard formation and Hess-law methods; rounded illustrative combustion values and derived cycle.')

add('2-03',[
 'A reaction pathway diagram places enthalpy on the vertical axis and progress of reaction on the horizontal axis.',
 'Forward activation energy is the enthalpy difference from reactants to the pathway maximum; reaction enthalpy is the difference from reactants to products.',
 'For the same one-step profile, reverse activation energy equals forward activation energy minus forward reaction enthalpy.'
], 'Reading and constructing a pathway diagram', '''A reaction pathway diagram shows enthalpy vertically and progress of reaction horizontally. The horizontal coordinate is not elapsed time. Begin with a reactant level, draw a pathway rising to a maximum and then reaching the product level. For an exothermic process the product level is lower; for an endothermic process it is higher. Label both levels, both axes, the activation-energy interval and the reaction-enthalpy interval.

Activation energy is the minimum energy that colliding particles must have for a reaction to occur. On the pathway diagram its forward value is the vertical difference from the reactant level to the maximum, not from the bottom of the page. Reaction enthalpy is the vertical product-minus-reactant difference. These intervals measure different features, so the highest point does not give ΔH directly.

![Original exothermic reaction pathway with reactants at 0, maximum at 80 and products at −40 kJ mol⁻¹](assets/8224-enthalpy-pathway.png)

In this original illustrative profile the reactants are at 0, the maximum at +80 and the products at −40 kJ mol⁻¹ on a relative scale. The forward activation energy is 80 kJ mol⁻¹, while ΔH = −40 kJ mol⁻¹. Starting at the products for the reverse reaction requires a rise of 120 kJ mol⁻¹ to reach the same maximum. Thus Ea(reverse) = Ea(forward) − ΔH(forward). A negative forward ΔH increases the reverse barrier in this example. The zero is an arbitrary reference, not an assertion that reactants contain no energy.

For contrast, an endothermic profile could have reactants at 0, a maximum at +100 and products at +30 kJ mol⁻¹. Its forward activation energy is 100 kJ mol⁻¹, its ΔH is +30 kJ mol⁻¹ and its reverse activation energy is 70 kJ mol⁻¹. Both directions still have a positive barrier even though their enthalpy changes have opposite signs. These differences follow from the same three labelled levels; there is no need to place a negative activation-energy arrow on the diagram.

When constructing a sketch, numerical scales are unnecessary unless supplied or requested, but relative levels and arrow endpoints must be unambiguous. When interpreting a numerical profile, calculate the vertical differences rather than reading absolute labels as barriers. Topic 2.4 develops how activation barriers affect rate; the present diagram separates the overall heat change from the barrier that must be crossed.''',
 '§5.3 enthalpy levels; §12.5, collision theory and reaction energy diagrams (chapter 12). Original numerical profile and derived differences.')

assets=t.dir/'assets'
f=Figure('Hess cycle: the same initial and final states','Three complete states A, B and C. A to B is −45, A to C is −120 and B to C is unknown, all in kJ per mole on the same basis.')
f.text(110,100,'A',30);f.text(660,100,'C',30);f.text(385,330,'B',30)
f.arrow((155,120),(635,120));f.text(280,76,'−120 kJ/mol',22)
f.arrow((145,147),(370,325));f.text(60,249,'−45 kJ/mol',21)
f.arrow((430,325),(651,150));f.text(552,249,'Unknown',21)
f.text(40,402,'A → C = A → B + B → C. Arrow directions define the signs.',18)
f.save('8224-hess-cycle',out=assets)
f=Figure('Reaction pathway: an exothermic example','Relative enthalpy axis in kJ per mole; reactants at 0, maximum at 80, products at −40. Forward activation energy 80 and reaction enthalpy −40. Horizontal axis is progress, not time.')
f.arrow((85,360),(790,360));f.arrow((85,360),(85,70));f.text(25,55,'Enthalpy / kJ/mol',18);f.text(527,389,'Progress of reaction',18)
def y(h):return 255-h*1.75
pts=[(110,y(0)),(230,y(0)),(260,y(10)),(290,y(35)),(330,y(64)),(370,y(80)),(400,y(77)),(440,y(55)),(480,y(15)),(520,y(-20)),(555,y(-40)),(730,y(-40))]
f.line(pts,width=4);f.text(120,270,'Reactants: 0',18);f.text(562,334,'Products: −40',18);f.text(335,75,'Maximum: +80',18)
f.arrow((250,y(0)),(250,y(80)),'#176e9a',2);f.text(107,150,'Ea = 80',20,'#176e9a')
f.arrow((750,y(0)),(750,y(-40)),'#a13922',2);f.text(558,269,'ΔH = −40',20,'#a13922')
f.text(28,425,'Relative levels, not absolute stored energies. Original illustrative data.',17)
f.save('8224-enthalpy-pathway',out=assets)

s=t.wo['item_slots']
answers=[
 ('Describe an exothermic reaction in terms of heat transfer, product enthalpy and the sign of ΔH. [3]','Heat is transferred from the reacting system to its surroundings [1]; products have lower enthalpy than reactants [1]; ΔH is negative [1].'),
 ('Explain why a solution surrounding an exothermic reaction can warm while the reaction has negative ΔH. [2]','The reaction loses energy as heat, so its enthalpy change is negative [1]; because the solution gains this heat, its temperature rises [1].'),
 ('Describe standard enthalpy change of formation using its amount basis, starting materials and reference states. [3]','It forms one mole of compound [1] from its constituent elements [1] in their standard states at standard pressure and a specified temperature [1].'),
 ('Explain why Cl2(g) → 2Cl(g) is a bond-dissociation equation but is twice the atomisation equation for chlorine. [2]','It breaks one mole of Cl–Cl bonds [1]; atomisation forms one mole of gaseous atoms, so its equation is ½Cl2(g) → Cl(g) [1].'),
 ('State the equation linking reaction heat to solution mass m, specific heat capacity c and temperature rise ΔT, assuming negligible heat transfer elsewhere. [1]','qreaction = −mcΔT [1]. Molar ΔH requires dividing this sample heat by the relevant amount of reaction.'),
 ('Calculate the molar enthalpy of neutralisation when 0.0250 mol water forms and 60.0 g solution warms by 5.00 K. Use c = 4.18 J g⁻¹ K⁻¹ and neglect other heat transfers. Give three significant figures. [3]','qsolution = mcΔT = 60.0 × 4.18 × 5.00 = 1254 J [1]. Convert qreaction = −1.254 kJ and use ΔH = qreaction/n [1]. Answer: −1.254/0.0250 = −50.2 kJ mol⁻¹ to three significant figures [1].'),
 ('Determine whether a reaction is exothermic or endothermic when it cools its surrounding solution by 3.0 K, assuming no other heat transfers. [1]','Endothermic [1]: the solution loses heat, so the reaction absorbs it.'),
 ('Describe the energy transfers in breaking reactant bonds, forming product bonds and obtaining an exothermic net change. [3]','Breaking bonds requires energy [1]; forming bonds releases energy [1]; an exothermic net change occurs when formation releases more energy than breaking requires [1].'),
 ('Explain why breaking bonds alone cannot account for the net heat released by combustion. [2]','Breaking bonds requires an energy input [1]; because forming product bonds releases more energy than the input in an exothermic combustion, the overall change releases heat [1].'),
 ('State the bond-energy relationship used to estimate a gaseous reaction enthalpy. [1]','ΔH ≈ ΣE(bonds broken) − ΣE(bonds formed) [1], with bond counts taken from the balanced equation.'),
 ('Calculate ΔH for H2(g) + Cl2(g) → 2HCl(g) using bond energies H–H 436, Cl–Cl 243 and H–Cl 432 kJ mol⁻¹. [3]','Input = 436 + 243 = 679 kJ [1]; output magnitude = 2 × 432 = 864 kJ [1]; ΔH ≈ 679 − 864 = −185 kJ mol⁻¹ for the equation as written [1]. No unit conversion is needed. Whole-kJ precision follows the supplied whole-number bond data.'),
 ('Determine whether a gaseous reaction is exothermic or endothermic if breaking its reactant bonds requires 700 kJ and forming its product bonds releases 820 kJ on the same reaction basis. [1]','Exothermic [1], because the release on forming bonds exceeds the energy input.'),
 ('State one reason a mean-bond-enthalpy estimate can differ from a specific reaction enthalpy for the same gaseous endpoints. [1]','Mean bond enthalpies average over molecular environments, so they may differ from the actual values for the particular molecules [1].'),
 ('Calculate the percentage discrepancy of a mean-bond estimate of −190 kJ mol⁻¹ from a specific value of −204 kJ mol⁻¹ for identical gaseous endpoints. Use the magnitude of the specific value as denominator and give two significant figures. [3]','Relationship: percentage discrepancy = |estimate − reference|/|reference| × 100. Difference = |−190 − (−204)| = 14 kJ mol⁻¹ [1]. Substitution = 14/204 × 100 = 6.8627 percent [1]. Answer: 6.9% to two significant figures [1]; the common energy units cancel, so no conversion is required.'),
 ('Determine which comparison requires a phase-change correction: A two values for identical gaseous endpoints; B a gaseous-water bond estimate and a liquid-water combustion value. [1]','B [1]: the water states differ, so a phase-change term is needed before the values describe matching endpoints.'),
 ('State Hess’s law. [1]','The enthalpy change between given initial and final states is independent of the route taken [1].'),
 ('Calculate ΔH for B → C when the same-basis changes A → C and A → B are −120 and −45 kJ mol⁻¹ respectively. [3]','Hess relationship: ΔH(A → C) = ΔH(A → B) + ΔH(B → C) [1]. Substitute −120 = −45 + x [1]. Answer x = −75 kJ mol⁻¹ [1], to the nearest kJ as supplied; no unit conversion is needed.'),
 ('Determine the sign change required when a thermochemical equation is reversed to fit a Hess cycle. [1]','Reverse the sign of its ΔH [1], because initial and final states exchange places.'),
 ('State the common final substances used to combine standard combustion data for C(s, graphite), H2(g) and CH4(g) into a methane formation cycle with liquid water. [1]','CO2(g) and H2O(l), in matching amounts on both routes [1].'),
 ('Calculate ΔH°f(CH4) from combustion values C(s, graphite): −394; H2(g): −286; CH4(g): −890 kJ mol⁻¹, with matching CO2(g) and H2O(l) endpoints. [3]','Relationship ΔH°f(CH4) = ΔH°c(C) + 2ΔH°c(H2) − ΔH°c(CH4) [1]. Substitution −394 + 2(−286) − (−890) [1]. Answer −76 kJ mol⁻¹ [1], to the nearest kJ as supplied. No unit conversion is required.'),
 ('Determine why combustion enthalpies cannot be combined directly in a formation cycle if one route ends with liquid water and the other ends with steam. [1]','The routes have different final states [1]; include a phase-change enthalpy to make their endpoints match.'),
 ('State what the vertical and horizontal axes represent in a reaction pathway diagram. [1]','Vertical: enthalpy; horizontal: progress of reaction [1].'),
 ('Determine ΔH from this reaction pathway diagram. Then sketch the same profile and label the forward activation-energy interval as additional practice. [1]\n\n![Reaction pathway with reactants 0, peak +80 and products −40 kJ mol⁻¹](assets/8224-enthalpy-pathway.png)','ΔH = −40 kJ mol⁻¹ [1], because products lie 40 kJ mol⁻¹ below reactants. In the practice sketch, label enthalpy and progress axes, reactants and products, and the activation interval from reactants to the peak (80 kJ mol⁻¹).')
]
for slot,(prompt,answer) in zip(s,answers):
    subtype='WHY' if slot['subtype']=='MECH' else None
    if subtype:t.deviations.append({'from':slot['slot']+' MECH','to':'WHY; original AO, Bloom, command word and tariff retained','why':'Energy-transfer or thermochemical-definition reasoning does not involve the electron movement, intermediate and product demanded by the generic reaction-mechanism structure.'})
    t.item(slot,prompt,answer,subtype=subtype)
t.deviations.append({'from':s[22]['slot']+' one-mark INTERP baseline','to':'Retain marked ΔH interpretation and add an explicitly unmarked construction sketch','why':'The syllabus asks for both construction and interpretation; a supplied diagram alone does not practise constructing the profile.'})
p=t.wo['performance_tasks']
t.item(p[0],'''Identify one correct option per question. [6]
1. For an exothermic reaction, ΔH is: A negative; B zero; C positive; D equal to the temperature rise.
2. Standard formation enthalpy refers to forming: A one mole of atoms; B one mole of compound from standard-state elements; C any amount of product; D one mole of water.
3. A solution gains 600 J with no other heat transfers. The reaction heat is: A +600 J; B 0 J; C −600 J; D +600 kJ.
4. A → C is −90 and A → B is −30 kJ mol⁻¹ on the same basis. B → C is: A +60; B −120; C +120; D −60 kJ mol⁻¹.
5. With m = 20.0 g, c = 4.00 J g⁻¹ K⁻¹ and ΔT = +5.00 K, solution heat is: A 400 J; B −400 J; C 25 J; D 4.00 J.
6. If a thermochemical equation and its amount are doubled, ΔH for that equation: A halves; B doubles; C changes sign; D remains unchanged.''',
 '''Key: 1 A, 2 B, 3 C, 4 D, 5 A, 6 B. Award one mark per correct option.
1. A follows heat loss from the reacting system. Distractor B means no net enthalpy change; C describes heat absorption; D confuses energy and temperature.
2. B has the correct amount and starting states. A describes atomisation; C omits the one-mole basis; D confuses formation with neutralisation.
3. C follows qreaction = −qsolution. A copies the surroundings' sign; B ignores transfer; D changes both sign and unit magnitude incorrectly.
4. D follows −90 = −30 + x. A reverses the target; B adds the two given values without respecting routes; C combines both errors.
5. A follows mcΔT = 20.0 × 4.00 × 5.00 = 400 J. B uses the reaction sign for the solution; C divides in place of multiplying; D mistakes c for heat.
6. B follows proportionality to amount. A applies inverse scaling; C corresponds to reversing the equation; D confuses total equation enthalpy with a fixed per-mole quantity.''')
t.item(p[1],'''Explain the energetic reasoning and complete the calculations. [8]
(a) State the energy effect of breaking a gaseous covalent bond, including the sign of its dissociation enthalpy. [1]
(b) Calculate the bond-energy estimate for H2(g) + Cl2(g) → 2HCl(g). Use H–H 436, Cl–Cl 243 and H–Cl 432 kJ mol⁻¹. [3]
(c) Explain why that estimated reaction is exothermic. [1]
(d) In a separate neutralisation, 50.0 g solution warms by 4.00 K. Calculate the reaction heat, using c = 4.18 J g⁻¹ K⁻¹ and neglecting other heat transfers. [2]
(e) State the amount basis used to express a standard enthalpy change of neutralisation. [1]''',
 '''Part (a): bond breaking requires energy and has positive dissociation enthalpy [1].
Part (b): energy input 436 + 243 = 679 kJ [1]; formation release magnitude 2 × 432 = 864 kJ [1]; ΔH ≈ 679 − 864 = −185 kJ mol⁻¹ for the equation as written [1], at whole-kJ precision from the supplied data.
Part (c): forming product bonds releases more energy than breaking reactant bonds requires [1].
Part (d): qreaction = −mcΔT = −50.0 × 4.18 × 4.00 = −836 J [1]; answer −0.836 kJ to three significant figures [1].
Part (e): one mole of water formed by reaction of acid and base [1]. Each bracket is a separate creditworthy point.''')
t.item(p[2],'''Calculate the indirect enthalpy change for dissolving one mole of anhydrous salt X(s), using these original model data. All routes end in the same dilute solution at the same stated temperature and pressure. Neglect heat transfer to apparatus and the wider surroundings. [5]
(a) When 0.0200 mol X(s) dissolves, a total 80.0 g solution warms by 2.50 K. Use c = 4.18 J g⁻¹ K⁻¹. Calculate the molar solution enthalpy and identify its thermal sign. [3]
(b) A cycle connects X(s) → X·nH2O(s), enthalpy x, followed by dissolution of one mole of this hydrated solid, ΔH = +8.00 kJ mol⁻¹. Extra water is included on the appropriate routes so the endpoints match. Calculate x using Hess’s law. [2]''',
 '''(a) Equation and working: qreaction = −mcΔT = −80.0 × 4.18 × 2.50 = −836 J [1]. Conversion and molar basis: −0.836/0.0200 = −41.8 kJ mol⁻¹ [1]. It is exothermic, with negative ΔH, expressed per mole of X dissolved [1]. Three significant figures follow the supplied data.
(b) Hess relationship: −41.8 = x + 8.00 [1]. Answer x = −49.8 kJ mol⁻¹ to three significant figures [1]. Here x describes formation of a hydrated solid, not gaseous-ion hydration; these are different processes.''')
t.deviations.append({'from':'Generic conditions variant register on a thermochemical definition','to':'State standard pressure and specified temperature explicitly in the definition, and distinguish gas reference settings; checker limitation recorded','why':'s.t.p. and r.t.p. are gas-volume conventions, not variants of thermochemical standard state. The shared checker also cannot match abbreviations ending in a full stop with its trailing word boundary.'})
t.save()
