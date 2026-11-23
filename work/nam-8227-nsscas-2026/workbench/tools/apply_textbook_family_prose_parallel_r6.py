"""Apply the isolated B.3--B.5 R6 author prose inputs in memory.

This module changes prose/evidence references only. It never infers membership,
retags syllabus links, creates exam relations or claims independent acceptance.
The reviewed JSON is the author input. Validation checks propagation and identity,
not the educational truth of every author judgement.
"""
import copy
import hashlib
import json
from pathlib import Path

INPUT_NAME='textbook-family-prose-parallel-r6.json'
FIELDS=('nearest_sibling_family_id','distinction_basis','difficulty_progression','units_and_precision')


def _wb(wb=None):
    return Path(wb) if wb is not None else Path(__file__).resolve().parents[1]


def _rows(families):
    return families['families'] if isinstance(families,dict) else families


def _read(wb=None):
    return json.loads((_wb(wb)/'tools'/INPUT_NAME).read_text())


def _identity(families):
    rows=sorted([[f['family_id'],sorted([[m['member_id'],m['item_id'],m['part_labels']]for m in f['members']])]
                 for f in _rows(families)])
    body=json.dumps(rows,ensure_ascii=False,sort_keys=True,separators=(',',':'))
    return hashlib.sha256(body.encode()).hexdigest()


def _r7_authorised_change(home,item_id,subpart,key,before,after):
    """Accept only an explicit source-backed R7 correction, not arbitrary drift."""
    path=home/'tools/textbook-source-repairs-r7.json'
    if not path.exists():return False
    rows=json.loads(path.read_text()).get('response_corrections',[])
    match=next((r for r in rows if (r['item_id'],r['subpart'])==(item_id,subpart)),None)
    if not match:return False
    if before!=match['baseline_fields'].get(key)or after!=match['corrected_fields'].get(key):return False
    assert (item_id,subpart)==('8227:TB:YM:C12:Try-Now-17:1','b-tangent-square-integral'),'unreviewed response correction'
    for field in ['source_evidence','key_evidence']:
        ev=json.loads((home/match[field]).read_text())
        assert hashlib.sha256((home.parents[2]/ev['path']).read_bytes()).hexdigest()==ev['sha256'],'R7 source correction render changed'
    import sympy as sp
    x=sp.Symbol('x',real=True)
    assert sp.simplify(sp.diff(sp.tan(x)-x,x)-sp.tan(x)**2)==0
    assert sp.simplify(sp.sympify(match['corrected_fields']['derived_answer'])-(sp.sqrt(3)/3-sp.pi/6))==0
    assert match['corrected_fields']['derivation_inputs']==dict(kind='proper-definite-integral',operands=['tan(x)**2','0','pi/6'])
    return True


def _current_evidence(inputs,wb=None):
    """Allow locator-only source-input revisions, never changed mathematics."""
    home=_wb(wb);root=home.parents[2]
    current={i['item_id']:i for i in json.loads((home/'analysis/textbook-inventory.json').read_text())['items']}
    hashes={};result={}
    for patch in inputs['entries']:
        for mp in patch['members']:
            actual={r['subpart']:r for r in current[mp['item_id']].get('answer_verification_r5',[])}
            evidence=copy.deepcopy(mp['membership_evidence_r6'])
            for baseline in evidence['responses']:
                row=actual[baseline['subpart']]
                for key in ('method','derived_answer','derivation_inputs'):
                    assert row.get(key)==baseline.get(key) or _r7_authorised_change(home,mp['item_id'],baseline['subpart'],key,baseline.get(key),row.get(key)), ('selected answer mathematics changed after prose authoring',mp['item_id'],baseline['subpart'],key)
                if any(row.get(k)!=baseline.get(k)for k in ('method','derived_answer','derivation_inputs')):
                    baseline['r7_authorised_source_correction']='YM543 actual tan²x; exact reviewed correction only'
                    for key in ('method','derived_answer','derivation_inputs'):baseline[key]=copy.deepcopy(row.get(key))
                assert row.get('source_input_path')==baseline.get('source_input_path'), 'selected answer input path changed'
                old=baseline.get('source_input_sha256');now=row.get('source_input_sha256');path=row.get('source_input_path')
                if path and now:
                    if path not in hashes:hashes[path]=hashlib.sha256((root/path).read_bytes()).hexdigest()
                    assert hashes[path]==now, ('current answer input hash is stale',mp['item_id'],path)
                baseline['author_baseline_source_input_sha256']=old
                baseline['source_input_sha256']=now
            result[mp['member_id']]=evidence
    return result


