"""Original transition-element and Namibian metallurgy syllabus resource."""
from authoring_common_8224 import Topic
t=Topic('3.3')
def add(short,claims,title,text,loc,source='OpenStax-Chemistry'):t.objective(short,claims,[(title,text)],source,loc)
add('1-01',[
 'The syllabus identifies a transition element as a d-block element forming one or more ions with an incomplete d subshell.',
 'Copper qualifies through ions such as Cu2+ with 3d9, whereas the usual Zn2+ ion has a full 3d10 subshell.',
 'Uranium is an actinide included here as a metallurgy example, not a first-row d-block element.'
], 'The definition depends on electronic structure', '''For this syllabus, a transition element is a d-block element that forms one or more ions with an incomplete d subshell. An incomplete d subshell contains fewer than the full ten d electrons and is not empty. The position of an element in a broad rectangular block of the table is useful evidence, but the stated ion criterion must also be checked.

Copper illustrates why looking only at the neutral atom is insufficient. Its atom has [Ar]3d10 4s1, with a full 3d subshell, but Cu2+ has [Ar]3d9. It therefore meets the syllabus criterion. Zinc's common Zn2+ ion has [Ar]3d10, so it does not meet this criterion merely by sitting beside the transition series. A coloured appearance or metallic conductivity alone does not replace this electronic test.

Iron supplies familiar incomplete-d ions: Fe2+ is 3d6 and Fe3+ is 3d5 beyond the argon core. The electrons are counted after removing those needed to give the ion's charge. Do not interpret a Roman numeral in the ion name as a number of d electrons; it describes oxidation number.

This chapter also includes Namibian metal-extraction examples. Uranium belongs to the actinides and is discussed because the syllabus uses it in metallurgy. Its appearance beside copper and manganese in an extraction section does not make it a first-row d-block transition metal. Keep a classification claim distinct from the choice of an industrial example. These definitions connect Topic 1.2's electron configurations to the characteristic chemistry of transition ions.''',
 'Syllabus §3.3.1 definition; OpenStax §19.1 printed pp.1052–1053 and §6.4 configurations. Governing syllabus ion criterion used where textbook wording is broader.')
add('1-02',[
 'First-row transition-ion configurations remove 4s electrons before 3d electrons from the corresponding neutral atom.',
 'Fe is [Ar]3d6 4s2, Fe2+ is [Ar]3d6 and Fe3+ is [Ar]3d5; Cr and Cu neutral configurations are [Ar]3d5 4s1 and [Ar]3d10 4s1.',
 'An orbital box holds at most two opposite-spin electrons; singly occupy equivalent d orbitals before pairing.'
], 'Configurations and electrons in boxes', '''Use s, p and d labels with their electron counts. Iron is [Ar]3d6 4s2. Its argon core represents 1s2 2s2 2p6 3s2 3p6. To form Fe2+, remove the two 4s electrons, giving [Ar]3d6. Fe3+ has lost one further d electron, giving [Ar]3d5. Count total electrons as atomic number minus positive charge: iron's 26 becomes 24 in Fe2+ and 23 in Fe3+.

In electron-box notation, draw one box for each orbital. There are five equivalent d boxes. Fill them singly with the same spin direction before adding a second electron to a box; a pair in one orbital has opposite spins. For Fe2+, one valid 3d representation is [↑↓][↑][↑][↑][↑]. For Fe3+ it is [↑][↑][↑][↑][↑]. The position of the paired box within a set of equivalent orbitals is not itself a different configuration.

The neutral chromium and copper exceptions introduced in Topic 1.2 remain relevant: Cr is [Ar]3d5 4s1 and Cu is [Ar]3d10 4s1. Cu2+ loses the 4s electron and one 3d electron, producing [Ar]3d9. Do not start from an incorrectly imposed 4s2 pattern and then carry its error into the ion.

When representing an unfamiliar ion, write the atom first, remove the required electrons in the appropriate order and verify the total. Then draw the partially filled subshell with correct box number and spin pairs. A superscript is an electron count; an ion charge is a separate label. If a question asks for both notations, a correct compact configuration alone does not supply the missing orbital-box representation.''',
 '§6.4, printed pp.314–319, configurations and ion formation; §19.1 printed p.1053, removal of s electrons before d.')
