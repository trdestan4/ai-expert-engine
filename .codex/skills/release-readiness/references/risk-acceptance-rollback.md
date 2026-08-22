# Risk Acceptance, Recovery and Abort Control

Risk acceptance is an accountable temporary release decision, not a severity rewrite or permanent waiver.

## Acceptance contract

Record:
- exact finding/candidate and unchanged severity/confidence;
- exposed users/tenants/data/money/service surface;
- why immediate remediation is not chosen;
- containment/mitigation and residual blast radius;
- accountable owner plus authority to accept;
- monitoring/detection signal;
- concrete follow-up/remediation;
- **future expiry timestamp**.

Accepted blocker risk becomes an effective blocker again after expiry. Missing/invalid/past expiry is not valid acceptance. A new candidate or expanded exposure may require re-acceptance.

Critical integrity/security/data-loss risks are normally not acceptable without extraordinary explicit authority, credible containment and recovery. Some risks should simply be NO-GO.

## Recovery classes

Keep these distinct:
- **feature disable / kill switch:** stop new exposure while code stays deployed;
- **traffic rollback:** route/canary/alias reversal;
- **application rollback:** previous artifact/version;
- **configuration rollback:** known-good flags/secrets/provider configuration;
- **dependency failover:** alternate provider/region where designed;
- **migration roll-forward:** corrective schema/data change when backward rollback is unsafe;
- **data recovery:** restore/PITR/replay/reconciliation after corruption/loss.

Application rollback cannot undo already-written incompatible or corrupted data.

## Rollback feasibility

Before claiming rollback, verify old code can operate against current schema/data/config and that provider/webhook/event formats remain compatible. For destructive migrations, recovery may be restore/roll-forward rather than `down` migration.

Estimate recovery objective where material: acceptable data-loss window (RPO), restoration/service target (RTO), ownership and required credentials/runbooks. Backup existence without restore testing is weak evidence.

## Progressive rollout

Canary/tenant cohort/percentage rollout reduces blast radius only when:
- exposure can actually be segmented;
- metrics identify the candidate/cohort;
- decision owner watches the rollout;
- stop/rollback works faster than expected harm;
- irreversible effects are separately controlled.

## Abort criteria

Define measurable trigger + action + owner. Examples:
- error/SLO burn exceeds threshold → stop rollout/rollback;
- payment/order reconciliation mismatch → disable checkout/new payments;
- auth/tenant anomaly → stop rollout and security containment;
- migration integrity count mismatch → stop migration and invoke recovery plan;
- queue age/depth/retry amplification → pause producer/scale or rollback;
- critical smoke failure → revert traffic.

Avoid “monitor closely” with no threshold or owner.
