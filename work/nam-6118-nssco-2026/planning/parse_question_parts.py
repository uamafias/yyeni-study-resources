"""Draft internal question-part segmentation. Semantic review is separate."""
from pathlib import Path
import collections
import json
import re

WORK=Path(__file__).resolve().parents[1]
ROOT=WORK.parent.parent
COMMANDS=re.compile(r'\b(calculate|determine|state|define|describe|explain|draw|sketch|complete|plot|suggest|predict|name|identify|distinguish|interpret|give|write|show|derive|compare|estimate|measure|label|record|design|deduce|find|mark|indicate|use|list|select|construct|discuss|evaluate|justify|account)\b',re.I)


def clean(line):
    line=line.replace('\u2002',' ').replace('\u2009',' ').replace('\u2003',' ')
    if re.match(r'\s*(?:6118/\d/\d+|©|\[Turn over|For\s*$|Examiner[’\x27]s\s*$|Use\s*$)',line):return ''
    if re.match(r'^\s*\d{5,}\s*$',line):return ''
    return line


def main():
    records=[];summaries=[]
    manifest=json.loads((WORK/'assessment-evidence/extraction-manifest.json').read_text())
    for source in manifest['records']:
        if source['kind']!='question_paper' or source['paper']==1:continue
        text=(WORK/source['outputs']['layout']['path']).read_text()
        page=1;question=None;letter=None;roman=None;segment=[];locators=[];parts=[]
        for raw in text.splitlines():
            p=re.match(r'=== SOURCE PDF PAGE (\d+) ===',raw)
            if p:page=int(p[1]);continue
            if page==1:continue
            line=clean(raw)
            # Top-level question labels begin at the left margin; figures/table
            # data are indented. Ignore numbered units/symbol lists.
            q=re.match(r'^\s{0,5}(\d{1,2})\s*(\([a-h]\).*|[A-Za-z].*)',line)
            if q and int(q[1])<=15 and not q[2].startswith(('For','Examiner','Use')):
                question=int(q[1]);letter=None;roman=None
            # Only a leading label changes the part reference. Inline cross-
            # references and labels inside a data table do not rename the task.
            labels=re.match(r'^\s{0,17}(?:\d{1,2}\s*)?(?:\(([a-h])\)\s*)?(?:\((i{1,3}|iv|v|vi|vii|viii|ix|x)\))?',line)
            if labels and labels[1]:letter=labels[1];roman=None
            if labels and labels[2]:roman=labels[2]
            if line.strip():segment.append(line);locators.append(page)
            tariffs=list(re.finditer(r'\[(\d{1,2})\]',line))
            for tariff in tariffs:
                candidate='\n'.join(segment)
                meaningful=re.sub(r'\[\d+\]','',candidate)
                meaningful=re.sub(r'[.\s_\d=+−–/×():,;°%\-]+',' ',meaningful)
                # Empty segment between a part mark and a question total.
                if len(re.findall(r'[A-Za-z]{3,}',meaningful))<1:
                    segment=[];locators=[];continue
                if question is None:
                    raise ValueError((source['source_id'],page,candidate))
                ref=str(question)+(f'({letter})' if letter else '')+(f'({roman})' if roman else '')
                commands=[m[1].lower() for m in COMMANDS.finditer(candidate)]
                record=dict(evidence_id=f"6118-{source['year']}-P{source['paper']}-{len(parts)+1:03d}",
                            source_id=source['source_id'],year=source['year'],paper_id=str(source['paper']),
                            question_ref=ref,mark_tariff=int(tariff[1]),
                            source_locator={'path':source['path'],'pdf_pages':sorted(set(locators))},
                            internal_source_text=candidate,command_candidates=commands,
                            semantic_review_status='pending',objective_ids=[],ao_focus=[],
                            creditworthy_points=[],examiner_findings=[],common_errors=[])
                parts.append(record);segment=[];locators=[]
        expected=80 if source['paper']==2 else 40
        total=sum(r['mark_tariff'] for r in parts)
        summaries.append({'year':source['year'],'paper':source['paper'],'parts':len(parts),
                          'parsed_marks':total,'cover_marks':expected,'difference':total-expected})
        records.extend(parts)
    dest=WORK/'assessment-evidence/question-parts-draft.json'
    dest.write_text(json.dumps({'status':'DRAFT segmentation; no semantic mapping or command eligibility accepted yet',
                                'summaries':summaries,'records':records},indent=2,ensure_ascii=False)+'\n')
    for r in summaries:print(r)


if __name__=='__main__':main()
