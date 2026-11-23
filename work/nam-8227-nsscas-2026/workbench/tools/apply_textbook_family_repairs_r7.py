"""Scoped assembled-family R7 repairs, after unchanged R6 author overlay.

Does not alter accepted source items or infer examination relations. The caller
must attach freshly migrated/rechecked examination comparisons afterwards.
"""
import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from textbook_family_repairs_r6 import member_id

WB=Path(__file__).resolve().parents[1]
PREFIX='8227:TEXTBOOK-FAMILY:'
DUPLICATE_PREFIX=re.compile(r'^(Compared with [^:]+: )\1')


def _load(wb):
    return json.loads((Path(wb)/'tools/textbook-family-repairs-r7.json').read_text())


def _pairs(families):
    return Counter((m['item_id'],label) for f in families for m in f['members'] for label in m['part_labels'])


def _selected_member(member, labels, family_id):
    row=copy.deepcopy(member)
    row['part_labels']=list(labels)
    row['member_id']=member_id(family_id,row['item_id'],labels)
    row['membership_scope']='selected responses (R7 source-backed family correction)'
    ev=row.get('membership_evidence_r6',{})
    if ev:
        ev['responses']=[r for r in ev['responses'] if r['subpart'] in labels]
        assert {r['subpart'] for r in ev['responses']}==set(labels), ('missing selected evidence',row['item_id'],labels)
    return row


def _verify_native(evidence,wb):
    root=Path(wb).resolve().parents[2]
    for name in evidence:
        from textbook_closeout_r7 import readings as closeout_readings
        new=next((r for r in closeout_readings()if r['reading_id']==name),None)
        if new:
            assert new['reader']=='Codex author' and new['read_date']=='2026-11-23','unread closeout native evidence'
            assert hashlib.sha256((root/new['render_path']).read_bytes()).hexdigest()==new['render_sha256'],'closeout native render hash'
            assert hashlib.sha256((root/new['source_path']).read_bytes()).hexdigest()==new['source_sha256'],'closeout source PDF hash'
            continue
        metadata=json.loads((Path(wb)/'checks/r7/parallel-families'/f'{name}.json').read_text())
        png=root/metadata['path']
        assert hashlib.sha256(png.read_bytes()).hexdigest()==metadata['sha256'],('native evidence hash',name)
        assert metadata.get('inspection_status_r7')=='read by author',('unread native evidence',name)


