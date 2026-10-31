import re
CARDS={}
def card(k,p,a,g,recall=0,sub='APP',ao='B',bloom='Apply'):
 CARDS[k]=dict(prompt=p,canonical_answer=a,marking_guidance=g.split('|'),recall=recall,subtype=sub,assessment_objectives=[ao],blooms_level=bloom)
card('2-086','Explain why an H2 molecule has two electrons in total even though each hydrogen atom is described as having a complete first shell.','The same pair is shared and counted around both nuclei; completing both shells does not create four separate electrons.','Both nuclei attract/share the same pair (1).|Counting that pair for each shell does not double the number of distinct electrons; total remains two (1).',0,'MECH','A','Understand')
card('3-021','Identify the bonding that must be broken to cut the molecular backbone of a polythene chain.','Covalent carbon–carbon bonds in the chain.','Covalent bonds in the backbone (1).',1,'DEF','A','Remember')
card('5-031','Outline why a rise in pH during electrolysis of concentrated aqueous NaCl does not by itself establish the amount of sodium hydroxide produced.','The pH indicates increased alkalinity, but it is not a direct measure of total amount. The solution volume and a suitable concentration measurement are needed to determine amount.','Rising pH supports alkalinity rather than a total product amount (1).|Amount requires concentration together with solution volume; use a suitable quantitative measurement (1).',0,'INTERP','B','Analyse')
card('10-016','Explain why a graph of increasing boiling point alone cannot establish that several organic compounds belong to one homologous series.','Many unrelated substances have different boiling points. Membership also requires the same functional group and successive members differing by CH2, so a physical trend alone is insufficient.','A boiling-point trend is not unique to a homologous series (1).|Check common functional group and the successive CH2 difference rather than relying on that trend alone (1).',0,'MECH','A','Understand')
card('11-040','Suggest the decision for a recovered CO2 batch containing 0.08% impurity when the stated drinks-use specification allows at most 0.02%, even though the batch gives a positive limewater test.','Reject or further purify it: 0.08% exceeds the 0.02% limit; a CO2 identity test does not establish that purity requirement.','Reject/further purify because 0.08% exceeds 0.02%; positive identity test cannot override the limit (1).',0,'APP','B','Apply')
card('6-052','State the interval with the greater average gas-production rate: a reaction produces 18 cm³ in its first 20 s and another 10 cm³ during the next 20 s.','The first interval: 18/20 = 0.90 cm³/s, compared with 10/20 = 0.50 cm³/s in the second.','First 20 s, with 0.90 versus 0.50 cm³/s or the equivalent equal-time comparison (1).',0,'INTERP','B','Apply')
OPTIONS={
(1,'5'):['Gas volume / s','Gas volume / cm³','Elapsed time / cm³','Gas volume / cm'],
(2,'1'):['Fills all available space','Occupies a measurable volume','Contains particles in motion','Has a measurable mass'],
(2,'8'):['Nuclei attracting other positive nuclei','Electrons attracting other negative electrons','Nuclei attracting a shared electron pair','Molecules attracting neighbouring neutral molecules'],
(3,'2'):['Transmits light and bends without breaking','Resists impact but blocks visible light','Bends readily but scratches very easily','Transmits light but fractures under impact'],
(3,'5'):['Constituents have different chemical structures','Constituents must have identical bonding','Mixing changes all bonds to covalent','Water makes all constituents ionic'],
(3,'9'):['Heads in grease, tails facing water','Heads and tails both inside grease','Heads and tails both outside grease','Tails in grease, heads facing water'],
(4,'6'):['Relative mass of the simplest formula','Molar mass divided by Avogadro constant','Mean atomic mass of its elements','Molecular mass divided by atom count'],
(8,'10'):['Damp red litmus turns blue','A lighted splint gives a pop','A glowing splint becomes a flame','Damp litmus loses its colour'],
(9,'10'):['Composition must suit the intended properties','Extra carbon improves all steel properties','All added elements have identical effects','Steel must retain one molecular formula'],
(10,'4'):['They contain equal numbers of carbons','They have the same molecular formula','They have the same boiling point','They contain the same functional group'],
(10,'11'):['Water joins sugars into longer starch chains','Protein chains lengthen without reacting with water','Amide links form as water molecules leave','Water breaks amide links to release amino acids'],
}
def apply_card(x,k):
 if k not in CARDS:return None
 for f,v in CARDS[k].items():
  if f!='recall':x[f]=v
 return CARDS[k]['recall']
def apply_mc(z,t):
 options=OPTIONS.get((t,z['part']))
 if not options:return
 old=dict(re.findall(r'^([A-D])\. (.+)$',z['prompt'],re.M));key=z['canonical_answer'][0]
 reason=z['canonical_answer'][len(key+'. '+old[key]):].lstrip('. ')
 z['prompt']=z['prompt'].split('\nA. ')[0]+'\n'+'\n'.join(k+'. '+v for k,v in zip('ABCD',options))
 z['canonical_answer']=key+'. '+options[ord(key)-65]+'. '+reason
 # Correct scientific explanation retained; options rewritten in parallel grammatical form.
