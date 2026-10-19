#!/usr/bin/env python3
"""Transcribe the NSSCO Biology 6116 syllabus into curriculum/syllabus-facts.json.

Written for this workspace, per TEAM-PLAYBOOK.md step 4.2: the scripts in
standard/v0.2.0-draft/mine/ are worked examples wired to another machine and to
Cambridge subjects. This reads them for method only.

Method borrowed from mine/mine_syllabus.py: pdftotext emits a form feed between
pages, so the page index is the page number, and every value carries the page
that states it plus the verbatim line. Nothing here is typed from recall.

Two page numberings exist and both are recorded:
  pdf_page     - physical page in the PDF (what pdftotext counts, what a viewer shows)
  printed_page - the number in the syllabus footer (pdf_page - 3)

Usage: python3 transcribe_syllabus.py [--out <path>]
"""
import json, os, re, subprocess, sys, datetime, argparse, html

PDF = 'Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_BIOLOGY_SYLLABUS.pdf'
WS = 'work/nam-6116-nssco-2026'
PAGE_OFFSET = 3           # printed_page + 3 == pdf_page, verified on pp.37/40 and 39/42
CONTENT_PAGES = range(9, 38)   # PDF pages carrying the TOPIC/GENERAL/SPECIFIC table
OUTLINE_PAGES = (7, 8)         # PDF pages carrying the topic/sub-topic list


def pages(pdf):
    """pdftotext -layout, split on form feed. Index 0 == PDF page 1."""
    out = subprocess.run(['pdftotext', '-layout', pdf, '-'],
                         capture_output=True, text=True, check=True).stdout
    return out.split('\f')


def printed(pdf_page):
    return pdf_page - PAGE_OFFSET


# The PDF renders list bullets as U+F0B7, a private-use glyph. It is not
# whitespace, so it survives .strip() and sits at the head of every objective -
# breaking any pattern anchored on the leading verb, and leaking into anything
# built from this text.
BULLET = re.compile(r'^[\uf0b7\u2022\u00b7\uf0a7\uf0fc\s]+')


def debullet(t):
    # leading glyphs, and any that survive mid-text from a wrapped continuation
    return re.sub(r'[\uf0b7\u2022\uf0a7\uf0fc]', ' ', BULLET.sub('', t)).strip()


def cite(pdf_page, line):
    return {'pdf_page': pdf_page, 'printed_page': printed(pdf_page),
            'quote': ' '.join(line.split())}


# The syllabus renders two codes irregularly: "4.3.5." carries a trailing dot
# (PDF p.30) and "4.4 .3" has a space inside it (PDF p.32). Tolerate both, then
# normalise, or those two sub-topics lose every objective they own.
CODE = re.compile(r'^(\d+(?:\s*\.\s*\d+)*)\s*\.?\s+(.*\S)\s*$')

# Lines that repeat in the SPECIFIC OBJECTIVES column but are not objectives:
# the column's own lead-in, and topic-intro prose that wraps into the column.
# 28 "Learners should be able to:" headers were being registered as objectives.
NOT_AN_OBJECTIVE = re.compile(
    r'^(learners (should|will)\b|teachers should\b|this topic\b|the learning content\b|'
    r'specific objectives\b|general objectives\b|cesses and skills)', re.I)


def norm(code):
    return re.sub(r'\s+', '', code).rstrip('.')


def outline(pgs):
    """Topic and sub-topic list from the content outline pages."""
    items = []
    for pno in OUTLINE_PAGES:
        for raw in pgs[pno - 1].split('\n'):
            line = raw.strip()
            m = re.match(r'^Topic\s+(\d+):\s*(.+?)\s*$', line)
            if m:
                items.append({'code': m.group(1), 'title': m.group(2),
                              'level': 'topic', 'source': cite(pno, raw)})
                continue
            m = CODE.match(line)
            # "5 LEARNING CONTENT" is the section heading, not sub-topic 5. Without
            # this guard the outline carries 71 entries against the content table's
            # 70, with code "5" appearing twice.
            if m and not line.startswith('NSSCO') and not m.group(2).isupper():
                items.append({'code': norm(m.group(1)), 'title': m.group(2),
                              'level': 'sub_topic', 'source': cite(pno, raw)})
    return items


