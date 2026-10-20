#!/usr/bin/env python3
"""Mine the Biology 6116 sections of the NSSCO examiner reports.

Playbook step 3 / MINER.md sections C and D. Subject-specific per step 4.2.

Each NSSCO report is a combined multi-subject volume. The Biology section is
located by its own heading (BIOLOGY then 6116) and bounded by the next subject
heading, rather than by a page number typed in, because the offset moves between
years (p.49 for 2020-2024, p.47 for 2025).

Mine, do not reproduce: statements are classified and stored as evidence for
auditing. Their wording never reaches a learner.

NOTE ON THE 'Answer:' BLOCKS. These reports print indicative answers beside some
questions. They are NOT mark schemes: no tariff breakdown, no award grammar, no
band descriptors, and they appear only for a subset of parts. They are recorded
as partial answer-shape evidence and labelled as such.

Usage: python3 mine_reports.py
"""
import os, re, json, subprocess, collections

REPORTS = [
 ('2020', 'Question Banks/Namibian Examiner Reports/NSSCO (New) /2020/NSSCO(New) Examiners Report 2020 (1).pdf'),
 ('2021', 'Question Banks/Namibian Curricula/NSSCO (New)/Biology (6116)/2021/NSSCO(New) Examiners Report 2021.pdf'),
 ('2022', 'Question Banks/Namibian Curricula/NSSCO (New)/Biology (6116)/2022/NSSCO(New) Examiners Report 2022.pdf'),
 ('2023', 'Question Banks/Namibian Examiner Reports/NSSCO (New) /2023/Examiners Report NSSCO 2023.pdf'),
 ('2024', 'Question Banks/Namibian Examiner Reports/NSSCO (New) /2024/Examiners Report NSSCO 2024.pdf'),
 ('2025', 'Question Banks/Namibian Examiner Reports/NSSCO (New) /2025/NSSCOExaminersReport2025.pdf'),
]
OUT = 'work/nam-6116-nssco-2026/assessment-evidence'

# MINER.md's four classes. Ordered: the first pattern that fires wins, so the
# more specific signals are tested before the generic ones.
# 'though' for 'thought' and similar slips appear in these reports, so the
# patterns tolerate them. Statements that match nothing are KEPT with class null:
# MINER.md asks for every statement mapped and classified, and silently dropping
# the unmatched ones lost most of the 2024 commentary on the first pass.
CLASSES = [
 ('command-word miss', r'did not answer the question|answered a different|misread the question|'
                       r'did not follow the instruction|ignored the command|instead of (?:describing|explaining|stating|naming|giving)|'
                       r'gave .{0,40} instead of|defined .{0,40} instead of|wrote about|'
                       r'did not read the question|misinterpreted the question'),
 ('misconception',     r'confus|mistook|mistake|incorrectly (?:believed|thought|though|stated|selected|identified|used)|'
                       r'wrongly (?:believed|thought|though|stated|identified)|misconception|'
                       r'thought that|though the|believed that|assumed that|'
                       r'without first convert|did not convert|interchanged|mixed up|'
                       r'is not the same as|should not be confused'),
 ('omission',          r'(?:failed|omitted|did not|could not|neglected) (?:to )?(?:mention|state|give|include|identify|name|provide|indicate|show|label)|'
                       r'left out|no mention of|did not attempt|omission|did not give|'
                       r'lost marks because|lost marks by|lost marks due'),
 ('shallow development', r'did not develop|lacked detail|superficial|not elaborated|vague|'
                         r'insufficient detail|too general|did not explain (?:fully|further)|'
                         r'not specific|lacked precision|incomplete answer|partially correct|'
                         r'did not qualify|answers were general'),
 ('spelling/terminology', r'spelling|misspel|incorrect term|wrong terminology|terminology was'),
 ('teaching advice', r'teachers should|it should be emphasised|it is important that (?:learners|teachers)|'
                     r'learners should be (?:taught|exposed)|should be emphasised'),
]


def pages(path, first=None, last=None):
    cmd = ['pdftotext', '-layout']
    if first: cmd += ['-f', str(first)]
    if last: cmd += ['-l', str(last)]
    return subprocess.run(cmd + [path, '-'], capture_output=True, text=True).stdout.split('\f')


