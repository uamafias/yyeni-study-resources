"""Explicit planning decisions resolving Claude plan review r1; never edit standard/."""
import json
import re
from pathlib import Path
WS = Path(__file__).resolve().parents[1]

# Parent demand is retained independently of its list membership.
PARENT_TYPES = {
 '1.1.2':'illustrated_comparison','1.2.2':'feature','1.3.3':'feature',
 '2.2.2':'feature','2.2.7':'mechanism','2.3.2':'list_mechanism','2.3.3':'defined_quantitative',
 '2.3.5':'feature','3.2.1':'feature','3.2.4':'feature','3.3.1':'feature','3.3.3':'feature',
 '3.5.1':'feature','4.3.1':'feature','5.3.1':'quantitative','5.3.2':'quantitative',
 '5.3.3':'quantitative_mechanism','5.4.3':'diagram','5.4.5':'feature','6.1.1':'feature',
 '6.2.3':'feature','7.1.1':'defined_quantitative','7.1.2':'defined_comparison',
 '8.1.1':'list_mechanism','8.2.1':'quantitative_comparison','9.1.1':'feature',
}
MEMBER_TYPES = {
 '1.2.2':'mechanism','1.3.3':'discussion','2.3.2':'list_mechanism',
 '2.3.5':'evaluation','3.2.4':'mechanism','3.3.1':'definition',
 '3.5.1':'defined_evaluation','4.2.2':'mechanism','4.3.1':'mechanism',
 '5.3.1':'definition','5.3.2':'definition','5.4.5':'mechanism','6.1.1':'feature',
 '6.2.2':'mechanism','6.2.3':'mechanism','8.1.1':'concept','9.1.1':'evaluation',
}
SHAPES = {
 'feature':['FEATURE'],'definition':['DEF'],
 'list_mechanism':['FEATURE','MECH'],'discussion':['MECH','EVAL'],
 'illustrated_comparison':['DIST','APP','DIAGRAM'],
 'defined_quantitative':['DEF','CALC','INTERP'],
 'quantitative_mechanism':['CALC','MECH','INTERP'],
 'defined_comparison':['DEF','DIST','APP'],
 'quantitative_comparison':['DIST','CALC','INTERP'],
 'defined_evaluation':['DEF','EVAL'],
}

def extend_types(type_ids, type_words):
    opener={'FEATURE':'Identify','DEF':'Define','DIST':'Explain','APP':'Explain','MECH':'Explain','EVAL':'Evaluate','BEN':'Explain','LIM':'Explain','CALC':'Calculate','INTERP':'Analyse','DIAGRAM':'Explain'}
    for kind in SHAPES:
        type_ids[kind] = 'economics_' + kind
        type_words[kind] = list(dict.fromkeys(opener[s] for s in SHAPES[kind]))

def improve_nodes(nodes):
    for n in nodes:
        oid=n['objective_id']; pieces=oid.split('-')
        if len(pieces)<4: continue
        key=pieces[2]+'.'+str(int(pieces[3]))
        member='-M' in oid
        kind=(MEMBER_TYPES if member else PARENT_TYPES).get(key)
        if kind:
            n['objective_type']='economics_policy_evaluation' if kind=='evaluation' else 'economics_'+kind
            n['assessment_objectives']=['A','B','C'] if 'evaluation' in kind or kind=='discussion' else ['A','B']
            n['depth_tier']=4 if 'evaluation' in kind or kind=='discussion' else 3 if kind!='definition' and kind!='feature' else 1
            op={'FEATURE':'Identify','DEF':'Define','DIST':'Explain','APP':'Explain','MECH':'Explain','EVAL':'Evaluate','CALC':'Calculate','INTERP':'Analyse','DIAGRAM':'Explain'}
            shapes=SHAPES.get(kind,{'mechanism':['MECH','APP'],'evaluation':['EVAL'],'concept':['DEF','FEATURE']}.get(kind,[]))
            n['command_words']=list(dict.fromkeys(op[s] for s in shapes))
        if member and key=='3.5.1':
            term='perfect competition' if oid.endswith('M01') else 'monopoly'
            n['learner_objective']=f'Define {term}; discuss and evaluate its pricing and output policies.'
        elif member and kind in ('evaluation','discussion'):
            n['learner_objective']='Discuss and evaluate '+('the functions of ' if key=='2.3.5' else '')+n['syllabus_text']+' with opposing effects, a decisive condition and a justified conclusion.'
        elif member and kind in ('mechanism','list_mechanism'):
            n['learner_objective']='Explain '+n['syllabus_text']+' through a developed economic reason and consequence.'
        if member and key=='4.2.2':
            n['learner_objective']='Explain earnings differences involving '+n['syllabus_text']+'; name the comparison group and explain a productivity, skill, bargaining or labour-demand cause.'
        if member and key=='4.1.1':
            n['learner_objective']='Contrast wage and non-wage factors in occupational choice, focusing on '+n['syllabus_text']+'.'
        if not member and key=='7.1.2':
            n['learner_objective']='Define inflation and distinguish demand-pull and cost-push inflation using their causes.'

