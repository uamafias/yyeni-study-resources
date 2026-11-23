"""Reconcile observed demand gaps and selected comparable evidence, not recipes."""
import collections
import json
import re
from analysis_sources import A, write

QUERIES={
 'M1:T1:O01:D03':('quadratic sketch',r'quadratic|stationary|sketch'),
 'M1:T1:O03:D01':('identity versus equation',r'identity|identically|equation'),
 'M1:T1:O05:D02':('reconstruct cubic from graph',r'cubic|degree\s*(?:3|three)'),
 'M1:T2:O02:D01':('arithmetic progression definition',r'arithmetic|progression|common difference'),
 'M1:T3:O01:D02':('function definition',r'function|mapping|domain|range'),
 'M1:T3:O01:D03':('one-to-one recognition',r'one.one|inverse|turning point'),
 'M1:T4:O02:D02':('tangency as repeated root',r'tangent|discriminant'),
 'M1:T5:O01:D01':('meaning of radian',r'radian|angle'),
 'M1:T5:O01:D02':('radian/degree conversion',r'radian|degrees'),
 'M1:T5:O02:D03':('circular segment area',r'\bsegment\b'),
 'M1:T6:O04:D01':('inverse principal values',r'sin.?1|cos.?1|tan.?1|principal'),
 'M1:T7:O03:D01':('unit vector construction',r'unit\s+vector'),
 'M1:T8:O03:D02':('monotonicity',r'increasing|decreasing'),
 'M2:T1:O03:D02':('quadratic divisor',r'divid|quotient'),
 'M2:T2:O02:D01':('exponential and natural-log definitions',r'exponential|natural|logarithm'),
 'M2:T6:O02:D02':('iteration failure',r'converg|diverg|oscillat'),
}
NOTES={
 'M1:T1:O01:D03':'One verified standalone sketch; more graph references can assess reading rather than producing a sketch. Three-item target not met.',
 'M1:T1:O03:D01':'Coefficient comparison is observed; explicit conceptual distinction identity/equation is not established by it. Broad hits remain unclassified.',
 'M1:T1:O05:D02':'No verified Cambridge reconstruction item found in this search. Namibia textbook PDF50 Revision Exercise1 Q5 supplies textbook-derived evidence.',
 'M1:T2:O02:D01':'Using the AP formula does not necessarily assess explaining/recognising what defines an AP. Definition demand retained syllabus-derived.',
 'M1:T3:O01:D02':'No explicit definition evidence verified. Composite/inverse calculations do not automatically prove the definition demand.',
 'M1:T3:O01:D03':'One verified explanation of inverse existence. Further function hits are discovery only; three-item target not met.',
 'M1:T4:O02:D02':'Three verified tangency/discriminant items supply comparable evidence. Ordinary intersections map to D01, not this repeated-root demand; award-accepted calculus alternatives remain visible.',
 'M1:T5:O01:D01':'A given radian angle or its conversion does not by itself assess the radian definition. No definition item verified.',
 'M1:T5:O01:D02':'One explicit supplied-radian-to-degree item verified. Angle calculations stated in radians alone do not establish conversion; three-item target not met.',
 'M1:T5:O02:D03':'Narrowed to circular-segment area. A compound sector sum is not circular-segment area; three verified diagram items.',
 'M1:T6:O04:D01':'2023 P1 Q9 held as defective. Syllabus is the authority for the principal-value demand; valid Cambridge items supply separately labelled comparable examination evidence.',
 'M1:T7:O03:D01':'Magnitude alone is not constructing a unit vector; four verified normalization items including a cuboid.',
 'M1:T8:O03:D02':'Three verified increasing/decreasing items; no inference from stationary-point classification alone.',
 'M2:T1:O03:D02':'Three verified division-by-quadratic items; division by a linear polynomial does not cover this demand.',
 'M2:T2:O02:D01':'No explicit definition item verified. Three selected graph-production examples add variety to D02, not definition coverage to D01.',
 'M2:T6:O02:D02':'Convergence of ordinary iteration is not recognising failure. Owner candidate corrected to 2021 Oct/Nov Paper22 Q6(c); conditional limit identification does not fill this gap. Goldie PDF170 supports syllabus-derived analysis.',
}

