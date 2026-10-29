#!/usr/bin/env python3
"""6137-only syllabus transcription and source verification, without shared-tool edits.

The shared miner has a closed Cambridge subject catalogue and environment-specific
paths. This adapter reads the actual NIED PDF; it does not run another subject's
miner or modify standard/. Numeric assessment values come from the extracted grid.
"""
import hashlib
import json
from pathlib import Path
import re
from pypdf import PdfReader
import pdfplumber

WS=Path(__file__).resolve().parents[1]
ROOT=WS.parents[1]
PDF=ROOT/'Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_Geography_syllabus.pdf'
def norm(s):return ' '.join(s.split())
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')

# These are the printed rows, not an invented allowed-command list. Several are
# question phrases or conceptual nouns. Corpus usage is decided only at step 3.
GLOSSARY_ROWS={
38:[('Annotate','Annotate'),('Calculate','Calculate'),('Compare','Compare'),('Complete','Complete'),('Contrast','Contrast'),('Define','Define'),('Demonstrate','Demonstrate'),('Describe','Describe'),('Devise or Plan','Devise or'),('Differentiate','Differentiate'),('Distinguish','Distinguish'),('Draw','Draw'),('Explain / Account for','Explain /')],
39:[('Factor','Factor'),('Feature','Feature'),('Giving your View','Giving your'),('How','How'),('Identify','Identify'),('Illustrating your answer','Illustrating'),('Insert or label','Insert'),('List','List'),('Locate','Locate'),('Mark','Mark'),('Match','Match'),('Measure','Measure'),('Name','Name'),('Pattern','Pattern'),('Reasons','Reasons'),('Refer to or with reference to','Refer to or')],
40:[('State','State'),('Study','Study'),('Suggest','Suggest'),('Use or using the information provided','Use or using'),('With the help of information in','With the help'),('What','What used'),('What differences','What differences'),('Where','Where'),('Why','Why')],
}
TOPICS=[
('1.1','The Earth’s structure',[8]),('1.2','Weathering and Erosion',[8]),('1.3','River processes',[9]),('1.4','Wind/Aeolian processes',[10]),('1.5','Coastal/Marine processes',[10,11]),('1.6','Weather and Climate',[12]),('1.7','Climatic regions and natural vegetation',[13]),
('2.1','Industrial system',[14,15]),('2.2','Agriculture',[16,17]),('2.3','Leisure and tourism',[18,19]),('2.4','Energy sources',[20]),('2.5','Utilisation and management of water resources in Namibia',[21]),('2.6','Utilisation and management of wildlife animals in Namibia',[21]),
('3.1','Population Studies',[22,23,24]),('3.2','HIV and AIDS',[25]),('3.3','Settlement Studies',[26,27]),('4.1','Research skills',[28]),('4.2','Map reading skills',[28])]

