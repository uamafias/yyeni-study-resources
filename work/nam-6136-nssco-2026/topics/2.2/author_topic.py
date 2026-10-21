"""Original Codex manuscript: planning and a clearly dated NDP5 example."""
import sys
from pathlib import Path
TD=Path(__file__).resolve().parent
sys.path.insert(0,str(TD.parent))
from authoring_support import assemble
C={
 '01-00':[
 ('procedural','A development plan turns priorities into objectives, actions, resource allocations, responsibilities and a timetable; monitoring compares results with intended outcomes.'),
 ('comparison','An activity or output is not the same as a development outcome: building a facility does not establish that people can use an effective service.')],
 '02-00':[
 ('comparison','Short-term planning organises nearer actions and resources, while long-term planning sets direction over a longer horizon; their timeframes are relative to the context.'),
 ('factual','NDP5 covered 2017/18–2021/22. Its stated goals concerned inclusive and equitable economic growth, capable and healthy people, environmental sustainability and resilience, and effective governance.'),
 ('evaluative','Evaluate a dated plan by comparing its objectives with relevant implementation and outcome evidence, considering distribution, resources and limits on attributing a change to the plan.')],
 '02-01':[
 ('definition','Short-term planning concerns nearer actions, responsibilities, resources and deadlines within a wider direction.'),
 ('procedural','A near-term action can contribute to a longer goal when its output addresses a relevant constraint and is monitored rather than treated as proof of final success.')],
 '02-02':[
 ('definition','Long-term planning sets a direction and intended development outcomes over a longer horizon, often requiring several linked stages.'),
 ('causal','Long-term direction can coordinate shorter actions, while monitoring and changing conditions can require revisions to the route.')]
}
B={
 '01':[
 ('plain_explanation','From national direction to action',"National Development Plans provide direction by connecting development priorities to actions and intended results. Planning identifies the problem, the objective and the resources available. Implementation puts decisions into practice through assigned responsibilities and a timetable. Monitoring checks what was delivered and whether it helped produce the intended outcome. Evaluation uses that evidence to judge progress and decide what to change. A plan can coordinate activities, but its existence does not guarantee that resources arrive or actions are carried out.",['01-00']),
 ('process','A worked planning sequence',"In a fictional district, long journeys prevent access to skills training. The objective is to improve usable access. Planners first identify affected communities and the size of the access problem. They then choose a feasible response, allocate funds and assign responsibility for transport or local provision. During implementation they record what is delivered and who can use it. Monitoring compares attendance and completion with the starting position and the aim. If attendance remains low, the district investigates the remaining barrier and changes the action rather than simply declaring the project complete.",['01-00']),
 ('comparison','Output and outcome',"Vehicles purchased or lessons scheduled are outputs. Improved access and completion are outcomes. A vehicle without a driver or reliable maintenance may not improve access. In a fictional programme, two vehicles are purchased as planned, but use reaches only 30% of intended learners because one route cannot operate. The purchase target is met while the access outcome remains limited. Judge the evidence at the level of the stated objective.",['01-00']),
 ('cross_link','Keep the development purpose in view',"Topic 1.1 explains why income, services and participation are different dimensions. Topic 10.1 explains evidence collection. A useful planning account connects resources, responsible action and measurable outcomes instead of listing ambitions without implementation.",['01-00'])],
 '02':[
 ('comparison','Short and long time horizons',"Short-term planning concerns nearer actions and resource decisions. Long-term planning sets a direction and intended outcomes over a longer horizon. Their distinction is relative to the context; there is no universal number of years that fits every organisation or activity. A long-term aim to improve access to skilled work can involve shorter actions such as recruiting tutors, arranging transport or repairing a training room. These actions form a route towards the wider goal. They must be relevant to the barrier identified, not merely convenient to count.",['02-00','02-01','02-02']),
 ('worked_application','Stages should connect',"Consider an invented district aiming to widen training access over several years. For the next term, it schedules a serviceable vehicle, driver and route to communities with the longest journeys. That near-term action is specific enough to implement. The longer direction is wider access and improved capabilities. Monitoring attendance and completion tests whether the transport action contributes to that direction. If missing childcare rather than distance remains the main barrier, the route may need revision or a complementary response. Changing a practical action in light of evidence can support the long-term aim rather than abandon it.",['02-00','02-01','02-02']),
 ('plain_explanation','A dated national example: NDP5',"Namibia's Fifth National Development Plan, NDP5, covered 2017/18–2021/22. Use it here as a historical example. Its stated goals addressed inclusive and equitable economic growth, people's capabilities and health, environmental protection and resilience, and governance through effective institutions. These goals connect economic progress with social conditions, resources and public implementation. They are intended directions; listing them does not establish what was achieved. The National Planning Commission's [NDP5 summary](https://www.npc.gov.na/national-plans/national-plans-ndp-5/) records the period and goal indicators, checked for this lesson on 20 October 2026. Its target columns must be read as targets, not observed results.",['02-00']),
 ('evaluation','How to evaluate the example',"Begin with one stated goal, then identify evidence that would show progress towards it. For a human-capabilities goal, facility construction is relevant implementation evidence, but service access, quality or usable skills are closer to the intended outcome. Compare a baseline and later observation measured consistently. Ask whether progress reaches the relevant groups and whether the supporting resources can be maintained. A positive change may have several causes, so avoid attributing the whole change to a plan without evidence. Equally, an unmet target is not evidence that every action had no benefit. An evaluation should distinguish progress, remaining gaps and the limits of the evidence.",['02-00']),
 ('worked_application','An original evaluation case',"The following is fictional practice and is not a claim about NDP5 performance. A programme aims to increase training access in remote settlements. It meets a target of opening four centres. However, only one has regular tutors and attendance remains unchanged. Judged by buildings, implementation appears successful; judged by usable training access, the result is limited. Assigning tutors and monitoring actual attendance would address the gap more directly than opening a fifth centre. The judgement follows the stated access criterion and uses both construction and service evidence. It is stronger than declaring the whole programme successful because one target was met.",['02-00','02-01','02-02']),
 ('cross_link','Keep policy examples dated',"Vision 2030 in Topic 2.1 gives the longer context; health and education in Topics 7.2 and 7.3 explain some intended benefits. When evaluating NDP5, name its period and goals, then separate real source evidence from an illustrative scenario. This lesson does not claim a final national verdict or describe NDP5 as the current programme.",['02-00','02-01','02-02'])]
}
Q={
 1:('Explain how a National Development Plan can provide direction rather than a list of wishes.',
    'It links priorities to objectives, resources, responsibilities and actions. Monitoring compares results with intended outcomes so implementation can be assessed and adjusted.',
    ['Reason: connect a planning component to coordinated implementation or assessment of outcomes.']),
 2:('Describe how an invented district could use a development-planning cycle to address long journeys that prevent access to training.',
    'Establish the access problem and a measurable objective; choose a feasible route or local-provision response; allocate resources and responsibilities; implement it and compare participation and completion with the baseline, then adjust unresolved barriers.',
    ['Sequence: move coherently from problem/objective through implementation to monitoring and adjustment.','Application: connect the stages to training access and the travel barrier; unrelated generic stages are insufficient.']),
 3:('Differentiate between short-term and long-term development planning.',
    'Short-term planning organises nearer actions and resources, whereas long-term planning sets direction and outcomes over a longer horizon. Shorter actions should contribute to the longer direction.',
    ['Comparison: paired distinction in time horizon and role; do not impose an unsupported universal year boundary.']),
 4:('Explain whether this fictional programme should be judged successful against its stated aim of improving usable training access: four centres are opened as planned, but only one has regular tutors and attendance remains unchanged. Weigh building completion against the access outcome.',
    'It meets the construction output but is not yet successful against the stated access aim. Only one centre has regular tutors and attendance has not improved, so new buildings have not translated into wider use. Tutor provision and monitoring would address the implementation gap more directly than counting buildings alone.',
    ['Judgement: assess success against usable access, recognising the met construction target.','Reason: weigh the output and outcome evidence; connect the missing tutors to the limited result.']),
 5:('Describe two features of short-term development planning.',
    'It specifies nearer actions and deadlines. It assigns the resources and responsibilities needed to implement those actions in support of a wider goal.',
    ['Feature: nearer operational actions and concrete resource/responsibility arrangements.']),
 6:('Describe two features of long-term development planning.',
    'It sets a direction and intended outcomes over a longer horizon. It coordinates linked stages, with progress monitored and the route revised where conditions change.',
    ['Feature: longer direction/outcomes and connected stages or capacity to adjust the route.'])
}
P={
 'P01':(['01-00','02-00'],
 'State (a) the difference between an output and an outcome in development planning [2]. Explain (b) what this original fictional evidence implies for success against an access aim [4]: a programme buys both planned vehicles, but a missing driver leaves one route unused and participation reaches only 30% of intended learners.',
 '(a) An output is what the programme delivers, such as purchased vehicles; an outcome is the resulting change, such as usable access to training. (b) The purchase output is achieved, but the missing driver prevents one route operating, restricting access despite the vehicles. Reaching 30% shows the intended beneficiaries are not widely served. The evidence therefore supports a limited outcome rather than full success against the access aim.',
 ['Point (a), 2 marks: distinguish delivery from resulting change.','Development (b), up to 4 marks: connect both purchases and the driver/participation evidence to a judgement about the access aim.']),
 'P02':(['01-00','02-00'],
 'Describe (a) the relationship in this original fictional comparison of two training routes [3]: Route A operates 4 of 20 planned trips and learner attendance is 30%; B operates 18 of 20 and attendance is 80%. Suggest (b) which should receive an immediate reliability investigation if the aim is to improve access; both routes serve communities with learners wanting training [3].',
 '(a) More delivered trips accompany higher attendance: B operates 14 more trips and attendance is 50 percentage points higher. (b) Investigate A first because most planned trips do not run and attendance is much lower despite stated demand. Identifying and addressing its service barrier could improve usable access. The association is evidence for an investigation, not proof that transport explains every absence.',
 ['Evidence (a), up to 3 marks: relate trip delivery and attendance with accurate comparisons.','Meaning (b), up to 3 marks: prioritise and justify against access and reliability using both sources, without inventing the reason for missed trips.'])
}
if __name__=='__main__':
 assemble(TD,C,B,Q,P,[{'from':'Separate full essays for short-term, long-term and their integrated parent',
   'to':'One integrated comparison and worked evaluation lesson, retaining every target and item.',
   'why':'The approved handover permits integrated teaching and advisory minima; related ideas are explained once, then applied.'}])
