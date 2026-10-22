"""Original periodicity manuscript: general trends, specified compounds and inference."""
from authoring_common_8224 import Topic
t=Topic('3.1')
def add(short,claims,title,text,loc):t.objective(short,claims,[(title,text)],'OpenStax-Chemistry',loc)
add('1-01',[
 'First ionisation energy is the energy required to remove one electron from each atom in one mole of gaseous atoms, forming one mole of gaseous singly positive ions.',
 'Ionisation requires energy and is represented by X(g) → X+(g) + e− for the first removal.'
], 'Ionisation energy specifies particles and states', '''First ionisation energy is the energy required to remove one electron from each atom in one mole of gaseous atoms, forming one mole of gaseous singly positive ions. The equation is X(g) → X+(g) + e−. “Gaseous” excludes energy changes involved in melting, vaporising or dissolving a sample. “First” specifies removal from a neutral atom rather than from an ion that has already lost electrons.

Ionisation requires an energy input to overcome the attraction between the nucleus and the electron. A molar ionisation energy is positive and is commonly quoted in kJ mol⁻¹. It is not the energy released when an atom gains an electron, and it is not a measure of the mass of the electron. The electron symbol accounts for the negative charge removed; the gaseous atom becomes a 1+ ion.

For a supplied first ionisation energy of 600 kJ mol⁻¹, ionising 0.0200 mol of separate gaseous atoms requires 12.0 kJ under the stated ideal amount basis. The calculation is energy = amount × molar ionisation energy. The example does not include energy to obtain those gaseous atoms from a solid sample. Such additional steps would need their own data.

Second ionisation instead removes an electron from each gaseous singly positive ion: X+(g) → X2+(g) + e−. Successive values describe different starting particles. A large jump after a given number of removals can indicate that further removal reaches an inner shell. When interpreting a series, count which electron is being removed before assigning the jump. The definition, equation and amount basis make ionisation data usable for comparing elements and inferring their outer-electron arrangements.''',
 '§6.5, printed pp.323–327 (PDF pp.333–337), ionisation definitions and successive values.')
add('1-02',[
 'Greater nuclear attraction to the removed electron generally increases ionisation energy, while greater distance and shielding generally reduce it.',
 'Inner electrons shield outer electrons from nuclear charge; nuclear charge alone cannot determine an ionisation comparison.',
 'Electron shell and subshell energy influence how strongly an electron is held.'
], 'Explaining attraction rather than quoting a trend', '''An electron is attracted to the positive nucleus. For comparable electronic arrangements, a larger nuclear charge tends to hold it more strongly and raises the energy needed to remove it. The comparison must also account for the electron's distance and shielding. More protons do not by themselves prove that an atom has the larger ionisation energy.

An outer electron farther from the nucleus is generally less strongly attracted. Inner electrons shield it from part of the nuclear attraction, reducing the effective pull it experiences. Down a group, added shells make outer electrons more distant and increase shielding. These effects can outweigh the increase in proton number, explaining why removal becomes easier even though the nucleus has greater charge.

Across a period, electrons are added to the same main shell while nuclear charge increases. Inner-shell shielding changes relatively little, so the outer electrons tend to feel a stronger effective attraction. This provides a general reason for a rise in first ionisation energy. Shell and subshell energies also matter to the detailed pattern; use the scope of the question rather than turning the broad trend into a strict step-by-step rule.

For an explanation, name the particles and connect cause to consequence: greater shielding and distance reduce attraction between nucleus and outer electron, so less energy is needed for removal. Merely saying that an atom has more electrons leaves out their location and effect. Likewise, “it has a bigger nucleus” does not specify nuclear charge. Use the electron arrangement developed in Topic 1.2 to decide which electrons shield and which electron is removed. Keep the comparison tied to gaseous atoms for first ionisation, not to the size of a solid metal sample.''',
 '§6.5 printed pp.319–327, effective nuclear charge, shielding and ionisation.')
add('1-03',[
 'Across Period 3, comparable atomic radii generally decrease as nuclear charge rises with little change in inner shielding.',
 'Na+, Mg2+ and Al3+ form a decreasing-radius isoelectronic sequence; P3−, S2− and Cl− form a separate decreasing-radius sequence.',
 'Electronegativity generally increases from sodium to chlorine; an ordinary electronegativity comparison does not assign argon an assumed high value.'
], 'Radius and electronegativity across Period 3', '''Across Period 3, nuclear charge increases while electrons enter the third main shell. Comparable atomic radii generally decrease because inner-shell shielding changes relatively little and effective attraction strengthens. The added electrons do not force a general expansion: increased positive charge draws the outer distribution closer to the nucleus. Use the same radius definition when comparing measurements; a van der Waals radius is not directly interchangeable with a covalent radius.

Ionic radii need separate comparisons. Na+, Mg2+ and Al3+ each contain ten electrons. Their radii decrease in that order because the same electron population experiences increasing nuclear charge. These cations are smaller than their parent atoms, with the third shell emptied in these examples. In contrast, P3−, S2− and Cl− each have eighteen electrons and retain a third shell. Within that sequence, increasing nuclear charge again contracts the electron cloud, so radius decreases from P3− to Cl−.

Do not join the two ion sequences into one smooth decreasing line across the period. Moving from small cations to larger anions changes the shell population and ionic charge. An anion is generally larger than its parent atom because adding electrons increases electron repulsion without adding protons. State the ions being compared rather than treating “ionic radius” as a unique value for an element without a charge.

Electronegativity is the ability of an atom in a bond to attract the shared electron pair. It generally increases from sodium towards chlorine as atomic size falls and effective nuclear attraction rises. Argon is not assigned an ordinary value merely by extending the line, because the usual comparison concerns bonded atoms. These ideas link the Period 3 trend to the bond polarity explained in Topic 1.3.''',
 '§6.5 printed pp.320–324, radii and isoelectronic series; §7.2, electronegativity and polar bonds.')
