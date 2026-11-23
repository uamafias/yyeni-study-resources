"""Validate R6 key-page corrections in canonical, flat and nested records.

A passing locator check does not certify the mathematical answer or independent
review. Render inspection is recorded separately in the author boundary audit.
"""
import json,hashlib
from analysis_sources import ROOT,WB,A

def check(items=None,answers=None):
    inventory=items or json.loads((A/'textbook-inventory.json').read_text())['items']
    answers=answers or json.loads((A/'textbook-answer-verification-r5.json').read_text())['subparts']
    byid={i['item_id']:i for i in inventory};flat={(x['item_id'],x['subpart']):x for x in answers}
    audit=json.loads((A/'textbook-answer-page-audit-r6.json').read_text())
    assert audit['coverage']['read_regions']==103
    assert len(audit['pages'])==103
    for r in audit['pages']:
        assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256'],('key-page render changed',r['path'])
        assert r['inspection_status']=='author inspected rendered top/column-start region'
        assert r['top_observation']
        if r['read_date']=='2026-11-23':
            from apply_textbook_source_repairs_r7 import _read,_evidence
            patch=next((p for p in _read()['page_observation_repairs']if p['book']==r['book']and p['pdf_page']==r['pdf_page']),None)
            assert patch and r['top_observation']==patch['top_observation']and r.get('r7_native_confirmation')==_evidence(patch),'unrecognised later answer-page observation'
        else:assert r['read_date']=='2026-11-22'
    leaf_count=0
    for patch in audit['findings']:
        i=byid[patch['item_id']]
        nested={x['subpart']:x for x in i['answer_verification_r5']}
        for part in patch['subparts']:
            for where,row in [('flat',flat[(i['item_id'],part)]),('nested',nested[part])]:
                assert row['answer_pdf_page']==patch['answer_pdf_page'],(where,i['item_id'],part,'wrong answer PDF page',row['answer_pdf_page'])
                assert row['answer_printed_page']==patch['answer_printed_page'],(where,i['item_id'],part,'wrong printed page')
            leaf_count+=1
        for pages,expected in [('pdf_pages','answer_pdf_page'),('printed_pages','answer_printed_page')]:
            assert patch[expected]in i['answer_key'][pages],('parent answer key missing corrected page',i['item_id'],pages)
        if i['item_id'].startswith('8227:TB:YM:C3:') and any(i['item_id'].endswith(s)for s in ['Try-Now-4:2','Try-Now-4:3','Try-Now-4:4']):
            assert i['answer_key']['pdf_pages']==[599],('stale parent page',i['item_id'])
    return {'end_key_pages_visually_inspected':103,'corrected_leaf_locations_checked':leaf_count,'new_question_locator_corrections':8,'preserved_prior_question_locator_corrections':2,'flat_and_nested_and_parent_agree':True,'additional_r7_locator_corrections':2 if audit.get('r7_repairs') else 0,'total_recorded_locator_findings':len(audit['findings'])}

if __name__=='__main__':print(json.dumps(check(),indent=2))
