"""R6 narrow figure taxonomy/status overlay and derived representation index.

No complete figure-content audit, same-type problem claim, or learner image right
is inferred. Main builder calls apply(items) after apply_textbook_r6.apply; then
write_comparisons(items) after canonical assembly. This tool never writes inventory.
"""
import collections
import copy
import json
from pathlib import Path
from analysis_sources import A, WB, ROOT, digest, write

KINDS = ['given-figure', 'teaching-figure']
NOT_CHECKED = 'not checked; not design evidence until checked'
INPUT = WB / 'tools/textbook-figure-repairs-r6.json'
COMPARISONS = A / 'textbook-figure-comparisons-r6.json'


def _figures(items):
    return [i for i in items if i.get('item_kind') in KINDS]


def _parts():
    return {p['part_id']: p for q in json.loads((A/'question-analysis.json').read_text())['questions'] for p in q['parts']}


def _demands(i):
    return sorted(set(i.get('assessed_8227_demand_ids',[]) + i.get('component_demand_ids',[]) +
                      i.get('teaches_8227_demand_ids',[]) + i.get('supports_8227_demand_ids',[])))


def compare(i, parts):
    """A medium-level comparison, deliberately narrower than task equivalence."""
    if i.get('figure_medium_review_r7'):
        from apply_textbook_source_repairs_r7 import compare_figure
        return compare_figure(i,parts)
    ds=set(_demands(i))
    overlap={pid:p for pid,p in parts.items() if ds & set(p['directly_assessed_demand_ids'])}
    rep=i['representation'];graphic=i['figure_record_type']=='graphic'
    # A legacy `table` figure can be a numeric table, a flow chart or number-line
    # composite. Do not pretend an exam medium is the exact subtype seen here.
    media=i['figure_comparison_media_r6']
    givens=[pid for pid,p in overlap.items() if p['given_representation']['kind']in media]
    sketches=[pid for pid,p in overlap.items() if 'graph'in media and p['response_format']=='sketch']
    usable=lambda pid:parts[pid]['disposition']=='include' and not parts[pid].get('hold_ids')
    observed=sorted(pid for pid in set(givens+sketches) if usable(pid)) if graphic else []
    held=sorted(pid for pid in set(givens+sketches) if not usable(pid)) if graphic else []
    if not graphic:
        status='not a graphic representation; internal text callout'
        relation='Formula/prose/working reference, not an examination diagram pattern. Demand-level practice links do not turn a teaching callout into a learner task.'
    elif observed:
        status='representation medium observed on linked demand; exact figure not equated'
        relation='The cited parts use the recorded graph/diagram medium on at least one linked demand. This does not establish matching labels, geometry, task structure, learner decisions or difficulty; consult the family relations before a same-type claim.'
    else:
        status='same representation medium not recorded for linked demands in sampled NSSCAS parts'
        relation='No usable part with both the linked demand and this recorded given/response medium was found in the 2021–2025 part records. This is bounded corpus evidence, not proof that the syllabus excludes the representation or future examinations cannot use it.'
    return dict(item_id=i['item_id'],figure_record_type=i['figure_record_type'],
        figure_subtype=i['figure_subtype'],source_representation=rep,comparison_media=media,
        source_feature_description=i.get('what_it_shows',i['notes']),
        demand_ids=sorted(ds),status=status,relation=relation,
        examination_part_ids=observed,
        same_medium_given_part_ids=sorted(pid for pid in givens if usable(pid)) if graphic else [],
        sketch_response_part_ids=sorted(pid for pid in sketches if usable(pid)) if graphic else [],
        held_medium_evidence_part_ids=held,
        same_demand_part_ids=sorted(overlap),
        objective_problem_map_pointer='analysis/objective-problem-map.json',
        objective_problem_map_demand_ids=sorted(ds),
        comparison_level='representation medium plus accepted demand links; not figure equivalence or same-type task',
        limitations='Recorded exam-medium tags are the input, not a new reading of every exam page. Source subtype/geometry is retained in source_feature_description. No inference of an exact figure match from shared demand or medium. Content remains unchecked; originals remain internal.')