# Selected for the specific demand, not registry position. The second field is the
# mechanism/data anchor, the third the discussion/decision anchor.
TASKS = {
 '1.1':('01 02','02','03','opportunity cost of reading support versus computer skills; a second time slot changes feasibility'),
 '1.2':('01 02','02','03','resource allocation under market, planned and mixed systems; efficiency versus equitable access'),
 '1.3':('01 02','02','03','individual versus regional specialisation; productivity gains versus dependence on a narrow market'),
 '2.1':('01 02','02','03','choose a sole proprietor or company for an expanding invented firm; capital needs versus control'),
 '2.2':('01 02 04','07','05 06','union bargaining and employer representation; worker protection versus effects on employment'),
 '2.3':('02 03','03 04','05','central banks, commercial banks and stock exchanges; compare their contribution under a credit constraint'),
 '3.1':('01 02','01 02',None,'goods and factor markets; explain buyers, sellers and exchange arrangements in two supplied cases'),
 '3.2':('01 02','03 05','02 04','a demand shift versus a supply shift; weigh effects on buyers and sellers with stated schedules'),
 '3.3':('01 03','03','02','PED and PES calculations; assess a price decision under elastic versus inelastic demand'),
 '3.4':('01 02','02',None,'informative and persuasive advertising; explain a specified purpose and suitable method, without a policy judgement'),
 '3.5':('01-M01 01-M02','01-M01 01-M02','01-M01 01-M02','pricing and output in monopoly versus perfect competition; efficiency gains versus consumer consequences'),
 '4.1':('01-M01 01-M02','01-M01 01-M02','01','an occupational choice with higher pay versus training and working conditions'),
 '4.2':('01 04','02 04','03','earnings changes between two occupations; weigh productivity and bargaining explanations against supplied evidence'),
 '4.3':('01 02','01 02','03','income-group expenditure changes; assess how income and interest conditions explain saving and borrowing'),
 '5.1':('01 02','03 04','01 04','a firm choosing labour or capital; assess profit gains subject to demand and substitution constraints'),
 '5.2':('01 02','02 04','03 05','IT and training to raise productivity; assess improvement while considering health-related disruption'),
 '5.3':('01 02','01 02 03','03 04','compute costs and revenue across outputs; weigh technology savings against new fixed costs'),
 '5.4':('01 02 03','02 03','04 05','expansion and integration; assess lower average cost against coordination costs and market size'),
 '6.1':('01-M01 01-M02 01-M03','01-M01 01-M02 01-M03',None,'government production, provision and employment; describe and explain each role in supplied examples'),
 '6.2':('01 02 04','03 06','02 05','tax and budget policy versus interest-rate policy; assess growth and inflation aims under the currency constraint'),
 '6.3':('01 02','01 02','03 04 05','consumer and employee protection including HIV and AIDS; weigh protection benefits and implementation constraints'),
 '7.1':('01 02','01 02','03','a simple price index and inflation; assess effects on fixed-income households and debtors'),
 '7.2':('01 02','02 03','04','unemployment causes and consequences; assess training versus demand support for different causes'),
 '7.3':('01 02','02 03',None,'national-income measures and methods; explain uses and consistent accounting without an invented evaluative outcome'),
 '7.4':('01 02 03','01 03','02','comparative advantage and external trade; discuss exchange-rate changes against a third currency'),
 '8.1':('01 03','01 03','02 04','development and population change; assess pressure on services versus a larger working population'),
 '8.2':('01 02','01 03','02','GDP per person and non-income indicators; discuss disparities with unequal distribution and access to IT'),
 '9.1':('01-M01 01-M02','01-M01 01-M02','01-M03 01-M04 01-M05','resource conservation, trade protection and public expenditure; assess who gains and who bears costs over time'),
}

