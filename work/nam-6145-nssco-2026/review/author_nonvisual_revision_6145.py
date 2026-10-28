#!/usr/bin/env python3
"""One-shot, snapshot-guarded authoring of the approved 37 nonvisual slots.

Never rerun over subsequent reviewer edits. This is a record of this authoring pass,
not a subject regeneration script. Planning and visual artefacts are read-only.
"""
import copy
import hashlib
import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
WS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text

# key, teaching block, prompt, answer, content-specific mark allocation, second claim
ROWS = [
('industrial-action','2.2-B06','Define industrial action.','Collective action by workers to put pressure on an employer over a workplace dispute, such as stopping work or deliberately restricting normal work.','Meaning: collective worker action over a workplace dispute (1); distinguishing feature: pressure through stopping or restricting normal work (1).','A strike stops work, whereas a go-slow deliberately reduces the pace of work.'),
('currency-issue','2.3.5-B01','Explain why a central bank issues notes and coins.','It provides a recognised currency for payments (1), giving buyers and sellers a common means of settling transactions rather than relying on barter (1).','Reason: provision of recognised currency (1); link: a common means of settling purchases or debts without barter (1).','Issuing currency does not create the real resources needed to produce goods and services.'),
('government-banker','2.3.5-B01','Explain why a government uses the central bank as its banker.','The central bank holds government accounts (1), through which government can receive revenue and make payments for public spending (1).','Reason: government accounts are held by the central bank (1); link: these accounts handle government receipts and payments (1).','Acting as banker to government is distinct from providing ordinary retail accounts to households.'),
('last-resort','2.3.5-B01','Explain why a central bank may lend to a solvent commercial bank facing a temporary shortage of cash.','Emergency lending can help the bank meet withdrawals and payments (1), reducing the risk that its cash shortage undermines depositors’ confidence in the banking system (1).','Reason: temporary liquidity enables withdrawals or payments to be met (1); link: this can support depositor confidence and financial stability (1). The prompt concerns a solvent bank, not guaranteed rescue of every failing bank.','Lender-of-last-resort support addresses temporary liquidity needs; it is not a guarantee that every bank or investment will be rescued.'),
('bank-supervision','2.3.5-B01','Explain why a central bank supervises commercial banks.','Supervision checks banks’ financial soundness and risk-taking (1), helping reduce the risk of failures that could harm depositors and disrupt payments (1).','Reason: checking bank soundness or risk-taking (1); link: lower risk to depositors or banking-system stability (1). Do not credit a guarantee that no bank can fail.','Bank supervision aims to support a sound banking system rather than guarantee that every investment succeeds.'),
('repo-rate','2.3.5-B01','Define the repo rate.','The interest rate charged by the central bank (1) when it lends to commercial banks (1).','Meaning: an interest rate charged by the central bank (1); distinguishing feature: on lending to commercial banks (1), rather than the rate a shop pays on its ordinary bank loan.','Commercial banks’ own lending rates are distinct from the repo rate.'),
('nsx-liquidity','2.3.5-B02','Explain why trading existing shares on a stock exchange can make share ownership more liquid.','An investor has a market in which to find a buyer for existing shares (1), so the investment can be converted into cash if a willing buyer is found (1).','Reason: access to a market for resale of existing holdings (1); link: conversion of shares into cash when a buyer is available (1). No guaranteed sale price is implied.','Payment for an existing share normally goes to its selling holder, not to the issuing company.'),
('nsx-capital','2.3.5-B02','Explain why a stock-exchange listing can help a company raise new capital through a new share issue.','A listing gives the company access to investors in its shares (1), so a new issue raises funds for the company if investors buy those newly issued shares (1).','Reason: access to share investors (1); link: their purchases of newly issued shares provide company finance (1). Listing alone and resale of existing shares do not guarantee new funds.','New share issuance and resale of existing shares have different immediate recipients of the purchase money.'),
('ped-formula-meaning','3.3.3-B01','Explain why price elasticity of demand divides the percentage change in quantity demanded by the percentage change in price, rather than dividing the raw changes.','Percentage changes measure each change relative to its starting value (1), so their ratio measures demand responsiveness without depending on the currency or quantity units chosen (1).','Reason: each change is relative to its starting value (1); because/link: the ratio is independent of the measurement units and compares proportional responsiveness (1).','Changing from dollars to cents must not change the measured price elasticity of demand.'),
('pes-formula-meaning','3.3.3-B02','Explain why price elasticity of supply uses percentage changes in quantity supplied and price rather than raw changes.','Each percentage change expresses movement relative to its starting value (1), so the ratio compares proportional supply responsiveness without changing merely because output or currency units are rescaled (1).','Reason: relative rather than raw changes (1); because/link: this makes the responsiveness measure independent of currency or output units (1).','Changing output measurement from individual units to dozens must not by itself change price elasticity of supply.'),
('occupational-mobility','4.1-B01','Define occupational mobility of labour.','The ease with which workers can move (1) from one type of occupation to another (1).','Meaning: ease of worker movement (1); distinguishing feature: between different occupations, rather than just between locations (1).','Training that enables a clerk to become a technician can improve occupational mobility.'),
('geographical-mobility','4.1-B01','Define geographical mobility of labour.','The ease with which workers can move (1) from one area to another for work (1).','Meaning: ease of worker movement (1); distinguishing feature: between geographical areas for work (1), rather than necessarily changing occupation.','Moving to another town while keeping the same occupation concerns geographical mobility.'),
('gross-pay','4.2-B01','Define gross pay.','A worker’s total earnings (1) before any deductions are taken off (1).','Meaning: total earnings from work (1); distinguishing feature: before deductions (1).','Gross pay differs from net pay because deductions have not yet been subtracted.'),
('net-pay','4.2-B01','Define net pay.','A worker’s take-home earnings (1), equal to gross pay minus deductions (1).','Meaning: take-home earnings (1); distinguishing feature: gross pay after deductions (1).','Income tax and relevant contributions can be deductions from gross pay.'),
('time-rate','4.2-B01','Define time-rate payment.','Payment for work at an agreed rate (1) for each unit of time worked, such as an hour, week or month (1).','Meaning: payment at an agreed rate (1); distinguishing feature: based on time worked, not units produced (1).','A wage per hour and a salary per month are time-based payment arrangements.'),
('piece-rate','4.2-B01','Define piece-rate payment.','Payment for work at an agreed rate (1) for each unit of output produced (1).','Meaning: payment at an agreed rate (1); distinguishing feature: based on units produced, rather than time worked (1).','Piece-rate payment differs from commission, which is linked to sales value.'),
('value-added','5.1-B03','Define value added.','The value of a firm’s output (1) minus the cost of materials and services bought from other firms to produce it (1).','Meaning: value of output (1); distinguishing feature: deduct purchased materials and services/intermediate inputs (1). Do not accept profit, which subtracts all relevant costs.','Value added is not profit because it does not subtract all production costs, such as the firm’s own wage bill.'),
('total-revenue-definition','5.3.2-B01','Define total revenue.','The amount received from sales; for a single product at one price, price multiplied by quantity sold.','Meaning: total sales receipts (1); distinguishing feature: price multiplied by quantity sold when all units sell at one price (1). Unsold output and loans are not sales receipts.','Producing an item without selling it does not add to current sales receipts.'),
('average-revenue-definition','5.3.2-B02','Define average revenue.','Total revenue divided by quantity sold.','Meaning: revenue per unit sold (1); distinguishing feature: total revenue divided by sold quantity (1), rather than extra revenue from one additional sale.','Average revenue is not marginal revenue or profit per unit.'),
('external-economies','5.4.2-B01','Define external economies of scale.','Reductions in a firm’s long-run average cost (1) arising from growth or concentration of the industry, rather than expansion of that firm alone (1).','Meaning: lower long-run average cost (1); distinguishing feature: industry growth or concentration creates the advantage outside the individual firm (1).','A shared local pool of skilled workers can lower firms’ recruitment or training costs as an industry expands.'),
('external-diseconomies','5.4.3-B01','Define external diseconomies of scale.','Increases in a firm’s long-run average cost (1) arising from growth or concentration of the industry outside the firm, such as congestion or greater competition for local resources (1).','Meaning: higher long-run average cost (1); distinguishing feature: industry growth or concentration causes the cost pressure outside the individual firm (1).','Industry concentration can raise local rents or wages when firms compete for scarce land or skilled workers.'),
('merit-goods','6.1.1-B01','Define merit goods.','Goods or services whose benefits consumers underestimate (1), so they would be under-consumed if provision were left entirely to the market (1).','Meaning: consumers underestimate the benefits (1); distinguishing feature: resulting under-consumption in an unassisted market (1). Being free or government-owned is not the definition.','Education and health care are common examples of merit goods.'),
('privatisation','6.1.1-B01','Define privatisation.','The transfer of ownership of an enterprise or activity (1) from the state/public sector to the private sector (1).','Meaning: a transfer of ownership (1); distinguishing feature: public/state to private ownership (1). Hiring a private contractor alone does not necessarily transfer ownership.','Privatisation can raise sale revenue for government but may reduce government control of services.'),
('nationalisation','6.1.1-B01','Define nationalisation.','The transfer of ownership of an enterprise or industry (1) from private owners to the state/public sector (1).','Meaning: a transfer of ownership (1); distinguishing feature: private to public/state ownership (1), the reverse of privatisation.','Nationalisation changes ownership rather than merely changing the tax paid by a private enterprise.'),
('income-tax-example','6.2.4-B01','Identify one direct tax charged on an individual’s earnings.','Personal income tax.','Characteristic/feature: personal income tax (1). Accept income tax or PAYE income tax; PAYE describes collection, not an additional separate tax.','Personal income tax is a direct tax on an individual’s taxable income.'),
('company-tax-example','6.2.4-B01','Identify the direct tax charged on a company’s taxable profits.','Company income tax (corporate income tax).','Characteristic/feature: company tax, corporate tax or corporate income tax (1). Do not credit VAT, which is not a tax on company profit.','Company income tax is charged on taxable profits rather than simply on all sales receipts.'),
('vat-example','6.2.4-B02','Identify the broad indirect tax whose abbreviation is VAT.','Value added tax.','Characteristic/feature: value added tax (1). No current tax rate is required.','VAT is an indirect tax on taxable goods and services, commonly collected through suppliers.'),
('excise-example','6.2.4-B02','Identify the indirect tax charged specifically on selected products such as alcohol or tobacco.','Excise duty.','Characteristic/feature: excise duty or excise tax (1). Do not credit the general name VAT in place of the selective product tax.','Excise duty is imposed on selected products, in contrast to the broader base of VAT.'),
('inflation','7.1-B02','Define inflation.','A sustained increase in the general price level, reducing the purchasing power of money.','Meaning: an increase in the general price level (1); distinguishing feature: sustained over time (1). A rise in one product’s price alone is insufficient.','A fall in the rate of inflation can still mean that the general price level is rising.'),
('current-account','7.4-B01','Define the current account of the balance of payments.','The account recording transactions between residents and the rest of the world in goods, services, primary income and current transfers over a stated period.','Meaning: a record of resident–rest-of-world transactions over a period (1); distinguishing feature: goods, services, primary income and current transfers, rather than investment and loan flows (1).','Purchases of financial assets are not treated as exports of services in the current account.'),
('current-account-components','7.4-B01','Identify the current-account component that records interest and dividends received from abroad.','Primary income.','Characteristic/feature: primary income (1). Accept income balance or income account when clearly referring to primary income; not services or current transfers.','Primary income includes interest and dividends, whereas current transfers involve no corresponding exchange.'),
('age-dependency','8.1-B04','Define the age-dependency ratio, using dependent ages below 15 and 65 or over and working ages 15–64.','The number of people below 15 plus those aged 65 or over, divided by the number aged 15–64 and multiplied by 100: people in dependent age bands per 100 working-age people.','Meaning: population in the stated dependent age bands divided by the stated working-age population (1); distinguishing feature: multiplied by 100/per 100 working-age people (1). This is not actual dependants per employed worker.','Some working-age people do not work and some older people work, so age dependency is not a count of actual economic dependence.'),
('hdi','8.2.1-B01','Define the Human Development Index (HDI).','A composite index of human development (1) combining health, education and income dimensions, represented by life expectancy, years of schooling and income per head (1).','Meaning: a composite index of human development (1); distinguishing feature: combines health, education and income (all three for 1). Accept the corresponding named indicators.','HDI values lie between zero and one; the index does not describe every person’s living conditions or income distribution.'),
('tariff','9.1.1-B04','Define an import tariff.','A tax (1) charged on goods imported from abroad (1).','Meaning: a tax (1); distinguishing feature: levied on imports (1), rather than a quantity limit.','A tariff can raise government revenue, whereas an import quota is a quantitative restriction.'),
('quota','9.1.1-B04','Define an import quota.','A limit on the quantity of a product (1) permitted to be imported during a stated period (1).','Meaning: a quantity limit (1); distinguishing feature: applies to imports over a stated period (1), rather than a tax on them.','An import quota is a non-tariff restriction.'),
('embargo','9.1.1-B04','Define a trade embargo.','An official ban on trade (1) in specified goods or with a specified country (1).','Meaning: an official trade ban (1); distinguishing feature: specified goods or trading country are prohibited (1), rather than merely taxed.','An embargo can prohibit specified imports rather than just make them more expensive.'),
('producer-subsidy','9.1.1-B04','Explain why a government subsidy to domestic producers can help them compete with imports.','The subsidy can reduce domestic producers’ effective cost per unit (1), enabling them to offer a lower price and compete more strongly with imports if they pass the saving to buyers (1).','Reason: reduction in domestic producers’ effective unit cost (1); because/link: this can support a lower competitive price if savings are passed on (1). A subsidy does not guarantee efficient production or increased sales.','A producer subsidy uses government resources and therefore has an opportunity cost.'),
]

