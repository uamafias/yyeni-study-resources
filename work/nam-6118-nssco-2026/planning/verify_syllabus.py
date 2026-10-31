"""Reopen the PDF and verify every stored transcription quotation and value."""
import hashlib
import json
import re
from pathlib import Path
import transcribe_syllabus as transcription

work=Path(__file__).resolve().parents[1]
facts=json.loads((work/'curriculum/syllabus-facts.json').read_text())
assert facts['source_sha256']==hashlib.sha256(transcription.PDF.read_bytes()).hexdigest()
checked=0


def verify(node):
    global checked
    if isinstance(node,dict):
        if node.get('provenance')=='syllabus' and 'verbatim' in node:
            page=node['pdf_page']
            assert node['verbatim'].strip(),node
            if 'bbox' in node:
                actual=transcription.region(page,*node['bbox'])['verbatim']
                assert actual==node['verbatim'],node
            else:
                assert transcription.norm(node['verbatim']) in transcription.norm(transcription.LAYOUT[page-1]),node
            checked+=1
        if 'value' in node and 'source' in node and not isinstance(node['value'],list):
            value=str(node['value'])
            assert value in transcription.norm(node['source']['verbatim']),node
        for value in node.values():
            verify(value)
    elif isinstance(node,list):
        for value in node:
            verify(value)


verify(facts)
# Reconcile every physical bullet, including the malformed pair retained on p.34.
specific=0
practical=0
for page in range(9,40):
    words=transcription.WORDS[page-1]
    headings=[w for w in words if w['text']=='SPECIFIC' and w['y']<100]
    for w in words:
        if w['text']!=transcription.BULLET:
            continue
        if headings and abs(w['x']-headings[0]['x'])<2:
            specific+=1
        elif w['x']<90:
            practical+=1
assert specific==len(facts['specific_objectives'])==335
assert practical==len(facts['required_practicals'])==61
assert len(facts['content_outline'])==len(facts['content_table_rows'])==78
assert len(facts['command_words'])==30
assert sum(p['marks']['value'] for p in facts['papers'])==160
assert sum(p['qualification_weight_percent']['value'] for p in facts['papers'])==100
assert facts['derived_reconciliation']['raw_mark_percent']=={'A':46.875,'B':28.125,'C':25.0}
assert facts['derived_reconciliation']['final_grade_percent']=={'A':50.0,'B':30.0,'C':20.0}
for p in facts['papers']:
    assert sum(r['marks_by_paper'][p['paper']]['value'] for r in facts['component_ao_marks'])==p['marks']['value']
decision_file=work/'curriculum/operator-decisions.json'
decision=json.loads(decision_file.read_text()) if decision_file.exists() else {}
approved=decision.get('step_2_tables',{}).get('status')=='approved'
result=dict(status='pass',quotation_records_reopened_and_verified=checked,
            specific_bullets_reconciled=specific,practical_bullets_reconciled=practical,
            human_checkpoint='Operator approved reviewed tables on 2026-10-31; approval is separate from agent verification.' if approved else 'pending; automated provenance checks do not constitute operator approval',
            visual_review_pdf_pages=[40,41,42,44,45,37,38,39,32])
(work/'planning/syllabus-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