add('1-04',[
 'First ionisation energy shows a general increase across Period 3 as effective nuclear attraction rises and atomic radius falls.',
 'A general periodic trend need not be monotonic; the syllabus requires the broad attraction explanation rather than detailed orbital-pairing analysis.'
], 'The general first-ionisation trend', '''From sodium towards argon, first ionisation energy generally rises. Sodium has a relatively easily removed outer electron, while argon's outer electrons are held much more strongly. The general explanation is increasing nuclear charge across the period, electrons entering the same main shell and a reduction in atomic radius. Inner shielding does not increase enough to cancel the extra positive charge.

Removing an electron from the right-hand end therefore generally requires more energy. State that the comparison concerns separate gaseous atoms and the first electron removed. Conductivity, melting point and chemical reactivity describe different properties and do not substitute for the nuclear-attraction explanation.

The word “general” matters. Experimental first ionisation energies do not form a perfectly smooth increasing series. Do not erase a local decrease in supplied data simply to preserve a memorised arrow across the table. Describe the broad pattern and any stated departure accurately, while keeping the explanation at the required level. The common-shell, rising-nuclear-charge account explains the overall trend; it does not assert that electronic details have no influence.

When using a table, identify the start and end of the period and the units before comparing. A larger positive value means more energy is required per mole for the defined removal, not a greater amount of energy released. An unknown with a much lower first value than its neighbours may have a more weakly held outer electron, but identity normally needs additional evidence. Successive ionisation data can provide a different clue about how many outer electrons are removed before an inner shell is reached. These comparisons use the same definition, keeping atom, ion and bulk-property evidence separate.''',
 '§6.5 printed pp.324–327; syllabus §3.1.1 sets the required general explanation and exclusion of detailed pairing effects.')
add('1-05',[
 'Sodium, magnesium and aluminium have metallic structures with mobile delocalised electrons; silicon has a giant covalent network.',
 'Phosphorus, sulphur and chlorine have molecular structures, while argon is monatomic, with lower melting points than silicon’s covalent network.',
 'Electrical conductivity across Period 3 depends on mobile charge carriers rather than melting point alone.'
], 'Melting and conduction depend on structure', '''Period 3 changes from metallic structures through a giant covalent network to molecular and monatomic substances. Sodium, magnesium and aluminium have positive metal centres attracted to delocalised electrons. Their metallic bonds must be overcome during melting, and their mobile electrons carry current in the solid. Melting points generally rise across these three as metal-ion charge and the supply of delocalised electrons increase, with size also affecting attraction.

Silicon has a giant covalent network. Melting requires disruption of strong covalent bonding throughout the extended structure, giving a high melting point. It is a semiconductor rather than an ordinary good metallic conductor. Its conductivity depends on the availability of mobile carriers and the material's state; a giant structure alone is not enough to classify electrical behaviour.

White phosphorus contains P4 molecules, sulphur contains S8 molecules and chlorine contains Cl2 molecules in their familiar elemental forms. Melting these molecular solids overcomes intermolecular attractions rather than breaking their covalent molecules apart. Their melting points are much lower than silicon's. Sulphur's larger molecular electron population gives stronger dispersion attractions than the small P4 or Cl2 comparison would suggest from position alone. Argon is monatomic and has weak dispersion attractions between atoms, giving a very low melting point.

These non-metal molecular and atomic substances lack the mobile charged particles needed for ordinary electrical conduction. Do not explain their low melting points by calling their internal covalent bonds weak. Nor should the high melting point of silicon be used to infer that it conducts as well as aluminium. Identify structure, the interactions disrupted on melting, and the available charge carriers separately. This applies Topic 1.3's structure–property reasoning to a whole period rather than treating each numerical property as an isolated fact.''',
 '§§6.5, 7.1–7.2 and 10.5, metallic/nonmetallic and solid structures; §18.3 representative elemental properties.')

add('2-01',[
 'Atomic radii and radii of comparable ions generally increase down Groups 2 and 17 because additional shells increase distance and shielding.',
 'Electronegativity generally decreases down these groups as bonding electrons are farther from and more shielded from the nucleus.'
], 'Comparing atoms and ions down a group', '''Down Group 2 or Group 17, atoms have additional occupied main shells. Their outer electrons lie farther from the nucleus, and inner electrons provide more shielding. Atomic radius therefore generally increases despite the larger nuclear charge. A valid explanation includes both the rising proton number and why distance and shielding dominate its effect on the outer region.

Comparable ions also become larger down these groups. In Group 2 compare the 2+ cations, such as Mg2+ and Ca2+. In Group 17 compare the 1− anions, such as F−, Cl− and Br−. The lower member has more occupied shells. Do not mix a neutral atom of one element with an ion of another and describe the result as the group ionic-radius trend.

Electronegativity generally decreases down each group. The shared electron pair in a bond is farther from the nucleus and experiences greater shielding, so the attraction for it is reduced. Increased nuclear charge alone would suggest stronger attraction, but omits the larger electron structure. This is why a statement that “more protons means higher electronegativity” needs a controlled comparison rather than being applied without considering shell number.

For an unfamiliar Group 17 member below chlorine, a reasonable prediction is a larger atom and halide ion, with lower electronegativity than chlorine. This prediction uses relative position, not an invented numerical radius. If a question supplies measured radii, confirm that they refer to the same charge and radius convention. Group 2 metal and Group 17 non-metal chemistry differ, but the distance-and-shielding argument can be applied to both when the compared quantities are defined consistently. Topics 3.2 and 3.4 develop the chemical consequences.''',
 '§6.5 printed pp.319–324; §7.2 electronegativity trends.')
