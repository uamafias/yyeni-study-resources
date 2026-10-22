"""Original foundation terminology, nomenclature, geometry and IR practice."""
import math
from authoring_common_8224 import Topic
from organic_visuals_8224 import Figure,curved_arrow,planar_ethene,tetrahedral_carbon
t=Topic('4.1')
def add(short,claims,title,text,source,loc):t.objective(short,claims,[(title,text)],source,loc)
add('1-01',[
 'A functional group is an atom or group of atoms responsible for characteristic chemical behaviour; a free radical contains an unpaired electron.',
 'Homolytic fission assigns one bond electron to each fragment; heterolytic fission assigns both to one fragment.',
 'A nucleophile donates an electron pair and an electrophile accepts one; full curved arrows show pair movement and fishhook arrows single-electron movement.',
 'Organic addition, substitution, elimination, hydrolysis, condensation and redox describe different overall changes; radical chains have initiation, propagation and termination.'
], 'Terms describe particles, electron movement and overall change', '''A functional group is an atom or group of atoms responsible for characteristic chemical behaviour, such as C=C in an alkene or –OH in an alcohol. A free radical contains an unpaired electron, shown by a dot. Homolytic fission splits a covalent bond with one electron going to each fragment; heterolytic fission sends both electrons to one fragment. Draw single-electron fishhook arrows for homolysis and a full-headed curved arrow for an electron pair in heterolysis.

A nucleophile is an electron-pair donor and an electrophile an electron-pair acceptor. A nucleophile can be neutral or negative; a lone pair or a multiple bond can supply its reactive pair. An electrophile can be positive or a suitable electron-deficient centre in a neutral molecule. Start a pair arrow at the electron source, not at a positive charge, and end it where the pair goes.

Initiation creates radicals, for example Cl2 splitting under suitable light. Propagation consumes a radical and makes another: Cl• + CH4 → HCl + CH3•, followed by CH3• + Cl2 → CH3Cl + Cl•. The methyl radical is an intermediate and chlorine radical is regenerated. Termination combines radicals without making another radical. These terms explain a chain, rather than three alternative names for its overall equation.

Addition joins species across a multiple bond without eliminating a small molecule. Substitution replaces one atom or group by another. Elimination removes groups to form a multiple bond. Hydrolysis breaks a bond through reaction with water; condensation joins species while eliminating a small molecule such as water. Organic oxidation commonly gains oxygen or loses hydrogen; reduction commonly gains hydrogen or loses oxygen, alongside the general electron/oxidation-number definitions from Topic 2.2. The symbols [O] and [H] may represent supplied oxidising and reducing equivalents, but an equation still needs atom balance.''',
 '6-2-how-organic-reactions-occur-mechanisms','OpenStax Organic §§6.2, 6.5–6.6 for fission/arrows/chains; §3.1 functional groups; syllabus §4.1.1 named overall reaction categories.')
add('1-02',[
 'Systematic names use a parent chain and functional-group ending or prefix, with locants chosen according to the required naming priority.',
 'The one-to-six carbon stems are meth-, eth-, prop-, but-, pent- and hex-; di-, tri-, tetra-, penta- and hexa- indicate repeated features.',
 'Molecular and empirical compositions differ from structural condensed, displayed and skeletal representations, which carry connection information in different ways.'
], 'Naming and representing the syllabus families', '''Choose the appropriate parent chain containing the principal functional group and number it to give that group or required prefix its lowest permitted locant. The one-to-six-carbon stems are meth-, eth-, prop-, but-, pent- and hex-. Alkanes use –ane, alkenes –ene, alcohols –ol, aldehydes –al, ketones –one, carboxylic acids –oic acid and amines –amine. Halogen substituents use fluoro-, chloro-, bromo- or iodo-. An ester has an alkyl name from the alcohol-derived part followed by an alkanoate name from the acid-derived part. Thus CH3COOCH2CH3 is ethyl ethanoate: the two-carbon group attached through oxygen supplies ethyl, while the acid-derived portion supplies ethanoate. Naming requires those connections, not just total carbon count.

Examples include hexane, but-1-ene, 1-chlorobutane, propan-2-ol, butanal, butan-2-one, pentanoic acid, ethyl ethanoate and ethanamine. The carboxyl or aldehyde carbon is part of the parent chain. Use di-, tri-, tetra-, penta- and hexa- for two through six repeated features; mono- means one but is commonly omitted where the naming convention implies it. For example, CH2ClCHClCH3 is 1,2-dichloropropane, not a name obtained by numbering from the end that gives 2,3.

A molecular formula gives actual atom numbers; an empirical formula gives their simplest ratio. Structural condensed notation such as CH3CH2OH shows grouped connections; a displayed representation shows the bonds explicitly; skeletal notation uses line ends and vertices for carbon and omits its attached hydrogens. Molecular, empirical, structural condensed, displayed and skeletal forms therefore answer different requests. Check that carbon has four bond contributions, counting a double bond twice, when moving between representations. Topic 1.1 covers composition ratios, while later organic topics apply the named functional groups.''',
 '3-4-naming-alkanes','OpenStax Organic §3.4 parent/locant principles, §3.1 family names, §1.12 representations; syllabus §4.1.1 limits chains to six carbons.')
