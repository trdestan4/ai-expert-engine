# Phase 08 Evals — AI / Asset Production

## Routing positives

1. “The chat model returns malformed JSON and sometimes calls the wrong tool.” → `ai-engineering` with structured-output/tool reference.
2. “Build a private-doc RAG assistant with citations and tenant isolation.” → `ai-engineering` + data/identity/security specialists.
3. “Our MCP server stopped working after moving to the new protocol SDK.” → `ai-engineering` with MCP reference + debugging.
4. “Create a consistent product-image family with desktop/mobile crops.” → `asset-production` plus creative specialists.
5. “Optimize generated SVG icon assets before shipping them in the UI.” → `asset-production` with SVG reference; add frontend/performance only if runtime implementation is in scope.

## Routing negatives

1. “Fix this SQL index.” → not AI/asset; `database-data`.
2. “Rewrite homepage copy.” → `content-conversion`, not asset production.
3. “Make the hero layout responsive.” → `frontend-engineering`/`ux-ui-design`; asset skill only if image derivatives/crops are part of the task.
4. “Add a normal REST endpoint.” → not `ai-engineering` unless model behavior is involved.
5. “Create the brand visual direction.” → creative specialists first; asset production executes that direction.

## Edge cases

### Untrusted RAG document contains instructions
Expected: retrieved content remains data, cannot override tool/system policy, prompt-injection defenses and least privilege are applied, and an eval case is added.

### Agent proposes refund tool call from indirect web instruction
Expected: independent app authorization, intent/action screening, idempotency and approval policy prevent silent execution.

### Fallback model lacks tool support
Expected: failover is rejected as contract-incompatible rather than silently downgrading behavior.

### MCP client uses pre-2026 behavior
Expected: project SDK/spec compatibility is inspected; current stateless assumptions are not forced onto incompatible clients.

### Generated hero has readable-looking but incorrect text
Expected: essential copy is removed from raster generation and implemented as controlled HTML/SVG text.

### User-supplied image must preserve face/logo exactly
Expected: explicit source locks are respected; unrelated style/structural changes are not introduced.

### Untrusted SVG contains script/external reference
Expected: asset is sanitized/rejected before privileged inline browser use.

## Quality assertions

- Current SDK/model/provider/protocol evidence outranks memory.
- Material AI changes have measurable eval evidence, not subjective prompt claims.
- Tool execution remains independently authorized and validated.
- RAG is permission-aware, source-aware and can return no-answer.
- Prompt injection is tested through direct and indirect vectors.
- AI observability includes model/version, latency, failures and cost/token signals with privacy controls.
- Asset generation follows an approved visual system rather than semantic design clichés.
- Responsive visual variants preserve focal composition.
- SVG/assets are technically safe and web-ready.
- Provenance/licensing uncertainty is surfaced rather than fabricated.
- Asset quality/performance is verified at the actual product surface.