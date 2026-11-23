"""8227 syllabus/level/assessment evidence. MF9 never establishes content scope."""
import collections
import json
import re
from pypdf import PdfReader
from analysis_sources import ROOT, WB, A, clean, digest, write
from analysis_inputs import OBJECTIVES

SYLLABUS = 'Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf'


def oid(short):
    m,t,o=short.split('.')
    return f'8227:2020:{m}:{t}:O{int(o):02d}'


QUALIFIERS = [
 ('LIMIT01','M1.T2.1','Greatest binomial term and coefficient properties are not required; binomial coefficient and factorial notation are required.'),
 ('LIMIT02','M1.T6.6','General trigonometric solution forms are not included.'),
 ('LIMIT03','M1.T8.1','Differentiation from first principles is not required.'),
 ('LIMIT04','M1.T8.2','Product and quotient rules are not required in Mathematics 1; they are required in Mathematics 2.'),
 ('LIMIT05','M2.T1.3','Polynomial dividend degree at most four; divisor linear or quadratic.'),
 ('LIMIT06','M2.T2.1','Change of logarithm base is excluded.'),
 ('LIMIT07','M2.T5.1','General integration by substitution is not required.'),
 ('LIMIT08','M2.T6.4','Formal convergence conditions are excluded; failure to converge must be understood.'),
 ('QUAL01','M2.T1.2','The specified modulus coefficients a, b and c are integers; grade descriptions additionally calibrate a|x+b|+c.'),
 ('QUAL02','M1.T2.1','Binomial exponent n is a positive integer; no rational-power infinite series scope.'),
 ('QUAL03','M1.T6.6','n is a small integer or simple fraction; equations are the specified sin(nx), cos(nx), tan(nx) forms or easily reducible to them; finite specified intervals.'),
 ('QUAL04','M1.T9.3',r'Only simple improper integrals; examples $\int_0^1x^{-1/2}dx$ and $\int_1^\infty x^{-2}dx$.'),
 ('QUAL05','M1.T9.1','Powers (ax+b)^n allow any rational n except -1; the logarithmic reciprocal-linear case belongs to Mathematics 2.'),
 ('QUAL06','M1.T9.4','Volumes of revolution are about one of the coordinate axes; arbitrary displaced or oblique axes are not prescribed.'),
 ('QUAL07','M1.T3.2','Identify domain and range in simple cases; grade descriptions calibrate more complex branches without adding objectives.'),
 ('QUAL08','M1.T3.3','Find an inverse of a one-one function in simple cases; retained branch restriction is essential.'),
 ('QUAL09','M1.T4.2','Line tangency corresponds to a repeated root in simple cases. Not every tangency task is a quadratic-discriminant task.'),
 ('QUAL10','M1.T8.2','The exponent in the power derivative may be any rational number.'),
 ('QUAL11','M2.T5.4','Use sketch graphs in simple cases to justify trapezium bias; do not impose formal second-derivative tests as the only method.'),
]


