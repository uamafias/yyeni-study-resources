"""Supplement the accounting audit with pay, price and currency recomputations."""
import json,subprocess,sys
from fractions import Fraction as F
from pathlib import Path
W=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(W/'topics/2.4/verify_numbers.py')],check=True)
values=[('monthly salary',F(120000,12),10000),('piece earnings',4*80,320),('time earnings',35*40,1400),('combination incentive',3*(120-100),60),('combination earnings',900+3*(120-100),960),('commission',F(5,100)*20000,1000),('profit pool',F(10,100)*80000,8000),('linked normal price',80*F(125,100),100),('linked discount',100*F(10,100),10),('linked final price',100-10,90),('cost-plus member',120*F(120,100),144),('promotional member',150*F(85,100),F(255,2)),('marketing case normal',80*F(150,100),120),('marketing case promotion',120*F(75,100),90),('marketing case spread',90-80,10),('snack promotion',50*F(90,100),45),('snack normal spread',50-35,15),('snack promotion spread',45-35,10),('production initial rate',F(400,10),40),('production later rate',F(480,12),40),('packs per labour hour',F(200,40),5),('currency N$',150*20,3000),('finance total needs',120000+15000,135000),('finance spare remaining',65000-60000,5000),('box survey percentage',F(12,40)*100,30),('wrap survey percentage',F(18,40)*100,45),('salad survey percentage',F(10,40)*100,25)]
for name,actual,expected in values:assert actual==expected,(name,actual,expected)
report={'method':'Exact fraction or integer recomputation of original supplied data; this supplements shared numerical checks, not an independent subject review.','supplementary_checks':[{'name':n,'actual':str(a),'expected':str(e),'pass':True} for n,a,e in values],'accounting_checks':38,'total_arithmetic_checks':len(values)+38,'failures':0}
(W/'authoring-numerical-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(report['total_arithmetic_checks'],'arithmetic checks passed.')
