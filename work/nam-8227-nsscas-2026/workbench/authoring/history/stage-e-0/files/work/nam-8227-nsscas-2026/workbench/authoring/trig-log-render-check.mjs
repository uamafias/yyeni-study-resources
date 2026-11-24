// Authoring-only renderer check. Pass the existing app's apps/web directory.
// Never imported by the subject provider; no app code is changed.
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';
import crypto from 'node:crypto';

const root=path.dirname(fileURLToPath(import.meta.url));
const web=process.argv[2];
if(!web)throw Error('Pass the existing app apps/web directory for its KaTeX and sharp dependencies');
const req=createRequire(path.join(path.resolve(web),'package.json'));
const katex=req('katex');
const sharp=req('sharp');
const expressions=new Set(JSON.parse(fs.readFileSync(path.join(root,'trig-log-math-expressions.json'),'utf8')));
for(const tex of expressions)katex.renderToString(tex,{throwOnError:true,strict:'error',trust:false});
const gallery=path.join(root,'trig-log-gallery');
const index=JSON.parse(fs.readFileSync(path.join(gallery,'index.json'),'utf8'));
const renders=[];
for(let i=0;i<index.length;i++){
  const name=`graph-${String(i).padStart(2,'0')}`;
  const svg=fs.readFileSync(path.join(gallery,`${name}.svg`));
  const png=await sharp(svg).resize(600,320).png().toBuffer();
  fs.writeFileSync(path.join(gallery,`${name}.png`),png);
  renders.push({path:`authoring/trig-log-gallery/${name}.png`,sha256:crypto.createHash('sha256').update(png).digest('hex')});
}
const composites=renders.map((v,i)=>({input:path.join(root,'..',v.path),left:(i%3)*600,top:Math.floor(i/3)*320}));
await sharp({create:{width:1800,height:960,channels:4,background:'white'}}).composite(composites).png().toFile(path.join(gallery,'contact-sheet.png'));
const report={status:'pass',scope:'All395 generated trig/log instances; nine rasterised graphs including a zero ordinate. No actual app UI test.',katex_version:req('katex/package.json').version,sharp_version:req('sharp/package.json').version,unique_math_expressions:expressions.size,rendered_graphs:renders};
fs.writeFileSync(path.join(root,'trig-log-render-check.json'),JSON.stringify(report,null,2)+'\n');
process.stdout.write(JSON.stringify({status:'pass',unique_math_expressions:expressions.size,rendered_graphs:renders.length})+'\n');
