# Supabase and Row Level Security

## Exposed data model

When Supabase Data API/browser clients can reach a schema, treat Postgres grants plus RLS as part of the application's primary authorization boundary. Current Supabase guidance requires RLS on tables in exposed schemas and warns that service-role/secret keys bypass RLS and must never be exposed to clients.

RLS should be enabled before granting client-visible access. Policies should be explicit about operation (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), role, row predicate and new-row checks.

## Policy design

Separate `USING` (which existing rows are visible/targetable) from `WITH CHECK` (which new row state is allowed) where relevant. Encode tenant/resource ownership using trusted authenticated claims and database relationships; never trust a client-supplied tenant ID without policy verification.

Avoid broad `true` policies unless the data is intentionally public. Test anonymous, authenticated, privileged/server and cross-tenant paths separately.

## Roles and keys

Publishable/legacy anon keys identify the project but are safe only with correct RLS/privileges. Secret/service-role keys are backend-only. Do not initialize a privileged client in browser code or expose it through public environment variables.

## Performance

RLS predicates run as part of queries. Index columns used in policy predicates and filters, avoid unnecessary repeated expensive expressions, and inspect query plans under realistic policy/query combinations. Security correctness comes first, but poorly designed policies can become a production bottleneck.

## Functions/views

Review `SECURITY DEFINER`, function `search_path`, exposed views/functions and bypass-RLS roles carefully. A helper function that runs with elevated privileges can silently defeat otherwise-correct policies.

## Testing

Test direct Data API/client access, not only application UI. Include cross-user/cross-tenant reads and writes, inserts with forged ownership, updates that attempt to move rows between tenants, delete restrictions, and privileged server paths.