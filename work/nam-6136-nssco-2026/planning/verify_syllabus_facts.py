"""Reopen the 6136 PDF and check saved Step 2 facts, independently of the writer."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

ws=Path(__file__).resolve().parents[1];repo=ws.parents[1]
facts=json.loads((ws/'curriculum/syllabus-facts.json').read_text())
pdf=repo/facts['source_document']
pages=subprocess.check_output(['pdftotext','-layout',str(pdf),'-']).decode().split('\f')
norm=lambda x:re.sub(r'\s+',' ',x).strip()
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==facts['source_sha256']
count=0
def walk(obj):
    global count
    if isinstance(obj,dict):
        if 'verbatim' in obj and 'source' in obj:
            src=obj['source'];pg=src['pdf_page']
            assert norm(obj['verbatim']) in norm(pages[pg-1]),(pg,obj['verbatim'][:80])
            if src.get('page') is not None:assert src['page']+3==pg
            count+=1
        for v in obj.values():walk(v)
    elif isinstance(obj,list):
        for v in obj:walk(v)
walk(facts)
pre=facts['command_word_table']
assert norm(pre['preamble_verbatim']) in norm(pages[pre['preamble_source']['pdf_page']-1])
for ao in facts['assessment_objectives']:
    assert norm(re.sub(r'^[ABCD]\.\s*','',ao['verbatim']))==ao['name']
    for sub in ao['sub_skills']:
        assert norm(re.sub(r'^[ABCD]\.\d\s*','',sub['verbatim']))==sub['text']

# Independently scan the source grid's label stream and value-line columns.
# Do not trust saved row marks, paper AO sums, or the writer's hard-coded expected list.
gl=pages[22].splitlines()
heading=next(s for s in gl if all('Paper '+str(n) in s for n in (1,2,3)))
offsets=[heading.index('Paper '+str(n)) for n in (1,2,3)]
parsed={};active=None
for line in gl:
    if 'Weighting of paper' in line:break
    label=re.match(r'\s*((?:A|B)\.\d|C\. Investigation|D\. Problem solving)\b',line)
    if label:
        active=label[1]
        if active in ('A.1','A.2'):active='A.1/A.2'
        elif active.startswith('C.'):active='C'
        elif active.startswith('D.'):active='D'
    percent=re.search(r'(\d+(?:\.\d+)?)%',line)
    if percent and active:
        cells=[line[a:b].strip() for a,b in zip(offsets,offsets[1:]+[percent.start()])]
        parsed[active]={'marks':dict(zip(['P1','P2','P3'],[int(c) if c else 0 for c in cells])),
          'qualification_weight_percent_as_printed':float(percent[1])}
assert len(parsed)==8
for row in facts['ao_weights']['grid_rows_as_printed']:
    assert parsed[row['code']]['marks']==row['marks'],row['code']
    assert parsed[row['code']]['qualification_weight_percent_as_printed']==row['qualification_weight_percent_as_printed'],row['code']
for ao,perpaper in facts['ao_weights']['grid_marks'].items():
    for paper,value in perpaper.items():
        assert value==sum(v['marks'][paper] for code,v in parsed.items() if code.startswith(ao))
raw_mark_lines=[s.split() for s in pages[22].splitlines() if re.match(r'^\s*[123]\s+\d+\s+\d+%',s)]
assert len(raw_mark_lines)==3
for row,p in zip(raw_mark_lines,facts['papers']):
    assert [p['paper'],str(p['marks']),str(p['weight_percent'])+'%']==row[:3]
    assert sum(p['ao_marks'].values())==p['marks']
    assert abs(sum(p['ao_split'].values())-100)<1e-9
    duration=re.search(r'Paper\s+\d\s+(\d+)\s+hours?(?:\s+(\d+)\s+mins)?',p['verbatim'])
    assert p['duration_minutes']==int(duration[1])*60+int(duration[2] or 0)
    for ao,value in p['ao_marks'].items():
        assert value==facts['ao_weights']['grid_marks'][ao]['P'+p['paper']]
    assert p['assessment_objectives_as_printed']==row[-1].split(',')
for section in facts['paper3_sections']:
    assert section['marks']==int(re.search(r'\((\d+)\s+marks\)',section['verbatim'])[1])
assert sum(p['weight_percent'] for p in facts['papers'])==100
assert sum(p['marks'] for p in facts['papers'])==200
for a in 'ABCD':
    marks=sum(p['ao_marks'][a] for p in facts['papers'])
    assert marks/2==facts['ao_weights']['qualification_percent'][a]
assert len(facts['content_themes'])==10
assert len(facts['content_outline'])==18
assert len(facts['command_words'])==35
specific=[];bytopic={};titles={};active=None
for page in range(5,18):
    ls=pages[page+2].splitlines()
    header=next(s for s in ls if s.count('OBJECTIVES')>=2)
    col=header.rfind('SPECIFIC OBJECTIVES')
    if col<0:col=header.rfind('GENERAL OBJECTIVES')
    left=header.index('GENERAL OBJECTIVES')
    for s in ls:
        if s.strip()==str(page):break
        t=re.match(r'^\s*(\d+\.\d+)\s+(.+)',s[:left])
        if t:
            active=t[1];bytopic.setdefault(active,[]);titles.setdefault(active,[])
            if '…' not in t[2]:titles[active].append(t[2].strip())
        elif active:
            value=s[:left].strip()
            if value and s.startswith('    ') and not any(x in value for x in ['Theme','Topic','Learners','Continued','GENERAL']) and not value.isdigit():titles[active].append(value)
        if '' in s[col:]:
            specific.append(s);bytopic[active].append(s)
saved=[o for t in facts['content_outline'] for o in t['specific_objectives']]
assert len(specific)==len(saved)==102
for raw,o in zip(specific,saved):
    assert o['source_lines'][0]['verbatim']==raw
    col=o['column_start']
    segments=[s['verbatim'][col:].replace('','',1).strip() for s in o['source_lines']]
    joined=''
    for segment in segments:joined+=('' if joined.endswith('-') else ' ')+segment
    reconstructed=norm(joined)
    assert reconstructed==o['text'],o['source_bullet_id']
for topic in facts['content_outline']:
    tid=topic['id']
    assert topic['theme']==tid.split('.')[0]
    assert len(topic['specific_objectives'])==len(bytopic[tid])
    assert [o['source_lines'][0]['verbatim'] for o in topic['specific_objectives']]==bytopic[tid],tid
    assert topic['title']==norm(' '.join(titles[tid])),tid
    for obj in topic['general_objectives']:
        a,b=obj['column_start'],obj['column_end']
        assert obj['text']==norm(' '.join(s['verbatim'][a:b].replace('','',1).strip() for s in obj['source_lines']))
for command in facts['command_words']:
    assert command['use_in_prompts'] is None
result={'result':'PASS','source_sha256':facts['source_sha256'],'verbatim_objects_rechecked':count,
 'content_source_bullets_reconstructed':102,'topics':18,'themes':10,'glossary_entries':35,
 'paper_totals_and_weights':'PASS','ao_percentages_reconciled_to_marks':'PASS','source_grid_rows_reparsed':'PASS',
 'duration_and_section_marks_parsed_from_source':'PASS','AO_names_and_subskill_text_checked':'PASS','topic_titles_and_bullet_membership_checked':'PASS',
 'method_limit':'Writer and verifier both use pdftotext -layout; Claude Code separately inspected the rendered primary PDF in review session 30f1d695-1486-45e2-8438-d1b55290cd0c. Mechanical validation is not a second independent model review.',
 'scope':'Step 2 source/transcription verification; not a pipeline publication or teacher-review verdict'}
(ws/'planning/syllabus-facts-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
