# Web Asset Quality and Performance

Judge quality at the actual product surface. Inspect hero imagery at desktop/mobile crop, thumbnails at small sizes, alpha assets on real backgrounds and motion under realistic network/device conditions. A technically high-resolution file can still be a poor production asset if composition fails at use size.

Define performance budgets in partnership with `performance`; do not optimize every asset to one arbitrary byte number. Brand/product-detail imagery may justify more bytes than decorative backgrounds, while below-the-fold/supporting visuals can be aggressively deferred or compressed.

Strip unnecessary metadata from delivery files when it adds privacy or byte risk, but preserve metadata required for workflow, color management or legal/provenance needs in the appropriate master/source system. Never leak device paths, private comments or secrets through exported metadata.

Verify color profile/gamma and transparency. Watch for washed gradients, dark halos, banding and alpha fringes after conversion. Compare delivery encodes visually rather than trusting encoder quality settings.

Avoid layout shift by communicating intrinsic dimensions/aspect ratios to implementation. Provide stable placeholder/poster behavior for large imagery and video. Decorative background assets should not block critical content rendering.

For icons/SVG, simplify safely and reuse symbols/components where appropriate. For raster families, prefer a small deliberate derivative set selected by the runtime rather than dozens of unused exports.

Handoff should include measured byte sizes, dimensions, visual QA status, known fallback behavior and any asset whose quality/performance tradeoff requires implementation review.