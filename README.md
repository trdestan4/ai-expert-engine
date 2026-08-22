# AI Expert Engine v1.3

A token-efficient master expert-engine architecture for production web design, software engineering, AI systems, asset production and release control in Cursor and Codex.

**Engine status: v1.3 master-hardened — 43 discoverable skills + 6 isolated Cursor reviewer subagents. No new discoverable skill was added in v1.3.**

## v1.3 master hardening
- release decisions are bound to exact candidate, target environment, evidence hash and expiry;
- expired accepted risks become effective blockers again instead of silently remaining accepted forever;
- Cursor production-shell enforcement covers a wider set of deploy/destructive CLIs and passes the target environment into the gate;
- runtime schema validation supports local refs, conditional schemas, const, composition keywords and date-time formats used by engine contracts;
- semantic validation now scans routing, SKILL bodies, policies, reviewer contracts and AGENTS for stale ownership language;
- repository profiling exposes truncation instead of silently treating partial large-monorepo scans as complete;
- stack resolution composes solution, application, data, infrastructure and experience profiles instead of forcing unrelated axes into one winner;
- knowledge freshness tracks 30+ official standards/framework/provider sources with owner coverage and multi-marker online assertions;
- reviewer agents load their owning expert skill and deep references before independent review;
- creative/product, quality, business and production references are deepened into master playbooks while the discoverable skill count remains bounded;
- reviewer calibration, behavioral evals and real repository benchmarks are expanded with ambiguous/adversarial cases.

Normal Cursor use requires no Cursor API key. API access is optional only for automated live model benchmarks.

## Architecture principle
The engine keeps a bounded discoverable skill set and loads deep references, composable stack profiles, reviewer agents and deterministic tools only when needed. Complexity C0–C4 and risk R0–R4 remain separate; high-risk work escalates evidence and independent review without loading every skill.

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
Web-platform, frontend, React/Next.js and software architecture with i18n/RTL and non-React framework adapters.
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
Independent multi-review, systemic audit and candidate/environment-bound release-readiness decisions.

## Runtime evidence
`engine/runtime/contracts.json` maps machine-readable runtime contracts. `session_checkpoint.py` protects long-running task state; `engine_telemetry.py` records routing/reviewer/token evidence when available; `review_store.py` persists findings and reactivates expired accepted blockers; `build_release_decision.py` binds a release decision to evidence hashes and expiry; `release_gate.py` enforces candidate + environment + freshness when deployment calls it.

## Stack intelligence
`profile_repository.py` records whether repository discovery was truncated. `resolve_stack_profile.py` returns backward-compatible `selected` plus `selected_profiles`, `selected_by_dimension` and merged owners/defaults so SaaS/ecommerce, framework, database, infrastructure and experience context can coexist.

## Benchmarks and freshness
Structural CI validates all offline corpora. Optional live Cursor benchmarks exercise routing, context drift and reviewer calibration. Repository benchmarks clone only pinned public commits and do not execute their code. Knowledge freshness is tracked in `engine/knowledge/sources.json` and checked against official sources.

## Distribution
Use `python scripts/enginectl.py install <project>`, `update`, and `doctor`. Updates detect local drift, back up before forced replacement/migration and record migration history. v1.2→v1.3 invalidates old release-decision artifacts because they lack the new environment/expiry contract. See `docs/INSTALL.md`.

## Governance
GitHub branch-protection desired state remains in `engine/governance/github.json`. Live `main` protection is intentionally left for the final governance step and is never inferred from repository files.
