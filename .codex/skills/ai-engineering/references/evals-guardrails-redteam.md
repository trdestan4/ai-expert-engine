# Evals, Guardrails and Red-Team Testing

Treat evaluation as the acceptance test layer for probabilistic behavior. Build a representative dataset from real product intents, difficult edge cases, known regressions, adversarial inputs and failure conditions. Version the cases and expected scoring policy so prompt/model/retrieval changes can be compared rather than judged by vibes.

Use deterministic checks whenever possible: schema validity, exact tool/action selection, authorization outcome, citation existence, forbidden data leakage, latency/cost ceilings and known factual constraints. Use model-based judges only for genuinely semantic criteria and calibrate them against human-reviewed examples.

Separate offline regression evals from online production signals. Offline evals protect known behavior before release; online monitoring catches distribution shift, provider/model drift, tool failures and newly observed unsafe patterns.

Prompt injection requires defense in depth. Test direct and indirect injection through user text, web/RAG documents, emails, code comments, metadata and tool outputs. Guardrails are not a replacement for least privilege, authz, action validation or human approval on high-impact actions.

Red-team tests should include data exfiltration attempts, system-prompt extraction, instruction override, tool misuse, encoded/obfuscated attacks, cross-tenant retrieval, unsafe markdown/HTML rendering and excessive-loop/cost behavior.

A model-based input/output/action guard can be useful as one layer, but it is itself probabilistic and attackable. Log decisions, measure false accepts/rejects, use a different attack surface when practical and reserve expensive guardrails for risk-bearing paths.

Block release when critical eval cases regress without an explicit risk decision. Preserve eval evidence with model/provider/prompt/retrieval versions so later changes are diagnosable.