def build_curriculum():
    pages=[p.extract_text() for p in PdfReader(ROOT/SYLLABUS).pages]
    source_hash=digest(ROOT/SYLLABUS)
    author=json.loads((WB/'tools/syllabus_author_transcriptions.json').read_text())
    assert author['source_sha256']==source_hash
    objectives=[]
    for row in author['objectives']:
        raw=pages[row['pdf_page']-1]
        # The quote is a separately frozen author input, not sliced from raw here.
        assert row['verbatim_extracted_quote'] in raw,('independent quote check',row['objective_id'])
        assert row['normalized_math_text'] and row['visual_check']['status']=='author-checked-against-rendered-page'
        source={'document':SYLLABUS,'sha256':source_hash,'pdf_page':row['pdf_page'],
                'printed_page':row['printed_page'],'verbatim_extracted_quote':row['verbatim_extracted_quote']}
        objectives.append({'objective_id':row['objective_id'],'topic_id':row['objective_id'].rsplit(':O',1)[0],
                           'source_kind':'syllabus','source':source,'syllabus_text':row['verbatim_extracted_quote'],
                           'normalized_math_text':row['normalized_math_text'],'normalization_review':row['visual_check'],
                           'screen':'in-scope','review_status':'r1 raw transcription accepted; r2 normalization awaiting independent re-review'})
    demands=[];counter=collections.Counter()
    for line in OBJECTIVES.strip().splitlines():
        if re.match(r'M[12]\.T\d+\|',line):
            topic,page,title=line.split('|');continue
        _, actions=line.split('|');counter[topic]+=1
        objective=oid(f'{topic}.{counter[topic]}')
        obj=next(x for x in objectives if x['objective_id']==objective);obj['topic_title']=title
        for n, action in enumerate(actions.split('/'),1):
            demands.append({'demand_id':f'{objective}:D{n:02d}','objective_id':objective,
                            'learner_action':action,'source_kind':'judgement','source':obj['source'],
                            'screen':'in-scope','basis':'Author decomposition of official bullet; not a board demand identifier',
                            'review_status':'round-2 author mapping; re-review pending'})
    assert len(objectives)==60 and len(demands)==138
    next(d for d in demands if d['demand_id']=='8227:2020:M2:T4:O03:D03')['learner_action']='Use an implicit or parametric derivative in a geometric demand'

    # The original D03 conflated segment and arbitrary compound regions, hiding
    # the segment gap. Keep its stable ID and make the named segment demand exact.
    next(d for d in demands if d['demand_id']=='8227:2020:M1:T5:O02:D03').update(
        learner_action='Find circular segment area',
        revision_note='R2 narrows original segment-or-compound wording; compound sector sums remain D01/D02 plus model construction. No new objective.')
    for d in demands:
        if d['demand_id']=='8227:2020:M1:T8:O04:D02':
            d['required_facets']=['maximum','minimum','stationary inflexion']
            d['facet_gap_note']='Observed maximum/minimum parts do not establish the inflexion branch.'
    limits=[]
    for code, short, rule in QUALIFIERS:
        obj=next(x for x in objectives if x['objective_id']==oid(short))
        limits.append({'limit_id':'8227:'+code,'objective_id':obj['objective_id'],
                       'demand_ids':[d['demand_id'] for d in demands if d['objective_id']==obj['objective_id']],
                       'normalized_rule':rule,'source':obj['source'],'source_kind':'syllabus-normalized'})
    write(WB.parent/'curriculum/objective_registry.json',{'schema_version':'workbench-analysis-8227-r2','source_sha256':source_hash,'objectives':objectives})
    write(WB.parent/'curriculum/syllabus-exclusions.json',{'limits':limits,
          'prior_knowledge':{'role':'prerequisite or explicitly assessed prior knowledge; never automatic AS-objective coverage',
                            'pdf_pages':[8,14],'verbatim_quote':'Knowledge of the content of NSSCO Mathematics is prescribed, and learners may be required to demonstrate such knowledge in answering questions.'}})
    write(A/'demand-registry.json',{'schema_version':'workbench-analysis-8227-r2','demands':demands,
          'supplementary_demands':[{'demand_id':'8227:2020:ABILITY:08:MODEL','learner_action':'Construct or establish a mathematical model from geometric/contextual constraints',
                                    'source_kind':'judgement linked to syllabus assessment ability 8','source':{'path':SYLLABUS,'pdf_page':17},
                                    'scope':'cross-cutting ability; not one of 138 specific-objective demands; no calculus coverage'},
                                   *[{'demand_id':'8227:PRIOR:NSSCO:'+name,'scope':'NSSCO prior technique; not AS objective coverage'} for name in
                                     ['quadratic','mensuration','similar-triangles','right-triangle-trig','coordinate-geometry','simultaneous-equations','circle-geometry']]]})
    evidence={'document_path':SYLLABUS,'sha256':source_hash,'extraction':'pypdf; raw mathematical text retained beside independently transcribed normalization',
              'pages':[{'pdf_page':i,'printed_page':i-3 if i>=4 else None,'text':p} for i,p in enumerate(pages,1)],
              'MF9':{'pdf_pages':list(range(25,31)),'role':'notation and formula support only; not content scope',
                     'out_of_scope_examples':['rational-power binomial series','integration by parts','inverse-tangent derivative','integral of 1/(x^2+a^2)']}}
    write(A/'syllabus-page-evidence.json',evidence)
    build_grade_descriptors(pages,objectives,demands)
    return objectives,demands


