"""Assemble authored exercise-family and demand-insight evidence.

Membership is authored explicitly. This builder neither clusters by topic nor
changes the independent item-to-demand coverage. These are analysis groups,
not recipes, work orders, marking criteria or delivery selections.
"""
import argparse,collections,copy,json
from analysis_sources import A,WB,ROOT,write,digest

FAMILY_FIELDS=['title','learner_decisions','givens_and_unknowns','constraints',
               'representation_and_response','scaffolding_and_connected_parts',
               'alternative_methods','units_and_precision','answer_form',
               'difficulty_progression','distinction_basis']
INSIGHT_FIELDS=['teaching_comparison','examination_comparison','difficulty_and_grade_bounds',
                'pitfalls','gaps_and_representations','implications_for_step3']

def validate_response_exclusions(records,items):
    """An explicit excluded source part is resolved,never hidden as a family."""
    excluded=collections.defaultdict(set)
    for row in records:
        assert row['item_id']in items,'excluded response has no source item'
        item=items[row['item_id']]
        answers={a['subpart']for a in item.get('answer_verification_r5',[])}
        assert row['part_labels']and set(row['part_labels'])<=answers,'excluded response has no source label'
        scope=item['scope_check']
        assert scope['status']=='in-scope-parts-only','unwarranted response exclusion'
        assert row['reason']and row['quoted_value'],'response exclusion lacks evidence'
        assert all(any(s.startswith(label+':')for s in scope['excluded_or_qualified_parts'])for label in row['part_labels']),'response exclusion disagrees with named source scope'
        assert any(d['rule_id']==row['rule_id']and d['status']=='outside'and d.get('applies_to')==row['applies_to']and d['quoted_value']==row['quoted_value']for d in item.get('value_level_scope_decisions',[])),'response exclusion lacks matching actual-value decision'
        assert not(excluded[row['item_id']]&set(row['part_labels'])),'duplicate response exclusion'
        excluded[row['item_id']].update(row['part_labels'])
    return excluded

