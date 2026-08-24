#!/usr/bin/env python3
"""Validate the Master Benchmark Lab without requiring browser packages."""
from __future__ import annotations

import ast
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks/master"
REQUIRED = [
    BENCH / "config.json",
    BENCH / "scenarios.json",
    BENCH / "judge-rubric.md",
    BENCH / "README.md",
    BENCH / "fixtures/reference.html",
    ROOT / "scripts/expert_benchmark.py",
    ROOT / "scripts/master_browser_probe.mjs",
    ROOT / "tests/test_master_benchmark.py",
    ROOT / "docs/MASTER_BENCHMARK.md",
    ROOT / ".github/workflows/master-benchmark.yml",
]
SHA = re.compile(r"^[0-9a-f]{40}$")
USES = re.compile(r"^\s*-?\s*uses:\s*([^@\s]+)@([^\s#]+)", re.M)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def fail(errors: list[str]) -> int:
    print("Master benchmark validation FAILED")
    for error in errors:
        print(" -", error)
    return 1


def main() -> int:
    errors: list[str] = []
    for path in REQUIRED:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")
    if errors:
        return fail(errors)
    try:
        config = load(BENCH / "config.json")
        scenarios = load(BENCH / "scenarios.json")
        ast.parse((ROOT / "scripts/expert_benchmark.py").read_text())
        ast.parse((ROOT / "tests/test_master_benchmark.py").read_text())
    except Exception as exc:
        return fail([f"parse failure: {exc}"])

    if config.get("scenario_count") != 40:
        errors.append("scenario_count must be 40")
    if config.get("domain_count") != 20:
        errors.append("domain_count must be 20")
    domains = config.get("domains", [])
    if len(domains) != 20 or len({x.get("id") for x in domains}) != 20:
        errors.append("20 unique domains required")
    if sum(float(x.get("weight", 0)) for x in domains) != 100:
        errors.append("domain weights must total 100")
    if config.get("modes", {}).get("quick", {}).get("repetitions") != 1:
        errors.append("quick mode must repeat once")
    if config.get("modes", {}).get("full", {}).get("repetitions") != 3:
        errors.append("full mode must repeat three times")
    if config.get("modes", {}).get("release", {}).get("repetitions") != 5:
        errors.append("release mode must repeat five times")
    if set(config.get("modes", {}).get("release", {}).get("browsers", [])) != {"chromium", "firefox", "webkit"}:
        errors.append("release browser matrix must contain Chromium, Firefox and WebKit")
    if len(config.get("hard_gates", [])) < 7:
        errors.append("hard gate set unexpectedly shallow")

    cases = scenarios.get("scenarios", [])
    if len(cases) != 40:
        errors.append("exactly 40 public benchmark scenarios required")
    if len({x.get("id") for x in cases}) != len(cases):
        errors.append("scenario ids must be unique")
    if sum(1 for x in cases if x.get("quick")) != 8:
        errors.append("quick suite must contain exactly 8 scenarios")
    known = {x.get("id") for x in domains}
    for case in cases:
        missing = set(case.get("required_domains", [])) - known
        if missing:
            errors.append(f"{case.get('id')}: unknown domains {sorted(missing)}")
        if case.get("risk") not in {"R0", "R1", "R2", "R3", "R4"}:
            errors.append(f"{case.get('id')}: invalid risk")
        if "fabricated_measurement" not in case.get("acceptance", {}).get("forbidden", []):
            errors.append(f"{case.get('id')}: fabricated measurement guard missing")

    forbidden_hidden = [p for p in BENCH.rglob("*") if p.is_file() and any(token in p.name.lower() for token in ("hidden", "secret-pack", "private-pack"))]
    if forbidden_hidden:
        errors.append("hidden/private packs must not be committed under candidate-visible benchmark root")

    workflow = (ROOT / ".github/workflows/master-benchmark.yml").read_text()
    for action, version in USES.findall(workflow):
        if not action.startswith("./") and not SHA.fullmatch(version):
            errors.append(f"workflow action is not SHA-pinned: {action}@{version}")
    for dependency in ("playwright@1.55.0", "@axe-core/playwright@4.10.2", "pixelmatch@7.1.0", "pngjs@7.0.0"):
        if dependency not in workflow:
            errors.append(f"workflow dependency is not exact-pinned: {dependency}")

    if shutil.which("node"):
        proc = subprocess.run(["node", "--check", "scripts/master_browser_probe.mjs"], cwd=ROOT, text=True, capture_output=True)
        if proc.returncode:
            errors.append("browser probe syntax failed: " + (proc.stderr or proc.stdout).strip())

    spec = importlib.util.spec_from_file_location("expert_benchmark", ROOT / "scripts/expert_benchmark.py")
    if not spec or not spec.loader:
        errors.append("cannot import expert_benchmark")
    else:
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            errors.extend(module.validate_pack(config, scenarios))
        except Exception as exc:
            errors.append(f"benchmark module load failed: {exc}")

    unit = subprocess.run([sys.executable, "-m", "unittest", "tests/test_master_benchmark.py"], cwd=ROOT, text=True, capture_output=True)
    if unit.returncode:
        errors.append("benchmark unit tests failed:\n" + (unit.stdout + unit.stderr)[-5000:])
    smoke = subprocess.run([sys.executable, "scripts/expert_benchmark.py", "self-test"], cwd=ROOT, text=True, capture_output=True)
    if smoke.returncode:
        errors.append("benchmark self-test failed:\n" + (smoke.stdout + smoke.stderr)[-5000:])

    if errors:
        return fail(errors)
    print("Master benchmark validation PASSED: 40 scenarios / 20 domains / 3 browsers / release x5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
