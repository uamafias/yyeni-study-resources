"""Extract labelled comments and general recommendations with page locators for review."""
import json
import re
from pathlib import Path

WS = Path(__file__).resolve().parents[1]
records = []
for path in sorted((WS/'assessment-evidence/extracted').glob('*-ER-raw.txt')):
    year = int(path.name.split('-')[1])
    paper, page, general = None, None, False
    active, text, question = None, [], ''
    def flush():
        if text:
            statement = re.sub(r'\s+', ' ', ' '.join(text)).strip()
            records.append({'finding_id': f'ER-6145-{year}-{len(records)+1:03}', 'year': year,
                            'paper_id': paper, 'question_ref': active or None,
                            'statement': statement, 'source_id': f'6145-{year}-ER',
                            'source_locator': {'pdf_page': first_page, 'extraction': str(path.relative_to(WS))}})
        text.clear()
    for line in path.read_text().splitlines():
        pm = re.match(r'=== PDF PAGE (\d+) ===',line)
        if pm:
            flush()
            page = int(pm[1])
            continue
        line = line.strip()
        if re.match(r'^Paper [12]$',line):
            flush()
            paper = 'P'+line[-1]
            question = ''
        if 'GENERAL COMMENTS' in line or 'SUGGESTIONS TO TEACHERS' in line:
            flush()
            general = True
            active = None
            continue
        if re.search(r'COMMENTS ON (?:INDIVIDUAL|SPECIFIC) QUESTIONS',line):
            flush()
            general = False
            continue
        if line.startswith(('Answer', 'NSSCO Examiners', 'SECTION')) or re.fullmatch(r'\d+',line):
            flush()
            continue
        m = re.match(r'^(?:(\d{1,2})\s+)?(?:(\([a-h]\))\s*)?(?:(\([ivx]+\))\s*)?(Well |Fairly |Poorly |Not well |Moderately |Most learners|Some learners|Learners |The majority|A few |Many learners)(.*)',line)
        if m:
            flush()
            if m[1]:
                question = m[1]
            if m[2]:
                question = re.match(r'\d+',question)[0] + m[2] if re.match(r'\d+',question) else m[2]
            if m[3]:
                question = re.sub(r'\([ivx]+\)$', '', question) + m[3]
            active = question
            first_page = page
            text.append(m[4]+m[5])
        elif general and line and not line.startswith(('ECONOMICS','6145','Paper')):
            if line.startswith('•'):
                flush()
            if not text:
                first_page = page
            text.append(line)
        elif text and line:
            text.append(line)
    flush()
(WS/'assessment-evidence/report-comment-candidates.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
for year in range(2020,2026):
    items = [f"{r['finding_id']} {r['paper_id']} {r['question_ref']} p{r['source_locator']['pdf_page']}: {r['statement']}" for r in records if r['year']==year]
    (WS/f'planning/report-comments-{year}.txt').write_text('\n'.join(items)+'\n')
print(len(records), 'report comments extracted for human review')
