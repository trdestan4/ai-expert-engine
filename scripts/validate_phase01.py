#!/usr/bin/env python3
"""Validate Phase 01 creative/product skill structure without third-party packages."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "engine" / "registry" / "phase-01-skills.json"
REQ = [
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
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED = {
    "product-strategy",
    "creative-director",
    "brand-design",
    "anti-generic-design",
    "color-intelligence",
    "typography-intelligence",
    "visual-art-direction",
    "motion-direction",
    "ux-ui-design",
}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    out: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip().strip("\"'")
    return out


def validate() -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(REG.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"invalid Phase 01 registry: {exc}"]

    seen: set[str] = set()
    descriptions: list[tuple[str, set[str]]] = []

    for item in data.get("skills", []):
        name = item.get("name", "")
        path = ROOT / item.get("path", "")

        if name in seen:
            errors.append(f"duplicate skill: {name}")
        seen.add(name)

        if not NAME.fullmatch(name):
            errors.append(f"invalid skill name: {name}")
        if path.parent.name != name:
            errors.append(f"folder/name mismatch: {path.parent.name} != {name}")
        if not path.exists():
            errors.append(f"missing skill: {path.relative_to(ROOT)}")
            continue

        text = path.read_text(encoding="utf-8")
        try:
            meta = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(f"{name}: {exc}")
            continue

        if meta.get("name") != name:
            errors.append(f"{name}: frontmatter mismatch")

        description = meta.get("description", "")
        words = len(description.split())
        if words < 12 or words > 80:
            errors.append(f"{name}: description routing budget {words}")
        descriptions.append((name, set(re.findall(r"[a-z]{4,}", description.lower()))))

        for heading in REQ:
            if heading not in text:
                errors.append(f"{name}: missing {heading}")

        word_count = len(text.split())
        if word_count > 2200:
            errors.append(f"{name}: SKILL too large ({word_count} words)")

        for ref in item.get("references", []):
            ref_path = path.parent / ref
            if not ref_path.exists():
                errors.append(f"{name}: missing ref {ref}")

    if seen != EXPECTED:
        errors.append(
            f"registry set mismatch: missing={sorted(EXPECTED-seen)} extra={sorted(seen-EXPECTED)}"
        )

    for index, (left_name, left_words) in enumerate(descriptions):
        for right_name, right_words in descriptions[index + 1 :]:
            union = left_words | right_words
            overlap = len(left_words & right_words) / len(union) if union else 0
            if overlap > 0.72:
                errors.append(
                    f"possible routing overlap: {left_name} / {right_name} ({overlap:.2f})"
                )

    if not (ROOT / "engine" / "policies" / "design-quality.md").exists():
        errors.append("missing design-quality policy")
    if not (ROOT / "engine" / "routing" / "phase-01-routing.md").exists():
        errors.append("missing Phase 01 routing policy")
    if not (ROOT / "evals" / "phase-01-creative-product.md").exists():
        errors.append("missing Phase 01 eval suite")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Phase 01 validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Phase 01 validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
