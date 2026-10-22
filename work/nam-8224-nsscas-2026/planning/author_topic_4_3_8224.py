"""Original halogenoalkane authoring and pair-arrow examples."""
from authoring_common_8224 import Topic
from organic_visuals_8224 import Figure,curved_arrow
t=Topic('4.3')
def add(short,claims,title,text,source,loc):t.objective(short,claims,[(title,text)],source,loc)
add('1-01',[
 'A halogenoalkane has one or more alkane hydrogens replaced by halogen, with C–halogen bonds shown explicitly in skeletal notation.',
 'An open-chain saturated monohalogenoalkane has composition CnH2n+1X; additional halogens replace additional hydrogens.'
], 'Representing halogenoalkanes', '''A halogenoalkane, also called a haloalkane, has one or more hydrogen atoms of an alkane replaced by halogen atoms. The halogen is bonded to a saturated carbon. Write X as a placeholder for F, Cl, Br or I when discussing the family. A saturated open-chain monohalogenoalkane has general composition CnH2n+1X; if two hydrogens are replaced, the corresponding count is CnH2nX2. Do not apply the monohalogen count to a molecule containing several halogens.

Structural condensed notation CH3CH2Br shows bromoethane's two-carbon connection and terminal bromine. A displayed drawing shows each C–H, C–C and C–Br bond. In skeletal notation the carbon positions and carbon-bound hydrogens can be omitted, but the halogen label must be written. A line ending at a printed Br means a bond to bromine, not an additional carbon hidden under that label.

Molecular, empirical, structural condensed, displayed and skeletal forms serve different purposes. A molecular formula gives actual atom counts, an empirical formula gives their simplest ratio, and the remaining forms preserve connectivity with different amounts of detail. For bromoethane, C2H5Br alone does not display each bond. Supplying that count when asked to draw the displayed structure leaves the representation unfinished.

![Original displayed bromoethane](assets/8224-bromoethane-displayed.png)

Carbon still needs four bond contributions: in CH3CH2Br the first carbon has three H and one C bond; the second has two H, one C and one Br bond. The neutral halogen has one covalent bond in this simple representation. Topic 4.2 supplies the hydrocarbon skeleton conventions, and this topic adds explicit halogen attachments without changing the valency-counting method.''',
 '10-1-names-and-structures-of-alkyl-halides','OpenStax Organic §10.1 names/structures and §1.12 representations; original monohalogen atom accounting.')
add('1-02',[
 'Halogenoalkane names use a suitable longest parent chain and numbered fluoro-, chloro-, bromo- and iodo- prefixes.',
 'Different halogen prefixes are written alphabetically, ignoring di- and similar multiplying prefixes for that ordering.'
], 'Naming halogen attachments', '''Choose the longest suitable carbon chain and name it as the parent alkane. Number the chain to obtain the lowest permitted sequence of substituent locants, comparing the first point of difference. The halogen prefixes are fluoro-, chloro-, bromo- and iodo-. A locant identifies the parent carbon carrying each halogen. Thus CH3CH2CH2CH2Cl is 1-chlorobutane, while CH3CHBrCH3 is 2-bromopropane.

Use di- or tri- when the same halogen appears more than once and give a locant for each occurrence. BrCH2CH2Br is 1,2-dibromoethane. Both numbers matter: 1,1-dibromoethane would put both bromines on one carbon and describe a different connectivity. A number records position, whereas di- records how many substituents of that type are present.

When different halogens occur, write their prefixes in alphabetical order. BrCH2CH2CH2Cl is 1-bromo-3-chloropropane: both numbering directions give the locant set 1,3, and the alphabetically earlier bromo receives the lower locant in this tie. Alphabetical order of prefixes is a writing rule; it does not mean their physical positions must follow that order along a drawing. Ignore multiplicative di- and tri- when ordering different substituent names.

Work backwards to check a proposed name: draw the parent, mark the stated carbon numbers, attach each halogen and complete hydrogen valencies. For 1,2-dibromoethane the two carbons each bear two hydrogens, giving BrCH2CH2Br. If the reconstruction does not match the given connectivity, revisit numbering or parent selection. Parent chains up to six carbons are used here, matching the syllabus naming range. Topic 4.1 introduces the shared stems and naming language.''',
 '10-1-names-and-structures-of-alkyl-halides','OpenStax Organic §10.1 naming steps1–3; syllabus §4.3.1 halogen alphabetical order.')
