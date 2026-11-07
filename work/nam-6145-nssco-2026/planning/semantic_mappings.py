"""Primary objective choices made by reading each question, in extraction order.

Numbers refer to syllabus topic.specific-bullet, not keyword matches. Related
constructs and data-processing skills may occur in the same question.
"""
MAPPINGS = {
    '2020-P1': '''1.1.1 1.2.1 1.2.2 1.3.2 2.1.2 2.2.7 2.2.6 3.2.3 2.3.2 8.2.1 3.4.2 6.2.5 5.2.2 5.2.3 5.3.2 5.4.1 5.4.3 8.2.1 4.2.2 7.3.3 7.4.2 9.1.1 6.2.5 3.2.3 6.2.5 6.2.5 6.1.1 6.1.1 2.1.3 3.2.4 3.3.1 3.3.3 3.3.2 5.3.3''',
    '2020-P2': '''8.2.1 3.2.3 6.3.1 7.3.1 7.1.3 7.2.2 7.2.3 4.3.1 4.3.2 2.3.5 4.3.3 1.2.1 2.1.1 1.1.2 6.1.1 5.1.2 5.1.2 9.1.1 9.1.1 8.1.3 8.1.4 8.1.2 8.1.2''',
    '2021-P1': '''1.1.1 1.1.1 1.3.3 2.1.2 2.1.2 2.1.2 2.3.5 3.1.2 3.3.1 6.2.4 6.2.2 6.2.4 6.2.5 7.4.2 6.3.5 6.3.3 6.3.1 7.4.3 7.4.1 7.4.1 2.3.3 9.1.1 8.1.2 9.1.1 2.1.1 2.1.2 2.3.5 2.3.5 3.3.3 3.3.2 3.5.1 3.5.1''',
    '2021-P2': '''9.1.1 3.2.3 9.1.1 7.2.3 1.2.2 1.2.3 1.2.3 2.2.1 2.2.6 2.2.7 2.2.6 5.1.1 5.2.1 5.2.3 5.3.3 7.3.2 7.3.3 6.2.3 6.2.5 8.1.3 8.2.2 8.2.3 8.2.3''',
    '2022-P1': '''1.1.1 1.2.1 2.1.2 2.1.2 2.2.4 2.3.3 2.3.2 3.1.1 3.2.3 3.2.3 3.3.3 4.2.1 8.2.1 3.2.4 5.2.1 5.2.5 5.3.1 5.3.3 6.2.4 6.2.5 6.1.1 6.3.4 7.3.1 9.1.1 7.1.1 7.1.1 7.1.2 7.1.3 4.1.1 3.2.3 4.1.1 4.2.2''',
    '2022-P2': '''1.3.1 3.2.3 3.1.1 5.1.4 7.2.2 1.1.3 7.2.3 5.4.5 5.4.3 5.1.1 2.2.3 3.2.3 6.3.2 3.2.4 4.2.4 4.3.2 8.1.3 8.1.1 8.1.4''',
    '2023-P1': '''1.1.2 1.2.2 1.2.1 5.1.2 2.1.2 2.3.5 2.3.5 2.3.2 3.2.4 3.2.4 3.3.2 3.5.1 4.2.2 5.3.1 5.4.1 7.1.2 7.1.3 7.4.1 7.4.3 7.2.1 8.1.3 8.2.1 9.1.1 9.1.1 2.1.2 9.1.1 6.3.1 9.1.1 2.1.2 5.1.3 9.1.1 5.4.4''',
    '2023-P2': '''8.2.1 8.2.1 8.2.1 8.2.2 6.2.5 5.2.1 5.2.5 5.2.4 6.2.3 8.2.2 4.3.2 6.2.6 3.4.2 3.2.3 5.4.5 7.2.2 7.4.2 7.2.4 2.3.4 3.3.3 3.2.4 5.3.3 1.3.2''',
    '2024-P1': '''1.1.1 1.2.3 1.3.2 2.1.3 2.2.6 2.3.2 2.3.5 3.2.1 3.2.3 3.3.2 4.1.1 5.3.2 5.4.1 5.4.5 6.2.3 6.2.2 2.3.3 8.2.1 8.1.1 8.2.1 9.1.1 9.1.1 2.3.5 6.2.6 6.2.3 7.4.1 7.3.3 3.2.3 7.4.1''',
    '2024-P2': '''3.2.4 3.3.2 3.2.3 6.3.1 6.2.5 2.1.1 8.1.1 6.2.5 7.1.2 7.1.2 7.1.1 7.1.3 1.2.2 6.1.1 1.2.3 6.1.1 7.2.2 7.2.2 7.2.3 6.2.2 7.4.1 7.4.1 4.2.2 8.1.2''',
}

