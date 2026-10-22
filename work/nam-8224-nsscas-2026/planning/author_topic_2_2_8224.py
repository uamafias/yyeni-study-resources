"""Original redox and electrolysis teaching, following the frozen 8224 plan."""
from authoring_common_8224 import Topic
t=Topic('2.2')
def add(short,claims,title,text,loc,source='OpenStax-Chemistry'):
    t.objective(short,claims,[(title,text)],source,loc)

add('1-01',[
 'Oxidation number is the charge assigned to an atom by agreed electron-accounting rules, not necessarily an actual ionic charge.',
 'The sum of oxidation numbers, counting the atoms present, equals zero for a neutral compound or the total charge for an ion.',
 'An uncombined element has oxidation number zero; a monatomic ion has oxidation number equal to its ionic charge.'
], 'Calculating an oxidation number', '''Oxidation number is the charge assigned to an atom by the agreed electron-accounting rules. It is not necessarily an actual ionic charge. In a covalent molecule it is an accounting device that helps track oxidation and reduction. Write an oxidation number with its sign before the number, such as +3; distinguish it from the overall charge on an ion, written as 3+.

An atom in an uncombined element has oxidation number zero: this applies to Cu(s), O2 and Cl2. A monatomic ion has the oxidation number of its charge, so Mg2+ is +2 and Cl− is −1. Group 1 metals in compounds are +1 and Group 2 metals are +2. Oxygen is usually −2 and hydrogen is usually +1 in the compounds used here. Remember the exceptions when relevant: oxygen is −1 in a peroxide and hydrogen is −1 in a metal hydride. Fluorine in compounds is −1; other halogens need not be −1 when bonded to oxygen.

For a neutral species, the sum is zero. For a polyatomic ion, the sum equals the ion charge. In SO4²−, let sulphur have oxidation number x. Four oxygen atoms contribute −8, so x − 8 = −2 and x = +6. The sulphur is not an S6+ ion inside the sulphate ion. In neutral H2SO4 the hydrogen contribution is +2, giving the same sulphur oxidation number.

Count subscripts before solving. In Cr2O7²− the equation is 2x − 14 = −2, giving x = +6 for each chromium atom. Do not assign +12 to one chromium: that is the combined contribution of both. These integer assignments are exact bookkeeping results, without a physical unit or a significant-figure rounding step. An oxidation-state result should therefore include its sign explicitly, even when the element’s name is also given. Topic 1.1 supplies the atom and charge counting used in this method.''',
 '§4.2, printed pp.187–189 (PDF pp.197–199), oxidation-number rules and worked assignments.')
add('1-02',[
 'Oxidation is loss of electrons and an increase in oxidation number; reduction is gain of electrons and a decrease in oxidation number.',
 'An oxidising agent causes oxidation and is itself reduced; a reducing agent causes reduction and is itself oxidised.',
 'The total electron loss and gain balance in an overall redox reaction.'
], 'Connecting electron transfer and redox roles', '''Oxidation is loss of electrons; reduction is gain of electrons. In oxidation-number terms, oxidation is an increase and reduction is a decrease. These are complementary processes: electrons released by one species are taken up by another. In an overall balanced equation electrons cancel, although separate half-equations can show where they are lost and gained.

Consider Zn(s) + Cu2+(aq) → Zn2+(aq) + Cu(s). Zinc changes from 0 to +2 and loses two electrons, so it is oxidised. Copper changes from +2 to 0 and gains two electrons, so copper(II) ions are reduced. Zinc is the reducing agent because it supplies the electrons that reduce copper(II). Copper(II) ions are the oxidising agent because they accept those electrons and cause zinc's oxidation. The agent's name describes what it does to another species, not the process it undergoes itself.

The half-equations are Zn(s) → Zn2+(aq) + 2e− and Cu2+(aq) + 2e− → Cu(s). Adding them removes the two electrons from both sides. This accounting does not require an invented intermediate between Zn and Zn2+. In covalent reactions, changes in oxidation number describe formal electron redistribution even when complete ionic transfer is not an adequate picture of the bonds.

To identify redox, calculate oxidation numbers before and after, then name the atom that increases and the atom that decreases. A change of physical state alone is not evidence of redox. Nor does the presence of oxygen in an equation prove that oxidation numbers change. Neutralising H+(aq) with OH−(aq) to make water leaves hydrogen at +1 and oxygen at −2. Use changes in the numbers as the test, with electron transfer as the underlying accounting principle.''',
 '§4.2, printed pp.187–191, electron transfer, formal oxidation states and oxidising/reducing agents.')
