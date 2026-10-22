"""Original halogen teaching and syllabus-aligned practice."""
from authoring_common_8224 import Topic
t=Topic('3.4')
def add(short,claims,title,text,loc):t.objective(short,claims,[(title,text)],'OpenStax-Chemistry',loc)
add('1-01',[
 'Chlorine is a pale green/yellow-green gas, bromine a red-brown liquid and iodine a grey-black solid at ordinary room temperature and pressure.',
 'Bromine vapour is red-brown and iodine vapour violet; aqueous iodine is brown while iodine in a suitable non-polar solvent is violet.',
 'Solution colour depends on solvent, concentration and the chemical species present.'
], 'Colours must carry a phase and solvent', '''At room temperature and pressure, chlorine is a pale green or yellow-green gas, bromine is a red-brown liquid and iodine is a grey-black crystalline solid. Bromine above its liquid is a red-brown vapour. Iodine produces a violet vapour when warmed. A description such as “iodine is purple” is therefore incomplete unless it identifies the vapour or a suitable solution rather than the ordinary solid.

In water, chlorine is usually described as pale green and bromine as orange to brown, with intensity depending on concentration. Aqueous iodine is brown. Iodine is much more soluble in an aqueous iodide solution than in pure water, but the resulting iodine-containing solution is still brown in the usual observation. The iodide ions themselves are colourless; do not assign iodine's colour to a halide salt simply because both contain the same element.

In a suitable non-polar organic solvent, iodine gives a violet or purple solution. Bromine gives an orange/red-brown solution, while chlorine remains pale green in a sufficiently concentrated sample. State the solvent when using colour to interpret a displacement experiment. Brown aqueous iodine and purple organic iodine are not contradictory observations and do not indicate two different elemental halogens.

Colour evidence supports identification but needs context. A very dilute coloured species may appear almost colourless, and a mixture of halogens or coloured reagents can give a less straightforward appearance. Record the actual phase, solvent and observed colour before naming the product. A change of layer colour after adding an organic solvent may reflect redistribution into that solvent rather than an extra redox step. This distinction connects the physical observations here to the iodide oxidation test in Topic 2.2.''',
 '§18.11, printed pp.1028–1029 (PDF pp.1038–1039), elemental and solution colours; source specifies iodine in non-polar solvents.')
add('1-02',[
 'At the same ordinary room temperature and pressure, chlorine is gaseous, bromine liquid and iodine solid.',
 'Melting and boiling temperatures rise from chlorine through bromine to iodine, giving the observed change of state.'
], 'The state trend follows phase-transition temperatures', '''Compare the three halogens at the same room temperature and pressure. Chlorine is above its boiling point and is a gas. Bromine lies between its melting and boiling temperatures and is a liquid. Iodine is below its melting temperature and is a solid. The trend is therefore gas to liquid to solid from chlorine to iodine under that common setting.

The increasing melting and boiling temperatures indicate that more thermal energy is needed to separate the particles sufficiently for the less condensed phase. These are molecular elements: Cl2, Br2 and I2. The change in state does not arise because iodine alone has become an ionic lattice. Nor does a halogen's increasing atom count down the table mean that its ordinary elemental molecule contains more than two atoms.

The distinction between liquid and vapour can be seen for bromine, where vapour exists above the liquid. A liquid does not need to be at its boiling point for some molecules to enter the gas phase. Similarly, iodine can sublime from solid to vapour, giving the characteristic violet appearance without requiring that a visible liquid first collects in an ordinary open demonstration.

Use a specified temperature when inferring a state. If an unfamiliar halogen is predicted to have a higher boiling point than bromine, that alone does not fix whether it is liquid or solid at room temperature: its melting point is also needed. The stated chlorine/bromine/iodine sequence uses both transitions. In a data question, locate the room temperature relative to each pair of phase-transition temperatures instead of treating the group name as a fixed state. This prepares the intermolecular explanation of volatility in the next section.''',
 '§18.11 printed p.1028, phases; §§10.1–10.3 phase transitions and intermolecular forces.')
