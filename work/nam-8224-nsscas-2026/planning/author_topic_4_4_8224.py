"""Original alcohol chemistry, discrimination and solvent explanations."""
from authoring_common_8224 import Topic
from organic_visuals_8224 import Figure
t=Topic('4.4')
def add(n,claims,title,text,source,loc):t.objective('1-'+n,claims,[(title,text)],source,loc)
add('01',[
 'An alcohol has OH attached to a saturated carbon; open-chain saturated monohydric alcohols follow CnH2n+2O.',
 'Primary, secondary and tertiary alcohols have respectively one, two and three carbon groups attached to the OH-bearing carbon; methanol is treated with primary alcohols.'
], 'Representing the alcohol families', '''An alcohol has a hydroxyl group, –OH, attached to a saturated carbon. For an open-chain saturated molecule with one hydroxyl group and no other functional group, the general composition is CnH2n+2O, also written CnH2n+1OH. The hydrogen on oxygen is part of the total hydrogen count. This relationship does not apply without qualification to molecules containing rings, additional multiple bonds or several hydroxyl groups.

Structural condensed notation CH3CH2OH makes ethanol's connections clear: two carbon atoms lead to O–H. A displayed drawing must show the C–O and O–H bonds, together with each C–H bond. In skeletal notation the carbon skeleton can omit carbon-bound hydrogen, but O and its attached H must remain explicit. Molecular, empirical, structural condensed, displayed and skeletal forms answer different requests: a molecular formula gives actual counts, an empirical formula their simplest ratio, and the other forms retain connectivity.

![Original displayed ethanol with explicit O–H](assets/8224-ethanol-displayed.png)

The local environment of the carbon bearing OH distinguishes alcohol classes. CH3CH2OH is primary because that carbon has one carbon neighbour. CH3CH(OH)CH3 is secondary because it has two, while (CH3)3COH is tertiary because it has three. The oxygen has one bond to carbon and one to hydrogen in each example; classifying by oxygen's two bonds would not distinguish them.

Keep branches and OH on their specified atoms when converting representations. In the tertiary example the central carbon has no attached H: it is bonded to three methyl carbons and oxygen. Drawing an additional H there would give five single bonds. Topic 4.1 supplies representation conventions, while the classification section below connects the OH-bearing carbon's attachments to oxidation behaviour.''',
 'OpenStax-organic-17.1','OpenStax Organic §17.1 names/classes and §1.12 drawings; original representation comparisons.')
add('02',[
 'Alcohol names use a parent containing the OH-bearing carbon and a locant giving OH its lowest permitted position.',
 'Propan-1-ol and propan-2-ol differ in OH position, while branching is specified by separate substituent prefixes.'
], 'Naming the hydroxyl position', '''Choose the longest suitable chain containing the carbon attached to OH and use the ending –ol. Number from the end giving the hydroxyl group its lowest permitted locant. The one-to-six-carbon parent stems are meth-, eth-, prop-, but-, pent- and hex-. Methanol and ethanol have no distinct alternative hydroxyl position after equivalent end numbering. Longer chains can require a number: CH3CH2CH2OH is propan-1-ol and CH3CH(OH)CH3 is propan-2-ol.

The locant belongs immediately before –ol in the naming style used here. For CH3CH2CH(OH)CH3, start numbering from the end nearer OH and obtain butan-2-ol. Butan-3-ol would describe the same connections with unnecessarily high numbering. Position is read from the molecular connections, not from which end happens to be printed on the left.

Branches are included as prefixes with their own locants. (CH3)2CHCH2OH is 2-methylpropan-1-ol: a three-carbon parent includes the OH-bearing carbon, and carbon 2 has a methyl substituent. (CH3)3COH is 2-methylpropan-2-ol. Both contain four carbons altogether but differ in the OH-bearing carbon's attachments. The names distinguish those connections instead of merely announcing a total atom count.

To check a name, draw the numbered parent, attach OH at the stated carbon and add the substituents. Complete valencies last, including O–H. Reconstructing propan-2-ol gives one hydrogen on the OH-bearing carbon, whereas reconstructing 2-methylpropan-2-ol gives none there. Naming and classification thus provide useful independent checks, but neither replaces the requested drawing or molecular count when a question asks for those forms. Topic 4.2 uses related locant reasoning for carbon–carbon double bonds.''',
 'OpenStax-organic-17.1','OpenStax Organic §17.1 alcohol names; syllabus §4.4.1 parent chains through six carbons.')
