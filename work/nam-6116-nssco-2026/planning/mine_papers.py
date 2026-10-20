#!/usr/bin/env python3
"""Mine the 6116 question papers for command words, tariffs and question shape.

Playbook step 3 / MINER.md. Subject-specific, per step 4.2: the scripts under
standard/v0.2.0-draft/mine/ are worked examples wired to Cambridge subjects.

Mine, do not reproduce. Stems are kept only inside the evidence file so a human
can audit a mapping; nothing here reaches a learner.

Two paper shapes:
  Paper 1  forty four-choice multiple-choice questions, one mark each, no command
           word in the glossary sense. Counted, not parsed for tariffs.
  Paper 2  short-answer and structured, parts carry [n]
  Paper 3  Alternative to Practical, parts carry [n]

Usage: python3 mine_papers.py [--out <dir>]
"""
import os, re, json, subprocess, argparse, collections

PAPERS_DIR = 'Question Banks/Namibian Curricula/NSSCO (New)/Biology (6116)'

# The 18 glossary command words, lower-cased, longest first so "describe and
# explain" wins over "describe". Read from syllabus-facts.json, never typed.
FACTS = 'work/nam-6116-nssco-2026/curriculum/syllabus-facts.json'

# Words the AO descriptions name as question openers but the glossary does not
# define. Counted separately: AGENTS.md rule 5 settles prompt-eligibility from
# the papers, so both sets must be measured.
AO_ONLY_WORDS = ['name', 'indicate', 'give examples', 'distinguish', 'deduce', 'find',
                 'interpret', 'evaluate', 'identify', 'relate', 'complete', 'label',
                 'draw', 'plot', 'explain', 'suggest', 'state', 'describe', 'calculate']


def text(path, layout=True):
    cmd = ['pdftotext', '-layout' if layout else '-raw', path, '-']
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def clean(lines):
    """Drop the vertical 'ORDINARY LEVEL' watermark, which pdftotext emits as
    stray single characters, and the running footers."""
    out = []
    for l in lines:
        s = l.strip()
        if not s or len(s) == 1:
            continue
        if re.match(r'^6116/[123]/\d+$', s) or re.match(r'^\d{6}$', s):
            continue
        if s in ('[Turn over', 'For', "Examiner's", 'Use', "Examiner’s"):
            continue
        out.append(l)
    return out


# Instruction openers the glossary does not list, mapped to the word recorded. Found when every
# part was read in its paper (2026-10-18): these opened parts that were recorded as None or as a
# word appearing later in the stem. "What is meant by" asks for a definition; "make ... drawing"
# is a drawing instruction.
EXTRA_OPENERS = {'what is meant by': 'what is meant by', 'give a reason': 'give a reason/give reasons',
                 'give reasons': 'give a reason/give reasons', 'give one reason': 'give a reason/give reasons',
                 'give two reasons': 'give a reason/give reasons', 'construct': 'construct',
                 'make a': 'draw', 'give': 'give',
                 'write': 'write', 'show': 'show', 'record': 'record', 'shade': 'shade',
                 'circle': 'circle', 'match': 'match', 'read': 'read', 'count': 'count',
                 'support': 'support', 'work out': 'work out'}
QUESTION = re.compile(r'(?i)(^|[,.:]\s*|\b(?:under|for|in|at|from|by|with reference to [^,]*,)\s+)'
                      r'(how|why|what|which|where|when|who)\b')


def command_word(part_text, glossary):
    """The word that OPENS the instruction, not any glossary word that appears in the stem.

    The instruction is a sentence that starts with an imperative or question word, normally the
    last such sentence before the mark. The earlier rule took the longest glossary word found
    anywhere, so "construct a dichotomous key ... identify" was recorded as identify and
    "Give a reason for ..." as None. Glossary entries written "give a reason/give reasons" or
    "apply/use" are split into their alternatives and recorded under the glossary form.
    """
    openers = {}
    for w in glossary:
        for alt in w.split('/'):
            openers[alt.strip()] = w
    for k, v in EXTRA_OPENERS.items():
        openers.setdefault(k, v)
    keys = sorted(openers, key=len, reverse=True)
    body = re.sub(r'\s+', ' ', re.sub(r'\[\d+\]', ' ', part_text)).strip()
    # the "For Examiner's Use" margin leaks in as a stray "Use"; it is not an instruction
    body = re.sub(r"(For )?Examiner['’]s Use|\bUse$|(?<=\.)\s+Use\b(?=\s+[A-Z(]|$)", ' ', body).strip()
    # "Use Fig. 2.1 to calculate ..." / "Using the table, describe ...": the task is the later verb
    body = re.sub(r'(?i)\b(?:use|using)\b[^.?!]*?\b(?:to|,)\s+(?=[a-z])', '', body)
    body = re.sub(r'^\(([a-z]|[ivx]+)\)\s*', '', body)
    sentences = [x.strip(' (').lower() for x in re.split(r'(?<=[.?!:])\s+|\s(?=\([ivx]+\)\s)', body) if x.strip()]
    for sent in reversed(sentences):
        for k in keys:
            if k in ('use', 'apply'):
                continue
            if re.match(re.escape(k) + r'\b', sent):
                return openers[k]
    low = ' ' + body.lower() + ' '
    hits = [(m.start(), -len(k), k) for k in keys if k not in ('how', 'why', 'what', 'which', 'where', 'when',
                                                             'use', 'apply', 'give', 'show', 'read', 'record',
                                                             'make a')
            for m in [re.search(r'\b' + re.escape(k) + r'\b', low)] if m]
    if hits:
        return openers[min(hits)[2]]
    return 'direct question' if QUESTION.search(body) else None


