# Media Processing

## Validation and decoding

Decode files with maintained libraries and explicit resource limits. Validate image dimensions/pixel count, video duration/resolution/codecs as needed, document/page limits and unsupported/active content. Do not trust metadata fields before parsing safely.

## Privacy metadata

Remove EXIF/GPS/device metadata from user-facing images when it is not required. Preserve orientation/color information intentionally; stripping all metadata blindly can damage rendering or workflows.

## Derivatives

Generate a controlled set of formats/sizes based on actual UI use. Prefer modern efficient formats when client/provider support fits, but retain compatibility fallbacks where needed. Avoid generating dozens of variants that are never requested.

Use immutable/versioned derivative keys tied to source version/transformation parameters so CDN caching and regeneration are deterministic.

## Async pipeline

Expensive transforms belong in background workers with bounded CPU/memory/time, retries only for transient failures, and terminal failure state. Store processing status separately from upload completion.

## Safety

Run risky converters/transcoders with sandbox/resource restrictions where feasible. Keep untrusted source inaccessible until required scan/validation passes. Do not execute embedded scripts/macros.

## Video

Transcoding can be expensive; define max input size/duration, target renditions and whether provider-managed media services are preferable. Stream large outputs from storage/CDN instead of application memory.

## Tests

Cover huge dimensions, malformed/truncated file, deceptive MIME, metadata privacy, transform timeout, duplicate processing, unsupported codec, derivative replacement, quarantine failure and deletion propagation.