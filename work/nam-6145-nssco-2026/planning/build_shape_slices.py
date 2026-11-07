"""Thin original DIAGRAM/INTERP/CALC examples; not whole authored topics."""
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
import jsonschema
WS=Path(__file__).resolve().parents[1];ROOT=WS.parents[1]
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text
def read(p):return json.loads(p.read_text())
def save(p,d):
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
base=read(WS/'exemplar/topics/1.1/learning-items/topic_1.1_items.json')['items'][0]
baseclaim=read(WS/'exemplar/topics/1.1/claims/canonical_claim_ledger.json')['claims'][0]
examples={
 '3.2':{
 'objective':'OBJ-6145-3.2-03',
 'supplied_data':'Invented weekly schedules for the fictional Khomas Bean Stall in Windhoek. Price in N$ per bag: 10, 20, 30, 40, 50. Original quantity demanded in bags: 100, 80, 60, 40, 20. Quantity supplied: 20, 40, 60, 80, 100. New quantity demanded: 140, 120, 100, 80, 60. Supply conditions remain unchanged.',
 'claim':'With supply unchanged, an outward shift of demand raises equilibrium price and quantity in the supplied upward-sloping supply schedule.',
 'text':'Use these invented weekly schedules for the fictional Khomas Bean Stall in Windhoek. Price in N$ per bag: 10, 20, 30, 40, 50. Original quantity demanded in bags: 100, 80, 60, 40, 20. Quantity supplied: 20, 40, 60, 80, 100. New quantity demanded: 140, 120, 100, 80, 60. Plot price vertically and quantity horizontally. Plot the original demand and supply schedules and label D and S. Their intersection is N$30 and 60 bags. New demand D1 lies to the right: at every listed price buyers now want 40 more bags. Supply is unchanged. The new intersection is N$40 and 80 bags. This is a demand shift and a movement along supply; a price rise alone would cause a movement along demand rather than the stated shift. The result depends on the supplied supply conditions and is not a guarantee for every possible market.',
 'items':[
 ('DIAGRAM','Explain the effect of the stated increase in demand using a diagram constructed from the supplied schedules. Label both equilibria and distinguish a demand shift from movement along a curve.',7,
  'Price goes vertically in N$ per bag and quantity horizontally in bags per week. Plot D, S and D1 from the schedules. D and S meet at N$30/60 bags; D1 and S meet at N$40/80 bags. Demand has shifted right while supply has not shifted. Buyers want more at each price, so equilibrium moves up the supply curve to a higher price and quantity.',
  ['Axes/labels (1): correct price and quantity axes with units. Original curves (2): accurately plot original demand (1) and supply (1). Original equilibrium (1): N$30 and 60 bags. Change/control (1): rightward D1 with S fixed. New equilibrium (1): N$40 and 80 bags. Explanation/interpretation (1): increased demand moves equilibrium up the unchanged supply curve. Total 7.']),
 ('INTERP','Analyse the change in the equilibrium and explain why it is not caused solely by a change in the product’s own price.',4,
  'Equilibrium price rises from N$30 to N$40 and quantity from 60 to 80 bags. New demand is 40 bags higher at every listed price, so it is a shift rather than movement along the original curve. The increased price induces more supply along the unchanged supply curve.',
  ['Relationship/pattern (1): both equilibrium price and quantity increase. Evidence/comparison (1): N$30/60 to N$40/80. Explanation/reason (2): demand rises at each price (1), distinguishing a shift from an own-price movement (1). Total 4.'])]},
 '5.3':{
 'objective':'OBJ-6145-5.3-01',
 'supplied_data':'Invented weekly figures for the fictional Etosha Cloth Workshop in Namibia. Fixed cost: N$120. Total variable cost: N$180. Weekly output: 30 cloth bags. Selling price: N$14 per bag. All 30 bags are sold.',
 'claim':'Total cost equals fixed plus variable cost, and average cost equals total cost divided by output over the same period.',
 'text':'These are invented weekly figures for the fictional Etosha Cloth Workshop in Namibia. Fixed cost is N$120 and total variable cost N$180 for 30 cloth bags. Total cost is N$120 + N$180 = N$300 per week. Average cost is N$300 divided by 30 = N$10 per bag. Fixed cost does not vary with output within the stated short-run range; average fixed cost can still change. Do not add an average cost to a total cost. If 30 bags sell at N$14 each, total revenue is N$420 and average revenue is N$14 per bag. Profit is N$420 minus N$300 = N$120 for the week, using the specified cost basis. Distinguish total values per period from average values per unit; an average-cost decrease need not imply lower total cost.',
 'items':[
 ('CALC','Calculate total cost and average cost for the supplied week. Show the formula, substitution and units.',2,
  'TC = FC + VC = N$120 + N$180 = N$300 per week. AC = TC/Q = N$300/30 = N$10 per bag.',
  ['Formula and substitution/working (1): TC = 120 + 180 = N$300 per week. Formula, result and units/interpretation (1): AC = 300/30 = N$10 per bag, the cost per unit. Total 2.']),
 ('INTERP','Analyse why an average-cost figure should not be interpreted as the total weekly cost. Use the supplied data to establish the figures you need.',4,
  'Average cost is N$10 for each bag while total weekly cost is N$300 for all 30 bags. Multiplying the average by 30 recovers the total. The two figures answer different questions, so a lower average does not by itself establish a fall in total cost when output changes.',
  ['Relationship/pattern (1): average cost is cost per unit, total cost covers the whole output. Evidence/comparison (1): N$10 per bag versus N$300 for 30 bags. Explanation/reason (2): multiply average by quantity to recover total (1), so output must also be considered when comparing totals (1). Total 4.'])]}
}
report=[]
for tid,data in examples.items():
    td=WS/'exemplar/shape-slices'/tid
    cid=f'CLM-6145-{tid}-SLICE-001';oid=data['objective']
    claim=copy.deepcopy(baseclaim);claim.update(claim_id=cid,objective_ids=[oid],text=data['claim'])
    claim['evidence'][0]['locator']='NSSCO syllabus topic '+tid+'; original worked teaching data'
    items=[]
    for subtype,prompt,marks,answer,rubric in data['items']:
        x=copy.deepcopy(base);x.update(item_id=f'EX-6145-{tid}-{subtype}',objective_ids=[oid],claim_ids=[cid],subtype=subtype,
          assessment_objectives=['B'],blooms_level='Apply' if subtype in ('CALC','DIAGRAM') else 'Analyse',
          command_word={'CALC':'Calculate','DIAGRAM':'Explain','INTERP':'Analyse'}[subtype],mark_tariff=marks,
          prompt=data['supplied_data']+'\n\n'+prompt,canonical_answer=answer,marking_guidance=rubric,
          context={'sector':'retail' if tid=='3.2' else 'manufacturing','business_size':'small','ownership':None,
          'situation':'Invented Namibian teaching example','facts':[data['supplied_data']]})
        x['claims_seen']={cid:1};x['authored_hash']=hashlib.sha256(_artefact_text(x).encode()).hexdigest();items.append(x)
    ledger={'ledger_id':'EX-SLICE-'+tid,'claims':[claim]}
    dataset={'dataset_id':'EX-SLICE-'+tid,'topic_id':tid,'items':items}
    for name,obj in [('canonical_claim_ledger',ledger),('learning_items',dataset)]:
        schema=read(ROOT/f'standard/v0.2.0-draft/schemas/{name}.schema.json')
        jsonschema.Draft202012Validator(schema).validate(obj)
    save(td/'claims/canonical_claim_ledger.json',ledger)
    save(td/f'learning-items/topic_{tid}_items.json',dataset)
    (td/'TEACHING-EXAMPLE.md').write_text('# Worked teaching explanation — '+tid+'\n\nRead after attempting the separate learner items. This worked version deliberately explains the results.\n\n'+data['text']+'\n')
    report.append({'topic':tid,'items':len(items),'schema_errors':0,'claim_links_and_revisions':'pass',
     'limit':'Thin shape slice, not a complete topic: no full-topic publication verdict or graphical-renderer certification.'})
