"""Final whole-population author consistency audit; independent acceptance is separate."""
import argparse,collections,copy,json
from analysis_sources import A,WB,ROOT,digest,write

QUALIFIER_DEMANDS={
 'QUAL01':['M2:T1:O02'],'QUAL02':['M1:T2:O01'],
 'QUAL03':['M1:T6:O06'],'QUAL04':['M1:T9:O03:D02'],
 'QUAL05':['M1:T9:O01'],'QUAL06':['M1:T9:O04:D02'],
 'QUAL07':['M1:T3:O02'],'QUAL08':['M1:T3:O03'],
 'QUAL09':['M1:T4:O02:D02'],'QUAL10':['M1:T8:O02'],
 'QUAL11':['M2:T5:O04:D02']}

def allowed_implicit_geometry():
    """Individually source-read cohort; never infer this class from family tags."""
    allowed=set()
    def add(book,ch,kind,ns):
        allowed.update(f'8227:TB:{book}:C{ch}:{kind}:{n}'for n in ns)
    add('Goldie',4,'Exercise-4D',range(2,13))
    add('Goldie',4,'Exercise-4E',[2,3,4,6,7,8,9,11,13,15])
    add('Goldie',4,'Example',[16,17,18,22,23,24])
    add('Goldie',6,'Exercise-6B',[16])
    add('YM',11,'Example',[29,30,31,37,38,39,40,42])
    add('YM',11,'Try-Now-29',[1,2,3,4])
    add('YM',11,'Try-Now',[30,41])
    add('YM',11,'Try-Now-31',[1,2])
    add('YM',11,'Try-Now-37',[1,2])
    add('YM',11,'Try-Now-38',[1,2])
    add('YM',11,'Try-Now-39',[1,2,3,4])
    add('YM',11,'Try-Now-40',[1,2])
    add('YM',11,'Try-Now-42',[1])
    add('YM',11,'Revision-Exercise-11',[4,5])
    add('YM',11,'Exercise-11',[6,7,8,9])
    add('YM',13,'Example',[11])
    return allowed

