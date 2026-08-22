#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def evidence_hash(paths):
    h=hashlib.sha256()
    for raw in sorted(dict.fromkeys(paths)):
        p=Path(raw);h.update(raw.encode());h.update(b'\0')
        if p.is_file():h.update(p.read_bytes())
        elif p.is_dir():
            for f in sorted(x for x in p.rglob('*') if x.is_file()):
                h.update(f.relative_to(p).as_posix().encode());h.update(b'\0');h.update(f.read_bytes())
        else:raise SystemExit(f'missing evidence path: {raw}')
    return h.hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--candidate',required=True);ap.add_argument('--environment',required=True);ap.add_argument('--risk',required=True,choices=['R0','R1','R2','R3','R4']);ap.add_argument('--decision',required=True,choices=['GO','GO WITH CONDITIONS','HOLD','NO-GO']);ap.add_argument('--evidence',action='append',required=True);ap.add_argument('--reviews',default='.ai-expert-engine/evidence/reviews.jsonl');ap.add_argument('--condition',action='append');ap.add_argument('--output',default='.ai-expert-engine/evidence/release-decision.json');n=ap.parse_args();paths=list(dict.fromkeys(n.evidence));reviews=Path(n.reviews);openb=0
    if reviews.exists():
        for line in reviews.read_text().splitlines():
            if not line.strip():continue
            r=json.loads(line)
            if r.get('candidate')==n.candidate and r.get('blocker') and r.get('status')=='open':openb+=1
    d={'candidate':n.candidate,'environment':n.environment,'risk':n.risk,'decision':n.decision,'evidence_paths':paths,'evidence_hash':evidence_hash(paths),'review_store':str(reviews) if reviews.exists() else None,'open_blockers':openb,'conditions':n.condition or[],'generated_at':datetime.now(timezone.utc).isoformat(),'expires_at':None};p=Path(n.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2)+'\n')
    rc=subprocess.run([sys.executable,str(ROOT/'scripts/runtime_contract.py'),'release-decision',str(p)]).returncode
    if openb and n.decision.startswith('GO'):print('warning: GO decision contains persisted blockers; release gate will reject')
    return rc
if __name__=='__main__':raise SystemExit(main())
