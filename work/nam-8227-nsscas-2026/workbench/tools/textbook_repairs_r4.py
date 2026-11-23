"""Item-specific rendered-page corrections, never range-level reassignment."""
import json
from analysis_sources import A,WB,ROOT,digest

def apply(items):
 aliases=[]
 by={i['item_id']:i for i in items}
 def item(book,ch,ex,n):return by[f'8227:TB:{book}:C{ch}:{ex}:{n}']
 duplicate=item('YM',6,'Revision-Exercise-6',2);original=item('YM',6,'Try-Now-15',2)
 original['duplicate_source_occurrences']=[{'alias_item_id':duplicate['item_id'],'pdf_page':duplicate['pdf_page'],'exercise':duplicate['exercise'],'answer_key':duplicate['answer_key'],'reason':'Same square-root curve and angle-between-tangents question; counted once.'}]
 aliases.append({'alias_item_id':duplicate['item_id'],'canonical_item_id':original['item_id'],'pdf_page':duplicate['pdf_page'],'counted_in_population':False})
 items=[i for i in items if i['item_id']!=duplicate['item_id']]
 # A second exact repetition, newly confirmed on rendered343and344. Do not
 # count a second source question as additional breadth or a different demand.
 original=item('YM',7,'Try-Now-20',1)
 repeated={'alias_item_id':'8227:TB:YM:C7:Try-Now-19:2','canonical_item_id':original['item_id'],'pdf_page':343,'counted_in_population':False,'reason':'Identical y=x^3,y8..27,y-axis area question repeats on344.'}
 aliases.append(repeated)
 original.setdefault('duplicate_source_occurrences',[]).append(dict(repeated,exercise='Try Now 19',answer_key_pdf_page=627))

 # Exact page locators checked in this repair. Other section spans remain explicitly pending.
 exact=[('Goldie',5,'Exercise-5C',2,346),('Goldie',3,'Exercise-3B',4,340),
  ('YM',1,'Exercise-1',12,591),('YM',3,'Try-Now',12,600),('YM',3,'Try-Now',15,600),
  ('YM',8,'Try-Now',12,634),('YM',6,'Exercise-6',3,624),('YM',6,'Try-Now-35',1,623),
  ('YM',11,'Try-Now-42',1,649),('YM',4,'Exercise-4.2',5,614),('YM',13,'Try-Now-2',1,653),
  ('YM',7,'Try-Now',27,628),('YM',7,'Try-Now',26,628),('YM',3,'Try-Now',3,598)]
 for b,ch,ex,n,pg in exact:
  i=item(b,ch,ex,n);a=i['answer_key'];a['pdf_pages']=[pg];a['printed_pages']=[pg-14]if b=='Goldie'else['A'+str({591:5,598:12,600:14,614:28,623:37,624:38,628:42,634:48,649:63,653:67}[pg])]
  a['verification']='Author read the exact answer page and corresponding original problem; defect/correction recorded below. Independent check pending.'
  a['verification_status']='author checked; source defect recorded; not accepted uncorrected design evidence'
  a['defect_records']=i['defects']
 for i in items:
  if i['book_id']=='8227-SRC-017' and i['chapter']==8 and i['exercise']=='Try Now 9' and i['item_number']=='2':
   i['scope_check']['status']='in-scope-parts-only';i['scope_check']['excluded_or_qualified_parts'].append('Part(e) y=-(1/3)|x|+2 has non-integer modulus coefficient, outside QUAL01 original scope; retain other permitted subparts or specialise coefficients.')
   i['scope_check']['qualifier_screen'][0]['status']='QUAL01 applied: exclude original part(e) from scope support'
  if i['book_id']=='8227-SRC-017' and i['pdf_page']==111:i['scan_annotation']='Handwritten answers from a prior owner are present; not printed/verified solutions.'
 answer_checks=json.loads((WB/'tools/textbook_answer_checks_r4.json').read_text())
 for i in items:
  if i['item_id']not in answer_checks:continue
  check=answer_checks[i['item_id']]
  i['answer_key'].update({k:v for k,v in check.items()if k not in ['evidence_sheets']})
  i['answer_key']['author_check']=check
  i['answer_key']['source_defects']=i['defects']
 return items,aliases