def build():
 rows=json.loads((A/'demand-dispositions.json').read_text())['rows']
 ds={d['demand_id']:d for d in json.loads((A/'demand-registry.json').read_text())['demands']}
 items=json.loads((A/'cambridge-evidence.json').read_text())['items']
 docs=[]
 for p in sorted((A/'cambridge-discovery').glob('*-*.json')):
  d=json.loads(p.read_text())
  if d['kind']=='qp':docs.append(d)
 gaps=[]
 for row in rows:
  if row['observed_part_links']:continue
  short=row['demand_id'].replace('8227:2020:','');label,rx=QUERIES[short]
  hits=[{'source_path':d['path'],'source_sha256':d['sha256'],'pdf_page':p['pdf_page']} for d in docs for p in d['pages'] if re.search(rx,p['text'],re.I)]
  gaps.append({**row,'learner_action':ds[row['demand_id']]['learner_action'],
       'cambridge_discovery_search':{'label':label,'regex':rx,'candidate_page_count':len(hits),'candidate_pages':hits,
            'corpus':'Existing 2015-2025 P1/P2 QPs; P3 also searched, but no P3 part selected. Text extraction is discovery only.'},
       'result_note':NOTES[short],'target_verified_distinct_items':3,
       'verified_comparable_count':len(row['cambridge_item_links']),
       'search_limit':'No verified item found is not a universal absence claim. Broad hits not yet transcribed/scope-reviewed remain acquisition/analysis leads, not evidence.'})
 inflexion=[{'source_path':d['path'],'pdf_page':p['pdf_page']} for d in docs for p in d['pages'] if re.search(r'inflexion|inflection',p['text'],re.I)]
 counts=collections.Counter(r['status'] for r in rows)
 corpus=json.loads((A/'cambridge-corpus-index.json').read_text())
 write(A/'gap-demand-reconciliation.json',{'gap_demands':gaps,'review_list_reconciliation':{
    'review_examples_confirmed':['M1:T1:O05:D02','M1:T5:O02:D03','M1:T7:O03:D01','M1:T8:O03:D02','M2:T1:O03:D02','M2:T6:O02:D02'],
    'principal_value':'Added held-defect gap; valid original cannot be used as observation.',
    'inflexion':'Required facet of M1:T8:O04:D02, not a new 139th demand. Other max/min facets are observed; inflexion is unobserved in NSSCAS and no verified Cambridge item found.',
    'inflexion_text_hits':inflexion,
    'additional_gaps':'Strict direct-demand annotation exposes quadratic sketch, identity/equation distinction, radian meaning/conversion and tangency gaps. Required domain/range answers, one-to-one conditions and inversion of ln(x-2) are directly assessed interpretations; their broad concepts are not incorrectly declared absent. A broad family label never fills a gap.',
    'caution':'Reviewer R13-02 examples were not an exhaustive list; compare exact demand IDs and held sources, not only the count.'},
    'counts':{'nsscas_zero_usable_demands':len(gaps),'inflexion_additional_unobserved_facet':1,
      'selected_cambridge_items':len(items),'demands_with_cambridge_items':sum(bool(r['cambridge_item_links']) for r in rows),
      'share_of_138_demands_with_cambridge_items':round(sum(bool(r['cambridge_item_links']) for r in rows)/138,6),
      'gap_demands_gaining_cambridge':sum(bool(r['cambridge_item_links']) for r in gaps),
      'thin_nsscas_demands':sum(0<len(r['observed_part_links'])<=2 for r in rows),
      'thin_nsscas_demands_gaining_cambridge':sum(0<len(r['observed_part_links'])<=2 and bool(r['cambridge_item_links']) for r in rows),
      'cambridge_diagram_items':sum(bool(i['diagram_assets']) for i in items),
      'local_document_paths':len(corpus['documents']),'unique_source_hashes':len({d['sha256'] for d in corpus['documents']}),
      'new_acquisitions_this_round':0,'statuses':dict(counts)},
    'priority_completion':'All current gaps have a search/disposition; selected verified evidence is finite. Three-item target remains unmet for explicitly listed sparse/unfound demands. Diagram and thin-demand expansion is not exhaustive.'})
if __name__=='__main__':build()
