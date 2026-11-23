"""Uncapped family-level candidates under the owner-revised R6 commission.

No overlap ranking, all-demands filter, automatic relation or read stamp.
The prior member-level workload is archived as superseded discovery.
"""
import json
from analysis_sources import A,WB,ROOT,digest,write
from textbook_family_repairs_r6 import member_id,validate_member_demands
from textbook_exam_comparison_r6 import candidate_ids

membership_id=member_id


def build():
    items={i['item_id']:i for i in json.loads((A/'textbook-inventory.json').read_text())['items']}
    families=json.loads((A/'textbook-families.json').read_text())['families']
    parts={p['part_id']:p for q in json.loads((A/'question-analysis.json').read_text())['questions']for p in q['parts']}
    records=[]
    for family in families:
        for member in family['members']:
            validate_member_demands(family,items[member['item_id']])
        demands=set(family['assessed_demand_ids'])
        candidates=[]
        for part_id,part in sorted(parts.items()):
            overlap=demands&set(part['directly_assessed_demand_ids'])
            if part_id not in candidate_ids(family,parts):continue
            candidates.append(dict(part_id=part_id,overlapping_demand_ids=sorted(overlap),
                response_format=part['response_format'],disposition=part['disposition'],
                hold_ids=part.get('hold_ids',[]),paper_locator=part['paper_locator'],
                review_status='candidate; decision not yet recorded'))
        records.append(dict(family_id=family['family_id'],title=family['title'],
            learner_decisions=family['learner_decisions'],assessed_demand_ids=sorted(demands),
            members=[dict(member_id=m['member_id'],item_id=m['item_id'],part_labels=m['part_labels'],
                source_path=m['source_path'],source_sha256=m['source_sha256'],
                pdf_page=m['pdf_page'],printed_page=m['printed_page'])for m in family['members']],
            candidates=candidates,demands_searched=sorted(demands),
            no_candidate_reason=('No directly assessed demand overlap in the 250-part NSSCAS corpus.'
                if demands else 'Supporting family has no common directly assessed demand; '
                'its source item/component links remain available separately.')if not candidates else None))
    counts=dict(families=len(families),families_with_candidates=sum(bool(f['candidates'])for f in records),
        families_without_candidates=sum(not f['candidates']for f in records),
        family_part_pairs=sum(len(f['candidates'])for f in records),
        maximum_candidates_per_family=max(len(f['candidates'])for f in records))
    result=dict(schema_version='8227-family-exam-candidates-r7',
        status='uncapped discovery; not comparison decisions',
        authority='R7 owner prompt: uncapped demand candidates plus explicit direct-source search candidates',
        inputs={str(p.relative_to(ROOT)):digest(p)for p in [A/'textbook-inventory.json',A/'textbook-families.json',A/'question-analysis.json']},
        counts=counts,families=records,
        limits='A positive demand overlap is a candidate only. Rejections need a learner-decision/response reason; '
        'same-type and structural-branch decisions require actual source-page reads. '
        'Held parts remain evidence and cannot supply an unqualified learner anchor.')
    write(A/'textbook-exam-candidates-r6.json',result)
    write(WB/'checks/r6/candidate-counts.json',counts)
    print(json.dumps(counts,indent=2))
    return result


if __name__=='__main__':build()