add('1-03',[
 'Dispersion attractions become stronger from Cl2 to Br2 to I2 as their electron clouds become larger and more polarisable.',
 'Stronger intermolecular attractions raise boiling temperature and reduce volatility under comparable settings.',
 'Vaporisation of a molecular halogen separates molecules rather than breaking the X–X covalent bond.'
], 'Explaining volatility through intermolecular attractions', '''Volatility describes how readily a substance enters the vapour phase. At comparable temperature and pressure, chlorine is more volatile than bromine, and bromine is more volatile than iodine. The molecules become larger down this sequence and contain more electrons. Their electron clouds are more readily distorted, so temporary dipole–induced dipole attractions become stronger.

More energy is then needed to separate molecules. Boiling temperature rises, and the tendency to escape into vapour at a given temperature is reduced. Link the greater molecular electron population to stronger dispersion attractions rather than merely saying that iodine is heavier. Mass and electron count correlate in this series, but intermolecular attraction is the relevant physical mechanism.

The X–X covalent bond inside a molecule is not broken during ordinary melting or vaporisation. An iodine vapour contains I2 molecules rather than being defined as free iodine atoms. Consequently, comparing I–I and Cl–Cl bond energies does not explain their boiling-point trend. The intermolecular and intramolecular changes are different even though both involve the same element symbols.

If interpreting a mass-loss demonstration, control temperature, exposed surface, time and airflow before comparing how readily material enters vapour. Faster loss of one sample can otherwise reflect a different setup. An original numerical example in which a solid loses 0.200 g over 10.0 minutes has average mass-loss rate 0.0200 g min⁻¹, but that rate alone cannot reveal a universal boiling point. Use the state observations and molecular model together. Topic 1.3 supplies the dispersion-force explanation, and Topic 5.1 develops the measurement controls needed to compare rates.''',
 '§10.1 dispersion forces and phase properties; §18.11 printed p.1028, volatility and phases. Mass-loss example original.')
add('2-01',[
 'Oxidising strength decreases from chlorine to bromine to iodine; the stronger halogen can oxidise halide ions of a weaker halogen in the specified displacement comparisons.',
 'Chlorine oxidises bromide and iodide, bromine oxidises iodide, and iodine does not oxidise chloride or bromide under the usual school comparison.',
 'The halogen gains electrons while displaced halide ions lose electrons.'
], 'Halogen displacement as a redox comparison', '''An oxidising agent accepts electrons from another species. For a halogen X2, the reduction half-equation is X2 + 2e− → 2X−. Oxidising strength decreases from chlorine to bromine to iodine. A stronger member can oxidise the halide ions of a weaker member in the usual aqueous displacement comparison.

Thus Cl2(aq) + 2Br−(aq) → 2Cl−(aq) + Br2(aq), and chlorine similarly oxidises iodide to iodine. Bromine can oxidise iodide: Br2(aq) + 2I−(aq) → 2Br−(aq) + I2(aq). Iodine does not displace chlorine or bromine from their halide solutions under the ordinary comparison. In each successful displacement, the starting halogen is reduced to its halide and the starting halide is oxidised to elemental halogen.

Colour changes can help identify the new element, but interpret them using phase and solvent. Liberating iodine gives brown colour in the aqueous system or violet in a suitable organic layer. Bromine gives an orange/brown appearance. The original added halogen may also contribute colour, especially if present in excess, so an observation should be connected to a balanced redox change rather than judged by a remembered colour alone.

The atom-level explanation uses the group trend in attraction for an incoming electron: greater distance and shielding down the group reduce the effective attraction at the outer region. Do not confuse elemental oxidising strength with halide reducing strength. I− loses electrons more readily than Br− or Cl− in this comparison, so the halide trend is the reverse. Topic 2.2 provides the oxidation-number and agent terminology that makes the two roles unambiguous.''',
 '§18.11 printed pp.1027–1029, relative oxidants and halide oxidation; §17.3 reduction data used qualitatively.')
add('2-02',[
 'Hydrogen reacts with the halogens to form hydrogen halides; reaction vigour decreases in the general sequence towards iodine.',
 'A hydrogen/chlorine mixture can react rapidly on light exposure, while bromine requires heating and iodine forms HI reversibly at elevated temperature.',
 'The hydride reaction depends on the competing energies of bonds broken and formed, not only on the X–X bond.'
], 'Reaction with hydrogen', '''Hydrogen and a halogen form a hydrogen halide: H2 + X2 → 2HX. In the familiar comparisons, fluorine reacts extremely vigorously, chlorine can react explosively when triggered by light, bromine needs heating for a useful reaction, and iodine gives a reversible change at elevated temperature. The stated initiation or heating belongs with the observation; an unlit hydrogen/chlorine mixture is not equivalent to one exposed to strong light.

For chlorine, H2(g) + Cl2(g) → 2HCl(g). The product here is hydrogen chloride gas. Dissolving it in water gives hydrochloric acid, a different physical description. For bromine vapour, H2(g) + Br2(g) → 2HBr(g). For heated iodine, H2(g) + I2(g) ⇌ 2HI(g), with reactants and product present in the equilibrium mixture at that temperature.

The energy account involves breaking H–H and X–X bonds and forming two H–X bonds. A reaction's overall enthalpy depends on all these terms. A weak X–X bond alone does not prove that its hydrogen reaction must be the most vigorous. The activation barrier and the strength of the new hydrogen–halogen bonds also matter.

Describe the trend without promising a particular yield from reaction vigour. A fast initiated reaction and a high equilibrium conversion are different ideas. For iodine at a stated temperature, reversibility limits the final composition even though HI forms. Increasing temperature can change both rate and composition, so use any supplied enthalpy information for the latter. These distinctions connect the hydrogen reactions with the energetics, equilibrium and kinetics already taught, rather than replacing chemical explanation with a list of dramatic observations.''',
 '§18.5 hydrogen/halogen reaction table and §18.11 printed p.1029, light-triggered chlorine; §13.3 HI at stated temperature; §7.5 bond-energy bookkeeping.')
