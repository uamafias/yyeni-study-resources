"""Exhaustive local page-to-question lexical/value discovery, never web harvesting.
Thresholds are explicit and independent of a top-N ranking. Reading is a separate act.
"""
import json,re,unicodedata
from collections import Counter,defaultdict
from analysis_sources import A,ROOT,clean,digest,write

STOP=set('the and that this with from have find show hence given curve equation value values question paper mathematics international cambridge use examiner for which where answer correct diagram marks following point points all not are in of to is it an as be on or by at its a when then such part using there no'.split())

def content_count(phrase):return sum(w not in STOP for w in phrase.split())

def normalise(text):
    text=unicodedata.normalize('NFKC',clean(text)).lower().replace('−','-').replace('–','-')
    text=re.sub(r'www\.[^\s]+|©[^\n]*|\b(?:9709|8227)/\S+|for examiner.?s use',' ',text)
    text=re.sub(r'/[a-z]+',' ',text)
    text=re.sub(r'\[\s*\d+\s*\]',' ',text)
    return text

def phrases(t,n):
    words=re.findall(r'[a-z]{2,}',t)
    return {' '.join(words[i:i+n]) for i in range(len(words)-n+1)}

def values(t):
    return set(re.findall(r'(?<!\d)(?:\d+\.\d+|[3-9]|[1-9]\d+)(?!\d)',t))

def build():
    docs=json.loads((A/'cambridge-corpus-index.json').read_text())['documents']
    paths=defaultdict(list)
    for d in docs:
        if d['kind']=='qp':paths[d['sha256']].append(d['path'])
    pages=[]
    for f in sorted((A/'cambridge-discovery').glob('*.json')):
        d=json.loads(f.read_text())
        if d.get('kind')!='qp':continue
        assert d['sha256'] in paths
        for p in d['pages']:
            t=normalise(p['text'])
            pages.append({'source_path':d['path'],'source_sha256':d['sha256'],'aliases':paths[d['sha256']],
              'pdf_page':p['pdf_page'],'text':t,'p5':phrases(t,5),'p8':phrases(t,8),'values':values(t)})
    df5=Counter(x for p in pages for x in p['p5']);df8=Counter(x for p in pages for x in p['p8']);dfv=Counter(x for p in pages for x in p['values'])
    results=[]
    for q in json.loads((A/'question-analysis.json').read_text())['questions']:
        t=normalise(' '.join(p['source_segment']for p in q['parts']))
        q5=phrases(t,5);q8=phrases(t,8);qv=values(t);candidates=[]
        for p in pages:
            r5=sorted(x for x in q5&p['p5']if df5[x]<=6 and content_count(x)>=3)
            r8=sorted(x for x in q8&p['p8']if df8[x]<=12 and content_count(x)>=4)
            common=sorted(qv&p['values'])
            rare_values=[x for x in common if dfv[x]<=100]
            if r8 or (r5 and len(common)>=2 and rare_values):
                cid=q['source_key']+'::'+p['source_sha256'][:12]+':'+str(p['pdf_page'])
                candidates.append({k:p[k]for k in ('source_path','source_sha256','aliases','pdf_page')}|{
                   'candidate_id':cid,'rare_five_word_phrases':r5,'rare_eight_word_phrases':r8,
                   'shared_values':common,'shared_rare_values':rare_values,'disposition':'unread','reason':'Lexical/value lead only; source images not yet read for this candidate.'})
        results.append({'source_key':q['source_key'],'pages_compared':len(pages),'candidates':candidates})
    write(A/'provenance-full-screen-r5.json',{
      'method':'Compare each of119 NSSCAS question texts with EVERY page including covers/blanks of all202 distinct local9709 QP content hashes2015–2025 (P1/P2 and locally indexed P3). Duplicate paths recorded as aliases. Unicode normalisation, punctuation/glyph-name removal and word-only5/8grams; numeric values separately. This is discovery, not mathematical verification.',
      'threshold':'At least one shared8-word phrase occurring on<=12 corpus pages with>=4 content words (STOP list in tool), OR a shared5-word phrase occurring on<=6 corpus pages with>=3 content words AND>=2 shared nontrivial numeric values of which>=1 occurs on<=100 corpus pages. Values are3..9,multi-digit or decimals. These content/value guards exclude boilerplate and ubiquitous tariff/page digits. No top-N truncation. Covers/blanks still compared. A preliminary unguarded screen yielded858 leads, not858 reads; below-threshold leads remain unread.',
      'limitations':'Extraction can miss visual/mathematical matches. Phrases discard single letters and may join across maths. Value tokens include question numbers: visual confirmation is mandatory. No detected match never proves originality. Frozen R5 measured recall was16/31 confirmed pairs; annotate_provenance_screen_r5.py recomputes current confirmed-register recall after the screen.',
      'question_count':len(results),'unique_qp_documents':len(paths),'qp_paths':sum(map(len,paths.values())),
      'pages_compared_per_question':len(pages),'total_comparisons':len(results)*len(pages),
      'candidates_above_threshold':sum(len(x['candidates'])for x in results),'results':results})
    print(len(pages),'pages;',sum(len(x['candidates'])for x in results),'candidates;',sum(bool(x['candidates'])for x in results),'questions with leads')
if __name__=='__main__':build()