def apply(families, items, wb=WB):
    """Mutate assembled family list; return deterministic migration/audit data."""
    wb=Path(wb);data=_load(wb)
    assert len(families)==data['baseline_family_count'],('R7 expects the assembled R6 family set',len(families))
    before=_pairs(families); assert len(before)==data['baseline_response_pairs']
    idx={f['family_id']:f for f in families}
    itemidx=items if isinstance(items,dict) else {i['item_id']:i for i in items}
    item_dd={k:tuple(v['assessed_8227_demand_ids']) for k,v in itemidx.items()}
    migrations=[];prefix_count=0
    for f in families:
        old=f['distinction_basis']; new=DUPLICATE_PREFIX.sub(r'\1',old)
        while DUPLICATE_PREFIX.match(new):new=DUPLICATE_PREFIX.sub(r'\1',new)
        if new!=old:f['distinction_basis']=new;prefix_count+=1
    for spec in data['new_families']:
        assert spec['family_id'] not in idx
        f=copy.deepcopy(idx[spec['clone_from']]);f.update(spec['fields']);f['family_id']=spec['family_id'];f['members']=[]
        f['r6_origin_family_id']=idx[spec['clone_from']].get('r6_origin_family_id',spec['clone_from'])
        f['family_prose_evidence_r7']={'basis':'Named native-page AUTHOR correction; no new R6 prose acceptance claimed.','input':'tools/textbook-family-repairs-r7.json'}
        for key in ['exam_relations','examination_evidence','member_level_exceptions','internal_held_comparisons','undecided_exam_part_ids']:f[key]=[]
        families.append(f);idx[f['family_id']]=f
    for spec in data['moves']:
        _verify_native(spec['native_evidence'],wb)
        src=idx[spec['from_family_id']];dst=idx[spec['to_family_id']]
        found=[m for m in src['members'] if m['item_id']==spec['item_id'] and set(spec['part_labels'])<=set(m['part_labels'])]
        assert len(found)==1,('move source not unique',spec)
        old=found[0]; src['members'].remove(old)
        labels=spec['part_labels']; moved=_selected_member(old,labels,dst['family_id'])
        moved['membership_reason']=spec['reason'];moved['membership_reason_source_r7']=spec['native_evidence']
        moved['r7_origin_member_id']=old['member_id'];dst['members'].append(moved)
        migrations.append({'old_family_id':src['family_id'],'new_family_id':dst['family_id'],'item_id':old['item_id'],'selected_part_labels':labels,'old_member_id':old['member_id'],'new_member_id':moved['member_id'],'kind':'moved selected responses','reason':spec['reason']})
        remain=[v for v in old['part_labels'] if v not in labels]
        if remain:
            residual=_selected_member(old,remain,src['family_id'])
            residual['membership_reason']='Retained source responses after removing the named misfit: '+ '; '.join('['+r['subpart']+'] '+r['method'] for r in residual.get('membership_evidence_r6',{}).get('responses',[]))
            src['members'].append(residual)
            migrations.append({'old_family_id':src['family_id'],'new_family_id':src['family_id'],'item_id':old['item_id'],'selected_part_labels':remain,'old_member_id':old['member_id'],'new_member_id':residual['member_id'],'kind':'retained residual responses','reason':'Other connected responses remain selected in their original family.'})
    for fid,patch in data['family_patches'].items():idx[fid].update(copy.deepcopy(patch))
    for spec in data['member_reason_patches']:
        _verify_native(spec['native_evidence'],wb)
        found=[m for m in idx[spec['family_id']]['members'] if m['item_id']==spec['item_id'] and m['part_labels']==spec['part_labels']];assert len(found)==1
        found[0]['membership_reason']=spec['reason'];found[0]['membership_reason_source_r7']=spec['native_evidence']
    for alias in data['retired_aliases']:
        f=idx[alias['family_id']];assert not f['members']
        f['legacy_assessed_demand_ids_r7']=f['assessed_demand_ids'];f['assessed_demand_ids']=[]
        f['status']='retired alias (R7 family merge)';f['retired']=True;f['canonical_family_id']=alias['canonical_family_id'];f['retirement_reason']=alias['reason']
        f['learner_decisions']='Retired alias: use '+alias['canonical_family_id']+'. '+alias['reason']
    for record in data['empty_family_dispositions']:
        f=idx[record['family_id']]
        assert f['assessed_demand_ids']==record['assessed_demand_ids_after']
        f['empty_demand_disposition_r7']={k:copy.deepcopy(v) for k,v in record.items() if k!='members'}
    for spec in data['family_response_demand_exceptions']:
        _verify_native(spec['native_evidence'],wb)
        f=idx[spec['family_id']];m=next(m for m in f['members'] if m['item_id']==spec['item_id'] and set(m['part_labels'])==set(spec['part_labels']))
        missing=set(f['assessed_demand_ids'])-set(itemidx[m['item_id']]['assessed_8227_demand_ids'])
        assert missing==set(spec['demand_ids']),('exception not exact',spec,missing)
        m['family_response_demand_evidence_r7']=copy.deepcopy(spec)
    for f in families:
        f['member_item_ids']=sorted({m['item_id'] for m in f['members']})
        f['book_ids']=sorted({itemidx[m['item_id']]['book_id'] for m in f['members']})
    assert _pairs(families)==before,'R7 source-response conservation failed'
    assert item_dd=={k:tuple(v['assessed_8227_demand_ids']) for k,v in itemidx.items()},'R7 changed item demand links'
    audit={'baseline_families':500,'families_after':len(families),'active_families':sum(not f.get('retired') for f in families),'retired_aliases':data['retired_aliases'],'memberships_after':sum(len(f['members'])for f in families),'source_response_pairs':len(before),'duplicate_comparison_prefixes_removed':prefix_count,'empty_family_dispositions':len(data['empty_family_dispositions']),'original_empty_families_assigned_direct_demands':sum(bool(x['assessed_demand_ids_after'])for x in data['empty_family_dispositions']),'member_migrations':migrations,'family_response_demand_exceptions':data['family_response_demand_exceptions'],'limits_note':data['limits_note']}
    validate(families,items,wb=wb)
    return audit


