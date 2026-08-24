# Master Benchmark Lab

This directory is the public benchmark contract for AI Expert Engine. It is **not** a hidden test pack. Public scenarios establish reproducible capability coverage; hidden/holdout packs, when used, must be supplied from outside the candidate workspace so a candidate cannot inspect them.

- `config.json` defines 20 weighted quality domains, Quick/Full/Release modes, hard gates and evidence trust.
- `scenarios.json` defines 40 adversarial production scenarios; exactly 8 form the Quick suite.
- `judge-rubric.md` constrains subjective expert scoring.
- `fixtures/reference.html` is a deterministic browser-lab smoke fixture only.

Use `python scripts/expert_benchmark.py validate` and `python scripts/expert_benchmark.py self-test` for offline validation. Full browser probing is performed by `scripts/master_browser_probe.mjs` with Playwright, axe-core, pixelmatch and pngjs installed at exact versions by CI.

Certification is evidence-based. Candidate self-reports cannot satisfy hard gates. Release mode requires five repetitions, all 40 public scenarios, Chromium/Firefox/WebKit coverage, deterministic evidence, expert-judge evidence and release evidence; score variance is penalized.
