# -*- coding: utf-8 -*-
"""STEP ZERO. Transcribe the syllabus's own statement of how the subject is assessed.

This exists because assessment values were once typed from recall instead of read
off the page, and two of them were wrong: a command-word list that did not match
the syllabus table, and per-paper AO splits that were inferred from the papers'
names rather than read from the weighting table. Both propagate into every item
in a subject.

So nothing about assessment is typed here either. Every value carries the page it
came from and the verbatim line that states it, and verify.py refuses any value
whose quote cannot be found in the syllabus text. A value you cannot cite is a
value you do not have.

Emits <workspace>/curriculum/syllabus-facts.json.
"""
import json, os, re, subprocess, sys, datetime

ROOT = os.path.expanduser('~/mine')
REPO = os.path.expanduser('~/mnt/YYeni Study Resources')

SUBJECTS = {
    '0450': {'pdf': 'Syllabi/Cambridge Curricula/IGCSE Cambridge /Business Studies-2026-syllabus.pdf',
             'ws': 'work/cie-0450-igcse-2026',
             'title': 'Cambridge IGCSE Business Studies 0450'},
    '0455': {'pdf': 'Syllabi/Cambridge Curricula/IGCSE Cambridge /Economics-2026-syllabus.pdf',
             'ws': 'work/cie-0455-igcse-2026',
             'title': 'Cambridge IGCSE Economics 0455'},
    '9609': {'pdf': 'Syllabi/Cambridge Curricula/Cambridge AS & A Level/'
                    'Business Studies 2026-2028-syllabus.pdf',
             'ws': 'work/cie-9609-as-2026-2028',
             'title': 'Cambridge International AS & A Level Business 9609',
             # The AS & A Level syllabus states weights for two routes. This
             # workspace is the AS route, so the AS column is the target; the
             # A Level column is kept in the facts but never used here.
             'route': 'AS Level', 'papers_in_route': ['1', '2']},
    # --- the November 2026 entries, in exam-date order. papers_sat is the learner's
    # actual entry; papers_in_route is what the route's plan covers.
    '9709': {'pdf': 'Syllabi/Cambridge Curricula/Cambridge AS & A Level/Maths-2026-2027-syllabus.pdf',
             'ws': 'work/cie-9709-as-2026-2027',
             'title': 'Cambridge International AS & A Level Mathematics 9709',
             'route': 'AS Level', 'papers_in_route': ['1', '5'],
             'papers_sat': ['12 Pure Mathematics 1', '52 Probability & Statistics 1'],
             'first_exam': '2026-09-30'},
    '0500': {'pdf': 'Syllabi/Cambridge Curricula/IGCSE Cambridge /IGCSE English 1st Syllabus.pdf',
             'ws': 'work/cie-0500-igcse-2024-2026',
             'title': 'Cambridge IGCSE First Language English 0500',
             'papers_in_route': ['1', '2'],
             'papers_sat': ['12 Reading', '22 Directed Writing and Composition'],
             'first_exam': '2026-10-05'},
    '9618': {'pdf': 'Syllabi/Cambridge Curricula/Cambridge AS & A Level/AS & A Computer Science (9618).pdf',
             'ws': 'work/cie-9618-as-2026',
             'title': 'Cambridge International AS & A Level Computer Science 9618',
             'route': 'AS Level', 'papers_in_route': ['1', '2'],
             'papers_sat': ['11 Theory Fundamentals', '21 Fundamental Problem-solving and Programming Skills'],
             'first_exam': '2026-10-09'},
    '9702': {'pdf': 'Syllabi/Cambridge Curricula/Cambridge AS & A Level/Cambridge AS & A Level Physics-syllabus.pdf',
             'ws': 'work/cie-9702-as-2025-2027',
             'title': 'Cambridge International AS & A Level Physics 9702',
             'route': 'AS Level', 'papers_in_route': ['1', '2', '3'],
             'papers_sat': ['12 Multiple Choice', '22 AS Level Structured Questions', '34 Advanced Practical Skills'],
             'first_exam': '2026-10-14'},
    '0460': {'pdf': 'Syllabi/Cambridge Curricula/IGCSE Cambridge /IGCSE Geography Syllabus.pdf',
             'ws': 'work/cie-0460-igcse-2025-2026',
             'title': 'Cambridge IGCSE Geography 0460',
             'papers_in_route': ['1', '2', '4'],
             'papers_sat': ['12 Geographical Themes', '22 Geographical Skills', '42 Alternative to Coursework'],
             'first_exam': '2026-10-14'},
    '9093': {'pdf': 'Syllabi/Cambridge Curricula/Cambridge AS & A Level/AS & A Level English Syllabus.pdf',
             'ws': 'work/cie-9093-as-2024-2026',
             'title': 'Cambridge International AS & A Level English Language 9093',
             'route': 'AS Level', 'papers_in_route': ['1', '2'],
             'papers_sat': ['12 Reading', '22 Writing'],
             'first_exam': '2026-10-16'},
}


