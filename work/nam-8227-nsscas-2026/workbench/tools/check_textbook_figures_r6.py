"""Narrow R6 figure-overlay checks; does not mutate canonical inventory."""
import copy
import json
from apply_textbook_figures_r6 import apply,validate,comparison_index,_figures
from analysis_sources import A,WB,digest,write


def main():
    original=json.loads((A/'textbook-inventory.json').read_text())['items']
    items=apply(copy.deepcopy(original));index=comparison_index(items)
    counts=validate(items,index)
    negative=[]
    def rejects(name,mutate):
        seeded=copy.deepcopy(items);mutate(_figures(seeded)[0])
        try:validate(seeded)
        except AssertionError as e:negative.append(dict(fixture=name,result='rejected',reason=str(e)))
        else:raise AssertionError('negative fixture passed:'+name)
    rejects('pending-figure-status',lambda i:i['exam_representation_check'].update(status='comparison pending'))
    rejects('unclassified-figure',lambda i:i.update(figure_record_type='unclassified'))
    rejects('content-certification-from-parent',lambda i:i.update(content_check='verified by parent answer'))
    rejects('invented-exam-part',lambda i:i['exam_representation_check'].update(examination_part_ids=['8227:EXAM:9999:P1:Q1:a']))
    rejects('textbook-image-learner-display',lambda i:i.update(learner_display=True))
    # An idempotent overlay does not mutate the accepted item-demand links.
    keys=['assessed_8227_demand_ids','component_demand_ids','objective_ids','learner_display']
    projection=lambda xs:{i['item_id']:{k:i.get(k)for k in keys}for i in xs}
    assert projection(original)==projection(items),'accepted mapping changed'
    twice=apply(copy.deepcopy(items));assert twice==items,'overlay not idempotent'
    assert comparison_index(twice)==index,'representation index not deterministic'
    proof=dict(status='author narrow checks pass; independent review required',date='2026-11-22',
        counts=counts,new_negative_fixtures=negative,
        accepted_item_links_preserved=True,overlay_idempotent=True,comparison_index_deterministic=True,
        input_sha256={n:digest(WB/n)for n in ['tools/apply_textbook_figures_r6.py','tools/textbook-figure-repairs-r6.json','tools/check_textbook_figures_r6.py']},
        native_layout_pages=23,
        limitations=['Taxonomy uses the accepted per-figure census descriptions, not 1758 fresh native reads. The23named native pages resolve ambiguous layout/role cases.',
            'All1758contentchecks remain explicitly notchecked; known9figuredefects are separately retained. No full content audit is required or claimed.',
            'Examcomparison is medium+demand only; not an exactfigure/sameproblem match. Figure features and objective map pointers preserve the distinction.',
            'This checker runs on in-memory copies; canonical inventory and derived comparison output are integrated by the parent builder.'])
    write(WB/'checks/r6/parallel-figures/checkpoint.json',proof)
    print(json.dumps(proof,indent=2))


if __name__=='__main__':main()
