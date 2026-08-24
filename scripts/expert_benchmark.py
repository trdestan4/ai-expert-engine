#!/usr/bin/env python3
"""Provider-neutral Master Benchmark orchestration and certification."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import shlex
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks/master"
CONFIG = BENCH / "config.json"
SCENARIOS = BENCH / "scenarios.json"
SENSITIVE = ("TOKEN", "SECRET", "PASSWORD", "PASSWD", "PRIVATE_KEY", "API_KEY", "AUTH")


class BenchmarkError(RuntimeError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise BenchmarkError(f"invalid JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise BenchmarkError(f"{path} must contain an object")
    return value


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha256_value(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def inside(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def validate_hidden_pack_path(candidate_root: Path, hidden_pack: Path | None) -> None:
    if hidden_pack is None:
        return
    if not hidden_pack.exists():
        raise BenchmarkError(f"hidden pack does not exist: {hidden_pack}")
    if inside(hidden_pack, candidate_root):
        raise BenchmarkError("hidden benchmark pack must reside outside candidate workspace")


def sanitized_environment(extra: dict[str, str] | None = None) -> dict[str, str]:
    env: dict[str, str] = {}
    for key, value in os.environ.items():
        upper = key.upper()
        if any(fragment in upper for fragment in SENSITIVE):
            continue
        if key.startswith(("AI_EXPERT_", "CI", "GITHUB_", "LC_")) or key in {"PATH", "HOME", "USER", "TMP", "TEMP", "LANG"}:
            env[key] = value
    if extra:
        env.update({str(k): str(v) for k, v in extra.items()})
    return env


def parse_command(command: str | list[str]) -> list[str]:
    parts = [str(x) for x in command] if isinstance(command, list) else shlex.split(command)
    if not parts:
        raise BenchmarkError("candidate command is empty")
    if Path(parts[0]).name.lower() in {"sudo", "su", "doas"}:
        raise BenchmarkError("privileged candidate command is not allowed")
    return parts


def run_command(command: str | list[str], cwd: Path, timeout: int, extra_env: dict[str, str] | None = None) -> dict[str, Any]:
    argv = parse_command(command)
    started = time.monotonic()
    try:
        proc = subprocess.run(argv, cwd=cwd, env=sanitized_environment(extra_env), text=True, capture_output=True, timeout=timeout, shell=False)
    except subprocess.TimeoutExpired as exc:
        raise BenchmarkError(f"candidate command timed out after {timeout}s") from exc
    return {
        "argv": argv,
        "returncode": proc.returncode,
        "duration_ms": int((time.monotonic() - started) * 1000),
        "stdout_tail": (proc.stdout or "")[-6000:],
        "stderr_tail": (proc.stderr or "")[-6000:],
    }


def environment_fingerprint(candidate_root: Path) -> dict[str, Any]:
    markers: dict[str, str] = {}
    for rel in ("package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock", "pyproject.toml", "requirements.txt"):
        p = candidate_root / rel
        if p.is_file():
            markers[rel] = file_sha256(p)
    value = {"platform": platform.platform(), "python": platform.python_version(), "machine": platform.machine(), "candidate_root_name": candidate_root.name, "markers": markers}
    value["fingerprint_sha256"] = sha256_value(value)
    return value


def validate_pack(config: dict[str, Any], scenarios_doc: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    domains = config.get("domains", [])
    scenarios = scenarios_doc.get("scenarios", [])
    ids = [d.get("id") for d in domains if isinstance(d, dict)]
    if len(domains) != config.get("domain_count"):
        errors.append("domain_count does not match domains")
    if len(ids) != len(set(ids)):
        errors.append("duplicate domain id")
    weight = sum(float(d.get("weight", 0)) for d in domains if isinstance(d, dict))
    if not math.isclose(weight, 100.0, abs_tol=1e-9):
        errors.append(f"domain weights must total 100, got {weight}")
    sids = [s.get("id") for s in scenarios if isinstance(s, dict)]
    if len(scenarios) != config.get("scenario_count"):
        errors.append("scenario_count does not match scenarios")
    if len(sids) != len(set(sids)):
        errors.append("duplicate scenario id")
    known = set(ids)
    quick = 0
    for scenario in scenarios:
        if not isinstance(scenario, dict):
            errors.append("scenario is not an object")
            continue
        quick += int(bool(scenario.get("quick")))
        unknown = set(scenario.get("required_domains", [])) - known
        if unknown:
            errors.append(f"{scenario.get('id')}: unknown domains {sorted(unknown)}")
        if not scenario.get("prompt"):
            errors.append(f"{scenario.get('id')}: missing prompt")
    quick_limit = int(config.get("modes", {}).get("quick", {}).get("scenario_limit", 0))
    if quick != quick_limit:
        errors.append(f"quick scenario count must equal {quick_limit}, got {quick}")
    for mode in ("quick", "full", "release"):
        if int(config.get("modes", {}).get(mode, {}).get("repetitions", 0)) < 1:
            errors.append(f"{mode}: invalid repetitions")
    return errors


def clamp_score(value: Any) -> float:
    try:
        n = float(value)
    except (TypeError, ValueError) as exc:
        raise BenchmarkError(f"invalid score {value!r}") from exc
    return min(100.0, max(0.0, n))


def domain_score(det: Any, expert: Any, det_weight: float, expert_weight: float) -> tuple[float | None, str]:
    if det is None and expert is None:
        return None, "missing"
    if det is not None and expert is not None:
        return round(clamp_score(det) * det_weight + clamp_score(expert) * expert_weight, 3), "mixed"
    if det is not None:
        return round(clamp_score(det), 3), "deterministic"
    return round(clamp_score(expert), 3), "expert-only"


def collect_hard_gate_failures(evidence: dict[str, Any], config: dict[str, Any]) -> list[str]:
    gates = evidence.get("hard_gates", {})
    out: list[str] = []
    for gate in config.get("hard_gates", []):
        if gates.get(gate) is False:
            out.append(gate)
        elif gates.get(gate) is None:
            out.append(gate + ":missing")
    return out


def required_evidence_missing(evidence: dict[str, Any], config: dict[str, Any], mode: str) -> list[str]:
    available = evidence.get("evidence_types", {})
    return [name for name in config["modes"][mode]["required_evidence"] if not available.get(name)]


def score_evidence(evidence: dict[str, Any], config: dict[str, Any], mode: str) -> dict[str, Any]:
    det_weight = float(config["scoring"]["deterministic_weight"])
    expert_weight = float(config["scoring"]["expert_weight"])
    if not math.isclose(det_weight + expert_weight, 1.0, abs_tol=1e-9):
        raise BenchmarkError("scoring weights must total 1")
    deterministic = evidence.get("deterministic_scores", {})
    expert = evidence.get("expert_scores", {})
    weighted = covered = 0.0
    results = []
    missing_domains = []
    for domain in config["domains"]:
        did = domain["id"]
        score, source = domain_score(deterministic.get(did), expert.get(did), det_weight, expert_weight)
        if score is None:
            missing_domains.append(did)
            continue
        weight = float(domain["weight"])
        weighted += score * weight
        covered += weight
        results.append({"id": did, "score": score, "weight": weight, "source": source})
    hard = collect_hard_gate_failures(evidence, config)
    missing_types = required_evidence_missing(evidence, config, mode)
    if mode in {"full", "release"} and missing_domains:
        hard.append("required-domain-coverage")
    return {"raw_score": round(weighted / covered if covered else 0.0, 3), "domain_results": results, "missing_domains": missing_domains, "missing_evidence_types": missing_types, "hard_gate_failures": hard, "eligible": not hard and not missing_types}


def variance_penalty(scores: Iterable[float], config: dict[str, Any]) -> tuple[float, float]:
    values = [float(x) for x in scores]
    if len(values) < 2:
        return 0.0, 0.0
    stdev = statistics.pstdev(values)
    rule = config["scoring"]["variance_penalty"]
    return round(stdev, 3), round(min(float(rule["max_points"]), stdev / float(rule["stdev_divisor"])), 3)


def certify_runs(runs: list[dict[str, Any]], config: dict[str, Any], mode: str) -> dict[str, Any]:
    expected = int(config["modes"][mode]["repetitions"])
    if len(runs) != expected:
        raise BenchmarkError(f"{mode} requires exactly {expected} runs, received {len(runs)}")
    scored = [score_evidence(run, config, mode) for run in runs]
    raw = [x["raw_score"] for x in scored]
    stdev, penalty = variance_penalty(raw, config)
    average = statistics.fmean(raw)
    final = max(0.0, average - penalty)
    gates = sorted({g for x in scored for g in x["hard_gate_failures"]})
    missing = sorted({g for x in scored for g in x["missing_evidence_types"]})
    eligible = not gates and not missing and all(x["eligible"] for x in scored)
    if not eligible:
        status = "FAIL"
    elif final >= float(config["certification"]["master_score"]):
        status = "MASTER"
    elif final >= float(config["certification"]["minimum_score"]):
        status = "PASS"
    else:
        status = "FAIL"
    return {"mode": mode, "runs": scored, "average_raw_score": round(average, 3), "stdev": stdev, "variance_penalty": penalty, "final_score": round(final, 3), "status": status, "eligible": eligible, "hard_gate_failures": gates, "missing_evidence_types": missing}


def verify_evidence_integrity(evidence: dict[str, Any], candidate_root: Path) -> list[str]:
    errors: list[str] = []
    claimed = evidence.get("environment_fingerprint_sha256")
    actual = environment_fingerprint(candidate_root)["fingerprint_sha256"]
    if claimed and claimed != actual:
        errors.append("environment-fingerprint-mismatch")
    files = evidence.get("evidence_files", {})
    if isinstance(files, dict):
        for rel, expected in files.items():
            p = (candidate_root / rel).resolve()
            if not inside(p, candidate_root):
                errors.append("evidence-path-escape:" + rel)
            elif not p.is_file():
                errors.append("evidence-missing:" + rel)
            elif file_sha256(p) != expected:
                errors.append("evidence-hash-mismatch:" + rel)
    return errors


def compare_baseline(report: dict[str, Any], baseline: dict[str, Any]) -> dict[str, Any]:
    current = float(report.get("final_score", 0))
    previous = float(baseline.get("final_score", 0))
    delta = current - previous
    return {"baseline_score": previous, "current_score": current, "delta": round(delta, 3), "regression": delta < -1.0, "material_improvement": delta > 1.0}


def build_self_test_evidence(config: dict[str, Any], score: float = 97.0) -> dict[str, Any]:
    return {"evidence_types": {"functional": True, "probe": True, "static": True, "tests": True, "expert_judge": True, "release": True}, "hard_gates": {g: True for g in config["hard_gates"]}, "deterministic_scores": {d["id"]: score for d in config["domains"]}, "expert_scores": {d["id"]: score for d in config["domains"]}}


def candidate_adapter_run(command: str, candidate_root: Path, scenario: dict[str, Any], output_dir: Path, timeout: int) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    scenario_path = output_dir / "scenario.json"
    result_path = output_dir / "candidate-result.json"
    scenario_path.write_text(json.dumps(scenario, indent=2) + "\n")
    extra = {"AI_EXPERT_BENCH_SCENARIO": str(scenario_path), "AI_EXPERT_BENCH_WORKSPACE": str(candidate_root.resolve()), "AI_EXPERT_BENCH_OUTPUT": str(result_path)}
    result = run_command(command, candidate_root, timeout, extra)
    candidate = None
    if result_path.is_file():
        try:
            candidate = json.loads(result_path.read_text())
        except Exception as exc:
            candidate = {"invalid_candidate_result": str(exc)}
    return {"scenario_id": scenario["id"], "command": result, "candidate_result": candidate}


def cmd_validate() -> int:
    config, scenarios = load_json(CONFIG), load_json(SCENARIOS)
    errors = validate_pack(config, scenarios)
    if errors:
        print("Master benchmark pack INVALID")
        for e in errors:
            print(" -", e)
        return 1
    print(f"Master benchmark pack valid: {len(scenarios['scenarios'])} scenarios / {len(config['domains'])} domains")
    return 0


def cmd_self_test() -> int:
    config, scenarios = load_json(CONFIG), load_json(SCENARIOS)
    errors = validate_pack(config, scenarios)
    if errors:
        raise BenchmarkError("; ".join(errors))
    runs = [build_self_test_evidence(config, 97 - (i % 2) * .4) for i in range(5)]
    if certify_runs(runs, config, "release")["status"] != "MASTER":
        raise BenchmarkError("release self-test did not reach MASTER")
    failed = build_self_test_evidence(config, 100)
    failed["hard_gates"]["security-blocker"] = False
    if certify_runs([failed], config, "quick")["status"] != "FAIL":
        raise BenchmarkError("hard gate failed to override score")
    with tempfile.TemporaryDirectory() as td:
        candidate = Path(td) / "candidate"; candidate.mkdir()
        hidden = candidate / "hidden.json"; hidden.write_text("{}")
        try:
            validate_hidden_pack_path(candidate, hidden)
        except BenchmarkError:
            pass
        else:
            raise BenchmarkError("hidden-pack isolation test failed")
    print("Master benchmark self-test PASSED")
    print("40 scenarios / 20 domains / release repetitions=5")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    sub.add_parser("self-test")
    c = sub.add_parser("certify"); c.add_argument("--mode", choices=("quick","full","release"), required=True); c.add_argument("--run", action="append", required=True); c.add_argument("--output", required=True); c.add_argument("--candidate-root"); c.add_argument("--baseline")
    a = sub.add_parser("adapter"); a.add_argument("--mode", choices=("quick","full","release"), required=True); a.add_argument("--command", required=True); a.add_argument("--candidate-root", required=True); a.add_argument("--output-dir", required=True); a.add_argument("--hidden-pack"); a.add_argument("--timeout", type=int, default=900); a.add_argument("--keep-going", action="store_true")
    p = sub.add_parser("promote-baseline"); p.add_argument("--report", required=True); p.add_argument("--destination", required=True); p.add_argument("--force", action="store_true")
    args = ap.parse_args()
    try:
        if args.cmd == "validate": return cmd_validate()
        if args.cmd == "self-test": return cmd_self_test()
        config = load_json(CONFIG)
        if args.cmd == "certify":
            paths = [Path(x) for x in args.run]; runs = [load_json(x) for x in paths]
            report = certify_runs(runs, config, args.mode)
            report["run_hashes"] = {str(x): file_sha256(x) for x in paths}
            if args.candidate_root:
                root = Path(args.candidate_root).resolve(); report["environment"] = environment_fingerprint(root)
                failures = sorted({e for run in runs for e in verify_evidence_integrity(run, root)})
                if failures: report.update({"integrity_failures": failures, "status": "FAIL", "eligible": False})
            if args.baseline:
                report["baseline_comparison"] = compare_baseline(report, load_json(Path(args.baseline)))
                if report["baseline_comparison"]["regression"]: report.update({"status":"FAIL","eligible":False})
            report["report_sha256"] = sha256_value(report)
            out = Path(args.output); out.parent.mkdir(parents=True, exist_ok=True); out.write_text(json.dumps(report, indent=2) + "\n")
            print(f"{report['status']} score={report['final_score']:.3f} mode={args.mode}")
            return 0 if report["status"] in {"PASS","MASTER"} else 1
        if args.cmd == "adapter":
            root = Path(args.candidate_root).resolve(); hidden = Path(args.hidden_pack).resolve() if args.hidden_pack else None
            if not root.exists(): raise BenchmarkError("candidate root does not exist")
            validate_hidden_pack_path(root, hidden)
            scenarios = load_json(SCENARIOS)["scenarios"]
            scenarios = [s for s in scenarios if s.get("quick")] if args.mode == "quick" else scenarios[:config["modes"][args.mode]["scenario_limit"]]
            out = Path(args.output_dir).resolve(); out.mkdir(parents=True, exist_ok=True)
            results = []
            for scenario in scenarios:
                r = candidate_adapter_run(args.command, root, scenario, out / scenario["id"], args.timeout); results.append(r)
                if r["command"]["returncode"] and not args.keep_going: break
            summary = {"mode": args.mode, "environment": environment_fingerprint(root), "results": results}; summary["summary_sha256"] = sha256_value(summary)
            (out / "adapter-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
            failures = sum(1 for r in results if r["command"]["returncode"])
            print(f"adapter completed scenarios={len(results)} failures={failures}")
            return 1 if failures else 0
        if args.cmd == "promote-baseline":
            report_path = Path(args.report).resolve(); report = load_json(report_path); dest = Path(args.destination).resolve()
            if report.get("status") not in {"PASS","MASTER"} or not report.get("eligible"): raise BenchmarkError("only eligible PASS/MASTER reports may be promoted")
            if dest.exists() and not args.force: raise BenchmarkError("baseline exists; use --force for intentional replacement")
            dest.parent.mkdir(parents=True, exist_ok=True)
            promoted = {"source_sha256": file_sha256(report_path), "final_score": report["final_score"], "status": report["status"], "mode": report["mode"], "report_sha256": report.get("report_sha256"), "promoted_at_unix": int(time.time())}
            dest.write_text(json.dumps(promoted, indent=2) + "\n"); print(f"baseline promoted: {dest}"); return 0
        raise BenchmarkError("unknown command")
    except BenchmarkError as exc:
        print(f"benchmark error: {exc}", file=sys.stderr); return 2


if __name__ == "__main__":
    raise SystemExit(main())