def pages(pdf):
    """Text of the PDF, one entry per printed page, layout preserved.

    pdftotext emits a form feed between pages, so the index is the page number.
    Carrying the page means every fact below can name where a human checks it.
    """
    out = subprocess.run(['pdftotext', '-layout', pdf, '-'],
                         capture_output=True, check=True).stdout.decode('utf-8', 'ignore')
    return out.split('\f')


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def find(pgs, pat, flags=re.I):
    """Every (page_number, line) matching a pattern."""
    rx = re.compile(pat, flags)
    hits = []
    for i, pg in enumerate(pgs, 1):
        for ln in pg.split('\n'):
            if rx.search(ln):
                hits.append((i, ln))
    return hits


# ---------------------------------------------------------------- AO sections
AO_HEAD = re.compile(r'^\s*(AO\d)\s+(.{3,60}?)\s*$')


AO_BARE = re.compile(r'^\s*(AO\d)\s*$')


def assessment_objectives(pgs):
    """The AO definitions, from 'The assessment objectives (AOs) are:'.

    Two layouts. Most syllabuses give each AO a name on its own line ('AO1
    Knowledge and understanding'). Some give only the number and put the whole
    definition beneath it (9618). The second must not be read as the first, or
    the weighting-table rows get taken for AO names.
    """
    out = []
    for i, pg in enumerate(pgs, 1):
        if 'assessment objectives (AOs) are' not in pg:
            continue
        lines = pg.split('\n')
        start = next(k for k, ln in enumerate(lines) if 'assessment objectives (AOs) are' in ln)
        end = next((k for k, ln in enumerate(lines) if k > start and
                    re.search(r'Weighting for assessment objectives', ln)), len(lines))
        block = lines[start + 1:end]
        if any(AO_BARE.match(ln) for ln in block):
            cur = None
            for ln in block:
                m = AO_BARE.match(ln)
                if m:
                    cur = {'code': m.group(1), 'name': None, 'can_do': [],
                           'name_note': 'the syllabus gives this objective a number and a '
                                        'definition, not a name',
                           'source': {'page': i, 'section': '2 Syllabus overview'},
                           'verbatim': m.group(1)}
                    out.append(cur)
                elif cur is not None and ln.strip() and not ln.strip().startswith('Candidates'):
                    if cur['can_do']:
                        cur['can_do'][-1] = norm(cur['can_do'][-1] + ' ' + ln)
                    else:
                        cur['can_do'].append(norm(ln))
            for a in out:
                a['verbatim'] = a['can_do'][0][:120] if a['can_do'] else a['code']
            return out
        break
    for i, pg in enumerate(pgs, 1):
        if 'assessment objectives (AOs) are' not in pg:
            continue
        lines = pg.split('\n')
        cur = None
        for ln in lines:
            m = AO_HEAD.match(ln)
            if m:
                cur = {'code': m.group(1), 'name': norm(m.group(2)),
                       'can_do': [], 'source': {'page': i, 'section': '2 Syllabus overview'},
                       'verbatim': norm(ln)}
                out.append(cur)
            elif cur is not None and ln.strip().startswith(('•', '•')):
                cur['can_do'].append(norm(ln.strip('• •')))
            elif cur is not None and ln.strip() and not ln.strip().startswith('Candidates'):
                if cur['can_do'] and len(ln) - len(ln.lstrip()) > 8:
                    cur['can_do'][-1] = norm(cur['can_do'][-1] + ' ' + ln)
        if out:
            break
    return out


