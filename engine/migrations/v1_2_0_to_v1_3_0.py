from __future__ import annotations
from pathlib import Path

def migrate(target:Path,context:dict):
    evidence=target/'.ai-expert-engine/evidence';evidence.mkdir(parents=True,exist_ok=True);decision=evidence/'release-decision.json';archived=None
    if decision.exists():
        archived=evidence/'release-decision.v1.2-invalidated.json';archived.unlink(missing_ok=True);decision.replace(archived)
    return {'release_decision_invalidated':bool(archived),'archived_to':str(archived) if archived else None,'reason':'v1.3 requires target-environment and expiry-bound release evidence'}