add('1-03',[
 'Characteristic transition-element behaviour includes variable oxidation states, catalytic activity and coloured compounds, linked to d-electron structure.',
 'Close energies of outer s and d electrons help permit several oxidation states; different ions need not have the same colour.',
 'These are characteristic tendencies, not claims that each compound of each transition element is coloured or catalytic.'
], 'Characteristic chemistry without a universal shortcut', '''Transition elements commonly show several oxidation states, form coloured compounds and act as catalysts. Their incomplete d subshells are associated with these characteristic behaviours. Outer s and d electrons are relatively close in energy, allowing different numbers to be involved in the formal electron accounting of compounds. Iron(II) and iron(III) are familiar examples of two accessible states.

Coloured transition-ion compounds interact with visible light through their electronic structure. The observed colour depends on the ion and its chemical surroundings. A copper(II) aqueous solution and an iron(III) solution need not have the same colour, and changing the species present can change the appearance. The element name alone does not specify the exact colour of any compound containing it.

Catalytic behaviour can involve changes in oxidation state during intermediate steps or interaction with reactants at a metal surface. The catalyst provides a different pathway and is regenerated overall. A homogeneous catalytic ion and a heterogeneous metal surface can therefore both be useful, with different chemical explanations for their active sites or temporary states. Topic 2.4 supplies the lower-activation-energy interpretation.

Treat these features as characteristic tendencies. They do not imply that a sample lacking visible colour cannot contain a transition element or that an arbitrary transition compound catalyses any reaction. The definition still requires the d-electron criterion, while an application needs evidence about the actual ion or catalyst. In a supplied reaction, a change from Fe2+ to Fe3+ demonstrates variable oxidation state. It does not by itself establish regeneration, which would also need to be shown before calling that reacting iron species a catalyst.''',
 '§19.1 printed pp.1054–1055, coloured ions and oxidation states; §12.7 catalysis; §19.3 electronic colour discussion used qualitatively only.')
add('1-04',[
 'Typical first-row transition metals have higher densities and melting points than calcium, although the comparison has exceptions and is qualitative.',
 'Both calcium and transition metals have metallic bonding and mobile electrons; their physical properties need not have equal magnitudes.'
], 'Contrasting with calcium', '''Calcium is a useful typical s-block comparison. Transition metals such as iron and copper generally have greater densities and higher melting points than calcium. Density means mass per unit volume, so a density comparison describes how much mass occupies the same volume. A melting-point comparison describes the energy-related change needed to disrupt the solid structure sufficiently to become liquid.

Both calcium and these transition metals have metallic bonding and can conduct electricity. Their similarity in bonding type does not make their bond strengths, packing or densities identical. Transition-metal structures involve d as well as s electrons in metallic behaviour, and the combination of electronic structure, atom size and solid arrangement contributes to their characteristic cohesion. A high melting point should be linked to strong metallic bonding rather than to the idea that covalent molecules are being separated.

The word “typical” prevents an overextended rule. The wider d-block region includes metals with unusual melting points, and individual comparisons should use the supplied data. Do not infer that being farther right automatically gives a steadily increasing density or melting point through the entire series. An irregular numerical pattern can coexist with a useful broad contrast against calcium.

For original measurement arithmetic, a metal sample of mass 15.8 g and volume 2.00 cm³ has density 7.90 g cm⁻³. Compared with a supplied calcium density of 1.55 g cm⁻³, it is about 5.10 times as dense. That supports the qualitative density contrast but does not identify the unknown uniquely. Use an electron configuration or additional chemical evidence if identity is requested. This separates a calculated physical property from the electronic definition of a transition element.''',
 '§19.1 printed pp.1054–1055 typical physical properties; §6.5 atom-size patterns. Measurement arithmetic original; supplied calcium comparison datum for practice.')

