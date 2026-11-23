"""Narrow R7 source, display, locator and figure repairs.

Canonical mathematics is corrected in its three named author scripts. This
module asserts propagation; it does not hide an unrecomputed old answer.
No learner demand link, family membership or source-response identity changes.
"""
import copy
import json
from pathlib import Path
from analysis_sources import WB, ROOT, A, digest

INPUT_NAME='textbook-source-repairs-r7.json'
FIGURES=['given-figure','teaching-figure']


def _wb(wb=None):return Path(wb)if wb is not None else WB

def _read(wb=None):return json.loads((_wb(wb)/'tools'/INPUT_NAME).read_text())

def _parts(wb=None):
    return {p['part_id']:p for q in json.loads((_wb(wb)/'analysis/question-analysis.json').read_text())['questions']for p in q['parts']}

def _demands(i):
    return set(i.get('assessed_8227_demand_ids',[])+i.get('component_demand_ids',[])+i.get('teaches_8227_demand_ids',[])+i.get('supports_8227_demand_ids',[]))

def _evidence(entry,wb=None):
    home=_wb(wb);root=home.parents[2]
    if 'native'in entry:entry=entry['native']
    assert digest(root/entry['render_path'])==entry['render_sha256'],'R7 native render changed'
    assert digest(root/entry['source_path'])==entry['source_sha256'],'R7 source PDF changed'
    return copy.deepcopy(entry)


def compare_figure(i,parts):
    """R6-compatible medium comparison, including learner-sketch readback.

    Independent implementation: never calls the R6 compare function, which may
    delegate here. It does not equate a textbook figure with an exam diagram.
    """
    ds=_demands(i);graphic=i['figure_record_type']=='graphic';media=i.get('figure_comparison_media_r6',[])
    overlap={pid:p for pid,p in parts.items()if ds&set(p['directly_assessed_demand_ids'])}
    usable=lambda pid:parts[pid]['disposition']=='include'and not parts[pid].get('hold_ids')
    givens=[pid for pid,p in overlap.items()if p['given_representation']['kind']in media]if graphic else[]
    sketches=[pid for pid,p in overlap.items()if 'graph'in media and p['response_format']=='sketch']if graphic else[]
    # The source part must itself be a sketch and explicitly linked by a cue;
    # these three native-confirmed cases are not inferred from any prior result.
    readbacks=[];dependencies={}
    for r in i.get('figure_medium_review_r7',{}).get('own_sketch_readbacks',[]):
        pid=r['part_id']
        if not graphic or r['medium']not in media or pid not in overlap:continue
        sources=r['source_sketch_part_ids']
        assert all(s in parts and parts[s]['response_format']=='sketch'for s in sources)
        edges=parts[pid]['dependency_edges']
        assert all(any(e['type']=='cue'and e['from_part']==s.rsplit(':',1)[1]for e in edges)for s in sources),'readback lacks sketch dependency'
        readbacks.append(pid);dependencies[pid]=sources
    allp=set(givens+sketches+readbacks);observed=sorted(pid for pid in allp if usable(pid));held=sorted(pid for pid in allp if not usable(pid))
    if not graphic:
        status='not a graphic representation; internal text callout'
        relation='Formula/prose/working reference, not an examination diagram pattern. Demand-level practice links do not turn a teaching callout into a learner task.'
    elif observed:
        status='representation medium observed on linked demand; exact figure not equated'
        relation='The cited parts use this graph/diagram medium on a linked demand as givens, a sketch response, or an explicit reading of the learner’s own sketch. Shared medium and demand do not establish matching geometry, values, learner decisions or difficulty.'
    else:
        status='same representation medium not recorded for linked demands in sampled NSSCAS parts'
        relation='No usable part with both the linked demand and this recorded given, response or own-sketch-reading medium was found in the2021–2025 part records. This bounded corpus absence does not remove the representation from syllabus scope.'
    return dict(item_id=i['item_id'],figure_record_type=i['figure_record_type'],figure_subtype=i['figure_subtype'],
        source_representation=i['representation'],comparison_media=media,source_feature_description=i.get('what_it_shows',i['notes']),
        demand_ids=sorted(ds),status=status,relation=relation,examination_part_ids=observed,
        same_medium_given_part_ids=sorted(pid for pid in givens if usable(pid)),
        sketch_response_part_ids=sorted(pid for pid in sketches if usable(pid)),
        own_sketch_readback_part_ids=sorted(pid for pid in readbacks if usable(pid)),
        own_sketch_dependencies=dependencies,held_medium_evidence_part_ids=held,same_demand_part_ids=sorted(overlap),
        objective_problem_map_pointer='analysis/objective-problem-map.json',objective_problem_map_demand_ids=sorted(ds),
        comparison_level='representation medium plus accepted demand links; not figure equivalence or same-type task',
        limitations='R7 separates vector-grid geometry from function graphs and counts the three native-confirmed own-sketch-reading targets. Exact figure/task equivalence requires the family evidence. All figure content checks remain explicitly unchecked.')