GRADE_LINKS = {
 'a': ['M2.T1.4 M1.T1.3 M1.T1.4 M1.T1.5','M1.T2.1 M1.T2.3','M1.T3.2 M1.T3.3 M1.T3.4 M1.T3.5',
       'M1.T4.1','M1.T5.2','M1.T6.2 M1.T6.5 M1.T6.6 M1.T5.2','M1.T7.1 M1.T7.4 M1.T7.5',
       'M1.T8.2 M1.T8.3 M1.T8.4','M1.T9.1 M2.T5.1 M2.T5.2','M1.T9.2 M1.T9.4 M2.T5.4',
       'M2.T1.1 M2.T1.2 M2.T1.3 M2.T1.4','M2.T2.1 M2.T2.2 M2.T2.3 M2.T2.4','M2.T3.1 M2.T3.2',
       'M2.T4.1 M2.T4.2 M2.T4.3','M2.T6.1 M2.T6.3'],
 'c': ['M1.T1.1 M1.T1.2 M1.T1.3 M1.T1.5 M1.T1.6','M1.T2.1 M1.T2.3 M1.T2.4 M1.T2.5',
       'M1.T3.2 M1.T3.3 M1.T3.4 M1.T3.5','M1.T4.2','M1.T5.2','M1.T6.1 M1.T6.2 M1.T6.3 M1.T6.5 M1.T6.6',
       'M1.T7.2 M1.T7.3 M1.T7.5','M1.T8.2 M1.T8.3 M1.T8.4','M1.T9.1 M1.T9.2 M1.T9.4',
       'M2.T1.1 M2.T1.2 M2.T1.4','M2.T2.1 M2.T2.2 M2.T2.3','M2.T3.1 M2.T3.2','M2.T4.1 M2.T4.2',
       'M2.T5.2','M2.T5.1 M2.T5.2 M2.T5.4','M2.T6.1 M2.T6.2 M2.T6.3'],
 'e': ['M1.T1.1 M1.T1.2','M1.T2.1 M1.T2.2 M1.T2.3 M1.T2.4','M1.T3.1 M1.T3.3','M1.T4.1 M1.T4.2',
       'M1.T5.1','M1.T6.1 M1.T6.4','M1.T7.1 M1.T7.3','M1.T8.1 M1.T8.3','M1.T9.1 M1.T9.2 M1.T9.4',
       'M2.T1.1 M2.T1.4','M2.T2.1 M2.T2.2 M2.T2.3','M2.T3.1 M2.T3.2','M2.T4.1','M2.T5.1 M2.T5.3','M2.T6.4']}


def build_grade_descriptors(pages, objectives, demands):
    grade=None;groups=collections.defaultdict(list)
    for n in range(19,25):
        # This PDF's plain-text reading order emits the footer before the body.
        text=pages[n-1].split('NSSCAS Mathematics syllabus, NIED 2020',1)[-1]
        # Remove only the final printed page number, retaining the paragraph text.
        text=re.sub(r'\n\s*\d+\s*$', '', text)
        marker=re.search(r'At Grade\s+([ace])\s+the learner is expected to:',text)
        if n==19:text=text[marker.end():];grade='a';marker=None
        chunks=re.split(r'(?=At Grade\s+[ace]\s+the learner is expected to:)',text)
        for chunk in chunks:
            m=re.match(r'At Grade\s+([ace])\s+the learner is expected to:',chunk)
            if m:grade=m[1];chunk=chunk[m.end():]
            bullets=chunk.split('\uf0b7')
            if bullets[0].strip() and groups[grade]:
                groups[grade][-1]['fragments'].append({'pdf_page':n,'text':bullets[0].strip()})
            for bullet in bullets[1:]:
                groups[grade].append({'fragments':[{'pdf_page':n,'text':bullet.strip()}]})
    rows=[]
    for grade in ['a','c','e']:
        assert len(groups[grade])==len(GRADE_LINKS[grade]),(grade,len(groups[grade]))
        for i,(record,links) in enumerate(zip(groups[grade],GRADE_LINKS[grade]),1):
            oids=[oid(x) for x in links.split()]
            record.update(descriptor_id=f'8227:GRADE:{grade.upper()}:{i:02d}',grade=grade,source_kind='syllabus',
                          objective_ids=oids,demand_ids=[d['demand_id'] for d in demands if d['objective_id'] in oids],
                          linkage_role='calibration evidence; not a new objective or claim that every linked demand is restated',
                          source_path=SYLLABUS,source_sha256=digest(ROOT/SYLLABUS),
                          visual_check={'by':'Codex','date':'2026-11-16','status':'author-read-on-rendered-pages; independent re-review pending'},
                          normalized_mathematics=[o['normalized_math_text'] for o in objectives if o['objective_id'] in oids])
            if grade=='a' and i==11:record['additional_grade_form']=r'$y=a|x+b|+c$; source has the same extra-equals-sign typo in the modulus relation.'
            if grade=='a' and i==12:record['additional_grade_form']=r'$y=e^{ax+b}+c$ and $y=\ln(ax+b)+c$; logarithmic inequalities.'
            if grade=='c' and i==10:record['additional_grade_form']=r'$y=a|x+b|$ or $y=a|x|+b$.'
            if grade=='c' and i==11:record['additional_grade_form']=r'$y=e^{ax+b}$ and $y=\ln(ax)$.'
            rows.append(record)
    write(WB.parent/'curriculum/grade-descriptions.json',{
      'source_path':SYLLABUS,'source_sha256':digest(ROOT/SYLLABUS),'descriptors':rows,
      'interpretation':'Official grade calibration interpreted with specific content; descriptions do not define additional content. Inheritance a includes c/e does not invent an a statement for every topic.',
      'owner_decision':'Vitalis 2026-11-16 decision 4: easiest branches at e/c; hardest no further than a',
      'limitations':'Raw extracted quotations preserve formula ordering limits; normalized mathematics and additional grade forms are separate author transcriptions. Demand links indicate calibration relevance, not a new assessment-coverage assertion.'})