add('2-01',[
 'The syllabus’s Namibian ore-extraction examples are copper, manganese and uranium.',
 'An ore is a naturally occurring material from which a valuable component can be extracted economically under the relevant circumstances.',
 'The occurrence of an element in an ore does not mean that every site or product yields the pure free metal.'
], 'The Namibian examples and what an ore represents', '''The syllabus uses copper, manganese and uranium as Namibian examples of metal-bearing ore resources. These examples connect classroom redox, solubility and electrolysis with the processing of geological materials. They are curriculum examples, not a current list of operating mines, plant production figures or company ownership. No particular mine's present output is needed to explain their chemistry.

An ore is a naturally occurring material from which a valuable component can be extracted economically in the relevant setting. It normally includes unwanted rock and other minerals as well as the valuable metal-bearing species. The useful component may be an oxide, sulphide or another compound, rather than particles of free metal. Removing the unwanted material and recovering the desired chemical form are distinct stages.

Copper and manganese are d-block examples in this topic, whereas uranium is an actinide included for extraction chemistry. A uranium-bearing ore does not imply that its first saleable product is pure uranium metal. Concentration and chemical conversion can produce intermediate compounds for further processing. Similarly, a manganese-bearing feed may be used to make an alloy such as ferromanganese rather than pure manganese.

For a Namibian processing scenario, identify the feed, the valuable component and the requested product before selecting a method. A statement that a material contains copper does not show whether direct oxide reduction or a leaching route is suitable. Ore composition, concentration, impurities and the product specification influence the choice. Avoid inventing a named plant, a recovery percentage or a commercial claim when only a chemical outline is supplied. The following sections describe the source-backed redox principles and the particular routes required by the syllabus.''',
 'Syllabus §3.3.2, Namibian copper/manganese/uranium examples; OpenStax §19.1 printed pp.1056–1057, ores and preparation.',source='NSSCAS-8224-SYLLABUS')
add('2-02',[
 'In carbon reduction of a suitable metal oxide, the metal species gains electrons while carbon or carbon monoxide is oxidised.',
 'Carbon reduction depends on metal-compound stability and operating temperature; it is not suitable for arbitrary ores or all metals.',
 'Preliminary treatment, reduction and refining have different roles in metal recovery.'
], 'Reduction by carbon', '''A metal in an oxide is already combined with oxygen and has a positive formal oxidation number. Reduction to the free metal lowers that number to zero. Carbon can remove oxygen from suitable oxides at an appropriate temperature, becoming an oxide of carbon. In electron terms the metal species gains electrons and the reducing carbon species is oxidised.

For a simple copper(II) oxide model, 2CuO(s) + C(s) → 2Cu(s) + CO2(g). Copper changes from +2 to 0 while carbon changes from 0 to +4. Under other furnace settings carbon monoxide may instead be the relevant carbon product or reducing species. For example, CuO + CO → Cu + CO2 describes carbon monoxide being oxidised as copper is reduced. State the given route rather than combining inconsistent equations.

Some oxides are too stable for a useful carbon route in the specified setting. Their metals may require electrolysis or a more reactive metal reductant. An ore may also need preliminary conversion into a suitable oxide before reduction. Sulphide roasting, for instance, can change the feed chemistry and produce sulphur dioxide; it is not the same step as reducing an oxide to metal.

Keep three purposes separate. Concentrating or preparing ore increases the useful component or changes it to a more suitable compound. Smelting can combine reduction with melting and separation of a slag. Refining then removes remaining impurities from an impure metal. A balanced reduction equation accounts for atoms and electron changes, but does not alone prove that a furnace achieves pure metal or economical recovery. Topic 2.2 supplies the electron-transfer language needed to explain why carbon is the reducing agent.''',
 '§19.1 printed pp.1057–1060, preparation, smelting, carbon/CO reduction and refining; balanced CuO/carbon route as specified by syllabus §3.3.2.')
