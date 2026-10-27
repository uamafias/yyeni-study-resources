"""Recompute the numerical demands from transcribed case inputs, not guide answers."""
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path

WS=Path(__file__).resolve().parents[1]
OUT=WS/'assessment-evidence'
D=Decimal


def rounded(value):
    return str(value.quantize(D('0.01'),rounding=ROUND_HALF_UP))


def source(name,page):
    doc=json.loads((OUT/'extracted'/f'{name}.json').read_text())
    text=next(p['raw'] for p in doc['pages'] if p['pdf_page']==page)
    return {'source_id':name,'path':doc['path'],'pdf_page':page,'input_page_text_internal_only':text}


checks=[]
def add(name,inputs,results,expected,locator,notes=''):
    actual={k:rounded(v) for k,v in results.items()}
    assert actual==expected,(name,actual,expected)
    checks.append({'check_id':name,'inputs_transcribed_from_case':inputs,'recomputed':actual,
                   'source_locator':locator,'notes':notes,'status':'pass','provenance':'corpus inputs; arithmetic derived'})

add('2020-P2-liquidity',{'current_liabilities':36000,'inventory':38000,'debtors':16000,'cash':8000},
    {'current_ratio':D(62000)/36000,'quick_ratio':D(24000)/36000},
    {'current_ratio':'1.72','quick_ratio':'0.67'},source('QP-2020-P2',3),
    'Results are x:1. The report evaluation says 0.66; do not copy that truncation into a two-decimal worked answer.')
add('2021-P2-profitability',{'2020':{'capital':200,'profit':40,'sales':175},'2021':{'capital':250,'profit':60,'sales':200},'source_unit':'N$000'},
    {'2020_ROCE_percent':D(40)/200*100,'2021_ROCE_percent':D(60)/250*100,
     '2020_NPM_percent':D(40)/175*100,'2021_NPM_percent':D(60)/200*100},
    {'2020_ROCE_percent':'20.00','2021_ROCE_percent':'24.00','2020_NPM_percent':'22.86','2021_NPM_percent':'30.00'},source('QP-2021-P2',3),
    'Case labels capital; using it as the ROCE denominator follows the report. Do not relabel an undefined datum as universally equivalent to capital employed.')
add('2022-P1-cost-plus',{'total_cost':2800,'output':200,'markup_percent':50},
    {'unit_cost':D(2800)/200,'markup_per_unit':D(2800)/200*D('0.5'),'selling_price':D(2800)/200*D('1.5')},
    {'unit_cost':'14.00','markup_per_unit':'7.00','selling_price':'21.00'},source('QP-2022-P1',9))
add('2022-P1-profitability',{'sales':300000,'cost_of_sales':150000,'gross_profit':150000,'net_profit':70000},
    {'gross_margin_percent':D(150000)/300000*100,'net_margin_percent':D(70000)/300000*100},
    {'gross_margin_percent':'50.00','net_margin_percent':'23.33'},source('QP-2022-P1',14))
add('2022-P2-liquidity',{'current_assets':125000,'inventory':50000,'debtors':60000,'cash':15000,'current_liabilities':100000},
    {'current_ratio':D(125000)/100000,'quick_ratio':D(75000)/100000},
    {'current_ratio':'1.25','quick_ratio':'0.75'},source('QP-2022-P2',2),'Ratios are x:1, not percentages.')
add('2023-P2-liquidity',{'first_column_label_in_case':2019,'first_column_label_in_question_and_report':2020,
                      'first':{'inventory':3000,'debtors':12000,'cash':5000,'liabilities':15000},
                      '2022':{'inventory':4000,'debtors':8000,'cash':4000,'liabilities':18000}},
    {'first_current':D(20000)/15000,'first_quick':D(17000)/15000,
     '2022_current':D(16000)/18000,'2022_quick':D(12000)/18000},
    {'first_current':'1.33','first_quick':'1.13','2022_current':'0.89','2022_quick':'0.67'},source('QP-2023-P2',2),
    'Source-year discrepancy retained. ER-2023 displays 0.88 and 0.66 in the 2022 column; two-decimal rounding gives 0.89 and 0.67.')
series={str(2019+i):5000+1500*i for i in range(4)}
assert series=={'2019':5000,'2020':6500,'2021':8000,'2022':9500}
checks.append({'check_id':'2023-P2-line-graph','inputs':{'2019':5000,'annual_increase_from_2020':1500},
               'recomputed_tonnes_by_year':series,'source_locator':source('QP-2023-P2',2),
               'axis_requirements':['year','output in tonnes'],'status':'pass','provenance':'corpus inputs; arithmetic derived'})
add('2024-P2-solvency',{'current_assets':53000,'fixed_assets':104000,'current_liabilities':57000,'long_term_liabilities':246000,'2023_ratio':'0.98:1'},
    {'2024_total_assets':D(157000),'2024_total_liabilities':D(303000),'2024_solvency_ratio':D(157000)/303000},
    {'2024_total_assets':'157000.00','2024_total_liabilities':'303000.00','2024_solvency_ratio':'0.52'},source('QP-2024-P2',2),
    'x:1. Correct order is assets/liabilities. It falls from 0.98:1; source guide accepts 0.51 or 0.52, but ordinary two-decimal rounding gives 0.52.')
checks.append({'check_id':'2020-P1-span-of-control','source_locator':source('QP-2020-P1',4),
               'visual_reading':{'managing_director_direct_reports':['Manager Product A','Manager Product B'],
                                 'marketing_manager_direct_reports':['Sales Manager','Public Relations Manager']},
               'recomputed_counts':{'managing_director':2,'marketing_manager':2},
               'status':'pass','provenance':'visually read chart links, then counted'})
doc={'status':'pass','numeric_and_chart_checks':len(checks),
     'rounding':'Annexe A: two decimal places; Decimal ROUND_HALF_UP used for decimal calculations.',
     'checks':checks,'limitations':'This verifies extracted case calculations and one source chart, not every numerical illustration in all examiner model answers. Official cases and answers remain internal evidence.'}
(OUT/'numeric-verification.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(checks),'source-linked numerical/chart checks')