# Independent numerical checks on the actual supplied teaching data.
numeric=[]
for tid in examples:
    actual=read(WS/f'exemplar/shape-slices/{tid}/learning-items/topic_{tid}_items.json')['items']
    for item in actual:
        stem=item['prompt'];answer=item['canonical_answer']
        assert item['context']['facts'][0] in stem
        if tid=='3.2':
            def values(label):return [float(v.strip()) for v in re.search(re.escape(label)+r': ([\d, ]+)\.',stem)[1].split(',')]
            prices=values('Price in N$ per bag');d=values('Original quantity demanded in bags');s=values('Quantity supplied');d1=values('New quantity demanded')
            assert len({len(prices),len(d),len(s),len(d1)})==1
            eq=[(p,q) for p,q,qs in zip(prices,d,s) if q==qs]
            new=[(p,q) for p,q,qs in zip(prices,d1,s) if q==qs]
            assert len(eq)==len(new)==1
            for p,q in eq+new:
                assert f'N${p:g}' in answer and re.search(r'\b'+str(int(q))+r'\b',answer)
            assert not any(v in stem.lower() for v in ['their intersection is','new intersection is','this is a demand shift','equilibrium moves up'])
            numeric.append({'item':item['item_id'],'original_equilibrium':eq,'new_equilibrium':new})
        else:
            def value(label):return float(re.search(re.escape(label)+r': (?:N\$)?([\d.]+)',stem)[1])
            fc=value('Fixed cost');vc=value('Total variable cost');q=value('Weekly output');price=value('Selling price')
            tc=fc+vc;ac=tc/q
            assert f'N${tc:g}' in answer and f'N${ac:g}' in answer
            assert not any(v in stem for v in [f'N${tc:g}',f'N${ac:g} per bag','TC =','AC ='])
            numeric.append({'item':item['item_id'],'total_cost':tc,'average_cost':ac,'profit_from_supplied_data':q*price-tc})
save(WS/'exemplar/shape-slices/validation.json',{'result':'PASS','slices':report,'numerical_controls':numeric,'answer_leakage_controls':'Supplied inputs are parsed from actual saved prompts; worked results/reasoning are excluded from stems and context facts.'})
print('Original market DIAGRAM/INTERP and cost CALC/INTERP slices: schemas, claim links and numerical controls pass.')