add('2-03',[
 'Carbon reduction of copper oxide can give impure copper, with later purification needed for a high-purity product.',
 'Reduction of an iron-oxide/manganese-oxide mixture can produce ferromanganese, an alloy rather than pure manganese.',
 'Carbon acts as the reducing agent in these specified routes and can also contribute to contamination of the metal product.'
], 'Impure copper and ferromanganese', '''The required copper example starts from copper oxide, which carbon reduces to metal. Use an equation consistent with the stated carbon oxide product, such as 2CuO + C → 2Cu + CO2. The copper obtained in a practical feed can contain impurities from the ore, carbon or other processing materials. An equation showing Cu as product does not establish a purity of 100%.

Impure copper may need further refining where a high-conductivity or otherwise high-purity product is required. Electrolytic refining is one possible route, but it starts from an impure metal anode and differs from depositing metal out of a prepared leach solution. Choose the description that fits the feed actually given in the question.

The syllabus's ferromanganese example uses a mixture of iron oxide and manganese oxide reduced with carbon. The product contains both iron and manganese and is an alloy. Its purpose is not to isolate manganese as a pure element. The exact furnace equations depend on the starting oxides and the carbon oxide formed; a generic oxide label cannot supply a unique balanced equation without that information.

If iron(III) oxide and manganese(II) oxide are supplied as model feeds with CO as the carbon product, separate idealised balances are Fe2O3 + 3C → 2Fe + 3CO and MnO + C → Mn + CO. The resulting metals can enter the common alloy product, which can retain carbon and other impurities. These equations illustrate redox bookkeeping rather than a universal plant recipe. A comparison answer should name the target product, the reducing agent and the reason the first metal product may be impure. Calling ferromanganese “manganese ore” would confuse a manufactured alloy with its mineral feed.''',
 'Syllabus §3.3.2 impure copper and ferromanganese examples; OpenStax §19.1 printed pp.1057–1059, carbon reduction and alloys. Particular mixed-feed route retained for independent semantic source review.')
add('2-04',[
 'Sulphuric-acid leaching can transfer suitable metal-bearing material into a solution for later separation and recovery.',
 'Leaching is dissolution or chemical conversion into soluble species, not automatically reduction to the free metal.',
 'The suitability of an acid leach depends on the mineral and any additional chemical requirements.'
], 'Leaching with sulphuric acid', '''Leaching uses a liquid reagent to transfer a valuable component from solid material into a solution. Sulphuric acid is the required example for suitable copper-, manganese- and uranium-bearing feeds. The resulting solution is separated from insoluble residue and prepared for later recovery. The choice of acid does not mean that each mineral dissolves equally rapidly or by the same chemical step.

Copper(II) oxide illustrates a simple acid–base route: CuO(s) + H2SO4(aq) → CuSO4(aq) + H2O(l). Copper stays in the +2 state. Leaching therefore has not produced copper metal; it has moved copper into dissolved copper-containing species. A later electron-gain step is needed to recover the free metal.

For manganese and uranium feeds, the mineral's oxidation state and structure affect what chemical treatment is needed. An acid plus any necessary redox preparation must suit the actual material. Do not infer a unique dissolution equation from an element name alone. At the syllabus's outline level, follow the metal from solid feed to dissolved species and distinguish this from the following extraction stage.

Preparing the solution includes separating residue and removing or controlling impurities that would interfere with recovery. Waste acid and dissolved metals need collection and treatment rather than uncontrolled discharge. That requirement follows from the solution's chemistry even when no named mine or legal discharge limit is supplied. Comparing leaching with carbon reduction, the former changes which phase contains the valuable species, while the latter changes a metal species to the zero-oxidation-state metal. A processing route may combine several stages, so identify each stage by its chemical function rather than calling the whole route “melting the ore”.''',
 'Syllabus §3.3.2 sulphuric-acid leaching examples; OpenStax §19.1 printed pp.1057 and 1060, preparation and hydrometallurgy; CuO acid balance derived from §4.2.',source='NSSCAS-8224-SYLLABUS')
