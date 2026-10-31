#!/usr/bin/env python3
"""Build the staged Biology visual bank: manifest, per-need bindings, source inventory and INDEX. No YYeni writes.

Inputs
  planning/visual_bank_sources.json              seeds (Codex's first pass, re-inspected), incl. local-notes extractions
  planning/visual_candidates/candidates_*.json   Commons candidates found and inspected by the sourcing passes
  visuals/generated/graphs.json                  project-owned graphs from make_graphs_6116.py
  visuals/variants/variants.json                 teaching / question / answer overlays from make_visual_variants.py

--acquire  extracts the local-notes rasters (Poppler) and writes a harvest manifest for every web original and its
           Commons metadata, then runs the shared harvester (`harvest run`). No scraping code lives here.
Without it, metadata is rebuilt from the files already held. Nothing here marks a review complete:
a candidate is not an approved image, and a located image does not meet a requirement.
"""
import argparse, collections, csv, glob, hashlib, json, pathlib, re, subprocess, urllib.parse

WS = pathlib.Path('work/nam-6116-nssco-2026')
BANK = WS / 'visuals'
J = lambda p: json.loads(pathlib.Path(p).read_text())
HARVEST_MANIFEST = pathlib.Path('_harvest/manifests/nam-6116-visual-bank.csv')
ALLOWED = re.compile(r'^(CC0( 1\.0)?|CC BY(-SA)? \d\.\d( [A-Za-z-]+)?|Public domain|PD[- ].*)$', re.I)


