#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,urllib.error,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def get(url,tok):
    h={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"ai-expert-engine"}
    if tok:h["Authorization"]=f"Bearer {tok}"
    with urllib.request.urlopen(urllib.request.Request(url,headers=h),timeout=20) as r:return json.load(r)
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",default=os.environ.get("GITHUB_REPOSITORY","trdestan4/ai-expert-engine"));ap.add_argument("--token",default=os.environ.get("GITHUB_TOKEN"));n=ap.parse_args();d=json.loads((ROOT/"engine/governance/github.json").read_text());b=d["branch"];req=d["required"];e=[]
    meta=get(f"https://api.github.com/repos/{n.repo}/branches/{b}",n.token)
    if req["protected"] and not meta.get("protected"):e.append(f"{b} is not protected")
    if meta.get("protected"):
        try:p=get(f"https://api.github.com/repos/{n.repo}/branches/{b}/protection",n.token)
        except urllib.error.HTTPError as ex:e.append(f"cannot inspect detailed protection: HTTP {ex.code}");p={}
        sc=p.get("required_status_checks") or {};contexts=set(sc.get("contexts") or [])|{x.get("context","") for x in sc.get("checks",[]) if isinstance(x,dict)}
        for x in req.get("required_status_checks",[]):
            if x not in contexts:e.append(f"missing required status check: {x}")
        if req.get("strict_status_checks") and sc.get("strict") is not True:e.append("strict status checks disabled")
        pr=p.get("required_pull_request_reviews") or {}
        if req.get("pull_request_reviews") and not pr:e.append("pull-request review requirement missing")
        if req.get("code_owner_reviews") and pr.get("require_code_owner_reviews") is not True:e.append("code-owner reviews not required")
        if int(pr.get("required_approving_review_count",0))<int(req.get("approvals",1)):e.append("approval count below desired state")
        if req.get("dismiss_stale_reviews") and pr.get("dismiss_stale_reviews") is not True:e.append("stale reviews are not dismissed")
        if req.get("allow_force_pushes") is False and (p.get("allow_force_pushes") or {}).get("enabled") is True:e.append("force pushes allowed")
        if req.get("allow_deletions") is False and (p.get("allow_deletions") or {}).get("enabled") is True:e.append("branch deletion allowed")
    if e:
        print("GitHub governance check failed:");[print(" -",x) for x in e];return 1
    print("GitHub governance check passed");return 0
if __name__=="__main__":raise SystemExit(main())
