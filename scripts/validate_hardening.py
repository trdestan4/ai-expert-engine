#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];REV={"code-reviewer","design-reviewer","security-reviewer","performance-reviewer","qa-reviewer","release-reviewer"};REQ={"run_behavioral_evals.py","validate_semantics.py","resolve_stack_profile.py","profile_repository.py","enginectl.py","check_github_governance.py","apply_github_governance.py","routing_report.py"}
def skills():
    s=set()
    for p in (ROOT/"engine/registry").glob("*.json"):s.update(i["name"] for i in json.loads(p.read_text()).get("skills",[]))
    return s
def main():
    e=[];s=skills()
    if len(s)!=43:e.append("skill count changed")
    if {p.stem for p in (ROOT/".cursor/agents").glob("*.md")}!=REV:e.append("reviewer set mismatch")
    ps=json.loads((ROOT/"engine/profiles/profiles.json").read_text())["profiles"]
    if len(ps)<9:e.append("need >=9 profiles")
    for p in ps:
        for x in p["owners"]+p["conditional"]:
            if x not in s:e.append(f"profile {p['id']} unknown {x}")
    ids=[json.loads(x)["id"] for x in (ROOT/"evals/behavioral/cases.jsonl").read_text().splitlines() if x.strip()]
    if len(ids)<15 or len(ids)!=len(set(ids)):e.append("behavioral corpus invalid")
    for x in REQ:
        if not (ROOT/"scripts"/x).exists():e.append("missing "+x)
    if e:print("hardening validation failed:");[print(" -",x) for x in e];return 1
    print(f"hardening validation passed: 43 skills, 6 reviewers, {len(ids)} cases, {len(ps)} profiles");return 0
if __name__=="__main__":raise SystemExit(main())
