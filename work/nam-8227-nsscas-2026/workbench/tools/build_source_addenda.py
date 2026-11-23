"""Index local source derivatives and scoped textbook/report findings for 8227.

OCR labels are discovery leads, not verified mathematical transcriptions.
"""
from pathlib import Path
import hashlib
import json
import re
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[4]
WB=Path(__file__).resolve().parents[1]
A=WB/'analysis'

def write(path,value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

register=json.loads((WB/'tools/source_holdings_inputs.json').read_text())
for i,year in enumerate([2022,2023,2024],18):
    p=ROOT/f'Question Banks/Namibian Examiner Reports/NSSCAS/{year}/NSSCAS_Examiners_Report_{year}.pdf'
    b=p.read_bytes(); r=PdfReader(p);d=json.loads((A/'extracted'/f'report-{year}.json').read_text())
    cover=r.pages[0].extract_text()
    assert str(year) in cover and 'NSSCAS' in cover
    record={'document_id':f'8227-SRC-{i:03d}','path':str(p.relative_to(ROOT)),
            'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'byte_kind':'pdf',
            'role':'combined-examiner-report','year':year,'page_count':len(r.pages),
            'source_location':'Third-party mirror (NANSO Erongo); DNEA cover verified; official-copy equivalence unverified; exact URL in harvest manifest',
            'acquisition_manifest':'_harvest/manifests/nsscas-8227-report-gaps-2026-11-15.csv',
            'section_heading_pdf_pages':[x['pdf_page'] for x in d['pages'] if '8227' in x['text'] and x['pdf_page']>10],
            'inspection':'cover and Mathematics heading pages verified; selected Mathematics commentary/award excerpts read; no whole-document content review'}
    register['records']=[x for x in register['records'] if x['document_id']!=record['document_id']]+[record]
book=next(x for x in register['records'] if x['document_id']=='8227-SRC-017')
book.update(isbn='9789991696645',isbn_verification='Back cover, PDF p663, visually read',
            extraction_limitation='Original text layer only scanner labels. Complete local Apple Vision OCR derivative exists; mathematics unverified except explicitly inspected samples.',
            ocr_derivative='work/nam-8227-nsscas-2026/workbench/analysis/ocr/ymxc',
            ocr_pages_completed=663,
            storage_basis='Vitalis owner decision 5, 2026-11-16: shared-repository commercial PDFs and OCR accepted for this project; no general public reproduction licence inferred',
            filing_status='Root PDF refiling deferred; source bytes and paths unchanged in repair round 2')
for record in register['records']:
    if record['document_id'] in ['8227-SRC-015','8227-SRC-017']:
        record['storage_basis']='Vitalis owner decision 5, 2026-11-16 accepts shared-repository commercial PDFs and OCR for this project; no public reproduction licence inferred'
write(A/'source-holdings.json',register)

ocr=A/'ocr/ymxc'
meta=json.loads((ocr/'metadata.json').read_text())
assert meta['source_sha256']==book['sha256']
leads=[];manifest={};empty=[]
for n in range(1,664):
    p=ocr/f'page-{n:04d}.json';d=json.loads(p.read_text());assert d['source_sha256']==book['sha256'] and d['pdf_page']==n
    manifest[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    if not d['lines']:empty.append(n)
    labels=[x['text'] for x in d['lines'] if re.search(r'(?:Example\s*\d|Try Now\s*\d|Revision Exercise|Exam.Style Questions|^\d+\.\d+\s)',x['text'],re.I)]
    if labels:leads.append({'pdf_page':n,'ocr_heading_leads':labels,'verification':'OCR-discovered only; inspect page image and item numbering'})
write(A/'textbook-exercise-index.json',{'document_id':book['document_id'],'source_sha256':book['sha256'],
    'index_scope':'All 663 scan pages OCR-processed; index labels do not certify exercise completeness or correctness.',
    'page_records':leads})
write(A/'ocr-validation.json',{'source_sha256':book['sha256'],'completed_pages':663,'pages_with_no_lines':empty,
    'engine':meta['engine'],'revision':meta['revision'],
    'page_record_hashes':manifest,'visual_qc_pages':[1,5,8,50,54,109,150,155,235,250,268,326,378,409,450,484,530,550,560,663],
    'qc_limit':'Only explicitly sampled images visually inspected. Equations in OCR contain substantial errors; do not calculate answers from OCR alone.',
    'external_transmission':False,'original_pdf_modified':False})

# Exact sample locators are visually read. Classification/reuse are analyst judgements.
SAMPLES=[
('TB01',50,39,'1.7 Exam-Style Questions, Revision Exercise 1, Q1-2','Quadratic inequality, vertex form and parameterised line intersection','M1:T1:O01 M1:T1:O02 M1:T1:O06','01 02 06','textbook-derived; compare structure with papers, not new recipes merely for different values'),
('TB02',54,43,'2.1 Example 1 and Try Now 1; Example 2 and Try Now 2 Q1-2','Recognise AP/GP, then determine parameters from overlapping progressions','M1:T2:O02 M1:T2:O03','08 09 10 13','numeric recognition is a candidate supporting branch; overlapping AP/GP decisions differ from ordinary term substitution'),
('TB03',109,98,'3.1 Example 1(a-c), Try Now 1(a)','Function recognition from graph, table and ordered pairs','M1:T3:O01','','include as supporting-practice analysis; classify representation and decision separately from inverse calculation; no automatic standalone drill approval'),
('TB04',155,143,'4.1 Examples 1-2 and Try Now 1','Degree/radian conversion with exact or rounded form','M1:T5:O01','','syllabus/textbook-derived standalone candidate; larger sector questions do not prove standalone conversion coverage'),
('TB05',235,223,'5.1 Try Now 1(a-b), Example 2, Try Now 2 Q1-2','Read coordinates of vertices from 3D cube or prism with varying origin','M1:T7:O01','24','diagram interpretation differs from calculation using supplied coordinates; shared renderer may support related branches'),
('TB06',250,238,'5.1 Example 11 and Try Now 11','Construct unit vector after connected position/displacement steps','M1:T7:O03','24 25','OCR item label visually checked; direct unit-vector demand stays distinct from magnitude-only coverage'),
('TB07',268,256,'Chapter 6 investigation Tasks (a-g), Question 1','Secant approaching tangent through interactive graph','M1:T8:O01','','supporting investigation, not required differentiation-from-first-principles technique; include as supporting-practice analysis under owner decision 6; moving-point interaction requirements remain untested'),
('TB08',326,314,'Chapter 7 Example 3(a-c), Try Now 3(a-f)','Integrate constants, reciprocal powers and fractional powers','M1:T9:O01','','Standard antiderivative component only: this page has no initial condition. Not evidence for an initial-condition reconstruction branch.'),
('TB09',378,366,'8.1 Example 2 and Try Now 2 Q1-2','Modulus calculation with signs and operation order','M2:T1:O01','37','supporting-practice candidate requiring evidenced need; not full modulus-equation/inequality coverage'),
('TB10',409,397,'9.1 Example 2 and Try Now 2(a-f)','Convert logarithmic and exponential statements and respect domain','M2:T2:O01','42','supporting or syllabus-derived branch; no claim of examination frequency'),
('TB11',450,438,'10.1 Try Now 1-2; Examples 2-3','Reciprocal trig sketches and graph-based root count','M2:T3:O01 M2:T6:O01','46 58','include under owner decision 6; derive consistent curves/axes/asymptotes and marking reference from instance data; app acceptance not tested here'),
('TB12',484,472,'11.1 Try Now 1-2; Examples 2-3','Product plus chain rule with polynomial or radical factors','M2:T4:O02','51','factorisation/required result and evidence define branch boundaries, not superficial expression length'),
('TB13',530,518,'12.1 Example 1, Try Now 1(a-d), Example 2(a-b)','Elementary exponential antiderivative versus definite evaluation','M2:T5:O01','54','same generator may share algebra, but definite bounds/exactness and constant requirements differ'),
('TB14',550,538,'12.4 Try Now 21 Q1(a-b), Q2(a-c)','Trapezium estimate and justified bias, including nonuniform curvature','M2:T5:O03 M2:T5:O04','56 57','Q2(c) cross-reference resolved: intended integral is part (b), not stationary-point part (a). f double-prime=(x-2)e^-x<0 on [0,2); trapezia underestimate. Prefer official concavity/relative-position explanation over conflicting concave/convex terminology.'),
('TB15',560,548,'13.1 Example 1(a-b), Try Now 1 Q1-3','Graphical root count and separate sign-change brackets','M2:T6:O01','58 59','Preserve global root count and local bracket separately. Book recommends plotting tables, conflicting with official graph-sketch guidance; use characteristic features and asymptotes. Sign change alone does not prove uniqueness.'),
]
samples=[]
for sid,pdf,printed,locator,action,objs,patterns,decision in SAMPLES:
    samples.append({'sample_id':'8227:'+sid,'document_id':book['document_id'],'sha256':book['sha256'],
                    'pdf_page':pdf,'printed_page':printed,'exercise_or_figure_locator':locator,
                    'learner_decision':action,'objective_ids':['8227:2020:'+o for o in objs.split()],
                    'related_pattern_ids':['8227:PAT-'+f for f in patterns.split()],
                    'evidence_kind':'textbook-derived','decision':decision,'source_review':'visual source scoping, not independent answer checking',
                    'output_origin':'newly authored problems and diagrams proposed; no direct reuse approved'})
goldie=next(x for x in register['records'] if x['document_id']=='8227-SRC-015')
for sid,pdf,printed,locator,action,oid,patterns,decision in [
    ('TB16',164,150,'6.1 Exercise 6A Q1-4; preceding Figure 6.5',
     'Separate global root count, continuity and local sign bracket','M2:T6:O01','58 59',
     'Sign changes across a discontinuity must not be treated as a root; graph and domain validation required.'),
    ('TB17',170,156,'6.3 Problems with fixed-point iteration; Figure 6.10',
     'Recognise divergence or convergence to unintended root','M2:T6:O02','62',
     'Textbook-derived and syllabus-required; no direct sampled paper part assigned. Exclude formal derivative convergence condition, which the Namibia syllabus does not require.')]:
    samples.append({'sample_id':'8227:'+sid,'document_id':goldie['document_id'],'sha256':goldie['sha256'],
        'pdf_page':pdf,'printed_page':printed,'exercise_or_figure_locator':locator,
        'learner_decision':action,'objective_ids':['8227:2020:'+oid],
        'related_pattern_ids':['8227:PAT-'+f for f in patterns.split()],
        'evidence_kind':'textbook-derived','decision':decision,
        'source_review':'native text inspected; diagrams/formulae not independently verified',
        'output_origin':'newly authored; no direct reuse approved'})
# Additional rendered-page scoping closes the two unsampled topic sections.
samples[0]['exercise_or_figure_locator']='1.7 Revision Exercise 1 Q1-3 and Q5'
samples[0]['objective_ids']+=['8227:2020:M1:T1:O04','8227:2020:M1:T1:O05']
samples[0]['additional_item_analysis']=[
 {'item':'Q3','demand_ids':['8227:2020:M1:T1:O04:D01','8227:2020:M1:T1:O04:D02','8227:2020:M1:T1:O04:D03'],'decision':'Quadratic in 1/x squared; recover x and reject inadmissible substitutions'},
 {'item':'Q5','demand_ids':['8227:2020:M1:T1:O05:D02'],'decision':'Reconstruct cubic from root -3, tangent root 2/3 and y-intercept 6; different reasoning from factorising a supplied cubic','diagram_required':True}]
for sid,page,printed,locator,decision,oids in [
 ('TB18',141,129,'3.3 Coordinate Geometry, Example 20 and Try Now 20','Reflection of a point in a line using perpendicular intersection and midpoint; chapter numbering is rendered 3.3, not inferred from OCR','M1:T4:O01 M1:T4:O02'),
 ('TB19',175,163,'4.2 Trigonometry, Try Now 12 and Example 13','Sine/cosine transformations and tangent period/asymptotes; plotting-table advice conflicts with official sketch conventions','M1:T6:O01')]:
 samples.append({'sample_id':'8227:'+sid,'document_id':book['document_id'],'sha256':book['sha256'],
   'pdf_page':page,'printed_page':printed,'exercise_or_figure_locator':locator,'learner_decision':decision,
   'objective_ids':['8227:2020:'+o for o in oids.split()],'related_pattern_ids':[],
   'evidence_kind':'textbook-derived','source_review':'rendered page inspected by Codex 2026-11-16; not independent answer-key review',
   'decision':'include as analysis lead, not recipe acceptance','output_origin':'newly authored proposed; no original textbook exercise delivered'})
write(A/'textbook-samples.json',{'samples':samples,'limitations':'Selected families across all 13 Namibia-book chapters and two Goldie sections; not every exercise or answer was reviewed. Remaining OCR index entries are leads.'})

errors=[
('ERR01',2021,231,'Candidates must be informed','Proof/show needs complete reasoning and explicit conclusion','22 47'),
('ERR02',2021,232,'hence means','Reuse the earlier result when demanded; keep connected parts','04 55'),
('ERR03',2021,232,'Many candidates did not find','Initial conditions and integration constants propagate to later motion parts','36'),
('ERR04',2021,235,'Candidates struggled to find the domain','Domain restrictions, inverse and graph are linked demands','14 15 17'),
('ERR05',2022,303,'because the line is a tangent','Do not apply a quadratic discriminant blindly to a nonquadratic tangency problem','28 18'),
('ERR06',2022,305,'relationship between r and h was problematic','Derive geometric relation before connected-rate calculation','31'),
('ERR07',2023,334,'Many candidates, wrongly used','A plotted coordinate is not automatically the transformed graph intercept','45'),
('ERR08',2024,337,'Most candidates wrongly attempted','There is no universal quotient rule for integration; use the algebraic quotient first','39 54'),
('ERR09',2025,347,'A few candidates calculated a scalar product','Perpendicularity requires the scalar product to equal zero','26'),
('ERR10',2025,352,'wrongly concluded that a','Recover original variable after quadratic substitution','04'),
('ERR11',2025,358,'Candidates must be taught to draw straight lines','Compare trapezium chords with curve to justify estimate bias','57'),
('ERR12',2025,362,'Most candidates failed to realize','Composite trig differentiation needs chain rule; later reverse integration is separate','50 55'),
]
e=[]
for sid,year,page,anchor,summary,patterns in errors:
    report=json.loads((A/'extracted'/f'report-{year}.json').read_text());raw=next(x['text'] for x in report['pages'] if x['pdf_page']==page)
    rx=re.compile(r'\s+'.join(map(re.escape,anchor.split())),re.I);m=rx.search(raw)
    if not m:raise ValueError((sid,anchor,page))
    # Bound at a paragraph or next question, rather than a fixed 700 chars.
    tail=raw[m.start():]
    boundaries=[x.start() for x in re.finditer(r'\n\s*\n|\n\s*Question\s+\d+|\n\s*\([a-z]\)',tail,re.I) if x.start()>len(m[0])]
    end=min(boundaries) if boundaries else len(tail)
    quote=tail[:end].strip()
    e.append({'error_id':'8227:'+sid,'summary':summary,'source_kind':'corpus',
              'source_path':report['source'],'sha256':report['sha256'],'pdf_page':page,
              'verbatim_extracted_excerpt':quote,'pattern_ids':['8227:PAT-'+p for p in patterns.split()],
              'limit':'Reported cohort difficulty; not diagnosis of an individual learner and not an invented distractor rationale'})
write(A/'examiner-difficulties.json',{'entries':e})
print(json.dumps({'source_records':len(register['records']),'ocr_pages':663,'indexed_heading_pages':len(leads),
                  'textbook_samples':len(samples),'examiner_difficulty_entries':len(e)},indent=2))