NUMROW = re.compile(r'^\s*(AO\d)(?:\s+([A-Za-z][^\d]{2,59}?))?\s{2,}((?:\d{1,3}\s+){0,9}\d{1,3})\s*$')


def ao_weights(pgs):
    """Both weighting tables: the qualification, and each component.

    The component table is the one that was previously inferred. It is a row per
    AO with one number per paper, in the column order the table's own header
    gives, so the header is read rather than assumed.
    """
    qual, comp, src = {}, {}, {}
    routes = {}
    qcols = []
    for i, pg in enumerate(pgs, 1):
        if 'Weighting for assessment objectives' not in pg and \
           'percentage of each component' not in pg:
            continue
        block, mode, order = pg.split('\n'), None, []
        for ln in block:
            if 'percentage of the qualification' in ln or 'percentage of each qualification' in ln:
                mode = 'qual'
                continue
            if mode == 'qual' and re.search(r'Weighting in', ln):
                qcols = re.findall(r'Weighting in\s+(AS Level|A Level|IGCSE|O Level)', ln)
                continue
            if 'percentage of each component' in ln:
                mode = 'comp'
                continue
            if mode == 'comp' and re.search(r'Paper\s*\d', ln):
                order = re.findall(r'Paper\s*(\d)', ln)
                continue
            m = NUMROW.match(ln)
            if not m:
                continue
            nums = [int(x) for x in m.group(3).split()]
            if mode == 'qual' and len(nums) >= 2 and len(qcols) == len(nums):
                for col, v in zip(qcols, nums):
                    routes.setdefault(col, {})[m.group(1)] = v
                src.setdefault('qualification', {'page': i,
                                                 'section': '2 Syllabus overview',
                                                 'table': 'Assessment objectives as a '
                                                          'percentage of each qualification',
                                                 'columns': qcols, 'rows': []})
                src['qualification']['rows'].append(norm(ln))
            elif mode == 'qual' and len(nums) == 1:
                qual[m.group(1)] = nums[0]
                src.setdefault('qualification', {'page': i,
                                                 'section': '2 Syllabus overview',
                                                 'table': 'Assessment objectives as a '
                                                          'percentage of the qualification',
                                                 'rows': []})
                src['qualification']['rows'].append(norm(ln))
            elif mode == 'comp' and order and len(nums) == len(order):
                for p, v in zip(order, nums):
                    comp.setdefault('P' + p, {})[m.group(1)] = v
                src.setdefault('per_component', {'page': i,
                                                 'section': '2 Syllabus overview',
                                                 'table': 'Assessment objectives as a '
                                                          'percentage of each component',
                                                 'column_order': ['Paper ' + p for p in order],
                                                 'rows': []})
                src['per_component']['rows'].append(norm(ln))
    return qual, comp, src, routes


# --------------------------------------------------------- the command words
CW_ROW = re.compile(r'^\s{2,}([A-Z][a-z]{1,11}(?:\s\([a-z]+\))?)\s{3,}([a-z(].{6,})$')


def command_words(pgs):
    """The command-word table in section 4, followed across page breaks.

    Two columns: word, and what it means. A meaning wraps onto following lines
    indented to its column. The table can run onto the next page (9618's does,
    with State, Suggest, Summarise and Write), so reading stops at the next
    section heading, not at the page footer. Stopping at the footer once dropped
    four of 27 words silently.
    """
    start = None
    for i, pg in enumerate(pgs):
        if re.search(r'^\s*Command words\s*$', pg, re.M) and \
           re.search(r'Command word\s+What it means', pg, re.I):
            start = i
            break
    if start is None:
        return [], None
    rows, cur, col, started = [], None, None, False
    for i in range(start, min(start + 3, len(pgs))):
        pg = pgs[i]
        ended = False
        for ln in pg.split('\n'):
            if not started:
                if re.search(r'Command word\s+What it means', ln, re.I):
                    started = True
                continue
            if re.search(r'Back to contents|cambridgeinternational\.org|syllabus for 20\d\d', ln):
                continue
            if re.match(r'^\s*\d\s+[A-Z][a-z]', ln) or re.match(r'^\s*(What else you need|Before you start)', ln.strip()):
                ended = True
                break
            m = CW_ROW.match(ln)
            if m:
                cur = {'word': m.group(1), 'meaning': norm(m.group(2)),
                       'source': {'page': i + 1, 'section': '4 Details of the assessment',
                                  'table': 'Command words'},
                       'verbatim': norm(ln)}
                col = ln.index(m.group(2))
                rows.append(cur)
            elif cur is not None and ln.strip():
                ind = len(ln) - len(ln.lstrip())
                if col is not None and abs(ind - col) <= 4 and ln.strip()[0].islower():
                    cur['meaning'] = norm(cur['meaning'] + ' ' + ln)
                    cur['verbatim'] = norm(cur['verbatim'] + ' ' + ln)
        if ended:
            break
    return rows, start + 1


