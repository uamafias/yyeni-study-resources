"""Derive the 8227 objective problem map from source links and authored comparisons.

This analysis index does not choose recipes, decks or a pilot PLAN. An unfinished
comparison remains unfinished and never becomes a no-counterpart claim.
"""
import collections
import json
from analysis_sources import A,WB,ROOT,digest,write
from textbook_closeout_r7 import LIMIT,documents


def tally(rows):
    return dict(total=len(rows),with_exam_parts=sum(bool(r['nsscas_exam_parts'])for r in rows),
        with_usable_exam_parts=sum(any(p['usable_learner_anchor']for p in r['nsscas_exam_parts'])for r in rows),
        with_same_type_textbook_practice=sum(bool(r['same_type_textbook_practice'])for r in rows),
        with_only_variant_or_other_practice=sum(not r['same_type_textbook_practice']and bool(
            r['textbook_structural_branches']or r['other_textbook_practice']or
            r['source_item_union_support']or r['cambridge_items'])for r in rows),
        with_no_practice_anywhere=sum(not(any(p['usable_learner_anchor']for p in r['nsscas_exam_parts'])or r['same_type_textbook_practice']or
            r['textbook_structural_branches']or r['other_textbook_practice']or
            r['source_item_union_support']or r['cambridge_items'])for r in rows),
        with_unfinished_textbook_comparison=sum(bool(r['unclassified_textbook_comparisons'])for r in rows))


def validate_map(result,registry):
    ids=[d['demand_id']for o in result['objectives']for d in o['demands']]
    assert len(ids)==len(set(ids)),'duplicate demand in objective problem map'
    assert set(ids)=={d['demand_id']for d in registry['demands']},'demand missing from objective problem map'