def validate(families, items, wb=WB):
    data=_load(wb);idx={f['family_id']:f for f in families};itemidx=items if isinstance(items,dict) else {i['item_id']:i for i in items}
    assert len(_pairs(families))==data['baseline_response_pairs']
    for f in families:
        assert not DUPLICATE_PREFIX.match(f['distinction_basis']),('doubled sibling prefix',f['family_id'])
        if f.get('retired'):
            assert not f['members'] and not f['assessed_demand_ids'] and f['canonical_family_id'] in idx
        for m in f['members']:
            assert m['member_id']==member_id(f['family_id'],m['item_id'],m['part_labels'])
            missing=set(f['assessed_demand_ids'])-set(itemidx[m['item_id']]['assessed_8227_demand_ids'])
            if missing:
                ev=m.get('family_response_demand_evidence_r7',{})
                assert set(ev.get('demand_ids',[]))==missing and ev.get('reason') and ev.get('native_evidence'),('unjustified family response demand',f['family_id'],m['item_id'],missing)
    for rec in data['empty_family_dispositions']:
        f=idx[rec['family_id']];d=f.get('empty_demand_disposition_r7',{})
        assert d.get('reason') and d.get('disposition'),('empty family missing explicit disposition',f['family_id'])
        assert f['assessed_demand_ids']==d['assessed_demand_ids_after']
    return {'families':len(families),'original_empty_dispositions':61,'source_response_pairs':len(_pairs(families))}


def write_records(audit, wb=WB):
    wb=Path(wb);data=_load(wb)
    record={'schema_version':'8227-empty-family-dispositions-r7-v1','role':'AUTHOR','scope':'All original 61 R6 empty-assessed-demand families, including connected item tags. Not a new audit of every textbook page.','limits':data['limits_note'],'counts':{k:v for k,v in audit.items() if k not in ['member_migrations','family_response_demand_exceptions','retired_aliases']},'families':data['empty_family_dispositions'],'member_migrations':audit['member_migrations'],'family_response_demand_exceptions':audit['family_response_demand_exceptions']}
    (wb/'analysis/empty-demand-families-r7.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
    lines=['# Original empty-demand families: R7 AUTHOR dispositions','',record['scope'],'',data['limits_note'],'','All accepted item-level demand links remain unchanged. A direct family demand describes the selected response and does not certify full examination coverage. '+str(audit['original_empty_families_assigned_direct_demands'])+' of the original 61 families now have limited direct demands; '+str(61-audit['original_empty_families_assigned_direct_demands'])+' retain explicit supporting or qualified dispositions.','','| Family | Disposition | Reason |','|---|---|---|']
    for f in record['families']:lines.append('| '+f['family_id'].replace(PREFIX,'')+' | '+f['disposition']+' | '+f['reason'].replace('|','\\|')+' |')
    lines+=['','The JSON contains every original selected member, part labels, native source locator, unchanged item-level demand tags and accepted response evidence. New native page readings are recorded in checks/r7/parallel-families/.','','The exponential-substitution duplicate is retained as a retired alias. The migration audit retains every old and new membership identifier; source-response pairs are conserved.']
    (wb/'analysis/empty-demand-families-r7.md').write_text('\n'.join(lines)+'\n')
    (wb/'checks/r7/parallel-families/integration-audit.json').write_text(json.dumps(audit,indent=2,ensure_ascii=False)+'\n')