add('1-03',[
 'Halogen atoms occupy carbon valencies that would otherwise bear hydrogen, so each must be included before counting omitted hydrogen.',
 'In skeletal notation an explicitly labelled halogen endpoint is not a carbon endpoint.'
], 'Counting halogen and hydrogen separately', '''Count the carbon skeleton, including branches, and then count every printed halogen label. At each carbon complete four bond contributions with hydrogen. A terminal carbon attached to another carbon and to Br has two hydrogens, not three. A carbon attached to two other carbons and one Br has one hydrogen. The halogen replaces a hydrogen attachment; it is not an extra group added on top of a completed CH3 carbon.

For CH3CHBrCH2Cl, the first carbon supplies three hydrogens, the middle carbon one and the terminal carbon two. The molecular count is C3H6BrCl. An open-chain propane skeleton would have eight hydrogens; replacing two by halogens leaves six, confirming the direct count. The structure is 2-bromo-1-chloropropane after lowest-locant numbering, illustrating that atom counting and naming ask related but distinct questions.

In a skeletal drawing, trace each unlabelled carbon end and vertex once. If a final line meets the printed symbol Cl, that endpoint is chlorine. Inventing an extra carbon there would increase both the carbon and hydrogen totals. Conversely, omitting a labelled halogen from the atom count gives the composition of a different substance even if the carbon count happens to agree.

A molecular formula records actual atom numbers, while an empirical formula records their simplest ratio. Structural condensed, displayed and skeletal forms additionally communicate connections. For BrCH2CH2Br, molecular C2H4Br2 reduces to empirical CH2Br; neither request is satisfied by accidentally giving the other. Molecular, empirical, structural condensed, displayed and skeletal representations should therefore be chosen deliberately. Topic 1.1 explains composition calculations from measurements, whereas the present method reads atoms directly from a supplied structure.''',
 '10-1-names-and-structures-of-alkyl-halides','OpenStax Organic §10.1 and §1.12; original atom counts and numbering.')
add('1-04',[
 'Heated aqueous hydroxide substitutes Br in bromoethane to form ethanol; ethanolic cyanide forms propanenitrile with one extra carbon.',
 'Excess ethanolic ammonia reacts with bromoethane to favour ethanamine; two ammonia molecules appear in the net primary-amine equation.',
 'Heated ethanolic hydroxide favours elimination from 2-bromopropane, giving propene, water and bromide.',
 'Direct hydroxide substitution at primary bromoethane is a single-step pair-transfer process without a discrete carbocation intermediate.'
], 'Substitution and elimination use different routes', '''Heating bromoethane with aqueous sodium or potassium hydroxide gives ethanol by nucleophilic substitution: CH3CH2Br + OH− → CH3CH2OH + Br−. A hydroxide lone pair forms a bond to the electron-deficient carbon attached to Br while the C–Br bond pair goes to Br. Draw a full curved arrow from oxygen's lone pair to that carbon and a second from C–Br to Br. In this direct primary-halogenoalkane route, the changes occur together; there is no separate ethyl carbocation intermediate.

![Original substitution pair arrows](assets/8224-bromoethane-hydroxide.png)

Heating bromoethane with ethanolic potassium or sodium cyanide gives CH3CH2CN, propanenitrile: CH3CH2Br + CN− → CH3CH2CN + Br−. The attacking carbon of cyanide becomes part of the organic product, so the chain gains one carbon. Heating with excess ethanolic ammonia favours ethanamine: CH3CH2Br + 2NH3 → CH3CH2NH2 + NH4Br. The first attack gives an alkylammonium species; another ammonia removes a proton. Excess ammonia favours attack by ammonia rather than further alkylation of the amine, although it does not guarantee a pure single product.

Heating 2-bromopropane with ethanolic hydroxide instead favours elimination. CH3CHBrCH3 + OH− → CH3CH=CH2 + H2O + Br−. The base removes hydrogen from a neighbouring carbon as the carbon–carbon double bond forms and Br leaves. Hydrogen and bromine are removed from adjacent carbons; they are not replaced by OH on the same carbon. Aqueous hydroxide favours the substitution preparation, while heated ethanolic hydroxide favours this elimination preparation. Carry solvent and heating information with the predicted product. Topic 4.4 studies the resulting alcohol chemistry; Topic 4.2 studies the resulting alkene.''',
 '11-2-the-sn2-reaction','OpenStax Organic §11.2 direct substitution; Study Guide §§11.7–11.8 elimination and amine/nitrile chapters; syllabus §4.3.1 examples and preparation settings.')
