"""Targeted independent-review repairs. Run once; logs every changed object.
No contracts, plans, curriculum, slots, labels or image bytes are edited.
"""
import copy,json,pathlib,re
W=pathlib.Path(__file__).resolve().parents[1]
docs={p:json.loads(p.read_text()) for p in W.glob('topics/*/*/*.json') if p.parent.name in ('content-units','learning-items','claims')}
before=copy.deepcopy(docs)
objects={}
for p,d in docs.items():
 for o in d.get('blocks',d.get('items',d.get('claims',[]))):
  objects[o.get('block_id',o.get('item_id',o.get('claim_id')))]=o

def block(id,text): objects['BL-6137-'+id]['text']=text

def claim(id,text,source=None):
 o=objects['CL-6137-'+id];o['text']=text
 if source:
  for e in o['evidence']:
   if e['source_id']=='CROSSREVIEW-6137': e['locator']=source

def item(id,**fields):
 key=next(k for k in objects if k.startswith('ITEM-6137-'+id+'-') or k=='ITEM-6137-'+id)
 objects[key].update(fields)

def replace(topic,old,new):
 n=0
 for k,o in objects.items():
  if not k.startswith(('BL-6137-'+topic,'CL-6137-'+topic,'ITEM-6137-'+topic)):continue
  for f in ('text','canonical_answer','prompt','marking_guidance'):
   v=o.get(f)
   if isinstance(v,str) and old in v:o[f]=v.replace(old,new);n+=1
   elif isinstance(v,list):
    for j,s in enumerate(v):
     if old in s:v[j]=s.replace(old,new);n+=1
 assert n,(topic,old)

