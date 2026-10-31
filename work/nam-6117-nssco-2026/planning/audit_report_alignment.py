"""Audit report answer links against paper labels and read answer meaning.

The semantic pass was performed question by question against the paired paper
and report excerpts. This script records that review and independently checks
printed labels so a future rerun does not silently accept positional drift.
"""
import json
import hashlib
import re
import subprocess
from pathlib import Path

import extract_question_parts as extract

WORK = Path(__file__).resolve().parents[1]
AE = WORK / 'assessment-evidence'

# This continuation has no fresh label: the paper allocates separate marks to
# observations for tubes X and Y. Their shared report row is split manually.
LABEL_EXCEPTIONS = {'QP-6117-2024-2-Q04-P02': 'a'}


def paper_labels():
    labels = {}
    pattern = re.compile(r'^\s*(?:\d+\s+)?\(([a-z]|[ivx]+)\)(?:\s*\(([ivx]+)\))?', re.I)
    for year in range(2020, 2026):
        for paper in (2, 3):
            source = extract.source_file(year, paper)
            text = subprocess.check_output(['pdftotext', '-raw', str(source), '-'], text=True)
            q = part = 1
            run = 0
            last_end = 0
            outer = None
            for mark in extract.MARK.finditer(text):
                tariff = int(mark.group(1))
                line = extract.line_bounds(text, mark)
                standalone = not line[:line.find('[')].strip() and not line[line.find(']') + 1:].strip()
                if standalone and tariff >= 5 and tariff == run:
                    q += 1
                    part = 1
                    run = 0
                    last_end = mark.end()
                    outer = None
                    continue
                segment = text[last_end:mark.start()]
                candidates = []
                for line in segment.splitlines():
                    match = pattern.match(line)
                    if not match:
                        continue
                    label, roman = match.groups()
                    label = label.lower()
                    if re.fullmatch('[ivx]+', label):
                        if outer:
                            candidates.append(('roman', label, None))
                    elif (outer is None and label == 'a') or (outer is not None and ord(label) <= ord(outer) + 1):
                        candidates.append(('alpha', label, roman))
                selected = candidates[0] if candidates else None
                if selected:
                    if selected[0] == 'alpha':
                        outer = selected[1]
                        label = outer + (selected[2] or '')
                    else:
                        label = (outer or '') + selected[1]
                else:
                    label = None
                eid = f'QP-6117-{year}-{paper}-Q{q:02d}-P{part:02d}'
                labels[eid] = label
                run += tariff
                part += 1
                last_end = mark.end()
    return labels


def report_labels(tables):
    labels = {}
    parent = re.compile(r'^(?:\d+[\s.]*|\d+\s*)?(?:\(([a-z])\)|([a-z])\.)(?:\s*(?:\(([ivx]+)\)|([ivx]+)\.))?', re.I)
    roman = re.compile(r'^(?:\(([ivx]+)\)|([ivx]+)\.)', re.I)
    for table in tables:
        outer = None
        key = (table['year'], table['paper'], table['question'])
        for index, row in enumerate(table['rows']):
            source = row['label_line'].strip()
            roman_match = roman.match(source)
            match = parent.match(source)
            if roman_match and outer:
                label = outer + (roman_match.group(1) or roman_match.group(2)).lower()
            elif match:
                outer = (match.group(1) or match.group(2)).lower()
                label = outer + ((match.group(3) or match.group(4) or '').lower())
            else:
                label = None
            labels[(*key, index)] = label
    return labels


def main():
    alignment = json.loads((AE / 'report-guidance-alignment.json').read_text())['aligned_parts']
    tables = json.loads((AE / 'report-answer-tables.json').read_text())['questions']
    table_map = {(t['year'], t['paper'], t['question']): t for t in tables}
    question_parts = {x['evidence_id']: x for x in json.loads((AE / 'question_parts.json').read_text())['records']}
    reviewed_hashes = json.loads((AE / 'reviewed-answer-pairs.json').read_text())['source_pair_sha256']
    qlabels = paper_labels()
    rlabels = report_labels(tables)
    entries = []
    for eid, aligned in alignment.items():
        year, paper, question = map(int, re.search(r'(\d{4})-(\d)-Q(\d+)', eid).groups())
        key = (year, paper, question)
        table = table_map[key]
        row_indices = [table['rows'].index(row) for row in aligned['source_rows']]
        qp_label = qlabels.get(eid) or LABEL_EXCEPTIONS.get(eid)
        answer_labels = [rlabels[(*key, index)] for index in row_indices]
        label_consistent = bool(qp_label) and all(
            label and (label == qp_label or (len(qp_label) == 1 and label.startswith(qp_label)))
            for label in answer_labels
        )
        pair = {'question_excerpt': question_parts[eid]['context_summary'],
                'mark_tariff': question_parts[eid]['mark_tariff'],
                'report_locator': aligned['source_locator'],
                'report_text': [row['source_text'] for row in aligned['source_rows']]}
        digest = hashlib.sha256(json.dumps(pair, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        meaning_reviewed = reviewed_hashes.get(eid) == digest
        # Answer meaning was read with the corresponding question for every
        # link. These four need corrected image/shared-row guidance; the
        # original row remains traceable but is not sufficient by itself.
        special = eid in {
            'QP-6117-2024-2-Q04-P01', 'QP-6117-2024-2-Q04-P02',
            'QP-6117-2023-2-Q07-P09', 'QP-6117-2025-2-Q03-P07',
        }
        status = ('verified_with_manual_guidance' if special else 'verified_label_and_meaning') if label_consistent and meaning_reviewed else 'unresolved_label_or_meaning'
        entries.append({
            'evidence_id': eid,
            'question_label': qp_label,
            'report_labels': answer_labels,
            'report_row_indices': row_indices,
            'report_locator': aligned['source_locator'],
            'label_consistent': label_consistent,
            'semantic_review': 'curated_source_pair_hash_matches' if meaning_reviewed else 'needs_review',
            'status': status,
        })
    unresolved = [e['evidence_id'] for e in entries if e['status'] == 'unresolved_label_or_meaning']
    output = {'status': 'question_label_and_meaning_review',
              'method': 'Printed label check independent of row count; question and answer meaning read by year/question. Image and shared rows use separately paraphrased guidance.',
              'linked_parts': len(entries), 'verified_parts': len(entries) - len(unresolved),
              'unresolved_parts': unresolved, 'parts': entries}
    (AE / 'report-alignment-audit.json').write_text(json.dumps(output, indent=2, ensure_ascii=False) + '\n')
    print('Alignment audit:', len(entries), 'links;', len(unresolved), 'unresolved')
    if unresolved:
        print(*unresolved, sep='\n')


if __name__ == '__main__':
    main()
