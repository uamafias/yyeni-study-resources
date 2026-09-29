#!/usr/bin/env python3
"""Turn the last check run into a short, ordered list of what to fix next.

    python3 what_to_fix.py <workspace> <topic> [--max 6]

`run_checks.py` prints 43 lines, most of them passes. An author - especially a smaller model
looping on its own output - needs the opposite: only what failed, in the order worth fixing,
with the affected ids and the one action that clears it. This reads the qa report and prints
that. Exit code 0 when there is nothing left to fix, 1 while failures remain, so it drives a
loop directly:

    until python3 checks/what_to_fix.py <ws> <topic>; do   # fix what it prints, then
      python3 checks/run_checks.py <ws> <topic> >/dev/null # re-run and look again
    done
"""
import argparse
import json
import os
import sys

# What actually clears each check, in the author's terms rather than the rule's.
ACTION = {
    'C-00': 'Fix the schema violation named above - usually a field the schema does not allow, or a required one missing.',
    'C-01': 'Every objective_ids entry must exist in curriculum/objective_registry.json.',
    'C-02': 'Every claim_ids entry must exist in the topic claim ledger.',
    'C-03': 'Cite the orphan claim from a block or an item, or delete it.',
    'C-04': 'Remove the objective from the item, or cite a claim that genuinely serves it. Listing an objective an item does not practise is manufactured coverage.',
    'C-05': 'Write an item that practises the uncovered objective.',
    'C-06': 'Write a content block that teaches the uncovered objective.',
    'C-07': 'Teach the claim in a content block, or stop citing it from the item. A card may not be the only place a learner meets an idea.',
    'C-08': 'Rewrite the absolute as a tendency, or - if it is genuinely definitional, legal or arithmetic - set generality on the claim.',
    'C-09': 'Rewrite what the third party will do as a likelihood with a reason.',
    'C-10': 'Delete the claim about examiners, marks or paper content. It cannot be evidenced.',
    'C-11': 'Remove the excluded construct from learner-facing text.',
    'C-12': 'Name the term\'s consequential variants where the term is taught, and condition each benefit and limitation on the variant.',
    'C-13': 'Declare generalisation_scope on the block, or narrow the statement to the members it holds for.',
    'C-14': 'Replace the command word with one this level uses.',
    'C-15': 'Give the objective an item whose prompt instructs with one of its own command words.',
    'C-16': 'Name every declared part of the subtype answer structure in the marking guidance. The parts are in the work order for that slot.',
    'C-17': 'Fix the assessment_objectives to ones the subtype permits.',
    'C-18': 'Shift the AO mix toward the target - usually more application and analysis, not more definitions.',
    'C-19': 'Give the flashcard a canonical answer and a declared subtype.',
    'C-20': 'Split the card: one target per flashcard.',
    'C-21': 'Rewrite or merge the duplicate prompt.',
    'C-22': 'Add marking guidance.',
    'C-23': 'Cite at least one claim from the item.',
    'C-24': 'A publishable claim needs verification recorded.',
    'C-25': 'Set a recognised qa_status.',
    'C-26': 'Bring the content unit inside its word budget, or recompute the budget in the contract if the plan changed.',
    'C-27': 'Write the missing subtype, or waive it in the contract subtype_waivers with a reason of at least twelve words.',
    'C-28': 'Regenerate the packet manifest.',
    'C-29': 'The claim was rewritten and this artefact still reflects the old text. Re-read it against the new claim, change what needs changing, then update claims_seen.',
    'C-30': 'Advancing a claims_seen stamp asserts you re-read the artefact. Either change the text or record reviewed_unchanged saying what you checked.',
    'C-31': 'The syllabus wording names a chart or diagram for this objective, so practise it in that form.',
    'C-32': 'The stated arithmetic does not evaluate. Recompute it.',
    'C-33': 'Make the flashcard self-contained - it currently depends on another card.',
    'C-34': 'Interpretation must say what the figure means, not check the arithmetic again.',
    'C-35': 'Declare context.chart on the item and make every stated value recompute from it. Do not state the value you ask the learner to read.',
    'C-36': 'State the figure behind the magnitude claim.',
    'C-43': 'Write the practice text the item cites at topics/<T>/texts/<text_id>.md, with front matter text_id, original: true, words_min and words_max, and a body inside that length.',
    'C-37': 'The artefact asserts a registered conditioned mechanism without its conditions. Carry every condition, in this artefact, not only in the claim.',
    'C-38': 'The answer asserts a completeness fact the prompt does not supply. Put it in the stem, or make the recommendation conditional on checking it.',
    'C-39': 'Exposure figures must recompute from the evidence map. Regenerate, do not edit.',
    'C-40': 'Name the quantity in the units it is measured in - a count is not currency.',
    'C-41': 'Regenerate the chart with build/render_chart.py. Do not hand-correct the characters.',
    'C-42': 'Set the contract counts to what the build actually contains.',
}
# Fix order: structure first, because everything else reads it; then truth; then shape.
PRIORITY = ['C-00', 'C-01', 'C-02', 'C-23', 'C-03', 'C-29', 'C-30', 'C-05', 'C-06', 'C-07',
            'C-04', 'C-32', 'C-41', 'C-35', 'C-38', 'C-37', 'C-08', 'C-09', 'C-10', 'C-40',
            'C-36', 'C-33', 'C-34', 'C-11', 'C-12', 'C-13', 'C-14', 'C-15', 'C-16', 'C-17',
            'C-27', 'C-42', 'C-26', 'C-19', 'C-20', 'C-21', 'C-22', 'C-24', 'C-25', 'C-28',
            'C-39', 'C-18', 'C-31']


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('workspace')
    ap.add_argument('topic')
    ap.add_argument('--max', type=int, default=6)
    a = ap.parse_args()
    qa = os.path.join(a.workspace, 'topics', a.topic, 'qa_report.json')
    if not os.path.exists(qa):
        print('No qa_report yet. Run: python3 standard/v0.2.0-draft/checks/run_checks.py %s %s'
              % (a.workspace, a.topic))
        return 1
    with open(qa) as fh:
        rep = json.load(fh)
    fails = [c for c in rep['deterministic_checks'] if c['status'] == 'fail']
    if not fails:
        warn = [c['check_id'] for c in rep['deterministic_checks'] if c['status'] == 'warn']
        print('Nothing left to fix. Decision: %s.%s'
              % (rep['release_decision'].upper(),
                 ('  (warnings, which do not block: %s)' % ', '.join(warn)) if warn else ''))
        return 0
    fails.sort(key=lambda c: PRIORITY.index(c['check_id']) if c['check_id'] in PRIORITY else 99)
    print('%d checks failing. Fix them in this order; re-run the checks after each.\n'
          % len(fails))
    for i, c in enumerate(fails[:a.max], 1):
        msg = c['message'].split('] ', 1)[-1]
        print('%d. %s' % (i, c['check_id']))
        print('   PROBLEM: %s' % msg[:400])
        if c['affected_ids']:
            ids = c['affected_ids'][:8]
            print('   AFFECTED: %s%s' % (', '.join(ids),
                                         ' (+%d more)' % (len(c['affected_ids']) - len(ids))
                                         if len(c['affected_ids']) > len(ids) else ''))
        print('   DO THIS: %s\n' % ACTION.get(c['check_id'], 'See the message above.'))
    if len(fails) > a.max:
        print('...and %d more once these are cleared.' % (len(fails) - a.max))
    return 1


if __name__ == '__main__':
    sys.exit(main())
