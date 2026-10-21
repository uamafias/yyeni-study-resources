"""6136 corpus extraction. Source text and evidence are internal, never learner output."""
import json,re,subprocess,hashlib
from pathlib import Path
from collections import Counter

WS=Path(__file__).resolve().parents[1];REPO=WS.parents[1]
EV=WS/'assessment-evidence';TEXT=EV/'extracted'
TEXT.mkdir(parents=True,exist_ok=True)
norm=lambda s:re.sub(r'\s+',' ',s).strip()
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
source_manifest=json.loads((REPO/'operations/handover/6136-dev-studies-retrofit/output/source-manifest.json').read_text())
sources=[]
report_ranges={2020:(125,140),2021:(117,130),2022:(143,158),2023:(155,172),2024:(153,170)}
for x in source_manifest:
    path=REPO/x['path']
    if 'Question Banks/' not in x['path']:continue
    assert hashlib.sha256(path.read_bytes()).hexdigest()==x['sha256']
    report='Examiner Reports' in x['path'];year=int(path.parent.name)
    paper=None if report else int(re.search(r'6136[_-]([123])',path.name)[1])
    sid=f'6136-{year}-'+('ER' if report else f'P{paper}')
    src={**x,'source_id':sid,'year':year,'paper_id':None if report else f'P{paper}',
      'kind':'examiner_report' if report else 'question_paper','series':'year only; month not stated in inventory',
      'pdf_page_range':list(report_ranges[year]) if report else None}
    for mode in ['layout','raw']:
        target=TEXT/f'{sid}-{mode}.txt'
        if not target.exists():
            args=['pdftotext','-'+mode]
            if report:
                a,z=report_ranges[year];args+=['-f',str(a),'-l',str(z)]
            subprocess.run(args+[str(path),str(target)],check=True)
        assert len(target.read_text().strip())>500
    sources.append(src)
dump(EV/'source-manifest.json',sources)

records=[];unassigned=[]
for src in sources:
    if src['kind']!='question_paper':continue
    pages=(TEXT/f'{src["source_id"]}-layout.txt').read_text().split('\f')
    root=None;letter=None;roman=None;active=[];pending=[];startpage=None;subtotal=[]
    for pg,txt in enumerate(pages,1):
        if pg==1:continue
        for rawline in txt.splitlines():
            rawline=re.sub(r'\s{3,}Use\s*$','',rawline)
            s=norm(rawline)
            if not s:continue
            if re.search(r'For Examiner|Examiner’s|Examiner.s|^Use$|^For$|6136[/ ]|Turn over|^\d{5,}$|^\d{1,2}$',s):continue
            if s.count('.')>=5: # answer lines sometimes end in a tariff
                s=re.sub(r'\.{3,}','',s).strip()
                if not s:continue
                if re.fullmatch(r'\d{1,2}|[A-F][.]?',s):continue
            if 'SECTION ' in s or 'BLANK PAGE' in s:continue
            top=re.match(r'^(\d{1,2})\s+(.*)',s)
            if top and re.match(r'(?:Study|Fig\.|During|In\b|You\b|The questions|\([a-z]\))',top[2]):
                root=top[1];letter=None;roman=None;pending=[];active=[];s=top[2]
            # A root beginning directly with an (a) marker may have no following space.
            compact=re.match(r'^(\d{1,2})\s*\(([a-z])\)',s)
            if compact:
                root=compact[1];letter=None;roman=None;s=s[len(compact[1]):].lstrip()
            markers=re.match(r'^(\([a-z]\))?\s*(\([ivx]+\))?\s*(.*)',s)
            lm=markers[1];rm=markers[2];body=markers[3]
            # A sole (i)/(v) is a roman part, never a fresh letter section.
            if lm and lm in ['(i)','(v)','(x)'] and not rm:rm,lm=lm,None
            if lm or rm:
                if lm:letter=lm[1:-1];roman=None
                if rm:roman=rm[1:-1]
                active=[];pending=[];startpage=pg;s=body
            tariff=re.search(r'\[(\d+)\]',s)
            if tariff:
                n=int(tariff[1]);body=s[:tariff.start()].strip()
                if body:active.append(body)
                # Bare high totals are subtotals. Explicit new assessed stems are kept.
                if not active:
                    subtotal.append({'page':pg,'marks':n});continue
                stem=norm(' '.join(active))
                if root is None or letter is None:
                    unassigned.append({'source':src['source_id'],'page':pg,'marks':n,'text':stem});active=[];continue
                ref=root+f'({letter})'+(f'({roman})' if roman else '')
                records.append({'evidence_id':f'{src["source_id"]}-{ref}','source_id':src['source_id'],
                  'year':src['year'],'exam_series':src['series'],'paper_id':src['paper_id'],'variant':None,
                  'question_ref':ref,'mark_tariff':n,'stem_internal':stem,
                  'source_locator':{'path':src['path'],'pdf_page':startpage or pg,'tariff_pdf_page':pg},
                  'proof':src['proof'],'mapping_method':'pending semantic reading; extraction only'})
                active=[];startpage=None
            elif letter is not None:
                # Retain until a tariff or a new part. Noise is removed before analysis.
                active.append(s)
    total=sum(r['mark_tariff'] for r in records if r['source_id']==src['source_id'])
    print(src['source_id'],len([r for r in records if r['source_id']==src['source_id']]),'marks',total,'expected',{'P1':80,'P2':70,'P3':50}[src['paper_id']])
dump(EV/'question-parts-draft.json',records);dump(EV/'unassigned-tariffs.json',unassigned)
assert len({r['evidence_id'] for r in records})==len(records)
print('Records',len(records),'unassigned',len(unassigned),'marks',sum(r['mark_tariff'] for r in records))
