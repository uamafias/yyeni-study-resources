"""Original isomer enumeration and generated spatial representations."""
from authoring_common_8224 import Topic
from organic_visuals_8224 import Figure
t=Topic('4.5')
def add(n,claims,title,text,source,loc):t.objective('-'+n,claims,[(title,text)],source,loc)
add('01',[
 'Isomer enumeration must preserve the given molecular composition while excluding drawings that differ merely by orientation or single-bond rotation.',
 'The open-chain alkene connectivities for C4H8 are but-1-ene, but-2-ene and 2-methylpropene; cis/trans but-2-ene increases the number of distinct spatial forms to four.'
], 'Enumerating structures systematically', '''Begin with the molecular composition and any class restriction in the question. The same atom count can sometimes describe several families, so “all isomers” needs the stated scope. A molecular formula gives actual counts, an empirical formula their simplest ratio; structural condensed, displayed and skeletal forms reveal connectivity. Keep these molecular, empirical, structural condensed, displayed and skeletal representations distinct while checking that a proposed drawing has the required atom count.

For C4H10 as an open-chain alkane, arrange four carbons first in an unbranched route and then in a branched skeleton. The distinct possibilities are butane, CH3CH2CH2CH3, and 2-methylpropane, (CH3)3CH. Fill hydrogens to valency four. Drawing butane in a different zigzag or reversing its left-to-right order does not create another connectivity. The two names make it easier to detect duplicate drawings.

For C4H8 restricted to open-chain alkenes with one double bond, use an unbranched four-carbon skeleton and move C=C between inequivalent positions. This gives but-1-ene, CH2=CHCH2CH3, and but-2-ene, CH3CH=CHCH3. Putting the bond at the opposite terminal end repeats but-1-ene. A branched skeleton supplies 2-methylpropene, CH2=C(CH3)2. These are three structural connectivities. Saturated rings are outside this particular question's stated open-chain restriction, rather than being impossible with C4H8.

Now inspect each connectivity for spatial alternatives. But-2-ene has cis and trans forms; the other two have a double-bond carbon with identical attachments and do not give this pair. Thus there are four distinct alkene forms when those two are counted separately. Record whether your total counts connectivities or includes stereoisomers. Check atom numbers, valencies, parent names and duplication at each stage. Topic 4.2 provides naming and composition tools; the later sections here explain the spatial test used in this enumeration.''',
 '3-2-alkanes-and-alkane-isomers','OpenStax Organic §3.2 structural enumeration and §7.4 cis/trans; original complete restricted C4 examples.')
add('02',[
 'Structural isomers share molecular composition but differ in connectivity; chain, positional and functional-group isomerism describe different connectivity changes.',
 'A rotated or reversed drawing with unchanged connections is not a distinct structural isomer.'
], 'Three kinds of structural isomerism', '''Structural isomers have the same molecular composition but a different arrangement of connections between atoms. Chain isomerism changes the carbon skeleton. Butane and 2-methylpropane both contain four carbons and ten hydrogens, but the first has an unbranched route and the second a carbon attached to three methyl groups. Their difference is not merely that one drawing looks straighter on a page.

Positional isomerism keeps the basic carbon skeleton and functional-group type but changes the position of a group or multiple bond. Propan-1-ol and propan-2-ol both have three-carbon chains and one OH, but OH is attached at an end in one and at the middle carbon in the other. But-1-ene and but-2-ene supply the corresponding double-bond example. Both members of each pair have matching total atom counts.

Functional-group isomerism changes the functional group while retaining total composition. Ethanol, CH3CH2OH, and methoxymethane, CH3OCH3, both have C2H6O. One has an O–H bond as an alcohol; the other has C–O–C connectivity as an ether. This example identifies a family difference; it does not require learning an extra ether reaction scheme. The oxygen's position among the connections supplies the distinguishing evidence.

To assign a type, compare the carbon skeleton, then the functional group and its position. A change in the way a molecule is oriented in space without changing which atoms bond belongs to another comparison. Turning a sheet upside down or rotating a flexible single bond can produce a different-looking sketch of the same compound. Name both drawings and trace each atom's neighbours before counting them separately. A matching molecular atom count is necessary for an isomer pair, but is insufficient: two identical drawings after reorientation also have matching counts. Topic 4.1's functional-group vocabulary helps identify what has actually changed.''',
 '3-2-alkanes-and-alkane-isomers','OpenStax Organic §3.2 constitutional/structural isomer categories and examples; syllabus §4.5 terminology.')