add('03',[
 'An alcohol atom count includes both carbon-bound hydrogen and the hydrogen bonded to oxygen.',
 'Different primary, secondary and tertiary alcohol structures can share the same molecular composition.'
], 'Counting atoms without losing the OH hydrogen', '''Count all carbon atoms, including methyl branches, then count oxygen and hydrogen separately. Carbon has four bond contributions; neutral alcohol oxygen has two single bonds, normally one to carbon and one to hydrogen. The hydrogen in OH can be overlooked when expanding a skeletal drawing, so include it explicitly in the final total. Classifying a molecule as primary, secondary or tertiary does not change this accounting method.

For CH3CH(OH)CH2CH3, two CH3 groups supply six hydrogen atoms, the OH-bearing CH supplies one, CH2 supplies two and OH supplies one. The total is ten, giving C4H10O. For (CH3)3COH, three methyl groups supply nine hydrogens and OH supplies one; the central carbon supplies none. The result is also C4H10O. Equal composition therefore does not prove equal connectivity or equal alcohol class.

For a saturated open-chain alcohol with one OH, use CnH2n+2O as a check after reading the structure. With n=4 it predicts H10, matching both examples. This check cannot locate OH or distinguish a branched structure from an unbranched one. It is also not a replacement for reading additional functional groups if the given molecule contains them.

A molecular formula states the actual numbers, while an empirical formula gives the simplest whole-number ratio. Structural condensed, displayed and skeletal forms show connections in different detail. Molecular, empirical, structural condensed, displayed and skeletal answers are therefore not interchangeable. In ethanol the molecular count C2H6O cannot be reduced further; this coincidence does not make the two definitions identical. Topic 1.1 develops composition from mass data. Here the evidence is the supplied connectivity, and a correct answer follows from completing each atom's allowed bonding.''',
 'OpenStax-organic-17.1','OpenStax Organic §17.1 classes/structures and §1.12; original counts.')
add('04',[
 'Ethanol burns to CO2 and water, reacts with sodium to form sodium ethoxide and H2, and can undergo substitution to bromoethane.',
 'Controlled ethanol oxidation gives ethanal; further oxidation gives ethanoic acid; dehydration gives ethene.',
 'Ethanol and a carboxylic acid reversibly form an ester and water with an acid catalyst and heating.'
], 'Ethanol as a reaction hub', '''Complete combustion is CH3CH2OH(l) + 3O2(g) → 2CO2(g) + 3H2O(g) for hot gaseous water. Ethanol can therefore act as a fuel. In substitution with hydrogen bromide under suitable heated acidic settings, CH3CH2OH + HBr → CH3CH2Br + H2O. The OH-derived group is replaced by bromine; this differs from replacing the hydrogen on oxygen in the reaction with sodium.

With sodium, 2CH3CH2OH + 2Na → 2CH3CH2O−Na+ + H2. The product is sodium ethoxide and hydrogen gas. The carbon skeleton and C–O connection remain, while the O–H hydrogen is removed. The whole molecule does not become a sodium atom with an attached hydrocarbon, and OH− is not the stated organic product.

Warm acidified dichromate(VI) oxidises ethanol. Controlled oxidation with removal of volatile ethanal as it forms gives CH3CH2OH + [O] → CH3CHO + H2O. Heating under reflux with excess oxidant permits further oxidation: CH3CH2OH + 2[O] → CH3COOH + H2O. Acidified dichromate changes from orange towards green as it is reduced. Distillation removes the aldehyde; reflux returns volatile material so reaction can continue. The choice changes the intended organic endpoint.

Dehydration eliminates water to give ethene: CH3CH2OH → CH2=CH2 + H2O. Heating with concentrated sulfuric acid, around 170°C for this conventional preparation, supplies a suitable dehydration setting. Passing ethanol vapour over heated aluminium oxide is an alternative catalytic route. Merely naming dilute acid does not specify the concentrated-acid dehydration preparation. The concentration and heating distinguish the stated route from mixing ethanol with a dilute aqueous acid.

Esterification with ethanoic acid gives CH3COOH + CH3CH2OH ⇌ CH3COOCH2CH3 + H2O using an acid catalyst and heating. The ester is ethyl ethanoate. At fixed temperature, equilibrium means the reaction need not consume all starting material. Topic 4.7 develops ester structure and hydrolysis; here recognise the alcohol's role and preserve the balance in each reaction.

For a stoichiometric example, the sodium equation shows that 0.200 mol ethanol produces at most 0.100 mol hydrogen when sodium is in excess and reaction is complete. Divide the alcohol amount by two because two O–H hydrogens combine to make each H2 molecule. The ratio follows the balanced equation, not the number of carbon atoms.''',
 '17-6-reactions-of-alcohols','OpenStax Organic §§17.2,17.6,17.7; Chemistry §20.2; syllabus §4.4.1 and misconception MC-8224-16 specify school dehydration. Exact ethanol settings flagged for verification.')
