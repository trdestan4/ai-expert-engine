# Master Benchmark Lab

The Master Benchmark Lab evaluates whether AI Expert Engine work remains expert-level under difficult production scenarios rather than only passing structural skill checks.

## Trust model

The benchmark separates **candidate output**, **deterministic evidence**, **browser evidence**, **expert judgment**, and **release evidence**. Candidate-authored pass/score claims are advisory. Hard gates are deterministic and cannot be overridden by an expert judge. Evidence files can be SHA-256 pinned and tied to an environment fingerprint. Hidden packs must live outside the candidate workspace; committing a hidden pack under `benchmarks/master` is itself a validation failure.

## Modes

**Quick** runs 8 representative scenarios once in Chromium and is intended for fast local regression. **Full** runs all 40 public scenarios three times and requires Chromium, Firefox and WebKit plus static/tests/expert evidence. **Release** runs all 40 scenarios five times, requires release evidence, and applies the configured variance penalty before certification.

The certification thresholds are 90 for PASS and 95 for MASTER. A high numeric score cannot rescue a failed hard gate, missing required evidence type, missing Full/Release domain coverage, evidence hash mismatch, environment mismatch, hidden-pack leakage, or material baseline regression.

## Candidate adapter

The provider-neutral adapter command is executed with `shell=False` in the candidate workspace. It receives `AI_EXPERT_BENCH_SCENARIO`, `AI_EXPERT_BENCH_WORKSPACE`, and `AI_EXPERT_BENCH_OUTPUT`. Sensitive environment variables are stripped and privilege wrappers such as `sudo`, `su`, and `doas` are rejected. Candidate result JSON is not trusted certification evidence by itself.

```bash
python scripts/expert_benchmark.py adapter \
  --mode quick \
  --command "python my_candidate_adapter.py" \
  --candidate-root /tmp/candidate \
  --output-dir /tmp/bench
```

For a holdout pack, pass `--hidden-pack /secure/holdout-pack.json`. The path is rejected if it resolves inside the candidate workspace.

## Browser lab

The browser probe records navigation status, runtime/console errors, semantic signals, resource/transfer counts, layout-shift/long-task/LCP signals, horizontal overflow, axe-core accessibility findings, reduced-motion media behavior, WebGL capability, screenshots and optional pixel diffs.

```bash
node scripts/master_browser_probe.mjs \
  --url http://127.0.0.1:4173 \
  --browser all \
  --screenshots-dir /tmp/screens \
  --output /tmp/browser-probe.json
```

Baseline updates are explicit. `--update-baseline` is never performed automatically by certification.

## Certification input

Each evidence JSON contains evidence-type availability, all hard-gate states, deterministic domain scores, expert domain scores and optionally candidate/environment/evidence-file hashes. Full/Release require all 20 domain scores. Deterministic and expert scores mix at 70/30. An expert score of 100 paired with a deterministic score of 0 produces only 30 and can never erase a hard-gate failure.

## Regression baseline

An eligible PASS/MASTER report may be promoted deliberately:

```bash
python scripts/expert_benchmark.py promote-baseline \
  --report /tmp/report.json \
  --destination benchmarks/baselines/current.json
```

Existing baselines are not overwritten unless `--force` is explicitly supplied. Certification with `--baseline` fails for regression greater than one point.

## Validation and CI

`validate_master_benchmark.py` validates the 40-scenario corpus, 20 weighted domains, exact repetition counts, three-browser release coverage, action/dependency pinning, absence of committed hidden packs, Python/Node syntax, unit tests and deterministic self-test. The dedicated GitHub Actions workflow additionally installs exact browser-lab dependencies and executes the fixture in Chromium, Firefox and WebKit.