add('2-01',[
 'Each ethane carbon has four bonding regions and tetrahedral geometry with angles approximately 109.5°.',
 'Each ethene carbon has three bonding regions and trigonal-planar geometry with angles approximately 120°; ethene is planar.',
 'The carbon–carbon double bond in ethene is shorter than the carbon–carbon single bond in ethane.'
], 'Ethane and ethene through electron-pair repulsion', '''Electron regions around a carbon centre repel and adopt an arrangement that keeps them apart. In ethane, each carbon has three C–H single bonds and one C–C single bond: four bonding regions with no carbon lone pair. The local geometry is tetrahedral and angles are approximately 109.5°. Do not draw ethane as a flat 120° carbon centre merely because a condensed composition is printed on one line.

![Generated tetrahedral carbon centre, with R = CH3 for ethane](assets/8224-ethane-centre.png)

In ethene, each carbon has two C–H bonds and one C=C double bond. The double bond counts as one region for the repulsion arrangement, although it contains two shared electron pairs between the same bonded atoms. Three regions give trigonal-planar geometry around each carbon, with angles approximately 120°. The molecule's atoms lie in one plane in this simple description.

![Generated planar ethene representation](assets/8224-ethene-planar.png)

The C=C bond is shorter and stronger than the C–C single bond in ethane. Greater shared electron density between the nuclei produces a stronger attraction and a shorter internuclear separation. Do not attribute that length difference to intermolecular attractions: the comparison is between covalent bonds inside molecules.

A displayed connectivity sketch and a three-dimensional shape sketch serve related but different purposes. For tetrahedral carbon, use a wedge towards the viewer and a hashed bond away where needed to make depth unambiguous. For ethene, show a double line and planar connections. In an explanation, count bonding regions first, state the repulsion arrangement and then give the angle. A numerical angle without that structural reasoning does not explain why the two molecules differ. Topic 1.3 established the same region-counting method for other covalent centres.''',
 'OpenStax-Chemistry','§7.6 electron-pair geometries; §7.5 bond length/strength; syllabus §4.1.2 ethane/ethene comparison, without excluded orbital mixing treatment.')
add('2-02',[
 'Related saturated carbon centres with four bonding regions are approximately tetrahedral; carbonyl and alkene carbons with three regions are approximately planar.',
 'The local geometry is determined at the named atom, so different atoms of one molecule can have different arrangements.'
], 'Applying the geometry rule to another molecule', '''Use the same electron-region count at a named atom rather than assigning one shape to an entire chain. A saturated carbon with four single bonds and no lone pair is approximately tetrahedral. Replacing one H by Cl or OH leaves four bonding regions around that carbon, so the local carbon angles remain near 109.5° in the simple prediction.

For example, the carbon of chloromethane has three C–H bonds and one C–Cl bond. A tetrahedral drawing should show all four attachments without accidentally giving carbon five bonds. In ethanol, both carbons have approximately tetrahedral arrangements, but this does not imply that oxygen also has a tetrahedral atom arrangement: its bonding pairs and lone pairs need their own count.

At a carbonyl carbon in propanone, the C=O double bond is one region and its two C–C bonds are two more. Three regions give an approximately trigonal-planar arrangement near 120°. The methyl carbons elsewhere in the same molecule still have four regions and remain approximately tetrahedral. This contrast shows why the phrase “the molecule has 120° bonds” is too broad unless the particular centre is specified.

To make a new prediction, identify the central atom, count its attached atoms and lone pairs, then select the arrangement. Multiple bonds count as one region in this method. Local substituents can cause departures from ideal angles, so use approximate values rather than claiming perfect regularity in an arbitrary molecule. The purpose is to transfer electron-pair repulsion reasoning, not to introduce a new bonding theory or memorise a separate shape for each named organic compound. Check the displayed structure after drawing: correct geometry does not excuse a missing atom or charge.''',
 'OpenStax-Chemistry','§7.6 electron-region geometry; OpenStax Organic §1.12 structural representations. Original applications to named centres.')
