"""Subject-only mining adapter. Raw parsed rows require semantic review before publication.

No keyword matching to syllabus outcomes. Mappings are supplied separately by the miner.
Internal evidence extracts may quote source material; these are not learner resources.
"""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib, json, re
from pypdf import PdfReader

W = Path(__file__).resolve().parents[1]
ROOT = W.parents[1]
E = W / 'assessment-evidence'

def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def extract():
    manifest = []
    for f in json.loads((W/'source-inventory.json').read_text())['files']:
        if f['type'] not in ('question_paper', 'annual_examiner_report'):
            continue
        r = PdfReader(ROOT/f['path'])
        if f['type'] == 'question_paper':
            paper = re.search(r'6137[ /-]+([123])', r.pages[0].extract_text())[1]
            sid = f"6137-{f['year']}-P{paper}"
            inds = range(len(r.pages))
        else:
            paper = None
            sid = f"6137-{f['year']}-ER"
            start = f['geography_content_page']-1
            end = start
            for i in range(start, min(start+65,len(r.pages))):
                if i > start and re.search(r'\bHISTORY\b',r.pages[i].extract_text()[:800]):
                    break
                end=i+1
            inds=range(start,end)
        pages=[{'pdf_page':i+1,'text':r.pages[i].extract_text(),
                'layout':r.pages[i].extract_text(extraction_mode='layout')} for i in inds]
        dump(E/'extracted'/f'{sid}.json',pages)
        (E/'extracted'/f'{sid}.txt').write_text('\n\n'.join(
            f"=== PDF PAGE {p['pdf_page']} ===\n{p['text']}" for p in pages))
        manifest.append({**f,'source_id':sid,'paper_id':paper,
                         'extracted_pages':[p['pdf_page'] for p in pages],
                         'extraction':'pypdf plain and layout (Poppler unavailable); figures require visual review',
                         'hash_verified':hashlib.sha256((ROOT/f['path']).read_bytes()).hexdigest()==f['sha256']})
    dump(E/'extraction-manifest.json',manifest)

def clean(line):
    line=re.sub(r'\.{3,}', ' ', line).strip()
    if re.fullmatch(r'\d+|6137/\d/\d+|\[Turn over|For|Examiner[’\x27]s|Use|926460',line): return ''
    return line

def parse():
    """Bracket terminal extraction; separate totals and unnumbered subparts explicitly."""
    records=[]; audits=[]
    for src in json.loads((E/'extraction-manifest.json').read_text()):
        if src['type']!='question_paper':continue
        q=a=roman=sub=None; buffer=[]; locs=[]; counts=Counter(); seq=Counter()
        pages=json.loads((E/'extracted'/f"{src['source_id']}.json").read_text())
        for p in pages[1:]:
            for raw in p['text'].splitlines():
                line=clean(raw)
                if not line:continue
                # Root labels require a letter subpart, excluding figure/table numbers.
                m=re.match(r'^([1-7])\s+(?=\([a-g]\)|Study\b|Figs?\.?\b|Four\b|Another\b|Photograph\b|The\b|A\b|Geography\b|Students\b|Table\b|Read\b)',line)
                if m:
                    q=m[1];a=None;roman=sub=None;buffer=[];locs=[]
                    line=line[m.end():].strip()
                m=re.match(r'^\(([a-h])\)',line)
                if m:
                    a=m[1];roman=sub=None;buffer=[];locs=[];line=line[m.end():].strip()
                m=re.match(r'^\(([ivx]+)\)',line)
                if m:
                    roman=m[1];sub=None;buffer=[];locs=[];line=line[m.end():].strip()
                m=re.match(r'^\(([a-d]{2})\)',line)
                if m:
                    sub=m[1];buffer=[];locs=[];line=line[m.end():].strip()
                # Capital response slots are tracked only when a preceding tariff split occurs.
                if q is None:continue
                buffer.append(line);locs.append(p['pdf_page'])
                for m in re.finditer(r'\[\s*(\d+)\s*\]',line):
                    n=int(m[1])
                    if n>=20 or not re.sub(r'\[\s*\d+\s*\]|[\W_]+','','\n'.join(buffer)):
                        audits.append({'source_id':src['source_id'],'pdf_page':p['pdf_page'],
                                       'question':q,'printed_total':n})
                        buffer=[];locs=[];continue
                    ref=q+(f'({a})' if a else '')+(f'({roman})' if roman else '')+(f'({sub})' if sub else '')
                    seq[ref]+=1
                    rid=ref if seq[ref]==1 else ref+f'#{seq[ref]}'
                    records.append({'evidence_id':src['source_id']+'-'+rid,
                         'source_id':src['source_id'],'exam_series':str(src['year']),
                         'year':src['year'],'paper_id':src['paper_id'],'variant':None,
                         'question_ref':rid,'mark_tariff':n,
                         'source_locator':{'path':src['path'],'pdf_pages':sorted(set(locs))},
                         'source_excerpt':'\n'.join(buffer), 'parse_status':'requires semantic review'})
                    counts[q]+=n;buffer=[];locs=[]
        print(src['source_id'],dict(counts),'sum',sum(counts.values()))
    dump(E/'parsed-question-parts.json',{'records':records,'printed_totals':audits})
    (E/'question-parts-review.txt').write_text('\n'.join(
        f"{r['evidence_id']} [{r['mark_tariff']}] p{r['source_locator']['pdf_pages']} "
        + re.sub(r'\s+',' ',r['source_excerpt']) for r in records))

def extract_report_blocks():
    """Preserve raw block refs; build_analysis applies the audited semantic crosswalk."""
    blocks=[]
    for f in sorted((E/'extracted').glob('*ER.json')):
        year=int(f.stem.split('-')[1]);paper='1';q=a=rom=sub=None;buf=[];loc=[]
        def flush():
            if buf:blocks.append({'year':year,'paper_id':paper,
                'question_ref':(q or '')+(f'({a})' if a else '')+(f'({rom})' if rom else '')+(f'({sub})' if sub else ''),
                'pdf_pages':sorted(set(loc)),'text':'\n'.join(buf)})
        for p in json.loads(f.read_text()):
            for raw in p['text'].splitlines():
                line=raw.strip()
                if re.fullmatch(r'NSSCO Examiners Report \d+|\d+|6137|GEOGRAPHY',line):continue
                m=re.match(r'^Paper\s+([123])\b',line)
                if m:flush();buf=[];loc=[];paper=m[1];q=a=rom=sub=None;continue
                m=re.match(r'^(?:([1-7])\s+)?\(([a-h])\)(?:\s+\(([ivx]+)\))?(?:\s+\(([a-d]{2})\))?',line)
                n=re.match(r'^\(([ivx]+)\)(?:\s+\(([a-d]{2})\))?',line)
                if m or n:
                    flush();buf=[];loc=[]
                    if m:
                        if m[1]:q=m[1]
                        a=m[2];rom=m[3];sub=m[4]
                    else:rom=n[1];sub=n[2]
                buf.append(line);loc.append(p['pdf_page'])
        flush()
    for i,b in enumerate(blocks):b['finding_block_id']=f'ER6137-{b["year"]}-P{b["paper_id"]}-{i+1:04}'
    dump(E/'report-blocks.json',blocks)

if __name__=='__main__':
    import sys
    if '--extract' in sys.argv:extract()
    parse()
    extract_report_blocks()