# -------------------------------------------------------------- the papers
# 'Paper 1 – Reading' in most syllabuses, 'Paper 1 Multiple Choice' in some (9702);
# the dash is optional but the name must start with a capital
PAPER_HEAD = re.compile(r'^\s*(Paper\s+\d)\s*(?:[–—-]\s*)?([A-Z].{2,60}?)\s*$')
PAPER_SPEC = re.compile(r'(?:(Written paper|Multiple-choice paper|Practical test)[, ]+)?'
                        r'(?:(\d+)\s*hours?\s*)?(?:(\d+)\s*minutes?)?[, ]*(\d+)\s*marks', re.I)


def papers(pgs):
    out = []
    for i, pg in enumerate(pgs, 1):
        lines = pg.split('\n')
        for j, ln in enumerate(lines):
            m = PAPER_HEAD.match(ln)
            if not m or re.match(r'Paper\s+\d', m.group(2)):
                continue          # a two-column overview line: 'Paper 1    Paper 2'
            spec = None
            for k in range(j + 1, min(j + 4, len(lines))):
                s = PAPER_SPEC.search(lines[k])
                if s and s.group(4):
                    spec = (lines[k], s)
                    break
            if not spec:
                continue
            line, s = spec
            hrs = int(s.group(2) or 0)
            mins = int(s.group(3) or 0)
            body = []
            for k in range(j + 1, len(lines)):
                t = lines[k].strip()
                if PAPER_HEAD.match(lines[k]) or t.startswith('Back to contents'):
                    break
                if t and t != norm(line):
                    body.append(t)
            sect4 = bool(re.search(r'(Written paper|Multiple-choice paper|Practical test)', line, re.I))
            out.append({'paper': m.group(1).split()[-1], '_sect4': sect4,
                        'name': norm(m.group(2)),
                        'marks': int(s.group(4)),
                        'duration_minutes': hrs * 60 + mins,
                        'description': norm(' '.join(body))[:900],
                        'source': {'page': i, 'section': '4 Details of the assessment'},
                        'verbatim': '%s %s' % (norm(ln), norm(line))})
    # Prefer the section-4 statement ('Written paper, 1 hour 15 minutes, 40 marks'),
    # which describes one paper; a two-column overview interleaves two papers and
    # once named Paper 1 'Paper 4'. Among section-4 entries, keep the fullest.
    best = {}
    for p in out:
        b = best.get(p['paper'])
        if (b is None or (p['_sect4'] and not b['_sect4']) or
                (p['_sect4'] == b['_sect4'] and len(p['description']) > len(b['description']))):
            best[p['paper']] = p
    res = [best[k] for k in sorted(best)]
    for p in res:
        p.pop('_sect4', None)
    return res


def transcription(code, pgs):
    """Hand-transcribed facts, for layouts the automatic readers cannot parse.

    A transcription is not a summary. Each fact names its page and quotes the
    lines that state it, and every quote is checked against that page here,
    before anything is built. A transcribed value whose quote is not on its page
    stops the build - that is the difference between transcribing and recalling.
    """
    p = os.path.join(REPO, SUBJECTS[code]['ws'], 'curriculum', 'syllabus-transcription.json')
    if not os.path.exists(p):
        return {}
    t = json.load(open(p))
    bad = []
    for kind in ('papers', 'notes'):
        for x in t.get(kind, []):
            pg = norm(pgs[x['page'] - 1]) if 1 <= x['page'] <= len(pgs) else ''
            for q in x['quotes']:
                if norm(q) not in pg:
                    bad.append('%s p.%d: %r' % (x.get('paper', x.get('topic', kind)), x['page'], q))
    if bad:
        raise SystemExit('Transcription quotes not found on their cited page - fix the '
                         'transcription, do not fix the check:\n  ' + '\n  '.join(bad))
    return t