add('2-01',[
 'For comparable halogenoalkanes under matched hydrolysis settings, weaker C–halogen bonds generally permit faster reaction.',
 'The carbon–halogen bond weakens from C–F through C–Cl and C–Br to C–I; polarity alone does not determine hydrolysis rate.'
], 'Interpreting hydrolysis reactivity', '''Compare halogenoalkanes with the same carbon skeleton under matched temperature, solvent composition and reagent concentration. Changing several factors at once would make a rate difference ambiguous. For analogous alkyl compounds, hydrolysis tends to become faster in the order fluoroalkane, chloroalkane, bromoalkane, iodoalkane. The C–halogen bond becomes weaker down that sequence, making the required bond breaking easier in the relevant reaction pathway.

The C–F bond is strongly polar because fluorine is much more electronegative than carbon, but it is also particularly strong. A prediction based on polarity alone would therefore be misleading. An iodoalkane can hydrolyse more rapidly than its fluoro analogue despite the C–I bond's smaller polarity. The explanation must consider the energy and pathway for bond cleavage, not just the partial positive charge at carbon.

Suppose equal concentrations of chloroethane, bromoethane and iodoethane are compared in the same solvent at the same temperature. If the measured times to a defined equal extent of reaction are 150 s, 45 s and 12 s, the iodo compound reaches that endpoint fastest. This evidence supports faster hydrolysis under the stated settings; it is not a claim that a reaction time is a universal constant for that compound. Changing the endpoint would change the times used in the comparison.

Keep the carbon skeleton matched because substitution pattern can affect mechanism and rate. The simple halogen trend is not a licence to rank arbitrary primary, secondary and tertiary molecules using just one bond-energy number. Topic 2.4 supplies the broader kinetic reasoning, and the final section here distinguishes bond energy, bond length and polarity as different properties.''',
 '10-1-names-and-structures-of-alkyl-halides','OpenStax Organic §10.1 Table10.1 lengths/strengths and §11 substitution; original controlled comparison.')
add('2-02',[
 'Strong C–F bonding helps explain the relative chemical inertness of suitable fluorinated compounds in ordinary service.',
 'Chemical resistance can make fluorinated materials useful in applications, but lower-atmosphere stability does not rule out upper-atmosphere photochemistry.'
], 'Uses depend on resistance during service', '''Fluorinated compounds can be relatively resistant to chemical attack because C–F bonds are strong. A molecule that remains stable during use can be useful where unwanted reaction would damage equipment or contaminate a material. Fluorohalogenoalkanes were historically used as refrigerants and aerosol propellants partly because of their relative chemical inertness during normal service. Their physical properties, including suitable volatility, also mattered: bond strength alone does not explain the complete engineering choice.

Relative inertness needs a setting. Resistance to reaction in the lower atmosphere or inside equipment does not mean resistance to energetic ultraviolet radiation in the stratosphere. A chlorofluoroalkane can survive long enough to be transported upwards and then undergo photochemical C–Cl cleavage. Its C–F bonds being strong does not prevent a different bond in the molecule from breaking. Treating the molecule as if all its bonds had fluorine's bond strength would miss the ozone problem.

An explanation of a use should connect a material property to the application. For a refrigerant example, stability under ordinary operating settings limits unwanted chemical reaction, while evaporation and condensation transfer thermal energy. It is insufficient to say “it contains fluorine, therefore it is useful” without identifying the relevant property and task. Equally, usefulness in one setting does not establish environmental suitability after release.

The next sections explain the separate ozone consequence and the development of replacement compounds. The discussion is historical and conceptual; it does not claim that a particular substance is currently permitted in a jurisdiction or recommend a refrigerant for a modern installation. Such a choice would require additional engineering and current regulatory information beyond the chemistry comparison taught here.''',
 'OpenStax-Chemistry','§18.11 fluorohalogen uses and §18.12 ozone; Organic §10.1 C–F strength; syllabus §4.3.2 applications.')
