#!/usr/bin/env python3
"""Validate Phase 02 web/frontend skill structure and routing contracts."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "engine" / "registry" / "phase-02-skills.json"
POLICY = ROOT / "engine" / "policies" / "frontend-engineering.md"
ROUTING = ROOT / "engine" / "routing" / "phase-02-routing.md"
SCHEMA = ROOT / "engine" / "schemas" / "frontend-implementation-plan.schema.json"
EVALS = ROOT / "evals" / "phase-02-web-frontend.md"

EXPECTED = {
    "web-platform",
    "frontend-engineering",
    "react-nextjs",
    "software-architecture",
}
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
WORD_RE = re.compile(r"[a-z][a-z0-9-]{3,}", re.I)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    result: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {raw}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip("\"'")
    return result


def similarity(a: str, b: str) -> float:
    wa = set(WORD_RE.findall(a.lower()))
    wb = set(WORD_RE.findall(b.lower()))
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / len(wa | wb)


def validate() -> list[str]:
    errors: list[str] = []

    for required in (REGISTRY, POLICY, ROUTING, SCHEMA, EVALS):
        if not required.exists():
            errors.append(f"missing Phase 02 artifact: {required.relative_to(ROOT)}")

    if errors:
        return errors

    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"invalid registry JSON: {exc}"]

    try:
        json.loads(SCHEMA.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"invalid frontend schema JSON: {exc}")

    seen: set[str] = set()
    descriptions: list[tuple[str, str]] = []

    for item in data.get("skills", []):
        name = item.get("name", "")
        raw_path = item.get("path", "")
        path = ROOT / raw_path

        if name in seen:
            errors.append(f"duplicate skill name: {name}")
        seen.add(name)

        if not NAME_RE.fullmatch(name):
            errors.append(f"invalid skill name: {name}")
        if not raw_path or not path.exists():
            errors.append(f"missing skill file: {raw_path}")
            continue
        if path.parent.name != name:
            errors.append(f"{raw_path}: folder/name mismatch ({path.parent.name} != {name})")

        text = path.read_text(encoding="utf-8")
        try:
            meta = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(f"{raw_path}: {exc}")
            continue

        if meta.get("name") != name:
            errors.append(f"{raw_path}: frontmatter name {meta.get('name')!r} != {name!r}")

        description = meta.get("description", "")
        words = len(description.split())
        if words < 12:
            errors.append(f"{raw_path}: description too vague/short ({words} words)")
        if words > 80:
            errors.append(f"{raw_path}: description exceeds routing budget ({words} words)")
        descriptions.append((name, description))

        for heading in REQUIRED_SECTIONS:
            if heading not in text:
                errors.append(f"{raw_path}: missing required section {heading!r}")

        word_count = len(text.split())
        if word_count > 2200:
            errors.append(f"{raw_path}: SKILL.md exceeds size guard ({word_count} words)")

        refs = item.get("references", [])
        if not refs:
            errors.append(f"{raw_path}: no lazy-loaded references registered")
        for ref in refs:
            ref_path = path.parent / ref
            if not ref_path.exists():
                errors.append(f"{raw_path}: missing registered reference {ref}")
                continue
            ref_words = len(ref_path.read_text(encoding="utf-8").split())
            if ref_words < 80:
                errors.append(f"{ref_path.relative_to(ROOT)}: reference too thin ({ref_words} words)")
            if ref_words > 1800:
                errors.append(f"{ref_path.relative_to(ROOT)}: reference exceeds lazy-load guard ({ref_words} words)")

    if seen != EXPECTED:
        errors.append(
            f"registry set mismatch: missing={sorted(EXPECTED - seen)} extra={sorted(seen - EXPECTED)}"
        )

    for i, (a_name, a_desc) in enumerate(descriptions):
        for b_name, b_desc in descriptions[i + 1 :]:
            score = similarity(a_desc, b_desc)
            if score > 0.62:
                errors.append(
                    f"possible routing overlap: {a_name} / {b_name} (jaccard={score:.2f})"
                )

    routing_text = ROUTING.read_text(encoding="utf-8")
    for name in EXPECTED:
        if f"`{name}`" not in routing_text:
            errors.append(f"routing file does not mention {name}")

    eval_text = EVALS.read_text(encoding="utf-8").lower()
    for marker in ("routing positives", "routing negatives", "edge cases", "quality assertions"):
        if marker not in eval_text:
            errors.append(f"eval suite missing section: {marker}")

    react_path = ROOT / ".codex/skills/react-nextjs/SKILL.md"
    if react_path.exists():
        react_text = react_path.read_text(encoding="utf-8").lower()
        for phrase in ("installed", "version", "server components", "server actions", "cache"):
            if phrase not in react_text:
                errors.append(f"react-nextjs missing version/runtime guard marker: {phrase}")

    frontend_path = ROOT / ".codex/skills/frontend-engineering/SKILL.md"
    if frontend_path.exists():
        frontend_text = frontend_path.read_text(encoding="utf-8").lower()
        for phrase in ("semantic", "state", "responsive", "quality gates"):
            if phrase not in frontend_text:
                errors.append(f"frontend-engineering missing core marker: {phrase}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Phase 02 validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Phase 02 validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
