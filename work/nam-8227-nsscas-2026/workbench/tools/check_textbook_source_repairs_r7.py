"""Named R7 source checks; default mode verifies the rebuilt canonical records.

--simulate-rebuild is a pre-integration test on in-memory copies. It cannot be
reported as proof that canonical generated analysis has been rebuilt.
"""
import argparse,copy,importlib,json,sys
import mpmath as mp
import sympy as sp
from pathlib import Path
import apply_textbook_source_repairs_r7 as p
from analysis_sources import WB,A,ROOT,digest,write


def independent_math(data):
    x=sp.symbols('x',real=True);target=sp.sqrt(3)/3-sp.pi/6
    assert sp.trigsimp(sp.diff(sp.tan(x)-x,x)-sp.tan(x)**2)==0
    assert sp.simplify(sp.tan(sp.pi/6)-sp.pi/6-target)==0
    mp.mp.dps=70;numeric=mp.quad(lambda z:mp.tan(z)**2,[0,mp.pi/6]);assert abs(numeric-(mp.sqrt(3)/3-mp.pi/6))<mp.mpf('1e-65')
    assert sp.simplify((sp.sqrt(3)/2-sp.pi/6)-target)!=0
    # Direct denominator/preimage checks, not agreement with an answer key.
    assert (-3)+3==0 and 3+3!=0
    y=sp.symbols('y',nonnegative=True);assert sp.sqrt(y*y)==y
    alpha=sp.atan(sp.sqrt(2));expr=sp.cos(x)+sp.sqrt(2)*sp.sin(x)
    assert sp.simplify(expr.subs(x,alpha)-sp.sqrt(3))==0
    assert sp.simplify(expr.subs(x,alpha+sp.pi)+sp.sqrt(3))==0
    assert 3-sp.sqrt(3)>0
    for patch in data['selected_result_repairs']:
        if patch['kind']!='required completed-square form':continue
        from verify_textbook_answers_r5 import expression
        assert sp.expand(expression(patch['result'])-expression(patch['original_polynomial']))==0
    return dict(tangent_square_exact='sqrt(3)/3-pi/6',numerical_quadrature=str(numeric),
        completed_form_identities=8,r_form_phase_degrees=str(sp.N(alpha*180/sp.pi,20)),
        domain_pole=-3,root_range='[0,infinity)')


def canonical_author_checks(data):
    sys.path.insert(0,str(WB/'tools/textbook-r5'))
    source=importlib.import_module('author_YM_C12_reverse_trig')
    row=copy.deepcopy(next(i for i in source.answers if i['item_id']==data['response_corrections'][0]['item_id']))
    c=data['response_corrections'][0];r=next(r for r in row['subparts']if r['subpart']==c['subpart'])
    assert r['method']==c['corrected_fields']['method']and r['operation']==c['corrected_fields']['derivation_inputs']
    assert row['notes']==c['corrected_note']and r['printed_key_normalised']==c['printed_key_normalised']
    assert r['original_integrand']=='tan(x)**2'and r['author_expected_normalised']=='sqrt(3)/3-pi/6'
    assert r['depends_on_source_parts']==[]
    checks=[]
    for module,iid,label,page in [('author_YM_C4_composite_equations','8227:TB:YM:C4:Try-Now-50:1','b',612),('author_YM_C13_iteration_branches','8227:TB:YM:C13:Try-Now-4:3','a-positive-P-bracket',653)]:
        m=importlib.import_module(module)
        a=next(p for i in m.answers if i['item_id']==iid for p in i['subparts']if p['subpart']==label)
        assert a['answer_pdf_page']==page,('canonical source author locator wrong',iid,label)
        checks.append(dict(item_id=iid,subpart=label,answer_pdf_page=page))
    return dict(corrected_tangent_source_author=True,canonical_locator_authors=checks)


