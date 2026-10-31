"""Extract the syllabus table's specific-objective column with PDF provenance."""
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = Path(__file__).resolve().parents[1]
PDF = ROOT / 'Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_Chemistry_syllabus.pdf'


def main():
    pages = subprocess.check_output(['pdftotext', '-layout', str(PDF), '-'], text=True).split('\f')
    facts = json.loads((WORK/'curriculum/syllabus-facts.json').read_text())
    headings = {s['number']: s['name'] for t in facts['content_outline'] for s in t['subtopics']}
    records = []
    current = None
    active = None
    practicals = []
    for page_number in range(9, 41):
        active = None
        lines = pages[page_number-1].splitlines()
        header = next((line for line in lines if 'SPECIFIC OBJECTIVES' in line), None)
        if not header:
            continue
        column = header.index('SPECIFIC OBJECTIVES')
        in_table = True
        for line_number,line in enumerate(lines,1):
            if line.strip().startswith('The practical '):
                in_table = False
                active = None
            if not in_table:
                if '' in line:
                    practicals.append({'practical_id':f'SP-6117-{len(practicals)+1:02d}','syllabus_topic':current.split('.')[0],
                        'pdf_page':page_number,'text':line.strip().lstrip('').strip()})
                elif practicals and practicals[-1]['pdf_page']==page_number and line.strip() and not line.strip().isdigit() and 'NSSCO Chemistry Syllabus' not in line:
                    practicals[-1]['text']+=' '+line.strip()
                continue
            if 'NSSCO Chemistry Syllabus' in line or 'SPECIFIC OBJECTIVES' in line or line.strip().isdigit():
                continue
            left = line[:31]
            heading = re.match(r'^\s*(\d+\.\d+(?:\.\d+)?)\.?\s', left)
            if heading and heading.group(1) in headings:
                current = heading.group(1)
            bullets = [m.start() for m in re.finditer('',line) if m.start() >= column-3]
            if bullets:
                assert current,(page_number,line)
                start = bullets[-1]
                active = {'syllabus_subtopic':current,'subtopic_heading':headings[current],
                          'source_pdf_page':page_number,'source_printed_page':page_number-3,
                          'source_lines':[],'text_lines':[]}
                records.append(active)
                text = line[start+1:].strip()
            else:
                text = line[column:].strip() if len(line)>column else ''
            diagram_tokens = text.split()
            diagram_line = diagram_tokens and all(token in {'H','C','N','O','S','Cl','Br','I','P','F','−','-','='} for token in diagram_tokens)
            if active and text and not text.startswith('Learners should') and not diagram_line:
                active['text_lines'].append(text)
                active['source_lines'].append({'pdf_page':page_number,'line':line_number,'verbatim_line':line.rstrip()})
    counts=Counter()
    for r in records:
        sub=r['syllabus_subtopic'];counts[sub]+=1
        r['outcome_id']=f'SYL-6117-{sub}-{counts[sub]:02d}'
        r['syllabus_text']=' '.join(r.pop('text_lines'))
        assert r['syllabus_text'],r
    out={'status':'extracted_for_semantic_planning_review','source':str(PDF.relative_to(ROOT)),
         'method':'Specific-objective bullets from the right-hand syllabus column; continuation and nested-list lines remain attached to their parent bullet. All rows retain original PDF page/line text.',
         'outcomes':records,'suggested_practicals':practicals}
    (WORK/'curriculum/syllabus-outcomes.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print('Extracted',len(records),'specific objectives across',len(counts),'subtopics')
    for sub,n in counts.items():print(sub,n)


if __name__=='__main__':main()