# Explicit flags prevent broad syllabus bullets from looking like exact matches.
MAPPING_NOTES = {
    '2020-P1-10': 'Real income is a supporting living-standard measure, not a separately named specific objective.',
    '2020-P1-12': 'Transfer payments are a supporting fiscal-policy construct within government spending.',
    '2020-P1-23(b)(i)': 'Pure table reading about subsidy allocation; objective allocation reflects its fiscal context, not an independent content test.',
    '2020-P1-23(b)(ii)': 'Percentage-change numeracy in a fiscal context; this is not proof of knowledge of the fiscal mechanism.',
    '2020-P1-24(c)': 'Profit effects over two time horizons span costs/revenue and firm aims. Primary placement is a judgement; retain both horizons.',
    '2020-P2-3(a)': 'Disposable income supports the spending/saving/borrowing objective; not a separately stated bullet.',
    '2020-P2-5(a)': 'Production sectors are supporting classification content, not a separately stated specific objective.',
    '2020-P2-5(b)': 'Value added is supporting production content, not a separately stated specific objective.',
    '2021-P1-5': 'Formal/informal activity is supporting business-organisation content; do not infer a new form-of-ownership objective.',
    '2021-P1-8': 'E-commerce is supporting market-type content; it also links to the explicit IT objectives.',
    '2021-P1-21': 'WTO is supporting international-trade/protection context; no standalone institutional objective is stated.',
    '2021-P1-24(b)': 'Listing benefits concern stock-exchange functions and consequences, rather than a token match to companies.',
    '2021-P1-25(b)': 'Price discrimination is observed policy content; airline context does not justify a standalone oligopoly unit.',
    '2021-P1-25(c)': 'Non-price competition is broader than advertising; do not map it to advertising simply because the scenario mentions an advertising campaign.',
    '2022-P1-12': 'Occupational mobility supports determination of earnings; the syllabus has no separately named mobility objective.',
    '2022-P1-13': 'Nominal/real conversion is supporting indicator numeracy. Verify the report arithmetic separately before using any example.',
    '2022-P1-24': 'Third-party relocation cost tests external cost, under the syllabus social/private/external-cost identity.',
    '2022-P1-26(c)': 'Motives for occupational choice/self-employment, not advantages of sole ownership.',
    '2022-P2-1(d)': 'Technology effects on vendors include factor substitution and productivity; primary allocation uses factor substitution.',
    '2022-P2-4(b)': 'Fishing production quota restricts output; this is not an import quota or tariff question.',
    '2023-P1-25(b)': 'General percentage-change numeracy in a social-cost context; allocation is contextual rather than a direct content test.',
    '2023-P1-25(c)': 'Government intervention proposal; appropriate AO is C by stated report label, not A because the response names measures.',
    '2023-P1-25(d)': 'Designing enquiries about economic costs, not merely listing costs. This can require Bloom Create while assessment remains AO C.',
    '2023-P1-26(c)': 'Public/private spending trade-off and evaluation of investment; also related to government policy. Primary allocation is provisional.',
    '2023-P2-1(c)': 'Pure proportion calculation in a living-standard context; not evidence of population-growth theory.',
    '2023-P2-5(c)': 'Exchange-rate effects must be linked to unemployment; primary placement is the consequences of exchange-rate changes.',
    '2024-P2-2(a)': 'Investment is supporting fiscal/production content. Do not teach financial asset purchases as the economic definition.',
    '2024-P2-6(b)': 'Tourism is an export service; assess reasons for increased foreign demand rather than infer a general tourism topic.',
}
