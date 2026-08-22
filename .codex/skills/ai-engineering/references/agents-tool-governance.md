# Agents and Tool Governance

Treat an agent as a controlled decision loop around models and tools, not as unlimited autonomy. Define the goal, permitted actions, stopping conditions, maximum steps/time/cost, approval boundaries and evidence required before side effects.

Split planning/reasoning from execution authority where risk warrants it. A model that reads untrusted web pages, documents, emails or repository content should not automatically gain privileged tools. For high-risk systems, isolate untrusted-content processing from privileged action selection and pass only structured, validated summaries or extracted facts across the boundary.

Tool catalogs should be minimal per task and user. Apply least privilege to credentials, tenant scope, resource ids and mutation types. Re-check authorization at execution time; never assume a prior tool result grants future permission.

Long-running flows need resumable state, idempotent steps, duplicate-event handling and explicit terminal states. Persist business-relevant checkpoints outside transient model context. A retry after timeout must not silently repeat charges, messages, deletes or writes.

Require approval when an action is destructive, financially meaningful, privacy-sensitive, external-facing or otherwise difficult to reverse and user intent is not already explicit. Approval is a product/policy control, not a prompt phrase.

Evaluate agents on task success, unnecessary tool calls, authorization violations, loop/step count, recovery from tool errors, prompt-injection resistance and cost/latency. Provide kill switches and degraded/manual paths for production failures.