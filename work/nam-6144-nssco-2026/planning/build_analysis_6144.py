"""Build source-linked mining outputs from explicit semantic miner annotations.

No learner resources, contracts or work orders are produced. Counts, exposure,
tables and the analysis report are derived from the records rather than typed.
"""
import collections
import copy
import hashlib
import json
import re
from pathlib import Path

from miner_annotations_6144 import ANNOTATIONS

WS = Path(__file__).resolve().parents[1]
REPO = WS.parents[1]
EVID = WS / 'assessment-evidence'
CURR = WS / 'curriculum'
FACTS = json.loads((CURR / 'syllabus-facts.json').read_text())
CANDIDATES = json.loads((EVID / 'question-candidates.json').read_text())
MANIFEST = json.loads((EVID / 'SOURCE-MANIFEST.json').read_text())
SOURCES = {x['source_id']: x for x in MANIFEST}
TAG = {'M': 'misconception', 'O': 'omission', 'C': 'command-word miss',
       'S': 'shallow development', 'P': 'positive observation', 'N': 'source ambiguity'}


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def ev(short):
    return 'EV-6144-' + short


def sid(topic, bullet):
    return f'SYL-6144-{topic}-{int(bullet):02}'


# Meaning-selected command after a contextual preface, not a keyword classifier.
COMMAND_OVERRIDES = {
    '2020-P1-2(d)': 'would you advise', '2020-P1-3(a)(i)': 'what is meant by',
    '2020-P1-3(a)(ii)': 'why', '2020-P1-4(a)(i)': 'what is meant by',
    '2020-P1-5(d)': 'how effective', '2020-P2-1(b)': 'analyse',
    '2020-P2-2(b)': 'is it advisable', '2020-P2-3(b)': 'advise',
    '2020-P2-5(b)': 'would you allow', '2021-P2-2(b)': 'recommend',
    '2022-P1-3(c)': 'calculate', '2022-P1-5(d)': 'evaluate',
    '2022-P2-1(b)': 'evaluate', '2023-P1-5(c)': 'analyse',
    '2024-P1-2(c)': 'distinguish', '2024-P1-5(c)': 'distinguish',
}

VISUAL_OR_DATA = {
    '2020-P1-2(a)(iii)': 'read organisation chart', '2020-P1-2(b)': 'count direct reports',
    '2020-P1-4(c)': 'construct and interpret product-life-cycle diagram',
    '2020-P2-1(b)': 'calculate and interpret two liquidity ratios',
    '2021-P2-5(b)': 'compare profitability across years',
    '2022-P1-3(c)': 'calculate unit cost, markup and selling price',
    '2022-P1-5(d)': 'calculate and interpret profit margins',
    '2022-P2-4(b)': 'calculate and interpret liquidity ratios',
    '2023-P2-2(a)': 'construct and explain expanded organisation chart',
    '2023-P2-3(b)': 'compare liquidity; year-label discrepancy retained',
    '2023-P2-5(a)': 'derive a time series and construct labelled line graph',
    '2024-P2-5(a)': 'calculate solvency and compare with prior-year ratio',
}


def outcomes():
    result = {}
    for topic in FACTS['content_outline']:
        for n, bullet in enumerate(topic['specific_objectives'], 1):
            key = sid(topic['topic_id'], n)
            result[key] = {'objective_id': key, 'topic_id': topic['topic_id'],
                           'syllabus_bullet_index': n, 'syllabus_text': bullet['text'],
                           'source': bullet['source'], 'provenance': 'syllabus'}
    return result


def shape_for(record):
    paper, marks = record['paper_id'], record['mark_tariff']
    if paper == 'P1':
        if marks <= 2:
            split = {'A': marks, 'B': 0, 'C': 0, 'D': 0}
            steps = ['Supply the requested distinct knowledge elements; a two-mark definition needs sufficient precise meaning, while two named items normally earn one mark each.']
        elif marks == 6:
            split = {'A': 2, 'B': 2, 'C': 2, 'D': 0}
            steps = ['Identify two relevant knowledge elements.', 'Apply each to the particular business.', 'Explain the relationship or consequence required by the question, one development per element.']
        elif marks == 8:
            split = {'A': 2, 'B': 2, 'C': 2, 'D': 2}
            steps = ['Identify the relevant alternatives or positive/negative considerations.', 'Apply and develop their effects in the business context.', 'Reach a clear choice and support it by weighing the considerations relevant to this decision.']
        else:
            raise ValueError((paper, marks))
    elif marks == 8:
        split = {'A': 2, 'B': 2, 'C': 4, 'D': 0}
        steps = ['Identify two relevant knowledge elements.', 'Use distinct contextual evidence.', 'Develop each explanation more fully; this tariff does not automatically require an evaluative choice.']
    elif marks == 12:
        split = {'A': 4, 'B': 2, 'C': 2, 'D': 4}
        steps = ['Establish the relevant options/considerations with enough precise knowledge.', 'Apply and analyse them using the shared business case.', 'Weigh the options and make a supported decision; a repeated list or unsupported preference does not earn the full evaluation allocation.']
    else:
        raise ValueError((paper, marks))
    short = record['evidence_id'].removeprefix('EV-6144-')
    if short == '2020-P1-4(c)':
        steps = ['Construct the correctly shaped and labelled life-cycle diagram (A2).',
                 'Use the stage supported by the supplied business description (B2).',
                 'Explain why the current position follows from the case evidence (C2); do not extend beyond the supported stage merely to reproduce a memorised full curve.']
    if short in ['2020-P2-1(b)', '2021-P2-5(b)', '2022-P2-4(b)', '2023-P2-3(b)']:
        steps = ['Identify the requested two financial ratios and their formulas (A4).',
                 'Substitute the appropriate case data (B2) and calculate correctly with the required percentage or x:1 format (C2).',
                 'Compare the relevant results/years or the reliability of the measures, and support the financial judgement with evidence (D4); heed the recorded source-year discrepancy where applicable.']
    if short == '2022-P1-3(c)':
        steps = ['State the unit-cost and cost-plus selling-price relationships (A2).',
                 'Use the given cost, output and markup correctly (B2).',
                 'Complete both unit-cost and selling-price calculations, rather than stopping at cost or markup alone (C2).']
    if short == '2022-P1-5(d)':
        steps = ['State the relevant two profitability formulas (A2).',
                 'Substitute the financial-statement figures (B2), calculate percentage results (C2).',
                 'Interpret what the actual results say about performance and support the judgement (D2).']
    if short == '2023-P2-2(a)':
        steps = ['Construct the requested expanded hierarchy and direct-report relationships (A2).',
                 'Include the case-specific area and functional roles (B2).',
                 'Explain the usefulness of the chart for authority, responsibilities or communication, with developed effects (C4).']
    if short == '2023-P2-5(a)':
        steps = ['Draw the axes with quantity/unit and years labelled (A2).',
                 'Use the correct four years from the case (B2).',
                 'Derive the missing annual quantities and plot the correct time-series values in a line graph (C4); do not substitute a life-cycle sketch or bar chart.']
    if short == '2024-P2-5(a)':
        steps = ['Give total assets divided by total liabilities, with both formula components correctly placed (A2).',
                 'Combine the correct current/non-current assets and current/long-term liabilities from the case (B2).',
                 'Calculate the x:1 result (one C mark) and compare it with the prior-year position and the guide’s reference level (up to three further C marks). This 8-mark task carries analysis rather than an added evaluation allocation.']
    source = record['report_locator']
    return split, {'shape': steps, 'source': source, 'provenance': 'corpus',
                   'basis': 'Question-specific report guidance read alongside the repeated report AO grids; wording below paraphrases the demand rather than reproducing model answers.'}