# Four short parts chosen by what can actually be recalled or briefly applied.
# Syntax: command / local objective suffix / precise subject of the part.
SHORT_PARTS={
 '1.1':['Define/01/scarcity','Identify/01/a scarce resource and one feasible alternative use','Explain/02/opportunity cost as the next-best feasible alternative forgone','Identify/02/a non-monetary benefit forgone in a supplied choice'],
 '1.2':['Define/01-M03/capital as a factor of production','Identify/01/two factors of production in supplied examples','Explain/02-M01/the price mechanism allocating a resource','Identify/02/two distinctions between planned and mixed systems'],
 '1.3':['Define/01-M01/specialisation','Identify/01-M02/two divided tasks in a supplied production process','Explain/02/a productivity gain from division of labour','Identify/03/regional and national specialisation in supplied examples'],
 '2.1':['Define/02-M01/sole proprietor','Identify/01/private and public sector ownership','Explain/02/a company ownership distinction','Identify/03/two constraints relevant to choosing a business form'],
 '2.2':['Define/01/trade union','Identify/02/two union aims','Explain/07/one employer-association role','Identify/04/two union types from supplied descriptions'],
 '2.3':['Define/03/exchange rate','Identify/02/two functions of money','Explain/05/one commercial-bank function','Identify/05/two differences between central and commercial bank roles'],
 '3.1':['Define/01/market','Identify/02/goods and factor markets in examples','Explain/01/how buyers and sellers interact without meeting physically','Identify/02/the traded product or factor in two supplied markets'],
 '3.2':['Define/01-M01/demand','Identify/02/equilibrium price and quantity from a supplied schedule','Explain/04/a non-price cause of a demand shift','Identify/01-M02/two determinants of supply'],
 '3.3':['Define/01-M01/price elasticity of demand','Identify/01-M02/elastic and inelastic supply from given coefficients','Explain/02/one implication of inelastic demand for revenue','Identify/03/the percentage price and quantity changes in supplied working'],
 '3.4':['Define/01/advertising','Identify/02/informative and persuasive messages','Explain/02/one advertising purpose','Identify/02/two advertising methods suitable for a supplied audience'],
 '3.5':['Define/01-M01/perfect competition','Identify/01-M02/two monopoly characteristics','Explain/01-M01/why a competitive firm is a price taker','Identify/01-M02/two constraints on monopoly pricing'],
 '4.1':['Identify/01-M01/two wage factors in occupational choice','Identify/01-M02/two non-wage factors','Explain/01/how working conditions affect a supplied job choice','Identify/01/a wage and a non-wage factor from the supplied offers'],
 '4.2':['Define/04/transfer earnings','Identify/01/two factors determining earnings','Explain/02/one supplied earnings difference','Identify/04/economic rent and transfer earnings in a simple stated reward'],
 '4.3':['Identify/01/two expenditure-pattern differences in a supplied table','Identify/02/two motives for saving','Explain/01/why saving shares can differ with income','Identify/02/a spending and a borrowing motive in supplied cases'],
 '5.1':['Define/02/production','Identify/03/two determinants of factor demand','Explain/04/a reason to substitute capital for labour','Identify/01/the profit-maximising output in a small total-cost/revenue schedule'],
 '5.2':['Define/01/productivity','Identify/02/output and input quantities needed to measure productivity','Explain/04/one IT effect on output per worker','Identify/03/two ways to improve productivity'],
 '5.3':['Define/01-M03/fixed cost','Identify/01/fixed and variable costs in supplied examples','Explain/03/why total and average costs can move differently','Identify/02/total and average revenue in supplied figures'],
 '5.4':['Define/01-M01/horizontal integration','Identify/01/forward and backward integration in supplied examples','Explain/02/one economy of scale','Identify/05/two constraints on firm size'],
 '6.1':['Identify/01-M01/two goods produced by government in supplied invented examples','Identify/01-M02/two government services','Explain/01-M03/one stated example of government employment','Identify/01/a production and an employment role in supplied cases'],
 '6.2':['Define/01/government economic policy','Identify/02/two policy aims','Explain/03/a fiscal-policy transmission step','Identify/04/direct and indirect taxes in supplied examples'],
 '6.3':['Define/01/external cost','Identify/02/two ways to control a harmful production activity','Explain/03/a consumer-protection mechanism','Identify/04/two employee interests relevant to protection'],
 '7.1':['Define/01/retail price index','Identify/02/demand-pull and cost-push inflation in examples','Explain/03/one inflation effect on a fixed-income household','Identify/01/base-year and current-year basket costs in supplied data'],
 '7.2':['Define/02/unemployment','Identify/02/two unemployment causes in supplied cases','Explain/03/one consequence of unemployment','Identify/04/two remedies matched to stated causes'],
 '7.3':['Define/01-M01/Gross Domestic Product','Identify/02/two national-income measurement methods','Explain/03/one use of national-income data','Identify/01/domestic and national measures in supplied definitions'],
 '7.4':['Define/03-M02/comparative advantage','Identify/01/goods exports and imports in a supplied table','Explain/02/a reason for a third-currency exchange-rate change','Identify/03/the lower opportunity-cost producer from supplied ratios'],
 '8.1':['Define/03-M04/net migration','Identify/01/two development indicators','Explain/03/one population-growth cause','Identify/03/birth and death rates from supplied definitions'],
 '8.2':['Define/01/GDP per capita','Identify/01/two non-income living-standard indicators','Explain/03/one IT effect on household living standards','Identify/02/two distributional differences in supplied data'],
 '9.1':['Identify/01-M01/private and external costs in a supplied example','Identify/01-M02/a short-term and a long-term effect','Explain/01-M03/a resource-conservation conflict','Identify/01-M05/public and private expenditure in supplied cases'],
}
VARIANTS={
 '1.1':'one staffed room versus a volunteer and second time slot',
 '1.2':'staple-food access for low-income households versus producer incentives',
 '1.3':'a worker specialising in a stable-demand task versus a region relying on one volatile export',
 '2.1':'a sole owner prioritising control versus expansion requiring substantial new capital',
 '2.2':'strong labour demand with scarce skills versus weak demand and abundant applicants',
 '2.3':'households needing deposit/payment services versus firms needing long-term equity capital; distinguish commercial banks, central-bank stability and the stock exchange',
 '3.2':'a rightward demand shift with responsive supply versus a supply contraction; weigh buyer affordability and seller receipts separately',
 '3.3':'PED magnitude 0.5 versus 2.0 for the same proposed price rise, other demand conditions unchanged',
 '3.5':'a monopolist able to exploit scale savings versus one passing few savings to consumers',
 '4.1':'a higher wage with long travel versus a lower wage with paid training and shorter travel',
 '4.2':'rising productivity with skill scarcity versus unchanged productivity with weak bargaining power',
 '4.3':'a lower-income household meeting essential spending versus a higher-income household able to save; compare the same period',
 '5.1':'strong demand permitting higher machine utilisation versus weak demand leaving new capital idle',
 '5.2':'IT introduced with worker training versus the same IT without training and with disruption from illness',
 '5.3':'technology used at high output versus low output; fixed costs increase while variable cost per unit falls',
 '5.4':'a large stable market supporting expansion versus a narrow market and growing coordination costs',
 '6.2':'tax-funded public investment during unemployment versus inflationary pressure constraining expansion; respect the rand peg when discussing rates',
 '6.3':'protection effectively enforced versus limited inspection capacity; consider consumers, workers and workplace HIV non-discrimination',
 '7.1':'fixed nominal pension income versus a debtor with a fixed nominal debt; distinguish nominal and real changes',
 '7.2':'skills mismatch versus a general fall in demand; assess remedies against each cause',
 '7.4':'an exporter versus an importer after a depreciation against a third currency, with different capacity to respond',
 '8.1':'a large working-age cohort with jobs available versus the same cohort facing insufficient jobs and services',
 '8.2':'similar GDP per person with unequal versus broadly shared income and access to services',
 '9.1':'short-term private gains from resource extraction versus long-term social costs; then free-trade gains to consumers versus producer protection and public/private expenditure trade-offs',
}

