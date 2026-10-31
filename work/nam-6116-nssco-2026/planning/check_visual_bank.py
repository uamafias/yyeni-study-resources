#!/usr/bin/env python3
"""Check staged visual-bank integrity. Passing is NOT scientific or learner-release approval."""
import hashlib, json, pathlib, re, sys, xml.etree.ElementTree as ET
WS = pathlib.Path('work/nam-6116-nssco-2026')
J = lambda p: json.loads((WS/p).read_text())
assets = J('visuals/manifest.json')['assets']
bindings = J('visuals/bindings.json')['bindings']
reqs = {r['requirement_id']: r for r in J('curriculum/visual-requirements.json')['requirements']}
reg = {r['objective_id'] for r in J('curriculum/objective_registry.json')['objectives']}
slots, units = {}, {}
for t in range(1, 6):
    w = J(f'topics/{t}/work_order.json')
    slots.update({s['slot']: s['objective_id'] for s in w['item_slots']})
    units.update({u['unit_id']: u['objective_ids'] for u in w['content_units']})
NEEDS = {'stimulus_image': {'teaching', 'question', 'answer', 'unfamiliar_example'}, 'teaching_diagram': {'teaching'},
         'model_drawing': {'model_drawing', 'marking_criteria'}, 'graph': {'question', 'answer'}}
STATES = {'candidate (unreviewed)', 'variant to prepare', 'GAP'}
bad = []
by_id = {a['asset_id']: a for a in assets}
approvals = J('planning/operator_approvals.json')['images']['assets']
for aid, approval in approvals.items():
    a = by_id.get(aid)
    if not a or a.get('operator_approval') != approval:
        bad.append('operator-approved asset missing or approval changed: ' + aid)
    elif {f['path']: f['sha256'] for f in a['files']} != approval['files']:
        bad.append('operator approval does not cover current asset files: ' + aid)
for a in assets:
    if a.get('operator_approval') and a['asset_id'] not in approvals:
        bad.append('asset has an unrecorded operator approval: ' + a['asset_id'])
for aid, reason in J('planning/visual_candidate_review.json')['holds'].items():
    if aid not in by_id or by_id[aid].get('hold') != reason:
        bad.append('declared hold missing/changed in manifest: ' + aid)
paths = {f['path']: a for a in assets for f in a['files']}
if len(by_id) != len(assets): bad.append('duplicate asset IDs')
for r in reqs.values():
    if r['requirement_id'] != 'VIS-' + r['objective_id'][len('OBJ-'):]: bad.append('unstable requirement ID ' + r['requirement_id'])
    if set(r['needs']) != set(r['kinds']): bad.append(r['requirement_id'] + ': needs do not match kinds')
for a in assets:
    aid = a['asset_id']
    if set(a['objective_ids']) - reg: bad.append(aid + ': unknown objective')
    if not a.get('rights') or not (a.get('source_locator') or a.get('pdf_page')): bad.append(aid + ': missing provenance/rights')
    if a['scientific_review']['status'] != 'pending': bad.append(aid + ': unexpected approval in staged bank')
    if not a['learner_release_status'].startswith('held') or not a['yyeni_status'].startswith('not attached'): bad.append(aid + ': release or YYeni state advanced')
    if a['source_kind'] == 'web':
        if not a.get('rights', {}).get('creator') or not a.get('rights', {}).get('licence'): bad.append(aid + ': web asset without creator or licence')
        if a['files'] and not a.get('commons_metadata'): bad.append(aid + ': stored web original without stored Commons metadata')
        o = [f for f in a['files'] if f['variant'] == 'original']
        if o and a.get('commons_metadata', {}).get('commons_sha1') and hashlib.sha1((WS/o[0]['path']).read_bytes()).hexdigest() != a['commons_metadata']['commons_sha1']:
            bad.append(aid + ': original differs from the file Commons serves (SHA-1)')
        if re.search(r'\b(NC|ND)\b|fair use', a.get('rights', {}).get('licence', ''), re.I): bad.append(aid + ': disallowed licence')
    if a['source_kind'] == 'local_notes' and not a['reuse_status'].startswith('REFERENCE ONLY'): bad.append(aid + ': local notes not marked reference only')
    originals = [f for f in a['files'] if f['variant'] == 'original']
    for f in a['files']:
        p = WS/f['path']
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != f['sha256']:
            bad.append(aid + ': missing/changed file ' + str(p)); continue
        if f['variant'] in ('teaching', 'question', 'answer') and a['source_kind'] != 'original_graph':
            src = f.get('derived_from')
            if not src or src not in {o['path'] for o in originals}: bad.append(aid + ': variant not derived from a held original ' + f['path'])
            if not f.get('changes') or f['changes'].startswith('none'):
                bad.append(aid + ': derivative changes not disclosed ' + f['path'])
            credit = f.get('attribution') or {}
            if credit.get('changes') != f.get('changes') or credit.get('licence') != a['rights'].get('licence'):
                bad.append(aid + ': derivative credit omits edits or source licence ' + f['path'])
        if p.suffix.lower() == '.svg':
            root = ET.fromstring(p.read_bytes())
            if any(n.tag.split('}')[-1] in ('script', 'foreignObject') for n in root.iter()): bad.append('active SVG content ' + f['path'])
            if any('href' in k and not v.startswith(('#', 'data:')) for n in root.iter() for k, v in n.attrib.items()): bad.append('external SVG reference ' + f['path'])
    if a['source_kind'] == 'original_graph' and {f['variant'] for f in a['files']} - {'question', 'answer'}: bad.append(aid + ': graph with unexpected variant')
