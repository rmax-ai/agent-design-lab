# Full Runs Execution Plan - exp-001-role-vs-goal

**Version**: 1.0  
**Date**: 2025-12-28  
**Status**: Design complete, execution pending harness implementation

---

## Overview

Execute ≥10 paired runs across the full task suite, following validated pilot workflow.

**Prerequisites**: Pilot runs completed successfully with no critical issues.

---

## Execution Strategy

### Full Task Coverage

Execute all 6 tasks from task suite:
- TASK-001: Simple File Creation
- TASK-002: Multi-File Read and Summarize
- TASK-003: Constrained File Edit
- TASK-004: Error Recovery
- TASK-005: Tool Composition
- TASK-006: Specification Ambiguity Test

### Sample Size per Task

**Target**: 15 paired runs per task (30 total runs per task)
- Minimum: 10 paired runs per task (per pre-registration)
- Buffer: 5 additional pairs for robustness and potential exclusions

**Total Runs**: 6 tasks × 15 pairs × 2 variants = **180 runs**

### Run Scheduling

**Temporal Interleaving**:
- Randomize variant order within each pair
- Don't batch all role-centric, then all goal-centric
- Example schedule:
  ```
  Pair 1:  G, R
  Pair 2:  R, G
  Pair 3:  G, R
  Pair 4:  R, G
  ... (randomized pattern)
  ```

**Task Interleaving**:
- Don't complete all runs for TASK-001 before starting TASK-002
- Rotate through tasks to minimize temporal confounds
- Example rotation: T1, T2, T3, T4, T5, T6, T1, T2, ...

### Execution Workflow (per run)

```bash
# 1. Initialize run
./harness/workflows/pin-and-run --init \
  --experiment exp-001-role-vs-goal \
  --variant {role-centric|goal-centric} \
  --task {TASK-00X} \
  --seed {42-47} \
  --pair-id {pair-NNNN} \
  --output runs/run-{timestamp}-{variant}-{task}/

# 2. Validate manifest
./harness/workflows/validate-manifest.py \
  runs/run-{id}/manifest.json

# 3. Execute agent
./harness/workflows/pin-and-run --execute \
  --manifest runs/run-{id}/manifest.json

# 4. Evaluate run
./harness/workflows/evaluate.py \
  --manifest runs/run-{id}/manifest.json

# 5. Lock run
./harness/workflows/lock-run.sh \
  runs/run-{id}/manifest.json

# 6. Log to run registry
echo "{run_id},{variant},{task},{timestamp},{status}" >> runs/registry.csv
```

---

## Quality Assurance During Execution

### Real-Time Checks (Step 8)

After each run:

**1. Manifest Validation**
- Schema compliance
- Pin consistency
- Hash integrity

**2. Scorecard Validation**
- All metrics present
- Values in expected ranges
- No null/undefined values

**3. Constraint Violation Check**
- Review scorecard constraint adherence score
- If score < 100, log violation details
- Determine if violation is critical (halt) or acceptable (document)

**4. Pairing Verification**
- Paired runs have identical inputs (hash check)
- Paired runs have identical seeds
- Paired runs differ only in variant

**5. Completion Tracking**
- Update progress in runs/progress.csv
- Mark pairs as complete
- Track remaining pairs per task

### Violation Handling

**Critical Violations** (halt experiment):
- Harness failure (crash, corruption)
- Reproducibility failure (identical inputs → different outputs, consistently)
- Security breach (unauthorized file access outside scope)
- Data loss (run artifacts lost or corrupted)

**Non-Critical Violations** (document and continue):
- Single run timeout (agent didn't complete within limit)
- Single clarification anomaly (unexpected count)
- Minor logging gaps (recoverable from context)

**Remediation Actions**:
- Critical: Fix issue, re-run affected pairs, document in violations.log
- Non-critical: Document in violations.log, continue, may exclude from analysis

### Progress Tracking

**runs/progress.csv**:
```csv
task_id,pair_id,run_id_role,run_id_goal,status,completed_at
TASK-001,pair-0001,run-001a,run-001b,complete,2025-12-28T19:00:00Z
TASK-001,pair-0002,run-002a,run-002b,complete,2025-12-28T19:05:00Z
...
```

**runs/violations.log** (append-only):
```
[2025-12-28T19:10:00Z] CRITICAL: run-003a manifest validation failed - missing evaluator pin
  Action: Fixed manifest template, re-ran as run-003a-v2
  Status: Resolved

[2025-12-28T19:20:00Z] NON-CRITICAL: run-005b timeout reached (600s)
  Action: Documented, included in analysis with timeout flag
  Status: Noted
```

---

## Data Management

### Run Directory Structure

```
experiments/exp-001-role-vs-goal/runs/
  registry.csv               # Master run registry
  progress.csv               # Execution progress
  violations.log             # Append-only violation log
  
  run-{timestamp}-{variant}-{task}/
    manifest.json
    agent.log
    outputs/
      {task-specific-files}
    scorecard.json
    evaluation.log
  
  ... (180 run directories)
```

### Storage Requirements

**Per-Run Estimate**:
- Manifest: ~5 KB
- Agent log: ~50-500 KB (varies by task complexity)
- Outputs: ~10-1000 KB (varies by task)
- Scorecard: ~10 KB
- Evaluation log: ~20 KB

**Total Estimate**: 180 runs × ~500 KB avg = ~90 MB

**Backup Strategy**:
- Incremental backup after each task completion
- Full backup after pilot and after full runs
- Store in results/ or external archive

---

## Automation Considerations

### Batch Execution Script

```bash
#!/bin/bash
# execute-full-runs.sh
# Automates execution of all paired runs

EXPERIMENT="exp-001-role-vs-goal"
TASKS=("TASK-001" "TASK-002" "TASK-003" "TASK-004" "TASK-005" "TASK-006")
PAIRS_PER_TASK=15
VARIANTS=("role-centric" "goal-centric")

for task in "${TASKS[@]}"; do
  for pair_num in $(seq 1 $PAIRS_PER_TASK); do
    # Randomize variant order
    if [ $((RANDOM % 2)) -eq 0 ]; then
      first="role-centric"
      second="goal-centric"
    else
      first="goal-centric"
      second="role-centric"
    fi
    
    pair_id="pair-$(printf '%04d' $((task_num * 100 + pair_num)))"
    
    # Execute first variant
    ./harness/workflows/pin-and-run --full \
      --experiment $EXPERIMENT \
      --variant $first \
      --task $task \
      --pair-id $pair_id
    
    # Execute second variant
    ./harness/workflows/pin-and-run --full \
      --experiment $EXPERIMENT \
      --variant $second \
      --task $task \
      --pair-id $pair_id
    
    # Verify pairing
    ./harness/workflows/verify-pairing.py \
      --pair-id $pair_id
  done
done

echo "Full runs complete"
```

### Monitoring Dashboard

**Optional**: Real-time execution monitoring
- Progress bar: N/180 runs complete
- Current task and pair
- Recent violations
- Estimated time remaining
- Success rate by variant (early indicator)

---

## Exit Criteria

From execution-plan.md Step 7:
- ✅ ≥10 paired runs per task (target: 15)
- ✅ Runs materialized in runs/
- ✅ All runs validated and immutable
- ✅ Progress tracking complete
- ✅ Violation log maintained

**Ready for**: Step 9 (Aggregate & Analyze Results)

---

**Status**: Plan ready, execution pending harness implementation  
**Version**: 1.0  
**Created**: 2025-12-28T19:32:00.000Z
