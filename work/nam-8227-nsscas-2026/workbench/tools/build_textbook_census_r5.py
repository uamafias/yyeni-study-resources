"""Assemble explicit page census readings; pending pages never count as read."""
import json,collections
from analysis_sources import A,WB,ROOT,write,digest,evidence_path

def validate_entry(entry,items):
    for iid in entry['item_ids']+entry['continuation_item_ids']:
        assert iid in items,('census entry has no inventory record',iid)
        row=items[iid]
        assert entry['pdf_page']==row['pdf_page']or entry['pdf_page']in row['continuation_pdf_pages'],('census page/item locator disagreement',iid)
    ev=entry['source_evidence'];assert digest(evidence_path(ev['path']))==ev['sha256']
    if entry['page_status']=='prose only':assert not entry['item_ids']and not entry['continuation_item_ids']

def build():
    inv=json.loads((A/'textbook-inventory.json').read_text());items={i['item_id']:i for i in inv['items']};read={}
    segments=[]
    for p in sorted((WB/'tools/textbook-r5').glob('census-*.json')):
        data=json.loads(p.read_text())
        for row in data['pages']:
            validate_entry(row,items)
            key=(data['book_id'],row['pdf_page']);assert key not in read,('duplicate census page',key)
            read[key]={'book_id':data['book_id'],**row}
        segments.append({'book_id':data['book_id'],'chapter':data['chapter'],'input_path':str(p.relative_to(ROOT)),
          'pdf_pages':[row['pdf_page']for row in data['pages']],'source_item_ids':sorted({iid for row in data['pages']for iid in row['item_ids']}),'scope':data['scope']})
    chapters=[]
    for bid,ch in sorted({(s['book_id'],s['chapter'])for s in segments}):
        own=[s for s in segments if s['book_id']==bid and s['chapter']==ch]
        chapters.append({'book_id':bid,'chapter':ch,'pages_enumerated':len({p for s in own for p in s['pdf_pages']}),
          'source_item_ids':sorted({iid for s in own for iid in s['source_item_ids']}),'source_segments':own,
          'chapter_page_enumeration_status':'Only the enumerated segments; whole-chapter completion depends on declared boundaries and remaining pages. Independent check pending.'})
    pages=[]
    for bid,ns in [('8227-SRC-015',range(15,333)),('8227-SRC-017',range(12,586))]:
        for n in ns:
            if bid=='8227-SRC-017'and n==139:
                pages.append({'book_id':bid,'pdf_page':n,'page_status':'duplicate scan,not a new content page','duplicates_pdf_page':138,'printed_page':127});continue
            pages.append(read.get((bid,n),{'book_id':bid,'pdf_page':n,'page_status':'pending page enumeration; previous render-read count is not a census'}))
    counts=collections.Counter(row['page_status']for row in pages)
    linked={iid for row in read.values()for iid in row['item_ids']+row['continuation_item_ids']}
    missing_items=sorted(set(items)-linked)
    complete=not any(row['page_status'].startswith('pending')for row in pages)and not missing_items
    result={'status':'Author page/item census complete; final synthesis, audits and independent acceptance remain pending'if complete else'R5 working census; textbook population NOT complete',
       'coverage':{'exhaustive':complete,'exhaustive_basis':'Author page-by-page enumeration of the declared source envelope, with every inventory record linked. This is census completeness, not educational or independent acceptance.',
          'inventory_items_without_census_link':missing_items,'content_envelope_pages':len(pages)-1,'duplicate_scan_pages':1,'pages_enumerated':len(read),'page_status_counts':dict(counts),'by_book':{bid:{'pages_in_envelope':sum(r['book_id']==bid and r['page_status']!='duplicate scan,not a new content page'for r in pages),'pages_enumerated':sum(k[0]==bid for k in read)}for bid in ['8227-SRC-015','8227-SRC-017']}},
       'chapter_counts':chapters,'pages':pages,
       'figures':[i for i in inv['items']if i.get('item_kind')in['teaching-figure','given-figure']],
       'scope_limits':'Recorded pages include explicit exclusions andretained facets;envelope coverage never asserts every source task is prescribed. Goldie author scope screening is complete only when all318pages are enumerated;independent scope acceptance remains pending. Answer pages andresponse checks are recorded per retained item separately.',
       'method':'textbook-census-method-r5.md'}
    write(A/'textbook-page-census.json',result)
    print(json.dumps(result['coverage'],indent=2))
if __name__=='__main__':build()