add('2-03',[
 'Chlorofluoroalkanes can release chlorine radicals under stratospheric ultraviolet radiation, leading to catalytic ozone destruction.',
 'A chlorine radical can be regenerated in an ozone-destruction cycle, so one released radical can participate repeatedly.'
], 'Chlorofluoroalkanes and stratospheric ozone', '''Stratospheric ozone absorbs ultraviolet radiation that would otherwise reach Earth's surface in greater amounts. Ozone depletion means a reduction in that protective ozone concentration. Chlorofluoroalkanes, often called CFCs, can be sufficiently persistent in the lower atmosphere to reach the stratosphere. Energetic ultraviolet radiation there can break a C–Cl bond homolytically and release a chlorine radical.

One simplified catalytic cycle is Cl• + O3 → ClO• + O2, followed by ClO• + O → Cl• + O2. Adding the two steps cancels Cl• and ClO• and gives O3 + O → 2O2. Chlorine radical is regenerated, so its effect is not limited to removing one ozone molecule and then becoming permanently used up. This example uses atomic oxygen already present in stratospheric photochemistry; the second step is not a claim that atomic oxygen is the main bulk form of atmospheric oxygen.

The consequence is reduced shielding from harmful ultraviolet radiation. Keep this chain of reasoning distinct from the enhanced greenhouse effect, which concerns absorption of outgoing infrared radiation. The same broad environmental discussion can include both, but they are different mechanisms involving different radiation and atmospheric roles. Ozone also has a different effect near the ground, where it contributes to air pollution; its usefulness in the stratosphere does not make ground-level ozone desirable.

When a compound contains fluorine and chlorine, identify which bond supplies the relevant radical rather than assuming that fluorine is responsible because C–F is polar. The stability of the original molecule during ordinary service can help it reach the region where photolysis occurs. Topic 4.2 provides radical-chain language, while the preceding section shows why an apparently useful property can have a different consequence after environmental release.''',
 'OpenStax-Chemistry','§18.12 stratospheric ozone and §12.7 ozone catalysis; original balanced simplified chlorine cycle.')
add('2-04',[
 'Developing replacements that avoid releasing ozone-destroying chlorine radicals addresses the CFC ozone-depletion mechanism.',
 'Removing chlorine from a replacement structure does not by itself establish low greenhouse impact or overall environmental suitability.'
], 'Replacement compounds and ozone recovery', '''Replacement compounds were developed to preserve useful applications while reducing damage to stratospheric ozone. One structural approach is to avoid chlorine in a refrigerant molecule, so it cannot supply chlorine radicals by C–Cl photolysis. Hydrofluorocarbons contain hydrogen, fluorine and carbon but no chlorine. They illustrate how changing molecular composition can remove the specific chlorine-based ozone-destruction route associated with CFCs.

Some earlier replacement families retained chlorine but incorporated hydrogen, which can make lower-atmosphere breakdown more likely. Such a change can reduce the fraction reaching the stratosphere, but retaining chlorine means the compound should not be described as structurally incapable of releasing chlorine radicals. Distinguish a reduced contribution from complete removal of a proposed source.

Reduced input of ozone-destroying substances allows natural ozone formation and destruction processes to move towards recovery. It does not imply that previously released persistent molecules disappear immediately or that adding a replacement repairs ozone directly. The replacement reduces further damaging input; atmospheric processes then determine the timescale. This explanation does not depend on claiming a current measured size of the ozone hole or forecasting a particular recovery year.

A compound with no chlorine can still absorb infrared radiation and contribute to warming. Evaluating ozone depletion and greenhouse impact therefore requires two separate questions. For example, the structural observation that a candidate refrigerant contains C, H and F but no Cl supports absence of its chlorine-radical source. It supplies no numerical information about atmospheric lifetime or warming effect. A careful conclusion states what the evidence establishes and what additional properties would be needed for a complete comparison, rather than calling a replacement environmentally harmless from one structural feature.''',
 'NSSCAS-8224-SYLLABUS','§4.3.2 replacement compounds and ozone repair; OpenStax Chemistry §18.12 CFC cause; replacement-family detail is a focused independent source-verification item.')
