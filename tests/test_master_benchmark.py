from __future__ import annotations
import importlib.util
import os
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("expert_benchmark", ROOT / "scripts/expert_benchmark.py")
assert SPEC and SPEC.loader
bench = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bench)


class MasterBenchmarkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = bench.load_json(ROOT / "benchmarks/master/config.json")
        cls.scenarios = bench.load_json(ROOT / "benchmarks/master/scenarios.json")

    def test_pack_shape(self):
        self.assertEqual([], bench.validate_pack(self.config, self.scenarios))
        self.assertEqual(40, len(self.scenarios["scenarios"]))
        self.assertEqual(20, len(self.config["domains"]))
        self.assertEqual(100, sum(x["weight"] for x in self.config["domains"]))
        self.assertEqual(8, sum(1 for x in self.scenarios["scenarios"] if x["quick"]))

    def test_release_repeats_five_times(self):
        self.assertEqual(5, self.config["modes"]["release"]["repetitions"])

    def test_high_score_cannot_override_security_gate(self):
        evidence = bench.build_self_test_evidence(self.config, 100)
        evidence["hard_gates"]["security-blocker"] = False
        report = bench.certify_runs([evidence], self.config, "quick")
        self.assertEqual("FAIL", report["status"])
        self.assertIn("security-blocker", report["hard_gate_failures"])

    def test_missing_hard_gate_fails(self):
        evidence = bench.build_self_test_evidence(self.config, 100)
        evidence["hard_gates"].pop("testing-integrity")
        report = bench.certify_runs([evidence], self.config, "quick")
        self.assertIn("testing-integrity:missing", report["hard_gate_failures"])

    def test_release_requires_expert_evidence(self):
        runs = []
        for _ in range(5):
            evidence = bench.build_self_test_evidence(self.config, 98)
            evidence["evidence_types"]["expert_judge"] = False
            runs.append(evidence)
        report = bench.certify_runs(runs, self.config, "release")
        self.assertEqual("FAIL", report["status"])
        self.assertIn("expert_judge", report["missing_evidence_types"])

    def test_variance_penalty(self):
        stable = [bench.build_self_test_evidence(self.config, 96) for _ in range(5)]
        variable = [bench.build_self_test_evidence(self.config, x) for x in (100, 92, 100, 92, 100)]
        self.assertGreater(bench.certify_runs(variable, self.config, "release")["variance_penalty"], bench.certify_runs(stable, self.config, "release")["variance_penalty"])

    def test_hidden_pack_inside_candidate_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            candidate = Path(td) / "candidate"; candidate.mkdir()
            hidden = candidate / "holdout.json"; hidden.write_text("{}")
            with self.assertRaises(bench.BenchmarkError):
                bench.validate_hidden_pack_path(candidate, hidden)

    def test_hidden_pack_outside_candidate_is_allowed(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td); candidate = base / "candidate"; candidate.mkdir()
            hidden = base / "holdout.json"; hidden.write_text("{}")
            bench.validate_hidden_pack_path(candidate, hidden)

    def test_environment_sanitizer_drops_secrets(self):
        old = dict(os.environ)
        try:
            os.environ["AI_EXPERT_VISIBLE"] = "ok"
            os.environ["MY_API_KEY"] = "no"
            os.environ["GITHUB_TOKEN"] = "no"
            env = bench.sanitized_environment()
            self.assertEqual("ok", env.get("AI_EXPERT_VISIBLE"))
            self.assertNotIn("MY_API_KEY", env)
            self.assertNotIn("GITHUB_TOKEN", env)
        finally:
            os.environ.clear(); os.environ.update(old)

    def test_privileged_command_is_rejected(self):
        with self.assertRaises(bench.BenchmarkError):
            bench.parse_command("sudo echo nope")

    def test_environment_fingerprint_changes_with_manifest(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); p = root / "package.json"
            p.write_text('{"name":"a"}')
            one = bench.environment_fingerprint(root)["fingerprint_sha256"]
            p.write_text('{"name":"b"}')
            two = bench.environment_fingerprint(root)["fingerprint_sha256"]
            self.assertNotEqual(one, two)

    def test_evidence_hash_tampering_is_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); artifact = root / "artifact.txt"; artifact.write_text("good")
            evidence = {"evidence_files":{"artifact.txt":bench.file_sha256(artifact)}}
            self.assertEqual([], bench.verify_evidence_integrity(evidence, root))
            artifact.write_text("tampered")
            self.assertIn("evidence-hash-mismatch:artifact.txt", bench.verify_evidence_integrity(evidence, root))

    def test_evidence_path_escape_is_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "candidate"; root.mkdir()
            self.assertIn("evidence-path-escape:../outside.txt", bench.verify_evidence_integrity({"evidence_files":{"../outside.txt":"x"}}, root))

    def test_baseline_regression(self):
        self.assertTrue(bench.compare_baseline({"final_score":92}, {"final_score":95})["regression"])

    def test_small_baseline_noise_is_not_regression(self):
        self.assertFalse(bench.compare_baseline({"final_score":94.5}, {"final_score":95})["regression"])

    def test_expert_score_cannot_erase_zero_deterministic_score(self):
        score, source = bench.domain_score(0, 100, .7, .3)
        self.assertEqual("mixed", source)
        self.assertEqual(30.0, score)

    def test_full_requires_all_domain_coverage(self):
        runs = []
        for _ in range(3):
            e = bench.build_self_test_evidence(self.config, 98)
            e["deterministic_scores"].pop("architecture")
            e["expert_scores"].pop("architecture")
            runs.append(e)
        report = bench.certify_runs(runs, self.config, "full")
        self.assertEqual("FAIL", report["status"])
        self.assertIn("required-domain-coverage", report["hard_gate_failures"])

    def test_release_can_reach_master_with_complete_evidence(self):
        runs = [bench.build_self_test_evidence(self.config, 97) for _ in range(5)]
        report = bench.certify_runs(runs, self.config, "release")
        self.assertEqual("MASTER", report["status"])
        self.assertTrue(report["eligible"])

    def test_adapter_records_nonzero_candidate_exit(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); out = root / "out"
            result = bench.candidate_adapter_run(f"{os.sys.executable} -c 'import sys;sys.exit(3)'", root, self.scenarios["scenarios"][0], out, 30)
            self.assertEqual(3, result["command"]["returncode"])


if __name__ == "__main__":
    unittest.main()
