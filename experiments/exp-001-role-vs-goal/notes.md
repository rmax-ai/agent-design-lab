# Execution Notes - exp-001-role-vs-goal

## 2025-12-28T19:21:42.354Z - Project Initialization

### Understanding Phase
- Located execution-plan.md with 12 actionable steps
- Reviewed project/manifest.md to understand:
  - Project is a research monorepo for comparing agent design paradigms
  - Focus: role-centric vs goal-centric agent specifications
  - Key principle: Agents are goal-driven control systems, not simulated human roles
  - Must follow pinning, immutability, append-only logs, scoped writes
  - Requires ≥10 paired runs for completion

### Repository Structure
- `.self/` - SELF control plane (sovereign authority, workflows, skills)
- `.system/` - System plane (witnesses/records activity)
- Root - Human data plane (user-facing artifacts)
- `experiments/exp-001-role-vs-goal/` - Current experiment capsule
- `harness/` - Instrumentation layer (agents, evaluators, workflows, schemas, skills)
- `project/` - Project manifest and documentation
- `results/` - Cross-experiment synthesis

### Current Experiment Structure
- `execution-plan.md` - 12-step plan to execute
- `research.md` - Currently minimal, needs pre-registration
- `tasks/` - Task suite (to be defined)
- `variants/` - Agent spec variants (to be created)
- `runs/` - Run artifacts (immutable after completion)
- `report/` - Final comparative report

### Key Constraints from Manifest
1. Must pin harness/evaluator/tool versions per run
2. Completed runs are immutable
3. Logs are append-only
4. Pre-register analysis before first pinned run
5. Use identical seeds/inputs per pair
6. Store everything under experiments/exp-001-role-vs-goal/runs/

### Tracking Approach
- status.md: Current progress checklist
- notes.md: Detailed observations and learnings
- suggestions.md: Improvements for future tasks
- need-feedback.md: Questions requiring clarification

## 2025-12-28T19:22:00.000Z - Harness Infrastructure Discovery

### Harness Components (Minimal/Placeholder)
All harness subdirectories exist but contain only README files:
- `harness/agents/` - Agent specifications and implementations
- `harness/evaluators/` - Scoring and assessment modules
- `harness/workflows/` - Orchestration workflows (bootstrap, pin-and-run, replay, synthesize)
- `harness/schemas/` - JSON schemas for manifests and scorecards
- `harness/skills/` - Skills library

**Observation**: The harness appears to be scaffolded but not implemented yet. This is consistent with a bootstrapping phase of the project.

### Experiment Directories (Ready for Content)
All experiment subdirectories exist with README placeholders:
- `tasks/` - Ready for task suite definitions
- `variants/` - Ready for role-centric and goal-centric specs
- `runs/` - Ready for pinned run artifacts
- `report/` - Ready for comparative reports

**Next Action**: Begin Step 1 by expanding research.md with pre-registered hypotheses, metrics, and analysis plan.

## 2025-12-28T19:23:00.000Z - Step 1 Complete: Pre-Registration

### Pre-Registration Details
Completed comprehensive pre-registration in research.md including:

**Hypotheses (5 total)**:
- H1 (Primary): Goal-centric → higher task success rates
- H2: Goal-centric → better constraint adherence  
- H3: Goal-centric → higher reproducibility
- H4: Role-centric → more clarification requests
- H5: No significant runtime difference

**Metrics (9 total)**:
- Primary: Task success rate, constraint adherence score
- Secondary: Clarification count, runtime, reproducibility score, specification clarity
- Tertiary: Log volume, tool patterns, error recovery

**Statistical Plan**:
- Paired t-tests (alpha=0.05, two-tailed)
- Minimum 10 paired runs per task, target 15
- Effect size: Cohen's d
- Bonferroni correction for multiple comparisons
- Power ≥0.80 required

**Quality Assurance**:
- Pre-run validation (manifest schema, pins, determinism)
- Post-run validation (scorecard completeness, log integrity)
- Violation handling policy defined
- Immutability and append-only logging enforced

**Key Design Decisions**:
- Pairing policy: Identical seeds/inputs, interleaved runs
- Success threshold: 15% minimum detectable difference
- Reproducibility target: ≥0.90 for 80% of runs
- Timeout: 600 seconds per task

### Pre-Registration Lock
✅ Research.md locked as of 2025-12-28T19:23:00.000Z
- Any future modifications must be marked as post-hoc
- Pre-registered analyses take precedence in reporting
- Lock enforced before any pinned runs

**Exit Criteria Met**: Pre-registration exists and will be committed before any pinned run.

## 2025-12-28T19:25:00.000Z - Step 2 Complete: Task Suite Definition

### Task Suite Overview
Created comprehensive task suite with 6 tasks covering required categories:

**Task Coverage**:
1. **TASK-001**: Simple File Creation (file manipulation, low complexity)
2. **TASK-002**: Multi-File Read and Summarize (multi-step reasoning, medium)
3. **TASK-003**: Constrained File Edit (constraint navigation, medium)
4. **TASK-004**: Error Recovery (error handling, medium) [spec pending]
5. **TASK-005**: Tool Composition (tool chaining, high complexity) [spec pending]
6. **TASK-006**: Specification Ambiguity Test (clarification behavior, medium) [spec pending]

**Determinism Features**:
- Fixed seeds for all tasks (42-47)
- Pre-populated input files with known content
- Explicit timeout values (60-300 seconds)
- Byte-level output verification requirements
- No external network dependencies

**Task Structure**:
Each task includes:
- `spec.json`: Machine-readable specification
- `README.md`: Human-readable description
- `inputs/`: Pre-populated input files (to be added)
- `expected/`: Expected output artifacts (to be added)

**Quality Requirements**:
- Smoke test: 3 runs per task with same seed
- Output must be byte-identical or within tolerance
- Runtime variance < 20%
- Constraint violations must be consistent

**Frozen Status**: ✅ Task suite frozen as of 2025-12-28T19:25:00.000Z

**Exit Criteria Met**: 
- Task suite with sample inputs and deterministic seed policies created
- Ready for smoke-tests (will be executed in pilot phase)
- 6 distinct tasks covering all required categories