def task_specs(tid, objects):
    recall,analysis,decision,focus=TASKS[tid]
    ids=lambda text:['OBJ-6145-'+tid+'-'+s for s in text.split()]
    rs=ids(recall); an=ids(analysis); de=ids(decision) if decision else []
    parts1=[]
    for text in SHORT_PARTS[tid]:
        command,local,demand=text.split('/',2)
        parts1.append({'command_word':command,'mark_tariff':2,'objective_ids':['OBJ-6145-'+tid+'-'+local],'demand':demand})
    parts2=[{'command_word':'Describe','mark_tariff':6,'objective_ids':rs,'demand':'three described economic features, each with a distinguishing detail'},
            {'command_word':'Explain','mark_tariff':7,'objective_ids':an,'demand':'develop the stated mechanism with supplied evidence and conditions'},
            {'command_word':'Discuss' if de else 'Explain','mark_tariff':7,'objective_ids':de or an,'demand':'weigh opposing effects and reach a conditional conclusion' if de else 'develop a second distinct mechanism in the supplied case'}]
    # Keep each structured case focused on no more than four source anchors.
    focused={'2.2':('07','07','05 06'),'3.2':('01','03','02 04'),
             '5.2':('02','04','03 05'),'5.4':('02 03','02 03','04 05'),
             '6.2':('02','03 06','05'),'6.3':('03 04','01','03 04 05')}
    if tid in focused:
        for part,local in zip(parts2,focused[tid]):part['objective_ids']=ids(local)
    for part in parts2:
        labels='; '.join(objects[o]['learner_objective'] for o in part['objective_ids'])
        part['demand']+=': '+labels
    parts3=[{'command_word':'Evaluate' if de else 'Explain','mark_tariff':7,'objective_ids':de or an,
             'demand':f'Case {i+1}: '+(VARIANTS.get(tid,focus).split(' versus ',1)[0] if i==0 else VARIANTS.get(tid,focus).split(' versus ',1)[-1])+'; '+focus} for i in range(2)]
    if not de:
        for p in parts2[1:]: p['mark_tariff']=4
    task_rows=[
        ('short_answer',parts1,{'A':8}),
        ('data_response' if de else 'case_analysis',parts2,{'A':6,'B':7,'C':7} if de else {'A':6,'B':8})]
    if de: task_rows.append(('essay_plan',parts3,{'C':14}))
    result=[]
    for i,(kind,parts,split) in enumerate(task_rows,1):
        covered=list(dict.fromkeys(o for p in parts for o in p['objective_ids']))
        result.append({'slot':f'ITEM-6145-{tid}-P{i:02}','topic_id':tid,'item_type':kind,
          'part_specs':parts,'ao_marks_equivalent':split,'assessment_objectives':list(split),
          'command_word':parts[0]['command_word'],'mark_tariff':sum(split.values()),
          'blooms_level':'Understand' if i==1 else 'Evaluate' if i==3 and de else 'Analyse',
          'objective_ids':covered,'objective_selection_note':'Demand-led selection: '+focus,
          'brief':('Four short retrieval/application parts: '+ '; '.join(p['command_word']+' '+p['demand'] for p in parts) if i==1 else ('Structured case analysis: ' if i==2 else 'Paired evaluation plans: ')+focus)+'. Follow the numbered part_specs in planning/performance-specs.json; all context/data must be supplied. Each part needs concrete credit points and an exact allocation. Do not infer an official AO split from this practice allocation.'})
    assert all(o in objects for r in result for o in r['objective_ids'])
    return result

