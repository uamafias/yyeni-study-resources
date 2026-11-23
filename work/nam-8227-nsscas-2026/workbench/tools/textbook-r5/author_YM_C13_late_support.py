"""Shared author-only helpers for the final, fixed-source Chapter 13 readings.

These save source-analysis records, never renewable learner questions.
"""
import hashlib,json
import author_YM_C13_opening as a
import author_YM_C13_iteration_examples as b
from author_YM_C13_opening import W,SRC,SHA,pp,compute,expression,equivalent,extra
ROOTG=a.ROOTG;BRACKET=a.BRACKET
RELATE=b.RELATE;REARRANGE=b.REARRANGE;ITERATE=b.ITERATE;STOP=b.STOP
CONVERGE='8227:2020:M2:T6:O02:D01';FAIL='8227:2020:M2:T6:O02:D02'

def ev(page):
    name=('YM-C13-key-657' if 657<=page<=660 else
          'YM-C13-key-653' if 653<=page<=656 else
          f'YM-C13-{560+4*((page-560)//4)}-source')
    p=W/f'checks/r5/textbooks/{name}.png'
    return dict(path=str(p.relative_to(W.parents[2])),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
a.ev=ev;b.ev=ev;a.h.common.base.ev=ev
answers=a.answers;new=a.new;corrections=a.corrections;figures=a.figures
def reset():
    for group in [answers,new,corrections,figures]:group.clear()

def add(kind,n,page,note,parts,rep='text',fresh=False):
    r=a.add(kind,n,page,note,parts,new_item=fresh)
    r.update(representation=rep,
        mapping_rationale='Map each requested outcome, not every calculation used to reach it. Preserve supplied versus derived recurrence, the selected real root, connected-part dependencies, and stipulated versus freely chosen starts. Formal convergence tests are outside LIMIT08.',
        scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:LIMIT08']),
        value_level_scope_decisions=[dict(rule_id='8227:LIMIT08',status='within',quoted_value=note,reason='Use the supplied recurrence or a provided rearrangement and interpret convergence qualitatively; no formal derivative convergence condition required.')],
        precision_angle_check=dict(source=note,comparison='Full internal iteration states; round only displays and the final response at their independently stated precisions. Trigonometric arguments are radians. A book display preference is not an official NSSCAS convention.'))
    for p in parts:
        p['given_representation']=rep
        p.setdefault('response_format','symbolic')
    return r

def reason(label,key,method,kp,ds,status='show/prove',rep='text'):
    p=a.a.reasoning(label,key,method,kp,status)
    p.update(assessed_8227_demand_ids=ds,component_demand_ids=[],response_format='proof/show-that' if status=='show/prove' else 'explanation',given_representation=rep)
    return p

def val(label,expr,key,kp,ds,method):return b.val(label,expr,key,kp,ds,method)

def sequence_sf(prefix,F,start,keys,state_sf,kp,equation,bracket,final,final_sf,policy):
    """Significant figures are a separate source requirement from decimal places."""
    parts=b.sequence_parts(prefix,F,start,keys,4,kp,equation,bracket,final,2,policy)
    for p in parts[:-1]:
        p['operation']['rounding']=dict(significant_figures=state_sf)
        p['display_precision']=str(state_sf)+' significant figures'
    p=parts[-1];p['operation']['rounding']=dict(significant_figures=final_sf)
    p['requested_precision']=str(final_sf)+' significant figures'
    for op in p['additional_operations'].values():op['rounding']=dict(significant_figures=final_sf)
    return parts

def panel(n,page,title,note,ds,rep='table',parent=None,given=False,checks=()):
    a.fig(n,page,title,note,ds,rep,list(checks),parent)
    r=figures[-1]
    r.update(item_id=f'8227:TB:YM:C13:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),
             item_kind='given-figure' if given else 'teaching-figure',
             parent_item_id=f'8227:TB:YM:C13:{parent}' if parent else None,value_level_scope_decisions=[])
    r['mathematical_feature_review']['method']='Read the source panel and independently recompute its values, domains or geometric features. Given assets, worked answers and teaching diagrams remain distinct; source defects are recorded separately.'
    return r

def census(start,end,notes,continuations=None):
    continuations=continuations or {}
    return [dict(pdf_page=page,printed_page=pp(page),chapter=13,
        page_status='items enumerated' if any(r['source_pdf_page']==page for r in answers) or any(r['pdf_page']==page for r in figures) else 'prose only',
        item_ids=[r['item_id'] for r in answers if r['source_pdf_page']==page]+[r['item_id'] for r in figures if r['pdf_page']==page],
        continuation_item_ids=continuations.get(page,[]),source_evidence=ev(page),reader='Codex author',date='2026-11-20',
        non_item_content=notes[page],scope_screen='Actual source values and root branches checked. Formal convergence-condition derivations remain extension; numerical recurrence use does not establish that every invented rearrangement is prescribed.') for page in range(start,end+1)]

def save(stem,pages):
    for row in answers:
        for p in row['subparts']:
            if 'operation' in p:
                target=p.get('author_expected_normalised',p.get('printed_key_normalised',p.get('author_check_target_normalised')))
                got=compute(p['operation'])
                if p.get('printed_approximation_check'):
                    tolerance=expression(p['printed_approximation_check']['absolute_error_strictly_below'])
                    assert abs(got-expression(target))<tolerance,(row['item_id'],p['subpart'],str(got),target)
                else:
                    assert equivalent(got,expression(target)),(row['item_id'],p['subpart'],str(got),target)
            for name,op in p.get('additional_operations',{}).items():
                if name in p.get('additional_operation_expected',{}):
                    assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
    for name,data in [(f'answers-YM-C13-{stem}.json',dict(scope=f'Fixed-source Chapter 13 {stem}; each explicit response checked.',items=answers)),
                      (f'census-YM-C13-{stem}.json',dict(book='YM',book_id='8227-SRC-017',chapter=13,source_path=SRC,source_sha256=SHA,scope=f'Complete source-page enumeration for {stem}.',new_items=new+figures,corrections=corrections,pages=pages))]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts']) for r in answers),'responses;',len(figures),'panels;',len(pages),'pages')
