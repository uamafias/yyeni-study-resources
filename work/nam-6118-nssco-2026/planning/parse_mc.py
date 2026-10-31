"""Split the 240 MC items for internal semantic review; do not infer commands."""
from pathlib import Path
import json,re

WORK=Path(__file__).resolve().parents[1]


def main():
    inv=json.loads((WORK/'assessment-evidence/extraction-manifest.json').read_text())
    rows=[]
    for source in inv['records']:
        if source.get('paper')!=1:continue
        text=(WORK/source['outputs']['layout']['path']).read_text()
        page=1;current=None;items=[]
        for line in text.splitlines():
            p=re.match(r'=== SOURCE PDF PAGE (\d+) ===',line)
            if p:page=int(p[1]);continue
            if page==1:continue
            m=re.match(r'^\s{0,5}(\d{1,2})\s+(\S.*)',line)
            if m and int(m[1])==len(items)+1:
                current={'evidence_id':f"6118-{source['year']}-P1-{int(m[1]):03d}",
                         'source_id':source['source_id'],'year':source['year'],
                         'paper_id':'1','question_ref':m[1],'mark_tariff':1,
                         'source_locator':{'path':source['path'],'pdf_pages':[page]},
                         'internal_source_text':line.strip(),'semantic_review_status':'pending'}
                items.append(current)
            elif current:
                if re.match(r'^\s*(?:6118/1/|©|\[Turn over)',line):continue
                if 'Periodic Table' in line or 'BLANK PAGE' in line:
                    current=None;continue
                if line.strip():
                    current['internal_source_text']+='\n'+line.rstrip()
                    if page not in current['source_locator']['pdf_pages']:current['source_locator']['pdf_pages'].append(page)
        assert len(items)==40,(source['year'],len(items))
        rows.extend(items)
    assert len(rows)==240
    (WORK/'assessment-evidence/mc-items-draft.json').write_text(json.dumps({'status':'DRAFT; source demand/diagram review pending','records':rows},indent=2,ensure_ascii=False)+'\n')
    print('Parsed all 240 MC question numbers; semantic mapping and keys pending.')


if __name__=='__main__':main()
