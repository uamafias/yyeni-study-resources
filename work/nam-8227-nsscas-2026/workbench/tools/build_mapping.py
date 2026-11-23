"""Subject-local mapping assembly; direct annotations never come from families."""
import collections
import json
import re
from pypdf import PdfReader
from analysis_sources import A, ROOT, WB, clean, digest, paper_scan, reference_label, write
from analysis_inputs import QUESTIONS
from repair_inputs import (part_annotations, HOLD_QUESTIONS, HOLD_PARTS, SKETCH_PARTS,
                           SKETCH_DEPENDENT, MAPPING_NOTES, DEPENDENCY_OVERRIDES,
                           PATTERN_OVERRIDES)

REPORT_SECTIONS = {2021:(231,236,242),2022:(301,307,316),2023:(320,330,339),
                   2024:(325,335,343),2025:(345,355,364)}


def scan_awards():
    results = {}
    scans = []
    for year, (lo, split, hi) in REPORT_SECTIONS.items():
        source = json.loads((A/'extracted'/f'report-{year}.json').read_text())
        assert digest(ROOT/source['source']) == source['sha256']
        pages = PdfReader(ROOT/source['source']).pages
        current = None
        for page in range(split, hi+1):
            text = pages[page-1].extract_text(extraction_mode='layout')
            headings = list(re.finditer(r'Question\s+(\d+)(?!\d)', text))
            chunks = [(current, text[:headings[0].start()] if headings else text)]
            for i, h in enumerate(headings):
                current = int(h[1])
                chunks.append((current, text[h.end():headings[i+1].start() if i+1<len(headings) else len(text)]))
            for question, chunk in chunks:
                if question is None:
                    continue
                awards = list(re.finditer(r'\b(?:D?[BMAE]|SC)\s*\d\b',chunk))
                if len(awards) < 2:
                    continue
                key = f'{year}-2-Q{question}'
                results.setdefault(key, []).append(page)
                scans.append({'question_key':key,'pdf_page':page,'award_token_count':len(awards),
                              'source_path':source['source'],'source_sha256':source['sha256'],
                              'has_follow_through':bool(re.search(r'F\s*\.\s*T(?:\s*\.)?',chunk,re.I)),
                              'text':chunk})
    return {k:sorted(set(v)) for k,v in results.items()}, scans


def label_from_segment(segment, previous, override_key):
    matches = re.findall(r'^\s*(?:\d+\s*)?\(([a-h]|i{1,3}|iv|v)\)\s*(?:\(([iv]+)\))?', segment, re.M)
    if not matches and override_key == '2021-1-Q12:c':
        assert 'Use(c)' in segment
        return 'c', {'reason':'PDF text layer concatenates examiner header and (c)',
                     'source_token':'Use(c)', 'kind':'label-extraction-override'}
    if not matches:
        return 'answer', None
    outer = previous.split('.')[0] if previous and previous != 'answer' else None
    result = None
    for letter, roman in matches:
        if len(letter)>1 or letter in ['i','v']:
            assert outer
            result = outer+'.'+letter
        else:
            outer = letter
            result = letter + ('.'+roman if roman else '')
    return result, None


def prerequisite_links(key, direct):
    out = []
    for did in direct:
        if ':PRIOR:' in did:
            out.append({'demand_id':did,'role':'directly-assessed-prior-knowledge',
                        'reason':'This part explicitly requires this prior technique, rather than differentiation.'})
    extra = {
      '2021-2-Q1:a':('simultaneous-equations','Solve the two remainder conditions for m and n; report PDF 237'),
      '2022-1-Q5:a':('simultaneous-equations','Recover first term and difference from two AP conditions'),
      '2022-2-Q4:a':('simultaneous-equations','Coupled factor/remainder conditions'),
      '2022-1-Q8:a':('mensuration','Wire length constrains the sector perimeter before eliminating theta'),
      '2021-1-Q7:a':('mensuration','Identify exposed straight edges and arc lengths of the compound plate'),
      '2021-1-Q7:b':('mensuration','Add major and minor sector areas'),
      '2023-1-Q6:b':('mensuration','Combine the sectors selected by the shaded boundary'),
      '2024-1-Q7:b':('mensuration','Common-tangent region is a trapezium less two sectors'),
      '2025-1-Q10:b':('mensuration','Compare circle area to sector area after R=3r'),
      '2025-2-Q3:answer':('right-triangle-trig','Recover an exact tangent from secant and the acute-angle restriction'),
    }
    if key in extra:
        name, reason = extra[key]
        out.append({'demand_id':'8227:PRIOR:NSSCO:'+name,'role':'supporting-prerequisite','reason':reason})
    # A substituted quadratic requires ordinary quadratic solving, but that
    # prerequisite does not earn another specific-objective coverage link.
    if any(':M1:T1:O04:' in d for d in direct):
        out.append({'demand_id':'8227:PRIOR:NSSCO:quadratic','role':'supporting-prerequisite',
                    'reason':'Solve the equation in the substituted variable before recovery and admissibility.'})
    return out


