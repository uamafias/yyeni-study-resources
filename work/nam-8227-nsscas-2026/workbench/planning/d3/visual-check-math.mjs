// Offline Stage-D3 syntax check, not application/browser acceptance.
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath,pathToFileURL} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));const wb=path.resolve(here,'../..');
const nm='/Users/professor/conductor/workspaces/yyeni/chiang-mai/apps/web/node_modules';
const imp=async name=>import(pathToFileURL(path.join(nm,name,'index.js')).href);
const {unified}=await imp('unified');const {default:parse}=await imp('remark-parse');const {default:gfm}=await imp('remark-gfm');const {default:math}=await imp('remark-math');
const {default:katex}=await import(pathToFileURL(path.join(nm,'katex/dist/katex.mjs')).href);
const files=['work-orders','exemplars'].flatMap(dir=>['WB8227-modulus-graph-recovery','WB8227-trapezium-sketch-estimate','WB8227-vector-geometry'].map(rid=>dir+'/'+rid+'.md'));let errors=[],records=[];
for(const file of files){const raw=fs.readFileSync(path.join(wb,file),'utf8');let spans=0,tables=0;const tree=unified().use(parse).use(gfm).use(math).parse(raw);
 function visit(n,parent){if(n.type==='math'||n.type==='inlineMath'){spans++;try{katex.renderToString(n.value,{throwOnError:true,strict:'error',displayMode:n.type==='math'});}catch(e){errors.push({file,line:n.position?.start.line,error:e.message});}if(parent?.type==='emphasis'||parent?.type==='strong')errors.push({file,line:n.position?.start.line,error:'math inside emphasis'});}
 if(n.type==='table'){tables++;const widths=n.children.map(row=>row.children.length);if(new Set(widths).size!==1)errors.push({file,line:n.position?.start.line,error:'table column count mismatch',widths});}
 for(const child of n.children??[])visit(child,n);};visit(tree,null);
 if(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/.test(raw))errors.push({file,error:'control character'});records.push({file,mathematical_spans:spans,tables});}
const result={status:errors.length?'fail':'pass',method:'Offline unified/remark AST, strict KaTeX renderToString, table/emphasis/control checks. Does not prove local website rendering.',katex_version:katex.version,files:records,errors};fs.writeFileSync(path.join(wb,'checks/plan-repair-d3-visual-math-syntax.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({status:result.status,files:records.length,math_spans:records.reduce((a,r)=>a+r.mathematical_spans,0),errors}));if(errors.length)process.exit(1);
