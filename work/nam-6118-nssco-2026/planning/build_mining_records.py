"""Assemble manually reviewed demand mappings; never infer them from tokens."""
from pathlib import Path
import collections,json,re

ROOT=Path(__file__).resolve().parents[3];WORK=ROOT/'work/nam-6118-nssco-2026'


def main():
    index=json.loads((WORK/'curriculum/source-objective-index.json').read_text())
    known={r['objective_id'] for r in index['objectives']}
    known.add('6118-ANNEX-D-01')
    records=[];details=[]
    drafts=[]
    for name in ('question-parts-draft.json','mc-items-draft.json'):
        drafts+=json.loads((WORK/'assessment-evidence'/name).read_text())['records']
    annotations={}
    for path in sorted((WORK/'planning').glob('semantic-*.tsv')):
        year=int(re.search(r'20\d{2}',path.name)[0])
        for line in path.read_text().splitlines():
            if not line or line.startswith('#'):continue
            part,command,codes,ao,demand=line.split('|')
            key=f'6118-{year}-{part}'
            assert key not in annotations,key
            obj=[]
            for code in codes.split(','):
                section,num=code.split(':');oid=f'6118-{section}-{int(num):02d}'
                assert oid in known,oid
                obj.append(oid)
            annotations[key]=dict(command_word=None if command=='null' else command,
                                  objective_ids=obj,ao_focus=list(ao),context_summary=demand)
    assert len(annotations)==len(drafts)==622
    corrections=json.loads((WORK/'planning/reference-corrections.json').read_text())
    for source in sorted(drafts,key=lambda r:(r['year'],int(r['paper_id']),r['evidence_id'])):
        key=source['evidence_id'];a=annotations[key]
        ref=corrections.get(key,{}).get('question_ref',source['question_ref'])
        command=a['command_word'];text=source['internal_source_text']
        command_origin='none_interrogative_mc' if source['paper_id']=='1' else 'direct'
        command_quote=None
        if command:
            match=re.search(r'\b'+re.escape(command)+r'\b',text,re.I)
            if not match:
                if command=='calculate' and 'Calulate' in text:
                    command_origin='source_typo_normalised';command_quote='Calulate'
                else:
                    question=re.match(r'\d+',ref)[0]
                    previous=[r for r in drafts if r['source_id']==source['source_id'] and r['evidence_id']<key and re.match(r'\d+',r['question_ref'])[0]==question and re.search(r'\b'+re.escape(command)+r'\b',r['internal_source_text'],re.I)]
                    assert previous,(key,command,'no source anchor')
                    command_origin='inherited_from_parent_instruction';command_quote=previous[-1]['evidence_id']
            else:command_quote=match[0]
        elif source['paper_id']!='1':command_origin='interrogative_no_imperative'
        loc=source['source_locator'];pages=loc['pdf_pages']
        locator=loc['path']+'; PDF '+(', '.join(map(str,pages)))+'; question '+ref
        notes=['mapping_method=manual_semantic_read_of_question_demand_against_syllabus_source_bullets; no token-matched first pass.',
               'AO focus is a demand-level judgement, not official part coding or a per-mark allocation; overlapping A/B records must not be summed as separate marks.',
               'Internal evidence only; source question wording must not enter learner-facing resources.',
               f'command_origin={command_origin}']
        if key in corrections:notes.append('reference_repair='+corrections[key]['reason'])
        usable=key!='6118-2024-P1-009'
        if not usable:notes.append('EXCLUDE_FROM_USABLE_EXPOSURE: examiner report 2024 PDF p.654 confirms no correct option and compensation for every candidate; source item retained in census.')
        records.append(dict(evidence_id=key,source_id=source['source_id'],evidence_type='past_paper',
                            exam_series=str(source['year']),year=source['year'],paper_id=source['paper_id'],variant=None,
                            question_ref=ref,mark_tariff=source['mark_tariff'],objective_ids=a['objective_ids'],
                            command_word=command,ao_focus=a['ao_focus'],
                            context_type='multiple_choice' if source['paper_id']=='1' else ('practical_written' if source['paper_id']=='3' else 'structured_theory'),
                            context_summary=a['context_summary'],creditworthy_points=[],examiner_findings=[],
                            common_errors=[],strong_response_features=[],source_locator=locator,notes=notes))
        details.append(dict(evidence_id=key,source_question_ref=source['question_ref'],question_ref=ref,
                            source_locator=loc,internal_source_text=text,
                            mapping_method='manual_semantic_demand_mapping',mapping_status='lead_agent_reviewed',
                            objective_ids=a['objective_ids'],primary_objective_id=a['objective_ids'][0],
                            command_word=command,command_origin=command_origin,command_source_anchor=command_quote,
                            usable_for_exposure=usable,primary_demand=a['context_summary'],
                            figure_review_limit='Meaning reviewed from question text/context; individual source images inspected where ambiguity was identified. This is not an audit of every exam diagram or every numerical answer.'))
    assert sum(r['mark_tariff'] for r in records)==960
    (WORK/'assessment-evidence/assessment_evidence.json').write_text(json.dumps({'map_id':'nam-6118-nssco-2026-assessment-evidence','status':'partial','records':records},indent=2,ensure_ascii=False)+'\n')
    (WORK/'assessment-evidence/demand-review.json').write_text(json.dumps({'scope':'622 source-demand mappings reviewed by the lead agent; report linking/marking coverage separately tracked. Not an independent review.','supplementary_syllabus_anchors':[{'objective_id':'6118-ANNEX-D-01','text':'Annexe D electrical symbols includes a diode. Diode rectification context is observed in the papers; no semiconductor-junction theory is authorised by this anchor.','pdf_page':50,'printed_page':47}],'records':details},indent=2,ensure_ascii=False)+'\n')
    print('Built',len(records),'demand records;',sum(r['mark_tariff'] for r in records),'printed marks; 1 compensated MC item excluded from usable exposure.')


if __name__=='__main__':main()
