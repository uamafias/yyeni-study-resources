"""Rebuild the local 6118 source inventory; never modify source PDFs."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / 'work/nam-6118-nssco-2026'


def inspect(path):
    data = path.read_bytes()
    assert data.startswith(b'%PDF-'), f'Not a PDF: {path}'
    info = subprocess.check_output(['pdfinfo', str(path)], text=True)
    count = int(re.search(r'^Pages:\s+(\d+)', info, re.M)[1])
    pages = subprocess.check_output(
        ['pdftotext', '-layout', str(path), '-'], text=True
    ).split('\f')
    if pages[-1] == '':
        pages.pop()
    assert len(pages) == count, (path, len(pages), count)
    return {
        'path': str(path.relative_to(ROOT)),
        'sha256': hashlib.sha256(data).hexdigest(),
        'bytes': len(data), 'pdf_pages': count,
        'extracted_characters': sum(map(len, pages)),
        'pdf_metadata': {
            key: re.search(r'^' + key + r':\s*(.*)$', info, re.M)[1]
            for key in ('CreationDate','ModDate','Creator','Producer')
            if re.search(r'^' + key + r':\s*(.*)$', info, re.M)
        },
    }, pages


def main():
    entries = []
    row, pages = inspect(ROOT / 'Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_Physics_syllabus.pdf')
    assert 'SYLLABUS CODE: 6118' in pages[0]
    row.update(kind='syllabus', edition=2018, implementation_year=2019,
               first_examination_year=2020, current_for_2026='Operator-approved working source for the 2026 cohort on 2026-10-31; no independent NIED cohort-validity statement established',
               cover_quote='SYLLABUS CODE: 6118', cover_pdf_page=1)
    currency=json.loads((WORK/'curriculum/syllabus-currency.json').read_text())
    assert row['sha256']==currency['local_sha256'], 'Publisher comparison is for a different local PDF'
    row['local_origin']={
        'method': 'manual addition, as reported in operator-forwarded review feedback',
        'harvest_log': '_harvest/logs/harvest_log.csv',
        'matching_harvest_entry_found': False,
        'origin_date': None, 'original_download_url': None, 'person_who_added_it': None,
        'limit': 'The publisher verification URL is not evidence of the original acquisition URL. Lack of a harvest entry alone does not identify who added the file or when.',
    }
    row['publisher_verification']={
        'catalogue_url': currency['catalogue_url'],
        'catalogue_link_text': currency['catalogue_link_text'],
        'pdf_url': currency['official_pdf_url'],
        'retrieved_at_utc': currency['retrieved_at_utc'],
        'official_sha256': currency['official_sha256'],
        'same_binary': currency['binary_equal'],
        'complete_extracted_layout_text_equal': currency['pdftotext_layout_output_equal'],
        'evidence_file': 'review/source-provenance-audit.json',
        'cohort_validity': 'No independent NIED cohort-validity statement established; operator approved use as the working source on 2026-10-31. External-authority caveat retained, not a progression gate.',
    }
    row['modification_caveat']={
        'local_modification_date': '2024-04-26T16:09:42+02:00',
        'publication_edition': 2018,
        'cause_of_modification': 'Likely local re-save/reprocessing, an inference from the different Producer metadata; exact processing history unknown.',
        'content_changed_since_2018': 'unknown; no independently archived historical baseline comparison performed',
        'comparison_limit': 'Complete extracted text matches the publisher PDF retrieved on the stated date. All 52 current page images, including diagrams, are pixel-identical at 144 dpi. Historical changes and hidden/non-rendered structures are not established. PDF ModDate is not a syllabus amendment or validity statement.',
    }
    comparison=json.loads((WORK/'review/syllabus-page-image-comparison.json').read_text())
    assert comparison['local_sha256']==row['sha256']
    assert comparison['publisher_sha256']==currency['official_sha256']
    row['page_image_comparison']={key:comparison[key] for key in (
        'checked_at_utc','pages_compared','pixel_equal_pages','differing_pages','method','scope_limit')}
    row['page_image_comparison']['evidence_file']='review/syllabus-page-image-comparison.json'
    row['publisher_reupload_inference']=currency['publisher_reupload_inference']
    row['binary_difference_explanation']=currency['binary_difference_explanation']
    entries.append(row)
    for path in sorted((ROOT / 'Question Banks/Namibian Curricula/NSSCO (New)/Physics').rglob('*.pdf')):
        row, pages = inspect(path)
        cover = pages[0]
        identity = re.search(r'6118/([123])/(\d{2})', cover)
        assert identity, path
        year, paper = 2000 + int(identity[2]), int(identity[1])
        assert year == int(path.parent.name), path
        duration = next(line.strip() for line in cover.splitlines() if re.match(r'\s*PAPER [123]', line))
        row.update(kind='question_paper', year=year, paper=paper,
                   series='not stated on inspected cover',
                   cover_identity=identity[0], cover_pdf_page=1,
                   duration_quote=duration,
                   first_proof_filename='first proof' in path.name.lower(),
                   final_print_status='not confirmed' if 'first proof' in path.name.lower() else 'not labelled First Proof')
        if year == 2025:
            row.update(intake_date='2026-10-30',
                       acquired_via='User-supplied ChatGPT Work mode download',
                       placement_authority='User supplied the files and accepted their placement in Question Banks in the forwarded review feedback on 2026-10-30; Codex performed the byte-for-byte copy, not a source download.',
                       intake_source_path='/Users/yyeniai/Downloads/NSSCO 2025 Physics/' + path.name,
                       download_url='not supplied; not independently established')
        entries.append(row)
    for path in sorted((ROOT / 'Question Banks/Namibian Examiner Reports/NSSCO (New) ').rglob('*.pdf')):
        row, pages = inspect(path)
        start = next(i for i, p in enumerate(pages) if re.search(r'PHYSICS\s*6118', p, re.I))
        # The next subject in these six volumes is Woodwork 6190.
        end = next(i for i in range(start + 1, len(pages)) if re.match(r'\s*WOODWORK\s+6190', pages[i], re.I))
        section = pages[start:end]
        headers = []
        for i, page in enumerate(section, start + 1):
            match = re.match(r'\s*(?:PHYSICS\s*)?6118\s*Paper\s*([123])', page, re.I)
            if match:
                headers.append({'paper': int(match[1]), 'pdf_page': i})
        row.update(kind='combined_examiner_report', year=int(path.parent.name),
                   physics_pdf_pages={'first': start + 1, 'last': end},
                   physics_heading_quote='PHYSICS / 6118', paper_headers=headers,
                   marking_guidance_candidate_pdf_pages=[
                       i for i, p in enumerate(section, start + 1)
                       if re.search(r'mark\s*scheme|additional\s*guidance|marking\s*(?:points|guidance)', p, re.I)
                   ],
                   evidence_note='Embedded keys/guidance require part-level verification at Step 3; not a complete stand-alone mark scheme.')
        key_headers=[h for h in headers if h['paper']==1]
        row['evidence_inventory']={
            'scope': 'Header/key-page intake classification only; no part-level corpus mining.',
            'key': [dict(paper=1,pdf_page=h['pdf_page'],provenance='examiner_report',
                         verbatim_excerpt='\n'.join(pages[h['pdf_page']-1].strip().splitlines()[:24])) for h in key_headers],
            'commentary': [dict(paper=h['paper'],pdf_page=h['pdf_page'],provenance='examiner_report',
                                verbatim_excerpt='\n'.join(pages[h['pdf_page']-1].strip().splitlines()[:12])) for h in headers if h['paper']!=1],
            'inference': dict(provenance='judgement',status='No inferred marking allocations authored at this stage; any future inference must be labelled separately and must not claim official credit.'),
            'marking_keyword_scan_limit': 'Candidate-page keyword matches are not verified marking rows. Zero matches does not mean no answer key or no usable marking evidence. Detailed marking rows and their completeness remain unassessed.',
        }
        entries.append(row)
    assert len(entries) == 25
    assert len({r['sha256'] for r in entries}) == len(entries), 'Duplicate source bytes'
    actual = {(r['year'], r['paper']) for r in entries if r['kind'] == 'question_paper'}
    assert actual == {(year, paper) for year in range(2020, 2026) for paper in (1, 2, 3)}
    result = {
        'syllabus_code': '6118', 'subject': 'Physics', 'board': 'Namibia NSSCO',
        'inventory_date': '2026-10-30', 'page_number_convention': 'one-based PDF viewer pages',
        'scope': 'Local official-source inventory with dated live publisher-link/text verification; no confirmed cohort validity or substantive corpus analysis.',
        'summary': {'syllabuses': 1, 'question_papers': 18, 'examiner_report_volumes': 6,
                    'standalone_mark_schemes_found': 0},
        'missing': ['Stand-alone mark schemes for 2020-2025',
                    'Confirmation that the 2018 syllabus governs the intended 2026 cohort'],
        'operator_source_decision': {
            'date': '2026-10-30', 'approved_by': 'Lotto N. Nanghonda Jr.',
            'verbatim': "we'll use the examiner's reports as the memos. let's move on to the next step",
            'decision': 'Examiner reports approved as marking evidence/memos on 2026-10-30; working syllabus and Step 2 tables approved for progression on 2026-10-31.',
            'limits': 'Approval does not assert complete marking coverage or independent NIED confirmation of 2026 validity. Unsupported marking inferences must be labelled judgement. See curriculum/operator-decisions.json for the progression decision and explicit non-major duration waiver.',
        },
        'entries': entries,
    }
    result['paper_1_duration_evidence']={
        'syllabus_minutes': 45,
        'syllabus_source': 'curriculum/syllabus-facts.json: papers[0].duration, printed p.38 / PDF p.41',
        'different_duration_evidence': [
            dict(year=r['year'],minutes=60,path=r['path'],pdf_page=1,
                 provenance='question_paper_cover',verbatim=r['duration_quote'])
            for r in entries if r['kind']=='question_paper' and r['paper']==1 and r['year'] in (2021,2025)
        ],
        'limit': 'The 2021 and 2025 one-hour covers are the only held evidence of a different Paper 1 duration. No amendment, circular or 2026 governing duration is established. No inference about 2026 is made.',
        'operator_resolution': 'Explicitly waived by Lotto on 2026-10-31 as a non-major, non-blocking issue; neither duration adopted as governing 2026 timing.',
    }
    dest = WORK / 'curriculum/source-inventory.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps(result['summary']))
    for row in entries:
        if row['kind'] == 'combined_examiner_report':
            print(row['year'], row['physics_pdf_pages'], row['paper_headers'],
                  'marking candidates', row['marking_guidance_candidate_pdf_pages'])


if __name__ == '__main__':
    main()