def build_questions(demands, negative_fixture=None):
    annotations = part_annotations()
    valid = {d['demand_id'] for d in demands}
    questions = []
    source_scans = {}
    paper_checks = []
    award_pages, award_scan = scan_awards()
    write(A/'award-source-scan.json', {'method':'scan report section headings and award-token density; full source sections retained',
                                     'questions':award_pages,'sections':award_scan})
    for year in range(2021,2026):
        for component in [1,2]:
            source, scanned = paper_scan(year,component)
            lines = [x.split('|') for x in QUESTIONS.strip().splitlines() if x.startswith(f'{year}-{component} ')]
            expected = [(r[0].replace(' ','-Q'),p.split(':')) for r in lines for p in r[3].split(';')]
            if negative_fixture=='tariff' and year==2021 and component==1:
                expected[0][1][2]=str(int(expected[0][1][2])+1)
            assert len(expected)==len(scanned), ('part census',year,component)
            assert [int(p[2]) for _,p in expected]==[s['marks'] for s in scanned],('ordered tariffs',year,component)
            assert sum(s['marks'] for s in scanned)==75
            i = 0
            for line in lines:
                qkey = line[0].replace(' ','-Q')
                qnum = int(line[0].split()[1])
                pages = list(map(int,line[1].split(',')))
                labels = []
                parts = []
                overrides = []
                for enc in line[3].split(';'):
                    label, legacy, mark = enc.split(':')
                    key=qkey+':'+label
                    scan=scanned[i]; i+=1
                    observed_label, override=label_from_segment(scan['segment'],labels[-1] if labels else None,key)
                    if negative_fixture=='label' and year==2021 and component==1 and i==1:
                        observed_label='b'
                    assert observed_label==label,('label alignment',key,observed_label)
                    assert scan['pdf_page'] in pages,('question-page alignment',key,scan['pdf_page'],pages)
                    if override:overrides.append({'part':label,**override})
                    labels.append(label)
                    direct=annotations[key]
                    assert direct and all(d in valid or d.startswith('8227:PRIOR:') or ':ABILITY:' in d for d in direct),key
                    objectives=list(dict.fromkeys(d.rsplit(':D',1)[0] for d in direct if d in valid))
                    hold=HOLD_PARTS.get(key) or HOLD_QUESTIONS.get(qkey)
                    legacy=PATTERN_OVERRIDES.get(key,legacy.split('+'))
                    part={'part_id':f'8227:EXAM:{year}:P{component}:Q{qnum}:{label}',
                          'source_key':key,'source_label':None if label=='answer' else label,
                          'paper_locator':{'path':source['source'],'sha256':source['sha256'],'question':qnum,
                                           'part':label,'question_pdf_pages':pages,'part_end_pdf_page':scan['pdf_page']},
                          'directly_assessed_objective_ids':objectives,'directly_assessed_demand_ids':direct,
                          'primary_objective_id':objectives[0] if objectives else None,
                          'other_directly_assessed_objective_ids':objectives[1:],
                          'assessment_ability_ids':['8227:2020:ABILITY:08'] if any(':ABILITY:' in x for x in direct) else [],
                          'prerequisite_demand_ids':prerequisite_links(key,direct),
                          'mapping_rationale':MAPPING_NOTES.get(key,'Direct actions annotated from this part, independently of family grouping; see source segment and demand labels.'),
                          'mapping_review_status':'round-2 author judgement; independent re-review pending',
                          'legacy_pattern_ids':['8227:PAT-'+f for f in legacy], 'pattern_ids':[],
                          'printed_marks':int(mark),'mark_source':'question-paper tariff; not criterion reconciliation',
                          'blooms_level':None,'bloom_status':'unclassified; criterion-linked recipe/branch review follows analysis',
                          'capability_hold':None,'capability_decision':'include under Vitalis decision 6, 2026-11-16; app change announced for 2026-11-17; no runtime test claimed',
                          'requires_sketch_response':key in SKETCH_PARTS,'requires_learner_sketch_reading':key in SKETCH_DEPENDENT,
                          'disposition':'hold' if hold else 'include','hold_ids':[hold] if hold else [],
                          'marking_excerpt_pdf_pages':award_pages.get(qkey,[]),
                          'marking_rule_status':'linked official excerpts; criterion reconciliation pending' if qkey in award_pages else 'no complete award schedule verified',
                          'source_segment':scan['segment'],'dependency_edges':[]}
                    parts.append(part);source_scans[key]=scan
                q={'question_id':f'8227:EXAM:{year}:P{component}:Q{qnum}', 'source_key':qkey,
                   'year':year,'paper':component,'question':qnum,'pdf_pages':pages,
                   'question_source_path':source['source'],'source_sha256':source['sha256'],
                   'pattern_summary':line[2], 'source_kind':'corpus','parts':parts,
                   'reported_question_total':sum(p['printed_marks'] for p in parts),
                   'dependencies':[],'extraction_overrides':overrides,
                   'marking_excerpt_pdf_pages':award_pages.get(qkey,[]),
                   'report_source':json.loads((A/'extracted'/f'report-{year}.json').read_text())['source'],
                   'source_hold':HOLD_QUESTIONS.get(qkey),'inspection':'round-2 author structural/label audit; independent re-review pending'}
                if qkey=='2021-1-Q6':q['pattern_summary']='External vector division AP=(3/2)AB and perpendicularity proof'
                add_dependencies(q, source_scans, award_scan)
                questions.append(q)
            paper_checks.append({'year':year,'paper':component,'full_ordered_tariffs_match':True,
                                 'labels_match':True,'marks':sum(s['marks'] for s in scanned),'parts':len(scanned)})
    assert len(questions)==119 and len(source_scans)==250
    write(A/'part-source-scan.json',{'method':'full ordered tariff and label alignment from actual PDFs; source segments retain text-layer limits','parts':source_scans})
    return questions,paper_checks


