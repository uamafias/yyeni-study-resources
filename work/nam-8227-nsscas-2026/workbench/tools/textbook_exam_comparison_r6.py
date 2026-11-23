"""Validate authored family decisions and derive summaries, without guessing reads."""
import collections
import copy
import datetime
import json
from analysis_sources import A,WB,ROOT,digest,write,evidence_path


def active_ledger_path():
    current=A/'textbook-exam-relations-r7.json'
    return current if current.exists() else WB/'tools/textbook-exam-relations-r6.json'


def candidate_ids(family,parts):
    overlap={pid for pid,p in parts.items()
            if set(family['assessed_demand_ids'])&set(p['directly_assessed_demand_ids'])}
    sourced=family.get('source_search_candidates_r7',[])
    assert all(r.get('reason') and r.get('exemplar_item_selections') and r['part_id']in parts for r in sourced),'source-search candidate lacks evidence'
    return overlap|{r['part_id']for r in sourced}


def validate_candidate_decisions(family,parts):
    recorded=[r['part_id']for r in family.get('exam_relations',[])]
    assert len(recorded)==len(set(recorded)),'duplicate family/part decision'
    assert set(recorded)==candidate_ids(family,parts),'family has undecided demand-overlap candidate'


def validate_insight_availability(insight,parts):
    observed={pid for pid,p in parts.items()
              if set(insight['demand_ids'])&set(p['directly_assessed_demand_ids'])}
    assert not observed or 'none claimed'not in insight['examination_comparison'].lower(), 'insight claims no exam parts despite direct-demand evidence'
    assert set(insight['examination_part_ids'])==observed,'insight exam availability disagrees with direct part links'


def validate_figure_status(figure):
    def check(value):
        if isinstance(value,dict):
            for k,v in value.items():
                if k.endswith('status')or k in ['exam_representation_check','status']:
                    assert 'pending'not in str(v).lower()or 'independent'in str(v).lower(), 'figure retains pending status'
                check(v)
        elif isinstance(value,list):
            for v in value:check(v)
    text=json.dumps(figure).lower()
    assert 'comparison pending'not in text and 'pending actual-value screening'not in text, 'figure retains pending status'
    check(figure)


def validate_summary_anchors(family,parts):
    for pid in family['examination_relation']['part_ids']:
        assert pid in parts and parts[pid]['disposition']=='include' and not parts[pid].get('hold_ids'), 'held part became a usable family anchor'


def validate_relation(record,family,parts,readings):
    pid=record['part_id'];kind=record['relation']
    assert pid in candidate_ids(family,parts),('relation is not a demand-overlap candidate',family['family_id'],pid)
    assert kind in ['same type','structural branch','rejected'],('invalid relation',kind)
    if kind=='rejected':
        assert record.get('rejection_reason','').strip(),'rejection lacks a decision/response reason'
        return
    date=record.get('read_date')
    assert date,'positive relation has no rendered-page read date'
    datetime.date.fromisoformat(date)
    member_ids={m['member_id']:m for m in family['members']}
    assert record.get('exemplar_member_ids'),'positive relation has no exemplar'
    assert set(record['exemplar_member_ids'])<=set(member_ids),'exemplar is not a family member'
    assert record.get('differing_decision','').strip(),'positive relation lacks comparison evidence'
    if kind=='same type':
        assert not record.get('additional_source_decisions'), \
            'same-type relation adds a source learner decision'
    if kind=='structural branch':
        assert record.get('difficulty_relative_to_exam')in ['easier','harder','mixed'], 'branch lacks warranted easier/harder/mixed direction'
    ids=record.get('rendered_reading_ids',[])
    assert ids and set(ids)<=set(readings),'positive relation has no rendered source evidence'
    seen=[]
    for rid in ids:
        r=readings[rid]
        # A comparison may cross midnight or reuse an unchanged page already
        # read in this repair. Preserve the actual source-read date; do not
        # invent a same-day reread merely to satisfy the comparison timestamp.
        source_date=r.get('read_date')
        assert source_date and r.get('reader')=='Codex author','source page not recorded as read'
        assert datetime.date.fromisoformat(source_date)<=datetime.date.fromisoformat(date), \
            'source page read after comparison date'
        assert digest(evidence_path(r['render_path']))==r['render_sha256'],'render evidence changed'
        seen.append(r)
    loc=parts[pid]['paper_locator']
    original=next(ref for ref in parts[pid]['examination_references']
                  if ref['relation']=='original'and ref['board']=='NSSCAS')
    # Question-level page lists can include a preceding question or a later
    # sibling part. Reading that page does not establish reading this part.
    part_pages=set(range(original['pdf_page'],loc['part_end_pdf_page']+1))
    assert any(r['source_path']==loc['path']and r['source_sha256']==loc['sha256']
               and r['pdf_page']in part_pages for r in seen),'exam part page not read'
    for mid in record['exemplar_member_ids']:
        m=member_ids[mid]
        assert any(r['source_path']==m['source_path']and r['source_sha256']==m['source_sha256']
                   and r['pdf_page']in [m['pdf_page']]+m['continuation_pdf_pages']for r in seen),'textbook exemplar page not read'
    for mid,labels in record.get('exemplar_part_labels',{}).items():
        assert mid in record['exemplar_member_ids']and set(labels)<=set(member_ids[mid]['part_labels']),'unknown exemplar response'


