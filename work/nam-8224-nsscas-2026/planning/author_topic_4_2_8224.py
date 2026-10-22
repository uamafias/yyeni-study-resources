"""Original hydrocarbon teaching, structures, mechanisms and practice."""
from authoring_common_8224 import Topic
from organic_visuals_8224 import Figure, curved_arrow
t=Topic('4.2')
def add(short,claims,title,text,source,loc):t.objective(short,claims,[(title,text)],source,loc)
add('1-01',[
 'Open-chain saturated hydrocarbons contain C–C and C–H single bonds and follow CnH2n+2.',
 'A skeletal hydrocarbon drawing implies carbon at unlabelled vertices and ends, with enough attached hydrogen to complete four bond contributions.'
], 'Alkanes in several representations', '''An alkane is a saturated hydrocarbon: it contains carbon and hydrogen, with single bonds between its carbon atoms. The open-chain series has general composition CnH2n+2. Here n counts all carbon atoms, including branches. Methane is CH4, ethane C2H6 and hexane C6H14. This relationship applies to open chains; a saturated carbon ring has a different hydrogen count because closing the ring makes an additional C–C connection.

A molecular formula records actual numbers of atoms, while an empirical formula gives their simplest ratio. Structural condensed notation groups atoms by their connections, a displayed drawing shows each bond, and skeletal notation omits carbon labels and hydrogens bonded to carbon. These molecular, empirical, structural condensed, displayed and skeletal forms carry different amounts of information. For ethane, C2H6 gives composition, CH3CH3 shows two connected methyl groups, and a displayed drawing shows six C–H bonds and one C–C bond. Its empirical ratio is CH3, which does not describe an isolated ethane molecule.

In skeletal notation a line end or unlabelled corner represents a carbon. A three-segment zigzag has four carbon positions, not three. With single bonds and no ring it represents butane, CH3CH2CH2CH3. At each end the carbon has one carbon neighbour and therefore three hydrogens; each internal carbon has two neighbours and two hydrogens. A branch creates another carbon position and must be counted.

![Original displayed ethane and skeletal butane](assets/8224-alkane-representations.png)

Practise both directions: expand a skeletal drawing into grouped atoms, then hide the carbon labels and carbon-bound hydrogens again. The connectivity must survive the conversion. Neither the zigzag's angle on the page nor its orientation changes the atom count. Topic 4.1 explains why a connectivity drawing is different from a three-dimensional shape drawing.''',
 '3-2-alkanes-and-alkane-isomers','OpenStax Organic §3.2 saturated chains and representations; §1.12 skeletal conventions; syllabus §4.2.1.')
add('1-02',[
 'An alkane parent is its longest continuous carbon chain, numbered to give substituents the lowest permitted locants.',
 'The name 2,2-dimethylhexane describes a six-carbon parent and two methyl substituents, eight carbons in total.'
], 'Names reconstruct connections', '''The parent name describes the longest continuous carbon chain. For one through six carbons use methane, ethane, propane, butane, pentane and hexane. A continuous chain can turn a corner in a drawing; the horizontal row is not automatically the parent. Trace possible routes without visiting a carbon twice, then choose the longest suitable route. Carbons outside that chain become substituents.

A methyl substituent, –CH3, is obtained conceptually by removing one hydrogen from methane. An ethyl substituent is –CH2CH3. Number the parent from the end giving the lower sequence of branch positions, comparing the first point of difference. CH3CH(CH3)CH2CH3 is 2-methylbutane: its longest route has four carbons, and its methyl branch is at carbon 2 rather than carbon 3. The molecule has five carbons altogether. Do not call it methylpentane just because five carbons appear in total.

Repeated identical substituents use di-, tri- and related prefixes. Each substituent needs a locant, including when two attach to the same parent carbon. Thus CH3C(CH3)2CH2CH2CH2CH3 is 2,2-dimethylhexane. Carbon 2 has four carbon bonds and no hydrogen. There are six parent carbons and two additional methyl carbons: eight in the molecule. The syllabus's six-carbon parent-chain limit therefore does not impose a six-carbon limit on the whole branched molecule.

Use commas between numbers and hyphens between numbers and words. To work backwards, draw the parent chain, number it, attach the named groups, and finally fill hydrogen valencies. Recheck the longest route before accepting the name. This prevents an apparently neat drawing from hiding a longer chain that should have been the parent.''',
 '3-4-naming-alkanes','OpenStax Organic §3.4 steps 1–4; syllabus §4.2.1 six-carbon parent and explicit dimethylhexane example.')
add('1-03',[
 'Alkane atom counts can be obtained by completing carbon valencies in the given connectivity.',
 'Branching changes connectivity but does not change the CnH2n+2 count for an open-chain saturated hydrocarbon.'
], 'Counting atoms rather than line segments', '''To determine composition from a structure, count carbon positions first, then count attached hydrogen by valency. A neutral alkane carbon has four single bonds. An end carbon attached to one other carbon is CH3, a carbon attached to two is CH2, one attached to three is CH, and one attached to four is C with no hydrogen. In a skeletal drawing the omitted hydrogen is still chemically present; its absence from the ink does not remove it from the molecule.

For CH3CH(CH3)CH2CH3, there are three CH3 groups, one CH and one CH2. The total is five carbon atoms and 9 + 1 + 2 = 12 hydrogens, giving C5H12. The parent-chain length is four but the total carbon count is five. The open-chain check gives 2(5) + 2 = 12 hydrogens, consistent with the detailed count. Use that check after reading the branches, rather than treating the parent name as the whole molecule's carbon count.

For 2,2-dimethylhexane, CH3C(CH3)2CH2CH2CH2CH3 contains four CH3 groups, three CH2 groups and one carbon without hydrogen. Total hydrogen is 12 + 6 = 18 and carbon is eight, so the molecular composition is C8H18. A wrong answer C6H14 has ignored the two methyl groups; C8H20 has not accounted for the four bonds already attached to the central carbon.

Molecular, empirical, structural condensed, displayed and skeletal forms can describe related information but answer different requests. The molecular formula C8H18 reduces to empirical C4H9; neither gives the connectivity by itself. If asked for the molecular form, retain actual atom counts. If asked for a displayed structure, show individual bonds instead of supplying just C8H18. Topic 1.1 covers the separate calculation of composition from measured masses.''',
 '3-2-alkanes-and-alkane-isomers','OpenStax Organic §3.2 structures and composition; original worked valency counts.')
add('1-04',[
 'Strong, nearly non-polar C–C and C–H bonds and the absence of an electron-rich multiple bond help explain alkane unreactivity towards many polar reagents.',
 'Alkane combustion and light-initiated halogen substitution require suitable activation despite general resistance to polar attack.'
], 'Why many polar reagents leave alkanes unchanged', '''Alkanes are generally unreactive towards many polar reagents under ordinary laboratory settings. Their C–C and C–H bonds are strong, and their bonding has little charge separation. A C–C bond joins identical atoms; the electronegativity difference between carbon and hydrogen is relatively small. There is no strongly electron-deficient carbon attached to a leaving group and no electron-rich C=C region for the familiar polar addition route.

An electrophile needs an accessible electron pair with which to form a bond; a nucleophile needs a suitable electron-poor centre. The saturated alkane skeleton provides neither of the strongly reactive sites used in the simple ionic reactions taught here. Saying merely that an alkane has “no charge” is insufficient: several neutral molecules, including alkenes, react readily with electrophiles. The relevant explanation concerns bond strength, electron distribution and the available reaction pathway.

Consider two separate samples, ethane and ethene, contacted with bromine without radical-initiating light. Ethene can react by addition at C=C. Ethane lacks that multiple bond and does not undergo the corresponding rapid addition. Under suitable ultraviolet light, however, bromine can form radicals and substitute a hydrogen in ethane. The different outcome follows a different mechanism, rather than contradicting the general statement about resistance to polar attack.

Alkanes also burn after ignition in oxygen. A high activation barrier can prevent noticeable reaction before ignition even when the overall combustion releases energy. Bond breaking needs energy at the start; formation of product bonds releases more energy over the complete process. Topic 2.1 separates activation energy from overall enthalpy, while Topic 2.4 explains how a temperature increase changes the fraction of sufficiently energetic collisions. Do not translate general unreactivity into a claim that alkanes cannot take part in chemical reactions.''',
 'OpenStax-Chemistry','§20.1 saturated hydrocarbons and combustion; §12.5 activation; OpenStax Organic §6.5 polar reactions and §10.2 radical substitution.')
