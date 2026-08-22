# Tenancy / Membership / Permissions

Model tenant identity separately from user identity. A user may belong to multiple organizations/workspaces with different roles. Resources need a single clear ownership boundary or an explicit sharing model. Every access path, including background jobs and admin tools, must preserve tenant context.

Invitation flows need target tenant, inviter authority, recipient identity rules, expiry/revocation and replay-safe acceptance. Protect last-owner/last-admin invariants and define ownership transfer/offboarding. Role names are product concepts; actual authorization should resolve to explicit permissions/capabilities where complexity warrants it.

Cross-tenant tests must include direct object access, search/list leakage, export, storage, async jobs and cached data—not only UI navigation.