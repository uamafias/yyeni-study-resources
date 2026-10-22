#!/usr/bin/env python3
"""Index acquired reference sources; map topics without claiming claim verification."""
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
from bs4 import BeautifulSoup

WS=Path(__file__).resolve().parents[1]
ROOT=WS.parents[1]
PACK=WS/'sources/reference-pack'


def main():
    rows=list(csv.DictReader((WS/'planning/source-preparation/acquisition.csv').open()))
    sources=[]
    for row in rows:
        p=ROOT/row['folder']/row['filename']
        if not p.is_file():raise FileNotFoundError(p)
        entry={'source_id':p.stem,'path':str(p.relative_to(ROOT)),'url':row['url'],'retrieved_date':'2026-10-22','sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'role':'factual_reference'}
        if p.suffix=='.html':
            soup=BeautifulSoup(p.read_text(),'html.parser')
            article=soup.select_one('[data-type="page"][data-book-content="true"]')
            if article is None:raise ValueError(f'No textbook content in {p}')
            text=article.get_text('\n',strip=True)
            if len(text)<1000:raise ValueError(f'Too little textbook content in {p}')
            # Preserve alternative text for formula/structure images when searching offline.
            alts=[im.get('alt','') for im in article.select('img[alt]') if im.get('alt')]
            p.with_suffix('.txt').write_text('Source: '+row['url']+'\n\n'+text+'\n\nImage alternative text:\n'+'\n'.join(alts)+'\n')
            entry.update(title=soup.title.get_text() if soup.title else p.stem,extracted_characters=len(text),text_path=str(p.with_suffix('.txt').relative_to(ROOT)))
        elif p.suffix=='.pdf':
            text=p.with_suffix('.txt')
            if not text.exists():subprocess.run(['pdftotext','-layout',str(p),str(text)],check=True)
            info=subprocess.run(['pdfinfo',str(p)],capture_output=True,text=True,check=True).stdout
            entry.update(pages=int(re.search(r'Pages:\s+(\d+)',info).group(1)),text_path=str(text.relative_to(ROOT)))
        if p.name=='NSSCASExaminersReport2025.pdf':
            assert entry['sha256'].startswith('8012a5d92edfde9e')
            entry.update(source_id='SRC-8224-ER-2025',role='assessment_evidence',recovery='Exact original hash match; no evidence re-mining necessary.')
        sources.append(entry)
    syllabus=ROOT/'Syllabi/Namibian Curricula/NSSCAS/NSSCAS_8224_Chemistry_approved_syllabus_updated_20_November_2020.pdf'
    sources.insert(0,{'source_id':'NSSCAS-8224-SYLLABUS','aliases':['SRC-8224-SYLLABUS'],'path':str(syllabus.relative_to(ROOT)),'sha256':hashlib.sha256(syllabus.read_bytes()).hexdigest(),'role':'governing_syllabus','retrieved_date':'Already held; verified in earlier syllabus stage'})
    registry=json.loads((WS/'curriculum/objective_registry.json').read_text())
    chapters={'1.1':['2.3','3.1','3.2','3.3','4.1','4.3','4.5'],'1.2':['2.3','6.3','6.4','6.5','6.6'],'1.3':['7.1','7.2','7.3','7.6','10.1','10.5','10.6'],'1.4':['9.2','9.6'],'2.1':['5.1','5.2','5.3'],'2.2':['4.2','17.1','17.7'],'2.3':['13.1','13.2','13.3','14.1','14.2'],'2.4':['12.1','12.2','12.5','12.7'],'3.1':['6.6','18.1'],'3.2':['18.1','18.2'],'3.3':['19.1','19.2'],'3.4':['18.11'],'3.5':['18.7','18.10'],'4.1':['20.1'],'4.2':['20.1'],'4.3':['20.1'],'4.4':['20.2'],'4.5':['20.1'],'4.6':['20.3'],'4.7':['20.3'],'5.1':['1.4','1.5','1.6','4.5']}
    organic={'4.1':['1-12-','3-1-','3-4-','6-2-','6-5-'],'4.2':['3-2-','6-6-','7-3-','7-7-','8-2-','8-6-','8-10-','10-2-','15-2-','16-1-','16-2-'],'4.3':['10-1-','10-2-','11-1-','11-2-','11-4-'],'4.4':['17-1-','17-2-','17-6-','17-7-','17-10-'],'4.5':['3-2-','5-1-','5-3-','7-4-'],'4.6':['19-1-','19-3-','19-4-','19-6-'],'4.7':['20-1-','20-2-','20-5-','21-4-','21-6-']}
    table=[]
    for topic,sections in chapters.items():
        section_sources=[s for s in sources if any(Path(s['path']).name.startswith(pr) for pr in organic.get(topic,[])) or (topic=='4.4' and s['source_id']=='OpenStax-organic-17.1')]
        objs=[o['objective_id'] for o in registry['objectives'] if o.get('parent_id') and o['topic_id']==topic]
        table.append({'topic_id':topic,'objective_ids':objs,'syllabus_source_id':'NSSCAS-8224-SYLLABUS','general_chemistry_sections':sections,'organic_source_ids':[s['source_id'] for s in section_sources],'practical_authority':'NSSCAS syllabus Annexe A' if topic=='5.1' else None,'status':'Reference route available; each authored claim still requires an exact locator and semantic verification.'})
    data={'purpose':'Authoring reference pack; no curriculum or work-order regeneration','edition_note':'OpenStax Chemistry is the 2015 edition, revision C-2015-002(03/17)-LC, not Chemistry 2e. Organic sections are from the current publisher-hosted Tenth Edition; the study guide is supplementary.','source_policy':'Use for facts and transparent derivations. Syllabus and exclusions govern scope. Write original prose and figures. Do not copy exercises, explanations or source diagrams. Preserve source licences/attribution on source copies.','limits':['Sources exceed NSSCAS scope; consult the frozen contract exclusions for each topic.','The textbook is not evidence of Namibia-specific marking rules.','Topic-level reference routes do not certify that every objective or claim has been independently verified.','The 2015 textbook predates the 2019 SI revision; use the current 2e mole section and syllabus conventions for amount-of-substance definitions and supplied constants.'],'sources':sources,'topics':table}
    (PACK/'references.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    lines=['# Chemistry 8224 authoring reference pack','','The governing syllabus and approved work orders are unchanged. The original 2025 examiner report has been recovered from NIED with the exact original hash. No assessment evidence was reclassified.','','## How to use this pack','','Search the local `.txt` files, then inspect the cited PDF page or HTML section. Record source ID plus page/section on every claim. The following routes help find material; they do not mark claims verified. Respect each topic’s exclusions and create original explanations, examples and figures.','','OpenStax Chemistry: 2015 edition, 2017 revision, 1,355 PDF pages. It is not Chemistry 2e. Use the separately archived current Chemistry 2e §3.1 for the modern mole definition. The 222-page Organic Chemistry Tenth Edition study guide supplements the 40 archived textbook sections. Both books cover material outside NSSCAS; consult the syllabus first.','','## Topic routes','','| Topic | General Chemistry sections | Archived organic textbook sections |','|---|---|---|']
    for row in table:
        organic_sections=', '.join(re.match(r'(\d+)-(\d+)',s).group(0).replace('-','.') if re.match(r'(\d+)-(\d+)',s) else '17.1' for s in row['organic_source_ids'])
        lines.append(f"| {row['topic_id']} | {', '.join(row['general_chemistry_sections'])} | {organic_sections or ('Syllabus Annexe A governs practical work' if row['topic_id']=='5.1' else '—')} |")
    lines+=['','## Provenance and limits','','`references.json` records original URLs, paths, SHA-256 hashes, extraction checks and topic/objective routes. Acquisition attempts, including failed superseded PDF links, are recorded by the shared harvester. The two `*-publisher.html` files are discovery shells and are excluded from the usable-source inventory.','','Missing official mark schemes and older examiner reports remain documented evidence limitations. Source availability does not turn generated claims into verified claims.']
    (PACK/'README.md').write_text('\n'.join(lines)+'\n')
    print(f'Indexed {len(sources)} primary sources, including {sum(s.get("path","").endswith(".html") for s in sources)} substantive textbook sections, across {len(table)} topics.')


if __name__=='__main__':main()