add('2-05',[
 'Bond energy measures energy for gaseous bond breaking, bond length is internuclear separation, and bond polarity concerns unequal electron sharing.',
 'For comparable carbon–halogen bonds, length generally increases and strength decreases down the halogen group, while reactivity also depends on the reaction pathway.'
], 'Energy, length and polarity are different comparisons', '''Bond energy is the energy required to break one mole of a specified covalent bond in gaseous species; tabulated mean bond energies average over suitable molecular environments. Breaking bonds requires energy. Bond length is the distance between the bonded nuclei at their stable separation, commonly expressed in picometres. Bond polarity is unequal sharing of the bonding electron density because the bonded atoms differ in electronegativity. It is indicated by partial charges, not by assigning complete ionic charges to a neutral covalent molecule.

For comparable carbon–halogen bonds, the halogen atom becomes larger from F to I, so C–halogen length increases. Bond strength generally decreases along C–F, C–Cl, C–Br, C–I. This is a trend within a specified related family, not a universal mathematical rule linking the length of any two unrelated bonds to their reaction rate. Electronic structure and the rest of each molecule also matter.

The halogen attracts the C–halogen pair more strongly than carbon does, leaving carbon δ+ and halogen δ−. A nucleophile can donate a pair to that electron-deficient carbon. However, the particularly strong C–F bond resists breaking even though it is very polar. Thus “more polar” and “more easily hydrolysed” are different judgments and can lead to different rankings.

As a worked interpretation, suppose analogous compounds have supplied C–X breaking energies 340 and 240 kJ mol−1. The lower value represents easier isolated gaseous bond breaking, but neither number alone specifies the whole activation barrier in solution. Use it alongside the matched hydrolysis evidence and settings. Topic 1.3 explains electronegativity and bond polarity, Topic 2.1 uses bond energies in overall enthalpy estimates, and Topic 2.4 distinguishes those estimates from the kinetic barrier determining rate.''',
 '10-1-names-and-structures-of-alkyl-halides','OpenStax Organic §10.1 Table10.1 and polarity; Chemistry §7.5 bond energy/length; supplied comparison numbers original.')

out=t.dir/'assets'
f=Figure('Displayed bromoethane','Two single-bonded carbons; first bears three hydrogens, second two hydrogens and bromine.')
for x in [280,470]:
 f.text(x,215,'C',32);f.text(x,95,'H',28);f.text(x,340,'H',28)
 f.line([(x+10,140),(x+10,205)]);f.line([(x+10,260),(x+10,330)])
