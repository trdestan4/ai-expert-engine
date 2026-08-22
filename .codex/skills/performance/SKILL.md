---
name: performance
description: Owns end-to-end performance engineering across Core Web Vitals, rendering, JavaScript/CSS/assets, network/cache/CDN, backend/API/database latency, concurrency, resource budgets, profiling, field telemetry, and regression gates; it optimizes measured bottlenecks rather than speculative micro-optimizations.
---

# Purpose

Deliver fast, stable experiences under realistic devices, networks, data sizes and production load by measuring first, assigning explicit budgets and fixing the highest-impact bottlenecks.

## Use when

- page load, interaction, rendering, bundle, asset, API, database or job latency is slow;
- Core Web Vitals, throughput, memory, CPU, connection or cache behavior needs improvement;
- a feature could materially increase client/server cost;
- performance budgets, profiling, load tests or regression gates are required.

## Do not use when

- behavior is incorrect rather than slow (`debugging` first);
- query/index design is the primary task (`database-data`, then performance review);
- visual/accessibility quality is primary (`ux-ui-design` / `accessibility`);
- infrastructure availability/reliability is primary (`observability-sre`).

## Inputs

Collect:

- user-visible symptom and affected routes/actions;
- field metrics when available, segmented by device/network/region;
- lab profiles/traces/build/bundle data;
- request waterfalls and cache behavior;
- API/database/job latency distributions, not averages only;
- traffic/concurrency/data-size expectations;
- runtime/deployment limits and cost constraints;
- current budgets/regressions.

## Workflow

### 1. Define a user-centric target

Choose metrics tied to the actual experience. For web UX, current Core Web Vitals use LCP, INP and CLS; target field performance at the 75th percentile rather than treating one fast lab run as success.

### 2. Measure before editing

Capture baseline field/lab/server evidence. Separate network, server, main-thread, rendering, image/font, hydration, database and third-party time.

### 3. Fix critical path first

Remove serial waterfalls, blocking resources and unnecessary client/server work on the path users wait for. Parallelize independent work and defer non-critical work.

### 4. Reduce shipped/runtime work

Limit JavaScript, hydration scope, component churn, expensive CSS/layout, image bytes, font variants and third-party scripts. Prefer server/native/browser capabilities where they reduce runtime cost without harming UX.

### 5. Make caching semantic

Define what may be cached, for how long, by whom, and how it invalidates. Optimize hit rate without serving incorrect/private/stale data beyond acceptable freshness.

### 6. Optimize server/data paths

Profile hot APIs/jobs/queries. Remove N+1s, over-fetching, excessive serialization, repeated remote calls, unbounded scans and inefficient connection use. Coordinate with backend/database specialists for structural changes.

### 7. Test realistic stress

Use representative data, concurrency, cold/warm cache, slower devices and network conditions. Watch latency percentiles, errors, saturation and queue buildup.

### 8. Add regression budgets

Set budgets for bundle/assets, CWV, API latency, query time or job duration where useful. Fail/review regressions above meaningful thresholds rather than chasing tiny noise.

## Decision rules

- Optimize measured bottlenecks, not stylistic preferences.
- Field data outranks synthetic data for real-user experience; lab data is valuable for diagnosis/reproduction.
- Current good Core Web Vitals targets are LCP <= 2.5s, INP <= 200ms and CLS <= 0.1 at p75; verify if standards change.
- Reduce waterfalls before micro-optimizing individual functions.
- Do not trade correctness/security/accessibility for speed.
- A cache without freshness/invalidations is a correctness risk.
- Average latency can hide tail pain; use p50/p75/p95/p99 as appropriate.
- Performance work should include before/after evidence.

## Reference routing

Load `references/web-vitals-rendering.md` for LCP/INP/CLS, rendering and field measurement.
Load `references/bundles-assets-network.md` for JS/CSS/images/fonts/third parties/cache/CDN.
Load `references/backend-data-load.md` for API/database/jobs/concurrency/load profiling.

Use `react-nextjs`, `frontend-engineering`, `backend-engineering`, `database-data` and `observability-sre` for implementation-specific ownership.

## Quality gates

- Baseline and target are explicit.
- Optimization is tied to measured evidence.
- Critical path and waterfalls are understood.
- Client/server work and asset budgets are justified.
- Cache correctness/freshness semantics are documented.
- High-impact server/data paths use representative latency/load evidence.
- Before/after metrics demonstrate improvement or explain why not.
- No security, accessibility or correctness regression is introduced.

## Failure handling

If only synthetic evidence exists, state that limitation and avoid claiming real-user improvement. If a regression is noisy, gather more representative samples before overfitting. If optimization requires architecture/data changes, hand off to the owning specialist and retain the performance target as an acceptance criterion.

## Output contract

Return:

- baseline and bottleneck evidence;
- target/budget;
- prioritized optimizations;
- cache/runtime/data decisions;
- before/after metrics;
- regression gates and remaining risks.