add('1-05',[
 'Complete ethane combustion forms carbon dioxide and water; oxygen shortage can produce carbon monoxide or carbon.',
 'Under suitable radical-initiating light, ethane substitutes hydrogen with chlorine or bromine, forming a haloethane and hydrogen halide.'
], 'Ethane combustion and halogen substitution', '''Ethane burns in sufficient oxygen to produce carbon dioxide and water. A balanced equation is 2C2H6(g) + 7O2(g) → 4CO2(g) + 6H2O(g) for water vapour in hot combustion products. If products are specified after cooling, water can be written as liquid instead; the stated physical setting determines its symbol. Balance carbon first, hydrogen second and oxygen last. One ethane molecule needs seven oxygen atoms, so using whole-number coefficients requires two ethane molecules and seven oxygen molecules.

Incomplete combustion under oxygen shortage can produce carbon monoxide and carbon particles as well as water. An idealised carbon-monoxide equation is 2C2H6 + 5O2 → 4CO + 6H2O. Actual flames can give mixtures rather than one pure carbon product. A black deposit indicates carbon-containing soot, not carbon dioxide, which is a gas under these settings.

With chlorine under suitable ultraviolet light, ethane gives chloroethane and hydrogen chloride: C2H6 + Cl2 → C2H5Cl + HCl. With bromine under radical-initiating light, C2H6 + Br2 → C2H5Br + HBr. These are substitution reactions: a hydrogen attached to carbon is replaced by a halogen atom, and the removed hydrogen appears in a hydrogen halide. Both atoms of a halogen molecule are therefore accounted for. The C–C skeleton remains intact in the first substitution.

Further substitution can follow because the first organic product still contains C–H bonds. Consequently the equations show one substitution stage, not a guarantee of a single pure final product. Excess alkane relative to halogen favours a greater proportion of singly substituted material, but the process can still need separation. Topic 4.3 develops haloalkane reactions; here the focus is their formation from an alkane and the radical chain that explains it.''',
 '10-2-preparing-alkyl-halides-from-alkanes-radical-halogenation','OpenStax Organic §10.2 radical halogenation; OpenStax Chemistry §20.1 combustion; original balanced ethane equations.')
add('1-06',[
 'Radical initiation involves homolytic bond fission; propagation consumes one radical while generating another; combination termination consumes radicals.',
 'Ethane chlorination propagates through Cl• + C2H6 → HCl + C2H5• and C2H5• + Cl2 → C2H5Cl + Cl•.',
 'A fishhook curved arrow represents movement of one electron, while a dot on a radical represents an unpaired electron.'
], 'Following the radical chain', '''A free radical is a species containing an unpaired electron. A dot records that electron; it is not a negative charge. In initiation, light supplies energy for homolytic fission of chlorine: Cl2 → 2Cl•. Each atom takes one electron from the original Cl–Cl pair. Draw two fishhook arrows starting at the bond, one towards each chlorine atom. Full-headed arrows would incorrectly indicate the movement of electron pairs.

Propagation in ethane chlorination has two linked steps. First, Cl• + CH3CH3 → HCl + CH3CH2•. The chlorine radical abstracts hydrogen and leaves an ethyl radical intermediate. Second, CH3CH2• + Cl2 → CH3CH2Cl + Cl•. The ethyl radical forms a C–Cl bond and regenerates chlorine radical. Add these equations and cancel the intermediate radicals to recover C2H6 + Cl2 → C2H5Cl + HCl. One radical is used and another is produced at each propagation step, which permits the chain to continue.

For electron movement in hydrogen abstraction, one electron from C–H remains on carbon, while the other pairs with the chlorine radical's electron in H–Cl. For attack on Cl2, one electron from Cl–Cl pairs with the carbon radical's electron in the new C–Cl bond; the other stays on the departing chlorine. Fishhook arrows distinguish these single-electron changes from ionic addition.

Termination combines radicals without regenerating a radical. Examples are Cl• + Cl• → Cl2, C2H5• + Cl• → C2H5Cl, and C2H5• + C2H5• → C4H10. The last equation explains a possible longer-chain side product. Substituting a hydrogen on a methyl group does not replace the entire carbon group: methane analogously forms CH3Cl through CH3•. Identify initiation, propagation or termination from the radical accounting, rather than from whether an organic product happens to appear.''',
 '6-6-radical-reactions','OpenStax Organic §6.6 chain and single-electron movement; §10.2 extension to ethane; original ethyl examples.')
add('1-07',[
 'Crude oil is a mixture that supplies aliphatic and aromatic hydrocarbons; fractions remain mixtures.',
 'Fractional distillation separates components by boiling behaviour, whereas chemical refining changes molecular connectivity.'
], 'Crude oil as a chemical feedstock', '''Crude oil is a complex mixture rather than a pure compound with one fixed composition. It contains hydrocarbons with a range of molecular sizes and structures, together with other substances. Aliphatic hydrocarbons include open-chain saturated and unsaturated compounds; aromatic hydrocarbons contain the characteristic benzene-type ring system. The word aromatic describes this structural family, not a test based on a pleasant smell.

Fractional distillation separates crude oil into groups of substances with different boiling ranges. Vapours rise through a temperature gradient and condense in regions suited to their boiling behaviour. A fraction is still a mixture: collecting one fraction does not establish that it contains a single alkane. Larger hydrocarbon molecules generally have stronger intermolecular attractions and higher boiling temperatures within comparable families, which helps organise the separation.

Some fractions serve as fuels, while others provide feedstock for producing useful smaller molecules and polymer monomers. Aliphatic and aromatic materials can be obtained through separation and further refinery processing. A refinery can also change molecules by chemical reactions; it is therefore necessary to distinguish a source of a substance from a claim that simple distillation makes that substance. Distillation does not break covalent bonds in a large molecule to create an alkene. Cracking does change those bonds.

For example, an invented materials workshop receiving a mixed hydrocarbon feed cannot infer a unique molecular structure merely from its boiling range. It needs composition information before identifying individual molecules. Nor does a sample's origin in crude oil prove that all its molecules are saturated open chains: aromatic structures belong to a different hydrocarbon family. Topic 1.3 provides the bonding background for benzene-type delocalisation, while the next section explains why chemical cracking changes the balance between large fuel molecules and useful smaller feedstocks.''',
 'OpenStax-Chemistry','§11.5 fractional distillation; §20.1 hydrocarbons; Organic Study Guide §15.1 petroleum and aromatic feedstocks; syllabus §4.2.1.')
add('1-08',[
 'Cracking breaks larger hydrocarbon molecules into smaller products, including alkanes and alkenes of lower relative molecular mass.',
 'Balanced cracking equations conserve atoms while representing one possible product combination rather than a unique industrial product mixture.'
], 'Cracking changes molecules', '''Cracking breaks larger hydrocarbon molecules into smaller molecules. High temperature supplies energy, and catalytic routes use a suitable catalyst to change the available pathway. Products commonly include smaller alkanes and alkenes. Smaller fuel molecules may be more useful for transport, while alkenes are reactive feedstocks for making polymers and other chemicals. The purpose is to alter the useful product distribution, rather than merely sort the original molecules into separate containers.

One possible balanced representation is C10H22 → C6H14 + C4H8, with the C4H8 product specified as an open-chain alkene. The starting molecule has ten carbon atoms and twenty-two hydrogens; the products contain six plus four carbons and fourteen plus eight hydrogens. Both totals are conserved. Relative molecular masses using Ar(C) = 12 and Ar(H) = 1 are 142 for the starting alkane, 86 for the smaller alkane and 56 for the alkene. Each product molecule has lower Mr, while the combined product mass equals the original mass for the balanced equation.

A second possible split is C10H22 → C8H18 + C2H4. These equations are alternative illustrative outcomes, not two compulsory consecutive stages. Real cracking gives a mixture, and a balanced atom count alone cannot identify the proportions or exact structures formed. In particular, C4H8 does not specify the location of a double bond without additional structural information.

Fractional distillation is a physical separation governed by boiling behaviour; cracking is a chemical change involving covalent-bond rearrangement. Use that distinction when explaining how a refinery can obtain more small molecules than were originally present in a chosen heavy fraction. Topic 2.4 connects catalysts and temperature to rate, while addition polymerisation later in this topic explains an important use of the alkene products.''',
 'OpenStax-Chemistry','§20.1 ethene production by cracking; Organic Study Guide §7.1 thermal cracking; original balanced examples.')
