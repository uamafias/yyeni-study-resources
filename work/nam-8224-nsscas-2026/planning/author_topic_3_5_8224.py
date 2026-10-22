"""Original nitrogen/sulphur resource with bounded WHO terminology correction."""
from authoring_common_8224 import Topic
from render_chemistry_visuals_8224 import Figure
t=Topic('3.5')
def add(short,claims,title,text,loc,source='OpenStax-Chemistry'):t.objective(short,claims,[(title,text)],source,loc)
add('1-01',[
 'Ammonia accepts H+ through its nitrogen lone pair, forming tetrahedral NH4+ with four N–H bonds and no nitrogen lone pair.',
 'Aqueous ammonia is a weak base: NH3 + H2O ⇌ NH4+ + OH−.',
 'An ammonium salt releases ammonia on reaction with a strong base, for example NH4+ + OH− → NH3 + H2O.'
], 'Ammonia, ammonium and proton transfer', '''Ammonia has three N–H bonds and one lone pair on nitrogen. It is a Brønsted–Lowry base because it accepts a proton. Nitrogen donates its lone pair to H+, forming NH4+. The donated pair makes a co-ordinate covalent bond in the formation description; after formation the four N–H bonds in the ammonium ion are equivalent rather than one being a permanently different weak attachment.

The ammonium ion is tetrahedral, with four bonding pairs and no lone pair on its central nitrogen. Its bond angles are approximately 109.5°. Draw brackets and the overall positive charge. Nitrogen has not acquired an extra electron from the proton: H+ contributes no electron, so the new shared pair comes from nitrogen. The valence count in NH4+ is five from nitrogen plus four from hydrogen minus one for the positive charge: eight electrons in four shared pairs. Topic 1.3 explains the electron-pair geometry.

![Generated tetrahedral ammonium representation, with a solid wedge towards and hashed bond away from the viewer](assets/8224-ammonium-tetrahedral.png)

In water, NH3(aq) + H2O(l) ⇌ NH4+(aq) + OH−(aq). Only part of the ammonia reacts in the weak-base model, and the hydroxide concentration makes the solution alkaline. Ammonia does not need an OH group in its original composition to act as a base. It accepts a proton from water, leaving OH−.

Adding a strong base to an ammonium salt reverses the proton-transfer role: NH4+(aq) + OH−(aq) → NH3 + H2O(l). Warming can help release NH3 gas from the mixture. For example, NH4Cl(aq) + NaOH(aq) → NH3(g) + NaCl(aq) + H2O(l) under the stated warming. Damp red litmus turns blue in a suitable ammonia-gas test. Do not explain this as oxidation of nitrogen: it remains −3 in NH3 and NH4+. The change is transfer of a proton, and the equation gives one mole of ammonia per mole of ammonium ion used.''',
 '§14.1 printed pp.766–768; §18.5 printed p.998; §7.6 electron-pair shapes. Tetrahedral geometry and acid/base balance derived from valence count.')
add('1-02',[
 'Farming removes nutrient elements in harvested material, while water movement can carry dissolved nutrients out of the root zone.',
 'Nitrogen, phosphorus and potassium are nutrient elements; their actual soil species differ in mobility and retention.',
 'Nitrate is highly mobile in soil water, while phosphorus and potassium losses depend on soil chemistry and transport pathways.'
], 'Why soils lose nutrient elements', '''Growing plants take up nutrient elements including nitrogen, phosphorus and potassium. When crops are harvested and removed, some of those elements leave the field in the crop material. Repeated farming can therefore deplete an available nutrient supply unless it is replenished. A plant does not create a nutrient element from water simply because its mass increases.

Leaching is a separate loss pathway. Water moving through soil can dissolve and transport nutrient-containing species below the root zone or into drainage. Highly soluble nitrate can move readily in this way. The process depends on water movement, nutrient form, soil retention and plant uptake; a dry period and a heavy-rainfall period need not give equal losses from the same field.

Phosphorus and potassium are also removed by harvest, but their soil species do not necessarily leach as readily as nitrate. Phosphate can interact strongly with soil solids, and potassium can be retained by some soil surfaces. Losses can still occur depending on soil composition, dissolved transport and movement of soil particles. Do not interpret “NPK depletion” as evidence that all three elements have identical water solubility or travel in the same ions.

For an original inventory, a field that loses 20.0 mol of a nutrient in harvested material and 5.00 mol through drainage has lost 25.0 mol through those two measured pathways. That total does not include an unmeasured process automatically. A fertiliser comparison should consider which nutrient is deficient and what reaches the roots, rather than merely choosing the largest product mass. This links the chemistry of soluble species to the soil application without inventing a recommended dose for a particular Namibian farm.''',
 'Syllabus §3.5.1 nutrient depletion; OpenStax §18.7 and §18.8 nutrient compounds; solubility/retention application. Detailed soil mobility is an explicit semantic-review reference focus.',source='NSSCAS-8224-SYLLABUS')