add('2-05',[
 'Electrolysis of an appropriately prepared leach solution can deposit a metal at the cathode by electron gain.',
 'The specified magnesium reduction of uranium is a chemical reduction of a prepared uranium compound, rather than addition of magnesium to an arbitrary aqueous leach.',
 'Magnesium is oxidised as it supplies electrons that reduce the uranium species to metal.'
], 'Recovering metal after solution preparation', '''A prepared metal-bearing solution can be electrolysed to deposit a suitable metal at the cathode. For copper, Cu2+(aq) + 2e− → Cu(s). The supply delivers electrons and the copper-containing solution supplies the metal ions. Suitable electrolyte and electrode operation are necessary; the same result cannot be assumed for an arbitrary mixture of dissolved species.

Manganese recovery likewise needs a controlled process because hydrogen evolution can compete in an aqueous cell. The formal cathode accounting Mn2+ + 2e− → Mn describes the metal-forming step, but does not specify a complete operating method. This is the distinction developed in Topic 2.2 between a school selective-discharge guide and an engineered recovery process.

The uranium example uses magnesium as a chemical reducing agent after the uranium-bearing material has been separated and converted into a suitable prepared compound. It is not a direction to add magnesium to a raw acidic aqueous leach, where reaction with acid and water would compete. Magnesium loses electrons and the uranium species gains them, giving uranium metal in the specified reduction route.

For formal electron accounting with uranium(IV), U4+ + 4e− → U and 2Mg → 2Mg2+ + 4e− show a two-to-one magnesium/uranium amount relationship. Here U4+ represents uranium in the prepared reacting compound, not a claim of free bare ions in an aqueous metal-making experiment. The actual compound supplies the accompanying anions and final salt products. The syllabus requires the reduction principle and reductant, rather than plant-specific preparation details. These examples show that leaching, solution purification and final metal reduction are separate operations; producing a dissolved metal species does not by itself complete extraction of the pure metal.''',
 'Syllabus §3.3.2 electrolysis and magnesium/uranium reduction; OpenStax §17.7 electrolytic deposition and §19.1 p.1057 active-metal reduction of f-block compounds. Uranium electron balance transparently derived; specific precursor/process left to semantic verification.',source='NSSCAS-8224-SYLLABUS')
add('2-06',[
 'Roasting sulphide-containing feeds can release sulphur dioxide; leaching and processing can also produce acidic metal-bearing liquids and dust.',
 'Waste monitoring must identify the pollutant and its pathway; gas capture, liquid treatment and dust collection address different forms of waste.',
 'Neutralising waste acidity alone does not demonstrate that dissolved toxic metals have been removed.'
], 'Monitor a pollutant and control its route', '''Metal extraction can transfer unwanted substances into gases, liquids or solid residues. Roasting a sulphide-containing feed in oxygen can release sulphur dioxide, an air pollutant. Acid leaching can leave acidic liquid containing dissolved metals. Crushing, handling and high-temperature operations can release airborne particles that contain metal-bearing material. Each pathway needs a corresponding monitoring and control approach.

For sulphur dioxide, measure the gas stream and use an appropriate capture or treatment process. Where a sulphuric-acid manufacture stage is included, it can convert a sulphur dioxide feed into a useful product; this still requires control of emissions. A particulate filter alone does not necessarily remove a dissolved or gaseous pollutant. Conversely, a gas absorber does not automatically remove solid dust throughout a site.

For leach waste, monitor acidity and metal concentrations in collected liquids, with treatment appropriate to the actual solution. Neutralisation can reduce acidity, but a neutral pH does not prove that toxic metal species are absent. Some may remain dissolved or be transferred into a solid sludge that itself needs controlled handling. Identify the pollutant before choosing a measure of successful treatment.

For metal-bearing dust, capture particles at relevant sources and limit uncontrolled transport during handling. The risk depends on composition, particle release and exposure, so do not treat a named metal as harmless merely because the ore is solid. In a supplied Namibian processing scenario, link a specific control to a named waste pathway and explain how monitoring shows whether that control works. No invented discharge threshold or legal claim is needed for the chemical reasoning. Waste control is part of evaluating the process rather than an unrelated sentence appended to the extraction equation.''',
 'Syllabus §3.3.2 named waste streams; OpenStax §19.1 pp.1057–1060 roasting/SO2 and hydrometallurgy; §18.10 sulphur dioxide pollution. Controls stated qualitatively, without site-specific engineering or legal limits.')
