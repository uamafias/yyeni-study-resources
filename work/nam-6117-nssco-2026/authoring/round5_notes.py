"""Additional teaching, distinct from new assessment prompts and numeric instances."""
NOTES={
1:('Measurement precision and significant figures', '''Significant figures describe the precision retained in a number, not its size. Leading zeros locate the decimal point and do not count: 0.00470 has three significant figures. Zeros between non-zero digits do count. A final zero after a decimal point can record precision: 6.20 has three significant figures whereas 6.2 has two. Scientific notation makes this unambiguous; 4.50 × 10³ carries three significant figures.

Keep extra digits during a calculation and round the final result. For multiplication or division, the least precise measured input usually limits the final significant figures. For addition and subtraction, consider decimal places. A measured value should not acquire extra precision merely because a calculator displays more digits. Exact counting numbers and defined conversions do not limit precision in the same way as measurements. For example, 1 dm³ = 1000 cm³ is an exact conversion.

Accuracy concerns closeness to a reference value; precision concerns agreement among repeated measurements. A balance that always reads too high may give precise results with poor accuracy. Repeating and averaging reduces the influence of random scatter but cannot remove a constant zero offset. Check calibration or the empty reading, record the correction and keep the original observations. A single apparently plausible result is not evidence that an instrument is calibrated.'''),
2:('Atoms, ionic diagrams and isotope calculations', '''The electron has relative charge −1 and a mass about 1/1840 of the proton’s. A proton has charge +1 and relative mass 1; a neutron has charge 0 and relative mass 1. A neutral atom has equal proton and electron counts. The nucleus contains the protons and neutrons; its nucleon number is their total. Losing electrons changes charge without changing the identity of the element.

In a Bohr diagram for a first-twenty-element atom, label the nucleus, then distribute the electrons in shells. The first shell holds two; the second holds eight. The simple syllabus patterns for potassium and calcium extend into a fourth shell. A shell is a model of electron arrangement, not a scale drawing of an orbit. Check the total number of electrons against the proton count before adding a charge label.

An ionic dot-and-cross diagram shows transferred electrons, not a shared pair between the final ions. For sodium chloride, sodium loses its outer electron and chlorine gains it. Enclose each resulting ion in brackets and place the charge outside. Chloride’s outer shell contains seven original electrons and one transferred electron. For a Group II metal with a Group VII non-metal, two non-metal ions are needed for each 2+ metal ion. Distinguish dots from crosses by origin; all electrons have the same charge.

Isotopes have the same proton number but different neutron counts. Relative atomic mass is an abundance-weighted mean, not an unweighted midpoint unless the isotope abundances are equal. A sample made of 80% mass-10 atoms and 20% mass-11 atoms has mean mass 10.2 relative units. Changing abundance changes the mean without changing either isotope’s mass. Radioactive decay changes an unstable nucleus by emission of radiation/particles; it is not loss of an outer-shell electron in a chemical reaction. No identification of radiation types or half-life calculation is required here.

Group I metals react with cold water to form an alkaline hydroxide solution and hydrogen. Lithium, sodium and potassium become more vigorous down the group. Balance atoms when writing an equation: two metal atoms and two water molecules produce two hydroxide formula units and one hydrogen molecule. These are teacher demonstrations; potassium and sodium must not be tested with dilute acids.'''),
4:('From formula to amount, particles and solution concentration', '''Relative formula mass is found by counting every atom, including brackets. For Mg(OH)2, the oxygen and hydrogen counts are each two; its relative formula mass is 24 + 2(16 + 1) = 58. Molar mass uses the same numerical value in g/mol. An amount is obtained by dividing sample mass by molar mass. Converting in the reverse direction multiplies amount by molar mass.

The Avogadro constant connects amount to particle count. Multiply moles by about 6.022 × 10²³ particles per mole, naming the counted particles: atoms, molecules, ions or formula units. One mole of a molecular substance does not necessarily contain one mole of atoms; count atoms per molecule before making that conversion.

Mass concentration divides mass by solution volume, while amount concentration divides moles by solution volume. Convert a volume in cm³ to dm³ before using a concentration in g/dm³ or mol/dm³. Concentration concerns the final solution volume, not the volume of solvent initially poured in.

An acid–alkali calculation starts with the balanced equation, not an assumed 1:1 ratio. A formula unit with two neutralisable hydrogen ions can require two hydroxide ions. Determine the known amount, use the coefficients to obtain the other amount, then divide by its solution volume if concentration is required. In a mixture with two known amounts, compare amount divided by its reaction coefficient. The smaller value limits the extent of reaction; the other reactant remains in excess.'''),
5:('Electrolysis vocabulary and half-equations', '''An electrolyte conducts through moving ions when molten or dissolved and undergoes chemical decomposition during electrolysis. A solid ionic lattice contains charged particles but cannot conduct through them while they remain fixed. Electrodes carry current between the external wires and the electrolyte.

In an electrolytic cell the anode is positive and oxidation occurs there; the cathode is negative and reduction occurs there. Write electrons on the product side for electron loss, and on the reactant side for electron gain. Balance charge as well as atoms. With a copper electrode present, distinguish cathode deposition from anode dissolution. For copper deposition, Cu²⁺ + 2e⁻ → Cu; for chloride oxidation, 2Cl⁻ → Cl2 + 2e⁻. The diatomic product requires two chloride ions. Keep a half-equation separate from the overall equation so the electron transfer is visible.'''),
6:('Reading energy profiles and extraction redox', '''On an energy profile, activation energy is measured from the reactant level to the peak. Reaction enthalpy change is measured from reactants to products, retaining its sign. A lower product level gives a negative change and an exothermic reaction. Do not measure activation energy from the graph’s zero unless the reactants happen to lie there. A catalyst lowers the peak for the reaction pathway without changing reactant and product levels.

During extraction, the substance removing oxygen from a metal oxide is the reducing agent. It is itself oxidised. Carbon monoxide can take oxygen from iron oxide and become carbon dioxide while iron is formed. Identify both changes from the actual equation because the role of a carbon-containing substance depends on the reaction.'''),
7:('Solubility exceptions and the acid–metal gas', '''The syllabus’s lead-compound rule has two soluble exceptions: lead nitrate and lead ethanoate. Most hydroxides are insoluble, but Group I hydroxides and barium hydroxide are soluble; calcium hydroxide is only slightly soluble. These exceptions matter when choosing a precipitation method. An intended product that stays dissolved cannot be recovered as a precipitate by ordinary filtration.

A suitable reactive metal with dilute acid produces a salt and hydrogen. Test a small separately collected gas sample with a lighted splint; a squeaky pop supports hydrogen. A glowing splint tests oxygen, not hydrogen. Do not bring a flame to the reaction vessel while gas is being generated.'''),
9:('Metal properties, reactivity and observations', '''Metals generally conduct heat and electricity, are malleable and ductile, and have a metallic appearance on a clean surface. Electrical conduction depends on delocalised electrons moving through the structure. Malleability is different from hardness: a metal may resist scratching yet still be capable of shaping. Alloying can impede layer movement, but properties depend on composition and treatment. Selection for an application must consider the actual loads, corrosion conditions and manufacturing process.

The syllabus reactivity sequence is potassium, sodium, calcium, magnesium, aluminium, carbon, zinc, iron, tin, lead, hydrogen, copper, silver, gold and platinum. Carbon and hydrogen are reference positions, not metals. Carbon’s position helps judge which metal oxides can be reduced by carbon. Hydrogen’s position helps predict displacement of hydrogen from dilute acid. Do not infer that reaction speed always gives the exact order: an oxide film, temperature and surface area can affect the observations.

Potassium and sodium are demonstrated only with cold water. They form hydroxides and hydrogen. Calcium also reacts with cold water, giving gas bubbles and calcium hydroxide; a cloudy mixture may develop. Magnesium reacts only slowly with cold water but reacts more readily with steam, producing magnesium oxide and hydrogen. Hot iron reacts with steam; copper does not displace hydrogen from water or dilute hydrochloric acid under ordinary test conditions. Never add sodium or potassium to dilute acid.

Magnesium, zinc and iron can dissolve in dilute hydrochloric acid with bubbles of hydrogen, with rates depending on conditions. Aluminium may initially appear unreactive because its adherent oxide layer blocks contact. Copper below hydrogen shows no comparable reaction with dilute hydrochloric acid. An observation is what is seen: bubbles, a dissolving solid, a deposit or a colour change. The identity of the gas or ion is an inference requiring the relevant evidence.

A more reactive metal can displace a less reactive one from its aqueous salt. A deposit on a strip and a changing solution colour can support displacement, but use the actual metal and solution identities before writing the equation. A set of displacement results can establish a relative order without knowing any rate. Conflicting results should prompt checking contamination, surface films and whether a visible change actually occurred.

Many metal oxides, such as magnesium oxide, are basic and react with acids to give a salt and water. Many non-metal oxides, such as sulfur dioxide, are acidic. Aluminium oxide is amphoteric: it reacts with both acids and strong alkalis. These are chemical classifications, not rules based solely on colour or whether the solid dissolves in water.'''),
10:('Petroleum fractions, structures and tests', '''The syllabus assigns fuel oil to fuel for ships and home heating systems. The lubricating fraction supplies lubricants, waxes and polishes. Keep these distinct from diesel fuel and from bitumen used for roads. Fractional distillation separates a mixture by boiling behaviour; cracking instead breaks larger molecules into smaller molecules.

Structural isomers have the same molecular formula but different connectivity. Rotating a drawing does not create an isomer. For pentane, compare a straight chain, a four-carbon chain with one methyl branch, and a three-carbon chain with two methyl branches on the central carbon. Count five carbon atoms in every representation. In propanol, moving the OH from an end carbon to the middle carbon gives propan-1-ol and propan-2-ol; both retain the same molecular formula.

Name an unbranched compound by carbon count and functional group, numbering the chain to locate a double bond or OH group where necessary. Include the carbon of a COOH group in the chain count. Ethyl ethanoate’s name contains the alcohol-derived ethyl part and the acid-derived ethanoate part.

Cold dilute acidified potassium manganate(VII) is purple. An alkene removes that colour under the stated test conditions, while a simple alkane does not. Bromine water is an alternative unsaturation test away from ultraviolet light. State reagent and conditions before interpreting an observation; neither test identifies one unique compound from colour change alone.'''),
11:('Water identification and industrial conditions', '''A chemical water test establishes presence, not purity. White anhydrous copper(II) sulfate becomes blue with water. Blue cobalt(II) chloride paper becomes pink. A solution containing salts can give a positive result, so purity needs a physical test at controlled conditions, such as a boiling or melting point.

For syllabus answers on Namibia’s water scarcity, retain the stated limitation: seawater desalination is expensive and is not presented as the solution to the national water-scarcity problem. The curriculum does not require assessment of a particular modern plant. Infrastructure and energy costs matter, but an unverified project webpage is not evidence for an examinable claim.

The Haber process uses nitrogen and hydrogen, commonly in a 1:3 feed ratio, an iron catalyst, about 450 °C and high pressure of about 200 atm. Nitrogen comes from air; hydrogen may come from hydrocarbons reacting with steam. Temperature is a compromise between rate and equilibrium yield. A catalyst speeds approach to equilibrium without increasing the equilibrium yield at fixed conditions.

The Contact process makes sulfur dioxide from sulfur and oxygen, then oxidises it reversibly to sulfur trioxide over vanadium(V) oxide near 450 °C and about atmospheric pressure. The equation is 2SO2 + O2 ⇌ 2SO3. Industrial absorption into concentrated sulfuric acid avoids the acid mist produced by direct reaction with water; subsequent dilution produces the required acid.

Nitrogen, phosphorus and potassium are all plant nutrients. Fertiliser selection should respond to deficiencies, rather than increasing nutrients indiscriminately. Nitrogen supports protein formation and growth; phosphorus supports root development; potassium supports healthy growth and physiological function. Run-off of excessive fertiliser can cause eutrophication.

Dry air contains about 78% nitrogen, 21% oxygen and 1% other gases. Removing oxygen does not leave pure nitrogen, because the other gases remain. Carbon dioxide forms during complete combustion, aerobic respiration, fermentation, acid–carbonate reactions and decomposition of suitable carbonates. Heating limestone gives calcium oxide and carbon dioxide. Adding water to calcium oxide makes calcium hydroxide; both the oxide and hydroxide have basic uses, such as neutralising acidic soils or waste.'''),
12:('Limits of repeated measurements', '''Repeats reveal scatter and allow a more stable mean when random variation is present. They do not prove that a shared instrument offset is absent. Compare an instrument with a calibrated reference, check its zero and record the circumstances. A graph can show a consistent trend even when every temperature has the same offset; the gradient may remain meaningful while absolute temperature values are wrong. Distinguish evidence for repeatability from evidence for accuracy before drawing a conclusion.''')}
ANNEX='''The following consolidated reference paraphrases syllabus Annexe B (PDF page 49, printed page 46). Record precipitate colour separately from the colour of a solution, and use fresh portions for different tests.

| Ion | Aqueous NaOH | Aqueous ammonia |
|---|---|---|
| Al³⁺ | White precipitate; dissolves in excess to a colourless solution | White precipitate remains in excess |
| Zn²⁺ | White precipitate; dissolves in excess to colourless solution | White precipitate; dissolves in excess to colourless solution |
| Ca²⁺ | White precipitate remains in excess | No precipitate or a very slight white precipitate |
| Cu²⁺ | Light-blue precipitate remains in excess | Light-blue precipitate dissolves in excess, giving dark-blue solution |
| Fe²⁺ | Green precipitate remains in excess | Green precipitate remains in excess |
| Fe³⁺ | Red-brown precipitate remains in excess | Red-brown precipitate remains in excess |
| NH4⁺ | Warm carefully: ammonia released | Not the ammonium test |

| Anion | Reagent sequence | Positive observation |
|---|---|---|
| Carbonate | Dilute acid; test evolved gas with limewater | Bubbles; gas makes limewater milky |
| Chloride | Dilute nitric acid, then silver nitrate | White precipitate, soluble in dilute ammonia |
| Bromide | Dilute nitric acid, then silver nitrate | Cream precipitate, insoluble in dilute ammonia |
| Iodide | Dilute nitric acid, then silver nitrate | Yellow precipitate |
| Nitrate | Sodium hydroxide and aluminium foil; warm carefully | Ammonia released |
| Sulfate | Dilute nitric acid, then barium nitrate | White precipitate |

| Flame-test ion | Colour |
|---|---|
| Lithium | Red |
| Sodium | Bright yellow |
| Potassium | Lilac |
| Calcium | Brick-red |
| Barium | Green |

| Gas | Test and positive result |
|---|---|
| Ammonia | Damp red litmus becomes blue |
| Carbon dioxide | Limewater becomes milky |
| Chlorine | Damp litmus is bleached |
| Hydrogen | A lighted splint gives a pop with a small collected sample |
| Oxygen | A glowing splint relights |

A reference-table match supports an identification only under the stated reagent and excess conditions. A contaminated wire or reagent can produce the same visible result as a sample ion. Check a blank when contamination is suspected. Colour alone is rarely enough: aluminium and zinc both form white precipitates, but their behaviour with excess ammonia differs.'''
NOTES[8]=('Qualitative analysis: consolidated Annexe B reference',ANNEX)
METAL_PROPERTIES='''A physical property describes behaviour without changing chemical identity. Conductivity can be tested with a complete low-voltage circuit; deformation under a load can be tested separately. A shiny surface alone is weak evidence for classifying a material, because coatings and some non-metals can also appear shiny. Identify the property required by the application before selecting a material.

A wire must conduct and must be drawn into a long, thin shape without breaking: conductivity and ductility serve different requirements. A saucepan body needs thermal conduction, whereas its handle should limit heat transfer. A structure supported over a long distance may need low density as well as adequate strength. Hardness describes resistance to scratching or indentation; strength describes resistance to failure under load. These words should not be treated as interchangeable.

Metals commonly have high melting points and densities, but these are trends, not definitions. Mercury is liquid at ordinary room temperature, and some Group I metals have low densities. Graphite is a non-metallic form of carbon that conducts electricity, so a conducting sample is not automatically a metal. A classification should use several properties together and, where available, the particle model.

In a metallic model, positive ions occupy a lattice and delocalised electrons move through the structure. The electrons are not each attached permanently to one particular ion. Electrical charge can therefore move even while the ions stay in their approximate positions. When layers move during shaping, attraction to the surrounding electrons can maintain bonding. By contrast, shifting an ionic lattice can bring like charges together and cause repulsion and fracture.

An alloy model retains the metallic structure but includes more than one element. Different-sized atoms can obstruct easy movement of layers, making deformation harder. The diagram should distinguish the added atoms without showing a separate molecular compound at each lattice site. The composition can vary, and the resulting hardness, corrosion resistance and ductility must be assessed for the proposed use rather than inferred from the word alloy alone.'''
