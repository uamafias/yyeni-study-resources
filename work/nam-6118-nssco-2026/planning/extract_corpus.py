"""Extract internal 6118 corpus in layout/raw order with original PDF pages."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'work/nam-6118-nssco-2026'


def main():
    decisions=json.loads((WORK/'curriculum/operator-decisions.json').read_text())
    assert decisions['working_syllabus']['status']=='operator_approved_for_progression'
    assert decisions['step_2_tables']['status']=='approved'
    inventory=json.loads((WORK/'curriculum/source-inventory.json').read_text())
    out=WORK/'planning/extracted';out.mkdir(exist_ok=True)
    manifest=[]
    for source in inventory['entries']:
        if source['kind']=='syllabus':continue
        pdf=ROOT/source['path']
        assert hashlib.sha256(pdf.read_bytes()).hexdigest()==source['sha256']
        report=source['kind']=='combined_examiner_report'
        stem=f"{source['year']}-"+('report' if report else f"paper-{source['paper']}")
        record={'source_id':'6118-'+stem,'path':source['path'],'sha256':source['sha256'],
                'year':source['year'],'kind':source['kind'],'outputs':{}}
        if report:
            first=source['physics_pdf_pages']['first'];last=source['physics_pdf_pages']['last']
        else:
            first=1;last=source['pdf_pages'];record['paper']=source['paper']
        for mode in ('layout','raw'):
            text=subprocess.check_output(['pdftotext','-'+mode,'-f',str(first),'-l',str(last),str(pdf),'-'],text=True)
            pages=text.split('\f')
            if not pages[-1].strip():pages.pop()
            assert len(pages)==last-first+1,(stem,mode,len(pages),first,last)
            assert sum(map(len,pages))>100
            labelled='\n\n'.join(f'=== SOURCE PDF PAGE {i} ===\n{page}' for i,page in enumerate(pages,first))
            path=out/f'{stem}.{mode}.txt';path.write_text(labelled+'\n')
            record['outputs'][mode]={'path':str(path.relative_to(WORK)),
                                      'first_pdf_page':first,'last_pdf_page':last,
                                      'characters':len(text),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
        manifest.append(record)
    assert len(manifest)==24
    (WORK/'assessment-evidence').mkdir(exist_ok=True)
    dest=WORK/'assessment-evidence/extraction-manifest.json'
    dest.write_text(json.dumps({'scope':'Internal evidence only; source wording must not enter learner-facing resources.',
                               'question_papers':18,'examiner_reports':6,'records':manifest},indent=2)+'\n')
    print(f'Extracted {len(manifest)} documents in both layout/raw modes; source hashes and page counts verified.')


if __name__=='__main__':main()
