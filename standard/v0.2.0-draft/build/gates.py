"""Order gates for the planning pipeline.

Step zero is the syllabus (curriculum/syllabus-facts.json).
Step one is the corpus analysis: operations/analysis/<code>-<slug>-corpus-analysis.md, which says
what the skills are and what a learner must do to succeed in each component, from the past papers,
mark schemes and examiner reports. No contract, work order or plan is built before both exist.
"""
import glob
import os


def repo_root(ws):
    return os.path.dirname(os.path.dirname(os.path.abspath(ws.rstrip('/'))))


def code_of(ws):
    return os.path.basename(ws.rstrip('/')).split('-')[1]


def require_prerequisites(ws):
    ws = ws.rstrip('/')
    code = code_of(ws)
    facts = os.path.join(ws, 'curriculum', 'syllabus-facts.json')
    if not os.path.exists(facts):
        raise SystemExit('%s: step zero not done. Run mine_syllabus.py %s first '
                         '(no curriculum/syllabus-facts.json).' % (code, code))
    found = glob.glob(os.path.join(repo_root(ws), 'operations', 'analysis',
                                   '%s-*-corpus-analysis.md' % code))
    if not found:
        raise SystemExit('%s: step one not done. Write operations/analysis/%s-<slug>-corpus-analysis.md '
                         '(past papers, mark schemes, examiner reports: the skills and what success in '
                         'each component takes) before any contract, work order or plan.' % (code, code))
    return found[0]