add('05',[
 'Alcohol class is determined by carbon groups directly attached to the OH-bearing carbon, not by total carbons or OH count.',
 'Primary and secondary alcohols have respectively two and one hydrogens on that carbon, whereas tertiary alcohols have none; methanol is a special primary case.'
], 'Classifying the carbon carrying OH', '''Locate OH, then identify the carbon directly bonded to its oxygen. Count the carbon atoms directly attached to that carbon. One gives a primary alcohol, two a secondary alcohol and three a tertiary alcohol. This is a local count. The total length of the molecule and the number of hydrogens elsewhere in the chain do not determine the class. Methanol has no attached carbon group but is conventionally treated with primary alcohols for its oxidation behaviour.

In CH3CH2CH2CH2OH, the OH-bearing carbon is at an end and touches one other carbon, so butan-1-ol is primary. In CH3CH(OH)CH2CH3, that carbon touches two carbons, making butan-2-ol secondary. In (CH3)3COH, it touches three methyl carbons, making 2-methylpropan-2-ol tertiary. All three examples contain one OH group; “tertiary” does not mean three hydroxyl groups.

The same local count shows how much hydrogen is attached to the OH-bearing carbon. A usual primary RCH2OH has two, a secondary R2CHOH has one, and a tertiary R3COH has none. These patterns help explain the simple oxidation outcomes: forming a carbonyl by removal of the O–H hydrogen and a hydrogen on the same carbon is possible for the first two types. The tertiary type lacks that second hydrogen.

Practise circling the relevant carbon before assigning a class, particularly in branched structures. For (CH3)2CHCH2OH the branched carbon is not the OH-bearing carbon; the terminal CH2OH still makes it primary. This prevents a neighbouring branch from being mistaken for a tertiary alcohol centre. The next section applies the classification to distinguishing reactions, while Topic 4.6 develops the carbonyl products formed by oxidation.''',
 'OpenStax-organic-17.1','OpenStax Organic §17.1 primary/secondary/tertiary classes; §17.7 oxidation relationship.')
