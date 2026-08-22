# Technical SEO: Crawl, Render and Index Control

Use current official search-engine guidance for version-sensitive behavior. SEO recommendations must be testable and should not override product/accessibility/security correctness.

## Crawlability

Verify important URLs are discoverable through internal links/sitemaps where appropriate, return intended HTTP status, are not blocked unintentionally by robots directives and render meaningful content without requiring unsupported client interactions.

Robots.txt controls crawling, not guaranteed de-indexing or access control. Sensitive/private content requires authorization and appropriate noindex/removal strategy, never robots alone.

## Canonicalization

Choose one canonical URL for duplicate/variant content and align internal links, redirects, sitemap and canonical tags. Canonical is a hint, not a permission to produce infinite duplicates. Avoid canonicalizing materially different locale/product/filter pages to unrelated parents just to reduce index count.

## Status/redirects

Use 2xx for real content, 3xx for durable moves, 404/410 for gone content as policy dictates. Avoid soft 404s, redirect chains/loops and SPA catch-all returning 200 for nonexistent routes.

## JavaScript/rendering

Ensure critical content/meta/links are available in the chosen rendering model and verify with search tooling/render tests when material. Client-side rendering can work but increases dependency on execution and can delay discovery; choose architecture from product/performance constraints, not SEO folklore.

## Sitemaps

Include canonical indexable URLs, correct lastmod only when meaningful and split/manage large sitemaps. Sitemaps do not replace internal linking or fix low-quality duplicate pages.

## Large-site/log analysis

For large catalogs/content sites, crawl samples and server/CDN logs can reveal wasted crawl on parameters/facets, orphan URLs, redirect loops and bot error patterns. Prioritize index-worthy content rather than maximizing crawl count.

## Migrations

Before URL/domain/framework migration inventory high-value URLs, map redirects, preserve metadata/structured data/internal links, verify analytics/search-console access and monitor post-launch indexing/404/traffic by cohorts. Keep redirects long enough for users/search depending on business policy.
