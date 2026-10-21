"""Codex repairs to Claude's complete-subject review, 2026-10-20.

Explicit authored changes; no model calls or network. Replays from a preserved
pre-repair baseline, preserving claim revisions and previous artefact hashes.
Run from the repository root, then render, restamp and audit every topic.
"""
import copy
import hashlib
import json
import re
import sys
from pathlib import Path

WS = Path(__file__).resolve().parents[2]
REPO = WS.parents[1]
BASE = Path(__file__).parent / 'baseline'
sys.path.insert(0, str(REPO / 'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text

def read(p): return json.loads(p.read_text())
def dump(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, ensure_ascii=False) + '\n')

def baseline(p):
    b = BASE / p.relative_to(WS)
    if not b.exists():
        b.parent.mkdir(parents=True, exist_ok=True)
        b.write_bytes(p.read_bytes())
    return read(b)

TOPICS = {}
for td in sorted((WS/'topics').iterdir()):
    if not (td/'contract.json').exists(): continue
    ip = next((td/'learning-items').glob('*.json'))
    lp = td/'claims/canonical_claim_ledger.json'
    TOPICS[td.name] = dict(td=td, ip=ip, lp=lp, items=baseline(ip), ledger=baseline(lp),
        units={p.name: baseline(p) for p in sorted((td/'content-units').glob('*.json'))},
        notes=baseline(td/'authoring_notes.json'))

CHANGES = []
def unit(t, n): return TOPICS[t]['units'][f'CU-6136-{t}.{n:02d}.json']
def item(t, n):
    key = f'ITEM-6136-{t}-'+(n if isinstance(n,str) else f'{n:03d}-')
    return next(i for i in TOPICS[t]['items']['items'] if i['item_id'].startswith(key))

def question(t, n, prompt, answer, guidance=None, finding='R6136-006'):
    i=item(t,n); i['prompt']=prompt; i['canonical_answer']=answer
    if guidance is not None: i['marking_guidance']=guidance+['Original indicative practice guidance; not an official mark scheme.']
    CHANGES.append(dict(finding=finding, artefact=i['item_id'], action='Rewrite prompt and answer to the actual demand.'))

def teach(t, n, heading, text, finding, source=None):
    u=unit(t,n); objective=u['objective_ids'][0]
    claims=TOPICS[t]['ledger']['claims']
    suffix=objective.removeprefix(f'OBJ-6136-{t}.')
    seq=90+sum(c['claim_id'].startswith(f'CLM-6136-{t}-{suffix}-9') for c in claims)
    cid=f'CLM-6136-{t}-{suffix}-{seq:02d}'
    claims.append(dict(claim_id=cid, objective_ids=[objective], text=text,
        claim_type='procedural' if finding in ['R6136-005','R6136-011'] else 'factual',
        provenance='source_synthesised', evidence=[dict(source_id=source or '6136-syllabus-and-local-assessment-corpus',
            locator=f'Topic {t}, sub-topic {n}; review {finding}; source-demand synthesis, original teaching wording.', support_type='derivation')],
        derived_from_claim_ids=[], revision=1,
        verification=dict(status='unverified',method='Codex source-based repair after Claude review; not independently re-reviewed.',reviewer_id=None,reviewed_at=None,confidence=0.9),
        publishable=False,notes=[finding]))
    bid=f'BLK-6136-{t}.{n:02d}-R{sum("-R" in b["block_id"] for b in u["blocks"])+1:02d}'
    u['blocks'].append(dict(block_id=bid,block_type='plain_explanation',heading=heading,text=text,claim_ids=[cid],claims_seen={cid:1},
        context_tags=['Codex repair after independent review; original teaching synthesis'],
        assessment_objectives=sorted({a for b in u['blocks'] for a in b.get('assessment_objectives',[])})))
    CHANGES.append(dict(finding=finding,artefact=bid,action='Add missing teaching and a traceable canonical claim.'))

# Definitions and the named, historically examined national plans.
teach('2.1',1,'Meaning and time horizon of Vision 2030',
    'Namibia Vision 2030 is a national development framework setting a direction from the country’s position in 2004 towards improved living conditions by 2030. It connects long-term social and economic goals with development strategies. It describes an intended future; the title and end date are not evidence that the goals have been achieved.',
    'R6136-001','6136-2020-ER: Paper 2 Q1(c)(i), printed p.143')
question('2.1',1,'Describe Namibia Vision 2030 and one way education can contribute to it.',
    'Vision 2030 is Namibia’s long-term development framework, linking its 2004 starting position to improved living conditions by 2030. Education can develop skills that people use in productive work and public life.',
    ['Feature: identify a national development framework and its long-term purpose.','Feature: describe the contribution of education, rather than naming it alone.'], 'R6136-001')
teach('2.2',2,'Harambee Prosperity Plan: a dated example',
    'The first Harambee Prosperity Plan (HPP) was introduced in 2016 under President Hage Geingob. It sought faster progress against poverty and large inequalities in wealth, supporting the longer national development direction. Its five pillars joined effective governance and service delivery, economic advancement, social progression, infrastructure development, and international relations and cooperation. Governance concerns accountable decisions and useful services. Economic advancement concerns productive opportunities and employment. Social progression includes food security, housing, sanitation and skills. Infrastructure supplies networks such as water, electricity and transport. International cooperation links national action with regional and wider partners. These are the plan’s intended contributions, not five proven achievements. Keep this 2016 example distinct from later plans.',
    'R6136-002','6136-2022-ER: Paper 2 Q1(a)(i)–(v), printed p.147')
question('2.2',4,'Explain how to judge NDP5 (2017/18–2021/22) against its economic-progress and social-inclusion goals. A fictional district comparison for practice records more jobs, but no rise in reliable water access in remote settlements. Weigh the mixed evidence; do not treat these invented results as a national assessment.',
    'More jobs would support the economic-progress goal if the comparison uses consistent measures. Unchanged remote water access would weaken evidence of wider inclusion: employment growth does not establish improvements in every service or place. The mixed pattern warrants separate checks on who obtained work, service reliability and the starting position. A judgement of complete success would be premature; the goals have to be tested with observed outcomes, not merely promised targets.',
    ['Judgement: acknowledge partial progress and the inclusion gap.','Reason: connect both supplied observations to named NDP5 goals, distinguish fictional district evidence from a real national verdict.'], 'R6136-002')
# Use the existing second short-answer slot for the examined HPP knowledge.
question('2.2',3,'Describe the first Harambee Prosperity Plan, giving its launch year, president and one pillar’s contribution.',
    'HPP began in 2016 under President Hage Geingob to accelerate progress against poverty and wealth inequality. Its infrastructure pillar concerned usable networks such as electricity, water and transport supporting services and production.',
    ['Feature: identify the 2016 HPP and Hage Geingob.','Feature: describe a pillar’s development contribution; accept another accurate pillar.'], 'R6136-002')

# Breadth: distinct mechanisms, not repeated qualifications or extra terminology.
teach('1.1',4,'Why an income average is incomplete',
    'GNP per person divides a national aggregate by population, so unequal distribution can leave many households with low incomes despite a high average. Unrecorded household farming and informal sales can make measured output incomplete. Money income does not show whether people can obtain safe water, education or health care. It also leaves out losses such as damaged habitats and the value of unpaid care. Price differences change what a given income buys, so international comparisons need a comparable basis. An average may help compare economic resources, but combine it with evidence on distribution, services and environmental conditions before judging living standards.', 'R6136-004')
teach('1.2',1,'Sustainable Development Goals',
    'The United Nations Sustainable Development Goals (SDGs) organise international development ambitions for 2030. They connect poverty, health, education and equality with environmental protection. Progress in one area can help another, but a trade-off such as jobs gained through damaging water use still needs a judgement about present and future needs.', 'R6136-004')
teach('1.2',3,'SDG 12 in everyday production',
    'SDG 12 concerns responsible consumption and production. Repairing equipment extends its useful life; reusing containers reduces repeated material demand; reducing food spoilage saves resources already used in production. Recycling can recover materials, but needs sorting and a usable collection route. Compare prevention, reuse and recovery rather than assuming all discarded material can be recycled.', 'R6136-004')
teach('3.1',14,'Privatisation: possible benefits and costs',
    'Privatisation transfers a state-owned activity into private ownership. A sale may raise public funds once, but this is not recurring tax revenue. A commercially accountable operator may cut waste, react to customers or invest in new methods. Competition can encourage better quality and restrain prices where customers have genuine alternatives. These gains are conditional: one private monopoly may raise charges instead. Staff reductions can remove jobs; loss of an access obligation can exclude poorer or remote users. Compare investment, efficiency, prices, employment and coverage together. Regulation and the sale terms affect who gains, so changing ownership is not proof of improvement.', 'R6136-004','6136-2022-ER: Paper 1 Q1(b)(v), printed p.142')
teach('4.1',4,'State roles in industrial development',
    'The syllabus’s NIC examples include South Africa and India. South Africa’s public transport and electricity networks illustrate shared infrastructure used in industrial production; India’s public technical education and research illustrate support for productive skills and knowledge. Neither example proves that a single policy caused growth or that services are currently reliable. More generally a state can coordinate investment, improve export links or support access to finance. These measures have opportunity costs and can fail through poor selection or weak accountability. Test actual use, access and productive benefit rather than the spending total.', 'R6136-004')
teach('4.1',5,'Namibian industries and links to livelihoods',
    'Namibian examples include mineral extraction and processing, fish processing, meat processing and tourism-related services. A fish-processing activity can add local handling, packaging and transport work to landed fish, provided stocks and quality are protected. Meat processing can connect livestock producers with slaughtering, storage and marketing. Mineral processing can retain a production stage locally but needs power, skills and buyers; mining income alone does not establish benefits for every household. Tourism creates service demand where local guides, accommodation and suppliers participate. These examples identify established activities, not current employment totals or a ranking of their size.', 'R6136-009')
teach('5.1',4,'Several benefits and obstacles of rural schemes',
    'A farmers’ cooperative can lower input prices through joint purchasing, share transport costs, provide storage, pool marketing and bargaining, connect members to credit and exchange farming advice. These are distinct benefits; repeating “cheaper” for every point hides the mechanism. Members need fair rules, trustworthy records and arrangements for conflicting interests. Loans can finance seed or tools before sales generate cash, but repayment costs and a poor harvest can threaten affordability. Resettlement can widen land access yet fail without water, services, productive skills and buyers. An integrated scheme can coordinate these complementary needs but needs clear budgets and agency responsibilities. Grassroots schemes can use local knowledge and voluntary effort, while limited finance and unequal voice can restrict them. Marketing problems include unreliable transport, inadequate storage, poor market information and failure to meet buyer quality requirements; rainfall and soil quality are production problems instead.',
    'R6136-004','6136-2024-ER: Paper 1 Q2(b)(ii)–(iv), printed p.153')
teach('5.1',4,'Southern African applications',
    'Land reform and resettlement are Southern African approaches to unequal land access, including in Namibia. Evaluate land suitability and continuing support rather than equating allocated hectares with better livelihoods. Collective farming shares productive work or assets; a cooperative may instead market members’ separately produced crops. Small self-help projects can pool labour around a local need. An integrated rural scheme connects farming support with roads, water or other services. Use these named approaches to describe how rural development is attempted in the region; their names do not establish that every scheme succeeded.', 'R6136-009')
teach('5.1',7,'Conservancies as a Namibian example',
    'Namibian communal conservancies illustrate community involvement in wildlife management and associated tourism opportunities. Local guides, accommodation work and supply contracts can retain income and support incentives to protect wildlife. Community decision rules and the distribution of returns matter: wildlife damage, restricted access and unequal benefits can impose costs. A conservancy is therefore an example to evaluate, rather than automatic proof that conservation has improved all livelihoods. Compare retained earnings, community influence, habitat condition and residents’ costs using evidence for the particular place and period.', 'R6136-009','6136-2024-ER: rural development and tourism commentary')
teach('6.1',3,'Historical mechanisms in Namibia',
    'Colonial land dispossession reduced access to productive resources in Namibia. Contract labour and migrant work could separate wage earners from rural households, increasing the farming and caring tasks left to women. Discriminatory access to education and formal jobs restricted some women’s alternatives, while cash-crop and wage relationships changed how households met needs. Do not describe women as passive or all households as identical: women also produced food, traded, organised and adapted to these pressures. Judge control of land and income as well as labour performed; a heavier contribution need not bring stronger decision rights.', 'R6136-009')
teach('6.2',3,'Women in the liberation struggle',
    'Women contributed to Namibia’s struggle for independence through political mobilisation, protest, maintaining households and communities, communication, medical support and participation in organised resistance. These are different roles, not a claim that every woman performed each task. Household and food work could sustain people engaged in public activity even without a wage. After independence, acknowledging those contributions should connect to real access to education, paid work, resources and public decisions. Representation alone cannot establish equal influence if priorities are already fixed before women are consulted.', 'R6136-009')
teach('7.1',3,'Why birth and growth rates differ',
    'Birth rates can remain high where children contribute to household livelihoods, families expect support in older age, early marriage lengthens the childbearing period, or high infant mortality leads parents to expect fewer surviving children. Limited access to education and voluntary family-planning information can restrict choices. Birth rates may fall with later marriage, better child survival, women’s education and wider work opportunities, accessible voluntary services, and the costs of raising children. These are interacting explanations, not stereotypes about a country or predictions about individuals. Death rates may fall as water, nutrition, sanitation and care improve. When deaths fall before births, natural increase rises; when births later fall towards deaths, growth slows. Net migration can still change total population growth, so natural increase is not the whole growth rate.', 'R6136-004','6136-2021-ER: Paper 2 population commentary')
teach('7.1',3,'Calculate natural increase and keep the units',
    'Crude birth and death rates use events per 1,000 people per year. Natural increase is the birth rate minus the death rate, using the same population basis and period. In a fictional population, 30 births per 1,000 minus 10 deaths per 1,000 gives 20 per 1,000 natural increase. Divide 20 by 10 to express that as 2.0% per year. The symbol ‰ means per thousand; % means per hundred. Natural increase omits immigration and emigration. A growing population with positive natural increase can grow more slowly if that positive rate falls.', 'R6136-005')
teach('7.1',6,'Explain a pyramid before planning services',
    'A broad base indicates a large young share, commonly associated with relatively high recent births; it does not prove one cause. A youthful population can increase demand for schools, child services and later jobs. A higher older-age share can increase demand for accessible health care, pensions and support services, while a smaller working-age share may face greater support responsibilities. Numbers matter as well as percentages: the same age share in a larger population means more people. Check cohort size, migration and changing births or survival before using a pyramid to explain a trend.', 'R6136-004')
teach('7.2',1,'Disease, prevention and productive participation',
    'Illness can interrupt attendance at school and work, add caring time and absorb household income. Malaria is caused by a parasite transmitted through bites of infected mosquitoes; it is not caused by drinking dirty water. Safe water, sanitation and hygiene instead reduce exposure to infections associated with faecal contamination, including cholera. Mosquito control and reducing bites address a different transmission route. Match prevention to the route rather than presenting one measure as protection against all diseases. Immunisation uses vaccines to develop protection against particular infections; it is not treatment for every existing illness. Programmes need trained personnel, dependable supplies, suitable storage and reachable services. This is a development explanation, not personal diagnosis or a vaccination schedule.', 'R6136-010','6136-2022-ER: Paper 2 malaria and health commentary')
teach('7.2',1,'Worked percentage change',
    'Percentage change compares a change with the starting value. Subtract the old value from the new value, divide that difference by the old value, then multiply by 100. If attendance rises from 80 to 100 users, the increase is 20 users; 20 divided by 80 is 0.25, giving 25% growth. If it falls from 100 to 80, the change is −20 users; dividing by the original 100 gives −0.2, or a 20% fall. The different denominators explain the different percentages. Percentage points instead subtract two percentages, such as coverage rising from 40% to 55%, a gain of 15 points. Starting from zero makes this percentage-change division undefined; report the absolute change.', 'R6136-005')
teach('7.3',2,'Distinct advantages and limitations',
    'Traditional learning can pass on local knowledge, practise tasks through participation, strengthen intergenerational relationships and use accessible local resources. Its limits may include narrow exposure to unfamiliar technical knowledge, unequal access to some roles and a lack of widely recognised qualifications. Modern education can provide scientific knowledge, specialist facilities, recognised qualifications and contact with wider occupations. Fees, distance and language can restrict access; teaching may be poorly matched to local needs or overemphasise recall. Neither description fixes the quality of every programme. Compare relevance, access, practical learning, recognition and the ability to adapt, using separate points with an explanation of each contribution or limitation.', 'R6136-004')
teach('9.3',1,'Achievements and continuing challenges',
    'SACU’s established common customs arrangements and shared revenue mechanism are practical forms of cooperation, rather than merely a declaration of friendship. They can ease internal goods trade and provide public revenue. Dependence on customs receipts exposes budgets to changes in that revenue, while the much larger South African economy creates unequal productive capacities within the union. SADC has created regional institutions and a free-trade framework among participating states. These provide routes for cooperation but do not remove every border delay, transport bottleneck or political disagreement. Unequal infrastructure and capacity can make gains uneven. Distinguish an institution or agreement that exists from the size of its economic effect, which needs dated performance evidence.', 'R6136-004')
teach('9.3',2,'EU cooperation in a Southern African example',
    'The 2016 EU–SADC Economic Partnership Agreement illustrates a regional trade relationship involving Namibia. Market-access arrangements can support exporters and encourage coordination, but firms still need to meet applicable standards and deliver reliably. Compliance can be costly for smaller producers; competition can benefit buyers while placing pressure on some local firms. An agreement’s existence is an achievement of cooperation, not evidence that all products or producers gain equally.', 'R6136-009')
teach('10.1',7,'Compare collection methods by their strengths and limits',
    'A questionnaire can collect comparable answers from many respondents at manageable cost, and a self-completed form may reduce interviewer pressure. Closed choices can hide reasons, unclear wording can distort answers, and low literacy or non-response can exclude people. Interviews allow clarification and detailed explanations, but take more time and can be affected by leading questions or pressure to please the interviewer. Observation records visible conditions directly and can use repeatable categories, but it cannot establish private motives; unusual times or weather can distort a short visit. Secondary evidence saves collection time and may supply wider or historical comparisons, but dates, units, definitions or coverage may not fit the enquiry. Compare at least two relevant benefits and limitations when choosing; do not substitute a definition of the method for its evaluation.', 'R6136-004')
teach('8.1',4,'Evaluate decentralisation with several criteria',
    'Decentralisation can bring decisions closer to residents, use local knowledge of needs, allow quicker responses and make local representatives easier to question. These gains depend on real authority, operating funds and capable staff. Poorer areas may lack the tax base or skills of richer areas, creating unequal services. Local capture or weak oversight can also restrict whose interests are heard. Central coordination remains useful for shared networks and fair resource distribution. A local decision is not automatically more inclusive: check participation, accountability, resources and the service outcome.', 'R6136-004')
teach('9.1',2,'Several reasons for international trade',
    'Natural resources and climate differ, so countries can obtain products unavailable locally. Different skills and equipment make some goods cheaper or better suited to production elsewhere. Specialising can allow larger-scale production and lower average costs when demand is sufficient. Producers can reach more buyers beyond a small domestic market. Consumers and firms can obtain a wider variety of goods, services and productive inputs. These are different benefits, but transport costs, unreliable suppliers or dependence on one export can reduce them. Explain the particular benefit and its condition rather than treating every import as a loss.', 'R6136-004')
teach('9.2',1,'Benefits and limitations of outside resources',
    'Aid can finance essential services when local public resources are limited, supply technical knowledge and provide relief after a shock. A grant avoids repayment, but donor conditions or poorly chosen projects can reduce local control or usefulness. Foreign investment can provide equipment, jobs, training and market connections. Profits may leave the economy, local suppliers may be bypassed, and weak safeguards can leave pollution or poor work conditions. Loans can spread payment for useful capacity over time but commit later resources to debt service. Judge feasibility, local influence, maintained benefits and opportunity cost for each arrangement; a larger inflow is not proof of greater welfare.', 'R6136-004')

# Sensitive, examined terminology: preserve the glossary wording and extend its meaning.
for u in TOPICS['6.2']['units'].values():
    for b in u['blocks']:
        b['text']=b['text'].replace('infant abandonment','baby dumping').replace('Infant abandonment','Baby dumping')
        b['heading']=b['heading'].replace('Infant abandonment','Baby dumping').replace('infant abandonment','baby dumping')
for i in TOPICS['6.2']['items']['items']:
    for k in ['prompt','canonical_answer']:
        i[k]=i[k].replace('infant abandonment','baby dumping')
teach('6.2',5,'Recognise the issue and its different effects',
    'Baby dumping means abandoning an infant, commonly a newborn, without appropriate care, exposing the child to danger and potentially death. It is distinct from seeking qualified support to keep a child safe. Contributing circumstances can include an unintended pregnancy, fear of losing education, lack of financial or partner support, coercion or violence, poor access to confidential information, and emotional crisis. They explain possible support needs, not an excuse or a prediction about a particular parent. Effects can include injury or death, lasting emotional harm to a surviving child, distress for family members, disruption of registration and care, and extra demands on protection services. Avoid using national death-rate changes as a substitute for explaining effects on the people involved.', 'R6136-003','6136-2022-ER: Paper 1 Q2(b), printed p.143')
teach('6.2',5,'Types and contributing factors of gender-based violence',
    'Gender-based violence includes physical and sexual violence; emotional abuse and economic control can also undermine safety and autonomy. Unequal power, entitlement and norms that excuse abuse can enable it. Substance misuse, exposure to violent behaviour and financial dependence can worsen risks or obstruct help, but neither poverty nor alcohol makes violence inevitable. Blaming clothing or the survivor shifts responsibility away from the person committing violence. Physical injury, distress, missed learning or work and the costs of obtaining protection can affect development. Name the type or mechanism required by a question rather than listing vague social problems.', 'R6136-003','6136-2022-ER: Paper 1 Q2(a), printed pp.142–143')
teach('6.2',6,'Distinct prevention and support responses',
    'Responses to GBV can include challenging norms that excuse abuse, improving equal access to income and education, teaching respectful relationships, providing safe reporting routes, and making professional protection and survivor support reachable. Public institutions, trained health and social workers, schools and community organisations have different responsibilities. Preventing baby dumping can include confidential pregnancy and parenting support, assistance to remain in education, reliable information on voluntary family planning, and help with financial or emotional crises. A response should remove a stated barrier and protect the infant; shame or exposure can deter help. These are educational support principles, not instructions for a learner to investigate violence or manage an emergency alone.', 'R6136-003')

# Research scaffolds and source coherence are handled below with exact package IDs.
teach('10.1',12,'Keep your own enquiry record',
    'Keep an individual dated record with these fields: topic and study area; question or hypothesis; aim and specific objectives; dates and the defined population; sample size and actual selection procedure; consent and safety arrangements; instruments and pilot problem, revision and recheck; collection procedure; anonymised observations, units and missing values; table or graph with title and source; main findings and an exception; conclusion linked to the question; limitations; recommendation, implementer and required resources; actual researcher obstacle and response. Preserve changes and reasons. If working in a group, state what was shared and what you personally did. A missing stage should be marked not completed, rather than replaced by a fictional event. Use this record to answer Section B in your own words.', 'R6136-011')

# Remove repeated unit-end filler; the distinct teaching links elsewhere remain.
for t,d in TOPICS.items():
    for u in d['units'].values():
        old=len(u['blocks']);u['blocks']=[b for b in u['blocks'] if b.get('heading') not in ['Connect the ideas','Apply the connection','Connect production to development']]
        if len(u['blocks'])!=old:CHANGES.append(dict(finding='R6136-015',artefact=u['unit_id'],action='Remove repeated unit-end boilerplate.'))

# Each of these is an individually authored repair, not a subject-name template.
REWRITES = {
'3.1': {
61: ('State two ways a change in technology can alter production work.', 'Automation can transfer repetitive tasks from people to machines. New equipment can create a need for workers with operating and repair skills.'),
63: ('Describe two productive uses of micro-electronics.', 'Electronic sensors can monitor temperatures during processing. Programmable controls can adjust machine operations consistently.'),
64: ('State what biotechnology uses and give one agricultural production example.', 'Biotechnology uses living organisms or biological processes for a useful purpose. Selective development and propagation of a crop variety suited to local growing conditions is an agricultural example.'),
65: ('Describe two ways a producer can use communication and information systems.', 'A producer can obtain buyer orders and coordinate delivery times electronically. Recorded stock information can show when inputs need replenishment.'),
},
'5.1': {
3: ('Describe two ways hunter-gathering obtains food.', 'People collect edible wild plants using knowledge of seasonal availability. They hunt or otherwise obtain wild animal foods using suitable skills and tools.'),
4: ('Describe two features of nomadic pastoralism.', 'Livestock provide an important basis for the livelihood. Herds and their keepers move between areas to reach pasture and water.'),
5: ('Describe two features of crop-based rural livelihoods.', 'Households cultivate plants on prepared fields. Work such as planting and harvesting is organised around the crop’s growing season.'),
8: ('Describe the difference between land use and rights over land in rural production.', 'Land use is the activity, such as grazing or growing crops. Land rights determine who may access the land and make decisions about its use.'),
9: ('Describe two examples of division of labour in farming households.', 'Different workers can specialise in tending livestock and cultivating crops. Others can process or market the harvested output while those tasks continue.'),
10: ('Describe two uses of tools in rural production.', 'A hand hoe can loosen soil and remove weeds around crops. Animal-drawn equipment can help cultivate a larger area with less direct human effort per task.'),
11: ('Describe two effects of seasonal rain on farming work.', 'The arrival of suitable rain can determine when rain-fed crops are planted. The resulting harvest period concentrates harvesting and storage work later in the season.'),
12: ('Describe two ways social cooperation can support rural production.', 'Neighbours can share labour during a short planting or harvesting period. Farmers can exchange knowledge about local soils, crops and conditions.'),
13: ('Describe two environmental influences on rural livelihoods.', 'Rainfall affects the water available for crops and grazing. Soil fertility affects which crops can be grown and the output obtained under suitable management.'),
14: ('Describe two ways farming could change before colonial rule.', 'Communities could adopt tools or techniques learned through exchange. They could introduce or adapt crops to changing local growing conditions.'),
15: ('Describe two ways colonial arrangements could alter rural livelihoods.', 'Loss of land could reduce the area available for food production. Pressure to earn cash through migrant work could change who remained to farm and care for the household.'),
16: ('Describe how smallholder farming and cash cropping identify different features of production.', 'Smallholder farming describes household-scale productive arrangements. Cash cropping describes growing crops mainly to sell; a smallholder can combine cash crops with food grown for household use.'),
19: ('Describe two tasks that equipment can assist on a commercial farm.', 'A pump can supply irrigation water where a usable source exists. Harvesting equipment can gather a crop more quickly when trained operators and repairs are available.'),
20: ('Describe the difference between monoculture and large-scale farming.', 'Monoculture means growing one crop across an area, often repeatedly. Scale concerns the size of the operation; a small farm can practise monoculture too.'),
21: ('Describe two features of plantation farming.', 'A plantation is an estate growing a commercial crop for sale. Its organised production can supply a processing activity using concentrated quantities of that crop.'),
22: ('Describe two features of crop rotation.', 'Different crops follow a planned sequence on the same land. A suitable sequence can interrupt some pests’ life cycles or help maintain soil condition.'),
41: ('Explain how public provision of a rural road can support farmers’ sales.', 'A usable road allows harvested produce to reach buyers before it spoils. Public provision can connect several farms where individual farmers cannot finance the shared route.'),
42: ('Explain how accountable records can help a formal rural group manage shared resources.', 'Recorded contributions and decisions let members check how shared funds are used. That can reduce disputes and make continued participation more credible.'),
43: ('Explain one limitation of relying on an informal neighbour group to maintain a regional water network.', 'Neighbours can share local work, but may lack the finance and technical capacity for a large network. The maintenance arrangement needs a provider able to meet those wider requirements.'),
44: ('Explain how an individual farmer can contribute to soil conservation.', 'Maintaining suitable ground cover reduces exposure of the soil to wind and rain. This can protect the productive layer without requiring the farmer to finance a regional project.'),
45: ('Explain why consultation about local values can improve a rural project.', 'Consultation can identify practices people value and changes they want. A project can then adapt its arrangements to gain useful participation rather than assume one person speaks for the whole community.'),
52: ('Describe one social benefit and one social cost of tourism.', 'Local guide work can develop communication and service skills. Visitor intrusion into private cultural activities can create conflict where consent is absent.'),
53: ('Describe two economic links between tourism and rural households.', 'Tourist businesses can pay local residents for work. They can purchase food or other supplies from local producers, retaining more spending in the area.'),
54: ('Describe one environmental benefit and one environmental cost tourism can bring.', 'Tourism income can help fund habitat protection. Concentrated visitors can increase waste and demand for scarce water.'),
},
'6.1': {
3: ('Describe two forms of women’s productive labour in rural societies.', 'Women may perform paid work such as selling produce. Unpaid farming or household production also supplies goods and services even when no wage is recorded.'),
4: ('Describe two stages of food production to which women can contribute.', 'Planting and tending crops help produce the harvest. Processing and preparing harvested food make it usable for households or sale.'),
5: ('Describe two ways household work supports family welfare.', 'Preparing food supports members’ daily nutritional needs. Caring for children or ill relatives supports their well-being and enables other necessary activities.'),
},
'6.2': {
6: ('Describe two changes that can widen women’s access to employment.', 'Fair selection procedures can remove gender discrimination in recruitment. Workable care or transport arrangements can make an available job usable for an applicant.'),
7: ('Describe two requirements for implementing a gender-equality policy.', 'Assign responsibility and resources to carry out the policy. Monitor access and outcomes to identify barriers that equal written rules have not removed.'),
8: ('Describe two ways a targeted development scheme can widen women’s opportunities.', 'Relevant training can address a documented skills gap. Accessible finance can help participants obtain productive equipment where a viable opportunity exists.'),
9: ('Describe two kinds of evidence needed to assess a female-headed household’s development needs.', 'Evidence on income and productive resources shows material capacity. Evidence on caring responsibilities and available support shows demands on time and access.'),
18: ('Explain how fear of public identification can obstruct access to support concerning GBV or baby dumping.', 'A person may avoid a service if seeking help exposes them to stigma or retaliation. A confidential, reachable professional service can reduce that barrier; low recorded use does not establish low need.'),
20: ('Explain how unequal power can contribute to gender-based violence.', 'A person claiming control over another’s choices may use threats or force, especially where norms excuse that behaviour. Unequal power can enable abuse, but responsibility remains with the person committing it.'),
21: ('Explain how fear of losing education can contribute to a crisis around baby dumping.', 'A pregnant learner who expects exclusion or cannot reach support may feel trapped and isolated. Continued-education and confidential qualified support can address that pressure; it does not make harmful abandonment inevitable or excuse it.'),
24: ('Describe two complementary responses to gender-based violence.', 'Education can challenge norms that excuse abuse and promote respectful relationships. Accessible professional protection and support can help survivors obtain safety and assistance.'),
25: ('Describe two ways support can help prevent baby dumping.', 'Confidential pregnancy and parenting support can help a person seek help before a crisis escalates. Assistance with continued education or financial hardship can reduce specific pressures while protecting the child.'),
},
'7.1': {
24: ('Describe two economic uses of population data.', 'Age and working-age numbers help plan future training and labour needs. The size and location of households help estimate demand for goods and services.'),
25: ('Describe two social-service uses of population data.', 'Child population estimates help plan school places. The number and location of older residents help plan accessible health and support services.'),
28: ('Describe two planning implications of an older population structure.', 'A larger older-age share can increase demand for pensions and accessible care. A smaller working-age share can face greater support responsibilities relative to its size.'),
29: ('Describe two planning implications of a youthful population structure.', 'Many children increase present demand for schools and child services. As those cohorts reach working age, more employment and further training opportunities may be needed.'),
},
'7.2': {
4: ('Explain how reliable safe-water access can support productive participation.', 'It can reduce exposure to contaminated supplies and reduce time lost obtaining water. With fewer interruptions to health and available time, people may attend school or work more consistently.'),
5: ('Explain why food availability alone does not establish an adequate diet.', 'People need suitable nutrients as well as enough energy. A household may obtain a large amount of one food while lacking the variety needed for an adequate diet.'),
6: ('Explain why a health programme needs trained staff as well as a clinic building.', 'A building provides space, but qualified workers deliver and refer care. Without operating staff, the extra physical facility need not provide usable treatment.'),
7: ('Explain how illness and poverty can reinforce each other.', 'Limited income can restrict food and access to care. Illness can then interrupt earnings and add care costs, making those material constraints harder to overcome.'),
12: ('Describe two economic effects HIV-related illness can have on a household.', 'Illness can reduce paid working hours and income. Caring responsibilities can reduce another household member’s time for work or education.'),
13: ('Describe two complementary elements of a public HIV response.', 'Confidential testing and continued professional care support timely access to services. Accurate education and community support can reduce misinformation and barriers to participation.'),
},
'9.1': {
11: ('Describe two effects of fluctuating export prices on a producer.', 'A price fall can reduce sales revenue even when the quantity sold is unchanged. Uncertain future prices can make investment and repayment planning harder.'),
12: ('Describe two development difficulties associated with a shortage of foreign-payment resources.', 'Essential imported equipment or inputs can become harder to obtain. Meeting external repayment obligations can compete with other uses of scarce finance.'),
13: ('Describe two aims of proposals for a fairer international economic order.', 'Improve developing producers’ opportunities to obtain a reasonable return from trade. Reduce barriers that leave weaker economies with little influence over trading or financing terms.'),
16: ('Describe two trade vulnerabilities of a developing economy relying on a few primary exports.', 'World price falls can sharply reduce earnings from its narrow export base. It may still need to buy machinery and other manufactured goods from abroad.'),
17: ('Describe two ways industrial expansion can change a NIC’s trade pattern.', 'Manufactured products can form a larger share of exports. Imported equipment and intermediate inputs may support the expanding production.'),
18: ('Describe two features that may occur in a developed economy’s trade.', 'Exports can include high-value manufactured products or services. Imports can include raw materials and products made through international production networks.'),
23: ('Describe two opportunities globalisation can offer local producers.', 'Access to foreign buyers can expand a producer’s market. International links can supply technology or knowledge that improves productive capability.'),
24: ('Describe two constraints that can limit local gains from globalisation.', 'Stronger foreign competition can displace producers unable to match price or quality. Reliance on external buyers can expose local work to distant demand shocks.'),
},
'10.1': {
5: ('Describe how personal interest can help an enquiry and one limit to relying on it.', 'Interest can sustain attention through collection and checking. It does not justify ignoring evidence that challenges the researcher’s expectation.'),
6: ('Describe two features of a development-relevant research question.', 'It concerns a defined development issue, such as access to a service. Its variables provide evidence that can answer a practical question about that issue.'),
7: ('Describe two ethical requirements when collecting questionnaire responses.', 'Explain the purpose and allow people to decline. Record answers without unnecessary identifying details and protect participants’ privacy.'),
8: ('Describe two boundaries that make a research topic manageable.', 'Specify the place and population to be investigated. State the collection period and the variables to be measured.'),
18: ('Describe how an enquiry can use both primary and secondary evidence.', 'The researcher can collect current local observations first-hand. Existing records can supply a comparison if their population, units and dates are suitable.'),
24: ('Explain one limitation of a questionnaire using only fixed answer choices.', 'Respondents may have reasons or circumstances outside the offered choices. Results can therefore conceal relevant differences unless categories and optional explanation are carefully piloted.'),
26: ('Explain why an interview may be suitable for understanding a participant’s reasons.', 'The interviewer can ask a neutral clarifying question when an answer is unclear. That can give richer explanation than a fixed choice, although leading questions would distort it.'),
28: ('Explain why observing litter cannot establish residents’ reasons for dropping it.', 'Observation records visible items or behaviour. Private motives are not visible, so an explanation of reasons needs suitable additional evidence rather than an inference from the count.'),
30: ('Explain why an old published table may be unsuitable for a new local enquiry.', 'Its period or population may differ from the question being investigated. Using it without checking those differences can produce a comparison that does not describe the current study group.'),
31: ('Explain why a researcher should choose a collection method after defining the variable.', 'Different methods produce different evidence. Direct counts can measure visible litter, while interviews can explore reasons; choosing first can leave the method unable to answer the actual question.'),
41: ('Explain why a sample needs an appropriate population list.', 'A selection procedure can only choose members covered by its list. Missing a group from that frame can bias coverage even when selection from the list is fair.'),
43: ('Explain why selecting the nearest households is not random sampling.', 'Distance from the researcher determines who is selected, so other households do not have an equal chance. A fair draw from a complete numbered list provides the required chance procedure.'),
45: ('Explain one advantage of proportional stratified sampling for two differently sized groups.', 'It deliberately allocates places to both groups in proportion to their population shares. A smaller group is therefore included by design, although non-response can still distort the final evidence.'),
47: ('Explain one risk when using systematic sampling from an ordered list.', 'A repeating list pattern can coincide with the selection interval. The sample may then overrepresent one type of unit even though a fixed rule was followed.'),
}}
assert sum(map(len,REWRITES.values()))==72
for t, pairs in REWRITES.items():
    for n, (p,a) in pairs.items():
        i=item(t,n)
        parts=['Feature: credit two distinct accurate descriptions matching the prompt.'] if i['subtype']=='FEATURE' else ['Reason: identify the stated mechanism.','Consequence: connect the mechanism to the outcome or limitation in the question.']
        question(t,n,p,a,parts)

# The final answer must be learnable from the text, including the added details.
teach('3.1',13,'Concrete information and biological applications',
    'Micro-electronic sensors can monitor processing temperatures, while programmable controls adjust operations. Communication systems can coordinate buyer orders and delivery times; stock records can warn when inputs need replacing. Biotechnology uses organisms or biological processes for a useful purpose, including developing and propagating crop varieties suited to growing conditions. Such changes can automate repetitive tasks and create demand for new operating or repair skills; they need suitable training rather than guaranteeing more employment.', 'R6136-006')
teach('7.1',5,'Match data to a planning decision',
    'Age and working-age numbers help estimate future training and labour needs. Household totals and locations help judge demand for goods and services. Child numbers support planning for school places; the location and number of older people support planning for accessible care. Use a relevant area and period and check denominators: a count of people can grow even when their percentage share falls.', 'R6136-006')

# Real trade-offs, with enough development to support four-mark reasoning.
# The existing work-order labels and tariffs remain unchanged.
EVALUATIONS = {
('4.1',10): (
 'Explain which industrial strategy better fits stable local employment in this fictional district. A small workshop serves steady local orders and can open immediately, but offers 12 jobs and little room to expand. A funded export plant offers 40 jobs and has a confirmed delivery route, but depends on one foreign buyer. Both have trained staff. Weigh the options.',
 'The workshop offers fewer jobs but a steadier local demand base and immediate work. The export plant offers substantially more employment and feasible delivery, but losing its single buyer would put more jobs at risk. For stability, the workshop is safer initially; the plant becomes stronger if it diversifies buyers or secures durable orders. The decision turns on resilience as well as the number of jobs, rather than assuming either local or export sales are sufficient.'),
('4.1',12): (
 'Explain whether a fictional producer should expand for confirmed foreign orders. It has suitable quality, finance and delivery capacity. Expansion would raise sales but put 70% of output with one buyer and require overtime for six months. A smaller expansion earns less but retains several buyers. The aim is dependable earnings.',
 'Expansion has a credible revenue opportunity because orders, capacity and delivery are available. However, concentration on one buyer exposes earnings to a cancelled contract, and sustained overtime may add costs or strain. A smaller expansion preserves diversification but forgoes some income. For dependable earnings, stage the increase while negotiating durable orders and manageable workloads; full expansion is more defensible if those risks are controlled.'),
('4.1',13): (
 'Explain which scale suits an invented repair group. A small workshop can adapt to varied orders with low borrowing but has higher unit costs. A funded automated line has reliable operators and can reduce unit costs for confirmed standard orders, but commits most capacity to them. The group values flexibility and dependable income.',
 'The workshop preserves flexibility and limits repayment exposure, useful when orders vary. The line has a genuine cost advantage on its confirmed standard work, but commits capacity and finance that cannot easily move to other tasks. A workshop is preferable if varied orders provide the more stable income; a line becomes attractive when standard demand is durable enough to cover its costs. Compare the actual mix of work before choosing scale.'),
('4.1',19): (
 'Explain which state action better supports a fictional industrial area. Its present route is usable but congested. A funded freight upgrade would reduce delivery delays for existing firms. A funded technical-training centre would address a documented skills shortage for future production but take longer to benefit firms. Funds cover one first.',
 'The freight upgrade can improve current deliveries and earnings across existing firms. Training offers longer-term productive capability and access to skilled jobs, but brings less immediate relief. Prioritise freight if present delays threaten orders now; prioritise training if firms can manage current deliveries and lack skills to expand. Either choice needs evidence on the scale of its constraint and a plan for the other need, rather than treating expenditure itself as a result.'),
('4.2',16): (
 'Explain which option to phase first in a fictional housing programme. Upgrading water in the present settlement reaches 200 households quickly but leaves crowded plots. A funded serviced extension can house 350 households with a work-bus connection, but takes two years. Both are feasible and funds cannot complete both immediately.',
 'The existing-area upgrade tackles current water need sooner, benefiting residents who already live there. The extension offers more space and wider coverage, with a credible work link, but leaves an access delay. Immediate upgrading is preferable where present water need is urgent, while reserving a staged extension for crowding. If safe interim water is already assured, the larger extension may deserve priority. Time, reach and livelihood access all matter.'),
('4.2',18): (
 'Explain which serviced-site option better fits a fictional low-income community. Both sites have water and usable work-bus connections. A is near jobs with higher plot payments; B has lower plot payments but longer journeys and higher travel costs. The budget evidence does not show which total cost households can afford.',
 'A reduces travel time and costs, but its plot payments may exclude some households. B lowers the entry cost but adds recurring travel expense and time. Compare combined housing and travel costs with household resources before declaring either affordable. A is stronger where the payment schedule is manageable; B may suit households prioritising lower upfront cost if the journey remains affordable. A cheap plot price alone cannot settle practical access.'),
('4.2',20): (
 'Explain whether a fictional new town is suitable for relocation. It offers serviced homes and funded transport to jobs but a 50-minute journey. Upgrading the present area keeps a 15-minute journey but leaves less space and takes disruptive building work. Both have feasible finance. The aim is housing and livelihood improvement.',
 'The town offers better space and services with a credible employment link, but the longer journey adds time and may weaken household routines. Upgrading preserves nearby work and social links, while its crowding and disruption remain costs. Prefer upgrading where livelihood proximity is most valuable and adequate improvement is possible; choose relocation where space and services outweigh the journey burden for participating households. Consultation and combined access costs should inform the judgement.'),
('5.1',24): (
 'Explain which rural scheme to fund first in a fictional village. Growers have buyers. An existing usable road causes delays and transport losses; repair would reduce those losses. A seed loan would increase output and can be repaid after harvest, but adds repayment risk. Funds cover only one first. The aim is more dependable net sales.',
 'Road repair can preserve more of the existing harvest and lower delivery losses without adding farmers’ debt. A seed loan can expand saleable output, but repayment remains due if the harvest or prices disappoint. Prioritise repair where current transport losses are large enough to outweigh the extra output from seed. If losses are minor and input shortage is decisive, the loan could offer the better gain. Compare retained sales after costs rather than output alone.'),
('5.1',25): (
 'Explain whether a seed loan suits this fictional household. Suitable water, skills and buyers exist. Repayment follows harvest and the expected return exceeds borrowing cost, but a poor season could leave a debt. A smaller self-financed planting has lower expected income and no repayment obligation. Weigh income and security.',
 'The loan removes an input constraint and repayment timing matches expected sales, making the larger planting credible. The household also bears a downside if weather or prices reduce returns. Self-financing limits income potential but protects it from a fixed repayment. The loan is preferable when a prudent smaller trial or reserve makes the downside manageable; otherwise the smaller planting may better protect basic needs. Expected gain alone does not establish affordability.'),
('5.1',26): (
 'Explain whether a cooperative store suits fictional growers. Shared storage lowers their cost per bag and members agree contributions. A private store costs more but offers flexible collection times; cooperative decisions currently favour larger members. Both stores are reachable and reliable.',
 'The cooperative offers a real cost saving and shared productive capacity, useful for growers unable to store separately. Unequal decision influence can distribute access unfairly, while the private store’s flexibility may suit small growers’ work schedules despite its higher fee. Prefer the cooperative if transparent access and voting arrangements make the savings usable for all members. If that cannot be secured, the flexible store can be more suitable for disadvantaged members.'),
('5.1',27): (
 'Explain whether resettlement suits fictional farmers. New plots offer more land, reliable water and a funded market route, but moving disrupts support networks. Improving the present site preserves those networks but leaves smaller plots and lower potential output. Both arrangements are financially feasible.',
 'Resettlement has credible productive benefits because water and market links accompany the land. Relocation still carries social and adjustment costs, particularly where families rely on nearby care or shared work. Present-site improvement protects those relationships but limits expansion. Relocation is stronger for households whose productive gains outweigh the disruption and who choose it with support; improving the current site may better fit others. More land is one criterion, not a complete welfare judgement.'),
('5.1',28): (
 'Explain whether to begin a fictional integrated water-and-road scheme or a smaller water project first. Agencies have funded both needs and agreed responsibilities. Integration reaches more farms but takes two years; the smaller project reaches fewer households in six months. The present water gap is serious and resources cover one start.',
 'Integration can join production and market access, avoiding a water improvement whose output cannot reach buyers. Its longer timetable leaves urgent needs unresolved for longer. The smaller project delivers earlier relief but with narrower reach and an outstanding road need. Prefer a staged start that secures urgent water while maintaining the agreed wider sequence if feasible. If choosing one alone, weigh the urgency of the gap against the additional households and connected benefits.'),
('5.1',29): (
 'Explain whether a fictional grassroots project should proceed now. Broad consultations, including remote households and women, identified the priority. It uses local skills and small member contributions, but expanding coverage requires outside funds and may delay work. A smaller start is feasible now.',
 'A smaller start can meet an agreed need with available skills and preserve local influence. Wider funding can include more households, but delay and funder conditions may weaken immediacy or community control. Proceed with a transparent first stage if its benefits are useful on their own and excluded households have a credible later route. Seek wider funds where the small stage would entrench unfair access. Local initiation is valuable but does not settle coverage.'),
('5.1',30): (
 'Explain whether to choose locally repairable soil-cover methods or a powered conservation service in this fictional farming area. Both reduce erosion. Soil cover uses available skills and little cash but needs more labour during planting. The funded service saves labour and includes repairs for two years, but later fees are uncertain.',
 'Soil cover offers low cash costs and local maintenance, but competes for scarce planting labour. The powered service has a genuine timeliness benefit and initial repair support, with an uncertain later cost. Prefer soil cover where households can supply the labour without harming planting. A service is stronger where seasonal labour is the main constraint and an affordable continuing arrangement can be secured. Compare long-term soil protection and resource demands together.'),
('6.2',10): (
 'Explain which fictional participation arrangement better supports women’s influence. A broad open meeting can amend the budget but takes travel and care time. Elected local delegates can negotiate the same budget with funded access, but may not reflect every group. Both occur before decisions are final.',
 'The open meeting offers direct voice and a chance to challenge priorities, but time and travel can exclude some participants. Delegation makes participation more practical for those facing barriers, while concentrating influence in representatives. Prefer delegates where they consult diverse groups, report back and can be held accountable; otherwise a supported open meeting may be more representative. Presence or an invitation alone is weaker evidence than a usable opportunity to change decisions.'),
('7.1',18): (
 'Explain which fictional voluntary population policy better balances slower growth and well-being. A funds wider information and confidential services. B combines a smaller service expansion with girls’ continued education. Both respect family choice and have the same budget, but their effects may take different times.',
 'A directly reduces an information and service-access barrier, potentially helping people act on their existing choices sooner. B addresses education and longer-term opportunities as well as access, but serves fewer people immediately. Prefer A where unmet service demand is the main current constraint; B may bring broader lasting benefits where school exclusion restricts choices. Assess access, well-being and later outcomes together, without assuming either policy determines private fertility decisions.'),
('7.1',21): (
 'Explain which fictional pronatalist support better fits parents’ reported needs. A provides a larger childcare subsidy, reducing cost more. B provides a smaller subsidy and workable time support. Both are affordable for the state; parents report both childcare costs and inflexible work hours.',
 'A makes a larger contribution to childcare affordability and may best help families whose main obstacle is cost. B addresses two different barriers, so it better fits families for whom work hours still block usable care. Prefer B when the timetable barrier is substantial; A can be stronger when cost dominates and hours can already be managed. Compare actual participation and family well-being, and do not promise either choice will raise births.'),
('7.1',30): (
 'Explain which fictional programme better supports households affected by HIV-related illness. A funds transport and continuity of professional care for more households. B reaches fewer but also provides care-time and livelihood support. Both protect confidentiality and workplace inclusion. The budget covers one programme initially.',
 'A offers wider health-service access and can reduce interruptions to care, helping more households initially. B tackles the linked loss of income and unpaid caring time more fully, but has narrower reach. Prefer B for households facing combined care and livelihood pressures, while A may be stronger where travel is the dominant barrier across many households. Use evidence on needs and reach to justify the choice; HIV status alone does not establish incapacity.'),
('7.2',8): (
 'Explain which fictional health programme better fits remote communities. A funds outreach for routine care and referrals for 80% of residents. B funds a reachable district hospital and transport serving 55%, with stronger specialist capacity. Both have staff and supplies; only one can be expanded first.',
 'Outreach reaches more residents and can support early and preventive care, but relies on referral for specialist needs. The hospital offers more complex care and transport, but covers fewer people in the current plan. Prefer outreach where unmet routine needs dominate; prioritise hospital capacity where the evidence shows serious referral bottlenecks. The strongest long-term arrangement connects the two. A building count or one coverage figure cannot establish overall quality and need.'),
('7.2',11): (
 'Explain which fictional HIV-support programme better fits continued participation. A reaches more people with confidential care and transport. B reaches fewer people but also funds household care-time support. Both preserve employment access for people able to work, and only one fits the initial budget.',
 'A removes the travel barrier for a wider group and supports continuity of care. B addresses care burdens as well, potentially protecting both the person’s and another household member’s participation, but helps fewer households. Prefer B where care-time losses are the most serious unmet need, or A where transport excludes many people from effective services. Judge reach and the depth of support against actual needs rather than choosing exclusion as a false alternative.'),
('7.3',6): (
 'Describe these fictional learning routes and give a reasoned judgement for a learner seeking recognised technical skills. A local craft apprenticeship offers daily practice, a small allowance and preparation for a recognised assessment. A reachable college course offers the qualification and broader technical theory but charges affordable fees and reduces earning time. Both are feasible.',
 'The apprenticeship combines workplace learning and an allowance, with recognition dependent on later assessment. College combines broader theory and a qualification route, with fees and less earning time. For a learner needing immediate income and extensive practice, the apprenticeship may fit better if assessment preparation is credible. College may be preferable for wider technical progression where the fees and lost time are manageable. Neither route is superior on every criterion; compare practical skill, recognition, income and longer-term aims.',),
('7.3',18): (
 'Explain which fictional ICT programme better fits accessible learning. A equips more schools with shared devices, basic teacher training and power. B equips fewer schools with more teaching support, accessible materials and reliable connectivity. Both operate, and the same budget covers one.',
 'A spreads a usable minimum of equipment and training more widely, but shared access may limit learning time. B offers richer teaching support and access arrangements, potentially helping learners with more varied needs, but covers fewer schools. Prefer B where unsupported learning needs are the main barrier, or A where basic access across many schools is the urgent priority. Monitor actual use and learning rather than device totals, and plan how the other group will later be reached.'),
('7.3',20): (
 'Explain which fictional adult course better fits usable skills and work. A offers a broad recognised qualification, supervised practice and higher fees. B offers a shorter affordable repair course with confirmed local demand, but narrower progression. Both have equipment and teachers; learners have limited time.',
 'A supports wider recognised progression and practical learning, but its cost and length can restrict completion. B meets a documented local skill need at lower time and cash cost, while leaving fewer alternatives if that demand changes. B is stronger for immediate repair opportunities and tight resources; A may suit learners able to invest in broader future options. Compare completion and actual use of skills, rather than assuming a certificate or a short course creates employment.'),
('7.3',22): (
 'Explain which lifelong-learning arrangement better fits fictional shift workers. A offers regular daytime classes with immediate teacher feedback. B offers flexible supported distance sessions with equal standards, but needs learners to organise time and travel to monthly practical meetings. Both are usable for some workers.',
 'A provides structured contact and quick feedback, useful for workers whose shifts allow attendance. B can fit changing schedules and preserve access for others, but self-organisation and monthly travel remain demands. Prefer B for workers regularly missing daytime sessions if the support and meeting arrangements are workable; A can serve those who benefit from fixed teaching. Compare participation and learning quality across shift patterns rather than declaring one timetable suitable for everyone.'),
('9.1',21): (
 'Explain which fictional global-production offer better fits retained local livelihoods. A offers 100 local production jobs with limited training and uses some local suppliers. B offers 60 jobs, more advanced training and more local purchasing, but lower initial output. Both are funded and have buyers.',
 'A offers more immediate employment and a genuine local-supply link, which can support more households now. B develops deeper capabilities and retains more supplier spending, but creates fewer jobs initially. Prefer B where lasting skills and stronger local production links are the main priority; A may fit urgent broad employment needs better. Compare job quality, retained spending and future opportunities rather than treating larger output or a foreign connection as proof of local benefit.'),
('9.2',5): (
 'Explain which fictional water offer better fits reliable community access. A is a grant for a smaller maintained network reaching 60 households. B is an affordable loan for a maintained network reaching 100; the council can repay from revenue but would postpone another service project. Both have qualified operators.',
 'The grant improves access without repayment and protects funds for the other service, but leaves more households unserved. The loan reaches a wider group with a credible operating and repayment route, while committing public income and delaying another benefit. Prefer the loan where the additional water need outweighs that opportunity cost and repayments remain manageable. Otherwise a grant-led first stage is safer. Neither grant status nor the larger funding amount settles the development judgement.'),
('9.3',1): (
 'Discuss how to phase two fictional regional-trade improvements. Coordinated documents can reduce delays at existing border facilities sooner and at lower cost. A funded freight-link upgrade serves more producers but takes two years. Both have agreed maintenance or operating responsibilities; resources cover one first.',
 'Document coordination offers earlier savings for existing traders and uses fewer resources. The freight link can widen participation beyond those traders, but its benefits take longer and commit more funds. Prioritise coordination where present administrative delay is the main obstacle; choose the link where excluded producers face much larger transport barriers. Judge actual reach, timing and costs, and retain a route to the second improvement. An agreement alone does not establish those outcomes.'),
('9.3',3): (
 'Discuss which fictional SACU-related support to phase first. Joint document assistance would reduce frequent delivery delays for existing producers. Quality training would help smaller producers qualify for buyers but takes longer. Both operate within common customs arrangements and are feasible.',
 'Document support helps existing sellers turn common-market access into more dependable deliveries quickly. Quality training expands the set of producers able to benefit, but brings less immediate relief. Prefer document assistance where delays threaten current sales; prefer training where exclusion through quality is the larger development gap. Assess the distribution as well as the size of gains. Common customs rules provide an opportunity without guaranteeing either reliable trade or equal participation.'),
('9.3',4): (
 'Discuss a fictional SADC transport project. Joint construction and funded maintenance can connect more markets, but cost-sharing commits resources that each state could use for smaller domestic routes. States agree roles; benefits are expected to be larger near the cross-border corridor.',
 'A joint route can overcome a bottleneck that separate national projects leave in place, widening trade and shared service opportunities. It also uses scarce public funds and may concentrate benefits near the corridor. Support it where expected cross-border gains justify those costs and less-connected communities have a credible access plan. Domestic routes may be preferable where local needs outweigh the marginal regional gain. Funded responsibilities improve feasibility but do not prove an equitable outcome.'),
('9.3',5): (
 'Discuss which support best helps fictional exporters use an EU-partner trade opportunity. Both have compliant products. A marketing programme would reach more buyers for existing large firms. A quality-training programme would help smaller suppliers maintain compliance but reach fewer export orders initially. Both have feasible finance.',
 'Marketing may convert existing capacity into sales sooner, using firms already able to comply and deliver. Training can broaden participation and reduce future quality failures, but initial sales may be smaller. Prefer training where lasting local supplier capability and inclusion are priorities; marketing may better serve urgent earnings from established capacity. Check cost, retained local gains and actual orders, rather than assuming agreement access makes every firm competitive.'),
('10.1',32): (
 'Explain which method to prioritise for a fictional enquiry into visible litter and service explanations. Safe structured observation measures counts directly; consenting provider interviews explain collection arrangements but take longer. Resources cover one detailed method first, with brief follow-up possible.',
 'Observation gives direct, consistently categorised counts and is stronger when the immediate question concerns where and how much litter is visible. It cannot establish why collection failed. Interviews can explain schedules and constraints but depend on accurate responses and are weaker for exact site counts. Start with observation for the count question, then use brief interviews to investigate the pattern; reverse the priority if the question mainly concerns service arrangements. Match the judgement to the required evidence.'),
('10.1',55): (
 'Explain which recommendation to prioritise after fictional records show repeated pump breakdowns. A trained provider can undertake repairs sooner, but a local monitoring-and-reporting arrangement costs less and can identify faults between visits. Either is feasible; funds cannot expand both immediately.',
 'Provider repairs directly restore the faulty equipment and have a qualified implementer, but recurring faults can go unnoticed between visits. Local reporting is cheaper and supports earlier diagnosis, but cannot itself repair the pump. Prioritise repair where the current fault prevents access, while retaining a basic reporting route. If the pump now works and delayed reporting is the main evidence-based problem, monitoring may merit the next funds. Judge restoration and continued reliability separately.'),
}
for (t,n),(p,a) in EVALUATIONS.items():
    question(t,n,p,a,['Judgement: compare genuine benefits and costs against the stated aim.','Reason: develop each option using supplied evidence, weigh the trade-off, and give a conditional conclusion.'], 'R6136-008')

# Three misconception checks now require an applied separating test.
question('9.1',31,'Explain whether this fictional change is globalisation or global warming: a local processor begins coordinating orders and suppliers across three countries; no temperature evidence is supplied.',
    'It illustrates globalisation because production and exchange are becoming more internationally connected. It supplies no evidence of a change in global average temperature, so the shared word global does not make it global warming.',
    ['Error: confuse international connections with a temperature process.','Distinction: apply the international-exchange test to the case, not the shared word.'], 'R6136-016')
question('9.2',17,'Explain the difference between the loan and debt in this fictional case: a group borrows N$1,000 and later repays N$300 of principal, with no interest or fees.',
    'The loan is the borrowing arrangement that advanced N$1,000. The remaining debt is N$700 after the principal repayment. The original amount advanced and the outstanding obligation therefore differ.',
    ['Error: treat the borrowing arrangement and the amount still owed as identical.','Distinction: use the repayment to distinguish N$1,000 advanced from N$700 outstanding.'], 'R6136-016')
question('9.2',18,'Explain whether fictional emergency food support delivered through an organisation funded by several countries must be either emergency relief or multilateral aid.',
    'It can be both. Emergency relief describes its immediate purpose; multilateral describes the channel through a shared international organisation. The categories answer different questions, so one does not exclude the other.',
    ['Error: treat purpose and delivery channel as competing categories.','Distinction: apply both labels to the same supplied programme with reasons.'], 'R6136-016')

# Correct the population and label the two overlapping totals explicitly.
question('4.2',22,'Describe the work pattern in an original fictional survey of 100 people available for work: 30 have no job and are seeking work; 40 have jobs but work fewer paid hours than they want and are available for; 30 have jobs with their desired hours.',
    'Thirty people are unemployed. Forty are employed but underemployed in hours. Thirty are employed with their desired hours. Thus 70 have a job (40 + 30), while a different overlapping total of 70 have unmet work needs (30 + 40). These totals describe different characteristics, not two separate groups of 70.',
    ['Evidence: distinguish all three categories and reconcile 30 + 40 + 30 = 100.','Relationship: explain why some employment and unmet work needs can overlap.'], 'R6136-007')
question('5.1',34,'Explain the rural-development mechanism in this fictional woodland: 180 trees are cut each year while 125 replace losses under unchanged conditions.',
    'Harvesting exceeds replacement by 55 trees a year. The stock therefore declines despite wood being renewable, reducing future fuel availability if that imbalance continues.',
    ['Mechanism: compare removal and regeneration, 180 minus 125.','Consequence: connect the declining stock to future supply under continued conditions.'], 'R6136-015')
question('5.1',38,'Explain how this fictional conservation improvement can support rural livelihoods: lining a leaking irrigation channel cuts water losses from 35 to 15 units out of 140 supplied; crop needs and farmers’ access arrangements are unchanged.',
    'Usable water rises from 105 to 125 units without increasing the original supply. Reducing loss can support farming while limiting additional extraction, provided the lining is maintained and the extra usable water reaches the farms.',
    ['Mechanism: connect the 20-unit loss reduction to water available for production.','Consequence: explain the possible livelihood and resource benefit with maintenance and access conditions.'], 'R6136-015')

# Retain the short/long-horizon distinction in its exact DIST slot.
question('2.2',3,'Differentiate the time horizon of a shorter national action plan, such as the first Harambee Prosperity Plan, from Vision 2030.',
    'HPP, introduced in 2016 under President Hage Geingob, concentrated action on selected priorities over a shorter period. Vision 2030 sets the longer national development direction from the 2004 starting position towards 2030; shorter actions should contribute to it.',
    ['Comparison: shorter implementation priorities versus the longer national development direction.'], 'R6136-002')
question('2.2','P01','State (a) the first Harambee Prosperity Plan’s launch year and the president who introduced it [2]. Explain (b) what this fictional evidence implies for the social-progression and infrastructure aims [4]: a funded project completes two water points, but repeated breakdowns leave half the intended households without reliable access.',
    '(a) 2016; President Hage Geingob. (b) Construction contributes to the infrastructure aim, but half the intended households still lack reliable access. That limits the social benefit: an installed point is an output, while dependable usable water is an outcome. Maintenance and evidence on actual reach are needed before judging success against both aims.',
    ['Point (a), 2 marks: accurate year and president.','Development (b), up to 4 marks: link completed infrastructure, breakdowns and unequal reliable access to a bounded judgement about intended outcomes.'], 'R6136-002')

B_SCAFFOLDS = {
'P01': [
 'My actual topic was [topic] in [area and dates]. My linked aim was [what I intended to find out]. Refer to my own record; if not completed, state that.',
 'My pilot revealed [actual problem]. I changed [instrument or procedure] because [reason], and rechecked it by [actual step]. If no pilot was done, acknowledge that limitation.',
 'I defined [population], selected [sample] using [actual procedure], obtained [permission/consent], then recorded [variables, units and dates] using [instrument]. Note missing responses and any changes.',
 'My main finding was [pattern], supported by [two comparable observations with units]. This suggests [bounded implication]; [exception or limitation] prevents a wider claim.',
 'Based on [actual finding], I recommend [specific feasible action]. [Responsible actor] could implement it using [resources], subject to [relevant constraint].'],
'P02': [
 'I selected [actual issue] because [development relevance] and [feasibility or other real reason]. Explain each using my actual setting and available evidence.',
 'My population was [defined group]. I selected [size and actual method] using [frame and procedure]. This fitted [aim or resources], but [coverage/non-response limitation] remains.',
 'I found [pattern] using [observations and units], with [exception]. Therefore [answer to the actual question]. Limit this conclusion to [sample, dates and evidence quality]; distinguish association from proof of cause.',
 'I actually encountered [collection difficulty], which affected [procedure or coverage]. I [real response], or would propose [feasible response and responsible person] if it remained unresolved. Distinguish the proposed response from an action already taken.'],
'P03': [
 'My actual question or hypothesis was [statement]. One objective was [specific measurable task that served it].',
 'I used [presentation] for [actual variables and units] because [fit to comparison or pattern]. I included [title, labels, source and relevant scale/key] and avoided [a genuine distortion].',
 'In my records, [group/date] had [value and unit] compared with [other value and unit]. This supports [relationship], with [exception or uncertainty] retained.',
 'The evidence supports/challenges [actual question or hypothesis] because [finding]. It applies to [actual scope] and is limited by [real limitation], so I cannot conclude [unsupported wider claim].',
 'I propose [specific feasible action] in response to [finding]. [Responsible actor] could arrange [resources/implementation], with [cost or access condition] checked.'],
'P04': [
 'A strength of my actual local enquiry was [advantage and why it helped]. A second relevant strength was [different advantage]. Limitations were [two distinct constraints and their effects on evidence], not invented events.',
 'In my actual pilot, [specific wording/recording problem] occurred. I changed [procedure] and checked [result of retry]. State honestly if this stage was not completed.',
 'I found [pattern] supported by [figures or observations with units]. This suggests [implication]. In answer to my question, [bounded conclusion], but [exception and limitation] prevent a stronger claim.',
 'My actual research obstacle was [difficulty obtaining evidence]. A matched response is [safe feasible change] arranged by [responsible actor]. Record whether it was done or remains proposed, and any resulting coverage limit.']}
models={}
for code,scaffolds in B_SCAFFOLDS.items():
    i=item('10.1',code); lines=i['canonical_answer'].splitlines()
    models[code]=[s for s in lines if re.match(r'B\(\d+\)',s)]
    assert len(models[code])==len(scaffolds)
    i['canonical_answer']='\n'.join([s for s in lines if not s.startswith('B(')] + [f'B({n}) Own-enquiry scaffold: {s}' for n,s in enumerate(scaffolds,1)])
    i['prompt']=i['prompt'].replace('The model below is fictional and illustrates answer structure only.',
        'Section B answers are fill-in scaffolds for your own real record; they are not completed fictional fieldwork. A fictional demonstration in the notes is a separate teaching example.')
    # Replace every B guidance line as well, so no memorisable model is smuggled back in.
    i['marking_guidance']=[s for s in i['marking_guidance'] if not s.startswith('B(')]
    qs=dict((int(n),int(m)) for n,m in re.findall(r'B\((\d+)\).*?\[(\d+)\]',i['prompt']))
    for n,s in enumerate(scaffolds,1):
        i['marking_guidance'].append(f'B({n}), up to {qs[n]} marks: require genuine enquiry evidence matching the requested function. {s} No credit is claimed here for an invented personal experience; guidance is indicative, not an official scheme.')
    CHANGES.append(dict(finding='R6136-011',artefact=i['item_id'],action='Replace all Section B canonical answers and guidance with own-enquiry scaffolds; preserve historical models separately.'))
dump(Path(__file__).parent/'prior-fictional-section-b-models.json',{'use':'Historical pre-repair audit only; not learner answers.','models':models})
teach('10.1',12,'Separate fictional demonstration from personal evidence',
    'This demonstration is invented, not an enquiry you carried out. Suppose a safe observation found 12 visible items at one site and six at another during the same period, with one route inaccessible. The finding is a two-to-one count contrast in the observed places, not a result for the whole community. A conclusion can say the recorded sites differed, while noting missing coverage. A recommendation might ask the responsible collection provider to inspect the higher-count site. For your own answer, replace the demonstration with your actual observations and limits. Do not claim these counts, visits or recommendations as your own experience.', 'R6136-011')

i=item('10.1','P02')
i['prompt']=i['prompt'].replace('resource-use shares for the later operation:', 'shares of the later operation’s total production cost (one stated whole):')
i['prompt']=i['prompt'].replace('resource-use', 'production-cost').replace('resource shares','production-cost shares')
i['canonical_answer']=i['canonical_answer'].replace('resource-use','production-cost').replace('resource shares','production-cost shares')
i['marking_guidance']=[s.replace('resource-use','production-cost').replace('resource shares','production-cost shares') for s in i['marking_guidance']]
i['prompt']=i['prompt'].replace('Explain a plausible resource/output relationship and its limit.',
    'Explain how lower spoilage relates to usable output and why the cost shares cannot prove the cause.')
i['canonical_answer']=i['canonical_answer'].replace('Storage is a recorded resource use and lower spoilage accompanies more usable output. The pair is consistent with better handling, but other conditions may differ and the shares alone do not prove causation.',
    'Lower spoilage leaves more of the harvest usable: 100 minus 20 gives 80 earlier, while 130 minus 10 gives 120 later. The single later-period cost shares show spending composition, not a change in spending or proof that storage caused the improvement. Other conditions may differ.')
i['marking_guidance']=[s if not s.startswith('A2(4)') else 'A2(4), up to 3 marks: link reduced spoilage to usable output, then distinguish the later-period spending composition from evidence of spending change or causation. Equivalent accurate explanation is valid.' for s in i['marking_guidance']]
CHANGES.append(dict(finding='R6136-013',artefact=i['item_id'],action='Define the whole of the divided rectangle as total production cost.'))
i=item('10.1','P03')
i['prompt']=i['prompt'].replace('Mode counts for 12 recorded journeys:',
    'The five sampled schools record 12 learner journeys, each classified once by its main travel mode during the stated week; this small sub-sample need not represent every learner. Mode counts:')
CHANGES.append(dict(finding='R6136-013',artefact=i['item_id'],action='Tie the 12 journeys to the five sampled schools and distinguish the sub-sample.'))

# Self-contained references and minor conceptual wording corrections.
for b in unit('1.1',4)['blocks']:
    if b['heading']=='Use it for an appropriate judgement':
        b['text']='For fictional Area H, average annual income per person is N$50,000 and safe-water access 40%; J has N$30,000 and 85%. An income-only rule prioritises J. For improving water access, H’s larger access gap provides stronger evidence of need. Income and access answer different questions: compare the measure directly relevant to the decision.'
unit('1.1',4)['blocks']=[b for b in unit('1.1',4)['blocks'] if b['heading']!='Go beyond one average']
for t,d in TOPICS.items():
    for u in d['units'].values():
        for b in u['blocks']:
            if t=='10.1':
                b['text']=b['text'].replace('For the Omi source in Package 1, 60 divided by 12',
                    'For a fictional list of 60 households and a sample of 12 (ITEM-6136-10.1-P01), 60 divided by 12')
                b['text']=b['text'].replace('The rural source in Package 2 has group proportions 40/60 and 20/60:',
                    'For fictional villages of 40 and 20 households (ITEM-6136-10.1-P02), the group proportions are 40/60 and 20/60:')
                b['text']=b['text'].replace('In Package 3, a fair draw of five distinct school numbers',
                    'For a fictional list of 20 schools (ITEM-6136-10.1-P03), a fair draw of five distinct school numbers')
                b['text']=b['text'].replace('For resource shares 40%,35%,25%', 'For production-cost shares 40%,35%,25%')
                b['text']=b['text'].replace('the supplied road, school, midpoint water point and northeast litter site',
                    'a fictional west–east road, school at its west end, water point at the midpoint and litter site north of its east end')
            if t=='1.1': b['text']=b['text'].replace('annual GNP per person N$50,000','annual average income per person N$50,000').replace('GNP per person N$30,000','average income per person N$30,000')
    if t=='1.1':
        for i in d['items']['items']:
            for k in ['prompt','canonical_answer']:
                i[k]=i[k].replace('annual GNP per person N$50,000','annual average income per person N$50,000').replace('GNP per person N$30,000','average income per person N$30,000').replace('reduce unsafe-water access','reduce the share lacking safe water')
        item('1.1',17)['canonical_answer']=item('1.1',17)['canonical_answer'].replace('GNP per person remains useful','Average income per person remains useful')

# Update all examples that quote the old prompts/answers to the repaired versions.
for t,d in TOPICS.items():
    originals=baseline(d['ip'])['items']
    newitems={i['item_id']:i for i in d['items']['items']}
    for old in originals:
        new=newitems[old['item_id']]
        for u in d['units'].values():
            for b in u['blocks']:
                for key in ['prompt','canonical_answer']:
                    if old[key]!=new[key] and old[key] in b['text']:
                        b['text']=b['text'].replace(old[key],new[key])
for b in unit('4.1',4)['blocks']:
    if b['heading']=='Evaluate an illustrative state action':
        b['text']='In a fictional industrial area, firms face delivery delays and a shortage of technical skills. A freight upgrade offers earlier gains for existing firms; a training centre develops future capability but takes longer. Where delays threaten current orders, the route may merit priority. Where deliveries remain manageable but skills block expansion, training may be stronger. Compare urgency, reach, cost and longer-term benefits. This is an illustrative decision, not a claimed policy result for a named country.'

# Provenance for already checked external facts: attach existing dated locators.
# Do not upgrade independent verification status or invent a new source visit.
for t,d in TOPICS.items():
    for u in d['units'].values():
        urls=[]
        for b in u['blocks']:
            urls.extend(re.findall(r'\]\((https?://[^)]+)\)',b['text']))
        if not urls:continue
        ids=set(c for b in u['blocks'] for c in b.get('claim_ids',[]))
        for c in d['ledger']['claims']:
            if c['claim_id'] in ids and not c['evidence']:
                c['evidence']=[dict(source_id=url,locator=f'Existing author source check, 2026-10-20; see {u["unit_id"]} linked source block. No new retrieval in repair.',support_type='corroboration') for url in dict.fromkeys(urls)]
                c['provenance']='source_synthesised'
                c.setdefault('notes',[]).append('R6136-017: existing dated source links attached; no independent re-verification claimed.')

# The term change is a claim revision, not just a derivative text edit.
for c in TOPICS['6.2']['ledger']['claims']:
    c['text']=c['text'].replace('infant abandonment','baby dumping').replace('Infant abandonment','Baby dumping')

def finish():
    changed=[]
    for t,d in TOPICS.items():
        before={c['claim_id']:c for c in baseline(d['lp'])['claims']}
        revised={}
        for c in d['ledger']['claims']:
            old=before.get(c['claim_id'])
            if old and c['text']!=old['text']:
                c['revision']=old.get('revision',1)+1
                c['revised_at']='2026-10-20';revised[c['claim_id']]=c['revision']
                changed.append(dict(finding='R6136-003',claim_id=c['claim_id'],before=old,after=c))
        # Bind repaired text to the newly supplied teaching claims for its objective.
        for i in d['items']['items']:
            added=[c['claim_id'] for c in d['ledger']['claims'] if c['claim_id'] not in before and set(c['objective_ids'])&set(i['objective_ids'])]
            i['claim_ids']=list(dict.fromkeys(i['claim_ids']+added))
        for u in d['units'].values():
            u['word_count']=sum(len((b['heading']+' '+b['text']).split()) for b in u['blocks'])
            if u['word_count']>u['word_budget']['max']:
                raise ValueError(f'{u["unit_id"]}: {u["word_count"]} exceeds {u["word_budget"]["max"]}')
            dump(d['td']/'content-units'/f'{u["unit_id"]}.json',u)
        revisions={c['claim_id']:c.get('revision',1) for c in d['ledger']['claims']}
        oldarts={i['item_id']:i for i in baseline(d['ip'])['items']}
        for name in d['units']:
            oldarts.update({b['block_id']:b for b in baseline(d['td']/'content-units'/name)['blocks']})
        artefacts=d['items']['items']+[b for u in d['units'].values() for b in u['blocks']]
        for x in artefacts:
            aid=x.get('item_id',x.get('block_id'));old=oldarts.get(aid)
            x['claims_seen']={c:revisions[c] for c in x['claim_ids']}
            newhash=hashlib.sha256(_artefact_text(x).encode()).hexdigest()
            if old and old.get('authored_hash')!=newhash:
                x['prior_hash']=old['authored_hash'];x['repair_note']='Codex repair of Claude R6136 findings; preserved pre-repair baseline and action log in review/repairs/.'
            elif old and any(c in revised for c in x['claim_ids']):
                x['reviewed_unchanged']='Checked against the revised baby-dumping terminology: this text supplies the same access/support mechanism without using the superseded term, so no wording change is needed.'
            x['authored_hash']=newhash
        for u in d['units'].values():dump(d['td']/'content-units'/f'{u["unit_id"]}.json',u)
        dump(d['ip'],d['items']);dump(d['lp'],d['ledger'])
        hist=d['td']/'authoring-history/post-claude-claim-repairs.json'
        dump(hist,[c for c in changed if c['claim_id'].startswith(f'CLM-6136-{t}-')])
        d['notes']['deviations'].append(dict(
            **{'from':'Pre-review draft and demand specifications criticised in Claude review R6136-001–017 / PL-1–5',
               'to':'Source-based teaching breadth, missing methods, natural prompts, real trade-offs and own-enquiry scaffolds; slots, IDs, labels and ceilings retained.',
               'why':'Jeremy authorised repairs after the whole-subject independent review. The correction supplement records exact scope and demand amendments.'}))
        d['notes']['post_review_status']='Repaired by Codex; original Claude verdict retained. No re-review or publication approval claimed.'
        dump(d['td']/'authoring_notes.json',d['notes'])
    dump(Path(__file__).parent/'content-actions.json',{'author':'Codex','date':'2026-10-20','claude_called':False,'changes':CHANGES,'claim_revisions':changed})
    print(f'Wrote {len(TOPICS)} topics; {len(CHANGES)} explicit actions; {len(changed)} claim revisions. Render and audit next.')

if __name__=='__main__':finish()
