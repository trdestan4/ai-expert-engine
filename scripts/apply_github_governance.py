#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",default=os.environ.get("GITHUB_REPOSITORY","trdestan4/ai-expert-engine"));ap.add_argument("--token",default=os.environ.get("GITHUB_ADMIN_TOKEN"));n=ap.parse_args()
    if not n.token:raise SystemExit("GITHUB_ADMIN_TOKEN is required")
    d=json.loads((ROOT/"engine/governance/github.json").read_text());r=d["required"];payload={"required_status_checks":{"strict":True,"contexts":r["required_status_checks"]},"enforce_admins":True,"required_pull_request_reviews":{"dismiss_stale_reviews":True,"require_code_owner_reviews":True,"required_approving_review_count":r["approvals"]},"restrictions":None,"required_conversation_resolution":True,"allow_force_pushes":False,"allow_deletions":False}
    req=urllib.request.Request(f"https://api.github.com/repos/{n.repo}/branches/{d['branch']}/protection",data=json.dumps(payload).encode(),method="PUT",headers={"Accept":"application/vnd.github+json","Authorization":f"Bearer {n.token}","X-GitHub-Api-Version":"2022-11-28","Content-Type":"application/json","User-Agent":"ai-expert-engine"})
    with urllib.request.urlopen(req,timeout=30):pass
    print("branch protection applied");return 0
if __name__=="__main__":raise SystemExit(main())
