"""Narrow R6 inventory repairs, preserving accepted item demand/answer records.

A content-check status is not inferred from the census, a parent task, a hash or
an earlier boilerplate claim. Figure taxonomy and exam representation are separate
remaining author tasks; this overlay does not mark them complete.
"""
import json
import hashlib
import re
from analysis_sources import A,WB,ROOT,digest


def apply(items):
    byid={i['item_id']:i for i in items}
    for i in items:
        if i.get('item_kind') not in ['given-figure','teaching-figure']:
            continue
        i['content_check']='not checked; not design evidence until checked'
        i['content_check_basis']='No complete figure-content audit is claimed. A parent answer check or census entry is not verification of every visual feature.'
        known=[d for d in i.get('defects',[])if d.get('source')=='textbook-corrections-r6.json']
        if known:
            i['known_figure_corrections_r6']=[d['defect_id']for d in known]
            i['content_check_basis']+=' The named defect correction is verified separately; it does not certify the whole figure.'
    spacing_entries=[]
    for name in ['textbook-note-spacing-r6.json','textbook-note-spacing-parallel-r6.json','textbook-note-spacing-root-r6.json']:
        spacing_entries.extend(json.loads((WB/'tools'/name).read_text())['entries'])
    assert len({r['item_id'] for r in spacing_entries})==len(spacing_entries),'duplicate note repair'
    for entry in spacing_entries:
        i=byid[entry['item_id']];old=i['notes'];new=entry['note']
        r7_path=WB/'tools/textbook-source-repairs-r7.json'
        corrections=json.loads(r7_path.read_text()).get('response_corrections',[]) if r7_path.exists() else []
        corrected_note=next((r for r in corrections if r['item_id']==i['item_id'] and old==r.get('corrected_note')),None)
        if corrected_note:
            assert new==corrected_note.get('baseline_note') or hashlib.sha256(corrected_note['baseline_source_note'].encode()).hexdigest()==entry['previous_note_sha256'],'unrecognised superseded note patch'
            i['note_spacing_repair_r6']=dict(date=entry['date'],change='Historical whitespace patch superseded by the explicit source-backed R7 tan²x correction; no old mathematical typo restored.')
            continue
        if old!=new:
            assert hashlib.sha256(old.encode()).hexdigest()==entry['previous_note_sha256'],('note baseline changed',i['item_id'])
            compact_old=re.sub(r'\s','',old)
            correction=entry.get('editorial_typo_correction')
            if correction:
                assert compact_old.count(correction['before_compact'])==1,('editorial typo baseline changed',i['item_id'])
                compact_old=compact_old.replace(correction['before_compact'],correction['after_compact'])
            assert compact_old==re.sub(r'\s','',new),('non-whitespace note mutation',i['item_id'])
            i['notes']=new
            if i['scope_check'].get('basis')==old:i['scope_check']['basis']=new
        i['note_spacing_repair_r6']=dict(date=entry['date'],change=entry['change'])
    page=json.loads((WB/'checks/r6/comparison/YM-34-figure-role-r6.json').read_text())
    assert digest(ROOT/page['path'])==page['sha256']
    assert digest(ROOT/page['source_path'])==page['source_sha256']
    for n,record_type,description in [
        (48,'text callout','Two alternative vertex calculations appear below the Solution heading.'),
        (49,'graphic','The plotted parabola is the worked solution to Sketch the graph, not a supplied learner given.')]:
        i=byid[f'8227:TB:YM:C1:Teaching-figure:{n}']
        assert i['pdf_page']==34 and i['parent_item_id']=='8227:TB:YM:C1:Example:24'
        i['item_kind']='teaching-figure'
        i['figure_record_type']=record_type
        i['figure_role']='worked-solution panel'
        i['figure_role_evidence']=dict(path=page['path'],sha256=page['sha256'],
            source_pdf_page=34,reader='Codex author',date='2026-11-22',reason=description)
        i['evidence_role']='prerequisite/supporting worked solution/teaching representation; not question givens or separately assessed coverage'
    return items