def write(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inventory_pdf(p):
    result = subprocess.run(['pdfimages', '-list', str(p)], capture_output=True, text=True, check=True)
    pages = subprocess.run(['pdftotext', '-layout', str(p), '-'], capture_output=True, text=True, check=True).stdout.split('\f')
    if pages and not pages[-1].strip(): pages.pop()
    rasters = collections.Counter()
    for line in result.stdout.splitlines()[2:]:
        v = line.split()
        if len(v) > 3 and v[0].isdigit() and v[2] == 'image': rasters[int(v[0])] += 1
    rows = []
    terms = ['microscope', 'cell', 'leaf', 'root', 'stem', 'blood', 'heart', 'villus', 'flower', 'mitosis', 'meiosis', 'osmosis', 'graph', 'eye', 'neurone', 'spinal', 'alimentary']
    for n, text in enumerate(pages, 1):
        tags = [t for t in terms if re.search(r'\b' + re.escape(t) + r'\w*\b', text, re.I)]
        # These are discovery tags, never a semantic coverage decision. No question text is copied.
        if rasters[n] or re.search(r'\b(?:Fig\.?|diagram|photomicrograph|cross.section)\b', text, re.I):
            rows.append({'pdf_page': n, 'embedded_rasters': rasters[n], 'discovery_tags': tags,
                         'mapping_status': 'page-text proposal; inspect the figure before selecting',
                         'vector_figures_may_exist': True})
    return {'path': str(p), 'sha256': digest(p), 'pages': len(pages), 'candidate_pages': rows}


def commons_title(url):
    return urllib.parse.unquote(url.rsplit('/wiki/', 1)[1]).replace('_', ' ')


def metadata_url(a):
    return ('https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo'
            '&iiprop=url|size|sha1|extmetadata&titles=' + urllib.parse.quote(commons_title(a['source_url'])))


def original_path(a):
    return BANK / 'originals' / (a['asset_id'] + pathlib.Path(urllib.parse.urlparse(a['download_url']).path).suffix.lower())


def provenance_path(a):
    return BANK / 'provenance' / (a['asset_id'] + '.commons.json')


def load_assets():
    """Seeds plus sourcing-pass candidates; the same original file is never held twice."""
    seeds = J(WS / 'planning/visual_bank_sources.json')['assets']
    seen = {a['download_url'] for a in seeds if a.get('download_url')}
    ids = {a['asset_id'] for a in seeds}
    out = [dict(a, found_by='seed: Codex first pass, re-inspected 2026-10-18') for a in seeds]
    for f in sorted(glob.glob(str(WS / 'planning/visual_candidates/candidates_*.json'))):
        for c in J(f):
            if c.get('download_url') in seen or c['asset_id'] in ids:
                continue
            seen.add(c.get('download_url')); ids.add(c['asset_id'])
            out.append(dict(c, found_by='sourcing pass: ' + pathlib.Path(f).name))
    review = J(WS / 'planning/visual_candidate_review.json')
    for a in out:
        if a['asset_id'] in review['holds']:
            a['hold'] = review['holds'][a['asset_id']]
        if a['asset_id'] in review['notes']:
            a['suitability_concerns'] = a.get('suitability_concerns', []) + ['Curator: ' + review['notes'][a['asset_id']]]
    return out


def acquire(assets):
    # Local notes: extract the embedded rasters of the named page. Reference only.
    for a in assets:
        if a['source_kind'] == 'local_notes':
            prefix = BANK / 'reference-only' / a['asset_id']
            if not list(prefix.parent.glob(prefix.name + '-*.png')):
                subprocess.run(['pdfimages', '-f', str(a['pdf_page']), '-l', str(a['pdf_page']), '-png',
                                a['source_path'], str(prefix)], check=True)
    # Web originals and their Commons metadata go through the shared harvester (CLAUDE.md: no scraping code here).
    rows = []
    for a in assets:
        if a['source_kind'] != 'web': continue
        if not original_path(a).exists():
            rows.append({'url': a['download_url'], 'target_path': str(original_path(a)), 'mode': 'http', 'note': a['asset_id'] + ' original'})
        if not provenance_path(a).exists():
            rows.append({'url': metadata_url(a), 'target_path': str(provenance_path(a)), 'mode': 'http', 'note': a['asset_id'] + ' Commons metadata'})
    if not rows:
        return
    HARVEST_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with HARVEST_MANIFEST.open('w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['url', 'target_path', 'mode', 'note']); w.writeheader(); w.writerows(rows)
    subprocess.run(['harvest', 'run', '--no-escalate', '--workers', '1', str(HARVEST_MANIFEST)], check=False)


def provenance(a):
    """Rights as stated by Commons for this file, read from the stored API response."""
    p = provenance_path(a)
    if not p.exists():
        return None
    try:
        pages = J(p)['query']['pages']
        info = next(iter(pages.values()))['imageinfo'][0]
    except (KeyError, StopIteration, ValueError):
        return {'error': 'metadata file unreadable; re-acquire'}
    md = {k: v.get('value') for k, v in info.get('extmetadata', {}).items()}
    strip = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', str(s or ''))).strip()
    return {'creator': strip(md.get('Artist')), 'licence': md.get('LicenseShortName'), 'licence_url': md.get('LicenseUrl'),
            'credit': strip(md.get('Credit'))[:300], 'description': strip(md.get('ImageDescription'))[:600],
            'width': info.get('width'), 'height': info.get('height'), 'commons_sha1': info.get('sha1'),
            'metadata_file': str(p.relative_to(WS))}


def reuse_status(a, prov):
    if a['source_kind'] == 'original_graph':
        return 'project-owned (generated from declared data)'
    if a['source_kind'] == 'local_notes':
        return 'REFERENCE ONLY: rights unknown; may guide sourcing or redrawing, never released'
    if prov and prov.get('error'):
        return 'CHECK: ' + prov['error']
    lic = ((prov or {}).get('licence') or a.get('rights', {}).get('licence') or '').strip()
    if not ALLOWED.match(lic):
        return 'BLOCKED: licence not confirmed as CC0, PD, CC BY or CC BY-SA (%s)' % (lic or 'none recorded')
    recorded = a.get('rights', {}).get('licence')
    norm = lambda x: re.sub(r'^CC0 1\.0$', 'CC0', (x or '').strip(), flags=re.I)
    if prov and recorded and norm(prov.get('licence')) != norm(recorded):
        return 'CHECK: Commons states %s, record says %s' % (prov.get('licence'), recorded)
    return 'licensed %s%s; attribution text and file-page review pending' % (lic, '' if prov else ' (as recorded; Commons metadata not yet stored)')


def releasable(a):
    """May serve a need once reviewed. Held assets (identity or content in doubt) are listed, never counted."""
    return a['source_kind'] in ('web', 'original_graph') and not a['reuse_status'].startswith('BLOCKED') and not a.get('hold')


def files_of(a, variant):
    return [f['path'] for f in a['files'] if f['variant'] == variant
            and not f.get('selection_review', '').startswith(('EXCLUDE', 'REJECT'))]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--acquire', action='store_true'); args = ap.parse_args()
    for d in ['originals', 'generated', 'reference-only', 'provenance', 'variants']: (BANK / d).mkdir(parents=True, exist_ok=True)
    assets = load_assets()
    if args.acquire:
        acquire(assets)

    source_inventory = J(WS / 'curriculum/source-inventory.json')
    pdfs = [pathlib.Path(x['path']) for x in source_inventory['question_papers']]
    pdfs += sorted(pathlib.Path('Revision Notes/NSSCO/NSSCO Biology (6116)').glob('*.pdf'))
    inventories = [inventory_pdf(p) for p in pdfs]
    write(BANK / 'source-inventory.json', {'rule': 'All local NSSCO Biology notes and the 18 papers were scanned. Raster counts omit vector-only figures. Tags are unreviewed discovery proposals. Examination figures are reference only: they show which views are examined and are never reproduced.', 'sources': inventories})

    variants = J(BANK / 'variants/variants.json')['variants'] if (BANK / 'variants/variants.json').exists() else []
    vby = collections.defaultdict(list)
    for v in variants: vby[v['asset_id']].append(v)

    out = []
    for a in assets:
        a = dict(a)
        if a['source_kind'] == 'web':
            targets = [original_path(a)] if original_path(a).exists() else []
        else:
            prefix = BANK / 'reference-only' / a['asset_id']
            targets = sorted(prefix.parent.glob(prefix.name + '-*.png'))
        a['files'] = [{'path': str(p.relative_to(WS)), 'sha256': digest(p), 'variant': 'original'} for p in targets]
        for f in a['files']:
            disp = a.get('file_dispositions', {}).get(pathlib.Path(f['path']).name)
            if disp: f['selection_review'] = disp
        for v in vby.get(a['asset_id'], []):
            if (WS / v['path']).exists():
                a['files'].append({'path': v['path'], 'sha256': digest(WS / v['path']), 'variant': v['variant'],
                                   'derived_from': v['derived_from'], 'label_review': v['label_review'],
                                   'changes': v['changes'], 'covered_regions': v.get('covered_regions', []),
                                   'attribution': {'creator': a['rights'].get('creator'),
                                                   'source_url': a.get('source_url'),
                                                   'licence': a['rights'].get('licence'),
                                                   'licence_url': a['rights'].get('licence_url'),
                                                   'changes': v['changes'],
                                                   'status': 'draft; file-page and reuse-terms review pending'}})
        for f in a['files']:
            if f['variant'] == 'original':
                f['changes'] = 'none; original file preserved'
        if vby.get(a['asset_id']):
            a['rights'] = dict(a['rights'], changes='Original unchanged; derived variants have labels/leader marks and any recorded masks or key panel. See each file changes and attribution fields.')
        prov = provenance(a) if a['source_kind'] == 'web' else None
        if prov: a['commons_metadata'] = prov
        a['reuse_status'] = reuse_status(a, prov)
        a['acquisition_status'] = ('stored' if targets else
                                   'source located; not stored (acquisition pending)' if a['source_kind'] == 'web' else
                                   'not extracted')
        a['scientific_review'] = {'status': 'pending', 'reviewer': None, 'date': None}
        a['learner_release_status'] = 'held: scientific accuracy and reuse-terms review required'
        a['yyeni_status'] = 'not attached; YYeni image display and learner image/drawing submission unavailable until demonstrated'
        out.append(a)

    for g in J(BANK / 'generated/graphs.json')['graphs']:
        files = [dict(f, variant={'Q': 'question', 'A': 'answer'}[k]) for k, fs in g['variants'].items() for f in fs]
        for f in files:
            if digest(WS / f['path']) != f['sha256']: raise SystemExit('graph file changed since make_graphs: ' + f['path'])
        graph_asset = {'asset_id': g['asset_id'], 'title': g['title'], 'source_kind': 'original_graph',
                    'source_path': 'planning/make_graphs_6116.py', 'source_locator': 'visuals/generated/graphs.json; data declared in the generator',
                    'data_kind': g['data_kind'], 'data_source': g['data_source'],
                    'objective_ids': g['objective_ids'], 'kinds': ['graph'], 'roles': ['question', 'answer'],
                    'intended_uses': g['uses'], 'files': files, 'acquisition_status': 'stored',
                    'rights': {'status': 'project-owned', 'creator': 'YYeni (generated)'},
                    'reuse_status': reuse_status({'source_kind': 'original_graph'}, None),
                    'suitability_concerns': g.get('flags', []),
                    'scientific_review': {'status': 'pending', 'reviewer': None, 'date': None},
                    'learner_release_status': 'held: data and shape review required',
                    'yyeni_status': 'not attached; YYeni image display unavailable until demonstrated'}
        hold = J(WS / 'planning/visual_candidate_review.json')['holds'].get(g['asset_id'])
        if hold:
            graph_asset['hold'] = hold
        out.append(graph_asset)

    approvals = J(WS / 'planning/operator_approvals.json')
    for a in out:
        approved = approvals['images']['assets'].get(a['asset_id'])
        if approved:
            actual = {f['path']: f['sha256'] for f in a['files']}
            if actual != approved['files']:
                raise SystemExit('approved image files changed; approval does not cover this version: ' + a['asset_id'])
            a['operator_approval'] = approved

    write(BANK / 'manifest.json', {'generated_by': str(WS / 'planning/build_visual_bank.py'),
                                   'status': 'plan and all banked images operator-approved; documented verification/rights/delivery holds retained; zero requirements met',
                                   'assets': out})
    bindings = bind(out)
    write(BANK / 'bindings.json', {'rule': 'One record per requirement × kind. Each need lists the candidate files that could serve it. "candidate (unreviewed)" means located, never met. Reference-only files never satisfy a need. Text descriptions never satisfy a visual need.', 'bindings': bindings})
    index(out, bindings, inventories)
    print(json.dumps(summary(out, bindings, inventories)))


def bind(assets):
    reqs = J(WS / 'curriculum/visual-requirements.json')['requirements']
    units, slots = [], []
    for topic in range(1, 6):
        wo = J(WS / f'topics/{topic}/work_order.json'); units += wo['content_units']; slots += wo['item_slots']
    out = []
    for req in reqs:
        oid = req['objective_id']
        for kind in req['kinds']:
            pool = [a for a in assets if oid in a['objective_ids'] and kind in a['kinds']]
            if kind == 'stimulus_image':   # a labelled diagram mapped to the objective can still teach it
                pool += [a for a in assets if oid in a['objective_ids'] and 'teaching_diagram' in a['kinds'] and a not in pool]
            usable = [a for a in pool if releasable(a)]
            needs = {}

            def need(key, cands, prepare=None, gap=None):
                if cands:
                    needs[key] = {'status': 'candidate (unreviewed)', 'candidates': cands}
                elif prepare:
                    needs[key] = {'status': 'variant to prepare', 'from': prepare}
                else:
                    needs[key] = {'status': 'GAP', 'gap': gap}

            if kind == 'stimulus_image':
                authentic = [a for a in usable if kind in a['kinds'] and 'diagram' not in a.get('image_type', '') and a['files']]
                labelled = [a for a in usable if a.get('has_labels') and a['files']]
                unlab = [a for a in authentic if a.get('has_labels') is False]
                need('teaching', [p for a in usable for p in files_of(a, 'teaching')] or
                     [p + ' (labelled original)' for a in labelled for p in files_of(a, 'original')],
                     prepare=[a['asset_id'] for a in unlab], gap='no labelled teaching image located')
                need('question', [p for a in usable for p in files_of(a, 'question')] or
                     [p + ' (unlabelled original)' for a in unlab for p in files_of(a, 'original')],
                     gap='no unlabelled authentic image stored' + ('; labelled originals only, whose labels would need covering' if labelled else ''))
                need('answer', [p for a in usable for p in files_of(a, 'answer')],
                     prepare=[a['asset_id'] for a in unlab], gap='needs a question image first')
                distinct = sorted({a['asset_id'] for a in authentic})
                need('unfamiliar_example', distinct if len(distinct) >= 2 else [],
                     gap='%d authentic specimen stored; recognition practice needs at least two different specimens' % len(distinct))
            elif kind == 'teaching_diagram':
                need('teaching', [p for a in usable for p in files_of(a, 'teaching')] or
                     [p + (' (labelled original)' if a.get('has_labels') else ' (unlabelled original; labels to add)')
                      for a in usable for p in files_of(a, 'original')],
                     gap='no licensed or original diagram stored')
            elif kind == 'model_drawing':
                need('model_drawing', [p for a in usable if a.get('image_type') == 'model drawing' for p in files_of(a, 'original')],
                     gap='no model drawing; a photograph or textbook diagram does not show the expected learner drawing')
                need('marking_criteria', [], gap='drawing criteria (clear outline, proportion, no shading, labels, magnification) to write with the model')
            elif kind == 'graph':
                need('question', [p for a in usable for p in files_of(a, 'question')], gap='no question graph generated')
                need('answer', [p for a in usable for p in files_of(a, 'answer')], gap='no answer graph generated')
            states = [n['status'] for n in needs.values()]
            first = lambda *ks: next((needs[k]['status'] for k in ks if k in needs), 'not applicable')
            out.append({'requirement_id': req['requirement_id'], 'objective_id': oid, 'kind': kind,
                        'needs': needs,
                        'candidate_asset_ids': [a['asset_id'] for a in usable],
                        'reference_only_ids': [a['asset_id'] for a in pool if a['source_kind'] == 'local_notes'],
                        'held_ids': {a['asset_id']: a['hold'] for a in pool if a.get('hold')},
                        'structures_missing_in_candidates': sorted({m for a in usable for m in a.get('structures_missing', [])}),
                        'flags': sorted({c for a in usable for c in a.get('suitability_concerns', [])
                                         if re.search(r'uncertain|wrong|conflict|no lymphocyte|omit|not visible', c, re.I)}),
                        'intended_use': {'notes': first('teaching', 'model_drawing', 'answer'),
                                         'activity': first('question', 'model_drawing', 'teaching'),
                                         'question_side': first('question'),
                                         'answer_side': first('answer', 'model_drawing')},
                        'content_unit_ids': [u['unit_id'] for u in units if oid in u['objective_ids']],
                        'card_slot_ids_to_review': [s['slot'] for s in slots if s['objective_id'] == oid],
                        'note_block_id': None, 'activity_id': None,
                        'status': ('every need has a candidate (unreviewed)' if all(s == 'candidate (unreviewed)' for s in states)
                                   else 'GAP' if all(s == 'GAP' for s in states) else 'partial'),
                        'attachment_status': 'planned only; no learner card changed'})
    return out


def summary(assets, bindings, inventories):
    return {'source_pdfs': len(inventories), 'candidate_pages': sum(len(x['candidate_pages']) for x in inventories),
            'asset_records': len(assets),
            'by_source': dict(collections.Counter(a['source_kind'] for a in assets)),
            'stored_files': sum(len(a['files']) for a in assets),
            'web_not_stored': [a['asset_id'] for a in assets if a['source_kind'] == 'web' and not a['files']],
            'blocked_or_check': [a['asset_id'] for a in assets if a['reuse_status'].startswith(('BLOCKED', 'CHECK'))],
            'held_assets': [a['asset_id'] for a in assets if a.get('hold')],
            'kind_bindings': len(bindings), 'binding_status': dict(collections.Counter(b['status'] for b in bindings)),
            'needs': dict(collections.Counter(n['status'] for b in bindings for n in b['needs'].values())),
            'operator_approved_images': sum(bool(a.get('operator_approval')) for a in assets), 'scientifically_verified_images': 0, 'approved_images': sum(bool(a.get('operator_approval')) for a in assets), 'requirements_met': 0}


def index(assets, bindings, inventories):
    s = summary(assets, bindings, inventories)
    L = ['# Biology 6116 visual bank', '',
         'Plan approved by Lotto, 2026-10-18. The originally banked 254 image assets are operator-approved at their recorded file hashes. New item-specific graphs remain unapproved. Authored resources are in review; scientific verification and learner delivery remain separate.', '',
         '**Counts.** %d asset records (%s). %d stored files. %d web originals not yet stored. %d with a licence to block or check. '
         '%d requirement × kind bindings: %s. Needs: %s. **Operator-approved image assets: %d. Scientific verification completed: 0. Requirements met: 0.**' % (
             s['asset_records'], ', '.join(f'{k} {v}' for k, v in s['by_source'].items()), s['stored_files'],
             len(s['web_not_stored']), len(s['blocked_or_check']), s['kind_bindings'],
             ', '.join(f'{k} {v}' for k, v in s['binding_status'].items()), ', '.join(f'{k} {v}' for k, v in s['needs'].items()),
             s['operator_approved_images']), '',
         '## Three separate stages', '',
         '1. **Preparation (now).** Locate, store and map. Graphs come from `planning/make_graphs_6116.py`, which reuses the plotting approach of `publish/cie-0455-igcse-2026/diagrams/make_diagrams_0455.py`. Micrographs and anatomical images are authentic, never generated.',
         '2. **Approval (before release).** A Biology teacher checks identity, orientation, label positions, scale and syllabus scope. Reuse terms and attribution are checked against the file page. Each check is recorded with a name and date in `manifest.json`. None has been done.',
         '3. **Delivery (blocked).** Current YYeni connector contracts expose card-side image asset fields and an attach action; actual image display and learner drawing or image submission remain undemonstrated. No card has been switched from a text task to a visual task.', '',
         '## Files', '',
         '- `manifest.json`: every asset, with source and page, creator, licence, reuse status, objectives, roles, inspection notes, scale, hashes and review state.',
         '- `bindings.json`: requirement × kind → needs (teaching / question / answer / unfamiliar example / model drawing) → candidate files, plus missing structures, flags, content units and card slots.',
         '- `source-inventory.json`: every local notes PDF and question paper, with candidate pages. Exam figures are reference only.',
         '- `originals/`: unmodified external originals. Never edited.',
         '- `variants/`: teaching, neutral-letter question and labelled answer overlays derived from originals; label positions are in `planning/visual_labels.json`.',
         '- `reference-only/`: extractions from local notes. Rights are unknown, so these are never released.',
         '- `provenance/`: Commons API metadata stored for each web original, fetched through the harvester (`_harvest/manifests/nam-6116-visual-bank.csv`).',
         '- `generated/`: project-owned graphs (question and answer variants) and `graphs.json`.', '',
         '## Rules applied', '',
         '- An image that is found is not therefore accurate, reusable or sufficient. Every record stays `candidate (unreviewed)`.',
         '- Originals stay untouched. Labelled teaching images, neutral-label question images and labelled answers are separate files.',
         '- Scale bars are preserved. A doubtful magnification or scale is flagged and never used for a calculation.',
         '- An unfamiliar-example need is met only by a second, different authentic specimen.',
         '- A model-drawing need is a gap until a model drawing and its criteria exist. A photograph does not substitute.',
         '- A text description never completes a visual objective.', '',
         '## Assets', '', '| Asset | Title | Source | Reuse | Files | Roles | Flags |', '|---|---|---|---|---|---|---|']
    hold_lines = ['## Explicit holds (excluded from candidate needs)', '', '| Asset | Reason |', '|---|---|']
    hold_lines += [f"| {a['asset_id']} | {a['hold']} |" for a in assets if a.get('hold')]
    at = L.index('## Assets')
    L[at:at] = hold_lines + ['']
    for a in assets:
        flags = '; '.join(c for c in a.get('suitability_concerns', [])
                          if re.search(r'WRONG|UNCERTAIN|conflict|no lymphocyte|omit|REJECT', c, re.I))
        flags = (flags[:200] + '…') if len(flags) > 200 else flags
        L.append(f"| {a['asset_id']} | {a['title']} | {a['source_kind']} | {a['reuse_status'].split(';')[0]} | {len(a['files'])} | {', '.join(a.get('roles', []))} | {flags} |")
    L += ['', '## Requirements and gaps', '', '| Requirement | Kind | Status | Needs | Missing in candidates |', '|---|---|---|---|---|']
    for b in bindings:
        nd = '; '.join(f"{k}: {v['status']}" for k, v in b['needs'].items())
        miss = ', '.join(b['structures_missing_in_candidates'])
        L.append(f"| {b['requirement_id']} | {b['kind']} | {b['status']} | {nd} | {miss[:140]} |")
    (BANK / 'INDEX.md').write_text('\n'.join(L) + '\n')


if __name__ == '__main__':
    main()
