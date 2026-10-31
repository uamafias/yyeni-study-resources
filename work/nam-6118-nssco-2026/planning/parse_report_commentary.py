"""Preserve native report commentary blocks with conservative question links.

Memo tables and keys are separate evidence. Labels below are triage categories;
the curated misconception register is independently selected from these blocks.
"""
from pathlib import Path
import collections,json,re

WORK=Path(__file__).resolve().parents[1]


def norm(t):return re.sub(r'\s+',' ',t).strip()


def parent_ref(ref):
    return ref.split('/')[0].replace('(i-iii)','')


def main():
    inv=json.loads((WORK/'curriculum/source-inventory.json').read_text())
    demands=json.loads((WORK/'assessment-evidence/assessment_evidence.json').read_text())['records']
    all_blocks=[];keys=[]
    for source in inv['entries']:
        if source['kind']!='combined_examiner_report':continue
        year=source['year'];text=(WORK/f'planning/extracted/{year}-report.layout.txt').read_text()
        pages={int(n):body for n,body in re.findall(r'=== SOURCE PDF PAGE (\d+) ===\n(.*?)(?=\n=== SOURCE PDF PAGE|\Z)',text,re.S)}
        paper=None;q=None;letter=None;roman=None;mode='ignore';buffer=[];buffer_pages=[]
        def flush():
            nonlocal buffer,buffer_pages
            body='\n'.join(buffer).strip();buffer=[]
            loc=sorted(set(buffer_pages));buffer_pages=[]
            if not body or len(re.findall(r'[A-Za-z]{2,}',body))<3:return
            if not re.search(r'candidate|learner|student|teacher|answer|question|experiment|graph|marks?|poor|well|fair|moderate|correct|incorrect|MP\d|M[pP]\d|[Ss]hould',body):return
            ref=(str(q)+(f'({letter})' if letter else '')+(f'({roman})' if roman else '')) if q else None
            repaired=None
            if year==2020 and paper==2 and q==5 and 'rainbow' in body.lower():repaired='5(c)'
            if year==2022 and paper==2 and ref=='9(d)':repaired='9(c)(ii)'
            if year==2022 and paper==3 and ref=='2(c)':repaired='2(b)(ii)'
            if repaired:ref=repaired
            eligible=[d for d in demands if d['year']==year and int(d['paper_id'])==paper]
            exact=[d for d in eligible if parent_ref(d['question_ref'])==ref] if ref else []
            children=[d for d in eligible if ref and parent_ref(d['question_ref']).startswith(ref+'(')]
            grouped=[d for d in eligible if '(i-iii)' in d['question_ref'] and ref and ref.startswith(parent_ref(d['question_ref'])+'(')]
            matches=exact or children or grouped
            if not matches and ref and '(' not in ref:matches=[d for d in eligible if re.match(r'\d+',d['question_ref'])[0]==ref]
            lower=body.lower()
            labels=[]
            if re.search(r'confus|instead of|interchang|swapp|swop|swoop|misconception|wrongly|misunderst',lower):labels.append('possible_misconception_or_confusion')
            if re.search(r'omit|failed|without|not mention|left out|missing|could not|unable',lower):labels.append('omission_or_skill_gap')
            if re.search(r'command|instruct|read the question|misinterpret|did not answer|rather than|asked',lower):labels.append('command_word_or_focus_miss')
            if re.search(r'insufficient|not sufficient|not enough|vague|general|clear comparison|clear justification|not specify',lower):labels.append('shallow_or_unspecified_response')
            if not labels:labels=['performance_or_teaching_observation']
            all_blocks.append(dict(finding_id=f'ER-{year}-{len([b for b in all_blocks if b["year"]==year])+1:03d}',
                                   year=year,paper_id=str(paper),question_ref=ref,
                                   source_id=f'6118-{year}-report',source_path=source['path'],pdf_pages=loc,
                                   internal_verbatim=body,evidence_kind='commentary',
                                   triage_categories=labels,
                                   classification_limit='Triage flags do not certify a scientific misconception. Only the curated misconception register can drive misconception slots.',
                                   linked_evidence_ids=[d['evidence_id'] for d in matches],
                                   objective_ids=sorted({oid for d in matches for oid in d['objective_ids']}),
                                   link_scope='exact_source_reference' if exact else ('parent_reference' if children else ('grouped_question_part' if grouped else ('whole_question' if matches else 'general_or_unmatched'))),
                                   reference_repair='manual_context_correction_of_report_label' if repaired else None))
        headers={h['pdf_page']:h['paper'] for h in source['paper_headers']}
        for page,body in sorted(pages.items()):
            if page in headers:
                flush();paper=headers[page];q=None;letter=None;roman=None;mode='key' if paper==1 else 'commentary'
                if paper==1:
                    keypart=re.split(r'(?i)general comments',body)[0]
                    pairs=re.findall(r'\b([1-9]|[1-3][0-9]|40)\s+([A-D*])(?=\s|$)',keypart)
                    found={int(n):answer for n,answer in pairs}
                    assert set(found)==set(range(1,41)),(year,found)
                    keys.append(dict(year=year,source_path=source['path'],pdf_page=page,
                                     evidence_kind='key',answers={str(n):found[n] for n in range(1,41)},
                                     limit='Published key, not a scientific correctness endorsement. Asterisk in 2024 question 9 denotes compensation.'))
            for raw in body.splitlines():
                line=raw.rstrip()
                if re.match(r'^\s*NSSCO Examiners Report',line) or re.match(r'^\s*\d+\s*$',line):continue
                if re.match(r'^\s*(?:GENERAL COMMENTS|General comments|POSITIVE SUGGEST|[\d. ]*POSITIVE SUGGEST)',line,re.I):
                    flush();q=None;letter=None;roman=None;mode='commentary';continue
                if re.match(r'^\s*(?:COMMENTS ON|Comments on)',line):flush();q=None;letter=None;roman=None;mode='commentary';continue
                heading=re.match(r'^\s*Question\s+(\d+)\s*$',line,re.I)
                if heading:
                    flush();q=int(heading[1]);letter=None;roman=None;mode='commentary';continue
                if paper==1 and mode=='commentary':
                    heading=re.match(r'^\s{0,3}([1-9]|[1-3][0-9]|40)[. ]+([A-Za-z].*)',line)
                    if heading:
                        flush();q=int(heading[1]);letter=None;roman=None
                if re.match(r'^\s*(?:Mark [Ss]cheme|Expected answers|Question\s+Answer\s+Additional)',line):
                    flush();mode='memo';continue
                numeric=re.match(r'^\s{0,3}([1-9])\s+(?:\(([a-h])\)|(?:Poorly|Well|Fairly))',line)
                if numeric and paper==3 and re.search(r'answered|question|Poorly|Well|Fairly',line,re.I):
                    flush();q=int(numeric[1]);letter=numeric[2];roman=None;mode='commentary'
                if paper in (2,3) and mode=='commentary' and re.match(r'^\s*\d+\s+\([a-h]\)\s+',line):
                    # A labelled memo table without a repeated table heading.
                    if not re.search(r'answered|question',line,re.I):
                        flush();mode='memo';continue
                if mode!='commentary' or paper is None:continue
                # 2020 practical section uses '4 (a)' and '5 Poorly answered'.
                if numeric and paper==3:
                    flush();q=int(numeric[1]);letter=numeric[2];roman=None;mode='commentary'
                leading=re.match(r'^\s{0,24}(?:\d+\s*)?\(([a-h])\)\s*(?:\((i{1,3}|iv|v|vi|vii|viii|ix|x)\))?',line)
                rom=re.match(r'^\s{0,24}\((i{1,3}|iv|v|vi|vii|viii|ix|x)\)',line)
                if leading:
                    flush();letter=leading[1];roman=leading[2]
                elif rom:
                    flush();roman=rom[1]
                if not line.strip():flush();continue
                if line.strip() in ('PHYSICS','6118','Paper 1','Paper 2','Paper 3','Alternative to practical'):continue
                buffer.append(line);buffer_pages.append(page)
        flush()
    (WORK/'assessment-evidence/report-commentary.json').write_text(json.dumps({'scope':'Native-text commentary blocks; keys/memo tables kept separate. Source references linked to manually mapped question demands.','records':all_blocks},indent=2,ensure_ascii=False)+'\n')
    (WORK/'assessment-evidence/published-mc-keys.json').write_text(json.dumps({'records':keys},indent=2)+'\n')
    print('Commentary blocks:',len(all_blocks),'linked:',sum(bool(b['linked_evidence_ids']) for b in all_blocks),'keys:',len(keys))
    for year in range(2020,2026):
        b=[r for r in all_blocks if r['year']==year]
        print(year,len(b),'unmatched specific',[(r['finding_id'],r['paper_id'],r['question_ref'],norm(r['internal_verbatim'])[:65]) for r in b if r['question_ref'] and not r['linked_evidence_ids']])


if __name__=='__main__':main()