add('06',[
 'Mild oxidation converts primary alcohols to aldehydes and secondary alcohols to ketones, while tertiary alcohols resist that ordinary route.',
 'An oxidant colour change alone can separate a tertiary sample from reactive primary/secondary samples but cannot distinguish the latter two without product evidence.'
], 'Distinguishing alcohols by oxidation', '''Warm a suitable alcohol with acidified dichromate(VI) in the school oxidation comparison. Primary and secondary alcohols reduce the oxidant as they are oxidised, so an orange-to-green change supports reaction. A tertiary alcohol normally does not undergo the corresponding mild oxidation because its OH-bearing carbon lacks hydrogen. This is a statement about the specified mild route, rather than a claim that severe oxidation could not break other bonds.

A primary alcohol can give an aldehyde and then a carboxylic acid. A secondary alcohol gives a ketone. For propan-1-ol, controlled oxidation produces propanal, CH3CH2CHO; further oxidation produces propanoic acid. Propan-2-ol gives propanone, CH3COCH3. Keeping the carbon skeleton intact provides a useful check on the oxidation products. An unexpected extra carbon in a proposed product would require an additional reagent or reaction not supplied here.

Suppose samples A and B both change orange dichromate to green, while C does not under matched mild settings. This supports reactive primary or secondary structures for A and B and, among the stated alcohol candidates, a tertiary structure for C. It does not decide which of A and B is primary, because both types react. Additional identification of an aldehyde versus ketone product is required. Topic 4.6 develops the structures of those carbonyl products.

State an observation separately from a conclusion. “Orange becomes green” is observable; “it is secondary” is a structural inference that needs adequate discrimination. To compare samples, match temperature, reagent concentration and observation time. A negative result from a cold mixture or insufficient mixing cannot be treated as an equally controlled comparison. The best distinguishing reaction is one whose different outcomes separate the actual candidate structures given, rather than a memorised colour change applied without checking what it distinguishes.''',
 '17-7-oxidation-of-alcohols','OpenStax Organic §17.7 class outcomes; syllabus §4.4.1 mild oxidation discrimination; original controlled comparison.')
add('07',[
 'Warm alkaline aqueous iodine gives a yellow triiodomethane precipitate with suitable CH3CH(OH)R alcohols; ethanol also gives a positive result.',
 'A positive result identifies a compatible local arrangement rather than a unique alcohol; the precipitate is CHI3, not an iodoalkane substitution product.'
], 'The alkaline iodine test identifies a local arrangement', '''An alcohol containing CH3CH(OH)R can be oxidised under the alkaline iodine test to a methyl carbonyl arrangement and then form triiodomethane, CHI3. The positive observation is a yellow precipitate, not merely disappearance of iodine colour or a yellow solution. Triiodomethane is also called iodoform. Write its identity clearly: three iodines and one hydrogen are attached to its single carbon.

Propan-2-ol, CH3CH(OH)CH3, and butan-2-ol, CH3CH(OH)CH2CH3, have the required local arrangement and give positive results with warm alkaline aqueous iodine. Ethanol also gives the test: it is oxidised to ethanal, which has the required CH3CO– arrangement for the subsequent reaction. This special primary alcohol must not be rejected simply because the other familiar positive alcohol examples are secondary.

Pentan-3-ol, CH3CH2CH(OH)CH2CH3, is secondary but lacks a methyl group directly attached to its OH-bearing carbon, so it does not give the corresponding positive alcohol test. Likewise, primary propan-1-ol lacks the required arrangement. Thus a positive result is not a general test for alcohols or even for all secondary alcohols. Inspect the local connections around OH rather than counting methyl groups somewhere else in the molecule.

For an original discrimination, a four-carbon alcohol gives a yellow CHI3 precipitate and is known to be secondary. Butan-2-ol fits both pieces of evidence. The test alone would not have established a unique structure without those restrictions. Nor is the precipitate 2-iodobutane: the alcohol's entire chain has not simply had OH replaced by I. Topic 4.6 connects the test with carbonyl structure. Record reagent, warmth, the solid observation and its chemical identity before drawing the structural conclusion.''',
 'NSSCAS-8224-SYLLABUS','§4.4.1 CH3CH(OH) group test; 2025 examiner misconception entries16–18 for demand; Organic Study Guide §22.3 haloform basis. Alcohol-specific endpoint requires independent semantic verification.')
