"""Original carbonyl representations, naming and preparation."""
from authoring_common_8224 import Topic
from organic_visuals_8224 import Figure
t=Topic('4.6')
def add(n,claims,title,text,source,loc):t.objective('1-'+n,claims,[(title,text)],source,loc)
add('01',[
 'An aldehyde carbonyl carbon has an H attachment, whereas a ketone carbonyl carbon has two carbon attachments.',
 'Open-chain saturated aldehydes and ketones with one carbonyl and no other functional group follow CnH2nO, but that composition alone does not distinguish them.'
], 'Aldehyde and ketone connections', '''A carbonyl group is C=O. In an aldehyde its carbon has at least one attached hydrogen, giving the group –CHO at the end of an open chain. In a ketone the carbonyl carbon is attached to two carbon groups, giving –CO– within a carbon skeleton. Methanal, HCHO, is the simplest aldehyde and has two H attached to the carbonyl carbon; a ketone needs at least three carbons to provide its two carbon attachments.

For saturated open-chain molecules containing one carbonyl and no other functional group, the general composition is CnH2nO. Propanal, CH3CH2CHO, and propanone, CH3COCH3, both have C3H6O. The count therefore does not decide whether the compound is an aldehyde or ketone. Connectivity supplies that distinction.

Molecular, empirical, structural condensed, displayed and skeletal forms describe different information. A molecular formula gives actual counts and an empirical formula their simplest ratio. Structural condensed notation retains grouped connections; a displayed drawing shows each bond; skeletal notation omits carbon labels and their hydrogen while retaining the oxygen and C=O double line. In condensed –CHO, the H is attached to carbon, not to oxygen. Do not read CHO as an alcohol OH group.

![Original aldehyde and ketone carbonyl connections](assets/8224-carbonyl-connections.png)

Each carbonyl carbon has four bond contributions: two to oxygen and two single-bond attachments. The oxygen has its double bond and no implied O–H hydrogen. Check these details when expanding a skeletal representation. Topic 4.1 explains planar geometry at a carbonyl carbon and infrared carbonyl absorption; Topic 4.4 distinguishes the alcohol C–OH arrangement from the oxidised C=O arrangement.''',
 '19-1-naming-aldehydes-and-ketones','OpenStax Organic §19.1 carbonyl names/structures; Chemistry §20.3; original representation comparisons.')
add('02',[
 'An aldehyde parent includes its CHO carbon as carbon1 and uses –al.',
 'A ketone parent includes the carbonyl carbon and uses a lowest-permitted carbonyl locant before –one.'
], 'Names include the carbonyl carbon', '''Aldehydes use the ending –al. Select a parent chain containing the CHO carbon and include that carbon in the chain count. It is carbon 1, so CH3CH2CHO is propanal, not ethanal with an extra unnamed group. The one-to-six-carbon straight-chain aldehydes are methanal, ethanal, propanal, butanal, pentanal and hexanal. Branch locants are counted from the aldehyde end.

For example, CH3CH(CH3)CHO is 2-methylpropanal. Its parent has three carbons including CHO, while the methyl substituent adds a fourth to the whole molecule. Reconstructing the name gives the same carbon skeleton and ensures that an H remains attached to the carbonyl carbon. Merely naming the longest chain anywhere in a branched drawing can be wrong if that route omits the aldehyde group.

Ketones use –one and number the parent from the end giving the carbonyl carbon its lowest permitted locant. CH3COCH2CH2CH3 is pentan-2-one. CH3CH2COCH2CH3 is pentan-3-one. Both parents contain five carbons; the number identifies which carbon bears =O. In propanone there is one possible internal carbonyl position, so its usual simple name needs no locant.

To reverse a ketone name, draw the complete parent carbon chain first, number it and add a double bond to oxygen at the named carbon. Then fill the remaining carbon valencies with hydrogen. A terminal carbon bearing =O and H would instead give an aldehyde structure. Naming is therefore tied to connections, rather than a choice of ending based solely on a total atom count. Topic 4.5 uses this difference when identifying functional-group structural isomers.''',
 '19-1-naming-aldehydes-and-ketones','OpenStax Organic §19.1 parent choice, carbon1 and modern locant placement; syllabus §4.6.1 through six-carbon parent.')