def apply(items):
    fs=_figures(items);byid={i['item_id']:i for i in fs}
    data=json.loads(INPUT.read_text());entries={r['item_id']:r for r in data['entries']}
    assert len(fs)==1758 and set(entries)==set(byid), 'figure taxonomy population mismatch'
    parts=_parts()
    for iid,i in byid.items():
        r=entries[iid]
        assert (r['pdf_page'],r['source_representation'],r['source_label'])==(i['pdf_page'],i['representation'],i.get('source_label','')),('figure taxonomy locator drift',iid)
        for k in ['figure_record_type','figure_subtype']:
            if k=='figure_record_type'and iid in ['8227:TB:YM:C1:Teaching-figure:48','8227:TB:YM:C1:Teaching-figure:49'] and i.get(k):assert i[k]==r[k],('prior explicit figure type changed',iid)
            i[k]=r[k]
        i['figure_comparison_media_r6']=r['comparison_media']
        i['figure_classification_r6']={k:copy.deepcopy(r[k])for k in ['classification_basis','classification_method','date']}
        i['figure_classification_r6']['author_input']='tools/textbook-figure-repairs-r6.json'
        if r.get('native_page_read'):
            e=json.loads((ROOT/r['native_page_read']['path']).read_text())
            assert digest(ROOT/e['path'])==e['sha256']
            assert digest(ROOT/e['source_path'])==e['source_sha256']
            i['figure_classification_r6']['native_page_read']={**r['native_page_read'],'page_render_sha256':e['sha256']}
        # A reference callout is not extra givens, even where the old generic
        # parent-based census selected `given-figure`.
        if i['figure_record_type']=='text callout':
            if i['item_kind']=='given-figure':
                i['figure_role_repair_r6']=dict(previous='given-figure',current='teaching-figure',
                    reason='The census describes a formula/prose/working callout, not an input graphic the learner must read.',
                    basis='accepted per-item census descriptor; no new claim of a native page read',date='2026-11-22')
            i['item_kind']='teaching-figure'
            if not i.get('figure_role'):i['figure_role']='formula/prose/working reference callout'
        if r.get('figure_role_override'):
            i['figure_role_repair_r6']=dict(previous='given-figure',current='teaching-figure',
                reason=r['figure_role_reason'],basis='native page read; see figure_classification_r6.native_page_read',date='2026-11-22')
            i['item_kind']='teaching-figure';i['figure_role']=r['figure_role_override']
        if 'pending actual-value screening' in str(i.get('value_level_scope_review_status_r5','')):
            i['value_level_scope_review_status_r5']='R6 scope disposition retained from accepted R5 item screen; no additional figure-content audit claimed'
        i['figure_scope_disposition_r6']=dict(status=i['scope_check']['status'],
            basis='Retain the accepted R5 item-level scope/qualifier decisions. Figure taxonomy and representation comparison add no mathematical scope certification.',
            qualifier_decisions=i.get('value_level_scope_decisions',[]),
            excluded_or_qualified_parts=i['scope_check'].get('excluded_or_qualified_parts',[]))
        i['content_check']=NOT_CHECKED
        i['content_check_basis']='No complete figure-content audit is claimed. Named registered defect corrections, census discovery, parent answers and representation comparisons do not certify every visual feature.'
        i['design_use_status']='internal source lead; not design evidence until figure content checked; independent R6 comparison review required'
        i['answer_accuracy_status_r5']='No separate answer task; content_check governs figure mathematics. A parent derivation is not a complete figure audit.'
        prior=i.get('mathematical_feature_review',{})
        prior['status']='Prior feature notes retained; not a complete figure-content audit'
        i['mathematical_feature_review']=prior
        c=compare(i,parts)
        i['exam_representation_check']={k:c[k]for k in ['status','relation','examination_part_ids','same_medium_given_part_ids','sketch_response_part_ids','held_medium_evidence_part_ids','comparison_level','limitations']}
        i['exam_representation_check']['comparison_pointer']='analysis/textbook-figure-comparisons-r6.json#/figures/'+iid
        i['exam_representation_check']['objective_problem_map_pointer']=c['objective_problem_map_pointer']
        i['exam_representation_check']['objective_problem_map_demand_ids']=c['demand_ids']
        assert i['learner_display'] is False
    if any(i.get('figure_medium_review_r7')for i in fs):
        from apply_textbook_source_repairs_r7 import apply as apply_source_r7
        items=apply_source_r7(items,wb=WB)
    validate(items)
    return items


