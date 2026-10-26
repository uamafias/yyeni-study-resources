"""Objective-specific answer shapes, calculation variants and tariff provenance."""
import re
from collections import Counter

# Context, supported answer, tariff. Constants are supplied to the learner.
MOLES={
 '4.2-01':[
 ('2Mg + O2 → 2MgO; 4.8 g Mg, Ar(Mg)=24, Ar(O)=16. Find MgO mass.','4.8/24 = 0.200 mol; 0.200 × 40 = 8.00 g MgO.',3),
 ('2Mg + O2 → 2MgO; 10.0 g MgO. Find the mass of Mg required.','10.0/40 = 0.250 mol MgO; 0.250 × 24 = 6.00 g Mg.',3),
 ('CaCO3 → CaO + CO2; 25.0 g pure CaCO3; Mr values 100 and 56. Find CaO mass.','25.0/100 = 0.250 mol; 0.250 × 56 = 14.0 g CaO.',3),
 ('2H2 + O2 → 2H2O; 3.2 g O2 with excess H2; Mr(O2)=32 and Mr(H2O)=18. Find water mass.','3.2/32 = 0.100 mol O2; water amount 0.200 mol; mass 3.60 g.',3)],
 '4.2-02':[
 ('Find acid moles in 40.0 cm³ of 0.150 mol/dm³ acid.','40.0/1000 = 0.0400 dm³; 0.150 × 0.0400 = 0.00600 mol.',3),
 ('0.0100 mol solute occupies 25.0 cm³. Find concentration; diagnose using 25 as dm³.','25.0/1000 = 0.0250 dm³; 0.0100/0.0250 = 0.400 mol/dm³. Using 25 gives a result 1000 times too small.',3),
 ('25.0 cm³ of 0.100 mol/dm³ NaOH reacts 1:1 with 0.200 mol/dm³ HCl. Find acid volume.','NaOH amount 0.00250 mol; acid volume 0.00250/0.200 = 0.0125 dm³ = 12.5 cm³.',3),
 ('Mix 20.0 cm³ 0.100 mol/dm³ HCl and 25.0 cm³ 0.100 mol/dm³ NaOH; ratio 1:1; Mr(NaCl)=58.5. Find limiting reagent and salt mass.','Acid amount 0.00200 mol; alkali 0.00250 mol; HCl limits; 0.00200 × 58.5 = 0.117 g NaCl.',3)],
 '4.2-03':[
 ('At room conditions, find volume of 0.250 mol gas; molar volume 24 dm³/mol.','0.250 × 24 = 6.00 dm³.',2),
 ('At room conditions, 120 cm³ of gas is collected. Find amount using 24 dm³/mol.','120/1000 = 0.120 dm³; 0.120/24 = 0.00500 mol.',3),
 ('2.50 g CaCO3, Mr=100, forms CO2 in a 1:1 ratio. Find gas volume at room conditions.','2.50/100 = 0.0250 mol; 0.0250 × 24 = 0.600 dm³.',3),
 ('N2 + 3H2 → 2NH3. With excess hydrogen, compare 1.20 dm³ nitrogen and ammonia volumes at the same conditions.','The volume ratio is 1:2, giving 2.40 dm³ NH3.',2)],
 '4.2-04':[
 ('Find empirical formula from 40.00% C, 6.67% H and 53.33% O; Ar 12,1,16.','Approximate amount ratio 3.333:6.67:3.333; simplest ratio 1:2:1; CH2O.',3),
 ('0.480 g Mg combines with 0.320 g O; Ar 24 and 16. Find empirical formula.','Amounts 0.0200 and 0.0200 mol; ratio 1:1; MgO.',3),
 ('Find empirical formula from 52.17% C, 13.04% H and 34.78% O.','Amount ratio approximately 2:6:1 after dividing by the smallest; C2H6O.',3),
 ('Find empirical formula from 54.55% C, 9.09% H and 36.36% O.','Amount ratio approximately 2:4:1; C2H4O.',3)],
 '4.2-05':[
 ('Empirical formula CH2O, molecular Mr 180; Ar 12,1,16. Find molecular formula.','Empirical Mr 30; 180/30 = 6; C6H12O6.',3),
 ('Empirical formula CH2, molecular Mr 56. Find molecular formula.','Empirical Mr 14; 56/14 = 4; C4H8.',3),
 ('Empirical formula NO2, molecular Mr 92; Ar(N)=14. Find molecular formula.','Empirical Mr 46; 92/46 = 2; N2O4.',3),
 ('Empirical formula CH, molecular Mr 78. Find molecular formula.','Empirical Mr 13; 78/13 = 6; C6H6.',3)],
 '4.2-06-01':[
 ('Calculate calcium percentage in CaCO3; Ar 40,12,16.','40/100 × 100 = 40.0%.',2),
 ('Calculate nitrogen percentage in NH4NO3; Ar 14,1,16.','28/80 × 100 = 35.0%.',2),
 ('Calculate nitrogen percentage in (NH4)2SO4; Ar(S)=32.','28/132 × 100 ≈ 21.2%.',2),
 ('Calculate oxygen percentage in MgO; Ar 24 and 16.','16/40 × 100 = 40.0%.',2)],
 '4.2-06-02':[
 ('Theoretical yield 10.0 g; actual yield 8.00 g. Find percentage yield.','8.00/10.0 × 100 = 80.0%.',2),
 ('Theoretical yield 5.60 g; actual yield 4.76 g. Find percentage yield.','4.76/5.60 × 100 = 85.0%.',2),
 ('At 75.0% yield, 9.00 g product is recovered. Find theoretical yield.','9.00/0.750 = 12.0 g.',2),
 ('25.0 g CaCO3 forms CaO; Mr 100 and 56. Actual CaO mass is 11.2 g. Find percentage yield.','Theoretical CaO mass 14.0 g; 11.2/14.0 × 100 = 80.0%.',3)],
 '4.2-06-03':[
 ('A 15.0 g sample contains 12.0 g pure material. Find percentage purity.','12.0/15.0 × 100 = 80.0%.',2),
 ('A 5.00 g sample contains 4.25 g pure material. Find percentage purity.','4.25/5.00 × 100 = 85.0%.',2),
 ('A 20.0 g sample is 90.0% pure. Find pure material mass.','20.0 × 0.900 = 18.0 g.',2),
 ('A 10.0 g limestone sample produces 1.92 dm³ CO2 at room conditions. CaCO3:CO2 ratio 1:1, Mr=100. Find purity.','1.92/24 = 0.0800 mol; CaCO3 mass 8.00 g; 8.00/10.0 × 100 = 80.0%.',3)],
}