add('1-03',[
 'N2 is relatively unreactive under ordinary settings because its strong N≡N bond gives a large barrier to many reactions.',
 'Industrial ammonia manufacture converts atmospheric nitrogen into chemically accessible nitrogen compounds for fertiliser use.',
 'The Haber process requires a rate/yield compromise and a catalyst rather than assuming abundant N2 reacts readily at room temperature.'
], 'Abundant nitrogen is not automatically available nitrogen', '''Nitrogen gas is abundant in air, but the N2 molecule is relatively unreactive under ordinary room-temperature settings. Its atoms are joined by a strong triple covalent bond. Chemical changes that rearrange this stable molecule often face a large activation barrier. The abundance of nitrogen in the atmosphere therefore does not guarantee that a crop can use it directly.

Industrial ammonia manufacture converts nitrogen and hydrogen into ammonia: N2(g) + 3H2(g) ⇌ 2NH3(g). A catalyst and suitable temperature and pressure give a useful production rate while recognising the exothermic reaction's equilibrium limit. The purpose of the process here is to convert atmospheric nitrogen into a form that can be used to make fertiliser compounds. Topic 2.3 explains why low temperature favours the equilibrium product but does not by itself give a useful industrial rate.

Ammonia can react with acids to form ammonium salts. For example, 2NH3 + H2SO4 → (NH4)2SO4. These products supply chemically accessible nitrogen rather than expecting N2 gas to react readily in the soil by the same uncatalysed industrial pathway. Biological nitrogen fixation can also convert atmospheric nitrogen into usable compounds; the existence of that specialised route does not make ordinary N2 chemically reactive in every setting.

An explanation of fertiliser manufacture should connect bond stability, difficulty of direct reaction and conversion into suitable compounds. Saying “plants need nitrogen” identifies the nutrient role but leaves out why industrial conversion is useful. Saying “nitrogen has a triple bond” names a structure but should also connect it to strong bonding and the reaction barrier. The industrial catalyst changes the pathway and approach rate, while the overall atom balance still requires one N2 for two NH3.''',
 '§13.3 printed pp.734–735 Haber rationale; §18.5 p.998 ammonia and §18.7 nitrogen reactivity; original cross-links.')
add('1-04',[
 'Nitrogen oxidation numbers in the required examples are −3 in NH3, 0 in N2, average +1 in N2O and +5 in NO3−.',
 'Conversion from N2 to NH3 is nitrogen reduction, while conversion from reduced nitrogen to nitrate is oxidation.',
 'Nitrogen-cycle transformations conserve nitrogen atoms while changing molecular or ionic form and formal oxidation number.'
], 'Tracking nitrogen through different forms', '''Use the oxidation-number rules from Topic 2.2 to track the specified nitrogen species. In NH3, three hydrogens at +1 require nitrogen −3. In uncombined N2, nitrogen is zero. In NO3−, three oxygens at −2 require nitrogen +5. These values refer to the nitrogen atoms, not the overall charge of each molecule or ion.

For N2O, oxygen contributes −2 and the molecule is neutral. The two nitrogen atoms therefore contribute +2 together, giving an average oxidation number of +1. This average does not claim that the two chemically different positions in the actual molecule must have identical local electronic descriptions. It is the whole-molecule accounting value requested for this comparison.

Fixing N2 into ammonia takes nitrogen from 0 to −3 and is reduction. Conversion of reduced nitrogen into nitrate raises its oxidation number towards +5 and is oxidation. Processes that return nitrate nitrogen to N2 lower the value from +5 towards 0 and are reductions; N2O can occur among gaseous nitrogen-containing forms in the cycle. Different biological and chemical steps carry out the transformations rather than a single universal reaction in one vessel.

Follow the direction before assigning a redox label. NH3 to NO3− is an increase of eight oxidation-number units per nitrogen atom; the reverse change would be a decrease. The atom does not become a new element when its number changes. Nitrogen is conserved even when it moves from dissolved species into a gas that leaves the soil. That phase transfer can remove plant-available nitrogen locally while keeping nitrogen in the wider cycle. Naming the species and calculating their values makes this a chemical account rather than a memorised circular arrow.''',
 'Syllabus §3.5.1 named nitrogen-cycle species; OpenStax §4.2 oxidation-number rules and §18.7 nitrogen compounds. Numerical assignments transparently derived; detailed cycle references remain for semantic review.')
