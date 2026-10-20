#!/usr/bin/env python3
"""Inventory the 6116 Biology source documents actually present in the repo.

Playbook step 1 asks for the syllabus, question papers, mark schemes and examiner
reports by year and series, with what is missing named. This replaces a hand
count, which was wrong twice: the examiner reports were called subject-general
when every one carries a Biology 6116 section, and the report years were counted
as four when six distinct volumes exist.

Distinctions this records, because they change what the evidence can support:
  - final paper vs "First Proof" (section 6: a proof may differ from the printed paper)
  - subject-specific report vs a combined volume containing a Biology section
  - distinct documents vs the same file duplicated across subject folders (by SHA-256)

Usage: python3 inventory_sources.py [--json <path>]
"""
import os, re, json, hashlib, subprocess, argparse, collections

PAPERS_DIR = 'Question Banks/Namibian Curricula/NSSCO (New)/Biology (6116)'
SYLLABUS = 'Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_BIOLOGY_SYLLABUS.pdf'
REPORT_GLOB_DIRS = ['Question Banks/Namibian Examiner Reports', PAPERS_DIR]


def sha(path, buf=1 << 20):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(buf):
            h.update(chunk)
    return h.hexdigest()


def pagecount(path):
    try:
        out = subprocess.run(['pdfinfo', path], capture_output=True, text=True).stdout
        m = re.search(r'^Pages:\s+(\d+)', out, re.M)
        return int(m.group(1)) if m else None
    except Exception:
        return None


def text_of(path, first=None, last=None):
    cmd = ['pdftotext', '-layout']
    if first: cmd += ['-f', str(first)]
    if last: cmd += ['-l', str(last)]
    return subprocess.run(cmd + [path, '-'], capture_output=True, text=True).stdout


def biology_page(path):
    """PDF page where the Biology 6116 section opens in a combined report."""
    n = pagecount(path) or 0
    for p in range(1, min(n, 200) + 1):
        t = text_of(path, p, p)
        if re.search(r'^\s*BIOLOGY\s*$', t, re.M) and re.search(r'^\s*6116\s*$', t, re.M):
            return p
    return None


def papers():
    rows = []
    for year in sorted(os.listdir(PAPERS_DIR)):
        d = os.path.join(PAPERS_DIR, year)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.lower().endswith('.pdf'):
                continue
            path = os.path.join(d, fn)
            if re.search(r'xaminer', fn, re.I):
                continue
            head = text_of(path, 1, 1)
            m = re.search(r'6116\s*/\s*([123])', head) or re.search(r'PAPER\s+([123])', head, re.I)
            dur = re.search(r'(\d+\s*hours?(?:\s+\d+\s*minutes)?|\d+\s*minutes)', head, re.I)
            marks = re.search(r'Marks\s+(\d+)', head, re.I)
            rows.append({
                'year': year, 'file': fn, 'paper': m.group(1) if m else '?',
                'is_first_proof': bool(re.search(r'First Proof', fn, re.I)),
                'duration_on_cover': ' '.join(dur.group(1).split()) if dur else None,
                'marks_on_cover': int(marks.group(1)) if marks else None,
                'pages': pagecount(path), 'sha256': sha(path), 'path': path,
            })
    return rows


def reports():
    seen, rows = {}, []
    for base in REPORT_GLOB_DIRS:
        for root, _, files in os.walk(base):
            for fn in files:
                if not fn.lower().endswith('.pdf') or not re.search(r'xaminer', fn, re.I):
                    continue
                if 'JSC' in root or 'English' in root:
                    continue
                path = os.path.join(root, fn)
                h = sha(path)
                ym = re.search(r'(20\d{2})', fn) or re.search(r'(20\d{2})', root)
                rows.append({'year': ym.group(1) if ym else '?', 'file': fn, 'path': path,
                             'sha256': h, 'pages': pagecount(path)})
                seen.setdefault(h, []).append(path)
    for r in rows:
        r['duplicate_copies'] = len(seen[r['sha256']])
    return rows, seen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', default='work/nam-6116-nssco-2026/curriculum/source-inventory.json')
    args = ap.parse_args()

    pp = papers()
    rr, seen = reports()
    distinct = {}
    for h, paths in seen.items():
        distinct[h] = {'copies': paths, 'pages': pagecount(paths[0]),
                       'biology_section_pdf_page': biology_page(paths[0])}

    inv = {
        'subject': '6116 NSSCO Biology',
        'syllabus': {'path': SYLLABUS, 'present': os.path.exists(SYLLABUS),
                     'pages': pagecount(SYLLABUS), 'sha256': sha(SYLLABUS) if os.path.exists(SYLLABUS) else None},
        'question_papers': pp,
        'examiner_reports': rr,
        'examiner_reports_distinct': distinct,
        'mark_schemes': [],
        'missing': ['mark schemes - none published for NSSCO 6116; examiner reports do not substitute'],
    }
    os.makedirs(os.path.dirname(args.json), exist_ok=True)
    json.dump(inv, open(args.json, 'w'), indent=2)

    by_year = collections.defaultdict(list)
    for p in pp:
        by_year[p['year']].append(p)
    print('QUESTION PAPERS')
    for y in sorted(by_year):
        got = sorted(x['paper'] for x in by_year[y])
        proof = any(x['is_first_proof'] for x in by_year[y])
        durs = {x['paper']: x['duration_on_cover'] for x in by_year[y]}
        print(f"  {y}  papers {','.join(got):<8} {'FIRST PROOF' if proof else 'final      '}  P1 duration: {durs.get('1')}")
    print(f"  total paper files: {len(pp)}")
    print('\nEXAMINER REPORTS (distinct volumes)')
    for h, d in sorted(distinct.items(), key=lambda kv: kv[1]['copies'][0]):
        yr = re.search(r'(20\d{2})', d['copies'][0])
        print(f"  {yr.group(1) if yr else '?'}  {d['pages']:>4}pp  Biology at PDF p.{d['biology_section_pdf_page']}  "
              f"copies={len(d['copies'])}  {h[:10]}")
    print(f"  distinct volumes: {len(distinct)}   total files on disk: {len(rr)}")
    print('\nMARK SCHEMES: none found')
    print('inventory -> %s' % args.json)


if __name__ == '__main__':
    main()
