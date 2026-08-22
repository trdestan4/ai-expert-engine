# Evidence Sampling

Broad audits need explicit coverage limits.

## Representative sampling
Choose examples that cover:
- one or more externally exposed entry points;
- one authenticated/authorized critical journey;
- one persistence/transaction path;
- one failure/retry/async path when present;
- deployment/config/secret boundaries;
- representative tests and observability evidence.

## Confidence rules
- One file can prove a local violation, not repository-wide prevalence.
- Repeated violations across independent modules, shared abstractions, templates or policy/config can support systemic classification.
- Absence of tests/logs/docs is meaningful only where those artifacts are required by the risk/operating model.
- Search/index results are discovery aids; inspect source context before final findings.

## Stop conditions
Stop expanding a sample when additional evidence is unlikely to change severity, systemic classification, remediation order or confidence. Expand when evidence conflicts, critical impact remains uncertain, or a shared abstraction may widen blast radius.

Always state uninspected high-risk surfaces and runtime evidence that was unavailable.