add('1-03',[
 'Oxidation-number changes determine the relative amounts of oxidised and reduced species needed to balance electron transfer.',
 'An acidic aqueous redox equation can be completed using H2O for oxygen, H+ for hydrogen and electrons for charge, followed by cancellation.'
], 'Balancing a redox equation', '''Begin by identifying the atoms whose oxidation numbers change. Work out the electron loss or gain per atom, then allow for the number of those atoms in each species. Equalise the total increase and total decrease. This supplies a starting ratio for the reacting redox species. It does not automatically finish hydrogen, oxygen or charge balance.

For acidified manganate(VII) reacting with iron(II), manganese changes from +7 in MnO4− to +2 in Mn2+, a gain of five electrons per manganese. Iron changes from +2 to +3, a loss of one electron per iron. Therefore five Fe2+ ions are required for each MnO4− ion. The half-equations are MnO4−(aq) + 8H+(aq) + 5e− → Mn2+(aq) + 4H2O(l) and Fe2+(aq) → Fe3+(aq) + e−. Multiply the iron half-equation by five before adding.

The overall equation is MnO4−(aq) + 8H+(aq) + 5Fe2+(aq) → Mn2+(aq) + 4H2O(l) + 5Fe3+(aq). There is one manganese and five iron atoms on each side. Four oxygens and eight hydrogens also balance. Total charge is +17 on both sides. Include the acidic medium: a different medium can give a different manganese product, so the +2 endpoint cannot be assumed independently of the stated reaction.

Changing a coefficient multiplies a whole species; changing a subscript changes the substance. Add only species appropriate to the stated medium when completing the balance. An ionic equation omits spectator ions, such as potassium in this example, because they undergo no net change. The final checks are separate: atom balance, charge balance, and the absence of uncancelled electrons in the overall equation. This method links the ratio to oxidation-number changes rather than relying on trial and error.''',
 '§4.2, printed pp.191–193, half-reaction balancing; manganate(VII)/iron example derived from oxidation-number rules and acidic products specified in syllabus §2.2.1.')
add('1-04',[
 'An oxidising agent can oxidise iodide in aqueous potassium iodide to iodine, producing a brown solution.',
 'A reducing agent can reduce purple acidified manganate(VII) to manganese(II), decolourising the reagent when the sample and reagent permit this reaction.',
 'A reagent colour change is an observation; identifying the sample as oxidising or reducing is a deduction from the electron-transfer process.'
], 'Recognising oxidising and reducing behaviour', '''Aqueous potassium iodide can test for oxidising behaviour. It supplies iodide ions, I−, which can lose electrons to an oxidising agent. The half-equation is 2I−(aq) → I2(aq) + 2e−. A colourless iodide solution develops a brown colour when iodine is produced in the aqueous mixture. Iodide is oxidised from −1 to 0, so the added sample acts as an oxidising agent. Potassium ions are spectators in this interpretation.

For reducing behaviour, use potassium manganate(VII) acidified with dilute sulphuric acid. The reagent begins purple. A suitable reducing agent changes MnO4− into Mn2+, so the purple colour disappears when the reagent is used in an amount that can be reduced by the sample. A dilute manganese(II) solution is very pale pink and commonly appears colourless. The change from manganese +7 to +2 is reduction, so the tested substance supplies electrons and is oxidised.

Record the observed colour change before giving its meaning. “Purple to colourless” describes evidence; “the sample is reducing” is the deduction. If purple reagent remains after addition, it may be present in excess. A negative observation by itself is not proof that a substance could not participate in any redox reaction: concentration, medium and reaction speed can matter. Compare appropriate fresh samples and use the stated acidic medium for the manganate(VII) interpretation.

For example, iron(II) can decolourise acidified manganate(VII) as Fe2+ becomes Fe3+. An oxidising sample that liberates iodine from iodide does the opposite electron-transfer job. Keep the two reagents and directions distinct. Brown iodine is not the colour of iodide ions, and the disappearance of purple manganate(VII) is not evidence that manganese atoms have left the solution. These tests connect to the supplied observations and deductions practised in Topic 5.1.''',
 'Syllabus §2.2.1, required redox tests; OpenStax §4.2 redox principles and §18.11 printed p.1028, brown aqueous iodine (PDF p.1038).',source='NSSCAS-8224-SYLLABUS')