def load(p): return json.loads(p.read_text())
def dump(p,d): p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def stamp(x):
    x['qa_status']='review_required'
    x['authored_hash']=hashlib.sha256(_artefact_text(x).encode()).hexdigest()

def main():
    scope={r['key']:r for r in load(WS/'planning/revision-01/scope.json') if r['owner']=='Codex'}
    assert len(ROWS)==len(scope)==37 and set(scope)=={r[0] for r in ROWS}
    snapshot=load(WS/'review/nonvisual-start-snapshot-6145.json')
    # Fail before mutation if this pass has already been run or canonical state drifted.
    for rel, old in snapshot.items():
        assert load(WS/rel)==old, f'Canonical state changed: {rel}; do not rerun authoring.'
    topics={}; manifest=[]
    for key,block,prompt,answer,rubric,qualifier in ROWS:
        r=scope[key]; t=r['topic_id']; td=WS/'topics'/t
        if t not in topics:
            topics[t]={'ledger':load(td/'claims/canonical_claim_ledger.json'),'items':load(td/f'learning-items/topic_{t}_items.json'),'units':{u['unit_id']:u for u in [load(p) for p in (td/'content-units').glob('*.json')]},'wo':load(td/'work_order.json')}
        a=topics[t]; slot=next(i for i in a['wo']['item_slots'] if i['slot']==r['slot_id'])
        assert not any(i['item_id']==slot['slot'] for i in a['items']['items'])
        uid='CU-6145-'+block.split('-B')[0]; bid='CU-6145-'+block
        unit=a['units'][uid]; b=next(b for b in unit['blocks'] if b['block_id']==bid)
        obj=slot['objective_id']; claim_ids=[]
        existing=[c for c in a['ledger']['claims'] if obj in c['objective_ids']]
        if key in ['total-revenue-definition','average-revenue-definition']:
            claim_ids=[c['claim_id'] for c in existing]
        else:
            # Existing quantitative objectives have two formula/example claims; add
            # their missing conceptual reason as one additional claim, not duplicates.
            texts=[answer] if key in ['ped-formula-meaning','pes-formula-meaning'] else [answer,qualifier]
            for n,text in enumerate(texts,1):
                cid=f'CL-6145-{t}-R01-{key}-{n}'
                c={'claim_id':cid,'objective_ids':[obj],'text':re.sub(r'\s*\([12]\)', '', text),'claim_type':'causal' if slot['subtype']=='WHY' else 'definition' if n==1 else 'comparison','provenance':'source_synthesised','evidence':[{'source_id':'NIED-6145-2018','locator':f"PDF p.{r.get('syllabus_pdf_page',10)}; {obj}; revision-01 bounded retrieval target",'support_type':'derivation'}],'derived_from_claim_ids':[],'verification':{'status':'unverified','method':'Codex revision-01 authoring; independent Claude cross-review pending','reviewer_id':None,'reviewed_at':None,'confidence':0.85},'publishable':False,'revision':1}
                a['ledger']['claims'].append(c);claim_ids.append(cid)
                b['claim_ids'].append(cid);b['claims_seen'][cid]=1
        if obj not in unit['objective_ids']:unit['objective_ids'].append(obj)
        # Keep the planned member unit mapped even where the root already teaches it.
        for pu in a['wo']['content_units']:
            if obj in pu['objective_ids']:
                target=a['units'][pu['unit_id']]
                if obj not in target['objective_ids']:target['objective_ids'].append(obj)
        exemplar=next(i for i in a['items']['items'] if i['item_type']=='flashcard')
        i={k:copy.deepcopy(v) for k,v in exemplar.items() if k not in ['prior_hash','repair_note','reviewed_unchanged']}
        i.update(item_id=slot['slot'],objective_ids=[obj],claim_ids=claim_ids,item_type='flashcard',prompt=prompt,canonical_answer=answer,marking_guidance=[rubric],context={'sector':None,'business_size':None,'ownership':None,'situation':'Focused retrieval','facts':[]},prerequisite_item_ids=[],intentional_duplicate_group=None,provenance='Original Codex authoring; approved 6145 revision-01 nonvisual scope',claims_seen={c:next(x['revision'] for x in a['ledger']['claims'] if x['claim_id']==c) for c in claim_ids})
        for k in ['subtype','assessment_objectives','difficulty','blooms_level','command_word','mark_tariff']:i[k]=copy.deepcopy(slot[k])
        stamp(i);a['items']['items'].append(i)
        manifest.append({'key':key,'item_id':i['item_id'],'objective_id':obj,'claim_ids':claim_ids,'teaching_block':bid})

    # Teaching additions are deliberately located outside the nearly full visual units.
    def block(t,u,n):return next(b for b in topics[t]['units']['CU-6145-'+u]['blocks'] if b['block_id']==f'CU-6145-{u}-B{n:02}')
    def append(t,u,n,text):block(t,u,n)['text']+='\n\n'+text
    append('3.3','3.3.3',1,'Percentage changes put price and quantity movements on a common proportional basis. Measuring price in cents instead of dollars changes raw numbers but not PED. The coefficient therefore compares responsiveness without depending on those units.')
    append('3.3','3.3.3',2,'PES likewise compares proportional changes. Counting output in dozens instead of single units must not change the responsiveness measured, since both the initial output and its change are rescaled together.')
    append('5.4','5.4.2',1,'External economies arise from industry growth or concentration, outside one firm’s own expansion. A shared pool of trained workers or nearby specialist repair suppliers can lower a producer’s average cost even without that producer expanding.')
    append('5.4','5.4.3',1,'External diseconomies arise outside the firm as an industry grows or concentrates. Competition for scarce local land and skilled workers can raise rents and wages; congestion can delay deliveries and raise cost per unit.')
    append('6.2','6.2.4',1,'Personal income tax is a direct tax on an individual’s taxable income, including earnings. Company income tax, also called corporate income tax, is a direct tax on company profits. Sales receipts are not the same as taxable profits.')
    append('6.2','6.2.4',2,'Value added tax (VAT) is a broad indirect tax on taxable goods and services. Excise duty instead applies to selected products, such as alcohol and tobacco. Both are indirect taxes; the examples identify their bases without assuming any current national rate.')
    append('8.2','8.2.1',1,'The Human Development Index (HDI) combines health, education and income into a composite measure of human development. Its dimensions use life expectancy, years of schooling and income per head. Values lie between zero and one. A higher value indicates higher measured human development, but does not show every person’s living conditions or how income is distributed.')
    append('9.1','9.1.1',4,'A domestic producer subsidy can reduce effective cost per unit. If the firm passes the saving to buyers, it can offer a lower price against imports. This uses government resources and does not guarantee efficiency or extra sales.')
    # Tight central-bank unit: replace only redundant framing, retaining each function.
    b=block('2.3','2.3.5',1)
    b['text']=b['text'].replace('The distinction concerns what the institution does, not simply the size of its building or whether the word bank appears in its name.','')
    b['text']+='\n\nCurrency provides a recognised common means of payment without barter. Government accounts handle public receipts and payments. Last-resort lending can meet a solvent bank’s temporary cash shortage; it does not promise to rescue every failing bank.'
    # Approved retarget of one existing definition slot, preserving its ID and labels.
    a=topics['5.4'];i=next(i for i in a['items']['items'] if i['item_id']=='ITEM-6145-5.4-013-DEF')
    cid='CL-6145-5.4-R01-internal-growth'
    c=copy.deepcopy(a['ledger']['claims'][0]);c.update(claim_id=cid,objective_ids=i['objective_ids'],text='Internal growth is expansion of a firm through developing its own operations rather than joining with or acquiring another firm.',revision=1,claim_type='definition',publishable=False)
    c['verification']={'status':'unverified','method':'Approved revision-01 internal-growth retarget; independent review pending','reviewer_id':None,'reviewed_at':None,'confidence':0.85}
    c['evidence']=[{'source_id':'NIED-6145-2018','locator':'PDF p.12; OBJ-6145-5.4-05; approved revision-01 internal-growth retarget','support_type':'derivation'}]
    a['ledger']['claims'].append(c)
    b=block('5.4','5.4',5);b['claim_ids'].append(cid);b['claims_seen'][cid]=1
    # Existing teaching describes organic growth; name it explicitly for retrieval.
    b['text']+='\n\nInternal growth means expanding the firm’s own operations, rather than growing by merger or acquisition.'
    i.update(prompt='Define internal growth of a firm.',canonical_answer=c['text'],marking_guidance=['Meaning: expansion of the firm’s own operations (1); distinguishing feature: developing internally rather than merger with or acquisition of another firm (1).'],claim_ids=[cid],claims_seen={cid:1},qa_status='review_required')
    p=WS/'topics/5.4/authoring_notes.json';notes=load(p) if p.exists() else {'topic_id':'5.4','deviations':[]}
    notes.setdefault('deviations',[]).append({'from':'ITEM-6145-5.4-013-DEF: generic firm-size definition','to':'Same ID, objective and planned labels; precise internal-growth definition','why':'Explicitly approved revision-01 retarget adds the missing named growth route; existing firm-size teaching is retained.'});dump(p,notes)

    # Add topics that need only budget repairs.
    for t in ['3.1','3.5']:
        td=WS/'topics'/t;topics[t]={'ledger':load(td/'claims/canonical_claim_ledger.json'),'items':load(td/f'learning-items/topic_{t}_items.json'),'units':{u['unit_id']:u for u in [load(p) for p in (td/'content-units').glob('*.json')]},'wo':load(td/'work_order.json')}
    def remove(t,u,n,text):
        b=block(t,u,n);assert text in b['text'],text;b['text']=b['text'].replace(text,'',1)
    remove('3.1','3.1',1,'The arrangement can exist without a sale being completed in every conversation: potential buyers may compare offers or decide not to buy. What matters is the connection through which exchange can be arranged.')
    remove('3.1','3.1',3,'First establish the market arrangement; then explain how the relevant information and constraints influence exchange. A market description should name the product and the people connected. A building with no arrangement for buyer-seller exchange is not established as a market merely because people gather there.')
    remove('3.5','3.5',2,'This links to market forces in topic 3.2, demand responsiveness in 3.3 and economies of scale in 5.4. These are simple economic models for explaining choices, rather than a claim that a real business perfectly matches their assumptions.')
    remove('3.5','3.5',1,'Ownership size alone does not settle the judgement.')
    remove('3.5','3.5',2,'Compare incentives and evidence under the stated conditions.')
    remove('4.1','4.1',1,'When advising an individual, compare monetary rewards, relevant conditions and the practical requirements of each option before making a condition-based judgement. The individual’s priorities should be stated explicitly.')
    remove('6.1','6.1.1',1,'Evaluate whether the output meets the intended need and whether its resources are used well. Paying no fee at the counter does not make staff time or equipment abundant.')
    remove('6.1','6.1.1',2,'A supported judgement identifies what work is needed and whether the arrangement delivers it effectively, rather than assuming either that public jobs are inherently unproductive or that more jobs necessarily mean a better service. A useful comparison also specifies the period. Hiring today can require induction before additional service is available, while an existing tool shortage may need attention sooner. Timing affects the feasible contribution of each option. Evidence should guide timing.')
    remove('6.1','6.1.1',1,'This distinction makes later policy analysis clearer by identifying which activity and responsibility the evidence actually describes.')
    remove('7.4','7.4',2,'These mechanisms operate together, so one trade change alone does not prove the final rate movement.')
    append('7.4','7.4.3',1,'For equal resources, 30 units exceed 12 units: the higher feasible output establishes absolute advantage in that good.')
    append('4.2','4.2.2',1,'For example, N$6,000 over 120 hours is N$50 per hour; N$7,000 over 175 hours is N$40 per hour. Higher monthly earnings can coexist with a lower hourly rate.')
    append('5.4','5.4.1',1,'Two independent bakeries joining at the same production stage illustrate horizontal integration. Merely opening another branch within one existing bakery is internal growth, without a merger.')
    # A subsequent self-check tightened the 3.5 comparison to retain explicit cross-links.
    block('3.5','3.5',2)['text']='A sole supplier’s large equipment may lower unit costs without justifying a higher price. Examine output, demand, quality and how savings are used. Several small sellers may face high costs, so their number does not prove prices must be low. Compare market forces (3.2), demand responsiveness (3.3) and economies of scale (5.4).'
    # All ten budget repairs now involve economic examples or removal of repetition.
    for t,a in topics.items():
        td=WS/'topics'/t
        dump(td/'claims/canonical_claim_ledger.json',a['ledger']);dump(td/f'learning-items/topic_{t}_items.json',a['items'])
        for uid,u in a['units'].items():
            u['word_count']=sum(len(b['text'].split()) for b in u['blocks'])
            dump(td/f'content-units/{uid}.json',u)
    dump(WS/'review/nonvisual-authored-items-6145.json',{'new_items':manifest,'existing_retarget':'ITEM-6145-5.4-013-DEF','topics_changed':sorted(topics),'independent_review':'pending Claude'})
    print('Authored',len(manifest),'new slots; one approved retarget; topics',len(topics))

if __name__=='__main__':main()
