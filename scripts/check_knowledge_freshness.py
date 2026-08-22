#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,urllib.request
from datetime import date,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/"engine/knowledge/sources.json"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--online",action="store_true");ap.add_argument("--fail-stale",action="store_true");n=ap.parse_args();d=json.loads(SRC.read_text());today=date.today();errors=[];warnings=[]
    for x in d["sources"]:
        age=(today-datetime.strptime(x["last_verified"],"%Y-%m-%d").date()).days;maxage=x["max_age_days"]
        if age>maxage:
            msg=f"{x['id']} stale {age}d>{maxage}d"
            (errors if n.fail_stale and x.get("critical") else warnings).append(msg)
        if n.online:
            try:
                req=urllib.request.Request(x["url"],headers={"User-Agent":"ai-expert-engine-freshness/1.2"});body=urllib.request.urlopen(req,timeout=15).read(500000).decode("utf-8","ignore")
                m=x.get("expected_marker")
                if m and m.lower() not in body.lower():warnings.append(f"{x['id']} marker not found: {m}")
            except Exception as ex:errors.append(f"{x['id']} online check failed: {ex}")
    [print("WARN",w) for w in warnings];[print("ERROR",e) for e in errors];print(f"freshness checked: {len(d['sources'])} sources")
    return 1 if errors else 0
if __name__=="__main__":raise SystemExit(main())
