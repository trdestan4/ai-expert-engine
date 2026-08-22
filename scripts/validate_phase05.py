#!/usr/bin/env python3
"""Validate Phase 05 quality skill structure and critical quality gates."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "engine/registry/phase-05-skills.json"
POLICY = ROOT / "engine/policies/quality-engineering.md"
ROUTING = ROOT / "engine/routing/phase-05-routing.md"
SCHEMA = ROOT / "engine/schemas/quality-review.schema.json"
EVALS = ROOT / "evals/phase-05-quality.md"
EXPECTED = {"security","privacy-compliance","performance","testing-qa","accessibility","code-quality"}
REQUIRED = ["# Purpose","## Use when","## Do not use when","## Inputs","## Workflow","## Decision rules","## Reference routing","## Quality gates","## Failure handling","## Output contract"]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
WORD_RE = re.compile(r"[a-z][a-z0-9-]{3,}", re.I)


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    out = {}
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
    aa, bb = set(WORD_RE.findall(a.lower())), set(WORD_RE.findall(b.lower()))
    return len(aa & bb) / len(aa | bb) if aa and bb else 0.0


def validate() -> list[str]:
    errors: list[str] = []
    for path in (REGISTRY, POLICY, ROUTING, SCHEMA, EVALS):
        if not path.exists():
            errors.append(f"missing artifact: {path.relative_to(ROOT)}")
    if errors:
        return errors

    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        json.loads(SCHEMA.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"invalid JSON: {exc}"]

    seen, descriptions = set(), []
    for item in registry.get("skills", []):
        name, raw = item.get("name", ""), item.get("path", "")
        path = ROOT / raw
        if name in seen: errors.append(f"duplicate skill: {name}")
        seen.add(name)
        if not NAME_RE.fullmatch(name): errors.append(f"invalid skill name: {name}")
        if not path.exists():
            errors.append(f"missing skill file: {raw}")
            continue
        if path.parent.name != name: errors.append(f"{raw}: folder/name mismatch")
        text = path.read_text(encoding="utf-8")
        try:
            meta = frontmatter(text)
        except ValueError as exc:
            errors.append(f"{raw}: {exc}")
            continue
        if meta.get("name") != name: errors.append(f"{raw}: frontmatter name mismatch")
        desc = meta.get("description", "")
        if not 12 <= len(desc.split()) <= 80: errors.append(f"{raw}: description routing budget invalid")
        descriptions.append((name, desc))
        for heading in REQUIRED:
            if heading not in text: errors.append(f"{raw}: missing {heading}")
        if len(text.split()) > 2200: errors.append(f"{raw}: SKILL.md too large")
        refs = item.get("references", [])
        if not refs: errors.append(f"{raw}: no lazy references")
        for ref in refs:
            rp = path.parent / ref
            if not rp.exists():
                errors.append(f"{raw}: missing reference {ref}")
                continue
            words = len(rp.read_text(encoding="utf-8").split())
            if words < 80: errors.append(f"{rp.relative_to(ROOT)}: reference too thin ({words})")
            if words > 1800: errors.append(f"{rp.relative_to(ROOT)}: reference too large ({words})")

    if seen != EXPECTED:
        errors.append(f"registry mismatch: missing={sorted(EXPECTED-seen)} extra={sorted(seen-EXPECTED)}")

    for i, (a, ad) in enumerate(descriptions):
        for b, bd in descriptions[i+1:]:
            score = similarity(ad, bd)
            if score > 0.62: errors.append(f"possible routing overlap: {a}/{b} ({score:.2f})")

    routing = ROUTING.read_text(encoding="utf-8").lower()
    for name in EXPECTED:
        if f"`{name}`" not in routing: errors.append(f"routing missing {name}")
    for marker in ("mandatory gate escalation","token rule","r3/r4"):
        if marker not in routing: errors.append(f"routing missing marker: {marker}")

    policy = POLICY.read_text(encoding="utf-8").lower()
    for marker in ("asvs 5.0.0","wcag 2.2","lcp <= 2.5s","inp <= 200ms","cls <= 0.1","legal certification","release"):
        if marker not in policy: errors.append(f"quality policy missing marker: {marker}")

    evals = EVALS.read_text(encoding="utf-8").lower()
    for marker in ("routing positives","routing negatives","edge cases","quality assertions"):
        if marker not in evals: errors.append(f"eval suite missing section: {marker}")

    markers = {
        "security": ("trust boundaries","authorization","secrets","supply chain","release"),
        "privacy-compliance": ("minimize","retention","delete","legal","current authoritative"),
        "performance": ("lcp","inp","cls","75th percentile","before/after"),
        "testing-qa": ("negative","contract","e2e","flaky","regression"),
        "accessibility": ("wcag 2.2","keyboard","focus","native","automated"),
        "code-quality": ("refactor","type","dependency","technical debt","behavior")
    }
    for name, required in markers.items():
        text = (ROOT / f".codex/skills/{name}/SKILL.md").read_text(encoding="utf-8").lower()
        for marker in required:
            if marker not in text: errors.append(f"{name} missing quality marker: {marker}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Phase 05 validation FAILED")
        for error in errors: print(f"- {error}")
        return 1
    print("Phase 05 validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