def attach(families,parts,require_complete=False,data=None):
    path=active_ledger_path()
    if data is None:data=json.loads(path.read_text())if path.exists()else dict(relations=[],readings=[])
    readings={r['reading_id']:r for r in data['readings']}
    assert len(readings)==len(data['readings']),'duplicate read identity'
    by_family=collections.defaultdict(list)
    family_ids={f['family_id']for f in families}
    for r in data['relations']:
        assert r['family_id']in family_ids,('relation refers to retired family',r['family_id'])
        by_family[r['family_id']].append(r)
    pending=[];totals=collections.Counter();exception_count=0
    for f in families:
        rows=by_family[f['family_id']]
        ids=[r['part_id']for r in rows]
        assert len(ids)==len(set(ids)),('duplicate family/part decision',f['family_id'])
        for r in rows:validate_relation(r,f,parts,readings)
        f['member_level_exceptions']=[]
        mids={m['member_id']:m for m in f['members']}
        for exception in data.get('member_level_exceptions',[]):
            if exception['family_id']!=f['family_id']:continue
            assert exception['member_id']in mids,'member exception has no source member'
            member=mids[exception['member_id']]
            assert exception['part_labels']and set(exception['part_labels'])<=set(member['part_labels']),'member exception names unknown response'
            for r in exception['exam_relations']:validate_relation(r,f,parts,readings)
            f['member_level_exceptions'].append(copy.deepcopy(exception))
            member.setdefault('exam_relations',[]).extend(dict(r,source_part_labels=exception['part_labels'])
                for r in copy.deepcopy(exception['exam_relations']))
            exception_count+=1
        missing=sorted(candidate_ids(f,parts)-set(ids))
        if require_complete:
            validate_candidate_decisions(dict(f,exam_relations=rows),parts)
        f['exam_relations']=[copy.deepcopy(r)for r in rows]
        f['exam_comparison_status']='all candidate pairs decided'if not missing else'comparison incomplete'
        f['undecided_exam_part_ids']=missing
        f['demands_searched']=list(f['assessed_demand_ids'])
        f['r5_examination_relation']=f['examination_relation']
        if 'examination_comparison_author_input'in f:
            f['r5_examination_comparison_author_input']=f['examination_comparison_author_input']
        f['examination_comparison_author_input']=str(active_ledger_path().relative_to(WB))
        positive=[r for r in rows if r['relation']!='rejected']+[
            dict(r,member_exception_id=e['member_id'],source_part_labels=e['part_labels'])
            for e in f['member_level_exceptions']for r in e['exam_relations']
            if r['relation']!='rejected']
        internal_held=[r for r in positive if parts[r['part_id']]['disposition']!='include' or parts[r['part_id']].get('hold_ids')]
        all_positive=positive
        positive=[r for r in all_positive if parts[r['part_id']]['disposition']=='include' and not parts[r['part_id']].get('hold_ids')]
        f['internal_held_comparisons']=copy.deepcopy(internal_held)
        if missing:
            kind='comparison incomplete'
        elif any(r['relation']=='same type'for r in positive):
            kind='same type as'
        elif positive:
            kind='structural branch'
        else:
            kind='textbook-only'
        f['examination_relation']=dict(kind=kind,
            part_ids=sorted({r['part_id']for r in positive}),
            same_type_part_ids=sorted({r['part_id']for r in positive if r['relation']=='same type'}),
            structural_branch_part_ids=sorted({r['part_id']for r in positive if r['relation']=='structural branch'}),
            pattern_ids=sorted({p for r in positive for p in parts[r['part_id']]['pattern_ids']}),
            reason='Derived from explicit family/part decisions and named member exceptions. '
                'A partial-response match applies only to the named responses. '
                'An incomplete comparison is never labelled textbook-only.',
            evidence_label='textbook-derived with separately identified examination comparisons',
            unqualified_learner_anchor_part_ids=sorted({r['part_id']for r in positive
                if parts[r['part_id']]['disposition']=='include'and not parts[r['part_id']].get('hold_ids')}))
        f['examination_evidence']=[dict(part_id=r['part_id'],relation=r['relation'],
            paper_locator=parts[r['part_id']]['paper_locator'],comparison_only=True,
            member_exception_id=r.get('member_exception_id'),
            source_part_labels=r.get('source_part_labels'),
            held=parts[r['part_id']]['disposition']!='include'or bool(parts[r['part_id']].get('hold_ids')))
            for r in all_positive]
        validate_summary_anchors(f,parts)
        pending.extend(dict(family_id=f['family_id'],part_id=pid)for pid in missing)
        totals.update(r['relation']for r in rows)
    exception_relations=[dict(r,family_id=e['family_id'])
        for e in data.get('member_level_exceptions',[])for r in e['exam_relations']]
    unique_same={(r['family_id'],r['part_id'])for r in data['relations']+exception_relations
        if r['relation']=='same type'}
    counts=dict(candidate_pairs=sum(len(candidate_ids(f,parts))for f in families),
        decisions_recorded=sum(totals.values()),decisions_by_kind=dict(totals),
        undecided_pairs=len(pending),member_level_exceptions=exception_count,
        member_exception_decisions_by_kind=dict(collections.Counter(
            r['relation']for r in exception_relations)),
        same_type_family_part_pairs_including_member_exceptions=len(unique_same),
        families_by_summary=dict(collections.Counter(f['examination_relation']['kind']for f in families)))
    write(WB/'checks/r6/comparison-progress.json',dict(counts=counts,undecided_pairs=pending))
    return counts


