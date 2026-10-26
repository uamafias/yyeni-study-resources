"""Check every curated report finding against the cited PDF viewer page.

Adjacent-page hits are reported as failures needing a locator correction. A
keyword check confirms traceability; interpretation remains a review task.
"""
import json
import re
import subprocess
import unicodedata
from functools import lru_cache

ANCHORS = [
    [r'copper electrodes', r'take part in the reaction', r'oxygen'],
    [r'planning an investigation', r'out of sequence'],
    [r'insoluble salt', r'evaporation', r'crystallisation'],
    [r'confused the rate of reaction with time', r'lumps'],
    [r'added the two burette readings', r'instead of subtracting'],
    [r'an atom and an element', r'isotope'],
    [r'flame tests', r'lighted or glowing splint'],
    [r'isotope', r'allotrope'],
    [r'difference between the mole', r'avogadro'],
    [r'glowing splint', r'lighted splint'],
    [r'ionic equations', r'ionic half-equations', r'weakness'],
    [r'without showing working', r'wrong units'],
    [r'question 3\(d\)', r'rate of', r'position of equilibrium'],
    [r'what the apparatus is used for', r'list of apparatus'],
    [r'electrons instead of ions', r'carry charge'],
    [r'smallest answer', r'whole numbers'],
    [r'range of 0-3 marks', r'not provided'],
    [r'test for carbon dioxide', r'could not describe this test correctly'],
    [r'failed to convert', r'cubic decimetres'],
    [r'avogadro', r'mole ratio', r'1:2'],
    [r'struggled to plot the points at 2, 6 and 8 minutes', r'plots which are more than 1mm in size', r'did not balance the points'],
    [r'addition of all the masses', r'instead of subtracting'],
    [r'green', r'most candidates gave blue'],
    [r'chromatography', r'fractional distillation or crystallisation'],
    [r'reaction is constant or is in equilibrium', r'not come to an end'],
    [r'negative tests', r'positive result for chloride ions'],
    [r'a4 piece of paper with a cross', r'chromatography experiments'],
    [r'electrons for bromide ion', r'differentiate between an atom and an ion'],
    [r'drew a covalent bond instead of an ionic bond'],
    [r'used the word electrons instead of ions'],
    [r'materials for preparing', r'referred to apparatus'],
    [r'differentiate between an atom and an ion', r'could not give an explanation'],
    [r'dark blue precipitate', r'instead of dark blue solution'],
    [r'amount or drops', r'volume of hydrochloric acid'],
]


def normalise(text):
    text = unicodedata.normalize('NFKC', text)
    text = text.translate(str.maketrans({'’': "'", '‘': "'", '–': '-', '−': '-', '‐': '-'}))
    text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)
    return ' '.join(text.lower().split())


@lru_cache(maxsize=6)
def read_pages(path):
    raw = subprocess.check_output(['pdftotext', '-layout', str(path), '-'], text=True)
    return [normalise(page) for page in raw.split('\f')]


def verify_findings(findings, report_path, output_path):
    assert len(findings) == len(ANCHORS), 'Add source anchors when findings change.'
    pages = {}
    results = []
    for index, (finding, anchors) in enumerate(zip(findings, ANCHORS), 1):
        year, cited_page, paper, question, *_ = finding
        if year not in pages:
            pages[year] = read_pages(report_path(year))
        checked = []
        for page in range(max(1, cited_page - 1), min(len(pages[year]), cited_page + 1) + 1):
            text = pages[year][page - 1]
            hits = [bool(re.search(pattern, text)) for pattern in anchors]
            checked.append({'pdf_page': page, 'all_anchors_found': all(hits),
                            'matched_anchor_count': sum(hits),
                            'missing_anchors': [a for a, hit in zip(anchors, hits) if not hit]})
        exact = next(x for x in checked if x['pdf_page'] == cited_page)
        status = 'exact_page_pass' if exact['all_anchors_found'] else 'adjacent_page_only' if any(x['all_anchors_found'] for x in checked) else 'missing_source_anchors'
        results.append({'evidence_id': f'ER-6117-{year}-{index:02d}', 'paper_id': paper,
                        'question_ref': question, 'source_file': str(report_path(year)),
                        'cited_pdf_page': cited_page, 'anchors': anchors,
                        'status': status, 'checked_pages': checked})
    failures = [x for x in results if x['status'] != 'exact_page_pass']
    output_path.write_text(json.dumps({'status': 'pass' if not failures else 'fail',
        'method': 'All curated anchors must occur on the exact cited PDF viewer page. Adjacent pages are searched for diagnosis only and never silently accepted.',
        'limitation': 'Text-anchor checks confirm source location, not the correctness of a paraphrase or objective mapping.',
        'finding_count': len(results), 'failure_count': len(failures), 'findings': results}, indent=2, ensure_ascii=False) + '\n')
    if failures:
        raise ValueError('Report citation check failed: ' + ', '.join(x['evidence_id'] + ':' + x['status'] for x in failures))
    return len(results)