add('03',[
 'Hydrogen counting in carbonyl compounds gives two bond contributions to C=O at carbon and does not add an O–H hydrogen.',
 'Aldehyde/ketone structural isomers may have the same molecular count despite different carbonyl positions and attachments.'
], 'Composition from a carbonyl drawing', '''Count the carbonyl carbon as part of the carbon skeleton, then complete valencies at each carbon. Its double bond to O uses two contributions. In an aldehyde, one remaining contribution can be C–H and the other C–C; in a ketone both remaining contributions are C–C. Oxygen does not carry an implicit hydrogen in C=O. This is a common difference from the alcohol structures used earlier.

For CH3CH2CH2CHO, the hydrogen total is 3 + 2 + 2 + 1 = 8, so butanal has C4H8O. For CH3COCH2CH3, the methyl groups supply six H, CH2 supplies two and the carbonyl carbon none, again giving C4H8O. Thus the same count can belong to an aldehyde or a ketone. The molecular composition does not establish the name or structure without further evidence.

In a skeletal drawing, a line to an explicit oxygen label is not an extra carbon position. The two lines of C=O represent a double bond between one carbon and one oxygen, not two oxygen atoms. Counting line strokes instead of labelled atoms and carbon positions would therefore give an impossible composition.

Use the saturated open-chain CnH2nO relationship as a check after the direct count. Molecular, empirical, structural condensed, displayed and skeletal forms are separate answers: a molecular formula gives actual counts, an empirical formula a ratio, and the connection representations show where atoms attach. Topic 1.1 covers calculating relative molecular mass from those counts. Here a calculated Mr can confirm arithmetic but cannot distinguish two isomers with equal composition.''',
 '19-1-naming-aldehydes-and-ketones','OpenStax Organic §19.1 structures and Chemistry §20.3; original valency counts.')
add('04',[
 'Acidified dichromate(VI) oxidises a primary alcohol to an aldehyde, which can oxidise further, while a secondary alcohol yields a ketone.',
 'Controlled oxidation and removal of an aldehyde limit further reaction; excess oxidant with reflux favours continued primary-alcohol oxidation to acid.'
], 'Preparing carbonyls from alcohols', '''Use acidified dichromate(VI), Cr2O7²−/H+, to oxidise primary and secondary alcohols. Ethanol gives ethanal in controlled oxidation: CH3CH2OH + [O] → CH3CHO + H2O. The primary alcohol loses hydrogen from OH and from the same carbon to form C=O. Further oxidation can produce ethanoic acid, so limiting the intended stage and removing the volatile aldehyde as it forms helps obtain the aldehyde product.

A secondary alcohol instead gives a ketone. Propan-2-ol gives propanone: CH3CH(OH)CH3 + [O] → CH3COCH3 + H2O. Its OH-bearing carbon has one H available for removal and two carbon attachments. The product retains those two attachments at the carbonyl carbon. Oxidation of butan-2-ol similarly gives butan-2-one, preserving four carbons and the carbonyl position corresponding to the original OH-bearing carbon.

The oxidant's orange colour changes towards green as dichromate(VI) is reduced. That observation supports oxidation but does not on its own identify which carbonyl formed, since both primary and secondary alcohols can react. Use the starting alcohol's connections and product structure as well. A tertiary alcohol lacks H on its OH-bearing carbon and resists this ordinary mild carbonyl-forming route.

For a worked amount calculation, 0.100 mol propan-2-ol can give at most 0.100 mol propanone if oxidation is complete: the organic ratio is 1:1. Mr(propanone)=3(12.0)+6(1.0)+16.0=58.0, so the corresponding mass is 5.80 g. Actual isolated yield can be lower through incomplete reaction or loss during separation; neither changes the stoichiometric maximum calculated from the balanced equation. Topic 4.4 teaches the alcohol reaction map, and Topic 4.7 develops the carboxylic-acid endpoint of further primary oxidation.''',
 '17-7-oxidation-of-alcohols','OpenStax Organic §17.7 primary/secondary oxidation and chromium reagents; syllabus §4.6.1 specific acidified dichromate preparation.')
out=t.dir/'assets'
f=Figure('Aldehyde and ketone carbonyl connections','Ethanal has carbonyl C attached to H and methyl; propanone has carbonyl C attached to two methyl groups. Condensed methyl groups are explicit abbreviations.')
for ox,label,right in [(0,'Ethanal','H'),(420,'Propanone','CH3')]:
 f.text(ox+45,90,label,24);f.text(ox+40,230,'CH3',25);f.text(ox+190,230,'C',28);f.text(ox+305,230,right,25);f.text(ox+190,125,'O',28)
 f.line([(ox+110,248),(ox+180,248)]);f.line([(ox+225,248),(ox+293,248)])
 f.line([(ox+197,172),(ox+197,220)]);f.line([(ox+209,172),(ox+209,220)])
