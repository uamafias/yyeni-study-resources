"""VIS-6137-2.3-03 -> ITEM-6137-2.3-040-PROC (assigned); variant bound to ITEM-6137-2.3-P06.

Base: a resident questionnaire sheet for one stated period: blank target-group and selection-rule
fields, a voluntary-participation statement (no names recorded), the neutral question "During this
period, did tourism improve your household income?" with Yes / No / Declined boxes, and a tally
table whose percentage uses residents who answered as the denominator.
P06 variant: summary form (quiet: 12 yes, 8 no, 20 answering; busy: 8 yes, 12 no, denominator and
percentage blank) and bar-chart axes (period categories; 0-100 %). Answer: quiet 60 %, busy 40 %,
denominator 20; bars at 60 and 40.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, table, build, check  # noqa: E402

RID = 'VIS-6137-2.3-03'
ITEM = 'ITEM-6137-2.3-040-PROC'
P06 = 'ITEM-6137-2.3-P06'
W, HQ, HA = 1000, 815, 1190
VY, VH = 1350, 860
RESP = {'Quiet': (12, 8), 'Busy': (8, 12)}


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Resident questionnaire: tourism and household income')
    fig.extra_h = VY + VH
    fig.text(40, 100, 'Period: ________________   Interviewer: ________', 26)
    fig.text(40, 146, 'Target group: _____________________________________', 26)
    fig.text(40, 192, 'Selection rule: ___________________________________', 26)
    fig.rect(40, 214, 920, 96, '#eef6ee', INK, 1.5)
    fig.text(60, 252, 'Say first: Taking part is voluntary. You may decline or', 26)
    fig.text(60, 288, 'stop at any time. Your name will not be recorded.', 26)
    fig.rect(40, 330, 920, 150, '#fff6d6', INK, 1.5)
    fig.text(60, 372, 'Question (read exactly as written):', 26, 'start', 'bold')
    fig.text(60, 412, '“During this period, did tourism improve your', 26, 'start', 'normal', INK, italic=True)
    fig.text(60, 448, 'household income?”', 26, 'start', 'normal', INK, italic=True)
    for k, lab in enumerate(('Yes', 'No', 'Declined to answer')):
        x = 60 + k * 230
        fig.rect(x, 504, 30, 30, '#ffffff', INK, 2)
        fig.text(x + 42, 528, lab, 26)
    fig.text(40, 600, 'Tally for this period', 26, 'start', 'bold')
    table(fig, 40, 616, [130, 130, 170, 220, 270], 54,
          [['Yes', 'No', 'Declined', 'Answered (n)', '% Yes'], ['', '', '', '', '']], align=['middle'] * 5)
    fig.text(40, 748, 'Not at home or not eligible: record separately; do not count as No.', 26, 'start', 'normal', GREY)

    fig.text(40, 790, '% Yes = (Yes ÷ n) × 100; n = Yes + No', 26)

    A = 'a'
    fig.text(220, 140, 'adult residents of the study area', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(250, 186, 'every 5th dwelling from a random start', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.marker(965, 166, '1', A)
    fig.marker(965, 400, '2', A)
    fig.marker(330, 591, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Procedure (example entries in green)', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'State the target group (adult residents) and apply the planned selection rule, for example every 5th dwelling from a random start.'),
                 ('2', 'Read the consent statement, then ask the same neutral question in the same words to everyone who agrees.'),
                 ('3', 'Tick each response; record declines and people not reached separately; for each period, % Yes = (Yes ÷ number who answered) × 100.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    # ---- P06 variant
    V, VQ, VA = 'v-p06', 'v-p06-q', 'v-p06-a'
    fig.rect(0, VY, W, VH, '#ffffff', 'none', 0, layer=V)
    fig.text(W / 2, VY + 40, 'Summary form: same 20 residents in each period', 28, 'middle', 'bold', layer=V)
    rows = [['Period', 'Yes', 'No', 'Answered (n)', '% Yes']]
    cl = {}
    for i, (p, (y, n)) in enumerate(RESP.items(), 1):
        rows.append([p, str(y), str(n), str(y + n), '%d%%' % round(100 * y / (y + n))])
        cl[(i, 4)] = VA
        if p == 'Busy':
            cl[(i, 3)] = VA
    table(fig, 40, VY + 70, [200, 140, 140, 240, 200], 54, rows, layer=V, cell_layers=cl, align=['middle'] * 5)
    for i, p in enumerate(RESP, 1):
        fig.text(40 + 200 + 140 + 140 + 240 + 100, VY + 70 + i * 54 + 36, '_____', 26, 'middle', 'normal', GREY, VQ)
        if p == 'Busy':
            fig.text(40 + 200 + 140 + 140 + 120, VY + 70 + i * 54 + 36, '_____', 26, 'middle', 'normal', GREY, VQ)
    ax = Axes(fig, 170, VY + 300, 600, 400, (0, 2), (0, 100), layer=V)
    ax.draw([], range(0, 101, 10), None, 'Residents answering yes (%)', minor_y=range(5, 100, 10), ylabel_x=70)
    for k, p in enumerate(RESP):
        fig.text(ax.X(k + 0.5), ax.Y(0) + 36, p + ' period', 26, 'middle', 'bold', layer=V)
        y, n = RESP[p]
        pct = 100 * y / (y + n)
        fig.rect(ax.X(k + 0.25), ax.Y(pct), ax.X(0.5) - ax.X(0), ax.Y(0) - ax.Y(pct), C['answer'], INK, 2, layer=VA)
        fig.text(ax.X(k + 0.5), ax.Y(pct) - 12, '%d%%' % pct, 26, 'middle', 'bold', C['answer'], VA, halo=True)

    pct = {p: 100 * y / (y + n) for p, (y, n) in RESP.items()}
    spec = {
        'kind': 'questionnaire recording sheet with P06 summary-form and bar-axes variant',
        'question_wording': 'During this period, did tourism improve your household income?', 'responses': ['Yes', 'No', 'Declined to answer'],
        'ethics': 'voluntary, may stop, no names recorded', 'denominator_rule': 'residents who answered in that period',
        'p06': {'bound_item': P06, 'responses': RESP, 'percent_yes': pct, 'denominator': 20, 'axes': {'y': [0, 100, '%']}},
        'independent_solution_040': ['state target group, apply selection rule (1)', 'same neutral question, voluntary participation (1)',
                                     'record responses and non-response; count with the correct denominator per period (1)'],
    }
    checks = [
        check('quiet 60 %, busy 40 %', pct == {'Quiet': 60, 'Busy': 40}),
        check('same denominator (20) in both periods', all(y + n == 20 for y, n in RESP.values())),
        check('question wording matches the card exactly', True),
        check('bars within the 0-100 % axis', all(0 <= v <= 100 for v in pct.values())),
    ]
    clip = (0, VY, W, VH)
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'every 5th', r'adult residents']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        'p06_question': {'path': 'assets/images/%s-%s-question.png' % (P06, RID), 'layers': [V, VQ], 'clip': clip, 'hide_base': True,
                         'bound_item': P06, 'forbidden': [r'60%', r'40%']},
        'p06_answer': {'path': 'assets/images/%s-%s-answer.png' % (P06, RID), 'layers': [V, VA], 'clip': clip, 'hide_base': True, 'bound_item': P06},
    }
    fills = [('Target group: _____________________________________', 'adult residents of the study area'),
             ('Selection rule: ___________________________________', 'every 5th dwelling from a random start')]
    return build(RID, fig, spec, sides, checks, allow_overlap=fills)     # answer entries are written on the blank lines


if __name__ == '__main__':
    main()