def build_assessment_conditions(questions):
    rows=[]
    common=['sphere/cone/pyramid mensuration; arc length and sector area',
            'quadratic formula; AP/GP terms and sums; positive-integer and rational binomial forms',
            'basic, reciprocal, compound- and double-angle trigonometric identities; inverse principal ranges',
            'power, log, exponential, sin, cos, tan, sec derivatives; product, quotient and parametric differentiation',
            'power, reciprocal, exponential, sin, cos and sec-squared antiderivatives; integration by parts',
            'vector scalar product and angle; trapezium rule']
    removed=['cosec derivative','cot derivative','arctan derivative',
             'integrals of 1/(x^2+a^2), 1/(x^2-a^2), 1/(a^2-x^2)',
             "integral of f'/f",'operations/notation page: Sigma, square root, modulus, factorial and binomial notation']
    for year in range(2021,2026):
        records=[]
        for component in [1,2]:
            q=next(q for q in questions if q['year']==year and q['paper']==component)
            source=q['question_source_path'];pdf=PdfReader(ROOT/source)
            texts=[p.extract_text() for p in pdf.pages]
            starts=[i for i,t in enumerate(texts,1) if re.search(r'FORMULAE\s+AND\s+NOTATIONS',t)]
            assert len(starts)==1,(year,component,starts)
            start=starts[0];nums=list(range(start,start+(4 if year<=2022 else 3)))
            cover=texts[0]
            assert 'three significant figures' in clean(cover),(year,component)
            sheet=' '.join(texts[n-1] for n in nums)
            assert 'Trapezium' in sheet and 'Principal values' in sheet
            records.append({'paper':str(component),'source_path':source,'source_sha256':digest(ROOT/source),
                'cover_pdf_page':1,'cover_verbatim_text':cover,'formula_sheet_pdf_pages':nums,
                'formula_sheet_pages':[{'pdf_page':n,'verbatim_extracted_text':texts[n-1]} for n in nums],
                'contents':common+(removed if year<=2022 else []),
                'removed_relative_to_2022':removed if year>=2023 else [],
                'calculator':'non-programmable',
                'precision':{'nonexact_numeric':'3 significant figures unless specified otherwise',
                             'degrees':'1 decimal place unless specified otherwise',
                             'radians':'3 significant figures explicitly on cover' if year<=2024 else 'general non-exact 3 significant figure instruction; no separately worded radian clause',
                             'pi':'calculator value or 3.142' if year==2021 else 'calculator value'},
                'working_instruction':'2025 adds explicit no credit for unsupported calculator answers; do not turn this into a blanket answer-only penalty for every criterion' if year==2025 else 'Show working if needed/as indicated; official part awards determine method credit',
                'scope_note':'A supplied formula (including rational-power series or integration by parts) does not add content scope; 8227 specific objectives and LIMIT01-08 control.'})
        rows.append({'year':year,'papers':records})
    parts=[p for q in questions if q['paper']==2 for p in q['parts']]
    m1=[p for p in parts if p['primary_objective_id'] and ':M1:' in p['primary_objective_id']]
    direct=[p for p in parts if any(':M1:' in x for x in p['directly_assessed_objective_ids'])]
    p1parts=[p for q in questions if q['paper']==1 for p in q['parts']]
    p1m2=[p for p in p1parts if p['primary_objective_id'] and ':M2:' in p['primary_objective_id']]
    p1direct=[p for p in p1parts if any(':M2:' in x for x in p['directly_assessed_objective_ids'])]
    write(WB.parent/'curriculum/assessment-conditions.json',{
        'schema_version':'workbench-analysis-8227-r2','years':rows,
        'cross_paper_theme':{'syllabus_pdf_page':17,'verbatim_quote':'can be assessed in any question in Paper 1 and 2',
                            'rule':'Theme is not paper: Mathematics 1 content is directly examined on Paper 2.',
                            'paper2_primary_m1_parts':len(m1),'paper2_primary_m1_marks':sum(p['printed_marks'] for p in m1),
                            'paper1_primary_m2_parts':len(p1m2),'paper1_primary_m2_marks':sum(p['printed_marks'] for p in p1m2),
                            'paper1_any_direct_m2_parts':len(p1direct),'paper1_m2_part_links':[p['part_id'] for p in p1direct],
                            'paper2_any_direct_m1_parts':len(direct),'part_links':[p['part_id'] for p in direct],
                            'mark_limit':'Part totals are not objective-specific mark allocations; do not double-count secondary objective marks.'}})