add('2-01',[
 'An open-chain hydrocarbon with one carbon–carbon double bond follows CnH2n; this composition alone does not establish a double bond.',
 'An alkene drawing must preserve the location and two bond contributions of C=C when converted between representations.'
], 'Representing the carbon–carbon double bond', '''An alkene contains a carbon–carbon double bond. For an open-chain hydrocarbon with one such bond, the general composition is CnH2n, beginning with ethene, C2H4. Relative to an open-chain alkane with the same carbon count, it has two fewer hydrogen atoms because the additional carbon–carbon bond contribution uses valencies that could otherwise attach hydrogen. The C=C region gives the characteristic addition chemistry.

Structural condensed notation for propene is CH2=CHCH3. A displayed drawing expands that into individual atoms and bonds, including two lines between the first two carbons. A skeletal drawing has three carbon positions and a double line on the appropriate first segment. The end of a double line is not an extra carbon: both lines join the same pair of atoms. Molecular C3H6 states the atom count but does not locate the double bond. Empirical CH2 gives a ratio, while structural condensed, displayed and skeletal representations can preserve connectivity. These five molecular, empirical, structural condensed, displayed and skeletal forms answer different questions about the same material.

Complete valencies carefully. The terminal double-bond carbon in propene has two hydrogens; the next has one; the remaining methyl carbon has three. A four-carbon open chain with one double bond has composition C4H8 whether the bond is terminal or internal. CnH2n by itself is therefore not proof of a particular alkene structure. A saturated ring can also have that composition.

Use the representation requested and mark C=C explicitly. A single zigzag without a second bond line communicates a different hydrogen count. Topic 4.1 explains the planar geometry around an alkene carbon; Topic 4.5 will use restricted rotation about the double bond when considering spatial arrangements.''',
 '7-3-naming-alkenes','OpenStax Organic §7.3 alkene structures; Chemistry §20.1 unsaturation; original representation guidance.')
add('2-02',[
 'The alkene parent includes C=C and is numbered to give the double bond its lowest locant.',
 'But-1-ene and but-2-ene differ in double-bond position, not in total atom count.'
], 'Naming alkenes up to a six-carbon parent', '''Choose the longest suitable carbon chain containing the double bond. Use the parent stem corresponding to its carbon count and the ending –ene. Ethene and propene have no alternative double-bond position after equivalent end numbering. In a longer chain the locant specifies the lower-numbered carbon of C=C, so CH2=CHCH2CH3 is but-1-ene and CH3CH=CHCH3 is but-2-ene.

Number from the end nearer the double bond, rather than choosing numbering simply to minimise a methyl branch position. For CH3CH2CH=CHCH2CH3, numbering from either end gives hex-3-ene. For CH3CH2CH2CH=CH2, start at the terminal CH2 end to obtain pent-1-ene, not pent-4-ene. The number refers to the first carbon of the double bond, not to the number of double bonds present.

Branches are named as substituents using their positions on that numbered parent. CH2=C(CH3)CH2CH3 is 2-methylbut-1-ene. The parent contains four carbons, the methyl branch supplies a fifth, and carbon 2 has no attached hydrogen because it already has four bond contributions. Reversing the naming process provides a useful check: draw but-1-ene, attach a methyl group at carbon 2, then complete valencies.

Use the syllabus's placement of locants, such as but-2-ene. A name must communicate the double-bond position unambiguously even when different drawing orientations are used. Turning a drawing around does not create a new molecule. Conversely, moving the double bond from the end to the middle changes connectivity and therefore the name. Topic 4.5 develops isomerism in more detail; naming here supplies the language needed to distinguish the structures without introducing additional naming systems.''',
 '7-3-naming-alkenes','OpenStax Organic §7.3 numbering, including newer locant-before-ene convention adopted by NSSCAS.')
add('2-03',[
 'In an alkene atom count, a C=C bond contributes two to the four allowed bond contributions at each carbon.',
 'Both branching and double-bond position must be read from the structure before determining its atom count.'
], 'Atom counting in unsaturated structures', '''Read the complete carbon skeleton before counting hydrogen. For each neutral carbon, subtract the bond contributions already used from four: a single bond contributes one and a double bond contributes two. Add the resulting attached hydrogens over all carbons. This direct method works on structural condensed, displayed and skeletal drawings and reveals errors that can be hidden by guessing a general series relationship.

Take CH2=C(CH3)CH2CH3. The terminal alkene carbon is CH2, the other double-bond carbon has no hydrogen, its methyl branch is CH3, and the remaining chain groups are CH2 and CH3. The totals are five carbons and 2 + 0 + 3 + 2 + 3 = 10 hydrogens. Thus its molecular composition is C5H10. The open-chain, one-double-bond check also gives 2(5) = 10. Counting the parent chain alone would miss the branch and give an incorrect four-carbon answer.

For CH3CH=CHCH3, two methyl groups contribute six hydrogens and the two double-bond carbons contribute one each, giving C4H8. The same total arises for CH2=CHCH2CH3 even though the double bond is in another position. Equal composition therefore does not establish identical connectivity. The empirical ratio of either is CH2, not the complete four-carbon molecular count.

If the question requests a molecular formula, give actual atom numbers; molecular, empirical, structural condensed, displayed and skeletal forms are distinct choices. If it instead requests a structure, retain the connections and double-bond location. A useful self-check is to redraw each carbon with explicit hydrogen and verify four bond contributions. A carbon drawn with a double bond and three additional single bonds has five contributions and cannot represent the neutral alkene intended here.''',
 '7-3-naming-alkenes','OpenStax Organic §7.3 and §1.12; original detailed atom counts.')
add('2-04',[
 'Ethene and propene undergo addition of hydrogen, steam, hydrogen halides and halogens, replacing C=C by C–C.',
 'Ordinary ionic HBr addition to propene favours 2-bromopropane through the more stable secondary carbocation.',
 'The syllabus distinguishes cold dilute acidified manganate(VII) giving diols from hot concentrated acidified manganate(VII) giving oxidative cleavage.',
 'Oxidative-cleavage products reveal the groups attached to the original double-bond carbons.'
], 'A reaction map for ethene and propene', '''Addition uses the reactive C=C region to form two new bonds while retaining the carbon skeleton. With hydrogen and a heated nickel catalyst, CH2=CH2 + H2 → CH3CH3; propene similarly gives propane. This hydrogenation is reduction because the organic molecule gains hydrogen. The catalyst changes the reaction pathway and is regenerated overall. Simply mixing a cold alkene with hydrogen without a suitable catalyst does not provide the stated preparation.

Addition of steam gives an alcohol. Industrial ethene hydration uses a phosphoric-acid catalyst at elevated temperature and pressure: CH2=CH2 + H2O ⇌ CH3CH2OH. Temperature, pressure and steam proportion influence the practical rate and equilibrium yield; the double arrow represents the reversible overall process. Propene hydration favours propan-2-ol, CH3CH(OH)CH3. The reaction supplies H and OH across C=C, rather than adding a separate water molecule as a loosely bound attachment.

Hydrogen halides supply H and halogen. Ethene plus HBr gives bromoethane: CH2=CH2 + HBr → CH3CH2Br. For propene under ordinary ionic addition, CH3CH=CH2 + HBr → CH3CHBrCH3 gives the major product, 2-bromopropane. Hydrogen adds preferentially to the end already bearing more hydrogen, while bromine ends up on the central carbon. This Markovnikov orientation follows the relative stability of the intermediate cations; it is not a reason to describe both orientations as equally favoured. HCl analogously supplies H and Cl.

Bromine or chlorine adds across C=C without requiring the radical-initiating light used for alkane substitution. CH2=CH2 + Br2 → BrCH2CH2Br gives 1,2-dibromoethane; CH3CH=CH2 + Br2 → CH3CHBrCH2Br gives 1,2-dibromopropane. Bromine is consumed and its orange-brown colour disappears. The written dibromo product describes the simple addition in a suitable non-aqueous medium; water can participate in aqueous mixtures, so a colour test by itself does not prove the isolated organic product's full identity.

The syllabus specifies cold, dilute, acidified manganate(VII) for oxidation to a diol. Ethene gives ethane-1,2-diol, HOCH2CH2OH, and propene gives propane-1,2-diol, CH3CH(OH)CH2OH. An organic oxidation balance is CH2=CH2 + [O] + H2O → HOCH2CH2OH. The two adjacent carbons each gain OH and C=C becomes C–C. Purple manganate(VII) is reduced; under adequately acidic settings its reduction product is Mn2+, rather than assuming a brown precipitate for every solution. Keep the specified temperature, dilution and acidity with the predicted organic product.

Hot, concentrated, acidified manganate(VII) oxidises further and cleaves C=C. At a double-bond carbon bearing a hydrogen, the resulting carbon-containing fragment becomes a carboxylic acid; a terminal CH2 carbon is oxidised to CO2. A double-bond carbon bonded to two carbon groups and no hydrogen gives a ketone. For but-2-ene, CH3CH=CHCH3 + 4[O] → 2CH3COOH. The two identical acid fragments locate a central double bond in the known four-carbon chain. Propene gives CH3CH=CH2 + 5[O] → CH3COOH + CO2 + H2O. All three original carbons are accounted for, including the one in CO2.

Finally, many alkene molecules can join by addition polymerisation. Ethene produces poly(ethene), while propene produces poly(propene), with carbon–carbon single-bond backbones and the original substituents retained. Later sections show repeat units and reverse the process on paper to identify monomers. In a reaction map, pair each arrow with its reagent and settings. An answer naming “oxidation” without distinguishing mild addition from vigorous cleavage leaves the key product undecided.''',
 'NSSCAS-8224-SYLLABUS','§4.2.2 exact acidified manganate settings; OpenStax Organic §§7.7,8.2,8.6,8.10; Study Guide §8.8 cleavage. Syllabus governs cold-diolation wording.')
