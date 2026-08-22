# Technical Crawl / Indexation

Treat crawlability, indexability and canonicalization as separate questions. Verify final HTTP status, redirect chains, robots.txt accessibility, page-level robots directives, canonical targets, sitemap URLs and rendered content. Important navigation should expose normal crawlable links. Avoid accidental noindex on production, canonicalizing distinct pages to irrelevant parents, redirect loops, soft-404 behavior and parameter explosions.

For migrations, inventory old-to-new URLs, prefer direct one-hop permanent redirects, update internal links/canonicals/sitemaps, preserve valuable content and monitor coverage/search traffic after launch. JavaScript frameworks are acceptable, but essential search content and links must survive rendering failures and should not depend on user interaction to exist.

Use log/Search Console evidence when available. Do not infer ranking problems from crawl metrics alone.