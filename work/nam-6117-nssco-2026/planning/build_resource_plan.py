"""Run repository contract/work-order generators with Chemistry planning data.

The schema-valid subject profile is extended in memory with slot-plan.json.
Unmeasured individual-outcome exposure uses a conservative full-teaching budget;
it is not relabelled as evidence of no examination. Standard files are untouched.
"""
import json
import sys
from collections import Counter
from pathlib import Path

WORK=Path(__file__).resolve().parents[1]
ROOT=WORK.parents[1]
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/build'))
import make_contract as contracts
import make_work_order as orders
from gates import require_prerequisites
from slot_details import detail_slots
from task_details import detail_tasks
from visual_details import detail_visuals

CONTEXTS={
 '1':'Separate a salt/sand mixture; read instruments, record results and evaluate precision.',
 '2':'Compare conductivity and physical behaviour of ionic, molecular and metallic samples.',
 '3':'Compare water absorption or insulation of familiar building/fibre materials using original data.',
 '4':'Use a titration to connect burette readings, concentration, mole ratio and mass.',
 '5':'Predict and test electrode products in an explicitly aqueous or molten electrolyte with stated electrodes.',
 '6':'Measure gas production against time and plan a fair investigation of one rate variable.',
 '7':'Select and plan preparation of soluble versus insoluble salts, including separation and purification.',
 '8':'Identify unknown ions from complete reagent/observation sequences; contrast solution and precipitate colours.',
 '9':'Compare metal reactivity using a controlled acid reaction, measurements and a defensible conclusion.',
 '10':'Separate and interpret hydrolysis products by chromatography, then plan an extraction/separation method.',
 '11':'Investigate water hardness or purification with controlled volumes and evidence-based conclusions.',
 '12':'Read and process experimental data, interpret a graph, evaluate a method and plan a fair investigation.',
}
# Each tuple fixes command, tariff, AO C criterion and Bloom demand. All tariffs
# occur in the audited written-paper corpus. Every practical activity is 12 marks.
PRACTICAL_PARTS={
 '1':[('State',2,'C3','Apply'),('Draw',2,'C1','Apply'),('Plot',3,'C3','Apply'),('Calculate',2,'C4','Apply'),('Explain',3,'C5','Evaluate')],
 '2':[('Draw',3,'C1','Apply'),('Describe',3,'C3','Apply'),('Explain',3,'C4','Analyse'),('Describe',3,'C5','Evaluate')],
 '3':[('State',2,'C3','Apply'),('Draw',2,'C1','Apply'),('Plot',3,'C3','Apply'),('Calculate',2,'C4','Apply'),('Explain',3,'C5','Evaluate')],
 '4':[('Name',1,'C1','Remember'),('State',2,'C3','Apply'),('Calculate',3,'C4','Apply'),('Calculate',2,'C4','Apply'),('Explain',2,'C5','Evaluate'),('State',2,'C2','Apply')],
 '5':[('Draw',3,'C1','Apply'),('Describe',3,'C3','Apply'),('Deduce',1,'C4','Analyse'),('Explain',2,'C4','Analyse'),('Describe',3,'C2','Create')],
 '6':[('Plot',3,'C3','Apply'),('Calculate',2,'C4','Apply'),('State',1,'C1','Understand'),('Plan',6,'C2','Create')],
 '7':[('Describe',3,'C1','Apply'),('State',2,'C3','Apply'),('Explain',1,'C4','Analyse'),('Plan',6,'C2','Create')],
 '8':[('Describe',3,'C3','Apply'),('Deduce',1,'C4','Analyse'),('Describe',3,'C3','Apply'),('Explain',3,'C4','Analyse'),('State',2,'C1','Understand')],
 '9':[('Describe',6,'C2','Create'),('Calculate',2,'C4','Apply'),('State',2,'C3','Apply'),('Explain',2,'C5','Evaluate')],
 '10':[('Plan',6,'C2','Create'),('State',2,'C3','Apply'),('Calculate',2,'C4','Apply'),('Explain',2,'C5','Evaluate')],
 '11':[('Plan',6,'C2','Create'),('Draw',2,'C1','Apply'),('State',2,'C3','Apply'),('Explain',2,'C4','Analyse')],
 '12':[('Plot',3,'C3','Apply'),('Calculate',2,'C4','Apply'),('State',1,'C1','Understand'),('Plan',6,'C2','Create')],
}
VISUALS={
 '1':['apparatus scale with readable divisions','filtration and distillation setups','table-to-graph axes and read-off'],
 '2':['particle arrangements and shell diagrams','dot-and-cross bonds with full relevant outer shells','four molecular shapes','diamond graphite and metallic lattice'],
 '3':['soap head/tail orientation around grease','nano-size comparison','materials comparison apparatus'],
 '4':['mole-conversion route with unit changes','burette meniscus and readings'],
 '5':['labelled electrolytic cell with polarity','active versus inert electrode comparison'],
 '6':['fully labelled energy profile','rate curves with distinct endpoints/gradients','closed-system equilibrium diagram'],
 '7':['pH scale and indicator colours','salt preparation separation sequence'],
 '8':['qualitative-test observation matrix','precipitate versus resulting solution sequence','gas and flame-test apparatus'],
 '9':['blast furnace essential reactions','metal/alloy particle models','reactivity comparison setup'],
 '10':['displayed structures and functional groups','ester amide and carbohydrate linkages','polymer repeating units','chromatogram baseline solvent front and spots'],
 '11':['water purification stages','fractional distillation of liquid air','Haber/Contact essential-condition flow diagrams'],
 '12':['readable thermometer burette and cylinder scales','original graph with plotting and read-off rubric','investigation setup with controls and measurements'],
}


