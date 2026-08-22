# AI Expert Engine v1.1

A token-efficient expert-engine architecture for production web design, software engineering, AI systems, asset production and release control in Cursor and Codex.

**Engine status: v1.1 hardened — 43 discoverable skills + 6 isolated Cursor reviewer subagents. No new skills were added in v1.1.**

## v1.1 runtime hardening

The v1.1 hardening pass closes the main runtime gaps discovered after the v1.0 manual audit:
- executable behavioral evals run the real Cursor local agent against a machine-readable corpus;
- six reviewer lenses have project subagent definitions under `.cursor/agents/` so mandatory Cursor reviews use separate context windows;
- semantic routing validation rejects stale “future skill” language for skills already present;
- nine stack profiles provide deterministic project signals before model routing;
- deterministic repository profiling, stack resolution, routing reports and governance checks reduce model-only judgment;
- `enginectl.py` installs, updates and verifies managed engine copies without silently overwriting an existing project;
- GitHub desired governance is machine-readable and has check/apply tooling. Live protection must still be verified against GitHub rather than inferred from repository files.

Install/update instructions are in `docs/INSTALL.md`. Governance instructions are in `docs/GOVERNANCE.md`.

## Architecture principle
The engine uses a bounded set of discoverable domain skills with deep expertise loaded lazily from references, policies, schemas, evals, stack profiles, isolated reviewer agents and deterministic tools. Normal tasks load only the minimum owners needed; high-risk work escalates independent review and release gates.

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
Orchestration, repository intelligence, task planning, debugging, token policy, schemas, routing contracts, evals and structural validation. Complexity C0–C4 and risk R0–R4 are classified independently.

## Phase 01 — Creative / Product Intelligence
Product strategy, creative direction, brand design, anti-generic review, color, typography, visual art direction, motion and UX/UI. The system rejects shortcut mappings such as `premium = navy + gold` and requires project-specific rationale.

## Phase 02 — Web Engineering / Frontend
Framework-independent web-platform reasoning, production frontend engineering, React/Next.js runtime expertise and application architecture. Installed framework versions outrank remembered behavior.

## Phase 03 — Backend / API Engineering
Backend service/runtime design plus REST/GraphQL contracts, OpenAPI, validation, errors, pagination, versioning, idempotency, rate limits and compatibility. Data, identity, async and security work is routed to their active owners rather than absorbed here.

## Phase 04 — Data / Platform
Identity/access, PostgreSQL/Supabase data engineering, realtime/durable async, external integrations and secure object/media storage. Cross-tenant access, privileged keys, duplicate side effects, unverified webhooks and unsafe migrations are high-risk boundaries.

## Phase 05 — Quality Engineering
Security, privacy/compliance, performance, testing/QA, accessibility and code-quality gates. Quality skills are activated by actual risk rather than as a permanent bundle.

## Phase 06 — Business / Growth
SEO/search discoverability, conversion messaging, ecommerce state and SaaS tenancy/entitlement/business logic. Dark patterns and client-authoritative pricing/entitlements are rejected.

## Phase 07 — Production Engineering
CI/CD, deployment, observability/SRE, Git delivery and durable documentation. Green CI is evidence, not proof of production readiness.

## Phase 08 — AI / Asset Production
Production AI engineering plus disciplined visual-asset production. AI outputs cannot authorize privileged actions; retrieved content remains untrusted data; asset generation follows approved creative direction and provenance rules.

## Phase 09 — Final Control
`multi-review` coordinates independent reviewer contexts, `audit-review` performs systemic risk audits, and `release-readiness` is the final production decision owner returning GO, GO WITH CONDITIONS, HOLD or NO-GO.

## Runtime validation
Structural CI runs every `scripts/validate_*.py` validator. `scripts/validate_engine.py` checks cross-phase integrity; `scripts/validate_semantics.py` checks stale/unknown routing references; `scripts/validate_hardening.py` checks reviewer/profile/eval/tool invariants.

Behavioral correctness is evaluated separately with `scripts/run_behavioral_evals.py`. These live evals require a Cursor API key and are not represented as passed unless they actually run.

## Distribution
Use `python scripts/enginectl.py install <project>` to install a managed copy and `python scripts/enginectl.py update <project>` to update it. `doctor` detects missing or modified managed files. Existing unmanaged engine paths require an explicit `--force` backup before replacement.

## Governance
`engine/governance/github.json` defines required `main` protection. `scripts/check_github_governance.py` checks live GitHub state and `scripts/apply_github_governance.py` applies it with an Administration-write token. Repository files alone never prove that branch protection is active.
