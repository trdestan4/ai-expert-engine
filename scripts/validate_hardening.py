#!/usr/bin/env python3
from __future__ import annotations
import ast,json,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REV={"code-reviewer","design-reviewer","security-reviewer","performance-reviewer","qa-reviewer","release-reviewer"}
REQ={"run_behavioral_evals.py","validate_semantics.py","resolve_stack_profile.py","profile_repository.py","enginectl.py","check_github_governance.py","apply_github_governance.py","routing_report.py"}
def skills():
    s=set()
    for p in (ROOT/"engine/registry").glob("*.json"):s.update(i["name"] for i in json.loads(p.read_text()).get("skills",[]))
    return s
def run(*args):return subprocess.run([sys.executable,*map(str,args)],cwd=ROOT,text=True,capture_output=True)
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
    for p in (ROOT/"scripts").glob("*.py"):
        try:ast.parse(p.read_text(),filename=str(p))
        except SyntaxError as ex:e.append(f"python syntax error {p.name}:{ex.lineno}: {ex.msg}")
    corpus=run(ROOT/"scripts/run_behavioral_evals.py","--validate-corpus")
    if corpus.returncode!=0:e.append("behavioral corpus runner failed: "+(corpus.stderr or corpus.stdout).strip())
    with tempfile.TemporaryDirectory() as td:
        t=Path(td)/"project";t.mkdir();(t/"AGENTS.md").write_text("# Project rules\n\nKeep this line.\n");(t/"package.json").write_text(json.dumps({"dependencies":{"next":"16.0.0","@supabase/supabase-js":"2.0.0"}}));(t/"app").mkdir();(t/"app/page.tsx").write_text("export default function Page(){return null}\n")
        prof=run(ROOT/"scripts/resolve_stack_profile.py",t,"--all")
        try:selected=json.loads(prof.stdout).get("selected",{}).get("id") if prof.returncode==0 else None
        except Exception:selected=None
        if selected!="next-supabase":e.append(f"stack profile smoke failed: selected={selected!r} stderr={prof.stderr.strip()}")
        install=run(ROOT/"scripts/enginectl.py","install",t)
        if install.returncode!=0:e.append("engine install smoke failed: "+(install.stderr or install.stdout).strip())
        doctor=run(ROOT/"scripts/enginectl.py","doctor",t)
        if doctor.returncode!=0:e.append("engine doctor smoke failed after install")
        update=run(ROOT/"scripts/enginectl.py","update",t)
        if update.returncode!=0:e.append("engine update smoke failed: "+(update.stderr or update.stdout).strip())
        managed=t/".codex/skills/master-agent/SKILL.md"
        if managed.exists():managed.write_text(managed.read_text()+"\nlocal drift\n")
        reject=run(ROOT/"scripts/enginectl.py","update",t)
        if reject.returncode==0:e.append("engine update failed to reject local drift")
        forced=run(ROOT/"scripts/enginectl.py","update",t,"--force")
        if forced.returncode!=0:e.append("engine forced update/backup smoke failed: "+(forced.stderr or forced.stdout).strip())
        doctor2=run(ROOT/"scripts/enginectl.py","doctor",t)
        if doctor2.returncode!=0:e.append("engine doctor smoke failed after forced update")
        if "Keep this line." not in (t/"AGENTS.md").read_text():e.append("installer failed to preserve project AGENTS content")
    if e:
        print("hardening validation failed:");[print(" -",x) for x in e];return 1
    print(f"hardening validation passed: 43 skills, 6 reviewers, {len(ids)} cases, {len(ps)} profiles, installer/profile smoke tests passed");return 0
if __name__=="__main__":raise SystemExit(main())