def build_records(index):
    records, findings = [], []
    for source_id, annotation_text in ANNOTATIONS.items():
        selected = [r for r in CANDIDATES if r['source_id'] == source_id]
        lines = [x.strip() for x in annotation_text.strip().splitlines() if x.strip()]
        assert len(selected) == len(lines), (source_id, len(selected), len(lines))
        for candidate, annotation in zip(selected, lines):
            mapping, page_text, notes = annotation.split('|', 2)
            mapped = [sid(*value.split(':')) for value in mapping.split(',')]
            assert all(x in index for x in mapped), (candidate['evidence_id'], mapped)
            record = copy.deepcopy(candidate)
            short = record['evidence_id'].removeprefix('EV-6144-')
            year = record['year']
            report_id = f'ER-{year}'
            pages = [int(n) for n in page_text.split(',')]
            record['report_locator'] = {'source_id': report_id, 'path': SOURCES[report_id]['path'],
                                        'pdf_pages': pages, 'question_ref': record['question_ref'],
                                        'paper_id': record['paper_id']}
            report = json.loads((EVID / 'extracted' / f'{report_id}.json').read_text())
            page_map = {p['pdf_page']:p for p in report['pages']}
            assert all(n in page_map for n in pages)
            record['report_page_text_sha256'] = {str(n): hashlib.sha256(page_map[n]['raw'].encode()).hexdigest() for n in pages}
            record['objective_ids'] = mapped
            record['topic_ids'] = list(dict.fromkeys(index[x]['topic_id'] for x in mapped))
            record['primary_topic_id'] = record['topic_ids'][0]
            record['mapping_method'] = 'Codex read the question demand, the corresponding report discussion and the cited syllabus bullets, and selected these exact bullets by meaning; no token scoring or automatic nearest match.'
            record['mapping_provenance'] = 'judgement'
            record['mapping_confidence'] = 'mapped'
            if short == '2022-P1-2(d)':
                record['candidate_objective_ids'] = mapped
                record['objective_ids'] = []
                record['primary_topic_id'] = None
                record['mapping_confidence'] = 'unresolved: employers in paper; employees in report'
            if short == '2020-P1-1(a)(i)':
                record['mapping_confidence'] = 'qualified: report clarifies activity types despite ownership-form distractor in paper wording'
            if short == '2023-P1-5(c)':
                record['mapping_confidence'] = 'qualified: time-rate demand conflicts with task-completion wording; do not reuse stem'
            record['exam_series'] = str(year)
            record['exam_series_note'] = 'Annual paper identifier; no month/series name invented where the cover only states the year.'
            record['variant'] = None
            record['context_type'] = 'short_business_scenario' if record['paper_id'] == 'P1' else 'shared_business_case'
            text = record['question_text_internal_only']
            lead = text.split()[0].lower().strip(',:;')
            record['literal_first_token'] = lead
            compound = next((c for c in ['identify and explain', 'name and explain'] if text.lower().startswith(c)), None)
            record['command_word'] = COMMAND_OVERRIDES.get(short, compound or lead)
            record['command_mapping_note'] = 'Substantive task identified by reading; contextual prefaces are retained in the internal source text. Distinct question frames are not silently equated with glossary verbs.'
            record['secondary_task_words'] = sorted(set(re.findall(r'\b(justify|explain|suggest|consider|evaluate|analyse|compare|draw|show)\b', text.lower())) - {record['command_word']})
            record['stimulus_or_calculation'] = VISUAL_OR_DATA.get(short)
            parts = re.split(r'(?<!\w)([MOCSPN]):', notes)
            question_findings = []
            for i in range(1, len(parts), 2):
                kind, summary = TAG[parts[i]], parts[i+1].strip()
                finding = {'finding_id': f"EF-6144-{short}-{len(question_findings)+1:02}",
                           'evidence_id': record['evidence_id'], 'classification': kind,
                           'summary': summary, 'objective_ids': record['objective_ids'],
                           'source_locator': record['report_locator'], 'provenance': 'corpus',
                           'classification_provenance': 'judgement'}
                question_findings.append(finding)
                findings.append(finding)
            record['examiner_findings'] = [f['finding_id'] for f in question_findings]
            record['common_errors'] = [f['summary'] for f in question_findings if f['classification'] not in ['positive observation', 'source ambiguity']]
            split, shape = shape_for(record)
            record['ao_focus'] = [ao for ao, marks in split.items() if marks]
            record['report_ao_marks'] = split
            record['report_ao_marks_provenance'] = 'corpus: report part structure, not command-word-only inference'
            record['creditworthy_points'] = shape['shape']
            record['answer_shape_evidence'] = shape
            record['strong_response_features'] = ['Answer the exact requested dimension and beneficiary.', 'Use the case meaningfully rather than repeat a name or copy an unprocessed sentence.']
            if record['stimulus_or_calculation']:
                record['strong_response_features'].append('Show the appropriate construction/formula, use the supplied data, label units/axes and interpret the result where requested.')
            record['notes'] = ['Internal assessment evidence only; question wording and report wording must not be exported to learners.']
            records.append(record)
    return records, findings