add('2-05',[
 'Heterolytic fission assigns both electrons of a covalent bond to one fragment and can form oppositely charged ions.',
 'A full-headed curved arrow starts at the bond pair and ends at the atom receiving that pair.'
], 'Heterolytic fission and charge accounting', '''Heterolytic fission is the breaking of a covalent bond with both electrons of its shared pair going to one fragment. For H–Br in the ionic addition pathway, the pair goes to bromine as the bond breaks. In an isolated charge-accounting representation this gives H+ and Br−. During reaction with an alkene, formation of the new C–H bond and H–Br cleavage are coupled; the mechanism need not first accumulate free hydrogen ions as separate gas particles.

Draw a full-headed curved arrow from the H–Br bond towards Br. The arrow begins at an electron source, which here is a bond, and ends on the atom receiving the pair. A straight reaction arrow records overall chemical change but does not tell which electrons moved. A fishhook arrow records one electron and is therefore the wrong symbol for transfer of the intact shared pair.

Charge provides an independent check. Neutral HBr has total charge zero. The formal products H+ and Br− also sum to zero. In the alkene addition step, the organic fragment becomes a positively charged carbocation while Br− carries the balancing negative charge. A drawing that shows neutral bromine and a positive carbocation after transferring both bonding electrons to bromine has lost track of an electron.

Contrast homolysis: Br–Br can split under suitable light to give two Br• radicals, each receiving one bond electron. That route uses two fishhook arrows and does not produce Br+ and Br−. Choose the fission description from the electron allocation and reaction setting, rather than from the fact that a bond has broken. Topic 4.1 introduced the terminology; the following mechanisms use it to connect the electron source, intermediate charge and final covalent product.''',
 '6-2-how-organic-reactions-occur-mechanisms','OpenStax Organic §§6.2,6.5 and7.7 heterolysis and pair arrows.')
add('2-06',[
 'In ionic HBr addition to propene, the π pair bonds to hydrogen while H–Br breaks to Br−, followed by bromide attack on the carbocation.',
 'Bromine is polarised by an approaching alkene; addition can proceed through a bridged bromonium ion followed by bromide attack.',
 'Mechanism arrows track electron pairs from a bond or lone pair to the atom or bond receiving them.'
], 'Electrophilic addition: two examples', '''An electrophile is an electron-pair acceptor. The π electron pair of C=C can form a bond to an electrophile, so the alkene acts as the electron-pair donor in the first step. A mechanism must show where that pair goes, which bond breaks, the intermediate and the final product. Naming addition without those changes does not explain the reaction.

For propene with HBr under ordinary ionic addition, start a full curved arrow at C=C and end it at H of H–Br. At the same time start another at H–Br and end it on Br. Bonding H to the terminal CH2 leaves the secondary carbocation CH3–CH+–CH3 and Br−. Next, a curved arrow starts at a bromide lone pair and ends at the positively charged carbon. A C–Br bond forms, giving CH3CHBrCH3. The bromide electron pair removes the electron deficiency; no radical dot belongs on this intermediate.

![Original HBr addition arrows and secondary carbocation](assets/8224-propene-hbr-mechanism.png)

For ethene with bromine in a suitable non-aqueous medium, the approaching electron-rich double bond polarises Br2. The nearer bromine becomes δ+ and accepts the alkene pair while the Br–Br pair moves to the farther bromine. The chemically supported intermediate is a three-membered bridged bromonium ion, in which positively charged Br bonds to both carbons, together with Br−. A bromide lone pair then attacks a carbon; the corresponding carbon–bridging-Br bond pair returns to bridging Br as the ring opens. The product is BrCH2CH2Br.

Partial charges on the approaching neutral Br2 molecule are different from the full charges on the intermediate ions. Keep those labels distinct. Both examples are electrophilic addition, but their intermediates need not be drawn as identical free carbocations. The HBr example supplies the carbocation reasoning used to explain propene's major product; the bridged bromine example explains the pair movement without teaching an unsupported free ethene-derived cation as its established intermediate.''',
 '8-2-halogenation-of-alkenes-addition-of-x2','OpenStax Organic §8.2 bromonium evidence/mechanism; §7.7 HBr carbocation route; original propene application.')
add('2-07',[
 'Alkyl groups donate electron density inductively and stabilise a neighbouring carbocation; comparable tertiary carbocations are more stable than secondary, then primary.',
 'Protonation of propene preferentially forms a secondary carbocation, explaining the major 2-bromopropane product after Br− attack.'
], 'Alkyl donation and the preferred cation', '''A carbocation has a positively charged, electron-deficient carbon. Alkyl groups can donate electron density through their bonds towards that centre: their positive inductive effect helps disperse the electron deficiency. Within the simple comparable alkyl cations considered here, increasing the number of attached alkyl groups increases stability. The order is tertiary greater than secondary greater than primary. This is a comparison of cations, not of the final haloalkanes' reaction speeds.

A primary carbocation has one carbon group attached directly to its positively charged carbon, a secondary has two and a tertiary has three. Count those attachments at the charged centre. CH3CH2+ is primary; CH3CH+CH3 is secondary; (CH3)3C+ is tertiary. The plus sign marks a full positive charge. Inductive donation does not make the species neutral and should not be drawn as the loss of a whole alkyl group from the skeleton.

Propene can be protonated in two orientations. Attaching H to the terminal carbon produces CH3CH+CH3, the secondary intermediate. Attaching H to the middle carbon would produce CH3CH2CH2+, a primary intermediate. Formation of the more stable secondary cation is favoured in ordinary ionic HBr addition. A bromide lone pair then forms a bond to the charged carbon, giving 2-bromopropane as the major product. Thus a stability explanation connects the first electron-pair movement, the cation and the observed product orientation.

In a sketch, show the two CH3 groups attached to the positive centre and label their inductive donation towards it. Use full curved arrows separately for actual pair transfer in the reaction steps; a small inductive-direction marker does not mean that an entire C–C bond pair has moved to make a new bond. Topic 4.1 supplies the distinction between electron-pair arrows and other directional annotations.''',
 '7-7-electrophilic-addition-reactions-of-alkenes','OpenStax Organic §§7.7–7.8 and Study Guide Chapter7 carbocation stability; syllabus §4.2.2 inductive explanation.')
add('2-08',[
 'Addition polymerisation joins alkene monomers without eliminating a small molecule and forms a carbon–carbon single-bond backbone.',
 'Ethene gives poly(ethene), whereas chloroethene gives PVC with its chlorine substituents retained.'
], 'Addition polymerisation conserves monomer atoms', '''A monomer is a small molecule that can join repeatedly to make a polymer, a very large molecule built from repeating structural units. In addition polymerisation of an alkene, the π contribution of C=C is used as new bonds connect monomers. The two original alkene carbons become adjacent carbons in a single-bond backbone. No small molecule such as water is eliminated in this overall addition process.

Ethene gives poly(ethene): nCH2=CH2 → [–CH2–CH2–]n. Here n is a large number of monomer molecules and repeat units, not a balancing coefficient to replace with a fixed small integer. The bracketed unit represents the repeating interior of a long chain; actual chain ends are not fully specified by that shorthand. Poly(ethene) has the same carbon-to-hydrogen ratio as its monomer, but very different molecular size and useful physical properties.

Chloroethene, CH2=CHCl, produces poly(chloroethene), commonly called PVC: nCH2=CHCl → [–CH2–CHCl–]n. Chlorine stays attached to the same carbon as a side substituent. It is not expelled as HCl in this addition equation, and it does not become a link in the main chain. The carbon–carbon double bond changes to a single bond while new links join neighbouring units.

A suitable initiator or catalyst and appropriate temperature and pressure are needed for practical polymer manufacture; different routes need different operating settings. The equation alone is an atom-accounting description, not a complete factory recipe. To check it, compare one monomer with one repeat unit: the atom types and counts should agree. Do not infer from the long polymer chain that extra hydrogen atoms have been inserted between the units. The open bonds at the bracket boundaries show precisely where the original monomer units connect.''',
 '8-10-radical-additions-to-alkenes-chain-growth-polymers','OpenStax Organic §8.10 ethene/PVC and chain growth; syllabus §4.2.2 addition characteristics.')
