"""6136 layout adapter: transcribe and verify the official syllabus without editing standard/.

The standard miner and verifier are Cambridge examples with fixed code/path registries.
This adapter preserves their provenance contract and adds Namibia's printed/PDF pages.
It is a Step 2 transcription check, never a substitute for the pilot publication checks.
"""
import hashlib
import json
import re
import subprocess
from pathlib import Path
from fractions import Fraction

WS=Path(__file__).resolve().parents[1]
REPO=WS.parents[1]
PDF=REPO/'Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_DevelopmentStudies_Syllabus.pdf'
OUT=WS/'curriculum'
OUT.mkdir(exist_ok=True)
PAGES=subprocess.check_output(['pdftotext','-layout',str(PDF),'-']).decode('utf-8').split('\f')
if not PAGES[-1].strip():PAGES.pop()
assert len(PAGES)==30
norm=lambda s:re.sub(r'\s+',' ',s).strip()
checks=[]
def cite(text, printed, section):
    assert norm(text) in norm(PAGES[printed+2]), (printed,text[:100])
    checks.append((printed,text))
    return {'page':printed,'pdf_page':printed+3,'section':section,'method':'transcribed from PDF layout text'}
def block(start,end,printed):
    s=PAGES[printed+2]
    return s[s.index(start):s.index(end)].strip()