def apply(items,wb=None):
    home=_wb(wb);data=_read(home);byid={i['item_id']:i for i in items};parts=_parts(home)
    defects=json.loads((home/'analysis/textbook-corrections-r7.json').read_text())['entries']
    for d in defects:
        i=byid[d['item_id']];_evidence(d['source_evidence'],home)
        marker=dict(defect_id=d['defect_id'],issue=d['issue'],correct_answer=d['correct_answer'],source='textbook-corrections-r7.json')
        i['defects']=[r for r in i['defects']if not(r.get('source')=='textbook-corrections-r7.json'and r.get('defect_id')==d['defect_id'])]+[marker]
        i.setdefault('source_defect_ids_r7',[])
        if d['defect_id']not in i['source_defect_ids_r7']:i['source_defect_ids_r7'].append(d['defect_id'])
        i['answer_key']['source_defects']=copy.deepcopy(i['defects'])
    for correction in data['response_corrections']:
        i=byid[correction['item_id']];row=next(r for r in i['answer_verification_r5']if r['subpart']==correction['subpart'])
        for key,value in correction['corrected_fields'].items():assert row.get(key)==value,('R7 canonical mathematical correction not propagated',i['item_id'],key)
        assert row['status']==correction['correct_status']and row['printed_key_normalised']==correction['printed_key_normalised']
        assert i['notes']==correction['corrected_note'],'obsolete whitespace repair replaced the corrected source note'
        row['source_correction_r7']=dict(author_input='tools/'+INPUT_NAME,date=data['date'],source_pdf_page=correction['source_pdf_page'],key_pdf_page=correction['answer_pdf_page'])
    for r in data['answer_page_repairs']:
        i=byid[r['item_id']]
        for label in r['subparts']:
            row=next(a for a in i['answer_verification_r5']if a['subpart']==label)
            assert row['answer_pdf_page']==r['answer_pdf_page']and row['answer_printed_page']==r['answer_printed_page'],('R7 canonical locator correction not propagated',i['item_id'],label)
        assert r['answer_pdf_page']in i['answer_key']['pdf_pages']
        i['answer_locator_confirmation_r7']=dict(source='tools/'+INPUT_NAME,native=_evidence(r,home),reason=r['reason'])
    patches={r['item_id']:r for r in data['figure_repairs']}
    for i in items:
        if i.get('item_kind')not in FIGURES:continue
        r=patches.get(i['item_id'])
        if r:
            for key in['item_kind','figure_role','figure_record_type','figure_subtype']:
                if key in r:i[key]=r[key]
            if 'comparison_media'in r:i['figure_comparison_media_r6']=r['comparison_media']
            i['figure_repair_r7']=dict(reason=r['reason'],author_input='tools/'+INPUT_NAME,date=data['date'])
            if r.get('native'):i['figure_repair_r7']['native']=_evidence(r,home)
        i['figure_medium_review_r7']=dict(author_input='tools/'+INPUT_NAME,date=data['date'],own_sketch_readbacks=data['own_sketch_readbacks'])
        c=compare_figure(i,parts)
        old=i['exam_representation_check']
        for key in['status','relation','examination_part_ids','same_medium_given_part_ids','sketch_response_part_ids','held_medium_evidence_part_ids','comparison_level','limitations','own_sketch_readback_part_ids','own_sketch_dependencies']:
            old[key]=c[key]
        old['comparison_pointer']='analysis/textbook-figure-comparisons-r6.json#/figures/'+i['item_id']
    return items


def apply_answer_page_audit(audit,wb=None):
    """Return corrected audit records; caller owns writing the generated file."""
    data=_read(wb);audit=copy.deepcopy(audit)
    lookup={(r['book'],r['pdf_page']):r for r in audit['pages']}
    for patch in data['page_observation_repairs']:
        r=lookup[patch['book'],patch['pdf_page']]
        r.setdefault('previous_top_observation_r6',r['top_observation'])
        r.setdefault('previous_read_date_r6',r['read_date'])
        r.update(top_observation=patch['top_observation'],read_date=data['date'],r7_native_confirmation=_evidence(patch,wb))
    known={(r['item_id'],tuple(r['subparts']))for r in audit['findings']}
    for patch in data['answer_page_repairs']:
        key=(patch['item_id'],tuple(patch['subparts']))
        if key not in known:audit['findings'].append(copy.deepcopy(patch))
    audit['r7_repairs']=dict(author_input='tools/'+INPUT_NAME,read_date=data['date'],corrected_page_observations=4,additional_locator_findings=2)
    return audit