def columns(pgs):
    """Specific objectives per sub-topic, read from word geometry, not text order.

    The -layout text cannot be trusted for this table. Its column offsets move
    from line to line, so on PDF p.27 (4.1, 4.2.1) the GENERAL column bled into
    SPECIFIC ("t cell define mitosis...", "mportant for of stages required") and
    ten bullets collapsed into one; topic-heading prose ("of teaching time)")
    was registered as an objective; wrapped lines in 3.6.2.3 were read as new
    bullets; and footer page numbers stuck to the last bullet on each page.

    pdftotext -bbox gives every word its position, and the bullet glyph U+F0B7 is
    a word of its own. So: a word is in SPECIFIC when its x is at or right of
    that column's header; a new objective starts only at a bullet glyph sitting
    at the column's bullet x; a glyph further right is a nested list item; a
    line carrying a bare topic number (2, 3, 4, 5) is the topic heading that
    spans all three columns and is skipped whole.
    """
    pdf_words = bbox_words(PDF, CONTENT_PAGES)
    rows = []
    notes = CONTENT_NOTES
    for pno in CONTENT_PAGES:
        words = pdf_words.get(pno, [])
        g = next((w for w in words if w[2] == 'GENERAL'), None)
        s = next((w for w in words if w[2] == 'SPECIFIC'), None)
        if not (g and s):
            continue
        g_x, s_x, head_y = g[0], s[0], s[1]
        foot = [w[1] for w in words if w[2] == 'NSSCO' and w[1] > 400]
        foot_y = min(foot) if foot else 1e9
        body = [w for w in words if head_y + 15 < w[1] < foot_y - 1]
        # the "Learners should be able to:" lead-in sits one line under the header
        # A page can repeat the header lower down; drop every header row and its lead-in.
        hdr_ys = [w[1] for w in words if w[2] in ('SPECIFIC', 'GENERAL', 'TOPIC')]
        body = [w for w in body if not any(-2 < w[1] - hy < 15.5 for hy in hdr_ys)]

        topic_col = sorted([w for w in body if w[0] < g_x - 3], key=lambda w: (w[1], w[0]))
        heading_ys = [w[1] for w in topic_col if w[0] < 100 and re.fullmatch(r'\d', w[2])]
        codes = []
        for hy in heading_ys:                       # topic rows own no objectives
            line = sorted(v for v in body if abs(v[1] - hy) < 2)
            raw = ' '.join(v[2] for v in line)
            codes.append((hy, line[0][2], ' '.join(v[2] for v in line[1:]), line))
        for w in topic_col:
            # "1.2.4Basic" and "5.4Human" arrive as one word: the code is glued to its title
            cm = re.fullmatch(r'(\d+(?:\.\d+)+\.?)(.*)', w[2])
            if w[0] < 100 and cm:
                line = [v for v in topic_col if abs(v[1] - w[1]) < 2]
                # "4.4 .3" is typeset as two words; "Basic" can start left of x=112
                frag = [v for v in line if v is not w and v[0] < 112 and re.fullmatch(r'[\d.]+', v[2])]
                code_txt = cm.group(1) + ''.join(v[2] for v in frag)
                title = ' '.join([cm.group(2)] + [v[2] for v in line
                                                  if v is not w and v not in frag]).strip()
                codes.append((w[1], norm(code_txt), title, line))
        for y, code, title, line in sorted(codes, key=lambda c: c[0]):
            raw = ' '.join(v[2] for v in sorted(line))
            rows.append({'code': code, 'title': title, 'specific_objectives': [],
                         'source': cite(pno, raw), '_y': (pno, y)})

        spec = [w for w in body if w[0] >= s_x - 3
                and not any(abs(w[1] - hy) < 2 for hy in heading_ys)]
        # glyphs sit ~3.5pt above their text line; align them before grouping
        # Sub- and superscripts (CO2, C6H12O6, ms-1) are smaller words set a few
        # points off the baseline. Lines are built from full-size words first, then
        # each small word joins the nearest line.
        full_h = sorted(w[4] for w in spec)[len(spec) // 2] if spec else 10
        small = [w for w in spec if w[4] < 0.8 * full_h and not is_glyph(w[2])]
        eff = sorted(((w[1] + (3.55 if is_glyph(w[2]) else 0), w[0], w[2], w[3])
                      for w in spec if w not in small))
        lines = []
        for y, x, t, x2 in eff:
            if lines and abs(lines[-1][0] - y) < 4:
                lines[-1][1].append((x, t, x2))
            else:
                lines.append([y, [(x, t, x2)]])
        # A line can open with a taller symbol (an arrow at 12pt), so measure from
        # the baseline of its body-text words, not from its first word.
        base = {id(ln): max((y for y, x, t, x2 in eff if any(x == v[0] and t == v[1] for v in ln[1])
                             and abs(y - ln[0]) < 4), default=ln[0]) for ln in lines}
        for w in small:
            near = min(lines, key=lambda ln: abs(base[id(ln)] - w[1]), default=None)
            if near is not None and abs(base[id(near)] - w[1]) < 9:
                near[1].append((w[0], w[2], w[3]))
        for y, ws in lines:
            ws.sort()
            first_x, first_t = ws[0][0], ws[0][1]
            owner = [r for r in rows if r['_y'][0] < pno or (r['_y'][0] == pno and r['_y'][1] <= y + 4)]
            if not owner:
                continue
            tgt = owner[-1]['specific_objectives']
            text, prev_x2 = [], None
            for x, t, x2 in ws:
                if is_glyph(t) and x > s_x + 5:
                    text.append(NEST)                   # nested list item
                elif not is_glyph(t):
                    # subscripts are separate words abutting their element (C,6,H,12,O,6);
                    # rejoin them rather than spacing them out
                    if text and prev_x2 is not None and x - prev_x2 < 0.8 and text[-1] != NEST:
                        text[-1] += t
                    else:
                        text.append(t)
                prev_x2 = x2
            # a real semicolon at a line end is text and must survive; only the
            # nested-item marker is trimmed
            txt = ' '.join(text).strip(' ' + NEST)
            txt = re.sub(r'\s*' + NEST + r'\s*', '; ', txt)
            if not txt:
                continue
            if txt.startswith('NB:'):
                notes.append({'note': txt, 'source': cite(pno, txt),
                              'sub_topic': owner[-1]['code']})
                continue
            if is_glyph(first_t) and abs(first_x - s_x) <= 3:
                tgt.append({'text': txt, 'source': cite(pno, txt)})
            elif tgt:
                sep = '; ' if (is_glyph(ws[0][1]) and ws[0][0] > s_x + 5) else ' '
                tgt[-1]['text'] = (tgt[-1]['text'] + sep + txt).replace(':;', ':')
            # an unbulleted line with no bullet before it in its row is prose, not an objective
    for r in rows:
        r.pop('_y', None)
        for o in r['specific_objectives']:
            o['text'] = ' '.join(o['text'].split())
    return rows


BULLET_GLYPH = '\uf0b7'
NEST = '\u2023'      # internal marker for a nested list item; never reaches the output
CONTENT_NOTES = []   # unbulleted teacher notes in the SPECIFIC column ("NB: ...")


def is_glyph(t):
    """A list bullet: one private-use or bullet character standing as its own word."""
    return len(t) == 1 and (0xE000 <= ord(t) <= 0xF8FF or t in '\u2022\u00b7\u25aa')


def bbox_words(pdf, page_range):
    """{pdf_page: [(xMin, yMin, text), ...]} from pdftotext -bbox."""
    first, last = page_range[0], page_range[-1]
    xml = subprocess.run(['pdftotext', '-bbox', '-f', str(first), '-l', str(last), pdf, '-'],
                         capture_output=True, text=True, check=True).stdout
    out = {}
    for pno, page in zip(page_range, re.findall(r'<page .*?</page>', xml, re.S)):
        out[pno] = [(float(x), float(y), html.unescape(t), float(x2), float(y2) - float(y))
                    for x, y, x2, y2, t in re.findall(
                        r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',
                        page)]
    return out


EXCLUSION = re.compile(r'(will not be assessed|is not required|not required|'
                       r'knowledge of .{0,60} is not expected|no knowledge of|'
                       r'is not expected|beyond the scope)', re.I)


def exclusions(pgs, rows):
    """Every limit the syllabus states inside its content.

    Read from the JOINED objective text, not from single -layout lines: two limits
    wrap across lines ("details of beta cells are not / required", 3.14) and the line
    scan missed them, along with "no reference to full names is required" (3.4),
    which is a limit phrased positively. Each limit carries its sub-topic, the
    whole objective it qualifies, and the page.
    """
    pat = re.compile(r'\(([^()]*?(?:not required|no reference to [^()]*? is required|'
                     r'is not expected|will not be assessed)[^()]*)\)', re.I)
    found = []
    for r in rows:
        for o in r['specific_objectives']:
            for m in pat.finditer(o['text']):
                found.append({'sub_topic': r['code'], 'limit': m.group(1).strip(),
                              'objective': o['text'], 'pdf_page': o['source']['pdf_page'],
                              'printed_page': o['source']['printed_page'], 'quote': m.group(0)})
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(WS, 'curriculum', 'syllabus-facts.json'))
    args = ap.parse_args()

    if not os.path.exists(PDF):
        sys.exit('syllabus PDF not found: %s' % PDF)
    pgs = pages(PDF)

    ao_subs, ao_ctx = assessment_objectives(pgs)
    ol = outline(pgs)
    rows = columns(pgs)
    # The topic column wraps, so its titles truncate. Prefer the outline's.
    titles = {o['code']: o['title'] for o in ol}
    for r in rows:
        if r['code'] in titles:
            r['title_from_table'] = r['title']
            r['title'] = titles[r['code']]

    facts = {
        'facts_id': 'SYLFACTS-NAM-6116-NSSCO-2026',
        'generated_at': datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'generated_by': 'work/nam-6116-nssco-2026/planning/transcribe_syllabus.py',
        'authority': 'NSSCO Biology Syllabus, NIED 2018 (syllabus code 6116, Ordinary Level, Grades 10-11)',
        'source_document': PDF,
        'pages_in_document': len([p for p in pgs if p.strip()]),
        'page_numbering': {
            'pdf_page': 'physical page in the PDF, what pdftotext counts',
            'printed_page': 'the number printed in the syllabus footer',
            'offset': 'pdf_page = printed_page + %d' % PAGE_OFFSET,
        },
        'rule': ('STEP ZERO. Every value is transcribed from the syllabus with the page that '
                 'states it and the verbatim line. No AO weight, per-paper split or command '
                 'word is written from memory. Where the syllabus does not state something, '
                 'this file says so.'),
        'provenance': 'syllabus',
        'assessment_objective_detail': ao_subs,
        'assessment_objective_context_lines': ao_ctx,
        'topic_outline': ol,
        'content': rows,
        'content_rows_missing_from_outline': sorted(
            {r['code'] for r in rows} - {o['code'] for o in ol}),
        'outline_codes_with_no_content_row': sorted(
            {o['code'] for o in ol} - {r['code'] for r in rows}),
        'stated_exclusions': exclusions(pgs, rows),
        'content_notes': CONTENT_NOTES,
    }
    facts.update(assessment(pgs))

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, 'w') as f:
        json.dump(facts, f, indent=2, ensure_ascii=False)

    print('syllabus-facts -> %s' % args.out)
    print('  %d outline entries' % len(facts['topic_outline']))
    print('  %d content rows, %d specific objectives'
          % (len(facts['content']), sum(len(r['specific_objectives']) for r in facts['content'])))
    print('  %d stated exclusions' % len(facts['stated_exclusions']))