def biology_span(path):
    """(start, end) PDF pages of the Biology section, found by heading not by offset."""
    all_pages = pages(path)
    start = None
    for i, p in enumerate(all_pages, start=1):
        if re.search(r'^\s*BIOLOGY\s*$', p, re.M) and re.search(r'^\s*6116\s*$', p, re.M):
            start = i
            break
    if start is None:
        return None, None, len(all_pages)
    for j in range(start + 1, len(all_pages) + 1):
        p = all_pages[j - 1]
        # next subject heading: an all-caps title line with a 4-digit code under it
        if re.search(r'^\s*[A-Z][A-Z &/\'-]{3,}\s*$', p, re.M) and re.search(r'^\s*(\d{4})\s*$', p, re.M):
            code = re.search(r'^\s*(\d{4})\s*$', p, re.M).group(1)
            if code != '6116':
                return start, j - 1, len(all_pages)
    return start, len(all_pages), len(all_pages)


def classify(sentence):
    low = sentence.lower()
    for name, pat in CLASSES:
        if re.search(pat, low):
            return name
    return None


def main():
    statements, spans, answer_blocks = [], [], 0
    for year, path in REPORTS:
        if not os.path.exists(path):
            print('MISSING:', path); continue
        s, e, total = biology_span(path)
        spans.append({'year': year, 'start_pdf_page': s, 'end_pdf_page': e,
                      'pages_in_volume': total, 'biology_pages': (e - s + 1) if s else 0})
        if s is None:
            continue
        body = '\n'.join(pages(path, s, e))
        answer_blocks += len(re.findall(r'^\s*Answers?\s*:', body, re.M))
        paper = None
        # Join wrapped lines into paragraphs BEFORE splitting sentences. Splitting
        # line by line truncated any sentence that spanned a line break, which is
        # most of them in a two-column report ("Some candidates confused insulin
        # with" lost its object).
        paras, cur, cur_q = [], [], None
        for raw in body.split('\n'):
            line = ' '.join(raw.split())
            if not line:
                if cur: paras.append((paper, cur_q, ' '.join(cur))); cur = []
                continue
            m = re.match(r'^Paper\s+([123])\b', line)
            if m:
                if cur: paras.append((paper, cur_q, ' '.join(cur))); cur = []
                paper = m.group(1); continue
            q = re.match(r'^(\d{1,2})\s*(\([a-z]\))?\s*(\([ivx]+\))?\s', line)
            if q and cur:                       # a new question ref starts a new paragraph
                paras.append((paper, cur_q, ' '.join(cur))); cur = []
            if q:
                cur_q = q.group(0).strip()
            cur.append(line)
        if cur: paras.append((paper, cur_q, ' '.join(cur)))

        for pap, qref, para in paras:
            for sent in re.split(r'(?<=[.;])\s+(?=[A-Z(])', para):
                sent = sent.strip()
                if len(sent) < 35:
                    continue
                cls = classify(sent)
                pct = None
                if re.search(r'(candidate|learner)', sent, re.I) and re.search(
                        r'(scor|answer|correct|got it right|performed|passed|achiev)', sent, re.I):
                    pct = re.search(r'(\d{1,3}(?:\.\d)?)\s*%', sent)
                if cls or pct:
                    statements.append({
                        'year': year, 'paper': pap, 'question_ref': qref,
                        'class': cls,
                        'percent_scoring': float(pct.group(1)) if pct else None,
                        'statement': sent[:500],
                        'source': {'report_year': year, 'pdf_pages': f'{s}-{e}'},
                    })
    os.makedirs(OUT, exist_ok=True)
    json.dump({'biology_spans': spans, 'statements': statements,
               'indicative_answer_blocks_seen': answer_blocks},
              open(os.path.join(OUT, 'examiner_evidence.json'), 'w'), indent=2, ensure_ascii=False)

    print('BIOLOGY SECTION PER REPORT')
    for sp in spans:
        print(f"  {sp['year']}  PDF p.{sp['start_pdf_page']}-{sp['end_pdf_page']}  "
              f"({sp['biology_pages']} pages of {sp['pages_in_volume']})")
    print(f"\nstatements classified: {len(statements)}")
    for k, v in collections.Counter(s['class'] or '(unclassified, kept for the percentage)' for s in statements).most_common():
        print(f"  {str(k):<40} {v}")
    print(f"by year: {dict(collections.Counter(s['year'] for s in statements))}")
    print(f"by paper: {dict(collections.Counter(str(s['paper']) for s in statements))}")
    pcts=[s for s in statements if s['percent_scoring'] is not None]
    print(f"statements carrying a scoring percentage: {len(pcts)}")
    print(f"indicative 'Answer:' blocks seen: {answer_blocks} (NOT mark schemes)")


if __name__ == '__main__':
    main()
