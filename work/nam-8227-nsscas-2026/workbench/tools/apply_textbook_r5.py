"""Merge explicit R5 source readings; never manufacture completed review fields."""
import copy,json
from analysis_sources import A,WB

def apply(items):
    byid={i['item_id']:i for i in items}
    for i in items:
        i['mapping_review_status_r5']='pending individual assessed/component reclassification'
        i['component_demand_ids']=None
        i['value_level_scope_review_status_r5']='pending actual-value screening'
        i['answer_accuracy_status_r5']='not yet independently derived for every assessed subpart'
    for path in sorted((WB/'tools/textbook-r5').glob('census-*.json')):
        census=json.loads(path.read_text())
        prototype=next(i for i in items if i['book_id']==census['book_id'])
        for entry in census['new_items']:
            assert entry['item_id']not in byid,('duplicate new source item',entry['item_id'])
            # Only book-level facts may carry across. A neighbouring example's
            # note,exam-style basis or verification status is not item evidence.
            row={key:copy.deepcopy(prototype[key])for key in ['book','rights']}
            row.update(disposition='include as internal analysis evidence',
              mapping_depth='Individual item/figure discovered by explicit R5 rendered-page census.',
              exam_style_basis=entry.get('exam_style_basis','Source teaching/practice element; no examination attribution or exam-style label on this element.'),
              value_level_scope_review_status_r5=entry.get('value_level_scope_review_status_r5','pending actual-value screening'),
              answer_accuracy_status_r5='not yet independently derived for every assessed subpart')
            row.update(entry,chapter=census['chapter'],book_id=census['book_id'],source_path=census['source_path'],source_sha256=census['source_sha256'],
                continuation_pdf_pages=entry.get('continuation_pdf_pages',[]),learner_display=False,defects=[],exam_style=entry.get('exam_style',False),sketch_response_required=entry.get('sketch_response_required',False),
                objective_ids=sorted({d.rsplit(':D',1)[0]for d in entry['assessed_8227_demand_ids']}),
                source_check='R5 original page/render enumerated; independent acceptance pending',
                scope_check=entry.get('scope_check',{'status':'in-scope','basis':entry['notes'],'excluded_or_qualified_parts':[],
                  'qualifier_screen':entry.get('value_level_scope_decisions',[]),'limits_considered':[]}),
                design_use_status='candidate internal evidence; T1–T6 completion and independent acceptance pending')
            row.setdefault('answer_key',{'available':None,'pdf_pages':[],'printed_pages':[],'locator':'Teaching figure; no separately assessed learner task','verification_status':'Figure mathematics requires feature verification,not an answer-key match'})
            row['answer_key'].setdefault('verification','R5 answer location or inline illustration identified from render; full independent subpart accuracy remains pending unless separately recorded.')
            row['evidence_role']=entry.get('evidence_role','prerequisite/supporting teaching figure; no directly assessed coverage'if row['item_kind']in['teaching-figure','given-figure']else'directly related assessed practice')
            row['mapping_review_status_r5']='author reclassified assessed/component roles; independent check pending'
            row['mapping_rule']='Explicit requested result or enforced method is assessed; intermediate methods or figure teaching context do not become separately assessed demands.'
            if row.get('item_kind')in ['teaching-figure','given-figure']:
                row['answer_accuracy_status_r5']='No separate learner response; source mathematical features checked with parent derivation and explicit figure reasoning; independent review pending'
            items.append(row);byid[row['item_id']]=row
        for patch in census.get('corrections',[]):
            byid[patch['item_id']].update({k:v for k,v in patch.items()if k!='item_id'})
    answer_rows=json.loads((A/'textbook-answer-verification-r5.json').read_text())['subparts']
    for path in sorted((WB/'tools/textbook-r5').glob('answers-*.json')):
        for entry in json.loads(path.read_text())['items']:
            row=byid[entry['item_id']]
            row['notes']=entry['notes'];row['scope_check']['basis']=entry['notes']
            row['component_demand_ids']=entry['component_demand_ids']
            if 'assessed_8227_demand_ids' in entry:
                row['assessed_8227_demand_ids']=entry['assessed_8227_demand_ids']
                row['objective_ids']=sorted({d.rsplit(':D',1)[0]for d in row['assessed_8227_demand_ids']})
            for field in ['teaches_8227_demand_ids','evidence_role','mapping_rationale','component_demand_roles','direct_demand_aspects','precision_angle_check','correlated_branch_check','source_interpretation','source_label_warning','principal_branch_check','representation','sketch_response_required','original_domain','physical_parameter_domain','source_domain_caution','source_goal_warning','connected_part_structure','continuation_pdf_pages','source_duplicate_of','source_part_repeats','source_related_item_ids','duplicate_basis','source_part_tariffs','source_total_marks','source_marks_kind']:
                if field in entry:row[field]=entry[field]
            row['mapping_review_status_r5']='author reclassified assessed/component roles; independent check pending'
            row['mapping_rule']='Explicit requested result or enforced method is assessed; intermediate computations are components. Supporting arithmetic without a matching8227demand has no invented demand link.'
            row['exam_style']=entry['exam_style']
            row['exam_style_basis']=entry['exam_style_basis']
            own=[a for a in answer_rows if a['item_id']==entry['item_id']]
            assert len(own)==len(entry['subparts'])
            row['answer_verification_r5']=own
            row['answer_expected_subpart_labels_r5']=entry['expected_subpart_labels']
            complete=set(entry['expected_subpart_labels'])=={r['subpart']for r in own}
            row['answer_accuracy_status_r5']='author independently derived every explicit subpart; printed result compared or absence/source-graph limitation explicit; independent check pending'if complete else'partial subpart verification; whole-item answer check remains open'
            if complete:
                row['answer_key']['previous_locator_before_r5']={key:copy.deepcopy(row['answer_key'].get(key))for key in ['pdf_pages','printed_pages','locator']}
                pages=sorted({r['answer_pdf_page']for r in own if r['answer_pdf_page']is not None})
                row['answer_key'].update(pdf_pages=pages,printed_pages=[next(r['answer_printed_page']for r in own if r['answer_pdf_page']==page)for page in pages],
                  available=bool(pages),per_subpart_key_presence_r5={r['subpart']:r.get('key_presence','Printed result/inline solution compared on the cited page')for r in own},
                  locator='Exact answer location recorded by each subpart in answer_verification_r5',
                  verification_status='Every stated subpart author-derived and compared; explicit no-key/show/sketch/source-defect dispositions retained; independent acceptance pending')
            if 'scope_check' in entry:
                row['scope_check'].update(entry['scope_check'])
            row['value_level_scope_decisions']=entry['value_level_scope_decisions']
            row['value_level_scope_review_status_r5']='author actual-value decisions complete; independent check pending'
            row['scope_check']['qualifier_screen']=entry['value_level_scope_decisions']
    # Explicit final audit annotations supplement the original per-item source
    # record. No applicability is inferred from a family, topic or desired count.
    from textbook_scope_audit_inputs_r5 import PATCHES
    for patch in PATCHES:
        row=byid[patch['item_id']]
        decision=copy.deepcopy(patch['decision'])
        assert decision['rule_id']not in {d['rule_id']for d in row.get('value_level_scope_decisions',[])},('final scope annotation duplicates an original decision',row['item_id'],decision['rule_id'])
        row.setdefault('value_level_scope_decisions',[]).append(decision)
        row['scope_check']['qualifier_screen']=copy.deepcopy(row['value_level_scope_decisions'])
    # A located wrong key must remain visible on its item,not only in a side register.
    for defect_register in [A/'textbook-defects-r5.json',A/'textbook-corrections-r6.json']:
        if not defect_register.exists():continue
        for defect in json.loads(defect_register.read_text())['entries']:
            for item_id in [defect['item_id'],*defect.get('also_affects_item_ids',[])]:
                assert item_id in byid,('source defect has no inventory item',item_id)
                row=byid[item_id]
                row.setdefault('source_defect_ids_r5',[]).append(defect['defect_id'])
                row['defects'].append({'defect_id':defect['defect_id'],'issue':defect['issue'],'correct_answer':defect['correct_answer'],'source':defect_register.name})
    registry=json.loads((A/'demand-registry.json').read_text())
    valid={d['demand_id']for d in registry['demands']}
    component_valid=valid|{d['demand_id']for d in registry['supplementary_demands']}
    for row in items:
        assert set(row['assessed_8227_demand_ids'])<=valid,('invalid assessed demand',row['item_id'])
        assert set(row.get('teaches_8227_demand_ids',[]))<=valid,('invalid teaching demand',row['item_id'])
        if row['component_demand_ids']is not None:
            assert set(row['component_demand_ids'])<=component_valid,('invalid component demand',row['item_id'])
            assert not set(row['component_demand_ids'])&set(row['assessed_8227_demand_ids']),('assessed/component role overlap',row['item_id'])
    return items
