---
name: seo
description: Owns search discoverability across technical SEO, crawl/indexation, information architecture, metadata, canonicals, structured data, internal linking, international/local/ecommerce SEO, content quality, launch/migration review, and search performance diagnostics; it does not own generic copywriting or application performance implementation.
---

# Purpose

Build search-visible web experiences that are crawlable, understandable, useful, trustworthy, and maintainable without chasing unsupported ranking myths or search-engine-specific hacks.

## Use when

- crawl/indexation, robots, sitemap, canonical, redirects, metadata, hreflang, structured data, internal linking, site architecture or search visibility is involved;
- ecommerce/product/category SEO, local SEO, migration/launch SEO, or search diagnostics are required;
- content/page templates need search-intent and entity-level review;
- generative search/AI search visibility is discussed and needs grounding in current official guidance.

## Do not use when

- the primary task is persuasion/copy only (`content-conversion`);
- runtime speed is the primary issue (`performance`);
- visual hierarchy/UX is primary (`ux-ui-design`);
- product catalog/order logic is primary (`ecommerce`).

## Inputs

Inspect target audience and markets, site type, current routes/URL patterns, rendered HTML, status codes/redirects, robots/sitemaps, canonical/hreflang, internal links, structured data, metadata, content uniqueness, indexation evidence, Search Console/analytics when available, and any migration constraints.

## Workflow

### 1. Establish search intent and page purpose
Map real user needs to indexable page types. Avoid creating pages solely to target keyword permutations.

### 2. Verify crawl and indexability
Check status codes, redirects, robots directives, robots.txt, canonicals, sitemap membership, duplicate/parameter handling and whether important content exists in rendered HTML.

### 3. Design information architecture
Ensure important pages are reachable through logical navigation and internal links. Keep category/entity relationships explicit and avoid orphaned commercial/content pages.

### 4. Optimize page semantics
Use accurate titles, descriptions, headings, descriptive links, image alt text where appropriate, meaningful copy, entity/context signals and structured data that matches visible content.

### 5. Apply specialist rules
Load ecommerce, local, international or structured-data guidance only when the site requires it. Validate against current search-engine documentation rather than assuming remembered rich-result behavior.

### 6. Protect migrations and launches
Map redirects, canonicals, sitemap changes, noindex removal, staging protections, internal links and monitoring before launch.

### 7. Measure outcomes
Separate crawl/indexation issues from ranking/CTR/conversion issues. Use evidence from Search Console, logs, analytics and SERP inspection where available.

## Decision rules

- Help users first; do not manufacture thin pages for keyword coverage.
- Technical crawl/indexation correctness precedes content tuning.
- Structured data must describe visible truthful content; it never guarantees a rich result.
- Canonical is a consolidation signal, not a substitute for clean architecture.
- Important pages need crawlable internal links; do not rely only on client-side interaction states.
- For AI/generative search, follow current official SEO guidance and high-quality source/content practices; reject invented GEO/AEO ranking formulas.
- Programmatic SEO is acceptable only when pages have genuine differentiated value and controlled indexation quality.

## Reference routing

Load `references/technical-crawl-index.md` for crawling, rendering, robots, canonicals, sitemaps, redirects and migrations.

Load `references/structured-data-entities.md` for Schema.org/JSON-LD, rich-result eligibility and entity semantics.

Load `references/ecommerce-local-international.md` for product/category, local-business and hreflang/international patterns.

Load `references/content-search-ai.md` for search intent, content quality, AI/generative search and measurement.

## Quality gates

- Important pages are crawlable/indexable by design.
- Canonical/redirect/robots/sitemap signals do not conflict.
- Search-critical content is present in usable rendered HTML.
- Page purpose and internal-link placement are intentional.
- Structured data validates and matches visible content.
- Migration/launch changes have redirect/indexation verification.
- SEO recommendations distinguish documented guidance from hypotheses.

## Failure handling

If search visibility evidence is unavailable, label conclusions as hypotheses and request/inspect Search Console or logs when possible. If current rich-result or AI-search behavior may have changed, verify current official documentation before prescribing markup. Never promise rankings.

## Output contract

Return search intent/page model, crawl/indexation findings, information-architecture actions, on-page/structured-data changes, launch/migration risks, measurement plan, and specialist handoffs.