def verify_answer_links(alignment, report_path, output_path):
    """Check row-level locators, including continuation pages in long tables."""
    pages = {}
    results = []
    for eid, link in alignment.items():
        year = int(eid.split('-')[2])
        if year not in pages:
            pages[year] = read_pages(report_path(year))
        locator = link['source_locator']
        match = re.search(r'PDF viewer pp?\. (\d+)(?:[–-](\d+))?', locator)
        assert match, locator
        cited_pages = set(range(int(match.group(1)), int(match.group(2) or match.group(1)) + 1))
        rows = []
        for row in link['source_rows']:
            page = row['source_page']
            text_found = normalise(row['label_line']) in pages[year][page - 1]
            rows.append({'pdf_page': page, 'label_line_found': text_found,
                         'page_in_locator': page in cited_pages})
        passed = all(r['label_line_found'] and r['page_in_locator'] for r in rows)
        results.append({'evidence_id': eid, 'source_locator': locator,
                        'status': 'pass' if passed else 'fail', 'rows': rows})
    failures = [x for x in results if x['status'] != 'pass']
    output_path.write_text(json.dumps({'status': 'pass' if not failures else 'fail',
        'method': 'Each report row label must occur on its stored PDF viewer page, and that page must be included in the part locator.',
        'link_count': len(results), 'failure_count': len(failures), 'links': results}, indent=2, ensure_ascii=False) + '\n')
    if failures:
        raise ValueError('Answer-row page check failed: ' + ', '.join(x['evidence_id'] for x in failures))
    return len(results)


def verify_manual_plans(manual_guidance, report_path, output_path):
    anchors = {
        'QP-6117-2021-3-Q04-P01': 'measure initial temperature',
        'QP-6117-2022-3-Q04-P01': 'crush the flower petals',
        'QP-6117-2023-3-Q04-P01': 'pour sodium thiosulfate',
        'QP-6117-2024-3-Q05-P01': 'add equal volume',
    }
    results = []
    for eid, anchor in anchors.items():
        year = int(eid.split('-')[2])
        page = manual_guidance[eid]['report_pdf_page']
        passed = anchor in read_pages(report_path(year))[page - 1]
        results.append({'evidence_id': eid, 'pdf_page': page, 'anchor': anchor,
                        'status': 'pass' if passed else 'fail'})
    failed = [x for x in results if x['status'] == 'fail']
    output_path.write_text(json.dumps({'status': 'fail' if failed else 'pass',
        'scope': 'The four text-native manually extracted planning answer tables. Scanned 2020 answers are outside this text check.',
        'plans': results}, indent=2) + '\n')
    if failed:
        raise ValueError('Manual planning page check failed: ' + ', '.join(x['evidence_id'] for x in failed))
    return len(results)


if __name__ == '__main__':
    import build_report_evidence as build
    count = verify_findings(build.FINDINGS, build.report_path, build.WORK / 'assessment-evidence/report-citation-audit.json')
    print(f'PASS: {count} findings on exact cited PDF viewer pages')
    alignment = json.loads((build.WORK / 'assessment-evidence/report-guidance-alignment.json').read_text())['aligned_parts']
    count = verify_answer_links(alignment, build.report_path, build.WORK / 'assessment-evidence/report-answer-page-audit.json')
    print(f'PASS: {count} answer links on their cited PDF viewer pages')