add('2-02',[
 'First ionisation energy generally decreases down Groups 2 and 17 because distance and shielding reduce attraction to the removed outer electron.',
 'Increasing nuclear charge down a group does not outweigh the additional-shell effects in the general first-ionisation trend.'
], 'Ionisation down Groups 2 and 17', '''First ionisation energy generally decreases down Group 2 and down Group 17. The removed electron occupies an outer shell at greater average distance from the nucleus. More inner electrons shield it. Less energy is needed to overcome the effective attraction, even though the lower element contains more protons.

For a Group 2 comparison, the outer electrons retain the same general valence pattern while main shell number increases. Removing the first electron from a lower gaseous atom is therefore easier in the broad trend. For halogen atoms, the outer-shell arrangement also repeats down the group, and the added shells similarly reduce the energy needed for first removal. This statement concerns ionisation, not the halogens' tendency to gain an electron in a separate reaction.

Use a full chain in an explanation: added shells give greater radius and shielding; the removed electron experiences weaker effective attraction; first ionisation energy decreases. A statement that lower atoms have “more shielding” without identifying the inner electrons or the nucleus–electron attraction is incomplete reasoning. Conversely, a statement about increased proton number alone predicts the wrong general direction for this comparison.

If supplied data ask for a comparison between two different groups as well as two periods, do not apply a one-dimensional trend blindly. Identify shell number, nuclear charge and the electron being removed. Group trends are most directly useful when comparing members of the same group. In an unknown-element problem, combine the general ionisation trend with evidence about ion charge, outer electrons or chemical reactions before assigning a position. This avoids treating one energy value as a unique fingerprint independent of the rest of the periodic pattern.''',
 '§6.5 printed pp.324–327, group trend and shielding.')

add('3-01',[
 'The specified Period 3 oxide products include Na2O, MgO, Al2O3, P4O10, SO2 and SO3; equations must describe the intended oxidation product.',
 'The specified chloride products are NaCl, MgCl2, Al2Cl6, SiCl4 and PCl5.',
 'Sodium reacts readily with cold water to form NaOH and hydrogen; magnesium reacts slowly with cold water but more readily with steam to form MgO and hydrogen.'
], 'Specified reactions with oxygen, chlorine and water', '''Write the intended product before balancing a Period 3 combination reaction. For the specified oxides, 4Na(s) + O2(g) → 2Na2O(s), 2Mg(s) + O2(g) → 2MgO(s), and 4Al(s) + 3O2(g) → 2Al2O3(s). Magnesium burns with a bright white light. Aluminium's protective surface oxide can slow visible reaction of bulk metal; the equation describes the oxide-forming change rather than the rate of an untreated object.

For phosphorus(V) oxide, P4(s) + 5O2(g) → P4O10(s). Sulphur burns mainly to sulphur dioxide: S(s) + O2(g) → SO2(g), with a blue flame. Sulphur trioxide is formed by further oxidation, 2SO2(g) + O2(g) ⇌ 2SO3(g), using suitable catalytic operating settings. Do not treat that last equilibrium step as proof that ordinary sulphur combustion gives pure SO3 directly.

With chlorine, 2Na(s) + Cl2(g) → 2NaCl(s) and Mg(s) + Cl2(g) → MgCl2(s). The syllabus represents aluminium chloride as Al2Cl6: 2Al(s) + 3Cl2(g) → Al2Cl6 in the molecular dimer description. State the relevant physical form if a problem requires its state symbol rather than assuming its molecular form is independent of temperature. Silicon gives SiCl4(l) from Si(s) + 2Cl2(g), and phosphorus in excess chlorine gives PCl5: P4(s) + 10Cl2(g) → 4PCl5(s).

Sodium reacts readily with cold water: 2Na(s) + 2H2O(l) → 2NaOH(aq) + H2(g). Magnesium reacts only slowly with cold water, forming Mg(OH)2 and hydrogen, but heated magnesium reacts with steam: Mg(s) + H2O(g) → MgO(s) + H2(g). The water state changes both rate and the stated solid product. These equations connect the observations with atom balance; they are not interchangeable descriptions of one experiment.''',
 'Syllabus §3.1.3 specified products; OpenStax §§18.1–18.4 and 18.8–18.11, representative element reactions. Al2Cl6 representation from syllabus; no bridge-connectivity claim made here.')
add('3-02',[
 'For the specified highest Period 3 oxides, central oxidation numbers rise Na +1, Mg +2, Al +3, Si +4, P +5 and S +6.',
 'For the specified chlorides from sodium to phosphorus, oxidation numbers rise from +1 through +5; these are formal states, not a claim that all compounds contain simple ions.',
 'The increasing maximum positive oxidation number reflects the increasing number of valence electrons available in formal bonding accounting.'
], 'Oxidation numbers follow valence-electron accounting', '''Use oxygen as −2 in these oxides and chlorine as −1 in the specified chlorides. Charge balance then assigns the other element's oxidation number. Na2O gives sodium +1, MgO gives magnesium +2 and Al2O3 gives aluminium +3. In SiO2, silicon is +4; in P4O10, phosphorus is +5. Sulphur is +4 in SO2 but +6 in SO3, so distinguish a particular oxide from the highest oxide in the comparison.

For the specified highest oxides from sodium through sulphur, the maximum positive numbers rise +1, +2, +3, +4, +5 and +6. They do not rise and then fall merely because the elements change from metals to non-metals. The increasing outer-electron count provides the formal valence accounting behind this sequence. It is a maximum-state trend for a named series, not a statement that a particular element has one oxidation number in all compounds.

The chlorides NaCl, MgCl2, Al2Cl6, SiCl4 and PCl5 give +1, +2, +3, +4 and +5 respectively. For Al2Cl6, two aluminium atoms together balance six chlorines at −1, so each aluminium is +3. Do not give one aluminium a +6 value by overlooking the subscript two.

Formal oxidation number does not establish bonding type. Silicon +4 in SiCl4 does not mean there are separate Si4+ and Cl− ions inside a liquid molecule. Nor does phosphorus +5 require P5+ ions. Link the numbers to the written composition, then use physical and chemical evidence for structure. As a check on an incorrect maximum-oxide sequence, calculate phosphorus in P4O10 and sulphur in SO3 explicitly; their +5 and +6 values test whether a proposed falling trend can be correct.''',
 '§4.2 oxidation-number rules; §§18.3–18.4 and 18.8–18.10 specified oxides/chlorides; syllabus §3.1.3 valence-electron trend.')
