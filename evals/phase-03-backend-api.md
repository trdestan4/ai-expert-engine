# Phase 03 Evals — Backend / API

## Routing positives

1. "Node servisinde sipariş oluşturma business logic'ini ve hata yönetimini düzenle." → `backend-engineering`.
2. "FastAPI endpoint'inde validation doğru ama service katmanı karışık." → `backend-engineering`.
3. "REST API için cursor pagination ve filtreleme sözleşmesi tasarla." → `api-engineering`.
4. "OpenAPI dokümanı runtime ile uyuşmuyor." → `api-engineering`.
5. "GraphQL schema'da N+1 ve breaking change riski var." → `api-engineering`, implementation gerekiyorsa `backend-engineering`.
6. "Aynı ödeme isteği iki kez gelirse duplicate oluşmasın." → `api-engineering` + `backend-engineering`, database/security review gerektiğinde sonraki specialist.

## Routing negatives

1. "Button mobilde taşıyor." → Phase 02 frontend, Phase 03 tetiklenmemeli.
2. "PostgreSQL index ekle." → future `database-data`, backend/API tetiklenmemeli.
3. "Google login ve rol sistemi tasarla." → future `identity-access`, API ancak contract değişiyorsa destek olur.
4. "CORS yüzünden browser request bloklanıyor." → `web-platform` / `debugging`, backend/API yalnız kök neden gerçekten server contract/config ise eklenir.
5. "WebSocket fan-out ve queue retry topology tasarla." → future `realtime-async`.

## Edge cases

- Existing API OAS 3.1 tooling kullanıyor ama latest spec 3.2.0 → körlemesine upgrade etme; tooling compatibility kontrol et.
- Retry edilen POST duplicate side effect yaratabilir → idempotency semantics zorunlu.
- GraphQL latest working draft özelliği server tooling'de yok → stable/supported feature set kullan.
- Offset pagination büyük ve sürekli değişen dataset'te skip/duplicate üretiyor → cursor/keyset değerlendir.
- Validation error detail insan-okunur ama client detail text parse ediyor → stable machine-readable error contract üret.
- Fire-and-forget email request sonunda process ölünce kayboluyor → durable async layer'a route et.

## Quality assertions

- Runtime/framework version-sensitive advice repository evidence ile doğrulanmalı.
- API contract persistence modelinin doğrudan dışa açılmış kopyası olmamalı.
- Unbounded collection pagination olmadan kabul edilmemeli.
- Retry/duplicate behavior side-effecting operations için açıklanmalı.
- Public errors secret/stack/SQL/internal topology sızdırmamalı.
- RFC 9457 kullanılıyorsa machine-readable fields contract olarak tanımlanmalı; client human detail parse etmemeli.
- REST/GraphQL/OpenAPI deep references yalnız ilgili style/tooling için yüklenmeli.
- Backend test planı success + important failure/retry/concurrency paths içermeli.
- Breaking API changes migration/deprecation stratejisi olmadan release-ready sayılmamalı.