add('3-01',[
 'Infrared absorption involves molecular vibrations; band positions and shapes can provide evidence for functional groups.',
 'A conventional transmittance spectrum has wavenumber in cm⁻¹ horizontally and absorption dips downward; spectra can also be displayed as absorbance.',
 'A strong carbonyl-region band supports C=O, while a broad alcohol O–H band supports an O–H-containing group; multiple evidence is needed for a unique structure.'
], 'Reading an infrared spectrum', '''Infrared radiation can be absorbed when it matches a molecular vibration that interacts with that radiation. Functional groups therefore have characteristic absorption regions. Read the horizontal axis as wavenumber in cm⁻¹; a conventional IR plot runs from higher wavenumber on the left to lower on the right. On a percentage-transmittance plot, stronger absorption appears as a downward band. An absorbance plot uses the opposite visual direction, so inspect the axis label first.

Use the official Data Booklet, reproduced in syllabus Annexe E, printed page 64. Its selected reference ranges are in cm⁻¹:

| Bond / group | Range | Appearance |
|---|---|---|
| C–O: alcohol, ether, ester | 1040–1300 | strong |
| C=C: alkene | 1500–1680 | weak unless conjugated |
| C=O: amide | 1640–1690 | strong |
| C=O: ketone or aldehyde | 1670–1740 | strong |
| C=O: carboxylic acid | 1680–1730 | strong |
| C=O: ester | 1710–1750 | strong |
| C–H: alkane | 2850–2950 | strong |
| C–H: alkene | 3000–3100 | weak |
| N–H: amide or amine | 3300–3500 | weak |
| O–H: carboxylic acid | 2500–3000 | strong, very broad |
| O–H: hydrogen-bonded alcohol | 3200–3600 | strong |
| O–H: free alcohol | 3580–3650 | strong, sharp |

These ranges overlap; a band identifies supporting bond evidence rather than a unique molecule.

![Original synthetic transmittance trace with a labelled 1720 cm^-1 band and no broad O–H band](assets/8224-ir-carbonyl.png)

For this synthetic teaching trace, the strong band at 1720 cm⁻¹ supports a carbonyl group. It does not alone distinguish every aldehyde, ketone, acid and ester. Use an O–H pattern, other bands and any composition or chemical evidence to narrow the choice. The absence of an expected strong band can help rule out a candidate in a suitable clean spectrum, but a weak feature, mixture or poor-quality measurement may limit that deduction. Do not infer a full carbon skeleton from one absorption. The trace is generated for practice and is not a reproduced experimental spectrum. Its interpretation links bond evidence to the functional groups named earlier.''',
 'NSSCAS-8224-SYLLABUS','Annexe E, printed p64, characteristic infrared table; OpenStax Organic §§12.6–12.8 for interpretation principles.')

