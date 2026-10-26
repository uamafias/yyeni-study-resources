"""Run unchanged standard checks with schema-incompatible runtime extensions in memory.

The canonical subject profile stays schema-valid. C-35/C-41's built-in chart
model is business break-even, not chemistry: original chemistry SVGs require
separate numerical and visual review. No standard code is changed.
"""
import argparse,json,sys
from pathlib import Path
W=Path(__file__).resolve().parents[1];R=W.parents[1]
sys.path.insert(0,str(R/'standard/v0.2.0-draft/checks'))
import yyeni_checks
from scope_text import scope_view
EXTENSIONS={'depictions':{'chart_model':'none'},'conditioned_mechanisms':[
 {'mechanism_id':'CHEM-GAS-24','asserted_when':[r'24\s*dm',r'mol'], 'required_conditions':[{'name':'room temperature and pressure','any_of':[r'room',r'\brtp\b']}]},
 {'mechanism_id':'CHEM-EQUILIBRIUM-PRESSURE','asserted_when':[r'pressure',r'(?:yield|equilibrium)',r'(?:increas|decreas|favour|shift)'], 'required_conditions':[{'name':'gaseous stoichiometry','any_of':[r'gas(?:eous)?',r'gas molecules',r'moles of gas']}]},
 {'mechanism_id':'CHEM-COPPER-ANODE','asserted_when':[r'anode',r'copper',r'dissolv'], 'required_conditions':[{'name':'active copper electrode','any_of':[r'copper anode',r'copper electrode',r'anode (?:is|of) copper']}]}
]}
def run(work,topic):
 original=yyeni_checks.Build.__init__
 checks_before=yyeni_checks.CHECKS[:]
 def scoped_check(build):
  class ScopeProxy:
   def __getattr__(self,key):return getattr(build,key)
   def learner_text(self):return [(a,b,scope_view(c,build.objectives.values())) for a,b,c in build.learner_text()]
   def answer_text(self):return [(a,b,scope_view(c,build.objectives.values())) for a,b,c in build.answer_text()]
  return yyeni_checks.c11(ScopeProxy())
 yyeni_checks.CHECKS=[(cid,rule,title,scoped_check if cid=='C-11' else fn) for cid,rule,title,fn in checks_before]
 def load(self,*args,**kwargs):
  original(self,*args,**kwargs)
  self.profile.update(EXTENSIONS)
 yyeni_checks.Build.__init__=load
 try:report=yyeni_checks.run(str(work),topic)
 finally:
  yyeni_checks.Build.__init__=original
  yyeni_checks.CHECKS=checks_before
 out=work/'topics'/topic/'qa_report.json';out.write_text(json.dumps(report,indent=2)+'\n')
 return report
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('topic');ap.add_argument('--workspace',type=Path,default=W);args=ap.parse_args()
 report=run(args.workspace,args.topic)
 for c in report['deterministic_checks']:print(c['check_id'],c['status'],c['message'])
 raise SystemExit(any(c['status']=='fail' for c in report['deterministic_checks']))
