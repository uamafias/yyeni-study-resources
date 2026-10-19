#!/usr/bin/env python3
"""Gate 1: validate the sub-topic mappings before they guide emphasis.

The first pass proposed a sub-topic per question part from distinctive single
terms. MINER.md warns that token matching was wrong repeatedly on 9609, so a
proposal is not evidence. This validates by a SECOND, independent method and
treats agreement between two unlike methods as the signal.

Method A (already run): distinctive single terms, document-frequency filtered.
Method B (here):        phrase matching against each objective's own wording -
                        contiguous 2- and 3-word sequences, which survive only
                        where the stem genuinely echoes the syllabus phrasing,
                        and are far harder to hit by coincidence than one word.

A part is VALIDATED where both methods choose the same sub-topic. Where they
disagree or B finds nothing, the part is marked unvalidated and is excluded from
emphasis. It is never excluded from coverage: every mandatory objective is
planned regardless.
"""
import json, re, collections

WS = 'work/nam-6116-nssco-2026'
STOP = set('''the a an and or of to in on for with from by as at is are be that this these those it
its their they them we you not no any some all each more most than then when which who what how why
can may must should would could will do does did have has had such same very also only just about
into over under between during before after above below out off again once here there both few many
show shows shown following figure fig table use used using given below above state give name list
describe explain outline define answer question candidate candidates marks mark'''.split())


def words(t):
    return [w for w in re.findall(r"[a-z][a-z\-']{2,}", t.lower()) if w not in STOP]


def ngrams(t, n):
    w = words(t)
    return {' '.join(w[i:i + n]) for i in range(len(w) - n + 1)}


def main():
    facts = json.load(open(f'{WS}/curriculum/syllabus-facts.json'))
    ev = json.load(open(f'{WS}/assessment-evidence/paper_evidence.json'))

    # Method B index: phrases from each sub-topic's own objective wording
    idx = {}
    for row in facts['content']:
        if row['code'].isdigit():
            continue
        blob = row['title'] + '. ' + '. '.join(o['text'] for o in row['specific_objectives'])
        idx[row['code']] = ngrams(blob, 2) | ngrams(blob, 3)
    # phrases shared by many sub-topics discriminate nothing
    df = collections.Counter()
    for v in idx.values():
        df.update(v)
    idx = {c: {p for p in v if df[p] <= 2} for c, v in idx.items()}

    agree = disagree = bonly = neither = 0
    for p in ev['question_parts']:
        stem = ngrams(p['stem_excerpt'], 2) | ngrams(p['stem_excerpt'], 3)
        scores = {c: len(stem & ph) for c, ph in idx.items() if stem & ph}
        if scores:
            top = max(scores.values())
            winners = sorted(c for c, v in scores.items() if v == top)
            b = winners[0]
            p['method_b_sub_topic'] = b
            p['method_b_phrase_hits'] = top
            p['method_b_matched'] = sorted(stem & idx[b])[:5]
        else:
            b = None
            p['method_b_sub_topic'] = None
            p['method_b_phrase_hits'] = 0
            p['method_b_matched'] = []
        a = p.get('proposed_sub_topic')
        if a and b and a == b:
            p['mapping_status'] = 'validated'; agree += 1
        elif a and b:
            p['mapping_status'] = 'conflict'; disagree += 1
        elif b and not a:
            p['mapping_status'] = 'method_b_only'; bonly += 1
        else:
            p['mapping_status'] = 'unvalidated'; neither += 1
        p['use_for_emphasis'] = p['mapping_status'] == 'validated'

    json.dump(ev, open(f'{WS}/assessment-evidence/paper_evidence.json', 'w'),
              indent=2, ensure_ascii=False)

    n = len(ev['question_parts'])
    print(f"question parts: {n}")
    print(f"  validated (both methods agree) : {agree}  ({agree/n*100:.0f}%)")
    print(f"  conflict (methods disagree)    : {disagree}")
    print(f"  method B only                  : {bonly}")
    print(f"  neither method mapped          : {neither}")
    print(f"\nmarks usable for emphasis: "
          f"{sum(p['mark_tariff'] for p in ev['question_parts'] if p['use_for_emphasis'])} of "
          f"{sum(p['mark_tariff'] for p in ev['question_parts'])}")


if __name__ == '__main__':
    main()
