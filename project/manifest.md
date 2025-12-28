# project/manifest.md

## PROJECT MANIFEST — AGENT DESIGN RESEARCH MONOREPO

### Authority
This document is the authoritative initialization contract for this project.  
It defines purpose, structure, invariants, and operating rules.  
All agents and workflows MUST comply with this document.  
If a conflict exists, this document prevails.

---

## 1. Purpose

This project establishes a research monorepo to empirically study agent design paradigms.

The primary objective is to compare **role-centric (anthropomorphic)** agent specifications against **goal-centric (first-principles)** agent specifications under controlled, reproducible conditions.

Agents in this project are treated as **goal-driven control systems**, not simulated human roles.

---

## 2. Architectural Principles

1. Agents are defined by objectives, constraints, inputs, tools, state, and evaluation.
2. Personas, roles, or styles MAY exist only as aliases; they MUST NOT define behavior.
3. The system MUST be auditable, reproducible, and comparable across experiments.
4. Research velocity MUST NOT compromise experimental rigor.

---

## 3. Plane Separation

### 3.1 Project Data Plane
- Contains research artifacts, experiments, tasks, runs, and reports.
- Mutable only within explicitly scoped experiment capsules.
- Subject to immutability rules after run completion.

### 3.2 SELF Control Plane
- Contains agent execution logic, skills, workflows, evaluators, and logs.
- This project MUST NOT modify SELF foundational files.
- Interaction occurs only through declared workflows and skills.

---

## 4. Repository Structure

```

/
├── harness/
│   ├── agents/
│   ├── evaluators/
│   ├── workflows/
│   ├── schemas/
│   └── skills/
│
├── experiments/
│   └── exp-001-role-vs-goal/
│       ├── research.md
│       ├── tasks/
│       ├── variants/
│       ├── runs/
│       └── report/
│
├── results/
│
└── project/
└── init.md

```

- `harness/` is the single canonical instrumentation layer.
- `experiments/` contains isolated experiment capsules.
- `results/` contains cross-experiment synthesis only.
- No experiment may duplicate or redefine harness components.

---

## 5. Invariants (Non-Negotiable)

1. **Pinning**  
   Every run MUST pin:
   - harness version
   - evaluator versions
   - tool permission set

2. **Immutability**  
   Completed runs are immutable. Corrections require new runs.

3. **Append-Only Logs**  
   All run summaries and violations are appended; never overwritten.

4. **Scoped Writes**  
   Agents may write only to:
   - the active experiment’s run directory
   - designated scratch space (if explicitly allowed)

5. **Separation of Duties**  
   - Orchestrators do not execute tasks.
   - Executors do not evaluate results.
   - Evaluators do not mutate project state.

---

## 6. Harness Responsibilities

The harness is responsible for:
- Agent specification loading
- Workflow execution
- Tool permission enforcement
- Run materialization
- Evaluation dispatch
- Log emission

The harness MUST remain paradigm-agnostic.

---

## 7. Experiment Capsule Contract

Each experiment MUST:
- Be self-contained within its folder
- Declare hypotheses and metrics before execution
- Reference (not copy) harness components
- Store all outputs under its `runs/` directory
- Be reproducible via pinned manifests

---

## 8. Initial Experiment

### Identifier
`exp-001-role-vs-goal`

### Objective
Compare role-centric agent specifications against goal-centric agent specifications across identical tasks, tools, constraints, and evaluation criteria.

### Variable
Agent specification paradigm only.

### Fixed
- Task suite
- Tool access
- Constraints
- Evaluators
- Harness version (per run)

---

## 9. Workflows

The project defines the following mandatory workflows:

1. **bootstrap**
   - Initialize harness and experiment scaffolding

2. **pin-and-run**
   - Create run manifest
   - Snapshot inputs
   - Execute paired variants
   - Dispatch evaluations

3. **replay**
   - Reproduce a run from its manifest

4. **synthesize**
   - Aggregate results
   - Produce experiment and cross-experiment reports

---

## 10. Logging Rules

- All runs MUST emit a structured run manifest.
- All evaluations MUST emit a scorecard with rationale.
- All violations MUST be recorded explicitly.
- Silence is considered a failure mode.

---

## 11. Termination Conditions

The project is considered complete when:
- The initial experiment has ≥10 paired runs
- All runs are reproducible within declared tolerances
- A comparative report is generated
- Design recommendations are derived from evidence, not narrative

---

## 12. Closing Clause

This project treats agents as executable control structures.
Human metaphors are conveniences, not foundations.
Correctness, constraint adherence, and auditability take precedence over style.

END OF MANIFEST