add('08',[
 'Alcohol OH groups participate in polar and hydrogen-bonding interactions while their hydrocarbon groups interact with less polar solutes.',
 'Solvent suitability depends on both the particular alcohol and solute; alcohol extraction of coal sulfur applies to compatible extractable compounds rather than all sulfur.'
], 'Why alcohols can act as solvents', '''An alcohol combines a polar hydroxyl group with a hydrocarbon group. Its OH can form hydrogen bonds with water and compatible solutes, while its carbon-containing part provides interactions with less polar substances. This combination allows suitable alcohols to dissolve a range of materials that would not all dissolve equally well in water alone. Dissolution is explained through favourable solute–solvent interactions, not by assuming the alcohol chemically destroys each dissolved substance.

Short-chain alcohols have a relatively large polar contribution and mix well with water. As the hydrocarbon portion becomes larger, its non-polar character becomes more influential and water solubility generally decreases within comparable alcohols. Consequently “contains OH” does not establish unlimited miscibility for an arbitrary long-chain alcohol. Both the molecule's structure and the identity of the solute need consideration.

In cosmetics, a suitable alcohol can help dissolve selected ingredients and distribute them through a formulation; volatility can also assist drying after application. This explains a solvent role and does not assert that all alcohols are appropriate for skin products. In the syllabus's coal application, an alcohol-based solvent can extract compatible soluble sulfur-containing compounds into the solvent phase. Extraction transfers those compounds for later separation. It does not mean that all forms of sulfur, including insoluble mineral material, are removed just by dissolving coal in any alcohol.

Suppose an invented materials laboratory observes that a selected sulfur-containing organic solute dissolves in its chosen alcohol but poorly in water. The supported explanation invokes the balance of polar and hydrocarbon interactions. The observation supplies no percentage removal for a whole coal sample, because that sample may contain other sulfur forms and an inaccessible solid matrix. Topic 1.3 explains hydrogen bonding; Topic 4.3 distinguishes chemical substitution from the physical separation involved here. A useful solvent claim names what is dissolved and the setting in which the solvent works.''',
 '17-2-properties-of-alcohols-and-phenols','OpenStax Organic §17.2 hydrogen bonding; Chemistry §20.2 solvent properties; syllabus §4.4.1 cosmetics/coal. Exact coal-solvent application is a focused reference-verification item.')
out=t.dir/'assets'
f=Figure('Displayed ethanol','Carbon-carbon-oxygen-hydrogen chain. First carbon has three hydrogen attachments, second has two; oxygen has C-O and O-H single bonds.')
for x in [230,410]:
 f.text(x,220,'C',31);f.text(x,100,'H',28);f.text(x,340,'H',28)
 f.line([(x+10,145),(x+10,208)]);f.line([(x+10,263),(x+10,330)])