add('2-03',[
 'Hydrogen-halide thermal stability decreases in the order HF > HCl > HBr > HI, linked to weakening H–X bonds down the group.',
 'A longer H–X bond generally has weaker orbital overlap and requires less energy to break in the down-group comparison.'
], 'Thermal stability of the hydrogen halides', '''Thermal stability describes resistance to decomposition on heating. For the hydrogen halides the usual order is HF, HCl, HBr, HI from most to least thermally stable. For the three heavier examples in the main comparison, HCl is more stable than HBr, which is more stable than HI. The order concerns the H–X bond in the molecule rather than attractions between different HX molecules.

The halogen atom becomes larger down the group. The bond to hydrogen is longer, and effective orbital overlap is reduced. The H–X bond is weaker and requires less energy to break. HI therefore decomposes more readily on heating than HCl in the qualitative comparison. Fluorine's small size and strong H–F bond place HF at the stable end.

Do not transfer this stability order to boiling points. Boiling separates molecules and can involve special intermolecular attractions, whereas thermal decomposition breaks chemical bonds. A compound may have a relatively high boiling point without its covalent bond being the most resistant to breaking in the group comparison. Name the process before selecting the bond-energy or intermolecular explanation.

Thermal stability also differs from aqueous acid strength. Ionisation in water depends on interactions with the solvent as well as bond breaking. A statement about HI being less thermally stable is not itself a pH calculation, and a strong acid label does not mean it has a stronger H–X covalent bond. For a question about heating, refer to bond length, overlap and dissociation energy. If decomposition is represented reversibly, the measured extent also depends on temperature and the maintained mixture, so a lower stability does not mean that all HI vanishes instantly at room temperature.''',
 '§7.5 Table 7.2 H–X dissociation values; §§18.5 and 18.11 hydrogen halides; down-group thermal interpretation from bond energies.')
add('2-04',[
 'Supplied H–X bond energies can be used to rank thermal stability; higher dissociation energy supports greater resistance to bond breaking.',
 'A bond-energy difference is an energy-per-mole comparison, not a direct numerical prediction of decomposition rate.'
], 'Interpreting bond-energy evidence', '''Use the supplied bond energies to test the thermal-stability explanation. Representative H–Cl, H–Br and H–I dissociation values are 432, 370 and 295 kJ mol⁻¹ in the local textbook table. They fall down the group, agreeing with the order HCl > HBr > HI in resistance to thermal decomposition. The values describe energy needed for gaseous bond breaking, so retain that state and process.

For an original numerical comparison, H–Cl requires 432 − 295 = 137 kJ mol⁻¹ more energy to dissociate than H–I using those data. The difference quantifies a bond-strength comparison. It does not say HCl reacts 137 times more slowly or establish a precise decomposition temperature. Rate and composition need further information.

If asked for the energy to dissociate a specified amount, multiply the molar value by moles of bonds. Breaking 0.0100 mol of H–I bonds at 295 kJ mol⁻¹ requires 2.95 kJ. This bond-breaking quantity is positive. Forming the same bond from separated gaseous atoms would have the opposite sign for matching endpoints.

When comparing different hydrogen reactions, use the full broken-minus-formed bond-energy account rather than just this H–X list. For thermal stability the H–X strength is the key qualitative evidence. For the enthalpy of H2 + X2 forming 2HX, both reactant bonds and both product bonds contribute. This is why a table can support one conclusion directly but require additional data for another. Quote the relevant values, identify the energy basis and give a chemically bounded inference. In a proposed decomposition equation such as 2HI → H2 + I2, count two H–I bonds broken and both new product bonds formed before estimating the overall heat change. The calculation method follows Topic 2.1, while the distinction between a threshold and rate follows Topic 2.4.''',
 '§7.5 Table 7.2, printed pp.364–365, H–Cl 432, H–Br 370 and H–I 295 kJ mol⁻¹; original arithmetic.')