def build():
    reg=json.loads((A/'demand-registry.json').read_text())
    objectives=json.loads((WB.parent/'curriculum/objective_registry.json').read_text())['objectives']
    qs=json.loads((A/'question-analysis.json').read_text())['questions']
    parts={p['part_id']:(q,p)for q in qs for p in q['parts']}
    families=json.loads((A/'textbook-families.json').read_text())['families']
    cb=json.loads((A/'cambridge-evidence.json').read_text())['items']
    items=json.loads((A/'textbook-inventory.json').read_text())['items']
    item_index={i['item_id']:i for i in items}
    related_closeout=[r for document in documents()for r in document.get('related_practice',[])]
    gap_searches=json.loads((A/'textbook-gap-search-r7.json').read_text())['parts']
    member_support=collections.defaultdict(list)
    for f in families:
        for m in f['members']:
            member_support[m['item_id']].append(dict(family_id=f['family_id'],
                member_id=m['member_id'],part_labels=m['part_labels'],
                common_family_assessed_demand_ids=f['assessed_demand_ids']))
    by_obj=collections.defaultdict(list)
    for d in reg['demands']:
        did=d['demand_id']
        exam=[dict(part_id=pid,year=q['year'],paper=q['paper'],question=q['question'],
             part=p['paper_locator']['part'],locator=p['paper_locator'],
             disposition=p['disposition'],hold_ids=p.get('hold_ids',[]),
             usable_learner_anchor=p['disposition']=='include'and not p.get('hold_ids'))
             for pid,(q,p)in parts.items()if did in p['directly_assessed_demand_ids']]
        same=[];branches=[];other=[];unclassified=[];nonordered=[];held_comparisons=[]
        for f in families:
            direct_family_demand=did in f['assessed_demand_ids']
            explicit_source_parts={r['part_id']for r in f.get('source_search_candidates_r7',[])}
            if not direct_family_demand and not any(did in parts[pid][1]['directly_assessed_demand_ids']for pid in explicit_source_parts):continue
            base=dict(family_id=f['family_id'],title=f['title'],
                members=[dict(member_id=m['member_id'],item_id=m['item_id'],part_labels=m['part_labels'],
                    source_path=m['source_path'],pdf_page=m['pdf_page'],printed_page=m['printed_page'])for m in f['members']],
                learner_display=False)
            relation_rows=f.get('exam_relations',[])+[
                dict(r,member_exception_id=e['member_id'],source_part_labels=e['part_labels'])
                for e in f.get('member_level_exceptions',[])for r in e['exam_relations']]
            nonordered.extend(dict(base,part_id=r['part_id'],comparison_evidence=r['rejection_reason'],
                exemplar_member_ids=r.get('exemplar_member_ids',[]),
                exemplar_part_labels=r.get('exemplar_part_labels',{}),
                status='relation not established; specific source comparison retained')
                for r in relation_rows if r.get('nonordered_connection') and r['relation']=='rejected'
                and did in parts[r['part_id']][1]['directly_assessed_demand_ids'])
            positive=[r for r in relation_rows if r['relation']!='rejected'
                      and did in parts[r['part_id']][1]['directly_assessed_demand_ids']]
            for r in positive:
                entry=dict(base,part_id=r['part_id'],exemplar_member_ids=r['exemplar_member_ids'],
                    exemplar_items=[dict(m,part_labels=r.get('exemplar_part_labels',{}).get(m['member_id'],m['part_labels']))
                        for m in base['members']if m['member_id']in r['exemplar_member_ids']],
                    exemplar_part_labels=r.get('exemplar_part_labels',{}),
                    comparison_evidence=r['differing_decision'],read_date=r['read_date'],
                    comparison_scope=r.get('comparison_scope','named exemplar responses'),
                    member_exception_id=r.get('member_exception_id'),
                    source_part_labels=r.get('source_part_labels'),
                    usable_learner_anchor=parts[r['part_id']][1]['disposition']=='include'
                      and not parts[r['part_id']][1].get('hold_ids'))
                if not entry['usable_learner_anchor']:
                    held_comparisons.append(dict(entry,relation=r['relation'],design_anchor=False));continue
                entry['demand_link_basis']='Common family/part assessed demand'if direct_family_demand else'R7 explicit native selected-response comparison to this assessed exam part; item tags unchanged'
                if r['relation']=='same type':same.append(entry)
                else:branches.append(dict(entry,differing_decision=r['differing_decision'],
                    difficulty_relative_to_exam=r['difficulty_relative_to_exam']))
            if f.get('undecided_exam_part_ids'):
                unclassified.append(dict(base,undecided_part_ids=f['undecided_exam_part_ids']))
            if direct_family_demand and not any(r['part_id']in {p['part_id']for p in exam if p['usable_learner_anchor']}for r in positive):
                kind=('practice on a never-examined demand'if not exam else
                      'comparison unfinished'if f.get('undecided_exam_part_ids')else
                      'supporting teaching practice'if 'support'in f['family_id']else
                      'textbook practice: relation not established')
                other.append(dict(base,kind=kind,learner_decisions=f['learner_decisions'],
                    candidate_decisions=f.get('exam_relations',[])))
        comparable=[dict(item_id=c['item_id'],locator=c['locator'],
                        evidence_label=c['evidence_label'],scope_check=c['scope_check'],
                        examination_references=c['examination_references'])
                    for c in cb if did in c['assessed_8227_demand_ids']]
        union=[dict(item_id=i['item_id'],role='assessed'if did in i['assessed_8227_demand_ids']else'component',
                    pdf_page=i['pdf_page'],source_path=i['source_path'],
                    family_memberships=member_support[i['item_id']],
                    warning='Accepted item-level support; not proof that every selected response assesses this demand.')
               for i in items if i.get('item_kind')not in ['teaching-figure','given-figure']
               and i['scope_check']['status']!='out-of-scope'
               and did in set(i['assessed_8227_demand_ids'])|set(i['component_demand_ids'])]
        related_internal=[]
        for related in related_closeout:
            if did not in parts[related['part_id']][1]['directly_assessed_demand_ids']:continue
            item=item_index[related['item_id']]
            related_internal.append(dict(related,source_path=item['source_path'],source_sha256=item['source_sha256'],pdf_page=item['pdf_page'],printed_page=item['printed_page'],coverage_role='Related graph-to-formula reasoning only; not a modulus counterpart or assessed-demand coverage claim.'))
        bounded_search_notes=[dict(part_id=r['part_id'],decision=r['decision'],reason=r['reason'],search_notes=r['search_notes'],record='analysis/textbook-gap-search-r7.json')for r in gap_searches if r['decision']=='no match found'and did in parts[r['part_id']][1]['directly_assessed_demand_ids']]
        by_obj[d['objective_id']].append(dict(related_internal_source_practice=related_internal,bounded_search_notes=bounded_search_notes,demand_id=did,learner_action=d['learner_action'],
            nsscas_exam_status='examination-observed'if exam else'NO NSSCAS EXAM PART',
            nsscas_exam_parts=exam,same_type_textbook_practice=same,
            textbook_structural_branches=branches,other_textbook_practice=other,
            nonordered_textbook_connections=nonordered,internal_held_textbook_comparisons=held_comparisons,
            unclassified_textbook_comparisons=unclassified,cambridge_items=comparable,
            source_item_union_support=union))
    rows=[]
    for o in objectives:
        ds=by_obj[o['objective_id']]
        rows.append(dict(objective_id=o['objective_id'],objective_text=o['normalized_math_text'],
            syllabus_source=o['source'],demands=ds,counts=tally(ds)))
    all_ds=[d for o in rows for d in o['demands']]
    # Objective counts use any constituent demand; absence means all demands lack it.
    collapsed=[{k:sum((d[k]for d in o['demands']),[])for k in [
        'nsscas_exam_parts','same_type_textbook_practice','textbook_structural_branches',
        'other_textbook_practice','source_item_union_support','cambridge_items','unclassified_textbook_comparisons']}
        for o in rows]
    pending=sum(len(f.get('undecided_exam_part_ids',[]))for f in families)
    result=dict(schema_version='8227-objective-problem-map-r7',
        status='WORKING: comparison decisions incomplete'if pending else'family-exam candidate comparisons complete; other R7 gates reported separately; independent check required',
        unfinished_family_part_decisions=pending,
        counts=dict(by_objective=tally(collapsed),by_demand=tally(all_ds)),objectives=rows,
        count_definitions='Same-type and close-variant counts use recorded family relations only. '
        'Other practice includes unfinished comparisons, explicitly labelled. No-practice-anywhere means '
        'no usable exam part, textbook family, accepted item-union support or recorded Cambridge item. Counts overlap; '
        'an objective counts once when any constituent demand qualifies.',
        limits=LIMIT+' R5-03: source-item support uses the union of accepted assessed/component links and is a lower bound. '
        'These links do not establish equivalence for every part of a connected item. '
        'Same-type and structural-branch entries identify the actual exemplar responses; '
        'A relation explicitly marked supporting assessed subtask does not cover the complete exam task. '
        'the full family member list is context and does not certify every member against that exam part. '
        'Held exam parts and intended-type comparisons are internal defective evidence, excluded from same-type/branch practice counts and usable anchors. '
        'Textbook originals remain internal. This map is not a PLAN, approved recipe bank or learner deck.',
        inputs={str(p.relative_to(ROOT)):digest(p)for p in [A/'demand-registry.json',
            WB.parent/'curriculum/objective_registry.json',A/'question-analysis.json',
            A/'textbook-families.json',A/'textbook-inventory.json',A/'cambridge-evidence.json',A/'textbook-gap-search-r7.json',WB/'tools/textbook-closeout-family-gap-inputs.json']})
    validate_map(result,reg)
    write(A/'objective-problem-map.json',result)
    lines=['# Objective problem map — NSSCAS Mathematics 8227','',result['status'],'',
        'Every objective retains all its demands. A missing exam match never removes textbook or Cambridge practice.','',
        '```json',json.dumps(result['counts'],indent=2),'```','',result['count_definitions'],'',result['limits'],'']
    for o in rows:
        lines+=['## '+o['objective_id'],'',o['objective_text'],'']
        for d in o['demands']:
            lines+=['### '+d['demand_id']+' — '+d['learner_action'],'',d['nsscas_exam_status'],'',
                'NSSCAS: '+('; '.join(f"{p['year']} P{p['paper']} Q{p['question']}({p['part']})"+
                    (' [held]'if not p['usable_learner_anchor']else'')for p in d['nsscas_exam_parts'])or'none')+'.','',
                'Same type: '+('; '.join(r['family_id']+' → '+r['part_id']+'; exemplar '+
                    ', '.join(m['item_id']+' ['+', '.join(m['part_labels'])+f"], PDF {m['pdf_page']}"for m in r['exemplar_items'])
                    for r in d['same_type_textbook_practice'])or'relation not established for the recorded exemplars')+'.','',
                'Close variants: '+('; '.join(r['family_id']+' → '+r['part_id']+'; '+r['differing_decision']+' ('+r['difficulty_relative_to_exam']+')'for r in d['textbook_structural_branches'])or'relation not established for the recorded exemplars')+'.','',
                'Other textbook practice: '+('; '.join(r['family_id']+' ['+r['kind']+']'for r in d['other_textbook_practice'])or'none recorded')+'.','',
                'Cambridge: '+('; '.join(r['item_id']for r in d['cambridge_items'])or'none recorded')+'.','',
                f"Accepted item-union support: {len(d['source_item_union_support'])} items; selected-response equivalence not inferred.",'',
                'Related internal source practice (not a modulus counterpart): '+('; '.join(r['item_id']+' ['+', '.join(r['part_labels'])+'] — '+r['reason']for r in d['related_internal_source_practice'])or'none recorded')+'.','',
                'Bounded unmatched-part searches: '+('; '.join(r['part_id']+' — '+r['reason']for r in d['bounded_search_notes'])or'none recorded')+'.','']
    (A/'objective-problem-map.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(dict(status=result['status'],counts=result['counts']),indent=2))
    return result


if __name__=='__main__':build()
