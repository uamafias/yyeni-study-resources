"""VIS-6137-2.1-01 -> ITEM-6137-2.1-038-INTERP: input-process-output diagram of a fish-processing plant.

Original, invented plant (no real company). A dashed system boundary encloses the plant's processes:
receive and check -> clean and gut -> fillet -> freeze -> grade and pack -> cold store. Inputs cross
the boundary from the left (delivered fish 10 t/day, water, electricity, labour, packaging); outputs
leave on the right: 4 t/day frozen fillet packs to buyers, 5 t/day heads, frames and skins to a
fishmeal plant, 1 t/day trimmings and liquid to wastewater treatment. Mass balance: 10 = 4 + 5 + 1.
Catching at sea is upstream of the boundary (notes BL-6137-2.1.07-01).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-2.1-01'
ITEM = 'ITEM-6137-2.1-038-INTERP'
W, HQ, HA = 1000, 860, 1215
FISH_IN = 10
OUTS = [('frozen fillet|packs', 4, 'to buyers (by refrigerated truck)'), ('heads, frames|and skins', 5, 'to fishmeal plant'),
        ('trimmings|and liquid', 1, 'to wastewater treatment')]
STEPS = ['receive and check', 'clean and gut', 'fillet', 'freeze', 'grade and pack', 'cold store']


def box(fig, x, y, w, h, lines, fill='#ffffff', bold=False, layer='base'):
    fig.rect(x, y, w, h, fill, INK, 2, 8, layer)
    fig.lines(x + w / 2, y + h / 2 - (len(lines) - 1) * 15 + 9, lines, 26, 30, anchor='middle', weight='bold' if bold else 'normal', layer=layer)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'A fish-processing plant (invented example; quantities per day)')
    # inputs
    ins = [['fish delivered', 'by vessels', '10 t'], ['fresh water'], ['electricity'], ['workers'], ['packaging']]
    ys = [80, 250, 360, 470, 580]
    hs = [140, 80, 80, 80, 80]
    for (lines, y, h) in zip(ins, ys, hs):
        box(fig, 30, y, 200, h, lines, '#eaf2fa', bold=(y == 80))
        fig.arrow(232, y + h / 2, 300, y + h / 2, INK, 4, 16, halo=False)
    # boundary and processes
    fig.rect(300, 70, 380, 640, '#f8f8f4', INK, 3, 10, extra='stroke-dasharray="16 10"')
    fig.text(490, 104, 'PLANT BOUNDARY', 26, 'middle', 'bold', GREY)
    for k, s in enumerate(STEPS):
        y = 124 + k * 96
        box(fig, 340, y, 300, 64, [s], '#ffffff')
        if k < len(STEPS) - 1:
            fig.arrow(490, y + 64, 490, y + 96, INK, 4, 14, halo=False)
    # outputs
    targets = [(124 + 5 * 96 + 32, 600), (124 + 2 * 96 + 32, 330), (124 + 1 * 96 + 32, 170)]
    for (name, t, dest), (src_y, by) in zip(OUTS, targets):
        fig.path('M640 %d C 680 %d, 690 %d, 720 %d' % (src_y, src_y, by + 50, by + 50), 'none', INK, 4)
        fig.arrow(706, by + 50, 726, by + 50, INK, 4, 16, halo=False)
        box(fig, 728, by - 10, 246, 120, name.split('|') + ['%d t' % t], '#fbf1e4', bold=True)
        fig.lines(851, by + 142, [dest.split(' (')[0]] + (['(' + dest.split(' (')[1]] if ' (' in dest else []), 26, 30, anchor='middle')
    fig.text(165, 742, 'catching at sea happens', 26, 'middle', 'normal', GREY)
    fig.text(165, 774, 'before the boundary', 26, 'middle', 'normal', GREY)
    fig.text(W / 2, HQ - 26, 'Arrows show flows into, through and out of the plant.', 26, 'middle', 'normal', GREY)

    A = 'a'
    fig.rect(24, 74, 212, 600, 'none', C['answer'], 4, 10, A)
    fig.text(130, 66, 'INPUTS', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.text(490, 66, 'PROCESSES', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.text(851, 66, 'OUTPUTS', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.marker(30, 60, '1', A)
    fig.marker(380, 60, '2', A)
    fig.marker(940, 140, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Inputs cross the boundary: 10 t of delivered fish, with water, electricity, workers and packaging.'),
                 ('2', 'Processes inside the plant transform and handle the fish: cleaning, filleting, freezing, then grading, packing and cold storage.'),
                 ('3', 'Outputs leave to different destinations: 4 t of saleable packs to buyers, 5 t of by-products to fishmeal and 1 t to wastewater treatment (4 + 5 + 1 = 10 t).')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {
        'kind': 'input-process-output flow diagram with system boundary (invented plant)',
        'inputs': ['fish delivered by vessels 10 t/day', 'fresh water', 'electricity', 'workers', 'packaging'],
        'processes': STEPS, 'outputs': [{'flow': n.replace('|', ' '), 't_per_day': t, 'destination': d} for n, t, d in OUTS],
        'mass_balance_t_per_day': {'in': FISH_IN, 'out': sum(t for n, t, d in OUTS)},
        'question_withholds': ['the words input/process/output as category labels'],
        'independent_solution': ['inputs: fish plus water, energy, labour, packaging (1)', 'processes transform/handle: clean, fillet, freeze, pack, store (1)',
                                 'outputs to destinations: 4 t packs to buyers, 5 t by-products to fishmeal, 1 t to wastewater (1)'],
    }
    checks = [
        check('mass balance: fish in equals outputs', FISH_IN == sum(t for n, t, d in OUTS), '10 = 4 + 5 + 1'),
        check('processes in a single ordered chain inside the boundary', len(STEPS) == 6),
        check('catching shown as upstream of the boundary', True),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'\bINPUTS\b', r'\bPROCESSES\b', r'\bOUTPUTS\b']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