def apply(families,*,wb=None):
    """Mutate and return an assembled list (or families document) in memory."""
    inputs=_read(wb);evidence=_current_evidence(inputs,wb);rows=_rows(families);lookup={f['family_id']:f for f in rows}
    assert len(lookup)==len(rows),'duplicate family id in prose application'
    assert _identity(rows)==inputs['family_member_identity_sha256'], 'family/member identity changed before prose application'
    assert set(lookup)=={p['family_id']for p in inputs['entries']},'family prose input scope differs'
    for patch in inputs['entries']:
        f=lookup[patch['family_id']]
        for key in FIELDS:f[key]=patch[key]
        members={m['member_id']:m for m in f['members']}
        for mp in patch['members']:
            m=members[mp['member_id']]
            assert m['item_id']==mp['item_id'] and m['part_labels']==mp['part_labels'], 'prose patch selects different source responses'
            m['membership_reason']=mp['membership_reason']
            m['membership_evidence_r6']=copy.deepcopy(evidence[mp['member_id']])
        f['family_prose_evidence_r6']={'author_input':'tools/'+INPUT_NAME,
            'basis':'Author synthesis of accepted selected-response records; no new rendered reading or independent acceptance claimed.',
            'date':inputs['date']}
    if isinstance(families,dict):
        families['family_prose_limits_r6']=list(inputs['limits'])
    validate(rows,wb=wb)
    return families


def validate(families,*,wb=None):
    """Assert exact author-prose propagation and unchanged membership identity."""
    inputs=_read(wb);evidence=_current_evidence(inputs,wb);rows=_rows(families);by_id={f['family_id']:f for f in rows}
    assert _identity(rows)==inputs['family_member_identity_sha256'], 'family/member identity changed by prose repair'
    assert set(by_id)=={p['family_id']for p in inputs['entries']},'family prose scope incomplete'
    counts={'families':len(rows),'memberships':0,'nearest_sibling_differences':0,
            'units_and_precision':0,'single_member':0,'multi_member_ordered':0,
            'selected_response_membership_reasons':0}
    for p in inputs['entries']:
        f=by_id[p['family_id']];sib=f.get('nearest_sibling_family_id')
        assert sib in by_id and sib!=f['family_id'],'missing valid nearest sibling comparison'
        assert f.get('distinction_basis')==p['distinction_basis'],'nearest-sibling decision prose differs from author input'
        counts['nearest_sibling_differences']+=1
        assert f.get('units_and_precision')==p['units_and_precision'],'units/precision prose not propagated'
        counts['units_and_precision']+=1
        assert f.get('difficulty_progression')==p['difficulty_progression'],'ordered progression differs from author input'
        if len(f['members'])==1:
            assert f['difficulty_progression']=='single item','singleton has invented difficulty progression'
            counts['single_member']+=1
        else:
            text=f['difficulty_progression']
            assert text!='single item' and text.startswith(('Begin with','Begin by')) and ('then'in text.lower()or'finally'in text.lower()),'multi-member progression is not ordered'
            counts['multi_member_ordered']+=1
        expected={r['member_id']:r for r in p['members']}
        for m in f['members']:
            counts['memberships']+=1;e=expected[m['member_id']]
            assert m.get('membership_reason')==e['membership_reason'],'member-specific selected response reason absent'
            assert m.get('membership_evidence_r6')==evidence[m['member_id']],'member response evidence absent'
            assert {r['subpart']for r in m['membership_evidence_r6']['responses']}==set(m['part_labels']),'membership evidence does not name every selected response'
            counts['selected_response_membership_reasons']+=1
    assert counts['families']==500 and counts['memberships']==2385,'unexpected family/member scope'
    assert counts['single_member']==147 and counts['multi_member_ordered']==353,'single/multi progression counts changed'
    return dict(counts,limits=inputs['limits'],status='author prose propagation and identity checked; independent semantic review required')