add('2-07',[
 'Metal ores are finite geological resources, while recovered metal can be reused or recycled.',
 'Recycling can reduce demand for fresh ore and some extraction energy or waste, but requires collection, sorting and processing.',
 'Mixed alloys, contamination and recovery losses can limit recycling purity and yield.'
], 'Benefits and limitations of recycling', '''Ore deposits are finite on human production timescales. Extraction removes material from a particular geological resource, and the remaining ore may become more difficult or costly to process as composition changes. Recycling recovers metal from used products or manufacturing scrap and can reduce the need to extract fresh ore. It does not recreate the geological deposit.

Benefits can include reduced demand for mining, lower use of some extraction stages and less associated waste. The energy saving depends on the metal and recycling route; avoid claiming the same percentage for all metals without data. A relatively clean metal scrap stream can require less chemical reduction than converting an oxide ore into metal, because much of the metal is already in a useful oxidation state.

Problems arise in collecting scattered products, separating different metals and removing contamination. An alloy cannot necessarily be melted directly into a product requiring a different composition or very high purity. Some valuable material is lost during sorting or processing, and recycling itself needs energy and waste controls. A high recovery percentage is useful evidence, but purity and the intended final product also matter.

For a decision, use a named criterion and supplied data. If a recycler collects 1.00 tonne of metal-bearing scrap and recovers 0.800 tonne of acceptable product, the mass recovery is 80.0%. The unaccepted fraction has not vanished; it may include residue, unrecovered metal or impurities that need handling. Recycling can be beneficial while still leaving a need for some fresh material. A reasoned judgement includes avoided extraction, process energy, recovery losses, collection and product quality rather than assuming that calling a route recycling automatically makes its impacts zero.''',
 'Syllabus §3.3.2 finite resources/recycling; OpenStax §19.1 recovery/refining stages. Numerical recovery example original; comparative benefits explicitly conditional.',source='NSSCAS-8224-SYLLABUS')
