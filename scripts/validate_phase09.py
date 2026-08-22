#!/usr/bin/env python3
"""Validate Phase 09 Final Control structure and release-gate invariants."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "engine/registry/phase-09-skills.json"
ROUTING = ROOT / "engine/routing/phase-09-routing.md"
POLICY = ROOT / "engine/policies/final-control.md"
SCHEMA = ROOT / "engine/schemas/final-control-result.schema.json"
EVALS = ROOT / "evals/phase-09-final-control.md"
MASTER_EVALS = ROOT / "evals/master-regression.md"
MANIFEST = ROOT / "engine/manifest.json"
REVIEWER_DIR = ROOT / "engine/reviewers"
EXPECTED = {"multi-review", "audit-review", "release-readiness"}
REVIEWERS = {
    "code-reviewer.md", "design-reviewer.md", "security-reviewer.md",
    "performance-reviewer.md", "qa-reviewer.md", "release-reviewer.md"
}
REQUIRED_HEADINGS = [
    "# Purpose", "## Use when", "## Do not use when", "## Inputs", "## Workflow",
    "## Decision rules", "## Reference routing", "## Quality gates", "## Failure handling", "## Output contract"
]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REF_RE = re.compile(r"references/[a-z0-9-]+\.md")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    data: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {raw}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


def validate() -> list[str]:
    errors: list[str] = []
    required_artifacts = (REGISTRY, ROUTING, POLICY, SCHEMA, EVALS, MASTER_EVALS, MANIFEST, REVIEWER_DIR / "reviewer-contract.md")
    for artifact in required_artifacts:
        if not artifact.exists():
            errors.append(f"missing artifact: {artifact.relative_to(ROOT)}")
    if errors:
        return errors

    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"invalid JSON: {exc}"]

    seen: set[str] = set()
    for item in registry.get("skills", []):
        name = item.get("name", "")
        raw_path = item.get("path", "")
        path = ROOT / raw_path
        seen.add(name)
        if not NAME_RE.fullmatch(name):
            errors.append(f"invalid skill name: {name}")
        if not path.exists():
            errors.append(f"missing skill file: {raw_path}")
            continue
        if path.parent.name != name:
            errors.append(f"{raw_path}: folder/name mismatch")
        text = path.read_text(encoding="utf-8")
        try:
            meta = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(f"{raw_path}: {exc}")
            continue
        if meta.get("name") != name:
            errors.append(f"{raw_path}: frontmatter name mismatch")
        desc = meta.get("description", "")
        if not 12 <= len(desc.split()) <= 95:
            errors.append(f"{raw_path}: description routing budget invalid")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{raw_path}: missing {heading}")
        if len(text.split()) > 2800:
            errors.append(f"{raw_path}: SKILL.md too large")

        registered = set(item.get("references", []))
        called = set(REF_RE.findall(text))
        if called != registered:
            errors.append(f"{raw_path}: reference registry mismatch called={sorted(called)} registered={sorted(registered)}")
        for ref in registered:
            rp = path.parent / ref
            if not rp.exists():
                errors.append(f"{raw_path}: missing reference {ref}")
                continue
            words = len(rp.read_text(encoding="utf-8").split())
            if not 70 <= words <= 1800:
                errors.append(f"{rp.relative_to(ROOT)}: reference size invalid ({words})")

    if seen != EXPECTED:
        errors.append(f"registry mismatch: missing={sorted(EXPECTED-seen)} extra={sorted(seen-EXPECTED)}")

    actual_reviewers = {p.name for p in REVIEWER_DIR.glob("*-reviewer.md")}
    if actual_reviewers != REVIEWERS:
        errors.append(f"reviewer profile mismatch: missing={sorted(REVIEWERS-actual_reviewers)} extra={sorted(actual_reviewers-REVIEWERS)}")
    for reviewer in REVIEWERS:
        text = (REVIEWER_DIR / reviewer).read_text(encoding="utf-8") if (REVIEWER_DIR / reviewer).exists() else ""
        for marker in ("## Lens", "## Inspect", "## Blockers", "## Avoid"):
            if marker not in text:
                errors.append(f"engine/reviewers/{reviewer}: missing {marker}")
        if len(text.split()) < 65:
            errors.append(f"engine/reviewers/{reviewer}: reviewer profile too thin")

    routing = ROUTING.read_text(encoding="utf-8").lower()
    for marker in ("`multi-review`", "`audit-review`", "`release-readiness`", "independent", "r3/r4", "do not load all reviewers"):
        if marker not in routing:
            errors.append(f"routing missing marker: {marker}")

    policy = POLICY.read_text(encoding="utf-8").lower()
    for marker in ("independence", "severity and confidence", "risk acceptance", "go with conditions", "hold", "no-go", "schedule pressure"):
        if marker not in policy:
            errors.append(f"final-control policy missing marker: {marker}")

    release_text = (ROOT / ".codex/skills/release-readiness/SKILL.md").read_text(encoding="utf-8").lower()
    for marker in ("green ci", "artifact", "evidence freshness", "data recovery", "go with conditions", "hold", "no-go", "schedule pressure"):
        if marker not in release_text:
            errors.append(f"release-readiness missing marker: {marker}")

    multi_text = (ROOT / ".codex/skills/multi-review/SKILL.md").read_text(encoding="utf-8").lower()
    for marker in ("reviewer independence", "severity and confidence", "majority vote", "accepted risk"):
        if marker not in multi_text:
            errors.append(f"multi-review missing marker: {marker}")

    audit_text = (ROOT / ".codex/skills/audit-review/SKILL.md").read_text(encoding="utf-8").lower()
    for marker in ("risk map", "sample evidence", "critical journeys", "systemic", "coverage limitations"):
        if marker not in audit_text:
            errors.append(f"audit-review missing marker: {marker}")

    decisions = schema.get("properties", {}).get("release_decision", {}).get("enum", [])
    for decision in ("GO", "GO WITH CONDITIONS", "HOLD", "NO-GO"):
        if decision not in decisions:
            errors.append(f"schema missing release decision: {decision}")

    phases = manifest.get("phases", [])
    phase_ids = [str(p.get("id")) for p in phases]
    if phase_ids != [f"{i:02d}" for i in range(10)]:
        errors.append(f"manifest phase sequence invalid: {phase_ids}")
    if manifest.get("status") != "complete":
        errors.append("manifest status must be complete")
    if set(manifest.get("reviewers", [])) != {r.removesuffix(".md") for r in REVIEWERS}:
        errors.append("manifest reviewer list mismatch")

    eval_text = EVALS.read_text(encoding="utf-8").lower()
    for marker in ("routine low-risk", "cross-tenant", "broad repository audit", "green ci", "reviewers disagree", "candidate changes"):
        if marker not in eval_text:
            errors.append(f"phase09 eval missing scenario marker: {marker}")
    master = MASTER_EVALS.read_text(encoding="utf-8")
    if len(re.findall(r"^## M\d+", master, flags=re.M)) < 30:
        errors.append("master regression must contain at least 30 cross-phase scenarios")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Phase 09 validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Phase 09 validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
