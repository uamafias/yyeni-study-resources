"""Curate conceptual confusions separately from answering habits and scope judgements."""
import json
import re
from pathlib import Path

WS = Path(__file__).resolve().parents[1]
def read(p): return json.loads((WS/p).read_text())
def write(p,obj): (WS/p).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
refs = {r['objective_id']:r for r in read('planning/objective-reference.json')['objectives']}
candidates = {r['finding_id']:r for r in read('assessment-evidence/report-comment-candidates.json')}

# objective, confusion, discriminating test, report finding ids. All wording below
# is our interpretation; the attached source comment remains auditable internally.
curated = [
 ('1.1.1','Scarcity of resources versus merely a shortage of finished goods', 'Can a fully stocked shop exist in an economy with scarce resources? Explain why.', ['2020-007']),
 ('2.2.7','Employer association versus trade union or employee association', 'Identify whose interests each organisation represents in a wage negotiation.', ['2020-012','2021-100']),
 ('2.2.6','Collective bargaining as a negotiation process versus a workers’ organisation', 'Separate the participants from the process when representatives negotiate working conditions.', ['2020-013']),
 ('8.2.1','Real income versus disposable income', 'If deductions stay fixed but consumer prices rise, identify which measure changes and why.', ['2020-016']),
 ('5.3.2','Average revenue per unit sold versus output merely produced', 'A firm produces more units than it sells. Which quantity belongs in the average-revenue denominator?', ['2020-021']),
 ('5.4.1','Forward versus backward vertical integration', 'Classify a manufacturer acquiring a retailer and then acquiring a raw-material supplier.', ['2020-022','2023-351']),
 ('5.4.3','Economies versus diseconomies of scale', 'Classify a sustained rise in average cost as a firm expands its scale.', ['2020-023','2022-286']),
 ('3.2.4','Demand determinants versus supply determinants', 'Separate a consumer-income change from an input-cost change and identify the curve affected.', ['2020-037']),
 ('3.2.3','An imposed price control versus a shift of demand or supply', 'Hold both curves fixed and place a binding minimum wage above equilibrium; identify the excess.', ['2020-049','2024-713']),
 ('9.1.1','Resource exploitation versus unsustainable overexploitation', 'Can harvesting and replanting be exploitation while maintaining resources? State the condition.', ['2020-058']),
 ('2.1.2','Formal versus informal business activity', 'Compare registration and regulation without treating business size alone as the defining test.', ['2021-069']),
 ('3.3.1','Perfectly inelastic versus inelastic demand', 'Contrast zero quantity response with a small non-zero proportional response to a price change.', ['2021-072','2023-340']),
 ('6.2.5','Government budget balance versus trade balance', 'Classify the comparison of tax receipts with public spending separately from exports with imports.', ['2021-075','2022-171']),
 ('7.4.1','Balance of trade versus balance of payments', 'Decide whether international services and investment transactions fit within trade in goods alone.', ['2021-079','2024-703']),
 ('2.1.1','Public/private ownership sectors versus primary/secondary/tertiary production sectors', 'Classify one firm by ownership and separately by the activity it performs.', ['2021-083']),
 ('5.1.1','Profit maximisation versus merely earning more profit', 'Distinguish a profit increase from selecting the highest attainable profit under the stated conditions.', ['2021-102']),
 ('5.2.1','Production versus productivity', 'Output rises while labour hours rise faster. Decide whether production and labour productivity both increased.', ['2021-103']),
 ('8.1.3','Natural population growth versus total population growth', 'Keep births and deaths fixed and add net migration. Identify which population-growth measure changes.', ['2021-110']),
 ('4.2.1','Occupational mobility versus geographical mobility', 'Contrast changing occupation without relocating with relocating while retaining the occupation.', ['2022-145']),
 ('6.2.4','A proportional tax rate versus an identical cash deduction', 'Compare applying the same percentage to two unequal incomes with deducting the same cash amount.', ['2022-168']),
 ('9.1.1','External costs versus social costs', 'Given private cost and third-party cost, identify the external component and calculate their social total.', ['2022-191','2024-699']),
 ('7.4.3','Absolute advantage versus comparative advantage', 'Use opportunity-cost comparisons to identify comparative advantage even when one producer is more productive in both goods.', ['2023-364']),
 ('7.4.1','Foreign direct investment versus a current-account transaction', 'Contrast an overseas purchase of a domestic business with a foreign purchase of an exported service.', ['2023-362']),
 ('6.2.3','Fiscal versus monetary policy', 'Distinguish a tax-and-spending intervention from an interest-rate intervention.', ['2023-485']),
 ('8.2.1','Real income versus real income per capita', 'Hold aggregate real income fixed and increase population; identify what happens to income per person.', ['2023-470']),
 ('3.2.4','Demand determinants versus determinants of price elasticity', 'Contrast a reason the whole demand curve shifts with a reason quantity responds weakly to price.', ['2023-636']),
 ('5.3.2','Average revenue versus marginal revenue', 'Distinguish total revenue divided by units sold from the extra revenue from an additional sale.', ['2024-689']),
 ('6.1.1','Public goods versus free goods', 'Explain why public funding does not mean a good uses no scarce resources.', ['2024-724']),
 ('6.2.5','Economic investment versus depositing savings in a bank', 'Distinguish creating productive capital from moving existing money into a savings account.', ['2024-715']),
 ('6.2.2','Economic growth versus population growth', 'Contrast an increase in real output with an increase in the number of residents.', ['2024-730']),
 ('4.2.4','Transfer earnings versus transfer payments', 'Compare the minimum reward needed to retain a worker with a payment not made for current production.', ['2025-750']),
 ('2.1.2','A public limited company versus a public corporation', 'Identify ownership and shareholding separately from government ownership, despite the shared word public.', ['2025-876']),
]
entries = []
for i,(objective,confusion,test,ids) in enumerate(curated,1):
    topic,number = objective.rsplit('.',1)
    oid = f'OBJ-6145-{topic}-{int(number):02}'
    assert oid in refs
    supports = []
    for fid in ids:
        row = candidates['ER-6145-'+fid]
        supports.append({'finding_id':row['finding_id'],'source_id':row['source_id'],
                         'source_locator':row['source_locator'],
                         'comment_excerpt':row['statement'][:500],
                         'note':'This is examiner evidence of a confusion; the distinction and diagnostic are our paraphrase.'})
    entries.append({'entry_id':f'MIS-6145-{i:03}','topic_id':topic,'objective_id':oid,
                    'confusion':confusion,'discriminating_test':test,'source_evidence':supports,
                    'provenance':{'observed_error':'corpus','distinction_and_test':'judgement'}})
