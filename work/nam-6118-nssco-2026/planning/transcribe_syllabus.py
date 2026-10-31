"""Transcribe 6118 from its PDF with page/rectangle provenance.

Uses Poppler geometry to separate the three content columns and glossary rows.
Source wording and formula glyphs are retained; this is not an authoring registry.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from collections import Counter

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / 'work/nam-6118-nssco-2026'
PDF = ROOT / 'Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_Physics_syllabus.pdf'
NS = {'h': 'http://www.w3.org/1999/xhtml'}
BULLET = '\uf0b7'


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def load_pdf():
    xml = subprocess.check_output(['pdftotext', '-bbox-layout', str(PDF), '-'])
    elements = ET.fromstring(xml).findall('.//h:page', NS)
    words = []
    for p in elements:
        words.append([dict(text=''.join(w.itertext()),
                           x=float(w.attrib['xMin']), y=float(w.attrib['yMin']),
                           xmax=float(w.attrib['xMax']), ymax=float(w.attrib['yMax']))
                      for w in p.findall('.//h:word', NS)])
    layout = subprocess.check_output(['pdftotext', '-layout', str(PDF), '-'], text=True).split('\f')
    if not layout[-1].strip():
        layout.pop()
    assert len(layout) == len(words) == 52
    return words, layout


WORDS, LAYOUT = load_pdf()


def lines(words):
    groups = []
    for word in sorted(words, key=lambda w: (w['y'], w['x'])):
        if groups and abs(groups[-1][0]['y'] - word['y']) < 3.3:
            groups[-1].append(word)
        else:
            groups.append([word])
    return [dict(y=min(w['y'] for w in g),
                 text=' '.join(w['text'] for w in sorted(g, key=lambda w: w['x']))) for g in groups]


def region(page, x0, y0, x1, y1):
    selected = [w for w in WORDS[page-1] if x0 <= w['x'] < x1 and y0 <= w['y'] < y1]
    quote = '\n'.join(row['text'] for row in lines(selected))
    return dict(provenance='syllabus', pdf_page=page,
                printed_page=page-3 if page >= 4 else None,
                bbox=[x0, y0, x1, y1], verbatim=quote)


def fact(value, page, x0, y0, x1, y1):
    return dict(value=value, source=region(page, x0, y0, x1, y1))


def line_fact(value, page, needle):
    raw = next(line.strip() for line in LAYOUT[page-1].splitlines() if needle in line)
    assert str(value) in raw
    return dict(value=value, source=dict(provenance='syllabus',pdf_page=page,
                                         printed_page=page-3 if page>=4 else None,verbatim=raw))


def ao_definitions():
    names = {
        'A': 'Knowledge with understanding',
        'B': 'Handling information, application and solving problems',
        'C': 'Practical (experimental and investigative) skills and abilities',
    }
    out = []
    for code, name in names.items():
        page = 41 if code == 'C' else 40
        text = LAYOUT[page-1]
        stop = {'A': 'The Learning Content', 'B': 'These skills cannot', 'C': '7.    SCHEME'}[code]
        block = text[:text.index(stop)]
        if code == 'B':
            block = block[block.index('B1'):]
        elif code == 'A':
            block = block[block.index('A1'):]
        else:
            block = block[block.index('C1'):]
        parts = list(re.finditer(r'(?m)^\s*(' + code + r'\d)\s+', block))
        clauses = []
        for i, m in enumerate(parts):
            raw = block[m.start():parts[i+1].start() if i+1<len(parts) else len(block)].strip()
            clauses.append(dict(code=m[1], text=norm(raw)[3:].strip(),
                                source=dict(provenance='syllabus', pdf_page=page,
                                            printed_page=page-3, verbatim=raw)))
        lead = {
            'A': 'Learners should be able to demonstrate knowledge and understanding in relation to:',
            'B': 'Learners should be able to, in word or using other written forms of presentation (i.e. symbolic, graphical and numerical) to:',
            'C': 'Learners should be able to:',
        }[code]
        assert norm(lead) in norm(text)
        assert name in norm(LAYOUT[39])
        out.append(dict(code=code, name=name,
                        name_source=dict(provenance='syllabus',pdf_page=40,printed_page=37,verbatim=name),
                        lead_in=dict(text=lead,source=dict(provenance='syllabus',pdf_page=page,printed_page=page-3,verbatim=lead)),
                        statements=clauses))
    assert [len(r['statements']) for r in out] == [5,7,5]
    return out


def glossary():
    out = []
    for page in (44,45):
        words = WORDS[page-1]
        rows = lines([w for w in words if w['x'] < 190 and 70 <= w['y'] < 784])
        # Relate is above y=70 on page 45; retain it explicitly by coordinates.
        if page == 45:
            rows = lines([w for w in words if w['x'] < 190 and 60 <= w['y'] < 740])
        for i, row in enumerate(rows):
            if row['text'].startswith('NSSCO'):
                continue
            stop = rows[i+1]['y']-1 if i+1 < len(rows) else (785 if page==44 else 300)
            src = region(page, 200, row['y']-1, 560, stop)
            if not src['verbatim'].strip():
                continue
            out.append(dict(term=row['text'], definition=norm(src['verbatim']),
                            term_source=region(page,65,row['y']-1,195,row['y']+3), source=src))
    # Predict crosses the printed-page break. Attach its continuation before Relate.
    pred = next(r for r in out if r['term']=='Predict')
    continuation = region(45,200,50,560,66)
    pred['definition'] += ' ' + norm(continuation['verbatim'])
    pred['continuation_source'] = continuation
    assert len(out) == 30, [(x['term'],x['definition']) for x in out]
    assert [r['term'] for r in out[-7:]] == ['Predict','Relate','Recall and use','Select','Sketch','Study','Suggest']
    assert next(r for r in out if r['term']=='Outline')['definition'] == 'Give a brief answer writing down the main points'
    return out


def content():
    outline = []
    for page in (7,8):
        for line in LAYOUT[page-1].splitlines():
            m = re.match(r'^\s*(Topic\s+\d+:|\d+(?:\.\d+)+)\s+(.+)',line)
            if m:
                outline.append(dict(code=m[1].replace('Topic ','').rstrip(':'),title=m[2].strip(),
                                    source=dict(provenance='syllabus',pdf_page=page,printed_page=page-3,verbatim=line.strip())))
    rows, objectives, practicals = [], [], []
    current = None
    for page in range(9,40):
        words = WORDS[page-1]
        headers = [w for w in words if w['text']=='SPECIFIC' and w['y'] < 100]
        # Activities can occupy a whole page or follow the final table on page 39.
        activities = [l for l in lines(words) if l['text'].startswith('The practical activities')]
        practical_y = activities[0]['y'] if activities else 530
        if activities:
            bullets = sorted([w for w in words if w['text']==BULLET and w['x']<90 and w['y']>practical_y],key=lambda w:w['y'])
            for i,b in enumerate(bullets):
                end = bullets[i+1]['y']-0.01 if i+1<len(bullets) else 535
                src = region(page,70,b['y']-0.01,810,end)
                practicals.append(dict(topic_id=str(current).split('.')[0] if current else '2',
                                      text=norm(src['verbatim']),source=src))
        if not headers:
            continue
        split = headers[0]['x']
        general = next(w['x'] for w in words if w['text']=='GENERAL' and w['y']<100)
        left = lines([w for w in words if w['x']<general-1 and 100<w['y']<practical_y])
        headings = []
        for row in left:
            m = re.match(r'^(\d+(?:\.\d+)*\.?)\s+(.+)',row['text'])
            if m:
                headings.append((row,m))
        for i,(row,m) in enumerate(headings):
            end = headings[i+1][0]['y']-0.01 if i+1<len(headings) else practical_y
            src = region(page,50,row['y']-0.01,general-1,end)
            title = norm(src['verbatim'])[len(m[1]):].strip()
            rows.append(dict(code=m[1].rstrip('.'),title=title.split('(Note:')[0].strip(),source=src))
        bullets = sorted([w for w in words if w['text']==BULLET and abs(w['x']-split)<2 and 95<w['y']<practical_y],key=lambda w:w['y'])
        # This PDF raises fraction numerators 9.3288 pt (one at 9.3588 pt)
        # above their own bullet. Bind those to the following objective rather
        # than the preceding paragraph. Do not move earlier denominators or the
        # nuclide Z subscript (different measured offsets).
        starts=[]
        for b in bullets:
            raised=[w['y'] for w in words if w['x']>split+9 and 9.30<b['y']-w['y']<9.38]
            starts.append(min(raised)-0.01 if raised else b['y']-0.01)
        for i,b in enumerate(bullets):
            previous = [m[1].rstrip('.') for row,m in headings if row['y'] <= b['y']+4]
            if previous:
                current = previous[-1]
            assert current
            end = starts[i+1] if i+1<len(bullets) else practical_y
            src = region(page,split+9,starts[i],810,end)
            objectives.append(dict(subtopic_code=current,text=norm(src['verbatim']),source=src))
    # Practical sheets follow the corresponding topic; identify from their own introduction.
    for item in practicals:
        intro = LAYOUT[item['source']['pdf_page']-1]
        topic = re.search(r'required for Topic (\d)',intro)
        assert topic
        item['topic_id']=topic[1]
    codes = [r['code'] for r in rows]
    assert len(set(codes))==len(codes), [c for c,n in Counter(codes).items() if n>1]
    assert set(codes)=={r['code'] for r in outline}, (set(codes)-{r['code'] for r in outline},{r['code'] for r in outline}-set(codes))
    assert all(o['text'] for o in objectives)
    limits = []
    for obj in objectives:
        text = obj['text']
        if re.search(r'not required|no nuclide|only mentioned',text,re.I):
            limits.append(dict(kind='explicit_limit',**obj))
        elif re.search(r'qualitatively|simple |one dimension|constant |provided that|negligible|at a fixed|100% efficiency',text,re.I):
            limits.append(dict(kind='depth_or_condition',**obj))
    return outline,rows,objectives,practicals,limits


def main():
    aos=ao_definitions()
    commands=glossary()
    outline,rows,objectives,practicals,limits=content()
    percentages = {}
    grid = []
    for code,y0,y1 in [('A',298,350),('B',354,420),('C',426,490)]:
        value=region(42,200,y0,310,y1)
        percentage=int(re.search(r'(\d+)%',value['verbatim'])[1])
        percentages[code]=fact(percentage,42,200,y0,310,y1)
        marks={}
        for paper,x0,x1 in [('1',315,375),('2',395,453),('3',470,525)]:
            src=region(42,x0,y0,x1,y1)
            marks[paper]=dict(value=int(re.search(r'\d+',src['verbatim'])[0]),source=src)
        grid.append(dict(ao=code,marks_by_paper=marks))
    papers=[]
    for num,y0,y1 in [(1,277,355),(2,372,420),(3,429,540)]:
        duration=region(41,405,y0,475,y1)
        ds=norm(duration['verbatim'])
        name=region(41,70,y0,170,y1)
        marks=region(41,480,y0,510,y1)
        weight=region(42,390,139+(num-1)*12.65,420,150+(num-1)*12.65)
        papers.append(dict(paper=str(num),name=norm(name['verbatim']),name_source=name,
                           description=region(41,173,y0,403,y1),
                           duration=dict(value=ds,source=duration),
                           marks=dict(value=int(marks['verbatim']),source=marks),
                           qualification_weight_percent=dict(value=int(weight['verbatim'].strip('%')),source=weight)))
    assert [p['marks']['value'] for p in papers]==[40,80,40]
    assert [p['duration']['value'] for p in papers]==['45 minutes','1 hour 30 minutes','1 hour 15 minutes']
    assert [p['qualification_weight_percent']['value'] for p in papers]==[30,50,20]
    raw={r['ao']:sum(m['value'] for m in r['marks_by_paper'].values())/160*100 for r in grid}
    final={r['ao']:sum(r['marks_by_paper'][p['paper']]['value']/p['marks']['value']*p['qualification_weight_percent']['value'] for p in papers) for r in grid}
    data=dict(syllabus_code='6118',subject='Physics',board='Namibia',level='NSSCO',
              source_pdf=str(PDF.relative_to(ROOT)),source_sha256=hashlib.sha256(PDF.read_bytes()).hexdigest(),
              transcription_date='2026-10-30',page_number_convention='one-based PDF viewer pages; printed page = PDF page - 3 after front matter',
              source_text_policy='Source wording retained, whitespace normalised in text fields. Verbatim fields preserve extracted region lines. Mathematical glyph placement is not a typeset formula representation; inspect cited PDF when interpreting fractions or superscripts.',
              identity=dict(code=line_fact('6118',1,'SYLLABUS CODE:'),
                            edition=line_fact(2018,2,'Publication date:'),
                            implementation_year=line_fact(2019,1,'FOR IMPLEMENTATION'),
                            first_examination_year=line_fact(2020,1,'FOR FIRST EXAMINATION')),
              assessment_objectives=aos,ao_weights_specification_grid_percent=percentages,
              component_ao_marks=grid,papers=papers,
              compulsory_papers=fact(['1','2','3'],41,70,215,530,235),
              grid_qualifier=region(42,70,217,540,246),
              stated_skills_knowledge_balance=dict(
                  provenance='syllabus',skills_percent=53,knowledge_understanding_percent=47,
                  source=region(42,70,558,540,620),
                  note='Stated syllabus balance; retained separately from derived final-grade AO weights. Not a card quota.'),
              recall_limit=dict(source=region(42,200,310,310,350),stated_percent=24,denominator='not stated; unresolved',provenance='syllabus'),
              derived_reconciliation=dict(provenance='judgement',method='Arithmetic from the cited paper marks, AO grid and qualification paper weights; not a transcription or card quota.',raw_mark_percent=raw,final_grade_percent=final),
              command_words=commands,
              command_word_policy='This is the complete syllabus glossary, including joint labels; prompt eligibility is not yet assessed and must come from the Step 3 corpus.',
              content_outline=outline,content_table_rows=rows,specific_objectives=objectives,
              required_practicals=practicals,scope_limits_and_conditions=limits,
              assessment_annexes=[dict(title='Practical assessment and Paper 3',source=region(46,65,45,540,790)),
                                  dict(title='Teaching practical skills and apparatus',source=region(47,65,45,540,740)),
                                  dict(title='Units of common physical quantities',source=region(49,55,40,550,790)),
                                  dict(title='Electrical symbols',source=region(50,55,40,550,790))],
              open_issues=[dict(issue='Paper 1 duration conflict',syllabus_pdf_page=41,
                                syllabus_minutes=45,observed_paper_minutes={'2020':45,'2021':60,'2022':45,'2023':45,'2024':45,'2025':60},
                                evidence_file='curriculum/source-inventory.json',status='Explicitly waived by Lotto on 2026-10-31 as non-major/non-blocking; discrepancy retained and no governing 2026 duration inferred'),
                           dict(issue='Recall ceiling denominator',status='unresolved; the syllabus does not state whether 24% is of all assessment or AO A'),
                           dict(issue='Governing syllabus for the cohort',status='Operator approved the documented 2018 edition as the working source on 2026-10-31. No independent NIED confirmation of 2026 applicability established; external-authority caveat retained, not a progression gate.',evidence_file='curriculum/syllabus-currency.json')])
    data['source_layout_notes'] = [
        dict(provenance='judgement',pdf_page=37,printed_page=34,
             note='The penultimate voltage-measurement entries are malformed in the PDF itself: the bullet beginning potential difference across the whole circuit interrupts the preceding sentence before individual components in a circuit. Raw bullets retained; plan must cover component and whole-circuit potential difference without treating this as a clean pair of authored tasks.'),
        dict(provenance='judgement',note='The three scope limits are local to their cited subtopics. In particular no nuclide formulas in 2.10.1 must not exclude the nuclide equations explicitly required in 6.1.1 and 6.2.4.'),
    ]
    dest=WORK/'curriculum/syllabus-facts.json'
    dest.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    counts=dict(topics=sum('.' not in r['code'] for r in rows),content_rows=len(rows),
                specific_objective_bullets=len(objectives),glossary_rows=len(commands),
                required_practical_bullets=len(practicals),
                explicit_limits=sum(r['kind']=='explicit_limit' for r in limits),
                depth_or_condition_entries=sum(r['kind']=='depth_or_condition' for r in limits),
                objectives_by_topic=dict(Counter(o['subtopic_code'].split('.')[0] for o in objectives)))
    (WORK/'planning/syllabus-transcription-counts.json').write_text(json.dumps(counts,indent=2)+'\n')
    print(json.dumps(counts,indent=2))


if __name__=='__main__':
    main()