def stated_shares(pgs, pps, route):
    """Each paper's weight as the syllabus STATES it.

    A paper's weight is not its share of the marks. 0455 weights its 30-mark and
    90-mark papers 30% and 70%, not 25% and 75%; 9702 weights 40, 60 and 40 marks
    as 31%, 46% and 23%. The stated figure is the one the qualification's AO
    weights reconcile to, so it is read from the page, never computed.

    Two layouts: an IGCSE overview line 'Reading    50%   Directed Writing   50%',
    and an AS overview block ending '31% of the AS Level'.
    """
    out = {}
    for i, pg in enumerate(pgs, 1):
        if not re.search(r'%', pg) or 'Assessment overview' not in pg and 'Components' not in pg:
            continue
        lines = pg.split('\n')
        for p in pps:
            if p['paper'] in out:
                continue
            nm = re.escape(p['name'][:22])
            for k, ln in enumerate(lines):
                mm = re.search(nm + r'.{0,30}?\s{2,}(\d{1,3}(?:\.\d)?)%', ln)
                if mm:
                    out[p['paper']] = (float(mm.group(1)), i, norm(ln))
                    break
                if re.search(nm, ln) and route:
                    col = re.search(nm, ln).start()
                    for ln2 in lines[k + 1:k + 12]:
                        for m2 in re.finditer(r'(\d{1,3})% of the ' + re.escape(route), ln2):
                            if abs(m2.start() - col) < 40:
                                out[p['paper']] = (float(m2.group(1)), i, norm(ln2[m2.start():m2.end()]))
                                break
                        if p['paper'] in out:
                            break
                    if p['paper'] in out:
                        break
    return out


