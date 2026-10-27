"""Generate two explicit reduced-scope structural exemplars using shared builders.

These are not completed production topics. Full contracts/work orders are untouched.
"""
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path
import yaml

WS=Path(__file__).resolve().parents[1]
REPO=WS.parents[1]
STD=REPO/'standard/v0.2.0-draft'
REG=json.loads((WS/'curriculum/objective_registry.json').read_text())

def write(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def stamp(obj):
    obj['claims_seen']={c:1 for c in obj['claim_ids']}
    text=(obj['prompt']+'|'+obj['canonical_answer']+'|'+'|'.join(obj['marking_guidance'])) if 'item_id' in obj else obj['heading']+'|'+obj['text']
    obj['authored_hash']=hashlib.sha256(text.encode()).hexdigest()
    return obj

def prepare(name,topic,ids):
    dst=WS/'exemplar'/name/'nam-6144-nssco-2026'
    assert (REPO/'operations/analysis/6144-nssco-business-studies-corpus-analysis.md').is_file()
    dst.mkdir(parents=True,exist_ok=True)
    reg=copy.deepcopy(REG)
    reg['objectives']=[o for o in reg['objectives'] if o['objective_id'] in ids or o['objective_id']==f'OBJ-6144-{topic}']
    for o in reg['objectives']:
        if o['objective_id'] in ids:o['parent_id']=f'OBJ-6144-{topic}';o['prerequisite_ids']=[]
    write(dst/'curriculum/objective_registry.json',reg)
    for filename in ['syllabus-facts.json','assessment-framework.json','glossary.json','scope-scan.json','syllabus-exclusions.json','unit_titles.json']:
        (dst/'curriculum'/filename).write_bytes((WS/'curriculum'/filename).read_bytes())
    exp=json.loads((WS/'curriculum/exam-exposure.json').read_text())
    exp['objectives']=[x for x in exp['objectives'] if x['objective_id'] in ids]
    write(dst/'curriculum/exam-exposure.json',exp)
    evidence=json.loads((WS/'assessment-evidence/assessment_evidence.json').read_text())
    for record in evidence['records']:record['objective_ids']=[x for x in record['objective_ids'] if x in ids]
    evidence['records']=[r for r in evidence['records'] if r['objective_ids']]
    write(dst/'assessment-evidence/assessment_evidence.json',evidence)
    write(dst/'curriculum/misconceptions.json',{'entries':[]})
    (dst/'qualification-profile.yaml').write_bytes((WS/'qualification-profile.yaml').read_bytes())
    profile=yaml.safe_load((WS/'subject-profile.yaml').read_text())
    profile['slot_plan']['performance_tasks']=[]
    profile['slot_plan']['misconception_slots']=None
    (dst/'subject-profile.yaml').write_text(yaml.safe_dump(profile,sort_keys=False,allow_unicode=True))
    sys.path.insert(0,str(STD/'build'))
    import make_contract,make_work_order
    make_contract.build(str(dst),force=True)
    wo=make_work_order.build(str(dst),topic)
    td=dst/'topics'/topic
    write(td/'work_order.json',wo)
    (td/'work_order.md').write_text(make_work_order.as_markdown(wo))
    write(dst/'REDUCED-SCOPE.json',{'purpose':'Structural exemplar, not a full production topic or semantic release.',
                                  'production_workspace':str(WS.relative_to(REPO)), 'selected_objectives':ids,
                                  'reductions':['Registry narrowed to named objectives plus topic root; member parent redirected only inside this scratch exemplar.','Performance tasks and misconception extras disabled only for this thin slice.','Shared builders and shared checks unchanged.']})
    return dst,td,wo


def ledger(topic,rows):
    claims=[]
    for n,(ids,text,kind,provenance,locator) in enumerate(rows,1):
        claims.append({'claim_id':f'CLM-6144-{topic}-EX-{n:02}','objective_ids':ids,'text':text,'claim_type':kind,'provenance':provenance,
                       'evidence':[{'source_id':'NIED-6144-SYLLABUS','locator':locator,'support_type':'paraphrase' if provenance=='syllabus_direct' else 'derivation'}],
                       'derived_from_claim_ids':[],'verification':{'status':'unverified','method':'Structural planning exemplar; no independent subject approval claimed.','reviewer_id':None,'reviewed_at':None,'confidence':0.85},
                       'publishable':False,'revision':1})
    return {'ledger_id':f'LEDGER-6144-{topic}-EX','claims':claims}


def unit(uid,title,oids,blocks,budget):
    shaped=[]
    for n,(kind,head,text,claims,aos) in enumerate(blocks,1):
        shaped.append(stamp({'block_id':f'EX-B{n:02}','block_type':kind,'heading':head,'text':text,'claim_ids':claims,'context_tags':['Namibia','original teaching example'], 'assessment_objectives':aos}))
    count=sum(len(b['text'].split()) for b in shaped)
    return {'unit_id':uid,'title':title,'objective_ids':oids,'level':'NSSCO','core_status':'core','objective_type':'integrated teaching slice','depth_tier':2,
            'word_budget':{'min':budget[0],'target':sum(budget)//2,'max':budget[1]},'blocks':shaped,'word_count':count,'qa_status':'review_required'}


def item(slot,claims,prompt,answer,guidance,facts):
    return stamp({'item_id':slot['slot'],'objective_ids':[slot['objective_id']],'claim_ids':claims,'item_type':'flashcard','subtype':slot['subtype'],
                  'assessment_objectives':slot['assessment_objectives'],'blooms_level':slot['blooms_level'],'command_word':slot['command_word'],
                  'mark_tariff':slot['mark_tariff'],'difficulty':slot['difficulty'],'prompt':prompt,'canonical_answer':answer,'marking_guidance':guidance,
                  'context':{'sector':'manufacturing','business_size':'small','ownership':None,'situation':'Original Namibian teaching example','facts':facts},
                  'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'Original structural exemplar derived from cited syllabus concepts.','qa_status':'review_required'})


def finish(dst,td,topic,wo,claims,units,items):
    write(td/'claims/canonical_claim_ledger.json',claims)
    for u in units:write(td/'content-units'/f"{u['unit_id']}.json",u)
    write(td/'learning-items'/f'topic_{topic}_items.json',{'dataset_id':f'EXEMPLAR-6144-{topic}','topic_id':topic,'items':items})
    assert {i['item_id'] for i in items}=={s['slot'] for s in wo['item_slots']}
    subprocess.run([sys.executable,str(STD/'build/render_notes.py'),str(dst),topic],check=True,capture_output=True)
    result=subprocess.run([sys.executable,str(STD/'checks/run_checks.py'),str(dst),topic],capture_output=True,text=True)
    report=json.loads((td/'qa_report.json').read_text())
    statuses=collections.Counter(c['status'] for c in report['deterministic_checks'])
    print(dst.parent.name,'decision',report['release_decision'],'checks',dict(statuses),'runner_exit',result.returncode)
    if statuses['fail']:print(result.stdout)
    return {'exemplar':str(dst.relative_to(WS)),'topic':topic,'release_decision':report['release_decision'],'check_status_counts':dict(statuses),'runner_exit_code':result.returncode,
            'scope':'Reduced structural slice only; no human or independent subject-content approval inferred.'}


def qualitative():
    ids=['OBJ-6144-2.5.01','OBJ-6144-2.5.02'];dst,td,wo=prepare('qualitative','2.5',ids)
    claims=ledger('2.5',[
        ([ids[0]],'Effective management coordinates planning, organising, leading and control so that people work towards business objectives.','definition','syllabus_direct','PDF p.30, effective management glossary; PDF p.12, topic 2.5'),
        ([ids[1]],'Clear plans and allocation of work can reduce avoidable duplication when the team follows them and the plan fits its resources.','causal','reasoned_extension','Derived from the management functions in PDF pp.12 and 30; original causal illustration.'),
        ([ids[1]],'Checking progress against a target can reveal a delay early enough for a feasible corrective action.','causal','reasoned_extension','Derived from planning and control in PDF pp.12 and 30; conditional teaching inference.'),
        (ids,'In the original teaching case, a small workshop must complete an order by Friday; the manager allocates jobs and checks progress each afternoon.','synthetic_example','generated_quality','Original fictional Namibian case; not an official examination scenario.')])
    c=[x['claim_id'] for x in claims['claims']]
    u1=unit(wo['content_units'][0]['unit_id'],'What makes management effective',[ids[0]],[
        ('definition','Coordinating work towards an objective','Effective management means coordinating planning, organising, leading and control so that the business works towards its objectives. An objective supplies the intended result. Planning establishes what needs to happen. Organising allocates the work and resources. Leading helps people carry out the work. Control compares progress with the plan and helps a manager respond to a shortfall. The functions matter because a business normally needs several people and resources to work together. Naming the functions alone leaves out the purpose that makes management effective.',[c[0]],['A']),
        ('worked_application','A workshop with a delivery target','Imagine a small workshop in Namibia that has promised a customer a completed order on Friday. This is an invented teaching situation. Its manager identifies the jobs that must be finished, checks which workers and equipment are available, and allocates the work. Each afternoon the manager compares completed jobs with the schedule. If one stage is late, the manager considers a feasible change to the allocation. The objective is timely completion, rather than merely keeping everyone busy. The example shows the connection between the functions and an intended result. A manager can carry out many activities yet still fail to coordinate them around the objective.',[c[0],c[3]],['A','B']),
        ('cross_link','Connecting the ideas','Organisational structure concerns how responsibilities are arranged. Communication helps people understand a plan. These connections explain why effective management needs more than a job title.',[c[0]],['A'])],wo['content_units'][0]['word_budget'])
    u2=unit(wo['content_units'][1]['unit_id'],'Why effective management is needed',[ids[1]],[
        ('analysis_chain','From coordination to a business effect','A plan gives people a common intended result, but the work still needs to be organised. If two workers repeat the same task while another necessary task is left unfinished, the team may waste effort and miss its deadline. Clear allocation can reduce that duplication when the instructions are understood and the resources are suitable. The reasoning runs from a management action, through what changes in the work, to an effect on the business. It does not mean that having a manager guarantees success: an unrealistic plan or inadequate resources may still prevent completion.',[c[1]],['A','C']),
        ('worked_application','Using the Friday deadline','In the workshop case, one worker prepares materials while another completes the first stage of the order. By checking progress each afternoon, the manager can notice a delay before Friday. If a worker is available and trained for the delayed task, changing the allocation may help the workshop recover time. Earlier action can therefore improve the chance of meeting the delivery commitment. The effect is conditional: moving an untrained worker to unfamiliar equipment may create mistakes instead. Effective management requires a feasible response to the problem, not simply a decision to move people. A useful explanation names the action, connects it to a case fact, and traces the consequence for the order.',[c[2],c[3]],['A','B','C']),
        ('summary','Keeping the purpose visible','Management is needed to coordinate people and resources around objectives. A reason becomes clearer when the explanation identifies the specific work problem it addresses and the effect that follows.',[c[1],c[2]],['A','C'])],wo['content_units'][1]['word_budget'])
    slots={s['objective_id']:s for s in wo['item_slots']}
    items=[item(slots[ids[0]],[c[0]],'Define effective management. [2]','Effective management coordinates the planning, organising, leading and control of people and resources so that the business works towards its objectives.',
                ['Precise meaning: coordination of the management functions, one knowledge mark.','Purpose: working towards business objectives, one knowledge mark.'],[]),
           item(slots[ids[1]],[c[1],c[2],c[3]],'Explain why a small Namibian workshop with a Friday delivery commitment needs clear allocation of work and daily progress checks. [6]',
                'Clear allocation identifies who performs each task, reducing duplicated work and unfinished stages when workers follow the plan. In this workshop that helps necessary jobs be completed before Friday. Daily progress checks can reveal a delay while time remains to respond. If trained workers and equipment are available, the manager can adjust the schedule, improving the chance of meeting the delivery commitment.',
                ['Starting point: clear allocation and progress checks, two knowledge marks.','Context: the small workshop, Friday commitment and unfinished jobs support two distinct applications.','Because mechanism: coordination reduces duplication and checking reveals delay; one developed explanation for each.','Consequence: connect each effect to the business delivery objective, with the resource condition kept visible.'],['Friday delivery commitment','Daily progress checks'])]
    return finish(dst,td,'2.5',wo,claims,[u1,u2],items)


def quantitative():
    target='OBJ-6144-4.4.10-01';dst,td,wo=prepare('quantitative','4.4',[target])
    claims=ledger('4.4',[
        ([target],'Unit production cost is total production cost divided by output.','formula','syllabus_direct','PDF p.33, unit cost glossary; PDF p.18, cost-plus prices'),
        ([target],'A cost-plus price adds the specified markup to the stated unit cost.','formula','reasoned_extension','PDF p.18, calculate cost plus prices; arithmetic derivation.'),
        ([target],'An original workshop example uses total batch production cost of N$1,800, output of 150 bags and a markup of 25% on unit production cost.','synthetic_example','generated_quality','Original numerical teaching inputs, distinct from official examination values.'),
        ([target],'A price N$3 above unit production cost does not establish net profit if other business expenses remain.','inference','reasoned_extension','Derived from the stated cost basis and the distinction between income, expenses and profit in PDF p.12.')])
    c=[x['claim_id'] for x in claims['claims']]
    text='''A cost-plus calculation starts with the cost basis specified in the information. Unit production cost allocates the total production cost across the output. The markup is then calculated on that unit cost and added to it. A markup percentage is not the same fraction as a profit margin on the selling price, because the denominator is different. Keeping the basis visible helps prevent using the wrong percentage.

Consider an invented workshop in Ondangwa that makes cloth bags. Its total production cost for a batch is N$1,800 and the batch contains 150 bags. The owner wants a markup of 25% on unit production cost. The information states a total production cost; there is no need to invent missing material or labour charges for the calculation.

Unit cost formula: total production cost divided by output. Substitution: 1800 ÷ 150 = 12, so unit production cost is N$12 per bag. Markup per bag: 0.25 × 12 = 3, giving N$3. Selling price: 12 + 3 = 15, giving N$15 per bag. The selling price is the amount charged for one bag under this pricing rule. The N$3 difference is the addition above allocated production cost; it does not establish net profit if other business expenses remain.

The interpretation concerns what the price means. It is not a second calculation to check the answer. Whether customers will buy at that price is a separate commercial question: a cost-plus rule alone does not demonstrate demand. When working from another example, retain its stated cost basis, calculate the markup on that basis, and give the final price with its currency and per-unit meaning.'''
    u=unit(wo['content_units'][0]['unit_id'],'Calculating a cost-plus price',[target],[('worked_calculation','From the cost basis to the selling price',text,c,['A','B','C'])],wo['content_units'][0]['word_budget'])
    slot=wo['item_slots'][0]
    it=item(slot,c,'Calculate the cost-plus selling price per bag for an invented Ondangwa workshop. Total production cost is N$1,800 for 150 bags; the markup is 25% on unit production cost. [6]',
            'Unit cost formula: total production cost ÷ output. Substitution: 1800 ÷ 150 = 12, giving N$12 per bag. Markup: 0.25 × 12 = 3, giving N$3 per bag. Selling price: 12 + 3 = 15, giving N$15 per bag. This is the charge per bag under the pricing rule; it is N$3 above allocated unit production cost and does not establish net profit if other expenses remain.',
            ['Formula: unit cost and selling price relationships, two knowledge marks.','Substitution and working: use the total batch cost, output and stated cost-based markup, two application marks.','Result with currency units: unit cost N$12 and selling price N$15 per bag, two analysis marks.','Interpretation: the price is a charge per bag above the stated unit production cost; other expenses may affect net profit.'],
            ['Total production cost N$1,800','150 bags','25% markup on unit production cost'])
    return finish(dst,td,'4.4',wo,claims,[u],[it])


if __name__=='__main__':
    import collections
    reports=[qualitative(),quantitative()]
    write(WS/'exemplar/VALIDATION.json',{'reports':reports,'all_zero_failures':all(not r['check_status_counts'].get('fail') for r in reports)})
