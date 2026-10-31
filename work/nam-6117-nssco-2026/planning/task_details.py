"""Fixed part-level teaching/marking briefs; original learner wording follows approval."""
from collections import Counter
from practical_data import attach_data

def mc_demand(objective):
 text=objective['learner_objective'].lower();verb=text.split()[0]
 if verb in {'evaluate','plan','design'}:
  level='Evaluate';ao='B';demand='Select a justified method or judgement from supplied alternatives using an explicit criterion.'
 elif verb in {'interpret','analyse','deduce'}:
  level='Analyse';ao='B';demand='Infer the answer from a supplied pattern, observations or numerical representation.'
 elif verb in {'use','calculate','determine','solve','add','make','carry','complete','record','predict','suggest'}:
  level='Apply';ao='B';demand='Apply the stated relationship or procedure to fresh supplied quantities or an unfamiliar case.'
 elif verb in {'define','state','name','recall','list','recognise'}:
  level='Remember';ao='A';demand='Recognise the specified fact, identity or definition among alternatives.'
 else:
  level='Understand';ao='A';demand='Recognise a scientifically correct explanation, description or comparison of the stated familiar concept.'
 # Discuss does not by itself imply evaluation: isotope examples test understanding.
 return level,[ao],demand

# Explicit review of each fixed short-answer credit brief, independent of part order.
SHORT_AO={
 '1':['A','A','A','B'],'2':['B','A','A','B'],'3':['A','A','A','B'],
 '4':['A','A','A','B'],'5':['A','A','A','B'],'6':['A','B','A','B'],
 '7':['A','A','A','B'],'8':['A','A','A','B'],'9':['A','B','A','B'],
 '10':['A','A','A','B'],'11':['A','A','A','B']}
SHORT_BASIS={
 '2:a':'B3: deduce neutron number by subtracting supplied proton count from nucleon count.',
 '6:b':'B4: describe trends read from supplied gas-volume data.',
 '9:b':'B4: interpret the supplied displacement observations.',
}

