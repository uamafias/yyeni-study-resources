"""Two isolated structural slices, not authored production topics or publication."""
from pathlib import Path
import copy,hashlib,json,shutil,subprocess,sys,yaml
W=Path(__file__).resolve().parents[1];ROOT=W.parents[1]
X=W/'exemplar';EW=X/'work'/W.name
def read(p):return json.loads(p.read_text())
def dump(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def run(script,*args):
    result=subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft'/script),*map(str,args)],cwd=ROOT)
    if script=='checks/run_checks.py':
        report=read(Path(args[0])/'topics'/str(args[1])/'qa_report.json')
        failures=[x for x in report['deterministic_checks'] if x['status']=='fail']
        if failures:raise RuntimeError(failures)
        if result.returncode:
            print('CLI LIMITATION: exit status',result.returncode,'despite release_decision',report['release_decision'],
                  'and zero FAIL checks. Retain the raw report; do not call NOT_RUN results passes.')
    else:result.check_returncode()

def setup():
    EW.mkdir(parents=True,exist_ok=True)
    for name in ['qualification-profile.yaml','subject-profile.yaml']:
        shutil.copyfile(W/name,EW/name)
    sp=yaml.safe_load((EW/'subject-profile.yaml').read_text());sp['slot_plan']['performance_tasks']=[]
    (EW/'subject-profile.yaml').write_text(yaml.safe_dump(sp,sort_keys=False,allow_unicode=True))
    for name in ['syllabus-facts.json','assessment-framework.json','exam-exposure.json','glossary.json','scope-scan.json','syllabus-exclusions.json','unit_titles.json']:
        dump(EW/'curriculum'/name,read(W/'curriculum'/name))
    reg=read(W/'curriculum/objective_registry.json');ids={'OBJ-6137-1.2','OBJ-6137-1.2.01','OBJ-6137-4.1','OBJ-6137-4.1.04'}
    reg['objectives']=[o for o in reg['objectives'] if o['objective_id'] in ids]
    dump(EW/'curriculum/objective_registry.json',reg)
    mc=read(W/'curriculum/misconceptions.json');mc['entries']=[e for e in mc['entries'] if e['objective_id']=='OBJ-6137-1.2.01']
    dump(EW/'curriculum/misconceptions.json',mc)
    dump(EW/'assessment-evidence/assessment_evidence.json',read(W/'assessment-evidence/assessment_evidence.json'))
    out=X/'operations/analysis/6137-nssco-geography-corpus-analysis.md';out.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(ROOT/'operations/analysis/6137-nssco-geography-corpus-analysis.md',out)
    run('build/make_contract.py',EW,'--force');run('build/make_work_order.py',EW,'--all')

TEXTS={
'1.2':[
('definition','Rock change and material removal',
'''Weathering breaks down rock or changes its minerals at the place where the rock lies. Physical weathering splits rock into smaller pieces without changing the minerals. Chemical weathering changes susceptible minerals through reactions. Plants can contribute through root growth or chemical changes associated with organic material. A loosened fragment can remain beside the outcrop. Its smaller size is evidence of breakdown, but does not by itself demonstrate transport away from that place.

Erosion involves wearing away and removal by a moving agent. River water, waves and wind can act on exposed surfaces or carry material away. Describing the agent makes an account more precise than saying that a rock has changed. The distinction concerns the action and the location of the material, rather than whether the example happens quickly or slowly. Both processes can operate in one landscape and can influence each other.'''),
('worked_application','Follow the evidence',
'''Consider an original field record from two unnamed sites. At site A, a jointed block has split and the new fragments remain beneath the parent rock. At site B, moving water repeatedly carries fragments from the foot of an exposed face and the face retreats. The first observation demonstrates weathering in place. The second supplies evidence of an erosional agent and removal. The observation at A alone does not establish that the fragments have been removed.

A photograph of smaller stones cannot establish the complete sequence that produced them. Look for the evidence actually supplied: a changed mineral, a widened joint, detached fragments, an active agent or material removed from an exposed surface. More than one process may be supported if the observations establish more than one action. Avoid adding a river, wave or wind that the description does not mention.'''),
('misconception','A useful discrimination',
'''The claim that any breaking rock is erosion confuses breakdown with removal. Ask whether the evidence shows alteration or splitting at the original location, or demonstrates wearing away and removal by a moving agent. A later event can move previously weathered fragments; this does not change the earlier event into erosion. This distinction connects weathering to river and coastal processes, where the agent and the movement must be described clearly.''')],
'4.1':[
('plain_explanation','Select a sample by a stated rule',
'''A sample is a selection from the people, places or objects an investigation concerns. Begin by stating that population and the aim. A beach study might concern pebbles along a marked transect; a tourism study might concern visitors leaving a leisure site during stated hours. The selection rule must match that aim. A method that misses a relevant group or location can produce a misleading result even if the measurements themselves are careful.

Random sampling uses a chance procedure, such as random numbers linked to a numbered list or positions. Looking around and choosing an object that seems typical is not a chance procedure. Systematic sampling selects at regular intervals after a stated start. Along a beach transect, this might mean taking a pebble at each marked interval using the same rule for which pebble to choose. Record the position so that the sampling route is clear.'''),
('worked_application','Beach and visitor investigations',
'''For systematic pebble selection, mark the transect and starting point, specify the interval and apply an agreed selection rule at each position. Selecting an especially large pebble at one position and the easiest pebble at another changes the procedure. A rule for a position with no suitable pebble should be agreed before collection. Keep sampling choices separate from how the pebble is measured; both decisions affect the quality of the investigation.

Stratified sampling first divides the population into relevant groups. The investigator then sets a selection rule within each group. A tourism investigation comparing age groups should include respondents from the groups it intends to compare. The allocation can follow known group proportions where that is the stated design; a different justified allocation may suit a comparison. Stratification by age does not automatically represent visitors at unobserved times or different entrances.'''),
('cross_link','Selection and conclusions',
'''Record the rule, coverage and collection period alongside the results. These details help a reader judge how far a conclusion can reasonably extend. A systematic sample is not automatically unbiased if a repeating spatial pattern matches its interval. A sample selected at one car park does not automatically cover people arriving on foot. Connect the sampling decision to the coastal or tourism question being investigated and identify the limitation it could create.''')]
}

def claim(cid,oid,text,typ):
    return {'claim_id':cid,'objective_ids':[oid],'text':text,'claim_type':typ,'provenance':'source_synthesised',
       'evidence':[{'source_id':'SYL-6137-2016','locator':'PDF p8' if '1.2' in oid else 'PDF p28','support_type':'paraphrase'}],
       'derived_from_claim_ids':[],'verification':{'status':'unverified','method':'Source-informed structural exemplar; independent review pending.',
           'reviewer_id':None,'reviewed_at':None,'confidence':0.8},'publishable':False,'revision':1}

def stamp(x,claims,is_item=False):
    x['claims_seen']={c:1 for c in claims}
    text=(x['prompt']+'|'+x['canonical_answer']+'|'+'|'.join(x['marking_guidance'])) if is_item else x['heading']+'|'+x['text']
    x['authored_hash']=hashlib.sha256(text.encode()).hexdigest()

def fill():
    for tid in ('1.2','4.1'):
        td=EW/'topics'/tid;wo=read(td/'work_order.json');oid=wo['content_units'][0]['objective_ids'][0]
        if tid=='1.2':
            statements=[('Weathering breaks down or alters rock in place.','definition'),
                ('Erosion wears away and removes material through the action of a moving agent.','definition'),
                ('Breakdown without evidence of removal does not by itself establish erosion.','misconception_correction')]
        else:
            statements=[('Random sampling uses a stated chance procedure rather than personal selection.','definition'),
                ('Systematic sampling selects at regular intervals after a stated start, using a consistent selection rule.','definition'),
                ('Stratified sampling divides the population into relevant groups and selects within each under a stated allocation.','definition')]
        claims=[claim(f'CL-6137-{tid}-{i:02}',oid,t,k) for i,(t,k) in enumerate(statements,1)];cids=[c['claim_id'] for c in claims]
        dump(td/'claims/canonical_claim_ledger.json',{'ledger_id':'LEDGER-6137-EXEMPLAR-'+tid,'claims':claims})
        blocks=[]
        for i,(kind,head,text) in enumerate(TEXTS[tid],1):
            b={'block_id':f'BL-6137-{tid}-{i:02}','block_type':kind,'heading':head,'text':text,
               'claim_ids':cids,'context_tags':['Namibian secondary learning','original teaching example'],
               'assessment_objectives':['A'] if tid=='1.2' else ['D']}
            stamp(b,cids);blocks.append(b)
        uplan=wo['content_units'][0];lo,hi=uplan['word_budget'];words=sum(len(b['text'].split()) for b in blocks)
        unit={'unit_id':uplan['unit_id'],'title':'Weathering and erosion' if tid=='1.2' else 'Sampling in geographical enquiries',
          'objective_ids':[oid],'level':'NSSCO','core_status':'core','objective_type':'geo_compare' if tid=='1.2' else 'enq_method',
          'depth_tier':3,'word_budget':{'min':lo,'target':(lo+hi)//2,'max':hi},'blocks':blocks,'word_count':words,'qa_status':'review_required'}
        dump(td/uplan['file'],unit)
        items=[]
        for s in wo['item_slots']:
            st=s['subtype']
            if tid=='1.2' and st=='DIST':
                prompt='Distinguish between weathering and erosion.'
                answer='Weathering breaks down or chemically alters rock in place, whereas erosion wears material away through a moving agent and removes it from its original position.'
                guide=['1 mark: weathering involves breakdown or chemical alteration.','1 mark: erosion wears a surface through a moving agent.','1 mark: make the difference in removal explicit: in-place change versus material taken away. Do not credit the same point twice.']
            elif tid=='1.2' and st=='APP':
                prompt='Suggest why the observations support weathering at site A and erosion at site B. At A, a block has split and its fragments remain beneath it. At B, moving water carries fragments from an exposed face, which retreats. Use the given evidence.'
                answer='The split at A demonstrates breakdown, and the fragments remaining beneath the block show change in place. At B, moving water and the retreating face provide evidence of an active agent wearing away and removing material.'
                guide=['1 mark: apply the given split-block evidence to breakdown at A.','1 mark: use the fragments remaining as evidence of change in place.','1 mark: give the reason for erosion at B by linking the moving-water/retreat evidence to wearing away and removal.']
            elif tid=='1.2':
                prompt='Explain the error in this claim and give a test that distinguishes the processes: “A block has split, so that observation by itself proves erosion.”'
                answer='Splitting can demonstrate weathering in place; the claim does not establish wearing away and removal. Test whether a moving agent has worn and removed material, rather than inferring erosion from splitting alone.'
                guide=['1 mark: identify the confusion between rock breakdown and erosion.','1 mark: state the correct distinction and apply the test of evidence for a moving agent and removal.']
            elif st=='PROC':
                prompt='Describe how learners could select pebbles systematically along a marked beach transect. Give a procedure that another group could repeat.'
                answer='State the starting point and mark regular intervals along the transect. At each interval apply the same agreed rule for selecting a pebble, with a pre-agreed rule if no suitable pebble is present. Record the position of each selected pebble so the sample can be traced and the procedure repeated.'
                guide=['1 mark: first state a start and regular interval.','1 mark: give a consistent selection step, including a rule for an unavailable pebble.','1 mark: record the position for each selection as the result of the sampling procedure.']
            else:
                prompt='Explain why a tourism survey comparing two age groups might use stratified sampling by age rather than interviewing the first people available at a car park.'
                answer='Stratifying by age deliberately includes respondents from the age groups being compared. This supports the intended comparison instead of allowing the available crowd at one moment to leave a group poorly represented.'
                guide=['1 mark: give the reason that the selection includes the relevant age groups.','1 mark: explain the consequence for a meaningful comparison, rather than relying on the first available crowd.']
            it={'item_id':s['slot'],'objective_ids':[oid],'claim_ids':cids,'item_type':'flashcard','subtype':st,
               'assessment_objectives':s['assessment_objectives'],'blooms_level':s['blooms_level'],'command_word':s['command_word'],
               'mark_tariff':s['mark_tariff'],'difficulty':s['difficulty'],'prompt':prompt,'canonical_answer':answer,
               'marking_guidance':guide,'context':{'sector':None,'business_size':None,'ownership':None,
                   'situation':'original Geography teaching scenario','facts':[]},'prerequisite_item_ids':[],
               'core_status':'core','intentional_duplicate_group':None,'provenance':'Original structural exemplar; not a production-bank item.','qa_status':'review_required'}
            if s.get('misconception_entry'):it['misconception_entry']=s['misconception_entry']
            stamp(it,cids,True);items.append(it)
        dump(td/'learning-items'/f'topic_{tid}_items.json',{'dataset_id':'DATA-6137-EXEMPLAR-'+tid,'topic_id':tid,'items':items})
        run('build/render_notes.py',EW,tid)
        run('checks/run_checks.py',EW,tid)

if __name__=='__main__':setup();fill()
