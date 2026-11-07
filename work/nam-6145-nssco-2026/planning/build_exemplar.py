"""Original structural exemplar in an isolated workspace; main topics remain unauthored."""
import hashlib
import json
import shutil
import sys
from pathlib import Path
import yaml
WS=Path(__file__).resolve().parents[1]
ROOT=WS.parents[1]
EX=WS/'exemplar'
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text
def write(path,x):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
for folder in ('curriculum','assessment-evidence'):
    (EX/folder).mkdir(parents=True,exist_ok=True)
    for file in (WS/folder).glob('*.json'):
        shutil.copy2(file,EX/folder/file.name)
for file in ('qualification-profile.yaml','subject-profile.yaml'):
    shutil.copy2(WS/file,EX/file)
TD=EX/'topics/1.1';TD.mkdir(parents=True,exist_ok=True)
for file in ('contract.json','work_order.json','work_order.md'):
    shutil.copy2(WS/'topics/1.1'/file,TD/file)
wo=json.loads((TD/'work_order.json').read_text())
O=['OBJ-6145-1.1-01','OBJ-6145-1.1-02','OBJ-6145-1.1-03']
claims=[]
specs=[
 (O[0],'Scarcity exists because available resources cannot satisfy the wants competing for them.','definition'),
 (O[0],'A plentiful stock of a finished product does not remove the scarcity of land, labour, capital and time used to produce it.','misconception_correction'),
 (O[1],'Opportunity cost is the value of the next-best feasible alternative forgone.','definition'),
 (O[1],'The alternative forgone can be a non-monetary benefit, such as study time, recreation or forgone output along a production possibility frontier with given resources and technology.','factual'),
 (O[2],'Comparing the selected benefit with the next-best alternative makes the sacrifice behind a choice explicit.','causal'),
 (O[2],'A justified choice depends on the decision-maker’s objective, constraints and the relative benefits of feasible alternatives.','evaluative'),
 (O[2],'New information about the value or feasibility of the alternative can change a reasoned decision.','evaluative'),
]
for i,(oid,text,kind) in enumerate(specs,1):
    claims.append({'claim_id':f'CLM-6145-1.1-{i:03}','objective_ids':[oid],'text':text,'claim_type':kind,
     'provenance':'generated_quality','evidence':[{'source_id':'NIED-6145-2018','locator':'PDF page 8, topic 1.1','support_type':'derivation'}],
     'derived_from_claim_ids':[],'verification':{'status':'unverified','method':'Original exemplar teaching statements; semantic review pending.','reviewer_id':None,'reviewed_at':None,'confidence':0.95},
     'publishable':False,'revision':1})
write(TD/'claims/canonical_claim_ledger.json',{'ledger_id':'LEDGER-6145-1.1-EXEMPLAR','claims':claims})
C=[c['claim_id'] for c in claims]
def stamp(x):
    x['claims_seen']={cid:1 for cid in x.get('claim_ids',[])}
    x['authored_hash']=hashlib.sha256(_artefact_text(x).encode()).hexdigest()
    return x
