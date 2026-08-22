# SaaS Onboarding, Administration and Product Analytics

## Onboarding

Optimize time-to-first-value, not checklist completion. Identify the smallest meaningful activation event and prerequisites. Use progressive setup; do not force optional profile/configuration before value unless operational/security needs require it.

Handle invited users, returning partially configured users, empty data, sample/demo data and multi-user handoff. Enterprise onboarding may include SSO/SCIM/security review/domain verification and should not be disguised as the same self-serve flow.

## Admin surfaces

Admin/operator tools can have more privilege than customer UI. Require explicit authorization, search/filter context, safe bulk actions, confirmation/recovery, audit and customer/tenant identification to prevent wrong-tenant operations. Avoid hidden “superadmin bypass” without control/logging.

## Product analytics

Define activation, adoption, retention, expansion and churn metrics from product jobs. Event semantics need stable actor/tenant/object IDs and source. Segment by plan/tenant size/cohort where useful without leaking tenant data.

Do not confuse logins/pageviews with value. Track successful outcomes and failure reasons. For experiments, use tenant vs user randomization based on collaboration effects and avoid mixing enterprise contract behavior into self-serve metrics.

## Support/operations feedback

Connect support reasons, onboarding failures, entitlement confusion and admin intervention to product decisions. Instrument “stuck” states and reconciliation jobs, not just happy-path funnels.
