"""R5 invariants, staged explicitly; part1 success never certifies textbooks."""
import argparse,copy,json,collections
from analysis_sources import A,WB,ROOT,write,digest,evidence_path

def check_marking(mc,questions):
    rows=[r for t in mc['award_tables']for r in t['rows']]
    for r in rows:
        if r['source_mark_type']=='E':assert r.get('establishes_given_result')is True,'E row lacks establishes_given_result flag'
        assert r['what_earns_it']not in r['accepted_alternatives'],'main answer repeated as alternative'
    for q in questions:
        for p in q['parts']:
            expected='official with derived completion'if p['derived_award_completion_ids']else 'official complete'if p['official_award_criterion_ids']else 'absent'
            assert p['marking_rule_status']==expected,('marking_rule_status disagrees with linked rows',p['part_id'])
    assert sum(r['source_mark_type']=='E'for r in rows)==42
    for r in json.loads((A/'award-repairs-r5.json').read_text())['rows']:
        ev=json.loads((WB/f"checks/r5/{r['detail_image_name']}.json").read_text())
        assert ev['render_scale']>=4 and 're-read'in ev['inspection']
        assert digest(evidence_path(ev['path']))==ev['sha256']
    return {'award_rows':len(rows),'E_rows_flagged':42,'parts_with_derived_status':sum(bool(p['derived_award_completion_ids'])for q in questions for p in q['parts'])}

def check_provenance():
    d=json.loads((A/'nsscas-cambridge-provenance.json').read_text())
    mids={m['match_id']for m in d['matches']}
    assert len(mids)==32 and '8227:PROVENANCE:004'not in mids and '8227:PROVENANCE:030'not in mids
    assert d['folded_duplicate_records'][0]['folded_into']=='8227:PROVENANCE:003'
    assert len(d['possible_sources_wording_only'])==1
    current=next(m for m in d['matches']if m['match_id']=='8227:PROVENANCE:037')
    assert current['nsscas_question_key']=='2023-2-Q4'
    assert current['cambridge_locator']['pdf_pages']==[3]
    assert current['part_correspondence']==[dict(nsscas_part_id='8227:EXAM:2023:P2:Q4:b',cambridge_part=None)]
    assert current['examination_references'][0]['learner_display']is False
    assert current['duplicate_variant_leads'][0]['stem']=='9709_s20_qp_23'

    for m in d['matches']+d['possible_sources_wording_only']+d['folded_duplicate_records']:
        ev=m['rendered_confirmation'];assert digest(evidence_path(ev['path']))==ev['sha256']
        assert not any(r['learner_display']for r in m['examination_references'])
    screen=json.loads((A/'provenance-full-screen-r5.json').read_text())
    assert screen['question_count']==119 and screen['pages_compared_per_question']==3208
    assert screen['rendered_candidates_read']==158 and screen['unread_above_threshold']==0
    recall=screen['measured_recall_on_confirmed_pairs']
    assert (recall['numerator'],recall['denominator'])==(16,32)
    assert recall['baseline_r5']==dict(numerator=16,denominator=31)
    assert '8227:PROVENANCE:037'in recall['match_ids_missed']

    for q in screen['results']:
        assert q['pages_compared']==3208
        for c in q['candidates']:
            assert c['disposition']!='unread'and c['reason']
            ev=c['render_reading'];assert digest(evidence_path(ev['image_path']))==ev['image_sha256']
    return {'confirmed_pairs':len(mids),'questions_with_confirmed_pair':d['coverage']['nsscas_questions_with_confirmed_match'],'QP_unique_documents':screen['unique_qp_documents'],'page_comparisons':screen['total_comparisons'],'candidate_pages_read':158}

