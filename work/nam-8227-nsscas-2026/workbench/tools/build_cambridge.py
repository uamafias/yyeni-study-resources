"""Assemble verified selected originals from local Cambridge sources and annotations."""
import json
import re
from analysis_sources import A, ROOT, WB, clean, crop_asset, digest, render_page, reference_label, write
from cambridge_inputs import ITEMS
from cambridge_part_inputs import PARTS
from repair_inputs import demand_id
from render_analysis_records import table


def resolve(stem):
    files=sorted((A/'cambridge-discovery').glob(stem+'-*.json'))
    assert files,('missing local source index',stem)
    docs=[json.loads(p.read_text()) for p in files]
    assert len({x['sha256'] for x in docs})==1,('ambiguous source bytes; choose explicitly',stem)
    result=docs[0]
    assert digest(ROOT/result['path'])==result['sha256']
    return result


def build():
    registry=json.loads((A/'demand-registry.json').read_text())['demands']
    valid={d['demand_id'] for d in registry}
    records=[]
    for annotation in ITEMS:
        a=annotation
        m=re.fullmatch(r'9709_([msw])(\d{2})_qp_(\d{2})',a['file']);assert m
        session={'m':'Feb/March','s':'May/June','w':'Oct/Nov'}[m[1]]
        qp=resolve(a['file']);ms=resolve(a['file'].replace('_qp_','_ms_'))
        for d in [qp,ms]:
            assert '9709' in d['pages'][0]['text'] and str(2000+int(m[2])) in d['pages'][0]['text'],a['file']
        codes=[demand_id(c) for c in a['demands']]
        assert codes and all(c in valid for c in codes),a['file']
        qpart=a['part'];suffix='' if qpart is None else '-'+qpart.replace('.','-')
        item_id=f'8227:CAMBRIDGE:{a["file"].replace("9709_", "").replace("_qp_", ":")}:{a["question"]}{suffix}'
        pages=a.get('pdf_pages',[a['pdf_page']])
        images={str(n):digest(render_page(qp['path'],n)) for n in pages}
        # This assertion binds the notation-normalized transcription to a source
        # page/identity and a named visual check. It cannot itself certify prose.
        assert a['verbatim_text'].strip()
        assets=[]
        if a.get('diagram_box'):
            assets.append(crop_asset(qp['path'],a['pdf_page'],a['diagram_box'],
                a['file'].lower()+f'-q{a["question"]}'+suffix+'-given','Cambridge original source diagram'))
        selected=a.get('selected_parts')
        part_rows=PARTS.get((a['file'],a['question']),[])
        if part_rows:
            assert sum(p[2] for p in part_rows)==a['marks']
            as_demands={demand_id(code) for p in part_rows for code in p[4].split() if not code.startswith('NSSCO.')}
            assert as_demands==set(codes),(a['file'],a['question'],'part demand reconciliation',as_demands,set(codes))
            selected=[p[0] for p in part_rows]
        refs=[]
        for part in selected if selected else [qpart]:
            ref_page=next((p[1] for p in part_rows if p[0]==part),a['pdf_page'])
            ref={'board':'Cambridge International','syllabus_code':'9709','year':2000+int(m[2]),
                 'session':session,'paper':m[3],'question':str(a['question']),'part':part,
                 'printed_page':ref_page,'pdf_page':ref_page,
                 'source_path':qp['path'],'source_sha256':qp['sha256'],'relation':'original',
                 'verified_by':'Codex 2026-11-16; original page image, printed header and paper footer; independent re-review pending'}
            ref['learner_label']=reference_label(ref);refs.append(ref)
        row={'item_id':item_id,'locator':{'source_path':qp['path'],'source_sha256':qp['sha256'],
             'year':2000+int(m[2]),'session':session,'paper':m[3],'question':str(a['question']),
             'part':qpart,'pdf_page':a['pdf_page'],'pdf_pages':pages,'printed_page':a['pdf_page']},
             'mark_scheme_locator':{'source_path':ms['path'],'source_sha256':ms['sha256'],
               'pdf_pages':a['ms_pages'],'question':str(a['question']),'part':qpart,
               'inspection':'matching component/session/year and selected awards read; full marking rules not transcribed'},
             'marks':a['marks'],'verbatim_text':a['verbatim_text'],
             'transcription_status':'checked-against-rendered-page',
             'transcription_scope':{'selected_parts':selected,'omitted_parts':a.get('omitted_parts',[]),
                 'rule':'Original shared stem and selected original parts; no paraphrase. Omitted parts are not claimed reproduced.'},
             'visual_check':{'by':'Codex','date':'2026-11-16','renderer':'macOS PDFKit; render_pdf_macos.swift',
                 'rendered_page_hashes':images,'independent_repair_review':'pending'},
             'assessed_8227_demand_ids':codes,'objective_ids':sorted({c.rsplit(':D',1)[0] for c in codes}),
             'scope_check':{'status':'in-scope-parts-only' if a.get('omitted_parts') else 'in-scope',
                 'authority':'NIED 8227 December 2020 specific objectives and LIMIT01-08, not the Cambridge syllabus edition',
                 'reason':scope_reason(codes),
                 'unselected_parts':'not used in this item; no automatic out-of-scope claim'},
             'purpose':a.get('purpose','gap-fill'),
             'evidence_label':'comparable-examination-observed (Cambridge 9709)',
             'given_representation':{'kind':'diagram' if assets else 'text',
                                     'must_read':a.get('diagram_read','Read the original expressions, interval/domain and requested output.')},
             'diagram_assets':assets,'diagram_parameters':{'variable':a.get('diagram_variables',[]),
                 'fixed':[x.strip() for x in a.get('diagram_fixed',[])],'relations':[x.strip() for x in a.get('diagram_constraints',[])],
                 'scale':'schematic; no measuring unstated lengths'},
             'response_format':a.get('response_format','symbolic'),
             'family_slugs':a['family_slugs'],'examination_references':refs,
             'rights_basis':'Vitalis owner request N2, 2026-11-16; exact attributed questions authorised for learner use; publication/assignment not performed',
             'evidence_limit':a.get('evidence_limit','Selected part(s) verified, not exhaustive paper/variant or mathematical-solution review.')}
        row['assessed_parts']=[{'part_id':item_id+':'+label,'source_label':label,'pdf_page':page,
            'printed_page':page,'marks':marks,'response_format':response,
            'directly_assessed_demand_ids':[demand_id(c) for c in short.split()],
            'objective_ids':sorted({demand_id(c).rsplit(':D',1)[0] for c in short.split() if not c.startswith('NSSCO.')}),
            'examination_references':[r for r in refs if r['part']==label],
            'evidence_role':'AS specific demands or explicitly assessed prior geometry; prior components do not create AS coverage'}
            for label,page,marks,response,short in part_rows]
        if not part_rows:
            row['assessed_parts']=[{'part_id':item_id+':'+(qpart or 'answer'), 'source_label':qpart,
                'pdf_page':a['pdf_page'],'printed_page':a['pdf_page'],'marks':a['marks'],
                'response_format':row['response_format'],'directly_assessed_demand_ids':codes,
                'objective_ids':row['objective_ids'],'examination_references':refs}]
        if part_rows:
            row['response_format_note']='Primary indexing format only; mixed assessed-part response formats and award totals are retained in assessed_parts.'
        if a['file']=='9709_w22_qp_12':
            row['sketch_credited_features']={'basis':'official MS PDF 10, Q6(c)',
                'features':['B1 upward quadratic with both sides of stationary point visible',
                            'B1 F.T. stationary x-coordinate','B1 F.T. stationary y-coordinate'],
                'note':'No axes required; ignore axes even if incorrect. Expected stationary point (-5/2,-19).'}
        if a['file']=='9709_w21_qp_22':
            row['scope_check']['reason']+=' Conditional limit identification is not a formal convergence test and does not establish failure-to-converge coverage.'
        records.append(row)
    write(A/'cambridge-evidence.json',{'schema_version':'workbench-analysis-8227-r2','items':records,
        'scope':'Selected verified originals; corpus-wide text search is discovery, not full content classification.',
        'limits':'No item establishes NSSCAS examination observation; distinct instances do not automatically establish distinct problem types.'})
    rows=[]
    for r in records:
        loc=r['locator'];ms=r['mark_scheme_locator']
        rows.append([r['item_id'],[x['learner_label'] for x in r['examination_references']],r['marks'],
                     r['assessed_8227_demand_ids'],r['scope_check']['status']+': '+r['scope_check']['reason'],
                     ms['source_path']+' PDF '+str(ms['pdf_pages']),r['purpose']])
    text=table('Cambridge evidence for NSSCAS Mathematics 8227',
        ['Item','Original attribution','Marks','Direct 8227 demands','Scope decision','Matching mark scheme','Purpose'],rows,
        'Owner Vitalis, request N2; author Codex, 16 November 2026; independent re-review pending. '
        'Exact originals and source-page/crop hashes are in the JSON. Text-search hits are not verified items. '
        'Gap filling is measured against direct NSSCAS part links; Cambridge evidence retains its own board/session/component. '
        'The iteration candidate was Q6(c), not Q9(c), and does not assess iteration failure.')
    (A/'cambridge-evidence.md').write_text(text)
    return records