add('3-03',[
 'Na2O and MgO react with water to give hydroxides, although MgO reacts much less readily; Al2O3 and SiO2 do not react appreciably with water in the ordinary comparison.',
 'P4O10 and SO3 react with water to give acids; aqueous SO2 gives an acidic solution described by the school SO2/H2SO3 representation.'
], 'Oxides in contact with water', '''Sodium oxide reacts with water to give sodium hydroxide: Na2O(s) + H2O(l) → 2NaOH(aq). The solution is alkaline. Magnesium oxide reacts much less readily and forms sparingly soluble magnesium hydroxide: MgO(s) + H2O(l) → Mg(OH)2(s). The modest dissolved hydroxide amount can still give an alkaline mixture. State both the chemical product and the observed extent rather than assuming that both oxides dissolve readily.

Aluminium oxide does not react appreciably with water in this ordinary comparison, and silicon dioxide also remains essentially unchanged. This lack of reaction does not by itself decide acid/base character. Aluminium oxide is amphoteric, while silicon dioxide behaves as an acidic oxide in reaction with strong alkali under suitable heating. A water test and an acid/base reaction test answer different questions.

Phosphorus(V) oxide reacts to form phosphoric(V) acid: P4O10(s) + 6H2O(l) → 4H3PO4(aq). Sulphur trioxide reacts with water to form sulphuric acid: SO3 + H2O(l) → H2SO4(aq), with a large heat release. Sulphur dioxide dissolves to give an acidic solution; the school representation SO2(g) + H2O(l) ⇌ H2SO3(aq) describes that aqueous acid system. Its reverse direction and changing concentrations matter, so it is not a claim that the liquid contains only one isolated molecular species.

Across the selected oxides, strongly basic behaviour gives way through amphoteric aluminium oxide to acidic non-metal oxides. Acidic-oxide character does not imply ready dissolution in water: SiO2 is an acidic oxide that does not simply form an acid solution with water, so reaction evidence must be interpreted separately from solubility. Use equations and named observations together to explain what each oxide does.''',
 '§18.9, representative oxides and hydroxides; §18.4 printed pp.986–988, acidic oxides; §18.10 sulphur oxides; school aqueous SO2 representation within syllabus §3.1.3.')
add('3-04',[
 'Na2O/MgO and their hydroxides show basic behaviour; aluminium oxide and hydroxide are amphoteric; selected non-metal oxides show acidic behaviour.',
 'An amphoteric oxide or hydroxide reacts with acids and with strong alkali, giving different products.',
 'Solubility in water and acid/base reaction type are separate properties.'
], 'Basic, acidic and amphoteric behaviour', '''Basic oxides react with acids to form a salt and water. For example, MgO(s) + 2HCl(aq) → MgCl2(aq) + H2O(l). Magnesium hydroxide behaves similarly: Mg(OH)2(s) + 2HCl(aq) → MgCl2(aq) + 2H2O(l). Sodium hydroxide neutralises an acid through H+(aq) + OH−(aq) → H2O(l). Its high water solubility is a separate property from its ability to accept protons.

Aluminium oxide and aluminium hydroxide are amphoteric: they react with acids and with strong alkali such as sodium hydroxide. In acid, Al2O3(s) + 6H+(aq) → 2Al3+(aq) + 3H2O(l). In aqueous alkali, Al2O3(s) + 2OH−(aq) + 3H2O(l) → 2[Al(OH)4]−(aq). The hydroxide analogues are Al(OH)3(s) + 3H+(aq) → Al3+(aq) + 3H2O(l), and Al(OH)3(s) + OH−(aq) → [Al(OH)4]−(aq).

The hydroxoaluminate notation states the aqueous alkaline product. If a problem specifies a different heated or dehydrated product form, balance the equation for that stated form instead. Do not mix an aqueous complex product and an anhydrous salt representation without accounting for water. Sodium ions can be omitted as spectators in the net ionic version.

An acidic oxide reacts with alkali. For example, SO3 + 2NaOH(aq) → Na2SO4(aq) + H2O(l), and heated SiO2(s) + 2NaOH → Na2SiO3 + H2O. The latter needs suitable strong-alkali heating and is not a claim of rapid reaction with a dilute cold solution. For phosphorus(V) oxide, full neutralisation gives P4O10 + 12NaOH → 4Na3PO4 + 6H2O; the stated amount of base determines the degree of neutralisation. Explain amphoterism by both acid and alkali reactions, rather than merely saying that a substance has an intermediate pH.''',
 '§14.3 oxyacid/basic oxide principles; §18.3–18.4, amphoteric aluminium and nonmetal oxides; §18.9 oxide/hydroxide reactions. Equations derived by atom and charge conservation for stated aqueous products.')
