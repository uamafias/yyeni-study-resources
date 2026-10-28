"""Extract question-comment spans; retain originals internally for audit."""
import json
import re
from pathlib import Path

WS = Path(__file__).resolve().parents[1]
OUT = WS / 'assessment-evidence'
TEXT = OUT / 'extracted'

PERFORMANCE = r'(?:Well answered|Fairly(?: well)? answered|Poorly answered|Partially answered|Moderately answered|Not well answered|Most learners|Majority|The majority|This question|Was not well answered|Was fairly answered|On average|Some learners|It was evident|In this question)'
REF = r'(?:(?P<main>\d{1,2})[ \t]*(?:\((?P<letter>[a-h])\)[ \t]*)?(?:\((?P<roman>[ivx]+)\)[ \t]*)?|\((?P<letter_only>[a-h])\)[ \t]*(?:\((?P<roman2>[ivx]+)\)[ \t]*)?|\((?P<roman_only>[ivx]+)\)[ \t]*)'
RX = re.compile(r'(?m)^[ \t]*' + REF + r'(?:\n[ \t]*)?(?=' + PERFORMANCE + r')', re.I)
STOP = re.compile(r'^(?:Answers?\b|Yes,|Yes they|Functions$|Private customers$|In favour$|No,|Q Answer|Question Answer|Kn\b|Ap\b|An\b|Ev\b|With the help|Use |Using |Except |According |[•\-]|\d+$|(?:Analyse|Calculate|Define|Describe|Discuss|Evaluate|Explain|Give|Identify|Justify|Outline|State|Suggest|What|Why|How|Who|Which|Name|List|Write|Consider|Assess|Comment|Distinguish|Examine|Advise)\b)')

questions = json.loads((OUT / 'question-parts-draft.json').read_text())
qlookup = {(q['year'], q['paper_id'], q['question_ref']): q for q in questions}
findings = []
blocks = []
for year in range(2020, 2025):
    raw = '\n'.join(re.sub(r'[ \t]+', ' ', l) for l in (TEXT / f'{year}-ER-plain.txt').read_text().splitlines())
    pages = list(re.finditer(r'=== SOURCE PDF PAGE (\d+) ===', raw))
    paper2 = raw.index('Paper 2')
    for paper, start, end in [('1', 0, paper2), ('2', paper2, len(raw))]:
        section = raw[start:end]
        matches = list(RX.finditer(section))
        main = None
        letter = roman = ''
        for k, m in enumerate(matches):
            if m['main']:
                main = m['main']
                letter, roman = m['letter'] or '', m['roman'] or ''
            elif m['letter_only']:
                letter, roman = m['letter_only'], m['roman2'] or ''
            elif m['roman_only']:
                roman = m['roman_only']
            if main is None:
                continue
            ref = main + (f'({letter})' if letter else '') + (f'({roman})' if roman else '')
            block = section[m.end():matches[k + 1].start() if k + 1 < len(matches) else len(section)]
            block = block.split('POSITIVE SUGGESTIONS TO TEACHERS')[0]
            absolute = start + m.start()
            pdf_page = max(int(pg[1]) for pg in pages if pg.start() < absolute)
            lines = block.splitlines()
            comment = []
            for l in lines:
                l = re.sub(r'\s+', ' ', l).strip()
                if not l:
                    continue
                if comment and (STOP.match(l) or 'SOURCE PDF PAGE' in l or 'NSSCO Examiners Report' in l):
                    break
                comment.append(l)
            text = ' '.join(comment)
            q = qlookup.get((year, paper, ref))
            if q:
                prefix = ' '.join(q['stem_internal'].split()[:8])
                pos = text.find(prefix)
                if pos > 0:
                    text = text[:pos].strip()
            text = re.split(r' \d+ - Remember', text)[0]
            original_ref = ref
            # These performance comments are displaced in the published report;
            # answer tables stay attached to their original reference.
            if year == 2021 and paper == '1':
                ref = {'4': '5', '7': '8', '8': '9', '9': '10', '10': '11(a)'}.get(ref, ref)
            bid = f'ERBLOCK-6145-{year}-P{paper}-{original_ref}'
            blocks.append({'block_id': bid, 'year': year, 'paper_id': paper,
                           'question_ref': original_ref, 'source_locator': {'source_id': f'{year}-ER', 'pdf_page': pdf_page},
                           'internal_text': block.strip(),
                           'scope': 'Report answer/guidance and comment; internal evidence only, never learner text.'})
            fid = f'ERF-6145-{year}-P{paper}-{original_ref}'
            findings.append({'finding_id': fid, 'year': year, 'paper_id': paper,
                             'question_ref': ref, 'printed_question_ref': original_ref,
                             'source_locator': {'source_id': f'{year}-ER', 'pdf_page': pdf_page, 'printed_page': pdf_page - 2},
                             'verbatim_internal': text, 'provenance': 'corpus',
                             'numbering_note': 'Performance comment semantically remapped from a displaced report row; answer guidance is NOT moved.' if original_ref != ref else None})

(OUT / 'report-blocks.json').write_text(json.dumps(blocks, indent=2, ensure_ascii=False) + '\n')
(OUT / 'report-findings-draft.json').write_text(json.dumps(findings, indent=2, ensure_ascii=False) + '\n')
for f in findings:
    print(f"{f['year']}-P{f['paper_id']} {f['question_ref']:10s} p{f['source_locator']['pdf_page']}: {f['verbatim_internal']}")
print('FINDINGS', len(findings))