add('1-05',[
 'The syllabus names NO2− nitrate(III), NO3− nitrate(V), ClO− chlorate(I) and ClO3− chlorate(V).',
 'The Roman numeral in these oxyanion names gives the central atom’s oxidation number, not the ion’s overall charge.'
], 'Naming the specified oxyanions', '''An oxyanion contains oxygen combined with another element and has a negative overall charge. In the naming convention required here, the Roman numeral states the oxidation number of the central element. It does not count oxygens and does not give the total charge on the ion. Calculate the number rather than choosing a familiar name by appearance.

For NO2−, oxygen contributes 2 × (−2) = −4. With nitrogen x, x − 4 = −1 gives x = +3. The syllabus name is nitrate(III). For NO3−, x − 6 = −1 gives +5, so the name is nitrate(V). Both ions have charge −1 even though nitrogen has different oxidation numbers. The names nitrite and nitrate are also common in reference books, but use the requested Roman-numeral convention in this syllabus practice.

For ClO−, x − 2 = −1 gives chlorine +1 and chlorate(I). For ClO3−, x − 6 = −1 gives +5 and chlorate(V). The names distinguish chemically different ions, so omitting or guessing the numeral can change the meaning of an answer. A Roman numeral V represents +5 here; it is not a 5− charge on the entire oxyanion.

A useful discriminating check is to work backwards from a proposed name. If a learner calls NO2− nitrate(V), combine nitrogen +5 with two oxygens at −2: the resulting total is +1, not the given −1. The proposed name therefore fails the charge sum. This check exposes the naming mistake directly without relying on recall of a second label. Use the same calculation for a new ion, and keep the numerical oxidation state and the chemical identity together.''',
 'Syllabus §2.2.1, four specified oxyanion names; OpenStax §4.2 printed p.188, charge-sum rule.',source='NSSCAS-8224-SYLLABUS')

add('2-01',[
 'Electrolysis uses electrical energy to drive chemical decomposition in an electrolyte with mobile ions.',
 'An ionic solid has ions fixed in a lattice; melting or dissolving can provide mobile ions that carry charge.',
 'In an electrolytic cell the negative cathode receives electrons for reduction and the positive anode removes electrons during oxidation.'
], 'What electrolysis requires', '''Electrolysis is chemical decomposition caused by passing an electric current through an electrolyte. A molten ionic compound or an aqueous solution containing mobile ions can act as the electrolyte. An external direct-current supply provides the energy that drives the electrode reactions. Electricity passing through a metal wire alone is conduction, but does not meet this description of decomposition in an electrolyte.

In a solid ionic lattice the ions are held in fixed positions and cannot carry a sustained current through the sample by migration. Melting releases their ability to move; dissolving a suitable ionic substance provides mobile solvated ions. The positive ions are cations and the negative ions are anions. These two populations can carry charge in opposite directions through the liquid.

The cathode of an electrolytic cell is connected to the negative terminal of the supply. Cations move towards it and a species gains electrons there: reduction. The anode is connected to the positive terminal. Anions move towards it and a species loses electrons there: oxidation. The electrode names identify reaction roles; the stated signs here refer to a driven electrolytic cell. Do not transfer the polarity statement to a different kind of cell without considering its energy source.

Molten sodium chloride illustrates the distinction from an aqueous solution. The molten electrolyte contains sodium and chloride ions, so sodium forms at the cathode and chlorine at the anode. In an aqueous sodium chloride solution, water can participate and hydrogen forms instead of sodium under the usual school prediction. “Molten” and “aqueous” therefore change the available reacting species, rather than merely describing the vessel temperature. Before assigning products, identify the electrolyte's state, its ions and the electrode material.''',
 '§17.7, printed pp.947–950 (PDF pp.957–960), driven cells, molten salt and aqueous competition.')