add('03',[
 'Stereoisomers share connectivity but differ in spatial arrangement; the syllabus covers geometrical cis/trans and optical isomerism.',
 'Enantiomers are non-superimposable mirror-image stereoisomers; simple cis/trans alkene pairs need not be mirror images.'
], 'Same connections, different arrangement in space', '''Stereoisomers have the same structural connections but a different arrangement of atoms in space. They also have the same molecular composition. The two divisions used here are geometrical, or cis–trans, isomerism and optical isomerism. A spatial difference must survive attempts to rotate the entire molecule into coincidence; a different viewing angle is not by itself a new stereoisomer.

In but-2-ene the two methyl groups can lie on the same side of C=C or opposite sides. Both structures have the same sequence CH3–CH=CH–CH3. Nothing has been moved from one carbon to another, so this is not positional isomerism. They differ in the arrangement held by the double bond: cis has the methyl groups on the same side and trans has them on opposite sides.

![Original cis and trans but-2-ene drawings](assets/8224-cis-trans-butene.png)

Optical isomers in the simple one-centre examples are a pair of non-superimposable mirror images, called enantiomers. A tetrahedral carbon attached to four different groups provides a common source. A pure member can rotate the plane of plane-polarised light; the corresponding pure mirror form rotates it equally in the opposite direction under matched settings. Equal amounts of the two can cancel the net rotation. This cancellation concerns the sample, not disappearance of the chiral centres in its molecules.

The diagnostic questions differ. For cis–trans, inspect C=C and compare attachments at each end. For the optical examples, inspect a tetrahedral centre and compare its four groups. Do not label any two differently drawn molecules “optical” merely because they have the same counts. Likewise, a cis–trans pair is not automatically a mirror-image pair. The following sections develop the restricted-rotation and four-different-groups tests without adding a new stereochemical naming system.''',
 '7-4-cis-trans-isomerism-in-alkenes','OpenStax Organic §7.4 geometrical pairs; §§5.1,5.3 enantiomers and rotation; syllabus §4.5 restricted scope.')
add('04',[
 'Cis/trans alkene alternatives require restricted C=C rotation and two different groups at each double-bond carbon in the examples used here.',
 'Ordinary rotation about a single bond does not interconvert cis/trans alkene structures while preserving an intact double bond.'
], 'Restricted rotation makes cis and trans distinct', '''A carbon–carbon double bond prevents the free rotation characteristic of a simple carbon–carbon single bond. Twisting the two alkene ends relative to one another would disrupt the π bonding interaction and requires a substantial energy input. Under ordinary settings the cis and trans structures therefore remain distinct rather than continuously exchanging through easy rotation about intact C=C.

Restriction alone is not enough to give two distinguishable forms. Each double-bond carbon must have two different attached groups. But-2-ene meets that test: each carbon has H and CH3. The methyl groups can be on the same side, cis, or opposite sides, trans. In propene, one double-bond carbon has two H atoms. Interchanging those identical hydrogens gives the same arrangement, so propene does not form a cis/trans pair. Likewise CH2=C(CH3)2 fails the test at its CH2 end and at its two-methyl end.

When drawing the but-2-ene pair, put C=C horizontally, give each carbon one H and one CH3, and keep three bonding directions around each alkene carbon. In the cis drawing both methyl labels are above, or both below, the double bond. In trans one is above and the other below. Reversing the entire drawing does not convert cis to trans, because the same-side or opposite-side relationship is unchanged.

Avoid saying simply that cis–trans is caused by molecules being unable to move. Molecules can translate, rotate as whole objects and rotate around other bonds; the relevant constraint is relative rotation about the double bond. That is why a freely rotating butane sketch does not supply an analogous isolable pair just by showing its methyl groups in two positions on paper. Topic 4.1 describes local planar alkene geometry, and Topic 4.2 supplies the names used to identify which bond is under discussion.''',
 '7-4-cis-trans-isomerism-in-alkenes','OpenStax Organic §7.4 restricted rotation and identical-group test; no excluded orbital-mixing treatment.')
