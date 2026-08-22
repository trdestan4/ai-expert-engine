# Risk Acceptance and Recovery

Risk acceptance is a release control, not a severity rewrite.

## Acceptance contract
Record:
- exact unresolved risk/finding;
- severity and evidence;
- exposed users/data/service surface;
- mitigation or blast-radius limit;
- accountable owner/authority;
- reason acceptance is justified;
- monitoring/trigger to revisit;
- follow-up and expiry/date when applicable.

Critical integrity/security/data-loss risks are normally not acceptable without extraordinary, explicit authority and credible containment/recovery.

## Recovery classes
- application rollback: previous artifact/version;
- traffic rollback: alias/routing/canary exposure reversal;
- feature disable: flag/kill switch;
- configuration rollback: known-good config/secret state;
- migration roll-forward: corrective schema/data change when backward rollback is unsafe;
- data restore/recovery: backup/PITR/reconciliation when data was corrupted/lost.

Never equate application rollback with data recovery.

## Abort criteria
Define measurable signals such as error/SLO breach, payment mismatch, auth/access anomaly, migration failure, queue backlog, data integrity alarm or critical-journey smoke failure. Name the action and owner for each material trigger.