def assemble():
    inventory=json.loads((A/'textbook-inventory.json').read_text())
    items={i['item_id']:i for i in inventory['items']}
    registry=json.loads((A/'demand-registry.json').read_text())
    demands={d['demand_id']:d for d in registry['demands']}
    questions=json.loads((A/'question-analysis.json').read_text())['questions']
    exam_parts={p['part_id']:p for q in questions for p in q['parts']}
    patterns={p['pattern_id']:p for p in json.loads((A/'problem-patterns.json').read_text())['patterns']}
    grades={g['descriptor_id']:g for g in json.loads((WB.parent/'curriculum/grade-descriptions.json').read_text())['descriptors']}
    conventions={r['rule_id']:r for r in json.loads((A/'marking-conventions.json').read_text())['rules']}
    errors={e['error_id']:e for e in json.loads((A/'examiner-difficulties.json').read_text())['entries']}
    families=[];insights=[];sources=[];covered=collections.defaultdict(set)
    inputs=[(path,json.loads(path.read_text()))for path in sorted((WB/'tools/textbook-r5').glob('synthesis-*.json'))]
    raw={}
    for path,data in inputs:
        for f in data['families']:
            assert f['family_id']not in raw,('duplicate authored family',f['family_id'])
            raw[f['family_id']]=copy.deepcopy(f)
    for path,data in inputs:
        for extension in data.get('family_extensions',[]):
            assert extension['family_id']in raw,('extension has no family',extension['family_id'])
            assert extension['reason'] and extension['member_specs']
            f=raw[extension['family_id']]
            f['member_specs'].extend(extension['member_specs'])
            f.setdefault('additional_source_branches',[]).append(dict(reason=extension['reason'],
                member_item_ids=sorted({m['item_id']for m in extension['member_specs']}),source_input=str(path.relative_to(ROOT))))
    # R6 repairs preserve the original author inputs and all accepted item links.
    # A new split belongs to its original source input for deterministic assembly.
    from textbook_family_repairs_r6 import (apply_repairs,member_id,
        validate_member_demands,validate_response_disposition)
    original_ids={str(path):{f['family_id']for f in data['families']}for path,data in inputs}
    raw,repair_changes=apply_repairs(raw,items)
    for path,data in inputs:
        ids=original_ids[str(path)]
        data['families']=[r for r in raw.values()
            if r.get('r6_origin_family_id',r['family_id'])in ids]
    write(WB/'checks/r6/family-membership-changes.json',dict(
        status='working membership repair; examination comparison not started',changes=repair_changes))
    for path,data in inputs:
        assert data['authorship']=='Codex author; independent review pending'
        sources.append(dict(path=str(path.relative_to(ROOT)),sha256=digest(path),scope=data['scope']))
        for record in data['families']:
            row=copy.deepcopy(raw[record['family_id']])
            assert all(row.get(f) for f in FAMILY_FIELDS),('incomplete family',row['family_id'])
            assert row['member_specs'] and set(row['assessed_demand_ids'])<=set(demands)
            members=[]
            for spec in row.pop('member_specs'):
                iid=spec['item_id'];assert iid in items,('unknown textbook family member',iid)
                item=items[iid];assert item.get('item_kind')not in ['teaching-figure','given-figure']
                validate_member_demands(row,item)
                answers={a['subpart']:a for a in item.get('answer_verification_r5',[])}
                labels=list(answers)if spec['parts']=='*'else spec['parts']
                assert labels and set(labels)<=set(answers),('unknown family response parts',iid,labels)
                validate_response_disposition(row,dict(part_labels=labels),item)
                assert spec.get('membership_reason'),('membership needs a decision-based reason',iid)
                covered[iid].update(labels)
                members.append(dict(member_id=member_id(row['family_id'],iid,labels),item_id=iid,part_labels=labels,
                    membership_scope='whole item'if set(labels)==set(answers)else'named responses within a preserved connected item',
                    membership_reason=spec['membership_reason'],
                    source_path=item['source_path'],source_sha256=item['source_sha256'],
                    pdf_page=item['pdf_page'],printed_page=item['printed_page'],
                    continuation_pdf_pages=item['continuation_pdf_pages'],
                    answer_pdf_pages=sorted({a['answer_pdf_page'] for label,a in answers.items()if label in labels and a['answer_pdf_page']is not None}),
                    source_scope=item['scope_check'],source_defect_ids=item.get('source_defect_ids_r5',[]),
                    design_use_status='Internal comparative evidence only; source defects and scope boundaries remain binding.',
                    learner_display=False))
            row['members']=members;row['member_item_ids']=sorted({m['item_id']for m in members})
            mapped={d for iid in row['member_item_ids']for d in items[iid]['assessed_8227_demand_ids']}
            assert set(row['assessed_demand_ids'])<=mapped,('family claims a demand unsupported by its item mappings',row['family_id'],sorted(set(row['assessed_demand_ids'])-mapped))
            row['book_ids']=sorted({items[i]['book_id']for i in row['member_item_ids']})
            row['source_basis']='textbook-derived'
            row['not_a_recipe_count']=True
            row['status']='author family judgement; independent review pending'
            relation=row['examination_relation'];kind=relation['kind']
            assert kind in ['same type as','structural branch','textbook-only']
            assert relation['reason']
            if kind=='textbook-only':
                assert not relation['part_ids']
                assert relation['evidence_label']=='textbook-derived'
            else:
                assert relation['part_ids'] and relation['pattern_ids']
                for pid in relation['part_ids']:
                    assert pid in exam_parts and exam_parts[pid]['disposition']=='include' and not exam_parts[pid].get('hold_ids'),('invalid/held exam anchor',pid)
                for pattern in relation['pattern_ids']:assert pattern in patterns
            row['examination_evidence']=[dict(part_id=p,paper_locator=exam_parts[p]['paper_locator'],
               directly_assessed_demand_ids=exam_parts[p]['directly_assessed_demand_ids'],
               response_format=exam_parts[p]['response_format'],
               comparison_only=True)for p in relation['part_ids']]
            row['connected_item_rule']='Named-response membership never separates the source question or its dependencies into approved standalone recipes.'
            row['claim_evidence_item_ids']=row['member_item_ids']
            if len(row['members'])==1:
                previous=row.get('difficulty_progression','')
                if previous!='single item':
                    row['single_item_variation_note']=previous
                row['difficulty_progression']='single item'
            families.append(row)
        for record in data.get('insights',[]):
            row=copy.deepcopy(record)
            assert all(row.get(f) for f in INSIGHT_FIELDS),('incomplete insight',row['insight_id'])
            assert row['demand_ids'] and set(row['demand_ids'])<=set(demands)
            assert row['evidence_item_ids'] and set(row['evidence_item_ids'])<=set(items)
            assert set(row.get('examination_part_ids',[]))<=set(exam_parts)
            assert set(row.get('grade_descriptor_ids',[]))<=set(grades)
            assert set(row.get('marking_rule_ids',[]))<=set(conventions)
            assert set(row.get('examiner_error_ids',[]))<=set(errors)
            row['source_basis']='author synthesis of separately labelled source evidence; not a PLAN'
            insights.append(row)
    assert len({f['family_id']for f in families})==len(families),'duplicate family identifier'
    assert len({i['insight_id']for i in insights})==len(insights),'duplicate insight identifier'
    response_items=[i for i in items.values()if i.get('item_kind')not in ['teaching-figure','given-figure']]
    part_exclusions=[copy.deepcopy(e)for path,data in inputs for e in data.get('response_exclusions',[])]
    excluded_parts=validate_response_exclusions(part_exclusions,items)
    for e in part_exclusions:
        item=items[e['item_id']]
        e.update(source_path=item['source_path'],source_sha256=item['source_sha256'],pdf_page=item['pdf_page'],printed_page=item['printed_page'],learner_display=False)
    pending=[];excluded=[]
    for item in response_items:
        if item['scope_check']['status']=='out-of-scope':
            excluded.append(dict(item_id=item['item_id'],reason=item['scope_check']['basis'],
                pdf_page=item['pdf_page'],source_path=item['source_path'],source_sha256=item['source_sha256']))
            continue
        expected={a['subpart']for a in item.get('answer_verification_r5',[])}
        missing=expected-covered[item['item_id']]-excluded_parts[item['item_id']]
        if missing or not expected:
            pending.append(dict(item_id=item['item_id'],pending_parts=sorted(missing),
                reason='Family review not complete for these source responses'if expected else'Explicit out-of-scope source activity; no prescribed response population',scope=item['scope_check']['status']))
    insight_demands={d for row in insights for d in row['demand_ids']}
    from apply_textbook_family_prose_parallel_r6 import apply as apply_parallel_family_prose
    families=apply_parallel_family_prose(families,wb=WB)
    from apply_textbook_family_repairs_r7 import apply as apply_family_r7,write_records as write_family_r7
    family_r7_audit=apply_family_r7(families,items,wb=WB)
    write_family_r7(family_r7_audit,wb=WB)
    from textbook_closeout_r7 import apply_family_metadata,patch_gap_records,LIMIT,prose
    families=apply_family_metadata(families,items)
    patch_gap_records()
    for row in insights:row['title']=prose(row['title'])
    from apply_textbook_source_repairs_r7 import apply_family_selected_results
    families=apply_family_selected_results(families,items,wb=WB)
    from build_textbook_relations_r7 import build_for as build_relations_r7
    r7_ledger=build_relations_r7(families,exam_parts,items)
    from textbook_exam_comparison_r6 import attach,rewrite_insight_comparisons
    comparison_counts=attach(families,exam_parts,data=r7_ledger)
    rewrite_insight_comparisons(insights,families,exam_parts)
    from textbook_exact_angles_insight_r7 import repair_exact_special_angle_insight
    repair_exact_special_angle_insight(insights,families,exam_parts)
    for name in ['textbook_family_repairs_r6.py','textbook_exam_comparison_r6.py','textbook-exam-relations-r6.json','apply_textbook_family_repairs_r7.py','textbook-family-repairs-r7.json','build_textbook_relations_r7.py','textbook-relation-decisions-r7.json','textbook-exam-overrides-r7.json','textbook_exact_angles_insight_r7.py','apply_textbook_source_repairs_r7.py','textbook-source-repairs-r7.json','textbook_closeout_r7.py','textbook-closeout-motion-decisions.json','textbook-closeout-curve-decisions.json','textbook-closeout-family-gap-inputs.json','textbook-closeout-cosmetic-inputs.json']:
        path=WB/'tools'/name
        sources.append(dict(path=str(path.relative_to(ROOT)),sha256=digest(path),
            scope='Retained R6 baseline plus scoped R7 family/source repairs, selected-response decisions and native reading evidence'))
    membership_gaps=[dict(family_id=f['family_id'],item_id=m['item_id'],
        part_labels=m['part_labels'],unsupported_family_demand_ids=sorted(
            set(f['assessed_demand_ids'])-set(items[m['item_id']]['assessed_8227_demand_ids'])))
        for f in families for m in f['members']
        if not set(f['assessed_demand_ids'])<=set(items[m['item_id']]['assessed_8227_demand_ids']) and not m.get('family_response_demand_evidence_r7')]
    write(WB/'checks/r6/family-membership-unresolved.json',dict(
        affected_families=len({r['family_id']for r in membership_gaps}),
        affected_memberships=len(membership_gaps),records=membership_gaps))
    # Current propagated family prose and complete comparison decisions establish
    # author synthesis completeness, never independent acceptance or other R6 gates.
    author_complete=not pending and insight_demands==set(demands) and all(
        not f['undecided_exam_part_ids'] for f in families)
    result=dict(schema_version='8227-textbook-synthesis-r7',status='author synthesis complete; independent review pending'if author_complete else'working synthesis; not complete or accepted',
        taxonomy_rule='Families share a discriminating learner decision and response structure; numerical or cosmetic changes alone do not create a family. Explicit branches retain changed reasoning or evidence requirements.',
        source_inputs=sources,families=families,
        progress=dict(families_authored=len(families),response_item_population=len(response_items),
           response_items_with_any_family=sum(bool(v)for v in covered.values()),response_items_with_all_existing_responses_grouped=sum(bool(i.get('answer_verification_r5'))and {a['subpart']for a in i['answer_verification_r5']}<=covered[i['item_id']]for i in response_items),
           response_items_explicitly_excluded=len(excluded),response_items_pending=len(pending),insight_demands_completed=len(insight_demands),demand_population=len(demands)),
        pending_response_items=pending,excluded_response_items=excluded,excluded_response_parts=part_exclusions,insight_demand_ids=sorted(insight_demands),pending_insight_demand_ids=sorted(set(demands)-insight_demands),
        exclusions_and_support_rule='Teaching/given figures retain their independent inventory records and may support a family through parent links. They do not create assessed-question families merely by being separate records.',
        limits=LIMIT+' '+family_r7_audit['limits_note']+' Membership/insight progress only. These counts do not replace part-to-demand coverage, establish exam frequency, approve recipes or accept source defects.')
    result['r7_family_repair_limits']=family_r7_audit['limits_note']
    result['r6_membership_repair']=dict(status='author membership repair; independent check required',
        unresolved_family_count=len({r['family_id']for r in membership_gaps}),
        unresolved_memberships=len(membership_gaps),
        comparison_status='Current R7 decisions over retained R6 baseline; any undecided comparison remains incomplete')
    result['r6_examination_comparison_counts']=comparison_counts
    result['progress']['source_responses_explicitly_excluded']=sum(len(v)for v in excluded_parts.values())
    result['progress']['response_items_with_all_eligible_responses_resolved']=sum(bool(i.get('answer_verification_r5'))and i['scope_check']['status']!='out-of-scope'and {a['subpart']for a in i['answer_verification_r5']}<=covered[i['item_id']]|excluded_parts[i['item_id']]for i in response_items)
    write(A/'textbook-families.json',result)
    # Human-readable family index; full member locators remain in the JSON.
    lines=['# Textbook exercise families — NSSCAS Mathematics 8227','',result['status'],
       '', 'Analysis groups, not recipe counts. Every ungrouped source response remains explicit.','',
       '| Family | Decision | Member items | Relation to inspected examination evidence |',
       '|---|---|---:|---|']
    for f in families:lines.append(f"| {f['family_id']} — {f['title']} | {f['learner_decisions']} | {len(f['member_item_ids'])} | {f['examination_relation']['kind']} |")
    lines+=['',json.dumps(result['progress'],indent=2),'',result['limits']]
    (A/'textbook-families.md').write_text('\n'.join(lines)+'\n')
    out=['# Textbook insights — NSSCAS Mathematics 8227','',
      '**Author synthesis complete; independent review pending.** All source responses are grouped or explicitly excluded; all syllabus demands have an insight section. These are analysis families,not approved recipes.'if author_complete else'**Working synthesis; not ready for independent acceptance.** Only the named sections below are authored. All remaining demands are explicitly listed at the end.','',
      LIMIT,'',
      'Textbook questions remain internal. Syllabus statements bound scope; examination parts and award rows establish observed demands and official marking; textbook methods and planner implications are separate author judgements.','']
    for row in insights:
        out.extend(['## '+row['title'],'','Demands: '+', '.join(row['demand_ids'])+'.',''])
        for field,title in [('teaching_comparison','Teaching across the books'),('examination_comparison','Examination comparison'),('difficulty_and_grade_bounds','Difficulty and grade descriptors'),('pitfalls','Pitfalls and evidential limits'),('gaps_and_representations','Gaps and representations'),('implications_for_step3','Proposals for step 3')]:
            out.extend(['### '+title,'',row[field],''])
        out.append('Source items: '+ '; '.join(f"{iid} (PDF{items[iid]['pdf_page']}, printed{items[iid]['printed_page']})"for iid in row['evidence_item_ids'])+'.')
        out.append('Examination parts: '+(', '.join(row.get('examination_part_ids',[]))or'none claimed')+'.')
        out.append('Grade descriptors: '+(', '.join(row.get('grade_descriptor_ids',[]))or'not yet linked; do not claim grade calibration')+'.')
        out.append('Official marking rules: '+(', '.join(row.get('marking_rule_ids',[]))or'none claimed')+'.')
        out.append('Examiner difficulties: '+(', '.join(row.get('examiner_error_ids',[]))or'no corroboration claimed')+'.\n')
    out+=['## Remaining demand synthesis','',f'{len(insight_demands)} of{len(demands)}demands have an authored section. This is a completion counter, not a syllabus-coverage score.','']
    out.extend('- '+d+' — '+demands[d]['learner_action']for d in result['pending_insight_demand_ids'])
    (A/'textbook-insights.md').write_text('\n'.join(out)+'\n')
    return result

if __name__=='__main__':
    print(json.dumps(assemble()['progress'],indent=2))