add('1-05',[
 'Ammonia is an industrial starting material for nitrogen fertilisers, including ammonium salts.',
 'Ammonium-containing fertilisers provide nitrogen in a chemically available form, but their nutrient percentage and environmental behaviour depend on composition.'
], 'From ammonia to a fertiliser product', '''Ammonia is important industrially because it is a starting material for nitrogen-containing fertilisers and other nitrogen compounds. Its reaction with an acid can form an ammonium salt. With sulphuric acid, 2NH3 + H2SO4 → (NH4)2SO4; with nitric acid, NH3 + HNO3 → NH4NO3. These acid–base equations show nitrogen entering salts rather than turning N2 directly into a plant nutrient without chemical conversion.

The nitrogen mass percentage depends on the composition. Ammonium sulphate contains two nitrogen atoms per composition unit. With supplied relative atomic masses N 14, H 1, S 32 and O 16, its molar mass is 132 g mol⁻¹ and nitrogen contributes 28 g mol⁻¹. Its nitrogen percentage is 28/132 × 100, about 21.2%. A product's total mass is therefore not the same as its mass of nitrogen.

Ammonium nitrate contains nitrogen in both the ammonium and nitrate parts, with different oxidation numbers. The compound name does not make the two nitrogen environments identical. A mixture described as NPK fertiliser contains nutrient sources for nitrogen, phosphorus and potassium; the exact proportions and chemical forms need the supplied composition data.

Industrial importance does not imply that more soluble fertiliser should be added without limit. A useful agricultural supply must match crop demand and soil information, while losses into drainage reduce efficiency. Compare nutrient amount, availability and environmental pathways when data are given. At this level, identify ammonia as a chemical feedstock and explain how its salts can supply accessible nitrogen. Keep the manufacturing reaction separate from the field processes that later release, retain, transform or remove the nutrient.''',
 '§18.5 p.998 ammonia/salt formation; §18.7 nitrates and fertiliser importance; original percentage arithmetic using supplied atomic masses.')
add('1-06',[
 'Soluble nitrate fertilisers can leach with water into surface waters or groundwater, including borehole sources.',
 'Nutrient enrichment can stimulate excessive aquatic growth, followed by decomposition that consumes dissolved oxygen and harms aquatic organisms.',
 'Possible drinking-water contamination needs chemical assessment rather than visual appearance alone.'
], 'Leaching, eutrophication and water quality', '''A soluble nitrate fertiliser dissolves in soil water and can be taken up by roots. If dissolved nitrate is carried away before uptake, some of the applied nutrient is lost through drainage or runoff. Groundwater can receive that transported nitrate, so a borehole drawing from affected water may contain contamination. The word “borehole” does not itself guarantee that nutrient-rich surface water cannot influence the source.

Nutrient enrichment of a lake or slow-moving water body can stimulate excessive growth of algae or other aquatic producers. As the material dies and is decomposed, microorganisms use dissolved oxygen. Oxygen depletion can harm fish and other organisms. This linked process is eutrophication. State the growth and decomposition stages rather than saying simply that nitrate removes oxygen directly in a one-step reaction.

The outcome depends on nutrient loading, water movement, light and other ecological factors, so a single small addition need not cause the same visible result in every water body. Soluble fertiliser can contribute to the nutrient input without being the only possible source. Compare the transport pathway and amounts in a supplied scenario before assigning a cause to one field.

Nitrate contamination of drinking-water sources is a separate concern from visible algal growth. A clear sample may contain dissolved species that cannot be seen. Chemical measurement is needed to assess the relevant contaminant; appearance or absence of smell is not a concentration result. The syllabus requires recognition of possible contamination, not a diagnosis or an invented safe concentration. A reasoned explanation links high solubility to transport and possible exposure, and links aquatic nutrient enrichment to growth, decay and oxygen use. This supports environmental evaluation of fertiliser use alongside its agricultural benefit.''',
 'Syllabus §3.5.1 explicit nitrate/leaching/eutrophication/borehole scope; general soluble-species principles from OpenStax §§3.3 and 4.2. Environmental mechanism retained for independent factual-reference verification.',source='NSSCAS-8224-SYLLABUS')
