#!/usr/bin/env python3
"""Cross-phase structural, semantic, runtime-hardening and CI governance validation."""
from __future__ import annotations
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"engine/manifest.json";SKILL_ROOT=ROOT/".codex/skills";README=ROOT/"README.md"
REQUIRED_HEADINGS=["# Purpose","## Use when","## Do not use when","## Inputs","## Workflow","## Decision rules","## Reference routing","## Quality gates","## Failure handling","## Output contract"]
REF_RE=re.compile(r"references/[a-z0-9-]+\.md");FULL_SHA_RE=re.compile(r"^[0-9a-f]{40}$");USES_RE=re.compile(r"^\s*-?\s*uses:\s*([^@\s]+)@([^\s#]+)",re.M)
def parse_frontmatter(text):
    if not text.startswith("---\n"):raise ValueError("missing YAML frontmatter")
    end=text.find("\n---\n",4)
    if end<0:raise ValueError("unterminated YAML frontmatter")
    out={}
    for raw in text[4:end].splitlines():
        line=raw.strip()
        if not line or line.startswith("#"):continue
        if ":" not in line:raise ValueError(f"invalid frontmatter line: {raw}")
        k,v=line.split(":",1);out[k.strip()]=v.strip().strip("\"'")
    return out
def validate():
    e=[]
    required=[MANIFEST,SKILL_ROOT,README,ROOT/".github/workflows/validate-skills.yml",ROOT/"evals/master-regression.md",ROOT/"evals/behavioral/cases.jsonl",ROOT/"engine/reviewers/reviewer-contract.md",ROOT/"engine/profiles/profiles.json",ROOT/"docs/INSTALL.md"]
    for p in required:
        if not p.exists():e.append(f"missing engine artifact: {p.relative_to(ROOT)}")
    if e:return e
    try:m=json.loads(MANIFEST.read_text())
    except Exception as ex:return [f"invalid engine manifest: {ex}"]
    if m.get("version")!="1.1.0" or m.get("status")!="hardened":e.append("manifest must declare v1.1.0 hardened")
    phases=m.get("phases",[]);ids=[str(p.get("id")) for p in phases]
    if ids!=[f"{i:02d}" for i in range(10)]:e.append(f"manifest phases must be 00..09 in order: {ids}")
    registered={};total_refs=0
    for phase in phases:
        raw=phase.get("registry","");rp=ROOT/raw
        if not rp.exists():e.append(f"missing registry: {raw}");continue
        try:r=json.loads(rp.read_text())
        except Exception as ex:e.append(f"invalid registry {raw}: {ex}");continue
        if not r.get("skills"):e.append(f"registry has no skills: {raw}")
        for item in r.get("skills",[]):
            name=item.get("name","");p=ROOT/item.get("path","")
            if name in registered:e.append(f"duplicate registered skill: {name}");continue
            registered[name]=p
            if not p.exists():e.append(f"missing registered skill: {p.relative_to(ROOT)}");continue
            if p.parent.name!=name:e.append(f"skill folder/name mismatch: {p.relative_to(ROOT)}")
            text=p.read_text()
            try:meta=parse_frontmatter(text)
            except ValueError as ex:e.append(f"{p.relative_to(ROOT)}: {ex}");continue
            if meta.get("name")!=name:e.append(f"{p.relative_to(ROOT)}: frontmatter name mismatch")
            if len(meta.get("description","").split())<10:e.append(f"{p.relative_to(ROOT)}: description too weak")
            for h in REQUIRED_HEADINGS:
                if h not in text:e.append(f"{p.relative_to(ROOT)}: missing {h}")
            refs=set(item.get("references",[]));called=set(REF_RE.findall(text))
            if called!=refs:e.append(f"{p.relative_to(ROOT)}: registered/called references differ")
            total_refs+=len(refs)
            for ref in refs:
                if not (p.parent/ref).exists():e.append(f"{p.relative_to(ROOT)}: missing {ref}")
    physical={p.name for p in SKILL_ROOT.iterdir() if p.is_dir() and (p/"SKILL.md").exists()};names=set(registered)
    if physical!=names:e.append(f"skill registry/physical mismatch: unregistered={sorted(physical-names)} missing={sorted(names-physical)}")
    if len(registered)!=m.get("expected_skill_count"):e.append(f"skill count mismatch: expected={m.get('expected_skill_count')} actual={len(registered)}")
    if not 35<=len(registered)<=50:e.append(f"discoverable skill count outside architecture guardrail: {len(registered)}")
    if total_refs<60:e.append(f"reference depth unexpectedly low: {total_refs}")
    for p in list((ROOT/"engine/registry").glob("*.json"))+list((ROOT/"engine/schemas").glob("*.json"))+[MANIFEST,ROOT/"engine/profiles/profiles.json",ROOT/"engine/governance/github.json"]:
        try:json.loads(p.read_text())
        except Exception as ex:e.append(f"invalid JSON {p.relative_to(ROOT)}: {ex}")
    readme=README.read_text()
    for i in range(10):
        if f"Phase {i:02d}" not in readme:e.append(f"README missing phase marker: Phase {i:02d}")
    if "Next phase:" in readme or "Next phases:" in readme:e.append("README still declares unfinished next phase")
    if "AI Expert Engine v1.1" not in readme:e.append("README missing v1.1 hardening marker")
    expected_validators={"validate_core.py","validate_engine.py","validate_hardening.py","validate_semantics.py"}|{f"validate_phase{i:02d}.py" for i in range(1,10)}
    namesv={p.name for p in (ROOT/"scripts").glob("validate_*.py")}
    if namesv!=expected_validators:e.append(f"validator set mismatch: missing={sorted(expected_validators-namesv)} extra={sorted(namesv-expected_validators)}")
    for wf in sorted((ROOT/".github/workflows").glob("*.yml")):
        text=wf.read_text();uses=USES_RE.findall(text)
        for action,version in uses:
            if not action.startswith("./") and not FULL_SHA_RE.fullmatch(version):e.append(f"{wf.relative_to(ROOT)} action is not immutable-SHA pinned: {action}@{version}")
    workflow=(ROOT/".github/workflows/validate-skills.yml").read_text()
    if "validators=(scripts/validate_*.py)" not in workflow:e.append("validation workflow does not execute all validators")
    agents=ROOT/".cursor/agents";expected_reviewers=set(m.get("reviewers",[]));actual={p.stem for p in agents.glob("*.md")}
    if actual!=expected_reviewers:e.append(f"isolated reviewer set mismatch: {sorted(actual)}")
    accidental=[p.name for p in ROOT.iterdir() if p.name.lower().startswith(("noop","dummy","tmp"))]
    if accidental:e.append(f"accidental root artifacts present: {sorted(accidental)}")
    return e
def main():
    e=validate()
    if e:
        print("Engine validation FAILED");[print("-",x) for x in e];return 1
    print("Engine validation PASSED");return 0
if __name__=="__main__":sys.exit(main())