assets=t.dir/'assets';tetrahedral_carbon(assets,'8224-ethane-centre');planar_ethene(assets)
tetrahedral_carbon(assets,'8224-tetrahedral-carbon')
f=Figure('Bond fission: electron arrows','Upper row shows homolysis of a Cl–Cl bond with two single-electron fishhook arrows, one to each Cl. Lower row shows heterolysis of C–Br with a full-headed pair arrow from the bond to Br, yielding a positive carbon fragment and bromide. Schematic fission, not a claim of reaction conditions.')
f.text(30,78,'Homolysis',20);f.text(288,141,'Cl',30);f.text(502,141,'Cl',30);f.line([(333,159),(483,159)])
curved_arrow(f,(405,159),(317,130),(360,65),single=True);curved_arrow(f,(408,159),(514,130),(460,65),single=True)
f.text(605,139,'→  2Cl•',26)
f.text(30,268,'Heterolysis',20);f.text(286,320,'C',30);f.text(502,320,'Br',30);f.line([(329,338),(483,338)])
curved_arrow(f,(406,338),(512,310),(456,245));f.text(605,318,'→ C+ + Br−',25)
f.text(28,390,'Other attached groups omitted; C labels denote fragments.',16)
f.text(28,420,'Start arrows at the bond electrons. Fishhook: one; full head: a pair.',17)
f.save('8224-bond-fission',out=assets)
f=Figure('Infrared: synthetic teaching trace','Original model percentage-transmittance spectrum with decreasing wavenumber from 4000 to 500 cm^-1, a sharp strong carbonyl-like band at 1720, plus illustrative C–H and fingerprint-region bands. It is not an experimental spectrum or unique compound identification.')
f.text(25,65,'Transmittance / %',18);f.arrow((85,360),(790,360));f.arrow((85,360),(85,110));f.text(574,405,'Wavenumber / cm^-1',17)
def xy(w,trans):return (85+(4000-w)*690/3500,360-trans*2.35)
pts=[]
for w in range(4000,499,-5):
 trans=91-25*math.exp(-((w-2940)/65)**2)-72*math.exp(-((w-1720)/29)**2)-32*math.exp(-((w-1110)/40)**2)-16*math.exp(-((w-1370)/33)**2)
 pts.append(xy(w,trans))
f.line(pts,'#176e9a',3)
for w in (4000,3000,2000,1500,1000,500):
 x,_=xy(w,0);f.line([(x,360),(x,367)],width=1);f.text(x-19,374,str(w),15)
for v in (0,50,100):
 _,y=xy(0,v);f.text(37,y-9,str(v),15)