add('1-07',[
 'Organic fertilisers can contain less immediately soluble nutrient material that becomes available progressively during decomposition.',
 'Slower nutrient release can reduce immediate leaching loss in a suitable comparison but does not eliminate nutrient pollution.',
 'Comparisons must account for nutrient composition, soluble fractions and release timing rather than assuming all organic material behaves identically.'
], 'Benefits of less immediately soluble nutrient sources', '''Organic fertilisers such as suitable composted plant or animal material can contain nutrients in forms that are less immediately soluble than a readily soluble nitrate salt. Decomposition and other soil processes progressively release chemically available nutrients. This can spread supply over time rather than placing the entire nutrient amount into soil water at once.

Lower immediate solubility can reduce rapid leaching in a comparison where other relevant factors are suitable. More nutrient may remain in or near the soil until it becomes available for uptake. This can improve retention relative to a soluble application followed immediately by heavy water movement. Explain the benefit through delayed release and transport rather than claiming that an organic label prevents movement of all nutrient species.

Organic materials differ in composition and can also contain soluble nutrient fractions. They may release nutrients when crop demand is low, and runoff or excessive application can still contribute to water pollution. The timing depends on material, soil and environmental settings. A slower-release source can also be less immediately available where a crop needs a prompt supply. These are trade-offs, not reasons to classify either fertiliser type as universally best.

For a supplied choice, compare the same nutrient amount rather than only the same mass of product. A bulky organic material and a concentrated nitrate salt can contain very different nitrogen percentages. Use data on release rate, rainfall or irrigation and uptake where available. State a conditional benefit, such as lower immediate leaching under a particular water regime, and a limitation, such as uncertain timing of release. This connects the solubility argument to the environmental mechanisms above without inventing a field-specific recommendation.''',
 'Syllabus §3.5.1 lower-solubility organic fertiliser comparison; chemistry of solubility and conservation applied qualitatively. Soil-release detail is a semantic-review reference focus.',source='NSSCAS-8224-SYLLABUS')

add('2-01',[
 'Burning sulphur-containing fossil fuels can produce sulphur dioxide as sulphur is oxidised.',
 'Roasting sulphide-containing ores can release sulphur dioxide while converting the metal-bearing feed.',
 'The sulphur content of a fuel affects the potential SO2 produced; fuel sulphur and combustion carbon are distinct inputs.'
], 'Where sulphur dioxide comes from', '''Sulphur dioxide is an atmospheric pollutant associated with burning fuels that contain sulphur compounds and with processing sulphide ores. Sulphur in the feed is oxidised during combustion or roasting. The simplified elemental relation is S + O2 → SO2. The sulphur may originally be in a compound, so the fuel is not assumed to contain only free yellow sulphur. Elemental sulphur changes from oxidation number 0 to +4 in SO2, consistent with oxidation and the oxygen consumed in this equation.

Coal and petroleum-derived fuels can contain sulphur-bearing material. If it is oxidised to SO2, increasing the mass of sulphur burned increases the potential gas amount unless capture or another pathway intervenes. Carbon combustion produces carbon oxides, whereas sulphur supplies the sulphur atom of SO2. A fuel's carbon content cannot by itself establish its sulphur dioxide output.

Roasting sulphide ores gives a second source. As the feed is heated in oxygen, sulphur can leave as SO2 while the metal-bearing material changes to a form suitable for further extraction. The precise equation depends on the ore, but the pathway connects to the copper-processing outline in Topic 3.3. Not every ore is a sulphide, so the pollutant cannot be assigned equally to every metal extraction solely from the word mining.

For original amount arithmetic, 1.00 mol of sulphur atoms can give 1.00 mol SO2 in the simplified complete-oxidation model. Using molar masses 32.0 and 64.0 g mol⁻¹, 32.0 g sulphur corresponds to 64.0 g SO2, with oxygen supplying the extra mass. Actual atmospheric release also depends on combustion and capture. Distinguish pollutant formed from pollutant emitted when interpreting an industrial scenario; neither a fuel label nor a reaction equation replaces an emission measurement.''',
 '§18.9 printed p.1017 (PDF p.1027), sulphur dioxide from fuel and sulphide roasting; §18.10 sulphur oxidation; original stoichiometric example.')
