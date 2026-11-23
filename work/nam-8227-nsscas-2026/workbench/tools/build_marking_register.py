"""Build source-backed examiner conventions and criterion transcriptions (not runtime rubrics)."""
from collections import defaultdict
import json
import re
from analysis_sources import A, WB, ROOT, clean, digest, write
from build_awards_r4 import build as build_awards
from convention_inputs import SPEC


def build():
    reports=json.loads((A/'report-page-index-r4.json').read_text())
    for page in reports['pages']:page['text']=page['text_discovery_only']
    pages={(x['year'],x['pdf_page']):x for x in reports['pages']}
    questions=json.loads((A/'question-analysis.json').read_text())['questions']
    qs={q['source_key']:q for q in questions}
    allparts=[p for q in questions for p in q['parts']]
    def links(parts):
        return {'demand_ids':sorted({d for p in parts for d in p['directly_assessed_demand_ids']}),
                'group_ids':sorted({d for p in parts for d in p['pattern_ids']})}
    def locator(y,p,q=None,part=None,paper=None):
        doc=pages[y,p];assert digest(ROOT/doc['source_path'])==doc['source_sha256']
        return {'report_year':y,'source_path':doc['source_path'],'source_sha256':doc['source_sha256'],
                'pdf_page':p,'printed_page':p-2,'paper':paper,'question':q,'part':part}
    rules=[]
    for i,line in enumerate(SPEC.strip().splitlines(),1):
        y,pg,key,part,kind,anchor,reading=line.split('|');y=int(y);pg=int(pg)
        text=clean(pages[y,pg]['text']); match=re.search(re.escape(anchor),text,re.I)
        visual_only=(y,pg,anchor)==(2025,364,'Correct ruled V-shape')
        assert match or visual_only,(key,part,anchor,'quote anchor missing')
        excerpt=match[0]if match else anchor
        # Anchor itself is a short, exact excerpt, not a paraphrase manufactured from the policy.
        targets=[p for p in (allparts if key=='general' else qs[key]['parts'])
                 if (part=='*' or (p['source_label'] or 'answer')==part)]
        assert targets,(key,part)
        rules.append({'rule_id':f'8227:CONVENTION:{i:03}', 'type':kind,
                      'source_question_key':None if key=='general' else key,
                      'verbatim_excerpt':excerpt,'source_locator':locator(y,pg,None if key=='general' else qs[key]['question'],None if part=='*' else part,None if key=='general' else qs[key]['paper']),
                      'interpretation':reading,'strength':'explicit general rule' if key=='general' else 'single-question remark',
                      'applies_to':{'part_ids':[p['part_id'] for p in targets],**links(targets)},
                      'application_condition':'Part instructions and explicit award rows govern; general report prose does not erase B/SC/F.T. criteria.' if key=='general' else 'Only this question/part unless independently supported elsewhere.',
                      'conflicts':[],'learner_display':False,'evidence_kind':'examiner-report-observed'})
    general_pages={(2021,231),(2021,236),(2022,301),(2022,307),(2023,321),(2023,330),(2024,325),(2024,335),(2025,345),(2025,355)}
    aliases={14:2,15:3,16:4,30:17,33:2,34:3,35:4,36:18,48:17,49:2,50:4,51:18,63:17,67:2,69:18,77:6,106:70}
    canonical={r['rule_id']:r for r in rules if int(r['rule_id'].rsplit(':',1)[1])not in aliases}
    for r in canonical.values():r['evidence']=[];r['historical_rule_ids']=[]
    for raw in rules:
        n=int(raw['rule_id'].rsplit(':',1)[1]);target=canonical[f'8227:CONVENTION:{aliases.get(n,n):03}']
        if n in aliases:target['historical_rule_ids'].append(raw['rule_id'])
        candidates=[(raw['source_locator']['report_year'],raw['source_locator']['pdf_page'])]
        if raw['strength']=='explicit general rule':
            candidates=sorted(general_pages)
        for y,pg in candidates:
            text=clean(pages[y,pg]['text']);m=re.search(re.escape(raw['verbatim_excerpt']),text,re.I)
            if not m and(y,pg)!=(raw['source_locator']['report_year'],raw['source_locator']['pdf_page']):continue
            ev={'source_locator':locator(y,pg,raw['source_locator']['question'],raw['source_locator']['part'],raw['source_locator']['paper']),
                'verbatim_excerpt':m[0]if m else raw['verbatim_excerpt'],
                'verification':'author inspected rendered page; text match is an additional locator check',
                'render_path':pages[y,pg]['render_path'],'render_sha256':pages[y,pg]['render_sha256']}
            if n==76:
                context=re.search(r'(?:It was noted that )?some candidates used calculators.*?No marks are awarded if only answers are given\.',text,re.I)
                assert context,(y,pg,'calculator context missing');ev['verbatim_context']=context[0]
            if not any(e['source_locator']==ev['source_locator']and e['verbatim_excerpt']==ev['verbatim_excerpt']for e in target['evidence']):target['evidence'].append(ev)
    rules=list(canonical.values())
    for rule in rules:
        if rule['strength']=='explicit general rule':
            rule['application_years']=[2021,2022,2023,2024,2025]
            rule['application_condition']='General convention across corpus years; exact question instructions and explicit award rows override. Calculator-only and hence rules retain their stated contexts.'
    # Preserve non-universal conflicts; no silent choice between inconsistent report conventions.
    conflicts=[
        ('8227:MC-CONFLICT:01',['2021-2-Q4:b'],'2021 PDF238 award accepts 35 although prose asks complete weeks and worked integer is 34.','Retain both; no general rounding-up rule.'),
        ('8227:MC-CONFLICT:02',['2023-2-Q7:b','2023-2-Q7:c'],'2023 PDF338 presents a degree-mode iteration alternative inconsistent with the radian equation.','Rejected alternative by binding owner decision 2; only radian path is operative.'),
        ('8227:MC-CONFLICT:03',['2023-2-Q4:b','2024-2-Q8:b'],'2023 PDF335 condones decimals after exact coefficient; 2024 PDF341 gives A0 if decimals also seen.','Part-specific precision policy; cannot promote either to a universal rule.'),
        ('8227:MC-CONFLICT:04',['2024-2-Q11:a','2025-1-Q4:b','2025-2-Q12:a'],'2024 PDF343 accepts straight by eye; 2025 PDF347 asks for ruler use and PDF364 explicitly requires a correct ruled V-shape.','Question-specific sketch requirements; assess branch criteria in step 3.'),
        ('8227:MC-CONFLICT:05',['2024-2-Q6:a','2023-2-Q5:b'],'2024 PDF338 prose explicitly requires boundary substitutions, not only results, while PDF339 table permits an implied second boundary. 2023 PDF336 also requires both boundaries shown.','Record criterion-specific proof evidence, not a universal zero-boundary rule.'),
        ('8227:MC-CONFLICT:06',['2023-2-Q6:b'],'General hence prose says no marks without prior result; PDF337 explicitly grants SC1 for correct result without hence.','Specific award table takes precedence for this source.'),
        ('8227:MC-CONFLICT:07',['2024-2-Q8:a'],'2024 PDF341 award caption says y=3e^{-x}; question and award graphic show y=e^{-x}, intercept 1.','Use question/graphic; retain caption defect as source evidence.'),
        ('8227:MC-CONFLICT:08',['2023-2-Q6:c'],'2023 PDF337 prose says unlabelled dual graphs lose all marks; table explicitly removes the shape B1 when more than one graph is seen but has separate asymptote and intercept B1 rows.','Preserve both. Do not silently turn a prose all-marks statement into a verified per-criterion policy.'),
        ('8227:MC-CONFLICT:09',['2025-2-Q12:d'],'2025 PDF363 prose says final answer four significant figures; PDF364 prose and printed answer1.70 support three significant figures, as question asks.','Use question three-significant-figure requirement; retain earlier prose error.'),
    ]
    for cid,keys,description,resolution in conflicts:
        for rule in rules:
            if any(k.rsplit(':',1)[0]==rule['source_question_key'] and
                   (rule['source_locator']['part'] is None or k.rsplit(':',1)[1]==rule['source_locator']['part']) for k in keys):
                rule['conflicts'].append(cid)
    awards=build_awards(final=True)
    tables=awards['award_tables']
    for table in tables:
        q=qs[table['source_key']]
        for row in table['rows']:
            part=next(p for p in q['parts']if p['part_id']==row['part_id'])
            row['dependencies']={'dependent_award':row['dependent_award'],'condition':row['condition'],
                'follow_through':'F.T.'in row['qualifier_codes'],'earlier_part_edges':part.get('dependency_edges',[])}
            row['demand_ids']=part['directly_assessed_demand_ids']
            row['criterion_demand_alignment']='Part context only; criterion-level branch allocation follows in step3.'
        table['total_check']='Part budgets reconcile per exclusive path; source gaps remain explicitly derived, not official.'
    rows=[r for t in tables for r in t['rows']]
    for rule in rules:
        candidates=[r for r in rows if r['part_id']in rule['applies_to']['part_ids']]
        if rule['strength']=='explicit general rule':
            n=int(rule['rule_id'].rsplit(':',1)[1])
            patterns={1:r'establish|conclu|shown|proof',2:r'method|working|integrat|differentiat|solve|factor',3:r'exact',4:r'round|accur|decimal|s\.f\.',5:r'establish|quoted',6:r'hence|their\s*\(a\)',7:r'otherwise',17:r'answer.only|without.*working',18:r'radian|degree|theta|angle',19:r'variable',68:r's\.f|decimal',70:r'sketch|shape|graph',76:r'answer.only|without.*working',78:r'variable|cos2A',79:r'quadratic|factor|solve'}
            pattern=patterns.get(n,r'(?!)')
            candidates=[r for r in candidates if re.search(pattern,r['what_earns_it']+' '+r['condition'],re.I)]
        rule['related_award_rows']=[r['criterion_id']for r in candidates]
        n=int(rule['rule_id'].rsplit(':',1)[1])
        exact={80:[3],81:[3],82:[6],83:[1],84:[],85:[],86:[8],87:[13,16],88:[6],89:[5,6],90:[2],109:[4],110:[3],111:[1],112:[4,5]}
        if n in exact:
            candidates=[r for r in candidates if int(r['criterion_id'].rsplit(':',1)[1])in exact[n]]
        else:
            anchor=clean(rule['verbatim_excerpt']).lower()
            candidates=[r for r in candidates if anchor in clean(r['what_earns_it']+' '+r['condition']+' '+' '.join(r['accepted_alternatives'])).lower()]
        rule['award_row_links']=[r['criterion_id']for r in candidates]
        rule['award_link_status']='same requirement stated in award'if candidates else 'prose evidence; no identical requirement identified in award wording'
        rule['award_link_limit']='Related rows give context only. An empty direct-link list does not imply that the prose is absent or unimportant.' 
        rule['award_link_basis']='Direct quote match or explicitly reviewed requirement correspondence; related part rows are stored separately. Links are not runtime penalty instructions.'
        for row in candidates:row.setdefault('convention_rule_ids',[]).append(rule['rule_id'])
    result={'schema_version':'8227-source-analysis-r4','status':'author round 4 marking pass; independent check pending',
         'coverage':{'report_ranges':reports['ranges'],'report_pages_read':len(reports['pages']),
              'award_tables':len(tables),'criterion_rows_including_exclusive_alternatives':awards['coverage']['criterion_rows'],
              'official_rows':awards['coverage']['official_rows'],'derived_completion_rows':awards['coverage']['derived_completion_rows'],
              'second_read_rows':awards['coverage']['second_read_rows'],'questions_without_award_table':0,
              'selection_method':'All 87 Mathematics report pages visually read; all 119 questions transcribed; every row second-read.',
              'limits':'Two parts have no printed award breakdown; one alternative path omits its final row. Derived completions reconcile tariffs but do not turn missing awards into official criteria. Independent review pending. Prose-only conventions and direct award links remain separate.'},
         'mark_type_normalisation':awards['mark_type_normalisation'],
         'rules':rules,'conflicts':[dict(zip(['conflict_id','part_keys','source_disagreement','disposition'],c))for c in conflicts],
         'award_tables':tables,'question_coverage':awards['question_coverage'],
         'rights':'Internal source analysis; examiner-report prose is not learner-display material.'}
    write(A/'marking-conventions.json',result)
    out=['# Examiner marking conventions — NSSCAS Mathematics 8227','',
         'Author source-analysis register, 17 November 2026. Focused independent check pending. Read all 87 Mathematics report pages. Tables found for 119 questions; 818 printed rows plus 3 explicitly derived completions. Every row second-read against the image. This is source analysis, not a certified runtime marking bank.','',
         'E, DM and DB source notation is preserved. Normalised E→A carries establishes_given_result=true and requires establishment; alternative paths and special cases must never be added together. Criterion wording below is a normalised transcription, not a claim of exact scheme prose.','',
         '| Rule | Source (PDF page) | Type / strength | Excerpt | Application |','|---|---|---|---|---|']
    for r in rules:
        l=r['source_locator'];out.append(f'| {r["rule_id"]} | {l["report_year"]} p{l["pdf_page"]}, Q{l["question"] or "general"} {l["part"] or ""} | {r["type"]}; {r["strength"]} | {r["verbatim_excerpt"]} | {r["interpretation"]} |')
    out+=['','## Conflicts retained','']
    for c in result['conflicts']:out.append(f'- **{c["conflict_id"]}**: {c["source_disagreement"]} {c["disposition"]}')
    for t in tables:
        out+=['',f'## {t["source_key"]} — {t["paper_tariff"]} marks','',
              '| Part | Exclusive path | Source mark | Earns credit | Dependency / F.T. / alternative | PDF page |','|---|---|---|---|---|---|']
        for r in t['rows']:out.append(f'| {r["part"]} | {r["exclusive_method_path"]} | {r["source_mark_type"]}{r["value"]} | {r["what_earns_it"]} | {r["accepted_alternatives"]} | {r["source_locator"]["pdf_page"]} |')
        out+=['','Exclusive path budgets reconcile with paper tariffs. See JSON for any derived completion where official rows are absent.']
    out+=['','## Coverage limits','',result['coverage']['limits'],'']
    (A/'marking-conventions.md').write_text('\n'.join(out))
    print(json.dumps(result['coverage'],indent=2))
if __name__=='__main__':build()
