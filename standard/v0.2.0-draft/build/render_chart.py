#!/usr/bin/env python3
"""Render a break-even chart from its declared parameters.

RS-47. A learner-visible depiction of declared data is GENERATED from that data, never
authored beside it. Review SR-9609-5.4-CODEX-R4 found a hand-drawn ASCII chart whose lines
did not cross at all, in four items whose declared parameters and stated arithmetic were
both correct - C-35 verified the metadata against the metadata and never looked at the
picture. This module is the single source of the picture; C-41 re-renders and compares.

    render_break_even({'price': 80, 'variable_cost': 40, 'fixed_costs': 160000,
                       'current_output': 6000})
"""
import sys

CAPTION = ('*Key: `*` is total revenue (TR), `+` is total cost (TC), `-` is fixed costs (FC), and `X` marks '
           'where TR and TC meet. All three lines are straight. TR passes through the origin; TC starts on the '
           'vertical axis at the level of the fixed cost line. Read values off the gridlines.*')

HEADER = 'N$000        TR = total revenue      TC = total cost      FC = fixed costs'

ROWS = 12           # value gridlines above the axis
COLS = 6            # output gridlines to the right of the origin
COL_W = 9           # characters between output gridlines
LABEL_W = 6         # width of the value-label gutter, e.g. '  480 '


NICE = (1, 1.5, 2, 2.5, 3, 4, 5, 6, 8)


def _nice_step(v):
    """Smallest round step whose ROWS gridlines reach v, so labels land on values a learner can read."""
    need = v / ROWS
    k = 10 ** (len(str(int(need))) - 2) if need >= 10 else 1
    while True:
        for n in NICE:
            if n * k >= need:
                return n * k
        k *= 10


def render_break_even(chart):
    """Return (plot_text, facts). plot_text is the fenced block a learner reads."""
    price = float(chart['price'])
    var = float(chart['variable_cost'])
    fc = float(chart['fixed_costs'])
    q_max = float(chart['current_output'])
    if price <= var:
        raise ValueError('revenue never overtakes total cost: price %s, variable cost %s' % (price, var))

    be_q = fc / (price - var)
    be_v = price * be_q
    v_step = _nice_step(price * q_max)
    top = v_step * ROWS
    q_step = q_max / COLS

    width = COLS * COL_W + 1
    grid = [[' '] * width for _ in range(ROWS + 1)]      # row 0 = top (value `top`), row ROWS = 0

    def row_of(value):
        return int(round(ROWS - value / v_step))

    def col_of(q):
        return int(round(q / q_max * (width - 1)))

    def plot(fn, mark):
        for c in range(width):
            q = c / (width - 1) * q_max
            r = row_of(fn(q))
            if 0 <= r <= ROWS:
                grid[r][c] = mark

    plot(lambda q: fc, '-')                              # fixed costs, horizontal
    plot(lambda q: fc + var * q, '+')                    # total cost
    plot(lambda q: price * q, '*')                       # total revenue
    # the intersection belongs to both lines; mark it so it cannot be missed
    r, c = row_of(be_v), col_of(be_q)
    if 0 <= r <= ROWS:
        grid[r][c] = 'X'

    lines = [HEADER]
    for r in range(ROWS + 1):
        value = (ROWS - r) * v_step
        label = ('%d' % round(value / 1000)) if (r % 2 == 0) else ''
        body = ''.join(grid[r]).rstrip()
        lines.append('%s |%s' % (label.rjust(LABEL_W - 1), body))
    # The axis and its ticks are placed from the same col_of() the lines were plotted with, so a
    # gridline always sits under the column it labels. Value rows read '<label> |<body>', which puts
    # the axis at index LABEL_W and plot column c at LABEL_W + 1 + c.
    def tick_at(i):
        return LABEL_W if i == 0 else LABEL_W + 1 + col_of(i * q_step)

    axis = [' '] * (LABEL_W + 1 + width)
    axis[LABEL_W] = '+'
    for c in range(width):
        axis[LABEL_W + 1 + c] = '-'
    for i in range(1, COLS + 1):
        axis[tick_at(i)] = '+'
    lines.append(''.join(axis) + '>')

    ticks = [' '] * (LABEL_W + 3 + width)
    for i in range(COLS + 1):
        t = '%d' % round(i * q_step)
        if len(t) > 3:
            t = t[:-3] + ' ' + t[-3:]
        at = max(0, tick_at(i) - len(t) // 2)
        for k, ch in enumerate(t):
            ticks[at + k] = ch
    lines.append(''.join(ticks).rstrip() + '  units')

    plot_text = ('```\n' + '\n'.join(lines) + '\n```\n\n' + CAPTION)
    facts = {'break_even_output': be_q, 'break_even_value': be_v,
             'revenue_at_max': price * q_max, 'cost_at_max': fc + var * q_max,
             'profit_at_max': (price - var) * q_max - fc,
             'margin_of_safety': q_max - be_q,
             'fc_revenue_crossing': fc / price}
    return plot_text, facts


if __name__ == '__main__':
    t, f = render_break_even({'price': 80, 'variable_cost': 40, 'fixed_costs': 160000,
                              'current_output': 6000})
    print(t)
    print()
    for k, v in f.items():
        print('%-22s %s' % (k, v))