add('2-09',[
 'An addition-polymer repeat unit retains the monomer substituents, changes C=C to C–C and has chain-continuation bonds through its brackets.',
 'A repeat unit that retains the original backbone C=C while adding two external chain bonds violates carbon valency for the simple alkene polymer.'
], 'Building a repeat unit from a monomer', '''Start by identifying the two carbon atoms of the monomer's C=C bond. Put those two carbons in the repeat-unit backbone, replace the double bond by a single bond and draw an external single bond from each end. Keep every substituent attached to its original carbon. Place brackets around the unit so that the external bonds cross the bracket boundaries, and write n outside the brackets.

For propene, CH2=CHCH3, the result is [–CH2–CH(CH3)–]n. The methyl group is a side branch, not a third consecutive backbone carbon within this two-carbon unit. The repeat unit contains three carbon atoms altogether, matching the monomer. For chloroethene the corresponding construction is [–CH2–CHCl–]n. The original H and Cl attachments remain while the new backbone links replace the π bonding contribution.

![Original displayed PVC repeat unit, showing external bonds through brackets](assets/8224-pvc-repeat-unit.png)

Check each carbon's four bond contributions after including the links to neighbouring units. In poly(ethene), each backbone carbon has two C–H bonds and two C–C single bonds. If C=C were retained between the two carbons while each also acquired an external chain bond, those carbons would have five bond contributions. That count distinguishes a plausible polymer unit from a drawing that has merely put brackets around the unchanged monomer.

Practise expanding three units into a chain segment and then enclosing the smallest chemically appropriate repeating section again. Do not put a terminal CH3 group at each bracket edge: the unit is part of a continuing chain, not an isolated two-carbon molecule. The subscript n counts repeat units in the idealised representation. It does not instruct you to multiply the number of bonds on one carbon or to insert n hydrogens at a boundary.''',
 '8-10-radical-additions-to-alkenes-chain-growth-polymers','OpenStax Organic §8.10 polymer structure construction; original propene/valency practice; MC-8224-19 demand, not copied wording.')
add('2-10',[
 'An alkene monomer is reconstructed by identifying its two-carbon repeat backbone, removing continuation bonds and restoring C=C while retaining substituents.',
 'Several repeat units in a chain segment do not necessarily indicate several different monomer species.'
], 'Recovering a monomer from a chain segment', '''To identify an alkene monomer from a polymer, first find the repeating pattern of backbone atoms and side substituents. For the simple polymers considered here, select the two adjacent backbone carbons corresponding to one original C=C. Remove their continuation links on paper, restore a double bond between them and retain the side groups. The resulting molecule must satisfy carbon valency and reproduce the supplied repeat unit when polymerised again.

For a chain segment –CH2–CHCl–CH2–CHCl–CH2–CHCl–, the repeating two-carbon pattern is –CH2–CHCl–. Restoring C=C gives CH2=CHCl, chloroethene. Three copies of the same pattern in the drawing do not require three different monomers. For –CH2–CH(CH3)– repeated along a chain, the monomer is CH2=CHCH3, propene. The methyl side group remains attached to the second double-bond carbon.

A common wrong approach selects the bond between a backbone carbon and a methyl branch and turns that into the monomer's double bond. That changes which atoms form the main chain and fails to regenerate the original repeat pattern. Another wrong approach removes chlorine or adds hydrogen arbitrarily to obtain a familiar hydrocarbon. Substituents in the supplied unit are evidence about the starting alkene and must be preserved.

Use a forward check as the final step: convert the proposed monomer back to a repeat unit, complete the external bonds and compare the positions of side groups with the original chain. If the prompt supplies more than one distinct kind of repeat structure, assess the actual patterns rather than assuming one monomer from the mere existence of a long chain. This reverse construction is the same conservation-of-atoms reasoning used in reaction equations, applied to repeated molecular connectivity.''',
 '8-10-radical-additions-to-alkenes-chain-growth-polymers','OpenStax Organic §8.10 identifying monomers from polymer chains; original reverse constructions.')
add('2-11',[
 'Poly(alkene) carbon–carbon backbones resist ordinary biological breakdown, so discarded material can persist.',
 'Fragmentation of plastic is different from complete biological conversion of its polymer carbon into simpler products.'
], 'Why durable polymers create disposal problems', '''Poly(alkene)s such as poly(ethene) have strong carbon–carbon backbones that resist attack by the biological processes normally responsible for decomposing many natural materials. Their useful resistance to water and chemical attack also makes discarded objects persistent. Calling a material non-biodegradable in this context means that it does not readily undergo biological breakdown under the ordinary disposal settings being considered, rather than claiming that no chemical change can occur over any timescale.

A bag can lose its visible shape without its polymer carbon having been fully converted into small molecules by organisms. Sunlight, abrasion and mechanical stress can break an object into smaller fragments. Those fragments may remain plastic and can be harder to collect. The observation that a film has torn into pieces is therefore insufficient evidence that it has biodegraded completely.

Consider two discarded films examined after a stated period. One remains as a large sheet; another is fragmented. To compare biodegradation, information about actual biological conversion is needed, alongside the temperature, moisture, oxygen availability and time. Counting visible pieces alone can even make a persistent material appear to have disappeared when it has simply become too small to see easily.

Durability is not automatically undesirable during use: a water container or protective covering needs to remain serviceable. The problem arises when the required useful lifetime is much shorter than persistence after disposal. A reasoned explanation links backbone structure to resistance and then to accumulation, rather than saying just that plastics are bad. The next section considers ways of reducing the amount discarded and choosing routes suited to the material and available facilities. Topic 4.2.3 returns to carbon-containing products when polymers or fuels are burned.''',
 'OpenStax-Chemistry','§20.1 Recycling Plastics persistent polymers/recycling; syllabus §4.2.2 disposal. Biological breakdown/fragmentation distinction is an explicit semantic-review focus.')
add('2-12',[
 'Reuse, recycling, controlled energy recovery and disposal have different benefits and constraints depending on sorting, contamination and facilities.',
 'Biodegradable polymers need suitable degradation settings; that description alone does not establish rapid breakdown in all environments.'
], 'Choosing an approach to polymer waste', '''Reducing unnecessary use and reusing serviceable objects can lower the amount of polymer entering a waste stream. Mechanical recycling collects and sorts suitable material, cleans it and reprocesses it into another product. This retains material value and can reduce demand for new feedstock, but collection, contamination, mixed polymer types and the properties needed in the next product constrain the route. A recycling symbol identifies material information; it does not prove that a particular local facility accepts the object.

Controlled combustion with energy recovery uses the chemical energy in the waste. It reduces the amount of solid polymer, but produces gases and requires suitable equipment and emission control. Carbon-containing polymers produce carbon dioxide on complete combustion; chlorinated material also needs appropriate treatment of chlorine-containing products. This is not a recommendation to burn waste in an open household fire. Landfill contains material in a managed site but uses space and does not by itself solve persistence or recover the original polymer's material value.

Manufacturing biodegradable polymers can help when the object's use and its eventual collection route match the settings required for biological breakdown. Temperature, moisture, oxygen, organisms and time affect performance. A material designed for a controlled composting facility cannot simply be assumed to degrade equally fast in dry soil or seawater. Product design and disposal arrangements must be considered together.

Suppose an invented Namibian packing cooperative has clean, separately collected poly(ethene) offcuts accepted by its recycler. Recycling is a supported option because the stated sorting and acceptance barriers are already addressed. If the waste were instead a contaminated mixture, the same conclusion would need further information. Explain a choice using the given material, route and constraint. No single approach is established as best by naming it without specifying the waste stream.''',
 'OpenStax-Chemistry','§20.1 recycling discussion; syllabus §4.2.2 waste routes and biodegradable materials. Detailed route trade-offs marked for semantic verification.')
add('2-13',[
 'Water solubility describes dispersal at molecular level in water; biodegradability describes biological chemical breakdown.',
 'Development of polymers can target different useful properties, so a water-soluble material need not be biodegradable under a given disposal setting.'
], 'Biodegradable and water-soluble are different properties', '''New polymer development can target useful changes in performance during use and after disposal. A biodegradable polymer is designed to undergo chemical breakdown through biological activity under specified settings. A water-soluble polymer can dissolve in water: its chains become dispersed in the liquid rather than remaining as a separate visible solid. These descriptions refer to different processes and cannot be substituted for one another.

Dissolution does not necessarily break the covalent backbone of a polymer. A clear solution can contain dissolved polymer chains. Conversely, a material may be biologically degradable under suitable settings without dissolving rapidly in a beaker of water. Evidence about one property therefore cannot establish the other. Avoid using the disappearance of a visible film as the sole test for complete biological conversion.

For an original comparison, imagine film A dissolves in water but its recovered dissolved chains retain their original backbone. That observation supports water solubility and supplies no demonstration of biodegradation. Imagine film B undergoes measured biological breakdown in a moist, controlled composting system over a specified period. That supports degradation in that system; it does not establish the same rate on a dry roadside. The relevant test must match the claimed property and environment.

Design also involves the intended service lifetime. A water-soluble coating may be useful where removal by water is needed, while a container exposed to rain may require water resistance. A biodegradable item still needs a suitable route after use and should not be treated as permission to litter. In interpreting a product claim, ask what changed chemically, what remained dissolved, and which temperature, moisture and biological setting were used. These questions connect polymer structure to observed behaviour without assuming that a newer material solves each waste problem automatically.''',
 'NSSCAS-8224-SYLLABUS','§4.2.2 new biodegradable/water-soluble polymers; Chemistry §11.1 dissolution as distinct process; specific biodegradation evidence distinctions require semantic review.')