s=t.wo['item_slots']
qa=[
 ('Describe the syllabus criterion for a transition element in terms of table block, ions and d occupancy. [3]','It is a d-block element [1] forming one or more ions [1] with an incomplete d subshell [1].'),
 ('Explain why copper meets the syllabus transition-element criterion despite its atom having 3d10. [2]','The criterion includes the ions it forms [1]; Cu2+ is 3d9, so it has an incomplete d subshell [1].'),
 ('State the electronic configuration of Fe2+ using an argon core. [1]','[Ar]3d6 [1].'),
 ('Explain why Fe2+ has [Ar]3d6 rather than [Ar]3d4 4s2. [2]','The 4s electrons are removed before 3d when forming these ions [1]; removing iron’s two 4s electrons leaves the six 3d electrons [1].'),
 ('State three characteristic chemical properties of transition elements. [1]','Variable oxidation states, catalytic activity and formation of coloured compounds [1].'),
 ('Suggest the characteristic transition-element property illustrated by Fe2+ and Fe3+ forming in different compounds. [1]','Variable oxidation states [1].'),
 ('Describe typical transition metals compared with calcium in density, melting point and conduction. [3]','They generally have higher densities [1] and higher melting points [1], while both show metallic electrical conduction [1].'),
 ('Contrast iron with calcium in typical density and melting point, while recognising their shared metallic character. [2]','Both are metals, but iron is denser [1] and has a higher melting point than calcium [1].'),
 ('State the three metal-ore examples used for Namibia in this syllabus section. [1]','Copper, manganese and uranium [1].'),
 ('Suggest why including uranium among Namibian extraction examples does not make uranium a first-row d-block transition metal. [1]','The examples concern extraction; uranium is an actinide rather than a first-row d-block element [1].'),
 ('State the redox role of carbon when it removes oxygen from a suitable metal oxide. [1]','It is the reducing agent [1].'),
 ('Suggest why a carbon-reduction equation alone does not establish that the collected metal is pure. [1]','Ore and processing impurities may enter the product, so refining can still be needed [1].'),
 ('State what ferromanganese is in the specified mixed-oxide reduction route. [1]','An iron–manganese alloy that can contain carbon and other impurities [1].'),
 ('Suggest why a mixture of iron oxide and manganese oxide can give ferromanganese rather than pure manganese when reduced with carbon. [1]','Both metal-bearing feeds contribute reduced metals to the common alloy product [1].'),
 ('State the function of sulphuric acid in a suitable metal-ore leaching route. [1]','It transfers suitable metal-bearing material into soluble species for later recovery [1].'),
 ('Suggest why CuO reacting with sulphuric acid to give CuSO4 solution has not yet produced copper metal. [1]','Copper remains in the +2 state in solution; a later reduction to Cu(0) is needed [1].'),
 ('State the reducing agent in the syllabus’s prepared-compound route to uranium metal. [1]','Magnesium [1].'),
 ('Suggest the cathode electron-transfer step for recovering copper metal from a prepared Cu2+ leach solution. [1]','Cu2+(aq) + 2e− → Cu(s) [1].'),
 ('State one gaseous pollutant associated with roasting sulphide ores. [1]','Sulphur dioxide [1].'),
 ('Explain why neutral pH alone does not demonstrate that treated leach waste is free of toxic metals. [2]','pH indicates acidity rather than metal concentration [1]; metal species can remain dissolved or be transferred into waste solids, so they need separate monitoring [1].'),
 ('State what makes metal ores finite resources. [1]','The usable geological deposits are limited and are not replaced on human extraction timescales [1].'),
 ('Explain why recycling metal can reduce fresh-ore demand while still producing waste. [2]','Recovered metal replaces some new extraction [1], but sorting, contamination and recovery losses leave residues requiring handling [1].')
]
assert len(qa)==len(s)
for slot,(prompt,answer) in zip(s,qa):
 st='WHY' if slot['subtype']=='MECH' else None
 t.item(slot,prompt,answer,subtype=st)
 if st:t.deviations.append({'from':slot['slot']+' MECH','to':'WHY; preserve original AO/Bloom/command/tariff','why':'The ion-based classification explanation does not have a reaction intermediate or product mechanism.'})
