# -*- coding: utf-8 -*-
"""The answer SHAPE per command word and tariff, derived from 168 mark schemes."""
import json, os, re, collections
ROOT = os.path.expanduser('~/mine')
def load(p): return json.load(open(os.path.join(ROOT, p)))

def report(code, expect_total):
    rows = load('%s_markscheme.json' % code)
    ok = [r for r in rows if r['cw'] and r['marks']]
    print('\n' + '=' * 92)
    print('%s  blocks %d  |  command word + tariff on %d  |  paper totals reconcile to %d'
          % (code, len(rows), len(ok), expect_total))

    print('\n--- ANSWER SHAPE: command word x tariff (n>=6) -----------------------------')
    print('%-10s %4s %5s  %-34s %s' % ('command', 'mks', 'n', 'AO tags per question', 'other'))
    grp = collections.defaultdict(list)
    for r in ok:
        grp[(r['cw'], r['marks'])].append(r)
    for (cw, t), rs in sorted(grp.items(), key=lambda x: (-len(x[1]))):
        if len(rs) < 6:
            continue
        tag = collections.Counter()
        ntag = 0
        for r in rs:
            if r['tags']:
                ntag += 1
                for k, v in r['tags'].items():
                    tag[k] += v
        cred = sorted(r['credit_tokens'] for r in rs if r['credit_tokens'])
        nb = sum(1 for r in rs if r['bands'])
        s = ''
        if ntag:
            s = ' '.join('%s%.1f' % (a, tag.get(a, 0) / float(ntag))
                         for a in ('k', 'app', 'an', 'ev'))
        extra = []
        if cred:
            extra.append('(1)-pts med %d' % cred[len(cred) // 2])
        if nb:
            extra.append('level-banded %d/%d' % (nb, len(rs)))
        print('%-10s %4d %5d  %-34s %s' % (cw, t, len(rs), s, '  '.join(extra)))

    print('\n--- AWARD GRAMMAR by tariff (what the marks are actually for) ---------------')
    by_t = collections.defaultdict(collections.Counter)
    for r in ok:
        for a in r['awards']:
            s = a['for'].lower()
            for pat, lab in (
                (r'relevant reference to (this|the) business|application|context', 'APPLICATION to the case'),
                (r'each relevant (explanation|development)|development of', 'DEVELOPED explanation'),
                (r'a full definition', 'full definition (2) / partial (1)'),
                (r'identification of (each )?(relevant )?', 'identification of a point'),
                (r'each relevant (problem|reason|factor|way|advantage|disadvantage|benefit|effect|issue|point|method|feature)',
                 'each relevant point'),
                (r'justified (decision|recommendation|conclusion)|justification', 'justified judgement'),
                (r'analysis|analys', 'analysis of a point'),
                (r'evaluation|evaluat', 'evaluation'),
                (r'diagram|axes|curve', 'correct diagram element'),
                (r'correct answer|calculation|working|formula', 'calculation step / answer'),
            ):
                if re.search(pat, s):
                    by_t[r['marks']]['%d mk %s' % (a['n'], lab)] += 1
                    break
    for t in sorted(by_t):
        tot = sum(by_t[t].values())
        if tot < 12:
            continue
        print('\n  %2d marks  (%d award clauses)' % (t, tot))
        for s, n in by_t[t].most_common(6):
            print('      %5.1f%%  %s' % (100.0 * n / tot, s))

    print('\n--- REQUIRED SKELETONS (sub-headings examiners structure answers around) ----')
    sk = collections.Counter()
    for r in rows:
        for s in r['skeleton']:
            sk[s] += 1
    for s, n in sk.most_common(16):
        print('  %4d  %s' % (n, s))

    print('\n--- TOP BAND DESCRIPTORS (extended response) --------------------------------')
    seen = collections.Counter()
    for r in rows:
        if not r['bands']:
            continue
        top = max(r['bands'], key=lambda b: b['band'])
        seen['%d-%d  %s' % (top['lo'], top['hi'], top['descriptor'])] += 1
    for s, n in seen.most_common(8):
        print('  %4d  %s' % (n, s))

    print('\n--- REFUSALS (recurring, generalised) ---------------------------------------')
    buckets = collections.Counter()
    ex = {}
    for r in rows:
        for s in r['refuse']:
            sl = s.lower()
            for pat, lab in (
                (r'no marks? for application|as application|application marks?',
                 'named context words alone do not earn the application mark'),
                (r'example', 'an example is not a definition or an explanation'),
                (r'impact on (the )?(employee|other stakeholder|customer)',
                 'answered from the wrong stakeholder\'s point of view'),
                (r'solution|solutions', 'gave a solution when the question asked for a cause/effect'),
                (r'just (stating|reproducing|describ)|description of the figures|reproducing these words',
                 'described or copied the data instead of analysing it'),
                (r'same as|more than once|repetition|repeat',
                 'repeated a point already credited, or restated it in other words'),
                (r'diagram', 'a diagram alone, without the written point'),
                (r'refer to (price|legal|quality)|does not answer the question',
                 'answered a nearby question rather than the one asked'),
            ):
                if re.search(pat, sl):
                    buckets[lab] += 1
                    ex.setdefault(lab, s[:96])
                    break
    for lab, n in buckets.most_common(10):
        print('  %4d  %s\n           e.g. %s' % (n, lab, ex[lab]))

report('0450', 80)
report('0455', 110)
