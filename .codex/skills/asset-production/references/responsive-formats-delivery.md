# Responsive Formats and Delivery

Choose asset formats from content type, browser/toolchain support, transparency/animation needs and measured quality. Avoid format dogma. Modern image formats can reduce bytes, but the delivery pipeline must still provide compatible behavior for the project's supported browsers and processing stack.

Design responsive derivatives around layout breakpoints and meaningful composition changes. Use source dimensions that avoid unnecessary upscaling; generate only variants the implementation can actually select. Preserve a stable focal point and safe areas for text/overlays.

For art-directed images, a mobile crop may be a different composition rather than a smaller desktop image. Record intended crop/fit (`cover`, `contain`, object position) so frontend implementation does not guess.

Separate raster master from delivery encodes. Keep a high-quality source, then derive optimized outputs for the web. Avoid repeatedly re-encoding lossy files from previous lossy derivatives.

For transparency, verify edge quality against real light/dark backgrounds. For logos/icons, prefer vector when geometry permits. For photographs/product renders, inspect perceptual quality at display scale and high-DPI density.

Video delivery needs poster/fallback, appropriate dimensions/bitrate, preload behavior and mobile/network consideration. Do not auto-load multi-megabyte decorative motion simply because bandwidth was acceptable on desktop Wi-Fi.

Document filenames, dimensions, aspect ratio, format, semantic role and fallback. Coordinate with `frontend-engineering`/`performance` for `srcset`/picture/framework image behavior rather than embedding implementation-specific assumptions into the asset itself.