def scope_reason(codes):
    if any(':M2:T1:O03:' in c for c in codes):
        return 'Polynomial degree 3 or 4 divided by a quadratic; within LIMIT05. No partial fractions or higher-degree divisor.'
    if any(':M1:T7:' in c for c in codes):
        return 'Three-dimensional coordinates, vector arithmetic, magnitude/unit vector or scalar product only; no vector-line equations or line/plane intersections.'
    if any(':M1:T5:O02:' in c for c in codes):
        return 'Arc/sector/circular-segment geometry with explicit radians, radii and tangent constraints; no beyond-syllabus calculus.'
    if any(':M1:T6:O04:' in c for c in codes):
        return 'Standard principal inverse trigonometric ranges and elementary algebra/exact ratios; no general trig-solution form or inverse-trig differentiation.'
    if any(':M2:T6:' in c for c in codes):
        return 'Given rearrangement, graph/sign bracket and prescribed-accuracy iteration; no formal derivative convergence criterion (LIMIT08).'
    if any(':M1:T8:O03:D02' in c for c in codes):
        return 'Sign of a rational-power/polynomial derivative on a stated domain; within Mathematics 1 power/chain rules (LIMIT04).'
    if any(':M1:T5:O01:' in c for c in codes):
        return 'Radian-to-degree conversion of an explicitly supplied angle; omitted sector derivations are not needed for the selected part.'
    if any(':M1:T3:' in c for c in codes):
        return 'One-to-one/inverse interpretation for a stated bounded function; no inverse differentiation or out-of-scope general theory.'
    if any(':M1:T4:O02:D02' in c for c in codes):
        return 'Tangency of a straight line and a quadratic curve can be solved by a repeated-root discriminant or an award-accepted derivative method. No higher-degree tangency or conic theory required.'
    if any(':M1:T4:O02:D01' in c for c in codes):
        return 'Eliminate a variable between a straight line and a simple algebraic curve, solve the resulting quadratic and recover both coordinates. No conic classification or conic formula required.'
    if any(':M2:T2:O02:D02' in c for c in codes):
        return 'Sketch a basic transformed exponential, with a modulus comparison where requested; no beyond-syllabus convergence or logarithmic differentiation.'
    return 'Quadratic shape and stationary coordinates within 8227 M1 T1; no additional content from the Cambridge edition.'


if __name__=='__main__':build()