def detail_slots(order,registry,evidence,framework):
    byid={o['objective_id']:o for o in registry}
    words={w['word']:w for w in framework['command_words']}
    repetitions=Counter()
    anchored=set()
    for slot in order['item_slots']:
        objective=byid[slot['objective_id']];text=objective['learner_objective'];raw=objective['syllabus_text']
        st=slot['subtype'];word=slot['command_word'];key=objective['objective_id'].removeprefix('OBJ-6117-')
        drawing=objective['objective_type']=='chem_diagram' and st=='APP'
        if drawing:
            word=next((w for w in objective['command_words'] if w in ['Draw','Sketch']), 'Draw')
            slot['command_word']=word
            slot['representation_task']=True
        own=[w for w in objective['command_words'] if w in words and words[w]['use_in_prompts']]
        if own and objective['objective_id'] not in anchored and not (drawing and own[0] not in ['Draw','Sketch']):
            word=own[0];slot['command_word']=word
            anchored.add(objective['objective_id'])
        pair=(objective['objective_id'],st);variant=repetitions[pair];repetitions[pair]+=1
        slot['answer_structure_keyword_checks']=slot.pop('marking_guidance_must_name')
        if st=='CALC' and key in MOLES:
            context,answer,marks=MOLES[key][variant]
            slot['mark_tariff']=marks;slot['command_word']='Calculate';word='Calculate'
            slot['variant_spec']={'variant':variant+1,'given_and_required':context,'independently_checked_answer':answer}
            slot['marking_guidance_must_name']=['Select the equation or reacting ratio for this specified calculation.',
              'Show the required numerical substitution'+(' and volume conversion before substitution.' if 'cm³' in context else '.'),
              'Reach this result with the stated unit or formula: '+answer] if marks==3 else ['Show the appropriate relationship and numerical substitution for: '+context,'Give the supported result: '+answer]
            if key=='4.2-02' and variant==1:slot['remediation_evidence_ids']=['ER-6117-2022-19']
        else:
            scope=text.split(' — focus: ')[-1] if ' — focus: ' in text else re.sub(r'^[A-Za-z]+\s+','',text)
            slot['variant_spec']={'variant':variant+1,'scope':scope,'task_distinction':
                'Recall the precise meaning or identity.' if st=='DEF' else
                'Describe observable or structural features of the named target.' if st=='FEATURE' else
                'Explain the chemical relationship or sequence for the named target.' if st=='MECH' else
                'Construct and label the representation specified by the objective.' if drawing else
                'Apply the target to fresh supplied substances, observations or data.' if st=='APP' else
                'Variant 1: find a direct unknown using a supplied relationship.' if st=='CALC' and variant==0 else
                'Variant 2: reverse the given/unknown relationship or introduce a necessary unit conversion.' if st=='CALC' else
                'Use the stated objective in a fresh task of this subtype.'}
            modal=words[word]['modal_tariff'];slot['mark_tariff']=modal
            if st=='DEF':
                meaning=re.sub(r'^(?:define|state that|state|recall that|recall|name|identify)\s+','',raw,flags=re.I)
                points=[f'For the target “{scope}”, give the precise chemical statement: {meaning}']
            elif drawing:points=[f'Represent the atoms, bonds, charges, apparatus or axes needed for “{scope}”.',f'Label the representation consistently with this source requirement: {raw}']
            elif st=='DIST':points=[f'Identify the distinguishing property or condition in “{scope}”.',f'Apply that distinction to both named alternatives: {raw}']
            elif st=='PROC':points=[f'State the relevant operation or reagent for “{scope}”.',f'Give the ordered next step, observation or endpoint required by: {raw}']
            elif st=='CALC':points=[f'Use the relationship and any required conversion for “{scope}”.',f'Show the numerical result and unit for the specified {slot["variant_spec"]["task_distinction"]}']
            elif st=='MISCON':points=[f'Discriminate the named misconception using its diagnostic: {text}.']
            elif st=='MECH':points=[f'Explain the chemical cause, arrangement or process specified by “{scope}”.',f'Connect that cause to the stated effect or property: {raw}']
            elif st=='INTERP':points=[f'Infer the requested identity, trend or value from fresh supplied evidence for “{scope}”.']
            elif st=='APP':points=[f'Give a justified answer for the supplied new case of “{scope}”, using this chemical requirement: {raw}']
            else:points=[f'Supply the requested {st.lower()} response for “{scope}”, bounded by: {raw}']
            if word=='Plan':
                points=[f'For {scope}: define the independent variable and suitable range.', 'Describe a workable apparatus setup and safe method.', 'Name relevant control variables and how to keep them constant.', 'Specify measurements, instruments and units.', 'Specify repeats and how results will be recorded/processed.', 'Explain how the results answer the investigation question.']
            slot['marking_guidance_must_name']=points[:slot['mark_tariff']]
        slot['answer_requirements']={'assessed_target':text,'answer_shape_template':slot['marking_guidance_must_name'],
            'guidance_status':'fixed_calculation_answer' if st=='CALC' and key in MOLES else 'template_requires_authored_answer',
            'author_must_supply':['Self-contained stimulus/data where needed','Original canonical answer','Explicit credited elements and accepted alternatives','Independently checked numbers and units'],
            'allocation_rule':f"Award at most {slot['mark_tariff']} marks; write the answer and identify each credited element explicitly.",
            'source_of_content':'Syllabus objective '+objective['objective_id'],'source_of_credit_shape':'Observed command/tariff evidence below; not a copied official allocation.'}
        candidates=[e for e in evidence if e.get('mark_tariff')==slot['mark_tariff'] and e.get('command_word','')==word.lower()]
        assert candidates,(word,slot['mark_tariff'])
        slot['tariff_provenance']={'observed_modal_tariff':words[word]['modal_tariff'],'planned_tariff':slot['mark_tariff'],
            'evidence_ids':[e['evidence_id'] for e in candidates[:3]],
            'reason':'Uses the observed modal tariff.' if slot['mark_tariff']==words[word]['modal_tariff'] else 'Uses an observed three-mark staged calculation: relationship/ratio, conversion or substitution, and result. The variant fixes the actual demand.'}
        slot['reason']='Opening command derives from the objective wording.' if word in objective['command_words'] else 'Observed command selected for this secondary task shape; it is not claimed to be the syllabus opening verb.'
    return order