def apply_family_selected_results(families,items,wb=None):
    data=_read(wb);byid=items if isinstance(items,dict)else{i['item_id']:i for i in items};rows=families['families']if isinstance(families,dict)else families
    patches={(r['item_id'],r['subpart']):r for r in data['selected_result_repairs']}
    corrected={(r['item_id'],r['subpart']):r for r in data['response_corrections']}
    for f in rows:
        trig=f['family_id']==data['trig_selected_result_family_id']
        for m in f['members']:
            actual={r['subpart']:r for r in byid[m['item_id']].get('answer_verification_r5',[])}
            selected=[];changed=False
            for label in m['part_labels']:
                r=actual[label];key=(m['item_id'],label);entry=None
                if key in patches:
                    p=patches[key];entry=dict(subpart=label,kind=p['kind'],result=p['result'],source_native=p['native'])
                    if p.get('latex'):entry['latex']=p['latex']
                    changed=True
                elif trig and r.get('working'):
                    # Full, explicitly named feature keys, never a sliced repr.
                    selected_features=list(r.get('printed_key_features',{}))
                    fields={k:v for k,v in r['working'].items()if k in selected_features}
                    if not fields:fields=copy.deepcopy(r['working'])
                    entry=dict(subpart=label,kind='complete named requested sketch/reference features',result=fields,
                        complete_computed_features=copy.deepcopy(r['working']),feature_role='Author-computed reference features; extra computed fields do not become additional assessed demands.')
                    changed=True
                elif key in corrected:
                    p=corrected[key]
                    for k,v in p['corrected_fields'].items():assert r.get(k)==v
                    entry=dict(subpart=label,kind='corrected original integrand and exact finite result',result=r['derived_answer'],method=r['method'])
                    changed=True
                    for response in m.get('membership_evidence_r6',{}).get('responses',[]):
                        if response['subpart']==label:
                            for k in['method','derived_answer','derivation_inputs','source_input_sha256']:response[k]=copy.deepcopy(r[k])
                else:entry=dict(subpart=label,kind='existing independently derived source response',result=r.get('derived_answer'))
                selected.append(entry)
            if changed:
                m['selected_response_results_r7']=selected
                def show(v):return json.dumps(v,ensure_ascii=False,sort_keys=True)if isinstance(v,dict)else str(v)
                m['membership_reason']='Selected responses for '+m['item_id']+': '+'; '.join(e['subpart']+' = '+show(e.get('latex',e['result']))for e in selected)+'.'
                m['selected_result_evidence_r7']=dict(author_input='tools/'+INPUT_NAME,date=data['date'],basis='Native source checks and independently derived requested forms/features. CAS-normalised mathematical answers are retained separately.')
    return families


def validate(items,families=None,wb=None):
    data=_read(wb);byid={i['item_id']:i for i in items};parts=_parts(wb)
    for r in data['native_readings']:_evidence(r,wb)
    for c in data['response_corrections']:
        row=next(r for r in byid[c['item_id']]['answer_verification_r5']if r['subpart']==c['subpart'])
        assert {k:row.get(k)for k in c['corrected_fields']}==c['corrected_fields'],'incorrect original-integrand correction'
        assert row['status']==c['correct_status']
    for r in data['answer_page_repairs']:
        i=byid[r['item_id']]
        assert all(next(a for a in i['answer_verification_r5']if a['subpart']==s)['answer_pdf_page']==r['answer_pdf_page']for s in r['subparts']),'wrong corrected key page'
    for r in data['figure_repairs']:
        i=byid[r['item_id']]
        for k in['item_kind','figure_role','figure_record_type','figure_subtype']:
            if k in r:assert i[k]==r[k],('unapplied R7 figure patch',i['item_id'],k)
        if'comparison_media'in r:assert i['figure_comparison_media_r6']==r['comparison_media']
    for i in items:
        if i.get('item_kind')not in FIGURES:continue
        c=compare_figure(i,parts)
        for key in['examination_part_ids','own_sketch_readback_part_ids','own_sketch_dependencies']:
            assert i['exam_representation_check'][key]==c[key],('R7 figure medium drift',i['item_id'],key)
        assert i['content_check']=='not checked; not design evidence until checked'and i['learner_display']is False
    if families is not None:
        rows=families['families']if isinstance(families,dict)else families
        for patch in data['selected_result_repairs']:
            matches=[m for f in rows for m in f['members']if m['item_id']==patch['item_id']and patch['subpart']in m['part_labels']]
            assert matches,('requested result lost its source response',patch['item_id'],patch['subpart'])
            for m in matches:
                selected=next(r for r in m['selected_response_results_r7']if r['subpart']==patch['subpart'])
                assert selected['result']==patch['result'],'incorrect selected completed form/attaining angle'
        for f in rows:
            if f['family_id']!=data['trig_selected_result_family_id']:continue
            for m in f['members']:
                assert 'selected_response_results_r7'in m
                assert 'window_m…'not in m['membership_reason']and 'window_m...'not in m['membership_reason'],'truncated sketch feature key'
                for r in m['selected_response_results_r7']:
                    if r['kind']=='complete named requested sketch/reference features':
                        assert set(r['result'])<=set(r['complete_computed_features'])
                        assert 'window_domain'in r['complete_computed_features']and 'window_range'in r['complete_computed_features']
    return dict(status='author named source/locator/medium repairs checked; independent review required',**data['counts'])
