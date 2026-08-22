# Incident Response, Command and Runbooks

## Incident goals

Protect users/data first, then restore service, understand cause and learn. Do not prioritize perfect diagnosis over safe mitigation when impact is ongoing.

## Roles

For material incidents establish incident commander/decision owner, operations/mitigation, communications and subject specialists as needed. One person may hold multiple roles in small teams, but decision ownership should be explicit.

## Flow

Detect/declare → assess impact/scope/security implications → stabilize/contain → mitigate/rollback/fail over → verify recovery → monitor → communicate → preserve evidence → follow-up/postmortem.

Security/data incidents may require restricted evidence handling and legal/privacy escalation; do not expose sensitive details in broad channels.

## Runbooks

A useful runbook states trigger/symptoms, dashboards/queries, safe diagnostic commands, known failure modes, mitigation options, rollback/restore steps, verification and escalation. Keep commands environment-safe and note destructive steps.

## Communication

Communicate known impact, current mitigation and next update cadence without speculation. Customer-facing claims need verified facts.

## Postmortem

Focus on contributing system conditions, detection/response and prevention—not individual blame. Actions need owner/prioritization and should address recurrence/detection/recovery. Avoid dozens of vague “be more careful” tasks.