f.text(110,220,'H',28);f.text(580,220,'O',31);f.text(720,220,'H',28)
for a,b in [(145,220),(270,400),(450,570),(620,710)]:f.line([(a,240),(b,240)])
f.text(40,420,'CH3CH2OH; the O–H hydrogen is included in C2H6O.',21);f.save('8224-ethanol-displayed',out=out)
qa=[
('Identify the general composition of an open-chain saturated monohydric alcohol.','CnH2n+2O, equivalently CnH2n+1OH.'),
('Draw displayed ethanol, including its hydroxyl hydrogen.','Draw C–C–O–H with three explicit H attachments on the first C and two on the second. Each C has four bonds and O has two. See assets/8224-ethanol-displayed.png.'),
('Name CH3CH2CH2OH.','Propan-1-ol.'),
('Suggest the correct name for CH3CH2CH(OH)CH3.','Butan-2-ol.'),
('State whether the hydroxyl hydrogen is included in an alcohol molecular atom count.','Yes; the H bonded to oxygen is part of the total.'),
('Determine the molecular composition of (CH3)3COH.','C4H10O: nine methyl hydrogens plus one O–H hydrogen.'),
('Describe ethanol reactions giving ethene, an aldehyde and an ester.','Heated concentrated sulfuric acid dehydrates it to ethene; controlled acidified-dichromate oxidation with product removal gives ethanal; heating with a carboxylic acid and an acid catalyst gives an ester reversibly at fixed temperature.'),
('Write the balanced equation for ethanol reacting with sodium.','2CH3CH2OH + 2Na → 2CH3CH2O−Na+ + H2.'),
('Write the organic equation using [O] for complete oxidation of ethanol to ethanoic acid by excess warm acidified dichromate under reflux.','CH3CH2OH + 2[O] → CH3COOH + H2O. Excess warm acidified dichromate(VI), reflux.'),
('Explain why removal of ethanal as it forms helps controlled ethanol oxidation stop at the aldehyde.','Removing the volatile aldehyde reduces its continued contact with the oxidant, limiting further oxidation to ethanoic acid.'),
('Explain why “dilute sulfuric acid” does not specify the conventional acid dehydration of ethanol to ethene.','The specified preparation uses concentrated sulfuric acid with strong heating, around170°C. Dilute aqueous acid does not provide that concentrated-acid dehydration setting; concentration and heating must accompany the named reagent.'),
('State what is counted when an alcohol is called secondary.','Two carbon groups directly attached to the OH-bearing carbon.'),
('Explain why (CH3)2CHCH2OH is primary even though its chain is branched.','The OH-bearing CH2 touches one other carbon, so the local class is primary; branching on a neighbouring carbon does not change that count.'),
('Describe the mild oxidation outcomes of primary, secondary and tertiary alcohols.','A primary alcohol can give an aldehyde then acid; a secondary alcohol gives a ketone; a tertiary alcohol resists the ordinary mild route because its OH-bearing carbon has no H.'),
('Contrast propan-1-ol and propan-2-ol under controlled oxidation with product identification.','Both reduce warm acidified dichromate from orange towards green. Propan-1-ol gives propanal under controlled product removal, while propan-2-ol gives propanone; colour change alone does not distinguish them.'),
('State the positive observation when a suitable alcohol is warmed with alkaline aqueous iodine.','A yellow precipitate of triiodomethane, CHI3.'),
('Determine which of propan-2-ol and pentan-3-ol has the alcohol arrangement giving a positive warm alkaline iodine test.','Propan-2-ol: CH3CH(OH)CH3 contains CH3CH(OH)–. Pentan-3-ol lacks the directly attached methyl group.'),
('Explain why “the solution turns yellow” is insufficient evidence of a positive warm alkaline iodine test on an alcohol.','A positive result requires a yellow solid precipitate of CHI3, so a solution colour alone does not establish the diagnostic product.'),
('Explain why the yellow solid from butan-2-ol and warm alkaline aqueous iodine is not iodobutane.','The test yields triiodomethane, CHI3, a one-carbon precipitate; it is an oxidation/cleavage test of the local arrangement rather than simple replacement of the alcohol OH by iodine on the intact chain.'),
('Describe three molecular features relevant to alcohol solvent behaviour.','Polar OH can hydrogen-bond; the hydrocarbon portion interacts with less polar solutes; the balance changes with carbon-chain size, affecting which solutes and water mixtures are compatible.'),
('Explain why an alcohol solvent can dissolve some organic ingredients that dissolve poorly in water.','Its hydrocarbon portion provides compatible interactions with less polar parts of the solute while OH supports polar/hydrogen-bond interactions; favourable combined interactions can stabilise the dissolved substance.')]
for s,(q,a) in zip(t.wo['item_slots'],qa):
 st='WHY' if s['slot'].endswith('018-MECH') else None
 t.item(s,q,a,subtype=st)
 if st:t.deviations.append({'from':s['slot']+' MECH','to':'WHY, frozen metadata retained','why':'Solvent behaviour is an intermolecular-interaction explanation, not a reaction mechanism with an intermediate.'})