x,_=xy(1720,0);f.arrow((x+60,255),(x+3,310),'#a13922',2);f.text(x+15,228,'1720',19,'#a13922')
f.text(26,435,'Synthetic trace: use supplied reference ranges; no unique structure is implied.',16)
f.save('8224-ir-carbonyl',out=assets)
s=t.wo['item_slots']
qa=[
 ('Describe a functional group, a nucleophile and an electrophile. [3]','A functional group supplies characteristic chemical behaviour [1]; a nucleophile donates an electron pair [1]; an electrophile accepts an electron pair [1].'),
 ('Explain how the two propagation steps Cl• + CH4 → HCl + CH3• and CH3• + Cl2 → CH3Cl + Cl• sustain a radical chain, identifying the intermediate and electron feature. [2]','The first step makes the methyl-radical intermediate CH3• with an unpaired electron [1]; it forms the C–Cl product bond in the second step while a chlorine radical is regenerated, allowing another cycle [1]. These are single-electron changes, not a claim that the carbon radical has a negative charge.'),
 ('Draw electron-movement arrows for Cl–Cl homolysis and for C–Br heterolysis in which both bonding electrons go to bromine. Include the fragment charges or radical dots. [2]','Homolysis: two fishhook arrows from the bond, one towards each Cl, giving 2Cl• [1]. Heterolysis: a full-headed curved arrow from the C–Br bond to Br, giving a positive carbon fragment and Br− [1].\n\n![Generated fission model](assets/8224-bond-fission.png)'),
 ('Name CH3CH(OH)CH3 systematically. [1]','Propan-2-ol [1].'),
 ('Suggest the systematic name for CH2ClCH2CH2CH3 using the lowest permitted halogen locant. [1]','1-Chlorobutane [1].'),
 ('Identify the approximate angle at each carbon in ethene. [1]','120° [1].'),
 ('Draw ethene with its carbon–carbon double bond, planar arrangement and approximate angle at carbon. [2]','Show CH2=CH2 with the four C–H bonds and planar arrangement [1]; label approximately 120° at carbon [1].\n\n![Generated ethene model](assets/8224-ethene-planar.png)'),
 ('Identify the local geometry at the carbonyl carbon of propanone. [1]','Approximately trigonal planar [1].'),
 ('Draw the local carbon arrangement of chloromethane, showing four bonds and an appropriate three-dimensional convention. Label the approximate bond angle. [2]','Carbon has three H and one Cl arranged tetrahedrally, with wedge/hashed depth where needed [1]; angles approximately 109.5° [1].'),
 ('State what molecular feature commonly produces a strong IR band in the supplied reference range 1670–1750 cm⁻¹. [1]','A carbonyl C=O group [1].'),
 ('Determine the functional group supported by the labelled strong band in this synthetic IR spectrum. Supplied reference: strong C=O absorption 1670–1750 cm⁻¹. [1]\n\n![Original synthetic spectrum](assets/8224-ir-carbonyl.png)','A carbonyl C=O group [1], supported by the labelled 1720 cm⁻¹ absorption. This alone does not uniquely identify the molecule.')
]
assert len(qa)==len(s)
for slot,(prompt,answer) in zip(s,qa):t.item(slot,prompt,answer)
p=t.wo['performance_tasks']
t.item(p[0],'''Identify one correct option per question. [5]
1. A nucleophile is an electron-pair: A donor; B acceptor; C destroyer; D neutron source.
2. CH3CH(OH)CH3 is: A propanal; B propan-2-ol; C propanoic acid; D ethanamine.
3. A carbon centre in ethane is approximately: A linear 180°; B square 90°; C tetrahedral 109.5°; D planar 120°.
4. The carbonyl carbon of propanone has: A four single-bond regions; B a lone pair giving bent shape; C tetrahedral 109.5° geometry; D three regions giving approximately planar 120° geometry.
5. Homolytic Cl–Cl fission forms: A two Cl• radicals; B Cl+ and Cl−; C two protons; D a carbonyl.''',
 '''Key: 1 A, 2 B, 3 C, 4 D, 5 A. One mark per correct option.
1. A is the donor definition. Distractor B describes an electrophile; C violates electron conservation; D concerns nuclear particles.
2. B has three carbons and OH at carbon 2. A is an aldehyde; C is an acid; D has nitrogen instead of oxygen.
3. C follows four regions. A uses two regions; B is not this carbon geometry; D describes a three-region centre.
4. D counts the double bond as one region. A miscounts bond order as extra directions; B invents a carbon lone pair; C uses the saturated-carbon rule.
5. A gives one electron to each fragment. B is heterolysis; C changes particle identity; D introduces carbon and oxygen absent from the bond.''')
t.item(p[1],'''Explain the following structures and terms. [8]
(a) Define a nucleophile and an electrophile by electron-pair roles. [2]
(b) Name CH3CH2OH and CH3COCH3. [2]
(c) Explain the local carbon geometry in ethane using bonding regions and repulsion. [2]
(d) Identify the geometry and approximate angle at the carbonyl carbon in propanone. [2]''',
 '''Part (a): nucleophile is an electron-pair donor [1]; electrophile an electron-pair acceptor [1].
Part (b): ethanol [1]; propanone [1].
Part (c): four bonding regions around each carbon repel [1] into an approximately tetrahedral arrangement, with 109.5° angles [1].
Part (d): approximately trigonal planar [1], 120° [1]. Each bracket is a separate creditworthy point.''')
t.item(p[2],'''Calculate and interpret the following original addition example. A 0.0500 mol ethene sample, CH2=CH2, undergoes complete addition of one mole HBr per mole ethene to give CH3CH2Br. [5]
(a) Calculate moles of HBr required. [1]
(b) Calculate moles of product and its mass using product molar mass 109 g mol⁻¹. Give three significant figures. [1]
(c) Name the product. [1]
(d) State the approximate local carbon angle in ethene and in the saturated product. [2]''',
 '''(a) Equation CH2=CH2 + HBr → CH3CH2Br; the 1:1 relationship gives 0.0500 mol HBr [1].
(b) Product is 0.0500 mol; working mass = nM = 0.0500 × 109 = 5.45 g to three significant figures [1]. No conversion is required because the molar mass is in g mol⁻¹.
(c) Bromoethane [1].
(d) Ethene approximately 120° [1]; saturated product carbons approximately 109.5° [1]. The overall addition changes local bonding-region counts.''')
t.deviations.append({'from':'Earlier authoring note incorrectly described the official IR table as absent','to':'Official syllabus Annexe E p64 reference ranges reproduced in original teaching layout; synthetic practice retained','why':'The full official Data Booklet is embedded in the held syllabus. Table located and read during final practical preparation; prior source-gap note corrected.'})
t.deviations.append({'from':'Broad terminology objective with only three slots','to':'Teach every named term; use the slots for definitions, a genuine radical-chain explanation and electron-arrow construction','why':'This preserves the planned count while keeping detailed reaction-specific practice for the subsequent organic topics.'})
t.save()