add('3-01',[
 'AgCl is white and dissolves in dilute ammonia; AgBr is cream and requires concentrated ammonia for appreciable dissolution; yellow AgI remains insoluble in that comparison.',
 'Concentrated sulphuric acid liberates HCl from a chloride without the analogous halide redox; bromide and iodide can reduce the acid and form their elemental halogens.',
 'Iodide can give sulphur dioxide, sulphur or hydrogen sulphide as sulphur reduction products, depending on the reacting mixture.'
], 'Two distinct halide comparisons', '''For the precipitation comparison, acidify the halide sample with dilute nitric acid and add aqueous silver nitrate. Ag+(aq) + X−(aq) → AgX(s). The chloride precipitate is white, bromide cream and iodide yellow. Follow with aqueous ammonia: AgCl dissolves in dilute ammonia; AgBr dissolves appreciably in concentrated ammonia; AgI remains insoluble in the stated comparison. Use a fresh portion where needed to keep the ammonia strength and precipitate identity clear.

These observations concern the precipitated halide and its subsequent interaction with ammonia. They are not the colours of elemental chlorine, bromine or iodine. Nitric acid avoids adding chloride from hydrochloric acid and removes interfering carbonate in the standard test. Explain a conclusion from both precipitation and the ammonia observation, rather than colour alone.

Concentrated sulphuric acid gives a different comparison. A chloride salt can liberate HCl by an acid–base reaction, for example NaCl + H2SO4 → NaHSO4 + HCl. There is no corresponding oxidation of chloride in this school comparison. Bromide first yields HBr, which can reduce the acid: 2HBr + H2SO4 → Br2 + SO2 + 2H2O. Bromine gives orange/brown colour or fumes.

Iodide is the stronger reducing halide and forms iodine, visible as dark solid or violet vapour, while sulphur can be reduced to SO2, S or H2S. One possible balance is 8HI + H2SO4 → 4I2 + H2S + 4H2O. The different products depend on the mixture; they should not be described as a single exclusive endpoint. Distinguish acid displacement from redox by checking oxidation numbers: halide rises from −1 to 0 when its element forms, while sulphur falls from +6 in the acid. These observations are chemical evidence, not instructions to identify gases by direct smelling.''',
 'Syllabus §3.4.3 tests; OpenStax §18.11 halide oxidation and §15.2 ammonia/AgCl dissolution. Full ammonia-strength sequence and concentrated-acid product detail require semantic reference verification.')
add('4-01',[
 'Cold dilute sodium hydroxide reacts with chlorine to give chloride and chlorate(I): Cl2 + 2OH− → Cl− + ClO− + H2O.',
 'Hot concentrated sodium hydroxide gives chloride and chlorate(V): 3Cl2 + 6OH− → 5Cl− + ClO3− + 3H2O.',
 'Both are disproportionation because chlorine at oxidation number zero is simultaneously reduced to −1 and oxidised to +1 or +5.'
], 'Cold and hot alkali give different oxyanions', '''Disproportionation is a redox change in which the same element is oxidised and reduced. Chlorine begins at oxidation number zero in Cl2. In cold dilute aqueous sodium hydroxide it gives chloride and chlorate(I): Cl2(aq) + 2OH−(aq) → Cl−(aq) + ClO−(aq) + H2O(l). Chlorine falls to −1 in chloride and rises to +1 in ClO−.

Including the spectator sodium gives Cl2 + 2NaOH → NaCl + NaClO + H2O. This is the cold dilute alkali equation; attach those qualifications to the product. The I in chlorate(I) is a Roman numeral for chlorine +1 and does not refer to the element iodine. Topic 2.2 established this naming convention.

With hot concentrated aqueous sodium hydroxide, the product is chlorate(V): 3Cl2 + 6OH− → 5Cl− + ClO3− + 3H2O. One chlorine atom rises from 0 to +5, losing five electrons formally; five chlorine atoms fall from 0 to −1, together gaining five. The 5:1 chloride-to-chlorate(V) amount ratio is therefore consistent with electron balance.

The equations also conserve atoms and total charge. Do not replace ClO− by ClO3− in the cold equation without changing coefficients and the reaction setting. Both oxyanions have overall charge −1, but their chlorine oxidation numbers differ. Distinguish the formal oxidation number from ion charge when explaining why the hot reaction still counts as disproportionation. A correct conclusion names both the oxidised and reduced chlorine products, rather than saying only that chlorine changes oxidation state. Heat and concentration are part of the stated comparison and must travel with the products in a stand-alone answer.''',
 'Syllabus §3.4.4 cold/hot alkali products; OpenStax §18.11 printed p.1029 chlorine disproportionation; extended alkali equations derived by atom/electron balance with specified syllabus endpoints.')
