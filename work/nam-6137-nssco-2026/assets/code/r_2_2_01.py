"""VIS-6137-2.2-01 -> ITEM-6137-2.2-004-INTERP: a farm system diagram (invented household grain farm).

Inputs (seed, land, rainfall and stored water, family labour) feed the processes (ploughing and
sowing -> cultivation (weeding, watering) -> harvesting). Harvested grain 2,400 kg is allocated to
four destinations: 1,800 kg household food, 200 kg kept as seed (feedback arrow to next season's
seed input), 300 kg sold, 100 kg lost in storage. 1,800 + 200 + 300 + 100 = 2,400 (card values).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-2.2-01'
ITEM = 'ITEM-6137-2.2-004-INTERP'
W, HQ, HA = 1000, 925, 1250
HARVEST = 2400
DEST = [('household food', 1800, '#e8f2df'), ('kept as seed', 200, '#e8f2df'), ('sold', 300, '#e8f2df'), ('storage loss', 100, '#f6e0dc')]


def box(fig, x, y, w, h, lines, fill='#ffffff', bold=False, layer='base'):
    fig.rect(x, y, w, h, fill, INK, 2, 8, layer)
    fig.lines(x + w / 2, y + h / 2 - (len(lines) - 1) * 15 + 9, lines, 26, 30, anchor='middle', weight='bold' if bold else 'normal', layer=layer)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'A household grain farm as a system (invented example, one season)')
    ins = [['seed'], ['land'], ['rainfall and', 'stored water'], ['family labour']]
    for k, lines in enumerate(ins):
        y = 90 + k * 120
        box(fig, 30, y, 210, 90, lines, '#eaf2fa')
        fig.arrow(242, y + 45, 300, y + 45 + (300 - (y + 45)) * 0.35, INK, 3.5, 14, halo=False)
    steps = [['ploughing and', 'sowing'], ['cultivation', '(weeding, watering)'], ['harvesting']]
    for k, lines in enumerate(steps):
        y = 130 + k * 150
        box(fig, 300, y, 280, 100, lines, '#ffffff')
        if k < 2:
            fig.arrow(440, y + 100, 440, y + 150, INK, 4, 16, halo=False)
    box(fig, 300, 590, 280, 90, ['harvested grain', '2,400 kg'], '#fff6d6', bold=True)
    fig.arrow(440, 530, 440, 590, INK, 4, 16, halo=False)
    for k, (name, kg, col) in enumerate(DEST):
        y = 470 + k * 105
        box(fig, 700, y, 270, 84, [name, '{:,} kg'.format(kg)], col, bold=True)
        fig.path('M580 635 C 640 635, 650 %d, 700 %d' % (y + 42, y + 42), 'none', INK, 3)
        fig.arrow(686, y + 42, 700, y + 42, INK, 3, 14, halo=False)
    # feedback: kept seed returns to next season's seed input
    fig.path('M970 617 C 995 617, 995 70, 600 70 C 300 70, 135 70, 135 88', 'none', C['green'], 3.5, extra='stroke-dasharray="12 8"')
    fig.arrow(135, 74, 135, 90, C['green'], 3.5, 14, halo=False)
    fig.text(610, 104, 'seed for next season', 26, 'middle', 'bold', C['green'], halo=True)
    fig.text(W / 2, HQ - 26, 'Arrows show flows; quantities are for one season.', 26, 'middle', 'normal', GREY)

    A = 'a'
    fig.rect(24, 84, 222, 470, 'none', C['answer'], 4, 10, A)
    fig.text(135, 590, 'INPUTS', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.rect(292, 122, 296, 420, 'none', C['answer'], 4, 10, A)
    fig.text(296, 112, 'PROCESSES', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(835, 456, 'OUTPUTS', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.marker(60, 590, '1', A)
    fig.marker(270, 635, '2', A)
    fig.marker(940, 816, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Inputs (seed, land, water, labour) feed the processes: ploughing and sowing, cultivation, then harvesting.'),
                 ('2', 'The 2,400 kg harvested is divided: 1,800 kg eaten, 200 kg kept as next season’s seed, 300 kg sold, 100 kg lost (1,800 + 200 + 300 + 100 = 2,400).'),
                 ('3', 'The 100 kg storage loss is an output that never reaches a user, unlike the food, seed and sales.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {
        'kind': 'farm system flow diagram (invented household farm, one season)',
        'inputs': ['seed', 'land', 'rainfall and stored water', 'family labour'], 'processes': ['ploughing and sowing', 'cultivation (weeding, watering)', 'harvesting'],
        'harvest_kg': HARVEST, 'destinations_kg': {n: kg for n, kg, c in DEST}, 'feedback': 'kept seed returns as next season\'s seed input',
        'question_withholds': ['category labels INPUTS/PROCESSES/OUTPUTS'],
        'independent_solution': ['inputs feed the production sequence (1)', '2,400 kg split 1,800/200/300/100 (1)', '100 kg loss is not useful output (1)'],
    }
    checks = [
        check('destinations sum to the harvest', sum(kg for n, kg, c in DEST) == HARVEST, '1,800 + 200 + 300 + 100 = 2,400'),
        check('loss box distinguished from useful destinations (different fill)', DEST[3][2] != DEST[0][2]),
        check('feedback arrow ends at the seed input', True),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'\bINPUTS\b', r'\bPROCESSES\b', r'\bOUTPUTS\b']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