def exposure(records, index):
    rows = []
    for key, objective in index.items():
        matches = [r for r in records if key in r['objective_ids']]
        years = sorted({r['year'] for r in matches})
        cls = 'recurrent' if len(years)>=4 else 'repeated' if len(years)>=2 else 'observed_once' if years else 'not_observed'
        rows.append({'objective_id':key,'topic_id':objective['topic_id'],
                     'question_parts':len(matches), 'distinct_series':len(years), 'series':years,
                     'maximum_tariff':max((r['mark_tariff'] for r in matches),default=0),
                     'command_word_mix':dict(collections.Counter(r['command_word'] for r in matches)),
                     'exposure_class':cls,'evidence_ids':[r['evidence_id'] for r in matches],
                     'provenance':'corpus','mapping_provenance':'judgement'})
    return {'qualification_id':'nam-6144-nssco-2026', 'granularity':'Transcribed syllabus bullets before member decomposition; not a final planner registry.',
            'definitions':{'recurrent':'directly mapped in 4–5 distinct years', 'repeated':'2–3 distinct years',
                           'observed_once':'1 distinct year','not_observed':'No confident direct match in this five-year collection; remains fully in scope.'},
            'counting_policy':'A part may map to multiple bullets. These are co-exposures, not separate marks. The unresolved employer/employee part is excluded from confident objective exposure.',
            'objectives':rows}


def command_table(records):
    listed = {x['word'] for x in FACTS['command_words']}
    all_words = listed | {r['command_word'] for r in records}
    result=[]
    for word in sorted(all_words):
        matches=[r for r in records if r['command_word']==word]
        literal=[r for r in matches if r['question_text_internal_only'].lower().startswith(word)]
        task_openings=[r for r in matches if r in literal or re.search(r'[.!?]\s+'+re.escape(word)+r'\b',r['question_text_internal_only'].lower())]
        secondary=[r for r in records if word in r['secondary_task_words']]
        counts=collections.Counter(r['mark_tariff'] for r in matches)
        maximum=max(counts.values(),default=0)
        result.append({'word':word,'in_syllabus_table':word in listed,
                       'substantive_task_count':len(matches),'literal_opening_count':len(literal), 'task_sentence_opening_count':len(task_openings),
                       'secondary_task_count':len(secondary),
                       'tariffs_seen':sorted(counts),'tariff_counts':dict(sorted(counts.items())),
                       'modal_tariffs':[k for k,v in sorted(counts.items()) if v==maximum],
                       'per_paper':{paper:dict(sorted(collections.Counter(r['mark_tariff'] for r in matches if r['paper_id']==paper).items())) for paper in ['P1','P2']},
                       'use_in_prompts':bool(task_openings),
                       'verdict':'observed task-sentence opener' if task_openings else 'observed only within task/frame' if matches or secondary else 'listed not observed',
                       'evidence_ids':[r['evidence_id'] for r in matches],
                       'provenance':'corpus','task_identification_provenance':'judgement',
                       'syllabus_sources':[c['source'] for c in FACTS['command_words'] if c['word']==word]})
    assert sum(row['substantive_task_count'] for row in result)==len(records)
    return result


