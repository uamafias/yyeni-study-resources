# -*- coding: utf-8 -*-
"""Turn examiner-report error statements into two rankable findings:

  A. CRAFT FAILURES  - how candidates lose marks regardless of topic.
     Ranked by SERIES SPREAD: a fault named in 12 of 17 reports is systemic;
     one named once is noise.
  B. CONCEPT CONFUSIONS - the specific pairs of ideas candidates mix up.
     These attach to syllabus objectives and become MISCON cards.
"""
import json, os, re, collections

ROOT = os.path.expanduser('~/mine')

CRAFT = [
 ('no-application',
  r'\bgeneric\b|not applied to|no application|lacked application|without (?:any )?application|'
  r'failed to apply|did not apply|not relate[d]? to the (?:case|business|context)|'
  r'application marks? (?:were )?(?:not|rarely)'),
 ('listed-not-explained',
  r'\b(?:merely|simply|only|just)\s+(?:listed|stated|identified|named)|list(?:ed)?\s+(?:of\s+)?'
  r'(?:points|factors|reasons|advantages)|list-?like|list of (?:points|factors)|'
  r'no (?:attempt at )?(?:explanation|development)|lacked? (?:any )?(?:explanation|development)|'
  r'not developed|undeveloped|without development'),
 ('description-not-analysis',
  r'descriptive|description (?:of|rather)|merely describ|simply describ|'
  r'(?:quoted|repeated|copied|lifted)\s+(?:the\s+)?(?:figures|data|text|from the)|'
  r'no analysis|lacked? analysis|rather than analys|instead of analys'),
 ('one-sided-no-evaluation',
  r'one-?sided|only one side|both sides|no (?:evaluation|judgement|judgment)|'
  r'lacked? (?:evaluation|judgement|judgment)|without (?:a )?(?:judgement|judgment|conclusion)|'
  r'no (?:supported )?conclusion|unsupported (?:judgement|judgment|conclusion)'),
 ('no-justified-recommendation',
  r'justif\w+ (?:was|were) (?:weak|absent|missing|limited)|not justif|without justif|'
  r'lacked? justif|did not (?:justify|explain why)|no reason for (?:the |their )?(?:choice|recommendation)|'
  r'why the (?:other|alternative|rejected)'),
 ('command-word-misread',
  r'approached this as a|answered? (?:a|as if) (?:a )?‘?\w+’? question|'
  r'did not (?:answer|address) the question (?:set|asked)|misread the question|'
  r'misinterpret|did not understand (?:the|what the) (?:command|question|term)|'
  r'rather than (?:an? )?‘\w+’|ignored the command'),
 ('vague-imprecise',
  r'\bvague\b|too general|imprecise|not specific|lacked precision|loosely|'
  r'insufficiently precise|ambiguous'),
 ('definition-weak',
  r'definition (?:was|were)? ?(?:weak|poor|vague|partial|incomplete)|'
  r'partial definition|could not define|unable to define|defined .{0,25}(?:incorrectly|wrongly)|'
  r'gave an example (?:rather|instead)'),
 ('wrong-stakeholder-or-perspective',
  r'from the (?:point of view|perspective) of the (?:wrong|employee|worker|customer)|'
  r'benefit(?:s|ed)? (?:to|for) (?:the )?(?:workers|employees|customers) rather than|'
  r'rather than (?:to )?the (?:business|firm|government|worker|consumer|producer)|'
  r'wrong stakeholder|answered for the'),
 ('repetition',
  r'repeat(?:ed|ing)? the|repetition|same point (?:twice|again)|'
  r'restat(?:ed|ing) the (?:question|point|knowledge)|mirror'),
 ('calculation-error',
  r'calculat\w+ (?:was|were)? ?(?:incorrect|wrong|poor)|wrong formula|incorrect formula|'
  r'arithmetic|did not show (?:their )?working|no working|unable to calculate|'
  r'used the wrong (?:figures|numbers|data)'),
 ('diagram-error',
  r'diagram|axes|curve (?:was|were) (?:not|incorrectly)|label(?:led|ling)? (?:the )?(?:axes|curves)|'
  r'shift(?:ed)? (?:the )?(?:wrong|curve in the wrong)'),
 ('lifted-from-source',
  r'lift(?:ed|ing) (?:directly )?from|copied (?:directly )?from|straight from the (?:case|extract|source)|'
  r'reproduc(?:ed|ing) the (?:text|wording|stem)'),
 ('confused-concepts',
  r'confus(?:ed|ion|ing)|mix(?:ed)? up|muddl|interchange|thought that|believed that|'
  r'mistook|assumed that'),
 ('knowledge-gap',
  r'(?:few|little|limited|poor|weak|no) (?:knowledge|understanding) of|'
  r'did not (?:know|understand|recognise|recognize)|unfamiliar with|'
  r'were unaware|unable to (?:identify|recall|name)'),
 ('irrelevant-content',
  r'irrelevant|off (?:the )?point|not (?:relevant|creditworthy|credit-worthy)|'
  r'wrote about .{0,40} rather than|drifted'),
]
CRAFT = [(n, re.compile(p, re.I)) for n, p in CRAFT]

