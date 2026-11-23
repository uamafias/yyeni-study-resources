"""Validate every intersecting text span and vector path against source crop bounds."""
import json
import pymupdf
from analysis_sources import A,ROOT,WB,write

def elements(page):
 for bi,b in enumerate(page.get_text('dict')['blocks']):
  for li,l in enumerate(b.get('lines',[])):
   for si,s in enumerate(l['spans']):
    yield {'element_id':f'text:{bi}:{li}:{si}','kind':'text','bbox':list(s['bbox']),'text':s['text']}
 for n,d in enumerate(page.get_drawings()):
  r=pymupdf.Rect(d['rect'])
  # Intersections must include the stroke of horizontal/vertical zero-area paths.
  r=r+(-0.01,-0.01,0.01,0.01)
  yield {'element_id':f'vector:{n}','kind':'vector','bbox':list(r),'path_item_count':len(d['items'])}

def validate(source_path,pdf_page,box,asset_id,exclusions=()):
 page=pymupdf.open(ROOT/source_path)[pdf_page-1];rect=pymupdf.Rect(box)
 allowed={x['element_id']:x for x in exclusions};hits=[];errors=[];intentional=[]
 for e in elements(page):
  r=pymupdf.Rect(e['bbox'])
  if not r.intersects(rect):continue
  hits.append(e)
  if rect.contains(r):continue
  if e['kind']=='text' and not e['text'].strip():
   intentional.append({**e,'reason':'Whitespace-only span contains no visible glyph. Its layout rectangle overlaps the crop but no text is truncated.'});continue
  if e['element_id'] in allowed:
   assert allowed[e['element_id']]['reason'];intentional.append({**e,**allowed[e['element_id']]});continue
  errors.append(e)
 assert not errors,('crop containment',asset_id,box,errors)
 return {'asset_id':asset_id,'source_path':source_path,'pdf_page':pdf_page,'crop_box_pdf_points':box,
         'intersecting_elements':len(hits),'contained_elements':len(hits)-len(intentional),
         'intentional_exclusions':intentional,'status':'pass'}

def check_all():
 assets=json.loads((A/'asset-index.json').read_text())['assets']+[a for i in json.loads((A/'cambridge-evidence.json').read_text())['items'] for a in i['diagram_assets']]
 assets=list({a['asset_id']:a for a in assets}.values())
 rows=[validate(a['source_path'],a['pdf_page'],a['crop_box_pdf_points'],a['asset_id'],a.get('intentional_exclusions',[])) for a in assets]
 assert len(rows)==39
 write(WB/'checks/crop-containment.json',{'method':'Every intersecting PDF text-span/vector-path bounding box must be wholly contained, or explicitly excluded with a reason; 0.01pt expansion includes zero-area vector strokes.',
       'rows':rows,'source_limit':'PDF object bounds are structural evidence. Author image inspection is still required for raster content and spatial meaning.'})
 return rows
if __name__=='__main__':print('Validated',len(check_all()),'crops')
