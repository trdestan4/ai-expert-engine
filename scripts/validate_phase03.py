#!/usr/bin/env python3
"""Validate Phase 03 backend/API skill structure and critical quality contracts."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "engine/registry/phase-03-skills.json"
POLICY = ROOT / "engine/policies/backend-api-engineering.md"
ROUTING = ROOT / "engine/routing/phase-03-routing.md"
SCHEMA = ROOT / "engine/schemas/backend-api-change.schema.json"
EVALS = ROOT / "evals/phase-03-backend-api.md"
EXPECTED = {"backend-engineering", "api-engineering"}
REQUIRED_SECTIONS = [
    "# Purpose", "## Use when", "## Do not use when", "## Inputs", "## Workflow",
    "## Decision rules", "## Reference routing", "## Quality gates", "## Failure handling",
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
    out: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {raw}")
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip().strip("\"'")
    return out


def similarity(a: str, b: str) -> float:
    wa = set(WORD_RE.findall(a.lower()))
    wb = set(WORD_RE.findall(b.lower()))
    return len(wa & wb) / len(wa | wb) if wa and wb else 0.0


def validate() -> list[str]:
    errors: list[str] = []
    for required in (REGISTRY, POLICY, ROUTING, SCHEMA, EVALS):
        if not required.exists():
            errors.append(f"missing Phase 03 artifact: {required.relative_to(ROOT)}")
    if errors:
        return errors

    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"invalid registry JSON: {exc}"]
    try:
        json.loads(SCHEMA.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"invalid backend/API schema JSON: {exc}")

    seen: set[str] = set()
    descriptions: list[tuple[str, str]] = []
    for item in registry.get("skills", []):
        name = item.get("name", "")
        raw_path = item.get("path", "")
        path = ROOT / raw_path
        if name in seen:
            errors.append(f"duplicate skill name: {name}")
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
        desc_words = len(desc.split())
        if desc_words < 12 or desc_words > 80:
            errors.append(f"{raw_path}: description routing budget invalid ({desc_words} words)")
        descriptions.append((name, desc))

        for heading in REQUIRED_SECTIONS:
            if heading not in text:
                errors.append(f"{raw_path}: missing {heading}")
        words = len(text.split())
        if words > 2200:
            errors.append(f"{raw_path}: SKILL.md too large ({words} words)")

        refs = item.get("references", [])
        if not refs:
            errors.append(f"{raw_path}: no lazy-loaded references")
        for ref in refs:
            ref_path = path.parent / ref
            if not ref_path.exists():
                errors.append(f"{raw_path}: missing reference {ref}")
                continue
            ref_words = len(ref_path.read_text(encoding="utf-8").split())
            if ref_words < 80:
                errors.append(f"{ref_path.relative_to(ROOT)}: reference too thin ({ref_words})")
            if ref_words > 1800:
                errors.append(f"{ref_path.relative_to(ROOT)}: reference too large ({ref_words})")

    if seen != EXPECTED:
        errors.append(f"registry set mismatch: missing={sorted(EXPECTED-seen)} extra={sorted(seen-EXPECTED)}")

    for i, (a_name, a_desc) in enumerate(descriptions):
        for b_name, b_desc in descriptions[i + 1:]:
            score = similarity(a_desc, b_desc)
            if score > 0.62:
                errors.append(f"possible routing overlap: {a_name}/{b_name} ({score:.2f})")

    routing = ROUTING.read_text(encoding="utf-8").lower()
    for name in EXPECTED:
        if f"`{name}`" not in routing:
            errors.append(f"routing missing {name}")
    for marker in ("database-data", "identity-access", "realtime-async"):
        if marker not in routing:
            errors.append(f"routing missing future boundary marker: {marker}")

    eval_text = EVALS.read_text(encoding="utf-8").lower()
    for marker in ("routing positives", "routing negatives", "edge cases", "quality assertions"):
        if marker not in eval_text:
            errors.append(f"eval suite missing section: {marker}")

    backend_text = (ROOT / ".codex/skills/backend-engineering/SKILL.md").read_text(encoding="utf-8").lower()
    for marker in ("installed", "validation", "side effects", "concurrency", "observability", "timeouts"):
        if marker not in backend_text:
            errors.append(f"backend-engineering missing core marker: {marker}")

    api_text = (ROOT / ".codex/skills/api-engineering/SKILL.md").read_text(encoding="utf-8").lower()
    for marker in ("openapi", "graphql", "pagination", "idempotency", "rate", "compatibility", "rfc 9457"):
        if marker not in api_text:
            errors.append(f"api-engineering missing contract marker: {marker}")

    policy_text = POLICY.read_text(encoding="utf-8").lower()
    for marker in ("runtime validation", "public errors", "unbounded collections", "durable work"):
        if marker not in policy_text:
            errors.append(f"backend/API policy missing marker: {marker}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Phase 03 validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Phase 03 validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())