add('2-02',[
 'SO2 exposure can affect breathing and is associated with respiratory ill health.',
 'Atmospheric sulphur dioxide can undergo reactions leading to acidic deposition, including sulphuric-acid formation.',
 'Acidic deposition can damage susceptible ecosystems and carbonate building materials.'
], 'Breathing effects and acid deposition', '''Sulphur dioxide is relevant to health because exposure can affect breathing. WHO identifies an association between SO2 exposure and asthma-related hospital and emergency visits. This is a reason to control exposure, not a claim that an observed illness in one person can be diagnosed from a nearby chimney. The chemistry resource concerns the pollutant pathway and general consequence rather than individual medical assessment.

SO2 also contributes to acid rain and other acidic deposition. It dissolves and reacts in atmospheric water, and oxidation can produce sulphuric acid. A simplified overall balance is 2SO2 + O2 + 2H2O → 2H2SO4. The real atmosphere contains several reaction pathways, so this net equation does not describe a single collision occurring as written.

Acidic water can change soil and surface-water chemistry and harm susceptible organisms. It also reacts with carbonate building materials such as limestone: CaCO3 + 2H+ → Ca2+ + CO2 + H2O. The material is gradually lost through chemical reaction, not simply stained by a coloured gas. Nitrogen oxides can contribute to acidic deposition as well, so identifying SO2 as a cause does not mean it is the only atmospheric acid precursor.

When evaluating a proposed control, identify the target. Reducing SO2 formation or capturing it lowers a precursor to both exposure and acid deposition. Filtering dust alone does not establish that SO2 has been removed, and a measured stack concentration does not directly equal the concentration inhaled by a population after dispersion. A complete explanation connects the source, gas transport or chemical transformation, and the named effect. No numerical exposure threshold is needed to recall the syllabus's breathing and acid-rain consequences.''',
 'WHO Type of pollutants, Sulfur Dioxide section, official page read 2026-10-22; OpenStax §14.2 printed p.774 and §15.3 p.863 acid rain/carbonate attack. WHO verification recorded in reference pack.',source='WHO-AQG-2021')
add('2-03',[
 'Using lower-sulphur fuel reduces the potential SO2 formed for a comparable fuel use and conversion.',
 'WHO air-quality guidelines concern pollutant concentrations and health exposure; they are not themselves a specific plant’s legally binding stack-emission limits.',
 'The syllabus names Van Eck in Windhoek as an application context; assessing its actual compliance requires current measurements and applicable requirements.'
], 'Low-sulphur fuels and interpreting a guideline', '''Using a lower-sulphur fuel reduces the sulphur available to form SO2 in a comparable combustion process. This is a source-control approach. Gas treatment can provide an additional control after formation. The relevance to vehicles and power generation follows the same atom balance: less sulphur feed generally means less potential sulphur dioxide, while the actual emitted amount also depends on capture and operation.

For an original comparison, two equal 1000 kg fuel batches containing 1.00% and 0.200% sulphur supply 10.0 kg and 2.00 kg sulphur respectively. Under the simplified complete-conversion model they could form 20.0 kg and 4.00 kg SO2. These are potential formation masses, not measured emissions. The example shows how changing fuel composition can reduce a pollutant source without assigning any current value to a named station.

The syllabus refers to WHO limits in this context. WHO's air-quality guidelines are health-based recommendations for pollutant concentrations over specified exposure averaging periods. They can inform national standards, but do not themselves establish a particular plant's legal emission permit. Keep ambient exposure, stack emissions and legal compliance distinct. This clarification follows the [official WHO explanation](https://www.who.int/news-room/questions-and-answers/item/who-global-air-quality-guidelines).

Van Eck at Windhoek is the syllabus's named power-station context. A question can use it to ask why low-sulphur fuel helps reduce SO2. A claim that the station currently meets or exceeds a requirement would instead need current relevant measurements, averaging basis and the applicable requirement. No such compliance claim is made from the chemical equation. State the control's purpose and the evidence required to assess it, preserving the syllabus lesson while keeping the meaning of a guideline precise.''',
 'WHO Global Air Quality Guidelines Q&A, What are the guidelines?/How can these guidelines be used?, read 2026-10-22; syllabus §3.5.2 named context. Source-control mass balance original.',source='WHO-AQG-2021')

