"""Run the explicitly requested read-only Claude plan review; retain its output."""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
if len(sys.argv)>1:
    HERE=Path(sys.argv[1]).resolve()
command = [
    'claude', '-p', '--model', 'opus', '--effort', 'medium',
    '--output-format', 'stream-json', '--verbose', '--no-session-persistence',
    '--tools', 'Read,Glob,Grep', '--allowedTools', 'Read,Glob,Grep',
    '--permission-mode', 'dontAsk', '--permission-prompts', 'none',
    '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}',
    '--name', '6145 Economics '+HERE.name,
]
with (HERE / 'events.jsonl').open('w') as output, (HERE / 'stderr.log').open('w') as errors:
    process = subprocess.Popen(command, cwd=ROOT, stdin=subprocess.PIPE,
                               stdout=output, stderr=errors, text=True)
    (HERE / 'run.json').write_text(json.dumps({'pid': process.pid, 'command': command}, indent=2))
    process.communicate((HERE / 'PROMPT.txt').read_text())
events = []
for line in (HERE / 'events.jsonl').read_text().splitlines():
    try:
        events.append(json.loads(line))
    except json.JSONDecodeError:
        pass
result = next((e for e in reversed(events) if e.get('type') == 'result'), {})
(HERE / 'result.json').write_text(json.dumps(result, indent=2))
if result.get('result'):
    (HERE / 'REVIEW.md').write_text(result['result'] + '\n')
print(json.dumps({'exit_code': process.returncode, 'result_type': result.get('subtype'),
                  'is_error': result.get('is_error'), 'report': str(HERE / 'REVIEW.md')}))
raise SystemExit(process.returncode)