def add_dependencies(q, scans, awards):
    parts=q['parts'];labels=[p['source_label'] or 'answer' for p in parts]
    key=q['source_key']
    edges=[]
    for i,p in enumerate(parts):
        scan=scans[p['source_key']]
        if not scan['cue_hits'] or not i:
            continue
        explicit=re.findall(r'\bparts?\s*\(([a-z])\)',scan['segment'],re.I)
        sources=[x for x in explicit if x in labels[:i]]
        sketch_sources=[labels[n] for n,prior in enumerate(parts[:i]) if prior['requires_sketch_response']]
        if re.search(r'use\s+your\s+graphs',scan['segment'],re.I):sources+=sketch_sources
        elif re.search(r'use\s+your\s+(?:graph|sketch)',scan['segment'],re.I):sources+=sketch_sources[-1:]
        if not sources:sources=[labels[i-1]]
        for src in dict.fromkeys(sources):
            edges.append({'from_part':src,'to_part':labels[i],'type':'cue',
                          'cue':scan['cue_hits'],'derivation':'wording scan',
                          'source_path':q['question_source_path'],'pdf_page':scan['pdf_page']})
    for src,to,reason in DEPENDENCY_OVERRIDES.get(key,[]):
        assert src in labels and to in labels,(key,src,to)
        if not any(e['from_part']==src and e['to_part']==to and e['type']=='cue' for e in edges):
            edges.append({'from_part':src,'to_part':to,'type':'cue','cue':'given/reused result',
                          'derivation':'manual override','reason':reason,'source_path':q['question_source_path'],
                          'pdf_page':parts[labels.index(to)]['paper_locator']['part_end_pdf_page']})
    # These override the antecedent only. The existence and page of F.T. are
    # scanned from the actual report; no cue edge implies an F.T. mark.
    ft={
      '2024-2-Q4':[('a','b')],
      '2024-2-Q5':[('a','b'),('a','c')], '2024-2-Q9':[('a','b')],
      '2024-2-Q10':[('a','b')], '2024-2-Q11':[('b','c')],
    }
    for src,to in ft.get(key,[]):
        candidates=[x for x in awards if x['question_key']==key and x['has_follow_through']]
        assert candidates,('F.T. evidence missing',key)
        edges.append({'from_part':src,'to_part':to,'type':'follow-through',
                      'derivation':'F.T. scan with manually resolved table antecedent',
                      'source_path':q['report_source'],'pdf_pages':sorted({x['pdf_page'] for x in candidates}),
                      'reason':'Official award-table F.T.; not a general permission for other criteria.'})
    q['dependencies']=edges
    for p,label in zip(parts,labels):
        p['dependency_edges']=[e for e in edges if e['to_part']==label]
        p['cue_scan_disposition']={'hits':scans[p['source_key']]['cue_hits'],'status':'inter-part edges recorded' if p['dependency_edges'] else 'no cue'}
        if p['source_key'] in ['2022-1-Q12:a','2023-1-Q13:a']:
            p['cue_scan_disposition'].update(status='within-part cue; no preceding assessed part',
                reason='Establish the geometric relation then hence derive the area expression within this single part; no fabricated inter-part edge.',
                derivation='manual scan interpretation')
