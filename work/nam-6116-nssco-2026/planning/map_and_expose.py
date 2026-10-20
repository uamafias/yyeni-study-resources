#!/usr/bin/env python3
"""Map mined evidence to the syllabus and compute exposure.

MINER.md is explicit that objective_ids must be mapped BY MEANING, not by token
match, and that a token-matched pass was wrong repeatedly on 9609. That warning
is respected here by NOT claiming objective-level mappings this pass.

What this does instead, and why:
  - builds a distinctive-term index from each sub-topic's own objective wording,
    discarding terms that occur across many sub-topics (which are the ones that
    cause false matches);
  - proposes a SUB-TOPIC for each question part and examiner statement;
  - records a confidence and the matched terms on every proposal, so a human
    reading the stem can confirm or overturn it;
  - leaves objective-level mapping to a reviewed pass, and says so in the output.

Exposure is therefore computed at sub-topic level and labelled as such. It is a
measure of examined demand. It is NOT a card count and nothing here converts it
into one.

Usage: python3 map_and_expose.py
"""
import json, re, collections, os

WS = 'work/nam-6116-nssco-2026'
FACTS = f'{WS}/curriculum/syllabus-facts.json'
EV = f'{WS}/assessment-evidence'

STOP = set('''the a an and or of to in on for with from by as at is are be that this these those
it its their his her they them we you i not no any some all each other more most than then when
where which who whom what how why can may must should would could will shall do does did done
been being have has had such same own very also only just about into over under between among
during before after above below up down out off again further once here there both few many
own s t don now learners learner should able state give name list describe explain outline define
using use used using used including include includes e g eg ie i.e. etc'''.split())


def terms(text):
    return [w for w in re.findall(r"[a-z][a-z\-']{3,}", text.lower()) if w not in STOP]


def build_index(facts):
    """Distinctive terms per sub-topic: terms that appear in few sub-topics."""
    per = {}
    for row in facts['content']:
        if row['code'].isdigit():          # topic-level row, skip
            continue
        blob = row['title'] + ' ' + ' '.join(o['text'] for o in row['specific_objectives'])
        per[row['code']] = collections.Counter(terms(blob))
    df = collections.Counter()
    for c in per.values():
        df.update(set(c))
    n = len(per)
    index = {}
    for code, c in per.items():
        # keep terms occurring in at most 15% of sub-topics; those are the ones
        # that actually discriminate. Common biology vocabulary is discarded.
        index[code] = {t for t in c if df[t] <= max(2, n * 0.15)}
    return index, df


def propose(text, index):
    tt = set(terms(text))
    scores = {c: len(tt & kws) for c, kws in index.items()}
    best = max(scores.values()) if scores else 0
    if best == 0:
        return None, 0, []
    winners = [c for c, v in scores.items() if v == best]
    code = sorted(winners)[0]
    matched = sorted(tt & index[code])
    # confidence: a single shared term is weak, and a tie across sub-topics weaker
    conf = 'low' if best == 1 or len(winners) > 1 else ('medium' if best == 2 else 'high')
    return code, best, matched if conf != 'low' else matched[:3]


def main():
    facts = json.load(open(FACTS))
    index, df = build_index(facts)
    titles = {r['code']: r['title'] for r in facts['content']}
    papers = json.load(open(f'{EV}/paper_evidence.json'))
    reports = json.load(open(f'{EV}/examiner_evidence.json'))

    for p in papers['question_parts']:
        c, n, m = propose(p['stem_excerpt'], index)
        p.update(proposed_sub_topic=c, match_strength=n, matched_terms=m,
                 mapping_method='distinctive-term proposal, NOT a reviewed meaning-based mapping',
                 mapping_confidence=('low' if n <= 1 else 'medium' if n == 2 else 'high'))
    for s in reports['statements']:
        c, n, m = propose(s['statement'], index)
        s.update(proposed_sub_topic=c, match_strength=n, matched_terms=m,
                 mapping_method='distinctive-term proposal, NOT a reviewed meaning-based mapping',
                 mapping_confidence=('low' if n <= 1 else 'medium' if n == 2 else 'high'))

    json.dump(papers, open(f'{EV}/paper_evidence.json', 'w'), indent=2, ensure_ascii=False)
    json.dump(reports, open(f'{EV}/examiner_evidence.json', 'w'), indent=2, ensure_ascii=False)

    expo = {}
    for row in facts['content']:
        if row['code'].isdigit():
            continue
        pts = [p for p in papers['question_parts'] if p['proposed_sub_topic'] == row['code']]
        sts = [s for s in reports['statements'] if s['proposed_sub_topic'] == row['code']]
        pcts = [s['percent_scoring'] for s in sts if s['percent_scoring'] is not None]
        expo[row['code']] = {
            'title': row['title'],
            'specific_objectives': len(row['specific_objectives']),
            'question_parts': len(pts),
            'distinct_years': sorted({p['year'] for p in pts}),
            'max_tariff': max([p['mark_tariff'] for p in pts], default=0),
            'total_marks_seen': sum(p['mark_tariff'] for p in pts),
            'command_words': dict(collections.Counter(
                p['command_word'] for p in pts if p['command_word'])),
            'examiner_statements': len(sts),
            'mean_percent_scoring': round(sum(pcts) / len(pcts), 1) if pcts else None,
            'high_confidence_parts': sum(1 for p in pts if p['mapping_confidence'] == 'high'),
        }
    for v in expo.values():
        y = len(v['distinct_years'])
        v['exposure_class'] = ('not seen' if v['question_parts'] == 0 else
                               'rare' if y <= 1 else
                               'occasional' if y <= 3 else 'frequent')
    out = {
        'computed_from': 'assessment-evidence/paper_evidence.json + examiner_evidence.json',
        'granularity': 'sub-topic',
        'caveat': ('Sub-topic level only. MINER.md requires objective-level mapping to be done by '
                   'MEANING; these are distinctive-term PROPOSALS awaiting a reviewed pass. '
                   'Exposure measures examined demand and is not a card count.'),
        'exposure': expo,
    }
    # exam-exposure.json is written by build_exposure.py, after validate_mapping.py,
    # because the build tools need objective-level entries counted from VALIDATED
    # parts only, and validation has not happened yet at this point.

    cls = collections.Counter(v['exposure_class'] for v in expo.values())
    print('exposure classes:', dict(cls))
    conf = collections.Counter(p['mapping_confidence'] for p in papers['question_parts'])
    print('part mapping confidence:', dict(conf))
    unseen = [f"{c} {v['title']}" for c, v in expo.items() if v['question_parts'] == 0]
    print(f"\nsub-topics with NO question part proposed ({len(unseen)}):")
    for u in unseen: print('   ', u)


if __name__ == '__main__':
    main()