SHORT={
 '1': [('1.3-02','SI volume unit: m³ (1).'),('1.5-03','Describe a sharp melting point (1) and agreement with the reference value for the pure substance (1).'),('1.5-06','Explain filtration: insoluble sand is retained (1) while dissolved salt passes through (1).'),('1.5-06','Recover water by simple distillation: water vaporises (1), vapour condenses (1), non-volatile salt stays behind (1).')],
 '2':[('2.1.2-09','For a sodium-23 atom, state the neutron count: 12 (1).'),('2.4.2-01','Describe sodium losing one electron (1) and chlorine gaining it to form oppositely charged ions (1).'),('2.4.3-10','Explain solid NaCl non-conduction: ions carry charge (1) but cannot move through the solid lattice (1).'),('2.4.3-10','Explain a supplied high-melting, conducting molten sample: identify ionic structure (1), strong electrostatic attractions require energy to overcome (1), mobile ions conduct when molten (1).')],
 '3':[('3.3-01','State that the soap tail is hydrophobic (1).'),('3.3-02','Describe tails entering grease (1) and hydrophilic heads facing water (1).'),('3.3-05','Explain biodegradability: microorganisms break the material down (1), reducing its persistence (1).'),('3.3-06','For supplied hard-water washing observations, explain insoluble scum with soap (1), reduced soap available for cleaning (1), and a detergent advantage based on its lack of that precipitate (1).')],
 '4':[('4.1-08','State amount concentration as moles of solute per dm³ of solution (1).'),('4.2-02','Describe making a dilution: transfer a measured solution volume (1), add water to the specified final volume and mix (1).'),('4.2-02','Explain that dilution retains solute amount (1) while increased solution volume lowers concentration (1).'),('4.2-02','Given two equal-volume NaOH solutions at 0.100 and 0.200 mol/dm³, explain that the second has twice the amount of NaOH (1), requires twice the HCl amount for 1:1 neutralisation (1), hence twice the same-concentration HCl volume (1).')],
 '5':[('5.1-03','State reduction occurs at the cathode (1).'),('5.1-05-04','Describe hydrogen formation at the cathode (1) and chlorine at the anode (1) for concentrated aqueous NaCl with inert electrodes.'),('5.1-07','For CuSO4 with copper electrodes, explain copper-anode dissolution (1) as Cu atoms lose two electrons to form Cu2+ (1).'),('5.1-07','For replacing the copper anode with inert carbon, explain oxygen replaces dissolving copper as the anode process (1), Cu2+ still deposits at the cathode (1), and Cu2+ is no longer replenished so solution blue colour fades (1).')],
 '6':[('6.4-01','State rate as change in reactant/product quantity per unit time (1).'),('6.4-09','Describe the supplied gas-volume curves: initially steep then flatten (1); equal final volume for equal limiting-reactant amount (1).'),('6.4-05-03','Explain powder reacting faster: larger exposed surface area (1), more frequent effective collisions at the surface (1).'),('6.4-09','For a fresh curve with steeper initial slope but the same endpoint, explain a higher initial rate (1), unchanged total gas amount (1), and distinguish a rate change from a change in limiting-reactant amount (1).')],
 '7':[('7.3-01','State the reaction of acid and base is neutralisation (1).'),('7.3-04','Describe adding excess copper(II) oxide to warm dilute sulfuric acid (1) and filtering off excess solid (1).'),('7.3-04','Explain excess oxide consumes acid (1), while insolubility permits removal of unreacted oxide (1).'),('7.4-03','For given soluble AgNO3 and NaCl, explain precipitation of insoluble AgCl (1), filtration to isolate it (1), washing to remove soluble impurities (1).')],
 '8':[('8.2-01-01','State ammonia turns damp red litmus blue (1).'),('8.2-01-02','Describe bubbling gas through limewater (1), which becomes milky with CO2 (1).'),('8.2-01-05','Explain a glowing splint relights (1) because oxygen supports combustion (1).'),('8.1-01-10','Given a transient yellow contamination followed by persistent lilac flame, explain lilac identifies potassium (1), yellow contamination can obscure it (1), repeat with a clean wire to distinguish the persistent sample colour (1).')],
 '9':[('9.2-01','State magnesium is above copper in the reactivity series (1).'),('9.2-02','Describe magnesium displacing copper from CuSO4: copper coating forms (1), blue solution fades (1).'),('9.4-08','Explain intact paint excludes oxygen/water (1), preventing the rusting conditions (1).'),('9.4-08','For scratched zinc-coated iron, explain zinc is more reactive (1), oxidises preferentially (1), and protects exposed iron sacrificially (1).')],
 '10':[('10.2.2-01','State the functional group of alcohols is hydroxyl, –OH (1).'),('10.4-04','Describe adding bromine water (1), which is decolourised by ethene but remains coloured with ethane under the stated test conditions (1).'),('10.7-01','Explain ester formation from ethanol and ethanoic acid (1) produces ethyl ethanoate and water (1).'),('10.7-01','Given propanol instead of ethanol, explain the alcohol supplies the propyl group (1), ethanoic acid supplies ethanoate (1), giving propyl ethanoate plus water (1).')],
 '11':[('11.1.2-02','State hard water forms lather less readily with soap (1).'),('11.1.2-07','Describe adding washing soda (1) to precipitate calcium ions as calcium carbonate (1).'),('11.4-03','Explain sulfur dioxide is an acidic oxide (1) that reacts with atmospheric water to produce acidic rain (1).'),('11.5-05','For a proposed higher-pressure Haber plant, explain fewer gas molecules on the product side (1), higher pressure favours ammonia yield (1), but pressure equipment/energy costs limit the practical choice (1).')]
}
# Criterion-specific deliverables prevent the old cyclic objective assignment from
# pretending that an apparatus drawing tests an unrelated recall objective.
SKILLS={'C1':'12.2-01','C2':'12.5-01','C3':'12.1-01','C4':'12.3-02','C5':'12.4-01'}
PRACTICAL={
 '1':['Read two stated instrument scales with units (1 each).','Draw filtration with filter paper/funnel (1) and vessel collecting filtrate (1).','Plot the supplied calibration pairs: axes/units (1), accurate points (1), appropriate best-fit line (1).','Calculate mean repeated volume: sum/count (1), result with unit (1).','Explain a named parallax error (1), its effect on the reading (1), and eye-level viewing as the corresponding improvement (1).'],
 '2':['Draw a low-voltage conductivity circuit: source/switch (1), indicator (1), two separated electrodes contacting the sample (1).','Describe testing each sample (1), recording bulb/current response (1), rinsing electrodes between samples (1).','Explain conductivity using mobile ions in solution (1), mobile electrons in metal (1), absence of mobile charges in a molecular sample (1).','Describe controlling electrode spacing (1), immersion depth (1), and voltage (1) for a fair comparison.'],
 '3':['State initial dry mass (1) and final drained wet mass (1).','Draw water-absorption setup showing sample immersion (1) and a balance for mass measurements (1).','Plot absorption data: axes/units (1), points (1), suitable trend line (1).','Calculate water uptake: wet minus dry mass (1), mass result and unit (1).','Explain inconsistent draining changes retained surface water (1), biases the mass gain (1), so use a fixed draining time (1).'],
 '4':['Name a burette for delivering measured titrant (1).','State initial and final burette readings (1 each).','Calculate titre: final minus initial (1), convert cm³ to dm³ (1), use cV for amount with mol unit (1).','Calculate the other reacting amount from the supplied balanced ratio (1), then its concentration from the stated solution volume (1).','Explain rough-titre uncertainty (1) and use repeated concordant titres for the mean (1).','State controlled aliquot volume (1) and the same indicator/endpoint criterion (1).'],
 '5':['Draw DC supply and polarity (1), separated electrodes in electrolyte (1), gas collection at the specified electrode (1).','Describe gas collection without contamination (1), the appropriate test reagent/procedure (1), its positive observation (1).','Deduce the collected gas from the supplied observation (1).','Explain charge transport by ions in electrolyte (1) and electrons in external circuit (1).','Describe comparing named active and inert electrodes (1), holding electrolyte/current/time constant (1), recording electrode mass or product differences (1).'],
 '6':['Plot time/gas volume: axes/units (1), points (1), smooth curve (1).','Calculate average rate from stated interval: volume change/time change (1), result with unit (1).','State a gas syringe measures evolved gas volume (1).','Plan concentration effect: gas-collection method (1), vary acid concentration (1), control carbonate mass and particle size (1), control temperature (1), measure gas volume at fixed times (1), compare initial rates for a conclusion (1).'],
 '7':['Describe dissolving/reacting suitable starting materials (1), filtering excess solid (1), concentrating and cooling the filtrate for crystals (1).','State an observation of reaction completion (1), and one observation of crystallisation (1).','Explain why washing crystals with a small volume of cold water limits product loss (1).','Plan AgCl preparation: soluble silver salt (1), soluble chloride solution (1), mix measured quantities (1), filter precipitate (1), wash/remove soluble impurities (1), dry and judge completion/purity from observations (1).'],
 '8':['Describe NaOH dropwise and in excess (1), initial precipitate colour (1), its excess-reagent behaviour (1) for the named unknown.','Deduce the cation from the supplied complete test results (1).','Describe acidifying a separate sample (1), adding AgNO3 (1), recording precipitate colour (1).','Explain separate portions prevent reagent carry-over (1), acidification removes carbonate interference (1), and compare recorded results with the specified ion alternatives (1).','State clean labelled test tubes (1) and a dropper for controlled addition (1).'],
 '9':['Plan metal/acid comparison: same acid concentration (1), same acid volume/temperature (1), matched exposed metal area (1), collect evolved gas safely (1), measure volume against time (1), compare rate to infer relative reactivity (1).','Calculate average gas-production rate (method 1; result/unit 1).','State time (1) and gas volume (1) measured during the comparison.','Explain oxide coatings alter apparent rate (1), clean surfaces consistently before testing (1).'],
 '10':['Plan chromatography of hydrolysed food extract: prepare/filter sample (1), pencil baseline above solvent (1), small dried sample/reference spots (1), develop in covered chamber (1), mark solvent front and visualise spots appropriately (1), compare with references for a conclusion (1).','State baseline-to-spot distance (1), baseline-to-solvent-front distance (1).','Calculate Rf: spot/front distance ratio (1), dimensionless result (1).','Explain overlarge spots merge components (1), smaller dried applications improve separation (1).'],
 '11':['Plan hardness comparison: equal measured water volumes (1), fixed soap concentration (1), add soap in measured increments (1), standardise shaking (1), use persistent-lather endpoint (1), compare soap volumes to infer hardness (1).','Draw a labelled measuring vessel (1) and apparatus for controlled soap-solution addition (1).','State initial and final soap-volume readings (1 each).','Explain a larger soap volume indicates greater hardness (1) because calcium/magnesium ions remove soap before lasting lather forms (1).'],
 '12':['Plot cooling data: axes/units (1), accurate points (1), suitable trend line (1).','Calculate cooling rate over a supplied interval: temperature change/time (1), value and unit (1).','State a thermometer measures the temperature (1).','Plan insulation comparison: same vessel/water volume (1), same starting temperature (1), vary only insulation material (1), record temperature at fixed times (1), repeat/control ambient conditions (1), compare cooling curves for a conclusion (1).']}

