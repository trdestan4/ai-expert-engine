# Finding Severity and Confidence

Severity and confidence are independent.

## Severity
- **Critical**: credible catastrophic/security/data/money/service outcome; release blocker.
- **High**: serious user/security/correctness/operational impact with meaningful likelihood or blast radius; blocker unless explicitly dispositioned.
- **Medium**: material defect/risk with bounded impact or workaround; usually must be planned before/after release based on context.
- **Low**: minor quality/maintainability/polish issue with limited operational impact.
- **Info**: observation/opportunity without demonstrated defect.

## Confidence
- **Verified**: directly reproduced, proven by code/config/runtime evidence, or deterministic contract violation.
- **Strong**: multiple consistent signals with a clear causal path; small verification gap remains.
- **Tentative**: plausible concern that needs a discriminating check before action/blocking.

## Finding contract
Every finding should include: title, affected path/behavior, severity, confidence, evidence, impact, acceptance condition, owner/specialist, and blocker status.

Do not call a tentative finding critical solely to force attention. Do not downgrade verified high impact because remediation is inconvenient.