expected = {(r['requirement_id'], k) for r in reqs.values() for k in r['kinds']}
actual = {(b['requirement_id'], b['kind']) for b in bindings}
if actual != expected or len(actual) != len(bindings): bad.append('visual-kind bindings incomplete or duplicated')
for b in bindings:
    rid = b['requirement_id']
    if reqs[rid]['objective_id'] != b['objective_id']: bad.append('requirement/objective mismatch ' + rid)
    if set(b['needs']) != NEEDS[b['kind']]: bad.append(rid + ': needs for ' + b['kind'] + ' incomplete')
    for k, n in b['needs'].items():
        if n['status'] not in STATES: bad.append(f'{rid} {k}: status "{n["status"]}" implies approval')
        for c in n.get('candidates', []):
            ref = c.split(' (')[0]
            a = paths.get(ref) or by_id.get(ref)
            if not a: bad.append(f'{rid} {k}: unknown candidate {c}'); continue
            if a['source_kind'] == 'local_notes': bad.append(f'{rid} {k}: reference-only file used as a candidate')
            if a.get('hold'): bad.append(f'{rid} {k}: held asset {a["asset_id"]} used as a candidate')
            if b['objective_id'] not in a['objective_ids']: bad.append(f'{rid} {k}: candidate {a["asset_id"]} not mapped to the objective')
        if k == 'unfamiliar_example' and n['status'] != 'GAP' and len(set(n['candidates'])) < 2: bad.append(rid + ': unfamiliar example with one specimen')
        if k in ('model_drawing', 'marking_criteria') and n['status'] != 'GAP':
            if not all((paths.get(c.split(' (')[0]) or {}).get('image_type') == 'model drawing' for c in n.get('candidates', [])): bad.append(rid + ': model drawing need met by a non-drawing')
    for aid in b['candidate_asset_ids']:
        if aid not in by_id or b['objective_id'] not in by_id[aid]['objective_ids']: bad.append('candidate binding mismatch: ' + aid)
    if any(slots.get(s) != b['objective_id'] for s in b['card_slot_ids_to_review']): bad.append('slot binding mismatch ' + rid)
    if any(b['objective_id'] not in units.get(u, []) for u in b['content_unit_ids']): bad.append('unit binding mismatch ' + rid)
    if not b['content_unit_ids'] or not b['card_slot_ids_to_review']: bad.append('missing planned unit/slot binding ' + rid)
graphs = J('visuals/generated/graphs.json')['graphs']
for g in graphs:
    if g['asset_id'] not in by_id: bad.append('graph not in manifest: ' + g['asset_id'])
on_disk = {str(p.relative_to(WS)) for d in ('originals', 'variants', 'generated') for p in (WS/'visuals'/d).iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg', '.svg')}
stray = sorted(on_disk - set(paths))
if stray: bad.append('files on disk not in the manifest: ' + ', '.join(stray))
print('visual-bank integrity: ' + ('PASS' if not bad else 'FAIL'))
need_n = sum(len(b['needs']) for b in bindings)
cand = sum(n['status'] == 'candidate (unreviewed)' for b in bindings for n in b['needs'].values())
print(f'{len(assets)} asset records; {sum(len(a["files"]) for a in assets)} stored files; {len(reqs)} objectives; {len(bindings)} kind-bindings; '
      f'{cand}/{need_n} needs have an unreviewed candidate; {sum(bool(a.get("operator_approval")) for a in assets)} operator-approved assets; zero completed scientific verifications; zero requirements met; no YYeni attachments.')
for x in bad: print('  ' + x)
sys.exit(bool(bad))