p=t.wo['performance_tasks']
t.item(p[0],'''Identify one correct option per question. [7]
1. The syllabus criterion refers to a d-block element forming an ion with: A an incomplete d subshell; B any full shell; C no electrons; D a negative nucleus.
2. Fe2+ from Fe [Ar]3d6 4s2 is: A [Ar]3d4 4s2; B [Ar]3d6; C [Ar]3d8; D [Ar]3d5.
3. Cu2+ is 3d9. This means its d subshell: A is full; B is empty; C is incomplete; D holds only two electrons.
4. Fe2+ and Fe3+ illustrate: A identical oxidation state; B isotope variation; C neutron transfer; D variable oxidation states.
5. Compared with calcium, iron typically has: A higher density and melting point; B lower density and melting point; C no electrical conductivity; D a molecular solid structure.
6. A catalyst is distinguished from a consumed reducing reagent by: A absence from all steps; B regeneration overall; C an assumed colour; D lack of interaction with reactants.
7. The 3d5 box occupancy consistent with singly filling equivalent orbitals is: A [↑↓][↑↓][↑][ ][ ]; B [↑↓][↑][↑][↑][↑]; C [↑][↑][↑][↑][↑]; D [↑↓][↑↓][↑↓][↑↓][↑↓].''',
 '''Key: 1 A, 2 B, 3 C, 4 D, 5 A, 6 B, 7 C; one mark per correct option.
1. A is the ion criterion. B ignores d occupancy; C describes a fully stripped atom; D contradicts nuclear charge.
2. B removes two 4s electrons. A removes the wrong subshell first; C adds d electrons; D removes three electrons overall.
3. C is nine of a possible ten. A needs ten; B needs zero; D confuses one orbital with the subshell.
4. D concerns +2 and +3. A ignores the difference; B concerns neutrons; C describes neither ion conversion.
5. A is the typical comparison. B reverses it; C ignores metallic conduction; D assigns an inappropriate molecular structure.
6. B is the catalytic distinction. A wrongly excludes temporary participation; C is not sufficient evidence of catalysis; D removes the pathway interaction.
7. C has five parallel single occupancies. A pairs prematurely; B contains six electrons; D contains ten.''')
t.item(p[1],'''Explain the following linked electronic and extraction examples. [8]
(a) Write Fe2+ in core notation and construct its five-box 3d occupancy. [2]
(b) Explain what Fe2+/Fe3+ shows about oxidation states and why it does not alone prove catalytic action. [2]
(c) Write the cathode half-equation for copper deposition from a prepared aqueous Cu2+ leach. [2]
(d) Explain the electron-transfer roles when magnesium reduces a prepared uranium compound to metal. [2]''',
 '''Part (a): [Ar]3d6 [1]; five d boxes [↑↓][↑][↑][↑][↑] with correct electron count and opposite-spin pair [1].
Part (b): different iron oxidation states show variable oxidation state [1]; catalysis also requires an appropriate rate effect and regeneration, which the two labels alone do not establish [1].
Part (c): Cu2+(aq) + 2e− → Cu(s). Correct species/states [1]; electron/charge balance [1].
Part (d): magnesium loses electrons and is oxidised [1]; the uranium species gains electrons and is reduced [1]. This concerns a prepared compound, not direct magnesium addition to an arbitrary acid leach. Each bracket is a separate creditworthy point.''')
t.item(p[2],'''Calculate and interpret the properties of an original iron sample with mass 15.8 g and volume 2.00 cm³. Take calcium’s comparison density as 1.55 g cm⁻³. Iron atoms have [Ar]3d6 4s2. [5]
(a) Calculate the iron sample density and its ratio to the calcium value, to three significant figures. [2]
(b) Give the Fe2+ configuration. [1]
(c) Use its d occupancy to state why iron meets the syllabus transition-element criterion. [1]
(d) State the characteristic property shown by the existence of Fe2+ and Fe3+. [1]''',
 '''(a) Equation density = mass/volume; working 15.8/2.00 = 7.90 g cm⁻³ to three significant figures [1]. Ratio = 7.90/1.55 = 5.10, dimensionless to three significant figures [1]. Units are already consistent and need no conversion; this supports a higher-density comparison with calcium.
(b) [Ar]3d6 [1], after removing the two 4s electrons.
(c) It forms an ion with an incomplete d subshell [1].
(d) Variable oxidation states [1].''')
t.deviations.append({'from':'Configuration objective with a WHY practice slot','to':'Preserve the slot and add explicit five-box construction in the structured task','why':'The syllabus requires both configuration and electrons-in-boxes notation, so the bank must practise producing both rather than only reading a configuration.'})
t.deviations.append({'from':'Metallurgy examples grouped under transition elements','to':'Identify uranium as an actinide and separate prepared-compound reduction from aqueous leaching','why':'The grouping is topical, not a d-block classification, and magnesium reduction must not be misrepresented as direct aqueous deposition.'})
t.deviations.append({'from':'Local general-reference coverage limits','to':'Record Namibia-specific route details, ferromanganese feed and uranium precursor as semantic-review focus','why':'The syllabus supplies the examples and reduction principles; the general textbook does not directly establish all local industrial details. No current plant claim or recipe is introduced.'})
t.save()