add('2-02',[
 'Aqueous selective-discharge predictions depend on relative discharge tendencies, concentration and electrode material.',
 'In the school reactivity-series approximation, Ag+ and Cu2+ deposit their metals ahead of hydrogen, while hydrogen forms ahead of iron, zinc and sodium from ordinary aqueous electrolytes.',
 'At inert anodes oxygen is expected from dilute hydroxide-containing solutions, while concentrated chloride solution favours chlorine; the boundary depends on the cell.'
], 'Choosing among competing species', '''An aqueous electrolyte contains species from the solute and from water. Selective discharge means that one possible electrode reaction occurs preferentially. To predict products, consider the competing species at the particular electrode, their relative tendencies to gain or lose electrons, concentration and whether the electrode reacts. The following classroom predictions assume suitable inert electrodes and ordinary aqueous electrolysis, rather than an industrial cell engineered to favour a particular product.

For the specified cathode sequence, silver and copper are less reactive than hydrogen; iron, zinc and sodium are more reactive. Thus Ag+ or Cu2+ can give the corresponding metal, while aqueous iron, zinc or sodium salts are commonly predicted to give hydrogen in competition with the metal ions. This simplified prediction guide has limits when applied to engineered metal-deposition processes. Specially chosen concentrations and electrode operating settings can change which process is effective. An aqueous sodium salt does not produce bulk sodium metal in the school model: water is reduced instead.

At an inert anode, dilute hydroxide-containing aqueous solutions produce oxygen. For a very dilute chloride solution, oxygen is the expected classroom product, whereas a concentrated chloride solution favours chlorine. Write “concentrated” when assigning chlorine from brine and “very dilute” when assigning oxygen in this comparison. The transition is not a universal numerical concentration threshold, and mixtures can arise near a boundary. The detailed cell setting matters.

For concentrated aqueous sodium chloride with inert electrodes, predict hydrogen at the cathode and chlorine at the anode. For dilute aqueous copper sulphate with inert electrodes, predict copper at the cathode and oxygen at the anode. If the anode is copper, it can dissolve instead, so the inert-anode prediction must not be applied unchanged. State the assumed electrode material alongside the products. These examples connect ion chemistry to the redox half-equations rather than treating discharge as an unexplained list.''',
 '§17.7 printed pp.949–951, competing aqueous reactions and electrode effects; §17.3 reduction data; syllabus §2.2.2 specified qualitative discharge sequence. School reactivity approximation explicitly distinguished from industrial behaviour.')