add('4-02',[
 'Chlorine in water is described by Cl2 + H2O ⇌ H+ + Cl− + HOCl; changing H+ concentration changes the equilibrium mixture.',
 'Removing H+ with alkali favours the right-hand mixture, while adding acid in the presence of chloride can favour chlorine release.',
 'The HOCl/ClO− balance depends qualitatively on H+ concentration; increasing pH favours ClO−.'
], 'pH changes the chlorine-containing mixture', '''Chlorine water contains an equilibrium mixture described by Cl2(aq) + H2O(l) ⇌ H+(aq) + Cl−(aq) + HOCl(aq). HOCl is chloric(I) acid, also called hypochlorous acid. Increasing H+ concentration shifts this balance towards the left in the stated mixture; removing H+ by adding alkali favours the right-hand side. Apply the concentration change explicitly rather than merely saying that pH affects chlorine.

HOCl can transfer a proton to water. The simplified representation is HOCl(aq) ⇌ H+(aq) + ClO−(aq). At higher pH, lower H+ concentration favours ClO−; at lower pH, HOCl has a larger share of that pair. This is a qualitative speciation comparison. Chlorine remains at oxidation number +1 in both HOCl and ClO−, so that proton-transfer balance is not itself a redox change. The element’s chemical form changes without changing its formal oxidation number. No numerical weak-acid dissociation calculation is needed to follow the proton-transfer and concentration reasoning.

Combining chlorine's water reaction with hydroxide consumption gives the cold-alkali chloride/chlorate(I) balance. The hot concentrated alkali product also depends on the higher-temperature chemistry already stated; pH alone is not a reason to relabel every alkaline sample chlorate(V). Keep temperature, concentration and time context where the product distinction requires it.

Acidifying a mixture containing chloride and chlorate(I) can release chlorine: ClO− + Cl− + 2H+ → Cl2 + H2O. This explains a relevant chemical hazard of combining chlorine-containing bleach with acid. It is not necessary to invent a treatment recipe to explain the reaction. In water-treatment reasoning, identify which chlorine-containing species is present and how pH changes its relative amount, rather than assuming that the dissolved element and the oxyanion are chemically identical. Topic 2.3 provides the concentration-response logic, while Topic 2.2 supplies the oxidation-number balance.''',
 '§18.11 printed p.1029 chlorine-water equilibrium; §14.1 proton transfer; syllabus §3.4.4 qualitative pH response. Acid-release equation derived by combining stated species and conserving atoms/charge.')
add('5-01',[
 'Chlorine-containing oxidants formed in water can disinfect by damaging biological material; HOCl is an important active species.',
 'Water pH changes the relative HOCl/ClO− population and can affect disinfection effectiveness.',
 'Chlorination is controlled and monitored as part of treatment; it is not equivalent to physically removing all contaminants.'
], 'Why chlorine can disinfect water', '''Chlorine reacts with water to form chlorine-containing oxidising species, including HOCl. These can damage biological material and help inactivate microorganisms. The useful treatment role follows oxidising chemistry, rather than chlorine simply colouring the water or acting as a physical filter. A reaction that destroys a coloured organic substance can show related chemistry without being a direct measurement of water quality.

pH affects the relative amounts of HOCl and ClO−. At higher pH the ClO− fraction is larger; at lower pH HOCl forms a larger fraction of that pair. HOCl is generally the more effective disinfecting species in this comparison. The concentration balance therefore matters to the operation as well as the presence of an oxidant in principle. Temperature and the substances already present in the water can also affect the required treatment performance.

An effective water-treatment process controls addition, contact and monitoring. Some oxidant can be consumed by other reacting material, so the amount added is not identical to the amount remaining available after contact. A specified residual measurement is evidence about the treated water at that stage, not a claim that the same amount was active throughout the earlier process.

Chlorination does not itself remove every dissolved salt or solid particle. Other treatment stages can address suspended material and chemical contaminants. Explain the particular function rather than promising complete purification from a single chemical. At this syllabus level, relate chlorine-water reactions and pH to disinfection, with no invented household dose or plant-specific numerical operating limit. The same chemistry helps explain why the water-treatment question needs the identity of active species and relevant concentration information. Two waters with the same total added chlorine can differ in the oxidant remaining after other substances have reacted with it.''',
 '§18.11 printed p.1029 chlorine disinfection; syllabus §3.4.5 use and pH-linked application. Relative HOCl/ClO− effectiveness and treatment-specific interpretation marked for independent semantic verification.')
add('5-02',[
 'Halogen compounds have industrial roles in bleaches, PVC manufacture, solvents and some refrigerant/aerosol systems.',
 'Some long-lived chlorine-containing refrigerants can reach the stratosphere and release chlorine radicals that catalyse ozone destruction.',
 'Environmental behaviour depends on the particular compound; a halogen-containing label alone does not specify persistence or impact.'
], 'Useful compounds and environmental consequences', '''Halogens and their compounds have several different industrial roles. Chlorine-containing oxidants are used in bleaching. Chloroethene is used to manufacture poly(chloroethene), PVC. Some halogenated hydrocarbons have been used as solvents, refrigerants or aerosol propellants because of their physical properties. These are examples of chemical uses, not a claim that all halogenated compounds are interchangeable.

A useful property can also create an environmental problem. Some chlorofluorocarbon refrigerants are sufficiently stable in the lower atmosphere to persist and reach the stratosphere. Ultraviolet radiation can release chlorine radicals, which participate in catalytic ozone destruction. The radical can be regenerated through a cycle, so one chlorine-containing species can affect more than one ozone molecule. Topic 2.4 explains regeneration; Topic 4.3 develops the relevant halogenated-carbon chemistry.

Do not infer the same environmental behaviour for every compound containing chlorine or fluorine. Stability, reactions, breakdown products and where a substance is released all matter. A proposed substitute can reduce one impact while leaving others that need evaluation. A chemical comparison should identify the particular compound and evidence, rather than treating a familiar trade category as a complete environmental assessment.

For PVC, the presence of chlorine in a manufactured polymer differs from chlorine gas used as a disinfectant. The form of an element affects its properties and exposure pathways. For solvent use, the value of dissolving suitable substances should be considered alongside persistence and waste handling where data are supplied. No current production figure or regulatory claim is required here. The syllabus asks for industrial importance and environmental significance, so state both the useful function and a chemically connected consequence.''',
 '§18.11 applications, printed pp.1032–1033; §12.7 pp.692–693, catalytic ozone loss; §20.1 polymers. Syllabus §3.4.5 industrial examples.')
