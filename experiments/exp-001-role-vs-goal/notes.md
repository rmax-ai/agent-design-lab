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