def detail_tasks(order,registry):
 byid={o['objective_id']:o for o in registry};topic=order['topic'].split()[0]
 for t in order['performance_tasks']:
  kind=t['item_type']
  if kind=='multiple_choice_set':
   t['context_brief']='Twelve independent four-option questions on the explicitly listed part targets; each part supplies its own fresh chemical case where required.'
   for p in t['parts']:
    p['command_word']=None
    p['command_word_basis']='Four-option multiple choice; no written-response command.'
    objective=byid[p['objective_ids'][0]]
    p['blooms_level'],p['assessment_objectives'],p['planned_cognitive_demand']=mc_demand(objective)
    p['ao_basis']='A: familiar knowledge with understanding.' if p['assessment_objectives']==['A'] else 'B: handling supplied information, applying a relationship or solving a new problem.'
    p['blooms_level_basis']='Provisional demand from the named objective and explicit MC task brief; confirm against the authored stem and options.'
    p['credit_requirement']='One mark for the uniquely correct option for '+p['content_target']+'. Supply the key, its chemical explanation and three distinct misconception-based distractor explanations.'
  elif kind=='short_answer':
   for index,(p,(target,rubric)) in enumerate(zip(t['parts'],SHORT[topic])):
    p['objective_ids']=['OBJ-6117-'+target];p['content_target']=byid[p['objective_ids'][0]]['learner_objective'];p['credit_requirement']=rubric
    p['assessment_objectives']=[SHORT_AO[topic][index]]
    p['ao_basis']=SHORT_BASIS.get(topic+':'+p['part'], 'A: recalled fact or explanation of a familiar chemical mechanism.' if p['assessment_objectives']==['A'] else 'B: apply chemistry to the supplied new case or interpret its evidence.')
    p['blooms_level']='Apply' if topic=='2' and index==0 else 'Analyse' if p['assessment_objectives']==['B'] else 'Remember' if index==0 else 'Understand'
   revise_short_shape(t,topic)
   if topic=='11':t['context_brief']='A chemical works treats hard water, controls sulfur-dioxide emissions and considers pressure choices in an ammonia plant.'
  elif kind=='practical_task':
   if topic=='12':t['context_brief']='Compare insulation materials using water-cooling data and a fair investigation.'
   local=[o for o in t['objective_ids'] if not o.startswith('OBJ-6117-12')]
   for p,rubric in zip(t['parts'],PRACTICAL[topic]):
    p['credit_requirement']=rubric
    skill=SKILLS[p['practical_criterion']]
    if p['command_word']=='Plot':skill='12.3-03'
    elif p['command_word']=='Draw':skill='12.2-03'
    elif p['command_word']=='Calculate':skill='12.2-02'
    # Credit the directly exercised skill; context topics are retained separately
    # rather than claiming every local objective on every practical subpart.
    p['context_objective_ids']=local
    p['objective_ids']=['OBJ-6117-'+skill]
    p['content_target']=t['context_brief']+' '+byid['OBJ-6117-'+SKILLS[p['practical_criterion']]]['learner_objective']
  elif kind=='calculation':
   pairs=([('4.2-02','State n=cV, with volume in dm³ (1).'),('4.2-02','Convert 25.0 cm³ to 0.0250 dm³ and substitute (1); n(HCl)=0.00500 mol (1).'),('4.2-03','Use the 2:1 ratio to obtain 0.00250 mol CO2 (1); multiply by 24 to give 0.0600 dm³ (1).')] if topic=='4' else [('6.2-04','State q=mcΔT (1).'),('6.2-04','Substitute 100×4.2×8.0 (1); q=3360 J (1).'),('6.2-05','Use broken-minus-formed, 436+243−2×431 (1); ΔH=−183 kJ/mol (1).')])
   for p,(target,rubric) in zip(t['parts'],pairs):p['objective_ids']=['OBJ-6117-'+target];p['content_target']=byid[p['objective_ids'][0]]['learner_objective'];p['credit_requirement']=rubric
  if kind=='practical_task':attach_data(t,topic)
  t['ao_split']=dict(Counter())
  for part in t['parts']:
   for ao in part['assessment_objectives']:t['ao_split'][ao]=t['ao_split'].get(ao,0)+part['mark_tariff']/len(part['assessment_objectives'])
  t['mark_tariff']=sum(p['mark_tariff'] for p in t['parts'])
  t['assessment_objectives']=sorted(t['ao_split'])
  t['objective_ids']=list(dict.fromkeys(o for p in t['parts'] for o in p['objective_ids']))
  if kind=='short_answer':t['required_visual_ids']=[v['visual_id'] for v in order['visual_requirements']]
 return order


