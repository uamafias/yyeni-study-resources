"""Explicit post-resource-review plan amendments; IDs/counts/labels stay fixed."""
from pathlib import Path
import json
import sys

WS=Path(__file__).resolve().parents[1]
NATURAL_TITLES={
'developed/developing':'Describe development differences using specified indicators.',
'LEDC and MEDC':'Describe what the LEDC and MEDC categories indicate and conceal.',
'industrialised/non-industrialised':'Describe differences in industrial structure.',
'capitalism/communism':'Describe the contrasting ownership principles of capitalism and communism.',
'newly industrialised countries':'Describe industrial expansion and structural change in NIC examples.',
'short-term planning':'Describe the implementation role of shorter development plans.',
'long-term planning':'Describe the direction set by long-term development planning.',
'oil':'Describe oil’s use and limitations as an energy resource.',
'coal':'Describe coal’s use and limitations as an energy resource.',
'nuclear energy':'Describe development considerations in nuclear electricity generation.',
'natural gas':'Describe natural gas as a production energy source.',
'solar energy':'Describe conditions affecting useful solar electricity.',
'biogas':'Describe how biogas is produced and used.',
'wood':'Describe conditions for sustainable use of wood fuel.',
'Hydro Electric Power':'Describe the water and infrastructure requirements of hydroelectricity.',
'micro-electronics':'Describe productive uses of micro-electronic sensors and controls.',
'biotechnology':'Describe biological applications to productive tasks.',
'communications and information systems':'Describe how information systems coordinate production and exchange.',
'complex machinery and advanced technology':'Describe the capabilities and support needs of advanced machinery.',
'wide range of raw material':'Describe how varied inputs contribute to industrial products.',
'complex division of labour':'Describe specialisation in industrial production.',
'coordination of specialised tasks':'Describe how specialised production stages are coordinated.',
'value-added processes':'Describe how processing can add value and local productive links.',
'foreign investors and local joint ventures':'Describe shared productive participation in a joint venture.',
'modern production processes':'Describe possible improvements from modern production methods.',
'research and exploration':'Describe how research can inform productive opportunities and constraints.',
'urbanisation in industrialised countries':'Describe historical urbanisation linked to industrial expansion.',
'urbanisation in developing countries':'Describe urban growth where service and employment expansion may lag.',
'hunter-gatherers':'Describe obtaining food through wild plants and animal resources.',
'nomadic pastoralists':'Describe livestock-based livelihoods and movement for pasture and water.',
'agriculturalists':'Describe crop cultivation and its seasonal tasks.',
'land use and ownership':'Distinguish productive land use from rights and control over land.',
'division of labour':'Describe the allocation of specialised rural tasks.',
'tools':'Describe how tools assist rural productive tasks.',
'seasonal agriculture':'Describe how seasonal conditions organise agricultural work.',
'social and cultural activities':'Describe cooperation and shared knowledge in rural production.',
'dependence on the local environment':'Describe effects of water, soil and vegetation on livelihoods.',
'pre-colonial farming changes':'Describe innovation and exchange in farming before colonial rule.',
'impact of colonialism':'Describe colonial changes to land, labour and rural opportunities.',
'peasant farming and cash cropping':'Distinguish household-scale farming from production mainly for sale.',
'tools and technology':'Describe equipment used in commercial farming and its support needs.',
'monoculture and large-scale projects':'Distinguish single-crop production from the scale of an operation.',
'plantations':'Describe estate production of commercial crops.',
'crop rotation':'Describe planned crop sequences and their soil or pest effects.',
'tourism impacts on people':'Describe social benefits and costs of tourism for residents.',
'tourism impacts on the economy':'Describe employment, supplier and income links from tourism.',
'tourism impacts on the environment':'Describe conservation benefits and resource pressures from tourism.',
"women's labour":'Describe women’s paid and unpaid productive labour.',
'food production and farming':'Describe women’s contributions across food-production stages.',
'family welfare':'Describe how household and caring work supports family welfare.',
'equal access to jobs':'Describe fair selection and practical access to employment.',
'new policies':'Describe implementation and monitoring of equality policies.',
'women-oriented schemes':'Describe targeted support for documented opportunity gaps.',
'female-headed households':'Describe evidence needed to assess female-headed households’ circumstances.',
'responses to gender-based violence':'Describe complementary prevention, protection and survivor support.',
'responses to baby dumping':'Describe confidential support and child-protection responses to baby dumping.',
'economic uses of population data':'Describe population evidence used in labour and demand planning.',
'social uses of population data':'Describe population evidence used in school and care planning.',
'population pyramids in developed countries':'Describe older age structures and their planning implications.',
'population pyramids in developing countries':'Describe youthful age structures and their planning implications.',
'HIV and AIDS effects on economic development':'Describe household income and care-time effects of HIV-related illness.',
'health-system responses to HIV and AIDS':'Describe linked professional services and inclusive HIV support.',
'ways countries trade and price fluctuations':'Describe trade-price changes and their effects on earnings and planning.',
'balance-of-payments problems':'Describe external-payment pressures on imports and repayment.',
'search for a new economic order':'Describe aims for fairer trading and financing opportunities.',
'trade involving developing countries':'Describe risks of a narrow primary-export base.',
'trade involving NICs':'Describe trade changes accompanying industrial expansion.',
'trade involving developed countries':'Describe manufactured, service and input trade in developed economies.',
'globalisation opportunities':'Describe market and knowledge opportunities from international connections.',
'globalisation constraints':'Describe competitive pressures and exposure to external shocks.',
'infrastructure':'Describe maintained networks that connect firms to international markets.',
'human-resource development':'Describe skills that support quality and productive participation.',
'international exposure':'Describe how producers learn about foreign buyers and requirements.',
'attracting foreign investment':'Describe productive finance and the conditions for retained local gains.',
'direct foreign investment and multinational companies':'Describe productive control, facilities and local links in foreign direct investment.',
'foreign loans and credits':'Describe repayment obligations and productive uses of foreign borrowing.',
'World Bank':'Describe development finance and technical support associated with the World Bank.',
'IMF':'Describe monetary cooperation, stability and balance-of-payments support associated with the IMF.',
'UNDP':'Describe UNDP’s development and institutional-capacity work.',
'UNICEF':'Describe UNICEF’s child-focused support across development needs.',
'FAO':'Describe FAO’s work on food security and agricultural knowledge.',
'UNESCO':'Describe UNESCO’s cooperation in education, science, culture and information.'}