def enrich(order,registry):
    topic=order['topic_id'];branch=[o for o in registry if o.get('parent_id') and o['topic_id']==topic]
    available={w['word']:w for w in json.loads((WORK/'curriculum/assessment-framework.json').read_text())['command_words']}
    visuals=[{'visual_id':f'VIS-6117-{topic}-{i:02d}','purpose':purpose,
              'planned_file':f'topics/{topic}/visuals/VIS-6117-{topic}-{i:02d}.svg',
              'requirements':['Original scientifically accurate drawing','Readable labels, units and charge/bond notation where relevant','Alt text explaining its teaching purpose']}
              for i,purpose in enumerate(VISUALS[topic],1)]
    visuals=detail_visuals(visuals,topic)
    specifications=[]
    for slot in order['item_slots']:
        slot['answer_requirements']={'target':slot['objective_title'],'shape':slot['marking_guidance_must_name'],
            'credit_rule':f"Allocate exactly {slot['mark_tariff']} marks to distinct supported elements; independently check any arithmetic.",
            'originality':'Write new learner-facing wording and a fresh example; do not copy an internal source answer.'}
        slot['required_visual_ids']=[v['visual_id'] for v in visuals] if any(o['objective_id']==slot['objective_id'] and o['objective_type']=='chem_diagram' for o in registry) else []
    evidence=json.loads((WORK/'assessment-evidence/assessment_evidence.json').read_text())['records']
    framework=json.loads((WORK/'curriculum/assessment-framework.json').read_text())
    order=detail_slots(order,registry,evidence,framework)
    misconceptions={e['entry_id']:e for e in json.loads((WORK/'curriculum/misconceptions.json').read_text())['entries']}
    for slot in order['item_slots']:
        if slot['subtype']=='MISCON':
            entry=misconceptions[slot['misconception_entry']]
            slot['marking_guidance_must_name']=[f"Reject the recorded confusion: {entry['a']} Apply this diagnostic to demonstrate the correct distinction: {entry['test']}"]
            slot['answer_requirements']['answer_shape_template']=slot['marking_guidance_must_name']
    for task in order['performance_tasks']:
        kind=task['item_type'];paper='1' if kind=='multiple_choice_set' else '2' if kind in ['short_answer','calculation'] else '3'
        eligible=[o for o in branch if paper in o['papers']]
        focus={'1':['1.5','1.2.2','1.4'],'2':['2.4.2','2.4.3','2.4.5'],'3':['3.2','3.3'],'4':['4.2'],
               '5':['5.1'],'6':['6.4'],'7':['7.3','7.4'],'8':['8.1'],'9':['9.2'],'10':['10.8.2'],
               '11':['11.1.2'],'12':['12.3','12.5','12.4']}[topic]
        selected=[o for o in eligible if o['sub_topic'] in focus] if kind=='practical_task' else eligible
        task['objective_ids']=[o['objective_id'] for o in (selected or eligible)[:4]]
        if kind=='practical_task':
            fixed={'1':['1.5-05-01','1.2.2-02','1.4-05'],
              '2':['2.4.2-05','2.4.3-10','2.4.5-02'],'3':['3.2-01','3.2-02','3.1-02'],
              '4':['4.2-02','4.1-08'],'5':['5.1-02','5.1-03','5.1-05-04','5.1-07'],
              '6':['6.4-08','6.4-09','6.4-05-01','6.4-01'],'7':['7.4-01','7.4-03','7.3-04'],
              '8':['8.1-01-05','8.1-01-03','8.1-01-14','8.1-01-15'],'9':['9.2-01','9.2-02'],
              '10':['10.8.2-04','10.8.2-07','10.8.2-08'],
              '11':['11.1.2-02','11.1.2-04','11.1.2-07','11.1.2-08'],
              '12':['12.3-03','12.3-04','12.4-01','12.5-01']}[topic]
            task['objective_ids']=['OBJ-6117-'+x for x in fixed]
            assert all(any(o['objective_id']==x for o in registry) for x in task['objective_ids']),task
        task['paper_id']=paper
        if kind=='multiple_choice_set':
            task['mark_tariff']=orders.MCQ_N;task['assessment_objectives']=[];task['ao_split']={}
            task['parts']=[{'part':str(i),'command_word':'State','mark_tariff':1,'assessment_objectives':[],'blooms_level':'Understand'} for i in range(1,orders.MCQ_N+1)]
            task['answer_requirements']=['A key for every question','Reason the key is correct','A named chemical error behind each distractor','AO and cognitive demand are assigned from each target and task brief; no positional quota is applied.']
        elif kind=='short_answer':
            task['mark_tariff']=8;task['assessment_objectives']=['A','B'];task['ao_split']={'A':5,'B':3}
            task['parts']=[{'part':chr(97+i),'command_word':word,'mark_tariff':marks,'assessment_objectives':[ao],'blooms_level':bloom}
                for i,(word,marks,ao,bloom) in enumerate([('State',1,'A','Remember'),('Describe',2,'A','Understand'),('Explain',2,'A','Understand'),('Explain',3,'B','Apply')])]
            task['answer_requirements']=['An original linked context in this topic','Four separately marked answers following the fixed AO split','Credit-worthy points and accepted alternatives','Supply every needed figure or diagram; no external question reference']
            theory={'1':['1.3-02','1.3-03','1.5-03','1.5-06'],'2':['2.1.2-09','2.4.2-01','2.4.3-10'],
                '3':['3.3-01','3.3-02','3.3-05','3.3-06'],'4':['4.1-08','4.2-02'],
                '5':['5.1-03','5.1-05-04','5.1-07'],'6':['6.4-01','6.4-05-01','6.4-09'],
                '7':['7.3-01','7.3-04','7.4-03'],'8':['8.2-01-01','8.2-01-02','8.2-01-05','8.1-01-10'],
                '9':['9.2-01','9.2-02','9.4-08'],'10':['10.2.2-01','10.4-04','10.7-01'],
                '11':['11.1.2-02','11.1.2-07','11.4-03','11.5-05']}[topic]
            task['objective_ids']=['OBJ-6117-'+x for x in theory]
            task['context_brief']={'1':'A salt/water sample is tested for purity and separated; interpret units and select a separation method.',
                '2':'Use supplied proton/electron counts and conductivity observations to distinguish atomic structure, ionic bonding and molecular properties.',
                '3':'Compare a soap and detergent used on greasy material and their environmental consequences.',
                '4':'Compare two acid solutions before and after dilution and connect concentration to a neutralisation context.',
                '5':'Compare electrolysis under named electrolyte states and active/inert electrode conditions.',
                '6':'Compare calcium carbonate lumps and powder reacting with acid using supplied rate observations.',
                '7':'Choose starting materials and separation methods for copper(II) sulfate and silver chloride.',
                '8':'Identify ammonia, carbon dioxide and oxygen from gas tests; recognise a potassium flame. No wet-ion tests in this Paper 2 task.',
                '9':'Compare a metal reactivity test with choices for protecting an iron object from corrosion.',
                '10':'Connect ethene, ethanol and an ester through functional groups and characteristic reactions.',
                '11':'A water-treatment context links hardness, softening and acidic industrial pollution to the relevant chemistry.'}[topic]
        elif kind=='calculation':
            task['objective_ids']=['OBJ-6117-4.2-02','OBJ-6117-4.2-03'] if topic=='4' else ['OBJ-6117-6.2-04','OBJ-6117-6.2-05']
            task['context_brief']='25.0 cm³ of 0.200 mol/dm³ HCl reacts with excess sodium carbonate in a 2:1 ratio; find acid amount and room-condition CO2 volume using 24 dm³/mol.' if topic=='4' else 'Compare a 100 g water sample heated by 8.0 °C (c=4.2 J/g/°C) with a separate H2+Cl2→2HCl bond-energy calculation (436,243,431 kJ/mol).'
            task['checked_answer']='n(HCl)=0.00500 mol; n(CO2)=0.00250 mol; V(CO2)=0.0600 dm³=60.0 cm³.' if topic=='4' else 'q=100×4.2×8.0=3360 J; ΔH=436+243−2×431=−183 kJ/mol.'
            task['mark_tariff']=5;task['assessment_objectives']=['A','B'];task['ao_split']={'A':1,'B':4}
            task['parts']=[{'part':chr(97+i),'command_word':word,'mark_tariff':marks,'assessment_objectives':[ao],'blooms_level':'Remember' if ao=='A' else 'Apply'}
                           for i,(word,marks,ao) in enumerate([('State',1,'A'),('Calculate',2,'B'),('Calculate',2,'B')])]
            task['answer_requirements']=['One relevant formula/relationship mark','Two independently marked calculation stages','Show conversion, substitution, intermediate values, final unit and appropriate rounding','State follow-through rules without copying a report answer']
            task['required_visual_ids']=[v['visual_id'] for v in visuals[:1]]
        else:
            task['mark_tariff']=12;task['assessment_objectives']=['C'];task['ao_split']={'C':12};task['context_brief']=CONTEXTS[topic]
            task['parts']=[{'part':chr(97+i),'command_word':word,'mark_tariff':marks,'assessment_objectives':['C'],'practical_criterion':criterion,'blooms_level':bloom}
                for i,(word,marks,criterion,bloom) in enumerate(PRACTICAL_PARTS[topic])]
            task['answer_requirements']=['Original realistic data/observations and an appropriate labelled apparatus or graph visual','Worked calculations, units and numerical tolerance where relevant','Separate plotting/curve/read-off criteria rather than an undifferentiated graph mark','For six-mark planning: setup, controls, measurements and conclusion; state alternatives and any thresholds','For tests: reagent, initial observation, excess-reagent behaviour and final solution colour where applicable','Describe activities on paper; do not imply unsupervised hazardous experiments']
            task['required_visual_ids']=[v['visual_id'] for v in visuals]
        assert sum(p['mark_tariff'] for p in task['parts'])==task['mark_tariff']
        for index,part in enumerate(task['parts']):
            assert part['mark_tariff'] in available[part['command_word']]['observed_tariffs'],part
            if kind=='multiple_choice_set':
                pool=eligible  # coverage selection is independent of AO and part position
                target=pool[(index*len(pool))//len(task['parts']) % len(pool)]
                part['objective_ids']=[target['objective_id']]
                part['content_target']=target['learner_objective']
            else:
                part['objective_ids']=[task['objective_ids'][index%len(task['objective_ids'])]]
                part['content_target']=next(o['learner_objective'] for o in registry if o['objective_id']==part['objective_ids'][0])
                if kind=='practical_task':
                    criterion=part['practical_criterion'];skill={'C1':'12.2-01','C2':'12.5-01','C3':'12.1-01','C4':'12.3-02','C5':'12.4-01'}[criterion]
                    part['objective_ids']=list(dict.fromkeys(part['objective_ids']+['OBJ-6117-'+skill]))
            part['credit_requirement']=f"{part['command_word']} task targeting: {part['content_target']}. Allocate {part['mark_tariff']} marks to the stated answer components; provide a fully worked original answer."
        task['objective_ids']=list(dict.fromkeys(oid for p in task['parts'] for oid in p['objective_ids']))
        specifications.append(task)
    order['visual_requirements']=visuals
    order=detail_tasks(order,registry)
    marks=Counter()
    for slot in order['item_slots']:
        for ao in slot['assessment_objectives']:marks[ao]+=slot['mark_tariff']/len(slot['assessment_objectives'])
    for task in order['performance_tasks']:marks.update(task['ao_split'])
    total=sum(marks.values())
    order['planned_ao_marks']=dict(marks)
    order['marks_equivalent_total']=total
    order['planned_ao_mix_by_marks']={ao:{'planned_share_percent':round(100*marks.get(ao,0)/total),
        'syllabus_weight_percent':weight} for ao,weight in [('A',50),('B',30),('C',20)]}
    return order,specifications


def main():
    require_prerequisites(str(WORK))
    contracts.WORDS_BY_EXPOSURE['unmeasured']=(230,330)
    contracts.ITEMS_BY_EXPOSURE['unmeasured']=4
    contracts.build(str(WORK),force=True)
    extension=json.loads((WORK/'planning/slot-plan.json').read_text())
    original=orders._yaml
    active_topic=None
    def profile(path):
        data=original(path)
        if Path(path).name=='subject-profile.yaml':
            slot=json.loads(json.dumps(extension['slot_plan']))
            slot['performance_tasks']+=extension.get('additional_performance_by_topic',{}).get(active_topic,[])
            data.update({'slot_plan':slot})
        return data
    orders._yaml=profile
    topics=sorted([p.name for p in (WORK/'topics').iterdir() if (p/'contract.json').exists()],key=lambda x:int(x))
    registry=json.loads((WORK/'curriculum/objective_registry.json').read_text())['objectives']
    all_tasks=[];all_visuals=[]
    for topic in topics:
        active_topic=topic
        order=orders.build(str(WORK),topic)
        order,specifications=enrich(order,registry)
        all_tasks.extend(specifications);all_visuals.extend(order['visual_requirements'])
        td=WORK/'topics'/topic
        (td/'work_order.json').write_text(json.dumps(order,indent=2,ensure_ascii=False)+'\n')
        (td/'work_order.md').write_text(orders.as_markdown(order))
        print(topic,order['assessable_objective_count'],order['planned_item_count'],order['planned_ao_mix_by_marks'])
    rows,share,weights,missing,grand=orders.subject_rollup(str(WORK),topics)
    exact=Counter()
    for topic in topics:
        exact.update(json.loads((WORK/'topics'/topic/'work_order.json').read_text())['planned_ao_marks'])
    grand=sum(exact.values())
    share={ao:round(100*exact.get(ao,0)/grand) for ao in weights}
    orders.write_rollup(str(WORK),rows,share,weights,missing,grand)
    (WORK/'planning/activity-specifications.json').write_text(json.dumps({'tasks':all_tasks},indent=2,ensure_ascii=False)+'\n')
    (WORK/'planning/visual-manifest.json').write_text(json.dumps({'status':'required_assets_not_yet_authored','visuals':all_visuals},indent=2,ensure_ascii=False)+'\n')
    print('SUBJECT',share,'largest gap',max(abs(share[k]-weights[k]) for k in share),'marks',grand)


if __name__=='__main__':main()
