import puppeteer from 'puppeteer-core';
const [file, width, height] = process.argv.slice(2);
const enc = encodeURI(file.normalize('NFC'));
const ORIGIN = `http://127.0.0.1:5292/${enc}`;
const MIG = `http://localhost:5274/${enc}`;
async function measure(url, w, h, noJs) {
  const browser = await puppeteer.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true, args: ['--hide-scrollbars', '--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: Number(w), height: Number(h), deviceScaleFactor: 1 });
  if (noJs) {
    await page.evaluateOnNewDocument(() => { document.addEventListener('DOMContentLoaded', () => document.documentElement.classList.add('no-js')); });
  }
  await page.goto(url, { waitUntil: 'networkidle0', timeout: 90000 });
  await page.evaluate(async () => {
    const step = Math.max(200, Math.floor(window.innerHeight * 0.8));
    for (let y = 0; y < document.documentElement.scrollHeight; y += step) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 60)); }
    window.scrollTo(0, 0);
  });
  await page.waitForNetworkIdle({ idleTime: 400, timeout: 30000 }).catch(() => {});
  await new Promise((r) => setTimeout(r, 1500));
  const data = await page.evaluate(() => {
    const main = document.querySelector('main');
    const els = Array.from(main.querySelectorAll('*')).filter((e) => !['SCRIPT', 'STYLE', 'LINK', 'META', 'NOSCRIPT', 'TEMPLATE'].includes(e.tagName));
    return { h: document.documentElement.scrollHeight, boxes: els.map((e) => { const r = e.getBoundingClientRect(); return [e.tagName.toLowerCase(), Math.round(r.x * 10) / 10, Math.round((r.y + window.scrollY) * 10) / 10, Math.round(r.width * 10) / 10, Math.round(r.height * 10) / 10]; }) };
  });
  if (process.env.STYLE_IDX) {
    const idx = process.env.STYLE_IDX.split(',').map(Number);
    data.styles = await page.evaluate((idx) => {
      const els = Array.from(document.querySelector('main').querySelectorAll('*')).filter((e) => !['SCRIPT','STYLE','LINK','META','NOSCRIPT','TEMPLATE'].includes(e.tagName));
      return idx.map((i) => { const e = els[i]; const cs = getComputedStyle(e); return [i, e.tagName.toLowerCase(), cs.marginTop, cs.marginBottom, cs.paddingTop, cs.paddingBottom, cs.lineHeight, cs.fontSize, cs.height, cs.display, cs.position]; });
    }, idx);
  }
  await browser.close();
  return data;
}
const withTimeout = (p, ms) => Promise.race([p, new Promise((_, rej) => setTimeout(() => rej(new Error('tiempo máximo excedido')), ms))]);
const o = await withTimeout(measure(ORIGIN, width, height, true), 120000);
const m = await withTimeout(measure(MIG, width, height, false), 120000);
if (process.env.STYLE_IDX) { console.log('ORIGEN ' + JSON.stringify(o.styles)); console.log('MIGRADA ' + JSON.stringify(m.styles)); }
let diff = 0; const samples = [];
const n = Math.min(o.boxes.length, m.boxes.length);
for (let i = 0; i < n; i++) {
  const a = o.boxes[i], b = m.boxes[i];
  const bad = a[0] !== b[0] || [1, 2, 3, 4].some((k) => Math.abs(a[k] - b[k]) > 1);
  if (bad) { diff++; if (samples.length < Number(process.env.N || 6)) samples.push(`#${i} ${a.join(' ')} | ${b.join(' ')}`); }
}
if (process.env.DUMP) { (await import('node:fs')).writeFileSync(process.env.DUMP, JSON.stringify({ o: o.boxes, m: m.boxes })); }
console.log(JSON.stringify({ file, width, altoOrigen: o.h, altoMigrada: m.h, elementosOrigen: o.boxes.length, elementosMigrada: m.boxes.length, desalineados: diff, muestras: samples }, null, 1));