add('5-03',[
 'Bleaching by chlorine-containing oxidants changes colour-causing chemical species through oxidation, rather than simply diluting them.',
 'Moisture enables the aqueous chlorine/HOCl chemistry used to explain ordinary chlorine bleaching.',
 'The syllabus’s Namibian water-treatment application uses the same controlled oxidising chemistry, with pH and concentration relevant to performance.'
], 'Bleaching and the Namibian treatment application', '''Chlorine-containing bleach reacts chemically with colour-causing substances. Oxidation changes their structures and can remove the visible colour. The colour loss is therefore not simply a result of adding extra water or transferring a dye to a different layer. A comparison with a dilution control can distinguish physical dilution from a reacting oxidant where the experimental evidence supports that interpretation.

Moisture matters in the ordinary chlorine-bleaching description. Chlorine reacts in water to give HOCl-containing mixtures; these species supply the oxidising action. A damp coloured material can therefore respond differently from a dry one. Do not attribute the effect to free atomic oxygen being stored inside a bottle without an appropriate chemical model. The chlorine-water equation and oxidant identity provide the more useful account.

The syllabus links this chemistry to water treatment in Namibia. The chemical role remains oxidation and disinfection in a controlled treatment process. A local setting does not change the equations or justify inventing a named plant's operating numbers. Relevant evidence includes pH, oxidant concentration, what other material consumes the oxidant and how treatment performance is monitored.

Bleaching a test material and disinfecting water are related applications but different performance tests. Removing a visible colour does not prove that a water sample satisfies every quality criterion. Conversely, a disinfecting concentration need not remove all colour from every mixture. In an explanation, name the oxidising species, the chemical change it causes and the particular result being assessed. This connects a visible classroom observation with the public-treatment application while keeping the limits of each observation clear.''',
 'Syllabus §3.4.5 bleach and Namibia treatment application; OpenStax §18.11 printed p.1029, oxidation of organic/biological material and chlorine-water species.')