def check_textbook_working(items,answers,census):
    from build_textbook_census_r5 import validate_entry
    lookup={i['item_id']:i for i in items}
    printed_pages={(p['book_id'],p['pdf_page']):p['printed_page']for p in census['pages']
      if p['page_status']in['items enumerated','prose only','scope-screened; no in-scope item starts']}
    defects=json.loads((A/'textbook-defects-r5.json').read_text())['entries']
    registered={(r['item_id'],part)for r in defects for part in[r['subpart'],*r.get('also_affects_subparts',[])]}
    # R7 restores the original tan²x integrand, exposing its already cautioned
    # bad key. Keep the accepted R5 register historical; link the additive R7
    # source defect explicitly instead of suppressing the key-defect guard.
    if (WB/'tools/textbook-source-repairs-r7.json').is_file():
        r7=json.loads((A/'textbook-corrections-r7.json').read_text())['entries']
        corrections=json.loads((WB/'tools/textbook-source-repairs-r7.json').read_text())['response_corrections']
        for correction in corrections:
            matches=[r for r in r7 if r['item_id']==correction['item_id']and r['source_pdf_page']==correction['source_pdf_page']]
            assert len(matches)==1,'R7 response correction has no unique source defect'
            assert matches[0]['defect_id']in lookup[correction['item_id']].get('source_defect_ids_r7',[]),'R7 source defect not linked back to item'
            registered.add((correction['item_id'],correction['subpart']))
    reviewed=[i for i in items if i['mapping_review_status_r5'].startswith('author reclassified')]
    notes={}
    for i in reviewed:
        key=(i['book_id'],i['chapter'],i['exercise'],i['notes'].strip())
        assert key not in notes,('item note shared with a sibling',i['item_id'],notes.get(key))
        notes[key]=i['item_id']
        assert isinstance(i['component_demand_ids'],list)
        for decision in i.get('value_level_scope_decisions',[]):
            assert decision['status']in ['within','outside','not applicable']
            if decision['status']in ['within','outside']:assert decision.get('quoted_value','').strip(),'qualifier applied with no quoted value'
    for answer in answers:
        if answer['status']=='matches':assert answer.get('method'),'answer matches with no method'
        assert answer['date']
        inline=(lookup[answer['item_id']]['book_id'],answer['answer_pdf_page'])
        if inline in printed_pages:
            assert answer['answer_printed_page']==printed_pages[inline],('inline answer printed-page mismatch',answer['item_id'],answer['subpart'],inline,answer['answer_printed_page'],printed_pages[inline])
        if answer['answer_pdf_page']is None:
            assert answer.get('key_presence')=='no separate key'and answer.get('inspected_key_pdf_pages'),'no-key answer lacks explicit absence/search evidence'
        if answer['status']in['key wrong','key incomplete']:
            assert(answer['item_id'],answer['subpart'])in registered,('unregistered source key defect',answer['item_id'],answer['subpart'])
        if answer.get('unit_comparison',{}).get('agrees')is False:
            assert answer['status']=='key wrong',('unit mismatch reported as an answer match',answer['item_id'],answer['subpart'])
    assert all(i['learner_display']is False for i in items),'textbook original became learner-displayable'
    for defect in defects:
        assert defect['defect_id']in lookup[defect['item_id']].get('source_defect_ids_r5',[]),('source defect not linked back to item',defect['defect_id'])
    for page in census['pages']:
        if 'source_evidence'in page:validate_entry(page,lookup)
    assert not (A/'textbook-review-sample.json').exists(),'retired author sample regenerated'
    return {'source_records':len(items),'item_mapping_reviews_completed':len(reviewed),'subparts_verified':len(answers),'census_pages_enumerated':census['coverage']['pages_enumerated'],
      'completion':'working checkpoint only; every unfinished page,item and subpart remains open'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--stage',choices=['part1','textbook-working'],required=True);p.add_argument('--negative-fixture',choices=['E-without-flag','self-alternative','stale-marking-status','shared-sibling-note','qualifier-without-value','matches-without-method','census-missing-item','singular-implicit-point','proper-integral-pole','singular-parametric-derivative','nonconstant-primitive-error','inline-answer-page-offset','exponential-derivative-sign','log-primitive-coefficient']);args=p.parse_args()
    if args.negative_fixture=='log-primitive-coefficient':
        from verify_textbook_answers_r5 import compute,expression,primitive_agrees
        operation={'kind':'real-elementary-antiderivative','operands':['3/(7-9*x)']}
        derived=compute(operation)
        assert primitive_agrees(operation,derived,expression('-log(Abs(7-9*x))/3')),'valid real logarithmic primitive rejected'
        assert primitive_agrees(operation,derived,expression('log(Abs(7-9*x))/3')),'source log primitive has the wrong coefficient'
    if args.negative_fixture=='exponential-derivative-sign':
        from verify_textbook_answers_r5 import compute,expression,equivalent
        original={'kind':'identity','operands':['diff((exp(x)-2)/(exp(x)-1),x)']}
        correct=expression('exp(x)/(exp(x)-1)**2')
        assert equivalent(compute(original),correct),'valid exponential form was rejected'
        assert equivalent(compute(original),-correct),'source exponential derivative has the wrong sign'
    if args.negative_fixture=='nonconstant-primitive-error':
        from verify_textbook_answers_r5 import compute,expression,primitive_agrees
        operation={'kind':'real-elementary-antiderivative','operands':['x**2']}
        assert primitive_agrees(operation,compute(operation),expression('x**3/3+x**2')),'source primitive has a nonconstant error'
    if args.negative_fixture=='singular-implicit-point':
        from verify_textbook_answers_r5 import compute
        compute({'kind':'implicit-horizontal-points','operands':['x**3+y**3-3*x*y']})
    if args.negative_fixture in ['proper-integral-pole','singular-parametric-derivative']:
        from verify_textbook_answers_r5 import compute
        if args.negative_fixture=='proper-integral-pole':
            compute({'kind':'proper-definite-integral','operands':['1/x','-1','1']})
        else:
            compute({'kind':'parametric-derivative','variable':'t','operands':['t**2','2*t'],'at':'0'})
    mc=json.loads((A/'marking-conventions.json').read_text());questions=json.loads((A/'question-analysis.json').read_text())['questions']
    rows=[r for t in mc['award_tables']for r in t['rows']]
    if args.negative_fixture=='E-without-flag':next(r for r in rows if r['source_mark_type']=='E').pop('establishes_given_result')
    if args.negative_fixture=='self-alternative':rows[0]['accepted_alternatives'].append(rows[0]['what_earns_it'])
    if args.negative_fixture=='stale-marking-status':questions[0]['parts'][0]['marking_rule_status']='no complete award schedule verified'
    if args.stage=='textbook-working':
        items=json.loads((A/'textbook-inventory.json').read_text())['items'];answers=json.loads((A/'textbook-answer-verification-r5.json').read_text())['subparts'];census=json.loads((A/'textbook-page-census.json').read_text())
        if args.negative_fixture=='shared-sibling-note':
            siblings=[i for i in items if 'Exercise-1A'in i['item_id']];siblings[1]['notes']=siblings[0]['notes']
        if args.negative_fixture=='qualifier-without-value':
            next(i for i in items if i['item_id']=='8227:TB:Goldie:C1:Exercise-1A:16')['value_level_scope_decisions'][0].pop('quoted_value')
        if args.negative_fixture=='matches-without-method':next(a for a in answers if a['status']=='matches').pop('method')
        if args.negative_fixture=='inline-answer-page-offset':
            candidate=next(a for a in answers if ':YM:'in a['item_id']and isinstance(a.get('answer_pdf_page'),int)and a['answer_pdf_page']<587 and isinstance(a.get('answer_printed_page'),int))
            candidate['answer_printed_page']+=1
        if args.negative_fixture=='census-missing-item':next(p for p in census['pages']if p.get('item_ids'))['item_ids'].append('8227:TB:MISSING')
        result=check_textbook_working(items,answers,census)
        assert not args.negative_fixture,'negative fixture escaped validation'
        write(WB/'checks/repair-r5-textbook-working-validation.json',result);print(json.dumps(result,indent=2));return
    counts=check_marking(mc,questions)
    assert not args.negative_fixture,'negative fixture escaped validation'
    counts['provenance']=check_provenance()
    result={'stage':'Part1 only; T1–T6 textbook completion not certified','status':'author structural checks pass; independent acceptance pending','counts':counts}
    write(WB/'checks/repair-r5-part1-validation.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()