f.text(28,410,'C=O carbon has four bond contributions; CH3 groups are condensed.',18);f.save('8224-carbonyl-connections',out=out)
qa=[
('Identify the group distinguishing an aldehyde from a ketone.','An aldehyde has at least one H attached to its C=O carbon; a ketone has two carbon groups attached there.'),
('Draw displayed ethanal, showing the aldehyde hydrogen.','Draw CH3–C(=O)–H with all three methyl C–H bonds explicit, a C–C single bond, C=O double bond and carbonyl C–H single bond. Oxygen has no O–H bond.'),
('Name CH3COCH2CH2CH3.','Pentan-2-one.'),
('Suggest the correct name for CH3CH2CH2CHO.','Butanal; include the CHO carbon in the four-carbon parent.'),
('State the general composition for saturated open-chain aldehydes and ketones with one carbonyl and no other functional group.','CnH2nO.'),
('Determine the molecular composition of CH3CH2COCH2CH3.','C5H10O.'),
('State the reagent used to oxidise a primary or secondary alcohol to a carbonyl in the stated syllabus preparation.','Acidified dichromate(VI), Cr2O7²−/H+, with suitable warming.'),
('Suggest how to limit further oxidation when preparing ethanal from ethanol with acidified dichromate(VI).','Use controlled oxidation and distil off volatile ethanal as it forms, reducing its continued exposure to the oxidant.')]
for s,(q,a) in zip(t.wo['item_slots'],qa):t.item(s,q,a)
mc=[
('Name CH3CH2CHO.',['propanal','propanone','ethanal','propan-1-ol'],0,'A includes the aldehyde carbon; B changes attachments, C misses a carbon and D changes C=O to C–OH.'),
('Identify the molecular count of CH3COCH3.',['C3H8O','C3H6O','C2H4O','C3H6O2'],1,'B counts two CH3 and one carbonyl C/O; A adds two H, C omits carbon and D adds oxygen.'),
('Identify the carbonyl structure of a ketone.',['CH3CH2OH','CH3CHO','CH3COCH3','CH3COOH'],2,'C has two carbon attachments at C=O; A is alcohol, B aldehyde and D acid.'),
('Identify the product of controlled propan-2-ol oxidation with warm acidified dichromate(VI).',['propanal','ethanal','propane','propanone'],3,'D is the matching ketone; A changes carbonyl position, B loses carbon and C removes oxygen.')]
t.item(t.wo['performance_tasks'][0],'Identify the correct option in each question (1 mark each).\n'+'\n'.join(f'{i}. {q} '+ '; '.join(f'{"ABCD"[j]} {v}' for j,v in enumerate(opts)) for i,(q,opts,k,a) in enumerate(mc,1)),'\n'.join(f'{i}. Key/correct option {"ABCD"[k]}. {a} Each distractor represents the stated error.' for i,(q,opts,k,a) in enumerate(mc,1)))
t.item(t.wo['performance_tasks'][1],'''Explain preparation of a carbonyl from CH3CH(OH)CH2CH3.
(a) State the oxidant and organic product name. [2]
(b) Draw its structural condensed product, including C=O, and give molecular composition. [2]
(c) Write the organic oxidation equation using [O]. [2]
(d) Explain why this product is a ketone rather than an aldehyde. [2]''','''(a) Warm acidified dichromate(VI) [1], butan-2-one [1]. (b) CH3C(=O)CH2CH3 [1], C4H8O [1]. (c) CH3CH(OH)CH2CH3 + [O] → CH3COCH2CH3 + H2O, organic change [1], balance [1]. (d) The OH-bearing carbon started with two carbon attachments [1]; these remain at C=O, with no carbonyl H, giving a ketone [1]. Creditworthy points per part, total8 marks.''')
t.item(t.wo['performance_tasks'][2],'''Calculate the maximum mass of carbonyl product from complete oxidation of 3.00 g propan-2-ol with warm acidified dichromate(VI). Name and represent the product, and give its molecular composition. Mr(propan-2-ol)=60.0; Ar(C)=12.0, Ar(H)=1.0, Ar(O)=16.0. [5]''','''Propanone, CH3C(=O)CH3, C3H6O [1]. Equation: CH3CH(OH)CH3 + [O] → CH3COCH3 + H2O [1]. Working: n(alcohol)=3.00/60.0=0.0500 mol [1]; ratio1:1 gives0.0500 mol product and Mr=58.0 [1]; m=0.0500×58.0=2.90 g [1]. Answer to three significant figures; masses already g so no prefix conversion needed. This is a theoretical maximum, not an observed isolated yield.''')
t.save()