OWNERSHIP=[
 ('exchange rates','2.3','7.4','2.3 owns quotation, conversion and direct agent effects; 7.4 owns macro causes, trade patterns and comparative advantage.'),
 ('banking and monetary policy','2.3','6.2','2.3 owns institutional functions and their evaluation; 6.2 owns policy aims, transmission and budget/interest instruments.'),
 ('policy aims and outcomes','6.2','7.1,7.2,7.3,7.4','6.2 owns instrument choices and conflicts between aims; indicator topics own definitions, measures and specific causes/consequences.'),
 ('trade protection','7.4','9.1','7.4 owns trade mechanisms; 9.1 owns conflicting interests and judgements over time. Cross-link the mechanism rather than reteach it.'),
 ('IT','5.2','8.2','5.2 owns output per input; 8.2 owns household access and living standards, including distribution.'),
 ('HIV and AIDS','5.2','6.3','5.2 owns productivity effects; 6.3 owns workplace protection and non-discrimination, without unverified statutory detail.'),
 ('public corporation','2.1','6.1','2.1 owns ownership/legal form; 6.1 owns government production, services and employment.'),
 ('firm output and national output','5.3','7.3','5.3 owns firm costs/revenue; 7.3 owns national accounting. Similar words do not establish an overlap.'),
 ('pricing and government policy','3.5','6.2','3.5 owns firm pricing/output in specified market structures; 6.2 owns macroeconomic policy.'),
 ('allocation and markets','1.2','3.1','1.2 owns economic systems; 3.1 owns the arrangement linking buyers and sellers.'),
]