add('3-01',[
 'Alkane combustion releases energy overall because product bond formation releases more energy than reactant bond breaking requires.',
 'Useful fuel heating depends on energy transferred to the intended load as well as fuel quantity and combustion completeness.'
], 'Why alkanes are used as fuels', '''Combustion transfers stored chemical energy into thermal energy. Although breaking C–C, C–H and O=O bonds requires energy, forming the bonds in carbon dioxide and water releases more over the complete alkane combustion reaction. The overall change is exothermic. Ignition supplies the initial activation energy; it is not the source of the much larger continuing energy release while fuel and oxygen react.

Alkanes and alkane-rich mixtures are used for industrial heating, domestic heating or cooking, and transport. In a stove the useful transfer heats cookware and its contents. In a furnace it heats a material or process stream. In an engine part of the released energy ultimately produces mechanical work, while substantial energy is transferred elsewhere as heat. Fuel usefulness therefore involves controllable combustion and practical handling as well as the energy per unit mass.

For propane, complete hot combustion is C3H8(g) + 5O2(g) → 3CO2(g) + 4H2O(g). This accounts for all atoms; writing energy on the product side can express the qualitative release, but energy is not an additional substance to be balanced as an atom. If an enthalpy value is supplied, keep its stated water phase because condensation changes the numerical energy transfer.

An illustrative heater transfers 480 kJ usefully from 800 kJ released. Its useful fraction is 480/800 = 0.600, or 60.0 percent. The remaining 320 kJ has not vanished; it is transferred outside the intended load. This links combustion to Topic 2.1's energy accounting. More fuel burned does not ensure a proportionate increase in useful heating if oxygen supply or heat transfer becomes limiting. Topic 4.2.1 explains incomplete combustion, while the next section considers the gases associated with engines.''',
 'OpenStax-Chemistry','§5.3 combustion/energy; §20.1 fuels; original propane balance and heater example.')
add('3-02',[
 'Engines can emit carbon monoxide, nitrogen oxides and unburnt hydrocarbons; catalytic converters promote reactions reducing those pollutants.',
 'Complete oxidation of carbon-containing exhaust still produces CO2, so catalytic treatment does not eliminate its greenhouse contribution.',
 'Greenhouse gases absorb outgoing infrared radiation; increased atmospheric amounts can enhance warming.'
], 'Exhaust chemistry and the enhanced greenhouse effect', '''Oxygen shortage or incomplete mixing can leave carbon monoxide and unburnt hydrocarbons in engine exhaust. High engine temperatures also permit nitrogen and oxygen from the air to react, producing nitrogen oxides. Nitrogen in the fuel is therefore not required for this source of NO. Carbon monoxide interferes with oxygen transport in the body; nitrogen oxides and unburnt hydrocarbons contribute to harmful air pollution, including photochemical smog. These effects should be distinguished from a greenhouse-gas explanation.

A catalytic converter supplies surfaces that promote exhaust reactions at a useful rate once sufficiently warm. Carbon monoxide is oxidised: 2CO(g) + O2(g) → 2CO2(g). Unburnt hydrocarbons are oxidised to carbon dioxide and water. Nitrogen monoxide can be reduced by carbon monoxide: 2NO(g) + 2CO(g) → N2(g) + 2CO2(g). Check nitrogen, carbon and oxygen in this combined equation. The catalyst is regenerated overall rather than being a reagent consumed in that balance.

Treatment changes pollutants; it does not make carbon atoms disappear. A converter can lower CO emissions while increasing the conversion of fuel carbon into CO2. Carbon dioxide, methane and nitrous oxide contribute to the greenhouse effect by absorbing infrared radiation and interacting with Earth's outgoing energy transfer. Increasing their atmospheric amounts can enhance warming. This is distinct from explaining ozone-layer depletion.

When interpreting an exhaust comparison, identify the measured gas. A lower CO reading alone is not evidence of lower total CO2 production or lower fuel consumption. Converter effectiveness also depends on temperature and the fuel–air mixture. Topic 2.4 explains catalytic rate changes, and Topic 3.5 connects nitrogen oxides with another part of the subject's environmental chemistry.''',
 'OpenStax-Chemistry','§12.7 catalytic converters and §5 energy; syllabus §4.2.3 environmental gases. Original balanced NO/CO reaction avoids textbook nitric-oxide caption inconsistency.')
add('3-03',[
 'Infrared monitoring identifies suitable gases by characteristic absorption and uses calibrated absorption strength to estimate concentration.',
 'A concentration comparison requires controlled optical settings and allowance for overlapping bands or other absorbing gases.'
], 'Infrared monitoring of air pollutants', '''Infrared radiation is absorbed at energies corresponding to suitable molecular vibrations. Different bonds and molecular structures give characteristic patterns, so an instrument can use selected absorption regions to detect gases such as carbon monoxide and carbon dioxide. Absorption must involve a vibration that changes the molecule's electric dipole. Nitrogen and oxygen are not detected by simply assuming that each gas has a strong ordinary infrared absorption band; their homonuclear diatomic vibrations do not satisfy that requirement.

Monitoring needs more than spotting a dip in a spectrum. First select a characteristic band for the target gas. Pass infrared radiation through a known optical path containing the sample and compare with a suitable reference. Use standards of known concentration to calibrate how absorption strength changes with concentration. Under matched measurement settings, stronger absorption in the selected working range can indicate a greater concentration of that gas.

Suppose two air samples are measured using the same instrument, path length and calibration, with interference corrected. The sample with greater calibrated CO absorption contains more CO within that working range. Without matching the path length, stronger absorption could instead arise because the radiation travelled through more gas. Water vapour and other absorbing species can overlap bands, so selecting a less interfered region and checking the reference are part of obtaining a defensible result.

An infrared concentration measurement identifies and quantifies a suitable absorber; it does not by itself establish the source of that gas or whether an unspecified legal limit has been met. Report the gas, concentration unit and measurement setting. Topic 4.1 teaches interpretation of infrared bands in organic compounds. Here the same physical principle is applied to air monitoring, with calibration supplying the additional link between an absorption signal and gas concentration.''',
 'OpenStax-Chemistry','§12.6 infrared measurement discussion and molecular spectroscopy; Organic §§12.6,12.8 IR; syllabus §4.2.3 monitoring application. Calibration example original.')

# Original, parameterised drawings; paired SVG/PNG and geometry are generated together.
out=t.dir/'assets'
f=Figure('Alkane representations','Displayed ethane has six hydrogen bonds and a carbon-carbon single bond. A three-segment skeletal zigzag represents four-carbon butane.')
f.text(45,85,'Displayed ethane',23)
for x in [180,340]:
 f.text(x,220,'C',30)
 for y in [130,325]:f.text(x,y,'H',26)
 f.line([(x+10,165),(x+10,210)]);f.line([(x+10,260),(x+10,315)])
f.text(80,220,'H',26);f.text(440,220,'H',26)
f.line([(115,237),(168,237)]);f.line([(215,237),(328,237)]);f.line([(375,237),(428,237)])
f.text(520,85,'Skeletal butane',23);f.line([(520,240),(600,180),(680,240),(760,180)])
f.text(525,305,'4 carbon positions',20);f.text(525,345,'C4H10',23);f.save('8224-alkane-representations',out=out)
f=Figure('Propene + HBr: ionic addition','Full curved arrows show the double bond pair moving to hydrogen, H-Br pair to bromine, then a bromide lone pair to the secondary carbocation. Product is 2-bromopropane.')
f.text(40,95,'CH3',29);f.text(200,95,'CH',29);f.text(335,95,'CH2',29)
f.line([(111,114),(190,114)]);f.line([(252,108),(325,108)]);f.line([(252,120),(325,120)])
f.text(455,95,'H',29);f.text(555,95,'Br',29);f.line([(487,114),(540,114)])
f.text(450,67,'δ+',18);f.text(550,67,'δ−',18)
curved_arrow(f,(287,108),(465,110),(355,15));curved_arrow(f,(510,114),(565,135),(555,180))
f.text(50,220,'CH3',29);f.text(210,220,'CH+',29);f.text(370,220,'CH3',29)
f.line([(122,239),(200,239)]);f.line([(287,239),(360,239)]);f.text(580,220,':Br−',29)
curved_arrow(f,(582,234),(223,226),(360,150))
f.text(50,335,'CH3–CHBr–CH3',29);f.text(470,335,'2-bromopropane',23)
f.text(50,412,'Full arrowheads track electron pairs; ionic route without radical initiation.',18)
f.save('8224-propene-hbr-mechanism',out=out)
f=Figure('PVC repeat unit','Two backbone carbons joined by a single bond; each connects externally through brackets. First carbon bears two hydrogens, second bears hydrogen and chlorine. Subscript n outside right bracket.')
f.text(300,215,'C',32);f.text(490,215,'C',32);f.line([(334,235),(480,235)])
f.line([(160,235),(290,235)]);f.line([(525,235),(655,235)])
for x in [310,500]:
 f.text(x-9,110,'H',27);f.line([(x+5,155),(x+5,207)])
 f.line([(x+5,257),(x+5,315)])
