#!/usr/bin/env python3
"""Cross-phase structural and governance validation for the complete AI Expert Engine."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "engine/manifest.json"
SKILL_ROOT = ROOT / ".codex/skills"
WORKFLOW = ROOT / ".github/workflows/validate-skills.yml"
README = ROOT / "README.md"
REQUIRED_HEADINGS = [
    "# Purpose", "## Use when", "## Do not use when", "## Inputs", "## Workflow",
    "## Decision rules", "## Reference routing", "## Quality gates", "## Failure handling", "## Output contract"
]
REF_RE = re.compile(r"references/[a-z0-9-]+\.md")
FULL_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
USES_RE = re.compile(r"^\s*-?\s*uses:\s*([^@\s]+)@([^\s#]+)", re.M)


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
    for path in (MANIFEST, SKILL_ROOT, WORKFLOW, README):
        if not path.exists():
            errors.append(f"missing engine artifact: {path.relative_to(ROOT)}")
    if errors:
        return errors

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"invalid engine manifest: {exc}"]

    phases = manifest.get("phases", [])
    expected_ids = [f"{i:02d}" for i in range(10)]
    ids = [str(p.get("id")) for p in phases]
    if ids != expected_ids:
        errors.append(f"manifest phases must be 00..09 in order: {ids}")

    registered: dict[str, Path] = {}
    total_refs = 0
    for phase in phases:
        raw_registry = phase.get("registry", "")
        registry_path = ROOT / raw_registry
        if not registry_path.exists():
            errors.append(f"missing registry: {raw_registry}")
            continue
        try:
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid registry {raw_registry}: {exc}")
            continue
        skills = registry.get("skills", [])
        if not skills:
            errors.append(f"registry has no skills: {raw_registry}")
        for item in skills:
            name = item.get("name", "")
            path = ROOT / item.get("path", "")
            if name in registered:
                errors.append(f"duplicate registered skill: {name}")
                continue
            registered[name] = path
            if not path.exists():
                errors.append(f"missing registered skill: {path.relative_to(ROOT)}")
                continue
            if path.parent.name != name:
                errors.append(f"skill folder/name mismatch: {path.relative_to(ROOT)}")
            text = path.read_text(encoding="utf-8")
            try:
                meta = parse_frontmatter(text)
            except ValueError as exc:
                errors.append(f"{path.relative_to(ROOT)}: {exc}")
                continue
            if meta.get("name") != name:
                errors.append(f"{path.relative_to(ROOT)}: frontmatter name mismatch")
            if len(meta.get("description", "").split()) < 10:
                errors.append(f"{path.relative_to(ROOT)}: description too weak")
            for heading in REQUIRED_HEADINGS:
                if heading not in text:
                    errors.append(f"{path.relative_to(ROOT)}: missing {heading}")
            refs = set(item.get("references", []))
            called = set(REF_RE.findall(text))
            if called != refs:
                errors.append(f"{path.relative_to(ROOT)}: registered/called references differ")
            total_refs += len(refs)
            for ref in refs:
                rp = path.parent / ref
                if not rp.exists():
                    errors.append(f"{path.relative_to(ROOT)}: missing {ref}")

    physical = {p.name for p in SKILL_ROOT.iterdir() if p.is_dir() and (p / "SKILL.md").exists()}
    registered_names = set(registered)
    if physical != registered_names:
        errors.append(
            f"skill registry/physical mismatch: unregistered={sorted(physical-registered_names)} missing={sorted(registered_names-physical)}"
        )

    expected_count = manifest.get("expected_skill_count")
    if expected_count is not None and len(registered) != expected_count:
        errors.append(f"skill count mismatch: expected={expected_count} actual={len(registered)}")
    if not 35 <= len(registered) <= 50:
        errors.append(f"discoverable skill count outside architecture guardrail: {len(registered)}")
    if total_refs < 60:
        errors.append(f"reference depth unexpectedly low: {total_refs}")

    for json_path in list((ROOT / "engine/registry").glob("*.json")) + list((ROOT / "engine/schemas").glob("*.json")) + [MANIFEST]:
        try:
            json.loads(json_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid JSON {json_path.relative_to(ROOT)}: {exc}")

    readme = README.read_text(encoding="utf-8")
    for i in range(10):
        marker = f"Phase {i:02d}"
        if marker not in readme:
            errors.append(f"README missing phase marker: {marker}")
    if "Next phase:" in readme or "Next phases:" in readme:
        errors.append("README still declares unfinished next phase")
    if "AI Expert Engine v1.0" not in readme:
        errors.append("README missing v1.0 completion marker")

    workflow = WORKFLOW.read_text(encoding="utf-8")
    if "validators=(scripts/validate_*.py)" not in workflow:
        errors.append("workflow does not execute all validators")
    uses = USES_RE.findall(workflow)
    if not uses:
        errors.append("workflow has no external actions")
    for action, version in uses:
        if action.startswith("./"):
            continue
        if not FULL_SHA_RE.fullmatch(version):
            errors.append(f"workflow action is not immutable-SHA pinned: {action}@{version}")

    validators = sorted((ROOT / "scripts").glob("validate_*.py"))
    names = {p.name for p in validators}
    required_validators = {"validate_core.py", "validate_engine.py"} | {f"validate_phase{i:02d}.py" for i in range(1, 10)}
    if names != required_validators:
        errors.append(f"validator set mismatch: missing={sorted(required_validators-names)} extra={sorted(names-required_validators)}")

    if not (ROOT / "evals/master-regression.md").exists():
        errors.append("missing master regression suite")
    if not (ROOT / "engine/reviewers/reviewer-contract.md").exists():
        errors.append("missing reviewer contract")

    accidental = [p.name for p in ROOT.iterdir() if p.name.lower().startswith(("noop", "dummy", "tmp"))]
    if accidental:
        errors.append(f"accidental root artifacts present: {sorted(accidental)}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Engine validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Engine validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