add('05',[
 'A chiral centre in the simple carbon examples is a tetrahedral carbon bonded to four different groups.',
 'One such centre normally gives two non-superimposable mirror arrangements; molecules may contain multiple chiral centres without requiring an advanced classification here.'
], 'A tetrahedral centre with four different groups', '''A chiral centre in the carbon examples taught here is a tetrahedral carbon attached to four different groups. The groups need not begin with four different elements: two can both begin with carbon but differ farther along their connections. For butan-2-ol, the OH-bearing carbon has H, OH, CH3 and CH2CH3. These are four different groups, making that carbon a chiral centre.

Its mirror image has the same atom connections but cannot be placed on the original so that all four groups coincide by rotating the whole molecule. A simple pair of such non-superimposable mirror images gives optical isomerism. A wedge represents a bond towards the viewer, a hashed bond one away, and ordinary lines bonds in the page. A flat four-arm cross without a depth convention does not demonstrate the tetrahedral mirror relationship adequately.

![Original mirror-image butan-2-ol centres](assets/8224-optical-mirror-pair.png)

Propan-2-ol does not have this centre because its OH-bearing carbon has two identical methyl groups. A CH2 carbon also has two identical H atoms. Neither becomes chiral simply because the other two groups look different. In a candidate with a longer branch, trace each attached group far enough to decide whether it is genuinely different. The plus or minus sign for measured light rotation cannot be assigned from a wedge drawing by guessing which group lies to the right.

Some molecules contain more than one chiral centre. Identify each candidate locally by its four attachments, but do not assume that the count of centres alone completely describes the whole molecule's optical behaviour. The syllabus does not require a fuller multi-centre classification. The essential transfer here is to inspect actual connections and show depth correctly in a one-centre pair. Topic 4.4 supplies the alcohol structures used in these examples; the centre remains a geometric property rather than a separate alcohol reaction.''',
 '5-1-enantiomers-and-the-tetrahedral-carbon','OpenStax Organic §5.1 mirror superposition and §5.3 rotation; syllabus §4.5 one/multiple-centre scope.')
add('06',[
 'A molecule must be inspected separately at each double bond for geometrical alternatives and at each tetrahedral carbon for chirality.',
 'A double-bond carbon with only three attachment directions is not the tetrahedral four-group chiral centre considered here.'
], 'Applying both structural tests', '''Use two separate inspection routes on a supplied structure. First mark each C=C and inspect the two groups attached at each end. If either end has identical groups, the simple geometrical pair is absent at that bond. If both ends have different groups, the relevant same-side and opposite-side arrangements can be considered where the cis/trans description is unambiguous. Do not infer this property merely from the appearance of two parallel bond lines.

Second inspect tetrahedral carbons. A carbon carrying two H atoms fails the four-different-groups test immediately. A carbon with four different attachments is a candidate chiral centre; mark that atom with an asterisk and identify the groups. The alkene carbons themselves have three attachment directions and are not the tetrahedral centres in this test. Thus the presence of a double bond does not automatically establish a chiral carbon.

For CH3CH=CHCH(OH)CH2CH3, the C=C carbons each have one H and one different carbon-containing group, so geometrical alternatives are possible. The OH-bearing carbon has H, OH, an ethyl group and an unsaturated three-carbon group. Those attachments are different, making it a chiral centre. The example illustrates that both kinds of structural feature can occur in one molecule without requiring a complete catalogue of its spatial forms.

By contrast, CH2=CHCH2OH has a terminal CH2 at the double bond and a CH2OH carbon. It fails the geometrical test because one alkene end has two H, and it fails the tetrahedral test because the alcohol carbon also has two H. State the specific duplicated group when rejecting a candidate. This is more informative than saying that the molecule is “too small” or “not symmetrical enough”. Throughout, preserve atom connections before discussing space: a change in OH position or carbon skeleton would create a structural comparison rather than a different arrangement of the same connections.''',
 '5-1-enantiomers-and-the-tetrahedral-carbon','OpenStax Organic §5.1 four-group test and §7.4 double-bond test; original combined example.')
oid='OBJ-8224-4.5-02'
t.blocks[oid][0]['text']+='''

For a final duplicate check, label the carbon atoms temporarily and follow the route between branch points or functional groups. Two sketches that can be matched atom for atom with the same neighbours represent one connectivity, even if one has been bent on the page. Remove the temporary labels before giving the chemical structure. By contrast, moving OH from an end carbon to an internal carbon changes its neighbours and gives a positional pair. This method keeps visual appearance separate from the evidence used to classify the isomers.'''
from authoring_common_8224 import stamp
for n in ['02','03','05','06']:
 oid='OBJ-8224-4.5-'+n
 for block in t.blocks[oid]:
  block['generalisation_scope']=[oid]
  stamp(block)