f.text(300,330,'H',27);f.text(485,330,'Cl',27)
f.line([(250,85),(225,85),(225,385),(250,385)]);f.line([(565,85),(590,85),(590,385),(565,385)])
f.text(603,365,'n',24);f.text(50,420,'External bonds cross brackets; C=C has become C–C.',19)
f.save('8224-pvc-repeat-unit',out=out)

qa=[
('Identify the general composition of an open-chain alkane with n carbon atoms.','CnH2n+2.'),
('Draw a displayed structure of ethane and a skeletal structure of butane.','Displayed ethane: two C joined by one bond, each C bearing three explicit H atoms and their bonds. Skeletal butane: a three-segment, four-position zigzag. See assets/8224-alkane-representations.png; no extra carbon is implied by a bond line.'),
('Name CH3C(CH3)2CH2CH2CH2CH3.','2,2-dimethylhexane.'),
('Suggest the correct alkane name for CH3CH(CH3)CH2CH3.','2-methylbutane; the longest chain has four carbons and the branch receives locant 2.'),
('State how many hydrogens are attached to an alkane carbon bonded to three other carbons.','One hydrogen.'),
('Determine the molecular composition of CH3C(CH3)2CH2CH3.','C6H14: four CH3 groups, one CH2 and one carbon with no H.'),
('Describe three structural reasons for the general resistance of alkanes to polar attack.','Strong C–C/C–H bonds; little bond polarity; absence of a reactive electron-rich multiple bond or suitable electron-deficient carbon centre.'),
('Explain why ethane resists rapid bromine addition without radical-initiating light.','It lacks an electron-rich C=C pair for electrophilic addition, and its strong nearly non-polar single bonds do not supply that ionic addition pathway.'),
('Describe complete combustion and light-initiated halogen substitution of ethane.','Sufficient oxygen gives CO2 and water with energy release; suitable light enables chlorine or bromine to replace an H; the substitution produces a haloethane and a hydrogen halide.'),
('Write the balanced complete combustion equation for ethane, with hot gaseous products and state symbols.','2C2H6(g) + 7O2(g) → 4CO2(g) + 6H2O(g).'),
('Write the equation for one bromine substitution in ethane under radical-initiating light.','C2H6 + Br2 → C2H5Br + HBr; suitable radical-initiating light.'),
('Explain why prolonged ethane chlorination can give more than one substituted product.','The first chloroethane product retains C–H bonds, so further light-initiated radical substitution can replace more H atoms and produce a mixture.'),
('Describe initiation, propagation and combination termination in ethane chlorination.','Initiation forms radicals by light-induced Cl–Cl homolysis; propagation consumes a radical and makes another through hydrogen abstraction then halogen transfer; termination joins radicals without producing a radical.'),
('Explain how the ethane chlorination chain regenerates its reactive radical.','Cl• abstracts H: Cl• + C2H6 → HCl + C2H5•. The ethyl radical intermediate takes Cl from Cl2: C2H5• + Cl2 → C2H5Cl + Cl•. Single-electron movement forms the new bonds and regenerates Cl•.'),
('Draw the initiation of ethane chlorination, including single-electron arrows.','Draw Cl–Cl with two fishhook arrows from the bond, one to each Cl, with light over the reaction arrow, giving Cl• + Cl•. Each atom receives one original bond electron; dots show unpaired electrons.'),
('Describe crude oil as a source of aliphatic and aromatic hydrocarbons.','It is a mixture containing different hydrocarbon families; distillation separates boiling-range fractions; separation and further refinery reactions supply aliphatic and benzene-type aromatic feedstocks.'),
('Explain why one crude-oil fraction cannot be assumed to be a pure alkane.','A fraction groups molecules by boiling behaviour and can contain several structures, so collection of a fraction does not establish one composition or connectivity.'),
('Describe cracking and its useful products.','Larger hydrocarbons undergo bond rearrangement at high temperature, sometimes with a catalyst; smaller alkanes can serve as fuels; alkenes provide reactive chemical and polymer feedstocks.'),
('Explain why C10H22 → C6H14 + C4H8 can represent useful cracking when C4H8 is an alkene.','The atoms are conserved while each product has lower Mr; the smaller alkane is a fuel and the alkene is a reactive feedstock. This represents one possible split, not a unique product mixture.'),
('Identify the general composition of an open-chain hydrocarbon containing one C=C bond.','CnH2n; n is at least 2.'),
('Draw a displayed structure of propene.','Draw CH2=CH–CH3 with each C–H bond explicit: two H at the first carbon, one at the second and three at the third; show the double bond and complete four bond contributions per C.'),
('Name CH3CH=CHCH2CH3.','Pent-2-ene.'),
('Suggest the correct name for CH2=C(CH3)CH2CH3.','2-methylbut-1-ene.'),
('State how many hydrogen atoms an alkene carbon bears if it has a double bond and two carbon single bonds.','Zero; the carbon already has four bond contributions.'),
('Determine the molecular composition of CH2=C(CH3)CH2CH3.','C5H10.'),
('Describe three additions across ethene C=C using hydrogen, steam and bromine.','Hydrogen with heated Ni gives ethane; steam with phosphoric-acid catalyst at elevated temperature and pressure gives ethanol reversibly; Br2 in a suitable non-aqueous medium gives 1,2-dibromoethane.'),
('Write the organic equation for cold, dilute, acidified manganate(VII) oxidation of ethene to its diol, using [O].','CH2=CH2 + [O] + H2O → HOCH2CH2OH. Cold, dilute, acidified manganate(VII).'),
('Write the organic oxidation equation for propene cleavage by hot, concentrated, acidified manganate(VII), using [O].','CH3CH=CH2 + 5[O] → CH3COOH + CO2 + H2O. Hot, concentrated, acidified manganate(VII).'),
('Explain why ordinary ionic HBr addition to propene gives mainly 2-bromopropane.','Protonation favours the more stable secondary carbocation over the primary alternative; a bromide pair then bonds to its central positive carbon, giving mainly 2-bromopropane.'),
('State what happens to the bond electron pair in heterolytic fission.','Both electrons go to one of the fragments.'),
('Suggest the charge on bromine after heterolytic H–Br cleavage with the pair transferred to bromine.','Br−.'),
('Describe the stages of bromine addition to ethene in a suitable non-aqueous medium.','Ethene polarises Br2 and donates its π pair to nearer Br as Br–Br breaks to Br−; a bridged bromonium intermediate forms; bromide attack opens it to give 1,2-dibromoethane.'),
('Explain the electron-pair movements in ordinary ionic HBr addition to propene giving its major product.','The π pair forms a bond to H while H–Br transfers its pair to Br, giving CH3CH+CH3 and Br−. A bromide lone pair then forms C–Br at the positive centre, producing 2-bromopropane.'),
('Draw the full curved arrows and intermediate for ordinary ionic HBr addition to propene giving its major product.','Draw π bond→H and H–Br bond→Br, then CH3–CH+–CH3 and :Br−. Draw a bromide lone-pair arrow→positive carbon to form CH3CHBrCH3. Full arrowheads show pairs; see assets/8224-propene-hbr-mechanism.png.'),
('Describe how alkyl substitution affects the stability of comparable carbocations.','Alkyl groups donate electron density inductively towards the electron-deficient centre; more attached alkyl groups give greater stabilisation; tertiary > secondary > primary.'),
('Explain the role of the secondary carbocation in ordinary ionic HBr addition to propene.','π electrons bond to H at the terminal carbon, giving the secondary CH3CH+CH3 intermediate. Two alkyl groups stabilise it by inductive donation; bromide pair attack then produces the major 2-bromopropane product.'),
('Draw the secondary carbocation from propene protonation and indicate alkyl inductive donation.','Draw CH3–CH+–CH3, with a positive charge at the central carbon and inductive-direction labels from both methyl groups towards that centre. These labels indicate electron-density donation, not complete bond-pair transfer.'),
('State whether addition polymerisation of ethene eliminates water.','It does not eliminate water or another small molecule in the overall addition process.'),
('Suggest the polymer made by addition polymerisation of CH2=CHCl.','Poly(chloroethene), PVC, with repeat unit [–CH2–CHCl–]n.'),
('State what happens to C=C when an alkene forms its simple addition-polymer backbone.','It becomes C–C as new single bonds link monomer-derived units.'),
('Determine the addition-polymer repeat unit from CH2=CHCH3.','[–CH2–CH(CH3)–]n, with chain-continuation bonds through the brackets.'),
('Explain why [–CH2=CH2–]n is an incorrect repeat unit for poly(ethene).','It retains C=C while adding external chain bonds, giving each carbon five bond contributions. Replace C=C by C–C to obtain [–CH2–CH2–]n; two C–H plus two C–C single bonds complete four per carbon.'),
('State the monomer corresponding to [–CH2–CHCl–]n.','CH2=CHCl, chloroethene.'),
('Suggest the monomer for the repeated chain pattern –CH2–CH(CH3)–.','CH2=CHCH3, propene.'),
('State the structural reason poly(ethene) is difficult to dispose of by ordinary biodegradation.','Its strong C–C backbone resists the usual biological breakdown processes.'),
('Suggest why a plastic film breaking into visible fragments does not demonstrate complete biodegradation.','Its polymer chains may remain in smaller plastic pieces; fragmentation alone does not show biological chemical conversion.'),
('State one practical obstacle to recycling mixed polymer waste.','Different polymer types or contamination can make sorting and reprocessing difficult.'),
('Suggest a supported waste route for clean, separately collected poly(ethene) offcuts accepted by a local recycler.','Mechanical recycling into another product; the stated clean, sorted material is accepted by the available facility.'),
('State the difference between water solubility and biodegradability of a polymer.','Solubility is dissolution in water; biodegradability is biological chemical breakdown under suitable settings.'),
('Suggest what can be concluded if a film dissolves in water but its recovered chains are unchanged.','The film is water-soluble; this observation does not demonstrate biodegradation.'),
('Describe why alkane combustion is useful in a stove, furnace and engine.','Its overall energy release can heat cookware, heat an industrial process and supply energy for mechanical work; bond formation in products releases more energy than reactant bond breaking requires.'),
('Write complete propane combustion with state symbols for hot gaseous products.','C3H8(g) + 5O2(g) → 3CO2(g) + 4H2O(g).'),
('Explain why an alkane fuel can require ignition even though combustion is exothermic.','Energy is needed to overcome the activation barrier before reaction proceeds; overall product-bond formation then releases more energy than reactant-bond breaking requires.'),
('State one greenhouse gas produced by complete combustion of an alkane.','Carbon dioxide, CO2.'),
('Suggest why reduced CO after catalytic exhaust treatment does not prove reduced CO2 production.','The catalyst can oxidise CO to CO2, so lowering CO can increase conversion of exhaust carbon to CO2.'),
('State how an infrared monitor can identify a suitable gaseous pollutant.','It detects characteristic absorption bands of that gas.'),
('Explain why gas concentration cannot be inferred from absorption strength without controlled optical settings.','Absorption also depends on the optical path and interfering gases, so matched path length and an appropriate calibration are needed to relate signal to concentration.')
]
assert len(qa)==len(t.wo['item_slots']),(len(qa),len(t.wo['item_slots']))
why={8,17,19}
for slot,(q,a) in zip(t.wo['item_slots'],qa):
 num=int(slot['slot'].split('-')[-2]);st='WHY' if num in why else None
 if st:t.deviations.append({'from':slot['slot']+' MECH','to':'WHY; frozen ID, AO, Bloom, command and tariff retained','why':'This objective explains reactivity, feedstock composition or cracking usefulness, rather than requiring an electron-level intermediate mechanism.'})
 t.item(slot,q,a,subtype=st)