add('2-03',[
 'Metal recovery from a leach solution can involve dissolving metal-bearing material, preparing the solution and reducing metal ions at a cathode.',
 'Copper recovery uses Cu2+(aq) + 2e− → Cu(s); the formal manganese-metal cathode step is Mn2+(aq) + 2e− → Mn(s).',
 'The syllabus’s industrial manganese example requires controlled deposition rather than an unqualified application of the simple hydrogen-discharge rule.'
], 'Metal recovery after leaching', '''Leaching transfers a metal from a metal-bearing solid into a solution. An acidic leach can contain dissolved metal ions together with unwanted dissolved substances and insoluble residue. Separate the residue and prepare the electrolyte before attempting to collect metal. Electrolysis then uses an external supply to transfer electrons to the metal ions at the cathode, forming metal on a suitable collecting surface.

For copper, the cathode half-equation is Cu2+(aq) + 2e− → Cu(s). The mass of the copper deposit grows while the solution supplies copper ions. With an appropriate inert anode in an acidic sulphate-based cell, oxidation of water can provide oxygen and H+ at the anode. The metal is recovered by reduction of ions already dissolved in the leach solution. This differs from refining a metal with a soluble metal anode that replenishes the same ions.

Manganese is also specified as an example of recovery from a leached solution. The formal deposition step for manganese metal is Mn2+(aq) + 2e− → Mn(s). This is an industrial application requiring a controlled electrolyte and electrode operation, rather than a prediction that an arbitrary acidic Mn2+ solution will deposit manganese efficiently. Hydrogen evolution competes at the cathode. The elementary aqueous reactivity guide cannot by itself describe a process engineered to favour metal recovery.

At this level, distinguish the stages and their roles: leaching dissolves suitable metal-bearing material, solution preparation removes material that would interfere, and electrolysis supplies electrons for deposition. Do not claim that current converts every dissolved ion into the desired metal, or that the same operating recipe works for copper and manganese. No plant-specific electrolyte recipe is required here. Use the named ions and their balanced cathode equations to explain the outline, with process control recognised as part of the industrial application.''',
 'Syllabus §2.2.2, acidic-leach copper and manganese examples; OpenStax §17.7 pp.947–951, applied electrolytic reduction. Industrial outline limited to syllabus and charge-balanced derivation; manganese process-specific source verification remains a review focus.',source='NSSCAS-8224-SYLLABUS')
add('2-04',[
 'A cathode reduction half-equation has electrons on the reactant side; an anode oxidation half-equation has electrons on the product side.',
 'Half-equations conserve atoms and total charge and include state symbols appropriate to molten or aqueous electrolysis.',
 'Hydrogen and oxygen electrode equations can be written using H+, OH− and H2O as appropriate to the stated aqueous medium.'
], 'Writing electrode half-equations', '''An electrode half-equation identifies the reacting species, product and electron transfer. Balance atoms first and then charge. At the cathode, electrons appear on the left because the reacting species gains them. Cu2+(aq) + 2e− → Cu(s) has zero net charge on both sides. For silver it is Ag+(aq) + e− → Ag(s); the coefficient of electrons follows the ion charge rather than being copied from another metal.

In an acidic electrolyte, hydrogen formation is 2H+(aq) + 2e− → H2(g). In a neutral or alkaline aqueous electrolyte, use 2H2O(l) + 2e− → H2(g) + 2OH−(aq). Both are reduction equations producing hydrogen, but their written reactants fit different media. The neutral-water equation explains why hydrogen can form from an aqueous sodium salt without reducing Na+.

For concentrated aqueous chloride at an inert anode, 2Cl−(aq) → Cl2(g) + 2e−. Two chloride ions are needed because chlorine is diatomic. For oxygen from hydroxide-containing solution, 4OH−(aq) → O2(g) + 2H2O(l) + 4e−. In acid, the equivalent water oxidation is 2H2O(l) → O2(g) + 4H+(aq) + 4e−. Check that the atoms and total charges balance in the chosen version.

When combining half-equations, multiply them so the electron coefficients match, then cancel electrons. For water electrolysis, two hydrogen-producing steps match one oxygen-producing step, giving 2H2O(l) → 2H2(g) + O2(g). The gas amount ratio is two to one, provided the products are collected under comparable settings without losses. The coefficients describe stoichiometry; they do not claim that ions of the same sign physically travel together as fixed groups. Preserve aqueous and molten state symbols because changing the medium changes the chemical competition.''',
 '§17.7 printed pp.947–950, electrode reactions; §4.2 printed pp.191–193, atom and charge balancing.')