def mine_structured(path, year, paper, glossary):
    """Question parts and their tariffs from Paper 2 or Paper 3."""
    lines = clean(text(path).split('\n'))
    # Full reference, every level kept: 4(b)(ii), not 4(ii). Keeping only the innermost level made
    # refs collide within a paper (2020 P2 had three parts called "4(ii)").
    parts, qno, buf = [], None, []
    lvl = {'letter': None, 'roman': None}

    leads = {}

    def ancestors():
        out = []
        if lvl['letter']:
            out.append('%s(%s)' % (qno, lvl['letter']))
        out.append(qno)
        return out

    def ref():
        return '%s%s%s' % (qno, '(%s)' % lvl['letter'] if lvl['letter'] else '',
                           '(%s)' % lvl['roman'] if lvl['roman'] else '')

    totals = []

    def flush(tariff):
        if buf and qno:
            body = ' '.join(' '.join(buf).split())
            # A [n] sitting alone is the question total, not a part tariff. Without
            # this the totals enter the tariff distribution as phantom parts with
            # no command word, inflating the high end (seen at [10] and [13]).
            # Test for ABSENCE OF WORDS, not for length: a character threshold
            # silently ate the genuine part "(ii) phagocyte [1]" (9 characters),
            # which is how P2 2021 came to 79 marks against a stated 80.
            if tariff is None and re.search(r'[A-Za-z]{3,}', body):
                # text with no mark of its own is the lead-in of the parts that follow
                leads[ref()] = body
                buf.clear()
                return
            if not re.search(r'[A-Za-z]{3,}', re.sub(r'\[\d+\]', '', body)):
                if tariff is not None:
                    totals.append({'year': year, 'paper': paper, 'question': qno,
                                   'question_total': tariff})
                buf.clear()
                return
            this_ref = ref()
            # Unmarked (i), (ii) answer lines followed by a marked (iii) are one item marked as a whole
            # (2023 P2 6(c): enzyme, substrate, end products [3]). Record it at the letter level.
            # Text printed between two marked parts is context for the next one, not an answer line.
            if lvl['roman'] and lvl['letter']:
                marked = {q['question_ref'] for q in parts if q['year'] == year and q['paper'] == paper}
                sib = [r_ for r_ in leads if r_.startswith('%s(%s)(' % (qno, lvl['letter']))]
                ctx = [r_ for r_ in sib if r_ in marked]
                unmarked = [r_ for r_ in sib if r_ not in marked]
                if ctx:
                    body = ' '.join([leads.pop(r_) for r_ in ctx] + [body])
                if unmarked:
                    body = ' '.join([leads.pop(r_) for r_ in unmarked] + [body])
                    this_ref = '%s(%s)' % (qno, lvl['letter'])
            parts.append({'year': year, 'paper': paper,
                          'question_ref': this_ref,
                          'mark_tariff': tariff,
                          'command_word': (command_word(body, glossary) or next(
                              (c for c in (command_word(leads[a], glossary) for a in ancestors() if a in leads)
                               if c and c != 'direct question'), None)),
                          'stem_excerpt': body[:300]})
        buf.clear()

    for raw in lines:
        s = raw.strip()
        m_q = re.match(r'^(\d{1,2})\s+(?=[A-Z(])', s)
        indent = len(raw) - len(raw.lstrip())
        if m_q and indent < 6:
            flush(None)
            qno = m_q.group(1)
            lvl['letter'] = lvl['roman'] = None
            rest = s[m_q.end():]
            m_t = re.match(r'^\(([a-h])\)\s*(.*)$', rest)      # "4 (a) Peeled apples ..." on one line
            if m_t:
                lvl['letter'], rest = m_t.group(1), m_t.group(2)
            buf.append(rest)
            continue
        m_p = re.match(r'^\(([a-z]{1,2}|[ivx]{1,4})\)\s*(.*)$', s)
        if m_p:
            flush(None)
            tag = m_p.group(1)
            rest = m_p.group(2)
            m_n = re.match(r'^\(([ivx]{1,4})\)\s*(.*)$', rest)
            # roman numerals are sub-parts; (i) after (h) would be a letter, which 6116 never reaches
            if re.fullmatch(r'[ivx]+', tag) and not (tag == 'i' and lvl['letter'] == 'h'):
                lvl['roman'] = tag
            else:
                lvl['letter'], lvl['roman'] = tag, None
            if m_n:                                 # "(a) (i) Make ..." on one line
                lvl['roman'] = m_n.group(1)
                rest = m_n.group(2)
            buf.append(rest)
        else:
            buf.append(re.sub(r'\.{4,}', ' ', s))
        for t in re.findall(r'\[(\d{1,2})\]', s):
            flush(int(t))
    flush(None)
    # Answer-line sub-items inside one part ("explanation [2]", "conclusion [1]" under 4(e);
    # "Receptor", "Effector", "Control centre" under 6(b)(i)) carry their own marks but no tag.
    # Number them so every reference is unique: 4(e)-1, 4(e)-2.
    seen = collections.Counter(p['question_ref'] for p in parts if p['mark_tariff'] is not None)
    k = collections.Counter()
    for p in parts:
        if p['mark_tariff'] is not None and seen[p['question_ref']] > 1:
            k[p['question_ref']] += 1
            first = next(q for q in parts if q['question_ref'] in (p['question_ref'], p['question_ref'] + '-1'))
            p['question_ref'] = '%s-%d' % (p['question_ref'], k[p['question_ref']])
            if p['command_word'] is None:          # an answer line shares its first sibling's instruction
                p['command_word'] = first['command_word']
    return ([p for p in parts if p['mark_tariff'] is not None and p['stem_excerpt'].strip()],
            totals)


