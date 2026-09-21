// Render both Markdown deliverables for local review; no preview CSS enters GitHub.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {pathToFileURL} from 'node:url';

const bundled = path.join(os.homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/marked/lib/marked.esm.js');
const {marked} = await import(process.env.MARKED_MODULE || pathToFileURL(bundled).href);
const style = `body{margin:0;background:#0d1117;color:#e6edf3;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}main{max-width:1012px;margin:auto;padding:32px}img{max-width:100%;height:auto}a{color:#79b8ff;text-decoration:none}a:hover{text-decoration:underline}p{margin:0 0 16px}h2{font-size:24px;border-bottom:1px solid #30363d;padding-bottom:8px;margin:32px 0 16px}details{border-top:1px solid #30363d;padding:12px 0}summary{cursor:pointer}details[open] summary{margin-bottom:12px}sub{font-size:12px}li{margin:8px 0}a:focus-visible,summary:focus-visible{outline:2px solid #b4e878;outline-offset:4px}table{border-collapse:collapse;width:100%}td,th{border:1px solid #30363d;padding:8px;text-align:left}@media(max-width:600px){main{padding:16px}body{font-size:16px}table{display:block;overflow:auto}}`;
const editions = [['es',''],['en','.en'],['zh','.zh'],['hi','.hi']];
const targets = editions.flatMap(([lang,suffix]) => [
 [`README${suffix}.md`,`docs/presentation-preview${suffix}.html`,`Mancar Software — ${lang}`,lang],
 [`docs/PROJECT-GALLERY${suffix}.md`,`docs/project-gallery-preview${suffix}.html`,`Mancar Software — ${lang}`,lang],
]);
targets.push(['docs/PROJECT-EVIDENCE.md','docs/project-evidence-preview.html','Mancar Software — capture sources','en']);
for (const [source,target,title,lang] of targets) {
 let content=marked.parse(fs.readFileSync(source,'utf8'));
 content=content.replace(/<h([1-6])>([^<]+)<\/h[1-6]>/g,(_,level,heading)=>`<h${level} id="heading-${heading.toLowerCase().replace(/[^\p{L}\p{N}\p{M} ]/gu,'').replace(/ +/g,'-')}">${heading}</h${level}>`);
 content=content.replaceAll('"profile/assets/','"../profile/assets/')
 .replaceAll('"docs/PROJECT-GALLERY.md','"project-gallery-preview.html')
 .replaceAll('"PROJECT-EVIDENCE.md','"project-evidence-preview.html');
 for (const [,suffix] of editions) {
   content=content.replaceAll(`href="README${suffix}.md`, `href="presentation-preview${suffix}.html`)
     .replaceAll(`href="docs/PROJECT-GALLERY${suffix}.md`, `href="project-gallery-preview${suffix}.html`);
 }
 const back='';
 fs.writeFileSync(target,`<!doctype html><html lang="${lang==='zh'?'zh-Hans':lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title}</title><style>${style}</style></head><body><main>${back}${content}</main></body></html>`);
}
console.log('Rendered presentation, gallery, and evidence previews.');
