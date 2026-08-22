#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess,sys
from datetime import datetime,timedelta,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def evidence_hash(paths):
    h=hashlib.sha256()
    for raw in sorted(dict.fromkeys(paths)):
        p=Path(raw);h.update(raw.encode());h.update(b'\0')
        if p.is_file():h.update(p.read_bytes())
        elif p.is_dir():
            for f in sorted(x for x in p.rglob('*') if x.is_file()):h.update(f.relative_to(p).as_posix().encode());h.update(b'\0');h.update(f.read_bytes())
        else:raise SystemExit(f'missing evidence path: {raw}')
    return h.hexdigest()
def parse_dt(raw):
    try:return datetime.fromisoformat(str(raw).replace('Z','+00:00')).astimezone(timezone.utc)
    except Exception:raise SystemExit('invalid ISO-8601 timestamp: '+str(raw))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--candidate',required=True);ap.add_argument('--environment',required=True);ap.add_argument('--risk',required=True,choices=['R0','R1','R2','R3','R4']);ap.add_argument('--decision',required=True,choices=['GO','GO WITH CONDITIONS','HOLD','NO-GO']);ap.add_argument('--evidence',action='append',required=True);ap.add_argument('--reviews',default='.ai-expert-engine/evidence/reviews.jsonl');ap.add_argument('--condition',action='append');ap.add_argument('--ttl-hours',type=float);ap.add_argument('--expires-at');ap.add_argument('--output',default='.ai-expert-engine/evidence/release-decision.json');n=ap.parse_args();paths=list(dict.fromkeys(n.evidence));reviews=Path(n.reviews);now=datetime.now(timezone.utc);openb=0
    if n.expires_at and n.ttl_hours is not None:raise SystemExit('use only one of --expires-at or --ttl-hours')
    ttl=n.ttl_hours if n.ttl_hours is not None else (24 if n.risk in ('R3','R4') or n.environment.lower()=='production' else 72)
    expiry=parse_dt(n.expires_at) if n.expires_at else now+timedelta(hours=ttl)
    if expiry<=now:raise SystemExit('release decision expiry must be in the future')
    if reviews.exists():
        from review_store import effective_blockers,load
        openb=len(effective_blockers(load(reviews),n.candidate))
    d={'candidate':n.candidate,'environment':n.environment.strip().lower(),'risk':n.risk,'decision':n.decision,'evidence_paths':paths,'evidence_hash':evidence_hash(paths),'review_store':str(reviews) if reviews.exists() else None,'open_blockers':openb,'conditions':n.condition or[],'generated_at':now.isoformat(),'expires_at':expiry.isoformat()};p=Path(n.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2)+'\n')
    rc=subprocess.run([sys.executable,str(ROOT/'scripts/runtime_contract.py'),'release-decision',str(p)]).returncode
    if openb and n.decision.startswith('GO'):print('warning: GO decision contains effective blockers; release gate will reject')
    return rc
if __name__=='__main__':raise SystemExit(main())
