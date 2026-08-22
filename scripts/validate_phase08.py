#!/usr/bin/env python3
"""Validate Phase 08 AI / Asset Production structure and critical quality rules."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "engine/registry/phase-08-skills.json"
ROUTING = ROOT / "engine/routing/phase-08-routing.md"
POLICY = ROOT / "engine/policies/ai-asset-production.md"
SCHEMA = ROOT / "engine/schemas/ai-asset-change.schema.json"
EVALS = ROOT / "evals/phase-08-ai-assets.md"
EXPECTED = {"ai-engineering", "asset-production"}
REQUIRED_HEADINGS = [
    "# Purpose", "## Use when", "## Do not use when", "## Inputs", "## Workflow",
    "## Decision rules", "## Reference routing", "## Quality gates", "## Failure handling", "## Output contract"
]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REF_RE = re.compile(r"references/[a-z0-9-]+\.md")
WORD_RE = re.compile(r"[a-z][a-z0-9-]{3,}", re.I)


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


def similarity(a: str, b: str) -> float:
    aa = set(WORD_RE.findall(a.lower()))
    bb = set(WORD_RE.findall(b.lower()))
    return len(aa & bb) / len(aa | bb) if aa and bb else 0.0


def validate() -> list[str]:
    errors: list[str] = []
    for artifact in (REGISTRY, ROUTING, POLICY, SCHEMA, EVALS):
        if not artifact.exists():
            errors.append(f"missing artifact: {artifact.relative_to(ROOT)}")
    if errors:
        return errors

    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        json.loads(SCHEMA.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"invalid JSON: {exc}"]

    seen: set[str] = set()
    descriptions: list[tuple[str, str]] = []

    for item in registry.get("skills", []):
        name = item.get("name", "")
        raw_path = item.get("path", "")
        path = ROOT / raw_path
        if name in seen:
            errors.append(f"duplicate skill: {name}")
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
        if not 12 <= len(desc.split()) <= 90:
            errors.append(f"{raw_path}: description routing budget invalid")
        descriptions.append((name, desc))

        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{raw_path}: missing {heading}")
        if len(text.split()) > 2600:
            errors.append(f"{raw_path}: SKILL.md too large")

        registered = set(item.get("references", []))
        called = set(REF_RE.findall(text))
        if not registered:
            errors.append(f"{raw_path}: no lazy references")
        if called != registered:
            errors.append(
                f"{raw_path}: reference registry mismatch called={sorted(called)} registered={sorted(registered)}"
            )
        for ref in registered:
            rp = path.parent / ref
            if not rp.exists():
                errors.append(f"{raw_path}: missing reference {ref}")
                continue
            words = len(rp.read_text(encoding="utf-8").split())
            if words < 80:
                errors.append(f"{rp.relative_to(ROOT)}: reference too thin ({words})")
            if words > 1800:
                errors.append(f"{rp.relative_to(ROOT)}: reference too large ({words})")

    if seen != EXPECTED:
        errors.append(f"registry mismatch: missing={sorted(EXPECTED-seen)} extra={sorted(seen-EXPECTED)}")

    for i, (a, ad) in enumerate(descriptions):
        for b, bd in descriptions[i + 1:]:
            score = similarity(ad, bd)
            if score > 0.62:
                errors.append(f"possible routing overlap: {a}/{b} ({score:.2f})")

    routing = ROUTING.read_text(encoding="utf-8").lower()
    for marker in ("`ai-engineering`", "`asset-production`", "mandatory gate escalation", "token rule", "r3/r4"):
        if marker not in routing:
            errors.append(f"routing missing marker: {marker}")

    policy = POLICY.read_text(encoding="utf-8").lower()
    for marker in (
        "2026-07-28", "stateless core", "prompt-injection", "least-privilege", "eval evidence",
        "source provenance", "svg", "accessibility", "privacy"
    ):
        if marker not in policy:
            errors.append(f"AI/asset policy missing marker: {marker}")

    evals = EVALS.read_text(encoding="utf-8").lower()
    for marker in ("routing positives", "routing negatives", "edge cases", "quality assertions"):
        if marker not in evals:
            errors.append(f"eval suite missing section: {marker}")

    markers = {
        "ai-engineering": (
            "current sdk", "model ids", "runtime validation", "least privilege", "prompt injection",
            "rag", "eval", "latency", "cost", "mcp", "privacy-compliance"
        ),
        "asset-production": (
            "creative direction", "source", "svg", "responsive", "accessibility", "reduced-motion",
            "provenance", "license", "performance", "frontend"
        ),
    }
    for name, required in markers.items():
        text = (ROOT / f".codex/skills/{name}/SKILL.md").read_text(encoding="utf-8").lower()
        for marker in required:
            if marker not in text:
                errors.append(f"{name} missing quality marker: {marker}")

    mcp = (ROOT / ".codex/skills/ai-engineering/references/mcp-integration.md").read_text(encoding="utf-8").lower()
    for marker in ("2026-07-28", "stateless", "authorization", "version mismatch"):
        if marker not in mcp:
            errors.append(f"MCP reference missing marker: {marker}")

    guardrails = (ROOT / ".codex/skills/ai-engineering/references/evals-guardrails-redteam.md").read_text(encoding="utf-8").lower()
    for marker in ("direct and indirect", "least privilege", "tool", "data exfiltration", "release"):
        if marker not in guardrails:
            errors.append(f"AI eval/guardrail reference missing marker: {marker}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Phase 08 validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Phase 08 validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