def simulate(items,data):
    items=copy.deepcopy(items);byid={i['item_id']:i for i in items}
    for c in data['response_corrections']:
        i=byid[c['item_id']];r=next(r for r in i['answer_verification_r5']if r['subpart']==c['subpart'])
        r.update(copy.deepcopy(c['corrected_fields']),status=c['correct_status'],original_integrand='tan(x)**2',depends_on_source_parts=[])
        i['notes']=c['corrected_note']
    for c in data['answer_page_repairs']:
        i=byid[c['item_id']]
        for label in c['subparts']:
            r=next(r for r in i['answer_verification_r5']if r['subpart']==label)
            r.update(answer_pdf_page=c['answer_pdf_page'],answer_printed_page=c['answer_printed_page'])
        pages=sorted({r['answer_pdf_page']for r in i['answer_verification_r5']if r['answer_pdf_page']is not None})
        i['answer_key']['pdf_pages']=pages;i['answer_key']['printed_pages']=[next(r['answer_printed_page']for r in i['answer_verification_r5']if r['answer_pdf_page']==pg)for pg in pages]
    return items


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--simulate-rebuild',action='store_true');args=parser.parse_args()
    data=p._read();math=independent_math(data);canonical=canonical_author_checks(data)
    original=json.loads((A/'textbook-inventory.json').read_text())['items']
    items=simulate(original,data)if args.simulate_rebuild else copy.deepcopy(original)
    families=json.loads((A/'textbook-families.json').read_text())
    if args.simulate_rebuild:
        repaired=p.apply(items);p.apply_family_selected_results(families,repaired)
    else:
        repaired=items
        # Check the saved canonical outputs first. Applying an overlay before
        # this check would conceal a missing builder hook.
        p.validate(repaired,families)
        assert p.apply(copy.deepcopy(repaired))==repaired,'canonical inventory missing R7 source overlay'
        assert p.apply_family_selected_results(copy.deepcopy(families),repaired)==families,'canonical families missing R7 selected results'
    result=p.validate(repaired,families)
    keys=['item_id','assessed_8227_demand_ids','component_demand_ids','objective_ids','learner_display']
    projection=lambda xs:[{k:i[k]for k in keys}for i in xs]
    assert projection(original)==projection(repaired),'accepted item links changed'
    assert p.apply(copy.deepcopy(repaired))==repaired,'R7 source overlay not idempotent'
    second=p.apply_family_selected_results(copy.deepcopy(families),repaired);assert second==families,'R7 selected-result overlay not idempotent'
    audit=json.loads((A/'textbook-answer-page-audit-r6.json').read_text());fixed=p.apply_answer_page_audit(audit)
    assert p.apply_answer_page_audit(fixed)==fixed,'page audit overlay not idempotent'
    negatives=[]
    def reject(name,change):
        bad=copy.deepcopy(repaired);fs=copy.deepcopy(families);change(bad,fs)
        try:p.validate(bad,fs)
        except AssertionError as e:negatives.append(dict(fixture=name,result='rejected',reason=str(e)))
        else:raise AssertionError('seeded R7 corruption passed:'+name)
    c=data['response_corrections'][0]
    reject('restored-wrong-tangent-argument',lambda xs,fs:next(r for i in xs if i['item_id']==c['item_id']for r in i['answer_verification_r5']if r['subpart']==c['subpart']).update(derivation_inputs=c['baseline_fields']['derivation_inputs']))
    loc=data['answer_page_repairs'][0]
    reject('restored-wrong-key-page',lambda xs,fs:next(r for i in xs if i['item_id']==loc['item_id']for r in i['answer_verification_r5']if r['subpart']=='b').update(answer_pdf_page=613))
    reject('long-division-regressed-to-text',lambda xs,fs:next(i for i in xs if i['item_id']=='8227:TB:YM:C8:Teaching-figure:35').update(figure_record_type='text callout'))
    target=next(i['item_id']for i in repaired if i.get('item_kind')in p.FIGURES and '8227:EXAM:2023:P2:Q6:d'in i['exam_representation_check']['own_sketch_readback_part_ids'])
    reject('lost-own-sketch-readback',lambda xs,fs:next(i for i in xs if i['item_id']==target)['exam_representation_check'].update(own_sketch_readback_part_ids=[]))
    patch=data['selected_result_repairs'][0]
    def corrupt_form(xs,fs):
        m=next(m for f in fs['families']for m in f['members']if m['item_id']==patch['item_id']and patch['subpart']in m['part_labels'])
        next(r for r in m['selected_response_results_r7']if r['subpart']==patch['subpart'])['result']='x**2'
    reject('wrong-selected-completed-form',corrupt_form)
    result.update(mode='pre-integration in-memory simulation; not canonical rebuild proof'if args.simulate_rebuild else'canonical rebuilt inventory and source author checks',
        independent_math=math,canonical_author_checks=canonical,negative_fixtures=negatives,
        accepted_item_links_preserved=True,overlay_idempotent=True,selected_result_overlay_idempotent=True,
        input_sha256={n:digest(WB/n)for n in ['tools/'+p.INPUT_NAME,'tools/apply_textbook_source_repairs_r7.py','tools/check_textbook_source_repairs_r7.py','analysis/textbook-corrections-r7.json']})
    write(WB/'checks/r7/parallel-sources/validation.json',result);print(json.dumps(result,indent=2))


if __name__=='__main__':main()
