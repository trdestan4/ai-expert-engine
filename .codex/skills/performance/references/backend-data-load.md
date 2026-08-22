# Backend, Data and Load Performance

Measure latency as distributions and decompose service time across network, application logic, external providers, serialization, database and queueing. Average latency can hide severe tail behavior; use percentiles appropriate to the user/SLO.

Look for N+1 access, repeated remote calls, oversized payloads, unbounded scans, lock contention, pool exhaustion, synchronous work that should be deferred, inefficient serialization and expensive logging.

Load tests should represent realistic concurrency, data volume, hot/cold cache, request mix and rate changes. Observe throughput, p95/p99 latency, error rate, CPU/memory, connection pools, database saturation and queue depth. A test that overwhelms a dependency unrealistically may measure the test harness rather than the product.

Capacity changes require correctness under concurrency. Do not add retries blindly: they can amplify overload. Pair timeouts, retry budgets, backoff and circuit/queue behavior with idempotency where needed.

Coordinate query/index/transaction changes with `database-data`; performance owns the measured target and verification.