add('3-05',[
 'NaCl dissolves in water without substantial hydrolysis; hydrated magnesium and aluminium cations can make their solutions acidic, with the aluminium effect more pronounced.',
 'SiCl4 hydrolyses with water to give silicon dioxide and HCl; excess-water hydrolysis of PCl5 gives phosphoric(V) acid and HCl.',
 'Dissolution, hydration and hydrolysis must be distinguished when explaining chloride behaviour.'
], 'Chlorides with water: dissolving or reacting', '''Sodium chloride dissolves by separating and hydrating its ions. It does not undergo substantial acid-producing hydrolysis, so a simple aqueous NaCl solution is approximately neutral. Magnesium chloride also supplies hydrated ions and is commonly described as weakly acidic rather than as violently hydrolysing. The magnesium cation's interaction with surrounding water is different from sodium's.

Aluminium chloride gives a distinctly acidic aqueous solution. Although the anhydrous chloride has covalent character and the syllabus uses the Al2Cl6 dimer description, water forms hydrated aluminium ions. A hydrated Al3+ ion strongly polarises O–H bonds in attached water, allowing proton transfer to surrounding water. A useful first-stage representation is [Al(H2O)6]3+(aq) + H2O(l) ⇌ [Al(H2O)5OH]2+(aq) + H3O+(aq). The increased H3O+ concentration explains acidity. Do not assume that simply adding much water precipitates all aluminium as Al(OH)3.

Silicon tetrachloride reacts strongly with water: SiCl4(l) + 2H2O(l) → SiO2(s) + 4HCl(aq). The white solid is often hydrated silica in practice, and hydrogen chloride produces acidic fumes in moist air. The simplified equation accounts for the main composition without representing the real solid as a single dissolved ion.

With excess water, PCl5(s) + 4H2O(l) → H3PO4(aq) + 5HCl(aq). With limited water other intermediate products can be retained, so the excess-water qualification belongs to this equation. The gaseous molecular description of PCl5 must also be distinguished from its ionic solid structure when interpreting physical data. Across these examples, soluble ionic chlorides and hydrolysing covalent chlorides can both produce conducting solutions; the solution products, rather than the original bonding alone, carry charge. Distinguish dissolution from hydrolysis by whether a chemical reaction with water produces new species such as acid.''',
 '§14.4 hydrated aluminium-ion acidity; §18.8 printed pp.1009–1010, phosphorus halides and PCl5 solid; §19.1 printed p.1062 (PDF p.1072), SiCl4 hydrolysis; syllabus §3.1.3 chloride comparison.')
add('3-06',[
 'Across Period 3, increasing electronegativity and decreasing electronegativity differences with oxygen/chlorine help explain the change towards covalent compounds.',
 'The shift from basic through amphoteric to acidic oxide behaviour must be interpreted with bonding and reaction evidence, rather than as a universal water-solubility trend.'
], 'Interpreting the pattern through bonding', '''Sodium and magnesium are electropositive metals. Their large electronegativity differences from oxygen or chlorine favour ionic descriptions for the usual oxides and chlorides. Across Period 3, electronegativity generally increases. The difference from oxygen or chlorine becomes smaller, and shared-electron covalent descriptions become more important. Aluminium sits in a useful intermediate position: its oxide is commonly treated as an ionic lattice with appreciable covalent character, while its anhydrous chloride has a strongly covalent description.

Silicon dioxide is a giant covalent network, whereas SiCl4 is molecular. Both contain silicon formally at +4, so oxidation number alone does not decide whether the compound is molecular, giant or ionic. The partners, geometry and bonding arrangement matter. Phosphorus and sulphur oxides and their reactions with water provide further examples of covalent non-metal chemistry.

The acid/base trend is related but needs its own evidence. Basic Na2O and MgO react with acids; Al2O3 reacts with acid and alkali; selected non-metal oxides react with alkali and often form acidic solutions with water. SiO2 requires particular care because its strong network resists ordinary water reaction despite its acidic-oxide behaviour. A decreasing water-reaction rate is not the same as a decreasing tendency to act as an acid towards alkali.

When interpreting a supplied table, connect a property to the interaction that explains it. A low boiling point can support a molecular structure with weak intermolecular forces. A high melting point may instead indicate an ionic lattice or a covalent network, which further evidence must distinguish. Acidity after adding water describes the products of that interaction, not a direct measurement of the original compound's bond type. Use several linked observations to support the periodic interpretation.''',
 '§7.2 electronegativity/bond polarity; §§18.3–18.4 and 18.9–18.10 representative compounds and acidic/basic trends.')
add('3-07',[
 'High melting point plus conduction when molten but not solid supports an ionic-lattice description.',
 'Low boiling point and lack of conduction in the pure liquid support a simple molecular description, while high melting point and poor conduction can fit a giant covalent network.',
 'A reaction with water can produce mobile ions even when the starting compound is covalent.'
], 'Inferring bonding from a set of observations', '''Bonding inference is an argument from evidence rather than a name attached to one property. A chloride that has a high melting point, does not conduct as a solid and conducts when molten is consistent with an ionic lattice. Fixed ions explain the solid's lack of conduction, and mobile ions explain the melt. The high melting point reflects strong lattice attractions.

A volatile chloride with a low boiling point and poor electrical conduction as a pure liquid is consistent with discrete molecules. Weak intermolecular attractions allow easy separation of the molecules. Its internal covalent bonds need not be weak. If adding water produces an acidic conducting solution, the new solution may contain ions formed by hydrolysis; that does not retrospectively prove the original liquid was ionic.

A high-melting oxide that is a poor ordinary conductor can be a giant covalent network such as SiO2. High melting point alone cannot distinguish it from MgO. Look for molten conduction, reaction behaviour or other stated evidence before choosing a structure. Likewise, a semiconducting element should not be treated as a typical metal merely because a small current can pass.

Consider two invented observations: chloride A melts at a high temperature and conducts only after melting; chloride B is a volatile nonconducting liquid that forms acid with water. Ionic A and molecular B are supported interpretations, but the measurements do not identify their elements uniquely. Use the Period 3 possibilities and any additional composition data to narrow identity. A good answer quotes the discriminating observation, supplies the particle model and states any remaining ambiguity. This is the same structure–property reasoning as Topic 1.3, now used to make a deduction from unfamiliar chloride and oxide evidence.''',
 '§§7.1–7.2 and 10.5, ionic/molecular/network properties; §19.1 SiCl4 hydrolysis. Invented comparison uses source-backed structure–property relations.')