# --- assessment transcription -------------------------------------------------
# Separated from the content table because these values are the ones that, when
# typed from recall rather than read, mis-shape every item in a subject
# (mine/mine_syllabus.py docstring; AGENTS.md rule 0). Each is pinned to the page
# that states it and the verbatim line.
AO_PAGE, SCHEME_PAGE, GRID_PAGE = 38, 39, 40
GLOSSARY_PAGES = (42, 43)
PRACTICAL_PAGE = 44
LINE_HEIGHT = 13.0       # one glossary line; Outline and Predict sit one line below their meaning
TERM_COL_MAX = 150        # x below this is the term column, above it the meaning column


def find_line(pgs, pdf_page, pattern):
    """First line on a page matching pattern, with its citation."""
    for raw in pgs[pdf_page - 1].split('\n'):
        if re.search(pattern, raw, re.I):
            return cite(pdf_page, raw)
    return None


AO_PAGES = (38, 39)
SUB_AO = re.compile(r'^([ABC])([1-7])\s+(.*\S)\s*$')


def assessment_objectives(pgs):
    """A1-C5 in the syllabus's own words, with each AO's lead-in and conditions.

    The sub-objectives wrap, and the parenthetical conditions on C1-C3 carry the
    qualification that makes them assessable, so a line-level read that drops the
    continuation loses the condition rather than merely shortening the text.
    """
    subs, context, current = [], [], None
    for pno in AO_PAGES:
        for raw in pgs[pno - 1].split('\n'):
            line = raw.rstrip()
            if not line.strip() or line.strip().startswith('NSSCO') or line.strip().isdigit():
                continue
            m = SUB_AO.match(line.strip())
            if m:
                current = {'ao': m.group(1), 'index': int(m.group(2)),
                           'code': m.group(1) + m.group(2), 'text': m.group(3),
                           'source': cite(pno, raw)}
                subs.append(current)
            elif current is not None and line.startswith('      ') and not re.match(r'^\s*[ABC67]\b', line.strip()):
                current['text'] += ' ' + line.strip()          # wrapped continuation
            else:
                current = None
                if len(line.strip()) > 25:
                    context.append(cite(pno, raw))
    for sdict in subs:
        sdict['text'] = debullet(' '.join(sdict['text'].split()))
    return subs, context