def write(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

facts={'facts_id':'SYLFACTS-NAM-6136-NSSCO-2026','authority':'NIED 2017 NSSCO Development Studies syllabus, code 6136',
 'source_document':str(PDF.relative_to(REPO)),'source_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),
 'pages_in_document':len(PAGES),'route':'NSSCO, all three papers','intended_exam_year':2026,
 'generated_by':'planning/transcribe_syllabus.py','page_convention':'page is printed page; pdf_page is one-based PDF page',
 'rule':'Every transcription carries PDF provenance. Calculated aggregates are explicitly derived, never called printed weights.',
 'edition':{'publication_year':2017,'first_examination':2020,'valid_until':None,
 'verbatim':'FOR FIRST EXAMINATION IN 2020','source':{'page':None,'pdf_page':1,'section':'Cover'},
 'note':'No terminal examination year is stated. The 2026 year names our intended resource use, not a printed validity range.'}}

# AO names and all eleven sub-objectives are read from printed p.18.
ao_page=PAGES[20]
names=dict(re.findall(r'^([ABCD])\.\s+([^\n]+)',ao_page,re.M))
assert set(names)==set('ABCD')
sub=[]
matches=list(re.finditer(r'^([ABCD]\.\d)\s+(.+?)(?=\n[ABCD]\.|\n\s*\n|\Z)',ao_page,re.M|re.S))
for m in matches:
    raw=m.group().strip();sub.append({'code':m[1],'text':norm(m[2]),'verbatim':raw,'source':cite(raw,18,'6 Assessment objectives')})
assert len(sub)==11
facts['assessment_objectives']=[]
for code,name in names.items():
    raw=re.findall(r'^'+code+r'\.\s+[^\n]+',ao_page,re.M)[-1]
    facts['assessment_objectives'].append({'code':code,'name':name.strip(),
      'can_do':[s['text'] for s in sub if s['code'].startswith(code)],
      'sub_skills':[s for s in sub if s['code'].startswith(code)],'verbatim':raw,'source':cite(raw,18,'6 Assessment objectives')})

# The detailed grid uses marks in the Paper columns, and percentages only overall.
grid=PAGES[22];lines=grid.splitlines()
header=next(s for s in lines if 'Paper 1 Paper 2 Paper 3' in s)
cols=[header.index('Paper 1'),header.index('Paper 2'),header.index('Paper 3')]
boundaries=[('A.1/A.2','A.1 recall','A.3 show'),('A.3','A.3 show','A.4 demonstrate'),
 ('A.4','A.4 demonstrate','B. Analysis'),('B.1','B.1 interpret','B.2 analyse'),
 ('B.2','B.2 analyse','B.3 analyse'),('B.3','B.3 analyse','C. Investigation'),
 ('C','C. Investigation','D. Problem solving'),('D','D. Problem solving','Total')]
rows=[]
for code,start,end in boundaries:
    raw=block(start,end,20)
    # Keep the indentation from the original page when reading column positions.
    first=next(i for i,l in enumerate(lines) if start in l)
    last=next(i for i,l in enumerate(lines[first+1:],first+1) if end in l)
    value_line=next(l for l in lines[first:last] if re.search(r'\d+(?:\.\d+)?%',l))
    amounts=[]
    for a,z in zip(cols,cols[1:]+[90]):
        cell=value_line[a:z].strip()
        amounts.append(int(cell) if cell else 0)
    pct=float(re.search(r'(\d+(?:\.\d+)?)%',value_line)[1])
    rows.append({'code':code,'marks':dict(zip(['P1','P2','P3'],amounts)),
      'qualification_weight_percent_as_printed':pct,'verbatim':raw,'source':cite(raw,20,'8 Specification grid'),
      'blank_cell_policy':'Blank cells transcribed as zero; A.1 and A.2 share one allocation and cannot be separated.'})
assert [r['marks'] for r in rows]==[
 {'P1':20,'P2':15,'P3':0},{'P1':15,'P2':0,'P3':0},{'P1':20,'P2':0,'P3':0},
 {'P1':25,'P2':15,'P3':5},{'P1':0,'P2':25,'P3':5},{'P1':0,'P2':15,'P3':5},
 {'P1':0,'P2':0,'P3':25},{'P1':0,'P2':0,'P3':10}]
marks={a:{p:sum(r['marks'][p] for r in rows if r['code'].startswith(a)) for p in ['P1','P2','P3']} for a in 'ABCD'}
qual={a:sum(r['qualification_weight_percent_as_printed'] for r in rows if r['code'].startswith(a)) for a in 'ABCD'}
totals={p:sum(marks[a][p] for a in 'ABCD') for p in ['P1','P2','P3']}
assert totals=={'P1':80,'P2':70,'P3':50} and sum(qual.values())==100
split={p:{a:float(Fraction(100*marks[a][p],totals[p])) for a in 'ABCD'} for p in totals}
facts['ao_weights']={'grid_rows_as_printed':rows,'grid_marks':marks,'qualification_percent':qual,
 'per_component_percent':split,'by_route':None,
 'aggregate_provenance':'derived: sum the printed p.20 sub-objective rows by AO letter; per-paper percentages = AO marks / paper total × 100',
 'source':{'qualification':{'page':20,'pdf_page':23,'rows':[r['verbatim'] for r in rows]},
           'per_component':{'page':20,'pdf_page':23,'rows':[r['verbatim'] for r in rows]}},
 'individual_A1_A2_weights':'NOT STATED separately; only a combined A.1/A.2 allocation is printed.'}
for a in facts['assessment_objectives']:
    a['qualification_weight_percent']=qual[a['code']]
    a['weight_provenance']='derived from printed sub-objective allocations on p.20; see ao_weights.grid_rows_as_printed'

facts['papers']=[]
scheme=PAGES[21]
for n in [1,2,3]:
    raw=scheme[scheme.index('Paper '+str(n)):scheme.index('Paper '+str(n+1)) if n<3 else scheme.index('                                                19')].strip()
    top=raw.splitlines()[0]
    m=re.search(r'Paper\s+(\d)\s+(\d) hour(?:s)?(?:\s+(\d+) mins)?\s+(\d+) marks',top)
    assert m,top
    weightline=next(l for l in lines if re.match(r'\s*'+str(n)+r'\s+'+m[4]+r'\s+\d+%',l))
    weight=int(re.search(r'(\d+)%',weightline)[1])
    facts['papers'].append({'paper':str(n),'name':'Written','marks':int(m[4]),
     'duration_minutes':int(m[2])*60+int(m[3] or 0),'weight_percent':weight,
     'weight_provenance':'syllabus, transcribed from printed p.20 Weighting of paper table',
     'verbatim':raw,'source':cite(raw,19,'7 Scheme of assessment'),
     'weight_verbatim':weightline.strip(),'weight_source':cite(weightline.strip(),20,'8 Weighting of paper'),
     'ao_marks':{a:marks[a]['P'+str(n)] for a in 'ABCD'},'ao_split':split['P'+str(n)],
     'ao_split_provenance':'derived percentages from transcribed grid marks on p.20; not independently printed percentages'})

# Capture every glossary entry, including phrases and noun cues, without inventing words.
starts={24:['Annotate','Calculate','Compare','Complete','Contrast','Define or state the','Describe'],
25:['Devise or plan','Draw','Explain or','Factor','Feature','Giving your views','How','Identify','Illustrating your','Insert or label','List','Locate','Mark','Match','Measure','Name'],
26:['Pattern','Reasons','Refer to or With','State','Study','Suggest','Use or using the','With the help of','What','What differences','Where','Why']}
facts['command_words']=[]
for page,labels in starts.items():
    ls=PAGES[page+2].splitlines();cut=next(i for i,l in enumerate(ls) if l.strip()==str(page));ls=ls[:cut]
    positions=[next(i for i,l in enumerate(ls) if l==key or l.startswith(key+' ')) for key in labels]
    for k,(label,i) in enumerate(zip(labels,positions)):
        raw='\n'.join(ls[i:positions[k+1] if k+1<len(positions) else len(ls)]).strip()
        c=22 if page==24 else 21
        labelparts=[l[:c].strip() for l in raw.splitlines() if l[:c].strip()]
        meaning=norm(' '.join(l[c:].strip() for l in raw.splitlines() if l[c:].strip()))
        word=norm(' '.join(labelparts))
        facts['command_words'].append({'word':word,'meaning':meaning,'verbatim':raw,'source':cite(raw,page,'11 Glossary'),
          'use_in_prompts':None,'use_note':'Pending paper mining; inclusion in glossary alone does not authorise prompt use.'})
assert len(facts['command_words'])==35
facts['command_word_table']={'pages':[24,25,26],'pdf_pages':[27,28,29],'section':'11 Glossary','count':35,
 'note':'Preserves complete glossary, including noun cues and multi-line phrases. No Evaluate, Discuss or Differentiate entry is added from memory.'}
preamble=block('It is hoped that this glossary','Annotate',24)
facts['command_word_table']['preamble_verbatim']=preamble
facts['command_word_table']['preamble_source']=cite(preamble,24,'11 Glossary preamble')
facts['command_word_table']['layout_note']='The split Explain or / Account for/ versus Factor is a reading of the printed two-column layout. The slash and awkward What differences… label are source typography, not editorially settled command forms.'

# Whole subject: retain every objective and wrapped qualifier in its original column.
themes=[];topics={};current=None;source_bullet_count=0;pending_general=None
for page in range(5,18):
    pending_general=None
    ls=PAGES[page+2].splitlines()
    th=next((re.search(r'Theme\s+(\d+):\s*(.+)',l) for l in ls if re.search(r'Theme\s+\d+:',l)),None)
    if th:themes.append({'theme':th[1],'title':th[2].strip(),'verbatim':th[0],'source':cite(th[0],page,'5 Learning content')})
    header=next(l for l in ls if l.count('OBJECTIVES')>=2)
    leftcol=header.index('GENERAL OBJECTIVES');rightcol=header.rfind('SPECIFIC OBJECTIVES')
    if rightcol<0:rightcol=header.rfind('GENERAL OBJECTIVES')
    for line in ls:
        if re.fullmatch(r'\s*'+str(page)+r'\s*',line):break
        left=line[:leftcol].strip();right=line[rightcol:].rstrip()
        t=re.match(r'^(\d+\.\d+)\s+(.+)',left)
        if t:
            tid=t[1];current=topics.setdefault(tid,{'id':tid,'level':'topic','theme':tid.split('.')[0],'title_parts':[],
              'title_source_lines':[],'general_objectives':[],'specific_objectives':[],'source_pages':[]})
            pending_general=None
            if page not in current['source_pages']:current['source_pages'].append(page)
            if 'Continued' not in left and '…' not in left:
                current['title_parts'].append(t[2]);current['title_source_lines'].append({'verbatim':line,'source':cite(line,page,'5 Learning content')})
        elif current and left and line.startswith('    ') and not any(x in left for x in ['Theme','Topic','Learners','Continued','GENERAL']):
            if not left.isdigit():
                current['title_parts'].append(left);current['title_source_lines'].append({'verbatim':line,'source':cite(line,page,'5 Learning content')})
        if not current:continue
        general=line[leftcol:rightcol].rstrip()
        if '' in general:
            pending_general={'text_parts':[general.split('',1)[1].strip()],
              'source_lines':[{'verbatim':line,'source':cite(line,page,'5 General objectives')}],
              'column_start':leftcol,'column_end':rightcol}
            current['general_objectives'].append(pending_general)
        elif general.strip() and pending_general and not any(x in general for x in ['OBJECTIVES','Learners will']):
            pending_general['text_parts'].append(general.strip())
            pending_general['source_lines'].append({'verbatim':line,'source':cite(line,page,'5 General objectives')})
        if '' in right:
            source_bullet_count+=1
            text=right[right.index('')+1:].strip()
            obj={'text_parts':[text],'source_lines':[{'verbatim':line,'source':cite(line,page,'5 Specific objectives')}],
                 'page':page,'pdf_page':page+3,'column_start':rightcol}
            current['specific_objectives'].append(obj)
        elif right.strip() and current['specific_objectives'] and not any(x in right for x in ['OBJECTIVES','Learners should']):
            obj=current['specific_objectives'][-1]
            obj['text_parts'].append(right.strip());obj['source_lines'].append({'verbatim':line,'source':cite(line,page,'5 Specific objectives')})
for t in topics.values():
    t['title']=norm(' '.join(t.pop('title_parts')))
    for o in t['general_objectives']:
        o['text']=norm(' '.join(o.pop('text_parts')))
    for i,o in enumerate(t['specific_objectives'],1):
        o['source_bullet_id']=f'{t["id"]}-bullet-{i:02d}'
        parts=o.pop('text_parts');joined=''
        for part in parts:
            joined+=('' if joined.endswith('-') else ' ')+part
        o['text']=norm(joined)
assert len(themes)==10 and len(topics)==18,(len(themes),len(topics))
assert sum(len(t['specific_objectives']) for t in topics.values())==source_bullet_count==102
facts['content_themes']=themes;facts['content_outline']=list(topics.values())
facts['content_notes']=['Source bullet 3.1 enterprise wording starts on p.7 and is restated with examples on p.8. Retain the source bullets here; deduplicate by meaning only in the later objective registry.',
 'Theme 8 on printed p.14 misprints the third column as GENERAL OBJECTIVES. It contains the specific objectives, as shown by its position and Learners should be able to heading; the original source lines are preserved.']

facts['limits']=[]
for page,pattern,label,section in [(3,r'Learners beginning.*?previously in Junior Secondary \(JS\) level\.', 'prior learning, not a content exclusion','4 Additional information – Prior learning'),
 (23,r'It is important that learners are aware.*?3 examination\.', 'research is not assessed as coursework; Paper 3 questions remain','10 Explanatory notes – (ii) Individual research'),
 (26,r'to B\. Factual descriptions of A and B are not required\.', 'comparative-answer instruction, not a topic exclusion','11 Glossary')]:
    raw=re.search(pattern,PAGES[page+2],re.S).group()
    facts['limits'].append({'applies_to':label,'verbatim':raw,'source':cite(raw,page,section)})
facts['content_exclusions']={'explicit_topic_not_assessed_exclusions':[],
 'basis':'No explicit not-assessed/not-required content exclusions occur in printed content pp.5–17. Keep all ten themes; examples do not become exhaustive exclusions.'}
facts['paper3_sections']=[]
for label,pattern in [('A',r'Section A\n.*?marks\)\.'),('B',r'Section B\n.*?marks\)\.')]:
    raw=re.search(pattern,PAGES[24],re.S).group()
    facts['paper3_sections'].append({'section':label,'marks':int(re.search(r'\((\d+)\s+marks\)',raw)[1]),
      'verbatim':raw,'source':cite(raw,22,'10 Paper 3 notes for guidance')})
paper3_label=re.search(r'Paper 3 \(Alternative to coursework\)[^\n]+',PAGES[24]).group()
facts['papers'][2]['alternative_title']={'text':'Alternative to coursework','verbatim':paper3_label,'source':cite(paper3_label,22,'10 Explanatory notes to teachers')}
stages=block('1.    identify','Present an investigation report',22)
components=block('Present an investigation report','                                                22',22)
tasks=block('For example learners may be asked','(iii) Examples',23)
report_rule=block('Once learners are ready','At all',23)
facts['paper3_guidance']={
 'investigation_stages':{'verbatim':stages,'source':cite(stages,22,'10 Explanatory notes – (i) Research skills')},
 'report_components':{'verbatim':components,'source':cite(components,22,'10 Explanatory notes – (i) Research skills')},
 'section_b_example_tasks':{'verbatim':tasks,'source':cite(tasks,23,'10 Explanatory notes – (ii) Individual research'),
   'scope_note':'Examples, not an exhaustive list of permitted examination tasks.'},
 'individual_report_requirement':{'verbatim':report_rule,'source':cite(report_rule,23,'10 Explanatory notes – (ii) Individual research')},
 'note':'Use with the full content outline. Investigation, data limitations, justified method choices and evaluation remain in scope.'}
facts['edition']['implementation']={'year':2019,'verbatim':'FOR IMPLEMENTATION IN 2019','source':{'page':None,'pdf_page':1,'section':'Cover'}}
grades=next(l.strip() for l in PAGES[21].splitlines() if 'Grades available' in l)
facts['grades_available']={'text':grades.replace('Grades available','').strip(),'verbatim':grades,'source':cite(grades,19,'7 Scheme of assessment')}
hours=re.search(r'The NSSCO level syllabuses.*?but this is for guidance only\.',PAGES[5],re.S).group()
facts['guided_learning_hours']={'hours':130,'note':'Guidance only over two years','verbatim':hours,'source':cite(hours,3,'4 Additional information – Guided learning hours')}
for p in facts['papers']:
    p['assessment_objectives_as_printed']=p['weight_verbatim'].split()[-1].split(',')
facts['transcribed_notes']=[
 {'note':'The p.20 grid includes B in Paper 3 (15 marks). Teacher guidance p.22 says all questions test C and D; preserve both, use detailed grid for numerical allocation.',
  'verbatim':block('All the questions on this paper','In order to prepare',22),'source':cite(block('All the questions on this paper','In order to prepare',22),22,'10 Paper 3 notes')},
 {'note':'A.1 and A.2 have a combined weight. No separate sub-objective split is stated.', 'source':{'page':20,'pdf_page':23}},
 {'note':'Historical named examples in the syllabus (such as NDP5) are examples, not statements of current policy. Verify current factual claims separately during authoring.'},
 {'note':'The standard mine_syllabus.py/verify.py examples hardcode Cambridge codes and other installation paths. This local layout adapter does not alter standard files or replace any later pipeline publication check.'}]
write(OUT/'syllabus-facts.json',facts)
write(OUT/'syllabus-page-text.json',[{'pdf_page':i,'printed_page':i-3 if i>=4 else None,'text':s} for i,s in enumerate(PAGES,1)])
write(WS/'planning/syllabus-transcription-checks.json',{
 'result':'PASS','source_sha256':facts['source_sha256'],'verbatim_citations_checked':len(checks),
 'assessment_objectives':len(facts['assessment_objectives']),'sub_objectives':len(sub),'glossary_entries':35,
 'themes':10,'topics':18,'specific_objective_source_bullets':sum(len(t['specific_objectives']) for t in topics.values()),
 'grid_totals':totals,'qualification_aggregate_percent':qual,
 'checks':['Every cited quote found on the cited freshly extracted PDF page','All grid row values read from fixed paper columns and reconciled to paper totals','Grouped A.1/A.2 preserved','All 35 glossary blocks retained in source order','All content table specific-objective bullet markers retained','All 10 themes and 18 topics retained'],
 'not_checked':['Jeremy’s visual verification','Corpus demand and mark-scheme rules','Publication checks; not applicable at Step 2']})
print(json.dumps({'AOs':qual,'paper_AO_marks':marks,'topics':[(t['id'],t['title'],len(t['specific_objectives'])) for t in topics.values()],
 'glossary':[w['word'] for w in facts['command_words']],'citations_checked':len(checks)},ensure_ascii=False,indent=2))

brief=['# 6136 NSSCO Development Studies — syllabus brief\n\nNIED 2017, Grades 10–11, first examination 2020. Intended resource year: 2026; no expiry year is stated. Source: `Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_DevelopmentStudies_Syllabus.pdf`. References are printed pages [PDF pages].\n\n## Assessment objectives\n\nDefinitions: p.18 [PDF 21]. Allocations: p.20 [PDF 23]. Paper columns are **marks**. Individual A.1/A.2 weights are not stated.\n\n| AO | Name | P1 | P2 | P3 | Overall (derived sum) |\n|---|---|---:|---:|---:|---:|\n']
for a in facts['assessment_objectives']:
    code=a['code'];brief.append(f'| {code} | {a["name"]} | {marks[code]["P1"]} | {marks[code]["P2"]} | {marks[code]["P3"]} | {qual[code]:g}% |\n')
brief.append('\nPrinted grid, p.20 [PDF 23]:\n\n| Row | P1 | P2 | P3 | Overall (printed) |\n|---|---:|---:|---:|---:|\n')
for row in rows:
    m=row['marks'];brief.append(f'| {row["code"]} | {m["P1"]} | {m["P2"]} | {m["P3"]} | {row["qualification_weight_percent_as_printed"]:g}% |\n')
brief.append('\n## Papers\n\nStructure/durations: p.19 [PDF 22]; weights: p.20 [PDF 23]. All three papers are compulsory.\n\n| Paper | Duration | Marks | Weight | Structure |\n|---|---|---:|---:|---|\n')
structures={'1':'Four compulsory structured questions; 4 × 20 marks; stimulus material.',
 '2':'Two compulsory structured questions; 2 × 35 marks; related source material.',
 '3':'Two compulsory sections: supplied development-issue data and the learner’s own investigation.'}
for p in facts['papers']:
    h,m=divmod(p['duration_minutes'],60)
    brief.append(f'| {p["paper"]} | {h}h {m:02d}m | {p["marks"]} | {p["weight_percent"]}% | {structures[p["paper"]]} |\n')
brief.append('''
Paper 3 (Alternative to coursework): Section A uses supplied data (35 marks); Section B concerns the learner’s own investigation (15 marks), p.22 [PDF 25]. Learners investigate individually or in groups; each presents their own report. The investigation is not assessed as formal coursework, but Paper 3 questions concern it (p.23 [PDF 26]).

## Coverage and command glossary

All ten themes and 18 syllabus topics are transcribed, including Research skills. The 102 source bullets include enterprise wording repeated across pp.7–8; this count is not a count of unique assessable objectives. Specific-objective examples and qualifiers are preserved for later registry decomposition.

The full glossary contains 35 entries across pp.24–26 [PDF 27–29], including multiword instructions and noun cues such as Factor and Pattern. The source’s awkward “What differences…” label is retained verbatim. Evaluate, Discuss and Differentiate are not separate glossary entries; they do occur in the learning content. Whether any word may open a resource question remains pending actual paper mining.

## Limits and issues to carry forward

- No topic-specific “not assessed/not required” content exclusion was found in pp.5–17. Prior Development Studies study is not assumed (p.3 [PDF 6]). The glossary requires comparative statements, rather than separate descriptions, for its “What differences…” instruction (p.26).
- Paper 3’s detailed grid assigns B=15, C=25 and D=10 marks. Guidance on p.22 says all questions test C/D; preserve that wording but use the detailed p.20 grid for numerical allocation. Do not omit B.
- Historical examples such as NDP5 are syllabus examples, not verified current policy statements. Current claims will require verification during authoring.
- Sources were approved with missing standalone mark schemes, missing 2025 material and proof-version limitations. These do not establish marking rules.

Facts: `work/nam-6136-nssco-2026/curriculum/syllabus-facts.json`. Every extracted quote was checked against a fresh PDF extraction. The standard miner/verifier have Cambridge-only code/path registries; the subject layout adapter leaves standard files untouched and does not replace later pilot publication checks.

**Checkpoint: Jeremy verifies the AO and paper tables against pp.18–20 [PDF 21–23] before Step 3.**
''')
(REPO/'operations/analysis/6136-nssco-development-studies-syllabus-brief.md').write_text(''.join(brief))