add('4-01',[
 'Main-group members with the same outer-electron pattern often show related ion charges and reaction types.',
 'A prediction from group position should account for down-group radius and shielding changes rather than assume identical reactivity.'
], 'Making a controlled group prediction', '''An element's group provides a useful first prediction because main-group members share a related outer-electron arrangement. Group 2 atoms have two outer electrons and commonly form 2+ ions. Group 17 atoms have seven outer electrons and commonly form 1− halide ions in ionic salts. Group similarity predicts a family of behaviour, not identical numerical properties.

Use a known neighbour as a comparison. For a Group 2 element below magnesium, larger radius and greater shielding make removal of outer electrons easier in the general trend. Stronger reaction with water may therefore be expected when comparing otherwise suitable samples. It is not necessary to invent an exact time or gas-production rate. Surface oxide, temperature and physical form can affect observations, so state the qualitative basis of the prediction.

For a Group 17 element below chlorine, predict larger atoms and halide ions, and lower electronegativity. Its elemental form remains diatomic in the ordinary halogen pattern. Avoid transferring the metal's electron-loss reactivity explanation directly to a halogen's electron-gain chemistry. The shared periodic vocabulary of charge, radius and shielding does not make their chemical roles the same.

When asked to suggest a property of an unfamiliar element, start with the stated group and the relevant comparison. Link the predicted property to an outer-electron or structural reason. Distinguish a direct group feature, such as typical ion charge, from a down-group tendency, such as changing radius. If the group is not given, use composition, ionisation or reaction data first to infer it. An uncertain position should give a conditional prediction rather than a falsely certain identity. The following section combines those clues to identify an unknown.''',
 '§6.4–6.5 periodic arrangement, valence patterns and group trends; §§18.2–18.3 group metal behaviour; syllabus §3.1.4 qualitative predictions.')
add('4-02',[
 'Unknown-element identity can be inferred by combining electron/ion data, period or group information and physical/chemical evidence.',
 'A property shared by several elements cannot alone identify an unknown uniquely; a deduction should state the candidates or remaining ambiguity.'
], 'Combining clues to identify an unknown', '''An unknown element is best identified from several independent clues. Electrical conduction and metallic appearance may indicate a metal but do not distinguish sodium, magnesium and aluminium. A typical ion charge can narrow the group. A known period or occupied-shell count then narrows the position further. Check that the proposed identity accounts for the chemical reactions as well as the physical evidence.

For an original example, an unknown is in Period 3, conducts as a solid, forms a common 2+ ion and gives a basic oxide. These clues together support magnesium. A metal below it in the same group would have more occupied shells and a larger atom, so it would not satisfy the Period 3 clue. A common 3+ ion would instead require a different candidate and acid/base evidence would need checking.

Successive ionisation data can provide another route. A large jump after the second electron has been removed suggests two relatively accessible outer electrons before reaching a more tightly held inner shell. Combined with a Period 3 location and metallic behaviour, that again supports Group 2 magnesium. The jump is evidence about electronic arrangement, not an instruction to use the largest raw number as a group label.

For a nonconducting Period 3 substance with a very high melting point, a giant covalent description suggests silicon rather than the simple molecular elements. If its chloride is a volatile liquid that hydrolyses, that strengthens the identification. Each extra clue should discriminate between candidates. Where the evidence leaves two plausible choices, name the uncertainty and state what further observation would decide. This is a chemical deduction: properties and electron arrangement must agree, rather than a guess from one familiar reaction.''',
 '§6.5 successive ionisation/electronic patterns; §§7.1–7.2 and 10.5 structure–property evidence; original multi-clue examples.')