add('2-05',[
 'Electrons carry charge through the metallic wires; mobile cations and anions carry charge through the electrolyte.',
 'The supply delivers electrons to the cathode and removes electrons from the anode during electrolysis.',
 'Ion migration in the electrolyte and electron transfer at electrode interfaces complete the circuit without free electrons travelling through the bulk solution.'
], 'Following charge around the complete circuit', '''A working electrolytic circuit contains more than one charge carrier. In its metal wires, electrons move through the conductor. In the electrolyte, cations and anions move through the liquid. A description that sends free electrons across the solution from one electrode to the other confuses these two parts of the circuit.

The negative supply terminal delivers electrons through a wire to the cathode. There, a reacting species takes electrons from the electrode and is reduced. At a copper-depositing cathode, dissolved Cu2+ accepts two electrons and becomes neutral copper metal. Cations migrate towards the cathode, but movement towards the surface and discharge at the surface are distinct events. A competing ion may remain in solution even though it contributes to carrying charge.

At the positive anode, a reacting species loses electrons. The external supply removes these electrons through the anode wire. Chloride oxidation in concentrated brine, for example, transfers electrons to the electrode while chlorine forms. Anions migrate towards the anode. The supply maintains the driving potential between the electrodes; it does not create the atoms in the products or supply a stock of metal ions.

Both signs of ion contribute to ionic conduction. Do not say that all current inside the electrolyte is due to the cations that eventually form a deposit. Spectator ions can move and carry charge without appearing in the net electrode equations. Sustained electrolysis requires a complete conducting path, mobile ions and charge-transfer reactions at both interfaces. If an ionic electrolyte solidifies and its ions become fixed, the liquid ionic path is lost even though the external wires still contain mobile electrons. This explanation extends Topic 1.3's distinction between metallic and ionic conduction to a circuit where chemical changes occur.''',
 '§17.7 printed pp.947–951 and §17.2 electrochemical circuits; charge-carrier account applied to the stated electrolytic examples.')