def glossary(pdf):
    """Command words, read off the glossary's geometry rather than its text order.

    Two reasons the plain -layout text cannot be trusted here, both found in this
    PDF: pages 42 and 43 share a y-space when extracted together, and the Word
    table renders some cells with the meaning's first line one line ABOVE its
    term (Outline at y=687.72 has "implies brevity" at y=675.00, while Measure
    and List align normally). Reading order therefore crosses Outline/Predict.

    Each meaning line is assigned to its NEAREST term by vertical distance, which
    is correct for both the aligned and the offset rows.
    """
    xml = subprocess.run(['pdftotext', '-bbox-layout', '-f', str(GLOSSARY_PAGES[0]),
                          '-l', str(GLOSSARY_PAGES[-1]), pdf, '-'],
                         capture_output=True, text=True, check=True).stdout
    skip = lambda t: ('GLOSSARY' in t.upper() or t.startswith('Learners should appreciate')
                      or t.strip().isdigit() or t.startswith('NSSCO'))
    out = []
    for pno, page in zip(GLOSSARY_PAGES, re.findall(r'<page .*?</page>', xml, re.S)):
        rows = []
        for xmin, ymin, body in re.findall(r'<line xMin="([\d.]+)" yMin="([\d.]+)"[^>]*>(.*?)</line>',
                                           page, re.S):
            w = ' '.join(x.strip() for x in re.findall(r'<word[^>]*>(.*?)</word>', body, re.S)).strip()
            if w:
                rows.append((float(ymin), float(xmin), w))
        rows.sort()
        terms = [(y, t) for y, x, t in rows if x < TERM_COL_MAX and not skip(t)]
        merged = []
        for y, t in terms:                       # a term that wrapped onto its own line
            if merged and re.match(r'^[a-z]', t):
                merged[-1] = (merged[-1][0], merged[-1][1] + ' ' + t)
            else:
                merged.append((y, t))
        terms = merged
        buckets = {y: [] for y, _ in terms}
        for y, x, t in rows:
            if x >= TERM_COL_MAX and not skip(t) and terms:
                eligible = [kt for kt in terms if kt[0] <= y + LINE_HEIGHT]
                best = (max(eligible, key=lambda kt: kt[0]) if eligible
                        else min(terms, key=lambda kt: abs(kt[0] - y)))
                buckets[best[0]].append((y, t))
        for y, t in terms:
            out.append({'word': re.sub(r'^\(([ab])\)\s*', '', t),
                        'sense': (re.match(r'^\(([ab])\)', t) or [None, None])[1],
                        'meaning': ' '.join(m for _, m in sorted(buckets[y])),
                        'source': {'pdf_page': pno, 'printed_page': printed(pno), 'quote': t}})
    return out