# Curated concept confusions. Generic omissions/answering habits stay in findings,
# not as fictitious conceptual misconceptions. Each discriminator is our teaching judgement.
MISCONCEPTIONS = [
('Activity type versus ownership form','Classify what the enterprise does separately from who owns it.','Does the label describe production/trading activity or a legal ownership arrangement?','2020-P1-1(a)(i);2020-P1-1(a)(ii);2021-P2-1(a);2022-P1-1(a)(i)'),
('Organisation structure versus hierarchy','An organisation structure includes responsibility divisions; hierarchy describes authority levels.','Can you name both responsibilities and levels rather than only rank?','2020-P1-2(a)(i)'),
('Direct reports versus all workers below a manager','Span of control counts the people reporting directly to that manager.','Count one connecting reporting step, not every person lower on the chart.','2020-P1-2(b)'),
('Delegation versus decentralisation','Delegating a task and distributing decision authority through an organisation are different ideas.','Is one manager assigning authority for a task, or is decision authority dispersed across levels?','2020-P1-2(d)'),
('Informal group versus trade union or outside association','An informal workplace group arises outside the official structure through shared interests.','Is this a friendship/common-interest group within work, or an organisation representing worker interests?','2020-P1-3(a)(i)'),
('Recruitment versus training','Recruitment attracts candidates for vacancies; training develops workforce capability.','Is the action finding applicants or developing an employee’s skills?','2020-P1-3(c)'),
('Marketing versus market research or advertising','Research and advertising are particular activities within the wider marketing role.','Is this the wider customer-focused process, collecting information, or communicating a message?','2020-P1-4(a)(i);2021-P1-3(a)(i)'),
('Redundancy versus dismissal','A redundant role is no longer needed; dismissal is not the same reason for losing employment.','Has the job ceased to be needed, or is the individual being removed for another reason?','2020-P1-5(a)(i);2024-P1-3(b)'),
('Job security versus social security','Confidence that a job continues differs from the social protection benefits asked about.','Is the point about keeping employment or a protection/benefit arrangement?','2020-P1-5(b);2021-P1-4(b)'),
('Public limited company versus public-sector ownership','The public in public limited company does not by itself mean government ownership.','Who owns the enterprise: private investors or the state?','2020-P2-2(b)'),
('Nationalisation versus international trade','Nationalisation concerns ownership moving to the state, not trade across borders.','Is ownership changing to government, or are goods moving between countries?','2020-P2-2(b)'),
('Herzberg versus Maslow/Taylor and hygiene versus motivators','Keep each theory’s categories and causal claims separate; hygiene and maintenance are alternative labels for the same category.','Identify the theory first, then distinguish prevention of dissatisfaction from motivators.','2020-P2-4(a);2024-P2-2(a)'),
('Stakeholders versus workplace groups or production sectors','Stakeholders have an interest in business outcomes; activity sectors and workplace groups answer different classifications.','Does the named group have a business interest, or is it a sector/type of group?','2021-P1-1(a)(i)'),
('Cooperation/joint responsibility versus ownership forms','Working together and sharing responsibility do not name legal business ownership forms.','Is this a way people work together or a way an enterprise is legally organised?','2021-P1-1(c)'),
('Need for finance versus source of finance','A need explains why money is required; a source explains where it comes from.','Does the answer state a use of money or its provider/origin?','2021-P1-2(a)(i)'),
('Production plan versus entire business plan','The production plan is one operational component of a broader business plan.','Does the detail concern how production operates rather than every part of the business plan?','2021-P1-2(b)'),
('Packaging function versus branding/AIDA/mix labels','Packaging must be explained by what the container or wrapping does.','Does this answer state a function of the packaging itself?','2021-P1-4(a)(ii)'),
('Employee versus consumer protection','Keep the protected party and the relevant business relationship explicit.','Is the person acting as an employee or as a buyer?','2021-P1-4(c);2021-P1-4(d)'),
('AIDA versus the marketing mix','AIDA describes advertising response requirements; the mix describes marketing decisions.','Is the label an advertising response stage or a marketing-mix element?','2021-P1-5(a)(i)'),
('Job versus batch versus flow production','Distinguish individual specifications, groups of similar units and continuous standardised output.','What happens to variety, sequence and volume in this actual production process?','2021-P2-2(b);2022-P2-2(b)'),
('Economies of scale versus economic systems','Scale economies concern unit-cost advantages of business size; economic systems concern resource allocation.','Is the question about a growing enterprise’s costs or the economy’s ownership/allocation arrangements?','2021-P2-4(a)'),
('Public/private finance and internal/external finance','These are distinct classification axes; identify the sector and origin separately.','Which sector is borrowing, and does the money arise inside or outside that business?','2022-P1-2(a)(i);2022-P1-2(a)(ii)'),
('Profit versus cash','Profit is a performance measure; cash is an available monetary resource.','Can a profitable business still lack the cash needed for an immediate payment?','2022-P1-2(b)'),
('Profitability versus liquidity versus solvency','Profit performance, short-term payment ability and total asset cover answer different questions.','Choose the formula by the financial question, not by whichever figures look familiar.','2022-P1-5(a)(i);2022-P2-4(b);2024-P2-5(a)'),
('Unit/average cost versus marginal cost','Unit cost averages the total across output; marginal cost concerns an extra unit.','Is the figure total cost divided by output or the added cost from additional output?','2022-P1-5(a)(ii);2024-P1-1(a)(i)'),
('Craft versus industrial union','A craft union groups a skill/trade; an industrial union groups workers within an industry.','Are members linked by an occupation/skill or by their industry?','2022-P2-1(a)'),
('Franchisor versus franchisee','The franchisor grants the business format/brand rights; the franchisee uses them under agreement.','Who is selling the right and who is buying/using it?','2022-P2-1(b)'),
('Communication elements versus types/ways','Sender/message/feedback are process elements, not the same classification as internal/external or verbal/written.','Is the answer a process component, a direction/boundary category, or a communication way?','2023-P1-1(a)(i);2024-P2-1(b)'),
('Manager qualities versus management functions','Qualities describe attributes/capabilities; functions describe management tasks.','Does the phrase describe the person’s capability or the task they perform?','2023-P1-1(a)(ii)'),
('Marketing promotion versus job promotion','A product communication activity differs from an employee moving to a higher position.','What is being promoted: the offer to customers or an employee’s position?','2023-P1-3(a)(ii)'),
('Specialisation levels versus management levels','Levels of specialisation classify concentration of activity, not managerial rank.','Is the classification about production focus or organisational authority?','2023-P1-3(b)'),
('Organisational conflict versus organisational structure','Disagreement differs from the arrangement of authority and responsibilities.','Is the description about a dispute or about the design of roles/reporting?','2023-P1-5(a)(i)'),
('Non-financial rewards versus cash allowances','A cash allowance is not made non-financial simply by calling it a benefit.','Is the reward money paid as an allowance or a distinct benefit/service/experience?','2023-P1-5(b)'),
('Close-corporation members versus company shareholders','Use the ownership vocabulary appropriate to the form being analysed.','Does this legal form have members or shareholders?','2023-P2-2(b)'),
('Loan security versus physical security','Security in lending refers to collateral/repayment protection in this context.','Is an asset securing repayment, or is someone physically guarding premises?','2023-P2-4(a)'),
('Location factors versus factors of production','A location decision needs reasons for a place; factor inputs alone do not explain that choice.','Explain why a particular site is suitable, rather than merely naming an input.','2023-P2-4(b)'),
('Time-series line graph versus product-life-cycle/bar chart','Choose a representation that matches the measured data and requested construction.','Are actual values over stated years plotted on labelled axes?','2023-P2-5(a)'),
('Income/expenses versus net profit/loss and fixed/variable cost','Money received/spent, the resulting profit/loss and cost behaviour are different concepts.','What is being measured: a flow, the difference between flows, or cost response to output?','2024-P1-1(a)(ii);2024-P1-1(b)'),
('Job production versus on-the-job training','A production method is not a workforce training method.','Is the action making a product or teaching a worker?','2024-P1-1(d)'),
('Primary/secondary research and internal/external sources','Whether information already exists differs from whether its source is inside the business.','Ask separately whether data are newly gathered and where the existing information originates.','2024-P1-2(a)(ii)'),
('Market versus product orientation','Customer research leading production differs from product-led decisions.','What guides the offering first: identified customer wants or the product focus?','2024-P1-2(c)'),
('Shop steward versus any trade-union official','The syllabus identifies the workplace-elected unpaid representative as a particular role.','Is the role an unpaid workplace representative elected by members?','2024-P1-3(a)(i)'),
('Fiscal versus monetary policy mechanisms','Tax/spending tools differ from monetary/interest-rate tools.','Identify the tool before tracing the effect on spending and the business.','2024-P1-4(c)'),
('Distribution versus transport','Transport moves goods; distribution describes how the offer reaches customers, including channels.','Is the answer a movement method or the route/availability arrangement?','2024-P1-5(a)(i)'),
('Product versus production','An offering is not the activity of making it.','Does the marketing-mix category name what is offered rather than the making process?','2024-P1-5(a)(ii)'),
('Partnership versus limited-liability incorporated ownership','Do not transfer shareholder/limited-liability features to an ordinary partnership in this syllabus model.','Which form is being considered, and what happens to the owners’ liability?','2024-P2-2(b)'),
('Quality circles versus worker councils','Different participation arrangements need their own purpose, membership and decision process.','Can the learner explain how each named arrangement operates before choosing?','2024-P2-3(b)'),
]


def misconceptions(records):
    lookup={r['evidence_id']:r for r in records}
    result=[]
    for n,(title,correction,test,refs) in enumerate(MISCONCEPTIONS,1):
        matched=[lookup[ev(x)] for x in refs.split(';')]
        result.append({'misconception_id':f'MISCON-6144-{n:03}', 'title':title,
                       'correct_distinction':correction,'discriminating_test':test,
                       'objective_ids':sorted({o for r in matched for o in r['objective_ids']}),
                       'evidence_ids':[r['evidence_id'] for r in matched],
                       'sources':[r['report_locator'] for r in matched],
                       'distinct_years':sorted({r['year'] for r in matched}),
                       'provenance':'corpus','correction_and_test_provenance':'judgement',
                       'verification_note':'Examiner evidence establishes that candidates made the confusion; it does not independently verify every domain/legal claim. Reconcile terminology and jurisdiction in planning.'})
    return result