def comparison_index(items):
    parts=_parts();fs=_figures(items)
    rows={i['item_id']:compare(i,parts)for i in fs}
    return dict(schema_version='8227-textbook-figure-comparisons-r6-v1',
        status='author narrow representation comparison; independent review required',
        corpus='NSSCAS8227 Mathematics2021–2025; source scope and defective/held status remain binding',
        counts=dict(total=len(fs),by_type=dict(collections.Counter(i['figure_record_type']for i in fs)),
            by_comparison_status=dict(collections.Counter(r['status']for r in rows.values())),
            content_checked=0,content_not_checked=len(fs)),
        input_sha256=dict(question_analysis=digest(A/'question-analysis.json'),taxonomy=digest(INPUT)),
        figures=rows,
        limits=['The complete source census was independently accepted in R5; this pass classifies its individual descriptions, with named native-page layout spot checks.',
                'No full figure-content audit, exact diagram equivalence or same-type problem claim follows. A graph medium on a common demand is only a representation lead.',
                'Formula/prose tables are text-reference panels; data/state arrays and spatial procedures remain graphics.',
                'Textbook graphics and callouts stay internal; later generated assets require their own design and checking.'])


def validate(items, comparison_index=None):
    from textbook_exam_comparison_r6 import validate_figure_status
    parts=_parts();fs=_figures(items)
    assert len(fs)==1758
    for i in fs:
        validate_figure_status(i)
        assert i['figure_record_type']in['graphic','text callout']
        assert i['content_check']==NOT_CHECKED and i['learner_display'] is False
        c=i['exam_representation_check']
        assert c.get('comparison_pointer') and c.get('comparison_level')
        expected=compare(i,parts)
        for key in ['status','examination_part_ids','same_medium_given_part_ids','sketch_response_part_ids','held_medium_evidence_part_ids']:
            assert c[key]==expected[key],('figure representation comparison drift',i['item_id'],key)

        for pid in c['examination_part_ids']:
            assert pid in parts
            assert set(_demands(i))&set(parts[pid]['directly_assessed_demand_ids'])
            assert parts[pid]['disposition']=='include'and not parts[pid].get('hold_ids')
        if comparison_index is not None:
            row=comparison_index['figures'][i['item_id']]
            assert row['examination_part_ids']==c['examination_part_ids']
            assert row['figure_record_type']==i['figure_record_type']
    return dict(total=len(fs),by_type=dict(collections.Counter(i['figure_record_type']for i in fs)),
        by_comparison_status=dict(collections.Counter(i['exam_representation_check']['status']for i in fs)),
        explicit_not_checked=sum(i['content_check']==NOT_CHECKED for i in fs),
        reference_callout_role_repairs=sum(bool(i.get('figure_role_repair_r6'))for i in fs))


def write_comparisons(items):
    index=comparison_index(items);validate(items,index);write(COMPARISONS,index)
    lines=['# Textbook figure representation comparison — NSSCAS8227 R6','',
        'Author narrow comparison; independent check required. No full figure-content audit or learner-image reuse is approved.','',
        '```json',json.dumps(index['counts'],indent=2),'```','',
        'Each source feature and every named exam part is in the JSON index. The objective map supplies task-family relations. Medium plus demand overlap does not prove the same geometry or problem type.','',
        '| Figure | Type | Source feature | Representation result | NSSCAS parts |','|---|---|---|---|---|']
    for iid,r in index['figures'].items():
        clean=lambda s:str(s).replace('|','\\|').replace('\n',' ')
        lines.append('| '+' | '.join(map(clean,[iid,r['figure_record_type'],r['source_feature_description'],r['status'],', '.join(r['examination_part_ids'])or'none recorded']))+' |')
    (A/'textbook-figure-comparisons-r6.md').write_text('\n'.join(lines)+'\n')
    return validate(items,index)


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--write-comparisons',action='store_true');p.add_argument('--dry-check',action='store_true');args=p.parse_args()
    items=json.loads((A/'textbook-inventory.json').read_text())['items']
    if args.dry_check:items=apply(items)
    print(json.dumps(write_comparisons(items)if args.write_comparisons else validate(items),indent=2))