def build(code):
    m = SUBJECTS[code]
    pgs = pages(os.path.join(REPO, m['pdf']))
    tr = transcription(code, pgs)
    aos = assessment_objectives(pgs)
    qual, comp, wsrc, routes = ao_weights(pgs)
    route = m.get('route')
    if routes:
        if not route or route not in routes:
            raise SystemExit('%s states weights for routes %s; name the workspace route '
                             'rather than guess one' % (code, sorted(routes)))
        qual = routes[route]
        cols = (wsrc.get('qualification') or {}).get('columns') or []
        k = cols.index(route)
        for row in (wsrc.get('qualification') or {}).get('rows', []):
            nums = [int(x) for x in re.findall(r'(?<![\w.])(\d{1,3})(?![\w.])', row)]
            code_ = re.match(r'(AO\d)', row).group(1)
            if len(nums) != len(cols) or nums[k] != qual[code_]:
                raise SystemExit('%s: %s row %r does not put %s under the %s column'
                                 % (code, code_, row, qual.get(code_), route))
    cws, cwpage = command_words(pgs)
    if tr.get('ao_per_component') and not comp:
        comp = tr['ao_per_component']
        wsrc['per_component'] = {'page': next((n['page'] for n in tr.get('notes', [])
                                               if n['topic'] == 'per-component weighting'), None),
                                 'section': '2 Syllabus overview', 'method': 'transcribed',
                                 'rows': [q for n in tr.get('notes', [])
                                          if n['topic'] == 'per-component weighting' for q in n['quotes']]}
    pps = papers(pgs)
    # A transcription exists because the reader mishandles this syllabus's layout,
    # so where one states a paper it replaces what the reader produced.
    trp = {x['paper'] for x in tr.get('papers', [])}
    pps = [p for p in pps if p['paper'] not in trp]
    for x in tr.get('papers', []):
        if True:
            pps.append({'paper': x['paper'], 'name': x['name'], 'marks': x['marks'],
                        'duration_minutes': x['duration_minutes'],
                        'description': x['description'],
                        'share_of_route': x.get('share_of_route'),
                        'questions': x.get('questions'),
                        'source': {'page': x['page'], 'section': x.get('section', ''),
                                   'method': 'transcribed; quotes verified against the page'},
                        'verbatim': ' | '.join(x['quotes'])})
    pps.sort(key=lambda p: int(p['paper']))
    if m.get('papers_in_route'):
        pps = [p for p in pps if p['paper'] in m['papers_in_route']]
    for p in pps:
        p['ao_split'] = comp.get('P' + p['paper'], {})
        tot = sum(x['marks'] for x in pps) or 1
    shares = stated_shares(pgs, pps, route)
    for p in pps:
        if p.get('share_of_route'):
            p['weight_percent'] = p['share_of_route']
            p['weight_provenance'] = 'syllabus, transcribed with the paper'
        elif p['paper'] in shares:
            v, pg_, q = shares[p['paper']]
            p['weight_percent'] = v if v % 1 else int(v)
            p['weight_provenance'] = 'syllabus, page %d: %s' % (pg_, q)
        else:
            p['weight_percent'] = round(100.0 * p['marks'] / tot)
            p['weight_provenance'] = ('NOT STATED in the syllabus; computed from marks. '
                                      'Check the assessment overview before relying on it.')
    wpage = (wsrc.get('qualification') or {}).get('page')
    for a in aos:
        a['qualification_weight_percent'] = qual.get(a['code'])
        if a['qualification_weight_percent'] is None:
            # a weight the table states in words, not a number, is still stated
            for i, pg in enumerate(pgs, 1):
                for ln in pg.split('\n'):
                    if re.match(r'^\s*%s\b' % a['code'], ln) and 'Separately endorsed' in ln:
                        a['qualification_weight_percent'] = 0
                        a['weight_note'] = 'Separately endorsed: reported apart from the grade'
                        a['weight_source'] = {'page': i, 'verbatim': norm(ln)}
                        break
    return {
        'facts_id': 'SYLFACTS-CIE-%s-IGCSE-2026' % code,
        'generated_at': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        'generated_by': 'mine_syllabus.py',
        'authority': m['title'] + ' syllabus for 2026.',
        'source_document': m['pdf'],
        'pages_in_document': len(pgs),
        'rule': 'STEP ZERO of the pipeline. Every value here is transcribed from the '
                'syllabus and carries the page that states it. Nothing downstream may '
                'assert an assessment objective weighting, a per-paper split, a paper '
                'structure or a command word that is not in this file. A value without '
                'a citation is a value we do not have.',
        'assessment_objectives': aos,
        'route': route or 'single route',
        'papers_sat': m.get('papers_sat'), 'first_exam': m.get('first_exam'),
        'ao_weights': {'qualification_percent': qual, 'per_component_percent': comp,
                       'by_route': routes or None, 'source': wsrc},
        'papers': pps,
        'command_words': cws,
        'transcribed_notes': tr.get('notes', []),
        'command_word_table': {'page': cwpage, 'section': '4 Details of the assessment',
                               'count': len(cws),
                               'note': 'This table is the complete list the syllabus '
                                       'publishes. A word outside it that appears in the '
                                       'papers is recorded separately as observed-not-listed; '
                                       'a word inside it that never appears is recorded as '
                                       'listed-not-observed. Neither is ever guessed.'},
    }


if __name__ == '__main__':
    for code in (sys.argv[1:] or ['0450', '0455']):
        f = build(code)
        p = os.path.join(REPO, SUBJECTS[code]['ws'], 'curriculum', 'syllabus-facts.json')
        os.makedirs(os.path.dirname(p), exist_ok=True)
        json.dump(f, open(p, 'w'), indent=1)
        print('\n%s  (%d pages)' % (code, f['pages_in_document']))
        print('  AOs            %d  %s'
              % (len(f['assessment_objectives']),
                 ', '.join('%s %s %s' % (a['code'], a['name'],
                                         a.get('weight_note') or '%s%%' % a['qualification_weight_percent'])
                           for a in f['assessment_objectives'])))
        print('  per component  %s' % json.dumps(f['ao_weights']['per_component_percent']))
        for pp in f['papers']:
            print('  Paper %s        %s, %d marks, %d min, AO %s  [p.%d]'
                  % (pp['paper'], pp['name'], pp['marks'], pp['duration_minutes'],
                     json.dumps(pp['ao_split']), pp['source']['page']))
        print('  command words  %d on page %s: %s'
              % (len(f['command_words']), f['command_word_table']['page'],
                 ', '.join(c['word'] for c in f['command_words'])))
