// Original SVG rasterisation only; uses installed app dependencies read-only.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath}from'node:url';
import {createRequire}from'node:module';
const dir=path.dirname(fileURLToPath(import.meta.url));
if(!process.argv[2])throw Error('Pass application apps/web path for installed sharp dependency');
const req=createRequire(path.join(path.resolve(process.argv[2]),'package.json'));
const sharp=req('sharp');const gallery=path.join(dir,'e1-trig-gallery');
const files=fs.readdirSync(gallery).filter(x=>x.endsWith('.svg')).sort();const output=[];
for(const file of files){const svg=fs.readFileSync(path.join(gallery,file));const name=file.slice(0,-4);const png=await sharp(svg).png().toBuffer();fs.writeFileSync(path.join(gallery,name+'.png'),png);output.push({domain_index:Number(name.slice(4)),svg:path.posix.join('authoring/e1-trig-gallery',file),png:path.posix.join('authoring/e1-trig-gallery',name+'.png'),sha256:crypto.createHash('sha256').update(png).digest('hex')});}
const thumbs=await Promise.all(output.map(async item=>await sharp(path.join(dir,'..',item.png)).resize(600,320).png().toBuffer()));
await sharp({create:{width:1800,height:Math.ceil(files.length/3)*320,channels:4,background:'white'}}).composite(thumbs.map((input,i)=>({input,left:i%3*600,top:Math.floor(i/3)*320}))).png().toFile(path.join(gallery,'contact-sheet.png'));
fs.writeFileSync(path.join(dir,'e1-trig-render.json'),JSON.stringify({status:'rendered-awaiting-visual-inspection',method:'sharp/librsvg, source1200x640, contactthumb600x320',sharp_version:req('sharp/package.json').version,rendered:output.length,images:output,limits:'Static SVG render; not application UI or marker acceptance'},null,2)+'\n');
console.log(JSON.stringify({rendered:output.length,indices:output.map(x=>x.domain_index)}));
