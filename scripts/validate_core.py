#!/usr/bin/env python3
"""Validate Phase 00 core skill contracts without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "engine" / "registry" / "core-skills.json"
REQUIRED_SECTIONS = [
    "# Purpose",
    "## Use when",
    "## Do not use when",
    "## Inputs",
    "## Workflow",
    "## Decision rules",
    "## Reference routing",
    "## Quality gates",
    "## Failure handling",
    "## Output contract",
]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    result: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise ValueError(f"invalid frontmatter line: {raw}")
        key, value = raw.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def validate() -> list[str]:
    errors: list[str] = []
    if not REGISTRY.exists():
        return [f"missing registry: {REGISTRY.relative_to(ROOT)}"]

    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"invalid registry JSON: {exc}"]

    seen: set[str] = set()
    for item in registry.get("skills", []):
        name = item.get("name", "")
        path = ROOT / item.get("path", "")
        rel = path.relative_to(ROOT) if path.is_absolute() and str(path).startswith(str(ROOT)) else path

        if name in seen:
            errors.append(f"duplicate skill name in registry: {name}")
        seen.add(name)
        if not NAME_RE.fullmatch(name):
            errors.append(f"invalid skill name: {name}")
        if not path.exists():
            errors.append(f"missing skill file: {item.get('path')}")
            continue

        text = path.read_text(encoding="utf-8")
        try:
            fm = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue

        if fm.get("name") != name:
            errors.append(f"{rel}: frontmatter name {fm.get('name')!r} != registry {name!r}")
        description = fm.get("description", "")
        if len(description.split()) < 12:
            errors.append(f"{rel}: description too vague/short")
        if len(description.split()) > 80:
            errors.append(f"{rel}: description exceeds routing budget")

        for heading in REQUIRED_SECTIONS:
            if heading not in text:
                errors.append(f"{rel}: missing required section {heading!r}")

        for ref in item.get("references", []):
            ref_path = path.parent / ref
            if not ref_path.exists():
                errors.append(f"{rel}: missing registered reference {ref}")

        word_count = len(text.split())
        if word_count > 2200:
            errors.append(f"{rel}: SKILL.md exceeds core size guard ({word_count} words)")

    expected = {"master-agent", "repository-intelligence", "task-planning", "debugging"}
    missing = expected - seen
    extra = seen - expected
    if missing:
        errors.append(f"registry missing core skills: {sorted(missing)}")
    if extra:
        errors.append(f"unexpected Phase 00 skills: {sorted(extra)}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Phase 00 validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Phase 00 validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
