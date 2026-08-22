from __future__ import annotations
import shutil
from pathlib import Path
def migrate(target:Path,context:dict)->dict:
    base=target/'.ai-expert-engine';(base/'state').mkdir(parents=True,exist_ok=True);(base/'evidence').mkdir(parents=True,exist_ok=True);(base/'telemetry').mkdir(parents=True,exist_ok=True)
    legacy=base/'reviews.jsonl';new=base/'evidence/reviews.jsonl'
    if legacy.exists() and not new.exists():shutil.move(str(legacy),str(new))
    return {'created':['.ai-expert-engine/state','.ai-expert-engine/evidence','.ai-expert-engine/telemetry'],'moved_legacy_reviews':new.exists()}