s=t.wo['item_slots']
qa=[
 ('Describe first ionisation energy, including amount basis, starting particles and final particles. [3]','Energy needed to remove one electron from each atom in one mole [1] of gaseous atoms [1], forming one mole of gaseous 1+ ions [1].'),
 ('Explain why the first ionisation equation X(g) → X+(g) + e− has a positive energy requirement. [2]','The electron is attracted to the positive nucleus [1]; energy must be supplied to overcome that attraction and separate it [1].'),
 ('Describe three factors relevant to the attraction holding an outer electron before first ionisation. [3]','Nuclear charge [1], distance of the electron from the nucleus [1], and shielding by inner electrons [1].'),
 ('Explain why increased nuclear charge alone does not prove a greater first ionisation energy when comparing atoms down a group. [2]','Additional shells increase distance and inner-electron shielding [1]; these can reduce effective attraction despite the extra protons [1].'),
 ('Describe the general Period 3 trends in atomic radius, the isoelectronic Na+/Mg2+/Al3+ radii, and electronegativity from sodium to chlorine. [3]','Atomic radius generally decreases [1]; Na+ > Mg2+ > Al3+ in radius [1]; electronegativity generally increases from sodium to chlorine [1].'),
 ('Explain why Al3+ is smaller than Na+, given that both ions have ten electrons. [2]','Al3+ has greater nuclear charge [1]; its nucleus attracts the same number of electrons more strongly, contracting the ion [1].'),
 ('Describe the general first-ionisation-energy trend across Period 3 and its main nuclear explanation. [3]','It generally increases [1]; nuclear charge rises [1], while comparable inner shielding and falling radius strengthen attraction to the removed electron [1].'),
 ('Explain why the outer electron of a Period 3 atom near the right-hand end is generally harder to remove than sodium’s outer electron. [2]','Nuclear charge is larger without a new main shell of inner shielding [1]; the effective attraction is greater and radius smaller, requiring more removal energy [1].'),
 ('Describe the structures and ordinary conduction of aluminium, silicon and molecular sulphur. [3]','Aluminium is metallic and conducts through delocalised electrons [1]; silicon is giant covalent and semiconducting [1]; sulphur contains S8 molecules and is a poor conductor [1].'),
 ('Explain why silicon has a much higher melting point than molecular chlorine. [2]','Silicon melting disrupts an extended strong covalent network [1]; chlorine melting overcomes much weaker intermolecular attractions between Cl2 molecules [1].'),
 ('Describe how comparable atomic/ionic radii and electronegativity generally change down Groups 2 and 17. [3]','Atomic radii increase [1]; comparable ionic radii increase [1]; electronegativity generally decreases [1].'),
 ('Explain why the chloride ion is larger than the fluoride ion. [2]','Cl− has an additional occupied shell [1]; the outer electrons are farther from the nucleus and more shielded, so the ion is larger [1].'),
 ('Describe the general first-ionisation trend down Groups 2 and 17 and the two shell-related causes. [3]','First ionisation energy generally decreases [1]; outer electrons are farther from the nucleus [1] and more shielded by inner electrons [1].'),
 ('Explain why a lower Group 2 atom generally loses its first electron more easily despite having more protons. [2]','Extra shells increase distance and shielding [1]; the resulting weaker effective attraction outweighs the increased nuclear charge in this group comparison [1].'),
 ('Describe the products of magnesium reacting with oxygen, cold water and steam. [3]','Oxygen gives MgO [1]; cold water reacts slowly to form Mg(OH)2 and H2 [1]; steam gives MgO and H2 [1].'),
 ('Write the balanced equation for phosphorus P4 forming phosphorus(V) oxide in excess oxygen. Include state symbols. [2]','P4(s) + 5O2(g) → P4O10(s). Correct product/states [1]; balance [1].'),
 ('Write the balanced equation for sodium with cold liquid water. Include state symbols. [2]','2Na(s) + 2H2O(l) → 2NaOH(aq) + H2(g). Correct products/states [1]; balance [1].'),
 ('Explain why a magnesium–water equation should state whether water is cold liquid or steam. [2]','Cold water reacts slowly and gives magnesium hydroxide [1]; steam reacts more readily with heated magnesium and gives magnesium oxide, so the stated medium affects both rate and product [1].'),
 ('Describe the maximum oxidation numbers in the specified highest oxides from sodium through sulphur, their direction of change and the valence-electron connection. [3]','They are +1, +2, +3, +4, +5 and +6 [1], increasing across the stated series [1] as formal maximum participation follows increasing valence-electron count [1].'),
 ('Explain why Al2Cl6 assigns aluminium +3 rather than +6. [2]','Six chlorines contribute −6 overall [1]; two aluminium atoms share the balancing +6 total, giving each +3 [1].'),
 ('Explain the error in a claimed maximum-oxide oxidation-number trend that rises to aluminium and then falls towards sulphur. Use P4O10 and SO3 as a discriminating test. [2]','It incorrectly predicts falling values for the non-metals [1]; charge balance gives phosphorus +5 and sulphur +6, continuing the increase in the specified highest oxides [1].'),
 ('Describe the water reaction of Na2O, Al2O3 and P4O10 in the ordinary comparison. [3]','Na2O forms alkaline sodium hydroxide [1]; Al2O3 does not react appreciably [1]; P4O10 forms phosphoric(V) acid [1].'),
 ('Write the balanced equation for P4O10 reacting with water to form phosphoric(V) acid. Include state symbols. [2]','P4O10(s) + 6H2O(l) → 4H3PO4(aq). Correct species/states [1]; balance [1].'),
 ('Explain why lack of reaction between SiO2 and ordinary water does not show that SiO2 is a basic oxide. [2]','Acid/base classification is not determined by water solubility alone [1]; SiO2 reacts with strong alkali under suitable heating, supporting acidic-oxide behaviour [1].'),
 ('Describe basic, acidic and amphoteric oxide behaviour in reactions with acids and sodium hydroxide. [3]','A basic oxide reacts with acid [1]; an acidic oxide reacts with sodium hydroxide under suitable settings [1]; an amphoteric oxide can react with both [1].'),
 ('Explain why aluminium oxide is described as amphoteric. [2]','It reacts with acid to give aqueous aluminium-containing salt species and water [1], and with sodium hydroxide to give an aluminate product under suitable settings [1].'),
 ('Describe the differences when NaCl, AlCl3 and SiCl4 are added to excess water. [3]','NaCl dissolves to an approximately neutral solution [1]; hydrated aluminium ions produce an acidic solution by hydrolysis [1]; SiCl4 hydrolyses to silica and HCl [1].'),
 ('Write the simplified balanced hydrolysis equation for SiCl4 in excess water, giving SiO2 and HCl. Include state symbols. [2]','SiCl4(l) + 2H2O(l) → SiO2(s) + 4HCl(aq). Correct products/states [1]; atom balance [1].'),
 ('Explain why an acidic conducting solution after SiCl4 hydrolysis does not prove the original pure liquid was ionic. [2]','SiCl4 reacts with water to form new substances including acid [1]; ions in those products carry solution current, so that observation is not direct evidence of original liquid ions [1].'),
 ('State the general change in bonding descriptions of the selected oxides and chlorides as Period 3 electronegativity rises. [1]','Descriptions change from predominantly ionic towards more covalent character [1], with structure- and state-specific qualifications.'),
 ('Determine which structure better fits an oxide that is very high-melting and does not conduct as a solid or ordinary liquid: a simple molecular solid or a giant covalent network. [1]','A giant covalent network [1]; high melting point and lack of mobile charge fit that description better.'),
 ('State the conduction observation that supports mobile ions appearing on melting a compound. [1]','It does not conduct as a solid but conducts when molten [1].'),
 ('Explain why high melting point alone cannot distinguish an ionic oxide from a giant covalent oxide. [2]','Both contain strong interactions throughout extended structures [1]; additional evidence such as molten conduction is needed to identify mobile ions rather than a covalent network [1].'),
 ('State the common ion charge predicted for a typical Group 2 metal. [1]','2+ [1].'),
 ('Suggest the atomic-radius change for a Group 17 element below chlorine compared with chlorine. [1]','A larger radius [1], because additional shells increase distance and shielding.'),
 ('State why several independent properties are preferable to one broad observation when identifying an unknown Period 3 element. [1]','A broad property can fit several candidates, while additional independent clues discriminate between them [1].'),
 ('Determine the Period 3 element that conducts as a metal, forms a common 2+ ion and gives a basic oxide. [1]','Magnesium [1].')
]
assert len(qa)==len(s)
for slot,(prompt,answer) in zip(s,qa):
 st='WHY' if slot['subtype']=='MECH' else None
 t.item(slot,prompt,answer,subtype=st)
 if st:t.deviations.append({'from':slot['slot']+' MECH','to':'WHY; preserve original AO/Bloom/command/tariff','why':'Nuclear attraction, periodic property and acid/base explanations do not require an invented electron-movement intermediate/product reaction mechanism.'})