mc=[
('Name the one-carbon alkane.',['methane','ethane','propane','butane'],0,'Methane has one carbon; ethane, propane and butane have two, three and four respectively.'),
('Name the five-carbon straight-chain alkane.',['butane','pentane','hexane','propene'],1,'Pentane has five carbons; butane has four, hexane six, and propene is a three-carbon alkene.'),
('Name CH2=CH2.',['ethane','propene','ethene','but-1-ene'],2,'Ethene has two carbons and C=C; ethane lacks C=C, propene has three carbons, and but-1-ene has four.'),
('Name CH3CH=CHCH3.',['but-1-ene','propene','butane','but-2-ene'],3,'But-2-ene has the internal double bond; but-1-ene places it terminally, propene has three carbons and butane is saturated.'),
('Identify the name of an alkane methyl substituent.',['methyl','ethene','hydroxy','chloro'],0,'Methyl denotes –CH3; ethene names a molecule, hydroxy denotes OH and chloro denotes Cl.'),
('Identify the suffix used for a simple alkene.',['–ane','–ene','–ol','–oic acid'],1,'–ene indicates C=C; –ane, –ol and –oic acid identify alkane, alcohol and acid families.'),
('Name CH3CH(CH3)CH2CH3.',['3-methylbutane','pentane','2-methylbutane','2-methylpentane'],2,'2-methylbutane has the correct four-carbon parent and lowest locant; A numbers from the wrong end, B loses branching and D adds a parent carbon.'),
('Name CH3C(CH3)2CH2CH2CH2CH3.',['2-methylhexane','2,2-dimethylpentane','5,5-dimethylhexane','2,2-dimethylhexane'],3,'D preserves the six-carbon parent and two branches; A loses one branch, B shortens the parent and C uses higher locants.'),
('Name CH2=CHCH2CH2CH3.',['pent-1-ene','pent-4-ene','hex-1-ene','pentane'],0,'A uses five carbons and the lowest double-bond locant; B reverses numbering, C adds carbon and D omits unsaturation.'),
('Name CH2=C(CH3)CH2CH3.',['2-methylbutane','2-methylbut-1-ene','3-methylbut-3-ene','pent-1-ene'],1,'B preserves the branch and terminal C=C; A loses the double bond, C uses incorrect numbering and D loses branching.'),
('Name CH3CH2CH=CHCH2CH3.',['hex-1-ene','hex-2-ene','hex-3-ene','pent-2-ene'],2,'C locates C=C between carbons3 and4 of six; A/B move it and D changes carbon count.'),
('Name CH3CH(CH3)CH(CH3)CH3.',['2,2-dimethylbutane','2-methylpentane','3,4-dimethylbutane','2,3-dimethylbutane'],3,'D gives two methyl branches at2 and3 of a four-carbon parent; A changes branching, B changes connectivity and C does not use lowest locants.')]
q='Identify the correct option for each question (1 mark each).\n'+'\n'.join(f'{i}. {a} '+ '; '.join(f'{"ABCD"[j]} {v}' for j,v in enumerate(b)) for i,(a,b,c,d) in enumerate(mc,1))
a='\n'.join(f'{i}. Key/correct option {"ABCD"[c]}. {d} Each distractor identifies the stated naming error.' for i,(z,b,c,d) in enumerate(mc,1))
t.item(t.wo['performance_tasks'][0],q,a)
t.item(t.wo['performance_tasks'][1],'''Explain the ordinary ionic addition of HBr to propene and related alkene reactions.
(a) Write the major organic product and name it. [2]
(b) Explain the first-step pair movements and intermediate. [3]
(c) Describe the final electron-pair movement. [1]
(d) Write the organic products of hot, concentrated, acidified manganate(VII) cleavage of propene. [2]''',
'''(a) CH3CHBrCH3 [1], 2-bromopropane [1].
(b) C=C pair to H of HBr [1]; H–Br pair to Br [1]; secondary CH3CH+CH3 and Br− formed [1].
(c) Bromide lone pair to positive carbon forms C–Br [1].
(d) CH3COOH [1] and CO2, with water in the full organic oxidation balance [1]. These are creditworthy points for each stated part; total8 marks.''')
t.item(t.wo['performance_tasks'][2],'''Calculate the atom counts and Mr of CH3C(CH3)2CH2CH3, using Ar(C)=12.0 and Ar(H)=1.0. Then name this open-chain alkane and explain why it does not undergo rapid ionic bromine addition without radical-initiating light. [5]''',
'''Equation/check: CnH2n+2 with n=6 gives H14. Working: four CH3, one CH2 and one C give C6H14 [1]; Mr =6(12.0)+14(1.0)=86.0 [1]. Mr has no unit; three significant figures match the supplied atomic masses. Name: 2,2-dimethylbutane [1]. Its strong, nearly non-polar C–C/C–H bonds [1] and absence of an electron-rich C=C pair [1] explain resistance to this ionic addition pathway. Counts are exact integers; no mass conversion is needed.''')
t.deviations.extend([
 {'from':'Generic textbook mild alkene oxidation settings','to':'Cold, dilute, acidified manganate(VII), exactly as the syllabus specifies','why':'The board explicitly requires these settings; the local study guide supports vigorous cleavage but does not independently establish this exact cold-acidified endpoint. Retained as a focused semantic-verification item.'},
 {'from':'Potentially simplified free-carbocation bromine-addition account','to':'Bridged bromonium intermediate from the held OpenStax §8.2 reference','why':'This is the chemically supported intermediate; no excluded stereochemical extension is taught. Board-expected diagram depth needs independent review because mark schemes are not held.'},
 {'from':'Objective source routes treated as sufficient direct support','to':'Specific semantic-review focus for biodegradation environments, water solubility, waste routes and air-monitor calibration','why':'The syllabus requires these applications but the held chemistry text gives incomplete direct detail; claims remain unverified/nonpublishable until independent review.'}
])
t.save()
