# AI Expert Engine v1.2

A token-efficient expert-engine architecture for production web design, software engineering, AI systems, asset production and release control in Cursor and Codex.

**Engine status: v1.2 hardened — 43 discoverable skills + 6 isolated Cursor reviewer subagents. No new discoverable skill was added in v1.2.**

## v1.2 evidence and runtime hardening
- routing/reviewer/release/checkpoint/telemetry data now has enforceable runtime schemas;
- routing activation width and real runtime token counts can be measured instead of guessed;
- independent reviewer findings can be persisted, resolved or explicitly accepted with expiry;
- production decisions can be built from candidate-bound evidence and technically blocked by the reusable release gate when wired into deployment;
- version-sensitive knowledge has freshness metadata and scheduled official-source checks;
- pinned real-world benchmark repos cover Next/Postgres auth, FastAPI full-stack, ecommerce and intentionally vulnerable legacy Node;
- multilingual/RTL guidance and stack profiles now cover Nuxt, SvelteKit, Astro, Remix, Go, Spring, .NET, Rails, MySQL, MongoDB, AWS/Terraform and Kubernetes without increasing discoverable-skill count;
- long-session context-drift and all six reviewer calibration corpora are executable live evals;
- engine updates use an explicit v1.1→v1.2 migration chain with state backup.

Normal Cursor use requires no Cursor API key. API access is optional only for automated live model benchmarks.

## Architecture principle
The engine keeps a bounded discoverable skill set and loads deep references, stack profiles, reviewer agents and deterministic tools only when needed. Complexity C0–C4 and risk R0–R4 remain separate; high-risk work escalates evidence and independent review without loading every skill.

## Build status
- Phase 00 — Core / AI Brain: complete
- Phase 01 — Creative / Product Intelligence: complete
- Phase 02 — Web Engineering / Frontend: complete
- Phase 03 — Backend / API Engineering: complete
- Phase 04 — Data / Platform: complete
- Phase 05 — Quality Engineering: complete
- Phase 06 — Business / Growth: complete
- Phase 07 — Production Engineering: complete
- Phase 08 — AI / Asset Production: complete
- Phase 09 — Final Control: complete

## Phase 00 — Core / AI Brain
Orchestration, repository intelligence, planning, debugging, token policy, schemas and routing.
## Phase 01 — Creative / Product Intelligence
Product strategy, creative direction, brand, anti-generic design, color, typography, visual art, motion and UX/UI.
## Phase 02 — Web Engineering / Frontend
Web-platform, frontend, React/Next.js and software architecture, now with deep i18n/RTL and non-React framework adapters.
## Phase 03 — Backend / API Engineering
Backend/API engineering with Node, Python, Go, JVM/Spring, .NET and Rails runtime adapters.
## Phase 04 — Data / Platform
Identity/access, PostgreSQL/Supabase plus multi-database adapters, realtime/async, integrations and storage/media.
## Phase 05 — Quality Engineering
Security, privacy/compliance, performance, testing/QA, accessibility and code quality.
## Phase 06 — Business / Growth
SEO, content/conversion, ecommerce and SaaS platform logic.
## Phase 07 — Production Engineering
Deployment, observability/SRE, Git delivery and docs, including cloud/IaC/Kubernetes guidance.
## Phase 08 — AI / Asset Production
Production AI systems and disciplined visual-asset production.
## Phase 09 — Final Control
Independent multi-review, systemic audit and final release-readiness decisions.

## Runtime evidence
`engine/runtime/contracts.json` maps machine-readable runtime contracts. `session_checkpoint.py` protects long-running task state; `engine_telemetry.py` records routing/reviewer/token evidence when available; `review_store.py` persists findings; `build_release_decision.py` binds a release decision to evidence hashes; `release_gate.py` enforces the candidate-bound decision when deployment calls it.

## Benchmarks and freshness
Structural CI validates all offline corpora. Optional live Cursor benchmarks exercise routing, context drift and reviewer calibration. Repository benchmarks clone only pinned public commits and do not execute their code. Knowledge freshness is tracked in `engine/knowledge/sources.json` and checked separately against official sources.

## Distribution
Use `python scripts/enginectl.py install <project>`, `update`, and `doctor`. Updates detect local drift, back up before forced replacement/migration and record migration history. See `docs/INSTALL.md`.

## Governance
GitHub branch-protection desired state remains in `engine/governance/github.json`. Live `main` protection is intentionally left for the final governance step and is never inferred from repository files.
