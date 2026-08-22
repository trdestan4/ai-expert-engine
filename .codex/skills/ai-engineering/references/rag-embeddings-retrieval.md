# RAG, Embeddings and Retrieval

Start with the retrieval question before choosing a vector database. Define what knowledge must be grounded, who owns it, freshness/retention rules, tenant/security boundaries and what the system should do when evidence is absent or conflicting.

Chunk by semantic/document structure where possible rather than arbitrary fixed slices alone. Preserve source ids, section/page anchors, timestamps/version, permissions and document type so retrieval can be filtered and cited. Evaluate chunk size/overlap against real questions instead of copying defaults.

Choose embeddings and indexing from corpus language/modality, update frequency, scale, latency and evaluation quality. Model migrations can invalidate similarity assumptions; version embeddings/indexes and plan reindexing rather than mixing incompatible vectors silently.

Retrieval should combine appropriate filters, lexical/semantic search and reranking when evaluation demonstrates value. Retrieve fewer higher-quality passages rather than filling the context window. Enforce tenant/user permissions before content enters model context.

Retrieved text is untrusted data. Documents/web content can contain indirect prompt injection; delimit/source-tag content, keep tool/system policy outside retrieved instructions and prevent retrieved text from escalating permissions.

Grounded answers should preserve provenance and uncertainty. If evidence is insufficient, return no-answer/clarification rather than fabricate. Track retrieval hit quality, citation/source correctness, freshness, latency and downstream answer quality in evals.