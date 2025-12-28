# Execution plan — exp-001-role-vs-goal

Summary: concise, actionable 12-step experiment plan to fully execute exp-001-role-vs-goal (role-centric vs goal-centric agent specs) consistent with project/manifest.md (pre-register hypotheses & metrics, pin versions, use pin-and-run/pilot/replay/synthesize workflows, ≥10 paired runs, immutable runs, append-only logs).

1. Pre-register hypotheses & analysis plan
- Action: Write explicit hypotheses, primary/secondary metrics, statistical tests, minimum sample size (≥10 paired runs), success thresholds into experiments/exp-001-role-vs-goal/research.md.
- Deliverable: Locked pre-registration section.
- Exit criteria: Pre-registration exists and is committed before any pinned run.

2. Define & freeze task suite
- Action: Create deterministic task specs (id, inputs, seeds, timeouts, expected outputs) in experiments/.../tasks.
- Deliverable: Task suite with sample inputs and deterministic seed policies.
- Exit criteria: Task smoke-tests pass deterministically for fixed seeds.

3. Implement variant specs (parity-first)
- Action: Add two variant descriptors in variants/ — role-centric and goal-centric — that reference harness agents/tools; ensure only the specification paradigm differs.
- Deliverable: Two variant files and a small parity-check script.
- Exit criteria: Parity check confirms identical tooling, constraints, permissions.

4. Instrument evaluation and metrics
- Action: Ensure harness/evaluators produce all pre-registered metrics (task success, constraint adherence, #clarifications, runtime, reproducibility stats); pin evaluator versions.
- Deliverable: Evaluator config and scoring rubrics.
- Exit criteria: Evaluators produce deterministic, reproducible scorecards on a sample run.

5. Prepare run manifest & pinning template
- Action: Create run-manifest template (pins: harness version, evaluator versions, tool permission set, variant id, seed policy).
- Deliverable: Manifest template and pre-run validator.
- Exit criteria: Manifest passes schema validation and pre-run checks.

6. Pilot paired runs
- Action: Execute 1–2 paired runs over a small task subset to validate instrument and workflow (pin-and-run → run → evaluate).
- Deliverable: Pilot run artifacts and issue log.
- Exit criteria: No critical gaps; evaluator outputs acceptable; workflows validated.

7. Execute full paired runs
- Action: Run ≥10 paired runs (same inputs/seeds per pair), using pin-and-run to materialize each run in runs/.
- Deliverable: Complete set of run artifacts and scorecards.
- Exit criteria: ≥10 validated paired runs completed and immutable.

8. Real-time QA & violation handling
- Action: After each run, validate manifests and scorecards; if constraint violation occurs, log it and follow remediation/re-run policy.
- Deliverable: QA log entries and resolution notes.
- Exit criteria: All critical violations resolved or recorded with rationale.

9. Aggregate & analyze results
- Action: Use synthesize workflow to aggregate scorecards, compute effect sizes, confidence intervals, and perform the pre-registered statistical tests (paired tests).
- Deliverable: Aggregate dataset, analysis notebook, visualizations.
- Exit criteria: Analysis reproducible and passes QC.

10. Produce comparative report
- Action: Write experiments/exp-001-role-vs-goal/report/ comparative report with methods, results, visualizations, raw data links, and evidence-based recommendations.
- Deliverable: Final report markdown and attached scorecards/manifests.
- Exit criteria: Report meets project termination condition and documents uncertainties/limitations.

11. Replay & reproducibility checks
- Action: Replay selected runs with replay workflow to confirm reproducibility; compare outputs to originals.
- Deliverable: Replay artifacts and discrepancy analysis.
- Exit criteria: Reproduced runs match within declared tolerances or anomalies explained.

12. Close experiment & archive outputs
- Action: Verify termination conditions (≥10 paired runs, reproducibility, report), move final artifacts to results/ if applicable, append lessons learned, and propose follow-ups.
- Deliverable: Closure note, archived manifests, and proposed next experiments.
- Exit criteria: Experiment marked complete in repo and logs; follow-up tasks created.

Notes / constraints (must follow)
- Always pin harness/evaluator/tool versions per project manifest.
- Keep runs immutable and logs append-only; store everything under experiments/exp-001-role-vs-goal/runs/.
- Pre-register analysis before first pinned run to avoid bias.
- Pairing policy: use identical seeds/inputs per pair and interleave runs to reduce temporal bias.
- Use execution-logger for each autonomous step and ensure run manifests and scorecards are emitted.

Estimated effort: prep & pilot (1–3 days), full runs + validation (1–4 days, dependent on per-run latency), analysis & report (1–3 days).

If you want, I can begin by (A) drafting the pre-registered hypotheses & metrics in experiments/exp-001-role-vs-goal/research.md and (B) scaffolding the run-manifest template — tell me to proceed and I will start.