CONFUSE = [
 re.compile(r'confus(?:ed|ing|ion between|ion of)\s+([a-z][\w \-’\']{2,40}?)\s+(?:with|and|for)\s+([a-z][\w \-’\']{2,40}?)(?:[.,;]|$)', re.I),
 re.compile(r'\b([a-z][\w \-’\']{2,40}?)\s+(?:was|were|is|are)\s+(?:often\s+)?confused with\s+([a-z][\w \-’\']{2,40}?)(?:[.,;]|$)', re.I),
 re.compile(r'mix(?:ed)? up\s+([a-z][\w \-’\']{2,40}?)\s+(?:with|and)\s+([a-z][\w \-’\']{2,40}?)(?:[.,;]|$)', re.I),
 re.compile(r'wrote about\s+([a-z][\w \-’\']{3,50}?)\s+rather than\s+([a-z][\w \-’\']{3,50}?)(?:[.,;]|$)', re.I),
 re.compile(r'gave\s+([a-z][\w \-’\']{3,45}?)\s+(?:rather|instead of)\s+(?:than\s+)?([a-z][\w \-’\']{3,45}?)(?:[.,;]|$)', re.I),
]

def run(code):
    rows = json.load(open(os.path.join(ROOT, '%s_examiner_errors.json' % code)))
    series = sorted({r['series'] for r in rows})
    print('\n' + '=' * 90)
    print('%s   %d error statements across %d series (%s)'
          % (code, len(rows), len(series), ' '.join(series)))

    hits = collections.defaultdict(list)
    for r in rows:
        s = r['statement']
        for name, rx in CRAFT:
            if rx.search(s):
                hits[name].append(r)

    print('\n--- CRAFT FAILURES ranked by how many series name them ------------------')
    print('%-34s %6s %8s  %s' % ('failure mode', 'stmts', 'series', 'share of all statements'))
    ranked = sorted(hits.items(),
                    key=lambda kv: (-len({r['series'] for r in kv[1]}), -len(kv[1])))
    for name, rs in ranked:
        sp = len({r['series'] for r in rs})
        bar = '#' * int(round(24.0 * len(rs) / len(rows)))
        print('%-34s %6d %5d/%-2d  %-25s %.0f%%'
              % (name, len(rs), sp, len(series), bar, 100.0 * len(rs) / len(rows)))

    print('\n--- exemplar statements for the top five --------------------------------')
    for name, rs in ranked[:5]:
        print('\n  [%s]  %d statements, %d/%d series'
              % (name, len(rs), len({r['series'] for r in rs}), len(series)))
        seen = set()
        for r in rs:
            k = r['statement'][:45]
            if k in seen:
                continue
            seen.add(k)
            print('    %s: %s' % (r['series'], r['statement'][:150]))
            if len(seen) >= 3:
                break

    print('\n--- CONCEPT CONFUSIONS (candidate pairs) --------------------------------')
    pairs = collections.Counter()
    where = {}
    for r in rows:
        for rx in CONFUSE:
            m = rx.search(r['statement'])
            if m:
                a = re.sub(r'\s+', ' ', m.group(1)).strip().lower()
                b = re.sub(r'\s+', ' ', m.group(2)).strip().lower()
                if 3 < len(a) < 45 and 3 < len(b) < 45 and a != b:
                    key = '%s  <>  %s' % (a, b)
                    pairs[key] += 1
                    where.setdefault(key, set()).add(r['series'])
                break
    print('found %d distinct pairs; showing those named in 2+ series or 2+ times'
          % len(pairs))
    shown = 0
    for k, n in pairs.most_common(400):
        if n >= 2 or len(where[k]) >= 2:
            print('  %2d x  %-2d series  %s' % (n, len(where[k]), k[:96]))
            shown += 1
            if shown >= 28:
                break
    json.dump({'craft': {k: {'n': len(v),
                             'series': sorted({r['series'] for r in v}),
                             'examples': [x['statement'] for x in v[:12]]}
                         for k, v in hits.items()},
               'confusions': {k: {'n': n, 'series': sorted(where[k])}
                              for k, n in pairs.items()}},
              open(os.path.join(ROOT, 'out', '%s_error_clusters.json' % code), 'w'),
              indent=1)

for c in ('0450', '0455'):
    run(c)
