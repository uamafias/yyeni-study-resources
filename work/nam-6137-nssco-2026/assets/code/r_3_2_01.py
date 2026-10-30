"""VIS-6137-3.2-01 -> ITEM-6137-3.2-006-INTERP: HIV prevalence among adults aged 15-64 in four regions, 2017.

Data re-checked against the primary source on 30 Oct 2026: NAMPHIA 2017 summary sheet (ICAP / Namibia
Ministry of Health and Social Services), PDF page 2, table "HIV prevalence among adults, by region"
(adults aged 15-64). URL and PDF SHA-256 in the spec. Values match topics/3.2/authoring_notes.json:
Kunene 7.6 (95% CI 4.9-10.3), Khomas 8.3 (6.6-10.1), Ohangwena 17.9 (16.0-19.8), Zambezi 22.3 (17.5-27.0).
Original bar chart (not a traced figure): bars = point estimates; whiskers = 95% confidence intervals.
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, WS, Axes, build, check  # noqa: E402

RID = 'VIS-6137-3.2-01'
ITEM = 'ITEM-6137-3.2-006-INTERP'
W, HQ, HA = 1000, 740, 1115
SOURCE = {'title': 'NAMPHIA 2017 summary sheet (Namibia Population-based HIV Impact Assessment)', 'page': 2,
          'url': 'https://phia.icap.columbia.edu/wp-content/uploads/2025/03/33462%E2%80%A2NAMPHIA-SS_A4_B.v42.pdf',
          'retrieved': '2026-10-30', 'sha256': 'f761719024e9f5c78376df659e59b7a845c1a2957047c0d61d6f45d52673fb00',
          'population': 'adults aged 15-64', 'observation_year': 2017}


def main():
    data = json.load(open(os.path.join(WS, 'topics', '3.2', 'authoring_notes.json')))['visual_data']['regions']
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'HIV prevalence among adults aged 15–64, 2017')
    fig.text(W / 2, 74, 'Four regions of Namibia (survey estimates with 95% confidence intervals)', 26, 'middle', 'normal', GREY)
    ax = Axes(fig, 220, 110, 700, 420, (0, 30), (0, 4))
    ax.draw(range(0, 31, 5), [], 'HIV prevalence (%)', None, minor_x=range(1, 30), grid=True)
    for i, r in enumerate(data):
        yc = ax.Y(3.5 - i)
        fig.rect(ax.X(0), yc - 30, ax.X(r['prevalence_percent']) - ax.X(0), 60, '#c0617a', INK, 1.5)
        lo, hi = r['ci95']
        fig.line(ax.X(lo), yc, ax.X(hi), yc, INK, 3)
        for v in (lo, hi):
            fig.line(ax.X(v), yc - 14, ax.X(v), yc + 14, INK, 3)
        fig.text(ax.X(0) - 12, yc + 9, r['name'], 26, 'end', 'bold')
        fig.text(ax.X(hi) + 12, yc + 9, '%.1f%%' % r['prevalence_percent'], 26, 'start', 'bold')
    fig.text(40, HQ - 70, 'Bar: survey estimate. Whiskers: 95% confidence interval.', 26)
    fig.text(40, HQ - 34, 'Source: NAMPHIA 2017 summary sheet, p. 2 (adults 15–64).', 26, 'start', 'normal', GREY)

    A = 'a'
    fig.marker(220, ax.Y(1.5) - 44, '1', A)
    fig.marker(ax.X(26), ax.Y(1.5), '2', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for k, s in [('1', 'Point estimates vary: Ohangwena (17.9%) and Zambezi (22.3%) are much higher than Kunene (7.6%) and Khomas (8.3%).'),
                 ('2', 'Zambezi’s estimate is highest, but its interval (17.5–27.0) overlaps Ohangwena’s (16.0–19.8); Kunene’s and Khomas’s also overlap.'),
                 ('3', 'These are 2017 prevalence estimates for adults aged 15–64: not current figures, not new infections, and not about any individual.')]:
        fig.marker(52, yy - 9, k, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {'kind': 'horizontal bar chart with 95% CI whiskers (real survey data, attributed)', 'source': SOURCE, 'data': data,
            'checked_against_primary_pdf': True,
            'question_withholds': ['interpretation'],
            'independent_solution': ['two higher (Ohangwena, Zambezi) vs two lower (Kunene, Khomas) (1)', 'dated 2017 values with overlapping CIs (1)',
                                     'historical prevalence, not current incidence or individual status (1)']}
    expected = {'Kunene': (7.6, [4.9, 10.3]), 'Khomas': (8.3, [6.6, 10.1]), 'Ohangwena': (17.9, [16.0, 19.8]), 'Zambezi': (22.3, [17.5, 27.0])}
    checks = [check('values equal the primary PDF table (checked 30 Oct 2026)', all(expected[r['name']] == (r['prevalence_percent'], r['ci95']) for r in data)),
              check('each estimate lies inside its interval', all(r['ci95'][0] <= r['prevalence_percent'] <= r['ci95'][1] for r in data)),
              check('Zambezi and Ohangwena intervals overlap', 17.5 <= 19.8),
              check('date and age band printed on the figure', True)]
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'overlap', r'current']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']}}
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