s=t.wo['item_slots']
qa=[
 ('State the colour of iodine vapour. [1]','Violet/purple [1].'),
 ('Suggest why iodine can appear brown in an aqueous layer but violet in a suitable non-polar organic layer. [1]','Its solution colour depends on solvent/species context; those are the expected aqueous and non-polar appearances [1].'),
 ('State the physical states of chlorine, bromine and iodine at ordinary room temperature and pressure. [1]','Chlorine gas, bromine liquid, iodine solid [1].'),
 ('Explain why the room-temperature state changes from chlorine gas to iodine solid. [2]','The larger molecular electron clouds give stronger dispersion attractions down the sequence [1], raising phase-transition temperatures so iodine remains solid at room temperature [1].'),
 ('State the relative volatility order for chlorine, bromine and iodine at comparable settings. [1]','Chlorine > bromine > iodine [1].'),
 ('Determine whether a rise in boiling point from Cl2 to I2 indicates weaker or stronger intermolecular attractions. [1]','Stronger attractions [1].'),
 ('State the oxidising-strength order of chlorine, bromine and iodine. [1]','Chlorine > bromine > iodine [1].'),
 ('Suggest the elemental halogen produced when chlorine reacts with aqueous bromide. [1]','Bromine [1], because chlorine oxidises Br−.'),
 ('Describe how hydrogen reacts with chlorine, bromine and iodine in the school comparison. [3]','Chlorine can react rapidly/explosively when initiated by light [1]; bromine requires heating [1]; iodine reacts reversibly at elevated temperature to give HI [1].'),
 ('Write the balanced gas-phase equation for hydrogen with chlorine forming hydrogen chloride. [2]','H2(g) + Cl2(g) → 2HCl(g). Correct species/states [1]; balance [1].'),
 ('Explain why a weaker halogen–halogen bond alone does not prove a more vigorous reaction with hydrogen. [2]','The energy account also includes breaking H–H and forming two H–X bonds [1]; the pathway barrier and the complete energy balance, rather than one bond, determine the comparison [1].'),
 ('Describe the thermal-stability order HCl, HBr and HI and the down-group bond change explaining it. [3]','HCl > HBr > HI [1]; H–X bonds become longer [1] and weaker, making thermal decomposition easier [1].'),
 ('Explain why HI is less thermally stable than HCl. [2]','The larger iodine atom gives a longer H–I bond with poorer overlap [1]; its lower bond energy makes breaking it easier [1].'),
 ('State which H–X bond value supports greater resistance to thermal bond breaking: a larger or smaller dissociation energy. [1]','A larger dissociation energy [1].'),
 ('Determine the most thermally stable hydride from supplied bond energies HCl 432, HBr 370 and HI 295 kJ mol⁻¹. [1]','HCl [1], which has the largest bond energy.'),
 ('Describe AgCl, AgBr and AgI in the aqueous silver-nitrate/ammonia comparison. [3]','AgCl is white and dissolves in dilute ammonia [1]; AgBr is cream and dissolves appreciably in concentrated ammonia [1]; AgI is yellow and remains insoluble in the stated ammonia comparison [1].'),
 ('Write the precipitation half of the chloride test as an ionic equation, including state symbols. [2]','Ag+(aq) + Cl−(aq) → AgCl(s). Correct species/states [1]; atom/charge balance [1].'),
 ('Write the balanced redox equation for HBr reducing concentrated sulphuric acid to SO2, with Br2 and water as the other products. [2]','2HBr + H2SO4 → Br2 + SO2 + 2H2O. Correct reactants/products [1]; balance [1].'),
 ('Explain why bromide reacting with concentrated sulphuric acid involves redox while the ordinary chloride/HCl displacement does not. [2]','Bromide is oxidised from −1 to 0 as Br2 forms [1], while sulphur is reduced from +6 to +4 in SO2; the chloride displacement has no corresponding oxidation-number changes [1].'),
 ('Describe chlorine disproportionation with cold dilute and hot concentrated aqueous sodium hydroxide, using chlorine oxidation numbers. [3]','Cold dilute alkali gives chloride and chlorate(I) [1]; hot concentrated alkali gives chloride and chlorate(V) [1]; chlorine 0 is reduced to −1 and oxidised to +1 or +5 respectively [1].'),
 ('Explain why Cl2 + 2OH− → Cl− + ClO− + H2O in cold dilute alkali is disproportionation. [2]','Chlorine 0 is reduced to −1 in Cl− [1] and oxidised to +1 in ClO− in the same overall reaction [1].'),
 ('Describe the qualitative concentration response of Cl2 + H2O ⇌ H+ + Cl− + HOCl when acid is added, alkali removes H+, and pH rises in the HOCl/ClO− pair. [3]','Adding H+ favours chlorine on the left [1]; removing H+ favours the right-hand mixture [1]; higher pH favours ClO− relative to HOCl [1].'),
 ('Write the balanced equation showing chlorine release from acidifying a chloride/chlorate(I) mixture, including aqueous states. [2]','ClO−(aq) + Cl−(aq) + 2H+(aq) → Cl2(g) + H2O(l). Correct species/states [1]; atom and charge balance [1].'),
 ('Explain why raising pH favours ClO− in the qualitative HOCl ⇌ H+ + ClO− balance. [2]','Higher pH means lower H+ concentration [1]; the equilibrium response forms more H+ and ClO− from HOCl [1].'),
 ('Describe the use of chlorine in water treatment through the active species, action and need for control. [3]','Water reaction forms oxidants including HOCl [1], which damage biological material and aid disinfection [1]; pH and oxidant concentration/contact need controlled monitoring [1].'),
 ('Explain why water pH can affect chlorine-based disinfection. [2]','It changes the relative HOCl and ClO− amounts [1]; these species differ in disinfecting effectiveness, so oxidant identity as well as total amount matters [1].'),
 ('State two industrial uses of halogen compounds besides water disinfection. [1]','For example, bleaching and PVC manufacture [1]; suitable solvent or refrigerant/propellant examples are also valid.'),
 ('Suggest why a persistent chlorine-containing refrigerant can cause an environmental concern in the stratosphere. [1]','Its breakdown can release chlorine radicals that catalyse ozone destruction [1].'),
 ('State the chemical process responsible for bleaching by chlorine-containing oxidants. [1]','Oxidation of colour-causing chemical species [1].'),
 ('Explain why loss of colour in a bleach demonstration does not by itself establish complete water purification. [2]','It tests reaction with a colour-causing substance [1]; other biological or chemical quality criteria need their own assessment [1].')
]
assert len(qa)==len(s)
for slot,(prompt,answer) in zip(s,qa):
 st='WHY' if slot['subtype']=='MECH' else None
 t.item(slot,prompt,answer,subtype=st)
 if st:t.deviations.append({'from':slot['slot']+' MECH','to':'WHY; preserve original AO/Bloom/command/tariff','why':'The task asks for stability, oxidation-state or application reasoning, not a specific electron-arrow intermediate/product mechanism.'})
