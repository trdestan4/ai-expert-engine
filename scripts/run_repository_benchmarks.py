#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];CORPUS=ROOT/"benchmarks/corpus.json"
def sh(a,cwd=None):return subprocess.run(a,cwd=cwd,text=True,capture_output=True)
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--limit",type=int);ap.add_argument("--output",default=".artifacts/repository-benchmarks.json");n=ap.parse_args();items=json.loads(CORPUS.read_text())["external"];items=items[:n.limit] if n.limit else items;results=[]
    with tempfile.TemporaryDirectory() as td:
        for x in items:
            p=Path(td)/x["id"];r=sh(["git","clone","--filter=blob:none","--no-checkout",f"https://github.com/{x['repo']}.git",str(p)])
            if r.returncode:results.append({"id":x["id"],"passed":False,"error":r.stderr[-1000:]});continue
            r=sh(["git","checkout","--detach",x["commit"]],p)
            if r.returncode:results.append({"id":x["id"],"passed":False,"error":r.stderr[-1000:]});continue
            prof=sh([sys.executable,str(ROOT/"scripts/profile_repository.py"),str(p)]);res=sh([sys.executable,str(ROOT/"scripts/resolve_stack_profile.py"),str(p),"--all"])
            try:data=json.loads(res.stdout);selected=(data.get("selected") or{}).get("id")
            except Exception:selected=None
            expected=x.get("expected_any_profile",[]);passed=prof.returncode==0 and (not expected or selected in expected)
            results.append({"id":x["id"],"repo":x["repo"],"commit":x["commit"],"selected_profile":selected,"expected_any_profile":expected,"passed":passed,"resolver_rc":res.returncode})
            print(f"[{'PASS' if passed else 'FAIL'}] {x['id']} -> {selected}")
    out={"passed":sum(r["passed"] for r in results),"total":len(results),"results":results};op=Path(n.output);op.parent.mkdir(parents=True,exist_ok=True);op.write_text(json.dumps(out,indent=2)+"\n");return 0 if out["passed"]==out["total"] else 1
if __name__=="__main__":raise SystemExit(main())
