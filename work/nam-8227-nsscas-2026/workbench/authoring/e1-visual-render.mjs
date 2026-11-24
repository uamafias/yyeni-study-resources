// Static native asset inspection only; no app UI execution or mutations.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
import crypto from 'node:crypto';
const dir=path.dirname(fileURLToPath(import.meta.url));
if(!process.argv[2])throw Error('Pass existing app apps/web directory for installed sharp');
const require=createRequire(path.join(path.resolve(process.argv[2]),'package.json'));
const sharp=require('sharp');
const folder=path.join(dir,'visual/e1');
const index=JSON.parse(fs.readFileSync(path.join(folder,'index.json'),'utf8'));
let renders=[];
for(const item of index){
 const svg=fs.readFileSync(path.join(folder,item.name+'.svg'));
 const output=await sharp(svg).png().toBuffer();fs.writeFileSync(path.join(folder,item.name+'.png'),output);
 renders.push({...item,path:'authoring/visual/e1/'+item.name+'.png',sha256:crypto.createHash('sha256').update(output).digest('hex')});
}
for(let group=0;group<4;group++){
 const subset=renders.filter(x=>x.kind==='modulus').slice(group*12,(group+1)*12);
 const thumbs=[];
 for(let i=0;i<subset.length;i++){const buffer=await sharp(path.join(dir,'../',subset[i].path)).resize(570,338).toBuffer();thumbs.push({input:buffer,left:(i%3)*570,top:Math.floor(i/3)*338});}
 await sharp({create:{width:1710,height:Math.ceil(subset.length/3)*338,channels:4,background:'white'}}).composite(thumbs).png().toFile(path.join(folder,'modulus-contact-'+group+'.png'));
}
const report={status:'rendered-awaiting-author-inspection',scope:'67 native visual SVGs; no website/access/history or learner sketch recognition check',sharp_version:require('sharp/package.json').version,renders};
fs.writeFileSync(path.join(dir,'e1-visual-renders.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:'rendered',count:renders.length,contacts:4}));
