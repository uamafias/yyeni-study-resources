"""Compose author-supplied concept/application packets into the approved slots.

No source-classification or domain facts are inferred here. Per-topic packets
provide precise concepts, original contexts, analysis and decisions.
"""
import re
from authoring_support import WS,REG,MIS,read,build

def sentences(text):return [x.strip() for x in re.split(r'(?<=[.!?])\s+',text) if x.strip()]

def compose(topic,parents,member_packets,case,miscon_packets=None,review_note=None,extra_evidence=None):
    """Parent packet: heading, teaching, context, application, imperative remainder.
    Member packet: same fields; exact labels map to the planned registry members.
    All text is original authored data except explicitly used syllabus glossary.
    """
    wo=read(WS/'topics'/topic/'work_order.json');blue=read(WS/'topics'/topic/'performance-blueprints.json')['packages']
    payload={};lessons={};members={};cards={};miscon_cards={}
    for suffix,p in parents.items():
        oid=f'OBJ-6144-{topic}.{suffix}';payload[oid]=p
        lessons[suffix]=(p[0],p[1],p[2]+' '+p[3])
    for oid,p in member_packets.items():payload[oid]=p;members[oid]=(p[0],p[1],p[2]+' '+p[3])
    for slot in wo['item_slots']:
        oid=slot['objective_id'];st=slot['subtype'];head,teach,context,application,task=payload[oid][:5]
        if st=='MISCON':
            m=MIS[slot['misconception_entry']]
            if miscon_packets and m['entry_id'] in miscon_packets:q,a=miscon_packets[m['entry_id']]
            else:
                q='Explain the distinction in the following original situation. '+context+' The distinction concerns '+m['a'].lower()+'.'
                a=m['b']+' '+m['test']+' In this situation, the distinction must be applied to the action or group actually described, rather than substituting the other category.'
            miscon_cards[m['entry_id']]=(q,a);continue
        if len(payload[oid])>5 and st in payload[oid][5]:q,a=payload[oid][5][st]
        elif st=='DEF':q='Define '+head.lower()+'.';a=teach
        elif st=='FEATURE':q='State two '+task.rstrip('.').rstrip('?')+'.';a=teach
        elif st in ['CALC','INTERP'] and len(payload[oid])>5:
            q,a=payload[oid][5][st]
        elif st=='DIST':q='Distinguish '+task.rstrip('.')+'. '+context;a=teach+' '+application
        elif st=='EVAL':q='Evaluate '+task.rstrip('.')+'. '+context;a=teach+' '+application
        elif st=='PROC':q=slot['command_word']+' '+task.rstrip('.')+'. '+context;a=teach+' '+application
        elif st=='SYNTH':q='Explain '+task.rstrip('.')+'. '+context;a=teach+' '+application
        else:q=slot['command_word']+' '+task.rstrip('.')+'. '+context;a=teach+' '+application
        cards.setdefault(oid,{})[st]=(q,a)
    ids=case['objectives']
    assert set(ids)==set(blue[0]['objective_ids'])
    supporting='\n\n'.join(payload[oid][1]+' '+payload[oid][3] for oid in ids)
    performance={}
    for bp in blue:
        key=bp['item_type'];facts=case['facts'] if key in ['short_answer','data_response'] else case['alternative_facts']
        if key=='case_analysis':facts+=' '+case['changed']
        if key=='short_answer':
            asks=case['p1_questions'];answers=case['p1_answers']
        elif key=='data_response':asks=case['p2_questions'];answers=case['p2_answers']
        elif key=='essay_plan':
            asks=case['essay_question'];answers=case['essay_answer']
        else:asks=case['case_questions'];answers=case['case_answers']
        performance[key]=(facts+'\n\n'+asks,answers)
    return build(topic,lessons,members,cards,miscon_cards,performance,review_note=review_note,extra_evidence=extra_evidence)
