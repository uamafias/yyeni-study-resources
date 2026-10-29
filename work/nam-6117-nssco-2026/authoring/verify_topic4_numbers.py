"""Independent arithmetic pass over the fixed authored numerical cases."""
import json,math
from pathlib import Path
W=Path(__file__).resolve().parents[1]
rows=[]
def check(slot,expression,result,expected,unit,tolerance=1e-8):
 ok=abs(result-expected)<=tolerance
 rows.append({'item_id':f'ITEM-6117-4-{slot:03d}-CALC','independent_working':expression,'recomputed':result,'authored_result':expected,'unit_or_formula':unit,'tolerance':tolerance,'pass':ok})
 assert ok,rows[-1]
for args in [(9,'4.8/24 × 40',4.8/24*40,8,'g'),(10,'10/40 × 24',10/40*24,6,'g'),(11,'25/100 × 56',25/100*56,14,'g'),(12,'3.2/32 × 2 × 18',3.2/32*2*18,3.6,'g'),(13,'.150 × 40/1000',.15*40/1000,.006,'mol'),(14,'.0100/(25/1000)',.01/(25/1000),.4,'mol/dm³'),(15,'(.100 × 25/1000)/.200 × 1000',(.1*25/1000)/.2*1000,12.5,'cm³'),(16,'min(.100×20/1000,.100×25/1000)×58.5',min(.1*.020,.1*.025)*58.5,.117,'g'),(17,'.250 × 24',.25*24,6,'dm³ at room conditions'),(18,'(120/1000)/24',.12/24,.005,'mol'),(19,'2.50/100×24',2.5/100*24,.6,'dm³ at room conditions'),(20,'1.20×2',1.2*2,2.4,'dm³ at same room conditions')]:check(*args)
for slot,masses,ars,target,formula in [(21,[40,6.67,53.33],[12,1,16],[1,2,1],'CH2O'),(22,[.480,.320],[24,16],[1,1],'MgO'),(23,[52.18,13.04,34.78],[12,1,16],[2,6,1],'C2H6O'),(24,[54.55,9.09,36.36],[12,1,16],[2,4,1],'C2H4O')]:
 amounts=[m/a for m,a in zip(masses,ars)];ratio=[a/min(amounts) for a in amounts];error=max(abs(a-b) for a,b in zip(ratio,target));check(slot,f'Amounts {amounts}; normalised ratio {ratio}',error,0,formula,.002)
for slot,mr,em,mult,formula in [(25,180,12+2+16,6,'C6H12O6'),(26,56,12+2,4,'C4H8'),(27,92,14+32,2,'N2O4'),(28,78,12+1,6,'C6H6')]:check(slot,f'{mr}/{em}; multiply each empirical subscript',mr/em,mult,formula)
for args in [(29,'40/(40+12+3×16)×100',40/100*100,40,'%',1e-8),(30,'(2×14)/(2×14+4+3×16)×100',28/80*100,35,'%',1e-8),(31,'28/(28+8+32+64)×100',28/132*100,21.2,'%',.05),(32,'16/(24+16)×100',16/40*100,40,'%',1e-8),(33,'8/10×100',8/10*100,80,'%',1e-8),(34,'4.76/5.60×100',4.76/5.6*100,85,'%',1e-8),(35,'9/.75',9/.75,12,'g',1e-8),(36,'11.2/(25/100×56)×100',11.2/(25/100*56)*100,80,'%',1e-8),(37,'12/15×100',12/15*100,80,'%',1e-8),(38,'4.25/5×100',4.25/5*100,85,'%',1e-8),(39,'20×.90',20*.9,18,'g',1e-8),(40,'(1.92/24×100)/10×100',1.92/24*100/10*100,80,'%',1e-8)]:check(*args)
assert len(rows)==32
activities={'P02_concentration':.01/.250,'P03_titre_cm3':25.4-.4,'P03_HCl_mol':.1*(25.4-.4)/1000,'P03_NaOH_concentration':(.1*(25.4-.4)/1000)/.025,'P04_CO2_dm3':(.2*.025/2)*24}
expected=[.04,25,.0025,.1,.06]
assert all(math.isclose(a,b,rel_tol=1e-10) for a,b in zip(activities.values(),expected))
(W/'topics/4/numerical-audit.json').write_text(json.dumps({'status':'pass','method':'Separate arithmetic expressions recomputed from the authored givens and compared with their stated answers; chemical assumptions were author-reviewed separately.','cards':rows,'activities':activities,'limits':'This checks arithmetic, not an independent chemical or pedagogical review.'},indent=2)+'\n')
print('32 calculation variants and five activity results independently recomputed; all pass.')
