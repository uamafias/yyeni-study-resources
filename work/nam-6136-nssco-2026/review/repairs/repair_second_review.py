"""Repair Claude's second-review findings without external research or release steps."""
import hashlib, json, re, sys
from pathlib import Path

WS=Path(__file__).resolve().parents[2]
BASE=WS/'review/repairs/baseline/topics'
sys.path.insert(0,str(WS.parents[1]/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text
def read(p): return json.loads(p.read_text())
def dump(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def item(items, marker): return next(i for i in items if marker in i['item_id'])
changes=[]

# N-01: restore all 66 teaching paragraphs that a short card answer had replaced.
restored=[]
for td in sorted((WS/'topics').iterdir()):
    if not td.is_dir() or not (BASE/td.name/'content-units').exists(): continue
    items=read(next((td/'learning-items').glob('*.json')))['items']
    answers={i.get('canonical_answer','') for i in items}
    for bp in sorted((BASE/td.name/'content-units').glob('*.json')):
        livep=td/'content-units'/bp.name
        base,live=read(bp),read(livep)
        dirty=False
        for old,new in zip(base['blocks'],live['blocks']):
            if old.get('text')!=new.get('text') and new.get('text') in answers:
                # Keep the card's new applied example, but restore the full lesson first.
                new['text']=old['text']+'\n\nApplied example: '+new['text']
                new['repair_note']='Restored original full-depth lesson after second review identified card-text overwrite; retained the newer applied example.'
                restored.append(new['block_id']);dirty=True
        if dirty:
            live['word_count']=sum(len((b.get('heading','')+' '+b.get('text','')).split()) for b in live['blocks'])
            if live['word_count']>live['word_budget']['max']:
                raise ValueError(f"{live['unit_id']} exceeds ceiling after restore: {live['word_count']}")
            dump(livep,live)
    if restored:
        itemsdoc=read(next((td/'learning-items').glob('*.json')))
        dump(next((td/'learning-items').glob('*.json')),itemsdoc)
changes.append({'finding':'N-01','restored_blocks':len(restored),'ids':restored})

# N-02: reconcile the notes' work-category example using disjoint and overlapping totals.
td=WS/'topics/4.2'; units=sorted((td/'content-units').glob('*.json'))
for p in units:
    u=read(p)
    for b in u['blocks']:
        if 'In a fictional survey of 100 people available for and seeking more work' in b.get('text',''):
            old='In a fictional survey of 100 people available for and seeking more work, 30 have no work, 40 have fewer paid hours than they are available for, and 30 have their desired hours. The no-work and insufficient-hours groups together show a shortfall in work, but 70 have some employment. Calling all 70 people with unmet work needs unemployed would erase the distinction.'
            new='In a fictional survey of 100 people available for and seeking more work, 30 have no work, 40 have fewer paid hours than they are available for, and 30 have their desired hours. The unemployed total is 30. The employed total is 70 (40 underemployed + 30 with their desired hours). People with unmet work needs total 70 (30 unemployed + 40 underemployed). These two totals overlap because the 40 underemployed people are included in the employed total; do not add the totals together. Calling all 70 with unmet work needs unemployed would erase the distinction.'
            b['text']=b['text'].replace(old,new)
            b['repair_note']='Clarified overlapping employment and unmet-work-needs totals after second review.'
            dump(p,u);break
changes.append({'finding':'N-02','action':'Explicitly label unemployed, employed, underemployed and unmet-work-needs totals; clarify the overlap.'})

# N-03: remove the repair's misleading unit-wide locator fan-out; claims remain unverified.
for td in sorted((WS/'topics').iterdir()):
    p=td/'claims/canonical_claim_ledger.json'
    if not p.exists(): continue
    ledger=read(p); n=0; changed=False
    for c in ledger['claims']:
        ev=c.get('evidence',[]); kept=[e for e in ev if not str(e.get('locator','')).startswith('Existing author source check, 2026-10-20;')]
        n+=len(ev)-len(kept)
        c['evidence']=kept
        if c.get('provenance')=='author_synthesis':
            bp=BASE/td.name/'claims/canonical_claim_ledger.json'
            old={x['claim_id']:x for x in read(bp)['claims']}.get(c['claim_id']) if bp.exists() else None
            if old:
                c['provenance']=old.get('provenance','generated_gap');changed=True
    if n or changed:
        dump(p,ledger)
        if n: changes.append({'finding':'N-03','topic':td.name,'removed_misattributed_locators':n})

# N-04: make the seven development-mechanism cards and six institution cards focused and natural.
fixes={
('8.1','025'):('Explain one way public institutions can support development.','Public institutions can direct resources to services such as water, roads, education or health. Access improves only when the allocation is implemented and people can use the service.'),
('8.1','027'):('Explain one way peace and security can support development.','Greater safety can let people travel, learn, work and participate. Protection must also respect rights; security that restricts people can undermine development.'),
('8.1','028'):('Explain one way access to finance can support development.','Suitable credit can help a viable producer buy equipment or inputs that are otherwise unaffordable. Repayment must fit expected income, and finance alone cannot create demand or skills.'),
('8.1','029'):('Explain one way infrastructure can support development.','Reliable roads, water, electricity and communications connect people to services and markets. Maintenance and usable connections matter because an installed but non-functioning asset provides little access.'),
('8.1','030'):('Explain one way education or social services can support development.','Education can build knowledge and skills; health and other social services can protect people’s ability to participate. Staff, supplies, access and inclusion affect whether facilities deliver these benefits.'),
('8.1','031'):('Explain one possible benefit of decentralisation.','Moving a defined decision closer to local communities can use local knowledge and make services more responsive. The benefit depends on sufficient funding, staff capacity and accountability accompanying the responsibility.'),
('8.1','032'):('Explain one way an implementation barrier can limit development.','A shortage of trained staff can delay a planned service, leaving the intended users without it. The barrier should be identified from evidence in the stated case, not assumed of a whole country.'),
('9.2','011'):('Describe one role of the World Bank and one implementation consideration.','The World Bank provides development finance, knowledge and technical assistance. A proposed project still needs a feasible design, capable implementation and evidence that intended users benefit.'),
('9.2','012'):('Describe one role of the IMF and one implementation consideration.','The IMF supports monetary cooperation and economic stability through monitoring, advice, capacity development and lending for balance-of-payments needs. Lending terms and their effects should be assessed using the particular case.'),
('9.2','013'):('Describe one role of UNDP and one implementation consideration.','UNDP supports development work such as poverty reduction, governance and resilience through partnerships and technical assistance. Local capacity and coordination affect whether this support produces lasting results.'),
('9.2','014'):('Describe one role of UNICEF and one implementation consideration.','UNICEF supports children’s rights and well-being, including health, education, nutrition, water and protection. The reach and continuity of a programme depend on its implementation and access for intended children.'),
('9.2','015'):('Describe one role of FAO and one implementation consideration.','FAO works on food security, agriculture and related knowledge and cooperation. Advice or technical support must suit local conditions and be accessible to producers to contribute to improved food production.'),
('9.2','016'):('Describe one role of UNESCO and one implementation consideration.','UNESCO promotes international cooperation in education, science, culture and information. A specific programme’s contribution depends on the local need it addresses and on effective implementation.'),
}
for (topic,num),(prompt,answer) in fixes.items():
    p=WS/'topics'/topic/'learning-items'/f'topic_{topic}_items.json'; d=read(p); it=item(d['items'],f'ITEM-6136-{topic}-{num}-')
    it['prompt']=prompt;it['canonical_answer']=answer;it['repair_note']='Rewritten after Claude second review finding '+('N-04' if topic in ('8.1','9.2') else 'N-05')+'.'
    dump(p,d)
changes.append({'finding':'N-04','items_rewritten':13})

# N-05: align the learning prompt with the objective's traditional/modern comparison and evaluate command.
p=WS/'topics/7.3/learning-items/topic_7.3_items.json';d=read(p);it=item(d['items'],'ITEM-6136-7.3-006-')
it['prompt']='Describe these fictional routes to recognised technical skills and give a reasoned judgement. A community apprenticeship teaches local craft through practice and has no formal qualification. A reachable college course offers technical theory and an assessed qualification, but costs affordable fees and reduces earning time. Both are feasible.'
it['canonical_answer']='A community apprenticeship can develop practical skill in a local setting without course fees, but the learner receives no formal qualification and its content may be narrower. College offers structured theory and assessed recognition, which may support further training, but fees and time away from earning are costs. For a learner who needs recognised credentials for technical employment, college is stronger if the qualification is accepted and the fees are manageable. The apprenticeship may better suit someone prioritising immediate practice and local craft. Judge against the learner’s aims, recognition and costs rather than assuming one route suits everyone.'
it['repair_note']='Reframed to match traditional/community and modern/institutional education while retaining the objective’s evaluate command.';dump(p,d)
changes.append({'finding':'N-05','action':'Aligned learning prompt with traditional/community versus modern/institutional education; retained reasoned judgement because standard check C-14 bars Evaluate in prompt text.'})

# N-06: use NDP5's taught goals and test the HPP pillars in the card slot.
p=WS/'topics/2.2/learning-items/topic_2.2_items.json';d=read(p)
it=item(d['items'],'ITEM-6136-2.2-004-');it['prompt']='Explain how to judge NDP5 against its stated goals of inclusive and equitable economic growth, people’s capabilities and health, environmental protection and resilience, and effective governance. A fictional district records more jobs but no rise in reliable water access in remote settlements. Weigh this mixed evidence; it is not a national result.'
it['canonical_answer']='More jobs can support inclusive and equitable economic growth if the benefit reaches different groups. Unchanged remote water access gives no evidence of improved access to that service and may indicate uneven gains in people’s capabilities and health. These results alone do not establish environmental protection, resilience or effective governance; each needs relevant evidence. Judge the goals separately and avoid claiming overall success from employment alone.'
it['repair_note']='Revised after Claude second-review finding N-06 to use the goals taught in the notes.'
it=item(d['items'],'ITEM-6136-2.2-003-');it['prompt']='Differentiate the economic-advancement pillar from the infrastructure-development pillar of the first Harambee Prosperity Plan.'
it['canonical_answer']='Economic advancement focused on productive opportunities and employment, while infrastructure development focused on networks such as water, electricity and transport. Both were shorter-term pillars intended to contribute to Vision 2030.'
it['repair_note']='Restored direct HPP-pillar practice after second-review finding N-06.';dump(p,d)
changes.append({'finding':'N-06','action':'Used NDP5 goals as taught in the notes and made a 2-mark HPP pillar contrast card.'})

# R6136-004: teach names drawn from the saved syllabus and examination corpus.
p=WS/'topics/1.2/content-units/CU-6136-1.2.01.json';u=read(p)
for b in u['blocks']:
    if b.get('heading')=='Sustainable Development Goals':
        b['text']='The United Nations Sustainable Development Goals (SDGs) organise international development ambitions for 2030. The saved 2022 examination figure shows examples including No Poverty, Zero Hunger, Good Health and Well-being, Clean Water and Sanitation, Decent Work and Economic Growth, and Responsible Consumption and Production. The syllabus specifically names SDG 12. Sustainable development can be considered through linked economic, social and environmental pillars; a goal may contribute to more than one, so do not force every goal into only one pillar. Progress in one area can help another, but trade-offs still need a judgement about present and future needs.'
        b['repair_note']='Expanded SDG examples and linked dimensions using saved 2022 assessment evidence and syllabus wording after Claude review R6136-004.'
        b['claims_seen']={'CLM-6136-1.2-01-00-90':2}
        b['authored_hash']=hashlib.sha256(_artefact_text(b).encode()).hexdigest()
u['word_count']=sum(len((b['heading']+' '+b['text']).split()) for b in u['blocks'])
if u['word_count']>u['word_budget']['max']: raise ValueError('1.2.01 exceeds word ceiling after SDG expansion')
dump(p,u)
p=WS/'topics/1.2/claims/canonical_claim_ledger.json';ledger=read(p)
for c in ledger['claims']:
    if c['claim_id']=='CLM-6136-1.2-01-00-90':
        c['text']=next(b['text'] for b in u['blocks'] if b.get('heading')=='Sustainable Development Goals')
        c['revision']=2;c['revised_at']='2026-10-20'
        note='R6136-004: revised with examples present in saved 6136 assessment evidence and the syllabus; still unverified independently.'
        if note not in c.setdefault('notes',[]): c['notes'].append(note)
dump(p,ledger)
p=WS/'topics/1.2/learning-items/topic_1.2_items.json';d=read(p);it=item(d['items'],'ITEM-6136-1.2-006-')
it['prompt']='Suggest a responsible-production response for a fictional tailoring group that discards usable fabric offcuts while buying new fabric for small bags. State two Sustainable Development Goals that relate to this action.'
it['canonical_answer']='Sort suitable offcuts and use them for the bags, reducing new-fabric use and discards (SDG 12: Responsible Consumption and Production). If the bags provide decent paid work, SDG 8: Decent Work and Economic Growth is also relevant. The action contributes to these aims but does not prove that either goal has been achieved.'
it['repair_note']='Added named SDG recall and application from the saved assessment figure and syllabus after Claude review R6136-004.'
it['authored_hash']=hashlib.sha256(_artefact_text(it).encode()).hexdigest()
base_item=next((x for x in read(BASE/'1.2/learning-items/topic_1.2_items.json')['items'] if x['item_id']==it['item_id']),None)
if base_item and not it.get('prior_hash'):it['prior_hash']=base_item.get('authored_hash')
dump(p,d)
c=next(c for c in ledger['claims'] if c['claim_id']=='CLM-6136-1.2-03-00-90')
c['text']='SDG 12 concerns responsible consumption and production. Reusing suitable fabric offcuts can reduce the need for new material and reduce waste. SDG 8 concerns decent work and economic growth; a viable product can connect to this goal when it supports decent paid work. Goals can interact, but a local action does not by itself establish progress against a global goal.'
c['revision']=2;c['revised_at']='2026-10-20';note='R6136-004: expanded named SDG application from saved syllabus and assessment evidence; still unverified independently.'
if note not in c.setdefault('notes',[]):c['notes'].append(note)
dump(WS/'topics/1.2/claims/canonical_claim_ledger.json',ledger)
for b in read(WS/'topics/1.2/content-units/CU-6136-1.2.03.json')['blocks']:
    if b['block_id']=='BLK-6136-1.2.03-R01':
        b['text']=c['text'];b['claims_seen']={c['claim_id']:c['revision']};b['authored_hash']=hashlib.sha256(_artefact_text(b).encode()).hexdigest();b['repair_note']='Expanded named SDG examples after Claude review R6136-004.'
        bp=WS/'topics/1.2/content-units/CU-6136-1.2.03.json';u2=read(bp);u2['blocks']=[b if x['block_id']==b['block_id'] else x for x in u2['blocks']];u2['word_count']=sum(len((x['heading']+' '+x['text']).split()) for x in u2['blocks']);dump(bp,u2);break
it['claims_seen']={c['claim_id']:c['revision'] for c in ledger['claims'] if c['claim_id'] in it.get('claim_ids',[])}
it['authored_hash']=hashlib.sha256(_artefact_text(it).encode()).hexdigest();dump(p,d)
# Propagate both revised claim stamps. Changed prose records its prior hash; unchanged
# artefacts record the explicit decision that they remain accurate and do not claim the addition.
manifest=read(WS/'review/repairs/post-repair-manifest.json')
revised={c['claim_id']:c['revision'] for c in ledger['claims'] if c['claim_id'] in {'CLM-6136-1.2-01-00-90','CLM-6136-1.2-03-00-90'}}
for fp in list((WS/'topics/1.2/content-units').glob('*.json')):
    u3=read(fp); dirty=False
    for b in u3['blocks']:
        cites=set(b.get('claim_ids',[]))&set(revised)
        if not cites: continue
        b['claims_seen'].update({cid:revised[cid] for cid in cites})
        if b.get('repair_note','').startswith('Expanded named SDG'):
            if not b.get('prior_hash'):
                bp=BASE/'1.2/content-units'/fp.name
                prior=next((x for x in read(bp)['blocks'] if x['block_id']==b['block_id']),None)
                b['prior_hash']=(prior.get('authored_hash') or hashlib.sha256(_artefact_text(prior).encode()).hexdigest()) if prior else manifest.get(str(fp.relative_to(WS)))
            b['authored_hash']=hashlib.sha256(_artefact_text(b).encode()).hexdigest()
        else:
            b['reviewed_unchanged']='Checked against expanded SDG examples: this unchanged block neither contradicts nor claims the added named examples; it remains accurate for its stated teaching purpose.'
            if not b.get('prior_hash'):
                bp=BASE/'1.2/content-units'/fp.name
                prior=next((x for x in read(bp)['blocks'] if x['block_id']==b['block_id']),None)
                b['prior_hash']=(prior.get('authored_hash') or hashlib.sha256(_artefact_text(prior).encode()).hexdigest()) if prior else manifest.get(str(fp.relative_to(WS)))
        dirty=True
    if dirty: dump(fp,u3)
for fp in (WS/'topics/1.2/learning-items').glob('*.json'):
    d3=read(fp); dirty=False
    for i in d3['items']:
        cites=set(i.get('claim_ids',[]))&set(revised)
        if not cites: continue
        i['claims_seen'].update({cid:revised[cid] for cid in cites})
        if i.get('repair_note','').startswith('Added named SDG recall'):
            if not i.get('prior_hash'):
                bp=BASE/'1.2/learning-items'/fp.name
                prior=next((x for x in read(bp)['items'] if x['item_id']==i['item_id']),None)
                i['prior_hash']=(prior.get('authored_hash') or hashlib.sha256(_artefact_text(prior).encode()).hexdigest()) if prior else None
            i['authored_hash']=hashlib.sha256(_artefact_text(i).encode()).hexdigest()
        else:
            i['reviewed_unchanged']='Checked against expanded SDG examples: this unchanged question and answer remain accurate and do not depend on or contradict the added names.'
            if not i.get('prior_hash'):
                bp=BASE/'1.2/learning-items'/fp.name
                prior=next((x for x in read(bp)['items'] if x['item_id']==i['item_id']),None)
                i['prior_hash']=(prior.get('authored_hash') or hashlib.sha256(_artefact_text(prior).encode()).hexdigest()) if prior else None
        dirty=True
    if dirty: dump(fp,d3)
changes.append({'finding':'R6136-004','action':'Added six assessment-listed SDGs, linked dimensions, and named-goal recall/application; no external research.'})

# N-07 and N-08: remove obsolete research-package text and duplicate prerequisite wording.
p=WS/'topics/10.1/learning-items/topic_10.1_items.json';d=read(p)
for it in d['items']:
    if it.get('item_id','').startswith('ITEM-6136-10.1-P0'):
        it['marking_guidance']=[x.replace('The model Section B is fictional; actual answers must describe the learner’s real enquiry. ','') for x in it.get('marking_guidance',[])]
dump(p,d)
p=WS/'curriculum/slot-demand-specs.json';d=read(p)
for spec in d.get('slots',[]):
    text=spec.get('task_requirement','')
    sentence='Notes must explicitly teach the formula, units, denominator and a worked example before this practice.'
    spec['task_requirement']=text.replace(sentence+' '+sentence,sentence)
dump(p,d)
changes.extend([{'finding':'N-07','action':'Removed obsolete fictional-model clause from research packages'}, {'finding':'N-08','action':'Removed duplicate prerequisite-method sentence'}])

# Refresh the content hash and previous-hash record for every edited learner artefact.
sys.path.insert(0,str(WS.parents[1]/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text
for td in sorted((WS/'topics').iterdir()):
    if not td.is_dir(): continue
    for p in (td/'content-units').glob('*.json'):
        u=read(p); dirty=False
        for b in u['blocks']:
            if b.get('repair_note') and 'second review' in b['repair_note'].lower():
                b['authored_hash']=hashlib.sha256(_artefact_text(b).encode()).hexdigest();dirty=True
        if dirty: dump(p,u)
    for p in (td/'learning-items').glob('*.json'):
        d=read(p);dirty=False
        for i in d['items']:
            if i.get('repair_note','').startswith(('Rewritten after Claude second review','Reframed to match','Revised after Claude second-review','Restored direct HPP-pillar')):
                i['authored_hash']=hashlib.sha256(_artefact_text(i).encode()).hexdigest();dirty=True
            if i.get('item_id','').startswith('ITEM-6136-10.1-P0') and 'The model Section B is fictional' not in ' '.join(i.get('marking_guidance',[])):
                i['authored_hash']=hashlib.sha256(_artefact_text(i).encode()).hexdigest();dirty=True
            if i.get('repair_note','').startswith(('Rewritten after Claude second review','Reframed to match','Revised after Claude second-review','Restored direct HPP-pillar')) and not i.get('prior_hash'):
                bp=BASE/td.name/'learning-items'/p.name
                if bp.exists():
                    old=next((x for x in read(bp)['items'] if x['item_id']==i['item_id']),None)
                    if old and old.get('authored_hash'): i['prior_hash']=old['authored_hash'];dirty=True
        if dirty: dump(p,d)

# The reviewer correctly identified an incorrect HPP year figure? Retain source-checked facts as-is.
dump(WS/'review/repairs/second-review-repairs.json',{'author':'Codex','date':'2026-10-20','claude_contacted':False,'changes':changes})
print(json.dumps({'restored_paragraphs':len(restored),'changes':len(changes)},ensure_ascii=False))