out=t.dir/'assets'
f=Figure('Cis and trans but-2-ene','Each double-bond carbon has H and CH3. Left cis has both methyl groups above; right trans has the right methyl below.')
for ox,trans in [(0,False),(420,True)]:
 f.text(ox+45,80,'trans-but-2-ene' if trans else 'cis-but-2-ene',22)
 for x in [130,270]:f.text(ox+x,215,'C',28)
 f.line([(ox+163,230),(ox+260,230)]);f.line([(ox+163,242),(ox+260,242)])
 for x,flip in [(130,False),(270,trans)]:
  dx=-55 if x==130 else 55
  f.line([(ox+x+10,209),(ox+x+dx+10,150)]);f.line([(ox+x+10,260),(ox+x+dx+10,315)])
  f.text(ox+x+dx-15,110,'H' if flip else 'CH3',24);f.text(ox+x+dx-15,335,'CH3' if flip else 'H',24)
f.save('8224-cis-trans-butene',out=out)
f=Figure('One chiral centre: mirror-image pair','Butan-2-ol tetrahedral centre attached to H, OH, methyl and ethyl. Right is reflected across the dashed mirror line, with solid and hashed depth preserved.')
for y in range(90,390,20):f.line([(420,y),(420,y+11)],'#718096',2)
for mirror in [False,True]:
 def p(x,y):return (840-x,y) if mirror else (x,y)
 def lab(x,y,s):
  xx,yy=p(x,y);f.text(xx-len(s)*6,yy,s,23)
 lab(220,220,'C*');lab(200,110,'H');lab(85,205,'OH');lab(315,340,'CH3');lab(125,350,'CH2CH3')
 f.line([p(220,210),p(205,150)]);f.line([p(195,235),p(110,225)])
 f.polygon([p(238,250),p(294,323),p(314,310)])
 for k in range(2,10):
  u=k/10;x=210-70*u;y=250+75*u;d=9*u;f.line([p(x-d,y-d),p(x+d,y+d)],width=2)
f.text(28,420,'Solid wedge: towards viewer. Hashed bond: away. * marks the centre.',18);f.save('8224-optical-mirror-pair',out=out)
qa=[
('Identify what is held constant when enumerating isomers from a given molecular atom count.','The numbers and types of atoms; different valid arrangements must retain that composition.'),
('Draw and name both open-chain alkane structures with composition C4H10.','Butane, CH3CH2CH2CH3, and 2-methylpropane, CH3CH(CH3)CH3. Draw all their connections; both have C4H10 and different carbon skeletons.'),
('State the difference between structural isomers.','They have the same molecular composition but different atom connectivity.'),
('Suggest the structural-isomer category for propan-1-ol and propan-2-ol.','Positional isomerism: the OH position differs on the same carbon skeleton.'),
('Identify the two syllabus divisions of stereoisomerism.','Geometrical cis–trans and optical isomerism.'),
('Draw cis and trans but-2-ene.','Draw each C=C carbon with H and CH3. In cis put methyl groups on the same side; in trans on opposite sides. Connectivity stays CH3CH=CHCH3; see assets/8224-cis-trans-butene.png.'),
('Describe the structural requirements and origin of cis–trans isomerism in but-2-ene.','C=C restricts relative rotation; each alkene carbon has two different attachments, H and CH3; same-side and opposite-side methyl arrangements therefore remain distinct under ordinary settings.'),
('Explain why turning a whole cis-but-2-ene drawing does not produce trans-but-2-ene.','Whole-molecule rotation preserves the same-side methyl relationship. Changing it requires relative rotation about C=C, which disrupts π bonding and has a substantial energy barrier.'),
('Identify the four different groups at the chiral centre of butan-2-ol.','H, OH, CH3 and CH2CH3 on carbon2.'),
('Draw a tetrahedral mirror-image pair for butan-2-ol, marking its chiral centre.','Mark the OH-bearing carbon C*. Attach H, OH, CH3 and CH2CH3 with a solid wedge, a hashed bond and two in-plane bonds; reflect the whole arrangement to produce its non-superimposable mirror. See assets/8224-optical-mirror-pair.png.'),
('State why propan-2-ol lacks a chiral carbon at its OH-bearing centre.','That carbon has two identical CH3 groups.'),
('Suggest which features in CH3CH=CHCH(OH)CH2CH3 permit the two kinds of isomerism taught here.','Each C=C carbon has H and a different carbon group, permitting geometrical alternatives; the OH-bearing carbon has four different groups and is a chiral centre.')]
for s,(q,a) in zip(t.wo['item_slots'],qa):
 st='WHY' if s['slot'].endswith('008-MECH') else None;t.item(s,q,a,subtype=st)
 if st:t.deviations.append({'from':s['slot']+' MECH','to':'WHY, frozen metadata retained','why':'Restricted rotation is a structural explanation, not an electron-transfer reaction requiring an intermediate.'})
