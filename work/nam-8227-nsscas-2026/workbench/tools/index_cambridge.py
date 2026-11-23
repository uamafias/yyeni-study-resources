"""Index already-held 9709 PDFs for 8227 evidence discovery. No web access."""
import collections
import json
from pathlib import Path
import re
from pypdf import PdfReader
from analysis_sources import ROOT, A, digest, write

BASE=ROOT/'Question Banks/Cambridge Curricula/Cambridge AS and A Level/Mathematics (9709)'
QUERIES={
 'monotonicity':r'increasing|decreasing', 'segment':r'\bsegment\b',
 'unit-vector':r'unit\s+vector', 'inflexion':r'inflexion|inflection',
 'inverse-principal':r'principal|sin[−–-]1|cos[−–-]1|tan[−–-]1|sin\s*[−–-]\s*1|cos\s*[−–-]\s*1',
 'quadratic-division':r'divid|quotient', 'iteration-failure':r'converg|diverg|oscillat',
 'cubic-from-graph':r'cubic|degree\s*(?:3|three)',
 'function-definition':r'one.one|domain|range|composite',
 'radian':r'radian|degrees', 'identity-equation':r'identity|identically',
 'quadratic-sketch':r'sketch|draw|diagram',
}


def main():
    output=A/'cambridge-discovery';output.mkdir(exist_ok=True)
    records=[];hits=[];unusable=[]
    for path in sorted(BASE.rglob('*.pdf')):
        m=re.fullmatch(r'9709_([msw])(\d{2})_(qp|ms)_([123]\d)\.pdf',path.name)
        if not m or not 15<=int(m[2])<=25:continue
        b=path.read_bytes()
        if not b.startswith(b'%PDF'):
            unusable.append({'path':str(path.relative_to(ROOT)),'reason':'not real PDF / LFS pointer'});continue
        rec={'path':str(path.relative_to(ROOT)),'sha256':digest(path),
             'year':2000+int(m[2]),'session_code':m[1],'kind':m[3],'component':m[4]}
        target=output/(path.stem+'-'+rec['sha256'][:12]+'.json')
        if target.exists():
            data=json.loads(target.read_text());assert data['sha256']==rec['sha256']
        else:
            pdf=PdfReader(path)
            data={**rec,'extraction':'pypdf; discovery only, not mathematical transcription',
                  'pages':[{'pdf_page':i,'text':p.extract_text()} for i,p in enumerate(pdf.pages,1)]}
            write(target,data)
        rec['page_count']=len(data['pages']);records.append(rec)
        if rec['kind']=='qp':
            for p in data['pages']:
                for query,rx in QUERIES.items():
                    matches=list(re.finditer(rx,p['text'],re.I))
                    if matches:hits.append({'file':path.name,'source_path':rec['path'],'pdf_page':p['pdf_page'],
                        'query':query,'snippets':[re.sub(r'\s+',' ',p['text'][max(0,x.start()-90):x.end()+140]) for x in matches]})
    write(A/'cambridge-corpus-index.json',{'source':'existing local holdings only; duplicate filenames are retained with distinct content hashes',
          'documents':records,'unusable':unusable,'counts':dict(collections.Counter(r['kind']+'-P'+r['component'][0] for r in records)),
          'limits':'P1/P2 2015-2025 searched; P3 leads indexed separately for strictly in-scope parts. Regex hits are not verified items.'})
    write(A/'cambridge-search-leads.json',{'queries':QUERIES,'hits':hits,'verification':'unverified discovery only'})
    print(len(records),'local documents indexed;',len(hits),'page/query leads;',len(unusable),'unusable')


if __name__=='__main__':main()
