"""Generate cropped source evidence and attach authored response/asset requirements."""
import json
import re
import pymupdf
from PIL import Image, ImageDraw
from analysis_sources import A, ROOT, clean, crop_asset, digest, render_page, reference_label, write
from repair_inputs import SKETCH_PARTS, SKETCH_DEPENDENT, response_annotations
from visual_inputs import DIAGRAMS, DIAGRAM_PARTS, SKETCH_FEATURES, RESPONSE_FRAMES


def printed_page_index(questions):
    rows=[]
    for year in range(2021,2026):
        cells=[]
        for component in [1,2]:
            group=[q for q in questions if q['year']==year and q['paper']==component]
            source=group[0]['question_source_path'];pages=sorted({n for q in group for n in q['pdf_pages']})
            doc=pymupdf.open(ROOT/source)
            for n in pages:
                raw=doc[n-1].get_textbox(pymupdf.Rect(260,5,335,45))
                numbers=set(re.findall(r'\b\d{1,2}\b',raw))
                assert len(numbers)==1,(year,component,n,raw)
                number=int(next(iter(numbers)))
                with Image.open(render_page(source,n)) as im:
                    cell=im.convert('RGB').crop((520,10,670,90))
                cells.append((f'P{component} PDF{n}: {number}',cell))
                rows.append({'source_path':source,'source_sha256':digest(ROOT/source),'pdf_page':n,
                             'printed_page':number,'verification':'PDFKit rendered-header contact sheet; Codex author check, 2026-11-16',
                             'note':'Printed pagination differs from PDF ordinal' if number!=n else None})
        sheet=Image.new('RGB',(1100,120*((len(cells)+5)//6)),'white');draw=ImageDraw.Draw(sheet)
        for i,(label,im) in enumerate(cells):
            x=i%6*183;y=i//6*120;draw.text((x+2,y+2),label,fill='red');sheet.paste(im,(x,y+25))
        target=A/'assets'/f'printed-page-headers-{year}.png';target.parent.mkdir(exist_ok=True);sheet.save(target)
    write(A/'printed-page-index.json',{'entries':rows,'method':'Header text plus rendered-header contact sheet; never assume a PDF-page offset.'})
    return {(r['source_path'],r['pdf_page']):r for r in rows}


def response_format(part):
    return response_annotations()[part['source_key']]


def attach_visuals_and_references(questions,negative_fixture=None):
    pages=printed_page_index(questions)
    index={q['source_key']:q for q in questions}
    diagrams={}
    all_assets=[]
    for row in DIAGRAMS.strip().splitlines():
        key,number,box,kind,read,variable,fixed,relations=row.split('|')
        q=index[key]
        asset=crop_asset(q['question_source_path'],int(number),list(map(float,box.split(','))),
                         key.lower()+'-given','given source diagram/graph')
        diagrams[key]=(asset,kind,read,variable,fixed,relations)
        all_assets.append(asset)
    scans=json.loads((A/'part-source-scan.json').read_text())['parts']
    for q in questions:
        key=q['source_key']
        for p in q['parts']:
            label=p['source_label'] or 'answer'
            diagram=diagrams.get(key) if label in DIAGRAM_PARTS.get(key,{label}) else None
            p['given_representation']={'kind':diagram[1] if diagram else 'text',
                 'must_read':diagram[2] if diagram else 'Read the stated expressions, numerical data, restrictions and requested result from this part and its inherited question stem.'}
            p['diagram_assets']=[diagram[0]] if diagram else []
            p['diagram_parameters']={'variable':[x.strip() for x in diagram[3].split(';') if x.strip()],'fixed':[x.strip() for x in diagram[4].split(';') if x.strip()],
                 'relations':[x.strip() for x in diagram[5].split(';') if x.strip()],'scale':'schematic; do not infer unstated measurements',
                 'generation_requirement':'Generate from the same instance values as the question, answer and marking reference; inspect geometry and labels.'} if diagram else {'variable':[],'fixed':[],'relations':[]}
            p['response_frame_assets']=[]
            if p['source_key'] in RESPONSE_FRAMES:
                frame_page,box=RESPONSE_FRAMES[p['source_key']]
                frame=crop_asset(q['question_source_path'],frame_page,box,
                    p['source_key'].lower().replace(':','-')+'-response-frame','provided blank response axes; not a given graph')
                p['response_frame_assets']=[frame]
                p['diagram_assets'].append(frame)
                p['diagram_parameters']['response_frame']={'fixed':['source axis variables and origin'],
                    'variable':['axis extent and optional scale when the authored instance requires them'],
                    'relations':['Do not pre-draw the required answer or count the blank axes as a given graph.']}
                all_assets.append(frame)
            p['response_format']=response_format(p)
            p['response_requirement']=p['response_format']
            if p['source_key'] in SKETCH_FEATURES:
                features,award=SKETCH_FEATURES[p['source_key']]
                p['sketch_credited_features']={'features':features,'basis':'official award table' if award else 'author-derived from task and tariff; not an official mark allocation',
                                             'report_pdf_page':award,'total_marks':p['printed_marks'],
                                             'criterion_reconciliation':'independent re-review pending'}
            if p['source_key']=='2023-2-Q6:d':
                p['sketch_credited_features']={'features':['State under-estimate','Reason must agree with learner graph and show trapezium tops below curve'],
                   'basis':'official table PDF 337: graph-consistency condition, not literal F.T. wording','report_pdf_page':337}
            # Reference the page where this part's label begins, not just where
            # its tariff ends (several questions span pages).
            scan=scans[p['source_key']]
            candidates=[]
            for segment in scan.get('segment_pages',[]):
                token=label.split('.')[-1]
                rx=r'^\s*(?:\d+\s*)?\('+re.escape(token)+r'\)'
                if re.search(rx,segment['text'],re.M):candidates.append(segment['pdf_page'])
            n=candidates[0] if candidates else q['pdf_pages'][0] if label=='answer' else scan['pdf_page']
            page=pages[(q['question_source_path'],n)]
            ref={'board':'NSSCAS','syllabus_code':'8227','year':q['year'],'session':None,
                 'paper':str(q['paper']),'question':str(q['question']),'part':None if label=='answer' else label,
                 'printed_page':page['printed_page'],'pdf_page':n,'source_path':q['question_source_path'],
                 'source_sha256':q['source_sha256'],'relation':'original',
                 'verified_by':'Codex, 2026-11-16; part-label scan and rendered pagination; independent re-review pending'}
            ref['learner_display']=p['disposition']!='hold'
            ref['learner_display_reason']='Owner-authorised attributed examination original; source disposition still controls use.' if ref['learner_display'] else 'Held defective source exemplar; never show the original to learners.'
            if negative_fixture=='held-reference' and p['disposition']=='hold':ref['learner_display']=True
            assert p['disposition']!='hold' or ref['learner_display'] is False,('held reference is learner-displayable',p['source_key'])
            ref['learner_label']=reference_label(ref)
            p['examination_references']=[ref]
    write(A/'asset-index.json',{'assets':all_assets,'crop_review':'Codex author source-page and generated-crop contact-sheet inspection, 2026-11-16; independent re-review pending',
          'capability_decision':'Vitalis 2026-11-16 decision 6; included; app availability announced for 2026-11-17, not locally runtime-tested here'})
    return all_assets