SOURCE_ISSUES = [
    {'id':'SRC-01','sources':['QP-2020-P1 PDF p.1','QP-2020-P2 PDF p.1','syllabus PDF p.24'], 'issue':'2020 covers print 2 hours; syllabus and later papers print 2 h 15 min.', 'handling':'Retain 2020 as first-examination content evidence; use the approved syllabus for current duration.'},
    {'id':'SRC-02','sources':['ER-2020 PDF p.77'], 'issue':'Paper 2 total row prints analysis 23, although its part rows give 4+2 per question and five questions.', 'handling':'Preserve the printed typo; the part rows and syllabus give analysis 30/100, not 23.'},
    {'id':'SRC-03','sources':['QP-2022-P1 Q2(d) PDF p.7','ER-2022 PDF p.78'], 'issue':'Question says employers; report guidance and marks discuss employees.', 'handling':'Retain the part and tariff but leave confident objective mapping empty; candidate employee-protection mapping is explicitly provisional.'},
    {'id':'SRC-04','sources':['QP-2023-P2 PDF p.2 and Q3(b) p.8','ER-2023 PDF p.91'], 'issue':'Case table labels the first year 2019; the question and report comparison call it 2020.', 'handling':'Do not silently change the source year; use original coherent data in learner tasks.'},
    {'id':'SRC-05','sources':['ER-2024 PDF p.94'], 'issue':'Hygiene-factor paragraph first says the factors do not themselves motivate, then includes contradictory motivating phrasing.', 'handling':'Treat as a guide defect; do not copy it into a teaching claim. Keep hygiene/maintenance and motivators distinct.'},
    {'id':'SRC-06','sources':['ER-2020 PDF p.78','ER-2023 PDF p.91','ER-2024 PDF p.102'], 'issue':'Some displayed ratio results/accepted values use truncation or wider tolerance: 24/36 and 12/18 are shown as 0.66; 16/18 as 0.88; 157/303 accepts 0.51 or 0.52.', 'handling':'Recompute: 0.67, 0.89 and 0.52 to two decimals under Annexe A. Do not propagate truncation into new worked examples.'},
    {'id':'SRC-07','sources':['ER-2020 PDF pp.65,77','ER-2023 PDF p.79','ER-2024 PDF pp.79,92'], 'issue':'Application commentary varies: earlier reports reject merely repeating company/product names, while later reports discuss distinct case details and guide examples sometimes credit named contextual references.', 'handling':'Teach a relevant case fact linked to a consequence and use distinct details; avoid promising that a name alone always earns or never earns credit.'},
    {'id':'SRC-08','sources':['QP-2023-P1 Q5(c) PDF p.13','ER-2023 PDF pp.86–87'], 'issue':'Time-rate task includes wording about task completion within a time period; the guide has a per-unit-of-work phrase under time rate.', 'handling':'Preserve the intended worker-motivation demand, flag ambiguous wording and use unambiguous payment definitions in new tasks.'},
    {'id':'SRC-09','sources':['ER-2022 PDF p.80','ER-2021 PDF p.77'], 'issue':'The 2022 guide separates avoidance from resolution methods more narrowly than the syllabus and other report examples.', 'handling':'Do not turn one guide’s contextual rejection into a universal claim that negotiation can never resolve conflict.'},
    {'id':'SRC-10','sources':['ER-2024 PDF p.90','ER-2023 PDF p.81'], 'issue':'Specialisation/division of labour is accepted as a productivity factor in 2024 but rejected among responses in the specific 2023 task.', 'handling':'Keep acceptance/rejection attached to its question context; do not blacklist a generally in-scope causal relationship.'},
    {'id':'SRC-11','sources':['syllabus PDF pp.12,34'], 'issue':'Topic 2.4 places inventory turnover in a liquidity list, while Annexe A groups it under efficiency.', 'handling':'Keep both source descriptions and use the ratio’s actual numerator, denominator and interpretation rather than forcing a false classification.'},
    {'id':'SRC-12','sources':['ER-2020 PDF p.82'], 'issue':'Worker-participation knowledge narrative appears to describe more components than its stated 4-mark subtotal.', 'handling':'Use the 12-mark allocation and demand shape; do not copy inconsistent component arithmetic into marking guidance.'},
]


def topic_totals(records):
    result=[]
    for topic in FACTS['content_outline']:
        matches=[r for r in records if r['primary_topic_id']==topic['topic_id']]
        result.append({'topic_id':topic['topic_id'],'title':topic['title'],
                       'parts':len(matches),'marks':sum(r['mark_tariff'] for r in matches),
                       'years':sorted({r['year'] for r in matches}),
                       'primary_allocation_provenance':'judgement; marks counted from the selected whole part, not official topic splits'})
    return result