p=t.wo['performance_tasks']
t.item(p[0],'''Identify one correct option per question. [8]
1. Iodine vapour is: A violet; B white; C green; D blue.
2. Bromine at room temperature and pressure is: A gas; B liquid; C giant covalent solid; D ionic solution by definition.
3. From Cl2 to I2 dispersion attractions generally: A vanish; B decrease; C increase; D become covalent bonds between all molecules.
4. The least volatile of Cl2, Br2 and I2 at comparable settings is: A Cl2; B Br2; C all equal; D I2.
5. Chlorine with aqueous bromide produces: A Br2; B I2; C chlorine ions at oxidation number +7; D no redox change.
6. Bromine with aqueous iodide produces: A Br− only with no other product; B I2 and Br−; C chlorine; D oxygen necessarily.
7. An aqueous iodine observation is usually: A violet in all solvents; B colourless because iodide is colourless; C brown; D silver-white.
8. Iodine cannot ordinarily displace bromine from bromide because: A I2 is more volatile; B Br− lacks electrons; C iodine is an ionic metal; D iodine is the weaker oxidising agent.''',
 '''Key: 1 A, 2 B, 3 C, 4 D, 5 A, 6 B, 7 C, 8 D. One mark per correct option.
1. A is the vapour colour. B is not iodine vapour; C suggests chlorine; D confuses an iodine/starch result.
2. B is the specified state. A ignores its phase-transition temperatures; C assigns a wrong structure; D confuses pure element and solution.
3. C follows larger polarisable electron clouds. A removes attractions; B reverses the trend; D confuses intermolecular attraction with covalent networking.
4. D has strongest dispersion attractions. A chooses the most volatile; B is intermediate; C ignores the state trend.
5. A follows oxidation of Br−. B introduces iodine absent from the system; C assigns an unrelated oxidation state; D ignores displacement redox.
6. B is the balanced redox outcome. A omits the oxidised iodine product; C introduces absent chlorine; D invents a required water-oxidation product.
7. C fits the aqueous context. A ignores solvent dependence; B confuses iodine and iodide; D is the wrong material appearance.
8. D compares oxidising strengths. A does not explain the electron-transfer direction; B is false; C misclassifies iodine.''')
t.item(p[1],'''Explain the halogen observations in these linked parts. [8]
(a) State the room-temperature state and vapour colour of iodine. [2]
(b) Explain why iodine is less volatile than chlorine, referring to intermolecular attraction. [2]
(c) Write the balanced ionic equation for chlorine displacing bromine from aqueous bromide. [2]
(d) Explain why the reverse displacement using bromine and chloride is not expected in the ordinary comparison. [2]''',
 '''Part (a): solid [1]; violet vapour [1].
Part (b): iodine’s larger electron cloud is more polarisable [1], giving stronger dispersion attractions and requiring more energy for molecular separation [1].
Part (c): Cl2(aq) + 2Br−(aq) → 2Cl−(aq) + Br2(aq). Correct species [1]; balance/charges [1].
Part (d): bromine is a weaker oxidising agent than chlorine [1], so it does not oxidise chloride to chlorine under the stated ordinary comparison [1]. Each bracket is a separate creditworthy point.''')
t.item(p[2],'''Calculate and interpret this original iodine observation. A sample loses 0.200 g as violet vapour over a stated interval; take I2 molar mass as 254 g mol⁻¹. [5]
(a) Calculate the amount of I2 entering the vapour, to three significant figures. [2]
(b) State iodine’s ordinary room-temperature state and its vapour colour. [1]
(c) State whether chlorine or iodine is more volatile under comparable settings, linking the choice to dispersion attractions. [1]
(d) State which is the stronger oxidising agent in the usual halide displacement comparison. [1]''',
 '''(a) Equation n = m/M; working 0.200/254 = 0.000787402 mol [1]. Answer 0.000787 mol, or 7.87 × 10⁻⁴ mol, to three significant figures [1]. Units g cancel against g mol⁻¹, so no mass conversion is needed.
(b) Iodine is a solid at room temperature and gives violet vapour [1].
(c) Chlorine is more volatile because its molecules have weaker dispersion attractions [1].
(d) Chlorine is the stronger oxidising agent [1].''')
t.deviations.append({'from':'Local-reference coverage limits','to':'Record ammonia strengths, concentrated-acid product mixture, hot-alkali endpoint and relative disinfection-species effectiveness as semantic verification focuses','why':'The corpus establishes governing syllabus scope and related principles, but does not directly verify every detailed test or application statement. Claims remain unverified and nonpublishable; no water-treatment dose is supplied.'})
t.save()