f.text(150,215,'H',28);f.text(620,215,'Br',28)
f.line([(190,235),(270,235)]);f.line([(320,235),(460,235)]);f.line([(510,235),(605,235)])
f.text(45,420,'CH3CH2Br: C2H5Br; carbon has four single bonds.',20);f.save('8224-bromoethane-displayed',out=out)
f=Figure('Bromoethane substitution by hydroxide','Hydroxide oxygen lone pair attacks carbon attached to Br while C-Br pair goes to Br. Primary direct route; no discrete carbocation intermediate. Products ethanol and bromide.')
f.text(50,160,'HO:−',30);f.text(280,160,'CH2',30);f.text(470,160,'Br',30)
f.line([(350,180),(455,180)]);f.text(280,280,'CH3',28);f.line([(305,210),(305,270)])
curved_arrow(f,(100,165),(293,170),(195,75));curved_arrow(f,(405,180),(485,205),(455,255))
f.text(50,355,'CH3CH2OH  +  Br−',30);f.text(50,415,'Heated aqueous hydroxide; arrows show pairs in one step.',20)
f.save('8224-bromoethane-hydroxide',out=out)
qa=[
('Identify the general composition of a saturated open-chain monohalogenoalkane.','CnH2n+1X, where X is a halogen.'),
('Draw displayed bromoethane.','Draw C–C with three explicit H bonds at the first carbon and two explicit H plus Br at the second. C–Br is single; see assets/8224-bromoethane-displayed.png.'),
('Name BrCH2CH2CH2Cl.','1-bromo-3-chloropropane.'),
('Suggest the correct name for BrCH2CH2Br.','1,2-dibromoethane.'),
('State how each halogen replacement changes the hydrogen count of an otherwise saturated open-chain alkane skeleton.','Each halogen replaces one hydrogen.'),
('Determine the molecular composition of CH3CHBrCH2Cl.','C3H6BrCl.'),
('Describe the products formed when bromoethane reacts separately with heated aqueous hydroxide, ethanolic cyanide and excess ethanolic ammonia.','Ethanol by hydroxide substitution; propanenitrile by cyanide substitution with one extra carbon; ethanamine favoured with excess ammonia, alongside ammonium bromide in the net balance.'),
('Explain the electron-pair movements when heated aqueous hydroxide substitutes bromine in bromoethane.','An oxygen lone pair forms a bond to the carbon attached to Br while C–Br transfers its pair to Br, giving ethanol and Br− in one step. There is no discrete carbocation intermediate in this direct primary route.'),
('Draw the full curved arrows for substitution of bromoethane by heated aqueous hydroxide.','Draw a hydroxide lone-pair arrow to the carbon bearing Br and an arrow from C–Br to Br; products CH3CH2OH and Br−. Both arrows represent pairs in the same step; see assets/8224-bromoethane-hydroxide.png.'),
('State the hydrolysis reactivity order for analogous fluoro-, chloro-, bromo- and iodoalkanes under matched settings.','Fluoro < chloro < bromo < iodo in increasing reactivity.'),
('Determine which analogous compound hydrolyses fastest if equal endpoints occur at 150 s for chloroethane, 45 s for bromoethane and 12 s for iodoethane under identical settings.','Iodoethane: it reaches the equal endpoint in the shortest time.'),
('Describe how relative inertness supported historical refrigerant and propellant uses of fluorohalogenoalkanes.','Chemical resistance reduced unwanted reactions during service; strong C–F bonding contributed to that resistance; suitable physical properties such as volatility also supported the use.'),
('Explain why a strong C–F bond does not prevent ozone-depleting chlorine release from a chlorofluoroalkane.','The molecule can contain a separate C–Cl bond that undergoes stratospheric ultraviolet cleavage; resistance of C–F does not establish resistance of C–Cl under that setting.'),
('State the atmospheric consequence of chlorine radicals released from CFCs in the stratosphere.','They catalyse ozone destruction and reduce the protective ozone concentration.'),
('Suggest why one stratospheric chlorine radical can participate in destroying multiple ozone molecules.','It is regenerated in the catalytic reaction cycle.'),
('State one structural approach used in developing replacements for ozone-depleting chlorofluoroalkanes.','Use a suitable compound without chlorine, removing its C–Cl source of chlorine radicals.'),
('Suggest why a chlorine-free replacement cannot be judged environmentally harmless from that fact alone.','It may still absorb infrared radiation and contribute to warming; ozone depletion and greenhouse impact are separate properties.'),
('Describe bond energy, bond length and bond polarity.','Bond energy is the energy to break one mole of specified gaseous bonds; bond length is internuclear separation; polarity is unequal sharing of bond electron density.'),
('Contrast C–F and C–I when explaining hydrolysis of analogous halogenoalkanes under matched settings.','C–F is shorter, stronger and more polar; C–I is longer, weaker and less polar. Easier C–I cleavage supports faster hydrolysis, showing that polarity alone does not determine rate.')]
for slot,(q,a) in zip(t.wo['item_slots'],qa):
 st='WHY' if slot['slot'].endswith('013-MECH') else None
 t.item(slot,q,a,subtype=st)
 if st:t.deviations.append({'from':slot['slot']+' MECH','to':'WHY with all frozen slot metadata retained','why':'The objective explains inertness/use, not a required electron-level mechanism with an intermediate.'})