def ownership_for(tid):
    return [f'{term}: {note} (topics {owner}; {others})' for term,owner,others,note in OWNERSHIP if tid==owner or tid in others.split(',')]

def scope_fixes():
    path=WS/'curriculum/scope-scan.json'; data=json.loads(path.read_text())
    patterns=[
     ('Higher-level aggregate models',r'\b(?:AD\s*/\s*AS|aggregate (?:demand|supply) curve|(?:fiscal|Keynesian|investment) multiplier)\b','Use the fiscal multiplier and AD/AS curves.','Explain how public spending may raise demand and employment.'),
     ('Additional market-structure and welfare theory',r'\b(?:oligopoly|consumer surplus|producer surplus|deadweight loss|price discrimination)\b','Explain oligopoly using consumer surplus, deadweight loss and price discrimination.','Discuss pricing and output in monopoly and perfect competition.'),
    ]
    for construct,pattern,catch,allow in patterns:
        assert re.search(pattern,catch,re.I) and not re.search(pattern,allow,re.I)
        if not any(e['construct']==construct for e in data['entries']):
            data['entries'].append({'construct':construct,'pattern':pattern,'applies_to':'subject',
             'controls':{'must_catch':[catch],'must_allow':[allow]},'source':'Planner depth judgement from the positive syllabus scope; not a stated board prohibition.',
             'provenance':{'boundary':'judgement','positive_scope':'syllabus'},'syllabus_sentence':None})
    path.write_text(json.dumps(data,indent=2)+'\n')

def improve_profile(sp):
    sp['answer_structures']['case_analysis']=['context|data','mechanism|explanation','marks|allocation']
    sp['answer_structures']['DIAGRAM']=['axes|labels','original equilibrium|initial position|original curve','change|control','explanation|interpretation']
    sp['slot_plan']['performance_tasks']=[]
    sp['slot_plan']['note']='Operative topic-specific performance inputs are performance_tasks_by_topic, projected by planning/generate_work_orders.py. All parts and objective selections are explicit. No generic performance fallback or AO top-up is commissioned.'
    sp['slot_plan']['subtypes_by_objective_type'].update({'economics_'+k:v for k,v in SHAPES.items()})
    # A full EVAL already develops both mechanisms; separate BEN and LIM cards
    # on every evaluation objective repeated those same arguments unnecessarily.
    sp['slot_plan']['subtypes_by_objective_type']['economics_policy_evaluation']=['EVAL']
    sp['slot_plan']['performance_tasks_by_topic']={t:task_specs(t,{o['objective_id']:o for o in json.loads((WS/'curriculum/objective_registry.json').read_text())['objectives']}) for t in TASKS}
    sp['authoring_constraints'] += [
      'Use curriculum/topic-ownership.json for overlaps; teach the owned demand and cross-link the rest.',
      'For actual Namibia examples the Namibia dollar is pegged one-to-one to the rand. Do not invent N$/rand appreciation. Use a third-currency quotation or explicitly hypothetical floating economy.',
      'Bank of Namibia interest-rate choices must support the peg; do not claim unlimited independent monetary policy or automatic equality of its rate with South Africa. See curriculum/jurisdiction-sources.json.',
      'Settled glossary definitions take precedence over imprecise syllabus shorthand while the syllabus controls scope. See curriculum/definition-rulings.json.',
    ]
    sp['conditioned_mechanisms'].append({'mechanism_id':'CM-6145-NAMIBIA-PEG','name':'Actual Namibia currency and monetary-policy examples',
     'asserted_when':[r'(?:\bNamibia(?:n)? dollar\b|N\$)',r'\b(?:exchange rate|policy rate|repo rate|monetary policy|appreciat\w*|depreciat\w*)\b'],
     'required_conditions':[{'name':'Recognise rand peg or specify third currency / hypothetical system','any_of':[r'\brand\b',r'\bpeg\b',r'\bthird.currency\b',r'\bhypothetical\b']}],
     'rationale':'Actual exchange-rate and monetary-policy scenarios must respect the verified one-to-one rand link; see jurisdiction-sources.json.'})
    (WS/'curriculum/topic-ownership.json').write_text(json.dumps({'provenance':'planner judgement assigning teaching ownership within the syllabus','entries':[dict(zip(['construct','owner','cross_links','rule'],r)) for r in OWNERSHIP]},indent=2)+'\n')