write('curriculum/misconceptions.json',{'register_id':'MISCONCEPTIONS-NAM-6145-NSSCO-2026',
    'curation_policy':'Only specific evidenced conceptual confusions. Generic listing, missing context, weak development, missing units and one-sided answers stay in examiner findings; they are not invented conceptual confusions.',
    'entries':entries})

# Reclassify the curated conceptual errors consistently in both evidence files.
ids = {x['finding_id'] for e in entries for x in e['source_evidence']}
findings = read('assessment-evidence/examiner_findings.json')
for row in findings['findings']:
    if row['finding_id'] in ids:
        row['classification'] = 'misconception'
        row['classification_provenance'] = 'Semantic curation in curriculum/misconceptions.json'
write('assessment-evidence/examiner_findings.json',findings)
evidence = read('assessment-evidence/assessment_evidence.json')
for row in evidence['records']:
    for error in row['common_errors']:
        if error['finding_id'] in ids:
            error['classification'] = 'misconception'
write('assessment-evidence/assessment_evidence.json',evidence)

scan_entries = [
 ('Advanced statistical estimation',r'\b(?:ordinary least squares|econometric regression|hypothesis test|confidence interval|statistical significance)\b',
  ['Estimate an econometric regression of demand.'], ['Calculate a simple percentage change in demand.']),
 ('Advanced consumer-choice theory',r'\b(?:indifference curve|marginal rate of substitution|Slutsky|Hicksian)\b',
  ['Use an indifference curve to derive demand.'], ['Explain the opportunity cost of a household decision.']),
 ('Advanced international-trade models',r'\b(?:Marshall[ -]Lerner|Heckscher[ -]Ohlin|J[ -]curve)\b',
  ['Apply the Marshall-Lerner condition.'], ['Use a simple numerical comparison of opportunity costs to identify comparative advantage.']),
 ('Advanced macroeconomic models',r'\b(?:IS[ -]LM|Phillips curve|Solow model|Taylor rule)\b',
  ['Derive the IS-LM equilibrium.'], ['Explain how an interest-rate increase may influence spending.']),
 ('Advanced investment appraisal',r'\b(?:net present value|internal rate of return|discounted cash flow|capital asset pricing)\b',
  ['Calculate net present value for this investment.'], ['Evaluate a government investment using costs, benefits and opportunity cost.']),
]
scope=[]
for construct,pattern,catch,allow in scan_entries:
    assert all(re.search(pattern,x,re.I) for x in catch)
    assert all(not re.search(pattern,x,re.I) for x in allow)
    scope.append({'construct':construct,'pattern':pattern,'applies_to':'subject',
                  'controls':{'must_catch':catch,'must_allow':allow},
                  'source':'Planner judgement from positive syllabus coverage and elementary/simple qualifiers; not an explicit syllabus prohibition.',
                  'provenance':{'boundary':'judgement','positive_scope':'syllabus'},
                  'syllabus_sentence':None})
write('curriculum/scope-scan.json',{'scope_scan_id':'SCOPE-SCAN-NAM-6145',
     'rule':'Regex catches selected advanced constructs; it cannot certify teaching depth. Positive depth limits require manual review. No syllabus exclusion was invented.',
     'entries':scope,
     'manual_review_constraints':[
       {'constraint':'Keep theory elementary and data handling basic.','source_pdf_page':6,'printed_page':2},
       {'constraint':'Use simple market situations and simple PED/PES calculations.','source_pdf_page':10,'printed_page':6},
       {'constraint':'Use simple RPI calculation and simple absolute/comparative advantage applications.','source_pdf_page':14,'printed_page':10},
       {'constraint':'Keep living-standard indicators simple.','source_pdf_page':15,'printed_page':11},
       {'constraint':'Do not create independent income/cross-elasticity units merely from glossary entries.','provenance':'judgement'},
       {'constraint':'Do include evidence-backed MC=MR profit-maximisation treatment; do not blanket-ban marginal quantities, economic rent or comparative advantage.','provenance':'syllabus plus report evidence'}]})
write('curriculum/syllabus-exclusions.json',{})
summary=read('planning/corpus-summary.json')
summary.update(curated_misconceptions=len(entries),scope_regex_controls=sum(len(e['controls']['must_catch'])+len(e['controls']['must_allow']) for e in scope))
write('planning/corpus-summary.json',summary)
print(f'{len(entries)} conceptual confusions curated; {len(scope)} scope patterns verified against catch/allow controls.')
