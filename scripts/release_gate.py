#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--decision',default='.ai-expert-engine/evidence/release-decision.json');ap.add_argument('--candidate',default=os.environ.get('GITHUB_SHA'));ap.add_argument('--reviews',default='.ai-expert-engine/evidence/reviews.jsonl');ap.add_argument('--ack-conditions',action='store_true');n=ap.parse_args();p=Path(n.decision)
    if not p.exists():print('release gate: missing decision');return 2
    if subprocess.run([sys.executable,str(ROOT/'scripts/runtime_contract.py'),'release-decision',str(p),'--quiet']).returncode:return 2
    d=json.loads(p.read_text());candidate=n.candidate
    if candidate and not (candidate.startswith(d['candidate']) or d['candidate'].startswith(candidate)):print('release gate: candidate mismatch');return 3
    if d['decision'] in ('HOLD','NO-GO'):print('release gate:',d['decision']);return 4
    if d['open_blockers']!=0:print('release gate: decision declares open blockers');return 5
    rp=Path(n.reviews)
    if rp.exists() and subprocess.run([sys.executable,str(ROOT/'scripts/review_store.py'),'check-blockers','--store',str(rp),'--candidate',d['candidate']],stdout=subprocess.DEVNULL).returncode:print('release gate: unresolved persisted blocker');return 6
    from build_release_decision import evidence_hash
    try:actual=evidence_hash(d['evidence_paths'])
    except SystemExit as ex:print('release gate: evidence unavailable',ex);return 8
    if actual!=d['evidence_hash']:print('release gate: evidence hash mismatch');return 9
    ack=n.ack_conditions or os.environ.get('AI_EXPERT_RELEASE_CONDITIONS_ACK','').lower() in ('1','true','yes')
    if d['decision']=='GO WITH CONDITIONS' and d['conditions'] and not ack:print('release gate: conditions require acknowledgement');return 7
    print('release gate: PASS',d['decision'],d['candidate']);return 0
if __name__=='__main__':raise SystemExit(main())