p=t.wo['performance_tasks']
t.item(p[0],'''Identify one correct option per question. [9]
1. First ionisation begins with: A gaseous neutral atoms; B solid 1+ ions; C aqueous atoms; D gaseous 2+ ions.
2. Its common molar unit is: A mol; B kJ mol⁻¹; C g cm⁻³; D cm³ s⁻¹.
3. Greater shielding of an otherwise comparable outer electron tends to make removal: A harder; B independent of attraction; C easier; D a mass change.
4. Na+, Mg2+ and Al3+ each have ten electrons. The smallest is: A Na+; B all equal; C Mg2+; D Al3+.
5. From sodium to chlorine, electronegativity generally: A increases; B decreases; C stays fixed; D equals atomic number.
6. A metallic Period 3 unknown forms a common 2+ ion and a basic oxide. It is: A Al; B Mg; C Si; D Cl.
7. A non-metallic Period 3 unknown has a giant covalent network and very high melting point. It is: A P; B S; C Si; D Ar.
8. Two comparable ions of one group have the same charge but the lower member has an extra shell. Its radius is generally: A zero; B smaller; C unchanged; D larger.
9. A jump after the second successive ionisation can support: A two accessible outer electrons before an inner shell; B two neutrons; C an atomic mass of two; D a 2− ion in every compound.''',
 '''Key: 1 A, 2 B, 3 C, 4 D, 5 A, 6 B, 7 C, 8 D, 9 A. One mark per correct option.
1. A is the definition. B uses the wrong state and charge; C changes to an aqueous starting point; D describes later ionisation.
2. B is energy per mole. A is amount; C is density; D is volume-production rate.
3. C follows reduced effective attraction. A reverses the effect; B ignores the mechanism; D confuses energy removal with nuclear mass.
4. D has the strongest nuclear pull for the common electron population. A reverses the trend; B ignores nuclear charge; C chooses an intermediate member.
5. A is the general trend. B gives the down-group direction; C ignores changing attraction; D confuses different quantities.
6. B matches all clues. A commonly forms 3+; C is network covalent; D is a non-metal.
7. C fits the network clue. A and B are molecular forms in this comparison; D is monatomic with low melting point.
8. D follows greater shell extent. A is physically impossible; B uses the across-period trend; C ignores the new shell.
9. A links the jump to electronic structure. B concerns the nucleus; C concerns mass; D confuses electron-removal evidence with a universal anion prediction.''')
t.item(p[1],'''Explain the periodic deductions from these original clues. Unknown X is in Period 3, conducts well as a solid, forms a common 2+ ion and gives a basic oxide. Y lies directly below X in the same group. [8]
(a) Identify X and its group. [2]
(b) Give the composition and acid/base type of X’s oxide. [2]
(c) Suggest the common ion charge and relative atomic radius of Y. [2]
(d) Explain the general difference in ease of first electron removal between Y and X. [2]''',
 '''Part (a): magnesium [1], Group 2 [1].
Part (b): MgO [1], a basic oxide [1].
Part (c): Y commonly forms 2+ [1] and has a larger atom [1].
Part (d): Y has an additional shell giving greater distance and shielding [1]; its outer electron is less strongly attracted and is generally easier to remove despite increased nuclear charge [1]. Each bracket is a separate creditworthy point.''')
t.item(p[2],'''Calculate the energy needed for first ionisation and interpret the related periodic evidence. A Period 3 metallic unknown X forms a common 2+ ion and has a supplied first ionisation energy of 738 kJ mol⁻¹. [5]
(a) Identify X from its period and common ion charge. [1]
(b) Calculate the energy to remove one electron from each atom of 0.0200 mol gaseous X atoms. Give three significant figures. [2]
(c) State which is smaller, Na+ or X2+, given that both contain ten electrons, and explain using nuclear attraction. [2]''',
 '''(a) Magnesium [1].
(b) Equation: energy = n × first ionisation energy; substitution 0.0200 × 738 = 14.76 kJ [1]. Answer 14.8 kJ to three significant figures [1]. No conversion is needed because n is mol and the datum is kJ mol⁻¹. The starting atoms are already gaseous.
(c) Mg2+ is smaller [1]; its greater nuclear charge attracts the same electron population more strongly [1].''')
t.deviations.append({'from':'Simple across-period chloride trend','to':'Qualify physical form for Al2Cl6 and PCl5, and distinguish aluminium hydration/hydrolysis from complete precipitation','why':'Bonding descriptions depend on physical state, while acidic aqueous aluminium chloride is not adequately represented as fully precipitated Al(OH)3.'})
t.save()
