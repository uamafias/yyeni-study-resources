"""Proposed Stage-D fixed-fixture bookkeeping, not a submission marker.

Authors supply independently justified gross evidence and once-only eligibility.
This helper derives the proposed net MR ledger; it never reads learner answers.
"""
from copy import deepcopy

def settle(awards,datums):
    """Ordered award dicts: id,part,type,value,earned,datum_ids,depends_on.

    Optional basis is canonical/misread. Datum dicts: datum_id,eligible,
    first_use_part,reason. Values are numeric criterion tariffs (normally one).
    Dependencies and correct-working evidence are tested before net deductions.
    """
    awards=deepcopy(awards);datums=deepcopy(datums)
    assert len({x['id']for x in awards})==len(awards)
    by={x['id']:x for x in awards};data={x['datum_id']:x for x in datums}
    assert len(data)==len(datums)
    for x in datums:
        assert isinstance(x['eligible'],bool)and x['reason']and x['first_use_part']
    for a in awards:
        a.setdefault('value',1);a.setdefault('datum_ids',[]);a.setdefault('depends_on',[])
        assert a['type']in ['M','DM','A','B']and 0<=a['earned']<=a['value']
        assert set(a['datum_ids'])<=set(data)
        if any(not data[d]['eligible']for d in a['datum_ids']):
            assert a.get('basis','canonical')=='canonical','ineligible datum was re-eligible in a later part'
        for dep in a['depends_on']:
            assert dep in by
            if a['earned']:assert by[dep]['earned']==by[dep].get('value',1),('gross dependency not earned',a['id'],dep)
    gross={a['id']:a['earned']for a in awards};net=gross.copy();ledger=[]
    for datum in datums:
        entry={**datum,'eligibility_decided_once':True,'gross_marking_basis':'misread data'if datum['eligible']else'canonical throughout','amount':0,'deducted_criterion':None,'deducted_part':None}
        if datum['eligible']:
            candidates=[a for a in awards if datum['datum_id']in a['datum_ids']and a['type']in ['A','B']and net[a['id']]>=1]
            if candidates:
                a=candidates[0];net[a['id']]-=1;entry.update(amount=1,deducted_criterion=a['id'],deducted_part=a['part'],allocation='first earned A/B on this datum in question/criterion order, including later-use parts')
            else:entry['allocation']='no available earned A/B on this datum anywhere; no M/DM deduction or negative score'
        else:entry['allocation']='ineligible at first use; ordinary canonical evidence in every part, no MR concession'
        ledger.append(entry)
    assert all(v>=0 for v in net.values())
    assert sum(gross.values())-sum(net.values())==sum(x['amount']for x in ledger)
    parts={}
    for a in awards:
        p=parts.setdefault(a['part'],dict(gross=0,net=0,tariff=0));p['gross']+=gross[a['id']];p['net']+=net[a['id']];p['tariff']+=a['value']
    return dict(gross_awards=gross,net_awards=net,gross_total=sum(gross.values()),net_total=sum(net.values()),tariff=sum(a['value']for a in awards),parts=parts,ledger=ledger,dependency_evidence={a['id']:{dep:gross[dep]for dep in a['depends_on']}for a in awards if a['depends_on']},authority='OD-6 principle binding; per-datum order, eligibility ledger and net-after-evidence mechanics proposed pending exact-manifest approval',scope='Fixed design evidence only; no learner response recognition or runtime marking implemented.')

def award(id,part,type,earned=1,datum_ids=None,depends_on=None,basis='misread'):
    return dict(id=id,part=part,type=type,value=1,earned=earned,datum_ids=datum_ids or [],depends_on=depends_on or [],basis=basis)
