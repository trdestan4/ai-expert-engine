# Docker, Serverless and Vercel-style Deployment

## Containers

Use minimal trusted base images, deterministic dependency install, non-root user where practical, explicit workdir/entrypoint and `.dockerignore`. Multi-stage builds reduce toolchain/runtime surface. Pin image versions/digests according to update policy; scan/provenance evidence may be required.

Do not bake secrets into image layers/build args. Configure health/readiness externally and handle SIGTERM/graceful shutdown. Container filesystem is usually ephemeral; persistent state belongs in designed storage.

## Serverless/functions

Design for stateless/reentrant execution, concurrency and cold starts appropriate to platform. Reuse clients carefully at module scope but never request/user state. Bound execution time/memory and external calls; background work after response may be terminated unless platform supports it.

Database pools need serverless-aware limits/proxies. Retries can duplicate effects; idempotency is application responsibility.

## Vercel/edge runtimes

Verify framework/runtime compatibility, region, Node vs edge API differences, environment variables, build output, preview/production domains and cache behavior. Edge is not automatically faster for data-bound work and may limit libraries/runtime APIs.

Production deployment command must pass AI Expert release gate with production environment; preview/staging GO cannot unlock prod.
