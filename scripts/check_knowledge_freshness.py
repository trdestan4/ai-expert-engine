#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,urllib.request
from datetime import date,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/'engine/knowledge/sources.json'
REQUIRED_OWNERS={'master-agent','react-nextjs','frontend-engineering','database-data','identity-access','security','accessibility','performance','api-engineering','ai-engineering','observability-sre','seo','integrations','ecommerce','saas-platform','devops-deployment','git-delivery'}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--online',action='store_true');ap.add_argument('--fail-stale',action='store_true');n=ap.parse_args();d=json.loads(SRC.read_text());today=date.today();errors=[];warnings=[];owners=set()
    for x in d['sources']:
        owners.update(x.get('owners',[]));age=(today-datetime.strptime(x['last_verified'],'%Y-%m-%d').date()).days;maxage=x['max_age_days']
        if age>maxage:
            msg=f"{x['id']} stale {age}d>{maxage}d";(errors if n.fail_stale and x.get('critical') else warnings).append(msg)
        if n.online:
            try:
                req=urllib.request.Request(x['url'],headers={'User-Agent':'ai-expert-engine-freshness/1.3'});body=urllib.request.urlopen(req,timeout=20).read(1000000).decode('utf-8','ignore').lower()
                for marker in x.get('assertions',[]):
                    if marker.lower() not in body:errors.append(f"{x['id']} assertion not found: {marker}")
            except Exception as ex:errors.append(f"{x['id']} online check failed: {ex}")
    missing=sorted(REQUIRED_OWNERS-owners)
    if d.get('policy',{}).get('require_owner_coverage') and missing:errors.append('knowledge-source owner coverage missing: '+','.join(missing))
    [print('WARN',w) for w in warnings];[print('ERROR',e) for e in errors];print(f"freshness checked: {len(d['sources'])} sources / {len(owners)} covered owners")
    return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