def revise_short_shape(task,topic):
 parts=task['parts']
 task['response_format']='structured short answer'
 if topic=='2':
  parts[0]['command_word']='Calculate'
  parts[0]['credit_requirement']='Calculate neutron count: 23 − 11 = 12 (1).'
 if topic=='4':
  parts[1].update(command_word='Calculate',mark_tariff=3,assessment_objectives=['B'],blooms_level='Apply',ao_basis='B3: convert supplied volume and calculate concentration.',credit_requirement='For 0.0100 mol in 250 cm³: V=0.250 dm³ (1), c=n/V (1), c=0.0400 mol/dm³ (1).')
  task['context_brief']='A solution contains 0.0100 mol in 250 cm³; compare two 25.0 cm³ NaOH portions at 0.100 and 0.200 mol/dm³, neutralised by the same HCl solution.'
 if topic=='6':
  parts[0].update(command_word='Define',mark_tariff=1)
  parts[3].update(command_word='Compare',mark_tariff=1,credit_requirement='From the supplied curves, identify the powder as initially faster (1); both reach 48 cm³ so the prompt asks only for the rate comparison.')
  from practical_data import DATA
  task['stimulus_specification']=DATA['6']
 if topic=='8':
  parts[0]['command_word']='State'
  parts[3].update(command_word='Suggest',mark_tariff=2,blooms_level='Apply',credit_requirement='Suggest cleaning the wire and repeating (1), to distinguish persistent lilac potassium colour from yellow contamination (1).')
 if topic in ['3','7','11']:
  task['response_format']='free_response'
  task['learner_presentation']='Present one continuous prompt without lettered scaffolding; internal credit groups below are for the marker, not separate learner questions.'
  task['free_response_prompt']={
   '3':'Describe how soap removes grease. Explain what biodegradability means for environmental persistence. Given that soap forms scum in hard water while detergent does not, explain which cleans more efficiently under those conditions.',
   '7':'Describe preparation of copper(II) sulfate crystals from copper(II) oxide and dilute sulfuric acid, explaining the separation steps. Given soluble silver nitrate and sodium chloride, explain how to isolate a washed silver chloride precipitate.',
   '11':'Describe how washing soda softens hard water. Explain how sulfur dioxide contributes to acid rain. For a proposed higher-pressure Haber plant, explain the yield advantage and one practical cost.'}[topic]
  # Remove isolated recall anchor; free responses credit connected descriptions and reasons.
  task['parts']=parts[1:]
  for i,p in enumerate(task['parts'],1):p['part']='credit-group-'+str(i)
