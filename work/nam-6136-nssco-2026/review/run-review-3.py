"""One bounded read-only Claude review; save its report without repeated polling."""
import datetime, json, os, subprocess
from pathlib import Path

WS=Path(__file__).resolve().parents[1]
REPO=WS.parents[1]
OUT=WS/'review'
state_path=OUT/'claude-resource-review-state-3.json'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(x):state_path.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
state={'review':3,'status':'running','started_at':now(),'worker_pid':os.getpid(),'model_requested':'opus','effort':'medium','reported_api_budget_usd':8,'fresh_session':True,'tools':['Read','Glob','Grep'],'report':'review/CLAUDE-RESOURCE-REVIEW-3.md'}
save(state)
print('Third independent whole-subject review started; report and completion state will be saved automatically.',flush=True)
cmd=['claude','--safe-mode','--restricted','--strict-mcp-config','--tools','Read,Glob,Grep','--allowedTools','Read','Glob','Grep','--permission-mode','plan','--model','opus','--effort','medium','--max-budget-usd','8','--no-session-persistence','--print','--output-format','json']
with (OUT/'CLAUDE-RESOURCE-REVIEW-INPUT-3.md').open() as inp, (OUT/'claude-resource-review-response-3.json').open('w') as out, (OUT/'claude-resource-review-stderr-3.log').open('w') as err:
    proc=subprocess.run(cmd,cwd=REPO,stdin=inp,stdout=out,stderr=err,text=True)
state.update({'finished_at':now(),'exit_code':proc.returncode})
try:
    result=json.loads((OUT/'claude-resource-review-response-3.json').read_text())
    state.update({k:result.get(k) for k in ['session_id','subtype','is_error','stop_reason','duration_api_ms','total_cost_usd','modelUsage']})
    report=result.get('result','')
    complete=proc.returncode==0 and not result.get('is_error',False) and result.get('subtype')=='success'
    state['status']='completed' if complete else 'incomplete_or_error'
    if report:(OUT/'CLAUDE-RESOURCE-REVIEW-3.md').write_text(report+'\n')
except (ValueError,OSError) as exc:
    state.update({'status':'error','error':str(exc)})
save(state)
print(json.dumps(state,ensure_ascii=False),flush=True)
