"""Reconcile inspected book pages and expose unclassified discovery leads."""
import json,re,hashlib,math
from pathlib import Path
from analysis_sources import A,WB,ROOT,write,digest,evidence_path

def build():
 groups=[('Goldie','goldie-render-manifest.json','problem'),('Goldie','goldie-continuations-manifest.json','continuation/scope'),('Goldie','goldie-answers-manifest.json','answer'),('YM','ym-revision-render-manifest.json','problem'),('YM','ym-exercises-manifest.json','problem'),('YM','ym-priority-manifest.json','problem'),('YM','ym-continuations-manifest.json','continuation')]
 seen=[]
 for book,name,kind in groups:
  for r in json.loads((WB/'checks/r3'/name).read_text()):
   path=evidence_path(r['path'])
   seen.append({'book':book,'kind':kind,'pdf_pages':r.get('pages',r.get('pdf_pages')),'evidence_path':str(path.relative_to(ROOT)),
      'sha256':digest(path),'inspection':'Codex author visually inspected this contact sheet, including problem mathematics and diagrams; not independent review'})
 for meta in sorted((WB/'checks/r4').glob('textbook-*.json')):
  r=json.loads(meta.read_text())
  if not r.get('inspection','').startswith('Codex author visually'):continue
  path=evidence_path(r['path']);assert digest(path)==r['sha256']
  seen.append({'book':r['book'],'kind':'r4 problem/answer correction','pdf_pages':r['pdf_pages'],'evidence_path':r['path'],'sha256':r['sha256'],'inspection':r['inspection']})
 # R5 finds valid material beyond the old bounded target. Count only explicit
 # page-census readings,never an image merely created by a rendering command.
 for path in sorted((WB/'tools/textbook-r5').glob('census-*.json')):
  data=json.loads(path.read_text())
  for row in data['pages']:
   assert row['reader']=='Codex author'and row['date']
   ev=row['source_evidence'];assert digest(evidence_path(ev['path']))==ev['sha256']
   seen.append({'book':data['book'],'kind':'r5 explicit rendered-page census','pdf_pages':[row['pdf_page']],
    'evidence_path':ev['path'],'sha256':ev['sha256'],'inspection':'Codex author page-specific enumeration; independent acceptance pending'})
 inv=json.loads((A/'textbook-inventory.json').read_text());items=inv['items']
 starts=[12,52,107,153,232,266,322,376,407,448,482,529,558]
 leads=[]
 for p in json.loads((A/'textbook-ymxc-discovery.json').read_text())['pages']:
  pg=p['pdf_page'];ch=max(i for i,n in enumerate(starts,1) if pg>=n)
  if pg==139:continue
  for h in p['heading_leads']:
   m=re.match(r'^(Example|Try Now|Lry Now)\s*[-:]?\s*(\d+)',h['heading'],re.I)
   if not m:continue
   kind='Example' if m[1].lower()=='example' else 'Try Now';n=int(m[2])
   matches=[i['item_id'] for i in items if i['book_id']=='8227-SRC-017' and i['chapter']==ch and pg in [i['pdf_page'],*i.get('continuation_pdf_pages',[])] and
     ((i['exercise']==kind and i['item_number']==str(n)) or (kind=='Try Now' and i['exercise']==f'Try Now {n}'))]
   leads.append({'book':'YM','chapter':ch,'pdf_page':pg,'heading':h['heading'],'kind':kind,'number_candidate':n,
      'disposition':'classified item/block linked' if matches else 'unclassified; original item/subpart population and visual/gap flags need rendered-page reconciliation',
      'item_ids':matches,'evidence_status':'OCR discovery only; duplicate/misread/continued headings can occur'})
 for p in json.loads((A/'textbook-goldie-discovery.json').read_text())['pages']:
  pg=p['pdf_page']
  if not (15<=pg<=175 or 248<=pg<=272):continue
  for m in re.finditer(r'Example\s+(\d+\.\d+)',p['text']):
   ch,num=map(int,m[1].split('.'))
   matches=[i['item_id']for i in items if i['book_id']=='8227-SRC-015'and i['chapter']==ch and i['exercise']=='Example'and i['item_number']==str(num)and pg in [i['pdf_page'],*i.get('continuation_pdf_pages',[])]]
   leads.append({'book':'Goldie','pdf_page':pg,'heading':m[0],'disposition':'classified rendered worked example'if matches else'unclassified worked-example lead; section/scope and rendered mathematics need reconciliation',
                 'item_ids':matches,'evidence_status':'native text discovery only until rendered item record; repeated cross-reference headings can occur'})
 decisions=json.loads((WB/'tools/textbook_heading_dispositions_r4.json').read_text())
 for lead in leads:
  key=f"{lead['book']}|{lead['pdf_page']}|{lead['heading']}"
  if key in decisions:
   decision=decisions[key];assert digest(evidence_path(decision['render_path']))==decision['render_sha256']
   lead['author_disposition']=decision;lead['disposition']=decision['status']
   if decision.get('item_ids'):lead['item_ids']=decision['item_ids']
 missing=[i['item_id'] for i in items if not any(s['book']==('Goldie' if i['book_id']=='8227-SRC-015' else 'YM') and i['pdf_page'] in s['pdf_pages'] for s in seen)]
 assert not missing,('catalogued item lacks inspected page sheet',missing)
 result={'schema_version':'8227-source-analysis-r3','author_reading':seen,'catalogued_items_with_render_evidence':len(items),
    'instructional_support_not_assessed_item_coverage':[
       {'book':'YM','pdf_page':45,'printed_page':34,'demand_id':'8227:2020:M1:T1:O03:D01','evidence':'Teaching comparison table of equation, inequality and identity; no separately classified task asks the learner to distinguish them.'},
       {'book':'YM','pdf_page':154,'printed_page':142,'demand_id':'8227:2020:M1:T5:O01:D01','evidence':'Radian definition, equal radius/arc diagram and full-turn explanation; conversion exercises alone do not demonstrate the full meaning demand.'},
       {'book':'Goldie','pdf_page':93,'printed_page':79,'demand_id':'8227:2020:M1:T6:O04:D01','evidence':'Principal-value ranges are relevant even though general-solution formulae in the surrounding section are excluded by LIMIT02.'}],
    'discovery_leads':leads,'unclassified_heading_leads':sum(not x['item_ids'] and not x.get('author_disposition')for x in leads),
    'limits':'The historical R4heading sweep/759-page target remains a bounded reading record. R5explicit census pages add verified material beyond that original target; textbook-page-census.json is the current page/item/figure completion record. No exhaustive claim or routine stop rule. Exact answer locations and full answer accuracy are separate; independent acceptance remains pending.'}
 write(A/'textbook-reading-r3.json',result)
 # A page read and a reconciled heading are distinct from an exhaustive figure
 # census or independent content acceptance. Keep all three visible.
 page_notes=json.loads((WB/'tools/textbook_page_sweep_notes_r4.json').read_text())
 page_rows=[]
 for book,target in [('Goldie',set(range(15,176))|set(range(248,273))),('YM',set(range(12,586))-{139})]:
  bid='8227-SRC-015'if book=='Goldie'else'8227-SRC-017'
  for pg in sorted(target):
   sheets=[s for s in seen if s['book']==book and pg in s['pdf_pages']]
   related=[i for i in items if i['book_id']==bid and pg in [i['pdf_page'],*i['continuation_pdf_pages']]]
   page_rows.append({'book':book,'pdf_page':pg,'render_read':bool(sheets),
     'evidence_paths':sorted({s['evidence_path']for s in sheets}),
     'item_ids':[i['item_id']for i in related],
     'given_visual_item_ids':[i['item_id']for i in related if i['representation']in['diagram','graph','table']],
     'sketch_item_ids':[i['item_id']for i in related if i['sketch_response_required']],
     'author_page_note':page_notes.get(f'{book}|{pg}'),
     'figure_census_status':'item-linked visuals recorded; independent completeness check and separate teaching-figure enumeration pending'})
 audit={'schema_version':'8227-source-analysis-r4','target_definition':'Goldie PDF15–175 and248–272; YM PDF12–585 excluding duplicate139. Includes scope-boundary introductions, summaries and teaching pages. Answer pages are tracked separately.',
   'target_pages':len(page_rows),'render_read_pages':sum(p['render_read']for p in page_rows),
   'unread_pdf_pages':[{'book':p['book'],'pdf_page':p['pdf_page']}for p in page_rows if not p['render_read']],
   'pages':page_rows,'scope_and_answer_limits':result['limits']}
 write(A/'textbook-page-audit-r4.json',audit)
 lines=['# Textbook page audit — NSSCAS Mathematics 8227','',
   f"{audit['render_read_pages']} of {audit['target_pages']} target source pages have author-inspected render evidence. This is page-reading coverage; it does not certify every figure, qualifier or answer.",'',
   '| Book | PDF page | Read | Items linked | Given visual items | Sketch items | Source caution / disposition |','|---|---:|---|---:|---:|---:|---|']
 for p in page_rows:
  lines.append(f"| {p['book']} | {p['pdf_page']} | {p['render_read']} | {len(p['item_ids'])} | {len(p['given_visual_item_ids'])} | {len(p['sketch_item_ids'])} | {(p['author_page_note']or'').replace('|','/')} |")
 lines+=['',result['limits'],'']
 (A/'textbook-page-audit-r4.md').write_text('\n'.join(lines))
 response_items=[i for i in items if i.get('item_kind')not in['teaching-figure','given-figure']]
 def has_r5_answers(i):return bool(i.get('answer_verification_r5'))and i['answer_accuracy_status_r5'].startswith('author independently derived every explicit subpart')
 missing_keys=[{'item_id':i['item_id'],'source_pdf_page':i['pdf_page'],
    'scope':i['scope_check']['status'],'answer_locator':i['answer_key']['locator'],
    'reason':'No separate exact answer-location author record. Original page reading does not substitute for a checked answer/derivation.'}
    for i in response_items if not i['answer_key'].get('author_check')and not has_r5_answers(i)]
 open_checks={'status':'unfinished evidence checks; not a PLAN or authoring work order',
    'population':len(items),'response_item_population':len(response_items),'teaching_figure_population':len(items)-len(response_items),
    'answer_check_records':len(response_items)-len(missing_keys),'full_subpart_author_accuracy_reviews_r5':sum(has_r5_answers(i)for i in response_items),
    'missing_exact_answer_records':missing_keys,
    'published_answer_page_records':sum(bool(i['answer_key'].get('author_check',{}).get('pdf_pages'))or(has_r5_answers(i)and any(a['answer_pdf_page']is not None and a.get('key_presence')!='no separate key'for a in i['answer_verification_r5']))for i in response_items),
    'author_derived_investigation_records':sum(i['answer_key'].get('author_check',{}).get('record_type','').startswith('author-derived')for i in items),
    'all_items_design_status':'Candidate internal evidence only. No blanket promotion from page, schema or locator checks.',
    'remaining_checks':[
      'Independent item/figure census completeness, including headingless tasks and connected late parts',
      'Value-level qualifier checks on relevant items; objective-linked generic screens are not completed decisions',
      'Full answer accuracy and branch/diagram consistency before design selection; the independent calculation register is representative, not exhaustive',
      'Fresh blind vendor sample plus every disputed boundary, source defect and assessed-item gap'],
    'sampling_stop_rule':False}
 write(A/'textbook-open-checks-r4.json',open_checks)
 out=['# Open textbook evidence checks — NSSCAS Mathematics 8227','',
    f"{open_checks['answer_check_records']} response-item answer-location/check records; {len(missing_keys)} response items still lack one. Teaching figures are counted separately. Only {open_checks['full_subpart_author_accuracy_reviews_r5']} response items currently have the full R5subpart derivation/comparison pass; independent acceptance remains pending.",'',
    f"Published answer-page records: {open_checks['published_answer_page_records']}; explicit author-derived investigation records: {open_checks['author_derived_investigation_records']}. A derived answer is not a printed key.",'', '| Item | Source PDF page | Scope | Current answer locator |','|---|---:|---|---|']
 out += [f"| {i['item_id']} | {i['source_pdf_page']} | {i['scope']} | {i['answer_locator'].replace('|','/')} |"for i in missing_keys]
 out += ['',*open_checks['remaining_checks'],'','No sampling stop rule or full source-analysis acceptance is claimed.']
 (A/'textbook-open-checks-r4.md').write_text('\n'.join(out)+'\n')
 # Owner decision R5: independent reviewer draws its own blind sample; never author-seed one.
 assert not (A/'textbook-review-sample.json').exists(),'retired author review sample must not be regenerated'
 print(json.dumps({'catalogued_items_with_render_evidence':len(items),'discovery_leads':len(leads),'unclassified_heading_leads':result['unclassified_heading_leads']},indent=2))
if __name__=='__main__':build()
