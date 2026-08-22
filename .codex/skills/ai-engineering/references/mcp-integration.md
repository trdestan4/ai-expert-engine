# MCP Integration

Treat Model Context Protocol as a versioned application protocol, not a timeless tool-call wrapper. Verify the client/server SDK and specification revision supported by the project before implementing transports, discovery, authorization or extension behavior.

As of the current 2026-07-28 MCP specification, the core protocol is stateless and supports routable request metadata, cacheable list results, authorization hardening and an extensions framework. Do not copy older assumptions about mandatory initialize handshakes, sticky protocol sessions or long-lived bidirectional transport into a project that targets the newer specification. Likewise, do not force a newer protocol onto clients that have not migrated.

Design MCP servers around narrow capabilities and least privilege. Tool/resource exposure should reflect authenticated caller scope, tenant and environment. Validate tool inputs and authorize resource access server-side just as with any API.

Remote servers require explicit authentication/authorization, origin/network controls where applicable, rate limits, auditability and secret isolation. Never treat MCP discovery metadata as permission to execute every advertised capability.

Clients should cache/discover capabilities only according to the supported spec/SDK semantics and handle capability/version mismatch explicitly. Names/descriptions are routing metadata, not security controls.

Test malformed requests, unsupported methods/extensions, authorization failures, duplicate/retried mutations, schema evolution and client/server version mismatch. Keep MCP-specific protocol logic separate from business/domain services so protocol upgrades do not rewrite core application behavior.