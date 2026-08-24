#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import process from 'node:process';
import { chromium, firefox, webkit } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import pixelmatch from 'pixelmatch';
import { PNG } from 'pngjs';

function arg(name, fallback = null) {
  const i = process.argv.indexOf(name);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}
function flag(name) { return process.argv.includes(name); }
function mkdir(p) { fs.mkdirSync(p, { recursive: true }); }
function sha256(buf) { return crypto.createHash('sha256').update(buf).digest('hex'); }
function safe(s) { return String(s).replace(/[^a-z0-9._-]+/gi, '-').toLowerCase(); }

const url = arg('--url');
const output = arg('--output');
const browserArg = arg('--browser', 'all');
const screenshotsDir = arg('--screenshots-dir');
const baselineDir = arg('--baseline-dir');
const updateBaseline = flag('--update-baseline');
const timeoutMs = Number(arg('--timeout-ms', '30000'));
const settleMs = Number(arg('--settle-ms', '350'));
const diffThreshold = Number(arg('--diff-threshold', '0.001'));
if (!url || !output) {
  console.error('usage: master_browser_probe.mjs --url URL --output report.json [--browser all|chromium|firefox|webkit]');
  process.exit(2);
}

const launchers = { chromium, firefox, webkit };
const browsers = browserArg === 'all' ? ['chromium', 'firefox', 'webkit'] : [browserArg];
for (const name of browsers) if (!launchers[name]) throw new Error(`unknown browser ${name}`);
const viewports = [
  { name: 'mobile', width: 390, height: 844 },
  { name: 'tablet', width: 1024, height: 768 },
  { name: 'desktop', width: 1440, height: 900 }
];

async function diffScreenshot(actualPath, baselinePath, diffPath) {
  if (!fs.existsSync(baselinePath)) return { available: false, reason: 'baseline-missing' };
  const actual = PNG.sync.read(fs.readFileSync(actualPath));
  const baseline = PNG.sync.read(fs.readFileSync(baselinePath));
  if (actual.width !== baseline.width || actual.height !== baseline.height) {
    return { available: true, ratio: 1, reason: 'dimension-mismatch' };
  }
  const diff = new PNG({ width: actual.width, height: actual.height });
  const pixels = pixelmatch(actual.data, baseline.data, diff.data, actual.width, actual.height, { threshold: 0.1, includeAA: false });
  fs.writeFileSync(diffPath, PNG.sync.write(diff));
  return { available: true, ratio: pixels / (actual.width * actual.height), pixels };
}