s=t.wo['item_slots']
qa=[
 ('State the sum of oxidation numbers for the atoms in a polyatomic ion. [1]','It equals the overall charge on that ion [1].'),
 ('Calculate the oxidation number of chromium in Cr2O7²−, taking oxygen as −2. Show the charge sum. [3]','Charge-sum equation: 2x + 7(−2) = −2 [1]. Thus 2x = +12 [1] and each chromium is +6 [1]. The result is exact and dimensionless; conversion and significant-figure rounding are inapplicable.'),
 ('Determine whether nitrogen is oxidised or reduced when its oxidation number changes from +3 to +5. [1]','Oxidised [1], because its oxidation number increases.'),
 ('Describe zinc and copper(II) ions in Zn(s) + Cu2+(aq) → Zn2+(aq) + Cu(s), giving electron transfer and the oxidising agent. [3]','Zinc loses two electrons and is oxidised [1]; Cu2+ gains two electrons and is reduced [1]; Cu2+ is the oxidising agent [1].'),
 ('Explain why Fe2+ is a reducing agent when it becomes Fe3+. [2]','Fe2+ loses an electron and is oxidised [1]; because another species accepts that electron and is reduced, Fe2+ acts as the reducing agent [1].'),
 ('State the electron-balance requirement used when balancing a redox equation. [1]','Total electrons lost equal total electrons gained [1].'),
 ('Write the balanced ionic equation for MnO4− reacting with Fe2+ in acidic aqueous solution to form Mn2+ and Fe3+. Include state symbols. [2]','MnO4−(aq) + 8H+(aq) + 5Fe2+(aq) → Mn2+(aq) + 4H2O(l) + 5Fe3+(aq). Correct species and acidic H+/water balance [1]; electron ratio and overall charge/atom balance [1].'),
 ('State the colour change when an oxidising sample liberates iodine from colourless aqueous potassium iodide. [1]','Colourless to brown [1], as iodine forms.'),
 ('Suggest the redox role of a sample that decolourises purple potassium manganate(VII) acidified with dilute sulphuric acid. [1]','It acts as a reducing agent [1], reducing Mn(VII) to Mn(II).'),
 ('Name NO3− using the syllabus oxidation-number convention. [1]','Nitrate(V) [1]; nitrogen is +5.'),
 ('Suggest the syllabus oxyanion name for ClO−, in which chlorine has oxidation number +1. [1]','Chlorate(I) [1].'),
 ('Explain the error in naming NO2− nitrate(V), using an oxidation-number calculation as a discriminating test. [2]','The V wrongly assigns nitrogen +5 [1]. Charge balance gives x + 2(−2) = −1, so x = +3 and the correct name is nitrate(III) [1].'),
 ('State what electrolysis does to a suitable electrolyte. [1]','Passing an electric current through it causes chemical decomposition [1].'),
 ('Suggest why molten sodium chloride conducts by ion movement but solid sodium chloride does not. [1]','Its ions can move in the melt, whereas the ions in the solid lattice are fixed [1].'),
 ('State the cathode product expected from dilute aqueous copper(II) sulphate with inert electrodes in the ordinary school selective-discharge model. [1]','Copper metal [1].'),
 ('Suggest the anode gas from concentrated aqueous sodium chloride using inert electrodes. [1]','Chlorine [1]; concentrated chloride favours chloride discharge in this cell.'),
 ('State the electrode at which copper ions are reduced when copper is recovered electrolytically from a prepared acidic leach solution. [1]','The cathode [1].'),
 ('Suggest the chemical reason for a growing copper deposit on the cathode during recovery from a prepared copper(II) leach solution. [1]','Cu2+ ions gain electrons to form Cu(s) on the cathode [1].'),
 ('State which side of a cathode reduction half-equation contains the electrons. [1]','The reactant, left-hand side [1].'),
 ('Write the anode half-equation for chlorine formation from concentrated aqueous chloride with an inert anode. Include state symbols. [2]','2Cl−(aq) → Cl2(g) + 2e−. Correct reactant/product and states [1]; atom and charge balance including electrons [1].'),
 ('State the charge carriers in the metallic wires and in the liquid electrolyte of an electrolytic circuit. [1]','Electrons in the wires; mobile ions in the electrolyte [1].'),
 ('Suggest why a claim that free electrons travel through the bulk aqueous electrolyte from cathode to anode is incorrect. [1]','Ions carry charge through the electrolyte; electron transfer occurs at the electrode interfaces [1].')
]
assert len(qa)==len(s)
for slot,(prompt,answer) in zip(s,qa):
 st='WHY' if slot['subtype']=='MECH' else None
 t.item(slot,prompt,answer,subtype=st)
 if st:t.deviations.append({'from':slot['slot']+' MECH','to':'WHY with original AO/Bloom/command/tariff','why':'Electron-transfer reasoning is required, but inventing an intermediate to fit the generic reaction-mechanism structure would misrepresent this oxidation-state explanation.'})
