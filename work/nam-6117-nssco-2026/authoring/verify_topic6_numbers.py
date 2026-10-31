"""Independent recalculation of the authored energy and rate cases."""
import json,math
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'topics/6'
cases=[('6-012',80*4.2*(26-20),2016,'J'),('6-013',2.10*1000/(100*4.2),5,'°C'),('6-014',436+193-2*366,-103,'kJ/mol'),('6-015',(436+243+183)/2,431,'kJ/mol'),('6-P01-3',50*4.2*4,840,'J'),('6-P03-b',(38-18)/(60-20),.5,'cm³/s'),('6-P04-b',100*4.2*(28-20),3360,'J'),('6-P04-c',436+243-2*431,-183,'kJ/mol'),('6-009-deltaH',10-40,-30,'kJ/mol'),('6-009-Ea',100-40,60,'kJ/mol')]
rows=[{'case':i,'calculated':a,'authored':b,'unit':u,'pass':math.isclose(a,b,rel_tol=1e-9)} for i,a,b,u in cases]
assert all(x['pass'] for x in rows)
(D/'numerical-audit.json').write_text(json.dumps({'status':'pass','method':'Independent arithmetic from stated inputs; does not replace semantic review.','cases':rows},indent=2)+'\n')
print(len(rows),'numerical cases pass')