f=Figure('Ammonium ion: tetrahedral, NH4+','Central N has four N–H bonds, no lone pair and tetrahedral geometry. Two lines lie in the page, a solid wedge points towards the viewer and a hashed bond away. Brackets show total positive charge. Schematic projection, angles about 109.5 degrees.')
cx,cy=420,230
f.text(cx-13,cy-18,'N',30)
for x,y in [(280,131),(560,131)]:
 f.line([(cx+(x-cx)*.13,cy+(y-cy)*.13),(x-(x-cx)*.13,y-(y-cy)*.13)],width=3);f.text(x-11,y-18,'H',29)
f.polygon([(405,250),(300,342),(321,360)])
f.text(286,367,'H',29)
for k in range(1,11):
 u=k/11;x=cx+110*u;y=cy+130*u;dx=9*u;f.line([(x-dx,y+dx*.7),(x+dx,y-dx*.7)],width=2)
f.text(531,367,'H',29)
f.line([(200,80),(180,80),(180,410),(200,410)],width=2);f.line([(640,80),(660,80),(660,410),(640,410)],width=2);f.text(673,70,'+',30)
f.text(305,66,'No N lone pair',19);f.text(28,105,'H–N–H:',18);f.text(28,135,'≈109.5°',18)
f.text(25,428,'Lines: in plane. Solid wedge: towards. Hashed bond: away.',17)
f.save('8224-ammonium-tetrahedral',out=t.dir/'assets')
s=t.wo['item_slots']
qa=[
 ('Identify the electron pair that allows NH3 to accept H+ and form NH4+. [1]','The lone pair on nitrogen [1].'),
 ('Draw NH4+ with its tetrahedral arrangement, showing four N–H bonds, the overall charge and whether nitrogen has a lone pair. [2]','Four N–H bonds around N with no N lone pair [1]; tetrahedral representation with overall + charge, approximately 109.5° [1].\n\n![Generated model ammonium structure](assets/8224-ammonium-tetrahedral.png)'),
 ('State two pathways by which farming can deplete soil nutrients. [1]','Removal in harvested material and loss through water-driven leaching [1].'),
 ('Explain why a field can lose nitrogen even when much of the crop remains locally. [2]','Dissolved nitrogen-containing species such as nitrate can be carried by moving water [1]; leaching can move them below roots or into drainage, removing available nutrient from the field [1].'),
 ('Describe why atmospheric nitrogen is difficult to use directly and why industrial ammonia manufacture is useful for fertilisers. [3]','N2 has a strong triple bond [1], giving a large barrier and low ordinary reactivity [1]; conversion to ammonia and salts supplies chemically accessible nitrogen compounds [1].'),
 ('Explain why plentiful N2 in air does not by itself provide readily reacting fertiliser nitrogen. [2]','Its strong N≡N bond makes ordinary chemical conversion difficult [1]; a specialised biological or industrial pathway is needed to produce suitable available compounds [1].'),
 ('Describe nitrogen’s oxidation numbers in NH3, N2, N2O and NO3−, and the direction from NH3 to nitrate. [3]','NH3 −3 and N2 0 [1]; N2O average +1 and NO3− +5 [1]; NH3 to nitrate raises the value and is oxidation [1].'),
 ('Explain why N2O has average nitrogen oxidation number +1 rather than +2 per nitrogen. [2]','Oxygen at −2 requires the two nitrogens together to contribute +2 [1]; dividing by two nitrogen atoms gives the average +1 [1].'),
 ('State an industrial use of ammonia relevant to crop nutrition. [1]','Manufacturing nitrogen fertilisers, including ammonium salts [1].'),
 ('Suggest how ammonia can be converted into ammonium sulphate. [1]','React it with sulphuric acid: 2NH3 + H2SO4 → (NH4)2SO4 [1].'),
 ('Describe three linked environmental consequences of highly soluble nitrate fertiliser being transported by water. [3]','Rapid leaching can remove nutrient from roots [1]; enrichment of surface waters can contribute to eutrophication and oxygen depletion [1]; groundwater or borehole sources can become nitrate-contaminated [1].'),
 ('Explain how nutrient enrichment can harm fish through eutrophication. [2]','It can stimulate excessive aquatic growth [1]; decomposition of dead material consumes dissolved oxygen, reducing what is available to fish [1].'),
 ('Describe a potential benefit, chemical reason and limitation of an organic fertiliser with less immediately soluble nutrient material. [3]','Lower immediate leaching can retain nutrient [1] because release into solution is slower [1]; release timing and soluble fractions vary, so pollution is not eliminated [1].'),
 ('Explain why lower immediate solubility can reduce early nutrient loss from a fertiliser. [2]','Less nutrient enters moving soil water at once [1], so a smaller amount can be carried away before later release and uptake [1].'),
 ('State two syllabus sources of atmospheric sulphur dioxide. [1]','Burning sulphur-containing fossil fuel and roasting sulphide ores [1].'),
 ('Suggest why burning two equal fuel masses can give different potential SO2 amounts. [1]','Their sulphur contents may differ [1], giving different sulphur amounts available for oxidation.'),
 ('State one breathing-related and one environmental consequence of SO2 pollution. [1]','Breathing difficulties/respiratory effects and contribution to acid rain [1].'),
 ('Suggest why sulphur dioxide pollution can damage limestone structures after atmospheric chemical changes. [1]','It contributes to acidic deposition, whose H+ reacts with the carbonate building material [1].'),
 ('State why using low-sulphur fuel is relevant to the syllabus’s vehicle and power-station example. [1]','It reduces the sulphur available to form SO2 and helps control pollutant exposure [1].'),
 ('Suggest what extra evidence is needed before claiming that a named station meets an applicable SO2 requirement. [1]','Relevant current measurements with the correct averaging/measurement basis and the actual applicable requirement [1]; a low-sulphur label alone is insufficient.')
]
assert len(qa)==len(s)
for slot,(prompt,answer) in zip(s,qa):
 st='WHY' if slot['subtype']=='MECH' else None
 t.item(slot,prompt,answer,subtype=st)
 if st:t.deviations.append({'from':slot['slot']+' MECH','to':'WHY; preserve original AO/Bloom/command/tariff','why':'The task concerns bond stability, oxidation-number arithmetic, transport or nutrient-release reasoning, without a specified electron-arrow reaction intermediate/product mechanism.'})
