"""Quarantine source-note prose; R6 spacing edits did not restore mathematics."""
from analysis_sources import A,WB

DAMAGED='extraction-damaged; read the page'

def apply(items):
    for item in items:
        item['notes_text_status']=DAMAGED
        item['notes_text_status_basis']='Conservative bank-wide warning for this unverified extraction/prose field. Some individual notes may be intact; no item-by-item intactness audit is claimed. R6 spacing edits did not restore all missing mathematical relation signs. Read the rendered source before design.'
        item['notes_are_design_evidence']=False
    return items


def validate(items):
    assert all(i.get('notes_text_status')==DAMAGED and i.get('notes_are_design_evidence')is False for i in items),'source note lacks extraction warning'
    return dict(notes_flagged=len(items),individual_damaged_note_count='not established; bank-wide precaution',full_text_repair_claimed=False)