mc=[
('Name CH3CH(OH)CH3.',['propan-2-ol','propan-1-ol','ethanol','propanone'],0,'A locates OH at carbon2; B moves it, C loses carbon and D changes functional group.'),
('Identify the gas formed by sodium reacting with ethanol.',['oxygen','hydrogen','carbon dioxide','ethene'],1,'Hydrogen is released from O–H; oxygen and CO2 are not products, and ethene requires dehydration.'),
('Identify the controlled primary oxidation product of ethanol.',['ethene','propanone','ethanal','methanoic acid'],2,'Ethanal retains two carbons and is the aldehyde; A is dehydration, B has the wrong carbon count/class and D loses carbon.'),
('Name CH3CH2CH2CH2OH.',['butan-2-ol','propan-1-ol','butanal','butan-1-ol'],3,'D matches terminal OH in a four-carbon chain; A changes position, B loses carbon and C changes family.'),
('Identify the appropriate conventional acid preparation for ethanol to ethene.',['concentrated sulfuric acid and strong heating','dilute acid at room temperature','aqueous hydroxide','cold hydrogen without catalyst'],0,'A supplies dehydration settings; B does not, C is not that reagent and D is not alcohol dehydration.'),
('Identify the ester from ethanol plus ethanoic acid under heated acid-catalysed esterification at fixed temperature.',['methyl propanoate','ethyl ethanoate','ethanal','sodium ethoxide'],1,'B uses the ethanol alkyl and ethanoic-acid acid portion; A changes connections, C is oxidation and D arises with sodium.')]
t.item(t.wo['performance_tasks'][0],'Identify the correct option in each question (1 mark each).\n'+'\n'.join(f'{i}. {q} '+ '; '.join(f'{"ABCD"[j]} {v}' for j,v in enumerate(opts)) for i,(q,opts,k,a) in enumerate(mc,1)),'\n'.join(f'{i}. Key/correct option {"ABCD"[k]}. {a} Each distractor represents the stated error.' for i,(q,opts,k,a) in enumerate(mc,1)))
t.item(t.wo['performance_tasks'][1],'''Explain the chemistry of CH3CH2OH.
(a) Name it and draw its displayed structure. [3]
(b) State its molecular composition. [1]
(c) Write its balanced reaction with sodium. [2]
(d) State the product and reagent settings for dehydration to an alkene. [2]''','''(a) Ethanol [1]; C–C–O–H chain [1] with three H on first carbon and two on second, all bonds explicit [1]. (b) C2H6O [1]. (c) 2CH3CH2OH + 2Na → 2CH3CH2O−Na+ + H2, correct organic/gas products [1] and coefficients [1]. (d) Ethene [1]; concentrated sulfuric acid with heating around170°C, or ethanol vapour over heated Al2O3 [1]. Creditworthy points per part, total8 marks.''')
t.item(t.wo['performance_tasks'][2],'''Calculate the maximum hydrogen amount, in mol, from 4.60 g of the saturated two-carbon monohydric alcohol reacting completely with excess sodium. Name the alcohol and give its structural condensed and molecular representations. Use Ar(C)=12.0, Ar(H)=1.0, Ar(O)=16.0. [5]''','''Ethanol, CH3CH2OH, C2H6O [1]. Equation: 2CH3CH2OH + 2Na → 2CH3CH2O−Na+ + H2 [1]. Working: Mr=2(12.0)+6(1.0)+16.0=46.0; n(ethanol)=4.60/46.0=0.100 mol [1]. Ratio2:1 gives n(H2)=0.100/2 [1]; answer0.0500 mol [1], three significant figures. Mass already g, no prefix conversion needed; hydrogen amount is not a gas volume.''')
t.deviations.append({'from':'Broad application source routes','to':'Independent source-verification focus for school ethanol preparation settings, alcohol-specific iodoform endpoint and coal-solvent example','why':'Held references support oxidation classes, hydrogen bonding and reaction families, but do not directly document every board-specific practical/application detail. Claims remain unverified and nonpublishable.'})
t.save()
