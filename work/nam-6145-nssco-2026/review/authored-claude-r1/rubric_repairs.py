"""Specific credit points for the items identified in review finding 005."""
R={}
def add(topic,rows):
 for n,points in rows.items():R[(topic,n)]=points
add('4.2',{
1:['Orders for repairs rise','Employers demand more qualified repair labour','Training delays restrict suitable supply','Competition to recruit or retain scarce workers can raise earnings'],
2:['160 hours earn N$4,000 while 80 earn N$2,000','Different hours explain earnings despite the same N$25 hourly rate'],
4:['The figures are group averages','Individuals can fall above/below their averages, allowing the distributions to overlap'],
5:['Paid hours differ, 30 versus 40','Both hourly rates are N$30','Weekly pay is N$900 versus N$1,200','The N$300 gap follows from ten hours, not a different hourly reward'],
6:['Qualifications, work and hours match in the supplied comparison','The stated sex-based rate difference is discriminatory pay rather than an hours explanation'],
7:['Repair demand is strong','Few suitable trained repair workers are available','Recruiting replacements is difficult, encouraging competing offers','Plentiful packing applicants create less scarcity pressure, supporting the relative pay gap'],
8:['The qualification certifies a skill employers no longer demand','Weak demand can keep pay low despite past training effort'],
9:['Technicians are scarce','Recruitment pressure encourages the clinic to compete on pay','Clinic funding permits N$12,000 while the public budget fixes N$10,000','The N$2,000 gap is conditional on these facts, not ownership alone'],
10:['The sectors may contain different occupational mixes','Unmatched jobs/hours prevent isolating pay for comparable work'],
11:['Farm work provides only six paid months','Farm annual earnings are N$24,000','Manufacturing annual earnings are N$36,000','Fewer paid months explain lower annual earnings despite higher farm monthly pay'],
12:['Required irrigation skills have limited suitable supply','Recruitment difficulty can support higher technician pay than for readily supplied general work'],
13:['The machine increases usable output from four to six panels per operator-hour','Orders support the extra output and productive labour demand','Scarce operators cannot readily be replaced','Competitive retention offers can raise pay, subject to bargaining and funding'],
14:['New specialists can earn more than the existing average','A larger specialist share raises the group average without raising existing individuals’ rates'],
15:['Specialist repair demand is strong','Few applicants possess the required skill','Limited substitutes create recruitment pressure','Specialist earnings can exceed reception pay where reception applicants are plentiful'],
16:['Suitable labour supply can expand quickly','Extra employment can meet demand without a large wage increase'],
17:['Technical productivity and product demand rise','Employers have stronger reasons to recruit technical workers','Restricted technical skill supply strengthens pay competition','Assistants lack these changes, so the technical pay gap can widen'],
18:['Pay and the consumption-bundle price both rise 10%','N$2,200 buys the previous bundle, leaving purchasing power unchanged'],
20:['The stated retention minimum gives transfer earnings N$5,000','Economic rent is N$6,000 minus N$5,000, or N$1,000']})
add('4.3',{
2:['Essential needs absorb much of the smaller income','Larger income can exceed the increase in essential costs','More remains after necessities at higher income','The essential income share can fall even if its cash amount rises'],
3:['B spends more cash, N$4,500 versus N$2,400','B spends a lower share, 50% versus 80%, so amount and share differ'],
4:['Income rises faster than current commitments','The remainder after consumption increases','Part of it can be withheld from present consumption','Saving can increase if chosen; greater capacity does not force saving'],
5:['Essentials absorb almost all income','Little capacity remains to save despite a strong precautionary motive'],
6:['An emergency cost exceeds current funds','A household therefore wants credit','Low remaining income makes repayment difficult and may restrict approval','Strong credit need can coexist with little actual borrowing'],
7:['N$400 repayment exceeds the N$150 remainder by N$250','The loan is unaffordable on the unchanged budget without an adjustment'],
8:['Saving delays the purchase while funds accumulate','This reduces present consumption capacity','Borrowing brings the purchase forward','Repayments and charges reduce later available resources'],
9:['The spending motive is to maintain shelter through the roof repair','The borrowing motive is to bridge the current funding gap before future income'],
10:['The failed appliance removes daily cooking service','A replacement restores meal preparation','Restoring that necessary service raises purchase priority','The fixed budget may require less discretionary spending'],
11:['Transport makes the required journey to work feasible','The spending meets necessary access rather than an assumed leisure want'],
12:['An uncertain repair risk creates a need for a reserve','Income can be set aside if current needs permit','Accumulation creates accessible funds for the repair','The reserve can reduce later reliance on borrowing'],
13:['N$200 over twelve months accumulates N$2,400','Postponed consumption finances the planned purchase without debt under the stated assumptions'],
14:['The loan supplies N$1,000 for an immediate purchase','Principal plus N$100 interest totals N$1,100','Ten equal repayments are N$110 each','Those commitments leave less future income for other uses'],
15:['Higher interest raises total repayment cost','Waiting or a cheaper purchase becomes relatively more attractive, so optional borrowing may fall'],
16:['Essential prices add N$150 without more quantity','Income and other spending remain fixed','The increase absorbs the previous N$150 remainder','New saving falls to zero without an increase in real consumption'],
17:['Essential commitments leave one household no discretionary remainder','The surplus household can redirect funds towards saving in response to a higher return']})
add('5.4',{
15:['Confirmed sustained orders support higher saleable output','More output permits use of larger capacity','Utilisation makes technical or other scale economies feasible','A narrow or temporary market could leave capacity idle, limiting viable size'],
16:['Few orders limit saleable output','A larger machine may be underused, making expansion unattractive'],
17:['Expansion requires N$200,000 but only N$60,000 is available','The funding gap is N$140,000','Without funding the required equipment/capacity cannot be secured','Additional affordable funds or a smaller stage are needed despite product demand'],
18:['The N$140,000 gap prevents the proposed acquisition','Expected customers do not themselves provide finance'],
19:['More outlets increase coordination demands','Missing shared records cause duplicated orders and errors','Rework and delay add cost per unit','Organisational problems constrain manageable scale until addressed'],
20:['Clear responsibilities and shared records align outlet decisions','Less duplication and delay permit more effective coordination of larger operations']})
add('6.1',{
1:['Making desks is the goods-production role','Hiring carpenters is the employer role'],
2:['Desks are a tangible government-workshop output','Storage cabinets are a second tangible output'],
3:['Clinic consultations are a service','Library lending is a distinct service'],
4:['Directly hired librarians are government employees','Directly hired carpenters are government employees; private courier drivers are excluded']})
add('6.2',{
4:['The programme demands previously unemployed suitable labour','Workers receive earnings','Spare equipment and labour create useful maintenance services','Employment/output can rise under the stated available-resource and funding conditions'],
5:['The recruits already held jobs elsewhere','Hiring may shift employment instead of creating an equal net gain'],
6:['Demand restraint slows growth in orders','Purchasing pressure on limited output eases','Less excess competition for available capacity weakens price pressure','Inflation can slow, although output/employment may weaken'],
7:['Inflation stays positive despite falling from 10% to 5%','The price level rises more slowly rather than falling'],
8:['Transport investment removes a documented production bottleneck','Inputs can reach producers more reliably','Products can reach buyers, allowing more real output','Living-standard gains remain conditional on per-capita outcomes, distribution and environment'],
9:['Population grows 6%, faster than real output at 4%','Output per person falls; distribution/environment also limit a welfare inference'],
10:['Tax removes N$100','The transfer adds N$300','Net disposable cash resources rise N$200','The net gain can support essential consumption with other conditions unchanged'],
11:['Benefits financed by the progressive tax may favour other groups','Net redistribution requires both taxes paid and benefits received'],
12:['Extra purchases contain imports','Import payments therefore rise','Higher external outflows require financing','Limited financing can weaken external sustainability, conditional on import content'],
13:['The full external accounts include more than goods trade','A zero goods balance alone cannot establish sustainable overall transactions and financing'],
15:['Public orders increase demand for domestic output','Idle capacity can be brought into use','Suitable unemployed workers can be recruited','Output/employment can rise if the stated resources and funding are available'],
16:['Tax-cut recipients may save, repay debt or import','Only the part spent on domestic output directly raises domestic demand in this channel'],
17:['Lending rates rise and are passed through','Repayment/financing cost increases','Some purchases or projects become less attractive and are postponed','Lower demand can restrain demand-related inflation; Namibia choices remain within the rand peg'],
18:['Lower financing cost does not itself create customers','Weak expected sales can still make the project unattractive despite cheaper credit'],
20:['N$200/N$2,000 and N$600/N$6,000 both give 10%','The same percentage means proportional taxation despite different cash payments'],
22:['Personal income is one direct-tax base','Business profit is the other stated direct-tax base'],
24:['Sale of the soap bar is the taxed transaction','A tax on that product transaction is indirect'],
26:['The average rates are 5% and 10%','A rising average rate with income is progressive'],
28:['The 10% liability on N$2,000 is N$200','The liability on N$6,000 is N$600, the same 10%'],
30:['The N$100 levy is 10% of N$1,000 and 2% of N$5,000','A falling income-share burden is regressive'],
32:['The lending rate rises from 8% to 10%','Annual interest rises N$8,000 to N$10,000','The extra N$2,000 reduces the expected project gain','A borderline project may be delayed, conditional on expected returns and credit terms within the rand-peg framework'],
33:['Customers’ financed purchases face higher repayment costs','Postponed customer purchases reduce orders even for an unborrowed firm']})
add('6.3',{
5:['Inspection can detect hidden food hazards','Detection and correction reduce consumer exposure','Accurate labels help informed storage/use','Limited staff/testing can miss hazards and compliance costs resources','Clear risk-focused checks need effective follow-up','Support the combined approach conditionally','Tie the judgement to hidden hazards and limited enforcement rather than a blanket safety promise'],
6:['Trusted complaints reveal the missing machine guard','Inspection and fitting the guard reduce injury exposure','Safer work protects employees’ interests','Equipment and enforcement impose resource costs','Effective correction and trusted reporting are necessary','Support prompt hazard correction','Explain that a written policy alone does not remove the guard hazard'],
7:['Education challenges HIV-status stereotypes','Confidential complaints support fair employment review','This protects against decisions based on status rather than actual work circumstances','Low awareness blocks access to the process','Unnecessary disclosure fears undermine trust','Support an accessible confidential policy with effective follow-up','Tie the judgement to awareness, privacy and non-discrimination, not status-based ability assumptions']})
add('7.2',{
1:['Agricultural jobs rise from 200 to 220','Total jobs rise from 500 to 600 as services grow faster','Agriculture’s share falls from 40% to about 36.67%','A falling share is compatible with a rising employment level'],
3:['Broad orders fall','Firms reduce planned saleable production','Derived demand for labour falls','Demand-deficient unemployment can rise despite suitable skills'],
5:['Unemployment removes earned income','Limited savings can cushion only some commitments','Spending cuts or hardship can follow without replacement earnings','Long duration can also weaken skills or later recruitment prospects']})
add('7.3',{
1:['Final output inside the territory identifies GDP','Adjustment for net factor income from abroad identifies GNP'],
3:['The factory’s output is produced inside the territory','Final furniture counts irrespective of foreign ownership, avoiding intermediate double counting'],
5:['Add residents’ relevant factor income received from abroad','Subtract corresponding factor income paid abroad'],
7:['Wages reward current labour','Rent is another factor reward, unlike a transfer without current production in exchange'],
8:['The output method records value added','The income method records earned factor rewards'],
10:['The grower adds N$100','The processor adds N$250 minus N$100 = N$150'],
12:['A new loan is financing, not earned factor income','A support transfer is not a current-production reward'],
14:['Include exports because they purchase domestic output','Remove imports because they represent foreign production']})
add('8.1',{
11:['Annual live births form the numerator','The specified whole population forms the denominator, with the rate per thousand'],
13:['Age structure affects the crude death rate','Health conditions also affect it, so the crude figure alone cannot rank services'],
15:['The 2.5 figure estimates births per woman using the period’s age-specific pattern','Its horizon is a lifetime estimate, not 2.5 births every year'],
17:['Immigration is 80 arrivals and emigration 120 departures','Immigration minus emigration gives net migration −40']})
add('9.1',{
2:['Original private net benefit N$4,000 exceeds cleaner N$3,000','That gives the owner a private reason to prefer the original method','Cleaner social net benefit N$2,000 exceeds original −N$1,000','External damage reverses the wider ranking','The full comparable effects and feasibility must hold','Prefer the cleaner method on the supplied social basis','Relate the judgement to external costs and who bears the cleaner-method cost'],
3:['Larger harvest raises current earnings','Current livelihoods therefore benefit','Damaged regeneration threatens future work','Future wetland services may also be lost','A lower feasible harvest must preserve regeneration and livelihoods','Prefer the managed option under those conditions','Explain why the current gain alone does not establish a good long-term outcome'],
4:['A ban conserves the resource more fully','That can preserve future options','A complete ban removes current harvest income','A genuinely sustainable managed harvest can retain some livelihoods','Monitoring must confirm regeneration and control damage','Prefer managed use under the supplied sustainable conditions','Shift to stricter conservation if damage persists'],
5:['Temporary protection supports local producer sales','Training can permit adjustment and efficiency improvement','Buyers face higher prices','Weaker competition can reduce improvement incentives if protection persists','Credible progress and an effective review/expiry are necessary','Support time-limited protection conditionally','Reject indefinite support without the stated improvement evidence'],
6:['Shared access can serve several producers','Reliable deliveries create useful benefits','Tax funding reduces private purchasing power','The other forgone project is an opportunity cost','Path use, maintenance and gains exceeding feasible alternatives are necessary','Support only under that net-value condition','Explain that ownership alone does not decide value or distribution']})

def apply(items):
 changed=[]
 for it in items:
  bits=it['item_id'].split('-');topic=bits[2]
  if not bits[3].isdigit():continue
  key=(topic,int(bits[3]))
  if key not in R:continue
  points=R[key];sub=it['subtype'];assert len(points)==it['mark_tariff'],it['item_id']
  if sub=='MECH':labels=['Starting change','Because/mechanism','Mechanism development','Consequence']
  elif sub=='APP':labels=['Context','Reason/conclusion']
  elif sub=='FEATURE':labels=['Feature/example','Distinct characteristic/example']
  elif sub=='EVAL':labels=['Argument for','Benefit development','Supporting comparison','Argument against/limitation','Condition/trade-off','Judgement','Conclusion linked to evidence']
  else:raise ValueError(sub)
  it['marking_guidance']=[f'{labels[i]} (1): {p}.' for i,p in enumerate(points)]
  changed.append(it['item_id'])
 return changed