paragraphs=[
 ('definition','Why choices arise',
  'Scarcity exists because available resources cannot satisfy the wants competing for them. A school may want more library books, a shaded playground and additional computers. Its budget, available rooms and staff time restrict what can be provided during the year. The economic problem is therefore a problem of choosing between competing uses of resources. Having a positive bank balance does not remove it. A larger budget increases the feasible choices, but the school can still face further wants that its resources cannot meet. Scarcity describes this relationship between resources and wants, rather than simply describing poverty.',C[:2]),
 ('misconception','A full shelf can still involve scarce resources',
  'Imagine a bakery with bread left on its shelves at closing time. The unsold bread does not prove that resources are unlimited. The bakery used flour, workers’ time, equipment and electricity to make it. Those resources could have been used for other production. Some bread may be unwanted at the price charged even though the resources used in producing it have alternative uses. To test whether the economic problem remains, ask whether competing uses still exist for the available resources. Do not use the number of finished products on display as the test of scarcity.',C[:2]),
 ('comparison','The next-best alternative',
  'Opportunity cost is the value of the next-best feasible alternative forgone. Start by identifying the decision-maker and what has actually been chosen. Next identify the best available alternative that the decision rules out. Other rejected alternatives are not added together. A learner deciding between an hour of revision, an hour of football and an hour of music practice gives up the most valued alternative to the selected activity. If revision is selected and football is the next-best option, the opportunity cost is the benefit of that football session. Money need not change hands for an opportunity cost to exist. In an invented Windhoek garden, fixed resources can produce weekly combinations of bean and tomato crates (0,12), (2,8), (4,4) and (6,0). Plot beans horizontally and tomatoes vertically, both in crates per week, and connect the four efficient combinations. Moving from (2,8) to (4,4) gives two more bean crates but sacrifices four tomato crates: two tomato crates per extra bean crate. This is a movement along a straight production possibility frontier, with constant opportunity cost, given resources and technology.',C[2:4]),
 ('worked_application','A community room',
  'Use these invented teaching data. The fictional Otjomuise community group in Windhoek has a N$600 room budget and one room available on Saturday afternoon. It must choose between a reading club and an art workshop, which cannot run together. The group ranks the reading club first and the art workshop second. Choosing the reading club means giving up the benefits of the art workshop. Those workshop benefits are the opportunity cost. The room hire bill is a separate money payment and is not automatically the value of the alternative activity. If another room becomes available without displacing any other activity, the feasible options change, so the original opportunity-cost comparison must be reconsidered.',C[2:4]+C[6:]),
 ('analysis_chain','How recognising the sacrifice helps',
  'Consider an invented neighbourhood committee choosing how to use a plot of land. It prefers a vegetable garden, while a shaded meeting area is the next-best feasible use. Recognising the forgone meeting space forces the committee to examine who gains and who loses from the garden decision. Food production may benefit participating households, but residents who need a meeting place lose that particular use of the plot. A committee that states both benefits can explain its priority more clearly. Recognising opportunity cost improves the comparison; it does not by itself decide which benefit should receive the greater weight.',C[4:]),
 ('evaluation','A decision needs a stated objective',
  'Suppose a learning centre can use a small room for either an additional reading group or a computer-skills group. Staff time allows one group this term. Its stated priority is to support learners who struggle with reading. There are applicants for both groups. The case for the reading group is that it serves the chosen priority directly. The case against it is the computer learning forgone by the other applicants. The reading choice is defensible if the reading need is more urgent under the centre’s stated objective. It could be reconsidered if a new volunteer can run the computer group at another time without reducing the reading support.',C[4:]),
 ('plain_explanation','Feasibility, value and new information',
  'A rejected option must be feasible before it can be the next-best alternative. A family cannot give up a holiday that its budget could not finance in the first place. Its relevant alternatives may instead be repairing a bicycle, buying school equipment or retaining money for a later purchase. The family needs to state which of those feasible alternatives it values most. New information may change that ranking. If the bicycle is essential for travelling to school, repairing it may become more urgent. A sound explanation identifies the changed condition and then shows why the preferred choice changes.',C[2:]),
 ('plain_explanation','Keeping the comparison fair',
  'Compare alternatives over the same period and using the same available resources. A weekly activity should not be compared with an annual benefit without explaining the difference in time. Likewise, an option requiring extra staff is not directly comparable with one that fits the existing staff allocation. State the constraint before judging the sacrifice. This helps separate a genuine change in preferences from a change in what the decision-maker can actually achieve.',C[4:]),
 ('cross_link','Where the idea leads',
  'Topic 1.2 considers the resources being allocated and the systems through which allocation occurs. Topic 6.2 applies choices to government policy, while topic 9.1 examines conflicts between different interests and different time horizons. The opportunity-cost method remains the same: identify the selected use, identify the next-best feasible alternative, and explain the benefit forgone. Later topics add detail about the people affected and the mechanisms connecting the decision to its consequences. Keeping that basic comparison clear makes those later explanations more precise.',C[2:]),
]
blocks=[]
for i,(kind,heading,text,cids) in enumerate(paragraphs,1):
    blocks.append(stamp({'block_id':f'EX-1.1-B{i:02}','block_type':kind,'heading':heading,'text':text,
                         'claim_ids':cids,'context_tags':['Namibia','invented teaching examples'],'assessment_objectives':['A','B','C']}))