def mine_mcq(path, year):
    """Paper 1 is forty four-choice questions. Counting line-initial numbers
    over-counts, because the options and stray numerics match too; count the
    DISTINCT question numbers instead and report the highest seen."""
    body = text(path)
    nums = {int(m) for m in re.findall(r'^\s*(\d{1,2})\s+(?=\S)', body, re.M) if 1 <= int(m) <= 40}
    stated = re.search(r'There are (\w+) questions on this paper', body)
    return {'year': year, 'paper': '1',
            'question_count_detected': len(nums), 'highest_question_number': max(nums) if nums else None,
            'count_stated_on_cover': stated.group(1) if stated else None,
            'marks_each': 1, 'command_words': None,
            'note': 'four-choice multiple choice; no glossary command word opens these'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='work/nam-6116-nssco-2026/assessment-evidence')
    args = ap.parse_args()

    facts = json.load(open(FACTS))
    glossary = sorted((w['word'].lower().replace('/ ', '/') for w in facts['command_words']),
                      key=len, reverse=True)
    glossary = [g for g in glossary]
    vocab = sorted(set(glossary + AO_ONLY_WORDS), key=len, reverse=True)

    parts, mcq, q_totals = [], [], []
    for year in sorted(os.listdir(PAPERS_DIR)):
        d = os.path.join(PAPERS_DIR, year)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.lower().endswith('.pdf') or re.search(r'xaminer', fn, re.I):
                continue
            path = os.path.join(d, fn)
            head = text(path)[:1500]
            m = re.search(r'6116\s*/\s*([123])', head)
            paper = m.group(1) if m else '?'
            if paper == '1':
                mcq.append(mine_mcq(path, year))
            elif paper in ('2', '3'):
                pr, tt = mine_structured(path, year, paper, vocab)
                parts.extend(pr)
                q_totals.extend(tt)

    os.makedirs(args.out, exist_ok=True)
    json.dump({'question_parts': parts, 'paper_1': mcq, 'question_totals': q_totals},
              open(os.path.join(args.out, 'paper_evidence.json'), 'w'), indent=2, ensure_ascii=False)

    print(f"question parts with tariffs: {len(parts)}")
    print(f"Paper 1 files: {len(mcq)}  distinct q-numbers: "
          f"{[m['question_count_detected'] for m in mcq]}  highest: "
          f"{[m['highest_question_number'] for m in mcq]}  cover says: "
          f"{sorted({m['count_stated_on_cover'] for m in mcq})}")
    print(f"question totals captured: {len(q_totals)}")
    cw = collections.Counter(p['command_word'] for p in parts)
    print("\ncommand word        parts   tariffs seen       modal")
    for w, c in cw.most_common(24):
        ts = [p['mark_tariff'] for p in parts if p['command_word'] == w]
        modal = collections.Counter(ts).most_common(1)[0][0] if ts else '-'
        print(f"  {str(w):<18} {c:>4}   {sorted(set(ts))}  {modal}")
    print("\nmarks by paper:",
          dict(collections.Counter(p['paper'] for p in parts)))


if __name__ == '__main__':
    main()