async function probe(browserName, viewport) {
  const browser = await launchers[browserName].launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height }, reducedMotion: 'no-preference', colorScheme: 'light', locale: 'en-US' });
  await context.addInitScript(() => {
    window.__aiExpertPerf = { cls: 0, longTasks: 0, lcp: 0 };
    try { new PerformanceObserver(list => { for (const e of list.getEntries()) if (!e.hadRecentInput) window.__aiExpertPerf.cls += e.value || 0; }).observe({ type: 'layout-shift', buffered: true }); } catch {}
    try { new PerformanceObserver(list => { window.__aiExpertPerf.longTasks += list.getEntries().length; }).observe({ type: 'longtask', buffered: true }); } catch {}
    try { new PerformanceObserver(list => { const a = list.getEntries(); const e = a[a.length - 1]; if (e) window.__aiExpertPerf.lcp = e.startTime || 0; }).observe({ type: 'largest-contentful-paint', buffered: true }); } catch {}
  });
  const page = await context.newPage();
  const consoleErrors = [];
  const pageErrors = [];
  page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text().slice(0, 1000)); });
  page.on('pageerror', e => pageErrors.push(String(e).slice(0, 1000)));

  let response = null;
  let navigationError = null;
  const started = Date.now();
  try { response = await page.goto(url, { waitUntil: 'networkidle', timeout: timeoutMs }); } catch (e) { navigationError = String(e); }
  await page.waitForTimeout(settleMs);

  const dom = await page.evaluate(() => {
    const rects = [...document.querySelectorAll('body *')].map(el => el.getBoundingClientRect());
    const nav = performance.getEntriesByType('navigation')[0];
    const resources = performance.getEntriesByType('resource');
    let transferBytes = 0;
    for (const r of resources) transferBytes += r.transferSize || 0;
    const canvas = document.createElement('canvas');
    let webglAvailable = false;
    try { webglAvailable = !!(canvas.getContext('webgl2') || canvas.getContext('webgl')); } catch {}
    return {
      title: document.title,
      lang: document.documentElement.lang || null,
      h1Count: document.querySelectorAll('h1').length,
      mainCount: document.querySelectorAll('main').length,
      navCount: document.querySelectorAll('nav').length,
      formCount: document.querySelectorAll('form').length,
      buttonCount: document.querySelectorAll('button').length,
      linkCount: document.querySelectorAll('a[href]').length,
      imageCount: document.images.length,
      imagesMissingAlt: [...document.images].filter(i => !i.hasAttribute('alt')).length,
      overflowElements: rects.filter(r => r.width > 0 && (r.x < -1 || r.x + r.width > innerWidth + 1)).length,
      metaDescription: document.querySelector('meta[name="description"]')?.getAttribute('content') || null,
      canonical: document.querySelector('link[rel="canonical"]')?.href || null,
      webglAvailable,
      performance: {
        domContentLoadedMs: nav ? nav.domContentLoadedEventEnd : null,
        loadMs: nav ? nav.loadEventEnd : null,
        transferBytes,
        resourceCount: resources.length,
        cls: window.__aiExpertPerf?.cls ?? null,
        longTasks: window.__aiExpertPerf?.longTasks ?? null,
        lcpMs: window.__aiExpertPerf?.lcp ?? null
      }
    };
  });

  let axe = { violations: [] };
  try { axe = await new AxeBuilder({ page }).analyze(); } catch (e) { axe = { violations: [], error: String(e) }; }
  const impactCounts = { critical: 0, serious: 0, moderate: 0, minor: 0, unknown: 0 };
  for (const v of axe.violations || []) {
    const key = v.impact && impactCounts[v.impact] !== undefined ? v.impact : 'unknown';
    impactCounts[key] += 1;
  }

  let screenshot = null;
  let visual = null;
  if (screenshotsDir) {
    mkdir(screenshotsDir);
    const file = `${safe(browserName)}-${safe(viewport.name)}-${viewport.width}x${viewport.height}.png`;
    const actualPath = path.join(screenshotsDir, file);
    await page.screenshot({ path: actualPath, fullPage: true, animations: 'disabled' });
    screenshot = { path: actualPath, sha256: sha256(fs.readFileSync(actualPath)) };
    if (baselineDir) {
      mkdir(baselineDir);
      const baselinePath = path.join(baselineDir, file);
      if (updateBaseline) fs.copyFileSync(actualPath, baselinePath);
      visual = await diffScreenshot(actualPath, baselinePath, path.join(screenshotsDir, `diff-${file}`));
      if (visual.available) visual.pass = visual.ratio <= diffThreshold;
    }
  }

  const reduced = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height }, reducedMotion: 'reduce', locale: 'en-US' });
  const reducedPage = await reduced.newPage();
  let reducedMotionMedia = null;
  try {
    await reducedPage.goto(url, { waitUntil: 'domcontentloaded', timeout: timeoutMs });
    reducedMotionMedia = await reducedPage.evaluate(() => matchMedia('(prefers-reduced-motion: reduce)').matches);
  } catch {}
  await reduced.close();
  await context.close();
  await browser.close();

  return {
    browser: browserName,
    viewport,
    durationMs: Date.now() - started,
    navigation: { ok: !navigationError && !!response, status: response ? response.status() : null, error: navigationError },
    consoleErrors,
    pageErrors,
    dom,
    accessibility: { violationCount: (axe.violations || []).length, impactCounts, error: axe.error || null },
    reducedMotionMedia,
    screenshot,
    visual
  };
}

const results = [];
for (const browserName of browsers) for (const viewport of viewports) results.push(await probe(browserName, viewport));
const blockers = [];
for (const r of results) {
  if (!r.navigation.ok || (r.navigation.status && r.navigation.status >= 400)) blockers.push(`${r.browser}/${r.viewport.name}:navigation`);
  if (r.pageErrors.length) blockers.push(`${r.browser}/${r.viewport.name}:pageerror`);
  if (r.accessibility.impactCounts.critical > 0) blockers.push(`${r.browser}/${r.viewport.name}:axe-critical`);
  if (r.visual?.available && r.visual.pass === false) blockers.push(`${r.browser}/${r.viewport.name}:visual-regression`);
}
const report = { version: 1, url, generatedAt: new Date().toISOString(), node: process.version, platform: `${process.platform}-${process.arch}`, browsers, viewports, results, blockers, passed: blockers.length === 0 };
report.reportSha256 = sha256(Buffer.from(JSON.stringify(report)));
mkdir(path.dirname(output));
fs.writeFileSync(output, JSON.stringify(report, null, 2) + '\n');
console.log(`browser probe ${report.passed ? 'PASSED' : 'FAILED'}: ${results.length} states, blockers=${blockers.length}`);
process.exit(report.passed ? 0 : 1);