def make_report(records, findings, exposure_doc, words, misconceptions_list, totals):
    total_marks=sum(r['mark_tariff'] for r in records)
    classes=collections.Counter(x['exposure_class'] for x in exposure_doc['objectives'])
    mapped=sum(bool(r['objective_ids']) for r in records)
    lines=['# Corpus analysis — NSSCO Business Studies 6144','',
           'Owner: Vitalis. Miner: Codex. Completed 27 October 2026. Step 3 evidence summary; no plan or learner resources are approved by this report.','',
           '## 1. The corpus','',
           f"Read the ten 2020–2024 question papers and the Business Studies sections of five annual examiner reports: {len(records)} question parts, {total_marks} available marks. All ten papers reconcile independently to 100 marks and every main question to 20. The 2020 Paper 1 (a) allocation sometimes splits into 2+1+1 rather than 2+2; no part was dropped to force a fixed count.",'',
           'The syllabus was read first. Vitalis confirmed its AO and paper tables before this analysis. Assessment sources are internal evidence only: no official question or model-answer wording is authorised for learner output. The annual papers state years; an unstated month or variant is not invented. 2022/2023 filenames say First Proof and final-paper equivalence is unverified. 2020 paper timing differs from the approved syllabus and is retained as older timing evidence, not the current timing authority.','',
           'No standalone mark schemes, 2025 papers/reports, grade-threshold tables or specimen papers were found locally. The examiner reports do contain extensive question-specific marking guidance, AO allocations and worked answers. These support the answer-shape findings below; they do not become ten standalone mark schemes by relabelling. Duplicate report copies count once.','',
           'Both ordinary and layout pypdf extraction were retained. The miner read every extracted question, the case data and report observation/marking passages. Thirteen selected chart/data/guide pages were rendered and visually inspected; this is not a claim of visual inspection of every PDF page. The filtered report review packets aid navigation and are not the complete reports. Full subject-section text remains saved.','',
           '## 2. What each paper looks like','',
           '| Paper and part | Repeated tariff | Knowledge A | Application B | Analysis C | Evaluation D |',
           '|---|---:|---:|---:|---:|---:|',
           '| Paper 1 (a), combined | 4 | 4 | 0 | 0 | 0 |',
           '| Paper 1 (b) | 2 | 2 | 0 | 0 | 0 |',
           '| Paper 1 (c) | 6 | 2 | 2 | 2 | 0 |',
           '| Paper 1 (d) | 8 | 2 | 2 | 2 | 2 |',
           '| Paper 2 (a) | 8 | 2 | 2 | 4 | 0 |',
           '| Paper 2 (b) | 12 | 4 | 2 | 2 | 4 |','',
           'Sources: ER-2020 PDF pp.65 and 77; ER-2022 PDF pp.83 and 90; individual report guides across the corpus. The Paper 2 total-row typo in ER-2020 is recorded separately. These are evidence-backed recurring allocations, not a licence to assign an AO from a verb alone. Arithmetic from these observed part structures reconciles to the approved whole-qualification 40/20/25/15 AO proportions.','',
           'Paper 1 presents separate short business scenarios across five compulsory questions. Paper 2 uses one shared case for five compulsory questions. Its 8-mark analytical part differs from Paper 1’s 8-mark evaluative part: identical tariffs do not imply identical skills. Ratio calculation and interpretation, chart reading/construction and a genuine numerical line graph occur alongside prose.','',
           '## 3. Command words actually used','',
           'Counts below identify one substantive leading task per part. A contextual preface such as a business name or Using is retained in the evidence; extracting the substantive task after it is labelled judgement. Distinct question frames and compound openers remain separate. Secondary instructions such as justify are tracked separately and are not added to the one-task denominator.','',
           '| Task word/frame | Parts | Tariffs (marks × count) | Modal tariff(s) | Papers | Prompt verdict |',
           '|---|---:|---|---|---|---|']
    for word in sorted(words,key=lambda x:(-x['substantive_task_count'],x['word'])):
        if not word['substantive_task_count']:
            continue
        tariff=', '.join(f'{k}×{v}' for k,v in word['tariff_counts'].items())
        papers=', '.join(p for p,v in word['per_paper'].items() if v)
        verdict='observed opener' if word['use_in_prompts'] else 'embedded frame/task only'
        lines.append(f"| {word['word']} | {word['substantive_task_count']} | {tariff} | {', '.join(map(str,word['modal_tariffs']))} | {papers} | {verdict} |")
    not_observed=[w['word'] for w in words if w['in_syllabus_table'] and not w['substantive_task_count'] and not w['secondary_task_count']]
    secondary=[w['word'] for w in words if w['in_syllabus_table'] and not w['substantive_task_count'] and w['secondary_task_count']]
    lines += ['', 'Listed without substantive or secondary observation: '+', '.join(not_observed)+'.',
              'Listed and observed only as a secondary instruction: '+', '.join(secondary)+'.',
              'The glossary has 25 entries/24 distinct expressions, including two Explain definitions. Observed compound/frame forms include Identify and explain, Name and explain, What is meant by, Why and Examine. Prompt permission requires an observed task-sentence opener; Calculate opens the demand sentence after numerical setup, even though it is not the first word of that entire part. The full JSON carries the per-paper tariffs and source IDs. Do not convert a listed but unused verb into a prompt merely to vary language.','',
              '## 4. What a creditable answer looks like','',
              '- Short knowledge: answer exactly what is asked. A two-mark definition needs sufficient precise meaning; two requested items normally earn one mark each. Do not impose two full definitions when a two-mark question asks for one element from each concept.',
              '- Paper 1, 6 marks: two relevant knowledge points, each linked to the case and developed into the requested relationship/effect. Comparisons need both named concepts; how/why, feature/benefit and stakeholder/user-purpose distinctions matter.',
              '- Paper 1, 8 marks: relevant knowledge, contextual application and causal development, followed by an evidence-based choice. Discuss the relevant positive and negative considerations or alternatives; do not add irrelevant alternatives where a named method itself is being assessed.',
              '- Paper 2, 8 marks: two knowledge elements, case application and deeper analysis. There is no automatic evaluation allocation. Graph/ratio tasks distribute these elements differently: follow the question-specific guide.',
              '- Paper 2, 12 marks: enough precise knowledge across the required options, contextual analysis and a developed comparative judgement. Which options to discuss depends on the task: a change-to-franchise question can concern the franchisor’s consequences rather than a generic before/after essay.',
              '- Quantitative work: choose the ratio from the financial question; give the formula, substitute correct figures, show a correctly formatted result, then interpret/compare it when asked. Profitability percentages differ from liquidity/solvency x:1 notation. Use Annexe A’s two-decimal convention, not accidental truncation in a report.',
              '- Context: link an original relevant fact to the point. A name or copied case sentence alone is an unreliable application strategy; distinct applications are needed for distinct credits. Preserve the reports’ variable wording rather than promising a universal marking shortcut.',
              '- Evaluation: a choice needs reasons that weigh the actual alternatives/conditions. A repeated advantage list or contradictory choices is insufficient. Reports recommend building the discussion before the conclusion; this is a preparation structure, not a mechanical universal order-of-sentences mark rule.','',
              'These are paraphrases of report structures and observations, not reproduced model answers. Guide inconsistencies and jurisdictional/legal simplifications must be resolved before they become factual teaching claims.','',
              '## 5. Where the marks fall','',
              'The following is a non-overlapping primary-topic allocation selected by the miner from each question’s meaning; the question tariffs are counted, while assignment of a whole multi-topic question to its principal topic is judgement. It is not a published board topic-weighting table. Co-exposure to additional syllabus bullets is retained separately without double-counting marks.','',
              '| Primary topic | Parts | Whole-part marks | Share of 1,000 | Years |',
              '|---|---:|---:|---:|---|']
    for topic in sorted(totals,key=lambda x:(-x['marks'],x['topic_id'])):
        lines.append(f"| {topic['topic_id']} {topic['title']} | {topic['parts']} | {topic['marks']} | {topic['marks']/total_marks:.1%} | {', '.join(map(str,topic['years'])) or '—'} |")
    unresolved=[r for r in records if not r['objective_ids']]
    lines += [f"| Unresolved employer/employee source discrepancy | {len(unresolved)} | {sum(r['mark_tariff'] for r in unresolved)} | {sum(r['mark_tariff'] for r in unresolved)/total_marks:.1%} | 2022 |",'',
              f"Confident or explicitly qualified direct mappings: {mapped}/{len(records)} parts. All {len(exposure_doc['objectives'])} syllabus bullets remain in the exposure file: "+', '.join(f'{k} {v}' for k,v in sorted(classes.items()))+'.',
              'Exposure classes count distinct years: recurrent 4–5; repeated 2–3; observed_once 1; not_observed 0. These thresholds are our declared planning categories. Broad list bullets have not yet been decomposed into member objectives; observing one member does not prove every member was examined. No low-frequency or unobserved outcome is removed from scope.','',
              '## 6. How candidates lose marks','',
              'Each point below is repeated or otherwise clearly evidenced in the reports. Evidence IDs and question/page locators are in examiner-findings.json; positive observations remain separately classified.',
              '- Precise knowledge is missing or circular: a definition repeats its term, omits a defining feature, or substitutes a nearby concept. Resource response: teach the distinction, then test retrieval in an original short question.',
              '- Knowledge is not applied to the actual business, or the same case detail is repeated. Resource response: show how a relevant fact changes the explanation, with more than one distinct application.',
              '- A point is named but its consequence is not developed. Resource response: demonstrate point → because → consequence for the requested worker/business/other party.',
              '- Evaluative answers are one-sided, give no choice, or repeat the body as the conclusion. Resource response: model weighing the actual alternatives and a supported decision.',
              '- The requested dimension is missed: how instead of why, feature instead of benefit, finance source instead of need, business effect instead of worker effect, or the wrong protected stakeholder. Resource response: identify verb, object, beneficiary and decision before answering.',
              '- Calculations stop before the required final result, use the wrong financial ratio, omit percentage/ratio formatting, or are not interpreted. Resource response: formula → substitution → result with units/format → meaning/comparison.',
              '- Graphs/charts are omitted, mislabelled or replaced with the wrong representation. Resource response: original organisation-chart, product-life-cycle and numerical line-graph practice with checked labels and values.',
              '- Theme 5 is underprepared or answered generically. Resource response: teach producer assistance, environment, employee protection, consumers and capital providers distinctly, including both effects and judgement.','',
              'Recurring examples: activity types/forms (2020 P1 Q1 and 2021 P2 Q1); unit/marginal cost (2022 and 2024 P1); Herzberg/Maslow (2020 and 2024 P2); redundancy/dismissal (2020 and 2024 P1). Theme 5 and application weaknesses recur across report years. These are qualitative report observations, not candidate-level statistical failure rates.','',
              '## 7. Misconceptions','',
              f"Curated {len(misconceptions_list)} concept-confusion entries, each with source-linked evidence, selected syllabus bullets, a corrected distinction and a discriminating test. Entries include single-year evidence and say so; frequency is not invented. Generic omissions, shallow chains, unsupported choices and command misses remain answering-skill findings rather than artificial MISCON cards. Correction/test wording is our judgement and still needs author/reviewer checking.",'',
              '## 8. Scope and source limitations','',
              'The syllabus limits detailed ownership legal procedures and requires descriptive social cost-benefit treatment. Additional brief/simple/general depth statements remain explicitly sourced. Scope scan contains two enforceable candidate regex rules plus semantic-review obligations for limits a keyword scan cannot judge. Patterns are tested against must-catch and must-allow examples; a clean scan cannot establish the depth of an explanation. In-scope marginal cost, ratio work and exchange-rate conversion must not inherit another qualification’s exclusions.','',
              'Source issue register:', '']
    for issue in SOURCE_ISSUES:
        lines.append(f"- {issue['id']}: {issue['issue']} Sources: {'; '.join(issue['sources'])}. Handling: {issue['handling']}")
    lines += ['', 'No grade-threshold evidence was available, so this report does not invent a mark total needed for a grade. No 2025 frequency claim is made. Report observations were curated at question-part level, including positive performance notes; this is not a sentence-by-sentence inventory of every praise or teacher-administration comment. Source quotations and official answers remain internal.','',
              '## 9. What this means for the plan','',
              '- Cover all five themes and every syllabus member; use exposure to tune emphasis, never to delete content.',
              '- Prepare for the actual tariff/paper combinations. Paper 1’s 8-mark judgement and Paper 2’s 8-mark analysis need different practice structures.',
              '- Give accounting/ratios, production/location, marketing and Theme 5 enough linked application and decision practice, while preserving full coverage of the remaining topics.',
              '- Build original Namibian contexts, N$ figures, visual constructions and marking guidance; do not paraphrase an official case into a near-copy.',
              '- Allocate misconception discrimination separately from general exam-answering skills; use both AO and Bloom labels on later items.',
              '- Resolve source ambiguities in the plan rather than silently copying guide errors or treating an accepted contextual answer as a universal business/legal fact.',
              '- Carry the missing mark schemes, 2025 data and grade thresholds as limitations. Seek no additional source acquisition without a reason that changes the plan.', '',
              'Next checkpoint: Vitalis reads the summaries of sections 2, 3 and 6 and confirms that they fit the examination. Only then begin Step 4 planning. No contracts, work orders, topic budgets or learner resources have been generated.', '']
    return '\n'.join(lines)