EVAL_REQUIREMENT=('Supply alternatives with genuine merits and costs, a stated development aim and enough original evidence to weigh them. '
 'Require developed comparison and a justified conditional judgement. Do not make the choice automatic by omitting a necessary input from one option. '
 'Multi-point knowledge of advantages, limitations and reasons remains essential in the notes; it complements evaluation rather than being prohibited by it.')

def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def main():
    cur=WS/'curriculum';p=cur/'objective_registry.json';reg=json.loads(p.read_text());changes={}
    for o in reg['objectives']:
        title=NATURAL_TITLES.get(o.get('syllabus_text'))
        if o['objective_id']=='OBJ-6136-3.1.04-01':title='Define division of labour in production.'
        if o['objective_id']=='OBJ-6136-8.1.04-03':title='Explain the contribution of public infrastructure to development.'
        if title and o.get('parent_id') and not o['objective_id'].endswith('-00'):
            changes[o['objective_id']]=title;o['learner_objective']=title
    dump(p,reg)
    sys.path.insert(0,str(WS.parents[1]/'standard/v0.2.0-draft/build'))
    from make_work_order import as_markdown
    for td in (WS/'topics').iterdir():
        p=td/'work_order.json'
        if not p.exists():continue
        wo=json.loads(p.read_text())
        for s in wo['item_slots']:
            if s['objective_id'] in changes:s['objective_title']=changes[s['objective_id']]
        for u in wo['content_units']:
            for o in u['objectives']:
                if o['objective_id'] in changes:o['title']=changes[o['objective_id']]
        dump(p,wo);(td/'work_order.md').write_text(as_markdown(wo))
    p=cur/'slot-demand-specs.json';spec=json.loads(p.read_text())
    for s in spec['slots']:
        if s['objective_id'] in changes:s['target']=changes[s['objective_id']]
        if s['subtype']=='EVAL':s['task_requirement']=EVAL_REQUIREMENT
        if s['subtype']=='CALC':s['task_requirement']+=' Notes must explicitly teach the formula, units, denominator and a worked example before this practice.'
    dump(p,spec)
    supplement={
      'authority':'Codex planning repair, explicitly authorised by Jeremy after Claude resource review; not a new Claude approval.',
      'preserved':['356 teaching targets','543 slots','item IDs, subtypes, AOs, Bloom labels, command metadata and tariffs','unit ceilings','official syllabus wording'],
      'PL-1':{'decision':'Multi-point breadth is required where the objective and reports demand it. Conditioned mechanisms and lists of distinct developed points serve different demands.',
              'teaching_sets':['GNP limitations','SDGs and responsible production','privatisation','state industrial roles','rural schemes and cooperatives','GBV types/factors/effects/responses','birth and death-rate explanations','traditional/modern education','regional achievements/challenges','research methods']},
      'PL-2':{'decision':'Replace 82 generic member-objective titles with explicit subject-specific teaching targets; independently authored natural questions replace the 72 flagged item templates.','title_updates':changes},
      'PL-3':{'decision':'Illustrative named material with recorded exposure remains required teaching: Vision 2030 definition, 2016 HPP, NDP5, and syllabus NIC contexts. It is not folded out of the learner materials.'},
      'PL-4':{'decision':'Retain the observed compound command metadata on 7.3-006 as evaluative extension of the comparison objective, not a claim that the syllabus itself commands evaluation. Describe both real alternatives, then weigh them and judge. The learner wording says give a reasoned judgement because C14 incorrectly rejects Evaluate within the compound.','limitation':'The standard command blacklist remains an owner issue; no standard edit or silent metadata change.'},
      'PL-5':{'decision':'CALC demand includes prerequisite teaching, not only card slots.','method_map':{'7.1-011':'7.1 unit 03: natural increase and per-thousand conversion','7.2-003 / 7.2-014':'7.2 unit 01: worked percentage change and percentage-point contrast'}},
      'research':{'decision':'Section B requires actual learner records and fill-in scaffolds. Fictional demonstrations remain separate from personal answers. Section A is 35 marks and B 15; P02 has A1 20/A2 15, the other three A1 25/A2 10. No universal A1/A2 split is inferred.'}}
    dump(cur/'post-resource-review-amendments.json',supplement)
    add='\n\n## Post-resource-review repair requirements (2026-10-20)\n\nJeremy authorised correcting the completed draft after Claude’s FIX CONTENT BEFORE PUBLICATION verdict. The amendment in `curriculum/post-resource-review-amendments.json` resolves PL-1–PL-5: multi-point teaching breadth, natural member targets, named examined examples, genuine comparison/evaluation and prerequisite calculation methods. Stable slots, labels and unit ceilings remain unchanged. Section B uses own-enquiry scaffolds; no fictional model may stand in for completed personal fieldwork. The resource repair manuscript is `review/repairs/repair_resources.py`, replayed after the original author manuscripts. No new Claude review is authorised.\n'
    for name in ['PLAN-6136-nssco-development-studies.md','HANDOVER-6136-nssco-development-studies.md']:
        p=WS/name;s=p.read_text();anchor='\n\n## Post-resource-review repair requirements'
        if anchor in s:s=s[:s.index(anchor)]
        p.write_text(s+add)
    print(f'Updated {len(changes)} member targets, mirrored work orders and explicit PL-1–5 amendment. Slots and labels unchanged.')

if __name__=='__main__':main()