n=sum(len(b['text'].split()) for b in blocks)
write(TD/'content-units/CU-6145-1.1.json',{'unit_id':'CU-6145-1.1','title':'Scarcity, choice and opportunity cost',
    'objective_ids':O,'level':'NSSCO','core_status':'core','objective_type':'economics_concept','depth_tier':4,
    'word_budget':{'min':820,'target':1100,'max':1300},'word_count':n,'blocks':blocks,'qa_status':'review_required'})

content={
 'DIAGRAM':('Explain opportunity cost using these invented production possibilities for the fictional Otjomuise school garden in Windhoek. With its fixed land and labour it can grow weekly combinations (bean crates, tomato crates): (0,12), (2,8), (4,4), (6,0). Plot beans horizontally and tomatoes vertically. Explain the movement from (2,8) to (4,4), assuming efficient use and unchanged resources and technology.', 'Label both axes in crates per week, plot all four points and connect the linear frontier. Moving from two to four bean crates sacrifices four tomato crates. Each extra bean crate costs two tomato crates over this interval. This is a movement along the frontier with unchanged productive capacity, illustrating the next-best feasible output forgone, not a shift of the frontier.', C[2:4]),
 'DEF':('Define scarcity.','Available resources are insufficient to satisfy the competing wants for them.',C[:1]),
 'FEATURE':('Identify the two features that together create the basic economic problem.','Resources are limited; wants competing for them exceed what those resources can satisfy.',C[:1]),
 'MISCON':('Explain why a shop with unsold notebooks can still operate in an economy facing scarcity.','Unsold notebooks do not establish unlimited resources. The paper, labour and time used have alternative uses; the test is whether resources can satisfy competing wants.',C[:2]),
 'DIST':('Explain the difference between opportunity cost and adding together every rejected option.','Opportunity cost concerns the next-best feasible alternative. Adding every rejected option counts sacrifices that could not all have been chosen instead.',C[2:4]),
 'APP':('Explain the opportunity cost when a learner chooses revision rather than a football session, with football ranked as the next-best feasible activity.','The opportunity cost is the benefit forgone from the football session, because it is the next-best feasible use of that time.',C[2:4]),
 'BEN':('Explain how identifying the opportunity cost of using a community plot as a garden can improve the committee’s decision, when the next-best use is a shaded meeting space.','The committee identifies the garden benefit, identifies the forgone meeting-space benefit, compares the needs of affected residents, and can explain which objective determines its decision.',C[4:]),
 'LIM':('Explain why recognising the opportunity cost does not settle whether a learning centre should run a reading group or a computer-skills group when it can run one.','Both groups have valued benefits. Identifying the forgone group exposes the sacrifice but does not rank its value. The centre must choose its priority and judge the urgency of each need under that priority.',C[4:]),
 'EVAL':('Evaluate a learning centre’s choice to use its room for reading support. It can run either reading support or computer skills this term, has applicants for both, and its stated priority is learners struggling with reading.','Reading support directly serves the stated priority. Computer learning is nevertheless forgone, so the rejected group has a real opportunity cost. Reading support is justified if the reading need is more urgent under that priority. An additional volunteer able to run computer skills at another time could change the feasible choices and therefore the judgement.',C[4:]),
}
items=[]
def item(iid,oids,cids,kind,subtype,aos,bloom,cw,marks,prompt,answer,parts):
    rubric={
     'DEF':['Meaning and essential element (1): resources cannot satisfy the competing wants; credit only the complete relationship.'],
     'FEATURE':['Characteristic (1): resources are limited. Distinction/example (1): wants exceed what those resources can satisfy; no duplicate credit.'],
     'DIST':['Difference (1): opportunity cost is the next-best feasible alternative. Contrast/test (1): exclude the sum of all rejected alternatives because only one can be the next-best option.'],
     'APP':['Context (1): identify the benefit of the stated football session. Conclusion/reason (1): it is the next-best feasible alternative forgone because revision was chosen.'],
     'MISCON':['Confusion/boundary (1): unsold goods do not imply unlimited productive resources. Test to distinguish (1): ask whether resources such as labour still have competing uses.'],
     'DIAGRAM':['Axes/labels (1): beans and tomatoes in crates per week. Initial position / original curve (2): all four supplied combinations accurately (1), straight line through them (1). Change/control (1): movement along the existing frontier from (2,8) to (4,4), resources unchanged. Explanation (2): four tomato crates forgone (1), because those resources are reassigned to two extra bean crates (1). Interpretation (1): two tomato crates per extra bean crate; this is the sacrifice along the supplied frontier.'],
     'EVAL':['Argument for/benefit (2): serves urgent reading needs (1) and links the scarce room to the stated priority (1). Argument against/limitation (2): computer learning is forgone (1), reducing access for the waiting computer group (1). Condition/trade-off (1): the relative urgency of reading under the stated objective. Judgement/conclusion (2): choose reading on that priority (1), but reconsider the feasible combination if an additional volunteer and time slot remove this particular sacrifice (1).'],
     'short_answer':['Meaning (2): limited resources (1) relative to competing wants (1). Identification (2): labour making bread (1), with another feasible use (1). Opportunity-cost explanation (2): next-best feasible activity (1), benefit forgone (1). Separate points (2): sports benefit (1), supplied ranking establishes it as next best (1). Marks allocation totals 8.'],
     'data_response':['Context/data description (6): one scarce afternoon (1) and limited staff (1); three desired uses (1); reading chosen (1); computing next-best feasible use (1); computing benefit forgone (1). Mechanism/explanation (7): same resource cannot support both uses (1); reading choice removes computing (1); computing ranks above art (1); computing is feasible (1); its benefit is sacrificed (1); art is not the next-best option (1); adding computing and art incorrectly aggregates mutually exclusive alternatives (1). Both sides and judgement (7): priority supports reading (1), urgent need makes it valuable (1); computer learning has a benefit (1) lost under the old constraint (1); volunteer plus separate time changes feasibility (1); retain reading and add computing if no other valued use is displaced (1); explicitly test that condition before concluding both can run (1). Marks allocation 6+7+7=20.'],
     'essay_plan':['Plan 1 allocation (7): argument for reading serves the priority (1) and targets urgent need (1); argument against loses computer learning (1) and access for waiting applicants (1); condition is relative need (1); judgement chooses reading (1) because that condition fits the stated priority (1). Plan 2 allocation (7): argument for a separate computer group uses the new volunteer (1) and time slot (1); argument against is other demands on volunteer time (1) and room availability (1); condition is no displacement of another valued use (1); judgement supports the revised combination (1) only after checking that condition (1). Total marks 14; no extra conclusion mark.']}
    guidance=rubric[subtype or kind]
    x={'item_id':iid,'objective_ids':oids,'claim_ids':cids,'item_type':kind,'subtype':subtype,'assessment_objectives':aos,
       'difficulty':3,'prompt':prompt,'canonical_answer':answer,'marking_guidance':guidance,
       'context':{'sector':None,'business_size':None,'ownership':None,'situation':'Original Namibian teaching example','facts':['All entities and data are invented teaching examples in Windhoek, Namibia.','The fictional Otjomuise Learning Centre has a room budget of N$600; staffing and room time, rather than the cash budget alone, limit activities.']},
       'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'original_exemplar',
       'qa_status':'review_required','blooms_level':bloom,'command_word':cw,'mark_tariff':marks}
    return stamp(x)