mc=[
('Identify the number of open-chain alkane connectivities for C4H10.',['2','3','4','1'],0,'Butane and2-methylpropane give2;3/4 duplicate or invent structures,1 omits branching.'),
('Identify the relationship between but-1-ene and but-2-ene.',['optical','positional structural','identical after rotating paper','different compositions'],1,'B moves double-bond position; A wrongly keeps connectivity, C overlooks its position and D miscounts identical totals.'),
('Identify the relationship between cis and trans but-2-ene.',['chain structural','functional-group structural','geometrical stereoisomers','different molecular counts'],2,'C preserves connections with different spatial arrangement; A/B change connections and D contradicts their equal counts.'),
('Identify why propene lacks a cis/trans pair.',['it contains no double bond','it is saturated','its carbon count is odd','one double-bond carbon has two identical H groups'],3,'D is the local attachment test; A/B are false and C is not the criterion.'),
('Identify the open-chain alkene connectivity missing from but-1-ene and but-2-ene in a C4H8 list.',['2-methylpropene','butane','pent-1-ene','ethanol'],0,'A is the branched valid alkene; B/C/D have different counts or families.')]
t.item(t.wo['performance_tasks'][0],'Identify the correct option in each question (1 mark each).\n'+'\n'.join(f'{i}. {q} '+ '; '.join(f'{"ABCD"[j]} {v}' for j,v in enumerate(opts)) for i,(q,opts,k,a) in enumerate(mc,1)),'\n'.join(f'{i}. Key/correct option {"ABCD"[k]}. {a} Each distractor represents the stated error.' for i,(q,opts,k,a) in enumerate(mc,1)))
t.item(t.wo['performance_tasks'][1],'''Explain isomer relationships for C4H8 restricted to open-chain alkenes.
(a) Draw and name the three structural connectivities. [3]
(b) State the structural-isomer relationship of but-1-ene and but-2-ene. [1]
(c) Draw the two but-2-ene spatial forms. [2]
(d) Explain why those spatial forms remain distinct under ordinary settings. [2]''','''(a) CH2=CHCH2CH3, but-1-ene [1]; CH3CH=CHCH3, but-2-ene [1]; CH2=C(CH3)2,2-methylpropene [1]. (b) Positional structural isomers [1]. (c) Correct same-side CH3 cis [1] and opposite-side trans [1], H completing each carbon. (d) Restricted rotation at C=C [1]; interchange requires disruption of π bonding [1]. Creditworthy points per part, total8 marks.''')
t.item(t.wo['performance_tasks'][2],'''Calculate how many distinct open-chain C4H8 alkene forms result when geometrical forms are counted separately. Give the structural connectivities, state their isomer relationships and account for whether each provides one or two spatial forms. [5]''','''Three structural connectivities: but-1-ene [1], but-2-ene and branched2-methylpropene [1]. But-1-ene/but-2-ene are positional, while2-methylpropene changes the chain skeleton [1]. But-2-ene supplies cis/trans stereoisomers because each C=C carbon has H and CH3; the other two lack this pair [1]. Equation/working:1+2+1=4 distinct forms [1]. Answer is a count with no physical unit; counts are exact integers so significant-figure rounding is inapplicable. No mass or volume conversion is required.''')
t.deviations.append({'from':'Generic calculation task expecting continuous quantities and significant figures','to':'Exact quantitative interpretation of isomer counts with full structural reasoning','why':'The mapped objectives concern representation and isomerism; adding unrelated mole calculations would manufacture objective coverage. Exact counts have no measurement precision.'})
t.save()
