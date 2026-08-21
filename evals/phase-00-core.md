# Phase 00 Core Evals

These evals test routing quality, decision discipline, and token behavior. A future automated runner may convert them to machine fixtures; until then they are normative acceptance cases.

## Routing cases

### C01 — Tiny known edit
Prompt: “Change the button label from Save to Continue in the known component.”
Expected: no formal planning; future UI/frontend owner only. `master-agent`, `repository-intelligence`, and `debugging` should not expand the task.
Failure: loading multiple core skills for a deterministic cosmetic edit.

### C02 — Existing repo feature
Prompt: “Add team invitations to this unfamiliar Next.js/Supabase repository.”
Expected: `master-agent` → targeted `repository-intelligence` → `task-planning` → future auth/database/frontend specialists.
Failure: planning against assumed stack conventions before repository evidence.

### C03 — Unknown login regression
Prompt: “Login succeeds but after refresh the user appears logged out.”
Expected: `debugging` as diagnostic owner; targeted repository evidence for session/middleware flow as needed. Do not jump directly to cookie rewrites.
Failure: speculative patch before reproduction/evidence.

### C04 — Proven bug
Prompt: “The failing test proves `parsePrice` rejects comma decimals because regex X excludes comma. Fix it.”
Expected: domain implementation; `debugging` need not repeat root-cause analysis.
Failure: re-running an elaborate diagnosis with cause already established.

### C05 — High-risk small diff
Prompt: “Change this RLS policy so support users can read customer orders.”
Expected: elevated risk despite small change; future database/security review required.
Failure: classifying by diff size and skipping security/data gate.

### C06 — Repository-only question
Prompt: “Which package owns API routes and where is auth enforced in this monorepo?”
Expected: `repository-intelligence` only.
Failure: activating task planning or implementation skills.

### C07 — Architecture trade-off
Prompt: “For this existing app, should jobs stay in-process or move to a queue?”
Expected: verify relevant repository/operational facts, then `task-planning` decision framework plus future architecture specialist.
Failure: choose newest technology without constraints/evidence.

### C08 — Failed attempted fix
Prompt: “We changed SameSite twice and the production logout bug still happens.”
Expected: `debugging` + failure-recovery; preserve what prior attempts disproved and compare production/local evidence.
Failure: stack another speculative cookie change.

## Quality assertions

For every non-trivial core flow:

- ownership is explicit;
- adjacent skill exclusions are respected;
- repository claims distinguish verified/inferred/unknown;
- debugging separates root cause, trigger, contributing factor, symptom;
- planning contains observable acceptance criteria and verification;
- elevated-risk work has escalation;
- completion is never claimed from confidence alone.

## Token assertions

- C01 should use no more than one discoverable specialist beyond global rules.
- C03 should not load broad architecture/planning references unless diagnosis proves they are needed.
- C06 should stop repository discovery when the asked ownership/enforcement facts are established.
- References are loaded individually, not directory-wide.

## Phase 00 acceptance target

Pass all routing cases conceptually with no ownership conflict and no unnecessary skill activation. Automated scoring will be added when the eval runner phase is implemented.