for slot in wo['item_slots']:
    p,a,cids=content[slot['subtype']]
    x=item(slot['slot'],[slot['objective_id']],cids,'flashcard',slot['subtype'],slot['assessment_objectives'],slot['blooms_level'],slot['command_word'],slot['mark_tariff'],p,a,slot['marking_guidance_must_name'])
    if slot.get('misconception_entry'):
        x['misconception_entry']=slot['misconception_entry']
    items.append(x)
perf=[
 ('short_answer','Define scarcity (2). Identify a scarce resource used in producing bread and one alternative use for it (2). Explain opportunity cost (2). Identify a non-monetary sacrifice when a learner chooses revision instead of sport, with sport stated to be the next-best feasible activity (2).',
  'Scarcity relates limited resources to competing wants (2). Labour can make bread or prepare another product (2). Opportunity cost is the next-best feasible alternative forgone (2). The learner gives up the benefit of the sports session, provided sport is the next-best feasible option (2).',['A'],8,'Define'),
 ('data_response','Invented Windhoek teaching data: Otjomuise Learning Centre, with a N$600 room budget, has one available afternoon and sufficient staff for one activity. Its priority ranking is reading support first, computer skills second and art third. Describe the scarcity and choice involved, including opportunity cost (6). Explain why the computer group rather than both rejected activities supplies the opportunity cost (7). Discuss whether choosing reading support remains justified if an additional volunteer can provide computer skills at a different time without reducing reading support (7).',
  'Description: one afternoon and limited staff constrain three desired uses; choosing reading support sacrifices the next-best feasible computer group (6). The same afternoon and staff cannot run reading and computing together. Choosing reading therefore removes computing from the feasible uses of those resources. Computing ranks above art and could have run instead of reading, so its benefit is the next-best feasible sacrifice. Art is lower ranked. Adding both rejected benefits would count activities that could not jointly replace reading under this constraint (7). Discussion: reading meets the stated priority, but computer learning has a value; an additional volunteer and separate time change feasibility. Retain reading while checking that the new arrangement genuinely avoids displacing another valued activity. Develop both sides and justify the decision within seven marks (7).',['A','B','C'],20,'Describe'),
 ('essay_plan','Evaluate two decisions, planning each response rather than writing an essay (7 marks each). Scenario 1: a centre prioritises urgent reading needs and must choose reading or computing with one room. Scenario 2: the same centre has a volunteer and another time slot for computing, without reducing reading support. Compare how the changed constraint affects the argument and judgement.',
  'Plan 1: for reading, direct response to urgent need; against, computing benefits forgone; decisive condition, relative urgency within the centre’s objective; judgement, reading is justified on the stated priority. Develop these into a seven-mark plan. Plan 2: the original room/time constraint has changed; running computing separately may retain both benefits; check other demands on volunteer and room time rather than assume there is no sacrifice anywhere. Judge the revised feasible combination using the updated constraints. Allocate seven marks to this separate plan.',['C'],14,'Evaluate'),
]
sp=yaml.safe_load((EX/'subject-profile.yaml').read_text())
for slot,(kind,prompt,answer,aos,marks,cw) in zip(wo['performance_tasks'],perf):
    items.append(item(slot['slot'],slot['objective_ids'],[c['claim_id'] for c in claims if set(c['objective_ids']) & set(slot['objective_ids'])],kind,None,aos,slot['blooms_level'],cw,marks,prompt,answer,sp['answer_structures'][kind]))
write(TD/'learning-items/topic_1.1_items.json',{'dataset_id':'EXEMPLAR-6145-1.1','topic_id':'1.1','items':items})
(EX/'README.md').write_text('''# NSSCO Economics structural exemplar

An isolated, original topic 1.1 example showing claims, blocks, item labels, claim revisions and standalone performance tasks. Copy the shape and the specific rubric discipline, never its scenarios or its volume. Main topics remain unauthored; this folder is not published output. Source limits and semantic review still apply. The full deterministic result is in topics/1.1/qa_report.json; not_run checks are reported explicitly, not called passes.
''')
print(n,'note words;',len(claims),'claims;',len(items),'items in isolated exemplar.')
