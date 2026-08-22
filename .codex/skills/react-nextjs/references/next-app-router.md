# Next.js App Router and Server Boundaries

Always inspect the installed Next.js version before applying version-sensitive conventions.

## Router mode

Determine whether the target code uses App Router (`app/` or `src/app/`), Pages Router, or both. Preserve local migration strategy. Do not rewrite Pages Router code into App Router as incidental cleanup.

## Server and Client Components

In App Router, prefer Server Components for server data/content with no browser interactivity. Add `'use client'` only at the smallest component boundary that needs hooks, browser APIs, client libraries, or events.

Props crossing server → client must be serializable under the framework's supported transfer semantics. Keep the payload narrow.

Do not call your own HTTP Route Handler from a Server Component just to access same-application server logic; call the underlying server/data function when architecture permits.

## Server Actions

Use Server Actions for UI-originated mutations when they fit the application's contract and installed version. Treat them as exposed server entry points:

- authenticate;
- authorize;
- validate input;
- handle expected domain failures;
- avoid leaking internal errors;
- revalidate/update affected data intentionally.

Never assume action input is trustworthy because the form/button came from your UI.

## Route Handlers

Use Route Handlers when an actual HTTP surface is needed: external consumers, webhooks, public/internal APIs, non-React clients, explicit method/status/header behavior, or streaming/file responses.

Keep business logic outside the handler when it should be reusable/testable independently.

## File conventions and request APIs

Use the installed version's conventions for page/layout/loading/error/not-found/default/route/proxy-or-middleware files. Recent Next versions changed several request APIs and the middleware/proxy naming model; inspect installed types/docs before editing.

Treat `params`, `searchParams`, `cookies()`, `headers()`, draft/request APIs, and route config as version-sensitive across recent releases.

## Error/control flow

Use framework redirect/notFound/error mechanisms intentionally. Avoid broad catch blocks that swallow framework control-flow exceptions. Design local `error` boundaries around recoverable route segments and reserve global error handling for truly global failures.

## Runtime

Default to the project's normal Node/runtime unless Edge-specific constraints/benefits are required and dependency compatibility is verified. Do not select Edge because it sounds faster.

## Metadata

Use framework metadata/file conventions for title/description/canonical/social images where appropriate. Dynamic metadata must avoid unnecessary duplicate data waterfalls.

## Verification

For route changes test direct URL load, client navigation, reload, back/forward, authenticated/unauthenticated paths where relevant, not-found/error behavior, and production build output.
