"""Reconcile each written marked part with its report guidance provenance."""
import json
from collections import Counter
from pathlib import Path

WORK=Path(__file__).resolve().parents[1]
AE=WORK/'assessment-evidence'
def read(name):return json.loads((AE/name).read_text())

def main():
    evidence=read('assessment_evidence.json')['records']
    aligned=read('report-guidance-alignment.json')['aligned_parts']
    audited={x['evidence_id']:x for x in read('report-alignment-audit.json')['parts']}
    manual={}
    for name in ('manual-credit-2020.json','manual-credit-supplement.json'):
        manual.update(read(name)['records'])
    rows=[]
    for item in evidence:
        if item['mark_tariff'] is None or item['paper_id']=='1':continue
        eid=item['evidence_id']; provenance=manual.get(eid)
        if provenance:status=provenance.get('status','paraphrased_scanned_answer_table')
        elif item['year']==2025 and any('Credit shape paraphrased' in n for n in item['notes']):status='paraphrased_answer_table'
        elif eid in aligned and audited[eid]['status'].startswith('verified_'):status='verified_internal_source_row_requires_paraphrase'
        elif eid in aligned:status='unresolved_answer_row_link'
        else:status='no_part_guidance_found'
        rows.append({'evidence_id':eid,'year':item['year'],'paper_id':item['paper_id'],
                     'question_ref':item['question_ref'],'mark_tariff':item['mark_tariff'],
                     'status':status,'question_locator':item['source_locator'],
                     'report_locator':aligned.get(eid,{}).get('source_locator'),
                     'alignment_audit_status':audited.get(eid,{}).get('status'),
                     'report_pdf_page':provenance.get('report_pdf_page') if provenance else None})
    counts=dict(sorted(Counter(x['status'] for x in rows).items()))
    output={'status':'part_level_provenance_audit','written_parts':len(rows),'counts':counts,
            'note':'Internal answer rows are source quotations for mining only. Paraphrase and independently check calculations before learner use. The five 2022 Paper 2 Q3 parts have report commentary but no printed part-level allocation.',
            'parts':rows}
    (AE/'guidance-coverage.json').write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
    print(counts)

if __name__=='__main__':main()
