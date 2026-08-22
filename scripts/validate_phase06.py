#!/usr/bin/env python3
"""Validate Phase 06 business/growth skills, references and critical contracts."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "engine/registry/phase-06-skills.json"
POL = ROOT / "engine/policies/business-growth.md"
ROUTE = ROOT / "engine/routing/phase-06-routing.md"
SCHEMA = ROOT / "engine/schemas/business-growth-change.schema.json"
EVAL = ROOT / "evals/phase-06-business-growth.md"
EXPECTED = {"seo","content-conversion","ecommerce","saas-platform"}
HEADINGS = ["# Purpose","## Use when","## Do not use when","## Inputs","## Workflow","## Decision rules","## Reference routing","## Quality gates","## Failure handling","## Output contract"]
REF_RE = re.compile(r"`(references/[a-z0-9._/-]+\.md)`")
WORD_RE = re.compile(r"[a-z][a-z0-9-]{3,}", re.I)


def meta(text: str) -> dict[str,str]:
    if not text.startswith("---\n"): raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0: raise ValueError("unterminated frontmatter")
    out = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            k,v = line.split(":",1); out[k.strip()] = v.strip().strip("\"'")
    return out


def sim(a: str,b: str) -> float:
    x,y=set(WORD_RE.findall(a.lower())),set(WORD_RE.findall(b.lower()))
    return len(x&y)/len(x|y) if x and y else 0.0


def validate() -> list[str]:
    errors=[]
    for p in (REG,POL,ROUTE,SCHEMA,EVAL):
        if not p.exists(): errors.append(f"missing artifact: {p.relative_to(ROOT)}")
    if errors: return errors
    try:
        registry=json.loads(REG.read_text()); json.loads(SCHEMA.read_text())
    except Exception as exc: return [f"invalid JSON: {exc}"]
    seen=set(); descs=[]
    for item in registry.get("skills",[]):
        name=item.get("name",""); path=ROOT/item.get("path","")
        seen.add(name)
        if not path.exists(): errors.append(f"missing skill: {name}"); continue
        text=path.read_text(); m=meta(text)
        if m.get("name")!=name: errors.append(f"{name}: frontmatter mismatch")
        d=m.get("description",""); descs.append((name,d))
        if not 12 <= len(d.split()) <= 85: errors.append(f"{name}: description budget invalid")
        for h in HEADINGS:
            if h not in text: errors.append(f"{name}: missing {h}")
        if len(text.split())>2200: errors.append(f"{name}: SKILL.md too large")
        registered=set(item.get("references",[]))
        called=set(REF_RE.findall(text))
        for ref in registered | called:
            rp=path.parent/ref
            if not rp.exists(): errors.append(f"{name}: missing reference {ref}"); continue
            n=len(rp.read_text().split())
            if n<80: errors.append(f"{name}/{ref}: reference too thin ({n})")
            if n>1800: errors.append(f"{name}/{ref}: reference too large ({n})")
        if called-registered: errors.append(f"{name}: called references not registered {sorted(called-registered)}")
        if registered-called: errors.append(f"{name}: registered references not routed {sorted(registered-called)}")
    if seen!=EXPECTED: errors.append(f"registry mismatch missing={sorted(EXPECTED-seen)} extra={sorted(seen-EXPECTED)}")
    for i,(a,ad) in enumerate(descs):
        for b,bd in descs[i+1:]:
            s=sim(ad,bd)
            if s>0.62: errors.append(f"routing overlap {a}/{b} {s:.2f}")
    routing=ROUTE.read_text().lower()
    for name in EXPECTED:
        if f"`{name}`" not in routing: errors.append(f"routing missing {name}")
    for marker in ("mandatory gate escalation","token rule","integrations","identity-access","database-data"):
        if marker not in routing: errors.append(f"routing missing marker: {marker}")
    policy=POL.read_text().lower()
    for marker in ("schema.org 30.0","no ranking guarantees","fake urgency","server-authoritative","cross-tenant access defaults to deny"):
        if marker not in policy: errors.append(f"policy missing marker: {marker}")
    ev=EVAL.read_text().lower()
    for marker in ("routing positives","routing negatives","edge cases","quality assertions"):
        if marker not in ev: errors.append(f"eval missing {marker}")
    skill_markers={
      "seo":("crawl","structured data","canonical","ai/generative","never promise rankings"),
      "content-conversion":("proof","dark-pattern","pricing","cta","hypothesis"),
      "ecommerce":("variant","inventory","server","idempotency","refund"),
      "saas-platform":("tenant","entitlement","client-side plan flag","meter","reconcile")}
    for name,marks in skill_markers.items():
        t=(ROOT/f".codex/skills/{name}/SKILL.md").read_text().lower()
        for mark in marks:
            if mark not in t: errors.append(f"{name} missing marker: {mark}")
    return errors


def main() -> int:
    errors=validate()
    if errors:
        print("Phase 06 validation FAILED")
        for e in errors: print(f"- {e}")
        return 1
    print("Phase 06 validation PASSED")
    return 0

if __name__ == "__main__": sys.exit(main())