def audit(items,census,answers,synthesis):
    lookup={i['item_id']:i for i in items}
    assert len(lookup)==len(items)
    assert census['coverage']['exhaustive']is True,'source census incomplete'
    assert all(i['mapping_review_status_r5'].startswith('author reclassified')for i in items)
    response=[i for i in items if i.get('item_kind')not in ['teaching-figure','given-figure']]
    figures=[i for i in items if i.get('item_kind')in ['teaching-figure','given-figure']]
    qualifiers=[];notes={};implicit=[];log_cohort=[];visual_dispositions=[]
    for item in items:
        assert item['learner_display']is False
        assert isinstance(item['exam_style'],bool)and item['exam_style_basis']
        assert item['notes'].strip()
        assert not set(item['assessed_8227_demand_ids'])&set(item['component_demand_ids'])
        assert item['evidence_role']and item['mapping_rule']
        if item in figures:
            assert item['mathematical_feature_review']and item['exam_representation_check']
            assert not item['assessed_8227_demand_ids'],'teaching figure became assessed practice'
            continue
        key=(item['book_id'],item['chapter'],item['exercise'],item['notes'].strip())
        assert key not in notes,'source item note shared with sibling'
        notes[key]=item['item_id']
        expected=set(item.get('answer_expected_subpart_labels_r5',[]))
        actual={p['subpart']for p in item.get('answer_verification_r5',[])}
        if item['scope_check']['status']!='out-of-scope':
            assert expected and expected==actual,'source response missing from answer checks'
        decisions=item['value_level_scope_decisions']
        for rule,patterns in QUALIFIER_DEMANDS.items():
            if any(any(pattern in d for pattern in patterns)for d in item['assessed_8227_demand_ids']):
                candidates=[d for d in decisions if d['rule_id']=='8227:'+rule]
                assert candidates,('missing applicable qualifier record',item['item_id'],rule)
                assert all(c['status']in ['within','outside','not applicable']and c['quoted_value'].strip()and c['reason']for c in candidates)
                qualifiers.append(dict(item_id=item['item_id'],rule_id='8227:'+rule,pdf_page=item['pdf_page'],decisions=candidates))
        if '8227:2020:M2:T4:O03:D03'in item['assessed_8227_demand_ids']:
            assert item['item_id']in allowed_implicit_geometry(),'explicit item incorrectly classified as implicit/parametric geometry'
            implicit.append(dict(item_id=item['item_id'],pdf_page=item['pdf_page'],source_note=item['notes'],mapping_rationale=item.get('mapping_rationale')))
        if any('M2:T2:O01:'in d or'M2:T2:O02:'in d for d in item['assessed_8227_demand_ids']):
            log_cohort.append(dict(item_id=item['item_id'],pdf_page=item['pdf_page'],direct_demand_ids=item['assessed_8227_demand_ids'],component_demand_ids=item['component_demand_ids'],source_note=item['notes']))
        has_sketch=any(p['status']=='sketch'for p in item.get('answer_verification_r5',[]))
        if has_sketch!=item['sketch_response_required']:
            if not item['sketch_response_required']:
                assert item['item_id']in {f'8227:TB:YM:C4:Worked-illustration:{n}'for n in range(4,12)},'new unreviewed teaching-sketch role mismatch'
                reason='Source teaching-ray feature QA,not a separately posed learner sketch; original source illustration role retained.'
            else:
                statuses={p['status']for p in item['answer_verification_r5']}
                if item['item_id']=='8227:TB:Goldie:C6:Activity:2':
                    reason='The original asks an explanation referring to a sketch; four matched iteration outcomes retain explicit graph/intersection features. This is sketch-dependent explanation,not a separate invented sketch part.'
                else:
                    assert statuses&{'key wrong','key incomplete','no key'},'new unreviewed sketch response/status mismatch'
                    reason='Required visual/explanatory response is retained; status prioritises wrong/incomplete/absent key rather than duplicating the sketch status. Source-specific sketch features remain in the answer record.'
            visual_dispositions.append(dict(item_id=item['item_id'],source_note=item['notes'],reason=reason))
    assert synthesis['progress']['response_items_pending']==0 and not synthesis['pending_response_items'],'unresolved source family responses'
    assert synthesis['progress']['insight_demands_completed']==138 and not synthesis['pending_insight_demand_ids'],'incomplete demand insights'
    assert len({(r['item_id'],r['subpart'])for r in answers})==len(answers)
    assert len(answers)==sum(len(i.get('answer_verification_r5',[]))for i in response)
    return dict(status='author whole-population consistency audit passed; independent source/classification/answer acceptance pending',
        counts=dict(source_records=len(items),response_items=len(response),figure_records=len(figures),answers=len(answers),
            response_statuses=dict(collections.Counter(r['status']for r in answers)),
            qualifier_applications_checked=len(qualifiers),implicit_parametric_geometry_items=len(implicit),logarithm_boundary_cohort=len(log_cohort),
            visual_role_exceptions=len(visual_dispositions),families=synthesis['progress']['families_authored'],insight_demands=138),
        qualifier_applications=qualifiers,implicit_parametric_geometry_cohort=implicit,
        forced_logarithmic_exception=dict(item_id='8227:TB:Goldie:C4:Exercise-4D:7',
            reason='Originaly=x^xexplicitlyrequiresbase-e logs and differentiating the resulting implicit log equation before stationary geometry. This source-enforced method is retained;ordinary explicit-function tasks do not acquire this label.'),
        logarithm_boundary_cohort=log_cohort,visual_role_dispositions=visual_dispositions,
        judgement_limits='This exhaustively checks record consistency against the individually authored source population. Cohort lists expose author judgements for cross-vendor checking; no lexical test, hash or membership count proves educational classification. Source/render reading and independent mathematical computation remain separately cited in each item.',
        independent_review=dict(status='pending',sample='Reviewer chooses a fresh blind sample of at least10percent;no author-selected review sample.'),
        source_inputs={str(p.relative_to(ROOT)):digest(p)for p in [A/'textbook-inventory.json',A/'textbook-page-census.json',A/'textbook-answer-verification-r5.json',A/'textbook-families.json',WB/'tools/textbook_scope_audit_inputs_r5.py']})

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--negative-fixture',choices=['missing-volume-axis','explicit-as-implicit','unresolved-family-response']);args=parser.parse_args()
    items=json.loads((A/'textbook-inventory.json').read_text())['items']
    census=json.loads((A/'textbook-page-census.json').read_text())
    answers=json.loads((A/'textbook-answer-verification-r5.json').read_text())['subparts']
    synthesis=json.loads((A/'textbook-families.json').read_text())
    if args.negative_fixture=='missing-volume-axis':
        item=next(i for i in items if i['item_id']=='8227:TB:YM:C7:Example:31')
        item['value_level_scope_decisions']=[d for d in item['value_level_scope_decisions']if d['rule_id']!='8227:QUAL06']
    if args.negative_fixture=='explicit-as-implicit':
        item=next(i for i in items if i['item_id']=='8227:TB:YM:C6:Example:1')
        item['assessed_8227_demand_ids'].append('8227:2020:M2:T4:O03:D03')
    if args.negative_fixture=='unresolved-family-response':synthesis['progress']['response_items_pending']=1
    result=audit(items,census,answers,synthesis)
    assert not args.negative_fixture,'seeded completion error escaped'
    write(A/'textbook-completion-audit-r5.json',result)
    lines=['# Final author consistency audit — NSSCAS Mathematics8227','',result['status'],'',
        'All source pages and individually authored item/answer records were covered. This is an author audit,not an independent review or permission to startstep3.','',
        '```json',json.dumps(result['counts'],indent=2),'```','',
        '## Qualifier audit','',
        'Missing applicable QUAL01–11 records were explicitly supplemented from the already-read source values. QUAL06checks the actual axis,QUAL04the actual simple limit,QUAL08the original inverse branch. Parameter and method exceptions remain source-specific; generic lists of rule identifiers are not treated as applications.','',
        '## Mapping and response roles','',result['forced_logarithmic_exception']['reason'],'',
        f'The JSON exposes every implicit/parametric geometry member and the complete logarithm/general-log versus natural-exponential boundary cohort. Direct and component identifiers remain disjoint. {result["counts"]["visual_role_exceptions"]} visual-role/status exceptions retain the original visual demand or source-illustration role.','',
        '## Limits and next check','',result['judgement_limits'],'',
        'Independent reviewer:draw a fresh blind sample of at least10percent,including diagrams,source defects,scope limits and family decisions. No author-selected sample has been produced.','']
    (A/'textbook-completion-audit-r5.md').write_text('\n'.join(lines))
    print(json.dumps(result['counts'],indent=2))
if __name__=='__main__':main()