p=t.wo['performance_tasks']
t.item(p[0],'''Identify one correct option per question. [7]
1. A source of SO2 is: A roasting a sulphide ore; B dissolving pure NaCl in water; C melting pure ice; D condensing nitrogen.
2. Low-sulphur fuel reduces the feed amount of: A carbon dioxide; B sulphur available for SO2 formation; C oxygen in air by definition; D calcium.
3. SO2 exposure can affect: A only colour vision; B only metal melting; C breathing; D no biological process.
4. Acid rain can attack limestone through: A creation of extra carbonate; B freezing alone; C removal of oxygen from calcium; D acid–carbonate reaction.
5. WHO air-quality guidelines are primarily: A health-based concentration guidance; B a named station’s individual permit; C a fuel mass specification; D proof of current compliance.
6. Lower potential SO2 formation establishes lower actual emitted mass only if: A the plant name is known; B the relevant conversion and capture comparison is accounted for; C the fuel is dark; D no measurement can be made.
7. A carbon-only fuel contains no sulphur. In the ideal atom balance, its carbon alone can form: A SO2; B H2SO4; C carbon oxides rather than SO2; D a sulphide ore.''',
 '''Key: 1 A, 2 B, 3 C, 4 D, 5 A, 6 B, 7 C. One mark per correct option.
1. A oxidises feed sulphur. B, C and D supply no sulphur-forming reaction.
2. B follows source control. A confuses the target element; C invents a fixed oxygen change; D introduces an unrelated element.
3. C is the syllabus health consequence. A and B select unrelated exclusive effects; D denies relevant health effects.
4. D consumes carbonate. A reverses the chemical loss; B is a different physical process; C misstates the reaction.
5. A describes the guidance. B confuses it with a plant-specific legal instrument; C uses the wrong measured quantity; D omits actual evidence.
6. B keeps formation distinct from release. A is not performance evidence; C is not a sulphur amount; D denies a measurable issue.
7. C conserves elements. A and B introduce sulphur absent from the specified input; D confuses fuel combustion with ore formation.''')
t.item(p[1],'''Explain the following nitrogen chemistry and environmental links. [8]
(a) Explain NH3’s basicity and how it forms NH4+. [2]
(b) State two ways farming can remove soil nutrients. [2]
(c) Explain why industrial conversion of N2 into ammonia is useful despite abundant N2 in air. [2]
(d) Explain how soluble nitrate transported to a water body can cause oxygen depletion. [2]''',
 '''Part (a): nitrogen’s lone pair accepts H+ [1], forming NH4+ by proton transfer/donation of that pair to the proton [1].
Part (b): removal in harvested crops [1] and leaching with moving water [1].
Part (c): the strong N≡N bond gives low ordinary reactivity [1]; industrial conversion supplies available nitrogen compounds for fertilisers [1].
Part (d): nutrient enrichment can stimulate excessive aquatic growth [1]; decomposition then consumes dissolved oxygen [1]. Each bracket is a separate creditworthy point.''')
t.item(p[2],'''Calculate the following original fertiliser quantities and interpret the chemistry. [5]
(a) A 6.60 g sample of pure (NH4)2SO4, molar mass 132 g mol⁻¹, reacts completely with excess strong alkali. Calculate moles of NH3 liberated, giving three significant figures. [2]
(b) State the oxidation-number change per nitrogen from NH3 to NO3−. [1]
(c) In a separate soil model, 20.0% of 0.100 mol nitrate nitrogen is lost in drainage. Calculate moles of nitrogen lost. [1]
(d) State the bond feature explaining why ordinary atmospheric N2 is relatively unreactive. [1]''',
 '''(a) Equation (NH4)2SO4 + 2OH− → 2NH3 + SO4²− + 2H2O; n(salt) = 6.60/132 = 0.0500 mol [1]. Working n(NH3) = 2 × 0.0500 = 0.100 mol to three significant figures [1]. Mass units are consistent and need no conversion.
(b) −3 to +5, an increase of eight units per nitrogen [1].
(c) n lost = 0.100 × 20.0/100 = 0.0200 mol to three significant figures [1].
(d) The strong N≡N triple bond [1], associated with a large reaction barrier.''')
t.deviations.append({'from':'Syllabus phrase WHO limits applied to named station emissions','to':'Teach low-sulphur source control and distinguish WHO exposure guidance from plant-specific legal emission limits','why':'Official WHO guidance explicitly distinguishes recommendations from legally binding standards. No station compliance claim, current operating claim or numerical limit is introduced; verified official links are recorded.'})
t.deviations.append({'from':'N2O nitrogen +1 label','to':'State average +1 for the two nitrogen atoms','why':'Whole-molecule charge balance gives the average; the two actual nitrogen positions need not be electronically equivalent.'})
t.deviations.append({'from':'Broad organic-fertiliser lower-solubility wording','to':'Qualify as less immediately soluble nutrient fractions and gradual release, with variable soluble content','why':'An organic label does not ensure uniform solubility, no leaching or universally superior performance.'})
t.deviations.append({'from':'Local factual-reference limits','to':'Keep soil transport/eutrophication/organic-release detail flagged for independent semantic source verification','why':'The syllabus names these processes and the manuscript gives original explanations, but the general local chemistry textbook has limited direct soil/ecology coverage.'})
t.save()