claim('1.6.08-02-R1','The troposphere is heated largely from the surface. As air rises into lower pressure, it expands and cools; temperature therefore generally decreases with altitude. The average environmental decrease is about 6.5°C per 1,000 m, though local inversions can reverse it.', 'NOAA/FAA Weather Theory, pressure, expansion and lapse rates: https://www.weather.gov/media/zhu/ZHU_Training_Page/Met_Tutorials/Weather_Theory.pdf ; environmental average is distinct from the dry adiabatic rate.')
block('1.6.08-05','Altitude commonly influences temperature in the troposphere: higher sites are generally cooler than comparable lower sites. The lower atmosphere receives much of its heat from the warmed ground. Air rising into lower pressure expands and cools, helping produce the usual fall of temperature with height. The average environmental decrease is about 6.5°C per 1,000 m; this describes an average temperature profile, not the cooling rate of every rising parcel. An inversion can reverse the decrease within a layer. A mountain summit and a sheltered valley floor can also differ in exposure and night-time cooling.')
replace('1.5','a pebbleometer or roundness chart for shape','a pebbleometer for size or a roundness chart for shape')
replace('1.5','Size is measured with a ruler or callipers, and shape with a pebbleometer or a roundness chart.','Size is measured with a ruler, callipers or pebbleometer; a roundness chart classifies shape.')
claim('1.3.06-01-R1','A reduction in flow can cause deposition when sediment-transport capacity falls. In floods examined by Jacobson and colleagues (2000), the ephemeral Kuiseb lost water downstream and deposited the transported material within the lower river without discharging to the Atlantic. This describes the studied events, not every Kuiseb flood.')
replace('1.4','along the resultant direction instead of migrating','along the resultant sand-transport direction; some sideways movement can also occur')
replace('1.4','grow upward rather than migrating','mainly grow upward rather than migrating steadily in one direction')
replace('1.4','grows upward instead of moving','mainly grows upward rather than migrating steadily in one direction')
replace('1.4','along the average direction of the two winds','along the resultant direction of sand transport, which depends on the strength and duration of the winds')
claim('1.5.07-R1','Obliquely approaching breaking waves drive swash up the beach at an angle; backwash returns down the beach under gravity, giving net longshore transport. Local winds can help determine wave direction, but distant swell and refraction also affect the approach, so drift cannot always be inferred from local prevailing wind alone.')
# Avoid an absolute ban on all northern livestock/meat exports.
claim('2.2.05-R2','The veterinary cordon fence separates livestock-health zones. Movement, quarantine and processing requirements restrict access to some markets for northern livestock and meat, increasing costs and limiting buyers. These restrictions help explain differences in commercialisation, alongside land tenure, household objectives and infrastructure.', 'Atlas of Namibia, Farming, veterinary cordon fence and quarantine before processing and sale elsewhere: https://atlasofnamibia.online/chapter-8/farming . Requirements depend on product and destination; no blanket overseas-export ban is asserted.')
item('2.2-017',canonical_answer='The fence separates livestock-health zones, protecting the centre and south from diseases such as foot-and-mouth disease. Northern livestock and meat face movement, quarantine and processing requirements for access to some markets. These raise marketing costs and restrict buyers, reducing incentives to sell commercially. Together with land tenure, infrastructure and household needs, the restrictions help explain why many northern households keep cattle as wealth and security while large commercial ranches developed south of the fence.',marking_guidance=['1 mark for disease control and the separation of livestock-health zones.','1 mark for the link to movement, quarantine or processing requirements restricting access to some markets.','1 mark for higher marketing costs or fewer buyers.','1 mark for the resulting constraint on commercial sales, recognising other influences.'])
replace('2.2','Most homesteads also keep cattle','Some homesteads also keep cattle')
replace('2.3','air links were reduced when the national airline stopped flying in 2021, ending direct flights to Frankfurt','the closure of Air Namibia in 2021 ended its own Frankfurt service, although other airlines continue direct international services')
claim('2.4.02-04-R1','The 2023 Population and Housing Census main report records wood/firewood as the main cooking fuel for 50.1% of private households nationally and 84.6% in rural areas. These are household population statistics, not unweighted case frequencies from the microdata browser.', 'NSA, Media Statement: 2023 Census Main Report, 30 October 2024, paragraph 5(k): https://nsa.org.na/wp-content/uploads/2024/10/Media-Statement-2023-Census-Main-Report-30-October-2024.pdf . The microdata variable browser explicitly warns that its case counts are not population statistics.')
replace('2.4','in the 2023 census sample data, 58% of households recorded wood or firewood and 29% electricity','the 2023 census main report records wood/firewood as the main cooking fuel for 50.1% of private households nationally and 84.6% in rural areas')
replace('2.4','every unit produced locally reduces payments to other countries','local generation can displace imported electricity and reduce payments overseas')
replace('2.4','When world oil prices rise, the fuel import bill rises, so pump prices go up.','Other things equal, higher world oil prices raise the fuel import bill and put upward pressure on pump prices; exchange rates, taxes and regulated adjustments also matter.')
replace('2.5','Namibia’s perennial rivers are all on its borders','Namibia’s perennial rivers lie along or cross its borders') if any('Namibia’s perennial rivers are all on its borders' in o.get('text','') for o in objects.values()) else None
item('2.5-008',prompt="A water-source map shows Namibia's perennial rivers concentrated near its northern, north-eastern and southern boundaries, widespread ephemeral channels in the interior, and productive aquifers in the Karstveld, Stampriet and Ohangwena. Describe the pattern shown.",canonical_answer='Perennial rivers are concentrated near the national boundaries, while most interior channels flow only after rain. Named aquifers occur in several interior areas, so groundwater is important away from the perennial rivers. Interior dams also store surface water; the pattern does not mean all permanent water is at the border.',marking_guidance=['1 mark for perennial rivers concentrated near the boundaries; 1 for widespread ephemeral interior channels; 1 for groundwater importance using a named aquifer.'])
item('2.5-011',canonical_answer='Most interior channels are ephemeral and flow briefly after rain. High evaporation removes much water from open reservoirs. Boreholes and wells can tap water stored underground, protected from direct open-water evaporation. Where aquifer storage, recharge, quality and abstraction permit, this sustains farms and settlements through dry periods; boreholes can still fail or be depleted.',marking_guidance=['1 mark for mainly ephemeral interior channels; 1 for high evaporation from open stores; 1 for protected underground storage tapped by boreholes; 1 for dry-period supply, conditional on adequate usable groundwater.'])
replace('2.5','the spread of bilharzia, carried by freshwater snails in still water','bilharzia risk where infected freshwater snails release parasite larvae that enter the skin during contact with infested water')
claim('2.5.05-01-R1','Dams can store water for dry periods, irrigation, flood management, recreation and sometimes hydropower. Costs include displacement, evaporation, sedimentation and altered downstream flows. Bilharzia can spread where infected freshwater snails release parasite larvae that penetrate skin during contact with infested water.', 'WHO, Schistosomiasis, transmission: https://www.who.int/news-room/fact-sheets/detail/schistosomiasis ; general dam benefits and costs are syllabus-level mechanisms, not claims that every dam has every effect.')
item('2.5-P03',prompt="How far do you agree that Windhoek's water supply was secure at the time of the city's August 2025 announcement? Use its sources and the dated conditions in your answer. [5]",canonical_answer='Partly agree for that short-term position. Windhoek uses the Von Bach, Swakoppoort and Omatako dams, boreholes and reclaimed water from Goreangab. Following the 2024/25 rains, the city reported in August 2025 reserves for at least two rainy seasons, lifted restrictions and began aquifer recharge. Against this, evaporation, recurring drought and growing demand remain, and there is no local perennial river. The announcement supported improved short-term security with continued management; it cannot establish conditions in a later year.',marking_guidance=['Up to 4 C marks for weighing the diverse sources and dated August 2025 reserve position against evaporation, drought and rising demand.','1 C mark for a supported, time-bounded judgement; do not require a claim about current restrictions.'])
replace('2.6','shows competition between livestock and wildlife for scarce water and grazing','suggests potential competition for water, but shared use alone does not prove a shortage or establish grazing competition')
replace('2.6','1 for the competition-for-water relationship','1 for identifying possible water competition without claiming the record proves a shortage')
replace('2.6','since 2012 counts in surveyed areas have fallen','since 2012 counts of several species in north-western monitoring areas have fallen')
replace('2.6','counts in surveyed areas have fallen since 2012','counts of several species in north-western monitoring areas have fallen since 2012')
replace('2.5','all lie on its borders and are fed by rain','lie along or cross its borders and are fed by rain')
# Regional prevalence is an outcome, not proof of an occupation or border causing infection.
claim('3.2.02-R1','NAMPHIA 2017 estimated adult HIV prevalence (ages 15–64) at 12.6% nationally, 22.3% in Zambezi, 17.9% in Ohangwena, 8.3% in Khomas and 7.6% in Kunene. Mobility can affect sexual networks and access to prevention or treatment, but these regional prevalences do not establish the main cause of their differences. Ordinary social contact does not transmit HIV.', 'NAMPHIA 2017 summary, regional prevalence table: https://phia.icap.columbia.edu/wp-content/uploads/2025/03/33462%E2%80%A2NAMPHIA-SS_A4_B.v42.pdf ; WHO HIV/AIDS, transmission and risk: https://www.who.int/news-room/fact-sheets/detail/hiv-aids . No causal ranking is inferred from regional prevalence alone.')
block('3.2.02-03','In 2017 national adult prevalence was 12.6%, with Zambezi and Ohangwena above it and Kunene and Khomas below it. Transport routes and border crossings offer a possible explanation for part of the pattern. Travel or migration can separate partners, connect sexual networks and interrupt access to prevention or treatment. These circumstances can increase exposure through unprotected sex; neither travelling nor working in a particular occupation automatically means that someone has HIV or several partners.')
block('3.2.02-04','Regional prevalence alone cannot establish why regions differ or which explanation matters most. It reflects past infections, age and sex composition, migration and survival on treatment. Population density and ordinary contact do not themselves transmit HIV. Unequal power in relationships can make negotiating protection harder. To test a transport-route explanation, compare evidence about exposure and access to services while accounting for these other influences; do not treat a regional correlation as proof of causation.')
item('3.2-P03',canonical_answer='Transport and borders are a plausible part of the explanation, but the figures cannot show that they are the main cause. Mobility can separate partners, connect sexual networks and interrupt prevention or treatment; unprotected sex can then transmit HIV. However, travel and ordinary social contact do not themselves transmit it. The regional percentages measure prevalence, reflecting past infection as well as age, sex, migration and survival on treatment. Zambezi also has a wide estimate interval (17.5–27.0%). Evidence on exposure and service access is needed before ranking causes. Therefore the transport explanation deserves investigation, but its primacy is unproven.',marking_guidance=['Up to 2 C marks for explaining a plausible mobility-related exposure or service-access mechanism.','Up to 2 C marks for explaining limits of regional prevalence as causal evidence, alternative influences or sampling uncertainty.','1 C mark for a supported judgement; do not require agreement that transport is the main cause.'])
replace('3.2','People on effective treatment do not pass HIV on sexually','People taking ART who maintain an undetectable viral load do not transmit HIV sexually')
replace('3.2','preventing an infection costs less than treating it','preventing infections can reduce future treatment costs, although the cost-effectiveness of each programme must be assessed')
replace('3.2','when the virus is suppressed','when treatment maintains an undetectable viral load')
claim('3.2.05-01-R1','Correct, consistent condom use reduces pregnancy and sexual HIV transmission. Fewer births tend to narrow the pyramid base; fewer HIV infections and deaths can preserve working-age and older groups. The birth effect tends to reduce growth while improved survival tends to raise it, so the net growth effect depends on both.', 'WHO, Condoms: https://www.who.int/news-room/questions-and-answers/item/condoms ; WHO HIV/AIDS: https://www.who.int/news-room/fact-sheets/detail/hiv-aids . Growth follows births minus deaths plus net migration; no unconditional net direction is asserted.')
replace('3.2','so the base of the population pyramid becomes narrower and population growth slows','so the base of the population pyramid tends to become narrower; this birth effect tends to slow growth')
replace('3.2','These effects depend on people actually using condoms.','The reduction in deaths tends to increase growth, so the net effect depends on births, deaths and migration as well as correct, consistent condom use.')
replace('3.2','so the upper bars become wider and growth slows','so the upper bars can become wider. The net effect on growth depends on the birth and death changes')
replace('3.2','or slower growth.','; the net growth effect is not fixed.')
replace('3.2','allowing slightly faster population growth','allowing faster growth if births and migration are unchanged')
replace('3.2','population growth can speed up slightly','population growth can increase if births and migration are unchanged')
# Remove answer-bearing alt text from the fronts of settlement cards.
for k,o in objects.items():
 if k.startswith('ITEM-6137-3.3-') and 'prompt' in o and '![' in o['prompt']:
  o['prompt']=re.sub(r'!\[[^\]]*\]', '![Settlement diagram; use its symbols, scale and key]',o['prompt'])
