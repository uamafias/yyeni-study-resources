"""Concrete drawing briefs; renderer must preserve these labels and relationships."""
from practical_data import DATA
# Per visual: labels/entities, geometry or values, scientific acceptance criteria.
DETAILS={
'1':[
(['cm³','°C','lower meniscus','eye level'], 'Cylinder 0–50 cm³ in 1 cm³ divisions at 36; thermometer 0–50 °C in 1 °C divisions at 24.', 'Volume scale increases upward; reading at bottom of concave meniscus; no printed answer beside the question image.'),
(['funnel','filter paper','residue','filtrate','distillation flask','thermometer','condenser','water in','water out','receiver'], 'Two panels: filtration and simple distillation. Condenser coolant enters lower port and exits upper; thermometer bulb at sidearm level.', 'Distillation receiver is open to atmosphere; no sealed heated apparatus; filter paper sits inside funnel.'),
(['reference volume / cm³','cylinder reading / cm³'], 'Use DATA-1 graph coordinates; reference x 0–50, reading y 0–55.', 'Provide blank learner axes separately from answer overlay; points and fit follow declared numerical tolerances.')],
'2':[
(['solid','liquid','gas','nucleus','proton','neutron','electron'], 'Three particle panels use identical-size particles, clustered/ordered, close/disordered, widely spaced respectively. Sodium-23: 11p,12n; shells 2,8,1. Na+ shells 2,8.', 'Gas particles are not larger than solid particles; atom/ion nuclear composition unchanged.'),
(['H2','HCl','H2O','NH3','CH4','shared pair','lone pair'], 'Dot/cross outer-shell counts: H2 one shared pair; HCl one bond and 3 Cl lone pairs; water 2 bonds/2 O lone pairs; ammonia 3 bonds/1 N lone pair; methane 4 bonds.', 'Dots/crosses identify electron origins, not unequal electron charge; show all specified outer-shell electrons.'),
(['linear CO2','tetrahedral CH4','pyramidal NH3','bent H2O'], 'Show CO2 straight; methane four tetrahedral directions with wedge/dash; ammonia three bonds and a lone pair above N; water two bonds and two O lone pairs.', 'Do not present ammonia as planar or water as linear; no numerical bond-angle memorisation added.'),
(['diamond','graphite','metal lattice','positive ions','delocalised electrons'], 'Diamond each C has 4 bonds in 3D; graphite each C 3 in hexagonal sheets; metal shows positive ions surrounded by electron sea.', 'No bonds linking graphite sheets as though covalent diamond; show layers separately.')],
'3':[
(['hydrophilic head','hydrophobic tail','grease droplet','water'], 'Circular grease droplet with tails directed inward and heads facing surrounding water.', 'No reversal of polar/non-polar orientation; soap and detergent panels use the same amphiphilic organisation.'),
(['1 nm','100 nm','1 μm','1 mm'], 'Logarithmic size ladder: 1 nm=10⁻9 m, 100 nm=10⁻7 m, 1 μm=10⁻6 m, 1 mm=10⁻3 m.', 'Explicitly label logarithmic spacing; do not draw sizes to a false linear scale.'),
(DATA['3']['apparatus_labels'], 'Use DATA-3 dry/wet masses and separate graph panel from declared water-uptake pairs.', 'Balance supports the sample vessel; use identical draining procedure before wet readings.')],
'4':[
(['mass / g','amount / mol','solution volume / dm³','concentration / mol dm⁻³','gas volume / dm³ at room conditions'], 'Directed links: n=m/M; n=cV; n=Vgas/24. cm³→dm³ divide by1000.', 'Do not treat mass concentration as molar concentration; molar gas volume applies at room temperature and pressure.'),
(DATA['4']['apparatus_labels'], 'Two magnified burette panels: initial 0.40 and final25.40 cm³, 0.1 cm³ graduations.', 'Numbers increase downwards; bottom of each meniscus gives stated reading ±0.05 cm³; answer overlay separate.')],
'5':[
(DATA['5']['apparatus_labels'], 'Aqueous CuSO4 with carbon electrodes; collect oxygen at positive anode using inverted water-filled tube.', 'Cathode copper deposit; gas labelled only on answer overlay; DC polarity and anode collection must agree.'),
(['carbon anode','copper anode','copper cathode','Cu²⁺','O2'], 'Side-by-side cells with same current/time/solution; copper anode dissolves, carbon anode evolves O2.', 'Show copper loss at active anode and gain at cathode; no oxygen label at copper anode.')],
'6':[
(['energy','reaction progress','reactants','products','activation energy','ΔH'], 'Original exothermic profile: reactants80, peak140, products30 in arbitrary energy units; Ea60 and ΔH−50.', 'Axes have no time label; ΔH arrow spans reactant/product levels, activation arrow reactants to peak. Include separate endothermic example reactants30, peak140, products80.'),
(['time / s','CO₂ volume / cm³','slow','fast'], 'Use DATA-6 time grid and both volume lists; both end at48 cm³, fast levels earlier.', 'Curves start at origin; fast never falls below slow; do not extend above limiting-reactant endpoint.'),
(['closed vessel','N2 + 3H2 ⇌ 2NH3','forward reaction','reverse reaction'], 'Particle/flow panels show a closed reversible system, with 4 gaseous reactant molecules versus2 product molecules per stoichiometric event.', 'At equilibrium rates equal, not necessarily amounts; no leaking vessel or stopped-reaction symbolism.')],
'7':[
(['pH 0–14','acidic','neutral','alkaline','litmus','universal indicator'], 'pH axis0–14; neutral7. Universal-indicator schematic red1, orange3, yellow5, green7, blue9, purple12; litmus acid red/alkali blue.', 'Colours labelled as approximate indicator colours; no conflation of acid strength and concentration.'),
(DATA['7']['apparatus_labels']+['AgNO3 solution','NaCl solution','AgCl precipitate'], 'Separate soluble-salt flow (excess CuO,filter,concentrate,cool) and insoluble-salt flow (mix,filter,wash,dry).', 'Do not crystallise AgCl from filtrate; do not evaporate CuSO4 preparation to dryness.')],
'8':[
(['NaOH dropwise','NaOH excess','dilute HNO3 then AgNO3','precipitate','solution'], 'Unknown X observations exactly DATA-8; additional answer key identifies Cu²⁺ and Cl⁻.', 'Learner table omits identities; observation colours belong to solids unless explicitly described as solution.'),
(['Cu²⁺ solution','NH3 dropwise','NH3 excess','light-blue precipitate','deep-blue solution'], 'Three stages: initial aqueous copper(II), small NH3 gives light-blue precipitate, excess NH3 gives clear deep-blue solution.', 'Final stage is solution with no residual solid; omit complex-ion formula and ligand mechanism.'),
(['glowing splint','oxygen','damp red litmus','ammonia','limewater','carbon dioxide','clean wire','potassium lilac flame'], 'Four separate small panels for oxygen/ammonia/CO2/flame test, with observation labels in answer overlay.', 'Do not use a lighted splint for oxygen confirmation; never smell gases directly; clean-wire flame test.')],
'9':[
(['iron ore','coke','limestone','hot air','waste gases','molten iron','slag'], 'Blast furnace hot air at lower tuyeres, charge at top, gas outlet near top, slag outlet above iron outlet. Equations C+O2→CO2; CO2+C→2CO; Fe2O3+3CO→2Fe+3CO2; CaCO3→CaO+CO2; CaO+SiO2→CaSiO3.', 'Balance each equation; iron below less dense slag; reduction attributed to CO.'),
(['pure metal','alloy','layers','different-sized atoms'], 'Pure lattice has equal atoms and aligned layers; alloy includes minority different-radius atoms disrupting alignment.', 'No claim every alloy has identical properties; show inhibited layer sliding for the model.'),
(DATA['9']['apparatus_labels'], 'Side-by-side Mg/Zn setups, matched area, same acid volume/concentration; DATA-9 time/volume table.', 'Gas syringe connected without leaks; no flame near evolved hydrogen.')],
'10':[
(['ethene','ethanol','ethanoic acid','ethyl ethanoate','C=C','–OH','–COOH','–COO–'], 'Display all bonds: CH2=CH2; CH3CH2OH; CH3COOH; CH3COOCH2CH3.', 'Carbon valency4, oxygen2, hydrogen1; distinguish alcohol OH from acid hydroxyl.'),
(['ester linkage','amide linkage','sugar units','joining oxygen'], 'Show R–C(=O)–O–R′ and R–C(=O)–NH–R′; schematic sugar boxes joined through O.', 'Preserve carbonyl double bond; use generic protein units without named individual amino acids.'),
(['poly(ethene)','poly(chloroethene)','n','repeat-unit brackets'], 'Repeat units [–CH2–CH2–]n and [–CH2–CHCl–]n; bonds extend through both brackets.', 'No C=C in addition-polymer backbone; chlorine attached as substituent, not in main chain.'),
(DATA['10']['apparatus_labels'], 'Use DATA-10 positions: baseline1 cm above bottom, solvent0.5 cm, front8 cm above baseline; spots2.4 and4.8 cm above baseline.', 'Distances measured from baseline; solvent below spots at start; separate annotated answer overlay.')],
'11':[
(['screening','sedimentation','filtration','chlorination','treated water'], 'Left-to-right treatment process with solid removal before disinfection; link sediment/sludge to waste path.', 'Filtration alone does not guarantee safe drinking water; chlorination is disinfection, not dissolved-salt removal.'),
(['remove water vapour','remove CO2','cool/compress','liquid air','fractional distillation','nitrogen','oxygen'], 'Show dry CO2-free air liquefaction then column; nitrogen lower boiling point(−196 °C) leaves before oxygen(−183 °C).', 'These are boiling points, not imposed syllabus gas-law calculations; remove water/CO2 before cooling to avoid blockage.'),
(['Haber: iron catalyst','450 °C','200 atm','recycle','Contact: V2O5','450 °C','approximately 1–2 atm'], 'Haber N2+3H2⇌2NH3, ammonia condensed and gases recycled. Contact2SO2+O2⇌2SO3 then absorb SO3 in concentrated H2SO4 to oleum, dilute carefully.', 'State conditions as typical industrial values; never depict direct uncontrolled SO3+water addition as industrial absorption.')],
'12':[
(['thermometer / °C','burette / cm³','cylinder / cm³','meniscus'], 'Panels: thermometer63°C with1°C divisions; burette6.40cm³ with0.1 divisions; cylinder36cm³ with1 divisions.', 'Burette scale increases down; thermometer/cylinder upward; do not print answer values beside task panels.'),
(['time / min','temperature / °C','uninsulated','insulated'], 'Use DATA-12 pairs and both cooling curves; x0–10min, y20–90°C.', 'No curve below room22°C or crossing implying insulated sample colder; answer read-offs follow stated tolerances.'),
(DATA['12']['apparatus_labels']+DATA['11']['apparatus_labels'], 'Two distinct panels: insulation investigation with identical vessels and water levels; hardness measurement with cylinder and soap burette using DATA-11 scales.', 'Thermometer bulb off vessel walls; insulation thickness controlled; clearly separate hot-water and soap apparatus.')]
}

def detail_visuals(visuals,topic):
 assert len(visuals)==len(DETAILS[topic])
 for v,(labels,geometry,acceptance) in zip(visuals,DETAILS[topic]):
  v['required_labels']=labels;v['geometry_and_values']=geometry;v['scientific_acceptance_criteria']=acceptance
  v['learner_answer_separation']='Where a reading/identity is assessed, supply an unkeyed learner panel and a separate labelled answer overlay.'
  v['review_status']='pending_scientific_and_numerical_review'
 return visuals