def rewrite_insight_comparisons(insights,families,parts):
    """Direct exam availability is independent of the family match decisions."""
    for i in insights:
        ds=set(i['demand_ids'])
        pids=sorted(pid for pid,p in parts.items()if ds&set(p['directly_assessed_demand_ids']))
        matched=[(f,r)for f in families
                 for r in f['exam_relations']+[r for e in f.get('member_level_exceptions',[])for r in e['exam_relations']]
                 if r['part_id']in pids and r['relation']!='rejected'
                 and parts[r['part_id']]['disposition']=='include' and not parts[r['part_id']].get('hold_ids')]
        same=[(f,r)for f,r in matched if r['relation']=='same type']
        branches=[(f,r)for f,r in matched if r['relation']=='structural branch']
        gaps=sorted(d for d in ds if not any(d in p['directly_assessed_demand_ids']for p in parts.values()))
        pending=sum(len(f['undecided_exam_part_ids'])for f in families if ds&set(f['assessed_demand_ids']))
        out=['Directly assessed NSSCAS parts: '+(', '.join(pids)if pids else'none claimed')+'.']
        out+=['Same-type textbook practice: '+('; '.join(f['family_id']+' to '+r['part_id']for f,r in same)if same else'relation not established for the recorded exemplars')+'.']
        out+=['Structural branches: '+('; '.join(f['family_id']+' to '+r['part_id']+' — '+r['differing_decision']+' ('+r['difficulty_relative_to_exam']+')'for f,r in branches)if branches else'relation not established for the recorded exemplars')+'.']
        out+=['Demands without an NSSCAS part: '+(', '.join(gaps)if gaps else'none')+'.']
        held=[p for p in pids if parts[p]['disposition']!='include'or parts[p].get('hold_ids')]
        if held:out.append('Held/defective evidence, not usable learner anchors: '+', '.join(held)+'.')
        if pending:out.append(f'Comparison remains open: {pending} family–part decisions in the associated families. Absence of a recorded match is not a no-counterpart judgement.')
        i['examination_comparison']='\n\n'.join(out)
        i['examination_part_ids']=pids
        validate_insight_availability(i,parts)
        i['exam_comparison_r6']=dict(same_type_relations=len(same),structural_branches=len(branches),
            unresolved_family_part_pairs=pending,unexamined_demand_ids=gaps)
        # Replace the active R5 proposals; old no-counterpart conclusions are
        # historical evidence, not advice the planner should still follow.
        i['r5_implications_for_step3']=i['implications_for_step3']
        associated=[f for f in families if ds&set(f['assessed_demand_ids'])]
        def named_examples(rows):
            seen=set();result=[]
            for f,r in rows:
                key=(f['family_id'],r['part_id'])
                if key in seen:continue
                seen.add(key)
                result.append(f['family_id']+' against '+r['part_id'])
            return result
        proposals=['Review problem sets for these exact demands: '+', '.join(sorted(ds))+'.']
        anchors=named_examples(same)
        if anchors:
            proposals.append('Begin equivalence review with '+('; '.join(anchors[:4]))+
                (f'; {len(anchors)-4} further named same-type family/part pairs are in the objective map.'
                 if len(anchors)>4 else'.')+
                ' Carry only the selected exemplar response labels into later branch-reference decisions.')
        elif any(parts[pid]['disposition']=='include' and not parts[pid].get('hold_ids') for pid in pids):
            proposals.append('NSSCAS directly assesses these demands, but no same-type textbook response is verified here. '
                'Use the listed exam demands as design evidence; review the actual close variants and other practice before deciding what new task structure to author.')
        if pids and not any(parts[pid]['disposition']=='include' and not parts[pid].get('hold_ids')for pid in pids):
            proposals.append('All listed NSSCAS parts are held/defective. They are internal source-defect evidence, not design evidence; use valid scoped textbook and Cambridge comparators instead.')
        if 'principal inverse' in i['title'].lower():
            cb=json.loads((A/'cambridge-evidence.json').read_text())['items']
            comparable=[c for c in cb if ds&set(c['assessed_8227_demand_ids'])]
            if comparable:
                proposals.append('Scoped Cambridge comparators linked in the objective map: '+ '; '.join(c['item_id']+' — '+c['examination_references'][0]['learner_label'] for c in comparable)+'. These are comparable Cambridge evidence, not NSSCAS originals.')
                i['cambridge_comparator_item_ids_r7']=[c['item_id']for c in comparable]
        for direction in ['easier','harder','mixed']:
            ordered=[(f,r)for f,r in branches if r['difficulty_relative_to_exam']==direction]
            if ordered:
                f,r=ordered[0]
                proposals.append('A concrete '+direction+' comparison is '+f['family_id']+' against '+r['part_id']+
                    ': '+r['differing_decision']+' Use this difference when deciding scaffolding and connected responses; '
                    'the complete ordered comparison list is in the objective map.')
        if gaps:
            proposals.append('Retain problem sets for the unexamined demands '+', '.join(gaps)+
                ', using the indexed textbook items and scoped Cambridge evidence where present; lack of a recent NSSCAS part does not remove syllabus scope.')
        nonordered=sum(r.get('nonordered_connection',False)for f in associated
            for r in f['exam_relations']+[r for e in f.get('member_level_exceptions',[])for r in e['exam_relations']]if r['relation']=='rejected')
        if nonordered:
            proposals.append(f'{nonordered} related comparisons add different decisions on the two sides. '
                'Their relation is not established; retain their specific source-search reasons without inferring absent practice or an established mixed branch.')
        if pending:
            proposals.append('Finish the explicitly open family comparisons before using this section to settle recipe coverage.')
        proposals.append('Resolve overlapping assessed/component registry links using the accepted source-item union. '
            'The next planning stage decides recipe boundaries, marking, generated diagrams and branch references; these suggestions approve none of them.')
        i['implications_for_step3']='\n\n'.join(proposals)
