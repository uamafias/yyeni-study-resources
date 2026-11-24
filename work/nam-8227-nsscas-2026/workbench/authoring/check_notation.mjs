import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';
const dir=path.dirname(fileURLToPath(import.meta.url));
if(!process.argv[2])throw Error('Pass existing application apps/web for installed KaTeX dependency; no app changes');
const req=createRequire(path.join(path.resolve(process.argv[2]),'package.json'));
const katex=req('katex');
const expressions=JSON.parse(fs.readFileSync(path.join(dir,'math-expressions.json'),'utf8'));
let errors=[];
for(const tex of expressions){try{katex.renderToString(tex,{throwOnError:true,strict:'error',trust:false});}catch(e){errors.push({tex,error:e.message});}}
const result={status:errors.length?'fail':'pass',scope:'All1702 generated stems, prompts, answers, steps and practice help; syntax only, not actual app display',katex_version:req('katex/package.json').version,expressions:expressions.length,errors};
fs.writeFileSync(path.join(dir,'../checks/stage-e/notation.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({...result,errors:errors.slice(0,12)}));
if(errors.length)process.exitCode=1;
