"""Structural regression checks for authored T5 evidence; no educational acceptance."""
import argparse,copy,json
from analysis_sources import A,WB,ROOT,digest,write
from build_textbook_synthesis_r5 import validate_response_exclusions

def validate(families,insights,items,demands,parts):
    covered={};family_ids=set()
    for f in families:
        assert f['family_id']not in family_ids,'duplicate textbook family'
        family_ids.add(f['family_id']);mapped=set()
        assert f['not_a_recipe_count']is True
        for m in f['members']:
            assert m['item_id']in items,'unknown textbook member'
            i=items[m['item_id']];labels={a['subpart']for a in i.get('answer_verification_r5',[])}
            assert m['part_labels']and set(m['part_labels'])<=labels,'unknown connected source response'
            assert m['source_path']==i['source_path']and m['source_sha256']==i['source_sha256'],'member source identity changed'
            assert m['pdf_page']==i['pdf_page']and m['printed_page']==i['printed_page'],'member page locator changed'
            assert m['learner_display']is False,'textbook original exposed to learner'
            mapped.update(i['assessed_8227_demand_ids'])
            if m.get('family_response_demand_evidence_r7'):
                from textbook_family_repairs_r6 import validate_member_demands
                validate_member_demands(f,i)
                mapped.update(m['family_response_demand_evidence_r7']['demand_ids'])
            covered.setdefault(m['item_id'],set()).update(m['part_labels'])
        assert set(f['assessed_demand_ids'])<=mapped,'unsupported textbook family demand'
        for p in f['examination_relation']['part_ids']:
            assert p in parts and parts[p]['disposition']=='include'and not parts[p].get('hold_ids'),'held or missing examination comparison'
        if f['examination_relation']['kind']=='textbook-only':assert not f['examination_relation']['part_ids']
    insight_demands=set()
    for row in insights:
        assert row['demand_ids']and set(row['demand_ids'])<=demands
        assert set(row['evidence_item_ids'])<=set(items)
        insight_demands.update(row['demand_ids'])
    return covered,insight_demands

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--negative-fixture',choices=['unknown-member','lost-connected-response','unsupported-family-demand','forged-response-exclusion']);args=parser.parse_args()
    families=json.loads((A/'textbook-families.json').read_text())
    inputs=[json.loads(p.read_text())for p in sorted((WB/'tools/textbook-r5').glob('synthesis-*.json'))]
    insights=[r for d in inputs for r in d.get('insights',[])]
    items={i['item_id']:i for i in json.loads((A/'textbook-inventory.json').read_text())['items']}
    demands={d['demand_id']for d in json.loads((A/'demand-registry.json').read_text())['demands']}
    parts={p['part_id']:p for q in json.loads((A/'question-analysis.json').read_text())['questions']for p in q['parts']}
    data=copy.deepcopy(families['families'])
    exclusions=copy.deepcopy(families.get('excluded_response_parts',[]))
    if args.negative_fixture=='unknown-member':data[0]['members'][0]['item_id']='8227:TB:missing'
    if args.negative_fixture=='lost-connected-response':data[0]['members'][0]['part_labels']=['not-a-source-part']
    if args.negative_fixture=='unsupported-family-demand':data[0]['assessed_demand_ids']=['8227:2020:M1:T5:O01:D01']
    if args.negative_fixture=='forged-response-exclusion':
        member=data[0]['members'][0]
        exclusions.append(dict(item_id=member['item_id'],part_labels=member['part_labels'][:1],rule_id='8227:LIMIT02',reason='seeded attempt to hide an in-scope response',applies_to='seeded',quoted_value='not a source exclusion'))
    excluded=validate_response_exclusions(exclusions,items)
    covered,done=validate(data,insights,items,demands,parts)
    progress=families['progress']
    assert progress['response_items_with_any_family']==len(covered),'family coverage counter includes empty memberships'
    assert progress['insight_demands_completed']==len(done)
    assert set(families['pending_insight_demand_ids'])==demands-done
    pending={}
    resolved=0
    for item in items.values():
        if item.get('item_kind')in ['teaching-figure','given-figure']or item['scope_check']['status']=='out-of-scope':continue
        expected={a['subpart']for a in item.get('answer_verification_r5',[])}
        missing=expected-covered.get(item['item_id'],set())-excluded[item['item_id']]
        if missing or not expected:pending[item['item_id']]=sorted(missing)
        else:resolved+=1
    assert pending=={r['item_id']:r['pending_parts']for r in families['pending_response_items']},'unresolved source responses hidden from pending ledger'
    assert progress['source_responses_explicitly_excluded']==sum(len(v)for v in excluded.values())
    assert progress['response_items_with_all_eligible_responses_resolved']==resolved
    assert not (A/'textbook-review-sample.json').exists(),'author review sample must stay retired'
    result=dict(status='author structural pass; independent family/classification review still required',
        families=len(data),response_items_with_membership=len(covered),insight_demands=len(done),
        input_hashes={str(p.relative_to(ROOT)):digest(p)for p in sorted((WB/'tools/textbook-r5').glob('synthesis-*.json'))},
        limitation='Does not certify discriminating decisions, educational equivalence, source completeness or future recipe economy.')
    write(WB/'checks/textbook-synthesis-validation-r5.json',result)
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
