"""Working R6 checks; --final additionally enforces all unfinished gates.

A working pass is never a completion declaration or independent review.
Negative fixtures run in memory and do not alter source/output records.
"""
import argparse
import copy
import json
from analysis_sources import A,WB,digest,write
from textbook_family_repairs_r6 import validate_member_demands,validate_response_disposition
from textbook_exam_comparison_r6 import (candidate_ids,validate_relation,
    validate_candidate_decisions,validate_insight_availability,validate_figure_status,validate_summary_anchors,active_ledger_path)
from build_objective_problem_map_r6 import validate_map


def expect_failure(name,needle,fn):
    try:fn()
    except AssertionError as e:
        assert needle in str(e),(name,'failed for an unexpected reason',str(e))
        return dict(fixture=name,result='rejected',reason=str(e))
    raise AssertionError(('seeded error passed',name))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true');args=parser.parse_args()
    data=json.loads((A/'textbook-families.json').read_text());families=data['families']
    items={i['item_id']:i for i in json.loads((A/'textbook-inventory.json').read_text())['items']}
    parts={p['part_id']:p for q in json.loads((A/'question-analysis.json').read_text())['questions']for p in q['parts']}
    ledger=json.loads(active_ledger_path().read_text())
    readings={r['reading_id']:r for r in ledger['readings']}
    registry=json.loads((A/'demand-registry.json').read_text())
    problem_map=json.loads((A/'objective-problem-map.json').read_text())
    by_id={f['family_id']:f for f in families}
    for f in families:
        validate_summary_anchors(f,parts)
        for m in f['members']:
            validate_member_demands(f,items[m['item_id']])
            validate_response_disposition(f,m,items[m['item_id']])
        for r in f['exam_relations']:validate_relation(r,f,parts,readings)
        if f['examination_relation']['kind']=='textbook-only':
            assert not f['undecided_exam_part_ids'],'incomplete family labelled textbook-only'
            assert not any(r['relation']!='rejected'
                for e in f['member_level_exceptions']for r in e['exam_relations']), \
                'textbook-only summary conceals a positive member exception'
        if args.final:validate_candidate_decisions(f,parts)
    validate_map(problem_map,registry)
    fields=['item_id','assessed_8227_demand_ids','component_demand_ids','objective_ids','learner_display']
    assert json.loads((A/'history/r6-accepted-item-links-r5.json').read_text())==[
        {k:i[k]for k in fields}for i in items.values()],'accepted source links changed'
    old=json.loads((A/'history/textbook-families-r5.json').read_text())
    def responses(fs):return {(m['item_id'],p)for f in fs for m in f['members']for p in m['part_labels']}
    assert responses(old['families'])==responses(families),'source responses lost or invented'
    assert digest(A/'history/analysis-snapshot-r5.json')=='03cde4e4192d6bcd0bd43ab776d283d9f96b12c7da91f53a656996f214b5022d','R5 snapshot changed'
    assert len(json.loads((A/'textbook-corrections-r6.json').read_text())['entries'])==11,'preserved correction register changed unexpectedly'
    negative=[]
    held=next(pid for pid,p in parts.items() if p['disposition']!='include' or p.get('hold_ids'))
    bad=copy.deepcopy(families[0]);bad['examination_relation']['part_ids']=[held]
    negative.append(expect_failure('held-part-as-usable-family-anchor','held part became a usable family anchor',lambda:validate_summary_anchors(bad,parts)))
    # A family with all its candidate decisions except one must fail.
    f=copy.deepcopy(next(f for f in families if f['exam_relations']))
    f['exam_relations']=[dict(part_id=p)for p in sorted(candidate_ids(f,parts))][1:]
    negative.append(expect_failure('undecided-family-candidate','undecided demand-overlap candidate',lambda:validate_candidate_decisions(f,parts)))
    unordered=copy.deepcopy(next(r for r in ledger['relations']if r['relation']=='structural branch'))
    unordered['difficulty_relative_to_exam']='unclassified'
    negative.append(expect_failure('unordered-branch-direction','warranted easier/harder',
        lambda:validate_relation(unordered,by_id[unordered['family_id']],parts,readings)))
    r=copy.deepcopy(next(r for r in ledger['relations']if r['relation']=='same type'))
    r.pop('read_date')
    negative.append(expect_failure('positive-relation-no-read-date','no rendered-page read date',lambda:validate_relation(r,by_id[r['family_id']],parts,readings)))
    r=copy.deepcopy(next(r for r in ledger['relations']if r['relation']=='same type'))
    future=copy.deepcopy(readings)
    future[r['rendered_reading_ids'][0]]['read_date']='2099-01-01'
    negative.append(expect_failure('positive-source-read-after-comparison','source page read after comparison date',
        lambda:validate_relation(r,by_id[r['family_id']],parts,future)))
    r=copy.deepcopy(next(r for e in ledger['member_level_exceptions']for r in e['exam_relations']
        if r.get('additional_source_decisions')))
    r['relation']='same type'
    negative.append(expect_failure('same-type-despite-implicit-seed-choice','adds a source learner decision',
        lambda:validate_relation(r,by_id[r['family_id']],parts,readings)))
    r=copy.deepcopy(next(r for r in ledger['relations']
        if r['part_id']=='8227:EXAM:2024:P2:Q5:c'and r['relation']!='rejected'))
    source=parts[r['part_id']]['paper_locator']['path']
    r['rendered_reading_ids']=[rid for rid in r['rendered_reading_ids']
        if readings[rid]['source_path']!=source]+['8227-EXAM-2024-P2-Q5-p6']
    negative.append(expect_failure('positive-reading-wrong-sibling-page','exam part page not read',
        lambda:validate_relation(r,by_id[r['family_id']],parts,readings)))
    f=copy.deepcopy(families[0]);i=items[f['members'][0]['item_id']]
    f['assessed_demand_ids']=[next(d['demand_id']for d in registry['demands']if d['demand_id']not in i['assessed_8227_demand_ids'])]
    negative.append(expect_failure('unsupported-member-demand','unsupported by member',lambda:validate_member_demands(f,i)))
    f=copy.deepcopy(next(f for f in families if f['family_id'].endswith(':proper-power-definite-integral')))
    i=items['8227:TB:YM:C7:Try-Now:14']
    negative.append(expect_failure('divergent-source-in-proper-integral-family','defective finite-integral response',
        lambda:validate_response_disposition(f,dict(part_labels=['e']),i)))
    i=dict(demand_ids=[parts[next(iter(parts))]['directly_assessed_demand_ids'][0]],
           examination_comparison='Examination parts: none claimed.',examination_part_ids=[])
    negative.append(expect_failure('false-no-exam-insight','claims no exam parts',lambda:validate_insight_availability(i,parts)))
    negative.append(expect_failure('pending-figure-status','figure retains pending status',lambda:validate_figure_status(dict(item_kind='teaching-figure',exam_representation_check='comparison pending'))))
    broken=copy.deepcopy(problem_map);next(o for o in broken['objectives']if o['demands'])['demands'].pop()
    negative.append(expect_failure('missing-demand-in-map','demand missing',lambda:validate_map(broken,registry)))
    figures=[i for i in items.values()if i.get('item_kind')in ['teaching-figure','given-figure']]
    if args.final:
        from check_textbook_answer_pages_r6 import check as check_answer_pages
        check_answer_pages(list(items.values()))
        from apply_textbook_family_prose_parallel_r6 import validate as validate_family_prose
        from apply_textbook_figures_r6 import validate as validate_figures
        validate_family_prose(families,wb=WB)
        figure_index=json.loads((A/'textbook-figure-comparisons-r6.json').read_text())
        validate_figures(list(items.values()),figure_index)
        for name in ['textbook-note-spacing-r6.json','textbook-note-spacing-parallel-r6.json','textbook-note-spacing-root-r6.json']:
            for entry in json.loads((WB/'tools'/name).read_text())['entries']:
                assert items[entry['item_id']]['notes']==entry['note'],('unapplied reviewed note repair',entry['item_id'])
        for i in figures:validate_figure_status(i)
        assert problem_map['unfinished_family_part_decisions']==0,'objective map comparison unfinished'
    result=dict(status='working structural checks pass; full R6 completion NOT established'if not args.final else'author final structural checks pass; independent check required',
        families=len(families),source_response_pairs_preserved=len(responses(families)),
        accepted_item_links_preserved=len(items),demands_in_problem_map=sum(len(o['demands'])for o in problem_map['objectives']),
        pair_decisions=len(ledger['relations']),positive_relations_with_rendered_reads=sum(r['relation']!='rejected'for r in ledger['relations']),
        negative_fixtures=negative,
        remaining_final_gates=['all family/part decisions','member-level exceptions','B.3–B.5 prose',
            'figure status/classification repair','remaining notes and answer-page audit','provenance addition',
            'all prior seeded fixtures and deterministic fresh-copy double rebuild','focused independent acceptance']if not args.final else[])
    write(WB/'checks/r6/working-validation.json',result)
    print(json.dumps({k:v for k,v in result.items()if k not in ['negative_fixtures','remaining_final_gates']},indent=2))
    print(len(negative),'new seeded errors rejected')


if __name__=='__main__':main()