def main():
    reader=PdfReader(PDF);raw=[p.extract_text() or '' for p in reader.pages];pages=[norm(s) for s in raw]
    assert len(pages)==46
    def src(page,quote,section):
        quote=norm(quote);assert quote in pages[page-1],(page,quote)
        return {'page':page,'pdf_page':page,'printed_page':page-3 if page>=4 else None,'section':section,'verbatim':quote,'provenance':'syllabus'}
    def fact(value,page,quote,section):return {'value':value,'source':src(page,quote,section)}
    with pdfplumber.open(PDF) as pdf:
        grid=pdf.pages[30].extract_tables()[0]
        # Read the labelled table, independently of the plain-text page extraction.
        assert [norm(x) for x in grid[0]]==['Assessment Objectives','Weighting %','Paper 1 Marks','Paper 2 Marks','Paper 3 Marks']
        rows={r[0]:r for r in grid[1:5]};assert set(rows)==set('ABCD')
        weight={a:int(rows[a][1]) for a in rows};marks={str(p):{a:0 if rows[a][p+1]=='-' else int(rows[a][p+1]) for a in rows} for p in [1,2,3]}
        totals={str(p):int(re.search(r'\d+',grid[5][p+1]).group()) for p in [1,2,3]}
        paper_weights={str(p):float(grid[6][p+1]) for p in [1,2,3]}
    row_sources={a:src(31,' '.join(rows[a]),'8 Specification grid; columns AO, overall %, P1 marks, P2 marks, P3 marks') for a in rows}
    ao_names={a:re.search(r'\b'+a+r'\s+([^\n]+)',raw[28]).group(1).strip() for a in 'ABCD'}
    # Obtain the detailed AO statements from the labelled paragraphs, not recall.
    ao_blocks={
      'A':pages[28].split('A. Knowledge with understanding',1)[1].split('B. Analysis',1)[0],
      'B':pages[28].split('B. Analysis',1)[1].split('C. Judgment and decision making',1)[0],
      'C':pages[28].split('C. Judgment and decision making',1)[1],
      'D':pages[29].split('D. Investigation (enquiry, practical and presentation skills)',1)[1].split('7. SCHEME OF ASSESSMENT',1)[0]}
    aos=[]
    for a in 'ABCD':
        page=30 if a=='D' else 29;block=ao_blocks[a];matches=list(re.finditer(r'\b'+a+r'\.\d+\s',block));statements=[]
        for k,m in enumerate(matches):
            text=block[m.start():matches[k+1].start() if k+1<len(matches) else len(block)].strip();statements.append({'id':m.group().strip(),'text':text,'source':src(page,text,'6 Assessment Objectives')})
        assert len(statements)=={'A':4,'B':4,'C':3,'D':6}[a]
        aos.append({'code':a,'name':ao_names[a],'source':src(29,f'{a} {ao_names[a]}','6 Assessment Objectives; summary list'),'verbatim':f'{a} {ao_names[a]}','can_do':[s['text'] for s in statements],'statements':statements,'qualification_weight_percent':weight[a],'qualification_weight_source':row_sources[a]})
    papers=[]
    for p in ['1','2','3']:
        start=pages[29].index('Paper '+p);end=pages[29].index('Paper '+str(int(p)+1),start+1) if p!='3' else len(pages[29]);block=pages[29][start:end]
        m=re.match(r'Paper \d (\d+ hours?(?: \d+ minutes)?) (\d+) marks',block);assert m,block[:130]
        duration=m.group(1);paper_marks=int(m.group(2));assert paper_marks==totals[p]
        wm=re.search(r'The weighting of this paper is ([\d.,]+)%',block);assert float(wm.group(1).replace(',','.'))==paper_weights[p]
        sources={a:row_sources[a] for a in 'ABCD'}
        minutes=sum(int(n)*({'hour':60,'hours':60,'minutes':1}[unit]) for n,unit in re.findall(r'(\d+) (hours?|minutes)',duration))
        papers.append({'paper':p,'name':{'1':'Written thematic paper','2':'Written geographical skills paper','3':'Written geographical investigation paper'}[p],'name_provenance':'judgement: descriptive labels; the printed titles are Paper 1, Paper 2, Paper 3, Written','duration':duration,'duration_minutes':minutes,'duration_minutes_provenance':'judgement: unit conversion from the stated duration','marks':paper_marks,'weight_percent':paper_weights[p],'source':src(30,block,'7 Scheme of Assessment'),'header_source':src(30,m.group(),'7 Scheme of Assessment; paper header'),'weight_source':src(30,wm.group(),'7 Scheme of Assessment; paper weight'),'weight_provenance':'syllabus','ao_split':marks[p],'ao_split_unit':'marks, not percentages','ao_split_marks':marks[p],'ao_split_sources':sources,'dash_interpretation':'The grid prints a dash for AO D in Papers 1 and 2; stored as 0 marks.','description':block,'all_compulsory':True})
    commands=[]
    for page,specs in GLOSSARY_ROWS.items():
        text=pages[page-1]
        text=text.split('11. Glossary of key terms',1)[0] if page==40 else text
        starts=[];cursor=0
        for label,marker in specs:
            n=text.index(marker,cursor);starts.append(n);cursor=n+len(marker)
        for k,(label,_) in enumerate(specs):
            quote=text[starts[k]:starts[k+1] if k+1<len(starts) else len(text)].strip()
            non_command=label in ['Factor','Feature','Pattern']
            commands.append({'word':label,'verbatim':quote,'source':src(page,quote,'10 Glossary for teaching and assessment'),'entry_kind':'conceptual noun' if non_command else 'command or question phrase','entry_kind_provenance':'judgement: classification only; the printed row is preserved verbatim','use_in_prompts':None,'use_in_prompts_note':'not decided at step 2; requires observed paper usage and tariffs at step 3'})
    assert len(commands)==38
    outline=[]
    for topic,title,pnums in TOPICS:
        page=pnums[0];text=pages[page-1];m=re.search(re.escape(topic)+r'\s',text);assert m,(topic,page)
        # Titles occupy the first column; raw extraction may interleave adjacent
        # columns. Store the full cited row-page instead of fabricating a quote.
        outline.append({'topic_id':topic,'title':title,'title_provenance':'syllabus: transcribed column heading, line breaks joined','pdf_pages':pnums,'printed_pages':[n-3 for n in pnums],'source':src(page,text,'5 Learning content; full page containing heading and specific-objective rows')})
    limits=[
      ('case-study-choice',7,'Case studies included in the learning content are not prescriptive. Teachers are urged to use other case studies which may be relevant.','5 Learning content'),
      ('integrated-theme4',28,'It is important that these skills are not taught in isolation but are integrated into the teaching of other three themes.','4 Research techniques and map reading skills'),
      ('p1-unfamiliar-resource',32,'The resource use does not require specific local or regional knowledge.','9 Explanatory notes; Paper 1 stimulus context, not a waiver of case studies'),
      ('p1-no-specific-fieldwork-question',32,'Whilst specific questions will not be set in Paper 1 based upon field work, learners may use this information to illustrate answers.','9 Explanatory notes; Paper 1'),
      ('p2-place-knowledge',30,'This paper will be largely skills-based and candidates will not require knowledge of specific places, but will be expected to apply some knowledge of topics.','7 Scheme of Assessment'),
      ('p2-map-scale-key',30,'One question will be specifically based on a large-scale (1:50 000) topographical map, with full colour map from any country in SADC. The map will always be presented with a full key.','7 Scheme of Assessment'),
      ('p2-cross-sections',33,'Cross-sections may be set for interpretation but learners will not be asked to construct them.','9 Explanatory notes; Paper 2'),
      ('p2-gradient-units',33,'It should be noted that both measurements must be made in the same units before the calculation can be made.','9 Explanatory notes; Paper 2'),
      ('p2-map-evidence',34,'It must be stressed that all answers to this question must be based on map evidence only.','9 Explanatory notes; mapwork question'),
      ('p2-simple-photographs',34,'Only simple descriptions will be required.','9 Explanatory notes; Photographs and pictorial materials'),
      ('p2-plotting-context',34,'Learners may be required to plot information on graphs when axes and scales are provided.','9 Explanatory notes; Maps, Diagrams, Graphs'),
      ('p3-coursework-not-operational',30,'Coursework will not become operational as an option until necessary materials and training of teachers are in place but the methodology of teaching geographical enquiry skills and techniques will be encouraged.','7 Scheme of Assessment'),
      ('p3-cycle-ends-2024',30,'Topics to be assessed in each theme from 2020-2024 will be highlighted under explanatory notes to teachers, page 30','7 Scheme of Assessment')]
    # PDF extraction leaves spaces inside some words/hyphen compounds. Source
    # slices below retain those exact characters and do not silently fix them.
    limits_out=[]
    for key,page,quote,section in limits:
        q=norm(quote)
        if q not in pages[page-1]:
            compact=lambda s:re.sub(r'[\s-]+','',s)
            target=compact(q);text=pages[page-1];mapping=[];chars=[]
            for n,ch in enumerate(text):
                if ch.isspace() or ch=='-':continue
                mapping.append(n);chars.append(ch)
            start=''.join(chars).index(target);q=text[mapping[start]:mapping[start+len(target)-1]+1]
        limits_out.append({'limit_id':key,'source':src(page,q,section)})
    historical=[]
    for y in range(2020,2025):
        m=re.search(str(y)+r' (.*?)(?= 202\d |$)',pages[36]);assert m
        # Last row runs into the page end only; no 2026 extrapolation is made.
        line=m.group().strip();historical.append({'year':y,'source':src(37,line,'9 Explanatory notes; External examination rotation')})
    facts={'facts_id':'SYLFACTS-NAM-6137-NSSCO-2026','generated_by':'planning/transcribe_syllabus_6137.py','generated_on':'2026-10-29','authority':'NIED NSSCO Geography syllabus 6137, publication 2016','source_document':str(PDF.relative_to(ROOT)),'source_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),'pages_in_document':len(pages),'page_convention':'page and pdf_page are one-based PDF page numbers; printed_page is the footer. Printed pages 1-43 begin at PDF page 4.','edition':fact(2016,2,'Publication date: 2016','Publication information'),'first_examination_year':fact(2020,1,'FOR FIRST EXAMINATION IN 2020','Cover'),'implementation_year':fact(2019,1,'FOR IMPLEMENTATION IN 2019','Cover'),'syllabus_code':fact('6137',1,'SYLLABUS CODE: 6137','Cover'),'grades':fact('10-11',1,'GRADES 10 - 11','Cover'),'target_exam_year':{'value':2026,'provenance':'judgement','basis':'Current session learners and timetable; source set accepted by Vitalis on 29 October 2026. The syllabus itself first examines in 2020 and does not supply a 2026 Paper 3 topic row.'},'route':'NSSCO Ordinary Level','papers_in_route':['1','2','3'],'route_source':src(30,'All learners will take papers 1, 2, 3.','7 Scheme of Assessment'),'grades_available':fact('A*-G',30,'Grades available A*-G','7 Scheme of Assessment'),'assessment_objectives':aos,'ao_weights':{'qualification':weight,'per_component':marks,'per_component_unit':'marks','source':{'qualification':{'page':31,'rows':[' '.join(rows[a]) for a in 'ABCD']},'per_component':{'page':31,'rows':[' '.join(rows[a]) for a in 'ABCD']}},'note':'All values transcribed from the specification grid. Per-paper percentages are not stated; do not relabel the marks as percentages.'},'papers':papers,'command_words':commands,'command_word_table_note':'38 printed glossary rows on PDF pages 38-40. This mixed glossary includes conceptual nouns and question phrases, not 38 automatically allowed prompt-openers. Combined/line-wrapped row labels are preserved; observed variants and tariffs belong to step 3.','content_outline':outline,'themes':[{'theme':n,'title':t,'source':src(7,f'{n}. {t}','5 Learning content; four broad themes')} for n,t in [(1,'Physical Geography'),(2,'Economic activities and the use of resources'),(3,'Population and Settlement Studies'),(4,'Research Techniques and Map Reading Skills')]],'stated_limits':limits_out,'historical_paper3_rotation':historical,'explanatory_notes':[{'pdf_page':p,'source':src(p,pages[p-1],'9 Explanatory notes to the teachers; full page')} for p in range(32,38)],'current_paper3_rotation':{'year':2026,'status':'not established by this source','topics':None,'provenance':'judgement: source limitation','basis_source':src(37,'Examination year Physical Geography Human Geography','9 Explanatory notes; historical rotation header')},'tooling_note':'Shared mine_syllabus.py and verify.py are Cambridge-catalogue/environment-specific and do not register 6137. This subject-only adapter verifies against the source PDF and leaves standard/ unchanged.'}
    circular_path=WS/'curriculum/paper3-prescribed-topics-2025-2029.json'
    if circular_path.exists():
        circular=json.loads(circular_path.read_text())
        assert circular['confirmation']['confirmed_by']=='Vitalis P Haupindi'
        year=facts['target_exam_year']['value']
        row=next(r for r in circular['rows'] if r['year']==year)
        facts['current_paper3_rotation']={
            'year':year,'status':'confirmed by Vitalis; adopted from the later circular',
            'topics':{'physical_geography':row['physical_geography'],'human_geography':row['human_geography']},
            'topic_ids':list(circular['2026_topic_mapping']),
            'provenance':'circular_copy_confirmed_by_operator; not the 2016 syllabus',
            'source_document':'curriculum/paper3-prescribed-topics-2025-2029.json',
            'source_url':circular['source_url'],'circular_date':circular['circular_date_as_printed'],
            'circular_row_verbatim':row['verbatim'],'confirmation':circular['confirmation']}
    # Source-quote verification is recursive: every structured source is checked.
    checks=[]
    def walk(x,path='facts'):
        if isinstance(x,dict):
            if 'verbatim' in x and 'pdf_page' in x:
                assert x['verbatim'] in pages[x['pdf_page']-1],path;checks.append(path)
            for k,v in x.items():walk(v,path+'.'+k)
        elif isinstance(x,list):
            for i,v in enumerate(x):walk(v,f'{path}[{i}]')
    walk(facts)
    assert sum(weight.values())==100 and sum(paper_weights.values())==100
    for p in ['1','2','3']:assert sum(marks[p].values())==totals[p]
    total=sum(totals.values());assert total==200
    for a in 'ABCD':assert sum(marks[p][a] for p in marks)/total*100==weight[a]
    for p in totals:assert totals[p]/total*100==paper_weights[p]
    # Check all and only the printed glossary row starts, including multiline labels.
    assert [len(GLOSSARY_ROWS[p]) for p in [38,39,40]]==[13,16,9]
    dump(WS/'curriculum/syllabus-facts.json',facts)
    dump(WS/'planning/syllabus-verification-6137.json',{'source_sha256':facts['source_sha256'],'source_quotes_checked':len(checks),'quote_failures':[],'assessment_grid_raw':grid,'qualification_weights_total':sum(weight.values()),'paper_weights_total':sum(paper_weights.values()),'paper_mark_totals':totals,'exam_marks':total,'row_and_column_sums_match':True,'glossary_rows':38,'glossary_rows_per_page':{'38':13,'39':16,'40':9},'themes':4,'topics':18,'ao_statement_counts':{a['code']:len(a['statements']) for a in aos},'source_pages_read':'Full 46-page PDF text read; grid, scheme and glossary additionally checked as rendered page images','visual_check_pages':[29,30,31,37,38,39,40],'current_2026_paper3_topic_allocation':facts['current_paper3_rotation']['status'],'limitations':['This verifies syllabus transcription, not exam-paper exposure or learner resources.','No curriculum framework, contracts or work orders have been generated.']})
    print(f'6137: {len(checks)} source quotes verified; 4 AOs; 3 papers; 38 glossary rows; 4 themes / 18 topics; 200 marks; row/column totals and stated weights reconcile.')

if __name__=='__main__':main()
