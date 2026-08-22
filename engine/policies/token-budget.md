# Context & Token Budget Policy

The engine optimizes for decision quality per token, not minimum tokens at any cost.

## Loading policy

1. Start with global rules and skill metadata only.
2. Load one primary skill for the current decision.
3. Load a second/third skill only when ownership crosses domains or risk requires independent expertise.
4. Load individual references on demand; never preload an entire reference directory.
5. Prefer summaries/profiles over repeatedly re-reading the same repository surface.
6. Use deterministic scripts for mechanical inspection when cheaper and more reliable than model reasoning.

## Default budgets

- trivial edit: 1 active specialist; no planning skill unless risk is elevated;
- normal feature: 1–3 specialists;
- cross-layer feature: 2–4 specialists;
- high-risk architecture/security/data work: 3–5 specialists plus required review;
- release audit: may exceed normal limits because independent review is the task.

## Escalation triggers

Additional context is justified when any of these is true:

- a decision depends on unknown repository facts;
- there are multiple plausible root causes;
- a public API/schema/auth/permission boundary changes;
- data loss, security, financial, privacy, or production risk exists;
- verification failed and the current hypothesis no longer explains evidence;
- an independent reviewer is required by risk policy.

## Compression rules

- Retain decisions, constraints, file paths, interfaces, failing evidence, and acceptance criteria.
- Drop exploratory dead ends once disproven, except when needed to prevent repetition.
- Summarize large repository discoveries into a structured repository profile.
- Do not copy long source files into planning/reference notes; point to exact paths/symbols.

## Anti-patterns

- Loading every potentially relevant skill “just in case”.
- Re-reading unchanged repository areas on each step.
- Keeping full logs after the decisive lines are identified.
- Using multiple review agents for low-risk cosmetic edits.
- Duplicating domain knowledge inside the master agent.

## Quality override

Token budget never authorizes skipping evidence or a mandatory safety/quality gate. When quality requires more context, spend it deliberately and record why.
