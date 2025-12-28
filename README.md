# Agent Design Research Monorepo

This repository is an instrumented research monorepo to empirically study agent design paradigms. Its primary objective is to compare role-centric (anthropomorphic) agent specifications against goal-centric (first-principles) agent specifications under controlled, reproducible conditions. Agents in this project are treated as goal-driven control systems — personas or human metaphors are conveniences, not foundations.

Purpose

- Compare role-centric and goal-centric agent specifications across identical tasks, tools, constraints, and evaluation criteria.
- Treat agents as first-class control structures specified by objectives, constraints, inputs, tools, state, and evaluation.

Core principles

- Agents are defined by objectives, constraints, inputs, tools, state, and evaluation.
- Personas, roles, or styles MAY exist only as aliases; they MUST NOT define behavior.
- The system MUST be auditable, reproducible, and comparable across experiments.
- Research velocity MUST NOT compromise experimental rigor.

Plane separation

- Project data plane (root): research artifacts, experiments, runs, and reports.
- SELF control plane (.self): constitution, protocols, workflows, skills (governing law for agents).
- SYSTEM plane (.system): neutral witnessing, recording, and ledgering of activity.

Repository layout (high level)

- harness/ — single canonical instrumentation layer (agents, evaluators, workflows, schemas, skills)
- experiments/ — isolated experiment capsules (e.g., exp-001-role-vs-goal)
- results/ — cross-experiment synthesis and aggregated outputs
- project/ — manifest and governance documents
- .self/ — sovereign control plane (constitution, workflows, and evolution rules)
- .system/ — witness plane (logs, attestations)

See project/manifest.md for the authoritative initialization contract and detailed rules.

Experiment capsule contract (summary)

- Be self-contained within its folder.
- Declare hypotheses and metrics before execution.
- Reference (not copy) harness components.
- Store all outputs under its runs/ directory.
- Be reproducible via pinned manifests.

Mandatory workflows (summary)

- bootstrap — initialize harness and experiment scaffolding
- pin-and-run — create run manifests, snapshot inputs, execute paired variants, dispatch evaluations
- replay — reproduce a run from its manifest
- synthesize — aggregate results and produce reports

Invariants (non-negotiable, summary)

- Pinning: runs MUST pin harness/evaluator versions and tool permission sets.
- Immutability: completed runs are immutable; corrections require new runs.
- Append-only logs: run summaries and violations are appended, never overwritten.
- Scoped writes: agents may write only to the active experiment’s run directory or explicitly allowed scratch space.
- Separation of duties: orchestrators do not execute tasks; executors do not evaluate; evaluators do not mutate project state.

Getting started (brief)

1. Read project/manifest.md (authoritative contract for this repository).
2. Review harness/README.md for instrumentation and harness responsibilities.
3. Create an experiment under experiments/ following the experiment capsule contract.
4. Use the bootstrap and pin-and-run workflows to initialize and execute runs.
5. Use synthesize to aggregate results and produce reports.

Logging & evaluation

- All runs MUST emit a structured run manifest.
- All evaluations MUST emit a scorecard with rationale.
- All violations MUST be recorded explicitly. Silence is considered a failure mode.

Contributing

Contributions are welcome. Ensure proposed changes adhere to the protocols defined in .self/ and are witnessed by the .system/ plane. Refer to AGENTS.md for the execution protocol required for modifications.

Status

Initial experiment: exp-001-role-vs-goal. This project is research-focused and in active development; design recommendations must be evidence-driven.

References

- project/manifest.md (authoritative manifest)
- .self/constitution.md (governing constitution)