def scope_scan():
    rules=[
        {'rule_id':'SCOPE-6144-LEGAL','topic_id':'2.1',
         'source':next(x['source'] for x in FACTS['scope_limits_and_requirements'] if x.get('topic_id')=='2.1'),
         'pattern':r'\b(?:memorandum of association|articles of association|company registration forms?|step.by.step (?:company )?registration)\b',
         'provenance':'judgement','action':'review potential detailed legal procedure; source limit does not exclude basic liability/ownership concepts',
         'must_catch':['Complete the company registration form.','Explain the articles of association.'],
         'must_allow':['Owners have limited liability.','A franchisee uses a franchisor’s business format.']},
        {'rule_id':'SCOPE-6144-CBA','topic_id':'5.1',
         'source':next(x['source'] for x in FACTS['scope_limits_and_requirements'] if 'entirely descriptive' in x['text']),
         'pattern':r'\b(?:net present value|discounted cash flow|social discount rate|monetis\w* (?:all |the )?social (?:costs|benefits))\b',
         'provenance':'judgement','action':'review potential quantitative social-cost-benefit treatment',
         'must_catch':['Calculate net present value for the social project.','Choose a social discount rate.'],
         'must_allow':['Compare the social costs and social benefits descriptively.','Calculate the current ratio using the financial table.']},
    ]
    for rule in rules:
        pattern=re.compile(rule['pattern'],re.I)
        assert all(pattern.search(s) for s in rule['must_catch'])
        assert not any(pattern.search(s) for s in rule['must_allow'])
    return {'scope_scan_id':'SCOPE-6144-NSSCO', 'status':'miner candidates for planner review; no contracts created',
            'rules':rules,'semantic_review_requirements':FACTS['scope_limits_and_requirements'],
            'note':'Every stated depth/application/calculation limit is retained. Brief/simple/general depth, case relevance and rounding cannot be established by these regexes. Advanced terms are review signals selected by judgement, not verbatim syllabus exclusions.'}