def assessment(pgs):
    grid_rows, papers = [], []
    # Specification grid: AO letter, overall weighting, then marks per paper.
    for raw in pgs[GRID_PAGE - 1].split('\n'):
        m = re.match(r'\s*([ABC])\s+(.*?)\s{2,}(\d+%.*?|\d+%)\s{2,}(\d+)\s*marks?\s+(\d+)\s*marks?\s+(\d+)',
                     raw)
        if m:
            weighting = m.group(3).strip()
            if weighting.count('(') > weighting.count(')'):
                # "47% (not more than" wraps; the ceiling itself is on a later line.
                tail = re.search(r'(\d+%\s*recall\))', pgs[GRID_PAGE - 1])
                if tail:
                    weighting = weighting + ' ' + tail.group(1)
            grid_rows.append({'ao': m.group(1), 'name_fragment': m.group(2).strip(),
                              'overall_weighting': weighting,
                              'paper_1_marks': int(m.group(4)), 'paper_2_marks': int(m.group(5)),
                              'paper_3_marks': int(m.group(6)), 'source': cite(GRID_PAGE, raw)})
    # Paper weightings table on the same page.
    for raw in pgs[GRID_PAGE - 1].split('\n'):
        m = re.match(r'\s*Paper\s+([123])\b.*?(\d+)%', raw)
        if m:
            papers.append({'paper': m.group(1), 'weighting_percent': int(m.group(2)),
                           'source': cite(GRID_PAGE, raw)})
    # Paper marks and durations from the scheme-of-assessment table.
    durations = []
    for raw in pgs[SCHEME_PAGE - 1].split('\n'):
        if re.search(r'\d+\s*(minutes|hour)', raw, re.I):
            durations.append(cite(SCHEME_PAGE, raw))

    aos = []
    for letter, name in [('A', 'Knowledge with understanding'),
                         ('B', 'Handling information, application and solving problems'),
                         ('C', 'Practical (experimental and investigative) skills and abilities')]:
        src = find_line(pgs, AO_PAGE, re.escape(name)) or find_line(pgs, AO_PAGE + 1, re.escape(name))
        aos.append({'ao': letter, 'name': name, 'source': src,
                    'stated_on_page': bool(src)})

    words = glossary(PDF)

    practical = []
    for raw in pgs[PRACTICAL_PAGE - 1].split('\n'):
        if re.match(r'\s*\([a-k]\)\s', raw):
            practical.append(cite(PRACTICAL_PAGE, raw))

    return {'assessment_objectives': aos, 'specification_grid': grid_rows,
            'paper_weightings': papers, 'paper_duration_lines': durations,
            'command_words': words, 'paper_3_practical_criteria': practical}


if __name__ == '__main__':
    main()