p=t.wo['performance_tasks']
t.item(p[0],'''Identify the correct option in each question. [7]
1. Sulphur in SO4²−, with oxygen −2, is: A +4; B +6; C −2; D +8.
2. A decrease from +7 to +2 represents: A oxidation; B neutralisation; C reduction; D no redox change.
3. An oxidising agent is itself: A reduced; B oxidised; C unchanged in oxidation number; D necessarily oxygen.
4. Colourless aqueous KI becoming brown with a sample indicates that: A iodide is reduced; B potassium is oxidised; C the sample reduces iodide; D iodide is oxidised.
5. In MnO4− + 8H+ + xFe2+ → Mn2+ + 4H2O + xFe3+, x is: A 2; B 5; C 7; D 8.
6. Reducing behaviour can be shown by acidified manganate(VII) changing: A colourless to brown; B blue to white; C purple to colourless; D brown to purple.
7. Fe2+ → Fe3+ + e− describes: A oxidation; B reduction; C condensation; D proton loss.''',
 '''Key: 1 B, 2 C, 3 A, 4 D, 5 B, 6 C, 7 A; one mark per correct option.
1. B follows x − 8 = −2. Distractor A is the sulphite value; C is the ion charge, not sulphur's number; D ignores the ion charge.
2. C is a fall in oxidation number. A has the opposite direction; B is an acid–base label; D ignores the change.
3. A follows electron acceptance. B confuses the agent's own change with what it causes; C omits its redox participation; D confuses a role with one element.
4. D follows iodine formation from iodide. A reverses the electron transfer; B incorrectly involves spectator potassium; C describes the opposite role for the sample.
5. B balances the five-electron gain of manganese with five one-electron iron losses. A borrows the Mn2+ charge; C borrows manganese's initial number; D borrows the hydrogen coefficient.
6. C is reduction to Mn2+ in acid. A describes iodine liberation; B is unrelated to the stated reagent; D introduces a brown starting reagent absent here.
7. A follows electron loss and an increase in oxidation number. B reverses the role; C concerns physical state; D confuses an electron with H+.''')
t.item(p[1],'''Explain the redox chemistry and complete the linked parts. [8]
(a) Calculate manganese's oxidation number in MnO4−, with oxygen −2. [1]
(b) Explain why MnO4− is an oxidising agent when acidified manganate(VII) reacts with Fe2+ to form Mn2+ and Fe3+. [2]
(c) Write the balanced ionic equation for that acidic aqueous reaction. [2]
(d) State the observed change when a small amount of purple acidified manganate(VII) is reduced by excess Fe2+. [1]
(e) Calculate the amount of Fe2+ needed for 0.00400 mol MnO4− and give three significant figures. [2]''',
 '''Part (a): x − 8 = −1, giving manganese +7 [1].
Part (b): Mn falls from +7 to +2 by gaining five electrons [1]; it causes Fe2+ to lose electrons and become Fe3+, so it is the oxidising agent [1].
Part (c): MnO4−(aq) + 8H+(aq) + 5Fe2+(aq) → Mn2+(aq) + 4H2O(l) + 5Fe3+(aq). Correct species/acidic balance [1]; 1:5 redox ratio and total charge balance [1].
Part (d): the purple colour disappears [1]; resulting solution colour can also reflect the other ions present.
Part (e): amount ratio Fe2+:MnO4− is 5:1 [1]; n(Fe2+) = 5 × 0.00400 = 0.0200 mol to three significant figures [1]. Each bracket identifies a separate creditworthy point.''')
t.item(p[2],'''Calculate the amount of Fe2+ that reacts with 18.0 cm³ of 0.0200 mol dm⁻³ acidified manganate(VII). Manganese changes from +7 to +2, iron from +2 to +3, and the resulting purple reagent is decolourised. [5]
(a) Use the oxidation-number changes to obtain the MnO4−:Fe2+ ratio. [2]
(b) Calculate the reacting amount of Fe2+, showing the volume conversion and three significant figures. [2]
(c) State which reactant acts as the reducing agent, consistent with the manganate colour change. [1]''',
 '''(a) Each manganese gains five electrons [1]; each iron loses one, so MnO4−:Fe2+ = 1:5 [1].
(b) Equation n = cV. Convert 18.0 cm³ = 0.0180 dm³; n(MnO4−) = 0.0200 × 0.0180 = 0.000360 mol [1]. Then n(Fe2+) = 5 × 0.000360 = 0.00180 mol to three significant figures [1].
(c) Fe2+ is the reducing agent [1], supplying electrons that reduce the purple Mn(VII) species to Mn(II).''')
t.deviations.append({'from':'Unqualified elementary discharge guide alongside industrial manganese recovery','to':'Teach the school approximation with explicit medium/electrode limits and separately identify engineered metal recovery','why':'Hydrogen competition makes an absolute reactivity-only rule inconsistent with the syllabus industrial example. No unverified plant recipe is introduced; manganese-specific source verification is recorded for semantic review.'})
t.save()