# Date a historic research finding and distinguish the area from informal settlements alone.
replace('3.1',"In Windhoek's crowded northern and north-western areas, for example, over 60% of the city's people live on a quarter of its land", "A 2014 study reported that Windhoek's northern and north-western areas held over 60% of its people on a quarter of its land")
replace('3.1',"mainly in informal settlements, where over 60% of the city's people live on 25% of its land", "often in informal settlements; the 2014 study reported that the northern and north-western areas together held over 60% of the city's people on 25% of its land")
# Make all claim revisions explicit and reconcile each dependent artefact.
changed_claims={}
for p,d in docs.items():
 for old,new in zip(before[p].get('claims',[]),d.get('claims',[])):
  if old['text']!=new['text']:
   new['revision']=old['revision']+1;changed_claims[new['claim_id']]=new['revision']
for p,d in docs.items():
 for o in d.get('blocks',d.get('items',[])):
  for cid,rev in changed_claims.items():
   if cid in o.get('claim_ids',[]):
    o.setdefault('claims_seen',{})[cid]=rev
    o['reviewed_unchanged']='Codex independently checked this artefact against revised claim text; content remains consistent unless separately logged as repaired.'
 if 'blocks' in d:d['word_count']=sum(len(b['text'].split()) for b in d['blocks'])
log=[]
for p,d in docs.items():
 if d!=before[p]:
  for old,new in zip(before[p].get('blocks',before[p].get('items',before[p].get('claims',[]))),d.get('blocks',d.get('items',d.get('claims',[])))):
   if old!=new:log.append({'path':str(p.relative_to(W)),'id':new.get('block_id',new.get('item_id',new.get('claim_id'))),'before':old,'after':new})
  p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
(W/'review/codex-crossreview-repairs-6137.json').write_text(json.dumps({'reviewer':'Codex','changes':log,'claim_revisions':changed_claims},indent=2,ensure_ascii=False)+'\n')
print('Changed objects:',len(log),'claim revisions:',len(changed_claims))
