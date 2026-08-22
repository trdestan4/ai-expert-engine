# Web Vitals and Rendering Performance

Use field metrics for real-user outcomes and lab traces for diagnosis. Current Core Web Vitals are LCP, INP and CLS. Good targets are LCP <= 2.5s, INP <= 200ms and CLS <= 0.1 at the 75th percentile, segmented meaningfully by device/network where possible.

Diagnose LCP by separating server response, resource discovery/download and rendering delay. Diagnose INP by finding long main-thread tasks, expensive event work, rendering/layout and unnecessary hydration/re-renders. Diagnose CLS by reserving space for media/ads/embeds, stabilizing fonts and avoiding late DOM/layout shifts.

Prefer streaming/progressive delivery when it improves meaningful content without excessive client work. Avoid sending large client bundles to render mostly static content. Measure interaction on realistic lower-end devices, not only desktop development hardware.

A Lighthouse-style score is a signal, not the product goal. Record before/after field or representative lab evidence for important performance changes.