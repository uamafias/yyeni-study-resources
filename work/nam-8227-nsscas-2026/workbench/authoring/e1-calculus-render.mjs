// Authoring-only static notation proof; existing KaTeX installation read-only.
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath,pathToFileURL} from 'node:url';
const a=path.dirname(fileURLToPath(import.meta.url)),web=process.argv[2];
if(!web)throw Error('Pass existing app apps/web directory');
const req=createRequire(path.join(path.resolve(web),'package.json')),katex=req('katex');
const data=JSON.parse(fs.readFileSync(path.join(a,'e1-calculus-prime-render-inputs.json'),'utf8'));
const css='katex.min.css';
const escape=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
const html=tex=>katex.renderToString(tex,{throwOnError:true,strict:'error',trust:false});
const examples=[['y\\prime',"y'"],['f\\prime(x)',"f'(x)"],['f\\prime\\prime(x)',"f''(x)"]];
for(const [before,after]of examples){if(!html(after).includes('msupsub'))throw Error('Prime was not superscripted');}
for(const row of data)html(row.tex);
const rows=examples.map(([old,now])=>`<tr><td>${escape(old)}</td><td>${html(old)}</td><td>${escape(now)}</td><td>${html(now)}</td></tr>`).join('');
const actual=[...data.filter(r=>r.branch==="normal"&&r.domain_index===0).slice(0,6),...data.filter(r=>r.branch==="gradient"&&r.domain_index===0).slice(0,4),...data.filter(r=>r.branch==="two-extrema"&&r.domain_index===0).slice(0,4),...data.filter(r=>r.branch==="flat-classification"&&r.domain_index===0).slice(0,4)].map(r=>`<section><small>${escape(r.branch)} / row ${r.domain_index}</small><div>${html(r.tex)}</div></section>`).join('');
const page=`<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>body{font:18px Arial;margin:32px;color:#17212b}h1{font-size:26px}table{border-collapse:collapse;width:100%}td,th{padding:18px;border:1px solid #ddd}.katex{font-size:1.25em}section{margin:18px 0;padding:14px;background:#f7f9fb}small{display:block;margin-bottom:12px}</style><h1>E1 derivative notation — before and after</h1><p>Static resource render only; no app workflow acceptance.</p><table><tr><th>Old source</th><th>Old appearance</th><th>Corrected source</th><th>Corrected appearance</th></tr>${rows}</table><h2>Actual corrected emitted expressions</h2>${actual}`;
fs.writeFileSync(path.join(a,'e1-calculus-render.html'),page);
fs.writeFileSync(path.join(a,'e1-calculus-render-structure.json'),JSON.stringify({status:'pass',katex_version:req('katex/package.json').version,generated_expressions_parsed:data.length,prime_superscript_pairs:3,actual_render_rows:(actual.match(/<section>/g)||[]).length,scope:'HTML prime superscript structure plus actual expressions; screenshot inspected separately'},null,2)+'\n');
console.log(JSON.stringify({status:'pass',parsed:data.length,renderRows:(actual.match(/<section>/g)||[]).length}));
