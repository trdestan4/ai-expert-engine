# Privacy Data Map and Minimization

Inventory personal-data categories by source, subject, purpose, sensitivity, storage, processors, regions and recipients. Trace data through primary databases, logs, analytics, search indexes, caches, object storage, exports, queues, backups and vector/embedding stores.

For each data item ask: is it required, can it be less precise, can it be pseudonymous, can it be processed locally/ephemerally, who needs access, and when should it disappear? Avoid personal data in URLs, cache keys, exception messages and telemetry unless there is a documented purpose and protection.

Derived identifiers and event histories can still be personal data when linkable to a person. Hashing is not automatically anonymization.

Document controller/processor boundaries and data sent to third-party SDKs. Prefer privacy-preserving defaults and collect optional analytics/marketing data only under the applicable product/legal control.

A privacy map is incomplete if deletion/retention cannot identify all meaningful replicas and downstream processors.