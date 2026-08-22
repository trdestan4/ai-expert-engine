#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def dt(raw):
    try:return datetime.fromisoformat(str(raw).replace('Z','+00:00')).astimezone(timezone.utc)
    except Exception:return None
def norm_env(x):return str(x or '').strip().lower()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--decision',default='.ai-expert-engine/evidence/release-decision.json');ap.add_argument('--candidate',default=os.environ.get('GITHUB_SHA'));ap.add_argument('--environment',default=os.environ.get('AI_EXPERT_RELEASE_ENVIRONMENT'));ap.add_argument('--reviews',default='.ai-expert-engine/evidence/reviews.jsonl');ap.add_argument('--ack-conditions',action='store_true');n=ap.parse_args();p=Path(n.decision)
    if not p.exists():print('release gate: missing decision');return 2
    if subprocess.run([sys.executable,str(ROOT/'scripts/runtime_contract.py'),'release-decision',str(p),'--quiet']).returncode:return 2
    d=json.loads(p.read_text());candidate=str(n.candidate or '')
    if not candidate:print('release gate: candidate is required');return 3
    if candidate!=d['candidate']:print('release gate: candidate mismatch');return 3
    target=norm_env(n.environment)
    if not target:print('release gate: target environment is required');return 10
    if target!=norm_env(d['environment']):print(f"release gate: environment mismatch decision={d['environment']} target={target}");return 10
    exp=dt(d.get('expires_at'))
    if exp is None or exp<=datetime.now(timezone.utc):print('release gate: release decision expired or has invalid expiry');return 11
    if d['decision'] in ('HOLD','NO-GO'):print('release gate:',d['decision']);return 4
    if d['open_blockers']!=0:print('release gate: decision declares effective blockers');return 5
    rp=Path(n.reviews)
    declared=d.get('review_store')
    if declared and Path(declared).as_posix()!=rp.as_posix():print('release gate: review store mismatch');return 12
    if rp.exists() and subprocess.run([sys.executable,str(ROOT/'scripts/review_store.py'),'check-blockers','--store',str(rp),'--candidate',d['candidate']],stdout=subprocess.DEVNULL).returncode:print('release gate: unresolved or expired accepted blocker');return 6
    from build_release_decision import evidence_hash
    try:actual=evidence_hash(d['evidence_paths'])
    except SystemExit as ex:print('release gate: evidence unavailable',ex);return 8
    if actual!=d['evidence_hash']:print('release gate: evidence hash mismatch');return 9
    ack=n.ack_conditions or os.environ.get('AI_EXPERT_RELEASE_CONDITIONS_ACK','').lower() in ('1','true','yes')
    if d['decision']=='GO WITH CONDITIONS' and d['conditions'] and not ack:print('release gate: conditions require acknowledgement');return 7
    print('release gate: PASS',d['decision'],d['candidate'],target);return 0
if __name__=='__main__':raise SystemExit(main())
