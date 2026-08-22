# WebSocket, SSE and Realtime

## Transport choice

Use SSE for primarily server-to-client event streams that benefit from HTTP semantics, automatic reconnection patterns, simple proxies and text/event framing. Use WebSockets when bidirectional low-latency messaging or client-driven realtime commands are core requirements.

Do not choose a realtime transport because it looks modern. Polling with conditional requests may be simpler and more reliable for low-frequency updates.

## Connection lifecycle

Define authentication at connect time and re-authorization when credentials/permissions change. Long-lived connections must handle token/session expiry, revocation, heartbeat/liveness, idle timeouts, network handoff and server restarts.

## Reconnect and recovery

A live connection is not durable history. Give clients a resume cursor/last-event identifier or force a refetch from authoritative state after reconnect. Handle duplicate replay after resume.

## Subscription scope

Authorize each channel/topic/resource, not only the initial socket. Tenant and resource identifiers from clients are untrusted. Unsubscribe when membership/permissions change where the platform supports it.

## Backpressure

Bound server/client buffers and per-connection send rates. Slow consumers should not cause unbounded memory growth. Decide whether to drop/coalesce ephemeral updates or disconnect slow clients.

## Presence and ephemeral state

Presence/typing indicators are usually best-effort and ephemeral. Do not confuse them with durable business records. Define expiry/heartbeat cleanup.

## Tests

Test reconnect after missed events, duplicate replay, permission revocation, token expiry, server restart, slow client, burst traffic, multi-tab/device behavior and cross-tenant subscription attempts.