def main():
    if (EVID/'step3-accepted/assessment_evidence.json').exists():
        raise SystemExit('Step 3 is snapshotted and Step 4 has adapted canonical inputs. Do not overwrite them with the mining generator. Inspect step3-accepted/ or explicitly reopen analysis/planning first.')
    index=outcomes()
    records,findings=build_records(index)
    exp=exposure(records,index)
    commands=command_table(records)
    miscon=misconceptions(records)
    totals=topic_totals(records)
    assert len(records)==176
    assert len({r['evidence_id'] for r in records})==len(records)
    for source in ANNOTATIONS:
        paper=[r for r in records if r['source_id']==source]
        assert sum(r['mark_tariff'] for r in paper)==100
        for q in range(1,6):assert sum(r['mark_tariff'] for r in paper if r['question_number']==q)==20
    assert sum(t['marks'] for t in totals)+sum(r['mark_tariff'] for r in records if r['primary_topic_id'] is None)==1000
    write(CURR/'syllabus-outcome-index.json', {'note':'Generated IDs for undecomposed syllabus bullets; planner must retain traceability when creating the final objective registry.','objectives':list(index.values())})
    write(EVID/'assessment_evidence.json',records)
    write(EVID/'examiner-findings.json',findings)
    write(EVID/'command-word-evidence.json',commands)
    write(EVID/'source-issues.json',SOURCE_ISSUES)
    write(EVID/'topic-mark-allocation.json',totals)
    write(CURR/'exam-exposure.json',exp)
    write(CURR/'misconceptions.json',{'qualification_id':'nam-6144-nssco-2026','misconceptions':miscon})
    write(CURR/'scope-scan.json',scope_scan())
    write(CURR/'answer-shapes.json',{'qualification_id':'nam-6144-nssco-2026','provenance':'corpus; paraphrased demand with judgement in synthesis',
                                  'per_question':[{'evidence_id':r['evidence_id'],'paper_id':r['paper_id'],'command_word':r['command_word'],'mark_tariff':r['mark_tariff'],'ao_marks':r['report_ao_marks'],**r['answer_shape_evidence']} for r in records],
                                  'source_issue_ids':[x['id'] for x in SOURCE_ISSUES],
                                  'guard':'Part-specific graph/calculation guidance takes precedence over a generic prose template; no mark is awarded solely from the presence of a memorised phrase.'})
    report=make_report(records,findings,exp,commands,miscon,totals)
    (REPO/'operations/analysis/6144-nssco-business-studies-corpus-analysis.md').write_text(report)
    summary={'status':'pass','papers':len(ANNOTATIONS),'report_years':5,'question_parts':len(records),
             'marks':sum(r['mark_tariff'] for r in records),'paper_totals_reconciled':10,
             'main_question_totals_reconciled':50,'parts_with_report_guidance':len(records),
             'parts_with_confident_or_qualified_mapping':sum(bool(r['objective_ids']) for r in records),
             'unresolved_mapping_parts':[r['evidence_id'] for r in records if not r['objective_ids']],
             'examiner_findings':len(findings),'finding_classes':dict(collections.Counter(f['classification'] for f in findings)),
             'curated_misconceptions':len(miscon),'syllabus_bullets':len(index),
             'scope_pattern_positive_examples':4,'scope_pattern_negative_examples':4,
             'visual_pages_inspected':13,'source_issues':len(SOURCE_ISSUES),
             'note':'This validates source-linked mining counts and internal consistency, not a publication decision or an independent content review.'}
    write(EVID/'mining-validation.json',summary)
    (EVID/'GAPS.md').write_text('''# Evidence gaps — NSSCO Business Studies 6144

- No standalone mark schemes, 2025 papers/reports, specimen papers or grade thresholds were found locally. Source collection was explicitly accepted by Vitalis. Report marking guidance is used with that provenance, not called a standalone mark scheme.
- 2022/2023 question filenames say First Proof. Final-version equivalence has not been established. Covers do not consistently give a month; no month/variant is invented.
- One 8-mark employer/employee question has unresolved meaning; no confident objective mapping is fabricated. Other qualified mappings and twelve source issues are retained in the evidence.
- Syllabus outcome IDs refer to the 146 undecomposed bullets. Observing a broad list bullet does not prove every listed member was tested. Planner decomposition must preserve these links.
- All 176 parts have source-linked report commentary/guidance. Examiner observations are curated paraphrases at question-part level, not an exhaustive sentence count of teacher advice or candidate praise. Missing a statement from the curated set is not evidence that no such statement exists.
- Thirteen selected data/chart/guide pages were viewed. Text was extracted in ordinary and layout modes; all-page visual review is not claimed. No OCR was required for these text-bearing sources.
- Report model answers are not automatically verified factual/legal authorities. Contextual acceptance rules, ratio norms and apparent guide mistakes must not be universalised or reproduced in learner content.
- Exposure is conditional on this five-year collection. It does not predict the forthcoming paper or justify removing unobserved outcomes. No learner publication, independent subject review or platform import is claimed.
''')
    (EVID/'IMAGE-REVIEW.md').write_text('''# Image review — NSSCO Business Studies 6144

Codex inspected rendered contact sheets of thirteen selected original pages, 27 October 2026:

- QP-2020-P1 PDF p.4: product organisation chart; direct reports checked visually.
- QP-2020-P2 PDF p.3; QP-2021-P2 PDF p.3; QP-2022-P1 PDF p.14; QP-2022-P2 PDF p.2; QP-2023-P2 PDF p.2; QP-2024-P2 PDF p.2: financial/case data inspected.
- QP-2023-P2 PDF pp.5 and 11: actual chart and line-graph construction demands confirmed.
- ER-2020 PDF p.77: repeated part grid and printed analysis-total typo inspected.
- ER-2023 PDF p.91: financial comparison and source-year/rounding discrepancies inspected.
- ER-2024 PDF pp.94 and 102: Herzberg wording and solvency guidance inspected.

Images and contact sheets are under page-images/. This is model visual inspection of the selected pages, not human diagram approval or all-page review. Numeric recomputation is separately saved in numeric-verification.json.
''')
    print(json.dumps(summary,indent=2))
    print('TOP TOPICS',[(x['topic_id'],x['marks']) for x in sorted(totals,key=lambda x:-x['marks'])[:8]])
    print('COMMANDS',[(x['word'],x['substantive_task_count'],x['tariffs_seen']) for x in commands if x['substantive_task_count']])


if __name__=='__main__':main()