# Parallel option forms also remove the reverse cue of unusually short correct answers.
OPTIONS.update({
(1,'3'):['View the lower meniscus at eye level','View the upper meniscus at eye level','Read the lower meniscus from well below','Tilt the cylinder towards the viewing eye'],
(1,'8'):['Every reaction speeds up at any temperature','Both trials have the same production rate','The warmer trial yields more gas overall','The warmer trial produces gas more quickly'],
(1,'12'):['Evaporate the entire mixture','Decant before sand settles','Crystallise the dissolved salt','Filter the stirred mixture'],
(2,'4'):['Isotopes are all naturally radioactive','Radioactivity removes an outer-shell electron','Isotopes may be stable or radioactive','Different mass numbers require different elements'],
(2,'5'):['X forms X⁻; Y forms Y⁺','X forms X⁺; Y forms Y⁻','X forms X²⁺; Y forms Y²⁻','X forms X⁻; Y forms Y⁻'],
(2,'7'):['Brass is a variable-composition mixture','Brass is a variable-formula compound','Cooling changes atoms into new elements','Copper and zinc require fixed proportions'],
(3,'7'):['Glass windows: transmission of visible light','Copper cable coverings: high electrical conductivity','Glass bending brackets: resistance to scratching','Concrete flexible sheets: high compressive strength'],
(4,'3'):['Exactly one gram of pure water','Approximately 6.022 × 10²³ hydrogen atoms','One individual molecule of pure water','Approximately 6.022 × 10²³ H2O molecules'],
(5,'10'):['Copper ions gain electrons there','Copper atoms gain two electrons','Copper atoms dissolve as Cu²⁺','Water oxidises instead of copper'],
(5,'11'):['Mixing metals into bulk alloys','Applying a decorative metal coating','Removing a metal by dissolution','Filtering out dissolved metal ions'],
(6,'5'):['No operating combustion; weather-dependent output','Low operating emissions; weather-independent output','No fuel combustion; no construction impacts','Variable weather dependence; no energy transfer'],
(6,'6'):['A larger final gas volume','A slower gas-production rate','A smaller final gas volume','A higher gas-production rate'],
(6,'7'):['Average particle kinetic energy increases','The activation-energy barrier becomes lower','Collisions transfer greater energy individually','Successful collisions occur more frequently'],
(6,'10'):['Copper metal dissolves without oxidising','A different blue oxide forms','Sulfate changes to another anion','The blue hydrated salt reforms'],
(6,'11'):['No shift; equilibrium remains unchanged','Forward shift; more C forms','Both forward and reverse reactions stop','Reverse shift; more A and B form'],
(7,'1'):['An electron donor','A proton donor','A proton acceptor','An oxygen donor'],
(7,'3'):['Solubility and dissociation describe different properties','Its pH is seven in every preparation','Its clear appearance establishes chemical neutrality','Limited solubility establishes weak dissolved-base dissociation'],
(7,'6'):['It necessarily contains hydroxide ions','It necessarily dissolves completely in water','It releases hydrogen with water','It reacts to neutralise acids'],
(7,'10'):['To dissolve the desired insoluble product','To remove all the insoluble residue','To remove the adhering soluble impurities','To add further reactant to crystals'],
(7,'11'):['Lead(II) carbonate','Lead(II) chloride','Lead(II) sulfate','Lead(II) nitrate'],
(8,'2'):['It confirms the later sample colour','It detects contamination on the wire','It measures the dissolved salt concentration','It establishes that the sample is pure'],
(8,'3'):['Sodium removes the other ion chemically','Mixtures give identical colours for all ions','Bright sodium emission masks other colours','Sodium makes the other salt colourless'],
(8,'7'):['Water alone makes the paper alkaline','Dissolved ammonia creates the alkaline conditions','Gas displaces water from the litmus','Dampness changes nitrogen gas to ammonia'],
(8,'9'):['Insoluble calcium carbonate forms a precipitate','Soluble calcium hydrogen carbonate immediately precipitates','Carbon dioxide deposits as white solid','Calcium hydroxide becomes solid calcium metal'],
(8,'12'):['A glowing splint relights','Clear limewater turns milky','A lighted splint pops','Damp litmus loses colour'],
(9,'1'):['High density and scratch resistance','Thermal conduction and material brittleness','Low density and electrical insulation','Electrical conductivity and material ductility'],
(9,'3'):['Native metals mixed with sand','Chemically combined in mineral compounds','Separate atoms within inert minerals','Alloys separated by physical methods'],
(9,'8'):['It forms an aqueous oxide solution','It dissolves oxide at lower temperature','It chemically reduces aluminium ions itself','It blocks ions from the cathode'],
(10,'2'):['They have different chemical reactivities','They have different boiling ranges','They have different solubilities in water','They have different solid melting points'],
(10,'5'):['Extra oxygen causes incomplete combustion','Restricted air permits complete carbon oxidation','Restricted air guarantees carbon dioxide only','Less oxygen permits incomplete combustion'],
(10,'12'):['Matching conditions permit meaningful reference comparisons','Matching conditions force all spots together','Different solvents improve comparisons of Rf','Reference spots belong above the front'],
(11,'1'):['Pure water boils independently of pressure','Impurities alone change the boiling temperature','Pressure can change the boiling temperature','Reduced pressure demonstrates increased dissolved impurity'],
(11,'3'):['Sulfate precipitates while calcium remains dissolved','Carbonate ions precipitate dissolved calcium ions','Calcium sulfate changes into calcium metal','Calcium ions become removable by filtration'],
})
# Complete forward-direction test practice without adding duplicate item slots.
card('8-027','Describe the reagent sequence and positive observation for chloride ions in a fresh aqueous sample.','Acidify with dilute nitric acid, then add aqueous silver nitrate. A white precipitate forms.','Dilute nitric acid followed by aqueous silver nitrate (1).|White precipitate (1).',2,'PROC','A','Remember')
card('8-029','Describe how to test a solution for bromide ions, naming the acid, the test reagent and the visible result.','Acidify with dilute nitric acid, then add aqueous silver nitrate. A cream precipitate forms.','Dilute nitric acid followed by aqueous silver nitrate (1).|Cream precipitate (1).',2,'PROC','A','Remember')

# Every option in this flame-colour question is now a flame colour.
OPTIONS[(8,"5")]=["Lilac","Bright yellow","Brick-red","Red"]