mc=[
('Name CH3CH2CH2Cl.',['1-chloropropane','2-chloropropane','1-chlorobutane','propene'],0,'A matches three carbons and terminal Cl; B moves Cl, C adds carbon and D removes halogen and changes bonding.'),
('Identify the gas region protected by ozone relevant to CFC depletion.',['ground-level smog','stratospheric ozone layer','dissolved oxygen in water','a fuel tank'],1,'B is the protective ozone layer; A is a different ozone problem and C/D are unrelated locations.'),
('Identify a structural approach removing a refrigerant chlorine-radical source.',['increase chlorine content','ignore structure','use a suitable chlorine-free replacement','make more CFC'],2,'C removes its C–Cl source; A/D retain or increase that source and B supplies no chemical solution.'),
('Name CH3CHBrCH2CH3.',['1-bromobutane','3-bromobutane','2-bromopropane','2-bromobutane'],3,'D gives the correct four-carbon parent and lower locant; A moves Br, B misnumbers, C loses carbon.'),
('Identify the supported conclusion if a CFC radical is regenerated in an ozone cycle.',['it can react repeatedly','it is permanently consumed in the first step','it becomes a harmless final polymer','ozone is unaffected'],0,'A follows regeneration; B contradicts it, C invents a product and D ignores net ozone loss.'),
('Identify the supported conclusion for a replacement containing C,H,F but no Cl.',['it cannot warm the atmosphere','it lacks a C–Cl chlorine source','it instantly repairs existing ozone loss','its lifetime is known numerically'],1,'B follows composition; A/C overstate consequences and D requires measurements not given.')]
t.item(t.wo['performance_tasks'][0],'Identify the correct option in each question (1 mark each).\n'+'\n'.join(f'{i}. {q} '+ '; '.join(f'{"ABCD"[j]} {v}' for j,v in enumerate(opts)) for i,(q,opts,k,a) in enumerate(mc,1)), '\n'.join(f'{i}. Key/correct option {"ABCD"[k]}. {a} Each distractor reflects the specified error.' for i,(q,opts,k,a) in enumerate(mc,1)))
t.item(t.wo['performance_tasks'][1],'''Explain changes to a two-carbon saturated molecule bearing one Br.
(a) Draw its displayed structure and name it. [3]
(b) State its molecular composition. [1]
(c) Write its ionic reaction with heated aqueous hydroxide. [2]
(d) Explain why heated ethanolic cyanide gives a three-carbon organic product. [2]''',
'''(a) Two single-bonded C atoms [1], three H on one and two H plus Br on the other [1], bromoethane [1]. (b) C2H5Br [1]. (c) CH3CH2Br + OH− → CH3CH2OH + Br−: organic change [1], correct ionic balance [1]. (d) Carbon of CN− bonds to the carbon losing Br [1]; its added carbon gives CH3CH2CN, propanenitrile [1]. Creditworthy points shown per part, total8 marks.''')
t.item(t.wo['performance_tasks'][2],'''Calculate the maximum ethanol mass obtainable by complete hydrolysis of 5.45 g of the saturated two-carbon monobromo compound. Name and represent that reactant. Use Ar(C)=12.0, Ar(H)=1.0, Ar(Br)=79.9 and Mr(ethanol)=46.0. [5]''',
'''Bromoethane, CH3CH2Br, molecular composition C2H5Br [1]. Equation: CH3CH2Br + OH− → CH3CH2OH + Br− [1], so mole ratio1:1. Working: Mr(bromoethane)=2(12.0)+5(1.0)+79.9=108.9; n=5.45/108.9=0.0500459 mol [1]. Ethanol n=0.0500459 mol [1]; m=0.0500459×46.0=2.30211 g, answer2.30 g to three significant figures [1]. Mass units already g; retain unrounded intermediate values.''')
t.deviations.append({'from':'Generic MECH guidance may imply an intermediate for each mechanism','to':'Primary direct substitution explicitly has no discrete carbocation intermediate','why':'OpenStax §11.2 establishes a one-step pathway; a transition state must not be presented as an intermediate.'})
t.deviations.append({'from':'Syllabus-only application coverage for replacement compounds and exact school preparation settings','to':'Explicit independent semantic source-verification focus','why':'Core substitution, bond trends and ozone chemistry have direct held references; replacement-family detail and ethanolic ammonia/cyanide preparations need more precise verification before release.'})
t.save()
