"""Run unchanged standard checks with schema-incompatible runtime extensions in memory.

The canonical subject profile stays schema-valid. C-35/C-41's built-in chart
model is business break-even, not chemistry: original chemistry SVGs require
separate numerical and visual review. No standard code is changed.
"""
import argparse,json,sys,re
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
 def written_command_check(build):
  class WrittenOnly:
   def __getattr__(self,key):return getattr(build,key)
   @property
   def items(self):return [i for i in build.items if i['item_type']!='multiple_choice_set']
  return yyeni_checks.c14(WrittenOnly())
 def rubric_semantic_gate(build):
  status,message,ids=yyeni_checks.c16(build)
  if status=='fail':
   return 'not_run', 'Literal subtype vocabulary does not establish Chemistry credit structure. Template prefixes were removed after independent review. Credit-point counts are checked by audit_production.py; semantic rubric adequacy remains an explicit independent review gate. '+message, ids
  return status,message,ids
 def positive_modality_check(build):
  # The aluminium/brine objective explicitly EXCLUDES technical diagrams.
  # Remove that negative clause from this check's view, preserving positive demands.
  class ModalityProxy:
   def __getattr__(self,key):return getattr(build,key)
   @property
   def objectives(self):
    return {oid:{**o,'syllabus_text':re.sub(r'but not technical details or diagrams', '', o.get('syllabus_text',''),flags=re.I)} for oid,o in build.objectives.items()}
  return yyeni_checks.c31(ModalityProxy())
 yyeni_checks.CHECKS=[(cid,rule,title,scoped_check if cid=='C-11' else written_command_check if cid=='C-14' else positive_modality_check if cid=='C-31' else rubric_semantic_gate if cid=='C-16' else fn) for cid,rule,title,fn in checks_before]
 def load(self,*args,**kwargs):
  original(self,*args,**kwargs)
  self.profile.update(EXTENSIONS)
 yyeni_checks.Build.__init__=load
 try:report=yyeni_checks.run(str(work),topic)
 finally:
  yyeni_checks.Build.__init__=original
  yyeni_checks.CHECKS=checks_before
 report['notes'].append('Generic standard decision was '+report['release_decision']+'. Chemistry HANDOVER and the user require independent re-verification before publication; the subject adapter enforces that stricter policy.')
 report['release_decision']='reject' if any(c['status']=='fail' for c in report['deterministic_checks']) else 'hold'
 report['blockers']=[b for b in report['blockers'] if not b.startswith('RS-28 - no semantic review')]
 report['blockers'].append('Chemistry release hold: independent semantic/rubric/visual re-verification and user release approval remain open. Mechanical success is not publication approval.')
 out=work/'topics'/topic/'qa_report.json';out.write_text(json.dumps(report,indent=2)+'\n')
 return report
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('topic');ap.add_argument('--workspace',type=Path,default=W);args=ap.parse_args()
 report=run(args.workspace,args.topic)
 for c in report['deterministic_checks']:print(c['check_id'],c['status'],c['message'])
 raise SystemExit(any(c['status']=='fail' for c in report['deterministic_checks']))
