"""Build item inventory from rendered-page author annotations, not OCR classification."""
import collections,json,re
from analysis_sources import A,WB,ROOT,digest,write
from textbook_inventory_inputs import GOLDIE,YM,GOLDIE_WORKED,GOLDIE_OTHER
from textbook_mapping_refinements import REFINEMENTS,SKETCH_OVERRIDES,NOTE_OVERRIDES,REPRESENTATION_OVERRIDES
from textbook_source_cautions import CAUTIONS
from build_curriculum import QUALIFIERS,oid

def numbers(s):
 result=[]
 for v in s.split(','):
  if '-' in v:a,b=map(int,v.split('-'));result+=list(range(a,b+1))
  else:result.append(int(v))
 return result

def did(alias):
 m,t,o,d=map(int,alias.split('.'));return f'8227:2020:M{m}:T{t}:O{o:02}:D{d:02}'

def aliases(s):return [did(x) for x in s.split(',') if x]

def build():
 holdings=json.loads((A/'source-holdings.json').read_text())['records']
 sources={r['document_id']:r for r in holdings}
 goldie=sources['8227-SRC-015'];ym=sources['8227-SRC-017']
 for r in [goldie,ym]:assert digest(ROOT/r['path'])==r['sha256']
 demands=json.loads((A/'demand-registry.json').read_text())['demands'];valid={r['demand_id'] for r in demands}
 gp=json.loads((A/'textbook-goldie-population-leads.json').read_text())['items']
 gl={(x['exercise'],int(x['item_number'])):x for x in gp}
 refinements={}
 for l in REFINEMENTS.strip().splitlines():
  if not l.strip():continue
  book,ch,ex,ns,ds=l.split('|')
  for n in numbers(ns):refinements[book,ch,ex,n]=aliases(ds)
 # Locate answer sections in the original books, not a guessed all-book offset.
 gd=json.loads((A/'textbook-goldie-discovery.json').read_text())['pages']
 gh=[]
 for page in gd[332:369]:
  for m in re.finditer(r'Exercise\s+(\d+[A-Z])',page['text']):gh.append((page['pdf_page'],m[1]))
 ganswers={}
 for i,(pg,ex) in enumerate(gh):
  # Ignore a repeated/chapter-misprinted header in later answers, retaining the first real section.
  if ex in ganswers:continue
  end=gh[i+1][0] if i+1<len(gh) else pg
  ganswers[ex]=list(range(pg,end+1))
 yanswers={};chapter=1;current=None
 for pg in range(587,658):
  page=json.loads((A/f'ocr/ymxc/page-{pg:04}.json').read_text())
  for line in page['lines']:
   t=line['text'];m=re.match(r'^Chapter\s*(\d+)\s*:',t,re.I)
   if m:chapter=int(m[1]);current=None
   m=re.match(r'^(?:Try|Lry)\s+Now\s*(\d+)',t,re.I)
   if m:current=(chapter,'Try Now',int(m[1]));yanswers.setdefault(current,[])
   m=re.match(r'^(Revision\s+Exercise|Exercise)\s*(\d+(?:\.\d+)?)',t,re.I)
   if m:current=(chapter,('Revision Exercise' if m[1].lower().startswith('revision') else 'Exercise')+' '+m[2],None);yanswers.setdefault(current,[])
   if current is not None and pg not in yanswers[current]:yanswers[current].append(pg)
 items=[]
 caution_map=collections.defaultdict(list)
 for line in CAUTIONS.strip().splitlines():
  if not line.strip():continue
  book,ch,ex,ns,kind,action,reason=line.split('|')
  for n in numbers(ns):caution_map[book,ch,ex,n].append({'kind':kind,'disposition':action,'reason':reason})
 exam_pages={p for g in json.loads((WB/'checks/r3/ym-revision-render-manifest.json').read_text()) for p in g['pdf_pages']}
 def record(book,ch,ex,n,page,ds,representation,sketch,exam,note,worked=False):
  key=(book,str(ch),ex,n);ds=refinements.get(key,ds);sketch=SKETCH_OVERRIDES.get(key,sketch);note=NOTE_OVERRIDES.get(key,note)
  representation=REPRESENTATION_OVERRIDES.get(key,representation)
  assert set(ds)<=valid,(key,set(ds)-valid)
  src=goldie if book=='Goldie' else ym
  pp=page-14 if book=='Goldie' else page-11 if page<=138 else 127 if page==139 else page-12
  scope='in-scope';disposition='include as internal analysis evidence';excluded=[]
  if (book,ch,ex,n) in [('YM',4,'Exercise 4.2',3),('YM',9,'Exercise 9',6),('YM',8,'Example',26)]:
   scope='in-scope-parts-only';excluded=['Only valid stated parts/specialisations count; see item note.']
  if (book,ch,ex,n)==('YM',9,'Exercise 9',11):
   disposition='source ambiguity: hold as design exemplar until transformed axes are clarified'
  cautions=caution_map[key]
  if any(c['disposition']=='hold' for c in cautions):disposition='source ambiguity: hold original as design exemplar pending correction'
  if any(c['disposition']=='partial' for c in cautions):scope='in-scope-parts-only';excluded += [c['reason'] for c in cautions if c['disposition']=='partial']
  if book=='Goldie' and not worked:
   akey=ganswers.get(ch,[])
   # ch is the exercise for this book; retain original item numbering.
   answer={'available':True if akey else None,'source_path':src['path'],'source_sha256':src['sha256'],
        'pdf_pages':akey,'printed_pages':[p-14 for p in akey],'locator':f'Answers, Exercise {ch}, Question {n}',
        'verification':'Answer section and printed item numbers author-inspected on rendered pages; presence of every item answer and answer accuracy are not certified by section availability.'}
   if (ch,n) in [('6B',2),('3E',3),('5B',12)]:answer['available']=False;answer['status']='not applicable (show/prove)';answer['verification']='The task asks show/prove; the worked reasoning is required instead of a standalone numerical answer key.'
   chapter=int(str(ch)[:-1]);exercise='Exercise '+ch
  else:
   chapter=int(ch);exercise=ex
   if ex=='Example' or worked:
    more={ (6,36):[314,315],(7,41):[370,371],(2,33):[81,82] }.get((chapter,n),[page])
    answer={'available':True,'source_path':src['path'],'source_sha256':src['sha256'],'pdf_pages':more,
      'printed_pages':[p-14 if book=='Goldie'else p-11 if p<=138 else p-12 for p in more],'locator':f'Example {n}, inline worked solution',
      'verification':'Worked mathematics author-read on rendered example pages; not independently reviewed.'}
   else:
    if ex=='Try Now':target=(chapter,'Try Now',n)
    elif ex.startswith('Try Now '):target=(chapter,'Try Now',int(ex.split()[-1]))
    else:target=(chapter,ex,None)
    akey=yanswers.get(target,[])
    answer={'available':True if akey else None,'source_path':src['path'],'source_sha256':src['sha256'],
       'pdf_pages':akey,'printed_pages':[p-12 for p in akey],
       'locator':f'Answers, Chapter {chapter}, {ex}'+(f' {n}' if ex=='Try Now' else f', item {n}'),
       'verification':'OCR section-heading discovery; actual answer-page image check pending. Unknown means not yet located, not absent.'}
  item={'item_id':f'8227:TB:{book}:C{chapter}:{exercise.replace(" ","-")}:{n}',
    'book_id':src['document_id'],'book':src.get('title',src['path']),'chapter':chapter,'exercise':exercise,'item_number':str(n),
    'source_path':src['path'],'source_sha256':src['sha256'],'pdf_page':page,'printed_page':pp,
    'continuation_pdf_pages':{('Goldie','2D','-',6):[67],('Goldie','2D','-',14):[69],('YM','3','Try Now',1):[110],('YM','2','Try Now 33',1):[83],('YM','4','Try Now 8',1):[162],('YM','2','Example',33):[82],('YM','6','Example',8):[278],('YM','9','Investigation exponential',1):[426],('YM','9','Investigation logarithmic',1):[429],('YM','4','Investigation transformed trig graphs',1):[170],('YM','11','Example',6):[488],('YM','3','Investigation transformations',3):[130],('YM','3','Investigation transformations',6):[132]}.get(key,[]),
    'assessed_8227_demand_ids':ds,'objective_ids':sorted({d.rsplit(':D',1)[0] for d in ds}),
    'mapping_depth':'Individual item record. Historical range seeds expanded; author corrections applied per item. Exact-set reclassification remains subject to a fresh independent sample.',
    'representation':representation,'sketch_response_required':sketch,'exam_style':exam,
    'answer_key':answer,'scope_check':{'status':scope,'basis':note,'limits_considered':['8227:LIMIT'+str(i).zfill(2) for i in range(1,9)]+['8227:QUAL'+str(i).zfill(2)for i in range(1,12)],'excluded_or_qualified_parts':excluded},
    'disposition':disposition,'notes':note,'defects':cautions,
    'design_use_status':'candidate evidence; answer/representation and independent classification checks required before selecting as design evidence',
    'source_check':'Author inspected original rendered problem mathematics/visuals; independent classification pending',
    'learner_display':False,'rights':'Internal textbook evidence only; exact textbook problem/solution learner reproduction not authorised.'}
  item['evidence_role']='directly related assessed practice'if ds else'prerequisite/supporting practice; no direct demand coverage claimed'
  item['scope_check']['qualifier_screen']=[{'qualifier_id':'8227:'+code,'rule':rule,
     'applicability':'objective-linked; value/part screening required'if oid(short)in item['objective_ids']else 'not linked to assessed objective',
     'status':'author scope note; independent check pending'}for code,short,rule in QUALIFIERS if code.startswith('QUAL')]
  item['exam_style_basis']='Explicit past-paper attribution in Goldie or YM section headed Exam-Style/Revision. Connected multipart structure alone does not set this flag.'
  item['answer_key']['verification_status']='unverified accuracy; section locator is not answer acceptance'
  items.append(item)
 for l in GOLDIE.strip().splitlines():
  if not l.strip():continue
  ex,ns,ds,rep,sketch,exam,note=l.split('|',6)
  for n in numbers(ns):
   lead=gl[ex,n];record('Goldie',ex,'-',n,lead['pdf_page'],aliases(ds),rep,sketch=='yes',exam=='yes',note)
 for l in GOLDIE_WORKED.strip().splitlines():
  if not l.strip():continue
  ch,n,pg,continuations,ds,rep,sketch,scope,note=l.split('|',8)
  record('Goldie',int(ch),'Example',int(n),int(pg),aliases(ds),rep,sketch=='yes',False,note,worked=True)
  row=items[-1];more=[int(p)for p in continuations.split(',')if p]
  row['continuation_pdf_pages']=more;row['answer_key']['pdf_pages']=[int(pg),*more]
  row['answer_key']['printed_pages']=[p-14 for p in [int(pg),*more]]
  row['scope_check']['status']=scope
  row['answer_key']['verification']='Inline worked solution visually author-read with original example,not independently reviewed.'
  if scope=='out-of-scope':row['disposition']='exclude from 8227 assessed scope; retain source-analysis evidence only'
 for l in GOLDIE_OTHER.strip().splitlines():
  if not l.strip():continue
  ch,unit,n,pg,continuations,ds,rep,sketch,scope,note=l.split('|',9)
  record('Goldie',int(ch),unit,int(n),int(pg),aliases(ds),rep,sketch=='yes',False,note,worked=True)
  row=items[-1];row['continuation_pdf_pages']=[int(p)for p in continuations.split(',')if p]
  row['scope_check']['status']=scope
  row['answer_key'].update(available=None,pdf_pages=[],printed_pages=[],locator='No separate answer key located for this boxed prompt/activity',verification='Original prompt visually read; independent derivation and any printed answer location remain pending.',verification_status='not selected as accepted design evidence')
  if scope=='out-of-scope':row['disposition']='exclude from 8227 assessed scope; retain source-analysis evidence only'
 for l in YM.strip().splitlines():
  if not l.strip():continue
  ch,ex,ns,page,ds,rep,sketch,note=l.split('|',7)
  for n in numbers(ns):record('YM',int(ch),ex,n,int(page),aliases(ds),rep,sketch=='yes',ex.startswith('Revision') or int(page) in exam_pages,note)
 from textbook_repairs_r4 import apply
 items,duplicate_aliases=apply(items)
 # Verify the original discovered exercise population before adding the explicit
 # R5 page-census discoveries from previously over-broad chapter exclusions.
 assert len([i for i in items if i['book_id']==goldie['document_id']and i['exercise'].startswith('Exercise ')])==len([i for i in gp if int(i['exercise'][:-1])<7 or i['exercise'] in ['10A','10B','10C']])
 from apply_textbook_r5 import apply as apply_r5
 items=apply_r5(items)
 from apply_textbook_r6 import apply as apply_r6
 items=apply_r6(items)
 from apply_textbook_figures_r6 import apply as apply_figures_r6
 items=apply_figures_r6(items)
 from apply_textbook_source_repairs_r7 import apply as apply_source_r7
 items=apply_source_r7(items,wb=WB)
 from apply_textbook_notes_r7 import apply as apply_notes_r7
 items=apply_notes_r7(items)
 ids=[i['item_id'] for i in items];assert len(ids)==len(set(ids)),[k for k,n in collections.Counter(ids).items() if n>1]
 rows=[]
 for d in demands:
  supported=[i for i in items if d['demand_id'] in i['assessed_8227_demand_ids'] and i['scope_check']['status']!='out-of-scope' and not i['disposition'].startswith('source ambiguity')]
  teaching=[i for i in items if d['demand_id']in i.get('teaches_8227_demand_ids',[])and i['scope_check']['status']!='out-of-scope']
  figures=[i for i in teaching if i.get('item_kind')in ['teaching-figure','given-figure']]
  exposition=[i for i in teaching if i.get('item_kind')not in ['teaching-figure','given-figure']]
  rows.append({'demand_id':d['demand_id'],'learner_action':d['learner_action'],'textbook_item_count':len(supported),
       'teaching_figure_count':len(figures),'teaching_figure_ids':[i['item_id']for i in figures],
       'teaching_exposition_count':len(exposition),'teaching_exposition_ids':[i['item_id']for i in exposition],
       'given_diagram_or_graph_item_count':sum(i['representation'] in ['diagram','graph'] for i in supported),
       'sketch_response_item_count':sum(i['sketch_response_required'] for i in supported),
       'visual_item_count':sum(i['representation'] in ['diagram','graph'] or i['sketch_response_required'] for i in supported),
       'item_ids':[i['item_id'] for i in supported],
       'coverage_interpretation':'textbook_item_count counts directly assessed practice only. Teaching figures and unprompted explanatory derivations are counted separately; neither becomes an assessed task or certifies full syllabus/examination coverage or independent answer acceptance.'})
 chapters=[]
 for bid in [goldie['document_id'],ym['document_id']]:
  for ch in sorted({i['chapter'] for i in items if i['book_id']==bid}):
   subset=[i for i in items if i['book_id']==bid and i['chapter']==ch]
   mapping_complete=all(i.get('mapping_review_status_r5','').startswith('author reclassified')for i in subset)
   answers_complete=all(i.get('answer_accuracy_status_r5','').startswith(('author independently derived every explicit subpart','No separate learner response','Excluded whole task:'))for i in subset)
   chapters.append({'book_id':bid,'chapter':ch,'catalogued_items':len(subset),
      'completed_population':'Individually enumerated retained source items/figures;see page census for completeness'if mapping_complete else'Formal exercise and exam-style/revision question sets plus individually completed R5segments',
      'author_item_mapping_complete':mapping_complete,'author_response_or_figure_check_complete':answers_complete,
      'whole_chapter_complete':False,'remaining':'Independent population/classification/answer acceptance and final cross-book family/demand synthesis remain open.'if mapping_complete and answers_complete else'Individual source census,assessed/component mapping,value-level decisions andanswer checks remain open for uncompleted items;independent acceptance and final synthesis also pending.'})
 result={'schema_version':'8227-source-analysis-r5-working','status':'bounded author inventory; whole-book source analysis incomplete',
   'books':[{'document_id':r['document_id'],'title':r.get('title'), 'path':r['path'],'sha256':r['sha256'],
             'edition':r.get('edition'),'rights':'internal evidence only'} for r in [goldie,ym]],
   'population_unit':'One original numbered question or worked Example/Try Now block; multiple numbered questions within a set are separate. Explicit boxed prompts, activities and investigations have stable local labels when the source has no question number. Explanatory worked illustrations are labelled separately. Subparts and cosmetic variants do not inflate counts. None of these counts is a problem-type count.',
   'coverage':{'catalogued_items':len(items),'teaching_or_given_figure_records':sum(i.get('item_kind')in ['teaching-figure','given-figure']for i in items),'problem_or_worked_items':sum(i.get('item_kind')not in ['teaching-figure','given-figure']for i in items),'by_book':dict(collections.Counter(i['book_id'] for i in items)),
        'demands_with_support':sum(r['textbook_item_count']>0 for r in rows),'demands_without_support':[r['demand_id'] for r in rows if not r['textbook_item_count']],
        'formal_stop_rule_applied':False,'stop_rule_reason':'No stop rule is claimed. Routine and mandatory visual/gap/thin populations have not yet been fully reconciled.',
        'exhaustive':False,'chapters':chapters,
        'count_limits':'Counts are source items, not distinct problem types. Repeated Cambridge/textbook questions remain duplicates for breadth purposes. Answers located by heading are not verified solutions.'},
   'items':items,'duplicate_aliases':duplicate_aliases,'per_demand':rows,
   'exam_style_definition':'Source-labelled exam-style: explicit past-paper attribution or a YM Exam-Style/Revision section; not a claim of observed NSSCAS assessment or multipart complexity.',
   'scope_exclusions':[{'book_id':goldie['document_id'],'sections':['3.5 general trigonometric solution forms (introductory principal-value ranges remain relevant teaching support)','7 negative/rational-power infinite binomial series and partial-fractions decomposition only: section7.2and explicit retained subparts/prompts are included in census-Goldie-C7.json','8 additional original general substitution/parts,unsupplied partial-fractions techniques and inverse-trig calculus;retained parts and reference figures are individually censused on198–230,with author scope judgements awaiting independent acceptance','9 general separation-of-variables solution methods only;rate formation,connected rates,explicit-gradient primitives,provided identity checks and qualified implicit verification are retained individually on231–247;both investigations are supporting model evidence','10.5–10.8 additional vector-line-equation/skew-line methods only;prescribed ordinary vector/Cartesian facets and separately labelled given-direction support on272–293are individually retained by the twoC10boundary censuses;formal3Dline construction/classification/projectionmethods remain additional','11 complex-number goals/methods only:all294–332pages screened;puretrig,realpolynomialandprerequisite/vectorfacetsretainedindividuallyincensus-Goldie-C11.json'],
                       'reason':'Outside prescribed 8227 demands or LIMIT01/02/07/08; no claim whole Cambridge A-Level book fits NSSCAS.'}],
   'next_required':'Reconcile any headingless or connected-part omissions in the final independent page/item/figure census; complete value-level qualifier and answer-accuracy checks before design use; independent 10% classification sample plus disputes. All discovered headings are disposed, but do not call step 2 complete from this inventory.'}
 # Book-wide answer conventions are source facts,kept apart from official
 # examination marking rules and from an individual stem's instructions.
 for path in sorted((WB/'tools/textbook-r5').glob('census-*.json')):
  convention=json.loads(path.read_text()).get('book_answer_conventions')
  if convention:
   ev=convention['evidence'];assert digest(ROOT/ev['path'])==ev['sha256']
   book=next(b for b in result['books']if b['document_id']==convention['book_id'])
   assert 'source_answer_conventions'not in book,('duplicate book convention record',convention['book_id'])
   book['source_answer_conventions']=convention
 write(A/'textbook-inventory.json',result)
 out=['# Textbook item inventory — NSSCAS Mathematics 8227','',
      '**Bounded author inventory. Whole-book source analysis remains incomplete.** No sampling stop rule is claimed. All listed question mathematics/visuals were checked on rendered source pages. Answer-key heading locations are recorded separately from answer correctness.','',
      f'{len(items)} source items across both books; {result["coverage"]["demands_with_support"]} of 138 demands have related items. These are not distinct recipe counts or full examination coverage. Textbooks remain internal evidence.','',
      '| Book | Chapter | Exercise | Item | Printed / PDF page | Direct demands | Given / response | Answer locator | Scope |','|---|---|---|---|---|---|---|---|---|']
 for i in items:
  out.append(f'| {i["book_id"]} | {i["chapter"]} | {i["exercise"]} | {i["item_number"]} | {i["printed_page"]} / {i["pdf_page"]} | {", ".join(i["assessed_8227_demand_ids"])} | {i["representation"]}; sketch={i["sketch_response_required"]} | PDF {i["answer_key"]["pdf_pages"]}; {i["answer_key"]["verification"]} | {i["scope_check"]["status"]}: {i["notes"].replace(chr(124),chr(92)+chr(124))} |')
 out+=['','## Demand support counts','',
       '| Demand | Items | Given diagrams/graphs | Sketch responses |','|---|---|---|---|']
 out += [f'| {r["demand_id"]} — {r["learner_action"]} | {r["textbook_item_count"]} | {r["given_diagram_or_graph_item_count"]} | {r["sketch_response_item_count"]} |' for r in rows]
 out+=['','## Completion limits','',result['next_required'],'','No-textbook-support identifiers refer only to this inspected population, not proven absence from either book. Goldie sections outside scope are listed in the JSON. The Namibian PDF repeats printed p127 at PDF138/139; the duplicate scan is not counted twice.','']
 (A/'textbook-inventory.md').write_text('\n'.join(out))
 print(json.dumps(result['coverage'],indent=2))
if __name__=='__main__':build()
